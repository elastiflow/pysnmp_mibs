# SNMP MIB module (CISCO-FIREPOWER-AP-COMPUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-COMPUTE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:13 2025
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

(CfprApComputeABoardPower,
 CfprApComputeAdminLinkAggregation,
 CfprApComputeAdminMemoryState,
 CfprApComputeAdminPowerState,
 CfprApComputeAdminState,
 CfprApComputeAdminTrigger,
 CfprApComputeAlarmSeverity,
 CfprApComputeAssociation,
 CfprApComputeAvailability,
 CfprApComputeBlackListing,
 CfprApComputeBladeFsmCurrentFsm,
 CfprApComputeBladeFsmStageName,
 CfprApComputeBladeFsmTaskFlags,
 CfprApComputeBladeFsmTaskItem,
 CfprApComputeBladeSlotId,
 CfprApComputeChassisConnPolicyChassisId,
 CfprApComputeChassisDiscAction,
 CfprApComputeChassisQualMaxId,
 CfprApComputeChassisQualMinId,
 CfprApComputeCheckPoint,
 CfprApComputeConnectivityRebalancing,
 CfprApComputeDiscovery,
 CfprApComputeIOHubEnvStatsHistThresholded,
 CfprApComputeIOHubEnvStatsThresholded,
 CfprApComputeIssues,
 CfprApComputeLinkAggregation,
 CfprApComputeMbPowerStatsHistThresholded,
 CfprApComputeMbPowerStatsThresholded,
 CfprApComputeMbTempStatsHistThresholded,
 CfprApComputeMbTempStatsThresholded,
 CfprApComputeMemoryUnitConstraintType,
 CfprApComputeMode,
 CfprApComputeOwner,
 CfprApComputePCIeFatalCompletionStatsThresholded,
 CfprApComputePCIeFatalProtocolStatsThresholded,
 CfprApComputePCIeFatalReceiveStatsThresholded,
 CfprApComputePCIeFatalStatsThresholded,
 CfprApComputePciCapOrder,
 CfprApComputePhysicalFsmCurrentFsm,
 CfprApComputePhysicalFsmStageName,
 CfprApComputePhysicalFsmTaskItem,
 CfprApComputePhysicalLowVoltageMemory,
 CfprApComputePooledRackUnitId,
 CfprApComputePooledSlotSlotId,
 CfprApComputePsuClusterState,
 CfprApComputePsuControlRedundancy,
 CfprApComputePsuRedundancy,
 CfprApComputePsuRedundancyOperQualifier,
 CfprApComputePsuRedundancyOperState,
 CfprApComputeRackQualMaxId,
 CfprApComputeRackQualMinId,
 CfprApComputeRackUnitFsmCurrentFsm,
 CfprApComputeRackUnitFsmStageName,
 CfprApComputeRackUnitId,
 CfprApComputeRackUnitMbTempStatsHistThresholded,
 CfprApComputeRackUnitMbTempStatsThresholded,
 CfprApComputeScrubAction,
 CfprApComputeServerDiscPolicyFsmCurrentFsm,
 CfprApComputeServerDiscPolicyFsmStageName,
 CfprApComputeServerDiscPolicyFsmTaskItem,
 CfprApComputeServerMgmtDiscAction,
 CfprApComputeSlotQualMaxId,
 CfprApComputeSlotQualMinId,
 CfprApComputeUpgradeStatus,
 CfprApConditionRemoteInvRslt,
 CfprApEquipmentBoardAggregationRole,
 CfprApEquipmentBoardConnectorType,
 CfprApEquipmentConnectionStatus,
 CfprApEquipmentCpuType,
 CfprApEquipmentOperability,
 CfprApEquipmentPowerState,
 CfprApEquipmentPresence,
 CfprApEquipmentSensorThresholdStatus,
 CfprApEquipmentSlotStatus,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApLsOperState,
 CfprApNetworkSwitchId,
 CfprApPolicyPolicyOwner,
 CfprApPoolPoolAssignmentOrder,
 CfprApTrigAckChangeDetails,
 CfprApTrigAckChanges,
 CfprApTrigAckDisr,
 CfprApTrigAckOperState,
 CfprApTrigAckPrevOperState,
 CfprApTrigAdminState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApComputeABoardPower",
    "CfprApComputeAdminLinkAggregation",
    "CfprApComputeAdminMemoryState",
    "CfprApComputeAdminPowerState",
    "CfprApComputeAdminState",
    "CfprApComputeAdminTrigger",
    "CfprApComputeAlarmSeverity",
    "CfprApComputeAssociation",
    "CfprApComputeAvailability",
    "CfprApComputeBlackListing",
    "CfprApComputeBladeFsmCurrentFsm",
    "CfprApComputeBladeFsmStageName",
    "CfprApComputeBladeFsmTaskFlags",
    "CfprApComputeBladeFsmTaskItem",
    "CfprApComputeBladeSlotId",
    "CfprApComputeChassisConnPolicyChassisId",
    "CfprApComputeChassisDiscAction",
    "CfprApComputeChassisQualMaxId",
    "CfprApComputeChassisQualMinId",
    "CfprApComputeCheckPoint",
    "CfprApComputeConnectivityRebalancing",
    "CfprApComputeDiscovery",
    "CfprApComputeIOHubEnvStatsHistThresholded",
    "CfprApComputeIOHubEnvStatsThresholded",
    "CfprApComputeIssues",
    "CfprApComputeLinkAggregation",
    "CfprApComputeMbPowerStatsHistThresholded",
    "CfprApComputeMbPowerStatsThresholded",
    "CfprApComputeMbTempStatsHistThresholded",
    "CfprApComputeMbTempStatsThresholded",
    "CfprApComputeMemoryUnitConstraintType",
    "CfprApComputeMode",
    "CfprApComputeOwner",
    "CfprApComputePCIeFatalCompletionStatsThresholded",
    "CfprApComputePCIeFatalProtocolStatsThresholded",
    "CfprApComputePCIeFatalReceiveStatsThresholded",
    "CfprApComputePCIeFatalStatsThresholded",
    "CfprApComputePciCapOrder",
    "CfprApComputePhysicalFsmCurrentFsm",
    "CfprApComputePhysicalFsmStageName",
    "CfprApComputePhysicalFsmTaskItem",
    "CfprApComputePhysicalLowVoltageMemory",
    "CfprApComputePooledRackUnitId",
    "CfprApComputePooledSlotSlotId",
    "CfprApComputePsuClusterState",
    "CfprApComputePsuControlRedundancy",
    "CfprApComputePsuRedundancy",
    "CfprApComputePsuRedundancyOperQualifier",
    "CfprApComputePsuRedundancyOperState",
    "CfprApComputeRackQualMaxId",
    "CfprApComputeRackQualMinId",
    "CfprApComputeRackUnitFsmCurrentFsm",
    "CfprApComputeRackUnitFsmStageName",
    "CfprApComputeRackUnitId",
    "CfprApComputeRackUnitMbTempStatsHistThresholded",
    "CfprApComputeRackUnitMbTempStatsThresholded",
    "CfprApComputeScrubAction",
    "CfprApComputeServerDiscPolicyFsmCurrentFsm",
    "CfprApComputeServerDiscPolicyFsmStageName",
    "CfprApComputeServerDiscPolicyFsmTaskItem",
    "CfprApComputeServerMgmtDiscAction",
    "CfprApComputeSlotQualMaxId",
    "CfprApComputeSlotQualMinId",
    "CfprApComputeUpgradeStatus",
    "CfprApConditionRemoteInvRslt",
    "CfprApEquipmentBoardAggregationRole",
    "CfprApEquipmentBoardConnectorType",
    "CfprApEquipmentConnectionStatus",
    "CfprApEquipmentCpuType",
    "CfprApEquipmentOperability",
    "CfprApEquipmentPowerState",
    "CfprApEquipmentPresence",
    "CfprApEquipmentSensorThresholdStatus",
    "CfprApEquipmentSlotStatus",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApLsOperState",
    "CfprApNetworkSwitchId",
    "CfprApPolicyPolicyOwner",
    "CfprApPoolPoolAssignmentOrder",
    "CfprApTrigAckChangeDetails",
    "CfprApTrigAckChanges",
    "CfprApTrigAckDisr",
    "CfprApTrigAckOperState",
    "CfprApTrigAckPrevOperState",
    "CfprApTrigAdminState")

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

cfprApComputeObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApComputeAutoconfigPolicyTable_Object = MibTable
cfprApComputeAutoconfigPolicyTable = _CfprApComputeAutoconfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicyTable.setStatus("current")
_CfprApComputeAutoconfigPolicyEntry_Object = MibTableRow
cfprApComputeAutoconfigPolicyEntry = _CfprApComputeAutoconfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1, 1)
)
cfprApComputeAutoconfigPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeAutoconfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicyEntry.setStatus("current")
_CfprApComputeAutoconfigPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApComputeAutoconfigPolicyInstanceId_Object = MibTableColumn
cfprApComputeAutoconfigPolicyInstanceId = _CfprApComputeAutoconfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1, 1, 1),
    _CfprApComputeAutoconfigPolicyInstanceId_Type()
)
cfprApComputeAutoconfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicyInstanceId.setStatus("current")
_CfprApComputeAutoconfigPolicyDn_Type = CfprApManagedObjectDn
_CfprApComputeAutoconfigPolicyDn_Object = MibTableColumn
cfprApComputeAutoconfigPolicyDn = _CfprApComputeAutoconfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1, 1, 2),
    _CfprApComputeAutoconfigPolicyDn_Type()
)
cfprApComputeAutoconfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicyDn.setStatus("current")
_CfprApComputeAutoconfigPolicyRn_Type = SnmpAdminString
_CfprApComputeAutoconfigPolicyRn_Object = MibTableColumn
cfprApComputeAutoconfigPolicyRn = _CfprApComputeAutoconfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1, 1, 3),
    _CfprApComputeAutoconfigPolicyRn_Type()
)
cfprApComputeAutoconfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicyRn.setStatus("current")
_CfprApComputeAutoconfigPolicyDescr_Type = SnmpAdminString
_CfprApComputeAutoconfigPolicyDescr_Object = MibTableColumn
cfprApComputeAutoconfigPolicyDescr = _CfprApComputeAutoconfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1, 1, 4),
    _CfprApComputeAutoconfigPolicyDescr_Type()
)
cfprApComputeAutoconfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicyDescr.setStatus("current")
_CfprApComputeAutoconfigPolicyDstDn_Type = SnmpAdminString
_CfprApComputeAutoconfigPolicyDstDn_Object = MibTableColumn
cfprApComputeAutoconfigPolicyDstDn = _CfprApComputeAutoconfigPolicyDstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1, 1, 5),
    _CfprApComputeAutoconfigPolicyDstDn_Type()
)
cfprApComputeAutoconfigPolicyDstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicyDstDn.setStatus("current")
_CfprApComputeAutoconfigPolicyIntId_Type = SnmpAdminString
_CfprApComputeAutoconfigPolicyIntId_Object = MibTableColumn
cfprApComputeAutoconfigPolicyIntId = _CfprApComputeAutoconfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1, 1, 6),
    _CfprApComputeAutoconfigPolicyIntId_Type()
)
cfprApComputeAutoconfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicyIntId.setStatus("current")
_CfprApComputeAutoconfigPolicyName_Type = SnmpAdminString
_CfprApComputeAutoconfigPolicyName_Object = MibTableColumn
cfprApComputeAutoconfigPolicyName = _CfprApComputeAutoconfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1, 1, 7),
    _CfprApComputeAutoconfigPolicyName_Type()
)
cfprApComputeAutoconfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicyName.setStatus("current")
_CfprApComputeAutoconfigPolicyPolicyLevel_Type = Gauge32
_CfprApComputeAutoconfigPolicyPolicyLevel_Object = MibTableColumn
cfprApComputeAutoconfigPolicyPolicyLevel = _CfprApComputeAutoconfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1, 1, 8),
    _CfprApComputeAutoconfigPolicyPolicyLevel_Type()
)
cfprApComputeAutoconfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicyPolicyLevel.setStatus("current")
_CfprApComputeAutoconfigPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeAutoconfigPolicyPolicyOwner_Object = MibTableColumn
cfprApComputeAutoconfigPolicyPolicyOwner = _CfprApComputeAutoconfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1, 1, 9),
    _CfprApComputeAutoconfigPolicyPolicyOwner_Type()
)
cfprApComputeAutoconfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicyPolicyOwner.setStatus("current")
_CfprApComputeAutoconfigPolicyQualifier_Type = SnmpAdminString
_CfprApComputeAutoconfigPolicyQualifier_Object = MibTableColumn
cfprApComputeAutoconfigPolicyQualifier = _CfprApComputeAutoconfigPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1, 1, 10),
    _CfprApComputeAutoconfigPolicyQualifier_Type()
)
cfprApComputeAutoconfigPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicyQualifier.setStatus("current")
_CfprApComputeAutoconfigPolicySrcTemplName_Type = SnmpAdminString
_CfprApComputeAutoconfigPolicySrcTemplName_Object = MibTableColumn
cfprApComputeAutoconfigPolicySrcTemplName = _CfprApComputeAutoconfigPolicySrcTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 1, 1, 11),
    _CfprApComputeAutoconfigPolicySrcTemplName_Type()
)
cfprApComputeAutoconfigPolicySrcTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeAutoconfigPolicySrcTemplName.setStatus("current")
_CfprApComputeBladeTable_Object = MibTable
cfprApComputeBladeTable = _CfprApComputeBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2)
)
if mibBuilder.loadTexts:
    cfprApComputeBladeTable.setStatus("current")
_CfprApComputeBladeEntry_Object = MibTableRow
cfprApComputeBladeEntry = _CfprApComputeBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1)
)
cfprApComputeBladeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeBladeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeBladeEntry.setStatus("current")
_CfprApComputeBladeInstanceId_Type = CfprApManagedObjectId
_CfprApComputeBladeInstanceId_Object = MibTableColumn
cfprApComputeBladeInstanceId = _CfprApComputeBladeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 1),
    _CfprApComputeBladeInstanceId_Type()
)
cfprApComputeBladeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeBladeInstanceId.setStatus("current")
_CfprApComputeBladeDn_Type = CfprApManagedObjectDn
_CfprApComputeBladeDn_Object = MibTableColumn
cfprApComputeBladeDn = _CfprApComputeBladeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 2),
    _CfprApComputeBladeDn_Type()
)
cfprApComputeBladeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDn.setStatus("current")
_CfprApComputeBladeRn_Type = SnmpAdminString
_CfprApComputeBladeRn_Object = MibTableColumn
cfprApComputeBladeRn = _CfprApComputeBladeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 3),
    _CfprApComputeBladeRn_Type()
)
cfprApComputeBladeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeRn.setStatus("current")
_CfprApComputeBladeAdminPower_Type = CfprApComputeAdminPowerState
_CfprApComputeBladeAdminPower_Object = MibTableColumn
cfprApComputeBladeAdminPower = _CfprApComputeBladeAdminPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 4),
    _CfprApComputeBladeAdminPower_Type()
)
cfprApComputeBladeAdminPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeAdminPower.setStatus("current")
_CfprApComputeBladeAdminState_Type = CfprApComputeAdminState
_CfprApComputeBladeAdminState_Object = MibTableColumn
cfprApComputeBladeAdminState = _CfprApComputeBladeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 5),
    _CfprApComputeBladeAdminState_Type()
)
cfprApComputeBladeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeAdminState.setStatus("current")
_CfprApComputeBladeAssignedToDn_Type = SnmpAdminString
_CfprApComputeBladeAssignedToDn_Object = MibTableColumn
cfprApComputeBladeAssignedToDn = _CfprApComputeBladeAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 6),
    _CfprApComputeBladeAssignedToDn_Type()
)
cfprApComputeBladeAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeAssignedToDn.setStatus("current")
_CfprApComputeBladeAssociation_Type = CfprApComputeAssociation
_CfprApComputeBladeAssociation_Object = MibTableColumn
cfprApComputeBladeAssociation = _CfprApComputeBladeAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 7),
    _CfprApComputeBladeAssociation_Type()
)
cfprApComputeBladeAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeAssociation.setStatus("current")
_CfprApComputeBladeAvailability_Type = CfprApComputeAvailability
_CfprApComputeBladeAvailability_Object = MibTableColumn
cfprApComputeBladeAvailability = _CfprApComputeBladeAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 8),
    _CfprApComputeBladeAvailability_Type()
)
cfprApComputeBladeAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeAvailability.setStatus("current")
_CfprApComputeBladeAvailableMemory_Type = Gauge32
_CfprApComputeBladeAvailableMemory_Object = MibTableColumn
cfprApComputeBladeAvailableMemory = _CfprApComputeBladeAvailableMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 9),
    _CfprApComputeBladeAvailableMemory_Type()
)
cfprApComputeBladeAvailableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeAvailableMemory.setStatus("current")
_CfprApComputeBladeChassisId_Type = Gauge32
_CfprApComputeBladeChassisId_Object = MibTableColumn
cfprApComputeBladeChassisId = _CfprApComputeBladeChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 10),
    _CfprApComputeBladeChassisId_Type()
)
cfprApComputeBladeChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeChassisId.setStatus("current")
_CfprApComputeBladeCheckPoint_Type = CfprApComputeCheckPoint
_CfprApComputeBladeCheckPoint_Object = MibTableColumn
cfprApComputeBladeCheckPoint = _CfprApComputeBladeCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 11),
    _CfprApComputeBladeCheckPoint_Type()
)
cfprApComputeBladeCheckPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeCheckPoint.setStatus("current")
_CfprApComputeBladeConnPath_Type = CfprApEquipmentConnectionStatus
_CfprApComputeBladeConnPath_Object = MibTableColumn
cfprApComputeBladeConnPath = _CfprApComputeBladeConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 12),
    _CfprApComputeBladeConnPath_Type()
)
cfprApComputeBladeConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeConnPath.setStatus("current")
_CfprApComputeBladeConnStatus_Type = CfprApEquipmentConnectionStatus
_CfprApComputeBladeConnStatus_Object = MibTableColumn
cfprApComputeBladeConnStatus = _CfprApComputeBladeConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 13),
    _CfprApComputeBladeConnStatus_Type()
)
cfprApComputeBladeConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeConnStatus.setStatus("current")
_CfprApComputeBladeDescr_Type = SnmpAdminString
_CfprApComputeBladeDescr_Object = MibTableColumn
cfprApComputeBladeDescr = _CfprApComputeBladeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 14),
    _CfprApComputeBladeDescr_Type()
)
cfprApComputeBladeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDescr.setStatus("current")
_CfprApComputeBladeDiscovery_Type = CfprApComputeDiscovery
_CfprApComputeBladeDiscovery_Object = MibTableColumn
cfprApComputeBladeDiscovery = _CfprApComputeBladeDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 15),
    _CfprApComputeBladeDiscovery_Type()
)
cfprApComputeBladeDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscovery.setStatus("current")
_CfprApComputeBladeFltAggr_Type = Unsigned64
_CfprApComputeBladeFltAggr_Object = MibTableColumn
cfprApComputeBladeFltAggr = _CfprApComputeBladeFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 16),
    _CfprApComputeBladeFltAggr_Type()
)
cfprApComputeBladeFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFltAggr.setStatus("current")
_CfprApComputeBladeFsmDescr_Type = SnmpAdminString
_CfprApComputeBladeFsmDescr_Object = MibTableColumn
cfprApComputeBladeFsmDescr = _CfprApComputeBladeFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 17),
    _CfprApComputeBladeFsmDescr_Type()
)
cfprApComputeBladeFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmDescr.setStatus("current")
_CfprApComputeBladeFsmFlags_Type = SnmpAdminString
_CfprApComputeBladeFsmFlags_Object = MibTableColumn
cfprApComputeBladeFsmFlags = _CfprApComputeBladeFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 18),
    _CfprApComputeBladeFsmFlags_Type()
)
cfprApComputeBladeFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmFlags.setStatus("current")
_CfprApComputeBladeFsmPrev_Type = SnmpAdminString
_CfprApComputeBladeFsmPrev_Object = MibTableColumn
cfprApComputeBladeFsmPrev = _CfprApComputeBladeFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 19),
    _CfprApComputeBladeFsmPrev_Type()
)
cfprApComputeBladeFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmPrev.setStatus("current")
_CfprApComputeBladeFsmProgr_Type = Gauge32
_CfprApComputeBladeFsmProgr_Object = MibTableColumn
cfprApComputeBladeFsmProgr = _CfprApComputeBladeFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 20),
    _CfprApComputeBladeFsmProgr_Type()
)
cfprApComputeBladeFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmProgr.setStatus("current")
_CfprApComputeBladeFsmRmtInvErrCode_Type = Gauge32
_CfprApComputeBladeFsmRmtInvErrCode_Object = MibTableColumn
cfprApComputeBladeFsmRmtInvErrCode = _CfprApComputeBladeFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 21),
    _CfprApComputeBladeFsmRmtInvErrCode_Type()
)
cfprApComputeBladeFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmRmtInvErrCode.setStatus("current")
_CfprApComputeBladeFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApComputeBladeFsmRmtInvErrDescr_Object = MibTableColumn
cfprApComputeBladeFsmRmtInvErrDescr = _CfprApComputeBladeFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 22),
    _CfprApComputeBladeFsmRmtInvErrDescr_Type()
)
cfprApComputeBladeFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmRmtInvErrDescr.setStatus("current")
_CfprApComputeBladeFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApComputeBladeFsmRmtInvRslt_Object = MibTableColumn
cfprApComputeBladeFsmRmtInvRslt = _CfprApComputeBladeFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 23),
    _CfprApComputeBladeFsmRmtInvRslt_Type()
)
cfprApComputeBladeFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmRmtInvRslt.setStatus("current")
_CfprApComputeBladeFsmStageDescr_Type = SnmpAdminString
_CfprApComputeBladeFsmStageDescr_Object = MibTableColumn
cfprApComputeBladeFsmStageDescr = _CfprApComputeBladeFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 24),
    _CfprApComputeBladeFsmStageDescr_Type()
)
cfprApComputeBladeFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStageDescr.setStatus("current")
_CfprApComputeBladeFsmStamp_Type = DateAndTime
_CfprApComputeBladeFsmStamp_Object = MibTableColumn
cfprApComputeBladeFsmStamp = _CfprApComputeBladeFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 25),
    _CfprApComputeBladeFsmStamp_Type()
)
cfprApComputeBladeFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStamp.setStatus("current")
_CfprApComputeBladeFsmStatus_Type = SnmpAdminString
_CfprApComputeBladeFsmStatus_Object = MibTableColumn
cfprApComputeBladeFsmStatus = _CfprApComputeBladeFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 26),
    _CfprApComputeBladeFsmStatus_Type()
)
cfprApComputeBladeFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStatus.setStatus("current")
_CfprApComputeBladeFsmTry_Type = Gauge32
_CfprApComputeBladeFsmTry_Object = MibTableColumn
cfprApComputeBladeFsmTry = _CfprApComputeBladeFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 27),
    _CfprApComputeBladeFsmTry_Type()
)
cfprApComputeBladeFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmTry.setStatus("current")
_CfprApComputeBladeIntId_Type = SnmpAdminString
_CfprApComputeBladeIntId_Object = MibTableColumn
cfprApComputeBladeIntId = _CfprApComputeBladeIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 28),
    _CfprApComputeBladeIntId_Type()
)
cfprApComputeBladeIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeIntId.setStatus("current")
_CfprApComputeBladeLc_Type = CfprApComputeAdminTrigger
_CfprApComputeBladeLc_Object = MibTableColumn
cfprApComputeBladeLc = _CfprApComputeBladeLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 29),
    _CfprApComputeBladeLc_Type()
)
cfprApComputeBladeLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeLc.setStatus("current")
_CfprApComputeBladeLcTs_Type = DateAndTime
_CfprApComputeBladeLcTs_Object = MibTableColumn
cfprApComputeBladeLcTs = _CfprApComputeBladeLcTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 30),
    _CfprApComputeBladeLcTs_Type()
)
cfprApComputeBladeLcTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeLcTs.setStatus("current")
_CfprApComputeBladeLocalId_Type = SnmpAdminString
_CfprApComputeBladeLocalId_Object = MibTableColumn
cfprApComputeBladeLocalId = _CfprApComputeBladeLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 31),
    _CfprApComputeBladeLocalId_Type()
)
cfprApComputeBladeLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeLocalId.setStatus("current")
_CfprApComputeBladeLowVoltageMemory_Type = CfprApComputePhysicalLowVoltageMemory
_CfprApComputeBladeLowVoltageMemory_Object = MibTableColumn
cfprApComputeBladeLowVoltageMemory = _CfprApComputeBladeLowVoltageMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 32),
    _CfprApComputeBladeLowVoltageMemory_Type()
)
cfprApComputeBladeLowVoltageMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeLowVoltageMemory.setStatus("current")
_CfprApComputeBladeManagingInst_Type = CfprApNetworkSwitchId
_CfprApComputeBladeManagingInst_Object = MibTableColumn
cfprApComputeBladeManagingInst = _CfprApComputeBladeManagingInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 33),
    _CfprApComputeBladeManagingInst_Type()
)
cfprApComputeBladeManagingInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeManagingInst.setStatus("current")
_CfprApComputeBladeMemorySpeed_Type = Gauge32
_CfprApComputeBladeMemorySpeed_Object = MibTableColumn
cfprApComputeBladeMemorySpeed = _CfprApComputeBladeMemorySpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 34),
    _CfprApComputeBladeMemorySpeed_Type()
)
cfprApComputeBladeMemorySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeMemorySpeed.setStatus("current")
_CfprApComputeBladeMfgTime_Type = DateAndTime
_CfprApComputeBladeMfgTime_Object = MibTableColumn
cfprApComputeBladeMfgTime = _CfprApComputeBladeMfgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 35),
    _CfprApComputeBladeMfgTime_Type()
)
cfprApComputeBladeMfgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeMfgTime.setStatus("current")
_CfprApComputeBladeModel_Type = SnmpAdminString
_CfprApComputeBladeModel_Object = MibTableColumn
cfprApComputeBladeModel = _CfprApComputeBladeModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 36),
    _CfprApComputeBladeModel_Type()
)
cfprApComputeBladeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeModel.setStatus("current")
_CfprApComputeBladeName_Type = SnmpAdminString
_CfprApComputeBladeName_Object = MibTableColumn
cfprApComputeBladeName = _CfprApComputeBladeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 37),
    _CfprApComputeBladeName_Type()
)
cfprApComputeBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeName.setStatus("current")
_CfprApComputeBladeNumOfAdaptors_Type = Gauge32
_CfprApComputeBladeNumOfAdaptors_Object = MibTableColumn
cfprApComputeBladeNumOfAdaptors = _CfprApComputeBladeNumOfAdaptors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 38),
    _CfprApComputeBladeNumOfAdaptors_Type()
)
cfprApComputeBladeNumOfAdaptors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeNumOfAdaptors.setStatus("current")
_CfprApComputeBladeNumOfCores_Type = Gauge32
_CfprApComputeBladeNumOfCores_Object = MibTableColumn
cfprApComputeBladeNumOfCores = _CfprApComputeBladeNumOfCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 39),
    _CfprApComputeBladeNumOfCores_Type()
)
cfprApComputeBladeNumOfCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeNumOfCores.setStatus("current")
_CfprApComputeBladeNumOfCoresEnabled_Type = Gauge32
_CfprApComputeBladeNumOfCoresEnabled_Object = MibTableColumn
cfprApComputeBladeNumOfCoresEnabled = _CfprApComputeBladeNumOfCoresEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 40),
    _CfprApComputeBladeNumOfCoresEnabled_Type()
)
cfprApComputeBladeNumOfCoresEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeNumOfCoresEnabled.setStatus("current")
_CfprApComputeBladeNumOfCpus_Type = Gauge32
_CfprApComputeBladeNumOfCpus_Object = MibTableColumn
cfprApComputeBladeNumOfCpus = _CfprApComputeBladeNumOfCpus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 41),
    _CfprApComputeBladeNumOfCpus_Type()
)
cfprApComputeBladeNumOfCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeNumOfCpus.setStatus("current")
_CfprApComputeBladeNumOfEthHostIfs_Type = Gauge32
_CfprApComputeBladeNumOfEthHostIfs_Object = MibTableColumn
cfprApComputeBladeNumOfEthHostIfs = _CfprApComputeBladeNumOfEthHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 42),
    _CfprApComputeBladeNumOfEthHostIfs_Type()
)
cfprApComputeBladeNumOfEthHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeNumOfEthHostIfs.setStatus("current")
_CfprApComputeBladeNumOfFcHostIfs_Type = Gauge32
_CfprApComputeBladeNumOfFcHostIfs_Object = MibTableColumn
cfprApComputeBladeNumOfFcHostIfs = _CfprApComputeBladeNumOfFcHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 43),
    _CfprApComputeBladeNumOfFcHostIfs_Type()
)
cfprApComputeBladeNumOfFcHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeNumOfFcHostIfs.setStatus("current")
_CfprApComputeBladeNumOfThreads_Type = Gauge32
_CfprApComputeBladeNumOfThreads_Object = MibTableColumn
cfprApComputeBladeNumOfThreads = _CfprApComputeBladeNumOfThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 44),
    _CfprApComputeBladeNumOfThreads_Type()
)
cfprApComputeBladeNumOfThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeNumOfThreads.setStatus("current")
_CfprApComputeBladeOperPower_Type = CfprApEquipmentPowerState
_CfprApComputeBladeOperPower_Object = MibTableColumn
cfprApComputeBladeOperPower = _CfprApComputeBladeOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 45),
    _CfprApComputeBladeOperPower_Type()
)
cfprApComputeBladeOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeOperPower.setStatus("current")
_CfprApComputeBladeOperQualifier_Type = CfprApComputeIssues
_CfprApComputeBladeOperQualifier_Object = MibTableColumn
cfprApComputeBladeOperQualifier = _CfprApComputeBladeOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 46),
    _CfprApComputeBladeOperQualifier_Type()
)
cfprApComputeBladeOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeOperQualifier.setStatus("current")
_CfprApComputeBladeOperState_Type = CfprApLsOperState
_CfprApComputeBladeOperState_Object = MibTableColumn
cfprApComputeBladeOperState = _CfprApComputeBladeOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 47),
    _CfprApComputeBladeOperState_Type()
)
cfprApComputeBladeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeOperState.setStatus("current")
_CfprApComputeBladeOperability_Type = CfprApEquipmentOperability
_CfprApComputeBladeOperability_Object = MibTableColumn
cfprApComputeBladeOperability = _CfprApComputeBladeOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 48),
    _CfprApComputeBladeOperability_Type()
)
cfprApComputeBladeOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeOperability.setStatus("current")
_CfprApComputeBladeOriginalUuid_Type = SnmpAdminString
_CfprApComputeBladeOriginalUuid_Object = MibTableColumn
cfprApComputeBladeOriginalUuid = _CfprApComputeBladeOriginalUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 49),
    _CfprApComputeBladeOriginalUuid_Type()
)
cfprApComputeBladeOriginalUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeOriginalUuid.setStatus("current")
_CfprApComputeBladePartNumber_Type = SnmpAdminString
_CfprApComputeBladePartNumber_Object = MibTableColumn
cfprApComputeBladePartNumber = _CfprApComputeBladePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 50),
    _CfprApComputeBladePartNumber_Type()
)
cfprApComputeBladePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladePartNumber.setStatus("current")
_CfprApComputeBladePolicyLevel_Type = Gauge32
_CfprApComputeBladePolicyLevel_Object = MibTableColumn
cfprApComputeBladePolicyLevel = _CfprApComputeBladePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 51),
    _CfprApComputeBladePolicyLevel_Type()
)
cfprApComputeBladePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladePolicyLevel.setStatus("current")
_CfprApComputeBladePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeBladePolicyOwner_Object = MibTableColumn
cfprApComputeBladePolicyOwner = _CfprApComputeBladePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 52),
    _CfprApComputeBladePolicyOwner_Type()
)
cfprApComputeBladePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladePolicyOwner.setStatus("current")
_CfprApComputeBladePresence_Type = CfprApEquipmentSlotStatus
_CfprApComputeBladePresence_Object = MibTableColumn
cfprApComputeBladePresence = _CfprApComputeBladePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 53),
    _CfprApComputeBladePresence_Type()
)
cfprApComputeBladePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladePresence.setStatus("current")
_CfprApComputeBladeRevision_Type = SnmpAdminString
_CfprApComputeBladeRevision_Object = MibTableColumn
cfprApComputeBladeRevision = _CfprApComputeBladeRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 54),
    _CfprApComputeBladeRevision_Type()
)
cfprApComputeBladeRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeRevision.setStatus("current")
_CfprApComputeBladeScaledMode_Type = CfprApComputeMode
_CfprApComputeBladeScaledMode_Object = MibTableColumn
cfprApComputeBladeScaledMode = _CfprApComputeBladeScaledMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 55),
    _CfprApComputeBladeScaledMode_Type()
)
cfprApComputeBladeScaledMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeScaledMode.setStatus("current")
_CfprApComputeBladeSerial_Type = SnmpAdminString
_CfprApComputeBladeSerial_Object = MibTableColumn
cfprApComputeBladeSerial = _CfprApComputeBladeSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 56),
    _CfprApComputeBladeSerial_Type()
)
cfprApComputeBladeSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeSerial.setStatus("current")
_CfprApComputeBladeServerId_Type = SnmpAdminString
_CfprApComputeBladeServerId_Object = MibTableColumn
cfprApComputeBladeServerId = _CfprApComputeBladeServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 57),
    _CfprApComputeBladeServerId_Type()
)
cfprApComputeBladeServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeServerId.setStatus("current")
_CfprApComputeBladeSlotId_Type = CfprApComputeBladeSlotId
_CfprApComputeBladeSlotId_Object = MibTableColumn
cfprApComputeBladeSlotId = _CfprApComputeBladeSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 58),
    _CfprApComputeBladeSlotId_Type()
)
cfprApComputeBladeSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeSlotId.setStatus("current")
_CfprApComputeBladeTotalMemory_Type = Gauge32
_CfprApComputeBladeTotalMemory_Object = MibTableColumn
cfprApComputeBladeTotalMemory = _CfprApComputeBladeTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 59),
    _CfprApComputeBladeTotalMemory_Type()
)
cfprApComputeBladeTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeTotalMemory.setStatus("current")
_CfprApComputeBladeUpgradeScenario_Type = CfprApComputeUpgradeStatus
_CfprApComputeBladeUpgradeScenario_Object = MibTableColumn
cfprApComputeBladeUpgradeScenario = _CfprApComputeBladeUpgradeScenario_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 60),
    _CfprApComputeBladeUpgradeScenario_Type()
)
cfprApComputeBladeUpgradeScenario.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeUpgradeScenario.setStatus("current")
_CfprApComputeBladeUsrLbl_Type = SnmpAdminString
_CfprApComputeBladeUsrLbl_Object = MibTableColumn
cfprApComputeBladeUsrLbl = _CfprApComputeBladeUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 61),
    _CfprApComputeBladeUsrLbl_Type()
)
cfprApComputeBladeUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeUsrLbl.setStatus("current")
_CfprApComputeBladeUuid_Type = SnmpAdminString
_CfprApComputeBladeUuid_Object = MibTableColumn
cfprApComputeBladeUuid = _CfprApComputeBladeUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 62),
    _CfprApComputeBladeUuid_Type()
)
cfprApComputeBladeUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeUuid.setStatus("current")
_CfprApComputeBladeVendor_Type = SnmpAdminString
_CfprApComputeBladeVendor_Object = MibTableColumn
cfprApComputeBladeVendor = _CfprApComputeBladeVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 63),
    _CfprApComputeBladeVendor_Type()
)
cfprApComputeBladeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeVendor.setStatus("current")
_CfprApComputeBladeVid_Type = SnmpAdminString
_CfprApComputeBladeVid_Object = MibTableColumn
cfprApComputeBladeVid = _CfprApComputeBladeVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 2, 1, 64),
    _CfprApComputeBladeVid_Type()
)
cfprApComputeBladeVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeVid.setStatus("current")
_CfprApComputeBladeDiscPolicyTable_Object = MibTable
cfprApComputeBladeDiscPolicyTable = _CfprApComputeBladeDiscPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3)
)
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyTable.setStatus("current")
_CfprApComputeBladeDiscPolicyEntry_Object = MibTableRow
cfprApComputeBladeDiscPolicyEntry = _CfprApComputeBladeDiscPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3, 1)
)
cfprApComputeBladeDiscPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeBladeDiscPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyEntry.setStatus("current")
_CfprApComputeBladeDiscPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApComputeBladeDiscPolicyInstanceId_Object = MibTableColumn
cfprApComputeBladeDiscPolicyInstanceId = _CfprApComputeBladeDiscPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3, 1, 1),
    _CfprApComputeBladeDiscPolicyInstanceId_Type()
)
cfprApComputeBladeDiscPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyInstanceId.setStatus("current")
_CfprApComputeBladeDiscPolicyDn_Type = CfprApManagedObjectDn
_CfprApComputeBladeDiscPolicyDn_Object = MibTableColumn
cfprApComputeBladeDiscPolicyDn = _CfprApComputeBladeDiscPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3, 1, 2),
    _CfprApComputeBladeDiscPolicyDn_Type()
)
cfprApComputeBladeDiscPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyDn.setStatus("current")
_CfprApComputeBladeDiscPolicyRn_Type = SnmpAdminString
_CfprApComputeBladeDiscPolicyRn_Object = MibTableColumn
cfprApComputeBladeDiscPolicyRn = _CfprApComputeBladeDiscPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3, 1, 3),
    _CfprApComputeBladeDiscPolicyRn_Type()
)
cfprApComputeBladeDiscPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyRn.setStatus("current")
_CfprApComputeBladeDiscPolicyAction_Type = SnmpAdminString
_CfprApComputeBladeDiscPolicyAction_Object = MibTableColumn
cfprApComputeBladeDiscPolicyAction = _CfprApComputeBladeDiscPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3, 1, 4),
    _CfprApComputeBladeDiscPolicyAction_Type()
)
cfprApComputeBladeDiscPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyAction.setStatus("current")
_CfprApComputeBladeDiscPolicyDescr_Type = SnmpAdminString
_CfprApComputeBladeDiscPolicyDescr_Object = MibTableColumn
cfprApComputeBladeDiscPolicyDescr = _CfprApComputeBladeDiscPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3, 1, 5),
    _CfprApComputeBladeDiscPolicyDescr_Type()
)
cfprApComputeBladeDiscPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyDescr.setStatus("current")
_CfprApComputeBladeDiscPolicyIntId_Type = SnmpAdminString
_CfprApComputeBladeDiscPolicyIntId_Object = MibTableColumn
cfprApComputeBladeDiscPolicyIntId = _CfprApComputeBladeDiscPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3, 1, 6),
    _CfprApComputeBladeDiscPolicyIntId_Type()
)
cfprApComputeBladeDiscPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyIntId.setStatus("current")
_CfprApComputeBladeDiscPolicyName_Type = SnmpAdminString
_CfprApComputeBladeDiscPolicyName_Object = MibTableColumn
cfprApComputeBladeDiscPolicyName = _CfprApComputeBladeDiscPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3, 1, 7),
    _CfprApComputeBladeDiscPolicyName_Type()
)
cfprApComputeBladeDiscPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyName.setStatus("current")
_CfprApComputeBladeDiscPolicyPolicyLevel_Type = Gauge32
_CfprApComputeBladeDiscPolicyPolicyLevel_Object = MibTableColumn
cfprApComputeBladeDiscPolicyPolicyLevel = _CfprApComputeBladeDiscPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3, 1, 8),
    _CfprApComputeBladeDiscPolicyPolicyLevel_Type()
)
cfprApComputeBladeDiscPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyPolicyLevel.setStatus("current")
_CfprApComputeBladeDiscPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeBladeDiscPolicyPolicyOwner_Object = MibTableColumn
cfprApComputeBladeDiscPolicyPolicyOwner = _CfprApComputeBladeDiscPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3, 1, 9),
    _CfprApComputeBladeDiscPolicyPolicyOwner_Type()
)
cfprApComputeBladeDiscPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyPolicyOwner.setStatus("current")
_CfprApComputeBladeDiscPolicyQualifier_Type = SnmpAdminString
_CfprApComputeBladeDiscPolicyQualifier_Object = MibTableColumn
cfprApComputeBladeDiscPolicyQualifier = _CfprApComputeBladeDiscPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3, 1, 10),
    _CfprApComputeBladeDiscPolicyQualifier_Type()
)
cfprApComputeBladeDiscPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyQualifier.setStatus("current")
_CfprApComputeBladeDiscPolicyScrubPolicyName_Type = SnmpAdminString
_CfprApComputeBladeDiscPolicyScrubPolicyName_Object = MibTableColumn
cfprApComputeBladeDiscPolicyScrubPolicyName = _CfprApComputeBladeDiscPolicyScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 3, 1, 11),
    _CfprApComputeBladeDiscPolicyScrubPolicyName_Type()
)
cfprApComputeBladeDiscPolicyScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeDiscPolicyScrubPolicyName.setStatus("current")
_CfprApComputeBladeFsmTable_Object = MibTable
cfprApComputeBladeFsmTable = _CfprApComputeBladeFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4)
)
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmTable.setStatus("current")
_CfprApComputeBladeFsmEntry_Object = MibTableRow
cfprApComputeBladeFsmEntry = _CfprApComputeBladeFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4, 1)
)
cfprApComputeBladeFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeBladeFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmEntry.setStatus("current")
_CfprApComputeBladeFsmInstanceId_Type = CfprApManagedObjectId
_CfprApComputeBladeFsmInstanceId_Object = MibTableColumn
cfprApComputeBladeFsmInstanceId = _CfprApComputeBladeFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4, 1, 1),
    _CfprApComputeBladeFsmInstanceId_Type()
)
cfprApComputeBladeFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmInstanceId.setStatus("current")
_CfprApComputeBladeFsmDn_Type = CfprApManagedObjectDn
_CfprApComputeBladeFsmDn_Object = MibTableColumn
cfprApComputeBladeFsmDn = _CfprApComputeBladeFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4, 1, 2),
    _CfprApComputeBladeFsmDn_Type()
)
cfprApComputeBladeFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmDn.setStatus("current")
_CfprApComputeBladeFsmRn_Type = SnmpAdminString
_CfprApComputeBladeFsmRn_Object = MibTableColumn
cfprApComputeBladeFsmRn = _CfprApComputeBladeFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4, 1, 3),
    _CfprApComputeBladeFsmRn_Type()
)
cfprApComputeBladeFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmRn.setStatus("current")
_CfprApComputeBladeFsmCompletionTime_Type = DateAndTime
_CfprApComputeBladeFsmCompletionTime_Object = MibTableColumn
cfprApComputeBladeFsmCompletionTime = _CfprApComputeBladeFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4, 1, 4),
    _CfprApComputeBladeFsmCompletionTime_Type()
)
cfprApComputeBladeFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmCompletionTime.setStatus("current")
_CfprApComputeBladeFsmCurrentFsm_Type = CfprApComputeBladeFsmCurrentFsm
_CfprApComputeBladeFsmCurrentFsm_Object = MibTableColumn
cfprApComputeBladeFsmCurrentFsm = _CfprApComputeBladeFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4, 1, 5),
    _CfprApComputeBladeFsmCurrentFsm_Type()
)
cfprApComputeBladeFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmCurrentFsm.setStatus("current")
_CfprApComputeBladeFsmDescrData_Type = SnmpAdminString
_CfprApComputeBladeFsmDescrData_Object = MibTableColumn
cfprApComputeBladeFsmDescrData = _CfprApComputeBladeFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4, 1, 6),
    _CfprApComputeBladeFsmDescrData_Type()
)
cfprApComputeBladeFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmDescrData.setStatus("current")
_CfprApComputeBladeFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApComputeBladeFsmFsmStatus_Object = MibTableColumn
cfprApComputeBladeFsmFsmStatus = _CfprApComputeBladeFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4, 1, 7),
    _CfprApComputeBladeFsmFsmStatus_Type()
)
cfprApComputeBladeFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmFsmStatus.setStatus("current")
_CfprApComputeBladeFsmProgress_Type = Gauge32
_CfprApComputeBladeFsmProgress_Object = MibTableColumn
cfprApComputeBladeFsmProgress = _CfprApComputeBladeFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4, 1, 8),
    _CfprApComputeBladeFsmProgress_Type()
)
cfprApComputeBladeFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmProgress.setStatus("current")
_CfprApComputeBladeFsmRmtErrCode_Type = Gauge32
_CfprApComputeBladeFsmRmtErrCode_Object = MibTableColumn
cfprApComputeBladeFsmRmtErrCode = _CfprApComputeBladeFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4, 1, 9),
    _CfprApComputeBladeFsmRmtErrCode_Type()
)
cfprApComputeBladeFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmRmtErrCode.setStatus("current")
_CfprApComputeBladeFsmRmtErrDescr_Type = SnmpAdminString
_CfprApComputeBladeFsmRmtErrDescr_Object = MibTableColumn
cfprApComputeBladeFsmRmtErrDescr = _CfprApComputeBladeFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4, 1, 10),
    _CfprApComputeBladeFsmRmtErrDescr_Type()
)
cfprApComputeBladeFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmRmtErrDescr.setStatus("current")
_CfprApComputeBladeFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApComputeBladeFsmRmtRslt_Object = MibTableColumn
cfprApComputeBladeFsmRmtRslt = _CfprApComputeBladeFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 4, 1, 11),
    _CfprApComputeBladeFsmRmtRslt_Type()
)
cfprApComputeBladeFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmRmtRslt.setStatus("current")
_CfprApComputeBladeFsmStageTable_Object = MibTable
cfprApComputeBladeFsmStageTable = _CfprApComputeBladeFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 5)
)
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStageTable.setStatus("current")
_CfprApComputeBladeFsmStageEntry_Object = MibTableRow
cfprApComputeBladeFsmStageEntry = _CfprApComputeBladeFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 5, 1)
)
cfprApComputeBladeFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeBladeFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStageEntry.setStatus("current")
_CfprApComputeBladeFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApComputeBladeFsmStageInstanceId_Object = MibTableColumn
cfprApComputeBladeFsmStageInstanceId = _CfprApComputeBladeFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 5, 1, 1),
    _CfprApComputeBladeFsmStageInstanceId_Type()
)
cfprApComputeBladeFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStageInstanceId.setStatus("current")
_CfprApComputeBladeFsmStageDn_Type = CfprApManagedObjectDn
_CfprApComputeBladeFsmStageDn_Object = MibTableColumn
cfprApComputeBladeFsmStageDn = _CfprApComputeBladeFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 5, 1, 2),
    _CfprApComputeBladeFsmStageDn_Type()
)
cfprApComputeBladeFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStageDn.setStatus("current")
_CfprApComputeBladeFsmStageRn_Type = SnmpAdminString
_CfprApComputeBladeFsmStageRn_Object = MibTableColumn
cfprApComputeBladeFsmStageRn = _CfprApComputeBladeFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 5, 1, 3),
    _CfprApComputeBladeFsmStageRn_Type()
)
cfprApComputeBladeFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStageRn.setStatus("current")
_CfprApComputeBladeFsmStageDescrData_Type = SnmpAdminString
_CfprApComputeBladeFsmStageDescrData_Object = MibTableColumn
cfprApComputeBladeFsmStageDescrData = _CfprApComputeBladeFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 5, 1, 4),
    _CfprApComputeBladeFsmStageDescrData_Type()
)
cfprApComputeBladeFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStageDescrData.setStatus("current")
_CfprApComputeBladeFsmStageLastUpdateTime_Type = DateAndTime
_CfprApComputeBladeFsmStageLastUpdateTime_Object = MibTableColumn
cfprApComputeBladeFsmStageLastUpdateTime = _CfprApComputeBladeFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 5, 1, 5),
    _CfprApComputeBladeFsmStageLastUpdateTime_Type()
)
cfprApComputeBladeFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStageLastUpdateTime.setStatus("current")
_CfprApComputeBladeFsmStageName_Type = CfprApComputeBladeFsmStageName
_CfprApComputeBladeFsmStageName_Object = MibTableColumn
cfprApComputeBladeFsmStageName = _CfprApComputeBladeFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 5, 1, 6),
    _CfprApComputeBladeFsmStageName_Type()
)
cfprApComputeBladeFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStageName.setStatus("current")
_CfprApComputeBladeFsmStageOrder_Type = Gauge32
_CfprApComputeBladeFsmStageOrder_Object = MibTableColumn
cfprApComputeBladeFsmStageOrder = _CfprApComputeBladeFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 5, 1, 7),
    _CfprApComputeBladeFsmStageOrder_Type()
)
cfprApComputeBladeFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStageOrder.setStatus("current")
_CfprApComputeBladeFsmStageRetry_Type = Gauge32
_CfprApComputeBladeFsmStageRetry_Object = MibTableColumn
cfprApComputeBladeFsmStageRetry = _CfprApComputeBladeFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 5, 1, 8),
    _CfprApComputeBladeFsmStageRetry_Type()
)
cfprApComputeBladeFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStageRetry.setStatus("current")
_CfprApComputeBladeFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApComputeBladeFsmStageStageStatus_Object = MibTableColumn
cfprApComputeBladeFsmStageStageStatus = _CfprApComputeBladeFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 5, 1, 9),
    _CfprApComputeBladeFsmStageStageStatus_Type()
)
cfprApComputeBladeFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmStageStageStatus.setStatus("current")
_CfprApComputeBladeFsmTaskTable_Object = MibTable
cfprApComputeBladeFsmTaskTable = _CfprApComputeBladeFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 6)
)
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmTaskTable.setStatus("current")
_CfprApComputeBladeFsmTaskEntry_Object = MibTableRow
cfprApComputeBladeFsmTaskEntry = _CfprApComputeBladeFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 6, 1)
)
cfprApComputeBladeFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeBladeFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmTaskEntry.setStatus("current")
_CfprApComputeBladeFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApComputeBladeFsmTaskInstanceId_Object = MibTableColumn
cfprApComputeBladeFsmTaskInstanceId = _CfprApComputeBladeFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 6, 1, 1),
    _CfprApComputeBladeFsmTaskInstanceId_Type()
)
cfprApComputeBladeFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmTaskInstanceId.setStatus("current")
_CfprApComputeBladeFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApComputeBladeFsmTaskDn_Object = MibTableColumn
cfprApComputeBladeFsmTaskDn = _CfprApComputeBladeFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 6, 1, 2),
    _CfprApComputeBladeFsmTaskDn_Type()
)
cfprApComputeBladeFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmTaskDn.setStatus("current")
_CfprApComputeBladeFsmTaskRn_Type = SnmpAdminString
_CfprApComputeBladeFsmTaskRn_Object = MibTableColumn
cfprApComputeBladeFsmTaskRn = _CfprApComputeBladeFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 6, 1, 3),
    _CfprApComputeBladeFsmTaskRn_Type()
)
cfprApComputeBladeFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmTaskRn.setStatus("current")
_CfprApComputeBladeFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApComputeBladeFsmTaskCompletion_Object = MibTableColumn
cfprApComputeBladeFsmTaskCompletion = _CfprApComputeBladeFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 6, 1, 4),
    _CfprApComputeBladeFsmTaskCompletion_Type()
)
cfprApComputeBladeFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmTaskCompletion.setStatus("current")
_CfprApComputeBladeFsmTaskFlags_Type = CfprApComputeBladeFsmTaskFlags
_CfprApComputeBladeFsmTaskFlags_Object = MibTableColumn
cfprApComputeBladeFsmTaskFlags = _CfprApComputeBladeFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 6, 1, 5),
    _CfprApComputeBladeFsmTaskFlags_Type()
)
cfprApComputeBladeFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmTaskFlags.setStatus("current")
_CfprApComputeBladeFsmTaskItem_Type = CfprApComputeBladeFsmTaskItem
_CfprApComputeBladeFsmTaskItem_Object = MibTableColumn
cfprApComputeBladeFsmTaskItem = _CfprApComputeBladeFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 6, 1, 6),
    _CfprApComputeBladeFsmTaskItem_Type()
)
cfprApComputeBladeFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmTaskItem.setStatus("current")
_CfprApComputeBladeFsmTaskSeqId_Type = Gauge32
_CfprApComputeBladeFsmTaskSeqId_Object = MibTableColumn
cfprApComputeBladeFsmTaskSeqId = _CfprApComputeBladeFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 6, 1, 7),
    _CfprApComputeBladeFsmTaskSeqId_Type()
)
cfprApComputeBladeFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeFsmTaskSeqId.setStatus("current")
_CfprApComputeBladeInheritPolicyTable_Object = MibTable
cfprApComputeBladeInheritPolicyTable = _CfprApComputeBladeInheritPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 7)
)
if mibBuilder.loadTexts:
    cfprApComputeBladeInheritPolicyTable.setStatus("current")
_CfprApComputeBladeInheritPolicyEntry_Object = MibTableRow
cfprApComputeBladeInheritPolicyEntry = _CfprApComputeBladeInheritPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 7, 1)
)
cfprApComputeBladeInheritPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeBladeInheritPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeBladeInheritPolicyEntry.setStatus("current")
_CfprApComputeBladeInheritPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApComputeBladeInheritPolicyInstanceId_Object = MibTableColumn
cfprApComputeBladeInheritPolicyInstanceId = _CfprApComputeBladeInheritPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 7, 1, 1),
    _CfprApComputeBladeInheritPolicyInstanceId_Type()
)
cfprApComputeBladeInheritPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeBladeInheritPolicyInstanceId.setStatus("current")
_CfprApComputeBladeInheritPolicyDn_Type = CfprApManagedObjectDn
_CfprApComputeBladeInheritPolicyDn_Object = MibTableColumn
cfprApComputeBladeInheritPolicyDn = _CfprApComputeBladeInheritPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 7, 1, 2),
    _CfprApComputeBladeInheritPolicyDn_Type()
)
cfprApComputeBladeInheritPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeInheritPolicyDn.setStatus("current")
_CfprApComputeBladeInheritPolicyRn_Type = SnmpAdminString
_CfprApComputeBladeInheritPolicyRn_Object = MibTableColumn
cfprApComputeBladeInheritPolicyRn = _CfprApComputeBladeInheritPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 7, 1, 3),
    _CfprApComputeBladeInheritPolicyRn_Type()
)
cfprApComputeBladeInheritPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeInheritPolicyRn.setStatus("current")
_CfprApComputeBladeInheritPolicyDescr_Type = SnmpAdminString
_CfprApComputeBladeInheritPolicyDescr_Object = MibTableColumn
cfprApComputeBladeInheritPolicyDescr = _CfprApComputeBladeInheritPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 7, 1, 4),
    _CfprApComputeBladeInheritPolicyDescr_Type()
)
cfprApComputeBladeInheritPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeInheritPolicyDescr.setStatus("current")
_CfprApComputeBladeInheritPolicyDstDn_Type = SnmpAdminString
_CfprApComputeBladeInheritPolicyDstDn_Object = MibTableColumn
cfprApComputeBladeInheritPolicyDstDn = _CfprApComputeBladeInheritPolicyDstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 7, 1, 5),
    _CfprApComputeBladeInheritPolicyDstDn_Type()
)
cfprApComputeBladeInheritPolicyDstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeInheritPolicyDstDn.setStatus("current")
_CfprApComputeBladeInheritPolicyIntId_Type = SnmpAdminString
_CfprApComputeBladeInheritPolicyIntId_Object = MibTableColumn
cfprApComputeBladeInheritPolicyIntId = _CfprApComputeBladeInheritPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 7, 1, 6),
    _CfprApComputeBladeInheritPolicyIntId_Type()
)
cfprApComputeBladeInheritPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeInheritPolicyIntId.setStatus("current")
_CfprApComputeBladeInheritPolicyName_Type = SnmpAdminString
_CfprApComputeBladeInheritPolicyName_Object = MibTableColumn
cfprApComputeBladeInheritPolicyName = _CfprApComputeBladeInheritPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 7, 1, 7),
    _CfprApComputeBladeInheritPolicyName_Type()
)
cfprApComputeBladeInheritPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeInheritPolicyName.setStatus("current")
_CfprApComputeBladeInheritPolicyPolicyLevel_Type = Gauge32
_CfprApComputeBladeInheritPolicyPolicyLevel_Object = MibTableColumn
cfprApComputeBladeInheritPolicyPolicyLevel = _CfprApComputeBladeInheritPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 7, 1, 8),
    _CfprApComputeBladeInheritPolicyPolicyLevel_Type()
)
cfprApComputeBladeInheritPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeInheritPolicyPolicyLevel.setStatus("current")
_CfprApComputeBladeInheritPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeBladeInheritPolicyPolicyOwner_Object = MibTableColumn
cfprApComputeBladeInheritPolicyPolicyOwner = _CfprApComputeBladeInheritPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 7, 1, 9),
    _CfprApComputeBladeInheritPolicyPolicyOwner_Type()
)
cfprApComputeBladeInheritPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeInheritPolicyPolicyOwner.setStatus("current")
_CfprApComputeBladeInheritPolicyQualifier_Type = SnmpAdminString
_CfprApComputeBladeInheritPolicyQualifier_Object = MibTableColumn
cfprApComputeBladeInheritPolicyQualifier = _CfprApComputeBladeInheritPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 7, 1, 10),
    _CfprApComputeBladeInheritPolicyQualifier_Type()
)
cfprApComputeBladeInheritPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBladeInheritPolicyQualifier.setStatus("current")
_CfprApComputeBoardTable_Object = MibTable
cfprApComputeBoardTable = _CfprApComputeBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8)
)
if mibBuilder.loadTexts:
    cfprApComputeBoardTable.setStatus("current")
_CfprApComputeBoardEntry_Object = MibTableRow
cfprApComputeBoardEntry = _CfprApComputeBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1)
)
cfprApComputeBoardEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeBoardInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeBoardEntry.setStatus("current")
_CfprApComputeBoardInstanceId_Type = CfprApManagedObjectId
_CfprApComputeBoardInstanceId_Object = MibTableColumn
cfprApComputeBoardInstanceId = _CfprApComputeBoardInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 1),
    _CfprApComputeBoardInstanceId_Type()
)
cfprApComputeBoardInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeBoardInstanceId.setStatus("current")
_CfprApComputeBoardDn_Type = CfprApManagedObjectDn
_CfprApComputeBoardDn_Object = MibTableColumn
cfprApComputeBoardDn = _CfprApComputeBoardDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 2),
    _CfprApComputeBoardDn_Type()
)
cfprApComputeBoardDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardDn.setStatus("current")
_CfprApComputeBoardRn_Type = SnmpAdminString
_CfprApComputeBoardRn_Object = MibTableColumn
cfprApComputeBoardRn = _CfprApComputeBoardRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 3),
    _CfprApComputeBoardRn_Type()
)
cfprApComputeBoardRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardRn.setStatus("current")
_CfprApComputeBoardCmosVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeBoardCmosVoltage_Object = MibTableColumn
cfprApComputeBoardCmosVoltage = _CfprApComputeBoardCmosVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 4),
    _CfprApComputeBoardCmosVoltage_Type()
)
cfprApComputeBoardCmosVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardCmosVoltage.setStatus("current")
_CfprApComputeBoardCpuType_Type = CfprApEquipmentCpuType
_CfprApComputeBoardCpuType_Object = MibTableColumn
cfprApComputeBoardCpuType = _CfprApComputeBoardCpuType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 5),
    _CfprApComputeBoardCpuType_Type()
)
cfprApComputeBoardCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardCpuType.setStatus("current")
_CfprApComputeBoardFaultQualifier_Type = SnmpAdminString
_CfprApComputeBoardFaultQualifier_Object = MibTableColumn
cfprApComputeBoardFaultQualifier = _CfprApComputeBoardFaultQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 6),
    _CfprApComputeBoardFaultQualifier_Type()
)
cfprApComputeBoardFaultQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardFaultQualifier.setStatus("current")
_CfprApComputeBoardId_Type = Gauge32
_CfprApComputeBoardId_Object = MibTableColumn
cfprApComputeBoardId = _CfprApComputeBoardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 7),
    _CfprApComputeBoardId_Type()
)
cfprApComputeBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardId.setStatus("current")
_CfprApComputeBoardLocationDn_Type = SnmpAdminString
_CfprApComputeBoardLocationDn_Object = MibTableColumn
cfprApComputeBoardLocationDn = _CfprApComputeBoardLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 8),
    _CfprApComputeBoardLocationDn_Type()
)
cfprApComputeBoardLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardLocationDn.setStatus("current")
_CfprApComputeBoardModel_Type = SnmpAdminString
_CfprApComputeBoardModel_Object = MibTableColumn
cfprApComputeBoardModel = _CfprApComputeBoardModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 9),
    _CfprApComputeBoardModel_Type()
)
cfprApComputeBoardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardModel.setStatus("current")
_CfprApComputeBoardOperPower_Type = CfprApEquipmentPowerState
_CfprApComputeBoardOperPower_Object = MibTableColumn
cfprApComputeBoardOperPower = _CfprApComputeBoardOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 10),
    _CfprApComputeBoardOperPower_Type()
)
cfprApComputeBoardOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardOperPower.setStatus("current")
_CfprApComputeBoardOperQualifierReason_Type = SnmpAdminString
_CfprApComputeBoardOperQualifierReason_Object = MibTableColumn
cfprApComputeBoardOperQualifierReason = _CfprApComputeBoardOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 11),
    _CfprApComputeBoardOperQualifierReason_Type()
)
cfprApComputeBoardOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardOperQualifierReason.setStatus("current")
_CfprApComputeBoardOperState_Type = CfprApEquipmentOperability
_CfprApComputeBoardOperState_Object = MibTableColumn
cfprApComputeBoardOperState = _CfprApComputeBoardOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 12),
    _CfprApComputeBoardOperState_Type()
)
cfprApComputeBoardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardOperState.setStatus("current")
_CfprApComputeBoardOperability_Type = CfprApEquipmentOperability
_CfprApComputeBoardOperability_Object = MibTableColumn
cfprApComputeBoardOperability = _CfprApComputeBoardOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 13),
    _CfprApComputeBoardOperability_Type()
)
cfprApComputeBoardOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardOperability.setStatus("current")
_CfprApComputeBoardPerf_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeBoardPerf_Object = MibTableColumn
cfprApComputeBoardPerf = _CfprApComputeBoardPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 14),
    _CfprApComputeBoardPerf_Type()
)
cfprApComputeBoardPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardPerf.setStatus("current")
_CfprApComputeBoardPower_Type = CfprApComputeABoardPower
_CfprApComputeBoardPower_Object = MibTableColumn
cfprApComputeBoardPower = _CfprApComputeBoardPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 15),
    _CfprApComputeBoardPower_Type()
)
cfprApComputeBoardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardPower.setStatus("current")
_CfprApComputeBoardPowerUsage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeBoardPowerUsage_Object = MibTableColumn
cfprApComputeBoardPowerUsage = _CfprApComputeBoardPowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 16),
    _CfprApComputeBoardPowerUsage_Type()
)
cfprApComputeBoardPowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardPowerUsage.setStatus("current")
_CfprApComputeBoardPresence_Type = CfprApEquipmentPresence
_CfprApComputeBoardPresence_Object = MibTableColumn
cfprApComputeBoardPresence = _CfprApComputeBoardPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 17),
    _CfprApComputeBoardPresence_Type()
)
cfprApComputeBoardPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardPresence.setStatus("current")
_CfprApComputeBoardRevision_Type = SnmpAdminString
_CfprApComputeBoardRevision_Object = MibTableColumn
cfprApComputeBoardRevision = _CfprApComputeBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 18),
    _CfprApComputeBoardRevision_Type()
)
cfprApComputeBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardRevision.setStatus("current")
_CfprApComputeBoardSerial_Type = SnmpAdminString
_CfprApComputeBoardSerial_Object = MibTableColumn
cfprApComputeBoardSerial = _CfprApComputeBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 19),
    _CfprApComputeBoardSerial_Type()
)
cfprApComputeBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardSerial.setStatus("current")
_CfprApComputeBoardThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeBoardThermal_Object = MibTableColumn
cfprApComputeBoardThermal = _CfprApComputeBoardThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 20),
    _CfprApComputeBoardThermal_Type()
)
cfprApComputeBoardThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardThermal.setStatus("current")
_CfprApComputeBoardVendor_Type = SnmpAdminString
_CfprApComputeBoardVendor_Object = MibTableColumn
cfprApComputeBoardVendor = _CfprApComputeBoardVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 21),
    _CfprApComputeBoardVendor_Type()
)
cfprApComputeBoardVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardVendor.setStatus("current")
_CfprApComputeBoardVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeBoardVoltage_Object = MibTableColumn
cfprApComputeBoardVoltage = _CfprApComputeBoardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 8, 1, 22),
    _CfprApComputeBoardVoltage_Type()
)
cfprApComputeBoardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardVoltage.setStatus("current")
_CfprApComputeBoardConnectorTable_Object = MibTable
cfprApComputeBoardConnectorTable = _CfprApComputeBoardConnectorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 9)
)
if mibBuilder.loadTexts:
    cfprApComputeBoardConnectorTable.setStatus("current")
_CfprApComputeBoardConnectorEntry_Object = MibTableRow
cfprApComputeBoardConnectorEntry = _CfprApComputeBoardConnectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 9, 1)
)
cfprApComputeBoardConnectorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeBoardConnectorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeBoardConnectorEntry.setStatus("current")
_CfprApComputeBoardConnectorInstanceId_Type = CfprApManagedObjectId
_CfprApComputeBoardConnectorInstanceId_Object = MibTableColumn
cfprApComputeBoardConnectorInstanceId = _CfprApComputeBoardConnectorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 9, 1, 1),
    _CfprApComputeBoardConnectorInstanceId_Type()
)
cfprApComputeBoardConnectorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeBoardConnectorInstanceId.setStatus("current")
_CfprApComputeBoardConnectorDn_Type = CfprApManagedObjectDn
_CfprApComputeBoardConnectorDn_Object = MibTableColumn
cfprApComputeBoardConnectorDn = _CfprApComputeBoardConnectorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 9, 1, 2),
    _CfprApComputeBoardConnectorDn_Type()
)
cfprApComputeBoardConnectorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardConnectorDn.setStatus("current")
_CfprApComputeBoardConnectorRn_Type = SnmpAdminString
_CfprApComputeBoardConnectorRn_Object = MibTableColumn
cfprApComputeBoardConnectorRn = _CfprApComputeBoardConnectorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 9, 1, 3),
    _CfprApComputeBoardConnectorRn_Type()
)
cfprApComputeBoardConnectorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardConnectorRn.setStatus("current")
_CfprApComputeBoardConnectorBoardConnectorType_Type = CfprApEquipmentBoardConnectorType
_CfprApComputeBoardConnectorBoardConnectorType_Object = MibTableColumn
cfprApComputeBoardConnectorBoardConnectorType = _CfprApComputeBoardConnectorBoardConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 9, 1, 4),
    _CfprApComputeBoardConnectorBoardConnectorType_Type()
)
cfprApComputeBoardConnectorBoardConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardConnectorBoardConnectorType.setStatus("current")
_CfprApComputeBoardConnectorMasterSlotId_Type = Gauge32
_CfprApComputeBoardConnectorMasterSlotId_Object = MibTableColumn
cfprApComputeBoardConnectorMasterSlotId = _CfprApComputeBoardConnectorMasterSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 9, 1, 5),
    _CfprApComputeBoardConnectorMasterSlotId_Type()
)
cfprApComputeBoardConnectorMasterSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardConnectorMasterSlotId.setStatus("current")
_CfprApComputeBoardConnectorSlaveSlotId_Type = Gauge32
_CfprApComputeBoardConnectorSlaveSlotId_Object = MibTableColumn
cfprApComputeBoardConnectorSlaveSlotId = _CfprApComputeBoardConnectorSlaveSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 9, 1, 6),
    _CfprApComputeBoardConnectorSlaveSlotId_Type()
)
cfprApComputeBoardConnectorSlaveSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardConnectorSlaveSlotId.setStatus("current")
_CfprApComputeBoardControllerTable_Object = MibTable
cfprApComputeBoardControllerTable = _CfprApComputeBoardControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10)
)
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerTable.setStatus("current")
_CfprApComputeBoardControllerEntry_Object = MibTableRow
cfprApComputeBoardControllerEntry = _CfprApComputeBoardControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1)
)
cfprApComputeBoardControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeBoardControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerEntry.setStatus("current")
_CfprApComputeBoardControllerInstanceId_Type = CfprApManagedObjectId
_CfprApComputeBoardControllerInstanceId_Object = MibTableColumn
cfprApComputeBoardControllerInstanceId = _CfprApComputeBoardControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 1),
    _CfprApComputeBoardControllerInstanceId_Type()
)
cfprApComputeBoardControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerInstanceId.setStatus("current")
_CfprApComputeBoardControllerDn_Type = CfprApManagedObjectDn
_CfprApComputeBoardControllerDn_Object = MibTableColumn
cfprApComputeBoardControllerDn = _CfprApComputeBoardControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 2),
    _CfprApComputeBoardControllerDn_Type()
)
cfprApComputeBoardControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerDn.setStatus("current")
_CfprApComputeBoardControllerRn_Type = SnmpAdminString
_CfprApComputeBoardControllerRn_Object = MibTableColumn
cfprApComputeBoardControllerRn = _CfprApComputeBoardControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 3),
    _CfprApComputeBoardControllerRn_Type()
)
cfprApComputeBoardControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerRn.setStatus("current")
_CfprApComputeBoardControllerId_Type = Gauge32
_CfprApComputeBoardControllerId_Object = MibTableColumn
cfprApComputeBoardControllerId = _CfprApComputeBoardControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 4),
    _CfprApComputeBoardControllerId_Type()
)
cfprApComputeBoardControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerId.setStatus("current")
_CfprApComputeBoardControllerLocationDn_Type = SnmpAdminString
_CfprApComputeBoardControllerLocationDn_Object = MibTableColumn
cfprApComputeBoardControllerLocationDn = _CfprApComputeBoardControllerLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 5),
    _CfprApComputeBoardControllerLocationDn_Type()
)
cfprApComputeBoardControllerLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerLocationDn.setStatus("current")
_CfprApComputeBoardControllerModel_Type = SnmpAdminString
_CfprApComputeBoardControllerModel_Object = MibTableColumn
cfprApComputeBoardControllerModel = _CfprApComputeBoardControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 6),
    _CfprApComputeBoardControllerModel_Type()
)
cfprApComputeBoardControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerModel.setStatus("current")
_CfprApComputeBoardControllerOperQualifierReason_Type = SnmpAdminString
_CfprApComputeBoardControllerOperQualifierReason_Object = MibTableColumn
cfprApComputeBoardControllerOperQualifierReason = _CfprApComputeBoardControllerOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 7),
    _CfprApComputeBoardControllerOperQualifierReason_Type()
)
cfprApComputeBoardControllerOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerOperQualifierReason.setStatus("current")
_CfprApComputeBoardControllerOperState_Type = CfprApEquipmentOperability
_CfprApComputeBoardControllerOperState_Object = MibTableColumn
cfprApComputeBoardControllerOperState = _CfprApComputeBoardControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 8),
    _CfprApComputeBoardControllerOperState_Type()
)
cfprApComputeBoardControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerOperState.setStatus("current")
_CfprApComputeBoardControllerOperability_Type = CfprApEquipmentOperability
_CfprApComputeBoardControllerOperability_Object = MibTableColumn
cfprApComputeBoardControllerOperability = _CfprApComputeBoardControllerOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 9),
    _CfprApComputeBoardControllerOperability_Type()
)
cfprApComputeBoardControllerOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerOperability.setStatus("current")
_CfprApComputeBoardControllerPerf_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeBoardControllerPerf_Object = MibTableColumn
cfprApComputeBoardControllerPerf = _CfprApComputeBoardControllerPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 10),
    _CfprApComputeBoardControllerPerf_Type()
)
cfprApComputeBoardControllerPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerPerf.setStatus("current")
_CfprApComputeBoardControllerPower_Type = CfprApEquipmentPowerState
_CfprApComputeBoardControllerPower_Object = MibTableColumn
cfprApComputeBoardControllerPower = _CfprApComputeBoardControllerPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 11),
    _CfprApComputeBoardControllerPower_Type()
)
cfprApComputeBoardControllerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerPower.setStatus("current")
_CfprApComputeBoardControllerPresence_Type = CfprApEquipmentPresence
_CfprApComputeBoardControllerPresence_Object = MibTableColumn
cfprApComputeBoardControllerPresence = _CfprApComputeBoardControllerPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 12),
    _CfprApComputeBoardControllerPresence_Type()
)
cfprApComputeBoardControllerPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerPresence.setStatus("current")
_CfprApComputeBoardControllerRevision_Type = SnmpAdminString
_CfprApComputeBoardControllerRevision_Object = MibTableColumn
cfprApComputeBoardControllerRevision = _CfprApComputeBoardControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 13),
    _CfprApComputeBoardControllerRevision_Type()
)
cfprApComputeBoardControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerRevision.setStatus("current")
_CfprApComputeBoardControllerSerial_Type = SnmpAdminString
_CfprApComputeBoardControllerSerial_Object = MibTableColumn
cfprApComputeBoardControllerSerial = _CfprApComputeBoardControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 14),
    _CfprApComputeBoardControllerSerial_Type()
)
cfprApComputeBoardControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerSerial.setStatus("current")
_CfprApComputeBoardControllerThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeBoardControllerThermal_Object = MibTableColumn
cfprApComputeBoardControllerThermal = _CfprApComputeBoardControllerThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 15),
    _CfprApComputeBoardControllerThermal_Type()
)
cfprApComputeBoardControllerThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerThermal.setStatus("current")
_CfprApComputeBoardControllerVendor_Type = SnmpAdminString
_CfprApComputeBoardControllerVendor_Object = MibTableColumn
cfprApComputeBoardControllerVendor = _CfprApComputeBoardControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 16),
    _CfprApComputeBoardControllerVendor_Type()
)
cfprApComputeBoardControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerVendor.setStatus("current")
_CfprApComputeBoardControllerVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeBoardControllerVoltage_Object = MibTableColumn
cfprApComputeBoardControllerVoltage = _CfprApComputeBoardControllerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 10, 1, 17),
    _CfprApComputeBoardControllerVoltage_Type()
)
cfprApComputeBoardControllerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeBoardControllerVoltage.setStatus("current")
_CfprApComputeChassisConnPolicyTable_Object = MibTable
cfprApComputeChassisConnPolicyTable = _CfprApComputeChassisConnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11)
)
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyTable.setStatus("current")
_CfprApComputeChassisConnPolicyEntry_Object = MibTableRow
cfprApComputeChassisConnPolicyEntry = _CfprApComputeChassisConnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1)
)
cfprApComputeChassisConnPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeChassisConnPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyEntry.setStatus("current")
_CfprApComputeChassisConnPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApComputeChassisConnPolicyInstanceId_Object = MibTableColumn
cfprApComputeChassisConnPolicyInstanceId = _CfprApComputeChassisConnPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1, 1),
    _CfprApComputeChassisConnPolicyInstanceId_Type()
)
cfprApComputeChassisConnPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyInstanceId.setStatus("current")
_CfprApComputeChassisConnPolicyDn_Type = CfprApManagedObjectDn
_CfprApComputeChassisConnPolicyDn_Object = MibTableColumn
cfprApComputeChassisConnPolicyDn = _CfprApComputeChassisConnPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1, 2),
    _CfprApComputeChassisConnPolicyDn_Type()
)
cfprApComputeChassisConnPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyDn.setStatus("current")
_CfprApComputeChassisConnPolicyRn_Type = SnmpAdminString
_CfprApComputeChassisConnPolicyRn_Object = MibTableColumn
cfprApComputeChassisConnPolicyRn = _CfprApComputeChassisConnPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1, 3),
    _CfprApComputeChassisConnPolicyRn_Type()
)
cfprApComputeChassisConnPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyRn.setStatus("current")
_CfprApComputeChassisConnPolicyAdminState_Type = CfprApComputeAdminLinkAggregation
_CfprApComputeChassisConnPolicyAdminState_Object = MibTableColumn
cfprApComputeChassisConnPolicyAdminState = _CfprApComputeChassisConnPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1, 4),
    _CfprApComputeChassisConnPolicyAdminState_Type()
)
cfprApComputeChassisConnPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyAdminState.setStatus("current")
_CfprApComputeChassisConnPolicyChassisId_Type = CfprApComputeChassisConnPolicyChassisId
_CfprApComputeChassisConnPolicyChassisId_Object = MibTableColumn
cfprApComputeChassisConnPolicyChassisId = _CfprApComputeChassisConnPolicyChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1, 5),
    _CfprApComputeChassisConnPolicyChassisId_Type()
)
cfprApComputeChassisConnPolicyChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyChassisId.setStatus("current")
_CfprApComputeChassisConnPolicyDescr_Type = SnmpAdminString
_CfprApComputeChassisConnPolicyDescr_Object = MibTableColumn
cfprApComputeChassisConnPolicyDescr = _CfprApComputeChassisConnPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1, 6),
    _CfprApComputeChassisConnPolicyDescr_Type()
)
cfprApComputeChassisConnPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyDescr.setStatus("current")
_CfprApComputeChassisConnPolicyIntId_Type = SnmpAdminString
_CfprApComputeChassisConnPolicyIntId_Object = MibTableColumn
cfprApComputeChassisConnPolicyIntId = _CfprApComputeChassisConnPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1, 7),
    _CfprApComputeChassisConnPolicyIntId_Type()
)
cfprApComputeChassisConnPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyIntId.setStatus("current")
_CfprApComputeChassisConnPolicyName_Type = SnmpAdminString
_CfprApComputeChassisConnPolicyName_Object = MibTableColumn
cfprApComputeChassisConnPolicyName = _CfprApComputeChassisConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1, 8),
    _CfprApComputeChassisConnPolicyName_Type()
)
cfprApComputeChassisConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyName.setStatus("current")
_CfprApComputeChassisConnPolicyPolicyLevel_Type = Gauge32
_CfprApComputeChassisConnPolicyPolicyLevel_Object = MibTableColumn
cfprApComputeChassisConnPolicyPolicyLevel = _CfprApComputeChassisConnPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1, 9),
    _CfprApComputeChassisConnPolicyPolicyLevel_Type()
)
cfprApComputeChassisConnPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyPolicyLevel.setStatus("current")
_CfprApComputeChassisConnPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeChassisConnPolicyPolicyOwner_Object = MibTableColumn
cfprApComputeChassisConnPolicyPolicyOwner = _CfprApComputeChassisConnPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1, 10),
    _CfprApComputeChassisConnPolicyPolicyOwner_Type()
)
cfprApComputeChassisConnPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyPolicyOwner.setStatus("current")
_CfprApComputeChassisConnPolicyQualifier_Type = SnmpAdminString
_CfprApComputeChassisConnPolicyQualifier_Object = MibTableColumn
cfprApComputeChassisConnPolicyQualifier = _CfprApComputeChassisConnPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1, 11),
    _CfprApComputeChassisConnPolicyQualifier_Type()
)
cfprApComputeChassisConnPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicyQualifier.setStatus("current")
_CfprApComputeChassisConnPolicySwitchId_Type = CfprApNetworkSwitchId
_CfprApComputeChassisConnPolicySwitchId_Object = MibTableColumn
cfprApComputeChassisConnPolicySwitchId = _CfprApComputeChassisConnPolicySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 11, 1, 12),
    _CfprApComputeChassisConnPolicySwitchId_Type()
)
cfprApComputeChassisConnPolicySwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisConnPolicySwitchId.setStatus("current")
_CfprApComputeChassisDiscPolicyTable_Object = MibTable
cfprApComputeChassisDiscPolicyTable = _CfprApComputeChassisDiscPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12)
)
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyTable.setStatus("current")
_CfprApComputeChassisDiscPolicyEntry_Object = MibTableRow
cfprApComputeChassisDiscPolicyEntry = _CfprApComputeChassisDiscPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1)
)
cfprApComputeChassisDiscPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeChassisDiscPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyEntry.setStatus("current")
_CfprApComputeChassisDiscPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApComputeChassisDiscPolicyInstanceId_Object = MibTableColumn
cfprApComputeChassisDiscPolicyInstanceId = _CfprApComputeChassisDiscPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1, 1),
    _CfprApComputeChassisDiscPolicyInstanceId_Type()
)
cfprApComputeChassisDiscPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyInstanceId.setStatus("current")
_CfprApComputeChassisDiscPolicyDn_Type = CfprApManagedObjectDn
_CfprApComputeChassisDiscPolicyDn_Object = MibTableColumn
cfprApComputeChassisDiscPolicyDn = _CfprApComputeChassisDiscPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1, 2),
    _CfprApComputeChassisDiscPolicyDn_Type()
)
cfprApComputeChassisDiscPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyDn.setStatus("current")
_CfprApComputeChassisDiscPolicyRn_Type = SnmpAdminString
_CfprApComputeChassisDiscPolicyRn_Object = MibTableColumn
cfprApComputeChassisDiscPolicyRn = _CfprApComputeChassisDiscPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1, 3),
    _CfprApComputeChassisDiscPolicyRn_Type()
)
cfprApComputeChassisDiscPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyRn.setStatus("current")
_CfprApComputeChassisDiscPolicyAction_Type = CfprApComputeChassisDiscAction
_CfprApComputeChassisDiscPolicyAction_Object = MibTableColumn
cfprApComputeChassisDiscPolicyAction = _CfprApComputeChassisDiscPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1, 4),
    _CfprApComputeChassisDiscPolicyAction_Type()
)
cfprApComputeChassisDiscPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyAction.setStatus("current")
_CfprApComputeChassisDiscPolicyDescr_Type = SnmpAdminString
_CfprApComputeChassisDiscPolicyDescr_Object = MibTableColumn
cfprApComputeChassisDiscPolicyDescr = _CfprApComputeChassisDiscPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1, 5),
    _CfprApComputeChassisDiscPolicyDescr_Type()
)
cfprApComputeChassisDiscPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyDescr.setStatus("current")
_CfprApComputeChassisDiscPolicyIntId_Type = SnmpAdminString
_CfprApComputeChassisDiscPolicyIntId_Object = MibTableColumn
cfprApComputeChassisDiscPolicyIntId = _CfprApComputeChassisDiscPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1, 6),
    _CfprApComputeChassisDiscPolicyIntId_Type()
)
cfprApComputeChassisDiscPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyIntId.setStatus("current")
_CfprApComputeChassisDiscPolicyLinkAggregationPref_Type = CfprApComputeLinkAggregation
_CfprApComputeChassisDiscPolicyLinkAggregationPref_Object = MibTableColumn
cfprApComputeChassisDiscPolicyLinkAggregationPref = _CfprApComputeChassisDiscPolicyLinkAggregationPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1, 7),
    _CfprApComputeChassisDiscPolicyLinkAggregationPref_Type()
)
cfprApComputeChassisDiscPolicyLinkAggregationPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyLinkAggregationPref.setStatus("current")
_CfprApComputeChassisDiscPolicyName_Type = SnmpAdminString
_CfprApComputeChassisDiscPolicyName_Object = MibTableColumn
cfprApComputeChassisDiscPolicyName = _CfprApComputeChassisDiscPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1, 8),
    _CfprApComputeChassisDiscPolicyName_Type()
)
cfprApComputeChassisDiscPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyName.setStatus("current")
_CfprApComputeChassisDiscPolicyPolicyLevel_Type = Gauge32
_CfprApComputeChassisDiscPolicyPolicyLevel_Object = MibTableColumn
cfprApComputeChassisDiscPolicyPolicyLevel = _CfprApComputeChassisDiscPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1, 9),
    _CfprApComputeChassisDiscPolicyPolicyLevel_Type()
)
cfprApComputeChassisDiscPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyPolicyLevel.setStatus("current")
_CfprApComputeChassisDiscPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeChassisDiscPolicyPolicyOwner_Object = MibTableColumn
cfprApComputeChassisDiscPolicyPolicyOwner = _CfprApComputeChassisDiscPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1, 10),
    _CfprApComputeChassisDiscPolicyPolicyOwner_Type()
)
cfprApComputeChassisDiscPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyPolicyOwner.setStatus("current")
_CfprApComputeChassisDiscPolicyQualifier_Type = SnmpAdminString
_CfprApComputeChassisDiscPolicyQualifier_Object = MibTableColumn
cfprApComputeChassisDiscPolicyQualifier = _CfprApComputeChassisDiscPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1, 11),
    _CfprApComputeChassisDiscPolicyQualifier_Type()
)
cfprApComputeChassisDiscPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyQualifier.setStatus("current")
_CfprApComputeChassisDiscPolicyRebalance_Type = CfprApComputeConnectivityRebalancing
_CfprApComputeChassisDiscPolicyRebalance_Object = MibTableColumn
cfprApComputeChassisDiscPolicyRebalance = _CfprApComputeChassisDiscPolicyRebalance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 12, 1, 12),
    _CfprApComputeChassisDiscPolicyRebalance_Type()
)
cfprApComputeChassisDiscPolicyRebalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisDiscPolicyRebalance.setStatus("current")
_CfprApComputeChassisQualTable_Object = MibTable
cfprApComputeChassisQualTable = _CfprApComputeChassisQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 13)
)
if mibBuilder.loadTexts:
    cfprApComputeChassisQualTable.setStatus("current")
_CfprApComputeChassisQualEntry_Object = MibTableRow
cfprApComputeChassisQualEntry = _CfprApComputeChassisQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 13, 1)
)
cfprApComputeChassisQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeChassisQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeChassisQualEntry.setStatus("current")
_CfprApComputeChassisQualInstanceId_Type = CfprApManagedObjectId
_CfprApComputeChassisQualInstanceId_Object = MibTableColumn
cfprApComputeChassisQualInstanceId = _CfprApComputeChassisQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 13, 1, 1),
    _CfprApComputeChassisQualInstanceId_Type()
)
cfprApComputeChassisQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeChassisQualInstanceId.setStatus("current")
_CfprApComputeChassisQualDn_Type = CfprApManagedObjectDn
_CfprApComputeChassisQualDn_Object = MibTableColumn
cfprApComputeChassisQualDn = _CfprApComputeChassisQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 13, 1, 2),
    _CfprApComputeChassisQualDn_Type()
)
cfprApComputeChassisQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisQualDn.setStatus("current")
_CfprApComputeChassisQualRn_Type = SnmpAdminString
_CfprApComputeChassisQualRn_Object = MibTableColumn
cfprApComputeChassisQualRn = _CfprApComputeChassisQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 13, 1, 3),
    _CfprApComputeChassisQualRn_Type()
)
cfprApComputeChassisQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisQualRn.setStatus("current")
_CfprApComputeChassisQualMaxId_Type = CfprApComputeChassisQualMaxId
_CfprApComputeChassisQualMaxId_Object = MibTableColumn
cfprApComputeChassisQualMaxId = _CfprApComputeChassisQualMaxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 13, 1, 4),
    _CfprApComputeChassisQualMaxId_Type()
)
cfprApComputeChassisQualMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisQualMaxId.setStatus("current")
_CfprApComputeChassisQualMinId_Type = CfprApComputeChassisQualMinId
_CfprApComputeChassisQualMinId_Object = MibTableColumn
cfprApComputeChassisQualMinId = _CfprApComputeChassisQualMinId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 13, 1, 5),
    _CfprApComputeChassisQualMinId_Type()
)
cfprApComputeChassisQualMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeChassisQualMinId.setStatus("current")
_CfprApComputeDefaultsTable_Object = MibTable
cfprApComputeDefaultsTable = _CfprApComputeDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 14)
)
if mibBuilder.loadTexts:
    cfprApComputeDefaultsTable.setStatus("current")
_CfprApComputeDefaultsEntry_Object = MibTableRow
cfprApComputeDefaultsEntry = _CfprApComputeDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 14, 1)
)
cfprApComputeDefaultsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeDefaultsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeDefaultsEntry.setStatus("current")
_CfprApComputeDefaultsInstanceId_Type = CfprApManagedObjectId
_CfprApComputeDefaultsInstanceId_Object = MibTableColumn
cfprApComputeDefaultsInstanceId = _CfprApComputeDefaultsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 14, 1, 1),
    _CfprApComputeDefaultsInstanceId_Type()
)
cfprApComputeDefaultsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeDefaultsInstanceId.setStatus("current")
_CfprApComputeDefaultsDn_Type = CfprApManagedObjectDn
_CfprApComputeDefaultsDn_Object = MibTableColumn
cfprApComputeDefaultsDn = _CfprApComputeDefaultsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 14, 1, 2),
    _CfprApComputeDefaultsDn_Type()
)
cfprApComputeDefaultsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeDefaultsDn.setStatus("current")
_CfprApComputeDefaultsRn_Type = SnmpAdminString
_CfprApComputeDefaultsRn_Object = MibTableColumn
cfprApComputeDefaultsRn = _CfprApComputeDefaultsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 14, 1, 3),
    _CfprApComputeDefaultsRn_Type()
)
cfprApComputeDefaultsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeDefaultsRn.setStatus("current")
_CfprApComputeExtBoardTable_Object = MibTable
cfprApComputeExtBoardTable = _CfprApComputeExtBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15)
)
if mibBuilder.loadTexts:
    cfprApComputeExtBoardTable.setStatus("current")
_CfprApComputeExtBoardEntry_Object = MibTableRow
cfprApComputeExtBoardEntry = _CfprApComputeExtBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1)
)
cfprApComputeExtBoardEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeExtBoardInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeExtBoardEntry.setStatus("current")
_CfprApComputeExtBoardInstanceId_Type = CfprApManagedObjectId
_CfprApComputeExtBoardInstanceId_Object = MibTableColumn
cfprApComputeExtBoardInstanceId = _CfprApComputeExtBoardInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 1),
    _CfprApComputeExtBoardInstanceId_Type()
)
cfprApComputeExtBoardInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardInstanceId.setStatus("current")
_CfprApComputeExtBoardDn_Type = CfprApManagedObjectDn
_CfprApComputeExtBoardDn_Object = MibTableColumn
cfprApComputeExtBoardDn = _CfprApComputeExtBoardDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 2),
    _CfprApComputeExtBoardDn_Type()
)
cfprApComputeExtBoardDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardDn.setStatus("current")
_CfprApComputeExtBoardRn_Type = SnmpAdminString
_CfprApComputeExtBoardRn_Object = MibTableColumn
cfprApComputeExtBoardRn = _CfprApComputeExtBoardRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 3),
    _CfprApComputeExtBoardRn_Type()
)
cfprApComputeExtBoardRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardRn.setStatus("current")
_CfprApComputeExtBoardBoardAggregationRole_Type = CfprApEquipmentBoardAggregationRole
_CfprApComputeExtBoardBoardAggregationRole_Object = MibTableColumn
cfprApComputeExtBoardBoardAggregationRole = _CfprApComputeExtBoardBoardAggregationRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 4),
    _CfprApComputeExtBoardBoardAggregationRole_Type()
)
cfprApComputeExtBoardBoardAggregationRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardBoardAggregationRole.setStatus("current")
_CfprApComputeExtBoardChassisId_Type = Gauge32
_CfprApComputeExtBoardChassisId_Object = MibTableColumn
cfprApComputeExtBoardChassisId = _CfprApComputeExtBoardChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 5),
    _CfprApComputeExtBoardChassisId_Type()
)
cfprApComputeExtBoardChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardChassisId.setStatus("current")
_CfprApComputeExtBoardCmosVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeExtBoardCmosVoltage_Object = MibTableColumn
cfprApComputeExtBoardCmosVoltage = _CfprApComputeExtBoardCmosVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 6),
    _CfprApComputeExtBoardCmosVoltage_Type()
)
cfprApComputeExtBoardCmosVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardCmosVoltage.setStatus("current")
_CfprApComputeExtBoardConnPath_Type = CfprApEquipmentConnectionStatus
_CfprApComputeExtBoardConnPath_Object = MibTableColumn
cfprApComputeExtBoardConnPath = _CfprApComputeExtBoardConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 7),
    _CfprApComputeExtBoardConnPath_Type()
)
cfprApComputeExtBoardConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardConnPath.setStatus("current")
_CfprApComputeExtBoardConnStatus_Type = CfprApEquipmentConnectionStatus
_CfprApComputeExtBoardConnStatus_Object = MibTableColumn
cfprApComputeExtBoardConnStatus = _CfprApComputeExtBoardConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 8),
    _CfprApComputeExtBoardConnStatus_Type()
)
cfprApComputeExtBoardConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardConnStatus.setStatus("current")
_CfprApComputeExtBoardFaultQualifier_Type = SnmpAdminString
_CfprApComputeExtBoardFaultQualifier_Object = MibTableColumn
cfprApComputeExtBoardFaultQualifier = _CfprApComputeExtBoardFaultQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 9),
    _CfprApComputeExtBoardFaultQualifier_Type()
)
cfprApComputeExtBoardFaultQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardFaultQualifier.setStatus("current")
_CfprApComputeExtBoardId_Type = Gauge32
_CfprApComputeExtBoardId_Object = MibTableColumn
cfprApComputeExtBoardId = _CfprApComputeExtBoardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 10),
    _CfprApComputeExtBoardId_Type()
)
cfprApComputeExtBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardId.setStatus("current")
_CfprApComputeExtBoardLocationDn_Type = SnmpAdminString
_CfprApComputeExtBoardLocationDn_Object = MibTableColumn
cfprApComputeExtBoardLocationDn = _CfprApComputeExtBoardLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 11),
    _CfprApComputeExtBoardLocationDn_Type()
)
cfprApComputeExtBoardLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardLocationDn.setStatus("current")
_CfprApComputeExtBoardManagingInst_Type = CfprApNetworkSwitchId
_CfprApComputeExtBoardManagingInst_Object = MibTableColumn
cfprApComputeExtBoardManagingInst = _CfprApComputeExtBoardManagingInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 12),
    _CfprApComputeExtBoardManagingInst_Type()
)
cfprApComputeExtBoardManagingInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardManagingInst.setStatus("current")
_CfprApComputeExtBoardModel_Type = SnmpAdminString
_CfprApComputeExtBoardModel_Object = MibTableColumn
cfprApComputeExtBoardModel = _CfprApComputeExtBoardModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 13),
    _CfprApComputeExtBoardModel_Type()
)
cfprApComputeExtBoardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardModel.setStatus("current")
_CfprApComputeExtBoardOperPower_Type = CfprApEquipmentPowerState
_CfprApComputeExtBoardOperPower_Object = MibTableColumn
cfprApComputeExtBoardOperPower = _CfprApComputeExtBoardOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 14),
    _CfprApComputeExtBoardOperPower_Type()
)
cfprApComputeExtBoardOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardOperPower.setStatus("current")
_CfprApComputeExtBoardOperQualifierReason_Type = SnmpAdminString
_CfprApComputeExtBoardOperQualifierReason_Object = MibTableColumn
cfprApComputeExtBoardOperQualifierReason = _CfprApComputeExtBoardOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 15),
    _CfprApComputeExtBoardOperQualifierReason_Type()
)
cfprApComputeExtBoardOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardOperQualifierReason.setStatus("current")
_CfprApComputeExtBoardOperState_Type = CfprApEquipmentOperability
_CfprApComputeExtBoardOperState_Object = MibTableColumn
cfprApComputeExtBoardOperState = _CfprApComputeExtBoardOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 16),
    _CfprApComputeExtBoardOperState_Type()
)
cfprApComputeExtBoardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardOperState.setStatus("current")
_CfprApComputeExtBoardOperability_Type = CfprApEquipmentOperability
_CfprApComputeExtBoardOperability_Object = MibTableColumn
cfprApComputeExtBoardOperability = _CfprApComputeExtBoardOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 17),
    _CfprApComputeExtBoardOperability_Type()
)
cfprApComputeExtBoardOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardOperability.setStatus("current")
_CfprApComputeExtBoardPerf_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeExtBoardPerf_Object = MibTableColumn
cfprApComputeExtBoardPerf = _CfprApComputeExtBoardPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 18),
    _CfprApComputeExtBoardPerf_Type()
)
cfprApComputeExtBoardPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardPerf.setStatus("current")
_CfprApComputeExtBoardPower_Type = CfprApComputeABoardPower
_CfprApComputeExtBoardPower_Object = MibTableColumn
cfprApComputeExtBoardPower = _CfprApComputeExtBoardPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 19),
    _CfprApComputeExtBoardPower_Type()
)
cfprApComputeExtBoardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardPower.setStatus("current")
_CfprApComputeExtBoardPowerUsage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeExtBoardPowerUsage_Object = MibTableColumn
cfprApComputeExtBoardPowerUsage = _CfprApComputeExtBoardPowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 20),
    _CfprApComputeExtBoardPowerUsage_Type()
)
cfprApComputeExtBoardPowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardPowerUsage.setStatus("current")
_CfprApComputeExtBoardPresence_Type = CfprApEquipmentPresence
_CfprApComputeExtBoardPresence_Object = MibTableColumn
cfprApComputeExtBoardPresence = _CfprApComputeExtBoardPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 21),
    _CfprApComputeExtBoardPresence_Type()
)
cfprApComputeExtBoardPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardPresence.setStatus("current")
_CfprApComputeExtBoardRevision_Type = SnmpAdminString
_CfprApComputeExtBoardRevision_Object = MibTableColumn
cfprApComputeExtBoardRevision = _CfprApComputeExtBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 22),
    _CfprApComputeExtBoardRevision_Type()
)
cfprApComputeExtBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardRevision.setStatus("current")
_CfprApComputeExtBoardSerial_Type = SnmpAdminString
_CfprApComputeExtBoardSerial_Object = MibTableColumn
cfprApComputeExtBoardSerial = _CfprApComputeExtBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 23),
    _CfprApComputeExtBoardSerial_Type()
)
cfprApComputeExtBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardSerial.setStatus("current")
_CfprApComputeExtBoardSlotId_Type = Gauge32
_CfprApComputeExtBoardSlotId_Object = MibTableColumn
cfprApComputeExtBoardSlotId = _CfprApComputeExtBoardSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 24),
    _CfprApComputeExtBoardSlotId_Type()
)
cfprApComputeExtBoardSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardSlotId.setStatus("current")
_CfprApComputeExtBoardThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeExtBoardThermal_Object = MibTableColumn
cfprApComputeExtBoardThermal = _CfprApComputeExtBoardThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 25),
    _CfprApComputeExtBoardThermal_Type()
)
cfprApComputeExtBoardThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardThermal.setStatus("current")
_CfprApComputeExtBoardVendor_Type = SnmpAdminString
_CfprApComputeExtBoardVendor_Object = MibTableColumn
cfprApComputeExtBoardVendor = _CfprApComputeExtBoardVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 26),
    _CfprApComputeExtBoardVendor_Type()
)
cfprApComputeExtBoardVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardVendor.setStatus("current")
_CfprApComputeExtBoardVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeExtBoardVoltage_Object = MibTableColumn
cfprApComputeExtBoardVoltage = _CfprApComputeExtBoardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 15, 1, 27),
    _CfprApComputeExtBoardVoltage_Type()
)
cfprApComputeExtBoardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeExtBoardVoltage.setStatus("current")
_CfprApComputeFwSyncAckTable_Object = MibTable
cfprApComputeFwSyncAckTable = _CfprApComputeFwSyncAckTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16)
)
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckTable.setStatus("current")
_CfprApComputeFwSyncAckEntry_Object = MibTableRow
cfprApComputeFwSyncAckEntry = _CfprApComputeFwSyncAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1)
)
cfprApComputeFwSyncAckEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeFwSyncAckInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckEntry.setStatus("current")
_CfprApComputeFwSyncAckInstanceId_Type = CfprApManagedObjectId
_CfprApComputeFwSyncAckInstanceId_Object = MibTableColumn
cfprApComputeFwSyncAckInstanceId = _CfprApComputeFwSyncAckInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 1),
    _CfprApComputeFwSyncAckInstanceId_Type()
)
cfprApComputeFwSyncAckInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckInstanceId.setStatus("current")
_CfprApComputeFwSyncAckDn_Type = CfprApManagedObjectDn
_CfprApComputeFwSyncAckDn_Object = MibTableColumn
cfprApComputeFwSyncAckDn = _CfprApComputeFwSyncAckDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 2),
    _CfprApComputeFwSyncAckDn_Type()
)
cfprApComputeFwSyncAckDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckDn.setStatus("current")
_CfprApComputeFwSyncAckRn_Type = SnmpAdminString
_CfprApComputeFwSyncAckRn_Object = MibTableColumn
cfprApComputeFwSyncAckRn = _CfprApComputeFwSyncAckRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 3),
    _CfprApComputeFwSyncAckRn_Type()
)
cfprApComputeFwSyncAckRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckRn.setStatus("current")
_CfprApComputeFwSyncAckAcked_Type = DateAndTime
_CfprApComputeFwSyncAckAcked_Object = MibTableColumn
cfprApComputeFwSyncAckAcked = _CfprApComputeFwSyncAckAcked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 4),
    _CfprApComputeFwSyncAckAcked_Type()
)
cfprApComputeFwSyncAckAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckAcked.setStatus("current")
_CfprApComputeFwSyncAckAckedBy_Type = SnmpAdminString
_CfprApComputeFwSyncAckAckedBy_Object = MibTableColumn
cfprApComputeFwSyncAckAckedBy = _CfprApComputeFwSyncAckAckedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 5),
    _CfprApComputeFwSyncAckAckedBy_Type()
)
cfprApComputeFwSyncAckAckedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckAckedBy.setStatus("current")
_CfprApComputeFwSyncAckAdminState_Type = CfprApTrigAdminState
_CfprApComputeFwSyncAckAdminState_Object = MibTableColumn
cfprApComputeFwSyncAckAdminState = _CfprApComputeFwSyncAckAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 6),
    _CfprApComputeFwSyncAckAdminState_Type()
)
cfprApComputeFwSyncAckAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckAdminState.setStatus("current")
_CfprApComputeFwSyncAckAutoDelete_Type = TruthValue
_CfprApComputeFwSyncAckAutoDelete_Object = MibTableColumn
cfprApComputeFwSyncAckAutoDelete = _CfprApComputeFwSyncAckAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 7),
    _CfprApComputeFwSyncAckAutoDelete_Type()
)
cfprApComputeFwSyncAckAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckAutoDelete.setStatus("current")
_CfprApComputeFwSyncAckChangeBy_Type = SnmpAdminString
_CfprApComputeFwSyncAckChangeBy_Object = MibTableColumn
cfprApComputeFwSyncAckChangeBy = _CfprApComputeFwSyncAckChangeBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 8),
    _CfprApComputeFwSyncAckChangeBy_Type()
)
cfprApComputeFwSyncAckChangeBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckChangeBy.setStatus("current")
_CfprApComputeFwSyncAckChangeDetails_Type = CfprApTrigAckChangeDetails
_CfprApComputeFwSyncAckChangeDetails_Object = MibTableColumn
cfprApComputeFwSyncAckChangeDetails = _CfprApComputeFwSyncAckChangeDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 9),
    _CfprApComputeFwSyncAckChangeDetails_Type()
)
cfprApComputeFwSyncAckChangeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckChangeDetails.setStatus("current")
_CfprApComputeFwSyncAckChanges_Type = CfprApTrigAckChanges
_CfprApComputeFwSyncAckChanges_Object = MibTableColumn
cfprApComputeFwSyncAckChanges = _CfprApComputeFwSyncAckChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 10),
    _CfprApComputeFwSyncAckChanges_Type()
)
cfprApComputeFwSyncAckChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckChanges.setStatus("current")
_CfprApComputeFwSyncAckDescr_Type = SnmpAdminString
_CfprApComputeFwSyncAckDescr_Object = MibTableColumn
cfprApComputeFwSyncAckDescr = _CfprApComputeFwSyncAckDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 11),
    _CfprApComputeFwSyncAckDescr_Type()
)
cfprApComputeFwSyncAckDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckDescr.setStatus("current")
_CfprApComputeFwSyncAckDisr_Type = CfprApTrigAckDisr
_CfprApComputeFwSyncAckDisr_Object = MibTableColumn
cfprApComputeFwSyncAckDisr = _CfprApComputeFwSyncAckDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 12),
    _CfprApComputeFwSyncAckDisr_Type()
)
cfprApComputeFwSyncAckDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckDisr.setStatus("current")
_CfprApComputeFwSyncAckIgnoreCap_Type = TruthValue
_CfprApComputeFwSyncAckIgnoreCap_Object = MibTableColumn
cfprApComputeFwSyncAckIgnoreCap = _CfprApComputeFwSyncAckIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 13),
    _CfprApComputeFwSyncAckIgnoreCap_Type()
)
cfprApComputeFwSyncAckIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckIgnoreCap.setStatus("current")
_CfprApComputeFwSyncAckIntId_Type = SnmpAdminString
_CfprApComputeFwSyncAckIntId_Object = MibTableColumn
cfprApComputeFwSyncAckIntId = _CfprApComputeFwSyncAckIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 14),
    _CfprApComputeFwSyncAckIntId_Type()
)
cfprApComputeFwSyncAckIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckIntId.setStatus("current")
_CfprApComputeFwSyncAckModified_Type = DateAndTime
_CfprApComputeFwSyncAckModified_Object = MibTableColumn
cfprApComputeFwSyncAckModified = _CfprApComputeFwSyncAckModified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 15),
    _CfprApComputeFwSyncAckModified_Type()
)
cfprApComputeFwSyncAckModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckModified.setStatus("current")
_CfprApComputeFwSyncAckName_Type = SnmpAdminString
_CfprApComputeFwSyncAckName_Object = MibTableColumn
cfprApComputeFwSyncAckName = _CfprApComputeFwSyncAckName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 16),
    _CfprApComputeFwSyncAckName_Type()
)
cfprApComputeFwSyncAckName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckName.setStatus("current")
_CfprApComputeFwSyncAckOperScheduler_Type = SnmpAdminString
_CfprApComputeFwSyncAckOperScheduler_Object = MibTableColumn
cfprApComputeFwSyncAckOperScheduler = _CfprApComputeFwSyncAckOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 17),
    _CfprApComputeFwSyncAckOperScheduler_Type()
)
cfprApComputeFwSyncAckOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckOperScheduler.setStatus("current")
_CfprApComputeFwSyncAckOperState_Type = CfprApTrigAckOperState
_CfprApComputeFwSyncAckOperState_Object = MibTableColumn
cfprApComputeFwSyncAckOperState = _CfprApComputeFwSyncAckOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 18),
    _CfprApComputeFwSyncAckOperState_Type()
)
cfprApComputeFwSyncAckOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckOperState.setStatus("current")
_CfprApComputeFwSyncAckPolicyLevel_Type = Gauge32
_CfprApComputeFwSyncAckPolicyLevel_Object = MibTableColumn
cfprApComputeFwSyncAckPolicyLevel = _CfprApComputeFwSyncAckPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 19),
    _CfprApComputeFwSyncAckPolicyLevel_Type()
)
cfprApComputeFwSyncAckPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckPolicyLevel.setStatus("current")
_CfprApComputeFwSyncAckPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeFwSyncAckPolicyOwner_Object = MibTableColumn
cfprApComputeFwSyncAckPolicyOwner = _CfprApComputeFwSyncAckPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 20),
    _CfprApComputeFwSyncAckPolicyOwner_Type()
)
cfprApComputeFwSyncAckPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckPolicyOwner.setStatus("current")
_CfprApComputeFwSyncAckPrevOperState_Type = CfprApTrigAckPrevOperState
_CfprApComputeFwSyncAckPrevOperState_Object = MibTableColumn
cfprApComputeFwSyncAckPrevOperState = _CfprApComputeFwSyncAckPrevOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 21),
    _CfprApComputeFwSyncAckPrevOperState_Type()
)
cfprApComputeFwSyncAckPrevOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckPrevOperState.setStatus("current")
_CfprApComputeFwSyncAckScheduler_Type = SnmpAdminString
_CfprApComputeFwSyncAckScheduler_Object = MibTableColumn
cfprApComputeFwSyncAckScheduler = _CfprApComputeFwSyncAckScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 16, 1, 22),
    _CfprApComputeFwSyncAckScheduler_Type()
)
cfprApComputeFwSyncAckScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeFwSyncAckScheduler.setStatus("current")
_CfprApComputeHealthLedSensorAlarmTable_Object = MibTable
cfprApComputeHealthLedSensorAlarmTable = _CfprApComputeHealthLedSensorAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 17)
)
if mibBuilder.loadTexts:
    cfprApComputeHealthLedSensorAlarmTable.setStatus("current")
_CfprApComputeHealthLedSensorAlarmEntry_Object = MibTableRow
cfprApComputeHealthLedSensorAlarmEntry = _CfprApComputeHealthLedSensorAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 17, 1)
)
cfprApComputeHealthLedSensorAlarmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeHealthLedSensorAlarmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeHealthLedSensorAlarmEntry.setStatus("current")
_CfprApComputeHealthLedSensorAlarmInstanceId_Type = CfprApManagedObjectId
_CfprApComputeHealthLedSensorAlarmInstanceId_Object = MibTableColumn
cfprApComputeHealthLedSensorAlarmInstanceId = _CfprApComputeHealthLedSensorAlarmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 17, 1, 1),
    _CfprApComputeHealthLedSensorAlarmInstanceId_Type()
)
cfprApComputeHealthLedSensorAlarmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeHealthLedSensorAlarmInstanceId.setStatus("current")
_CfprApComputeHealthLedSensorAlarmDn_Type = CfprApManagedObjectDn
_CfprApComputeHealthLedSensorAlarmDn_Object = MibTableColumn
cfprApComputeHealthLedSensorAlarmDn = _CfprApComputeHealthLedSensorAlarmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 17, 1, 2),
    _CfprApComputeHealthLedSensorAlarmDn_Type()
)
cfprApComputeHealthLedSensorAlarmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeHealthLedSensorAlarmDn.setStatus("current")
_CfprApComputeHealthLedSensorAlarmRn_Type = SnmpAdminString
_CfprApComputeHealthLedSensorAlarmRn_Object = MibTableColumn
cfprApComputeHealthLedSensorAlarmRn = _CfprApComputeHealthLedSensorAlarmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 17, 1, 3),
    _CfprApComputeHealthLedSensorAlarmRn_Type()
)
cfprApComputeHealthLedSensorAlarmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeHealthLedSensorAlarmRn.setStatus("current")
_CfprApComputeHealthLedSensorAlarmAlarmDesc_Type = SnmpAdminString
_CfprApComputeHealthLedSensorAlarmAlarmDesc_Object = MibTableColumn
cfprApComputeHealthLedSensorAlarmAlarmDesc = _CfprApComputeHealthLedSensorAlarmAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 17, 1, 4),
    _CfprApComputeHealthLedSensorAlarmAlarmDesc_Type()
)
cfprApComputeHealthLedSensorAlarmAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeHealthLedSensorAlarmAlarmDesc.setStatus("current")
_CfprApComputeHealthLedSensorAlarmAlarmSeverity_Type = CfprApComputeAlarmSeverity
_CfprApComputeHealthLedSensorAlarmAlarmSeverity_Object = MibTableColumn
cfprApComputeHealthLedSensorAlarmAlarmSeverity = _CfprApComputeHealthLedSensorAlarmAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 17, 1, 5),
    _CfprApComputeHealthLedSensorAlarmAlarmSeverity_Type()
)
cfprApComputeHealthLedSensorAlarmAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeHealthLedSensorAlarmAlarmSeverity.setStatus("current")
_CfprApComputeHealthLedSensorAlarmSensorId_Type = Gauge32
_CfprApComputeHealthLedSensorAlarmSensorId_Object = MibTableColumn
cfprApComputeHealthLedSensorAlarmSensorId = _CfprApComputeHealthLedSensorAlarmSensorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 17, 1, 6),
    _CfprApComputeHealthLedSensorAlarmSensorId_Type()
)
cfprApComputeHealthLedSensorAlarmSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeHealthLedSensorAlarmSensorId.setStatus("current")
_CfprApComputeHealthLedSensorAlarmSensorName_Type = SnmpAdminString
_CfprApComputeHealthLedSensorAlarmSensorName_Object = MibTableColumn
cfprApComputeHealthLedSensorAlarmSensorName = _CfprApComputeHealthLedSensorAlarmSensorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 17, 1, 7),
    _CfprApComputeHealthLedSensorAlarmSensorName_Type()
)
cfprApComputeHealthLedSensorAlarmSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeHealthLedSensorAlarmSensorName.setStatus("current")
_CfprApComputeIOHubTable_Object = MibTable
cfprApComputeIOHubTable = _CfprApComputeIOHubTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18)
)
if mibBuilder.loadTexts:
    cfprApComputeIOHubTable.setStatus("current")
_CfprApComputeIOHubEntry_Object = MibTableRow
cfprApComputeIOHubEntry = _CfprApComputeIOHubEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1)
)
cfprApComputeIOHubEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeIOHubInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeIOHubEntry.setStatus("current")
_CfprApComputeIOHubInstanceId_Type = CfprApManagedObjectId
_CfprApComputeIOHubInstanceId_Object = MibTableColumn
cfprApComputeIOHubInstanceId = _CfprApComputeIOHubInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 1),
    _CfprApComputeIOHubInstanceId_Type()
)
cfprApComputeIOHubInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeIOHubInstanceId.setStatus("current")
_CfprApComputeIOHubDn_Type = CfprApManagedObjectDn
_CfprApComputeIOHubDn_Object = MibTableColumn
cfprApComputeIOHubDn = _CfprApComputeIOHubDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 2),
    _CfprApComputeIOHubDn_Type()
)
cfprApComputeIOHubDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubDn.setStatus("current")
_CfprApComputeIOHubRn_Type = SnmpAdminString
_CfprApComputeIOHubRn_Object = MibTableColumn
cfprApComputeIOHubRn = _CfprApComputeIOHubRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 3),
    _CfprApComputeIOHubRn_Type()
)
cfprApComputeIOHubRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubRn.setStatus("current")
_CfprApComputeIOHubId_Type = Gauge32
_CfprApComputeIOHubId_Object = MibTableColumn
cfprApComputeIOHubId = _CfprApComputeIOHubId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 4),
    _CfprApComputeIOHubId_Type()
)
cfprApComputeIOHubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubId.setStatus("current")
_CfprApComputeIOHubLocationDn_Type = SnmpAdminString
_CfprApComputeIOHubLocationDn_Object = MibTableColumn
cfprApComputeIOHubLocationDn = _CfprApComputeIOHubLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 5),
    _CfprApComputeIOHubLocationDn_Type()
)
cfprApComputeIOHubLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubLocationDn.setStatus("current")
_CfprApComputeIOHubModel_Type = SnmpAdminString
_CfprApComputeIOHubModel_Object = MibTableColumn
cfprApComputeIOHubModel = _CfprApComputeIOHubModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 6),
    _CfprApComputeIOHubModel_Type()
)
cfprApComputeIOHubModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubModel.setStatus("current")
_CfprApComputeIOHubOperQualifierReason_Type = SnmpAdminString
_CfprApComputeIOHubOperQualifierReason_Object = MibTableColumn
cfprApComputeIOHubOperQualifierReason = _CfprApComputeIOHubOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 7),
    _CfprApComputeIOHubOperQualifierReason_Type()
)
cfprApComputeIOHubOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubOperQualifierReason.setStatus("current")
_CfprApComputeIOHubOperState_Type = CfprApEquipmentOperability
_CfprApComputeIOHubOperState_Object = MibTableColumn
cfprApComputeIOHubOperState = _CfprApComputeIOHubOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 8),
    _CfprApComputeIOHubOperState_Type()
)
cfprApComputeIOHubOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubOperState.setStatus("current")
_CfprApComputeIOHubOperability_Type = CfprApEquipmentOperability
_CfprApComputeIOHubOperability_Object = MibTableColumn
cfprApComputeIOHubOperability = _CfprApComputeIOHubOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 9),
    _CfprApComputeIOHubOperability_Type()
)
cfprApComputeIOHubOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubOperability.setStatus("current")
_CfprApComputeIOHubPerf_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeIOHubPerf_Object = MibTableColumn
cfprApComputeIOHubPerf = _CfprApComputeIOHubPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 10),
    _CfprApComputeIOHubPerf_Type()
)
cfprApComputeIOHubPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubPerf.setStatus("current")
_CfprApComputeIOHubPower_Type = CfprApEquipmentPowerState
_CfprApComputeIOHubPower_Object = MibTableColumn
cfprApComputeIOHubPower = _CfprApComputeIOHubPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 11),
    _CfprApComputeIOHubPower_Type()
)
cfprApComputeIOHubPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubPower.setStatus("current")
_CfprApComputeIOHubPresence_Type = CfprApEquipmentPresence
_CfprApComputeIOHubPresence_Object = MibTableColumn
cfprApComputeIOHubPresence = _CfprApComputeIOHubPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 12),
    _CfprApComputeIOHubPresence_Type()
)
cfprApComputeIOHubPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubPresence.setStatus("current")
_CfprApComputeIOHubRevision_Type = SnmpAdminString
_CfprApComputeIOHubRevision_Object = MibTableColumn
cfprApComputeIOHubRevision = _CfprApComputeIOHubRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 13),
    _CfprApComputeIOHubRevision_Type()
)
cfprApComputeIOHubRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubRevision.setStatus("current")
_CfprApComputeIOHubSerial_Type = SnmpAdminString
_CfprApComputeIOHubSerial_Object = MibTableColumn
cfprApComputeIOHubSerial = _CfprApComputeIOHubSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 14),
    _CfprApComputeIOHubSerial_Type()
)
cfprApComputeIOHubSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubSerial.setStatus("current")
_CfprApComputeIOHubThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeIOHubThermal_Object = MibTableColumn
cfprApComputeIOHubThermal = _CfprApComputeIOHubThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 15),
    _CfprApComputeIOHubThermal_Type()
)
cfprApComputeIOHubThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubThermal.setStatus("current")
_CfprApComputeIOHubVendor_Type = SnmpAdminString
_CfprApComputeIOHubVendor_Object = MibTableColumn
cfprApComputeIOHubVendor = _CfprApComputeIOHubVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 16),
    _CfprApComputeIOHubVendor_Type()
)
cfprApComputeIOHubVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubVendor.setStatus("current")
_CfprApComputeIOHubVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeIOHubVoltage_Object = MibTableColumn
cfprApComputeIOHubVoltage = _CfprApComputeIOHubVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 18, 1, 17),
    _CfprApComputeIOHubVoltage_Type()
)
cfprApComputeIOHubVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubVoltage.setStatus("current")
_CfprApComputeIOHubEnvStatsTable_Object = MibTable
cfprApComputeIOHubEnvStatsTable = _CfprApComputeIOHubEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19)
)
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsTable.setStatus("current")
_CfprApComputeIOHubEnvStatsEntry_Object = MibTableRow
cfprApComputeIOHubEnvStatsEntry = _CfprApComputeIOHubEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1)
)
cfprApComputeIOHubEnvStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeIOHubEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsEntry.setStatus("current")
_CfprApComputeIOHubEnvStatsInstanceId_Type = CfprApManagedObjectId
_CfprApComputeIOHubEnvStatsInstanceId_Object = MibTableColumn
cfprApComputeIOHubEnvStatsInstanceId = _CfprApComputeIOHubEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1, 1),
    _CfprApComputeIOHubEnvStatsInstanceId_Type()
)
cfprApComputeIOHubEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsInstanceId.setStatus("current")
_CfprApComputeIOHubEnvStatsDn_Type = CfprApManagedObjectDn
_CfprApComputeIOHubEnvStatsDn_Object = MibTableColumn
cfprApComputeIOHubEnvStatsDn = _CfprApComputeIOHubEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1, 2),
    _CfprApComputeIOHubEnvStatsDn_Type()
)
cfprApComputeIOHubEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsDn.setStatus("current")
_CfprApComputeIOHubEnvStatsRn_Type = SnmpAdminString
_CfprApComputeIOHubEnvStatsRn_Object = MibTableColumn
cfprApComputeIOHubEnvStatsRn = _CfprApComputeIOHubEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1, 3),
    _CfprApComputeIOHubEnvStatsRn_Type()
)
cfprApComputeIOHubEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsRn.setStatus("current")
_CfprApComputeIOHubEnvStatsIntervals_Type = Gauge32
_CfprApComputeIOHubEnvStatsIntervals_Object = MibTableColumn
cfprApComputeIOHubEnvStatsIntervals = _CfprApComputeIOHubEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1, 4),
    _CfprApComputeIOHubEnvStatsIntervals_Type()
)
cfprApComputeIOHubEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsIntervals.setStatus("current")
_CfprApComputeIOHubEnvStatsSuspect_Type = TruthValue
_CfprApComputeIOHubEnvStatsSuspect_Object = MibTableColumn
cfprApComputeIOHubEnvStatsSuspect = _CfprApComputeIOHubEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1, 5),
    _CfprApComputeIOHubEnvStatsSuspect_Type()
)
cfprApComputeIOHubEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsSuspect.setStatus("current")
_CfprApComputeIOHubEnvStatsTemperature_Type = Integer32
_CfprApComputeIOHubEnvStatsTemperature_Object = MibTableColumn
cfprApComputeIOHubEnvStatsTemperature = _CfprApComputeIOHubEnvStatsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1, 6),
    _CfprApComputeIOHubEnvStatsTemperature_Type()
)
cfprApComputeIOHubEnvStatsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsTemperature.setStatus("current")
_CfprApComputeIOHubEnvStatsTemperatureAvg_Type = Integer32
_CfprApComputeIOHubEnvStatsTemperatureAvg_Object = MibTableColumn
cfprApComputeIOHubEnvStatsTemperatureAvg = _CfprApComputeIOHubEnvStatsTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1, 7),
    _CfprApComputeIOHubEnvStatsTemperatureAvg_Type()
)
cfprApComputeIOHubEnvStatsTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsTemperatureAvg.setStatus("current")
_CfprApComputeIOHubEnvStatsTemperatureMax_Type = Integer32
_CfprApComputeIOHubEnvStatsTemperatureMax_Object = MibTableColumn
cfprApComputeIOHubEnvStatsTemperatureMax = _CfprApComputeIOHubEnvStatsTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1, 8),
    _CfprApComputeIOHubEnvStatsTemperatureMax_Type()
)
cfprApComputeIOHubEnvStatsTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsTemperatureMax.setStatus("current")
_CfprApComputeIOHubEnvStatsTemperatureMin_Type = Integer32
_CfprApComputeIOHubEnvStatsTemperatureMin_Object = MibTableColumn
cfprApComputeIOHubEnvStatsTemperatureMin = _CfprApComputeIOHubEnvStatsTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1, 9),
    _CfprApComputeIOHubEnvStatsTemperatureMin_Type()
)
cfprApComputeIOHubEnvStatsTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsTemperatureMin.setStatus("current")
_CfprApComputeIOHubEnvStatsThresholded_Type = CfprApComputeIOHubEnvStatsThresholded
_CfprApComputeIOHubEnvStatsThresholded_Object = MibTableColumn
cfprApComputeIOHubEnvStatsThresholded = _CfprApComputeIOHubEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1, 10),
    _CfprApComputeIOHubEnvStatsThresholded_Type()
)
cfprApComputeIOHubEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsThresholded.setStatus("current")
_CfprApComputeIOHubEnvStatsTimeCollected_Type = DateAndTime
_CfprApComputeIOHubEnvStatsTimeCollected_Object = MibTableColumn
cfprApComputeIOHubEnvStatsTimeCollected = _CfprApComputeIOHubEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1, 11),
    _CfprApComputeIOHubEnvStatsTimeCollected_Type()
)
cfprApComputeIOHubEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsTimeCollected.setStatus("current")
_CfprApComputeIOHubEnvStatsUpdate_Type = Gauge32
_CfprApComputeIOHubEnvStatsUpdate_Object = MibTableColumn
cfprApComputeIOHubEnvStatsUpdate = _CfprApComputeIOHubEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 19, 1, 12),
    _CfprApComputeIOHubEnvStatsUpdate_Type()
)
cfprApComputeIOHubEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsUpdate.setStatus("current")
_CfprApComputeIOHubEnvStatsHistTable_Object = MibTable
cfprApComputeIOHubEnvStatsHistTable = _CfprApComputeIOHubEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20)
)
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistTable.setStatus("current")
_CfprApComputeIOHubEnvStatsHistEntry_Object = MibTableRow
cfprApComputeIOHubEnvStatsHistEntry = _CfprApComputeIOHubEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1)
)
cfprApComputeIOHubEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeIOHubEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistEntry.setStatus("current")
_CfprApComputeIOHubEnvStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApComputeIOHubEnvStatsHistInstanceId_Object = MibTableColumn
cfprApComputeIOHubEnvStatsHistInstanceId = _CfprApComputeIOHubEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1, 1),
    _CfprApComputeIOHubEnvStatsHistInstanceId_Type()
)
cfprApComputeIOHubEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistInstanceId.setStatus("current")
_CfprApComputeIOHubEnvStatsHistDn_Type = CfprApManagedObjectDn
_CfprApComputeIOHubEnvStatsHistDn_Object = MibTableColumn
cfprApComputeIOHubEnvStatsHistDn = _CfprApComputeIOHubEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1, 2),
    _CfprApComputeIOHubEnvStatsHistDn_Type()
)
cfprApComputeIOHubEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistDn.setStatus("current")
_CfprApComputeIOHubEnvStatsHistRn_Type = SnmpAdminString
_CfprApComputeIOHubEnvStatsHistRn_Object = MibTableColumn
cfprApComputeIOHubEnvStatsHistRn = _CfprApComputeIOHubEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1, 3),
    _CfprApComputeIOHubEnvStatsHistRn_Type()
)
cfprApComputeIOHubEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistRn.setStatus("current")
_CfprApComputeIOHubEnvStatsHistId_Type = Unsigned64
_CfprApComputeIOHubEnvStatsHistId_Object = MibTableColumn
cfprApComputeIOHubEnvStatsHistId = _CfprApComputeIOHubEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1, 4),
    _CfprApComputeIOHubEnvStatsHistId_Type()
)
cfprApComputeIOHubEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistId.setStatus("current")
_CfprApComputeIOHubEnvStatsHistMostRecent_Type = TruthValue
_CfprApComputeIOHubEnvStatsHistMostRecent_Object = MibTableColumn
cfprApComputeIOHubEnvStatsHistMostRecent = _CfprApComputeIOHubEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1, 5),
    _CfprApComputeIOHubEnvStatsHistMostRecent_Type()
)
cfprApComputeIOHubEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistMostRecent.setStatus("current")
_CfprApComputeIOHubEnvStatsHistSuspect_Type = TruthValue
_CfprApComputeIOHubEnvStatsHistSuspect_Object = MibTableColumn
cfprApComputeIOHubEnvStatsHistSuspect = _CfprApComputeIOHubEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1, 6),
    _CfprApComputeIOHubEnvStatsHistSuspect_Type()
)
cfprApComputeIOHubEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistSuspect.setStatus("current")
_CfprApComputeIOHubEnvStatsHistTemperature_Type = Integer32
_CfprApComputeIOHubEnvStatsHistTemperature_Object = MibTableColumn
cfprApComputeIOHubEnvStatsHistTemperature = _CfprApComputeIOHubEnvStatsHistTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1, 7),
    _CfprApComputeIOHubEnvStatsHistTemperature_Type()
)
cfprApComputeIOHubEnvStatsHistTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistTemperature.setStatus("current")
_CfprApComputeIOHubEnvStatsHistTemperatureAvg_Type = Integer32
_CfprApComputeIOHubEnvStatsHistTemperatureAvg_Object = MibTableColumn
cfprApComputeIOHubEnvStatsHistTemperatureAvg = _CfprApComputeIOHubEnvStatsHistTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1, 8),
    _CfprApComputeIOHubEnvStatsHistTemperatureAvg_Type()
)
cfprApComputeIOHubEnvStatsHistTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistTemperatureAvg.setStatus("current")
_CfprApComputeIOHubEnvStatsHistTemperatureMax_Type = Integer32
_CfprApComputeIOHubEnvStatsHistTemperatureMax_Object = MibTableColumn
cfprApComputeIOHubEnvStatsHistTemperatureMax = _CfprApComputeIOHubEnvStatsHistTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1, 9),
    _CfprApComputeIOHubEnvStatsHistTemperatureMax_Type()
)
cfprApComputeIOHubEnvStatsHistTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistTemperatureMax.setStatus("current")
_CfprApComputeIOHubEnvStatsHistTemperatureMin_Type = Integer32
_CfprApComputeIOHubEnvStatsHistTemperatureMin_Object = MibTableColumn
cfprApComputeIOHubEnvStatsHistTemperatureMin = _CfprApComputeIOHubEnvStatsHistTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1, 10),
    _CfprApComputeIOHubEnvStatsHistTemperatureMin_Type()
)
cfprApComputeIOHubEnvStatsHistTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistTemperatureMin.setStatus("current")
_CfprApComputeIOHubEnvStatsHistThresholded_Type = CfprApComputeIOHubEnvStatsHistThresholded
_CfprApComputeIOHubEnvStatsHistThresholded_Object = MibTableColumn
cfprApComputeIOHubEnvStatsHistThresholded = _CfprApComputeIOHubEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1, 11),
    _CfprApComputeIOHubEnvStatsHistThresholded_Type()
)
cfprApComputeIOHubEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistThresholded.setStatus("current")
_CfprApComputeIOHubEnvStatsHistTimeCollected_Type = DateAndTime
_CfprApComputeIOHubEnvStatsHistTimeCollected_Object = MibTableColumn
cfprApComputeIOHubEnvStatsHistTimeCollected = _CfprApComputeIOHubEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 20, 1, 12),
    _CfprApComputeIOHubEnvStatsHistTimeCollected_Type()
)
cfprApComputeIOHubEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeIOHubEnvStatsHistTimeCollected.setStatus("current")
_CfprApComputeMbPowerStatsTable_Object = MibTable
cfprApComputeMbPowerStatsTable = _CfprApComputeMbPowerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22)
)
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsTable.setStatus("current")
_CfprApComputeMbPowerStatsEntry_Object = MibTableRow
cfprApComputeMbPowerStatsEntry = _CfprApComputeMbPowerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1)
)
cfprApComputeMbPowerStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeMbPowerStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsEntry.setStatus("current")
_CfprApComputeMbPowerStatsInstanceId_Type = CfprApManagedObjectId
_CfprApComputeMbPowerStatsInstanceId_Object = MibTableColumn
cfprApComputeMbPowerStatsInstanceId = _CfprApComputeMbPowerStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 1),
    _CfprApComputeMbPowerStatsInstanceId_Type()
)
cfprApComputeMbPowerStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsInstanceId.setStatus("current")
_CfprApComputeMbPowerStatsDn_Type = CfprApManagedObjectDn
_CfprApComputeMbPowerStatsDn_Object = MibTableColumn
cfprApComputeMbPowerStatsDn = _CfprApComputeMbPowerStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 2),
    _CfprApComputeMbPowerStatsDn_Type()
)
cfprApComputeMbPowerStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsDn.setStatus("current")
_CfprApComputeMbPowerStatsRn_Type = SnmpAdminString
_CfprApComputeMbPowerStatsRn_Object = MibTableColumn
cfprApComputeMbPowerStatsRn = _CfprApComputeMbPowerStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 3),
    _CfprApComputeMbPowerStatsRn_Type()
)
cfprApComputeMbPowerStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsRn.setStatus("current")
_CfprApComputeMbPowerStatsConsumedPower_Type = Integer32
_CfprApComputeMbPowerStatsConsumedPower_Object = MibTableColumn
cfprApComputeMbPowerStatsConsumedPower = _CfprApComputeMbPowerStatsConsumedPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 4),
    _CfprApComputeMbPowerStatsConsumedPower_Type()
)
cfprApComputeMbPowerStatsConsumedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsConsumedPower.setStatus("current")
_CfprApComputeMbPowerStatsConsumedPowerAvg_Type = Integer32
_CfprApComputeMbPowerStatsConsumedPowerAvg_Object = MibTableColumn
cfprApComputeMbPowerStatsConsumedPowerAvg = _CfprApComputeMbPowerStatsConsumedPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 5),
    _CfprApComputeMbPowerStatsConsumedPowerAvg_Type()
)
cfprApComputeMbPowerStatsConsumedPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsConsumedPowerAvg.setStatus("current")
_CfprApComputeMbPowerStatsConsumedPowerMax_Type = Integer32
_CfprApComputeMbPowerStatsConsumedPowerMax_Object = MibTableColumn
cfprApComputeMbPowerStatsConsumedPowerMax = _CfprApComputeMbPowerStatsConsumedPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 6),
    _CfprApComputeMbPowerStatsConsumedPowerMax_Type()
)
cfprApComputeMbPowerStatsConsumedPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsConsumedPowerMax.setStatus("current")
_CfprApComputeMbPowerStatsConsumedPowerMin_Type = Integer32
_CfprApComputeMbPowerStatsConsumedPowerMin_Object = MibTableColumn
cfprApComputeMbPowerStatsConsumedPowerMin = _CfprApComputeMbPowerStatsConsumedPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 7),
    _CfprApComputeMbPowerStatsConsumedPowerMin_Type()
)
cfprApComputeMbPowerStatsConsumedPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsConsumedPowerMin.setStatus("current")
_CfprApComputeMbPowerStatsInputCurrent_Type = Integer32
_CfprApComputeMbPowerStatsInputCurrent_Object = MibTableColumn
cfprApComputeMbPowerStatsInputCurrent = _CfprApComputeMbPowerStatsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 8),
    _CfprApComputeMbPowerStatsInputCurrent_Type()
)
cfprApComputeMbPowerStatsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsInputCurrent.setStatus("current")
_CfprApComputeMbPowerStatsInputCurrentAvg_Type = Integer32
_CfprApComputeMbPowerStatsInputCurrentAvg_Object = MibTableColumn
cfprApComputeMbPowerStatsInputCurrentAvg = _CfprApComputeMbPowerStatsInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 9),
    _CfprApComputeMbPowerStatsInputCurrentAvg_Type()
)
cfprApComputeMbPowerStatsInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsInputCurrentAvg.setStatus("current")
_CfprApComputeMbPowerStatsInputCurrentMax_Type = Integer32
_CfprApComputeMbPowerStatsInputCurrentMax_Object = MibTableColumn
cfprApComputeMbPowerStatsInputCurrentMax = _CfprApComputeMbPowerStatsInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 10),
    _CfprApComputeMbPowerStatsInputCurrentMax_Type()
)
cfprApComputeMbPowerStatsInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsInputCurrentMax.setStatus("current")
_CfprApComputeMbPowerStatsInputCurrentMin_Type = Integer32
_CfprApComputeMbPowerStatsInputCurrentMin_Object = MibTableColumn
cfprApComputeMbPowerStatsInputCurrentMin = _CfprApComputeMbPowerStatsInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 11),
    _CfprApComputeMbPowerStatsInputCurrentMin_Type()
)
cfprApComputeMbPowerStatsInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsInputCurrentMin.setStatus("current")
_CfprApComputeMbPowerStatsInputVoltage_Type = Integer32
_CfprApComputeMbPowerStatsInputVoltage_Object = MibTableColumn
cfprApComputeMbPowerStatsInputVoltage = _CfprApComputeMbPowerStatsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 12),
    _CfprApComputeMbPowerStatsInputVoltage_Type()
)
cfprApComputeMbPowerStatsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsInputVoltage.setStatus("current")
_CfprApComputeMbPowerStatsInputVoltageAvg_Type = Integer32
_CfprApComputeMbPowerStatsInputVoltageAvg_Object = MibTableColumn
cfprApComputeMbPowerStatsInputVoltageAvg = _CfprApComputeMbPowerStatsInputVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 13),
    _CfprApComputeMbPowerStatsInputVoltageAvg_Type()
)
cfprApComputeMbPowerStatsInputVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsInputVoltageAvg.setStatus("current")
_CfprApComputeMbPowerStatsInputVoltageMax_Type = Integer32
_CfprApComputeMbPowerStatsInputVoltageMax_Object = MibTableColumn
cfprApComputeMbPowerStatsInputVoltageMax = _CfprApComputeMbPowerStatsInputVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 14),
    _CfprApComputeMbPowerStatsInputVoltageMax_Type()
)
cfprApComputeMbPowerStatsInputVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsInputVoltageMax.setStatus("current")
_CfprApComputeMbPowerStatsInputVoltageMin_Type = Integer32
_CfprApComputeMbPowerStatsInputVoltageMin_Object = MibTableColumn
cfprApComputeMbPowerStatsInputVoltageMin = _CfprApComputeMbPowerStatsInputVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 15),
    _CfprApComputeMbPowerStatsInputVoltageMin_Type()
)
cfprApComputeMbPowerStatsInputVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsInputVoltageMin.setStatus("current")
_CfprApComputeMbPowerStatsIntervals_Type = Gauge32
_CfprApComputeMbPowerStatsIntervals_Object = MibTableColumn
cfprApComputeMbPowerStatsIntervals = _CfprApComputeMbPowerStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 16),
    _CfprApComputeMbPowerStatsIntervals_Type()
)
cfprApComputeMbPowerStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsIntervals.setStatus("current")
_CfprApComputeMbPowerStatsSuspect_Type = TruthValue
_CfprApComputeMbPowerStatsSuspect_Object = MibTableColumn
cfprApComputeMbPowerStatsSuspect = _CfprApComputeMbPowerStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 17),
    _CfprApComputeMbPowerStatsSuspect_Type()
)
cfprApComputeMbPowerStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsSuspect.setStatus("current")
_CfprApComputeMbPowerStatsThresholded_Type = CfprApComputeMbPowerStatsThresholded
_CfprApComputeMbPowerStatsThresholded_Object = MibTableColumn
cfprApComputeMbPowerStatsThresholded = _CfprApComputeMbPowerStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 18),
    _CfprApComputeMbPowerStatsThresholded_Type()
)
cfprApComputeMbPowerStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsThresholded.setStatus("current")
_CfprApComputeMbPowerStatsTimeCollected_Type = DateAndTime
_CfprApComputeMbPowerStatsTimeCollected_Object = MibTableColumn
cfprApComputeMbPowerStatsTimeCollected = _CfprApComputeMbPowerStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 19),
    _CfprApComputeMbPowerStatsTimeCollected_Type()
)
cfprApComputeMbPowerStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsTimeCollected.setStatus("current")
_CfprApComputeMbPowerStatsUpdate_Type = Gauge32
_CfprApComputeMbPowerStatsUpdate_Object = MibTableColumn
cfprApComputeMbPowerStatsUpdate = _CfprApComputeMbPowerStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 22, 1, 20),
    _CfprApComputeMbPowerStatsUpdate_Type()
)
cfprApComputeMbPowerStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsUpdate.setStatus("current")
_CfprApComputeMbPowerStatsHistTable_Object = MibTable
cfprApComputeMbPowerStatsHistTable = _CfprApComputeMbPowerStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23)
)
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistTable.setStatus("current")
_CfprApComputeMbPowerStatsHistEntry_Object = MibTableRow
cfprApComputeMbPowerStatsHistEntry = _CfprApComputeMbPowerStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1)
)
cfprApComputeMbPowerStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeMbPowerStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistEntry.setStatus("current")
_CfprApComputeMbPowerStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApComputeMbPowerStatsHistInstanceId_Object = MibTableColumn
cfprApComputeMbPowerStatsHistInstanceId = _CfprApComputeMbPowerStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 1),
    _CfprApComputeMbPowerStatsHistInstanceId_Type()
)
cfprApComputeMbPowerStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistInstanceId.setStatus("current")
_CfprApComputeMbPowerStatsHistDn_Type = CfprApManagedObjectDn
_CfprApComputeMbPowerStatsHistDn_Object = MibTableColumn
cfprApComputeMbPowerStatsHistDn = _CfprApComputeMbPowerStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 2),
    _CfprApComputeMbPowerStatsHistDn_Type()
)
cfprApComputeMbPowerStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistDn.setStatus("current")
_CfprApComputeMbPowerStatsHistRn_Type = SnmpAdminString
_CfprApComputeMbPowerStatsHistRn_Object = MibTableColumn
cfprApComputeMbPowerStatsHistRn = _CfprApComputeMbPowerStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 3),
    _CfprApComputeMbPowerStatsHistRn_Type()
)
cfprApComputeMbPowerStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistRn.setStatus("current")
_CfprApComputeMbPowerStatsHistConsumedPower_Type = Integer32
_CfprApComputeMbPowerStatsHistConsumedPower_Object = MibTableColumn
cfprApComputeMbPowerStatsHistConsumedPower = _CfprApComputeMbPowerStatsHistConsumedPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 4),
    _CfprApComputeMbPowerStatsHistConsumedPower_Type()
)
cfprApComputeMbPowerStatsHistConsumedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistConsumedPower.setStatus("current")
_CfprApComputeMbPowerStatsHistConsumedPowerAvg_Type = Integer32
_CfprApComputeMbPowerStatsHistConsumedPowerAvg_Object = MibTableColumn
cfprApComputeMbPowerStatsHistConsumedPowerAvg = _CfprApComputeMbPowerStatsHistConsumedPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 5),
    _CfprApComputeMbPowerStatsHistConsumedPowerAvg_Type()
)
cfprApComputeMbPowerStatsHistConsumedPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistConsumedPowerAvg.setStatus("current")
_CfprApComputeMbPowerStatsHistConsumedPowerMax_Type = Integer32
_CfprApComputeMbPowerStatsHistConsumedPowerMax_Object = MibTableColumn
cfprApComputeMbPowerStatsHistConsumedPowerMax = _CfprApComputeMbPowerStatsHistConsumedPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 6),
    _CfprApComputeMbPowerStatsHistConsumedPowerMax_Type()
)
cfprApComputeMbPowerStatsHistConsumedPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistConsumedPowerMax.setStatus("current")
_CfprApComputeMbPowerStatsHistConsumedPowerMin_Type = Integer32
_CfprApComputeMbPowerStatsHistConsumedPowerMin_Object = MibTableColumn
cfprApComputeMbPowerStatsHistConsumedPowerMin = _CfprApComputeMbPowerStatsHistConsumedPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 7),
    _CfprApComputeMbPowerStatsHistConsumedPowerMin_Type()
)
cfprApComputeMbPowerStatsHistConsumedPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistConsumedPowerMin.setStatus("current")
_CfprApComputeMbPowerStatsHistId_Type = Unsigned64
_CfprApComputeMbPowerStatsHistId_Object = MibTableColumn
cfprApComputeMbPowerStatsHistId = _CfprApComputeMbPowerStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 8),
    _CfprApComputeMbPowerStatsHistId_Type()
)
cfprApComputeMbPowerStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistId.setStatus("current")
_CfprApComputeMbPowerStatsHistInputCurrent_Type = Integer32
_CfprApComputeMbPowerStatsHistInputCurrent_Object = MibTableColumn
cfprApComputeMbPowerStatsHistInputCurrent = _CfprApComputeMbPowerStatsHistInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 9),
    _CfprApComputeMbPowerStatsHistInputCurrent_Type()
)
cfprApComputeMbPowerStatsHistInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistInputCurrent.setStatus("current")
_CfprApComputeMbPowerStatsHistInputCurrentAvg_Type = Integer32
_CfprApComputeMbPowerStatsHistInputCurrentAvg_Object = MibTableColumn
cfprApComputeMbPowerStatsHistInputCurrentAvg = _CfprApComputeMbPowerStatsHistInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 10),
    _CfprApComputeMbPowerStatsHistInputCurrentAvg_Type()
)
cfprApComputeMbPowerStatsHistInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistInputCurrentAvg.setStatus("current")
_CfprApComputeMbPowerStatsHistInputCurrentMax_Type = Integer32
_CfprApComputeMbPowerStatsHistInputCurrentMax_Object = MibTableColumn
cfprApComputeMbPowerStatsHistInputCurrentMax = _CfprApComputeMbPowerStatsHistInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 11),
    _CfprApComputeMbPowerStatsHistInputCurrentMax_Type()
)
cfprApComputeMbPowerStatsHistInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistInputCurrentMax.setStatus("current")
_CfprApComputeMbPowerStatsHistInputCurrentMin_Type = Integer32
_CfprApComputeMbPowerStatsHistInputCurrentMin_Object = MibTableColumn
cfprApComputeMbPowerStatsHistInputCurrentMin = _CfprApComputeMbPowerStatsHistInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 12),
    _CfprApComputeMbPowerStatsHistInputCurrentMin_Type()
)
cfprApComputeMbPowerStatsHistInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistInputCurrentMin.setStatus("current")
_CfprApComputeMbPowerStatsHistInputVoltage_Type = Integer32
_CfprApComputeMbPowerStatsHistInputVoltage_Object = MibTableColumn
cfprApComputeMbPowerStatsHistInputVoltage = _CfprApComputeMbPowerStatsHistInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 13),
    _CfprApComputeMbPowerStatsHistInputVoltage_Type()
)
cfprApComputeMbPowerStatsHistInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistInputVoltage.setStatus("current")
_CfprApComputeMbPowerStatsHistInputVoltageAvg_Type = Integer32
_CfprApComputeMbPowerStatsHistInputVoltageAvg_Object = MibTableColumn
cfprApComputeMbPowerStatsHistInputVoltageAvg = _CfprApComputeMbPowerStatsHistInputVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 14),
    _CfprApComputeMbPowerStatsHistInputVoltageAvg_Type()
)
cfprApComputeMbPowerStatsHistInputVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistInputVoltageAvg.setStatus("current")
_CfprApComputeMbPowerStatsHistInputVoltageMax_Type = Integer32
_CfprApComputeMbPowerStatsHistInputVoltageMax_Object = MibTableColumn
cfprApComputeMbPowerStatsHistInputVoltageMax = _CfprApComputeMbPowerStatsHistInputVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 15),
    _CfprApComputeMbPowerStatsHistInputVoltageMax_Type()
)
cfprApComputeMbPowerStatsHistInputVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistInputVoltageMax.setStatus("current")
_CfprApComputeMbPowerStatsHistInputVoltageMin_Type = Integer32
_CfprApComputeMbPowerStatsHistInputVoltageMin_Object = MibTableColumn
cfprApComputeMbPowerStatsHistInputVoltageMin = _CfprApComputeMbPowerStatsHistInputVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 16),
    _CfprApComputeMbPowerStatsHistInputVoltageMin_Type()
)
cfprApComputeMbPowerStatsHistInputVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistInputVoltageMin.setStatus("current")
_CfprApComputeMbPowerStatsHistMostRecent_Type = TruthValue
_CfprApComputeMbPowerStatsHistMostRecent_Object = MibTableColumn
cfprApComputeMbPowerStatsHistMostRecent = _CfprApComputeMbPowerStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 17),
    _CfprApComputeMbPowerStatsHistMostRecent_Type()
)
cfprApComputeMbPowerStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistMostRecent.setStatus("current")
_CfprApComputeMbPowerStatsHistSuspect_Type = TruthValue
_CfprApComputeMbPowerStatsHistSuspect_Object = MibTableColumn
cfprApComputeMbPowerStatsHistSuspect = _CfprApComputeMbPowerStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 18),
    _CfprApComputeMbPowerStatsHistSuspect_Type()
)
cfprApComputeMbPowerStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistSuspect.setStatus("current")
_CfprApComputeMbPowerStatsHistThresholded_Type = CfprApComputeMbPowerStatsHistThresholded
_CfprApComputeMbPowerStatsHistThresholded_Object = MibTableColumn
cfprApComputeMbPowerStatsHistThresholded = _CfprApComputeMbPowerStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 19),
    _CfprApComputeMbPowerStatsHistThresholded_Type()
)
cfprApComputeMbPowerStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistThresholded.setStatus("current")
_CfprApComputeMbPowerStatsHistTimeCollected_Type = DateAndTime
_CfprApComputeMbPowerStatsHistTimeCollected_Object = MibTableColumn
cfprApComputeMbPowerStatsHistTimeCollected = _CfprApComputeMbPowerStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 23, 1, 20),
    _CfprApComputeMbPowerStatsHistTimeCollected_Type()
)
cfprApComputeMbPowerStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbPowerStatsHistTimeCollected.setStatus("current")
_CfprApComputeMbTempStatsTable_Object = MibTable
cfprApComputeMbTempStatsTable = _CfprApComputeMbTempStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24)
)
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsTable.setStatus("current")
_CfprApComputeMbTempStatsEntry_Object = MibTableRow
cfprApComputeMbTempStatsEntry = _CfprApComputeMbTempStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1)
)
cfprApComputeMbTempStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeMbTempStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsEntry.setStatus("current")
_CfprApComputeMbTempStatsInstanceId_Type = CfprApManagedObjectId
_CfprApComputeMbTempStatsInstanceId_Object = MibTableColumn
cfprApComputeMbTempStatsInstanceId = _CfprApComputeMbTempStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 1),
    _CfprApComputeMbTempStatsInstanceId_Type()
)
cfprApComputeMbTempStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsInstanceId.setStatus("current")
_CfprApComputeMbTempStatsDn_Type = CfprApManagedObjectDn
_CfprApComputeMbTempStatsDn_Object = MibTableColumn
cfprApComputeMbTempStatsDn = _CfprApComputeMbTempStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 2),
    _CfprApComputeMbTempStatsDn_Type()
)
cfprApComputeMbTempStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsDn.setStatus("current")
_CfprApComputeMbTempStatsRn_Type = SnmpAdminString
_CfprApComputeMbTempStatsRn_Object = MibTableColumn
cfprApComputeMbTempStatsRn = _CfprApComputeMbTempStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 3),
    _CfprApComputeMbTempStatsRn_Type()
)
cfprApComputeMbTempStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsRn.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenIo_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenIo_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenIo = _CfprApComputeMbTempStatsFmTempSenIo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 4),
    _CfprApComputeMbTempStatsFmTempSenIo_Type()
)
cfprApComputeMbTempStatsFmTempSenIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenIo.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenIoAvg_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenIoAvg_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenIoAvg = _CfprApComputeMbTempStatsFmTempSenIoAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 5),
    _CfprApComputeMbTempStatsFmTempSenIoAvg_Type()
)
cfprApComputeMbTempStatsFmTempSenIoAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenIoAvg.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenIoMax_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenIoMax_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenIoMax = _CfprApComputeMbTempStatsFmTempSenIoMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 6),
    _CfprApComputeMbTempStatsFmTempSenIoMax_Type()
)
cfprApComputeMbTempStatsFmTempSenIoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenIoMax.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenIoMin_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenIoMin_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenIoMin = _CfprApComputeMbTempStatsFmTempSenIoMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 7),
    _CfprApComputeMbTempStatsFmTempSenIoMin_Type()
)
cfprApComputeMbTempStatsFmTempSenIoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenIoMin.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenRear_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenRear_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenRear = _CfprApComputeMbTempStatsFmTempSenRear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 8),
    _CfprApComputeMbTempStatsFmTempSenRear_Type()
)
cfprApComputeMbTempStatsFmTempSenRear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenRear.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenRearAvg_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenRearAvg_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenRearAvg = _CfprApComputeMbTempStatsFmTempSenRearAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 9),
    _CfprApComputeMbTempStatsFmTempSenRearAvg_Type()
)
cfprApComputeMbTempStatsFmTempSenRearAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenRearAvg.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenRearL_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenRearL_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenRearL = _CfprApComputeMbTempStatsFmTempSenRearL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 10),
    _CfprApComputeMbTempStatsFmTempSenRearL_Type()
)
cfprApComputeMbTempStatsFmTempSenRearL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenRearL.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenRearLAvg_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenRearLAvg_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenRearLAvg = _CfprApComputeMbTempStatsFmTempSenRearLAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 11),
    _CfprApComputeMbTempStatsFmTempSenRearLAvg_Type()
)
cfprApComputeMbTempStatsFmTempSenRearLAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenRearLAvg.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenRearLMax_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenRearLMax_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenRearLMax = _CfprApComputeMbTempStatsFmTempSenRearLMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 12),
    _CfprApComputeMbTempStatsFmTempSenRearLMax_Type()
)
cfprApComputeMbTempStatsFmTempSenRearLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenRearLMax.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenRearLMin_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenRearLMin_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenRearLMin = _CfprApComputeMbTempStatsFmTempSenRearLMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 13),
    _CfprApComputeMbTempStatsFmTempSenRearLMin_Type()
)
cfprApComputeMbTempStatsFmTempSenRearLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenRearLMin.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenRearMax_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenRearMax_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenRearMax = _CfprApComputeMbTempStatsFmTempSenRearMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 14),
    _CfprApComputeMbTempStatsFmTempSenRearMax_Type()
)
cfprApComputeMbTempStatsFmTempSenRearMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenRearMax.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenRearMin_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenRearMin_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenRearMin = _CfprApComputeMbTempStatsFmTempSenRearMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 15),
    _CfprApComputeMbTempStatsFmTempSenRearMin_Type()
)
cfprApComputeMbTempStatsFmTempSenRearMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenRearMin.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenRearR_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenRearR_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenRearR = _CfprApComputeMbTempStatsFmTempSenRearR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 16),
    _CfprApComputeMbTempStatsFmTempSenRearR_Type()
)
cfprApComputeMbTempStatsFmTempSenRearR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenRearR.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenRearRAvg_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenRearRAvg_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenRearRAvg = _CfprApComputeMbTempStatsFmTempSenRearRAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 17),
    _CfprApComputeMbTempStatsFmTempSenRearRAvg_Type()
)
cfprApComputeMbTempStatsFmTempSenRearRAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenRearRAvg.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenRearRMax_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenRearRMax_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenRearRMax = _CfprApComputeMbTempStatsFmTempSenRearRMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 18),
    _CfprApComputeMbTempStatsFmTempSenRearRMax_Type()
)
cfprApComputeMbTempStatsFmTempSenRearRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenRearRMax.setStatus("current")
_CfprApComputeMbTempStatsFmTempSenRearRMin_Type = Integer32
_CfprApComputeMbTempStatsFmTempSenRearRMin_Object = MibTableColumn
cfprApComputeMbTempStatsFmTempSenRearRMin = _CfprApComputeMbTempStatsFmTempSenRearRMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 19),
    _CfprApComputeMbTempStatsFmTempSenRearRMin_Type()
)
cfprApComputeMbTempStatsFmTempSenRearRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsFmTempSenRearRMin.setStatus("current")
_CfprApComputeMbTempStatsIntervals_Type = Gauge32
_CfprApComputeMbTempStatsIntervals_Object = MibTableColumn
cfprApComputeMbTempStatsIntervals = _CfprApComputeMbTempStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 20),
    _CfprApComputeMbTempStatsIntervals_Type()
)
cfprApComputeMbTempStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsIntervals.setStatus("current")
_CfprApComputeMbTempStatsSuspect_Type = TruthValue
_CfprApComputeMbTempStatsSuspect_Object = MibTableColumn
cfprApComputeMbTempStatsSuspect = _CfprApComputeMbTempStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 21),
    _CfprApComputeMbTempStatsSuspect_Type()
)
cfprApComputeMbTempStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsSuspect.setStatus("current")
_CfprApComputeMbTempStatsThresholded_Type = CfprApComputeMbTempStatsThresholded
_CfprApComputeMbTempStatsThresholded_Object = MibTableColumn
cfprApComputeMbTempStatsThresholded = _CfprApComputeMbTempStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 22),
    _CfprApComputeMbTempStatsThresholded_Type()
)
cfprApComputeMbTempStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsThresholded.setStatus("current")
_CfprApComputeMbTempStatsTimeCollected_Type = DateAndTime
_CfprApComputeMbTempStatsTimeCollected_Object = MibTableColumn
cfprApComputeMbTempStatsTimeCollected = _CfprApComputeMbTempStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 23),
    _CfprApComputeMbTempStatsTimeCollected_Type()
)
cfprApComputeMbTempStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsTimeCollected.setStatus("current")
_CfprApComputeMbTempStatsUpdate_Type = Gauge32
_CfprApComputeMbTempStatsUpdate_Object = MibTableColumn
cfprApComputeMbTempStatsUpdate = _CfprApComputeMbTempStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 24, 1, 24),
    _CfprApComputeMbTempStatsUpdate_Type()
)
cfprApComputeMbTempStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsUpdate.setStatus("current")
_CfprApComputeMbTempStatsHistTable_Object = MibTable
cfprApComputeMbTempStatsHistTable = _CfprApComputeMbTempStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25)
)
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistTable.setStatus("current")
_CfprApComputeMbTempStatsHistEntry_Object = MibTableRow
cfprApComputeMbTempStatsHistEntry = _CfprApComputeMbTempStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1)
)
cfprApComputeMbTempStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeMbTempStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistEntry.setStatus("current")
_CfprApComputeMbTempStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApComputeMbTempStatsHistInstanceId_Object = MibTableColumn
cfprApComputeMbTempStatsHistInstanceId = _CfprApComputeMbTempStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 1),
    _CfprApComputeMbTempStatsHistInstanceId_Type()
)
cfprApComputeMbTempStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistInstanceId.setStatus("current")
_CfprApComputeMbTempStatsHistDn_Type = CfprApManagedObjectDn
_CfprApComputeMbTempStatsHistDn_Object = MibTableColumn
cfprApComputeMbTempStatsHistDn = _CfprApComputeMbTempStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 2),
    _CfprApComputeMbTempStatsHistDn_Type()
)
cfprApComputeMbTempStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistDn.setStatus("current")
_CfprApComputeMbTempStatsHistRn_Type = SnmpAdminString
_CfprApComputeMbTempStatsHistRn_Object = MibTableColumn
cfprApComputeMbTempStatsHistRn = _CfprApComputeMbTempStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 3),
    _CfprApComputeMbTempStatsHistRn_Type()
)
cfprApComputeMbTempStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistRn.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenIo_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenIo_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenIo = _CfprApComputeMbTempStatsHistFmTempSenIo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 4),
    _CfprApComputeMbTempStatsHistFmTempSenIo_Type()
)
cfprApComputeMbTempStatsHistFmTempSenIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenIo.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenIoAvg_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenIoAvg_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenIoAvg = _CfprApComputeMbTempStatsHistFmTempSenIoAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 5),
    _CfprApComputeMbTempStatsHistFmTempSenIoAvg_Type()
)
cfprApComputeMbTempStatsHistFmTempSenIoAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenIoAvg.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenIoMax_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenIoMax_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenIoMax = _CfprApComputeMbTempStatsHistFmTempSenIoMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 6),
    _CfprApComputeMbTempStatsHistFmTempSenIoMax_Type()
)
cfprApComputeMbTempStatsHistFmTempSenIoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenIoMax.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenIoMin_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenIoMin_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenIoMin = _CfprApComputeMbTempStatsHistFmTempSenIoMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 7),
    _CfprApComputeMbTempStatsHistFmTempSenIoMin_Type()
)
cfprApComputeMbTempStatsHistFmTempSenIoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenIoMin.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenRear_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenRear_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenRear = _CfprApComputeMbTempStatsHistFmTempSenRear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 8),
    _CfprApComputeMbTempStatsHistFmTempSenRear_Type()
)
cfprApComputeMbTempStatsHistFmTempSenRear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenRear.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenRearAvg_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenRearAvg_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenRearAvg = _CfprApComputeMbTempStatsHistFmTempSenRearAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 9),
    _CfprApComputeMbTempStatsHistFmTempSenRearAvg_Type()
)
cfprApComputeMbTempStatsHistFmTempSenRearAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenRearAvg.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenRearL_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenRearL_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenRearL = _CfprApComputeMbTempStatsHistFmTempSenRearL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 10),
    _CfprApComputeMbTempStatsHistFmTempSenRearL_Type()
)
cfprApComputeMbTempStatsHistFmTempSenRearL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenRearL.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenRearLAvg_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenRearLAvg_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenRearLAvg = _CfprApComputeMbTempStatsHistFmTempSenRearLAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 11),
    _CfprApComputeMbTempStatsHistFmTempSenRearLAvg_Type()
)
cfprApComputeMbTempStatsHistFmTempSenRearLAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenRearLAvg.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenRearLMax_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenRearLMax_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenRearLMax = _CfprApComputeMbTempStatsHistFmTempSenRearLMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 12),
    _CfprApComputeMbTempStatsHistFmTempSenRearLMax_Type()
)
cfprApComputeMbTempStatsHistFmTempSenRearLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenRearLMax.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenRearLMin_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenRearLMin_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenRearLMin = _CfprApComputeMbTempStatsHistFmTempSenRearLMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 13),
    _CfprApComputeMbTempStatsHistFmTempSenRearLMin_Type()
)
cfprApComputeMbTempStatsHistFmTempSenRearLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenRearLMin.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenRearMax_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenRearMax_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenRearMax = _CfprApComputeMbTempStatsHistFmTempSenRearMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 14),
    _CfprApComputeMbTempStatsHistFmTempSenRearMax_Type()
)
cfprApComputeMbTempStatsHistFmTempSenRearMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenRearMax.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenRearMin_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenRearMin_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenRearMin = _CfprApComputeMbTempStatsHistFmTempSenRearMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 15),
    _CfprApComputeMbTempStatsHistFmTempSenRearMin_Type()
)
cfprApComputeMbTempStatsHistFmTempSenRearMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenRearMin.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenRearR_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenRearR_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenRearR = _CfprApComputeMbTempStatsHistFmTempSenRearR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 16),
    _CfprApComputeMbTempStatsHistFmTempSenRearR_Type()
)
cfprApComputeMbTempStatsHistFmTempSenRearR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenRearR.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenRearRAvg_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenRearRAvg_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenRearRAvg = _CfprApComputeMbTempStatsHistFmTempSenRearRAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 17),
    _CfprApComputeMbTempStatsHistFmTempSenRearRAvg_Type()
)
cfprApComputeMbTempStatsHistFmTempSenRearRAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenRearRAvg.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenRearRMax_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenRearRMax_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenRearRMax = _CfprApComputeMbTempStatsHistFmTempSenRearRMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 18),
    _CfprApComputeMbTempStatsHistFmTempSenRearRMax_Type()
)
cfprApComputeMbTempStatsHistFmTempSenRearRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenRearRMax.setStatus("current")
_CfprApComputeMbTempStatsHistFmTempSenRearRMin_Type = Integer32
_CfprApComputeMbTempStatsHistFmTempSenRearRMin_Object = MibTableColumn
cfprApComputeMbTempStatsHistFmTempSenRearRMin = _CfprApComputeMbTempStatsHistFmTempSenRearRMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 19),
    _CfprApComputeMbTempStatsHistFmTempSenRearRMin_Type()
)
cfprApComputeMbTempStatsHistFmTempSenRearRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistFmTempSenRearRMin.setStatus("current")
_CfprApComputeMbTempStatsHistId_Type = Unsigned64
_CfprApComputeMbTempStatsHistId_Object = MibTableColumn
cfprApComputeMbTempStatsHistId = _CfprApComputeMbTempStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 20),
    _CfprApComputeMbTempStatsHistId_Type()
)
cfprApComputeMbTempStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistId.setStatus("current")
_CfprApComputeMbTempStatsHistMostRecent_Type = TruthValue
_CfprApComputeMbTempStatsHistMostRecent_Object = MibTableColumn
cfprApComputeMbTempStatsHistMostRecent = _CfprApComputeMbTempStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 21),
    _CfprApComputeMbTempStatsHistMostRecent_Type()
)
cfprApComputeMbTempStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistMostRecent.setStatus("current")
_CfprApComputeMbTempStatsHistSuspect_Type = TruthValue
_CfprApComputeMbTempStatsHistSuspect_Object = MibTableColumn
cfprApComputeMbTempStatsHistSuspect = _CfprApComputeMbTempStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 22),
    _CfprApComputeMbTempStatsHistSuspect_Type()
)
cfprApComputeMbTempStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistSuspect.setStatus("current")
_CfprApComputeMbTempStatsHistThresholded_Type = CfprApComputeMbTempStatsHistThresholded
_CfprApComputeMbTempStatsHistThresholded_Object = MibTableColumn
cfprApComputeMbTempStatsHistThresholded = _CfprApComputeMbTempStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 23),
    _CfprApComputeMbTempStatsHistThresholded_Type()
)
cfprApComputeMbTempStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistThresholded.setStatus("current")
_CfprApComputeMbTempStatsHistTimeCollected_Type = DateAndTime
_CfprApComputeMbTempStatsHistTimeCollected_Object = MibTableColumn
cfprApComputeMbTempStatsHistTimeCollected = _CfprApComputeMbTempStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 25, 1, 24),
    _CfprApComputeMbTempStatsHistTimeCollected_Type()
)
cfprApComputeMbTempStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMbTempStatsHistTimeCollected.setStatus("current")
_CfprApComputeMemoryConfigPolicyTable_Object = MibTable
cfprApComputeMemoryConfigPolicyTable = _CfprApComputeMemoryConfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 26)
)
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigPolicyTable.setStatus("current")
_CfprApComputeMemoryConfigPolicyEntry_Object = MibTableRow
cfprApComputeMemoryConfigPolicyEntry = _CfprApComputeMemoryConfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 26, 1)
)
cfprApComputeMemoryConfigPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeMemoryConfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigPolicyEntry.setStatus("current")
_CfprApComputeMemoryConfigPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApComputeMemoryConfigPolicyInstanceId_Object = MibTableColumn
cfprApComputeMemoryConfigPolicyInstanceId = _CfprApComputeMemoryConfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 26, 1, 1),
    _CfprApComputeMemoryConfigPolicyInstanceId_Type()
)
cfprApComputeMemoryConfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigPolicyInstanceId.setStatus("current")
_CfprApComputeMemoryConfigPolicyDn_Type = CfprApManagedObjectDn
_CfprApComputeMemoryConfigPolicyDn_Object = MibTableColumn
cfprApComputeMemoryConfigPolicyDn = _CfprApComputeMemoryConfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 26, 1, 2),
    _CfprApComputeMemoryConfigPolicyDn_Type()
)
cfprApComputeMemoryConfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigPolicyDn.setStatus("current")
_CfprApComputeMemoryConfigPolicyRn_Type = SnmpAdminString
_CfprApComputeMemoryConfigPolicyRn_Object = MibTableColumn
cfprApComputeMemoryConfigPolicyRn = _CfprApComputeMemoryConfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 26, 1, 3),
    _CfprApComputeMemoryConfigPolicyRn_Type()
)
cfprApComputeMemoryConfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigPolicyRn.setStatus("current")
_CfprApComputeMemoryConfigPolicyBlackListing_Type = CfprApComputeBlackListing
_CfprApComputeMemoryConfigPolicyBlackListing_Object = MibTableColumn
cfprApComputeMemoryConfigPolicyBlackListing = _CfprApComputeMemoryConfigPolicyBlackListing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 26, 1, 4),
    _CfprApComputeMemoryConfigPolicyBlackListing_Type()
)
cfprApComputeMemoryConfigPolicyBlackListing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigPolicyBlackListing.setStatus("current")
_CfprApComputeMemoryConfigPolicyDescr_Type = SnmpAdminString
_CfprApComputeMemoryConfigPolicyDescr_Object = MibTableColumn
cfprApComputeMemoryConfigPolicyDescr = _CfprApComputeMemoryConfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 26, 1, 5),
    _CfprApComputeMemoryConfigPolicyDescr_Type()
)
cfprApComputeMemoryConfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigPolicyDescr.setStatus("current")
_CfprApComputeMemoryConfigPolicyIntId_Type = SnmpAdminString
_CfprApComputeMemoryConfigPolicyIntId_Object = MibTableColumn
cfprApComputeMemoryConfigPolicyIntId = _CfprApComputeMemoryConfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 26, 1, 6),
    _CfprApComputeMemoryConfigPolicyIntId_Type()
)
cfprApComputeMemoryConfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigPolicyIntId.setStatus("current")
_CfprApComputeMemoryConfigPolicyName_Type = SnmpAdminString
_CfprApComputeMemoryConfigPolicyName_Object = MibTableColumn
cfprApComputeMemoryConfigPolicyName = _CfprApComputeMemoryConfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 26, 1, 7),
    _CfprApComputeMemoryConfigPolicyName_Type()
)
cfprApComputeMemoryConfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigPolicyName.setStatus("current")
_CfprApComputeMemoryConfigPolicyPolicyLevel_Type = Gauge32
_CfprApComputeMemoryConfigPolicyPolicyLevel_Object = MibTableColumn
cfprApComputeMemoryConfigPolicyPolicyLevel = _CfprApComputeMemoryConfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 26, 1, 8),
    _CfprApComputeMemoryConfigPolicyPolicyLevel_Type()
)
cfprApComputeMemoryConfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigPolicyPolicyLevel.setStatus("current")
_CfprApComputeMemoryConfigPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeMemoryConfigPolicyPolicyOwner_Object = MibTableColumn
cfprApComputeMemoryConfigPolicyPolicyOwner = _CfprApComputeMemoryConfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 26, 1, 9),
    _CfprApComputeMemoryConfigPolicyPolicyOwner_Type()
)
cfprApComputeMemoryConfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigPolicyPolicyOwner.setStatus("current")
_CfprApComputeMemoryConfigurationTable_Object = MibTable
cfprApComputeMemoryConfigurationTable = _CfprApComputeMemoryConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 27)
)
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigurationTable.setStatus("current")
_CfprApComputeMemoryConfigurationEntry_Object = MibTableRow
cfprApComputeMemoryConfigurationEntry = _CfprApComputeMemoryConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 27, 1)
)
cfprApComputeMemoryConfigurationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeMemoryConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigurationEntry.setStatus("current")
_CfprApComputeMemoryConfigurationInstanceId_Type = CfprApManagedObjectId
_CfprApComputeMemoryConfigurationInstanceId_Object = MibTableColumn
cfprApComputeMemoryConfigurationInstanceId = _CfprApComputeMemoryConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 27, 1, 1),
    _CfprApComputeMemoryConfigurationInstanceId_Type()
)
cfprApComputeMemoryConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigurationInstanceId.setStatus("current")
_CfprApComputeMemoryConfigurationDn_Type = CfprApManagedObjectDn
_CfprApComputeMemoryConfigurationDn_Object = MibTableColumn
cfprApComputeMemoryConfigurationDn = _CfprApComputeMemoryConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 27, 1, 2),
    _CfprApComputeMemoryConfigurationDn_Type()
)
cfprApComputeMemoryConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigurationDn.setStatus("current")
_CfprApComputeMemoryConfigurationRn_Type = SnmpAdminString
_CfprApComputeMemoryConfigurationRn_Object = MibTableColumn
cfprApComputeMemoryConfigurationRn = _CfprApComputeMemoryConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 27, 1, 3),
    _CfprApComputeMemoryConfigurationRn_Type()
)
cfprApComputeMemoryConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigurationRn.setStatus("current")
_CfprApComputeMemoryConfigurationAdminMemoryState_Type = CfprApComputeAdminMemoryState
_CfprApComputeMemoryConfigurationAdminMemoryState_Object = MibTableColumn
cfprApComputeMemoryConfigurationAdminMemoryState = _CfprApComputeMemoryConfigurationAdminMemoryState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 27, 1, 4),
    _CfprApComputeMemoryConfigurationAdminMemoryState_Type()
)
cfprApComputeMemoryConfigurationAdminMemoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigurationAdminMemoryState.setStatus("current")
_CfprApComputeMemoryConfigurationBlackListing_Type = CfprApComputeBlackListing
_CfprApComputeMemoryConfigurationBlackListing_Object = MibTableColumn
cfprApComputeMemoryConfigurationBlackListing = _CfprApComputeMemoryConfigurationBlackListing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 27, 1, 5),
    _CfprApComputeMemoryConfigurationBlackListing_Type()
)
cfprApComputeMemoryConfigurationBlackListing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryConfigurationBlackListing.setStatus("current")
_CfprApComputeMemoryUnitConstraintDefTable_Object = MibTable
cfprApComputeMemoryUnitConstraintDefTable = _CfprApComputeMemoryUnitConstraintDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 28)
)
if mibBuilder.loadTexts:
    cfprApComputeMemoryUnitConstraintDefTable.setStatus("current")
_CfprApComputeMemoryUnitConstraintDefEntry_Object = MibTableRow
cfprApComputeMemoryUnitConstraintDefEntry = _CfprApComputeMemoryUnitConstraintDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 28, 1)
)
cfprApComputeMemoryUnitConstraintDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeMemoryUnitConstraintDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeMemoryUnitConstraintDefEntry.setStatus("current")
_CfprApComputeMemoryUnitConstraintDefInstanceId_Type = CfprApManagedObjectId
_CfprApComputeMemoryUnitConstraintDefInstanceId_Object = MibTableColumn
cfprApComputeMemoryUnitConstraintDefInstanceId = _CfprApComputeMemoryUnitConstraintDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 28, 1, 1),
    _CfprApComputeMemoryUnitConstraintDefInstanceId_Type()
)
cfprApComputeMemoryUnitConstraintDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeMemoryUnitConstraintDefInstanceId.setStatus("current")
_CfprApComputeMemoryUnitConstraintDefDn_Type = CfprApManagedObjectDn
_CfprApComputeMemoryUnitConstraintDefDn_Object = MibTableColumn
cfprApComputeMemoryUnitConstraintDefDn = _CfprApComputeMemoryUnitConstraintDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 28, 1, 2),
    _CfprApComputeMemoryUnitConstraintDefDn_Type()
)
cfprApComputeMemoryUnitConstraintDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryUnitConstraintDefDn.setStatus("current")
_CfprApComputeMemoryUnitConstraintDefRn_Type = SnmpAdminString
_CfprApComputeMemoryUnitConstraintDefRn_Object = MibTableColumn
cfprApComputeMemoryUnitConstraintDefRn = _CfprApComputeMemoryUnitConstraintDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 28, 1, 3),
    _CfprApComputeMemoryUnitConstraintDefRn_Type()
)
cfprApComputeMemoryUnitConstraintDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryUnitConstraintDefRn.setStatus("current")
_CfprApComputeMemoryUnitConstraintDefDescr_Type = SnmpAdminString
_CfprApComputeMemoryUnitConstraintDefDescr_Object = MibTableColumn
cfprApComputeMemoryUnitConstraintDefDescr = _CfprApComputeMemoryUnitConstraintDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 28, 1, 4),
    _CfprApComputeMemoryUnitConstraintDefDescr_Type()
)
cfprApComputeMemoryUnitConstraintDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryUnitConstraintDefDescr.setStatus("current")
_CfprApComputeMemoryUnitConstraintDefIntId_Type = SnmpAdminString
_CfprApComputeMemoryUnitConstraintDefIntId_Object = MibTableColumn
cfprApComputeMemoryUnitConstraintDefIntId = _CfprApComputeMemoryUnitConstraintDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 28, 1, 5),
    _CfprApComputeMemoryUnitConstraintDefIntId_Type()
)
cfprApComputeMemoryUnitConstraintDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryUnitConstraintDefIntId.setStatus("current")
_CfprApComputeMemoryUnitConstraintDefName_Type = SnmpAdminString
_CfprApComputeMemoryUnitConstraintDefName_Object = MibTableColumn
cfprApComputeMemoryUnitConstraintDefName = _CfprApComputeMemoryUnitConstraintDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 28, 1, 6),
    _CfprApComputeMemoryUnitConstraintDefName_Type()
)
cfprApComputeMemoryUnitConstraintDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryUnitConstraintDefName.setStatus("current")
_CfprApComputeMemoryUnitConstraintDefPolicyLevel_Type = Gauge32
_CfprApComputeMemoryUnitConstraintDefPolicyLevel_Object = MibTableColumn
cfprApComputeMemoryUnitConstraintDefPolicyLevel = _CfprApComputeMemoryUnitConstraintDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 28, 1, 7),
    _CfprApComputeMemoryUnitConstraintDefPolicyLevel_Type()
)
cfprApComputeMemoryUnitConstraintDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryUnitConstraintDefPolicyLevel.setStatus("current")
_CfprApComputeMemoryUnitConstraintDefPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeMemoryUnitConstraintDefPolicyOwner_Object = MibTableColumn
cfprApComputeMemoryUnitConstraintDefPolicyOwner = _CfprApComputeMemoryUnitConstraintDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 28, 1, 8),
    _CfprApComputeMemoryUnitConstraintDefPolicyOwner_Type()
)
cfprApComputeMemoryUnitConstraintDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryUnitConstraintDefPolicyOwner.setStatus("current")
_CfprApComputeMemoryUnitConstraintDefRevisionModifier_Type = SnmpAdminString
_CfprApComputeMemoryUnitConstraintDefRevisionModifier_Object = MibTableColumn
cfprApComputeMemoryUnitConstraintDefRevisionModifier = _CfprApComputeMemoryUnitConstraintDefRevisionModifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 28, 1, 9),
    _CfprApComputeMemoryUnitConstraintDefRevisionModifier_Type()
)
cfprApComputeMemoryUnitConstraintDefRevisionModifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryUnitConstraintDefRevisionModifier.setStatus("current")
_CfprApComputeMemoryUnitConstraintDefType_Type = CfprApComputeMemoryUnitConstraintType
_CfprApComputeMemoryUnitConstraintDefType_Object = MibTableColumn
cfprApComputeMemoryUnitConstraintDefType = _CfprApComputeMemoryUnitConstraintDefType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 28, 1, 10),
    _CfprApComputeMemoryUnitConstraintDefType_Type()
)
cfprApComputeMemoryUnitConstraintDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeMemoryUnitConstraintDefType.setStatus("current")
_CfprApComputeNpuTable_Object = MibTable
cfprApComputeNpuTable = _CfprApComputeNpuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29)
)
if mibBuilder.loadTexts:
    cfprApComputeNpuTable.setStatus("current")
_CfprApComputeNpuEntry_Object = MibTableRow
cfprApComputeNpuEntry = _CfprApComputeNpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1)
)
cfprApComputeNpuEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeNpuInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeNpuEntry.setStatus("current")
_CfprApComputeNpuInstanceId_Type = CfprApManagedObjectId
_CfprApComputeNpuInstanceId_Object = MibTableColumn
cfprApComputeNpuInstanceId = _CfprApComputeNpuInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 1),
    _CfprApComputeNpuInstanceId_Type()
)
cfprApComputeNpuInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeNpuInstanceId.setStatus("current")
_CfprApComputeNpuDn_Type = CfprApManagedObjectDn
_CfprApComputeNpuDn_Object = MibTableColumn
cfprApComputeNpuDn = _CfprApComputeNpuDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 2),
    _CfprApComputeNpuDn_Type()
)
cfprApComputeNpuDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuDn.setStatus("current")
_CfprApComputeNpuRn_Type = SnmpAdminString
_CfprApComputeNpuRn_Object = MibTableColumn
cfprApComputeNpuRn = _CfprApComputeNpuRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 3),
    _CfprApComputeNpuRn_Type()
)
cfprApComputeNpuRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuRn.setStatus("current")
_CfprApComputeNpuId_Type = Gauge32
_CfprApComputeNpuId_Object = MibTableColumn
cfprApComputeNpuId = _CfprApComputeNpuId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 4),
    _CfprApComputeNpuId_Type()
)
cfprApComputeNpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuId.setStatus("current")
_CfprApComputeNpuLocationDn_Type = SnmpAdminString
_CfprApComputeNpuLocationDn_Object = MibTableColumn
cfprApComputeNpuLocationDn = _CfprApComputeNpuLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 5),
    _CfprApComputeNpuLocationDn_Type()
)
cfprApComputeNpuLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuLocationDn.setStatus("current")
_CfprApComputeNpuModel_Type = SnmpAdminString
_CfprApComputeNpuModel_Object = MibTableColumn
cfprApComputeNpuModel = _CfprApComputeNpuModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 6),
    _CfprApComputeNpuModel_Type()
)
cfprApComputeNpuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuModel.setStatus("current")
_CfprApComputeNpuOperQualifierReason_Type = SnmpAdminString
_CfprApComputeNpuOperQualifierReason_Object = MibTableColumn
cfprApComputeNpuOperQualifierReason = _CfprApComputeNpuOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 7),
    _CfprApComputeNpuOperQualifierReason_Type()
)
cfprApComputeNpuOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuOperQualifierReason.setStatus("current")
_CfprApComputeNpuOperState_Type = CfprApEquipmentOperability
_CfprApComputeNpuOperState_Object = MibTableColumn
cfprApComputeNpuOperState = _CfprApComputeNpuOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 8),
    _CfprApComputeNpuOperState_Type()
)
cfprApComputeNpuOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuOperState.setStatus("current")
_CfprApComputeNpuOperability_Type = CfprApEquipmentOperability
_CfprApComputeNpuOperability_Object = MibTableColumn
cfprApComputeNpuOperability = _CfprApComputeNpuOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 9),
    _CfprApComputeNpuOperability_Type()
)
cfprApComputeNpuOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuOperability.setStatus("current")
_CfprApComputeNpuPerf_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeNpuPerf_Object = MibTableColumn
cfprApComputeNpuPerf = _CfprApComputeNpuPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 10),
    _CfprApComputeNpuPerf_Type()
)
cfprApComputeNpuPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuPerf.setStatus("current")
_CfprApComputeNpuPower_Type = CfprApEquipmentPowerState
_CfprApComputeNpuPower_Object = MibTableColumn
cfprApComputeNpuPower = _CfprApComputeNpuPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 11),
    _CfprApComputeNpuPower_Type()
)
cfprApComputeNpuPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuPower.setStatus("current")
_CfprApComputeNpuPresence_Type = CfprApEquipmentPresence
_CfprApComputeNpuPresence_Object = MibTableColumn
cfprApComputeNpuPresence = _CfprApComputeNpuPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 12),
    _CfprApComputeNpuPresence_Type()
)
cfprApComputeNpuPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuPresence.setStatus("current")
_CfprApComputeNpuRevision_Type = SnmpAdminString
_CfprApComputeNpuRevision_Object = MibTableColumn
cfprApComputeNpuRevision = _CfprApComputeNpuRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 13),
    _CfprApComputeNpuRevision_Type()
)
cfprApComputeNpuRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuRevision.setStatus("current")
_CfprApComputeNpuSerial_Type = SnmpAdminString
_CfprApComputeNpuSerial_Object = MibTableColumn
cfprApComputeNpuSerial = _CfprApComputeNpuSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 14),
    _CfprApComputeNpuSerial_Type()
)
cfprApComputeNpuSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuSerial.setStatus("current")
_CfprApComputeNpuThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeNpuThermal_Object = MibTableColumn
cfprApComputeNpuThermal = _CfprApComputeNpuThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 15),
    _CfprApComputeNpuThermal_Type()
)
cfprApComputeNpuThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuThermal.setStatus("current")
_CfprApComputeNpuVendor_Type = SnmpAdminString
_CfprApComputeNpuVendor_Object = MibTableColumn
cfprApComputeNpuVendor = _CfprApComputeNpuVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 16),
    _CfprApComputeNpuVendor_Type()
)
cfprApComputeNpuVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuVendor.setStatus("current")
_CfprApComputeNpuVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeNpuVoltage_Object = MibTableColumn
cfprApComputeNpuVoltage = _CfprApComputeNpuVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 29, 1, 17),
    _CfprApComputeNpuVoltage_Type()
)
cfprApComputeNpuVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeNpuVoltage.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTable_Object = MibTable
cfprApComputePCIeFatalCompletionStatsTable = _CfprApComputePCIeFatalCompletionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30)
)
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTable.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsEntry_Object = MibTableRow
cfprApComputePCIeFatalCompletionStatsEntry = _CfprApComputePCIeFatalCompletionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1)
)
cfprApComputePCIeFatalCompletionStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePCIeFatalCompletionStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsEntry.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsInstanceId_Type = CfprApManagedObjectId
_CfprApComputePCIeFatalCompletionStatsInstanceId_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsInstanceId = _CfprApComputePCIeFatalCompletionStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 1),
    _CfprApComputePCIeFatalCompletionStatsInstanceId_Type()
)
cfprApComputePCIeFatalCompletionStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsInstanceId.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsDn_Type = CfprApManagedObjectDn
_CfprApComputePCIeFatalCompletionStatsDn_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsDn = _CfprApComputePCIeFatalCompletionStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 2),
    _CfprApComputePCIeFatalCompletionStatsDn_Type()
)
cfprApComputePCIeFatalCompletionStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsDn.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsRn_Type = SnmpAdminString
_CfprApComputePCIeFatalCompletionStatsRn_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsRn = _CfprApComputePCIeFatalCompletionStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 3),
    _CfprApComputePCIeFatalCompletionStatsRn_Type()
)
cfprApComputePCIeFatalCompletionStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsRn.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsAbortErrors_Type = Counter32
_CfprApComputePCIeFatalCompletionStatsAbortErrors_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsAbortErrors = _CfprApComputePCIeFatalCompletionStatsAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 4),
    _CfprApComputePCIeFatalCompletionStatsAbortErrors_Type()
)
cfprApComputePCIeFatalCompletionStatsAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsAbortErrors.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsAbortErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsAbortErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsAbortErrors15Min = _CfprApComputePCIeFatalCompletionStatsAbortErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 5),
    _CfprApComputePCIeFatalCompletionStatsAbortErrors15Min_Type()
)
cfprApComputePCIeFatalCompletionStatsAbortErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsAbortErrors15Min.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsAbortErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsAbortErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsAbortErrors15MinH = _CfprApComputePCIeFatalCompletionStatsAbortErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 6),
    _CfprApComputePCIeFatalCompletionStatsAbortErrors15MinH_Type()
)
cfprApComputePCIeFatalCompletionStatsAbortErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsAbortErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsAbortErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsAbortErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsAbortErrors1Day = _CfprApComputePCIeFatalCompletionStatsAbortErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 7),
    _CfprApComputePCIeFatalCompletionStatsAbortErrors1Day_Type()
)
cfprApComputePCIeFatalCompletionStatsAbortErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsAbortErrors1Day.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsAbortErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsAbortErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsAbortErrors1DayH = _CfprApComputePCIeFatalCompletionStatsAbortErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 8),
    _CfprApComputePCIeFatalCompletionStatsAbortErrors1DayH_Type()
)
cfprApComputePCIeFatalCompletionStatsAbortErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsAbortErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsAbortErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsAbortErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsAbortErrors1Hour = _CfprApComputePCIeFatalCompletionStatsAbortErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 9),
    _CfprApComputePCIeFatalCompletionStatsAbortErrors1Hour_Type()
)
cfprApComputePCIeFatalCompletionStatsAbortErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsAbortErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsAbortErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsAbortErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsAbortErrors1HourH = _CfprApComputePCIeFatalCompletionStatsAbortErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 10),
    _CfprApComputePCIeFatalCompletionStatsAbortErrors1HourH_Type()
)
cfprApComputePCIeFatalCompletionStatsAbortErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsAbortErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsAbortErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsAbortErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsAbortErrors1Week = _CfprApComputePCIeFatalCompletionStatsAbortErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 11),
    _CfprApComputePCIeFatalCompletionStatsAbortErrors1Week_Type()
)
cfprApComputePCIeFatalCompletionStatsAbortErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsAbortErrors1Week.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsAbortErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsAbortErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsAbortErrors1WeekH = _CfprApComputePCIeFatalCompletionStatsAbortErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 12),
    _CfprApComputePCIeFatalCompletionStatsAbortErrors1WeekH_Type()
)
cfprApComputePCIeFatalCompletionStatsAbortErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsAbortErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsAbortErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsAbortErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsAbortErrors2Weeks = _CfprApComputePCIeFatalCompletionStatsAbortErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 13),
    _CfprApComputePCIeFatalCompletionStatsAbortErrors2Weeks_Type()
)
cfprApComputePCIeFatalCompletionStatsAbortErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsAbortErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsAbortErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsAbortErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsAbortErrors2WeeksH = _CfprApComputePCIeFatalCompletionStatsAbortErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 14),
    _CfprApComputePCIeFatalCompletionStatsAbortErrors2WeeksH_Type()
)
cfprApComputePCIeFatalCompletionStatsAbortErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsAbortErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors_Type = Counter32
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsTimeoutErrors = _CfprApComputePCIeFatalCompletionStatsTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 15),
    _CfprApComputePCIeFatalCompletionStatsTimeoutErrors_Type()
)
cfprApComputePCIeFatalCompletionStatsTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTimeoutErrors.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsTimeoutErrors15Min = _CfprApComputePCIeFatalCompletionStatsTimeoutErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 16),
    _CfprApComputePCIeFatalCompletionStatsTimeoutErrors15Min_Type()
)
cfprApComputePCIeFatalCompletionStatsTimeoutErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTimeoutErrors15Min.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsTimeoutErrors15MinH = _CfprApComputePCIeFatalCompletionStatsTimeoutErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 17),
    _CfprApComputePCIeFatalCompletionStatsTimeoutErrors15MinH_Type()
)
cfprApComputePCIeFatalCompletionStatsTimeoutErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTimeoutErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Day = _CfprApComputePCIeFatalCompletionStatsTimeoutErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 18),
    _CfprApComputePCIeFatalCompletionStatsTimeoutErrors1Day_Type()
)
cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Day.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsTimeoutErrors1DayH = _CfprApComputePCIeFatalCompletionStatsTimeoutErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 19),
    _CfprApComputePCIeFatalCompletionStatsTimeoutErrors1DayH_Type()
)
cfprApComputePCIeFatalCompletionStatsTimeoutErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTimeoutErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Hour = _CfprApComputePCIeFatalCompletionStatsTimeoutErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 20),
    _CfprApComputePCIeFatalCompletionStatsTimeoutErrors1Hour_Type()
)
cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsTimeoutErrors1HourH = _CfprApComputePCIeFatalCompletionStatsTimeoutErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 21),
    _CfprApComputePCIeFatalCompletionStatsTimeoutErrors1HourH_Type()
)
cfprApComputePCIeFatalCompletionStatsTimeoutErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTimeoutErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Week = _CfprApComputePCIeFatalCompletionStatsTimeoutErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 22),
    _CfprApComputePCIeFatalCompletionStatsTimeoutErrors1Week_Type()
)
cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Week.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsTimeoutErrors1WeekH = _CfprApComputePCIeFatalCompletionStatsTimeoutErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 23),
    _CfprApComputePCIeFatalCompletionStatsTimeoutErrors1WeekH_Type()
)
cfprApComputePCIeFatalCompletionStatsTimeoutErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTimeoutErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsTimeoutErrors2Weeks = _CfprApComputePCIeFatalCompletionStatsTimeoutErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 24),
    _CfprApComputePCIeFatalCompletionStatsTimeoutErrors2Weeks_Type()
)
cfprApComputePCIeFatalCompletionStatsTimeoutErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTimeoutErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH = _CfprApComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 25),
    _CfprApComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH_Type()
)
cfprApComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsIntervals_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsIntervals_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsIntervals = _CfprApComputePCIeFatalCompletionStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 26),
    _CfprApComputePCIeFatalCompletionStatsIntervals_Type()
)
cfprApComputePCIeFatalCompletionStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsIntervals.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsSuspect_Type = TruthValue
_CfprApComputePCIeFatalCompletionStatsSuspect_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsSuspect = _CfprApComputePCIeFatalCompletionStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 27),
    _CfprApComputePCIeFatalCompletionStatsSuspect_Type()
)
cfprApComputePCIeFatalCompletionStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsSuspect.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsThresholded_Type = CfprApComputePCIeFatalCompletionStatsThresholded
_CfprApComputePCIeFatalCompletionStatsThresholded_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsThresholded = _CfprApComputePCIeFatalCompletionStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 28),
    _CfprApComputePCIeFatalCompletionStatsThresholded_Type()
)
cfprApComputePCIeFatalCompletionStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsThresholded.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsTimeCollected_Type = DateAndTime
_CfprApComputePCIeFatalCompletionStatsTimeCollected_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsTimeCollected = _CfprApComputePCIeFatalCompletionStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 29),
    _CfprApComputePCIeFatalCompletionStatsTimeCollected_Type()
)
cfprApComputePCIeFatalCompletionStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsTimeCollected.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors_Type = Counter32
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors = _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 30),
    _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors_Type()
)
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsUnexpectedErrors.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors15Min = _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 31),
    _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors15Min_Type()
)
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsUnexpectedErrors15Min.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors15MinH = _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 32),
    _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors15MinH_Type()
)
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsUnexpectedErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Day = _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 33),
    _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Day_Type()
)
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Day.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1DayH = _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 34),
    _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1DayH_Type()
)
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Hour = _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 35),
    _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Hour_Type()
)
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1HourH = _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 36),
    _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1HourH_Type()
)
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Week = _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 37),
    _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Week_Type()
)
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Week.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH = _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 38),
    _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH_Type()
)
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks = _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 39),
    _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks_Type()
)
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH = _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 40),
    _CfprApComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH_Type()
)
cfprApComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalCompletionStatsUpdate_Type = Gauge32
_CfprApComputePCIeFatalCompletionStatsUpdate_Object = MibTableColumn
cfprApComputePCIeFatalCompletionStatsUpdate = _CfprApComputePCIeFatalCompletionStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 30, 1, 41),
    _CfprApComputePCIeFatalCompletionStatsUpdate_Type()
)
cfprApComputePCIeFatalCompletionStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalCompletionStatsUpdate.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsTable_Object = MibTable
cfprApComputePCIeFatalProtocolStatsTable = _CfprApComputePCIeFatalProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31)
)
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsTable.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsEntry_Object = MibTableRow
cfprApComputePCIeFatalProtocolStatsEntry = _CfprApComputePCIeFatalProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1)
)
cfprApComputePCIeFatalProtocolStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePCIeFatalProtocolStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsEntry.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsInstanceId_Type = CfprApManagedObjectId
_CfprApComputePCIeFatalProtocolStatsInstanceId_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsInstanceId = _CfprApComputePCIeFatalProtocolStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 1),
    _CfprApComputePCIeFatalProtocolStatsInstanceId_Type()
)
cfprApComputePCIeFatalProtocolStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsInstanceId.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsDn_Type = CfprApManagedObjectDn
_CfprApComputePCIeFatalProtocolStatsDn_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsDn = _CfprApComputePCIeFatalProtocolStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 2),
    _CfprApComputePCIeFatalProtocolStatsDn_Type()
)
cfprApComputePCIeFatalProtocolStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsDn.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsRn_Type = SnmpAdminString
_CfprApComputePCIeFatalProtocolStatsRn_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsRn = _CfprApComputePCIeFatalProtocolStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 3),
    _CfprApComputePCIeFatalProtocolStatsRn_Type()
)
cfprApComputePCIeFatalProtocolStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsRn.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsDllpErrors_Type = Counter32
_CfprApComputePCIeFatalProtocolStatsDllpErrors_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsDllpErrors = _CfprApComputePCIeFatalProtocolStatsDllpErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 4),
    _CfprApComputePCIeFatalProtocolStatsDllpErrors_Type()
)
cfprApComputePCIeFatalProtocolStatsDllpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsDllpErrors.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsDllpErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsDllpErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsDllpErrors15Min = _CfprApComputePCIeFatalProtocolStatsDllpErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 5),
    _CfprApComputePCIeFatalProtocolStatsDllpErrors15Min_Type()
)
cfprApComputePCIeFatalProtocolStatsDllpErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsDllpErrors15Min.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsDllpErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsDllpErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsDllpErrors15MinH = _CfprApComputePCIeFatalProtocolStatsDllpErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 6),
    _CfprApComputePCIeFatalProtocolStatsDllpErrors15MinH_Type()
)
cfprApComputePCIeFatalProtocolStatsDllpErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsDllpErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsDllpErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsDllpErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsDllpErrors1Day = _CfprApComputePCIeFatalProtocolStatsDllpErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 7),
    _CfprApComputePCIeFatalProtocolStatsDllpErrors1Day_Type()
)
cfprApComputePCIeFatalProtocolStatsDllpErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsDllpErrors1Day.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsDllpErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsDllpErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsDllpErrors1DayH = _CfprApComputePCIeFatalProtocolStatsDllpErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 8),
    _CfprApComputePCIeFatalProtocolStatsDllpErrors1DayH_Type()
)
cfprApComputePCIeFatalProtocolStatsDllpErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsDllpErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsDllpErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsDllpErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsDllpErrors1Hour = _CfprApComputePCIeFatalProtocolStatsDllpErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 9),
    _CfprApComputePCIeFatalProtocolStatsDllpErrors1Hour_Type()
)
cfprApComputePCIeFatalProtocolStatsDllpErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsDllpErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsDllpErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsDllpErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsDllpErrors1HourH = _CfprApComputePCIeFatalProtocolStatsDllpErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 10),
    _CfprApComputePCIeFatalProtocolStatsDllpErrors1HourH_Type()
)
cfprApComputePCIeFatalProtocolStatsDllpErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsDllpErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsDllpErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsDllpErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsDllpErrors1Week = _CfprApComputePCIeFatalProtocolStatsDllpErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 11),
    _CfprApComputePCIeFatalProtocolStatsDllpErrors1Week_Type()
)
cfprApComputePCIeFatalProtocolStatsDllpErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsDllpErrors1Week.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsDllpErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsDllpErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsDllpErrors1WeekH = _CfprApComputePCIeFatalProtocolStatsDllpErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 12),
    _CfprApComputePCIeFatalProtocolStatsDllpErrors1WeekH_Type()
)
cfprApComputePCIeFatalProtocolStatsDllpErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsDllpErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsDllpErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsDllpErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsDllpErrors2Weeks = _CfprApComputePCIeFatalProtocolStatsDllpErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 13),
    _CfprApComputePCIeFatalProtocolStatsDllpErrors2Weeks_Type()
)
cfprApComputePCIeFatalProtocolStatsDllpErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsDllpErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsDllpErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsDllpErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsDllpErrors2WeeksH = _CfprApComputePCIeFatalProtocolStatsDllpErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 14),
    _CfprApComputePCIeFatalProtocolStatsDllpErrors2WeeksH_Type()
)
cfprApComputePCIeFatalProtocolStatsDllpErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsDllpErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors_Type = Counter32
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsFlowControlErrors = _CfprApComputePCIeFatalProtocolStatsFlowControlErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 15),
    _CfprApComputePCIeFatalProtocolStatsFlowControlErrors_Type()
)
cfprApComputePCIeFatalProtocolStatsFlowControlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsFlowControlErrors.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsFlowControlErrors15Min = _CfprApComputePCIeFatalProtocolStatsFlowControlErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 16),
    _CfprApComputePCIeFatalProtocolStatsFlowControlErrors15Min_Type()
)
cfprApComputePCIeFatalProtocolStatsFlowControlErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsFlowControlErrors15Min.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsFlowControlErrors15MinH = _CfprApComputePCIeFatalProtocolStatsFlowControlErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 17),
    _CfprApComputePCIeFatalProtocolStatsFlowControlErrors15MinH_Type()
)
cfprApComputePCIeFatalProtocolStatsFlowControlErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsFlowControlErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Day = _CfprApComputePCIeFatalProtocolStatsFlowControlErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 18),
    _CfprApComputePCIeFatalProtocolStatsFlowControlErrors1Day_Type()
)
cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Day.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsFlowControlErrors1DayH = _CfprApComputePCIeFatalProtocolStatsFlowControlErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 19),
    _CfprApComputePCIeFatalProtocolStatsFlowControlErrors1DayH_Type()
)
cfprApComputePCIeFatalProtocolStatsFlowControlErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsFlowControlErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Hour = _CfprApComputePCIeFatalProtocolStatsFlowControlErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 20),
    _CfprApComputePCIeFatalProtocolStatsFlowControlErrors1Hour_Type()
)
cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsFlowControlErrors1HourH = _CfprApComputePCIeFatalProtocolStatsFlowControlErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 21),
    _CfprApComputePCIeFatalProtocolStatsFlowControlErrors1HourH_Type()
)
cfprApComputePCIeFatalProtocolStatsFlowControlErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsFlowControlErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Week = _CfprApComputePCIeFatalProtocolStatsFlowControlErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 22),
    _CfprApComputePCIeFatalProtocolStatsFlowControlErrors1Week_Type()
)
cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Week.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsFlowControlErrors1WeekH = _CfprApComputePCIeFatalProtocolStatsFlowControlErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 23),
    _CfprApComputePCIeFatalProtocolStatsFlowControlErrors1WeekH_Type()
)
cfprApComputePCIeFatalProtocolStatsFlowControlErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsFlowControlErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsFlowControlErrors2Weeks = _CfprApComputePCIeFatalProtocolStatsFlowControlErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 24),
    _CfprApComputePCIeFatalProtocolStatsFlowControlErrors2Weeks_Type()
)
cfprApComputePCIeFatalProtocolStatsFlowControlErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsFlowControlErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH = _CfprApComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 25),
    _CfprApComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH_Type()
)
cfprApComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsIntervals_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsIntervals_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsIntervals = _CfprApComputePCIeFatalProtocolStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 26),
    _CfprApComputePCIeFatalProtocolStatsIntervals_Type()
)
cfprApComputePCIeFatalProtocolStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsIntervals.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsSuspect_Type = TruthValue
_CfprApComputePCIeFatalProtocolStatsSuspect_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsSuspect = _CfprApComputePCIeFatalProtocolStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 27),
    _CfprApComputePCIeFatalProtocolStatsSuspect_Type()
)
cfprApComputePCIeFatalProtocolStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsSuspect.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsThresholded_Type = CfprApComputePCIeFatalProtocolStatsThresholded
_CfprApComputePCIeFatalProtocolStatsThresholded_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsThresholded = _CfprApComputePCIeFatalProtocolStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 28),
    _CfprApComputePCIeFatalProtocolStatsThresholded_Type()
)
cfprApComputePCIeFatalProtocolStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsThresholded.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsTimeCollected_Type = DateAndTime
_CfprApComputePCIeFatalProtocolStatsTimeCollected_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsTimeCollected = _CfprApComputePCIeFatalProtocolStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 29),
    _CfprApComputePCIeFatalProtocolStatsTimeCollected_Type()
)
cfprApComputePCIeFatalProtocolStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsTimeCollected.setStatus("current")
_CfprApComputePCIeFatalProtocolStatsUpdate_Type = Gauge32
_CfprApComputePCIeFatalProtocolStatsUpdate_Object = MibTableColumn
cfprApComputePCIeFatalProtocolStatsUpdate = _CfprApComputePCIeFatalProtocolStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 31, 1, 30),
    _CfprApComputePCIeFatalProtocolStatsUpdate_Type()
)
cfprApComputePCIeFatalProtocolStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalProtocolStatsUpdate.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsTable_Object = MibTable
cfprApComputePCIeFatalReceiveStatsTable = _CfprApComputePCIeFatalReceiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32)
)
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsTable.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsEntry_Object = MibTableRow
cfprApComputePCIeFatalReceiveStatsEntry = _CfprApComputePCIeFatalReceiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1)
)
cfprApComputePCIeFatalReceiveStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePCIeFatalReceiveStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsEntry.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsInstanceId_Type = CfprApManagedObjectId
_CfprApComputePCIeFatalReceiveStatsInstanceId_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsInstanceId = _CfprApComputePCIeFatalReceiveStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 1),
    _CfprApComputePCIeFatalReceiveStatsInstanceId_Type()
)
cfprApComputePCIeFatalReceiveStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsInstanceId.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsDn_Type = CfprApManagedObjectDn
_CfprApComputePCIeFatalReceiveStatsDn_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsDn = _CfprApComputePCIeFatalReceiveStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 2),
    _CfprApComputePCIeFatalReceiveStatsDn_Type()
)
cfprApComputePCIeFatalReceiveStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsDn.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsRn_Type = SnmpAdminString
_CfprApComputePCIeFatalReceiveStatsRn_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsRn = _CfprApComputePCIeFatalReceiveStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 3),
    _CfprApComputePCIeFatalReceiveStatsRn_Type()
)
cfprApComputePCIeFatalReceiveStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsRn.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors_Type = Counter32
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors = _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 4),
    _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors_Type()
)
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15Min = _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 5),
    _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15Min_Type()
)
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15Min.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH = _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 6),
    _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH_Type()
)
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Day = _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 7),
    _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Day_Type()
)
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Day.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH = _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 8),
    _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH_Type()
)
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour = _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 9),
    _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour_Type()
)
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH = _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 10),
    _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH_Type()
)
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Week = _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 11),
    _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Week_Type()
)
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Week.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH = _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 12),
    _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH_Type()
)
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks = _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 13),
    _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks_Type()
)
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH = _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 14),
    _CfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH_Type()
)
cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors_Type = Counter32
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrFatalErrors = _CfprApComputePCIeFatalReceiveStatsErrFatalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 15),
    _CfprApComputePCIeFatalReceiveStatsErrFatalErrors_Type()
)
cfprApComputePCIeFatalReceiveStatsErrFatalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrFatalErrors.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrFatalErrors15Min = _CfprApComputePCIeFatalReceiveStatsErrFatalErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 16),
    _CfprApComputePCIeFatalReceiveStatsErrFatalErrors15Min_Type()
)
cfprApComputePCIeFatalReceiveStatsErrFatalErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrFatalErrors15Min.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrFatalErrors15MinH = _CfprApComputePCIeFatalReceiveStatsErrFatalErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 17),
    _CfprApComputePCIeFatalReceiveStatsErrFatalErrors15MinH_Type()
)
cfprApComputePCIeFatalReceiveStatsErrFatalErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrFatalErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Day = _CfprApComputePCIeFatalReceiveStatsErrFatalErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 18),
    _CfprApComputePCIeFatalReceiveStatsErrFatalErrors1Day_Type()
)
cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Day.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrFatalErrors1DayH = _CfprApComputePCIeFatalReceiveStatsErrFatalErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 19),
    _CfprApComputePCIeFatalReceiveStatsErrFatalErrors1DayH_Type()
)
cfprApComputePCIeFatalReceiveStatsErrFatalErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrFatalErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Hour = _CfprApComputePCIeFatalReceiveStatsErrFatalErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 20),
    _CfprApComputePCIeFatalReceiveStatsErrFatalErrors1Hour_Type()
)
cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrFatalErrors1HourH = _CfprApComputePCIeFatalReceiveStatsErrFatalErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 21),
    _CfprApComputePCIeFatalReceiveStatsErrFatalErrors1HourH_Type()
)
cfprApComputePCIeFatalReceiveStatsErrFatalErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrFatalErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Week = _CfprApComputePCIeFatalReceiveStatsErrFatalErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 22),
    _CfprApComputePCIeFatalReceiveStatsErrFatalErrors1Week_Type()
)
cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Week.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrFatalErrors1WeekH = _CfprApComputePCIeFatalReceiveStatsErrFatalErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 23),
    _CfprApComputePCIeFatalReceiveStatsErrFatalErrors1WeekH_Type()
)
cfprApComputePCIeFatalReceiveStatsErrFatalErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrFatalErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrFatalErrors2Weeks = _CfprApComputePCIeFatalReceiveStatsErrFatalErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 24),
    _CfprApComputePCIeFatalReceiveStatsErrFatalErrors2Weeks_Type()
)
cfprApComputePCIeFatalReceiveStatsErrFatalErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrFatalErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH = _CfprApComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 25),
    _CfprApComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH_Type()
)
cfprApComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors_Type = Counter32
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors = _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 26),
    _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors_Type()
)
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15Min = _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 27),
    _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15Min_Type()
)
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15Min.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH = _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 28),
    _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH_Type()
)
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Day = _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 29),
    _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Day_Type()
)
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Day.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH = _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 30),
    _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH_Type()
)
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour = _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 31),
    _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour_Type()
)
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH = _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 32),
    _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH_Type()
)
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Week = _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 33),
    _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Week_Type()
)
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Week.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH = _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 34),
    _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH_Type()
)
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks = _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 35),
    _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks_Type()
)
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH = _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 36),
    _CfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH_Type()
)
cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsIntervals_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsIntervals_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsIntervals = _CfprApComputePCIeFatalReceiveStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 37),
    _CfprApComputePCIeFatalReceiveStatsIntervals_Type()
)
cfprApComputePCIeFatalReceiveStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsIntervals.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsSuspect_Type = TruthValue
_CfprApComputePCIeFatalReceiveStatsSuspect_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsSuspect = _CfprApComputePCIeFatalReceiveStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 38),
    _CfprApComputePCIeFatalReceiveStatsSuspect_Type()
)
cfprApComputePCIeFatalReceiveStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsSuspect.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsThresholded_Type = CfprApComputePCIeFatalReceiveStatsThresholded
_CfprApComputePCIeFatalReceiveStatsThresholded_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsThresholded = _CfprApComputePCIeFatalReceiveStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 39),
    _CfprApComputePCIeFatalReceiveStatsThresholded_Type()
)
cfprApComputePCIeFatalReceiveStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsThresholded.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsTimeCollected_Type = DateAndTime
_CfprApComputePCIeFatalReceiveStatsTimeCollected_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsTimeCollected = _CfprApComputePCIeFatalReceiveStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 40),
    _CfprApComputePCIeFatalReceiveStatsTimeCollected_Type()
)
cfprApComputePCIeFatalReceiveStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsTimeCollected.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors_Type = Counter32
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors = _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 41),
    _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors_Type()
)
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min = _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 42),
    _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min_Type()
)
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH = _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 43),
    _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH_Type()
)
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day = _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 44),
    _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day_Type()
)
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH = _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 45),
    _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH_Type()
)
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour = _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 46),
    _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour_Type()
)
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH = _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 47),
    _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH_Type()
)
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week = _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 48),
    _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week_Type()
)
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH = _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 49),
    _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH_Type()
)
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks = _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 50),
    _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks_Type()
)
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH = _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 51),
    _CfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH_Type()
)
cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalReceiveStatsUpdate_Type = Gauge32
_CfprApComputePCIeFatalReceiveStatsUpdate_Object = MibTableColumn
cfprApComputePCIeFatalReceiveStatsUpdate = _CfprApComputePCIeFatalReceiveStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 32, 1, 52),
    _CfprApComputePCIeFatalReceiveStatsUpdate_Type()
)
cfprApComputePCIeFatalReceiveStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalReceiveStatsUpdate.setStatus("current")
_CfprApComputePCIeFatalStatsTable_Object = MibTable
cfprApComputePCIeFatalStatsTable = _CfprApComputePCIeFatalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33)
)
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsTable.setStatus("current")
_CfprApComputePCIeFatalStatsEntry_Object = MibTableRow
cfprApComputePCIeFatalStatsEntry = _CfprApComputePCIeFatalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1)
)
cfprApComputePCIeFatalStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePCIeFatalStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsEntry.setStatus("current")
_CfprApComputePCIeFatalStatsInstanceId_Type = CfprApManagedObjectId
_CfprApComputePCIeFatalStatsInstanceId_Object = MibTableColumn
cfprApComputePCIeFatalStatsInstanceId = _CfprApComputePCIeFatalStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 1),
    _CfprApComputePCIeFatalStatsInstanceId_Type()
)
cfprApComputePCIeFatalStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsInstanceId.setStatus("current")
_CfprApComputePCIeFatalStatsDn_Type = CfprApManagedObjectDn
_CfprApComputePCIeFatalStatsDn_Object = MibTableColumn
cfprApComputePCIeFatalStatsDn = _CfprApComputePCIeFatalStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 2),
    _CfprApComputePCIeFatalStatsDn_Type()
)
cfprApComputePCIeFatalStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsDn.setStatus("current")
_CfprApComputePCIeFatalStatsRn_Type = SnmpAdminString
_CfprApComputePCIeFatalStatsRn_Object = MibTableColumn
cfprApComputePCIeFatalStatsRn = _CfprApComputePCIeFatalStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 3),
    _CfprApComputePCIeFatalStatsRn_Type()
)
cfprApComputePCIeFatalStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsRn.setStatus("current")
_CfprApComputePCIeFatalStatsAcsViolationErrors_Type = Counter32
_CfprApComputePCIeFatalStatsAcsViolationErrors_Object = MibTableColumn
cfprApComputePCIeFatalStatsAcsViolationErrors = _CfprApComputePCIeFatalStatsAcsViolationErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 4),
    _CfprApComputePCIeFatalStatsAcsViolationErrors_Type()
)
cfprApComputePCIeFatalStatsAcsViolationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsAcsViolationErrors.setStatus("current")
_CfprApComputePCIeFatalStatsAcsViolationErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalStatsAcsViolationErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalStatsAcsViolationErrors15Min = _CfprApComputePCIeFatalStatsAcsViolationErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 5),
    _CfprApComputePCIeFatalStatsAcsViolationErrors15Min_Type()
)
cfprApComputePCIeFatalStatsAcsViolationErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsAcsViolationErrors15Min.setStatus("current")
_CfprApComputePCIeFatalStatsAcsViolationErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalStatsAcsViolationErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalStatsAcsViolationErrors15MinH = _CfprApComputePCIeFatalStatsAcsViolationErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 6),
    _CfprApComputePCIeFatalStatsAcsViolationErrors15MinH_Type()
)
cfprApComputePCIeFatalStatsAcsViolationErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsAcsViolationErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalStatsAcsViolationErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalStatsAcsViolationErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalStatsAcsViolationErrors1Day = _CfprApComputePCIeFatalStatsAcsViolationErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 7),
    _CfprApComputePCIeFatalStatsAcsViolationErrors1Day_Type()
)
cfprApComputePCIeFatalStatsAcsViolationErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsAcsViolationErrors1Day.setStatus("current")
_CfprApComputePCIeFatalStatsAcsViolationErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalStatsAcsViolationErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalStatsAcsViolationErrors1DayH = _CfprApComputePCIeFatalStatsAcsViolationErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 8),
    _CfprApComputePCIeFatalStatsAcsViolationErrors1DayH_Type()
)
cfprApComputePCIeFatalStatsAcsViolationErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsAcsViolationErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalStatsAcsViolationErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalStatsAcsViolationErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalStatsAcsViolationErrors1Hour = _CfprApComputePCIeFatalStatsAcsViolationErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 9),
    _CfprApComputePCIeFatalStatsAcsViolationErrors1Hour_Type()
)
cfprApComputePCIeFatalStatsAcsViolationErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsAcsViolationErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalStatsAcsViolationErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalStatsAcsViolationErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalStatsAcsViolationErrors1HourH = _CfprApComputePCIeFatalStatsAcsViolationErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 10),
    _CfprApComputePCIeFatalStatsAcsViolationErrors1HourH_Type()
)
cfprApComputePCIeFatalStatsAcsViolationErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsAcsViolationErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalStatsAcsViolationErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalStatsAcsViolationErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalStatsAcsViolationErrors1Week = _CfprApComputePCIeFatalStatsAcsViolationErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 11),
    _CfprApComputePCIeFatalStatsAcsViolationErrors1Week_Type()
)
cfprApComputePCIeFatalStatsAcsViolationErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsAcsViolationErrors1Week.setStatus("current")
_CfprApComputePCIeFatalStatsAcsViolationErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalStatsAcsViolationErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalStatsAcsViolationErrors1WeekH = _CfprApComputePCIeFatalStatsAcsViolationErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 12),
    _CfprApComputePCIeFatalStatsAcsViolationErrors1WeekH_Type()
)
cfprApComputePCIeFatalStatsAcsViolationErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsAcsViolationErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalStatsAcsViolationErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalStatsAcsViolationErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalStatsAcsViolationErrors2Weeks = _CfprApComputePCIeFatalStatsAcsViolationErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 13),
    _CfprApComputePCIeFatalStatsAcsViolationErrors2Weeks_Type()
)
cfprApComputePCIeFatalStatsAcsViolationErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsAcsViolationErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalStatsAcsViolationErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalStatsAcsViolationErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalStatsAcsViolationErrors2WeeksH = _CfprApComputePCIeFatalStatsAcsViolationErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 14),
    _CfprApComputePCIeFatalStatsAcsViolationErrors2WeeksH_Type()
)
cfprApComputePCIeFatalStatsAcsViolationErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsAcsViolationErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalStatsIntervals_Type = Gauge32
_CfprApComputePCIeFatalStatsIntervals_Object = MibTableColumn
cfprApComputePCIeFatalStatsIntervals = _CfprApComputePCIeFatalStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 15),
    _CfprApComputePCIeFatalStatsIntervals_Type()
)
cfprApComputePCIeFatalStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsIntervals.setStatus("current")
_CfprApComputePCIeFatalStatsMalformedTLPErrors_Type = Counter32
_CfprApComputePCIeFatalStatsMalformedTLPErrors_Object = MibTableColumn
cfprApComputePCIeFatalStatsMalformedTLPErrors = _CfprApComputePCIeFatalStatsMalformedTLPErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 16),
    _CfprApComputePCIeFatalStatsMalformedTLPErrors_Type()
)
cfprApComputePCIeFatalStatsMalformedTLPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsMalformedTLPErrors.setStatus("current")
_CfprApComputePCIeFatalStatsMalformedTLPErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalStatsMalformedTLPErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalStatsMalformedTLPErrors15Min = _CfprApComputePCIeFatalStatsMalformedTLPErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 17),
    _CfprApComputePCIeFatalStatsMalformedTLPErrors15Min_Type()
)
cfprApComputePCIeFatalStatsMalformedTLPErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsMalformedTLPErrors15Min.setStatus("current")
_CfprApComputePCIeFatalStatsMalformedTLPErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalStatsMalformedTLPErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalStatsMalformedTLPErrors15MinH = _CfprApComputePCIeFatalStatsMalformedTLPErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 18),
    _CfprApComputePCIeFatalStatsMalformedTLPErrors15MinH_Type()
)
cfprApComputePCIeFatalStatsMalformedTLPErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsMalformedTLPErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalStatsMalformedTLPErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalStatsMalformedTLPErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalStatsMalformedTLPErrors1Day = _CfprApComputePCIeFatalStatsMalformedTLPErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 19),
    _CfprApComputePCIeFatalStatsMalformedTLPErrors1Day_Type()
)
cfprApComputePCIeFatalStatsMalformedTLPErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsMalformedTLPErrors1Day.setStatus("current")
_CfprApComputePCIeFatalStatsMalformedTLPErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalStatsMalformedTLPErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalStatsMalformedTLPErrors1DayH = _CfprApComputePCIeFatalStatsMalformedTLPErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 20),
    _CfprApComputePCIeFatalStatsMalformedTLPErrors1DayH_Type()
)
cfprApComputePCIeFatalStatsMalformedTLPErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsMalformedTLPErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalStatsMalformedTLPErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalStatsMalformedTLPErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalStatsMalformedTLPErrors1Hour = _CfprApComputePCIeFatalStatsMalformedTLPErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 21),
    _CfprApComputePCIeFatalStatsMalformedTLPErrors1Hour_Type()
)
cfprApComputePCIeFatalStatsMalformedTLPErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsMalformedTLPErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalStatsMalformedTLPErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalStatsMalformedTLPErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalStatsMalformedTLPErrors1HourH = _CfprApComputePCIeFatalStatsMalformedTLPErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 22),
    _CfprApComputePCIeFatalStatsMalformedTLPErrors1HourH_Type()
)
cfprApComputePCIeFatalStatsMalformedTLPErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsMalformedTLPErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalStatsMalformedTLPErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalStatsMalformedTLPErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalStatsMalformedTLPErrors1Week = _CfprApComputePCIeFatalStatsMalformedTLPErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 23),
    _CfprApComputePCIeFatalStatsMalformedTLPErrors1Week_Type()
)
cfprApComputePCIeFatalStatsMalformedTLPErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsMalformedTLPErrors1Week.setStatus("current")
_CfprApComputePCIeFatalStatsMalformedTLPErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalStatsMalformedTLPErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalStatsMalformedTLPErrors1WeekH = _CfprApComputePCIeFatalStatsMalformedTLPErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 24),
    _CfprApComputePCIeFatalStatsMalformedTLPErrors1WeekH_Type()
)
cfprApComputePCIeFatalStatsMalformedTLPErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsMalformedTLPErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalStatsMalformedTLPErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalStatsMalformedTLPErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalStatsMalformedTLPErrors2Weeks = _CfprApComputePCIeFatalStatsMalformedTLPErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 25),
    _CfprApComputePCIeFatalStatsMalformedTLPErrors2Weeks_Type()
)
cfprApComputePCIeFatalStatsMalformedTLPErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsMalformedTLPErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalStatsMalformedTLPErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalStatsMalformedTLPErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalStatsMalformedTLPErrors2WeeksH = _CfprApComputePCIeFatalStatsMalformedTLPErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 26),
    _CfprApComputePCIeFatalStatsMalformedTLPErrors2WeeksH_Type()
)
cfprApComputePCIeFatalStatsMalformedTLPErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsMalformedTLPErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalStatsPoisonedTLPErrors_Type = Counter32
_CfprApComputePCIeFatalStatsPoisonedTLPErrors_Object = MibTableColumn
cfprApComputePCIeFatalStatsPoisonedTLPErrors = _CfprApComputePCIeFatalStatsPoisonedTLPErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 27),
    _CfprApComputePCIeFatalStatsPoisonedTLPErrors_Type()
)
cfprApComputePCIeFatalStatsPoisonedTLPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsPoisonedTLPErrors.setStatus("current")
_CfprApComputePCIeFatalStatsPoisonedTLPErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalStatsPoisonedTLPErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalStatsPoisonedTLPErrors15Min = _CfprApComputePCIeFatalStatsPoisonedTLPErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 28),
    _CfprApComputePCIeFatalStatsPoisonedTLPErrors15Min_Type()
)
cfprApComputePCIeFatalStatsPoisonedTLPErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsPoisonedTLPErrors15Min.setStatus("current")
_CfprApComputePCIeFatalStatsPoisonedTLPErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalStatsPoisonedTLPErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalStatsPoisonedTLPErrors15MinH = _CfprApComputePCIeFatalStatsPoisonedTLPErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 29),
    _CfprApComputePCIeFatalStatsPoisonedTLPErrors15MinH_Type()
)
cfprApComputePCIeFatalStatsPoisonedTLPErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsPoisonedTLPErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalStatsPoisonedTLPErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalStatsPoisonedTLPErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalStatsPoisonedTLPErrors1Day = _CfprApComputePCIeFatalStatsPoisonedTLPErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 30),
    _CfprApComputePCIeFatalStatsPoisonedTLPErrors1Day_Type()
)
cfprApComputePCIeFatalStatsPoisonedTLPErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsPoisonedTLPErrors1Day.setStatus("current")
_CfprApComputePCIeFatalStatsPoisonedTLPErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalStatsPoisonedTLPErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalStatsPoisonedTLPErrors1DayH = _CfprApComputePCIeFatalStatsPoisonedTLPErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 31),
    _CfprApComputePCIeFatalStatsPoisonedTLPErrors1DayH_Type()
)
cfprApComputePCIeFatalStatsPoisonedTLPErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsPoisonedTLPErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalStatsPoisonedTLPErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalStatsPoisonedTLPErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalStatsPoisonedTLPErrors1Hour = _CfprApComputePCIeFatalStatsPoisonedTLPErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 32),
    _CfprApComputePCIeFatalStatsPoisonedTLPErrors1Hour_Type()
)
cfprApComputePCIeFatalStatsPoisonedTLPErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsPoisonedTLPErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalStatsPoisonedTLPErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalStatsPoisonedTLPErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalStatsPoisonedTLPErrors1HourH = _CfprApComputePCIeFatalStatsPoisonedTLPErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 33),
    _CfprApComputePCIeFatalStatsPoisonedTLPErrors1HourH_Type()
)
cfprApComputePCIeFatalStatsPoisonedTLPErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsPoisonedTLPErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalStatsPoisonedTLPErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalStatsPoisonedTLPErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalStatsPoisonedTLPErrors1Week = _CfprApComputePCIeFatalStatsPoisonedTLPErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 34),
    _CfprApComputePCIeFatalStatsPoisonedTLPErrors1Week_Type()
)
cfprApComputePCIeFatalStatsPoisonedTLPErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsPoisonedTLPErrors1Week.setStatus("current")
_CfprApComputePCIeFatalStatsPoisonedTLPErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalStatsPoisonedTLPErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalStatsPoisonedTLPErrors1WeekH = _CfprApComputePCIeFatalStatsPoisonedTLPErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 35),
    _CfprApComputePCIeFatalStatsPoisonedTLPErrors1WeekH_Type()
)
cfprApComputePCIeFatalStatsPoisonedTLPErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsPoisonedTLPErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalStatsPoisonedTLPErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalStatsPoisonedTLPErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalStatsPoisonedTLPErrors2Weeks = _CfprApComputePCIeFatalStatsPoisonedTLPErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 36),
    _CfprApComputePCIeFatalStatsPoisonedTLPErrors2Weeks_Type()
)
cfprApComputePCIeFatalStatsPoisonedTLPErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsPoisonedTLPErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalStatsPoisonedTLPErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalStatsPoisonedTLPErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalStatsPoisonedTLPErrors2WeeksH = _CfprApComputePCIeFatalStatsPoisonedTLPErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 37),
    _CfprApComputePCIeFatalStatsPoisonedTLPErrors2WeeksH_Type()
)
cfprApComputePCIeFatalStatsPoisonedTLPErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsPoisonedTLPErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors_Type = Counter32
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors_Object = MibTableColumn
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors = _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 38),
    _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors_Type()
)
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsSurpriseLinkDownErrors.setStatus("current")
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors15Min_Type = Gauge32
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors15Min_Object = MibTableColumn
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors15Min = _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 39),
    _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors15Min_Type()
)
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsSurpriseLinkDownErrors15Min.setStatus("current")
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors15MinH_Type = Gauge32
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors15MinH_Object = MibTableColumn
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors15MinH = _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 40),
    _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors15MinH_Type()
)
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsSurpriseLinkDownErrors15MinH.setStatus("current")
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Day_Type = Gauge32
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Day_Object = MibTableColumn
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Day = _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 41),
    _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Day_Type()
)
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Day.setStatus("current")
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1DayH_Type = Gauge32
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1DayH_Object = MibTableColumn
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1DayH = _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 42),
    _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1DayH_Type()
)
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1DayH.setStatus("current")
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Hour_Type = Gauge32
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Hour_Object = MibTableColumn
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Hour = _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 43),
    _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Hour_Type()
)
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Hour.setStatus("current")
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1HourH_Type = Gauge32
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1HourH_Object = MibTableColumn
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1HourH = _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 44),
    _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1HourH_Type()
)
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1HourH.setStatus("current")
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Week_Type = Gauge32
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Week_Object = MibTableColumn
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Week = _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 45),
    _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Week_Type()
)
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Week.setStatus("current")
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH_Type = Gauge32
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH_Object = MibTableColumn
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH = _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 46),
    _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH_Type()
)
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH.setStatus("current")
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks_Type = Gauge32
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks_Object = MibTableColumn
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks = _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 47),
    _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks_Type()
)
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks.setStatus("current")
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH_Type = Gauge32
_CfprApComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH_Object = MibTableColumn
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH = _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 48),
    _CfprApComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH_Type()
)
cfprApComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH.setStatus("current")
_CfprApComputePCIeFatalStatsSuspect_Type = TruthValue
_CfprApComputePCIeFatalStatsSuspect_Object = MibTableColumn
cfprApComputePCIeFatalStatsSuspect = _CfprApComputePCIeFatalStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 49),
    _CfprApComputePCIeFatalStatsSuspect_Type()
)
cfprApComputePCIeFatalStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsSuspect.setStatus("current")
_CfprApComputePCIeFatalStatsThresholded_Type = CfprApComputePCIeFatalStatsThresholded
_CfprApComputePCIeFatalStatsThresholded_Object = MibTableColumn
cfprApComputePCIeFatalStatsThresholded = _CfprApComputePCIeFatalStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 50),
    _CfprApComputePCIeFatalStatsThresholded_Type()
)
cfprApComputePCIeFatalStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsThresholded.setStatus("current")
_CfprApComputePCIeFatalStatsTimeCollected_Type = DateAndTime
_CfprApComputePCIeFatalStatsTimeCollected_Object = MibTableColumn
cfprApComputePCIeFatalStatsTimeCollected = _CfprApComputePCIeFatalStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 51),
    _CfprApComputePCIeFatalStatsTimeCollected_Type()
)
cfprApComputePCIeFatalStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsTimeCollected.setStatus("current")
_CfprApComputePCIeFatalStatsUpdate_Type = Gauge32
_CfprApComputePCIeFatalStatsUpdate_Object = MibTableColumn
cfprApComputePCIeFatalStatsUpdate = _CfprApComputePCIeFatalStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 33, 1, 52),
    _CfprApComputePCIeFatalStatsUpdate_Type()
)
cfprApComputePCIeFatalStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePCIeFatalStatsUpdate.setStatus("current")
_CfprApComputePciCapTable_Object = MibTable
cfprApComputePciCapTable = _CfprApComputePciCapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 34)
)
if mibBuilder.loadTexts:
    cfprApComputePciCapTable.setStatus("current")
_CfprApComputePciCapEntry_Object = MibTableRow
cfprApComputePciCapEntry = _CfprApComputePciCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 34, 1)
)
cfprApComputePciCapEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePciCapInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePciCapEntry.setStatus("current")
_CfprApComputePciCapInstanceId_Type = CfprApManagedObjectId
_CfprApComputePciCapInstanceId_Object = MibTableColumn
cfprApComputePciCapInstanceId = _CfprApComputePciCapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 34, 1, 1),
    _CfprApComputePciCapInstanceId_Type()
)
cfprApComputePciCapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePciCapInstanceId.setStatus("current")
_CfprApComputePciCapDn_Type = CfprApManagedObjectDn
_CfprApComputePciCapDn_Object = MibTableColumn
cfprApComputePciCapDn = _CfprApComputePciCapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 34, 1, 2),
    _CfprApComputePciCapDn_Type()
)
cfprApComputePciCapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciCapDn.setStatus("current")
_CfprApComputePciCapRn_Type = SnmpAdminString
_CfprApComputePciCapRn_Object = MibTableColumn
cfprApComputePciCapRn = _CfprApComputePciCapRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 34, 1, 3),
    _CfprApComputePciCapRn_Type()
)
cfprApComputePciCapRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciCapRn.setStatus("current")
_CfprApComputePciCapMaxBusIdPerSlot_Type = Gauge32
_CfprApComputePciCapMaxBusIdPerSlot_Object = MibTableColumn
cfprApComputePciCapMaxBusIdPerSlot = _CfprApComputePciCapMaxBusIdPerSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 34, 1, 4),
    _CfprApComputePciCapMaxBusIdPerSlot_Type()
)
cfprApComputePciCapMaxBusIdPerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciCapMaxBusIdPerSlot.setStatus("current")
_CfprApComputePciCapNumOfPhysSlots_Type = Gauge32
_CfprApComputePciCapNumOfPhysSlots_Object = MibTableColumn
cfprApComputePciCapNumOfPhysSlots = _CfprApComputePciCapNumOfPhysSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 34, 1, 5),
    _CfprApComputePciCapNumOfPhysSlots_Type()
)
cfprApComputePciCapNumOfPhysSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciCapNumOfPhysSlots.setStatus("current")
_CfprApComputePciCapOrder_Type = CfprApComputePciCapOrder
_CfprApComputePciCapOrder_Object = MibTableColumn
cfprApComputePciCapOrder = _CfprApComputePciCapOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 34, 1, 6),
    _CfprApComputePciCapOrder_Type()
)
cfprApComputePciCapOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciCapOrder.setStatus("current")
_CfprApComputePciCapStartsWith_Type = Gauge32
_CfprApComputePciCapStartsWith_Object = MibTableColumn
cfprApComputePciCapStartsWith = _CfprApComputePciCapStartsWith_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 34, 1, 7),
    _CfprApComputePciCapStartsWith_Type()
)
cfprApComputePciCapStartsWith.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciCapStartsWith.setStatus("current")
_CfprApComputePciSlotScanDefTable_Object = MibTable
cfprApComputePciSlotScanDefTable = _CfprApComputePciSlotScanDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 35)
)
if mibBuilder.loadTexts:
    cfprApComputePciSlotScanDefTable.setStatus("current")
_CfprApComputePciSlotScanDefEntry_Object = MibTableRow
cfprApComputePciSlotScanDefEntry = _CfprApComputePciSlotScanDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 35, 1)
)
cfprApComputePciSlotScanDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePciSlotScanDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePciSlotScanDefEntry.setStatus("current")
_CfprApComputePciSlotScanDefInstanceId_Type = CfprApManagedObjectId
_CfprApComputePciSlotScanDefInstanceId_Object = MibTableColumn
cfprApComputePciSlotScanDefInstanceId = _CfprApComputePciSlotScanDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 35, 1, 1),
    _CfprApComputePciSlotScanDefInstanceId_Type()
)
cfprApComputePciSlotScanDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePciSlotScanDefInstanceId.setStatus("current")
_CfprApComputePciSlotScanDefDn_Type = CfprApManagedObjectDn
_CfprApComputePciSlotScanDefDn_Object = MibTableColumn
cfprApComputePciSlotScanDefDn = _CfprApComputePciSlotScanDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 35, 1, 2),
    _CfprApComputePciSlotScanDefDn_Type()
)
cfprApComputePciSlotScanDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciSlotScanDefDn.setStatus("current")
_CfprApComputePciSlotScanDefRn_Type = SnmpAdminString
_CfprApComputePciSlotScanDefRn_Object = MibTableColumn
cfprApComputePciSlotScanDefRn = _CfprApComputePciSlotScanDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 35, 1, 3),
    _CfprApComputePciSlotScanDefRn_Type()
)
cfprApComputePciSlotScanDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciSlotScanDefRn.setStatus("current")
_CfprApComputePciSlotScanDefDescr_Type = SnmpAdminString
_CfprApComputePciSlotScanDefDescr_Object = MibTableColumn
cfprApComputePciSlotScanDefDescr = _CfprApComputePciSlotScanDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 35, 1, 4),
    _CfprApComputePciSlotScanDefDescr_Type()
)
cfprApComputePciSlotScanDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciSlotScanDefDescr.setStatus("current")
_CfprApComputePciSlotScanDefIntId_Type = SnmpAdminString
_CfprApComputePciSlotScanDefIntId_Object = MibTableColumn
cfprApComputePciSlotScanDefIntId = _CfprApComputePciSlotScanDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 35, 1, 5),
    _CfprApComputePciSlotScanDefIntId_Type()
)
cfprApComputePciSlotScanDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciSlotScanDefIntId.setStatus("current")
_CfprApComputePciSlotScanDefName_Type = SnmpAdminString
_CfprApComputePciSlotScanDefName_Object = MibTableColumn
cfprApComputePciSlotScanDefName = _CfprApComputePciSlotScanDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 35, 1, 6),
    _CfprApComputePciSlotScanDefName_Type()
)
cfprApComputePciSlotScanDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciSlotScanDefName.setStatus("current")
_CfprApComputePciSlotScanDefPolicyLevel_Type = Gauge32
_CfprApComputePciSlotScanDefPolicyLevel_Object = MibTableColumn
cfprApComputePciSlotScanDefPolicyLevel = _CfprApComputePciSlotScanDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 35, 1, 7),
    _CfprApComputePciSlotScanDefPolicyLevel_Type()
)
cfprApComputePciSlotScanDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciSlotScanDefPolicyLevel.setStatus("current")
_CfprApComputePciSlotScanDefPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputePciSlotScanDefPolicyOwner_Object = MibTableColumn
cfprApComputePciSlotScanDefPolicyOwner = _CfprApComputePciSlotScanDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 35, 1, 8),
    _CfprApComputePciSlotScanDefPolicyOwner_Type()
)
cfprApComputePciSlotScanDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciSlotScanDefPolicyOwner.setStatus("current")
_CfprApComputePciSlotScanDefScanOrder_Type = Gauge32
_CfprApComputePciSlotScanDefScanOrder_Object = MibTableColumn
cfprApComputePciSlotScanDefScanOrder = _CfprApComputePciSlotScanDefScanOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 35, 1, 9),
    _CfprApComputePciSlotScanDefScanOrder_Type()
)
cfprApComputePciSlotScanDefScanOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciSlotScanDefScanOrder.setStatus("current")
_CfprApComputePciSlotScanDefSlotId_Type = Gauge32
_CfprApComputePciSlotScanDefSlotId_Object = MibTableColumn
cfprApComputePciSlotScanDefSlotId = _CfprApComputePciSlotScanDefSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 35, 1, 10),
    _CfprApComputePciSlotScanDefSlotId_Type()
)
cfprApComputePciSlotScanDefSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePciSlotScanDefSlotId.setStatus("current")
_CfprApComputePhysicalAssocCtxTable_Object = MibTable
cfprApComputePhysicalAssocCtxTable = _CfprApComputePhysicalAssocCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 36)
)
if mibBuilder.loadTexts:
    cfprApComputePhysicalAssocCtxTable.setStatus("current")
_CfprApComputePhysicalAssocCtxEntry_Object = MibTableRow
cfprApComputePhysicalAssocCtxEntry = _CfprApComputePhysicalAssocCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 36, 1)
)
cfprApComputePhysicalAssocCtxEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePhysicalAssocCtxInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePhysicalAssocCtxEntry.setStatus("current")
_CfprApComputePhysicalAssocCtxInstanceId_Type = CfprApManagedObjectId
_CfprApComputePhysicalAssocCtxInstanceId_Object = MibTableColumn
cfprApComputePhysicalAssocCtxInstanceId = _CfprApComputePhysicalAssocCtxInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 36, 1, 1),
    _CfprApComputePhysicalAssocCtxInstanceId_Type()
)
cfprApComputePhysicalAssocCtxInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePhysicalAssocCtxInstanceId.setStatus("current")
_CfprApComputePhysicalAssocCtxDn_Type = CfprApManagedObjectDn
_CfprApComputePhysicalAssocCtxDn_Object = MibTableColumn
cfprApComputePhysicalAssocCtxDn = _CfprApComputePhysicalAssocCtxDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 36, 1, 2),
    _CfprApComputePhysicalAssocCtxDn_Type()
)
cfprApComputePhysicalAssocCtxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalAssocCtxDn.setStatus("current")
_CfprApComputePhysicalAssocCtxRn_Type = SnmpAdminString
_CfprApComputePhysicalAssocCtxRn_Object = MibTableColumn
cfprApComputePhysicalAssocCtxRn = _CfprApComputePhysicalAssocCtxRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 36, 1, 3),
    _CfprApComputePhysicalAssocCtxRn_Type()
)
cfprApComputePhysicalAssocCtxRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalAssocCtxRn.setStatus("current")
_CfprApComputePhysicalAssocCtxFruCapDn_Type = SnmpAdminString
_CfprApComputePhysicalAssocCtxFruCapDn_Object = MibTableColumn
cfprApComputePhysicalAssocCtxFruCapDn = _CfprApComputePhysicalAssocCtxFruCapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 36, 1, 4),
    _CfprApComputePhysicalAssocCtxFruCapDn_Type()
)
cfprApComputePhysicalAssocCtxFruCapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalAssocCtxFruCapDn.setStatus("current")
_CfprApComputePhysicalFsmTable_Object = MibTable
cfprApComputePhysicalFsmTable = _CfprApComputePhysicalFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37)
)
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmTable.setStatus("current")
_CfprApComputePhysicalFsmEntry_Object = MibTableRow
cfprApComputePhysicalFsmEntry = _CfprApComputePhysicalFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37, 1)
)
cfprApComputePhysicalFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePhysicalFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmEntry.setStatus("current")
_CfprApComputePhysicalFsmInstanceId_Type = CfprApManagedObjectId
_CfprApComputePhysicalFsmInstanceId_Object = MibTableColumn
cfprApComputePhysicalFsmInstanceId = _CfprApComputePhysicalFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37, 1, 1),
    _CfprApComputePhysicalFsmInstanceId_Type()
)
cfprApComputePhysicalFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmInstanceId.setStatus("current")
_CfprApComputePhysicalFsmDn_Type = CfprApManagedObjectDn
_CfprApComputePhysicalFsmDn_Object = MibTableColumn
cfprApComputePhysicalFsmDn = _CfprApComputePhysicalFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37, 1, 2),
    _CfprApComputePhysicalFsmDn_Type()
)
cfprApComputePhysicalFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmDn.setStatus("current")
_CfprApComputePhysicalFsmRn_Type = SnmpAdminString
_CfprApComputePhysicalFsmRn_Object = MibTableColumn
cfprApComputePhysicalFsmRn = _CfprApComputePhysicalFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37, 1, 3),
    _CfprApComputePhysicalFsmRn_Type()
)
cfprApComputePhysicalFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmRn.setStatus("current")
_CfprApComputePhysicalFsmCompletionTime_Type = DateAndTime
_CfprApComputePhysicalFsmCompletionTime_Object = MibTableColumn
cfprApComputePhysicalFsmCompletionTime = _CfprApComputePhysicalFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37, 1, 4),
    _CfprApComputePhysicalFsmCompletionTime_Type()
)
cfprApComputePhysicalFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmCompletionTime.setStatus("current")
_CfprApComputePhysicalFsmCurrentFsm_Type = CfprApComputePhysicalFsmCurrentFsm
_CfprApComputePhysicalFsmCurrentFsm_Object = MibTableColumn
cfprApComputePhysicalFsmCurrentFsm = _CfprApComputePhysicalFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37, 1, 5),
    _CfprApComputePhysicalFsmCurrentFsm_Type()
)
cfprApComputePhysicalFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmCurrentFsm.setStatus("current")
_CfprApComputePhysicalFsmDescr_Type = SnmpAdminString
_CfprApComputePhysicalFsmDescr_Object = MibTableColumn
cfprApComputePhysicalFsmDescr = _CfprApComputePhysicalFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37, 1, 6),
    _CfprApComputePhysicalFsmDescr_Type()
)
cfprApComputePhysicalFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmDescr.setStatus("current")
_CfprApComputePhysicalFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApComputePhysicalFsmFsmStatus_Object = MibTableColumn
cfprApComputePhysicalFsmFsmStatus = _CfprApComputePhysicalFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37, 1, 7),
    _CfprApComputePhysicalFsmFsmStatus_Type()
)
cfprApComputePhysicalFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmFsmStatus.setStatus("current")
_CfprApComputePhysicalFsmProgress_Type = Gauge32
_CfprApComputePhysicalFsmProgress_Object = MibTableColumn
cfprApComputePhysicalFsmProgress = _CfprApComputePhysicalFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37, 1, 8),
    _CfprApComputePhysicalFsmProgress_Type()
)
cfprApComputePhysicalFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmProgress.setStatus("current")
_CfprApComputePhysicalFsmRmtErrCode_Type = Gauge32
_CfprApComputePhysicalFsmRmtErrCode_Object = MibTableColumn
cfprApComputePhysicalFsmRmtErrCode = _CfprApComputePhysicalFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37, 1, 9),
    _CfprApComputePhysicalFsmRmtErrCode_Type()
)
cfprApComputePhysicalFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmRmtErrCode.setStatus("current")
_CfprApComputePhysicalFsmRmtErrDescr_Type = SnmpAdminString
_CfprApComputePhysicalFsmRmtErrDescr_Object = MibTableColumn
cfprApComputePhysicalFsmRmtErrDescr = _CfprApComputePhysicalFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37, 1, 10),
    _CfprApComputePhysicalFsmRmtErrDescr_Type()
)
cfprApComputePhysicalFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmRmtErrDescr.setStatus("current")
_CfprApComputePhysicalFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApComputePhysicalFsmRmtRslt_Object = MibTableColumn
cfprApComputePhysicalFsmRmtRslt = _CfprApComputePhysicalFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 37, 1, 11),
    _CfprApComputePhysicalFsmRmtRslt_Type()
)
cfprApComputePhysicalFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmRmtRslt.setStatus("current")
_CfprApComputePhysicalFsmStageTable_Object = MibTable
cfprApComputePhysicalFsmStageTable = _CfprApComputePhysicalFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 38)
)
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmStageTable.setStatus("current")
_CfprApComputePhysicalFsmStageEntry_Object = MibTableRow
cfprApComputePhysicalFsmStageEntry = _CfprApComputePhysicalFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 38, 1)
)
cfprApComputePhysicalFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePhysicalFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmStageEntry.setStatus("current")
_CfprApComputePhysicalFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApComputePhysicalFsmStageInstanceId_Object = MibTableColumn
cfprApComputePhysicalFsmStageInstanceId = _CfprApComputePhysicalFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 38, 1, 1),
    _CfprApComputePhysicalFsmStageInstanceId_Type()
)
cfprApComputePhysicalFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmStageInstanceId.setStatus("current")
_CfprApComputePhysicalFsmStageDn_Type = CfprApManagedObjectDn
_CfprApComputePhysicalFsmStageDn_Object = MibTableColumn
cfprApComputePhysicalFsmStageDn = _CfprApComputePhysicalFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 38, 1, 2),
    _CfprApComputePhysicalFsmStageDn_Type()
)
cfprApComputePhysicalFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmStageDn.setStatus("current")
_CfprApComputePhysicalFsmStageRn_Type = SnmpAdminString
_CfprApComputePhysicalFsmStageRn_Object = MibTableColumn
cfprApComputePhysicalFsmStageRn = _CfprApComputePhysicalFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 38, 1, 3),
    _CfprApComputePhysicalFsmStageRn_Type()
)
cfprApComputePhysicalFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmStageRn.setStatus("current")
_CfprApComputePhysicalFsmStageDescr_Type = SnmpAdminString
_CfprApComputePhysicalFsmStageDescr_Object = MibTableColumn
cfprApComputePhysicalFsmStageDescr = _CfprApComputePhysicalFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 38, 1, 4),
    _CfprApComputePhysicalFsmStageDescr_Type()
)
cfprApComputePhysicalFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmStageDescr.setStatus("current")
_CfprApComputePhysicalFsmStageLastUpdateTime_Type = DateAndTime
_CfprApComputePhysicalFsmStageLastUpdateTime_Object = MibTableColumn
cfprApComputePhysicalFsmStageLastUpdateTime = _CfprApComputePhysicalFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 38, 1, 5),
    _CfprApComputePhysicalFsmStageLastUpdateTime_Type()
)
cfprApComputePhysicalFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmStageLastUpdateTime.setStatus("current")
_CfprApComputePhysicalFsmStageName_Type = CfprApComputePhysicalFsmStageName
_CfprApComputePhysicalFsmStageName_Object = MibTableColumn
cfprApComputePhysicalFsmStageName = _CfprApComputePhysicalFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 38, 1, 6),
    _CfprApComputePhysicalFsmStageName_Type()
)
cfprApComputePhysicalFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmStageName.setStatus("current")
_CfprApComputePhysicalFsmStageOrder_Type = Gauge32
_CfprApComputePhysicalFsmStageOrder_Object = MibTableColumn
cfprApComputePhysicalFsmStageOrder = _CfprApComputePhysicalFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 38, 1, 7),
    _CfprApComputePhysicalFsmStageOrder_Type()
)
cfprApComputePhysicalFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmStageOrder.setStatus("current")
_CfprApComputePhysicalFsmStageRetry_Type = Gauge32
_CfprApComputePhysicalFsmStageRetry_Object = MibTableColumn
cfprApComputePhysicalFsmStageRetry = _CfprApComputePhysicalFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 38, 1, 8),
    _CfprApComputePhysicalFsmStageRetry_Type()
)
cfprApComputePhysicalFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmStageRetry.setStatus("current")
_CfprApComputePhysicalFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApComputePhysicalFsmStageStageStatus_Object = MibTableColumn
cfprApComputePhysicalFsmStageStageStatus = _CfprApComputePhysicalFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 38, 1, 9),
    _CfprApComputePhysicalFsmStageStageStatus_Type()
)
cfprApComputePhysicalFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmStageStageStatus.setStatus("current")
_CfprApComputePhysicalFsmTaskTable_Object = MibTable
cfprApComputePhysicalFsmTaskTable = _CfprApComputePhysicalFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 39)
)
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmTaskTable.setStatus("current")
_CfprApComputePhysicalFsmTaskEntry_Object = MibTableRow
cfprApComputePhysicalFsmTaskEntry = _CfprApComputePhysicalFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 39, 1)
)
cfprApComputePhysicalFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePhysicalFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmTaskEntry.setStatus("current")
_CfprApComputePhysicalFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApComputePhysicalFsmTaskInstanceId_Object = MibTableColumn
cfprApComputePhysicalFsmTaskInstanceId = _CfprApComputePhysicalFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 39, 1, 1),
    _CfprApComputePhysicalFsmTaskInstanceId_Type()
)
cfprApComputePhysicalFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmTaskInstanceId.setStatus("current")
_CfprApComputePhysicalFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApComputePhysicalFsmTaskDn_Object = MibTableColumn
cfprApComputePhysicalFsmTaskDn = _CfprApComputePhysicalFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 39, 1, 2),
    _CfprApComputePhysicalFsmTaskDn_Type()
)
cfprApComputePhysicalFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmTaskDn.setStatus("current")
_CfprApComputePhysicalFsmTaskRn_Type = SnmpAdminString
_CfprApComputePhysicalFsmTaskRn_Object = MibTableColumn
cfprApComputePhysicalFsmTaskRn = _CfprApComputePhysicalFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 39, 1, 3),
    _CfprApComputePhysicalFsmTaskRn_Type()
)
cfprApComputePhysicalFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmTaskRn.setStatus("current")
_CfprApComputePhysicalFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApComputePhysicalFsmTaskCompletion_Object = MibTableColumn
cfprApComputePhysicalFsmTaskCompletion = _CfprApComputePhysicalFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 39, 1, 4),
    _CfprApComputePhysicalFsmTaskCompletion_Type()
)
cfprApComputePhysicalFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmTaskCompletion.setStatus("current")
_CfprApComputePhysicalFsmTaskFlags_Type = CfprApFsmFlags
_CfprApComputePhysicalFsmTaskFlags_Object = MibTableColumn
cfprApComputePhysicalFsmTaskFlags = _CfprApComputePhysicalFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 39, 1, 5),
    _CfprApComputePhysicalFsmTaskFlags_Type()
)
cfprApComputePhysicalFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmTaskFlags.setStatus("current")
_CfprApComputePhysicalFsmTaskItem_Type = CfprApComputePhysicalFsmTaskItem
_CfprApComputePhysicalFsmTaskItem_Object = MibTableColumn
cfprApComputePhysicalFsmTaskItem = _CfprApComputePhysicalFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 39, 1, 6),
    _CfprApComputePhysicalFsmTaskItem_Type()
)
cfprApComputePhysicalFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmTaskItem.setStatus("current")
_CfprApComputePhysicalFsmTaskSeqId_Type = Gauge32
_CfprApComputePhysicalFsmTaskSeqId_Object = MibTableColumn
cfprApComputePhysicalFsmTaskSeqId = _CfprApComputePhysicalFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 39, 1, 7),
    _CfprApComputePhysicalFsmTaskSeqId_Type()
)
cfprApComputePhysicalFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalFsmTaskSeqId.setStatus("current")
_CfprApComputePhysicalQualTable_Object = MibTable
cfprApComputePhysicalQualTable = _CfprApComputePhysicalQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 40)
)
if mibBuilder.loadTexts:
    cfprApComputePhysicalQualTable.setStatus("current")
_CfprApComputePhysicalQualEntry_Object = MibTableRow
cfprApComputePhysicalQualEntry = _CfprApComputePhysicalQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 40, 1)
)
cfprApComputePhysicalQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePhysicalQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePhysicalQualEntry.setStatus("current")
_CfprApComputePhysicalQualInstanceId_Type = CfprApManagedObjectId
_CfprApComputePhysicalQualInstanceId_Object = MibTableColumn
cfprApComputePhysicalQualInstanceId = _CfprApComputePhysicalQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 40, 1, 1),
    _CfprApComputePhysicalQualInstanceId_Type()
)
cfprApComputePhysicalQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePhysicalQualInstanceId.setStatus("current")
_CfprApComputePhysicalQualDn_Type = CfprApManagedObjectDn
_CfprApComputePhysicalQualDn_Object = MibTableColumn
cfprApComputePhysicalQualDn = _CfprApComputePhysicalQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 40, 1, 2),
    _CfprApComputePhysicalQualDn_Type()
)
cfprApComputePhysicalQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalQualDn.setStatus("current")
_CfprApComputePhysicalQualRn_Type = SnmpAdminString
_CfprApComputePhysicalQualRn_Object = MibTableColumn
cfprApComputePhysicalQualRn = _CfprApComputePhysicalQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 40, 1, 3),
    _CfprApComputePhysicalQualRn_Type()
)
cfprApComputePhysicalQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalQualRn.setStatus("current")
_CfprApComputePhysicalQualModel_Type = SnmpAdminString
_CfprApComputePhysicalQualModel_Object = MibTableColumn
cfprApComputePhysicalQualModel = _CfprApComputePhysicalQualModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 40, 1, 4),
    _CfprApComputePhysicalQualModel_Type()
)
cfprApComputePhysicalQualModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePhysicalQualModel.setStatus("current")
_CfprApComputePlatformTable_Object = MibTable
cfprApComputePlatformTable = _CfprApComputePlatformTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 41)
)
if mibBuilder.loadTexts:
    cfprApComputePlatformTable.setStatus("current")
_CfprApComputePlatformEntry_Object = MibTableRow
cfprApComputePlatformEntry = _CfprApComputePlatformEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 41, 1)
)
cfprApComputePlatformEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePlatformInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePlatformEntry.setStatus("current")
_CfprApComputePlatformInstanceId_Type = CfprApManagedObjectId
_CfprApComputePlatformInstanceId_Object = MibTableColumn
cfprApComputePlatformInstanceId = _CfprApComputePlatformInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 41, 1, 1),
    _CfprApComputePlatformInstanceId_Type()
)
cfprApComputePlatformInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePlatformInstanceId.setStatus("current")
_CfprApComputePlatformDn_Type = CfprApManagedObjectDn
_CfprApComputePlatformDn_Object = MibTableColumn
cfprApComputePlatformDn = _CfprApComputePlatformDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 41, 1, 2),
    _CfprApComputePlatformDn_Type()
)
cfprApComputePlatformDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePlatformDn.setStatus("current")
_CfprApComputePlatformRn_Type = SnmpAdminString
_CfprApComputePlatformRn_Object = MibTableColumn
cfprApComputePlatformRn = _CfprApComputePlatformRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 41, 1, 3),
    _CfprApComputePlatformRn_Type()
)
cfprApComputePlatformRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePlatformRn.setStatus("current")
_CfprApComputePlatformModel_Type = SnmpAdminString
_CfprApComputePlatformModel_Object = MibTableColumn
cfprApComputePlatformModel = _CfprApComputePlatformModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 41, 1, 4),
    _CfprApComputePlatformModel_Type()
)
cfprApComputePlatformModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePlatformModel.setStatus("current")
_CfprApComputePlatformProductName_Type = SnmpAdminString
_CfprApComputePlatformProductName_Object = MibTableColumn
cfprApComputePlatformProductName = _CfprApComputePlatformProductName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 41, 1, 5),
    _CfprApComputePlatformProductName_Type()
)
cfprApComputePlatformProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePlatformProductName.setStatus("current")
_CfprApComputePlatformRevision_Type = SnmpAdminString
_CfprApComputePlatformRevision_Object = MibTableColumn
cfprApComputePlatformRevision = _CfprApComputePlatformRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 41, 1, 6),
    _CfprApComputePlatformRevision_Type()
)
cfprApComputePlatformRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePlatformRevision.setStatus("current")
_CfprApComputePlatformVendor_Type = SnmpAdminString
_CfprApComputePlatformVendor_Object = MibTableColumn
cfprApComputePlatformVendor = _CfprApComputePlatformVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 41, 1, 7),
    _CfprApComputePlatformVendor_Type()
)
cfprApComputePlatformVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePlatformVendor.setStatus("current")
_CfprApComputePnuOSImageTable_Object = MibTable
cfprApComputePnuOSImageTable = _CfprApComputePnuOSImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 42)
)
if mibBuilder.loadTexts:
    cfprApComputePnuOSImageTable.setStatus("current")
_CfprApComputePnuOSImageEntry_Object = MibTableRow
cfprApComputePnuOSImageEntry = _CfprApComputePnuOSImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 42, 1)
)
cfprApComputePnuOSImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePnuOSImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePnuOSImageEntry.setStatus("current")
_CfprApComputePnuOSImageInstanceId_Type = CfprApManagedObjectId
_CfprApComputePnuOSImageInstanceId_Object = MibTableColumn
cfprApComputePnuOSImageInstanceId = _CfprApComputePnuOSImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 42, 1, 1),
    _CfprApComputePnuOSImageInstanceId_Type()
)
cfprApComputePnuOSImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePnuOSImageInstanceId.setStatus("current")
_CfprApComputePnuOSImageDn_Type = CfprApManagedObjectDn
_CfprApComputePnuOSImageDn_Object = MibTableColumn
cfprApComputePnuOSImageDn = _CfprApComputePnuOSImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 42, 1, 2),
    _CfprApComputePnuOSImageDn_Type()
)
cfprApComputePnuOSImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePnuOSImageDn.setStatus("current")
_CfprApComputePnuOSImageRn_Type = SnmpAdminString
_CfprApComputePnuOSImageRn_Object = MibTableColumn
cfprApComputePnuOSImageRn = _CfprApComputePnuOSImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 42, 1, 3),
    _CfprApComputePnuOSImageRn_Type()
)
cfprApComputePnuOSImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePnuOSImageRn.setStatus("current")
_CfprApComputePnuOSImageImgLFBFFName_Type = SnmpAdminString
_CfprApComputePnuOSImageImgLFBFFName_Object = MibTableColumn
cfprApComputePnuOSImageImgLFBFFName = _CfprApComputePnuOSImageImgLFBFFName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 42, 1, 4),
    _CfprApComputePnuOSImageImgLFBFFName_Type()
)
cfprApComputePnuOSImageImgLFBFFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePnuOSImageImgLFBFFName.setStatus("current")
_CfprApComputePnuOSImageImgLoc_Type = SnmpAdminString
_CfprApComputePnuOSImageImgLoc_Object = MibTableColumn
cfprApComputePnuOSImageImgLoc = _CfprApComputePnuOSImageImgLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 42, 1, 5),
    _CfprApComputePnuOSImageImgLoc_Type()
)
cfprApComputePnuOSImageImgLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePnuOSImageImgLoc.setStatus("current")
_CfprApComputePnuOSImageImgName_Type = SnmpAdminString
_CfprApComputePnuOSImageImgName_Object = MibTableColumn
cfprApComputePnuOSImageImgName = _CfprApComputePnuOSImageImgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 42, 1, 6),
    _CfprApComputePnuOSImageImgName_Type()
)
cfprApComputePnuOSImageImgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePnuOSImageImgName.setStatus("current")
_CfprApComputePoolTable_Object = MibTable
cfprApComputePoolTable = _CfprApComputePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43)
)
if mibBuilder.loadTexts:
    cfprApComputePoolTable.setStatus("current")
_CfprApComputePoolEntry_Object = MibTableRow
cfprApComputePoolEntry = _CfprApComputePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43, 1)
)
cfprApComputePoolEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePoolInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePoolEntry.setStatus("current")
_CfprApComputePoolInstanceId_Type = CfprApManagedObjectId
_CfprApComputePoolInstanceId_Object = MibTableColumn
cfprApComputePoolInstanceId = _CfprApComputePoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43, 1, 1),
    _CfprApComputePoolInstanceId_Type()
)
cfprApComputePoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePoolInstanceId.setStatus("current")
_CfprApComputePoolDn_Type = CfprApManagedObjectDn
_CfprApComputePoolDn_Object = MibTableColumn
cfprApComputePoolDn = _CfprApComputePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43, 1, 2),
    _CfprApComputePoolDn_Type()
)
cfprApComputePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolDn.setStatus("current")
_CfprApComputePoolRn_Type = SnmpAdminString
_CfprApComputePoolRn_Object = MibTableColumn
cfprApComputePoolRn = _CfprApComputePoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43, 1, 3),
    _CfprApComputePoolRn_Type()
)
cfprApComputePoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolRn.setStatus("current")
_CfprApComputePoolAssigned_Type = Gauge32
_CfprApComputePoolAssigned_Object = MibTableColumn
cfprApComputePoolAssigned = _CfprApComputePoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43, 1, 4),
    _CfprApComputePoolAssigned_Type()
)
cfprApComputePoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolAssigned.setStatus("current")
_CfprApComputePoolAssignmentOrder_Type = CfprApPoolPoolAssignmentOrder
_CfprApComputePoolAssignmentOrder_Object = MibTableColumn
cfprApComputePoolAssignmentOrder = _CfprApComputePoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43, 1, 5),
    _CfprApComputePoolAssignmentOrder_Type()
)
cfprApComputePoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolAssignmentOrder.setStatus("current")
_CfprApComputePoolDescr_Type = SnmpAdminString
_CfprApComputePoolDescr_Object = MibTableColumn
cfprApComputePoolDescr = _CfprApComputePoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43, 1, 6),
    _CfprApComputePoolDescr_Type()
)
cfprApComputePoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolDescr.setStatus("current")
_CfprApComputePoolIntId_Type = SnmpAdminString
_CfprApComputePoolIntId_Object = MibTableColumn
cfprApComputePoolIntId = _CfprApComputePoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43, 1, 7),
    _CfprApComputePoolIntId_Type()
)
cfprApComputePoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolIntId.setStatus("current")
_CfprApComputePoolName_Type = SnmpAdminString
_CfprApComputePoolName_Object = MibTableColumn
cfprApComputePoolName = _CfprApComputePoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43, 1, 8),
    _CfprApComputePoolName_Type()
)
cfprApComputePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolName.setStatus("current")
_CfprApComputePoolPolicyLevel_Type = Gauge32
_CfprApComputePoolPolicyLevel_Object = MibTableColumn
cfprApComputePoolPolicyLevel = _CfprApComputePoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43, 1, 9),
    _CfprApComputePoolPolicyLevel_Type()
)
cfprApComputePoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolPolicyLevel.setStatus("current")
_CfprApComputePoolPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputePoolPolicyOwner_Object = MibTableColumn
cfprApComputePoolPolicyOwner = _CfprApComputePoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43, 1, 10),
    _CfprApComputePoolPolicyOwner_Type()
)
cfprApComputePoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolPolicyOwner.setStatus("current")
_CfprApComputePoolSize_Type = Gauge32
_CfprApComputePoolSize_Object = MibTableColumn
cfprApComputePoolSize = _CfprApComputePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 43, 1, 11),
    _CfprApComputePoolSize_Type()
)
cfprApComputePoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolSize.setStatus("current")
_CfprApComputePoolPolicyRefTable_Object = MibTable
cfprApComputePoolPolicyRefTable = _CfprApComputePoolPolicyRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 44)
)
if mibBuilder.loadTexts:
    cfprApComputePoolPolicyRefTable.setStatus("current")
_CfprApComputePoolPolicyRefEntry_Object = MibTableRow
cfprApComputePoolPolicyRefEntry = _CfprApComputePoolPolicyRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 44, 1)
)
cfprApComputePoolPolicyRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePoolPolicyRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePoolPolicyRefEntry.setStatus("current")
_CfprApComputePoolPolicyRefInstanceId_Type = CfprApManagedObjectId
_CfprApComputePoolPolicyRefInstanceId_Object = MibTableColumn
cfprApComputePoolPolicyRefInstanceId = _CfprApComputePoolPolicyRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 44, 1, 1),
    _CfprApComputePoolPolicyRefInstanceId_Type()
)
cfprApComputePoolPolicyRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePoolPolicyRefInstanceId.setStatus("current")
_CfprApComputePoolPolicyRefDn_Type = CfprApManagedObjectDn
_CfprApComputePoolPolicyRefDn_Object = MibTableColumn
cfprApComputePoolPolicyRefDn = _CfprApComputePoolPolicyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 44, 1, 2),
    _CfprApComputePoolPolicyRefDn_Type()
)
cfprApComputePoolPolicyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolPolicyRefDn.setStatus("current")
_CfprApComputePoolPolicyRefRn_Type = SnmpAdminString
_CfprApComputePoolPolicyRefRn_Object = MibTableColumn
cfprApComputePoolPolicyRefRn = _CfprApComputePoolPolicyRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 44, 1, 3),
    _CfprApComputePoolPolicyRefRn_Type()
)
cfprApComputePoolPolicyRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolPolicyRefRn.setStatus("current")
_CfprApComputePoolPolicyRefId_Type = Unsigned64
_CfprApComputePoolPolicyRefId_Object = MibTableColumn
cfprApComputePoolPolicyRefId = _CfprApComputePoolPolicyRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 44, 1, 4),
    _CfprApComputePoolPolicyRefId_Type()
)
cfprApComputePoolPolicyRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolPolicyRefId.setStatus("current")
_CfprApComputePoolPolicyRefPolicyDn_Type = SnmpAdminString
_CfprApComputePoolPolicyRefPolicyDn_Object = MibTableColumn
cfprApComputePoolPolicyRefPolicyDn = _CfprApComputePoolPolicyRefPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 44, 1, 5),
    _CfprApComputePoolPolicyRefPolicyDn_Type()
)
cfprApComputePoolPolicyRefPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolPolicyRefPolicyDn.setStatus("current")
_CfprApComputePoolableTable_Object = MibTable
cfprApComputePoolableTable = _CfprApComputePoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 45)
)
if mibBuilder.loadTexts:
    cfprApComputePoolableTable.setStatus("current")
_CfprApComputePoolableEntry_Object = MibTableRow
cfprApComputePoolableEntry = _CfprApComputePoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 45, 1)
)
cfprApComputePoolableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePoolableEntry.setStatus("current")
_CfprApComputePoolableInstanceId_Type = CfprApManagedObjectId
_CfprApComputePoolableInstanceId_Object = MibTableColumn
cfprApComputePoolableInstanceId = _CfprApComputePoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 45, 1, 1),
    _CfprApComputePoolableInstanceId_Type()
)
cfprApComputePoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePoolableInstanceId.setStatus("current")
_CfprApComputePoolableDn_Type = CfprApManagedObjectDn
_CfprApComputePoolableDn_Object = MibTableColumn
cfprApComputePoolableDn = _CfprApComputePoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 45, 1, 2),
    _CfprApComputePoolableDn_Type()
)
cfprApComputePoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolableDn.setStatus("current")
_CfprApComputePoolableRn_Type = SnmpAdminString
_CfprApComputePoolableRn_Object = MibTableColumn
cfprApComputePoolableRn = _CfprApComputePoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 45, 1, 3),
    _CfprApComputePoolableRn_Type()
)
cfprApComputePoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolableRn.setStatus("current")
_CfprApComputePoolableId_Type = Unsigned64
_CfprApComputePoolableId_Object = MibTableColumn
cfprApComputePoolableId = _CfprApComputePoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 45, 1, 4),
    _CfprApComputePoolableId_Type()
)
cfprApComputePoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolableId.setStatus("current")
_CfprApComputePoolablePoolDn_Type = SnmpAdminString
_CfprApComputePoolablePoolDn_Object = MibTableColumn
cfprApComputePoolablePoolDn = _CfprApComputePoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 45, 1, 5),
    _CfprApComputePoolablePoolDn_Type()
)
cfprApComputePoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolablePoolDn.setStatus("current")
_CfprApComputePooledRackUnitTable_Object = MibTable
cfprApComputePooledRackUnitTable = _CfprApComputePooledRackUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 46)
)
if mibBuilder.loadTexts:
    cfprApComputePooledRackUnitTable.setStatus("current")
_CfprApComputePooledRackUnitEntry_Object = MibTableRow
cfprApComputePooledRackUnitEntry = _CfprApComputePooledRackUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 46, 1)
)
cfprApComputePooledRackUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePooledRackUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePooledRackUnitEntry.setStatus("current")
_CfprApComputePooledRackUnitInstanceId_Type = CfprApManagedObjectId
_CfprApComputePooledRackUnitInstanceId_Object = MibTableColumn
cfprApComputePooledRackUnitInstanceId = _CfprApComputePooledRackUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 46, 1, 1),
    _CfprApComputePooledRackUnitInstanceId_Type()
)
cfprApComputePooledRackUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePooledRackUnitInstanceId.setStatus("current")
_CfprApComputePooledRackUnitDn_Type = CfprApManagedObjectDn
_CfprApComputePooledRackUnitDn_Object = MibTableColumn
cfprApComputePooledRackUnitDn = _CfprApComputePooledRackUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 46, 1, 2),
    _CfprApComputePooledRackUnitDn_Type()
)
cfprApComputePooledRackUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledRackUnitDn.setStatus("current")
_CfprApComputePooledRackUnitRn_Type = SnmpAdminString
_CfprApComputePooledRackUnitRn_Object = MibTableColumn
cfprApComputePooledRackUnitRn = _CfprApComputePooledRackUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 46, 1, 3),
    _CfprApComputePooledRackUnitRn_Type()
)
cfprApComputePooledRackUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledRackUnitRn.setStatus("current")
_CfprApComputePooledRackUnitAssigned_Type = TruthValue
_CfprApComputePooledRackUnitAssigned_Object = MibTableColumn
cfprApComputePooledRackUnitAssigned = _CfprApComputePooledRackUnitAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 46, 1, 4),
    _CfprApComputePooledRackUnitAssigned_Type()
)
cfprApComputePooledRackUnitAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledRackUnitAssigned.setStatus("current")
_CfprApComputePooledRackUnitAssignedToDn_Type = SnmpAdminString
_CfprApComputePooledRackUnitAssignedToDn_Object = MibTableColumn
cfprApComputePooledRackUnitAssignedToDn = _CfprApComputePooledRackUnitAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 46, 1, 5),
    _CfprApComputePooledRackUnitAssignedToDn_Type()
)
cfprApComputePooledRackUnitAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledRackUnitAssignedToDn.setStatus("current")
_CfprApComputePooledRackUnitId_Type = CfprApComputePooledRackUnitId
_CfprApComputePooledRackUnitId_Object = MibTableColumn
cfprApComputePooledRackUnitId = _CfprApComputePooledRackUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 46, 1, 6),
    _CfprApComputePooledRackUnitId_Type()
)
cfprApComputePooledRackUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledRackUnitId.setStatus("current")
_CfprApComputePooledRackUnitOwner_Type = CfprApComputeOwner
_CfprApComputePooledRackUnitOwner_Object = MibTableColumn
cfprApComputePooledRackUnitOwner = _CfprApComputePooledRackUnitOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 46, 1, 7),
    _CfprApComputePooledRackUnitOwner_Type()
)
cfprApComputePooledRackUnitOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledRackUnitOwner.setStatus("current")
_CfprApComputePooledRackUnitPoolableDn_Type = SnmpAdminString
_CfprApComputePooledRackUnitPoolableDn_Object = MibTableColumn
cfprApComputePooledRackUnitPoolableDn = _CfprApComputePooledRackUnitPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 46, 1, 8),
    _CfprApComputePooledRackUnitPoolableDn_Type()
)
cfprApComputePooledRackUnitPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledRackUnitPoolableDn.setStatus("current")
_CfprApComputePooledRackUnitPrevAssignedToDn_Type = SnmpAdminString
_CfprApComputePooledRackUnitPrevAssignedToDn_Object = MibTableColumn
cfprApComputePooledRackUnitPrevAssignedToDn = _CfprApComputePooledRackUnitPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 46, 1, 9),
    _CfprApComputePooledRackUnitPrevAssignedToDn_Type()
)
cfprApComputePooledRackUnitPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledRackUnitPrevAssignedToDn.setStatus("current")
_CfprApComputePooledSlotTable_Object = MibTable
cfprApComputePooledSlotTable = _CfprApComputePooledSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 47)
)
if mibBuilder.loadTexts:
    cfprApComputePooledSlotTable.setStatus("current")
_CfprApComputePooledSlotEntry_Object = MibTableRow
cfprApComputePooledSlotEntry = _CfprApComputePooledSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 47, 1)
)
cfprApComputePooledSlotEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePooledSlotInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePooledSlotEntry.setStatus("current")
_CfprApComputePooledSlotInstanceId_Type = CfprApManagedObjectId
_CfprApComputePooledSlotInstanceId_Object = MibTableColumn
cfprApComputePooledSlotInstanceId = _CfprApComputePooledSlotInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 47, 1, 1),
    _CfprApComputePooledSlotInstanceId_Type()
)
cfprApComputePooledSlotInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePooledSlotInstanceId.setStatus("current")
_CfprApComputePooledSlotDn_Type = CfprApManagedObjectDn
_CfprApComputePooledSlotDn_Object = MibTableColumn
cfprApComputePooledSlotDn = _CfprApComputePooledSlotDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 47, 1, 2),
    _CfprApComputePooledSlotDn_Type()
)
cfprApComputePooledSlotDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledSlotDn.setStatus("current")
_CfprApComputePooledSlotRn_Type = SnmpAdminString
_CfprApComputePooledSlotRn_Object = MibTableColumn
cfprApComputePooledSlotRn = _CfprApComputePooledSlotRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 47, 1, 3),
    _CfprApComputePooledSlotRn_Type()
)
cfprApComputePooledSlotRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledSlotRn.setStatus("current")
_CfprApComputePooledSlotAssigned_Type = TruthValue
_CfprApComputePooledSlotAssigned_Object = MibTableColumn
cfprApComputePooledSlotAssigned = _CfprApComputePooledSlotAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 47, 1, 4),
    _CfprApComputePooledSlotAssigned_Type()
)
cfprApComputePooledSlotAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledSlotAssigned.setStatus("current")
_CfprApComputePooledSlotAssignedToDn_Type = SnmpAdminString
_CfprApComputePooledSlotAssignedToDn_Object = MibTableColumn
cfprApComputePooledSlotAssignedToDn = _CfprApComputePooledSlotAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 47, 1, 5),
    _CfprApComputePooledSlotAssignedToDn_Type()
)
cfprApComputePooledSlotAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledSlotAssignedToDn.setStatus("current")
_CfprApComputePooledSlotChassisId_Type = Gauge32
_CfprApComputePooledSlotChassisId_Object = MibTableColumn
cfprApComputePooledSlotChassisId = _CfprApComputePooledSlotChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 47, 1, 6),
    _CfprApComputePooledSlotChassisId_Type()
)
cfprApComputePooledSlotChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledSlotChassisId.setStatus("current")
_CfprApComputePooledSlotOwner_Type = CfprApComputeOwner
_CfprApComputePooledSlotOwner_Object = MibTableColumn
cfprApComputePooledSlotOwner = _CfprApComputePooledSlotOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 47, 1, 7),
    _CfprApComputePooledSlotOwner_Type()
)
cfprApComputePooledSlotOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledSlotOwner.setStatus("current")
_CfprApComputePooledSlotPoolableDn_Type = SnmpAdminString
_CfprApComputePooledSlotPoolableDn_Object = MibTableColumn
cfprApComputePooledSlotPoolableDn = _CfprApComputePooledSlotPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 47, 1, 8),
    _CfprApComputePooledSlotPoolableDn_Type()
)
cfprApComputePooledSlotPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledSlotPoolableDn.setStatus("current")
_CfprApComputePooledSlotPrevAssignedToDn_Type = SnmpAdminString
_CfprApComputePooledSlotPrevAssignedToDn_Object = MibTableColumn
cfprApComputePooledSlotPrevAssignedToDn = _CfprApComputePooledSlotPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 47, 1, 9),
    _CfprApComputePooledSlotPrevAssignedToDn_Type()
)
cfprApComputePooledSlotPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledSlotPrevAssignedToDn.setStatus("current")
_CfprApComputePooledSlotSlotId_Type = CfprApComputePooledSlotSlotId
_CfprApComputePooledSlotSlotId_Object = MibTableColumn
cfprApComputePooledSlotSlotId = _CfprApComputePooledSlotSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 47, 1, 10),
    _CfprApComputePooledSlotSlotId_Type()
)
cfprApComputePooledSlotSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePooledSlotSlotId.setStatus("current")
_CfprApComputePoolingPolicyTable_Object = MibTable
cfprApComputePoolingPolicyTable = _CfprApComputePoolingPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 48)
)
if mibBuilder.loadTexts:
    cfprApComputePoolingPolicyTable.setStatus("current")
_CfprApComputePoolingPolicyEntry_Object = MibTableRow
cfprApComputePoolingPolicyEntry = _CfprApComputePoolingPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 48, 1)
)
cfprApComputePoolingPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePoolingPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePoolingPolicyEntry.setStatus("current")
_CfprApComputePoolingPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApComputePoolingPolicyInstanceId_Object = MibTableColumn
cfprApComputePoolingPolicyInstanceId = _CfprApComputePoolingPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 48, 1, 1),
    _CfprApComputePoolingPolicyInstanceId_Type()
)
cfprApComputePoolingPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePoolingPolicyInstanceId.setStatus("current")
_CfprApComputePoolingPolicyDn_Type = CfprApManagedObjectDn
_CfprApComputePoolingPolicyDn_Object = MibTableColumn
cfprApComputePoolingPolicyDn = _CfprApComputePoolingPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 48, 1, 2),
    _CfprApComputePoolingPolicyDn_Type()
)
cfprApComputePoolingPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolingPolicyDn.setStatus("current")
_CfprApComputePoolingPolicyRn_Type = SnmpAdminString
_CfprApComputePoolingPolicyRn_Object = MibTableColumn
cfprApComputePoolingPolicyRn = _CfprApComputePoolingPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 48, 1, 3),
    _CfprApComputePoolingPolicyRn_Type()
)
cfprApComputePoolingPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolingPolicyRn.setStatus("current")
_CfprApComputePoolingPolicyDescr_Type = SnmpAdminString
_CfprApComputePoolingPolicyDescr_Object = MibTableColumn
cfprApComputePoolingPolicyDescr = _CfprApComputePoolingPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 48, 1, 4),
    _CfprApComputePoolingPolicyDescr_Type()
)
cfprApComputePoolingPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolingPolicyDescr.setStatus("current")
_CfprApComputePoolingPolicyIntId_Type = SnmpAdminString
_CfprApComputePoolingPolicyIntId_Object = MibTableColumn
cfprApComputePoolingPolicyIntId = _CfprApComputePoolingPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 48, 1, 5),
    _CfprApComputePoolingPolicyIntId_Type()
)
cfprApComputePoolingPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolingPolicyIntId.setStatus("current")
_CfprApComputePoolingPolicyName_Type = SnmpAdminString
_CfprApComputePoolingPolicyName_Object = MibTableColumn
cfprApComputePoolingPolicyName = _CfprApComputePoolingPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 48, 1, 6),
    _CfprApComputePoolingPolicyName_Type()
)
cfprApComputePoolingPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolingPolicyName.setStatus("current")
_CfprApComputePoolingPolicyPolicyLevel_Type = Gauge32
_CfprApComputePoolingPolicyPolicyLevel_Object = MibTableColumn
cfprApComputePoolingPolicyPolicyLevel = _CfprApComputePoolingPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 48, 1, 7),
    _CfprApComputePoolingPolicyPolicyLevel_Type()
)
cfprApComputePoolingPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolingPolicyPolicyLevel.setStatus("current")
_CfprApComputePoolingPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputePoolingPolicyPolicyOwner_Object = MibTableColumn
cfprApComputePoolingPolicyPolicyOwner = _CfprApComputePoolingPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 48, 1, 8),
    _CfprApComputePoolingPolicyPolicyOwner_Type()
)
cfprApComputePoolingPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolingPolicyPolicyOwner.setStatus("current")
_CfprApComputePoolingPolicyPoolDn_Type = SnmpAdminString
_CfprApComputePoolingPolicyPoolDn_Object = MibTableColumn
cfprApComputePoolingPolicyPoolDn = _CfprApComputePoolingPolicyPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 48, 1, 9),
    _CfprApComputePoolingPolicyPoolDn_Type()
)
cfprApComputePoolingPolicyPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolingPolicyPoolDn.setStatus("current")
_CfprApComputePoolingPolicyQualifier_Type = SnmpAdminString
_CfprApComputePoolingPolicyQualifier_Object = MibTableColumn
cfprApComputePoolingPolicyQualifier = _CfprApComputePoolingPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 48, 1, 10),
    _CfprApComputePoolingPolicyQualifier_Type()
)
cfprApComputePoolingPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePoolingPolicyQualifier.setStatus("current")
_CfprApComputePsuControlTable_Object = MibTable
cfprApComputePsuControlTable = _CfprApComputePsuControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49)
)
if mibBuilder.loadTexts:
    cfprApComputePsuControlTable.setStatus("current")
_CfprApComputePsuControlEntry_Object = MibTableRow
cfprApComputePsuControlEntry = _CfprApComputePsuControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1)
)
cfprApComputePsuControlEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePsuControlInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePsuControlEntry.setStatus("current")
_CfprApComputePsuControlInstanceId_Type = CfprApManagedObjectId
_CfprApComputePsuControlInstanceId_Object = MibTableColumn
cfprApComputePsuControlInstanceId = _CfprApComputePsuControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 1),
    _CfprApComputePsuControlInstanceId_Type()
)
cfprApComputePsuControlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePsuControlInstanceId.setStatus("current")
_CfprApComputePsuControlDn_Type = CfprApManagedObjectDn
_CfprApComputePsuControlDn_Object = MibTableColumn
cfprApComputePsuControlDn = _CfprApComputePsuControlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 2),
    _CfprApComputePsuControlDn_Type()
)
cfprApComputePsuControlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlDn.setStatus("current")
_CfprApComputePsuControlRn_Type = SnmpAdminString
_CfprApComputePsuControlRn_Object = MibTableColumn
cfprApComputePsuControlRn = _CfprApComputePsuControlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 3),
    _CfprApComputePsuControlRn_Type()
)
cfprApComputePsuControlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlRn.setStatus("current")
_CfprApComputePsuControlClusterState_Type = CfprApComputePsuClusterState
_CfprApComputePsuControlClusterState_Object = MibTableColumn
cfprApComputePsuControlClusterState = _CfprApComputePsuControlClusterState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 4),
    _CfprApComputePsuControlClusterState_Type()
)
cfprApComputePsuControlClusterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlClusterState.setStatus("current")
_CfprApComputePsuControlDescr_Type = SnmpAdminString
_CfprApComputePsuControlDescr_Object = MibTableColumn
cfprApComputePsuControlDescr = _CfprApComputePsuControlDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 5),
    _CfprApComputePsuControlDescr_Type()
)
cfprApComputePsuControlDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlDescr.setStatus("current")
_CfprApComputePsuControlInputPowerState_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputePsuControlInputPowerState_Object = MibTableColumn
cfprApComputePsuControlInputPowerState = _CfprApComputePsuControlInputPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 6),
    _CfprApComputePsuControlInputPowerState_Type()
)
cfprApComputePsuControlInputPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlInputPowerState.setStatus("current")
_CfprApComputePsuControlIntId_Type = SnmpAdminString
_CfprApComputePsuControlIntId_Object = MibTableColumn
cfprApComputePsuControlIntId = _CfprApComputePsuControlIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 7),
    _CfprApComputePsuControlIntId_Type()
)
cfprApComputePsuControlIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlIntId.setStatus("current")
_CfprApComputePsuControlName_Type = SnmpAdminString
_CfprApComputePsuControlName_Object = MibTableColumn
cfprApComputePsuControlName = _CfprApComputePsuControlName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 8),
    _CfprApComputePsuControlName_Type()
)
cfprApComputePsuControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlName.setStatus("current")
_CfprApComputePsuControlOperQualifier_Type = CfprApComputePsuRedundancyOperQualifier
_CfprApComputePsuControlOperQualifier_Object = MibTableColumn
cfprApComputePsuControlOperQualifier = _CfprApComputePsuControlOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 9),
    _CfprApComputePsuControlOperQualifier_Type()
)
cfprApComputePsuControlOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlOperQualifier.setStatus("current")
_CfprApComputePsuControlOperState_Type = CfprApComputePsuRedundancyOperState
_CfprApComputePsuControlOperState_Object = MibTableColumn
cfprApComputePsuControlOperState = _CfprApComputePsuControlOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 10),
    _CfprApComputePsuControlOperState_Type()
)
cfprApComputePsuControlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlOperState.setStatus("current")
_CfprApComputePsuControlOutputPowerState_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputePsuControlOutputPowerState_Object = MibTableColumn
cfprApComputePsuControlOutputPowerState = _CfprApComputePsuControlOutputPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 11),
    _CfprApComputePsuControlOutputPowerState_Type()
)
cfprApComputePsuControlOutputPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlOutputPowerState.setStatus("current")
_CfprApComputePsuControlPolicyLevel_Type = Gauge32
_CfprApComputePsuControlPolicyLevel_Object = MibTableColumn
cfprApComputePsuControlPolicyLevel = _CfprApComputePsuControlPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 12),
    _CfprApComputePsuControlPolicyLevel_Type()
)
cfprApComputePsuControlPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlPolicyLevel.setStatus("current")
_CfprApComputePsuControlPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputePsuControlPolicyOwner_Object = MibTableColumn
cfprApComputePsuControlPolicyOwner = _CfprApComputePsuControlPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 13),
    _CfprApComputePsuControlPolicyOwner_Type()
)
cfprApComputePsuControlPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlPolicyOwner.setStatus("current")
_CfprApComputePsuControlRedundancy_Type = CfprApComputePsuControlRedundancy
_CfprApComputePsuControlRedundancy_Object = MibTableColumn
cfprApComputePsuControlRedundancy = _CfprApComputePsuControlRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 49, 1, 14),
    _CfprApComputePsuControlRedundancy_Type()
)
cfprApComputePsuControlRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuControlRedundancy.setStatus("current")
_CfprApComputePsuPolicyTable_Object = MibTable
cfprApComputePsuPolicyTable = _CfprApComputePsuPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 50)
)
if mibBuilder.loadTexts:
    cfprApComputePsuPolicyTable.setStatus("current")
_CfprApComputePsuPolicyEntry_Object = MibTableRow
cfprApComputePsuPolicyEntry = _CfprApComputePsuPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 50, 1)
)
cfprApComputePsuPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputePsuPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputePsuPolicyEntry.setStatus("current")
_CfprApComputePsuPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApComputePsuPolicyInstanceId_Object = MibTableColumn
cfprApComputePsuPolicyInstanceId = _CfprApComputePsuPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 50, 1, 1),
    _CfprApComputePsuPolicyInstanceId_Type()
)
cfprApComputePsuPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputePsuPolicyInstanceId.setStatus("current")
_CfprApComputePsuPolicyDn_Type = CfprApManagedObjectDn
_CfprApComputePsuPolicyDn_Object = MibTableColumn
cfprApComputePsuPolicyDn = _CfprApComputePsuPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 50, 1, 2),
    _CfprApComputePsuPolicyDn_Type()
)
cfprApComputePsuPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuPolicyDn.setStatus("current")
_CfprApComputePsuPolicyRn_Type = SnmpAdminString
_CfprApComputePsuPolicyRn_Object = MibTableColumn
cfprApComputePsuPolicyRn = _CfprApComputePsuPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 50, 1, 3),
    _CfprApComputePsuPolicyRn_Type()
)
cfprApComputePsuPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuPolicyRn.setStatus("current")
_CfprApComputePsuPolicyDescr_Type = SnmpAdminString
_CfprApComputePsuPolicyDescr_Object = MibTableColumn
cfprApComputePsuPolicyDescr = _CfprApComputePsuPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 50, 1, 4),
    _CfprApComputePsuPolicyDescr_Type()
)
cfprApComputePsuPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuPolicyDescr.setStatus("current")
_CfprApComputePsuPolicyIntId_Type = SnmpAdminString
_CfprApComputePsuPolicyIntId_Object = MibTableColumn
cfprApComputePsuPolicyIntId = _CfprApComputePsuPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 50, 1, 5),
    _CfprApComputePsuPolicyIntId_Type()
)
cfprApComputePsuPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuPolicyIntId.setStatus("current")
_CfprApComputePsuPolicyName_Type = SnmpAdminString
_CfprApComputePsuPolicyName_Object = MibTableColumn
cfprApComputePsuPolicyName = _CfprApComputePsuPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 50, 1, 6),
    _CfprApComputePsuPolicyName_Type()
)
cfprApComputePsuPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuPolicyName.setStatus("current")
_CfprApComputePsuPolicyPolicyLevel_Type = Gauge32
_CfprApComputePsuPolicyPolicyLevel_Object = MibTableColumn
cfprApComputePsuPolicyPolicyLevel = _CfprApComputePsuPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 50, 1, 7),
    _CfprApComputePsuPolicyPolicyLevel_Type()
)
cfprApComputePsuPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuPolicyPolicyLevel.setStatus("current")
_CfprApComputePsuPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputePsuPolicyPolicyOwner_Object = MibTableColumn
cfprApComputePsuPolicyPolicyOwner = _CfprApComputePsuPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 50, 1, 8),
    _CfprApComputePsuPolicyPolicyOwner_Type()
)
cfprApComputePsuPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuPolicyPolicyOwner.setStatus("current")
_CfprApComputePsuPolicyRedundancy_Type = CfprApComputePsuRedundancy
_CfprApComputePsuPolicyRedundancy_Object = MibTableColumn
cfprApComputePsuPolicyRedundancy = _CfprApComputePsuPolicyRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 50, 1, 9),
    _CfprApComputePsuPolicyRedundancy_Type()
)
cfprApComputePsuPolicyRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputePsuPolicyRedundancy.setStatus("current")
_CfprApComputeQualTable_Object = MibTable
cfprApComputeQualTable = _CfprApComputeQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 51)
)
if mibBuilder.loadTexts:
    cfprApComputeQualTable.setStatus("current")
_CfprApComputeQualEntry_Object = MibTableRow
cfprApComputeQualEntry = _CfprApComputeQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 51, 1)
)
cfprApComputeQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeQualEntry.setStatus("current")
_CfprApComputeQualInstanceId_Type = CfprApManagedObjectId
_CfprApComputeQualInstanceId_Object = MibTableColumn
cfprApComputeQualInstanceId = _CfprApComputeQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 51, 1, 1),
    _CfprApComputeQualInstanceId_Type()
)
cfprApComputeQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeQualInstanceId.setStatus("current")
_CfprApComputeQualDn_Type = CfprApManagedObjectDn
_CfprApComputeQualDn_Object = MibTableColumn
cfprApComputeQualDn = _CfprApComputeQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 51, 1, 2),
    _CfprApComputeQualDn_Type()
)
cfprApComputeQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeQualDn.setStatus("current")
_CfprApComputeQualRn_Type = SnmpAdminString
_CfprApComputeQualRn_Object = MibTableColumn
cfprApComputeQualRn = _CfprApComputeQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 51, 1, 3),
    _CfprApComputeQualRn_Type()
)
cfprApComputeQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeQualRn.setStatus("current")
_CfprApComputeQualDescr_Type = SnmpAdminString
_CfprApComputeQualDescr_Object = MibTableColumn
cfprApComputeQualDescr = _CfprApComputeQualDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 51, 1, 4),
    _CfprApComputeQualDescr_Type()
)
cfprApComputeQualDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeQualDescr.setStatus("current")
_CfprApComputeQualIntId_Type = SnmpAdminString
_CfprApComputeQualIntId_Object = MibTableColumn
cfprApComputeQualIntId = _CfprApComputeQualIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 51, 1, 5),
    _CfprApComputeQualIntId_Type()
)
cfprApComputeQualIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeQualIntId.setStatus("current")
_CfprApComputeQualName_Type = SnmpAdminString
_CfprApComputeQualName_Object = MibTableColumn
cfprApComputeQualName = _CfprApComputeQualName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 51, 1, 6),
    _CfprApComputeQualName_Type()
)
cfprApComputeQualName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeQualName.setStatus("current")
_CfprApComputeQualPolicyLevel_Type = Gauge32
_CfprApComputeQualPolicyLevel_Object = MibTableColumn
cfprApComputeQualPolicyLevel = _CfprApComputeQualPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 51, 1, 7),
    _CfprApComputeQualPolicyLevel_Type()
)
cfprApComputeQualPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeQualPolicyLevel.setStatus("current")
_CfprApComputeQualPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeQualPolicyOwner_Object = MibTableColumn
cfprApComputeQualPolicyOwner = _CfprApComputeQualPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 51, 1, 8),
    _CfprApComputeQualPolicyOwner_Type()
)
cfprApComputeQualPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeQualPolicyOwner.setStatus("current")
_CfprApComputeRackQualTable_Object = MibTable
cfprApComputeRackQualTable = _CfprApComputeRackQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 52)
)
if mibBuilder.loadTexts:
    cfprApComputeRackQualTable.setStatus("current")
_CfprApComputeRackQualEntry_Object = MibTableRow
cfprApComputeRackQualEntry = _CfprApComputeRackQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 52, 1)
)
cfprApComputeRackQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeRackQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeRackQualEntry.setStatus("current")
_CfprApComputeRackQualInstanceId_Type = CfprApManagedObjectId
_CfprApComputeRackQualInstanceId_Object = MibTableColumn
cfprApComputeRackQualInstanceId = _CfprApComputeRackQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 52, 1, 1),
    _CfprApComputeRackQualInstanceId_Type()
)
cfprApComputeRackQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeRackQualInstanceId.setStatus("current")
_CfprApComputeRackQualDn_Type = CfprApManagedObjectDn
_CfprApComputeRackQualDn_Object = MibTableColumn
cfprApComputeRackQualDn = _CfprApComputeRackQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 52, 1, 2),
    _CfprApComputeRackQualDn_Type()
)
cfprApComputeRackQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackQualDn.setStatus("current")
_CfprApComputeRackQualRn_Type = SnmpAdminString
_CfprApComputeRackQualRn_Object = MibTableColumn
cfprApComputeRackQualRn = _CfprApComputeRackQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 52, 1, 3),
    _CfprApComputeRackQualRn_Type()
)
cfprApComputeRackQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackQualRn.setStatus("current")
_CfprApComputeRackQualMaxId_Type = CfprApComputeRackQualMaxId
_CfprApComputeRackQualMaxId_Object = MibTableColumn
cfprApComputeRackQualMaxId = _CfprApComputeRackQualMaxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 52, 1, 4),
    _CfprApComputeRackQualMaxId_Type()
)
cfprApComputeRackQualMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackQualMaxId.setStatus("current")
_CfprApComputeRackQualMinId_Type = CfprApComputeRackQualMinId
_CfprApComputeRackQualMinId_Object = MibTableColumn
cfprApComputeRackQualMinId = _CfprApComputeRackQualMinId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 52, 1, 5),
    _CfprApComputeRackQualMinId_Type()
)
cfprApComputeRackQualMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackQualMinId.setStatus("current")
_CfprApComputeRackUnitTable_Object = MibTable
cfprApComputeRackUnitTable = _CfprApComputeRackUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53)
)
if mibBuilder.loadTexts:
    cfprApComputeRackUnitTable.setStatus("current")
_CfprApComputeRackUnitEntry_Object = MibTableRow
cfprApComputeRackUnitEntry = _CfprApComputeRackUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1)
)
cfprApComputeRackUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeRackUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeRackUnitEntry.setStatus("current")
_CfprApComputeRackUnitInstanceId_Type = CfprApManagedObjectId
_CfprApComputeRackUnitInstanceId_Object = MibTableColumn
cfprApComputeRackUnitInstanceId = _CfprApComputeRackUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 1),
    _CfprApComputeRackUnitInstanceId_Type()
)
cfprApComputeRackUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitInstanceId.setStatus("current")
_CfprApComputeRackUnitDn_Type = CfprApManagedObjectDn
_CfprApComputeRackUnitDn_Object = MibTableColumn
cfprApComputeRackUnitDn = _CfprApComputeRackUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 2),
    _CfprApComputeRackUnitDn_Type()
)
cfprApComputeRackUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitDn.setStatus("current")
_CfprApComputeRackUnitRn_Type = SnmpAdminString
_CfprApComputeRackUnitRn_Object = MibTableColumn
cfprApComputeRackUnitRn = _CfprApComputeRackUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 3),
    _CfprApComputeRackUnitRn_Type()
)
cfprApComputeRackUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitRn.setStatus("current")
_CfprApComputeRackUnitAdminPower_Type = CfprApComputeAdminPowerState
_CfprApComputeRackUnitAdminPower_Object = MibTableColumn
cfprApComputeRackUnitAdminPower = _CfprApComputeRackUnitAdminPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 4),
    _CfprApComputeRackUnitAdminPower_Type()
)
cfprApComputeRackUnitAdminPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitAdminPower.setStatus("current")
_CfprApComputeRackUnitAdminState_Type = CfprApComputeAdminState
_CfprApComputeRackUnitAdminState_Object = MibTableColumn
cfprApComputeRackUnitAdminState = _CfprApComputeRackUnitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 5),
    _CfprApComputeRackUnitAdminState_Type()
)
cfprApComputeRackUnitAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitAdminState.setStatus("current")
_CfprApComputeRackUnitAssignedToDn_Type = SnmpAdminString
_CfprApComputeRackUnitAssignedToDn_Object = MibTableColumn
cfprApComputeRackUnitAssignedToDn = _CfprApComputeRackUnitAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 6),
    _CfprApComputeRackUnitAssignedToDn_Type()
)
cfprApComputeRackUnitAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitAssignedToDn.setStatus("current")
_CfprApComputeRackUnitAssociation_Type = CfprApComputeAssociation
_CfprApComputeRackUnitAssociation_Object = MibTableColumn
cfprApComputeRackUnitAssociation = _CfprApComputeRackUnitAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 7),
    _CfprApComputeRackUnitAssociation_Type()
)
cfprApComputeRackUnitAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitAssociation.setStatus("current")
_CfprApComputeRackUnitAvailability_Type = CfprApComputeAvailability
_CfprApComputeRackUnitAvailability_Object = MibTableColumn
cfprApComputeRackUnitAvailability = _CfprApComputeRackUnitAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 8),
    _CfprApComputeRackUnitAvailability_Type()
)
cfprApComputeRackUnitAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitAvailability.setStatus("current")
_CfprApComputeRackUnitAvailableMemory_Type = Gauge32
_CfprApComputeRackUnitAvailableMemory_Object = MibTableColumn
cfprApComputeRackUnitAvailableMemory = _CfprApComputeRackUnitAvailableMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 9),
    _CfprApComputeRackUnitAvailableMemory_Type()
)
cfprApComputeRackUnitAvailableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitAvailableMemory.setStatus("current")
_CfprApComputeRackUnitCheckPoint_Type = CfprApComputeCheckPoint
_CfprApComputeRackUnitCheckPoint_Object = MibTableColumn
cfprApComputeRackUnitCheckPoint = _CfprApComputeRackUnitCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 10),
    _CfprApComputeRackUnitCheckPoint_Type()
)
cfprApComputeRackUnitCheckPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitCheckPoint.setStatus("current")
_CfprApComputeRackUnitConnPath_Type = CfprApEquipmentConnectionStatus
_CfprApComputeRackUnitConnPath_Object = MibTableColumn
cfprApComputeRackUnitConnPath = _CfprApComputeRackUnitConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 11),
    _CfprApComputeRackUnitConnPath_Type()
)
cfprApComputeRackUnitConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitConnPath.setStatus("current")
_CfprApComputeRackUnitConnStatus_Type = CfprApEquipmentConnectionStatus
_CfprApComputeRackUnitConnStatus_Object = MibTableColumn
cfprApComputeRackUnitConnStatus = _CfprApComputeRackUnitConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 12),
    _CfprApComputeRackUnitConnStatus_Type()
)
cfprApComputeRackUnitConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitConnStatus.setStatus("current")
_CfprApComputeRackUnitDescr_Type = SnmpAdminString
_CfprApComputeRackUnitDescr_Object = MibTableColumn
cfprApComputeRackUnitDescr = _CfprApComputeRackUnitDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 13),
    _CfprApComputeRackUnitDescr_Type()
)
cfprApComputeRackUnitDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitDescr.setStatus("current")
_CfprApComputeRackUnitDiscovery_Type = CfprApComputeDiscovery
_CfprApComputeRackUnitDiscovery_Object = MibTableColumn
cfprApComputeRackUnitDiscovery = _CfprApComputeRackUnitDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 14),
    _CfprApComputeRackUnitDiscovery_Type()
)
cfprApComputeRackUnitDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitDiscovery.setStatus("current")
_CfprApComputeRackUnitFltAggr_Type = Unsigned64
_CfprApComputeRackUnitFltAggr_Object = MibTableColumn
cfprApComputeRackUnitFltAggr = _CfprApComputeRackUnitFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 15),
    _CfprApComputeRackUnitFltAggr_Type()
)
cfprApComputeRackUnitFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFltAggr.setStatus("current")
_CfprApComputeRackUnitFsmDescr_Type = SnmpAdminString
_CfprApComputeRackUnitFsmDescr_Object = MibTableColumn
cfprApComputeRackUnitFsmDescr = _CfprApComputeRackUnitFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 16),
    _CfprApComputeRackUnitFsmDescr_Type()
)
cfprApComputeRackUnitFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmDescr.setStatus("current")
_CfprApComputeRackUnitFsmPrev_Type = SnmpAdminString
_CfprApComputeRackUnitFsmPrev_Object = MibTableColumn
cfprApComputeRackUnitFsmPrev = _CfprApComputeRackUnitFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 17),
    _CfprApComputeRackUnitFsmPrev_Type()
)
cfprApComputeRackUnitFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmPrev.setStatus("current")
_CfprApComputeRackUnitFsmProgr_Type = Gauge32
_CfprApComputeRackUnitFsmProgr_Object = MibTableColumn
cfprApComputeRackUnitFsmProgr = _CfprApComputeRackUnitFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 18),
    _CfprApComputeRackUnitFsmProgr_Type()
)
cfprApComputeRackUnitFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmProgr.setStatus("current")
_CfprApComputeRackUnitFsmRmtInvErrCode_Type = Gauge32
_CfprApComputeRackUnitFsmRmtInvErrCode_Object = MibTableColumn
cfprApComputeRackUnitFsmRmtInvErrCode = _CfprApComputeRackUnitFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 19),
    _CfprApComputeRackUnitFsmRmtInvErrCode_Type()
)
cfprApComputeRackUnitFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmRmtInvErrCode.setStatus("current")
_CfprApComputeRackUnitFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApComputeRackUnitFsmRmtInvErrDescr_Object = MibTableColumn
cfprApComputeRackUnitFsmRmtInvErrDescr = _CfprApComputeRackUnitFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 20),
    _CfprApComputeRackUnitFsmRmtInvErrDescr_Type()
)
cfprApComputeRackUnitFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmRmtInvErrDescr.setStatus("current")
_CfprApComputeRackUnitFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApComputeRackUnitFsmRmtInvRslt_Object = MibTableColumn
cfprApComputeRackUnitFsmRmtInvRslt = _CfprApComputeRackUnitFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 21),
    _CfprApComputeRackUnitFsmRmtInvRslt_Type()
)
cfprApComputeRackUnitFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmRmtInvRslt.setStatus("current")
_CfprApComputeRackUnitFsmStageDescr_Type = SnmpAdminString
_CfprApComputeRackUnitFsmStageDescr_Object = MibTableColumn
cfprApComputeRackUnitFsmStageDescr = _CfprApComputeRackUnitFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 22),
    _CfprApComputeRackUnitFsmStageDescr_Type()
)
cfprApComputeRackUnitFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStageDescr.setStatus("current")
_CfprApComputeRackUnitFsmStamp_Type = DateAndTime
_CfprApComputeRackUnitFsmStamp_Object = MibTableColumn
cfprApComputeRackUnitFsmStamp = _CfprApComputeRackUnitFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 23),
    _CfprApComputeRackUnitFsmStamp_Type()
)
cfprApComputeRackUnitFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStamp.setStatus("current")
_CfprApComputeRackUnitFsmStatus_Type = SnmpAdminString
_CfprApComputeRackUnitFsmStatus_Object = MibTableColumn
cfprApComputeRackUnitFsmStatus = _CfprApComputeRackUnitFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 24),
    _CfprApComputeRackUnitFsmStatus_Type()
)
cfprApComputeRackUnitFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStatus.setStatus("current")
_CfprApComputeRackUnitFsmTry_Type = Gauge32
_CfprApComputeRackUnitFsmTry_Object = MibTableColumn
cfprApComputeRackUnitFsmTry = _CfprApComputeRackUnitFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 25),
    _CfprApComputeRackUnitFsmTry_Type()
)
cfprApComputeRackUnitFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmTry.setStatus("current")
_CfprApComputeRackUnitId_Type = CfprApComputeRackUnitId
_CfprApComputeRackUnitId_Object = MibTableColumn
cfprApComputeRackUnitId = _CfprApComputeRackUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 26),
    _CfprApComputeRackUnitId_Type()
)
cfprApComputeRackUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitId.setStatus("current")
_CfprApComputeRackUnitIntId_Type = SnmpAdminString
_CfprApComputeRackUnitIntId_Object = MibTableColumn
cfprApComputeRackUnitIntId = _CfprApComputeRackUnitIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 27),
    _CfprApComputeRackUnitIntId_Type()
)
cfprApComputeRackUnitIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitIntId.setStatus("current")
_CfprApComputeRackUnitLc_Type = CfprApComputeAdminTrigger
_CfprApComputeRackUnitLc_Object = MibTableColumn
cfprApComputeRackUnitLc = _CfprApComputeRackUnitLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 28),
    _CfprApComputeRackUnitLc_Type()
)
cfprApComputeRackUnitLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitLc.setStatus("current")
_CfprApComputeRackUnitLcTs_Type = DateAndTime
_CfprApComputeRackUnitLcTs_Object = MibTableColumn
cfprApComputeRackUnitLcTs = _CfprApComputeRackUnitLcTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 29),
    _CfprApComputeRackUnitLcTs_Type()
)
cfprApComputeRackUnitLcTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitLcTs.setStatus("current")
_CfprApComputeRackUnitLocalId_Type = SnmpAdminString
_CfprApComputeRackUnitLocalId_Object = MibTableColumn
cfprApComputeRackUnitLocalId = _CfprApComputeRackUnitLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 30),
    _CfprApComputeRackUnitLocalId_Type()
)
cfprApComputeRackUnitLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitLocalId.setStatus("current")
_CfprApComputeRackUnitLowVoltageMemory_Type = CfprApComputePhysicalLowVoltageMemory
_CfprApComputeRackUnitLowVoltageMemory_Object = MibTableColumn
cfprApComputeRackUnitLowVoltageMemory = _CfprApComputeRackUnitLowVoltageMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 31),
    _CfprApComputeRackUnitLowVoltageMemory_Type()
)
cfprApComputeRackUnitLowVoltageMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitLowVoltageMemory.setStatus("current")
_CfprApComputeRackUnitManagingInst_Type = CfprApNetworkSwitchId
_CfprApComputeRackUnitManagingInst_Object = MibTableColumn
cfprApComputeRackUnitManagingInst = _CfprApComputeRackUnitManagingInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 32),
    _CfprApComputeRackUnitManagingInst_Type()
)
cfprApComputeRackUnitManagingInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitManagingInst.setStatus("current")
_CfprApComputeRackUnitMemorySpeed_Type = Gauge32
_CfprApComputeRackUnitMemorySpeed_Object = MibTableColumn
cfprApComputeRackUnitMemorySpeed = _CfprApComputeRackUnitMemorySpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 33),
    _CfprApComputeRackUnitMemorySpeed_Type()
)
cfprApComputeRackUnitMemorySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMemorySpeed.setStatus("current")
_CfprApComputeRackUnitMfgTime_Type = DateAndTime
_CfprApComputeRackUnitMfgTime_Object = MibTableColumn
cfprApComputeRackUnitMfgTime = _CfprApComputeRackUnitMfgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 34),
    _CfprApComputeRackUnitMfgTime_Type()
)
cfprApComputeRackUnitMfgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMfgTime.setStatus("current")
_CfprApComputeRackUnitModel_Type = SnmpAdminString
_CfprApComputeRackUnitModel_Object = MibTableColumn
cfprApComputeRackUnitModel = _CfprApComputeRackUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 35),
    _CfprApComputeRackUnitModel_Type()
)
cfprApComputeRackUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitModel.setStatus("current")
_CfprApComputeRackUnitName_Type = SnmpAdminString
_CfprApComputeRackUnitName_Object = MibTableColumn
cfprApComputeRackUnitName = _CfprApComputeRackUnitName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 36),
    _CfprApComputeRackUnitName_Type()
)
cfprApComputeRackUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitName.setStatus("current")
_CfprApComputeRackUnitNumOfAdaptors_Type = Gauge32
_CfprApComputeRackUnitNumOfAdaptors_Object = MibTableColumn
cfprApComputeRackUnitNumOfAdaptors = _CfprApComputeRackUnitNumOfAdaptors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 37),
    _CfprApComputeRackUnitNumOfAdaptors_Type()
)
cfprApComputeRackUnitNumOfAdaptors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitNumOfAdaptors.setStatus("current")
_CfprApComputeRackUnitNumOfCores_Type = Gauge32
_CfprApComputeRackUnitNumOfCores_Object = MibTableColumn
cfprApComputeRackUnitNumOfCores = _CfprApComputeRackUnitNumOfCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 38),
    _CfprApComputeRackUnitNumOfCores_Type()
)
cfprApComputeRackUnitNumOfCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitNumOfCores.setStatus("current")
_CfprApComputeRackUnitNumOfCoresEnabled_Type = Gauge32
_CfprApComputeRackUnitNumOfCoresEnabled_Object = MibTableColumn
cfprApComputeRackUnitNumOfCoresEnabled = _CfprApComputeRackUnitNumOfCoresEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 39),
    _CfprApComputeRackUnitNumOfCoresEnabled_Type()
)
cfprApComputeRackUnitNumOfCoresEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitNumOfCoresEnabled.setStatus("current")
_CfprApComputeRackUnitNumOfCpus_Type = Gauge32
_CfprApComputeRackUnitNumOfCpus_Object = MibTableColumn
cfprApComputeRackUnitNumOfCpus = _CfprApComputeRackUnitNumOfCpus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 40),
    _CfprApComputeRackUnitNumOfCpus_Type()
)
cfprApComputeRackUnitNumOfCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitNumOfCpus.setStatus("current")
_CfprApComputeRackUnitNumOfEthHostIfs_Type = Gauge32
_CfprApComputeRackUnitNumOfEthHostIfs_Object = MibTableColumn
cfprApComputeRackUnitNumOfEthHostIfs = _CfprApComputeRackUnitNumOfEthHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 41),
    _CfprApComputeRackUnitNumOfEthHostIfs_Type()
)
cfprApComputeRackUnitNumOfEthHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitNumOfEthHostIfs.setStatus("current")
_CfprApComputeRackUnitNumOfFcHostIfs_Type = Gauge32
_CfprApComputeRackUnitNumOfFcHostIfs_Object = MibTableColumn
cfprApComputeRackUnitNumOfFcHostIfs = _CfprApComputeRackUnitNumOfFcHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 42),
    _CfprApComputeRackUnitNumOfFcHostIfs_Type()
)
cfprApComputeRackUnitNumOfFcHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitNumOfFcHostIfs.setStatus("current")
_CfprApComputeRackUnitNumOfThreads_Type = Gauge32
_CfprApComputeRackUnitNumOfThreads_Object = MibTableColumn
cfprApComputeRackUnitNumOfThreads = _CfprApComputeRackUnitNumOfThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 43),
    _CfprApComputeRackUnitNumOfThreads_Type()
)
cfprApComputeRackUnitNumOfThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitNumOfThreads.setStatus("current")
_CfprApComputeRackUnitOperPower_Type = CfprApEquipmentPowerState
_CfprApComputeRackUnitOperPower_Object = MibTableColumn
cfprApComputeRackUnitOperPower = _CfprApComputeRackUnitOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 44),
    _CfprApComputeRackUnitOperPower_Type()
)
cfprApComputeRackUnitOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitOperPower.setStatus("current")
_CfprApComputeRackUnitOperQualifier_Type = CfprApComputeIssues
_CfprApComputeRackUnitOperQualifier_Object = MibTableColumn
cfprApComputeRackUnitOperQualifier = _CfprApComputeRackUnitOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 45),
    _CfprApComputeRackUnitOperQualifier_Type()
)
cfprApComputeRackUnitOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitOperQualifier.setStatus("current")
_CfprApComputeRackUnitOperState_Type = CfprApLsOperState
_CfprApComputeRackUnitOperState_Object = MibTableColumn
cfprApComputeRackUnitOperState = _CfprApComputeRackUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 46),
    _CfprApComputeRackUnitOperState_Type()
)
cfprApComputeRackUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitOperState.setStatus("current")
_CfprApComputeRackUnitOperability_Type = CfprApEquipmentOperability
_CfprApComputeRackUnitOperability_Object = MibTableColumn
cfprApComputeRackUnitOperability = _CfprApComputeRackUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 47),
    _CfprApComputeRackUnitOperability_Type()
)
cfprApComputeRackUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitOperability.setStatus("current")
_CfprApComputeRackUnitOriginalUuid_Type = SnmpAdminString
_CfprApComputeRackUnitOriginalUuid_Object = MibTableColumn
cfprApComputeRackUnitOriginalUuid = _CfprApComputeRackUnitOriginalUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 48),
    _CfprApComputeRackUnitOriginalUuid_Type()
)
cfprApComputeRackUnitOriginalUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitOriginalUuid.setStatus("current")
_CfprApComputeRackUnitPartNumber_Type = SnmpAdminString
_CfprApComputeRackUnitPartNumber_Object = MibTableColumn
cfprApComputeRackUnitPartNumber = _CfprApComputeRackUnitPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 49),
    _CfprApComputeRackUnitPartNumber_Type()
)
cfprApComputeRackUnitPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitPartNumber.setStatus("current")
_CfprApComputeRackUnitPolicyLevel_Type = Gauge32
_CfprApComputeRackUnitPolicyLevel_Object = MibTableColumn
cfprApComputeRackUnitPolicyLevel = _CfprApComputeRackUnitPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 50),
    _CfprApComputeRackUnitPolicyLevel_Type()
)
cfprApComputeRackUnitPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitPolicyLevel.setStatus("current")
_CfprApComputeRackUnitPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeRackUnitPolicyOwner_Object = MibTableColumn
cfprApComputeRackUnitPolicyOwner = _CfprApComputeRackUnitPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 51),
    _CfprApComputeRackUnitPolicyOwner_Type()
)
cfprApComputeRackUnitPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitPolicyOwner.setStatus("current")
_CfprApComputeRackUnitPresence_Type = CfprApEquipmentSlotStatus
_CfprApComputeRackUnitPresence_Object = MibTableColumn
cfprApComputeRackUnitPresence = _CfprApComputeRackUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 52),
    _CfprApComputeRackUnitPresence_Type()
)
cfprApComputeRackUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitPresence.setStatus("current")
_CfprApComputeRackUnitRevision_Type = SnmpAdminString
_CfprApComputeRackUnitRevision_Object = MibTableColumn
cfprApComputeRackUnitRevision = _CfprApComputeRackUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 53),
    _CfprApComputeRackUnitRevision_Type()
)
cfprApComputeRackUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitRevision.setStatus("current")
_CfprApComputeRackUnitSerial_Type = SnmpAdminString
_CfprApComputeRackUnitSerial_Object = MibTableColumn
cfprApComputeRackUnitSerial = _CfprApComputeRackUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 54),
    _CfprApComputeRackUnitSerial_Type()
)
cfprApComputeRackUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitSerial.setStatus("current")
_CfprApComputeRackUnitServerId_Type = SnmpAdminString
_CfprApComputeRackUnitServerId_Object = MibTableColumn
cfprApComputeRackUnitServerId = _CfprApComputeRackUnitServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 55),
    _CfprApComputeRackUnitServerId_Type()
)
cfprApComputeRackUnitServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitServerId.setStatus("current")
_CfprApComputeRackUnitTotalMemory_Type = Gauge32
_CfprApComputeRackUnitTotalMemory_Object = MibTableColumn
cfprApComputeRackUnitTotalMemory = _CfprApComputeRackUnitTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 56),
    _CfprApComputeRackUnitTotalMemory_Type()
)
cfprApComputeRackUnitTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitTotalMemory.setStatus("current")
_CfprApComputeRackUnitUsrLbl_Type = SnmpAdminString
_CfprApComputeRackUnitUsrLbl_Object = MibTableColumn
cfprApComputeRackUnitUsrLbl = _CfprApComputeRackUnitUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 57),
    _CfprApComputeRackUnitUsrLbl_Type()
)
cfprApComputeRackUnitUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitUsrLbl.setStatus("current")
_CfprApComputeRackUnitUuid_Type = SnmpAdminString
_CfprApComputeRackUnitUuid_Object = MibTableColumn
cfprApComputeRackUnitUuid = _CfprApComputeRackUnitUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 58),
    _CfprApComputeRackUnitUuid_Type()
)
cfprApComputeRackUnitUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitUuid.setStatus("current")
_CfprApComputeRackUnitVendor_Type = SnmpAdminString
_CfprApComputeRackUnitVendor_Object = MibTableColumn
cfprApComputeRackUnitVendor = _CfprApComputeRackUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 59),
    _CfprApComputeRackUnitVendor_Type()
)
cfprApComputeRackUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitVendor.setStatus("current")
_CfprApComputeRackUnitVersionHolder_Type = TruthValue
_CfprApComputeRackUnitVersionHolder_Object = MibTableColumn
cfprApComputeRackUnitVersionHolder = _CfprApComputeRackUnitVersionHolder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 60),
    _CfprApComputeRackUnitVersionHolder_Type()
)
cfprApComputeRackUnitVersionHolder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitVersionHolder.setStatus("current")
_CfprApComputeRackUnitVid_Type = SnmpAdminString
_CfprApComputeRackUnitVid_Object = MibTableColumn
cfprApComputeRackUnitVid = _CfprApComputeRackUnitVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 53, 1, 61),
    _CfprApComputeRackUnitVid_Type()
)
cfprApComputeRackUnitVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitVid.setStatus("current")
_CfprApComputeRackUnitFsmTable_Object = MibTable
cfprApComputeRackUnitFsmTable = _CfprApComputeRackUnitFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54)
)
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmTable.setStatus("current")
_CfprApComputeRackUnitFsmEntry_Object = MibTableRow
cfprApComputeRackUnitFsmEntry = _CfprApComputeRackUnitFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54, 1)
)
cfprApComputeRackUnitFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeRackUnitFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmEntry.setStatus("current")
_CfprApComputeRackUnitFsmInstanceId_Type = CfprApManagedObjectId
_CfprApComputeRackUnitFsmInstanceId_Object = MibTableColumn
cfprApComputeRackUnitFsmInstanceId = _CfprApComputeRackUnitFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54, 1, 1),
    _CfprApComputeRackUnitFsmInstanceId_Type()
)
cfprApComputeRackUnitFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmInstanceId.setStatus("current")
_CfprApComputeRackUnitFsmDn_Type = CfprApManagedObjectDn
_CfprApComputeRackUnitFsmDn_Object = MibTableColumn
cfprApComputeRackUnitFsmDn = _CfprApComputeRackUnitFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54, 1, 2),
    _CfprApComputeRackUnitFsmDn_Type()
)
cfprApComputeRackUnitFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmDn.setStatus("current")
_CfprApComputeRackUnitFsmRn_Type = SnmpAdminString
_CfprApComputeRackUnitFsmRn_Object = MibTableColumn
cfprApComputeRackUnitFsmRn = _CfprApComputeRackUnitFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54, 1, 3),
    _CfprApComputeRackUnitFsmRn_Type()
)
cfprApComputeRackUnitFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmRn.setStatus("current")
_CfprApComputeRackUnitFsmCompletionTime_Type = DateAndTime
_CfprApComputeRackUnitFsmCompletionTime_Object = MibTableColumn
cfprApComputeRackUnitFsmCompletionTime = _CfprApComputeRackUnitFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54, 1, 4),
    _CfprApComputeRackUnitFsmCompletionTime_Type()
)
cfprApComputeRackUnitFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmCompletionTime.setStatus("current")
_CfprApComputeRackUnitFsmCurrentFsm_Type = CfprApComputeRackUnitFsmCurrentFsm
_CfprApComputeRackUnitFsmCurrentFsm_Object = MibTableColumn
cfprApComputeRackUnitFsmCurrentFsm = _CfprApComputeRackUnitFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54, 1, 5),
    _CfprApComputeRackUnitFsmCurrentFsm_Type()
)
cfprApComputeRackUnitFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmCurrentFsm.setStatus("current")
_CfprApComputeRackUnitFsmDescrData_Type = SnmpAdminString
_CfprApComputeRackUnitFsmDescrData_Object = MibTableColumn
cfprApComputeRackUnitFsmDescrData = _CfprApComputeRackUnitFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54, 1, 6),
    _CfprApComputeRackUnitFsmDescrData_Type()
)
cfprApComputeRackUnitFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmDescrData.setStatus("current")
_CfprApComputeRackUnitFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApComputeRackUnitFsmFsmStatus_Object = MibTableColumn
cfprApComputeRackUnitFsmFsmStatus = _CfprApComputeRackUnitFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54, 1, 7),
    _CfprApComputeRackUnitFsmFsmStatus_Type()
)
cfprApComputeRackUnitFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmFsmStatus.setStatus("current")
_CfprApComputeRackUnitFsmProgress_Type = Gauge32
_CfprApComputeRackUnitFsmProgress_Object = MibTableColumn
cfprApComputeRackUnitFsmProgress = _CfprApComputeRackUnitFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54, 1, 8),
    _CfprApComputeRackUnitFsmProgress_Type()
)
cfprApComputeRackUnitFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmProgress.setStatus("current")
_CfprApComputeRackUnitFsmRmtErrCode_Type = Gauge32
_CfprApComputeRackUnitFsmRmtErrCode_Object = MibTableColumn
cfprApComputeRackUnitFsmRmtErrCode = _CfprApComputeRackUnitFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54, 1, 9),
    _CfprApComputeRackUnitFsmRmtErrCode_Type()
)
cfprApComputeRackUnitFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmRmtErrCode.setStatus("current")
_CfprApComputeRackUnitFsmRmtErrDescr_Type = SnmpAdminString
_CfprApComputeRackUnitFsmRmtErrDescr_Object = MibTableColumn
cfprApComputeRackUnitFsmRmtErrDescr = _CfprApComputeRackUnitFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54, 1, 10),
    _CfprApComputeRackUnitFsmRmtErrDescr_Type()
)
cfprApComputeRackUnitFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmRmtErrDescr.setStatus("current")
_CfprApComputeRackUnitFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApComputeRackUnitFsmRmtRslt_Object = MibTableColumn
cfprApComputeRackUnitFsmRmtRslt = _CfprApComputeRackUnitFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 54, 1, 11),
    _CfprApComputeRackUnitFsmRmtRslt_Type()
)
cfprApComputeRackUnitFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmRmtRslt.setStatus("current")
_CfprApComputeRackUnitFsmStageTable_Object = MibTable
cfprApComputeRackUnitFsmStageTable = _CfprApComputeRackUnitFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 55)
)
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStageTable.setStatus("current")
_CfprApComputeRackUnitFsmStageEntry_Object = MibTableRow
cfprApComputeRackUnitFsmStageEntry = _CfprApComputeRackUnitFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 55, 1)
)
cfprApComputeRackUnitFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeRackUnitFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStageEntry.setStatus("current")
_CfprApComputeRackUnitFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApComputeRackUnitFsmStageInstanceId_Object = MibTableColumn
cfprApComputeRackUnitFsmStageInstanceId = _CfprApComputeRackUnitFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 55, 1, 1),
    _CfprApComputeRackUnitFsmStageInstanceId_Type()
)
cfprApComputeRackUnitFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStageInstanceId.setStatus("current")
_CfprApComputeRackUnitFsmStageDn_Type = CfprApManagedObjectDn
_CfprApComputeRackUnitFsmStageDn_Object = MibTableColumn
cfprApComputeRackUnitFsmStageDn = _CfprApComputeRackUnitFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 55, 1, 2),
    _CfprApComputeRackUnitFsmStageDn_Type()
)
cfprApComputeRackUnitFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStageDn.setStatus("current")
_CfprApComputeRackUnitFsmStageRn_Type = SnmpAdminString
_CfprApComputeRackUnitFsmStageRn_Object = MibTableColumn
cfprApComputeRackUnitFsmStageRn = _CfprApComputeRackUnitFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 55, 1, 3),
    _CfprApComputeRackUnitFsmStageRn_Type()
)
cfprApComputeRackUnitFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStageRn.setStatus("current")
_CfprApComputeRackUnitFsmStageDescrData_Type = SnmpAdminString
_CfprApComputeRackUnitFsmStageDescrData_Object = MibTableColumn
cfprApComputeRackUnitFsmStageDescrData = _CfprApComputeRackUnitFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 55, 1, 4),
    _CfprApComputeRackUnitFsmStageDescrData_Type()
)
cfprApComputeRackUnitFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStageDescrData.setStatus("current")
_CfprApComputeRackUnitFsmStageLastUpdateTime_Type = DateAndTime
_CfprApComputeRackUnitFsmStageLastUpdateTime_Object = MibTableColumn
cfprApComputeRackUnitFsmStageLastUpdateTime = _CfprApComputeRackUnitFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 55, 1, 5),
    _CfprApComputeRackUnitFsmStageLastUpdateTime_Type()
)
cfprApComputeRackUnitFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStageLastUpdateTime.setStatus("current")
_CfprApComputeRackUnitFsmStageName_Type = CfprApComputeRackUnitFsmStageName
_CfprApComputeRackUnitFsmStageName_Object = MibTableColumn
cfprApComputeRackUnitFsmStageName = _CfprApComputeRackUnitFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 55, 1, 6),
    _CfprApComputeRackUnitFsmStageName_Type()
)
cfprApComputeRackUnitFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStageName.setStatus("current")
_CfprApComputeRackUnitFsmStageOrder_Type = Gauge32
_CfprApComputeRackUnitFsmStageOrder_Object = MibTableColumn
cfprApComputeRackUnitFsmStageOrder = _CfprApComputeRackUnitFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 55, 1, 7),
    _CfprApComputeRackUnitFsmStageOrder_Type()
)
cfprApComputeRackUnitFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStageOrder.setStatus("current")
_CfprApComputeRackUnitFsmStageRetry_Type = Gauge32
_CfprApComputeRackUnitFsmStageRetry_Object = MibTableColumn
cfprApComputeRackUnitFsmStageRetry = _CfprApComputeRackUnitFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 55, 1, 8),
    _CfprApComputeRackUnitFsmStageRetry_Type()
)
cfprApComputeRackUnitFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStageRetry.setStatus("current")
_CfprApComputeRackUnitFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApComputeRackUnitFsmStageStageStatus_Object = MibTableColumn
cfprApComputeRackUnitFsmStageStageStatus = _CfprApComputeRackUnitFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 55, 1, 9),
    _CfprApComputeRackUnitFsmStageStageStatus_Type()
)
cfprApComputeRackUnitFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitFsmStageStageStatus.setStatus("current")
_CfprApComputeRackUnitMbTempStatsTable_Object = MibTable
cfprApComputeRackUnitMbTempStatsTable = _CfprApComputeRackUnitMbTempStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56)
)
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsTable.setStatus("current")
_CfprApComputeRackUnitMbTempStatsEntry_Object = MibTableRow
cfprApComputeRackUnitMbTempStatsEntry = _CfprApComputeRackUnitMbTempStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1)
)
cfprApComputeRackUnitMbTempStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeRackUnitMbTempStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsEntry.setStatus("current")
_CfprApComputeRackUnitMbTempStatsInstanceId_Type = CfprApManagedObjectId
_CfprApComputeRackUnitMbTempStatsInstanceId_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsInstanceId = _CfprApComputeRackUnitMbTempStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 1),
    _CfprApComputeRackUnitMbTempStatsInstanceId_Type()
)
cfprApComputeRackUnitMbTempStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsInstanceId.setStatus("current")
_CfprApComputeRackUnitMbTempStatsDn_Type = CfprApManagedObjectDn
_CfprApComputeRackUnitMbTempStatsDn_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsDn = _CfprApComputeRackUnitMbTempStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 2),
    _CfprApComputeRackUnitMbTempStatsDn_Type()
)
cfprApComputeRackUnitMbTempStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsDn.setStatus("current")
_CfprApComputeRackUnitMbTempStatsRn_Type = SnmpAdminString
_CfprApComputeRackUnitMbTempStatsRn_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsRn = _CfprApComputeRackUnitMbTempStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 3),
    _CfprApComputeRackUnitMbTempStatsRn_Type()
)
cfprApComputeRackUnitMbTempStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsRn.setStatus("current")
_CfprApComputeRackUnitMbTempStatsAmbientTemp_Type = Integer32
_CfprApComputeRackUnitMbTempStatsAmbientTemp_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsAmbientTemp = _CfprApComputeRackUnitMbTempStatsAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 4),
    _CfprApComputeRackUnitMbTempStatsAmbientTemp_Type()
)
cfprApComputeRackUnitMbTempStatsAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsAmbientTemp.setStatus("current")
_CfprApComputeRackUnitMbTempStatsAmbientTempAvg_Type = Integer32
_CfprApComputeRackUnitMbTempStatsAmbientTempAvg_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsAmbientTempAvg = _CfprApComputeRackUnitMbTempStatsAmbientTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 5),
    _CfprApComputeRackUnitMbTempStatsAmbientTempAvg_Type()
)
cfprApComputeRackUnitMbTempStatsAmbientTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsAmbientTempAvg.setStatus("current")
_CfprApComputeRackUnitMbTempStatsAmbientTempMax_Type = Integer32
_CfprApComputeRackUnitMbTempStatsAmbientTempMax_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsAmbientTempMax = _CfprApComputeRackUnitMbTempStatsAmbientTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 6),
    _CfprApComputeRackUnitMbTempStatsAmbientTempMax_Type()
)
cfprApComputeRackUnitMbTempStatsAmbientTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsAmbientTempMax.setStatus("current")
_CfprApComputeRackUnitMbTempStatsAmbientTempMin_Type = Integer32
_CfprApComputeRackUnitMbTempStatsAmbientTempMin_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsAmbientTempMin = _CfprApComputeRackUnitMbTempStatsAmbientTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 7),
    _CfprApComputeRackUnitMbTempStatsAmbientTempMin_Type()
)
cfprApComputeRackUnitMbTempStatsAmbientTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsAmbientTempMin.setStatus("current")
_CfprApComputeRackUnitMbTempStatsFrontTemp_Type = Integer32
_CfprApComputeRackUnitMbTempStatsFrontTemp_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsFrontTemp = _CfprApComputeRackUnitMbTempStatsFrontTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 8),
    _CfprApComputeRackUnitMbTempStatsFrontTemp_Type()
)
cfprApComputeRackUnitMbTempStatsFrontTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsFrontTemp.setStatus("current")
_CfprApComputeRackUnitMbTempStatsFrontTempAvg_Type = Integer32
_CfprApComputeRackUnitMbTempStatsFrontTempAvg_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsFrontTempAvg = _CfprApComputeRackUnitMbTempStatsFrontTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 9),
    _CfprApComputeRackUnitMbTempStatsFrontTempAvg_Type()
)
cfprApComputeRackUnitMbTempStatsFrontTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsFrontTempAvg.setStatus("current")
_CfprApComputeRackUnitMbTempStatsFrontTempMax_Type = Integer32
_CfprApComputeRackUnitMbTempStatsFrontTempMax_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsFrontTempMax = _CfprApComputeRackUnitMbTempStatsFrontTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 10),
    _CfprApComputeRackUnitMbTempStatsFrontTempMax_Type()
)
cfprApComputeRackUnitMbTempStatsFrontTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsFrontTempMax.setStatus("current")
_CfprApComputeRackUnitMbTempStatsFrontTempMin_Type = Integer32
_CfprApComputeRackUnitMbTempStatsFrontTempMin_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsFrontTempMin = _CfprApComputeRackUnitMbTempStatsFrontTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 11),
    _CfprApComputeRackUnitMbTempStatsFrontTempMin_Type()
)
cfprApComputeRackUnitMbTempStatsFrontTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsFrontTempMin.setStatus("current")
_CfprApComputeRackUnitMbTempStatsIntervals_Type = Gauge32
_CfprApComputeRackUnitMbTempStatsIntervals_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsIntervals = _CfprApComputeRackUnitMbTempStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 12),
    _CfprApComputeRackUnitMbTempStatsIntervals_Type()
)
cfprApComputeRackUnitMbTempStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsIntervals.setStatus("current")
_CfprApComputeRackUnitMbTempStatsIoh1Temp_Type = Integer32
_CfprApComputeRackUnitMbTempStatsIoh1Temp_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsIoh1Temp = _CfprApComputeRackUnitMbTempStatsIoh1Temp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 13),
    _CfprApComputeRackUnitMbTempStatsIoh1Temp_Type()
)
cfprApComputeRackUnitMbTempStatsIoh1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsIoh1Temp.setStatus("current")
_CfprApComputeRackUnitMbTempStatsIoh1TempAvg_Type = Integer32
_CfprApComputeRackUnitMbTempStatsIoh1TempAvg_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsIoh1TempAvg = _CfprApComputeRackUnitMbTempStatsIoh1TempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 14),
    _CfprApComputeRackUnitMbTempStatsIoh1TempAvg_Type()
)
cfprApComputeRackUnitMbTempStatsIoh1TempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsIoh1TempAvg.setStatus("current")
_CfprApComputeRackUnitMbTempStatsIoh1TempMax_Type = Integer32
_CfprApComputeRackUnitMbTempStatsIoh1TempMax_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsIoh1TempMax = _CfprApComputeRackUnitMbTempStatsIoh1TempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 15),
    _CfprApComputeRackUnitMbTempStatsIoh1TempMax_Type()
)
cfprApComputeRackUnitMbTempStatsIoh1TempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsIoh1TempMax.setStatus("current")
_CfprApComputeRackUnitMbTempStatsIoh1TempMin_Type = Integer32
_CfprApComputeRackUnitMbTempStatsIoh1TempMin_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsIoh1TempMin = _CfprApComputeRackUnitMbTempStatsIoh1TempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 16),
    _CfprApComputeRackUnitMbTempStatsIoh1TempMin_Type()
)
cfprApComputeRackUnitMbTempStatsIoh1TempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsIoh1TempMin.setStatus("current")
_CfprApComputeRackUnitMbTempStatsIoh2Temp_Type = Integer32
_CfprApComputeRackUnitMbTempStatsIoh2Temp_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsIoh2Temp = _CfprApComputeRackUnitMbTempStatsIoh2Temp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 17),
    _CfprApComputeRackUnitMbTempStatsIoh2Temp_Type()
)
cfprApComputeRackUnitMbTempStatsIoh2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsIoh2Temp.setStatus("current")
_CfprApComputeRackUnitMbTempStatsIoh2TempAvg_Type = Integer32
_CfprApComputeRackUnitMbTempStatsIoh2TempAvg_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsIoh2TempAvg = _CfprApComputeRackUnitMbTempStatsIoh2TempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 18),
    _CfprApComputeRackUnitMbTempStatsIoh2TempAvg_Type()
)
cfprApComputeRackUnitMbTempStatsIoh2TempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsIoh2TempAvg.setStatus("current")
_CfprApComputeRackUnitMbTempStatsIoh2TempMax_Type = Integer32
_CfprApComputeRackUnitMbTempStatsIoh2TempMax_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsIoh2TempMax = _CfprApComputeRackUnitMbTempStatsIoh2TempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 19),
    _CfprApComputeRackUnitMbTempStatsIoh2TempMax_Type()
)
cfprApComputeRackUnitMbTempStatsIoh2TempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsIoh2TempMax.setStatus("current")
_CfprApComputeRackUnitMbTempStatsIoh2TempMin_Type = Integer32
_CfprApComputeRackUnitMbTempStatsIoh2TempMin_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsIoh2TempMin = _CfprApComputeRackUnitMbTempStatsIoh2TempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 20),
    _CfprApComputeRackUnitMbTempStatsIoh2TempMin_Type()
)
cfprApComputeRackUnitMbTempStatsIoh2TempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsIoh2TempMin.setStatus("current")
_CfprApComputeRackUnitMbTempStatsRearTemp_Type = Integer32
_CfprApComputeRackUnitMbTempStatsRearTemp_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsRearTemp = _CfprApComputeRackUnitMbTempStatsRearTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 21),
    _CfprApComputeRackUnitMbTempStatsRearTemp_Type()
)
cfprApComputeRackUnitMbTempStatsRearTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsRearTemp.setStatus("current")
_CfprApComputeRackUnitMbTempStatsRearTempAvg_Type = Integer32
_CfprApComputeRackUnitMbTempStatsRearTempAvg_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsRearTempAvg = _CfprApComputeRackUnitMbTempStatsRearTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 22),
    _CfprApComputeRackUnitMbTempStatsRearTempAvg_Type()
)
cfprApComputeRackUnitMbTempStatsRearTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsRearTempAvg.setStatus("current")
_CfprApComputeRackUnitMbTempStatsRearTempMax_Type = Integer32
_CfprApComputeRackUnitMbTempStatsRearTempMax_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsRearTempMax = _CfprApComputeRackUnitMbTempStatsRearTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 23),
    _CfprApComputeRackUnitMbTempStatsRearTempMax_Type()
)
cfprApComputeRackUnitMbTempStatsRearTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsRearTempMax.setStatus("current")
_CfprApComputeRackUnitMbTempStatsRearTempMin_Type = Integer32
_CfprApComputeRackUnitMbTempStatsRearTempMin_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsRearTempMin = _CfprApComputeRackUnitMbTempStatsRearTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 24),
    _CfprApComputeRackUnitMbTempStatsRearTempMin_Type()
)
cfprApComputeRackUnitMbTempStatsRearTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsRearTempMin.setStatus("current")
_CfprApComputeRackUnitMbTempStatsSuspect_Type = TruthValue
_CfprApComputeRackUnitMbTempStatsSuspect_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsSuspect = _CfprApComputeRackUnitMbTempStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 25),
    _CfprApComputeRackUnitMbTempStatsSuspect_Type()
)
cfprApComputeRackUnitMbTempStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsSuspect.setStatus("current")
_CfprApComputeRackUnitMbTempStatsThresholded_Type = CfprApComputeRackUnitMbTempStatsThresholded
_CfprApComputeRackUnitMbTempStatsThresholded_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsThresholded = _CfprApComputeRackUnitMbTempStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 26),
    _CfprApComputeRackUnitMbTempStatsThresholded_Type()
)
cfprApComputeRackUnitMbTempStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsThresholded.setStatus("current")
_CfprApComputeRackUnitMbTempStatsTimeCollected_Type = DateAndTime
_CfprApComputeRackUnitMbTempStatsTimeCollected_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsTimeCollected = _CfprApComputeRackUnitMbTempStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 27),
    _CfprApComputeRackUnitMbTempStatsTimeCollected_Type()
)
cfprApComputeRackUnitMbTempStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsTimeCollected.setStatus("current")
_CfprApComputeRackUnitMbTempStatsUpdate_Type = Gauge32
_CfprApComputeRackUnitMbTempStatsUpdate_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsUpdate = _CfprApComputeRackUnitMbTempStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 56, 1, 28),
    _CfprApComputeRackUnitMbTempStatsUpdate_Type()
)
cfprApComputeRackUnitMbTempStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsUpdate.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistTable_Object = MibTable
cfprApComputeRackUnitMbTempStatsHistTable = _CfprApComputeRackUnitMbTempStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57)
)
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistTable.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistEntry_Object = MibTableRow
cfprApComputeRackUnitMbTempStatsHistEntry = _CfprApComputeRackUnitMbTempStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1)
)
cfprApComputeRackUnitMbTempStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeRackUnitMbTempStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistEntry.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApComputeRackUnitMbTempStatsHistInstanceId_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistInstanceId = _CfprApComputeRackUnitMbTempStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 1),
    _CfprApComputeRackUnitMbTempStatsHistInstanceId_Type()
)
cfprApComputeRackUnitMbTempStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistInstanceId.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistDn_Type = CfprApManagedObjectDn
_CfprApComputeRackUnitMbTempStatsHistDn_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistDn = _CfprApComputeRackUnitMbTempStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 2),
    _CfprApComputeRackUnitMbTempStatsHistDn_Type()
)
cfprApComputeRackUnitMbTempStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistDn.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistRn_Type = SnmpAdminString
_CfprApComputeRackUnitMbTempStatsHistRn_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistRn = _CfprApComputeRackUnitMbTempStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 3),
    _CfprApComputeRackUnitMbTempStatsHistRn_Type()
)
cfprApComputeRackUnitMbTempStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistRn.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistAmbientTemp_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistAmbientTemp_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistAmbientTemp = _CfprApComputeRackUnitMbTempStatsHistAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 4),
    _CfprApComputeRackUnitMbTempStatsHistAmbientTemp_Type()
)
cfprApComputeRackUnitMbTempStatsHistAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistAmbientTemp.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistAmbientTempAvg_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistAmbientTempAvg_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistAmbientTempAvg = _CfprApComputeRackUnitMbTempStatsHistAmbientTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 5),
    _CfprApComputeRackUnitMbTempStatsHistAmbientTempAvg_Type()
)
cfprApComputeRackUnitMbTempStatsHistAmbientTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistAmbientTempAvg.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistAmbientTempMax_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistAmbientTempMax_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistAmbientTempMax = _CfprApComputeRackUnitMbTempStatsHistAmbientTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 6),
    _CfprApComputeRackUnitMbTempStatsHistAmbientTempMax_Type()
)
cfprApComputeRackUnitMbTempStatsHistAmbientTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistAmbientTempMax.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistAmbientTempMin_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistAmbientTempMin_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistAmbientTempMin = _CfprApComputeRackUnitMbTempStatsHistAmbientTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 7),
    _CfprApComputeRackUnitMbTempStatsHistAmbientTempMin_Type()
)
cfprApComputeRackUnitMbTempStatsHistAmbientTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistAmbientTempMin.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistFrontTemp_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistFrontTemp_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistFrontTemp = _CfprApComputeRackUnitMbTempStatsHistFrontTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 8),
    _CfprApComputeRackUnitMbTempStatsHistFrontTemp_Type()
)
cfprApComputeRackUnitMbTempStatsHistFrontTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistFrontTemp.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistFrontTempAvg_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistFrontTempAvg_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistFrontTempAvg = _CfprApComputeRackUnitMbTempStatsHistFrontTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 9),
    _CfprApComputeRackUnitMbTempStatsHistFrontTempAvg_Type()
)
cfprApComputeRackUnitMbTempStatsHistFrontTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistFrontTempAvg.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistFrontTempMax_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistFrontTempMax_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistFrontTempMax = _CfprApComputeRackUnitMbTempStatsHistFrontTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 10),
    _CfprApComputeRackUnitMbTempStatsHistFrontTempMax_Type()
)
cfprApComputeRackUnitMbTempStatsHistFrontTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistFrontTempMax.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistFrontTempMin_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistFrontTempMin_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistFrontTempMin = _CfprApComputeRackUnitMbTempStatsHistFrontTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 11),
    _CfprApComputeRackUnitMbTempStatsHistFrontTempMin_Type()
)
cfprApComputeRackUnitMbTempStatsHistFrontTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistFrontTempMin.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistId_Type = Unsigned64
_CfprApComputeRackUnitMbTempStatsHistId_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistId = _CfprApComputeRackUnitMbTempStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 12),
    _CfprApComputeRackUnitMbTempStatsHistId_Type()
)
cfprApComputeRackUnitMbTempStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistId.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistIoh1Temp_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistIoh1Temp_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistIoh1Temp = _CfprApComputeRackUnitMbTempStatsHistIoh1Temp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 13),
    _CfprApComputeRackUnitMbTempStatsHistIoh1Temp_Type()
)
cfprApComputeRackUnitMbTempStatsHistIoh1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistIoh1Temp.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistIoh1TempAvg_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistIoh1TempAvg_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistIoh1TempAvg = _CfprApComputeRackUnitMbTempStatsHistIoh1TempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 14),
    _CfprApComputeRackUnitMbTempStatsHistIoh1TempAvg_Type()
)
cfprApComputeRackUnitMbTempStatsHistIoh1TempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistIoh1TempAvg.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistIoh1TempMax_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistIoh1TempMax_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistIoh1TempMax = _CfprApComputeRackUnitMbTempStatsHistIoh1TempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 15),
    _CfprApComputeRackUnitMbTempStatsHistIoh1TempMax_Type()
)
cfprApComputeRackUnitMbTempStatsHistIoh1TempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistIoh1TempMax.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistIoh1TempMin_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistIoh1TempMin_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistIoh1TempMin = _CfprApComputeRackUnitMbTempStatsHistIoh1TempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 16),
    _CfprApComputeRackUnitMbTempStatsHistIoh1TempMin_Type()
)
cfprApComputeRackUnitMbTempStatsHistIoh1TempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistIoh1TempMin.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistIoh2Temp_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistIoh2Temp_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistIoh2Temp = _CfprApComputeRackUnitMbTempStatsHistIoh2Temp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 17),
    _CfprApComputeRackUnitMbTempStatsHistIoh2Temp_Type()
)
cfprApComputeRackUnitMbTempStatsHistIoh2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistIoh2Temp.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistIoh2TempAvg_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistIoh2TempAvg_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistIoh2TempAvg = _CfprApComputeRackUnitMbTempStatsHistIoh2TempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 18),
    _CfprApComputeRackUnitMbTempStatsHistIoh2TempAvg_Type()
)
cfprApComputeRackUnitMbTempStatsHistIoh2TempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistIoh2TempAvg.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistIoh2TempMax_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistIoh2TempMax_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistIoh2TempMax = _CfprApComputeRackUnitMbTempStatsHistIoh2TempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 19),
    _CfprApComputeRackUnitMbTempStatsHistIoh2TempMax_Type()
)
cfprApComputeRackUnitMbTempStatsHistIoh2TempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistIoh2TempMax.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistIoh2TempMin_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistIoh2TempMin_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistIoh2TempMin = _CfprApComputeRackUnitMbTempStatsHistIoh2TempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 20),
    _CfprApComputeRackUnitMbTempStatsHistIoh2TempMin_Type()
)
cfprApComputeRackUnitMbTempStatsHistIoh2TempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistIoh2TempMin.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistMostRecent_Type = TruthValue
_CfprApComputeRackUnitMbTempStatsHistMostRecent_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistMostRecent = _CfprApComputeRackUnitMbTempStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 21),
    _CfprApComputeRackUnitMbTempStatsHistMostRecent_Type()
)
cfprApComputeRackUnitMbTempStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistMostRecent.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistRearTemp_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistRearTemp_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistRearTemp = _CfprApComputeRackUnitMbTempStatsHistRearTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 22),
    _CfprApComputeRackUnitMbTempStatsHistRearTemp_Type()
)
cfprApComputeRackUnitMbTempStatsHistRearTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistRearTemp.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistRearTempAvg_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistRearTempAvg_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistRearTempAvg = _CfprApComputeRackUnitMbTempStatsHistRearTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 23),
    _CfprApComputeRackUnitMbTempStatsHistRearTempAvg_Type()
)
cfprApComputeRackUnitMbTempStatsHistRearTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistRearTempAvg.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistRearTempMax_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistRearTempMax_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistRearTempMax = _CfprApComputeRackUnitMbTempStatsHistRearTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 24),
    _CfprApComputeRackUnitMbTempStatsHistRearTempMax_Type()
)
cfprApComputeRackUnitMbTempStatsHistRearTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistRearTempMax.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistRearTempMin_Type = Integer32
_CfprApComputeRackUnitMbTempStatsHistRearTempMin_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistRearTempMin = _CfprApComputeRackUnitMbTempStatsHistRearTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 25),
    _CfprApComputeRackUnitMbTempStatsHistRearTempMin_Type()
)
cfprApComputeRackUnitMbTempStatsHistRearTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistRearTempMin.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistSuspect_Type = TruthValue
_CfprApComputeRackUnitMbTempStatsHistSuspect_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistSuspect = _CfprApComputeRackUnitMbTempStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 26),
    _CfprApComputeRackUnitMbTempStatsHistSuspect_Type()
)
cfprApComputeRackUnitMbTempStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistSuspect.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistThresholded_Type = CfprApComputeRackUnitMbTempStatsHistThresholded
_CfprApComputeRackUnitMbTempStatsHistThresholded_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistThresholded = _CfprApComputeRackUnitMbTempStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 27),
    _CfprApComputeRackUnitMbTempStatsHistThresholded_Type()
)
cfprApComputeRackUnitMbTempStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistThresholded.setStatus("current")
_CfprApComputeRackUnitMbTempStatsHistTimeCollected_Type = DateAndTime
_CfprApComputeRackUnitMbTempStatsHistTimeCollected_Object = MibTableColumn
cfprApComputeRackUnitMbTempStatsHistTimeCollected = _CfprApComputeRackUnitMbTempStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 57, 1, 28),
    _CfprApComputeRackUnitMbTempStatsHistTimeCollected_Type()
)
cfprApComputeRackUnitMbTempStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRackUnitMbTempStatsHistTimeCollected.setStatus("current")
_CfprApComputeRtcBatteryTable_Object = MibTable
cfprApComputeRtcBatteryTable = _CfprApComputeRtcBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58)
)
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryTable.setStatus("current")
_CfprApComputeRtcBatteryEntry_Object = MibTableRow
cfprApComputeRtcBatteryEntry = _CfprApComputeRtcBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1)
)
cfprApComputeRtcBatteryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeRtcBatteryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryEntry.setStatus("current")
_CfprApComputeRtcBatteryInstanceId_Type = CfprApManagedObjectId
_CfprApComputeRtcBatteryInstanceId_Object = MibTableColumn
cfprApComputeRtcBatteryInstanceId = _CfprApComputeRtcBatteryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 1),
    _CfprApComputeRtcBatteryInstanceId_Type()
)
cfprApComputeRtcBatteryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryInstanceId.setStatus("current")
_CfprApComputeRtcBatteryDn_Type = CfprApManagedObjectDn
_CfprApComputeRtcBatteryDn_Object = MibTableColumn
cfprApComputeRtcBatteryDn = _CfprApComputeRtcBatteryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 2),
    _CfprApComputeRtcBatteryDn_Type()
)
cfprApComputeRtcBatteryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryDn.setStatus("current")
_CfprApComputeRtcBatteryRn_Type = SnmpAdminString
_CfprApComputeRtcBatteryRn_Object = MibTableColumn
cfprApComputeRtcBatteryRn = _CfprApComputeRtcBatteryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 3),
    _CfprApComputeRtcBatteryRn_Type()
)
cfprApComputeRtcBatteryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryRn.setStatus("current")
_CfprApComputeRtcBatteryId_Type = Gauge32
_CfprApComputeRtcBatteryId_Object = MibTableColumn
cfprApComputeRtcBatteryId = _CfprApComputeRtcBatteryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 4),
    _CfprApComputeRtcBatteryId_Type()
)
cfprApComputeRtcBatteryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryId.setStatus("current")
_CfprApComputeRtcBatteryLocationDn_Type = SnmpAdminString
_CfprApComputeRtcBatteryLocationDn_Object = MibTableColumn
cfprApComputeRtcBatteryLocationDn = _CfprApComputeRtcBatteryLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 5),
    _CfprApComputeRtcBatteryLocationDn_Type()
)
cfprApComputeRtcBatteryLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryLocationDn.setStatus("current")
_CfprApComputeRtcBatteryModel_Type = SnmpAdminString
_CfprApComputeRtcBatteryModel_Object = MibTableColumn
cfprApComputeRtcBatteryModel = _CfprApComputeRtcBatteryModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 6),
    _CfprApComputeRtcBatteryModel_Type()
)
cfprApComputeRtcBatteryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryModel.setStatus("current")
_CfprApComputeRtcBatteryOperQualifierReason_Type = SnmpAdminString
_CfprApComputeRtcBatteryOperQualifierReason_Object = MibTableColumn
cfprApComputeRtcBatteryOperQualifierReason = _CfprApComputeRtcBatteryOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 7),
    _CfprApComputeRtcBatteryOperQualifierReason_Type()
)
cfprApComputeRtcBatteryOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryOperQualifierReason.setStatus("current")
_CfprApComputeRtcBatteryOperState_Type = CfprApEquipmentOperability
_CfprApComputeRtcBatteryOperState_Object = MibTableColumn
cfprApComputeRtcBatteryOperState = _CfprApComputeRtcBatteryOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 8),
    _CfprApComputeRtcBatteryOperState_Type()
)
cfprApComputeRtcBatteryOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryOperState.setStatus("current")
_CfprApComputeRtcBatteryOperability_Type = CfprApEquipmentOperability
_CfprApComputeRtcBatteryOperability_Object = MibTableColumn
cfprApComputeRtcBatteryOperability = _CfprApComputeRtcBatteryOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 9),
    _CfprApComputeRtcBatteryOperability_Type()
)
cfprApComputeRtcBatteryOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryOperability.setStatus("current")
_CfprApComputeRtcBatteryPerf_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeRtcBatteryPerf_Object = MibTableColumn
cfprApComputeRtcBatteryPerf = _CfprApComputeRtcBatteryPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 10),
    _CfprApComputeRtcBatteryPerf_Type()
)
cfprApComputeRtcBatteryPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryPerf.setStatus("current")
_CfprApComputeRtcBatteryPower_Type = CfprApEquipmentPowerState
_CfprApComputeRtcBatteryPower_Object = MibTableColumn
cfprApComputeRtcBatteryPower = _CfprApComputeRtcBatteryPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 11),
    _CfprApComputeRtcBatteryPower_Type()
)
cfprApComputeRtcBatteryPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryPower.setStatus("current")
_CfprApComputeRtcBatteryPresence_Type = CfprApEquipmentPresence
_CfprApComputeRtcBatteryPresence_Object = MibTableColumn
cfprApComputeRtcBatteryPresence = _CfprApComputeRtcBatteryPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 12),
    _CfprApComputeRtcBatteryPresence_Type()
)
cfprApComputeRtcBatteryPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryPresence.setStatus("current")
_CfprApComputeRtcBatteryRevision_Type = SnmpAdminString
_CfprApComputeRtcBatteryRevision_Object = MibTableColumn
cfprApComputeRtcBatteryRevision = _CfprApComputeRtcBatteryRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 13),
    _CfprApComputeRtcBatteryRevision_Type()
)
cfprApComputeRtcBatteryRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryRevision.setStatus("current")
_CfprApComputeRtcBatterySerial_Type = SnmpAdminString
_CfprApComputeRtcBatterySerial_Object = MibTableColumn
cfprApComputeRtcBatterySerial = _CfprApComputeRtcBatterySerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 14),
    _CfprApComputeRtcBatterySerial_Type()
)
cfprApComputeRtcBatterySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatterySerial.setStatus("current")
_CfprApComputeRtcBatteryThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeRtcBatteryThermal_Object = MibTableColumn
cfprApComputeRtcBatteryThermal = _CfprApComputeRtcBatteryThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 15),
    _CfprApComputeRtcBatteryThermal_Type()
)
cfprApComputeRtcBatteryThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryThermal.setStatus("current")
_CfprApComputeRtcBatteryVendor_Type = SnmpAdminString
_CfprApComputeRtcBatteryVendor_Object = MibTableColumn
cfprApComputeRtcBatteryVendor = _CfprApComputeRtcBatteryVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 16),
    _CfprApComputeRtcBatteryVendor_Type()
)
cfprApComputeRtcBatteryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryVendor.setStatus("current")
_CfprApComputeRtcBatteryVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApComputeRtcBatteryVoltage_Object = MibTableColumn
cfprApComputeRtcBatteryVoltage = _CfprApComputeRtcBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 58, 1, 17),
    _CfprApComputeRtcBatteryVoltage_Type()
)
cfprApComputeRtcBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeRtcBatteryVoltage.setStatus("current")
_CfprApComputeScrubPolicyTable_Object = MibTable
cfprApComputeScrubPolicyTable = _CfprApComputeScrubPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59)
)
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyTable.setStatus("current")
_CfprApComputeScrubPolicyEntry_Object = MibTableRow
cfprApComputeScrubPolicyEntry = _CfprApComputeScrubPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59, 1)
)
cfprApComputeScrubPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeScrubPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyEntry.setStatus("current")
_CfprApComputeScrubPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApComputeScrubPolicyInstanceId_Object = MibTableColumn
cfprApComputeScrubPolicyInstanceId = _CfprApComputeScrubPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59, 1, 1),
    _CfprApComputeScrubPolicyInstanceId_Type()
)
cfprApComputeScrubPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyInstanceId.setStatus("current")
_CfprApComputeScrubPolicyDn_Type = CfprApManagedObjectDn
_CfprApComputeScrubPolicyDn_Object = MibTableColumn
cfprApComputeScrubPolicyDn = _CfprApComputeScrubPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59, 1, 2),
    _CfprApComputeScrubPolicyDn_Type()
)
cfprApComputeScrubPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyDn.setStatus("current")
_CfprApComputeScrubPolicyRn_Type = SnmpAdminString
_CfprApComputeScrubPolicyRn_Object = MibTableColumn
cfprApComputeScrubPolicyRn = _CfprApComputeScrubPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59, 1, 3),
    _CfprApComputeScrubPolicyRn_Type()
)
cfprApComputeScrubPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyRn.setStatus("current")
_CfprApComputeScrubPolicyBiosSettingsScrub_Type = CfprApComputeScrubAction
_CfprApComputeScrubPolicyBiosSettingsScrub_Object = MibTableColumn
cfprApComputeScrubPolicyBiosSettingsScrub = _CfprApComputeScrubPolicyBiosSettingsScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59, 1, 4),
    _CfprApComputeScrubPolicyBiosSettingsScrub_Type()
)
cfprApComputeScrubPolicyBiosSettingsScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyBiosSettingsScrub.setStatus("current")
_CfprApComputeScrubPolicyDescr_Type = SnmpAdminString
_CfprApComputeScrubPolicyDescr_Object = MibTableColumn
cfprApComputeScrubPolicyDescr = _CfprApComputeScrubPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59, 1, 5),
    _CfprApComputeScrubPolicyDescr_Type()
)
cfprApComputeScrubPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyDescr.setStatus("current")
_CfprApComputeScrubPolicyDiskScrub_Type = CfprApComputeScrubAction
_CfprApComputeScrubPolicyDiskScrub_Object = MibTableColumn
cfprApComputeScrubPolicyDiskScrub = _CfprApComputeScrubPolicyDiskScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59, 1, 6),
    _CfprApComputeScrubPolicyDiskScrub_Type()
)
cfprApComputeScrubPolicyDiskScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyDiskScrub.setStatus("current")
_CfprApComputeScrubPolicyFlexFlashScrub_Type = CfprApComputeScrubAction
_CfprApComputeScrubPolicyFlexFlashScrub_Object = MibTableColumn
cfprApComputeScrubPolicyFlexFlashScrub = _CfprApComputeScrubPolicyFlexFlashScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59, 1, 7),
    _CfprApComputeScrubPolicyFlexFlashScrub_Type()
)
cfprApComputeScrubPolicyFlexFlashScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyFlexFlashScrub.setStatus("current")
_CfprApComputeScrubPolicyIntId_Type = SnmpAdminString
_CfprApComputeScrubPolicyIntId_Object = MibTableColumn
cfprApComputeScrubPolicyIntId = _CfprApComputeScrubPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59, 1, 8),
    _CfprApComputeScrubPolicyIntId_Type()
)
cfprApComputeScrubPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyIntId.setStatus("current")
_CfprApComputeScrubPolicyName_Type = SnmpAdminString
_CfprApComputeScrubPolicyName_Object = MibTableColumn
cfprApComputeScrubPolicyName = _CfprApComputeScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59, 1, 9),
    _CfprApComputeScrubPolicyName_Type()
)
cfprApComputeScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyName.setStatus("current")
_CfprApComputeScrubPolicyPolicyLevel_Type = Gauge32
_CfprApComputeScrubPolicyPolicyLevel_Object = MibTableColumn
cfprApComputeScrubPolicyPolicyLevel = _CfprApComputeScrubPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59, 1, 10),
    _CfprApComputeScrubPolicyPolicyLevel_Type()
)
cfprApComputeScrubPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyPolicyLevel.setStatus("current")
_CfprApComputeScrubPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeScrubPolicyPolicyOwner_Object = MibTableColumn
cfprApComputeScrubPolicyPolicyOwner = _CfprApComputeScrubPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 59, 1, 11),
    _CfprApComputeScrubPolicyPolicyOwner_Type()
)
cfprApComputeScrubPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeScrubPolicyPolicyOwner.setStatus("current")
_CfprApComputeServerDiscPolicyTable_Object = MibTable
cfprApComputeServerDiscPolicyTable = _CfprApComputeServerDiscPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60)
)
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyTable.setStatus("current")
_CfprApComputeServerDiscPolicyEntry_Object = MibTableRow
cfprApComputeServerDiscPolicyEntry = _CfprApComputeServerDiscPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1)
)
cfprApComputeServerDiscPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeServerDiscPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyEntry.setStatus("current")
_CfprApComputeServerDiscPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApComputeServerDiscPolicyInstanceId_Object = MibTableColumn
cfprApComputeServerDiscPolicyInstanceId = _CfprApComputeServerDiscPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 1),
    _CfprApComputeServerDiscPolicyInstanceId_Type()
)
cfprApComputeServerDiscPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyInstanceId.setStatus("current")
_CfprApComputeServerDiscPolicyDn_Type = CfprApManagedObjectDn
_CfprApComputeServerDiscPolicyDn_Object = MibTableColumn
cfprApComputeServerDiscPolicyDn = _CfprApComputeServerDiscPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 2),
    _CfprApComputeServerDiscPolicyDn_Type()
)
cfprApComputeServerDiscPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyDn.setStatus("current")
_CfprApComputeServerDiscPolicyRn_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyRn_Object = MibTableColumn
cfprApComputeServerDiscPolicyRn = _CfprApComputeServerDiscPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 3),
    _CfprApComputeServerDiscPolicyRn_Type()
)
cfprApComputeServerDiscPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyRn.setStatus("current")
_CfprApComputeServerDiscPolicyAction_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyAction_Object = MibTableColumn
cfprApComputeServerDiscPolicyAction = _CfprApComputeServerDiscPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 4),
    _CfprApComputeServerDiscPolicyAction_Type()
)
cfprApComputeServerDiscPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyAction.setStatus("current")
_CfprApComputeServerDiscPolicyDescr_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyDescr_Object = MibTableColumn
cfprApComputeServerDiscPolicyDescr = _CfprApComputeServerDiscPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 5),
    _CfprApComputeServerDiscPolicyDescr_Type()
)
cfprApComputeServerDiscPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyDescr.setStatus("current")
_CfprApComputeServerDiscPolicyFsmDescr_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyFsmDescr_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmDescr = _CfprApComputeServerDiscPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 6),
    _CfprApComputeServerDiscPolicyFsmDescr_Type()
)
cfprApComputeServerDiscPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmDescr.setStatus("current")
_CfprApComputeServerDiscPolicyFsmPrev_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyFsmPrev_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmPrev = _CfprApComputeServerDiscPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 7),
    _CfprApComputeServerDiscPolicyFsmPrev_Type()
)
cfprApComputeServerDiscPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmPrev.setStatus("current")
_CfprApComputeServerDiscPolicyFsmProgr_Type = Gauge32
_CfprApComputeServerDiscPolicyFsmProgr_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmProgr = _CfprApComputeServerDiscPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 8),
    _CfprApComputeServerDiscPolicyFsmProgr_Type()
)
cfprApComputeServerDiscPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmProgr.setStatus("current")
_CfprApComputeServerDiscPolicyFsmRmtInvErrCode_Type = Gauge32
_CfprApComputeServerDiscPolicyFsmRmtInvErrCode_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmRmtInvErrCode = _CfprApComputeServerDiscPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 9),
    _CfprApComputeServerDiscPolicyFsmRmtInvErrCode_Type()
)
cfprApComputeServerDiscPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmRmtInvErrCode.setStatus("current")
_CfprApComputeServerDiscPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmRmtInvErrDescr = _CfprApComputeServerDiscPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 10),
    _CfprApComputeServerDiscPolicyFsmRmtInvErrDescr_Type()
)
cfprApComputeServerDiscPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmRmtInvErrDescr.setStatus("current")
_CfprApComputeServerDiscPolicyFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApComputeServerDiscPolicyFsmRmtInvRslt_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmRmtInvRslt = _CfprApComputeServerDiscPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 11),
    _CfprApComputeServerDiscPolicyFsmRmtInvRslt_Type()
)
cfprApComputeServerDiscPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmRmtInvRslt.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStageDescr_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyFsmStageDescr_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmStageDescr = _CfprApComputeServerDiscPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 12),
    _CfprApComputeServerDiscPolicyFsmStageDescr_Type()
)
cfprApComputeServerDiscPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStageDescr.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStamp_Type = DateAndTime
_CfprApComputeServerDiscPolicyFsmStamp_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmStamp = _CfprApComputeServerDiscPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 13),
    _CfprApComputeServerDiscPolicyFsmStamp_Type()
)
cfprApComputeServerDiscPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStamp.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStatus_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyFsmStatus_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmStatus = _CfprApComputeServerDiscPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 14),
    _CfprApComputeServerDiscPolicyFsmStatus_Type()
)
cfprApComputeServerDiscPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStatus.setStatus("current")
_CfprApComputeServerDiscPolicyFsmTry_Type = Gauge32
_CfprApComputeServerDiscPolicyFsmTry_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmTry = _CfprApComputeServerDiscPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 15),
    _CfprApComputeServerDiscPolicyFsmTry_Type()
)
cfprApComputeServerDiscPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmTry.setStatus("current")
_CfprApComputeServerDiscPolicyIntId_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyIntId_Object = MibTableColumn
cfprApComputeServerDiscPolicyIntId = _CfprApComputeServerDiscPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 16),
    _CfprApComputeServerDiscPolicyIntId_Type()
)
cfprApComputeServerDiscPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyIntId.setStatus("current")
_CfprApComputeServerDiscPolicyName_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyName_Object = MibTableColumn
cfprApComputeServerDiscPolicyName = _CfprApComputeServerDiscPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 17),
    _CfprApComputeServerDiscPolicyName_Type()
)
cfprApComputeServerDiscPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyName.setStatus("current")
_CfprApComputeServerDiscPolicyPolicyLevel_Type = Gauge32
_CfprApComputeServerDiscPolicyPolicyLevel_Object = MibTableColumn
cfprApComputeServerDiscPolicyPolicyLevel = _CfprApComputeServerDiscPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 18),
    _CfprApComputeServerDiscPolicyPolicyLevel_Type()
)
cfprApComputeServerDiscPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyPolicyLevel.setStatus("current")
_CfprApComputeServerDiscPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeServerDiscPolicyPolicyOwner_Object = MibTableColumn
cfprApComputeServerDiscPolicyPolicyOwner = _CfprApComputeServerDiscPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 19),
    _CfprApComputeServerDiscPolicyPolicyOwner_Type()
)
cfprApComputeServerDiscPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyPolicyOwner.setStatus("current")
_CfprApComputeServerDiscPolicyQualifier_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyQualifier_Object = MibTableColumn
cfprApComputeServerDiscPolicyQualifier = _CfprApComputeServerDiscPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 20),
    _CfprApComputeServerDiscPolicyQualifier_Type()
)
cfprApComputeServerDiscPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyQualifier.setStatus("current")
_CfprApComputeServerDiscPolicyScrubPolicyName_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyScrubPolicyName_Object = MibTableColumn
cfprApComputeServerDiscPolicyScrubPolicyName = _CfprApComputeServerDiscPolicyScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 60, 1, 21),
    _CfprApComputeServerDiscPolicyScrubPolicyName_Type()
)
cfprApComputeServerDiscPolicyScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyScrubPolicyName.setStatus("current")
_CfprApComputeServerDiscPolicyFsmTable_Object = MibTable
cfprApComputeServerDiscPolicyFsmTable = _CfprApComputeServerDiscPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61)
)
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmTable.setStatus("current")
_CfprApComputeServerDiscPolicyFsmEntry_Object = MibTableRow
cfprApComputeServerDiscPolicyFsmEntry = _CfprApComputeServerDiscPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61, 1)
)
cfprApComputeServerDiscPolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeServerDiscPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmEntry.setStatus("current")
_CfprApComputeServerDiscPolicyFsmInstanceId_Type = CfprApManagedObjectId
_CfprApComputeServerDiscPolicyFsmInstanceId_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmInstanceId = _CfprApComputeServerDiscPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61, 1, 1),
    _CfprApComputeServerDiscPolicyFsmInstanceId_Type()
)
cfprApComputeServerDiscPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmInstanceId.setStatus("current")
_CfprApComputeServerDiscPolicyFsmDn_Type = CfprApManagedObjectDn
_CfprApComputeServerDiscPolicyFsmDn_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmDn = _CfprApComputeServerDiscPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61, 1, 2),
    _CfprApComputeServerDiscPolicyFsmDn_Type()
)
cfprApComputeServerDiscPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmDn.setStatus("current")
_CfprApComputeServerDiscPolicyFsmRn_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyFsmRn_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmRn = _CfprApComputeServerDiscPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61, 1, 3),
    _CfprApComputeServerDiscPolicyFsmRn_Type()
)
cfprApComputeServerDiscPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmRn.setStatus("current")
_CfprApComputeServerDiscPolicyFsmCompletionTime_Type = DateAndTime
_CfprApComputeServerDiscPolicyFsmCompletionTime_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmCompletionTime = _CfprApComputeServerDiscPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61, 1, 4),
    _CfprApComputeServerDiscPolicyFsmCompletionTime_Type()
)
cfprApComputeServerDiscPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmCompletionTime.setStatus("current")
_CfprApComputeServerDiscPolicyFsmCurrentFsm_Type = CfprApComputeServerDiscPolicyFsmCurrentFsm
_CfprApComputeServerDiscPolicyFsmCurrentFsm_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmCurrentFsm = _CfprApComputeServerDiscPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61, 1, 5),
    _CfprApComputeServerDiscPolicyFsmCurrentFsm_Type()
)
cfprApComputeServerDiscPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmCurrentFsm.setStatus("current")
_CfprApComputeServerDiscPolicyFsmDescrData_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyFsmDescrData_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmDescrData = _CfprApComputeServerDiscPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61, 1, 6),
    _CfprApComputeServerDiscPolicyFsmDescrData_Type()
)
cfprApComputeServerDiscPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmDescrData.setStatus("current")
_CfprApComputeServerDiscPolicyFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApComputeServerDiscPolicyFsmFsmStatus_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmFsmStatus = _CfprApComputeServerDiscPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61, 1, 7),
    _CfprApComputeServerDiscPolicyFsmFsmStatus_Type()
)
cfprApComputeServerDiscPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmFsmStatus.setStatus("current")
_CfprApComputeServerDiscPolicyFsmProgress_Type = Gauge32
_CfprApComputeServerDiscPolicyFsmProgress_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmProgress = _CfprApComputeServerDiscPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61, 1, 8),
    _CfprApComputeServerDiscPolicyFsmProgress_Type()
)
cfprApComputeServerDiscPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmProgress.setStatus("current")
_CfprApComputeServerDiscPolicyFsmRmtErrCode_Type = Gauge32
_CfprApComputeServerDiscPolicyFsmRmtErrCode_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmRmtErrCode = _CfprApComputeServerDiscPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61, 1, 9),
    _CfprApComputeServerDiscPolicyFsmRmtErrCode_Type()
)
cfprApComputeServerDiscPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmRmtErrCode.setStatus("current")
_CfprApComputeServerDiscPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyFsmRmtErrDescr_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmRmtErrDescr = _CfprApComputeServerDiscPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61, 1, 10),
    _CfprApComputeServerDiscPolicyFsmRmtErrDescr_Type()
)
cfprApComputeServerDiscPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmRmtErrDescr.setStatus("current")
_CfprApComputeServerDiscPolicyFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApComputeServerDiscPolicyFsmRmtRslt_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmRmtRslt = _CfprApComputeServerDiscPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 61, 1, 11),
    _CfprApComputeServerDiscPolicyFsmRmtRslt_Type()
)
cfprApComputeServerDiscPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmRmtRslt.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStageTable_Object = MibTable
cfprApComputeServerDiscPolicyFsmStageTable = _CfprApComputeServerDiscPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 62)
)
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStageTable.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStageEntry_Object = MibTableRow
cfprApComputeServerDiscPolicyFsmStageEntry = _CfprApComputeServerDiscPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 62, 1)
)
cfprApComputeServerDiscPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeServerDiscPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStageEntry.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApComputeServerDiscPolicyFsmStageInstanceId_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmStageInstanceId = _CfprApComputeServerDiscPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 62, 1, 1),
    _CfprApComputeServerDiscPolicyFsmStageInstanceId_Type()
)
cfprApComputeServerDiscPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStageInstanceId.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStageDn_Type = CfprApManagedObjectDn
_CfprApComputeServerDiscPolicyFsmStageDn_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmStageDn = _CfprApComputeServerDiscPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 62, 1, 2),
    _CfprApComputeServerDiscPolicyFsmStageDn_Type()
)
cfprApComputeServerDiscPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStageDn.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStageRn_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyFsmStageRn_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmStageRn = _CfprApComputeServerDiscPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 62, 1, 3),
    _CfprApComputeServerDiscPolicyFsmStageRn_Type()
)
cfprApComputeServerDiscPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStageRn.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStageDescrData_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyFsmStageDescrData_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmStageDescrData = _CfprApComputeServerDiscPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 62, 1, 4),
    _CfprApComputeServerDiscPolicyFsmStageDescrData_Type()
)
cfprApComputeServerDiscPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStageDescrData.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprApComputeServerDiscPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmStageLastUpdateTime = _CfprApComputeServerDiscPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 62, 1, 5),
    _CfprApComputeServerDiscPolicyFsmStageLastUpdateTime_Type()
)
cfprApComputeServerDiscPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStageLastUpdateTime.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStageName_Type = CfprApComputeServerDiscPolicyFsmStageName
_CfprApComputeServerDiscPolicyFsmStageName_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmStageName = _CfprApComputeServerDiscPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 62, 1, 6),
    _CfprApComputeServerDiscPolicyFsmStageName_Type()
)
cfprApComputeServerDiscPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStageName.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStageOrder_Type = Gauge32
_CfprApComputeServerDiscPolicyFsmStageOrder_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmStageOrder = _CfprApComputeServerDiscPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 62, 1, 7),
    _CfprApComputeServerDiscPolicyFsmStageOrder_Type()
)
cfprApComputeServerDiscPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStageOrder.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStageRetry_Type = Gauge32
_CfprApComputeServerDiscPolicyFsmStageRetry_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmStageRetry = _CfprApComputeServerDiscPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 62, 1, 8),
    _CfprApComputeServerDiscPolicyFsmStageRetry_Type()
)
cfprApComputeServerDiscPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStageRetry.setStatus("current")
_CfprApComputeServerDiscPolicyFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApComputeServerDiscPolicyFsmStageStageStatus_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmStageStageStatus = _CfprApComputeServerDiscPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 62, 1, 9),
    _CfprApComputeServerDiscPolicyFsmStageStageStatus_Type()
)
cfprApComputeServerDiscPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmStageStageStatus.setStatus("current")
_CfprApComputeServerDiscPolicyFsmTaskTable_Object = MibTable
cfprApComputeServerDiscPolicyFsmTaskTable = _CfprApComputeServerDiscPolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 63)
)
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmTaskTable.setStatus("current")
_CfprApComputeServerDiscPolicyFsmTaskEntry_Object = MibTableRow
cfprApComputeServerDiscPolicyFsmTaskEntry = _CfprApComputeServerDiscPolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 63, 1)
)
cfprApComputeServerDiscPolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeServerDiscPolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmTaskEntry.setStatus("current")
_CfprApComputeServerDiscPolicyFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApComputeServerDiscPolicyFsmTaskInstanceId_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmTaskInstanceId = _CfprApComputeServerDiscPolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 63, 1, 1),
    _CfprApComputeServerDiscPolicyFsmTaskInstanceId_Type()
)
cfprApComputeServerDiscPolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmTaskInstanceId.setStatus("current")
_CfprApComputeServerDiscPolicyFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApComputeServerDiscPolicyFsmTaskDn_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmTaskDn = _CfprApComputeServerDiscPolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 63, 1, 2),
    _CfprApComputeServerDiscPolicyFsmTaskDn_Type()
)
cfprApComputeServerDiscPolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmTaskDn.setStatus("current")
_CfprApComputeServerDiscPolicyFsmTaskRn_Type = SnmpAdminString
_CfprApComputeServerDiscPolicyFsmTaskRn_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmTaskRn = _CfprApComputeServerDiscPolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 63, 1, 3),
    _CfprApComputeServerDiscPolicyFsmTaskRn_Type()
)
cfprApComputeServerDiscPolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmTaskRn.setStatus("current")
_CfprApComputeServerDiscPolicyFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApComputeServerDiscPolicyFsmTaskCompletion_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmTaskCompletion = _CfprApComputeServerDiscPolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 63, 1, 4),
    _CfprApComputeServerDiscPolicyFsmTaskCompletion_Type()
)
cfprApComputeServerDiscPolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmTaskCompletion.setStatus("current")
_CfprApComputeServerDiscPolicyFsmTaskFlags_Type = CfprApFsmFlags
_CfprApComputeServerDiscPolicyFsmTaskFlags_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmTaskFlags = _CfprApComputeServerDiscPolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 63, 1, 5),
    _CfprApComputeServerDiscPolicyFsmTaskFlags_Type()
)
cfprApComputeServerDiscPolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmTaskFlags.setStatus("current")
_CfprApComputeServerDiscPolicyFsmTaskItem_Type = CfprApComputeServerDiscPolicyFsmTaskItem
_CfprApComputeServerDiscPolicyFsmTaskItem_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmTaskItem = _CfprApComputeServerDiscPolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 63, 1, 6),
    _CfprApComputeServerDiscPolicyFsmTaskItem_Type()
)
cfprApComputeServerDiscPolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmTaskItem.setStatus("current")
_CfprApComputeServerDiscPolicyFsmTaskSeqId_Type = Gauge32
_CfprApComputeServerDiscPolicyFsmTaskSeqId_Object = MibTableColumn
cfprApComputeServerDiscPolicyFsmTaskSeqId = _CfprApComputeServerDiscPolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 63, 1, 7),
    _CfprApComputeServerDiscPolicyFsmTaskSeqId_Type()
)
cfprApComputeServerDiscPolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerDiscPolicyFsmTaskSeqId.setStatus("current")
_CfprApComputeServerMgmtPolicyTable_Object = MibTable
cfprApComputeServerMgmtPolicyTable = _CfprApComputeServerMgmtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 64)
)
if mibBuilder.loadTexts:
    cfprApComputeServerMgmtPolicyTable.setStatus("current")
_CfprApComputeServerMgmtPolicyEntry_Object = MibTableRow
cfprApComputeServerMgmtPolicyEntry = _CfprApComputeServerMgmtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 64, 1)
)
cfprApComputeServerMgmtPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeServerMgmtPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeServerMgmtPolicyEntry.setStatus("current")
_CfprApComputeServerMgmtPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApComputeServerMgmtPolicyInstanceId_Object = MibTableColumn
cfprApComputeServerMgmtPolicyInstanceId = _CfprApComputeServerMgmtPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 64, 1, 1),
    _CfprApComputeServerMgmtPolicyInstanceId_Type()
)
cfprApComputeServerMgmtPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeServerMgmtPolicyInstanceId.setStatus("current")
_CfprApComputeServerMgmtPolicyDn_Type = CfprApManagedObjectDn
_CfprApComputeServerMgmtPolicyDn_Object = MibTableColumn
cfprApComputeServerMgmtPolicyDn = _CfprApComputeServerMgmtPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 64, 1, 2),
    _CfprApComputeServerMgmtPolicyDn_Type()
)
cfprApComputeServerMgmtPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerMgmtPolicyDn.setStatus("current")
_CfprApComputeServerMgmtPolicyRn_Type = SnmpAdminString
_CfprApComputeServerMgmtPolicyRn_Object = MibTableColumn
cfprApComputeServerMgmtPolicyRn = _CfprApComputeServerMgmtPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 64, 1, 3),
    _CfprApComputeServerMgmtPolicyRn_Type()
)
cfprApComputeServerMgmtPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerMgmtPolicyRn.setStatus("current")
_CfprApComputeServerMgmtPolicyAction_Type = CfprApComputeServerMgmtDiscAction
_CfprApComputeServerMgmtPolicyAction_Object = MibTableColumn
cfprApComputeServerMgmtPolicyAction = _CfprApComputeServerMgmtPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 64, 1, 4),
    _CfprApComputeServerMgmtPolicyAction_Type()
)
cfprApComputeServerMgmtPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerMgmtPolicyAction.setStatus("current")
_CfprApComputeServerMgmtPolicyDescr_Type = SnmpAdminString
_CfprApComputeServerMgmtPolicyDescr_Object = MibTableColumn
cfprApComputeServerMgmtPolicyDescr = _CfprApComputeServerMgmtPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 64, 1, 5),
    _CfprApComputeServerMgmtPolicyDescr_Type()
)
cfprApComputeServerMgmtPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerMgmtPolicyDescr.setStatus("current")
_CfprApComputeServerMgmtPolicyIntId_Type = SnmpAdminString
_CfprApComputeServerMgmtPolicyIntId_Object = MibTableColumn
cfprApComputeServerMgmtPolicyIntId = _CfprApComputeServerMgmtPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 64, 1, 6),
    _CfprApComputeServerMgmtPolicyIntId_Type()
)
cfprApComputeServerMgmtPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerMgmtPolicyIntId.setStatus("current")
_CfprApComputeServerMgmtPolicyName_Type = SnmpAdminString
_CfprApComputeServerMgmtPolicyName_Object = MibTableColumn
cfprApComputeServerMgmtPolicyName = _CfprApComputeServerMgmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 64, 1, 7),
    _CfprApComputeServerMgmtPolicyName_Type()
)
cfprApComputeServerMgmtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerMgmtPolicyName.setStatus("current")
_CfprApComputeServerMgmtPolicyPolicyLevel_Type = Gauge32
_CfprApComputeServerMgmtPolicyPolicyLevel_Object = MibTableColumn
cfprApComputeServerMgmtPolicyPolicyLevel = _CfprApComputeServerMgmtPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 64, 1, 8),
    _CfprApComputeServerMgmtPolicyPolicyLevel_Type()
)
cfprApComputeServerMgmtPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerMgmtPolicyPolicyLevel.setStatus("current")
_CfprApComputeServerMgmtPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApComputeServerMgmtPolicyPolicyOwner_Object = MibTableColumn
cfprApComputeServerMgmtPolicyPolicyOwner = _CfprApComputeServerMgmtPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 64, 1, 9),
    _CfprApComputeServerMgmtPolicyPolicyOwner_Type()
)
cfprApComputeServerMgmtPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerMgmtPolicyPolicyOwner.setStatus("current")
_CfprApComputeServerMgmtPolicyQualifier_Type = SnmpAdminString
_CfprApComputeServerMgmtPolicyQualifier_Object = MibTableColumn
cfprApComputeServerMgmtPolicyQualifier = _CfprApComputeServerMgmtPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 64, 1, 10),
    _CfprApComputeServerMgmtPolicyQualifier_Type()
)
cfprApComputeServerMgmtPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeServerMgmtPolicyQualifier.setStatus("current")
_CfprApComputeSlotQualTable_Object = MibTable
cfprApComputeSlotQualTable = _CfprApComputeSlotQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 65)
)
if mibBuilder.loadTexts:
    cfprApComputeSlotQualTable.setStatus("current")
_CfprApComputeSlotQualEntry_Object = MibTableRow
cfprApComputeSlotQualEntry = _CfprApComputeSlotQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 65, 1)
)
cfprApComputeSlotQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-COMPUTE-MIB", "cfprApComputeSlotQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApComputeSlotQualEntry.setStatus("current")
_CfprApComputeSlotQualInstanceId_Type = CfprApManagedObjectId
_CfprApComputeSlotQualInstanceId_Object = MibTableColumn
cfprApComputeSlotQualInstanceId = _CfprApComputeSlotQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 65, 1, 1),
    _CfprApComputeSlotQualInstanceId_Type()
)
cfprApComputeSlotQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApComputeSlotQualInstanceId.setStatus("current")
_CfprApComputeSlotQualDn_Type = CfprApManagedObjectDn
_CfprApComputeSlotQualDn_Object = MibTableColumn
cfprApComputeSlotQualDn = _CfprApComputeSlotQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 65, 1, 2),
    _CfprApComputeSlotQualDn_Type()
)
cfprApComputeSlotQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeSlotQualDn.setStatus("current")
_CfprApComputeSlotQualRn_Type = SnmpAdminString
_CfprApComputeSlotQualRn_Object = MibTableColumn
cfprApComputeSlotQualRn = _CfprApComputeSlotQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 65, 1, 3),
    _CfprApComputeSlotQualRn_Type()
)
cfprApComputeSlotQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeSlotQualRn.setStatus("current")
_CfprApComputeSlotQualMaxId_Type = CfprApComputeSlotQualMaxId
_CfprApComputeSlotQualMaxId_Object = MibTableColumn
cfprApComputeSlotQualMaxId = _CfprApComputeSlotQualMaxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 65, 1, 4),
    _CfprApComputeSlotQualMaxId_Type()
)
cfprApComputeSlotQualMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeSlotQualMaxId.setStatus("current")
_CfprApComputeSlotQualMinId_Type = CfprApComputeSlotQualMinId
_CfprApComputeSlotQualMinId_Object = MibTableColumn
cfprApComputeSlotQualMinId = _CfprApComputeSlotQualMinId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 12, 65, 1, 5),
    _CfprApComputeSlotQualMinId_Type()
)
cfprApComputeSlotQualMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApComputeSlotQualMinId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-COMPUTE-MIB",
    **{"cfprApComputeObjects": cfprApComputeObjects,
       "cfprApComputeAutoconfigPolicyTable": cfprApComputeAutoconfigPolicyTable,
       "cfprApComputeAutoconfigPolicyEntry": cfprApComputeAutoconfigPolicyEntry,
       "cfprApComputeAutoconfigPolicyInstanceId": cfprApComputeAutoconfigPolicyInstanceId,
       "cfprApComputeAutoconfigPolicyDn": cfprApComputeAutoconfigPolicyDn,
       "cfprApComputeAutoconfigPolicyRn": cfprApComputeAutoconfigPolicyRn,
       "cfprApComputeAutoconfigPolicyDescr": cfprApComputeAutoconfigPolicyDescr,
       "cfprApComputeAutoconfigPolicyDstDn": cfprApComputeAutoconfigPolicyDstDn,
       "cfprApComputeAutoconfigPolicyIntId": cfprApComputeAutoconfigPolicyIntId,
       "cfprApComputeAutoconfigPolicyName": cfprApComputeAutoconfigPolicyName,
       "cfprApComputeAutoconfigPolicyPolicyLevel": cfprApComputeAutoconfigPolicyPolicyLevel,
       "cfprApComputeAutoconfigPolicyPolicyOwner": cfprApComputeAutoconfigPolicyPolicyOwner,
       "cfprApComputeAutoconfigPolicyQualifier": cfprApComputeAutoconfigPolicyQualifier,
       "cfprApComputeAutoconfigPolicySrcTemplName": cfprApComputeAutoconfigPolicySrcTemplName,
       "cfprApComputeBladeTable": cfprApComputeBladeTable,
       "cfprApComputeBladeEntry": cfprApComputeBladeEntry,
       "cfprApComputeBladeInstanceId": cfprApComputeBladeInstanceId,
       "cfprApComputeBladeDn": cfprApComputeBladeDn,
       "cfprApComputeBladeRn": cfprApComputeBladeRn,
       "cfprApComputeBladeAdminPower": cfprApComputeBladeAdminPower,
       "cfprApComputeBladeAdminState": cfprApComputeBladeAdminState,
       "cfprApComputeBladeAssignedToDn": cfprApComputeBladeAssignedToDn,
       "cfprApComputeBladeAssociation": cfprApComputeBladeAssociation,
       "cfprApComputeBladeAvailability": cfprApComputeBladeAvailability,
       "cfprApComputeBladeAvailableMemory": cfprApComputeBladeAvailableMemory,
       "cfprApComputeBladeChassisId": cfprApComputeBladeChassisId,
       "cfprApComputeBladeCheckPoint": cfprApComputeBladeCheckPoint,
       "cfprApComputeBladeConnPath": cfprApComputeBladeConnPath,
       "cfprApComputeBladeConnStatus": cfprApComputeBladeConnStatus,
       "cfprApComputeBladeDescr": cfprApComputeBladeDescr,
       "cfprApComputeBladeDiscovery": cfprApComputeBladeDiscovery,
       "cfprApComputeBladeFltAggr": cfprApComputeBladeFltAggr,
       "cfprApComputeBladeFsmDescr": cfprApComputeBladeFsmDescr,
       "cfprApComputeBladeFsmFlags": cfprApComputeBladeFsmFlags,
       "cfprApComputeBladeFsmPrev": cfprApComputeBladeFsmPrev,
       "cfprApComputeBladeFsmProgr": cfprApComputeBladeFsmProgr,
       "cfprApComputeBladeFsmRmtInvErrCode": cfprApComputeBladeFsmRmtInvErrCode,
       "cfprApComputeBladeFsmRmtInvErrDescr": cfprApComputeBladeFsmRmtInvErrDescr,
       "cfprApComputeBladeFsmRmtInvRslt": cfprApComputeBladeFsmRmtInvRslt,
       "cfprApComputeBladeFsmStageDescr": cfprApComputeBladeFsmStageDescr,
       "cfprApComputeBladeFsmStamp": cfprApComputeBladeFsmStamp,
       "cfprApComputeBladeFsmStatus": cfprApComputeBladeFsmStatus,
       "cfprApComputeBladeFsmTry": cfprApComputeBladeFsmTry,
       "cfprApComputeBladeIntId": cfprApComputeBladeIntId,
       "cfprApComputeBladeLc": cfprApComputeBladeLc,
       "cfprApComputeBladeLcTs": cfprApComputeBladeLcTs,
       "cfprApComputeBladeLocalId": cfprApComputeBladeLocalId,
       "cfprApComputeBladeLowVoltageMemory": cfprApComputeBladeLowVoltageMemory,
       "cfprApComputeBladeManagingInst": cfprApComputeBladeManagingInst,
       "cfprApComputeBladeMemorySpeed": cfprApComputeBladeMemorySpeed,
       "cfprApComputeBladeMfgTime": cfprApComputeBladeMfgTime,
       "cfprApComputeBladeModel": cfprApComputeBladeModel,
       "cfprApComputeBladeName": cfprApComputeBladeName,
       "cfprApComputeBladeNumOfAdaptors": cfprApComputeBladeNumOfAdaptors,
       "cfprApComputeBladeNumOfCores": cfprApComputeBladeNumOfCores,
       "cfprApComputeBladeNumOfCoresEnabled": cfprApComputeBladeNumOfCoresEnabled,
       "cfprApComputeBladeNumOfCpus": cfprApComputeBladeNumOfCpus,
       "cfprApComputeBladeNumOfEthHostIfs": cfprApComputeBladeNumOfEthHostIfs,
       "cfprApComputeBladeNumOfFcHostIfs": cfprApComputeBladeNumOfFcHostIfs,
       "cfprApComputeBladeNumOfThreads": cfprApComputeBladeNumOfThreads,
       "cfprApComputeBladeOperPower": cfprApComputeBladeOperPower,
       "cfprApComputeBladeOperQualifier": cfprApComputeBladeOperQualifier,
       "cfprApComputeBladeOperState": cfprApComputeBladeOperState,
       "cfprApComputeBladeOperability": cfprApComputeBladeOperability,
       "cfprApComputeBladeOriginalUuid": cfprApComputeBladeOriginalUuid,
       "cfprApComputeBladePartNumber": cfprApComputeBladePartNumber,
       "cfprApComputeBladePolicyLevel": cfprApComputeBladePolicyLevel,
       "cfprApComputeBladePolicyOwner": cfprApComputeBladePolicyOwner,
       "cfprApComputeBladePresence": cfprApComputeBladePresence,
       "cfprApComputeBladeRevision": cfprApComputeBladeRevision,
       "cfprApComputeBladeScaledMode": cfprApComputeBladeScaledMode,
       "cfprApComputeBladeSerial": cfprApComputeBladeSerial,
       "cfprApComputeBladeServerId": cfprApComputeBladeServerId,
       "cfprApComputeBladeSlotId": cfprApComputeBladeSlotId,
       "cfprApComputeBladeTotalMemory": cfprApComputeBladeTotalMemory,
       "cfprApComputeBladeUpgradeScenario": cfprApComputeBladeUpgradeScenario,
       "cfprApComputeBladeUsrLbl": cfprApComputeBladeUsrLbl,
       "cfprApComputeBladeUuid": cfprApComputeBladeUuid,
       "cfprApComputeBladeVendor": cfprApComputeBladeVendor,
       "cfprApComputeBladeVid": cfprApComputeBladeVid,
       "cfprApComputeBladeDiscPolicyTable": cfprApComputeBladeDiscPolicyTable,
       "cfprApComputeBladeDiscPolicyEntry": cfprApComputeBladeDiscPolicyEntry,
       "cfprApComputeBladeDiscPolicyInstanceId": cfprApComputeBladeDiscPolicyInstanceId,
       "cfprApComputeBladeDiscPolicyDn": cfprApComputeBladeDiscPolicyDn,
       "cfprApComputeBladeDiscPolicyRn": cfprApComputeBladeDiscPolicyRn,
       "cfprApComputeBladeDiscPolicyAction": cfprApComputeBladeDiscPolicyAction,
       "cfprApComputeBladeDiscPolicyDescr": cfprApComputeBladeDiscPolicyDescr,
       "cfprApComputeBladeDiscPolicyIntId": cfprApComputeBladeDiscPolicyIntId,
       "cfprApComputeBladeDiscPolicyName": cfprApComputeBladeDiscPolicyName,
       "cfprApComputeBladeDiscPolicyPolicyLevel": cfprApComputeBladeDiscPolicyPolicyLevel,
       "cfprApComputeBladeDiscPolicyPolicyOwner": cfprApComputeBladeDiscPolicyPolicyOwner,
       "cfprApComputeBladeDiscPolicyQualifier": cfprApComputeBladeDiscPolicyQualifier,
       "cfprApComputeBladeDiscPolicyScrubPolicyName": cfprApComputeBladeDiscPolicyScrubPolicyName,
       "cfprApComputeBladeFsmTable": cfprApComputeBladeFsmTable,
       "cfprApComputeBladeFsmEntry": cfprApComputeBladeFsmEntry,
       "cfprApComputeBladeFsmInstanceId": cfprApComputeBladeFsmInstanceId,
       "cfprApComputeBladeFsmDn": cfprApComputeBladeFsmDn,
       "cfprApComputeBladeFsmRn": cfprApComputeBladeFsmRn,
       "cfprApComputeBladeFsmCompletionTime": cfprApComputeBladeFsmCompletionTime,
       "cfprApComputeBladeFsmCurrentFsm": cfprApComputeBladeFsmCurrentFsm,
       "cfprApComputeBladeFsmDescrData": cfprApComputeBladeFsmDescrData,
       "cfprApComputeBladeFsmFsmStatus": cfprApComputeBladeFsmFsmStatus,
       "cfprApComputeBladeFsmProgress": cfprApComputeBladeFsmProgress,
       "cfprApComputeBladeFsmRmtErrCode": cfprApComputeBladeFsmRmtErrCode,
       "cfprApComputeBladeFsmRmtErrDescr": cfprApComputeBladeFsmRmtErrDescr,
       "cfprApComputeBladeFsmRmtRslt": cfprApComputeBladeFsmRmtRslt,
       "cfprApComputeBladeFsmStageTable": cfprApComputeBladeFsmStageTable,
       "cfprApComputeBladeFsmStageEntry": cfprApComputeBladeFsmStageEntry,
       "cfprApComputeBladeFsmStageInstanceId": cfprApComputeBladeFsmStageInstanceId,
       "cfprApComputeBladeFsmStageDn": cfprApComputeBladeFsmStageDn,
       "cfprApComputeBladeFsmStageRn": cfprApComputeBladeFsmStageRn,
       "cfprApComputeBladeFsmStageDescrData": cfprApComputeBladeFsmStageDescrData,
       "cfprApComputeBladeFsmStageLastUpdateTime": cfprApComputeBladeFsmStageLastUpdateTime,
       "cfprApComputeBladeFsmStageName": cfprApComputeBladeFsmStageName,
       "cfprApComputeBladeFsmStageOrder": cfprApComputeBladeFsmStageOrder,
       "cfprApComputeBladeFsmStageRetry": cfprApComputeBladeFsmStageRetry,
       "cfprApComputeBladeFsmStageStageStatus": cfprApComputeBladeFsmStageStageStatus,
       "cfprApComputeBladeFsmTaskTable": cfprApComputeBladeFsmTaskTable,
       "cfprApComputeBladeFsmTaskEntry": cfprApComputeBladeFsmTaskEntry,
       "cfprApComputeBladeFsmTaskInstanceId": cfprApComputeBladeFsmTaskInstanceId,
       "cfprApComputeBladeFsmTaskDn": cfprApComputeBladeFsmTaskDn,
       "cfprApComputeBladeFsmTaskRn": cfprApComputeBladeFsmTaskRn,
       "cfprApComputeBladeFsmTaskCompletion": cfprApComputeBladeFsmTaskCompletion,
       "cfprApComputeBladeFsmTaskFlags": cfprApComputeBladeFsmTaskFlags,
       "cfprApComputeBladeFsmTaskItem": cfprApComputeBladeFsmTaskItem,
       "cfprApComputeBladeFsmTaskSeqId": cfprApComputeBladeFsmTaskSeqId,
       "cfprApComputeBladeInheritPolicyTable": cfprApComputeBladeInheritPolicyTable,
       "cfprApComputeBladeInheritPolicyEntry": cfprApComputeBladeInheritPolicyEntry,
       "cfprApComputeBladeInheritPolicyInstanceId": cfprApComputeBladeInheritPolicyInstanceId,
       "cfprApComputeBladeInheritPolicyDn": cfprApComputeBladeInheritPolicyDn,
       "cfprApComputeBladeInheritPolicyRn": cfprApComputeBladeInheritPolicyRn,
       "cfprApComputeBladeInheritPolicyDescr": cfprApComputeBladeInheritPolicyDescr,
       "cfprApComputeBladeInheritPolicyDstDn": cfprApComputeBladeInheritPolicyDstDn,
       "cfprApComputeBladeInheritPolicyIntId": cfprApComputeBladeInheritPolicyIntId,
       "cfprApComputeBladeInheritPolicyName": cfprApComputeBladeInheritPolicyName,
       "cfprApComputeBladeInheritPolicyPolicyLevel": cfprApComputeBladeInheritPolicyPolicyLevel,
       "cfprApComputeBladeInheritPolicyPolicyOwner": cfprApComputeBladeInheritPolicyPolicyOwner,
       "cfprApComputeBladeInheritPolicyQualifier": cfprApComputeBladeInheritPolicyQualifier,
       "cfprApComputeBoardTable": cfprApComputeBoardTable,
       "cfprApComputeBoardEntry": cfprApComputeBoardEntry,
       "cfprApComputeBoardInstanceId": cfprApComputeBoardInstanceId,
       "cfprApComputeBoardDn": cfprApComputeBoardDn,
       "cfprApComputeBoardRn": cfprApComputeBoardRn,
       "cfprApComputeBoardCmosVoltage": cfprApComputeBoardCmosVoltage,
       "cfprApComputeBoardCpuType": cfprApComputeBoardCpuType,
       "cfprApComputeBoardFaultQualifier": cfprApComputeBoardFaultQualifier,
       "cfprApComputeBoardId": cfprApComputeBoardId,
       "cfprApComputeBoardLocationDn": cfprApComputeBoardLocationDn,
       "cfprApComputeBoardModel": cfprApComputeBoardModel,
       "cfprApComputeBoardOperPower": cfprApComputeBoardOperPower,
       "cfprApComputeBoardOperQualifierReason": cfprApComputeBoardOperQualifierReason,
       "cfprApComputeBoardOperState": cfprApComputeBoardOperState,
       "cfprApComputeBoardOperability": cfprApComputeBoardOperability,
       "cfprApComputeBoardPerf": cfprApComputeBoardPerf,
       "cfprApComputeBoardPower": cfprApComputeBoardPower,
       "cfprApComputeBoardPowerUsage": cfprApComputeBoardPowerUsage,
       "cfprApComputeBoardPresence": cfprApComputeBoardPresence,
       "cfprApComputeBoardRevision": cfprApComputeBoardRevision,
       "cfprApComputeBoardSerial": cfprApComputeBoardSerial,
       "cfprApComputeBoardThermal": cfprApComputeBoardThermal,
       "cfprApComputeBoardVendor": cfprApComputeBoardVendor,
       "cfprApComputeBoardVoltage": cfprApComputeBoardVoltage,
       "cfprApComputeBoardConnectorTable": cfprApComputeBoardConnectorTable,
       "cfprApComputeBoardConnectorEntry": cfprApComputeBoardConnectorEntry,
       "cfprApComputeBoardConnectorInstanceId": cfprApComputeBoardConnectorInstanceId,
       "cfprApComputeBoardConnectorDn": cfprApComputeBoardConnectorDn,
       "cfprApComputeBoardConnectorRn": cfprApComputeBoardConnectorRn,
       "cfprApComputeBoardConnectorBoardConnectorType": cfprApComputeBoardConnectorBoardConnectorType,
       "cfprApComputeBoardConnectorMasterSlotId": cfprApComputeBoardConnectorMasterSlotId,
       "cfprApComputeBoardConnectorSlaveSlotId": cfprApComputeBoardConnectorSlaveSlotId,
       "cfprApComputeBoardControllerTable": cfprApComputeBoardControllerTable,
       "cfprApComputeBoardControllerEntry": cfprApComputeBoardControllerEntry,
       "cfprApComputeBoardControllerInstanceId": cfprApComputeBoardControllerInstanceId,
       "cfprApComputeBoardControllerDn": cfprApComputeBoardControllerDn,
       "cfprApComputeBoardControllerRn": cfprApComputeBoardControllerRn,
       "cfprApComputeBoardControllerId": cfprApComputeBoardControllerId,
       "cfprApComputeBoardControllerLocationDn": cfprApComputeBoardControllerLocationDn,
       "cfprApComputeBoardControllerModel": cfprApComputeBoardControllerModel,
       "cfprApComputeBoardControllerOperQualifierReason": cfprApComputeBoardControllerOperQualifierReason,
       "cfprApComputeBoardControllerOperState": cfprApComputeBoardControllerOperState,
       "cfprApComputeBoardControllerOperability": cfprApComputeBoardControllerOperability,
       "cfprApComputeBoardControllerPerf": cfprApComputeBoardControllerPerf,
       "cfprApComputeBoardControllerPower": cfprApComputeBoardControllerPower,
       "cfprApComputeBoardControllerPresence": cfprApComputeBoardControllerPresence,
       "cfprApComputeBoardControllerRevision": cfprApComputeBoardControllerRevision,
       "cfprApComputeBoardControllerSerial": cfprApComputeBoardControllerSerial,
       "cfprApComputeBoardControllerThermal": cfprApComputeBoardControllerThermal,
       "cfprApComputeBoardControllerVendor": cfprApComputeBoardControllerVendor,
       "cfprApComputeBoardControllerVoltage": cfprApComputeBoardControllerVoltage,
       "cfprApComputeChassisConnPolicyTable": cfprApComputeChassisConnPolicyTable,
       "cfprApComputeChassisConnPolicyEntry": cfprApComputeChassisConnPolicyEntry,
       "cfprApComputeChassisConnPolicyInstanceId": cfprApComputeChassisConnPolicyInstanceId,
       "cfprApComputeChassisConnPolicyDn": cfprApComputeChassisConnPolicyDn,
       "cfprApComputeChassisConnPolicyRn": cfprApComputeChassisConnPolicyRn,
       "cfprApComputeChassisConnPolicyAdminState": cfprApComputeChassisConnPolicyAdminState,
       "cfprApComputeChassisConnPolicyChassisId": cfprApComputeChassisConnPolicyChassisId,
       "cfprApComputeChassisConnPolicyDescr": cfprApComputeChassisConnPolicyDescr,
       "cfprApComputeChassisConnPolicyIntId": cfprApComputeChassisConnPolicyIntId,
       "cfprApComputeChassisConnPolicyName": cfprApComputeChassisConnPolicyName,
       "cfprApComputeChassisConnPolicyPolicyLevel": cfprApComputeChassisConnPolicyPolicyLevel,
       "cfprApComputeChassisConnPolicyPolicyOwner": cfprApComputeChassisConnPolicyPolicyOwner,
       "cfprApComputeChassisConnPolicyQualifier": cfprApComputeChassisConnPolicyQualifier,
       "cfprApComputeChassisConnPolicySwitchId": cfprApComputeChassisConnPolicySwitchId,
       "cfprApComputeChassisDiscPolicyTable": cfprApComputeChassisDiscPolicyTable,
       "cfprApComputeChassisDiscPolicyEntry": cfprApComputeChassisDiscPolicyEntry,
       "cfprApComputeChassisDiscPolicyInstanceId": cfprApComputeChassisDiscPolicyInstanceId,
       "cfprApComputeChassisDiscPolicyDn": cfprApComputeChassisDiscPolicyDn,
       "cfprApComputeChassisDiscPolicyRn": cfprApComputeChassisDiscPolicyRn,
       "cfprApComputeChassisDiscPolicyAction": cfprApComputeChassisDiscPolicyAction,
       "cfprApComputeChassisDiscPolicyDescr": cfprApComputeChassisDiscPolicyDescr,
       "cfprApComputeChassisDiscPolicyIntId": cfprApComputeChassisDiscPolicyIntId,
       "cfprApComputeChassisDiscPolicyLinkAggregationPref": cfprApComputeChassisDiscPolicyLinkAggregationPref,
       "cfprApComputeChassisDiscPolicyName": cfprApComputeChassisDiscPolicyName,
       "cfprApComputeChassisDiscPolicyPolicyLevel": cfprApComputeChassisDiscPolicyPolicyLevel,
       "cfprApComputeChassisDiscPolicyPolicyOwner": cfprApComputeChassisDiscPolicyPolicyOwner,
       "cfprApComputeChassisDiscPolicyQualifier": cfprApComputeChassisDiscPolicyQualifier,
       "cfprApComputeChassisDiscPolicyRebalance": cfprApComputeChassisDiscPolicyRebalance,
       "cfprApComputeChassisQualTable": cfprApComputeChassisQualTable,
       "cfprApComputeChassisQualEntry": cfprApComputeChassisQualEntry,
       "cfprApComputeChassisQualInstanceId": cfprApComputeChassisQualInstanceId,
       "cfprApComputeChassisQualDn": cfprApComputeChassisQualDn,
       "cfprApComputeChassisQualRn": cfprApComputeChassisQualRn,
       "cfprApComputeChassisQualMaxId": cfprApComputeChassisQualMaxId,
       "cfprApComputeChassisQualMinId": cfprApComputeChassisQualMinId,
       "cfprApComputeDefaultsTable": cfprApComputeDefaultsTable,
       "cfprApComputeDefaultsEntry": cfprApComputeDefaultsEntry,
       "cfprApComputeDefaultsInstanceId": cfprApComputeDefaultsInstanceId,
       "cfprApComputeDefaultsDn": cfprApComputeDefaultsDn,
       "cfprApComputeDefaultsRn": cfprApComputeDefaultsRn,
       "cfprApComputeExtBoardTable": cfprApComputeExtBoardTable,
       "cfprApComputeExtBoardEntry": cfprApComputeExtBoardEntry,
       "cfprApComputeExtBoardInstanceId": cfprApComputeExtBoardInstanceId,
       "cfprApComputeExtBoardDn": cfprApComputeExtBoardDn,
       "cfprApComputeExtBoardRn": cfprApComputeExtBoardRn,
       "cfprApComputeExtBoardBoardAggregationRole": cfprApComputeExtBoardBoardAggregationRole,
       "cfprApComputeExtBoardChassisId": cfprApComputeExtBoardChassisId,
       "cfprApComputeExtBoardCmosVoltage": cfprApComputeExtBoardCmosVoltage,
       "cfprApComputeExtBoardConnPath": cfprApComputeExtBoardConnPath,
       "cfprApComputeExtBoardConnStatus": cfprApComputeExtBoardConnStatus,
       "cfprApComputeExtBoardFaultQualifier": cfprApComputeExtBoardFaultQualifier,
       "cfprApComputeExtBoardId": cfprApComputeExtBoardId,
       "cfprApComputeExtBoardLocationDn": cfprApComputeExtBoardLocationDn,
       "cfprApComputeExtBoardManagingInst": cfprApComputeExtBoardManagingInst,
       "cfprApComputeExtBoardModel": cfprApComputeExtBoardModel,
       "cfprApComputeExtBoardOperPower": cfprApComputeExtBoardOperPower,
       "cfprApComputeExtBoardOperQualifierReason": cfprApComputeExtBoardOperQualifierReason,
       "cfprApComputeExtBoardOperState": cfprApComputeExtBoardOperState,
       "cfprApComputeExtBoardOperability": cfprApComputeExtBoardOperability,
       "cfprApComputeExtBoardPerf": cfprApComputeExtBoardPerf,
       "cfprApComputeExtBoardPower": cfprApComputeExtBoardPower,
       "cfprApComputeExtBoardPowerUsage": cfprApComputeExtBoardPowerUsage,
       "cfprApComputeExtBoardPresence": cfprApComputeExtBoardPresence,
       "cfprApComputeExtBoardRevision": cfprApComputeExtBoardRevision,
       "cfprApComputeExtBoardSerial": cfprApComputeExtBoardSerial,
       "cfprApComputeExtBoardSlotId": cfprApComputeExtBoardSlotId,
       "cfprApComputeExtBoardThermal": cfprApComputeExtBoardThermal,
       "cfprApComputeExtBoardVendor": cfprApComputeExtBoardVendor,
       "cfprApComputeExtBoardVoltage": cfprApComputeExtBoardVoltage,
       "cfprApComputeFwSyncAckTable": cfprApComputeFwSyncAckTable,
       "cfprApComputeFwSyncAckEntry": cfprApComputeFwSyncAckEntry,
       "cfprApComputeFwSyncAckInstanceId": cfprApComputeFwSyncAckInstanceId,
       "cfprApComputeFwSyncAckDn": cfprApComputeFwSyncAckDn,
       "cfprApComputeFwSyncAckRn": cfprApComputeFwSyncAckRn,
       "cfprApComputeFwSyncAckAcked": cfprApComputeFwSyncAckAcked,
       "cfprApComputeFwSyncAckAckedBy": cfprApComputeFwSyncAckAckedBy,
       "cfprApComputeFwSyncAckAdminState": cfprApComputeFwSyncAckAdminState,
       "cfprApComputeFwSyncAckAutoDelete": cfprApComputeFwSyncAckAutoDelete,
       "cfprApComputeFwSyncAckChangeBy": cfprApComputeFwSyncAckChangeBy,
       "cfprApComputeFwSyncAckChangeDetails": cfprApComputeFwSyncAckChangeDetails,
       "cfprApComputeFwSyncAckChanges": cfprApComputeFwSyncAckChanges,
       "cfprApComputeFwSyncAckDescr": cfprApComputeFwSyncAckDescr,
       "cfprApComputeFwSyncAckDisr": cfprApComputeFwSyncAckDisr,
       "cfprApComputeFwSyncAckIgnoreCap": cfprApComputeFwSyncAckIgnoreCap,
       "cfprApComputeFwSyncAckIntId": cfprApComputeFwSyncAckIntId,
       "cfprApComputeFwSyncAckModified": cfprApComputeFwSyncAckModified,
       "cfprApComputeFwSyncAckName": cfprApComputeFwSyncAckName,
       "cfprApComputeFwSyncAckOperScheduler": cfprApComputeFwSyncAckOperScheduler,
       "cfprApComputeFwSyncAckOperState": cfprApComputeFwSyncAckOperState,
       "cfprApComputeFwSyncAckPolicyLevel": cfprApComputeFwSyncAckPolicyLevel,
       "cfprApComputeFwSyncAckPolicyOwner": cfprApComputeFwSyncAckPolicyOwner,
       "cfprApComputeFwSyncAckPrevOperState": cfprApComputeFwSyncAckPrevOperState,
       "cfprApComputeFwSyncAckScheduler": cfprApComputeFwSyncAckScheduler,
       "cfprApComputeHealthLedSensorAlarmTable": cfprApComputeHealthLedSensorAlarmTable,
       "cfprApComputeHealthLedSensorAlarmEntry": cfprApComputeHealthLedSensorAlarmEntry,
       "cfprApComputeHealthLedSensorAlarmInstanceId": cfprApComputeHealthLedSensorAlarmInstanceId,
       "cfprApComputeHealthLedSensorAlarmDn": cfprApComputeHealthLedSensorAlarmDn,
       "cfprApComputeHealthLedSensorAlarmRn": cfprApComputeHealthLedSensorAlarmRn,
       "cfprApComputeHealthLedSensorAlarmAlarmDesc": cfprApComputeHealthLedSensorAlarmAlarmDesc,
       "cfprApComputeHealthLedSensorAlarmAlarmSeverity": cfprApComputeHealthLedSensorAlarmAlarmSeverity,
       "cfprApComputeHealthLedSensorAlarmSensorId": cfprApComputeHealthLedSensorAlarmSensorId,
       "cfprApComputeHealthLedSensorAlarmSensorName": cfprApComputeHealthLedSensorAlarmSensorName,
       "cfprApComputeIOHubTable": cfprApComputeIOHubTable,
       "cfprApComputeIOHubEntry": cfprApComputeIOHubEntry,
       "cfprApComputeIOHubInstanceId": cfprApComputeIOHubInstanceId,
       "cfprApComputeIOHubDn": cfprApComputeIOHubDn,
       "cfprApComputeIOHubRn": cfprApComputeIOHubRn,
       "cfprApComputeIOHubId": cfprApComputeIOHubId,
       "cfprApComputeIOHubLocationDn": cfprApComputeIOHubLocationDn,
       "cfprApComputeIOHubModel": cfprApComputeIOHubModel,
       "cfprApComputeIOHubOperQualifierReason": cfprApComputeIOHubOperQualifierReason,
       "cfprApComputeIOHubOperState": cfprApComputeIOHubOperState,
       "cfprApComputeIOHubOperability": cfprApComputeIOHubOperability,
       "cfprApComputeIOHubPerf": cfprApComputeIOHubPerf,
       "cfprApComputeIOHubPower": cfprApComputeIOHubPower,
       "cfprApComputeIOHubPresence": cfprApComputeIOHubPresence,
       "cfprApComputeIOHubRevision": cfprApComputeIOHubRevision,
       "cfprApComputeIOHubSerial": cfprApComputeIOHubSerial,
       "cfprApComputeIOHubThermal": cfprApComputeIOHubThermal,
       "cfprApComputeIOHubVendor": cfprApComputeIOHubVendor,
       "cfprApComputeIOHubVoltage": cfprApComputeIOHubVoltage,
       "cfprApComputeIOHubEnvStatsTable": cfprApComputeIOHubEnvStatsTable,
       "cfprApComputeIOHubEnvStatsEntry": cfprApComputeIOHubEnvStatsEntry,
       "cfprApComputeIOHubEnvStatsInstanceId": cfprApComputeIOHubEnvStatsInstanceId,
       "cfprApComputeIOHubEnvStatsDn": cfprApComputeIOHubEnvStatsDn,
       "cfprApComputeIOHubEnvStatsRn": cfprApComputeIOHubEnvStatsRn,
       "cfprApComputeIOHubEnvStatsIntervals": cfprApComputeIOHubEnvStatsIntervals,
       "cfprApComputeIOHubEnvStatsSuspect": cfprApComputeIOHubEnvStatsSuspect,
       "cfprApComputeIOHubEnvStatsTemperature": cfprApComputeIOHubEnvStatsTemperature,
       "cfprApComputeIOHubEnvStatsTemperatureAvg": cfprApComputeIOHubEnvStatsTemperatureAvg,
       "cfprApComputeIOHubEnvStatsTemperatureMax": cfprApComputeIOHubEnvStatsTemperatureMax,
       "cfprApComputeIOHubEnvStatsTemperatureMin": cfprApComputeIOHubEnvStatsTemperatureMin,
       "cfprApComputeIOHubEnvStatsThresholded": cfprApComputeIOHubEnvStatsThresholded,
       "cfprApComputeIOHubEnvStatsTimeCollected": cfprApComputeIOHubEnvStatsTimeCollected,
       "cfprApComputeIOHubEnvStatsUpdate": cfprApComputeIOHubEnvStatsUpdate,
       "cfprApComputeIOHubEnvStatsHistTable": cfprApComputeIOHubEnvStatsHistTable,
       "cfprApComputeIOHubEnvStatsHistEntry": cfprApComputeIOHubEnvStatsHistEntry,
       "cfprApComputeIOHubEnvStatsHistInstanceId": cfprApComputeIOHubEnvStatsHistInstanceId,
       "cfprApComputeIOHubEnvStatsHistDn": cfprApComputeIOHubEnvStatsHistDn,
       "cfprApComputeIOHubEnvStatsHistRn": cfprApComputeIOHubEnvStatsHistRn,
       "cfprApComputeIOHubEnvStatsHistId": cfprApComputeIOHubEnvStatsHistId,
       "cfprApComputeIOHubEnvStatsHistMostRecent": cfprApComputeIOHubEnvStatsHistMostRecent,
       "cfprApComputeIOHubEnvStatsHistSuspect": cfprApComputeIOHubEnvStatsHistSuspect,
       "cfprApComputeIOHubEnvStatsHistTemperature": cfprApComputeIOHubEnvStatsHistTemperature,
       "cfprApComputeIOHubEnvStatsHistTemperatureAvg": cfprApComputeIOHubEnvStatsHistTemperatureAvg,
       "cfprApComputeIOHubEnvStatsHistTemperatureMax": cfprApComputeIOHubEnvStatsHistTemperatureMax,
       "cfprApComputeIOHubEnvStatsHistTemperatureMin": cfprApComputeIOHubEnvStatsHistTemperatureMin,
       "cfprApComputeIOHubEnvStatsHistThresholded": cfprApComputeIOHubEnvStatsHistThresholded,
       "cfprApComputeIOHubEnvStatsHistTimeCollected": cfprApComputeIOHubEnvStatsHistTimeCollected,
       "cfprApComputeMbPowerStatsTable": cfprApComputeMbPowerStatsTable,
       "cfprApComputeMbPowerStatsEntry": cfprApComputeMbPowerStatsEntry,
       "cfprApComputeMbPowerStatsInstanceId": cfprApComputeMbPowerStatsInstanceId,
       "cfprApComputeMbPowerStatsDn": cfprApComputeMbPowerStatsDn,
       "cfprApComputeMbPowerStatsRn": cfprApComputeMbPowerStatsRn,
       "cfprApComputeMbPowerStatsConsumedPower": cfprApComputeMbPowerStatsConsumedPower,
       "cfprApComputeMbPowerStatsConsumedPowerAvg": cfprApComputeMbPowerStatsConsumedPowerAvg,
       "cfprApComputeMbPowerStatsConsumedPowerMax": cfprApComputeMbPowerStatsConsumedPowerMax,
       "cfprApComputeMbPowerStatsConsumedPowerMin": cfprApComputeMbPowerStatsConsumedPowerMin,
       "cfprApComputeMbPowerStatsInputCurrent": cfprApComputeMbPowerStatsInputCurrent,
       "cfprApComputeMbPowerStatsInputCurrentAvg": cfprApComputeMbPowerStatsInputCurrentAvg,
       "cfprApComputeMbPowerStatsInputCurrentMax": cfprApComputeMbPowerStatsInputCurrentMax,
       "cfprApComputeMbPowerStatsInputCurrentMin": cfprApComputeMbPowerStatsInputCurrentMin,
       "cfprApComputeMbPowerStatsInputVoltage": cfprApComputeMbPowerStatsInputVoltage,
       "cfprApComputeMbPowerStatsInputVoltageAvg": cfprApComputeMbPowerStatsInputVoltageAvg,
       "cfprApComputeMbPowerStatsInputVoltageMax": cfprApComputeMbPowerStatsInputVoltageMax,
       "cfprApComputeMbPowerStatsInputVoltageMin": cfprApComputeMbPowerStatsInputVoltageMin,
       "cfprApComputeMbPowerStatsIntervals": cfprApComputeMbPowerStatsIntervals,
       "cfprApComputeMbPowerStatsSuspect": cfprApComputeMbPowerStatsSuspect,
       "cfprApComputeMbPowerStatsThresholded": cfprApComputeMbPowerStatsThresholded,
       "cfprApComputeMbPowerStatsTimeCollected": cfprApComputeMbPowerStatsTimeCollected,
       "cfprApComputeMbPowerStatsUpdate": cfprApComputeMbPowerStatsUpdate,
       "cfprApComputeMbPowerStatsHistTable": cfprApComputeMbPowerStatsHistTable,
       "cfprApComputeMbPowerStatsHistEntry": cfprApComputeMbPowerStatsHistEntry,
       "cfprApComputeMbPowerStatsHistInstanceId": cfprApComputeMbPowerStatsHistInstanceId,
       "cfprApComputeMbPowerStatsHistDn": cfprApComputeMbPowerStatsHistDn,
       "cfprApComputeMbPowerStatsHistRn": cfprApComputeMbPowerStatsHistRn,
       "cfprApComputeMbPowerStatsHistConsumedPower": cfprApComputeMbPowerStatsHistConsumedPower,
       "cfprApComputeMbPowerStatsHistConsumedPowerAvg": cfprApComputeMbPowerStatsHistConsumedPowerAvg,
       "cfprApComputeMbPowerStatsHistConsumedPowerMax": cfprApComputeMbPowerStatsHistConsumedPowerMax,
       "cfprApComputeMbPowerStatsHistConsumedPowerMin": cfprApComputeMbPowerStatsHistConsumedPowerMin,
       "cfprApComputeMbPowerStatsHistId": cfprApComputeMbPowerStatsHistId,
       "cfprApComputeMbPowerStatsHistInputCurrent": cfprApComputeMbPowerStatsHistInputCurrent,
       "cfprApComputeMbPowerStatsHistInputCurrentAvg": cfprApComputeMbPowerStatsHistInputCurrentAvg,
       "cfprApComputeMbPowerStatsHistInputCurrentMax": cfprApComputeMbPowerStatsHistInputCurrentMax,
       "cfprApComputeMbPowerStatsHistInputCurrentMin": cfprApComputeMbPowerStatsHistInputCurrentMin,
       "cfprApComputeMbPowerStatsHistInputVoltage": cfprApComputeMbPowerStatsHistInputVoltage,
       "cfprApComputeMbPowerStatsHistInputVoltageAvg": cfprApComputeMbPowerStatsHistInputVoltageAvg,
       "cfprApComputeMbPowerStatsHistInputVoltageMax": cfprApComputeMbPowerStatsHistInputVoltageMax,
       "cfprApComputeMbPowerStatsHistInputVoltageMin": cfprApComputeMbPowerStatsHistInputVoltageMin,
       "cfprApComputeMbPowerStatsHistMostRecent": cfprApComputeMbPowerStatsHistMostRecent,
       "cfprApComputeMbPowerStatsHistSuspect": cfprApComputeMbPowerStatsHistSuspect,
       "cfprApComputeMbPowerStatsHistThresholded": cfprApComputeMbPowerStatsHistThresholded,
       "cfprApComputeMbPowerStatsHistTimeCollected": cfprApComputeMbPowerStatsHistTimeCollected,
       "cfprApComputeMbTempStatsTable": cfprApComputeMbTempStatsTable,
       "cfprApComputeMbTempStatsEntry": cfprApComputeMbTempStatsEntry,
       "cfprApComputeMbTempStatsInstanceId": cfprApComputeMbTempStatsInstanceId,
       "cfprApComputeMbTempStatsDn": cfprApComputeMbTempStatsDn,
       "cfprApComputeMbTempStatsRn": cfprApComputeMbTempStatsRn,
       "cfprApComputeMbTempStatsFmTempSenIo": cfprApComputeMbTempStatsFmTempSenIo,
       "cfprApComputeMbTempStatsFmTempSenIoAvg": cfprApComputeMbTempStatsFmTempSenIoAvg,
       "cfprApComputeMbTempStatsFmTempSenIoMax": cfprApComputeMbTempStatsFmTempSenIoMax,
       "cfprApComputeMbTempStatsFmTempSenIoMin": cfprApComputeMbTempStatsFmTempSenIoMin,
       "cfprApComputeMbTempStatsFmTempSenRear": cfprApComputeMbTempStatsFmTempSenRear,
       "cfprApComputeMbTempStatsFmTempSenRearAvg": cfprApComputeMbTempStatsFmTempSenRearAvg,
       "cfprApComputeMbTempStatsFmTempSenRearL": cfprApComputeMbTempStatsFmTempSenRearL,
       "cfprApComputeMbTempStatsFmTempSenRearLAvg": cfprApComputeMbTempStatsFmTempSenRearLAvg,
       "cfprApComputeMbTempStatsFmTempSenRearLMax": cfprApComputeMbTempStatsFmTempSenRearLMax,
       "cfprApComputeMbTempStatsFmTempSenRearLMin": cfprApComputeMbTempStatsFmTempSenRearLMin,
       "cfprApComputeMbTempStatsFmTempSenRearMax": cfprApComputeMbTempStatsFmTempSenRearMax,
       "cfprApComputeMbTempStatsFmTempSenRearMin": cfprApComputeMbTempStatsFmTempSenRearMin,
       "cfprApComputeMbTempStatsFmTempSenRearR": cfprApComputeMbTempStatsFmTempSenRearR,
       "cfprApComputeMbTempStatsFmTempSenRearRAvg": cfprApComputeMbTempStatsFmTempSenRearRAvg,
       "cfprApComputeMbTempStatsFmTempSenRearRMax": cfprApComputeMbTempStatsFmTempSenRearRMax,
       "cfprApComputeMbTempStatsFmTempSenRearRMin": cfprApComputeMbTempStatsFmTempSenRearRMin,
       "cfprApComputeMbTempStatsIntervals": cfprApComputeMbTempStatsIntervals,
       "cfprApComputeMbTempStatsSuspect": cfprApComputeMbTempStatsSuspect,
       "cfprApComputeMbTempStatsThresholded": cfprApComputeMbTempStatsThresholded,
       "cfprApComputeMbTempStatsTimeCollected": cfprApComputeMbTempStatsTimeCollected,
       "cfprApComputeMbTempStatsUpdate": cfprApComputeMbTempStatsUpdate,
       "cfprApComputeMbTempStatsHistTable": cfprApComputeMbTempStatsHistTable,
       "cfprApComputeMbTempStatsHistEntry": cfprApComputeMbTempStatsHistEntry,
       "cfprApComputeMbTempStatsHistInstanceId": cfprApComputeMbTempStatsHistInstanceId,
       "cfprApComputeMbTempStatsHistDn": cfprApComputeMbTempStatsHistDn,
       "cfprApComputeMbTempStatsHistRn": cfprApComputeMbTempStatsHistRn,
       "cfprApComputeMbTempStatsHistFmTempSenIo": cfprApComputeMbTempStatsHistFmTempSenIo,
       "cfprApComputeMbTempStatsHistFmTempSenIoAvg": cfprApComputeMbTempStatsHistFmTempSenIoAvg,
       "cfprApComputeMbTempStatsHistFmTempSenIoMax": cfprApComputeMbTempStatsHistFmTempSenIoMax,
       "cfprApComputeMbTempStatsHistFmTempSenIoMin": cfprApComputeMbTempStatsHistFmTempSenIoMin,
       "cfprApComputeMbTempStatsHistFmTempSenRear": cfprApComputeMbTempStatsHistFmTempSenRear,
       "cfprApComputeMbTempStatsHistFmTempSenRearAvg": cfprApComputeMbTempStatsHistFmTempSenRearAvg,
       "cfprApComputeMbTempStatsHistFmTempSenRearL": cfprApComputeMbTempStatsHistFmTempSenRearL,
       "cfprApComputeMbTempStatsHistFmTempSenRearLAvg": cfprApComputeMbTempStatsHistFmTempSenRearLAvg,
       "cfprApComputeMbTempStatsHistFmTempSenRearLMax": cfprApComputeMbTempStatsHistFmTempSenRearLMax,
       "cfprApComputeMbTempStatsHistFmTempSenRearLMin": cfprApComputeMbTempStatsHistFmTempSenRearLMin,
       "cfprApComputeMbTempStatsHistFmTempSenRearMax": cfprApComputeMbTempStatsHistFmTempSenRearMax,
       "cfprApComputeMbTempStatsHistFmTempSenRearMin": cfprApComputeMbTempStatsHistFmTempSenRearMin,
       "cfprApComputeMbTempStatsHistFmTempSenRearR": cfprApComputeMbTempStatsHistFmTempSenRearR,
       "cfprApComputeMbTempStatsHistFmTempSenRearRAvg": cfprApComputeMbTempStatsHistFmTempSenRearRAvg,
       "cfprApComputeMbTempStatsHistFmTempSenRearRMax": cfprApComputeMbTempStatsHistFmTempSenRearRMax,
       "cfprApComputeMbTempStatsHistFmTempSenRearRMin": cfprApComputeMbTempStatsHistFmTempSenRearRMin,
       "cfprApComputeMbTempStatsHistId": cfprApComputeMbTempStatsHistId,
       "cfprApComputeMbTempStatsHistMostRecent": cfprApComputeMbTempStatsHistMostRecent,
       "cfprApComputeMbTempStatsHistSuspect": cfprApComputeMbTempStatsHistSuspect,
       "cfprApComputeMbTempStatsHistThresholded": cfprApComputeMbTempStatsHistThresholded,
       "cfprApComputeMbTempStatsHistTimeCollected": cfprApComputeMbTempStatsHistTimeCollected,
       "cfprApComputeMemoryConfigPolicyTable": cfprApComputeMemoryConfigPolicyTable,
       "cfprApComputeMemoryConfigPolicyEntry": cfprApComputeMemoryConfigPolicyEntry,
       "cfprApComputeMemoryConfigPolicyInstanceId": cfprApComputeMemoryConfigPolicyInstanceId,
       "cfprApComputeMemoryConfigPolicyDn": cfprApComputeMemoryConfigPolicyDn,
       "cfprApComputeMemoryConfigPolicyRn": cfprApComputeMemoryConfigPolicyRn,
       "cfprApComputeMemoryConfigPolicyBlackListing": cfprApComputeMemoryConfigPolicyBlackListing,
       "cfprApComputeMemoryConfigPolicyDescr": cfprApComputeMemoryConfigPolicyDescr,
       "cfprApComputeMemoryConfigPolicyIntId": cfprApComputeMemoryConfigPolicyIntId,
       "cfprApComputeMemoryConfigPolicyName": cfprApComputeMemoryConfigPolicyName,
       "cfprApComputeMemoryConfigPolicyPolicyLevel": cfprApComputeMemoryConfigPolicyPolicyLevel,
       "cfprApComputeMemoryConfigPolicyPolicyOwner": cfprApComputeMemoryConfigPolicyPolicyOwner,
       "cfprApComputeMemoryConfigurationTable": cfprApComputeMemoryConfigurationTable,
       "cfprApComputeMemoryConfigurationEntry": cfprApComputeMemoryConfigurationEntry,
       "cfprApComputeMemoryConfigurationInstanceId": cfprApComputeMemoryConfigurationInstanceId,
       "cfprApComputeMemoryConfigurationDn": cfprApComputeMemoryConfigurationDn,
       "cfprApComputeMemoryConfigurationRn": cfprApComputeMemoryConfigurationRn,
       "cfprApComputeMemoryConfigurationAdminMemoryState": cfprApComputeMemoryConfigurationAdminMemoryState,
       "cfprApComputeMemoryConfigurationBlackListing": cfprApComputeMemoryConfigurationBlackListing,
       "cfprApComputeMemoryUnitConstraintDefTable": cfprApComputeMemoryUnitConstraintDefTable,
       "cfprApComputeMemoryUnitConstraintDefEntry": cfprApComputeMemoryUnitConstraintDefEntry,
       "cfprApComputeMemoryUnitConstraintDefInstanceId": cfprApComputeMemoryUnitConstraintDefInstanceId,
       "cfprApComputeMemoryUnitConstraintDefDn": cfprApComputeMemoryUnitConstraintDefDn,
       "cfprApComputeMemoryUnitConstraintDefRn": cfprApComputeMemoryUnitConstraintDefRn,
       "cfprApComputeMemoryUnitConstraintDefDescr": cfprApComputeMemoryUnitConstraintDefDescr,
       "cfprApComputeMemoryUnitConstraintDefIntId": cfprApComputeMemoryUnitConstraintDefIntId,
       "cfprApComputeMemoryUnitConstraintDefName": cfprApComputeMemoryUnitConstraintDefName,
       "cfprApComputeMemoryUnitConstraintDefPolicyLevel": cfprApComputeMemoryUnitConstraintDefPolicyLevel,
       "cfprApComputeMemoryUnitConstraintDefPolicyOwner": cfprApComputeMemoryUnitConstraintDefPolicyOwner,
       "cfprApComputeMemoryUnitConstraintDefRevisionModifier": cfprApComputeMemoryUnitConstraintDefRevisionModifier,
       "cfprApComputeMemoryUnitConstraintDefType": cfprApComputeMemoryUnitConstraintDefType,
       "cfprApComputeNpuTable": cfprApComputeNpuTable,
       "cfprApComputeNpuEntry": cfprApComputeNpuEntry,
       "cfprApComputeNpuInstanceId": cfprApComputeNpuInstanceId,
       "cfprApComputeNpuDn": cfprApComputeNpuDn,
       "cfprApComputeNpuRn": cfprApComputeNpuRn,
       "cfprApComputeNpuId": cfprApComputeNpuId,
       "cfprApComputeNpuLocationDn": cfprApComputeNpuLocationDn,
       "cfprApComputeNpuModel": cfprApComputeNpuModel,
       "cfprApComputeNpuOperQualifierReason": cfprApComputeNpuOperQualifierReason,
       "cfprApComputeNpuOperState": cfprApComputeNpuOperState,
       "cfprApComputeNpuOperability": cfprApComputeNpuOperability,
       "cfprApComputeNpuPerf": cfprApComputeNpuPerf,
       "cfprApComputeNpuPower": cfprApComputeNpuPower,
       "cfprApComputeNpuPresence": cfprApComputeNpuPresence,
       "cfprApComputeNpuRevision": cfprApComputeNpuRevision,
       "cfprApComputeNpuSerial": cfprApComputeNpuSerial,
       "cfprApComputeNpuThermal": cfprApComputeNpuThermal,
       "cfprApComputeNpuVendor": cfprApComputeNpuVendor,
       "cfprApComputeNpuVoltage": cfprApComputeNpuVoltage,
       "cfprApComputePCIeFatalCompletionStatsTable": cfprApComputePCIeFatalCompletionStatsTable,
       "cfprApComputePCIeFatalCompletionStatsEntry": cfprApComputePCIeFatalCompletionStatsEntry,
       "cfprApComputePCIeFatalCompletionStatsInstanceId": cfprApComputePCIeFatalCompletionStatsInstanceId,
       "cfprApComputePCIeFatalCompletionStatsDn": cfprApComputePCIeFatalCompletionStatsDn,
       "cfprApComputePCIeFatalCompletionStatsRn": cfprApComputePCIeFatalCompletionStatsRn,
       "cfprApComputePCIeFatalCompletionStatsAbortErrors": cfprApComputePCIeFatalCompletionStatsAbortErrors,
       "cfprApComputePCIeFatalCompletionStatsAbortErrors15Min": cfprApComputePCIeFatalCompletionStatsAbortErrors15Min,
       "cfprApComputePCIeFatalCompletionStatsAbortErrors15MinH": cfprApComputePCIeFatalCompletionStatsAbortErrors15MinH,
       "cfprApComputePCIeFatalCompletionStatsAbortErrors1Day": cfprApComputePCIeFatalCompletionStatsAbortErrors1Day,
       "cfprApComputePCIeFatalCompletionStatsAbortErrors1DayH": cfprApComputePCIeFatalCompletionStatsAbortErrors1DayH,
       "cfprApComputePCIeFatalCompletionStatsAbortErrors1Hour": cfprApComputePCIeFatalCompletionStatsAbortErrors1Hour,
       "cfprApComputePCIeFatalCompletionStatsAbortErrors1HourH": cfprApComputePCIeFatalCompletionStatsAbortErrors1HourH,
       "cfprApComputePCIeFatalCompletionStatsAbortErrors1Week": cfprApComputePCIeFatalCompletionStatsAbortErrors1Week,
       "cfprApComputePCIeFatalCompletionStatsAbortErrors1WeekH": cfprApComputePCIeFatalCompletionStatsAbortErrors1WeekH,
       "cfprApComputePCIeFatalCompletionStatsAbortErrors2Weeks": cfprApComputePCIeFatalCompletionStatsAbortErrors2Weeks,
       "cfprApComputePCIeFatalCompletionStatsAbortErrors2WeeksH": cfprApComputePCIeFatalCompletionStatsAbortErrors2WeeksH,
       "cfprApComputePCIeFatalCompletionStatsTimeoutErrors": cfprApComputePCIeFatalCompletionStatsTimeoutErrors,
       "cfprApComputePCIeFatalCompletionStatsTimeoutErrors15Min": cfprApComputePCIeFatalCompletionStatsTimeoutErrors15Min,
       "cfprApComputePCIeFatalCompletionStatsTimeoutErrors15MinH": cfprApComputePCIeFatalCompletionStatsTimeoutErrors15MinH,
       "cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Day": cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Day,
       "cfprApComputePCIeFatalCompletionStatsTimeoutErrors1DayH": cfprApComputePCIeFatalCompletionStatsTimeoutErrors1DayH,
       "cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Hour": cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Hour,
       "cfprApComputePCIeFatalCompletionStatsTimeoutErrors1HourH": cfprApComputePCIeFatalCompletionStatsTimeoutErrors1HourH,
       "cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Week": cfprApComputePCIeFatalCompletionStatsTimeoutErrors1Week,
       "cfprApComputePCIeFatalCompletionStatsTimeoutErrors1WeekH": cfprApComputePCIeFatalCompletionStatsTimeoutErrors1WeekH,
       "cfprApComputePCIeFatalCompletionStatsTimeoutErrors2Weeks": cfprApComputePCIeFatalCompletionStatsTimeoutErrors2Weeks,
       "cfprApComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH": cfprApComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH,
       "cfprApComputePCIeFatalCompletionStatsIntervals": cfprApComputePCIeFatalCompletionStatsIntervals,
       "cfprApComputePCIeFatalCompletionStatsSuspect": cfprApComputePCIeFatalCompletionStatsSuspect,
       "cfprApComputePCIeFatalCompletionStatsThresholded": cfprApComputePCIeFatalCompletionStatsThresholded,
       "cfprApComputePCIeFatalCompletionStatsTimeCollected": cfprApComputePCIeFatalCompletionStatsTimeCollected,
       "cfprApComputePCIeFatalCompletionStatsUnexpectedErrors": cfprApComputePCIeFatalCompletionStatsUnexpectedErrors,
       "cfprApComputePCIeFatalCompletionStatsUnexpectedErrors15Min": cfprApComputePCIeFatalCompletionStatsUnexpectedErrors15Min,
       "cfprApComputePCIeFatalCompletionStatsUnexpectedErrors15MinH": cfprApComputePCIeFatalCompletionStatsUnexpectedErrors15MinH,
       "cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Day": cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Day,
       "cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1DayH": cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1DayH,
       "cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Hour": cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Hour,
       "cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1HourH": cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1HourH,
       "cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Week": cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1Week,
       "cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH": cfprApComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH,
       "cfprApComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks": cfprApComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks,
       "cfprApComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH": cfprApComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH,
       "cfprApComputePCIeFatalCompletionStatsUpdate": cfprApComputePCIeFatalCompletionStatsUpdate,
       "cfprApComputePCIeFatalProtocolStatsTable": cfprApComputePCIeFatalProtocolStatsTable,
       "cfprApComputePCIeFatalProtocolStatsEntry": cfprApComputePCIeFatalProtocolStatsEntry,
       "cfprApComputePCIeFatalProtocolStatsInstanceId": cfprApComputePCIeFatalProtocolStatsInstanceId,
       "cfprApComputePCIeFatalProtocolStatsDn": cfprApComputePCIeFatalProtocolStatsDn,
       "cfprApComputePCIeFatalProtocolStatsRn": cfprApComputePCIeFatalProtocolStatsRn,
       "cfprApComputePCIeFatalProtocolStatsDllpErrors": cfprApComputePCIeFatalProtocolStatsDllpErrors,
       "cfprApComputePCIeFatalProtocolStatsDllpErrors15Min": cfprApComputePCIeFatalProtocolStatsDllpErrors15Min,
       "cfprApComputePCIeFatalProtocolStatsDllpErrors15MinH": cfprApComputePCIeFatalProtocolStatsDllpErrors15MinH,
       "cfprApComputePCIeFatalProtocolStatsDllpErrors1Day": cfprApComputePCIeFatalProtocolStatsDllpErrors1Day,
       "cfprApComputePCIeFatalProtocolStatsDllpErrors1DayH": cfprApComputePCIeFatalProtocolStatsDllpErrors1DayH,
       "cfprApComputePCIeFatalProtocolStatsDllpErrors1Hour": cfprApComputePCIeFatalProtocolStatsDllpErrors1Hour,
       "cfprApComputePCIeFatalProtocolStatsDllpErrors1HourH": cfprApComputePCIeFatalProtocolStatsDllpErrors1HourH,
       "cfprApComputePCIeFatalProtocolStatsDllpErrors1Week": cfprApComputePCIeFatalProtocolStatsDllpErrors1Week,
       "cfprApComputePCIeFatalProtocolStatsDllpErrors1WeekH": cfprApComputePCIeFatalProtocolStatsDllpErrors1WeekH,
       "cfprApComputePCIeFatalProtocolStatsDllpErrors2Weeks": cfprApComputePCIeFatalProtocolStatsDllpErrors2Weeks,
       "cfprApComputePCIeFatalProtocolStatsDllpErrors2WeeksH": cfprApComputePCIeFatalProtocolStatsDllpErrors2WeeksH,
       "cfprApComputePCIeFatalProtocolStatsFlowControlErrors": cfprApComputePCIeFatalProtocolStatsFlowControlErrors,
       "cfprApComputePCIeFatalProtocolStatsFlowControlErrors15Min": cfprApComputePCIeFatalProtocolStatsFlowControlErrors15Min,
       "cfprApComputePCIeFatalProtocolStatsFlowControlErrors15MinH": cfprApComputePCIeFatalProtocolStatsFlowControlErrors15MinH,
       "cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Day": cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Day,
       "cfprApComputePCIeFatalProtocolStatsFlowControlErrors1DayH": cfprApComputePCIeFatalProtocolStatsFlowControlErrors1DayH,
       "cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Hour": cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Hour,
       "cfprApComputePCIeFatalProtocolStatsFlowControlErrors1HourH": cfprApComputePCIeFatalProtocolStatsFlowControlErrors1HourH,
       "cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Week": cfprApComputePCIeFatalProtocolStatsFlowControlErrors1Week,
       "cfprApComputePCIeFatalProtocolStatsFlowControlErrors1WeekH": cfprApComputePCIeFatalProtocolStatsFlowControlErrors1WeekH,
       "cfprApComputePCIeFatalProtocolStatsFlowControlErrors2Weeks": cfprApComputePCIeFatalProtocolStatsFlowControlErrors2Weeks,
       "cfprApComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH": cfprApComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH,
       "cfprApComputePCIeFatalProtocolStatsIntervals": cfprApComputePCIeFatalProtocolStatsIntervals,
       "cfprApComputePCIeFatalProtocolStatsSuspect": cfprApComputePCIeFatalProtocolStatsSuspect,
       "cfprApComputePCIeFatalProtocolStatsThresholded": cfprApComputePCIeFatalProtocolStatsThresholded,
       "cfprApComputePCIeFatalProtocolStatsTimeCollected": cfprApComputePCIeFatalProtocolStatsTimeCollected,
       "cfprApComputePCIeFatalProtocolStatsUpdate": cfprApComputePCIeFatalProtocolStatsUpdate,
       "cfprApComputePCIeFatalReceiveStatsTable": cfprApComputePCIeFatalReceiveStatsTable,
       "cfprApComputePCIeFatalReceiveStatsEntry": cfprApComputePCIeFatalReceiveStatsEntry,
       "cfprApComputePCIeFatalReceiveStatsInstanceId": cfprApComputePCIeFatalReceiveStatsInstanceId,
       "cfprApComputePCIeFatalReceiveStatsDn": cfprApComputePCIeFatalReceiveStatsDn,
       "cfprApComputePCIeFatalReceiveStatsRn": cfprApComputePCIeFatalReceiveStatsRn,
       "cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors": cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors,
       "cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15Min": cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15Min,
       "cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH": cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH,
       "cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Day": cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Day,
       "cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH": cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH,
       "cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour": cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour,
       "cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH": cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH,
       "cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Week": cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1Week,
       "cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH": cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH,
       "cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks": cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks,
       "cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH": cfprApComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH,
       "cfprApComputePCIeFatalReceiveStatsErrFatalErrors": cfprApComputePCIeFatalReceiveStatsErrFatalErrors,
       "cfprApComputePCIeFatalReceiveStatsErrFatalErrors15Min": cfprApComputePCIeFatalReceiveStatsErrFatalErrors15Min,
       "cfprApComputePCIeFatalReceiveStatsErrFatalErrors15MinH": cfprApComputePCIeFatalReceiveStatsErrFatalErrors15MinH,
       "cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Day": cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Day,
       "cfprApComputePCIeFatalReceiveStatsErrFatalErrors1DayH": cfprApComputePCIeFatalReceiveStatsErrFatalErrors1DayH,
       "cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Hour": cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Hour,
       "cfprApComputePCIeFatalReceiveStatsErrFatalErrors1HourH": cfprApComputePCIeFatalReceiveStatsErrFatalErrors1HourH,
       "cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Week": cfprApComputePCIeFatalReceiveStatsErrFatalErrors1Week,
       "cfprApComputePCIeFatalReceiveStatsErrFatalErrors1WeekH": cfprApComputePCIeFatalReceiveStatsErrFatalErrors1WeekH,
       "cfprApComputePCIeFatalReceiveStatsErrFatalErrors2Weeks": cfprApComputePCIeFatalReceiveStatsErrFatalErrors2Weeks,
       "cfprApComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH": cfprApComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH,
       "cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors": cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors,
       "cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15Min": cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15Min,
       "cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH": cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH,
       "cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Day": cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Day,
       "cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH": cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH,
       "cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour": cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour,
       "cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH": cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH,
       "cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Week": cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1Week,
       "cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH": cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH,
       "cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks": cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks,
       "cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH": cfprApComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH,
       "cfprApComputePCIeFatalReceiveStatsIntervals": cfprApComputePCIeFatalReceiveStatsIntervals,
       "cfprApComputePCIeFatalReceiveStatsSuspect": cfprApComputePCIeFatalReceiveStatsSuspect,
       "cfprApComputePCIeFatalReceiveStatsThresholded": cfprApComputePCIeFatalReceiveStatsThresholded,
       "cfprApComputePCIeFatalReceiveStatsTimeCollected": cfprApComputePCIeFatalReceiveStatsTimeCollected,
       "cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors": cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors,
       "cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min": cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min,
       "cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH": cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH,
       "cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day": cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day,
       "cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH": cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH,
       "cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour": cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour,
       "cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH": cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH,
       "cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week": cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week,
       "cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH": cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH,
       "cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks": cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks,
       "cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH": cfprApComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH,
       "cfprApComputePCIeFatalReceiveStatsUpdate": cfprApComputePCIeFatalReceiveStatsUpdate,
       "cfprApComputePCIeFatalStatsTable": cfprApComputePCIeFatalStatsTable,
       "cfprApComputePCIeFatalStatsEntry": cfprApComputePCIeFatalStatsEntry,
       "cfprApComputePCIeFatalStatsInstanceId": cfprApComputePCIeFatalStatsInstanceId,
       "cfprApComputePCIeFatalStatsDn": cfprApComputePCIeFatalStatsDn,
       "cfprApComputePCIeFatalStatsRn": cfprApComputePCIeFatalStatsRn,
       "cfprApComputePCIeFatalStatsAcsViolationErrors": cfprApComputePCIeFatalStatsAcsViolationErrors,
       "cfprApComputePCIeFatalStatsAcsViolationErrors15Min": cfprApComputePCIeFatalStatsAcsViolationErrors15Min,
       "cfprApComputePCIeFatalStatsAcsViolationErrors15MinH": cfprApComputePCIeFatalStatsAcsViolationErrors15MinH,
       "cfprApComputePCIeFatalStatsAcsViolationErrors1Day": cfprApComputePCIeFatalStatsAcsViolationErrors1Day,
       "cfprApComputePCIeFatalStatsAcsViolationErrors1DayH": cfprApComputePCIeFatalStatsAcsViolationErrors1DayH,
       "cfprApComputePCIeFatalStatsAcsViolationErrors1Hour": cfprApComputePCIeFatalStatsAcsViolationErrors1Hour,
       "cfprApComputePCIeFatalStatsAcsViolationErrors1HourH": cfprApComputePCIeFatalStatsAcsViolationErrors1HourH,
       "cfprApComputePCIeFatalStatsAcsViolationErrors1Week": cfprApComputePCIeFatalStatsAcsViolationErrors1Week,
       "cfprApComputePCIeFatalStatsAcsViolationErrors1WeekH": cfprApComputePCIeFatalStatsAcsViolationErrors1WeekH,
       "cfprApComputePCIeFatalStatsAcsViolationErrors2Weeks": cfprApComputePCIeFatalStatsAcsViolationErrors2Weeks,
       "cfprApComputePCIeFatalStatsAcsViolationErrors2WeeksH": cfprApComputePCIeFatalStatsAcsViolationErrors2WeeksH,
       "cfprApComputePCIeFatalStatsIntervals": cfprApComputePCIeFatalStatsIntervals,
       "cfprApComputePCIeFatalStatsMalformedTLPErrors": cfprApComputePCIeFatalStatsMalformedTLPErrors,
       "cfprApComputePCIeFatalStatsMalformedTLPErrors15Min": cfprApComputePCIeFatalStatsMalformedTLPErrors15Min,
       "cfprApComputePCIeFatalStatsMalformedTLPErrors15MinH": cfprApComputePCIeFatalStatsMalformedTLPErrors15MinH,
       "cfprApComputePCIeFatalStatsMalformedTLPErrors1Day": cfprApComputePCIeFatalStatsMalformedTLPErrors1Day,
       "cfprApComputePCIeFatalStatsMalformedTLPErrors1DayH": cfprApComputePCIeFatalStatsMalformedTLPErrors1DayH,
       "cfprApComputePCIeFatalStatsMalformedTLPErrors1Hour": cfprApComputePCIeFatalStatsMalformedTLPErrors1Hour,
       "cfprApComputePCIeFatalStatsMalformedTLPErrors1HourH": cfprApComputePCIeFatalStatsMalformedTLPErrors1HourH,
       "cfprApComputePCIeFatalStatsMalformedTLPErrors1Week": cfprApComputePCIeFatalStatsMalformedTLPErrors1Week,
       "cfprApComputePCIeFatalStatsMalformedTLPErrors1WeekH": cfprApComputePCIeFatalStatsMalformedTLPErrors1WeekH,
       "cfprApComputePCIeFatalStatsMalformedTLPErrors2Weeks": cfprApComputePCIeFatalStatsMalformedTLPErrors2Weeks,
       "cfprApComputePCIeFatalStatsMalformedTLPErrors2WeeksH": cfprApComputePCIeFatalStatsMalformedTLPErrors2WeeksH,
       "cfprApComputePCIeFatalStatsPoisonedTLPErrors": cfprApComputePCIeFatalStatsPoisonedTLPErrors,
       "cfprApComputePCIeFatalStatsPoisonedTLPErrors15Min": cfprApComputePCIeFatalStatsPoisonedTLPErrors15Min,
       "cfprApComputePCIeFatalStatsPoisonedTLPErrors15MinH": cfprApComputePCIeFatalStatsPoisonedTLPErrors15MinH,
       "cfprApComputePCIeFatalStatsPoisonedTLPErrors1Day": cfprApComputePCIeFatalStatsPoisonedTLPErrors1Day,
       "cfprApComputePCIeFatalStatsPoisonedTLPErrors1DayH": cfprApComputePCIeFatalStatsPoisonedTLPErrors1DayH,
       "cfprApComputePCIeFatalStatsPoisonedTLPErrors1Hour": cfprApComputePCIeFatalStatsPoisonedTLPErrors1Hour,
       "cfprApComputePCIeFatalStatsPoisonedTLPErrors1HourH": cfprApComputePCIeFatalStatsPoisonedTLPErrors1HourH,
       "cfprApComputePCIeFatalStatsPoisonedTLPErrors1Week": cfprApComputePCIeFatalStatsPoisonedTLPErrors1Week,
       "cfprApComputePCIeFatalStatsPoisonedTLPErrors1WeekH": cfprApComputePCIeFatalStatsPoisonedTLPErrors1WeekH,
       "cfprApComputePCIeFatalStatsPoisonedTLPErrors2Weeks": cfprApComputePCIeFatalStatsPoisonedTLPErrors2Weeks,
       "cfprApComputePCIeFatalStatsPoisonedTLPErrors2WeeksH": cfprApComputePCIeFatalStatsPoisonedTLPErrors2WeeksH,
       "cfprApComputePCIeFatalStatsSurpriseLinkDownErrors": cfprApComputePCIeFatalStatsSurpriseLinkDownErrors,
       "cfprApComputePCIeFatalStatsSurpriseLinkDownErrors15Min": cfprApComputePCIeFatalStatsSurpriseLinkDownErrors15Min,
       "cfprApComputePCIeFatalStatsSurpriseLinkDownErrors15MinH": cfprApComputePCIeFatalStatsSurpriseLinkDownErrors15MinH,
       "cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Day": cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Day,
       "cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1DayH": cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1DayH,
       "cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Hour": cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Hour,
       "cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1HourH": cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1HourH,
       "cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Week": cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1Week,
       "cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH": cfprApComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH,
       "cfprApComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks": cfprApComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks,
       "cfprApComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH": cfprApComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH,
       "cfprApComputePCIeFatalStatsSuspect": cfprApComputePCIeFatalStatsSuspect,
       "cfprApComputePCIeFatalStatsThresholded": cfprApComputePCIeFatalStatsThresholded,
       "cfprApComputePCIeFatalStatsTimeCollected": cfprApComputePCIeFatalStatsTimeCollected,
       "cfprApComputePCIeFatalStatsUpdate": cfprApComputePCIeFatalStatsUpdate,
       "cfprApComputePciCapTable": cfprApComputePciCapTable,
       "cfprApComputePciCapEntry": cfprApComputePciCapEntry,
       "cfprApComputePciCapInstanceId": cfprApComputePciCapInstanceId,
       "cfprApComputePciCapDn": cfprApComputePciCapDn,
       "cfprApComputePciCapRn": cfprApComputePciCapRn,
       "cfprApComputePciCapMaxBusIdPerSlot": cfprApComputePciCapMaxBusIdPerSlot,
       "cfprApComputePciCapNumOfPhysSlots": cfprApComputePciCapNumOfPhysSlots,
       "cfprApComputePciCapOrder": cfprApComputePciCapOrder,
       "cfprApComputePciCapStartsWith": cfprApComputePciCapStartsWith,
       "cfprApComputePciSlotScanDefTable": cfprApComputePciSlotScanDefTable,
       "cfprApComputePciSlotScanDefEntry": cfprApComputePciSlotScanDefEntry,
       "cfprApComputePciSlotScanDefInstanceId": cfprApComputePciSlotScanDefInstanceId,
       "cfprApComputePciSlotScanDefDn": cfprApComputePciSlotScanDefDn,
       "cfprApComputePciSlotScanDefRn": cfprApComputePciSlotScanDefRn,
       "cfprApComputePciSlotScanDefDescr": cfprApComputePciSlotScanDefDescr,
       "cfprApComputePciSlotScanDefIntId": cfprApComputePciSlotScanDefIntId,
       "cfprApComputePciSlotScanDefName": cfprApComputePciSlotScanDefName,
       "cfprApComputePciSlotScanDefPolicyLevel": cfprApComputePciSlotScanDefPolicyLevel,
       "cfprApComputePciSlotScanDefPolicyOwner": cfprApComputePciSlotScanDefPolicyOwner,
       "cfprApComputePciSlotScanDefScanOrder": cfprApComputePciSlotScanDefScanOrder,
       "cfprApComputePciSlotScanDefSlotId": cfprApComputePciSlotScanDefSlotId,
       "cfprApComputePhysicalAssocCtxTable": cfprApComputePhysicalAssocCtxTable,
       "cfprApComputePhysicalAssocCtxEntry": cfprApComputePhysicalAssocCtxEntry,
       "cfprApComputePhysicalAssocCtxInstanceId": cfprApComputePhysicalAssocCtxInstanceId,
       "cfprApComputePhysicalAssocCtxDn": cfprApComputePhysicalAssocCtxDn,
       "cfprApComputePhysicalAssocCtxRn": cfprApComputePhysicalAssocCtxRn,
       "cfprApComputePhysicalAssocCtxFruCapDn": cfprApComputePhysicalAssocCtxFruCapDn,
       "cfprApComputePhysicalFsmTable": cfprApComputePhysicalFsmTable,
       "cfprApComputePhysicalFsmEntry": cfprApComputePhysicalFsmEntry,
       "cfprApComputePhysicalFsmInstanceId": cfprApComputePhysicalFsmInstanceId,
       "cfprApComputePhysicalFsmDn": cfprApComputePhysicalFsmDn,
       "cfprApComputePhysicalFsmRn": cfprApComputePhysicalFsmRn,
       "cfprApComputePhysicalFsmCompletionTime": cfprApComputePhysicalFsmCompletionTime,
       "cfprApComputePhysicalFsmCurrentFsm": cfprApComputePhysicalFsmCurrentFsm,
       "cfprApComputePhysicalFsmDescr": cfprApComputePhysicalFsmDescr,
       "cfprApComputePhysicalFsmFsmStatus": cfprApComputePhysicalFsmFsmStatus,
       "cfprApComputePhysicalFsmProgress": cfprApComputePhysicalFsmProgress,
       "cfprApComputePhysicalFsmRmtErrCode": cfprApComputePhysicalFsmRmtErrCode,
       "cfprApComputePhysicalFsmRmtErrDescr": cfprApComputePhysicalFsmRmtErrDescr,
       "cfprApComputePhysicalFsmRmtRslt": cfprApComputePhysicalFsmRmtRslt,
       "cfprApComputePhysicalFsmStageTable": cfprApComputePhysicalFsmStageTable,
       "cfprApComputePhysicalFsmStageEntry": cfprApComputePhysicalFsmStageEntry,
       "cfprApComputePhysicalFsmStageInstanceId": cfprApComputePhysicalFsmStageInstanceId,
       "cfprApComputePhysicalFsmStageDn": cfprApComputePhysicalFsmStageDn,
       "cfprApComputePhysicalFsmStageRn": cfprApComputePhysicalFsmStageRn,
       "cfprApComputePhysicalFsmStageDescr": cfprApComputePhysicalFsmStageDescr,
       "cfprApComputePhysicalFsmStageLastUpdateTime": cfprApComputePhysicalFsmStageLastUpdateTime,
       "cfprApComputePhysicalFsmStageName": cfprApComputePhysicalFsmStageName,
       "cfprApComputePhysicalFsmStageOrder": cfprApComputePhysicalFsmStageOrder,
       "cfprApComputePhysicalFsmStageRetry": cfprApComputePhysicalFsmStageRetry,
       "cfprApComputePhysicalFsmStageStageStatus": cfprApComputePhysicalFsmStageStageStatus,
       "cfprApComputePhysicalFsmTaskTable": cfprApComputePhysicalFsmTaskTable,
       "cfprApComputePhysicalFsmTaskEntry": cfprApComputePhysicalFsmTaskEntry,
       "cfprApComputePhysicalFsmTaskInstanceId": cfprApComputePhysicalFsmTaskInstanceId,
       "cfprApComputePhysicalFsmTaskDn": cfprApComputePhysicalFsmTaskDn,
       "cfprApComputePhysicalFsmTaskRn": cfprApComputePhysicalFsmTaskRn,
       "cfprApComputePhysicalFsmTaskCompletion": cfprApComputePhysicalFsmTaskCompletion,
       "cfprApComputePhysicalFsmTaskFlags": cfprApComputePhysicalFsmTaskFlags,
       "cfprApComputePhysicalFsmTaskItem": cfprApComputePhysicalFsmTaskItem,
       "cfprApComputePhysicalFsmTaskSeqId": cfprApComputePhysicalFsmTaskSeqId,
       "cfprApComputePhysicalQualTable": cfprApComputePhysicalQualTable,
       "cfprApComputePhysicalQualEntry": cfprApComputePhysicalQualEntry,
       "cfprApComputePhysicalQualInstanceId": cfprApComputePhysicalQualInstanceId,
       "cfprApComputePhysicalQualDn": cfprApComputePhysicalQualDn,
       "cfprApComputePhysicalQualRn": cfprApComputePhysicalQualRn,
       "cfprApComputePhysicalQualModel": cfprApComputePhysicalQualModel,
       "cfprApComputePlatformTable": cfprApComputePlatformTable,
       "cfprApComputePlatformEntry": cfprApComputePlatformEntry,
       "cfprApComputePlatformInstanceId": cfprApComputePlatformInstanceId,
       "cfprApComputePlatformDn": cfprApComputePlatformDn,
       "cfprApComputePlatformRn": cfprApComputePlatformRn,
       "cfprApComputePlatformModel": cfprApComputePlatformModel,
       "cfprApComputePlatformProductName": cfprApComputePlatformProductName,
       "cfprApComputePlatformRevision": cfprApComputePlatformRevision,
       "cfprApComputePlatformVendor": cfprApComputePlatformVendor,
       "cfprApComputePnuOSImageTable": cfprApComputePnuOSImageTable,
       "cfprApComputePnuOSImageEntry": cfprApComputePnuOSImageEntry,
       "cfprApComputePnuOSImageInstanceId": cfprApComputePnuOSImageInstanceId,
       "cfprApComputePnuOSImageDn": cfprApComputePnuOSImageDn,
       "cfprApComputePnuOSImageRn": cfprApComputePnuOSImageRn,
       "cfprApComputePnuOSImageImgLFBFFName": cfprApComputePnuOSImageImgLFBFFName,
       "cfprApComputePnuOSImageImgLoc": cfprApComputePnuOSImageImgLoc,
       "cfprApComputePnuOSImageImgName": cfprApComputePnuOSImageImgName,
       "cfprApComputePoolTable": cfprApComputePoolTable,
       "cfprApComputePoolEntry": cfprApComputePoolEntry,
       "cfprApComputePoolInstanceId": cfprApComputePoolInstanceId,
       "cfprApComputePoolDn": cfprApComputePoolDn,
       "cfprApComputePoolRn": cfprApComputePoolRn,
       "cfprApComputePoolAssigned": cfprApComputePoolAssigned,
       "cfprApComputePoolAssignmentOrder": cfprApComputePoolAssignmentOrder,
       "cfprApComputePoolDescr": cfprApComputePoolDescr,
       "cfprApComputePoolIntId": cfprApComputePoolIntId,
       "cfprApComputePoolName": cfprApComputePoolName,
       "cfprApComputePoolPolicyLevel": cfprApComputePoolPolicyLevel,
       "cfprApComputePoolPolicyOwner": cfprApComputePoolPolicyOwner,
       "cfprApComputePoolSize": cfprApComputePoolSize,
       "cfprApComputePoolPolicyRefTable": cfprApComputePoolPolicyRefTable,
       "cfprApComputePoolPolicyRefEntry": cfprApComputePoolPolicyRefEntry,
       "cfprApComputePoolPolicyRefInstanceId": cfprApComputePoolPolicyRefInstanceId,
       "cfprApComputePoolPolicyRefDn": cfprApComputePoolPolicyRefDn,
       "cfprApComputePoolPolicyRefRn": cfprApComputePoolPolicyRefRn,
       "cfprApComputePoolPolicyRefId": cfprApComputePoolPolicyRefId,
       "cfprApComputePoolPolicyRefPolicyDn": cfprApComputePoolPolicyRefPolicyDn,
       "cfprApComputePoolableTable": cfprApComputePoolableTable,
       "cfprApComputePoolableEntry": cfprApComputePoolableEntry,
       "cfprApComputePoolableInstanceId": cfprApComputePoolableInstanceId,
       "cfprApComputePoolableDn": cfprApComputePoolableDn,
       "cfprApComputePoolableRn": cfprApComputePoolableRn,
       "cfprApComputePoolableId": cfprApComputePoolableId,
       "cfprApComputePoolablePoolDn": cfprApComputePoolablePoolDn,
       "cfprApComputePooledRackUnitTable": cfprApComputePooledRackUnitTable,
       "cfprApComputePooledRackUnitEntry": cfprApComputePooledRackUnitEntry,
       "cfprApComputePooledRackUnitInstanceId": cfprApComputePooledRackUnitInstanceId,
       "cfprApComputePooledRackUnitDn": cfprApComputePooledRackUnitDn,
       "cfprApComputePooledRackUnitRn": cfprApComputePooledRackUnitRn,
       "cfprApComputePooledRackUnitAssigned": cfprApComputePooledRackUnitAssigned,
       "cfprApComputePooledRackUnitAssignedToDn": cfprApComputePooledRackUnitAssignedToDn,
       "cfprApComputePooledRackUnitId": cfprApComputePooledRackUnitId,
       "cfprApComputePooledRackUnitOwner": cfprApComputePooledRackUnitOwner,
       "cfprApComputePooledRackUnitPoolableDn": cfprApComputePooledRackUnitPoolableDn,
       "cfprApComputePooledRackUnitPrevAssignedToDn": cfprApComputePooledRackUnitPrevAssignedToDn,
       "cfprApComputePooledSlotTable": cfprApComputePooledSlotTable,
       "cfprApComputePooledSlotEntry": cfprApComputePooledSlotEntry,
       "cfprApComputePooledSlotInstanceId": cfprApComputePooledSlotInstanceId,
       "cfprApComputePooledSlotDn": cfprApComputePooledSlotDn,
       "cfprApComputePooledSlotRn": cfprApComputePooledSlotRn,
       "cfprApComputePooledSlotAssigned": cfprApComputePooledSlotAssigned,
       "cfprApComputePooledSlotAssignedToDn": cfprApComputePooledSlotAssignedToDn,
       "cfprApComputePooledSlotChassisId": cfprApComputePooledSlotChassisId,
       "cfprApComputePooledSlotOwner": cfprApComputePooledSlotOwner,
       "cfprApComputePooledSlotPoolableDn": cfprApComputePooledSlotPoolableDn,
       "cfprApComputePooledSlotPrevAssignedToDn": cfprApComputePooledSlotPrevAssignedToDn,
       "cfprApComputePooledSlotSlotId": cfprApComputePooledSlotSlotId,
       "cfprApComputePoolingPolicyTable": cfprApComputePoolingPolicyTable,
       "cfprApComputePoolingPolicyEntry": cfprApComputePoolingPolicyEntry,
       "cfprApComputePoolingPolicyInstanceId": cfprApComputePoolingPolicyInstanceId,
       "cfprApComputePoolingPolicyDn": cfprApComputePoolingPolicyDn,
       "cfprApComputePoolingPolicyRn": cfprApComputePoolingPolicyRn,
       "cfprApComputePoolingPolicyDescr": cfprApComputePoolingPolicyDescr,
       "cfprApComputePoolingPolicyIntId": cfprApComputePoolingPolicyIntId,
       "cfprApComputePoolingPolicyName": cfprApComputePoolingPolicyName,
       "cfprApComputePoolingPolicyPolicyLevel": cfprApComputePoolingPolicyPolicyLevel,
       "cfprApComputePoolingPolicyPolicyOwner": cfprApComputePoolingPolicyPolicyOwner,
       "cfprApComputePoolingPolicyPoolDn": cfprApComputePoolingPolicyPoolDn,
       "cfprApComputePoolingPolicyQualifier": cfprApComputePoolingPolicyQualifier,
       "cfprApComputePsuControlTable": cfprApComputePsuControlTable,
       "cfprApComputePsuControlEntry": cfprApComputePsuControlEntry,
       "cfprApComputePsuControlInstanceId": cfprApComputePsuControlInstanceId,
       "cfprApComputePsuControlDn": cfprApComputePsuControlDn,
       "cfprApComputePsuControlRn": cfprApComputePsuControlRn,
       "cfprApComputePsuControlClusterState": cfprApComputePsuControlClusterState,
       "cfprApComputePsuControlDescr": cfprApComputePsuControlDescr,
       "cfprApComputePsuControlInputPowerState": cfprApComputePsuControlInputPowerState,
       "cfprApComputePsuControlIntId": cfprApComputePsuControlIntId,
       "cfprApComputePsuControlName": cfprApComputePsuControlName,
       "cfprApComputePsuControlOperQualifier": cfprApComputePsuControlOperQualifier,
       "cfprApComputePsuControlOperState": cfprApComputePsuControlOperState,
       "cfprApComputePsuControlOutputPowerState": cfprApComputePsuControlOutputPowerState,
       "cfprApComputePsuControlPolicyLevel": cfprApComputePsuControlPolicyLevel,
       "cfprApComputePsuControlPolicyOwner": cfprApComputePsuControlPolicyOwner,
       "cfprApComputePsuControlRedundancy": cfprApComputePsuControlRedundancy,
       "cfprApComputePsuPolicyTable": cfprApComputePsuPolicyTable,
       "cfprApComputePsuPolicyEntry": cfprApComputePsuPolicyEntry,
       "cfprApComputePsuPolicyInstanceId": cfprApComputePsuPolicyInstanceId,
       "cfprApComputePsuPolicyDn": cfprApComputePsuPolicyDn,
       "cfprApComputePsuPolicyRn": cfprApComputePsuPolicyRn,
       "cfprApComputePsuPolicyDescr": cfprApComputePsuPolicyDescr,
       "cfprApComputePsuPolicyIntId": cfprApComputePsuPolicyIntId,
       "cfprApComputePsuPolicyName": cfprApComputePsuPolicyName,
       "cfprApComputePsuPolicyPolicyLevel": cfprApComputePsuPolicyPolicyLevel,
       "cfprApComputePsuPolicyPolicyOwner": cfprApComputePsuPolicyPolicyOwner,
       "cfprApComputePsuPolicyRedundancy": cfprApComputePsuPolicyRedundancy,
       "cfprApComputeQualTable": cfprApComputeQualTable,
       "cfprApComputeQualEntry": cfprApComputeQualEntry,
       "cfprApComputeQualInstanceId": cfprApComputeQualInstanceId,
       "cfprApComputeQualDn": cfprApComputeQualDn,
       "cfprApComputeQualRn": cfprApComputeQualRn,
       "cfprApComputeQualDescr": cfprApComputeQualDescr,
       "cfprApComputeQualIntId": cfprApComputeQualIntId,
       "cfprApComputeQualName": cfprApComputeQualName,
       "cfprApComputeQualPolicyLevel": cfprApComputeQualPolicyLevel,
       "cfprApComputeQualPolicyOwner": cfprApComputeQualPolicyOwner,
       "cfprApComputeRackQualTable": cfprApComputeRackQualTable,
       "cfprApComputeRackQualEntry": cfprApComputeRackQualEntry,
       "cfprApComputeRackQualInstanceId": cfprApComputeRackQualInstanceId,
       "cfprApComputeRackQualDn": cfprApComputeRackQualDn,
       "cfprApComputeRackQualRn": cfprApComputeRackQualRn,
       "cfprApComputeRackQualMaxId": cfprApComputeRackQualMaxId,
       "cfprApComputeRackQualMinId": cfprApComputeRackQualMinId,
       "cfprApComputeRackUnitTable": cfprApComputeRackUnitTable,
       "cfprApComputeRackUnitEntry": cfprApComputeRackUnitEntry,
       "cfprApComputeRackUnitInstanceId": cfprApComputeRackUnitInstanceId,
       "cfprApComputeRackUnitDn": cfprApComputeRackUnitDn,
       "cfprApComputeRackUnitRn": cfprApComputeRackUnitRn,
       "cfprApComputeRackUnitAdminPower": cfprApComputeRackUnitAdminPower,
       "cfprApComputeRackUnitAdminState": cfprApComputeRackUnitAdminState,
       "cfprApComputeRackUnitAssignedToDn": cfprApComputeRackUnitAssignedToDn,
       "cfprApComputeRackUnitAssociation": cfprApComputeRackUnitAssociation,
       "cfprApComputeRackUnitAvailability": cfprApComputeRackUnitAvailability,
       "cfprApComputeRackUnitAvailableMemory": cfprApComputeRackUnitAvailableMemory,
       "cfprApComputeRackUnitCheckPoint": cfprApComputeRackUnitCheckPoint,
       "cfprApComputeRackUnitConnPath": cfprApComputeRackUnitConnPath,
       "cfprApComputeRackUnitConnStatus": cfprApComputeRackUnitConnStatus,
       "cfprApComputeRackUnitDescr": cfprApComputeRackUnitDescr,
       "cfprApComputeRackUnitDiscovery": cfprApComputeRackUnitDiscovery,
       "cfprApComputeRackUnitFltAggr": cfprApComputeRackUnitFltAggr,
       "cfprApComputeRackUnitFsmDescr": cfprApComputeRackUnitFsmDescr,
       "cfprApComputeRackUnitFsmPrev": cfprApComputeRackUnitFsmPrev,
       "cfprApComputeRackUnitFsmProgr": cfprApComputeRackUnitFsmProgr,
       "cfprApComputeRackUnitFsmRmtInvErrCode": cfprApComputeRackUnitFsmRmtInvErrCode,
       "cfprApComputeRackUnitFsmRmtInvErrDescr": cfprApComputeRackUnitFsmRmtInvErrDescr,
       "cfprApComputeRackUnitFsmRmtInvRslt": cfprApComputeRackUnitFsmRmtInvRslt,
       "cfprApComputeRackUnitFsmStageDescr": cfprApComputeRackUnitFsmStageDescr,
       "cfprApComputeRackUnitFsmStamp": cfprApComputeRackUnitFsmStamp,
       "cfprApComputeRackUnitFsmStatus": cfprApComputeRackUnitFsmStatus,
       "cfprApComputeRackUnitFsmTry": cfprApComputeRackUnitFsmTry,
       "cfprApComputeRackUnitId": cfprApComputeRackUnitId,
       "cfprApComputeRackUnitIntId": cfprApComputeRackUnitIntId,
       "cfprApComputeRackUnitLc": cfprApComputeRackUnitLc,
       "cfprApComputeRackUnitLcTs": cfprApComputeRackUnitLcTs,
       "cfprApComputeRackUnitLocalId": cfprApComputeRackUnitLocalId,
       "cfprApComputeRackUnitLowVoltageMemory": cfprApComputeRackUnitLowVoltageMemory,
       "cfprApComputeRackUnitManagingInst": cfprApComputeRackUnitManagingInst,
       "cfprApComputeRackUnitMemorySpeed": cfprApComputeRackUnitMemorySpeed,
       "cfprApComputeRackUnitMfgTime": cfprApComputeRackUnitMfgTime,
       "cfprApComputeRackUnitModel": cfprApComputeRackUnitModel,
       "cfprApComputeRackUnitName": cfprApComputeRackUnitName,
       "cfprApComputeRackUnitNumOfAdaptors": cfprApComputeRackUnitNumOfAdaptors,
       "cfprApComputeRackUnitNumOfCores": cfprApComputeRackUnitNumOfCores,
       "cfprApComputeRackUnitNumOfCoresEnabled": cfprApComputeRackUnitNumOfCoresEnabled,
       "cfprApComputeRackUnitNumOfCpus": cfprApComputeRackUnitNumOfCpus,
       "cfprApComputeRackUnitNumOfEthHostIfs": cfprApComputeRackUnitNumOfEthHostIfs,
       "cfprApComputeRackUnitNumOfFcHostIfs": cfprApComputeRackUnitNumOfFcHostIfs,
       "cfprApComputeRackUnitNumOfThreads": cfprApComputeRackUnitNumOfThreads,
       "cfprApComputeRackUnitOperPower": cfprApComputeRackUnitOperPower,
       "cfprApComputeRackUnitOperQualifier": cfprApComputeRackUnitOperQualifier,
       "cfprApComputeRackUnitOperState": cfprApComputeRackUnitOperState,
       "cfprApComputeRackUnitOperability": cfprApComputeRackUnitOperability,
       "cfprApComputeRackUnitOriginalUuid": cfprApComputeRackUnitOriginalUuid,
       "cfprApComputeRackUnitPartNumber": cfprApComputeRackUnitPartNumber,
       "cfprApComputeRackUnitPolicyLevel": cfprApComputeRackUnitPolicyLevel,
       "cfprApComputeRackUnitPolicyOwner": cfprApComputeRackUnitPolicyOwner,
       "cfprApComputeRackUnitPresence": cfprApComputeRackUnitPresence,
       "cfprApComputeRackUnitRevision": cfprApComputeRackUnitRevision,
       "cfprApComputeRackUnitSerial": cfprApComputeRackUnitSerial,
       "cfprApComputeRackUnitServerId": cfprApComputeRackUnitServerId,
       "cfprApComputeRackUnitTotalMemory": cfprApComputeRackUnitTotalMemory,
       "cfprApComputeRackUnitUsrLbl": cfprApComputeRackUnitUsrLbl,
       "cfprApComputeRackUnitUuid": cfprApComputeRackUnitUuid,
       "cfprApComputeRackUnitVendor": cfprApComputeRackUnitVendor,
       "cfprApComputeRackUnitVersionHolder": cfprApComputeRackUnitVersionHolder,
       "cfprApComputeRackUnitVid": cfprApComputeRackUnitVid,
       "cfprApComputeRackUnitFsmTable": cfprApComputeRackUnitFsmTable,
       "cfprApComputeRackUnitFsmEntry": cfprApComputeRackUnitFsmEntry,
       "cfprApComputeRackUnitFsmInstanceId": cfprApComputeRackUnitFsmInstanceId,
       "cfprApComputeRackUnitFsmDn": cfprApComputeRackUnitFsmDn,
       "cfprApComputeRackUnitFsmRn": cfprApComputeRackUnitFsmRn,
       "cfprApComputeRackUnitFsmCompletionTime": cfprApComputeRackUnitFsmCompletionTime,
       "cfprApComputeRackUnitFsmCurrentFsm": cfprApComputeRackUnitFsmCurrentFsm,
       "cfprApComputeRackUnitFsmDescrData": cfprApComputeRackUnitFsmDescrData,
       "cfprApComputeRackUnitFsmFsmStatus": cfprApComputeRackUnitFsmFsmStatus,
       "cfprApComputeRackUnitFsmProgress": cfprApComputeRackUnitFsmProgress,
       "cfprApComputeRackUnitFsmRmtErrCode": cfprApComputeRackUnitFsmRmtErrCode,
       "cfprApComputeRackUnitFsmRmtErrDescr": cfprApComputeRackUnitFsmRmtErrDescr,
       "cfprApComputeRackUnitFsmRmtRslt": cfprApComputeRackUnitFsmRmtRslt,
       "cfprApComputeRackUnitFsmStageTable": cfprApComputeRackUnitFsmStageTable,
       "cfprApComputeRackUnitFsmStageEntry": cfprApComputeRackUnitFsmStageEntry,
       "cfprApComputeRackUnitFsmStageInstanceId": cfprApComputeRackUnitFsmStageInstanceId,
       "cfprApComputeRackUnitFsmStageDn": cfprApComputeRackUnitFsmStageDn,
       "cfprApComputeRackUnitFsmStageRn": cfprApComputeRackUnitFsmStageRn,
       "cfprApComputeRackUnitFsmStageDescrData": cfprApComputeRackUnitFsmStageDescrData,
       "cfprApComputeRackUnitFsmStageLastUpdateTime": cfprApComputeRackUnitFsmStageLastUpdateTime,
       "cfprApComputeRackUnitFsmStageName": cfprApComputeRackUnitFsmStageName,
       "cfprApComputeRackUnitFsmStageOrder": cfprApComputeRackUnitFsmStageOrder,
       "cfprApComputeRackUnitFsmStageRetry": cfprApComputeRackUnitFsmStageRetry,
       "cfprApComputeRackUnitFsmStageStageStatus": cfprApComputeRackUnitFsmStageStageStatus,
       "cfprApComputeRackUnitMbTempStatsTable": cfprApComputeRackUnitMbTempStatsTable,
       "cfprApComputeRackUnitMbTempStatsEntry": cfprApComputeRackUnitMbTempStatsEntry,
       "cfprApComputeRackUnitMbTempStatsInstanceId": cfprApComputeRackUnitMbTempStatsInstanceId,
       "cfprApComputeRackUnitMbTempStatsDn": cfprApComputeRackUnitMbTempStatsDn,
       "cfprApComputeRackUnitMbTempStatsRn": cfprApComputeRackUnitMbTempStatsRn,
       "cfprApComputeRackUnitMbTempStatsAmbientTemp": cfprApComputeRackUnitMbTempStatsAmbientTemp,
       "cfprApComputeRackUnitMbTempStatsAmbientTempAvg": cfprApComputeRackUnitMbTempStatsAmbientTempAvg,
       "cfprApComputeRackUnitMbTempStatsAmbientTempMax": cfprApComputeRackUnitMbTempStatsAmbientTempMax,
       "cfprApComputeRackUnitMbTempStatsAmbientTempMin": cfprApComputeRackUnitMbTempStatsAmbientTempMin,
       "cfprApComputeRackUnitMbTempStatsFrontTemp": cfprApComputeRackUnitMbTempStatsFrontTemp,
       "cfprApComputeRackUnitMbTempStatsFrontTempAvg": cfprApComputeRackUnitMbTempStatsFrontTempAvg,
       "cfprApComputeRackUnitMbTempStatsFrontTempMax": cfprApComputeRackUnitMbTempStatsFrontTempMax,
       "cfprApComputeRackUnitMbTempStatsFrontTempMin": cfprApComputeRackUnitMbTempStatsFrontTempMin,
       "cfprApComputeRackUnitMbTempStatsIntervals": cfprApComputeRackUnitMbTempStatsIntervals,
       "cfprApComputeRackUnitMbTempStatsIoh1Temp": cfprApComputeRackUnitMbTempStatsIoh1Temp,
       "cfprApComputeRackUnitMbTempStatsIoh1TempAvg": cfprApComputeRackUnitMbTempStatsIoh1TempAvg,
       "cfprApComputeRackUnitMbTempStatsIoh1TempMax": cfprApComputeRackUnitMbTempStatsIoh1TempMax,
       "cfprApComputeRackUnitMbTempStatsIoh1TempMin": cfprApComputeRackUnitMbTempStatsIoh1TempMin,
       "cfprApComputeRackUnitMbTempStatsIoh2Temp": cfprApComputeRackUnitMbTempStatsIoh2Temp,
       "cfprApComputeRackUnitMbTempStatsIoh2TempAvg": cfprApComputeRackUnitMbTempStatsIoh2TempAvg,
       "cfprApComputeRackUnitMbTempStatsIoh2TempMax": cfprApComputeRackUnitMbTempStatsIoh2TempMax,
       "cfprApComputeRackUnitMbTempStatsIoh2TempMin": cfprApComputeRackUnitMbTempStatsIoh2TempMin,
       "cfprApComputeRackUnitMbTempStatsRearTemp": cfprApComputeRackUnitMbTempStatsRearTemp,
       "cfprApComputeRackUnitMbTempStatsRearTempAvg": cfprApComputeRackUnitMbTempStatsRearTempAvg,
       "cfprApComputeRackUnitMbTempStatsRearTempMax": cfprApComputeRackUnitMbTempStatsRearTempMax,
       "cfprApComputeRackUnitMbTempStatsRearTempMin": cfprApComputeRackUnitMbTempStatsRearTempMin,
       "cfprApComputeRackUnitMbTempStatsSuspect": cfprApComputeRackUnitMbTempStatsSuspect,
       "cfprApComputeRackUnitMbTempStatsThresholded": cfprApComputeRackUnitMbTempStatsThresholded,
       "cfprApComputeRackUnitMbTempStatsTimeCollected": cfprApComputeRackUnitMbTempStatsTimeCollected,
       "cfprApComputeRackUnitMbTempStatsUpdate": cfprApComputeRackUnitMbTempStatsUpdate,
       "cfprApComputeRackUnitMbTempStatsHistTable": cfprApComputeRackUnitMbTempStatsHistTable,
       "cfprApComputeRackUnitMbTempStatsHistEntry": cfprApComputeRackUnitMbTempStatsHistEntry,
       "cfprApComputeRackUnitMbTempStatsHistInstanceId": cfprApComputeRackUnitMbTempStatsHistInstanceId,
       "cfprApComputeRackUnitMbTempStatsHistDn": cfprApComputeRackUnitMbTempStatsHistDn,
       "cfprApComputeRackUnitMbTempStatsHistRn": cfprApComputeRackUnitMbTempStatsHistRn,
       "cfprApComputeRackUnitMbTempStatsHistAmbientTemp": cfprApComputeRackUnitMbTempStatsHistAmbientTemp,
       "cfprApComputeRackUnitMbTempStatsHistAmbientTempAvg": cfprApComputeRackUnitMbTempStatsHistAmbientTempAvg,
       "cfprApComputeRackUnitMbTempStatsHistAmbientTempMax": cfprApComputeRackUnitMbTempStatsHistAmbientTempMax,
       "cfprApComputeRackUnitMbTempStatsHistAmbientTempMin": cfprApComputeRackUnitMbTempStatsHistAmbientTempMin,
       "cfprApComputeRackUnitMbTempStatsHistFrontTemp": cfprApComputeRackUnitMbTempStatsHistFrontTemp,
       "cfprApComputeRackUnitMbTempStatsHistFrontTempAvg": cfprApComputeRackUnitMbTempStatsHistFrontTempAvg,
       "cfprApComputeRackUnitMbTempStatsHistFrontTempMax": cfprApComputeRackUnitMbTempStatsHistFrontTempMax,
       "cfprApComputeRackUnitMbTempStatsHistFrontTempMin": cfprApComputeRackUnitMbTempStatsHistFrontTempMin,
       "cfprApComputeRackUnitMbTempStatsHistId": cfprApComputeRackUnitMbTempStatsHistId,
       "cfprApComputeRackUnitMbTempStatsHistIoh1Temp": cfprApComputeRackUnitMbTempStatsHistIoh1Temp,
       "cfprApComputeRackUnitMbTempStatsHistIoh1TempAvg": cfprApComputeRackUnitMbTempStatsHistIoh1TempAvg,
       "cfprApComputeRackUnitMbTempStatsHistIoh1TempMax": cfprApComputeRackUnitMbTempStatsHistIoh1TempMax,
       "cfprApComputeRackUnitMbTempStatsHistIoh1TempMin": cfprApComputeRackUnitMbTempStatsHistIoh1TempMin,
       "cfprApComputeRackUnitMbTempStatsHistIoh2Temp": cfprApComputeRackUnitMbTempStatsHistIoh2Temp,
       "cfprApComputeRackUnitMbTempStatsHistIoh2TempAvg": cfprApComputeRackUnitMbTempStatsHistIoh2TempAvg,
       "cfprApComputeRackUnitMbTempStatsHistIoh2TempMax": cfprApComputeRackUnitMbTempStatsHistIoh2TempMax,
       "cfprApComputeRackUnitMbTempStatsHistIoh2TempMin": cfprApComputeRackUnitMbTempStatsHistIoh2TempMin,
       "cfprApComputeRackUnitMbTempStatsHistMostRecent": cfprApComputeRackUnitMbTempStatsHistMostRecent,
       "cfprApComputeRackUnitMbTempStatsHistRearTemp": cfprApComputeRackUnitMbTempStatsHistRearTemp,
       "cfprApComputeRackUnitMbTempStatsHistRearTempAvg": cfprApComputeRackUnitMbTempStatsHistRearTempAvg,
       "cfprApComputeRackUnitMbTempStatsHistRearTempMax": cfprApComputeRackUnitMbTempStatsHistRearTempMax,
       "cfprApComputeRackUnitMbTempStatsHistRearTempMin": cfprApComputeRackUnitMbTempStatsHistRearTempMin,
       "cfprApComputeRackUnitMbTempStatsHistSuspect": cfprApComputeRackUnitMbTempStatsHistSuspect,
       "cfprApComputeRackUnitMbTempStatsHistThresholded": cfprApComputeRackUnitMbTempStatsHistThresholded,
       "cfprApComputeRackUnitMbTempStatsHistTimeCollected": cfprApComputeRackUnitMbTempStatsHistTimeCollected,
       "cfprApComputeRtcBatteryTable": cfprApComputeRtcBatteryTable,
       "cfprApComputeRtcBatteryEntry": cfprApComputeRtcBatteryEntry,
       "cfprApComputeRtcBatteryInstanceId": cfprApComputeRtcBatteryInstanceId,
       "cfprApComputeRtcBatteryDn": cfprApComputeRtcBatteryDn,
       "cfprApComputeRtcBatteryRn": cfprApComputeRtcBatteryRn,
       "cfprApComputeRtcBatteryId": cfprApComputeRtcBatteryId,
       "cfprApComputeRtcBatteryLocationDn": cfprApComputeRtcBatteryLocationDn,
       "cfprApComputeRtcBatteryModel": cfprApComputeRtcBatteryModel,
       "cfprApComputeRtcBatteryOperQualifierReason": cfprApComputeRtcBatteryOperQualifierReason,
       "cfprApComputeRtcBatteryOperState": cfprApComputeRtcBatteryOperState,
       "cfprApComputeRtcBatteryOperability": cfprApComputeRtcBatteryOperability,
       "cfprApComputeRtcBatteryPerf": cfprApComputeRtcBatteryPerf,
       "cfprApComputeRtcBatteryPower": cfprApComputeRtcBatteryPower,
       "cfprApComputeRtcBatteryPresence": cfprApComputeRtcBatteryPresence,
       "cfprApComputeRtcBatteryRevision": cfprApComputeRtcBatteryRevision,
       "cfprApComputeRtcBatterySerial": cfprApComputeRtcBatterySerial,
       "cfprApComputeRtcBatteryThermal": cfprApComputeRtcBatteryThermal,
       "cfprApComputeRtcBatteryVendor": cfprApComputeRtcBatteryVendor,
       "cfprApComputeRtcBatteryVoltage": cfprApComputeRtcBatteryVoltage,
       "cfprApComputeScrubPolicyTable": cfprApComputeScrubPolicyTable,
       "cfprApComputeScrubPolicyEntry": cfprApComputeScrubPolicyEntry,
       "cfprApComputeScrubPolicyInstanceId": cfprApComputeScrubPolicyInstanceId,
       "cfprApComputeScrubPolicyDn": cfprApComputeScrubPolicyDn,
       "cfprApComputeScrubPolicyRn": cfprApComputeScrubPolicyRn,
       "cfprApComputeScrubPolicyBiosSettingsScrub": cfprApComputeScrubPolicyBiosSettingsScrub,
       "cfprApComputeScrubPolicyDescr": cfprApComputeScrubPolicyDescr,
       "cfprApComputeScrubPolicyDiskScrub": cfprApComputeScrubPolicyDiskScrub,
       "cfprApComputeScrubPolicyFlexFlashScrub": cfprApComputeScrubPolicyFlexFlashScrub,
       "cfprApComputeScrubPolicyIntId": cfprApComputeScrubPolicyIntId,
       "cfprApComputeScrubPolicyName": cfprApComputeScrubPolicyName,
       "cfprApComputeScrubPolicyPolicyLevel": cfprApComputeScrubPolicyPolicyLevel,
       "cfprApComputeScrubPolicyPolicyOwner": cfprApComputeScrubPolicyPolicyOwner,
       "cfprApComputeServerDiscPolicyTable": cfprApComputeServerDiscPolicyTable,
       "cfprApComputeServerDiscPolicyEntry": cfprApComputeServerDiscPolicyEntry,
       "cfprApComputeServerDiscPolicyInstanceId": cfprApComputeServerDiscPolicyInstanceId,
       "cfprApComputeServerDiscPolicyDn": cfprApComputeServerDiscPolicyDn,
       "cfprApComputeServerDiscPolicyRn": cfprApComputeServerDiscPolicyRn,
       "cfprApComputeServerDiscPolicyAction": cfprApComputeServerDiscPolicyAction,
       "cfprApComputeServerDiscPolicyDescr": cfprApComputeServerDiscPolicyDescr,
       "cfprApComputeServerDiscPolicyFsmDescr": cfprApComputeServerDiscPolicyFsmDescr,
       "cfprApComputeServerDiscPolicyFsmPrev": cfprApComputeServerDiscPolicyFsmPrev,
       "cfprApComputeServerDiscPolicyFsmProgr": cfprApComputeServerDiscPolicyFsmProgr,
       "cfprApComputeServerDiscPolicyFsmRmtInvErrCode": cfprApComputeServerDiscPolicyFsmRmtInvErrCode,
       "cfprApComputeServerDiscPolicyFsmRmtInvErrDescr": cfprApComputeServerDiscPolicyFsmRmtInvErrDescr,
       "cfprApComputeServerDiscPolicyFsmRmtInvRslt": cfprApComputeServerDiscPolicyFsmRmtInvRslt,
       "cfprApComputeServerDiscPolicyFsmStageDescr": cfprApComputeServerDiscPolicyFsmStageDescr,
       "cfprApComputeServerDiscPolicyFsmStamp": cfprApComputeServerDiscPolicyFsmStamp,
       "cfprApComputeServerDiscPolicyFsmStatus": cfprApComputeServerDiscPolicyFsmStatus,
       "cfprApComputeServerDiscPolicyFsmTry": cfprApComputeServerDiscPolicyFsmTry,
       "cfprApComputeServerDiscPolicyIntId": cfprApComputeServerDiscPolicyIntId,
       "cfprApComputeServerDiscPolicyName": cfprApComputeServerDiscPolicyName,
       "cfprApComputeServerDiscPolicyPolicyLevel": cfprApComputeServerDiscPolicyPolicyLevel,
       "cfprApComputeServerDiscPolicyPolicyOwner": cfprApComputeServerDiscPolicyPolicyOwner,
       "cfprApComputeServerDiscPolicyQualifier": cfprApComputeServerDiscPolicyQualifier,
       "cfprApComputeServerDiscPolicyScrubPolicyName": cfprApComputeServerDiscPolicyScrubPolicyName,
       "cfprApComputeServerDiscPolicyFsmTable": cfprApComputeServerDiscPolicyFsmTable,
       "cfprApComputeServerDiscPolicyFsmEntry": cfprApComputeServerDiscPolicyFsmEntry,
       "cfprApComputeServerDiscPolicyFsmInstanceId": cfprApComputeServerDiscPolicyFsmInstanceId,
       "cfprApComputeServerDiscPolicyFsmDn": cfprApComputeServerDiscPolicyFsmDn,
       "cfprApComputeServerDiscPolicyFsmRn": cfprApComputeServerDiscPolicyFsmRn,
       "cfprApComputeServerDiscPolicyFsmCompletionTime": cfprApComputeServerDiscPolicyFsmCompletionTime,
       "cfprApComputeServerDiscPolicyFsmCurrentFsm": cfprApComputeServerDiscPolicyFsmCurrentFsm,
       "cfprApComputeServerDiscPolicyFsmDescrData": cfprApComputeServerDiscPolicyFsmDescrData,
       "cfprApComputeServerDiscPolicyFsmFsmStatus": cfprApComputeServerDiscPolicyFsmFsmStatus,
       "cfprApComputeServerDiscPolicyFsmProgress": cfprApComputeServerDiscPolicyFsmProgress,
       "cfprApComputeServerDiscPolicyFsmRmtErrCode": cfprApComputeServerDiscPolicyFsmRmtErrCode,
       "cfprApComputeServerDiscPolicyFsmRmtErrDescr": cfprApComputeServerDiscPolicyFsmRmtErrDescr,
       "cfprApComputeServerDiscPolicyFsmRmtRslt": cfprApComputeServerDiscPolicyFsmRmtRslt,
       "cfprApComputeServerDiscPolicyFsmStageTable": cfprApComputeServerDiscPolicyFsmStageTable,
       "cfprApComputeServerDiscPolicyFsmStageEntry": cfprApComputeServerDiscPolicyFsmStageEntry,
       "cfprApComputeServerDiscPolicyFsmStageInstanceId": cfprApComputeServerDiscPolicyFsmStageInstanceId,
       "cfprApComputeServerDiscPolicyFsmStageDn": cfprApComputeServerDiscPolicyFsmStageDn,
       "cfprApComputeServerDiscPolicyFsmStageRn": cfprApComputeServerDiscPolicyFsmStageRn,
       "cfprApComputeServerDiscPolicyFsmStageDescrData": cfprApComputeServerDiscPolicyFsmStageDescrData,
       "cfprApComputeServerDiscPolicyFsmStageLastUpdateTime": cfprApComputeServerDiscPolicyFsmStageLastUpdateTime,
       "cfprApComputeServerDiscPolicyFsmStageName": cfprApComputeServerDiscPolicyFsmStageName,
       "cfprApComputeServerDiscPolicyFsmStageOrder": cfprApComputeServerDiscPolicyFsmStageOrder,
       "cfprApComputeServerDiscPolicyFsmStageRetry": cfprApComputeServerDiscPolicyFsmStageRetry,
       "cfprApComputeServerDiscPolicyFsmStageStageStatus": cfprApComputeServerDiscPolicyFsmStageStageStatus,
       "cfprApComputeServerDiscPolicyFsmTaskTable": cfprApComputeServerDiscPolicyFsmTaskTable,
       "cfprApComputeServerDiscPolicyFsmTaskEntry": cfprApComputeServerDiscPolicyFsmTaskEntry,
       "cfprApComputeServerDiscPolicyFsmTaskInstanceId": cfprApComputeServerDiscPolicyFsmTaskInstanceId,
       "cfprApComputeServerDiscPolicyFsmTaskDn": cfprApComputeServerDiscPolicyFsmTaskDn,
       "cfprApComputeServerDiscPolicyFsmTaskRn": cfprApComputeServerDiscPolicyFsmTaskRn,
       "cfprApComputeServerDiscPolicyFsmTaskCompletion": cfprApComputeServerDiscPolicyFsmTaskCompletion,
       "cfprApComputeServerDiscPolicyFsmTaskFlags": cfprApComputeServerDiscPolicyFsmTaskFlags,
       "cfprApComputeServerDiscPolicyFsmTaskItem": cfprApComputeServerDiscPolicyFsmTaskItem,
       "cfprApComputeServerDiscPolicyFsmTaskSeqId": cfprApComputeServerDiscPolicyFsmTaskSeqId,
       "cfprApComputeServerMgmtPolicyTable": cfprApComputeServerMgmtPolicyTable,
       "cfprApComputeServerMgmtPolicyEntry": cfprApComputeServerMgmtPolicyEntry,
       "cfprApComputeServerMgmtPolicyInstanceId": cfprApComputeServerMgmtPolicyInstanceId,
       "cfprApComputeServerMgmtPolicyDn": cfprApComputeServerMgmtPolicyDn,
       "cfprApComputeServerMgmtPolicyRn": cfprApComputeServerMgmtPolicyRn,
       "cfprApComputeServerMgmtPolicyAction": cfprApComputeServerMgmtPolicyAction,
       "cfprApComputeServerMgmtPolicyDescr": cfprApComputeServerMgmtPolicyDescr,
       "cfprApComputeServerMgmtPolicyIntId": cfprApComputeServerMgmtPolicyIntId,
       "cfprApComputeServerMgmtPolicyName": cfprApComputeServerMgmtPolicyName,
       "cfprApComputeServerMgmtPolicyPolicyLevel": cfprApComputeServerMgmtPolicyPolicyLevel,
       "cfprApComputeServerMgmtPolicyPolicyOwner": cfprApComputeServerMgmtPolicyPolicyOwner,
       "cfprApComputeServerMgmtPolicyQualifier": cfprApComputeServerMgmtPolicyQualifier,
       "cfprApComputeSlotQualTable": cfprApComputeSlotQualTable,
       "cfprApComputeSlotQualEntry": cfprApComputeSlotQualEntry,
       "cfprApComputeSlotQualInstanceId": cfprApComputeSlotQualInstanceId,
       "cfprApComputeSlotQualDn": cfprApComputeSlotQualDn,
       "cfprApComputeSlotQualRn": cfprApComputeSlotQualRn,
       "cfprApComputeSlotQualMaxId": cfprApComputeSlotQualMaxId,
       "cfprApComputeSlotQualMinId": cfprApComputeSlotQualMinId}
)
