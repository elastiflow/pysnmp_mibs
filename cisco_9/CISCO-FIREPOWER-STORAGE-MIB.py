# SNMP MIB module (CISCO-FIREPOWER-STORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-STORAGE-MIB.mib
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

(CfprAaaConfigState,
 CfprConditionRemoteInvRslt,
 CfprEquipmentOperability,
 CfprEquipmentPowerState,
 CfprEquipmentPresence,
 CfprEquipmentSensorThresholdStatus,
 CfprFabricZoningState,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprFsmLifecycle,
 CfprPolicyPolicyOwner,
 CfprStorageAccessType,
 CfprStorageActualWriteType,
 CfprStorageBatteryType,
 CfprStorageBbuStatus,
 CfprStorageBootableType,
 CfprStorageCacheType,
 CfprStorageConfiguration,
 CfprStorageConfiguredWriteType,
 CfprStorageConnectionProtocol,
 CfprStorageControllerFaultMonitoring,
 CfprStorageControllerId,
 CfprStorageControllerStatus,
 CfprStorageControllerType,
 CfprStorageDisklessAction,
 CfprStorageEpAccess,
 CfprStorageEtherIfVlanType,
 CfprStorageFFCardHealth,
 CfprStorageFFCardMode,
 CfprStorageFFCardSizeMismatch,
 CfprStorageFFCardState,
 CfprStorageFFCardSync,
 CfprStorageFFCardWriteEnable,
 CfprStorageFFControllerHealth,
 CfprStorageFFControllerState,
 CfprStorageFFDriveRemovable,
 CfprStorageFFDriveState,
 CfprStorageFFDriveType,
 CfprStorageFFDriveVisible,
 CfprStorageFFFormatRunning,
 CfprStorageFFHasError,
 CfprStorageFFRAIDHealth,
 CfprStorageFFRAIDState,
 CfprStorageFFRWType,
 CfprStorageFFRaidSyncSupport,
 CfprStorageFFSlotENUM,
 CfprStorageFFType,
 CfprStorageFcZoningType,
 CfprStorageFileSystemStatus,
 CfprStorageFlexFlashControllerFsmCurrentFsm,
 CfprStorageFlexFlashControllerFsmStageName,
 CfprStorageFlexFlashControllerFsmTaskItem,
 CfprStorageFlexFlashControllerId,
 CfprStorageIOType,
 CfprStorageIniGroupOperProtocol,
 CfprStorageIniGroupOwner,
 CfprStorageIniGroupProtocol,
 CfprStorageKeyType,
 CfprStorageLearnCycleRequested,
 CfprStorageLearnMode,
 CfprStorageLinkSpeed,
 CfprStorageLocalDiskConfigFlexFlashRAIDReportingState,
 CfprStorageLocalDiskConfigFlexFlashState,
 CfprStorageLocalDiskMode,
 CfprStorageLocalDiskPartitionType,
 CfprStorageLunType,
 CfprStorageOperState,
 CfprStorageOperatingModeType,
 CfprStorageOperationRequestType,
 CfprStorageOperationState,
 CfprStorageOperationStateType,
 CfprStorageOperationType,
 CfprStoragePDriveStatus,
 CfprStoragePowerState,
 CfprStorageProtocol,
 CfprStorageRaidBatteryOperabilityQualifier,
 CfprStorageReadType,
 CfprStorageSystemFsmCurrentFsm,
 CfprStorageSystemFsmStageName,
 CfprStorageSystemFsmTaskItem,
 CfprStorageTargetPath,
 CfprStorageTechnology,
 CfprStorageVDriveState,
 CfprStorageVsanRefSwitchId,
 CfprVnicConfigIssues) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprAaaConfigState",
    "CfprConditionRemoteInvRslt",
    "CfprEquipmentOperability",
    "CfprEquipmentPowerState",
    "CfprEquipmentPresence",
    "CfprEquipmentSensorThresholdStatus",
    "CfprFabricZoningState",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprFsmLifecycle",
    "CfprPolicyPolicyOwner",
    "CfprStorageAccessType",
    "CfprStorageActualWriteType",
    "CfprStorageBatteryType",
    "CfprStorageBbuStatus",
    "CfprStorageBootableType",
    "CfprStorageCacheType",
    "CfprStorageConfiguration",
    "CfprStorageConfiguredWriteType",
    "CfprStorageConnectionProtocol",
    "CfprStorageControllerFaultMonitoring",
    "CfprStorageControllerId",
    "CfprStorageControllerStatus",
    "CfprStorageControllerType",
    "CfprStorageDisklessAction",
    "CfprStorageEpAccess",
    "CfprStorageEtherIfVlanType",
    "CfprStorageFFCardHealth",
    "CfprStorageFFCardMode",
    "CfprStorageFFCardSizeMismatch",
    "CfprStorageFFCardState",
    "CfprStorageFFCardSync",
    "CfprStorageFFCardWriteEnable",
    "CfprStorageFFControllerHealth",
    "CfprStorageFFControllerState",
    "CfprStorageFFDriveRemovable",
    "CfprStorageFFDriveState",
    "CfprStorageFFDriveType",
    "CfprStorageFFDriveVisible",
    "CfprStorageFFFormatRunning",
    "CfprStorageFFHasError",
    "CfprStorageFFRAIDHealth",
    "CfprStorageFFRAIDState",
    "CfprStorageFFRWType",
    "CfprStorageFFRaidSyncSupport",
    "CfprStorageFFSlotENUM",
    "CfprStorageFFType",
    "CfprStorageFcZoningType",
    "CfprStorageFileSystemStatus",
    "CfprStorageFlexFlashControllerFsmCurrentFsm",
    "CfprStorageFlexFlashControllerFsmStageName",
    "CfprStorageFlexFlashControllerFsmTaskItem",
    "CfprStorageFlexFlashControllerId",
    "CfprStorageIOType",
    "CfprStorageIniGroupOperProtocol",
    "CfprStorageIniGroupOwner",
    "CfprStorageIniGroupProtocol",
    "CfprStorageKeyType",
    "CfprStorageLearnCycleRequested",
    "CfprStorageLearnMode",
    "CfprStorageLinkSpeed",
    "CfprStorageLocalDiskConfigFlexFlashRAIDReportingState",
    "CfprStorageLocalDiskConfigFlexFlashState",
    "CfprStorageLocalDiskMode",
    "CfprStorageLocalDiskPartitionType",
    "CfprStorageLunType",
    "CfprStorageOperState",
    "CfprStorageOperatingModeType",
    "CfprStorageOperationRequestType",
    "CfprStorageOperationState",
    "CfprStorageOperationStateType",
    "CfprStorageOperationType",
    "CfprStoragePDriveStatus",
    "CfprStoragePowerState",
    "CfprStorageProtocol",
    "CfprStorageRaidBatteryOperabilityQualifier",
    "CfprStorageReadType",
    "CfprStorageSystemFsmCurrentFsm",
    "CfprStorageSystemFsmStageName",
    "CfprStorageSystemFsmTaskItem",
    "CfprStorageTargetPath",
    "CfprStorageTechnology",
    "CfprStorageVDriveState",
    "CfprStorageVsanRefSwitchId",
    "CfprVnicConfigIssues")

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

cfprStorageObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprStorageAuthKeyTable_Object = MibTable
cfprStorageAuthKeyTable = _CfprStorageAuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1)
)
if mibBuilder.loadTexts:
    cfprStorageAuthKeyTable.setStatus("current")
_CfprStorageAuthKeyEntry_Object = MibTableRow
cfprStorageAuthKeyEntry = _CfprStorageAuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1, 1)
)
cfprStorageAuthKeyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageAuthKeyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageAuthKeyEntry.setStatus("current")
_CfprStorageAuthKeyInstanceId_Type = CfprManagedObjectId
_CfprStorageAuthKeyInstanceId_Object = MibTableColumn
cfprStorageAuthKeyInstanceId = _CfprStorageAuthKeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1, 1, 1),
    _CfprStorageAuthKeyInstanceId_Type()
)
cfprStorageAuthKeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageAuthKeyInstanceId.setStatus("current")
_CfprStorageAuthKeyDn_Type = CfprManagedObjectDn
_CfprStorageAuthKeyDn_Object = MibTableColumn
cfprStorageAuthKeyDn = _CfprStorageAuthKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1, 1, 2),
    _CfprStorageAuthKeyDn_Type()
)
cfprStorageAuthKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageAuthKeyDn.setStatus("current")
_CfprStorageAuthKeyRn_Type = SnmpAdminString
_CfprStorageAuthKeyRn_Object = MibTableColumn
cfprStorageAuthKeyRn = _CfprStorageAuthKeyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1, 1, 3),
    _CfprStorageAuthKeyRn_Type()
)
cfprStorageAuthKeyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageAuthKeyRn.setStatus("current")
_CfprStorageAuthKeyDescr_Type = SnmpAdminString
_CfprStorageAuthKeyDescr_Object = MibTableColumn
cfprStorageAuthKeyDescr = _CfprStorageAuthKeyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1, 1, 4),
    _CfprStorageAuthKeyDescr_Type()
)
cfprStorageAuthKeyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageAuthKeyDescr.setStatus("current")
_CfprStorageAuthKeyIntId_Type = SnmpAdminString
_CfprStorageAuthKeyIntId_Object = MibTableColumn
cfprStorageAuthKeyIntId = _CfprStorageAuthKeyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1, 1, 5),
    _CfprStorageAuthKeyIntId_Type()
)
cfprStorageAuthKeyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageAuthKeyIntId.setStatus("current")
_CfprStorageAuthKeyName_Type = SnmpAdminString
_CfprStorageAuthKeyName_Object = MibTableColumn
cfprStorageAuthKeyName = _CfprStorageAuthKeyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1, 1, 6),
    _CfprStorageAuthKeyName_Type()
)
cfprStorageAuthKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageAuthKeyName.setStatus("current")
_CfprStorageAuthKeyPassword_Type = SnmpAdminString
_CfprStorageAuthKeyPassword_Object = MibTableColumn
cfprStorageAuthKeyPassword = _CfprStorageAuthKeyPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1, 1, 7),
    _CfprStorageAuthKeyPassword_Type()
)
cfprStorageAuthKeyPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageAuthKeyPassword.setStatus("current")
_CfprStorageAuthKeyPolicyLevel_Type = Gauge32
_CfprStorageAuthKeyPolicyLevel_Object = MibTableColumn
cfprStorageAuthKeyPolicyLevel = _CfprStorageAuthKeyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1, 1, 8),
    _CfprStorageAuthKeyPolicyLevel_Type()
)
cfprStorageAuthKeyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageAuthKeyPolicyLevel.setStatus("current")
_CfprStorageAuthKeyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStorageAuthKeyPolicyOwner_Object = MibTableColumn
cfprStorageAuthKeyPolicyOwner = _CfprStorageAuthKeyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1, 1, 9),
    _CfprStorageAuthKeyPolicyOwner_Type()
)
cfprStorageAuthKeyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageAuthKeyPolicyOwner.setStatus("current")
_CfprStorageAuthKeyType_Type = CfprStorageKeyType
_CfprStorageAuthKeyType_Object = MibTableColumn
cfprStorageAuthKeyType = _CfprStorageAuthKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1, 1, 10),
    _CfprStorageAuthKeyType_Type()
)
cfprStorageAuthKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageAuthKeyType.setStatus("current")
_CfprStorageAuthKeyUserId_Type = SnmpAdminString
_CfprStorageAuthKeyUserId_Object = MibTableColumn
cfprStorageAuthKeyUserId = _CfprStorageAuthKeyUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 1, 1, 11),
    _CfprStorageAuthKeyUserId_Type()
)
cfprStorageAuthKeyUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageAuthKeyUserId.setStatus("current")
_CfprStorageConnectionDefTable_Object = MibTable
cfprStorageConnectionDefTable = _CfprStorageConnectionDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 2)
)
if mibBuilder.loadTexts:
    cfprStorageConnectionDefTable.setStatus("current")
_CfprStorageConnectionDefEntry_Object = MibTableRow
cfprStorageConnectionDefEntry = _CfprStorageConnectionDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 2, 1)
)
cfprStorageConnectionDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageConnectionDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageConnectionDefEntry.setStatus("current")
_CfprStorageConnectionDefInstanceId_Type = CfprManagedObjectId
_CfprStorageConnectionDefInstanceId_Object = MibTableColumn
cfprStorageConnectionDefInstanceId = _CfprStorageConnectionDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 2, 1, 1),
    _CfprStorageConnectionDefInstanceId_Type()
)
cfprStorageConnectionDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageConnectionDefInstanceId.setStatus("current")
_CfprStorageConnectionDefDn_Type = CfprManagedObjectDn
_CfprStorageConnectionDefDn_Object = MibTableColumn
cfprStorageConnectionDefDn = _CfprStorageConnectionDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 2, 1, 2),
    _CfprStorageConnectionDefDn_Type()
)
cfprStorageConnectionDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionDefDn.setStatus("current")
_CfprStorageConnectionDefRn_Type = SnmpAdminString
_CfprStorageConnectionDefRn_Object = MibTableColumn
cfprStorageConnectionDefRn = _CfprStorageConnectionDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 2, 1, 3),
    _CfprStorageConnectionDefRn_Type()
)
cfprStorageConnectionDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionDefRn.setStatus("current")
_CfprStorageConnectionDefDescr_Type = SnmpAdminString
_CfprStorageConnectionDefDescr_Object = MibTableColumn
cfprStorageConnectionDefDescr = _CfprStorageConnectionDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 2, 1, 4),
    _CfprStorageConnectionDefDescr_Type()
)
cfprStorageConnectionDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionDefDescr.setStatus("current")
_CfprStorageConnectionDefIntId_Type = SnmpAdminString
_CfprStorageConnectionDefIntId_Object = MibTableColumn
cfprStorageConnectionDefIntId = _CfprStorageConnectionDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 2, 1, 5),
    _CfprStorageConnectionDefIntId_Type()
)
cfprStorageConnectionDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionDefIntId.setStatus("current")
_CfprStorageConnectionDefName_Type = SnmpAdminString
_CfprStorageConnectionDefName_Object = MibTableColumn
cfprStorageConnectionDefName = _CfprStorageConnectionDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 2, 1, 6),
    _CfprStorageConnectionDefName_Type()
)
cfprStorageConnectionDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionDefName.setStatus("current")
_CfprStorageConnectionDefOperState_Type = CfprStorageOperState
_CfprStorageConnectionDefOperState_Object = MibTableColumn
cfprStorageConnectionDefOperState = _CfprStorageConnectionDefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 2, 1, 7),
    _CfprStorageConnectionDefOperState_Type()
)
cfprStorageConnectionDefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionDefOperState.setStatus("current")
_CfprStorageConnectionDefPolicyLevel_Type = Gauge32
_CfprStorageConnectionDefPolicyLevel_Object = MibTableColumn
cfprStorageConnectionDefPolicyLevel = _CfprStorageConnectionDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 2, 1, 8),
    _CfprStorageConnectionDefPolicyLevel_Type()
)
cfprStorageConnectionDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionDefPolicyLevel.setStatus("current")
_CfprStorageConnectionDefPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStorageConnectionDefPolicyOwner_Object = MibTableColumn
cfprStorageConnectionDefPolicyOwner = _CfprStorageConnectionDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 2, 1, 9),
    _CfprStorageConnectionDefPolicyOwner_Type()
)
cfprStorageConnectionDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionDefPolicyOwner.setStatus("current")
_CfprStorageConnectionDefZoningType_Type = CfprStorageFcZoningType
_CfprStorageConnectionDefZoningType_Object = MibTableColumn
cfprStorageConnectionDefZoningType = _CfprStorageConnectionDefZoningType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 2, 1, 10),
    _CfprStorageConnectionDefZoningType_Type()
)
cfprStorageConnectionDefZoningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionDefZoningType.setStatus("current")
_CfprStorageConnectionPolicyTable_Object = MibTable
cfprStorageConnectionPolicyTable = _CfprStorageConnectionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 3)
)
if mibBuilder.loadTexts:
    cfprStorageConnectionPolicyTable.setStatus("current")
_CfprStorageConnectionPolicyEntry_Object = MibTableRow
cfprStorageConnectionPolicyEntry = _CfprStorageConnectionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 3, 1)
)
cfprStorageConnectionPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageConnectionPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageConnectionPolicyEntry.setStatus("current")
_CfprStorageConnectionPolicyInstanceId_Type = CfprManagedObjectId
_CfprStorageConnectionPolicyInstanceId_Object = MibTableColumn
cfprStorageConnectionPolicyInstanceId = _CfprStorageConnectionPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 3, 1, 1),
    _CfprStorageConnectionPolicyInstanceId_Type()
)
cfprStorageConnectionPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageConnectionPolicyInstanceId.setStatus("current")
_CfprStorageConnectionPolicyDn_Type = CfprManagedObjectDn
_CfprStorageConnectionPolicyDn_Object = MibTableColumn
cfprStorageConnectionPolicyDn = _CfprStorageConnectionPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 3, 1, 2),
    _CfprStorageConnectionPolicyDn_Type()
)
cfprStorageConnectionPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionPolicyDn.setStatus("current")
_CfprStorageConnectionPolicyRn_Type = SnmpAdminString
_CfprStorageConnectionPolicyRn_Object = MibTableColumn
cfprStorageConnectionPolicyRn = _CfprStorageConnectionPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 3, 1, 3),
    _CfprStorageConnectionPolicyRn_Type()
)
cfprStorageConnectionPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionPolicyRn.setStatus("current")
_CfprStorageConnectionPolicyDescr_Type = SnmpAdminString
_CfprStorageConnectionPolicyDescr_Object = MibTableColumn
cfprStorageConnectionPolicyDescr = _CfprStorageConnectionPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 3, 1, 4),
    _CfprStorageConnectionPolicyDescr_Type()
)
cfprStorageConnectionPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionPolicyDescr.setStatus("current")
_CfprStorageConnectionPolicyIntId_Type = SnmpAdminString
_CfprStorageConnectionPolicyIntId_Object = MibTableColumn
cfprStorageConnectionPolicyIntId = _CfprStorageConnectionPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 3, 1, 5),
    _CfprStorageConnectionPolicyIntId_Type()
)
cfprStorageConnectionPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionPolicyIntId.setStatus("current")
_CfprStorageConnectionPolicyName_Type = SnmpAdminString
_CfprStorageConnectionPolicyName_Object = MibTableColumn
cfprStorageConnectionPolicyName = _CfprStorageConnectionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 3, 1, 6),
    _CfprStorageConnectionPolicyName_Type()
)
cfprStorageConnectionPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionPolicyName.setStatus("current")
_CfprStorageConnectionPolicyOperState_Type = CfprStorageOperState
_CfprStorageConnectionPolicyOperState_Object = MibTableColumn
cfprStorageConnectionPolicyOperState = _CfprStorageConnectionPolicyOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 3, 1, 7),
    _CfprStorageConnectionPolicyOperState_Type()
)
cfprStorageConnectionPolicyOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionPolicyOperState.setStatus("current")
_CfprStorageConnectionPolicyPolicyLevel_Type = Gauge32
_CfprStorageConnectionPolicyPolicyLevel_Object = MibTableColumn
cfprStorageConnectionPolicyPolicyLevel = _CfprStorageConnectionPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 3, 1, 8),
    _CfprStorageConnectionPolicyPolicyLevel_Type()
)
cfprStorageConnectionPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionPolicyPolicyLevel.setStatus("current")
_CfprStorageConnectionPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStorageConnectionPolicyPolicyOwner_Object = MibTableColumn
cfprStorageConnectionPolicyPolicyOwner = _CfprStorageConnectionPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 3, 1, 9),
    _CfprStorageConnectionPolicyPolicyOwner_Type()
)
cfprStorageConnectionPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionPolicyPolicyOwner.setStatus("current")
_CfprStorageConnectionPolicyZoningType_Type = CfprStorageFcZoningType
_CfprStorageConnectionPolicyZoningType_Object = MibTableColumn
cfprStorageConnectionPolicyZoningType = _CfprStorageConnectionPolicyZoningType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 3, 1, 10),
    _CfprStorageConnectionPolicyZoningType_Type()
)
cfprStorageConnectionPolicyZoningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageConnectionPolicyZoningType.setStatus("current")
_CfprStorageControllerTable_Object = MibTable
cfprStorageControllerTable = _CfprStorageControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4)
)
if mibBuilder.loadTexts:
    cfprStorageControllerTable.setStatus("current")
_CfprStorageControllerEntry_Object = MibTableRow
cfprStorageControllerEntry = _CfprStorageControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1)
)
cfprStorageControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageControllerEntry.setStatus("current")
_CfprStorageControllerInstanceId_Type = CfprManagedObjectId
_CfprStorageControllerInstanceId_Object = MibTableColumn
cfprStorageControllerInstanceId = _CfprStorageControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 1),
    _CfprStorageControllerInstanceId_Type()
)
cfprStorageControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageControllerInstanceId.setStatus("current")
_CfprStorageControllerDn_Type = CfprManagedObjectDn
_CfprStorageControllerDn_Object = MibTableColumn
cfprStorageControllerDn = _CfprStorageControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 2),
    _CfprStorageControllerDn_Type()
)
cfprStorageControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerDn.setStatus("current")
_CfprStorageControllerRn_Type = SnmpAdminString
_CfprStorageControllerRn_Object = MibTableColumn
cfprStorageControllerRn = _CfprStorageControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 3),
    _CfprStorageControllerRn_Type()
)
cfprStorageControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerRn.setStatus("current")
_CfprStorageControllerControllerStatus_Type = CfprStorageControllerStatus
_CfprStorageControllerControllerStatus_Object = MibTableColumn
cfprStorageControllerControllerStatus = _CfprStorageControllerControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 4),
    _CfprStorageControllerControllerStatus_Type()
)
cfprStorageControllerControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerControllerStatus.setStatus("current")
_CfprStorageControllerDeviceRaidSupport_Type = SnmpAdminString
_CfprStorageControllerDeviceRaidSupport_Object = MibTableColumn
cfprStorageControllerDeviceRaidSupport = _CfprStorageControllerDeviceRaidSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 5),
    _CfprStorageControllerDeviceRaidSupport_Type()
)
cfprStorageControllerDeviceRaidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerDeviceRaidSupport.setStatus("current")
_CfprStorageControllerFaultMonitoring_Type = CfprStorageControllerFaultMonitoring
_CfprStorageControllerFaultMonitoring_Object = MibTableColumn
cfprStorageControllerFaultMonitoring = _CfprStorageControllerFaultMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 6),
    _CfprStorageControllerFaultMonitoring_Type()
)
cfprStorageControllerFaultMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerFaultMonitoring.setStatus("current")
_CfprStorageControllerHwRevision_Type = SnmpAdminString
_CfprStorageControllerHwRevision_Object = MibTableColumn
cfprStorageControllerHwRevision = _CfprStorageControllerHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 7),
    _CfprStorageControllerHwRevision_Type()
)
cfprStorageControllerHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerHwRevision.setStatus("current")
_CfprStorageControllerId_Type = CfprStorageControllerId
_CfprStorageControllerId_Object = MibTableColumn
cfprStorageControllerId = _CfprStorageControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 8),
    _CfprStorageControllerId_Type()
)
cfprStorageControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerId.setStatus("current")
_CfprStorageControllerLc_Type = CfprFsmLifecycle
_CfprStorageControllerLc_Object = MibTableColumn
cfprStorageControllerLc = _CfprStorageControllerLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 9),
    _CfprStorageControllerLc_Type()
)
cfprStorageControllerLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerLc.setStatus("current")
_CfprStorageControllerLocationDn_Type = SnmpAdminString
_CfprStorageControllerLocationDn_Object = MibTableColumn
cfprStorageControllerLocationDn = _CfprStorageControllerLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 10),
    _CfprStorageControllerLocationDn_Type()
)
cfprStorageControllerLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerLocationDn.setStatus("current")
_CfprStorageControllerModel_Type = SnmpAdminString
_CfprStorageControllerModel_Object = MibTableColumn
cfprStorageControllerModel = _CfprStorageControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 11),
    _CfprStorageControllerModel_Type()
)
cfprStorageControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerModel.setStatus("current")
_CfprStorageControllerOobControllerId_Type = Gauge32
_CfprStorageControllerOobControllerId_Object = MibTableColumn
cfprStorageControllerOobControllerId = _CfprStorageControllerOobControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 12),
    _CfprStorageControllerOobControllerId_Type()
)
cfprStorageControllerOobControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerOobControllerId.setStatus("current")
_CfprStorageControllerOobInterfaceSupported_Type = TruthValue
_CfprStorageControllerOobInterfaceSupported_Object = MibTableColumn
cfprStorageControllerOobInterfaceSupported = _CfprStorageControllerOobInterfaceSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 13),
    _CfprStorageControllerOobInterfaceSupported_Type()
)
cfprStorageControllerOobInterfaceSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerOobInterfaceSupported.setStatus("current")
_CfprStorageControllerOperQualifierReason_Type = SnmpAdminString
_CfprStorageControllerOperQualifierReason_Object = MibTableColumn
cfprStorageControllerOperQualifierReason = _CfprStorageControllerOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 14),
    _CfprStorageControllerOperQualifierReason_Type()
)
cfprStorageControllerOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerOperQualifierReason.setStatus("current")
_CfprStorageControllerOperState_Type = CfprEquipmentOperability
_CfprStorageControllerOperState_Object = MibTableColumn
cfprStorageControllerOperState = _CfprStorageControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 15),
    _CfprStorageControllerOperState_Type()
)
cfprStorageControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerOperState.setStatus("current")
_CfprStorageControllerOperability_Type = CfprEquipmentOperability
_CfprStorageControllerOperability_Object = MibTableColumn
cfprStorageControllerOperability = _CfprStorageControllerOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 16),
    _CfprStorageControllerOperability_Type()
)
cfprStorageControllerOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerOperability.setStatus("current")
_CfprStorageControllerPartNumber_Type = SnmpAdminString
_CfprStorageControllerPartNumber_Object = MibTableColumn
cfprStorageControllerPartNumber = _CfprStorageControllerPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 17),
    _CfprStorageControllerPartNumber_Type()
)
cfprStorageControllerPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerPartNumber.setStatus("current")
_CfprStorageControllerPciAddr_Type = SnmpAdminString
_CfprStorageControllerPciAddr_Object = MibTableColumn
cfprStorageControllerPciAddr = _CfprStorageControllerPciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 18),
    _CfprStorageControllerPciAddr_Type()
)
cfprStorageControllerPciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerPciAddr.setStatus("current")
_CfprStorageControllerPciSlot_Type = SnmpAdminString
_CfprStorageControllerPciSlot_Object = MibTableColumn
cfprStorageControllerPciSlot = _CfprStorageControllerPciSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 19),
    _CfprStorageControllerPciSlot_Type()
)
cfprStorageControllerPciSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerPciSlot.setStatus("current")
_CfprStorageControllerPerf_Type = CfprEquipmentSensorThresholdStatus
_CfprStorageControllerPerf_Object = MibTableColumn
cfprStorageControllerPerf = _CfprStorageControllerPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 20),
    _CfprStorageControllerPerf_Type()
)
cfprStorageControllerPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerPerf.setStatus("current")
_CfprStorageControllerPower_Type = CfprEquipmentPowerState
_CfprStorageControllerPower_Object = MibTableColumn
cfprStorageControllerPower = _CfprStorageControllerPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 21),
    _CfprStorageControllerPower_Type()
)
cfprStorageControllerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerPower.setStatus("current")
_CfprStorageControllerPresence_Type = CfprEquipmentPresence
_CfprStorageControllerPresence_Object = MibTableColumn
cfprStorageControllerPresence = _CfprStorageControllerPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 22),
    _CfprStorageControllerPresence_Type()
)
cfprStorageControllerPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerPresence.setStatus("current")
_CfprStorageControllerRaidSupport_Type = SnmpAdminString
_CfprStorageControllerRaidSupport_Object = MibTableColumn
cfprStorageControllerRaidSupport = _CfprStorageControllerRaidSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 23),
    _CfprStorageControllerRaidSupport_Type()
)
cfprStorageControllerRaidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerRaidSupport.setStatus("current")
_CfprStorageControllerRebuildRate_Type = Gauge32
_CfprStorageControllerRebuildRate_Object = MibTableColumn
cfprStorageControllerRebuildRate = _CfprStorageControllerRebuildRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 24),
    _CfprStorageControllerRebuildRate_Type()
)
cfprStorageControllerRebuildRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerRebuildRate.setStatus("current")
_CfprStorageControllerRevision_Type = SnmpAdminString
_CfprStorageControllerRevision_Object = MibTableColumn
cfprStorageControllerRevision = _CfprStorageControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 25),
    _CfprStorageControllerRevision_Type()
)
cfprStorageControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerRevision.setStatus("current")
_CfprStorageControllerSerial_Type = SnmpAdminString
_CfprStorageControllerSerial_Object = MibTableColumn
cfprStorageControllerSerial = _CfprStorageControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 26),
    _CfprStorageControllerSerial_Type()
)
cfprStorageControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerSerial.setStatus("current")
_CfprStorageControllerThermal_Type = CfprEquipmentSensorThresholdStatus
_CfprStorageControllerThermal_Object = MibTableColumn
cfprStorageControllerThermal = _CfprStorageControllerThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 27),
    _CfprStorageControllerThermal_Type()
)
cfprStorageControllerThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerThermal.setStatus("current")
_CfprStorageControllerType_Type = CfprStorageControllerType
_CfprStorageControllerType_Object = MibTableColumn
cfprStorageControllerType = _CfprStorageControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 28),
    _CfprStorageControllerType_Type()
)
cfprStorageControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerType.setStatus("current")
_CfprStorageControllerVendor_Type = SnmpAdminString
_CfprStorageControllerVendor_Object = MibTableColumn
cfprStorageControllerVendor = _CfprStorageControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 29),
    _CfprStorageControllerVendor_Type()
)
cfprStorageControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerVendor.setStatus("current")
_CfprStorageControllerVid_Type = SnmpAdminString
_CfprStorageControllerVid_Object = MibTableColumn
cfprStorageControllerVid = _CfprStorageControllerVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 30),
    _CfprStorageControllerVid_Type()
)
cfprStorageControllerVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerVid.setStatus("current")
_CfprStorageControllerVoltage_Type = CfprEquipmentSensorThresholdStatus
_CfprStorageControllerVoltage_Object = MibTableColumn
cfprStorageControllerVoltage = _CfprStorageControllerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 4, 1, 31),
    _CfprStorageControllerVoltage_Type()
)
cfprStorageControllerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageControllerVoltage.setStatus("current")
_CfprStorageDomainEpTable_Object = MibTable
cfprStorageDomainEpTable = _CfprStorageDomainEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 5)
)
if mibBuilder.loadTexts:
    cfprStorageDomainEpTable.setStatus("current")
_CfprStorageDomainEpEntry_Object = MibTableRow
cfprStorageDomainEpEntry = _CfprStorageDomainEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 5, 1)
)
cfprStorageDomainEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageDomainEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageDomainEpEntry.setStatus("current")
_CfprStorageDomainEpInstanceId_Type = CfprManagedObjectId
_CfprStorageDomainEpInstanceId_Object = MibTableColumn
cfprStorageDomainEpInstanceId = _CfprStorageDomainEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 5, 1, 1),
    _CfprStorageDomainEpInstanceId_Type()
)
cfprStorageDomainEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageDomainEpInstanceId.setStatus("current")
_CfprStorageDomainEpDn_Type = CfprManagedObjectDn
_CfprStorageDomainEpDn_Object = MibTableColumn
cfprStorageDomainEpDn = _CfprStorageDomainEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 5, 1, 2),
    _CfprStorageDomainEpDn_Type()
)
cfprStorageDomainEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageDomainEpDn.setStatus("current")
_CfprStorageDomainEpRn_Type = SnmpAdminString
_CfprStorageDomainEpRn_Object = MibTableColumn
cfprStorageDomainEpRn = _CfprStorageDomainEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 5, 1, 3),
    _CfprStorageDomainEpRn_Type()
)
cfprStorageDomainEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageDomainEpRn.setStatus("current")
_CfprStorageDriveTable_Object = MibTable
cfprStorageDriveTable = _CfprStorageDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 6)
)
if mibBuilder.loadTexts:
    cfprStorageDriveTable.setStatus("current")
_CfprStorageDriveEntry_Object = MibTableRow
cfprStorageDriveEntry = _CfprStorageDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 6, 1)
)
cfprStorageDriveEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageDriveInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageDriveEntry.setStatus("current")
_CfprStorageDriveInstanceId_Type = CfprManagedObjectId
_CfprStorageDriveInstanceId_Object = MibTableColumn
cfprStorageDriveInstanceId = _CfprStorageDriveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 6, 1, 1),
    _CfprStorageDriveInstanceId_Type()
)
cfprStorageDriveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageDriveInstanceId.setStatus("current")
_CfprStorageDriveDn_Type = CfprManagedObjectDn
_CfprStorageDriveDn_Object = MibTableColumn
cfprStorageDriveDn = _CfprStorageDriveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 6, 1, 2),
    _CfprStorageDriveDn_Type()
)
cfprStorageDriveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageDriveDn.setStatus("current")
_CfprStorageDriveRn_Type = SnmpAdminString
_CfprStorageDriveRn_Object = MibTableColumn
cfprStorageDriveRn = _CfprStorageDriveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 6, 1, 3),
    _CfprStorageDriveRn_Type()
)
cfprStorageDriveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageDriveRn.setStatus("current")
_CfprStorageDriveId_Type = Gauge32
_CfprStorageDriveId_Object = MibTableColumn
cfprStorageDriveId = _CfprStorageDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 6, 1, 4),
    _CfprStorageDriveId_Type()
)
cfprStorageDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageDriveId.setStatus("current")
_CfprStorageDriveModel_Type = SnmpAdminString
_CfprStorageDriveModel_Object = MibTableColumn
cfprStorageDriveModel = _CfprStorageDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 6, 1, 5),
    _CfprStorageDriveModel_Type()
)
cfprStorageDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageDriveModel.setStatus("current")
_CfprStorageDrivePciAddr_Type = SnmpAdminString
_CfprStorageDrivePciAddr_Object = MibTableColumn
cfprStorageDrivePciAddr = _CfprStorageDrivePciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 6, 1, 6),
    _CfprStorageDrivePciAddr_Type()
)
cfprStorageDrivePciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageDrivePciAddr.setStatus("current")
_CfprStorageDriveRevision_Type = SnmpAdminString
_CfprStorageDriveRevision_Object = MibTableColumn
cfprStorageDriveRevision = _CfprStorageDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 6, 1, 7),
    _CfprStorageDriveRevision_Type()
)
cfprStorageDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageDriveRevision.setStatus("current")
_CfprStorageDriveSerial_Type = SnmpAdminString
_CfprStorageDriveSerial_Object = MibTableColumn
cfprStorageDriveSerial = _CfprStorageDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 6, 1, 8),
    _CfprStorageDriveSerial_Type()
)
cfprStorageDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageDriveSerial.setStatus("current")
_CfprStorageDriveVendor_Type = SnmpAdminString
_CfprStorageDriveVendor_Object = MibTableColumn
cfprStorageDriveVendor = _CfprStorageDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 6, 1, 9),
    _CfprStorageDriveVendor_Type()
)
cfprStorageDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageDriveVendor.setStatus("current")
_CfprStorageEnclosureTable_Object = MibTable
cfprStorageEnclosureTable = _CfprStorageEnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 7)
)
if mibBuilder.loadTexts:
    cfprStorageEnclosureTable.setStatus("current")
