# SNMP MIB module (CISCO-FIREPOWER-AP-FIRMWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-FIRMWARE-MIB.mib
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

(CfprApConditionRemoteInvRslt,
 CfprApExtpolConnProtocol,
 CfprApFirmwareAdminState,
 CfprApFirmwareAutoSyncConfigIssue,
 CfprApFirmwareAutoSyncState,
 CfprApFirmwareBootUnitImage,
 CfprApFirmwareBootUnitMode,
 CfprApFirmwareCatalogPackConfigState,
 CfprApFirmwareCompleteness,
 CfprApFirmwareComponentType,
 CfprApFirmwareDependencyRelationship,
 CfprApFirmwareDependencyScope,
 CfprApFirmwareDependencySensitivity,
 CfprApFirmwareDistributableFsmCurrentFsm,
 CfprApFirmwareDistributableFsmStageName,
 CfprApFirmwareDistributableFsmTaskItem,
 CfprApFirmwareDistributableType,
 CfprApFirmwareDownloadActivity,
 CfprApFirmwareDownloaderFsmCurrentFsm,
 CfprApFirmwareDownloaderFsmStageName,
 CfprApFirmwareDownloaderFsmTaskItem,
 CfprApFirmwareEquipmentType,
 CfprApFirmwareFirmwareState,
 CfprApFirmwareFwState,
 CfprApFirmwareFwUpgradeState,
 CfprApFirmwareHostPackConfigQualifier,
 CfprApFirmwareImageDeleted,
 CfprApFirmwareImageError,
 CfprApFirmwareImageFsmCurrentFsm,
 CfprApFirmwareImageFsmStageName,
 CfprApFirmwareImageFsmTaskItem,
 CfprApFirmwareImagePresence,
 CfprApFirmwareImageState,
 CfprApFirmwareImpactType,
 CfprApFirmwareInfraPackFsmCurrentFsm,
 CfprApFirmwareInfraPackFsmStageName,
 CfprApFirmwareInfraPackFsmTaskFlags,
 CfprApFirmwareInfraPackFsmTaskItem,
 CfprApFirmwareInstallState,
 CfprApFirmwareItemType,
 CfprApFirmwarePackItemPresence,
 CfprApFirmwarePackMode,
 CfprApFirmwarePlatformPackFsmCurrentFsm,
 CfprApFirmwarePlatformPackFsmStageName,
 CfprApFirmwarePlatformPackFsmTaskFlags,
 CfprApFirmwarePlatformPackFsmTaskItem,
 CfprApFirmwarePlatformType,
 CfprApFirmwareRunningDeployment,
 CfprApFirmwareSupFirmwareFsmCurrentFsm,
 CfprApFirmwareSupFirmwareFsmStageName,
 CfprApFirmwareSupFirmwareFsmTaskFlags,
 CfprApFirmwareSupFirmwareFsmTaskItem,
 CfprApFirmwareSystemFsmCurrentFsm,
 CfprApFirmwareSystemFsmStageName,
 CfprApFirmwareSystemFsmTaskFlags,
 CfprApFirmwareSystemFsmTaskItem,
 CfprApFirmwareTransferState,
 CfprApFirmwareTransport,
 CfprApFirmwareTriggerState,
 CfprApFirmwareType,
 CfprApFirmwareUpdatableDeployment,
 CfprApFirmwareUpgradeCategory,
 CfprApFirmwareUpgradeSeverity,
 CfprApFirmwareUpgradeState,
 CfprApFirmwareUpgradeStatus,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApPolicyPolicyOwner,
 CfprApTrigAckChangeDetails,
 CfprApTrigAckChanges,
 CfprApTrigAckDisr,
 CfprApTrigAckOperState,
 CfprApTrigAckPrevOperState,
 CfprApTrigAdminState,
 CfprApTrigTrigOperState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApExtpolConnProtocol",
    "CfprApFirmwareAdminState",
    "CfprApFirmwareAutoSyncConfigIssue",
    "CfprApFirmwareAutoSyncState",
    "CfprApFirmwareBootUnitImage",
    "CfprApFirmwareBootUnitMode",
    "CfprApFirmwareCatalogPackConfigState",
    "CfprApFirmwareCompleteness",
    "CfprApFirmwareComponentType",
    "CfprApFirmwareDependencyRelationship",
    "CfprApFirmwareDependencyScope",
    "CfprApFirmwareDependencySensitivity",
    "CfprApFirmwareDistributableFsmCurrentFsm",
    "CfprApFirmwareDistributableFsmStageName",
    "CfprApFirmwareDistributableFsmTaskItem",
    "CfprApFirmwareDistributableType",
    "CfprApFirmwareDownloadActivity",
    "CfprApFirmwareDownloaderFsmCurrentFsm",
    "CfprApFirmwareDownloaderFsmStageName",
    "CfprApFirmwareDownloaderFsmTaskItem",
    "CfprApFirmwareEquipmentType",
    "CfprApFirmwareFirmwareState",
    "CfprApFirmwareFwState",
    "CfprApFirmwareFwUpgradeState",
    "CfprApFirmwareHostPackConfigQualifier",
    "CfprApFirmwareImageDeleted",
    "CfprApFirmwareImageError",
    "CfprApFirmwareImageFsmCurrentFsm",
    "CfprApFirmwareImageFsmStageName",
    "CfprApFirmwareImageFsmTaskItem",
    "CfprApFirmwareImagePresence",
    "CfprApFirmwareImageState",
    "CfprApFirmwareImpactType",
    "CfprApFirmwareInfraPackFsmCurrentFsm",
    "CfprApFirmwareInfraPackFsmStageName",
    "CfprApFirmwareInfraPackFsmTaskFlags",
    "CfprApFirmwareInfraPackFsmTaskItem",
    "CfprApFirmwareInstallState",
    "CfprApFirmwareItemType",
    "CfprApFirmwarePackItemPresence",
    "CfprApFirmwarePackMode",
    "CfprApFirmwarePlatformPackFsmCurrentFsm",
    "CfprApFirmwarePlatformPackFsmStageName",
    "CfprApFirmwarePlatformPackFsmTaskFlags",
    "CfprApFirmwarePlatformPackFsmTaskItem",
    "CfprApFirmwarePlatformType",
    "CfprApFirmwareRunningDeployment",
    "CfprApFirmwareSupFirmwareFsmCurrentFsm",
    "CfprApFirmwareSupFirmwareFsmStageName",
    "CfprApFirmwareSupFirmwareFsmTaskFlags",
    "CfprApFirmwareSupFirmwareFsmTaskItem",
    "CfprApFirmwareSystemFsmCurrentFsm",
    "CfprApFirmwareSystemFsmStageName",
    "CfprApFirmwareSystemFsmTaskFlags",
    "CfprApFirmwareSystemFsmTaskItem",
    "CfprApFirmwareTransferState",
    "CfprApFirmwareTransport",
    "CfprApFirmwareTriggerState",
    "CfprApFirmwareType",
    "CfprApFirmwareUpdatableDeployment",
    "CfprApFirmwareUpgradeCategory",
    "CfprApFirmwareUpgradeSeverity",
    "CfprApFirmwareUpgradeState",
    "CfprApFirmwareUpgradeStatus",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApPolicyPolicyOwner",
    "CfprApTrigAckChangeDetails",
    "CfprApTrigAckChanges",
    "CfprApTrigAckDisr",
    "CfprApTrigAckOperState",
    "CfprApTrigAckPrevOperState",
    "CfprApTrigAdminState",
    "CfprApTrigTrigOperState")

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

cfprApFirmwareObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApFirmwareAckTable_Object = MibTable
cfprApFirmwareAckTable = _CfprApFirmwareAckTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1)
)
if mibBuilder.loadTexts:
    cfprApFirmwareAckTable.setStatus("current")
_CfprApFirmwareAckEntry_Object = MibTableRow
cfprApFirmwareAckEntry = _CfprApFirmwareAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1)
)
cfprApFirmwareAckEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareAckInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareAckEntry.setStatus("current")
_CfprApFirmwareAckInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareAckInstanceId_Object = MibTableColumn
cfprApFirmwareAckInstanceId = _CfprApFirmwareAckInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 1),
    _CfprApFirmwareAckInstanceId_Type()
)
cfprApFirmwareAckInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareAckInstanceId.setStatus("current")
_CfprApFirmwareAckDn_Type = CfprApManagedObjectDn
_CfprApFirmwareAckDn_Object = MibTableColumn
cfprApFirmwareAckDn = _CfprApFirmwareAckDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 2),
    _CfprApFirmwareAckDn_Type()
)
cfprApFirmwareAckDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckDn.setStatus("current")
_CfprApFirmwareAckRn_Type = SnmpAdminString
_CfprApFirmwareAckRn_Object = MibTableColumn
cfprApFirmwareAckRn = _CfprApFirmwareAckRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 3),
    _CfprApFirmwareAckRn_Type()
)
cfprApFirmwareAckRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckRn.setStatus("current")
_CfprApFirmwareAckAcked_Type = DateAndTime
_CfprApFirmwareAckAcked_Object = MibTableColumn
cfprApFirmwareAckAcked = _CfprApFirmwareAckAcked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 4),
    _CfprApFirmwareAckAcked_Type()
)
cfprApFirmwareAckAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckAcked.setStatus("current")
_CfprApFirmwareAckAckedBy_Type = SnmpAdminString
_CfprApFirmwareAckAckedBy_Object = MibTableColumn
cfprApFirmwareAckAckedBy = _CfprApFirmwareAckAckedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 5),
    _CfprApFirmwareAckAckedBy_Type()
)
cfprApFirmwareAckAckedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckAckedBy.setStatus("current")
_CfprApFirmwareAckAdminState_Type = CfprApTrigAdminState
_CfprApFirmwareAckAdminState_Object = MibTableColumn
cfprApFirmwareAckAdminState = _CfprApFirmwareAckAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 6),
    _CfprApFirmwareAckAdminState_Type()
)
cfprApFirmwareAckAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckAdminState.setStatus("current")
_CfprApFirmwareAckAutoDelete_Type = TruthValue
_CfprApFirmwareAckAutoDelete_Object = MibTableColumn
cfprApFirmwareAckAutoDelete = _CfprApFirmwareAckAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 7),
    _CfprApFirmwareAckAutoDelete_Type()
)
cfprApFirmwareAckAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckAutoDelete.setStatus("current")
_CfprApFirmwareAckChangeBy_Type = SnmpAdminString
_CfprApFirmwareAckChangeBy_Object = MibTableColumn
cfprApFirmwareAckChangeBy = _CfprApFirmwareAckChangeBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 8),
    _CfprApFirmwareAckChangeBy_Type()
)
cfprApFirmwareAckChangeBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckChangeBy.setStatus("current")
_CfprApFirmwareAckChangeDetails_Type = CfprApTrigAckChangeDetails
_CfprApFirmwareAckChangeDetails_Object = MibTableColumn
cfprApFirmwareAckChangeDetails = _CfprApFirmwareAckChangeDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 9),
    _CfprApFirmwareAckChangeDetails_Type()
)
cfprApFirmwareAckChangeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckChangeDetails.setStatus("current")
_CfprApFirmwareAckChanges_Type = CfprApTrigAckChanges
_CfprApFirmwareAckChanges_Object = MibTableColumn
cfprApFirmwareAckChanges = _CfprApFirmwareAckChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 10),
    _CfprApFirmwareAckChanges_Type()
)
cfprApFirmwareAckChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckChanges.setStatus("current")
_CfprApFirmwareAckDescr_Type = SnmpAdminString
_CfprApFirmwareAckDescr_Object = MibTableColumn
cfprApFirmwareAckDescr = _CfprApFirmwareAckDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 11),
    _CfprApFirmwareAckDescr_Type()
)
cfprApFirmwareAckDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckDescr.setStatus("current")
_CfprApFirmwareAckDisr_Type = CfprApTrigAckDisr
_CfprApFirmwareAckDisr_Object = MibTableColumn
cfprApFirmwareAckDisr = _CfprApFirmwareAckDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 12),
    _CfprApFirmwareAckDisr_Type()
)
cfprApFirmwareAckDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckDisr.setStatus("current")
_CfprApFirmwareAckIgnoreCap_Type = TruthValue
_CfprApFirmwareAckIgnoreCap_Object = MibTableColumn
cfprApFirmwareAckIgnoreCap = _CfprApFirmwareAckIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 13),
    _CfprApFirmwareAckIgnoreCap_Type()
)
cfprApFirmwareAckIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckIgnoreCap.setStatus("current")
_CfprApFirmwareAckIntId_Type = SnmpAdminString
_CfprApFirmwareAckIntId_Object = MibTableColumn
cfprApFirmwareAckIntId = _CfprApFirmwareAckIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 14),
    _CfprApFirmwareAckIntId_Type()
)
cfprApFirmwareAckIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckIntId.setStatus("current")
_CfprApFirmwareAckModified_Type = DateAndTime
_CfprApFirmwareAckModified_Object = MibTableColumn
cfprApFirmwareAckModified = _CfprApFirmwareAckModified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 15),
    _CfprApFirmwareAckModified_Type()
)
cfprApFirmwareAckModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckModified.setStatus("current")
_CfprApFirmwareAckName_Type = SnmpAdminString
_CfprApFirmwareAckName_Object = MibTableColumn
cfprApFirmwareAckName = _CfprApFirmwareAckName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 16),
    _CfprApFirmwareAckName_Type()
)
cfprApFirmwareAckName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckName.setStatus("current")
_CfprApFirmwareAckOperScheduler_Type = SnmpAdminString
_CfprApFirmwareAckOperScheduler_Object = MibTableColumn
cfprApFirmwareAckOperScheduler = _CfprApFirmwareAckOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 17),
    _CfprApFirmwareAckOperScheduler_Type()
)
cfprApFirmwareAckOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckOperScheduler.setStatus("current")
_CfprApFirmwareAckOperState_Type = CfprApTrigAckOperState
_CfprApFirmwareAckOperState_Object = MibTableColumn
cfprApFirmwareAckOperState = _CfprApFirmwareAckOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 18),
    _CfprApFirmwareAckOperState_Type()
)
cfprApFirmwareAckOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckOperState.setStatus("current")
_CfprApFirmwareAckPolicyLevel_Type = Gauge32
_CfprApFirmwareAckPolicyLevel_Object = MibTableColumn
cfprApFirmwareAckPolicyLevel = _CfprApFirmwareAckPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 19),
    _CfprApFirmwareAckPolicyLevel_Type()
)
cfprApFirmwareAckPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckPolicyLevel.setStatus("current")
_CfprApFirmwareAckPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwareAckPolicyOwner_Object = MibTableColumn
cfprApFirmwareAckPolicyOwner = _CfprApFirmwareAckPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 20),
    _CfprApFirmwareAckPolicyOwner_Type()
)
cfprApFirmwareAckPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckPolicyOwner.setStatus("current")
_CfprApFirmwareAckPrevOperState_Type = CfprApTrigAckPrevOperState
_CfprApFirmwareAckPrevOperState_Object = MibTableColumn
cfprApFirmwareAckPrevOperState = _CfprApFirmwareAckPrevOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 21),
    _CfprApFirmwareAckPrevOperState_Type()
)
cfprApFirmwareAckPrevOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckPrevOperState.setStatus("current")
_CfprApFirmwareAckScheduler_Type = SnmpAdminString
_CfprApFirmwareAckScheduler_Object = MibTableColumn
cfprApFirmwareAckScheduler = _CfprApFirmwareAckScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 1, 1, 22),
    _CfprApFirmwareAckScheduler_Type()
)
cfprApFirmwareAckScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAckScheduler.setStatus("current")
_CfprApFirmwareAutoSyncPolicyTable_Object = MibTable
cfprApFirmwareAutoSyncPolicyTable = _CfprApFirmwareAutoSyncPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 2)
)
if mibBuilder.loadTexts:
    cfprApFirmwareAutoSyncPolicyTable.setStatus("current")
_CfprApFirmwareAutoSyncPolicyEntry_Object = MibTableRow
cfprApFirmwareAutoSyncPolicyEntry = _CfprApFirmwareAutoSyncPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 2, 1)
)
cfprApFirmwareAutoSyncPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareAutoSyncPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareAutoSyncPolicyEntry.setStatus("current")
_CfprApFirmwareAutoSyncPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareAutoSyncPolicyInstanceId_Object = MibTableColumn
cfprApFirmwareAutoSyncPolicyInstanceId = _CfprApFirmwareAutoSyncPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 2, 1, 1),
    _CfprApFirmwareAutoSyncPolicyInstanceId_Type()
)
cfprApFirmwareAutoSyncPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareAutoSyncPolicyInstanceId.setStatus("current")
_CfprApFirmwareAutoSyncPolicyDn_Type = CfprApManagedObjectDn
_CfprApFirmwareAutoSyncPolicyDn_Object = MibTableColumn
cfprApFirmwareAutoSyncPolicyDn = _CfprApFirmwareAutoSyncPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 2, 1, 2),
    _CfprApFirmwareAutoSyncPolicyDn_Type()
)
cfprApFirmwareAutoSyncPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAutoSyncPolicyDn.setStatus("current")
_CfprApFirmwareAutoSyncPolicyRn_Type = SnmpAdminString
_CfprApFirmwareAutoSyncPolicyRn_Object = MibTableColumn
cfprApFirmwareAutoSyncPolicyRn = _CfprApFirmwareAutoSyncPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 2, 1, 3),
    _CfprApFirmwareAutoSyncPolicyRn_Type()
)
cfprApFirmwareAutoSyncPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAutoSyncPolicyRn.setStatus("current")
_CfprApFirmwareAutoSyncPolicyConfigIssue_Type = CfprApFirmwareAutoSyncConfigIssue
_CfprApFirmwareAutoSyncPolicyConfigIssue_Object = MibTableColumn
cfprApFirmwareAutoSyncPolicyConfigIssue = _CfprApFirmwareAutoSyncPolicyConfigIssue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 2, 1, 4),
    _CfprApFirmwareAutoSyncPolicyConfigIssue_Type()
)
cfprApFirmwareAutoSyncPolicyConfigIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAutoSyncPolicyConfigIssue.setStatus("current")
_CfprApFirmwareAutoSyncPolicyDescr_Type = SnmpAdminString
_CfprApFirmwareAutoSyncPolicyDescr_Object = MibTableColumn
cfprApFirmwareAutoSyncPolicyDescr = _CfprApFirmwareAutoSyncPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 2, 1, 5),
    _CfprApFirmwareAutoSyncPolicyDescr_Type()
)
cfprApFirmwareAutoSyncPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAutoSyncPolicyDescr.setStatus("current")
_CfprApFirmwareAutoSyncPolicyIntId_Type = SnmpAdminString
_CfprApFirmwareAutoSyncPolicyIntId_Object = MibTableColumn
cfprApFirmwareAutoSyncPolicyIntId = _CfprApFirmwareAutoSyncPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 2, 1, 6),
    _CfprApFirmwareAutoSyncPolicyIntId_Type()
)
cfprApFirmwareAutoSyncPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAutoSyncPolicyIntId.setStatus("current")
_CfprApFirmwareAutoSyncPolicyName_Type = SnmpAdminString
_CfprApFirmwareAutoSyncPolicyName_Object = MibTableColumn
cfprApFirmwareAutoSyncPolicyName = _CfprApFirmwareAutoSyncPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 2, 1, 7),
    _CfprApFirmwareAutoSyncPolicyName_Type()
)
cfprApFirmwareAutoSyncPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAutoSyncPolicyName.setStatus("current")
_CfprApFirmwareAutoSyncPolicyPolicyLevel_Type = Gauge32
_CfprApFirmwareAutoSyncPolicyPolicyLevel_Object = MibTableColumn
cfprApFirmwareAutoSyncPolicyPolicyLevel = _CfprApFirmwareAutoSyncPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 2, 1, 8),
    _CfprApFirmwareAutoSyncPolicyPolicyLevel_Type()
)
cfprApFirmwareAutoSyncPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAutoSyncPolicyPolicyLevel.setStatus("current")
_CfprApFirmwareAutoSyncPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwareAutoSyncPolicyPolicyOwner_Object = MibTableColumn
cfprApFirmwareAutoSyncPolicyPolicyOwner = _CfprApFirmwareAutoSyncPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 2, 1, 9),
    _CfprApFirmwareAutoSyncPolicyPolicyOwner_Type()
)
cfprApFirmwareAutoSyncPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAutoSyncPolicyPolicyOwner.setStatus("current")
_CfprApFirmwareAutoSyncPolicySyncState_Type = CfprApFirmwareAutoSyncState
_CfprApFirmwareAutoSyncPolicySyncState_Object = MibTableColumn
cfprApFirmwareAutoSyncPolicySyncState = _CfprApFirmwareAutoSyncPolicySyncState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 2, 1, 10),
    _CfprApFirmwareAutoSyncPolicySyncState_Type()
)
cfprApFirmwareAutoSyncPolicySyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareAutoSyncPolicySyncState.setStatus("current")
_CfprApFirmwareBladeTable_Object = MibTable
cfprApFirmwareBladeTable = _CfprApFirmwareBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 3)
)
if mibBuilder.loadTexts:
    cfprApFirmwareBladeTable.setStatus("current")
_CfprApFirmwareBladeEntry_Object = MibTableRow
cfprApFirmwareBladeEntry = _CfprApFirmwareBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 3, 1)
)
cfprApFirmwareBladeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareBladeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareBladeEntry.setStatus("current")
_CfprApFirmwareBladeInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareBladeInstanceId_Object = MibTableColumn
cfprApFirmwareBladeInstanceId = _CfprApFirmwareBladeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 3, 1, 1),
    _CfprApFirmwareBladeInstanceId_Type()
)
cfprApFirmwareBladeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareBladeInstanceId.setStatus("current")
_CfprApFirmwareBladeDn_Type = CfprApManagedObjectDn
_CfprApFirmwareBladeDn_Object = MibTableColumn
cfprApFirmwareBladeDn = _CfprApFirmwareBladeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 3, 1, 2),
    _CfprApFirmwareBladeDn_Type()
)
cfprApFirmwareBladeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBladeDn.setStatus("current")
_CfprApFirmwareBladeRn_Type = SnmpAdminString
_CfprApFirmwareBladeRn_Object = MibTableColumn
cfprApFirmwareBladeRn = _CfprApFirmwareBladeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 3, 1, 3),
    _CfprApFirmwareBladeRn_Type()
)
cfprApFirmwareBladeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBladeRn.setStatus("current")
_CfprApFirmwareBladeOperVersion_Type = SnmpAdminString
_CfprApFirmwareBladeOperVersion_Object = MibTableColumn
cfprApFirmwareBladeOperVersion = _CfprApFirmwareBladeOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 3, 1, 4),
    _CfprApFirmwareBladeOperVersion_Type()
)
cfprApFirmwareBladeOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBladeOperVersion.setStatus("current")
_CfprApFirmwareBootDefinitionTable_Object = MibTable
cfprApFirmwareBootDefinitionTable = _CfprApFirmwareBootDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 4)
)
if mibBuilder.loadTexts:
    cfprApFirmwareBootDefinitionTable.setStatus("current")
_CfprApFirmwareBootDefinitionEntry_Object = MibTableRow
cfprApFirmwareBootDefinitionEntry = _CfprApFirmwareBootDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 4, 1)
)
cfprApFirmwareBootDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareBootDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareBootDefinitionEntry.setStatus("current")
_CfprApFirmwareBootDefinitionInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareBootDefinitionInstanceId_Object = MibTableColumn
cfprApFirmwareBootDefinitionInstanceId = _CfprApFirmwareBootDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 4, 1, 1),
    _CfprApFirmwareBootDefinitionInstanceId_Type()
)
cfprApFirmwareBootDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareBootDefinitionInstanceId.setStatus("current")
_CfprApFirmwareBootDefinitionDn_Type = CfprApManagedObjectDn
_CfprApFirmwareBootDefinitionDn_Object = MibTableColumn
cfprApFirmwareBootDefinitionDn = _CfprApFirmwareBootDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 4, 1, 2),
    _CfprApFirmwareBootDefinitionDn_Type()
)
cfprApFirmwareBootDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootDefinitionDn.setStatus("current")
_CfprApFirmwareBootDefinitionRn_Type = SnmpAdminString
_CfprApFirmwareBootDefinitionRn_Object = MibTableColumn
cfprApFirmwareBootDefinitionRn = _CfprApFirmwareBootDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 4, 1, 3),
    _CfprApFirmwareBootDefinitionRn_Type()
)
cfprApFirmwareBootDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootDefinitionRn.setStatus("current")
_CfprApFirmwareBootDefinitionType_Type = CfprApFirmwareType
_CfprApFirmwareBootDefinitionType_Object = MibTableColumn
cfprApFirmwareBootDefinitionType = _CfprApFirmwareBootDefinitionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 4, 1, 4),
    _CfprApFirmwareBootDefinitionType_Type()
)
cfprApFirmwareBootDefinitionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootDefinitionType.setStatus("current")
_CfprApFirmwareBootUnitTable_Object = MibTable
cfprApFirmwareBootUnitTable = _CfprApFirmwareBootUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5)
)
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitTable.setStatus("current")
_CfprApFirmwareBootUnitEntry_Object = MibTableRow
cfprApFirmwareBootUnitEntry = _CfprApFirmwareBootUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1)
)
cfprApFirmwareBootUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareBootUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitEntry.setStatus("current")
_CfprApFirmwareBootUnitInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareBootUnitInstanceId_Object = MibTableColumn
cfprApFirmwareBootUnitInstanceId = _CfprApFirmwareBootUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 1),
    _CfprApFirmwareBootUnitInstanceId_Type()
)
cfprApFirmwareBootUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitInstanceId.setStatus("current")
_CfprApFirmwareBootUnitDn_Type = CfprApManagedObjectDn
_CfprApFirmwareBootUnitDn_Object = MibTableColumn
cfprApFirmwareBootUnitDn = _CfprApFirmwareBootUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 2),
    _CfprApFirmwareBootUnitDn_Type()
)
cfprApFirmwareBootUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitDn.setStatus("current")
_CfprApFirmwareBootUnitRn_Type = SnmpAdminString
_CfprApFirmwareBootUnitRn_Object = MibTableColumn
cfprApFirmwareBootUnitRn = _CfprApFirmwareBootUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 3),
    _CfprApFirmwareBootUnitRn_Type()
)
cfprApFirmwareBootUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitRn.setStatus("current")
_CfprApFirmwareBootUnitAdminState_Type = CfprApFirmwareTriggerState
_CfprApFirmwareBootUnitAdminState_Object = MibTableColumn
cfprApFirmwareBootUnitAdminState = _CfprApFirmwareBootUnitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 4),
    _CfprApFirmwareBootUnitAdminState_Type()
)
cfprApFirmwareBootUnitAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitAdminState.setStatus("current")
_CfprApFirmwareBootUnitIgnoreCompCheck_Type = TruthValue
_CfprApFirmwareBootUnitIgnoreCompCheck_Object = MibTableColumn
cfprApFirmwareBootUnitIgnoreCompCheck = _CfprApFirmwareBootUnitIgnoreCompCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 5),
    _CfprApFirmwareBootUnitIgnoreCompCheck_Type()
)
cfprApFirmwareBootUnitIgnoreCompCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitIgnoreCompCheck.setStatus("current")
_CfprApFirmwareBootUnitImage_Type = CfprApFirmwareBootUnitImage
_CfprApFirmwareBootUnitImage_Object = MibTableColumn
cfprApFirmwareBootUnitImage = _CfprApFirmwareBootUnitImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 6),
    _CfprApFirmwareBootUnitImage_Type()
)
cfprApFirmwareBootUnitImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitImage.setStatus("current")
_CfprApFirmwareBootUnitInvTag_Type = SnmpAdminString
_CfprApFirmwareBootUnitInvTag_Object = MibTableColumn
cfprApFirmwareBootUnitInvTag = _CfprApFirmwareBootUnitInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 7),
    _CfprApFirmwareBootUnitInvTag_Type()
)
cfprApFirmwareBootUnitInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitInvTag.setStatus("current")
_CfprApFirmwareBootUnitMode_Type = CfprApFirmwareBootUnitMode
_CfprApFirmwareBootUnitMode_Object = MibTableColumn
cfprApFirmwareBootUnitMode = _CfprApFirmwareBootUnitMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 8),
    _CfprApFirmwareBootUnitMode_Type()
)
cfprApFirmwareBootUnitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitMode.setStatus("current")
_CfprApFirmwareBootUnitOperState_Type = CfprApFirmwareImageState
_CfprApFirmwareBootUnitOperState_Object = MibTableColumn
cfprApFirmwareBootUnitOperState = _CfprApFirmwareBootUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 9),
    _CfprApFirmwareBootUnitOperState_Type()
)
cfprApFirmwareBootUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitOperState.setStatus("current")
_CfprApFirmwareBootUnitPrevVersion_Type = SnmpAdminString
_CfprApFirmwareBootUnitPrevVersion_Object = MibTableColumn
cfprApFirmwareBootUnitPrevVersion = _CfprApFirmwareBootUnitPrevVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 10),
    _CfprApFirmwareBootUnitPrevVersion_Type()
)
cfprApFirmwareBootUnitPrevVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitPrevVersion.setStatus("current")
_CfprApFirmwareBootUnitResetOnActivate_Type = TruthValue
_CfprApFirmwareBootUnitResetOnActivate_Object = MibTableColumn
cfprApFirmwareBootUnitResetOnActivate = _CfprApFirmwareBootUnitResetOnActivate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 11),
    _CfprApFirmwareBootUnitResetOnActivate_Type()
)
cfprApFirmwareBootUnitResetOnActivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitResetOnActivate.setStatus("current")
_CfprApFirmwareBootUnitSkipValidation_Type = TruthValue
_CfprApFirmwareBootUnitSkipValidation_Object = MibTableColumn
cfprApFirmwareBootUnitSkipValidation = _CfprApFirmwareBootUnitSkipValidation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 12),
    _CfprApFirmwareBootUnitSkipValidation_Type()
)
cfprApFirmwareBootUnitSkipValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitSkipValidation.setStatus("current")
_CfprApFirmwareBootUnitType_Type = CfprApFirmwareComponentType
_CfprApFirmwareBootUnitType_Object = MibTableColumn
cfprApFirmwareBootUnitType = _CfprApFirmwareBootUnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 13),
    _CfprApFirmwareBootUnitType_Type()
)
cfprApFirmwareBootUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitType.setStatus("current")
_CfprApFirmwareBootUnitVersion_Type = SnmpAdminString
_CfprApFirmwareBootUnitVersion_Object = MibTableColumn
cfprApFirmwareBootUnitVersion = _CfprApFirmwareBootUnitVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 5, 1, 14),
    _CfprApFirmwareBootUnitVersion_Type()
)
cfprApFirmwareBootUnitVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBootUnitVersion.setStatus("current")
_CfprApFirmwareBundleInfoTable_Object = MibTable
cfprApFirmwareBundleInfoTable = _CfprApFirmwareBundleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 6)
)
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoTable.setStatus("current")
_CfprApFirmwareBundleInfoEntry_Object = MibTableRow
cfprApFirmwareBundleInfoEntry = _CfprApFirmwareBundleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 6, 1)
)
cfprApFirmwareBundleInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareBundleInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoEntry.setStatus("current")
_CfprApFirmwareBundleInfoInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareBundleInfoInstanceId_Object = MibTableColumn
cfprApFirmwareBundleInfoInstanceId = _CfprApFirmwareBundleInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 6, 1, 1),
    _CfprApFirmwareBundleInfoInstanceId_Type()
)
cfprApFirmwareBundleInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoInstanceId.setStatus("current")
_CfprApFirmwareBundleInfoDn_Type = CfprApManagedObjectDn
_CfprApFirmwareBundleInfoDn_Object = MibTableColumn
cfprApFirmwareBundleInfoDn = _CfprApFirmwareBundleInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 6, 1, 2),
    _CfprApFirmwareBundleInfoDn_Type()
)
cfprApFirmwareBundleInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoDn.setStatus("current")
_CfprApFirmwareBundleInfoRn_Type = SnmpAdminString
_CfprApFirmwareBundleInfoRn_Object = MibTableColumn
cfprApFirmwareBundleInfoRn = _CfprApFirmwareBundleInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 6, 1, 3),
    _CfprApFirmwareBundleInfoRn_Type()
)
cfprApFirmwareBundleInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoRn.setStatus("current")
_CfprApFirmwareBundleInfoType_Type = CfprApFirmwareDistributableType
_CfprApFirmwareBundleInfoType_Object = MibTableColumn
cfprApFirmwareBundleInfoType = _CfprApFirmwareBundleInfoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 6, 1, 4),
    _CfprApFirmwareBundleInfoType_Type()
)
cfprApFirmwareBundleInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoType.setStatus("current")
_CfprApFirmwareBundleInfoVersion_Type = SnmpAdminString
_CfprApFirmwareBundleInfoVersion_Object = MibTableColumn
cfprApFirmwareBundleInfoVersion = _CfprApFirmwareBundleInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 6, 1, 5),
    _CfprApFirmwareBundleInfoVersion_Type()
)
cfprApFirmwareBundleInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoVersion.setStatus("current")
_CfprApFirmwareBundleInfoDigestTable_Object = MibTable
cfprApFirmwareBundleInfoDigestTable = _CfprApFirmwareBundleInfoDigestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 7)
)
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoDigestTable.setStatus("current")
_CfprApFirmwareBundleInfoDigestEntry_Object = MibTableRow
cfprApFirmwareBundleInfoDigestEntry = _CfprApFirmwareBundleInfoDigestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 7, 1)
)
cfprApFirmwareBundleInfoDigestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareBundleInfoDigestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoDigestEntry.setStatus("current")
_CfprApFirmwareBundleInfoDigestInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareBundleInfoDigestInstanceId_Object = MibTableColumn
cfprApFirmwareBundleInfoDigestInstanceId = _CfprApFirmwareBundleInfoDigestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 7, 1, 1),
    _CfprApFirmwareBundleInfoDigestInstanceId_Type()
)
cfprApFirmwareBundleInfoDigestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoDigestInstanceId.setStatus("current")
_CfprApFirmwareBundleInfoDigestDn_Type = CfprApManagedObjectDn
_CfprApFirmwareBundleInfoDigestDn_Object = MibTableColumn
cfprApFirmwareBundleInfoDigestDn = _CfprApFirmwareBundleInfoDigestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 7, 1, 2),
    _CfprApFirmwareBundleInfoDigestDn_Type()
)
cfprApFirmwareBundleInfoDigestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoDigestDn.setStatus("current")
_CfprApFirmwareBundleInfoDigestRn_Type = SnmpAdminString
_CfprApFirmwareBundleInfoDigestRn_Object = MibTableColumn
cfprApFirmwareBundleInfoDigestRn = _CfprApFirmwareBundleInfoDigestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 7, 1, 3),
    _CfprApFirmwareBundleInfoDigestRn_Type()
)
cfprApFirmwareBundleInfoDigestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoDigestRn.setStatus("current")
_CfprApFirmwareBundleInfoDigestBundleName_Type = SnmpAdminString
_CfprApFirmwareBundleInfoDigestBundleName_Object = MibTableColumn
cfprApFirmwareBundleInfoDigestBundleName = _CfprApFirmwareBundleInfoDigestBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 7, 1, 4),
    _CfprApFirmwareBundleInfoDigestBundleName_Type()
)
cfprApFirmwareBundleInfoDigestBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoDigestBundleName.setStatus("current")
_CfprApFirmwareBundleInfoDigestType_Type = CfprApFirmwareDistributableType
_CfprApFirmwareBundleInfoDigestType_Object = MibTableColumn
cfprApFirmwareBundleInfoDigestType = _CfprApFirmwareBundleInfoDigestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 7, 1, 5),
    _CfprApFirmwareBundleInfoDigestType_Type()
)
cfprApFirmwareBundleInfoDigestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoDigestType.setStatus("current")
_CfprApFirmwareBundleInfoDigestVersion_Type = SnmpAdminString
_CfprApFirmwareBundleInfoDigestVersion_Object = MibTableColumn
cfprApFirmwareBundleInfoDigestVersion = _CfprApFirmwareBundleInfoDigestVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 7, 1, 6),
    _CfprApFirmwareBundleInfoDigestVersion_Type()
)
cfprApFirmwareBundleInfoDigestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleInfoDigestVersion.setStatus("current")
_CfprApFirmwareBundleTypeTable_Object = MibTable
cfprApFirmwareBundleTypeTable = _CfprApFirmwareBundleTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 8)
)
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeTable.setStatus("current")
_CfprApFirmwareBundleTypeEntry_Object = MibTableRow
cfprApFirmwareBundleTypeEntry = _CfprApFirmwareBundleTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 8, 1)
)
cfprApFirmwareBundleTypeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareBundleTypeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeEntry.setStatus("current")
_CfprApFirmwareBundleTypeInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareBundleTypeInstanceId_Object = MibTableColumn
cfprApFirmwareBundleTypeInstanceId = _CfprApFirmwareBundleTypeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 8, 1, 1),
    _CfprApFirmwareBundleTypeInstanceId_Type()
)
cfprApFirmwareBundleTypeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeInstanceId.setStatus("current")
_CfprApFirmwareBundleTypeDn_Type = CfprApManagedObjectDn
_CfprApFirmwareBundleTypeDn_Object = MibTableColumn
cfprApFirmwareBundleTypeDn = _CfprApFirmwareBundleTypeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 8, 1, 2),
    _CfprApFirmwareBundleTypeDn_Type()
)
cfprApFirmwareBundleTypeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeDn.setStatus("current")
_CfprApFirmwareBundleTypeRn_Type = SnmpAdminString
_CfprApFirmwareBundleTypeRn_Object = MibTableColumn
cfprApFirmwareBundleTypeRn = _CfprApFirmwareBundleTypeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 8, 1, 3),
    _CfprApFirmwareBundleTypeRn_Type()
)
cfprApFirmwareBundleTypeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeRn.setStatus("current")
_CfprApFirmwareBundleTypeInvTag_Type = SnmpAdminString
_CfprApFirmwareBundleTypeInvTag_Object = MibTableColumn
cfprApFirmwareBundleTypeInvTag = _CfprApFirmwareBundleTypeInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 8, 1, 4),
    _CfprApFirmwareBundleTypeInvTag_Type()
)
cfprApFirmwareBundleTypeInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeInvTag.setStatus("current")
_CfprApFirmwareBundleTypeType_Type = CfprApFirmwareDistributableType
_CfprApFirmwareBundleTypeType_Object = MibTableColumn
cfprApFirmwareBundleTypeType = _CfprApFirmwareBundleTypeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 8, 1, 5),
    _CfprApFirmwareBundleTypeType_Type()
)
cfprApFirmwareBundleTypeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeType.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderTable_Object = MibTable
cfprApFirmwareBundleTypeCapProviderTable = _CfprApFirmwareBundleTypeCapProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9)
)
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderTable.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderEntry_Object = MibTableRow
cfprApFirmwareBundleTypeCapProviderEntry = _CfprApFirmwareBundleTypeCapProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1)
)
cfprApFirmwareBundleTypeCapProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareBundleTypeCapProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderEntry.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareBundleTypeCapProviderInstanceId_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderInstanceId = _CfprApFirmwareBundleTypeCapProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 1),
    _CfprApFirmwareBundleTypeCapProviderInstanceId_Type()
)
cfprApFirmwareBundleTypeCapProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderInstanceId.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderDn_Type = CfprApManagedObjectDn
_CfprApFirmwareBundleTypeCapProviderDn_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderDn = _CfprApFirmwareBundleTypeCapProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 2),
    _CfprApFirmwareBundleTypeCapProviderDn_Type()
)
cfprApFirmwareBundleTypeCapProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderDn.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderRn_Type = SnmpAdminString
_CfprApFirmwareBundleTypeCapProviderRn_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderRn = _CfprApFirmwareBundleTypeCapProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 3),
    _CfprApFirmwareBundleTypeCapProviderRn_Type()
)
cfprApFirmwareBundleTypeCapProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderRn.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderDeleted_Type = TruthValue
_CfprApFirmwareBundleTypeCapProviderDeleted_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderDeleted = _CfprApFirmwareBundleTypeCapProviderDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 4),
    _CfprApFirmwareBundleTypeCapProviderDeleted_Type()
)
cfprApFirmwareBundleTypeCapProviderDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderDeleted.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderDeprecated_Type = TruthValue
_CfprApFirmwareBundleTypeCapProviderDeprecated_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderDeprecated = _CfprApFirmwareBundleTypeCapProviderDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 5),
    _CfprApFirmwareBundleTypeCapProviderDeprecated_Type()
)
cfprApFirmwareBundleTypeCapProviderDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderDeprecated.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderElementLoadFailures_Type = Gauge32
_CfprApFirmwareBundleTypeCapProviderElementLoadFailures_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderElementLoadFailures = _CfprApFirmwareBundleTypeCapProviderElementLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 6),
    _CfprApFirmwareBundleTypeCapProviderElementLoadFailures_Type()
)
cfprApFirmwareBundleTypeCapProviderElementLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderElementLoadFailures.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderElementsLoaded_Type = Gauge32
_CfprApFirmwareBundleTypeCapProviderElementsLoaded_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderElementsLoaded = _CfprApFirmwareBundleTypeCapProviderElementsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 7),
    _CfprApFirmwareBundleTypeCapProviderElementsLoaded_Type()
)
cfprApFirmwareBundleTypeCapProviderElementsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderElementsLoaded.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderGencount_Type = Gauge32
_CfprApFirmwareBundleTypeCapProviderGencount_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderGencount = _CfprApFirmwareBundleTypeCapProviderGencount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 8),
    _CfprApFirmwareBundleTypeCapProviderGencount_Type()
)
cfprApFirmwareBundleTypeCapProviderGencount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderGencount.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderLoadErrors_Type = Gauge32
_CfprApFirmwareBundleTypeCapProviderLoadErrors_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderLoadErrors = _CfprApFirmwareBundleTypeCapProviderLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 9),
    _CfprApFirmwareBundleTypeCapProviderLoadErrors_Type()
)
cfprApFirmwareBundleTypeCapProviderLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderLoadErrors.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderLoadWarnings_Type = Gauge32
_CfprApFirmwareBundleTypeCapProviderLoadWarnings_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderLoadWarnings = _CfprApFirmwareBundleTypeCapProviderLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 10),
    _CfprApFirmwareBundleTypeCapProviderLoadWarnings_Type()
)
cfprApFirmwareBundleTypeCapProviderLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderLoadWarnings.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderMgmtPlaneVer_Type = SnmpAdminString
_CfprApFirmwareBundleTypeCapProviderMgmtPlaneVer_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderMgmtPlaneVer = _CfprApFirmwareBundleTypeCapProviderMgmtPlaneVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 11),
    _CfprApFirmwareBundleTypeCapProviderMgmtPlaneVer_Type()
)
cfprApFirmwareBundleTypeCapProviderMgmtPlaneVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderMgmtPlaneVer.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderModel_Type = SnmpAdminString
_CfprApFirmwareBundleTypeCapProviderModel_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderModel = _CfprApFirmwareBundleTypeCapProviderModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 12),
    _CfprApFirmwareBundleTypeCapProviderModel_Type()
)
cfprApFirmwareBundleTypeCapProviderModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderModel.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderPlatformType_Type = CfprApFirmwarePlatformType
_CfprApFirmwareBundleTypeCapProviderPlatformType_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderPlatformType = _CfprApFirmwareBundleTypeCapProviderPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 13),
    _CfprApFirmwareBundleTypeCapProviderPlatformType_Type()
)
cfprApFirmwareBundleTypeCapProviderPlatformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderPlatformType.setStatus("current")
_CfprApFirmwareBundleTypeCapProviderVendor_Type = SnmpAdminString
_CfprApFirmwareBundleTypeCapProviderVendor_Object = MibTableColumn
cfprApFirmwareBundleTypeCapProviderVendor = _CfprApFirmwareBundleTypeCapProviderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 9, 1, 14),
    _CfprApFirmwareBundleTypeCapProviderVendor_Type()
)
cfprApFirmwareBundleTypeCapProviderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareBundleTypeCapProviderVendor.setStatus("current")
_CfprApFirmwareCatalogPackTable_Object = MibTable
cfprApFirmwareCatalogPackTable = _CfprApFirmwareCatalogPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10)
)
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackTable.setStatus("current")
_CfprApFirmwareCatalogPackEntry_Object = MibTableRow
cfprApFirmwareCatalogPackEntry = _CfprApFirmwareCatalogPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1)
)
cfprApFirmwareCatalogPackEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareCatalogPackInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackEntry.setStatus("current")
_CfprApFirmwareCatalogPackInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareCatalogPackInstanceId_Object = MibTableColumn
cfprApFirmwareCatalogPackInstanceId = _CfprApFirmwareCatalogPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 1),
    _CfprApFirmwareCatalogPackInstanceId_Type()
)
cfprApFirmwareCatalogPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackInstanceId.setStatus("current")
_CfprApFirmwareCatalogPackDn_Type = CfprApManagedObjectDn
_CfprApFirmwareCatalogPackDn_Object = MibTableColumn
cfprApFirmwareCatalogPackDn = _CfprApFirmwareCatalogPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 2),
    _CfprApFirmwareCatalogPackDn_Type()
)
cfprApFirmwareCatalogPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackDn.setStatus("current")
_CfprApFirmwareCatalogPackRn_Type = SnmpAdminString
_CfprApFirmwareCatalogPackRn_Object = MibTableColumn
cfprApFirmwareCatalogPackRn = _CfprApFirmwareCatalogPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 3),
    _CfprApFirmwareCatalogPackRn_Type()
)
cfprApFirmwareCatalogPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackRn.setStatus("current")
_CfprApFirmwareCatalogPackCatalogName_Type = SnmpAdminString
_CfprApFirmwareCatalogPackCatalogName_Object = MibTableColumn
cfprApFirmwareCatalogPackCatalogName = _CfprApFirmwareCatalogPackCatalogName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 4),
    _CfprApFirmwareCatalogPackCatalogName_Type()
)
cfprApFirmwareCatalogPackCatalogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackCatalogName.setStatus("current")
_CfprApFirmwareCatalogPackCatalogVersion_Type = SnmpAdminString
_CfprApFirmwareCatalogPackCatalogVersion_Object = MibTableColumn
cfprApFirmwareCatalogPackCatalogVersion = _CfprApFirmwareCatalogPackCatalogVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 5),
    _CfprApFirmwareCatalogPackCatalogVersion_Type()
)
cfprApFirmwareCatalogPackCatalogVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackCatalogVersion.setStatus("current")
_CfprApFirmwareCatalogPackConfigState_Type = CfprApFirmwareCatalogPackConfigState
_CfprApFirmwareCatalogPackConfigState_Object = MibTableColumn
cfprApFirmwareCatalogPackConfigState = _CfprApFirmwareCatalogPackConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 6),
    _CfprApFirmwareCatalogPackConfigState_Type()
)
cfprApFirmwareCatalogPackConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackConfigState.setStatus("current")
_CfprApFirmwareCatalogPackConfigStatusMessage_Type = SnmpAdminString
_CfprApFirmwareCatalogPackConfigStatusMessage_Object = MibTableColumn
cfprApFirmwareCatalogPackConfigStatusMessage = _CfprApFirmwareCatalogPackConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 7),
    _CfprApFirmwareCatalogPackConfigStatusMessage_Type()
)
cfprApFirmwareCatalogPackConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackConfigStatusMessage.setStatus("current")
_CfprApFirmwareCatalogPackDescr_Type = SnmpAdminString
_CfprApFirmwareCatalogPackDescr_Object = MibTableColumn
cfprApFirmwareCatalogPackDescr = _CfprApFirmwareCatalogPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 8),
    _CfprApFirmwareCatalogPackDescr_Type()
)
cfprApFirmwareCatalogPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackDescr.setStatus("current")
_CfprApFirmwareCatalogPackIntId_Type = SnmpAdminString
_CfprApFirmwareCatalogPackIntId_Object = MibTableColumn
cfprApFirmwareCatalogPackIntId = _CfprApFirmwareCatalogPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 9),
    _CfprApFirmwareCatalogPackIntId_Type()
)
cfprApFirmwareCatalogPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackIntId.setStatus("current")
_CfprApFirmwareCatalogPackMode_Type = CfprApFirmwarePackMode
_CfprApFirmwareCatalogPackMode_Object = MibTableColumn
cfprApFirmwareCatalogPackMode = _CfprApFirmwareCatalogPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 10),
    _CfprApFirmwareCatalogPackMode_Type()
)
cfprApFirmwareCatalogPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackMode.setStatus("current")
_CfprApFirmwareCatalogPackName_Type = SnmpAdminString
_CfprApFirmwareCatalogPackName_Object = MibTableColumn
cfprApFirmwareCatalogPackName = _CfprApFirmwareCatalogPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 11),
    _CfprApFirmwareCatalogPackName_Type()
)
cfprApFirmwareCatalogPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackName.setStatus("current")
_CfprApFirmwareCatalogPackPolicyLevel_Type = Gauge32
_CfprApFirmwareCatalogPackPolicyLevel_Object = MibTableColumn
cfprApFirmwareCatalogPackPolicyLevel = _CfprApFirmwareCatalogPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 12),
    _CfprApFirmwareCatalogPackPolicyLevel_Type()
)
cfprApFirmwareCatalogPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackPolicyLevel.setStatus("current")
_CfprApFirmwareCatalogPackPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwareCatalogPackPolicyOwner_Object = MibTableColumn
cfprApFirmwareCatalogPackPolicyOwner = _CfprApFirmwareCatalogPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 13),
    _CfprApFirmwareCatalogPackPolicyOwner_Type()
)
cfprApFirmwareCatalogPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackPolicyOwner.setStatus("current")
_CfprApFirmwareCatalogPackStageSize_Type = Gauge32
_CfprApFirmwareCatalogPackStageSize_Object = MibTableColumn
cfprApFirmwareCatalogPackStageSize = _CfprApFirmwareCatalogPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 14),
    _CfprApFirmwareCatalogPackStageSize_Type()
)
cfprApFirmwareCatalogPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackStageSize.setStatus("current")
_CfprApFirmwareCatalogPackUpdateTrigger_Type = DateAndTime
_CfprApFirmwareCatalogPackUpdateTrigger_Object = MibTableColumn
cfprApFirmwareCatalogPackUpdateTrigger = _CfprApFirmwareCatalogPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 10, 1, 15),
    _CfprApFirmwareCatalogPackUpdateTrigger_Type()
)
cfprApFirmwareCatalogPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogPackUpdateTrigger.setStatus("current")
_CfprApFirmwareCatalogueTable_Object = MibTable
cfprApFirmwareCatalogueTable = _CfprApFirmwareCatalogueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 11)
)
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogueTable.setStatus("current")
_CfprApFirmwareCatalogueEntry_Object = MibTableRow
cfprApFirmwareCatalogueEntry = _CfprApFirmwareCatalogueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 11, 1)
)
cfprApFirmwareCatalogueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareCatalogueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogueEntry.setStatus("current")
_CfprApFirmwareCatalogueInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareCatalogueInstanceId_Object = MibTableColumn
cfprApFirmwareCatalogueInstanceId = _CfprApFirmwareCatalogueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 11, 1, 1),
    _CfprApFirmwareCatalogueInstanceId_Type()
)
cfprApFirmwareCatalogueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogueInstanceId.setStatus("current")
_CfprApFirmwareCatalogueDn_Type = CfprApManagedObjectDn
_CfprApFirmwareCatalogueDn_Object = MibTableColumn
cfprApFirmwareCatalogueDn = _CfprApFirmwareCatalogueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 11, 1, 2),
    _CfprApFirmwareCatalogueDn_Type()
)
cfprApFirmwareCatalogueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogueDn.setStatus("current")
_CfprApFirmwareCatalogueRn_Type = SnmpAdminString
_CfprApFirmwareCatalogueRn_Object = MibTableColumn
cfprApFirmwareCatalogueRn = _CfprApFirmwareCatalogueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 11, 1, 3),
    _CfprApFirmwareCatalogueRn_Type()
)
cfprApFirmwareCatalogueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogueRn.setStatus("current")
_CfprApFirmwareCatalogueSyncTrigger_Type = TruthValue
_CfprApFirmwareCatalogueSyncTrigger_Object = MibTableColumn
cfprApFirmwareCatalogueSyncTrigger = _CfprApFirmwareCatalogueSyncTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 11, 1, 4),
    _CfprApFirmwareCatalogueSyncTrigger_Type()
)
cfprApFirmwareCatalogueSyncTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCatalogueSyncTrigger.setStatus("current")
_CfprApFirmwareCompSourceTable_Object = MibTable
cfprApFirmwareCompSourceTable = _CfprApFirmwareCompSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 12)
)
if mibBuilder.loadTexts:
    cfprApFirmwareCompSourceTable.setStatus("current")
_CfprApFirmwareCompSourceEntry_Object = MibTableRow
cfprApFirmwareCompSourceEntry = _CfprApFirmwareCompSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 12, 1)
)
cfprApFirmwareCompSourceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareCompSourceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareCompSourceEntry.setStatus("current")
_CfprApFirmwareCompSourceInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareCompSourceInstanceId_Object = MibTableColumn
cfprApFirmwareCompSourceInstanceId = _CfprApFirmwareCompSourceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 12, 1, 1),
    _CfprApFirmwareCompSourceInstanceId_Type()
)
cfprApFirmwareCompSourceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareCompSourceInstanceId.setStatus("current")
_CfprApFirmwareCompSourceDn_Type = CfprApManagedObjectDn
_CfprApFirmwareCompSourceDn_Object = MibTableColumn
cfprApFirmwareCompSourceDn = _CfprApFirmwareCompSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 12, 1, 2),
    _CfprApFirmwareCompSourceDn_Type()
)
cfprApFirmwareCompSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompSourceDn.setStatus("current")
_CfprApFirmwareCompSourceRn_Type = SnmpAdminString
_CfprApFirmwareCompSourceRn_Object = MibTableColumn
cfprApFirmwareCompSourceRn = _CfprApFirmwareCompSourceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 12, 1, 3),
    _CfprApFirmwareCompSourceRn_Type()
)
cfprApFirmwareCompSourceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompSourceRn.setStatus("current")
_CfprApFirmwareCompSourceDescr_Type = SnmpAdminString
_CfprApFirmwareCompSourceDescr_Object = MibTableColumn
cfprApFirmwareCompSourceDescr = _CfprApFirmwareCompSourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 12, 1, 4),
    _CfprApFirmwareCompSourceDescr_Type()
)
cfprApFirmwareCompSourceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompSourceDescr.setStatus("current")
_CfprApFirmwareCompSourceIntId_Type = SnmpAdminString
_CfprApFirmwareCompSourceIntId_Object = MibTableColumn
cfprApFirmwareCompSourceIntId = _CfprApFirmwareCompSourceIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 12, 1, 5),
    _CfprApFirmwareCompSourceIntId_Type()
)
cfprApFirmwareCompSourceIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompSourceIntId.setStatus("current")
_CfprApFirmwareCompSourceInvTag_Type = SnmpAdminString
_CfprApFirmwareCompSourceInvTag_Object = MibTableColumn
cfprApFirmwareCompSourceInvTag = _CfprApFirmwareCompSourceInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 12, 1, 6),
    _CfprApFirmwareCompSourceInvTag_Type()
)
cfprApFirmwareCompSourceInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompSourceInvTag.setStatus("current")
_CfprApFirmwareCompSourceName_Type = SnmpAdminString
_CfprApFirmwareCompSourceName_Object = MibTableColumn
cfprApFirmwareCompSourceName = _CfprApFirmwareCompSourceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 12, 1, 7),
    _CfprApFirmwareCompSourceName_Type()
)
cfprApFirmwareCompSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompSourceName.setStatus("current")
_CfprApFirmwareCompSourcePolicyLevel_Type = Gauge32
_CfprApFirmwareCompSourcePolicyLevel_Object = MibTableColumn
cfprApFirmwareCompSourcePolicyLevel = _CfprApFirmwareCompSourcePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 12, 1, 8),
    _CfprApFirmwareCompSourcePolicyLevel_Type()
)
cfprApFirmwareCompSourcePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompSourcePolicyLevel.setStatus("current")
_CfprApFirmwareCompSourcePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwareCompSourcePolicyOwner_Object = MibTableColumn
cfprApFirmwareCompSourcePolicyOwner = _CfprApFirmwareCompSourcePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 12, 1, 9),
    _CfprApFirmwareCompSourcePolicyOwner_Type()
)
cfprApFirmwareCompSourcePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompSourcePolicyOwner.setStatus("current")
_CfprApFirmwareCompSourceVersion_Type = SnmpAdminString
_CfprApFirmwareCompSourceVersion_Object = MibTableColumn
cfprApFirmwareCompSourceVersion = _CfprApFirmwareCompSourceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 12, 1, 10),
    _CfprApFirmwareCompSourceVersion_Type()
)
cfprApFirmwareCompSourceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompSourceVersion.setStatus("current")
_CfprApFirmwareCompTargetTable_Object = MibTable
cfprApFirmwareCompTargetTable = _CfprApFirmwareCompTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 13)
)
if mibBuilder.loadTexts:
    cfprApFirmwareCompTargetTable.setStatus("current")
_CfprApFirmwareCompTargetEntry_Object = MibTableRow
cfprApFirmwareCompTargetEntry = _CfprApFirmwareCompTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 13, 1)
)
cfprApFirmwareCompTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareCompTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareCompTargetEntry.setStatus("current")
_CfprApFirmwareCompTargetInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareCompTargetInstanceId_Object = MibTableColumn
cfprApFirmwareCompTargetInstanceId = _CfprApFirmwareCompTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 13, 1, 1),
    _CfprApFirmwareCompTargetInstanceId_Type()
)
cfprApFirmwareCompTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareCompTargetInstanceId.setStatus("current")
_CfprApFirmwareCompTargetDn_Type = CfprApManagedObjectDn
_CfprApFirmwareCompTargetDn_Object = MibTableColumn
cfprApFirmwareCompTargetDn = _CfprApFirmwareCompTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 13, 1, 2),
    _CfprApFirmwareCompTargetDn_Type()
)
cfprApFirmwareCompTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompTargetDn.setStatus("current")
_CfprApFirmwareCompTargetRn_Type = SnmpAdminString
_CfprApFirmwareCompTargetRn_Object = MibTableColumn
cfprApFirmwareCompTargetRn = _CfprApFirmwareCompTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 13, 1, 3),
    _CfprApFirmwareCompTargetRn_Type()
)
cfprApFirmwareCompTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompTargetRn.setStatus("current")
_CfprApFirmwareCompTargetDescr_Type = SnmpAdminString
_CfprApFirmwareCompTargetDescr_Object = MibTableColumn
cfprApFirmwareCompTargetDescr = _CfprApFirmwareCompTargetDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 13, 1, 4),
    _CfprApFirmwareCompTargetDescr_Type()
)
cfprApFirmwareCompTargetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompTargetDescr.setStatus("current")
_CfprApFirmwareCompTargetIntId_Type = SnmpAdminString
_CfprApFirmwareCompTargetIntId_Object = MibTableColumn
cfprApFirmwareCompTargetIntId = _CfprApFirmwareCompTargetIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 13, 1, 5),
    _CfprApFirmwareCompTargetIntId_Type()
)
cfprApFirmwareCompTargetIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompTargetIntId.setStatus("current")
_CfprApFirmwareCompTargetInvTag_Type = SnmpAdminString
_CfprApFirmwareCompTargetInvTag_Object = MibTableColumn
cfprApFirmwareCompTargetInvTag = _CfprApFirmwareCompTargetInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 13, 1, 6),
    _CfprApFirmwareCompTargetInvTag_Type()
)
cfprApFirmwareCompTargetInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompTargetInvTag.setStatus("current")
_CfprApFirmwareCompTargetName_Type = SnmpAdminString
_CfprApFirmwareCompTargetName_Object = MibTableColumn
cfprApFirmwareCompTargetName = _CfprApFirmwareCompTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 13, 1, 7),
    _CfprApFirmwareCompTargetName_Type()
)
cfprApFirmwareCompTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompTargetName.setStatus("current")
_CfprApFirmwareCompTargetPolicyLevel_Type = Gauge32
_CfprApFirmwareCompTargetPolicyLevel_Object = MibTableColumn
cfprApFirmwareCompTargetPolicyLevel = _CfprApFirmwareCompTargetPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 13, 1, 8),
    _CfprApFirmwareCompTargetPolicyLevel_Type()
)
cfprApFirmwareCompTargetPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompTargetPolicyLevel.setStatus("current")
_CfprApFirmwareCompTargetPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwareCompTargetPolicyOwner_Object = MibTableColumn
cfprApFirmwareCompTargetPolicyOwner = _CfprApFirmwareCompTargetPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 13, 1, 9),
    _CfprApFirmwareCompTargetPolicyOwner_Type()
)
cfprApFirmwareCompTargetPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompTargetPolicyOwner.setStatus("current")
_CfprApFirmwareCompTargetVersion_Type = SnmpAdminString
_CfprApFirmwareCompTargetVersion_Object = MibTableColumn
cfprApFirmwareCompTargetVersion = _CfprApFirmwareCompTargetVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 13, 1, 10),
    _CfprApFirmwareCompTargetVersion_Type()
)
cfprApFirmwareCompTargetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCompTargetVersion.setStatus("current")
_CfprApFirmwareComputeHostPackTable_Object = MibTable
cfprApFirmwareComputeHostPackTable = _CfprApFirmwareComputeHostPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14)
)
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackTable.setStatus("current")
_CfprApFirmwareComputeHostPackEntry_Object = MibTableRow
cfprApFirmwareComputeHostPackEntry = _CfprApFirmwareComputeHostPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1)
)
cfprApFirmwareComputeHostPackEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareComputeHostPackInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackEntry.setStatus("current")
_CfprApFirmwareComputeHostPackInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareComputeHostPackInstanceId_Object = MibTableColumn
cfprApFirmwareComputeHostPackInstanceId = _CfprApFirmwareComputeHostPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 1),
    _CfprApFirmwareComputeHostPackInstanceId_Type()
)
cfprApFirmwareComputeHostPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackInstanceId.setStatus("current")
_CfprApFirmwareComputeHostPackDn_Type = CfprApManagedObjectDn
_CfprApFirmwareComputeHostPackDn_Object = MibTableColumn
cfprApFirmwareComputeHostPackDn = _CfprApFirmwareComputeHostPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 2),
    _CfprApFirmwareComputeHostPackDn_Type()
)
cfprApFirmwareComputeHostPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackDn.setStatus("current")
_CfprApFirmwareComputeHostPackRn_Type = SnmpAdminString
_CfprApFirmwareComputeHostPackRn_Object = MibTableColumn
cfprApFirmwareComputeHostPackRn = _CfprApFirmwareComputeHostPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 3),
    _CfprApFirmwareComputeHostPackRn_Type()
)
cfprApFirmwareComputeHostPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackRn.setStatus("current")
_CfprApFirmwareComputeHostPackBladeBundleName_Type = SnmpAdminString
_CfprApFirmwareComputeHostPackBladeBundleName_Object = MibTableColumn
cfprApFirmwareComputeHostPackBladeBundleName = _CfprApFirmwareComputeHostPackBladeBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 4),
    _CfprApFirmwareComputeHostPackBladeBundleName_Type()
)
cfprApFirmwareComputeHostPackBladeBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackBladeBundleName.setStatus("current")
_CfprApFirmwareComputeHostPackBladeBundleVersion_Type = SnmpAdminString
_CfprApFirmwareComputeHostPackBladeBundleVersion_Object = MibTableColumn
cfprApFirmwareComputeHostPackBladeBundleVersion = _CfprApFirmwareComputeHostPackBladeBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 5),
    _CfprApFirmwareComputeHostPackBladeBundleVersion_Type()
)
cfprApFirmwareComputeHostPackBladeBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackBladeBundleVersion.setStatus("current")
_CfprApFirmwareComputeHostPackConfigQualifier_Type = CfprApFirmwareHostPackConfigQualifier
_CfprApFirmwareComputeHostPackConfigQualifier_Object = MibTableColumn
cfprApFirmwareComputeHostPackConfigQualifier = _CfprApFirmwareComputeHostPackConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 6),
    _CfprApFirmwareComputeHostPackConfigQualifier_Type()
)
cfprApFirmwareComputeHostPackConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackConfigQualifier.setStatus("current")
_CfprApFirmwareComputeHostPackDescr_Type = SnmpAdminString
_CfprApFirmwareComputeHostPackDescr_Object = MibTableColumn
cfprApFirmwareComputeHostPackDescr = _CfprApFirmwareComputeHostPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 7),
    _CfprApFirmwareComputeHostPackDescr_Type()
)
cfprApFirmwareComputeHostPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackDescr.setStatus("current")
_CfprApFirmwareComputeHostPackIgnoreCompCheck_Type = TruthValue
_CfprApFirmwareComputeHostPackIgnoreCompCheck_Object = MibTableColumn
cfprApFirmwareComputeHostPackIgnoreCompCheck = _CfprApFirmwareComputeHostPackIgnoreCompCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 8),
    _CfprApFirmwareComputeHostPackIgnoreCompCheck_Type()
)
cfprApFirmwareComputeHostPackIgnoreCompCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackIgnoreCompCheck.setStatus("current")
_CfprApFirmwareComputeHostPackIntId_Type = SnmpAdminString
_CfprApFirmwareComputeHostPackIntId_Object = MibTableColumn
cfprApFirmwareComputeHostPackIntId = _CfprApFirmwareComputeHostPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 9),
    _CfprApFirmwareComputeHostPackIntId_Type()
)
cfprApFirmwareComputeHostPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackIntId.setStatus("current")
_CfprApFirmwareComputeHostPackMode_Type = CfprApFirmwarePackMode
_CfprApFirmwareComputeHostPackMode_Object = MibTableColumn
cfprApFirmwareComputeHostPackMode = _CfprApFirmwareComputeHostPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 10),
    _CfprApFirmwareComputeHostPackMode_Type()
)
cfprApFirmwareComputeHostPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackMode.setStatus("current")
_CfprApFirmwareComputeHostPackName_Type = SnmpAdminString
_CfprApFirmwareComputeHostPackName_Object = MibTableColumn
cfprApFirmwareComputeHostPackName = _CfprApFirmwareComputeHostPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 11),
    _CfprApFirmwareComputeHostPackName_Type()
)
cfprApFirmwareComputeHostPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackName.setStatus("current")
_CfprApFirmwareComputeHostPackPlatformBundleVersion_Type = SnmpAdminString
_CfprApFirmwareComputeHostPackPlatformBundleVersion_Object = MibTableColumn
cfprApFirmwareComputeHostPackPlatformBundleVersion = _CfprApFirmwareComputeHostPackPlatformBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 12),
    _CfprApFirmwareComputeHostPackPlatformBundleVersion_Type()
)
cfprApFirmwareComputeHostPackPlatformBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackPlatformBundleVersion.setStatus("current")
_CfprApFirmwareComputeHostPackPolicyLevel_Type = Gauge32
_CfprApFirmwareComputeHostPackPolicyLevel_Object = MibTableColumn
cfprApFirmwareComputeHostPackPolicyLevel = _CfprApFirmwareComputeHostPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 13),
    _CfprApFirmwareComputeHostPackPolicyLevel_Type()
)
cfprApFirmwareComputeHostPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackPolicyLevel.setStatus("current")
_CfprApFirmwareComputeHostPackPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwareComputeHostPackPolicyOwner_Object = MibTableColumn
cfprApFirmwareComputeHostPackPolicyOwner = _CfprApFirmwareComputeHostPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 14),
    _CfprApFirmwareComputeHostPackPolicyOwner_Type()
)
cfprApFirmwareComputeHostPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackPolicyOwner.setStatus("current")
_CfprApFirmwareComputeHostPackRackBundleName_Type = SnmpAdminString
_CfprApFirmwareComputeHostPackRackBundleName_Object = MibTableColumn
cfprApFirmwareComputeHostPackRackBundleName = _CfprApFirmwareComputeHostPackRackBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 15),
    _CfprApFirmwareComputeHostPackRackBundleName_Type()
)
cfprApFirmwareComputeHostPackRackBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackRackBundleName.setStatus("current")
_CfprApFirmwareComputeHostPackRackBundleVersion_Type = SnmpAdminString
_CfprApFirmwareComputeHostPackRackBundleVersion_Object = MibTableColumn
cfprApFirmwareComputeHostPackRackBundleVersion = _CfprApFirmwareComputeHostPackRackBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 16),
    _CfprApFirmwareComputeHostPackRackBundleVersion_Type()
)
cfprApFirmwareComputeHostPackRackBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackRackBundleVersion.setStatus("current")
_CfprApFirmwareComputeHostPackStageSize_Type = Gauge32
_CfprApFirmwareComputeHostPackStageSize_Object = MibTableColumn
cfprApFirmwareComputeHostPackStageSize = _CfprApFirmwareComputeHostPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 17),
    _CfprApFirmwareComputeHostPackStageSize_Type()
)
cfprApFirmwareComputeHostPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackStageSize.setStatus("current")
_CfprApFirmwareComputeHostPackUpdateTrigger_Type = DateAndTime
_CfprApFirmwareComputeHostPackUpdateTrigger_Object = MibTableColumn
cfprApFirmwareComputeHostPackUpdateTrigger = _CfprApFirmwareComputeHostPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 14, 1, 18),
    _CfprApFirmwareComputeHostPackUpdateTrigger_Type()
)
cfprApFirmwareComputeHostPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeHostPackUpdateTrigger.setStatus("current")
_CfprApFirmwareComputeMgmtPackTable_Object = MibTable
cfprApFirmwareComputeMgmtPackTable = _CfprApFirmwareComputeMgmtPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15)
)
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackTable.setStatus("current")
_CfprApFirmwareComputeMgmtPackEntry_Object = MibTableRow
cfprApFirmwareComputeMgmtPackEntry = _CfprApFirmwareComputeMgmtPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1)
)
cfprApFirmwareComputeMgmtPackEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareComputeMgmtPackInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackEntry.setStatus("current")
_CfprApFirmwareComputeMgmtPackInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareComputeMgmtPackInstanceId_Object = MibTableColumn
cfprApFirmwareComputeMgmtPackInstanceId = _CfprApFirmwareComputeMgmtPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1, 1),
    _CfprApFirmwareComputeMgmtPackInstanceId_Type()
)
cfprApFirmwareComputeMgmtPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackInstanceId.setStatus("current")
_CfprApFirmwareComputeMgmtPackDn_Type = CfprApManagedObjectDn
_CfprApFirmwareComputeMgmtPackDn_Object = MibTableColumn
cfprApFirmwareComputeMgmtPackDn = _CfprApFirmwareComputeMgmtPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1, 2),
    _CfprApFirmwareComputeMgmtPackDn_Type()
)
cfprApFirmwareComputeMgmtPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackDn.setStatus("current")
_CfprApFirmwareComputeMgmtPackRn_Type = SnmpAdminString
_CfprApFirmwareComputeMgmtPackRn_Object = MibTableColumn
cfprApFirmwareComputeMgmtPackRn = _CfprApFirmwareComputeMgmtPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1, 3),
    _CfprApFirmwareComputeMgmtPackRn_Type()
)
cfprApFirmwareComputeMgmtPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackRn.setStatus("current")
_CfprApFirmwareComputeMgmtPackDescr_Type = SnmpAdminString
_CfprApFirmwareComputeMgmtPackDescr_Object = MibTableColumn
cfprApFirmwareComputeMgmtPackDescr = _CfprApFirmwareComputeMgmtPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1, 4),
    _CfprApFirmwareComputeMgmtPackDescr_Type()
)
cfprApFirmwareComputeMgmtPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackDescr.setStatus("current")
_CfprApFirmwareComputeMgmtPackIgnoreCompCheck_Type = TruthValue
_CfprApFirmwareComputeMgmtPackIgnoreCompCheck_Object = MibTableColumn
cfprApFirmwareComputeMgmtPackIgnoreCompCheck = _CfprApFirmwareComputeMgmtPackIgnoreCompCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1, 5),
    _CfprApFirmwareComputeMgmtPackIgnoreCompCheck_Type()
)
cfprApFirmwareComputeMgmtPackIgnoreCompCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackIgnoreCompCheck.setStatus("current")
_CfprApFirmwareComputeMgmtPackIntId_Type = SnmpAdminString
_CfprApFirmwareComputeMgmtPackIntId_Object = MibTableColumn
cfprApFirmwareComputeMgmtPackIntId = _CfprApFirmwareComputeMgmtPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1, 6),
    _CfprApFirmwareComputeMgmtPackIntId_Type()
)
cfprApFirmwareComputeMgmtPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackIntId.setStatus("current")
_CfprApFirmwareComputeMgmtPackMode_Type = CfprApFirmwarePackMode
_CfprApFirmwareComputeMgmtPackMode_Object = MibTableColumn
cfprApFirmwareComputeMgmtPackMode = _CfprApFirmwareComputeMgmtPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1, 7),
    _CfprApFirmwareComputeMgmtPackMode_Type()
)
cfprApFirmwareComputeMgmtPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackMode.setStatus("current")
_CfprApFirmwareComputeMgmtPackName_Type = SnmpAdminString
_CfprApFirmwareComputeMgmtPackName_Object = MibTableColumn
cfprApFirmwareComputeMgmtPackName = _CfprApFirmwareComputeMgmtPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1, 8),
    _CfprApFirmwareComputeMgmtPackName_Type()
)
cfprApFirmwareComputeMgmtPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackName.setStatus("current")
_CfprApFirmwareComputeMgmtPackPolicyLevel_Type = Gauge32
_CfprApFirmwareComputeMgmtPackPolicyLevel_Object = MibTableColumn
cfprApFirmwareComputeMgmtPackPolicyLevel = _CfprApFirmwareComputeMgmtPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1, 9),
    _CfprApFirmwareComputeMgmtPackPolicyLevel_Type()
)
cfprApFirmwareComputeMgmtPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackPolicyLevel.setStatus("current")
_CfprApFirmwareComputeMgmtPackPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwareComputeMgmtPackPolicyOwner_Object = MibTableColumn
cfprApFirmwareComputeMgmtPackPolicyOwner = _CfprApFirmwareComputeMgmtPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1, 10),
    _CfprApFirmwareComputeMgmtPackPolicyOwner_Type()
)
cfprApFirmwareComputeMgmtPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackPolicyOwner.setStatus("current")
_CfprApFirmwareComputeMgmtPackStageSize_Type = Gauge32
_CfprApFirmwareComputeMgmtPackStageSize_Object = MibTableColumn
cfprApFirmwareComputeMgmtPackStageSize = _CfprApFirmwareComputeMgmtPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1, 11),
    _CfprApFirmwareComputeMgmtPackStageSize_Type()
)
cfprApFirmwareComputeMgmtPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackStageSize.setStatus("current")
_CfprApFirmwareComputeMgmtPackUpdateTrigger_Type = DateAndTime
_CfprApFirmwareComputeMgmtPackUpdateTrigger_Object = MibTableColumn
cfprApFirmwareComputeMgmtPackUpdateTrigger = _CfprApFirmwareComputeMgmtPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 15, 1, 12),
    _CfprApFirmwareComputeMgmtPackUpdateTrigger_Type()
)
cfprApFirmwareComputeMgmtPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareComputeMgmtPackUpdateTrigger.setStatus("current")
_CfprApFirmwareConstraintTable_Object = MibTable
cfprApFirmwareConstraintTable = _CfprApFirmwareConstraintTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 16)
)
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintTable.setStatus("current")
_CfprApFirmwareConstraintEntry_Object = MibTableRow
cfprApFirmwareConstraintEntry = _CfprApFirmwareConstraintEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 16, 1)
)
cfprApFirmwareConstraintEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareConstraintInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintEntry.setStatus("current")
_CfprApFirmwareConstraintInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareConstraintInstanceId_Object = MibTableColumn
cfprApFirmwareConstraintInstanceId = _CfprApFirmwareConstraintInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 16, 1, 1),
    _CfprApFirmwareConstraintInstanceId_Type()
)
cfprApFirmwareConstraintInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintInstanceId.setStatus("current")
_CfprApFirmwareConstraintDn_Type = CfprApManagedObjectDn
_CfprApFirmwareConstraintDn_Object = MibTableColumn
cfprApFirmwareConstraintDn = _CfprApFirmwareConstraintDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 16, 1, 2),
    _CfprApFirmwareConstraintDn_Type()
)
cfprApFirmwareConstraintDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintDn.setStatus("current")
_CfprApFirmwareConstraintRn_Type = SnmpAdminString
_CfprApFirmwareConstraintRn_Object = MibTableColumn
cfprApFirmwareConstraintRn = _CfprApFirmwareConstraintRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 16, 1, 3),
    _CfprApFirmwareConstraintRn_Type()
)
cfprApFirmwareConstraintRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintRn.setStatus("current")
_CfprApFirmwareConstraintFeature_Type = SnmpAdminString
_CfprApFirmwareConstraintFeature_Object = MibTableColumn
cfprApFirmwareConstraintFeature = _CfprApFirmwareConstraintFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 16, 1, 4),
    _CfprApFirmwareConstraintFeature_Type()
)
cfprApFirmwareConstraintFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintFeature.setStatus("current")
_CfprApFirmwareConstraintMinBiosVersion_Type = SnmpAdminString
_CfprApFirmwareConstraintMinBiosVersion_Object = MibTableColumn
cfprApFirmwareConstraintMinBiosVersion = _CfprApFirmwareConstraintMinBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 16, 1, 5),
    _CfprApFirmwareConstraintMinBiosVersion_Type()
)
cfprApFirmwareConstraintMinBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintMinBiosVersion.setStatus("current")
_CfprApFirmwareConstraintMinCimcVersion_Type = SnmpAdminString
_CfprApFirmwareConstraintMinCimcVersion_Object = MibTableColumn
cfprApFirmwareConstraintMinCimcVersion = _CfprApFirmwareConstraintMinCimcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 16, 1, 6),
    _CfprApFirmwareConstraintMinCimcVersion_Type()
)
cfprApFirmwareConstraintMinCimcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintMinCimcVersion.setStatus("current")
_CfprApFirmwareConstraintsTable_Object = MibTable
cfprApFirmwareConstraintsTable = _CfprApFirmwareConstraintsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 17)
)
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintsTable.setStatus("current")
_CfprApFirmwareConstraintsEntry_Object = MibTableRow
cfprApFirmwareConstraintsEntry = _CfprApFirmwareConstraintsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 17, 1)
)
cfprApFirmwareConstraintsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareConstraintsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintsEntry.setStatus("current")
_CfprApFirmwareConstraintsInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareConstraintsInstanceId_Object = MibTableColumn
cfprApFirmwareConstraintsInstanceId = _CfprApFirmwareConstraintsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 17, 1, 1),
    _CfprApFirmwareConstraintsInstanceId_Type()
)
cfprApFirmwareConstraintsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintsInstanceId.setStatus("current")
_CfprApFirmwareConstraintsDn_Type = CfprApManagedObjectDn
_CfprApFirmwareConstraintsDn_Object = MibTableColumn
cfprApFirmwareConstraintsDn = _CfprApFirmwareConstraintsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 17, 1, 2),
    _CfprApFirmwareConstraintsDn_Type()
)
cfprApFirmwareConstraintsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintsDn.setStatus("current")
_CfprApFirmwareConstraintsRn_Type = SnmpAdminString
_CfprApFirmwareConstraintsRn_Object = MibTableColumn
cfprApFirmwareConstraintsRn = _CfprApFirmwareConstraintsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 17, 1, 3),
    _CfprApFirmwareConstraintsRn_Type()
)
cfprApFirmwareConstraintsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareConstraintsRn.setStatus("current")
_CfprApFirmwareCspAppListTable_Object = MibTable
cfprApFirmwareCspAppListTable = _CfprApFirmwareCspAppListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 18)
)
if mibBuilder.loadTexts:
    cfprApFirmwareCspAppListTable.setStatus("current")
_CfprApFirmwareCspAppListEntry_Object = MibTableRow
cfprApFirmwareCspAppListEntry = _CfprApFirmwareCspAppListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 18, 1)
)
cfprApFirmwareCspAppListEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareCspAppListInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareCspAppListEntry.setStatus("current")
_CfprApFirmwareCspAppListInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareCspAppListInstanceId_Object = MibTableColumn
cfprApFirmwareCspAppListInstanceId = _CfprApFirmwareCspAppListInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 18, 1, 1),
    _CfprApFirmwareCspAppListInstanceId_Type()
)
cfprApFirmwareCspAppListInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareCspAppListInstanceId.setStatus("current")
_CfprApFirmwareCspAppListDn_Type = CfprApManagedObjectDn
_CfprApFirmwareCspAppListDn_Object = MibTableColumn
cfprApFirmwareCspAppListDn = _CfprApFirmwareCspAppListDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 18, 1, 2),
    _CfprApFirmwareCspAppListDn_Type()
)
cfprApFirmwareCspAppListDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCspAppListDn.setStatus("current")
_CfprApFirmwareCspAppListRn_Type = SnmpAdminString
_CfprApFirmwareCspAppListRn_Object = MibTableColumn
cfprApFirmwareCspAppListRn = _CfprApFirmwareCspAppListRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 18, 1, 3),
    _CfprApFirmwareCspAppListRn_Type()
)
cfprApFirmwareCspAppListRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCspAppListRn.setStatus("current")
_CfprApFirmwareCspAppListName_Type = SnmpAdminString
_CfprApFirmwareCspAppListName_Object = MibTableColumn
cfprApFirmwareCspAppListName = _CfprApFirmwareCspAppListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 18, 1, 4),
    _CfprApFirmwareCspAppListName_Type()
)
cfprApFirmwareCspAppListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCspAppListName.setStatus("current")
_CfprApFirmwareCspVersionTable_Object = MibTable
cfprApFirmwareCspVersionTable = _CfprApFirmwareCspVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 19)
)
if mibBuilder.loadTexts:
    cfprApFirmwareCspVersionTable.setStatus("current")
_CfprApFirmwareCspVersionEntry_Object = MibTableRow
cfprApFirmwareCspVersionEntry = _CfprApFirmwareCspVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 19, 1)
)
cfprApFirmwareCspVersionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareCspVersionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareCspVersionEntry.setStatus("current")
_CfprApFirmwareCspVersionInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareCspVersionInstanceId_Object = MibTableColumn
cfprApFirmwareCspVersionInstanceId = _CfprApFirmwareCspVersionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 19, 1, 1),
    _CfprApFirmwareCspVersionInstanceId_Type()
)
cfprApFirmwareCspVersionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareCspVersionInstanceId.setStatus("current")
_CfprApFirmwareCspVersionDn_Type = CfprApManagedObjectDn
_CfprApFirmwareCspVersionDn_Object = MibTableColumn
cfprApFirmwareCspVersionDn = _CfprApFirmwareCspVersionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 19, 1, 2),
    _CfprApFirmwareCspVersionDn_Type()
)
cfprApFirmwareCspVersionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCspVersionDn.setStatus("current")
_CfprApFirmwareCspVersionRn_Type = SnmpAdminString
_CfprApFirmwareCspVersionRn_Object = MibTableColumn
cfprApFirmwareCspVersionRn = _CfprApFirmwareCspVersionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 19, 1, 3),
    _CfprApFirmwareCspVersionRn_Type()
)
cfprApFirmwareCspVersionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCspVersionRn.setStatus("current")
_CfprApFirmwareCspVersionAppName_Type = SnmpAdminString
_CfprApFirmwareCspVersionAppName_Object = MibTableColumn
cfprApFirmwareCspVersionAppName = _CfprApFirmwareCspVersionAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 19, 1, 4),
    _CfprApFirmwareCspVersionAppName_Type()
)
cfprApFirmwareCspVersionAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCspVersionAppName.setStatus("current")
_CfprApFirmwareCspVersionFromVersion_Type = SnmpAdminString
_CfprApFirmwareCspVersionFromVersion_Object = MibTableColumn
cfprApFirmwareCspVersionFromVersion = _CfprApFirmwareCspVersionFromVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 19, 1, 5),
    _CfprApFirmwareCspVersionFromVersion_Type()
)
cfprApFirmwareCspVersionFromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCspVersionFromVersion.setStatus("current")
_CfprApFirmwareCspVersionName_Type = SnmpAdminString
_CfprApFirmwareCspVersionName_Object = MibTableColumn
cfprApFirmwareCspVersionName = _CfprApFirmwareCspVersionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 19, 1, 6),
    _CfprApFirmwareCspVersionName_Type()
)
cfprApFirmwareCspVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCspVersionName.setStatus("current")
_CfprApFirmwareCspVersionToVersion_Type = SnmpAdminString
_CfprApFirmwareCspVersionToVersion_Object = MibTableColumn
cfprApFirmwareCspVersionToVersion = _CfprApFirmwareCspVersionToVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 19, 1, 7),
    _CfprApFirmwareCspVersionToVersion_Type()
)
cfprApFirmwareCspVersionToVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareCspVersionToVersion.setStatus("current")
_CfprApFirmwareDependencyTable_Object = MibTable
cfprApFirmwareDependencyTable = _CfprApFirmwareDependencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20)
)
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyTable.setStatus("current")
_CfprApFirmwareDependencyEntry_Object = MibTableRow
cfprApFirmwareDependencyEntry = _CfprApFirmwareDependencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1)
)
cfprApFirmwareDependencyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareDependencyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyEntry.setStatus("current")
_CfprApFirmwareDependencyInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareDependencyInstanceId_Object = MibTableColumn
cfprApFirmwareDependencyInstanceId = _CfprApFirmwareDependencyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 1),
    _CfprApFirmwareDependencyInstanceId_Type()
)
cfprApFirmwareDependencyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyInstanceId.setStatus("current")
_CfprApFirmwareDependencyDn_Type = CfprApManagedObjectDn
_CfprApFirmwareDependencyDn_Object = MibTableColumn
cfprApFirmwareDependencyDn = _CfprApFirmwareDependencyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 2),
    _CfprApFirmwareDependencyDn_Type()
)
cfprApFirmwareDependencyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyDn.setStatus("current")
_CfprApFirmwareDependencyRn_Type = SnmpAdminString
_CfprApFirmwareDependencyRn_Object = MibTableColumn
cfprApFirmwareDependencyRn = _CfprApFirmwareDependencyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 3),
    _CfprApFirmwareDependencyRn_Type()
)
cfprApFirmwareDependencyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyRn.setStatus("current")
_CfprApFirmwareDependencyEp_Type = CfprApFirmwareType
_CfprApFirmwareDependencyEp_Object = MibTableColumn
cfprApFirmwareDependencyEp = _CfprApFirmwareDependencyEp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 4),
    _CfprApFirmwareDependencyEp_Type()
)
cfprApFirmwareDependencyEp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyEp.setStatus("current")
_CfprApFirmwareDependencyHwModel_Type = SnmpAdminString
_CfprApFirmwareDependencyHwModel_Object = MibTableColumn
cfprApFirmwareDependencyHwModel = _CfprApFirmwareDependencyHwModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 5),
    _CfprApFirmwareDependencyHwModel_Type()
)
cfprApFirmwareDependencyHwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyHwModel.setStatus("current")
_CfprApFirmwareDependencyHwRevision_Type = SnmpAdminString
_CfprApFirmwareDependencyHwRevision_Object = MibTableColumn
cfprApFirmwareDependencyHwRevision = _CfprApFirmwareDependencyHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 6),
    _CfprApFirmwareDependencyHwRevision_Type()
)
cfprApFirmwareDependencyHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyHwRevision.setStatus("current")
_CfprApFirmwareDependencyHwVendor_Type = SnmpAdminString
_CfprApFirmwareDependencyHwVendor_Object = MibTableColumn
cfprApFirmwareDependencyHwVendor = _CfprApFirmwareDependencyHwVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 7),
    _CfprApFirmwareDependencyHwVendor_Type()
)
cfprApFirmwareDependencyHwVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyHwVendor.setStatus("current")
_CfprApFirmwareDependencyInvTag_Type = SnmpAdminString
_CfprApFirmwareDependencyInvTag_Object = MibTableColumn
cfprApFirmwareDependencyInvTag = _CfprApFirmwareDependencyInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 8),
    _CfprApFirmwareDependencyInvTag_Type()
)
cfprApFirmwareDependencyInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyInvTag.setStatus("current")
_CfprApFirmwareDependencyMaxVer_Type = SnmpAdminString
_CfprApFirmwareDependencyMaxVer_Object = MibTableColumn
cfprApFirmwareDependencyMaxVer = _CfprApFirmwareDependencyMaxVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 9),
    _CfprApFirmwareDependencyMaxVer_Type()
)
cfprApFirmwareDependencyMaxVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyMaxVer.setStatus("current")
_CfprApFirmwareDependencyMinVer_Type = SnmpAdminString
_CfprApFirmwareDependencyMinVer_Object = MibTableColumn
cfprApFirmwareDependencyMinVer = _CfprApFirmwareDependencyMinVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 10),
    _CfprApFirmwareDependencyMinVer_Type()
)
cfprApFirmwareDependencyMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyMinVer.setStatus("current")
_CfprApFirmwareDependencyRelationship_Type = CfprApFirmwareDependencyRelationship
_CfprApFirmwareDependencyRelationship_Object = MibTableColumn
cfprApFirmwareDependencyRelationship = _CfprApFirmwareDependencyRelationship_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 11),
    _CfprApFirmwareDependencyRelationship_Type()
)
cfprApFirmwareDependencyRelationship.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyRelationship.setStatus("current")
_CfprApFirmwareDependencyScope_Type = CfprApFirmwareDependencyScope
_CfprApFirmwareDependencyScope_Object = MibTableColumn
cfprApFirmwareDependencyScope = _CfprApFirmwareDependencyScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 12),
    _CfprApFirmwareDependencyScope_Type()
)
cfprApFirmwareDependencyScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencyScope.setStatus("current")
_CfprApFirmwareDependencySensitivity_Type = CfprApFirmwareDependencySensitivity
_CfprApFirmwareDependencySensitivity_Object = MibTableColumn
cfprApFirmwareDependencySensitivity = _CfprApFirmwareDependencySensitivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 20, 1, 13),
    _CfprApFirmwareDependencySensitivity_Type()
)
cfprApFirmwareDependencySensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDependencySensitivity.setStatus("current")
_CfprApFirmwareDistCspBlackListTable_Object = MibTable
cfprApFirmwareDistCspBlackListTable = _CfprApFirmwareDistCspBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 21)
)
if mibBuilder.loadTexts:
    cfprApFirmwareDistCspBlackListTable.setStatus("current")
_CfprApFirmwareDistCspBlackListEntry_Object = MibTableRow
cfprApFirmwareDistCspBlackListEntry = _CfprApFirmwareDistCspBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 21, 1)
)
cfprApFirmwareDistCspBlackListEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareDistCspBlackListInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareDistCspBlackListEntry.setStatus("current")
_CfprApFirmwareDistCspBlackListInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareDistCspBlackListInstanceId_Object = MibTableColumn
cfprApFirmwareDistCspBlackListInstanceId = _CfprApFirmwareDistCspBlackListInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 21, 1, 1),
    _CfprApFirmwareDistCspBlackListInstanceId_Type()
)
cfprApFirmwareDistCspBlackListInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareDistCspBlackListInstanceId.setStatus("current")
_CfprApFirmwareDistCspBlackListDn_Type = CfprApManagedObjectDn
_CfprApFirmwareDistCspBlackListDn_Object = MibTableColumn
cfprApFirmwareDistCspBlackListDn = _CfprApFirmwareDistCspBlackListDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 21, 1, 2),
    _CfprApFirmwareDistCspBlackListDn_Type()
)
cfprApFirmwareDistCspBlackListDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistCspBlackListDn.setStatus("current")
_CfprApFirmwareDistCspBlackListRn_Type = SnmpAdminString
_CfprApFirmwareDistCspBlackListRn_Object = MibTableColumn
cfprApFirmwareDistCspBlackListRn = _CfprApFirmwareDistCspBlackListRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 21, 1, 3),
    _CfprApFirmwareDistCspBlackListRn_Type()
)
cfprApFirmwareDistCspBlackListRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistCspBlackListRn.setStatus("current")
_CfprApFirmwareDistCspBlackListName_Type = SnmpAdminString
_CfprApFirmwareDistCspBlackListName_Object = MibTableColumn
cfprApFirmwareDistCspBlackListName = _CfprApFirmwareDistCspBlackListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 21, 1, 4),
    _CfprApFirmwareDistCspBlackListName_Type()
)
cfprApFirmwareDistCspBlackListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistCspBlackListName.setStatus("current")
_CfprApFirmwareDistCspBlackListTimeStamp_Type = DateAndTime
_CfprApFirmwareDistCspBlackListTimeStamp_Object = MibTableColumn
cfprApFirmwareDistCspBlackListTimeStamp = _CfprApFirmwareDistCspBlackListTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 21, 1, 5),
    _CfprApFirmwareDistCspBlackListTimeStamp_Type()
)
cfprApFirmwareDistCspBlackListTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistCspBlackListTimeStamp.setStatus("current")
_CfprApFirmwareDistCspBlackListVersion_Type = SnmpAdminString
_CfprApFirmwareDistCspBlackListVersion_Object = MibTableColumn
cfprApFirmwareDistCspBlackListVersion = _CfprApFirmwareDistCspBlackListVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 21, 1, 6),
    _CfprApFirmwareDistCspBlackListVersion_Type()
)
cfprApFirmwareDistCspBlackListVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistCspBlackListVersion.setStatus("current")
_CfprApFirmwareDistImageTable_Object = MibTable
cfprApFirmwareDistImageTable = _CfprApFirmwareDistImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 22)
)
if mibBuilder.loadTexts:
    cfprApFirmwareDistImageTable.setStatus("current")
_CfprApFirmwareDistImageEntry_Object = MibTableRow
cfprApFirmwareDistImageEntry = _CfprApFirmwareDistImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 22, 1)
)
cfprApFirmwareDistImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareDistImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareDistImageEntry.setStatus("current")
_CfprApFirmwareDistImageInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareDistImageInstanceId_Object = MibTableColumn
cfprApFirmwareDistImageInstanceId = _CfprApFirmwareDistImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 22, 1, 1),
    _CfprApFirmwareDistImageInstanceId_Type()
)
cfprApFirmwareDistImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareDistImageInstanceId.setStatus("current")
_CfprApFirmwareDistImageDn_Type = CfprApManagedObjectDn
_CfprApFirmwareDistImageDn_Object = MibTableColumn
cfprApFirmwareDistImageDn = _CfprApFirmwareDistImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 22, 1, 2),
    _CfprApFirmwareDistImageDn_Type()
)
cfprApFirmwareDistImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistImageDn.setStatus("current")
_CfprApFirmwareDistImageRn_Type = SnmpAdminString
_CfprApFirmwareDistImageRn_Object = MibTableColumn
cfprApFirmwareDistImageRn = _CfprApFirmwareDistImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 22, 1, 3),
    _CfprApFirmwareDistImageRn_Type()
)
cfprApFirmwareDistImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistImageRn.setStatus("current")
_CfprApFirmwareDistImageImageDeleted_Type = CfprApFirmwareImageDeleted
_CfprApFirmwareDistImageImageDeleted_Object = MibTableColumn
cfprApFirmwareDistImageImageDeleted = _CfprApFirmwareDistImageImageDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 22, 1, 4),
    _CfprApFirmwareDistImageImageDeleted_Type()
)
cfprApFirmwareDistImageImageDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistImageImageDeleted.setStatus("current")
_CfprApFirmwareDistImageName_Type = SnmpAdminString
_CfprApFirmwareDistImageName_Object = MibTableColumn
cfprApFirmwareDistImageName = _CfprApFirmwareDistImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 22, 1, 5),
    _CfprApFirmwareDistImageName_Type()
)
cfprApFirmwareDistImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistImageName.setStatus("current")
_CfprApFirmwareDistImageType_Type = CfprApFirmwareType
_CfprApFirmwareDistImageType_Object = MibTableColumn
cfprApFirmwareDistImageType = _CfprApFirmwareDistImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 22, 1, 6),
    _CfprApFirmwareDistImageType_Type()
)
cfprApFirmwareDistImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistImageType.setStatus("current")
_CfprApFirmwareDistributableTable_Object = MibTable
cfprApFirmwareDistributableTable = _CfprApFirmwareDistributableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23)
)
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableTable.setStatus("current")
_CfprApFirmwareDistributableEntry_Object = MibTableRow
cfprApFirmwareDistributableEntry = _CfprApFirmwareDistributableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1)
)
cfprApFirmwareDistributableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareDistributableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableEntry.setStatus("current")
_CfprApFirmwareDistributableInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareDistributableInstanceId_Object = MibTableColumn
cfprApFirmwareDistributableInstanceId = _CfprApFirmwareDistributableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 1),
    _CfprApFirmwareDistributableInstanceId_Type()
)
cfprApFirmwareDistributableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableInstanceId.setStatus("current")
_CfprApFirmwareDistributableDn_Type = CfprApManagedObjectDn
_CfprApFirmwareDistributableDn_Object = MibTableColumn
cfprApFirmwareDistributableDn = _CfprApFirmwareDistributableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 2),
    _CfprApFirmwareDistributableDn_Type()
)
cfprApFirmwareDistributableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableDn.setStatus("current")
_CfprApFirmwareDistributableRn_Type = SnmpAdminString
_CfprApFirmwareDistributableRn_Object = MibTableColumn
cfprApFirmwareDistributableRn = _CfprApFirmwareDistributableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 3),
    _CfprApFirmwareDistributableRn_Type()
)
cfprApFirmwareDistributableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableRn.setStatus("current")
_CfprApFirmwareDistributableAdminState_Type = CfprApFirmwareAdminState
_CfprApFirmwareDistributableAdminState_Object = MibTableColumn
cfprApFirmwareDistributableAdminState = _CfprApFirmwareDistributableAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 4),
    _CfprApFirmwareDistributableAdminState_Type()
)
cfprApFirmwareDistributableAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableAdminState.setStatus("current")
_CfprApFirmwareDistributableBuildDate_Type = SnmpAdminString
_CfprApFirmwareDistributableBuildDate_Object = MibTableColumn
cfprApFirmwareDistributableBuildDate = _CfprApFirmwareDistributableBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 5),
    _CfprApFirmwareDistributableBuildDate_Type()
)
cfprApFirmwareDistributableBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableBuildDate.setStatus("current")
_CfprApFirmwareDistributableCompleteness_Type = CfprApFirmwareCompleteness
_CfprApFirmwareDistributableCompleteness_Object = MibTableColumn
cfprApFirmwareDistributableCompleteness = _CfprApFirmwareDistributableCompleteness_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 6),
    _CfprApFirmwareDistributableCompleteness_Type()
)
cfprApFirmwareDistributableCompleteness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableCompleteness.setStatus("current")
_CfprApFirmwareDistributableDescr_Type = SnmpAdminString
_CfprApFirmwareDistributableDescr_Object = MibTableColumn
cfprApFirmwareDistributableDescr = _CfprApFirmwareDistributableDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 7),
    _CfprApFirmwareDistributableDescr_Type()
)
cfprApFirmwareDistributableDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableDescr.setStatus("current")
_CfprApFirmwareDistributableDisplayFlag_Type = TruthValue
_CfprApFirmwareDistributableDisplayFlag_Object = MibTableColumn
cfprApFirmwareDistributableDisplayFlag = _CfprApFirmwareDistributableDisplayFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 8),
    _CfprApFirmwareDistributableDisplayFlag_Type()
)
cfprApFirmwareDistributableDisplayFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableDisplayFlag.setStatus("current")
_CfprApFirmwareDistributableFsmDescr_Type = SnmpAdminString
_CfprApFirmwareDistributableFsmDescr_Object = MibTableColumn
cfprApFirmwareDistributableFsmDescr = _CfprApFirmwareDistributableFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 9),
    _CfprApFirmwareDistributableFsmDescr_Type()
)
cfprApFirmwareDistributableFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmDescr.setStatus("current")
_CfprApFirmwareDistributableFsmPrev_Type = SnmpAdminString
_CfprApFirmwareDistributableFsmPrev_Object = MibTableColumn
cfprApFirmwareDistributableFsmPrev = _CfprApFirmwareDistributableFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 10),
    _CfprApFirmwareDistributableFsmPrev_Type()
)
cfprApFirmwareDistributableFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmPrev.setStatus("current")
_CfprApFirmwareDistributableFsmProgr_Type = Gauge32
_CfprApFirmwareDistributableFsmProgr_Object = MibTableColumn
cfprApFirmwareDistributableFsmProgr = _CfprApFirmwareDistributableFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 11),
    _CfprApFirmwareDistributableFsmProgr_Type()
)
cfprApFirmwareDistributableFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmProgr.setStatus("current")
_CfprApFirmwareDistributableFsmRmtInvErrCode_Type = Gauge32
_CfprApFirmwareDistributableFsmRmtInvErrCode_Object = MibTableColumn
cfprApFirmwareDistributableFsmRmtInvErrCode = _CfprApFirmwareDistributableFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 12),
    _CfprApFirmwareDistributableFsmRmtInvErrCode_Type()
)
cfprApFirmwareDistributableFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmRmtInvErrCode.setStatus("current")
_CfprApFirmwareDistributableFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApFirmwareDistributableFsmRmtInvErrDescr_Object = MibTableColumn
cfprApFirmwareDistributableFsmRmtInvErrDescr = _CfprApFirmwareDistributableFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 13),
    _CfprApFirmwareDistributableFsmRmtInvErrDescr_Type()
)
cfprApFirmwareDistributableFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmRmtInvErrDescr.setStatus("current")
_CfprApFirmwareDistributableFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwareDistributableFsmRmtInvRslt_Object = MibTableColumn
cfprApFirmwareDistributableFsmRmtInvRslt = _CfprApFirmwareDistributableFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 14),
    _CfprApFirmwareDistributableFsmRmtInvRslt_Type()
)
cfprApFirmwareDistributableFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmRmtInvRslt.setStatus("current")
_CfprApFirmwareDistributableFsmStageDescr_Type = SnmpAdminString
_CfprApFirmwareDistributableFsmStageDescr_Object = MibTableColumn
cfprApFirmwareDistributableFsmStageDescr = _CfprApFirmwareDistributableFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 15),
    _CfprApFirmwareDistributableFsmStageDescr_Type()
)
cfprApFirmwareDistributableFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStageDescr.setStatus("current")
_CfprApFirmwareDistributableFsmStamp_Type = DateAndTime
_CfprApFirmwareDistributableFsmStamp_Object = MibTableColumn
cfprApFirmwareDistributableFsmStamp = _CfprApFirmwareDistributableFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 16),
    _CfprApFirmwareDistributableFsmStamp_Type()
)
cfprApFirmwareDistributableFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStamp.setStatus("current")
_CfprApFirmwareDistributableFsmStatus_Type = SnmpAdminString
_CfprApFirmwareDistributableFsmStatus_Object = MibTableColumn
cfprApFirmwareDistributableFsmStatus = _CfprApFirmwareDistributableFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 17),
    _CfprApFirmwareDistributableFsmStatus_Type()
)
cfprApFirmwareDistributableFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStatus.setStatus("current")
_CfprApFirmwareDistributableFsmTry_Type = Gauge32
_CfprApFirmwareDistributableFsmTry_Object = MibTableColumn
cfprApFirmwareDistributableFsmTry = _CfprApFirmwareDistributableFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 18),
    _CfprApFirmwareDistributableFsmTry_Type()
)
cfprApFirmwareDistributableFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmTry.setStatus("current")
_CfprApFirmwareDistributableImagePresence_Type = CfprApFirmwareImagePresence
_CfprApFirmwareDistributableImagePresence_Object = MibTableColumn
cfprApFirmwareDistributableImagePresence = _CfprApFirmwareDistributableImagePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 19),
    _CfprApFirmwareDistributableImagePresence_Type()
)
cfprApFirmwareDistributableImagePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableImagePresence.setStatus("current")
_CfprApFirmwareDistributableIntId_Type = SnmpAdminString
_CfprApFirmwareDistributableIntId_Object = MibTableColumn
cfprApFirmwareDistributableIntId = _CfprApFirmwareDistributableIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 20),
    _CfprApFirmwareDistributableIntId_Type()
)
cfprApFirmwareDistributableIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableIntId.setStatus("current")
_CfprApFirmwareDistributableInvTag_Type = SnmpAdminString
_CfprApFirmwareDistributableInvTag_Object = MibTableColumn
cfprApFirmwareDistributableInvTag = _CfprApFirmwareDistributableInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 21),
    _CfprApFirmwareDistributableInvTag_Type()
)
cfprApFirmwareDistributableInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableInvTag.setStatus("current")
_CfprApFirmwareDistributableModel_Type = SnmpAdminString
_CfprApFirmwareDistributableModel_Object = MibTableColumn
cfprApFirmwareDistributableModel = _CfprApFirmwareDistributableModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 22),
    _CfprApFirmwareDistributableModel_Type()
)
cfprApFirmwareDistributableModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableModel.setStatus("current")
_CfprApFirmwareDistributableName_Type = SnmpAdminString
_CfprApFirmwareDistributableName_Object = MibTableColumn
cfprApFirmwareDistributableName = _CfprApFirmwareDistributableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 23),
    _CfprApFirmwareDistributableName_Type()
)
cfprApFirmwareDistributableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableName.setStatus("current")
_CfprApFirmwareDistributablePlatformVersion_Type = SnmpAdminString
_CfprApFirmwareDistributablePlatformVersion_Object = MibTableColumn
cfprApFirmwareDistributablePlatformVersion = _CfprApFirmwareDistributablePlatformVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 24),
    _CfprApFirmwareDistributablePlatformVersion_Type()
)
cfprApFirmwareDistributablePlatformVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributablePlatformVersion.setStatus("current")
_CfprApFirmwareDistributablePolicyLevel_Type = Gauge32
_CfprApFirmwareDistributablePolicyLevel_Object = MibTableColumn
cfprApFirmwareDistributablePolicyLevel = _CfprApFirmwareDistributablePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 25),
    _CfprApFirmwareDistributablePolicyLevel_Type()
)
cfprApFirmwareDistributablePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributablePolicyLevel.setStatus("current")
_CfprApFirmwareDistributablePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwareDistributablePolicyOwner_Object = MibTableColumn
cfprApFirmwareDistributablePolicyOwner = _CfprApFirmwareDistributablePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 26),
    _CfprApFirmwareDistributablePolicyOwner_Type()
)
cfprApFirmwareDistributablePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributablePolicyOwner.setStatus("current")
_CfprApFirmwareDistributableTimeStamp_Type = DateAndTime
_CfprApFirmwareDistributableTimeStamp_Object = MibTableColumn
cfprApFirmwareDistributableTimeStamp = _CfprApFirmwareDistributableTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 27),
    _CfprApFirmwareDistributableTimeStamp_Type()
)
cfprApFirmwareDistributableTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableTimeStamp.setStatus("current")
_CfprApFirmwareDistributableTransferState_Type = CfprApFirmwareTransferState
_CfprApFirmwareDistributableTransferState_Object = MibTableColumn
cfprApFirmwareDistributableTransferState = _CfprApFirmwareDistributableTransferState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 28),
    _CfprApFirmwareDistributableTransferState_Type()
)
cfprApFirmwareDistributableTransferState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableTransferState.setStatus("current")
_CfprApFirmwareDistributableType_Type = CfprApFirmwareDistributableType
_CfprApFirmwareDistributableType_Object = MibTableColumn
cfprApFirmwareDistributableType = _CfprApFirmwareDistributableType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 29),
    _CfprApFirmwareDistributableType_Type()
)
cfprApFirmwareDistributableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableType.setStatus("current")
_CfprApFirmwareDistributableVendor_Type = SnmpAdminString
_CfprApFirmwareDistributableVendor_Object = MibTableColumn
cfprApFirmwareDistributableVendor = _CfprApFirmwareDistributableVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 30),
    _CfprApFirmwareDistributableVendor_Type()
)
cfprApFirmwareDistributableVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableVendor.setStatus("current")
_CfprApFirmwareDistributableVersion_Type = SnmpAdminString
_CfprApFirmwareDistributableVersion_Object = MibTableColumn
cfprApFirmwareDistributableVersion = _CfprApFirmwareDistributableVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 23, 1, 31),
    _CfprApFirmwareDistributableVersion_Type()
)
cfprApFirmwareDistributableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableVersion.setStatus("current")
_CfprApFirmwareDistributableFsmTable_Object = MibTable
cfprApFirmwareDistributableFsmTable = _CfprApFirmwareDistributableFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24)
)
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmTable.setStatus("current")
_CfprApFirmwareDistributableFsmEntry_Object = MibTableRow
cfprApFirmwareDistributableFsmEntry = _CfprApFirmwareDistributableFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24, 1)
)
cfprApFirmwareDistributableFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareDistributableFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmEntry.setStatus("current")
_CfprApFirmwareDistributableFsmInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareDistributableFsmInstanceId_Object = MibTableColumn
cfprApFirmwareDistributableFsmInstanceId = _CfprApFirmwareDistributableFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24, 1, 1),
    _CfprApFirmwareDistributableFsmInstanceId_Type()
)
cfprApFirmwareDistributableFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmInstanceId.setStatus("current")
_CfprApFirmwareDistributableFsmDn_Type = CfprApManagedObjectDn
_CfprApFirmwareDistributableFsmDn_Object = MibTableColumn
cfprApFirmwareDistributableFsmDn = _CfprApFirmwareDistributableFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24, 1, 2),
    _CfprApFirmwareDistributableFsmDn_Type()
)
cfprApFirmwareDistributableFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmDn.setStatus("current")
_CfprApFirmwareDistributableFsmRn_Type = SnmpAdminString
_CfprApFirmwareDistributableFsmRn_Object = MibTableColumn
cfprApFirmwareDistributableFsmRn = _CfprApFirmwareDistributableFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24, 1, 3),
    _CfprApFirmwareDistributableFsmRn_Type()
)
cfprApFirmwareDistributableFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmRn.setStatus("current")
_CfprApFirmwareDistributableFsmCompletionTime_Type = DateAndTime
_CfprApFirmwareDistributableFsmCompletionTime_Object = MibTableColumn
cfprApFirmwareDistributableFsmCompletionTime = _CfprApFirmwareDistributableFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24, 1, 4),
    _CfprApFirmwareDistributableFsmCompletionTime_Type()
)
cfprApFirmwareDistributableFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmCompletionTime.setStatus("current")
_CfprApFirmwareDistributableFsmCurrentFsm_Type = CfprApFirmwareDistributableFsmCurrentFsm
_CfprApFirmwareDistributableFsmCurrentFsm_Object = MibTableColumn
cfprApFirmwareDistributableFsmCurrentFsm = _CfprApFirmwareDistributableFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24, 1, 5),
    _CfprApFirmwareDistributableFsmCurrentFsm_Type()
)
cfprApFirmwareDistributableFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmCurrentFsm.setStatus("current")
_CfprApFirmwareDistributableFsmDescrData_Type = SnmpAdminString
_CfprApFirmwareDistributableFsmDescrData_Object = MibTableColumn
cfprApFirmwareDistributableFsmDescrData = _CfprApFirmwareDistributableFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24, 1, 6),
    _CfprApFirmwareDistributableFsmDescrData_Type()
)
cfprApFirmwareDistributableFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmDescrData.setStatus("current")
_CfprApFirmwareDistributableFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwareDistributableFsmFsmStatus_Object = MibTableColumn
cfprApFirmwareDistributableFsmFsmStatus = _CfprApFirmwareDistributableFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24, 1, 7),
    _CfprApFirmwareDistributableFsmFsmStatus_Type()
)
cfprApFirmwareDistributableFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmFsmStatus.setStatus("current")
_CfprApFirmwareDistributableFsmProgress_Type = Gauge32
_CfprApFirmwareDistributableFsmProgress_Object = MibTableColumn
cfprApFirmwareDistributableFsmProgress = _CfprApFirmwareDistributableFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24, 1, 8),
    _CfprApFirmwareDistributableFsmProgress_Type()
)
cfprApFirmwareDistributableFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmProgress.setStatus("current")
_CfprApFirmwareDistributableFsmRmtErrCode_Type = Gauge32
_CfprApFirmwareDistributableFsmRmtErrCode_Object = MibTableColumn
cfprApFirmwareDistributableFsmRmtErrCode = _CfprApFirmwareDistributableFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24, 1, 9),
    _CfprApFirmwareDistributableFsmRmtErrCode_Type()
)
cfprApFirmwareDistributableFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmRmtErrCode.setStatus("current")
_CfprApFirmwareDistributableFsmRmtErrDescr_Type = SnmpAdminString
_CfprApFirmwareDistributableFsmRmtErrDescr_Object = MibTableColumn
cfprApFirmwareDistributableFsmRmtErrDescr = _CfprApFirmwareDistributableFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24, 1, 10),
    _CfprApFirmwareDistributableFsmRmtErrDescr_Type()
)
cfprApFirmwareDistributableFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmRmtErrDescr.setStatus("current")
_CfprApFirmwareDistributableFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwareDistributableFsmRmtRslt_Object = MibTableColumn
cfprApFirmwareDistributableFsmRmtRslt = _CfprApFirmwareDistributableFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 24, 1, 11),
    _CfprApFirmwareDistributableFsmRmtRslt_Type()
)
cfprApFirmwareDistributableFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmRmtRslt.setStatus("current")
_CfprApFirmwareDistributableFsmStageTable_Object = MibTable
cfprApFirmwareDistributableFsmStageTable = _CfprApFirmwareDistributableFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 25)
)
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStageTable.setStatus("current")
_CfprApFirmwareDistributableFsmStageEntry_Object = MibTableRow
cfprApFirmwareDistributableFsmStageEntry = _CfprApFirmwareDistributableFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 25, 1)
)
cfprApFirmwareDistributableFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareDistributableFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStageEntry.setStatus("current")
_CfprApFirmwareDistributableFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareDistributableFsmStageInstanceId_Object = MibTableColumn
cfprApFirmwareDistributableFsmStageInstanceId = _CfprApFirmwareDistributableFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 25, 1, 1),
    _CfprApFirmwareDistributableFsmStageInstanceId_Type()
)
cfprApFirmwareDistributableFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStageInstanceId.setStatus("current")
_CfprApFirmwareDistributableFsmStageDn_Type = CfprApManagedObjectDn
_CfprApFirmwareDistributableFsmStageDn_Object = MibTableColumn
cfprApFirmwareDistributableFsmStageDn = _CfprApFirmwareDistributableFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 25, 1, 2),
    _CfprApFirmwareDistributableFsmStageDn_Type()
)
cfprApFirmwareDistributableFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStageDn.setStatus("current")
_CfprApFirmwareDistributableFsmStageRn_Type = SnmpAdminString
_CfprApFirmwareDistributableFsmStageRn_Object = MibTableColumn
cfprApFirmwareDistributableFsmStageRn = _CfprApFirmwareDistributableFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 25, 1, 3),
    _CfprApFirmwareDistributableFsmStageRn_Type()
)
cfprApFirmwareDistributableFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStageRn.setStatus("current")
_CfprApFirmwareDistributableFsmStageDescrData_Type = SnmpAdminString
_CfprApFirmwareDistributableFsmStageDescrData_Object = MibTableColumn
cfprApFirmwareDistributableFsmStageDescrData = _CfprApFirmwareDistributableFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 25, 1, 4),
    _CfprApFirmwareDistributableFsmStageDescrData_Type()
)
cfprApFirmwareDistributableFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStageDescrData.setStatus("current")
_CfprApFirmwareDistributableFsmStageLastUpdateTime_Type = DateAndTime
_CfprApFirmwareDistributableFsmStageLastUpdateTime_Object = MibTableColumn
cfprApFirmwareDistributableFsmStageLastUpdateTime = _CfprApFirmwareDistributableFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 25, 1, 5),
    _CfprApFirmwareDistributableFsmStageLastUpdateTime_Type()
)
cfprApFirmwareDistributableFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStageLastUpdateTime.setStatus("current")
_CfprApFirmwareDistributableFsmStageName_Type = CfprApFirmwareDistributableFsmStageName
_CfprApFirmwareDistributableFsmStageName_Object = MibTableColumn
cfprApFirmwareDistributableFsmStageName = _CfprApFirmwareDistributableFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 25, 1, 6),
    _CfprApFirmwareDistributableFsmStageName_Type()
)
cfprApFirmwareDistributableFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStageName.setStatus("current")
_CfprApFirmwareDistributableFsmStageOrder_Type = Gauge32
_CfprApFirmwareDistributableFsmStageOrder_Object = MibTableColumn
cfprApFirmwareDistributableFsmStageOrder = _CfprApFirmwareDistributableFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 25, 1, 7),
    _CfprApFirmwareDistributableFsmStageOrder_Type()
)
cfprApFirmwareDistributableFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStageOrder.setStatus("current")
_CfprApFirmwareDistributableFsmStageRetry_Type = Gauge32
_CfprApFirmwareDistributableFsmStageRetry_Object = MibTableColumn
cfprApFirmwareDistributableFsmStageRetry = _CfprApFirmwareDistributableFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 25, 1, 8),
    _CfprApFirmwareDistributableFsmStageRetry_Type()
)
cfprApFirmwareDistributableFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStageRetry.setStatus("current")
_CfprApFirmwareDistributableFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwareDistributableFsmStageStageStatus_Object = MibTableColumn
cfprApFirmwareDistributableFsmStageStageStatus = _CfprApFirmwareDistributableFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 25, 1, 9),
    _CfprApFirmwareDistributableFsmStageStageStatus_Type()
)
cfprApFirmwareDistributableFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmStageStageStatus.setStatus("current")
_CfprApFirmwareDistributableFsmTaskTable_Object = MibTable
cfprApFirmwareDistributableFsmTaskTable = _CfprApFirmwareDistributableFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 26)
)
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmTaskTable.setStatus("current")
_CfprApFirmwareDistributableFsmTaskEntry_Object = MibTableRow
cfprApFirmwareDistributableFsmTaskEntry = _CfprApFirmwareDistributableFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 26, 1)
)
cfprApFirmwareDistributableFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareDistributableFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmTaskEntry.setStatus("current")
_CfprApFirmwareDistributableFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareDistributableFsmTaskInstanceId_Object = MibTableColumn
cfprApFirmwareDistributableFsmTaskInstanceId = _CfprApFirmwareDistributableFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 26, 1, 1),
    _CfprApFirmwareDistributableFsmTaskInstanceId_Type()
)
cfprApFirmwareDistributableFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmTaskInstanceId.setStatus("current")
_CfprApFirmwareDistributableFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApFirmwareDistributableFsmTaskDn_Object = MibTableColumn
cfprApFirmwareDistributableFsmTaskDn = _CfprApFirmwareDistributableFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 26, 1, 2),
    _CfprApFirmwareDistributableFsmTaskDn_Type()
)
cfprApFirmwareDistributableFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmTaskDn.setStatus("current")
_CfprApFirmwareDistributableFsmTaskRn_Type = SnmpAdminString
_CfprApFirmwareDistributableFsmTaskRn_Object = MibTableColumn
cfprApFirmwareDistributableFsmTaskRn = _CfprApFirmwareDistributableFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 26, 1, 3),
    _CfprApFirmwareDistributableFsmTaskRn_Type()
)
cfprApFirmwareDistributableFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmTaskRn.setStatus("current")
_CfprApFirmwareDistributableFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApFirmwareDistributableFsmTaskCompletion_Object = MibTableColumn
cfprApFirmwareDistributableFsmTaskCompletion = _CfprApFirmwareDistributableFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 26, 1, 4),
    _CfprApFirmwareDistributableFsmTaskCompletion_Type()
)
cfprApFirmwareDistributableFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmTaskCompletion.setStatus("current")
_CfprApFirmwareDistributableFsmTaskFlags_Type = CfprApFsmFlags
_CfprApFirmwareDistributableFsmTaskFlags_Object = MibTableColumn
cfprApFirmwareDistributableFsmTaskFlags = _CfprApFirmwareDistributableFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 26, 1, 5),
    _CfprApFirmwareDistributableFsmTaskFlags_Type()
)
cfprApFirmwareDistributableFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmTaskFlags.setStatus("current")
_CfprApFirmwareDistributableFsmTaskItem_Type = CfprApFirmwareDistributableFsmTaskItem
_CfprApFirmwareDistributableFsmTaskItem_Object = MibTableColumn
cfprApFirmwareDistributableFsmTaskItem = _CfprApFirmwareDistributableFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 26, 1, 6),
    _CfprApFirmwareDistributableFsmTaskItem_Type()
)
cfprApFirmwareDistributableFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmTaskItem.setStatus("current")
_CfprApFirmwareDistributableFsmTaskSeqId_Type = Gauge32
_CfprApFirmwareDistributableFsmTaskSeqId_Object = MibTableColumn
cfprApFirmwareDistributableFsmTaskSeqId = _CfprApFirmwareDistributableFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 26, 1, 7),
    _CfprApFirmwareDistributableFsmTaskSeqId_Type()
)
cfprApFirmwareDistributableFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDistributableFsmTaskSeqId.setStatus("current")
_CfprApFirmwareDownloaderTable_Object = MibTable
cfprApFirmwareDownloaderTable = _CfprApFirmwareDownloaderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27)
)
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderTable.setStatus("current")
_CfprApFirmwareDownloaderEntry_Object = MibTableRow
cfprApFirmwareDownloaderEntry = _CfprApFirmwareDownloaderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1)
)
cfprApFirmwareDownloaderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareDownloaderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderEntry.setStatus("current")
_CfprApFirmwareDownloaderInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareDownloaderInstanceId_Object = MibTableColumn
cfprApFirmwareDownloaderInstanceId = _CfprApFirmwareDownloaderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 1),
    _CfprApFirmwareDownloaderInstanceId_Type()
)
cfprApFirmwareDownloaderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderInstanceId.setStatus("current")
_CfprApFirmwareDownloaderDn_Type = CfprApManagedObjectDn
_CfprApFirmwareDownloaderDn_Object = MibTableColumn
cfprApFirmwareDownloaderDn = _CfprApFirmwareDownloaderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 2),
    _CfprApFirmwareDownloaderDn_Type()
)
cfprApFirmwareDownloaderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderDn.setStatus("current")
_CfprApFirmwareDownloaderRn_Type = SnmpAdminString
_CfprApFirmwareDownloaderRn_Object = MibTableColumn
cfprApFirmwareDownloaderRn = _CfprApFirmwareDownloaderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 3),
    _CfprApFirmwareDownloaderRn_Type()
)
cfprApFirmwareDownloaderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderRn.setStatus("current")
_CfprApFirmwareDownloaderAdminState_Type = CfprApFirmwareDownloadActivity
_CfprApFirmwareDownloaderAdminState_Object = MibTableColumn
cfprApFirmwareDownloaderAdminState = _CfprApFirmwareDownloaderAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 4),
    _CfprApFirmwareDownloaderAdminState_Type()
)
cfprApFirmwareDownloaderAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderAdminState.setStatus("current")
_CfprApFirmwareDownloaderFileName_Type = SnmpAdminString
_CfprApFirmwareDownloaderFileName_Object = MibTableColumn
cfprApFirmwareDownloaderFileName = _CfprApFirmwareDownloaderFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 5),
    _CfprApFirmwareDownloaderFileName_Type()
)
cfprApFirmwareDownloaderFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFileName.setStatus("current")
_CfprApFirmwareDownloaderFsmDescr_Type = SnmpAdminString
_CfprApFirmwareDownloaderFsmDescr_Object = MibTableColumn
cfprApFirmwareDownloaderFsmDescr = _CfprApFirmwareDownloaderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 6),
    _CfprApFirmwareDownloaderFsmDescr_Type()
)
cfprApFirmwareDownloaderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmDescr.setStatus("current")
_CfprApFirmwareDownloaderFsmPrev_Type = SnmpAdminString
_CfprApFirmwareDownloaderFsmPrev_Object = MibTableColumn
cfprApFirmwareDownloaderFsmPrev = _CfprApFirmwareDownloaderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 7),
    _CfprApFirmwareDownloaderFsmPrev_Type()
)
cfprApFirmwareDownloaderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmPrev.setStatus("current")
_CfprApFirmwareDownloaderFsmProgr_Type = Gauge32
_CfprApFirmwareDownloaderFsmProgr_Object = MibTableColumn
cfprApFirmwareDownloaderFsmProgr = _CfprApFirmwareDownloaderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 8),
    _CfprApFirmwareDownloaderFsmProgr_Type()
)
cfprApFirmwareDownloaderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmProgr.setStatus("current")
_CfprApFirmwareDownloaderFsmRmtInvErrCode_Type = Gauge32
_CfprApFirmwareDownloaderFsmRmtInvErrCode_Object = MibTableColumn
cfprApFirmwareDownloaderFsmRmtInvErrCode = _CfprApFirmwareDownloaderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 9),
    _CfprApFirmwareDownloaderFsmRmtInvErrCode_Type()
)
cfprApFirmwareDownloaderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmRmtInvErrCode.setStatus("current")
_CfprApFirmwareDownloaderFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApFirmwareDownloaderFsmRmtInvErrDescr_Object = MibTableColumn
cfprApFirmwareDownloaderFsmRmtInvErrDescr = _CfprApFirmwareDownloaderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 10),
    _CfprApFirmwareDownloaderFsmRmtInvErrDescr_Type()
)
cfprApFirmwareDownloaderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmRmtInvErrDescr.setStatus("current")
_CfprApFirmwareDownloaderFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwareDownloaderFsmRmtInvRslt_Object = MibTableColumn
cfprApFirmwareDownloaderFsmRmtInvRslt = _CfprApFirmwareDownloaderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 11),
    _CfprApFirmwareDownloaderFsmRmtInvRslt_Type()
)
cfprApFirmwareDownloaderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmRmtInvRslt.setStatus("current")
_CfprApFirmwareDownloaderFsmStageDescr_Type = SnmpAdminString
_CfprApFirmwareDownloaderFsmStageDescr_Object = MibTableColumn
cfprApFirmwareDownloaderFsmStageDescr = _CfprApFirmwareDownloaderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 12),
    _CfprApFirmwareDownloaderFsmStageDescr_Type()
)
cfprApFirmwareDownloaderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStageDescr.setStatus("current")
_CfprApFirmwareDownloaderFsmStamp_Type = DateAndTime
_CfprApFirmwareDownloaderFsmStamp_Object = MibTableColumn
cfprApFirmwareDownloaderFsmStamp = _CfprApFirmwareDownloaderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 13),
    _CfprApFirmwareDownloaderFsmStamp_Type()
)
cfprApFirmwareDownloaderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStamp.setStatus("current")
_CfprApFirmwareDownloaderFsmStatus_Type = SnmpAdminString
_CfprApFirmwareDownloaderFsmStatus_Object = MibTableColumn
cfprApFirmwareDownloaderFsmStatus = _CfprApFirmwareDownloaderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 14),
    _CfprApFirmwareDownloaderFsmStatus_Type()
)
cfprApFirmwareDownloaderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStatus.setStatus("current")
_CfprApFirmwareDownloaderFsmTry_Type = Gauge32
_CfprApFirmwareDownloaderFsmTry_Object = MibTableColumn
cfprApFirmwareDownloaderFsmTry = _CfprApFirmwareDownloaderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 15),
    _CfprApFirmwareDownloaderFsmTry_Type()
)
cfprApFirmwareDownloaderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmTry.setStatus("current")
_CfprApFirmwareDownloaderImageSize_Type = Gauge32
_CfprApFirmwareDownloaderImageSize_Object = MibTableColumn
cfprApFirmwareDownloaderImageSize = _CfprApFirmwareDownloaderImageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 16),
    _CfprApFirmwareDownloaderImageSize_Type()
)
cfprApFirmwareDownloaderImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderImageSize.setStatus("current")
_CfprApFirmwareDownloaderPort_Type = Gauge32
_CfprApFirmwareDownloaderPort_Object = MibTableColumn
cfprApFirmwareDownloaderPort = _CfprApFirmwareDownloaderPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 17),
    _CfprApFirmwareDownloaderPort_Type()
)
cfprApFirmwareDownloaderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderPort.setStatus("current")
_CfprApFirmwareDownloaderProtocol_Type = CfprApFirmwareTransport
_CfprApFirmwareDownloaderProtocol_Object = MibTableColumn
cfprApFirmwareDownloaderProtocol = _CfprApFirmwareDownloaderProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 18),
    _CfprApFirmwareDownloaderProtocol_Type()
)
cfprApFirmwareDownloaderProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderProtocol.setStatus("current")
_CfprApFirmwareDownloaderPwd_Type = SnmpAdminString
_CfprApFirmwareDownloaderPwd_Object = MibTableColumn
cfprApFirmwareDownloaderPwd = _CfprApFirmwareDownloaderPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 19),
    _CfprApFirmwareDownloaderPwd_Type()
)
cfprApFirmwareDownloaderPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderPwd.setStatus("current")
_CfprApFirmwareDownloaderRemotePath_Type = SnmpAdminString
_CfprApFirmwareDownloaderRemotePath_Object = MibTableColumn
cfprApFirmwareDownloaderRemotePath = _CfprApFirmwareDownloaderRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 20),
    _CfprApFirmwareDownloaderRemotePath_Type()
)
cfprApFirmwareDownloaderRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderRemotePath.setStatus("current")
_CfprApFirmwareDownloaderServer_Type = SnmpAdminString
_CfprApFirmwareDownloaderServer_Object = MibTableColumn
cfprApFirmwareDownloaderServer = _CfprApFirmwareDownloaderServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 21),
    _CfprApFirmwareDownloaderServer_Type()
)
cfprApFirmwareDownloaderServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderServer.setStatus("current")
_CfprApFirmwareDownloaderStartTime_Type = DateAndTime
_CfprApFirmwareDownloaderStartTime_Object = MibTableColumn
cfprApFirmwareDownloaderStartTime = _CfprApFirmwareDownloaderStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 22),
    _CfprApFirmwareDownloaderStartTime_Type()
)
cfprApFirmwareDownloaderStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderStartTime.setStatus("current")
_CfprApFirmwareDownloaderTimeStamp_Type = DateAndTime
_CfprApFirmwareDownloaderTimeStamp_Object = MibTableColumn
cfprApFirmwareDownloaderTimeStamp = _CfprApFirmwareDownloaderTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 23),
    _CfprApFirmwareDownloaderTimeStamp_Type()
)
cfprApFirmwareDownloaderTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderTimeStamp.setStatus("current")
_CfprApFirmwareDownloaderTransferRate_Type = Integer32
_CfprApFirmwareDownloaderTransferRate_Object = MibTableColumn
cfprApFirmwareDownloaderTransferRate = _CfprApFirmwareDownloaderTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 24),
    _CfprApFirmwareDownloaderTransferRate_Type()
)
cfprApFirmwareDownloaderTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderTransferRate.setStatus("current")
_CfprApFirmwareDownloaderTransferState_Type = CfprApFirmwareTransferState
_CfprApFirmwareDownloaderTransferState_Object = MibTableColumn
cfprApFirmwareDownloaderTransferState = _CfprApFirmwareDownloaderTransferState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 25),
    _CfprApFirmwareDownloaderTransferState_Type()
)
cfprApFirmwareDownloaderTransferState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderTransferState.setStatus("current")
_CfprApFirmwareDownloaderUser_Type = SnmpAdminString
_CfprApFirmwareDownloaderUser_Object = MibTableColumn
cfprApFirmwareDownloaderUser = _CfprApFirmwareDownloaderUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 27, 1, 26),
    _CfprApFirmwareDownloaderUser_Type()
)
cfprApFirmwareDownloaderUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderUser.setStatus("current")
_CfprApFirmwareDownloaderFsmTable_Object = MibTable
cfprApFirmwareDownloaderFsmTable = _CfprApFirmwareDownloaderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28)
)
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmTable.setStatus("current")
_CfprApFirmwareDownloaderFsmEntry_Object = MibTableRow
cfprApFirmwareDownloaderFsmEntry = _CfprApFirmwareDownloaderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28, 1)
)
cfprApFirmwareDownloaderFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareDownloaderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmEntry.setStatus("current")
_CfprApFirmwareDownloaderFsmInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareDownloaderFsmInstanceId_Object = MibTableColumn
cfprApFirmwareDownloaderFsmInstanceId = _CfprApFirmwareDownloaderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28, 1, 1),
    _CfprApFirmwareDownloaderFsmInstanceId_Type()
)
cfprApFirmwareDownloaderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmInstanceId.setStatus("current")
_CfprApFirmwareDownloaderFsmDn_Type = CfprApManagedObjectDn
_CfprApFirmwareDownloaderFsmDn_Object = MibTableColumn
cfprApFirmwareDownloaderFsmDn = _CfprApFirmwareDownloaderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28, 1, 2),
    _CfprApFirmwareDownloaderFsmDn_Type()
)
cfprApFirmwareDownloaderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmDn.setStatus("current")
_CfprApFirmwareDownloaderFsmRn_Type = SnmpAdminString
_CfprApFirmwareDownloaderFsmRn_Object = MibTableColumn
cfprApFirmwareDownloaderFsmRn = _CfprApFirmwareDownloaderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28, 1, 3),
    _CfprApFirmwareDownloaderFsmRn_Type()
)
cfprApFirmwareDownloaderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmRn.setStatus("current")
_CfprApFirmwareDownloaderFsmCompletionTime_Type = DateAndTime
_CfprApFirmwareDownloaderFsmCompletionTime_Object = MibTableColumn
cfprApFirmwareDownloaderFsmCompletionTime = _CfprApFirmwareDownloaderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28, 1, 4),
    _CfprApFirmwareDownloaderFsmCompletionTime_Type()
)
cfprApFirmwareDownloaderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmCompletionTime.setStatus("current")
_CfprApFirmwareDownloaderFsmCurrentFsm_Type = CfprApFirmwareDownloaderFsmCurrentFsm
_CfprApFirmwareDownloaderFsmCurrentFsm_Object = MibTableColumn
cfprApFirmwareDownloaderFsmCurrentFsm = _CfprApFirmwareDownloaderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28, 1, 5),
    _CfprApFirmwareDownloaderFsmCurrentFsm_Type()
)
cfprApFirmwareDownloaderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmCurrentFsm.setStatus("current")
_CfprApFirmwareDownloaderFsmDescrData_Type = SnmpAdminString
_CfprApFirmwareDownloaderFsmDescrData_Object = MibTableColumn
cfprApFirmwareDownloaderFsmDescrData = _CfprApFirmwareDownloaderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28, 1, 6),
    _CfprApFirmwareDownloaderFsmDescrData_Type()
)
cfprApFirmwareDownloaderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmDescrData.setStatus("current")
_CfprApFirmwareDownloaderFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwareDownloaderFsmFsmStatus_Object = MibTableColumn
cfprApFirmwareDownloaderFsmFsmStatus = _CfprApFirmwareDownloaderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28, 1, 7),
    _CfprApFirmwareDownloaderFsmFsmStatus_Type()
)
cfprApFirmwareDownloaderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmFsmStatus.setStatus("current")
_CfprApFirmwareDownloaderFsmProgress_Type = Gauge32
_CfprApFirmwareDownloaderFsmProgress_Object = MibTableColumn
cfprApFirmwareDownloaderFsmProgress = _CfprApFirmwareDownloaderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28, 1, 8),
    _CfprApFirmwareDownloaderFsmProgress_Type()
)
cfprApFirmwareDownloaderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmProgress.setStatus("current")
_CfprApFirmwareDownloaderFsmRmtErrCode_Type = Gauge32
_CfprApFirmwareDownloaderFsmRmtErrCode_Object = MibTableColumn
cfprApFirmwareDownloaderFsmRmtErrCode = _CfprApFirmwareDownloaderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28, 1, 9),
    _CfprApFirmwareDownloaderFsmRmtErrCode_Type()
)
cfprApFirmwareDownloaderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmRmtErrCode.setStatus("current")
_CfprApFirmwareDownloaderFsmRmtErrDescr_Type = SnmpAdminString
_CfprApFirmwareDownloaderFsmRmtErrDescr_Object = MibTableColumn
cfprApFirmwareDownloaderFsmRmtErrDescr = _CfprApFirmwareDownloaderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28, 1, 10),
    _CfprApFirmwareDownloaderFsmRmtErrDescr_Type()
)
cfprApFirmwareDownloaderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmRmtErrDescr.setStatus("current")
_CfprApFirmwareDownloaderFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwareDownloaderFsmRmtRslt_Object = MibTableColumn
cfprApFirmwareDownloaderFsmRmtRslt = _CfprApFirmwareDownloaderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 28, 1, 11),
    _CfprApFirmwareDownloaderFsmRmtRslt_Type()
)
cfprApFirmwareDownloaderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmRmtRslt.setStatus("current")
_CfprApFirmwareDownloaderFsmStageTable_Object = MibTable
cfprApFirmwareDownloaderFsmStageTable = _CfprApFirmwareDownloaderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 29)
)
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStageTable.setStatus("current")
_CfprApFirmwareDownloaderFsmStageEntry_Object = MibTableRow
cfprApFirmwareDownloaderFsmStageEntry = _CfprApFirmwareDownloaderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 29, 1)
)
cfprApFirmwareDownloaderFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareDownloaderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStageEntry.setStatus("current")
_CfprApFirmwareDownloaderFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareDownloaderFsmStageInstanceId_Object = MibTableColumn
cfprApFirmwareDownloaderFsmStageInstanceId = _CfprApFirmwareDownloaderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 29, 1, 1),
    _CfprApFirmwareDownloaderFsmStageInstanceId_Type()
)
cfprApFirmwareDownloaderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStageInstanceId.setStatus("current")
_CfprApFirmwareDownloaderFsmStageDn_Type = CfprApManagedObjectDn
_CfprApFirmwareDownloaderFsmStageDn_Object = MibTableColumn
cfprApFirmwareDownloaderFsmStageDn = _CfprApFirmwareDownloaderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 29, 1, 2),
    _CfprApFirmwareDownloaderFsmStageDn_Type()
)
cfprApFirmwareDownloaderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStageDn.setStatus("current")
_CfprApFirmwareDownloaderFsmStageRn_Type = SnmpAdminString
_CfprApFirmwareDownloaderFsmStageRn_Object = MibTableColumn
cfprApFirmwareDownloaderFsmStageRn = _CfprApFirmwareDownloaderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 29, 1, 3),
    _CfprApFirmwareDownloaderFsmStageRn_Type()
)
cfprApFirmwareDownloaderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStageRn.setStatus("current")
_CfprApFirmwareDownloaderFsmStageDescrData_Type = SnmpAdminString
_CfprApFirmwareDownloaderFsmStageDescrData_Object = MibTableColumn
cfprApFirmwareDownloaderFsmStageDescrData = _CfprApFirmwareDownloaderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 29, 1, 4),
    _CfprApFirmwareDownloaderFsmStageDescrData_Type()
)
cfprApFirmwareDownloaderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStageDescrData.setStatus("current")
_CfprApFirmwareDownloaderFsmStageLastUpdateTime_Type = DateAndTime
_CfprApFirmwareDownloaderFsmStageLastUpdateTime_Object = MibTableColumn
cfprApFirmwareDownloaderFsmStageLastUpdateTime = _CfprApFirmwareDownloaderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 29, 1, 5),
    _CfprApFirmwareDownloaderFsmStageLastUpdateTime_Type()
)
cfprApFirmwareDownloaderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStageLastUpdateTime.setStatus("current")
_CfprApFirmwareDownloaderFsmStageName_Type = CfprApFirmwareDownloaderFsmStageName
_CfprApFirmwareDownloaderFsmStageName_Object = MibTableColumn
cfprApFirmwareDownloaderFsmStageName = _CfprApFirmwareDownloaderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 29, 1, 6),
    _CfprApFirmwareDownloaderFsmStageName_Type()
)
cfprApFirmwareDownloaderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStageName.setStatus("current")
_CfprApFirmwareDownloaderFsmStageOrder_Type = Gauge32
_CfprApFirmwareDownloaderFsmStageOrder_Object = MibTableColumn
cfprApFirmwareDownloaderFsmStageOrder = _CfprApFirmwareDownloaderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 29, 1, 7),
    _CfprApFirmwareDownloaderFsmStageOrder_Type()
)
cfprApFirmwareDownloaderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStageOrder.setStatus("current")
_CfprApFirmwareDownloaderFsmStageRetry_Type = Gauge32
_CfprApFirmwareDownloaderFsmStageRetry_Object = MibTableColumn
cfprApFirmwareDownloaderFsmStageRetry = _CfprApFirmwareDownloaderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 29, 1, 8),
    _CfprApFirmwareDownloaderFsmStageRetry_Type()
)
cfprApFirmwareDownloaderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStageRetry.setStatus("current")
_CfprApFirmwareDownloaderFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwareDownloaderFsmStageStageStatus_Object = MibTableColumn
cfprApFirmwareDownloaderFsmStageStageStatus = _CfprApFirmwareDownloaderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 29, 1, 9),
    _CfprApFirmwareDownloaderFsmStageStageStatus_Type()
)
cfprApFirmwareDownloaderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmStageStageStatus.setStatus("current")
_CfprApFirmwareDownloaderFsmTaskTable_Object = MibTable
cfprApFirmwareDownloaderFsmTaskTable = _CfprApFirmwareDownloaderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 30)
)
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmTaskTable.setStatus("current")
_CfprApFirmwareDownloaderFsmTaskEntry_Object = MibTableRow
cfprApFirmwareDownloaderFsmTaskEntry = _CfprApFirmwareDownloaderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 30, 1)
)
cfprApFirmwareDownloaderFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareDownloaderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmTaskEntry.setStatus("current")
_CfprApFirmwareDownloaderFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareDownloaderFsmTaskInstanceId_Object = MibTableColumn
cfprApFirmwareDownloaderFsmTaskInstanceId = _CfprApFirmwareDownloaderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 30, 1, 1),
    _CfprApFirmwareDownloaderFsmTaskInstanceId_Type()
)
cfprApFirmwareDownloaderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmTaskInstanceId.setStatus("current")
_CfprApFirmwareDownloaderFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApFirmwareDownloaderFsmTaskDn_Object = MibTableColumn
cfprApFirmwareDownloaderFsmTaskDn = _CfprApFirmwareDownloaderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 30, 1, 2),
    _CfprApFirmwareDownloaderFsmTaskDn_Type()
)
cfprApFirmwareDownloaderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmTaskDn.setStatus("current")
_CfprApFirmwareDownloaderFsmTaskRn_Type = SnmpAdminString
_CfprApFirmwareDownloaderFsmTaskRn_Object = MibTableColumn
cfprApFirmwareDownloaderFsmTaskRn = _CfprApFirmwareDownloaderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 30, 1, 3),
    _CfprApFirmwareDownloaderFsmTaskRn_Type()
)
cfprApFirmwareDownloaderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmTaskRn.setStatus("current")
_CfprApFirmwareDownloaderFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApFirmwareDownloaderFsmTaskCompletion_Object = MibTableColumn
cfprApFirmwareDownloaderFsmTaskCompletion = _CfprApFirmwareDownloaderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 30, 1, 4),
    _CfprApFirmwareDownloaderFsmTaskCompletion_Type()
)
cfprApFirmwareDownloaderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmTaskCompletion.setStatus("current")
_CfprApFirmwareDownloaderFsmTaskFlags_Type = CfprApFsmFlags
_CfprApFirmwareDownloaderFsmTaskFlags_Object = MibTableColumn
cfprApFirmwareDownloaderFsmTaskFlags = _CfprApFirmwareDownloaderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 30, 1, 5),
    _CfprApFirmwareDownloaderFsmTaskFlags_Type()
)
cfprApFirmwareDownloaderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmTaskFlags.setStatus("current")
_CfprApFirmwareDownloaderFsmTaskItem_Type = CfprApFirmwareDownloaderFsmTaskItem
_CfprApFirmwareDownloaderFsmTaskItem_Object = MibTableColumn
cfprApFirmwareDownloaderFsmTaskItem = _CfprApFirmwareDownloaderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 30, 1, 6),
    _CfprApFirmwareDownloaderFsmTaskItem_Type()
)
cfprApFirmwareDownloaderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmTaskItem.setStatus("current")
_CfprApFirmwareDownloaderFsmTaskSeqId_Type = Gauge32
_CfprApFirmwareDownloaderFsmTaskSeqId_Object = MibTableColumn
cfprApFirmwareDownloaderFsmTaskSeqId = _CfprApFirmwareDownloaderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 30, 1, 7),
    _CfprApFirmwareDownloaderFsmTaskSeqId_Type()
)
cfprApFirmwareDownloaderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareDownloaderFsmTaskSeqId.setStatus("current")
_CfprApFirmwareHostTable_Object = MibTable
cfprApFirmwareHostTable = _CfprApFirmwareHostTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 31)
)
if mibBuilder.loadTexts:
    cfprApFirmwareHostTable.setStatus("current")
_CfprApFirmwareHostEntry_Object = MibTableRow
cfprApFirmwareHostEntry = _CfprApFirmwareHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 31, 1)
)
cfprApFirmwareHostEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareHostInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareHostEntry.setStatus("current")
_CfprApFirmwareHostInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareHostInstanceId_Object = MibTableColumn
cfprApFirmwareHostInstanceId = _CfprApFirmwareHostInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 31, 1, 1),
    _CfprApFirmwareHostInstanceId_Type()
)
cfprApFirmwareHostInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareHostInstanceId.setStatus("current")
_CfprApFirmwareHostDn_Type = CfprApManagedObjectDn
_CfprApFirmwareHostDn_Object = MibTableColumn
cfprApFirmwareHostDn = _CfprApFirmwareHostDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 31, 1, 2),
    _CfprApFirmwareHostDn_Type()
)
cfprApFirmwareHostDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareHostDn.setStatus("current")
_CfprApFirmwareHostRn_Type = SnmpAdminString
_CfprApFirmwareHostRn_Object = MibTableColumn
cfprApFirmwareHostRn = _CfprApFirmwareHostRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 31, 1, 3),
    _CfprApFirmwareHostRn_Type()
)
cfprApFirmwareHostRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareHostRn.setStatus("current")
_CfprApFirmwareHostPackModImpactTable_Object = MibTable
cfprApFirmwareHostPackModImpactTable = _CfprApFirmwareHostPackModImpactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 32)
)
if mibBuilder.loadTexts:
    cfprApFirmwareHostPackModImpactTable.setStatus("current")
_CfprApFirmwareHostPackModImpactEntry_Object = MibTableRow
cfprApFirmwareHostPackModImpactEntry = _CfprApFirmwareHostPackModImpactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 32, 1)
)
cfprApFirmwareHostPackModImpactEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareHostPackModImpactInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareHostPackModImpactEntry.setStatus("current")
_CfprApFirmwareHostPackModImpactInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareHostPackModImpactInstanceId_Object = MibTableColumn
cfprApFirmwareHostPackModImpactInstanceId = _CfprApFirmwareHostPackModImpactInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 32, 1, 1),
    _CfprApFirmwareHostPackModImpactInstanceId_Type()
)
cfprApFirmwareHostPackModImpactInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareHostPackModImpactInstanceId.setStatus("current")
_CfprApFirmwareHostPackModImpactDn_Type = CfprApManagedObjectDn
_CfprApFirmwareHostPackModImpactDn_Object = MibTableColumn
cfprApFirmwareHostPackModImpactDn = _CfprApFirmwareHostPackModImpactDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 32, 1, 2),
    _CfprApFirmwareHostPackModImpactDn_Type()
)
cfprApFirmwareHostPackModImpactDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareHostPackModImpactDn.setStatus("current")
_CfprApFirmwareHostPackModImpactRn_Type = SnmpAdminString
_CfprApFirmwareHostPackModImpactRn_Object = MibTableColumn
cfprApFirmwareHostPackModImpactRn = _CfprApFirmwareHostPackModImpactRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 32, 1, 3),
    _CfprApFirmwareHostPackModImpactRn_Type()
)
cfprApFirmwareHostPackModImpactRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareHostPackModImpactRn.setStatus("current")
_CfprApFirmwareHostPackModImpactKeyDn_Type = SnmpAdminString
_CfprApFirmwareHostPackModImpactKeyDn_Object = MibTableColumn
cfprApFirmwareHostPackModImpactKeyDn = _CfprApFirmwareHostPackModImpactKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 32, 1, 4),
    _CfprApFirmwareHostPackModImpactKeyDn_Type()
)
cfprApFirmwareHostPackModImpactKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareHostPackModImpactKeyDn.setStatus("current")
_CfprApFirmwareHostPackModImpactMaintPolicyDn_Type = SnmpAdminString
_CfprApFirmwareHostPackModImpactMaintPolicyDn_Object = MibTableColumn
cfprApFirmwareHostPackModImpactMaintPolicyDn = _CfprApFirmwareHostPackModImpactMaintPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 32, 1, 5),
    _CfprApFirmwareHostPackModImpactMaintPolicyDn_Type()
)
cfprApFirmwareHostPackModImpactMaintPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareHostPackModImpactMaintPolicyDn.setStatus("current")
_CfprApFirmwareHostPackModImpactPnDn_Type = SnmpAdminString
_CfprApFirmwareHostPackModImpactPnDn_Object = MibTableColumn
cfprApFirmwareHostPackModImpactPnDn = _CfprApFirmwareHostPackModImpactPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 32, 1, 6),
    _CfprApFirmwareHostPackModImpactPnDn_Type()
)
cfprApFirmwareHostPackModImpactPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareHostPackModImpactPnDn.setStatus("current")
_CfprApFirmwareHostPackModImpactRebootPolicy_Type = SnmpAdminString
_CfprApFirmwareHostPackModImpactRebootPolicy_Object = MibTableColumn
cfprApFirmwareHostPackModImpactRebootPolicy = _CfprApFirmwareHostPackModImpactRebootPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 32, 1, 7),
    _CfprApFirmwareHostPackModImpactRebootPolicy_Type()
)
cfprApFirmwareHostPackModImpactRebootPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareHostPackModImpactRebootPolicy.setStatus("current")
_CfprApFirmwareHostPackModImpactServiceProfileDn_Type = SnmpAdminString
_CfprApFirmwareHostPackModImpactServiceProfileDn_Object = MibTableColumn
cfprApFirmwareHostPackModImpactServiceProfileDn = _CfprApFirmwareHostPackModImpactServiceProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 32, 1, 8),
    _CfprApFirmwareHostPackModImpactServiceProfileDn_Type()
)
cfprApFirmwareHostPackModImpactServiceProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareHostPackModImpactServiceProfileDn.setStatus("current")
_CfprApFirmwareImageTable_Object = MibTable
cfprApFirmwareImageTable = _CfprApFirmwareImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33)
)
if mibBuilder.loadTexts:
    cfprApFirmwareImageTable.setStatus("current")
_CfprApFirmwareImageEntry_Object = MibTableRow
cfprApFirmwareImageEntry = _CfprApFirmwareImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1)
)
cfprApFirmwareImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareImageEntry.setStatus("current")
_CfprApFirmwareImageInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareImageInstanceId_Object = MibTableColumn
cfprApFirmwareImageInstanceId = _CfprApFirmwareImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 1),
    _CfprApFirmwareImageInstanceId_Type()
)
cfprApFirmwareImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareImageInstanceId.setStatus("current")
_CfprApFirmwareImageDn_Type = CfprApManagedObjectDn
_CfprApFirmwareImageDn_Object = MibTableColumn
cfprApFirmwareImageDn = _CfprApFirmwareImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 2),
    _CfprApFirmwareImageDn_Type()
)
cfprApFirmwareImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageDn.setStatus("current")
_CfprApFirmwareImageRn_Type = SnmpAdminString
_CfprApFirmwareImageRn_Object = MibTableColumn
cfprApFirmwareImageRn = _CfprApFirmwareImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 3),
    _CfprApFirmwareImageRn_Type()
)
cfprApFirmwareImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageRn.setStatus("current")
_CfprApFirmwareImageAdminState_Type = CfprApFirmwareAdminState
_CfprApFirmwareImageAdminState_Object = MibTableColumn
cfprApFirmwareImageAdminState = _CfprApFirmwareImageAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 4),
    _CfprApFirmwareImageAdminState_Type()
)
cfprApFirmwareImageAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageAdminState.setStatus("current")
_CfprApFirmwareImageChecksum_Type = SnmpAdminString
_CfprApFirmwareImageChecksum_Object = MibTableColumn
cfprApFirmwareImageChecksum = _CfprApFirmwareImageChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 5),
    _CfprApFirmwareImageChecksum_Type()
)
cfprApFirmwareImageChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageChecksum.setStatus("current")
_CfprApFirmwareImageDescr_Type = SnmpAdminString
_CfprApFirmwareImageDescr_Object = MibTableColumn
cfprApFirmwareImageDescr = _CfprApFirmwareImageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 6),
    _CfprApFirmwareImageDescr_Type()
)
cfprApFirmwareImageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageDescr.setStatus("current")
_CfprApFirmwareImageDownloadDate_Type = DateAndTime
_CfprApFirmwareImageDownloadDate_Object = MibTableColumn
cfprApFirmwareImageDownloadDate = _CfprApFirmwareImageDownloadDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 7),
    _CfprApFirmwareImageDownloadDate_Type()
)
cfprApFirmwareImageDownloadDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageDownloadDate.setStatus("current")
_CfprApFirmwareImageFsmDescr_Type = SnmpAdminString
_CfprApFirmwareImageFsmDescr_Object = MibTableColumn
cfprApFirmwareImageFsmDescr = _CfprApFirmwareImageFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 8),
    _CfprApFirmwareImageFsmDescr_Type()
)
cfprApFirmwareImageFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmDescr.setStatus("current")
_CfprApFirmwareImageFsmPrev_Type = SnmpAdminString
_CfprApFirmwareImageFsmPrev_Object = MibTableColumn
cfprApFirmwareImageFsmPrev = _CfprApFirmwareImageFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 9),
    _CfprApFirmwareImageFsmPrev_Type()
)
cfprApFirmwareImageFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmPrev.setStatus("current")
_CfprApFirmwareImageFsmProgr_Type = Gauge32
_CfprApFirmwareImageFsmProgr_Object = MibTableColumn
cfprApFirmwareImageFsmProgr = _CfprApFirmwareImageFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 10),
    _CfprApFirmwareImageFsmProgr_Type()
)
cfprApFirmwareImageFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmProgr.setStatus("current")
_CfprApFirmwareImageFsmRmtInvErrCode_Type = Gauge32
_CfprApFirmwareImageFsmRmtInvErrCode_Object = MibTableColumn
cfprApFirmwareImageFsmRmtInvErrCode = _CfprApFirmwareImageFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 11),
    _CfprApFirmwareImageFsmRmtInvErrCode_Type()
)
cfprApFirmwareImageFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmRmtInvErrCode.setStatus("current")
_CfprApFirmwareImageFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApFirmwareImageFsmRmtInvErrDescr_Object = MibTableColumn
cfprApFirmwareImageFsmRmtInvErrDescr = _CfprApFirmwareImageFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 12),
    _CfprApFirmwareImageFsmRmtInvErrDescr_Type()
)
cfprApFirmwareImageFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmRmtInvErrDescr.setStatus("current")
_CfprApFirmwareImageFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwareImageFsmRmtInvRslt_Object = MibTableColumn
cfprApFirmwareImageFsmRmtInvRslt = _CfprApFirmwareImageFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 13),
    _CfprApFirmwareImageFsmRmtInvRslt_Type()
)
cfprApFirmwareImageFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmRmtInvRslt.setStatus("current")
_CfprApFirmwareImageFsmStageDescr_Type = SnmpAdminString
_CfprApFirmwareImageFsmStageDescr_Object = MibTableColumn
cfprApFirmwareImageFsmStageDescr = _CfprApFirmwareImageFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 14),
    _CfprApFirmwareImageFsmStageDescr_Type()
)
cfprApFirmwareImageFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStageDescr.setStatus("current")
_CfprApFirmwareImageFsmStamp_Type = DateAndTime
_CfprApFirmwareImageFsmStamp_Object = MibTableColumn
cfprApFirmwareImageFsmStamp = _CfprApFirmwareImageFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 15),
    _CfprApFirmwareImageFsmStamp_Type()
)
cfprApFirmwareImageFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStamp.setStatus("current")
_CfprApFirmwareImageFsmStatus_Type = SnmpAdminString
_CfprApFirmwareImageFsmStatus_Object = MibTableColumn
cfprApFirmwareImageFsmStatus = _CfprApFirmwareImageFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 16),
    _CfprApFirmwareImageFsmStatus_Type()
)
cfprApFirmwareImageFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStatus.setStatus("current")
_CfprApFirmwareImageFsmTry_Type = Gauge32
_CfprApFirmwareImageFsmTry_Object = MibTableColumn
cfprApFirmwareImageFsmTry = _CfprApFirmwareImageFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 17),
    _CfprApFirmwareImageFsmTry_Type()
)
cfprApFirmwareImageFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmTry.setStatus("current")
_CfprApFirmwareImageImagePresence_Type = CfprApFirmwareImagePresence
_CfprApFirmwareImageImagePresence_Object = MibTableColumn
cfprApFirmwareImageImagePresence = _CfprApFirmwareImageImagePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 18),
    _CfprApFirmwareImageImagePresence_Type()
)
cfprApFirmwareImageImagePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageImagePresence.setStatus("current")
_CfprApFirmwareImageIntId_Type = SnmpAdminString
_CfprApFirmwareImageIntId_Object = MibTableColumn
cfprApFirmwareImageIntId = _CfprApFirmwareImageIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 19),
    _CfprApFirmwareImageIntId_Type()
)
cfprApFirmwareImageIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageIntId.setStatus("current")
_CfprApFirmwareImageInvTag_Type = SnmpAdminString
_CfprApFirmwareImageInvTag_Object = MibTableColumn
cfprApFirmwareImageInvTag = _CfprApFirmwareImageInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 20),
    _CfprApFirmwareImageInvTag_Type()
)
cfprApFirmwareImageInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageInvTag.setStatus("current")
_CfprApFirmwareImageIsoname_Type = SnmpAdminString
_CfprApFirmwareImageIsoname_Object = MibTableColumn
cfprApFirmwareImageIsoname = _CfprApFirmwareImageIsoname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 21),
    _CfprApFirmwareImageIsoname_Type()
)
cfprApFirmwareImageIsoname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageIsoname.setStatus("current")
_CfprApFirmwareImageLocation_Type = SnmpAdminString
_CfprApFirmwareImageLocation_Object = MibTableColumn
cfprApFirmwareImageLocation = _CfprApFirmwareImageLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 22),
    _CfprApFirmwareImageLocation_Type()
)
cfprApFirmwareImageLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageLocation.setStatus("current")
_CfprApFirmwareImageName_Type = SnmpAdminString
_CfprApFirmwareImageName_Object = MibTableColumn
cfprApFirmwareImageName = _CfprApFirmwareImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 23),
    _CfprApFirmwareImageName_Type()
)
cfprApFirmwareImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageName.setStatus("current")
_CfprApFirmwareImagePolicyLevel_Type = Gauge32
_CfprApFirmwareImagePolicyLevel_Object = MibTableColumn
cfprApFirmwareImagePolicyLevel = _CfprApFirmwareImagePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 24),
    _CfprApFirmwareImagePolicyLevel_Type()
)
cfprApFirmwareImagePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImagePolicyLevel.setStatus("current")
_CfprApFirmwareImagePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwareImagePolicyOwner_Object = MibTableColumn
cfprApFirmwareImagePolicyOwner = _CfprApFirmwareImagePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 25),
    _CfprApFirmwareImagePolicyOwner_Type()
)
cfprApFirmwareImagePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImagePolicyOwner.setStatus("current")
_CfprApFirmwareImageSize_Type = Gauge32
_CfprApFirmwareImageSize_Object = MibTableColumn
cfprApFirmwareImageSize = _CfprApFirmwareImageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 26),
    _CfprApFirmwareImageSize_Type()
)
cfprApFirmwareImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageSize.setStatus("current")
_CfprApFirmwareImageType_Type = CfprApFirmwareType
_CfprApFirmwareImageType_Object = MibTableColumn
cfprApFirmwareImageType = _CfprApFirmwareImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 27),
    _CfprApFirmwareImageType_Type()
)
cfprApFirmwareImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageType.setStatus("current")
_CfprApFirmwareImageVersion_Type = SnmpAdminString
_CfprApFirmwareImageVersion_Object = MibTableColumn
cfprApFirmwareImageVersion = _CfprApFirmwareImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 33, 1, 28),
    _CfprApFirmwareImageVersion_Type()
)
cfprApFirmwareImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageVersion.setStatus("current")
_CfprApFirmwareImageFsmTable_Object = MibTable
cfprApFirmwareImageFsmTable = _CfprApFirmwareImageFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34)
)
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmTable.setStatus("current")
_CfprApFirmwareImageFsmEntry_Object = MibTableRow
cfprApFirmwareImageFsmEntry = _CfprApFirmwareImageFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34, 1)
)
cfprApFirmwareImageFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareImageFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmEntry.setStatus("current")
_CfprApFirmwareImageFsmInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareImageFsmInstanceId_Object = MibTableColumn
cfprApFirmwareImageFsmInstanceId = _CfprApFirmwareImageFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34, 1, 1),
    _CfprApFirmwareImageFsmInstanceId_Type()
)
cfprApFirmwareImageFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmInstanceId.setStatus("current")
_CfprApFirmwareImageFsmDn_Type = CfprApManagedObjectDn
_CfprApFirmwareImageFsmDn_Object = MibTableColumn
cfprApFirmwareImageFsmDn = _CfprApFirmwareImageFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34, 1, 2),
    _CfprApFirmwareImageFsmDn_Type()
)
cfprApFirmwareImageFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmDn.setStatus("current")
_CfprApFirmwareImageFsmRn_Type = SnmpAdminString
_CfprApFirmwareImageFsmRn_Object = MibTableColumn
cfprApFirmwareImageFsmRn = _CfprApFirmwareImageFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34, 1, 3),
    _CfprApFirmwareImageFsmRn_Type()
)
cfprApFirmwareImageFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmRn.setStatus("current")
_CfprApFirmwareImageFsmCompletionTime_Type = DateAndTime
_CfprApFirmwareImageFsmCompletionTime_Object = MibTableColumn
cfprApFirmwareImageFsmCompletionTime = _CfprApFirmwareImageFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34, 1, 4),
    _CfprApFirmwareImageFsmCompletionTime_Type()
)
cfprApFirmwareImageFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmCompletionTime.setStatus("current")
_CfprApFirmwareImageFsmCurrentFsm_Type = CfprApFirmwareImageFsmCurrentFsm
_CfprApFirmwareImageFsmCurrentFsm_Object = MibTableColumn
cfprApFirmwareImageFsmCurrentFsm = _CfprApFirmwareImageFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34, 1, 5),
    _CfprApFirmwareImageFsmCurrentFsm_Type()
)
cfprApFirmwareImageFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmCurrentFsm.setStatus("current")
_CfprApFirmwareImageFsmDescrData_Type = SnmpAdminString
_CfprApFirmwareImageFsmDescrData_Object = MibTableColumn
cfprApFirmwareImageFsmDescrData = _CfprApFirmwareImageFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34, 1, 6),
    _CfprApFirmwareImageFsmDescrData_Type()
)
cfprApFirmwareImageFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmDescrData.setStatus("current")
_CfprApFirmwareImageFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwareImageFsmFsmStatus_Object = MibTableColumn
cfprApFirmwareImageFsmFsmStatus = _CfprApFirmwareImageFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34, 1, 7),
    _CfprApFirmwareImageFsmFsmStatus_Type()
)
cfprApFirmwareImageFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmFsmStatus.setStatus("current")
_CfprApFirmwareImageFsmProgress_Type = Gauge32
_CfprApFirmwareImageFsmProgress_Object = MibTableColumn
cfprApFirmwareImageFsmProgress = _CfprApFirmwareImageFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34, 1, 8),
    _CfprApFirmwareImageFsmProgress_Type()
)
cfprApFirmwareImageFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmProgress.setStatus("current")
_CfprApFirmwareImageFsmRmtErrCode_Type = Gauge32
_CfprApFirmwareImageFsmRmtErrCode_Object = MibTableColumn
cfprApFirmwareImageFsmRmtErrCode = _CfprApFirmwareImageFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34, 1, 9),
    _CfprApFirmwareImageFsmRmtErrCode_Type()
)
cfprApFirmwareImageFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmRmtErrCode.setStatus("current")
_CfprApFirmwareImageFsmRmtErrDescr_Type = SnmpAdminString
_CfprApFirmwareImageFsmRmtErrDescr_Object = MibTableColumn
cfprApFirmwareImageFsmRmtErrDescr = _CfprApFirmwareImageFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34, 1, 10),
    _CfprApFirmwareImageFsmRmtErrDescr_Type()
)
cfprApFirmwareImageFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmRmtErrDescr.setStatus("current")
_CfprApFirmwareImageFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwareImageFsmRmtRslt_Object = MibTableColumn
cfprApFirmwareImageFsmRmtRslt = _CfprApFirmwareImageFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 34, 1, 11),
    _CfprApFirmwareImageFsmRmtRslt_Type()
)
cfprApFirmwareImageFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmRmtRslt.setStatus("current")
_CfprApFirmwareImageFsmStageTable_Object = MibTable
cfprApFirmwareImageFsmStageTable = _CfprApFirmwareImageFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 35)
)
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStageTable.setStatus("current")
_CfprApFirmwareImageFsmStageEntry_Object = MibTableRow
cfprApFirmwareImageFsmStageEntry = _CfprApFirmwareImageFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 35, 1)
)
cfprApFirmwareImageFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareImageFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStageEntry.setStatus("current")
_CfprApFirmwareImageFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareImageFsmStageInstanceId_Object = MibTableColumn
cfprApFirmwareImageFsmStageInstanceId = _CfprApFirmwareImageFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 35, 1, 1),
    _CfprApFirmwareImageFsmStageInstanceId_Type()
)
cfprApFirmwareImageFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStageInstanceId.setStatus("current")
_CfprApFirmwareImageFsmStageDn_Type = CfprApManagedObjectDn
_CfprApFirmwareImageFsmStageDn_Object = MibTableColumn
cfprApFirmwareImageFsmStageDn = _CfprApFirmwareImageFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 35, 1, 2),
    _CfprApFirmwareImageFsmStageDn_Type()
)
cfprApFirmwareImageFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStageDn.setStatus("current")
_CfprApFirmwareImageFsmStageRn_Type = SnmpAdminString
_CfprApFirmwareImageFsmStageRn_Object = MibTableColumn
cfprApFirmwareImageFsmStageRn = _CfprApFirmwareImageFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 35, 1, 3),
    _CfprApFirmwareImageFsmStageRn_Type()
)
cfprApFirmwareImageFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStageRn.setStatus("current")
_CfprApFirmwareImageFsmStageDescrData_Type = SnmpAdminString
_CfprApFirmwareImageFsmStageDescrData_Object = MibTableColumn
cfprApFirmwareImageFsmStageDescrData = _CfprApFirmwareImageFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 35, 1, 4),
    _CfprApFirmwareImageFsmStageDescrData_Type()
)
cfprApFirmwareImageFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStageDescrData.setStatus("current")
_CfprApFirmwareImageFsmStageLastUpdateTime_Type = DateAndTime
_CfprApFirmwareImageFsmStageLastUpdateTime_Object = MibTableColumn
cfprApFirmwareImageFsmStageLastUpdateTime = _CfprApFirmwareImageFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 35, 1, 5),
    _CfprApFirmwareImageFsmStageLastUpdateTime_Type()
)
cfprApFirmwareImageFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStageLastUpdateTime.setStatus("current")
_CfprApFirmwareImageFsmStageName_Type = CfprApFirmwareImageFsmStageName
_CfprApFirmwareImageFsmStageName_Object = MibTableColumn
cfprApFirmwareImageFsmStageName = _CfprApFirmwareImageFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 35, 1, 6),
    _CfprApFirmwareImageFsmStageName_Type()
)
cfprApFirmwareImageFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStageName.setStatus("current")
_CfprApFirmwareImageFsmStageOrder_Type = Gauge32
_CfprApFirmwareImageFsmStageOrder_Object = MibTableColumn
cfprApFirmwareImageFsmStageOrder = _CfprApFirmwareImageFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 35, 1, 7),
    _CfprApFirmwareImageFsmStageOrder_Type()
)
cfprApFirmwareImageFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStageOrder.setStatus("current")
_CfprApFirmwareImageFsmStageRetry_Type = Gauge32
_CfprApFirmwareImageFsmStageRetry_Object = MibTableColumn
cfprApFirmwareImageFsmStageRetry = _CfprApFirmwareImageFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 35, 1, 8),
    _CfprApFirmwareImageFsmStageRetry_Type()
)
cfprApFirmwareImageFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStageRetry.setStatus("current")
_CfprApFirmwareImageFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwareImageFsmStageStageStatus_Object = MibTableColumn
cfprApFirmwareImageFsmStageStageStatus = _CfprApFirmwareImageFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 35, 1, 9),
    _CfprApFirmwareImageFsmStageStageStatus_Type()
)
cfprApFirmwareImageFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmStageStageStatus.setStatus("current")
_CfprApFirmwareImageFsmTaskTable_Object = MibTable
cfprApFirmwareImageFsmTaskTable = _CfprApFirmwareImageFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 36)
)
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmTaskTable.setStatus("current")
_CfprApFirmwareImageFsmTaskEntry_Object = MibTableRow
cfprApFirmwareImageFsmTaskEntry = _CfprApFirmwareImageFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 36, 1)
)
cfprApFirmwareImageFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareImageFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmTaskEntry.setStatus("current")
_CfprApFirmwareImageFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareImageFsmTaskInstanceId_Object = MibTableColumn
cfprApFirmwareImageFsmTaskInstanceId = _CfprApFirmwareImageFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 36, 1, 1),
    _CfprApFirmwareImageFsmTaskInstanceId_Type()
)
cfprApFirmwareImageFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmTaskInstanceId.setStatus("current")
_CfprApFirmwareImageFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApFirmwareImageFsmTaskDn_Object = MibTableColumn
cfprApFirmwareImageFsmTaskDn = _CfprApFirmwareImageFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 36, 1, 2),
    _CfprApFirmwareImageFsmTaskDn_Type()
)
cfprApFirmwareImageFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmTaskDn.setStatus("current")
_CfprApFirmwareImageFsmTaskRn_Type = SnmpAdminString
_CfprApFirmwareImageFsmTaskRn_Object = MibTableColumn
cfprApFirmwareImageFsmTaskRn = _CfprApFirmwareImageFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 36, 1, 3),
    _CfprApFirmwareImageFsmTaskRn_Type()
)
cfprApFirmwareImageFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmTaskRn.setStatus("current")
_CfprApFirmwareImageFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApFirmwareImageFsmTaskCompletion_Object = MibTableColumn
cfprApFirmwareImageFsmTaskCompletion = _CfprApFirmwareImageFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 36, 1, 4),
    _CfprApFirmwareImageFsmTaskCompletion_Type()
)
cfprApFirmwareImageFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmTaskCompletion.setStatus("current")
_CfprApFirmwareImageFsmTaskFlags_Type = CfprApFsmFlags
_CfprApFirmwareImageFsmTaskFlags_Object = MibTableColumn
cfprApFirmwareImageFsmTaskFlags = _CfprApFirmwareImageFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 36, 1, 5),
    _CfprApFirmwareImageFsmTaskFlags_Type()
)
cfprApFirmwareImageFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmTaskFlags.setStatus("current")
_CfprApFirmwareImageFsmTaskItem_Type = CfprApFirmwareImageFsmTaskItem
_CfprApFirmwareImageFsmTaskItem_Object = MibTableColumn
cfprApFirmwareImageFsmTaskItem = _CfprApFirmwareImageFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 36, 1, 6),
    _CfprApFirmwareImageFsmTaskItem_Type()
)
cfprApFirmwareImageFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmTaskItem.setStatus("current")
_CfprApFirmwareImageFsmTaskSeqId_Type = Gauge32
_CfprApFirmwareImageFsmTaskSeqId_Object = MibTableColumn
cfprApFirmwareImageFsmTaskSeqId = _CfprApFirmwareImageFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 36, 1, 7),
    _CfprApFirmwareImageFsmTaskSeqId_Type()
)
cfprApFirmwareImageFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageFsmTaskSeqId.setStatus("current")
_CfprApFirmwareImageLockTable_Object = MibTable
cfprApFirmwareImageLockTable = _CfprApFirmwareImageLockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 37)
)
if mibBuilder.loadTexts:
    cfprApFirmwareImageLockTable.setStatus("current")
_CfprApFirmwareImageLockEntry_Object = MibTableRow
cfprApFirmwareImageLockEntry = _CfprApFirmwareImageLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 37, 1)
)
cfprApFirmwareImageLockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareImageLockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareImageLockEntry.setStatus("current")
_CfprApFirmwareImageLockInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareImageLockInstanceId_Object = MibTableColumn
cfprApFirmwareImageLockInstanceId = _CfprApFirmwareImageLockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 37, 1, 1),
    _CfprApFirmwareImageLockInstanceId_Type()
)
cfprApFirmwareImageLockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareImageLockInstanceId.setStatus("current")
_CfprApFirmwareImageLockDn_Type = CfprApManagedObjectDn
_CfprApFirmwareImageLockDn_Object = MibTableColumn
cfprApFirmwareImageLockDn = _CfprApFirmwareImageLockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 37, 1, 2),
    _CfprApFirmwareImageLockDn_Type()
)
cfprApFirmwareImageLockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageLockDn.setStatus("current")
_CfprApFirmwareImageLockRn_Type = SnmpAdminString
_CfprApFirmwareImageLockRn_Object = MibTableColumn
cfprApFirmwareImageLockRn = _CfprApFirmwareImageLockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 37, 1, 3),
    _CfprApFirmwareImageLockRn_Type()
)
cfprApFirmwareImageLockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageLockRn.setStatus("current")
_CfprApFirmwareImageLockImageNameDn_Type = SnmpAdminString
_CfprApFirmwareImageLockImageNameDn_Object = MibTableColumn
cfprApFirmwareImageLockImageNameDn = _CfprApFirmwareImageLockImageNameDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 37, 1, 4),
    _CfprApFirmwareImageLockImageNameDn_Type()
)
cfprApFirmwareImageLockImageNameDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageLockImageNameDn.setStatus("current")
_CfprApFirmwareImageLockName_Type = SnmpAdminString
_CfprApFirmwareImageLockName_Object = MibTableColumn
cfprApFirmwareImageLockName = _CfprApFirmwareImageLockName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 37, 1, 5),
    _CfprApFirmwareImageLockName_Type()
)
cfprApFirmwareImageLockName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareImageLockName.setStatus("current")
_CfprApFirmwareInfraTable_Object = MibTable
cfprApFirmwareInfraTable = _CfprApFirmwareInfraTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38)
)
if mibBuilder.loadTexts:
    cfprApFirmwareInfraTable.setStatus("current")
_CfprApFirmwareInfraEntry_Object = MibTableRow
cfprApFirmwareInfraEntry = _CfprApFirmwareInfraEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1)
)
cfprApFirmwareInfraEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareInfraInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareInfraEntry.setStatus("current")
_CfprApFirmwareInfraInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareInfraInstanceId_Object = MibTableColumn
cfprApFirmwareInfraInstanceId = _CfprApFirmwareInfraInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 1),
    _CfprApFirmwareInfraInstanceId_Type()
)
cfprApFirmwareInfraInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraInstanceId.setStatus("current")
_CfprApFirmwareInfraDn_Type = CfprApManagedObjectDn
_CfprApFirmwareInfraDn_Object = MibTableColumn
cfprApFirmwareInfraDn = _CfprApFirmwareInfraDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 2),
    _CfprApFirmwareInfraDn_Type()
)
cfprApFirmwareInfraDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraDn.setStatus("current")
_CfprApFirmwareInfraRn_Type = SnmpAdminString
_CfprApFirmwareInfraRn_Object = MibTableColumn
cfprApFirmwareInfraRn = _CfprApFirmwareInfraRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 3),
    _CfprApFirmwareInfraRn_Type()
)
cfprApFirmwareInfraRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraRn.setStatus("current")
_CfprApFirmwareInfraAdminState_Type = CfprApTrigAdminState
_CfprApFirmwareInfraAdminState_Object = MibTableColumn
cfprApFirmwareInfraAdminState = _CfprApFirmwareInfraAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 4),
    _CfprApFirmwareInfraAdminState_Type()
)
cfprApFirmwareInfraAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraAdminState.setStatus("current")
_CfprApFirmwareInfraAutoDelete_Type = TruthValue
_CfprApFirmwareInfraAutoDelete_Object = MibTableColumn
cfprApFirmwareInfraAutoDelete = _CfprApFirmwareInfraAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 5),
    _CfprApFirmwareInfraAutoDelete_Type()
)
cfprApFirmwareInfraAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraAutoDelete.setStatus("current")
_CfprApFirmwareInfraDescr_Type = SnmpAdminString
_CfprApFirmwareInfraDescr_Object = MibTableColumn
cfprApFirmwareInfraDescr = _CfprApFirmwareInfraDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 6),
    _CfprApFirmwareInfraDescr_Type()
)
cfprApFirmwareInfraDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraDescr.setStatus("current")
_CfprApFirmwareInfraIgnoreCap_Type = TruthValue
_CfprApFirmwareInfraIgnoreCap_Object = MibTableColumn
cfprApFirmwareInfraIgnoreCap = _CfprApFirmwareInfraIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 7),
    _CfprApFirmwareInfraIgnoreCap_Type()
)
cfprApFirmwareInfraIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraIgnoreCap.setStatus("current")
_CfprApFirmwareInfraIntId_Type = SnmpAdminString
_CfprApFirmwareInfraIntId_Object = MibTableColumn
cfprApFirmwareInfraIntId = _CfprApFirmwareInfraIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 8),
    _CfprApFirmwareInfraIntId_Type()
)
cfprApFirmwareInfraIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraIntId.setStatus("current")
_CfprApFirmwareInfraName_Type = SnmpAdminString
_CfprApFirmwareInfraName_Object = MibTableColumn
cfprApFirmwareInfraName = _CfprApFirmwareInfraName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 9),
    _CfprApFirmwareInfraName_Type()
)
cfprApFirmwareInfraName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraName.setStatus("current")
_CfprApFirmwareInfraOperScheduler_Type = SnmpAdminString
_CfprApFirmwareInfraOperScheduler_Object = MibTableColumn
cfprApFirmwareInfraOperScheduler = _CfprApFirmwareInfraOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 10),
    _CfprApFirmwareInfraOperScheduler_Type()
)
cfprApFirmwareInfraOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraOperScheduler.setStatus("current")
_CfprApFirmwareInfraOperState_Type = CfprApTrigTrigOperState
_CfprApFirmwareInfraOperState_Object = MibTableColumn
cfprApFirmwareInfraOperState = _CfprApFirmwareInfraOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 11),
    _CfprApFirmwareInfraOperState_Type()
)
cfprApFirmwareInfraOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraOperState.setStatus("current")
_CfprApFirmwareInfraOperVersion_Type = SnmpAdminString
_CfprApFirmwareInfraOperVersion_Object = MibTableColumn
cfprApFirmwareInfraOperVersion = _CfprApFirmwareInfraOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 12),
    _CfprApFirmwareInfraOperVersion_Type()
)
cfprApFirmwareInfraOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraOperVersion.setStatus("current")
_CfprApFirmwareInfraPolicyLevel_Type = Gauge32
_CfprApFirmwareInfraPolicyLevel_Object = MibTableColumn
cfprApFirmwareInfraPolicyLevel = _CfprApFirmwareInfraPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 13),
    _CfprApFirmwareInfraPolicyLevel_Type()
)
cfprApFirmwareInfraPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPolicyLevel.setStatus("current")
_CfprApFirmwareInfraPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwareInfraPolicyOwner_Object = MibTableColumn
cfprApFirmwareInfraPolicyOwner = _CfprApFirmwareInfraPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 14),
    _CfprApFirmwareInfraPolicyOwner_Type()
)
cfprApFirmwareInfraPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPolicyOwner.setStatus("current")
_CfprApFirmwareInfraScheduler_Type = SnmpAdminString
_CfprApFirmwareInfraScheduler_Object = MibTableColumn
cfprApFirmwareInfraScheduler = _CfprApFirmwareInfraScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 38, 1, 15),
    _CfprApFirmwareInfraScheduler_Type()
)
cfprApFirmwareInfraScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraScheduler.setStatus("current")
_CfprApFirmwareInfraPackTable_Object = MibTable
cfprApFirmwareInfraPackTable = _CfprApFirmwareInfraPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39)
)
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackTable.setStatus("current")
_CfprApFirmwareInfraPackEntry_Object = MibTableRow
cfprApFirmwareInfraPackEntry = _CfprApFirmwareInfraPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1)
)
cfprApFirmwareInfraPackEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareInfraPackInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackEntry.setStatus("current")
_CfprApFirmwareInfraPackInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareInfraPackInstanceId_Object = MibTableColumn
cfprApFirmwareInfraPackInstanceId = _CfprApFirmwareInfraPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 1),
    _CfprApFirmwareInfraPackInstanceId_Type()
)
cfprApFirmwareInfraPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackInstanceId.setStatus("current")
_CfprApFirmwareInfraPackDn_Type = CfprApManagedObjectDn
_CfprApFirmwareInfraPackDn_Object = MibTableColumn
cfprApFirmwareInfraPackDn = _CfprApFirmwareInfraPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 2),
    _CfprApFirmwareInfraPackDn_Type()
)
cfprApFirmwareInfraPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackDn.setStatus("current")
_CfprApFirmwareInfraPackRn_Type = SnmpAdminString
_CfprApFirmwareInfraPackRn_Object = MibTableColumn
cfprApFirmwareInfraPackRn = _CfprApFirmwareInfraPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 3),
    _CfprApFirmwareInfraPackRn_Type()
)
cfprApFirmwareInfraPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackRn.setStatus("current")
_CfprApFirmwareInfraPackDescr_Type = SnmpAdminString
_CfprApFirmwareInfraPackDescr_Object = MibTableColumn
cfprApFirmwareInfraPackDescr = _CfprApFirmwareInfraPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 4),
    _CfprApFirmwareInfraPackDescr_Type()
)
cfprApFirmwareInfraPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackDescr.setStatus("current")
_CfprApFirmwareInfraPackForceDeploy_Type = TruthValue
_CfprApFirmwareInfraPackForceDeploy_Object = MibTableColumn
cfprApFirmwareInfraPackForceDeploy = _CfprApFirmwareInfraPackForceDeploy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 5),
    _CfprApFirmwareInfraPackForceDeploy_Type()
)
cfprApFirmwareInfraPackForceDeploy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackForceDeploy.setStatus("current")
_CfprApFirmwareInfraPackFsmDescr_Type = SnmpAdminString
_CfprApFirmwareInfraPackFsmDescr_Object = MibTableColumn
cfprApFirmwareInfraPackFsmDescr = _CfprApFirmwareInfraPackFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 6),
    _CfprApFirmwareInfraPackFsmDescr_Type()
)
cfprApFirmwareInfraPackFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmDescr.setStatus("current")
_CfprApFirmwareInfraPackFsmFlags_Type = SnmpAdminString
_CfprApFirmwareInfraPackFsmFlags_Object = MibTableColumn
cfprApFirmwareInfraPackFsmFlags = _CfprApFirmwareInfraPackFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 7),
    _CfprApFirmwareInfraPackFsmFlags_Type()
)
cfprApFirmwareInfraPackFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmFlags.setStatus("current")
_CfprApFirmwareInfraPackFsmPrev_Type = SnmpAdminString
_CfprApFirmwareInfraPackFsmPrev_Object = MibTableColumn
cfprApFirmwareInfraPackFsmPrev = _CfprApFirmwareInfraPackFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 8),
    _CfprApFirmwareInfraPackFsmPrev_Type()
)
cfprApFirmwareInfraPackFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmPrev.setStatus("current")
_CfprApFirmwareInfraPackFsmProgr_Type = Gauge32
_CfprApFirmwareInfraPackFsmProgr_Object = MibTableColumn
cfprApFirmwareInfraPackFsmProgr = _CfprApFirmwareInfraPackFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 9),
    _CfprApFirmwareInfraPackFsmProgr_Type()
)
cfprApFirmwareInfraPackFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmProgr.setStatus("current")
_CfprApFirmwareInfraPackFsmRmtInvErrCode_Type = Gauge32
_CfprApFirmwareInfraPackFsmRmtInvErrCode_Object = MibTableColumn
cfprApFirmwareInfraPackFsmRmtInvErrCode = _CfprApFirmwareInfraPackFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 10),
    _CfprApFirmwareInfraPackFsmRmtInvErrCode_Type()
)
cfprApFirmwareInfraPackFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmRmtInvErrCode.setStatus("current")
_CfprApFirmwareInfraPackFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApFirmwareInfraPackFsmRmtInvErrDescr_Object = MibTableColumn
cfprApFirmwareInfraPackFsmRmtInvErrDescr = _CfprApFirmwareInfraPackFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 11),
    _CfprApFirmwareInfraPackFsmRmtInvErrDescr_Type()
)
cfprApFirmwareInfraPackFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmRmtInvErrDescr.setStatus("current")
_CfprApFirmwareInfraPackFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwareInfraPackFsmRmtInvRslt_Object = MibTableColumn
cfprApFirmwareInfraPackFsmRmtInvRslt = _CfprApFirmwareInfraPackFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 12),
    _CfprApFirmwareInfraPackFsmRmtInvRslt_Type()
)
cfprApFirmwareInfraPackFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmRmtInvRslt.setStatus("current")
_CfprApFirmwareInfraPackFsmStageDescr_Type = SnmpAdminString
_CfprApFirmwareInfraPackFsmStageDescr_Object = MibTableColumn
cfprApFirmwareInfraPackFsmStageDescr = _CfprApFirmwareInfraPackFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 13),
    _CfprApFirmwareInfraPackFsmStageDescr_Type()
)
cfprApFirmwareInfraPackFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStageDescr.setStatus("current")
_CfprApFirmwareInfraPackFsmStamp_Type = DateAndTime
_CfprApFirmwareInfraPackFsmStamp_Object = MibTableColumn
cfprApFirmwareInfraPackFsmStamp = _CfprApFirmwareInfraPackFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 14),
    _CfprApFirmwareInfraPackFsmStamp_Type()
)
cfprApFirmwareInfraPackFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStamp.setStatus("current")
_CfprApFirmwareInfraPackFsmStatus_Type = SnmpAdminString
_CfprApFirmwareInfraPackFsmStatus_Object = MibTableColumn
cfprApFirmwareInfraPackFsmStatus = _CfprApFirmwareInfraPackFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 15),
    _CfprApFirmwareInfraPackFsmStatus_Type()
)
cfprApFirmwareInfraPackFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStatus.setStatus("current")
_CfprApFirmwareInfraPackFsmTry_Type = Gauge32
_CfprApFirmwareInfraPackFsmTry_Object = MibTableColumn
cfprApFirmwareInfraPackFsmTry = _CfprApFirmwareInfraPackFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 16),
    _CfprApFirmwareInfraPackFsmTry_Type()
)
cfprApFirmwareInfraPackFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmTry.setStatus("current")
_CfprApFirmwareInfraPackInfraBundleName_Type = SnmpAdminString
_CfprApFirmwareInfraPackInfraBundleName_Object = MibTableColumn
cfprApFirmwareInfraPackInfraBundleName = _CfprApFirmwareInfraPackInfraBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 17),
    _CfprApFirmwareInfraPackInfraBundleName_Type()
)
cfprApFirmwareInfraPackInfraBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackInfraBundleName.setStatus("current")
_CfprApFirmwareInfraPackInfraBundleVersion_Type = SnmpAdminString
_CfprApFirmwareInfraPackInfraBundleVersion_Object = MibTableColumn
cfprApFirmwareInfraPackInfraBundleVersion = _CfprApFirmwareInfraPackInfraBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 18),
    _CfprApFirmwareInfraPackInfraBundleVersion_Type()
)
cfprApFirmwareInfraPackInfraBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackInfraBundleVersion.setStatus("current")
_CfprApFirmwareInfraPackIntId_Type = SnmpAdminString
_CfprApFirmwareInfraPackIntId_Object = MibTableColumn
cfprApFirmwareInfraPackIntId = _CfprApFirmwareInfraPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 19),
    _CfprApFirmwareInfraPackIntId_Type()
)
cfprApFirmwareInfraPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackIntId.setStatus("current")
_CfprApFirmwareInfraPackMode_Type = CfprApFirmwarePackMode
_CfprApFirmwareInfraPackMode_Object = MibTableColumn
cfprApFirmwareInfraPackMode = _CfprApFirmwareInfraPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 20),
    _CfprApFirmwareInfraPackMode_Type()
)
cfprApFirmwareInfraPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackMode.setStatus("current")
_CfprApFirmwareInfraPackName_Type = SnmpAdminString
_CfprApFirmwareInfraPackName_Object = MibTableColumn
cfprApFirmwareInfraPackName = _CfprApFirmwareInfraPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 21),
    _CfprApFirmwareInfraPackName_Type()
)
cfprApFirmwareInfraPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackName.setStatus("current")
_CfprApFirmwareInfraPackPolicyLevel_Type = Gauge32
_CfprApFirmwareInfraPackPolicyLevel_Object = MibTableColumn
cfprApFirmwareInfraPackPolicyLevel = _CfprApFirmwareInfraPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 22),
    _CfprApFirmwareInfraPackPolicyLevel_Type()
)
cfprApFirmwareInfraPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackPolicyLevel.setStatus("current")
_CfprApFirmwareInfraPackPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwareInfraPackPolicyOwner_Object = MibTableColumn
cfprApFirmwareInfraPackPolicyOwner = _CfprApFirmwareInfraPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 23),
    _CfprApFirmwareInfraPackPolicyOwner_Type()
)
cfprApFirmwareInfraPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackPolicyOwner.setStatus("current")
_CfprApFirmwareInfraPackPreviousBundleVersion_Type = SnmpAdminString
_CfprApFirmwareInfraPackPreviousBundleVersion_Object = MibTableColumn
cfprApFirmwareInfraPackPreviousBundleVersion = _CfprApFirmwareInfraPackPreviousBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 24),
    _CfprApFirmwareInfraPackPreviousBundleVersion_Type()
)
cfprApFirmwareInfraPackPreviousBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackPreviousBundleVersion.setStatus("current")
_CfprApFirmwareInfraPackStageSize_Type = Gauge32
_CfprApFirmwareInfraPackStageSize_Object = MibTableColumn
cfprApFirmwareInfraPackStageSize = _CfprApFirmwareInfraPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 25),
    _CfprApFirmwareInfraPackStageSize_Type()
)
cfprApFirmwareInfraPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackStageSize.setStatus("current")
_CfprApFirmwareInfraPackUpdateTrigger_Type = DateAndTime
_CfprApFirmwareInfraPackUpdateTrigger_Object = MibTableColumn
cfprApFirmwareInfraPackUpdateTrigger = _CfprApFirmwareInfraPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 39, 1, 26),
    _CfprApFirmwareInfraPackUpdateTrigger_Type()
)
cfprApFirmwareInfraPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackUpdateTrigger.setStatus("current")
_CfprApFirmwareInfraPackFsmTable_Object = MibTable
cfprApFirmwareInfraPackFsmTable = _CfprApFirmwareInfraPackFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40)
)
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmTable.setStatus("current")
_CfprApFirmwareInfraPackFsmEntry_Object = MibTableRow
cfprApFirmwareInfraPackFsmEntry = _CfprApFirmwareInfraPackFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40, 1)
)
cfprApFirmwareInfraPackFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareInfraPackFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmEntry.setStatus("current")
_CfprApFirmwareInfraPackFsmInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareInfraPackFsmInstanceId_Object = MibTableColumn
cfprApFirmwareInfraPackFsmInstanceId = _CfprApFirmwareInfraPackFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40, 1, 1),
    _CfprApFirmwareInfraPackFsmInstanceId_Type()
)
cfprApFirmwareInfraPackFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmInstanceId.setStatus("current")
_CfprApFirmwareInfraPackFsmDn_Type = CfprApManagedObjectDn
_CfprApFirmwareInfraPackFsmDn_Object = MibTableColumn
cfprApFirmwareInfraPackFsmDn = _CfprApFirmwareInfraPackFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40, 1, 2),
    _CfprApFirmwareInfraPackFsmDn_Type()
)
cfprApFirmwareInfraPackFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmDn.setStatus("current")
_CfprApFirmwareInfraPackFsmRn_Type = SnmpAdminString
_CfprApFirmwareInfraPackFsmRn_Object = MibTableColumn
cfprApFirmwareInfraPackFsmRn = _CfprApFirmwareInfraPackFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40, 1, 3),
    _CfprApFirmwareInfraPackFsmRn_Type()
)
cfprApFirmwareInfraPackFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmRn.setStatus("current")
_CfprApFirmwareInfraPackFsmCompletionTime_Type = DateAndTime
_CfprApFirmwareInfraPackFsmCompletionTime_Object = MibTableColumn
cfprApFirmwareInfraPackFsmCompletionTime = _CfprApFirmwareInfraPackFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40, 1, 4),
    _CfprApFirmwareInfraPackFsmCompletionTime_Type()
)
cfprApFirmwareInfraPackFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmCompletionTime.setStatus("current")
_CfprApFirmwareInfraPackFsmCurrentFsm_Type = CfprApFirmwareInfraPackFsmCurrentFsm
_CfprApFirmwareInfraPackFsmCurrentFsm_Object = MibTableColumn
cfprApFirmwareInfraPackFsmCurrentFsm = _CfprApFirmwareInfraPackFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40, 1, 5),
    _CfprApFirmwareInfraPackFsmCurrentFsm_Type()
)
cfprApFirmwareInfraPackFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmCurrentFsm.setStatus("current")
_CfprApFirmwareInfraPackFsmDescrData_Type = SnmpAdminString
_CfprApFirmwareInfraPackFsmDescrData_Object = MibTableColumn
cfprApFirmwareInfraPackFsmDescrData = _CfprApFirmwareInfraPackFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40, 1, 6),
    _CfprApFirmwareInfraPackFsmDescrData_Type()
)
cfprApFirmwareInfraPackFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmDescrData.setStatus("current")
_CfprApFirmwareInfraPackFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwareInfraPackFsmFsmStatus_Object = MibTableColumn
cfprApFirmwareInfraPackFsmFsmStatus = _CfprApFirmwareInfraPackFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40, 1, 7),
    _CfprApFirmwareInfraPackFsmFsmStatus_Type()
)
cfprApFirmwareInfraPackFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmFsmStatus.setStatus("current")
_CfprApFirmwareInfraPackFsmProgress_Type = Gauge32
_CfprApFirmwareInfraPackFsmProgress_Object = MibTableColumn
cfprApFirmwareInfraPackFsmProgress = _CfprApFirmwareInfraPackFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40, 1, 8),
    _CfprApFirmwareInfraPackFsmProgress_Type()
)
cfprApFirmwareInfraPackFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmProgress.setStatus("current")
_CfprApFirmwareInfraPackFsmRmtErrCode_Type = Gauge32
_CfprApFirmwareInfraPackFsmRmtErrCode_Object = MibTableColumn
cfprApFirmwareInfraPackFsmRmtErrCode = _CfprApFirmwareInfraPackFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40, 1, 9),
    _CfprApFirmwareInfraPackFsmRmtErrCode_Type()
)
cfprApFirmwareInfraPackFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmRmtErrCode.setStatus("current")
_CfprApFirmwareInfraPackFsmRmtErrDescr_Type = SnmpAdminString
_CfprApFirmwareInfraPackFsmRmtErrDescr_Object = MibTableColumn
cfprApFirmwareInfraPackFsmRmtErrDescr = _CfprApFirmwareInfraPackFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40, 1, 10),
    _CfprApFirmwareInfraPackFsmRmtErrDescr_Type()
)
cfprApFirmwareInfraPackFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmRmtErrDescr.setStatus("current")
_CfprApFirmwareInfraPackFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwareInfraPackFsmRmtRslt_Object = MibTableColumn
cfprApFirmwareInfraPackFsmRmtRslt = _CfprApFirmwareInfraPackFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 40, 1, 11),
    _CfprApFirmwareInfraPackFsmRmtRslt_Type()
)
cfprApFirmwareInfraPackFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmRmtRslt.setStatus("current")
_CfprApFirmwareInfraPackFsmStageTable_Object = MibTable
cfprApFirmwareInfraPackFsmStageTable = _CfprApFirmwareInfraPackFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 41)
)
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStageTable.setStatus("current")
_CfprApFirmwareInfraPackFsmStageEntry_Object = MibTableRow
cfprApFirmwareInfraPackFsmStageEntry = _CfprApFirmwareInfraPackFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 41, 1)
)
cfprApFirmwareInfraPackFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareInfraPackFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStageEntry.setStatus("current")
_CfprApFirmwareInfraPackFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareInfraPackFsmStageInstanceId_Object = MibTableColumn
cfprApFirmwareInfraPackFsmStageInstanceId = _CfprApFirmwareInfraPackFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 41, 1, 1),
    _CfprApFirmwareInfraPackFsmStageInstanceId_Type()
)
cfprApFirmwareInfraPackFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStageInstanceId.setStatus("current")
_CfprApFirmwareInfraPackFsmStageDn_Type = CfprApManagedObjectDn
_CfprApFirmwareInfraPackFsmStageDn_Object = MibTableColumn
cfprApFirmwareInfraPackFsmStageDn = _CfprApFirmwareInfraPackFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 41, 1, 2),
    _CfprApFirmwareInfraPackFsmStageDn_Type()
)
cfprApFirmwareInfraPackFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStageDn.setStatus("current")
_CfprApFirmwareInfraPackFsmStageRn_Type = SnmpAdminString
_CfprApFirmwareInfraPackFsmStageRn_Object = MibTableColumn
cfprApFirmwareInfraPackFsmStageRn = _CfprApFirmwareInfraPackFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 41, 1, 3),
    _CfprApFirmwareInfraPackFsmStageRn_Type()
)
cfprApFirmwareInfraPackFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStageRn.setStatus("current")
_CfprApFirmwareInfraPackFsmStageDescrData_Type = SnmpAdminString
_CfprApFirmwareInfraPackFsmStageDescrData_Object = MibTableColumn
cfprApFirmwareInfraPackFsmStageDescrData = _CfprApFirmwareInfraPackFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 41, 1, 4),
    _CfprApFirmwareInfraPackFsmStageDescrData_Type()
)
cfprApFirmwareInfraPackFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStageDescrData.setStatus("current")
_CfprApFirmwareInfraPackFsmStageLastUpdateTime_Type = DateAndTime
_CfprApFirmwareInfraPackFsmStageLastUpdateTime_Object = MibTableColumn
cfprApFirmwareInfraPackFsmStageLastUpdateTime = _CfprApFirmwareInfraPackFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 41, 1, 5),
    _CfprApFirmwareInfraPackFsmStageLastUpdateTime_Type()
)
cfprApFirmwareInfraPackFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStageLastUpdateTime.setStatus("current")
_CfprApFirmwareInfraPackFsmStageName_Type = CfprApFirmwareInfraPackFsmStageName
_CfprApFirmwareInfraPackFsmStageName_Object = MibTableColumn
cfprApFirmwareInfraPackFsmStageName = _CfprApFirmwareInfraPackFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 41, 1, 6),
    _CfprApFirmwareInfraPackFsmStageName_Type()
)
cfprApFirmwareInfraPackFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStageName.setStatus("current")
_CfprApFirmwareInfraPackFsmStageOrder_Type = Gauge32
_CfprApFirmwareInfraPackFsmStageOrder_Object = MibTableColumn
cfprApFirmwareInfraPackFsmStageOrder = _CfprApFirmwareInfraPackFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 41, 1, 7),
    _CfprApFirmwareInfraPackFsmStageOrder_Type()
)
cfprApFirmwareInfraPackFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStageOrder.setStatus("current")
_CfprApFirmwareInfraPackFsmStageRetry_Type = Gauge32
_CfprApFirmwareInfraPackFsmStageRetry_Object = MibTableColumn
cfprApFirmwareInfraPackFsmStageRetry = _CfprApFirmwareInfraPackFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 41, 1, 8),
    _CfprApFirmwareInfraPackFsmStageRetry_Type()
)
cfprApFirmwareInfraPackFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStageRetry.setStatus("current")
_CfprApFirmwareInfraPackFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwareInfraPackFsmStageStageStatus_Object = MibTableColumn
cfprApFirmwareInfraPackFsmStageStageStatus = _CfprApFirmwareInfraPackFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 41, 1, 9),
    _CfprApFirmwareInfraPackFsmStageStageStatus_Type()
)
cfprApFirmwareInfraPackFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmStageStageStatus.setStatus("current")
_CfprApFirmwareInfraPackFsmTaskTable_Object = MibTable
cfprApFirmwareInfraPackFsmTaskTable = _CfprApFirmwareInfraPackFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 42)
)
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmTaskTable.setStatus("current")
_CfprApFirmwareInfraPackFsmTaskEntry_Object = MibTableRow
cfprApFirmwareInfraPackFsmTaskEntry = _CfprApFirmwareInfraPackFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 42, 1)
)
cfprApFirmwareInfraPackFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareInfraPackFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmTaskEntry.setStatus("current")
_CfprApFirmwareInfraPackFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareInfraPackFsmTaskInstanceId_Object = MibTableColumn
cfprApFirmwareInfraPackFsmTaskInstanceId = _CfprApFirmwareInfraPackFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 42, 1, 1),
    _CfprApFirmwareInfraPackFsmTaskInstanceId_Type()
)
cfprApFirmwareInfraPackFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmTaskInstanceId.setStatus("current")
_CfprApFirmwareInfraPackFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApFirmwareInfraPackFsmTaskDn_Object = MibTableColumn
cfprApFirmwareInfraPackFsmTaskDn = _CfprApFirmwareInfraPackFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 42, 1, 2),
    _CfprApFirmwareInfraPackFsmTaskDn_Type()
)
cfprApFirmwareInfraPackFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmTaskDn.setStatus("current")
_CfprApFirmwareInfraPackFsmTaskRn_Type = SnmpAdminString
_CfprApFirmwareInfraPackFsmTaskRn_Object = MibTableColumn
cfprApFirmwareInfraPackFsmTaskRn = _CfprApFirmwareInfraPackFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 42, 1, 3),
    _CfprApFirmwareInfraPackFsmTaskRn_Type()
)
cfprApFirmwareInfraPackFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmTaskRn.setStatus("current")
_CfprApFirmwareInfraPackFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApFirmwareInfraPackFsmTaskCompletion_Object = MibTableColumn
cfprApFirmwareInfraPackFsmTaskCompletion = _CfprApFirmwareInfraPackFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 42, 1, 4),
    _CfprApFirmwareInfraPackFsmTaskCompletion_Type()
)
cfprApFirmwareInfraPackFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmTaskCompletion.setStatus("current")
_CfprApFirmwareInfraPackFsmTaskFlags_Type = CfprApFirmwareInfraPackFsmTaskFlags
_CfprApFirmwareInfraPackFsmTaskFlags_Object = MibTableColumn
cfprApFirmwareInfraPackFsmTaskFlags = _CfprApFirmwareInfraPackFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 42, 1, 5),
    _CfprApFirmwareInfraPackFsmTaskFlags_Type()
)
cfprApFirmwareInfraPackFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmTaskFlags.setStatus("current")
_CfprApFirmwareInfraPackFsmTaskItem_Type = CfprApFirmwareInfraPackFsmTaskItem
_CfprApFirmwareInfraPackFsmTaskItem_Object = MibTableColumn
cfprApFirmwareInfraPackFsmTaskItem = _CfprApFirmwareInfraPackFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 42, 1, 6),
    _CfprApFirmwareInfraPackFsmTaskItem_Type()
)
cfprApFirmwareInfraPackFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmTaskItem.setStatus("current")
_CfprApFirmwareInfraPackFsmTaskSeqId_Type = Gauge32
_CfprApFirmwareInfraPackFsmTaskSeqId_Object = MibTableColumn
cfprApFirmwareInfraPackFsmTaskSeqId = _CfprApFirmwareInfraPackFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 42, 1, 7),
    _CfprApFirmwareInfraPackFsmTaskSeqId_Type()
)
cfprApFirmwareInfraPackFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInfraPackFsmTaskSeqId.setStatus("current")
_CfprApFirmwareInstallImpactTable_Object = MibTable
cfprApFirmwareInstallImpactTable = _CfprApFirmwareInstallImpactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 43)
)
if mibBuilder.loadTexts:
    cfprApFirmwareInstallImpactTable.setStatus("current")
_CfprApFirmwareInstallImpactEntry_Object = MibTableRow
cfprApFirmwareInstallImpactEntry = _CfprApFirmwareInstallImpactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 43, 1)
)
cfprApFirmwareInstallImpactEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareInstallImpactInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareInstallImpactEntry.setStatus("current")
_CfprApFirmwareInstallImpactInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareInstallImpactInstanceId_Object = MibTableColumn
cfprApFirmwareInstallImpactInstanceId = _CfprApFirmwareInstallImpactInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 43, 1, 1),
    _CfprApFirmwareInstallImpactInstanceId_Type()
)
cfprApFirmwareInstallImpactInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallImpactInstanceId.setStatus("current")
_CfprApFirmwareInstallImpactDn_Type = CfprApManagedObjectDn
_CfprApFirmwareInstallImpactDn_Object = MibTableColumn
cfprApFirmwareInstallImpactDn = _CfprApFirmwareInstallImpactDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 43, 1, 2),
    _CfprApFirmwareInstallImpactDn_Type()
)
cfprApFirmwareInstallImpactDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallImpactDn.setStatus("current")
_CfprApFirmwareInstallImpactRn_Type = SnmpAdminString
_CfprApFirmwareInstallImpactRn_Object = MibTableColumn
cfprApFirmwareInstallImpactRn = _CfprApFirmwareInstallImpactRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 43, 1, 3),
    _CfprApFirmwareInstallImpactRn_Type()
)
cfprApFirmwareInstallImpactRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallImpactRn.setStatus("current")
_CfprApFirmwareInstallImpactDescr_Type = SnmpAdminString
_CfprApFirmwareInstallImpactDescr_Object = MibTableColumn
cfprApFirmwareInstallImpactDescr = _CfprApFirmwareInstallImpactDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 43, 1, 4),
    _CfprApFirmwareInstallImpactDescr_Type()
)
cfprApFirmwareInstallImpactDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallImpactDescr.setStatus("current")
_CfprApFirmwareInstallImpactKeyDn_Type = SnmpAdminString
_CfprApFirmwareInstallImpactKeyDn_Object = MibTableColumn
cfprApFirmwareInstallImpactKeyDn = _CfprApFirmwareInstallImpactKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 43, 1, 5),
    _CfprApFirmwareInstallImpactKeyDn_Type()
)
cfprApFirmwareInstallImpactKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallImpactKeyDn.setStatus("current")
_CfprApFirmwareInstallImpactMaintPolicyDn_Type = SnmpAdminString
_CfprApFirmwareInstallImpactMaintPolicyDn_Object = MibTableColumn
cfprApFirmwareInstallImpactMaintPolicyDn = _CfprApFirmwareInstallImpactMaintPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 43, 1, 6),
    _CfprApFirmwareInstallImpactMaintPolicyDn_Type()
)
cfprApFirmwareInstallImpactMaintPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallImpactMaintPolicyDn.setStatus("current")
_CfprApFirmwareInstallImpactRebootPolicy_Type = SnmpAdminString
_CfprApFirmwareInstallImpactRebootPolicy_Object = MibTableColumn
cfprApFirmwareInstallImpactRebootPolicy = _CfprApFirmwareInstallImpactRebootPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 43, 1, 7),
    _CfprApFirmwareInstallImpactRebootPolicy_Type()
)
cfprApFirmwareInstallImpactRebootPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallImpactRebootPolicy.setStatus("current")
_CfprApFirmwareInstallImpactSubject_Type = CfprApFirmwareEquipmentType
_CfprApFirmwareInstallImpactSubject_Object = MibTableColumn
cfprApFirmwareInstallImpactSubject = _CfprApFirmwareInstallImpactSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 43, 1, 8),
    _CfprApFirmwareInstallImpactSubject_Type()
)
cfprApFirmwareInstallImpactSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallImpactSubject.setStatus("current")
_CfprApFirmwareInstallImpactType_Type = CfprApFirmwareImpactType
_CfprApFirmwareInstallImpactType_Object = MibTableColumn
cfprApFirmwareInstallImpactType = _CfprApFirmwareInstallImpactType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 43, 1, 9),
    _CfprApFirmwareInstallImpactType_Type()
)
cfprApFirmwareInstallImpactType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallImpactType.setStatus("current")
_CfprApFirmwareInstallableTable_Object = MibTable
cfprApFirmwareInstallableTable = _CfprApFirmwareInstallableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44)
)
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableTable.setStatus("current")
_CfprApFirmwareInstallableEntry_Object = MibTableRow
cfprApFirmwareInstallableEntry = _CfprApFirmwareInstallableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1)
)
cfprApFirmwareInstallableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareInstallableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableEntry.setStatus("current")
_CfprApFirmwareInstallableInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareInstallableInstanceId_Object = MibTableColumn
cfprApFirmwareInstallableInstanceId = _CfprApFirmwareInstallableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 1),
    _CfprApFirmwareInstallableInstanceId_Type()
)
cfprApFirmwareInstallableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableInstanceId.setStatus("current")
_CfprApFirmwareInstallableDn_Type = CfprApManagedObjectDn
_CfprApFirmwareInstallableDn_Object = MibTableColumn
cfprApFirmwareInstallableDn = _CfprApFirmwareInstallableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 2),
    _CfprApFirmwareInstallableDn_Type()
)
cfprApFirmwareInstallableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableDn.setStatus("current")
_CfprApFirmwareInstallableRn_Type = SnmpAdminString
_CfprApFirmwareInstallableRn_Object = MibTableColumn
cfprApFirmwareInstallableRn = _CfprApFirmwareInstallableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 3),
    _CfprApFirmwareInstallableRn_Type()
)
cfprApFirmwareInstallableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableRn.setStatus("current")
_CfprApFirmwareInstallableChecksum_Type = SnmpAdminString
_CfprApFirmwareInstallableChecksum_Object = MibTableColumn
cfprApFirmwareInstallableChecksum = _CfprApFirmwareInstallableChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 4),
    _CfprApFirmwareInstallableChecksum_Type()
)
cfprApFirmwareInstallableChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableChecksum.setStatus("current")
_CfprApFirmwareInstallableInProgress_Type = Gauge32
_CfprApFirmwareInstallableInProgress_Object = MibTableColumn
cfprApFirmwareInstallableInProgress = _CfprApFirmwareInstallableInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 5),
    _CfprApFirmwareInstallableInProgress_Type()
)
cfprApFirmwareInstallableInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableInProgress.setStatus("current")
_CfprApFirmwareInstallableIsoname_Type = SnmpAdminString
_CfprApFirmwareInstallableIsoname_Object = MibTableColumn
cfprApFirmwareInstallableIsoname = _CfprApFirmwareInstallableIsoname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 6),
    _CfprApFirmwareInstallableIsoname_Type()
)
cfprApFirmwareInstallableIsoname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableIsoname.setStatus("current")
_CfprApFirmwareInstallableLocation_Type = SnmpAdminString
_CfprApFirmwareInstallableLocation_Object = MibTableColumn
cfprApFirmwareInstallableLocation = _CfprApFirmwareInstallableLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 7),
    _CfprApFirmwareInstallableLocation_Type()
)
cfprApFirmwareInstallableLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableLocation.setStatus("current")
_CfprApFirmwareInstallableModel_Type = SnmpAdminString
_CfprApFirmwareInstallableModel_Object = MibTableColumn
cfprApFirmwareInstallableModel = _CfprApFirmwareInstallableModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 8),
    _CfprApFirmwareInstallableModel_Type()
)
cfprApFirmwareInstallableModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableModel.setStatus("current")
_CfprApFirmwareInstallableName_Type = SnmpAdminString
_CfprApFirmwareInstallableName_Object = MibTableColumn
cfprApFirmwareInstallableName = _CfprApFirmwareInstallableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 9),
    _CfprApFirmwareInstallableName_Type()
)
cfprApFirmwareInstallableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableName.setStatus("current")
_CfprApFirmwareInstallableSize_Type = Gauge32
_CfprApFirmwareInstallableSize_Object = MibTableColumn
cfprApFirmwareInstallableSize = _CfprApFirmwareInstallableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 10),
    _CfprApFirmwareInstallableSize_Type()
)
cfprApFirmwareInstallableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableSize.setStatus("current")
_CfprApFirmwareInstallableType_Type = CfprApFirmwareType
_CfprApFirmwareInstallableType_Object = MibTableColumn
cfprApFirmwareInstallableType = _CfprApFirmwareInstallableType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 11),
    _CfprApFirmwareInstallableType_Type()
)
cfprApFirmwareInstallableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableType.setStatus("current")
_CfprApFirmwareInstallableVendor_Type = SnmpAdminString
_CfprApFirmwareInstallableVendor_Object = MibTableColumn
cfprApFirmwareInstallableVendor = _CfprApFirmwareInstallableVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 12),
    _CfprApFirmwareInstallableVendor_Type()
)
cfprApFirmwareInstallableVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableVendor.setStatus("current")
_CfprApFirmwareInstallableVersion_Type = SnmpAdminString
_CfprApFirmwareInstallableVersion_Object = MibTableColumn
cfprApFirmwareInstallableVersion = _CfprApFirmwareInstallableVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 44, 1, 13),
    _CfprApFirmwareInstallableVersion_Type()
)
cfprApFirmwareInstallableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareInstallableVersion.setStatus("current")
_CfprApFirmwarePackItemTable_Object = MibTable
cfprApFirmwarePackItemTable = _CfprApFirmwarePackItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 45)
)
if mibBuilder.loadTexts:
    cfprApFirmwarePackItemTable.setStatus("current")
_CfprApFirmwarePackItemEntry_Object = MibTableRow
cfprApFirmwarePackItemEntry = _CfprApFirmwarePackItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 45, 1)
)
cfprApFirmwarePackItemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwarePackItemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwarePackItemEntry.setStatus("current")
_CfprApFirmwarePackItemInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwarePackItemInstanceId_Object = MibTableColumn
cfprApFirmwarePackItemInstanceId = _CfprApFirmwarePackItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 45, 1, 1),
    _CfprApFirmwarePackItemInstanceId_Type()
)
cfprApFirmwarePackItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwarePackItemInstanceId.setStatus("current")
_CfprApFirmwarePackItemDn_Type = CfprApManagedObjectDn
_CfprApFirmwarePackItemDn_Object = MibTableColumn
cfprApFirmwarePackItemDn = _CfprApFirmwarePackItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 45, 1, 2),
    _CfprApFirmwarePackItemDn_Type()
)
cfprApFirmwarePackItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePackItemDn.setStatus("current")
_CfprApFirmwarePackItemRn_Type = SnmpAdminString
_CfprApFirmwarePackItemRn_Object = MibTableColumn
cfprApFirmwarePackItemRn = _CfprApFirmwarePackItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 45, 1, 3),
    _CfprApFirmwarePackItemRn_Type()
)
cfprApFirmwarePackItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePackItemRn.setStatus("current")
_CfprApFirmwarePackItemHwModel_Type = SnmpAdminString
_CfprApFirmwarePackItemHwModel_Object = MibTableColumn
cfprApFirmwarePackItemHwModel = _CfprApFirmwarePackItemHwModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 45, 1, 4),
    _CfprApFirmwarePackItemHwModel_Type()
)
cfprApFirmwarePackItemHwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePackItemHwModel.setStatus("current")
_CfprApFirmwarePackItemHwVendor_Type = SnmpAdminString
_CfprApFirmwarePackItemHwVendor_Object = MibTableColumn
cfprApFirmwarePackItemHwVendor = _CfprApFirmwarePackItemHwVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 45, 1, 5),
    _CfprApFirmwarePackItemHwVendor_Type()
)
cfprApFirmwarePackItemHwVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePackItemHwVendor.setStatus("current")
_CfprApFirmwarePackItemPresence_Type = CfprApFirmwarePackItemPresence
_CfprApFirmwarePackItemPresence_Object = MibTableColumn
cfprApFirmwarePackItemPresence = _CfprApFirmwarePackItemPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 45, 1, 6),
    _CfprApFirmwarePackItemPresence_Type()
)
cfprApFirmwarePackItemPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePackItemPresence.setStatus("current")
_CfprApFirmwarePackItemType_Type = CfprApFirmwareItemType
_CfprApFirmwarePackItemType_Object = MibTableColumn
cfprApFirmwarePackItemType = _CfprApFirmwarePackItemType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 45, 1, 7),
    _CfprApFirmwarePackItemType_Type()
)
cfprApFirmwarePackItemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePackItemType.setStatus("current")
_CfprApFirmwarePackItemVersion_Type = SnmpAdminString
_CfprApFirmwarePackItemVersion_Object = MibTableColumn
cfprApFirmwarePackItemVersion = _CfprApFirmwarePackItemVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 45, 1, 8),
    _CfprApFirmwarePackItemVersion_Type()
)
cfprApFirmwarePackItemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePackItemVersion.setStatus("current")
_CfprApFirmwarePlatformTable_Object = MibTable
cfprApFirmwarePlatformTable = _CfprApFirmwarePlatformTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46)
)
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformTable.setStatus("current")
_CfprApFirmwarePlatformEntry_Object = MibTableRow
cfprApFirmwarePlatformEntry = _CfprApFirmwarePlatformEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1)
)
cfprApFirmwarePlatformEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwarePlatformInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformEntry.setStatus("current")
_CfprApFirmwarePlatformInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwarePlatformInstanceId_Object = MibTableColumn
cfprApFirmwarePlatformInstanceId = _CfprApFirmwarePlatformInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 1),
    _CfprApFirmwarePlatformInstanceId_Type()
)
cfprApFirmwarePlatformInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformInstanceId.setStatus("current")
_CfprApFirmwarePlatformDn_Type = CfprApManagedObjectDn
_CfprApFirmwarePlatformDn_Object = MibTableColumn
cfprApFirmwarePlatformDn = _CfprApFirmwarePlatformDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 2),
    _CfprApFirmwarePlatformDn_Type()
)
cfprApFirmwarePlatformDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformDn.setStatus("current")
_CfprApFirmwarePlatformRn_Type = SnmpAdminString
_CfprApFirmwarePlatformRn_Object = MibTableColumn
cfprApFirmwarePlatformRn = _CfprApFirmwarePlatformRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 3),
    _CfprApFirmwarePlatformRn_Type()
)
cfprApFirmwarePlatformRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformRn.setStatus("current")
_CfprApFirmwarePlatformAdminState_Type = CfprApTrigAdminState
_CfprApFirmwarePlatformAdminState_Object = MibTableColumn
cfprApFirmwarePlatformAdminState = _CfprApFirmwarePlatformAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 4),
    _CfprApFirmwarePlatformAdminState_Type()
)
cfprApFirmwarePlatformAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformAdminState.setStatus("current")
_CfprApFirmwarePlatformAutoDelete_Type = TruthValue
_CfprApFirmwarePlatformAutoDelete_Object = MibTableColumn
cfprApFirmwarePlatformAutoDelete = _CfprApFirmwarePlatformAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 5),
    _CfprApFirmwarePlatformAutoDelete_Type()
)
cfprApFirmwarePlatformAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformAutoDelete.setStatus("current")
_CfprApFirmwarePlatformDescr_Type = SnmpAdminString
_CfprApFirmwarePlatformDescr_Object = MibTableColumn
cfprApFirmwarePlatformDescr = _CfprApFirmwarePlatformDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 6),
    _CfprApFirmwarePlatformDescr_Type()
)
cfprApFirmwarePlatformDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformDescr.setStatus("current")
_CfprApFirmwarePlatformIgnoreCap_Type = TruthValue
_CfprApFirmwarePlatformIgnoreCap_Object = MibTableColumn
cfprApFirmwarePlatformIgnoreCap = _CfprApFirmwarePlatformIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 7),
    _CfprApFirmwarePlatformIgnoreCap_Type()
)
cfprApFirmwarePlatformIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformIgnoreCap.setStatus("current")
_CfprApFirmwarePlatformIntId_Type = SnmpAdminString
_CfprApFirmwarePlatformIntId_Object = MibTableColumn
cfprApFirmwarePlatformIntId = _CfprApFirmwarePlatformIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 8),
    _CfprApFirmwarePlatformIntId_Type()
)
cfprApFirmwarePlatformIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformIntId.setStatus("current")
_CfprApFirmwarePlatformName_Type = SnmpAdminString
_CfprApFirmwarePlatformName_Object = MibTableColumn
cfprApFirmwarePlatformName = _CfprApFirmwarePlatformName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 9),
    _CfprApFirmwarePlatformName_Type()
)
cfprApFirmwarePlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformName.setStatus("current")
_CfprApFirmwarePlatformOperScheduler_Type = SnmpAdminString
_CfprApFirmwarePlatformOperScheduler_Object = MibTableColumn
cfprApFirmwarePlatformOperScheduler = _CfprApFirmwarePlatformOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 10),
    _CfprApFirmwarePlatformOperScheduler_Type()
)
cfprApFirmwarePlatformOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformOperScheduler.setStatus("current")
_CfprApFirmwarePlatformOperState_Type = CfprApTrigTrigOperState
_CfprApFirmwarePlatformOperState_Object = MibTableColumn
cfprApFirmwarePlatformOperState = _CfprApFirmwarePlatformOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 11),
    _CfprApFirmwarePlatformOperState_Type()
)
cfprApFirmwarePlatformOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformOperState.setStatus("current")
_CfprApFirmwarePlatformOperVersion_Type = SnmpAdminString
_CfprApFirmwarePlatformOperVersion_Object = MibTableColumn
cfprApFirmwarePlatformOperVersion = _CfprApFirmwarePlatformOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 12),
    _CfprApFirmwarePlatformOperVersion_Type()
)
cfprApFirmwarePlatformOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformOperVersion.setStatus("current")
_CfprApFirmwarePlatformPolicyLevel_Type = Gauge32
_CfprApFirmwarePlatformPolicyLevel_Object = MibTableColumn
cfprApFirmwarePlatformPolicyLevel = _CfprApFirmwarePlatformPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 13),
    _CfprApFirmwarePlatformPolicyLevel_Type()
)
cfprApFirmwarePlatformPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPolicyLevel.setStatus("current")
_CfprApFirmwarePlatformPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwarePlatformPolicyOwner_Object = MibTableColumn
cfprApFirmwarePlatformPolicyOwner = _CfprApFirmwarePlatformPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 14),
    _CfprApFirmwarePlatformPolicyOwner_Type()
)
cfprApFirmwarePlatformPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPolicyOwner.setStatus("current")
_CfprApFirmwarePlatformScheduler_Type = SnmpAdminString
_CfprApFirmwarePlatformScheduler_Object = MibTableColumn
cfprApFirmwarePlatformScheduler = _CfprApFirmwarePlatformScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 46, 1, 15),
    _CfprApFirmwarePlatformScheduler_Type()
)
cfprApFirmwarePlatformScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformScheduler.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderTable_Object = MibTable
cfprApFirmwarePlatformBundleTypeCapProviderTable = _CfprApFirmwarePlatformBundleTypeCapProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47)
)
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderTable.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderEntry_Object = MibTableRow
cfprApFirmwarePlatformBundleTypeCapProviderEntry = _CfprApFirmwarePlatformBundleTypeCapProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1)
)
cfprApFirmwarePlatformBundleTypeCapProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwarePlatformBundleTypeCapProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderEntry.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwarePlatformBundleTypeCapProviderInstanceId_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderInstanceId = _CfprApFirmwarePlatformBundleTypeCapProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 1),
    _CfprApFirmwarePlatformBundleTypeCapProviderInstanceId_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderInstanceId.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderDn_Type = CfprApManagedObjectDn
_CfprApFirmwarePlatformBundleTypeCapProviderDn_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderDn = _CfprApFirmwarePlatformBundleTypeCapProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 2),
    _CfprApFirmwarePlatformBundleTypeCapProviderDn_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderDn.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderRn_Type = SnmpAdminString
_CfprApFirmwarePlatformBundleTypeCapProviderRn_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderRn = _CfprApFirmwarePlatformBundleTypeCapProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 3),
    _CfprApFirmwarePlatformBundleTypeCapProviderRn_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderRn.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderDeleted_Type = TruthValue
_CfprApFirmwarePlatformBundleTypeCapProviderDeleted_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderDeleted = _CfprApFirmwarePlatformBundleTypeCapProviderDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 4),
    _CfprApFirmwarePlatformBundleTypeCapProviderDeleted_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderDeleted.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderDeprecated_Type = TruthValue
_CfprApFirmwarePlatformBundleTypeCapProviderDeprecated_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderDeprecated = _CfprApFirmwarePlatformBundleTypeCapProviderDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 5),
    _CfprApFirmwarePlatformBundleTypeCapProviderDeprecated_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderDeprecated.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderElementLoadFailures_Type = Gauge32
_CfprApFirmwarePlatformBundleTypeCapProviderElementLoadFailures_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderElementLoadFailures = _CfprApFirmwarePlatformBundleTypeCapProviderElementLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 6),
    _CfprApFirmwarePlatformBundleTypeCapProviderElementLoadFailures_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderElementLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderElementLoadFailures.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderElementsLoaded_Type = Gauge32
_CfprApFirmwarePlatformBundleTypeCapProviderElementsLoaded_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderElementsLoaded = _CfprApFirmwarePlatformBundleTypeCapProviderElementsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 7),
    _CfprApFirmwarePlatformBundleTypeCapProviderElementsLoaded_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderElementsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderElementsLoaded.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderGencount_Type = Gauge32
_CfprApFirmwarePlatformBundleTypeCapProviderGencount_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderGencount = _CfprApFirmwarePlatformBundleTypeCapProviderGencount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 8),
    _CfprApFirmwarePlatformBundleTypeCapProviderGencount_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderGencount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderGencount.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderLoadErrors_Type = Gauge32
_CfprApFirmwarePlatformBundleTypeCapProviderLoadErrors_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderLoadErrors = _CfprApFirmwarePlatformBundleTypeCapProviderLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 9),
    _CfprApFirmwarePlatformBundleTypeCapProviderLoadErrors_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderLoadErrors.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderLoadWarnings_Type = Gauge32
_CfprApFirmwarePlatformBundleTypeCapProviderLoadWarnings_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderLoadWarnings = _CfprApFirmwarePlatformBundleTypeCapProviderLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 10),
    _CfprApFirmwarePlatformBundleTypeCapProviderLoadWarnings_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderLoadWarnings.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer_Type = SnmpAdminString
_CfprApFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer = _CfprApFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 11),
    _CfprApFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderModel_Type = SnmpAdminString
_CfprApFirmwarePlatformBundleTypeCapProviderModel_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderModel = _CfprApFirmwarePlatformBundleTypeCapProviderModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 12),
    _CfprApFirmwarePlatformBundleTypeCapProviderModel_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderModel.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderPlatformType_Type = CfprApFirmwarePlatformType
_CfprApFirmwarePlatformBundleTypeCapProviderPlatformType_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderPlatformType = _CfprApFirmwarePlatformBundleTypeCapProviderPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 13),
    _CfprApFirmwarePlatformBundleTypeCapProviderPlatformType_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderPlatformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderPlatformType.setStatus("current")
_CfprApFirmwarePlatformBundleTypeCapProviderVendor_Type = SnmpAdminString
_CfprApFirmwarePlatformBundleTypeCapProviderVendor_Object = MibTableColumn
cfprApFirmwarePlatformBundleTypeCapProviderVendor = _CfprApFirmwarePlatformBundleTypeCapProviderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 47, 1, 14),
    _CfprApFirmwarePlatformBundleTypeCapProviderVendor_Type()
)
cfprApFirmwarePlatformBundleTypeCapProviderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformBundleTypeCapProviderVendor.setStatus("current")
_CfprApFirmwarePlatformPackTable_Object = MibTable
cfprApFirmwarePlatformPackTable = _CfprApFirmwarePlatformPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48)
)
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackTable.setStatus("current")
_CfprApFirmwarePlatformPackEntry_Object = MibTableRow
cfprApFirmwarePlatformPackEntry = _CfprApFirmwarePlatformPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1)
)
cfprApFirmwarePlatformPackEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwarePlatformPackInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackEntry.setStatus("current")
_CfprApFirmwarePlatformPackInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwarePlatformPackInstanceId_Object = MibTableColumn
cfprApFirmwarePlatformPackInstanceId = _CfprApFirmwarePlatformPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 1),
    _CfprApFirmwarePlatformPackInstanceId_Type()
)
cfprApFirmwarePlatformPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackInstanceId.setStatus("current")
_CfprApFirmwarePlatformPackDn_Type = CfprApManagedObjectDn
_CfprApFirmwarePlatformPackDn_Object = MibTableColumn
cfprApFirmwarePlatformPackDn = _CfprApFirmwarePlatformPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 2),
    _CfprApFirmwarePlatformPackDn_Type()
)
cfprApFirmwarePlatformPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackDn.setStatus("current")
_CfprApFirmwarePlatformPackRn_Type = SnmpAdminString
_CfprApFirmwarePlatformPackRn_Object = MibTableColumn
cfprApFirmwarePlatformPackRn = _CfprApFirmwarePlatformPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 3),
    _CfprApFirmwarePlatformPackRn_Type()
)
cfprApFirmwarePlatformPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackRn.setStatus("current")
_CfprApFirmwarePlatformPackDescr_Type = SnmpAdminString
_CfprApFirmwarePlatformPackDescr_Object = MibTableColumn
cfprApFirmwarePlatformPackDescr = _CfprApFirmwarePlatformPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 4),
    _CfprApFirmwarePlatformPackDescr_Type()
)
cfprApFirmwarePlatformPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackDescr.setStatus("current")
_CfprApFirmwarePlatformPackForceDeploy_Type = TruthValue
_CfprApFirmwarePlatformPackForceDeploy_Object = MibTableColumn
cfprApFirmwarePlatformPackForceDeploy = _CfprApFirmwarePlatformPackForceDeploy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 5),
    _CfprApFirmwarePlatformPackForceDeploy_Type()
)
cfprApFirmwarePlatformPackForceDeploy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackForceDeploy.setStatus("current")
_CfprApFirmwarePlatformPackFsmDescr_Type = SnmpAdminString
_CfprApFirmwarePlatformPackFsmDescr_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmDescr = _CfprApFirmwarePlatformPackFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 6),
    _CfprApFirmwarePlatformPackFsmDescr_Type()
)
cfprApFirmwarePlatformPackFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmDescr.setStatus("current")
_CfprApFirmwarePlatformPackFsmFlags_Type = SnmpAdminString
_CfprApFirmwarePlatformPackFsmFlags_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmFlags = _CfprApFirmwarePlatformPackFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 7),
    _CfprApFirmwarePlatformPackFsmFlags_Type()
)
cfprApFirmwarePlatformPackFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmFlags.setStatus("current")
_CfprApFirmwarePlatformPackFsmPrev_Type = SnmpAdminString
_CfprApFirmwarePlatformPackFsmPrev_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmPrev = _CfprApFirmwarePlatformPackFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 8),
    _CfprApFirmwarePlatformPackFsmPrev_Type()
)
cfprApFirmwarePlatformPackFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmPrev.setStatus("current")
_CfprApFirmwarePlatformPackFsmProgr_Type = Gauge32
_CfprApFirmwarePlatformPackFsmProgr_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmProgr = _CfprApFirmwarePlatformPackFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 9),
    _CfprApFirmwarePlatformPackFsmProgr_Type()
)
cfprApFirmwarePlatformPackFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmProgr.setStatus("current")
_CfprApFirmwarePlatformPackFsmRmtInvErrCode_Type = Gauge32
_CfprApFirmwarePlatformPackFsmRmtInvErrCode_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmRmtInvErrCode = _CfprApFirmwarePlatformPackFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 10),
    _CfprApFirmwarePlatformPackFsmRmtInvErrCode_Type()
)
cfprApFirmwarePlatformPackFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmRmtInvErrCode.setStatus("current")
_CfprApFirmwarePlatformPackFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApFirmwarePlatformPackFsmRmtInvErrDescr_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmRmtInvErrDescr = _CfprApFirmwarePlatformPackFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 11),
    _CfprApFirmwarePlatformPackFsmRmtInvErrDescr_Type()
)
cfprApFirmwarePlatformPackFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmRmtInvErrDescr.setStatus("current")
_CfprApFirmwarePlatformPackFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwarePlatformPackFsmRmtInvRslt_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmRmtInvRslt = _CfprApFirmwarePlatformPackFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 12),
    _CfprApFirmwarePlatformPackFsmRmtInvRslt_Type()
)
cfprApFirmwarePlatformPackFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmRmtInvRslt.setStatus("current")
_CfprApFirmwarePlatformPackFsmStageDescr_Type = SnmpAdminString
_CfprApFirmwarePlatformPackFsmStageDescr_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmStageDescr = _CfprApFirmwarePlatformPackFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 13),
    _CfprApFirmwarePlatformPackFsmStageDescr_Type()
)
cfprApFirmwarePlatformPackFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStageDescr.setStatus("current")
_CfprApFirmwarePlatformPackFsmStamp_Type = DateAndTime
_CfprApFirmwarePlatformPackFsmStamp_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmStamp = _CfprApFirmwarePlatformPackFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 14),
    _CfprApFirmwarePlatformPackFsmStamp_Type()
)
cfprApFirmwarePlatformPackFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStamp.setStatus("current")
_CfprApFirmwarePlatformPackFsmStatus_Type = SnmpAdminString
_CfprApFirmwarePlatformPackFsmStatus_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmStatus = _CfprApFirmwarePlatformPackFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 15),
    _CfprApFirmwarePlatformPackFsmStatus_Type()
)
cfprApFirmwarePlatformPackFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStatus.setStatus("current")
_CfprApFirmwarePlatformPackFsmTry_Type = Gauge32
_CfprApFirmwarePlatformPackFsmTry_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmTry = _CfprApFirmwarePlatformPackFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 16),
    _CfprApFirmwarePlatformPackFsmTry_Type()
)
cfprApFirmwarePlatformPackFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmTry.setStatus("current")
_CfprApFirmwarePlatformPackIntId_Type = SnmpAdminString
_CfprApFirmwarePlatformPackIntId_Object = MibTableColumn
cfprApFirmwarePlatformPackIntId = _CfprApFirmwarePlatformPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 17),
    _CfprApFirmwarePlatformPackIntId_Type()
)
cfprApFirmwarePlatformPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackIntId.setStatus("current")
_CfprApFirmwarePlatformPackMode_Type = CfprApFirmwarePackMode
_CfprApFirmwarePlatformPackMode_Object = MibTableColumn
cfprApFirmwarePlatformPackMode = _CfprApFirmwarePlatformPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 18),
    _CfprApFirmwarePlatformPackMode_Type()
)
cfprApFirmwarePlatformPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackMode.setStatus("current")
_CfprApFirmwarePlatformPackName_Type = SnmpAdminString
_CfprApFirmwarePlatformPackName_Object = MibTableColumn
cfprApFirmwarePlatformPackName = _CfprApFirmwarePlatformPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 19),
    _CfprApFirmwarePlatformPackName_Type()
)
cfprApFirmwarePlatformPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackName.setStatus("current")
_CfprApFirmwarePlatformPackPlatformBundleName_Type = SnmpAdminString
_CfprApFirmwarePlatformPackPlatformBundleName_Object = MibTableColumn
cfprApFirmwarePlatformPackPlatformBundleName = _CfprApFirmwarePlatformPackPlatformBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 20),
    _CfprApFirmwarePlatformPackPlatformBundleName_Type()
)
cfprApFirmwarePlatformPackPlatformBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackPlatformBundleName.setStatus("current")
_CfprApFirmwarePlatformPackPlatformBundleVersion_Type = SnmpAdminString
_CfprApFirmwarePlatformPackPlatformBundleVersion_Object = MibTableColumn
cfprApFirmwarePlatformPackPlatformBundleVersion = _CfprApFirmwarePlatformPackPlatformBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 21),
    _CfprApFirmwarePlatformPackPlatformBundleVersion_Type()
)
cfprApFirmwarePlatformPackPlatformBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackPlatformBundleVersion.setStatus("current")
_CfprApFirmwarePlatformPackPolicyLevel_Type = Gauge32
_CfprApFirmwarePlatformPackPolicyLevel_Object = MibTableColumn
cfprApFirmwarePlatformPackPolicyLevel = _CfprApFirmwarePlatformPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 22),
    _CfprApFirmwarePlatformPackPolicyLevel_Type()
)
cfprApFirmwarePlatformPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackPolicyLevel.setStatus("current")
_CfprApFirmwarePlatformPackPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFirmwarePlatformPackPolicyOwner_Object = MibTableColumn
cfprApFirmwarePlatformPackPolicyOwner = _CfprApFirmwarePlatformPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 23),
    _CfprApFirmwarePlatformPackPolicyOwner_Type()
)
cfprApFirmwarePlatformPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackPolicyOwner.setStatus("current")
_CfprApFirmwarePlatformPackPreviousBundleVersion_Type = SnmpAdminString
_CfprApFirmwarePlatformPackPreviousBundleVersion_Object = MibTableColumn
cfprApFirmwarePlatformPackPreviousBundleVersion = _CfprApFirmwarePlatformPackPreviousBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 24),
    _CfprApFirmwarePlatformPackPreviousBundleVersion_Type()
)
cfprApFirmwarePlatformPackPreviousBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackPreviousBundleVersion.setStatus("current")
_CfprApFirmwarePlatformPackRestoreVersion_Type = TruthValue
_CfprApFirmwarePlatformPackRestoreVersion_Object = MibTableColumn
cfprApFirmwarePlatformPackRestoreVersion = _CfprApFirmwarePlatformPackRestoreVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 25),
    _CfprApFirmwarePlatformPackRestoreVersion_Type()
)
cfprApFirmwarePlatformPackRestoreVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackRestoreVersion.setStatus("current")
_CfprApFirmwarePlatformPackSerializeHostUpgrade_Type = TruthValue
_CfprApFirmwarePlatformPackSerializeHostUpgrade_Object = MibTableColumn
cfprApFirmwarePlatformPackSerializeHostUpgrade = _CfprApFirmwarePlatformPackSerializeHostUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 26),
    _CfprApFirmwarePlatformPackSerializeHostUpgrade_Type()
)
cfprApFirmwarePlatformPackSerializeHostUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackSerializeHostUpgrade.setStatus("current")
_CfprApFirmwarePlatformPackSkipManagerValidation_Type = TruthValue
_CfprApFirmwarePlatformPackSkipManagerValidation_Object = MibTableColumn
cfprApFirmwarePlatformPackSkipManagerValidation = _CfprApFirmwarePlatformPackSkipManagerValidation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 27),
    _CfprApFirmwarePlatformPackSkipManagerValidation_Type()
)
cfprApFirmwarePlatformPackSkipManagerValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackSkipManagerValidation.setStatus("current")
_CfprApFirmwarePlatformPackStageSize_Type = Gauge32
_CfprApFirmwarePlatformPackStageSize_Object = MibTableColumn
cfprApFirmwarePlatformPackStageSize = _CfprApFirmwarePlatformPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 28),
    _CfprApFirmwarePlatformPackStageSize_Type()
)
cfprApFirmwarePlatformPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackStageSize.setStatus("current")
_CfprApFirmwarePlatformPackUpdateTrigger_Type = DateAndTime
_CfprApFirmwarePlatformPackUpdateTrigger_Object = MibTableColumn
cfprApFirmwarePlatformPackUpdateTrigger = _CfprApFirmwarePlatformPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 48, 1, 29),
    _CfprApFirmwarePlatformPackUpdateTrigger_Type()
)
cfprApFirmwarePlatformPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackUpdateTrigger.setStatus("current")
_CfprApFirmwarePlatformPackFsmTable_Object = MibTable
cfprApFirmwarePlatformPackFsmTable = _CfprApFirmwarePlatformPackFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49)
)
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmTable.setStatus("current")
_CfprApFirmwarePlatformPackFsmEntry_Object = MibTableRow
cfprApFirmwarePlatformPackFsmEntry = _CfprApFirmwarePlatformPackFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49, 1)
)
cfprApFirmwarePlatformPackFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwarePlatformPackFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmEntry.setStatus("current")
_CfprApFirmwarePlatformPackFsmInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwarePlatformPackFsmInstanceId_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmInstanceId = _CfprApFirmwarePlatformPackFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49, 1, 1),
    _CfprApFirmwarePlatformPackFsmInstanceId_Type()
)
cfprApFirmwarePlatformPackFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmInstanceId.setStatus("current")
_CfprApFirmwarePlatformPackFsmDn_Type = CfprApManagedObjectDn
_CfprApFirmwarePlatformPackFsmDn_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmDn = _CfprApFirmwarePlatformPackFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49, 1, 2),
    _CfprApFirmwarePlatformPackFsmDn_Type()
)
cfprApFirmwarePlatformPackFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmDn.setStatus("current")
_CfprApFirmwarePlatformPackFsmRn_Type = SnmpAdminString
_CfprApFirmwarePlatformPackFsmRn_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmRn = _CfprApFirmwarePlatformPackFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49, 1, 3),
    _CfprApFirmwarePlatformPackFsmRn_Type()
)
cfprApFirmwarePlatformPackFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmRn.setStatus("current")
_CfprApFirmwarePlatformPackFsmCompletionTime_Type = DateAndTime
_CfprApFirmwarePlatformPackFsmCompletionTime_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmCompletionTime = _CfprApFirmwarePlatformPackFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49, 1, 4),
    _CfprApFirmwarePlatformPackFsmCompletionTime_Type()
)
cfprApFirmwarePlatformPackFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmCompletionTime.setStatus("current")
_CfprApFirmwarePlatformPackFsmCurrentFsm_Type = CfprApFirmwarePlatformPackFsmCurrentFsm
_CfprApFirmwarePlatformPackFsmCurrentFsm_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmCurrentFsm = _CfprApFirmwarePlatformPackFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49, 1, 5),
    _CfprApFirmwarePlatformPackFsmCurrentFsm_Type()
)
cfprApFirmwarePlatformPackFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmCurrentFsm.setStatus("current")
_CfprApFirmwarePlatformPackFsmDescrData_Type = SnmpAdminString
_CfprApFirmwarePlatformPackFsmDescrData_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmDescrData = _CfprApFirmwarePlatformPackFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49, 1, 6),
    _CfprApFirmwarePlatformPackFsmDescrData_Type()
)
cfprApFirmwarePlatformPackFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmDescrData.setStatus("current")
_CfprApFirmwarePlatformPackFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwarePlatformPackFsmFsmStatus_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmFsmStatus = _CfprApFirmwarePlatformPackFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49, 1, 7),
    _CfprApFirmwarePlatformPackFsmFsmStatus_Type()
)
cfprApFirmwarePlatformPackFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmFsmStatus.setStatus("current")
_CfprApFirmwarePlatformPackFsmProgress_Type = Gauge32
_CfprApFirmwarePlatformPackFsmProgress_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmProgress = _CfprApFirmwarePlatformPackFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49, 1, 8),
    _CfprApFirmwarePlatformPackFsmProgress_Type()
)
cfprApFirmwarePlatformPackFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmProgress.setStatus("current")
_CfprApFirmwarePlatformPackFsmRmtErrCode_Type = Gauge32
_CfprApFirmwarePlatformPackFsmRmtErrCode_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmRmtErrCode = _CfprApFirmwarePlatformPackFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49, 1, 9),
    _CfprApFirmwarePlatformPackFsmRmtErrCode_Type()
)
cfprApFirmwarePlatformPackFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmRmtErrCode.setStatus("current")
_CfprApFirmwarePlatformPackFsmRmtErrDescr_Type = SnmpAdminString
_CfprApFirmwarePlatformPackFsmRmtErrDescr_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmRmtErrDescr = _CfprApFirmwarePlatformPackFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49, 1, 10),
    _CfprApFirmwarePlatformPackFsmRmtErrDescr_Type()
)
cfprApFirmwarePlatformPackFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmRmtErrDescr.setStatus("current")
_CfprApFirmwarePlatformPackFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwarePlatformPackFsmRmtRslt_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmRmtRslt = _CfprApFirmwarePlatformPackFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 49, 1, 11),
    _CfprApFirmwarePlatformPackFsmRmtRslt_Type()
)
cfprApFirmwarePlatformPackFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmRmtRslt.setStatus("current")
_CfprApFirmwarePlatformPackFsmStageTable_Object = MibTable
cfprApFirmwarePlatformPackFsmStageTable = _CfprApFirmwarePlatformPackFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 50)
)
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStageTable.setStatus("current")
_CfprApFirmwarePlatformPackFsmStageEntry_Object = MibTableRow
cfprApFirmwarePlatformPackFsmStageEntry = _CfprApFirmwarePlatformPackFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 50, 1)
)
cfprApFirmwarePlatformPackFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwarePlatformPackFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStageEntry.setStatus("current")
_CfprApFirmwarePlatformPackFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwarePlatformPackFsmStageInstanceId_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmStageInstanceId = _CfprApFirmwarePlatformPackFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 50, 1, 1),
    _CfprApFirmwarePlatformPackFsmStageInstanceId_Type()
)
cfprApFirmwarePlatformPackFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStageInstanceId.setStatus("current")
_CfprApFirmwarePlatformPackFsmStageDn_Type = CfprApManagedObjectDn
_CfprApFirmwarePlatformPackFsmStageDn_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmStageDn = _CfprApFirmwarePlatformPackFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 50, 1, 2),
    _CfprApFirmwarePlatformPackFsmStageDn_Type()
)
cfprApFirmwarePlatformPackFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStageDn.setStatus("current")
_CfprApFirmwarePlatformPackFsmStageRn_Type = SnmpAdminString
_CfprApFirmwarePlatformPackFsmStageRn_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmStageRn = _CfprApFirmwarePlatformPackFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 50, 1, 3),
    _CfprApFirmwarePlatformPackFsmStageRn_Type()
)
cfprApFirmwarePlatformPackFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStageRn.setStatus("current")
_CfprApFirmwarePlatformPackFsmStageDescrData_Type = SnmpAdminString
_CfprApFirmwarePlatformPackFsmStageDescrData_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmStageDescrData = _CfprApFirmwarePlatformPackFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 50, 1, 4),
    _CfprApFirmwarePlatformPackFsmStageDescrData_Type()
)
cfprApFirmwarePlatformPackFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStageDescrData.setStatus("current")
_CfprApFirmwarePlatformPackFsmStageLastUpdateTime_Type = DateAndTime
_CfprApFirmwarePlatformPackFsmStageLastUpdateTime_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmStageLastUpdateTime = _CfprApFirmwarePlatformPackFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 50, 1, 5),
    _CfprApFirmwarePlatformPackFsmStageLastUpdateTime_Type()
)
cfprApFirmwarePlatformPackFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStageLastUpdateTime.setStatus("current")
_CfprApFirmwarePlatformPackFsmStageName_Type = CfprApFirmwarePlatformPackFsmStageName
_CfprApFirmwarePlatformPackFsmStageName_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmStageName = _CfprApFirmwarePlatformPackFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 50, 1, 6),
    _CfprApFirmwarePlatformPackFsmStageName_Type()
)
cfprApFirmwarePlatformPackFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStageName.setStatus("current")
_CfprApFirmwarePlatformPackFsmStageOrder_Type = Gauge32
_CfprApFirmwarePlatformPackFsmStageOrder_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmStageOrder = _CfprApFirmwarePlatformPackFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 50, 1, 7),
    _CfprApFirmwarePlatformPackFsmStageOrder_Type()
)
cfprApFirmwarePlatformPackFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStageOrder.setStatus("current")
_CfprApFirmwarePlatformPackFsmStageRetry_Type = Gauge32
_CfprApFirmwarePlatformPackFsmStageRetry_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmStageRetry = _CfprApFirmwarePlatformPackFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 50, 1, 8),
    _CfprApFirmwarePlatformPackFsmStageRetry_Type()
)
cfprApFirmwarePlatformPackFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStageRetry.setStatus("current")
_CfprApFirmwarePlatformPackFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwarePlatformPackFsmStageStageStatus_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmStageStageStatus = _CfprApFirmwarePlatformPackFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 50, 1, 9),
    _CfprApFirmwarePlatformPackFsmStageStageStatus_Type()
)
cfprApFirmwarePlatformPackFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmStageStageStatus.setStatus("current")
_CfprApFirmwarePlatformPackFsmTaskTable_Object = MibTable
cfprApFirmwarePlatformPackFsmTaskTable = _CfprApFirmwarePlatformPackFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 51)
)
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmTaskTable.setStatus("current")
_CfprApFirmwarePlatformPackFsmTaskEntry_Object = MibTableRow
cfprApFirmwarePlatformPackFsmTaskEntry = _CfprApFirmwarePlatformPackFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 51, 1)
)
cfprApFirmwarePlatformPackFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwarePlatformPackFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmTaskEntry.setStatus("current")
_CfprApFirmwarePlatformPackFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwarePlatformPackFsmTaskInstanceId_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmTaskInstanceId = _CfprApFirmwarePlatformPackFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 51, 1, 1),
    _CfprApFirmwarePlatformPackFsmTaskInstanceId_Type()
)
cfprApFirmwarePlatformPackFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmTaskInstanceId.setStatus("current")
_CfprApFirmwarePlatformPackFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApFirmwarePlatformPackFsmTaskDn_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmTaskDn = _CfprApFirmwarePlatformPackFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 51, 1, 2),
    _CfprApFirmwarePlatformPackFsmTaskDn_Type()
)
cfprApFirmwarePlatformPackFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmTaskDn.setStatus("current")
_CfprApFirmwarePlatformPackFsmTaskRn_Type = SnmpAdminString
_CfprApFirmwarePlatformPackFsmTaskRn_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmTaskRn = _CfprApFirmwarePlatformPackFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 51, 1, 3),
    _CfprApFirmwarePlatformPackFsmTaskRn_Type()
)
cfprApFirmwarePlatformPackFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmTaskRn.setStatus("current")
_CfprApFirmwarePlatformPackFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApFirmwarePlatformPackFsmTaskCompletion_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmTaskCompletion = _CfprApFirmwarePlatformPackFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 51, 1, 4),
    _CfprApFirmwarePlatformPackFsmTaskCompletion_Type()
)
cfprApFirmwarePlatformPackFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmTaskCompletion.setStatus("current")
_CfprApFirmwarePlatformPackFsmTaskFlags_Type = CfprApFirmwarePlatformPackFsmTaskFlags
_CfprApFirmwarePlatformPackFsmTaskFlags_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmTaskFlags = _CfprApFirmwarePlatformPackFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 51, 1, 5),
    _CfprApFirmwarePlatformPackFsmTaskFlags_Type()
)
cfprApFirmwarePlatformPackFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmTaskFlags.setStatus("current")
_CfprApFirmwarePlatformPackFsmTaskItem_Type = CfprApFirmwarePlatformPackFsmTaskItem
_CfprApFirmwarePlatformPackFsmTaskItem_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmTaskItem = _CfprApFirmwarePlatformPackFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 51, 1, 6),
    _CfprApFirmwarePlatformPackFsmTaskItem_Type()
)
cfprApFirmwarePlatformPackFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmTaskItem.setStatus("current")
_CfprApFirmwarePlatformPackFsmTaskSeqId_Type = Gauge32
_CfprApFirmwarePlatformPackFsmTaskSeqId_Object = MibTableColumn
cfprApFirmwarePlatformPackFsmTaskSeqId = _CfprApFirmwarePlatformPackFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 51, 1, 7),
    _CfprApFirmwarePlatformPackFsmTaskSeqId_Type()
)
cfprApFirmwarePlatformPackFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwarePlatformPackFsmTaskSeqId.setStatus("current")
_CfprApFirmwareRackTable_Object = MibTable
cfprApFirmwareRackTable = _CfprApFirmwareRackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 52)
)
if mibBuilder.loadTexts:
    cfprApFirmwareRackTable.setStatus("current")
_CfprApFirmwareRackEntry_Object = MibTableRow
cfprApFirmwareRackEntry = _CfprApFirmwareRackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 52, 1)
)
cfprApFirmwareRackEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareRackInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareRackEntry.setStatus("current")
_CfprApFirmwareRackInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareRackInstanceId_Object = MibTableColumn
cfprApFirmwareRackInstanceId = _CfprApFirmwareRackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 52, 1, 1),
    _CfprApFirmwareRackInstanceId_Type()
)
cfprApFirmwareRackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareRackInstanceId.setStatus("current")
_CfprApFirmwareRackDn_Type = CfprApManagedObjectDn
_CfprApFirmwareRackDn_Object = MibTableColumn
cfprApFirmwareRackDn = _CfprApFirmwareRackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 52, 1, 2),
    _CfprApFirmwareRackDn_Type()
)
cfprApFirmwareRackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRackDn.setStatus("current")
_CfprApFirmwareRackRn_Type = SnmpAdminString
_CfprApFirmwareRackRn_Object = MibTableColumn
cfprApFirmwareRackRn = _CfprApFirmwareRackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 52, 1, 3),
    _CfprApFirmwareRackRn_Type()
)
cfprApFirmwareRackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRackRn.setStatus("current")
_CfprApFirmwareRackOperVersion_Type = SnmpAdminString
_CfprApFirmwareRackOperVersion_Object = MibTableColumn
cfprApFirmwareRackOperVersion = _CfprApFirmwareRackOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 52, 1, 4),
    _CfprApFirmwareRackOperVersion_Type()
)
cfprApFirmwareRackOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRackOperVersion.setStatus("current")
_CfprApFirmwareRommonInfoTable_Object = MibTable
cfprApFirmwareRommonInfoTable = _CfprApFirmwareRommonInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 53)
)
if mibBuilder.loadTexts:
    cfprApFirmwareRommonInfoTable.setStatus("current")
_CfprApFirmwareRommonInfoEntry_Object = MibTableRow
cfprApFirmwareRommonInfoEntry = _CfprApFirmwareRommonInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 53, 1)
)
cfprApFirmwareRommonInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareRommonInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareRommonInfoEntry.setStatus("current")
_CfprApFirmwareRommonInfoInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareRommonInfoInstanceId_Object = MibTableColumn
cfprApFirmwareRommonInfoInstanceId = _CfprApFirmwareRommonInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 53, 1, 1),
    _CfprApFirmwareRommonInfoInstanceId_Type()
)
cfprApFirmwareRommonInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareRommonInfoInstanceId.setStatus("current")
_CfprApFirmwareRommonInfoDn_Type = CfprApManagedObjectDn
_CfprApFirmwareRommonInfoDn_Object = MibTableColumn
cfprApFirmwareRommonInfoDn = _CfprApFirmwareRommonInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 53, 1, 2),
    _CfprApFirmwareRommonInfoDn_Type()
)
cfprApFirmwareRommonInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRommonInfoDn.setStatus("current")
_CfprApFirmwareRommonInfoRn_Type = SnmpAdminString
_CfprApFirmwareRommonInfoRn_Object = MibTableColumn
cfprApFirmwareRommonInfoRn = _CfprApFirmwareRommonInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 53, 1, 3),
    _CfprApFirmwareRommonInfoRn_Type()
)
cfprApFirmwareRommonInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRommonInfoRn.setStatus("current")
_CfprApFirmwareRommonInfoFirmwareStatus_Type = SnmpAdminString
_CfprApFirmwareRommonInfoFirmwareStatus_Object = MibTableColumn
cfprApFirmwareRommonInfoFirmwareStatus = _CfprApFirmwareRommonInfoFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 53, 1, 4),
    _CfprApFirmwareRommonInfoFirmwareStatus_Type()
)
cfprApFirmwareRommonInfoFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRommonInfoFirmwareStatus.setStatus("current")
_CfprApFirmwareRommonInfoFirmwareVersion_Type = SnmpAdminString
_CfprApFirmwareRommonInfoFirmwareVersion_Object = MibTableColumn
cfprApFirmwareRommonInfoFirmwareVersion = _CfprApFirmwareRommonInfoFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 53, 1, 5),
    _CfprApFirmwareRommonInfoFirmwareVersion_Type()
)
cfprApFirmwareRommonInfoFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRommonInfoFirmwareVersion.setStatus("current")
_CfprApFirmwareRommonInfoFpgaVersion_Type = SnmpAdminString
_CfprApFirmwareRommonInfoFpgaVersion_Object = MibTableColumn
cfprApFirmwareRommonInfoFpgaVersion = _CfprApFirmwareRommonInfoFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 53, 1, 6),
    _CfprApFirmwareRommonInfoFpgaVersion_Type()
)
cfprApFirmwareRommonInfoFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRommonInfoFpgaVersion.setStatus("current")
_CfprApFirmwareRommonInfoLanSpiVersion_Type = SnmpAdminString
_CfprApFirmwareRommonInfoLanSpiVersion_Object = MibTableColumn
cfprApFirmwareRommonInfoLanSpiVersion = _CfprApFirmwareRommonInfoLanSpiVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 53, 1, 7),
    _CfprApFirmwareRommonInfoLanSpiVersion_Type()
)
cfprApFirmwareRommonInfoLanSpiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRommonInfoLanSpiVersion.setStatus("current")
_CfprApFirmwareRommonInfoPowerSequencerVersion_Type = SnmpAdminString
_CfprApFirmwareRommonInfoPowerSequencerVersion_Object = MibTableColumn
cfprApFirmwareRommonInfoPowerSequencerVersion = _CfprApFirmwareRommonInfoPowerSequencerVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 53, 1, 8),
    _CfprApFirmwareRommonInfoPowerSequencerVersion_Type()
)
cfprApFirmwareRommonInfoPowerSequencerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRommonInfoPowerSequencerVersion.setStatus("current")
_CfprApFirmwareRommonInfoRommonVersion_Type = SnmpAdminString
_CfprApFirmwareRommonInfoRommonVersion_Object = MibTableColumn
cfprApFirmwareRommonInfoRommonVersion = _CfprApFirmwareRommonInfoRommonVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 53, 1, 9),
    _CfprApFirmwareRommonInfoRommonVersion_Type()
)
cfprApFirmwareRommonInfoRommonVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRommonInfoRommonVersion.setStatus("current")
_CfprApFirmwareRunningTable_Object = MibTable
cfprApFirmwareRunningTable = _CfprApFirmwareRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 54)
)
if mibBuilder.loadTexts:
    cfprApFirmwareRunningTable.setStatus("current")
_CfprApFirmwareRunningEntry_Object = MibTableRow
cfprApFirmwareRunningEntry = _CfprApFirmwareRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 54, 1)
)
cfprApFirmwareRunningEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareRunningInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareRunningEntry.setStatus("current")
_CfprApFirmwareRunningInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareRunningInstanceId_Object = MibTableColumn
cfprApFirmwareRunningInstanceId = _CfprApFirmwareRunningInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 54, 1, 1),
    _CfprApFirmwareRunningInstanceId_Type()
)
cfprApFirmwareRunningInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareRunningInstanceId.setStatus("current")
_CfprApFirmwareRunningDn_Type = CfprApManagedObjectDn
_CfprApFirmwareRunningDn_Object = MibTableColumn
cfprApFirmwareRunningDn = _CfprApFirmwareRunningDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 54, 1, 2),
    _CfprApFirmwareRunningDn_Type()
)
cfprApFirmwareRunningDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRunningDn.setStatus("current")
_CfprApFirmwareRunningRn_Type = SnmpAdminString
_CfprApFirmwareRunningRn_Object = MibTableColumn
cfprApFirmwareRunningRn = _CfprApFirmwareRunningRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 54, 1, 3),
    _CfprApFirmwareRunningRn_Type()
)
cfprApFirmwareRunningRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRunningRn.setStatus("current")
_CfprApFirmwareRunningDeployment_Type = CfprApFirmwareRunningDeployment
_CfprApFirmwareRunningDeployment_Object = MibTableColumn
cfprApFirmwareRunningDeployment = _CfprApFirmwareRunningDeployment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 54, 1, 4),
    _CfprApFirmwareRunningDeployment_Type()
)
cfprApFirmwareRunningDeployment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRunningDeployment.setStatus("current")
_CfprApFirmwareRunningInvTag_Type = SnmpAdminString
_CfprApFirmwareRunningInvTag_Object = MibTableColumn
cfprApFirmwareRunningInvTag = _CfprApFirmwareRunningInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 54, 1, 5),
    _CfprApFirmwareRunningInvTag_Type()
)
cfprApFirmwareRunningInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRunningInvTag.setStatus("current")
_CfprApFirmwareRunningPackageVersion_Type = SnmpAdminString
_CfprApFirmwareRunningPackageVersion_Object = MibTableColumn
cfprApFirmwareRunningPackageVersion = _CfprApFirmwareRunningPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 54, 1, 6),
    _CfprApFirmwareRunningPackageVersion_Type()
)
cfprApFirmwareRunningPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRunningPackageVersion.setStatus("current")
_CfprApFirmwareRunningPlatformVersion_Type = SnmpAdminString
_CfprApFirmwareRunningPlatformVersion_Object = MibTableColumn
cfprApFirmwareRunningPlatformVersion = _CfprApFirmwareRunningPlatformVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 54, 1, 7),
    _CfprApFirmwareRunningPlatformVersion_Type()
)
cfprApFirmwareRunningPlatformVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRunningPlatformVersion.setStatus("current")
_CfprApFirmwareRunningType_Type = CfprApFirmwareType
_CfprApFirmwareRunningType_Object = MibTableColumn
cfprApFirmwareRunningType = _CfprApFirmwareRunningType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 54, 1, 8),
    _CfprApFirmwareRunningType_Type()
)
cfprApFirmwareRunningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRunningType.setStatus("current")
_CfprApFirmwareRunningVersion_Type = SnmpAdminString
_CfprApFirmwareRunningVersion_Object = MibTableColumn
cfprApFirmwareRunningVersion = _CfprApFirmwareRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 54, 1, 9),
    _CfprApFirmwareRunningVersion_Type()
)
cfprApFirmwareRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareRunningVersion.setStatus("current")
_CfprApFirmwareSpecTable_Object = MibTable
cfprApFirmwareSpecTable = _CfprApFirmwareSpecTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 55)
)
if mibBuilder.loadTexts:
    cfprApFirmwareSpecTable.setStatus("current")
_CfprApFirmwareSpecEntry_Object = MibTableRow
cfprApFirmwareSpecEntry = _CfprApFirmwareSpecEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 55, 1)
)
cfprApFirmwareSpecEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareSpecInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareSpecEntry.setStatus("current")
_CfprApFirmwareSpecInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareSpecInstanceId_Object = MibTableColumn
cfprApFirmwareSpecInstanceId = _CfprApFirmwareSpecInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 55, 1, 1),
    _CfprApFirmwareSpecInstanceId_Type()
)
cfprApFirmwareSpecInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareSpecInstanceId.setStatus("current")
_CfprApFirmwareSpecDn_Type = CfprApManagedObjectDn
_CfprApFirmwareSpecDn_Object = MibTableColumn
cfprApFirmwareSpecDn = _CfprApFirmwareSpecDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 55, 1, 2),
    _CfprApFirmwareSpecDn_Type()
)
cfprApFirmwareSpecDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSpecDn.setStatus("current")
_CfprApFirmwareSpecRn_Type = SnmpAdminString
_CfprApFirmwareSpecRn_Object = MibTableColumn
cfprApFirmwareSpecRn = _CfprApFirmwareSpecRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 55, 1, 3),
    _CfprApFirmwareSpecRn_Type()
)
cfprApFirmwareSpecRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSpecRn.setStatus("current")
_CfprApFirmwareSpecBundleVersion_Type = SnmpAdminString
_CfprApFirmwareSpecBundleVersion_Object = MibTableColumn
cfprApFirmwareSpecBundleVersion = _CfprApFirmwareSpecBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 55, 1, 4),
    _CfprApFirmwareSpecBundleVersion_Type()
)
cfprApFirmwareSpecBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSpecBundleVersion.setStatus("current")
_CfprApFirmwareSpecEthEFIVersion_Type = SnmpAdminString
_CfprApFirmwareSpecEthEFIVersion_Object = MibTableColumn
cfprApFirmwareSpecEthEFIVersion = _CfprApFirmwareSpecEthEFIVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 55, 1, 5),
    _CfprApFirmwareSpecEthEFIVersion_Type()
)
cfprApFirmwareSpecEthEFIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSpecEthEFIVersion.setStatus("current")
_CfprApFirmwareSpecEthOptionRomVersion_Type = SnmpAdminString
_CfprApFirmwareSpecEthOptionRomVersion_Object = MibTableColumn
cfprApFirmwareSpecEthOptionRomVersion = _CfprApFirmwareSpecEthOptionRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 55, 1, 6),
    _CfprApFirmwareSpecEthOptionRomVersion_Type()
)
cfprApFirmwareSpecEthOptionRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSpecEthOptionRomVersion.setStatus("current")
_CfprApFirmwareSpecFcFWVersion_Type = SnmpAdminString
_CfprApFirmwareSpecFcFWVersion_Object = MibTableColumn
cfprApFirmwareSpecFcFWVersion = _CfprApFirmwareSpecFcFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 55, 1, 7),
    _CfprApFirmwareSpecFcFWVersion_Type()
)
cfprApFirmwareSpecFcFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSpecFcFWVersion.setStatus("current")
_CfprApFirmwareSpecFcOptionRomVersion_Type = SnmpAdminString
_CfprApFirmwareSpecFcOptionRomVersion_Object = MibTableColumn
cfprApFirmwareSpecFcOptionRomVersion = _CfprApFirmwareSpecFcOptionRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 55, 1, 8),
    _CfprApFirmwareSpecFcOptionRomVersion_Type()
)
cfprApFirmwareSpecFcOptionRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSpecFcOptionRomVersion.setStatus("current")
_CfprApFirmwareStatusTable_Object = MibTable
cfprApFirmwareStatusTable = _CfprApFirmwareStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 56)
)
if mibBuilder.loadTexts:
    cfprApFirmwareStatusTable.setStatus("current")
_CfprApFirmwareStatusEntry_Object = MibTableRow
cfprApFirmwareStatusEntry = _CfprApFirmwareStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 56, 1)
)
cfprApFirmwareStatusEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareStatusEntry.setStatus("current")
_CfprApFirmwareStatusInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareStatusInstanceId_Object = MibTableColumn
cfprApFirmwareStatusInstanceId = _CfprApFirmwareStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 56, 1, 1),
    _CfprApFirmwareStatusInstanceId_Type()
)
cfprApFirmwareStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareStatusInstanceId.setStatus("current")
_CfprApFirmwareStatusDn_Type = CfprApManagedObjectDn
_CfprApFirmwareStatusDn_Object = MibTableColumn
cfprApFirmwareStatusDn = _CfprApFirmwareStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 56, 1, 2),
    _CfprApFirmwareStatusDn_Type()
)
cfprApFirmwareStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareStatusDn.setStatus("current")
_CfprApFirmwareStatusRn_Type = SnmpAdminString
_CfprApFirmwareStatusRn_Object = MibTableColumn
cfprApFirmwareStatusRn = _CfprApFirmwareStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 56, 1, 3),
    _CfprApFirmwareStatusRn_Type()
)
cfprApFirmwareStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareStatusRn.setStatus("current")
_CfprApFirmwareStatusCimcVersion_Type = SnmpAdminString
_CfprApFirmwareStatusCimcVersion_Object = MibTableColumn
cfprApFirmwareStatusCimcVersion = _CfprApFirmwareStatusCimcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 56, 1, 4),
    _CfprApFirmwareStatusCimcVersion_Type()
)
cfprApFirmwareStatusCimcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareStatusCimcVersion.setStatus("current")
_CfprApFirmwareStatusFirmwareState_Type = CfprApFirmwareFirmwareState
_CfprApFirmwareStatusFirmwareState_Object = MibTableColumn
cfprApFirmwareStatusFirmwareState = _CfprApFirmwareStatusFirmwareState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 56, 1, 5),
    _CfprApFirmwareStatusFirmwareState_Type()
)
cfprApFirmwareStatusFirmwareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareStatusFirmwareState.setStatus("current")
_CfprApFirmwareStatusOperState_Type = CfprApFirmwareImageState
_CfprApFirmwareStatusOperState_Object = MibTableColumn
cfprApFirmwareStatusOperState = _CfprApFirmwareStatusOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 56, 1, 6),
    _CfprApFirmwareStatusOperState_Type()
)
cfprApFirmwareStatusOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareStatusOperState.setStatus("current")
_CfprApFirmwareStatusPackageVersion_Type = SnmpAdminString
_CfprApFirmwareStatusPackageVersion_Object = MibTableColumn
cfprApFirmwareStatusPackageVersion = _CfprApFirmwareStatusPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 56, 1, 7),
    _CfprApFirmwareStatusPackageVersion_Type()
)
cfprApFirmwareStatusPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareStatusPackageVersion.setStatus("current")
_CfprApFirmwareStatusPldVersion_Type = SnmpAdminString
_CfprApFirmwareStatusPldVersion_Object = MibTableColumn
cfprApFirmwareStatusPldVersion = _CfprApFirmwareStatusPldVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 56, 1, 8),
    _CfprApFirmwareStatusPldVersion_Type()
)
cfprApFirmwareStatusPldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareStatusPldVersion.setStatus("current")
_CfprApFirmwareSupFirmwareTable_Object = MibTable
cfprApFirmwareSupFirmwareTable = _CfprApFirmwareSupFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57)
)
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareTable.setStatus("current")
_CfprApFirmwareSupFirmwareEntry_Object = MibTableRow
cfprApFirmwareSupFirmwareEntry = _CfprApFirmwareSupFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1)
)
cfprApFirmwareSupFirmwareEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareSupFirmwareInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareEntry.setStatus("current")
_CfprApFirmwareSupFirmwareInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareSupFirmwareInstanceId_Object = MibTableColumn
cfprApFirmwareSupFirmwareInstanceId = _CfprApFirmwareSupFirmwareInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 1),
    _CfprApFirmwareSupFirmwareInstanceId_Type()
)
cfprApFirmwareSupFirmwareInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareInstanceId.setStatus("current")
_CfprApFirmwareSupFirmwareDn_Type = CfprApManagedObjectDn
_CfprApFirmwareSupFirmwareDn_Object = MibTableColumn
cfprApFirmwareSupFirmwareDn = _CfprApFirmwareSupFirmwareDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 2),
    _CfprApFirmwareSupFirmwareDn_Type()
)
cfprApFirmwareSupFirmwareDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareDn.setStatus("current")
_CfprApFirmwareSupFirmwareRn_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareRn_Object = MibTableColumn
cfprApFirmwareSupFirmwareRn = _CfprApFirmwareSupFirmwareRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 3),
    _CfprApFirmwareSupFirmwareRn_Type()
)
cfprApFirmwareSupFirmwareRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareRn.setStatus("current")
_CfprApFirmwareSupFirmwareFsmDescr_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareFsmDescr_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmDescr = _CfprApFirmwareSupFirmwareFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 4),
    _CfprApFirmwareSupFirmwareFsmDescr_Type()
)
cfprApFirmwareSupFirmwareFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmDescr.setStatus("current")
_CfprApFirmwareSupFirmwareFsmFlags_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareFsmFlags_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmFlags = _CfprApFirmwareSupFirmwareFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 5),
    _CfprApFirmwareSupFirmwareFsmFlags_Type()
)
cfprApFirmwareSupFirmwareFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmFlags.setStatus("current")
_CfprApFirmwareSupFirmwareFsmPrev_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareFsmPrev_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmPrev = _CfprApFirmwareSupFirmwareFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 6),
    _CfprApFirmwareSupFirmwareFsmPrev_Type()
)
cfprApFirmwareSupFirmwareFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmPrev.setStatus("current")
_CfprApFirmwareSupFirmwareFsmProgr_Type = Gauge32
_CfprApFirmwareSupFirmwareFsmProgr_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmProgr = _CfprApFirmwareSupFirmwareFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 7),
    _CfprApFirmwareSupFirmwareFsmProgr_Type()
)
cfprApFirmwareSupFirmwareFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmProgr.setStatus("current")
_CfprApFirmwareSupFirmwareFsmRmtInvErrCode_Type = Gauge32
_CfprApFirmwareSupFirmwareFsmRmtInvErrCode_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmRmtInvErrCode = _CfprApFirmwareSupFirmwareFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 8),
    _CfprApFirmwareSupFirmwareFsmRmtInvErrCode_Type()
)
cfprApFirmwareSupFirmwareFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmRmtInvErrCode.setStatus("current")
_CfprApFirmwareSupFirmwareFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareFsmRmtInvErrDescr_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmRmtInvErrDescr = _CfprApFirmwareSupFirmwareFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 9),
    _CfprApFirmwareSupFirmwareFsmRmtInvErrDescr_Type()
)
cfprApFirmwareSupFirmwareFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmRmtInvErrDescr.setStatus("current")
_CfprApFirmwareSupFirmwareFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwareSupFirmwareFsmRmtInvRslt_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmRmtInvRslt = _CfprApFirmwareSupFirmwareFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 10),
    _CfprApFirmwareSupFirmwareFsmRmtInvRslt_Type()
)
cfprApFirmwareSupFirmwareFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmRmtInvRslt.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStageDescr_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareFsmStageDescr_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmStageDescr = _CfprApFirmwareSupFirmwareFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 11),
    _CfprApFirmwareSupFirmwareFsmStageDescr_Type()
)
cfprApFirmwareSupFirmwareFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStageDescr.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStamp_Type = DateAndTime
_CfprApFirmwareSupFirmwareFsmStamp_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmStamp = _CfprApFirmwareSupFirmwareFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 12),
    _CfprApFirmwareSupFirmwareFsmStamp_Type()
)
cfprApFirmwareSupFirmwareFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStamp.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStatus_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareFsmStatus_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmStatus = _CfprApFirmwareSupFirmwareFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 13),
    _CfprApFirmwareSupFirmwareFsmStatus_Type()
)
cfprApFirmwareSupFirmwareFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStatus.setStatus("current")
_CfprApFirmwareSupFirmwareFsmTry_Type = Gauge32
_CfprApFirmwareSupFirmwareFsmTry_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmTry = _CfprApFirmwareSupFirmwareFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 14),
    _CfprApFirmwareSupFirmwareFsmTry_Type()
)
cfprApFirmwareSupFirmwareFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmTry.setStatus("current")
_CfprApFirmwareSupFirmwareOperState_Type = CfprApFirmwareFwUpgradeState
_CfprApFirmwareSupFirmwareOperState_Object = MibTableColumn
cfprApFirmwareSupFirmwareOperState = _CfprApFirmwareSupFirmwareOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 15),
    _CfprApFirmwareSupFirmwareOperState_Type()
)
cfprApFirmwareSupFirmwareOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareOperState.setStatus("current")
_CfprApFirmwareSupFirmwarePackVersion_Type = SnmpAdminString
_CfprApFirmwareSupFirmwarePackVersion_Object = MibTableColumn
cfprApFirmwareSupFirmwarePackVersion = _CfprApFirmwareSupFirmwarePackVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 16),
    _CfprApFirmwareSupFirmwarePackVersion_Type()
)
cfprApFirmwareSupFirmwarePackVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwarePackVersion.setStatus("current")
_CfprApFirmwareSupFirmwareState_Type = CfprApFirmwareFwState
_CfprApFirmwareSupFirmwareState_Object = MibTableColumn
cfprApFirmwareSupFirmwareState = _CfprApFirmwareSupFirmwareState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 17),
    _CfprApFirmwareSupFirmwareState_Type()
)
cfprApFirmwareSupFirmwareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareState.setStatus("current")
_CfprApFirmwareSupFirmwareUpgradeStatus_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareUpgradeStatus_Object = MibTableColumn
cfprApFirmwareSupFirmwareUpgradeStatus = _CfprApFirmwareSupFirmwareUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 57, 1, 18),
    _CfprApFirmwareSupFirmwareUpgradeStatus_Type()
)
cfprApFirmwareSupFirmwareUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareUpgradeStatus.setStatus("current")
_CfprApFirmwareSupFirmwareFsmTable_Object = MibTable
cfprApFirmwareSupFirmwareFsmTable = _CfprApFirmwareSupFirmwareFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58)
)
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmTable.setStatus("current")
_CfprApFirmwareSupFirmwareFsmEntry_Object = MibTableRow
cfprApFirmwareSupFirmwareFsmEntry = _CfprApFirmwareSupFirmwareFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58, 1)
)
cfprApFirmwareSupFirmwareFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareSupFirmwareFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmEntry.setStatus("current")
_CfprApFirmwareSupFirmwareFsmInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareSupFirmwareFsmInstanceId_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmInstanceId = _CfprApFirmwareSupFirmwareFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58, 1, 1),
    _CfprApFirmwareSupFirmwareFsmInstanceId_Type()
)
cfprApFirmwareSupFirmwareFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmInstanceId.setStatus("current")
_CfprApFirmwareSupFirmwareFsmDn_Type = CfprApManagedObjectDn
_CfprApFirmwareSupFirmwareFsmDn_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmDn = _CfprApFirmwareSupFirmwareFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58, 1, 2),
    _CfprApFirmwareSupFirmwareFsmDn_Type()
)
cfprApFirmwareSupFirmwareFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmDn.setStatus("current")
_CfprApFirmwareSupFirmwareFsmRn_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareFsmRn_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmRn = _CfprApFirmwareSupFirmwareFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58, 1, 3),
    _CfprApFirmwareSupFirmwareFsmRn_Type()
)
cfprApFirmwareSupFirmwareFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmRn.setStatus("current")
_CfprApFirmwareSupFirmwareFsmCompletionTime_Type = DateAndTime
_CfprApFirmwareSupFirmwareFsmCompletionTime_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmCompletionTime = _CfprApFirmwareSupFirmwareFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58, 1, 4),
    _CfprApFirmwareSupFirmwareFsmCompletionTime_Type()
)
cfprApFirmwareSupFirmwareFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmCompletionTime.setStatus("current")
_CfprApFirmwareSupFirmwareFsmCurrentFsm_Type = CfprApFirmwareSupFirmwareFsmCurrentFsm
_CfprApFirmwareSupFirmwareFsmCurrentFsm_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmCurrentFsm = _CfprApFirmwareSupFirmwareFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58, 1, 5),
    _CfprApFirmwareSupFirmwareFsmCurrentFsm_Type()
)
cfprApFirmwareSupFirmwareFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmCurrentFsm.setStatus("current")
_CfprApFirmwareSupFirmwareFsmDescrData_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareFsmDescrData_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmDescrData = _CfprApFirmwareSupFirmwareFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58, 1, 6),
    _CfprApFirmwareSupFirmwareFsmDescrData_Type()
)
cfprApFirmwareSupFirmwareFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmDescrData.setStatus("current")
_CfprApFirmwareSupFirmwareFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwareSupFirmwareFsmFsmStatus_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmFsmStatus = _CfprApFirmwareSupFirmwareFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58, 1, 7),
    _CfprApFirmwareSupFirmwareFsmFsmStatus_Type()
)
cfprApFirmwareSupFirmwareFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmFsmStatus.setStatus("current")
_CfprApFirmwareSupFirmwareFsmProgress_Type = Gauge32
_CfprApFirmwareSupFirmwareFsmProgress_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmProgress = _CfprApFirmwareSupFirmwareFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58, 1, 8),
    _CfprApFirmwareSupFirmwareFsmProgress_Type()
)
cfprApFirmwareSupFirmwareFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmProgress.setStatus("current")
_CfprApFirmwareSupFirmwareFsmRmtErrCode_Type = Gauge32
_CfprApFirmwareSupFirmwareFsmRmtErrCode_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmRmtErrCode = _CfprApFirmwareSupFirmwareFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58, 1, 9),
    _CfprApFirmwareSupFirmwareFsmRmtErrCode_Type()
)
cfprApFirmwareSupFirmwareFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmRmtErrCode.setStatus("current")
_CfprApFirmwareSupFirmwareFsmRmtErrDescr_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareFsmRmtErrDescr_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmRmtErrDescr = _CfprApFirmwareSupFirmwareFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58, 1, 10),
    _CfprApFirmwareSupFirmwareFsmRmtErrDescr_Type()
)
cfprApFirmwareSupFirmwareFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmRmtErrDescr.setStatus("current")
_CfprApFirmwareSupFirmwareFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwareSupFirmwareFsmRmtRslt_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmRmtRslt = _CfprApFirmwareSupFirmwareFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 58, 1, 11),
    _CfprApFirmwareSupFirmwareFsmRmtRslt_Type()
)
cfprApFirmwareSupFirmwareFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmRmtRslt.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStageTable_Object = MibTable
cfprApFirmwareSupFirmwareFsmStageTable = _CfprApFirmwareSupFirmwareFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 59)
)
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStageTable.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStageEntry_Object = MibTableRow
cfprApFirmwareSupFirmwareFsmStageEntry = _CfprApFirmwareSupFirmwareFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 59, 1)
)
cfprApFirmwareSupFirmwareFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareSupFirmwareFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStageEntry.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareSupFirmwareFsmStageInstanceId_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmStageInstanceId = _CfprApFirmwareSupFirmwareFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 59, 1, 1),
    _CfprApFirmwareSupFirmwareFsmStageInstanceId_Type()
)
cfprApFirmwareSupFirmwareFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStageInstanceId.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStageDn_Type = CfprApManagedObjectDn
_CfprApFirmwareSupFirmwareFsmStageDn_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmStageDn = _CfprApFirmwareSupFirmwareFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 59, 1, 2),
    _CfprApFirmwareSupFirmwareFsmStageDn_Type()
)
cfprApFirmwareSupFirmwareFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStageDn.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStageRn_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareFsmStageRn_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmStageRn = _CfprApFirmwareSupFirmwareFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 59, 1, 3),
    _CfprApFirmwareSupFirmwareFsmStageRn_Type()
)
cfprApFirmwareSupFirmwareFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStageRn.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStageDescrData_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareFsmStageDescrData_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmStageDescrData = _CfprApFirmwareSupFirmwareFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 59, 1, 4),
    _CfprApFirmwareSupFirmwareFsmStageDescrData_Type()
)
cfprApFirmwareSupFirmwareFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStageDescrData.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStageLastUpdateTime_Type = DateAndTime
_CfprApFirmwareSupFirmwareFsmStageLastUpdateTime_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmStageLastUpdateTime = _CfprApFirmwareSupFirmwareFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 59, 1, 5),
    _CfprApFirmwareSupFirmwareFsmStageLastUpdateTime_Type()
)
cfprApFirmwareSupFirmwareFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStageLastUpdateTime.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStageName_Type = CfprApFirmwareSupFirmwareFsmStageName
_CfprApFirmwareSupFirmwareFsmStageName_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmStageName = _CfprApFirmwareSupFirmwareFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 59, 1, 6),
    _CfprApFirmwareSupFirmwareFsmStageName_Type()
)
cfprApFirmwareSupFirmwareFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStageName.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStageOrder_Type = Gauge32
_CfprApFirmwareSupFirmwareFsmStageOrder_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmStageOrder = _CfprApFirmwareSupFirmwareFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 59, 1, 7),
    _CfprApFirmwareSupFirmwareFsmStageOrder_Type()
)
cfprApFirmwareSupFirmwareFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStageOrder.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStageRetry_Type = Gauge32
_CfprApFirmwareSupFirmwareFsmStageRetry_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmStageRetry = _CfprApFirmwareSupFirmwareFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 59, 1, 8),
    _CfprApFirmwareSupFirmwareFsmStageRetry_Type()
)
cfprApFirmwareSupFirmwareFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStageRetry.setStatus("current")
_CfprApFirmwareSupFirmwareFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwareSupFirmwareFsmStageStageStatus_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmStageStageStatus = _CfprApFirmwareSupFirmwareFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 59, 1, 9),
    _CfprApFirmwareSupFirmwareFsmStageStageStatus_Type()
)
cfprApFirmwareSupFirmwareFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmStageStageStatus.setStatus("current")
_CfprApFirmwareSupFirmwareFsmTaskTable_Object = MibTable
cfprApFirmwareSupFirmwareFsmTaskTable = _CfprApFirmwareSupFirmwareFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 60)
)
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmTaskTable.setStatus("current")
_CfprApFirmwareSupFirmwareFsmTaskEntry_Object = MibTableRow
cfprApFirmwareSupFirmwareFsmTaskEntry = _CfprApFirmwareSupFirmwareFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 60, 1)
)
cfprApFirmwareSupFirmwareFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareSupFirmwareFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmTaskEntry.setStatus("current")
_CfprApFirmwareSupFirmwareFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareSupFirmwareFsmTaskInstanceId_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmTaskInstanceId = _CfprApFirmwareSupFirmwareFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 60, 1, 1),
    _CfprApFirmwareSupFirmwareFsmTaskInstanceId_Type()
)
cfprApFirmwareSupFirmwareFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmTaskInstanceId.setStatus("current")
_CfprApFirmwareSupFirmwareFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApFirmwareSupFirmwareFsmTaskDn_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmTaskDn = _CfprApFirmwareSupFirmwareFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 60, 1, 2),
    _CfprApFirmwareSupFirmwareFsmTaskDn_Type()
)
cfprApFirmwareSupFirmwareFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmTaskDn.setStatus("current")
_CfprApFirmwareSupFirmwareFsmTaskRn_Type = SnmpAdminString
_CfprApFirmwareSupFirmwareFsmTaskRn_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmTaskRn = _CfprApFirmwareSupFirmwareFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 60, 1, 3),
    _CfprApFirmwareSupFirmwareFsmTaskRn_Type()
)
cfprApFirmwareSupFirmwareFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmTaskRn.setStatus("current")
_CfprApFirmwareSupFirmwareFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApFirmwareSupFirmwareFsmTaskCompletion_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmTaskCompletion = _CfprApFirmwareSupFirmwareFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 60, 1, 4),
    _CfprApFirmwareSupFirmwareFsmTaskCompletion_Type()
)
cfprApFirmwareSupFirmwareFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmTaskCompletion.setStatus("current")
_CfprApFirmwareSupFirmwareFsmTaskFlags_Type = CfprApFirmwareSupFirmwareFsmTaskFlags
_CfprApFirmwareSupFirmwareFsmTaskFlags_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmTaskFlags = _CfprApFirmwareSupFirmwareFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 60, 1, 5),
    _CfprApFirmwareSupFirmwareFsmTaskFlags_Type()
)
cfprApFirmwareSupFirmwareFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmTaskFlags.setStatus("current")
_CfprApFirmwareSupFirmwareFsmTaskItem_Type = CfprApFirmwareSupFirmwareFsmTaskItem
_CfprApFirmwareSupFirmwareFsmTaskItem_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmTaskItem = _CfprApFirmwareSupFirmwareFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 60, 1, 6),
    _CfprApFirmwareSupFirmwareFsmTaskItem_Type()
)
cfprApFirmwareSupFirmwareFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmTaskItem.setStatus("current")
_CfprApFirmwareSupFirmwareFsmTaskSeqId_Type = Gauge32
_CfprApFirmwareSupFirmwareFsmTaskSeqId_Object = MibTableColumn
cfprApFirmwareSupFirmwareFsmTaskSeqId = _CfprApFirmwareSupFirmwareFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 60, 1, 7),
    _CfprApFirmwareSupFirmwareFsmTaskSeqId_Type()
)
cfprApFirmwareSupFirmwareFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSupFirmwareFsmTaskSeqId.setStatus("current")
_CfprApFirmwareSystemTable_Object = MibTable
cfprApFirmwareSystemTable = _CfprApFirmwareSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61)
)
if mibBuilder.loadTexts:
    cfprApFirmwareSystemTable.setStatus("current")
_CfprApFirmwareSystemEntry_Object = MibTableRow
cfprApFirmwareSystemEntry = _CfprApFirmwareSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1)
)
cfprApFirmwareSystemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareSystemEntry.setStatus("current")
_CfprApFirmwareSystemInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareSystemInstanceId_Object = MibTableColumn
cfprApFirmwareSystemInstanceId = _CfprApFirmwareSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 1),
    _CfprApFirmwareSystemInstanceId_Type()
)
cfprApFirmwareSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemInstanceId.setStatus("current")
_CfprApFirmwareSystemDn_Type = CfprApManagedObjectDn
_CfprApFirmwareSystemDn_Object = MibTableColumn
cfprApFirmwareSystemDn = _CfprApFirmwareSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 2),
    _CfprApFirmwareSystemDn_Type()
)
cfprApFirmwareSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemDn.setStatus("current")
_CfprApFirmwareSystemRn_Type = SnmpAdminString
_CfprApFirmwareSystemRn_Object = MibTableColumn
cfprApFirmwareSystemRn = _CfprApFirmwareSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 3),
    _CfprApFirmwareSystemRn_Type()
)
cfprApFirmwareSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemRn.setStatus("current")
_CfprApFirmwareSystemFsmDescr_Type = SnmpAdminString
_CfprApFirmwareSystemFsmDescr_Object = MibTableColumn
cfprApFirmwareSystemFsmDescr = _CfprApFirmwareSystemFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 4),
    _CfprApFirmwareSystemFsmDescr_Type()
)
cfprApFirmwareSystemFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmDescr.setStatus("current")
_CfprApFirmwareSystemFsmFlags_Type = SnmpAdminString
_CfprApFirmwareSystemFsmFlags_Object = MibTableColumn
cfprApFirmwareSystemFsmFlags = _CfprApFirmwareSystemFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 5),
    _CfprApFirmwareSystemFsmFlags_Type()
)
cfprApFirmwareSystemFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmFlags.setStatus("current")
_CfprApFirmwareSystemFsmPrev_Type = SnmpAdminString
_CfprApFirmwareSystemFsmPrev_Object = MibTableColumn
cfprApFirmwareSystemFsmPrev = _CfprApFirmwareSystemFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 6),
    _CfprApFirmwareSystemFsmPrev_Type()
)
cfprApFirmwareSystemFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmPrev.setStatus("current")
_CfprApFirmwareSystemFsmProgr_Type = Gauge32
_CfprApFirmwareSystemFsmProgr_Object = MibTableColumn
cfprApFirmwareSystemFsmProgr = _CfprApFirmwareSystemFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 7),
    _CfprApFirmwareSystemFsmProgr_Type()
)
cfprApFirmwareSystemFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmProgr.setStatus("current")
_CfprApFirmwareSystemFsmRmtInvErrCode_Type = Gauge32
_CfprApFirmwareSystemFsmRmtInvErrCode_Object = MibTableColumn
cfprApFirmwareSystemFsmRmtInvErrCode = _CfprApFirmwareSystemFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 8),
    _CfprApFirmwareSystemFsmRmtInvErrCode_Type()
)
cfprApFirmwareSystemFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmRmtInvErrCode.setStatus("current")
_CfprApFirmwareSystemFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApFirmwareSystemFsmRmtInvErrDescr_Object = MibTableColumn
cfprApFirmwareSystemFsmRmtInvErrDescr = _CfprApFirmwareSystemFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 9),
    _CfprApFirmwareSystemFsmRmtInvErrDescr_Type()
)
cfprApFirmwareSystemFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmRmtInvErrDescr.setStatus("current")
_CfprApFirmwareSystemFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwareSystemFsmRmtInvRslt_Object = MibTableColumn
cfprApFirmwareSystemFsmRmtInvRslt = _CfprApFirmwareSystemFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 10),
    _CfprApFirmwareSystemFsmRmtInvRslt_Type()
)
cfprApFirmwareSystemFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmRmtInvRslt.setStatus("current")
_CfprApFirmwareSystemFsmStageDescr_Type = SnmpAdminString
_CfprApFirmwareSystemFsmStageDescr_Object = MibTableColumn
cfprApFirmwareSystemFsmStageDescr = _CfprApFirmwareSystemFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 11),
    _CfprApFirmwareSystemFsmStageDescr_Type()
)
cfprApFirmwareSystemFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStageDescr.setStatus("current")
_CfprApFirmwareSystemFsmStamp_Type = DateAndTime
_CfprApFirmwareSystemFsmStamp_Object = MibTableColumn
cfprApFirmwareSystemFsmStamp = _CfprApFirmwareSystemFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 12),
    _CfprApFirmwareSystemFsmStamp_Type()
)
cfprApFirmwareSystemFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStamp.setStatus("current")
_CfprApFirmwareSystemFsmStatus_Type = SnmpAdminString
_CfprApFirmwareSystemFsmStatus_Object = MibTableColumn
cfprApFirmwareSystemFsmStatus = _CfprApFirmwareSystemFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 13),
    _CfprApFirmwareSystemFsmStatus_Type()
)
cfprApFirmwareSystemFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStatus.setStatus("current")
_CfprApFirmwareSystemFsmTry_Type = Gauge32
_CfprApFirmwareSystemFsmTry_Object = MibTableColumn
cfprApFirmwareSystemFsmTry = _CfprApFirmwareSystemFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 14),
    _CfprApFirmwareSystemFsmTry_Type()
)
cfprApFirmwareSystemFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmTry.setStatus("current")
_CfprApFirmwareSystemFwUpgradeBitmap_Type = Gauge32
_CfprApFirmwareSystemFwUpgradeBitmap_Object = MibTableColumn
cfprApFirmwareSystemFwUpgradeBitmap = _CfprApFirmwareSystemFwUpgradeBitmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 15),
    _CfprApFirmwareSystemFwUpgradeBitmap_Type()
)
cfprApFirmwareSystemFwUpgradeBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFwUpgradeBitmap.setStatus("current")
_CfprApFirmwareSystemFwUpgradeStatus_Type = SnmpAdminString
_CfprApFirmwareSystemFwUpgradeStatus_Object = MibTableColumn
cfprApFirmwareSystemFwUpgradeStatus = _CfprApFirmwareSystemFwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 16),
    _CfprApFirmwareSystemFwUpgradeStatus_Type()
)
cfprApFirmwareSystemFwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFwUpgradeStatus.setStatus("current")
_CfprApFirmwareSystemOperState_Type = CfprApFirmwareInstallState
_CfprApFirmwareSystemOperState_Object = MibTableColumn
cfprApFirmwareSystemOperState = _CfprApFirmwareSystemOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 17),
    _CfprApFirmwareSystemOperState_Type()
)
cfprApFirmwareSystemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemOperState.setStatus("current")
_CfprApFirmwareSystemPackVersion_Type = SnmpAdminString
_CfprApFirmwareSystemPackVersion_Object = MibTableColumn
cfprApFirmwareSystemPackVersion = _CfprApFirmwareSystemPackVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 18),
    _CfprApFirmwareSystemPackVersion_Type()
)
cfprApFirmwareSystemPackVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemPackVersion.setStatus("current")
_CfprApFirmwareSystemScheduledInstallTime_Type = DateAndTime
_CfprApFirmwareSystemScheduledInstallTime_Object = MibTableColumn
cfprApFirmwareSystemScheduledInstallTime = _CfprApFirmwareSystemScheduledInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 19),
    _CfprApFirmwareSystemScheduledInstallTime_Type()
)
cfprApFirmwareSystemScheduledInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemScheduledInstallTime.setStatus("current")
_CfprApFirmwareSystemState_Type = CfprApFirmwareFwState
_CfprApFirmwareSystemState_Object = MibTableColumn
cfprApFirmwareSystemState = _CfprApFirmwareSystemState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 20),
    _CfprApFirmwareSystemState_Type()
)
cfprApFirmwareSystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemState.setStatus("current")
_CfprApFirmwareSystemUpgradeState_Type = CfprApFirmwareUpgradeState
_CfprApFirmwareSystemUpgradeState_Object = MibTableColumn
cfprApFirmwareSystemUpgradeState = _CfprApFirmwareSystemUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 21),
    _CfprApFirmwareSystemUpgradeState_Type()
)
cfprApFirmwareSystemUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemUpgradeState.setStatus("current")
_CfprApFirmwareSystemUpgradeStatus_Type = SnmpAdminString
_CfprApFirmwareSystemUpgradeStatus_Object = MibTableColumn
cfprApFirmwareSystemUpgradeStatus = _CfprApFirmwareSystemUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 61, 1, 22),
    _CfprApFirmwareSystemUpgradeStatus_Type()
)
cfprApFirmwareSystemUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemUpgradeStatus.setStatus("current")
_CfprApFirmwareSystemCompCheckResultTable_Object = MibTable
cfprApFirmwareSystemCompCheckResultTable = _CfprApFirmwareSystemCompCheckResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 62)
)
if mibBuilder.loadTexts:
    cfprApFirmwareSystemCompCheckResultTable.setStatus("current")
_CfprApFirmwareSystemCompCheckResultEntry_Object = MibTableRow
cfprApFirmwareSystemCompCheckResultEntry = _CfprApFirmwareSystemCompCheckResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 62, 1)
)
cfprApFirmwareSystemCompCheckResultEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareSystemCompCheckResultInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareSystemCompCheckResultEntry.setStatus("current")
_CfprApFirmwareSystemCompCheckResultInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareSystemCompCheckResultInstanceId_Object = MibTableColumn
cfprApFirmwareSystemCompCheckResultInstanceId = _CfprApFirmwareSystemCompCheckResultInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 62, 1, 1),
    _CfprApFirmwareSystemCompCheckResultInstanceId_Type()
)
cfprApFirmwareSystemCompCheckResultInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemCompCheckResultInstanceId.setStatus("current")
_CfprApFirmwareSystemCompCheckResultDn_Type = CfprApManagedObjectDn
_CfprApFirmwareSystemCompCheckResultDn_Object = MibTableColumn
cfprApFirmwareSystemCompCheckResultDn = _CfprApFirmwareSystemCompCheckResultDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 62, 1, 2),
    _CfprApFirmwareSystemCompCheckResultDn_Type()
)
cfprApFirmwareSystemCompCheckResultDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemCompCheckResultDn.setStatus("current")
_CfprApFirmwareSystemCompCheckResultRn_Type = SnmpAdminString
_CfprApFirmwareSystemCompCheckResultRn_Object = MibTableColumn
cfprApFirmwareSystemCompCheckResultRn = _CfprApFirmwareSystemCompCheckResultRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 62, 1, 3),
    _CfprApFirmwareSystemCompCheckResultRn_Type()
)
cfprApFirmwareSystemCompCheckResultRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemCompCheckResultRn.setStatus("current")
_CfprApFirmwareSystemCompCheckResultKeyDescr_Type = SnmpAdminString
_CfprApFirmwareSystemCompCheckResultKeyDescr_Object = MibTableColumn
cfprApFirmwareSystemCompCheckResultKeyDescr = _CfprApFirmwareSystemCompCheckResultKeyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 62, 1, 4),
    _CfprApFirmwareSystemCompCheckResultKeyDescr_Type()
)
cfprApFirmwareSystemCompCheckResultKeyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemCompCheckResultKeyDescr.setStatus("current")
_CfprApFirmwareSystemCompCheckResultKeyDn_Type = SnmpAdminString
_CfprApFirmwareSystemCompCheckResultKeyDn_Object = MibTableColumn
cfprApFirmwareSystemCompCheckResultKeyDn = _CfprApFirmwareSystemCompCheckResultKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 62, 1, 5),
    _CfprApFirmwareSystemCompCheckResultKeyDn_Type()
)
cfprApFirmwareSystemCompCheckResultKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemCompCheckResultKeyDn.setStatus("current")
_CfprApFirmwareSystemCompCheckResultNonCompDescr_Type = SnmpAdminString
_CfprApFirmwareSystemCompCheckResultNonCompDescr_Object = MibTableColumn
cfprApFirmwareSystemCompCheckResultNonCompDescr = _CfprApFirmwareSystemCompCheckResultNonCompDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 62, 1, 6),
    _CfprApFirmwareSystemCompCheckResultNonCompDescr_Type()
)
cfprApFirmwareSystemCompCheckResultNonCompDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemCompCheckResultNonCompDescr.setStatus("current")
_CfprApFirmwareSystemCompCheckResultNonCompDns_Type = SnmpAdminString
_CfprApFirmwareSystemCompCheckResultNonCompDns_Object = MibTableColumn
cfprApFirmwareSystemCompCheckResultNonCompDns = _CfprApFirmwareSystemCompCheckResultNonCompDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 62, 1, 7),
    _CfprApFirmwareSystemCompCheckResultNonCompDns_Type()
)
cfprApFirmwareSystemCompCheckResultNonCompDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemCompCheckResultNonCompDns.setStatus("current")
_CfprApFirmwareSystemCompCheckResultSubject_Type = CfprApFirmwareEquipmentType
_CfprApFirmwareSystemCompCheckResultSubject_Object = MibTableColumn
cfprApFirmwareSystemCompCheckResultSubject = _CfprApFirmwareSystemCompCheckResultSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 62, 1, 8),
    _CfprApFirmwareSystemCompCheckResultSubject_Type()
)
cfprApFirmwareSystemCompCheckResultSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemCompCheckResultSubject.setStatus("current")
_CfprApFirmwareSystemFsmTable_Object = MibTable
cfprApFirmwareSystemFsmTable = _CfprApFirmwareSystemFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63)
)
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmTable.setStatus("current")
_CfprApFirmwareSystemFsmEntry_Object = MibTableRow
cfprApFirmwareSystemFsmEntry = _CfprApFirmwareSystemFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63, 1)
)
cfprApFirmwareSystemFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareSystemFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmEntry.setStatus("current")
_CfprApFirmwareSystemFsmInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareSystemFsmInstanceId_Object = MibTableColumn
cfprApFirmwareSystemFsmInstanceId = _CfprApFirmwareSystemFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63, 1, 1),
    _CfprApFirmwareSystemFsmInstanceId_Type()
)
cfprApFirmwareSystemFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmInstanceId.setStatus("current")
_CfprApFirmwareSystemFsmDn_Type = CfprApManagedObjectDn
_CfprApFirmwareSystemFsmDn_Object = MibTableColumn
cfprApFirmwareSystemFsmDn = _CfprApFirmwareSystemFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63, 1, 2),
    _CfprApFirmwareSystemFsmDn_Type()
)
cfprApFirmwareSystemFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmDn.setStatus("current")
_CfprApFirmwareSystemFsmRn_Type = SnmpAdminString
_CfprApFirmwareSystemFsmRn_Object = MibTableColumn
cfprApFirmwareSystemFsmRn = _CfprApFirmwareSystemFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63, 1, 3),
    _CfprApFirmwareSystemFsmRn_Type()
)
cfprApFirmwareSystemFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmRn.setStatus("current")
_CfprApFirmwareSystemFsmCompletionTime_Type = DateAndTime
_CfprApFirmwareSystemFsmCompletionTime_Object = MibTableColumn
cfprApFirmwareSystemFsmCompletionTime = _CfprApFirmwareSystemFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63, 1, 4),
    _CfprApFirmwareSystemFsmCompletionTime_Type()
)
cfprApFirmwareSystemFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmCompletionTime.setStatus("current")
_CfprApFirmwareSystemFsmCurrentFsm_Type = CfprApFirmwareSystemFsmCurrentFsm
_CfprApFirmwareSystemFsmCurrentFsm_Object = MibTableColumn
cfprApFirmwareSystemFsmCurrentFsm = _CfprApFirmwareSystemFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63, 1, 5),
    _CfprApFirmwareSystemFsmCurrentFsm_Type()
)
cfprApFirmwareSystemFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmCurrentFsm.setStatus("current")
_CfprApFirmwareSystemFsmDescrData_Type = SnmpAdminString
_CfprApFirmwareSystemFsmDescrData_Object = MibTableColumn
cfprApFirmwareSystemFsmDescrData = _CfprApFirmwareSystemFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63, 1, 6),
    _CfprApFirmwareSystemFsmDescrData_Type()
)
cfprApFirmwareSystemFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmDescrData.setStatus("current")
_CfprApFirmwareSystemFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwareSystemFsmFsmStatus_Object = MibTableColumn
cfprApFirmwareSystemFsmFsmStatus = _CfprApFirmwareSystemFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63, 1, 7),
    _CfprApFirmwareSystemFsmFsmStatus_Type()
)
cfprApFirmwareSystemFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmFsmStatus.setStatus("current")
_CfprApFirmwareSystemFsmProgress_Type = Gauge32
_CfprApFirmwareSystemFsmProgress_Object = MibTableColumn
cfprApFirmwareSystemFsmProgress = _CfprApFirmwareSystemFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63, 1, 8),
    _CfprApFirmwareSystemFsmProgress_Type()
)
cfprApFirmwareSystemFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmProgress.setStatus("current")
_CfprApFirmwareSystemFsmRmtErrCode_Type = Gauge32
_CfprApFirmwareSystemFsmRmtErrCode_Object = MibTableColumn
cfprApFirmwareSystemFsmRmtErrCode = _CfprApFirmwareSystemFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63, 1, 9),
    _CfprApFirmwareSystemFsmRmtErrCode_Type()
)
cfprApFirmwareSystemFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmRmtErrCode.setStatus("current")
_CfprApFirmwareSystemFsmRmtErrDescr_Type = SnmpAdminString
_CfprApFirmwareSystemFsmRmtErrDescr_Object = MibTableColumn
cfprApFirmwareSystemFsmRmtErrDescr = _CfprApFirmwareSystemFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63, 1, 10),
    _CfprApFirmwareSystemFsmRmtErrDescr_Type()
)
cfprApFirmwareSystemFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmRmtErrDescr.setStatus("current")
_CfprApFirmwareSystemFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFirmwareSystemFsmRmtRslt_Object = MibTableColumn
cfprApFirmwareSystemFsmRmtRslt = _CfprApFirmwareSystemFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 63, 1, 11),
    _CfprApFirmwareSystemFsmRmtRslt_Type()
)
cfprApFirmwareSystemFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmRmtRslt.setStatus("current")
_CfprApFirmwareSystemFsmStageTable_Object = MibTable
cfprApFirmwareSystemFsmStageTable = _CfprApFirmwareSystemFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 64)
)
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStageTable.setStatus("current")
_CfprApFirmwareSystemFsmStageEntry_Object = MibTableRow
cfprApFirmwareSystemFsmStageEntry = _CfprApFirmwareSystemFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 64, 1)
)
cfprApFirmwareSystemFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareSystemFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStageEntry.setStatus("current")
_CfprApFirmwareSystemFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareSystemFsmStageInstanceId_Object = MibTableColumn
cfprApFirmwareSystemFsmStageInstanceId = _CfprApFirmwareSystemFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 64, 1, 1),
    _CfprApFirmwareSystemFsmStageInstanceId_Type()
)
cfprApFirmwareSystemFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStageInstanceId.setStatus("current")
_CfprApFirmwareSystemFsmStageDn_Type = CfprApManagedObjectDn
_CfprApFirmwareSystemFsmStageDn_Object = MibTableColumn
cfprApFirmwareSystemFsmStageDn = _CfprApFirmwareSystemFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 64, 1, 2),
    _CfprApFirmwareSystemFsmStageDn_Type()
)
cfprApFirmwareSystemFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStageDn.setStatus("current")
_CfprApFirmwareSystemFsmStageRn_Type = SnmpAdminString
_CfprApFirmwareSystemFsmStageRn_Object = MibTableColumn
cfprApFirmwareSystemFsmStageRn = _CfprApFirmwareSystemFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 64, 1, 3),
    _CfprApFirmwareSystemFsmStageRn_Type()
)
cfprApFirmwareSystemFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStageRn.setStatus("current")
_CfprApFirmwareSystemFsmStageDescrData_Type = SnmpAdminString
_CfprApFirmwareSystemFsmStageDescrData_Object = MibTableColumn
cfprApFirmwareSystemFsmStageDescrData = _CfprApFirmwareSystemFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 64, 1, 4),
    _CfprApFirmwareSystemFsmStageDescrData_Type()
)
cfprApFirmwareSystemFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStageDescrData.setStatus("current")
_CfprApFirmwareSystemFsmStageLastUpdateTime_Type = DateAndTime
_CfprApFirmwareSystemFsmStageLastUpdateTime_Object = MibTableColumn
cfprApFirmwareSystemFsmStageLastUpdateTime = _CfprApFirmwareSystemFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 64, 1, 5),
    _CfprApFirmwareSystemFsmStageLastUpdateTime_Type()
)
cfprApFirmwareSystemFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStageLastUpdateTime.setStatus("current")
_CfprApFirmwareSystemFsmStageName_Type = CfprApFirmwareSystemFsmStageName
_CfprApFirmwareSystemFsmStageName_Object = MibTableColumn
cfprApFirmwareSystemFsmStageName = _CfprApFirmwareSystemFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 64, 1, 6),
    _CfprApFirmwareSystemFsmStageName_Type()
)
cfprApFirmwareSystemFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStageName.setStatus("current")
_CfprApFirmwareSystemFsmStageOrder_Type = Gauge32
_CfprApFirmwareSystemFsmStageOrder_Object = MibTableColumn
cfprApFirmwareSystemFsmStageOrder = _CfprApFirmwareSystemFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 64, 1, 7),
    _CfprApFirmwareSystemFsmStageOrder_Type()
)
cfprApFirmwareSystemFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStageOrder.setStatus("current")
_CfprApFirmwareSystemFsmStageRetry_Type = Gauge32
_CfprApFirmwareSystemFsmStageRetry_Object = MibTableColumn
cfprApFirmwareSystemFsmStageRetry = _CfprApFirmwareSystemFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 64, 1, 8),
    _CfprApFirmwareSystemFsmStageRetry_Type()
)
cfprApFirmwareSystemFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStageRetry.setStatus("current")
_CfprApFirmwareSystemFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApFirmwareSystemFsmStageStageStatus_Object = MibTableColumn
cfprApFirmwareSystemFsmStageStageStatus = _CfprApFirmwareSystemFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 64, 1, 9),
    _CfprApFirmwareSystemFsmStageStageStatus_Type()
)
cfprApFirmwareSystemFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmStageStageStatus.setStatus("current")
_CfprApFirmwareSystemFsmTaskTable_Object = MibTable
cfprApFirmwareSystemFsmTaskTable = _CfprApFirmwareSystemFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 65)
)
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmTaskTable.setStatus("current")
_CfprApFirmwareSystemFsmTaskEntry_Object = MibTableRow
cfprApFirmwareSystemFsmTaskEntry = _CfprApFirmwareSystemFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 65, 1)
)
cfprApFirmwareSystemFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareSystemFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmTaskEntry.setStatus("current")
_CfprApFirmwareSystemFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareSystemFsmTaskInstanceId_Object = MibTableColumn
cfprApFirmwareSystemFsmTaskInstanceId = _CfprApFirmwareSystemFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 65, 1, 1),
    _CfprApFirmwareSystemFsmTaskInstanceId_Type()
)
cfprApFirmwareSystemFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmTaskInstanceId.setStatus("current")
_CfprApFirmwareSystemFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApFirmwareSystemFsmTaskDn_Object = MibTableColumn
cfprApFirmwareSystemFsmTaskDn = _CfprApFirmwareSystemFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 65, 1, 2),
    _CfprApFirmwareSystemFsmTaskDn_Type()
)
cfprApFirmwareSystemFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmTaskDn.setStatus("current")
_CfprApFirmwareSystemFsmTaskRn_Type = SnmpAdminString
_CfprApFirmwareSystemFsmTaskRn_Object = MibTableColumn
cfprApFirmwareSystemFsmTaskRn = _CfprApFirmwareSystemFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 65, 1, 3),
    _CfprApFirmwareSystemFsmTaskRn_Type()
)
cfprApFirmwareSystemFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmTaskRn.setStatus("current")
_CfprApFirmwareSystemFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApFirmwareSystemFsmTaskCompletion_Object = MibTableColumn
cfprApFirmwareSystemFsmTaskCompletion = _CfprApFirmwareSystemFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 65, 1, 4),
    _CfprApFirmwareSystemFsmTaskCompletion_Type()
)
cfprApFirmwareSystemFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmTaskCompletion.setStatus("current")
_CfprApFirmwareSystemFsmTaskFlags_Type = CfprApFirmwareSystemFsmTaskFlags
_CfprApFirmwareSystemFsmTaskFlags_Object = MibTableColumn
cfprApFirmwareSystemFsmTaskFlags = _CfprApFirmwareSystemFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 65, 1, 5),
    _CfprApFirmwareSystemFsmTaskFlags_Type()
)
cfprApFirmwareSystemFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmTaskFlags.setStatus("current")
_CfprApFirmwareSystemFsmTaskItem_Type = CfprApFirmwareSystemFsmTaskItem
_CfprApFirmwareSystemFsmTaskItem_Object = MibTableColumn
cfprApFirmwareSystemFsmTaskItem = _CfprApFirmwareSystemFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 65, 1, 6),
    _CfprApFirmwareSystemFsmTaskItem_Type()
)
cfprApFirmwareSystemFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmTaskItem.setStatus("current")
_CfprApFirmwareSystemFsmTaskSeqId_Type = Gauge32
_CfprApFirmwareSystemFsmTaskSeqId_Object = MibTableColumn
cfprApFirmwareSystemFsmTaskSeqId = _CfprApFirmwareSystemFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 65, 1, 7),
    _CfprApFirmwareSystemFsmTaskSeqId_Type()
)
cfprApFirmwareSystemFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareSystemFsmTaskSeqId.setStatus("current")
_CfprApFirmwareTypeTable_Object = MibTable
cfprApFirmwareTypeTable = _CfprApFirmwareTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 66)
)
if mibBuilder.loadTexts:
    cfprApFirmwareTypeTable.setStatus("current")
_CfprApFirmwareTypeEntry_Object = MibTableRow
cfprApFirmwareTypeEntry = _CfprApFirmwareTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 66, 1)
)
cfprApFirmwareTypeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareTypeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareTypeEntry.setStatus("current")
_CfprApFirmwareTypeInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareTypeInstanceId_Object = MibTableColumn
cfprApFirmwareTypeInstanceId = _CfprApFirmwareTypeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 66, 1, 1),
    _CfprApFirmwareTypeInstanceId_Type()
)
cfprApFirmwareTypeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareTypeInstanceId.setStatus("current")
_CfprApFirmwareTypeDn_Type = CfprApManagedObjectDn
_CfprApFirmwareTypeDn_Object = MibTableColumn
cfprApFirmwareTypeDn = _CfprApFirmwareTypeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 66, 1, 2),
    _CfprApFirmwareTypeDn_Type()
)
cfprApFirmwareTypeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareTypeDn.setStatus("current")
_CfprApFirmwareTypeRn_Type = SnmpAdminString
_CfprApFirmwareTypeRn_Object = MibTableColumn
cfprApFirmwareTypeRn = _CfprApFirmwareTypeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 66, 1, 3),
    _CfprApFirmwareTypeRn_Type()
)
cfprApFirmwareTypeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareTypeRn.setStatus("current")
_CfprApFirmwareTypeEp_Type = CfprApFirmwareType
_CfprApFirmwareTypeEp_Object = MibTableColumn
cfprApFirmwareTypeEp = _CfprApFirmwareTypeEp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 66, 1, 4),
    _CfprApFirmwareTypeEp_Type()
)
cfprApFirmwareTypeEp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareTypeEp.setStatus("current")
_CfprApFirmwareTypeInvTag_Type = SnmpAdminString
_CfprApFirmwareTypeInvTag_Object = MibTableColumn
cfprApFirmwareTypeInvTag = _CfprApFirmwareTypeInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 66, 1, 5),
    _CfprApFirmwareTypeInvTag_Type()
)
cfprApFirmwareTypeInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareTypeInvTag.setStatus("current")
_CfprApFirmwareTypeMaxVer_Type = SnmpAdminString
_CfprApFirmwareTypeMaxVer_Object = MibTableColumn
cfprApFirmwareTypeMaxVer = _CfprApFirmwareTypeMaxVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 66, 1, 6),
    _CfprApFirmwareTypeMaxVer_Type()
)
cfprApFirmwareTypeMaxVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareTypeMaxVer.setStatus("current")
_CfprApFirmwareTypeMinVer_Type = SnmpAdminString
_CfprApFirmwareTypeMinVer_Object = MibTableColumn
cfprApFirmwareTypeMinVer = _CfprApFirmwareTypeMinVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 66, 1, 7),
    _CfprApFirmwareTypeMinVer_Type()
)
cfprApFirmwareTypeMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareTypeMinVer.setStatus("current")
_CfprApFirmwareTypeScheduledInstallTime_Type = DateAndTime
_CfprApFirmwareTypeScheduledInstallTime_Object = MibTableColumn
cfprApFirmwareTypeScheduledInstallTime = _CfprApFirmwareTypeScheduledInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 66, 1, 8),
    _CfprApFirmwareTypeScheduledInstallTime_Type()
)
cfprApFirmwareTypeScheduledInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareTypeScheduledInstallTime.setStatus("current")
_CfprApFirmwareUcscInfoTable_Object = MibTable
cfprApFirmwareUcscInfoTable = _CfprApFirmwareUcscInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 67)
)
if mibBuilder.loadTexts:
    cfprApFirmwareUcscInfoTable.setStatus("current")
_CfprApFirmwareUcscInfoEntry_Object = MibTableRow
cfprApFirmwareUcscInfoEntry = _CfprApFirmwareUcscInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 67, 1)
)
cfprApFirmwareUcscInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareUcscInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareUcscInfoEntry.setStatus("current")
_CfprApFirmwareUcscInfoInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareUcscInfoInstanceId_Object = MibTableColumn
cfprApFirmwareUcscInfoInstanceId = _CfprApFirmwareUcscInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 67, 1, 1),
    _CfprApFirmwareUcscInfoInstanceId_Type()
)
cfprApFirmwareUcscInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareUcscInfoInstanceId.setStatus("current")
_CfprApFirmwareUcscInfoDn_Type = CfprApManagedObjectDn
_CfprApFirmwareUcscInfoDn_Object = MibTableColumn
cfprApFirmwareUcscInfoDn = _CfprApFirmwareUcscInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 67, 1, 2),
    _CfprApFirmwareUcscInfoDn_Type()
)
cfprApFirmwareUcscInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUcscInfoDn.setStatus("current")
_CfprApFirmwareUcscInfoRn_Type = SnmpAdminString
_CfprApFirmwareUcscInfoRn_Object = MibTableColumn
cfprApFirmwareUcscInfoRn = _CfprApFirmwareUcscInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 67, 1, 3),
    _CfprApFirmwareUcscInfoRn_Type()
)
cfprApFirmwareUcscInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUcscInfoRn.setStatus("current")
_CfprApFirmwareUcscInfoConnProtocol_Type = CfprApExtpolConnProtocol
_CfprApFirmwareUcscInfoConnProtocol_Object = MibTableColumn
cfprApFirmwareUcscInfoConnProtocol = _CfprApFirmwareUcscInfoConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 67, 1, 4),
    _CfprApFirmwareUcscInfoConnProtocol_Type()
)
cfprApFirmwareUcscInfoConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUcscInfoConnProtocol.setStatus("current")
_CfprApFirmwareUcscInfoHost_Type = SnmpAdminString
_CfprApFirmwareUcscInfoHost_Object = MibTableColumn
cfprApFirmwareUcscInfoHost = _CfprApFirmwareUcscInfoHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 67, 1, 5),
    _CfprApFirmwareUcscInfoHost_Type()
)
cfprApFirmwareUcscInfoHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUcscInfoHost.setStatus("current")
_CfprApFirmwareUcscInfoVersion_Type = SnmpAdminString
_CfprApFirmwareUcscInfoVersion_Object = MibTableColumn
cfprApFirmwareUcscInfoVersion = _CfprApFirmwareUcscInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 67, 1, 6),
    _CfprApFirmwareUcscInfoVersion_Type()
)
cfprApFirmwareUcscInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUcscInfoVersion.setStatus("current")
_CfprApFirmwareUpdatableTable_Object = MibTable
cfprApFirmwareUpdatableTable = _CfprApFirmwareUpdatableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 68)
)
if mibBuilder.loadTexts:
    cfprApFirmwareUpdatableTable.setStatus("current")
_CfprApFirmwareUpdatableEntry_Object = MibTableRow
cfprApFirmwareUpdatableEntry = _CfprApFirmwareUpdatableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 68, 1)
)
cfprApFirmwareUpdatableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareUpdatableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareUpdatableEntry.setStatus("current")
_CfprApFirmwareUpdatableInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareUpdatableInstanceId_Object = MibTableColumn
cfprApFirmwareUpdatableInstanceId = _CfprApFirmwareUpdatableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 68, 1, 1),
    _CfprApFirmwareUpdatableInstanceId_Type()
)
cfprApFirmwareUpdatableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareUpdatableInstanceId.setStatus("current")
_CfprApFirmwareUpdatableDn_Type = CfprApManagedObjectDn
_CfprApFirmwareUpdatableDn_Object = MibTableColumn
cfprApFirmwareUpdatableDn = _CfprApFirmwareUpdatableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 68, 1, 2),
    _CfprApFirmwareUpdatableDn_Type()
)
cfprApFirmwareUpdatableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpdatableDn.setStatus("current")
_CfprApFirmwareUpdatableRn_Type = SnmpAdminString
_CfprApFirmwareUpdatableRn_Object = MibTableColumn
cfprApFirmwareUpdatableRn = _CfprApFirmwareUpdatableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 68, 1, 3),
    _CfprApFirmwareUpdatableRn_Type()
)
cfprApFirmwareUpdatableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpdatableRn.setStatus("current")
_CfprApFirmwareUpdatableAdminState_Type = CfprApFirmwareTriggerState
_CfprApFirmwareUpdatableAdminState_Object = MibTableColumn
cfprApFirmwareUpdatableAdminState = _CfprApFirmwareUpdatableAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 68, 1, 4),
    _CfprApFirmwareUpdatableAdminState_Type()
)
cfprApFirmwareUpdatableAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpdatableAdminState.setStatus("current")
_CfprApFirmwareUpdatableDeployment_Type = CfprApFirmwareUpdatableDeployment
_CfprApFirmwareUpdatableDeployment_Object = MibTableColumn
cfprApFirmwareUpdatableDeployment = _CfprApFirmwareUpdatableDeployment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 68, 1, 5),
    _CfprApFirmwareUpdatableDeployment_Type()
)
cfprApFirmwareUpdatableDeployment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpdatableDeployment.setStatus("current")
_CfprApFirmwareUpdatableOperState_Type = CfprApFirmwareImageState
_CfprApFirmwareUpdatableOperState_Object = MibTableColumn
cfprApFirmwareUpdatableOperState = _CfprApFirmwareUpdatableOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 68, 1, 6),
    _CfprApFirmwareUpdatableOperState_Type()
)
cfprApFirmwareUpdatableOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpdatableOperState.setStatus("current")
_CfprApFirmwareUpdatableOperStateQual_Type = CfprApFirmwareImageError
_CfprApFirmwareUpdatableOperStateQual_Object = MibTableColumn
cfprApFirmwareUpdatableOperStateQual = _CfprApFirmwareUpdatableOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 68, 1, 7),
    _CfprApFirmwareUpdatableOperStateQual_Type()
)
cfprApFirmwareUpdatableOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpdatableOperStateQual.setStatus("current")
_CfprApFirmwareUpdatablePrevVersion_Type = SnmpAdminString
_CfprApFirmwareUpdatablePrevVersion_Object = MibTableColumn
cfprApFirmwareUpdatablePrevVersion = _CfprApFirmwareUpdatablePrevVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 68, 1, 8),
    _CfprApFirmwareUpdatablePrevVersion_Type()
)
cfprApFirmwareUpdatablePrevVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpdatablePrevVersion.setStatus("current")
_CfprApFirmwareUpdatableVersion_Type = SnmpAdminString
_CfprApFirmwareUpdatableVersion_Object = MibTableColumn
cfprApFirmwareUpdatableVersion = _CfprApFirmwareUpdatableVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 68, 1, 9),
    _CfprApFirmwareUpdatableVersion_Type()
)
cfprApFirmwareUpdatableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpdatableVersion.setStatus("current")
_CfprApFirmwareUpgradeConstraintTable_Object = MibTable
cfprApFirmwareUpgradeConstraintTable = _CfprApFirmwareUpgradeConstraintTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 69)
)
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeConstraintTable.setStatus("current")
_CfprApFirmwareUpgradeConstraintEntry_Object = MibTableRow
cfprApFirmwareUpgradeConstraintEntry = _CfprApFirmwareUpgradeConstraintEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 69, 1)
)
cfprApFirmwareUpgradeConstraintEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareUpgradeConstraintInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeConstraintEntry.setStatus("current")
_CfprApFirmwareUpgradeConstraintInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareUpgradeConstraintInstanceId_Object = MibTableColumn
cfprApFirmwareUpgradeConstraintInstanceId = _CfprApFirmwareUpgradeConstraintInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 69, 1, 1),
    _CfprApFirmwareUpgradeConstraintInstanceId_Type()
)
cfprApFirmwareUpgradeConstraintInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeConstraintInstanceId.setStatus("current")
_CfprApFirmwareUpgradeConstraintDn_Type = CfprApManagedObjectDn
_CfprApFirmwareUpgradeConstraintDn_Object = MibTableColumn
cfprApFirmwareUpgradeConstraintDn = _CfprApFirmwareUpgradeConstraintDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 69, 1, 2),
    _CfprApFirmwareUpgradeConstraintDn_Type()
)
cfprApFirmwareUpgradeConstraintDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeConstraintDn.setStatus("current")
_CfprApFirmwareUpgradeConstraintRn_Type = SnmpAdminString
_CfprApFirmwareUpgradeConstraintRn_Object = MibTableColumn
cfprApFirmwareUpgradeConstraintRn = _CfprApFirmwareUpgradeConstraintRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 69, 1, 3),
    _CfprApFirmwareUpgradeConstraintRn_Type()
)
cfprApFirmwareUpgradeConstraintRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeConstraintRn.setStatus("current")
_CfprApFirmwareUpgradeConstraintMinVer_Type = SnmpAdminString
_CfprApFirmwareUpgradeConstraintMinVer_Object = MibTableColumn
cfprApFirmwareUpgradeConstraintMinVer = _CfprApFirmwareUpgradeConstraintMinVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 69, 1, 4),
    _CfprApFirmwareUpgradeConstraintMinVer_Type()
)
cfprApFirmwareUpgradeConstraintMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeConstraintMinVer.setStatus("current")
_CfprApFirmwareUpgradeDetailTable_Object = MibTable
cfprApFirmwareUpgradeDetailTable = _CfprApFirmwareUpgradeDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 70)
)
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeDetailTable.setStatus("current")
_CfprApFirmwareUpgradeDetailEntry_Object = MibTableRow
cfprApFirmwareUpgradeDetailEntry = _CfprApFirmwareUpgradeDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 70, 1)
)
cfprApFirmwareUpgradeDetailEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareUpgradeDetailInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeDetailEntry.setStatus("current")
_CfprApFirmwareUpgradeDetailInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareUpgradeDetailInstanceId_Object = MibTableColumn
cfprApFirmwareUpgradeDetailInstanceId = _CfprApFirmwareUpgradeDetailInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 70, 1, 1),
    _CfprApFirmwareUpgradeDetailInstanceId_Type()
)
cfprApFirmwareUpgradeDetailInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeDetailInstanceId.setStatus("current")
_CfprApFirmwareUpgradeDetailDn_Type = CfprApManagedObjectDn
_CfprApFirmwareUpgradeDetailDn_Object = MibTableColumn
cfprApFirmwareUpgradeDetailDn = _CfprApFirmwareUpgradeDetailDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 70, 1, 2),
    _CfprApFirmwareUpgradeDetailDn_Type()
)
cfprApFirmwareUpgradeDetailDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeDetailDn.setStatus("current")
_CfprApFirmwareUpgradeDetailRn_Type = SnmpAdminString
_CfprApFirmwareUpgradeDetailRn_Object = MibTableColumn
cfprApFirmwareUpgradeDetailRn = _CfprApFirmwareUpgradeDetailRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 70, 1, 3),
    _CfprApFirmwareUpgradeDetailRn_Type()
)
cfprApFirmwareUpgradeDetailRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeDetailRn.setStatus("current")
_CfprApFirmwareUpgradeDetailCategory_Type = CfprApFirmwareUpgradeCategory
_CfprApFirmwareUpgradeDetailCategory_Object = MibTableColumn
cfprApFirmwareUpgradeDetailCategory = _CfprApFirmwareUpgradeDetailCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 70, 1, 4),
    _CfprApFirmwareUpgradeDetailCategory_Type()
)
cfprApFirmwareUpgradeDetailCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeDetailCategory.setStatus("current")
_CfprApFirmwareUpgradeDetailDescription_Type = SnmpAdminString
_CfprApFirmwareUpgradeDetailDescription_Object = MibTableColumn
cfprApFirmwareUpgradeDetailDescription = _CfprApFirmwareUpgradeDetailDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 70, 1, 5),
    _CfprApFirmwareUpgradeDetailDescription_Type()
)
cfprApFirmwareUpgradeDetailDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeDetailDescription.setStatus("current")
_CfprApFirmwareUpgradeDetailId_Type = Gauge32
_CfprApFirmwareUpgradeDetailId_Object = MibTableColumn
cfprApFirmwareUpgradeDetailId = _CfprApFirmwareUpgradeDetailId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 70, 1, 6),
    _CfprApFirmwareUpgradeDetailId_Type()
)
cfprApFirmwareUpgradeDetailId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeDetailId.setStatus("current")
_CfprApFirmwareUpgradeDetailSeverity_Type = CfprApFirmwareUpgradeSeverity
_CfprApFirmwareUpgradeDetailSeverity_Object = MibTableColumn
cfprApFirmwareUpgradeDetailSeverity = _CfprApFirmwareUpgradeDetailSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 70, 1, 7),
    _CfprApFirmwareUpgradeDetailSeverity_Type()
)
cfprApFirmwareUpgradeDetailSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeDetailSeverity.setStatus("current")
_CfprApFirmwareUpgradeInfoTable_Object = MibTable
cfprApFirmwareUpgradeInfoTable = _CfprApFirmwareUpgradeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 71)
)
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeInfoTable.setStatus("current")
_CfprApFirmwareUpgradeInfoEntry_Object = MibTableRow
cfprApFirmwareUpgradeInfoEntry = _CfprApFirmwareUpgradeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 71, 1)
)
cfprApFirmwareUpgradeInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FIRMWARE-MIB", "cfprApFirmwareUpgradeInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeInfoEntry.setStatus("current")
_CfprApFirmwareUpgradeInfoInstanceId_Type = CfprApManagedObjectId
_CfprApFirmwareUpgradeInfoInstanceId_Object = MibTableColumn
cfprApFirmwareUpgradeInfoInstanceId = _CfprApFirmwareUpgradeInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 71, 1, 1),
    _CfprApFirmwareUpgradeInfoInstanceId_Type()
)
cfprApFirmwareUpgradeInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeInfoInstanceId.setStatus("current")
_CfprApFirmwareUpgradeInfoDn_Type = CfprApManagedObjectDn
_CfprApFirmwareUpgradeInfoDn_Object = MibTableColumn
cfprApFirmwareUpgradeInfoDn = _CfprApFirmwareUpgradeInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 71, 1, 2),
    _CfprApFirmwareUpgradeInfoDn_Type()
)
cfprApFirmwareUpgradeInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeInfoDn.setStatus("current")
_CfprApFirmwareUpgradeInfoRn_Type = SnmpAdminString
_CfprApFirmwareUpgradeInfoRn_Object = MibTableColumn
cfprApFirmwareUpgradeInfoRn = _CfprApFirmwareUpgradeInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 71, 1, 3),
    _CfprApFirmwareUpgradeInfoRn_Type()
)
cfprApFirmwareUpgradeInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeInfoRn.setStatus("current")
_CfprApFirmwareUpgradeInfoMessage_Type = SnmpAdminString
_CfprApFirmwareUpgradeInfoMessage_Object = MibTableColumn
cfprApFirmwareUpgradeInfoMessage = _CfprApFirmwareUpgradeInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 71, 1, 4),
    _CfprApFirmwareUpgradeInfoMessage_Type()
)
cfprApFirmwareUpgradeInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeInfoMessage.setStatus("current")
_CfprApFirmwareUpgradeInfoTimeStamp_Type = DateAndTime
_CfprApFirmwareUpgradeInfoTimeStamp_Object = MibTableColumn
cfprApFirmwareUpgradeInfoTimeStamp = _CfprApFirmwareUpgradeInfoTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 71, 1, 5),
    _CfprApFirmwareUpgradeInfoTimeStamp_Type()
)
cfprApFirmwareUpgradeInfoTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeInfoTimeStamp.setStatus("current")
_CfprApFirmwareUpgradeInfoValidateStatus_Type = CfprApFirmwareUpgradeStatus
_CfprApFirmwareUpgradeInfoValidateStatus_Object = MibTableColumn
cfprApFirmwareUpgradeInfoValidateStatus = _CfprApFirmwareUpgradeInfoValidateStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 71, 1, 6),
    _CfprApFirmwareUpgradeInfoValidateStatus_Type()
)
cfprApFirmwareUpgradeInfoValidateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeInfoValidateStatus.setStatus("current")
_CfprApFirmwareUpgradeInfoVersion_Type = SnmpAdminString
_CfprApFirmwareUpgradeInfoVersion_Object = MibTableColumn
cfprApFirmwareUpgradeInfoVersion = _CfprApFirmwareUpgradeInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 30, 71, 1, 7),
    _CfprApFirmwareUpgradeInfoVersion_Type()
)
cfprApFirmwareUpgradeInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFirmwareUpgradeInfoVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-FIRMWARE-MIB",
    **{"cfprApFirmwareObjects": cfprApFirmwareObjects,
       "cfprApFirmwareAckTable": cfprApFirmwareAckTable,
       "cfprApFirmwareAckEntry": cfprApFirmwareAckEntry,
       "cfprApFirmwareAckInstanceId": cfprApFirmwareAckInstanceId,
       "cfprApFirmwareAckDn": cfprApFirmwareAckDn,
       "cfprApFirmwareAckRn": cfprApFirmwareAckRn,
       "cfprApFirmwareAckAcked": cfprApFirmwareAckAcked,
       "cfprApFirmwareAckAckedBy": cfprApFirmwareAckAckedBy,
       "cfprApFirmwareAckAdminState": cfprApFirmwareAckAdminState,
       "cfprApFirmwareAckAutoDelete": cfprApFirmwareAckAutoDelete,
       "cfprApFirmwareAckChangeBy": cfprApFirmwareAckChangeBy,
       "cfprApFirmwareAckChangeDetails": cfprApFirmwareAckChangeDetails,
       "cfprApFirmwareAckChanges": cfprApFirmwareAckChanges,
       "cfprApFirmwareAckDescr": cfprApFirmwareAckDescr,
       "cfprApFirmwareAckDisr": cfprApFirmwareAckDisr,
       "cfprApFirmwareAckIgnoreCap": cfprApFirmwareAckIgnoreCap,
       "cfprApFirmwareAckIntId": cfprApFirmwareAckIntId,
       "cfprApFirmwareAckModified": cfprApFirmwareAckModified,
       "cfprApFirmwareAckName": cfprApFirmwareAckName,
       "cfprApFirmwareAckOperScheduler": cfprApFirmwareAckOperScheduler,
       "cfprApFirmwareAckOperState": cfprApFirmwareAckOperState,
       "cfprApFirmwareAckPolicyLevel": cfprApFirmwareAckPolicyLevel,
       "cfprApFirmwareAckPolicyOwner": cfprApFirmwareAckPolicyOwner,
       "cfprApFirmwareAckPrevOperState": cfprApFirmwareAckPrevOperState,
       "cfprApFirmwareAckScheduler": cfprApFirmwareAckScheduler,
       "cfprApFirmwareAutoSyncPolicyTable": cfprApFirmwareAutoSyncPolicyTable,
       "cfprApFirmwareAutoSyncPolicyEntry": cfprApFirmwareAutoSyncPolicyEntry,
       "cfprApFirmwareAutoSyncPolicyInstanceId": cfprApFirmwareAutoSyncPolicyInstanceId,
       "cfprApFirmwareAutoSyncPolicyDn": cfprApFirmwareAutoSyncPolicyDn,
       "cfprApFirmwareAutoSyncPolicyRn": cfprApFirmwareAutoSyncPolicyRn,
       "cfprApFirmwareAutoSyncPolicyConfigIssue": cfprApFirmwareAutoSyncPolicyConfigIssue,
       "cfprApFirmwareAutoSyncPolicyDescr": cfprApFirmwareAutoSyncPolicyDescr,
       "cfprApFirmwareAutoSyncPolicyIntId": cfprApFirmwareAutoSyncPolicyIntId,
       "cfprApFirmwareAutoSyncPolicyName": cfprApFirmwareAutoSyncPolicyName,
       "cfprApFirmwareAutoSyncPolicyPolicyLevel": cfprApFirmwareAutoSyncPolicyPolicyLevel,
       "cfprApFirmwareAutoSyncPolicyPolicyOwner": cfprApFirmwareAutoSyncPolicyPolicyOwner,
       "cfprApFirmwareAutoSyncPolicySyncState": cfprApFirmwareAutoSyncPolicySyncState,
       "cfprApFirmwareBladeTable": cfprApFirmwareBladeTable,
       "cfprApFirmwareBladeEntry": cfprApFirmwareBladeEntry,
       "cfprApFirmwareBladeInstanceId": cfprApFirmwareBladeInstanceId,
       "cfprApFirmwareBladeDn": cfprApFirmwareBladeDn,
       "cfprApFirmwareBladeRn": cfprApFirmwareBladeRn,
       "cfprApFirmwareBladeOperVersion": cfprApFirmwareBladeOperVersion,
       "cfprApFirmwareBootDefinitionTable": cfprApFirmwareBootDefinitionTable,
       "cfprApFirmwareBootDefinitionEntry": cfprApFirmwareBootDefinitionEntry,
       "cfprApFirmwareBootDefinitionInstanceId": cfprApFirmwareBootDefinitionInstanceId,
       "cfprApFirmwareBootDefinitionDn": cfprApFirmwareBootDefinitionDn,
       "cfprApFirmwareBootDefinitionRn": cfprApFirmwareBootDefinitionRn,
       "cfprApFirmwareBootDefinitionType": cfprApFirmwareBootDefinitionType,
       "cfprApFirmwareBootUnitTable": cfprApFirmwareBootUnitTable,
       "cfprApFirmwareBootUnitEntry": cfprApFirmwareBootUnitEntry,
       "cfprApFirmwareBootUnitInstanceId": cfprApFirmwareBootUnitInstanceId,
       "cfprApFirmwareBootUnitDn": cfprApFirmwareBootUnitDn,
       "cfprApFirmwareBootUnitRn": cfprApFirmwareBootUnitRn,
       "cfprApFirmwareBootUnitAdminState": cfprApFirmwareBootUnitAdminState,
       "cfprApFirmwareBootUnitIgnoreCompCheck": cfprApFirmwareBootUnitIgnoreCompCheck,
       "cfprApFirmwareBootUnitImage": cfprApFirmwareBootUnitImage,
       "cfprApFirmwareBootUnitInvTag": cfprApFirmwareBootUnitInvTag,
       "cfprApFirmwareBootUnitMode": cfprApFirmwareBootUnitMode,
       "cfprApFirmwareBootUnitOperState": cfprApFirmwareBootUnitOperState,
       "cfprApFirmwareBootUnitPrevVersion": cfprApFirmwareBootUnitPrevVersion,
       "cfprApFirmwareBootUnitResetOnActivate": cfprApFirmwareBootUnitResetOnActivate,
       "cfprApFirmwareBootUnitSkipValidation": cfprApFirmwareBootUnitSkipValidation,
       "cfprApFirmwareBootUnitType": cfprApFirmwareBootUnitType,
       "cfprApFirmwareBootUnitVersion": cfprApFirmwareBootUnitVersion,
       "cfprApFirmwareBundleInfoTable": cfprApFirmwareBundleInfoTable,
       "cfprApFirmwareBundleInfoEntry": cfprApFirmwareBundleInfoEntry,
       "cfprApFirmwareBundleInfoInstanceId": cfprApFirmwareBundleInfoInstanceId,
       "cfprApFirmwareBundleInfoDn": cfprApFirmwareBundleInfoDn,
       "cfprApFirmwareBundleInfoRn": cfprApFirmwareBundleInfoRn,
       "cfprApFirmwareBundleInfoType": cfprApFirmwareBundleInfoType,
       "cfprApFirmwareBundleInfoVersion": cfprApFirmwareBundleInfoVersion,
       "cfprApFirmwareBundleInfoDigestTable": cfprApFirmwareBundleInfoDigestTable,
       "cfprApFirmwareBundleInfoDigestEntry": cfprApFirmwareBundleInfoDigestEntry,
       "cfprApFirmwareBundleInfoDigestInstanceId": cfprApFirmwareBundleInfoDigestInstanceId,
       "cfprApFirmwareBundleInfoDigestDn": cfprApFirmwareBundleInfoDigestDn,
       "cfprApFirmwareBundleInfoDigestRn": cfprApFirmwareBundleInfoDigestRn,
       "cfprApFirmwareBundleInfoDigestBundleName": cfprApFirmwareBundleInfoDigestBundleName,
       "cfprApFirmwareBundleInfoDigestType": cfprApFirmwareBundleInfoDigestType,
       "cfprApFirmwareBundleInfoDigestVersion": cfprApFirmwareBundleInfoDigestVersion,
       "cfprApFirmwareBundleTypeTable": cfprApFirmwareBundleTypeTable,
       "cfprApFirmwareBundleTypeEntry": cfprApFirmwareBundleTypeEntry,
       "cfprApFirmwareBundleTypeInstanceId": cfprApFirmwareBundleTypeInstanceId,
       "cfprApFirmwareBundleTypeDn": cfprApFirmwareBundleTypeDn,
       "cfprApFirmwareBundleTypeRn": cfprApFirmwareBundleTypeRn,
       "cfprApFirmwareBundleTypeInvTag": cfprApFirmwareBundleTypeInvTag,
       "cfprApFirmwareBundleTypeType": cfprApFirmwareBundleTypeType,
       "cfprApFirmwareBundleTypeCapProviderTable": cfprApFirmwareBundleTypeCapProviderTable,
       "cfprApFirmwareBundleTypeCapProviderEntry": cfprApFirmwareBundleTypeCapProviderEntry,
       "cfprApFirmwareBundleTypeCapProviderInstanceId": cfprApFirmwareBundleTypeCapProviderInstanceId,
       "cfprApFirmwareBundleTypeCapProviderDn": cfprApFirmwareBundleTypeCapProviderDn,
       "cfprApFirmwareBundleTypeCapProviderRn": cfprApFirmwareBundleTypeCapProviderRn,
       "cfprApFirmwareBundleTypeCapProviderDeleted": cfprApFirmwareBundleTypeCapProviderDeleted,
       "cfprApFirmwareBundleTypeCapProviderDeprecated": cfprApFirmwareBundleTypeCapProviderDeprecated,
       "cfprApFirmwareBundleTypeCapProviderElementLoadFailures": cfprApFirmwareBundleTypeCapProviderElementLoadFailures,
       "cfprApFirmwareBundleTypeCapProviderElementsLoaded": cfprApFirmwareBundleTypeCapProviderElementsLoaded,
       "cfprApFirmwareBundleTypeCapProviderGencount": cfprApFirmwareBundleTypeCapProviderGencount,
       "cfprApFirmwareBundleTypeCapProviderLoadErrors": cfprApFirmwareBundleTypeCapProviderLoadErrors,
       "cfprApFirmwareBundleTypeCapProviderLoadWarnings": cfprApFirmwareBundleTypeCapProviderLoadWarnings,
       "cfprApFirmwareBundleTypeCapProviderMgmtPlaneVer": cfprApFirmwareBundleTypeCapProviderMgmtPlaneVer,
       "cfprApFirmwareBundleTypeCapProviderModel": cfprApFirmwareBundleTypeCapProviderModel,
       "cfprApFirmwareBundleTypeCapProviderPlatformType": cfprApFirmwareBundleTypeCapProviderPlatformType,
       "cfprApFirmwareBundleTypeCapProviderVendor": cfprApFirmwareBundleTypeCapProviderVendor,
       "cfprApFirmwareCatalogPackTable": cfprApFirmwareCatalogPackTable,
       "cfprApFirmwareCatalogPackEntry": cfprApFirmwareCatalogPackEntry,
       "cfprApFirmwareCatalogPackInstanceId": cfprApFirmwareCatalogPackInstanceId,
       "cfprApFirmwareCatalogPackDn": cfprApFirmwareCatalogPackDn,
       "cfprApFirmwareCatalogPackRn": cfprApFirmwareCatalogPackRn,
       "cfprApFirmwareCatalogPackCatalogName": cfprApFirmwareCatalogPackCatalogName,
       "cfprApFirmwareCatalogPackCatalogVersion": cfprApFirmwareCatalogPackCatalogVersion,
       "cfprApFirmwareCatalogPackConfigState": cfprApFirmwareCatalogPackConfigState,
       "cfprApFirmwareCatalogPackConfigStatusMessage": cfprApFirmwareCatalogPackConfigStatusMessage,
       "cfprApFirmwareCatalogPackDescr": cfprApFirmwareCatalogPackDescr,
       "cfprApFirmwareCatalogPackIntId": cfprApFirmwareCatalogPackIntId,
       "cfprApFirmwareCatalogPackMode": cfprApFirmwareCatalogPackMode,
       "cfprApFirmwareCatalogPackName": cfprApFirmwareCatalogPackName,
       "cfprApFirmwareCatalogPackPolicyLevel": cfprApFirmwareCatalogPackPolicyLevel,
       "cfprApFirmwareCatalogPackPolicyOwner": cfprApFirmwareCatalogPackPolicyOwner,
       "cfprApFirmwareCatalogPackStageSize": cfprApFirmwareCatalogPackStageSize,
       "cfprApFirmwareCatalogPackUpdateTrigger": cfprApFirmwareCatalogPackUpdateTrigger,
       "cfprApFirmwareCatalogueTable": cfprApFirmwareCatalogueTable,
       "cfprApFirmwareCatalogueEntry": cfprApFirmwareCatalogueEntry,
       "cfprApFirmwareCatalogueInstanceId": cfprApFirmwareCatalogueInstanceId,
       "cfprApFirmwareCatalogueDn": cfprApFirmwareCatalogueDn,
       "cfprApFirmwareCatalogueRn": cfprApFirmwareCatalogueRn,
       "cfprApFirmwareCatalogueSyncTrigger": cfprApFirmwareCatalogueSyncTrigger,
       "cfprApFirmwareCompSourceTable": cfprApFirmwareCompSourceTable,
       "cfprApFirmwareCompSourceEntry": cfprApFirmwareCompSourceEntry,
       "cfprApFirmwareCompSourceInstanceId": cfprApFirmwareCompSourceInstanceId,
       "cfprApFirmwareCompSourceDn": cfprApFirmwareCompSourceDn,
       "cfprApFirmwareCompSourceRn": cfprApFirmwareCompSourceRn,
       "cfprApFirmwareCompSourceDescr": cfprApFirmwareCompSourceDescr,
       "cfprApFirmwareCompSourceIntId": cfprApFirmwareCompSourceIntId,
       "cfprApFirmwareCompSourceInvTag": cfprApFirmwareCompSourceInvTag,
       "cfprApFirmwareCompSourceName": cfprApFirmwareCompSourceName,
       "cfprApFirmwareCompSourcePolicyLevel": cfprApFirmwareCompSourcePolicyLevel,
       "cfprApFirmwareCompSourcePolicyOwner": cfprApFirmwareCompSourcePolicyOwner,
       "cfprApFirmwareCompSourceVersion": cfprApFirmwareCompSourceVersion,
       "cfprApFirmwareCompTargetTable": cfprApFirmwareCompTargetTable,
       "cfprApFirmwareCompTargetEntry": cfprApFirmwareCompTargetEntry,
       "cfprApFirmwareCompTargetInstanceId": cfprApFirmwareCompTargetInstanceId,
       "cfprApFirmwareCompTargetDn": cfprApFirmwareCompTargetDn,
       "cfprApFirmwareCompTargetRn": cfprApFirmwareCompTargetRn,
       "cfprApFirmwareCompTargetDescr": cfprApFirmwareCompTargetDescr,
       "cfprApFirmwareCompTargetIntId": cfprApFirmwareCompTargetIntId,
       "cfprApFirmwareCompTargetInvTag": cfprApFirmwareCompTargetInvTag,
       "cfprApFirmwareCompTargetName": cfprApFirmwareCompTargetName,
       "cfprApFirmwareCompTargetPolicyLevel": cfprApFirmwareCompTargetPolicyLevel,
       "cfprApFirmwareCompTargetPolicyOwner": cfprApFirmwareCompTargetPolicyOwner,
       "cfprApFirmwareCompTargetVersion": cfprApFirmwareCompTargetVersion,
       "cfprApFirmwareComputeHostPackTable": cfprApFirmwareComputeHostPackTable,
       "cfprApFirmwareComputeHostPackEntry": cfprApFirmwareComputeHostPackEntry,
       "cfprApFirmwareComputeHostPackInstanceId": cfprApFirmwareComputeHostPackInstanceId,
       "cfprApFirmwareComputeHostPackDn": cfprApFirmwareComputeHostPackDn,
       "cfprApFirmwareComputeHostPackRn": cfprApFirmwareComputeHostPackRn,
       "cfprApFirmwareComputeHostPackBladeBundleName": cfprApFirmwareComputeHostPackBladeBundleName,
       "cfprApFirmwareComputeHostPackBladeBundleVersion": cfprApFirmwareComputeHostPackBladeBundleVersion,
       "cfprApFirmwareComputeHostPackConfigQualifier": cfprApFirmwareComputeHostPackConfigQualifier,
       "cfprApFirmwareComputeHostPackDescr": cfprApFirmwareComputeHostPackDescr,
       "cfprApFirmwareComputeHostPackIgnoreCompCheck": cfprApFirmwareComputeHostPackIgnoreCompCheck,
       "cfprApFirmwareComputeHostPackIntId": cfprApFirmwareComputeHostPackIntId,
       "cfprApFirmwareComputeHostPackMode": cfprApFirmwareComputeHostPackMode,
       "cfprApFirmwareComputeHostPackName": cfprApFirmwareComputeHostPackName,
       "cfprApFirmwareComputeHostPackPlatformBundleVersion": cfprApFirmwareComputeHostPackPlatformBundleVersion,
       "cfprApFirmwareComputeHostPackPolicyLevel": cfprApFirmwareComputeHostPackPolicyLevel,
       "cfprApFirmwareComputeHostPackPolicyOwner": cfprApFirmwareComputeHostPackPolicyOwner,
       "cfprApFirmwareComputeHostPackRackBundleName": cfprApFirmwareComputeHostPackRackBundleName,
       "cfprApFirmwareComputeHostPackRackBundleVersion": cfprApFirmwareComputeHostPackRackBundleVersion,
       "cfprApFirmwareComputeHostPackStageSize": cfprApFirmwareComputeHostPackStageSize,
       "cfprApFirmwareComputeHostPackUpdateTrigger": cfprApFirmwareComputeHostPackUpdateTrigger,
       "cfprApFirmwareComputeMgmtPackTable": cfprApFirmwareComputeMgmtPackTable,
       "cfprApFirmwareComputeMgmtPackEntry": cfprApFirmwareComputeMgmtPackEntry,
       "cfprApFirmwareComputeMgmtPackInstanceId": cfprApFirmwareComputeMgmtPackInstanceId,
       "cfprApFirmwareComputeMgmtPackDn": cfprApFirmwareComputeMgmtPackDn,
       "cfprApFirmwareComputeMgmtPackRn": cfprApFirmwareComputeMgmtPackRn,
       "cfprApFirmwareComputeMgmtPackDescr": cfprApFirmwareComputeMgmtPackDescr,
       "cfprApFirmwareComputeMgmtPackIgnoreCompCheck": cfprApFirmwareComputeMgmtPackIgnoreCompCheck,
       "cfprApFirmwareComputeMgmtPackIntId": cfprApFirmwareComputeMgmtPackIntId,
       "cfprApFirmwareComputeMgmtPackMode": cfprApFirmwareComputeMgmtPackMode,
       "cfprApFirmwareComputeMgmtPackName": cfprApFirmwareComputeMgmtPackName,
       "cfprApFirmwareComputeMgmtPackPolicyLevel": cfprApFirmwareComputeMgmtPackPolicyLevel,
       "cfprApFirmwareComputeMgmtPackPolicyOwner": cfprApFirmwareComputeMgmtPackPolicyOwner,
       "cfprApFirmwareComputeMgmtPackStageSize": cfprApFirmwareComputeMgmtPackStageSize,
       "cfprApFirmwareComputeMgmtPackUpdateTrigger": cfprApFirmwareComputeMgmtPackUpdateTrigger,
       "cfprApFirmwareConstraintTable": cfprApFirmwareConstraintTable,
       "cfprApFirmwareConstraintEntry": cfprApFirmwareConstraintEntry,
       "cfprApFirmwareConstraintInstanceId": cfprApFirmwareConstraintInstanceId,
       "cfprApFirmwareConstraintDn": cfprApFirmwareConstraintDn,
       "cfprApFirmwareConstraintRn": cfprApFirmwareConstraintRn,
       "cfprApFirmwareConstraintFeature": cfprApFirmwareConstraintFeature,
       "cfprApFirmwareConstraintMinBiosVersion": cfprApFirmwareConstraintMinBiosVersion,
       "cfprApFirmwareConstraintMinCimcVersion": cfprApFirmwareConstraintMinCimcVersion,
       "cfprApFirmwareConstraintsTable": cfprApFirmwareConstraintsTable,
       "cfprApFirmwareConstraintsEntry": cfprApFirmwareConstraintsEntry,
       "cfprApFirmwareConstraintsInstanceId": cfprApFirmwareConstraintsInstanceId,
       "cfprApFirmwareConstraintsDn": cfprApFirmwareConstraintsDn,
       "cfprApFirmwareConstraintsRn": cfprApFirmwareConstraintsRn,
       "cfprApFirmwareCspAppListTable": cfprApFirmwareCspAppListTable,
       "cfprApFirmwareCspAppListEntry": cfprApFirmwareCspAppListEntry,
       "cfprApFirmwareCspAppListInstanceId": cfprApFirmwareCspAppListInstanceId,
       "cfprApFirmwareCspAppListDn": cfprApFirmwareCspAppListDn,
       "cfprApFirmwareCspAppListRn": cfprApFirmwareCspAppListRn,
       "cfprApFirmwareCspAppListName": cfprApFirmwareCspAppListName,
       "cfprApFirmwareCspVersionTable": cfprApFirmwareCspVersionTable,
       "cfprApFirmwareCspVersionEntry": cfprApFirmwareCspVersionEntry,
       "cfprApFirmwareCspVersionInstanceId": cfprApFirmwareCspVersionInstanceId,
       "cfprApFirmwareCspVersionDn": cfprApFirmwareCspVersionDn,
       "cfprApFirmwareCspVersionRn": cfprApFirmwareCspVersionRn,
       "cfprApFirmwareCspVersionAppName": cfprApFirmwareCspVersionAppName,
       "cfprApFirmwareCspVersionFromVersion": cfprApFirmwareCspVersionFromVersion,
       "cfprApFirmwareCspVersionName": cfprApFirmwareCspVersionName,
       "cfprApFirmwareCspVersionToVersion": cfprApFirmwareCspVersionToVersion,
       "cfprApFirmwareDependencyTable": cfprApFirmwareDependencyTable,
       "cfprApFirmwareDependencyEntry": cfprApFirmwareDependencyEntry,
       "cfprApFirmwareDependencyInstanceId": cfprApFirmwareDependencyInstanceId,
       "cfprApFirmwareDependencyDn": cfprApFirmwareDependencyDn,
       "cfprApFirmwareDependencyRn": cfprApFirmwareDependencyRn,
       "cfprApFirmwareDependencyEp": cfprApFirmwareDependencyEp,
       "cfprApFirmwareDependencyHwModel": cfprApFirmwareDependencyHwModel,
       "cfprApFirmwareDependencyHwRevision": cfprApFirmwareDependencyHwRevision,
       "cfprApFirmwareDependencyHwVendor": cfprApFirmwareDependencyHwVendor,
       "cfprApFirmwareDependencyInvTag": cfprApFirmwareDependencyInvTag,
       "cfprApFirmwareDependencyMaxVer": cfprApFirmwareDependencyMaxVer,
       "cfprApFirmwareDependencyMinVer": cfprApFirmwareDependencyMinVer,
       "cfprApFirmwareDependencyRelationship": cfprApFirmwareDependencyRelationship,
       "cfprApFirmwareDependencyScope": cfprApFirmwareDependencyScope,
       "cfprApFirmwareDependencySensitivity": cfprApFirmwareDependencySensitivity,
       "cfprApFirmwareDistCspBlackListTable": cfprApFirmwareDistCspBlackListTable,
       "cfprApFirmwareDistCspBlackListEntry": cfprApFirmwareDistCspBlackListEntry,
       "cfprApFirmwareDistCspBlackListInstanceId": cfprApFirmwareDistCspBlackListInstanceId,
       "cfprApFirmwareDistCspBlackListDn": cfprApFirmwareDistCspBlackListDn,
       "cfprApFirmwareDistCspBlackListRn": cfprApFirmwareDistCspBlackListRn,
       "cfprApFirmwareDistCspBlackListName": cfprApFirmwareDistCspBlackListName,
       "cfprApFirmwareDistCspBlackListTimeStamp": cfprApFirmwareDistCspBlackListTimeStamp,
       "cfprApFirmwareDistCspBlackListVersion": cfprApFirmwareDistCspBlackListVersion,
       "cfprApFirmwareDistImageTable": cfprApFirmwareDistImageTable,
       "cfprApFirmwareDistImageEntry": cfprApFirmwareDistImageEntry,
       "cfprApFirmwareDistImageInstanceId": cfprApFirmwareDistImageInstanceId,
       "cfprApFirmwareDistImageDn": cfprApFirmwareDistImageDn,
       "cfprApFirmwareDistImageRn": cfprApFirmwareDistImageRn,
       "cfprApFirmwareDistImageImageDeleted": cfprApFirmwareDistImageImageDeleted,
       "cfprApFirmwareDistImageName": cfprApFirmwareDistImageName,
       "cfprApFirmwareDistImageType": cfprApFirmwareDistImageType,
       "cfprApFirmwareDistributableTable": cfprApFirmwareDistributableTable,
       "cfprApFirmwareDistributableEntry": cfprApFirmwareDistributableEntry,
       "cfprApFirmwareDistributableInstanceId": cfprApFirmwareDistributableInstanceId,
       "cfprApFirmwareDistributableDn": cfprApFirmwareDistributableDn,
       "cfprApFirmwareDistributableRn": cfprApFirmwareDistributableRn,
       "cfprApFirmwareDistributableAdminState": cfprApFirmwareDistributableAdminState,
       "cfprApFirmwareDistributableBuildDate": cfprApFirmwareDistributableBuildDate,
       "cfprApFirmwareDistributableCompleteness": cfprApFirmwareDistributableCompleteness,
       "cfprApFirmwareDistributableDescr": cfprApFirmwareDistributableDescr,
       "cfprApFirmwareDistributableDisplayFlag": cfprApFirmwareDistributableDisplayFlag,
       "cfprApFirmwareDistributableFsmDescr": cfprApFirmwareDistributableFsmDescr,
       "cfprApFirmwareDistributableFsmPrev": cfprApFirmwareDistributableFsmPrev,
       "cfprApFirmwareDistributableFsmProgr": cfprApFirmwareDistributableFsmProgr,
       "cfprApFirmwareDistributableFsmRmtInvErrCode": cfprApFirmwareDistributableFsmRmtInvErrCode,
       "cfprApFirmwareDistributableFsmRmtInvErrDescr": cfprApFirmwareDistributableFsmRmtInvErrDescr,
       "cfprApFirmwareDistributableFsmRmtInvRslt": cfprApFirmwareDistributableFsmRmtInvRslt,
       "cfprApFirmwareDistributableFsmStageDescr": cfprApFirmwareDistributableFsmStageDescr,
       "cfprApFirmwareDistributableFsmStamp": cfprApFirmwareDistributableFsmStamp,
       "cfprApFirmwareDistributableFsmStatus": cfprApFirmwareDistributableFsmStatus,
       "cfprApFirmwareDistributableFsmTry": cfprApFirmwareDistributableFsmTry,
       "cfprApFirmwareDistributableImagePresence": cfprApFirmwareDistributableImagePresence,
       "cfprApFirmwareDistributableIntId": cfprApFirmwareDistributableIntId,
       "cfprApFirmwareDistributableInvTag": cfprApFirmwareDistributableInvTag,
       "cfprApFirmwareDistributableModel": cfprApFirmwareDistributableModel,
       "cfprApFirmwareDistributableName": cfprApFirmwareDistributableName,
       "cfprApFirmwareDistributablePlatformVersion": cfprApFirmwareDistributablePlatformVersion,
       "cfprApFirmwareDistributablePolicyLevel": cfprApFirmwareDistributablePolicyLevel,
       "cfprApFirmwareDistributablePolicyOwner": cfprApFirmwareDistributablePolicyOwner,
       "cfprApFirmwareDistributableTimeStamp": cfprApFirmwareDistributableTimeStamp,
       "cfprApFirmwareDistributableTransferState": cfprApFirmwareDistributableTransferState,
       "cfprApFirmwareDistributableType": cfprApFirmwareDistributableType,
       "cfprApFirmwareDistributableVendor": cfprApFirmwareDistributableVendor,
       "cfprApFirmwareDistributableVersion": cfprApFirmwareDistributableVersion,
       "cfprApFirmwareDistributableFsmTable": cfprApFirmwareDistributableFsmTable,
       "cfprApFirmwareDistributableFsmEntry": cfprApFirmwareDistributableFsmEntry,
       "cfprApFirmwareDistributableFsmInstanceId": cfprApFirmwareDistributableFsmInstanceId,
       "cfprApFirmwareDistributableFsmDn": cfprApFirmwareDistributableFsmDn,
       "cfprApFirmwareDistributableFsmRn": cfprApFirmwareDistributableFsmRn,
       "cfprApFirmwareDistributableFsmCompletionTime": cfprApFirmwareDistributableFsmCompletionTime,
       "cfprApFirmwareDistributableFsmCurrentFsm": cfprApFirmwareDistributableFsmCurrentFsm,
       "cfprApFirmwareDistributableFsmDescrData": cfprApFirmwareDistributableFsmDescrData,
       "cfprApFirmwareDistributableFsmFsmStatus": cfprApFirmwareDistributableFsmFsmStatus,
       "cfprApFirmwareDistributableFsmProgress": cfprApFirmwareDistributableFsmProgress,
       "cfprApFirmwareDistributableFsmRmtErrCode": cfprApFirmwareDistributableFsmRmtErrCode,
       "cfprApFirmwareDistributableFsmRmtErrDescr": cfprApFirmwareDistributableFsmRmtErrDescr,
       "cfprApFirmwareDistributableFsmRmtRslt": cfprApFirmwareDistributableFsmRmtRslt,
       "cfprApFirmwareDistributableFsmStageTable": cfprApFirmwareDistributableFsmStageTable,
       "cfprApFirmwareDistributableFsmStageEntry": cfprApFirmwareDistributableFsmStageEntry,
       "cfprApFirmwareDistributableFsmStageInstanceId": cfprApFirmwareDistributableFsmStageInstanceId,
       "cfprApFirmwareDistributableFsmStageDn": cfprApFirmwareDistributableFsmStageDn,
       "cfprApFirmwareDistributableFsmStageRn": cfprApFirmwareDistributableFsmStageRn,
       "cfprApFirmwareDistributableFsmStageDescrData": cfprApFirmwareDistributableFsmStageDescrData,
       "cfprApFirmwareDistributableFsmStageLastUpdateTime": cfprApFirmwareDistributableFsmStageLastUpdateTime,
       "cfprApFirmwareDistributableFsmStageName": cfprApFirmwareDistributableFsmStageName,
       "cfprApFirmwareDistributableFsmStageOrder": cfprApFirmwareDistributableFsmStageOrder,
       "cfprApFirmwareDistributableFsmStageRetry": cfprApFirmwareDistributableFsmStageRetry,
       "cfprApFirmwareDistributableFsmStageStageStatus": cfprApFirmwareDistributableFsmStageStageStatus,
       "cfprApFirmwareDistributableFsmTaskTable": cfprApFirmwareDistributableFsmTaskTable,
       "cfprApFirmwareDistributableFsmTaskEntry": cfprApFirmwareDistributableFsmTaskEntry,
       "cfprApFirmwareDistributableFsmTaskInstanceId": cfprApFirmwareDistributableFsmTaskInstanceId,
       "cfprApFirmwareDistributableFsmTaskDn": cfprApFirmwareDistributableFsmTaskDn,
       "cfprApFirmwareDistributableFsmTaskRn": cfprApFirmwareDistributableFsmTaskRn,
       "cfprApFirmwareDistributableFsmTaskCompletion": cfprApFirmwareDistributableFsmTaskCompletion,
       "cfprApFirmwareDistributableFsmTaskFlags": cfprApFirmwareDistributableFsmTaskFlags,
       "cfprApFirmwareDistributableFsmTaskItem": cfprApFirmwareDistributableFsmTaskItem,
       "cfprApFirmwareDistributableFsmTaskSeqId": cfprApFirmwareDistributableFsmTaskSeqId,
       "cfprApFirmwareDownloaderTable": cfprApFirmwareDownloaderTable,
       "cfprApFirmwareDownloaderEntry": cfprApFirmwareDownloaderEntry,
       "cfprApFirmwareDownloaderInstanceId": cfprApFirmwareDownloaderInstanceId,
       "cfprApFirmwareDownloaderDn": cfprApFirmwareDownloaderDn,
       "cfprApFirmwareDownloaderRn": cfprApFirmwareDownloaderRn,
       "cfprApFirmwareDownloaderAdminState": cfprApFirmwareDownloaderAdminState,
       "cfprApFirmwareDownloaderFileName": cfprApFirmwareDownloaderFileName,
       "cfprApFirmwareDownloaderFsmDescr": cfprApFirmwareDownloaderFsmDescr,
       "cfprApFirmwareDownloaderFsmPrev": cfprApFirmwareDownloaderFsmPrev,
       "cfprApFirmwareDownloaderFsmProgr": cfprApFirmwareDownloaderFsmProgr,
       "cfprApFirmwareDownloaderFsmRmtInvErrCode": cfprApFirmwareDownloaderFsmRmtInvErrCode,
       "cfprApFirmwareDownloaderFsmRmtInvErrDescr": cfprApFirmwareDownloaderFsmRmtInvErrDescr,
       "cfprApFirmwareDownloaderFsmRmtInvRslt": cfprApFirmwareDownloaderFsmRmtInvRslt,
       "cfprApFirmwareDownloaderFsmStageDescr": cfprApFirmwareDownloaderFsmStageDescr,
       "cfprApFirmwareDownloaderFsmStamp": cfprApFirmwareDownloaderFsmStamp,
       "cfprApFirmwareDownloaderFsmStatus": cfprApFirmwareDownloaderFsmStatus,
       "cfprApFirmwareDownloaderFsmTry": cfprApFirmwareDownloaderFsmTry,
       "cfprApFirmwareDownloaderImageSize": cfprApFirmwareDownloaderImageSize,
       "cfprApFirmwareDownloaderPort": cfprApFirmwareDownloaderPort,
       "cfprApFirmwareDownloaderProtocol": cfprApFirmwareDownloaderProtocol,
       "cfprApFirmwareDownloaderPwd": cfprApFirmwareDownloaderPwd,
       "cfprApFirmwareDownloaderRemotePath": cfprApFirmwareDownloaderRemotePath,
       "cfprApFirmwareDownloaderServer": cfprApFirmwareDownloaderServer,
       "cfprApFirmwareDownloaderStartTime": cfprApFirmwareDownloaderStartTime,
       "cfprApFirmwareDownloaderTimeStamp": cfprApFirmwareDownloaderTimeStamp,
       "cfprApFirmwareDownloaderTransferRate": cfprApFirmwareDownloaderTransferRate,
       "cfprApFirmwareDownloaderTransferState": cfprApFirmwareDownloaderTransferState,
       "cfprApFirmwareDownloaderUser": cfprApFirmwareDownloaderUser,
       "cfprApFirmwareDownloaderFsmTable": cfprApFirmwareDownloaderFsmTable,
       "cfprApFirmwareDownloaderFsmEntry": cfprApFirmwareDownloaderFsmEntry,
       "cfprApFirmwareDownloaderFsmInstanceId": cfprApFirmwareDownloaderFsmInstanceId,
       "cfprApFirmwareDownloaderFsmDn": cfprApFirmwareDownloaderFsmDn,
       "cfprApFirmwareDownloaderFsmRn": cfprApFirmwareDownloaderFsmRn,
       "cfprApFirmwareDownloaderFsmCompletionTime": cfprApFirmwareDownloaderFsmCompletionTime,
       "cfprApFirmwareDownloaderFsmCurrentFsm": cfprApFirmwareDownloaderFsmCurrentFsm,
       "cfprApFirmwareDownloaderFsmDescrData": cfprApFirmwareDownloaderFsmDescrData,
       "cfprApFirmwareDownloaderFsmFsmStatus": cfprApFirmwareDownloaderFsmFsmStatus,
       "cfprApFirmwareDownloaderFsmProgress": cfprApFirmwareDownloaderFsmProgress,
       "cfprApFirmwareDownloaderFsmRmtErrCode": cfprApFirmwareDownloaderFsmRmtErrCode,
       "cfprApFirmwareDownloaderFsmRmtErrDescr": cfprApFirmwareDownloaderFsmRmtErrDescr,
       "cfprApFirmwareDownloaderFsmRmtRslt": cfprApFirmwareDownloaderFsmRmtRslt,
       "cfprApFirmwareDownloaderFsmStageTable": cfprApFirmwareDownloaderFsmStageTable,
       "cfprApFirmwareDownloaderFsmStageEntry": cfprApFirmwareDownloaderFsmStageEntry,
       "cfprApFirmwareDownloaderFsmStageInstanceId": cfprApFirmwareDownloaderFsmStageInstanceId,
       "cfprApFirmwareDownloaderFsmStageDn": cfprApFirmwareDownloaderFsmStageDn,
       "cfprApFirmwareDownloaderFsmStageRn": cfprApFirmwareDownloaderFsmStageRn,
       "cfprApFirmwareDownloaderFsmStageDescrData": cfprApFirmwareDownloaderFsmStageDescrData,
       "cfprApFirmwareDownloaderFsmStageLastUpdateTime": cfprApFirmwareDownloaderFsmStageLastUpdateTime,
       "cfprApFirmwareDownloaderFsmStageName": cfprApFirmwareDownloaderFsmStageName,
       "cfprApFirmwareDownloaderFsmStageOrder": cfprApFirmwareDownloaderFsmStageOrder,
       "cfprApFirmwareDownloaderFsmStageRetry": cfprApFirmwareDownloaderFsmStageRetry,
       "cfprApFirmwareDownloaderFsmStageStageStatus": cfprApFirmwareDownloaderFsmStageStageStatus,
       "cfprApFirmwareDownloaderFsmTaskTable": cfprApFirmwareDownloaderFsmTaskTable,
       "cfprApFirmwareDownloaderFsmTaskEntry": cfprApFirmwareDownloaderFsmTaskEntry,
       "cfprApFirmwareDownloaderFsmTaskInstanceId": cfprApFirmwareDownloaderFsmTaskInstanceId,
       "cfprApFirmwareDownloaderFsmTaskDn": cfprApFirmwareDownloaderFsmTaskDn,
       "cfprApFirmwareDownloaderFsmTaskRn": cfprApFirmwareDownloaderFsmTaskRn,
       "cfprApFirmwareDownloaderFsmTaskCompletion": cfprApFirmwareDownloaderFsmTaskCompletion,
       "cfprApFirmwareDownloaderFsmTaskFlags": cfprApFirmwareDownloaderFsmTaskFlags,
       "cfprApFirmwareDownloaderFsmTaskItem": cfprApFirmwareDownloaderFsmTaskItem,
       "cfprApFirmwareDownloaderFsmTaskSeqId": cfprApFirmwareDownloaderFsmTaskSeqId,
       "cfprApFirmwareHostTable": cfprApFirmwareHostTable,
       "cfprApFirmwareHostEntry": cfprApFirmwareHostEntry,
       "cfprApFirmwareHostInstanceId": cfprApFirmwareHostInstanceId,
       "cfprApFirmwareHostDn": cfprApFirmwareHostDn,
       "cfprApFirmwareHostRn": cfprApFirmwareHostRn,
       "cfprApFirmwareHostPackModImpactTable": cfprApFirmwareHostPackModImpactTable,
       "cfprApFirmwareHostPackModImpactEntry": cfprApFirmwareHostPackModImpactEntry,
       "cfprApFirmwareHostPackModImpactInstanceId": cfprApFirmwareHostPackModImpactInstanceId,
       "cfprApFirmwareHostPackModImpactDn": cfprApFirmwareHostPackModImpactDn,
       "cfprApFirmwareHostPackModImpactRn": cfprApFirmwareHostPackModImpactRn,
       "cfprApFirmwareHostPackModImpactKeyDn": cfprApFirmwareHostPackModImpactKeyDn,
       "cfprApFirmwareHostPackModImpactMaintPolicyDn": cfprApFirmwareHostPackModImpactMaintPolicyDn,
       "cfprApFirmwareHostPackModImpactPnDn": cfprApFirmwareHostPackModImpactPnDn,
       "cfprApFirmwareHostPackModImpactRebootPolicy": cfprApFirmwareHostPackModImpactRebootPolicy,
       "cfprApFirmwareHostPackModImpactServiceProfileDn": cfprApFirmwareHostPackModImpactServiceProfileDn,
       "cfprApFirmwareImageTable": cfprApFirmwareImageTable,
       "cfprApFirmwareImageEntry": cfprApFirmwareImageEntry,
       "cfprApFirmwareImageInstanceId": cfprApFirmwareImageInstanceId,
       "cfprApFirmwareImageDn": cfprApFirmwareImageDn,
       "cfprApFirmwareImageRn": cfprApFirmwareImageRn,
       "cfprApFirmwareImageAdminState": cfprApFirmwareImageAdminState,
       "cfprApFirmwareImageChecksum": cfprApFirmwareImageChecksum,
       "cfprApFirmwareImageDescr": cfprApFirmwareImageDescr,
       "cfprApFirmwareImageDownloadDate": cfprApFirmwareImageDownloadDate,
       "cfprApFirmwareImageFsmDescr": cfprApFirmwareImageFsmDescr,
       "cfprApFirmwareImageFsmPrev": cfprApFirmwareImageFsmPrev,
       "cfprApFirmwareImageFsmProgr": cfprApFirmwareImageFsmProgr,
       "cfprApFirmwareImageFsmRmtInvErrCode": cfprApFirmwareImageFsmRmtInvErrCode,
       "cfprApFirmwareImageFsmRmtInvErrDescr": cfprApFirmwareImageFsmRmtInvErrDescr,
       "cfprApFirmwareImageFsmRmtInvRslt": cfprApFirmwareImageFsmRmtInvRslt,
       "cfprApFirmwareImageFsmStageDescr": cfprApFirmwareImageFsmStageDescr,
       "cfprApFirmwareImageFsmStamp": cfprApFirmwareImageFsmStamp,
       "cfprApFirmwareImageFsmStatus": cfprApFirmwareImageFsmStatus,
       "cfprApFirmwareImageFsmTry": cfprApFirmwareImageFsmTry,
       "cfprApFirmwareImageImagePresence": cfprApFirmwareImageImagePresence,
       "cfprApFirmwareImageIntId": cfprApFirmwareImageIntId,
       "cfprApFirmwareImageInvTag": cfprApFirmwareImageInvTag,
       "cfprApFirmwareImageIsoname": cfprApFirmwareImageIsoname,
       "cfprApFirmwareImageLocation": cfprApFirmwareImageLocation,
       "cfprApFirmwareImageName": cfprApFirmwareImageName,
       "cfprApFirmwareImagePolicyLevel": cfprApFirmwareImagePolicyLevel,
       "cfprApFirmwareImagePolicyOwner": cfprApFirmwareImagePolicyOwner,
       "cfprApFirmwareImageSize": cfprApFirmwareImageSize,
       "cfprApFirmwareImageType": cfprApFirmwareImageType,
       "cfprApFirmwareImageVersion": cfprApFirmwareImageVersion,
       "cfprApFirmwareImageFsmTable": cfprApFirmwareImageFsmTable,
       "cfprApFirmwareImageFsmEntry": cfprApFirmwareImageFsmEntry,
       "cfprApFirmwareImageFsmInstanceId": cfprApFirmwareImageFsmInstanceId,
       "cfprApFirmwareImageFsmDn": cfprApFirmwareImageFsmDn,
       "cfprApFirmwareImageFsmRn": cfprApFirmwareImageFsmRn,
       "cfprApFirmwareImageFsmCompletionTime": cfprApFirmwareImageFsmCompletionTime,
       "cfprApFirmwareImageFsmCurrentFsm": cfprApFirmwareImageFsmCurrentFsm,
       "cfprApFirmwareImageFsmDescrData": cfprApFirmwareImageFsmDescrData,
       "cfprApFirmwareImageFsmFsmStatus": cfprApFirmwareImageFsmFsmStatus,
       "cfprApFirmwareImageFsmProgress": cfprApFirmwareImageFsmProgress,
       "cfprApFirmwareImageFsmRmtErrCode": cfprApFirmwareImageFsmRmtErrCode,
       "cfprApFirmwareImageFsmRmtErrDescr": cfprApFirmwareImageFsmRmtErrDescr,
       "cfprApFirmwareImageFsmRmtRslt": cfprApFirmwareImageFsmRmtRslt,
       "cfprApFirmwareImageFsmStageTable": cfprApFirmwareImageFsmStageTable,
       "cfprApFirmwareImageFsmStageEntry": cfprApFirmwareImageFsmStageEntry,
       "cfprApFirmwareImageFsmStageInstanceId": cfprApFirmwareImageFsmStageInstanceId,
       "cfprApFirmwareImageFsmStageDn": cfprApFirmwareImageFsmStageDn,
       "cfprApFirmwareImageFsmStageRn": cfprApFirmwareImageFsmStageRn,
       "cfprApFirmwareImageFsmStageDescrData": cfprApFirmwareImageFsmStageDescrData,
       "cfprApFirmwareImageFsmStageLastUpdateTime": cfprApFirmwareImageFsmStageLastUpdateTime,
       "cfprApFirmwareImageFsmStageName": cfprApFirmwareImageFsmStageName,
       "cfprApFirmwareImageFsmStageOrder": cfprApFirmwareImageFsmStageOrder,
       "cfprApFirmwareImageFsmStageRetry": cfprApFirmwareImageFsmStageRetry,
       "cfprApFirmwareImageFsmStageStageStatus": cfprApFirmwareImageFsmStageStageStatus,
       "cfprApFirmwareImageFsmTaskTable": cfprApFirmwareImageFsmTaskTable,
       "cfprApFirmwareImageFsmTaskEntry": cfprApFirmwareImageFsmTaskEntry,
       "cfprApFirmwareImageFsmTaskInstanceId": cfprApFirmwareImageFsmTaskInstanceId,
       "cfprApFirmwareImageFsmTaskDn": cfprApFirmwareImageFsmTaskDn,
       "cfprApFirmwareImageFsmTaskRn": cfprApFirmwareImageFsmTaskRn,
       "cfprApFirmwareImageFsmTaskCompletion": cfprApFirmwareImageFsmTaskCompletion,
       "cfprApFirmwareImageFsmTaskFlags": cfprApFirmwareImageFsmTaskFlags,
       "cfprApFirmwareImageFsmTaskItem": cfprApFirmwareImageFsmTaskItem,
       "cfprApFirmwareImageFsmTaskSeqId": cfprApFirmwareImageFsmTaskSeqId,
       "cfprApFirmwareImageLockTable": cfprApFirmwareImageLockTable,
       "cfprApFirmwareImageLockEntry": cfprApFirmwareImageLockEntry,
       "cfprApFirmwareImageLockInstanceId": cfprApFirmwareImageLockInstanceId,
       "cfprApFirmwareImageLockDn": cfprApFirmwareImageLockDn,
       "cfprApFirmwareImageLockRn": cfprApFirmwareImageLockRn,
       "cfprApFirmwareImageLockImageNameDn": cfprApFirmwareImageLockImageNameDn,
       "cfprApFirmwareImageLockName": cfprApFirmwareImageLockName,
       "cfprApFirmwareInfraTable": cfprApFirmwareInfraTable,
       "cfprApFirmwareInfraEntry": cfprApFirmwareInfraEntry,
       "cfprApFirmwareInfraInstanceId": cfprApFirmwareInfraInstanceId,
       "cfprApFirmwareInfraDn": cfprApFirmwareInfraDn,
       "cfprApFirmwareInfraRn": cfprApFirmwareInfraRn,
       "cfprApFirmwareInfraAdminState": cfprApFirmwareInfraAdminState,
       "cfprApFirmwareInfraAutoDelete": cfprApFirmwareInfraAutoDelete,
       "cfprApFirmwareInfraDescr": cfprApFirmwareInfraDescr,
       "cfprApFirmwareInfraIgnoreCap": cfprApFirmwareInfraIgnoreCap,
       "cfprApFirmwareInfraIntId": cfprApFirmwareInfraIntId,
       "cfprApFirmwareInfraName": cfprApFirmwareInfraName,
       "cfprApFirmwareInfraOperScheduler": cfprApFirmwareInfraOperScheduler,
       "cfprApFirmwareInfraOperState": cfprApFirmwareInfraOperState,
       "cfprApFirmwareInfraOperVersion": cfprApFirmwareInfraOperVersion,
       "cfprApFirmwareInfraPolicyLevel": cfprApFirmwareInfraPolicyLevel,
       "cfprApFirmwareInfraPolicyOwner": cfprApFirmwareInfraPolicyOwner,
       "cfprApFirmwareInfraScheduler": cfprApFirmwareInfraScheduler,
       "cfprApFirmwareInfraPackTable": cfprApFirmwareInfraPackTable,
       "cfprApFirmwareInfraPackEntry": cfprApFirmwareInfraPackEntry,
       "cfprApFirmwareInfraPackInstanceId": cfprApFirmwareInfraPackInstanceId,
       "cfprApFirmwareInfraPackDn": cfprApFirmwareInfraPackDn,
       "cfprApFirmwareInfraPackRn": cfprApFirmwareInfraPackRn,
       "cfprApFirmwareInfraPackDescr": cfprApFirmwareInfraPackDescr,
       "cfprApFirmwareInfraPackForceDeploy": cfprApFirmwareInfraPackForceDeploy,
       "cfprApFirmwareInfraPackFsmDescr": cfprApFirmwareInfraPackFsmDescr,
       "cfprApFirmwareInfraPackFsmFlags": cfprApFirmwareInfraPackFsmFlags,
       "cfprApFirmwareInfraPackFsmPrev": cfprApFirmwareInfraPackFsmPrev,
       "cfprApFirmwareInfraPackFsmProgr": cfprApFirmwareInfraPackFsmProgr,
       "cfprApFirmwareInfraPackFsmRmtInvErrCode": cfprApFirmwareInfraPackFsmRmtInvErrCode,
       "cfprApFirmwareInfraPackFsmRmtInvErrDescr": cfprApFirmwareInfraPackFsmRmtInvErrDescr,
       "cfprApFirmwareInfraPackFsmRmtInvRslt": cfprApFirmwareInfraPackFsmRmtInvRslt,
       "cfprApFirmwareInfraPackFsmStageDescr": cfprApFirmwareInfraPackFsmStageDescr,
       "cfprApFirmwareInfraPackFsmStamp": cfprApFirmwareInfraPackFsmStamp,
       "cfprApFirmwareInfraPackFsmStatus": cfprApFirmwareInfraPackFsmStatus,
       "cfprApFirmwareInfraPackFsmTry": cfprApFirmwareInfraPackFsmTry,
       "cfprApFirmwareInfraPackInfraBundleName": cfprApFirmwareInfraPackInfraBundleName,
       "cfprApFirmwareInfraPackInfraBundleVersion": cfprApFirmwareInfraPackInfraBundleVersion,
       "cfprApFirmwareInfraPackIntId": cfprApFirmwareInfraPackIntId,
       "cfprApFirmwareInfraPackMode": cfprApFirmwareInfraPackMode,
       "cfprApFirmwareInfraPackName": cfprApFirmwareInfraPackName,
       "cfprApFirmwareInfraPackPolicyLevel": cfprApFirmwareInfraPackPolicyLevel,
       "cfprApFirmwareInfraPackPolicyOwner": cfprApFirmwareInfraPackPolicyOwner,
       "cfprApFirmwareInfraPackPreviousBundleVersion": cfprApFirmwareInfraPackPreviousBundleVersion,
       "cfprApFirmwareInfraPackStageSize": cfprApFirmwareInfraPackStageSize,
       "cfprApFirmwareInfraPackUpdateTrigger": cfprApFirmwareInfraPackUpdateTrigger,
       "cfprApFirmwareInfraPackFsmTable": cfprApFirmwareInfraPackFsmTable,
       "cfprApFirmwareInfraPackFsmEntry": cfprApFirmwareInfraPackFsmEntry,
       "cfprApFirmwareInfraPackFsmInstanceId": cfprApFirmwareInfraPackFsmInstanceId,
       "cfprApFirmwareInfraPackFsmDn": cfprApFirmwareInfraPackFsmDn,
       "cfprApFirmwareInfraPackFsmRn": cfprApFirmwareInfraPackFsmRn,
       "cfprApFirmwareInfraPackFsmCompletionTime": cfprApFirmwareInfraPackFsmCompletionTime,
       "cfprApFirmwareInfraPackFsmCurrentFsm": cfprApFirmwareInfraPackFsmCurrentFsm,
       "cfprApFirmwareInfraPackFsmDescrData": cfprApFirmwareInfraPackFsmDescrData,
       "cfprApFirmwareInfraPackFsmFsmStatus": cfprApFirmwareInfraPackFsmFsmStatus,
       "cfprApFirmwareInfraPackFsmProgress": cfprApFirmwareInfraPackFsmProgress,
       "cfprApFirmwareInfraPackFsmRmtErrCode": cfprApFirmwareInfraPackFsmRmtErrCode,
       "cfprApFirmwareInfraPackFsmRmtErrDescr": cfprApFirmwareInfraPackFsmRmtErrDescr,
       "cfprApFirmwareInfraPackFsmRmtRslt": cfprApFirmwareInfraPackFsmRmtRslt,
       "cfprApFirmwareInfraPackFsmStageTable": cfprApFirmwareInfraPackFsmStageTable,
       "cfprApFirmwareInfraPackFsmStageEntry": cfprApFirmwareInfraPackFsmStageEntry,
       "cfprApFirmwareInfraPackFsmStageInstanceId": cfprApFirmwareInfraPackFsmStageInstanceId,
       "cfprApFirmwareInfraPackFsmStageDn": cfprApFirmwareInfraPackFsmStageDn,
       "cfprApFirmwareInfraPackFsmStageRn": cfprApFirmwareInfraPackFsmStageRn,
       "cfprApFirmwareInfraPackFsmStageDescrData": cfprApFirmwareInfraPackFsmStageDescrData,
       "cfprApFirmwareInfraPackFsmStageLastUpdateTime": cfprApFirmwareInfraPackFsmStageLastUpdateTime,
       "cfprApFirmwareInfraPackFsmStageName": cfprApFirmwareInfraPackFsmStageName,
       "cfprApFirmwareInfraPackFsmStageOrder": cfprApFirmwareInfraPackFsmStageOrder,
       "cfprApFirmwareInfraPackFsmStageRetry": cfprApFirmwareInfraPackFsmStageRetry,
       "cfprApFirmwareInfraPackFsmStageStageStatus": cfprApFirmwareInfraPackFsmStageStageStatus,
       "cfprApFirmwareInfraPackFsmTaskTable": cfprApFirmwareInfraPackFsmTaskTable,
       "cfprApFirmwareInfraPackFsmTaskEntry": cfprApFirmwareInfraPackFsmTaskEntry,
       "cfprApFirmwareInfraPackFsmTaskInstanceId": cfprApFirmwareInfraPackFsmTaskInstanceId,
       "cfprApFirmwareInfraPackFsmTaskDn": cfprApFirmwareInfraPackFsmTaskDn,
       "cfprApFirmwareInfraPackFsmTaskRn": cfprApFirmwareInfraPackFsmTaskRn,
       "cfprApFirmwareInfraPackFsmTaskCompletion": cfprApFirmwareInfraPackFsmTaskCompletion,
       "cfprApFirmwareInfraPackFsmTaskFlags": cfprApFirmwareInfraPackFsmTaskFlags,
       "cfprApFirmwareInfraPackFsmTaskItem": cfprApFirmwareInfraPackFsmTaskItem,
       "cfprApFirmwareInfraPackFsmTaskSeqId": cfprApFirmwareInfraPackFsmTaskSeqId,
       "cfprApFirmwareInstallImpactTable": cfprApFirmwareInstallImpactTable,
       "cfprApFirmwareInstallImpactEntry": cfprApFirmwareInstallImpactEntry,
       "cfprApFirmwareInstallImpactInstanceId": cfprApFirmwareInstallImpactInstanceId,
       "cfprApFirmwareInstallImpactDn": cfprApFirmwareInstallImpactDn,
       "cfprApFirmwareInstallImpactRn": cfprApFirmwareInstallImpactRn,
       "cfprApFirmwareInstallImpactDescr": cfprApFirmwareInstallImpactDescr,
       "cfprApFirmwareInstallImpactKeyDn": cfprApFirmwareInstallImpactKeyDn,
       "cfprApFirmwareInstallImpactMaintPolicyDn": cfprApFirmwareInstallImpactMaintPolicyDn,
       "cfprApFirmwareInstallImpactRebootPolicy": cfprApFirmwareInstallImpactRebootPolicy,
       "cfprApFirmwareInstallImpactSubject": cfprApFirmwareInstallImpactSubject,
       "cfprApFirmwareInstallImpactType": cfprApFirmwareInstallImpactType,
       "cfprApFirmwareInstallableTable": cfprApFirmwareInstallableTable,
       "cfprApFirmwareInstallableEntry": cfprApFirmwareInstallableEntry,
       "cfprApFirmwareInstallableInstanceId": cfprApFirmwareInstallableInstanceId,
       "cfprApFirmwareInstallableDn": cfprApFirmwareInstallableDn,
       "cfprApFirmwareInstallableRn": cfprApFirmwareInstallableRn,
       "cfprApFirmwareInstallableChecksum": cfprApFirmwareInstallableChecksum,
       "cfprApFirmwareInstallableInProgress": cfprApFirmwareInstallableInProgress,
       "cfprApFirmwareInstallableIsoname": cfprApFirmwareInstallableIsoname,
       "cfprApFirmwareInstallableLocation": cfprApFirmwareInstallableLocation,
       "cfprApFirmwareInstallableModel": cfprApFirmwareInstallableModel,
       "cfprApFirmwareInstallableName": cfprApFirmwareInstallableName,
       "cfprApFirmwareInstallableSize": cfprApFirmwareInstallableSize,
       "cfprApFirmwareInstallableType": cfprApFirmwareInstallableType,
       "cfprApFirmwareInstallableVendor": cfprApFirmwareInstallableVendor,
       "cfprApFirmwareInstallableVersion": cfprApFirmwareInstallableVersion,
       "cfprApFirmwarePackItemTable": cfprApFirmwarePackItemTable,
       "cfprApFirmwarePackItemEntry": cfprApFirmwarePackItemEntry,
       "cfprApFirmwarePackItemInstanceId": cfprApFirmwarePackItemInstanceId,
       "cfprApFirmwarePackItemDn": cfprApFirmwarePackItemDn,
       "cfprApFirmwarePackItemRn": cfprApFirmwarePackItemRn,
       "cfprApFirmwarePackItemHwModel": cfprApFirmwarePackItemHwModel,
       "cfprApFirmwarePackItemHwVendor": cfprApFirmwarePackItemHwVendor,
       "cfprApFirmwarePackItemPresence": cfprApFirmwarePackItemPresence,
       "cfprApFirmwarePackItemType": cfprApFirmwarePackItemType,
       "cfprApFirmwarePackItemVersion": cfprApFirmwarePackItemVersion,
       "cfprApFirmwarePlatformTable": cfprApFirmwarePlatformTable,
       "cfprApFirmwarePlatformEntry": cfprApFirmwarePlatformEntry,
       "cfprApFirmwarePlatformInstanceId": cfprApFirmwarePlatformInstanceId,
       "cfprApFirmwarePlatformDn": cfprApFirmwarePlatformDn,
       "cfprApFirmwarePlatformRn": cfprApFirmwarePlatformRn,
       "cfprApFirmwarePlatformAdminState": cfprApFirmwarePlatformAdminState,
       "cfprApFirmwarePlatformAutoDelete": cfprApFirmwarePlatformAutoDelete,
       "cfprApFirmwarePlatformDescr": cfprApFirmwarePlatformDescr,
       "cfprApFirmwarePlatformIgnoreCap": cfprApFirmwarePlatformIgnoreCap,
       "cfprApFirmwarePlatformIntId": cfprApFirmwarePlatformIntId,
       "cfprApFirmwarePlatformName": cfprApFirmwarePlatformName,
       "cfprApFirmwarePlatformOperScheduler": cfprApFirmwarePlatformOperScheduler,
       "cfprApFirmwarePlatformOperState": cfprApFirmwarePlatformOperState,
       "cfprApFirmwarePlatformOperVersion": cfprApFirmwarePlatformOperVersion,
       "cfprApFirmwarePlatformPolicyLevel": cfprApFirmwarePlatformPolicyLevel,
       "cfprApFirmwarePlatformPolicyOwner": cfprApFirmwarePlatformPolicyOwner,
       "cfprApFirmwarePlatformScheduler": cfprApFirmwarePlatformScheduler,
       "cfprApFirmwarePlatformBundleTypeCapProviderTable": cfprApFirmwarePlatformBundleTypeCapProviderTable,
       "cfprApFirmwarePlatformBundleTypeCapProviderEntry": cfprApFirmwarePlatformBundleTypeCapProviderEntry,
       "cfprApFirmwarePlatformBundleTypeCapProviderInstanceId": cfprApFirmwarePlatformBundleTypeCapProviderInstanceId,
       "cfprApFirmwarePlatformBundleTypeCapProviderDn": cfprApFirmwarePlatformBundleTypeCapProviderDn,
       "cfprApFirmwarePlatformBundleTypeCapProviderRn": cfprApFirmwarePlatformBundleTypeCapProviderRn,
       "cfprApFirmwarePlatformBundleTypeCapProviderDeleted": cfprApFirmwarePlatformBundleTypeCapProviderDeleted,
       "cfprApFirmwarePlatformBundleTypeCapProviderDeprecated": cfprApFirmwarePlatformBundleTypeCapProviderDeprecated,
       "cfprApFirmwarePlatformBundleTypeCapProviderElementLoadFailures": cfprApFirmwarePlatformBundleTypeCapProviderElementLoadFailures,
       "cfprApFirmwarePlatformBundleTypeCapProviderElementsLoaded": cfprApFirmwarePlatformBundleTypeCapProviderElementsLoaded,
       "cfprApFirmwarePlatformBundleTypeCapProviderGencount": cfprApFirmwarePlatformBundleTypeCapProviderGencount,
       "cfprApFirmwarePlatformBundleTypeCapProviderLoadErrors": cfprApFirmwarePlatformBundleTypeCapProviderLoadErrors,
       "cfprApFirmwarePlatformBundleTypeCapProviderLoadWarnings": cfprApFirmwarePlatformBundleTypeCapProviderLoadWarnings,
       "cfprApFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer": cfprApFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer,
       "cfprApFirmwarePlatformBundleTypeCapProviderModel": cfprApFirmwarePlatformBundleTypeCapProviderModel,
       "cfprApFirmwarePlatformBundleTypeCapProviderPlatformType": cfprApFirmwarePlatformBundleTypeCapProviderPlatformType,
       "cfprApFirmwarePlatformBundleTypeCapProviderVendor": cfprApFirmwarePlatformBundleTypeCapProviderVendor,
       "cfprApFirmwarePlatformPackTable": cfprApFirmwarePlatformPackTable,
       "cfprApFirmwarePlatformPackEntry": cfprApFirmwarePlatformPackEntry,
       "cfprApFirmwarePlatformPackInstanceId": cfprApFirmwarePlatformPackInstanceId,
       "cfprApFirmwarePlatformPackDn": cfprApFirmwarePlatformPackDn,
       "cfprApFirmwarePlatformPackRn": cfprApFirmwarePlatformPackRn,
       "cfprApFirmwarePlatformPackDescr": cfprApFirmwarePlatformPackDescr,
       "cfprApFirmwarePlatformPackForceDeploy": cfprApFirmwarePlatformPackForceDeploy,
       "cfprApFirmwarePlatformPackFsmDescr": cfprApFirmwarePlatformPackFsmDescr,
       "cfprApFirmwarePlatformPackFsmFlags": cfprApFirmwarePlatformPackFsmFlags,
       "cfprApFirmwarePlatformPackFsmPrev": cfprApFirmwarePlatformPackFsmPrev,
       "cfprApFirmwarePlatformPackFsmProgr": cfprApFirmwarePlatformPackFsmProgr,
       "cfprApFirmwarePlatformPackFsmRmtInvErrCode": cfprApFirmwarePlatformPackFsmRmtInvErrCode,
       "cfprApFirmwarePlatformPackFsmRmtInvErrDescr": cfprApFirmwarePlatformPackFsmRmtInvErrDescr,
       "cfprApFirmwarePlatformPackFsmRmtInvRslt": cfprApFirmwarePlatformPackFsmRmtInvRslt,
       "cfprApFirmwarePlatformPackFsmStageDescr": cfprApFirmwarePlatformPackFsmStageDescr,
       "cfprApFirmwarePlatformPackFsmStamp": cfprApFirmwarePlatformPackFsmStamp,
       "cfprApFirmwarePlatformPackFsmStatus": cfprApFirmwarePlatformPackFsmStatus,
       "cfprApFirmwarePlatformPackFsmTry": cfprApFirmwarePlatformPackFsmTry,
       "cfprApFirmwarePlatformPackIntId": cfprApFirmwarePlatformPackIntId,
       "cfprApFirmwarePlatformPackMode": cfprApFirmwarePlatformPackMode,
       "cfprApFirmwarePlatformPackName": cfprApFirmwarePlatformPackName,
       "cfprApFirmwarePlatformPackPlatformBundleName": cfprApFirmwarePlatformPackPlatformBundleName,
       "cfprApFirmwarePlatformPackPlatformBundleVersion": cfprApFirmwarePlatformPackPlatformBundleVersion,
       "cfprApFirmwarePlatformPackPolicyLevel": cfprApFirmwarePlatformPackPolicyLevel,
       "cfprApFirmwarePlatformPackPolicyOwner": cfprApFirmwarePlatformPackPolicyOwner,
       "cfprApFirmwarePlatformPackPreviousBundleVersion": cfprApFirmwarePlatformPackPreviousBundleVersion,
       "cfprApFirmwarePlatformPackRestoreVersion": cfprApFirmwarePlatformPackRestoreVersion,
       "cfprApFirmwarePlatformPackSerializeHostUpgrade": cfprApFirmwarePlatformPackSerializeHostUpgrade,
       "cfprApFirmwarePlatformPackSkipManagerValidation": cfprApFirmwarePlatformPackSkipManagerValidation,
       "cfprApFirmwarePlatformPackStageSize": cfprApFirmwarePlatformPackStageSize,
       "cfprApFirmwarePlatformPackUpdateTrigger": cfprApFirmwarePlatformPackUpdateTrigger,
       "cfprApFirmwarePlatformPackFsmTable": cfprApFirmwarePlatformPackFsmTable,
       "cfprApFirmwarePlatformPackFsmEntry": cfprApFirmwarePlatformPackFsmEntry,
       "cfprApFirmwarePlatformPackFsmInstanceId": cfprApFirmwarePlatformPackFsmInstanceId,
       "cfprApFirmwarePlatformPackFsmDn": cfprApFirmwarePlatformPackFsmDn,
       "cfprApFirmwarePlatformPackFsmRn": cfprApFirmwarePlatformPackFsmRn,
       "cfprApFirmwarePlatformPackFsmCompletionTime": cfprApFirmwarePlatformPackFsmCompletionTime,
       "cfprApFirmwarePlatformPackFsmCurrentFsm": cfprApFirmwarePlatformPackFsmCurrentFsm,
       "cfprApFirmwarePlatformPackFsmDescrData": cfprApFirmwarePlatformPackFsmDescrData,
       "cfprApFirmwarePlatformPackFsmFsmStatus": cfprApFirmwarePlatformPackFsmFsmStatus,
       "cfprApFirmwarePlatformPackFsmProgress": cfprApFirmwarePlatformPackFsmProgress,
       "cfprApFirmwarePlatformPackFsmRmtErrCode": cfprApFirmwarePlatformPackFsmRmtErrCode,
       "cfprApFirmwarePlatformPackFsmRmtErrDescr": cfprApFirmwarePlatformPackFsmRmtErrDescr,
       "cfprApFirmwarePlatformPackFsmRmtRslt": cfprApFirmwarePlatformPackFsmRmtRslt,
       "cfprApFirmwarePlatformPackFsmStageTable": cfprApFirmwarePlatformPackFsmStageTable,
       "cfprApFirmwarePlatformPackFsmStageEntry": cfprApFirmwarePlatformPackFsmStageEntry,
       "cfprApFirmwarePlatformPackFsmStageInstanceId": cfprApFirmwarePlatformPackFsmStageInstanceId,
       "cfprApFirmwarePlatformPackFsmStageDn": cfprApFirmwarePlatformPackFsmStageDn,
       "cfprApFirmwarePlatformPackFsmStageRn": cfprApFirmwarePlatformPackFsmStageRn,
       "cfprApFirmwarePlatformPackFsmStageDescrData": cfprApFirmwarePlatformPackFsmStageDescrData,
       "cfprApFirmwarePlatformPackFsmStageLastUpdateTime": cfprApFirmwarePlatformPackFsmStageLastUpdateTime,
       "cfprApFirmwarePlatformPackFsmStageName": cfprApFirmwarePlatformPackFsmStageName,
       "cfprApFirmwarePlatformPackFsmStageOrder": cfprApFirmwarePlatformPackFsmStageOrder,
       "cfprApFirmwarePlatformPackFsmStageRetry": cfprApFirmwarePlatformPackFsmStageRetry,
       "cfprApFirmwarePlatformPackFsmStageStageStatus": cfprApFirmwarePlatformPackFsmStageStageStatus,
       "cfprApFirmwarePlatformPackFsmTaskTable": cfprApFirmwarePlatformPackFsmTaskTable,
       "cfprApFirmwarePlatformPackFsmTaskEntry": cfprApFirmwarePlatformPackFsmTaskEntry,
       "cfprApFirmwarePlatformPackFsmTaskInstanceId": cfprApFirmwarePlatformPackFsmTaskInstanceId,
       "cfprApFirmwarePlatformPackFsmTaskDn": cfprApFirmwarePlatformPackFsmTaskDn,
       "cfprApFirmwarePlatformPackFsmTaskRn": cfprApFirmwarePlatformPackFsmTaskRn,
       "cfprApFirmwarePlatformPackFsmTaskCompletion": cfprApFirmwarePlatformPackFsmTaskCompletion,
       "cfprApFirmwarePlatformPackFsmTaskFlags": cfprApFirmwarePlatformPackFsmTaskFlags,
       "cfprApFirmwarePlatformPackFsmTaskItem": cfprApFirmwarePlatformPackFsmTaskItem,
       "cfprApFirmwarePlatformPackFsmTaskSeqId": cfprApFirmwarePlatformPackFsmTaskSeqId,
       "cfprApFirmwareRackTable": cfprApFirmwareRackTable,
       "cfprApFirmwareRackEntry": cfprApFirmwareRackEntry,
       "cfprApFirmwareRackInstanceId": cfprApFirmwareRackInstanceId,
       "cfprApFirmwareRackDn": cfprApFirmwareRackDn,
       "cfprApFirmwareRackRn": cfprApFirmwareRackRn,
       "cfprApFirmwareRackOperVersion": cfprApFirmwareRackOperVersion,
       "cfprApFirmwareRommonInfoTable": cfprApFirmwareRommonInfoTable,
       "cfprApFirmwareRommonInfoEntry": cfprApFirmwareRommonInfoEntry,
       "cfprApFirmwareRommonInfoInstanceId": cfprApFirmwareRommonInfoInstanceId,
       "cfprApFirmwareRommonInfoDn": cfprApFirmwareRommonInfoDn,
       "cfprApFirmwareRommonInfoRn": cfprApFirmwareRommonInfoRn,
       "cfprApFirmwareRommonInfoFirmwareStatus": cfprApFirmwareRommonInfoFirmwareStatus,
       "cfprApFirmwareRommonInfoFirmwareVersion": cfprApFirmwareRommonInfoFirmwareVersion,
       "cfprApFirmwareRommonInfoFpgaVersion": cfprApFirmwareRommonInfoFpgaVersion,
       "cfprApFirmwareRommonInfoLanSpiVersion": cfprApFirmwareRommonInfoLanSpiVersion,
       "cfprApFirmwareRommonInfoPowerSequencerVersion": cfprApFirmwareRommonInfoPowerSequencerVersion,
       "cfprApFirmwareRommonInfoRommonVersion": cfprApFirmwareRommonInfoRommonVersion,
       "cfprApFirmwareRunningTable": cfprApFirmwareRunningTable,
       "cfprApFirmwareRunningEntry": cfprApFirmwareRunningEntry,
       "cfprApFirmwareRunningInstanceId": cfprApFirmwareRunningInstanceId,
       "cfprApFirmwareRunningDn": cfprApFirmwareRunningDn,
       "cfprApFirmwareRunningRn": cfprApFirmwareRunningRn,
       "cfprApFirmwareRunningDeployment": cfprApFirmwareRunningDeployment,
       "cfprApFirmwareRunningInvTag": cfprApFirmwareRunningInvTag,
       "cfprApFirmwareRunningPackageVersion": cfprApFirmwareRunningPackageVersion,
       "cfprApFirmwareRunningPlatformVersion": cfprApFirmwareRunningPlatformVersion,
       "cfprApFirmwareRunningType": cfprApFirmwareRunningType,
       "cfprApFirmwareRunningVersion": cfprApFirmwareRunningVersion,
       "cfprApFirmwareSpecTable": cfprApFirmwareSpecTable,
       "cfprApFirmwareSpecEntry": cfprApFirmwareSpecEntry,
       "cfprApFirmwareSpecInstanceId": cfprApFirmwareSpecInstanceId,
       "cfprApFirmwareSpecDn": cfprApFirmwareSpecDn,
       "cfprApFirmwareSpecRn": cfprApFirmwareSpecRn,
       "cfprApFirmwareSpecBundleVersion": cfprApFirmwareSpecBundleVersion,
       "cfprApFirmwareSpecEthEFIVersion": cfprApFirmwareSpecEthEFIVersion,
       "cfprApFirmwareSpecEthOptionRomVersion": cfprApFirmwareSpecEthOptionRomVersion,
       "cfprApFirmwareSpecFcFWVersion": cfprApFirmwareSpecFcFWVersion,
       "cfprApFirmwareSpecFcOptionRomVersion": cfprApFirmwareSpecFcOptionRomVersion,
       "cfprApFirmwareStatusTable": cfprApFirmwareStatusTable,
       "cfprApFirmwareStatusEntry": cfprApFirmwareStatusEntry,
       "cfprApFirmwareStatusInstanceId": cfprApFirmwareStatusInstanceId,
       "cfprApFirmwareStatusDn": cfprApFirmwareStatusDn,
       "cfprApFirmwareStatusRn": cfprApFirmwareStatusRn,
       "cfprApFirmwareStatusCimcVersion": cfprApFirmwareStatusCimcVersion,
       "cfprApFirmwareStatusFirmwareState": cfprApFirmwareStatusFirmwareState,
       "cfprApFirmwareStatusOperState": cfprApFirmwareStatusOperState,
       "cfprApFirmwareStatusPackageVersion": cfprApFirmwareStatusPackageVersion,
       "cfprApFirmwareStatusPldVersion": cfprApFirmwareStatusPldVersion,
       "cfprApFirmwareSupFirmwareTable": cfprApFirmwareSupFirmwareTable,
       "cfprApFirmwareSupFirmwareEntry": cfprApFirmwareSupFirmwareEntry,
       "cfprApFirmwareSupFirmwareInstanceId": cfprApFirmwareSupFirmwareInstanceId,
       "cfprApFirmwareSupFirmwareDn": cfprApFirmwareSupFirmwareDn,
       "cfprApFirmwareSupFirmwareRn": cfprApFirmwareSupFirmwareRn,
       "cfprApFirmwareSupFirmwareFsmDescr": cfprApFirmwareSupFirmwareFsmDescr,
       "cfprApFirmwareSupFirmwareFsmFlags": cfprApFirmwareSupFirmwareFsmFlags,
       "cfprApFirmwareSupFirmwareFsmPrev": cfprApFirmwareSupFirmwareFsmPrev,
       "cfprApFirmwareSupFirmwareFsmProgr": cfprApFirmwareSupFirmwareFsmProgr,
       "cfprApFirmwareSupFirmwareFsmRmtInvErrCode": cfprApFirmwareSupFirmwareFsmRmtInvErrCode,
       "cfprApFirmwareSupFirmwareFsmRmtInvErrDescr": cfprApFirmwareSupFirmwareFsmRmtInvErrDescr,
       "cfprApFirmwareSupFirmwareFsmRmtInvRslt": cfprApFirmwareSupFirmwareFsmRmtInvRslt,
       "cfprApFirmwareSupFirmwareFsmStageDescr": cfprApFirmwareSupFirmwareFsmStageDescr,
       "cfprApFirmwareSupFirmwareFsmStamp": cfprApFirmwareSupFirmwareFsmStamp,
       "cfprApFirmwareSupFirmwareFsmStatus": cfprApFirmwareSupFirmwareFsmStatus,
       "cfprApFirmwareSupFirmwareFsmTry": cfprApFirmwareSupFirmwareFsmTry,
       "cfprApFirmwareSupFirmwareOperState": cfprApFirmwareSupFirmwareOperState,
       "cfprApFirmwareSupFirmwarePackVersion": cfprApFirmwareSupFirmwarePackVersion,
       "cfprApFirmwareSupFirmwareState": cfprApFirmwareSupFirmwareState,
       "cfprApFirmwareSupFirmwareUpgradeStatus": cfprApFirmwareSupFirmwareUpgradeStatus,
       "cfprApFirmwareSupFirmwareFsmTable": cfprApFirmwareSupFirmwareFsmTable,
       "cfprApFirmwareSupFirmwareFsmEntry": cfprApFirmwareSupFirmwareFsmEntry,
       "cfprApFirmwareSupFirmwareFsmInstanceId": cfprApFirmwareSupFirmwareFsmInstanceId,
       "cfprApFirmwareSupFirmwareFsmDn": cfprApFirmwareSupFirmwareFsmDn,
       "cfprApFirmwareSupFirmwareFsmRn": cfprApFirmwareSupFirmwareFsmRn,
       "cfprApFirmwareSupFirmwareFsmCompletionTime": cfprApFirmwareSupFirmwareFsmCompletionTime,
       "cfprApFirmwareSupFirmwareFsmCurrentFsm": cfprApFirmwareSupFirmwareFsmCurrentFsm,
       "cfprApFirmwareSupFirmwareFsmDescrData": cfprApFirmwareSupFirmwareFsmDescrData,
       "cfprApFirmwareSupFirmwareFsmFsmStatus": cfprApFirmwareSupFirmwareFsmFsmStatus,
       "cfprApFirmwareSupFirmwareFsmProgress": cfprApFirmwareSupFirmwareFsmProgress,
       "cfprApFirmwareSupFirmwareFsmRmtErrCode": cfprApFirmwareSupFirmwareFsmRmtErrCode,
       "cfprApFirmwareSupFirmwareFsmRmtErrDescr": cfprApFirmwareSupFirmwareFsmRmtErrDescr,
       "cfprApFirmwareSupFirmwareFsmRmtRslt": cfprApFirmwareSupFirmwareFsmRmtRslt,
       "cfprApFirmwareSupFirmwareFsmStageTable": cfprApFirmwareSupFirmwareFsmStageTable,
       "cfprApFirmwareSupFirmwareFsmStageEntry": cfprApFirmwareSupFirmwareFsmStageEntry,
       "cfprApFirmwareSupFirmwareFsmStageInstanceId": cfprApFirmwareSupFirmwareFsmStageInstanceId,
       "cfprApFirmwareSupFirmwareFsmStageDn": cfprApFirmwareSupFirmwareFsmStageDn,
       "cfprApFirmwareSupFirmwareFsmStageRn": cfprApFirmwareSupFirmwareFsmStageRn,
       "cfprApFirmwareSupFirmwareFsmStageDescrData": cfprApFirmwareSupFirmwareFsmStageDescrData,
       "cfprApFirmwareSupFirmwareFsmStageLastUpdateTime": cfprApFirmwareSupFirmwareFsmStageLastUpdateTime,
       "cfprApFirmwareSupFirmwareFsmStageName": cfprApFirmwareSupFirmwareFsmStageName,
       "cfprApFirmwareSupFirmwareFsmStageOrder": cfprApFirmwareSupFirmwareFsmStageOrder,
       "cfprApFirmwareSupFirmwareFsmStageRetry": cfprApFirmwareSupFirmwareFsmStageRetry,
       "cfprApFirmwareSupFirmwareFsmStageStageStatus": cfprApFirmwareSupFirmwareFsmStageStageStatus,
       "cfprApFirmwareSupFirmwareFsmTaskTable": cfprApFirmwareSupFirmwareFsmTaskTable,
       "cfprApFirmwareSupFirmwareFsmTaskEntry": cfprApFirmwareSupFirmwareFsmTaskEntry,
       "cfprApFirmwareSupFirmwareFsmTaskInstanceId": cfprApFirmwareSupFirmwareFsmTaskInstanceId,
       "cfprApFirmwareSupFirmwareFsmTaskDn": cfprApFirmwareSupFirmwareFsmTaskDn,
       "cfprApFirmwareSupFirmwareFsmTaskRn": cfprApFirmwareSupFirmwareFsmTaskRn,
       "cfprApFirmwareSupFirmwareFsmTaskCompletion": cfprApFirmwareSupFirmwareFsmTaskCompletion,
       "cfprApFirmwareSupFirmwareFsmTaskFlags": cfprApFirmwareSupFirmwareFsmTaskFlags,
       "cfprApFirmwareSupFirmwareFsmTaskItem": cfprApFirmwareSupFirmwareFsmTaskItem,
       "cfprApFirmwareSupFirmwareFsmTaskSeqId": cfprApFirmwareSupFirmwareFsmTaskSeqId,
       "cfprApFirmwareSystemTable": cfprApFirmwareSystemTable,
       "cfprApFirmwareSystemEntry": cfprApFirmwareSystemEntry,
       "cfprApFirmwareSystemInstanceId": cfprApFirmwareSystemInstanceId,
       "cfprApFirmwareSystemDn": cfprApFirmwareSystemDn,
       "cfprApFirmwareSystemRn": cfprApFirmwareSystemRn,
       "cfprApFirmwareSystemFsmDescr": cfprApFirmwareSystemFsmDescr,
       "cfprApFirmwareSystemFsmFlags": cfprApFirmwareSystemFsmFlags,
       "cfprApFirmwareSystemFsmPrev": cfprApFirmwareSystemFsmPrev,
       "cfprApFirmwareSystemFsmProgr": cfprApFirmwareSystemFsmProgr,
       "cfprApFirmwareSystemFsmRmtInvErrCode": cfprApFirmwareSystemFsmRmtInvErrCode,
       "cfprApFirmwareSystemFsmRmtInvErrDescr": cfprApFirmwareSystemFsmRmtInvErrDescr,
       "cfprApFirmwareSystemFsmRmtInvRslt": cfprApFirmwareSystemFsmRmtInvRslt,
       "cfprApFirmwareSystemFsmStageDescr": cfprApFirmwareSystemFsmStageDescr,
       "cfprApFirmwareSystemFsmStamp": cfprApFirmwareSystemFsmStamp,
       "cfprApFirmwareSystemFsmStatus": cfprApFirmwareSystemFsmStatus,
       "cfprApFirmwareSystemFsmTry": cfprApFirmwareSystemFsmTry,
       "cfprApFirmwareSystemFwUpgradeBitmap": cfprApFirmwareSystemFwUpgradeBitmap,
       "cfprApFirmwareSystemFwUpgradeStatus": cfprApFirmwareSystemFwUpgradeStatus,
       "cfprApFirmwareSystemOperState": cfprApFirmwareSystemOperState,
       "cfprApFirmwareSystemPackVersion": cfprApFirmwareSystemPackVersion,
       "cfprApFirmwareSystemScheduledInstallTime": cfprApFirmwareSystemScheduledInstallTime,
       "cfprApFirmwareSystemState": cfprApFirmwareSystemState,
       "cfprApFirmwareSystemUpgradeState": cfprApFirmwareSystemUpgradeState,
       "cfprApFirmwareSystemUpgradeStatus": cfprApFirmwareSystemUpgradeStatus,
       "cfprApFirmwareSystemCompCheckResultTable": cfprApFirmwareSystemCompCheckResultTable,
       "cfprApFirmwareSystemCompCheckResultEntry": cfprApFirmwareSystemCompCheckResultEntry,
       "cfprApFirmwareSystemCompCheckResultInstanceId": cfprApFirmwareSystemCompCheckResultInstanceId,
       "cfprApFirmwareSystemCompCheckResultDn": cfprApFirmwareSystemCompCheckResultDn,
       "cfprApFirmwareSystemCompCheckResultRn": cfprApFirmwareSystemCompCheckResultRn,
       "cfprApFirmwareSystemCompCheckResultKeyDescr": cfprApFirmwareSystemCompCheckResultKeyDescr,
       "cfprApFirmwareSystemCompCheckResultKeyDn": cfprApFirmwareSystemCompCheckResultKeyDn,
       "cfprApFirmwareSystemCompCheckResultNonCompDescr": cfprApFirmwareSystemCompCheckResultNonCompDescr,
       "cfprApFirmwareSystemCompCheckResultNonCompDns": cfprApFirmwareSystemCompCheckResultNonCompDns,
       "cfprApFirmwareSystemCompCheckResultSubject": cfprApFirmwareSystemCompCheckResultSubject,
       "cfprApFirmwareSystemFsmTable": cfprApFirmwareSystemFsmTable,
       "cfprApFirmwareSystemFsmEntry": cfprApFirmwareSystemFsmEntry,
       "cfprApFirmwareSystemFsmInstanceId": cfprApFirmwareSystemFsmInstanceId,
       "cfprApFirmwareSystemFsmDn": cfprApFirmwareSystemFsmDn,
       "cfprApFirmwareSystemFsmRn": cfprApFirmwareSystemFsmRn,
       "cfprApFirmwareSystemFsmCompletionTime": cfprApFirmwareSystemFsmCompletionTime,
       "cfprApFirmwareSystemFsmCurrentFsm": cfprApFirmwareSystemFsmCurrentFsm,
       "cfprApFirmwareSystemFsmDescrData": cfprApFirmwareSystemFsmDescrData,
       "cfprApFirmwareSystemFsmFsmStatus": cfprApFirmwareSystemFsmFsmStatus,
       "cfprApFirmwareSystemFsmProgress": cfprApFirmwareSystemFsmProgress,
       "cfprApFirmwareSystemFsmRmtErrCode": cfprApFirmwareSystemFsmRmtErrCode,
       "cfprApFirmwareSystemFsmRmtErrDescr": cfprApFirmwareSystemFsmRmtErrDescr,
       "cfprApFirmwareSystemFsmRmtRslt": cfprApFirmwareSystemFsmRmtRslt,
       "cfprApFirmwareSystemFsmStageTable": cfprApFirmwareSystemFsmStageTable,
       "cfprApFirmwareSystemFsmStageEntry": cfprApFirmwareSystemFsmStageEntry,
       "cfprApFirmwareSystemFsmStageInstanceId": cfprApFirmwareSystemFsmStageInstanceId,
       "cfprApFirmwareSystemFsmStageDn": cfprApFirmwareSystemFsmStageDn,
       "cfprApFirmwareSystemFsmStageRn": cfprApFirmwareSystemFsmStageRn,
       "cfprApFirmwareSystemFsmStageDescrData": cfprApFirmwareSystemFsmStageDescrData,
       "cfprApFirmwareSystemFsmStageLastUpdateTime": cfprApFirmwareSystemFsmStageLastUpdateTime,
       "cfprApFirmwareSystemFsmStageName": cfprApFirmwareSystemFsmStageName,
       "cfprApFirmwareSystemFsmStageOrder": cfprApFirmwareSystemFsmStageOrder,
       "cfprApFirmwareSystemFsmStageRetry": cfprApFirmwareSystemFsmStageRetry,
       "cfprApFirmwareSystemFsmStageStageStatus": cfprApFirmwareSystemFsmStageStageStatus,
       "cfprApFirmwareSystemFsmTaskTable": cfprApFirmwareSystemFsmTaskTable,
       "cfprApFirmwareSystemFsmTaskEntry": cfprApFirmwareSystemFsmTaskEntry,
       "cfprApFirmwareSystemFsmTaskInstanceId": cfprApFirmwareSystemFsmTaskInstanceId,
       "cfprApFirmwareSystemFsmTaskDn": cfprApFirmwareSystemFsmTaskDn,
       "cfprApFirmwareSystemFsmTaskRn": cfprApFirmwareSystemFsmTaskRn,
       "cfprApFirmwareSystemFsmTaskCompletion": cfprApFirmwareSystemFsmTaskCompletion,
       "cfprApFirmwareSystemFsmTaskFlags": cfprApFirmwareSystemFsmTaskFlags,
       "cfprApFirmwareSystemFsmTaskItem": cfprApFirmwareSystemFsmTaskItem,
       "cfprApFirmwareSystemFsmTaskSeqId": cfprApFirmwareSystemFsmTaskSeqId,
       "cfprApFirmwareTypeTable": cfprApFirmwareTypeTable,
       "cfprApFirmwareTypeEntry": cfprApFirmwareTypeEntry,
       "cfprApFirmwareTypeInstanceId": cfprApFirmwareTypeInstanceId,
       "cfprApFirmwareTypeDn": cfprApFirmwareTypeDn,
       "cfprApFirmwareTypeRn": cfprApFirmwareTypeRn,
       "cfprApFirmwareTypeEp": cfprApFirmwareTypeEp,
       "cfprApFirmwareTypeInvTag": cfprApFirmwareTypeInvTag,
       "cfprApFirmwareTypeMaxVer": cfprApFirmwareTypeMaxVer,
       "cfprApFirmwareTypeMinVer": cfprApFirmwareTypeMinVer,
       "cfprApFirmwareTypeScheduledInstallTime": cfprApFirmwareTypeScheduledInstallTime,
       "cfprApFirmwareUcscInfoTable": cfprApFirmwareUcscInfoTable,
       "cfprApFirmwareUcscInfoEntry": cfprApFirmwareUcscInfoEntry,
       "cfprApFirmwareUcscInfoInstanceId": cfprApFirmwareUcscInfoInstanceId,
       "cfprApFirmwareUcscInfoDn": cfprApFirmwareUcscInfoDn,
       "cfprApFirmwareUcscInfoRn": cfprApFirmwareUcscInfoRn,
       "cfprApFirmwareUcscInfoConnProtocol": cfprApFirmwareUcscInfoConnProtocol,
       "cfprApFirmwareUcscInfoHost": cfprApFirmwareUcscInfoHost,
       "cfprApFirmwareUcscInfoVersion": cfprApFirmwareUcscInfoVersion,
       "cfprApFirmwareUpdatableTable": cfprApFirmwareUpdatableTable,
       "cfprApFirmwareUpdatableEntry": cfprApFirmwareUpdatableEntry,
       "cfprApFirmwareUpdatableInstanceId": cfprApFirmwareUpdatableInstanceId,
       "cfprApFirmwareUpdatableDn": cfprApFirmwareUpdatableDn,
       "cfprApFirmwareUpdatableRn": cfprApFirmwareUpdatableRn,
       "cfprApFirmwareUpdatableAdminState": cfprApFirmwareUpdatableAdminState,
       "cfprApFirmwareUpdatableDeployment": cfprApFirmwareUpdatableDeployment,
       "cfprApFirmwareUpdatableOperState": cfprApFirmwareUpdatableOperState,
       "cfprApFirmwareUpdatableOperStateQual": cfprApFirmwareUpdatableOperStateQual,
       "cfprApFirmwareUpdatablePrevVersion": cfprApFirmwareUpdatablePrevVersion,
       "cfprApFirmwareUpdatableVersion": cfprApFirmwareUpdatableVersion,
       "cfprApFirmwareUpgradeConstraintTable": cfprApFirmwareUpgradeConstraintTable,
       "cfprApFirmwareUpgradeConstraintEntry": cfprApFirmwareUpgradeConstraintEntry,
       "cfprApFirmwareUpgradeConstraintInstanceId": cfprApFirmwareUpgradeConstraintInstanceId,
       "cfprApFirmwareUpgradeConstraintDn": cfprApFirmwareUpgradeConstraintDn,
       "cfprApFirmwareUpgradeConstraintRn": cfprApFirmwareUpgradeConstraintRn,
       "cfprApFirmwareUpgradeConstraintMinVer": cfprApFirmwareUpgradeConstraintMinVer,
       "cfprApFirmwareUpgradeDetailTable": cfprApFirmwareUpgradeDetailTable,
       "cfprApFirmwareUpgradeDetailEntry": cfprApFirmwareUpgradeDetailEntry,
       "cfprApFirmwareUpgradeDetailInstanceId": cfprApFirmwareUpgradeDetailInstanceId,
       "cfprApFirmwareUpgradeDetailDn": cfprApFirmwareUpgradeDetailDn,
       "cfprApFirmwareUpgradeDetailRn": cfprApFirmwareUpgradeDetailRn,
       "cfprApFirmwareUpgradeDetailCategory": cfprApFirmwareUpgradeDetailCategory,
       "cfprApFirmwareUpgradeDetailDescription": cfprApFirmwareUpgradeDetailDescription,
       "cfprApFirmwareUpgradeDetailId": cfprApFirmwareUpgradeDetailId,
       "cfprApFirmwareUpgradeDetailSeverity": cfprApFirmwareUpgradeDetailSeverity,
       "cfprApFirmwareUpgradeInfoTable": cfprApFirmwareUpgradeInfoTable,
       "cfprApFirmwareUpgradeInfoEntry": cfprApFirmwareUpgradeInfoEntry,
       "cfprApFirmwareUpgradeInfoInstanceId": cfprApFirmwareUpgradeInfoInstanceId,
       "cfprApFirmwareUpgradeInfoDn": cfprApFirmwareUpgradeInfoDn,
       "cfprApFirmwareUpgradeInfoRn": cfprApFirmwareUpgradeInfoRn,
       "cfprApFirmwareUpgradeInfoMessage": cfprApFirmwareUpgradeInfoMessage,
       "cfprApFirmwareUpgradeInfoTimeStamp": cfprApFirmwareUpgradeInfoTimeStamp,
       "cfprApFirmwareUpgradeInfoValidateStatus": cfprApFirmwareUpgradeInfoValidateStatus,
       "cfprApFirmwareUpgradeInfoVersion": cfprApFirmwareUpgradeInfoVersion}
)
