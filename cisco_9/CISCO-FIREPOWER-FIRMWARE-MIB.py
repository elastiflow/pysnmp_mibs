# SNMP MIB module (CISCO-FIREPOWER-FIRMWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-FIRMWARE-MIB.mib
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

(CfprConditionRemoteInvRslt,
 CfprExtpolConnProtocol,
 CfprFirmwareAdminState,
 CfprFirmwareAutoSyncConfigIssue,
 CfprFirmwareAutoSyncState,
 CfprFirmwareBootUnitImage,
 CfprFirmwareBootUnitMode,
 CfprFirmwareCatalogPackConfigState,
 CfprFirmwareCompleteness,
 CfprFirmwareComponentType,
 CfprFirmwareDependencyRelationship,
 CfprFirmwareDependencyScope,
 CfprFirmwareDependencySensitivity,
 CfprFirmwareDeployment,
 CfprFirmwareDistributableFsmCurrentFsm,
 CfprFirmwareDistributableFsmStageName,
 CfprFirmwareDistributableFsmTaskItem,
 CfprFirmwareDistributableType,
 CfprFirmwareDownloadActivity,
 CfprFirmwareDownloaderFsmCurrentFsm,
 CfprFirmwareDownloaderFsmStageName,
 CfprFirmwareDownloaderFsmTaskItem,
 CfprFirmwareEquipmentType,
 CfprFirmwareFirmwareState,
 CfprFirmwareFwState,
 CfprFirmwareFwUpgradeState,
 CfprFirmwareHostPackConfigQualifier,
 CfprFirmwareImageDeleted,
 CfprFirmwareImageError,
 CfprFirmwareImageFsmCurrentFsm,
 CfprFirmwareImageFsmStageName,
 CfprFirmwareImageFsmTaskItem,
 CfprFirmwareImagePresence,
 CfprFirmwareImageState,
 CfprFirmwareImageValidationStateType,
 CfprFirmwareImageValidationType,
 CfprFirmwareImpactType,
 CfprFirmwareInstallState,
 CfprFirmwareItemType,
 CfprFirmwarePackItemPresence,
 CfprFirmwarePackMode,
 CfprFirmwarePlatformPackFsmCurrentFsm,
 CfprFirmwarePlatformPackFsmStageName,
 CfprFirmwarePlatformPackFsmTaskFlags,
 CfprFirmwarePlatformPackFsmTaskItem,
 CfprFirmwarePlatformType,
 CfprFirmwareRunningDeployment,
 CfprFirmwareSupFirmwareFsmCurrentFsm,
 CfprFirmwareSupFirmwareFsmStageName,
 CfprFirmwareSupFirmwareFsmTaskFlags,
 CfprFirmwareSupFirmwareFsmTaskItem,
 CfprFirmwareSupportedModeType,
 CfprFirmwareSystemFsmCurrentFsm,
 CfprFirmwareSystemFsmStageName,
 CfprFirmwareSystemFsmTaskFlags,
 CfprFirmwareSystemFsmTaskItem,
 CfprFirmwareTransferState,
 CfprFirmwareTransport,
 CfprFirmwareTriggerState,
 CfprFirmwareType,
 CfprFirmwareUpdatableDeployment,
 CfprFirmwareUpgradeCategory,
 CfprFirmwareUpgradeSeverity,
 CfprFirmwareUpgradeStatus,
 CfprFirmwareValidationStatusFsmCurrentFsm,
 CfprFirmwareValidationStatusFsmStageName,
 CfprFirmwareValidationStatusFsmTaskFlags,
 CfprFirmwareValidationStatusFsmTaskItem,
 CfprFirmwareVerifyPackStatus,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprPolicyPolicyOwner,
 CfprTrigAckChangeDetails,
 CfprTrigAckChanges,
 CfprTrigAckDisr,
 CfprTrigAckOperState,
 CfprTrigAckPrevOperState,
 CfprTrigAdminState,
 CfprTrigTrigOperState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprExtpolConnProtocol",
    "CfprFirmwareAdminState",
    "CfprFirmwareAutoSyncConfigIssue",
    "CfprFirmwareAutoSyncState",
    "CfprFirmwareBootUnitImage",
    "CfprFirmwareBootUnitMode",
    "CfprFirmwareCatalogPackConfigState",
    "CfprFirmwareCompleteness",
    "CfprFirmwareComponentType",
    "CfprFirmwareDependencyRelationship",
    "CfprFirmwareDependencyScope",
    "CfprFirmwareDependencySensitivity",
    "CfprFirmwareDeployment",
    "CfprFirmwareDistributableFsmCurrentFsm",
    "CfprFirmwareDistributableFsmStageName",
    "CfprFirmwareDistributableFsmTaskItem",
    "CfprFirmwareDistributableType",
    "CfprFirmwareDownloadActivity",
    "CfprFirmwareDownloaderFsmCurrentFsm",
    "CfprFirmwareDownloaderFsmStageName",
    "CfprFirmwareDownloaderFsmTaskItem",
    "CfprFirmwareEquipmentType",
    "CfprFirmwareFirmwareState",
    "CfprFirmwareFwState",
    "CfprFirmwareFwUpgradeState",
    "CfprFirmwareHostPackConfigQualifier",
    "CfprFirmwareImageDeleted",
    "CfprFirmwareImageError",
    "CfprFirmwareImageFsmCurrentFsm",
    "CfprFirmwareImageFsmStageName",
    "CfprFirmwareImageFsmTaskItem",
    "CfprFirmwareImagePresence",
    "CfprFirmwareImageState",
    "CfprFirmwareImageValidationStateType",
    "CfprFirmwareImageValidationType",
    "CfprFirmwareImpactType",
    "CfprFirmwareInstallState",
    "CfprFirmwareItemType",
    "CfprFirmwarePackItemPresence",
    "CfprFirmwarePackMode",
    "CfprFirmwarePlatformPackFsmCurrentFsm",
    "CfprFirmwarePlatformPackFsmStageName",
    "CfprFirmwarePlatformPackFsmTaskFlags",
    "CfprFirmwarePlatformPackFsmTaskItem",
    "CfprFirmwarePlatformType",
    "CfprFirmwareRunningDeployment",
    "CfprFirmwareSupFirmwareFsmCurrentFsm",
    "CfprFirmwareSupFirmwareFsmStageName",
    "CfprFirmwareSupFirmwareFsmTaskFlags",
    "CfprFirmwareSupFirmwareFsmTaskItem",
    "CfprFirmwareSupportedModeType",
    "CfprFirmwareSystemFsmCurrentFsm",
    "CfprFirmwareSystemFsmStageName",
    "CfprFirmwareSystemFsmTaskFlags",
    "CfprFirmwareSystemFsmTaskItem",
    "CfprFirmwareTransferState",
    "CfprFirmwareTransport",
    "CfprFirmwareTriggerState",
    "CfprFirmwareType",
    "CfprFirmwareUpdatableDeployment",
    "CfprFirmwareUpgradeCategory",
    "CfprFirmwareUpgradeSeverity",
    "CfprFirmwareUpgradeStatus",
    "CfprFirmwareValidationStatusFsmCurrentFsm",
    "CfprFirmwareValidationStatusFsmStageName",
    "CfprFirmwareValidationStatusFsmTaskFlags",
    "CfprFirmwareValidationStatusFsmTaskItem",
    "CfprFirmwareVerifyPackStatus",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprPolicyPolicyOwner",
    "CfprTrigAckChangeDetails",
    "CfprTrigAckChanges",
    "CfprTrigAckDisr",
    "CfprTrigAckOperState",
    "CfprTrigAckPrevOperState",
    "CfprTrigAdminState",
    "CfprTrigTrigOperState")

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

cfprFirmwareObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprFirmwareAckTable_Object = MibTable
cfprFirmwareAckTable = _CfprFirmwareAckTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1)
)
if mibBuilder.loadTexts:
    cfprFirmwareAckTable.setStatus("current")
_CfprFirmwareAckEntry_Object = MibTableRow
cfprFirmwareAckEntry = _CfprFirmwareAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1)
)
cfprFirmwareAckEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareAckInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareAckEntry.setStatus("current")
_CfprFirmwareAckInstanceId_Type = CfprManagedObjectId
_CfprFirmwareAckInstanceId_Object = MibTableColumn
cfprFirmwareAckInstanceId = _CfprFirmwareAckInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 1),
    _CfprFirmwareAckInstanceId_Type()
)
cfprFirmwareAckInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareAckInstanceId.setStatus("current")
_CfprFirmwareAckDn_Type = CfprManagedObjectDn
_CfprFirmwareAckDn_Object = MibTableColumn
cfprFirmwareAckDn = _CfprFirmwareAckDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 2),
    _CfprFirmwareAckDn_Type()
)
cfprFirmwareAckDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckDn.setStatus("current")
_CfprFirmwareAckRn_Type = SnmpAdminString
_CfprFirmwareAckRn_Object = MibTableColumn
cfprFirmwareAckRn = _CfprFirmwareAckRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 3),
    _CfprFirmwareAckRn_Type()
)
cfprFirmwareAckRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckRn.setStatus("current")
_CfprFirmwareAckAcked_Type = DateAndTime
_CfprFirmwareAckAcked_Object = MibTableColumn
cfprFirmwareAckAcked = _CfprFirmwareAckAcked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 4),
    _CfprFirmwareAckAcked_Type()
)
cfprFirmwareAckAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckAcked.setStatus("current")
_CfprFirmwareAckAckedBy_Type = SnmpAdminString
_CfprFirmwareAckAckedBy_Object = MibTableColumn
cfprFirmwareAckAckedBy = _CfprFirmwareAckAckedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 5),
    _CfprFirmwareAckAckedBy_Type()
)
cfprFirmwareAckAckedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckAckedBy.setStatus("current")
_CfprFirmwareAckAdminState_Type = CfprTrigAdminState
_CfprFirmwareAckAdminState_Object = MibTableColumn
cfprFirmwareAckAdminState = _CfprFirmwareAckAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 6),
    _CfprFirmwareAckAdminState_Type()
)
cfprFirmwareAckAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckAdminState.setStatus("current")
_CfprFirmwareAckAutoDelete_Type = TruthValue
_CfprFirmwareAckAutoDelete_Object = MibTableColumn
cfprFirmwareAckAutoDelete = _CfprFirmwareAckAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 7),
    _CfprFirmwareAckAutoDelete_Type()
)
cfprFirmwareAckAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckAutoDelete.setStatus("current")
_CfprFirmwareAckChangeBy_Type = SnmpAdminString
_CfprFirmwareAckChangeBy_Object = MibTableColumn
cfprFirmwareAckChangeBy = _CfprFirmwareAckChangeBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 8),
    _CfprFirmwareAckChangeBy_Type()
)
cfprFirmwareAckChangeBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckChangeBy.setStatus("current")
_CfprFirmwareAckChangeDetails_Type = CfprTrigAckChangeDetails
_CfprFirmwareAckChangeDetails_Object = MibTableColumn
cfprFirmwareAckChangeDetails = _CfprFirmwareAckChangeDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 9),
    _CfprFirmwareAckChangeDetails_Type()
)
cfprFirmwareAckChangeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckChangeDetails.setStatus("current")
_CfprFirmwareAckChanges_Type = CfprTrigAckChanges
_CfprFirmwareAckChanges_Object = MibTableColumn
cfprFirmwareAckChanges = _CfprFirmwareAckChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 10),
    _CfprFirmwareAckChanges_Type()
)
cfprFirmwareAckChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckChanges.setStatus("current")
_CfprFirmwareAckDescr_Type = SnmpAdminString
_CfprFirmwareAckDescr_Object = MibTableColumn
cfprFirmwareAckDescr = _CfprFirmwareAckDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 11),
    _CfprFirmwareAckDescr_Type()
)
cfprFirmwareAckDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckDescr.setStatus("current")
_CfprFirmwareAckDisr_Type = CfprTrigAckDisr
_CfprFirmwareAckDisr_Object = MibTableColumn
cfprFirmwareAckDisr = _CfprFirmwareAckDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 12),
    _CfprFirmwareAckDisr_Type()
)
cfprFirmwareAckDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckDisr.setStatus("current")
_CfprFirmwareAckIgnoreCap_Type = TruthValue
_CfprFirmwareAckIgnoreCap_Object = MibTableColumn
cfprFirmwareAckIgnoreCap = _CfprFirmwareAckIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 13),
    _CfprFirmwareAckIgnoreCap_Type()
)
cfprFirmwareAckIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckIgnoreCap.setStatus("current")
_CfprFirmwareAckIntId_Type = SnmpAdminString
_CfprFirmwareAckIntId_Object = MibTableColumn
cfprFirmwareAckIntId = _CfprFirmwareAckIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 14),
    _CfprFirmwareAckIntId_Type()
)
cfprFirmwareAckIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckIntId.setStatus("current")
_CfprFirmwareAckModified_Type = DateAndTime
_CfprFirmwareAckModified_Object = MibTableColumn
cfprFirmwareAckModified = _CfprFirmwareAckModified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 15),
    _CfprFirmwareAckModified_Type()
)
cfprFirmwareAckModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckModified.setStatus("current")
_CfprFirmwareAckName_Type = SnmpAdminString
_CfprFirmwareAckName_Object = MibTableColumn
cfprFirmwareAckName = _CfprFirmwareAckName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 16),
    _CfprFirmwareAckName_Type()
)
cfprFirmwareAckName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckName.setStatus("current")
_CfprFirmwareAckOperScheduler_Type = SnmpAdminString
_CfprFirmwareAckOperScheduler_Object = MibTableColumn
cfprFirmwareAckOperScheduler = _CfprFirmwareAckOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 17),
    _CfprFirmwareAckOperScheduler_Type()
)
cfprFirmwareAckOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckOperScheduler.setStatus("current")
_CfprFirmwareAckOperState_Type = CfprTrigAckOperState
_CfprFirmwareAckOperState_Object = MibTableColumn
cfprFirmwareAckOperState = _CfprFirmwareAckOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 18),
    _CfprFirmwareAckOperState_Type()
)
cfprFirmwareAckOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckOperState.setStatus("current")
_CfprFirmwareAckPolicyLevel_Type = Gauge32
_CfprFirmwareAckPolicyLevel_Object = MibTableColumn
cfprFirmwareAckPolicyLevel = _CfprFirmwareAckPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 19),
    _CfprFirmwareAckPolicyLevel_Type()
)
cfprFirmwareAckPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckPolicyLevel.setStatus("current")
_CfprFirmwareAckPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwareAckPolicyOwner_Object = MibTableColumn
cfprFirmwareAckPolicyOwner = _CfprFirmwareAckPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 20),
    _CfprFirmwareAckPolicyOwner_Type()
)
cfprFirmwareAckPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckPolicyOwner.setStatus("current")
_CfprFirmwareAckPrevOperState_Type = CfprTrigAckPrevOperState
_CfprFirmwareAckPrevOperState_Object = MibTableColumn
cfprFirmwareAckPrevOperState = _CfprFirmwareAckPrevOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 21),
    _CfprFirmwareAckPrevOperState_Type()
)
cfprFirmwareAckPrevOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckPrevOperState.setStatus("current")
_CfprFirmwareAckScheduler_Type = SnmpAdminString
_CfprFirmwareAckScheduler_Object = MibTableColumn
cfprFirmwareAckScheduler = _CfprFirmwareAckScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 1, 1, 22),
    _CfprFirmwareAckScheduler_Type()
)
cfprFirmwareAckScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAckScheduler.setStatus("current")
_CfprFirmwareAutoSyncPolicyTable_Object = MibTable
cfprFirmwareAutoSyncPolicyTable = _CfprFirmwareAutoSyncPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 2)
)
if mibBuilder.loadTexts:
    cfprFirmwareAutoSyncPolicyTable.setStatus("current")
_CfprFirmwareAutoSyncPolicyEntry_Object = MibTableRow
cfprFirmwareAutoSyncPolicyEntry = _CfprFirmwareAutoSyncPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 2, 1)
)
cfprFirmwareAutoSyncPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareAutoSyncPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareAutoSyncPolicyEntry.setStatus("current")
_CfprFirmwareAutoSyncPolicyInstanceId_Type = CfprManagedObjectId
_CfprFirmwareAutoSyncPolicyInstanceId_Object = MibTableColumn
cfprFirmwareAutoSyncPolicyInstanceId = _CfprFirmwareAutoSyncPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 2, 1, 1),
    _CfprFirmwareAutoSyncPolicyInstanceId_Type()
)
cfprFirmwareAutoSyncPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareAutoSyncPolicyInstanceId.setStatus("current")
_CfprFirmwareAutoSyncPolicyDn_Type = CfprManagedObjectDn
_CfprFirmwareAutoSyncPolicyDn_Object = MibTableColumn
cfprFirmwareAutoSyncPolicyDn = _CfprFirmwareAutoSyncPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 2, 1, 2),
    _CfprFirmwareAutoSyncPolicyDn_Type()
)
cfprFirmwareAutoSyncPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAutoSyncPolicyDn.setStatus("current")
_CfprFirmwareAutoSyncPolicyRn_Type = SnmpAdminString
_CfprFirmwareAutoSyncPolicyRn_Object = MibTableColumn
cfprFirmwareAutoSyncPolicyRn = _CfprFirmwareAutoSyncPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 2, 1, 3),
    _CfprFirmwareAutoSyncPolicyRn_Type()
)
cfprFirmwareAutoSyncPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAutoSyncPolicyRn.setStatus("current")
_CfprFirmwareAutoSyncPolicyConfigIssue_Type = CfprFirmwareAutoSyncConfigIssue
_CfprFirmwareAutoSyncPolicyConfigIssue_Object = MibTableColumn
cfprFirmwareAutoSyncPolicyConfigIssue = _CfprFirmwareAutoSyncPolicyConfigIssue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 2, 1, 4),
    _CfprFirmwareAutoSyncPolicyConfigIssue_Type()
)
cfprFirmwareAutoSyncPolicyConfigIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAutoSyncPolicyConfigIssue.setStatus("current")
_CfprFirmwareAutoSyncPolicyDescr_Type = SnmpAdminString
_CfprFirmwareAutoSyncPolicyDescr_Object = MibTableColumn
cfprFirmwareAutoSyncPolicyDescr = _CfprFirmwareAutoSyncPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 2, 1, 5),
    _CfprFirmwareAutoSyncPolicyDescr_Type()
)
cfprFirmwareAutoSyncPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAutoSyncPolicyDescr.setStatus("current")
_CfprFirmwareAutoSyncPolicyIntId_Type = SnmpAdminString
_CfprFirmwareAutoSyncPolicyIntId_Object = MibTableColumn
cfprFirmwareAutoSyncPolicyIntId = _CfprFirmwareAutoSyncPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 2, 1, 6),
    _CfprFirmwareAutoSyncPolicyIntId_Type()
)
cfprFirmwareAutoSyncPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAutoSyncPolicyIntId.setStatus("current")
_CfprFirmwareAutoSyncPolicyName_Type = SnmpAdminString
_CfprFirmwareAutoSyncPolicyName_Object = MibTableColumn
cfprFirmwareAutoSyncPolicyName = _CfprFirmwareAutoSyncPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 2, 1, 7),
    _CfprFirmwareAutoSyncPolicyName_Type()
)
cfprFirmwareAutoSyncPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAutoSyncPolicyName.setStatus("current")
_CfprFirmwareAutoSyncPolicyPolicyLevel_Type = Gauge32
_CfprFirmwareAutoSyncPolicyPolicyLevel_Object = MibTableColumn
cfprFirmwareAutoSyncPolicyPolicyLevel = _CfprFirmwareAutoSyncPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 2, 1, 8),
    _CfprFirmwareAutoSyncPolicyPolicyLevel_Type()
)
cfprFirmwareAutoSyncPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAutoSyncPolicyPolicyLevel.setStatus("current")
_CfprFirmwareAutoSyncPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwareAutoSyncPolicyPolicyOwner_Object = MibTableColumn
cfprFirmwareAutoSyncPolicyPolicyOwner = _CfprFirmwareAutoSyncPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 2, 1, 9),
    _CfprFirmwareAutoSyncPolicyPolicyOwner_Type()
)
cfprFirmwareAutoSyncPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAutoSyncPolicyPolicyOwner.setStatus("current")
_CfprFirmwareAutoSyncPolicySyncState_Type = CfprFirmwareAutoSyncState
_CfprFirmwareAutoSyncPolicySyncState_Object = MibTableColumn
cfprFirmwareAutoSyncPolicySyncState = _CfprFirmwareAutoSyncPolicySyncState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 2, 1, 10),
    _CfprFirmwareAutoSyncPolicySyncState_Type()
)
cfprFirmwareAutoSyncPolicySyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareAutoSyncPolicySyncState.setStatus("current")
_CfprFirmwareBladeTable_Object = MibTable
cfprFirmwareBladeTable = _CfprFirmwareBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 3)
)
if mibBuilder.loadTexts:
    cfprFirmwareBladeTable.setStatus("current")
_CfprFirmwareBladeEntry_Object = MibTableRow
cfprFirmwareBladeEntry = _CfprFirmwareBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 3, 1)
)
cfprFirmwareBladeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareBladeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareBladeEntry.setStatus("current")
_CfprFirmwareBladeInstanceId_Type = CfprManagedObjectId
_CfprFirmwareBladeInstanceId_Object = MibTableColumn
cfprFirmwareBladeInstanceId = _CfprFirmwareBladeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 3, 1, 1),
    _CfprFirmwareBladeInstanceId_Type()
)
cfprFirmwareBladeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareBladeInstanceId.setStatus("current")
_CfprFirmwareBladeDn_Type = CfprManagedObjectDn
_CfprFirmwareBladeDn_Object = MibTableColumn
cfprFirmwareBladeDn = _CfprFirmwareBladeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 3, 1, 2),
    _CfprFirmwareBladeDn_Type()
)
cfprFirmwareBladeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBladeDn.setStatus("current")
_CfprFirmwareBladeRn_Type = SnmpAdminString
_CfprFirmwareBladeRn_Object = MibTableColumn
cfprFirmwareBladeRn = _CfprFirmwareBladeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 3, 1, 3),
    _CfprFirmwareBladeRn_Type()
)
cfprFirmwareBladeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBladeRn.setStatus("current")
_CfprFirmwareBladeOperVersion_Type = SnmpAdminString
_CfprFirmwareBladeOperVersion_Object = MibTableColumn
cfprFirmwareBladeOperVersion = _CfprFirmwareBladeOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 3, 1, 4),
    _CfprFirmwareBladeOperVersion_Type()
)
cfprFirmwareBladeOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBladeOperVersion.setStatus("current")
_CfprFirmwareBootDefinitionTable_Object = MibTable
cfprFirmwareBootDefinitionTable = _CfprFirmwareBootDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 4)
)
if mibBuilder.loadTexts:
    cfprFirmwareBootDefinitionTable.setStatus("current")
_CfprFirmwareBootDefinitionEntry_Object = MibTableRow
cfprFirmwareBootDefinitionEntry = _CfprFirmwareBootDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 4, 1)
)
cfprFirmwareBootDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareBootDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareBootDefinitionEntry.setStatus("current")
_CfprFirmwareBootDefinitionInstanceId_Type = CfprManagedObjectId
_CfprFirmwareBootDefinitionInstanceId_Object = MibTableColumn
cfprFirmwareBootDefinitionInstanceId = _CfprFirmwareBootDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 4, 1, 1),
    _CfprFirmwareBootDefinitionInstanceId_Type()
)
cfprFirmwareBootDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareBootDefinitionInstanceId.setStatus("current")
_CfprFirmwareBootDefinitionDn_Type = CfprManagedObjectDn
_CfprFirmwareBootDefinitionDn_Object = MibTableColumn
cfprFirmwareBootDefinitionDn = _CfprFirmwareBootDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 4, 1, 2),
    _CfprFirmwareBootDefinitionDn_Type()
)
cfprFirmwareBootDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootDefinitionDn.setStatus("current")
_CfprFirmwareBootDefinitionRn_Type = SnmpAdminString
_CfprFirmwareBootDefinitionRn_Object = MibTableColumn
cfprFirmwareBootDefinitionRn = _CfprFirmwareBootDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 4, 1, 3),
    _CfprFirmwareBootDefinitionRn_Type()
)
cfprFirmwareBootDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootDefinitionRn.setStatus("current")
_CfprFirmwareBootDefinitionType_Type = CfprFirmwareType
_CfprFirmwareBootDefinitionType_Object = MibTableColumn
cfprFirmwareBootDefinitionType = _CfprFirmwareBootDefinitionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 4, 1, 4),
    _CfprFirmwareBootDefinitionType_Type()
)
cfprFirmwareBootDefinitionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootDefinitionType.setStatus("current")
_CfprFirmwareBootUnitTable_Object = MibTable
cfprFirmwareBootUnitTable = _CfprFirmwareBootUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5)
)
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitTable.setStatus("current")
_CfprFirmwareBootUnitEntry_Object = MibTableRow
cfprFirmwareBootUnitEntry = _CfprFirmwareBootUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1)
)
cfprFirmwareBootUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareBootUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitEntry.setStatus("current")
_CfprFirmwareBootUnitInstanceId_Type = CfprManagedObjectId
_CfprFirmwareBootUnitInstanceId_Object = MibTableColumn
cfprFirmwareBootUnitInstanceId = _CfprFirmwareBootUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 1),
    _CfprFirmwareBootUnitInstanceId_Type()
)
cfprFirmwareBootUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitInstanceId.setStatus("current")
_CfprFirmwareBootUnitDn_Type = CfprManagedObjectDn
_CfprFirmwareBootUnitDn_Object = MibTableColumn
cfprFirmwareBootUnitDn = _CfprFirmwareBootUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 2),
    _CfprFirmwareBootUnitDn_Type()
)
cfprFirmwareBootUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitDn.setStatus("current")
_CfprFirmwareBootUnitRn_Type = SnmpAdminString
_CfprFirmwareBootUnitRn_Object = MibTableColumn
cfprFirmwareBootUnitRn = _CfprFirmwareBootUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 3),
    _CfprFirmwareBootUnitRn_Type()
)
cfprFirmwareBootUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitRn.setStatus("current")
_CfprFirmwareBootUnitAdminState_Type = CfprFirmwareTriggerState
_CfprFirmwareBootUnitAdminState_Object = MibTableColumn
cfprFirmwareBootUnitAdminState = _CfprFirmwareBootUnitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 4),
    _CfprFirmwareBootUnitAdminState_Type()
)
cfprFirmwareBootUnitAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitAdminState.setStatus("current")
_CfprFirmwareBootUnitIgnoreCompCheck_Type = TruthValue
_CfprFirmwareBootUnitIgnoreCompCheck_Object = MibTableColumn
cfprFirmwareBootUnitIgnoreCompCheck = _CfprFirmwareBootUnitIgnoreCompCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 5),
    _CfprFirmwareBootUnitIgnoreCompCheck_Type()
)
cfprFirmwareBootUnitIgnoreCompCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitIgnoreCompCheck.setStatus("current")
_CfprFirmwareBootUnitImage_Type = CfprFirmwareBootUnitImage
_CfprFirmwareBootUnitImage_Object = MibTableColumn
cfprFirmwareBootUnitImage = _CfprFirmwareBootUnitImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 6),
    _CfprFirmwareBootUnitImage_Type()
)
cfprFirmwareBootUnitImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitImage.setStatus("current")
_CfprFirmwareBootUnitInvTag_Type = SnmpAdminString
_CfprFirmwareBootUnitInvTag_Object = MibTableColumn
cfprFirmwareBootUnitInvTag = _CfprFirmwareBootUnitInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 7),
    _CfprFirmwareBootUnitInvTag_Type()
)
cfprFirmwareBootUnitInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitInvTag.setStatus("current")
_CfprFirmwareBootUnitMode_Type = CfprFirmwareBootUnitMode
_CfprFirmwareBootUnitMode_Object = MibTableColumn
cfprFirmwareBootUnitMode = _CfprFirmwareBootUnitMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 8),
    _CfprFirmwareBootUnitMode_Type()
)
cfprFirmwareBootUnitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitMode.setStatus("current")
_CfprFirmwareBootUnitOperState_Type = CfprFirmwareImageState
_CfprFirmwareBootUnitOperState_Object = MibTableColumn
cfprFirmwareBootUnitOperState = _CfprFirmwareBootUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 9),
    _CfprFirmwareBootUnitOperState_Type()
)
cfprFirmwareBootUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitOperState.setStatus("current")
_CfprFirmwareBootUnitPrevVersion_Type = SnmpAdminString
_CfprFirmwareBootUnitPrevVersion_Object = MibTableColumn
cfprFirmwareBootUnitPrevVersion = _CfprFirmwareBootUnitPrevVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 10),
    _CfprFirmwareBootUnitPrevVersion_Type()
)
cfprFirmwareBootUnitPrevVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitPrevVersion.setStatus("current")
_CfprFirmwareBootUnitResetOnActivate_Type = TruthValue
_CfprFirmwareBootUnitResetOnActivate_Object = MibTableColumn
cfprFirmwareBootUnitResetOnActivate = _CfprFirmwareBootUnitResetOnActivate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 11),
    _CfprFirmwareBootUnitResetOnActivate_Type()
)
cfprFirmwareBootUnitResetOnActivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitResetOnActivate.setStatus("current")
_CfprFirmwareBootUnitSkipValidation_Type = TruthValue
_CfprFirmwareBootUnitSkipValidation_Object = MibTableColumn
cfprFirmwareBootUnitSkipValidation = _CfprFirmwareBootUnitSkipValidation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 12),
    _CfprFirmwareBootUnitSkipValidation_Type()
)
cfprFirmwareBootUnitSkipValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitSkipValidation.setStatus("current")
_CfprFirmwareBootUnitType_Type = CfprFirmwareComponentType
_CfprFirmwareBootUnitType_Object = MibTableColumn
cfprFirmwareBootUnitType = _CfprFirmwareBootUnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 13),
    _CfprFirmwareBootUnitType_Type()
)
cfprFirmwareBootUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitType.setStatus("current")
_CfprFirmwareBootUnitVersion_Type = SnmpAdminString
_CfprFirmwareBootUnitVersion_Object = MibTableColumn
cfprFirmwareBootUnitVersion = _CfprFirmwareBootUnitVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 14),
    _CfprFirmwareBootUnitVersion_Type()
)
cfprFirmwareBootUnitVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitVersion.setStatus("current")
_CfprFirmwareBootUnitMioSsdmodel_Type = SnmpAdminString
_CfprFirmwareBootUnitMioSsdmodel_Object = MibTableColumn
cfprFirmwareBootUnitMioSsdmodel = _CfprFirmwareBootUnitMioSsdmodel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 5, 1, 15),
    _CfprFirmwareBootUnitMioSsdmodel_Type()
)
cfprFirmwareBootUnitMioSsdmodel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBootUnitMioSsdmodel.setStatus("current")
_CfprFirmwareBundleInfoTable_Object = MibTable
cfprFirmwareBundleInfoTable = _CfprFirmwareBundleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 6)
)
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoTable.setStatus("current")
_CfprFirmwareBundleInfoEntry_Object = MibTableRow
cfprFirmwareBundleInfoEntry = _CfprFirmwareBundleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 6, 1)
)
cfprFirmwareBundleInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareBundleInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoEntry.setStatus("current")
_CfprFirmwareBundleInfoInstanceId_Type = CfprManagedObjectId
_CfprFirmwareBundleInfoInstanceId_Object = MibTableColumn
cfprFirmwareBundleInfoInstanceId = _CfprFirmwareBundleInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 6, 1, 1),
    _CfprFirmwareBundleInfoInstanceId_Type()
)
cfprFirmwareBundleInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoInstanceId.setStatus("current")
_CfprFirmwareBundleInfoDn_Type = CfprManagedObjectDn
_CfprFirmwareBundleInfoDn_Object = MibTableColumn
cfprFirmwareBundleInfoDn = _CfprFirmwareBundleInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 6, 1, 2),
    _CfprFirmwareBundleInfoDn_Type()
)
cfprFirmwareBundleInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoDn.setStatus("current")
_CfprFirmwareBundleInfoRn_Type = SnmpAdminString
_CfprFirmwareBundleInfoRn_Object = MibTableColumn
cfprFirmwareBundleInfoRn = _CfprFirmwareBundleInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 6, 1, 3),
    _CfprFirmwareBundleInfoRn_Type()
)
cfprFirmwareBundleInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoRn.setStatus("current")
_CfprFirmwareBundleInfoType_Type = CfprFirmwareDistributableType
_CfprFirmwareBundleInfoType_Object = MibTableColumn
cfprFirmwareBundleInfoType = _CfprFirmwareBundleInfoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 6, 1, 4),
    _CfprFirmwareBundleInfoType_Type()
)
cfprFirmwareBundleInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoType.setStatus("current")
_CfprFirmwareBundleInfoVersion_Type = SnmpAdminString
_CfprFirmwareBundleInfoVersion_Object = MibTableColumn
cfprFirmwareBundleInfoVersion = _CfprFirmwareBundleInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 6, 1, 5),
    _CfprFirmwareBundleInfoVersion_Type()
)
cfprFirmwareBundleInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoVersion.setStatus("current")
_CfprFirmwareBundleInfoSecModelSupported_Type = SnmpAdminString
_CfprFirmwareBundleInfoSecModelSupported_Object = MibTableColumn
cfprFirmwareBundleInfoSecModelSupported = _CfprFirmwareBundleInfoSecModelSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 6, 1, 6),
    _CfprFirmwareBundleInfoSecModelSupported_Type()
)
cfprFirmwareBundleInfoSecModelSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoSecModelSupported.setStatus("current")
_CfprFirmwareBundleInfoDigestTable_Object = MibTable
cfprFirmwareBundleInfoDigestTable = _CfprFirmwareBundleInfoDigestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 7)
)
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoDigestTable.setStatus("current")
_CfprFirmwareBundleInfoDigestEntry_Object = MibTableRow
cfprFirmwareBundleInfoDigestEntry = _CfprFirmwareBundleInfoDigestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 7, 1)
)
cfprFirmwareBundleInfoDigestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareBundleInfoDigestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoDigestEntry.setStatus("current")
_CfprFirmwareBundleInfoDigestInstanceId_Type = CfprManagedObjectId
_CfprFirmwareBundleInfoDigestInstanceId_Object = MibTableColumn
cfprFirmwareBundleInfoDigestInstanceId = _CfprFirmwareBundleInfoDigestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 7, 1, 1),
    _CfprFirmwareBundleInfoDigestInstanceId_Type()
)
cfprFirmwareBundleInfoDigestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoDigestInstanceId.setStatus("current")
_CfprFirmwareBundleInfoDigestDn_Type = CfprManagedObjectDn
_CfprFirmwareBundleInfoDigestDn_Object = MibTableColumn
cfprFirmwareBundleInfoDigestDn = _CfprFirmwareBundleInfoDigestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 7, 1, 2),
    _CfprFirmwareBundleInfoDigestDn_Type()
)
cfprFirmwareBundleInfoDigestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoDigestDn.setStatus("current")
_CfprFirmwareBundleInfoDigestRn_Type = SnmpAdminString
_CfprFirmwareBundleInfoDigestRn_Object = MibTableColumn
cfprFirmwareBundleInfoDigestRn = _CfprFirmwareBundleInfoDigestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 7, 1, 3),
    _CfprFirmwareBundleInfoDigestRn_Type()
)
cfprFirmwareBundleInfoDigestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoDigestRn.setStatus("current")
_CfprFirmwareBundleInfoDigestBundleName_Type = SnmpAdminString
_CfprFirmwareBundleInfoDigestBundleName_Object = MibTableColumn
cfprFirmwareBundleInfoDigestBundleName = _CfprFirmwareBundleInfoDigestBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 7, 1, 4),
    _CfprFirmwareBundleInfoDigestBundleName_Type()
)
cfprFirmwareBundleInfoDigestBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoDigestBundleName.setStatus("current")
_CfprFirmwareBundleInfoDigestType_Type = CfprFirmwareDistributableType
_CfprFirmwareBundleInfoDigestType_Object = MibTableColumn
cfprFirmwareBundleInfoDigestType = _CfprFirmwareBundleInfoDigestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 7, 1, 5),
    _CfprFirmwareBundleInfoDigestType_Type()
)
cfprFirmwareBundleInfoDigestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoDigestType.setStatus("current")
_CfprFirmwareBundleInfoDigestVersion_Type = SnmpAdminString
_CfprFirmwareBundleInfoDigestVersion_Object = MibTableColumn
cfprFirmwareBundleInfoDigestVersion = _CfprFirmwareBundleInfoDigestVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 7, 1, 6),
    _CfprFirmwareBundleInfoDigestVersion_Type()
)
cfprFirmwareBundleInfoDigestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleInfoDigestVersion.setStatus("current")
_CfprFirmwareBundleTypeTable_Object = MibTable
cfprFirmwareBundleTypeTable = _CfprFirmwareBundleTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 8)
)
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeTable.setStatus("current")
_CfprFirmwareBundleTypeEntry_Object = MibTableRow
cfprFirmwareBundleTypeEntry = _CfprFirmwareBundleTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 8, 1)
)
cfprFirmwareBundleTypeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareBundleTypeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeEntry.setStatus("current")
_CfprFirmwareBundleTypeInstanceId_Type = CfprManagedObjectId
_CfprFirmwareBundleTypeInstanceId_Object = MibTableColumn
cfprFirmwareBundleTypeInstanceId = _CfprFirmwareBundleTypeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 8, 1, 1),
    _CfprFirmwareBundleTypeInstanceId_Type()
)
cfprFirmwareBundleTypeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeInstanceId.setStatus("current")
_CfprFirmwareBundleTypeDn_Type = CfprManagedObjectDn
_CfprFirmwareBundleTypeDn_Object = MibTableColumn
cfprFirmwareBundleTypeDn = _CfprFirmwareBundleTypeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 8, 1, 2),
    _CfprFirmwareBundleTypeDn_Type()
)
cfprFirmwareBundleTypeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeDn.setStatus("current")
_CfprFirmwareBundleTypeRn_Type = SnmpAdminString
_CfprFirmwareBundleTypeRn_Object = MibTableColumn
cfprFirmwareBundleTypeRn = _CfprFirmwareBundleTypeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 8, 1, 3),
    _CfprFirmwareBundleTypeRn_Type()
)
cfprFirmwareBundleTypeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeRn.setStatus("current")
_CfprFirmwareBundleTypeInvTag_Type = SnmpAdminString
_CfprFirmwareBundleTypeInvTag_Object = MibTableColumn
cfprFirmwareBundleTypeInvTag = _CfprFirmwareBundleTypeInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 8, 1, 4),
    _CfprFirmwareBundleTypeInvTag_Type()
)
cfprFirmwareBundleTypeInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeInvTag.setStatus("current")
_CfprFirmwareBundleTypeType_Type = CfprFirmwareDistributableType
_CfprFirmwareBundleTypeType_Object = MibTableColumn
cfprFirmwareBundleTypeType = _CfprFirmwareBundleTypeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 8, 1, 5),
    _CfprFirmwareBundleTypeType_Type()
)
cfprFirmwareBundleTypeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeType.setStatus("current")
_CfprFirmwareBundleTypeCapProviderTable_Object = MibTable
cfprFirmwareBundleTypeCapProviderTable = _CfprFirmwareBundleTypeCapProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9)
)
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderTable.setStatus("current")
_CfprFirmwareBundleTypeCapProviderEntry_Object = MibTableRow
cfprFirmwareBundleTypeCapProviderEntry = _CfprFirmwareBundleTypeCapProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1)
)
cfprFirmwareBundleTypeCapProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareBundleTypeCapProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderEntry.setStatus("current")
_CfprFirmwareBundleTypeCapProviderInstanceId_Type = CfprManagedObjectId
_CfprFirmwareBundleTypeCapProviderInstanceId_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderInstanceId = _CfprFirmwareBundleTypeCapProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 1),
    _CfprFirmwareBundleTypeCapProviderInstanceId_Type()
)
cfprFirmwareBundleTypeCapProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderInstanceId.setStatus("current")
_CfprFirmwareBundleTypeCapProviderDn_Type = CfprManagedObjectDn
_CfprFirmwareBundleTypeCapProviderDn_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderDn = _CfprFirmwareBundleTypeCapProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 2),
    _CfprFirmwareBundleTypeCapProviderDn_Type()
)
cfprFirmwareBundleTypeCapProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderDn.setStatus("current")
_CfprFirmwareBundleTypeCapProviderRn_Type = SnmpAdminString
_CfprFirmwareBundleTypeCapProviderRn_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderRn = _CfprFirmwareBundleTypeCapProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 3),
    _CfprFirmwareBundleTypeCapProviderRn_Type()
)
cfprFirmwareBundleTypeCapProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderRn.setStatus("current")
_CfprFirmwareBundleTypeCapProviderDeleted_Type = TruthValue
_CfprFirmwareBundleTypeCapProviderDeleted_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderDeleted = _CfprFirmwareBundleTypeCapProviderDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 4),
    _CfprFirmwareBundleTypeCapProviderDeleted_Type()
)
cfprFirmwareBundleTypeCapProviderDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderDeleted.setStatus("current")
_CfprFirmwareBundleTypeCapProviderDeprecated_Type = TruthValue
_CfprFirmwareBundleTypeCapProviderDeprecated_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderDeprecated = _CfprFirmwareBundleTypeCapProviderDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 5),
    _CfprFirmwareBundleTypeCapProviderDeprecated_Type()
)
cfprFirmwareBundleTypeCapProviderDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderDeprecated.setStatus("current")
_CfprFirmwareBundleTypeCapProviderElementLoadFailures_Type = Gauge32
_CfprFirmwareBundleTypeCapProviderElementLoadFailures_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderElementLoadFailures = _CfprFirmwareBundleTypeCapProviderElementLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 6),
    _CfprFirmwareBundleTypeCapProviderElementLoadFailures_Type()
)
cfprFirmwareBundleTypeCapProviderElementLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderElementLoadFailures.setStatus("current")
_CfprFirmwareBundleTypeCapProviderElementsLoaded_Type = Gauge32
_CfprFirmwareBundleTypeCapProviderElementsLoaded_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderElementsLoaded = _CfprFirmwareBundleTypeCapProviderElementsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 7),
    _CfprFirmwareBundleTypeCapProviderElementsLoaded_Type()
)
cfprFirmwareBundleTypeCapProviderElementsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderElementsLoaded.setStatus("current")
_CfprFirmwareBundleTypeCapProviderGencount_Type = Gauge32
_CfprFirmwareBundleTypeCapProviderGencount_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderGencount = _CfprFirmwareBundleTypeCapProviderGencount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 8),
    _CfprFirmwareBundleTypeCapProviderGencount_Type()
)
cfprFirmwareBundleTypeCapProviderGencount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderGencount.setStatus("current")
_CfprFirmwareBundleTypeCapProviderLoadErrors_Type = Gauge32
_CfprFirmwareBundleTypeCapProviderLoadErrors_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderLoadErrors = _CfprFirmwareBundleTypeCapProviderLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 9),
    _CfprFirmwareBundleTypeCapProviderLoadErrors_Type()
)
cfprFirmwareBundleTypeCapProviderLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderLoadErrors.setStatus("current")
_CfprFirmwareBundleTypeCapProviderLoadWarnings_Type = Gauge32
_CfprFirmwareBundleTypeCapProviderLoadWarnings_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderLoadWarnings = _CfprFirmwareBundleTypeCapProviderLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 10),
    _CfprFirmwareBundleTypeCapProviderLoadWarnings_Type()
)
cfprFirmwareBundleTypeCapProviderLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderLoadWarnings.setStatus("current")
_CfprFirmwareBundleTypeCapProviderMgmtPlaneVer_Type = SnmpAdminString
_CfprFirmwareBundleTypeCapProviderMgmtPlaneVer_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderMgmtPlaneVer = _CfprFirmwareBundleTypeCapProviderMgmtPlaneVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 11),
    _CfprFirmwareBundleTypeCapProviderMgmtPlaneVer_Type()
)
cfprFirmwareBundleTypeCapProviderMgmtPlaneVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderMgmtPlaneVer.setStatus("current")
_CfprFirmwareBundleTypeCapProviderModel_Type = SnmpAdminString
_CfprFirmwareBundleTypeCapProviderModel_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderModel = _CfprFirmwareBundleTypeCapProviderModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 12),
    _CfprFirmwareBundleTypeCapProviderModel_Type()
)
cfprFirmwareBundleTypeCapProviderModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderModel.setStatus("current")
_CfprFirmwareBundleTypeCapProviderPlatformType_Type = CfprFirmwarePlatformType
_CfprFirmwareBundleTypeCapProviderPlatformType_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderPlatformType = _CfprFirmwareBundleTypeCapProviderPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 13),
    _CfprFirmwareBundleTypeCapProviderPlatformType_Type()
)
cfprFirmwareBundleTypeCapProviderPlatformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderPlatformType.setStatus("current")
_CfprFirmwareBundleTypeCapProviderVendor_Type = SnmpAdminString
_CfprFirmwareBundleTypeCapProviderVendor_Object = MibTableColumn
cfprFirmwareBundleTypeCapProviderVendor = _CfprFirmwareBundleTypeCapProviderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 9, 1, 14),
    _CfprFirmwareBundleTypeCapProviderVendor_Type()
)
cfprFirmwareBundleTypeCapProviderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareBundleTypeCapProviderVendor.setStatus("current")
_CfprFirmwareCatalogPackTable_Object = MibTable
cfprFirmwareCatalogPackTable = _CfprFirmwareCatalogPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10)
)
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackTable.setStatus("current")
_CfprFirmwareCatalogPackEntry_Object = MibTableRow
cfprFirmwareCatalogPackEntry = _CfprFirmwareCatalogPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1)
)
cfprFirmwareCatalogPackEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareCatalogPackInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackEntry.setStatus("current")
_CfprFirmwareCatalogPackInstanceId_Type = CfprManagedObjectId
_CfprFirmwareCatalogPackInstanceId_Object = MibTableColumn
cfprFirmwareCatalogPackInstanceId = _CfprFirmwareCatalogPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 1),
    _CfprFirmwareCatalogPackInstanceId_Type()
)
cfprFirmwareCatalogPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackInstanceId.setStatus("current")
_CfprFirmwareCatalogPackDn_Type = CfprManagedObjectDn
_CfprFirmwareCatalogPackDn_Object = MibTableColumn
cfprFirmwareCatalogPackDn = _CfprFirmwareCatalogPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 2),
    _CfprFirmwareCatalogPackDn_Type()
)
cfprFirmwareCatalogPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackDn.setStatus("current")
_CfprFirmwareCatalogPackRn_Type = SnmpAdminString
_CfprFirmwareCatalogPackRn_Object = MibTableColumn
cfprFirmwareCatalogPackRn = _CfprFirmwareCatalogPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 3),
    _CfprFirmwareCatalogPackRn_Type()
)
cfprFirmwareCatalogPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackRn.setStatus("current")
_CfprFirmwareCatalogPackCatalogName_Type = SnmpAdminString
_CfprFirmwareCatalogPackCatalogName_Object = MibTableColumn
cfprFirmwareCatalogPackCatalogName = _CfprFirmwareCatalogPackCatalogName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 4),
    _CfprFirmwareCatalogPackCatalogName_Type()
)
cfprFirmwareCatalogPackCatalogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackCatalogName.setStatus("current")
_CfprFirmwareCatalogPackCatalogVersion_Type = SnmpAdminString
_CfprFirmwareCatalogPackCatalogVersion_Object = MibTableColumn
cfprFirmwareCatalogPackCatalogVersion = _CfprFirmwareCatalogPackCatalogVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 5),
    _CfprFirmwareCatalogPackCatalogVersion_Type()
)
cfprFirmwareCatalogPackCatalogVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackCatalogVersion.setStatus("current")
_CfprFirmwareCatalogPackConfigState_Type = CfprFirmwareCatalogPackConfigState
_CfprFirmwareCatalogPackConfigState_Object = MibTableColumn
cfprFirmwareCatalogPackConfigState = _CfprFirmwareCatalogPackConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 6),
    _CfprFirmwareCatalogPackConfigState_Type()
)
cfprFirmwareCatalogPackConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackConfigState.setStatus("current")
_CfprFirmwareCatalogPackConfigStatusMessage_Type = SnmpAdminString
_CfprFirmwareCatalogPackConfigStatusMessage_Object = MibTableColumn
cfprFirmwareCatalogPackConfigStatusMessage = _CfprFirmwareCatalogPackConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 7),
    _CfprFirmwareCatalogPackConfigStatusMessage_Type()
)
cfprFirmwareCatalogPackConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackConfigStatusMessage.setStatus("current")
_CfprFirmwareCatalogPackDescr_Type = SnmpAdminString
_CfprFirmwareCatalogPackDescr_Object = MibTableColumn
cfprFirmwareCatalogPackDescr = _CfprFirmwareCatalogPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 8),
    _CfprFirmwareCatalogPackDescr_Type()
)
cfprFirmwareCatalogPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackDescr.setStatus("current")
_CfprFirmwareCatalogPackIntId_Type = SnmpAdminString
_CfprFirmwareCatalogPackIntId_Object = MibTableColumn
cfprFirmwareCatalogPackIntId = _CfprFirmwareCatalogPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 9),
    _CfprFirmwareCatalogPackIntId_Type()
)
cfprFirmwareCatalogPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackIntId.setStatus("current")
_CfprFirmwareCatalogPackMode_Type = CfprFirmwarePackMode
_CfprFirmwareCatalogPackMode_Object = MibTableColumn
cfprFirmwareCatalogPackMode = _CfprFirmwareCatalogPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 10),
    _CfprFirmwareCatalogPackMode_Type()
)
cfprFirmwareCatalogPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackMode.setStatus("current")
_CfprFirmwareCatalogPackName_Type = SnmpAdminString
_CfprFirmwareCatalogPackName_Object = MibTableColumn
cfprFirmwareCatalogPackName = _CfprFirmwareCatalogPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 11),
    _CfprFirmwareCatalogPackName_Type()
)
cfprFirmwareCatalogPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackName.setStatus("current")
_CfprFirmwareCatalogPackPolicyLevel_Type = Gauge32
_CfprFirmwareCatalogPackPolicyLevel_Object = MibTableColumn
cfprFirmwareCatalogPackPolicyLevel = _CfprFirmwareCatalogPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 12),
    _CfprFirmwareCatalogPackPolicyLevel_Type()
)
cfprFirmwareCatalogPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackPolicyLevel.setStatus("current")
_CfprFirmwareCatalogPackPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwareCatalogPackPolicyOwner_Object = MibTableColumn
cfprFirmwareCatalogPackPolicyOwner = _CfprFirmwareCatalogPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 13),
    _CfprFirmwareCatalogPackPolicyOwner_Type()
)
cfprFirmwareCatalogPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackPolicyOwner.setStatus("current")
_CfprFirmwareCatalogPackStageSize_Type = Gauge32
_CfprFirmwareCatalogPackStageSize_Object = MibTableColumn
cfprFirmwareCatalogPackStageSize = _CfprFirmwareCatalogPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 14),
    _CfprFirmwareCatalogPackStageSize_Type()
)
cfprFirmwareCatalogPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackStageSize.setStatus("current")
_CfprFirmwareCatalogPackUpdateTrigger_Type = DateAndTime
_CfprFirmwareCatalogPackUpdateTrigger_Object = MibTableColumn
cfprFirmwareCatalogPackUpdateTrigger = _CfprFirmwareCatalogPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 10, 1, 15),
    _CfprFirmwareCatalogPackUpdateTrigger_Type()
)
cfprFirmwareCatalogPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogPackUpdateTrigger.setStatus("current")
_CfprFirmwareCatalogueTable_Object = MibTable
cfprFirmwareCatalogueTable = _CfprFirmwareCatalogueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 11)
)
if mibBuilder.loadTexts:
    cfprFirmwareCatalogueTable.setStatus("current")
_CfprFirmwareCatalogueEntry_Object = MibTableRow
cfprFirmwareCatalogueEntry = _CfprFirmwareCatalogueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 11, 1)
)
cfprFirmwareCatalogueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareCatalogueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareCatalogueEntry.setStatus("current")
_CfprFirmwareCatalogueInstanceId_Type = CfprManagedObjectId
_CfprFirmwareCatalogueInstanceId_Object = MibTableColumn
cfprFirmwareCatalogueInstanceId = _CfprFirmwareCatalogueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 11, 1, 1),
    _CfprFirmwareCatalogueInstanceId_Type()
)
cfprFirmwareCatalogueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogueInstanceId.setStatus("current")
_CfprFirmwareCatalogueDn_Type = CfprManagedObjectDn
_CfprFirmwareCatalogueDn_Object = MibTableColumn
cfprFirmwareCatalogueDn = _CfprFirmwareCatalogueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 11, 1, 2),
    _CfprFirmwareCatalogueDn_Type()
)
cfprFirmwareCatalogueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogueDn.setStatus("current")
_CfprFirmwareCatalogueRn_Type = SnmpAdminString
_CfprFirmwareCatalogueRn_Object = MibTableColumn
cfprFirmwareCatalogueRn = _CfprFirmwareCatalogueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 11, 1, 3),
    _CfprFirmwareCatalogueRn_Type()
)
cfprFirmwareCatalogueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogueRn.setStatus("current")
_CfprFirmwareCatalogueSyncTrigger_Type = TruthValue
_CfprFirmwareCatalogueSyncTrigger_Object = MibTableColumn
cfprFirmwareCatalogueSyncTrigger = _CfprFirmwareCatalogueSyncTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 11, 1, 4),
    _CfprFirmwareCatalogueSyncTrigger_Type()
)
cfprFirmwareCatalogueSyncTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCatalogueSyncTrigger.setStatus("current")
_CfprFirmwareCompSourceTable_Object = MibTable
cfprFirmwareCompSourceTable = _CfprFirmwareCompSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 12)
)
if mibBuilder.loadTexts:
    cfprFirmwareCompSourceTable.setStatus("current")
_CfprFirmwareCompSourceEntry_Object = MibTableRow
cfprFirmwareCompSourceEntry = _CfprFirmwareCompSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 12, 1)
)
cfprFirmwareCompSourceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareCompSourceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareCompSourceEntry.setStatus("current")
_CfprFirmwareCompSourceInstanceId_Type = CfprManagedObjectId
_CfprFirmwareCompSourceInstanceId_Object = MibTableColumn
cfprFirmwareCompSourceInstanceId = _CfprFirmwareCompSourceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 12, 1, 1),
    _CfprFirmwareCompSourceInstanceId_Type()
)
cfprFirmwareCompSourceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareCompSourceInstanceId.setStatus("current")
_CfprFirmwareCompSourceDn_Type = CfprManagedObjectDn
_CfprFirmwareCompSourceDn_Object = MibTableColumn
cfprFirmwareCompSourceDn = _CfprFirmwareCompSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 12, 1, 2),
    _CfprFirmwareCompSourceDn_Type()
)
cfprFirmwareCompSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompSourceDn.setStatus("current")
_CfprFirmwareCompSourceRn_Type = SnmpAdminString
_CfprFirmwareCompSourceRn_Object = MibTableColumn
cfprFirmwareCompSourceRn = _CfprFirmwareCompSourceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 12, 1, 3),
    _CfprFirmwareCompSourceRn_Type()
)
cfprFirmwareCompSourceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompSourceRn.setStatus("current")
_CfprFirmwareCompSourceDescr_Type = SnmpAdminString
_CfprFirmwareCompSourceDescr_Object = MibTableColumn
cfprFirmwareCompSourceDescr = _CfprFirmwareCompSourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 12, 1, 4),
    _CfprFirmwareCompSourceDescr_Type()
)
cfprFirmwareCompSourceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompSourceDescr.setStatus("current")
_CfprFirmwareCompSourceIntId_Type = SnmpAdminString
_CfprFirmwareCompSourceIntId_Object = MibTableColumn
cfprFirmwareCompSourceIntId = _CfprFirmwareCompSourceIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 12, 1, 5),
    _CfprFirmwareCompSourceIntId_Type()
)
cfprFirmwareCompSourceIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompSourceIntId.setStatus("current")
_CfprFirmwareCompSourceInvTag_Type = SnmpAdminString
_CfprFirmwareCompSourceInvTag_Object = MibTableColumn
cfprFirmwareCompSourceInvTag = _CfprFirmwareCompSourceInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 12, 1, 6),
    _CfprFirmwareCompSourceInvTag_Type()
)
cfprFirmwareCompSourceInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompSourceInvTag.setStatus("current")
_CfprFirmwareCompSourceName_Type = SnmpAdminString
_CfprFirmwareCompSourceName_Object = MibTableColumn
cfprFirmwareCompSourceName = _CfprFirmwareCompSourceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 12, 1, 7),
    _CfprFirmwareCompSourceName_Type()
)
cfprFirmwareCompSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompSourceName.setStatus("current")
_CfprFirmwareCompSourcePolicyLevel_Type = Gauge32
_CfprFirmwareCompSourcePolicyLevel_Object = MibTableColumn
cfprFirmwareCompSourcePolicyLevel = _CfprFirmwareCompSourcePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 12, 1, 8),
    _CfprFirmwareCompSourcePolicyLevel_Type()
)
cfprFirmwareCompSourcePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompSourcePolicyLevel.setStatus("current")
_CfprFirmwareCompSourcePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwareCompSourcePolicyOwner_Object = MibTableColumn
cfprFirmwareCompSourcePolicyOwner = _CfprFirmwareCompSourcePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 12, 1, 9),
    _CfprFirmwareCompSourcePolicyOwner_Type()
)
cfprFirmwareCompSourcePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompSourcePolicyOwner.setStatus("current")
_CfprFirmwareCompSourceVersion_Type = SnmpAdminString
_CfprFirmwareCompSourceVersion_Object = MibTableColumn
cfprFirmwareCompSourceVersion = _CfprFirmwareCompSourceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 12, 1, 10),
    _CfprFirmwareCompSourceVersion_Type()
)
cfprFirmwareCompSourceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompSourceVersion.setStatus("current")
_CfprFirmwareCompTargetTable_Object = MibTable
cfprFirmwareCompTargetTable = _CfprFirmwareCompTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 13)
)
if mibBuilder.loadTexts:
    cfprFirmwareCompTargetTable.setStatus("current")
_CfprFirmwareCompTargetEntry_Object = MibTableRow
cfprFirmwareCompTargetEntry = _CfprFirmwareCompTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 13, 1)
)
cfprFirmwareCompTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareCompTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareCompTargetEntry.setStatus("current")
_CfprFirmwareCompTargetInstanceId_Type = CfprManagedObjectId
_CfprFirmwareCompTargetInstanceId_Object = MibTableColumn
cfprFirmwareCompTargetInstanceId = _CfprFirmwareCompTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 13, 1, 1),
    _CfprFirmwareCompTargetInstanceId_Type()
)
cfprFirmwareCompTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareCompTargetInstanceId.setStatus("current")
_CfprFirmwareCompTargetDn_Type = CfprManagedObjectDn
_CfprFirmwareCompTargetDn_Object = MibTableColumn
cfprFirmwareCompTargetDn = _CfprFirmwareCompTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 13, 1, 2),
    _CfprFirmwareCompTargetDn_Type()
)
cfprFirmwareCompTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompTargetDn.setStatus("current")
_CfprFirmwareCompTargetRn_Type = SnmpAdminString
_CfprFirmwareCompTargetRn_Object = MibTableColumn
cfprFirmwareCompTargetRn = _CfprFirmwareCompTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 13, 1, 3),
    _CfprFirmwareCompTargetRn_Type()
)
cfprFirmwareCompTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompTargetRn.setStatus("current")
_CfprFirmwareCompTargetDescr_Type = SnmpAdminString
_CfprFirmwareCompTargetDescr_Object = MibTableColumn
cfprFirmwareCompTargetDescr = _CfprFirmwareCompTargetDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 13, 1, 4),
    _CfprFirmwareCompTargetDescr_Type()
)
cfprFirmwareCompTargetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompTargetDescr.setStatus("current")
_CfprFirmwareCompTargetIntId_Type = SnmpAdminString
_CfprFirmwareCompTargetIntId_Object = MibTableColumn
cfprFirmwareCompTargetIntId = _CfprFirmwareCompTargetIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 13, 1, 5),
    _CfprFirmwareCompTargetIntId_Type()
)
cfprFirmwareCompTargetIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompTargetIntId.setStatus("current")
_CfprFirmwareCompTargetInvTag_Type = SnmpAdminString
_CfprFirmwareCompTargetInvTag_Object = MibTableColumn
cfprFirmwareCompTargetInvTag = _CfprFirmwareCompTargetInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 13, 1, 6),
    _CfprFirmwareCompTargetInvTag_Type()
)
cfprFirmwareCompTargetInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompTargetInvTag.setStatus("current")
_CfprFirmwareCompTargetName_Type = SnmpAdminString
_CfprFirmwareCompTargetName_Object = MibTableColumn
cfprFirmwareCompTargetName = _CfprFirmwareCompTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 13, 1, 7),
    _CfprFirmwareCompTargetName_Type()
)
cfprFirmwareCompTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompTargetName.setStatus("current")
_CfprFirmwareCompTargetPolicyLevel_Type = Gauge32
_CfprFirmwareCompTargetPolicyLevel_Object = MibTableColumn
cfprFirmwareCompTargetPolicyLevel = _CfprFirmwareCompTargetPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 13, 1, 8),
    _CfprFirmwareCompTargetPolicyLevel_Type()
)
cfprFirmwareCompTargetPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompTargetPolicyLevel.setStatus("current")
_CfprFirmwareCompTargetPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwareCompTargetPolicyOwner_Object = MibTableColumn
cfprFirmwareCompTargetPolicyOwner = _CfprFirmwareCompTargetPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 13, 1, 9),
    _CfprFirmwareCompTargetPolicyOwner_Type()
)
cfprFirmwareCompTargetPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompTargetPolicyOwner.setStatus("current")
_CfprFirmwareCompTargetVersion_Type = SnmpAdminString
_CfprFirmwareCompTargetVersion_Object = MibTableColumn
cfprFirmwareCompTargetVersion = _CfprFirmwareCompTargetVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 13, 1, 10),
    _CfprFirmwareCompTargetVersion_Type()
)
cfprFirmwareCompTargetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCompTargetVersion.setStatus("current")
_CfprFirmwareComputeHostPackTable_Object = MibTable
cfprFirmwareComputeHostPackTable = _CfprFirmwareComputeHostPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14)
)
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackTable.setStatus("current")
_CfprFirmwareComputeHostPackEntry_Object = MibTableRow
cfprFirmwareComputeHostPackEntry = _CfprFirmwareComputeHostPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1)
)
cfprFirmwareComputeHostPackEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareComputeHostPackInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackEntry.setStatus("current")
_CfprFirmwareComputeHostPackInstanceId_Type = CfprManagedObjectId
_CfprFirmwareComputeHostPackInstanceId_Object = MibTableColumn
cfprFirmwareComputeHostPackInstanceId = _CfprFirmwareComputeHostPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 1),
    _CfprFirmwareComputeHostPackInstanceId_Type()
)
cfprFirmwareComputeHostPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackInstanceId.setStatus("current")
_CfprFirmwareComputeHostPackDn_Type = CfprManagedObjectDn
_CfprFirmwareComputeHostPackDn_Object = MibTableColumn
cfprFirmwareComputeHostPackDn = _CfprFirmwareComputeHostPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 2),
    _CfprFirmwareComputeHostPackDn_Type()
)
cfprFirmwareComputeHostPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackDn.setStatus("current")
_CfprFirmwareComputeHostPackRn_Type = SnmpAdminString
_CfprFirmwareComputeHostPackRn_Object = MibTableColumn
cfprFirmwareComputeHostPackRn = _CfprFirmwareComputeHostPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 3),
    _CfprFirmwareComputeHostPackRn_Type()
)
cfprFirmwareComputeHostPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackRn.setStatus("current")
_CfprFirmwareComputeHostPackBladeBundleName_Type = SnmpAdminString
_CfprFirmwareComputeHostPackBladeBundleName_Object = MibTableColumn
cfprFirmwareComputeHostPackBladeBundleName = _CfprFirmwareComputeHostPackBladeBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 4),
    _CfprFirmwareComputeHostPackBladeBundleName_Type()
)
cfprFirmwareComputeHostPackBladeBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackBladeBundleName.setStatus("current")
_CfprFirmwareComputeHostPackBladeBundleVersion_Type = SnmpAdminString
_CfprFirmwareComputeHostPackBladeBundleVersion_Object = MibTableColumn
cfprFirmwareComputeHostPackBladeBundleVersion = _CfprFirmwareComputeHostPackBladeBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 5),
    _CfprFirmwareComputeHostPackBladeBundleVersion_Type()
)
cfprFirmwareComputeHostPackBladeBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackBladeBundleVersion.setStatus("current")
_CfprFirmwareComputeHostPackConfigQualifier_Type = CfprFirmwareHostPackConfigQualifier
_CfprFirmwareComputeHostPackConfigQualifier_Object = MibTableColumn
cfprFirmwareComputeHostPackConfigQualifier = _CfprFirmwareComputeHostPackConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 6),
    _CfprFirmwareComputeHostPackConfigQualifier_Type()
)
cfprFirmwareComputeHostPackConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackConfigQualifier.setStatus("current")
_CfprFirmwareComputeHostPackDescr_Type = SnmpAdminString
_CfprFirmwareComputeHostPackDescr_Object = MibTableColumn
cfprFirmwareComputeHostPackDescr = _CfprFirmwareComputeHostPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 7),
    _CfprFirmwareComputeHostPackDescr_Type()
)
cfprFirmwareComputeHostPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackDescr.setStatus("current")
_CfprFirmwareComputeHostPackIgnoreCompCheck_Type = TruthValue
_CfprFirmwareComputeHostPackIgnoreCompCheck_Object = MibTableColumn
cfprFirmwareComputeHostPackIgnoreCompCheck = _CfprFirmwareComputeHostPackIgnoreCompCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 8),
    _CfprFirmwareComputeHostPackIgnoreCompCheck_Type()
)
cfprFirmwareComputeHostPackIgnoreCompCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackIgnoreCompCheck.setStatus("current")
_CfprFirmwareComputeHostPackIntId_Type = SnmpAdminString
_CfprFirmwareComputeHostPackIntId_Object = MibTableColumn
cfprFirmwareComputeHostPackIntId = _CfprFirmwareComputeHostPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 9),
    _CfprFirmwareComputeHostPackIntId_Type()
)
cfprFirmwareComputeHostPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackIntId.setStatus("current")
_CfprFirmwareComputeHostPackMode_Type = CfprFirmwarePackMode
_CfprFirmwareComputeHostPackMode_Object = MibTableColumn
cfprFirmwareComputeHostPackMode = _CfprFirmwareComputeHostPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 10),
    _CfprFirmwareComputeHostPackMode_Type()
)
cfprFirmwareComputeHostPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackMode.setStatus("current")
_CfprFirmwareComputeHostPackName_Type = SnmpAdminString
_CfprFirmwareComputeHostPackName_Object = MibTableColumn
cfprFirmwareComputeHostPackName = _CfprFirmwareComputeHostPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 11),
    _CfprFirmwareComputeHostPackName_Type()
)
cfprFirmwareComputeHostPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackName.setStatus("current")
_CfprFirmwareComputeHostPackPlatformBundleVersion_Type = SnmpAdminString
_CfprFirmwareComputeHostPackPlatformBundleVersion_Object = MibTableColumn
cfprFirmwareComputeHostPackPlatformBundleVersion = _CfprFirmwareComputeHostPackPlatformBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 12),
    _CfprFirmwareComputeHostPackPlatformBundleVersion_Type()
)
cfprFirmwareComputeHostPackPlatformBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackPlatformBundleVersion.setStatus("current")
_CfprFirmwareComputeHostPackPolicyLevel_Type = Gauge32
_CfprFirmwareComputeHostPackPolicyLevel_Object = MibTableColumn
cfprFirmwareComputeHostPackPolicyLevel = _CfprFirmwareComputeHostPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 13),
    _CfprFirmwareComputeHostPackPolicyLevel_Type()
)
cfprFirmwareComputeHostPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackPolicyLevel.setStatus("current")
_CfprFirmwareComputeHostPackPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwareComputeHostPackPolicyOwner_Object = MibTableColumn
cfprFirmwareComputeHostPackPolicyOwner = _CfprFirmwareComputeHostPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 14),
    _CfprFirmwareComputeHostPackPolicyOwner_Type()
)
cfprFirmwareComputeHostPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackPolicyOwner.setStatus("current")
_CfprFirmwareComputeHostPackRackBundleName_Type = SnmpAdminString
_CfprFirmwareComputeHostPackRackBundleName_Object = MibTableColumn
cfprFirmwareComputeHostPackRackBundleName = _CfprFirmwareComputeHostPackRackBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 15),
    _CfprFirmwareComputeHostPackRackBundleName_Type()
)
cfprFirmwareComputeHostPackRackBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackRackBundleName.setStatus("current")
_CfprFirmwareComputeHostPackRackBundleVersion_Type = SnmpAdminString
_CfprFirmwareComputeHostPackRackBundleVersion_Object = MibTableColumn
cfprFirmwareComputeHostPackRackBundleVersion = _CfprFirmwareComputeHostPackRackBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 16),
    _CfprFirmwareComputeHostPackRackBundleVersion_Type()
)
cfprFirmwareComputeHostPackRackBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackRackBundleVersion.setStatus("current")
_CfprFirmwareComputeHostPackStageSize_Type = Gauge32
_CfprFirmwareComputeHostPackStageSize_Object = MibTableColumn
cfprFirmwareComputeHostPackStageSize = _CfprFirmwareComputeHostPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 17),
    _CfprFirmwareComputeHostPackStageSize_Type()
)
cfprFirmwareComputeHostPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackStageSize.setStatus("current")
_CfprFirmwareComputeHostPackUpdateTrigger_Type = DateAndTime
_CfprFirmwareComputeHostPackUpdateTrigger_Object = MibTableColumn
cfprFirmwareComputeHostPackUpdateTrigger = _CfprFirmwareComputeHostPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 14, 1, 18),
    _CfprFirmwareComputeHostPackUpdateTrigger_Type()
)
cfprFirmwareComputeHostPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeHostPackUpdateTrigger.setStatus("current")
_CfprFirmwareComputeMgmtPackTable_Object = MibTable
cfprFirmwareComputeMgmtPackTable = _CfprFirmwareComputeMgmtPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15)
)
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackTable.setStatus("current")
_CfprFirmwareComputeMgmtPackEntry_Object = MibTableRow
cfprFirmwareComputeMgmtPackEntry = _CfprFirmwareComputeMgmtPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1)
)
cfprFirmwareComputeMgmtPackEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareComputeMgmtPackInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackEntry.setStatus("current")
_CfprFirmwareComputeMgmtPackInstanceId_Type = CfprManagedObjectId
_CfprFirmwareComputeMgmtPackInstanceId_Object = MibTableColumn
cfprFirmwareComputeMgmtPackInstanceId = _CfprFirmwareComputeMgmtPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1, 1),
    _CfprFirmwareComputeMgmtPackInstanceId_Type()
)
cfprFirmwareComputeMgmtPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackInstanceId.setStatus("current")
_CfprFirmwareComputeMgmtPackDn_Type = CfprManagedObjectDn
_CfprFirmwareComputeMgmtPackDn_Object = MibTableColumn
cfprFirmwareComputeMgmtPackDn = _CfprFirmwareComputeMgmtPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1, 2),
    _CfprFirmwareComputeMgmtPackDn_Type()
)
cfprFirmwareComputeMgmtPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackDn.setStatus("current")
_CfprFirmwareComputeMgmtPackRn_Type = SnmpAdminString
_CfprFirmwareComputeMgmtPackRn_Object = MibTableColumn
cfprFirmwareComputeMgmtPackRn = _CfprFirmwareComputeMgmtPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1, 3),
    _CfprFirmwareComputeMgmtPackRn_Type()
)
cfprFirmwareComputeMgmtPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackRn.setStatus("current")
_CfprFirmwareComputeMgmtPackDescr_Type = SnmpAdminString
_CfprFirmwareComputeMgmtPackDescr_Object = MibTableColumn
cfprFirmwareComputeMgmtPackDescr = _CfprFirmwareComputeMgmtPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1, 4),
    _CfprFirmwareComputeMgmtPackDescr_Type()
)
cfprFirmwareComputeMgmtPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackDescr.setStatus("current")
_CfprFirmwareComputeMgmtPackIgnoreCompCheck_Type = TruthValue
_CfprFirmwareComputeMgmtPackIgnoreCompCheck_Object = MibTableColumn
cfprFirmwareComputeMgmtPackIgnoreCompCheck = _CfprFirmwareComputeMgmtPackIgnoreCompCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1, 5),
    _CfprFirmwareComputeMgmtPackIgnoreCompCheck_Type()
)
cfprFirmwareComputeMgmtPackIgnoreCompCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackIgnoreCompCheck.setStatus("current")
_CfprFirmwareComputeMgmtPackIntId_Type = SnmpAdminString
_CfprFirmwareComputeMgmtPackIntId_Object = MibTableColumn
cfprFirmwareComputeMgmtPackIntId = _CfprFirmwareComputeMgmtPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1, 6),
    _CfprFirmwareComputeMgmtPackIntId_Type()
)
cfprFirmwareComputeMgmtPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackIntId.setStatus("current")
_CfprFirmwareComputeMgmtPackMode_Type = CfprFirmwarePackMode
_CfprFirmwareComputeMgmtPackMode_Object = MibTableColumn
cfprFirmwareComputeMgmtPackMode = _CfprFirmwareComputeMgmtPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1, 7),
    _CfprFirmwareComputeMgmtPackMode_Type()
)
cfprFirmwareComputeMgmtPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackMode.setStatus("current")
_CfprFirmwareComputeMgmtPackName_Type = SnmpAdminString
_CfprFirmwareComputeMgmtPackName_Object = MibTableColumn
cfprFirmwareComputeMgmtPackName = _CfprFirmwareComputeMgmtPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1, 8),
    _CfprFirmwareComputeMgmtPackName_Type()
)
cfprFirmwareComputeMgmtPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackName.setStatus("current")
_CfprFirmwareComputeMgmtPackPolicyLevel_Type = Gauge32
_CfprFirmwareComputeMgmtPackPolicyLevel_Object = MibTableColumn
cfprFirmwareComputeMgmtPackPolicyLevel = _CfprFirmwareComputeMgmtPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1, 9),
    _CfprFirmwareComputeMgmtPackPolicyLevel_Type()
)
cfprFirmwareComputeMgmtPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackPolicyLevel.setStatus("current")
_CfprFirmwareComputeMgmtPackPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwareComputeMgmtPackPolicyOwner_Object = MibTableColumn
cfprFirmwareComputeMgmtPackPolicyOwner = _CfprFirmwareComputeMgmtPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1, 10),
    _CfprFirmwareComputeMgmtPackPolicyOwner_Type()
)
cfprFirmwareComputeMgmtPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackPolicyOwner.setStatus("current")
_CfprFirmwareComputeMgmtPackStageSize_Type = Gauge32
_CfprFirmwareComputeMgmtPackStageSize_Object = MibTableColumn
cfprFirmwareComputeMgmtPackStageSize = _CfprFirmwareComputeMgmtPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1, 11),
    _CfprFirmwareComputeMgmtPackStageSize_Type()
)
cfprFirmwareComputeMgmtPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackStageSize.setStatus("current")
_CfprFirmwareComputeMgmtPackUpdateTrigger_Type = DateAndTime
_CfprFirmwareComputeMgmtPackUpdateTrigger_Object = MibTableColumn
cfprFirmwareComputeMgmtPackUpdateTrigger = _CfprFirmwareComputeMgmtPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 15, 1, 12),
    _CfprFirmwareComputeMgmtPackUpdateTrigger_Type()
)
cfprFirmwareComputeMgmtPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareComputeMgmtPackUpdateTrigger.setStatus("current")
_CfprFirmwareConstraintTable_Object = MibTable
cfprFirmwareConstraintTable = _CfprFirmwareConstraintTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 16)
)
if mibBuilder.loadTexts:
    cfprFirmwareConstraintTable.setStatus("current")
_CfprFirmwareConstraintEntry_Object = MibTableRow
cfprFirmwareConstraintEntry = _CfprFirmwareConstraintEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 16, 1)
)
cfprFirmwareConstraintEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareConstraintInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareConstraintEntry.setStatus("current")
_CfprFirmwareConstraintInstanceId_Type = CfprManagedObjectId
_CfprFirmwareConstraintInstanceId_Object = MibTableColumn
cfprFirmwareConstraintInstanceId = _CfprFirmwareConstraintInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 16, 1, 1),
    _CfprFirmwareConstraintInstanceId_Type()
)
cfprFirmwareConstraintInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareConstraintInstanceId.setStatus("current")
_CfprFirmwareConstraintDn_Type = CfprManagedObjectDn
_CfprFirmwareConstraintDn_Object = MibTableColumn
cfprFirmwareConstraintDn = _CfprFirmwareConstraintDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 16, 1, 2),
    _CfprFirmwareConstraintDn_Type()
)
cfprFirmwareConstraintDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareConstraintDn.setStatus("current")
_CfprFirmwareConstraintRn_Type = SnmpAdminString
_CfprFirmwareConstraintRn_Object = MibTableColumn
cfprFirmwareConstraintRn = _CfprFirmwareConstraintRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 16, 1, 3),
    _CfprFirmwareConstraintRn_Type()
)
cfprFirmwareConstraintRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareConstraintRn.setStatus("current")
_CfprFirmwareConstraintFeature_Type = SnmpAdminString
_CfprFirmwareConstraintFeature_Object = MibTableColumn
cfprFirmwareConstraintFeature = _CfprFirmwareConstraintFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 16, 1, 4),
    _CfprFirmwareConstraintFeature_Type()
)
cfprFirmwareConstraintFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareConstraintFeature.setStatus("current")
_CfprFirmwareConstraintMinBiosVersion_Type = SnmpAdminString
_CfprFirmwareConstraintMinBiosVersion_Object = MibTableColumn
cfprFirmwareConstraintMinBiosVersion = _CfprFirmwareConstraintMinBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 16, 1, 5),
    _CfprFirmwareConstraintMinBiosVersion_Type()
)
cfprFirmwareConstraintMinBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareConstraintMinBiosVersion.setStatus("current")
_CfprFirmwareConstraintMinCimcVersion_Type = SnmpAdminString
_CfprFirmwareConstraintMinCimcVersion_Object = MibTableColumn
cfprFirmwareConstraintMinCimcVersion = _CfprFirmwareConstraintMinCimcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 16, 1, 6),
    _CfprFirmwareConstraintMinCimcVersion_Type()
)
cfprFirmwareConstraintMinCimcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareConstraintMinCimcVersion.setStatus("current")
_CfprFirmwareConstraintsTable_Object = MibTable
cfprFirmwareConstraintsTable = _CfprFirmwareConstraintsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 17)
)
if mibBuilder.loadTexts:
    cfprFirmwareConstraintsTable.setStatus("current")
_CfprFirmwareConstraintsEntry_Object = MibTableRow
cfprFirmwareConstraintsEntry = _CfprFirmwareConstraintsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 17, 1)
)
cfprFirmwareConstraintsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareConstraintsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareConstraintsEntry.setStatus("current")
_CfprFirmwareConstraintsInstanceId_Type = CfprManagedObjectId
_CfprFirmwareConstraintsInstanceId_Object = MibTableColumn
cfprFirmwareConstraintsInstanceId = _CfprFirmwareConstraintsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 17, 1, 1),
    _CfprFirmwareConstraintsInstanceId_Type()
)
cfprFirmwareConstraintsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareConstraintsInstanceId.setStatus("current")
_CfprFirmwareConstraintsDn_Type = CfprManagedObjectDn
_CfprFirmwareConstraintsDn_Object = MibTableColumn
cfprFirmwareConstraintsDn = _CfprFirmwareConstraintsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 17, 1, 2),
    _CfprFirmwareConstraintsDn_Type()
)
cfprFirmwareConstraintsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareConstraintsDn.setStatus("current")
_CfprFirmwareConstraintsRn_Type = SnmpAdminString
_CfprFirmwareConstraintsRn_Object = MibTableColumn
cfprFirmwareConstraintsRn = _CfprFirmwareConstraintsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 17, 1, 3),
    _CfprFirmwareConstraintsRn_Type()
)
cfprFirmwareConstraintsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareConstraintsRn.setStatus("current")
_CfprFirmwareDependencyTable_Object = MibTable
cfprFirmwareDependencyTable = _CfprFirmwareDependencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18)
)
if mibBuilder.loadTexts:
    cfprFirmwareDependencyTable.setStatus("current")
_CfprFirmwareDependencyEntry_Object = MibTableRow
cfprFirmwareDependencyEntry = _CfprFirmwareDependencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1)
)
cfprFirmwareDependencyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareDependencyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareDependencyEntry.setStatus("current")
_CfprFirmwareDependencyInstanceId_Type = CfprManagedObjectId
_CfprFirmwareDependencyInstanceId_Object = MibTableColumn
cfprFirmwareDependencyInstanceId = _CfprFirmwareDependencyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 1),
    _CfprFirmwareDependencyInstanceId_Type()
)
cfprFirmwareDependencyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyInstanceId.setStatus("current")
_CfprFirmwareDependencyDn_Type = CfprManagedObjectDn
_CfprFirmwareDependencyDn_Object = MibTableColumn
cfprFirmwareDependencyDn = _CfprFirmwareDependencyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 2),
    _CfprFirmwareDependencyDn_Type()
)
cfprFirmwareDependencyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyDn.setStatus("current")
_CfprFirmwareDependencyRn_Type = SnmpAdminString
_CfprFirmwareDependencyRn_Object = MibTableColumn
cfprFirmwareDependencyRn = _CfprFirmwareDependencyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 3),
    _CfprFirmwareDependencyRn_Type()
)
cfprFirmwareDependencyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyRn.setStatus("current")
_CfprFirmwareDependencyEp_Type = CfprFirmwareType
_CfprFirmwareDependencyEp_Object = MibTableColumn
cfprFirmwareDependencyEp = _CfprFirmwareDependencyEp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 4),
    _CfprFirmwareDependencyEp_Type()
)
cfprFirmwareDependencyEp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyEp.setStatus("current")
_CfprFirmwareDependencyHwModel_Type = SnmpAdminString
_CfprFirmwareDependencyHwModel_Object = MibTableColumn
cfprFirmwareDependencyHwModel = _CfprFirmwareDependencyHwModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 5),
    _CfprFirmwareDependencyHwModel_Type()
)
cfprFirmwareDependencyHwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyHwModel.setStatus("current")
_CfprFirmwareDependencyHwRevision_Type = SnmpAdminString
_CfprFirmwareDependencyHwRevision_Object = MibTableColumn
cfprFirmwareDependencyHwRevision = _CfprFirmwareDependencyHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 6),
    _CfprFirmwareDependencyHwRevision_Type()
)
cfprFirmwareDependencyHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyHwRevision.setStatus("current")
_CfprFirmwareDependencyHwVendor_Type = SnmpAdminString
_CfprFirmwareDependencyHwVendor_Object = MibTableColumn
cfprFirmwareDependencyHwVendor = _CfprFirmwareDependencyHwVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 7),
    _CfprFirmwareDependencyHwVendor_Type()
)
cfprFirmwareDependencyHwVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyHwVendor.setStatus("current")
_CfprFirmwareDependencyInvTag_Type = SnmpAdminString
_CfprFirmwareDependencyInvTag_Object = MibTableColumn
cfprFirmwareDependencyInvTag = _CfprFirmwareDependencyInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 8),
    _CfprFirmwareDependencyInvTag_Type()
)
cfprFirmwareDependencyInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyInvTag.setStatus("current")
_CfprFirmwareDependencyMaxVer_Type = SnmpAdminString
_CfprFirmwareDependencyMaxVer_Object = MibTableColumn
cfprFirmwareDependencyMaxVer = _CfprFirmwareDependencyMaxVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 9),
    _CfprFirmwareDependencyMaxVer_Type()
)
cfprFirmwareDependencyMaxVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyMaxVer.setStatus("current")
_CfprFirmwareDependencyMinVer_Type = SnmpAdminString
_CfprFirmwareDependencyMinVer_Object = MibTableColumn
cfprFirmwareDependencyMinVer = _CfprFirmwareDependencyMinVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 10),
    _CfprFirmwareDependencyMinVer_Type()
)
cfprFirmwareDependencyMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyMinVer.setStatus("current")
_CfprFirmwareDependencyRelationship_Type = CfprFirmwareDependencyRelationship
_CfprFirmwareDependencyRelationship_Object = MibTableColumn
cfprFirmwareDependencyRelationship = _CfprFirmwareDependencyRelationship_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 11),
    _CfprFirmwareDependencyRelationship_Type()
)
cfprFirmwareDependencyRelationship.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyRelationship.setStatus("current")
_CfprFirmwareDependencyScope_Type = CfprFirmwareDependencyScope
_CfprFirmwareDependencyScope_Object = MibTableColumn
cfprFirmwareDependencyScope = _CfprFirmwareDependencyScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 12),
    _CfprFirmwareDependencyScope_Type()
)
cfprFirmwareDependencyScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyScope.setStatus("current")
_CfprFirmwareDependencySensitivity_Type = CfprFirmwareDependencySensitivity
_CfprFirmwareDependencySensitivity_Object = MibTableColumn
cfprFirmwareDependencySensitivity = _CfprFirmwareDependencySensitivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 13),
    _CfprFirmwareDependencySensitivity_Type()
)
cfprFirmwareDependencySensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencySensitivity.setStatus("current")
_CfprFirmwareDependencyValidationStatus_Type = CfprFirmwareVerifyPackStatus
_CfprFirmwareDependencyValidationStatus_Object = MibTableColumn
cfprFirmwareDependencyValidationStatus = _CfprFirmwareDependencyValidationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 18, 1, 14),
    _CfprFirmwareDependencyValidationStatus_Type()
)
cfprFirmwareDependencyValidationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDependencyValidationStatus.setStatus("current")
_CfprFirmwareDistImageTable_Object = MibTable
cfprFirmwareDistImageTable = _CfprFirmwareDistImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 19)
)
if mibBuilder.loadTexts:
    cfprFirmwareDistImageTable.setStatus("current")
_CfprFirmwareDistImageEntry_Object = MibTableRow
cfprFirmwareDistImageEntry = _CfprFirmwareDistImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 19, 1)
)
cfprFirmwareDistImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareDistImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareDistImageEntry.setStatus("current")
_CfprFirmwareDistImageInstanceId_Type = CfprManagedObjectId
_CfprFirmwareDistImageInstanceId_Object = MibTableColumn
cfprFirmwareDistImageInstanceId = _CfprFirmwareDistImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 19, 1, 1),
    _CfprFirmwareDistImageInstanceId_Type()
)
cfprFirmwareDistImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareDistImageInstanceId.setStatus("current")
_CfprFirmwareDistImageDn_Type = CfprManagedObjectDn
_CfprFirmwareDistImageDn_Object = MibTableColumn
cfprFirmwareDistImageDn = _CfprFirmwareDistImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 19, 1, 2),
    _CfprFirmwareDistImageDn_Type()
)
cfprFirmwareDistImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistImageDn.setStatus("current")
_CfprFirmwareDistImageRn_Type = SnmpAdminString
_CfprFirmwareDistImageRn_Object = MibTableColumn
cfprFirmwareDistImageRn = _CfprFirmwareDistImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 19, 1, 3),
    _CfprFirmwareDistImageRn_Type()
)
cfprFirmwareDistImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistImageRn.setStatus("current")
_CfprFirmwareDistImageImageDeleted_Type = CfprFirmwareImageDeleted
_CfprFirmwareDistImageImageDeleted_Object = MibTableColumn
cfprFirmwareDistImageImageDeleted = _CfprFirmwareDistImageImageDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 19, 1, 4),
    _CfprFirmwareDistImageImageDeleted_Type()
)
cfprFirmwareDistImageImageDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistImageImageDeleted.setStatus("current")
_CfprFirmwareDistImageName_Type = SnmpAdminString
_CfprFirmwareDistImageName_Object = MibTableColumn
cfprFirmwareDistImageName = _CfprFirmwareDistImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 19, 1, 5),
    _CfprFirmwareDistImageName_Type()
)
cfprFirmwareDistImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistImageName.setStatus("current")
_CfprFirmwareDistImageType_Type = CfprFirmwareType
_CfprFirmwareDistImageType_Object = MibTableColumn
cfprFirmwareDistImageType = _CfprFirmwareDistImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 19, 1, 6),
    _CfprFirmwareDistImageType_Type()
)
cfprFirmwareDistImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistImageType.setStatus("current")
_CfprFirmwareDistributableTable_Object = MibTable
cfprFirmwareDistributableTable = _CfprFirmwareDistributableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20)
)
if mibBuilder.loadTexts:
    cfprFirmwareDistributableTable.setStatus("current")
_CfprFirmwareDistributableEntry_Object = MibTableRow
cfprFirmwareDistributableEntry = _CfprFirmwareDistributableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1)
)
cfprFirmwareDistributableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareDistributableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareDistributableEntry.setStatus("current")
_CfprFirmwareDistributableInstanceId_Type = CfprManagedObjectId
_CfprFirmwareDistributableInstanceId_Object = MibTableColumn
cfprFirmwareDistributableInstanceId = _CfprFirmwareDistributableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 1),
    _CfprFirmwareDistributableInstanceId_Type()
)
cfprFirmwareDistributableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableInstanceId.setStatus("current")
_CfprFirmwareDistributableDn_Type = CfprManagedObjectDn
_CfprFirmwareDistributableDn_Object = MibTableColumn
cfprFirmwareDistributableDn = _CfprFirmwareDistributableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 2),
    _CfprFirmwareDistributableDn_Type()
)
cfprFirmwareDistributableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableDn.setStatus("current")
_CfprFirmwareDistributableRn_Type = SnmpAdminString
_CfprFirmwareDistributableRn_Object = MibTableColumn
cfprFirmwareDistributableRn = _CfprFirmwareDistributableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 3),
    _CfprFirmwareDistributableRn_Type()
)
cfprFirmwareDistributableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableRn.setStatus("current")
_CfprFirmwareDistributableAdminState_Type = CfprFirmwareAdminState
_CfprFirmwareDistributableAdminState_Object = MibTableColumn
cfprFirmwareDistributableAdminState = _CfprFirmwareDistributableAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 4),
    _CfprFirmwareDistributableAdminState_Type()
)
cfprFirmwareDistributableAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableAdminState.setStatus("current")
_CfprFirmwareDistributableCompleteness_Type = CfprFirmwareCompleteness
_CfprFirmwareDistributableCompleteness_Object = MibTableColumn
cfprFirmwareDistributableCompleteness = _CfprFirmwareDistributableCompleteness_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 5),
    _CfprFirmwareDistributableCompleteness_Type()
)
cfprFirmwareDistributableCompleteness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableCompleteness.setStatus("current")
_CfprFirmwareDistributableDescr_Type = SnmpAdminString
_CfprFirmwareDistributableDescr_Object = MibTableColumn
cfprFirmwareDistributableDescr = _CfprFirmwareDistributableDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 6),
    _CfprFirmwareDistributableDescr_Type()
)
cfprFirmwareDistributableDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableDescr.setStatus("current")
_CfprFirmwareDistributableFsmDescr_Type = SnmpAdminString
_CfprFirmwareDistributableFsmDescr_Object = MibTableColumn
cfprFirmwareDistributableFsmDescr = _CfprFirmwareDistributableFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 7),
    _CfprFirmwareDistributableFsmDescr_Type()
)
cfprFirmwareDistributableFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmDescr.setStatus("current")
_CfprFirmwareDistributableFsmPrev_Type = SnmpAdminString
_CfprFirmwareDistributableFsmPrev_Object = MibTableColumn
cfprFirmwareDistributableFsmPrev = _CfprFirmwareDistributableFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 8),
    _CfprFirmwareDistributableFsmPrev_Type()
)
cfprFirmwareDistributableFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmPrev.setStatus("current")
_CfprFirmwareDistributableFsmProgr_Type = Gauge32
_CfprFirmwareDistributableFsmProgr_Object = MibTableColumn
cfprFirmwareDistributableFsmProgr = _CfprFirmwareDistributableFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 9),
    _CfprFirmwareDistributableFsmProgr_Type()
)
cfprFirmwareDistributableFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmProgr.setStatus("current")
_CfprFirmwareDistributableFsmRmtInvErrCode_Type = Gauge32
_CfprFirmwareDistributableFsmRmtInvErrCode_Object = MibTableColumn
cfprFirmwareDistributableFsmRmtInvErrCode = _CfprFirmwareDistributableFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 10),
    _CfprFirmwareDistributableFsmRmtInvErrCode_Type()
)
cfprFirmwareDistributableFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmRmtInvErrCode.setStatus("current")
_CfprFirmwareDistributableFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprFirmwareDistributableFsmRmtInvErrDescr_Object = MibTableColumn
cfprFirmwareDistributableFsmRmtInvErrDescr = _CfprFirmwareDistributableFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 11),
    _CfprFirmwareDistributableFsmRmtInvErrDescr_Type()
)
cfprFirmwareDistributableFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmRmtInvErrDescr.setStatus("current")
_CfprFirmwareDistributableFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwareDistributableFsmRmtInvRslt_Object = MibTableColumn
cfprFirmwareDistributableFsmRmtInvRslt = _CfprFirmwareDistributableFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 12),
    _CfprFirmwareDistributableFsmRmtInvRslt_Type()
)
cfprFirmwareDistributableFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmRmtInvRslt.setStatus("current")
_CfprFirmwareDistributableFsmStageDescr_Type = SnmpAdminString
_CfprFirmwareDistributableFsmStageDescr_Object = MibTableColumn
cfprFirmwareDistributableFsmStageDescr = _CfprFirmwareDistributableFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 13),
    _CfprFirmwareDistributableFsmStageDescr_Type()
)
cfprFirmwareDistributableFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStageDescr.setStatus("current")
_CfprFirmwareDistributableFsmStamp_Type = DateAndTime
_CfprFirmwareDistributableFsmStamp_Object = MibTableColumn
cfprFirmwareDistributableFsmStamp = _CfprFirmwareDistributableFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 14),
    _CfprFirmwareDistributableFsmStamp_Type()
)
cfprFirmwareDistributableFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStamp.setStatus("current")
_CfprFirmwareDistributableFsmStatus_Type = SnmpAdminString
_CfprFirmwareDistributableFsmStatus_Object = MibTableColumn
cfprFirmwareDistributableFsmStatus = _CfprFirmwareDistributableFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 15),
    _CfprFirmwareDistributableFsmStatus_Type()
)
cfprFirmwareDistributableFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStatus.setStatus("current")
_CfprFirmwareDistributableFsmTry_Type = Gauge32
_CfprFirmwareDistributableFsmTry_Object = MibTableColumn
cfprFirmwareDistributableFsmTry = _CfprFirmwareDistributableFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 16),
    _CfprFirmwareDistributableFsmTry_Type()
)
cfprFirmwareDistributableFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmTry.setStatus("current")
_CfprFirmwareDistributableImagePresence_Type = CfprFirmwareImagePresence
_CfprFirmwareDistributableImagePresence_Object = MibTableColumn
cfprFirmwareDistributableImagePresence = _CfprFirmwareDistributableImagePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 17),
    _CfprFirmwareDistributableImagePresence_Type()
)
cfprFirmwareDistributableImagePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableImagePresence.setStatus("current")
_CfprFirmwareDistributableIntId_Type = SnmpAdminString
_CfprFirmwareDistributableIntId_Object = MibTableColumn
cfprFirmwareDistributableIntId = _CfprFirmwareDistributableIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 18),
    _CfprFirmwareDistributableIntId_Type()
)
cfprFirmwareDistributableIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableIntId.setStatus("current")
_CfprFirmwareDistributableInvTag_Type = SnmpAdminString
_CfprFirmwareDistributableInvTag_Object = MibTableColumn
cfprFirmwareDistributableInvTag = _CfprFirmwareDistributableInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 19),
    _CfprFirmwareDistributableInvTag_Type()
)
cfprFirmwareDistributableInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableInvTag.setStatus("current")
_CfprFirmwareDistributableModel_Type = SnmpAdminString
_CfprFirmwareDistributableModel_Object = MibTableColumn
cfprFirmwareDistributableModel = _CfprFirmwareDistributableModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 20),
    _CfprFirmwareDistributableModel_Type()
)
cfprFirmwareDistributableModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableModel.setStatus("current")
_CfprFirmwareDistributableName_Type = SnmpAdminString
_CfprFirmwareDistributableName_Object = MibTableColumn
cfprFirmwareDistributableName = _CfprFirmwareDistributableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 21),
    _CfprFirmwareDistributableName_Type()
)
cfprFirmwareDistributableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableName.setStatus("current")
_CfprFirmwareDistributablePolicyLevel_Type = Gauge32
_CfprFirmwareDistributablePolicyLevel_Object = MibTableColumn
cfprFirmwareDistributablePolicyLevel = _CfprFirmwareDistributablePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 22),
    _CfprFirmwareDistributablePolicyLevel_Type()
)
cfprFirmwareDistributablePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributablePolicyLevel.setStatus("current")
_CfprFirmwareDistributablePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwareDistributablePolicyOwner_Object = MibTableColumn
cfprFirmwareDistributablePolicyOwner = _CfprFirmwareDistributablePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 23),
    _CfprFirmwareDistributablePolicyOwner_Type()
)
cfprFirmwareDistributablePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributablePolicyOwner.setStatus("current")
_CfprFirmwareDistributableTransferState_Type = CfprFirmwareTransferState
_CfprFirmwareDistributableTransferState_Object = MibTableColumn
cfprFirmwareDistributableTransferState = _CfprFirmwareDistributableTransferState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 24),
    _CfprFirmwareDistributableTransferState_Type()
)
cfprFirmwareDistributableTransferState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableTransferState.setStatus("current")
_CfprFirmwareDistributableType_Type = CfprFirmwareDistributableType
_CfprFirmwareDistributableType_Object = MibTableColumn
cfprFirmwareDistributableType = _CfprFirmwareDistributableType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 25),
    _CfprFirmwareDistributableType_Type()
)
cfprFirmwareDistributableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableType.setStatus("current")
_CfprFirmwareDistributableVendor_Type = SnmpAdminString
_CfprFirmwareDistributableVendor_Object = MibTableColumn
cfprFirmwareDistributableVendor = _CfprFirmwareDistributableVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 26),
    _CfprFirmwareDistributableVendor_Type()
)
cfprFirmwareDistributableVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableVendor.setStatus("current")
_CfprFirmwareDistributableVersion_Type = SnmpAdminString
_CfprFirmwareDistributableVersion_Object = MibTableColumn
cfprFirmwareDistributableVersion = _CfprFirmwareDistributableVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 27),
    _CfprFirmwareDistributableVersion_Type()
)
cfprFirmwareDistributableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableVersion.setStatus("current")
_CfprFirmwareDistributableBuildDate_Type = SnmpAdminString
_CfprFirmwareDistributableBuildDate_Object = MibTableColumn
cfprFirmwareDistributableBuildDate = _CfprFirmwareDistributableBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 28),
    _CfprFirmwareDistributableBuildDate_Type()
)
cfprFirmwareDistributableBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableBuildDate.setStatus("current")
_CfprFirmwareDistributableDisplayFlag_Type = TruthValue
_CfprFirmwareDistributableDisplayFlag_Object = MibTableColumn
cfprFirmwareDistributableDisplayFlag = _CfprFirmwareDistributableDisplayFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 29),
    _CfprFirmwareDistributableDisplayFlag_Type()
)
cfprFirmwareDistributableDisplayFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableDisplayFlag.setStatus("current")
_CfprFirmwareDistributableSupportsMultiInstance_Type = TruthValue
_CfprFirmwareDistributableSupportsMultiInstance_Object = MibTableColumn
cfprFirmwareDistributableSupportsMultiInstance = _CfprFirmwareDistributableSupportsMultiInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 30),
    _CfprFirmwareDistributableSupportsMultiInstance_Type()
)
cfprFirmwareDistributableSupportsMultiInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableSupportsMultiInstance.setStatus("current")
_CfprFirmwareDistributableTimeStamp_Type = DateAndTime
_CfprFirmwareDistributableTimeStamp_Object = MibTableColumn
cfprFirmwareDistributableTimeStamp = _CfprFirmwareDistributableTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 20, 1, 31),
    _CfprFirmwareDistributableTimeStamp_Type()
)
cfprFirmwareDistributableTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableTimeStamp.setStatus("current")
_CfprFirmwareDistributableFsmTable_Object = MibTable
cfprFirmwareDistributableFsmTable = _CfprFirmwareDistributableFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21)
)
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmTable.setStatus("current")
_CfprFirmwareDistributableFsmEntry_Object = MibTableRow
cfprFirmwareDistributableFsmEntry = _CfprFirmwareDistributableFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21, 1)
)
cfprFirmwareDistributableFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareDistributableFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmEntry.setStatus("current")
_CfprFirmwareDistributableFsmInstanceId_Type = CfprManagedObjectId
_CfprFirmwareDistributableFsmInstanceId_Object = MibTableColumn
cfprFirmwareDistributableFsmInstanceId = _CfprFirmwareDistributableFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21, 1, 1),
    _CfprFirmwareDistributableFsmInstanceId_Type()
)
cfprFirmwareDistributableFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmInstanceId.setStatus("current")
_CfprFirmwareDistributableFsmDn_Type = CfprManagedObjectDn
_CfprFirmwareDistributableFsmDn_Object = MibTableColumn
cfprFirmwareDistributableFsmDn = _CfprFirmwareDistributableFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21, 1, 2),
    _CfprFirmwareDistributableFsmDn_Type()
)
cfprFirmwareDistributableFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmDn.setStatus("current")
_CfprFirmwareDistributableFsmRn_Type = SnmpAdminString
_CfprFirmwareDistributableFsmRn_Object = MibTableColumn
cfprFirmwareDistributableFsmRn = _CfprFirmwareDistributableFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21, 1, 3),
    _CfprFirmwareDistributableFsmRn_Type()
)
cfprFirmwareDistributableFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmRn.setStatus("current")
_CfprFirmwareDistributableFsmCompletionTime_Type = DateAndTime
_CfprFirmwareDistributableFsmCompletionTime_Object = MibTableColumn
cfprFirmwareDistributableFsmCompletionTime = _CfprFirmwareDistributableFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21, 1, 4),
    _CfprFirmwareDistributableFsmCompletionTime_Type()
)
cfprFirmwareDistributableFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmCompletionTime.setStatus("current")
_CfprFirmwareDistributableFsmCurrentFsm_Type = CfprFirmwareDistributableFsmCurrentFsm
_CfprFirmwareDistributableFsmCurrentFsm_Object = MibTableColumn
cfprFirmwareDistributableFsmCurrentFsm = _CfprFirmwareDistributableFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21, 1, 5),
    _CfprFirmwareDistributableFsmCurrentFsm_Type()
)
cfprFirmwareDistributableFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmCurrentFsm.setStatus("current")
_CfprFirmwareDistributableFsmDescrData_Type = SnmpAdminString
_CfprFirmwareDistributableFsmDescrData_Object = MibTableColumn
cfprFirmwareDistributableFsmDescrData = _CfprFirmwareDistributableFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21, 1, 6),
    _CfprFirmwareDistributableFsmDescrData_Type()
)
cfprFirmwareDistributableFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmDescrData.setStatus("current")
_CfprFirmwareDistributableFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwareDistributableFsmFsmStatus_Object = MibTableColumn
cfprFirmwareDistributableFsmFsmStatus = _CfprFirmwareDistributableFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21, 1, 7),
    _CfprFirmwareDistributableFsmFsmStatus_Type()
)
cfprFirmwareDistributableFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmFsmStatus.setStatus("current")
_CfprFirmwareDistributableFsmProgress_Type = Gauge32
_CfprFirmwareDistributableFsmProgress_Object = MibTableColumn
cfprFirmwareDistributableFsmProgress = _CfprFirmwareDistributableFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21, 1, 8),
    _CfprFirmwareDistributableFsmProgress_Type()
)
cfprFirmwareDistributableFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmProgress.setStatus("current")
_CfprFirmwareDistributableFsmRmtErrCode_Type = Gauge32
_CfprFirmwareDistributableFsmRmtErrCode_Object = MibTableColumn
cfprFirmwareDistributableFsmRmtErrCode = _CfprFirmwareDistributableFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21, 1, 9),
    _CfprFirmwareDistributableFsmRmtErrCode_Type()
)
cfprFirmwareDistributableFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmRmtErrCode.setStatus("current")
_CfprFirmwareDistributableFsmRmtErrDescr_Type = SnmpAdminString
_CfprFirmwareDistributableFsmRmtErrDescr_Object = MibTableColumn
cfprFirmwareDistributableFsmRmtErrDescr = _CfprFirmwareDistributableFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21, 1, 10),
    _CfprFirmwareDistributableFsmRmtErrDescr_Type()
)
cfprFirmwareDistributableFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmRmtErrDescr.setStatus("current")
_CfprFirmwareDistributableFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwareDistributableFsmRmtRslt_Object = MibTableColumn
cfprFirmwareDistributableFsmRmtRslt = _CfprFirmwareDistributableFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 21, 1, 11),
    _CfprFirmwareDistributableFsmRmtRslt_Type()
)
cfprFirmwareDistributableFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmRmtRslt.setStatus("current")
_CfprFirmwareDistributableFsmStageTable_Object = MibTable
cfprFirmwareDistributableFsmStageTable = _CfprFirmwareDistributableFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 22)
)
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStageTable.setStatus("current")
_CfprFirmwareDistributableFsmStageEntry_Object = MibTableRow
cfprFirmwareDistributableFsmStageEntry = _CfprFirmwareDistributableFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 22, 1)
)
cfprFirmwareDistributableFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareDistributableFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStageEntry.setStatus("current")
_CfprFirmwareDistributableFsmStageInstanceId_Type = CfprManagedObjectId
_CfprFirmwareDistributableFsmStageInstanceId_Object = MibTableColumn
cfprFirmwareDistributableFsmStageInstanceId = _CfprFirmwareDistributableFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 22, 1, 1),
    _CfprFirmwareDistributableFsmStageInstanceId_Type()
)
cfprFirmwareDistributableFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStageInstanceId.setStatus("current")
_CfprFirmwareDistributableFsmStageDn_Type = CfprManagedObjectDn
_CfprFirmwareDistributableFsmStageDn_Object = MibTableColumn
cfprFirmwareDistributableFsmStageDn = _CfprFirmwareDistributableFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 22, 1, 2),
    _CfprFirmwareDistributableFsmStageDn_Type()
)
cfprFirmwareDistributableFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStageDn.setStatus("current")
_CfprFirmwareDistributableFsmStageRn_Type = SnmpAdminString
_CfprFirmwareDistributableFsmStageRn_Object = MibTableColumn
cfprFirmwareDistributableFsmStageRn = _CfprFirmwareDistributableFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 22, 1, 3),
    _CfprFirmwareDistributableFsmStageRn_Type()
)
cfprFirmwareDistributableFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStageRn.setStatus("current")
_CfprFirmwareDistributableFsmStageDescrData_Type = SnmpAdminString
_CfprFirmwareDistributableFsmStageDescrData_Object = MibTableColumn
cfprFirmwareDistributableFsmStageDescrData = _CfprFirmwareDistributableFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 22, 1, 4),
    _CfprFirmwareDistributableFsmStageDescrData_Type()
)
cfprFirmwareDistributableFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStageDescrData.setStatus("current")
_CfprFirmwareDistributableFsmStageLastUpdateTime_Type = DateAndTime
_CfprFirmwareDistributableFsmStageLastUpdateTime_Object = MibTableColumn
cfprFirmwareDistributableFsmStageLastUpdateTime = _CfprFirmwareDistributableFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 22, 1, 5),
    _CfprFirmwareDistributableFsmStageLastUpdateTime_Type()
)
cfprFirmwareDistributableFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStageLastUpdateTime.setStatus("current")
_CfprFirmwareDistributableFsmStageName_Type = CfprFirmwareDistributableFsmStageName
_CfprFirmwareDistributableFsmStageName_Object = MibTableColumn
cfprFirmwareDistributableFsmStageName = _CfprFirmwareDistributableFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 22, 1, 6),
    _CfprFirmwareDistributableFsmStageName_Type()
)
cfprFirmwareDistributableFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStageName.setStatus("current")
_CfprFirmwareDistributableFsmStageOrder_Type = Gauge32
_CfprFirmwareDistributableFsmStageOrder_Object = MibTableColumn
cfprFirmwareDistributableFsmStageOrder = _CfprFirmwareDistributableFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 22, 1, 7),
    _CfprFirmwareDistributableFsmStageOrder_Type()
)
cfprFirmwareDistributableFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStageOrder.setStatus("current")
_CfprFirmwareDistributableFsmStageRetry_Type = Gauge32
_CfprFirmwareDistributableFsmStageRetry_Object = MibTableColumn
cfprFirmwareDistributableFsmStageRetry = _CfprFirmwareDistributableFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 22, 1, 8),
    _CfprFirmwareDistributableFsmStageRetry_Type()
)
cfprFirmwareDistributableFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStageRetry.setStatus("current")
_CfprFirmwareDistributableFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwareDistributableFsmStageStageStatus_Object = MibTableColumn
cfprFirmwareDistributableFsmStageStageStatus = _CfprFirmwareDistributableFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 22, 1, 9),
    _CfprFirmwareDistributableFsmStageStageStatus_Type()
)
cfprFirmwareDistributableFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmStageStageStatus.setStatus("current")
_CfprFirmwareDistributableFsmTaskTable_Object = MibTable
cfprFirmwareDistributableFsmTaskTable = _CfprFirmwareDistributableFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 23)
)
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmTaskTable.setStatus("current")
_CfprFirmwareDistributableFsmTaskEntry_Object = MibTableRow
cfprFirmwareDistributableFsmTaskEntry = _CfprFirmwareDistributableFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 23, 1)
)
cfprFirmwareDistributableFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareDistributableFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmTaskEntry.setStatus("current")
_CfprFirmwareDistributableFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprFirmwareDistributableFsmTaskInstanceId_Object = MibTableColumn
cfprFirmwareDistributableFsmTaskInstanceId = _CfprFirmwareDistributableFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 23, 1, 1),
    _CfprFirmwareDistributableFsmTaskInstanceId_Type()
)
cfprFirmwareDistributableFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmTaskInstanceId.setStatus("current")
_CfprFirmwareDistributableFsmTaskDn_Type = CfprManagedObjectDn
_CfprFirmwareDistributableFsmTaskDn_Object = MibTableColumn
cfprFirmwareDistributableFsmTaskDn = _CfprFirmwareDistributableFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 23, 1, 2),
    _CfprFirmwareDistributableFsmTaskDn_Type()
)
cfprFirmwareDistributableFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmTaskDn.setStatus("current")
_CfprFirmwareDistributableFsmTaskRn_Type = SnmpAdminString
_CfprFirmwareDistributableFsmTaskRn_Object = MibTableColumn
cfprFirmwareDistributableFsmTaskRn = _CfprFirmwareDistributableFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 23, 1, 3),
    _CfprFirmwareDistributableFsmTaskRn_Type()
)
cfprFirmwareDistributableFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmTaskRn.setStatus("current")
_CfprFirmwareDistributableFsmTaskCompletion_Type = CfprFsmCompletion
_CfprFirmwareDistributableFsmTaskCompletion_Object = MibTableColumn
cfprFirmwareDistributableFsmTaskCompletion = _CfprFirmwareDistributableFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 23, 1, 4),
    _CfprFirmwareDistributableFsmTaskCompletion_Type()
)
cfprFirmwareDistributableFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmTaskCompletion.setStatus("current")
_CfprFirmwareDistributableFsmTaskFlags_Type = CfprFsmFlags
_CfprFirmwareDistributableFsmTaskFlags_Object = MibTableColumn
cfprFirmwareDistributableFsmTaskFlags = _CfprFirmwareDistributableFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 23, 1, 5),
    _CfprFirmwareDistributableFsmTaskFlags_Type()
)
cfprFirmwareDistributableFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmTaskFlags.setStatus("current")
_CfprFirmwareDistributableFsmTaskItem_Type = CfprFirmwareDistributableFsmTaskItem
_CfprFirmwareDistributableFsmTaskItem_Object = MibTableColumn
cfprFirmwareDistributableFsmTaskItem = _CfprFirmwareDistributableFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 23, 1, 6),
    _CfprFirmwareDistributableFsmTaskItem_Type()
)
cfprFirmwareDistributableFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmTaskItem.setStatus("current")
_CfprFirmwareDistributableFsmTaskSeqId_Type = Gauge32
_CfprFirmwareDistributableFsmTaskSeqId_Object = MibTableColumn
cfprFirmwareDistributableFsmTaskSeqId = _CfprFirmwareDistributableFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 23, 1, 7),
    _CfprFirmwareDistributableFsmTaskSeqId_Type()
)
cfprFirmwareDistributableFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistributableFsmTaskSeqId.setStatus("current")
_CfprFirmwareDownloaderTable_Object = MibTable
cfprFirmwareDownloaderTable = _CfprFirmwareDownloaderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24)
)
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderTable.setStatus("current")
_CfprFirmwareDownloaderEntry_Object = MibTableRow
cfprFirmwareDownloaderEntry = _CfprFirmwareDownloaderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1)
)
cfprFirmwareDownloaderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareDownloaderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderEntry.setStatus("current")
_CfprFirmwareDownloaderInstanceId_Type = CfprManagedObjectId
_CfprFirmwareDownloaderInstanceId_Object = MibTableColumn
cfprFirmwareDownloaderInstanceId = _CfprFirmwareDownloaderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 1),
    _CfprFirmwareDownloaderInstanceId_Type()
)
cfprFirmwareDownloaderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderInstanceId.setStatus("current")
_CfprFirmwareDownloaderDn_Type = CfprManagedObjectDn
_CfprFirmwareDownloaderDn_Object = MibTableColumn
cfprFirmwareDownloaderDn = _CfprFirmwareDownloaderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 2),
    _CfprFirmwareDownloaderDn_Type()
)
cfprFirmwareDownloaderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderDn.setStatus("current")
_CfprFirmwareDownloaderRn_Type = SnmpAdminString
_CfprFirmwareDownloaderRn_Object = MibTableColumn
cfprFirmwareDownloaderRn = _CfprFirmwareDownloaderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 3),
    _CfprFirmwareDownloaderRn_Type()
)
cfprFirmwareDownloaderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderRn.setStatus("current")
_CfprFirmwareDownloaderAdminState_Type = CfprFirmwareDownloadActivity
_CfprFirmwareDownloaderAdminState_Object = MibTableColumn
cfprFirmwareDownloaderAdminState = _CfprFirmwareDownloaderAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 4),
    _CfprFirmwareDownloaderAdminState_Type()
)
cfprFirmwareDownloaderAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderAdminState.setStatus("current")
_CfprFirmwareDownloaderFileName_Type = SnmpAdminString
_CfprFirmwareDownloaderFileName_Object = MibTableColumn
cfprFirmwareDownloaderFileName = _CfprFirmwareDownloaderFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 5),
    _CfprFirmwareDownloaderFileName_Type()
)
cfprFirmwareDownloaderFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFileName.setStatus("current")
_CfprFirmwareDownloaderFsmDescr_Type = SnmpAdminString
_CfprFirmwareDownloaderFsmDescr_Object = MibTableColumn
cfprFirmwareDownloaderFsmDescr = _CfprFirmwareDownloaderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 6),
    _CfprFirmwareDownloaderFsmDescr_Type()
)
cfprFirmwareDownloaderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmDescr.setStatus("current")
_CfprFirmwareDownloaderFsmPrev_Type = SnmpAdminString
_CfprFirmwareDownloaderFsmPrev_Object = MibTableColumn
cfprFirmwareDownloaderFsmPrev = _CfprFirmwareDownloaderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 7),
    _CfprFirmwareDownloaderFsmPrev_Type()
)
cfprFirmwareDownloaderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmPrev.setStatus("current")
_CfprFirmwareDownloaderFsmProgr_Type = Gauge32
_CfprFirmwareDownloaderFsmProgr_Object = MibTableColumn
cfprFirmwareDownloaderFsmProgr = _CfprFirmwareDownloaderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 8),
    _CfprFirmwareDownloaderFsmProgr_Type()
)
cfprFirmwareDownloaderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmProgr.setStatus("current")
_CfprFirmwareDownloaderFsmRmtInvErrCode_Type = Gauge32
_CfprFirmwareDownloaderFsmRmtInvErrCode_Object = MibTableColumn
cfprFirmwareDownloaderFsmRmtInvErrCode = _CfprFirmwareDownloaderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 9),
    _CfprFirmwareDownloaderFsmRmtInvErrCode_Type()
)
cfprFirmwareDownloaderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmRmtInvErrCode.setStatus("current")
_CfprFirmwareDownloaderFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprFirmwareDownloaderFsmRmtInvErrDescr_Object = MibTableColumn
cfprFirmwareDownloaderFsmRmtInvErrDescr = _CfprFirmwareDownloaderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 10),
    _CfprFirmwareDownloaderFsmRmtInvErrDescr_Type()
)
cfprFirmwareDownloaderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmRmtInvErrDescr.setStatus("current")
_CfprFirmwareDownloaderFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwareDownloaderFsmRmtInvRslt_Object = MibTableColumn
cfprFirmwareDownloaderFsmRmtInvRslt = _CfprFirmwareDownloaderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 11),
    _CfprFirmwareDownloaderFsmRmtInvRslt_Type()
)
cfprFirmwareDownloaderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmRmtInvRslt.setStatus("current")
_CfprFirmwareDownloaderFsmStageDescr_Type = SnmpAdminString
_CfprFirmwareDownloaderFsmStageDescr_Object = MibTableColumn
cfprFirmwareDownloaderFsmStageDescr = _CfprFirmwareDownloaderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 12),
    _CfprFirmwareDownloaderFsmStageDescr_Type()
)
cfprFirmwareDownloaderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStageDescr.setStatus("current")
_CfprFirmwareDownloaderFsmStamp_Type = DateAndTime
_CfprFirmwareDownloaderFsmStamp_Object = MibTableColumn
cfprFirmwareDownloaderFsmStamp = _CfprFirmwareDownloaderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 13),
    _CfprFirmwareDownloaderFsmStamp_Type()
)
cfprFirmwareDownloaderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStamp.setStatus("current")
_CfprFirmwareDownloaderFsmStatus_Type = SnmpAdminString
_CfprFirmwareDownloaderFsmStatus_Object = MibTableColumn
cfprFirmwareDownloaderFsmStatus = _CfprFirmwareDownloaderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 14),
    _CfprFirmwareDownloaderFsmStatus_Type()
)
cfprFirmwareDownloaderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStatus.setStatus("current")
_CfprFirmwareDownloaderFsmTry_Type = Gauge32
_CfprFirmwareDownloaderFsmTry_Object = MibTableColumn
cfprFirmwareDownloaderFsmTry = _CfprFirmwareDownloaderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 15),
    _CfprFirmwareDownloaderFsmTry_Type()
)
cfprFirmwareDownloaderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmTry.setStatus("current")
_CfprFirmwareDownloaderImageSize_Type = Unsigned64
_CfprFirmwareDownloaderImageSize_Object = MibTableColumn
cfprFirmwareDownloaderImageSize = _CfprFirmwareDownloaderImageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 16),
    _CfprFirmwareDownloaderImageSize_Type()
)
cfprFirmwareDownloaderImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderImageSize.setStatus("current")
_CfprFirmwareDownloaderProtocol_Type = CfprFirmwareTransport
_CfprFirmwareDownloaderProtocol_Object = MibTableColumn
cfprFirmwareDownloaderProtocol = _CfprFirmwareDownloaderProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 17),
    _CfprFirmwareDownloaderProtocol_Type()
)
cfprFirmwareDownloaderProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderProtocol.setStatus("current")
_CfprFirmwareDownloaderPwd_Type = SnmpAdminString
_CfprFirmwareDownloaderPwd_Object = MibTableColumn
cfprFirmwareDownloaderPwd = _CfprFirmwareDownloaderPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 18),
    _CfprFirmwareDownloaderPwd_Type()
)
cfprFirmwareDownloaderPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderPwd.setStatus("current")
_CfprFirmwareDownloaderRemotePath_Type = SnmpAdminString
_CfprFirmwareDownloaderRemotePath_Object = MibTableColumn
cfprFirmwareDownloaderRemotePath = _CfprFirmwareDownloaderRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 19),
    _CfprFirmwareDownloaderRemotePath_Type()
)
cfprFirmwareDownloaderRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderRemotePath.setStatus("current")
_CfprFirmwareDownloaderServer_Type = SnmpAdminString
_CfprFirmwareDownloaderServer_Object = MibTableColumn
cfprFirmwareDownloaderServer = _CfprFirmwareDownloaderServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 20),
    _CfprFirmwareDownloaderServer_Type()
)
cfprFirmwareDownloaderServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderServer.setStatus("current")
_CfprFirmwareDownloaderTransferState_Type = CfprFirmwareTransferState
_CfprFirmwareDownloaderTransferState_Object = MibTableColumn
cfprFirmwareDownloaderTransferState = _CfprFirmwareDownloaderTransferState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 21),
    _CfprFirmwareDownloaderTransferState_Type()
)
cfprFirmwareDownloaderTransferState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderTransferState.setStatus("current")
_CfprFirmwareDownloaderUser_Type = SnmpAdminString
_CfprFirmwareDownloaderUser_Object = MibTableColumn
cfprFirmwareDownloaderUser = _CfprFirmwareDownloaderUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 22),
    _CfprFirmwareDownloaderUser_Type()
)
cfprFirmwareDownloaderUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderUser.setStatus("current")
_CfprFirmwareDownloaderTimeStamp_Type = DateAndTime
_CfprFirmwareDownloaderTimeStamp_Object = MibTableColumn
cfprFirmwareDownloaderTimeStamp = _CfprFirmwareDownloaderTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 23),
    _CfprFirmwareDownloaderTimeStamp_Type()
)
cfprFirmwareDownloaderTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderTimeStamp.setStatus("current")
_CfprFirmwareDownloaderMsgStatus_Type = SnmpAdminString
_CfprFirmwareDownloaderMsgStatus_Object = MibTableColumn
cfprFirmwareDownloaderMsgStatus = _CfprFirmwareDownloaderMsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 24),
    _CfprFirmwareDownloaderMsgStatus_Type()
)
cfprFirmwareDownloaderMsgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderMsgStatus.setStatus("current")
_CfprFirmwareDownloaderPort_Type = Gauge32
_CfprFirmwareDownloaderPort_Object = MibTableColumn
cfprFirmwareDownloaderPort = _CfprFirmwareDownloaderPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 25),
    _CfprFirmwareDownloaderPort_Type()
)
cfprFirmwareDownloaderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderPort.setStatus("current")
_CfprFirmwareDownloaderStartTime_Type = DateAndTime
_CfprFirmwareDownloaderStartTime_Object = MibTableColumn
cfprFirmwareDownloaderStartTime = _CfprFirmwareDownloaderStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 26),
    _CfprFirmwareDownloaderStartTime_Type()
)
cfprFirmwareDownloaderStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderStartTime.setStatus("current")
_CfprFirmwareDownloaderTransferRate_Type = Integer32
_CfprFirmwareDownloaderTransferRate_Object = MibTableColumn
cfprFirmwareDownloaderTransferRate = _CfprFirmwareDownloaderTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 27),
    _CfprFirmwareDownloaderTransferRate_Type()
)
cfprFirmwareDownloaderTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderTransferRate.setStatus("current")
_CfprFirmwareDownloaderSilent_Type = Gauge32
_CfprFirmwareDownloaderSilent_Object = MibTableColumn
cfprFirmwareDownloaderSilent = _CfprFirmwareDownloaderSilent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 28),
    _CfprFirmwareDownloaderSilent_Type()
)
cfprFirmwareDownloaderSilent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderSilent.setStatus("current")
_CfprFirmwareDownloaderTtyName_Type = SnmpAdminString
_CfprFirmwareDownloaderTtyName_Object = MibTableColumn
cfprFirmwareDownloaderTtyName = _CfprFirmwareDownloaderTtyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 24, 1, 29),
    _CfprFirmwareDownloaderTtyName_Type()
)
cfprFirmwareDownloaderTtyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderTtyName.setStatus("current")
_CfprFirmwareDownloaderFsmTable_Object = MibTable
cfprFirmwareDownloaderFsmTable = _CfprFirmwareDownloaderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25)
)
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmTable.setStatus("current")
_CfprFirmwareDownloaderFsmEntry_Object = MibTableRow
cfprFirmwareDownloaderFsmEntry = _CfprFirmwareDownloaderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25, 1)
)
cfprFirmwareDownloaderFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareDownloaderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmEntry.setStatus("current")
_CfprFirmwareDownloaderFsmInstanceId_Type = CfprManagedObjectId
_CfprFirmwareDownloaderFsmInstanceId_Object = MibTableColumn
cfprFirmwareDownloaderFsmInstanceId = _CfprFirmwareDownloaderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25, 1, 1),
    _CfprFirmwareDownloaderFsmInstanceId_Type()
)
cfprFirmwareDownloaderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmInstanceId.setStatus("current")
_CfprFirmwareDownloaderFsmDn_Type = CfprManagedObjectDn
_CfprFirmwareDownloaderFsmDn_Object = MibTableColumn
cfprFirmwareDownloaderFsmDn = _CfprFirmwareDownloaderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25, 1, 2),
    _CfprFirmwareDownloaderFsmDn_Type()
)
cfprFirmwareDownloaderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmDn.setStatus("current")
_CfprFirmwareDownloaderFsmRn_Type = SnmpAdminString
_CfprFirmwareDownloaderFsmRn_Object = MibTableColumn
cfprFirmwareDownloaderFsmRn = _CfprFirmwareDownloaderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25, 1, 3),
    _CfprFirmwareDownloaderFsmRn_Type()
)
cfprFirmwareDownloaderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmRn.setStatus("current")
_CfprFirmwareDownloaderFsmCompletionTime_Type = DateAndTime
_CfprFirmwareDownloaderFsmCompletionTime_Object = MibTableColumn
cfprFirmwareDownloaderFsmCompletionTime = _CfprFirmwareDownloaderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25, 1, 4),
    _CfprFirmwareDownloaderFsmCompletionTime_Type()
)
cfprFirmwareDownloaderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmCompletionTime.setStatus("current")
_CfprFirmwareDownloaderFsmCurrentFsm_Type = CfprFirmwareDownloaderFsmCurrentFsm
_CfprFirmwareDownloaderFsmCurrentFsm_Object = MibTableColumn
cfprFirmwareDownloaderFsmCurrentFsm = _CfprFirmwareDownloaderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25, 1, 5),
    _CfprFirmwareDownloaderFsmCurrentFsm_Type()
)
cfprFirmwareDownloaderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmCurrentFsm.setStatus("current")
_CfprFirmwareDownloaderFsmDescrData_Type = SnmpAdminString
_CfprFirmwareDownloaderFsmDescrData_Object = MibTableColumn
cfprFirmwareDownloaderFsmDescrData = _CfprFirmwareDownloaderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25, 1, 6),
    _CfprFirmwareDownloaderFsmDescrData_Type()
)
cfprFirmwareDownloaderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmDescrData.setStatus("current")
_CfprFirmwareDownloaderFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwareDownloaderFsmFsmStatus_Object = MibTableColumn
cfprFirmwareDownloaderFsmFsmStatus = _CfprFirmwareDownloaderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25, 1, 7),
    _CfprFirmwareDownloaderFsmFsmStatus_Type()
)
cfprFirmwareDownloaderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmFsmStatus.setStatus("current")
_CfprFirmwareDownloaderFsmProgress_Type = Gauge32
_CfprFirmwareDownloaderFsmProgress_Object = MibTableColumn
cfprFirmwareDownloaderFsmProgress = _CfprFirmwareDownloaderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25, 1, 8),
    _CfprFirmwareDownloaderFsmProgress_Type()
)
cfprFirmwareDownloaderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmProgress.setStatus("current")
_CfprFirmwareDownloaderFsmRmtErrCode_Type = Gauge32
_CfprFirmwareDownloaderFsmRmtErrCode_Object = MibTableColumn
cfprFirmwareDownloaderFsmRmtErrCode = _CfprFirmwareDownloaderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25, 1, 9),
    _CfprFirmwareDownloaderFsmRmtErrCode_Type()
)
cfprFirmwareDownloaderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmRmtErrCode.setStatus("current")
_CfprFirmwareDownloaderFsmRmtErrDescr_Type = SnmpAdminString
_CfprFirmwareDownloaderFsmRmtErrDescr_Object = MibTableColumn
cfprFirmwareDownloaderFsmRmtErrDescr = _CfprFirmwareDownloaderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25, 1, 10),
    _CfprFirmwareDownloaderFsmRmtErrDescr_Type()
)
cfprFirmwareDownloaderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmRmtErrDescr.setStatus("current")
_CfprFirmwareDownloaderFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwareDownloaderFsmRmtRslt_Object = MibTableColumn
cfprFirmwareDownloaderFsmRmtRslt = _CfprFirmwareDownloaderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 25, 1, 11),
    _CfprFirmwareDownloaderFsmRmtRslt_Type()
)
cfprFirmwareDownloaderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmRmtRslt.setStatus("current")
_CfprFirmwareDownloaderFsmStageTable_Object = MibTable
cfprFirmwareDownloaderFsmStageTable = _CfprFirmwareDownloaderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 26)
)
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStageTable.setStatus("current")
_CfprFirmwareDownloaderFsmStageEntry_Object = MibTableRow
cfprFirmwareDownloaderFsmStageEntry = _CfprFirmwareDownloaderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 26, 1)
)
cfprFirmwareDownloaderFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareDownloaderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStageEntry.setStatus("current")
_CfprFirmwareDownloaderFsmStageInstanceId_Type = CfprManagedObjectId
_CfprFirmwareDownloaderFsmStageInstanceId_Object = MibTableColumn
cfprFirmwareDownloaderFsmStageInstanceId = _CfprFirmwareDownloaderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 26, 1, 1),
    _CfprFirmwareDownloaderFsmStageInstanceId_Type()
)
cfprFirmwareDownloaderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStageInstanceId.setStatus("current")
_CfprFirmwareDownloaderFsmStageDn_Type = CfprManagedObjectDn
_CfprFirmwareDownloaderFsmStageDn_Object = MibTableColumn
cfprFirmwareDownloaderFsmStageDn = _CfprFirmwareDownloaderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 26, 1, 2),
    _CfprFirmwareDownloaderFsmStageDn_Type()
)
cfprFirmwareDownloaderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStageDn.setStatus("current")
_CfprFirmwareDownloaderFsmStageRn_Type = SnmpAdminString
_CfprFirmwareDownloaderFsmStageRn_Object = MibTableColumn
cfprFirmwareDownloaderFsmStageRn = _CfprFirmwareDownloaderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 26, 1, 3),
    _CfprFirmwareDownloaderFsmStageRn_Type()
)
cfprFirmwareDownloaderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStageRn.setStatus("current")
_CfprFirmwareDownloaderFsmStageDescrData_Type = SnmpAdminString
_CfprFirmwareDownloaderFsmStageDescrData_Object = MibTableColumn
cfprFirmwareDownloaderFsmStageDescrData = _CfprFirmwareDownloaderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 26, 1, 4),
    _CfprFirmwareDownloaderFsmStageDescrData_Type()
)
cfprFirmwareDownloaderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStageDescrData.setStatus("current")
_CfprFirmwareDownloaderFsmStageLastUpdateTime_Type = DateAndTime
_CfprFirmwareDownloaderFsmStageLastUpdateTime_Object = MibTableColumn
cfprFirmwareDownloaderFsmStageLastUpdateTime = _CfprFirmwareDownloaderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 26, 1, 5),
    _CfprFirmwareDownloaderFsmStageLastUpdateTime_Type()
)
cfprFirmwareDownloaderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStageLastUpdateTime.setStatus("current")
_CfprFirmwareDownloaderFsmStageName_Type = CfprFirmwareDownloaderFsmStageName
_CfprFirmwareDownloaderFsmStageName_Object = MibTableColumn
cfprFirmwareDownloaderFsmStageName = _CfprFirmwareDownloaderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 26, 1, 6),
    _CfprFirmwareDownloaderFsmStageName_Type()
)
cfprFirmwareDownloaderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStageName.setStatus("current")
_CfprFirmwareDownloaderFsmStageOrder_Type = Gauge32
_CfprFirmwareDownloaderFsmStageOrder_Object = MibTableColumn
cfprFirmwareDownloaderFsmStageOrder = _CfprFirmwareDownloaderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 26, 1, 7),
    _CfprFirmwareDownloaderFsmStageOrder_Type()
)
cfprFirmwareDownloaderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStageOrder.setStatus("current")
_CfprFirmwareDownloaderFsmStageRetry_Type = Gauge32
_CfprFirmwareDownloaderFsmStageRetry_Object = MibTableColumn
cfprFirmwareDownloaderFsmStageRetry = _CfprFirmwareDownloaderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 26, 1, 8),
    _CfprFirmwareDownloaderFsmStageRetry_Type()
)
cfprFirmwareDownloaderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStageRetry.setStatus("current")
_CfprFirmwareDownloaderFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwareDownloaderFsmStageStageStatus_Object = MibTableColumn
cfprFirmwareDownloaderFsmStageStageStatus = _CfprFirmwareDownloaderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 26, 1, 9),
    _CfprFirmwareDownloaderFsmStageStageStatus_Type()
)
cfprFirmwareDownloaderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmStageStageStatus.setStatus("current")
_CfprFirmwareDownloaderFsmTaskTable_Object = MibTable
cfprFirmwareDownloaderFsmTaskTable = _CfprFirmwareDownloaderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 27)
)
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmTaskTable.setStatus("current")
_CfprFirmwareDownloaderFsmTaskEntry_Object = MibTableRow
cfprFirmwareDownloaderFsmTaskEntry = _CfprFirmwareDownloaderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 27, 1)
)
cfprFirmwareDownloaderFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareDownloaderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmTaskEntry.setStatus("current")
_CfprFirmwareDownloaderFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprFirmwareDownloaderFsmTaskInstanceId_Object = MibTableColumn
cfprFirmwareDownloaderFsmTaskInstanceId = _CfprFirmwareDownloaderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 27, 1, 1),
    _CfprFirmwareDownloaderFsmTaskInstanceId_Type()
)
cfprFirmwareDownloaderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmTaskInstanceId.setStatus("current")
_CfprFirmwareDownloaderFsmTaskDn_Type = CfprManagedObjectDn
_CfprFirmwareDownloaderFsmTaskDn_Object = MibTableColumn
cfprFirmwareDownloaderFsmTaskDn = _CfprFirmwareDownloaderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 27, 1, 2),
    _CfprFirmwareDownloaderFsmTaskDn_Type()
)
cfprFirmwareDownloaderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmTaskDn.setStatus("current")
_CfprFirmwareDownloaderFsmTaskRn_Type = SnmpAdminString
_CfprFirmwareDownloaderFsmTaskRn_Object = MibTableColumn
cfprFirmwareDownloaderFsmTaskRn = _CfprFirmwareDownloaderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 27, 1, 3),
    _CfprFirmwareDownloaderFsmTaskRn_Type()
)
cfprFirmwareDownloaderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmTaskRn.setStatus("current")
_CfprFirmwareDownloaderFsmTaskCompletion_Type = CfprFsmCompletion
_CfprFirmwareDownloaderFsmTaskCompletion_Object = MibTableColumn
cfprFirmwareDownloaderFsmTaskCompletion = _CfprFirmwareDownloaderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 27, 1, 4),
    _CfprFirmwareDownloaderFsmTaskCompletion_Type()
)
cfprFirmwareDownloaderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmTaskCompletion.setStatus("current")
_CfprFirmwareDownloaderFsmTaskFlags_Type = CfprFsmFlags
_CfprFirmwareDownloaderFsmTaskFlags_Object = MibTableColumn
cfprFirmwareDownloaderFsmTaskFlags = _CfprFirmwareDownloaderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 27, 1, 5),
    _CfprFirmwareDownloaderFsmTaskFlags_Type()
)
cfprFirmwareDownloaderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmTaskFlags.setStatus("current")
_CfprFirmwareDownloaderFsmTaskItem_Type = CfprFirmwareDownloaderFsmTaskItem
_CfprFirmwareDownloaderFsmTaskItem_Object = MibTableColumn
cfprFirmwareDownloaderFsmTaskItem = _CfprFirmwareDownloaderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 27, 1, 6),
    _CfprFirmwareDownloaderFsmTaskItem_Type()
)
cfprFirmwareDownloaderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmTaskItem.setStatus("current")
_CfprFirmwareDownloaderFsmTaskSeqId_Type = Gauge32
_CfprFirmwareDownloaderFsmTaskSeqId_Object = MibTableColumn
cfprFirmwareDownloaderFsmTaskSeqId = _CfprFirmwareDownloaderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 27, 1, 7),
    _CfprFirmwareDownloaderFsmTaskSeqId_Type()
)
cfprFirmwareDownloaderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDownloaderFsmTaskSeqId.setStatus("current")
_CfprFirmwareHostTable_Object = MibTable
cfprFirmwareHostTable = _CfprFirmwareHostTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 28)
)
if mibBuilder.loadTexts:
    cfprFirmwareHostTable.setStatus("current")
_CfprFirmwareHostEntry_Object = MibTableRow
cfprFirmwareHostEntry = _CfprFirmwareHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 28, 1)
)
cfprFirmwareHostEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareHostInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareHostEntry.setStatus("current")
_CfprFirmwareHostInstanceId_Type = CfprManagedObjectId
_CfprFirmwareHostInstanceId_Object = MibTableColumn
cfprFirmwareHostInstanceId = _CfprFirmwareHostInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 28, 1, 1),
    _CfprFirmwareHostInstanceId_Type()
)
cfprFirmwareHostInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareHostInstanceId.setStatus("current")
_CfprFirmwareHostDn_Type = CfprManagedObjectDn
_CfprFirmwareHostDn_Object = MibTableColumn
cfprFirmwareHostDn = _CfprFirmwareHostDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 28, 1, 2),
    _CfprFirmwareHostDn_Type()
)
cfprFirmwareHostDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareHostDn.setStatus("current")
_CfprFirmwareHostRn_Type = SnmpAdminString
_CfprFirmwareHostRn_Object = MibTableColumn
cfprFirmwareHostRn = _CfprFirmwareHostRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 28, 1, 3),
    _CfprFirmwareHostRn_Type()
)
cfprFirmwareHostRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareHostRn.setStatus("current")
_CfprFirmwareHostPackModImpactTable_Object = MibTable
cfprFirmwareHostPackModImpactTable = _CfprFirmwareHostPackModImpactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 29)
)
if mibBuilder.loadTexts:
    cfprFirmwareHostPackModImpactTable.setStatus("current")
_CfprFirmwareHostPackModImpactEntry_Object = MibTableRow
cfprFirmwareHostPackModImpactEntry = _CfprFirmwareHostPackModImpactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 29, 1)
)
cfprFirmwareHostPackModImpactEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareHostPackModImpactInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareHostPackModImpactEntry.setStatus("current")
_CfprFirmwareHostPackModImpactInstanceId_Type = CfprManagedObjectId
_CfprFirmwareHostPackModImpactInstanceId_Object = MibTableColumn
cfprFirmwareHostPackModImpactInstanceId = _CfprFirmwareHostPackModImpactInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 29, 1, 1),
    _CfprFirmwareHostPackModImpactInstanceId_Type()
)
cfprFirmwareHostPackModImpactInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareHostPackModImpactInstanceId.setStatus("current")
_CfprFirmwareHostPackModImpactDn_Type = CfprManagedObjectDn
_CfprFirmwareHostPackModImpactDn_Object = MibTableColumn
cfprFirmwareHostPackModImpactDn = _CfprFirmwareHostPackModImpactDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 29, 1, 2),
    _CfprFirmwareHostPackModImpactDn_Type()
)
cfprFirmwareHostPackModImpactDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareHostPackModImpactDn.setStatus("current")
_CfprFirmwareHostPackModImpactRn_Type = SnmpAdminString
_CfprFirmwareHostPackModImpactRn_Object = MibTableColumn
cfprFirmwareHostPackModImpactRn = _CfprFirmwareHostPackModImpactRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 29, 1, 3),
    _CfprFirmwareHostPackModImpactRn_Type()
)
cfprFirmwareHostPackModImpactRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareHostPackModImpactRn.setStatus("current")
_CfprFirmwareHostPackModImpactKeyDn_Type = SnmpAdminString
_CfprFirmwareHostPackModImpactKeyDn_Object = MibTableColumn
cfprFirmwareHostPackModImpactKeyDn = _CfprFirmwareHostPackModImpactKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 29, 1, 4),
    _CfprFirmwareHostPackModImpactKeyDn_Type()
)
cfprFirmwareHostPackModImpactKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareHostPackModImpactKeyDn.setStatus("current")
_CfprFirmwareHostPackModImpactMaintPolicyDn_Type = SnmpAdminString
_CfprFirmwareHostPackModImpactMaintPolicyDn_Object = MibTableColumn
cfprFirmwareHostPackModImpactMaintPolicyDn = _CfprFirmwareHostPackModImpactMaintPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 29, 1, 5),
    _CfprFirmwareHostPackModImpactMaintPolicyDn_Type()
)
cfprFirmwareHostPackModImpactMaintPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareHostPackModImpactMaintPolicyDn.setStatus("current")
_CfprFirmwareHostPackModImpactPnDn_Type = SnmpAdminString
_CfprFirmwareHostPackModImpactPnDn_Object = MibTableColumn
cfprFirmwareHostPackModImpactPnDn = _CfprFirmwareHostPackModImpactPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 29, 1, 6),
    _CfprFirmwareHostPackModImpactPnDn_Type()
)
cfprFirmwareHostPackModImpactPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareHostPackModImpactPnDn.setStatus("current")
_CfprFirmwareHostPackModImpactRebootPolicy_Type = SnmpAdminString
_CfprFirmwareHostPackModImpactRebootPolicy_Object = MibTableColumn
cfprFirmwareHostPackModImpactRebootPolicy = _CfprFirmwareHostPackModImpactRebootPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 29, 1, 7),
    _CfprFirmwareHostPackModImpactRebootPolicy_Type()
)
cfprFirmwareHostPackModImpactRebootPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareHostPackModImpactRebootPolicy.setStatus("current")
_CfprFirmwareHostPackModImpactServiceProfileDn_Type = SnmpAdminString
_CfprFirmwareHostPackModImpactServiceProfileDn_Object = MibTableColumn
cfprFirmwareHostPackModImpactServiceProfileDn = _CfprFirmwareHostPackModImpactServiceProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 29, 1, 8),
    _CfprFirmwareHostPackModImpactServiceProfileDn_Type()
)
cfprFirmwareHostPackModImpactServiceProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareHostPackModImpactServiceProfileDn.setStatus("current")
_CfprFirmwareImageTable_Object = MibTable
cfprFirmwareImageTable = _CfprFirmwareImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30)
)
if mibBuilder.loadTexts:
    cfprFirmwareImageTable.setStatus("current")
_CfprFirmwareImageEntry_Object = MibTableRow
cfprFirmwareImageEntry = _CfprFirmwareImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1)
)
cfprFirmwareImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareImageEntry.setStatus("current")
_CfprFirmwareImageInstanceId_Type = CfprManagedObjectId
_CfprFirmwareImageInstanceId_Object = MibTableColumn
cfprFirmwareImageInstanceId = _CfprFirmwareImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 1),
    _CfprFirmwareImageInstanceId_Type()
)
cfprFirmwareImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareImageInstanceId.setStatus("current")
_CfprFirmwareImageDn_Type = CfprManagedObjectDn
_CfprFirmwareImageDn_Object = MibTableColumn
cfprFirmwareImageDn = _CfprFirmwareImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 2),
    _CfprFirmwareImageDn_Type()
)
cfprFirmwareImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageDn.setStatus("current")
_CfprFirmwareImageRn_Type = SnmpAdminString
_CfprFirmwareImageRn_Object = MibTableColumn
cfprFirmwareImageRn = _CfprFirmwareImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 3),
    _CfprFirmwareImageRn_Type()
)
cfprFirmwareImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageRn.setStatus("current")
_CfprFirmwareImageAdminState_Type = CfprFirmwareAdminState
_CfprFirmwareImageAdminState_Object = MibTableColumn
cfprFirmwareImageAdminState = _CfprFirmwareImageAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 4),
    _CfprFirmwareImageAdminState_Type()
)
cfprFirmwareImageAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageAdminState.setStatus("current")
_CfprFirmwareImageChecksum_Type = SnmpAdminString
_CfprFirmwareImageChecksum_Object = MibTableColumn
cfprFirmwareImageChecksum = _CfprFirmwareImageChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 5),
    _CfprFirmwareImageChecksum_Type()
)
cfprFirmwareImageChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageChecksum.setStatus("current")
_CfprFirmwareImageDescr_Type = SnmpAdminString
_CfprFirmwareImageDescr_Object = MibTableColumn
cfprFirmwareImageDescr = _CfprFirmwareImageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 6),
    _CfprFirmwareImageDescr_Type()
)
cfprFirmwareImageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageDescr.setStatus("current")
_CfprFirmwareImageDownloadDate_Type = DateAndTime
_CfprFirmwareImageDownloadDate_Object = MibTableColumn
cfprFirmwareImageDownloadDate = _CfprFirmwareImageDownloadDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 7),
    _CfprFirmwareImageDownloadDate_Type()
)
cfprFirmwareImageDownloadDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageDownloadDate.setStatus("current")
_CfprFirmwareImageFsmDescr_Type = SnmpAdminString
_CfprFirmwareImageFsmDescr_Object = MibTableColumn
cfprFirmwareImageFsmDescr = _CfprFirmwareImageFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 8),
    _CfprFirmwareImageFsmDescr_Type()
)
cfprFirmwareImageFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmDescr.setStatus("current")
_CfprFirmwareImageFsmPrev_Type = SnmpAdminString
_CfprFirmwareImageFsmPrev_Object = MibTableColumn
cfprFirmwareImageFsmPrev = _CfprFirmwareImageFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 9),
    _CfprFirmwareImageFsmPrev_Type()
)
cfprFirmwareImageFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmPrev.setStatus("current")
_CfprFirmwareImageFsmProgr_Type = Gauge32
_CfprFirmwareImageFsmProgr_Object = MibTableColumn
cfprFirmwareImageFsmProgr = _CfprFirmwareImageFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 10),
    _CfprFirmwareImageFsmProgr_Type()
)
cfprFirmwareImageFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmProgr.setStatus("current")
_CfprFirmwareImageFsmRmtInvErrCode_Type = Gauge32
_CfprFirmwareImageFsmRmtInvErrCode_Object = MibTableColumn
cfprFirmwareImageFsmRmtInvErrCode = _CfprFirmwareImageFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 11),
    _CfprFirmwareImageFsmRmtInvErrCode_Type()
)
cfprFirmwareImageFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmRmtInvErrCode.setStatus("current")
_CfprFirmwareImageFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprFirmwareImageFsmRmtInvErrDescr_Object = MibTableColumn
cfprFirmwareImageFsmRmtInvErrDescr = _CfprFirmwareImageFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 12),
    _CfprFirmwareImageFsmRmtInvErrDescr_Type()
)
cfprFirmwareImageFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmRmtInvErrDescr.setStatus("current")
_CfprFirmwareImageFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwareImageFsmRmtInvRslt_Object = MibTableColumn
cfprFirmwareImageFsmRmtInvRslt = _CfprFirmwareImageFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 13),
    _CfprFirmwareImageFsmRmtInvRslt_Type()
)
cfprFirmwareImageFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmRmtInvRslt.setStatus("current")
_CfprFirmwareImageFsmStageDescr_Type = SnmpAdminString
_CfprFirmwareImageFsmStageDescr_Object = MibTableColumn
cfprFirmwareImageFsmStageDescr = _CfprFirmwareImageFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 14),
    _CfprFirmwareImageFsmStageDescr_Type()
)
cfprFirmwareImageFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStageDescr.setStatus("current")
_CfprFirmwareImageFsmStamp_Type = DateAndTime
_CfprFirmwareImageFsmStamp_Object = MibTableColumn
cfprFirmwareImageFsmStamp = _CfprFirmwareImageFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 15),
    _CfprFirmwareImageFsmStamp_Type()
)
cfprFirmwareImageFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStamp.setStatus("current")
_CfprFirmwareImageFsmStatus_Type = SnmpAdminString
_CfprFirmwareImageFsmStatus_Object = MibTableColumn
cfprFirmwareImageFsmStatus = _CfprFirmwareImageFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 16),
    _CfprFirmwareImageFsmStatus_Type()
)
cfprFirmwareImageFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStatus.setStatus("current")
_CfprFirmwareImageFsmTry_Type = Gauge32
_CfprFirmwareImageFsmTry_Object = MibTableColumn
cfprFirmwareImageFsmTry = _CfprFirmwareImageFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 17),
    _CfprFirmwareImageFsmTry_Type()
)
cfprFirmwareImageFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmTry.setStatus("current")
_CfprFirmwareImageImagePresence_Type = CfprFirmwareImagePresence
_CfprFirmwareImageImagePresence_Object = MibTableColumn
cfprFirmwareImageImagePresence = _CfprFirmwareImageImagePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 18),
    _CfprFirmwareImageImagePresence_Type()
)
cfprFirmwareImageImagePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageImagePresence.setStatus("current")
_CfprFirmwareImageIntId_Type = SnmpAdminString
_CfprFirmwareImageIntId_Object = MibTableColumn
cfprFirmwareImageIntId = _CfprFirmwareImageIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 19),
    _CfprFirmwareImageIntId_Type()
)
cfprFirmwareImageIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageIntId.setStatus("current")
_CfprFirmwareImageInvTag_Type = SnmpAdminString
_CfprFirmwareImageInvTag_Object = MibTableColumn
cfprFirmwareImageInvTag = _CfprFirmwareImageInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 20),
    _CfprFirmwareImageInvTag_Type()
)
cfprFirmwareImageInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageInvTag.setStatus("current")
_CfprFirmwareImageIsoname_Type = SnmpAdminString
_CfprFirmwareImageIsoname_Object = MibTableColumn
cfprFirmwareImageIsoname = _CfprFirmwareImageIsoname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 21),
    _CfprFirmwareImageIsoname_Type()
)
cfprFirmwareImageIsoname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageIsoname.setStatus("current")
_CfprFirmwareImageLocation_Type = SnmpAdminString
_CfprFirmwareImageLocation_Object = MibTableColumn
cfprFirmwareImageLocation = _CfprFirmwareImageLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 22),
    _CfprFirmwareImageLocation_Type()
)
cfprFirmwareImageLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageLocation.setStatus("current")
_CfprFirmwareImageName_Type = SnmpAdminString
_CfprFirmwareImageName_Object = MibTableColumn
cfprFirmwareImageName = _CfprFirmwareImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 23),
    _CfprFirmwareImageName_Type()
)
cfprFirmwareImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageName.setStatus("current")
_CfprFirmwareImagePolicyLevel_Type = Gauge32
_CfprFirmwareImagePolicyLevel_Object = MibTableColumn
cfprFirmwareImagePolicyLevel = _CfprFirmwareImagePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 24),
    _CfprFirmwareImagePolicyLevel_Type()
)
cfprFirmwareImagePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImagePolicyLevel.setStatus("current")
_CfprFirmwareImagePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwareImagePolicyOwner_Object = MibTableColumn
cfprFirmwareImagePolicyOwner = _CfprFirmwareImagePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 25),
    _CfprFirmwareImagePolicyOwner_Type()
)
cfprFirmwareImagePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImagePolicyOwner.setStatus("current")
_CfprFirmwareImageSize_Type = Unsigned64
_CfprFirmwareImageSize_Object = MibTableColumn
cfprFirmwareImageSize = _CfprFirmwareImageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 26),
    _CfprFirmwareImageSize_Type()
)
cfprFirmwareImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageSize.setStatus("current")
_CfprFirmwareImageType_Type = CfprFirmwareType
_CfprFirmwareImageType_Object = MibTableColumn
cfprFirmwareImageType = _CfprFirmwareImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 27),
    _CfprFirmwareImageType_Type()
)
cfprFirmwareImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageType.setStatus("current")
_CfprFirmwareImageVersion_Type = SnmpAdminString
_CfprFirmwareImageVersion_Object = MibTableColumn
cfprFirmwareImageVersion = _CfprFirmwareImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 28),
    _CfprFirmwareImageVersion_Type()
)
cfprFirmwareImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageVersion.setStatus("current")
_CfprFirmwareImageIsApplicableForEquippedSsd_Type = TruthValue
_CfprFirmwareImageIsApplicableForEquippedSsd_Object = MibTableColumn
cfprFirmwareImageIsApplicableForEquippedSsd = _CfprFirmwareImageIsApplicableForEquippedSsd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 30, 1, 29),
    _CfprFirmwareImageIsApplicableForEquippedSsd_Type()
)
cfprFirmwareImageIsApplicableForEquippedSsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageIsApplicableForEquippedSsd.setStatus("current")
_CfprFirmwareImageFsmTable_Object = MibTable
cfprFirmwareImageFsmTable = _CfprFirmwareImageFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31)
)
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmTable.setStatus("current")
_CfprFirmwareImageFsmEntry_Object = MibTableRow
cfprFirmwareImageFsmEntry = _CfprFirmwareImageFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31, 1)
)
cfprFirmwareImageFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareImageFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmEntry.setStatus("current")
_CfprFirmwareImageFsmInstanceId_Type = CfprManagedObjectId
_CfprFirmwareImageFsmInstanceId_Object = MibTableColumn
cfprFirmwareImageFsmInstanceId = _CfprFirmwareImageFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31, 1, 1),
    _CfprFirmwareImageFsmInstanceId_Type()
)
cfprFirmwareImageFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmInstanceId.setStatus("current")
_CfprFirmwareImageFsmDn_Type = CfprManagedObjectDn
_CfprFirmwareImageFsmDn_Object = MibTableColumn
cfprFirmwareImageFsmDn = _CfprFirmwareImageFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31, 1, 2),
    _CfprFirmwareImageFsmDn_Type()
)
cfprFirmwareImageFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmDn.setStatus("current")
_CfprFirmwareImageFsmRn_Type = SnmpAdminString
_CfprFirmwareImageFsmRn_Object = MibTableColumn
cfprFirmwareImageFsmRn = _CfprFirmwareImageFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31, 1, 3),
    _CfprFirmwareImageFsmRn_Type()
)
cfprFirmwareImageFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmRn.setStatus("current")
_CfprFirmwareImageFsmCompletionTime_Type = DateAndTime
_CfprFirmwareImageFsmCompletionTime_Object = MibTableColumn
cfprFirmwareImageFsmCompletionTime = _CfprFirmwareImageFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31, 1, 4),
    _CfprFirmwareImageFsmCompletionTime_Type()
)
cfprFirmwareImageFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmCompletionTime.setStatus("current")
_CfprFirmwareImageFsmCurrentFsm_Type = CfprFirmwareImageFsmCurrentFsm
_CfprFirmwareImageFsmCurrentFsm_Object = MibTableColumn
cfprFirmwareImageFsmCurrentFsm = _CfprFirmwareImageFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31, 1, 5),
    _CfprFirmwareImageFsmCurrentFsm_Type()
)
cfprFirmwareImageFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmCurrentFsm.setStatus("current")
_CfprFirmwareImageFsmDescrData_Type = SnmpAdminString
_CfprFirmwareImageFsmDescrData_Object = MibTableColumn
cfprFirmwareImageFsmDescrData = _CfprFirmwareImageFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31, 1, 6),
    _CfprFirmwareImageFsmDescrData_Type()
)
cfprFirmwareImageFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmDescrData.setStatus("current")
_CfprFirmwareImageFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwareImageFsmFsmStatus_Object = MibTableColumn
cfprFirmwareImageFsmFsmStatus = _CfprFirmwareImageFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31, 1, 7),
    _CfprFirmwareImageFsmFsmStatus_Type()
)
cfprFirmwareImageFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmFsmStatus.setStatus("current")
_CfprFirmwareImageFsmProgress_Type = Gauge32
_CfprFirmwareImageFsmProgress_Object = MibTableColumn
cfprFirmwareImageFsmProgress = _CfprFirmwareImageFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31, 1, 8),
    _CfprFirmwareImageFsmProgress_Type()
)
cfprFirmwareImageFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmProgress.setStatus("current")
_CfprFirmwareImageFsmRmtErrCode_Type = Gauge32
_CfprFirmwareImageFsmRmtErrCode_Object = MibTableColumn
cfprFirmwareImageFsmRmtErrCode = _CfprFirmwareImageFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31, 1, 9),
    _CfprFirmwareImageFsmRmtErrCode_Type()
)
cfprFirmwareImageFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmRmtErrCode.setStatus("current")
_CfprFirmwareImageFsmRmtErrDescr_Type = SnmpAdminString
_CfprFirmwareImageFsmRmtErrDescr_Object = MibTableColumn
cfprFirmwareImageFsmRmtErrDescr = _CfprFirmwareImageFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31, 1, 10),
    _CfprFirmwareImageFsmRmtErrDescr_Type()
)
cfprFirmwareImageFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmRmtErrDescr.setStatus("current")
_CfprFirmwareImageFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwareImageFsmRmtRslt_Object = MibTableColumn
cfprFirmwareImageFsmRmtRslt = _CfprFirmwareImageFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 31, 1, 11),
    _CfprFirmwareImageFsmRmtRslt_Type()
)
cfprFirmwareImageFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmRmtRslt.setStatus("current")
_CfprFirmwareImageFsmStageTable_Object = MibTable
cfprFirmwareImageFsmStageTable = _CfprFirmwareImageFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 32)
)
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStageTable.setStatus("current")
_CfprFirmwareImageFsmStageEntry_Object = MibTableRow
cfprFirmwareImageFsmStageEntry = _CfprFirmwareImageFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 32, 1)
)
cfprFirmwareImageFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareImageFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStageEntry.setStatus("current")
_CfprFirmwareImageFsmStageInstanceId_Type = CfprManagedObjectId
_CfprFirmwareImageFsmStageInstanceId_Object = MibTableColumn
cfprFirmwareImageFsmStageInstanceId = _CfprFirmwareImageFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 32, 1, 1),
    _CfprFirmwareImageFsmStageInstanceId_Type()
)
cfprFirmwareImageFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStageInstanceId.setStatus("current")
_CfprFirmwareImageFsmStageDn_Type = CfprManagedObjectDn
_CfprFirmwareImageFsmStageDn_Object = MibTableColumn
cfprFirmwareImageFsmStageDn = _CfprFirmwareImageFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 32, 1, 2),
    _CfprFirmwareImageFsmStageDn_Type()
)
cfprFirmwareImageFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStageDn.setStatus("current")
_CfprFirmwareImageFsmStageRn_Type = SnmpAdminString
_CfprFirmwareImageFsmStageRn_Object = MibTableColumn
cfprFirmwareImageFsmStageRn = _CfprFirmwareImageFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 32, 1, 3),
    _CfprFirmwareImageFsmStageRn_Type()
)
cfprFirmwareImageFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStageRn.setStatus("current")
_CfprFirmwareImageFsmStageDescrData_Type = SnmpAdminString
_CfprFirmwareImageFsmStageDescrData_Object = MibTableColumn
cfprFirmwareImageFsmStageDescrData = _CfprFirmwareImageFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 32, 1, 4),
    _CfprFirmwareImageFsmStageDescrData_Type()
)
cfprFirmwareImageFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStageDescrData.setStatus("current")
_CfprFirmwareImageFsmStageLastUpdateTime_Type = DateAndTime
_CfprFirmwareImageFsmStageLastUpdateTime_Object = MibTableColumn
cfprFirmwareImageFsmStageLastUpdateTime = _CfprFirmwareImageFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 32, 1, 5),
    _CfprFirmwareImageFsmStageLastUpdateTime_Type()
)
cfprFirmwareImageFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStageLastUpdateTime.setStatus("current")
_CfprFirmwareImageFsmStageName_Type = CfprFirmwareImageFsmStageName
_CfprFirmwareImageFsmStageName_Object = MibTableColumn
cfprFirmwareImageFsmStageName = _CfprFirmwareImageFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 32, 1, 6),
    _CfprFirmwareImageFsmStageName_Type()
)
cfprFirmwareImageFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStageName.setStatus("current")
_CfprFirmwareImageFsmStageOrder_Type = Gauge32
_CfprFirmwareImageFsmStageOrder_Object = MibTableColumn
cfprFirmwareImageFsmStageOrder = _CfprFirmwareImageFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 32, 1, 7),
    _CfprFirmwareImageFsmStageOrder_Type()
)
cfprFirmwareImageFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStageOrder.setStatus("current")
_CfprFirmwareImageFsmStageRetry_Type = Gauge32
_CfprFirmwareImageFsmStageRetry_Object = MibTableColumn
cfprFirmwareImageFsmStageRetry = _CfprFirmwareImageFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 32, 1, 8),
    _CfprFirmwareImageFsmStageRetry_Type()
)
cfprFirmwareImageFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStageRetry.setStatus("current")
_CfprFirmwareImageFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwareImageFsmStageStageStatus_Object = MibTableColumn
cfprFirmwareImageFsmStageStageStatus = _CfprFirmwareImageFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 32, 1, 9),
    _CfprFirmwareImageFsmStageStageStatus_Type()
)
cfprFirmwareImageFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmStageStageStatus.setStatus("current")
_CfprFirmwareImageFsmTaskTable_Object = MibTable
cfprFirmwareImageFsmTaskTable = _CfprFirmwareImageFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 33)
)
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmTaskTable.setStatus("current")
_CfprFirmwareImageFsmTaskEntry_Object = MibTableRow
cfprFirmwareImageFsmTaskEntry = _CfprFirmwareImageFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 33, 1)
)
cfprFirmwareImageFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareImageFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmTaskEntry.setStatus("current")
_CfprFirmwareImageFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprFirmwareImageFsmTaskInstanceId_Object = MibTableColumn
cfprFirmwareImageFsmTaskInstanceId = _CfprFirmwareImageFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 33, 1, 1),
    _CfprFirmwareImageFsmTaskInstanceId_Type()
)
cfprFirmwareImageFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmTaskInstanceId.setStatus("current")
_CfprFirmwareImageFsmTaskDn_Type = CfprManagedObjectDn
_CfprFirmwareImageFsmTaskDn_Object = MibTableColumn
cfprFirmwareImageFsmTaskDn = _CfprFirmwareImageFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 33, 1, 2),
    _CfprFirmwareImageFsmTaskDn_Type()
)
cfprFirmwareImageFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmTaskDn.setStatus("current")
_CfprFirmwareImageFsmTaskRn_Type = SnmpAdminString
_CfprFirmwareImageFsmTaskRn_Object = MibTableColumn
cfprFirmwareImageFsmTaskRn = _CfprFirmwareImageFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 33, 1, 3),
    _CfprFirmwareImageFsmTaskRn_Type()
)
cfprFirmwareImageFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmTaskRn.setStatus("current")
_CfprFirmwareImageFsmTaskCompletion_Type = CfprFsmCompletion
_CfprFirmwareImageFsmTaskCompletion_Object = MibTableColumn
cfprFirmwareImageFsmTaskCompletion = _CfprFirmwareImageFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 33, 1, 4),
    _CfprFirmwareImageFsmTaskCompletion_Type()
)
cfprFirmwareImageFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmTaskCompletion.setStatus("current")
_CfprFirmwareImageFsmTaskFlags_Type = CfprFsmFlags
_CfprFirmwareImageFsmTaskFlags_Object = MibTableColumn
cfprFirmwareImageFsmTaskFlags = _CfprFirmwareImageFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 33, 1, 5),
    _CfprFirmwareImageFsmTaskFlags_Type()
)
cfprFirmwareImageFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmTaskFlags.setStatus("current")
_CfprFirmwareImageFsmTaskItem_Type = CfprFirmwareImageFsmTaskItem
_CfprFirmwareImageFsmTaskItem_Object = MibTableColumn
cfprFirmwareImageFsmTaskItem = _CfprFirmwareImageFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 33, 1, 6),
    _CfprFirmwareImageFsmTaskItem_Type()
)
cfprFirmwareImageFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmTaskItem.setStatus("current")
_CfprFirmwareImageFsmTaskSeqId_Type = Gauge32
_CfprFirmwareImageFsmTaskSeqId_Object = MibTableColumn
cfprFirmwareImageFsmTaskSeqId = _CfprFirmwareImageFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 33, 1, 7),
    _CfprFirmwareImageFsmTaskSeqId_Type()
)
cfprFirmwareImageFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageFsmTaskSeqId.setStatus("current")
_CfprFirmwareImageLockTable_Object = MibTable
cfprFirmwareImageLockTable = _CfprFirmwareImageLockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 34)
)
if mibBuilder.loadTexts:
    cfprFirmwareImageLockTable.setStatus("current")
_CfprFirmwareImageLockEntry_Object = MibTableRow
cfprFirmwareImageLockEntry = _CfprFirmwareImageLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 34, 1)
)
cfprFirmwareImageLockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareImageLockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareImageLockEntry.setStatus("current")
_CfprFirmwareImageLockInstanceId_Type = CfprManagedObjectId
_CfprFirmwareImageLockInstanceId_Object = MibTableColumn
cfprFirmwareImageLockInstanceId = _CfprFirmwareImageLockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 34, 1, 1),
    _CfprFirmwareImageLockInstanceId_Type()
)
cfprFirmwareImageLockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareImageLockInstanceId.setStatus("current")
_CfprFirmwareImageLockDn_Type = CfprManagedObjectDn
_CfprFirmwareImageLockDn_Object = MibTableColumn
cfprFirmwareImageLockDn = _CfprFirmwareImageLockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 34, 1, 2),
    _CfprFirmwareImageLockDn_Type()
)
cfprFirmwareImageLockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageLockDn.setStatus("current")
_CfprFirmwareImageLockRn_Type = SnmpAdminString
_CfprFirmwareImageLockRn_Object = MibTableColumn
cfprFirmwareImageLockRn = _CfprFirmwareImageLockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 34, 1, 3),
    _CfprFirmwareImageLockRn_Type()
)
cfprFirmwareImageLockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageLockRn.setStatus("current")
_CfprFirmwareImageLockImageNameDn_Type = SnmpAdminString
_CfprFirmwareImageLockImageNameDn_Object = MibTableColumn
cfprFirmwareImageLockImageNameDn = _CfprFirmwareImageLockImageNameDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 34, 1, 4),
    _CfprFirmwareImageLockImageNameDn_Type()
)
cfprFirmwareImageLockImageNameDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageLockImageNameDn.setStatus("current")
_CfprFirmwareImageLockName_Type = SnmpAdminString
_CfprFirmwareImageLockName_Object = MibTableColumn
cfprFirmwareImageLockName = _CfprFirmwareImageLockName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 34, 1, 5),
    _CfprFirmwareImageLockName_Type()
)
cfprFirmwareImageLockName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareImageLockName.setStatus("current")
_CfprFirmwareInfraTable_Object = MibTable
cfprFirmwareInfraTable = _CfprFirmwareInfraTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35)
)
if mibBuilder.loadTexts:
    cfprFirmwareInfraTable.setStatus("current")
_CfprFirmwareInfraEntry_Object = MibTableRow
cfprFirmwareInfraEntry = _CfprFirmwareInfraEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1)
)
cfprFirmwareInfraEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareInfraInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareInfraEntry.setStatus("current")
_CfprFirmwareInfraInstanceId_Type = CfprManagedObjectId
_CfprFirmwareInfraInstanceId_Object = MibTableColumn
cfprFirmwareInfraInstanceId = _CfprFirmwareInfraInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 1),
    _CfprFirmwareInfraInstanceId_Type()
)
cfprFirmwareInfraInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareInfraInstanceId.setStatus("current")
_CfprFirmwareInfraDn_Type = CfprManagedObjectDn
_CfprFirmwareInfraDn_Object = MibTableColumn
cfprFirmwareInfraDn = _CfprFirmwareInfraDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 2),
    _CfprFirmwareInfraDn_Type()
)
cfprFirmwareInfraDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraDn.setStatus("current")
_CfprFirmwareInfraRn_Type = SnmpAdminString
_CfprFirmwareInfraRn_Object = MibTableColumn
cfprFirmwareInfraRn = _CfprFirmwareInfraRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 3),
    _CfprFirmwareInfraRn_Type()
)
cfprFirmwareInfraRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraRn.setStatus("current")
_CfprFirmwareInfraAdminState_Type = CfprTrigAdminState
_CfprFirmwareInfraAdminState_Object = MibTableColumn
cfprFirmwareInfraAdminState = _CfprFirmwareInfraAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 4),
    _CfprFirmwareInfraAdminState_Type()
)
cfprFirmwareInfraAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraAdminState.setStatus("current")
_CfprFirmwareInfraAutoDelete_Type = TruthValue
_CfprFirmwareInfraAutoDelete_Object = MibTableColumn
cfprFirmwareInfraAutoDelete = _CfprFirmwareInfraAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 5),
    _CfprFirmwareInfraAutoDelete_Type()
)
cfprFirmwareInfraAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraAutoDelete.setStatus("current")
_CfprFirmwareInfraDescr_Type = SnmpAdminString
_CfprFirmwareInfraDescr_Object = MibTableColumn
cfprFirmwareInfraDescr = _CfprFirmwareInfraDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 6),
    _CfprFirmwareInfraDescr_Type()
)
cfprFirmwareInfraDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraDescr.setStatus("current")
_CfprFirmwareInfraIgnoreCap_Type = TruthValue
_CfprFirmwareInfraIgnoreCap_Object = MibTableColumn
cfprFirmwareInfraIgnoreCap = _CfprFirmwareInfraIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 7),
    _CfprFirmwareInfraIgnoreCap_Type()
)
cfprFirmwareInfraIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraIgnoreCap.setStatus("current")
_CfprFirmwareInfraIntId_Type = SnmpAdminString
_CfprFirmwareInfraIntId_Object = MibTableColumn
cfprFirmwareInfraIntId = _CfprFirmwareInfraIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 8),
    _CfprFirmwareInfraIntId_Type()
)
cfprFirmwareInfraIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraIntId.setStatus("current")
_CfprFirmwareInfraName_Type = SnmpAdminString
_CfprFirmwareInfraName_Object = MibTableColumn
cfprFirmwareInfraName = _CfprFirmwareInfraName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 9),
    _CfprFirmwareInfraName_Type()
)
cfprFirmwareInfraName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraName.setStatus("current")
_CfprFirmwareInfraOperScheduler_Type = SnmpAdminString
_CfprFirmwareInfraOperScheduler_Object = MibTableColumn
cfprFirmwareInfraOperScheduler = _CfprFirmwareInfraOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 10),
    _CfprFirmwareInfraOperScheduler_Type()
)
cfprFirmwareInfraOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraOperScheduler.setStatus("current")
_CfprFirmwareInfraOperState_Type = CfprTrigTrigOperState
_CfprFirmwareInfraOperState_Object = MibTableColumn
cfprFirmwareInfraOperState = _CfprFirmwareInfraOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 11),
    _CfprFirmwareInfraOperState_Type()
)
cfprFirmwareInfraOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraOperState.setStatus("current")
_CfprFirmwareInfraOperVersion_Type = SnmpAdminString
_CfprFirmwareInfraOperVersion_Object = MibTableColumn
cfprFirmwareInfraOperVersion = _CfprFirmwareInfraOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 12),
    _CfprFirmwareInfraOperVersion_Type()
)
cfprFirmwareInfraOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraOperVersion.setStatus("current")
_CfprFirmwareInfraPolicyLevel_Type = Gauge32
_CfprFirmwareInfraPolicyLevel_Object = MibTableColumn
cfprFirmwareInfraPolicyLevel = _CfprFirmwareInfraPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 13),
    _CfprFirmwareInfraPolicyLevel_Type()
)
cfprFirmwareInfraPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPolicyLevel.setStatus("current")
_CfprFirmwareInfraPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwareInfraPolicyOwner_Object = MibTableColumn
cfprFirmwareInfraPolicyOwner = _CfprFirmwareInfraPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 14),
    _CfprFirmwareInfraPolicyOwner_Type()
)
cfprFirmwareInfraPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPolicyOwner.setStatus("current")
_CfprFirmwareInfraScheduler_Type = SnmpAdminString
_CfprFirmwareInfraScheduler_Object = MibTableColumn
cfprFirmwareInfraScheduler = _CfprFirmwareInfraScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 35, 1, 15),
    _CfprFirmwareInfraScheduler_Type()
)
cfprFirmwareInfraScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraScheduler.setStatus("current")
_CfprFirmwareInfraPackTable_Object = MibTable
cfprFirmwareInfraPackTable = _CfprFirmwareInfraPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36)
)
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackTable.setStatus("current")
_CfprFirmwareInfraPackEntry_Object = MibTableRow
cfprFirmwareInfraPackEntry = _CfprFirmwareInfraPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1)
)
cfprFirmwareInfraPackEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareInfraPackInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackEntry.setStatus("current")
_CfprFirmwareInfraPackInstanceId_Type = CfprManagedObjectId
_CfprFirmwareInfraPackInstanceId_Object = MibTableColumn
cfprFirmwareInfraPackInstanceId = _CfprFirmwareInfraPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 1),
    _CfprFirmwareInfraPackInstanceId_Type()
)
cfprFirmwareInfraPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackInstanceId.setStatus("current")
_CfprFirmwareInfraPackDn_Type = CfprManagedObjectDn
_CfprFirmwareInfraPackDn_Object = MibTableColumn
cfprFirmwareInfraPackDn = _CfprFirmwareInfraPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 2),
    _CfprFirmwareInfraPackDn_Type()
)
cfprFirmwareInfraPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackDn.setStatus("current")
_CfprFirmwareInfraPackRn_Type = SnmpAdminString
_CfprFirmwareInfraPackRn_Object = MibTableColumn
cfprFirmwareInfraPackRn = _CfprFirmwareInfraPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 3),
    _CfprFirmwareInfraPackRn_Type()
)
cfprFirmwareInfraPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackRn.setStatus("current")
_CfprFirmwareInfraPackDescr_Type = SnmpAdminString
_CfprFirmwareInfraPackDescr_Object = MibTableColumn
cfprFirmwareInfraPackDescr = _CfprFirmwareInfraPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 4),
    _CfprFirmwareInfraPackDescr_Type()
)
cfprFirmwareInfraPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackDescr.setStatus("current")
_CfprFirmwareInfraPackForceDeploy_Type = TruthValue
_CfprFirmwareInfraPackForceDeploy_Object = MibTableColumn
cfprFirmwareInfraPackForceDeploy = _CfprFirmwareInfraPackForceDeploy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 5),
    _CfprFirmwareInfraPackForceDeploy_Type()
)
cfprFirmwareInfraPackForceDeploy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackForceDeploy.setStatus("current")
_CfprFirmwareInfraPackInfraBundleName_Type = SnmpAdminString
_CfprFirmwareInfraPackInfraBundleName_Object = MibTableColumn
cfprFirmwareInfraPackInfraBundleName = _CfprFirmwareInfraPackInfraBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 6),
    _CfprFirmwareInfraPackInfraBundleName_Type()
)
cfprFirmwareInfraPackInfraBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackInfraBundleName.setStatus("current")
_CfprFirmwareInfraPackInfraBundleVersion_Type = SnmpAdminString
_CfprFirmwareInfraPackInfraBundleVersion_Object = MibTableColumn
cfprFirmwareInfraPackInfraBundleVersion = _CfprFirmwareInfraPackInfraBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 7),
    _CfprFirmwareInfraPackInfraBundleVersion_Type()
)
cfprFirmwareInfraPackInfraBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackInfraBundleVersion.setStatus("current")
_CfprFirmwareInfraPackIntId_Type = SnmpAdminString
_CfprFirmwareInfraPackIntId_Object = MibTableColumn
cfprFirmwareInfraPackIntId = _CfprFirmwareInfraPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 8),
    _CfprFirmwareInfraPackIntId_Type()
)
cfprFirmwareInfraPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackIntId.setStatus("current")
_CfprFirmwareInfraPackMode_Type = CfprFirmwarePackMode
_CfprFirmwareInfraPackMode_Object = MibTableColumn
cfprFirmwareInfraPackMode = _CfprFirmwareInfraPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 9),
    _CfprFirmwareInfraPackMode_Type()
)
cfprFirmwareInfraPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackMode.setStatus("current")
_CfprFirmwareInfraPackName_Type = SnmpAdminString
_CfprFirmwareInfraPackName_Object = MibTableColumn
cfprFirmwareInfraPackName = _CfprFirmwareInfraPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 10),
    _CfprFirmwareInfraPackName_Type()
)
cfprFirmwareInfraPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackName.setStatus("current")
_CfprFirmwareInfraPackPolicyLevel_Type = Gauge32
_CfprFirmwareInfraPackPolicyLevel_Object = MibTableColumn
cfprFirmwareInfraPackPolicyLevel = _CfprFirmwareInfraPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 11),
    _CfprFirmwareInfraPackPolicyLevel_Type()
)
cfprFirmwareInfraPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackPolicyLevel.setStatus("current")
_CfprFirmwareInfraPackPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwareInfraPackPolicyOwner_Object = MibTableColumn
cfprFirmwareInfraPackPolicyOwner = _CfprFirmwareInfraPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 12),
    _CfprFirmwareInfraPackPolicyOwner_Type()
)
cfprFirmwareInfraPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackPolicyOwner.setStatus("current")
_CfprFirmwareInfraPackStageSize_Type = Gauge32
_CfprFirmwareInfraPackStageSize_Object = MibTableColumn
cfprFirmwareInfraPackStageSize = _CfprFirmwareInfraPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 13),
    _CfprFirmwareInfraPackStageSize_Type()
)
cfprFirmwareInfraPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackStageSize.setStatus("current")
_CfprFirmwareInfraPackUpdateTrigger_Type = DateAndTime
_CfprFirmwareInfraPackUpdateTrigger_Object = MibTableColumn
cfprFirmwareInfraPackUpdateTrigger = _CfprFirmwareInfraPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 36, 1, 14),
    _CfprFirmwareInfraPackUpdateTrigger_Type()
)
cfprFirmwareInfraPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInfraPackUpdateTrigger.setStatus("current")
_CfprFirmwareInstallImpactTable_Object = MibTable
cfprFirmwareInstallImpactTable = _CfprFirmwareInstallImpactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 37)
)
if mibBuilder.loadTexts:
    cfprFirmwareInstallImpactTable.setStatus("current")
_CfprFirmwareInstallImpactEntry_Object = MibTableRow
cfprFirmwareInstallImpactEntry = _CfprFirmwareInstallImpactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 37, 1)
)
cfprFirmwareInstallImpactEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareInstallImpactInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareInstallImpactEntry.setStatus("current")
_CfprFirmwareInstallImpactInstanceId_Type = CfprManagedObjectId
_CfprFirmwareInstallImpactInstanceId_Object = MibTableColumn
cfprFirmwareInstallImpactInstanceId = _CfprFirmwareInstallImpactInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 37, 1, 1),
    _CfprFirmwareInstallImpactInstanceId_Type()
)
cfprFirmwareInstallImpactInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareInstallImpactInstanceId.setStatus("current")
_CfprFirmwareInstallImpactDn_Type = CfprManagedObjectDn
_CfprFirmwareInstallImpactDn_Object = MibTableColumn
cfprFirmwareInstallImpactDn = _CfprFirmwareInstallImpactDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 37, 1, 2),
    _CfprFirmwareInstallImpactDn_Type()
)
cfprFirmwareInstallImpactDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallImpactDn.setStatus("current")
_CfprFirmwareInstallImpactRn_Type = SnmpAdminString
_CfprFirmwareInstallImpactRn_Object = MibTableColumn
cfprFirmwareInstallImpactRn = _CfprFirmwareInstallImpactRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 37, 1, 3),
    _CfprFirmwareInstallImpactRn_Type()
)
cfprFirmwareInstallImpactRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallImpactRn.setStatus("current")
_CfprFirmwareInstallImpactDescr_Type = SnmpAdminString
_CfprFirmwareInstallImpactDescr_Object = MibTableColumn
cfprFirmwareInstallImpactDescr = _CfprFirmwareInstallImpactDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 37, 1, 4),
    _CfprFirmwareInstallImpactDescr_Type()
)
cfprFirmwareInstallImpactDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallImpactDescr.setStatus("current")
_CfprFirmwareInstallImpactKeyDn_Type = SnmpAdminString
_CfprFirmwareInstallImpactKeyDn_Object = MibTableColumn
cfprFirmwareInstallImpactKeyDn = _CfprFirmwareInstallImpactKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 37, 1, 5),
    _CfprFirmwareInstallImpactKeyDn_Type()
)
cfprFirmwareInstallImpactKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallImpactKeyDn.setStatus("current")
_CfprFirmwareInstallImpactMaintPolicyDn_Type = SnmpAdminString
_CfprFirmwareInstallImpactMaintPolicyDn_Object = MibTableColumn
cfprFirmwareInstallImpactMaintPolicyDn = _CfprFirmwareInstallImpactMaintPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 37, 1, 6),
    _CfprFirmwareInstallImpactMaintPolicyDn_Type()
)
cfprFirmwareInstallImpactMaintPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallImpactMaintPolicyDn.setStatus("current")
_CfprFirmwareInstallImpactRebootPolicy_Type = SnmpAdminString
_CfprFirmwareInstallImpactRebootPolicy_Object = MibTableColumn
cfprFirmwareInstallImpactRebootPolicy = _CfprFirmwareInstallImpactRebootPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 37, 1, 7),
    _CfprFirmwareInstallImpactRebootPolicy_Type()
)
cfprFirmwareInstallImpactRebootPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallImpactRebootPolicy.setStatus("current")
_CfprFirmwareInstallImpactSubject_Type = CfprFirmwareEquipmentType
_CfprFirmwareInstallImpactSubject_Object = MibTableColumn
cfprFirmwareInstallImpactSubject = _CfprFirmwareInstallImpactSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 37, 1, 8),
    _CfprFirmwareInstallImpactSubject_Type()
)
cfprFirmwareInstallImpactSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallImpactSubject.setStatus("current")
_CfprFirmwareInstallImpactType_Type = CfprFirmwareImpactType
_CfprFirmwareInstallImpactType_Object = MibTableColumn
cfprFirmwareInstallImpactType = _CfprFirmwareInstallImpactType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 37, 1, 9),
    _CfprFirmwareInstallImpactType_Type()
)
cfprFirmwareInstallImpactType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallImpactType.setStatus("current")
_CfprFirmwareInstallableTable_Object = MibTable
cfprFirmwareInstallableTable = _CfprFirmwareInstallableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38)
)
if mibBuilder.loadTexts:
    cfprFirmwareInstallableTable.setStatus("current")
_CfprFirmwareInstallableEntry_Object = MibTableRow
cfprFirmwareInstallableEntry = _CfprFirmwareInstallableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1)
)
cfprFirmwareInstallableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareInstallableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareInstallableEntry.setStatus("current")
_CfprFirmwareInstallableInstanceId_Type = CfprManagedObjectId
_CfprFirmwareInstallableInstanceId_Object = MibTableColumn
cfprFirmwareInstallableInstanceId = _CfprFirmwareInstallableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 1),
    _CfprFirmwareInstallableInstanceId_Type()
)
cfprFirmwareInstallableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableInstanceId.setStatus("current")
_CfprFirmwareInstallableDn_Type = CfprManagedObjectDn
_CfprFirmwareInstallableDn_Object = MibTableColumn
cfprFirmwareInstallableDn = _CfprFirmwareInstallableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 2),
    _CfprFirmwareInstallableDn_Type()
)
cfprFirmwareInstallableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableDn.setStatus("current")
_CfprFirmwareInstallableRn_Type = SnmpAdminString
_CfprFirmwareInstallableRn_Object = MibTableColumn
cfprFirmwareInstallableRn = _CfprFirmwareInstallableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 3),
    _CfprFirmwareInstallableRn_Type()
)
cfprFirmwareInstallableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableRn.setStatus("current")
_CfprFirmwareInstallableChecksum_Type = SnmpAdminString
_CfprFirmwareInstallableChecksum_Object = MibTableColumn
cfprFirmwareInstallableChecksum = _CfprFirmwareInstallableChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 4),
    _CfprFirmwareInstallableChecksum_Type()
)
cfprFirmwareInstallableChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableChecksum.setStatus("current")
_CfprFirmwareInstallableInProgress_Type = Gauge32
_CfprFirmwareInstallableInProgress_Object = MibTableColumn
cfprFirmwareInstallableInProgress = _CfprFirmwareInstallableInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 5),
    _CfprFirmwareInstallableInProgress_Type()
)
cfprFirmwareInstallableInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableInProgress.setStatus("current")
_CfprFirmwareInstallableIsoname_Type = SnmpAdminString
_CfprFirmwareInstallableIsoname_Object = MibTableColumn
cfprFirmwareInstallableIsoname = _CfprFirmwareInstallableIsoname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 6),
    _CfprFirmwareInstallableIsoname_Type()
)
cfprFirmwareInstallableIsoname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableIsoname.setStatus("current")
_CfprFirmwareInstallableLocation_Type = SnmpAdminString
_CfprFirmwareInstallableLocation_Object = MibTableColumn
cfprFirmwareInstallableLocation = _CfprFirmwareInstallableLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 7),
    _CfprFirmwareInstallableLocation_Type()
)
cfprFirmwareInstallableLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableLocation.setStatus("current")
_CfprFirmwareInstallableModel_Type = SnmpAdminString
_CfprFirmwareInstallableModel_Object = MibTableColumn
cfprFirmwareInstallableModel = _CfprFirmwareInstallableModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 8),
    _CfprFirmwareInstallableModel_Type()
)
cfprFirmwareInstallableModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableModel.setStatus("current")
_CfprFirmwareInstallableName_Type = SnmpAdminString
_CfprFirmwareInstallableName_Object = MibTableColumn
cfprFirmwareInstallableName = _CfprFirmwareInstallableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 9),
    _CfprFirmwareInstallableName_Type()
)
cfprFirmwareInstallableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableName.setStatus("current")
_CfprFirmwareInstallableSize_Type = Unsigned64
_CfprFirmwareInstallableSize_Object = MibTableColumn
cfprFirmwareInstallableSize = _CfprFirmwareInstallableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 10),
    _CfprFirmwareInstallableSize_Type()
)
cfprFirmwareInstallableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableSize.setStatus("current")
_CfprFirmwareInstallableType_Type = CfprFirmwareType
_CfprFirmwareInstallableType_Object = MibTableColumn
cfprFirmwareInstallableType = _CfprFirmwareInstallableType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 11),
    _CfprFirmwareInstallableType_Type()
)
cfprFirmwareInstallableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableType.setStatus("current")
_CfprFirmwareInstallableVendor_Type = SnmpAdminString
_CfprFirmwareInstallableVendor_Object = MibTableColumn
cfprFirmwareInstallableVendor = _CfprFirmwareInstallableVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 12),
    _CfprFirmwareInstallableVendor_Type()
)
cfprFirmwareInstallableVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableVendor.setStatus("current")
_CfprFirmwareInstallableVersion_Type = SnmpAdminString
_CfprFirmwareInstallableVersion_Object = MibTableColumn
cfprFirmwareInstallableVersion = _CfprFirmwareInstallableVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 38, 1, 13),
    _CfprFirmwareInstallableVersion_Type()
)
cfprFirmwareInstallableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareInstallableVersion.setStatus("current")
_CfprFirmwarePackItemTable_Object = MibTable
cfprFirmwarePackItemTable = _CfprFirmwarePackItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 39)
)
if mibBuilder.loadTexts:
    cfprFirmwarePackItemTable.setStatus("current")
_CfprFirmwarePackItemEntry_Object = MibTableRow
cfprFirmwarePackItemEntry = _CfprFirmwarePackItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 39, 1)
)
cfprFirmwarePackItemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwarePackItemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwarePackItemEntry.setStatus("current")
_CfprFirmwarePackItemInstanceId_Type = CfprManagedObjectId
_CfprFirmwarePackItemInstanceId_Object = MibTableColumn
cfprFirmwarePackItemInstanceId = _CfprFirmwarePackItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 39, 1, 1),
    _CfprFirmwarePackItemInstanceId_Type()
)
cfprFirmwarePackItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwarePackItemInstanceId.setStatus("current")
_CfprFirmwarePackItemDn_Type = CfprManagedObjectDn
_CfprFirmwarePackItemDn_Object = MibTableColumn
cfprFirmwarePackItemDn = _CfprFirmwarePackItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 39, 1, 2),
    _CfprFirmwarePackItemDn_Type()
)
cfprFirmwarePackItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePackItemDn.setStatus("current")
_CfprFirmwarePackItemRn_Type = SnmpAdminString
_CfprFirmwarePackItemRn_Object = MibTableColumn
cfprFirmwarePackItemRn = _CfprFirmwarePackItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 39, 1, 3),
    _CfprFirmwarePackItemRn_Type()
)
cfprFirmwarePackItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePackItemRn.setStatus("current")
_CfprFirmwarePackItemHwModel_Type = SnmpAdminString
_CfprFirmwarePackItemHwModel_Object = MibTableColumn
cfprFirmwarePackItemHwModel = _CfprFirmwarePackItemHwModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 39, 1, 4),
    _CfprFirmwarePackItemHwModel_Type()
)
cfprFirmwarePackItemHwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePackItemHwModel.setStatus("current")
_CfprFirmwarePackItemHwVendor_Type = SnmpAdminString
_CfprFirmwarePackItemHwVendor_Object = MibTableColumn
cfprFirmwarePackItemHwVendor = _CfprFirmwarePackItemHwVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 39, 1, 5),
    _CfprFirmwarePackItemHwVendor_Type()
)
cfprFirmwarePackItemHwVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePackItemHwVendor.setStatus("current")
_CfprFirmwarePackItemPresence_Type = CfprFirmwarePackItemPresence
_CfprFirmwarePackItemPresence_Object = MibTableColumn
cfprFirmwarePackItemPresence = _CfprFirmwarePackItemPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 39, 1, 6),
    _CfprFirmwarePackItemPresence_Type()
)
cfprFirmwarePackItemPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePackItemPresence.setStatus("current")
_CfprFirmwarePackItemType_Type = CfprFirmwareItemType
_CfprFirmwarePackItemType_Object = MibTableColumn
cfprFirmwarePackItemType = _CfprFirmwarePackItemType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 39, 1, 7),
    _CfprFirmwarePackItemType_Type()
)
cfprFirmwarePackItemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePackItemType.setStatus("current")
_CfprFirmwarePackItemVersion_Type = SnmpAdminString
_CfprFirmwarePackItemVersion_Object = MibTableColumn
cfprFirmwarePackItemVersion = _CfprFirmwarePackItemVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 39, 1, 8),
    _CfprFirmwarePackItemVersion_Type()
)
cfprFirmwarePackItemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePackItemVersion.setStatus("current")
_CfprFirmwarePlatformTable_Object = MibTable
cfprFirmwarePlatformTable = _CfprFirmwarePlatformTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40)
)
if mibBuilder.loadTexts:
    cfprFirmwarePlatformTable.setStatus("current")
_CfprFirmwarePlatformEntry_Object = MibTableRow
cfprFirmwarePlatformEntry = _CfprFirmwarePlatformEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1)
)
cfprFirmwarePlatformEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwarePlatformInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwarePlatformEntry.setStatus("current")
_CfprFirmwarePlatformInstanceId_Type = CfprManagedObjectId
_CfprFirmwarePlatformInstanceId_Object = MibTableColumn
cfprFirmwarePlatformInstanceId = _CfprFirmwarePlatformInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 1),
    _CfprFirmwarePlatformInstanceId_Type()
)
cfprFirmwarePlatformInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformInstanceId.setStatus("current")
_CfprFirmwarePlatformDn_Type = CfprManagedObjectDn
_CfprFirmwarePlatformDn_Object = MibTableColumn
cfprFirmwarePlatformDn = _CfprFirmwarePlatformDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 2),
    _CfprFirmwarePlatformDn_Type()
)
cfprFirmwarePlatformDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformDn.setStatus("current")
_CfprFirmwarePlatformRn_Type = SnmpAdminString
_CfprFirmwarePlatformRn_Object = MibTableColumn
cfprFirmwarePlatformRn = _CfprFirmwarePlatformRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 3),
    _CfprFirmwarePlatformRn_Type()
)
cfprFirmwarePlatformRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformRn.setStatus("current")
_CfprFirmwarePlatformAdminState_Type = CfprTrigAdminState
_CfprFirmwarePlatformAdminState_Object = MibTableColumn
cfprFirmwarePlatformAdminState = _CfprFirmwarePlatformAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 4),
    _CfprFirmwarePlatformAdminState_Type()
)
cfprFirmwarePlatformAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformAdminState.setStatus("current")
_CfprFirmwarePlatformAutoDelete_Type = TruthValue
_CfprFirmwarePlatformAutoDelete_Object = MibTableColumn
cfprFirmwarePlatformAutoDelete = _CfprFirmwarePlatformAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 5),
    _CfprFirmwarePlatformAutoDelete_Type()
)
cfprFirmwarePlatformAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformAutoDelete.setStatus("current")
_CfprFirmwarePlatformDescr_Type = SnmpAdminString
_CfprFirmwarePlatformDescr_Object = MibTableColumn
cfprFirmwarePlatformDescr = _CfprFirmwarePlatformDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 6),
    _CfprFirmwarePlatformDescr_Type()
)
cfprFirmwarePlatformDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformDescr.setStatus("current")
_CfprFirmwarePlatformIgnoreCap_Type = TruthValue
_CfprFirmwarePlatformIgnoreCap_Object = MibTableColumn
cfprFirmwarePlatformIgnoreCap = _CfprFirmwarePlatformIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 7),
    _CfprFirmwarePlatformIgnoreCap_Type()
)
cfprFirmwarePlatformIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformIgnoreCap.setStatus("current")
_CfprFirmwarePlatformIntId_Type = SnmpAdminString
_CfprFirmwarePlatformIntId_Object = MibTableColumn
cfprFirmwarePlatformIntId = _CfprFirmwarePlatformIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 8),
    _CfprFirmwarePlatformIntId_Type()
)
cfprFirmwarePlatformIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformIntId.setStatus("current")
_CfprFirmwarePlatformName_Type = SnmpAdminString
_CfprFirmwarePlatformName_Object = MibTableColumn
cfprFirmwarePlatformName = _CfprFirmwarePlatformName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 9),
    _CfprFirmwarePlatformName_Type()
)
cfprFirmwarePlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformName.setStatus("current")
_CfprFirmwarePlatformOperScheduler_Type = SnmpAdminString
_CfprFirmwarePlatformOperScheduler_Object = MibTableColumn
cfprFirmwarePlatformOperScheduler = _CfprFirmwarePlatformOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 10),
    _CfprFirmwarePlatformOperScheduler_Type()
)
cfprFirmwarePlatformOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformOperScheduler.setStatus("current")
_CfprFirmwarePlatformOperState_Type = CfprTrigTrigOperState
_CfprFirmwarePlatformOperState_Object = MibTableColumn
cfprFirmwarePlatformOperState = _CfprFirmwarePlatformOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 11),
    _CfprFirmwarePlatformOperState_Type()
)
cfprFirmwarePlatformOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformOperState.setStatus("current")
_CfprFirmwarePlatformOperVersion_Type = SnmpAdminString
_CfprFirmwarePlatformOperVersion_Object = MibTableColumn
cfprFirmwarePlatformOperVersion = _CfprFirmwarePlatformOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 12),
    _CfprFirmwarePlatformOperVersion_Type()
)
cfprFirmwarePlatformOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformOperVersion.setStatus("current")
_CfprFirmwarePlatformPolicyLevel_Type = Gauge32
_CfprFirmwarePlatformPolicyLevel_Object = MibTableColumn
cfprFirmwarePlatformPolicyLevel = _CfprFirmwarePlatformPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 13),
    _CfprFirmwarePlatformPolicyLevel_Type()
)
cfprFirmwarePlatformPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPolicyLevel.setStatus("current")
_CfprFirmwarePlatformPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwarePlatformPolicyOwner_Object = MibTableColumn
cfprFirmwarePlatformPolicyOwner = _CfprFirmwarePlatformPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 14),
    _CfprFirmwarePlatformPolicyOwner_Type()
)
cfprFirmwarePlatformPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPolicyOwner.setStatus("current")
_CfprFirmwarePlatformScheduler_Type = SnmpAdminString
_CfprFirmwarePlatformScheduler_Object = MibTableColumn
cfprFirmwarePlatformScheduler = _CfprFirmwarePlatformScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 40, 1, 15),
    _CfprFirmwarePlatformScheduler_Type()
)
cfprFirmwarePlatformScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformScheduler.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderTable_Object = MibTable
cfprFirmwarePlatformBundleTypeCapProviderTable = _CfprFirmwarePlatformBundleTypeCapProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41)
)
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderTable.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderEntry_Object = MibTableRow
cfprFirmwarePlatformBundleTypeCapProviderEntry = _CfprFirmwarePlatformBundleTypeCapProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1)
)
cfprFirmwarePlatformBundleTypeCapProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwarePlatformBundleTypeCapProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderEntry.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderInstanceId_Type = CfprManagedObjectId
_CfprFirmwarePlatformBundleTypeCapProviderInstanceId_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderInstanceId = _CfprFirmwarePlatformBundleTypeCapProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 1),
    _CfprFirmwarePlatformBundleTypeCapProviderInstanceId_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderInstanceId.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderDn_Type = CfprManagedObjectDn
_CfprFirmwarePlatformBundleTypeCapProviderDn_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderDn = _CfprFirmwarePlatformBundleTypeCapProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 2),
    _CfprFirmwarePlatformBundleTypeCapProviderDn_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderDn.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderRn_Type = SnmpAdminString
_CfprFirmwarePlatformBundleTypeCapProviderRn_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderRn = _CfprFirmwarePlatformBundleTypeCapProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 3),
    _CfprFirmwarePlatformBundleTypeCapProviderRn_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderRn.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderDeleted_Type = TruthValue
_CfprFirmwarePlatformBundleTypeCapProviderDeleted_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderDeleted = _CfprFirmwarePlatformBundleTypeCapProviderDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 4),
    _CfprFirmwarePlatformBundleTypeCapProviderDeleted_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderDeleted.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderDeprecated_Type = TruthValue
_CfprFirmwarePlatformBundleTypeCapProviderDeprecated_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderDeprecated = _CfprFirmwarePlatformBundleTypeCapProviderDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 5),
    _CfprFirmwarePlatformBundleTypeCapProviderDeprecated_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderDeprecated.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderElementLoadFailures_Type = Gauge32
_CfprFirmwarePlatformBundleTypeCapProviderElementLoadFailures_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderElementLoadFailures = _CfprFirmwarePlatformBundleTypeCapProviderElementLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 6),
    _CfprFirmwarePlatformBundleTypeCapProviderElementLoadFailures_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderElementLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderElementLoadFailures.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderElementsLoaded_Type = Gauge32
_CfprFirmwarePlatformBundleTypeCapProviderElementsLoaded_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderElementsLoaded = _CfprFirmwarePlatformBundleTypeCapProviderElementsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 7),
    _CfprFirmwarePlatformBundleTypeCapProviderElementsLoaded_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderElementsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderElementsLoaded.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderGencount_Type = Gauge32
_CfprFirmwarePlatformBundleTypeCapProviderGencount_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderGencount = _CfprFirmwarePlatformBundleTypeCapProviderGencount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 8),
    _CfprFirmwarePlatformBundleTypeCapProviderGencount_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderGencount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderGencount.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderLoadErrors_Type = Gauge32
_CfprFirmwarePlatformBundleTypeCapProviderLoadErrors_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderLoadErrors = _CfprFirmwarePlatformBundleTypeCapProviderLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 9),
    _CfprFirmwarePlatformBundleTypeCapProviderLoadErrors_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderLoadErrors.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderLoadWarnings_Type = Gauge32
_CfprFirmwarePlatformBundleTypeCapProviderLoadWarnings_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderLoadWarnings = _CfprFirmwarePlatformBundleTypeCapProviderLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 10),
    _CfprFirmwarePlatformBundleTypeCapProviderLoadWarnings_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderLoadWarnings.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer_Type = SnmpAdminString
_CfprFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer = _CfprFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 11),
    _CfprFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderModel_Type = SnmpAdminString
_CfprFirmwarePlatformBundleTypeCapProviderModel_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderModel = _CfprFirmwarePlatformBundleTypeCapProviderModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 12),
    _CfprFirmwarePlatformBundleTypeCapProviderModel_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderModel.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderPlatformType_Type = CfprFirmwarePlatformType
_CfprFirmwarePlatformBundleTypeCapProviderPlatformType_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderPlatformType = _CfprFirmwarePlatformBundleTypeCapProviderPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 13),
    _CfprFirmwarePlatformBundleTypeCapProviderPlatformType_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderPlatformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderPlatformType.setStatus("current")
_CfprFirmwarePlatformBundleTypeCapProviderVendor_Type = SnmpAdminString
_CfprFirmwarePlatformBundleTypeCapProviderVendor_Object = MibTableColumn
cfprFirmwarePlatformBundleTypeCapProviderVendor = _CfprFirmwarePlatformBundleTypeCapProviderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 41, 1, 14),
    _CfprFirmwarePlatformBundleTypeCapProviderVendor_Type()
)
cfprFirmwarePlatformBundleTypeCapProviderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformBundleTypeCapProviderVendor.setStatus("current")
_CfprFirmwarePlatformPackTable_Object = MibTable
cfprFirmwarePlatformPackTable = _CfprFirmwarePlatformPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42)
)
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackTable.setStatus("current")
_CfprFirmwarePlatformPackEntry_Object = MibTableRow
cfprFirmwarePlatformPackEntry = _CfprFirmwarePlatformPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1)
)
cfprFirmwarePlatformPackEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwarePlatformPackInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackEntry.setStatus("current")
_CfprFirmwarePlatformPackInstanceId_Type = CfprManagedObjectId
_CfprFirmwarePlatformPackInstanceId_Object = MibTableColumn
cfprFirmwarePlatformPackInstanceId = _CfprFirmwarePlatformPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 1),
    _CfprFirmwarePlatformPackInstanceId_Type()
)
cfprFirmwarePlatformPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackInstanceId.setStatus("current")
_CfprFirmwarePlatformPackDn_Type = CfprManagedObjectDn
_CfprFirmwarePlatformPackDn_Object = MibTableColumn
cfprFirmwarePlatformPackDn = _CfprFirmwarePlatformPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 2),
    _CfprFirmwarePlatformPackDn_Type()
)
cfprFirmwarePlatformPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackDn.setStatus("current")
_CfprFirmwarePlatformPackRn_Type = SnmpAdminString
_CfprFirmwarePlatformPackRn_Object = MibTableColumn
cfprFirmwarePlatformPackRn = _CfprFirmwarePlatformPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 3),
    _CfprFirmwarePlatformPackRn_Type()
)
cfprFirmwarePlatformPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackRn.setStatus("current")
_CfprFirmwarePlatformPackDescr_Type = SnmpAdminString
_CfprFirmwarePlatformPackDescr_Object = MibTableColumn
cfprFirmwarePlatformPackDescr = _CfprFirmwarePlatformPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 4),
    _CfprFirmwarePlatformPackDescr_Type()
)
cfprFirmwarePlatformPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackDescr.setStatus("current")
_CfprFirmwarePlatformPackForceDeploy_Type = TruthValue
_CfprFirmwarePlatformPackForceDeploy_Object = MibTableColumn
cfprFirmwarePlatformPackForceDeploy = _CfprFirmwarePlatformPackForceDeploy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 5),
    _CfprFirmwarePlatformPackForceDeploy_Type()
)
cfprFirmwarePlatformPackForceDeploy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackForceDeploy.setStatus("current")
_CfprFirmwarePlatformPackFsmDescr_Type = SnmpAdminString
_CfprFirmwarePlatformPackFsmDescr_Object = MibTableColumn
cfprFirmwarePlatformPackFsmDescr = _CfprFirmwarePlatformPackFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 6),
    _CfprFirmwarePlatformPackFsmDescr_Type()
)
cfprFirmwarePlatformPackFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmDescr.setStatus("current")
_CfprFirmwarePlatformPackFsmFlags_Type = SnmpAdminString
_CfprFirmwarePlatformPackFsmFlags_Object = MibTableColumn
cfprFirmwarePlatformPackFsmFlags = _CfprFirmwarePlatformPackFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 7),
    _CfprFirmwarePlatformPackFsmFlags_Type()
)
cfprFirmwarePlatformPackFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmFlags.setStatus("current")
_CfprFirmwarePlatformPackFsmPrev_Type = SnmpAdminString
_CfprFirmwarePlatformPackFsmPrev_Object = MibTableColumn
cfprFirmwarePlatformPackFsmPrev = _CfprFirmwarePlatformPackFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 8),
    _CfprFirmwarePlatformPackFsmPrev_Type()
)
cfprFirmwarePlatformPackFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmPrev.setStatus("current")
_CfprFirmwarePlatformPackFsmProgr_Type = Gauge32
_CfprFirmwarePlatformPackFsmProgr_Object = MibTableColumn
cfprFirmwarePlatformPackFsmProgr = _CfprFirmwarePlatformPackFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 9),
    _CfprFirmwarePlatformPackFsmProgr_Type()
)
cfprFirmwarePlatformPackFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmProgr.setStatus("current")
_CfprFirmwarePlatformPackFsmRmtInvErrCode_Type = Gauge32
_CfprFirmwarePlatformPackFsmRmtInvErrCode_Object = MibTableColumn
cfprFirmwarePlatformPackFsmRmtInvErrCode = _CfprFirmwarePlatformPackFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 10),
    _CfprFirmwarePlatformPackFsmRmtInvErrCode_Type()
)
cfprFirmwarePlatformPackFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmRmtInvErrCode.setStatus("current")
_CfprFirmwarePlatformPackFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprFirmwarePlatformPackFsmRmtInvErrDescr_Object = MibTableColumn
cfprFirmwarePlatformPackFsmRmtInvErrDescr = _CfprFirmwarePlatformPackFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 11),
    _CfprFirmwarePlatformPackFsmRmtInvErrDescr_Type()
)
cfprFirmwarePlatformPackFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmRmtInvErrDescr.setStatus("current")
_CfprFirmwarePlatformPackFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwarePlatformPackFsmRmtInvRslt_Object = MibTableColumn
cfprFirmwarePlatformPackFsmRmtInvRslt = _CfprFirmwarePlatformPackFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 12),
    _CfprFirmwarePlatformPackFsmRmtInvRslt_Type()
)
cfprFirmwarePlatformPackFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmRmtInvRslt.setStatus("current")
_CfprFirmwarePlatformPackFsmStageDescr_Type = SnmpAdminString
_CfprFirmwarePlatformPackFsmStageDescr_Object = MibTableColumn
cfprFirmwarePlatformPackFsmStageDescr = _CfprFirmwarePlatformPackFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 13),
    _CfprFirmwarePlatformPackFsmStageDescr_Type()
)
cfprFirmwarePlatformPackFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStageDescr.setStatus("current")
_CfprFirmwarePlatformPackFsmStamp_Type = DateAndTime
_CfprFirmwarePlatformPackFsmStamp_Object = MibTableColumn
cfprFirmwarePlatformPackFsmStamp = _CfprFirmwarePlatformPackFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 14),
    _CfprFirmwarePlatformPackFsmStamp_Type()
)
cfprFirmwarePlatformPackFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStamp.setStatus("current")
_CfprFirmwarePlatformPackFsmStatus_Type = SnmpAdminString
_CfprFirmwarePlatformPackFsmStatus_Object = MibTableColumn
cfprFirmwarePlatformPackFsmStatus = _CfprFirmwarePlatformPackFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 15),
    _CfprFirmwarePlatformPackFsmStatus_Type()
)
cfprFirmwarePlatformPackFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStatus.setStatus("current")
_CfprFirmwarePlatformPackFsmTry_Type = Gauge32
_CfprFirmwarePlatformPackFsmTry_Object = MibTableColumn
cfprFirmwarePlatformPackFsmTry = _CfprFirmwarePlatformPackFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 16),
    _CfprFirmwarePlatformPackFsmTry_Type()
)
cfprFirmwarePlatformPackFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmTry.setStatus("current")
_CfprFirmwarePlatformPackIntId_Type = SnmpAdminString
_CfprFirmwarePlatformPackIntId_Object = MibTableColumn
cfprFirmwarePlatformPackIntId = _CfprFirmwarePlatformPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 17),
    _CfprFirmwarePlatformPackIntId_Type()
)
cfprFirmwarePlatformPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackIntId.setStatus("current")
_CfprFirmwarePlatformPackMode_Type = CfprFirmwarePackMode
_CfprFirmwarePlatformPackMode_Object = MibTableColumn
cfprFirmwarePlatformPackMode = _CfprFirmwarePlatformPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 18),
    _CfprFirmwarePlatformPackMode_Type()
)
cfprFirmwarePlatformPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackMode.setStatus("current")
_CfprFirmwarePlatformPackName_Type = SnmpAdminString
_CfprFirmwarePlatformPackName_Object = MibTableColumn
cfprFirmwarePlatformPackName = _CfprFirmwarePlatformPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 19),
    _CfprFirmwarePlatformPackName_Type()
)
cfprFirmwarePlatformPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackName.setStatus("current")
_CfprFirmwarePlatformPackPlatformBundleName_Type = SnmpAdminString
_CfprFirmwarePlatformPackPlatformBundleName_Object = MibTableColumn
cfprFirmwarePlatformPackPlatformBundleName = _CfprFirmwarePlatformPackPlatformBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 20),
    _CfprFirmwarePlatformPackPlatformBundleName_Type()
)
cfprFirmwarePlatformPackPlatformBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackPlatformBundleName.setStatus("current")
_CfprFirmwarePlatformPackPlatformBundleVersion_Type = SnmpAdminString
_CfprFirmwarePlatformPackPlatformBundleVersion_Object = MibTableColumn
cfprFirmwarePlatformPackPlatformBundleVersion = _CfprFirmwarePlatformPackPlatformBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 21),
    _CfprFirmwarePlatformPackPlatformBundleVersion_Type()
)
cfprFirmwarePlatformPackPlatformBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackPlatformBundleVersion.setStatus("current")
_CfprFirmwarePlatformPackPolicyLevel_Type = Gauge32
_CfprFirmwarePlatformPackPolicyLevel_Object = MibTableColumn
cfprFirmwarePlatformPackPolicyLevel = _CfprFirmwarePlatformPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 22),
    _CfprFirmwarePlatformPackPolicyLevel_Type()
)
cfprFirmwarePlatformPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackPolicyLevel.setStatus("current")
_CfprFirmwarePlatformPackPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFirmwarePlatformPackPolicyOwner_Object = MibTableColumn
cfprFirmwarePlatformPackPolicyOwner = _CfprFirmwarePlatformPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 23),
    _CfprFirmwarePlatformPackPolicyOwner_Type()
)
cfprFirmwarePlatformPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackPolicyOwner.setStatus("current")
_CfprFirmwarePlatformPackPreviousBundleVersion_Type = SnmpAdminString
_CfprFirmwarePlatformPackPreviousBundleVersion_Object = MibTableColumn
cfprFirmwarePlatformPackPreviousBundleVersion = _CfprFirmwarePlatformPackPreviousBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 24),
    _CfprFirmwarePlatformPackPreviousBundleVersion_Type()
)
cfprFirmwarePlatformPackPreviousBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackPreviousBundleVersion.setStatus("current")
_CfprFirmwarePlatformPackRestoreVersion_Type = TruthValue
_CfprFirmwarePlatformPackRestoreVersion_Object = MibTableColumn
cfprFirmwarePlatformPackRestoreVersion = _CfprFirmwarePlatformPackRestoreVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 25),
    _CfprFirmwarePlatformPackRestoreVersion_Type()
)
cfprFirmwarePlatformPackRestoreVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackRestoreVersion.setStatus("current")
_CfprFirmwarePlatformPackSerializeHostUpgrade_Type = TruthValue
_CfprFirmwarePlatformPackSerializeHostUpgrade_Object = MibTableColumn
cfprFirmwarePlatformPackSerializeHostUpgrade = _CfprFirmwarePlatformPackSerializeHostUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 26),
    _CfprFirmwarePlatformPackSerializeHostUpgrade_Type()
)
cfprFirmwarePlatformPackSerializeHostUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackSerializeHostUpgrade.setStatus("current")
_CfprFirmwarePlatformPackSkipManagerValidation_Type = TruthValue
_CfprFirmwarePlatformPackSkipManagerValidation_Object = MibTableColumn
cfprFirmwarePlatformPackSkipManagerValidation = _CfprFirmwarePlatformPackSkipManagerValidation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 27),
    _CfprFirmwarePlatformPackSkipManagerValidation_Type()
)
cfprFirmwarePlatformPackSkipManagerValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackSkipManagerValidation.setStatus("current")
_CfprFirmwarePlatformPackStageSize_Type = Gauge32
_CfprFirmwarePlatformPackStageSize_Object = MibTableColumn
cfprFirmwarePlatformPackStageSize = _CfprFirmwarePlatformPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 28),
    _CfprFirmwarePlatformPackStageSize_Type()
)
cfprFirmwarePlatformPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackStageSize.setStatus("current")
_CfprFirmwarePlatformPackUpdateTrigger_Type = DateAndTime
_CfprFirmwarePlatformPackUpdateTrigger_Object = MibTableColumn
cfprFirmwarePlatformPackUpdateTrigger = _CfprFirmwarePlatformPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 29),
    _CfprFirmwarePlatformPackUpdateTrigger_Type()
)
cfprFirmwarePlatformPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackUpdateTrigger.setStatus("current")
_CfprFirmwarePlatformPackPrevBundleVersion_Type = SnmpAdminString
_CfprFirmwarePlatformPackPrevBundleVersion_Object = MibTableColumn
cfprFirmwarePlatformPackPrevBundleVersion = _CfprFirmwarePlatformPackPrevBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 30),
    _CfprFirmwarePlatformPackPrevBundleVersion_Type()
)
cfprFirmwarePlatformPackPrevBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackPrevBundleVersion.setStatus("current")
_CfprFirmwarePlatformPackVersionChecked_Type = TruthValue
_CfprFirmwarePlatformPackVersionChecked_Object = MibTableColumn
cfprFirmwarePlatformPackVersionChecked = _CfprFirmwarePlatformPackVersionChecked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 42, 1, 31),
    _CfprFirmwarePlatformPackVersionChecked_Type()
)
cfprFirmwarePlatformPackVersionChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackVersionChecked.setStatus("current")
_CfprFirmwarePlatformPackFsmTable_Object = MibTable
cfprFirmwarePlatformPackFsmTable = _CfprFirmwarePlatformPackFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43)
)
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmTable.setStatus("current")
_CfprFirmwarePlatformPackFsmEntry_Object = MibTableRow
cfprFirmwarePlatformPackFsmEntry = _CfprFirmwarePlatformPackFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43, 1)
)
cfprFirmwarePlatformPackFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwarePlatformPackFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmEntry.setStatus("current")
_CfprFirmwarePlatformPackFsmInstanceId_Type = CfprManagedObjectId
_CfprFirmwarePlatformPackFsmInstanceId_Object = MibTableColumn
cfprFirmwarePlatformPackFsmInstanceId = _CfprFirmwarePlatformPackFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43, 1, 1),
    _CfprFirmwarePlatformPackFsmInstanceId_Type()
)
cfprFirmwarePlatformPackFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmInstanceId.setStatus("current")
_CfprFirmwarePlatformPackFsmDn_Type = CfprManagedObjectDn
_CfprFirmwarePlatformPackFsmDn_Object = MibTableColumn
cfprFirmwarePlatformPackFsmDn = _CfprFirmwarePlatformPackFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43, 1, 2),
    _CfprFirmwarePlatformPackFsmDn_Type()
)
cfprFirmwarePlatformPackFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmDn.setStatus("current")
_CfprFirmwarePlatformPackFsmRn_Type = SnmpAdminString
_CfprFirmwarePlatformPackFsmRn_Object = MibTableColumn
cfprFirmwarePlatformPackFsmRn = _CfprFirmwarePlatformPackFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43, 1, 3),
    _CfprFirmwarePlatformPackFsmRn_Type()
)
cfprFirmwarePlatformPackFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmRn.setStatus("current")
_CfprFirmwarePlatformPackFsmCompletionTime_Type = DateAndTime
_CfprFirmwarePlatformPackFsmCompletionTime_Object = MibTableColumn
cfprFirmwarePlatformPackFsmCompletionTime = _CfprFirmwarePlatformPackFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43, 1, 4),
    _CfprFirmwarePlatformPackFsmCompletionTime_Type()
)
cfprFirmwarePlatformPackFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmCompletionTime.setStatus("current")
_CfprFirmwarePlatformPackFsmCurrentFsm_Type = CfprFirmwarePlatformPackFsmCurrentFsm
_CfprFirmwarePlatformPackFsmCurrentFsm_Object = MibTableColumn
cfprFirmwarePlatformPackFsmCurrentFsm = _CfprFirmwarePlatformPackFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43, 1, 5),
    _CfprFirmwarePlatformPackFsmCurrentFsm_Type()
)
cfprFirmwarePlatformPackFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmCurrentFsm.setStatus("current")
_CfprFirmwarePlatformPackFsmDescrData_Type = SnmpAdminString
_CfprFirmwarePlatformPackFsmDescrData_Object = MibTableColumn
cfprFirmwarePlatformPackFsmDescrData = _CfprFirmwarePlatformPackFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43, 1, 6),
    _CfprFirmwarePlatformPackFsmDescrData_Type()
)
cfprFirmwarePlatformPackFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmDescrData.setStatus("current")
_CfprFirmwarePlatformPackFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwarePlatformPackFsmFsmStatus_Object = MibTableColumn
cfprFirmwarePlatformPackFsmFsmStatus = _CfprFirmwarePlatformPackFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43, 1, 7),
    _CfprFirmwarePlatformPackFsmFsmStatus_Type()
)
cfprFirmwarePlatformPackFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmFsmStatus.setStatus("current")
_CfprFirmwarePlatformPackFsmProgress_Type = Gauge32
_CfprFirmwarePlatformPackFsmProgress_Object = MibTableColumn
cfprFirmwarePlatformPackFsmProgress = _CfprFirmwarePlatformPackFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43, 1, 8),
    _CfprFirmwarePlatformPackFsmProgress_Type()
)
cfprFirmwarePlatformPackFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmProgress.setStatus("current")
_CfprFirmwarePlatformPackFsmRmtErrCode_Type = Gauge32
_CfprFirmwarePlatformPackFsmRmtErrCode_Object = MibTableColumn
cfprFirmwarePlatformPackFsmRmtErrCode = _CfprFirmwarePlatformPackFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43, 1, 9),
    _CfprFirmwarePlatformPackFsmRmtErrCode_Type()
)
cfprFirmwarePlatformPackFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmRmtErrCode.setStatus("current")
_CfprFirmwarePlatformPackFsmRmtErrDescr_Type = SnmpAdminString
_CfprFirmwarePlatformPackFsmRmtErrDescr_Object = MibTableColumn
cfprFirmwarePlatformPackFsmRmtErrDescr = _CfprFirmwarePlatformPackFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43, 1, 10),
    _CfprFirmwarePlatformPackFsmRmtErrDescr_Type()
)
cfprFirmwarePlatformPackFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmRmtErrDescr.setStatus("current")
_CfprFirmwarePlatformPackFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwarePlatformPackFsmRmtRslt_Object = MibTableColumn
cfprFirmwarePlatformPackFsmRmtRslt = _CfprFirmwarePlatformPackFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 43, 1, 11),
    _CfprFirmwarePlatformPackFsmRmtRslt_Type()
)
cfprFirmwarePlatformPackFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmRmtRslt.setStatus("current")
_CfprFirmwarePlatformPackFsmStageTable_Object = MibTable
cfprFirmwarePlatformPackFsmStageTable = _CfprFirmwarePlatformPackFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 44)
)
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStageTable.setStatus("current")
_CfprFirmwarePlatformPackFsmStageEntry_Object = MibTableRow
cfprFirmwarePlatformPackFsmStageEntry = _CfprFirmwarePlatformPackFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 44, 1)
)
cfprFirmwarePlatformPackFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwarePlatformPackFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStageEntry.setStatus("current")
_CfprFirmwarePlatformPackFsmStageInstanceId_Type = CfprManagedObjectId
_CfprFirmwarePlatformPackFsmStageInstanceId_Object = MibTableColumn
cfprFirmwarePlatformPackFsmStageInstanceId = _CfprFirmwarePlatformPackFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 44, 1, 1),
    _CfprFirmwarePlatformPackFsmStageInstanceId_Type()
)
cfprFirmwarePlatformPackFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStageInstanceId.setStatus("current")
_CfprFirmwarePlatformPackFsmStageDn_Type = CfprManagedObjectDn
_CfprFirmwarePlatformPackFsmStageDn_Object = MibTableColumn
cfprFirmwarePlatformPackFsmStageDn = _CfprFirmwarePlatformPackFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 44, 1, 2),
    _CfprFirmwarePlatformPackFsmStageDn_Type()
)
cfprFirmwarePlatformPackFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStageDn.setStatus("current")
_CfprFirmwarePlatformPackFsmStageRn_Type = SnmpAdminString
_CfprFirmwarePlatformPackFsmStageRn_Object = MibTableColumn
cfprFirmwarePlatformPackFsmStageRn = _CfprFirmwarePlatformPackFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 44, 1, 3),
    _CfprFirmwarePlatformPackFsmStageRn_Type()
)
cfprFirmwarePlatformPackFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStageRn.setStatus("current")
_CfprFirmwarePlatformPackFsmStageDescrData_Type = SnmpAdminString
_CfprFirmwarePlatformPackFsmStageDescrData_Object = MibTableColumn
cfprFirmwarePlatformPackFsmStageDescrData = _CfprFirmwarePlatformPackFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 44, 1, 4),
    _CfprFirmwarePlatformPackFsmStageDescrData_Type()
)
cfprFirmwarePlatformPackFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStageDescrData.setStatus("current")
_CfprFirmwarePlatformPackFsmStageLastUpdateTime_Type = DateAndTime
_CfprFirmwarePlatformPackFsmStageLastUpdateTime_Object = MibTableColumn
cfprFirmwarePlatformPackFsmStageLastUpdateTime = _CfprFirmwarePlatformPackFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 44, 1, 5),
    _CfprFirmwarePlatformPackFsmStageLastUpdateTime_Type()
)
cfprFirmwarePlatformPackFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStageLastUpdateTime.setStatus("current")
_CfprFirmwarePlatformPackFsmStageName_Type = CfprFirmwarePlatformPackFsmStageName
_CfprFirmwarePlatformPackFsmStageName_Object = MibTableColumn
cfprFirmwarePlatformPackFsmStageName = _CfprFirmwarePlatformPackFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 44, 1, 6),
    _CfprFirmwarePlatformPackFsmStageName_Type()
)
cfprFirmwarePlatformPackFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStageName.setStatus("current")
_CfprFirmwarePlatformPackFsmStageOrder_Type = Gauge32
_CfprFirmwarePlatformPackFsmStageOrder_Object = MibTableColumn
cfprFirmwarePlatformPackFsmStageOrder = _CfprFirmwarePlatformPackFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 44, 1, 7),
    _CfprFirmwarePlatformPackFsmStageOrder_Type()
)
cfprFirmwarePlatformPackFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStageOrder.setStatus("current")
_CfprFirmwarePlatformPackFsmStageRetry_Type = Gauge32
_CfprFirmwarePlatformPackFsmStageRetry_Object = MibTableColumn
cfprFirmwarePlatformPackFsmStageRetry = _CfprFirmwarePlatformPackFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 44, 1, 8),
    _CfprFirmwarePlatformPackFsmStageRetry_Type()
)
cfprFirmwarePlatformPackFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStageRetry.setStatus("current")
_CfprFirmwarePlatformPackFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwarePlatformPackFsmStageStageStatus_Object = MibTableColumn
cfprFirmwarePlatformPackFsmStageStageStatus = _CfprFirmwarePlatformPackFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 44, 1, 9),
    _CfprFirmwarePlatformPackFsmStageStageStatus_Type()
)
cfprFirmwarePlatformPackFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmStageStageStatus.setStatus("current")
_CfprFirmwarePlatformPackFsmTaskTable_Object = MibTable
cfprFirmwarePlatformPackFsmTaskTable = _CfprFirmwarePlatformPackFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 45)
)
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmTaskTable.setStatus("current")
_CfprFirmwarePlatformPackFsmTaskEntry_Object = MibTableRow
cfprFirmwarePlatformPackFsmTaskEntry = _CfprFirmwarePlatformPackFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 45, 1)
)
cfprFirmwarePlatformPackFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwarePlatformPackFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmTaskEntry.setStatus("current")
_CfprFirmwarePlatformPackFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprFirmwarePlatformPackFsmTaskInstanceId_Object = MibTableColumn
cfprFirmwarePlatformPackFsmTaskInstanceId = _CfprFirmwarePlatformPackFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 45, 1, 1),
    _CfprFirmwarePlatformPackFsmTaskInstanceId_Type()
)
cfprFirmwarePlatformPackFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmTaskInstanceId.setStatus("current")
_CfprFirmwarePlatformPackFsmTaskDn_Type = CfprManagedObjectDn
_CfprFirmwarePlatformPackFsmTaskDn_Object = MibTableColumn
cfprFirmwarePlatformPackFsmTaskDn = _CfprFirmwarePlatformPackFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 45, 1, 2),
    _CfprFirmwarePlatformPackFsmTaskDn_Type()
)
cfprFirmwarePlatformPackFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmTaskDn.setStatus("current")
_CfprFirmwarePlatformPackFsmTaskRn_Type = SnmpAdminString
_CfprFirmwarePlatformPackFsmTaskRn_Object = MibTableColumn
cfprFirmwarePlatformPackFsmTaskRn = _CfprFirmwarePlatformPackFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 45, 1, 3),
    _CfprFirmwarePlatformPackFsmTaskRn_Type()
)
cfprFirmwarePlatformPackFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmTaskRn.setStatus("current")
_CfprFirmwarePlatformPackFsmTaskCompletion_Type = CfprFsmCompletion
_CfprFirmwarePlatformPackFsmTaskCompletion_Object = MibTableColumn
cfprFirmwarePlatformPackFsmTaskCompletion = _CfprFirmwarePlatformPackFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 45, 1, 4),
    _CfprFirmwarePlatformPackFsmTaskCompletion_Type()
)
cfprFirmwarePlatformPackFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmTaskCompletion.setStatus("current")
_CfprFirmwarePlatformPackFsmTaskFlags_Type = CfprFirmwarePlatformPackFsmTaskFlags
_CfprFirmwarePlatformPackFsmTaskFlags_Object = MibTableColumn
cfprFirmwarePlatformPackFsmTaskFlags = _CfprFirmwarePlatformPackFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 45, 1, 5),
    _CfprFirmwarePlatformPackFsmTaskFlags_Type()
)
cfprFirmwarePlatformPackFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmTaskFlags.setStatus("current")
_CfprFirmwarePlatformPackFsmTaskItem_Type = CfprFirmwarePlatformPackFsmTaskItem
_CfprFirmwarePlatformPackFsmTaskItem_Object = MibTableColumn
cfprFirmwarePlatformPackFsmTaskItem = _CfprFirmwarePlatformPackFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 45, 1, 6),
    _CfprFirmwarePlatformPackFsmTaskItem_Type()
)
cfprFirmwarePlatformPackFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmTaskItem.setStatus("current")
_CfprFirmwarePlatformPackFsmTaskSeqId_Type = Gauge32
_CfprFirmwarePlatformPackFsmTaskSeqId_Object = MibTableColumn
cfprFirmwarePlatformPackFsmTaskSeqId = _CfprFirmwarePlatformPackFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 45, 1, 7),
    _CfprFirmwarePlatformPackFsmTaskSeqId_Type()
)
cfprFirmwarePlatformPackFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwarePlatformPackFsmTaskSeqId.setStatus("current")
_CfprFirmwareRackTable_Object = MibTable
cfprFirmwareRackTable = _CfprFirmwareRackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 46)
)
if mibBuilder.loadTexts:
    cfprFirmwareRackTable.setStatus("current")
_CfprFirmwareRackEntry_Object = MibTableRow
cfprFirmwareRackEntry = _CfprFirmwareRackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 46, 1)
)
cfprFirmwareRackEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareRackInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareRackEntry.setStatus("current")
_CfprFirmwareRackInstanceId_Type = CfprManagedObjectId
_CfprFirmwareRackInstanceId_Object = MibTableColumn
cfprFirmwareRackInstanceId = _CfprFirmwareRackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 46, 1, 1),
    _CfprFirmwareRackInstanceId_Type()
)
cfprFirmwareRackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareRackInstanceId.setStatus("current")
_CfprFirmwareRackDn_Type = CfprManagedObjectDn
_CfprFirmwareRackDn_Object = MibTableColumn
cfprFirmwareRackDn = _CfprFirmwareRackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 46, 1, 2),
    _CfprFirmwareRackDn_Type()
)
cfprFirmwareRackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRackDn.setStatus("current")
_CfprFirmwareRackRn_Type = SnmpAdminString
_CfprFirmwareRackRn_Object = MibTableColumn
cfprFirmwareRackRn = _CfprFirmwareRackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 46, 1, 3),
    _CfprFirmwareRackRn_Type()
)
cfprFirmwareRackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRackRn.setStatus("current")
_CfprFirmwareRackOperVersion_Type = SnmpAdminString
_CfprFirmwareRackOperVersion_Object = MibTableColumn
cfprFirmwareRackOperVersion = _CfprFirmwareRackOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 46, 1, 4),
    _CfprFirmwareRackOperVersion_Type()
)
cfprFirmwareRackOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRackOperVersion.setStatus("current")
_CfprFirmwareRunningTable_Object = MibTable
cfprFirmwareRunningTable = _CfprFirmwareRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 47)
)
if mibBuilder.loadTexts:
    cfprFirmwareRunningTable.setStatus("current")
_CfprFirmwareRunningEntry_Object = MibTableRow
cfprFirmwareRunningEntry = _CfprFirmwareRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 47, 1)
)
cfprFirmwareRunningEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareRunningInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareRunningEntry.setStatus("current")
_CfprFirmwareRunningInstanceId_Type = CfprManagedObjectId
_CfprFirmwareRunningInstanceId_Object = MibTableColumn
cfprFirmwareRunningInstanceId = _CfprFirmwareRunningInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 47, 1, 1),
    _CfprFirmwareRunningInstanceId_Type()
)
cfprFirmwareRunningInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareRunningInstanceId.setStatus("current")
_CfprFirmwareRunningDn_Type = CfprManagedObjectDn
_CfprFirmwareRunningDn_Object = MibTableColumn
cfprFirmwareRunningDn = _CfprFirmwareRunningDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 47, 1, 2),
    _CfprFirmwareRunningDn_Type()
)
cfprFirmwareRunningDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunningDn.setStatus("current")
_CfprFirmwareRunningRn_Type = SnmpAdminString
_CfprFirmwareRunningRn_Object = MibTableColumn
cfprFirmwareRunningRn = _CfprFirmwareRunningRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 47, 1, 3),
    _CfprFirmwareRunningRn_Type()
)
cfprFirmwareRunningRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunningRn.setStatus("current")
_CfprFirmwareRunningDeployment_Type = CfprFirmwareRunningDeployment
_CfprFirmwareRunningDeployment_Object = MibTableColumn
cfprFirmwareRunningDeployment = _CfprFirmwareRunningDeployment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 47, 1, 4),
    _CfprFirmwareRunningDeployment_Type()
)
cfprFirmwareRunningDeployment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunningDeployment.setStatus("current")
_CfprFirmwareRunningInvTag_Type = SnmpAdminString
_CfprFirmwareRunningInvTag_Object = MibTableColumn
cfprFirmwareRunningInvTag = _CfprFirmwareRunningInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 47, 1, 5),
    _CfprFirmwareRunningInvTag_Type()
)
cfprFirmwareRunningInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunningInvTag.setStatus("current")
_CfprFirmwareRunningPackageVersion_Type = SnmpAdminString
_CfprFirmwareRunningPackageVersion_Object = MibTableColumn
cfprFirmwareRunningPackageVersion = _CfprFirmwareRunningPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 47, 1, 6),
    _CfprFirmwareRunningPackageVersion_Type()
)
cfprFirmwareRunningPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunningPackageVersion.setStatus("current")
_CfprFirmwareRunningType_Type = CfprFirmwareType
_CfprFirmwareRunningType_Object = MibTableColumn
cfprFirmwareRunningType = _CfprFirmwareRunningType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 47, 1, 7),
    _CfprFirmwareRunningType_Type()
)
cfprFirmwareRunningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunningType.setStatus("current")
_CfprFirmwareRunningVersion_Type = SnmpAdminString
_CfprFirmwareRunningVersion_Object = MibTableColumn
cfprFirmwareRunningVersion = _CfprFirmwareRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 47, 1, 8),
    _CfprFirmwareRunningVersion_Type()
)
cfprFirmwareRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunningVersion.setStatus("current")
_CfprFirmwareRunningMioSsdmodel_Type = SnmpAdminString
_CfprFirmwareRunningMioSsdmodel_Object = MibTableColumn
cfprFirmwareRunningMioSsdmodel = _CfprFirmwareRunningMioSsdmodel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 47, 1, 9),
    _CfprFirmwareRunningMioSsdmodel_Type()
)
cfprFirmwareRunningMioSsdmodel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunningMioSsdmodel.setStatus("current")
_CfprFirmwareSpecTable_Object = MibTable
cfprFirmwareSpecTable = _CfprFirmwareSpecTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 48)
)
if mibBuilder.loadTexts:
    cfprFirmwareSpecTable.setStatus("current")
_CfprFirmwareSpecEntry_Object = MibTableRow
cfprFirmwareSpecEntry = _CfprFirmwareSpecEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 48, 1)
)
cfprFirmwareSpecEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareSpecInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareSpecEntry.setStatus("current")
_CfprFirmwareSpecInstanceId_Type = CfprManagedObjectId
_CfprFirmwareSpecInstanceId_Object = MibTableColumn
cfprFirmwareSpecInstanceId = _CfprFirmwareSpecInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 48, 1, 1),
    _CfprFirmwareSpecInstanceId_Type()
)
cfprFirmwareSpecInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareSpecInstanceId.setStatus("current")
_CfprFirmwareSpecDn_Type = CfprManagedObjectDn
_CfprFirmwareSpecDn_Object = MibTableColumn
cfprFirmwareSpecDn = _CfprFirmwareSpecDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 48, 1, 2),
    _CfprFirmwareSpecDn_Type()
)
cfprFirmwareSpecDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSpecDn.setStatus("current")
_CfprFirmwareSpecRn_Type = SnmpAdminString
_CfprFirmwareSpecRn_Object = MibTableColumn
cfprFirmwareSpecRn = _CfprFirmwareSpecRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 48, 1, 3),
    _CfprFirmwareSpecRn_Type()
)
cfprFirmwareSpecRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSpecRn.setStatus("current")
_CfprFirmwareSpecBundleVersion_Type = SnmpAdminString
_CfprFirmwareSpecBundleVersion_Object = MibTableColumn
cfprFirmwareSpecBundleVersion = _CfprFirmwareSpecBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 48, 1, 4),
    _CfprFirmwareSpecBundleVersion_Type()
)
cfprFirmwareSpecBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSpecBundleVersion.setStatus("current")
_CfprFirmwareSpecEthEFIVersion_Type = SnmpAdminString
_CfprFirmwareSpecEthEFIVersion_Object = MibTableColumn
cfprFirmwareSpecEthEFIVersion = _CfprFirmwareSpecEthEFIVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 48, 1, 5),
    _CfprFirmwareSpecEthEFIVersion_Type()
)
cfprFirmwareSpecEthEFIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSpecEthEFIVersion.setStatus("current")
_CfprFirmwareSpecEthOptionRomVersion_Type = SnmpAdminString
_CfprFirmwareSpecEthOptionRomVersion_Object = MibTableColumn
cfprFirmwareSpecEthOptionRomVersion = _CfprFirmwareSpecEthOptionRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 48, 1, 6),
    _CfprFirmwareSpecEthOptionRomVersion_Type()
)
cfprFirmwareSpecEthOptionRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSpecEthOptionRomVersion.setStatus("current")
_CfprFirmwareSpecFcFWVersion_Type = SnmpAdminString
_CfprFirmwareSpecFcFWVersion_Object = MibTableColumn
cfprFirmwareSpecFcFWVersion = _CfprFirmwareSpecFcFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 48, 1, 7),
    _CfprFirmwareSpecFcFWVersion_Type()
)
cfprFirmwareSpecFcFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSpecFcFWVersion.setStatus("current")
_CfprFirmwareSpecFcOptionRomVersion_Type = SnmpAdminString
_CfprFirmwareSpecFcOptionRomVersion_Object = MibTableColumn
cfprFirmwareSpecFcOptionRomVersion = _CfprFirmwareSpecFcOptionRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 48, 1, 8),
    _CfprFirmwareSpecFcOptionRomVersion_Type()
)
cfprFirmwareSpecFcOptionRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSpecFcOptionRomVersion.setStatus("current")
_CfprFirmwareStatusTable_Object = MibTable
cfprFirmwareStatusTable = _CfprFirmwareStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 49)
)
if mibBuilder.loadTexts:
    cfprFirmwareStatusTable.setStatus("current")
_CfprFirmwareStatusEntry_Object = MibTableRow
cfprFirmwareStatusEntry = _CfprFirmwareStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 49, 1)
)
cfprFirmwareStatusEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareStatusEntry.setStatus("current")
_CfprFirmwareStatusInstanceId_Type = CfprManagedObjectId
_CfprFirmwareStatusInstanceId_Object = MibTableColumn
cfprFirmwareStatusInstanceId = _CfprFirmwareStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 49, 1, 1),
    _CfprFirmwareStatusInstanceId_Type()
)
cfprFirmwareStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareStatusInstanceId.setStatus("current")
_CfprFirmwareStatusDn_Type = CfprManagedObjectDn
_CfprFirmwareStatusDn_Object = MibTableColumn
cfprFirmwareStatusDn = _CfprFirmwareStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 49, 1, 2),
    _CfprFirmwareStatusDn_Type()
)
cfprFirmwareStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareStatusDn.setStatus("current")
_CfprFirmwareStatusRn_Type = SnmpAdminString
_CfprFirmwareStatusRn_Object = MibTableColumn
cfprFirmwareStatusRn = _CfprFirmwareStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 49, 1, 3),
    _CfprFirmwareStatusRn_Type()
)
cfprFirmwareStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareStatusRn.setStatus("current")
_CfprFirmwareStatusCimcVersion_Type = SnmpAdminString
_CfprFirmwareStatusCimcVersion_Object = MibTableColumn
cfprFirmwareStatusCimcVersion = _CfprFirmwareStatusCimcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 49, 1, 4),
    _CfprFirmwareStatusCimcVersion_Type()
)
cfprFirmwareStatusCimcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareStatusCimcVersion.setStatus("current")
_CfprFirmwareStatusFirmwareState_Type = CfprFirmwareFirmwareState
_CfprFirmwareStatusFirmwareState_Object = MibTableColumn
cfprFirmwareStatusFirmwareState = _CfprFirmwareStatusFirmwareState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 49, 1, 5),
    _CfprFirmwareStatusFirmwareState_Type()
)
cfprFirmwareStatusFirmwareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareStatusFirmwareState.setStatus("current")
_CfprFirmwareStatusOperState_Type = CfprFirmwareImageState
_CfprFirmwareStatusOperState_Object = MibTableColumn
cfprFirmwareStatusOperState = _CfprFirmwareStatusOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 49, 1, 6),
    _CfprFirmwareStatusOperState_Type()
)
cfprFirmwareStatusOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareStatusOperState.setStatus("current")
_CfprFirmwareStatusPackageVersion_Type = SnmpAdminString
_CfprFirmwareStatusPackageVersion_Object = MibTableColumn
cfprFirmwareStatusPackageVersion = _CfprFirmwareStatusPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 49, 1, 7),
    _CfprFirmwareStatusPackageVersion_Type()
)
cfprFirmwareStatusPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareStatusPackageVersion.setStatus("current")
_CfprFirmwareStatusPldVersion_Type = SnmpAdminString
_CfprFirmwareStatusPldVersion_Object = MibTableColumn
cfprFirmwareStatusPldVersion = _CfprFirmwareStatusPldVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 49, 1, 8),
    _CfprFirmwareStatusPldVersion_Type()
)
cfprFirmwareStatusPldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareStatusPldVersion.setStatus("current")
_CfprFirmwareSystemTable_Object = MibTable
cfprFirmwareSystemTable = _CfprFirmwareSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50)
)
if mibBuilder.loadTexts:
    cfprFirmwareSystemTable.setStatus("current")
_CfprFirmwareSystemEntry_Object = MibTableRow
cfprFirmwareSystemEntry = _CfprFirmwareSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1)
)
cfprFirmwareSystemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareSystemEntry.setStatus("current")
_CfprFirmwareSystemInstanceId_Type = CfprManagedObjectId
_CfprFirmwareSystemInstanceId_Object = MibTableColumn
cfprFirmwareSystemInstanceId = _CfprFirmwareSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 1),
    _CfprFirmwareSystemInstanceId_Type()
)
cfprFirmwareSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareSystemInstanceId.setStatus("current")
_CfprFirmwareSystemDn_Type = CfprManagedObjectDn
_CfprFirmwareSystemDn_Object = MibTableColumn
cfprFirmwareSystemDn = _CfprFirmwareSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 2),
    _CfprFirmwareSystemDn_Type()
)
cfprFirmwareSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemDn.setStatus("current")
_CfprFirmwareSystemRn_Type = SnmpAdminString
_CfprFirmwareSystemRn_Object = MibTableColumn
cfprFirmwareSystemRn = _CfprFirmwareSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 3),
    _CfprFirmwareSystemRn_Type()
)
cfprFirmwareSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemRn.setStatus("current")
_CfprFirmwareSystemFsmDescr_Type = SnmpAdminString
_CfprFirmwareSystemFsmDescr_Object = MibTableColumn
cfprFirmwareSystemFsmDescr = _CfprFirmwareSystemFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 4),
    _CfprFirmwareSystemFsmDescr_Type()
)
cfprFirmwareSystemFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmDescr.setStatus("current")
_CfprFirmwareSystemFsmFlags_Type = SnmpAdminString
_CfprFirmwareSystemFsmFlags_Object = MibTableColumn
cfprFirmwareSystemFsmFlags = _CfprFirmwareSystemFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 5),
    _CfprFirmwareSystemFsmFlags_Type()
)
cfprFirmwareSystemFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmFlags.setStatus("current")
_CfprFirmwareSystemFsmPrev_Type = SnmpAdminString
_CfprFirmwareSystemFsmPrev_Object = MibTableColumn
cfprFirmwareSystemFsmPrev = _CfprFirmwareSystemFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 6),
    _CfprFirmwareSystemFsmPrev_Type()
)
cfprFirmwareSystemFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmPrev.setStatus("current")
_CfprFirmwareSystemFsmProgr_Type = Gauge32
_CfprFirmwareSystemFsmProgr_Object = MibTableColumn
cfprFirmwareSystemFsmProgr = _CfprFirmwareSystemFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 7),
    _CfprFirmwareSystemFsmProgr_Type()
)
cfprFirmwareSystemFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmProgr.setStatus("current")
_CfprFirmwareSystemFsmRmtInvErrCode_Type = Gauge32
_CfprFirmwareSystemFsmRmtInvErrCode_Object = MibTableColumn
cfprFirmwareSystemFsmRmtInvErrCode = _CfprFirmwareSystemFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 8),
    _CfprFirmwareSystemFsmRmtInvErrCode_Type()
)
cfprFirmwareSystemFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmRmtInvErrCode.setStatus("current")
_CfprFirmwareSystemFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprFirmwareSystemFsmRmtInvErrDescr_Object = MibTableColumn
cfprFirmwareSystemFsmRmtInvErrDescr = _CfprFirmwareSystemFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 9),
    _CfprFirmwareSystemFsmRmtInvErrDescr_Type()
)
cfprFirmwareSystemFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmRmtInvErrDescr.setStatus("current")
_CfprFirmwareSystemFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwareSystemFsmRmtInvRslt_Object = MibTableColumn
cfprFirmwareSystemFsmRmtInvRslt = _CfprFirmwareSystemFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 10),
    _CfprFirmwareSystemFsmRmtInvRslt_Type()
)
cfprFirmwareSystemFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmRmtInvRslt.setStatus("current")
_CfprFirmwareSystemFsmStageDescr_Type = SnmpAdminString
_CfprFirmwareSystemFsmStageDescr_Object = MibTableColumn
cfprFirmwareSystemFsmStageDescr = _CfprFirmwareSystemFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 11),
    _CfprFirmwareSystemFsmStageDescr_Type()
)
cfprFirmwareSystemFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStageDescr.setStatus("current")
_CfprFirmwareSystemFsmStamp_Type = DateAndTime
_CfprFirmwareSystemFsmStamp_Object = MibTableColumn
cfprFirmwareSystemFsmStamp = _CfprFirmwareSystemFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 12),
    _CfprFirmwareSystemFsmStamp_Type()
)
cfprFirmwareSystemFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStamp.setStatus("current")
_CfprFirmwareSystemFsmStatus_Type = SnmpAdminString
_CfprFirmwareSystemFsmStatus_Object = MibTableColumn
cfprFirmwareSystemFsmStatus = _CfprFirmwareSystemFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 13),
    _CfprFirmwareSystemFsmStatus_Type()
)
cfprFirmwareSystemFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStatus.setStatus("current")
_CfprFirmwareSystemFsmTry_Type = Gauge32
_CfprFirmwareSystemFsmTry_Object = MibTableColumn
cfprFirmwareSystemFsmTry = _CfprFirmwareSystemFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 14),
    _CfprFirmwareSystemFsmTry_Type()
)
cfprFirmwareSystemFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmTry.setStatus("current")
_CfprFirmwareSystemOperState_Type = CfprFirmwareInstallState
_CfprFirmwareSystemOperState_Object = MibTableColumn
cfprFirmwareSystemOperState = _CfprFirmwareSystemOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 15),
    _CfprFirmwareSystemOperState_Type()
)
cfprFirmwareSystemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemOperState.setStatus("current")
_CfprFirmwareSystemState_Type = CfprFirmwareFwState
_CfprFirmwareSystemState_Object = MibTableColumn
cfprFirmwareSystemState = _CfprFirmwareSystemState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 16),
    _CfprFirmwareSystemState_Type()
)
cfprFirmwareSystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemState.setStatus("current")
_CfprFirmwareSystemResetOnUpgrade_Type = TruthValue
_CfprFirmwareSystemResetOnUpgrade_Object = MibTableColumn
cfprFirmwareSystemResetOnUpgrade = _CfprFirmwareSystemResetOnUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 17),
    _CfprFirmwareSystemResetOnUpgrade_Type()
)
cfprFirmwareSystemResetOnUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemResetOnUpgrade.setStatus("current")
_CfprFirmwareSystemScheduledInstallTime_Type = DateAndTime
_CfprFirmwareSystemScheduledInstallTime_Object = MibTableColumn
cfprFirmwareSystemScheduledInstallTime = _CfprFirmwareSystemScheduledInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 18),
    _CfprFirmwareSystemScheduledInstallTime_Type()
)
cfprFirmwareSystemScheduledInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemScheduledInstallTime.setStatus("current")
_CfprFirmwareSystemValidationStatus_Type = CfprFirmwareVerifyPackStatus
_CfprFirmwareSystemValidationStatus_Object = MibTableColumn
cfprFirmwareSystemValidationStatus = _CfprFirmwareSystemValidationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 50, 1, 19),
    _CfprFirmwareSystemValidationStatus_Type()
)
cfprFirmwareSystemValidationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemValidationStatus.setStatus("current")
_CfprFirmwareSystemCompCheckResultTable_Object = MibTable
cfprFirmwareSystemCompCheckResultTable = _CfprFirmwareSystemCompCheckResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 51)
)
if mibBuilder.loadTexts:
    cfprFirmwareSystemCompCheckResultTable.setStatus("current")
_CfprFirmwareSystemCompCheckResultEntry_Object = MibTableRow
cfprFirmwareSystemCompCheckResultEntry = _CfprFirmwareSystemCompCheckResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 51, 1)
)
cfprFirmwareSystemCompCheckResultEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareSystemCompCheckResultInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareSystemCompCheckResultEntry.setStatus("current")
_CfprFirmwareSystemCompCheckResultInstanceId_Type = CfprManagedObjectId
_CfprFirmwareSystemCompCheckResultInstanceId_Object = MibTableColumn
cfprFirmwareSystemCompCheckResultInstanceId = _CfprFirmwareSystemCompCheckResultInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 51, 1, 1),
    _CfprFirmwareSystemCompCheckResultInstanceId_Type()
)
cfprFirmwareSystemCompCheckResultInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareSystemCompCheckResultInstanceId.setStatus("current")
_CfprFirmwareSystemCompCheckResultDn_Type = CfprManagedObjectDn
_CfprFirmwareSystemCompCheckResultDn_Object = MibTableColumn
cfprFirmwareSystemCompCheckResultDn = _CfprFirmwareSystemCompCheckResultDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 51, 1, 2),
    _CfprFirmwareSystemCompCheckResultDn_Type()
)
cfprFirmwareSystemCompCheckResultDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemCompCheckResultDn.setStatus("current")
_CfprFirmwareSystemCompCheckResultRn_Type = SnmpAdminString
_CfprFirmwareSystemCompCheckResultRn_Object = MibTableColumn
cfprFirmwareSystemCompCheckResultRn = _CfprFirmwareSystemCompCheckResultRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 51, 1, 3),
    _CfprFirmwareSystemCompCheckResultRn_Type()
)
cfprFirmwareSystemCompCheckResultRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemCompCheckResultRn.setStatus("current")
_CfprFirmwareSystemCompCheckResultKeyDescr_Type = SnmpAdminString
_CfprFirmwareSystemCompCheckResultKeyDescr_Object = MibTableColumn
cfprFirmwareSystemCompCheckResultKeyDescr = _CfprFirmwareSystemCompCheckResultKeyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 51, 1, 4),
    _CfprFirmwareSystemCompCheckResultKeyDescr_Type()
)
cfprFirmwareSystemCompCheckResultKeyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemCompCheckResultKeyDescr.setStatus("current")
_CfprFirmwareSystemCompCheckResultKeyDn_Type = SnmpAdminString
_CfprFirmwareSystemCompCheckResultKeyDn_Object = MibTableColumn
cfprFirmwareSystemCompCheckResultKeyDn = _CfprFirmwareSystemCompCheckResultKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 51, 1, 5),
    _CfprFirmwareSystemCompCheckResultKeyDn_Type()
)
cfprFirmwareSystemCompCheckResultKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemCompCheckResultKeyDn.setStatus("current")
_CfprFirmwareSystemCompCheckResultNonCompDescr_Type = SnmpAdminString
_CfprFirmwareSystemCompCheckResultNonCompDescr_Object = MibTableColumn
cfprFirmwareSystemCompCheckResultNonCompDescr = _CfprFirmwareSystemCompCheckResultNonCompDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 51, 1, 6),
    _CfprFirmwareSystemCompCheckResultNonCompDescr_Type()
)
cfprFirmwareSystemCompCheckResultNonCompDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemCompCheckResultNonCompDescr.setStatus("current")
_CfprFirmwareSystemCompCheckResultNonCompDns_Type = SnmpAdminString
_CfprFirmwareSystemCompCheckResultNonCompDns_Object = MibTableColumn
cfprFirmwareSystemCompCheckResultNonCompDns = _CfprFirmwareSystemCompCheckResultNonCompDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 51, 1, 7),
    _CfprFirmwareSystemCompCheckResultNonCompDns_Type()
)
cfprFirmwareSystemCompCheckResultNonCompDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemCompCheckResultNonCompDns.setStatus("current")
_CfprFirmwareSystemCompCheckResultSubject_Type = CfprFirmwareEquipmentType
_CfprFirmwareSystemCompCheckResultSubject_Object = MibTableColumn
cfprFirmwareSystemCompCheckResultSubject = _CfprFirmwareSystemCompCheckResultSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 51, 1, 8),
    _CfprFirmwareSystemCompCheckResultSubject_Type()
)
cfprFirmwareSystemCompCheckResultSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemCompCheckResultSubject.setStatus("current")
_CfprFirmwareSystemFsmTable_Object = MibTable
cfprFirmwareSystemFsmTable = _CfprFirmwareSystemFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52)
)
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmTable.setStatus("current")
_CfprFirmwareSystemFsmEntry_Object = MibTableRow
cfprFirmwareSystemFsmEntry = _CfprFirmwareSystemFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52, 1)
)
cfprFirmwareSystemFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareSystemFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmEntry.setStatus("current")
_CfprFirmwareSystemFsmInstanceId_Type = CfprManagedObjectId
_CfprFirmwareSystemFsmInstanceId_Object = MibTableColumn
cfprFirmwareSystemFsmInstanceId = _CfprFirmwareSystemFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52, 1, 1),
    _CfprFirmwareSystemFsmInstanceId_Type()
)
cfprFirmwareSystemFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmInstanceId.setStatus("current")
_CfprFirmwareSystemFsmDn_Type = CfprManagedObjectDn
_CfprFirmwareSystemFsmDn_Object = MibTableColumn
cfprFirmwareSystemFsmDn = _CfprFirmwareSystemFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52, 1, 2),
    _CfprFirmwareSystemFsmDn_Type()
)
cfprFirmwareSystemFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmDn.setStatus("current")
_CfprFirmwareSystemFsmRn_Type = SnmpAdminString
_CfprFirmwareSystemFsmRn_Object = MibTableColumn
cfprFirmwareSystemFsmRn = _CfprFirmwareSystemFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52, 1, 3),
    _CfprFirmwareSystemFsmRn_Type()
)
cfprFirmwareSystemFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmRn.setStatus("current")
_CfprFirmwareSystemFsmCompletionTime_Type = DateAndTime
_CfprFirmwareSystemFsmCompletionTime_Object = MibTableColumn
cfprFirmwareSystemFsmCompletionTime = _CfprFirmwareSystemFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52, 1, 4),
    _CfprFirmwareSystemFsmCompletionTime_Type()
)
cfprFirmwareSystemFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmCompletionTime.setStatus("current")
_CfprFirmwareSystemFsmCurrentFsm_Type = CfprFirmwareSystemFsmCurrentFsm
_CfprFirmwareSystemFsmCurrentFsm_Object = MibTableColumn
cfprFirmwareSystemFsmCurrentFsm = _CfprFirmwareSystemFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52, 1, 5),
    _CfprFirmwareSystemFsmCurrentFsm_Type()
)
cfprFirmwareSystemFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmCurrentFsm.setStatus("current")
_CfprFirmwareSystemFsmDescrData_Type = SnmpAdminString
_CfprFirmwareSystemFsmDescrData_Object = MibTableColumn
cfprFirmwareSystemFsmDescrData = _CfprFirmwareSystemFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52, 1, 6),
    _CfprFirmwareSystemFsmDescrData_Type()
)
cfprFirmwareSystemFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmDescrData.setStatus("current")
_CfprFirmwareSystemFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwareSystemFsmFsmStatus_Object = MibTableColumn
cfprFirmwareSystemFsmFsmStatus = _CfprFirmwareSystemFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52, 1, 7),
    _CfprFirmwareSystemFsmFsmStatus_Type()
)
cfprFirmwareSystemFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmFsmStatus.setStatus("current")
_CfprFirmwareSystemFsmProgress_Type = Gauge32
_CfprFirmwareSystemFsmProgress_Object = MibTableColumn
cfprFirmwareSystemFsmProgress = _CfprFirmwareSystemFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52, 1, 8),
    _CfprFirmwareSystemFsmProgress_Type()
)
cfprFirmwareSystemFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmProgress.setStatus("current")
_CfprFirmwareSystemFsmRmtErrCode_Type = Gauge32
_CfprFirmwareSystemFsmRmtErrCode_Object = MibTableColumn
cfprFirmwareSystemFsmRmtErrCode = _CfprFirmwareSystemFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52, 1, 9),
    _CfprFirmwareSystemFsmRmtErrCode_Type()
)
cfprFirmwareSystemFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmRmtErrCode.setStatus("current")
_CfprFirmwareSystemFsmRmtErrDescr_Type = SnmpAdminString
_CfprFirmwareSystemFsmRmtErrDescr_Object = MibTableColumn
cfprFirmwareSystemFsmRmtErrDescr = _CfprFirmwareSystemFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52, 1, 10),
    _CfprFirmwareSystemFsmRmtErrDescr_Type()
)
cfprFirmwareSystemFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmRmtErrDescr.setStatus("current")
_CfprFirmwareSystemFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwareSystemFsmRmtRslt_Object = MibTableColumn
cfprFirmwareSystemFsmRmtRslt = _CfprFirmwareSystemFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 52, 1, 11),
    _CfprFirmwareSystemFsmRmtRslt_Type()
)
cfprFirmwareSystemFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmRmtRslt.setStatus("current")
_CfprFirmwareSystemFsmStageTable_Object = MibTable
cfprFirmwareSystemFsmStageTable = _CfprFirmwareSystemFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 53)
)
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStageTable.setStatus("current")
_CfprFirmwareSystemFsmStageEntry_Object = MibTableRow
cfprFirmwareSystemFsmStageEntry = _CfprFirmwareSystemFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 53, 1)
)
cfprFirmwareSystemFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareSystemFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStageEntry.setStatus("current")
_CfprFirmwareSystemFsmStageInstanceId_Type = CfprManagedObjectId
_CfprFirmwareSystemFsmStageInstanceId_Object = MibTableColumn
cfprFirmwareSystemFsmStageInstanceId = _CfprFirmwareSystemFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 53, 1, 1),
    _CfprFirmwareSystemFsmStageInstanceId_Type()
)
cfprFirmwareSystemFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStageInstanceId.setStatus("current")
_CfprFirmwareSystemFsmStageDn_Type = CfprManagedObjectDn
_CfprFirmwareSystemFsmStageDn_Object = MibTableColumn
cfprFirmwareSystemFsmStageDn = _CfprFirmwareSystemFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 53, 1, 2),
    _CfprFirmwareSystemFsmStageDn_Type()
)
cfprFirmwareSystemFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStageDn.setStatus("current")
_CfprFirmwareSystemFsmStageRn_Type = SnmpAdminString
_CfprFirmwareSystemFsmStageRn_Object = MibTableColumn
cfprFirmwareSystemFsmStageRn = _CfprFirmwareSystemFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 53, 1, 3),
    _CfprFirmwareSystemFsmStageRn_Type()
)
cfprFirmwareSystemFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStageRn.setStatus("current")
_CfprFirmwareSystemFsmStageDescrData_Type = SnmpAdminString
_CfprFirmwareSystemFsmStageDescrData_Object = MibTableColumn
cfprFirmwareSystemFsmStageDescrData = _CfprFirmwareSystemFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 53, 1, 4),
    _CfprFirmwareSystemFsmStageDescrData_Type()
)
cfprFirmwareSystemFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStageDescrData.setStatus("current")
_CfprFirmwareSystemFsmStageLastUpdateTime_Type = DateAndTime
_CfprFirmwareSystemFsmStageLastUpdateTime_Object = MibTableColumn
cfprFirmwareSystemFsmStageLastUpdateTime = _CfprFirmwareSystemFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 53, 1, 5),
    _CfprFirmwareSystemFsmStageLastUpdateTime_Type()
)
cfprFirmwareSystemFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStageLastUpdateTime.setStatus("current")
_CfprFirmwareSystemFsmStageName_Type = CfprFirmwareSystemFsmStageName
_CfprFirmwareSystemFsmStageName_Object = MibTableColumn
cfprFirmwareSystemFsmStageName = _CfprFirmwareSystemFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 53, 1, 6),
    _CfprFirmwareSystemFsmStageName_Type()
)
cfprFirmwareSystemFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStageName.setStatus("current")
_CfprFirmwareSystemFsmStageOrder_Type = Gauge32
_CfprFirmwareSystemFsmStageOrder_Object = MibTableColumn
cfprFirmwareSystemFsmStageOrder = _CfprFirmwareSystemFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 53, 1, 7),
    _CfprFirmwareSystemFsmStageOrder_Type()
)
cfprFirmwareSystemFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStageOrder.setStatus("current")
_CfprFirmwareSystemFsmStageRetry_Type = Gauge32
_CfprFirmwareSystemFsmStageRetry_Object = MibTableColumn
cfprFirmwareSystemFsmStageRetry = _CfprFirmwareSystemFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 53, 1, 8),
    _CfprFirmwareSystemFsmStageRetry_Type()
)
cfprFirmwareSystemFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStageRetry.setStatus("current")
_CfprFirmwareSystemFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwareSystemFsmStageStageStatus_Object = MibTableColumn
cfprFirmwareSystemFsmStageStageStatus = _CfprFirmwareSystemFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 53, 1, 9),
    _CfprFirmwareSystemFsmStageStageStatus_Type()
)
cfprFirmwareSystemFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmStageStageStatus.setStatus("current")
_CfprFirmwareSystemFsmTaskTable_Object = MibTable
cfprFirmwareSystemFsmTaskTable = _CfprFirmwareSystemFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 54)
)
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmTaskTable.setStatus("current")
_CfprFirmwareSystemFsmTaskEntry_Object = MibTableRow
cfprFirmwareSystemFsmTaskEntry = _CfprFirmwareSystemFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 54, 1)
)
cfprFirmwareSystemFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareSystemFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmTaskEntry.setStatus("current")
_CfprFirmwareSystemFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprFirmwareSystemFsmTaskInstanceId_Object = MibTableColumn
cfprFirmwareSystemFsmTaskInstanceId = _CfprFirmwareSystemFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 54, 1, 1),
    _CfprFirmwareSystemFsmTaskInstanceId_Type()
)
cfprFirmwareSystemFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmTaskInstanceId.setStatus("current")
_CfprFirmwareSystemFsmTaskDn_Type = CfprManagedObjectDn
_CfprFirmwareSystemFsmTaskDn_Object = MibTableColumn
cfprFirmwareSystemFsmTaskDn = _CfprFirmwareSystemFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 54, 1, 2),
    _CfprFirmwareSystemFsmTaskDn_Type()
)
cfprFirmwareSystemFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmTaskDn.setStatus("current")
_CfprFirmwareSystemFsmTaskRn_Type = SnmpAdminString
_CfprFirmwareSystemFsmTaskRn_Object = MibTableColumn
cfprFirmwareSystemFsmTaskRn = _CfprFirmwareSystemFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 54, 1, 3),
    _CfprFirmwareSystemFsmTaskRn_Type()
)
cfprFirmwareSystemFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmTaskRn.setStatus("current")
_CfprFirmwareSystemFsmTaskCompletion_Type = CfprFsmCompletion
_CfprFirmwareSystemFsmTaskCompletion_Object = MibTableColumn
cfprFirmwareSystemFsmTaskCompletion = _CfprFirmwareSystemFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 54, 1, 4),
    _CfprFirmwareSystemFsmTaskCompletion_Type()
)
cfprFirmwareSystemFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmTaskCompletion.setStatus("current")
_CfprFirmwareSystemFsmTaskFlags_Type = CfprFirmwareSystemFsmTaskFlags
_CfprFirmwareSystemFsmTaskFlags_Object = MibTableColumn
cfprFirmwareSystemFsmTaskFlags = _CfprFirmwareSystemFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 54, 1, 5),
    _CfprFirmwareSystemFsmTaskFlags_Type()
)
cfprFirmwareSystemFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmTaskFlags.setStatus("current")
_CfprFirmwareSystemFsmTaskItem_Type = CfprFirmwareSystemFsmTaskItem
_CfprFirmwareSystemFsmTaskItem_Object = MibTableColumn
cfprFirmwareSystemFsmTaskItem = _CfprFirmwareSystemFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 54, 1, 6),
    _CfprFirmwareSystemFsmTaskItem_Type()
)
cfprFirmwareSystemFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmTaskItem.setStatus("current")
_CfprFirmwareSystemFsmTaskSeqId_Type = Gauge32
_CfprFirmwareSystemFsmTaskSeqId_Object = MibTableColumn
cfprFirmwareSystemFsmTaskSeqId = _CfprFirmwareSystemFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 54, 1, 7),
    _CfprFirmwareSystemFsmTaskSeqId_Type()
)
cfprFirmwareSystemFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSystemFsmTaskSeqId.setStatus("current")
_CfprFirmwareTypeTable_Object = MibTable
cfprFirmwareTypeTable = _CfprFirmwareTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 55)
)
if mibBuilder.loadTexts:
    cfprFirmwareTypeTable.setStatus("current")
_CfprFirmwareTypeEntry_Object = MibTableRow
cfprFirmwareTypeEntry = _CfprFirmwareTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 55, 1)
)
cfprFirmwareTypeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareTypeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareTypeEntry.setStatus("current")
_CfprFirmwareTypeInstanceId_Type = CfprManagedObjectId
_CfprFirmwareTypeInstanceId_Object = MibTableColumn
cfprFirmwareTypeInstanceId = _CfprFirmwareTypeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 55, 1, 1),
    _CfprFirmwareTypeInstanceId_Type()
)
cfprFirmwareTypeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareTypeInstanceId.setStatus("current")
_CfprFirmwareTypeDn_Type = CfprManagedObjectDn
_CfprFirmwareTypeDn_Object = MibTableColumn
cfprFirmwareTypeDn = _CfprFirmwareTypeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 55, 1, 2),
    _CfprFirmwareTypeDn_Type()
)
cfprFirmwareTypeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareTypeDn.setStatus("current")
_CfprFirmwareTypeRn_Type = SnmpAdminString
_CfprFirmwareTypeRn_Object = MibTableColumn
cfprFirmwareTypeRn = _CfprFirmwareTypeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 55, 1, 3),
    _CfprFirmwareTypeRn_Type()
)
cfprFirmwareTypeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareTypeRn.setStatus("current")
_CfprFirmwareTypeEp_Type = CfprFirmwareType
_CfprFirmwareTypeEp_Object = MibTableColumn
cfprFirmwareTypeEp = _CfprFirmwareTypeEp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 55, 1, 4),
    _CfprFirmwareTypeEp_Type()
)
cfprFirmwareTypeEp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareTypeEp.setStatus("current")
_CfprFirmwareTypeInvTag_Type = SnmpAdminString
_CfprFirmwareTypeInvTag_Object = MibTableColumn
cfprFirmwareTypeInvTag = _CfprFirmwareTypeInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 55, 1, 5),
    _CfprFirmwareTypeInvTag_Type()
)
cfprFirmwareTypeInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareTypeInvTag.setStatus("current")
_CfprFirmwareTypeMaxVer_Type = SnmpAdminString
_CfprFirmwareTypeMaxVer_Object = MibTableColumn
cfprFirmwareTypeMaxVer = _CfprFirmwareTypeMaxVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 55, 1, 6),
    _CfprFirmwareTypeMaxVer_Type()
)
cfprFirmwareTypeMaxVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareTypeMaxVer.setStatus("current")
_CfprFirmwareTypeMinVer_Type = SnmpAdminString
_CfprFirmwareTypeMinVer_Object = MibTableColumn
cfprFirmwareTypeMinVer = _CfprFirmwareTypeMinVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 55, 1, 7),
    _CfprFirmwareTypeMinVer_Type()
)
cfprFirmwareTypeMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareTypeMinVer.setStatus("current")
_CfprFirmwareTypePid_Type = SnmpAdminString
_CfprFirmwareTypePid_Object = MibTableColumn
cfprFirmwareTypePid = _CfprFirmwareTypePid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 55, 1, 8),
    _CfprFirmwareTypePid_Type()
)
cfprFirmwareTypePid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareTypePid.setStatus("current")
_CfprFirmwareTypeScheduledInstallTime_Type = DateAndTime
_CfprFirmwareTypeScheduledInstallTime_Object = MibTableColumn
cfprFirmwareTypeScheduledInstallTime = _CfprFirmwareTypeScheduledInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 55, 1, 9),
    _CfprFirmwareTypeScheduledInstallTime_Type()
)
cfprFirmwareTypeScheduledInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareTypeScheduledInstallTime.setStatus("current")
_CfprFirmwareFprcInfoTable_Object = MibTable
cfprFirmwareFprcInfoTable = _CfprFirmwareFprcInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 56)
)
if mibBuilder.loadTexts:
    cfprFirmwareFprcInfoTable.setStatus("current")
_CfprFirmwareFprcInfoEntry_Object = MibTableRow
cfprFirmwareFprcInfoEntry = _CfprFirmwareFprcInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 56, 1)
)
cfprFirmwareFprcInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareFprcInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareFprcInfoEntry.setStatus("current")
_CfprFirmwareFprcInfoInstanceId_Type = CfprManagedObjectId
_CfprFirmwareFprcInfoInstanceId_Object = MibTableColumn
cfprFirmwareFprcInfoInstanceId = _CfprFirmwareFprcInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 56, 1, 1),
    _CfprFirmwareFprcInfoInstanceId_Type()
)
cfprFirmwareFprcInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareFprcInfoInstanceId.setStatus("current")
_CfprFirmwareFprcInfoDn_Type = CfprManagedObjectDn
_CfprFirmwareFprcInfoDn_Object = MibTableColumn
cfprFirmwareFprcInfoDn = _CfprFirmwareFprcInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 56, 1, 2),
    _CfprFirmwareFprcInfoDn_Type()
)
cfprFirmwareFprcInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareFprcInfoDn.setStatus("current")
_CfprFirmwareFprcInfoRn_Type = SnmpAdminString
_CfprFirmwareFprcInfoRn_Object = MibTableColumn
cfprFirmwareFprcInfoRn = _CfprFirmwareFprcInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 56, 1, 3),
    _CfprFirmwareFprcInfoRn_Type()
)
cfprFirmwareFprcInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareFprcInfoRn.setStatus("current")
_CfprFirmwareFprcInfoConnProtocol_Type = CfprExtpolConnProtocol
_CfprFirmwareFprcInfoConnProtocol_Object = MibTableColumn
cfprFirmwareFprcInfoConnProtocol = _CfprFirmwareFprcInfoConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 56, 1, 4),
    _CfprFirmwareFprcInfoConnProtocol_Type()
)
cfprFirmwareFprcInfoConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareFprcInfoConnProtocol.setStatus("current")
_CfprFirmwareFprcInfoHost_Type = SnmpAdminString
_CfprFirmwareFprcInfoHost_Object = MibTableColumn
cfprFirmwareFprcInfoHost = _CfprFirmwareFprcInfoHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 56, 1, 5),
    _CfprFirmwareFprcInfoHost_Type()
)
cfprFirmwareFprcInfoHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareFprcInfoHost.setStatus("current")
_CfprFirmwareFprcInfoVersion_Type = SnmpAdminString
_CfprFirmwareFprcInfoVersion_Object = MibTableColumn
cfprFirmwareFprcInfoVersion = _CfprFirmwareFprcInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 56, 1, 6),
    _CfprFirmwareFprcInfoVersion_Type()
)
cfprFirmwareFprcInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareFprcInfoVersion.setStatus("current")
_CfprFirmwareUpdatableTable_Object = MibTable
cfprFirmwareUpdatableTable = _CfprFirmwareUpdatableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 57)
)
if mibBuilder.loadTexts:
    cfprFirmwareUpdatableTable.setStatus("current")
_CfprFirmwareUpdatableEntry_Object = MibTableRow
cfprFirmwareUpdatableEntry = _CfprFirmwareUpdatableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 57, 1)
)
cfprFirmwareUpdatableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareUpdatableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareUpdatableEntry.setStatus("current")
_CfprFirmwareUpdatableInstanceId_Type = CfprManagedObjectId
_CfprFirmwareUpdatableInstanceId_Object = MibTableColumn
cfprFirmwareUpdatableInstanceId = _CfprFirmwareUpdatableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 57, 1, 1),
    _CfprFirmwareUpdatableInstanceId_Type()
)
cfprFirmwareUpdatableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareUpdatableInstanceId.setStatus("current")
_CfprFirmwareUpdatableDn_Type = CfprManagedObjectDn
_CfprFirmwareUpdatableDn_Object = MibTableColumn
cfprFirmwareUpdatableDn = _CfprFirmwareUpdatableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 57, 1, 2),
    _CfprFirmwareUpdatableDn_Type()
)
cfprFirmwareUpdatableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpdatableDn.setStatus("current")
_CfprFirmwareUpdatableRn_Type = SnmpAdminString
_CfprFirmwareUpdatableRn_Object = MibTableColumn
cfprFirmwareUpdatableRn = _CfprFirmwareUpdatableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 57, 1, 3),
    _CfprFirmwareUpdatableRn_Type()
)
cfprFirmwareUpdatableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpdatableRn.setStatus("current")
_CfprFirmwareUpdatableAdminState_Type = CfprFirmwareTriggerState
_CfprFirmwareUpdatableAdminState_Object = MibTableColumn
cfprFirmwareUpdatableAdminState = _CfprFirmwareUpdatableAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 57, 1, 4),
    _CfprFirmwareUpdatableAdminState_Type()
)
cfprFirmwareUpdatableAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpdatableAdminState.setStatus("current")
_CfprFirmwareUpdatableDeployment_Type = CfprFirmwareUpdatableDeployment
_CfprFirmwareUpdatableDeployment_Object = MibTableColumn
cfprFirmwareUpdatableDeployment = _CfprFirmwareUpdatableDeployment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 57, 1, 5),
    _CfprFirmwareUpdatableDeployment_Type()
)
cfprFirmwareUpdatableDeployment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpdatableDeployment.setStatus("current")
_CfprFirmwareUpdatableOperState_Type = CfprFirmwareImageState
_CfprFirmwareUpdatableOperState_Object = MibTableColumn
cfprFirmwareUpdatableOperState = _CfprFirmwareUpdatableOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 57, 1, 6),
    _CfprFirmwareUpdatableOperState_Type()
)
cfprFirmwareUpdatableOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpdatableOperState.setStatus("current")
_CfprFirmwareUpdatableOperStateQual_Type = CfprFirmwareImageError
_CfprFirmwareUpdatableOperStateQual_Object = MibTableColumn
cfprFirmwareUpdatableOperStateQual = _CfprFirmwareUpdatableOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 57, 1, 7),
    _CfprFirmwareUpdatableOperStateQual_Type()
)
cfprFirmwareUpdatableOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpdatableOperStateQual.setStatus("current")
_CfprFirmwareUpdatablePrevVersion_Type = SnmpAdminString
_CfprFirmwareUpdatablePrevVersion_Object = MibTableColumn
cfprFirmwareUpdatablePrevVersion = _CfprFirmwareUpdatablePrevVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 57, 1, 8),
    _CfprFirmwareUpdatablePrevVersion_Type()
)
cfprFirmwareUpdatablePrevVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpdatablePrevVersion.setStatus("current")
_CfprFirmwareUpdatableVersion_Type = SnmpAdminString
_CfprFirmwareUpdatableVersion_Object = MibTableColumn
cfprFirmwareUpdatableVersion = _CfprFirmwareUpdatableVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 57, 1, 9),
    _CfprFirmwareUpdatableVersion_Type()
)
cfprFirmwareUpdatableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpdatableVersion.setStatus("current")
_CfprFirmwareUpgradeConstraintTable_Object = MibTable
cfprFirmwareUpgradeConstraintTable = _CfprFirmwareUpgradeConstraintTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 58)
)
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeConstraintTable.setStatus("current")
_CfprFirmwareUpgradeConstraintEntry_Object = MibTableRow
cfprFirmwareUpgradeConstraintEntry = _CfprFirmwareUpgradeConstraintEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 58, 1)
)
cfprFirmwareUpgradeConstraintEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareUpgradeConstraintInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeConstraintEntry.setStatus("current")
_CfprFirmwareUpgradeConstraintInstanceId_Type = CfprManagedObjectId
_CfprFirmwareUpgradeConstraintInstanceId_Object = MibTableColumn
cfprFirmwareUpgradeConstraintInstanceId = _CfprFirmwareUpgradeConstraintInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 58, 1, 1),
    _CfprFirmwareUpgradeConstraintInstanceId_Type()
)
cfprFirmwareUpgradeConstraintInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeConstraintInstanceId.setStatus("current")
_CfprFirmwareUpgradeConstraintDn_Type = CfprManagedObjectDn
_CfprFirmwareUpgradeConstraintDn_Object = MibTableColumn
cfprFirmwareUpgradeConstraintDn = _CfprFirmwareUpgradeConstraintDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 58, 1, 2),
    _CfprFirmwareUpgradeConstraintDn_Type()
)
cfprFirmwareUpgradeConstraintDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeConstraintDn.setStatus("current")
_CfprFirmwareUpgradeConstraintRn_Type = SnmpAdminString
_CfprFirmwareUpgradeConstraintRn_Object = MibTableColumn
cfprFirmwareUpgradeConstraintRn = _CfprFirmwareUpgradeConstraintRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 58, 1, 3),
    _CfprFirmwareUpgradeConstraintRn_Type()
)
cfprFirmwareUpgradeConstraintRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeConstraintRn.setStatus("current")
_CfprFirmwareUpgradeConstraintMinVer_Type = SnmpAdminString
_CfprFirmwareUpgradeConstraintMinVer_Object = MibTableColumn
cfprFirmwareUpgradeConstraintMinVer = _CfprFirmwareUpgradeConstraintMinVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 58, 1, 4),
    _CfprFirmwareUpgradeConstraintMinVer_Type()
)
cfprFirmwareUpgradeConstraintMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeConstraintMinVer.setStatus("current")
_CfprFirmwareUpgradeDetailTable_Object = MibTable
cfprFirmwareUpgradeDetailTable = _CfprFirmwareUpgradeDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 59)
)
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeDetailTable.setStatus("current")
_CfprFirmwareUpgradeDetailEntry_Object = MibTableRow
cfprFirmwareUpgradeDetailEntry = _CfprFirmwareUpgradeDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 59, 1)
)
cfprFirmwareUpgradeDetailEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareUpgradeDetailInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeDetailEntry.setStatus("current")
_CfprFirmwareUpgradeDetailInstanceId_Type = CfprManagedObjectId
_CfprFirmwareUpgradeDetailInstanceId_Object = MibTableColumn
cfprFirmwareUpgradeDetailInstanceId = _CfprFirmwareUpgradeDetailInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 59, 1, 1),
    _CfprFirmwareUpgradeDetailInstanceId_Type()
)
cfprFirmwareUpgradeDetailInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeDetailInstanceId.setStatus("current")
_CfprFirmwareUpgradeDetailDn_Type = CfprManagedObjectDn
_CfprFirmwareUpgradeDetailDn_Object = MibTableColumn
cfprFirmwareUpgradeDetailDn = _CfprFirmwareUpgradeDetailDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 59, 1, 2),
    _CfprFirmwareUpgradeDetailDn_Type()
)
cfprFirmwareUpgradeDetailDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeDetailDn.setStatus("current")
_CfprFirmwareUpgradeDetailRn_Type = SnmpAdminString
_CfprFirmwareUpgradeDetailRn_Object = MibTableColumn
cfprFirmwareUpgradeDetailRn = _CfprFirmwareUpgradeDetailRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 59, 1, 3),
    _CfprFirmwareUpgradeDetailRn_Type()
)
cfprFirmwareUpgradeDetailRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeDetailRn.setStatus("current")
_CfprFirmwareUpgradeDetailCategory_Type = CfprFirmwareUpgradeCategory
_CfprFirmwareUpgradeDetailCategory_Object = MibTableColumn
cfprFirmwareUpgradeDetailCategory = _CfprFirmwareUpgradeDetailCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 59, 1, 4),
    _CfprFirmwareUpgradeDetailCategory_Type()
)
cfprFirmwareUpgradeDetailCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeDetailCategory.setStatus("current")
_CfprFirmwareUpgradeDetailDescription_Type = SnmpAdminString
_CfprFirmwareUpgradeDetailDescription_Object = MibTableColumn
cfprFirmwareUpgradeDetailDescription = _CfprFirmwareUpgradeDetailDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 59, 1, 5),
    _CfprFirmwareUpgradeDetailDescription_Type()
)
cfprFirmwareUpgradeDetailDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeDetailDescription.setStatus("current")
_CfprFirmwareUpgradeDetailId_Type = Gauge32
_CfprFirmwareUpgradeDetailId_Object = MibTableColumn
cfprFirmwareUpgradeDetailId = _CfprFirmwareUpgradeDetailId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 59, 1, 6),
    _CfprFirmwareUpgradeDetailId_Type()
)
cfprFirmwareUpgradeDetailId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeDetailId.setStatus("current")
_CfprFirmwareUpgradeDetailSeverity_Type = CfprFirmwareUpgradeSeverity
_CfprFirmwareUpgradeDetailSeverity_Object = MibTableColumn
cfprFirmwareUpgradeDetailSeverity = _CfprFirmwareUpgradeDetailSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 59, 1, 7),
    _CfprFirmwareUpgradeDetailSeverity_Type()
)
cfprFirmwareUpgradeDetailSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeDetailSeverity.setStatus("current")
_CfprFirmwareUpgradeInfoTable_Object = MibTable
cfprFirmwareUpgradeInfoTable = _CfprFirmwareUpgradeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 60)
)
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeInfoTable.setStatus("current")
_CfprFirmwareUpgradeInfoEntry_Object = MibTableRow
cfprFirmwareUpgradeInfoEntry = _CfprFirmwareUpgradeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 60, 1)
)
cfprFirmwareUpgradeInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareUpgradeInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeInfoEntry.setStatus("current")
_CfprFirmwareUpgradeInfoInstanceId_Type = CfprManagedObjectId
_CfprFirmwareUpgradeInfoInstanceId_Object = MibTableColumn
cfprFirmwareUpgradeInfoInstanceId = _CfprFirmwareUpgradeInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 60, 1, 1),
    _CfprFirmwareUpgradeInfoInstanceId_Type()
)
cfprFirmwareUpgradeInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeInfoInstanceId.setStatus("current")
_CfprFirmwareUpgradeInfoDn_Type = CfprManagedObjectDn
_CfprFirmwareUpgradeInfoDn_Object = MibTableColumn
cfprFirmwareUpgradeInfoDn = _CfprFirmwareUpgradeInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 60, 1, 2),
    _CfprFirmwareUpgradeInfoDn_Type()
)
cfprFirmwareUpgradeInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeInfoDn.setStatus("current")
_CfprFirmwareUpgradeInfoRn_Type = SnmpAdminString
_CfprFirmwareUpgradeInfoRn_Object = MibTableColumn
cfprFirmwareUpgradeInfoRn = _CfprFirmwareUpgradeInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 60, 1, 3),
    _CfprFirmwareUpgradeInfoRn_Type()
)
cfprFirmwareUpgradeInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeInfoRn.setStatus("current")
_CfprFirmwareUpgradeInfoMessage_Type = SnmpAdminString
_CfprFirmwareUpgradeInfoMessage_Object = MibTableColumn
cfprFirmwareUpgradeInfoMessage = _CfprFirmwareUpgradeInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 60, 1, 4),
    _CfprFirmwareUpgradeInfoMessage_Type()
)
cfprFirmwareUpgradeInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeInfoMessage.setStatus("current")
_CfprFirmwareUpgradeInfoTimeStamp_Type = DateAndTime
_CfprFirmwareUpgradeInfoTimeStamp_Object = MibTableColumn
cfprFirmwareUpgradeInfoTimeStamp = _CfprFirmwareUpgradeInfoTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 60, 1, 5),
    _CfprFirmwareUpgradeInfoTimeStamp_Type()
)
cfprFirmwareUpgradeInfoTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeInfoTimeStamp.setStatus("current")
_CfprFirmwareUpgradeInfoValidateStatus_Type = CfprFirmwareUpgradeStatus
_CfprFirmwareUpgradeInfoValidateStatus_Object = MibTableColumn
cfprFirmwareUpgradeInfoValidateStatus = _CfprFirmwareUpgradeInfoValidateStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 60, 1, 6),
    _CfprFirmwareUpgradeInfoValidateStatus_Type()
)
cfprFirmwareUpgradeInfoValidateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeInfoValidateStatus.setStatus("current")
_CfprFirmwareUpgradeInfoVersion_Type = SnmpAdminString
_CfprFirmwareUpgradeInfoVersion_Object = MibTableColumn
cfprFirmwareUpgradeInfoVersion = _CfprFirmwareUpgradeInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 60, 1, 7),
    _CfprFirmwareUpgradeInfoVersion_Type()
)
cfprFirmwareUpgradeInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareUpgradeInfoVersion.setStatus("current")
_CfprFirmwareCspAppListTable_Object = MibTable
cfprFirmwareCspAppListTable = _CfprFirmwareCspAppListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 61)
)
if mibBuilder.loadTexts:
    cfprFirmwareCspAppListTable.setStatus("current")
_CfprFirmwareCspAppListEntry_Object = MibTableRow
cfprFirmwareCspAppListEntry = _CfprFirmwareCspAppListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 61, 1)
)
cfprFirmwareCspAppListEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareCspAppListInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareCspAppListEntry.setStatus("current")
_CfprFirmwareCspAppListInstanceId_Type = CfprManagedObjectId
_CfprFirmwareCspAppListInstanceId_Object = MibTableColumn
cfprFirmwareCspAppListInstanceId = _CfprFirmwareCspAppListInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 61, 1, 1),
    _CfprFirmwareCspAppListInstanceId_Type()
)
cfprFirmwareCspAppListInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareCspAppListInstanceId.setStatus("current")
_CfprFirmwareCspAppListDn_Type = CfprManagedObjectDn
_CfprFirmwareCspAppListDn_Object = MibTableColumn
cfprFirmwareCspAppListDn = _CfprFirmwareCspAppListDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 61, 1, 2),
    _CfprFirmwareCspAppListDn_Type()
)
cfprFirmwareCspAppListDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCspAppListDn.setStatus("current")
_CfprFirmwareCspAppListRn_Type = SnmpAdminString
_CfprFirmwareCspAppListRn_Object = MibTableColumn
cfprFirmwareCspAppListRn = _CfprFirmwareCspAppListRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 61, 1, 3),
    _CfprFirmwareCspAppListRn_Type()
)
cfprFirmwareCspAppListRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCspAppListRn.setStatus("current")
_CfprFirmwareCspAppListName_Type = SnmpAdminString
_CfprFirmwareCspAppListName_Object = MibTableColumn
cfprFirmwareCspAppListName = _CfprFirmwareCspAppListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 61, 1, 4),
    _CfprFirmwareCspAppListName_Type()
)
cfprFirmwareCspAppListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCspAppListName.setStatus("current")
_CfprFirmwareCspVersionTable_Object = MibTable
cfprFirmwareCspVersionTable = _CfprFirmwareCspVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 62)
)
if mibBuilder.loadTexts:
    cfprFirmwareCspVersionTable.setStatus("current")
_CfprFirmwareCspVersionEntry_Object = MibTableRow
cfprFirmwareCspVersionEntry = _CfprFirmwareCspVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 62, 1)
)
cfprFirmwareCspVersionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareCspVersionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareCspVersionEntry.setStatus("current")
_CfprFirmwareCspVersionInstanceId_Type = CfprManagedObjectId
_CfprFirmwareCspVersionInstanceId_Object = MibTableColumn
cfprFirmwareCspVersionInstanceId = _CfprFirmwareCspVersionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 62, 1, 1),
    _CfprFirmwareCspVersionInstanceId_Type()
)
cfprFirmwareCspVersionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareCspVersionInstanceId.setStatus("current")
_CfprFirmwareCspVersionDn_Type = CfprManagedObjectDn
_CfprFirmwareCspVersionDn_Object = MibTableColumn
cfprFirmwareCspVersionDn = _CfprFirmwareCspVersionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 62, 1, 2),
    _CfprFirmwareCspVersionDn_Type()
)
cfprFirmwareCspVersionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCspVersionDn.setStatus("current")
_CfprFirmwareCspVersionRn_Type = SnmpAdminString
_CfprFirmwareCspVersionRn_Object = MibTableColumn
cfprFirmwareCspVersionRn = _CfprFirmwareCspVersionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 62, 1, 3),
    _CfprFirmwareCspVersionRn_Type()
)
cfprFirmwareCspVersionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCspVersionRn.setStatus("current")
_CfprFirmwareCspVersionAppName_Type = SnmpAdminString
_CfprFirmwareCspVersionAppName_Object = MibTableColumn
cfprFirmwareCspVersionAppName = _CfprFirmwareCspVersionAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 62, 1, 4),
    _CfprFirmwareCspVersionAppName_Type()
)
cfprFirmwareCspVersionAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCspVersionAppName.setStatus("current")
_CfprFirmwareCspVersionFromVersion_Type = SnmpAdminString
_CfprFirmwareCspVersionFromVersion_Object = MibTableColumn
cfprFirmwareCspVersionFromVersion = _CfprFirmwareCspVersionFromVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 62, 1, 5),
    _CfprFirmwareCspVersionFromVersion_Type()
)
cfprFirmwareCspVersionFromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCspVersionFromVersion.setStatus("current")
_CfprFirmwareCspVersionName_Type = SnmpAdminString
_CfprFirmwareCspVersionName_Object = MibTableColumn
cfprFirmwareCspVersionName = _CfprFirmwareCspVersionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 62, 1, 6),
    _CfprFirmwareCspVersionName_Type()
)
cfprFirmwareCspVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCspVersionName.setStatus("current")
_CfprFirmwareCspVersionSecModelSupported_Type = SnmpAdminString
_CfprFirmwareCspVersionSecModelSupported_Object = MibTableColumn
cfprFirmwareCspVersionSecModelSupported = _CfprFirmwareCspVersionSecModelSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 62, 1, 7),
    _CfprFirmwareCspVersionSecModelSupported_Type()
)
cfprFirmwareCspVersionSecModelSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCspVersionSecModelSupported.setStatus("current")
_CfprFirmwareCspVersionSupportMode_Type = CfprFirmwareSupportedModeType
_CfprFirmwareCspVersionSupportMode_Object = MibTableColumn
cfprFirmwareCspVersionSupportMode = _CfprFirmwareCspVersionSupportMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 62, 1, 8),
    _CfprFirmwareCspVersionSupportMode_Type()
)
cfprFirmwareCspVersionSupportMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCspVersionSupportMode.setStatus("current")
_CfprFirmwareCspVersionToVersion_Type = SnmpAdminString
_CfprFirmwareCspVersionToVersion_Object = MibTableColumn
cfprFirmwareCspVersionToVersion = _CfprFirmwareCspVersionToVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 62, 1, 9),
    _CfprFirmwareCspVersionToVersion_Type()
)
cfprFirmwareCspVersionToVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareCspVersionToVersion.setStatus("current")
_CfprFirmwareDistCspBlackListTable_Object = MibTable
cfprFirmwareDistCspBlackListTable = _CfprFirmwareDistCspBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 63)
)
if mibBuilder.loadTexts:
    cfprFirmwareDistCspBlackListTable.setStatus("current")
_CfprFirmwareDistCspBlackListEntry_Object = MibTableRow
cfprFirmwareDistCspBlackListEntry = _CfprFirmwareDistCspBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 63, 1)
)
cfprFirmwareDistCspBlackListEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareDistCspBlackListInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareDistCspBlackListEntry.setStatus("current")
_CfprFirmwareDistCspBlackListInstanceId_Type = CfprManagedObjectId
_CfprFirmwareDistCspBlackListInstanceId_Object = MibTableColumn
cfprFirmwareDistCspBlackListInstanceId = _CfprFirmwareDistCspBlackListInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 63, 1, 1),
    _CfprFirmwareDistCspBlackListInstanceId_Type()
)
cfprFirmwareDistCspBlackListInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareDistCspBlackListInstanceId.setStatus("current")
_CfprFirmwareDistCspBlackListDn_Type = CfprManagedObjectDn
_CfprFirmwareDistCspBlackListDn_Object = MibTableColumn
cfprFirmwareDistCspBlackListDn = _CfprFirmwareDistCspBlackListDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 63, 1, 2),
    _CfprFirmwareDistCspBlackListDn_Type()
)
cfprFirmwareDistCspBlackListDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistCspBlackListDn.setStatus("current")
_CfprFirmwareDistCspBlackListRn_Type = SnmpAdminString
_CfprFirmwareDistCspBlackListRn_Object = MibTableColumn
cfprFirmwareDistCspBlackListRn = _CfprFirmwareDistCspBlackListRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 63, 1, 3),
    _CfprFirmwareDistCspBlackListRn_Type()
)
cfprFirmwareDistCspBlackListRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistCspBlackListRn.setStatus("current")
_CfprFirmwareDistCspBlackListName_Type = SnmpAdminString
_CfprFirmwareDistCspBlackListName_Object = MibTableColumn
cfprFirmwareDistCspBlackListName = _CfprFirmwareDistCspBlackListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 63, 1, 4),
    _CfprFirmwareDistCspBlackListName_Type()
)
cfprFirmwareDistCspBlackListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistCspBlackListName.setStatus("current")
_CfprFirmwareDistCspBlackListTimeStamp_Type = DateAndTime
_CfprFirmwareDistCspBlackListTimeStamp_Object = MibTableColumn
cfprFirmwareDistCspBlackListTimeStamp = _CfprFirmwareDistCspBlackListTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 63, 1, 5),
    _CfprFirmwareDistCspBlackListTimeStamp_Type()
)
cfprFirmwareDistCspBlackListTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistCspBlackListTimeStamp.setStatus("current")
_CfprFirmwareDistCspBlackListVersion_Type = SnmpAdminString
_CfprFirmwareDistCspBlackListVersion_Object = MibTableColumn
cfprFirmwareDistCspBlackListVersion = _CfprFirmwareDistCspBlackListVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 63, 1, 6),
    _CfprFirmwareDistCspBlackListVersion_Type()
)
cfprFirmwareDistCspBlackListVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareDistCspBlackListVersion.setStatus("current")
_CfprFirmwareRunnableTable_Object = MibTable
cfprFirmwareRunnableTable = _CfprFirmwareRunnableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 64)
)
if mibBuilder.loadTexts:
    cfprFirmwareRunnableTable.setStatus("current")
_CfprFirmwareRunnableEntry_Object = MibTableRow
cfprFirmwareRunnableEntry = _CfprFirmwareRunnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 64, 1)
)
cfprFirmwareRunnableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareRunnableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareRunnableEntry.setStatus("current")
_CfprFirmwareRunnableInstanceId_Type = CfprManagedObjectId
_CfprFirmwareRunnableInstanceId_Object = MibTableColumn
cfprFirmwareRunnableInstanceId = _CfprFirmwareRunnableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 64, 1, 1),
    _CfprFirmwareRunnableInstanceId_Type()
)
cfprFirmwareRunnableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareRunnableInstanceId.setStatus("current")
_CfprFirmwareRunnableDn_Type = CfprManagedObjectDn
_CfprFirmwareRunnableDn_Object = MibTableColumn
cfprFirmwareRunnableDn = _CfprFirmwareRunnableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 64, 1, 2),
    _CfprFirmwareRunnableDn_Type()
)
cfprFirmwareRunnableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunnableDn.setStatus("current")
_CfprFirmwareRunnableRn_Type = SnmpAdminString
_CfprFirmwareRunnableRn_Object = MibTableColumn
cfprFirmwareRunnableRn = _CfprFirmwareRunnableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 64, 1, 3),
    _CfprFirmwareRunnableRn_Type()
)
cfprFirmwareRunnableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunnableRn.setStatus("current")
_CfprFirmwareRunnableAdminState_Type = CfprFirmwareTriggerState
_CfprFirmwareRunnableAdminState_Object = MibTableColumn
cfprFirmwareRunnableAdminState = _CfprFirmwareRunnableAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 64, 1, 4),
    _CfprFirmwareRunnableAdminState_Type()
)
cfprFirmwareRunnableAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunnableAdminState.setStatus("current")
_CfprFirmwareRunnableDeployment_Type = CfprFirmwareDeployment
_CfprFirmwareRunnableDeployment_Object = MibTableColumn
cfprFirmwareRunnableDeployment = _CfprFirmwareRunnableDeployment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 64, 1, 5),
    _CfprFirmwareRunnableDeployment_Type()
)
cfprFirmwareRunnableDeployment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunnableDeployment.setStatus("current")
_CfprFirmwareRunnableMemFault_Type = TruthValue
_CfprFirmwareRunnableMemFault_Object = MibTableColumn
cfprFirmwareRunnableMemFault = _CfprFirmwareRunnableMemFault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 64, 1, 6),
    _CfprFirmwareRunnableMemFault_Type()
)
cfprFirmwareRunnableMemFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunnableMemFault.setStatus("current")
_CfprFirmwareRunnableOperState_Type = CfprFirmwareImageState
_CfprFirmwareRunnableOperState_Object = MibTableColumn
cfprFirmwareRunnableOperState = _CfprFirmwareRunnableOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 64, 1, 7),
    _CfprFirmwareRunnableOperState_Type()
)
cfprFirmwareRunnableOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunnableOperState.setStatus("current")
_CfprFirmwareRunnablePrevVersion_Type = SnmpAdminString
_CfprFirmwareRunnablePrevVersion_Object = MibTableColumn
cfprFirmwareRunnablePrevVersion = _CfprFirmwareRunnablePrevVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 64, 1, 8),
    _CfprFirmwareRunnablePrevVersion_Type()
)
cfprFirmwareRunnablePrevVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunnablePrevVersion.setStatus("current")
_CfprFirmwareRunnableVersion_Type = SnmpAdminString
_CfprFirmwareRunnableVersion_Object = MibTableColumn
cfprFirmwareRunnableVersion = _CfprFirmwareRunnableVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 64, 1, 9),
    _CfprFirmwareRunnableVersion_Type()
)
cfprFirmwareRunnableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareRunnableVersion.setStatus("current")
_CfprFirmwareSupFirmwareTable_Object = MibTable
cfprFirmwareSupFirmwareTable = _CfprFirmwareSupFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65)
)
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareTable.setStatus("current")
_CfprFirmwareSupFirmwareEntry_Object = MibTableRow
cfprFirmwareSupFirmwareEntry = _CfprFirmwareSupFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1)
)
cfprFirmwareSupFirmwareEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareSupFirmwareInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareEntry.setStatus("current")
_CfprFirmwareSupFirmwareInstanceId_Type = CfprManagedObjectId
_CfprFirmwareSupFirmwareInstanceId_Object = MibTableColumn
cfprFirmwareSupFirmwareInstanceId = _CfprFirmwareSupFirmwareInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 1),
    _CfprFirmwareSupFirmwareInstanceId_Type()
)
cfprFirmwareSupFirmwareInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareInstanceId.setStatus("current")
_CfprFirmwareSupFirmwareDn_Type = CfprManagedObjectDn
_CfprFirmwareSupFirmwareDn_Object = MibTableColumn
cfprFirmwareSupFirmwareDn = _CfprFirmwareSupFirmwareDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 2),
    _CfprFirmwareSupFirmwareDn_Type()
)
cfprFirmwareSupFirmwareDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareDn.setStatus("current")
_CfprFirmwareSupFirmwareRn_Type = SnmpAdminString
_CfprFirmwareSupFirmwareRn_Object = MibTableColumn
cfprFirmwareSupFirmwareRn = _CfprFirmwareSupFirmwareRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 3),
    _CfprFirmwareSupFirmwareRn_Type()
)
cfprFirmwareSupFirmwareRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareRn.setStatus("current")
_CfprFirmwareSupFirmwareForceUpgrade_Type = TruthValue
_CfprFirmwareSupFirmwareForceUpgrade_Object = MibTableColumn
cfprFirmwareSupFirmwareForceUpgrade = _CfprFirmwareSupFirmwareForceUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 4),
    _CfprFirmwareSupFirmwareForceUpgrade_Type()
)
cfprFirmwareSupFirmwareForceUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareForceUpgrade.setStatus("current")
_CfprFirmwareSupFirmwareFsmDescr_Type = SnmpAdminString
_CfprFirmwareSupFirmwareFsmDescr_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmDescr = _CfprFirmwareSupFirmwareFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 5),
    _CfprFirmwareSupFirmwareFsmDescr_Type()
)
cfprFirmwareSupFirmwareFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmDescr.setStatus("current")
_CfprFirmwareSupFirmwareFsmFlags_Type = SnmpAdminString
_CfprFirmwareSupFirmwareFsmFlags_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmFlags = _CfprFirmwareSupFirmwareFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 6),
    _CfprFirmwareSupFirmwareFsmFlags_Type()
)
cfprFirmwareSupFirmwareFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmFlags.setStatus("current")
_CfprFirmwareSupFirmwareFsmPrev_Type = SnmpAdminString
_CfprFirmwareSupFirmwareFsmPrev_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmPrev = _CfprFirmwareSupFirmwareFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 7),
    _CfprFirmwareSupFirmwareFsmPrev_Type()
)
cfprFirmwareSupFirmwareFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmPrev.setStatus("current")
_CfprFirmwareSupFirmwareFsmProgr_Type = Gauge32
_CfprFirmwareSupFirmwareFsmProgr_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmProgr = _CfprFirmwareSupFirmwareFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 8),
    _CfprFirmwareSupFirmwareFsmProgr_Type()
)
cfprFirmwareSupFirmwareFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmProgr.setStatus("current")
_CfprFirmwareSupFirmwareFsmRmtInvErrCode_Type = Gauge32
_CfprFirmwareSupFirmwareFsmRmtInvErrCode_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmRmtInvErrCode = _CfprFirmwareSupFirmwareFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 9),
    _CfprFirmwareSupFirmwareFsmRmtInvErrCode_Type()
)
cfprFirmwareSupFirmwareFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmRmtInvErrCode.setStatus("current")
_CfprFirmwareSupFirmwareFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprFirmwareSupFirmwareFsmRmtInvErrDescr_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmRmtInvErrDescr = _CfprFirmwareSupFirmwareFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 10),
    _CfprFirmwareSupFirmwareFsmRmtInvErrDescr_Type()
)
cfprFirmwareSupFirmwareFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmRmtInvErrDescr.setStatus("current")
_CfprFirmwareSupFirmwareFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwareSupFirmwareFsmRmtInvRslt_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmRmtInvRslt = _CfprFirmwareSupFirmwareFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 11),
    _CfprFirmwareSupFirmwareFsmRmtInvRslt_Type()
)
cfprFirmwareSupFirmwareFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmRmtInvRslt.setStatus("current")
_CfprFirmwareSupFirmwareFsmStageDescr_Type = SnmpAdminString
_CfprFirmwareSupFirmwareFsmStageDescr_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmStageDescr = _CfprFirmwareSupFirmwareFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 12),
    _CfprFirmwareSupFirmwareFsmStageDescr_Type()
)
cfprFirmwareSupFirmwareFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStageDescr.setStatus("current")
_CfprFirmwareSupFirmwareFsmStamp_Type = DateAndTime
_CfprFirmwareSupFirmwareFsmStamp_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmStamp = _CfprFirmwareSupFirmwareFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 13),
    _CfprFirmwareSupFirmwareFsmStamp_Type()
)
cfprFirmwareSupFirmwareFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStamp.setStatus("current")
_CfprFirmwareSupFirmwareFsmStatus_Type = SnmpAdminString
_CfprFirmwareSupFirmwareFsmStatus_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmStatus = _CfprFirmwareSupFirmwareFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 14),
    _CfprFirmwareSupFirmwareFsmStatus_Type()
)
cfprFirmwareSupFirmwareFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStatus.setStatus("current")
_CfprFirmwareSupFirmwareFsmTry_Type = Gauge32
_CfprFirmwareSupFirmwareFsmTry_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmTry = _CfprFirmwareSupFirmwareFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 15),
    _CfprFirmwareSupFirmwareFsmTry_Type()
)
cfprFirmwareSupFirmwareFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmTry.setStatus("current")
_CfprFirmwareSupFirmwareOperState_Type = CfprFirmwareFwUpgradeState
_CfprFirmwareSupFirmwareOperState_Object = MibTableColumn
cfprFirmwareSupFirmwareOperState = _CfprFirmwareSupFirmwareOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 16),
    _CfprFirmwareSupFirmwareOperState_Type()
)
cfprFirmwareSupFirmwareOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareOperState.setStatus("current")
_CfprFirmwareSupFirmwarePackVersion_Type = SnmpAdminString
_CfprFirmwareSupFirmwarePackVersion_Object = MibTableColumn
cfprFirmwareSupFirmwarePackVersion = _CfprFirmwareSupFirmwarePackVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 17),
    _CfprFirmwareSupFirmwarePackVersion_Type()
)
cfprFirmwareSupFirmwarePackVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwarePackVersion.setStatus("current")
_CfprFirmwareSupFirmwareState_Type = CfprFirmwareFwState
_CfprFirmwareSupFirmwareState_Object = MibTableColumn
cfprFirmwareSupFirmwareState = _CfprFirmwareSupFirmwareState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 18),
    _CfprFirmwareSupFirmwareState_Type()
)
cfprFirmwareSupFirmwareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareState.setStatus("current")
_CfprFirmwareSupFirmwareUpgradeStatus_Type = SnmpAdminString
_CfprFirmwareSupFirmwareUpgradeStatus_Object = MibTableColumn
cfprFirmwareSupFirmwareUpgradeStatus = _CfprFirmwareSupFirmwareUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 19),
    _CfprFirmwareSupFirmwareUpgradeStatus_Type()
)
cfprFirmwareSupFirmwareUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareUpgradeStatus.setStatus("current")
_CfprFirmwareSupFirmwareIsAutoFwUpgradeInProgress_Type = TruthValue
_CfprFirmwareSupFirmwareIsAutoFwUpgradeInProgress_Object = MibTableColumn
cfprFirmwareSupFirmwareIsAutoFwUpgradeInProgress = _CfprFirmwareSupFirmwareIsAutoFwUpgradeInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 65, 1, 20),
    _CfprFirmwareSupFirmwareIsAutoFwUpgradeInProgress_Type()
)
cfprFirmwareSupFirmwareIsAutoFwUpgradeInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareIsAutoFwUpgradeInProgress.setStatus("current")
_CfprFirmwareSupFirmwareFsmTable_Object = MibTable
cfprFirmwareSupFirmwareFsmTable = _CfprFirmwareSupFirmwareFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66)
)
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmTable.setStatus("current")
_CfprFirmwareSupFirmwareFsmEntry_Object = MibTableRow
cfprFirmwareSupFirmwareFsmEntry = _CfprFirmwareSupFirmwareFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66, 1)
)
cfprFirmwareSupFirmwareFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareSupFirmwareFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmEntry.setStatus("current")
_CfprFirmwareSupFirmwareFsmInstanceId_Type = CfprManagedObjectId
_CfprFirmwareSupFirmwareFsmInstanceId_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmInstanceId = _CfprFirmwareSupFirmwareFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66, 1, 1),
    _CfprFirmwareSupFirmwareFsmInstanceId_Type()
)
cfprFirmwareSupFirmwareFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmInstanceId.setStatus("current")
_CfprFirmwareSupFirmwareFsmDn_Type = CfprManagedObjectDn
_CfprFirmwareSupFirmwareFsmDn_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmDn = _CfprFirmwareSupFirmwareFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66, 1, 2),
    _CfprFirmwareSupFirmwareFsmDn_Type()
)
cfprFirmwareSupFirmwareFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmDn.setStatus("current")
_CfprFirmwareSupFirmwareFsmRn_Type = SnmpAdminString
_CfprFirmwareSupFirmwareFsmRn_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmRn = _CfprFirmwareSupFirmwareFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66, 1, 3),
    _CfprFirmwareSupFirmwareFsmRn_Type()
)
cfprFirmwareSupFirmwareFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmRn.setStatus("current")
_CfprFirmwareSupFirmwareFsmCompletionTime_Type = DateAndTime
_CfprFirmwareSupFirmwareFsmCompletionTime_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmCompletionTime = _CfprFirmwareSupFirmwareFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66, 1, 4),
    _CfprFirmwareSupFirmwareFsmCompletionTime_Type()
)
cfprFirmwareSupFirmwareFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmCompletionTime.setStatus("current")
_CfprFirmwareSupFirmwareFsmCurrentFsm_Type = CfprFirmwareSupFirmwareFsmCurrentFsm
_CfprFirmwareSupFirmwareFsmCurrentFsm_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmCurrentFsm = _CfprFirmwareSupFirmwareFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66, 1, 5),
    _CfprFirmwareSupFirmwareFsmCurrentFsm_Type()
)
cfprFirmwareSupFirmwareFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmCurrentFsm.setStatus("current")
_CfprFirmwareSupFirmwareFsmDescrData_Type = SnmpAdminString
_CfprFirmwareSupFirmwareFsmDescrData_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmDescrData = _CfprFirmwareSupFirmwareFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66, 1, 6),
    _CfprFirmwareSupFirmwareFsmDescrData_Type()
)
cfprFirmwareSupFirmwareFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmDescrData.setStatus("current")
_CfprFirmwareSupFirmwareFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwareSupFirmwareFsmFsmStatus_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmFsmStatus = _CfprFirmwareSupFirmwareFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66, 1, 7),
    _CfprFirmwareSupFirmwareFsmFsmStatus_Type()
)
cfprFirmwareSupFirmwareFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmFsmStatus.setStatus("current")
_CfprFirmwareSupFirmwareFsmProgress_Type = Gauge32
_CfprFirmwareSupFirmwareFsmProgress_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmProgress = _CfprFirmwareSupFirmwareFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66, 1, 8),
    _CfprFirmwareSupFirmwareFsmProgress_Type()
)
cfprFirmwareSupFirmwareFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmProgress.setStatus("current")
_CfprFirmwareSupFirmwareFsmRmtErrCode_Type = Gauge32
_CfprFirmwareSupFirmwareFsmRmtErrCode_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmRmtErrCode = _CfprFirmwareSupFirmwareFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66, 1, 9),
    _CfprFirmwareSupFirmwareFsmRmtErrCode_Type()
)
cfprFirmwareSupFirmwareFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmRmtErrCode.setStatus("current")
_CfprFirmwareSupFirmwareFsmRmtErrDescr_Type = SnmpAdminString
_CfprFirmwareSupFirmwareFsmRmtErrDescr_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmRmtErrDescr = _CfprFirmwareSupFirmwareFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66, 1, 10),
    _CfprFirmwareSupFirmwareFsmRmtErrDescr_Type()
)
cfprFirmwareSupFirmwareFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmRmtErrDescr.setStatus("current")
_CfprFirmwareSupFirmwareFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwareSupFirmwareFsmRmtRslt_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmRmtRslt = _CfprFirmwareSupFirmwareFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 66, 1, 11),
    _CfprFirmwareSupFirmwareFsmRmtRslt_Type()
)
cfprFirmwareSupFirmwareFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmRmtRslt.setStatus("current")
_CfprFirmwareSupFirmwareFsmStageTable_Object = MibTable
cfprFirmwareSupFirmwareFsmStageTable = _CfprFirmwareSupFirmwareFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 67)
)
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStageTable.setStatus("current")
_CfprFirmwareSupFirmwareFsmStageEntry_Object = MibTableRow
cfprFirmwareSupFirmwareFsmStageEntry = _CfprFirmwareSupFirmwareFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 67, 1)
)
cfprFirmwareSupFirmwareFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareSupFirmwareFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStageEntry.setStatus("current")
_CfprFirmwareSupFirmwareFsmStageInstanceId_Type = CfprManagedObjectId
_CfprFirmwareSupFirmwareFsmStageInstanceId_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmStageInstanceId = _CfprFirmwareSupFirmwareFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 67, 1, 1),
    _CfprFirmwareSupFirmwareFsmStageInstanceId_Type()
)
cfprFirmwareSupFirmwareFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStageInstanceId.setStatus("current")
_CfprFirmwareSupFirmwareFsmStageDn_Type = CfprManagedObjectDn
_CfprFirmwareSupFirmwareFsmStageDn_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmStageDn = _CfprFirmwareSupFirmwareFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 67, 1, 2),
    _CfprFirmwareSupFirmwareFsmStageDn_Type()
)
cfprFirmwareSupFirmwareFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStageDn.setStatus("current")
_CfprFirmwareSupFirmwareFsmStageRn_Type = SnmpAdminString
_CfprFirmwareSupFirmwareFsmStageRn_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmStageRn = _CfprFirmwareSupFirmwareFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 67, 1, 3),
    _CfprFirmwareSupFirmwareFsmStageRn_Type()
)
cfprFirmwareSupFirmwareFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStageRn.setStatus("current")
_CfprFirmwareSupFirmwareFsmStageDescrData_Type = SnmpAdminString
_CfprFirmwareSupFirmwareFsmStageDescrData_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmStageDescrData = _CfprFirmwareSupFirmwareFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 67, 1, 4),
    _CfprFirmwareSupFirmwareFsmStageDescrData_Type()
)
cfprFirmwareSupFirmwareFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStageDescrData.setStatus("current")
_CfprFirmwareSupFirmwareFsmStageLastUpdateTime_Type = DateAndTime
_CfprFirmwareSupFirmwareFsmStageLastUpdateTime_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmStageLastUpdateTime = _CfprFirmwareSupFirmwareFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 67, 1, 5),
    _CfprFirmwareSupFirmwareFsmStageLastUpdateTime_Type()
)
cfprFirmwareSupFirmwareFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStageLastUpdateTime.setStatus("current")
_CfprFirmwareSupFirmwareFsmStageName_Type = CfprFirmwareSupFirmwareFsmStageName
_CfprFirmwareSupFirmwareFsmStageName_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmStageName = _CfprFirmwareSupFirmwareFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 67, 1, 6),
    _CfprFirmwareSupFirmwareFsmStageName_Type()
)
cfprFirmwareSupFirmwareFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStageName.setStatus("current")
_CfprFirmwareSupFirmwareFsmStageOrder_Type = Gauge32
_CfprFirmwareSupFirmwareFsmStageOrder_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmStageOrder = _CfprFirmwareSupFirmwareFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 67, 1, 7),
    _CfprFirmwareSupFirmwareFsmStageOrder_Type()
)
cfprFirmwareSupFirmwareFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStageOrder.setStatus("current")
_CfprFirmwareSupFirmwareFsmStageRetry_Type = Gauge32
_CfprFirmwareSupFirmwareFsmStageRetry_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmStageRetry = _CfprFirmwareSupFirmwareFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 67, 1, 8),
    _CfprFirmwareSupFirmwareFsmStageRetry_Type()
)
cfprFirmwareSupFirmwareFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStageRetry.setStatus("current")
_CfprFirmwareSupFirmwareFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwareSupFirmwareFsmStageStageStatus_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmStageStageStatus = _CfprFirmwareSupFirmwareFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 67, 1, 9),
    _CfprFirmwareSupFirmwareFsmStageStageStatus_Type()
)
cfprFirmwareSupFirmwareFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmStageStageStatus.setStatus("current")
_CfprFirmwareSupFirmwareFsmTaskTable_Object = MibTable
cfprFirmwareSupFirmwareFsmTaskTable = _CfprFirmwareSupFirmwareFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 68)
)
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmTaskTable.setStatus("current")
_CfprFirmwareSupFirmwareFsmTaskEntry_Object = MibTableRow
cfprFirmwareSupFirmwareFsmTaskEntry = _CfprFirmwareSupFirmwareFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 68, 1)
)
cfprFirmwareSupFirmwareFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareSupFirmwareFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmTaskEntry.setStatus("current")
_CfprFirmwareSupFirmwareFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprFirmwareSupFirmwareFsmTaskInstanceId_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmTaskInstanceId = _CfprFirmwareSupFirmwareFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 68, 1, 1),
    _CfprFirmwareSupFirmwareFsmTaskInstanceId_Type()
)
cfprFirmwareSupFirmwareFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmTaskInstanceId.setStatus("current")
_CfprFirmwareSupFirmwareFsmTaskDn_Type = CfprManagedObjectDn
_CfprFirmwareSupFirmwareFsmTaskDn_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmTaskDn = _CfprFirmwareSupFirmwareFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 68, 1, 2),
    _CfprFirmwareSupFirmwareFsmTaskDn_Type()
)
cfprFirmwareSupFirmwareFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmTaskDn.setStatus("current")
_CfprFirmwareSupFirmwareFsmTaskRn_Type = SnmpAdminString
_CfprFirmwareSupFirmwareFsmTaskRn_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmTaskRn = _CfprFirmwareSupFirmwareFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 68, 1, 3),
    _CfprFirmwareSupFirmwareFsmTaskRn_Type()
)
cfprFirmwareSupFirmwareFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmTaskRn.setStatus("current")
_CfprFirmwareSupFirmwareFsmTaskCompletion_Type = CfprFsmCompletion
_CfprFirmwareSupFirmwareFsmTaskCompletion_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmTaskCompletion = _CfprFirmwareSupFirmwareFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 68, 1, 4),
    _CfprFirmwareSupFirmwareFsmTaskCompletion_Type()
)
cfprFirmwareSupFirmwareFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmTaskCompletion.setStatus("current")
_CfprFirmwareSupFirmwareFsmTaskFlags_Type = CfprFirmwareSupFirmwareFsmTaskFlags
_CfprFirmwareSupFirmwareFsmTaskFlags_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmTaskFlags = _CfprFirmwareSupFirmwareFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 68, 1, 5),
    _CfprFirmwareSupFirmwareFsmTaskFlags_Type()
)
cfprFirmwareSupFirmwareFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmTaskFlags.setStatus("current")
_CfprFirmwareSupFirmwareFsmTaskItem_Type = CfprFirmwareSupFirmwareFsmTaskItem
_CfprFirmwareSupFirmwareFsmTaskItem_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmTaskItem = _CfprFirmwareSupFirmwareFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 68, 1, 6),
    _CfprFirmwareSupFirmwareFsmTaskItem_Type()
)
cfprFirmwareSupFirmwareFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmTaskItem.setStatus("current")
_CfprFirmwareSupFirmwareFsmTaskSeqId_Type = Gauge32
_CfprFirmwareSupFirmwareFsmTaskSeqId_Object = MibTableColumn
cfprFirmwareSupFirmwareFsmTaskSeqId = _CfprFirmwareSupFirmwareFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 68, 1, 7),
    _CfprFirmwareSupFirmwareFsmTaskSeqId_Type()
)
cfprFirmwareSupFirmwareFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareSupFirmwareFsmTaskSeqId.setStatus("current")
_CfprFirmwareValidationStatusTable_Object = MibTable
cfprFirmwareValidationStatusTable = _CfprFirmwareValidationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69)
)
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusTable.setStatus("current")
_CfprFirmwareValidationStatusEntry_Object = MibTableRow
cfprFirmwareValidationStatusEntry = _CfprFirmwareValidationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1)
)
cfprFirmwareValidationStatusEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareValidationStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusEntry.setStatus("current")
_CfprFirmwareValidationStatusInstanceId_Type = CfprManagedObjectId
_CfprFirmwareValidationStatusInstanceId_Object = MibTableColumn
cfprFirmwareValidationStatusInstanceId = _CfprFirmwareValidationStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 1),
    _CfprFirmwareValidationStatusInstanceId_Type()
)
cfprFirmwareValidationStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusInstanceId.setStatus("current")
_CfprFirmwareValidationStatusDn_Type = CfprManagedObjectDn
_CfprFirmwareValidationStatusDn_Object = MibTableColumn
cfprFirmwareValidationStatusDn = _CfprFirmwareValidationStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 2),
    _CfprFirmwareValidationStatusDn_Type()
)
cfprFirmwareValidationStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusDn.setStatus("current")
_CfprFirmwareValidationStatusRn_Type = SnmpAdminString
_CfprFirmwareValidationStatusRn_Object = MibTableColumn
cfprFirmwareValidationStatusRn = _CfprFirmwareValidationStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 3),
    _CfprFirmwareValidationStatusRn_Type()
)
cfprFirmwareValidationStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusRn.setStatus("current")
_CfprFirmwareValidationStatusAdapterImageStatusCode_Type = CfprFirmwareImageValidationType
_CfprFirmwareValidationStatusAdapterImageStatusCode_Object = MibTableColumn
cfprFirmwareValidationStatusAdapterImageStatusCode = _CfprFirmwareValidationStatusAdapterImageStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 4),
    _CfprFirmwareValidationStatusAdapterImageStatusCode_Type()
)
cfprFirmwareValidationStatusAdapterImageStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusAdapterImageStatusCode.setStatus("current")
_CfprFirmwareValidationStatusBiosImageStatusCode_Type = CfprFirmwareImageValidationType
_CfprFirmwareValidationStatusBiosImageStatusCode_Object = MibTableColumn
cfprFirmwareValidationStatusBiosImageStatusCode = _CfprFirmwareValidationStatusBiosImageStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 5),
    _CfprFirmwareValidationStatusBiosImageStatusCode_Type()
)
cfprFirmwareValidationStatusBiosImageStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusBiosImageStatusCode.setStatus("current")
_CfprFirmwareValidationStatusBmcImageStatusCode_Type = CfprFirmwareImageValidationType
_CfprFirmwareValidationStatusBmcImageStatusCode_Object = MibTableColumn
cfprFirmwareValidationStatusBmcImageStatusCode = _CfprFirmwareValidationStatusBmcImageStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 6),
    _CfprFirmwareValidationStatusBmcImageStatusCode_Type()
)
cfprFirmwareValidationStatusBmcImageStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusBmcImageStatusCode.setStatus("current")
_CfprFirmwareValidationStatusBrdctrlImageStatusCode_Type = CfprFirmwareImageValidationType
_CfprFirmwareValidationStatusBrdctrlImageStatusCode_Object = MibTableColumn
cfprFirmwareValidationStatusBrdctrlImageStatusCode = _CfprFirmwareValidationStatusBrdctrlImageStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 7),
    _CfprFirmwareValidationStatusBrdctrlImageStatusCode_Type()
)
cfprFirmwareValidationStatusBrdctrlImageStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusBrdctrlImageStatusCode.setStatus("current")
_CfprFirmwareValidationStatusFsmDescr_Type = SnmpAdminString
_CfprFirmwareValidationStatusFsmDescr_Object = MibTableColumn
cfprFirmwareValidationStatusFsmDescr = _CfprFirmwareValidationStatusFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 8),
    _CfprFirmwareValidationStatusFsmDescr_Type()
)
cfprFirmwareValidationStatusFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmDescr.setStatus("current")
_CfprFirmwareValidationStatusFsmFlags_Type = SnmpAdminString
_CfprFirmwareValidationStatusFsmFlags_Object = MibTableColumn
cfprFirmwareValidationStatusFsmFlags = _CfprFirmwareValidationStatusFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 9),
    _CfprFirmwareValidationStatusFsmFlags_Type()
)
cfprFirmwareValidationStatusFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmFlags.setStatus("current")
_CfprFirmwareValidationStatusFsmPrev_Type = SnmpAdminString
_CfprFirmwareValidationStatusFsmPrev_Object = MibTableColumn
cfprFirmwareValidationStatusFsmPrev = _CfprFirmwareValidationStatusFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 10),
    _CfprFirmwareValidationStatusFsmPrev_Type()
)
cfprFirmwareValidationStatusFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmPrev.setStatus("current")
_CfprFirmwareValidationStatusFsmProgr_Type = Gauge32
_CfprFirmwareValidationStatusFsmProgr_Object = MibTableColumn
cfprFirmwareValidationStatusFsmProgr = _CfprFirmwareValidationStatusFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 11),
    _CfprFirmwareValidationStatusFsmProgr_Type()
)
cfprFirmwareValidationStatusFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmProgr.setStatus("current")
_CfprFirmwareValidationStatusFsmRmtInvErrCode_Type = Gauge32
_CfprFirmwareValidationStatusFsmRmtInvErrCode_Object = MibTableColumn
cfprFirmwareValidationStatusFsmRmtInvErrCode = _CfprFirmwareValidationStatusFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 12),
    _CfprFirmwareValidationStatusFsmRmtInvErrCode_Type()
)
cfprFirmwareValidationStatusFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmRmtInvErrCode.setStatus("current")
_CfprFirmwareValidationStatusFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprFirmwareValidationStatusFsmRmtInvErrDescr_Object = MibTableColumn
cfprFirmwareValidationStatusFsmRmtInvErrDescr = _CfprFirmwareValidationStatusFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 13),
    _CfprFirmwareValidationStatusFsmRmtInvErrDescr_Type()
)
cfprFirmwareValidationStatusFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmRmtInvErrDescr.setStatus("current")
_CfprFirmwareValidationStatusFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwareValidationStatusFsmRmtInvRslt_Object = MibTableColumn
cfprFirmwareValidationStatusFsmRmtInvRslt = _CfprFirmwareValidationStatusFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 14),
    _CfprFirmwareValidationStatusFsmRmtInvRslt_Type()
)
cfprFirmwareValidationStatusFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmRmtInvRslt.setStatus("current")
_CfprFirmwareValidationStatusFsmStageDescr_Type = SnmpAdminString
_CfprFirmwareValidationStatusFsmStageDescr_Object = MibTableColumn
cfprFirmwareValidationStatusFsmStageDescr = _CfprFirmwareValidationStatusFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 15),
    _CfprFirmwareValidationStatusFsmStageDescr_Type()
)
cfprFirmwareValidationStatusFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStageDescr.setStatus("current")
_CfprFirmwareValidationStatusFsmStamp_Type = DateAndTime
_CfprFirmwareValidationStatusFsmStamp_Object = MibTableColumn
cfprFirmwareValidationStatusFsmStamp = _CfprFirmwareValidationStatusFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 16),
    _CfprFirmwareValidationStatusFsmStamp_Type()
)
cfprFirmwareValidationStatusFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStamp.setStatus("current")
_CfprFirmwareValidationStatusFsmStatus_Type = SnmpAdminString
_CfprFirmwareValidationStatusFsmStatus_Object = MibTableColumn
cfprFirmwareValidationStatusFsmStatus = _CfprFirmwareValidationStatusFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 17),
    _CfprFirmwareValidationStatusFsmStatus_Type()
)
cfprFirmwareValidationStatusFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStatus.setStatus("current")
_CfprFirmwareValidationStatusFsmTry_Type = Gauge32
_CfprFirmwareValidationStatusFsmTry_Object = MibTableColumn
cfprFirmwareValidationStatusFsmTry = _CfprFirmwareValidationStatusFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 18),
    _CfprFirmwareValidationStatusFsmTry_Type()
)
cfprFirmwareValidationStatusFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmTry.setStatus("current")
_CfprFirmwareValidationStatusKickstartImageStatusCode_Type = CfprFirmwareImageValidationType
_CfprFirmwareValidationStatusKickstartImageStatusCode_Object = MibTableColumn
cfprFirmwareValidationStatusKickstartImageStatusCode = _CfprFirmwareValidationStatusKickstartImageStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 19),
    _CfprFirmwareValidationStatusKickstartImageStatusCode_Type()
)
cfprFirmwareValidationStatusKickstartImageStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusKickstartImageStatusCode.setStatus("current")
_CfprFirmwareValidationStatusMgtExtImageStatusCode_Type = CfprFirmwareImageValidationType
_CfprFirmwareValidationStatusMgtExtImageStatusCode_Object = MibTableColumn
cfprFirmwareValidationStatusMgtExtImageStatusCode = _CfprFirmwareValidationStatusMgtExtImageStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 20),
    _CfprFirmwareValidationStatusMgtExtImageStatusCode_Type()
)
cfprFirmwareValidationStatusMgtExtImageStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusMgtExtImageStatusCode.setStatus("current")
_CfprFirmwareValidationStatusOverallStatusCode_Type = CfprFirmwareImageValidationType
_CfprFirmwareValidationStatusOverallStatusCode_Object = MibTableColumn
cfprFirmwareValidationStatusOverallStatusCode = _CfprFirmwareValidationStatusOverallStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 21),
    _CfprFirmwareValidationStatusOverallStatusCode_Type()
)
cfprFirmwareValidationStatusOverallStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusOverallStatusCode.setStatus("current")
_CfprFirmwareValidationStatusOverallStatusString_Type = SnmpAdminString
_CfprFirmwareValidationStatusOverallStatusString_Object = MibTableColumn
cfprFirmwareValidationStatusOverallStatusString = _CfprFirmwareValidationStatusOverallStatusString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 22),
    _CfprFirmwareValidationStatusOverallStatusString_Type()
)
cfprFirmwareValidationStatusOverallStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusOverallStatusString.setStatus("current")
_CfprFirmwareValidationStatusPackName_Type = SnmpAdminString
_CfprFirmwareValidationStatusPackName_Object = MibTableColumn
cfprFirmwareValidationStatusPackName = _CfprFirmwareValidationStatusPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 23),
    _CfprFirmwareValidationStatusPackName_Type()
)
cfprFirmwareValidationStatusPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusPackName.setStatus("current")
_CfprFirmwareValidationStatusPackVersion_Type = SnmpAdminString
_CfprFirmwareValidationStatusPackVersion_Object = MibTableColumn
cfprFirmwareValidationStatusPackVersion = _CfprFirmwareValidationStatusPackVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 24),
    _CfprFirmwareValidationStatusPackVersion_Type()
)
cfprFirmwareValidationStatusPackVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusPackVersion.setStatus("current")
_CfprFirmwareValidationStatusSsposImageStatusCode_Type = CfprFirmwareImageValidationType
_CfprFirmwareValidationStatusSsposImageStatusCode_Object = MibTableColumn
cfprFirmwareValidationStatusSsposImageStatusCode = _CfprFirmwareValidationStatusSsposImageStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 25),
    _CfprFirmwareValidationStatusSsposImageStatusCode_Type()
)
cfprFirmwareValidationStatusSsposImageStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusSsposImageStatusCode.setStatus("current")
_CfprFirmwareValidationStatusState_Type = CfprFirmwareImageValidationStateType
_CfprFirmwareValidationStatusState_Object = MibTableColumn
cfprFirmwareValidationStatusState = _CfprFirmwareValidationStatusState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 26),
    _CfprFirmwareValidationStatusState_Type()
)
cfprFirmwareValidationStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusState.setStatus("current")
_CfprFirmwareValidationStatusStorageImageStatusCode_Type = CfprFirmwareImageValidationType
_CfprFirmwareValidationStatusStorageImageStatusCode_Object = MibTableColumn
cfprFirmwareValidationStatusStorageImageStatusCode = _CfprFirmwareValidationStatusStorageImageStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 27),
    _CfprFirmwareValidationStatusStorageImageStatusCode_Type()
)
cfprFirmwareValidationStatusStorageImageStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusStorageImageStatusCode.setStatus("current")
_CfprFirmwareValidationStatusSvcMgrImageStatusCode_Type = CfprFirmwareImageValidationType
_CfprFirmwareValidationStatusSvcMgrImageStatusCode_Object = MibTableColumn
cfprFirmwareValidationStatusSvcMgrImageStatusCode = _CfprFirmwareValidationStatusSvcMgrImageStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 28),
    _CfprFirmwareValidationStatusSvcMgrImageStatusCode_Type()
)
cfprFirmwareValidationStatusSvcMgrImageStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusSvcMgrImageStatusCode.setStatus("current")
_CfprFirmwareValidationStatusSystemImageStatusCode_Type = CfprFirmwareImageValidationType
_CfprFirmwareValidationStatusSystemImageStatusCode_Object = MibTableColumn
cfprFirmwareValidationStatusSystemImageStatusCode = _CfprFirmwareValidationStatusSystemImageStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 29),
    _CfprFirmwareValidationStatusSystemImageStatusCode_Type()
)
cfprFirmwareValidationStatusSystemImageStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusSystemImageStatusCode.setStatus("current")
_CfprFirmwareValidationStatusTimeStamp_Type = DateAndTime
_CfprFirmwareValidationStatusTimeStamp_Object = MibTableColumn
cfprFirmwareValidationStatusTimeStamp = _CfprFirmwareValidationStatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 69, 1, 30),
    _CfprFirmwareValidationStatusTimeStamp_Type()
)
cfprFirmwareValidationStatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusTimeStamp.setStatus("current")
_CfprFirmwareValidationStatusFsmTable_Object = MibTable
cfprFirmwareValidationStatusFsmTable = _CfprFirmwareValidationStatusFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70)
)
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmTable.setStatus("current")
_CfprFirmwareValidationStatusFsmEntry_Object = MibTableRow
cfprFirmwareValidationStatusFsmEntry = _CfprFirmwareValidationStatusFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70, 1)
)
cfprFirmwareValidationStatusFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareValidationStatusFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmEntry.setStatus("current")
_CfprFirmwareValidationStatusFsmInstanceId_Type = CfprManagedObjectId
_CfprFirmwareValidationStatusFsmInstanceId_Object = MibTableColumn
cfprFirmwareValidationStatusFsmInstanceId = _CfprFirmwareValidationStatusFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70, 1, 1),
    _CfprFirmwareValidationStatusFsmInstanceId_Type()
)
cfprFirmwareValidationStatusFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmInstanceId.setStatus("current")
_CfprFirmwareValidationStatusFsmDn_Type = CfprManagedObjectDn
_CfprFirmwareValidationStatusFsmDn_Object = MibTableColumn
cfprFirmwareValidationStatusFsmDn = _CfprFirmwareValidationStatusFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70, 1, 2),
    _CfprFirmwareValidationStatusFsmDn_Type()
)
cfprFirmwareValidationStatusFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmDn.setStatus("current")
_CfprFirmwareValidationStatusFsmRn_Type = SnmpAdminString
_CfprFirmwareValidationStatusFsmRn_Object = MibTableColumn
cfprFirmwareValidationStatusFsmRn = _CfprFirmwareValidationStatusFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70, 1, 3),
    _CfprFirmwareValidationStatusFsmRn_Type()
)
cfprFirmwareValidationStatusFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmRn.setStatus("current")
_CfprFirmwareValidationStatusFsmCompletionTime_Type = DateAndTime
_CfprFirmwareValidationStatusFsmCompletionTime_Object = MibTableColumn
cfprFirmwareValidationStatusFsmCompletionTime = _CfprFirmwareValidationStatusFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70, 1, 4),
    _CfprFirmwareValidationStatusFsmCompletionTime_Type()
)
cfprFirmwareValidationStatusFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmCompletionTime.setStatus("current")
_CfprFirmwareValidationStatusFsmCurrentFsm_Type = CfprFirmwareValidationStatusFsmCurrentFsm
_CfprFirmwareValidationStatusFsmCurrentFsm_Object = MibTableColumn
cfprFirmwareValidationStatusFsmCurrentFsm = _CfprFirmwareValidationStatusFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70, 1, 5),
    _CfprFirmwareValidationStatusFsmCurrentFsm_Type()
)
cfprFirmwareValidationStatusFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmCurrentFsm.setStatus("current")
_CfprFirmwareValidationStatusFsmDescrData_Type = SnmpAdminString
_CfprFirmwareValidationStatusFsmDescrData_Object = MibTableColumn
cfprFirmwareValidationStatusFsmDescrData = _CfprFirmwareValidationStatusFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70, 1, 6),
    _CfprFirmwareValidationStatusFsmDescrData_Type()
)
cfprFirmwareValidationStatusFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmDescrData.setStatus("current")
_CfprFirmwareValidationStatusFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwareValidationStatusFsmFsmStatus_Object = MibTableColumn
cfprFirmwareValidationStatusFsmFsmStatus = _CfprFirmwareValidationStatusFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70, 1, 7),
    _CfprFirmwareValidationStatusFsmFsmStatus_Type()
)
cfprFirmwareValidationStatusFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmFsmStatus.setStatus("current")
_CfprFirmwareValidationStatusFsmProgress_Type = Gauge32
_CfprFirmwareValidationStatusFsmProgress_Object = MibTableColumn
cfprFirmwareValidationStatusFsmProgress = _CfprFirmwareValidationStatusFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70, 1, 8),
    _CfprFirmwareValidationStatusFsmProgress_Type()
)
cfprFirmwareValidationStatusFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmProgress.setStatus("current")
_CfprFirmwareValidationStatusFsmRmtErrCode_Type = Gauge32
_CfprFirmwareValidationStatusFsmRmtErrCode_Object = MibTableColumn
cfprFirmwareValidationStatusFsmRmtErrCode = _CfprFirmwareValidationStatusFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70, 1, 9),
    _CfprFirmwareValidationStatusFsmRmtErrCode_Type()
)
cfprFirmwareValidationStatusFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmRmtErrCode.setStatus("current")
_CfprFirmwareValidationStatusFsmRmtErrDescr_Type = SnmpAdminString
_CfprFirmwareValidationStatusFsmRmtErrDescr_Object = MibTableColumn
cfprFirmwareValidationStatusFsmRmtErrDescr = _CfprFirmwareValidationStatusFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70, 1, 10),
    _CfprFirmwareValidationStatusFsmRmtErrDescr_Type()
)
cfprFirmwareValidationStatusFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmRmtErrDescr.setStatus("current")
_CfprFirmwareValidationStatusFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprFirmwareValidationStatusFsmRmtRslt_Object = MibTableColumn
cfprFirmwareValidationStatusFsmRmtRslt = _CfprFirmwareValidationStatusFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 70, 1, 11),
    _CfprFirmwareValidationStatusFsmRmtRslt_Type()
)
cfprFirmwareValidationStatusFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmRmtRslt.setStatus("current")
_CfprFirmwareValidationStatusFsmStageTable_Object = MibTable
cfprFirmwareValidationStatusFsmStageTable = _CfprFirmwareValidationStatusFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 71)
)
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStageTable.setStatus("current")
_CfprFirmwareValidationStatusFsmStageEntry_Object = MibTableRow
cfprFirmwareValidationStatusFsmStageEntry = _CfprFirmwareValidationStatusFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 71, 1)
)
cfprFirmwareValidationStatusFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareValidationStatusFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStageEntry.setStatus("current")
_CfprFirmwareValidationStatusFsmStageInstanceId_Type = CfprManagedObjectId
_CfprFirmwareValidationStatusFsmStageInstanceId_Object = MibTableColumn
cfprFirmwareValidationStatusFsmStageInstanceId = _CfprFirmwareValidationStatusFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 71, 1, 1),
    _CfprFirmwareValidationStatusFsmStageInstanceId_Type()
)
cfprFirmwareValidationStatusFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStageInstanceId.setStatus("current")
_CfprFirmwareValidationStatusFsmStageDn_Type = CfprManagedObjectDn
_CfprFirmwareValidationStatusFsmStageDn_Object = MibTableColumn
cfprFirmwareValidationStatusFsmStageDn = _CfprFirmwareValidationStatusFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 71, 1, 2),
    _CfprFirmwareValidationStatusFsmStageDn_Type()
)
cfprFirmwareValidationStatusFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStageDn.setStatus("current")
_CfprFirmwareValidationStatusFsmStageRn_Type = SnmpAdminString
_CfprFirmwareValidationStatusFsmStageRn_Object = MibTableColumn
cfprFirmwareValidationStatusFsmStageRn = _CfprFirmwareValidationStatusFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 71, 1, 3),
    _CfprFirmwareValidationStatusFsmStageRn_Type()
)
cfprFirmwareValidationStatusFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStageRn.setStatus("current")
_CfprFirmwareValidationStatusFsmStageDescrData_Type = SnmpAdminString
_CfprFirmwareValidationStatusFsmStageDescrData_Object = MibTableColumn
cfprFirmwareValidationStatusFsmStageDescrData = _CfprFirmwareValidationStatusFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 71, 1, 4),
    _CfprFirmwareValidationStatusFsmStageDescrData_Type()
)
cfprFirmwareValidationStatusFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStageDescrData.setStatus("current")
_CfprFirmwareValidationStatusFsmStageLastUpdateTime_Type = DateAndTime
_CfprFirmwareValidationStatusFsmStageLastUpdateTime_Object = MibTableColumn
cfprFirmwareValidationStatusFsmStageLastUpdateTime = _CfprFirmwareValidationStatusFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 71, 1, 5),
    _CfprFirmwareValidationStatusFsmStageLastUpdateTime_Type()
)
cfprFirmwareValidationStatusFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStageLastUpdateTime.setStatus("current")
_CfprFirmwareValidationStatusFsmStageName_Type = CfprFirmwareValidationStatusFsmStageName
_CfprFirmwareValidationStatusFsmStageName_Object = MibTableColumn
cfprFirmwareValidationStatusFsmStageName = _CfprFirmwareValidationStatusFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 71, 1, 6),
    _CfprFirmwareValidationStatusFsmStageName_Type()
)
cfprFirmwareValidationStatusFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStageName.setStatus("current")
_CfprFirmwareValidationStatusFsmStageOrder_Type = Gauge32
_CfprFirmwareValidationStatusFsmStageOrder_Object = MibTableColumn
cfprFirmwareValidationStatusFsmStageOrder = _CfprFirmwareValidationStatusFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 71, 1, 7),
    _CfprFirmwareValidationStatusFsmStageOrder_Type()
)
cfprFirmwareValidationStatusFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStageOrder.setStatus("current")
_CfprFirmwareValidationStatusFsmStageRetry_Type = Gauge32
_CfprFirmwareValidationStatusFsmStageRetry_Object = MibTableColumn
cfprFirmwareValidationStatusFsmStageRetry = _CfprFirmwareValidationStatusFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 71, 1, 8),
    _CfprFirmwareValidationStatusFsmStageRetry_Type()
)
cfprFirmwareValidationStatusFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStageRetry.setStatus("current")
_CfprFirmwareValidationStatusFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprFirmwareValidationStatusFsmStageStageStatus_Object = MibTableColumn
cfprFirmwareValidationStatusFsmStageStageStatus = _CfprFirmwareValidationStatusFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 71, 1, 9),
    _CfprFirmwareValidationStatusFsmStageStageStatus_Type()
)
cfprFirmwareValidationStatusFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmStageStageStatus.setStatus("current")
_CfprFirmwareValidationStatusFsmTaskTable_Object = MibTable
cfprFirmwareValidationStatusFsmTaskTable = _CfprFirmwareValidationStatusFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 72)
)
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmTaskTable.setStatus("current")
_CfprFirmwareValidationStatusFsmTaskEntry_Object = MibTableRow
cfprFirmwareValidationStatusFsmTaskEntry = _CfprFirmwareValidationStatusFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 72, 1)
)
cfprFirmwareValidationStatusFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareValidationStatusFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmTaskEntry.setStatus("current")
_CfprFirmwareValidationStatusFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprFirmwareValidationStatusFsmTaskInstanceId_Object = MibTableColumn
cfprFirmwareValidationStatusFsmTaskInstanceId = _CfprFirmwareValidationStatusFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 72, 1, 1),
    _CfprFirmwareValidationStatusFsmTaskInstanceId_Type()
)
cfprFirmwareValidationStatusFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmTaskInstanceId.setStatus("current")
_CfprFirmwareValidationStatusFsmTaskDn_Type = CfprManagedObjectDn
_CfprFirmwareValidationStatusFsmTaskDn_Object = MibTableColumn
cfprFirmwareValidationStatusFsmTaskDn = _CfprFirmwareValidationStatusFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 72, 1, 2),
    _CfprFirmwareValidationStatusFsmTaskDn_Type()
)
cfprFirmwareValidationStatusFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmTaskDn.setStatus("current")
_CfprFirmwareValidationStatusFsmTaskRn_Type = SnmpAdminString
_CfprFirmwareValidationStatusFsmTaskRn_Object = MibTableColumn
cfprFirmwareValidationStatusFsmTaskRn = _CfprFirmwareValidationStatusFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 72, 1, 3),
    _CfprFirmwareValidationStatusFsmTaskRn_Type()
)
cfprFirmwareValidationStatusFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmTaskRn.setStatus("current")
_CfprFirmwareValidationStatusFsmTaskCompletion_Type = CfprFsmCompletion
_CfprFirmwareValidationStatusFsmTaskCompletion_Object = MibTableColumn
cfprFirmwareValidationStatusFsmTaskCompletion = _CfprFirmwareValidationStatusFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 72, 1, 4),
    _CfprFirmwareValidationStatusFsmTaskCompletion_Type()
)
cfprFirmwareValidationStatusFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmTaskCompletion.setStatus("current")
_CfprFirmwareValidationStatusFsmTaskFlags_Type = CfprFirmwareValidationStatusFsmTaskFlags
_CfprFirmwareValidationStatusFsmTaskFlags_Object = MibTableColumn
cfprFirmwareValidationStatusFsmTaskFlags = _CfprFirmwareValidationStatusFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 72, 1, 5),
    _CfprFirmwareValidationStatusFsmTaskFlags_Type()
)
cfprFirmwareValidationStatusFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmTaskFlags.setStatus("current")
_CfprFirmwareValidationStatusFsmTaskItem_Type = CfprFirmwareValidationStatusFsmTaskItem
_CfprFirmwareValidationStatusFsmTaskItem_Object = MibTableColumn
cfprFirmwareValidationStatusFsmTaskItem = _CfprFirmwareValidationStatusFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 72, 1, 6),
    _CfprFirmwareValidationStatusFsmTaskItem_Type()
)
cfprFirmwareValidationStatusFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmTaskItem.setStatus("current")
_CfprFirmwareValidationStatusFsmTaskSeqId_Type = Gauge32
_CfprFirmwareValidationStatusFsmTaskSeqId_Object = MibTableColumn
cfprFirmwareValidationStatusFsmTaskSeqId = _CfprFirmwareValidationStatusFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 72, 1, 7),
    _CfprFirmwareValidationStatusFsmTaskSeqId_Type()
)
cfprFirmwareValidationStatusFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareValidationStatusFsmTaskSeqId.setStatus("current")
_CfprFirmwareActivateIssueTable_Object = MibTable
cfprFirmwareActivateIssueTable = _CfprFirmwareActivateIssueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 73)
)
if mibBuilder.loadTexts:
    cfprFirmwareActivateIssueTable.setStatus("current")
_CfprFirmwareActivateIssueEntry_Object = MibTableRow
cfprFirmwareActivateIssueEntry = _CfprFirmwareActivateIssueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 73, 1)
)
cfprFirmwareActivateIssueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareActivateIssueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareActivateIssueEntry.setStatus("current")
_CfprFirmwareActivateIssueInstanceId_Type = CfprManagedObjectId
_CfprFirmwareActivateIssueInstanceId_Object = MibTableColumn
cfprFirmwareActivateIssueInstanceId = _CfprFirmwareActivateIssueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 73, 1, 1),
    _CfprFirmwareActivateIssueInstanceId_Type()
)
cfprFirmwareActivateIssueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareActivateIssueInstanceId.setStatus("current")
_CfprFirmwareActivateIssueDn_Type = CfprManagedObjectDn
_CfprFirmwareActivateIssueDn_Object = MibTableColumn
cfprFirmwareActivateIssueDn = _CfprFirmwareActivateIssueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 73, 1, 2),
    _CfprFirmwareActivateIssueDn_Type()
)
cfprFirmwareActivateIssueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareActivateIssueDn.setStatus("current")
_CfprFirmwareActivateIssueRn_Type = SnmpAdminString
_CfprFirmwareActivateIssueRn_Object = MibTableColumn
cfprFirmwareActivateIssueRn = _CfprFirmwareActivateIssueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 73, 1, 3),
    _CfprFirmwareActivateIssueRn_Type()
)
cfprFirmwareActivateIssueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareActivateIssueRn.setStatus("current")
_CfprFirmwareActivateIssueIsActivationRequired_Type = TruthValue
_CfprFirmwareActivateIssueIsActivationRequired_Object = MibTableColumn
cfprFirmwareActivateIssueIsActivationRequired = _CfprFirmwareActivateIssueIsActivationRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 73, 1, 4),
    _CfprFirmwareActivateIssueIsActivationRequired_Type()
)
cfprFirmwareActivateIssueIsActivationRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareActivateIssueIsActivationRequired.setStatus("current")
_CfprFirmwareMgrVersionMismatchTable_Object = MibTable
cfprFirmwareMgrVersionMismatchTable = _CfprFirmwareMgrVersionMismatchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 74)
)
if mibBuilder.loadTexts:
    cfprFirmwareMgrVersionMismatchTable.setStatus("current")
_CfprFirmwareMgrVersionMismatchEntry_Object = MibTableRow
cfprFirmwareMgrVersionMismatchEntry = _CfprFirmwareMgrVersionMismatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 74, 1)
)
cfprFirmwareMgrVersionMismatchEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareMgrVersionMismatchInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareMgrVersionMismatchEntry.setStatus("current")
_CfprFirmwareMgrVersionMismatchInstanceId_Type = CfprManagedObjectId
_CfprFirmwareMgrVersionMismatchInstanceId_Object = MibTableColumn
cfprFirmwareMgrVersionMismatchInstanceId = _CfprFirmwareMgrVersionMismatchInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 74, 1, 1),
    _CfprFirmwareMgrVersionMismatchInstanceId_Type()
)
cfprFirmwareMgrVersionMismatchInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareMgrVersionMismatchInstanceId.setStatus("current")
_CfprFirmwareMgrVersionMismatchDn_Type = CfprManagedObjectDn
_CfprFirmwareMgrVersionMismatchDn_Object = MibTableColumn
cfprFirmwareMgrVersionMismatchDn = _CfprFirmwareMgrVersionMismatchDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 74, 1, 2),
    _CfprFirmwareMgrVersionMismatchDn_Type()
)
cfprFirmwareMgrVersionMismatchDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareMgrVersionMismatchDn.setStatus("current")
_CfprFirmwareMgrVersionMismatchRn_Type = SnmpAdminString
_CfprFirmwareMgrVersionMismatchRn_Object = MibTableColumn
cfprFirmwareMgrVersionMismatchRn = _CfprFirmwareMgrVersionMismatchRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 74, 1, 3),
    _CfprFirmwareMgrVersionMismatchRn_Type()
)
cfprFirmwareMgrVersionMismatchRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareMgrVersionMismatchRn.setStatus("current")
_CfprFirmwareMgrVersionMismatchIsMgrVersionMismatch_Type = TruthValue
_CfprFirmwareMgrVersionMismatchIsMgrVersionMismatch_Object = MibTableColumn
cfprFirmwareMgrVersionMismatchIsMgrVersionMismatch = _CfprFirmwareMgrVersionMismatchIsMgrVersionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 74, 1, 4),
    _CfprFirmwareMgrVersionMismatchIsMgrVersionMismatch_Type()
)
cfprFirmwareMgrVersionMismatchIsMgrVersionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareMgrVersionMismatchIsMgrVersionMismatch.setStatus("current")
_CfprFirmwareVersionIssueTable_Object = MibTable
cfprFirmwareVersionIssueTable = _CfprFirmwareVersionIssueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 75)
)
if mibBuilder.loadTexts:
    cfprFirmwareVersionIssueTable.setStatus("current")
_CfprFirmwareVersionIssueEntry_Object = MibTableRow
cfprFirmwareVersionIssueEntry = _CfprFirmwareVersionIssueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 75, 1)
)
cfprFirmwareVersionIssueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FIRMWARE-MIB", "cfprFirmwareVersionIssueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFirmwareVersionIssueEntry.setStatus("current")
_CfprFirmwareVersionIssueInstanceId_Type = CfprManagedObjectId
_CfprFirmwareVersionIssueInstanceId_Object = MibTableColumn
cfprFirmwareVersionIssueInstanceId = _CfprFirmwareVersionIssueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 75, 1, 1),
    _CfprFirmwareVersionIssueInstanceId_Type()
)
cfprFirmwareVersionIssueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFirmwareVersionIssueInstanceId.setStatus("current")
_CfprFirmwareVersionIssueDn_Type = CfprManagedObjectDn
_CfprFirmwareVersionIssueDn_Object = MibTableColumn
cfprFirmwareVersionIssueDn = _CfprFirmwareVersionIssueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 75, 1, 2),
    _CfprFirmwareVersionIssueDn_Type()
)
cfprFirmwareVersionIssueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareVersionIssueDn.setStatus("current")
_CfprFirmwareVersionIssueRn_Type = SnmpAdminString
_CfprFirmwareVersionIssueRn_Object = MibTableColumn
cfprFirmwareVersionIssueRn = _CfprFirmwareVersionIssueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 75, 1, 3),
    _CfprFirmwareVersionIssueRn_Type()
)
cfprFirmwareVersionIssueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareVersionIssueRn.setStatus("current")
_CfprFirmwareVersionIssueInstalledImageVersion_Type = SnmpAdminString
_CfprFirmwareVersionIssueInstalledImageVersion_Object = MibTableColumn
cfprFirmwareVersionIssueInstalledImageVersion = _CfprFirmwareVersionIssueInstalledImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 75, 1, 4),
    _CfprFirmwareVersionIssueInstalledImageVersion_Type()
)
cfprFirmwareVersionIssueInstalledImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareVersionIssueInstalledImageVersion.setStatus("current")
_CfprFirmwareVersionIssueInstalledPackageVersion_Type = SnmpAdminString
_CfprFirmwareVersionIssueInstalledPackageVersion_Object = MibTableColumn
cfprFirmwareVersionIssueInstalledPackageVersion = _CfprFirmwareVersionIssueInstalledPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 75, 1, 5),
    _CfprFirmwareVersionIssueInstalledPackageVersion_Type()
)
cfprFirmwareVersionIssueInstalledPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareVersionIssueInstalledPackageVersion.setStatus("current")
_CfprFirmwareVersionIssueMismatchType_Type = SnmpAdminString
_CfprFirmwareVersionIssueMismatchType_Object = MibTableColumn
cfprFirmwareVersionIssueMismatchType = _CfprFirmwareVersionIssueMismatchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 30, 75, 1, 6),
    _CfprFirmwareVersionIssueMismatchType_Type()
)
cfprFirmwareVersionIssueMismatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFirmwareVersionIssueMismatchType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-FIRMWARE-MIB",
    **{"cfprFirmwareObjects": cfprFirmwareObjects,
       "cfprFirmwareAckTable": cfprFirmwareAckTable,
       "cfprFirmwareAckEntry": cfprFirmwareAckEntry,
       "cfprFirmwareAckInstanceId": cfprFirmwareAckInstanceId,
       "cfprFirmwareAckDn": cfprFirmwareAckDn,
       "cfprFirmwareAckRn": cfprFirmwareAckRn,
       "cfprFirmwareAckAcked": cfprFirmwareAckAcked,
       "cfprFirmwareAckAckedBy": cfprFirmwareAckAckedBy,
       "cfprFirmwareAckAdminState": cfprFirmwareAckAdminState,
       "cfprFirmwareAckAutoDelete": cfprFirmwareAckAutoDelete,
       "cfprFirmwareAckChangeBy": cfprFirmwareAckChangeBy,
       "cfprFirmwareAckChangeDetails": cfprFirmwareAckChangeDetails,
       "cfprFirmwareAckChanges": cfprFirmwareAckChanges,
       "cfprFirmwareAckDescr": cfprFirmwareAckDescr,
       "cfprFirmwareAckDisr": cfprFirmwareAckDisr,
       "cfprFirmwareAckIgnoreCap": cfprFirmwareAckIgnoreCap,
       "cfprFirmwareAckIntId": cfprFirmwareAckIntId,
       "cfprFirmwareAckModified": cfprFirmwareAckModified,
       "cfprFirmwareAckName": cfprFirmwareAckName,
       "cfprFirmwareAckOperScheduler": cfprFirmwareAckOperScheduler,
       "cfprFirmwareAckOperState": cfprFirmwareAckOperState,
       "cfprFirmwareAckPolicyLevel": cfprFirmwareAckPolicyLevel,
       "cfprFirmwareAckPolicyOwner": cfprFirmwareAckPolicyOwner,
       "cfprFirmwareAckPrevOperState": cfprFirmwareAckPrevOperState,
       "cfprFirmwareAckScheduler": cfprFirmwareAckScheduler,
       "cfprFirmwareAutoSyncPolicyTable": cfprFirmwareAutoSyncPolicyTable,
       "cfprFirmwareAutoSyncPolicyEntry": cfprFirmwareAutoSyncPolicyEntry,
       "cfprFirmwareAutoSyncPolicyInstanceId": cfprFirmwareAutoSyncPolicyInstanceId,
       "cfprFirmwareAutoSyncPolicyDn": cfprFirmwareAutoSyncPolicyDn,
       "cfprFirmwareAutoSyncPolicyRn": cfprFirmwareAutoSyncPolicyRn,
       "cfprFirmwareAutoSyncPolicyConfigIssue": cfprFirmwareAutoSyncPolicyConfigIssue,
       "cfprFirmwareAutoSyncPolicyDescr": cfprFirmwareAutoSyncPolicyDescr,
       "cfprFirmwareAutoSyncPolicyIntId": cfprFirmwareAutoSyncPolicyIntId,
       "cfprFirmwareAutoSyncPolicyName": cfprFirmwareAutoSyncPolicyName,
       "cfprFirmwareAutoSyncPolicyPolicyLevel": cfprFirmwareAutoSyncPolicyPolicyLevel,
       "cfprFirmwareAutoSyncPolicyPolicyOwner": cfprFirmwareAutoSyncPolicyPolicyOwner,
       "cfprFirmwareAutoSyncPolicySyncState": cfprFirmwareAutoSyncPolicySyncState,
       "cfprFirmwareBladeTable": cfprFirmwareBladeTable,
       "cfprFirmwareBladeEntry": cfprFirmwareBladeEntry,
       "cfprFirmwareBladeInstanceId": cfprFirmwareBladeInstanceId,
       "cfprFirmwareBladeDn": cfprFirmwareBladeDn,
       "cfprFirmwareBladeRn": cfprFirmwareBladeRn,
       "cfprFirmwareBladeOperVersion": cfprFirmwareBladeOperVersion,
       "cfprFirmwareBootDefinitionTable": cfprFirmwareBootDefinitionTable,
       "cfprFirmwareBootDefinitionEntry": cfprFirmwareBootDefinitionEntry,
       "cfprFirmwareBootDefinitionInstanceId": cfprFirmwareBootDefinitionInstanceId,
       "cfprFirmwareBootDefinitionDn": cfprFirmwareBootDefinitionDn,
       "cfprFirmwareBootDefinitionRn": cfprFirmwareBootDefinitionRn,
       "cfprFirmwareBootDefinitionType": cfprFirmwareBootDefinitionType,
       "cfprFirmwareBootUnitTable": cfprFirmwareBootUnitTable,
       "cfprFirmwareBootUnitEntry": cfprFirmwareBootUnitEntry,
       "cfprFirmwareBootUnitInstanceId": cfprFirmwareBootUnitInstanceId,
       "cfprFirmwareBootUnitDn": cfprFirmwareBootUnitDn,
       "cfprFirmwareBootUnitRn": cfprFirmwareBootUnitRn,
       "cfprFirmwareBootUnitAdminState": cfprFirmwareBootUnitAdminState,
       "cfprFirmwareBootUnitIgnoreCompCheck": cfprFirmwareBootUnitIgnoreCompCheck,
       "cfprFirmwareBootUnitImage": cfprFirmwareBootUnitImage,
       "cfprFirmwareBootUnitInvTag": cfprFirmwareBootUnitInvTag,
       "cfprFirmwareBootUnitMode": cfprFirmwareBootUnitMode,
       "cfprFirmwareBootUnitOperState": cfprFirmwareBootUnitOperState,
       "cfprFirmwareBootUnitPrevVersion": cfprFirmwareBootUnitPrevVersion,
       "cfprFirmwareBootUnitResetOnActivate": cfprFirmwareBootUnitResetOnActivate,
       "cfprFirmwareBootUnitSkipValidation": cfprFirmwareBootUnitSkipValidation,
       "cfprFirmwareBootUnitType": cfprFirmwareBootUnitType,
       "cfprFirmwareBootUnitVersion": cfprFirmwareBootUnitVersion,
       "cfprFirmwareBootUnitMioSsdmodel": cfprFirmwareBootUnitMioSsdmodel,
       "cfprFirmwareBundleInfoTable": cfprFirmwareBundleInfoTable,
       "cfprFirmwareBundleInfoEntry": cfprFirmwareBundleInfoEntry,
       "cfprFirmwareBundleInfoInstanceId": cfprFirmwareBundleInfoInstanceId,
       "cfprFirmwareBundleInfoDn": cfprFirmwareBundleInfoDn,
       "cfprFirmwareBundleInfoRn": cfprFirmwareBundleInfoRn,
       "cfprFirmwareBundleInfoType": cfprFirmwareBundleInfoType,
       "cfprFirmwareBundleInfoVersion": cfprFirmwareBundleInfoVersion,
       "cfprFirmwareBundleInfoSecModelSupported": cfprFirmwareBundleInfoSecModelSupported,
       "cfprFirmwareBundleInfoDigestTable": cfprFirmwareBundleInfoDigestTable,
       "cfprFirmwareBundleInfoDigestEntry": cfprFirmwareBundleInfoDigestEntry,
       "cfprFirmwareBundleInfoDigestInstanceId": cfprFirmwareBundleInfoDigestInstanceId,
       "cfprFirmwareBundleInfoDigestDn": cfprFirmwareBundleInfoDigestDn,
       "cfprFirmwareBundleInfoDigestRn": cfprFirmwareBundleInfoDigestRn,
       "cfprFirmwareBundleInfoDigestBundleName": cfprFirmwareBundleInfoDigestBundleName,
       "cfprFirmwareBundleInfoDigestType": cfprFirmwareBundleInfoDigestType,
       "cfprFirmwareBundleInfoDigestVersion": cfprFirmwareBundleInfoDigestVersion,
       "cfprFirmwareBundleTypeTable": cfprFirmwareBundleTypeTable,
       "cfprFirmwareBundleTypeEntry": cfprFirmwareBundleTypeEntry,
       "cfprFirmwareBundleTypeInstanceId": cfprFirmwareBundleTypeInstanceId,
       "cfprFirmwareBundleTypeDn": cfprFirmwareBundleTypeDn,
       "cfprFirmwareBundleTypeRn": cfprFirmwareBundleTypeRn,
       "cfprFirmwareBundleTypeInvTag": cfprFirmwareBundleTypeInvTag,
       "cfprFirmwareBundleTypeType": cfprFirmwareBundleTypeType,
       "cfprFirmwareBundleTypeCapProviderTable": cfprFirmwareBundleTypeCapProviderTable,
       "cfprFirmwareBundleTypeCapProviderEntry": cfprFirmwareBundleTypeCapProviderEntry,
       "cfprFirmwareBundleTypeCapProviderInstanceId": cfprFirmwareBundleTypeCapProviderInstanceId,
       "cfprFirmwareBundleTypeCapProviderDn": cfprFirmwareBundleTypeCapProviderDn,
       "cfprFirmwareBundleTypeCapProviderRn": cfprFirmwareBundleTypeCapProviderRn,
       "cfprFirmwareBundleTypeCapProviderDeleted": cfprFirmwareBundleTypeCapProviderDeleted,
       "cfprFirmwareBundleTypeCapProviderDeprecated": cfprFirmwareBundleTypeCapProviderDeprecated,
       "cfprFirmwareBundleTypeCapProviderElementLoadFailures": cfprFirmwareBundleTypeCapProviderElementLoadFailures,
       "cfprFirmwareBundleTypeCapProviderElementsLoaded": cfprFirmwareBundleTypeCapProviderElementsLoaded,
       "cfprFirmwareBundleTypeCapProviderGencount": cfprFirmwareBundleTypeCapProviderGencount,
       "cfprFirmwareBundleTypeCapProviderLoadErrors": cfprFirmwareBundleTypeCapProviderLoadErrors,
       "cfprFirmwareBundleTypeCapProviderLoadWarnings": cfprFirmwareBundleTypeCapProviderLoadWarnings,
       "cfprFirmwareBundleTypeCapProviderMgmtPlaneVer": cfprFirmwareBundleTypeCapProviderMgmtPlaneVer,
       "cfprFirmwareBundleTypeCapProviderModel": cfprFirmwareBundleTypeCapProviderModel,
       "cfprFirmwareBundleTypeCapProviderPlatformType": cfprFirmwareBundleTypeCapProviderPlatformType,
       "cfprFirmwareBundleTypeCapProviderVendor": cfprFirmwareBundleTypeCapProviderVendor,
       "cfprFirmwareCatalogPackTable": cfprFirmwareCatalogPackTable,
       "cfprFirmwareCatalogPackEntry": cfprFirmwareCatalogPackEntry,
       "cfprFirmwareCatalogPackInstanceId": cfprFirmwareCatalogPackInstanceId,
       "cfprFirmwareCatalogPackDn": cfprFirmwareCatalogPackDn,
       "cfprFirmwareCatalogPackRn": cfprFirmwareCatalogPackRn,
       "cfprFirmwareCatalogPackCatalogName": cfprFirmwareCatalogPackCatalogName,
       "cfprFirmwareCatalogPackCatalogVersion": cfprFirmwareCatalogPackCatalogVersion,
       "cfprFirmwareCatalogPackConfigState": cfprFirmwareCatalogPackConfigState,
       "cfprFirmwareCatalogPackConfigStatusMessage": cfprFirmwareCatalogPackConfigStatusMessage,
       "cfprFirmwareCatalogPackDescr": cfprFirmwareCatalogPackDescr,
       "cfprFirmwareCatalogPackIntId": cfprFirmwareCatalogPackIntId,
       "cfprFirmwareCatalogPackMode": cfprFirmwareCatalogPackMode,
       "cfprFirmwareCatalogPackName": cfprFirmwareCatalogPackName,
       "cfprFirmwareCatalogPackPolicyLevel": cfprFirmwareCatalogPackPolicyLevel,
       "cfprFirmwareCatalogPackPolicyOwner": cfprFirmwareCatalogPackPolicyOwner,
       "cfprFirmwareCatalogPackStageSize": cfprFirmwareCatalogPackStageSize,
       "cfprFirmwareCatalogPackUpdateTrigger": cfprFirmwareCatalogPackUpdateTrigger,
       "cfprFirmwareCatalogueTable": cfprFirmwareCatalogueTable,
       "cfprFirmwareCatalogueEntry": cfprFirmwareCatalogueEntry,
       "cfprFirmwareCatalogueInstanceId": cfprFirmwareCatalogueInstanceId,
       "cfprFirmwareCatalogueDn": cfprFirmwareCatalogueDn,
       "cfprFirmwareCatalogueRn": cfprFirmwareCatalogueRn,
       "cfprFirmwareCatalogueSyncTrigger": cfprFirmwareCatalogueSyncTrigger,
       "cfprFirmwareCompSourceTable": cfprFirmwareCompSourceTable,
       "cfprFirmwareCompSourceEntry": cfprFirmwareCompSourceEntry,
       "cfprFirmwareCompSourceInstanceId": cfprFirmwareCompSourceInstanceId,
       "cfprFirmwareCompSourceDn": cfprFirmwareCompSourceDn,
       "cfprFirmwareCompSourceRn": cfprFirmwareCompSourceRn,
       "cfprFirmwareCompSourceDescr": cfprFirmwareCompSourceDescr,
       "cfprFirmwareCompSourceIntId": cfprFirmwareCompSourceIntId,
       "cfprFirmwareCompSourceInvTag": cfprFirmwareCompSourceInvTag,
       "cfprFirmwareCompSourceName": cfprFirmwareCompSourceName,
       "cfprFirmwareCompSourcePolicyLevel": cfprFirmwareCompSourcePolicyLevel,
       "cfprFirmwareCompSourcePolicyOwner": cfprFirmwareCompSourcePolicyOwner,
       "cfprFirmwareCompSourceVersion": cfprFirmwareCompSourceVersion,
       "cfprFirmwareCompTargetTable": cfprFirmwareCompTargetTable,
       "cfprFirmwareCompTargetEntry": cfprFirmwareCompTargetEntry,
       "cfprFirmwareCompTargetInstanceId": cfprFirmwareCompTargetInstanceId,
       "cfprFirmwareCompTargetDn": cfprFirmwareCompTargetDn,
       "cfprFirmwareCompTargetRn": cfprFirmwareCompTargetRn,
       "cfprFirmwareCompTargetDescr": cfprFirmwareCompTargetDescr,
       "cfprFirmwareCompTargetIntId": cfprFirmwareCompTargetIntId,
       "cfprFirmwareCompTargetInvTag": cfprFirmwareCompTargetInvTag,
       "cfprFirmwareCompTargetName": cfprFirmwareCompTargetName,
       "cfprFirmwareCompTargetPolicyLevel": cfprFirmwareCompTargetPolicyLevel,
       "cfprFirmwareCompTargetPolicyOwner": cfprFirmwareCompTargetPolicyOwner,
       "cfprFirmwareCompTargetVersion": cfprFirmwareCompTargetVersion,
       "cfprFirmwareComputeHostPackTable": cfprFirmwareComputeHostPackTable,
       "cfprFirmwareComputeHostPackEntry": cfprFirmwareComputeHostPackEntry,
       "cfprFirmwareComputeHostPackInstanceId": cfprFirmwareComputeHostPackInstanceId,
       "cfprFirmwareComputeHostPackDn": cfprFirmwareComputeHostPackDn,
       "cfprFirmwareComputeHostPackRn": cfprFirmwareComputeHostPackRn,
       "cfprFirmwareComputeHostPackBladeBundleName": cfprFirmwareComputeHostPackBladeBundleName,
       "cfprFirmwareComputeHostPackBladeBundleVersion": cfprFirmwareComputeHostPackBladeBundleVersion,
       "cfprFirmwareComputeHostPackConfigQualifier": cfprFirmwareComputeHostPackConfigQualifier,
       "cfprFirmwareComputeHostPackDescr": cfprFirmwareComputeHostPackDescr,
       "cfprFirmwareComputeHostPackIgnoreCompCheck": cfprFirmwareComputeHostPackIgnoreCompCheck,
       "cfprFirmwareComputeHostPackIntId": cfprFirmwareComputeHostPackIntId,
       "cfprFirmwareComputeHostPackMode": cfprFirmwareComputeHostPackMode,
       "cfprFirmwareComputeHostPackName": cfprFirmwareComputeHostPackName,
       "cfprFirmwareComputeHostPackPlatformBundleVersion": cfprFirmwareComputeHostPackPlatformBundleVersion,
       "cfprFirmwareComputeHostPackPolicyLevel": cfprFirmwareComputeHostPackPolicyLevel,
       "cfprFirmwareComputeHostPackPolicyOwner": cfprFirmwareComputeHostPackPolicyOwner,
       "cfprFirmwareComputeHostPackRackBundleName": cfprFirmwareComputeHostPackRackBundleName,
       "cfprFirmwareComputeHostPackRackBundleVersion": cfprFirmwareComputeHostPackRackBundleVersion,
       "cfprFirmwareComputeHostPackStageSize": cfprFirmwareComputeHostPackStageSize,
       "cfprFirmwareComputeHostPackUpdateTrigger": cfprFirmwareComputeHostPackUpdateTrigger,
       "cfprFirmwareComputeMgmtPackTable": cfprFirmwareComputeMgmtPackTable,
       "cfprFirmwareComputeMgmtPackEntry": cfprFirmwareComputeMgmtPackEntry,
       "cfprFirmwareComputeMgmtPackInstanceId": cfprFirmwareComputeMgmtPackInstanceId,
       "cfprFirmwareComputeMgmtPackDn": cfprFirmwareComputeMgmtPackDn,
       "cfprFirmwareComputeMgmtPackRn": cfprFirmwareComputeMgmtPackRn,
       "cfprFirmwareComputeMgmtPackDescr": cfprFirmwareComputeMgmtPackDescr,
       "cfprFirmwareComputeMgmtPackIgnoreCompCheck": cfprFirmwareComputeMgmtPackIgnoreCompCheck,
       "cfprFirmwareComputeMgmtPackIntId": cfprFirmwareComputeMgmtPackIntId,
       "cfprFirmwareComputeMgmtPackMode": cfprFirmwareComputeMgmtPackMode,
       "cfprFirmwareComputeMgmtPackName": cfprFirmwareComputeMgmtPackName,
       "cfprFirmwareComputeMgmtPackPolicyLevel": cfprFirmwareComputeMgmtPackPolicyLevel,
       "cfprFirmwareComputeMgmtPackPolicyOwner": cfprFirmwareComputeMgmtPackPolicyOwner,
       "cfprFirmwareComputeMgmtPackStageSize": cfprFirmwareComputeMgmtPackStageSize,
       "cfprFirmwareComputeMgmtPackUpdateTrigger": cfprFirmwareComputeMgmtPackUpdateTrigger,
       "cfprFirmwareConstraintTable": cfprFirmwareConstraintTable,
       "cfprFirmwareConstraintEntry": cfprFirmwareConstraintEntry,
       "cfprFirmwareConstraintInstanceId": cfprFirmwareConstraintInstanceId,
       "cfprFirmwareConstraintDn": cfprFirmwareConstraintDn,
       "cfprFirmwareConstraintRn": cfprFirmwareConstraintRn,
       "cfprFirmwareConstraintFeature": cfprFirmwareConstraintFeature,
       "cfprFirmwareConstraintMinBiosVersion": cfprFirmwareConstraintMinBiosVersion,
       "cfprFirmwareConstraintMinCimcVersion": cfprFirmwareConstraintMinCimcVersion,
       "cfprFirmwareConstraintsTable": cfprFirmwareConstraintsTable,
       "cfprFirmwareConstraintsEntry": cfprFirmwareConstraintsEntry,
       "cfprFirmwareConstraintsInstanceId": cfprFirmwareConstraintsInstanceId,
       "cfprFirmwareConstraintsDn": cfprFirmwareConstraintsDn,
       "cfprFirmwareConstraintsRn": cfprFirmwareConstraintsRn,
       "cfprFirmwareDependencyTable": cfprFirmwareDependencyTable,
       "cfprFirmwareDependencyEntry": cfprFirmwareDependencyEntry,
       "cfprFirmwareDependencyInstanceId": cfprFirmwareDependencyInstanceId,
       "cfprFirmwareDependencyDn": cfprFirmwareDependencyDn,
       "cfprFirmwareDependencyRn": cfprFirmwareDependencyRn,
       "cfprFirmwareDependencyEp": cfprFirmwareDependencyEp,
       "cfprFirmwareDependencyHwModel": cfprFirmwareDependencyHwModel,
       "cfprFirmwareDependencyHwRevision": cfprFirmwareDependencyHwRevision,
       "cfprFirmwareDependencyHwVendor": cfprFirmwareDependencyHwVendor,
       "cfprFirmwareDependencyInvTag": cfprFirmwareDependencyInvTag,
       "cfprFirmwareDependencyMaxVer": cfprFirmwareDependencyMaxVer,
       "cfprFirmwareDependencyMinVer": cfprFirmwareDependencyMinVer,
       "cfprFirmwareDependencyRelationship": cfprFirmwareDependencyRelationship,
       "cfprFirmwareDependencyScope": cfprFirmwareDependencyScope,
       "cfprFirmwareDependencySensitivity": cfprFirmwareDependencySensitivity,
       "cfprFirmwareDependencyValidationStatus": cfprFirmwareDependencyValidationStatus,
       "cfprFirmwareDistImageTable": cfprFirmwareDistImageTable,
       "cfprFirmwareDistImageEntry": cfprFirmwareDistImageEntry,
       "cfprFirmwareDistImageInstanceId": cfprFirmwareDistImageInstanceId,
       "cfprFirmwareDistImageDn": cfprFirmwareDistImageDn,
       "cfprFirmwareDistImageRn": cfprFirmwareDistImageRn,
       "cfprFirmwareDistImageImageDeleted": cfprFirmwareDistImageImageDeleted,
       "cfprFirmwareDistImageName": cfprFirmwareDistImageName,
       "cfprFirmwareDistImageType": cfprFirmwareDistImageType,
       "cfprFirmwareDistributableTable": cfprFirmwareDistributableTable,
       "cfprFirmwareDistributableEntry": cfprFirmwareDistributableEntry,
       "cfprFirmwareDistributableInstanceId": cfprFirmwareDistributableInstanceId,
       "cfprFirmwareDistributableDn": cfprFirmwareDistributableDn,
       "cfprFirmwareDistributableRn": cfprFirmwareDistributableRn,
       "cfprFirmwareDistributableAdminState": cfprFirmwareDistributableAdminState,
       "cfprFirmwareDistributableCompleteness": cfprFirmwareDistributableCompleteness,
       "cfprFirmwareDistributableDescr": cfprFirmwareDistributableDescr,
       "cfprFirmwareDistributableFsmDescr": cfprFirmwareDistributableFsmDescr,
       "cfprFirmwareDistributableFsmPrev": cfprFirmwareDistributableFsmPrev,
       "cfprFirmwareDistributableFsmProgr": cfprFirmwareDistributableFsmProgr,
       "cfprFirmwareDistributableFsmRmtInvErrCode": cfprFirmwareDistributableFsmRmtInvErrCode,
       "cfprFirmwareDistributableFsmRmtInvErrDescr": cfprFirmwareDistributableFsmRmtInvErrDescr,
       "cfprFirmwareDistributableFsmRmtInvRslt": cfprFirmwareDistributableFsmRmtInvRslt,
       "cfprFirmwareDistributableFsmStageDescr": cfprFirmwareDistributableFsmStageDescr,
       "cfprFirmwareDistributableFsmStamp": cfprFirmwareDistributableFsmStamp,
       "cfprFirmwareDistributableFsmStatus": cfprFirmwareDistributableFsmStatus,
       "cfprFirmwareDistributableFsmTry": cfprFirmwareDistributableFsmTry,
       "cfprFirmwareDistributableImagePresence": cfprFirmwareDistributableImagePresence,
       "cfprFirmwareDistributableIntId": cfprFirmwareDistributableIntId,
       "cfprFirmwareDistributableInvTag": cfprFirmwareDistributableInvTag,
       "cfprFirmwareDistributableModel": cfprFirmwareDistributableModel,
       "cfprFirmwareDistributableName": cfprFirmwareDistributableName,
       "cfprFirmwareDistributablePolicyLevel": cfprFirmwareDistributablePolicyLevel,
       "cfprFirmwareDistributablePolicyOwner": cfprFirmwareDistributablePolicyOwner,
       "cfprFirmwareDistributableTransferState": cfprFirmwareDistributableTransferState,
       "cfprFirmwareDistributableType": cfprFirmwareDistributableType,
       "cfprFirmwareDistributableVendor": cfprFirmwareDistributableVendor,
       "cfprFirmwareDistributableVersion": cfprFirmwareDistributableVersion,
       "cfprFirmwareDistributableBuildDate": cfprFirmwareDistributableBuildDate,
       "cfprFirmwareDistributableDisplayFlag": cfprFirmwareDistributableDisplayFlag,
       "cfprFirmwareDistributableSupportsMultiInstance": cfprFirmwareDistributableSupportsMultiInstance,
       "cfprFirmwareDistributableTimeStamp": cfprFirmwareDistributableTimeStamp,
       "cfprFirmwareDistributableFsmTable": cfprFirmwareDistributableFsmTable,
       "cfprFirmwareDistributableFsmEntry": cfprFirmwareDistributableFsmEntry,
       "cfprFirmwareDistributableFsmInstanceId": cfprFirmwareDistributableFsmInstanceId,
       "cfprFirmwareDistributableFsmDn": cfprFirmwareDistributableFsmDn,
       "cfprFirmwareDistributableFsmRn": cfprFirmwareDistributableFsmRn,
       "cfprFirmwareDistributableFsmCompletionTime": cfprFirmwareDistributableFsmCompletionTime,
       "cfprFirmwareDistributableFsmCurrentFsm": cfprFirmwareDistributableFsmCurrentFsm,
       "cfprFirmwareDistributableFsmDescrData": cfprFirmwareDistributableFsmDescrData,
       "cfprFirmwareDistributableFsmFsmStatus": cfprFirmwareDistributableFsmFsmStatus,
       "cfprFirmwareDistributableFsmProgress": cfprFirmwareDistributableFsmProgress,
       "cfprFirmwareDistributableFsmRmtErrCode": cfprFirmwareDistributableFsmRmtErrCode,
       "cfprFirmwareDistributableFsmRmtErrDescr": cfprFirmwareDistributableFsmRmtErrDescr,
       "cfprFirmwareDistributableFsmRmtRslt": cfprFirmwareDistributableFsmRmtRslt,
       "cfprFirmwareDistributableFsmStageTable": cfprFirmwareDistributableFsmStageTable,
       "cfprFirmwareDistributableFsmStageEntry": cfprFirmwareDistributableFsmStageEntry,
       "cfprFirmwareDistributableFsmStageInstanceId": cfprFirmwareDistributableFsmStageInstanceId,
       "cfprFirmwareDistributableFsmStageDn": cfprFirmwareDistributableFsmStageDn,
       "cfprFirmwareDistributableFsmStageRn": cfprFirmwareDistributableFsmStageRn,
       "cfprFirmwareDistributableFsmStageDescrData": cfprFirmwareDistributableFsmStageDescrData,
       "cfprFirmwareDistributableFsmStageLastUpdateTime": cfprFirmwareDistributableFsmStageLastUpdateTime,
       "cfprFirmwareDistributableFsmStageName": cfprFirmwareDistributableFsmStageName,
       "cfprFirmwareDistributableFsmStageOrder": cfprFirmwareDistributableFsmStageOrder,
       "cfprFirmwareDistributableFsmStageRetry": cfprFirmwareDistributableFsmStageRetry,
       "cfprFirmwareDistributableFsmStageStageStatus": cfprFirmwareDistributableFsmStageStageStatus,
       "cfprFirmwareDistributableFsmTaskTable": cfprFirmwareDistributableFsmTaskTable,
       "cfprFirmwareDistributableFsmTaskEntry": cfprFirmwareDistributableFsmTaskEntry,
       "cfprFirmwareDistributableFsmTaskInstanceId": cfprFirmwareDistributableFsmTaskInstanceId,
       "cfprFirmwareDistributableFsmTaskDn": cfprFirmwareDistributableFsmTaskDn,
       "cfprFirmwareDistributableFsmTaskRn": cfprFirmwareDistributableFsmTaskRn,
       "cfprFirmwareDistributableFsmTaskCompletion": cfprFirmwareDistributableFsmTaskCompletion,
       "cfprFirmwareDistributableFsmTaskFlags": cfprFirmwareDistributableFsmTaskFlags,
       "cfprFirmwareDistributableFsmTaskItem": cfprFirmwareDistributableFsmTaskItem,
       "cfprFirmwareDistributableFsmTaskSeqId": cfprFirmwareDistributableFsmTaskSeqId,
       "cfprFirmwareDownloaderTable": cfprFirmwareDownloaderTable,
       "cfprFirmwareDownloaderEntry": cfprFirmwareDownloaderEntry,
       "cfprFirmwareDownloaderInstanceId": cfprFirmwareDownloaderInstanceId,
       "cfprFirmwareDownloaderDn": cfprFirmwareDownloaderDn,
       "cfprFirmwareDownloaderRn": cfprFirmwareDownloaderRn,
       "cfprFirmwareDownloaderAdminState": cfprFirmwareDownloaderAdminState,
       "cfprFirmwareDownloaderFileName": cfprFirmwareDownloaderFileName,
       "cfprFirmwareDownloaderFsmDescr": cfprFirmwareDownloaderFsmDescr,
       "cfprFirmwareDownloaderFsmPrev": cfprFirmwareDownloaderFsmPrev,
       "cfprFirmwareDownloaderFsmProgr": cfprFirmwareDownloaderFsmProgr,
       "cfprFirmwareDownloaderFsmRmtInvErrCode": cfprFirmwareDownloaderFsmRmtInvErrCode,
       "cfprFirmwareDownloaderFsmRmtInvErrDescr": cfprFirmwareDownloaderFsmRmtInvErrDescr,
       "cfprFirmwareDownloaderFsmRmtInvRslt": cfprFirmwareDownloaderFsmRmtInvRslt,
       "cfprFirmwareDownloaderFsmStageDescr": cfprFirmwareDownloaderFsmStageDescr,
       "cfprFirmwareDownloaderFsmStamp": cfprFirmwareDownloaderFsmStamp,
       "cfprFirmwareDownloaderFsmStatus": cfprFirmwareDownloaderFsmStatus,
       "cfprFirmwareDownloaderFsmTry": cfprFirmwareDownloaderFsmTry,
       "cfprFirmwareDownloaderImageSize": cfprFirmwareDownloaderImageSize,
       "cfprFirmwareDownloaderProtocol": cfprFirmwareDownloaderProtocol,
       "cfprFirmwareDownloaderPwd": cfprFirmwareDownloaderPwd,
       "cfprFirmwareDownloaderRemotePath": cfprFirmwareDownloaderRemotePath,
       "cfprFirmwareDownloaderServer": cfprFirmwareDownloaderServer,
       "cfprFirmwareDownloaderTransferState": cfprFirmwareDownloaderTransferState,
       "cfprFirmwareDownloaderUser": cfprFirmwareDownloaderUser,
       "cfprFirmwareDownloaderTimeStamp": cfprFirmwareDownloaderTimeStamp,
       "cfprFirmwareDownloaderMsgStatus": cfprFirmwareDownloaderMsgStatus,
       "cfprFirmwareDownloaderPort": cfprFirmwareDownloaderPort,
       "cfprFirmwareDownloaderStartTime": cfprFirmwareDownloaderStartTime,
       "cfprFirmwareDownloaderTransferRate": cfprFirmwareDownloaderTransferRate,
       "cfprFirmwareDownloaderSilent": cfprFirmwareDownloaderSilent,
       "cfprFirmwareDownloaderTtyName": cfprFirmwareDownloaderTtyName,
       "cfprFirmwareDownloaderFsmTable": cfprFirmwareDownloaderFsmTable,
       "cfprFirmwareDownloaderFsmEntry": cfprFirmwareDownloaderFsmEntry,
       "cfprFirmwareDownloaderFsmInstanceId": cfprFirmwareDownloaderFsmInstanceId,
       "cfprFirmwareDownloaderFsmDn": cfprFirmwareDownloaderFsmDn,
       "cfprFirmwareDownloaderFsmRn": cfprFirmwareDownloaderFsmRn,
       "cfprFirmwareDownloaderFsmCompletionTime": cfprFirmwareDownloaderFsmCompletionTime,
       "cfprFirmwareDownloaderFsmCurrentFsm": cfprFirmwareDownloaderFsmCurrentFsm,
       "cfprFirmwareDownloaderFsmDescrData": cfprFirmwareDownloaderFsmDescrData,
       "cfprFirmwareDownloaderFsmFsmStatus": cfprFirmwareDownloaderFsmFsmStatus,
       "cfprFirmwareDownloaderFsmProgress": cfprFirmwareDownloaderFsmProgress,
       "cfprFirmwareDownloaderFsmRmtErrCode": cfprFirmwareDownloaderFsmRmtErrCode,
       "cfprFirmwareDownloaderFsmRmtErrDescr": cfprFirmwareDownloaderFsmRmtErrDescr,
       "cfprFirmwareDownloaderFsmRmtRslt": cfprFirmwareDownloaderFsmRmtRslt,
       "cfprFirmwareDownloaderFsmStageTable": cfprFirmwareDownloaderFsmStageTable,
       "cfprFirmwareDownloaderFsmStageEntry": cfprFirmwareDownloaderFsmStageEntry,
       "cfprFirmwareDownloaderFsmStageInstanceId": cfprFirmwareDownloaderFsmStageInstanceId,
       "cfprFirmwareDownloaderFsmStageDn": cfprFirmwareDownloaderFsmStageDn,
       "cfprFirmwareDownloaderFsmStageRn": cfprFirmwareDownloaderFsmStageRn,
       "cfprFirmwareDownloaderFsmStageDescrData": cfprFirmwareDownloaderFsmStageDescrData,
       "cfprFirmwareDownloaderFsmStageLastUpdateTime": cfprFirmwareDownloaderFsmStageLastUpdateTime,
       "cfprFirmwareDownloaderFsmStageName": cfprFirmwareDownloaderFsmStageName,
       "cfprFirmwareDownloaderFsmStageOrder": cfprFirmwareDownloaderFsmStageOrder,
       "cfprFirmwareDownloaderFsmStageRetry": cfprFirmwareDownloaderFsmStageRetry,
       "cfprFirmwareDownloaderFsmStageStageStatus": cfprFirmwareDownloaderFsmStageStageStatus,
       "cfprFirmwareDownloaderFsmTaskTable": cfprFirmwareDownloaderFsmTaskTable,
       "cfprFirmwareDownloaderFsmTaskEntry": cfprFirmwareDownloaderFsmTaskEntry,
       "cfprFirmwareDownloaderFsmTaskInstanceId": cfprFirmwareDownloaderFsmTaskInstanceId,
       "cfprFirmwareDownloaderFsmTaskDn": cfprFirmwareDownloaderFsmTaskDn,
       "cfprFirmwareDownloaderFsmTaskRn": cfprFirmwareDownloaderFsmTaskRn,
       "cfprFirmwareDownloaderFsmTaskCompletion": cfprFirmwareDownloaderFsmTaskCompletion,
       "cfprFirmwareDownloaderFsmTaskFlags": cfprFirmwareDownloaderFsmTaskFlags,
       "cfprFirmwareDownloaderFsmTaskItem": cfprFirmwareDownloaderFsmTaskItem,
       "cfprFirmwareDownloaderFsmTaskSeqId": cfprFirmwareDownloaderFsmTaskSeqId,
       "cfprFirmwareHostTable": cfprFirmwareHostTable,
       "cfprFirmwareHostEntry": cfprFirmwareHostEntry,
       "cfprFirmwareHostInstanceId": cfprFirmwareHostInstanceId,
       "cfprFirmwareHostDn": cfprFirmwareHostDn,
       "cfprFirmwareHostRn": cfprFirmwareHostRn,
       "cfprFirmwareHostPackModImpactTable": cfprFirmwareHostPackModImpactTable,
       "cfprFirmwareHostPackModImpactEntry": cfprFirmwareHostPackModImpactEntry,
       "cfprFirmwareHostPackModImpactInstanceId": cfprFirmwareHostPackModImpactInstanceId,
       "cfprFirmwareHostPackModImpactDn": cfprFirmwareHostPackModImpactDn,
       "cfprFirmwareHostPackModImpactRn": cfprFirmwareHostPackModImpactRn,
       "cfprFirmwareHostPackModImpactKeyDn": cfprFirmwareHostPackModImpactKeyDn,
       "cfprFirmwareHostPackModImpactMaintPolicyDn": cfprFirmwareHostPackModImpactMaintPolicyDn,
       "cfprFirmwareHostPackModImpactPnDn": cfprFirmwareHostPackModImpactPnDn,
       "cfprFirmwareHostPackModImpactRebootPolicy": cfprFirmwareHostPackModImpactRebootPolicy,
       "cfprFirmwareHostPackModImpactServiceProfileDn": cfprFirmwareHostPackModImpactServiceProfileDn,
       "cfprFirmwareImageTable": cfprFirmwareImageTable,
       "cfprFirmwareImageEntry": cfprFirmwareImageEntry,
       "cfprFirmwareImageInstanceId": cfprFirmwareImageInstanceId,
       "cfprFirmwareImageDn": cfprFirmwareImageDn,
       "cfprFirmwareImageRn": cfprFirmwareImageRn,
       "cfprFirmwareImageAdminState": cfprFirmwareImageAdminState,
       "cfprFirmwareImageChecksum": cfprFirmwareImageChecksum,
       "cfprFirmwareImageDescr": cfprFirmwareImageDescr,
       "cfprFirmwareImageDownloadDate": cfprFirmwareImageDownloadDate,
       "cfprFirmwareImageFsmDescr": cfprFirmwareImageFsmDescr,
       "cfprFirmwareImageFsmPrev": cfprFirmwareImageFsmPrev,
       "cfprFirmwareImageFsmProgr": cfprFirmwareImageFsmProgr,
       "cfprFirmwareImageFsmRmtInvErrCode": cfprFirmwareImageFsmRmtInvErrCode,
       "cfprFirmwareImageFsmRmtInvErrDescr": cfprFirmwareImageFsmRmtInvErrDescr,
       "cfprFirmwareImageFsmRmtInvRslt": cfprFirmwareImageFsmRmtInvRslt,
       "cfprFirmwareImageFsmStageDescr": cfprFirmwareImageFsmStageDescr,
       "cfprFirmwareImageFsmStamp": cfprFirmwareImageFsmStamp,
       "cfprFirmwareImageFsmStatus": cfprFirmwareImageFsmStatus,
       "cfprFirmwareImageFsmTry": cfprFirmwareImageFsmTry,
       "cfprFirmwareImageImagePresence": cfprFirmwareImageImagePresence,
       "cfprFirmwareImageIntId": cfprFirmwareImageIntId,
       "cfprFirmwareImageInvTag": cfprFirmwareImageInvTag,
       "cfprFirmwareImageIsoname": cfprFirmwareImageIsoname,
       "cfprFirmwareImageLocation": cfprFirmwareImageLocation,
       "cfprFirmwareImageName": cfprFirmwareImageName,
       "cfprFirmwareImagePolicyLevel": cfprFirmwareImagePolicyLevel,
       "cfprFirmwareImagePolicyOwner": cfprFirmwareImagePolicyOwner,
       "cfprFirmwareImageSize": cfprFirmwareImageSize,
       "cfprFirmwareImageType": cfprFirmwareImageType,
       "cfprFirmwareImageVersion": cfprFirmwareImageVersion,
       "cfprFirmwareImageIsApplicableForEquippedSsd": cfprFirmwareImageIsApplicableForEquippedSsd,
       "cfprFirmwareImageFsmTable": cfprFirmwareImageFsmTable,
       "cfprFirmwareImageFsmEntry": cfprFirmwareImageFsmEntry,
       "cfprFirmwareImageFsmInstanceId": cfprFirmwareImageFsmInstanceId,
       "cfprFirmwareImageFsmDn": cfprFirmwareImageFsmDn,
       "cfprFirmwareImageFsmRn": cfprFirmwareImageFsmRn,
       "cfprFirmwareImageFsmCompletionTime": cfprFirmwareImageFsmCompletionTime,
       "cfprFirmwareImageFsmCurrentFsm": cfprFirmwareImageFsmCurrentFsm,
       "cfprFirmwareImageFsmDescrData": cfprFirmwareImageFsmDescrData,
       "cfprFirmwareImageFsmFsmStatus": cfprFirmwareImageFsmFsmStatus,
       "cfprFirmwareImageFsmProgress": cfprFirmwareImageFsmProgress,
       "cfprFirmwareImageFsmRmtErrCode": cfprFirmwareImageFsmRmtErrCode,
       "cfprFirmwareImageFsmRmtErrDescr": cfprFirmwareImageFsmRmtErrDescr,
       "cfprFirmwareImageFsmRmtRslt": cfprFirmwareImageFsmRmtRslt,
       "cfprFirmwareImageFsmStageTable": cfprFirmwareImageFsmStageTable,
       "cfprFirmwareImageFsmStageEntry": cfprFirmwareImageFsmStageEntry,
       "cfprFirmwareImageFsmStageInstanceId": cfprFirmwareImageFsmStageInstanceId,
       "cfprFirmwareImageFsmStageDn": cfprFirmwareImageFsmStageDn,
       "cfprFirmwareImageFsmStageRn": cfprFirmwareImageFsmStageRn,
       "cfprFirmwareImageFsmStageDescrData": cfprFirmwareImageFsmStageDescrData,
       "cfprFirmwareImageFsmStageLastUpdateTime": cfprFirmwareImageFsmStageLastUpdateTime,
       "cfprFirmwareImageFsmStageName": cfprFirmwareImageFsmStageName,
       "cfprFirmwareImageFsmStageOrder": cfprFirmwareImageFsmStageOrder,
       "cfprFirmwareImageFsmStageRetry": cfprFirmwareImageFsmStageRetry,
       "cfprFirmwareImageFsmStageStageStatus": cfprFirmwareImageFsmStageStageStatus,
       "cfprFirmwareImageFsmTaskTable": cfprFirmwareImageFsmTaskTable,
       "cfprFirmwareImageFsmTaskEntry": cfprFirmwareImageFsmTaskEntry,
       "cfprFirmwareImageFsmTaskInstanceId": cfprFirmwareImageFsmTaskInstanceId,
       "cfprFirmwareImageFsmTaskDn": cfprFirmwareImageFsmTaskDn,
       "cfprFirmwareImageFsmTaskRn": cfprFirmwareImageFsmTaskRn,
       "cfprFirmwareImageFsmTaskCompletion": cfprFirmwareImageFsmTaskCompletion,
       "cfprFirmwareImageFsmTaskFlags": cfprFirmwareImageFsmTaskFlags,
       "cfprFirmwareImageFsmTaskItem": cfprFirmwareImageFsmTaskItem,
       "cfprFirmwareImageFsmTaskSeqId": cfprFirmwareImageFsmTaskSeqId,
       "cfprFirmwareImageLockTable": cfprFirmwareImageLockTable,
       "cfprFirmwareImageLockEntry": cfprFirmwareImageLockEntry,
       "cfprFirmwareImageLockInstanceId": cfprFirmwareImageLockInstanceId,
       "cfprFirmwareImageLockDn": cfprFirmwareImageLockDn,
       "cfprFirmwareImageLockRn": cfprFirmwareImageLockRn,
       "cfprFirmwareImageLockImageNameDn": cfprFirmwareImageLockImageNameDn,
       "cfprFirmwareImageLockName": cfprFirmwareImageLockName,
       "cfprFirmwareInfraTable": cfprFirmwareInfraTable,
       "cfprFirmwareInfraEntry": cfprFirmwareInfraEntry,
       "cfprFirmwareInfraInstanceId": cfprFirmwareInfraInstanceId,
       "cfprFirmwareInfraDn": cfprFirmwareInfraDn,
       "cfprFirmwareInfraRn": cfprFirmwareInfraRn,
       "cfprFirmwareInfraAdminState": cfprFirmwareInfraAdminState,
       "cfprFirmwareInfraAutoDelete": cfprFirmwareInfraAutoDelete,
       "cfprFirmwareInfraDescr": cfprFirmwareInfraDescr,
       "cfprFirmwareInfraIgnoreCap": cfprFirmwareInfraIgnoreCap,
       "cfprFirmwareInfraIntId": cfprFirmwareInfraIntId,
       "cfprFirmwareInfraName": cfprFirmwareInfraName,
       "cfprFirmwareInfraOperScheduler": cfprFirmwareInfraOperScheduler,
       "cfprFirmwareInfraOperState": cfprFirmwareInfraOperState,
       "cfprFirmwareInfraOperVersion": cfprFirmwareInfraOperVersion,
       "cfprFirmwareInfraPolicyLevel": cfprFirmwareInfraPolicyLevel,
       "cfprFirmwareInfraPolicyOwner": cfprFirmwareInfraPolicyOwner,
       "cfprFirmwareInfraScheduler": cfprFirmwareInfraScheduler,
       "cfprFirmwareInfraPackTable": cfprFirmwareInfraPackTable,
       "cfprFirmwareInfraPackEntry": cfprFirmwareInfraPackEntry,
       "cfprFirmwareInfraPackInstanceId": cfprFirmwareInfraPackInstanceId,
       "cfprFirmwareInfraPackDn": cfprFirmwareInfraPackDn,
       "cfprFirmwareInfraPackRn": cfprFirmwareInfraPackRn,
       "cfprFirmwareInfraPackDescr": cfprFirmwareInfraPackDescr,
       "cfprFirmwareInfraPackForceDeploy": cfprFirmwareInfraPackForceDeploy,
       "cfprFirmwareInfraPackInfraBundleName": cfprFirmwareInfraPackInfraBundleName,
       "cfprFirmwareInfraPackInfraBundleVersion": cfprFirmwareInfraPackInfraBundleVersion,
       "cfprFirmwareInfraPackIntId": cfprFirmwareInfraPackIntId,
       "cfprFirmwareInfraPackMode": cfprFirmwareInfraPackMode,
       "cfprFirmwareInfraPackName": cfprFirmwareInfraPackName,
       "cfprFirmwareInfraPackPolicyLevel": cfprFirmwareInfraPackPolicyLevel,
       "cfprFirmwareInfraPackPolicyOwner": cfprFirmwareInfraPackPolicyOwner,
       "cfprFirmwareInfraPackStageSize": cfprFirmwareInfraPackStageSize,
       "cfprFirmwareInfraPackUpdateTrigger": cfprFirmwareInfraPackUpdateTrigger,
       "cfprFirmwareInstallImpactTable": cfprFirmwareInstallImpactTable,
       "cfprFirmwareInstallImpactEntry": cfprFirmwareInstallImpactEntry,
       "cfprFirmwareInstallImpactInstanceId": cfprFirmwareInstallImpactInstanceId,
       "cfprFirmwareInstallImpactDn": cfprFirmwareInstallImpactDn,
       "cfprFirmwareInstallImpactRn": cfprFirmwareInstallImpactRn,
       "cfprFirmwareInstallImpactDescr": cfprFirmwareInstallImpactDescr,
       "cfprFirmwareInstallImpactKeyDn": cfprFirmwareInstallImpactKeyDn,
       "cfprFirmwareInstallImpactMaintPolicyDn": cfprFirmwareInstallImpactMaintPolicyDn,
       "cfprFirmwareInstallImpactRebootPolicy": cfprFirmwareInstallImpactRebootPolicy,
       "cfprFirmwareInstallImpactSubject": cfprFirmwareInstallImpactSubject,
       "cfprFirmwareInstallImpactType": cfprFirmwareInstallImpactType,
       "cfprFirmwareInstallableTable": cfprFirmwareInstallableTable,
       "cfprFirmwareInstallableEntry": cfprFirmwareInstallableEntry,
       "cfprFirmwareInstallableInstanceId": cfprFirmwareInstallableInstanceId,
       "cfprFirmwareInstallableDn": cfprFirmwareInstallableDn,
       "cfprFirmwareInstallableRn": cfprFirmwareInstallableRn,
       "cfprFirmwareInstallableChecksum": cfprFirmwareInstallableChecksum,
       "cfprFirmwareInstallableInProgress": cfprFirmwareInstallableInProgress,
       "cfprFirmwareInstallableIsoname": cfprFirmwareInstallableIsoname,
       "cfprFirmwareInstallableLocation": cfprFirmwareInstallableLocation,
       "cfprFirmwareInstallableModel": cfprFirmwareInstallableModel,
       "cfprFirmwareInstallableName": cfprFirmwareInstallableName,
       "cfprFirmwareInstallableSize": cfprFirmwareInstallableSize,
       "cfprFirmwareInstallableType": cfprFirmwareInstallableType,
       "cfprFirmwareInstallableVendor": cfprFirmwareInstallableVendor,
       "cfprFirmwareInstallableVersion": cfprFirmwareInstallableVersion,
       "cfprFirmwarePackItemTable": cfprFirmwarePackItemTable,
       "cfprFirmwarePackItemEntry": cfprFirmwarePackItemEntry,
       "cfprFirmwarePackItemInstanceId": cfprFirmwarePackItemInstanceId,
       "cfprFirmwarePackItemDn": cfprFirmwarePackItemDn,
       "cfprFirmwarePackItemRn": cfprFirmwarePackItemRn,
       "cfprFirmwarePackItemHwModel": cfprFirmwarePackItemHwModel,
       "cfprFirmwarePackItemHwVendor": cfprFirmwarePackItemHwVendor,
       "cfprFirmwarePackItemPresence": cfprFirmwarePackItemPresence,
       "cfprFirmwarePackItemType": cfprFirmwarePackItemType,
       "cfprFirmwarePackItemVersion": cfprFirmwarePackItemVersion,
       "cfprFirmwarePlatformTable": cfprFirmwarePlatformTable,
       "cfprFirmwarePlatformEntry": cfprFirmwarePlatformEntry,
       "cfprFirmwarePlatformInstanceId": cfprFirmwarePlatformInstanceId,
       "cfprFirmwarePlatformDn": cfprFirmwarePlatformDn,
       "cfprFirmwarePlatformRn": cfprFirmwarePlatformRn,
       "cfprFirmwarePlatformAdminState": cfprFirmwarePlatformAdminState,
       "cfprFirmwarePlatformAutoDelete": cfprFirmwarePlatformAutoDelete,
       "cfprFirmwarePlatformDescr": cfprFirmwarePlatformDescr,
       "cfprFirmwarePlatformIgnoreCap": cfprFirmwarePlatformIgnoreCap,
       "cfprFirmwarePlatformIntId": cfprFirmwarePlatformIntId,
       "cfprFirmwarePlatformName": cfprFirmwarePlatformName,
       "cfprFirmwarePlatformOperScheduler": cfprFirmwarePlatformOperScheduler,
       "cfprFirmwarePlatformOperState": cfprFirmwarePlatformOperState,
       "cfprFirmwarePlatformOperVersion": cfprFirmwarePlatformOperVersion,
       "cfprFirmwarePlatformPolicyLevel": cfprFirmwarePlatformPolicyLevel,
       "cfprFirmwarePlatformPolicyOwner": cfprFirmwarePlatformPolicyOwner,
       "cfprFirmwarePlatformScheduler": cfprFirmwarePlatformScheduler,
       "cfprFirmwarePlatformBundleTypeCapProviderTable": cfprFirmwarePlatformBundleTypeCapProviderTable,
       "cfprFirmwarePlatformBundleTypeCapProviderEntry": cfprFirmwarePlatformBundleTypeCapProviderEntry,
       "cfprFirmwarePlatformBundleTypeCapProviderInstanceId": cfprFirmwarePlatformBundleTypeCapProviderInstanceId,
       "cfprFirmwarePlatformBundleTypeCapProviderDn": cfprFirmwarePlatformBundleTypeCapProviderDn,
       "cfprFirmwarePlatformBundleTypeCapProviderRn": cfprFirmwarePlatformBundleTypeCapProviderRn,
       "cfprFirmwarePlatformBundleTypeCapProviderDeleted": cfprFirmwarePlatformBundleTypeCapProviderDeleted,
       "cfprFirmwarePlatformBundleTypeCapProviderDeprecated": cfprFirmwarePlatformBundleTypeCapProviderDeprecated,
       "cfprFirmwarePlatformBundleTypeCapProviderElementLoadFailures": cfprFirmwarePlatformBundleTypeCapProviderElementLoadFailures,
       "cfprFirmwarePlatformBundleTypeCapProviderElementsLoaded": cfprFirmwarePlatformBundleTypeCapProviderElementsLoaded,
       "cfprFirmwarePlatformBundleTypeCapProviderGencount": cfprFirmwarePlatformBundleTypeCapProviderGencount,
       "cfprFirmwarePlatformBundleTypeCapProviderLoadErrors": cfprFirmwarePlatformBundleTypeCapProviderLoadErrors,
       "cfprFirmwarePlatformBundleTypeCapProviderLoadWarnings": cfprFirmwarePlatformBundleTypeCapProviderLoadWarnings,
       "cfprFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer": cfprFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer,
       "cfprFirmwarePlatformBundleTypeCapProviderModel": cfprFirmwarePlatformBundleTypeCapProviderModel,
       "cfprFirmwarePlatformBundleTypeCapProviderPlatformType": cfprFirmwarePlatformBundleTypeCapProviderPlatformType,
       "cfprFirmwarePlatformBundleTypeCapProviderVendor": cfprFirmwarePlatformBundleTypeCapProviderVendor,
       "cfprFirmwarePlatformPackTable": cfprFirmwarePlatformPackTable,
       "cfprFirmwarePlatformPackEntry": cfprFirmwarePlatformPackEntry,
       "cfprFirmwarePlatformPackInstanceId": cfprFirmwarePlatformPackInstanceId,
       "cfprFirmwarePlatformPackDn": cfprFirmwarePlatformPackDn,
       "cfprFirmwarePlatformPackRn": cfprFirmwarePlatformPackRn,
       "cfprFirmwarePlatformPackDescr": cfprFirmwarePlatformPackDescr,
       "cfprFirmwarePlatformPackForceDeploy": cfprFirmwarePlatformPackForceDeploy,
       "cfprFirmwarePlatformPackFsmDescr": cfprFirmwarePlatformPackFsmDescr,
       "cfprFirmwarePlatformPackFsmFlags": cfprFirmwarePlatformPackFsmFlags,
       "cfprFirmwarePlatformPackFsmPrev": cfprFirmwarePlatformPackFsmPrev,
       "cfprFirmwarePlatformPackFsmProgr": cfprFirmwarePlatformPackFsmProgr,
       "cfprFirmwarePlatformPackFsmRmtInvErrCode": cfprFirmwarePlatformPackFsmRmtInvErrCode,
       "cfprFirmwarePlatformPackFsmRmtInvErrDescr": cfprFirmwarePlatformPackFsmRmtInvErrDescr,
       "cfprFirmwarePlatformPackFsmRmtInvRslt": cfprFirmwarePlatformPackFsmRmtInvRslt,
       "cfprFirmwarePlatformPackFsmStageDescr": cfprFirmwarePlatformPackFsmStageDescr,
       "cfprFirmwarePlatformPackFsmStamp": cfprFirmwarePlatformPackFsmStamp,
       "cfprFirmwarePlatformPackFsmStatus": cfprFirmwarePlatformPackFsmStatus,
       "cfprFirmwarePlatformPackFsmTry": cfprFirmwarePlatformPackFsmTry,
       "cfprFirmwarePlatformPackIntId": cfprFirmwarePlatformPackIntId,
       "cfprFirmwarePlatformPackMode": cfprFirmwarePlatformPackMode,
       "cfprFirmwarePlatformPackName": cfprFirmwarePlatformPackName,
       "cfprFirmwarePlatformPackPlatformBundleName": cfprFirmwarePlatformPackPlatformBundleName,
       "cfprFirmwarePlatformPackPlatformBundleVersion": cfprFirmwarePlatformPackPlatformBundleVersion,
       "cfprFirmwarePlatformPackPolicyLevel": cfprFirmwarePlatformPackPolicyLevel,
       "cfprFirmwarePlatformPackPolicyOwner": cfprFirmwarePlatformPackPolicyOwner,
       "cfprFirmwarePlatformPackPreviousBundleVersion": cfprFirmwarePlatformPackPreviousBundleVersion,
       "cfprFirmwarePlatformPackRestoreVersion": cfprFirmwarePlatformPackRestoreVersion,
       "cfprFirmwarePlatformPackSerializeHostUpgrade": cfprFirmwarePlatformPackSerializeHostUpgrade,
       "cfprFirmwarePlatformPackSkipManagerValidation": cfprFirmwarePlatformPackSkipManagerValidation,
       "cfprFirmwarePlatformPackStageSize": cfprFirmwarePlatformPackStageSize,
       "cfprFirmwarePlatformPackUpdateTrigger": cfprFirmwarePlatformPackUpdateTrigger,
       "cfprFirmwarePlatformPackPrevBundleVersion": cfprFirmwarePlatformPackPrevBundleVersion,
       "cfprFirmwarePlatformPackVersionChecked": cfprFirmwarePlatformPackVersionChecked,
       "cfprFirmwarePlatformPackFsmTable": cfprFirmwarePlatformPackFsmTable,
       "cfprFirmwarePlatformPackFsmEntry": cfprFirmwarePlatformPackFsmEntry,
       "cfprFirmwarePlatformPackFsmInstanceId": cfprFirmwarePlatformPackFsmInstanceId,
       "cfprFirmwarePlatformPackFsmDn": cfprFirmwarePlatformPackFsmDn,
       "cfprFirmwarePlatformPackFsmRn": cfprFirmwarePlatformPackFsmRn,
       "cfprFirmwarePlatformPackFsmCompletionTime": cfprFirmwarePlatformPackFsmCompletionTime,
       "cfprFirmwarePlatformPackFsmCurrentFsm": cfprFirmwarePlatformPackFsmCurrentFsm,
       "cfprFirmwarePlatformPackFsmDescrData": cfprFirmwarePlatformPackFsmDescrData,
       "cfprFirmwarePlatformPackFsmFsmStatus": cfprFirmwarePlatformPackFsmFsmStatus,
       "cfprFirmwarePlatformPackFsmProgress": cfprFirmwarePlatformPackFsmProgress,
       "cfprFirmwarePlatformPackFsmRmtErrCode": cfprFirmwarePlatformPackFsmRmtErrCode,
       "cfprFirmwarePlatformPackFsmRmtErrDescr": cfprFirmwarePlatformPackFsmRmtErrDescr,
       "cfprFirmwarePlatformPackFsmRmtRslt": cfprFirmwarePlatformPackFsmRmtRslt,
       "cfprFirmwarePlatformPackFsmStageTable": cfprFirmwarePlatformPackFsmStageTable,
       "cfprFirmwarePlatformPackFsmStageEntry": cfprFirmwarePlatformPackFsmStageEntry,
       "cfprFirmwarePlatformPackFsmStageInstanceId": cfprFirmwarePlatformPackFsmStageInstanceId,
       "cfprFirmwarePlatformPackFsmStageDn": cfprFirmwarePlatformPackFsmStageDn,
       "cfprFirmwarePlatformPackFsmStageRn": cfprFirmwarePlatformPackFsmStageRn,
       "cfprFirmwarePlatformPackFsmStageDescrData": cfprFirmwarePlatformPackFsmStageDescrData,
       "cfprFirmwarePlatformPackFsmStageLastUpdateTime": cfprFirmwarePlatformPackFsmStageLastUpdateTime,
       "cfprFirmwarePlatformPackFsmStageName": cfprFirmwarePlatformPackFsmStageName,
       "cfprFirmwarePlatformPackFsmStageOrder": cfprFirmwarePlatformPackFsmStageOrder,
       "cfprFirmwarePlatformPackFsmStageRetry": cfprFirmwarePlatformPackFsmStageRetry,
       "cfprFirmwarePlatformPackFsmStageStageStatus": cfprFirmwarePlatformPackFsmStageStageStatus,
       "cfprFirmwarePlatformPackFsmTaskTable": cfprFirmwarePlatformPackFsmTaskTable,
       "cfprFirmwarePlatformPackFsmTaskEntry": cfprFirmwarePlatformPackFsmTaskEntry,
       "cfprFirmwarePlatformPackFsmTaskInstanceId": cfprFirmwarePlatformPackFsmTaskInstanceId,
       "cfprFirmwarePlatformPackFsmTaskDn": cfprFirmwarePlatformPackFsmTaskDn,
       "cfprFirmwarePlatformPackFsmTaskRn": cfprFirmwarePlatformPackFsmTaskRn,
       "cfprFirmwarePlatformPackFsmTaskCompletion": cfprFirmwarePlatformPackFsmTaskCompletion,
       "cfprFirmwarePlatformPackFsmTaskFlags": cfprFirmwarePlatformPackFsmTaskFlags,
       "cfprFirmwarePlatformPackFsmTaskItem": cfprFirmwarePlatformPackFsmTaskItem,
       "cfprFirmwarePlatformPackFsmTaskSeqId": cfprFirmwarePlatformPackFsmTaskSeqId,
       "cfprFirmwareRackTable": cfprFirmwareRackTable,
       "cfprFirmwareRackEntry": cfprFirmwareRackEntry,
       "cfprFirmwareRackInstanceId": cfprFirmwareRackInstanceId,
       "cfprFirmwareRackDn": cfprFirmwareRackDn,
       "cfprFirmwareRackRn": cfprFirmwareRackRn,
       "cfprFirmwareRackOperVersion": cfprFirmwareRackOperVersion,
       "cfprFirmwareRunningTable": cfprFirmwareRunningTable,
       "cfprFirmwareRunningEntry": cfprFirmwareRunningEntry,
       "cfprFirmwareRunningInstanceId": cfprFirmwareRunningInstanceId,
       "cfprFirmwareRunningDn": cfprFirmwareRunningDn,
       "cfprFirmwareRunningRn": cfprFirmwareRunningRn,
       "cfprFirmwareRunningDeployment": cfprFirmwareRunningDeployment,
       "cfprFirmwareRunningInvTag": cfprFirmwareRunningInvTag,
       "cfprFirmwareRunningPackageVersion": cfprFirmwareRunningPackageVersion,
       "cfprFirmwareRunningType": cfprFirmwareRunningType,
       "cfprFirmwareRunningVersion": cfprFirmwareRunningVersion,
       "cfprFirmwareRunningMioSsdmodel": cfprFirmwareRunningMioSsdmodel,
       "cfprFirmwareSpecTable": cfprFirmwareSpecTable,
       "cfprFirmwareSpecEntry": cfprFirmwareSpecEntry,
       "cfprFirmwareSpecInstanceId": cfprFirmwareSpecInstanceId,
       "cfprFirmwareSpecDn": cfprFirmwareSpecDn,
       "cfprFirmwareSpecRn": cfprFirmwareSpecRn,
       "cfprFirmwareSpecBundleVersion": cfprFirmwareSpecBundleVersion,
       "cfprFirmwareSpecEthEFIVersion": cfprFirmwareSpecEthEFIVersion,
       "cfprFirmwareSpecEthOptionRomVersion": cfprFirmwareSpecEthOptionRomVersion,
       "cfprFirmwareSpecFcFWVersion": cfprFirmwareSpecFcFWVersion,
       "cfprFirmwareSpecFcOptionRomVersion": cfprFirmwareSpecFcOptionRomVersion,
       "cfprFirmwareStatusTable": cfprFirmwareStatusTable,
       "cfprFirmwareStatusEntry": cfprFirmwareStatusEntry,
       "cfprFirmwareStatusInstanceId": cfprFirmwareStatusInstanceId,
       "cfprFirmwareStatusDn": cfprFirmwareStatusDn,
       "cfprFirmwareStatusRn": cfprFirmwareStatusRn,
       "cfprFirmwareStatusCimcVersion": cfprFirmwareStatusCimcVersion,
       "cfprFirmwareStatusFirmwareState": cfprFirmwareStatusFirmwareState,
       "cfprFirmwareStatusOperState": cfprFirmwareStatusOperState,
       "cfprFirmwareStatusPackageVersion": cfprFirmwareStatusPackageVersion,
       "cfprFirmwareStatusPldVersion": cfprFirmwareStatusPldVersion,
       "cfprFirmwareSystemTable": cfprFirmwareSystemTable,
       "cfprFirmwareSystemEntry": cfprFirmwareSystemEntry,
       "cfprFirmwareSystemInstanceId": cfprFirmwareSystemInstanceId,
       "cfprFirmwareSystemDn": cfprFirmwareSystemDn,
       "cfprFirmwareSystemRn": cfprFirmwareSystemRn,
       "cfprFirmwareSystemFsmDescr": cfprFirmwareSystemFsmDescr,
       "cfprFirmwareSystemFsmFlags": cfprFirmwareSystemFsmFlags,
       "cfprFirmwareSystemFsmPrev": cfprFirmwareSystemFsmPrev,
       "cfprFirmwareSystemFsmProgr": cfprFirmwareSystemFsmProgr,
       "cfprFirmwareSystemFsmRmtInvErrCode": cfprFirmwareSystemFsmRmtInvErrCode,
       "cfprFirmwareSystemFsmRmtInvErrDescr": cfprFirmwareSystemFsmRmtInvErrDescr,
       "cfprFirmwareSystemFsmRmtInvRslt": cfprFirmwareSystemFsmRmtInvRslt,
       "cfprFirmwareSystemFsmStageDescr": cfprFirmwareSystemFsmStageDescr,
       "cfprFirmwareSystemFsmStamp": cfprFirmwareSystemFsmStamp,
       "cfprFirmwareSystemFsmStatus": cfprFirmwareSystemFsmStatus,
       "cfprFirmwareSystemFsmTry": cfprFirmwareSystemFsmTry,
       "cfprFirmwareSystemOperState": cfprFirmwareSystemOperState,
       "cfprFirmwareSystemState": cfprFirmwareSystemState,
       "cfprFirmwareSystemResetOnUpgrade": cfprFirmwareSystemResetOnUpgrade,
       "cfprFirmwareSystemScheduledInstallTime": cfprFirmwareSystemScheduledInstallTime,
       "cfprFirmwareSystemValidationStatus": cfprFirmwareSystemValidationStatus,
       "cfprFirmwareSystemCompCheckResultTable": cfprFirmwareSystemCompCheckResultTable,
       "cfprFirmwareSystemCompCheckResultEntry": cfprFirmwareSystemCompCheckResultEntry,
       "cfprFirmwareSystemCompCheckResultInstanceId": cfprFirmwareSystemCompCheckResultInstanceId,
       "cfprFirmwareSystemCompCheckResultDn": cfprFirmwareSystemCompCheckResultDn,
       "cfprFirmwareSystemCompCheckResultRn": cfprFirmwareSystemCompCheckResultRn,
       "cfprFirmwareSystemCompCheckResultKeyDescr": cfprFirmwareSystemCompCheckResultKeyDescr,
       "cfprFirmwareSystemCompCheckResultKeyDn": cfprFirmwareSystemCompCheckResultKeyDn,
       "cfprFirmwareSystemCompCheckResultNonCompDescr": cfprFirmwareSystemCompCheckResultNonCompDescr,
       "cfprFirmwareSystemCompCheckResultNonCompDns": cfprFirmwareSystemCompCheckResultNonCompDns,
       "cfprFirmwareSystemCompCheckResultSubject": cfprFirmwareSystemCompCheckResultSubject,
       "cfprFirmwareSystemFsmTable": cfprFirmwareSystemFsmTable,
       "cfprFirmwareSystemFsmEntry": cfprFirmwareSystemFsmEntry,
       "cfprFirmwareSystemFsmInstanceId": cfprFirmwareSystemFsmInstanceId,
       "cfprFirmwareSystemFsmDn": cfprFirmwareSystemFsmDn,
       "cfprFirmwareSystemFsmRn": cfprFirmwareSystemFsmRn,
       "cfprFirmwareSystemFsmCompletionTime": cfprFirmwareSystemFsmCompletionTime,
       "cfprFirmwareSystemFsmCurrentFsm": cfprFirmwareSystemFsmCurrentFsm,
       "cfprFirmwareSystemFsmDescrData": cfprFirmwareSystemFsmDescrData,
       "cfprFirmwareSystemFsmFsmStatus": cfprFirmwareSystemFsmFsmStatus,
       "cfprFirmwareSystemFsmProgress": cfprFirmwareSystemFsmProgress,
       "cfprFirmwareSystemFsmRmtErrCode": cfprFirmwareSystemFsmRmtErrCode,
       "cfprFirmwareSystemFsmRmtErrDescr": cfprFirmwareSystemFsmRmtErrDescr,
       "cfprFirmwareSystemFsmRmtRslt": cfprFirmwareSystemFsmRmtRslt,
       "cfprFirmwareSystemFsmStageTable": cfprFirmwareSystemFsmStageTable,
       "cfprFirmwareSystemFsmStageEntry": cfprFirmwareSystemFsmStageEntry,
       "cfprFirmwareSystemFsmStageInstanceId": cfprFirmwareSystemFsmStageInstanceId,
       "cfprFirmwareSystemFsmStageDn": cfprFirmwareSystemFsmStageDn,
       "cfprFirmwareSystemFsmStageRn": cfprFirmwareSystemFsmStageRn,
       "cfprFirmwareSystemFsmStageDescrData": cfprFirmwareSystemFsmStageDescrData,
       "cfprFirmwareSystemFsmStageLastUpdateTime": cfprFirmwareSystemFsmStageLastUpdateTime,
       "cfprFirmwareSystemFsmStageName": cfprFirmwareSystemFsmStageName,
       "cfprFirmwareSystemFsmStageOrder": cfprFirmwareSystemFsmStageOrder,
       "cfprFirmwareSystemFsmStageRetry": cfprFirmwareSystemFsmStageRetry,
       "cfprFirmwareSystemFsmStageStageStatus": cfprFirmwareSystemFsmStageStageStatus,
       "cfprFirmwareSystemFsmTaskTable": cfprFirmwareSystemFsmTaskTable,
       "cfprFirmwareSystemFsmTaskEntry": cfprFirmwareSystemFsmTaskEntry,
       "cfprFirmwareSystemFsmTaskInstanceId": cfprFirmwareSystemFsmTaskInstanceId,
       "cfprFirmwareSystemFsmTaskDn": cfprFirmwareSystemFsmTaskDn,
       "cfprFirmwareSystemFsmTaskRn": cfprFirmwareSystemFsmTaskRn,
       "cfprFirmwareSystemFsmTaskCompletion": cfprFirmwareSystemFsmTaskCompletion,
       "cfprFirmwareSystemFsmTaskFlags": cfprFirmwareSystemFsmTaskFlags,
       "cfprFirmwareSystemFsmTaskItem": cfprFirmwareSystemFsmTaskItem,
       "cfprFirmwareSystemFsmTaskSeqId": cfprFirmwareSystemFsmTaskSeqId,
       "cfprFirmwareTypeTable": cfprFirmwareTypeTable,
       "cfprFirmwareTypeEntry": cfprFirmwareTypeEntry,
       "cfprFirmwareTypeInstanceId": cfprFirmwareTypeInstanceId,
       "cfprFirmwareTypeDn": cfprFirmwareTypeDn,
       "cfprFirmwareTypeRn": cfprFirmwareTypeRn,
       "cfprFirmwareTypeEp": cfprFirmwareTypeEp,
       "cfprFirmwareTypeInvTag": cfprFirmwareTypeInvTag,
       "cfprFirmwareTypeMaxVer": cfprFirmwareTypeMaxVer,
       "cfprFirmwareTypeMinVer": cfprFirmwareTypeMinVer,
       "cfprFirmwareTypePid": cfprFirmwareTypePid,
       "cfprFirmwareTypeScheduledInstallTime": cfprFirmwareTypeScheduledInstallTime,
       "cfprFirmwareFprcInfoTable": cfprFirmwareFprcInfoTable,
       "cfprFirmwareFprcInfoEntry": cfprFirmwareFprcInfoEntry,
       "cfprFirmwareFprcInfoInstanceId": cfprFirmwareFprcInfoInstanceId,
       "cfprFirmwareFprcInfoDn": cfprFirmwareFprcInfoDn,
       "cfprFirmwareFprcInfoRn": cfprFirmwareFprcInfoRn,
       "cfprFirmwareFprcInfoConnProtocol": cfprFirmwareFprcInfoConnProtocol,
       "cfprFirmwareFprcInfoHost": cfprFirmwareFprcInfoHost,
       "cfprFirmwareFprcInfoVersion": cfprFirmwareFprcInfoVersion,
       "cfprFirmwareUpdatableTable": cfprFirmwareUpdatableTable,
       "cfprFirmwareUpdatableEntry": cfprFirmwareUpdatableEntry,
       "cfprFirmwareUpdatableInstanceId": cfprFirmwareUpdatableInstanceId,
       "cfprFirmwareUpdatableDn": cfprFirmwareUpdatableDn,
       "cfprFirmwareUpdatableRn": cfprFirmwareUpdatableRn,
       "cfprFirmwareUpdatableAdminState": cfprFirmwareUpdatableAdminState,
       "cfprFirmwareUpdatableDeployment": cfprFirmwareUpdatableDeployment,
       "cfprFirmwareUpdatableOperState": cfprFirmwareUpdatableOperState,
       "cfprFirmwareUpdatableOperStateQual": cfprFirmwareUpdatableOperStateQual,
       "cfprFirmwareUpdatablePrevVersion": cfprFirmwareUpdatablePrevVersion,
       "cfprFirmwareUpdatableVersion": cfprFirmwareUpdatableVersion,
       "cfprFirmwareUpgradeConstraintTable": cfprFirmwareUpgradeConstraintTable,
       "cfprFirmwareUpgradeConstraintEntry": cfprFirmwareUpgradeConstraintEntry,
       "cfprFirmwareUpgradeConstraintInstanceId": cfprFirmwareUpgradeConstraintInstanceId,
       "cfprFirmwareUpgradeConstraintDn": cfprFirmwareUpgradeConstraintDn,
       "cfprFirmwareUpgradeConstraintRn": cfprFirmwareUpgradeConstraintRn,
       "cfprFirmwareUpgradeConstraintMinVer": cfprFirmwareUpgradeConstraintMinVer,
       "cfprFirmwareUpgradeDetailTable": cfprFirmwareUpgradeDetailTable,
       "cfprFirmwareUpgradeDetailEntry": cfprFirmwareUpgradeDetailEntry,
       "cfprFirmwareUpgradeDetailInstanceId": cfprFirmwareUpgradeDetailInstanceId,
       "cfprFirmwareUpgradeDetailDn": cfprFirmwareUpgradeDetailDn,
       "cfprFirmwareUpgradeDetailRn": cfprFirmwareUpgradeDetailRn,
       "cfprFirmwareUpgradeDetailCategory": cfprFirmwareUpgradeDetailCategory,
       "cfprFirmwareUpgradeDetailDescription": cfprFirmwareUpgradeDetailDescription,
       "cfprFirmwareUpgradeDetailId": cfprFirmwareUpgradeDetailId,
       "cfprFirmwareUpgradeDetailSeverity": cfprFirmwareUpgradeDetailSeverity,
       "cfprFirmwareUpgradeInfoTable": cfprFirmwareUpgradeInfoTable,
       "cfprFirmwareUpgradeInfoEntry": cfprFirmwareUpgradeInfoEntry,
       "cfprFirmwareUpgradeInfoInstanceId": cfprFirmwareUpgradeInfoInstanceId,
       "cfprFirmwareUpgradeInfoDn": cfprFirmwareUpgradeInfoDn,
       "cfprFirmwareUpgradeInfoRn": cfprFirmwareUpgradeInfoRn,
       "cfprFirmwareUpgradeInfoMessage": cfprFirmwareUpgradeInfoMessage,
       "cfprFirmwareUpgradeInfoTimeStamp": cfprFirmwareUpgradeInfoTimeStamp,
       "cfprFirmwareUpgradeInfoValidateStatus": cfprFirmwareUpgradeInfoValidateStatus,
       "cfprFirmwareUpgradeInfoVersion": cfprFirmwareUpgradeInfoVersion,
       "cfprFirmwareCspAppListTable": cfprFirmwareCspAppListTable,
       "cfprFirmwareCspAppListEntry": cfprFirmwareCspAppListEntry,
       "cfprFirmwareCspAppListInstanceId": cfprFirmwareCspAppListInstanceId,
       "cfprFirmwareCspAppListDn": cfprFirmwareCspAppListDn,
       "cfprFirmwareCspAppListRn": cfprFirmwareCspAppListRn,
       "cfprFirmwareCspAppListName": cfprFirmwareCspAppListName,
       "cfprFirmwareCspVersionTable": cfprFirmwareCspVersionTable,
       "cfprFirmwareCspVersionEntry": cfprFirmwareCspVersionEntry,
       "cfprFirmwareCspVersionInstanceId": cfprFirmwareCspVersionInstanceId,
       "cfprFirmwareCspVersionDn": cfprFirmwareCspVersionDn,
       "cfprFirmwareCspVersionRn": cfprFirmwareCspVersionRn,
       "cfprFirmwareCspVersionAppName": cfprFirmwareCspVersionAppName,
       "cfprFirmwareCspVersionFromVersion": cfprFirmwareCspVersionFromVersion,
       "cfprFirmwareCspVersionName": cfprFirmwareCspVersionName,
       "cfprFirmwareCspVersionSecModelSupported": cfprFirmwareCspVersionSecModelSupported,
       "cfprFirmwareCspVersionSupportMode": cfprFirmwareCspVersionSupportMode,
       "cfprFirmwareCspVersionToVersion": cfprFirmwareCspVersionToVersion,
       "cfprFirmwareDistCspBlackListTable": cfprFirmwareDistCspBlackListTable,
       "cfprFirmwareDistCspBlackListEntry": cfprFirmwareDistCspBlackListEntry,
       "cfprFirmwareDistCspBlackListInstanceId": cfprFirmwareDistCspBlackListInstanceId,
       "cfprFirmwareDistCspBlackListDn": cfprFirmwareDistCspBlackListDn,
       "cfprFirmwareDistCspBlackListRn": cfprFirmwareDistCspBlackListRn,
       "cfprFirmwareDistCspBlackListName": cfprFirmwareDistCspBlackListName,
       "cfprFirmwareDistCspBlackListTimeStamp": cfprFirmwareDistCspBlackListTimeStamp,
       "cfprFirmwareDistCspBlackListVersion": cfprFirmwareDistCspBlackListVersion,
       "cfprFirmwareRunnableTable": cfprFirmwareRunnableTable,
       "cfprFirmwareRunnableEntry": cfprFirmwareRunnableEntry,
       "cfprFirmwareRunnableInstanceId": cfprFirmwareRunnableInstanceId,
       "cfprFirmwareRunnableDn": cfprFirmwareRunnableDn,
       "cfprFirmwareRunnableRn": cfprFirmwareRunnableRn,
       "cfprFirmwareRunnableAdminState": cfprFirmwareRunnableAdminState,
       "cfprFirmwareRunnableDeployment": cfprFirmwareRunnableDeployment,
       "cfprFirmwareRunnableMemFault": cfprFirmwareRunnableMemFault,
       "cfprFirmwareRunnableOperState": cfprFirmwareRunnableOperState,
       "cfprFirmwareRunnablePrevVersion": cfprFirmwareRunnablePrevVersion,
       "cfprFirmwareRunnableVersion": cfprFirmwareRunnableVersion,
       "cfprFirmwareSupFirmwareTable": cfprFirmwareSupFirmwareTable,
       "cfprFirmwareSupFirmwareEntry": cfprFirmwareSupFirmwareEntry,
       "cfprFirmwareSupFirmwareInstanceId": cfprFirmwareSupFirmwareInstanceId,
       "cfprFirmwareSupFirmwareDn": cfprFirmwareSupFirmwareDn,
       "cfprFirmwareSupFirmwareRn": cfprFirmwareSupFirmwareRn,
       "cfprFirmwareSupFirmwareForceUpgrade": cfprFirmwareSupFirmwareForceUpgrade,
       "cfprFirmwareSupFirmwareFsmDescr": cfprFirmwareSupFirmwareFsmDescr,
       "cfprFirmwareSupFirmwareFsmFlags": cfprFirmwareSupFirmwareFsmFlags,
       "cfprFirmwareSupFirmwareFsmPrev": cfprFirmwareSupFirmwareFsmPrev,
       "cfprFirmwareSupFirmwareFsmProgr": cfprFirmwareSupFirmwareFsmProgr,
       "cfprFirmwareSupFirmwareFsmRmtInvErrCode": cfprFirmwareSupFirmwareFsmRmtInvErrCode,
       "cfprFirmwareSupFirmwareFsmRmtInvErrDescr": cfprFirmwareSupFirmwareFsmRmtInvErrDescr,
       "cfprFirmwareSupFirmwareFsmRmtInvRslt": cfprFirmwareSupFirmwareFsmRmtInvRslt,
       "cfprFirmwareSupFirmwareFsmStageDescr": cfprFirmwareSupFirmwareFsmStageDescr,
       "cfprFirmwareSupFirmwareFsmStamp": cfprFirmwareSupFirmwareFsmStamp,
       "cfprFirmwareSupFirmwareFsmStatus": cfprFirmwareSupFirmwareFsmStatus,
       "cfprFirmwareSupFirmwareFsmTry": cfprFirmwareSupFirmwareFsmTry,
       "cfprFirmwareSupFirmwareOperState": cfprFirmwareSupFirmwareOperState,
       "cfprFirmwareSupFirmwarePackVersion": cfprFirmwareSupFirmwarePackVersion,
       "cfprFirmwareSupFirmwareState": cfprFirmwareSupFirmwareState,
       "cfprFirmwareSupFirmwareUpgradeStatus": cfprFirmwareSupFirmwareUpgradeStatus,
       "cfprFirmwareSupFirmwareIsAutoFwUpgradeInProgress": cfprFirmwareSupFirmwareIsAutoFwUpgradeInProgress,
       "cfprFirmwareSupFirmwareFsmTable": cfprFirmwareSupFirmwareFsmTable,
       "cfprFirmwareSupFirmwareFsmEntry": cfprFirmwareSupFirmwareFsmEntry,
       "cfprFirmwareSupFirmwareFsmInstanceId": cfprFirmwareSupFirmwareFsmInstanceId,
       "cfprFirmwareSupFirmwareFsmDn": cfprFirmwareSupFirmwareFsmDn,
       "cfprFirmwareSupFirmwareFsmRn": cfprFirmwareSupFirmwareFsmRn,
       "cfprFirmwareSupFirmwareFsmCompletionTime": cfprFirmwareSupFirmwareFsmCompletionTime,
       "cfprFirmwareSupFirmwareFsmCurrentFsm": cfprFirmwareSupFirmwareFsmCurrentFsm,
       "cfprFirmwareSupFirmwareFsmDescrData": cfprFirmwareSupFirmwareFsmDescrData,
       "cfprFirmwareSupFirmwareFsmFsmStatus": cfprFirmwareSupFirmwareFsmFsmStatus,
       "cfprFirmwareSupFirmwareFsmProgress": cfprFirmwareSupFirmwareFsmProgress,
       "cfprFirmwareSupFirmwareFsmRmtErrCode": cfprFirmwareSupFirmwareFsmRmtErrCode,
       "cfprFirmwareSupFirmwareFsmRmtErrDescr": cfprFirmwareSupFirmwareFsmRmtErrDescr,
       "cfprFirmwareSupFirmwareFsmRmtRslt": cfprFirmwareSupFirmwareFsmRmtRslt,
       "cfprFirmwareSupFirmwareFsmStageTable": cfprFirmwareSupFirmwareFsmStageTable,
       "cfprFirmwareSupFirmwareFsmStageEntry": cfprFirmwareSupFirmwareFsmStageEntry,
       "cfprFirmwareSupFirmwareFsmStageInstanceId": cfprFirmwareSupFirmwareFsmStageInstanceId,
       "cfprFirmwareSupFirmwareFsmStageDn": cfprFirmwareSupFirmwareFsmStageDn,
       "cfprFirmwareSupFirmwareFsmStageRn": cfprFirmwareSupFirmwareFsmStageRn,
       "cfprFirmwareSupFirmwareFsmStageDescrData": cfprFirmwareSupFirmwareFsmStageDescrData,
       "cfprFirmwareSupFirmwareFsmStageLastUpdateTime": cfprFirmwareSupFirmwareFsmStageLastUpdateTime,
       "cfprFirmwareSupFirmwareFsmStageName": cfprFirmwareSupFirmwareFsmStageName,
       "cfprFirmwareSupFirmwareFsmStageOrder": cfprFirmwareSupFirmwareFsmStageOrder,
       "cfprFirmwareSupFirmwareFsmStageRetry": cfprFirmwareSupFirmwareFsmStageRetry,
       "cfprFirmwareSupFirmwareFsmStageStageStatus": cfprFirmwareSupFirmwareFsmStageStageStatus,
       "cfprFirmwareSupFirmwareFsmTaskTable": cfprFirmwareSupFirmwareFsmTaskTable,
       "cfprFirmwareSupFirmwareFsmTaskEntry": cfprFirmwareSupFirmwareFsmTaskEntry,
       "cfprFirmwareSupFirmwareFsmTaskInstanceId": cfprFirmwareSupFirmwareFsmTaskInstanceId,
       "cfprFirmwareSupFirmwareFsmTaskDn": cfprFirmwareSupFirmwareFsmTaskDn,
       "cfprFirmwareSupFirmwareFsmTaskRn": cfprFirmwareSupFirmwareFsmTaskRn,
       "cfprFirmwareSupFirmwareFsmTaskCompletion": cfprFirmwareSupFirmwareFsmTaskCompletion,
       "cfprFirmwareSupFirmwareFsmTaskFlags": cfprFirmwareSupFirmwareFsmTaskFlags,
       "cfprFirmwareSupFirmwareFsmTaskItem": cfprFirmwareSupFirmwareFsmTaskItem,
       "cfprFirmwareSupFirmwareFsmTaskSeqId": cfprFirmwareSupFirmwareFsmTaskSeqId,
       "cfprFirmwareValidationStatusTable": cfprFirmwareValidationStatusTable,
       "cfprFirmwareValidationStatusEntry": cfprFirmwareValidationStatusEntry,
       "cfprFirmwareValidationStatusInstanceId": cfprFirmwareValidationStatusInstanceId,
       "cfprFirmwareValidationStatusDn": cfprFirmwareValidationStatusDn,
       "cfprFirmwareValidationStatusRn": cfprFirmwareValidationStatusRn,
       "cfprFirmwareValidationStatusAdapterImageStatusCode": cfprFirmwareValidationStatusAdapterImageStatusCode,
       "cfprFirmwareValidationStatusBiosImageStatusCode": cfprFirmwareValidationStatusBiosImageStatusCode,
       "cfprFirmwareValidationStatusBmcImageStatusCode": cfprFirmwareValidationStatusBmcImageStatusCode,
       "cfprFirmwareValidationStatusBrdctrlImageStatusCode": cfprFirmwareValidationStatusBrdctrlImageStatusCode,
       "cfprFirmwareValidationStatusFsmDescr": cfprFirmwareValidationStatusFsmDescr,
       "cfprFirmwareValidationStatusFsmFlags": cfprFirmwareValidationStatusFsmFlags,
       "cfprFirmwareValidationStatusFsmPrev": cfprFirmwareValidationStatusFsmPrev,
       "cfprFirmwareValidationStatusFsmProgr": cfprFirmwareValidationStatusFsmProgr,
       "cfprFirmwareValidationStatusFsmRmtInvErrCode": cfprFirmwareValidationStatusFsmRmtInvErrCode,
       "cfprFirmwareValidationStatusFsmRmtInvErrDescr": cfprFirmwareValidationStatusFsmRmtInvErrDescr,
       "cfprFirmwareValidationStatusFsmRmtInvRslt": cfprFirmwareValidationStatusFsmRmtInvRslt,
       "cfprFirmwareValidationStatusFsmStageDescr": cfprFirmwareValidationStatusFsmStageDescr,
       "cfprFirmwareValidationStatusFsmStamp": cfprFirmwareValidationStatusFsmStamp,
       "cfprFirmwareValidationStatusFsmStatus": cfprFirmwareValidationStatusFsmStatus,
       "cfprFirmwareValidationStatusFsmTry": cfprFirmwareValidationStatusFsmTry,
       "cfprFirmwareValidationStatusKickstartImageStatusCode": cfprFirmwareValidationStatusKickstartImageStatusCode,
       "cfprFirmwareValidationStatusMgtExtImageStatusCode": cfprFirmwareValidationStatusMgtExtImageStatusCode,
       "cfprFirmwareValidationStatusOverallStatusCode": cfprFirmwareValidationStatusOverallStatusCode,
       "cfprFirmwareValidationStatusOverallStatusString": cfprFirmwareValidationStatusOverallStatusString,
       "cfprFirmwareValidationStatusPackName": cfprFirmwareValidationStatusPackName,
       "cfprFirmwareValidationStatusPackVersion": cfprFirmwareValidationStatusPackVersion,
       "cfprFirmwareValidationStatusSsposImageStatusCode": cfprFirmwareValidationStatusSsposImageStatusCode,
       "cfprFirmwareValidationStatusState": cfprFirmwareValidationStatusState,
       "cfprFirmwareValidationStatusStorageImageStatusCode": cfprFirmwareValidationStatusStorageImageStatusCode,
       "cfprFirmwareValidationStatusSvcMgrImageStatusCode": cfprFirmwareValidationStatusSvcMgrImageStatusCode,
       "cfprFirmwareValidationStatusSystemImageStatusCode": cfprFirmwareValidationStatusSystemImageStatusCode,
       "cfprFirmwareValidationStatusTimeStamp": cfprFirmwareValidationStatusTimeStamp,
       "cfprFirmwareValidationStatusFsmTable": cfprFirmwareValidationStatusFsmTable,
       "cfprFirmwareValidationStatusFsmEntry": cfprFirmwareValidationStatusFsmEntry,
       "cfprFirmwareValidationStatusFsmInstanceId": cfprFirmwareValidationStatusFsmInstanceId,
       "cfprFirmwareValidationStatusFsmDn": cfprFirmwareValidationStatusFsmDn,
       "cfprFirmwareValidationStatusFsmRn": cfprFirmwareValidationStatusFsmRn,
       "cfprFirmwareValidationStatusFsmCompletionTime": cfprFirmwareValidationStatusFsmCompletionTime,
       "cfprFirmwareValidationStatusFsmCurrentFsm": cfprFirmwareValidationStatusFsmCurrentFsm,
       "cfprFirmwareValidationStatusFsmDescrData": cfprFirmwareValidationStatusFsmDescrData,
       "cfprFirmwareValidationStatusFsmFsmStatus": cfprFirmwareValidationStatusFsmFsmStatus,
       "cfprFirmwareValidationStatusFsmProgress": cfprFirmwareValidationStatusFsmProgress,
       "cfprFirmwareValidationStatusFsmRmtErrCode": cfprFirmwareValidationStatusFsmRmtErrCode,
       "cfprFirmwareValidationStatusFsmRmtErrDescr": cfprFirmwareValidationStatusFsmRmtErrDescr,
       "cfprFirmwareValidationStatusFsmRmtRslt": cfprFirmwareValidationStatusFsmRmtRslt,
       "cfprFirmwareValidationStatusFsmStageTable": cfprFirmwareValidationStatusFsmStageTable,
       "cfprFirmwareValidationStatusFsmStageEntry": cfprFirmwareValidationStatusFsmStageEntry,
       "cfprFirmwareValidationStatusFsmStageInstanceId": cfprFirmwareValidationStatusFsmStageInstanceId,
       "cfprFirmwareValidationStatusFsmStageDn": cfprFirmwareValidationStatusFsmStageDn,
       "cfprFirmwareValidationStatusFsmStageRn": cfprFirmwareValidationStatusFsmStageRn,
       "cfprFirmwareValidationStatusFsmStageDescrData": cfprFirmwareValidationStatusFsmStageDescrData,
       "cfprFirmwareValidationStatusFsmStageLastUpdateTime": cfprFirmwareValidationStatusFsmStageLastUpdateTime,
       "cfprFirmwareValidationStatusFsmStageName": cfprFirmwareValidationStatusFsmStageName,
       "cfprFirmwareValidationStatusFsmStageOrder": cfprFirmwareValidationStatusFsmStageOrder,
       "cfprFirmwareValidationStatusFsmStageRetry": cfprFirmwareValidationStatusFsmStageRetry,
       "cfprFirmwareValidationStatusFsmStageStageStatus": cfprFirmwareValidationStatusFsmStageStageStatus,
       "cfprFirmwareValidationStatusFsmTaskTable": cfprFirmwareValidationStatusFsmTaskTable,
       "cfprFirmwareValidationStatusFsmTaskEntry": cfprFirmwareValidationStatusFsmTaskEntry,
       "cfprFirmwareValidationStatusFsmTaskInstanceId": cfprFirmwareValidationStatusFsmTaskInstanceId,
       "cfprFirmwareValidationStatusFsmTaskDn": cfprFirmwareValidationStatusFsmTaskDn,
       "cfprFirmwareValidationStatusFsmTaskRn": cfprFirmwareValidationStatusFsmTaskRn,
       "cfprFirmwareValidationStatusFsmTaskCompletion": cfprFirmwareValidationStatusFsmTaskCompletion,
       "cfprFirmwareValidationStatusFsmTaskFlags": cfprFirmwareValidationStatusFsmTaskFlags,
       "cfprFirmwareValidationStatusFsmTaskItem": cfprFirmwareValidationStatusFsmTaskItem,
       "cfprFirmwareValidationStatusFsmTaskSeqId": cfprFirmwareValidationStatusFsmTaskSeqId,
       "cfprFirmwareActivateIssueTable": cfprFirmwareActivateIssueTable,
       "cfprFirmwareActivateIssueEntry": cfprFirmwareActivateIssueEntry,
       "cfprFirmwareActivateIssueInstanceId": cfprFirmwareActivateIssueInstanceId,
       "cfprFirmwareActivateIssueDn": cfprFirmwareActivateIssueDn,
       "cfprFirmwareActivateIssueRn": cfprFirmwareActivateIssueRn,
       "cfprFirmwareActivateIssueIsActivationRequired": cfprFirmwareActivateIssueIsActivationRequired,
       "cfprFirmwareMgrVersionMismatchTable": cfprFirmwareMgrVersionMismatchTable,
       "cfprFirmwareMgrVersionMismatchEntry": cfprFirmwareMgrVersionMismatchEntry,
       "cfprFirmwareMgrVersionMismatchInstanceId": cfprFirmwareMgrVersionMismatchInstanceId,
       "cfprFirmwareMgrVersionMismatchDn": cfprFirmwareMgrVersionMismatchDn,
       "cfprFirmwareMgrVersionMismatchRn": cfprFirmwareMgrVersionMismatchRn,
       "cfprFirmwareMgrVersionMismatchIsMgrVersionMismatch": cfprFirmwareMgrVersionMismatchIsMgrVersionMismatch,
       "cfprFirmwareVersionIssueTable": cfprFirmwareVersionIssueTable,
       "cfprFirmwareVersionIssueEntry": cfprFirmwareVersionIssueEntry,
       "cfprFirmwareVersionIssueInstanceId": cfprFirmwareVersionIssueInstanceId,
       "cfprFirmwareVersionIssueDn": cfprFirmwareVersionIssueDn,
       "cfprFirmwareVersionIssueRn": cfprFirmwareVersionIssueRn,
       "cfprFirmwareVersionIssueInstalledImageVersion": cfprFirmwareVersionIssueInstalledImageVersion,
       "cfprFirmwareVersionIssueInstalledPackageVersion": cfprFirmwareVersionIssueInstalledPackageVersion,
       "cfprFirmwareVersionIssueMismatchType": cfprFirmwareVersionIssueMismatchType}
)