_CfprStorageEnclosureEntry_Object = MibTableRow
cfprStorageEnclosureEntry = _CfprStorageEnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 7, 1)
)
cfprStorageEnclosureEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageEnclosureInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageEnclosureEntry.setStatus("current")
_CfprStorageEnclosureInstanceId_Type = CfprManagedObjectId
_CfprStorageEnclosureInstanceId_Object = MibTableColumn
cfprStorageEnclosureInstanceId = _CfprStorageEnclosureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 7, 1, 1),
    _CfprStorageEnclosureInstanceId_Type()
)
cfprStorageEnclosureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageEnclosureInstanceId.setStatus("current")
_CfprStorageEnclosureDn_Type = CfprManagedObjectDn
_CfprStorageEnclosureDn_Object = MibTableColumn
cfprStorageEnclosureDn = _CfprStorageEnclosureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 7, 1, 2),
    _CfprStorageEnclosureDn_Type()
)
cfprStorageEnclosureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEnclosureDn.setStatus("current")
_CfprStorageEnclosureRn_Type = SnmpAdminString
_CfprStorageEnclosureRn_Object = MibTableColumn
cfprStorageEnclosureRn = _CfprStorageEnclosureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 7, 1, 3),
    _CfprStorageEnclosureRn_Type()
)
cfprStorageEnclosureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEnclosureRn.setStatus("current")
_CfprStorageEnclosureId_Type = Gauge32
_CfprStorageEnclosureId_Object = MibTableColumn
cfprStorageEnclosureId = _CfprStorageEnclosureId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 7, 1, 4),
    _CfprStorageEnclosureId_Type()
)
cfprStorageEnclosureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEnclosureId.setStatus("current")
_CfprStorageEnclosureLc_Type = CfprFsmLifecycle
_CfprStorageEnclosureLc_Object = MibTableColumn
cfprStorageEnclosureLc = _CfprStorageEnclosureLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 7, 1, 5),
    _CfprStorageEnclosureLc_Type()
)
cfprStorageEnclosureLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEnclosureLc.setStatus("current")
_CfprStorageEnclosureModel_Type = SnmpAdminString
_CfprStorageEnclosureModel_Object = MibTableColumn
cfprStorageEnclosureModel = _CfprStorageEnclosureModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 7, 1, 6),
    _CfprStorageEnclosureModel_Type()
)
cfprStorageEnclosureModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEnclosureModel.setStatus("current")
_CfprStorageEnclosureNumSlots_Type = Gauge32
_CfprStorageEnclosureNumSlots_Object = MibTableColumn
cfprStorageEnclosureNumSlots = _CfprStorageEnclosureNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 7, 1, 7),
    _CfprStorageEnclosureNumSlots_Type()
)
cfprStorageEnclosureNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEnclosureNumSlots.setStatus("current")
_CfprStorageEnclosureRevision_Type = SnmpAdminString
_CfprStorageEnclosureRevision_Object = MibTableColumn
cfprStorageEnclosureRevision = _CfprStorageEnclosureRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 7, 1, 8),
    _CfprStorageEnclosureRevision_Type()
)
cfprStorageEnclosureRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEnclosureRevision.setStatus("current")
_CfprStorageEnclosureSerial_Type = SnmpAdminString
_CfprStorageEnclosureSerial_Object = MibTableColumn
cfprStorageEnclosureSerial = _CfprStorageEnclosureSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 7, 1, 9),
    _CfprStorageEnclosureSerial_Type()
)
cfprStorageEnclosureSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEnclosureSerial.setStatus("current")
_CfprStorageEnclosureVendor_Type = SnmpAdminString
_CfprStorageEnclosureVendor_Object = MibTableColumn
cfprStorageEnclosureVendor = _CfprStorageEnclosureVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 7, 1, 10),
    _CfprStorageEnclosureVendor_Type()
)
cfprStorageEnclosureVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEnclosureVendor.setStatus("current")
_CfprStorageEpUserTable_Object = MibTable
cfprStorageEpUserTable = _CfprStorageEpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8)
)
if mibBuilder.loadTexts:
    cfprStorageEpUserTable.setStatus("current")
_CfprStorageEpUserEntry_Object = MibTableRow
cfprStorageEpUserEntry = _CfprStorageEpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8, 1)
)
cfprStorageEpUserEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageEpUserInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageEpUserEntry.setStatus("current")
_CfprStorageEpUserInstanceId_Type = CfprManagedObjectId
_CfprStorageEpUserInstanceId_Object = MibTableColumn
cfprStorageEpUserInstanceId = _CfprStorageEpUserInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8, 1, 1),
    _CfprStorageEpUserInstanceId_Type()
)
cfprStorageEpUserInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageEpUserInstanceId.setStatus("current")
_CfprStorageEpUserDn_Type = CfprManagedObjectDn
_CfprStorageEpUserDn_Object = MibTableColumn
cfprStorageEpUserDn = _CfprStorageEpUserDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8, 1, 2),
    _CfprStorageEpUserDn_Type()
)
cfprStorageEpUserDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEpUserDn.setStatus("current")
_CfprStorageEpUserRn_Type = SnmpAdminString
_CfprStorageEpUserRn_Object = MibTableColumn
cfprStorageEpUserRn = _CfprStorageEpUserRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8, 1, 3),
    _CfprStorageEpUserRn_Type()
)
cfprStorageEpUserRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEpUserRn.setStatus("current")
_CfprStorageEpUserConfigState_Type = CfprAaaConfigState
_CfprStorageEpUserConfigState_Object = MibTableColumn
cfprStorageEpUserConfigState = _CfprStorageEpUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8, 1, 4),
    _CfprStorageEpUserConfigState_Type()
)
cfprStorageEpUserConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEpUserConfigState.setStatus("current")
_CfprStorageEpUserConfigStatusMessage_Type = SnmpAdminString
_CfprStorageEpUserConfigStatusMessage_Object = MibTableColumn
cfprStorageEpUserConfigStatusMessage = _CfprStorageEpUserConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8, 1, 5),
    _CfprStorageEpUserConfigStatusMessage_Type()
)
cfprStorageEpUserConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEpUserConfigStatusMessage.setStatus("current")
_CfprStorageEpUserDescr_Type = SnmpAdminString
_CfprStorageEpUserDescr_Object = MibTableColumn
cfprStorageEpUserDescr = _CfprStorageEpUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8, 1, 6),
    _CfprStorageEpUserDescr_Type()
)
cfprStorageEpUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEpUserDescr.setStatus("current")
_CfprStorageEpUserDomain_Type = SnmpAdminString
_CfprStorageEpUserDomain_Object = MibTableColumn
cfprStorageEpUserDomain = _CfprStorageEpUserDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8, 1, 7),
    _CfprStorageEpUserDomain_Type()
)
cfprStorageEpUserDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEpUserDomain.setStatus("current")
_CfprStorageEpUserName_Type = SnmpAdminString
_CfprStorageEpUserName_Object = MibTableColumn
cfprStorageEpUserName = _CfprStorageEpUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8, 1, 8),
    _CfprStorageEpUserName_Type()
)
cfprStorageEpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEpUserName.setStatus("current")
_CfprStorageEpUserPriv_Type = CfprStorageEpAccess
_CfprStorageEpUserPriv_Object = MibTableColumn
cfprStorageEpUserPriv = _CfprStorageEpUserPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8, 1, 9),
    _CfprStorageEpUserPriv_Type()
)
cfprStorageEpUserPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEpUserPriv.setStatus("current")
_CfprStorageEpUserPwd_Type = SnmpAdminString
_CfprStorageEpUserPwd_Object = MibTableColumn
cfprStorageEpUserPwd = _CfprStorageEpUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8, 1, 10),
    _CfprStorageEpUserPwd_Type()
)
cfprStorageEpUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEpUserPwd.setStatus("current")
_CfprStorageEpUserPwdSet_Type = TruthValue
_CfprStorageEpUserPwdSet_Object = MibTableColumn
cfprStorageEpUserPwdSet = _CfprStorageEpUserPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 8, 1, 11),
    _CfprStorageEpUserPwdSet_Type()
)
cfprStorageEpUserPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEpUserPwdSet.setStatus("current")
_CfprStorageEtherIfTable_Object = MibTable
cfprStorageEtherIfTable = _CfprStorageEtherIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 9)
)
if mibBuilder.loadTexts:
    cfprStorageEtherIfTable.setStatus("current")
_CfprStorageEtherIfEntry_Object = MibTableRow
cfprStorageEtherIfEntry = _CfprStorageEtherIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 9, 1)
)
cfprStorageEtherIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageEtherIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageEtherIfEntry.setStatus("current")
_CfprStorageEtherIfInstanceId_Type = CfprManagedObjectId
_CfprStorageEtherIfInstanceId_Object = MibTableColumn
cfprStorageEtherIfInstanceId = _CfprStorageEtherIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 9, 1, 1),
    _CfprStorageEtherIfInstanceId_Type()
)
cfprStorageEtherIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageEtherIfInstanceId.setStatus("current")
_CfprStorageEtherIfDn_Type = CfprManagedObjectDn
_CfprStorageEtherIfDn_Object = MibTableColumn
cfprStorageEtherIfDn = _CfprStorageEtherIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 9, 1, 2),
    _CfprStorageEtherIfDn_Type()
)
cfprStorageEtherIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEtherIfDn.setStatus("current")
_CfprStorageEtherIfRn_Type = SnmpAdminString
_CfprStorageEtherIfRn_Object = MibTableColumn
cfprStorageEtherIfRn = _CfprStorageEtherIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 9, 1, 3),
    _CfprStorageEtherIfRn_Type()
)
cfprStorageEtherIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEtherIfRn.setStatus("current")
_CfprStorageEtherIfName_Type = SnmpAdminString
_CfprStorageEtherIfName_Object = MibTableColumn
cfprStorageEtherIfName = _CfprStorageEtherIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 9, 1, 4),
    _CfprStorageEtherIfName_Type()
)
cfprStorageEtherIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEtherIfName.setStatus("current")
_CfprStorageEtherIfVlanType_Type = CfprStorageEtherIfVlanType
_CfprStorageEtherIfVlanType_Object = MibTableColumn
cfprStorageEtherIfVlanType = _CfprStorageEtherIfVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 9, 1, 5),
    _CfprStorageEtherIfVlanType_Type()
)
cfprStorageEtherIfVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageEtherIfVlanType.setStatus("current")
_CfprStorageFcIfTable_Object = MibTable
cfprStorageFcIfTable = _CfprStorageFcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 10)
)
if mibBuilder.loadTexts:
    cfprStorageFcIfTable.setStatus("current")
_CfprStorageFcIfEntry_Object = MibTableRow
cfprStorageFcIfEntry = _CfprStorageFcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 10, 1)
)
cfprStorageFcIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageFcIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageFcIfEntry.setStatus("current")
_CfprStorageFcIfInstanceId_Type = CfprManagedObjectId
_CfprStorageFcIfInstanceId_Object = MibTableColumn
cfprStorageFcIfInstanceId = _CfprStorageFcIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 10, 1, 1),
    _CfprStorageFcIfInstanceId_Type()
)
cfprStorageFcIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageFcIfInstanceId.setStatus("current")
_CfprStorageFcIfDn_Type = CfprManagedObjectDn
_CfprStorageFcIfDn_Object = MibTableColumn
cfprStorageFcIfDn = _CfprStorageFcIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 10, 1, 2),
    _CfprStorageFcIfDn_Type()
)
cfprStorageFcIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFcIfDn.setStatus("current")
_CfprStorageFcIfRn_Type = SnmpAdminString
_CfprStorageFcIfRn_Object = MibTableColumn
cfprStorageFcIfRn = _CfprStorageFcIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 10, 1, 3),
    _CfprStorageFcIfRn_Type()
)
cfprStorageFcIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFcIfRn.setStatus("current")
_CfprStorageFcIfName_Type = SnmpAdminString
_CfprStorageFcIfName_Object = MibTableColumn
cfprStorageFcIfName = _CfprStorageFcIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 10, 1, 4),
    _CfprStorageFcIfName_Type()
)
cfprStorageFcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFcIfName.setStatus("current")
_CfprStorageFcTargetEpTable_Object = MibTable
cfprStorageFcTargetEpTable = _CfprStorageFcTargetEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 11)
)
if mibBuilder.loadTexts:
    cfprStorageFcTargetEpTable.setStatus("current")
_CfprStorageFcTargetEpEntry_Object = MibTableRow
cfprStorageFcTargetEpEntry = _CfprStorageFcTargetEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 11, 1)
)
cfprStorageFcTargetEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageFcTargetEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageFcTargetEpEntry.setStatus("current")
_CfprStorageFcTargetEpInstanceId_Type = CfprManagedObjectId
_CfprStorageFcTargetEpInstanceId_Object = MibTableColumn
cfprStorageFcTargetEpInstanceId = _CfprStorageFcTargetEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 11, 1, 1),
    _CfprStorageFcTargetEpInstanceId_Type()
)
cfprStorageFcTargetEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageFcTargetEpInstanceId.setStatus("current")
_CfprStorageFcTargetEpDn_Type = CfprManagedObjectDn
_CfprStorageFcTargetEpDn_Object = MibTableColumn
cfprStorageFcTargetEpDn = _CfprStorageFcTargetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 11, 1, 2),
    _CfprStorageFcTargetEpDn_Type()
)
cfprStorageFcTargetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFcTargetEpDn.setStatus("current")
_CfprStorageFcTargetEpRn_Type = SnmpAdminString
_CfprStorageFcTargetEpRn_Object = MibTableColumn
cfprStorageFcTargetEpRn = _CfprStorageFcTargetEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 11, 1, 3),
    _CfprStorageFcTargetEpRn_Type()
)
cfprStorageFcTargetEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFcTargetEpRn.setStatus("current")
_CfprStorageFcTargetEpDescr_Type = SnmpAdminString
_CfprStorageFcTargetEpDescr_Object = MibTableColumn
cfprStorageFcTargetEpDescr = _CfprStorageFcTargetEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 11, 1, 4),
    _CfprStorageFcTargetEpDescr_Type()
)
cfprStorageFcTargetEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFcTargetEpDescr.setStatus("current")
_CfprStorageFcTargetEpPath_Type = CfprStorageTargetPath
_CfprStorageFcTargetEpPath_Object = MibTableColumn
cfprStorageFcTargetEpPath = _CfprStorageFcTargetEpPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 11, 1, 5),
    _CfprStorageFcTargetEpPath_Type()
)
cfprStorageFcTargetEpPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFcTargetEpPath.setStatus("current")
_CfprStorageFcTargetEpTargetwwpn_Type = SnmpAdminString
_CfprStorageFcTargetEpTargetwwpn_Object = MibTableColumn
cfprStorageFcTargetEpTargetwwpn = _CfprStorageFcTargetEpTargetwwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 11, 1, 6),
    _CfprStorageFcTargetEpTargetwwpn_Type()
)
cfprStorageFcTargetEpTargetwwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFcTargetEpTargetwwpn.setStatus("current")
_CfprStorageFcTargetIfTable_Object = MibTable
cfprStorageFcTargetIfTable = _CfprStorageFcTargetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 12)
)
if mibBuilder.loadTexts:
    cfprStorageFcTargetIfTable.setStatus("current")
_CfprStorageFcTargetIfEntry_Object = MibTableRow
cfprStorageFcTargetIfEntry = _CfprStorageFcTargetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 12, 1)
)
cfprStorageFcTargetIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageFcTargetIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageFcTargetIfEntry.setStatus("current")
_CfprStorageFcTargetIfInstanceId_Type = CfprManagedObjectId
_CfprStorageFcTargetIfInstanceId_Object = MibTableColumn
cfprStorageFcTargetIfInstanceId = _CfprStorageFcTargetIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 12, 1, 1),
    _CfprStorageFcTargetIfInstanceId_Type()
)
cfprStorageFcTargetIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageFcTargetIfInstanceId.setStatus("current")
_CfprStorageFcTargetIfDn_Type = CfprManagedObjectDn
_CfprStorageFcTargetIfDn_Object = MibTableColumn
cfprStorageFcTargetIfDn = _CfprStorageFcTargetIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 12, 1, 2),
    _CfprStorageFcTargetIfDn_Type()
)
cfprStorageFcTargetIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFcTargetIfDn.setStatus("current")
_CfprStorageFcTargetIfRn_Type = SnmpAdminString
_CfprStorageFcTargetIfRn_Object = MibTableColumn
cfprStorageFcTargetIfRn = _CfprStorageFcTargetIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 12, 1, 3),
    _CfprStorageFcTargetIfRn_Type()
)
cfprStorageFcTargetIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFcTargetIfRn.setStatus("current")
_CfprStorageFcTargetIfId_Type = Unsigned64
_CfprStorageFcTargetIfId_Object = MibTableColumn
cfprStorageFcTargetIfId = _CfprStorageFcTargetIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 12, 1, 4),
    _CfprStorageFcTargetIfId_Type()
)
cfprStorageFcTargetIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFcTargetIfId.setStatus("current")
_CfprStorageFcTargetIfProt_Type = CfprStorageProtocol
_CfprStorageFcTargetIfProt_Object = MibTableColumn
cfprStorageFcTargetIfProt = _CfprStorageFcTargetIfProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 12, 1, 5),
    _CfprStorageFcTargetIfProt_Type()
)
cfprStorageFcTargetIfProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFcTargetIfProt.setStatus("current")
_CfprStorageFlexFlashCardTable_Object = MibTable
cfprStorageFlexFlashCardTable = _CfprStorageFlexFlashCardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13)
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardTable.setStatus("current")
_CfprStorageFlexFlashCardEntry_Object = MibTableRow
cfprStorageFlexFlashCardEntry = _CfprStorageFlexFlashCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1)
)
cfprStorageFlexFlashCardEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageFlexFlashCardInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardEntry.setStatus("current")
_CfprStorageFlexFlashCardInstanceId_Type = CfprManagedObjectId
_CfprStorageFlexFlashCardInstanceId_Object = MibTableColumn
cfprStorageFlexFlashCardInstanceId = _CfprStorageFlexFlashCardInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 1),
    _CfprStorageFlexFlashCardInstanceId_Type()
)
cfprStorageFlexFlashCardInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardInstanceId.setStatus("current")
_CfprStorageFlexFlashCardDn_Type = CfprManagedObjectDn
_CfprStorageFlexFlashCardDn_Object = MibTableColumn
cfprStorageFlexFlashCardDn = _CfprStorageFlexFlashCardDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 2),
    _CfprStorageFlexFlashCardDn_Type()
)
cfprStorageFlexFlashCardDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardDn.setStatus("current")
_CfprStorageFlexFlashCardRn_Type = SnmpAdminString
_CfprStorageFlexFlashCardRn_Object = MibTableColumn
cfprStorageFlexFlashCardRn = _CfprStorageFlexFlashCardRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 3),
    _CfprStorageFlexFlashCardRn_Type()
)
cfprStorageFlexFlashCardRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardRn.setStatus("current")
_CfprStorageFlexFlashCardBlockSize_Type = Gauge32
_CfprStorageFlexFlashCardBlockSize_Object = MibTableColumn
cfprStorageFlexFlashCardBlockSize = _CfprStorageFlexFlashCardBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 4),
    _CfprStorageFlexFlashCardBlockSize_Type()
)
cfprStorageFlexFlashCardBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardBlockSize.setStatus("current")
_CfprStorageFlexFlashCardCardHealth_Type = CfprStorageFFCardHealth
_CfprStorageFlexFlashCardCardHealth_Object = MibTableColumn
cfprStorageFlexFlashCardCardHealth = _CfprStorageFlexFlashCardCardHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 5),
    _CfprStorageFlexFlashCardCardHealth_Type()
)
cfprStorageFlexFlashCardCardHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardCardHealth.setStatus("current")
_CfprStorageFlexFlashCardCardMode_Type = CfprStorageFFCardMode
_CfprStorageFlexFlashCardCardMode_Object = MibTableColumn
cfprStorageFlexFlashCardCardMode = _CfprStorageFlexFlashCardCardMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 6),
    _CfprStorageFlexFlashCardCardMode_Type()
)
cfprStorageFlexFlashCardCardMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardCardMode.setStatus("current")
_CfprStorageFlexFlashCardCardState_Type = CfprStorageFFCardState
_CfprStorageFlexFlashCardCardState_Object = MibTableColumn
cfprStorageFlexFlashCardCardState = _CfprStorageFlexFlashCardCardState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 7),
    _CfprStorageFlexFlashCardCardState_Type()
)
cfprStorageFlexFlashCardCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardCardState.setStatus("current")
_CfprStorageFlexFlashCardCardSync_Type = CfprStorageFFCardSync
_CfprStorageFlexFlashCardCardSync_Object = MibTableColumn
cfprStorageFlexFlashCardCardSync = _CfprStorageFlexFlashCardCardSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 8),
    _CfprStorageFlexFlashCardCardSync_Type()
)
cfprStorageFlexFlashCardCardSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardCardSync.setStatus("current")
_CfprStorageFlexFlashCardCardType_Type = SnmpAdminString
_CfprStorageFlexFlashCardCardType_Object = MibTableColumn
cfprStorageFlexFlashCardCardType = _CfprStorageFlexFlashCardCardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 9),
    _CfprStorageFlexFlashCardCardType_Type()
)
cfprStorageFlexFlashCardCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardCardType.setStatus("current")
_CfprStorageFlexFlashCardConnectionProtocol_Type = CfprStorageConnectionProtocol
_CfprStorageFlexFlashCardConnectionProtocol_Object = MibTableColumn
cfprStorageFlexFlashCardConnectionProtocol = _CfprStorageFlexFlashCardConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 10),
    _CfprStorageFlexFlashCardConnectionProtocol_Type()
)
cfprStorageFlexFlashCardConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardConnectionProtocol.setStatus("current")
_CfprStorageFlexFlashCardControllerIndex_Type = Gauge32
_CfprStorageFlexFlashCardControllerIndex_Object = MibTableColumn
cfprStorageFlexFlashCardControllerIndex = _CfprStorageFlexFlashCardControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 11),
    _CfprStorageFlexFlashCardControllerIndex_Type()
)
cfprStorageFlexFlashCardControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardControllerIndex.setStatus("current")
_CfprStorageFlexFlashCardDrivesEnabled_Type = SnmpAdminString
_CfprStorageFlexFlashCardDrivesEnabled_Object = MibTableColumn
cfprStorageFlexFlashCardDrivesEnabled = _CfprStorageFlexFlashCardDrivesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 12),
    _CfprStorageFlexFlashCardDrivesEnabled_Type()
)
cfprStorageFlexFlashCardDrivesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardDrivesEnabled.setStatus("current")
_CfprStorageFlexFlashCardId_Type = Gauge32
_CfprStorageFlexFlashCardId_Object = MibTableColumn
cfprStorageFlexFlashCardId = _CfprStorageFlexFlashCardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 13),
    _CfprStorageFlexFlashCardId_Type()
)
cfprStorageFlexFlashCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardId.setStatus("current")
_CfprStorageFlexFlashCardMfgDate_Type = SnmpAdminString
_CfprStorageFlexFlashCardMfgDate_Object = MibTableColumn
cfprStorageFlexFlashCardMfgDate = _CfprStorageFlexFlashCardMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 14),
    _CfprStorageFlexFlashCardMfgDate_Type()
)
cfprStorageFlexFlashCardMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardMfgDate.setStatus("current")
_CfprStorageFlexFlashCardMfgId_Type = SnmpAdminString
_CfprStorageFlexFlashCardMfgId_Object = MibTableColumn
cfprStorageFlexFlashCardMfgId = _CfprStorageFlexFlashCardMfgId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 15),
    _CfprStorageFlexFlashCardMfgId_Type()
)
cfprStorageFlexFlashCardMfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardMfgId.setStatus("current")
_CfprStorageFlexFlashCardModel_Type = SnmpAdminString
_CfprStorageFlexFlashCardModel_Object = MibTableColumn
cfprStorageFlexFlashCardModel = _CfprStorageFlexFlashCardModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 16),
    _CfprStorageFlexFlashCardModel_Type()
)
cfprStorageFlexFlashCardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardModel.setStatus("current")
_CfprStorageFlexFlashCardNumberOfBlocks_Type = Unsigned64
_CfprStorageFlexFlashCardNumberOfBlocks_Object = MibTableColumn
cfprStorageFlexFlashCardNumberOfBlocks = _CfprStorageFlexFlashCardNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 17),
    _CfprStorageFlexFlashCardNumberOfBlocks_Type()
)
cfprStorageFlexFlashCardNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardNumberOfBlocks.setStatus("current")
_CfprStorageFlexFlashCardOemId_Type = SnmpAdminString
_CfprStorageFlexFlashCardOemId_Object = MibTableColumn
cfprStorageFlexFlashCardOemId = _CfprStorageFlexFlashCardOemId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 18),
    _CfprStorageFlexFlashCardOemId_Type()
)
cfprStorageFlexFlashCardOemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardOemId.setStatus("current")
_CfprStorageFlexFlashCardOperQualifierReason_Type = SnmpAdminString
_CfprStorageFlexFlashCardOperQualifierReason_Object = MibTableColumn
cfprStorageFlexFlashCardOperQualifierReason = _CfprStorageFlexFlashCardOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 19),
    _CfprStorageFlexFlashCardOperQualifierReason_Type()
)
cfprStorageFlexFlashCardOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardOperQualifierReason.setStatus("current")
_CfprStorageFlexFlashCardOperability_Type = CfprEquipmentOperability
_CfprStorageFlexFlashCardOperability_Object = MibTableColumn
cfprStorageFlexFlashCardOperability = _CfprStorageFlexFlashCardOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 20),
    _CfprStorageFlexFlashCardOperability_Type()
)
cfprStorageFlexFlashCardOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardOperability.setStatus("current")
_CfprStorageFlexFlashCardPartitionCount_Type = Gauge32
_CfprStorageFlexFlashCardPartitionCount_Object = MibTableColumn
cfprStorageFlexFlashCardPartitionCount = _CfprStorageFlexFlashCardPartitionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 21),
    _CfprStorageFlexFlashCardPartitionCount_Type()
)
cfprStorageFlexFlashCardPartitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardPartitionCount.setStatus("current")
_CfprStorageFlexFlashCardPresence_Type = CfprEquipmentPresence
_CfprStorageFlexFlashCardPresence_Object = MibTableColumn
cfprStorageFlexFlashCardPresence = _CfprStorageFlexFlashCardPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 22),
    _CfprStorageFlexFlashCardPresence_Type()
)
cfprStorageFlexFlashCardPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardPresence.setStatus("current")
_CfprStorageFlexFlashCardReadErrorThreshold_Type = Gauge32
_CfprStorageFlexFlashCardReadErrorThreshold_Object = MibTableColumn
cfprStorageFlexFlashCardReadErrorThreshold = _CfprStorageFlexFlashCardReadErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 23),
    _CfprStorageFlexFlashCardReadErrorThreshold_Type()
)
cfprStorageFlexFlashCardReadErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardReadErrorThreshold.setStatus("current")
_CfprStorageFlexFlashCardReadIOErrorCount_Type = Gauge32
_CfprStorageFlexFlashCardReadIOErrorCount_Object = MibTableColumn
cfprStorageFlexFlashCardReadIOErrorCount = _CfprStorageFlexFlashCardReadIOErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 24),
    _CfprStorageFlexFlashCardReadIOErrorCount_Type()
)
cfprStorageFlexFlashCardReadIOErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardReadIOErrorCount.setStatus("current")
_CfprStorageFlexFlashCardRevision_Type = SnmpAdminString
_CfprStorageFlexFlashCardRevision_Object = MibTableColumn
cfprStorageFlexFlashCardRevision = _CfprStorageFlexFlashCardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 25),
    _CfprStorageFlexFlashCardRevision_Type()
)
cfprStorageFlexFlashCardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardRevision.setStatus("current")
_CfprStorageFlexFlashCardSerial_Type = SnmpAdminString
_CfprStorageFlexFlashCardSerial_Object = MibTableColumn
cfprStorageFlexFlashCardSerial = _CfprStorageFlexFlashCardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 26),
    _CfprStorageFlexFlashCardSerial_Type()
)
cfprStorageFlexFlashCardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardSerial.setStatus("current")
_CfprStorageFlexFlashCardSignature_Type = SnmpAdminString
_CfprStorageFlexFlashCardSignature_Object = MibTableColumn
cfprStorageFlexFlashCardSignature = _CfprStorageFlexFlashCardSignature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 27),
    _CfprStorageFlexFlashCardSignature_Type()
)
cfprStorageFlexFlashCardSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardSignature.setStatus("current")
_CfprStorageFlexFlashCardSize_Type = Unsigned64
_CfprStorageFlexFlashCardSize_Object = MibTableColumn
cfprStorageFlexFlashCardSize = _CfprStorageFlexFlashCardSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 28),
    _CfprStorageFlexFlashCardSize_Type()
)
cfprStorageFlexFlashCardSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardSize.setStatus("current")
_CfprStorageFlexFlashCardSlotNumber_Type = Gauge32
_CfprStorageFlexFlashCardSlotNumber_Object = MibTableColumn
cfprStorageFlexFlashCardSlotNumber = _CfprStorageFlexFlashCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 29),
    _CfprStorageFlexFlashCardSlotNumber_Type()
)
cfprStorageFlexFlashCardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardSlotNumber.setStatus("current")
_CfprStorageFlexFlashCardVendor_Type = SnmpAdminString
_CfprStorageFlexFlashCardVendor_Object = MibTableColumn
cfprStorageFlexFlashCardVendor = _CfprStorageFlexFlashCardVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 30),
    _CfprStorageFlexFlashCardVendor_Type()
)
cfprStorageFlexFlashCardVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardVendor.setStatus("current")
_CfprStorageFlexFlashCardWriteEnable_Type = CfprStorageFFCardWriteEnable
_CfprStorageFlexFlashCardWriteEnable_Object = MibTableColumn
cfprStorageFlexFlashCardWriteEnable = _CfprStorageFlexFlashCardWriteEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 31),
    _CfprStorageFlexFlashCardWriteEnable_Type()
)
cfprStorageFlexFlashCardWriteEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardWriteEnable.setStatus("current")
_CfprStorageFlexFlashCardWriteErrorThreshold_Type = Gauge32
_CfprStorageFlexFlashCardWriteErrorThreshold_Object = MibTableColumn
cfprStorageFlexFlashCardWriteErrorThreshold = _CfprStorageFlexFlashCardWriteErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 32),
    _CfprStorageFlexFlashCardWriteErrorThreshold_Type()
)
cfprStorageFlexFlashCardWriteErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardWriteErrorThreshold.setStatus("current")
_CfprStorageFlexFlashCardWriteIOErrorCount_Type = Gauge32
_CfprStorageFlexFlashCardWriteIOErrorCount_Object = MibTableColumn
cfprStorageFlexFlashCardWriteIOErrorCount = _CfprStorageFlexFlashCardWriteIOErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 13, 1, 33),
    _CfprStorageFlexFlashCardWriteIOErrorCount_Type()
)
cfprStorageFlexFlashCardWriteIOErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashCardWriteIOErrorCount.setStatus("current")
_CfprStorageFlexFlashControllerTable_Object = MibTable
cfprStorageFlexFlashControllerTable = _CfprStorageFlexFlashControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14)
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerTable.setStatus("current")
_CfprStorageFlexFlashControllerEntry_Object = MibTableRow
cfprStorageFlexFlashControllerEntry = _CfprStorageFlexFlashControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1)
)
cfprStorageFlexFlashControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageFlexFlashControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerEntry.setStatus("current")
_CfprStorageFlexFlashControllerInstanceId_Type = CfprManagedObjectId
_CfprStorageFlexFlashControllerInstanceId_Object = MibTableColumn
cfprStorageFlexFlashControllerInstanceId = _CfprStorageFlexFlashControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 1),
    _CfprStorageFlexFlashControllerInstanceId_Type()
)
cfprStorageFlexFlashControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerInstanceId.setStatus("current")
_CfprStorageFlexFlashControllerDn_Type = CfprManagedObjectDn
_CfprStorageFlexFlashControllerDn_Object = MibTableColumn
cfprStorageFlexFlashControllerDn = _CfprStorageFlexFlashControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 2),
    _CfprStorageFlexFlashControllerDn_Type()
)
cfprStorageFlexFlashControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerDn.setStatus("current")
_CfprStorageFlexFlashControllerRn_Type = SnmpAdminString
_CfprStorageFlexFlashControllerRn_Object = MibTableColumn
cfprStorageFlexFlashControllerRn = _CfprStorageFlexFlashControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 3),
    _CfprStorageFlexFlashControllerRn_Type()
)
cfprStorageFlexFlashControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerRn.setStatus("current")
_CfprStorageFlexFlashControllerAdminSlotNumber_Type = CfprStorageFFSlotENUM
_CfprStorageFlexFlashControllerAdminSlotNumber_Object = MibTableColumn
cfprStorageFlexFlashControllerAdminSlotNumber = _CfprStorageFlexFlashControllerAdminSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 4),
    _CfprStorageFlexFlashControllerAdminSlotNumber_Type()
)
cfprStorageFlexFlashControllerAdminSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerAdminSlotNumber.setStatus("current")
_CfprStorageFlexFlashControllerConfiguredMode_Type = CfprStorageOperatingModeType
_CfprStorageFlexFlashControllerConfiguredMode_Object = MibTableColumn
cfprStorageFlexFlashControllerConfiguredMode = _CfprStorageFlexFlashControllerConfiguredMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 5),
    _CfprStorageFlexFlashControllerConfiguredMode_Type()
)
cfprStorageFlexFlashControllerConfiguredMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerConfiguredMode.setStatus("current")
_CfprStorageFlexFlashControllerControllerHealth_Type = CfprStorageFFControllerHealth
_CfprStorageFlexFlashControllerControllerHealth_Object = MibTableColumn
cfprStorageFlexFlashControllerControllerHealth = _CfprStorageFlexFlashControllerControllerHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 6),
    _CfprStorageFlexFlashControllerControllerHealth_Type()
)
cfprStorageFlexFlashControllerControllerHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerControllerHealth.setStatus("current")
_CfprStorageFlexFlashControllerControllerState_Type = CfprStorageFFControllerState
_CfprStorageFlexFlashControllerControllerState_Object = MibTableColumn
cfprStorageFlexFlashControllerControllerState = _CfprStorageFlexFlashControllerControllerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 7),
    _CfprStorageFlexFlashControllerControllerState_Type()
)
cfprStorageFlexFlashControllerControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerControllerState.setStatus("current")
_CfprStorageFlexFlashControllerFirmwareVersion_Type = SnmpAdminString
_CfprStorageFlexFlashControllerFirmwareVersion_Object = MibTableColumn
cfprStorageFlexFlashControllerFirmwareVersion = _CfprStorageFlexFlashControllerFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 8),
    _CfprStorageFlexFlashControllerFirmwareVersion_Type()
)
cfprStorageFlexFlashControllerFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFirmwareVersion.setStatus("current")
_CfprStorageFlexFlashControllerFlexFlashType_Type = CfprStorageFFType
_CfprStorageFlexFlashControllerFlexFlashType_Object = MibTableColumn
cfprStorageFlexFlashControllerFlexFlashType = _CfprStorageFlexFlashControllerFlexFlashType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 9),
    _CfprStorageFlexFlashControllerFlexFlashType_Type()
)
cfprStorageFlexFlashControllerFlexFlashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFlexFlashType.setStatus("current")
_CfprStorageFlexFlashControllerFsmDescr_Type = SnmpAdminString
_CfprStorageFlexFlashControllerFsmDescr_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmDescr = _CfprStorageFlexFlashControllerFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 10),
    _CfprStorageFlexFlashControllerFsmDescr_Type()
)
cfprStorageFlexFlashControllerFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmDescr.setStatus("current")
_CfprStorageFlexFlashControllerFsmPrev_Type = SnmpAdminString
_CfprStorageFlexFlashControllerFsmPrev_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmPrev = _CfprStorageFlexFlashControllerFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 11),
    _CfprStorageFlexFlashControllerFsmPrev_Type()
)
cfprStorageFlexFlashControllerFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmPrev.setStatus("current")
_CfprStorageFlexFlashControllerFsmProgr_Type = Gauge32
_CfprStorageFlexFlashControllerFsmProgr_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmProgr = _CfprStorageFlexFlashControllerFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 12),
    _CfprStorageFlexFlashControllerFsmProgr_Type()
)
cfprStorageFlexFlashControllerFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmProgr.setStatus("current")
_CfprStorageFlexFlashControllerFsmRmtInvErrCode_Type = Gauge32
_CfprStorageFlexFlashControllerFsmRmtInvErrCode_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmRmtInvErrCode = _CfprStorageFlexFlashControllerFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 13),
    _CfprStorageFlexFlashControllerFsmRmtInvErrCode_Type()
)
cfprStorageFlexFlashControllerFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmRmtInvErrCode.setStatus("current")
_CfprStorageFlexFlashControllerFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprStorageFlexFlashControllerFsmRmtInvErrDescr_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmRmtInvErrDescr = _CfprStorageFlexFlashControllerFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 14),
    _CfprStorageFlexFlashControllerFsmRmtInvErrDescr_Type()
)
cfprStorageFlexFlashControllerFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmRmtInvErrDescr.setStatus("current")
_CfprStorageFlexFlashControllerFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprStorageFlexFlashControllerFsmRmtInvRslt_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmRmtInvRslt = _CfprStorageFlexFlashControllerFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 15),
    _CfprStorageFlexFlashControllerFsmRmtInvRslt_Type()
)
cfprStorageFlexFlashControllerFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmRmtInvRslt.setStatus("current")
_CfprStorageFlexFlashControllerFsmStageDescr_Type = SnmpAdminString
_CfprStorageFlexFlashControllerFsmStageDescr_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmStageDescr = _CfprStorageFlexFlashControllerFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 16),
    _CfprStorageFlexFlashControllerFsmStageDescr_Type()
)
cfprStorageFlexFlashControllerFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStageDescr.setStatus("current")
_CfprStorageFlexFlashControllerFsmStamp_Type = DateAndTime
_CfprStorageFlexFlashControllerFsmStamp_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmStamp = _CfprStorageFlexFlashControllerFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 17),
    _CfprStorageFlexFlashControllerFsmStamp_Type()
)
cfprStorageFlexFlashControllerFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStamp.setStatus("current")
_CfprStorageFlexFlashControllerFsmStatus_Type = SnmpAdminString
_CfprStorageFlexFlashControllerFsmStatus_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmStatus = _CfprStorageFlexFlashControllerFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 18),
    _CfprStorageFlexFlashControllerFsmStatus_Type()
)
cfprStorageFlexFlashControllerFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStatus.setStatus("current")
_CfprStorageFlexFlashControllerFsmTry_Type = Gauge32
_CfprStorageFlexFlashControllerFsmTry_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmTry = _CfprStorageFlexFlashControllerFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 19),
    _CfprStorageFlexFlashControllerFsmTry_Type()
)
cfprStorageFlexFlashControllerFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmTry.setStatus("current")
_CfprStorageFlexFlashControllerHasError_Type = CfprStorageFFHasError
_CfprStorageFlexFlashControllerHasError_Object = MibTableColumn
cfprStorageFlexFlashControllerHasError = _CfprStorageFlexFlashControllerHasError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 20),
    _CfprStorageFlexFlashControllerHasError_Type()
)
cfprStorageFlexFlashControllerHasError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerHasError.setStatus("current")
_CfprStorageFlexFlashControllerId_Type = CfprStorageFlexFlashControllerId
_CfprStorageFlexFlashControllerId_Object = MibTableColumn
cfprStorageFlexFlashControllerId = _CfprStorageFlexFlashControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 21),
    _CfprStorageFlexFlashControllerId_Type()
)
cfprStorageFlexFlashControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerId.setStatus("current")
_CfprStorageFlexFlashControllerIsCardMismatch_Type = CfprStorageFFCardSizeMismatch
_CfprStorageFlexFlashControllerIsCardMismatch_Object = MibTableColumn
cfprStorageFlexFlashControllerIsCardMismatch = _CfprStorageFlexFlashControllerIsCardMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 22),
    _CfprStorageFlexFlashControllerIsCardMismatch_Type()
)
cfprStorageFlexFlashControllerIsCardMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerIsCardMismatch.setStatus("current")
_CfprStorageFlexFlashControllerIsFormatFSMRunning_Type = CfprStorageFFFormatRunning
_CfprStorageFlexFlashControllerIsFormatFSMRunning_Object = MibTableColumn
cfprStorageFlexFlashControllerIsFormatFSMRunning = _CfprStorageFlexFlashControllerIsFormatFSMRunning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 23),
    _CfprStorageFlexFlashControllerIsFormatFSMRunning_Type()
)
cfprStorageFlexFlashControllerIsFormatFSMRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerIsFormatFSMRunning.setStatus("current")
_CfprStorageFlexFlashControllerLocationDn_Type = SnmpAdminString
_CfprStorageFlexFlashControllerLocationDn_Object = MibTableColumn
cfprStorageFlexFlashControllerLocationDn = _CfprStorageFlexFlashControllerLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 24),
    _CfprStorageFlexFlashControllerLocationDn_Type()
)
cfprStorageFlexFlashControllerLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerLocationDn.setStatus("current")
_CfprStorageFlexFlashControllerModel_Type = SnmpAdminString
_CfprStorageFlexFlashControllerModel_Object = MibTableColumn
cfprStorageFlexFlashControllerModel = _CfprStorageFlexFlashControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 25),
    _CfprStorageFlexFlashControllerModel_Type()
)
cfprStorageFlexFlashControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerModel.setStatus("current")
_CfprStorageFlexFlashControllerOperQualifierReason_Type = SnmpAdminString
_CfprStorageFlexFlashControllerOperQualifierReason_Object = MibTableColumn
cfprStorageFlexFlashControllerOperQualifierReason = _CfprStorageFlexFlashControllerOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 26),
    _CfprStorageFlexFlashControllerOperQualifierReason_Type()
)
cfprStorageFlexFlashControllerOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerOperQualifierReason.setStatus("current")
_CfprStorageFlexFlashControllerOperState_Type = CfprEquipmentOperability
_CfprStorageFlexFlashControllerOperState_Object = MibTableColumn
cfprStorageFlexFlashControllerOperState = _CfprStorageFlexFlashControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 27),
    _CfprStorageFlexFlashControllerOperState_Type()
)
cfprStorageFlexFlashControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerOperState.setStatus("current")
_CfprStorageFlexFlashControllerOperability_Type = CfprEquipmentOperability
_CfprStorageFlexFlashControllerOperability_Object = MibTableColumn
cfprStorageFlexFlashControllerOperability = _CfprStorageFlexFlashControllerOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 28),
    _CfprStorageFlexFlashControllerOperability_Type()
)
cfprStorageFlexFlashControllerOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerOperability.setStatus("current")
_CfprStorageFlexFlashControllerOperatingMode_Type = CfprStorageOperatingModeType
_CfprStorageFlexFlashControllerOperatingMode_Object = MibTableColumn
cfprStorageFlexFlashControllerOperatingMode = _CfprStorageFlexFlashControllerOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 29),
    _CfprStorageFlexFlashControllerOperatingMode_Type()
)
cfprStorageFlexFlashControllerOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerOperatingMode.setStatus("current")
_CfprStorageFlexFlashControllerOperationRequest_Type = CfprStorageOperationRequestType
_CfprStorageFlexFlashControllerOperationRequest_Object = MibTableColumn
cfprStorageFlexFlashControllerOperationRequest = _CfprStorageFlexFlashControllerOperationRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 30),
    _CfprStorageFlexFlashControllerOperationRequest_Type()
)
cfprStorageFlexFlashControllerOperationRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerOperationRequest.setStatus("current")
_CfprStorageFlexFlashControllerPciAddr_Type = SnmpAdminString
_CfprStorageFlexFlashControllerPciAddr_Object = MibTableColumn
cfprStorageFlexFlashControllerPciAddr = _CfprStorageFlexFlashControllerPciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 31),
    _CfprStorageFlexFlashControllerPciAddr_Type()
)
cfprStorageFlexFlashControllerPciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerPciAddr.setStatus("current")
_CfprStorageFlexFlashControllerPciSlot_Type = SnmpAdminString
_CfprStorageFlexFlashControllerPciSlot_Object = MibTableColumn
cfprStorageFlexFlashControllerPciSlot = _CfprStorageFlexFlashControllerPciSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 32),
    _CfprStorageFlexFlashControllerPciSlot_Type()
)
cfprStorageFlexFlashControllerPciSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerPciSlot.setStatus("current")
_CfprStorageFlexFlashControllerPerf_Type = CfprEquipmentSensorThresholdStatus
_CfprStorageFlexFlashControllerPerf_Object = MibTableColumn
cfprStorageFlexFlashControllerPerf = _CfprStorageFlexFlashControllerPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 33),
    _CfprStorageFlexFlashControllerPerf_Type()
)
cfprStorageFlexFlashControllerPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerPerf.setStatus("current")
_CfprStorageFlexFlashControllerPhysicalDriveCount_Type = Gauge32
_CfprStorageFlexFlashControllerPhysicalDriveCount_Object = MibTableColumn
cfprStorageFlexFlashControllerPhysicalDriveCount = _CfprStorageFlexFlashControllerPhysicalDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 34),
    _CfprStorageFlexFlashControllerPhysicalDriveCount_Type()
)
cfprStorageFlexFlashControllerPhysicalDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerPhysicalDriveCount.setStatus("current")
_CfprStorageFlexFlashControllerPower_Type = CfprEquipmentPowerState
_CfprStorageFlexFlashControllerPower_Object = MibTableColumn
cfprStorageFlexFlashControllerPower = _CfprStorageFlexFlashControllerPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 35),
    _CfprStorageFlexFlashControllerPower_Type()
)
cfprStorageFlexFlashControllerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerPower.setStatus("current")
_CfprStorageFlexFlashControllerPresence_Type = CfprEquipmentPresence
_CfprStorageFlexFlashControllerPresence_Object = MibTableColumn
cfprStorageFlexFlashControllerPresence = _CfprStorageFlexFlashControllerPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 36),
    _CfprStorageFlexFlashControllerPresence_Type()
)
cfprStorageFlexFlashControllerPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerPresence.setStatus("current")
_CfprStorageFlexFlashControllerPrimarySlotNumber_Type = Gauge32
_CfprStorageFlexFlashControllerPrimarySlotNumber_Object = MibTableColumn
cfprStorageFlexFlashControllerPrimarySlotNumber = _CfprStorageFlexFlashControllerPrimarySlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 37),
    _CfprStorageFlexFlashControllerPrimarySlotNumber_Type()
)
cfprStorageFlexFlashControllerPrimarySlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerPrimarySlotNumber.setStatus("current")
_CfprStorageFlexFlashControllerRaidSyncSupport_Type = CfprStorageFFRaidSyncSupport
_CfprStorageFlexFlashControllerRaidSyncSupport_Object = MibTableColumn
cfprStorageFlexFlashControllerRaidSyncSupport = _CfprStorageFlexFlashControllerRaidSyncSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 38),
    _CfprStorageFlexFlashControllerRaidSyncSupport_Type()
)
cfprStorageFlexFlashControllerRaidSyncSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerRaidSyncSupport.setStatus("current")
_CfprStorageFlexFlashControllerReadErrorThreshold_Type = Gauge32
_CfprStorageFlexFlashControllerReadErrorThreshold_Object = MibTableColumn
cfprStorageFlexFlashControllerReadErrorThreshold = _CfprStorageFlexFlashControllerReadErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 39),
    _CfprStorageFlexFlashControllerReadErrorThreshold_Type()
)
cfprStorageFlexFlashControllerReadErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerReadErrorThreshold.setStatus("current")
_CfprStorageFlexFlashControllerRevision_Type = SnmpAdminString
_CfprStorageFlexFlashControllerRevision_Object = MibTableColumn
cfprStorageFlexFlashControllerRevision = _CfprStorageFlexFlashControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 40),
    _CfprStorageFlexFlashControllerRevision_Type()
)
cfprStorageFlexFlashControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerRevision.setStatus("current")
_CfprStorageFlexFlashControllerSerial_Type = SnmpAdminString
_CfprStorageFlexFlashControllerSerial_Object = MibTableColumn
cfprStorageFlexFlashControllerSerial = _CfprStorageFlexFlashControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 41),
    _CfprStorageFlexFlashControllerSerial_Type()
)
cfprStorageFlexFlashControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerSerial.setStatus("current")
_CfprStorageFlexFlashControllerThermal_Type = CfprEquipmentSensorThresholdStatus
_CfprStorageFlexFlashControllerThermal_Object = MibTableColumn
cfprStorageFlexFlashControllerThermal = _CfprStorageFlexFlashControllerThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 42),
    _CfprStorageFlexFlashControllerThermal_Type()
)
cfprStorageFlexFlashControllerThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerThermal.setStatus("current")
_CfprStorageFlexFlashControllerType_Type = CfprStorageControllerType
_CfprStorageFlexFlashControllerType_Object = MibTableColumn
cfprStorageFlexFlashControllerType = _CfprStorageFlexFlashControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 43),
    _CfprStorageFlexFlashControllerType_Type()
)
cfprStorageFlexFlashControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerType.setStatus("current")
_CfprStorageFlexFlashControllerVendor_Type = SnmpAdminString
_CfprStorageFlexFlashControllerVendor_Object = MibTableColumn
cfprStorageFlexFlashControllerVendor = _CfprStorageFlexFlashControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 44),
    _CfprStorageFlexFlashControllerVendor_Type()
)
cfprStorageFlexFlashControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerVendor.setStatus("current")
_CfprStorageFlexFlashControllerVirtualDriveCount_Type = Gauge32
_CfprStorageFlexFlashControllerVirtualDriveCount_Object = MibTableColumn
cfprStorageFlexFlashControllerVirtualDriveCount = _CfprStorageFlexFlashControllerVirtualDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 45),
    _CfprStorageFlexFlashControllerVirtualDriveCount_Type()
)
cfprStorageFlexFlashControllerVirtualDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerVirtualDriveCount.setStatus("current")
_CfprStorageFlexFlashControllerVoltage_Type = CfprEquipmentSensorThresholdStatus
_CfprStorageFlexFlashControllerVoltage_Object = MibTableColumn
cfprStorageFlexFlashControllerVoltage = _CfprStorageFlexFlashControllerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 46),
    _CfprStorageFlexFlashControllerVoltage_Type()
)
cfprStorageFlexFlashControllerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerVoltage.setStatus("current")
_CfprStorageFlexFlashControllerWriteErrorThreshold_Type = Gauge32
_CfprStorageFlexFlashControllerWriteErrorThreshold_Object = MibTableColumn
cfprStorageFlexFlashControllerWriteErrorThreshold = _CfprStorageFlexFlashControllerWriteErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 14, 1, 47),
    _CfprStorageFlexFlashControllerWriteErrorThreshold_Type()
)
cfprStorageFlexFlashControllerWriteErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerWriteErrorThreshold.setStatus("current")
_CfprStorageFlexFlashControllerFsmTable_Object = MibTable
cfprStorageFlexFlashControllerFsmTable = _CfprStorageFlexFlashControllerFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15)
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmTable.setStatus("current")
_CfprStorageFlexFlashControllerFsmEntry_Object = MibTableRow
cfprStorageFlexFlashControllerFsmEntry = _CfprStorageFlexFlashControllerFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15, 1)
)
cfprStorageFlexFlashControllerFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageFlexFlashControllerFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmEntry.setStatus("current")
_CfprStorageFlexFlashControllerFsmInstanceId_Type = CfprManagedObjectId
_CfprStorageFlexFlashControllerFsmInstanceId_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmInstanceId = _CfprStorageFlexFlashControllerFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15, 1, 1),
    _CfprStorageFlexFlashControllerFsmInstanceId_Type()
)
cfprStorageFlexFlashControllerFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmInstanceId.setStatus("current")
_CfprStorageFlexFlashControllerFsmDn_Type = CfprManagedObjectDn
_CfprStorageFlexFlashControllerFsmDn_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmDn = _CfprStorageFlexFlashControllerFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15, 1, 2),
    _CfprStorageFlexFlashControllerFsmDn_Type()
)
cfprStorageFlexFlashControllerFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmDn.setStatus("current")
_CfprStorageFlexFlashControllerFsmRn_Type = SnmpAdminString
_CfprStorageFlexFlashControllerFsmRn_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmRn = _CfprStorageFlexFlashControllerFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15, 1, 3),
    _CfprStorageFlexFlashControllerFsmRn_Type()
)
cfprStorageFlexFlashControllerFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmRn.setStatus("current")
_CfprStorageFlexFlashControllerFsmCompletionTime_Type = DateAndTime
_CfprStorageFlexFlashControllerFsmCompletionTime_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmCompletionTime = _CfprStorageFlexFlashControllerFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15, 1, 4),
    _CfprStorageFlexFlashControllerFsmCompletionTime_Type()
)
cfprStorageFlexFlashControllerFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmCompletionTime.setStatus("current")
_CfprStorageFlexFlashControllerFsmCurrentFsm_Type = CfprStorageFlexFlashControllerFsmCurrentFsm
_CfprStorageFlexFlashControllerFsmCurrentFsm_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmCurrentFsm = _CfprStorageFlexFlashControllerFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15, 1, 5),
    _CfprStorageFlexFlashControllerFsmCurrentFsm_Type()
)
cfprStorageFlexFlashControllerFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmCurrentFsm.setStatus("current")
_CfprStorageFlexFlashControllerFsmDescrData_Type = SnmpAdminString
_CfprStorageFlexFlashControllerFsmDescrData_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmDescrData = _CfprStorageFlexFlashControllerFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15, 1, 6),
    _CfprStorageFlexFlashControllerFsmDescrData_Type()
)
cfprStorageFlexFlashControllerFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmDescrData.setStatus("current")
_CfprStorageFlexFlashControllerFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprStorageFlexFlashControllerFsmFsmStatus_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmFsmStatus = _CfprStorageFlexFlashControllerFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15, 1, 7),
    _CfprStorageFlexFlashControllerFsmFsmStatus_Type()
)
cfprStorageFlexFlashControllerFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmFsmStatus.setStatus("current")
_CfprStorageFlexFlashControllerFsmProgress_Type = Gauge32
_CfprStorageFlexFlashControllerFsmProgress_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmProgress = _CfprStorageFlexFlashControllerFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15, 1, 8),
    _CfprStorageFlexFlashControllerFsmProgress_Type()
)
cfprStorageFlexFlashControllerFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmProgress.setStatus("current")
_CfprStorageFlexFlashControllerFsmRmtErrCode_Type = Gauge32
_CfprStorageFlexFlashControllerFsmRmtErrCode_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmRmtErrCode = _CfprStorageFlexFlashControllerFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15, 1, 9),
    _CfprStorageFlexFlashControllerFsmRmtErrCode_Type()
)
cfprStorageFlexFlashControllerFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmRmtErrCode.setStatus("current")
_CfprStorageFlexFlashControllerFsmRmtErrDescr_Type = SnmpAdminString
_CfprStorageFlexFlashControllerFsmRmtErrDescr_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmRmtErrDescr = _CfprStorageFlexFlashControllerFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15, 1, 10),
    _CfprStorageFlexFlashControllerFsmRmtErrDescr_Type()
)
cfprStorageFlexFlashControllerFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmRmtErrDescr.setStatus("current")
_CfprStorageFlexFlashControllerFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprStorageFlexFlashControllerFsmRmtRslt_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmRmtRslt = _CfprStorageFlexFlashControllerFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 15, 1, 11),
    _CfprStorageFlexFlashControllerFsmRmtRslt_Type()
)
cfprStorageFlexFlashControllerFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmRmtRslt.setStatus("current")
_CfprStorageFlexFlashControllerFsmStageTable_Object = MibTable
cfprStorageFlexFlashControllerFsmStageTable = _CfprStorageFlexFlashControllerFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 16)
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStageTable.setStatus("current")
_CfprStorageFlexFlashControllerFsmStageEntry_Object = MibTableRow
cfprStorageFlexFlashControllerFsmStageEntry = _CfprStorageFlexFlashControllerFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 16, 1)
)
cfprStorageFlexFlashControllerFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageFlexFlashControllerFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStageEntry.setStatus("current")
_CfprStorageFlexFlashControllerFsmStageInstanceId_Type = CfprManagedObjectId
_CfprStorageFlexFlashControllerFsmStageInstanceId_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmStageInstanceId = _CfprStorageFlexFlashControllerFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 16, 1, 1),
    _CfprStorageFlexFlashControllerFsmStageInstanceId_Type()
)
cfprStorageFlexFlashControllerFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStageInstanceId.setStatus("current")
_CfprStorageFlexFlashControllerFsmStageDn_Type = CfprManagedObjectDn
_CfprStorageFlexFlashControllerFsmStageDn_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmStageDn = _CfprStorageFlexFlashControllerFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 16, 1, 2),
    _CfprStorageFlexFlashControllerFsmStageDn_Type()
)
cfprStorageFlexFlashControllerFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStageDn.setStatus("current")
_CfprStorageFlexFlashControllerFsmStageRn_Type = SnmpAdminString
_CfprStorageFlexFlashControllerFsmStageRn_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmStageRn = _CfprStorageFlexFlashControllerFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 16, 1, 3),
    _CfprStorageFlexFlashControllerFsmStageRn_Type()
)
cfprStorageFlexFlashControllerFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStageRn.setStatus("current")
_CfprStorageFlexFlashControllerFsmStageDescrData_Type = SnmpAdminString
_CfprStorageFlexFlashControllerFsmStageDescrData_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmStageDescrData = _CfprStorageFlexFlashControllerFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 16, 1, 4),
    _CfprStorageFlexFlashControllerFsmStageDescrData_Type()
)
cfprStorageFlexFlashControllerFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStageDescrData.setStatus("current")
_CfprStorageFlexFlashControllerFsmStageLastUpdateTime_Type = DateAndTime
_CfprStorageFlexFlashControllerFsmStageLastUpdateTime_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmStageLastUpdateTime = _CfprStorageFlexFlashControllerFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 16, 1, 5),
    _CfprStorageFlexFlashControllerFsmStageLastUpdateTime_Type()
)
cfprStorageFlexFlashControllerFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStageLastUpdateTime.setStatus("current")
_CfprStorageFlexFlashControllerFsmStageName_Type = CfprStorageFlexFlashControllerFsmStageName
_CfprStorageFlexFlashControllerFsmStageName_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmStageName = _CfprStorageFlexFlashControllerFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 16, 1, 6),
    _CfprStorageFlexFlashControllerFsmStageName_Type()
)
cfprStorageFlexFlashControllerFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStageName.setStatus("current")
_CfprStorageFlexFlashControllerFsmStageOrder_Type = Gauge32
_CfprStorageFlexFlashControllerFsmStageOrder_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmStageOrder = _CfprStorageFlexFlashControllerFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 16, 1, 7),
    _CfprStorageFlexFlashControllerFsmStageOrder_Type()
)
cfprStorageFlexFlashControllerFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStageOrder.setStatus("current")
_CfprStorageFlexFlashControllerFsmStageRetry_Type = Gauge32
_CfprStorageFlexFlashControllerFsmStageRetry_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmStageRetry = _CfprStorageFlexFlashControllerFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 16, 1, 8),
    _CfprStorageFlexFlashControllerFsmStageRetry_Type()
)
cfprStorageFlexFlashControllerFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStageRetry.setStatus("current")
_CfprStorageFlexFlashControllerFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprStorageFlexFlashControllerFsmStageStageStatus_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmStageStageStatus = _CfprStorageFlexFlashControllerFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 16, 1, 9),
    _CfprStorageFlexFlashControllerFsmStageStageStatus_Type()
)
cfprStorageFlexFlashControllerFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmStageStageStatus.setStatus("current")
_CfprStorageFlexFlashControllerFsmTaskTable_Object = MibTable
cfprStorageFlexFlashControllerFsmTaskTable = _CfprStorageFlexFlashControllerFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 17)
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmTaskTable.setStatus("current")
_CfprStorageFlexFlashControllerFsmTaskEntry_Object = MibTableRow
cfprStorageFlexFlashControllerFsmTaskEntry = _CfprStorageFlexFlashControllerFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 17, 1)
)
cfprStorageFlexFlashControllerFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageFlexFlashControllerFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmTaskEntry.setStatus("current")
_CfprStorageFlexFlashControllerFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprStorageFlexFlashControllerFsmTaskInstanceId_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmTaskInstanceId = _CfprStorageFlexFlashControllerFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 17, 1, 1),
    _CfprStorageFlexFlashControllerFsmTaskInstanceId_Type()
)
cfprStorageFlexFlashControllerFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmTaskInstanceId.setStatus("current")
_CfprStorageFlexFlashControllerFsmTaskDn_Type = CfprManagedObjectDn
_CfprStorageFlexFlashControllerFsmTaskDn_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmTaskDn = _CfprStorageFlexFlashControllerFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 17, 1, 2),
    _CfprStorageFlexFlashControllerFsmTaskDn_Type()
)
cfprStorageFlexFlashControllerFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmTaskDn.setStatus("current")
_CfprStorageFlexFlashControllerFsmTaskRn_Type = SnmpAdminString
_CfprStorageFlexFlashControllerFsmTaskRn_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmTaskRn = _CfprStorageFlexFlashControllerFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 17, 1, 3),
    _CfprStorageFlexFlashControllerFsmTaskRn_Type()
)
cfprStorageFlexFlashControllerFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmTaskRn.setStatus("current")
_CfprStorageFlexFlashControllerFsmTaskCompletion_Type = CfprFsmCompletion
_CfprStorageFlexFlashControllerFsmTaskCompletion_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmTaskCompletion = _CfprStorageFlexFlashControllerFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 17, 1, 4),
    _CfprStorageFlexFlashControllerFsmTaskCompletion_Type()
)
cfprStorageFlexFlashControllerFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmTaskCompletion.setStatus("current")
_CfprStorageFlexFlashControllerFsmTaskFlags_Type = CfprFsmFlags
_CfprStorageFlexFlashControllerFsmTaskFlags_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmTaskFlags = _CfprStorageFlexFlashControllerFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 17, 1, 5),
    _CfprStorageFlexFlashControllerFsmTaskFlags_Type()
)
cfprStorageFlexFlashControllerFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmTaskFlags.setStatus("current")
_CfprStorageFlexFlashControllerFsmTaskItem_Type = CfprStorageFlexFlashControllerFsmTaskItem
_CfprStorageFlexFlashControllerFsmTaskItem_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmTaskItem = _CfprStorageFlexFlashControllerFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 17, 1, 6),
    _CfprStorageFlexFlashControllerFsmTaskItem_Type()
)
cfprStorageFlexFlashControllerFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmTaskItem.setStatus("current")
_CfprStorageFlexFlashControllerFsmTaskSeqId_Type = Gauge32
_CfprStorageFlexFlashControllerFsmTaskSeqId_Object = MibTableColumn
cfprStorageFlexFlashControllerFsmTaskSeqId = _CfprStorageFlexFlashControllerFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 17, 1, 7),
    _CfprStorageFlexFlashControllerFsmTaskSeqId_Type()
)
cfprStorageFlexFlashControllerFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashControllerFsmTaskSeqId.setStatus("current")
_CfprStorageFlexFlashDriveTable_Object = MibTable
cfprStorageFlexFlashDriveTable = _CfprStorageFlexFlashDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18)
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveTable.setStatus("current")
_CfprStorageFlexFlashDriveEntry_Object = MibTableRow
cfprStorageFlexFlashDriveEntry = _CfprStorageFlexFlashDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1)
)
cfprStorageFlexFlashDriveEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageFlexFlashDriveInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveEntry.setStatus("current")
_CfprStorageFlexFlashDriveInstanceId_Type = CfprManagedObjectId
_CfprStorageFlexFlashDriveInstanceId_Object = MibTableColumn
cfprStorageFlexFlashDriveInstanceId = _CfprStorageFlexFlashDriveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 1),
    _CfprStorageFlexFlashDriveInstanceId_Type()
)
cfprStorageFlexFlashDriveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveInstanceId.setStatus("current")
_CfprStorageFlexFlashDriveDn_Type = CfprManagedObjectDn
_CfprStorageFlexFlashDriveDn_Object = MibTableColumn
cfprStorageFlexFlashDriveDn = _CfprStorageFlexFlashDriveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 2),
    _CfprStorageFlexFlashDriveDn_Type()
)
cfprStorageFlexFlashDriveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveDn.setStatus("current")
_CfprStorageFlexFlashDriveRn_Type = SnmpAdminString
_CfprStorageFlexFlashDriveRn_Object = MibTableColumn
cfprStorageFlexFlashDriveRn = _CfprStorageFlexFlashDriveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 3),
    _CfprStorageFlexFlashDriveRn_Type()
)
cfprStorageFlexFlashDriveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveRn.setStatus("current")
_CfprStorageFlexFlashDriveRWType_Type = CfprStorageFFRWType
_CfprStorageFlexFlashDriveRWType_Object = MibTableColumn
cfprStorageFlexFlashDriveRWType = _CfprStorageFlexFlashDriveRWType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 4),
    _CfprStorageFlexFlashDriveRWType_Type()
)
cfprStorageFlexFlashDriveRWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveRWType.setStatus("current")
_CfprStorageFlexFlashDriveBlockSize_Type = Gauge32
_CfprStorageFlexFlashDriveBlockSize_Object = MibTableColumn
cfprStorageFlexFlashDriveBlockSize = _CfprStorageFlexFlashDriveBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 5),
    _CfprStorageFlexFlashDriveBlockSize_Type()
)
cfprStorageFlexFlashDriveBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveBlockSize.setStatus("current")
_CfprStorageFlexFlashDriveConnectionProtocol_Type = CfprStorageConnectionProtocol
_CfprStorageFlexFlashDriveConnectionProtocol_Object = MibTableColumn
cfprStorageFlexFlashDriveConnectionProtocol = _CfprStorageFlexFlashDriveConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 6),
    _CfprStorageFlexFlashDriveConnectionProtocol_Type()
)
cfprStorageFlexFlashDriveConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveConnectionProtocol.setStatus("current")
_CfprStorageFlexFlashDriveControllerIndex_Type = Gauge32
_CfprStorageFlexFlashDriveControllerIndex_Object = MibTableColumn
cfprStorageFlexFlashDriveControllerIndex = _CfprStorageFlexFlashDriveControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 7),
    _CfprStorageFlexFlashDriveControllerIndex_Type()
)
cfprStorageFlexFlashDriveControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveControllerIndex.setStatus("current")
_CfprStorageFlexFlashDriveDriveState_Type = CfprStorageFFDriveState
_CfprStorageFlexFlashDriveDriveState_Object = MibTableColumn
cfprStorageFlexFlashDriveDriveState = _CfprStorageFlexFlashDriveDriveState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 8),
    _CfprStorageFlexFlashDriveDriveState_Type()
)
cfprStorageFlexFlashDriveDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveDriveState.setStatus("current")
_CfprStorageFlexFlashDriveDriveType_Type = CfprStorageFFDriveType
_CfprStorageFlexFlashDriveDriveType_Object = MibTableColumn
cfprStorageFlexFlashDriveDriveType = _CfprStorageFlexFlashDriveDriveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 9),
    _CfprStorageFlexFlashDriveDriveType_Type()
)
cfprStorageFlexFlashDriveDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveDriveType.setStatus("current")
_CfprStorageFlexFlashDriveId_Type = Gauge32
_CfprStorageFlexFlashDriveId_Object = MibTableColumn
cfprStorageFlexFlashDriveId = _CfprStorageFlexFlashDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 10),
    _CfprStorageFlexFlashDriveId_Type()
)
cfprStorageFlexFlashDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveId.setStatus("current")
_CfprStorageFlexFlashDriveLastOperation_Type = CfprStorageOperationStateType
_CfprStorageFlexFlashDriveLastOperation_Object = MibTableColumn
cfprStorageFlexFlashDriveLastOperation = _CfprStorageFlexFlashDriveLastOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 11),
    _CfprStorageFlexFlashDriveLastOperation_Type()
)
cfprStorageFlexFlashDriveLastOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveLastOperation.setStatus("current")
_CfprStorageFlexFlashDriveModel_Type = SnmpAdminString
_CfprStorageFlexFlashDriveModel_Object = MibTableColumn
cfprStorageFlexFlashDriveModel = _CfprStorageFlexFlashDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 12),
    _CfprStorageFlexFlashDriveModel_Type()
)
cfprStorageFlexFlashDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveModel.setStatus("current")
_CfprStorageFlexFlashDriveName_Type = SnmpAdminString
_CfprStorageFlexFlashDriveName_Object = MibTableColumn
cfprStorageFlexFlashDriveName = _CfprStorageFlexFlashDriveName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 13),
    _CfprStorageFlexFlashDriveName_Type()
)
cfprStorageFlexFlashDriveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveName.setStatus("current")
_CfprStorageFlexFlashDriveNumberOfBlocks_Type = Unsigned64
_CfprStorageFlexFlashDriveNumberOfBlocks_Object = MibTableColumn
cfprStorageFlexFlashDriveNumberOfBlocks = _CfprStorageFlexFlashDriveNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 14),
    _CfprStorageFlexFlashDriveNumberOfBlocks_Type()
)
cfprStorageFlexFlashDriveNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveNumberOfBlocks.setStatus("current")
_CfprStorageFlexFlashDriveOperQualifierReason_Type = SnmpAdminString
_CfprStorageFlexFlashDriveOperQualifierReason_Object = MibTableColumn
cfprStorageFlexFlashDriveOperQualifierReason = _CfprStorageFlexFlashDriveOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 15),
    _CfprStorageFlexFlashDriveOperQualifierReason_Type()
)
cfprStorageFlexFlashDriveOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveOperQualifierReason.setStatus("current")
_CfprStorageFlexFlashDriveOperability_Type = CfprEquipmentOperability
_CfprStorageFlexFlashDriveOperability_Object = MibTableColumn
cfprStorageFlexFlashDriveOperability = _CfprStorageFlexFlashDriveOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 16),
    _CfprStorageFlexFlashDriveOperability_Type()
)
cfprStorageFlexFlashDriveOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveOperability.setStatus("current")
_CfprStorageFlexFlashDriveOperationState_Type = CfprStorageOperationStateType
_CfprStorageFlexFlashDriveOperationState_Object = MibTableColumn
cfprStorageFlexFlashDriveOperationState = _CfprStorageFlexFlashDriveOperationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 17),
    _CfprStorageFlexFlashDriveOperationState_Type()
)
cfprStorageFlexFlashDriveOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveOperationState.setStatus("current")
_CfprStorageFlexFlashDrivePresence_Type = CfprEquipmentPresence
_CfprStorageFlexFlashDrivePresence_Object = MibTableColumn
cfprStorageFlexFlashDrivePresence = _CfprStorageFlexFlashDrivePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 18),
    _CfprStorageFlexFlashDrivePresence_Type()
)
cfprStorageFlexFlashDrivePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDrivePresence.setStatus("current")
_CfprStorageFlexFlashDriveRemovable_Type = CfprStorageFFDriveRemovable
_CfprStorageFlexFlashDriveRemovable_Object = MibTableColumn
cfprStorageFlexFlashDriveRemovable = _CfprStorageFlexFlashDriveRemovable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 19),
    _CfprStorageFlexFlashDriveRemovable_Type()
)
cfprStorageFlexFlashDriveRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveRemovable.setStatus("current")
_CfprStorageFlexFlashDriveRevision_Type = SnmpAdminString
_CfprStorageFlexFlashDriveRevision_Object = MibTableColumn
cfprStorageFlexFlashDriveRevision = _CfprStorageFlexFlashDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 20),
    _CfprStorageFlexFlashDriveRevision_Type()
)
cfprStorageFlexFlashDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveRevision.setStatus("current")
_CfprStorageFlexFlashDriveSerial_Type = SnmpAdminString
_CfprStorageFlexFlashDriveSerial_Object = MibTableColumn
cfprStorageFlexFlashDriveSerial = _CfprStorageFlexFlashDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 21),
    _CfprStorageFlexFlashDriveSerial_Type()
)
cfprStorageFlexFlashDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveSerial.setStatus("current")
_CfprStorageFlexFlashDriveSize_Type = Unsigned64
_CfprStorageFlexFlashDriveSize_Object = MibTableColumn
cfprStorageFlexFlashDriveSize = _CfprStorageFlexFlashDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 22),
    _CfprStorageFlexFlashDriveSize_Type()
)
cfprStorageFlexFlashDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveSize.setStatus("current")
_CfprStorageFlexFlashDriveSlotNumber_Type = Gauge32
_CfprStorageFlexFlashDriveSlotNumber_Object = MibTableColumn
cfprStorageFlexFlashDriveSlotNumber = _CfprStorageFlexFlashDriveSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 23),
    _CfprStorageFlexFlashDriveSlotNumber_Type()
)
cfprStorageFlexFlashDriveSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveSlotNumber.setStatus("current")
_CfprStorageFlexFlashDriveVendor_Type = SnmpAdminString
_CfprStorageFlexFlashDriveVendor_Object = MibTableColumn
cfprStorageFlexFlashDriveVendor = _CfprStorageFlexFlashDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 24),
    _CfprStorageFlexFlashDriveVendor_Type()
)
cfprStorageFlexFlashDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveVendor.setStatus("current")
_CfprStorageFlexFlashDriveVisible_Type = CfprStorageFFDriveVisible
_CfprStorageFlexFlashDriveVisible_Object = MibTableColumn
cfprStorageFlexFlashDriveVisible = _CfprStorageFlexFlashDriveVisible_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 18, 1, 25),
    _CfprStorageFlexFlashDriveVisible_Type()
)
cfprStorageFlexFlashDriveVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashDriveVisible.setStatus("current")
_CfprStorageFlexFlashVirtualDriveTable_Object = MibTable
cfprStorageFlexFlashVirtualDriveTable = _CfprStorageFlexFlashVirtualDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19)
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveTable.setStatus("current")
_CfprStorageFlexFlashVirtualDriveEntry_Object = MibTableRow
cfprStorageFlexFlashVirtualDriveEntry = _CfprStorageFlexFlashVirtualDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1)
)
cfprStorageFlexFlashVirtualDriveEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageFlexFlashVirtualDriveInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveEntry.setStatus("current")
_CfprStorageFlexFlashVirtualDriveInstanceId_Type = CfprManagedObjectId
_CfprStorageFlexFlashVirtualDriveInstanceId_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveInstanceId = _CfprStorageFlexFlashVirtualDriveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 1),
    _CfprStorageFlexFlashVirtualDriveInstanceId_Type()
)
cfprStorageFlexFlashVirtualDriveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveInstanceId.setStatus("current")
_CfprStorageFlexFlashVirtualDriveDn_Type = CfprManagedObjectDn
_CfprStorageFlexFlashVirtualDriveDn_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveDn = _CfprStorageFlexFlashVirtualDriveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 2),
    _CfprStorageFlexFlashVirtualDriveDn_Type()
)
cfprStorageFlexFlashVirtualDriveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveDn.setStatus("current")
_CfprStorageFlexFlashVirtualDriveRn_Type = SnmpAdminString
_CfprStorageFlexFlashVirtualDriveRn_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveRn = _CfprStorageFlexFlashVirtualDriveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 3),
    _CfprStorageFlexFlashVirtualDriveRn_Type()
)
cfprStorageFlexFlashVirtualDriveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveRn.setStatus("current")
_CfprStorageFlexFlashVirtualDriveBlockSize_Type = Gauge32
_CfprStorageFlexFlashVirtualDriveBlockSize_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveBlockSize = _CfprStorageFlexFlashVirtualDriveBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 4),
    _CfprStorageFlexFlashVirtualDriveBlockSize_Type()
)
cfprStorageFlexFlashVirtualDriveBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveBlockSize.setStatus("current")
_CfprStorageFlexFlashVirtualDriveConnectionProtocol_Type = CfprStorageConnectionProtocol
_CfprStorageFlexFlashVirtualDriveConnectionProtocol_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveConnectionProtocol = _CfprStorageFlexFlashVirtualDriveConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 5),
    _CfprStorageFlexFlashVirtualDriveConnectionProtocol_Type()
)
cfprStorageFlexFlashVirtualDriveConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveConnectionProtocol.setStatus("current")
_CfprStorageFlexFlashVirtualDriveId_Type = Gauge32
_CfprStorageFlexFlashVirtualDriveId_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveId = _CfprStorageFlexFlashVirtualDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 6),
    _CfprStorageFlexFlashVirtualDriveId_Type()
)
cfprStorageFlexFlashVirtualDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveId.setStatus("current")
_CfprStorageFlexFlashVirtualDriveModel_Type = SnmpAdminString
_CfprStorageFlexFlashVirtualDriveModel_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveModel = _CfprStorageFlexFlashVirtualDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 7),
    _CfprStorageFlexFlashVirtualDriveModel_Type()
)
cfprStorageFlexFlashVirtualDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveModel.setStatus("current")
_CfprStorageFlexFlashVirtualDriveNumberOfBlocks_Type = Unsigned64
_CfprStorageFlexFlashVirtualDriveNumberOfBlocks_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveNumberOfBlocks = _CfprStorageFlexFlashVirtualDriveNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 8),
    _CfprStorageFlexFlashVirtualDriveNumberOfBlocks_Type()
)
cfprStorageFlexFlashVirtualDriveNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveNumberOfBlocks.setStatus("current")
_CfprStorageFlexFlashVirtualDriveOperQualifierReason_Type = SnmpAdminString
_CfprStorageFlexFlashVirtualDriveOperQualifierReason_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveOperQualifierReason = _CfprStorageFlexFlashVirtualDriveOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 9),
    _CfprStorageFlexFlashVirtualDriveOperQualifierReason_Type()
)
cfprStorageFlexFlashVirtualDriveOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveOperQualifierReason.setStatus("current")
_CfprStorageFlexFlashVirtualDriveOperability_Type = CfprEquipmentOperability
_CfprStorageFlexFlashVirtualDriveOperability_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveOperability = _CfprStorageFlexFlashVirtualDriveOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 10),
    _CfprStorageFlexFlashVirtualDriveOperability_Type()
)
cfprStorageFlexFlashVirtualDriveOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveOperability.setStatus("current")
_CfprStorageFlexFlashVirtualDrivePresence_Type = CfprEquipmentPresence
_CfprStorageFlexFlashVirtualDrivePresence_Object = MibTableColumn
cfprStorageFlexFlashVirtualDrivePresence = _CfprStorageFlexFlashVirtualDrivePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 11),
    _CfprStorageFlexFlashVirtualDrivePresence_Type()
)
cfprStorageFlexFlashVirtualDrivePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDrivePresence.setStatus("current")
_CfprStorageFlexFlashVirtualDriveRaidHealth_Type = CfprStorageFFRAIDHealth
_CfprStorageFlexFlashVirtualDriveRaidHealth_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveRaidHealth = _CfprStorageFlexFlashVirtualDriveRaidHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 12),
    _CfprStorageFlexFlashVirtualDriveRaidHealth_Type()
)
cfprStorageFlexFlashVirtualDriveRaidHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveRaidHealth.setStatus("current")
_CfprStorageFlexFlashVirtualDriveRaidState_Type = CfprStorageFFRAIDState
_CfprStorageFlexFlashVirtualDriveRaidState_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveRaidState = _CfprStorageFlexFlashVirtualDriveRaidState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 13),
    _CfprStorageFlexFlashVirtualDriveRaidState_Type()
)
cfprStorageFlexFlashVirtualDriveRaidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveRaidState.setStatus("current")
_CfprStorageFlexFlashVirtualDriveRevision_Type = SnmpAdminString
_CfprStorageFlexFlashVirtualDriveRevision_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveRevision = _CfprStorageFlexFlashVirtualDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 14),
    _CfprStorageFlexFlashVirtualDriveRevision_Type()
)
cfprStorageFlexFlashVirtualDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveRevision.setStatus("current")
_CfprStorageFlexFlashVirtualDriveSerial_Type = SnmpAdminString
_CfprStorageFlexFlashVirtualDriveSerial_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveSerial = _CfprStorageFlexFlashVirtualDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 15),
    _CfprStorageFlexFlashVirtualDriveSerial_Type()
)
cfprStorageFlexFlashVirtualDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveSerial.setStatus("current")
_CfprStorageFlexFlashVirtualDriveSize_Type = Unsigned64
_CfprStorageFlexFlashVirtualDriveSize_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveSize = _CfprStorageFlexFlashVirtualDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 16),
    _CfprStorageFlexFlashVirtualDriveSize_Type()
)
cfprStorageFlexFlashVirtualDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveSize.setStatus("current")
_CfprStorageFlexFlashVirtualDriveType_Type = CfprStorageLunType
_CfprStorageFlexFlashVirtualDriveType_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveType = _CfprStorageFlexFlashVirtualDriveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 17),
    _CfprStorageFlexFlashVirtualDriveType_Type()
)
cfprStorageFlexFlashVirtualDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveType.setStatus("current")
_CfprStorageFlexFlashVirtualDriveVendor_Type = SnmpAdminString
_CfprStorageFlexFlashVirtualDriveVendor_Object = MibTableColumn
cfprStorageFlexFlashVirtualDriveVendor = _CfprStorageFlexFlashVirtualDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 19, 1, 18),
    _CfprStorageFlexFlashVirtualDriveVendor_Type()
)
cfprStorageFlexFlashVirtualDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageFlexFlashVirtualDriveVendor.setStatus("current")
_CfprStorageIScsiTargetIfTable_Object = MibTable
cfprStorageIScsiTargetIfTable = _CfprStorageIScsiTargetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 20)
)
if mibBuilder.loadTexts:
    cfprStorageIScsiTargetIfTable.setStatus("current")
_CfprStorageIScsiTargetIfEntry_Object = MibTableRow
cfprStorageIScsiTargetIfEntry = _CfprStorageIScsiTargetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 20, 1)
)
cfprStorageIScsiTargetIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageIScsiTargetIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageIScsiTargetIfEntry.setStatus("current")
_CfprStorageIScsiTargetIfInstanceId_Type = CfprManagedObjectId
_CfprStorageIScsiTargetIfInstanceId_Object = MibTableColumn
cfprStorageIScsiTargetIfInstanceId = _CfprStorageIScsiTargetIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 20, 1, 1),
    _CfprStorageIScsiTargetIfInstanceId_Type()
)
cfprStorageIScsiTargetIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageIScsiTargetIfInstanceId.setStatus("current")
_CfprStorageIScsiTargetIfDn_Type = CfprManagedObjectDn
_CfprStorageIScsiTargetIfDn_Object = MibTableColumn
cfprStorageIScsiTargetIfDn = _CfprStorageIScsiTargetIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 20, 1, 2),
    _CfprStorageIScsiTargetIfDn_Type()
)
cfprStorageIScsiTargetIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIScsiTargetIfDn.setStatus("current")
_CfprStorageIScsiTargetIfRn_Type = SnmpAdminString
_CfprStorageIScsiTargetIfRn_Object = MibTableColumn
cfprStorageIScsiTargetIfRn = _CfprStorageIScsiTargetIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 20, 1, 3),
    _CfprStorageIScsiTargetIfRn_Type()
)
cfprStorageIScsiTargetIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIScsiTargetIfRn.setStatus("current")
_CfprStorageIScsiTargetIfName_Type = SnmpAdminString
_CfprStorageIScsiTargetIfName_Object = MibTableColumn
cfprStorageIScsiTargetIfName = _CfprStorageIScsiTargetIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 20, 1, 4),
    _CfprStorageIScsiTargetIfName_Type()
)
cfprStorageIScsiTargetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIScsiTargetIfName.setStatus("current")
_CfprStorageIScsiTargetIfProt_Type = CfprStorageProtocol
_CfprStorageIScsiTargetIfProt_Object = MibTableColumn
cfprStorageIScsiTargetIfProt = _CfprStorageIScsiTargetIfProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 20, 1, 5),
    _CfprStorageIScsiTargetIfProt_Type()
)
cfprStorageIScsiTargetIfProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIScsiTargetIfProt.setStatus("current")
_CfprStorageIniGroupTable_Object = MibTable
cfprStorageIniGroupTable = _CfprStorageIniGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21)
)
if mibBuilder.loadTexts:
    cfprStorageIniGroupTable.setStatus("current")
_CfprStorageIniGroupEntry_Object = MibTableRow
cfprStorageIniGroupEntry = _CfprStorageIniGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1)
)
cfprStorageIniGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageIniGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageIniGroupEntry.setStatus("current")
_CfprStorageIniGroupInstanceId_Type = CfprManagedObjectId
_CfprStorageIniGroupInstanceId_Object = MibTableColumn
cfprStorageIniGroupInstanceId = _CfprStorageIniGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 1),
    _CfprStorageIniGroupInstanceId_Type()
)
cfprStorageIniGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageIniGroupInstanceId.setStatus("current")
_CfprStorageIniGroupDn_Type = CfprManagedObjectDn
_CfprStorageIniGroupDn_Object = MibTableColumn
cfprStorageIniGroupDn = _CfprStorageIniGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 2),
    _CfprStorageIniGroupDn_Type()
)
cfprStorageIniGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupDn.setStatus("current")
_CfprStorageIniGroupRn_Type = SnmpAdminString
_CfprStorageIniGroupRn_Object = MibTableColumn
cfprStorageIniGroupRn = _CfprStorageIniGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 3),
    _CfprStorageIniGroupRn_Type()
)
cfprStorageIniGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupRn.setStatus("current")
_CfprStorageIniGroupDescr_Type = SnmpAdminString
_CfprStorageIniGroupDescr_Object = MibTableColumn
cfprStorageIniGroupDescr = _CfprStorageIniGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 4),
    _CfprStorageIniGroupDescr_Type()
)
cfprStorageIniGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupDescr.setStatus("current")
_CfprStorageIniGroupGroupPolicyName_Type = SnmpAdminString
_CfprStorageIniGroupGroupPolicyName_Object = MibTableColumn
cfprStorageIniGroupGroupPolicyName = _CfprStorageIniGroupGroupPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 5),
    _CfprStorageIniGroupGroupPolicyName_Type()
)
cfprStorageIniGroupGroupPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupGroupPolicyName.setStatus("current")
_CfprStorageIniGroupIntId_Type = SnmpAdminString
_CfprStorageIniGroupIntId_Object = MibTableColumn
cfprStorageIniGroupIntId = _CfprStorageIniGroupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 6),
    _CfprStorageIniGroupIntId_Type()
)
cfprStorageIniGroupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupIntId.setStatus("current")
_CfprStorageIniGroupName_Type = SnmpAdminString
_CfprStorageIniGroupName_Object = MibTableColumn
cfprStorageIniGroupName = _CfprStorageIniGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 7),
    _CfprStorageIniGroupName_Type()
)
cfprStorageIniGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupName.setStatus("current")
_CfprStorageIniGroupOperProtocol_Type = CfprStorageIniGroupOperProtocol
_CfprStorageIniGroupOperProtocol_Object = MibTableColumn
cfprStorageIniGroupOperProtocol = _CfprStorageIniGroupOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 8),
    _CfprStorageIniGroupOperProtocol_Type()
)
cfprStorageIniGroupOperProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupOperProtocol.setStatus("current")
_CfprStorageIniGroupOperState_Type = CfprStorageOperState
_CfprStorageIniGroupOperState_Object = MibTableColumn
cfprStorageIniGroupOperState = _CfprStorageIniGroupOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 9),
    _CfprStorageIniGroupOperState_Type()
)
cfprStorageIniGroupOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupOperState.setStatus("current")
_CfprStorageIniGroupOwner_Type = CfprStorageIniGroupOwner
_CfprStorageIniGroupOwner_Object = MibTableColumn
cfprStorageIniGroupOwner = _CfprStorageIniGroupOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 10),
    _CfprStorageIniGroupOwner_Type()
)
cfprStorageIniGroupOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupOwner.setStatus("current")
_CfprStorageIniGroupPolicyLevel_Type = Gauge32
_CfprStorageIniGroupPolicyLevel_Object = MibTableColumn
cfprStorageIniGroupPolicyLevel = _CfprStorageIniGroupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 11),
    _CfprStorageIniGroupPolicyLevel_Type()
)
cfprStorageIniGroupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupPolicyLevel.setStatus("current")
_CfprStorageIniGroupPolicyName_Type = SnmpAdminString
_CfprStorageIniGroupPolicyName_Object = MibTableColumn
cfprStorageIniGroupPolicyName = _CfprStorageIniGroupPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 12),
    _CfprStorageIniGroupPolicyName_Type()
)
cfprStorageIniGroupPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupPolicyName.setStatus("current")
_CfprStorageIniGroupPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStorageIniGroupPolicyOwner_Object = MibTableColumn
cfprStorageIniGroupPolicyOwner = _CfprStorageIniGroupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 13),
    _CfprStorageIniGroupPolicyOwner_Type()
)
cfprStorageIniGroupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupPolicyOwner.setStatus("current")
_CfprStorageIniGroupProtocol_Type = CfprStorageIniGroupProtocol
_CfprStorageIniGroupProtocol_Object = MibTableColumn
cfprStorageIniGroupProtocol = _CfprStorageIniGroupProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 14),
    _CfprStorageIniGroupProtocol_Type()
)
cfprStorageIniGroupProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupProtocol.setStatus("current")
_CfprStorageIniGroupRmtDiskCfgName_Type = SnmpAdminString
_CfprStorageIniGroupRmtDiskCfgName_Object = MibTableColumn
cfprStorageIniGroupRmtDiskCfgName = _CfprStorageIniGroupRmtDiskCfgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 21, 1, 15),
    _CfprStorageIniGroupRmtDiskCfgName_Type()
)
cfprStorageIniGroupRmtDiskCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageIniGroupRmtDiskCfgName.setStatus("current")
_CfprStorageInitiatorTable_Object = MibTable
cfprStorageInitiatorTable = _CfprStorageInitiatorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 22)
)
if mibBuilder.loadTexts:
    cfprStorageInitiatorTable.setStatus("current")
_CfprStorageInitiatorEntry_Object = MibTableRow
cfprStorageInitiatorEntry = _CfprStorageInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 22, 1)
)
cfprStorageInitiatorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageInitiatorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageInitiatorEntry.setStatus("current")
_CfprStorageInitiatorInstanceId_Type = CfprManagedObjectId
_CfprStorageInitiatorInstanceId_Object = MibTableColumn
cfprStorageInitiatorInstanceId = _CfprStorageInitiatorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 22, 1, 1),
    _CfprStorageInitiatorInstanceId_Type()
)
cfprStorageInitiatorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageInitiatorInstanceId.setStatus("current")
_CfprStorageInitiatorDn_Type = CfprManagedObjectDn
_CfprStorageInitiatorDn_Object = MibTableColumn
cfprStorageInitiatorDn = _CfprStorageInitiatorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 22, 1, 2),
    _CfprStorageInitiatorDn_Type()
)
cfprStorageInitiatorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageInitiatorDn.setStatus("current")
_CfprStorageInitiatorRn_Type = SnmpAdminString
_CfprStorageInitiatorRn_Object = MibTableColumn
cfprStorageInitiatorRn = _CfprStorageInitiatorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 22, 1, 3),
    _CfprStorageInitiatorRn_Type()
)
cfprStorageInitiatorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageInitiatorRn.setStatus("current")
_CfprStorageInitiatorDescr_Type = SnmpAdminString
_CfprStorageInitiatorDescr_Object = MibTableColumn
cfprStorageInitiatorDescr = _CfprStorageInitiatorDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 22, 1, 4),
    _CfprStorageInitiatorDescr_Type()
)
cfprStorageInitiatorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageInitiatorDescr.setStatus("current")
_CfprStorageInitiatorDuplicateTarget_Type = SnmpAdminString
_CfprStorageInitiatorDuplicateTarget_Object = MibTableColumn
cfprStorageInitiatorDuplicateTarget = _CfprStorageInitiatorDuplicateTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 22, 1, 5),
    _CfprStorageInitiatorDuplicateTarget_Type()
)
cfprStorageInitiatorDuplicateTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageInitiatorDuplicateTarget.setStatus("current")
_CfprStorageInitiatorIntId_Type = SnmpAdminString
_CfprStorageInitiatorIntId_Object = MibTableColumn
cfprStorageInitiatorIntId = _CfprStorageInitiatorIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 22, 1, 6),
    _CfprStorageInitiatorIntId_Type()
)
cfprStorageInitiatorIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageInitiatorIntId.setStatus("current")
_CfprStorageInitiatorName_Type = SnmpAdminString
_CfprStorageInitiatorName_Object = MibTableColumn
cfprStorageInitiatorName = _CfprStorageInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 22, 1, 7),
    _CfprStorageInitiatorName_Type()
)
cfprStorageInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageInitiatorName.setStatus("current")
_CfprStorageInitiatorOperState_Type = CfprStorageOperState
_CfprStorageInitiatorOperState_Object = MibTableColumn
cfprStorageInitiatorOperState = _CfprStorageInitiatorOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 22, 1, 8),
    _CfprStorageInitiatorOperState_Type()
)
cfprStorageInitiatorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageInitiatorOperState.setStatus("current")
_CfprStorageInitiatorPolicyLevel_Type = Gauge32
_CfprStorageInitiatorPolicyLevel_Object = MibTableColumn
cfprStorageInitiatorPolicyLevel = _CfprStorageInitiatorPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 22, 1, 9),
    _CfprStorageInitiatorPolicyLevel_Type()
)
cfprStorageInitiatorPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageInitiatorPolicyLevel.setStatus("current")
_CfprStorageInitiatorPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStorageInitiatorPolicyOwner_Object = MibTableColumn
cfprStorageInitiatorPolicyOwner = _CfprStorageInitiatorPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 22, 1, 10),
    _CfprStorageInitiatorPolicyOwner_Type()
)
cfprStorageInitiatorPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageInitiatorPolicyOwner.setStatus("current")
_CfprStorageItemTable_Object = MibTable
cfprStorageItemTable = _CfprStorageItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 23)
)
if mibBuilder.loadTexts:
    cfprStorageItemTable.setStatus("current")
_CfprStorageItemEntry_Object = MibTableRow
cfprStorageItemEntry = _CfprStorageItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 23, 1)
)
cfprStorageItemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageItemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageItemEntry.setStatus("current")
_CfprStorageItemInstanceId_Type = CfprManagedObjectId
_CfprStorageItemInstanceId_Object = MibTableColumn
cfprStorageItemInstanceId = _CfprStorageItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 23, 1, 1),
    _CfprStorageItemInstanceId_Type()
)
cfprStorageItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageItemInstanceId.setStatus("current")
_CfprStorageItemDn_Type = CfprManagedObjectDn
_CfprStorageItemDn_Object = MibTableColumn
cfprStorageItemDn = _CfprStorageItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 23, 1, 2),
    _CfprStorageItemDn_Type()
)
cfprStorageItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageItemDn.setStatus("current")
_CfprStorageItemRn_Type = SnmpAdminString
_CfprStorageItemRn_Object = MibTableColumn
cfprStorageItemRn = _CfprStorageItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 23, 1, 3),
    _CfprStorageItemRn_Type()
)
cfprStorageItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageItemRn.setStatus("current")
_CfprStorageItemName_Type = SnmpAdminString
_CfprStorageItemName_Object = MibTableColumn
cfprStorageItemName = _CfprStorageItemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 23, 1, 4),
    _CfprStorageItemName_Type()
)
cfprStorageItemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageItemName.setStatus("current")
_CfprStorageItemOperState_Type = CfprStorageFileSystemStatus
_CfprStorageItemOperState_Object = MibTableColumn
cfprStorageItemOperState = _CfprStorageItemOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 23, 1, 5),
    _CfprStorageItemOperState_Type()
)
cfprStorageItemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageItemOperState.setStatus("current")
_CfprStorageItemSize_Type = Unsigned64
_CfprStorageItemSize_Object = MibTableColumn
cfprStorageItemSize = _CfprStorageItemSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 23, 1, 6),
    _CfprStorageItemSize_Type()
)
cfprStorageItemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageItemSize.setStatus("current")
_CfprStorageItemUsed_Type = Gauge32
_CfprStorageItemUsed_Object = MibTableColumn
cfprStorageItemUsed = _CfprStorageItemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 23, 1, 7),
    _CfprStorageItemUsed_Type()
)
cfprStorageItemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageItemUsed.setStatus("current")
_CfprStorageLocalDiskTable_Object = MibTable
cfprStorageLocalDiskTable = _CfprStorageLocalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24)
)
if mibBuilder.loadTexts:
    cfprStorageLocalDiskTable.setStatus("current")
_CfprStorageLocalDiskEntry_Object = MibTableRow
cfprStorageLocalDiskEntry = _CfprStorageLocalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1)
)
cfprStorageLocalDiskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageLocalDiskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageLocalDiskEntry.setStatus("current")
_CfprStorageLocalDiskInstanceId_Type = CfprManagedObjectId
_CfprStorageLocalDiskInstanceId_Object = MibTableColumn
cfprStorageLocalDiskInstanceId = _CfprStorageLocalDiskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 1),
    _CfprStorageLocalDiskInstanceId_Type()
)
cfprStorageLocalDiskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskInstanceId.setStatus("current")
_CfprStorageLocalDiskDn_Type = CfprManagedObjectDn
_CfprStorageLocalDiskDn_Object = MibTableColumn
cfprStorageLocalDiskDn = _CfprStorageLocalDiskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 2),
    _CfprStorageLocalDiskDn_Type()
)
cfprStorageLocalDiskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskDn.setStatus("current")
_CfprStorageLocalDiskRn_Type = SnmpAdminString
_CfprStorageLocalDiskRn_Object = MibTableColumn
cfprStorageLocalDiskRn = _CfprStorageLocalDiskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 3),
    _CfprStorageLocalDiskRn_Type()
)
cfprStorageLocalDiskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskRn.setStatus("current")
_CfprStorageLocalDiskBlockSize_Type = Gauge32
_CfprStorageLocalDiskBlockSize_Object = MibTableColumn
cfprStorageLocalDiskBlockSize = _CfprStorageLocalDiskBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 4),
    _CfprStorageLocalDiskBlockSize_Type()
)
cfprStorageLocalDiskBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskBlockSize.setStatus("current")
_CfprStorageLocalDiskConnectionProtocol_Type = CfprStorageConnectionProtocol
_CfprStorageLocalDiskConnectionProtocol_Object = MibTableColumn
cfprStorageLocalDiskConnectionProtocol = _CfprStorageLocalDiskConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 5),
    _CfprStorageLocalDiskConnectionProtocol_Type()
)
cfprStorageLocalDiskConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConnectionProtocol.setStatus("current")
_CfprStorageLocalDiskDeviceType_Type = CfprStorageTechnology
_CfprStorageLocalDiskDeviceType_Object = MibTableColumn
cfprStorageLocalDiskDeviceType = _CfprStorageLocalDiskDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 6),
    _CfprStorageLocalDiskDeviceType_Type()
)
cfprStorageLocalDiskDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskDeviceType.setStatus("current")
_CfprStorageLocalDiskDiskState_Type = CfprStoragePDriveStatus
_CfprStorageLocalDiskDiskState_Object = MibTableColumn
cfprStorageLocalDiskDiskState = _CfprStorageLocalDiskDiskState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 7),
    _CfprStorageLocalDiskDiskState_Type()
)
cfprStorageLocalDiskDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskDiskState.setStatus("current")
_CfprStorageLocalDiskId_Type = Gauge32
_CfprStorageLocalDiskId_Object = MibTableColumn
cfprStorageLocalDiskId = _CfprStorageLocalDiskId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 8),
    _CfprStorageLocalDiskId_Type()
)
cfprStorageLocalDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskId.setStatus("current")
_CfprStorageLocalDiskLc_Type = CfprFsmLifecycle
_CfprStorageLocalDiskLc_Object = MibTableColumn
cfprStorageLocalDiskLc = _CfprStorageLocalDiskLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 9),
    _CfprStorageLocalDiskLc_Type()
)
cfprStorageLocalDiskLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskLc.setStatus("current")
_CfprStorageLocalDiskLinkSpeed_Type = CfprStorageLinkSpeed
_CfprStorageLocalDiskLinkSpeed_Object = MibTableColumn
cfprStorageLocalDiskLinkSpeed = _CfprStorageLocalDiskLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 10),
    _CfprStorageLocalDiskLinkSpeed_Type()
)
cfprStorageLocalDiskLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskLinkSpeed.setStatus("current")
_CfprStorageLocalDiskModel_Type = SnmpAdminString
_CfprStorageLocalDiskModel_Object = MibTableColumn
cfprStorageLocalDiskModel = _CfprStorageLocalDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 11),
    _CfprStorageLocalDiskModel_Type()
)
cfprStorageLocalDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskModel.setStatus("current")
_CfprStorageLocalDiskNumberOfBlocks_Type = Unsigned64
_CfprStorageLocalDiskNumberOfBlocks_Object = MibTableColumn
cfprStorageLocalDiskNumberOfBlocks = _CfprStorageLocalDiskNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 12),
    _CfprStorageLocalDiskNumberOfBlocks_Type()
)
cfprStorageLocalDiskNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskNumberOfBlocks.setStatus("current")
_CfprStorageLocalDiskOperQualifierReason_Type = SnmpAdminString
_CfprStorageLocalDiskOperQualifierReason_Object = MibTableColumn
cfprStorageLocalDiskOperQualifierReason = _CfprStorageLocalDiskOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 13),
    _CfprStorageLocalDiskOperQualifierReason_Type()
)
cfprStorageLocalDiskOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskOperQualifierReason.setStatus("current")
_CfprStorageLocalDiskOperability_Type = CfprEquipmentOperability
_CfprStorageLocalDiskOperability_Object = MibTableColumn
cfprStorageLocalDiskOperability = _CfprStorageLocalDiskOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 14),
    _CfprStorageLocalDiskOperability_Type()
)
cfprStorageLocalDiskOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskOperability.setStatus("current")
_CfprStorageLocalDiskPowerState_Type = CfprStoragePowerState
_CfprStorageLocalDiskPowerState_Object = MibTableColumn
cfprStorageLocalDiskPowerState = _CfprStorageLocalDiskPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 15),
    _CfprStorageLocalDiskPowerState_Type()
)
cfprStorageLocalDiskPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPowerState.setStatus("current")
_CfprStorageLocalDiskPresence_Type = CfprEquipmentPresence
_CfprStorageLocalDiskPresence_Object = MibTableColumn
cfprStorageLocalDiskPresence = _CfprStorageLocalDiskPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 16),
    _CfprStorageLocalDiskPresence_Type()
)
cfprStorageLocalDiskPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPresence.setStatus("current")
_CfprStorageLocalDiskRevision_Type = SnmpAdminString
_CfprStorageLocalDiskRevision_Object = MibTableColumn
cfprStorageLocalDiskRevision = _CfprStorageLocalDiskRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 17),
    _CfprStorageLocalDiskRevision_Type()
)
cfprStorageLocalDiskRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskRevision.setStatus("current")
_CfprStorageLocalDiskSerial_Type = SnmpAdminString
_CfprStorageLocalDiskSerial_Object = MibTableColumn
cfprStorageLocalDiskSerial = _CfprStorageLocalDiskSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 18),
    _CfprStorageLocalDiskSerial_Type()
)
cfprStorageLocalDiskSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSerial.setStatus("current")
_CfprStorageLocalDiskSize_Type = Unsigned64
_CfprStorageLocalDiskSize_Object = MibTableColumn
cfprStorageLocalDiskSize = _CfprStorageLocalDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 19),
    _CfprStorageLocalDiskSize_Type()
)
cfprStorageLocalDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSize.setStatus("current")
_CfprStorageLocalDiskVendor_Type = SnmpAdminString
_CfprStorageLocalDiskVendor_Object = MibTableColumn
cfprStorageLocalDiskVendor = _CfprStorageLocalDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 24, 1, 20),
    _CfprStorageLocalDiskVendor_Type()
)
cfprStorageLocalDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskVendor.setStatus("current")
_CfprStorageLocalDiskConfigDefTable_Object = MibTable
cfprStorageLocalDiskConfigDefTable = _CfprStorageLocalDiskConfigDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25)
)
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefTable.setStatus("current")
_CfprStorageLocalDiskConfigDefEntry_Object = MibTableRow
cfprStorageLocalDiskConfigDefEntry = _CfprStorageLocalDiskConfigDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1)
)
cfprStorageLocalDiskConfigDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageLocalDiskConfigDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefEntry.setStatus("current")
_CfprStorageLocalDiskConfigDefInstanceId_Type = CfprManagedObjectId
_CfprStorageLocalDiskConfigDefInstanceId_Object = MibTableColumn
cfprStorageLocalDiskConfigDefInstanceId = _CfprStorageLocalDiskConfigDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1, 1),
    _CfprStorageLocalDiskConfigDefInstanceId_Type()
)
cfprStorageLocalDiskConfigDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefInstanceId.setStatus("current")
_CfprStorageLocalDiskConfigDefDn_Type = CfprManagedObjectDn
_CfprStorageLocalDiskConfigDefDn_Object = MibTableColumn
cfprStorageLocalDiskConfigDefDn = _CfprStorageLocalDiskConfigDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1, 2),
    _CfprStorageLocalDiskConfigDefDn_Type()
)
cfprStorageLocalDiskConfigDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefDn.setStatus("current")
_CfprStorageLocalDiskConfigDefRn_Type = SnmpAdminString
_CfprStorageLocalDiskConfigDefRn_Object = MibTableColumn
cfprStorageLocalDiskConfigDefRn = _CfprStorageLocalDiskConfigDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1, 3),
    _CfprStorageLocalDiskConfigDefRn_Type()
)
cfprStorageLocalDiskConfigDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefRn.setStatus("current")
_CfprStorageLocalDiskConfigDefDescr_Type = SnmpAdminString
_CfprStorageLocalDiskConfigDefDescr_Object = MibTableColumn
cfprStorageLocalDiskConfigDefDescr = _CfprStorageLocalDiskConfigDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1, 4),
    _CfprStorageLocalDiskConfigDefDescr_Type()
)
cfprStorageLocalDiskConfigDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefDescr.setStatus("current")
_CfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Type = CfprStorageLocalDiskConfigFlexFlashRAIDReportingState
_CfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Object = MibTableColumn
cfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState = _CfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1, 5),
    _CfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Type()
)
cfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState.setStatus("current")
_CfprStorageLocalDiskConfigDefFlexFlashState_Type = CfprStorageLocalDiskConfigFlexFlashState
_CfprStorageLocalDiskConfigDefFlexFlashState_Object = MibTableColumn
cfprStorageLocalDiskConfigDefFlexFlashState = _CfprStorageLocalDiskConfigDefFlexFlashState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1, 6),
    _CfprStorageLocalDiskConfigDefFlexFlashState_Type()
)
cfprStorageLocalDiskConfigDefFlexFlashState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefFlexFlashState.setStatus("current")
_CfprStorageLocalDiskConfigDefIntId_Type = SnmpAdminString
_CfprStorageLocalDiskConfigDefIntId_Object = MibTableColumn
cfprStorageLocalDiskConfigDefIntId = _CfprStorageLocalDiskConfigDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1, 7),
    _CfprStorageLocalDiskConfigDefIntId_Type()
)
cfprStorageLocalDiskConfigDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefIntId.setStatus("current")
_CfprStorageLocalDiskConfigDefMode_Type = CfprStorageLocalDiskMode
_CfprStorageLocalDiskConfigDefMode_Object = MibTableColumn
cfprStorageLocalDiskConfigDefMode = _CfprStorageLocalDiskConfigDefMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1, 8),
    _CfprStorageLocalDiskConfigDefMode_Type()
)
cfprStorageLocalDiskConfigDefMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefMode.setStatus("current")
_CfprStorageLocalDiskConfigDefName_Type = SnmpAdminString
_CfprStorageLocalDiskConfigDefName_Object = MibTableColumn
cfprStorageLocalDiskConfigDefName = _CfprStorageLocalDiskConfigDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1, 9),
    _CfprStorageLocalDiskConfigDefName_Type()
)
cfprStorageLocalDiskConfigDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefName.setStatus("current")
_CfprStorageLocalDiskConfigDefPolicyLevel_Type = Gauge32
_CfprStorageLocalDiskConfigDefPolicyLevel_Object = MibTableColumn
cfprStorageLocalDiskConfigDefPolicyLevel = _CfprStorageLocalDiskConfigDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1, 10),
    _CfprStorageLocalDiskConfigDefPolicyLevel_Type()
)
cfprStorageLocalDiskConfigDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefPolicyLevel.setStatus("current")
_CfprStorageLocalDiskConfigDefPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStorageLocalDiskConfigDefPolicyOwner_Object = MibTableColumn
cfprStorageLocalDiskConfigDefPolicyOwner = _CfprStorageLocalDiskConfigDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1, 11),
    _CfprStorageLocalDiskConfigDefPolicyOwner_Type()
)
cfprStorageLocalDiskConfigDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefPolicyOwner.setStatus("current")
_CfprStorageLocalDiskConfigDefProtectConfig_Type = TruthValue
_CfprStorageLocalDiskConfigDefProtectConfig_Object = MibTableColumn
cfprStorageLocalDiskConfigDefProtectConfig = _CfprStorageLocalDiskConfigDefProtectConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 25, 1, 12),
    _CfprStorageLocalDiskConfigDefProtectConfig_Type()
)
cfprStorageLocalDiskConfigDefProtectConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigDefProtectConfig.setStatus("current")
_CfprStorageLocalDiskConfigPolicyTable_Object = MibTable
cfprStorageLocalDiskConfigPolicyTable = _CfprStorageLocalDiskConfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26)
)
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyTable.setStatus("current")
_CfprStorageLocalDiskConfigPolicyEntry_Object = MibTableRow
cfprStorageLocalDiskConfigPolicyEntry = _CfprStorageLocalDiskConfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1)
)
cfprStorageLocalDiskConfigPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageLocalDiskConfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyEntry.setStatus("current")
_CfprStorageLocalDiskConfigPolicyInstanceId_Type = CfprManagedObjectId
_CfprStorageLocalDiskConfigPolicyInstanceId_Object = MibTableColumn
cfprStorageLocalDiskConfigPolicyInstanceId = _CfprStorageLocalDiskConfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1, 1),
    _CfprStorageLocalDiskConfigPolicyInstanceId_Type()
)
cfprStorageLocalDiskConfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyInstanceId.setStatus("current")
_CfprStorageLocalDiskConfigPolicyDn_Type = CfprManagedObjectDn
_CfprStorageLocalDiskConfigPolicyDn_Object = MibTableColumn
cfprStorageLocalDiskConfigPolicyDn = _CfprStorageLocalDiskConfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1, 2),
    _CfprStorageLocalDiskConfigPolicyDn_Type()
)
cfprStorageLocalDiskConfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyDn.setStatus("current")
_CfprStorageLocalDiskConfigPolicyRn_Type = SnmpAdminString
_CfprStorageLocalDiskConfigPolicyRn_Object = MibTableColumn
cfprStorageLocalDiskConfigPolicyRn = _CfprStorageLocalDiskConfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1, 3),
    _CfprStorageLocalDiskConfigPolicyRn_Type()
)
cfprStorageLocalDiskConfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyRn.setStatus("current")
_CfprStorageLocalDiskConfigPolicyDescr_Type = SnmpAdminString
_CfprStorageLocalDiskConfigPolicyDescr_Object = MibTableColumn
cfprStorageLocalDiskConfigPolicyDescr = _CfprStorageLocalDiskConfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1, 4),
    _CfprStorageLocalDiskConfigPolicyDescr_Type()
)
cfprStorageLocalDiskConfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyDescr.setStatus("current")
_CfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Type = CfprStorageLocalDiskConfigFlexFlashRAIDReportingState
_CfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Object = MibTableColumn
cfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState = _CfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1, 5),
    _CfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Type()
)
cfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState.setStatus("current")
_CfprStorageLocalDiskConfigPolicyFlexFlashState_Type = CfprStorageLocalDiskConfigFlexFlashState
_CfprStorageLocalDiskConfigPolicyFlexFlashState_Object = MibTableColumn
cfprStorageLocalDiskConfigPolicyFlexFlashState = _CfprStorageLocalDiskConfigPolicyFlexFlashState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1, 6),
    _CfprStorageLocalDiskConfigPolicyFlexFlashState_Type()
)
cfprStorageLocalDiskConfigPolicyFlexFlashState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyFlexFlashState.setStatus("current")
_CfprStorageLocalDiskConfigPolicyIntId_Type = SnmpAdminString
_CfprStorageLocalDiskConfigPolicyIntId_Object = MibTableColumn
cfprStorageLocalDiskConfigPolicyIntId = _CfprStorageLocalDiskConfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1, 7),
    _CfprStorageLocalDiskConfigPolicyIntId_Type()
)
cfprStorageLocalDiskConfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyIntId.setStatus("current")
_CfprStorageLocalDiskConfigPolicyMode_Type = CfprStorageLocalDiskMode
_CfprStorageLocalDiskConfigPolicyMode_Object = MibTableColumn
cfprStorageLocalDiskConfigPolicyMode = _CfprStorageLocalDiskConfigPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1, 8),
    _CfprStorageLocalDiskConfigPolicyMode_Type()
)
cfprStorageLocalDiskConfigPolicyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyMode.setStatus("current")
_CfprStorageLocalDiskConfigPolicyName_Type = SnmpAdminString
_CfprStorageLocalDiskConfigPolicyName_Object = MibTableColumn
cfprStorageLocalDiskConfigPolicyName = _CfprStorageLocalDiskConfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1, 9),
    _CfprStorageLocalDiskConfigPolicyName_Type()
)
cfprStorageLocalDiskConfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyName.setStatus("current")
_CfprStorageLocalDiskConfigPolicyPolicyLevel_Type = Gauge32
_CfprStorageLocalDiskConfigPolicyPolicyLevel_Object = MibTableColumn
cfprStorageLocalDiskConfigPolicyPolicyLevel = _CfprStorageLocalDiskConfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1, 10),
    _CfprStorageLocalDiskConfigPolicyPolicyLevel_Type()
)
cfprStorageLocalDiskConfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyPolicyLevel.setStatus("current")
_CfprStorageLocalDiskConfigPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStorageLocalDiskConfigPolicyPolicyOwner_Object = MibTableColumn
cfprStorageLocalDiskConfigPolicyPolicyOwner = _CfprStorageLocalDiskConfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1, 11),
    _CfprStorageLocalDiskConfigPolicyPolicyOwner_Type()
)
cfprStorageLocalDiskConfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyPolicyOwner.setStatus("current")
_CfprStorageLocalDiskConfigPolicyProtectConfig_Type = TruthValue
_CfprStorageLocalDiskConfigPolicyProtectConfig_Object = MibTableColumn
cfprStorageLocalDiskConfigPolicyProtectConfig = _CfprStorageLocalDiskConfigPolicyProtectConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 26, 1, 12),
    _CfprStorageLocalDiskConfigPolicyProtectConfig_Type()
)
cfprStorageLocalDiskConfigPolicyProtectConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskConfigPolicyProtectConfig.setStatus("current")
_CfprStorageLocalDiskPartitionTable_Object = MibTable
cfprStorageLocalDiskPartitionTable = _CfprStorageLocalDiskPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27)
)
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionTable.setStatus("current")
_CfprStorageLocalDiskPartitionEntry_Object = MibTableRow
cfprStorageLocalDiskPartitionEntry = _CfprStorageLocalDiskPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27, 1)
)
cfprStorageLocalDiskPartitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageLocalDiskPartitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionEntry.setStatus("current")
_CfprStorageLocalDiskPartitionInstanceId_Type = CfprManagedObjectId
_CfprStorageLocalDiskPartitionInstanceId_Object = MibTableColumn
cfprStorageLocalDiskPartitionInstanceId = _CfprStorageLocalDiskPartitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27, 1, 1),
    _CfprStorageLocalDiskPartitionInstanceId_Type()
)
cfprStorageLocalDiskPartitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionInstanceId.setStatus("current")
_CfprStorageLocalDiskPartitionDn_Type = CfprManagedObjectDn
_CfprStorageLocalDiskPartitionDn_Object = MibTableColumn
cfprStorageLocalDiskPartitionDn = _CfprStorageLocalDiskPartitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27, 1, 2),
    _CfprStorageLocalDiskPartitionDn_Type()
)
cfprStorageLocalDiskPartitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionDn.setStatus("current")
_CfprStorageLocalDiskPartitionRn_Type = SnmpAdminString
_CfprStorageLocalDiskPartitionRn_Object = MibTableColumn
cfprStorageLocalDiskPartitionRn = _CfprStorageLocalDiskPartitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27, 1, 3),
    _CfprStorageLocalDiskPartitionRn_Type()
)
cfprStorageLocalDiskPartitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionRn.setStatus("current")
_CfprStorageLocalDiskPartitionDescr_Type = SnmpAdminString
_CfprStorageLocalDiskPartitionDescr_Object = MibTableColumn
cfprStorageLocalDiskPartitionDescr = _CfprStorageLocalDiskPartitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27, 1, 4),
    _CfprStorageLocalDiskPartitionDescr_Type()
)
cfprStorageLocalDiskPartitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionDescr.setStatus("current")
_CfprStorageLocalDiskPartitionIntId_Type = SnmpAdminString
_CfprStorageLocalDiskPartitionIntId_Object = MibTableColumn
cfprStorageLocalDiskPartitionIntId = _CfprStorageLocalDiskPartitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27, 1, 5),
    _CfprStorageLocalDiskPartitionIntId_Type()
)
cfprStorageLocalDiskPartitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionIntId.setStatus("current")
_CfprStorageLocalDiskPartitionName_Type = SnmpAdminString
_CfprStorageLocalDiskPartitionName_Object = MibTableColumn
cfprStorageLocalDiskPartitionName = _CfprStorageLocalDiskPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27, 1, 6),
    _CfprStorageLocalDiskPartitionName_Type()
)
cfprStorageLocalDiskPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionName.setStatus("current")
_CfprStorageLocalDiskPartitionOrder_Type = Gauge32
_CfprStorageLocalDiskPartitionOrder_Object = MibTableColumn
cfprStorageLocalDiskPartitionOrder = _CfprStorageLocalDiskPartitionOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27, 1, 7),
    _CfprStorageLocalDiskPartitionOrder_Type()
)
cfprStorageLocalDiskPartitionOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionOrder.setStatus("current")
_CfprStorageLocalDiskPartitionPolicyLevel_Type = Gauge32
_CfprStorageLocalDiskPartitionPolicyLevel_Object = MibTableColumn
cfprStorageLocalDiskPartitionPolicyLevel = _CfprStorageLocalDiskPartitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27, 1, 8),
    _CfprStorageLocalDiskPartitionPolicyLevel_Type()
)
cfprStorageLocalDiskPartitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionPolicyLevel.setStatus("current")
_CfprStorageLocalDiskPartitionPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStorageLocalDiskPartitionPolicyOwner_Object = MibTableColumn
cfprStorageLocalDiskPartitionPolicyOwner = _CfprStorageLocalDiskPartitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27, 1, 9),
    _CfprStorageLocalDiskPartitionPolicyOwner_Type()
)
cfprStorageLocalDiskPartitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionPolicyOwner.setStatus("current")
_CfprStorageLocalDiskPartitionSize_Type = Unsigned64
_CfprStorageLocalDiskPartitionSize_Object = MibTableColumn
cfprStorageLocalDiskPartitionSize = _CfprStorageLocalDiskPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27, 1, 10),
    _CfprStorageLocalDiskPartitionSize_Type()
)
cfprStorageLocalDiskPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionSize.setStatus("current")
_CfprStorageLocalDiskPartitionType_Type = CfprStorageLocalDiskPartitionType
_CfprStorageLocalDiskPartitionType_Object = MibTableColumn
cfprStorageLocalDiskPartitionType = _CfprStorageLocalDiskPartitionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 27, 1, 11),
    _CfprStorageLocalDiskPartitionType_Type()
)
cfprStorageLocalDiskPartitionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskPartitionType.setStatus("current")
_CfprStorageLocalDiskSlotEpTable_Object = MibTable
cfprStorageLocalDiskSlotEpTable = _CfprStorageLocalDiskSlotEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 28)
)
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSlotEpTable.setStatus("current")
_CfprStorageLocalDiskSlotEpEntry_Object = MibTableRow
cfprStorageLocalDiskSlotEpEntry = _CfprStorageLocalDiskSlotEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 28, 1)
)
cfprStorageLocalDiskSlotEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageLocalDiskSlotEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSlotEpEntry.setStatus("current")
_CfprStorageLocalDiskSlotEpInstanceId_Type = CfprManagedObjectId
_CfprStorageLocalDiskSlotEpInstanceId_Object = MibTableColumn
cfprStorageLocalDiskSlotEpInstanceId = _CfprStorageLocalDiskSlotEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 28, 1, 1),
    _CfprStorageLocalDiskSlotEpInstanceId_Type()
)
cfprStorageLocalDiskSlotEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSlotEpInstanceId.setStatus("current")
_CfprStorageLocalDiskSlotEpDn_Type = CfprManagedObjectDn
_CfprStorageLocalDiskSlotEpDn_Object = MibTableColumn
cfprStorageLocalDiskSlotEpDn = _CfprStorageLocalDiskSlotEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 28, 1, 2),
    _CfprStorageLocalDiskSlotEpDn_Type()
)
cfprStorageLocalDiskSlotEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSlotEpDn.setStatus("current")
_CfprStorageLocalDiskSlotEpRn_Type = SnmpAdminString
_CfprStorageLocalDiskSlotEpRn_Object = MibTableColumn
cfprStorageLocalDiskSlotEpRn = _CfprStorageLocalDiskSlotEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 28, 1, 3),
    _CfprStorageLocalDiskSlotEpRn_Type()
)
cfprStorageLocalDiskSlotEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSlotEpRn.setStatus("current")
_CfprStorageLocalDiskSlotEpConfiguration_Type = CfprStorageConfiguration
_CfprStorageLocalDiskSlotEpConfiguration_Object = MibTableColumn
cfprStorageLocalDiskSlotEpConfiguration = _CfprStorageLocalDiskSlotEpConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 28, 1, 4),
    _CfprStorageLocalDiskSlotEpConfiguration_Type()
)
cfprStorageLocalDiskSlotEpConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSlotEpConfiguration.setStatus("current")
_CfprStorageLocalDiskSlotEpId_Type = Gauge32
_CfprStorageLocalDiskSlotEpId_Object = MibTableColumn
cfprStorageLocalDiskSlotEpId = _CfprStorageLocalDiskSlotEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 28, 1, 5),
    _CfprStorageLocalDiskSlotEpId_Type()
)
cfprStorageLocalDiskSlotEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSlotEpId.setStatus("current")
_CfprStorageLocalDiskSlotEpOperQualifierReason_Type = SnmpAdminString
_CfprStorageLocalDiskSlotEpOperQualifierReason_Object = MibTableColumn
cfprStorageLocalDiskSlotEpOperQualifierReason = _CfprStorageLocalDiskSlotEpOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 28, 1, 6),
    _CfprStorageLocalDiskSlotEpOperQualifierReason_Type()
)
cfprStorageLocalDiskSlotEpOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSlotEpOperQualifierReason.setStatus("current")
_CfprStorageLocalDiskSlotEpOperability_Type = CfprEquipmentOperability
_CfprStorageLocalDiskSlotEpOperability_Object = MibTableColumn
cfprStorageLocalDiskSlotEpOperability = _CfprStorageLocalDiskSlotEpOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 28, 1, 7),
    _CfprStorageLocalDiskSlotEpOperability_Type()
)
cfprStorageLocalDiskSlotEpOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSlotEpOperability.setStatus("current")
_CfprStorageLocalDiskSlotEpPeerDn_Type = SnmpAdminString
_CfprStorageLocalDiskSlotEpPeerDn_Object = MibTableColumn
cfprStorageLocalDiskSlotEpPeerDn = _CfprStorageLocalDiskSlotEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 28, 1, 8),
    _CfprStorageLocalDiskSlotEpPeerDn_Type()
)
cfprStorageLocalDiskSlotEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSlotEpPeerDn.setStatus("current")
_CfprStorageLocalDiskSlotEpPresence_Type = CfprEquipmentPresence
_CfprStorageLocalDiskSlotEpPresence_Object = MibTableColumn
cfprStorageLocalDiskSlotEpPresence = _CfprStorageLocalDiskSlotEpPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 28, 1, 9),
    _CfprStorageLocalDiskSlotEpPresence_Type()
)
cfprStorageLocalDiskSlotEpPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalDiskSlotEpPresence.setStatus("current")
_CfprStorageLocalLunTable_Object = MibTable
cfprStorageLocalLunTable = _CfprStorageLocalLunTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29)
)
if mibBuilder.loadTexts:
    cfprStorageLocalLunTable.setStatus("current")
_CfprStorageLocalLunEntry_Object = MibTableRow
cfprStorageLocalLunEntry = _CfprStorageLocalLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1)
)
cfprStorageLocalLunEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageLocalLunInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageLocalLunEntry.setStatus("current")
_CfprStorageLocalLunInstanceId_Type = CfprManagedObjectId
_CfprStorageLocalLunInstanceId_Object = MibTableColumn
cfprStorageLocalLunInstanceId = _CfprStorageLocalLunInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 1),
    _CfprStorageLocalLunInstanceId_Type()
)
cfprStorageLocalLunInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageLocalLunInstanceId.setStatus("current")
_CfprStorageLocalLunDn_Type = CfprManagedObjectDn
_CfprStorageLocalLunDn_Object = MibTableColumn
cfprStorageLocalLunDn = _CfprStorageLocalLunDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 2),
    _CfprStorageLocalLunDn_Type()
)
cfprStorageLocalLunDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunDn.setStatus("current")
_CfprStorageLocalLunRn_Type = SnmpAdminString
_CfprStorageLocalLunRn_Object = MibTableColumn
cfprStorageLocalLunRn = _CfprStorageLocalLunRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 3),
    _CfprStorageLocalLunRn_Type()
)
cfprStorageLocalLunRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunRn.setStatus("current")
_CfprStorageLocalLunBlockSize_Type = Gauge32
_CfprStorageLocalLunBlockSize_Object = MibTableColumn
cfprStorageLocalLunBlockSize = _CfprStorageLocalLunBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 4),
    _CfprStorageLocalLunBlockSize_Type()
)
cfprStorageLocalLunBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunBlockSize.setStatus("current")
_CfprStorageLocalLunConnectionProtocol_Type = CfprStorageConnectionProtocol
_CfprStorageLocalLunConnectionProtocol_Object = MibTableColumn
cfprStorageLocalLunConnectionProtocol = _CfprStorageLocalLunConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 5),
    _CfprStorageLocalLunConnectionProtocol_Type()
)
cfprStorageLocalLunConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunConnectionProtocol.setStatus("current")
_CfprStorageLocalLunId_Type = Gauge32
_CfprStorageLocalLunId_Object = MibTableColumn
cfprStorageLocalLunId = _CfprStorageLocalLunId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 6),
    _CfprStorageLocalLunId_Type()
)
cfprStorageLocalLunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunId.setStatus("current")
_CfprStorageLocalLunLc_Type = CfprFsmLifecycle
_CfprStorageLocalLunLc_Object = MibTableColumn
cfprStorageLocalLunLc = _CfprStorageLocalLunLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 7),
    _CfprStorageLocalLunLc_Type()
)
cfprStorageLocalLunLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunLc.setStatus("current")
_CfprStorageLocalLunModel_Type = SnmpAdminString
_CfprStorageLocalLunModel_Object = MibTableColumn
cfprStorageLocalLunModel = _CfprStorageLocalLunModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 8),
    _CfprStorageLocalLunModel_Type()
)
cfprStorageLocalLunModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunModel.setStatus("current")
_CfprStorageLocalLunNumberOfBlocks_Type = Unsigned64
_CfprStorageLocalLunNumberOfBlocks_Object = MibTableColumn
cfprStorageLocalLunNumberOfBlocks = _CfprStorageLocalLunNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 9),
    _CfprStorageLocalLunNumberOfBlocks_Type()
)
cfprStorageLocalLunNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunNumberOfBlocks.setStatus("current")
_CfprStorageLocalLunOperQualifierReason_Type = SnmpAdminString
_CfprStorageLocalLunOperQualifierReason_Object = MibTableColumn
cfprStorageLocalLunOperQualifierReason = _CfprStorageLocalLunOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 10),
    _CfprStorageLocalLunOperQualifierReason_Type()
)
cfprStorageLocalLunOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunOperQualifierReason.setStatus("current")
_CfprStorageLocalLunOperability_Type = CfprEquipmentOperability
_CfprStorageLocalLunOperability_Object = MibTableColumn
cfprStorageLocalLunOperability = _CfprStorageLocalLunOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 11),
    _CfprStorageLocalLunOperability_Type()
)
cfprStorageLocalLunOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunOperability.setStatus("current")
_CfprStorageLocalLunPresence_Type = CfprEquipmentPresence
_CfprStorageLocalLunPresence_Object = MibTableColumn
cfprStorageLocalLunPresence = _CfprStorageLocalLunPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 12),
    _CfprStorageLocalLunPresence_Type()
)
cfprStorageLocalLunPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunPresence.setStatus("current")
_CfprStorageLocalLunRevision_Type = SnmpAdminString
_CfprStorageLocalLunRevision_Object = MibTableColumn
cfprStorageLocalLunRevision = _CfprStorageLocalLunRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 13),
    _CfprStorageLocalLunRevision_Type()
)
cfprStorageLocalLunRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunRevision.setStatus("current")
_CfprStorageLocalLunSerial_Type = SnmpAdminString
_CfprStorageLocalLunSerial_Object = MibTableColumn
cfprStorageLocalLunSerial = _CfprStorageLocalLunSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 14),
    _CfprStorageLocalLunSerial_Type()
)
cfprStorageLocalLunSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunSerial.setStatus("current")
_CfprStorageLocalLunSize_Type = Unsigned64
_CfprStorageLocalLunSize_Object = MibTableColumn
cfprStorageLocalLunSize = _CfprStorageLocalLunSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 15),
    _CfprStorageLocalLunSize_Type()
)
cfprStorageLocalLunSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunSize.setStatus("current")
_CfprStorageLocalLunType_Type = CfprStorageLunType
_CfprStorageLocalLunType_Object = MibTableColumn
cfprStorageLocalLunType = _CfprStorageLocalLunType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 16),
    _CfprStorageLocalLunType_Type()
)
cfprStorageLocalLunType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunType.setStatus("current")
_CfprStorageLocalLunVendor_Type = SnmpAdminString
_CfprStorageLocalLunVendor_Object = MibTableColumn
cfprStorageLocalLunVendor = _CfprStorageLocalLunVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 29, 1, 17),
    _CfprStorageLocalLunVendor_Type()
)
cfprStorageLocalLunVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLocalLunVendor.setStatus("current")
_CfprStorageLunDiskTable_Object = MibTable
cfprStorageLunDiskTable = _CfprStorageLunDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 30)
)
if mibBuilder.loadTexts:
    cfprStorageLunDiskTable.setStatus("current")
_CfprStorageLunDiskEntry_Object = MibTableRow
cfprStorageLunDiskEntry = _CfprStorageLunDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 30, 1)
)
cfprStorageLunDiskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageLunDiskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageLunDiskEntry.setStatus("current")
_CfprStorageLunDiskInstanceId_Type = CfprManagedObjectId
_CfprStorageLunDiskInstanceId_Object = MibTableColumn
cfprStorageLunDiskInstanceId = _CfprStorageLunDiskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 30, 1, 1),
    _CfprStorageLunDiskInstanceId_Type()
)
cfprStorageLunDiskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageLunDiskInstanceId.setStatus("current")
_CfprStorageLunDiskDn_Type = CfprManagedObjectDn
_CfprStorageLunDiskDn_Object = MibTableColumn
cfprStorageLunDiskDn = _CfprStorageLunDiskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 30, 1, 2),
    _CfprStorageLunDiskDn_Type()
)
cfprStorageLunDiskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLunDiskDn.setStatus("current")
_CfprStorageLunDiskRn_Type = SnmpAdminString
_CfprStorageLunDiskRn_Object = MibTableColumn
cfprStorageLunDiskRn = _CfprStorageLunDiskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 30, 1, 3),
    _CfprStorageLunDiskRn_Type()
)
cfprStorageLunDiskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLunDiskRn.setStatus("current")
_CfprStorageLunDiskId_Type = Gauge32
_CfprStorageLunDiskId_Object = MibTableColumn
cfprStorageLunDiskId = _CfprStorageLunDiskId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 30, 1, 4),
    _CfprStorageLunDiskId_Type()
)
cfprStorageLunDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageLunDiskId.setStatus("current")
_CfprStorageMezzFlashLifeTable_Object = MibTable
cfprStorageMezzFlashLifeTable = _CfprStorageMezzFlashLifeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31)
)
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeTable.setStatus("current")
_CfprStorageMezzFlashLifeEntry_Object = MibTableRow
cfprStorageMezzFlashLifeEntry = _CfprStorageMezzFlashLifeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1)
)
cfprStorageMezzFlashLifeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageMezzFlashLifeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeEntry.setStatus("current")
_CfprStorageMezzFlashLifeInstanceId_Type = CfprManagedObjectId
_CfprStorageMezzFlashLifeInstanceId_Object = MibTableColumn
cfprStorageMezzFlashLifeInstanceId = _CfprStorageMezzFlashLifeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 1),
    _CfprStorageMezzFlashLifeInstanceId_Type()
)
cfprStorageMezzFlashLifeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeInstanceId.setStatus("current")
_CfprStorageMezzFlashLifeDn_Type = CfprManagedObjectDn
_CfprStorageMezzFlashLifeDn_Object = MibTableColumn
cfprStorageMezzFlashLifeDn = _CfprStorageMezzFlashLifeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 2),
    _CfprStorageMezzFlashLifeDn_Type()
)
cfprStorageMezzFlashLifeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeDn.setStatus("current")
_CfprStorageMezzFlashLifeRn_Type = SnmpAdminString
_CfprStorageMezzFlashLifeRn_Object = MibTableColumn
cfprStorageMezzFlashLifeRn = _CfprStorageMezzFlashLifeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 3),
    _CfprStorageMezzFlashLifeRn_Type()
)
cfprStorageMezzFlashLifeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeRn.setStatus("current")
_CfprStorageMezzFlashLifeBlockSize_Type = Gauge32
_CfprStorageMezzFlashLifeBlockSize_Object = MibTableColumn
cfprStorageMezzFlashLifeBlockSize = _CfprStorageMezzFlashLifeBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 4),
    _CfprStorageMezzFlashLifeBlockSize_Type()
)
cfprStorageMezzFlashLifeBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeBlockSize.setStatus("current")
_CfprStorageMezzFlashLifeConnectionProtocol_Type = CfprStorageConnectionProtocol
_CfprStorageMezzFlashLifeConnectionProtocol_Object = MibTableColumn
cfprStorageMezzFlashLifeConnectionProtocol = _CfprStorageMezzFlashLifeConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 5),
    _CfprStorageMezzFlashLifeConnectionProtocol_Type()
)
cfprStorageMezzFlashLifeConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeConnectionProtocol.setStatus("current")
_CfprStorageMezzFlashLifeFlashPercentage_Type = SnmpAdminString
_CfprStorageMezzFlashLifeFlashPercentage_Object = MibTableColumn
cfprStorageMezzFlashLifeFlashPercentage = _CfprStorageMezzFlashLifeFlashPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 6),
    _CfprStorageMezzFlashLifeFlashPercentage_Type()
)
cfprStorageMezzFlashLifeFlashPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeFlashPercentage.setStatus("current")
_CfprStorageMezzFlashLifeFlashStatus_Type = SnmpAdminString
_CfprStorageMezzFlashLifeFlashStatus_Object = MibTableColumn
cfprStorageMezzFlashLifeFlashStatus = _CfprStorageMezzFlashLifeFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 7),
    _CfprStorageMezzFlashLifeFlashStatus_Type()
)
cfprStorageMezzFlashLifeFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeFlashStatus.setStatus("current")
_CfprStorageMezzFlashLifeId_Type = Gauge32
_CfprStorageMezzFlashLifeId_Object = MibTableColumn
cfprStorageMezzFlashLifeId = _CfprStorageMezzFlashLifeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 8),
    _CfprStorageMezzFlashLifeId_Type()
)
cfprStorageMezzFlashLifeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeId.setStatus("current")
_CfprStorageMezzFlashLifeModel_Type = SnmpAdminString
_CfprStorageMezzFlashLifeModel_Object = MibTableColumn
cfprStorageMezzFlashLifeModel = _CfprStorageMezzFlashLifeModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 9),
    _CfprStorageMezzFlashLifeModel_Type()
)
cfprStorageMezzFlashLifeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeModel.setStatus("current")
_CfprStorageMezzFlashLifeNumberOfBlocks_Type = Unsigned64
_CfprStorageMezzFlashLifeNumberOfBlocks_Object = MibTableColumn
cfprStorageMezzFlashLifeNumberOfBlocks = _CfprStorageMezzFlashLifeNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 10),
    _CfprStorageMezzFlashLifeNumberOfBlocks_Type()
)
cfprStorageMezzFlashLifeNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeNumberOfBlocks.setStatus("current")
_CfprStorageMezzFlashLifeOperQualifierReason_Type = SnmpAdminString
_CfprStorageMezzFlashLifeOperQualifierReason_Object = MibTableColumn
cfprStorageMezzFlashLifeOperQualifierReason = _CfprStorageMezzFlashLifeOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 11),
    _CfprStorageMezzFlashLifeOperQualifierReason_Type()
)
cfprStorageMezzFlashLifeOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeOperQualifierReason.setStatus("current")
_CfprStorageMezzFlashLifeOperability_Type = CfprEquipmentOperability
_CfprStorageMezzFlashLifeOperability_Object = MibTableColumn
cfprStorageMezzFlashLifeOperability = _CfprStorageMezzFlashLifeOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 12),
    _CfprStorageMezzFlashLifeOperability_Type()
)
cfprStorageMezzFlashLifeOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeOperability.setStatus("current")
_CfprStorageMezzFlashLifePresence_Type = CfprEquipmentPresence
_CfprStorageMezzFlashLifePresence_Object = MibTableColumn
cfprStorageMezzFlashLifePresence = _CfprStorageMezzFlashLifePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 13),
    _CfprStorageMezzFlashLifePresence_Type()
)
cfprStorageMezzFlashLifePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifePresence.setStatus("current")
_CfprStorageMezzFlashLifeRevision_Type = SnmpAdminString
_CfprStorageMezzFlashLifeRevision_Object = MibTableColumn
cfprStorageMezzFlashLifeRevision = _CfprStorageMezzFlashLifeRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 14),
    _CfprStorageMezzFlashLifeRevision_Type()
)
cfprStorageMezzFlashLifeRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeRevision.setStatus("current")
_CfprStorageMezzFlashLifeSerial_Type = SnmpAdminString
_CfprStorageMezzFlashLifeSerial_Object = MibTableColumn
cfprStorageMezzFlashLifeSerial = _CfprStorageMezzFlashLifeSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 15),
    _CfprStorageMezzFlashLifeSerial_Type()
)
cfprStorageMezzFlashLifeSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeSerial.setStatus("current")
_CfprStorageMezzFlashLifeSize_Type = Unsigned64
_CfprStorageMezzFlashLifeSize_Object = MibTableColumn
cfprStorageMezzFlashLifeSize = _CfprStorageMezzFlashLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 16),
    _CfprStorageMezzFlashLifeSize_Type()
)
cfprStorageMezzFlashLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeSize.setStatus("current")
_CfprStorageMezzFlashLifeVendor_Type = SnmpAdminString
_CfprStorageMezzFlashLifeVendor_Object = MibTableColumn
cfprStorageMezzFlashLifeVendor = _CfprStorageMezzFlashLifeVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 31, 1, 17),
    _CfprStorageMezzFlashLifeVendor_Type()
)
cfprStorageMezzFlashLifeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageMezzFlashLifeVendor.setStatus("current")
_CfprStorageNodeEpTable_Object = MibTable
cfprStorageNodeEpTable = _CfprStorageNodeEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 32)
)
if mibBuilder.loadTexts:
    cfprStorageNodeEpTable.setStatus("current")
_CfprStorageNodeEpEntry_Object = MibTableRow
cfprStorageNodeEpEntry = _CfprStorageNodeEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 32, 1)
)
cfprStorageNodeEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageNodeEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageNodeEpEntry.setStatus("current")
_CfprStorageNodeEpInstanceId_Type = CfprManagedObjectId
_CfprStorageNodeEpInstanceId_Object = MibTableColumn
cfprStorageNodeEpInstanceId = _CfprStorageNodeEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 32, 1, 1),
    _CfprStorageNodeEpInstanceId_Type()
)
cfprStorageNodeEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageNodeEpInstanceId.setStatus("current")
_CfprStorageNodeEpDn_Type = CfprManagedObjectDn
_CfprStorageNodeEpDn_Object = MibTableColumn
cfprStorageNodeEpDn = _CfprStorageNodeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 32, 1, 2),
    _CfprStorageNodeEpDn_Type()
)
cfprStorageNodeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageNodeEpDn.setStatus("current")
_CfprStorageNodeEpRn_Type = SnmpAdminString
_CfprStorageNodeEpRn_Object = MibTableColumn
cfprStorageNodeEpRn = _CfprStorageNodeEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 32, 1, 3),
    _CfprStorageNodeEpRn_Type()
)
cfprStorageNodeEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageNodeEpRn.setStatus("current")
_CfprStorageNodeEpEpDn_Type = SnmpAdminString
_CfprStorageNodeEpEpDn_Object = MibTableColumn
cfprStorageNodeEpEpDn = _CfprStorageNodeEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 32, 1, 4),
    _CfprStorageNodeEpEpDn_Type()
)
cfprStorageNodeEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageNodeEpEpDn.setStatus("current")
_CfprStorageNodeEpId_Type = Gauge32
_CfprStorageNodeEpId_Object = MibTableColumn
cfprStorageNodeEpId = _CfprStorageNodeEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 32, 1, 5),
    _CfprStorageNodeEpId_Type()
)
cfprStorageNodeEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageNodeEpId.setStatus("current")
_CfprStorageOperationTable_Object = MibTable
cfprStorageOperationTable = _CfprStorageOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 33)
)
if mibBuilder.loadTexts:
    cfprStorageOperationTable.setStatus("current")
_CfprStorageOperationEntry_Object = MibTableRow
cfprStorageOperationEntry = _CfprStorageOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 33, 1)
)
cfprStorageOperationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageOperationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageOperationEntry.setStatus("current")
_CfprStorageOperationInstanceId_Type = CfprManagedObjectId
_CfprStorageOperationInstanceId_Object = MibTableColumn
cfprStorageOperationInstanceId = _CfprStorageOperationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 33, 1, 1),
    _CfprStorageOperationInstanceId_Type()
)
cfprStorageOperationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageOperationInstanceId.setStatus("current")
_CfprStorageOperationDn_Type = CfprManagedObjectDn
_CfprStorageOperationDn_Object = MibTableColumn
cfprStorageOperationDn = _CfprStorageOperationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 33, 1, 2),
    _CfprStorageOperationDn_Type()
)
cfprStorageOperationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageOperationDn.setStatus("current")
_CfprStorageOperationRn_Type = SnmpAdminString
_CfprStorageOperationRn_Object = MibTableColumn
cfprStorageOperationRn = _CfprStorageOperationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 33, 1, 3),
    _CfprStorageOperationRn_Type()
)
cfprStorageOperationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageOperationRn.setStatus("current")
_CfprStorageOperationEndTime_Type = DateAndTime
_CfprStorageOperationEndTime_Object = MibTableColumn
cfprStorageOperationEndTime = _CfprStorageOperationEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 33, 1, 4),
    _CfprStorageOperationEndTime_Type()
)
cfprStorageOperationEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageOperationEndTime.setStatus("current")
_CfprStorageOperationName_Type = CfprStorageOperationType
_CfprStorageOperationName_Object = MibTableColumn
cfprStorageOperationName = _CfprStorageOperationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 33, 1, 5),
    _CfprStorageOperationName_Type()
)
cfprStorageOperationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageOperationName.setStatus("current")
_CfprStorageOperationOperState_Type = CfprStorageOperationState
_CfprStorageOperationOperState_Object = MibTableColumn
cfprStorageOperationOperState = _CfprStorageOperationOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 33, 1, 6),
    _CfprStorageOperationOperState_Type()
)
cfprStorageOperationOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageOperationOperState.setStatus("current")
_CfprStorageOperationProgress_Type = Gauge32
_CfprStorageOperationProgress_Object = MibTableColumn
cfprStorageOperationProgress = _CfprStorageOperationProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 33, 1, 7),
    _CfprStorageOperationProgress_Type()
)
cfprStorageOperationProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageOperationProgress.setStatus("current")
_CfprStorageOperationStartTime_Type = DateAndTime
_CfprStorageOperationStartTime_Object = MibTableColumn
cfprStorageOperationStartTime = _CfprStorageOperationStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 33, 1, 8),
    _CfprStorageOperationStartTime_Type()
)
cfprStorageOperationStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageOperationStartTime.setStatus("current")
_CfprStorageOperationStatusDescr_Type = SnmpAdminString
_CfprStorageOperationStatusDescr_Object = MibTableColumn
cfprStorageOperationStatusDescr = _CfprStorageOperationStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 33, 1, 9),
    _CfprStorageOperationStatusDescr_Type()
)
cfprStorageOperationStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageOperationStatusDescr.setStatus("current")
_CfprStorageQualTable_Object = MibTable
cfprStorageQualTable = _CfprStorageQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34)
)
if mibBuilder.loadTexts:
    cfprStorageQualTable.setStatus("current")
_CfprStorageQualEntry_Object = MibTableRow
cfprStorageQualEntry = _CfprStorageQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34, 1)
)
cfprStorageQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageQualEntry.setStatus("current")
_CfprStorageQualInstanceId_Type = CfprManagedObjectId
_CfprStorageQualInstanceId_Object = MibTableColumn
cfprStorageQualInstanceId = _CfprStorageQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34, 1, 1),
    _CfprStorageQualInstanceId_Type()
)
cfprStorageQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageQualInstanceId.setStatus("current")
_CfprStorageQualDn_Type = CfprManagedObjectDn
_CfprStorageQualDn_Object = MibTableColumn
cfprStorageQualDn = _CfprStorageQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34, 1, 2),
    _CfprStorageQualDn_Type()
)
cfprStorageQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageQualDn.setStatus("current")
_CfprStorageQualRn_Type = SnmpAdminString
_CfprStorageQualRn_Object = MibTableColumn
cfprStorageQualRn = _CfprStorageQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34, 1, 3),
    _CfprStorageQualRn_Type()
)
cfprStorageQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageQualRn.setStatus("current")
_CfprStorageQualBlockSize_Type = Gauge32
_CfprStorageQualBlockSize_Object = MibTableColumn
cfprStorageQualBlockSize = _CfprStorageQualBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34, 1, 4),
    _CfprStorageQualBlockSize_Type()
)
cfprStorageQualBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageQualBlockSize.setStatus("current")
_CfprStorageQualDiskless_Type = CfprStorageDisklessAction
_CfprStorageQualDiskless_Object = MibTableColumn
cfprStorageQualDiskless = _CfprStorageQualDiskless_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34, 1, 5),
    _CfprStorageQualDiskless_Type()
)
cfprStorageQualDiskless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageQualDiskless.setStatus("current")
_CfprStorageQualMaxCap_Type = Unsigned64
_CfprStorageQualMaxCap_Object = MibTableColumn
cfprStorageQualMaxCap = _CfprStorageQualMaxCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34, 1, 6),
    _CfprStorageQualMaxCap_Type()
)
cfprStorageQualMaxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageQualMaxCap.setStatus("current")
_CfprStorageQualMinCap_Type = Unsigned64
_CfprStorageQualMinCap_Object = MibTableColumn
cfprStorageQualMinCap = _CfprStorageQualMinCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34, 1, 7),
    _CfprStorageQualMinCap_Type()
)
cfprStorageQualMinCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageQualMinCap.setStatus("current")
_CfprStorageQualNumberOfBlocks_Type = Unsigned64
_CfprStorageQualNumberOfBlocks_Object = MibTableColumn
cfprStorageQualNumberOfBlocks = _CfprStorageQualNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34, 1, 8),
    _CfprStorageQualNumberOfBlocks_Type()
)
cfprStorageQualNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageQualNumberOfBlocks.setStatus("current")
_CfprStorageQualNumberOfFlexFlashCards_Type = Integer32
_CfprStorageQualNumberOfFlexFlashCards_Object = MibTableColumn
cfprStorageQualNumberOfFlexFlashCards = _CfprStorageQualNumberOfFlexFlashCards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34, 1, 9),
    _CfprStorageQualNumberOfFlexFlashCards_Type()
)
cfprStorageQualNumberOfFlexFlashCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageQualNumberOfFlexFlashCards.setStatus("current")
_CfprStorageQualPerDiskCap_Type = Unsigned64
_CfprStorageQualPerDiskCap_Object = MibTableColumn
cfprStorageQualPerDiskCap = _CfprStorageQualPerDiskCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34, 1, 10),
    _CfprStorageQualPerDiskCap_Type()
)
cfprStorageQualPerDiskCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageQualPerDiskCap.setStatus("current")
_CfprStorageQualUnits_Type = Gauge32
_CfprStorageQualUnits_Object = MibTableColumn
cfprStorageQualUnits = _CfprStorageQualUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 34, 1, 11),
    _CfprStorageQualUnits_Type()
)
cfprStorageQualUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageQualUnits.setStatus("current")
_CfprStorageRaidBatteryTable_Object = MibTable
cfprStorageRaidBatteryTable = _CfprStorageRaidBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35)
)
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryTable.setStatus("current")
_CfprStorageRaidBatteryEntry_Object = MibTableRow
cfprStorageRaidBatteryEntry = _CfprStorageRaidBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1)
)
cfprStorageRaidBatteryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageRaidBatteryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryEntry.setStatus("current")
_CfprStorageRaidBatteryInstanceId_Type = CfprManagedObjectId
_CfprStorageRaidBatteryInstanceId_Object = MibTableColumn
cfprStorageRaidBatteryInstanceId = _CfprStorageRaidBatteryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 1),
    _CfprStorageRaidBatteryInstanceId_Type()
)
cfprStorageRaidBatteryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryInstanceId.setStatus("current")
_CfprStorageRaidBatteryDn_Type = CfprManagedObjectDn
_CfprStorageRaidBatteryDn_Object = MibTableColumn
cfprStorageRaidBatteryDn = _CfprStorageRaidBatteryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 2),
    _CfprStorageRaidBatteryDn_Type()
)
cfprStorageRaidBatteryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryDn.setStatus("current")
_CfprStorageRaidBatteryRn_Type = SnmpAdminString
_CfprStorageRaidBatteryRn_Object = MibTableColumn
cfprStorageRaidBatteryRn = _CfprStorageRaidBatteryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 3),
    _CfprStorageRaidBatteryRn_Type()
)
cfprStorageRaidBatteryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryRn.setStatus("current")
_CfprStorageRaidBatteryBatteryType_Type = CfprStorageBatteryType
_CfprStorageRaidBatteryBatteryType_Object = MibTableColumn
cfprStorageRaidBatteryBatteryType = _CfprStorageRaidBatteryBatteryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 4),
    _CfprStorageRaidBatteryBatteryType_Type()
)
cfprStorageRaidBatteryBatteryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryBatteryType.setStatus("current")
_CfprStorageRaidBatteryBbuStatus_Type = CfprStorageBbuStatus
_CfprStorageRaidBatteryBbuStatus_Object = MibTableColumn
cfprStorageRaidBatteryBbuStatus = _CfprStorageRaidBatteryBbuStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 5),
    _CfprStorageRaidBatteryBbuStatus_Type()
)
cfprStorageRaidBatteryBbuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryBbuStatus.setStatus("current")
_CfprStorageRaidBatteryBlockSize_Type = Gauge32
_CfprStorageRaidBatteryBlockSize_Object = MibTableColumn
cfprStorageRaidBatteryBlockSize = _CfprStorageRaidBatteryBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 6),
    _CfprStorageRaidBatteryBlockSize_Type()
)
cfprStorageRaidBatteryBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryBlockSize.setStatus("current")
_CfprStorageRaidBatteryCapacityPercentage_Type = Gauge32
_CfprStorageRaidBatteryCapacityPercentage_Object = MibTableColumn
cfprStorageRaidBatteryCapacityPercentage = _CfprStorageRaidBatteryCapacityPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 7),
    _CfprStorageRaidBatteryCapacityPercentage_Type()
)
cfprStorageRaidBatteryCapacityPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryCapacityPercentage.setStatus("current")
_CfprStorageRaidBatteryConnectionProtocol_Type = CfprStorageConnectionProtocol
_CfprStorageRaidBatteryConnectionProtocol_Object = MibTableColumn
cfprStorageRaidBatteryConnectionProtocol = _CfprStorageRaidBatteryConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 8),
    _CfprStorageRaidBatteryConnectionProtocol_Type()
)
cfprStorageRaidBatteryConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryConnectionProtocol.setStatus("current")
_CfprStorageRaidBatteryId_Type = Gauge32
_CfprStorageRaidBatteryId_Object = MibTableColumn
cfprStorageRaidBatteryId = _CfprStorageRaidBatteryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 9),
    _CfprStorageRaidBatteryId_Type()
)
cfprStorageRaidBatteryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryId.setStatus("current")
_CfprStorageRaidBatteryLc_Type = CfprFsmLifecycle
_CfprStorageRaidBatteryLc_Object = MibTableColumn
cfprStorageRaidBatteryLc = _CfprStorageRaidBatteryLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 10),
    _CfprStorageRaidBatteryLc_Type()
)
cfprStorageRaidBatteryLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryLc.setStatus("current")
_CfprStorageRaidBatteryLearnCycleRequested_Type = CfprStorageLearnCycleRequested
_CfprStorageRaidBatteryLearnCycleRequested_Object = MibTableColumn
cfprStorageRaidBatteryLearnCycleRequested = _CfprStorageRaidBatteryLearnCycleRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 11),
    _CfprStorageRaidBatteryLearnCycleRequested_Type()
)
cfprStorageRaidBatteryLearnCycleRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryLearnCycleRequested.setStatus("current")
_CfprStorageRaidBatteryLearnMode_Type = CfprStorageLearnMode
_CfprStorageRaidBatteryLearnMode_Object = MibTableColumn
cfprStorageRaidBatteryLearnMode = _CfprStorageRaidBatteryLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 12),
    _CfprStorageRaidBatteryLearnMode_Type()
)
cfprStorageRaidBatteryLearnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryLearnMode.setStatus("current")
_CfprStorageRaidBatteryModel_Type = SnmpAdminString
_CfprStorageRaidBatteryModel_Object = MibTableColumn
cfprStorageRaidBatteryModel = _CfprStorageRaidBatteryModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 13),
    _CfprStorageRaidBatteryModel_Type()
)
cfprStorageRaidBatteryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryModel.setStatus("current")
_CfprStorageRaidBatteryNextLearnCycleTs_Type = DateAndTime
_CfprStorageRaidBatteryNextLearnCycleTs_Object = MibTableColumn
cfprStorageRaidBatteryNextLearnCycleTs = _CfprStorageRaidBatteryNextLearnCycleTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 14),
    _CfprStorageRaidBatteryNextLearnCycleTs_Type()
)
cfprStorageRaidBatteryNextLearnCycleTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryNextLearnCycleTs.setStatus("current")
_CfprStorageRaidBatteryNumberOfBlocks_Type = Unsigned64
_CfprStorageRaidBatteryNumberOfBlocks_Object = MibTableColumn
cfprStorageRaidBatteryNumberOfBlocks = _CfprStorageRaidBatteryNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 15),
    _CfprStorageRaidBatteryNumberOfBlocks_Type()
)
cfprStorageRaidBatteryNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryNumberOfBlocks.setStatus("current")
_CfprStorageRaidBatteryOperQualifierReason_Type = SnmpAdminString
_CfprStorageRaidBatteryOperQualifierReason_Object = MibTableColumn
cfprStorageRaidBatteryOperQualifierReason = _CfprStorageRaidBatteryOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 16),
    _CfprStorageRaidBatteryOperQualifierReason_Type()
)
cfprStorageRaidBatteryOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryOperQualifierReason.setStatus("current")
_CfprStorageRaidBatteryOperability_Type = CfprEquipmentOperability
_CfprStorageRaidBatteryOperability_Object = MibTableColumn
cfprStorageRaidBatteryOperability = _CfprStorageRaidBatteryOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 17),
    _CfprStorageRaidBatteryOperability_Type()
)
cfprStorageRaidBatteryOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryOperability.setStatus("current")
_CfprStorageRaidBatteryOperabilityQualifier_Type = CfprStorageRaidBatteryOperabilityQualifier
_CfprStorageRaidBatteryOperabilityQualifier_Object = MibTableColumn
cfprStorageRaidBatteryOperabilityQualifier = _CfprStorageRaidBatteryOperabilityQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 18),
    _CfprStorageRaidBatteryOperabilityQualifier_Type()
)
cfprStorageRaidBatteryOperabilityQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryOperabilityQualifier.setStatus("current")
_CfprStorageRaidBatteryOperabilityQualifierReason_Type = SnmpAdminString
_CfprStorageRaidBatteryOperabilityQualifierReason_Object = MibTableColumn
cfprStorageRaidBatteryOperabilityQualifierReason = _CfprStorageRaidBatteryOperabilityQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 19),
    _CfprStorageRaidBatteryOperabilityQualifierReason_Type()
)
cfprStorageRaidBatteryOperabilityQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryOperabilityQualifierReason.setStatus("current")
_CfprStorageRaidBatteryPresence_Type = CfprEquipmentPresence
_CfprStorageRaidBatteryPresence_Object = MibTableColumn
cfprStorageRaidBatteryPresence = _CfprStorageRaidBatteryPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 20),
    _CfprStorageRaidBatteryPresence_Type()
)
cfprStorageRaidBatteryPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryPresence.setStatus("current")
_CfprStorageRaidBatteryRevision_Type = SnmpAdminString
_CfprStorageRaidBatteryRevision_Object = MibTableColumn
cfprStorageRaidBatteryRevision = _CfprStorageRaidBatteryRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 21),
    _CfprStorageRaidBatteryRevision_Type()
)
cfprStorageRaidBatteryRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryRevision.setStatus("current")
_CfprStorageRaidBatterySerial_Type = SnmpAdminString
_CfprStorageRaidBatterySerial_Object = MibTableColumn
cfprStorageRaidBatterySerial = _CfprStorageRaidBatterySerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 22),
    _CfprStorageRaidBatterySerial_Type()
)
cfprStorageRaidBatterySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatterySerial.setStatus("current")
_CfprStorageRaidBatterySize_Type = Unsigned64
_CfprStorageRaidBatterySize_Object = MibTableColumn
cfprStorageRaidBatterySize = _CfprStorageRaidBatterySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 23),
    _CfprStorageRaidBatterySize_Type()
)
cfprStorageRaidBatterySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatterySize.setStatus("current")
_CfprStorageRaidBatteryTemperature_Type = Integer32
_CfprStorageRaidBatteryTemperature_Object = MibTableColumn
cfprStorageRaidBatteryTemperature = _CfprStorageRaidBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 24),
    _CfprStorageRaidBatteryTemperature_Type()
)
cfprStorageRaidBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryTemperature.setStatus("current")
_CfprStorageRaidBatteryVendor_Type = SnmpAdminString
_CfprStorageRaidBatteryVendor_Object = MibTableColumn
cfprStorageRaidBatteryVendor = _CfprStorageRaidBatteryVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 35, 1, 25),
    _CfprStorageRaidBatteryVendor_Type()
)
cfprStorageRaidBatteryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageRaidBatteryVendor.setStatus("current")
_CfprStorageSystemTable_Object = MibTable
cfprStorageSystemTable = _CfprStorageSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36)
)
if mibBuilder.loadTexts:
    cfprStorageSystemTable.setStatus("current")
_CfprStorageSystemEntry_Object = MibTableRow
cfprStorageSystemEntry = _CfprStorageSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1)
)
cfprStorageSystemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageSystemEntry.setStatus("current")
_CfprStorageSystemInstanceId_Type = CfprManagedObjectId
_CfprStorageSystemInstanceId_Object = MibTableColumn
cfprStorageSystemInstanceId = _CfprStorageSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 1),
    _CfprStorageSystemInstanceId_Type()
)
cfprStorageSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageSystemInstanceId.setStatus("current")
_CfprStorageSystemDn_Type = CfprManagedObjectDn
_CfprStorageSystemDn_Object = MibTableColumn
cfprStorageSystemDn = _CfprStorageSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 2),
    _CfprStorageSystemDn_Type()
)
cfprStorageSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemDn.setStatus("current")
_CfprStorageSystemRn_Type = SnmpAdminString
_CfprStorageSystemRn_Object = MibTableColumn
cfprStorageSystemRn = _CfprStorageSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 3),
    _CfprStorageSystemRn_Type()
)
cfprStorageSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemRn.setStatus("current")
_CfprStorageSystemFsmDescr_Type = SnmpAdminString
_CfprStorageSystemFsmDescr_Object = MibTableColumn
cfprStorageSystemFsmDescr = _CfprStorageSystemFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 4),
    _CfprStorageSystemFsmDescr_Type()
)
cfprStorageSystemFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmDescr.setStatus("current")
_CfprStorageSystemFsmPrev_Type = SnmpAdminString
_CfprStorageSystemFsmPrev_Object = MibTableColumn
cfprStorageSystemFsmPrev = _CfprStorageSystemFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 5),
    _CfprStorageSystemFsmPrev_Type()
)
cfprStorageSystemFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmPrev.setStatus("current")
_CfprStorageSystemFsmProgr_Type = Gauge32
_CfprStorageSystemFsmProgr_Object = MibTableColumn
cfprStorageSystemFsmProgr = _CfprStorageSystemFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 6),
    _CfprStorageSystemFsmProgr_Type()
)
cfprStorageSystemFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmProgr.setStatus("current")
_CfprStorageSystemFsmRmtInvErrCode_Type = Gauge32
_CfprStorageSystemFsmRmtInvErrCode_Object = MibTableColumn
cfprStorageSystemFsmRmtInvErrCode = _CfprStorageSystemFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 7),
    _CfprStorageSystemFsmRmtInvErrCode_Type()
)
cfprStorageSystemFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmRmtInvErrCode.setStatus("current")
_CfprStorageSystemFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprStorageSystemFsmRmtInvErrDescr_Object = MibTableColumn
cfprStorageSystemFsmRmtInvErrDescr = _CfprStorageSystemFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 8),
    _CfprStorageSystemFsmRmtInvErrDescr_Type()
)
cfprStorageSystemFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmRmtInvErrDescr.setStatus("current")
_CfprStorageSystemFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprStorageSystemFsmRmtInvRslt_Object = MibTableColumn
cfprStorageSystemFsmRmtInvRslt = _CfprStorageSystemFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 9),
    _CfprStorageSystemFsmRmtInvRslt_Type()
)
cfprStorageSystemFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmRmtInvRslt.setStatus("current")
_CfprStorageSystemFsmStageDescr_Type = SnmpAdminString
_CfprStorageSystemFsmStageDescr_Object = MibTableColumn
cfprStorageSystemFsmStageDescr = _CfprStorageSystemFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 10),
    _CfprStorageSystemFsmStageDescr_Type()
)
cfprStorageSystemFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStageDescr.setStatus("current")
_CfprStorageSystemFsmStamp_Type = DateAndTime
_CfprStorageSystemFsmStamp_Object = MibTableColumn
cfprStorageSystemFsmStamp = _CfprStorageSystemFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 11),
    _CfprStorageSystemFsmStamp_Type()
)
cfprStorageSystemFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStamp.setStatus("current")
_CfprStorageSystemFsmStatus_Type = SnmpAdminString
_CfprStorageSystemFsmStatus_Object = MibTableColumn
cfprStorageSystemFsmStatus = _CfprStorageSystemFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 12),
    _CfprStorageSystemFsmStatus_Type()
)
cfprStorageSystemFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStatus.setStatus("current")
_CfprStorageSystemFsmTry_Type = Gauge32
_CfprStorageSystemFsmTry_Object = MibTableColumn
cfprStorageSystemFsmTry = _CfprStorageSystemFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 13),
    _CfprStorageSystemFsmTry_Type()
)
cfprStorageSystemFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmTry.setStatus("current")
_CfprStorageSystemId_Type = SnmpAdminString
_CfprStorageSystemId_Object = MibTableColumn
cfprStorageSystemId = _CfprStorageSystemId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 14),
    _CfprStorageSystemId_Type()
)
cfprStorageSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemId.setStatus("current")
_CfprStorageSystemName_Type = SnmpAdminString
_CfprStorageSystemName_Object = MibTableColumn
cfprStorageSystemName = _CfprStorageSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 36, 1, 15),
    _CfprStorageSystemName_Type()
)
cfprStorageSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemName.setStatus("current")
_CfprStorageSystemFsmTable_Object = MibTable
cfprStorageSystemFsmTable = _CfprStorageSystemFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37)
)
if mibBuilder.loadTexts:
    cfprStorageSystemFsmTable.setStatus("current")
_CfprStorageSystemFsmEntry_Object = MibTableRow
cfprStorageSystemFsmEntry = _CfprStorageSystemFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37, 1)
)
cfprStorageSystemFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageSystemFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageSystemFsmEntry.setStatus("current")
_CfprStorageSystemFsmInstanceId_Type = CfprManagedObjectId
_CfprStorageSystemFsmInstanceId_Object = MibTableColumn
cfprStorageSystemFsmInstanceId = _CfprStorageSystemFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37, 1, 1),
    _CfprStorageSystemFsmInstanceId_Type()
)
cfprStorageSystemFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmInstanceId.setStatus("current")
_CfprStorageSystemFsmDn_Type = CfprManagedObjectDn
_CfprStorageSystemFsmDn_Object = MibTableColumn
cfprStorageSystemFsmDn = _CfprStorageSystemFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37, 1, 2),
    _CfprStorageSystemFsmDn_Type()
)
cfprStorageSystemFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmDn.setStatus("current")
_CfprStorageSystemFsmRn_Type = SnmpAdminString
_CfprStorageSystemFsmRn_Object = MibTableColumn
cfprStorageSystemFsmRn = _CfprStorageSystemFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37, 1, 3),
    _CfprStorageSystemFsmRn_Type()
)
cfprStorageSystemFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmRn.setStatus("current")
_CfprStorageSystemFsmCompletionTime_Type = DateAndTime
_CfprStorageSystemFsmCompletionTime_Object = MibTableColumn
cfprStorageSystemFsmCompletionTime = _CfprStorageSystemFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37, 1, 4),
    _CfprStorageSystemFsmCompletionTime_Type()
)
cfprStorageSystemFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmCompletionTime.setStatus("current")
_CfprStorageSystemFsmCurrentFsm_Type = CfprStorageSystemFsmCurrentFsm
_CfprStorageSystemFsmCurrentFsm_Object = MibTableColumn
cfprStorageSystemFsmCurrentFsm = _CfprStorageSystemFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37, 1, 5),
    _CfprStorageSystemFsmCurrentFsm_Type()
)
cfprStorageSystemFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmCurrentFsm.setStatus("current")
_CfprStorageSystemFsmDescrData_Type = SnmpAdminString
_CfprStorageSystemFsmDescrData_Object = MibTableColumn
cfprStorageSystemFsmDescrData = _CfprStorageSystemFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37, 1, 6),
    _CfprStorageSystemFsmDescrData_Type()
)
cfprStorageSystemFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmDescrData.setStatus("current")
_CfprStorageSystemFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprStorageSystemFsmFsmStatus_Object = MibTableColumn
cfprStorageSystemFsmFsmStatus = _CfprStorageSystemFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37, 1, 7),
    _CfprStorageSystemFsmFsmStatus_Type()
)
cfprStorageSystemFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmFsmStatus.setStatus("current")
_CfprStorageSystemFsmProgress_Type = Gauge32
_CfprStorageSystemFsmProgress_Object = MibTableColumn
cfprStorageSystemFsmProgress = _CfprStorageSystemFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37, 1, 8),
    _CfprStorageSystemFsmProgress_Type()
)
cfprStorageSystemFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmProgress.setStatus("current")
_CfprStorageSystemFsmRmtErrCode_Type = Gauge32
_CfprStorageSystemFsmRmtErrCode_Object = MibTableColumn
cfprStorageSystemFsmRmtErrCode = _CfprStorageSystemFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37, 1, 9),
    _CfprStorageSystemFsmRmtErrCode_Type()
)
cfprStorageSystemFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmRmtErrCode.setStatus("current")
_CfprStorageSystemFsmRmtErrDescr_Type = SnmpAdminString
_CfprStorageSystemFsmRmtErrDescr_Object = MibTableColumn
cfprStorageSystemFsmRmtErrDescr = _CfprStorageSystemFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37, 1, 10),
    _CfprStorageSystemFsmRmtErrDescr_Type()
)
cfprStorageSystemFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmRmtErrDescr.setStatus("current")
_CfprStorageSystemFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprStorageSystemFsmRmtRslt_Object = MibTableColumn
cfprStorageSystemFsmRmtRslt = _CfprStorageSystemFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 37, 1, 11),
    _CfprStorageSystemFsmRmtRslt_Type()
)
cfprStorageSystemFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmRmtRslt.setStatus("current")
_CfprStorageSystemFsmStageTable_Object = MibTable
cfprStorageSystemFsmStageTable = _CfprStorageSystemFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 38)
)
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStageTable.setStatus("current")
_CfprStorageSystemFsmStageEntry_Object = MibTableRow
cfprStorageSystemFsmStageEntry = _CfprStorageSystemFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 38, 1)
)
cfprStorageSystemFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageSystemFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStageEntry.setStatus("current")
_CfprStorageSystemFsmStageInstanceId_Type = CfprManagedObjectId
_CfprStorageSystemFsmStageInstanceId_Object = MibTableColumn
cfprStorageSystemFsmStageInstanceId = _CfprStorageSystemFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 38, 1, 1),
    _CfprStorageSystemFsmStageInstanceId_Type()
)
cfprStorageSystemFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStageInstanceId.setStatus("current")
_CfprStorageSystemFsmStageDn_Type = CfprManagedObjectDn
_CfprStorageSystemFsmStageDn_Object = MibTableColumn
cfprStorageSystemFsmStageDn = _CfprStorageSystemFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 38, 1, 2),
    _CfprStorageSystemFsmStageDn_Type()
)
cfprStorageSystemFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStageDn.setStatus("current")
_CfprStorageSystemFsmStageRn_Type = SnmpAdminString
_CfprStorageSystemFsmStageRn_Object = MibTableColumn
cfprStorageSystemFsmStageRn = _CfprStorageSystemFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 38, 1, 3),
    _CfprStorageSystemFsmStageRn_Type()
)
cfprStorageSystemFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStageRn.setStatus("current")
_CfprStorageSystemFsmStageDescrData_Type = SnmpAdminString
_CfprStorageSystemFsmStageDescrData_Object = MibTableColumn
cfprStorageSystemFsmStageDescrData = _CfprStorageSystemFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 38, 1, 4),
    _CfprStorageSystemFsmStageDescrData_Type()
)
cfprStorageSystemFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStageDescrData.setStatus("current")
_CfprStorageSystemFsmStageLastUpdateTime_Type = DateAndTime
_CfprStorageSystemFsmStageLastUpdateTime_Object = MibTableColumn
cfprStorageSystemFsmStageLastUpdateTime = _CfprStorageSystemFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 38, 1, 5),
    _CfprStorageSystemFsmStageLastUpdateTime_Type()
)
cfprStorageSystemFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStageLastUpdateTime.setStatus("current")
_CfprStorageSystemFsmStageName_Type = CfprStorageSystemFsmStageName
_CfprStorageSystemFsmStageName_Object = MibTableColumn
cfprStorageSystemFsmStageName = _CfprStorageSystemFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 38, 1, 6),
    _CfprStorageSystemFsmStageName_Type()
)
cfprStorageSystemFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStageName.setStatus("current")
_CfprStorageSystemFsmStageOrder_Type = Gauge32
_CfprStorageSystemFsmStageOrder_Object = MibTableColumn
cfprStorageSystemFsmStageOrder = _CfprStorageSystemFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 38, 1, 7),
    _CfprStorageSystemFsmStageOrder_Type()
)
cfprStorageSystemFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStageOrder.setStatus("current")
_CfprStorageSystemFsmStageRetry_Type = Gauge32
_CfprStorageSystemFsmStageRetry_Object = MibTableColumn
cfprStorageSystemFsmStageRetry = _CfprStorageSystemFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 38, 1, 8),
    _CfprStorageSystemFsmStageRetry_Type()
)
cfprStorageSystemFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStageRetry.setStatus("current")
_CfprStorageSystemFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprStorageSystemFsmStageStageStatus_Object = MibTableColumn
cfprStorageSystemFsmStageStageStatus = _CfprStorageSystemFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 38, 1, 9),
    _CfprStorageSystemFsmStageStageStatus_Type()
)
cfprStorageSystemFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmStageStageStatus.setStatus("current")
_CfprStorageSystemFsmTaskTable_Object = MibTable
cfprStorageSystemFsmTaskTable = _CfprStorageSystemFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 39)
)
if mibBuilder.loadTexts:
    cfprStorageSystemFsmTaskTable.setStatus("current")
_CfprStorageSystemFsmTaskEntry_Object = MibTableRow
cfprStorageSystemFsmTaskEntry = _CfprStorageSystemFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 39, 1)
)
cfprStorageSystemFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageSystemFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageSystemFsmTaskEntry.setStatus("current")
_CfprStorageSystemFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprStorageSystemFsmTaskInstanceId_Object = MibTableColumn
cfprStorageSystemFsmTaskInstanceId = _CfprStorageSystemFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 39, 1, 1),
    _CfprStorageSystemFsmTaskInstanceId_Type()
)
cfprStorageSystemFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmTaskInstanceId.setStatus("current")
_CfprStorageSystemFsmTaskDn_Type = CfprManagedObjectDn
_CfprStorageSystemFsmTaskDn_Object = MibTableColumn
cfprStorageSystemFsmTaskDn = _CfprStorageSystemFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 39, 1, 2),
    _CfprStorageSystemFsmTaskDn_Type()
)
cfprStorageSystemFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmTaskDn.setStatus("current")
_CfprStorageSystemFsmTaskRn_Type = SnmpAdminString
_CfprStorageSystemFsmTaskRn_Object = MibTableColumn
cfprStorageSystemFsmTaskRn = _CfprStorageSystemFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 39, 1, 3),
    _CfprStorageSystemFsmTaskRn_Type()
)
cfprStorageSystemFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmTaskRn.setStatus("current")
_CfprStorageSystemFsmTaskCompletion_Type = CfprFsmCompletion
_CfprStorageSystemFsmTaskCompletion_Object = MibTableColumn
cfprStorageSystemFsmTaskCompletion = _CfprStorageSystemFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 39, 1, 4),
    _CfprStorageSystemFsmTaskCompletion_Type()
)
cfprStorageSystemFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmTaskCompletion.setStatus("current")
_CfprStorageSystemFsmTaskFlags_Type = CfprFsmFlags
_CfprStorageSystemFsmTaskFlags_Object = MibTableColumn
cfprStorageSystemFsmTaskFlags = _CfprStorageSystemFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 39, 1, 5),
    _CfprStorageSystemFsmTaskFlags_Type()
)
cfprStorageSystemFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmTaskFlags.setStatus("current")
_CfprStorageSystemFsmTaskItem_Type = CfprStorageSystemFsmTaskItem
_CfprStorageSystemFsmTaskItem_Object = MibTableColumn
cfprStorageSystemFsmTaskItem = _CfprStorageSystemFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 39, 1, 6),
    _CfprStorageSystemFsmTaskItem_Type()
)
cfprStorageSystemFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmTaskItem.setStatus("current")
_CfprStorageSystemFsmTaskSeqId_Type = Gauge32
_CfprStorageSystemFsmTaskSeqId_Object = MibTableColumn
cfprStorageSystemFsmTaskSeqId = _CfprStorageSystemFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 39, 1, 7),
    _CfprStorageSystemFsmTaskSeqId_Type()
)
cfprStorageSystemFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageSystemFsmTaskSeqId.setStatus("current")
_CfprStorageTransportableFlashModuleTable_Object = MibTable
cfprStorageTransportableFlashModuleTable = _CfprStorageTransportableFlashModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40)
)
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleTable.setStatus("current")
_CfprStorageTransportableFlashModuleEntry_Object = MibTableRow
cfprStorageTransportableFlashModuleEntry = _CfprStorageTransportableFlashModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1)
)
cfprStorageTransportableFlashModuleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageTransportableFlashModuleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleEntry.setStatus("current")
_CfprStorageTransportableFlashModuleInstanceId_Type = CfprManagedObjectId
_CfprStorageTransportableFlashModuleInstanceId_Object = MibTableColumn
cfprStorageTransportableFlashModuleInstanceId = _CfprStorageTransportableFlashModuleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 1),
    _CfprStorageTransportableFlashModuleInstanceId_Type()
)
cfprStorageTransportableFlashModuleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleInstanceId.setStatus("current")
_CfprStorageTransportableFlashModuleDn_Type = CfprManagedObjectDn
_CfprStorageTransportableFlashModuleDn_Object = MibTableColumn
cfprStorageTransportableFlashModuleDn = _CfprStorageTransportableFlashModuleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 2),
    _CfprStorageTransportableFlashModuleDn_Type()
)
cfprStorageTransportableFlashModuleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleDn.setStatus("current")
_CfprStorageTransportableFlashModuleRn_Type = SnmpAdminString
_CfprStorageTransportableFlashModuleRn_Object = MibTableColumn
cfprStorageTransportableFlashModuleRn = _CfprStorageTransportableFlashModuleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 3),
    _CfprStorageTransportableFlashModuleRn_Type()
)
cfprStorageTransportableFlashModuleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleRn.setStatus("current")
_CfprStorageTransportableFlashModuleBlockSize_Type = Gauge32
_CfprStorageTransportableFlashModuleBlockSize_Object = MibTableColumn
cfprStorageTransportableFlashModuleBlockSize = _CfprStorageTransportableFlashModuleBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 4),
    _CfprStorageTransportableFlashModuleBlockSize_Type()
)
cfprStorageTransportableFlashModuleBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleBlockSize.setStatus("current")
_CfprStorageTransportableFlashModuleConnectionProtocol_Type = CfprStorageConnectionProtocol
_CfprStorageTransportableFlashModuleConnectionProtocol_Object = MibTableColumn
cfprStorageTransportableFlashModuleConnectionProtocol = _CfprStorageTransportableFlashModuleConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 5),
    _CfprStorageTransportableFlashModuleConnectionProtocol_Type()
)
cfprStorageTransportableFlashModuleConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleConnectionProtocol.setStatus("current")
_CfprStorageTransportableFlashModuleId_Type = Gauge32
_CfprStorageTransportableFlashModuleId_Object = MibTableColumn
cfprStorageTransportableFlashModuleId = _CfprStorageTransportableFlashModuleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 6),
    _CfprStorageTransportableFlashModuleId_Type()
)
cfprStorageTransportableFlashModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleId.setStatus("current")
_CfprStorageTransportableFlashModuleModel_Type = SnmpAdminString
_CfprStorageTransportableFlashModuleModel_Object = MibTableColumn
cfprStorageTransportableFlashModuleModel = _CfprStorageTransportableFlashModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 7),
    _CfprStorageTransportableFlashModuleModel_Type()
)
cfprStorageTransportableFlashModuleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleModel.setStatus("current")
_CfprStorageTransportableFlashModuleNumberOfBlocks_Type = Unsigned64
_CfprStorageTransportableFlashModuleNumberOfBlocks_Object = MibTableColumn
cfprStorageTransportableFlashModuleNumberOfBlocks = _CfprStorageTransportableFlashModuleNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 8),
    _CfprStorageTransportableFlashModuleNumberOfBlocks_Type()
)
cfprStorageTransportableFlashModuleNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleNumberOfBlocks.setStatus("current")
_CfprStorageTransportableFlashModuleOperQualifierReason_Type = SnmpAdminString
_CfprStorageTransportableFlashModuleOperQualifierReason_Object = MibTableColumn
cfprStorageTransportableFlashModuleOperQualifierReason = _CfprStorageTransportableFlashModuleOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 9),
    _CfprStorageTransportableFlashModuleOperQualifierReason_Type()
)
cfprStorageTransportableFlashModuleOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleOperQualifierReason.setStatus("current")
_CfprStorageTransportableFlashModuleOperability_Type = CfprEquipmentOperability
_CfprStorageTransportableFlashModuleOperability_Object = MibTableColumn
cfprStorageTransportableFlashModuleOperability = _CfprStorageTransportableFlashModuleOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 10),
    _CfprStorageTransportableFlashModuleOperability_Type()
)
cfprStorageTransportableFlashModuleOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleOperability.setStatus("current")
_CfprStorageTransportableFlashModulePresence_Type = CfprEquipmentPresence
_CfprStorageTransportableFlashModulePresence_Object = MibTableColumn
cfprStorageTransportableFlashModulePresence = _CfprStorageTransportableFlashModulePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 11),
    _CfprStorageTransportableFlashModulePresence_Type()
)
cfprStorageTransportableFlashModulePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModulePresence.setStatus("current")
_CfprStorageTransportableFlashModuleRevision_Type = SnmpAdminString
_CfprStorageTransportableFlashModuleRevision_Object = MibTableColumn
cfprStorageTransportableFlashModuleRevision = _CfprStorageTransportableFlashModuleRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 12),
    _CfprStorageTransportableFlashModuleRevision_Type()
)
cfprStorageTransportableFlashModuleRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleRevision.setStatus("current")
_CfprStorageTransportableFlashModuleSerial_Type = SnmpAdminString
_CfprStorageTransportableFlashModuleSerial_Object = MibTableColumn
cfprStorageTransportableFlashModuleSerial = _CfprStorageTransportableFlashModuleSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 13),
    _CfprStorageTransportableFlashModuleSerial_Type()
)
cfprStorageTransportableFlashModuleSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleSerial.setStatus("current")
_CfprStorageTransportableFlashModuleSize_Type = Unsigned64
_CfprStorageTransportableFlashModuleSize_Object = MibTableColumn
cfprStorageTransportableFlashModuleSize = _CfprStorageTransportableFlashModuleSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 14),
    _CfprStorageTransportableFlashModuleSize_Type()
)
cfprStorageTransportableFlashModuleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleSize.setStatus("current")
_CfprStorageTransportableFlashModuleVendor_Type = SnmpAdminString
_CfprStorageTransportableFlashModuleVendor_Object = MibTableColumn
cfprStorageTransportableFlashModuleVendor = _CfprStorageTransportableFlashModuleVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 40, 1, 15),
    _CfprStorageTransportableFlashModuleVendor_Type()
)
cfprStorageTransportableFlashModuleVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageTransportableFlashModuleVendor.setStatus("current")
_CfprStorageVirtualDriveTable_Object = MibTable
cfprStorageVirtualDriveTable = _CfprStorageVirtualDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41)
)
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveTable.setStatus("current")
_CfprStorageVirtualDriveEntry_Object = MibTableRow
cfprStorageVirtualDriveEntry = _CfprStorageVirtualDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1)
)
cfprStorageVirtualDriveEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageVirtualDriveInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveEntry.setStatus("current")
_CfprStorageVirtualDriveInstanceId_Type = CfprManagedObjectId
_CfprStorageVirtualDriveInstanceId_Object = MibTableColumn
cfprStorageVirtualDriveInstanceId = _CfprStorageVirtualDriveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 1),
    _CfprStorageVirtualDriveInstanceId_Type()
)
cfprStorageVirtualDriveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveInstanceId.setStatus("current")
_CfprStorageVirtualDriveDn_Type = CfprManagedObjectDn
_CfprStorageVirtualDriveDn_Object = MibTableColumn
cfprStorageVirtualDriveDn = _CfprStorageVirtualDriveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 2),
    _CfprStorageVirtualDriveDn_Type()
)
cfprStorageVirtualDriveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveDn.setStatus("current")
_CfprStorageVirtualDriveRn_Type = SnmpAdminString
_CfprStorageVirtualDriveRn_Object = MibTableColumn
cfprStorageVirtualDriveRn = _CfprStorageVirtualDriveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 3),
    _CfprStorageVirtualDriveRn_Type()
)
cfprStorageVirtualDriveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveRn.setStatus("current")
_CfprStorageVirtualDriveAccessPolicy_Type = CfprStorageAccessType
_CfprStorageVirtualDriveAccessPolicy_Object = MibTableColumn
cfprStorageVirtualDriveAccessPolicy = _CfprStorageVirtualDriveAccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 4),
    _CfprStorageVirtualDriveAccessPolicy_Type()
)
cfprStorageVirtualDriveAccessPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveAccessPolicy.setStatus("current")
_CfprStorageVirtualDriveActualWriteCachePolicy_Type = CfprStorageActualWriteType
_CfprStorageVirtualDriveActualWriteCachePolicy_Object = MibTableColumn
cfprStorageVirtualDriveActualWriteCachePolicy = _CfprStorageVirtualDriveActualWriteCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 5),
    _CfprStorageVirtualDriveActualWriteCachePolicy_Type()
)
cfprStorageVirtualDriveActualWriteCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveActualWriteCachePolicy.setStatus("current")
_CfprStorageVirtualDriveBlockSize_Type = Gauge32
_CfprStorageVirtualDriveBlockSize_Object = MibTableColumn
cfprStorageVirtualDriveBlockSize = _CfprStorageVirtualDriveBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 6),
    _CfprStorageVirtualDriveBlockSize_Type()
)
cfprStorageVirtualDriveBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveBlockSize.setStatus("current")
_CfprStorageVirtualDriveBootable_Type = CfprStorageBootableType
_CfprStorageVirtualDriveBootable_Object = MibTableColumn
cfprStorageVirtualDriveBootable = _CfprStorageVirtualDriveBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 7),
    _CfprStorageVirtualDriveBootable_Type()
)
cfprStorageVirtualDriveBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveBootable.setStatus("current")
_CfprStorageVirtualDriveConfiguredWriteCachePolicy_Type = CfprStorageConfiguredWriteType
_CfprStorageVirtualDriveConfiguredWriteCachePolicy_Object = MibTableColumn
cfprStorageVirtualDriveConfiguredWriteCachePolicy = _CfprStorageVirtualDriveConfiguredWriteCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 8),
    _CfprStorageVirtualDriveConfiguredWriteCachePolicy_Type()
)
cfprStorageVirtualDriveConfiguredWriteCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveConfiguredWriteCachePolicy.setStatus("current")
_CfprStorageVirtualDriveConnectionProtocol_Type = CfprStorageConnectionProtocol
_CfprStorageVirtualDriveConnectionProtocol_Object = MibTableColumn
cfprStorageVirtualDriveConnectionProtocol = _CfprStorageVirtualDriveConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 9),
    _CfprStorageVirtualDriveConnectionProtocol_Type()
)
cfprStorageVirtualDriveConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveConnectionProtocol.setStatus("current")
_CfprStorageVirtualDriveDriveCache_Type = CfprStorageCacheType
_CfprStorageVirtualDriveDriveCache_Object = MibTableColumn
cfprStorageVirtualDriveDriveCache = _CfprStorageVirtualDriveDriveCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 10),
    _CfprStorageVirtualDriveDriveCache_Type()
)
cfprStorageVirtualDriveDriveCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveDriveCache.setStatus("current")
_CfprStorageVirtualDriveDriveState_Type = CfprStorageVDriveState
_CfprStorageVirtualDriveDriveState_Object = MibTableColumn
cfprStorageVirtualDriveDriveState = _CfprStorageVirtualDriveDriveState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 11),
    _CfprStorageVirtualDriveDriveState_Type()
)
cfprStorageVirtualDriveDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveDriveState.setStatus("current")
_CfprStorageVirtualDriveId_Type = Gauge32
_CfprStorageVirtualDriveId_Object = MibTableColumn
cfprStorageVirtualDriveId = _CfprStorageVirtualDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 12),
    _CfprStorageVirtualDriveId_Type()
)
cfprStorageVirtualDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveId.setStatus("current")
_CfprStorageVirtualDriveIoPolicy_Type = CfprStorageIOType
_CfprStorageVirtualDriveIoPolicy_Object = MibTableColumn
cfprStorageVirtualDriveIoPolicy = _CfprStorageVirtualDriveIoPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 13),
    _CfprStorageVirtualDriveIoPolicy_Type()
)
cfprStorageVirtualDriveIoPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveIoPolicy.setStatus("current")
_CfprStorageVirtualDriveLc_Type = CfprFsmLifecycle
_CfprStorageVirtualDriveLc_Object = MibTableColumn
cfprStorageVirtualDriveLc = _CfprStorageVirtualDriveLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 14),
    _CfprStorageVirtualDriveLc_Type()
)
cfprStorageVirtualDriveLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveLc.setStatus("current")
_CfprStorageVirtualDriveModel_Type = SnmpAdminString
_CfprStorageVirtualDriveModel_Object = MibTableColumn
cfprStorageVirtualDriveModel = _CfprStorageVirtualDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 15),
    _CfprStorageVirtualDriveModel_Type()
)
cfprStorageVirtualDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveModel.setStatus("current")
_CfprStorageVirtualDriveNumberOfBlocks_Type = Unsigned64
_CfprStorageVirtualDriveNumberOfBlocks_Object = MibTableColumn
cfprStorageVirtualDriveNumberOfBlocks = _CfprStorageVirtualDriveNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 16),
    _CfprStorageVirtualDriveNumberOfBlocks_Type()
)
cfprStorageVirtualDriveNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveNumberOfBlocks.setStatus("current")
_CfprStorageVirtualDriveOperQualifierReason_Type = SnmpAdminString
_CfprStorageVirtualDriveOperQualifierReason_Object = MibTableColumn
cfprStorageVirtualDriveOperQualifierReason = _CfprStorageVirtualDriveOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 17),
    _CfprStorageVirtualDriveOperQualifierReason_Type()
)
cfprStorageVirtualDriveOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveOperQualifierReason.setStatus("current")
_CfprStorageVirtualDriveOperability_Type = CfprEquipmentOperability
_CfprStorageVirtualDriveOperability_Object = MibTableColumn
cfprStorageVirtualDriveOperability = _CfprStorageVirtualDriveOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 18),
    _CfprStorageVirtualDriveOperability_Type()
)
cfprStorageVirtualDriveOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveOperability.setStatus("current")
_CfprStorageVirtualDrivePresence_Type = CfprEquipmentPresence
_CfprStorageVirtualDrivePresence_Object = MibTableColumn
cfprStorageVirtualDrivePresence = _CfprStorageVirtualDrivePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 19),
    _CfprStorageVirtualDrivePresence_Type()
)
cfprStorageVirtualDrivePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDrivePresence.setStatus("current")
_CfprStorageVirtualDriveReadPolicy_Type = CfprStorageReadType
_CfprStorageVirtualDriveReadPolicy_Object = MibTableColumn
cfprStorageVirtualDriveReadPolicy = _CfprStorageVirtualDriveReadPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 20),
    _CfprStorageVirtualDriveReadPolicy_Type()
)
cfprStorageVirtualDriveReadPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveReadPolicy.setStatus("current")
_CfprStorageVirtualDriveRevision_Type = SnmpAdminString
_CfprStorageVirtualDriveRevision_Object = MibTableColumn
cfprStorageVirtualDriveRevision = _CfprStorageVirtualDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 21),
    _CfprStorageVirtualDriveRevision_Type()
)
cfprStorageVirtualDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveRevision.setStatus("current")
_CfprStorageVirtualDriveSerial_Type = SnmpAdminString
_CfprStorageVirtualDriveSerial_Object = MibTableColumn
cfprStorageVirtualDriveSerial = _CfprStorageVirtualDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 22),
    _CfprStorageVirtualDriveSerial_Type()
)
cfprStorageVirtualDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveSerial.setStatus("current")
_CfprStorageVirtualDriveSize_Type = Unsigned64
_CfprStorageVirtualDriveSize_Object = MibTableColumn
cfprStorageVirtualDriveSize = _CfprStorageVirtualDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 23),
    _CfprStorageVirtualDriveSize_Type()
)
cfprStorageVirtualDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveSize.setStatus("current")
_CfprStorageVirtualDriveStripSize_Type = Unsigned64
_CfprStorageVirtualDriveStripSize_Object = MibTableColumn
cfprStorageVirtualDriveStripSize = _CfprStorageVirtualDriveStripSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 24),
    _CfprStorageVirtualDriveStripSize_Type()
)
cfprStorageVirtualDriveStripSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveStripSize.setStatus("current")
_CfprStorageVirtualDriveType_Type = CfprStorageLunType
_CfprStorageVirtualDriveType_Object = MibTableColumn
cfprStorageVirtualDriveType = _CfprStorageVirtualDriveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 25),
    _CfprStorageVirtualDriveType_Type()
)
cfprStorageVirtualDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveType.setStatus("current")
_CfprStorageVirtualDriveVendor_Type = SnmpAdminString
_CfprStorageVirtualDriveVendor_Object = MibTableColumn
cfprStorageVirtualDriveVendor = _CfprStorageVirtualDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 41, 1, 26),
    _CfprStorageVirtualDriveVendor_Type()
)
cfprStorageVirtualDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVirtualDriveVendor.setStatus("current")
_CfprStorageVsanRefTable_Object = MibTable
cfprStorageVsanRefTable = _CfprStorageVsanRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 42)
)
if mibBuilder.loadTexts:
    cfprStorageVsanRefTable.setStatus("current")
_CfprStorageVsanRefEntry_Object = MibTableRow
cfprStorageVsanRefEntry = _CfprStorageVsanRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 42, 1)
)
cfprStorageVsanRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STORAGE-MIB", "cfprStorageVsanRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStorageVsanRefEntry.setStatus("current")
_CfprStorageVsanRefInstanceId_Type = CfprManagedObjectId
_CfprStorageVsanRefInstanceId_Object = MibTableColumn
cfprStorageVsanRefInstanceId = _CfprStorageVsanRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 42, 1, 1),
    _CfprStorageVsanRefInstanceId_Type()
)
cfprStorageVsanRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStorageVsanRefInstanceId.setStatus("current")
_CfprStorageVsanRefDn_Type = CfprManagedObjectDn
_CfprStorageVsanRefDn_Object = MibTableColumn
cfprStorageVsanRefDn = _CfprStorageVsanRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 42, 1, 2),
    _CfprStorageVsanRefDn_Type()
)
cfprStorageVsanRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVsanRefDn.setStatus("current")
_CfprStorageVsanRefRn_Type = SnmpAdminString
_CfprStorageVsanRefRn_Object = MibTableColumn
cfprStorageVsanRefRn = _CfprStorageVsanRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 42, 1, 3),
    _CfprStorageVsanRefRn_Type()
)
cfprStorageVsanRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVsanRefRn.setStatus("current")
_CfprStorageVsanRefConfigQualifier_Type = CfprVnicConfigIssues
_CfprStorageVsanRefConfigQualifier_Object = MibTableColumn
cfprStorageVsanRefConfigQualifier = _CfprStorageVsanRefConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 42, 1, 4),
    _CfprStorageVsanRefConfigQualifier_Type()
)
cfprStorageVsanRefConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVsanRefConfigQualifier.setStatus("current")
_CfprStorageVsanRefName_Type = SnmpAdminString
_CfprStorageVsanRefName_Object = MibTableColumn
cfprStorageVsanRefName = _CfprStorageVsanRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 42, 1, 5),
    _CfprStorageVsanRefName_Type()
)
cfprStorageVsanRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVsanRefName.setStatus("current")
_CfprStorageVsanRefOperVnetDn_Type = SnmpAdminString
_CfprStorageVsanRefOperVnetDn_Object = MibTableColumn
cfprStorageVsanRefOperVnetDn = _CfprStorageVsanRefOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 42, 1, 6),
    _CfprStorageVsanRefOperVnetDn_Type()
)
cfprStorageVsanRefOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVsanRefOperVnetDn.setStatus("current")
_CfprStorageVsanRefOperVnetName_Type = SnmpAdminString
_CfprStorageVsanRefOperVnetName_Object = MibTableColumn
cfprStorageVsanRefOperVnetName = _CfprStorageVsanRefOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 42, 1, 7),
    _CfprStorageVsanRefOperVnetName_Type()
)
cfprStorageVsanRefOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVsanRefOperVnetName.setStatus("current")
_CfprStorageVsanRefSwitchId_Type = CfprStorageVsanRefSwitchId
_CfprStorageVsanRefSwitchId_Object = MibTableColumn
cfprStorageVsanRefSwitchId = _CfprStorageVsanRefSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 42, 1, 8),
    _CfprStorageVsanRefSwitchId_Type()
)
cfprStorageVsanRefSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVsanRefSwitchId.setStatus("current")
_CfprStorageVsanRefVnet_Type = Gauge32
_CfprStorageVsanRefVnet_Object = MibTableColumn
cfprStorageVsanRefVnet = _CfprStorageVsanRefVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 42, 1, 9),
    _CfprStorageVsanRefVnet_Type()
)
cfprStorageVsanRefVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVsanRefVnet.setStatus("current")
_CfprStorageVsanRefZoningState_Type = CfprFabricZoningState
_CfprStorageVsanRefZoningState_Object = MibTableColumn
cfprStorageVsanRefZoningState = _CfprStorageVsanRefZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 74, 42, 1, 10),
    _CfprStorageVsanRefZoningState_Type()
)
cfprStorageVsanRefZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStorageVsanRefZoningState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-STORAGE-MIB",
    **{"cfprStorageObjects": cfprStorageObjects,
       "cfprStorageAuthKeyTable": cfprStorageAuthKeyTable,
       "cfprStorageAuthKeyEntry": cfprStorageAuthKeyEntry,
       "cfprStorageAuthKeyInstanceId": cfprStorageAuthKeyInstanceId,
       "cfprStorageAuthKeyDn": cfprStorageAuthKeyDn,
       "cfprStorageAuthKeyRn": cfprStorageAuthKeyRn,
       "cfprStorageAuthKeyDescr": cfprStorageAuthKeyDescr,
       "cfprStorageAuthKeyIntId": cfprStorageAuthKeyIntId,
       "cfprStorageAuthKeyName": cfprStorageAuthKeyName,
       "cfprStorageAuthKeyPassword": cfprStorageAuthKeyPassword,
       "cfprStorageAuthKeyPolicyLevel": cfprStorageAuthKeyPolicyLevel,
       "cfprStorageAuthKeyPolicyOwner": cfprStorageAuthKeyPolicyOwner,
       "cfprStorageAuthKeyType": cfprStorageAuthKeyType,
       "cfprStorageAuthKeyUserId": cfprStorageAuthKeyUserId,
       "cfprStorageConnectionDefTable": cfprStorageConnectionDefTable,
       "cfprStorageConnectionDefEntry": cfprStorageConnectionDefEntry,
       "cfprStorageConnectionDefInstanceId": cfprStorageConnectionDefInstanceId,
       "cfprStorageConnectionDefDn": cfprStorageConnectionDefDn,
       "cfprStorageConnectionDefRn": cfprStorageConnectionDefRn,
       "cfprStorageConnectionDefDescr": cfprStorageConnectionDefDescr,
       "cfprStorageConnectionDefIntId": cfprStorageConnectionDefIntId,
       "cfprStorageConnectionDefName": cfprStorageConnectionDefName,
       "cfprStorageConnectionDefOperState": cfprStorageConnectionDefOperState,
       "cfprStorageConnectionDefPolicyLevel": cfprStorageConnectionDefPolicyLevel,
       "cfprStorageConnectionDefPolicyOwner": cfprStorageConnectionDefPolicyOwner,
       "cfprStorageConnectionDefZoningType": cfprStorageConnectionDefZoningType,
       "cfprStorageConnectionPolicyTable": cfprStorageConnectionPolicyTable,
       "cfprStorageConnectionPolicyEntry": cfprStorageConnectionPolicyEntry,
       "cfprStorageConnectionPolicyInstanceId": cfprStorageConnectionPolicyInstanceId,
       "cfprStorageConnectionPolicyDn": cfprStorageConnectionPolicyDn,
       "cfprStorageConnectionPolicyRn": cfprStorageConnectionPolicyRn,
       "cfprStorageConnectionPolicyDescr": cfprStorageConnectionPolicyDescr,
       "cfprStorageConnectionPolicyIntId": cfprStorageConnectionPolicyIntId,
       "cfprStorageConnectionPolicyName": cfprStorageConnectionPolicyName,
       "cfprStorageConnectionPolicyOperState": cfprStorageConnectionPolicyOperState,
       "cfprStorageConnectionPolicyPolicyLevel": cfprStorageConnectionPolicyPolicyLevel,
       "cfprStorageConnectionPolicyPolicyOwner": cfprStorageConnectionPolicyPolicyOwner,
       "cfprStorageConnectionPolicyZoningType": cfprStorageConnectionPolicyZoningType,
       "cfprStorageControllerTable": cfprStorageControllerTable,
       "cfprStorageControllerEntry": cfprStorageControllerEntry,
       "cfprStorageControllerInstanceId": cfprStorageControllerInstanceId,
       "cfprStorageControllerDn": cfprStorageControllerDn,
       "cfprStorageControllerRn": cfprStorageControllerRn,
       "cfprStorageControllerControllerStatus": cfprStorageControllerControllerStatus,
       "cfprStorageControllerDeviceRaidSupport": cfprStorageControllerDeviceRaidSupport,
       "cfprStorageControllerFaultMonitoring": cfprStorageControllerFaultMonitoring,
       "cfprStorageControllerHwRevision": cfprStorageControllerHwRevision,
       "cfprStorageControllerId": cfprStorageControllerId,
       "cfprStorageControllerLc": cfprStorageControllerLc,
       "cfprStorageControllerLocationDn": cfprStorageControllerLocationDn,
       "cfprStorageControllerModel": cfprStorageControllerModel,
       "cfprStorageControllerOobControllerId": cfprStorageControllerOobControllerId,
       "cfprStorageControllerOobInterfaceSupported": cfprStorageControllerOobInterfaceSupported,
       "cfprStorageControllerOperQualifierReason": cfprStorageControllerOperQualifierReason,
       "cfprStorageControllerOperState": cfprStorageControllerOperState,
       "cfprStorageControllerOperability": cfprStorageControllerOperability,
       "cfprStorageControllerPartNumber": cfprStorageControllerPartNumber,
       "cfprStorageControllerPciAddr": cfprStorageControllerPciAddr,
       "cfprStorageControllerPciSlot": cfprStorageControllerPciSlot,
       "cfprStorageControllerPerf": cfprStorageControllerPerf,
       "cfprStorageControllerPower": cfprStorageControllerPower,
       "cfprStorageControllerPresence": cfprStorageControllerPresence,
       "cfprStorageControllerRaidSupport": cfprStorageControllerRaidSupport,
       "cfprStorageControllerRebuildRate": cfprStorageControllerRebuildRate,
       "cfprStorageControllerRevision": cfprStorageControllerRevision,
       "cfprStorageControllerSerial": cfprStorageControllerSerial,
       "cfprStorageControllerThermal": cfprStorageControllerThermal,
       "cfprStorageControllerType": cfprStorageControllerType,
       "cfprStorageControllerVendor": cfprStorageControllerVendor,
       "cfprStorageControllerVid": cfprStorageControllerVid,
       "cfprStorageControllerVoltage": cfprStorageControllerVoltage,
       "cfprStorageDomainEpTable": cfprStorageDomainEpTable,
       "cfprStorageDomainEpEntry": cfprStorageDomainEpEntry,
       "cfprStorageDomainEpInstanceId": cfprStorageDomainEpInstanceId,
       "cfprStorageDomainEpDn": cfprStorageDomainEpDn,
       "cfprStorageDomainEpRn": cfprStorageDomainEpRn,
       "cfprStorageDriveTable": cfprStorageDriveTable,
       "cfprStorageDriveEntry": cfprStorageDriveEntry,
       "cfprStorageDriveInstanceId": cfprStorageDriveInstanceId,
       "cfprStorageDriveDn": cfprStorageDriveDn,
       "cfprStorageDriveRn": cfprStorageDriveRn,
       "cfprStorageDriveId": cfprStorageDriveId,
       "cfprStorageDriveModel": cfprStorageDriveModel,
       "cfprStorageDrivePciAddr": cfprStorageDrivePciAddr,
       "cfprStorageDriveRevision": cfprStorageDriveRevision,
       "cfprStorageDriveSerial": cfprStorageDriveSerial,
       "cfprStorageDriveVendor": cfprStorageDriveVendor,
       "cfprStorageEnclosureTable": cfprStorageEnclosureTable,
       "cfprStorageEnclosureEntry": cfprStorageEnclosureEntry,
       "cfprStorageEnclosureInstanceId": cfprStorageEnclosureInstanceId,
       "cfprStorageEnclosureDn": cfprStorageEnclosureDn,
       "cfprStorageEnclosureRn": cfprStorageEnclosureRn,
       "cfprStorageEnclosureId": cfprStorageEnclosureId,
       "cfprStorageEnclosureLc": cfprStorageEnclosureLc,
       "cfprStorageEnclosureModel": cfprStorageEnclosureModel,
       "cfprStorageEnclosureNumSlots": cfprStorageEnclosureNumSlots,
       "cfprStorageEnclosureRevision": cfprStorageEnclosureRevision,
       "cfprStorageEnclosureSerial": cfprStorageEnclosureSerial,
       "cfprStorageEnclosureVendor": cfprStorageEnclosureVendor,
       "cfprStorageEpUserTable": cfprStorageEpUserTable,
       "cfprStorageEpUserEntry": cfprStorageEpUserEntry,
       "cfprStorageEpUserInstanceId": cfprStorageEpUserInstanceId,
       "cfprStorageEpUserDn": cfprStorageEpUserDn,
       "cfprStorageEpUserRn": cfprStorageEpUserRn,
       "cfprStorageEpUserConfigState": cfprStorageEpUserConfigState,
       "cfprStorageEpUserConfigStatusMessage": cfprStorageEpUserConfigStatusMessage,
       "cfprStorageEpUserDescr": cfprStorageEpUserDescr,
       "cfprStorageEpUserDomain": cfprStorageEpUserDomain,
       "cfprStorageEpUserName": cfprStorageEpUserName,
       "cfprStorageEpUserPriv": cfprStorageEpUserPriv,
       "cfprStorageEpUserPwd": cfprStorageEpUserPwd,
       "cfprStorageEpUserPwdSet": cfprStorageEpUserPwdSet,
       "cfprStorageEtherIfTable": cfprStorageEtherIfTable,
       "cfprStorageEtherIfEntry": cfprStorageEtherIfEntry,
       "cfprStorageEtherIfInstanceId": cfprStorageEtherIfInstanceId,
       "cfprStorageEtherIfDn": cfprStorageEtherIfDn,
       "cfprStorageEtherIfRn": cfprStorageEtherIfRn,
       "cfprStorageEtherIfName": cfprStorageEtherIfName,
       "cfprStorageEtherIfVlanType": cfprStorageEtherIfVlanType,
       "cfprStorageFcIfTable": cfprStorageFcIfTable,
       "cfprStorageFcIfEntry": cfprStorageFcIfEntry,
       "cfprStorageFcIfInstanceId": cfprStorageFcIfInstanceId,
       "cfprStorageFcIfDn": cfprStorageFcIfDn,
       "cfprStorageFcIfRn": cfprStorageFcIfRn,
       "cfprStorageFcIfName": cfprStorageFcIfName,
       "cfprStorageFcTargetEpTable": cfprStorageFcTargetEpTable,
       "cfprStorageFcTargetEpEntry": cfprStorageFcTargetEpEntry,
       "cfprStorageFcTargetEpInstanceId": cfprStorageFcTargetEpInstanceId,
       "cfprStorageFcTargetEpDn": cfprStorageFcTargetEpDn,
       "cfprStorageFcTargetEpRn": cfprStorageFcTargetEpRn,
       "cfprStorageFcTargetEpDescr": cfprStorageFcTargetEpDescr,
       "cfprStorageFcTargetEpPath": cfprStorageFcTargetEpPath,
       "cfprStorageFcTargetEpTargetwwpn": cfprStorageFcTargetEpTargetwwpn,
       "cfprStorageFcTargetIfTable": cfprStorageFcTargetIfTable,
       "cfprStorageFcTargetIfEntry": cfprStorageFcTargetIfEntry,
       "cfprStorageFcTargetIfInstanceId": cfprStorageFcTargetIfInstanceId,
       "cfprStorageFcTargetIfDn": cfprStorageFcTargetIfDn,
       "cfprStorageFcTargetIfRn": cfprStorageFcTargetIfRn,
       "cfprStorageFcTargetIfId": cfprStorageFcTargetIfId,
       "cfprStorageFcTargetIfProt": cfprStorageFcTargetIfProt,
       "cfprStorageFlexFlashCardTable": cfprStorageFlexFlashCardTable,
       "cfprStorageFlexFlashCardEntry": cfprStorageFlexFlashCardEntry,
       "cfprStorageFlexFlashCardInstanceId": cfprStorageFlexFlashCardInstanceId,
       "cfprStorageFlexFlashCardDn": cfprStorageFlexFlashCardDn,
       "cfprStorageFlexFlashCardRn": cfprStorageFlexFlashCardRn,
       "cfprStorageFlexFlashCardBlockSize": cfprStorageFlexFlashCardBlockSize,
       "cfprStorageFlexFlashCardCardHealth": cfprStorageFlexFlashCardCardHealth,
       "cfprStorageFlexFlashCardCardMode": cfprStorageFlexFlashCardCardMode,
       "cfprStorageFlexFlashCardCardState": cfprStorageFlexFlashCardCardState,
       "cfprStorageFlexFlashCardCardSync": cfprStorageFlexFlashCardCardSync,
       "cfprStorageFlexFlashCardCardType": cfprStorageFlexFlashCardCardType,
       "cfprStorageFlexFlashCardConnectionProtocol": cfprStorageFlexFlashCardConnectionProtocol,
       "cfprStorageFlexFlashCardControllerIndex": cfprStorageFlexFlashCardControllerIndex,
       "cfprStorageFlexFlashCardDrivesEnabled": cfprStorageFlexFlashCardDrivesEnabled,
       "cfprStorageFlexFlashCardId": cfprStorageFlexFlashCardId,
       "cfprStorageFlexFlashCardMfgDate": cfprStorageFlexFlashCardMfgDate,
       "cfprStorageFlexFlashCardMfgId": cfprStorageFlexFlashCardMfgId,
       "cfprStorageFlexFlashCardModel": cfprStorageFlexFlashCardModel,
       "cfprStorageFlexFlashCardNumberOfBlocks": cfprStorageFlexFlashCardNumberOfBlocks,
       "cfprStorageFlexFlashCardOemId": cfprStorageFlexFlashCardOemId,
       "cfprStorageFlexFlashCardOperQualifierReason": cfprStorageFlexFlashCardOperQualifierReason,
       "cfprStorageFlexFlashCardOperability": cfprStorageFlexFlashCardOperability,
       "cfprStorageFlexFlashCardPartitionCount": cfprStorageFlexFlashCardPartitionCount,
       "cfprStorageFlexFlashCardPresence": cfprStorageFlexFlashCardPresence,
       "cfprStorageFlexFlashCardReadErrorThreshold": cfprStorageFlexFlashCardReadErrorThreshold,
       "cfprStorageFlexFlashCardReadIOErrorCount": cfprStorageFlexFlashCardReadIOErrorCount,
       "cfprStorageFlexFlashCardRevision": cfprStorageFlexFlashCardRevision,
       "cfprStorageFlexFlashCardSerial": cfprStorageFlexFlashCardSerial,
       "cfprStorageFlexFlashCardSignature": cfprStorageFlexFlashCardSignature,
       "cfprStorageFlexFlashCardSize": cfprStorageFlexFlashCardSize,
       "cfprStorageFlexFlashCardSlotNumber": cfprStorageFlexFlashCardSlotNumber,
       "cfprStorageFlexFlashCardVendor": cfprStorageFlexFlashCardVendor,
       "cfprStorageFlexFlashCardWriteEnable": cfprStorageFlexFlashCardWriteEnable,
       "cfprStorageFlexFlashCardWriteErrorThreshold": cfprStorageFlexFlashCardWriteErrorThreshold,
       "cfprStorageFlexFlashCardWriteIOErrorCount": cfprStorageFlexFlashCardWriteIOErrorCount,
       "cfprStorageFlexFlashControllerTable": cfprStorageFlexFlashControllerTable,
       "cfprStorageFlexFlashControllerEntry": cfprStorageFlexFlashControllerEntry,
       "cfprStorageFlexFlashControllerInstanceId": cfprStorageFlexFlashControllerInstanceId,
       "cfprStorageFlexFlashControllerDn": cfprStorageFlexFlashControllerDn,
       "cfprStorageFlexFlashControllerRn": cfprStorageFlexFlashControllerRn,
       "cfprStorageFlexFlashControllerAdminSlotNumber": cfprStorageFlexFlashControllerAdminSlotNumber,
       "cfprStorageFlexFlashControllerConfiguredMode": cfprStorageFlexFlashControllerConfiguredMode,
       "cfprStorageFlexFlashControllerControllerHealth": cfprStorageFlexFlashControllerControllerHealth,
       "cfprStorageFlexFlashControllerControllerState": cfprStorageFlexFlashControllerControllerState,
       "cfprStorageFlexFlashControllerFirmwareVersion": cfprStorageFlexFlashControllerFirmwareVersion,
       "cfprStorageFlexFlashControllerFlexFlashType": cfprStorageFlexFlashControllerFlexFlashType,
       "cfprStorageFlexFlashControllerFsmDescr": cfprStorageFlexFlashControllerFsmDescr,
       "cfprStorageFlexFlashControllerFsmPrev": cfprStorageFlexFlashControllerFsmPrev,
       "cfprStorageFlexFlashControllerFsmProgr": cfprStorageFlexFlashControllerFsmProgr,
       "cfprStorageFlexFlashControllerFsmRmtInvErrCode": cfprStorageFlexFlashControllerFsmRmtInvErrCode,
       "cfprStorageFlexFlashControllerFsmRmtInvErrDescr": cfprStorageFlexFlashControllerFsmRmtInvErrDescr,
       "cfprStorageFlexFlashControllerFsmRmtInvRslt": cfprStorageFlexFlashControllerFsmRmtInvRslt,
       "cfprStorageFlexFlashControllerFsmStageDescr": cfprStorageFlexFlashControllerFsmStageDescr,
       "cfprStorageFlexFlashControllerFsmStamp": cfprStorageFlexFlashControllerFsmStamp,
       "cfprStorageFlexFlashControllerFsmStatus": cfprStorageFlexFlashControllerFsmStatus,
       "cfprStorageFlexFlashControllerFsmTry": cfprStorageFlexFlashControllerFsmTry,
       "cfprStorageFlexFlashControllerHasError": cfprStorageFlexFlashControllerHasError,
       "cfprStorageFlexFlashControllerId": cfprStorageFlexFlashControllerId,
       "cfprStorageFlexFlashControllerIsCardMismatch": cfprStorageFlexFlashControllerIsCardMismatch,
       "cfprStorageFlexFlashControllerIsFormatFSMRunning": cfprStorageFlexFlashControllerIsFormatFSMRunning,
       "cfprStorageFlexFlashControllerLocationDn": cfprStorageFlexFlashControllerLocationDn,
       "cfprStorageFlexFlashControllerModel": cfprStorageFlexFlashControllerModel,
       "cfprStorageFlexFlashControllerOperQualifierReason": cfprStorageFlexFlashControllerOperQualifierReason,
       "cfprStorageFlexFlashControllerOperState": cfprStorageFlexFlashControllerOperState,
       "cfprStorageFlexFlashControllerOperability": cfprStorageFlexFlashControllerOperability,
       "cfprStorageFlexFlashControllerOperatingMode": cfprStorageFlexFlashControllerOperatingMode,
       "cfprStorageFlexFlashControllerOperationRequest": cfprStorageFlexFlashControllerOperationRequest,
       "cfprStorageFlexFlashControllerPciAddr": cfprStorageFlexFlashControllerPciAddr,
       "cfprStorageFlexFlashControllerPciSlot": cfprStorageFlexFlashControllerPciSlot,
       "cfprStorageFlexFlashControllerPerf": cfprStorageFlexFlashControllerPerf,
       "cfprStorageFlexFlashControllerPhysicalDriveCount": cfprStorageFlexFlashControllerPhysicalDriveCount,
       "cfprStorageFlexFlashControllerPower": cfprStorageFlexFlashControllerPower,
       "cfprStorageFlexFlashControllerPresence": cfprStorageFlexFlashControllerPresence,
       "cfprStorageFlexFlashControllerPrimarySlotNumber": cfprStorageFlexFlashControllerPrimarySlotNumber,
       "cfprStorageFlexFlashControllerRaidSyncSupport": cfprStorageFlexFlashControllerRaidSyncSupport,
       "cfprStorageFlexFlashControllerReadErrorThreshold": cfprStorageFlexFlashControllerReadErrorThreshold,
       "cfprStorageFlexFlashControllerRevision": cfprStorageFlexFlashControllerRevision,
       "cfprStorageFlexFlashControllerSerial": cfprStorageFlexFlashControllerSerial,
       "cfprStorageFlexFlashControllerThermal": cfprStorageFlexFlashControllerThermal,
       "cfprStorageFlexFlashControllerType": cfprStorageFlexFlashControllerType,
       "cfprStorageFlexFlashControllerVendor": cfprStorageFlexFlashControllerVendor,
       "cfprStorageFlexFlashControllerVirtualDriveCount": cfprStorageFlexFlashControllerVirtualDriveCount,
       "cfprStorageFlexFlashControllerVoltage": cfprStorageFlexFlashControllerVoltage,
       "cfprStorageFlexFlashControllerWriteErrorThreshold": cfprStorageFlexFlashControllerWriteErrorThreshold,
       "cfprStorageFlexFlashControllerFsmTable": cfprStorageFlexFlashControllerFsmTable,
       "cfprStorageFlexFlashControllerFsmEntry": cfprStorageFlexFlashControllerFsmEntry,
       "cfprStorageFlexFlashControllerFsmInstanceId": cfprStorageFlexFlashControllerFsmInstanceId,
       "cfprStorageFlexFlashControllerFsmDn": cfprStorageFlexFlashControllerFsmDn,
       "cfprStorageFlexFlashControllerFsmRn": cfprStorageFlexFlashControllerFsmRn,
       "cfprStorageFlexFlashControllerFsmCompletionTime": cfprStorageFlexFlashControllerFsmCompletionTime,
       "cfprStorageFlexFlashControllerFsmCurrentFsm": cfprStorageFlexFlashControllerFsmCurrentFsm,
       "cfprStorageFlexFlashControllerFsmDescrData": cfprStorageFlexFlashControllerFsmDescrData,
       "cfprStorageFlexFlashControllerFsmFsmStatus": cfprStorageFlexFlashControllerFsmFsmStatus,
       "cfprStorageFlexFlashControllerFsmProgress": cfprStorageFlexFlashControllerFsmProgress,
       "cfprStorageFlexFlashControllerFsmRmtErrCode": cfprStorageFlexFlashControllerFsmRmtErrCode,
       "cfprStorageFlexFlashControllerFsmRmtErrDescr": cfprStorageFlexFlashControllerFsmRmtErrDescr,
       "cfprStorageFlexFlashControllerFsmRmtRslt": cfprStorageFlexFlashControllerFsmRmtRslt,
       "cfprStorageFlexFlashControllerFsmStageTable": cfprStorageFlexFlashControllerFsmStageTable,
       "cfprStorageFlexFlashControllerFsmStageEntry": cfprStorageFlexFlashControllerFsmStageEntry,
       "cfprStorageFlexFlashControllerFsmStageInstanceId": cfprStorageFlexFlashControllerFsmStageInstanceId,
       "cfprStorageFlexFlashControllerFsmStageDn": cfprStorageFlexFlashControllerFsmStageDn,
       "cfprStorageFlexFlashControllerFsmStageRn": cfprStorageFlexFlashControllerFsmStageRn,
       "cfprStorageFlexFlashControllerFsmStageDescrData": cfprStorageFlexFlashControllerFsmStageDescrData,
       "cfprStorageFlexFlashControllerFsmStageLastUpdateTime": cfprStorageFlexFlashControllerFsmStageLastUpdateTime,
       "cfprStorageFlexFlashControllerFsmStageName": cfprStorageFlexFlashControllerFsmStageName,
       "cfprStorageFlexFlashControllerFsmStageOrder": cfprStorageFlexFlashControllerFsmStageOrder,
       "cfprStorageFlexFlashControllerFsmStageRetry": cfprStorageFlexFlashControllerFsmStageRetry,
       "cfprStorageFlexFlashControllerFsmStageStageStatus": cfprStorageFlexFlashControllerFsmStageStageStatus,
       "cfprStorageFlexFlashControllerFsmTaskTable": cfprStorageFlexFlashControllerFsmTaskTable,
       "cfprStorageFlexFlashControllerFsmTaskEntry": cfprStorageFlexFlashControllerFsmTaskEntry,
       "cfprStorageFlexFlashControllerFsmTaskInstanceId": cfprStorageFlexFlashControllerFsmTaskInstanceId,
       "cfprStorageFlexFlashControllerFsmTaskDn": cfprStorageFlexFlashControllerFsmTaskDn,
       "cfprStorageFlexFlashControllerFsmTaskRn": cfprStorageFlexFlashControllerFsmTaskRn,
       "cfprStorageFlexFlashControllerFsmTaskCompletion": cfprStorageFlexFlashControllerFsmTaskCompletion,
       "cfprStorageFlexFlashControllerFsmTaskFlags": cfprStorageFlexFlashControllerFsmTaskFlags,
       "cfprStorageFlexFlashControllerFsmTaskItem": cfprStorageFlexFlashControllerFsmTaskItem,
       "cfprStorageFlexFlashControllerFsmTaskSeqId": cfprStorageFlexFlashControllerFsmTaskSeqId,
       "cfprStorageFlexFlashDriveTable": cfprStorageFlexFlashDriveTable,
       "cfprStorageFlexFlashDriveEntry": cfprStorageFlexFlashDriveEntry,
       "cfprStorageFlexFlashDriveInstanceId": cfprStorageFlexFlashDriveInstanceId,
       "cfprStorageFlexFlashDriveDn": cfprStorageFlexFlashDriveDn,
       "cfprStorageFlexFlashDriveRn": cfprStorageFlexFlashDriveRn,
       "cfprStorageFlexFlashDriveRWType": cfprStorageFlexFlashDriveRWType,
       "cfprStorageFlexFlashDriveBlockSize": cfprStorageFlexFlashDriveBlockSize,
       "cfprStorageFlexFlashDriveConnectionProtocol": cfprStorageFlexFlashDriveConnectionProtocol,
       "cfprStorageFlexFlashDriveControllerIndex": cfprStorageFlexFlashDriveControllerIndex,
       "cfprStorageFlexFlashDriveDriveState": cfprStorageFlexFlashDriveDriveState,
       "cfprStorageFlexFlashDriveDriveType": cfprStorageFlexFlashDriveDriveType,
       "cfprStorageFlexFlashDriveId": cfprStorageFlexFlashDriveId,
       "cfprStorageFlexFlashDriveLastOperation": cfprStorageFlexFlashDriveLastOperation,
       "cfprStorageFlexFlashDriveModel": cfprStorageFlexFlashDriveModel,
       "cfprStorageFlexFlashDriveName": cfprStorageFlexFlashDriveName,
       "cfprStorageFlexFlashDriveNumberOfBlocks": cfprStorageFlexFlashDriveNumberOfBlocks,
       "cfprStorageFlexFlashDriveOperQualifierReason": cfprStorageFlexFlashDriveOperQualifierReason,
       "cfprStorageFlexFlashDriveOperability": cfprStorageFlexFlashDriveOperability,
       "cfprStorageFlexFlashDriveOperationState": cfprStorageFlexFlashDriveOperationState,
       "cfprStorageFlexFlashDrivePresence": cfprStorageFlexFlashDrivePresence,
       "cfprStorageFlexFlashDriveRemovable": cfprStorageFlexFlashDriveRemovable,
       "cfprStorageFlexFlashDriveRevision": cfprStorageFlexFlashDriveRevision,
       "cfprStorageFlexFlashDriveSerial": cfprStorageFlexFlashDriveSerial,
       "cfprStorageFlexFlashDriveSize": cfprStorageFlexFlashDriveSize,
       "cfprStorageFlexFlashDriveSlotNumber": cfprStorageFlexFlashDriveSlotNumber,
       "cfprStorageFlexFlashDriveVendor": cfprStorageFlexFlashDriveVendor,
       "cfprStorageFlexFlashDriveVisible": cfprStorageFlexFlashDriveVisible,
       "cfprStorageFlexFlashVirtualDriveTable": cfprStorageFlexFlashVirtualDriveTable,
       "cfprStorageFlexFlashVirtualDriveEntry": cfprStorageFlexFlashVirtualDriveEntry,
       "cfprStorageFlexFlashVirtualDriveInstanceId": cfprStorageFlexFlashVirtualDriveInstanceId,
       "cfprStorageFlexFlashVirtualDriveDn": cfprStorageFlexFlashVirtualDriveDn,
       "cfprStorageFlexFlashVirtualDriveRn": cfprStorageFlexFlashVirtualDriveRn,
       "cfprStorageFlexFlashVirtualDriveBlockSize": cfprStorageFlexFlashVirtualDriveBlockSize,
       "cfprStorageFlexFlashVirtualDriveConnectionProtocol": cfprStorageFlexFlashVirtualDriveConnectionProtocol,
       "cfprStorageFlexFlashVirtualDriveId": cfprStorageFlexFlashVirtualDriveId,
       "cfprStorageFlexFlashVirtualDriveModel": cfprStorageFlexFlashVirtualDriveModel,
       "cfprStorageFlexFlashVirtualDriveNumberOfBlocks": cfprStorageFlexFlashVirtualDriveNumberOfBlocks,
       "cfprStorageFlexFlashVirtualDriveOperQualifierReason": cfprStorageFlexFlashVirtualDriveOperQualifierReason,
       "cfprStorageFlexFlashVirtualDriveOperability": cfprStorageFlexFlashVirtualDriveOperability,
       "cfprStorageFlexFlashVirtualDrivePresence": cfprStorageFlexFlashVirtualDrivePresence,
       "cfprStorageFlexFlashVirtualDriveRaidHealth": cfprStorageFlexFlashVirtualDriveRaidHealth,
       "cfprStorageFlexFlashVirtualDriveRaidState": cfprStorageFlexFlashVirtualDriveRaidState,
       "cfprStorageFlexFlashVirtualDriveRevision": cfprStorageFlexFlashVirtualDriveRevision,
       "cfprStorageFlexFlashVirtualDriveSerial": cfprStorageFlexFlashVirtualDriveSerial,
       "cfprStorageFlexFlashVirtualDriveSize": cfprStorageFlexFlashVirtualDriveSize,
       "cfprStorageFlexFlashVirtualDriveType": cfprStorageFlexFlashVirtualDriveType,
       "cfprStorageFlexFlashVirtualDriveVendor": cfprStorageFlexFlashVirtualDriveVendor,
       "cfprStorageIScsiTargetIfTable": cfprStorageIScsiTargetIfTable,
       "cfprStorageIScsiTargetIfEntry": cfprStorageIScsiTargetIfEntry,
       "cfprStorageIScsiTargetIfInstanceId": cfprStorageIScsiTargetIfInstanceId,
       "cfprStorageIScsiTargetIfDn": cfprStorageIScsiTargetIfDn,
       "cfprStorageIScsiTargetIfRn": cfprStorageIScsiTargetIfRn,
       "cfprStorageIScsiTargetIfName": cfprStorageIScsiTargetIfName,
       "cfprStorageIScsiTargetIfProt": cfprStorageIScsiTargetIfProt,
       "cfprStorageIniGroupTable": cfprStorageIniGroupTable,
       "cfprStorageIniGroupEntry": cfprStorageIniGroupEntry,
       "cfprStorageIniGroupInstanceId": cfprStorageIniGroupInstanceId,
       "cfprStorageIniGroupDn": cfprStorageIniGroupDn,
       "cfprStorageIniGroupRn": cfprStorageIniGroupRn,
       "cfprStorageIniGroupDescr": cfprStorageIniGroupDescr,
       "cfprStorageIniGroupGroupPolicyName": cfprStorageIniGroupGroupPolicyName,
       "cfprStorageIniGroupIntId": cfprStorageIniGroupIntId,
       "cfprStorageIniGroupName": cfprStorageIniGroupName,
       "cfprStorageIniGroupOperProtocol": cfprStorageIniGroupOperProtocol,
       "cfprStorageIniGroupOperState": cfprStorageIniGroupOperState,
       "cfprStorageIniGroupOwner": cfprStorageIniGroupOwner,
       "cfprStorageIniGroupPolicyLevel": cfprStorageIniGroupPolicyLevel,
       "cfprStorageIniGroupPolicyName": cfprStorageIniGroupPolicyName,
       "cfprStorageIniGroupPolicyOwner": cfprStorageIniGroupPolicyOwner,
       "cfprStorageIniGroupProtocol": cfprStorageIniGroupProtocol,
       "cfprStorageIniGroupRmtDiskCfgName": cfprStorageIniGroupRmtDiskCfgName,
       "cfprStorageInitiatorTable": cfprStorageInitiatorTable,
       "cfprStorageInitiatorEntry": cfprStorageInitiatorEntry,
       "cfprStorageInitiatorInstanceId": cfprStorageInitiatorInstanceId,
       "cfprStorageInitiatorDn": cfprStorageInitiatorDn,
       "cfprStorageInitiatorRn": cfprStorageInitiatorRn,
       "cfprStorageInitiatorDescr": cfprStorageInitiatorDescr,
       "cfprStorageInitiatorDuplicateTarget": cfprStorageInitiatorDuplicateTarget,
       "cfprStorageInitiatorIntId": cfprStorageInitiatorIntId,
       "cfprStorageInitiatorName": cfprStorageInitiatorName,
       "cfprStorageInitiatorOperState": cfprStorageInitiatorOperState,
       "cfprStorageInitiatorPolicyLevel": cfprStorageInitiatorPolicyLevel,
       "cfprStorageInitiatorPolicyOwner": cfprStorageInitiatorPolicyOwner,
       "cfprStorageItemTable": cfprStorageItemTable,
       "cfprStorageItemEntry": cfprStorageItemEntry,
       "cfprStorageItemInstanceId": cfprStorageItemInstanceId,
       "cfprStorageItemDn": cfprStorageItemDn,
       "cfprStorageItemRn": cfprStorageItemRn,
       "cfprStorageItemName": cfprStorageItemName,
       "cfprStorageItemOperState": cfprStorageItemOperState,
       "cfprStorageItemSize": cfprStorageItemSize,
       "cfprStorageItemUsed": cfprStorageItemUsed,
       "cfprStorageLocalDiskTable": cfprStorageLocalDiskTable,
       "cfprStorageLocalDiskEntry": cfprStorageLocalDiskEntry,
       "cfprStorageLocalDiskInstanceId": cfprStorageLocalDiskInstanceId,
       "cfprStorageLocalDiskDn": cfprStorageLocalDiskDn,
       "cfprStorageLocalDiskRn": cfprStorageLocalDiskRn,
       "cfprStorageLocalDiskBlockSize": cfprStorageLocalDiskBlockSize,
       "cfprStorageLocalDiskConnectionProtocol": cfprStorageLocalDiskConnectionProtocol,
       "cfprStorageLocalDiskDeviceType": cfprStorageLocalDiskDeviceType,
       "cfprStorageLocalDiskDiskState": cfprStorageLocalDiskDiskState,
       "cfprStorageLocalDiskId": cfprStorageLocalDiskId,
       "cfprStorageLocalDiskLc": cfprStorageLocalDiskLc,
       "cfprStorageLocalDiskLinkSpeed": cfprStorageLocalDiskLinkSpeed,
       "cfprStorageLocalDiskModel": cfprStorageLocalDiskModel,
       "cfprStorageLocalDiskNumberOfBlocks": cfprStorageLocalDiskNumberOfBlocks,
       "cfprStorageLocalDiskOperQualifierReason": cfprStorageLocalDiskOperQualifierReason,
       "cfprStorageLocalDiskOperability": cfprStorageLocalDiskOperability,
       "cfprStorageLocalDiskPowerState": cfprStorageLocalDiskPowerState,
       "cfprStorageLocalDiskPresence": cfprStorageLocalDiskPresence,
       "cfprStorageLocalDiskRevision": cfprStorageLocalDiskRevision,
       "cfprStorageLocalDiskSerial": cfprStorageLocalDiskSerial,
       "cfprStorageLocalDiskSize": cfprStorageLocalDiskSize,
       "cfprStorageLocalDiskVendor": cfprStorageLocalDiskVendor,
       "cfprStorageLocalDiskConfigDefTable": cfprStorageLocalDiskConfigDefTable,
       "cfprStorageLocalDiskConfigDefEntry": cfprStorageLocalDiskConfigDefEntry,
       "cfprStorageLocalDiskConfigDefInstanceId": cfprStorageLocalDiskConfigDefInstanceId,
       "cfprStorageLocalDiskConfigDefDn": cfprStorageLocalDiskConfigDefDn,
       "cfprStorageLocalDiskConfigDefRn": cfprStorageLocalDiskConfigDefRn,
       "cfprStorageLocalDiskConfigDefDescr": cfprStorageLocalDiskConfigDefDescr,
       "cfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState": cfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState,
       "cfprStorageLocalDiskConfigDefFlexFlashState": cfprStorageLocalDiskConfigDefFlexFlashState,
       "cfprStorageLocalDiskConfigDefIntId": cfprStorageLocalDiskConfigDefIntId,
       "cfprStorageLocalDiskConfigDefMode": cfprStorageLocalDiskConfigDefMode,
       "cfprStorageLocalDiskConfigDefName": cfprStorageLocalDiskConfigDefName,
       "cfprStorageLocalDiskConfigDefPolicyLevel": cfprStorageLocalDiskConfigDefPolicyLevel,
       "cfprStorageLocalDiskConfigDefPolicyOwner": cfprStorageLocalDiskConfigDefPolicyOwner,
       "cfprStorageLocalDiskConfigDefProtectConfig": cfprStorageLocalDiskConfigDefProtectConfig,
       "cfprStorageLocalDiskConfigPolicyTable": cfprStorageLocalDiskConfigPolicyTable,
       "cfprStorageLocalDiskConfigPolicyEntry": cfprStorageLocalDiskConfigPolicyEntry,
       "cfprStorageLocalDiskConfigPolicyInstanceId": cfprStorageLocalDiskConfigPolicyInstanceId,
       "cfprStorageLocalDiskConfigPolicyDn": cfprStorageLocalDiskConfigPolicyDn,
       "cfprStorageLocalDiskConfigPolicyRn": cfprStorageLocalDiskConfigPolicyRn,
       "cfprStorageLocalDiskConfigPolicyDescr": cfprStorageLocalDiskConfigPolicyDescr,
       "cfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState": cfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState,
       "cfprStorageLocalDiskConfigPolicyFlexFlashState": cfprStorageLocalDiskConfigPolicyFlexFlashState,
       "cfprStorageLocalDiskConfigPolicyIntId": cfprStorageLocalDiskConfigPolicyIntId,
       "cfprStorageLocalDiskConfigPolicyMode": cfprStorageLocalDiskConfigPolicyMode,
       "cfprStorageLocalDiskConfigPolicyName": cfprStorageLocalDiskConfigPolicyName,
       "cfprStorageLocalDiskConfigPolicyPolicyLevel": cfprStorageLocalDiskConfigPolicyPolicyLevel,
       "cfprStorageLocalDiskConfigPolicyPolicyOwner": cfprStorageLocalDiskConfigPolicyPolicyOwner,
       "cfprStorageLocalDiskConfigPolicyProtectConfig": cfprStorageLocalDiskConfigPolicyProtectConfig,
       "cfprStorageLocalDiskPartitionTable": cfprStorageLocalDiskPartitionTable,
       "cfprStorageLocalDiskPartitionEntry": cfprStorageLocalDiskPartitionEntry,
       "cfprStorageLocalDiskPartitionInstanceId": cfprStorageLocalDiskPartitionInstanceId,
       "cfprStorageLocalDiskPartitionDn": cfprStorageLocalDiskPartitionDn,
       "cfprStorageLocalDiskPartitionRn": cfprStorageLocalDiskPartitionRn,
       "cfprStorageLocalDiskPartitionDescr": cfprStorageLocalDiskPartitionDescr,
       "cfprStorageLocalDiskPartitionIntId": cfprStorageLocalDiskPartitionIntId,
       "cfprStorageLocalDiskPartitionName": cfprStorageLocalDiskPartitionName,
       "cfprStorageLocalDiskPartitionOrder": cfprStorageLocalDiskPartitionOrder,
       "cfprStorageLocalDiskPartitionPolicyLevel": cfprStorageLocalDiskPartitionPolicyLevel,
       "cfprStorageLocalDiskPartitionPolicyOwner": cfprStorageLocalDiskPartitionPolicyOwner,
       "cfprStorageLocalDiskPartitionSize": cfprStorageLocalDiskPartitionSize,
       "cfprStorageLocalDiskPartitionType": cfprStorageLocalDiskPartitionType,
       "cfprStorageLocalDiskSlotEpTable": cfprStorageLocalDiskSlotEpTable,
       "cfprStorageLocalDiskSlotEpEntry": cfprStorageLocalDiskSlotEpEntry,
       "cfprStorageLocalDiskSlotEpInstanceId": cfprStorageLocalDiskSlotEpInstanceId,
       "cfprStorageLocalDiskSlotEpDn": cfprStorageLocalDiskSlotEpDn,
       "cfprStorageLocalDiskSlotEpRn": cfprStorageLocalDiskSlotEpRn,
       "cfprStorageLocalDiskSlotEpConfiguration": cfprStorageLocalDiskSlotEpConfiguration,
       "cfprStorageLocalDiskSlotEpId": cfprStorageLocalDiskSlotEpId,
       "cfprStorageLocalDiskSlotEpOperQualifierReason": cfprStorageLocalDiskSlotEpOperQualifierReason,
       "cfprStorageLocalDiskSlotEpOperability": cfprStorageLocalDiskSlotEpOperability,
       "cfprStorageLocalDiskSlotEpPeerDn": cfprStorageLocalDiskSlotEpPeerDn,
       "cfprStorageLocalDiskSlotEpPresence": cfprStorageLocalDiskSlotEpPresence,
       "cfprStorageLocalLunTable": cfprStorageLocalLunTable,
       "cfprStorageLocalLunEntry": cfprStorageLocalLunEntry,
       "cfprStorageLocalLunInstanceId": cfprStorageLocalLunInstanceId,
       "cfprStorageLocalLunDn": cfprStorageLocalLunDn,
       "cfprStorageLocalLunRn": cfprStorageLocalLunRn,
       "cfprStorageLocalLunBlockSize": cfprStorageLocalLunBlockSize,
       "cfprStorageLocalLunConnectionProtocol": cfprStorageLocalLunConnectionProtocol,
       "cfprStorageLocalLunId": cfprStorageLocalLunId,
       "cfprStorageLocalLunLc": cfprStorageLocalLunLc,
       "cfprStorageLocalLunModel": cfprStorageLocalLunModel,
       "cfprStorageLocalLunNumberOfBlocks": cfprStorageLocalLunNumberOfBlocks,
       "cfprStorageLocalLunOperQualifierReason": cfprStorageLocalLunOperQualifierReason,
       "cfprStorageLocalLunOperability": cfprStorageLocalLunOperability,
       "cfprStorageLocalLunPresence": cfprStorageLocalLunPresence,
       "cfprStorageLocalLunRevision": cfprStorageLocalLunRevision,
       "cfprStorageLocalLunSerial": cfprStorageLocalLunSerial,
       "cfprStorageLocalLunSize": cfprStorageLocalLunSize,
       "cfprStorageLocalLunType": cfprStorageLocalLunType,
       "cfprStorageLocalLunVendor": cfprStorageLocalLunVendor,
       "cfprStorageLunDiskTable": cfprStorageLunDiskTable,
       "cfprStorageLunDiskEntry": cfprStorageLunDiskEntry,
       "cfprStorageLunDiskInstanceId": cfprStorageLunDiskInstanceId,
       "cfprStorageLunDiskDn": cfprStorageLunDiskDn,
       "cfprStorageLunDiskRn": cfprStorageLunDiskRn,
       "cfprStorageLunDiskId": cfprStorageLunDiskId,
       "cfprStorageMezzFlashLifeTable": cfprStorageMezzFlashLifeTable,
       "cfprStorageMezzFlashLifeEntry": cfprStorageMezzFlashLifeEntry,
       "cfprStorageMezzFlashLifeInstanceId": cfprStorageMezzFlashLifeInstanceId,
       "cfprStorageMezzFlashLifeDn": cfprStorageMezzFlashLifeDn,
       "cfprStorageMezzFlashLifeRn": cfprStorageMezzFlashLifeRn,
       "cfprStorageMezzFlashLifeBlockSize": cfprStorageMezzFlashLifeBlockSize,
       "cfprStorageMezzFlashLifeConnectionProtocol": cfprStorageMezzFlashLifeConnectionProtocol,
       "cfprStorageMezzFlashLifeFlashPercentage": cfprStorageMezzFlashLifeFlashPercentage,
       "cfprStorageMezzFlashLifeFlashStatus": cfprStorageMezzFlashLifeFlashStatus,
       "cfprStorageMezzFlashLifeId": cfprStorageMezzFlashLifeId,
       "cfprStorageMezzFlashLifeModel": cfprStorageMezzFlashLifeModel,
       "cfprStorageMezzFlashLifeNumberOfBlocks": cfprStorageMezzFlashLifeNumberOfBlocks,
       "cfprStorageMezzFlashLifeOperQualifierReason": cfprStorageMezzFlashLifeOperQualifierReason,
       "cfprStorageMezzFlashLifeOperability": cfprStorageMezzFlashLifeOperability,
       "cfprStorageMezzFlashLifePresence": cfprStorageMezzFlashLifePresence,
       "cfprStorageMezzFlashLifeRevision": cfprStorageMezzFlashLifeRevision,
       "cfprStorageMezzFlashLifeSerial": cfprStorageMezzFlashLifeSerial,
       "cfprStorageMezzFlashLifeSize": cfprStorageMezzFlashLifeSize,
       "cfprStorageMezzFlashLifeVendor": cfprStorageMezzFlashLifeVendor,
       "cfprStorageNodeEpTable": cfprStorageNodeEpTable,
       "cfprStorageNodeEpEntry": cfprStorageNodeEpEntry,
       "cfprStorageNodeEpInstanceId": cfprStorageNodeEpInstanceId,
       "cfprStorageNodeEpDn": cfprStorageNodeEpDn,
       "cfprStorageNodeEpRn": cfprStorageNodeEpRn,
       "cfprStorageNodeEpEpDn": cfprStorageNodeEpEpDn,
       "cfprStorageNodeEpId": cfprStorageNodeEpId,
       "cfprStorageOperationTable": cfprStorageOperationTable,
       "cfprStorageOperationEntry": cfprStorageOperationEntry,
       "cfprStorageOperationInstanceId": cfprStorageOperationInstanceId,
       "cfprStorageOperationDn": cfprStorageOperationDn,
       "cfprStorageOperationRn": cfprStorageOperationRn,
       "cfprStorageOperationEndTime": cfprStorageOperationEndTime,
       "cfprStorageOperationName": cfprStorageOperationName,
       "cfprStorageOperationOperState": cfprStorageOperationOperState,
       "cfprStorageOperationProgress": cfprStorageOperationProgress,
       "cfprStorageOperationStartTime": cfprStorageOperationStartTime,
       "cfprStorageOperationStatusDescr": cfprStorageOperationStatusDescr,
       "cfprStorageQualTable": cfprStorageQualTable,
       "cfprStorageQualEntry": cfprStorageQualEntry,
       "cfprStorageQualInstanceId": cfprStorageQualInstanceId,
       "cfprStorageQualDn": cfprStorageQualDn,
       "cfprStorageQualRn": cfprStorageQualRn,
       "cfprStorageQualBlockSize": cfprStorageQualBlockSize,
       "cfprStorageQualDiskless": cfprStorageQualDiskless,
       "cfprStorageQualMaxCap": cfprStorageQualMaxCap,
       "cfprStorageQualMinCap": cfprStorageQualMinCap,
       "cfprStorageQualNumberOfBlocks": cfprStorageQualNumberOfBlocks,
       "cfprStorageQualNumberOfFlexFlashCards": cfprStorageQualNumberOfFlexFlashCards,
       "cfprStorageQualPerDiskCap": cfprStorageQualPerDiskCap,
       "cfprStorageQualUnits": cfprStorageQualUnits,
       "cfprStorageRaidBatteryTable": cfprStorageRaidBatteryTable,
       "cfprStorageRaidBatteryEntry": cfprStorageRaidBatteryEntry,
       "cfprStorageRaidBatteryInstanceId": cfprStorageRaidBatteryInstanceId,
       "cfprStorageRaidBatteryDn": cfprStorageRaidBatteryDn,
       "cfprStorageRaidBatteryRn": cfprStorageRaidBatteryRn,
       "cfprStorageRaidBatteryBatteryType": cfprStorageRaidBatteryBatteryType,
       "cfprStorageRaidBatteryBbuStatus": cfprStorageRaidBatteryBbuStatus,
       "cfprStorageRaidBatteryBlockSize": cfprStorageRaidBatteryBlockSize,
       "cfprStorageRaidBatteryCapacityPercentage": cfprStorageRaidBatteryCapacityPercentage,
       "cfprStorageRaidBatteryConnectionProtocol": cfprStorageRaidBatteryConnectionProtocol,
       "cfprStorageRaidBatteryId": cfprStorageRaidBatteryId,
       "cfprStorageRaidBatteryLc": cfprStorageRaidBatteryLc,
       "cfprStorageRaidBatteryLearnCycleRequested": cfprStorageRaidBatteryLearnCycleRequested,
       "cfprStorageRaidBatteryLearnMode": cfprStorageRaidBatteryLearnMode,
       "cfprStorageRaidBatteryModel": cfprStorageRaidBatteryModel,
       "cfprStorageRaidBatteryNextLearnCycleTs": cfprStorageRaidBatteryNextLearnCycleTs,
       "cfprStorageRaidBatteryNumberOfBlocks": cfprStorageRaidBatteryNumberOfBlocks,
       "cfprStorageRaidBatteryOperQualifierReason": cfprStorageRaidBatteryOperQualifierReason,
       "cfprStorageRaidBatteryOperability": cfprStorageRaidBatteryOperability,
       "cfprStorageRaidBatteryOperabilityQualifier": cfprStorageRaidBatteryOperabilityQualifier,
       "cfprStorageRaidBatteryOperabilityQualifierReason": cfprStorageRaidBatteryOperabilityQualifierReason,
       "cfprStorageRaidBatteryPresence": cfprStorageRaidBatteryPresence,
       "cfprStorageRaidBatteryRevision": cfprStorageRaidBatteryRevision,
       "cfprStorageRaidBatterySerial": cfprStorageRaidBatterySerial,
       "cfprStorageRaidBatterySize": cfprStorageRaidBatterySize,
       "cfprStorageRaidBatteryTemperature": cfprStorageRaidBatteryTemperature,
       "cfprStorageRaidBatteryVendor": cfprStorageRaidBatteryVendor,
       "cfprStorageSystemTable": cfprStorageSystemTable,
       "cfprStorageSystemEntry": cfprStorageSystemEntry,
       "cfprStorageSystemInstanceId": cfprStorageSystemInstanceId,
       "cfprStorageSystemDn": cfprStorageSystemDn,
       "cfprStorageSystemRn": cfprStorageSystemRn,
       "cfprStorageSystemFsmDescr": cfprStorageSystemFsmDescr,
       "cfprStorageSystemFsmPrev": cfprStorageSystemFsmPrev,
       "cfprStorageSystemFsmProgr": cfprStorageSystemFsmProgr,
       "cfprStorageSystemFsmRmtInvErrCode": cfprStorageSystemFsmRmtInvErrCode,
       "cfprStorageSystemFsmRmtInvErrDescr": cfprStorageSystemFsmRmtInvErrDescr,
       "cfprStorageSystemFsmRmtInvRslt": cfprStorageSystemFsmRmtInvRslt,
       "cfprStorageSystemFsmStageDescr": cfprStorageSystemFsmStageDescr,
       "cfprStorageSystemFsmStamp": cfprStorageSystemFsmStamp,
       "cfprStorageSystemFsmStatus": cfprStorageSystemFsmStatus,
       "cfprStorageSystemFsmTry": cfprStorageSystemFsmTry,
       "cfprStorageSystemId": cfprStorageSystemId,
       "cfprStorageSystemName": cfprStorageSystemName,
       "cfprStorageSystemFsmTable": cfprStorageSystemFsmTable,
       "cfprStorageSystemFsmEntry": cfprStorageSystemFsmEntry,
       "cfprStorageSystemFsmInstanceId": cfprStorageSystemFsmInstanceId,
       "cfprStorageSystemFsmDn": cfprStorageSystemFsmDn,
       "cfprStorageSystemFsmRn": cfprStorageSystemFsmRn,
       "cfprStorageSystemFsmCompletionTime": cfprStorageSystemFsmCompletionTime,
       "cfprStorageSystemFsmCurrentFsm": cfprStorageSystemFsmCurrentFsm,
       "cfprStorageSystemFsmDescrData": cfprStorageSystemFsmDescrData,
       "cfprStorageSystemFsmFsmStatus": cfprStorageSystemFsmFsmStatus,
       "cfprStorageSystemFsmProgress": cfprStorageSystemFsmProgress,
       "cfprStorageSystemFsmRmtErrCode": cfprStorageSystemFsmRmtErrCode,
       "cfprStorageSystemFsmRmtErrDescr": cfprStorageSystemFsmRmtErrDescr,
       "cfprStorageSystemFsmRmtRslt": cfprStorageSystemFsmRmtRslt,
       "cfprStorageSystemFsmStageTable": cfprStorageSystemFsmStageTable,
       "cfprStorageSystemFsmStageEntry": cfprStorageSystemFsmStageEntry,
       "cfprStorageSystemFsmStageInstanceId": cfprStorageSystemFsmStageInstanceId,
       "cfprStorageSystemFsmStageDn": cfprStorageSystemFsmStageDn,
       "cfprStorageSystemFsmStageRn": cfprStorageSystemFsmStageRn,
       "cfprStorageSystemFsmStageDescrData": cfprStorageSystemFsmStageDescrData,
       "cfprStorageSystemFsmStageLastUpdateTime": cfprStorageSystemFsmStageLastUpdateTime,
       "cfprStorageSystemFsmStageName": cfprStorageSystemFsmStageName,
       "cfprStorageSystemFsmStageOrder": cfprStorageSystemFsmStageOrder,
       "cfprStorageSystemFsmStageRetry": cfprStorageSystemFsmStageRetry,
       "cfprStorageSystemFsmStageStageStatus": cfprStorageSystemFsmStageStageStatus,
       "cfprStorageSystemFsmTaskTable": cfprStorageSystemFsmTaskTable,
       "cfprStorageSystemFsmTaskEntry": cfprStorageSystemFsmTaskEntry,
       "cfprStorageSystemFsmTaskInstanceId": cfprStorageSystemFsmTaskInstanceId,
       "cfprStorageSystemFsmTaskDn": cfprStorageSystemFsmTaskDn,
       "cfprStorageSystemFsmTaskRn": cfprStorageSystemFsmTaskRn,
       "cfprStorageSystemFsmTaskCompletion": cfprStorageSystemFsmTaskCompletion,
       "cfprStorageSystemFsmTaskFlags": cfprStorageSystemFsmTaskFlags,
       "cfprStorageSystemFsmTaskItem": cfprStorageSystemFsmTaskItem,
       "cfprStorageSystemFsmTaskSeqId": cfprStorageSystemFsmTaskSeqId,
       "cfprStorageTransportableFlashModuleTable": cfprStorageTransportableFlashModuleTable,
       "cfprStorageTransportableFlashModuleEntry": cfprStorageTransportableFlashModuleEntry,
       "cfprStorageTransportableFlashModuleInstanceId": cfprStorageTransportableFlashModuleInstanceId,
       "cfprStorageTransportableFlashModuleDn": cfprStorageTransportableFlashModuleDn,
       "cfprStorageTransportableFlashModuleRn": cfprStorageTransportableFlashModuleRn,
       "cfprStorageTransportableFlashModuleBlockSize": cfprStorageTransportableFlashModuleBlockSize,
       "cfprStorageTransportableFlashModuleConnectionProtocol": cfprStorageTransportableFlashModuleConnectionProtocol,
       "cfprStorageTransportableFlashModuleId": cfprStorageTransportableFlashModuleId,
       "cfprStorageTransportableFlashModuleModel": cfprStorageTransportableFlashModuleModel,
       "cfprStorageTransportableFlashModuleNumberOfBlocks": cfprStorageTransportableFlashModuleNumberOfBlocks,
       "cfprStorageTransportableFlashModuleOperQualifierReason": cfprStorageTransportableFlashModuleOperQualifierReason,
       "cfprStorageTransportableFlashModuleOperability": cfprStorageTransportableFlashModuleOperability,
       "cfprStorageTransportableFlashModulePresence": cfprStorageTransportableFlashModulePresence,
       "cfprStorageTransportableFlashModuleRevision": cfprStorageTransportableFlashModuleRevision,
       "cfprStorageTransportableFlashModuleSerial": cfprStorageTransportableFlashModuleSerial,
       "cfprStorageTransportableFlashModuleSize": cfprStorageTransportableFlashModuleSize,
       "cfprStorageTransportableFlashModuleVendor": cfprStorageTransportableFlashModuleVendor,
       "cfprStorageVirtualDriveTable": cfprStorageVirtualDriveTable,
       "cfprStorageVirtualDriveEntry": cfprStorageVirtualDriveEntry,
       "cfprStorageVirtualDriveInstanceId": cfprStorageVirtualDriveInstanceId,
       "cfprStorageVirtualDriveDn": cfprStorageVirtualDriveDn,
       "cfprStorageVirtualDriveRn": cfprStorageVirtualDriveRn,
       "cfprStorageVirtualDriveAccessPolicy": cfprStorageVirtualDriveAccessPolicy,
       "cfprStorageVirtualDriveActualWriteCachePolicy": cfprStorageVirtualDriveActualWriteCachePolicy,
       "cfprStorageVirtualDriveBlockSize": cfprStorageVirtualDriveBlockSize,
       "cfprStorageVirtualDriveBootable": cfprStorageVirtualDriveBootable,
       "cfprStorageVirtualDriveConfiguredWriteCachePolicy": cfprStorageVirtualDriveConfiguredWriteCachePolicy,
       "cfprStorageVirtualDriveConnectionProtocol": cfprStorageVirtualDriveConnectionProtocol,
       "cfprStorageVirtualDriveDriveCache": cfprStorageVirtualDriveDriveCache,
       "cfprStorageVirtualDriveDriveState": cfprStorageVirtualDriveDriveState,
       "cfprStorageVirtualDriveId": cfprStorageVirtualDriveId,
       "cfprStorageVirtualDriveIoPolicy": cfprStorageVirtualDriveIoPolicy,
       "cfprStorageVirtualDriveLc": cfprStorageVirtualDriveLc,
       "cfprStorageVirtualDriveModel": cfprStorageVirtualDriveModel,
       "cfprStorageVirtualDriveNumberOfBlocks": cfprStorageVirtualDriveNumberOfBlocks,
       "cfprStorageVirtualDriveOperQualifierReason": cfprStorageVirtualDriveOperQualifierReason,
       "cfprStorageVirtualDriveOperability": cfprStorageVirtualDriveOperability,
       "cfprStorageVirtualDrivePresence": cfprStorageVirtualDrivePresence,
       "cfprStorageVirtualDriveReadPolicy": cfprStorageVirtualDriveReadPolicy,
       "cfprStorageVirtualDriveRevision": cfprStorageVirtualDriveRevision,
       "cfprStorageVirtualDriveSerial": cfprStorageVirtualDriveSerial,
       "cfprStorageVirtualDriveSize": cfprStorageVirtualDriveSize,
       "cfprStorageVirtualDriveStripSize": cfprStorageVirtualDriveStripSize,
       "cfprStorageVirtualDriveType": cfprStorageVirtualDriveType,
       "cfprStorageVirtualDriveVendor": cfprStorageVirtualDriveVendor,
       "cfprStorageVsanRefTable": cfprStorageVsanRefTable,
       "cfprStorageVsanRefEntry": cfprStorageVsanRefEntry,
       "cfprStorageVsanRefInstanceId": cfprStorageVsanRefInstanceId,
       "cfprStorageVsanRefDn": cfprStorageVsanRefDn,
       "cfprStorageVsanRefRn": cfprStorageVsanRefRn,
       "cfprStorageVsanRefConfigQualifier": cfprStorageVsanRefConfigQualifier,
       "cfprStorageVsanRefName": cfprStorageVsanRefName,
       "cfprStorageVsanRefOperVnetDn": cfprStorageVsanRefOperVnetDn,
       "cfprStorageVsanRefOperVnetName": cfprStorageVsanRefOperVnetName,
       "cfprStorageVsanRefSwitchId": cfprStorageVsanRefSwitchId,
       "cfprStorageVsanRefVnet": cfprStorageVsanRefVnet,
       "cfprStorageVsanRefZoningState": cfprStorageVsanRefZoningState}
)
