# SNMP MIB module (CISCO-FIREPOWER-AP-STORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-STORAGE-MIB.mib
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

(CfprApAaaConfigState,
 CfprApConditionRemoteInvRslt,
 CfprApEquipmentOperability,
 CfprApEquipmentPowerState,
 CfprApEquipmentPresence,
 CfprApEquipmentSensorThresholdStatus,
 CfprApFabricZoningState,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApFsmLifecycle,
 CfprApPolicyPolicyOwner,
 CfprApStorageAccessType,
 CfprApStorageActualWriteType,
 CfprApStorageBatteryType,
 CfprApStorageBbuStatus,
 CfprApStorageBootableType,
 CfprApStorageCacheType,
 CfprApStorageConfiguration,
 CfprApStorageConfiguredWriteType,
 CfprApStorageConnectionProtocol,
 CfprApStorageControllerFaultMonitoring,
 CfprApStorageControllerId,
 CfprApStorageControllerStatus,
 CfprApStorageControllerType,
 CfprApStorageDisklessAction,
 CfprApStorageEpAccess,
 CfprApStorageEtherIfVlanType,
 CfprApStorageFFCardHealth,
 CfprApStorageFFCardMode,
 CfprApStorageFFCardSizeMismatch,
 CfprApStorageFFCardState,
 CfprApStorageFFCardSync,
 CfprApStorageFFCardWriteEnable,
 CfprApStorageFFControllerHealth,
 CfprApStorageFFControllerState,
 CfprApStorageFFDriveRemovable,
 CfprApStorageFFDriveState,
 CfprApStorageFFDriveType,
 CfprApStorageFFDriveVisible,
 CfprApStorageFFFormatRunning,
 CfprApStorageFFHasError,
 CfprApStorageFFRAIDHealth,
 CfprApStorageFFRAIDState,
 CfprApStorageFFRWType,
 CfprApStorageFFRaidSyncSupport,
 CfprApStorageFFSlotENUM,
 CfprApStorageFFType,
 CfprApStorageFileSystemStatus,
 CfprApStorageFlexFlashControllerId,
 CfprApStorageIOType,
 CfprApStorageKeyType,
 CfprApStorageLearnCycleRequested,
 CfprApStorageLearnMode,
 CfprApStorageLinkSpeed,
 CfprApStorageLocalDiskConfigFlexFlashRAIDReportingState,
 CfprApStorageLocalDiskConfigFlexFlashState,
 CfprApStorageLocalDiskMode,
 CfprApStorageLocalDiskPartitionType,
 CfprApStorageLunType,
 CfprApStorageOperatingModeType,
 CfprApStorageOperationRequestType,
 CfprApStorageOperationState,
 CfprApStorageOperationStateType,
 CfprApStorageOperationType,
 CfprApStoragePDriveStatus,
 CfprApStoragePowerState,
 CfprApStorageProtocol,
 CfprApStorageRaidBatteryOperabilityQualifier,
 CfprApStorageReadType,
 CfprApStorageSystemFsmCurrentFsm,
 CfprApStorageSystemFsmStageName,
 CfprApStorageSystemFsmTaskItem,
 CfprApStorageTechnology,
 CfprApStorageVDriveState,
 CfprApStorageVsanRefSwitchId,
 CfprApVnicConfigIssues) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApAaaConfigState",
    "CfprApConditionRemoteInvRslt",
    "CfprApEquipmentOperability",
    "CfprApEquipmentPowerState",
    "CfprApEquipmentPresence",
    "CfprApEquipmentSensorThresholdStatus",
    "CfprApFabricZoningState",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApFsmLifecycle",
    "CfprApPolicyPolicyOwner",
    "CfprApStorageAccessType",
    "CfprApStorageActualWriteType",
    "CfprApStorageBatteryType",
    "CfprApStorageBbuStatus",
    "CfprApStorageBootableType",
    "CfprApStorageCacheType",
    "CfprApStorageConfiguration",
    "CfprApStorageConfiguredWriteType",
    "CfprApStorageConnectionProtocol",
    "CfprApStorageControllerFaultMonitoring",
    "CfprApStorageControllerId",
    "CfprApStorageControllerStatus",
    "CfprApStorageControllerType",
    "CfprApStorageDisklessAction",
    "CfprApStorageEpAccess",
    "CfprApStorageEtherIfVlanType",
    "CfprApStorageFFCardHealth",
    "CfprApStorageFFCardMode",
    "CfprApStorageFFCardSizeMismatch",
    "CfprApStorageFFCardState",
    "CfprApStorageFFCardSync",
    "CfprApStorageFFCardWriteEnable",
    "CfprApStorageFFControllerHealth",
    "CfprApStorageFFControllerState",
    "CfprApStorageFFDriveRemovable",
    "CfprApStorageFFDriveState",
    "CfprApStorageFFDriveType",
    "CfprApStorageFFDriveVisible",
    "CfprApStorageFFFormatRunning",
    "CfprApStorageFFHasError",
    "CfprApStorageFFRAIDHealth",
    "CfprApStorageFFRAIDState",
    "CfprApStorageFFRWType",
    "CfprApStorageFFRaidSyncSupport",
    "CfprApStorageFFSlotENUM",
    "CfprApStorageFFType",
    "CfprApStorageFileSystemStatus",
    "CfprApStorageFlexFlashControllerId",
    "CfprApStorageIOType",
    "CfprApStorageKeyType",
    "CfprApStorageLearnCycleRequested",
    "CfprApStorageLearnMode",
    "CfprApStorageLinkSpeed",
    "CfprApStorageLocalDiskConfigFlexFlashRAIDReportingState",
    "CfprApStorageLocalDiskConfigFlexFlashState",
    "CfprApStorageLocalDiskMode",
    "CfprApStorageLocalDiskPartitionType",
    "CfprApStorageLunType",
    "CfprApStorageOperatingModeType",
    "CfprApStorageOperationRequestType",
    "CfprApStorageOperationState",
    "CfprApStorageOperationStateType",
    "CfprApStorageOperationType",
    "CfprApStoragePDriveStatus",
    "CfprApStoragePowerState",
    "CfprApStorageProtocol",
    "CfprApStorageRaidBatteryOperabilityQualifier",
    "CfprApStorageReadType",
    "CfprApStorageSystemFsmCurrentFsm",
    "CfprApStorageSystemFsmStageName",
    "CfprApStorageSystemFsmTaskItem",
    "CfprApStorageTechnology",
    "CfprApStorageVDriveState",
    "CfprApStorageVsanRefSwitchId",
    "CfprApVnicConfigIssues")

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

cfprApStorageObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApStorageAuthKeyTable_Object = MibTable
cfprApStorageAuthKeyTable = _CfprApStorageAuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1)
)
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyTable.setStatus("current")
_CfprApStorageAuthKeyEntry_Object = MibTableRow
cfprApStorageAuthKeyEntry = _CfprApStorageAuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1, 1)
)
cfprApStorageAuthKeyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageAuthKeyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyEntry.setStatus("current")
_CfprApStorageAuthKeyInstanceId_Type = CfprApManagedObjectId
_CfprApStorageAuthKeyInstanceId_Object = MibTableColumn
cfprApStorageAuthKeyInstanceId = _CfprApStorageAuthKeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1, 1, 1),
    _CfprApStorageAuthKeyInstanceId_Type()
)
cfprApStorageAuthKeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyInstanceId.setStatus("current")
_CfprApStorageAuthKeyDn_Type = CfprApManagedObjectDn
_CfprApStorageAuthKeyDn_Object = MibTableColumn
cfprApStorageAuthKeyDn = _CfprApStorageAuthKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1, 1, 2),
    _CfprApStorageAuthKeyDn_Type()
)
cfprApStorageAuthKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyDn.setStatus("current")
_CfprApStorageAuthKeyRn_Type = SnmpAdminString
_CfprApStorageAuthKeyRn_Object = MibTableColumn
cfprApStorageAuthKeyRn = _CfprApStorageAuthKeyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1, 1, 3),
    _CfprApStorageAuthKeyRn_Type()
)
cfprApStorageAuthKeyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyRn.setStatus("current")
_CfprApStorageAuthKeyDescr_Type = SnmpAdminString
_CfprApStorageAuthKeyDescr_Object = MibTableColumn
cfprApStorageAuthKeyDescr = _CfprApStorageAuthKeyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1, 1, 4),
    _CfprApStorageAuthKeyDescr_Type()
)
cfprApStorageAuthKeyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyDescr.setStatus("current")
_CfprApStorageAuthKeyIntId_Type = SnmpAdminString
_CfprApStorageAuthKeyIntId_Object = MibTableColumn
cfprApStorageAuthKeyIntId = _CfprApStorageAuthKeyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1, 1, 5),
    _CfprApStorageAuthKeyIntId_Type()
)
cfprApStorageAuthKeyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyIntId.setStatus("current")
_CfprApStorageAuthKeyName_Type = SnmpAdminString
_CfprApStorageAuthKeyName_Object = MibTableColumn
cfprApStorageAuthKeyName = _CfprApStorageAuthKeyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1, 1, 6),
    _CfprApStorageAuthKeyName_Type()
)
cfprApStorageAuthKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyName.setStatus("current")
_CfprApStorageAuthKeyPassword_Type = SnmpAdminString
_CfprApStorageAuthKeyPassword_Object = MibTableColumn
cfprApStorageAuthKeyPassword = _CfprApStorageAuthKeyPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1, 1, 7),
    _CfprApStorageAuthKeyPassword_Type()
)
cfprApStorageAuthKeyPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyPassword.setStatus("current")
_CfprApStorageAuthKeyPolicyLevel_Type = Gauge32
_CfprApStorageAuthKeyPolicyLevel_Object = MibTableColumn
cfprApStorageAuthKeyPolicyLevel = _CfprApStorageAuthKeyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1, 1, 8),
    _CfprApStorageAuthKeyPolicyLevel_Type()
)
cfprApStorageAuthKeyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyPolicyLevel.setStatus("current")
_CfprApStorageAuthKeyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApStorageAuthKeyPolicyOwner_Object = MibTableColumn
cfprApStorageAuthKeyPolicyOwner = _CfprApStorageAuthKeyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1, 1, 9),
    _CfprApStorageAuthKeyPolicyOwner_Type()
)
cfprApStorageAuthKeyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyPolicyOwner.setStatus("current")
_CfprApStorageAuthKeyType_Type = CfprApStorageKeyType
_CfprApStorageAuthKeyType_Object = MibTableColumn
cfprApStorageAuthKeyType = _CfprApStorageAuthKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1, 1, 10),
    _CfprApStorageAuthKeyType_Type()
)
cfprApStorageAuthKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyType.setStatus("current")
_CfprApStorageAuthKeyUserId_Type = SnmpAdminString
_CfprApStorageAuthKeyUserId_Object = MibTableColumn
cfprApStorageAuthKeyUserId = _CfprApStorageAuthKeyUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 1, 1, 11),
    _CfprApStorageAuthKeyUserId_Type()
)
cfprApStorageAuthKeyUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageAuthKeyUserId.setStatus("current")
_CfprApStorageControllerTable_Object = MibTable
cfprApStorageControllerTable = _CfprApStorageControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4)
)
if mibBuilder.loadTexts:
    cfprApStorageControllerTable.setStatus("current")
_CfprApStorageControllerEntry_Object = MibTableRow
cfprApStorageControllerEntry = _CfprApStorageControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1)
)
cfprApStorageControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageControllerEntry.setStatus("current")
_CfprApStorageControllerInstanceId_Type = CfprApManagedObjectId
_CfprApStorageControllerInstanceId_Object = MibTableColumn
cfprApStorageControllerInstanceId = _CfprApStorageControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 1),
    _CfprApStorageControllerInstanceId_Type()
)
cfprApStorageControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageControllerInstanceId.setStatus("current")
_CfprApStorageControllerDn_Type = CfprApManagedObjectDn
_CfprApStorageControllerDn_Object = MibTableColumn
cfprApStorageControllerDn = _CfprApStorageControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 2),
    _CfprApStorageControllerDn_Type()
)
cfprApStorageControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerDn.setStatus("current")
_CfprApStorageControllerRn_Type = SnmpAdminString
_CfprApStorageControllerRn_Object = MibTableColumn
cfprApStorageControllerRn = _CfprApStorageControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 3),
    _CfprApStorageControllerRn_Type()
)
cfprApStorageControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerRn.setStatus("current")
_CfprApStorageControllerControllerStatus_Type = CfprApStorageControllerStatus
_CfprApStorageControllerControllerStatus_Object = MibTableColumn
cfprApStorageControllerControllerStatus = _CfprApStorageControllerControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 4),
    _CfprApStorageControllerControllerStatus_Type()
)
cfprApStorageControllerControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerControllerStatus.setStatus("current")
_CfprApStorageControllerDeviceRaidSupport_Type = SnmpAdminString
_CfprApStorageControllerDeviceRaidSupport_Object = MibTableColumn
cfprApStorageControllerDeviceRaidSupport = _CfprApStorageControllerDeviceRaidSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 5),
    _CfprApStorageControllerDeviceRaidSupport_Type()
)
cfprApStorageControllerDeviceRaidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerDeviceRaidSupport.setStatus("current")
_CfprApStorageControllerFaultMonitoring_Type = CfprApStorageControllerFaultMonitoring
_CfprApStorageControllerFaultMonitoring_Object = MibTableColumn
cfprApStorageControllerFaultMonitoring = _CfprApStorageControllerFaultMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 6),
    _CfprApStorageControllerFaultMonitoring_Type()
)
cfprApStorageControllerFaultMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerFaultMonitoring.setStatus("current")
_CfprApStorageControllerHwRevision_Type = SnmpAdminString
_CfprApStorageControllerHwRevision_Object = MibTableColumn
cfprApStorageControllerHwRevision = _CfprApStorageControllerHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 7),
    _CfprApStorageControllerHwRevision_Type()
)
cfprApStorageControllerHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerHwRevision.setStatus("current")
_CfprApStorageControllerId_Type = CfprApStorageControllerId
_CfprApStorageControllerId_Object = MibTableColumn
cfprApStorageControllerId = _CfprApStorageControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 8),
    _CfprApStorageControllerId_Type()
)
cfprApStorageControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerId.setStatus("current")
_CfprApStorageControllerLc_Type = CfprApFsmLifecycle
_CfprApStorageControllerLc_Object = MibTableColumn
cfprApStorageControllerLc = _CfprApStorageControllerLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 9),
    _CfprApStorageControllerLc_Type()
)
cfprApStorageControllerLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerLc.setStatus("current")
_CfprApStorageControllerLocationDn_Type = SnmpAdminString
_CfprApStorageControllerLocationDn_Object = MibTableColumn
cfprApStorageControllerLocationDn = _CfprApStorageControllerLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 10),
    _CfprApStorageControllerLocationDn_Type()
)
cfprApStorageControllerLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerLocationDn.setStatus("current")
_CfprApStorageControllerModel_Type = SnmpAdminString
_CfprApStorageControllerModel_Object = MibTableColumn
cfprApStorageControllerModel = _CfprApStorageControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 11),
    _CfprApStorageControllerModel_Type()
)
cfprApStorageControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerModel.setStatus("current")
_CfprApStorageControllerOobControllerId_Type = Gauge32
_CfprApStorageControllerOobControllerId_Object = MibTableColumn
cfprApStorageControllerOobControllerId = _CfprApStorageControllerOobControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 12),
    _CfprApStorageControllerOobControllerId_Type()
)
cfprApStorageControllerOobControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerOobControllerId.setStatus("current")
_CfprApStorageControllerOobInterfaceSupported_Type = TruthValue
_CfprApStorageControllerOobInterfaceSupported_Object = MibTableColumn
cfprApStorageControllerOobInterfaceSupported = _CfprApStorageControllerOobInterfaceSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 13),
    _CfprApStorageControllerOobInterfaceSupported_Type()
)
cfprApStorageControllerOobInterfaceSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerOobInterfaceSupported.setStatus("current")
_CfprApStorageControllerOperQualifierReason_Type = SnmpAdminString
_CfprApStorageControllerOperQualifierReason_Object = MibTableColumn
cfprApStorageControllerOperQualifierReason = _CfprApStorageControllerOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 14),
    _CfprApStorageControllerOperQualifierReason_Type()
)
cfprApStorageControllerOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerOperQualifierReason.setStatus("current")
_CfprApStorageControllerOperState_Type = CfprApEquipmentOperability
_CfprApStorageControllerOperState_Object = MibTableColumn
cfprApStorageControllerOperState = _CfprApStorageControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 15),
    _CfprApStorageControllerOperState_Type()
)
cfprApStorageControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerOperState.setStatus("current")
_CfprApStorageControllerOperability_Type = CfprApEquipmentOperability
_CfprApStorageControllerOperability_Object = MibTableColumn
cfprApStorageControllerOperability = _CfprApStorageControllerOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 16),
    _CfprApStorageControllerOperability_Type()
)
cfprApStorageControllerOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerOperability.setStatus("current")
_CfprApStorageControllerPartNumber_Type = SnmpAdminString
_CfprApStorageControllerPartNumber_Object = MibTableColumn
cfprApStorageControllerPartNumber = _CfprApStorageControllerPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 17),
    _CfprApStorageControllerPartNumber_Type()
)
cfprApStorageControllerPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerPartNumber.setStatus("current")
_CfprApStorageControllerPciAddr_Type = SnmpAdminString
_CfprApStorageControllerPciAddr_Object = MibTableColumn
cfprApStorageControllerPciAddr = _CfprApStorageControllerPciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 18),
    _CfprApStorageControllerPciAddr_Type()
)
cfprApStorageControllerPciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerPciAddr.setStatus("current")
_CfprApStorageControllerPciSlot_Type = SnmpAdminString
_CfprApStorageControllerPciSlot_Object = MibTableColumn
cfprApStorageControllerPciSlot = _CfprApStorageControllerPciSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 19),
    _CfprApStorageControllerPciSlot_Type()
)
cfprApStorageControllerPciSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerPciSlot.setStatus("current")
_CfprApStorageControllerPerf_Type = CfprApEquipmentSensorThresholdStatus
_CfprApStorageControllerPerf_Object = MibTableColumn
cfprApStorageControllerPerf = _CfprApStorageControllerPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 20),
    _CfprApStorageControllerPerf_Type()
)
cfprApStorageControllerPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerPerf.setStatus("current")
_CfprApStorageControllerPower_Type = CfprApEquipmentPowerState
_CfprApStorageControllerPower_Object = MibTableColumn
cfprApStorageControllerPower = _CfprApStorageControllerPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 21),
    _CfprApStorageControllerPower_Type()
)
cfprApStorageControllerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerPower.setStatus("current")
_CfprApStorageControllerPresence_Type = CfprApEquipmentPresence
_CfprApStorageControllerPresence_Object = MibTableColumn
cfprApStorageControllerPresence = _CfprApStorageControllerPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 22),
    _CfprApStorageControllerPresence_Type()
)
cfprApStorageControllerPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerPresence.setStatus("current")
_CfprApStorageControllerRaidSupport_Type = SnmpAdminString
_CfprApStorageControllerRaidSupport_Object = MibTableColumn
cfprApStorageControllerRaidSupport = _CfprApStorageControllerRaidSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 23),
    _CfprApStorageControllerRaidSupport_Type()
)
cfprApStorageControllerRaidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerRaidSupport.setStatus("current")
_CfprApStorageControllerRebuildRate_Type = Gauge32
_CfprApStorageControllerRebuildRate_Object = MibTableColumn
cfprApStorageControllerRebuildRate = _CfprApStorageControllerRebuildRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 24),
    _CfprApStorageControllerRebuildRate_Type()
)
cfprApStorageControllerRebuildRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerRebuildRate.setStatus("current")
_CfprApStorageControllerRevision_Type = SnmpAdminString
_CfprApStorageControllerRevision_Object = MibTableColumn
cfprApStorageControllerRevision = _CfprApStorageControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 25),
    _CfprApStorageControllerRevision_Type()
)
cfprApStorageControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerRevision.setStatus("current")
_CfprApStorageControllerSerial_Type = SnmpAdminString
_CfprApStorageControllerSerial_Object = MibTableColumn
cfprApStorageControllerSerial = _CfprApStorageControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 26),
    _CfprApStorageControllerSerial_Type()
)
cfprApStorageControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerSerial.setStatus("current")
_CfprApStorageControllerThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApStorageControllerThermal_Object = MibTableColumn
cfprApStorageControllerThermal = _CfprApStorageControllerThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 27),
    _CfprApStorageControllerThermal_Type()
)
cfprApStorageControllerThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerThermal.setStatus("current")
_CfprApStorageControllerType_Type = CfprApStorageControllerType
_CfprApStorageControllerType_Object = MibTableColumn
cfprApStorageControllerType = _CfprApStorageControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 28),
    _CfprApStorageControllerType_Type()
)
cfprApStorageControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerType.setStatus("current")
_CfprApStorageControllerVendor_Type = SnmpAdminString
_CfprApStorageControllerVendor_Object = MibTableColumn
cfprApStorageControllerVendor = _CfprApStorageControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 29),
    _CfprApStorageControllerVendor_Type()
)
cfprApStorageControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerVendor.setStatus("current")
_CfprApStorageControllerVid_Type = SnmpAdminString
_CfprApStorageControllerVid_Object = MibTableColumn
cfprApStorageControllerVid = _CfprApStorageControllerVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 30),
    _CfprApStorageControllerVid_Type()
)
cfprApStorageControllerVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerVid.setStatus("current")
_CfprApStorageControllerVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApStorageControllerVoltage_Object = MibTableColumn
cfprApStorageControllerVoltage = _CfprApStorageControllerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 4, 1, 31),
    _CfprApStorageControllerVoltage_Type()
)
cfprApStorageControllerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageControllerVoltage.setStatus("current")
_CfprApStorageDomainEpTable_Object = MibTable
cfprApStorageDomainEpTable = _CfprApStorageDomainEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 5)
)
if mibBuilder.loadTexts:
    cfprApStorageDomainEpTable.setStatus("current")
_CfprApStorageDomainEpEntry_Object = MibTableRow
cfprApStorageDomainEpEntry = _CfprApStorageDomainEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 5, 1)
)
cfprApStorageDomainEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageDomainEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageDomainEpEntry.setStatus("current")
_CfprApStorageDomainEpInstanceId_Type = CfprApManagedObjectId
_CfprApStorageDomainEpInstanceId_Object = MibTableColumn
cfprApStorageDomainEpInstanceId = _CfprApStorageDomainEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 5, 1, 1),
    _CfprApStorageDomainEpInstanceId_Type()
)
cfprApStorageDomainEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageDomainEpInstanceId.setStatus("current")
_CfprApStorageDomainEpDn_Type = CfprApManagedObjectDn
_CfprApStorageDomainEpDn_Object = MibTableColumn
cfprApStorageDomainEpDn = _CfprApStorageDomainEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 5, 1, 2),
    _CfprApStorageDomainEpDn_Type()
)
cfprApStorageDomainEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageDomainEpDn.setStatus("current")
_CfprApStorageDomainEpRn_Type = SnmpAdminString
_CfprApStorageDomainEpRn_Object = MibTableColumn
cfprApStorageDomainEpRn = _CfprApStorageDomainEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 5, 1, 3),
    _CfprApStorageDomainEpRn_Type()
)
cfprApStorageDomainEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageDomainEpRn.setStatus("current")
_CfprApStorageDriveTable_Object = MibTable
cfprApStorageDriveTable = _CfprApStorageDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 6)
)
if mibBuilder.loadTexts:
    cfprApStorageDriveTable.setStatus("current")
_CfprApStorageDriveEntry_Object = MibTableRow
cfprApStorageDriveEntry = _CfprApStorageDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 6, 1)
)
cfprApStorageDriveEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageDriveInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageDriveEntry.setStatus("current")
_CfprApStorageDriveInstanceId_Type = CfprApManagedObjectId
_CfprApStorageDriveInstanceId_Object = MibTableColumn
cfprApStorageDriveInstanceId = _CfprApStorageDriveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 6, 1, 1),
    _CfprApStorageDriveInstanceId_Type()
)
cfprApStorageDriveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageDriveInstanceId.setStatus("current")
_CfprApStorageDriveDn_Type = CfprApManagedObjectDn
_CfprApStorageDriveDn_Object = MibTableColumn
cfprApStorageDriveDn = _CfprApStorageDriveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 6, 1, 2),
    _CfprApStorageDriveDn_Type()
)
cfprApStorageDriveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageDriveDn.setStatus("current")
_CfprApStorageDriveRn_Type = SnmpAdminString
_CfprApStorageDriveRn_Object = MibTableColumn
cfprApStorageDriveRn = _CfprApStorageDriveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 6, 1, 3),
    _CfprApStorageDriveRn_Type()
)
cfprApStorageDriveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageDriveRn.setStatus("current")
_CfprApStorageDriveId_Type = Gauge32
_CfprApStorageDriveId_Object = MibTableColumn
cfprApStorageDriveId = _CfprApStorageDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 6, 1, 4),
    _CfprApStorageDriveId_Type()
)
cfprApStorageDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageDriveId.setStatus("current")
_CfprApStorageDriveModel_Type = SnmpAdminString
_CfprApStorageDriveModel_Object = MibTableColumn
cfprApStorageDriveModel = _CfprApStorageDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 6, 1, 5),
    _CfprApStorageDriveModel_Type()
)
cfprApStorageDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageDriveModel.setStatus("current")
_CfprApStorageDrivePciAddr_Type = SnmpAdminString
_CfprApStorageDrivePciAddr_Object = MibTableColumn
cfprApStorageDrivePciAddr = _CfprApStorageDrivePciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 6, 1, 6),
    _CfprApStorageDrivePciAddr_Type()
)
cfprApStorageDrivePciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageDrivePciAddr.setStatus("current")
_CfprApStorageDriveRevision_Type = SnmpAdminString
_CfprApStorageDriveRevision_Object = MibTableColumn
cfprApStorageDriveRevision = _CfprApStorageDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 6, 1, 7),
    _CfprApStorageDriveRevision_Type()
)
cfprApStorageDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageDriveRevision.setStatus("current")
_CfprApStorageDriveSerial_Type = SnmpAdminString
_CfprApStorageDriveSerial_Object = MibTableColumn
cfprApStorageDriveSerial = _CfprApStorageDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 6, 1, 8),
    _CfprApStorageDriveSerial_Type()
)
cfprApStorageDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageDriveSerial.setStatus("current")
_CfprApStorageDriveVendor_Type = SnmpAdminString
_CfprApStorageDriveVendor_Object = MibTableColumn
cfprApStorageDriveVendor = _CfprApStorageDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 6, 1, 9),
    _CfprApStorageDriveVendor_Type()
)
cfprApStorageDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageDriveVendor.setStatus("current")
_CfprApStorageEnclosureTable_Object = MibTable
cfprApStorageEnclosureTable = _CfprApStorageEnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 7)
)
if mibBuilder.loadTexts:
    cfprApStorageEnclosureTable.setStatus("current")
_CfprApStorageEnclosureEntry_Object = MibTableRow
cfprApStorageEnclosureEntry = _CfprApStorageEnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 7, 1)
)
cfprApStorageEnclosureEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageEnclosureInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageEnclosureEntry.setStatus("current")
_CfprApStorageEnclosureInstanceId_Type = CfprApManagedObjectId
_CfprApStorageEnclosureInstanceId_Object = MibTableColumn
cfprApStorageEnclosureInstanceId = _CfprApStorageEnclosureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 7, 1, 1),
    _CfprApStorageEnclosureInstanceId_Type()
)
cfprApStorageEnclosureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageEnclosureInstanceId.setStatus("current")
_CfprApStorageEnclosureDn_Type = CfprApManagedObjectDn
_CfprApStorageEnclosureDn_Object = MibTableColumn
cfprApStorageEnclosureDn = _CfprApStorageEnclosureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 7, 1, 2),
    _CfprApStorageEnclosureDn_Type()
)
cfprApStorageEnclosureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEnclosureDn.setStatus("current")
_CfprApStorageEnclosureRn_Type = SnmpAdminString
_CfprApStorageEnclosureRn_Object = MibTableColumn
cfprApStorageEnclosureRn = _CfprApStorageEnclosureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 7, 1, 3),
    _CfprApStorageEnclosureRn_Type()
)
cfprApStorageEnclosureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEnclosureRn.setStatus("current")
_CfprApStorageEnclosureId_Type = Gauge32
_CfprApStorageEnclosureId_Object = MibTableColumn
cfprApStorageEnclosureId = _CfprApStorageEnclosureId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 7, 1, 4),
    _CfprApStorageEnclosureId_Type()
)
cfprApStorageEnclosureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEnclosureId.setStatus("current")
_CfprApStorageEnclosureLc_Type = CfprApFsmLifecycle
_CfprApStorageEnclosureLc_Object = MibTableColumn
cfprApStorageEnclosureLc = _CfprApStorageEnclosureLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 7, 1, 5),
    _CfprApStorageEnclosureLc_Type()
)
cfprApStorageEnclosureLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEnclosureLc.setStatus("current")
_CfprApStorageEnclosureModel_Type = SnmpAdminString
_CfprApStorageEnclosureModel_Object = MibTableColumn
cfprApStorageEnclosureModel = _CfprApStorageEnclosureModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 7, 1, 6),
    _CfprApStorageEnclosureModel_Type()
)
cfprApStorageEnclosureModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEnclosureModel.setStatus("current")
_CfprApStorageEnclosureNumSlots_Type = Gauge32
_CfprApStorageEnclosureNumSlots_Object = MibTableColumn
cfprApStorageEnclosureNumSlots = _CfprApStorageEnclosureNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 7, 1, 7),
    _CfprApStorageEnclosureNumSlots_Type()
)
cfprApStorageEnclosureNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEnclosureNumSlots.setStatus("current")
_CfprApStorageEnclosureRevision_Type = SnmpAdminString
_CfprApStorageEnclosureRevision_Object = MibTableColumn
cfprApStorageEnclosureRevision = _CfprApStorageEnclosureRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 7, 1, 8),
    _CfprApStorageEnclosureRevision_Type()
)
cfprApStorageEnclosureRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEnclosureRevision.setStatus("current")
_CfprApStorageEnclosureSerial_Type = SnmpAdminString
_CfprApStorageEnclosureSerial_Object = MibTableColumn
cfprApStorageEnclosureSerial = _CfprApStorageEnclosureSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 7, 1, 9),
    _CfprApStorageEnclosureSerial_Type()
)
cfprApStorageEnclosureSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEnclosureSerial.setStatus("current")
_CfprApStorageEnclosureVendor_Type = SnmpAdminString
_CfprApStorageEnclosureVendor_Object = MibTableColumn
cfprApStorageEnclosureVendor = _CfprApStorageEnclosureVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 7, 1, 10),
    _CfprApStorageEnclosureVendor_Type()
)
cfprApStorageEnclosureVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEnclosureVendor.setStatus("current")
_CfprApStorageEpUserTable_Object = MibTable
cfprApStorageEpUserTable = _CfprApStorageEpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8)
)
if mibBuilder.loadTexts:
    cfprApStorageEpUserTable.setStatus("current")
_CfprApStorageEpUserEntry_Object = MibTableRow
cfprApStorageEpUserEntry = _CfprApStorageEpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8, 1)
)
cfprApStorageEpUserEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageEpUserInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageEpUserEntry.setStatus("current")
_CfprApStorageEpUserInstanceId_Type = CfprApManagedObjectId
_CfprApStorageEpUserInstanceId_Object = MibTableColumn
cfprApStorageEpUserInstanceId = _CfprApStorageEpUserInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8, 1, 1),
    _CfprApStorageEpUserInstanceId_Type()
)
cfprApStorageEpUserInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageEpUserInstanceId.setStatus("current")
_CfprApStorageEpUserDn_Type = CfprApManagedObjectDn
_CfprApStorageEpUserDn_Object = MibTableColumn
cfprApStorageEpUserDn = _CfprApStorageEpUserDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8, 1, 2),
    _CfprApStorageEpUserDn_Type()
)
cfprApStorageEpUserDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEpUserDn.setStatus("current")
_CfprApStorageEpUserRn_Type = SnmpAdminString
_CfprApStorageEpUserRn_Object = MibTableColumn
cfprApStorageEpUserRn = _CfprApStorageEpUserRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8, 1, 3),
    _CfprApStorageEpUserRn_Type()
)
cfprApStorageEpUserRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEpUserRn.setStatus("current")
_CfprApStorageEpUserConfigState_Type = CfprApAaaConfigState
_CfprApStorageEpUserConfigState_Object = MibTableColumn
cfprApStorageEpUserConfigState = _CfprApStorageEpUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8, 1, 4),
    _CfprApStorageEpUserConfigState_Type()
)
cfprApStorageEpUserConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEpUserConfigState.setStatus("current")
_CfprApStorageEpUserConfigStatusMessage_Type = SnmpAdminString
_CfprApStorageEpUserConfigStatusMessage_Object = MibTableColumn
cfprApStorageEpUserConfigStatusMessage = _CfprApStorageEpUserConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8, 1, 5),
    _CfprApStorageEpUserConfigStatusMessage_Type()
)
cfprApStorageEpUserConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEpUserConfigStatusMessage.setStatus("current")
_CfprApStorageEpUserDescr_Type = SnmpAdminString
_CfprApStorageEpUserDescr_Object = MibTableColumn
cfprApStorageEpUserDescr = _CfprApStorageEpUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8, 1, 6),
    _CfprApStorageEpUserDescr_Type()
)
cfprApStorageEpUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEpUserDescr.setStatus("current")
_CfprApStorageEpUserDomain_Type = SnmpAdminString
_CfprApStorageEpUserDomain_Object = MibTableColumn
cfprApStorageEpUserDomain = _CfprApStorageEpUserDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8, 1, 7),
    _CfprApStorageEpUserDomain_Type()
)
cfprApStorageEpUserDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEpUserDomain.setStatus("current")
_CfprApStorageEpUserName_Type = SnmpAdminString
_CfprApStorageEpUserName_Object = MibTableColumn
cfprApStorageEpUserName = _CfprApStorageEpUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8, 1, 8),
    _CfprApStorageEpUserName_Type()
)
cfprApStorageEpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEpUserName.setStatus("current")
_CfprApStorageEpUserPriv_Type = CfprApStorageEpAccess
_CfprApStorageEpUserPriv_Object = MibTableColumn
cfprApStorageEpUserPriv = _CfprApStorageEpUserPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8, 1, 9),
    _CfprApStorageEpUserPriv_Type()
)
cfprApStorageEpUserPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEpUserPriv.setStatus("current")
_CfprApStorageEpUserPwd_Type = SnmpAdminString
_CfprApStorageEpUserPwd_Object = MibTableColumn
cfprApStorageEpUserPwd = _CfprApStorageEpUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8, 1, 10),
    _CfprApStorageEpUserPwd_Type()
)
cfprApStorageEpUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEpUserPwd.setStatus("current")
_CfprApStorageEpUserPwdSet_Type = TruthValue
_CfprApStorageEpUserPwdSet_Object = MibTableColumn
cfprApStorageEpUserPwdSet = _CfprApStorageEpUserPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 8, 1, 11),
    _CfprApStorageEpUserPwdSet_Type()
)
cfprApStorageEpUserPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEpUserPwdSet.setStatus("current")
_CfprApStorageEtherIfTable_Object = MibTable
cfprApStorageEtherIfTable = _CfprApStorageEtherIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 9)
)
if mibBuilder.loadTexts:
    cfprApStorageEtherIfTable.setStatus("current")
_CfprApStorageEtherIfEntry_Object = MibTableRow
cfprApStorageEtherIfEntry = _CfprApStorageEtherIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 9, 1)
)
cfprApStorageEtherIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageEtherIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageEtherIfEntry.setStatus("current")
_CfprApStorageEtherIfInstanceId_Type = CfprApManagedObjectId
_CfprApStorageEtherIfInstanceId_Object = MibTableColumn
cfprApStorageEtherIfInstanceId = _CfprApStorageEtherIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 9, 1, 1),
    _CfprApStorageEtherIfInstanceId_Type()
)
cfprApStorageEtherIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageEtherIfInstanceId.setStatus("current")
_CfprApStorageEtherIfDn_Type = CfprApManagedObjectDn
_CfprApStorageEtherIfDn_Object = MibTableColumn
cfprApStorageEtherIfDn = _CfprApStorageEtherIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 9, 1, 2),
    _CfprApStorageEtherIfDn_Type()
)
cfprApStorageEtherIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEtherIfDn.setStatus("current")
_CfprApStorageEtherIfRn_Type = SnmpAdminString
_CfprApStorageEtherIfRn_Object = MibTableColumn
cfprApStorageEtherIfRn = _CfprApStorageEtherIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 9, 1, 3),
    _CfprApStorageEtherIfRn_Type()
)
cfprApStorageEtherIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEtherIfRn.setStatus("current")
_CfprApStorageEtherIfName_Type = SnmpAdminString
_CfprApStorageEtherIfName_Object = MibTableColumn
cfprApStorageEtherIfName = _CfprApStorageEtherIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 9, 1, 4),
    _CfprApStorageEtherIfName_Type()
)
cfprApStorageEtherIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEtherIfName.setStatus("current")
_CfprApStorageEtherIfVlanType_Type = CfprApStorageEtherIfVlanType
_CfprApStorageEtherIfVlanType_Object = MibTableColumn
cfprApStorageEtherIfVlanType = _CfprApStorageEtherIfVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 9, 1, 5),
    _CfprApStorageEtherIfVlanType_Type()
)
cfprApStorageEtherIfVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageEtherIfVlanType.setStatus("current")
_CfprApStorageFcIfTable_Object = MibTable
cfprApStorageFcIfTable = _CfprApStorageFcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 10)
)
if mibBuilder.loadTexts:
    cfprApStorageFcIfTable.setStatus("current")
_CfprApStorageFcIfEntry_Object = MibTableRow
cfprApStorageFcIfEntry = _CfprApStorageFcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 10, 1)
)
cfprApStorageFcIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageFcIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageFcIfEntry.setStatus("current")
_CfprApStorageFcIfInstanceId_Type = CfprApManagedObjectId
_CfprApStorageFcIfInstanceId_Object = MibTableColumn
cfprApStorageFcIfInstanceId = _CfprApStorageFcIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 10, 1, 1),
    _CfprApStorageFcIfInstanceId_Type()
)
cfprApStorageFcIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageFcIfInstanceId.setStatus("current")
_CfprApStorageFcIfDn_Type = CfprApManagedObjectDn
_CfprApStorageFcIfDn_Object = MibTableColumn
cfprApStorageFcIfDn = _CfprApStorageFcIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 10, 1, 2),
    _CfprApStorageFcIfDn_Type()
)
cfprApStorageFcIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFcIfDn.setStatus("current")
_CfprApStorageFcIfRn_Type = SnmpAdminString
_CfprApStorageFcIfRn_Object = MibTableColumn
cfprApStorageFcIfRn = _CfprApStorageFcIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 10, 1, 3),
    _CfprApStorageFcIfRn_Type()
)
cfprApStorageFcIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFcIfRn.setStatus("current")
_CfprApStorageFcIfName_Type = SnmpAdminString
_CfprApStorageFcIfName_Object = MibTableColumn
cfprApStorageFcIfName = _CfprApStorageFcIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 10, 1, 4),
    _CfprApStorageFcIfName_Type()
)
cfprApStorageFcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFcIfName.setStatus("current")
_CfprApStorageFcTargetIfTable_Object = MibTable
cfprApStorageFcTargetIfTable = _CfprApStorageFcTargetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 12)
)
if mibBuilder.loadTexts:
    cfprApStorageFcTargetIfTable.setStatus("current")
_CfprApStorageFcTargetIfEntry_Object = MibTableRow
cfprApStorageFcTargetIfEntry = _CfprApStorageFcTargetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 12, 1)
)
cfprApStorageFcTargetIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageFcTargetIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageFcTargetIfEntry.setStatus("current")
_CfprApStorageFcTargetIfInstanceId_Type = CfprApManagedObjectId
_CfprApStorageFcTargetIfInstanceId_Object = MibTableColumn
cfprApStorageFcTargetIfInstanceId = _CfprApStorageFcTargetIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 12, 1, 1),
    _CfprApStorageFcTargetIfInstanceId_Type()
)
cfprApStorageFcTargetIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageFcTargetIfInstanceId.setStatus("current")
_CfprApStorageFcTargetIfDn_Type = CfprApManagedObjectDn
_CfprApStorageFcTargetIfDn_Object = MibTableColumn
cfprApStorageFcTargetIfDn = _CfprApStorageFcTargetIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 12, 1, 2),
    _CfprApStorageFcTargetIfDn_Type()
)
cfprApStorageFcTargetIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFcTargetIfDn.setStatus("current")
_CfprApStorageFcTargetIfRn_Type = SnmpAdminString
_CfprApStorageFcTargetIfRn_Object = MibTableColumn
cfprApStorageFcTargetIfRn = _CfprApStorageFcTargetIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 12, 1, 3),
    _CfprApStorageFcTargetIfRn_Type()
)
cfprApStorageFcTargetIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFcTargetIfRn.setStatus("current")
_CfprApStorageFcTargetIfId_Type = Unsigned64
_CfprApStorageFcTargetIfId_Object = MibTableColumn
cfprApStorageFcTargetIfId = _CfprApStorageFcTargetIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 12, 1, 4),
    _CfprApStorageFcTargetIfId_Type()
)
cfprApStorageFcTargetIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFcTargetIfId.setStatus("current")
_CfprApStorageFcTargetIfProt_Type = CfprApStorageProtocol
_CfprApStorageFcTargetIfProt_Object = MibTableColumn
cfprApStorageFcTargetIfProt = _CfprApStorageFcTargetIfProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 12, 1, 5),
    _CfprApStorageFcTargetIfProt_Type()
)
cfprApStorageFcTargetIfProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFcTargetIfProt.setStatus("current")
_CfprApStorageFlexFlashCardTable_Object = MibTable
cfprApStorageFlexFlashCardTable = _CfprApStorageFlexFlashCardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13)
)
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardTable.setStatus("current")
_CfprApStorageFlexFlashCardEntry_Object = MibTableRow
cfprApStorageFlexFlashCardEntry = _CfprApStorageFlexFlashCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1)
)
cfprApStorageFlexFlashCardEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageFlexFlashCardInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardEntry.setStatus("current")
_CfprApStorageFlexFlashCardInstanceId_Type = CfprApManagedObjectId
_CfprApStorageFlexFlashCardInstanceId_Object = MibTableColumn
cfprApStorageFlexFlashCardInstanceId = _CfprApStorageFlexFlashCardInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 1),
    _CfprApStorageFlexFlashCardInstanceId_Type()
)
cfprApStorageFlexFlashCardInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardInstanceId.setStatus("current")
_CfprApStorageFlexFlashCardDn_Type = CfprApManagedObjectDn
_CfprApStorageFlexFlashCardDn_Object = MibTableColumn
cfprApStorageFlexFlashCardDn = _CfprApStorageFlexFlashCardDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 2),
    _CfprApStorageFlexFlashCardDn_Type()
)
cfprApStorageFlexFlashCardDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardDn.setStatus("current")
_CfprApStorageFlexFlashCardRn_Type = SnmpAdminString
_CfprApStorageFlexFlashCardRn_Object = MibTableColumn
cfprApStorageFlexFlashCardRn = _CfprApStorageFlexFlashCardRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 3),
    _CfprApStorageFlexFlashCardRn_Type()
)
cfprApStorageFlexFlashCardRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardRn.setStatus("current")
_CfprApStorageFlexFlashCardBlockSize_Type = Gauge32
_CfprApStorageFlexFlashCardBlockSize_Object = MibTableColumn
cfprApStorageFlexFlashCardBlockSize = _CfprApStorageFlexFlashCardBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 4),
    _CfprApStorageFlexFlashCardBlockSize_Type()
)
cfprApStorageFlexFlashCardBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardBlockSize.setStatus("current")
_CfprApStorageFlexFlashCardCardHealth_Type = CfprApStorageFFCardHealth
_CfprApStorageFlexFlashCardCardHealth_Object = MibTableColumn
cfprApStorageFlexFlashCardCardHealth = _CfprApStorageFlexFlashCardCardHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 5),
    _CfprApStorageFlexFlashCardCardHealth_Type()
)
cfprApStorageFlexFlashCardCardHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardCardHealth.setStatus("current")
_CfprApStorageFlexFlashCardCardMode_Type = CfprApStorageFFCardMode
_CfprApStorageFlexFlashCardCardMode_Object = MibTableColumn
cfprApStorageFlexFlashCardCardMode = _CfprApStorageFlexFlashCardCardMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 6),
    _CfprApStorageFlexFlashCardCardMode_Type()
)
cfprApStorageFlexFlashCardCardMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardCardMode.setStatus("current")
_CfprApStorageFlexFlashCardCardState_Type = CfprApStorageFFCardState
_CfprApStorageFlexFlashCardCardState_Object = MibTableColumn
cfprApStorageFlexFlashCardCardState = _CfprApStorageFlexFlashCardCardState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 7),
    _CfprApStorageFlexFlashCardCardState_Type()
)
cfprApStorageFlexFlashCardCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardCardState.setStatus("current")
_CfprApStorageFlexFlashCardCardSync_Type = CfprApStorageFFCardSync
_CfprApStorageFlexFlashCardCardSync_Object = MibTableColumn
cfprApStorageFlexFlashCardCardSync = _CfprApStorageFlexFlashCardCardSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 8),
    _CfprApStorageFlexFlashCardCardSync_Type()
)
cfprApStorageFlexFlashCardCardSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardCardSync.setStatus("current")
_CfprApStorageFlexFlashCardCardType_Type = SnmpAdminString
_CfprApStorageFlexFlashCardCardType_Object = MibTableColumn
cfprApStorageFlexFlashCardCardType = _CfprApStorageFlexFlashCardCardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 9),
    _CfprApStorageFlexFlashCardCardType_Type()
)
cfprApStorageFlexFlashCardCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardCardType.setStatus("current")
_CfprApStorageFlexFlashCardConnectionProtocol_Type = CfprApStorageConnectionProtocol
_CfprApStorageFlexFlashCardConnectionProtocol_Object = MibTableColumn
cfprApStorageFlexFlashCardConnectionProtocol = _CfprApStorageFlexFlashCardConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 10),
    _CfprApStorageFlexFlashCardConnectionProtocol_Type()
)
cfprApStorageFlexFlashCardConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardConnectionProtocol.setStatus("current")
_CfprApStorageFlexFlashCardControllerIndex_Type = Gauge32
_CfprApStorageFlexFlashCardControllerIndex_Object = MibTableColumn
cfprApStorageFlexFlashCardControllerIndex = _CfprApStorageFlexFlashCardControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 11),
    _CfprApStorageFlexFlashCardControllerIndex_Type()
)
cfprApStorageFlexFlashCardControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardControllerIndex.setStatus("current")
_CfprApStorageFlexFlashCardDrivesEnabled_Type = SnmpAdminString
_CfprApStorageFlexFlashCardDrivesEnabled_Object = MibTableColumn
cfprApStorageFlexFlashCardDrivesEnabled = _CfprApStorageFlexFlashCardDrivesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 12),
    _CfprApStorageFlexFlashCardDrivesEnabled_Type()
)
cfprApStorageFlexFlashCardDrivesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardDrivesEnabled.setStatus("current")
_CfprApStorageFlexFlashCardId_Type = Gauge32
_CfprApStorageFlexFlashCardId_Object = MibTableColumn
cfprApStorageFlexFlashCardId = _CfprApStorageFlexFlashCardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 13),
    _CfprApStorageFlexFlashCardId_Type()
)
cfprApStorageFlexFlashCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardId.setStatus("current")
_CfprApStorageFlexFlashCardMfgDate_Type = SnmpAdminString
_CfprApStorageFlexFlashCardMfgDate_Object = MibTableColumn
cfprApStorageFlexFlashCardMfgDate = _CfprApStorageFlexFlashCardMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 14),
    _CfprApStorageFlexFlashCardMfgDate_Type()
)
cfprApStorageFlexFlashCardMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardMfgDate.setStatus("current")
_CfprApStorageFlexFlashCardMfgId_Type = SnmpAdminString
_CfprApStorageFlexFlashCardMfgId_Object = MibTableColumn
cfprApStorageFlexFlashCardMfgId = _CfprApStorageFlexFlashCardMfgId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 15),
    _CfprApStorageFlexFlashCardMfgId_Type()
)
cfprApStorageFlexFlashCardMfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardMfgId.setStatus("current")
_CfprApStorageFlexFlashCardModel_Type = SnmpAdminString
_CfprApStorageFlexFlashCardModel_Object = MibTableColumn
cfprApStorageFlexFlashCardModel = _CfprApStorageFlexFlashCardModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 16),
    _CfprApStorageFlexFlashCardModel_Type()
)
cfprApStorageFlexFlashCardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardModel.setStatus("current")
_CfprApStorageFlexFlashCardNumberOfBlocks_Type = Unsigned64
_CfprApStorageFlexFlashCardNumberOfBlocks_Object = MibTableColumn
cfprApStorageFlexFlashCardNumberOfBlocks = _CfprApStorageFlexFlashCardNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 17),
    _CfprApStorageFlexFlashCardNumberOfBlocks_Type()
)
cfprApStorageFlexFlashCardNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardNumberOfBlocks.setStatus("current")
_CfprApStorageFlexFlashCardOemId_Type = SnmpAdminString
_CfprApStorageFlexFlashCardOemId_Object = MibTableColumn
cfprApStorageFlexFlashCardOemId = _CfprApStorageFlexFlashCardOemId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 18),
    _CfprApStorageFlexFlashCardOemId_Type()
)
cfprApStorageFlexFlashCardOemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardOemId.setStatus("current")
_CfprApStorageFlexFlashCardOperQualifierReason_Type = SnmpAdminString
_CfprApStorageFlexFlashCardOperQualifierReason_Object = MibTableColumn
cfprApStorageFlexFlashCardOperQualifierReason = _CfprApStorageFlexFlashCardOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 19),
    _CfprApStorageFlexFlashCardOperQualifierReason_Type()
)
cfprApStorageFlexFlashCardOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardOperQualifierReason.setStatus("current")
_CfprApStorageFlexFlashCardOperability_Type = CfprApEquipmentOperability
_CfprApStorageFlexFlashCardOperability_Object = MibTableColumn
cfprApStorageFlexFlashCardOperability = _CfprApStorageFlexFlashCardOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 20),
    _CfprApStorageFlexFlashCardOperability_Type()
)
cfprApStorageFlexFlashCardOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardOperability.setStatus("current")
_CfprApStorageFlexFlashCardPartitionCount_Type = Gauge32
_CfprApStorageFlexFlashCardPartitionCount_Object = MibTableColumn
cfprApStorageFlexFlashCardPartitionCount = _CfprApStorageFlexFlashCardPartitionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 21),
    _CfprApStorageFlexFlashCardPartitionCount_Type()
)
cfprApStorageFlexFlashCardPartitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardPartitionCount.setStatus("current")
_CfprApStorageFlexFlashCardPresence_Type = CfprApEquipmentPresence
_CfprApStorageFlexFlashCardPresence_Object = MibTableColumn
cfprApStorageFlexFlashCardPresence = _CfprApStorageFlexFlashCardPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 22),
    _CfprApStorageFlexFlashCardPresence_Type()
)
cfprApStorageFlexFlashCardPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardPresence.setStatus("current")
_CfprApStorageFlexFlashCardReadErrorThreshold_Type = Gauge32
_CfprApStorageFlexFlashCardReadErrorThreshold_Object = MibTableColumn
cfprApStorageFlexFlashCardReadErrorThreshold = _CfprApStorageFlexFlashCardReadErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 23),
    _CfprApStorageFlexFlashCardReadErrorThreshold_Type()
)
cfprApStorageFlexFlashCardReadErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardReadErrorThreshold.setStatus("current")
_CfprApStorageFlexFlashCardReadIOErrorCount_Type = Gauge32
_CfprApStorageFlexFlashCardReadIOErrorCount_Object = MibTableColumn
cfprApStorageFlexFlashCardReadIOErrorCount = _CfprApStorageFlexFlashCardReadIOErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 24),
    _CfprApStorageFlexFlashCardReadIOErrorCount_Type()
)
cfprApStorageFlexFlashCardReadIOErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardReadIOErrorCount.setStatus("current")
_CfprApStorageFlexFlashCardRevision_Type = SnmpAdminString
_CfprApStorageFlexFlashCardRevision_Object = MibTableColumn
cfprApStorageFlexFlashCardRevision = _CfprApStorageFlexFlashCardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 25),
    _CfprApStorageFlexFlashCardRevision_Type()
)
cfprApStorageFlexFlashCardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardRevision.setStatus("current")
_CfprApStorageFlexFlashCardSerial_Type = SnmpAdminString
_CfprApStorageFlexFlashCardSerial_Object = MibTableColumn
cfprApStorageFlexFlashCardSerial = _CfprApStorageFlexFlashCardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 26),
    _CfprApStorageFlexFlashCardSerial_Type()
)
cfprApStorageFlexFlashCardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardSerial.setStatus("current")
_CfprApStorageFlexFlashCardSignature_Type = SnmpAdminString
_CfprApStorageFlexFlashCardSignature_Object = MibTableColumn
cfprApStorageFlexFlashCardSignature = _CfprApStorageFlexFlashCardSignature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 27),
    _CfprApStorageFlexFlashCardSignature_Type()
)
cfprApStorageFlexFlashCardSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardSignature.setStatus("current")
_CfprApStorageFlexFlashCardSize_Type = Unsigned64
_CfprApStorageFlexFlashCardSize_Object = MibTableColumn
cfprApStorageFlexFlashCardSize = _CfprApStorageFlexFlashCardSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 28),
    _CfprApStorageFlexFlashCardSize_Type()
)
cfprApStorageFlexFlashCardSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardSize.setStatus("current")
_CfprApStorageFlexFlashCardSlotNumber_Type = Gauge32
_CfprApStorageFlexFlashCardSlotNumber_Object = MibTableColumn
cfprApStorageFlexFlashCardSlotNumber = _CfprApStorageFlexFlashCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 29),
    _CfprApStorageFlexFlashCardSlotNumber_Type()
)
cfprApStorageFlexFlashCardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardSlotNumber.setStatus("current")
_CfprApStorageFlexFlashCardVendor_Type = SnmpAdminString
_CfprApStorageFlexFlashCardVendor_Object = MibTableColumn
cfprApStorageFlexFlashCardVendor = _CfprApStorageFlexFlashCardVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 30),
    _CfprApStorageFlexFlashCardVendor_Type()
)
cfprApStorageFlexFlashCardVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardVendor.setStatus("current")
_CfprApStorageFlexFlashCardWriteEnable_Type = CfprApStorageFFCardWriteEnable
_CfprApStorageFlexFlashCardWriteEnable_Object = MibTableColumn
cfprApStorageFlexFlashCardWriteEnable = _CfprApStorageFlexFlashCardWriteEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 31),
    _CfprApStorageFlexFlashCardWriteEnable_Type()
)
cfprApStorageFlexFlashCardWriteEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardWriteEnable.setStatus("current")
_CfprApStorageFlexFlashCardWriteErrorThreshold_Type = Gauge32
_CfprApStorageFlexFlashCardWriteErrorThreshold_Object = MibTableColumn
cfprApStorageFlexFlashCardWriteErrorThreshold = _CfprApStorageFlexFlashCardWriteErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 32),
    _CfprApStorageFlexFlashCardWriteErrorThreshold_Type()
)
cfprApStorageFlexFlashCardWriteErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardWriteErrorThreshold.setStatus("current")
_CfprApStorageFlexFlashCardWriteIOErrorCount_Type = Gauge32
_CfprApStorageFlexFlashCardWriteIOErrorCount_Object = MibTableColumn
cfprApStorageFlexFlashCardWriteIOErrorCount = _CfprApStorageFlexFlashCardWriteIOErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 13, 1, 33),
    _CfprApStorageFlexFlashCardWriteIOErrorCount_Type()
)
cfprApStorageFlexFlashCardWriteIOErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashCardWriteIOErrorCount.setStatus("current")
_CfprApStorageFlexFlashControllerTable_Object = MibTable
cfprApStorageFlexFlashControllerTable = _CfprApStorageFlexFlashControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14)
)
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerTable.setStatus("current")
_CfprApStorageFlexFlashControllerEntry_Object = MibTableRow
cfprApStorageFlexFlashControllerEntry = _CfprApStorageFlexFlashControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1)
)
cfprApStorageFlexFlashControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageFlexFlashControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerEntry.setStatus("current")
_CfprApStorageFlexFlashControllerInstanceId_Type = CfprApManagedObjectId
_CfprApStorageFlexFlashControllerInstanceId_Object = MibTableColumn
cfprApStorageFlexFlashControllerInstanceId = _CfprApStorageFlexFlashControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 1),
    _CfprApStorageFlexFlashControllerInstanceId_Type()
)
cfprApStorageFlexFlashControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerInstanceId.setStatus("current")
_CfprApStorageFlexFlashControllerDn_Type = CfprApManagedObjectDn
_CfprApStorageFlexFlashControllerDn_Object = MibTableColumn
cfprApStorageFlexFlashControllerDn = _CfprApStorageFlexFlashControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 2),
    _CfprApStorageFlexFlashControllerDn_Type()
)
cfprApStorageFlexFlashControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerDn.setStatus("current")
_CfprApStorageFlexFlashControllerRn_Type = SnmpAdminString
_CfprApStorageFlexFlashControllerRn_Object = MibTableColumn
cfprApStorageFlexFlashControllerRn = _CfprApStorageFlexFlashControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 3),
    _CfprApStorageFlexFlashControllerRn_Type()
)
cfprApStorageFlexFlashControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerRn.setStatus("current")
_CfprApStorageFlexFlashControllerAdminSlotNumber_Type = CfprApStorageFFSlotENUM
_CfprApStorageFlexFlashControllerAdminSlotNumber_Object = MibTableColumn
cfprApStorageFlexFlashControllerAdminSlotNumber = _CfprApStorageFlexFlashControllerAdminSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 4),
    _CfprApStorageFlexFlashControllerAdminSlotNumber_Type()
)
cfprApStorageFlexFlashControllerAdminSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerAdminSlotNumber.setStatus("current")
_CfprApStorageFlexFlashControllerConfiguredMode_Type = CfprApStorageOperatingModeType
_CfprApStorageFlexFlashControllerConfiguredMode_Object = MibTableColumn
cfprApStorageFlexFlashControllerConfiguredMode = _CfprApStorageFlexFlashControllerConfiguredMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 5),
    _CfprApStorageFlexFlashControllerConfiguredMode_Type()
)
cfprApStorageFlexFlashControllerConfiguredMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerConfiguredMode.setStatus("current")
_CfprApStorageFlexFlashControllerControllerHealth_Type = CfprApStorageFFControllerHealth
_CfprApStorageFlexFlashControllerControllerHealth_Object = MibTableColumn
cfprApStorageFlexFlashControllerControllerHealth = _CfprApStorageFlexFlashControllerControllerHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 6),
    _CfprApStorageFlexFlashControllerControllerHealth_Type()
)
cfprApStorageFlexFlashControllerControllerHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerControllerHealth.setStatus("current")
_CfprApStorageFlexFlashControllerControllerState_Type = CfprApStorageFFControllerState
_CfprApStorageFlexFlashControllerControllerState_Object = MibTableColumn
cfprApStorageFlexFlashControllerControllerState = _CfprApStorageFlexFlashControllerControllerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 7),
    _CfprApStorageFlexFlashControllerControllerState_Type()
)
cfprApStorageFlexFlashControllerControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerControllerState.setStatus("current")
_CfprApStorageFlexFlashControllerFirmwareVersion_Type = SnmpAdminString
_CfprApStorageFlexFlashControllerFirmwareVersion_Object = MibTableColumn
cfprApStorageFlexFlashControllerFirmwareVersion = _CfprApStorageFlexFlashControllerFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 8),
    _CfprApStorageFlexFlashControllerFirmwareVersion_Type()
)
cfprApStorageFlexFlashControllerFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerFirmwareVersion.setStatus("current")
_CfprApStorageFlexFlashControllerFlexFlashType_Type = CfprApStorageFFType
_CfprApStorageFlexFlashControllerFlexFlashType_Object = MibTableColumn
cfprApStorageFlexFlashControllerFlexFlashType = _CfprApStorageFlexFlashControllerFlexFlashType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 9),
    _CfprApStorageFlexFlashControllerFlexFlashType_Type()
)
cfprApStorageFlexFlashControllerFlexFlashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerFlexFlashType.setStatus("current")
_CfprApStorageFlexFlashControllerHasError_Type = CfprApStorageFFHasError
_CfprApStorageFlexFlashControllerHasError_Object = MibTableColumn
cfprApStorageFlexFlashControllerHasError = _CfprApStorageFlexFlashControllerHasError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 10),
    _CfprApStorageFlexFlashControllerHasError_Type()
)
cfprApStorageFlexFlashControllerHasError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerHasError.setStatus("current")
_CfprApStorageFlexFlashControllerId_Type = CfprApStorageFlexFlashControllerId
_CfprApStorageFlexFlashControllerId_Object = MibTableColumn
cfprApStorageFlexFlashControllerId = _CfprApStorageFlexFlashControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 11),
    _CfprApStorageFlexFlashControllerId_Type()
)
cfprApStorageFlexFlashControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerId.setStatus("current")
_CfprApStorageFlexFlashControllerIsCardMismatch_Type = CfprApStorageFFCardSizeMismatch
_CfprApStorageFlexFlashControllerIsCardMismatch_Object = MibTableColumn
cfprApStorageFlexFlashControllerIsCardMismatch = _CfprApStorageFlexFlashControllerIsCardMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 12),
    _CfprApStorageFlexFlashControllerIsCardMismatch_Type()
)
cfprApStorageFlexFlashControllerIsCardMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerIsCardMismatch.setStatus("current")
_CfprApStorageFlexFlashControllerIsFormatFSMRunning_Type = CfprApStorageFFFormatRunning
_CfprApStorageFlexFlashControllerIsFormatFSMRunning_Object = MibTableColumn
cfprApStorageFlexFlashControllerIsFormatFSMRunning = _CfprApStorageFlexFlashControllerIsFormatFSMRunning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 13),
    _CfprApStorageFlexFlashControllerIsFormatFSMRunning_Type()
)
cfprApStorageFlexFlashControllerIsFormatFSMRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerIsFormatFSMRunning.setStatus("current")
_CfprApStorageFlexFlashControllerLocationDn_Type = SnmpAdminString
_CfprApStorageFlexFlashControllerLocationDn_Object = MibTableColumn
cfprApStorageFlexFlashControllerLocationDn = _CfprApStorageFlexFlashControllerLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 14),
    _CfprApStorageFlexFlashControllerLocationDn_Type()
)
cfprApStorageFlexFlashControllerLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerLocationDn.setStatus("current")
_CfprApStorageFlexFlashControllerModel_Type = SnmpAdminString
_CfprApStorageFlexFlashControllerModel_Object = MibTableColumn
cfprApStorageFlexFlashControllerModel = _CfprApStorageFlexFlashControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 15),
    _CfprApStorageFlexFlashControllerModel_Type()
)
cfprApStorageFlexFlashControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerModel.setStatus("current")
_CfprApStorageFlexFlashControllerOperQualifierReason_Type = SnmpAdminString
_CfprApStorageFlexFlashControllerOperQualifierReason_Object = MibTableColumn
cfprApStorageFlexFlashControllerOperQualifierReason = _CfprApStorageFlexFlashControllerOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 16),
    _CfprApStorageFlexFlashControllerOperQualifierReason_Type()
)
cfprApStorageFlexFlashControllerOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerOperQualifierReason.setStatus("current")
_CfprApStorageFlexFlashControllerOperState_Type = CfprApEquipmentOperability
_CfprApStorageFlexFlashControllerOperState_Object = MibTableColumn
cfprApStorageFlexFlashControllerOperState = _CfprApStorageFlexFlashControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 17),
    _CfprApStorageFlexFlashControllerOperState_Type()
)
cfprApStorageFlexFlashControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerOperState.setStatus("current")
_CfprApStorageFlexFlashControllerOperability_Type = CfprApEquipmentOperability
_CfprApStorageFlexFlashControllerOperability_Object = MibTableColumn
cfprApStorageFlexFlashControllerOperability = _CfprApStorageFlexFlashControllerOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 18),
    _CfprApStorageFlexFlashControllerOperability_Type()
)
cfprApStorageFlexFlashControllerOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerOperability.setStatus("current")
_CfprApStorageFlexFlashControllerOperatingMode_Type = CfprApStorageOperatingModeType
_CfprApStorageFlexFlashControllerOperatingMode_Object = MibTableColumn
cfprApStorageFlexFlashControllerOperatingMode = _CfprApStorageFlexFlashControllerOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 19),
    _CfprApStorageFlexFlashControllerOperatingMode_Type()
)
cfprApStorageFlexFlashControllerOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerOperatingMode.setStatus("current")
_CfprApStorageFlexFlashControllerOperationRequest_Type = CfprApStorageOperationRequestType
_CfprApStorageFlexFlashControllerOperationRequest_Object = MibTableColumn
cfprApStorageFlexFlashControllerOperationRequest = _CfprApStorageFlexFlashControllerOperationRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 20),
    _CfprApStorageFlexFlashControllerOperationRequest_Type()
)
cfprApStorageFlexFlashControllerOperationRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerOperationRequest.setStatus("current")
_CfprApStorageFlexFlashControllerPciAddr_Type = SnmpAdminString
_CfprApStorageFlexFlashControllerPciAddr_Object = MibTableColumn
cfprApStorageFlexFlashControllerPciAddr = _CfprApStorageFlexFlashControllerPciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 21),
    _CfprApStorageFlexFlashControllerPciAddr_Type()
)
cfprApStorageFlexFlashControllerPciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerPciAddr.setStatus("current")
_CfprApStorageFlexFlashControllerPciSlot_Type = SnmpAdminString
_CfprApStorageFlexFlashControllerPciSlot_Object = MibTableColumn
cfprApStorageFlexFlashControllerPciSlot = _CfprApStorageFlexFlashControllerPciSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 22),
    _CfprApStorageFlexFlashControllerPciSlot_Type()
)
cfprApStorageFlexFlashControllerPciSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerPciSlot.setStatus("current")
_CfprApStorageFlexFlashControllerPerf_Type = CfprApEquipmentSensorThresholdStatus
_CfprApStorageFlexFlashControllerPerf_Object = MibTableColumn
cfprApStorageFlexFlashControllerPerf = _CfprApStorageFlexFlashControllerPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 23),
    _CfprApStorageFlexFlashControllerPerf_Type()
)
cfprApStorageFlexFlashControllerPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerPerf.setStatus("current")
_CfprApStorageFlexFlashControllerPhysicalDriveCount_Type = Gauge32
_CfprApStorageFlexFlashControllerPhysicalDriveCount_Object = MibTableColumn
cfprApStorageFlexFlashControllerPhysicalDriveCount = _CfprApStorageFlexFlashControllerPhysicalDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 24),
    _CfprApStorageFlexFlashControllerPhysicalDriveCount_Type()
)
cfprApStorageFlexFlashControllerPhysicalDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerPhysicalDriveCount.setStatus("current")
_CfprApStorageFlexFlashControllerPower_Type = CfprApEquipmentPowerState
_CfprApStorageFlexFlashControllerPower_Object = MibTableColumn
cfprApStorageFlexFlashControllerPower = _CfprApStorageFlexFlashControllerPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 25),
    _CfprApStorageFlexFlashControllerPower_Type()
)
cfprApStorageFlexFlashControllerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerPower.setStatus("current")
_CfprApStorageFlexFlashControllerPresence_Type = CfprApEquipmentPresence
_CfprApStorageFlexFlashControllerPresence_Object = MibTableColumn
cfprApStorageFlexFlashControllerPresence = _CfprApStorageFlexFlashControllerPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 26),
    _CfprApStorageFlexFlashControllerPresence_Type()
)
cfprApStorageFlexFlashControllerPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerPresence.setStatus("current")
_CfprApStorageFlexFlashControllerPrimarySlotNumber_Type = Gauge32
_CfprApStorageFlexFlashControllerPrimarySlotNumber_Object = MibTableColumn
cfprApStorageFlexFlashControllerPrimarySlotNumber = _CfprApStorageFlexFlashControllerPrimarySlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 27),
    _CfprApStorageFlexFlashControllerPrimarySlotNumber_Type()
)
cfprApStorageFlexFlashControllerPrimarySlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerPrimarySlotNumber.setStatus("current")
_CfprApStorageFlexFlashControllerRaidSyncSupport_Type = CfprApStorageFFRaidSyncSupport
_CfprApStorageFlexFlashControllerRaidSyncSupport_Object = MibTableColumn
cfprApStorageFlexFlashControllerRaidSyncSupport = _CfprApStorageFlexFlashControllerRaidSyncSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 28),
    _CfprApStorageFlexFlashControllerRaidSyncSupport_Type()
)
cfprApStorageFlexFlashControllerRaidSyncSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerRaidSyncSupport.setStatus("current")
_CfprApStorageFlexFlashControllerReadErrorThreshold_Type = Gauge32
_CfprApStorageFlexFlashControllerReadErrorThreshold_Object = MibTableColumn
cfprApStorageFlexFlashControllerReadErrorThreshold = _CfprApStorageFlexFlashControllerReadErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 29),
    _CfprApStorageFlexFlashControllerReadErrorThreshold_Type()
)
cfprApStorageFlexFlashControllerReadErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerReadErrorThreshold.setStatus("current")
_CfprApStorageFlexFlashControllerRevision_Type = SnmpAdminString
_CfprApStorageFlexFlashControllerRevision_Object = MibTableColumn
cfprApStorageFlexFlashControllerRevision = _CfprApStorageFlexFlashControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 30),
    _CfprApStorageFlexFlashControllerRevision_Type()
)
cfprApStorageFlexFlashControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerRevision.setStatus("current")
_CfprApStorageFlexFlashControllerSerial_Type = SnmpAdminString
_CfprApStorageFlexFlashControllerSerial_Object = MibTableColumn
cfprApStorageFlexFlashControllerSerial = _CfprApStorageFlexFlashControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 31),
    _CfprApStorageFlexFlashControllerSerial_Type()
)
cfprApStorageFlexFlashControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerSerial.setStatus("current")
_CfprApStorageFlexFlashControllerThermal_Type = CfprApEquipmentSensorThresholdStatus
_CfprApStorageFlexFlashControllerThermal_Object = MibTableColumn
cfprApStorageFlexFlashControllerThermal = _CfprApStorageFlexFlashControllerThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 32),
    _CfprApStorageFlexFlashControllerThermal_Type()
)
cfprApStorageFlexFlashControllerThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerThermal.setStatus("current")
_CfprApStorageFlexFlashControllerType_Type = CfprApStorageControllerType
_CfprApStorageFlexFlashControllerType_Object = MibTableColumn
cfprApStorageFlexFlashControllerType = _CfprApStorageFlexFlashControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 33),
    _CfprApStorageFlexFlashControllerType_Type()
)
cfprApStorageFlexFlashControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerType.setStatus("current")
_CfprApStorageFlexFlashControllerVendor_Type = SnmpAdminString
_CfprApStorageFlexFlashControllerVendor_Object = MibTableColumn
cfprApStorageFlexFlashControllerVendor = _CfprApStorageFlexFlashControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 34),
    _CfprApStorageFlexFlashControllerVendor_Type()
)
cfprApStorageFlexFlashControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerVendor.setStatus("current")
_CfprApStorageFlexFlashControllerVirtualDriveCount_Type = Gauge32
_CfprApStorageFlexFlashControllerVirtualDriveCount_Object = MibTableColumn
cfprApStorageFlexFlashControllerVirtualDriveCount = _CfprApStorageFlexFlashControllerVirtualDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 35),
    _CfprApStorageFlexFlashControllerVirtualDriveCount_Type()
)
cfprApStorageFlexFlashControllerVirtualDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerVirtualDriveCount.setStatus("current")
_CfprApStorageFlexFlashControllerVoltage_Type = CfprApEquipmentSensorThresholdStatus
_CfprApStorageFlexFlashControllerVoltage_Object = MibTableColumn
cfprApStorageFlexFlashControllerVoltage = _CfprApStorageFlexFlashControllerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 36),
    _CfprApStorageFlexFlashControllerVoltage_Type()
)
cfprApStorageFlexFlashControllerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerVoltage.setStatus("current")
_CfprApStorageFlexFlashControllerWriteErrorThreshold_Type = Gauge32
_CfprApStorageFlexFlashControllerWriteErrorThreshold_Object = MibTableColumn
cfprApStorageFlexFlashControllerWriteErrorThreshold = _CfprApStorageFlexFlashControllerWriteErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 14, 1, 37),
    _CfprApStorageFlexFlashControllerWriteErrorThreshold_Type()
)
cfprApStorageFlexFlashControllerWriteErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashControllerWriteErrorThreshold.setStatus("current")
_CfprApStorageFlexFlashDriveTable_Object = MibTable
cfprApStorageFlexFlashDriveTable = _CfprApStorageFlexFlashDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15)
)
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveTable.setStatus("current")
_CfprApStorageFlexFlashDriveEntry_Object = MibTableRow
cfprApStorageFlexFlashDriveEntry = _CfprApStorageFlexFlashDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1)
)
cfprApStorageFlexFlashDriveEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageFlexFlashDriveInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveEntry.setStatus("current")
_CfprApStorageFlexFlashDriveInstanceId_Type = CfprApManagedObjectId
_CfprApStorageFlexFlashDriveInstanceId_Object = MibTableColumn
cfprApStorageFlexFlashDriveInstanceId = _CfprApStorageFlexFlashDriveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 1),
    _CfprApStorageFlexFlashDriveInstanceId_Type()
)
cfprApStorageFlexFlashDriveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveInstanceId.setStatus("current")
_CfprApStorageFlexFlashDriveDn_Type = CfprApManagedObjectDn
_CfprApStorageFlexFlashDriveDn_Object = MibTableColumn
cfprApStorageFlexFlashDriveDn = _CfprApStorageFlexFlashDriveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 2),
    _CfprApStorageFlexFlashDriveDn_Type()
)
cfprApStorageFlexFlashDriveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveDn.setStatus("current")
_CfprApStorageFlexFlashDriveRn_Type = SnmpAdminString
_CfprApStorageFlexFlashDriveRn_Object = MibTableColumn
cfprApStorageFlexFlashDriveRn = _CfprApStorageFlexFlashDriveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 3),
    _CfprApStorageFlexFlashDriveRn_Type()
)
cfprApStorageFlexFlashDriveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveRn.setStatus("current")
_CfprApStorageFlexFlashDriveRWType_Type = CfprApStorageFFRWType
_CfprApStorageFlexFlashDriveRWType_Object = MibTableColumn
cfprApStorageFlexFlashDriveRWType = _CfprApStorageFlexFlashDriveRWType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 4),
    _CfprApStorageFlexFlashDriveRWType_Type()
)
cfprApStorageFlexFlashDriveRWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveRWType.setStatus("current")
_CfprApStorageFlexFlashDriveBlockSize_Type = Gauge32
_CfprApStorageFlexFlashDriveBlockSize_Object = MibTableColumn
cfprApStorageFlexFlashDriveBlockSize = _CfprApStorageFlexFlashDriveBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 5),
    _CfprApStorageFlexFlashDriveBlockSize_Type()
)
cfprApStorageFlexFlashDriveBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveBlockSize.setStatus("current")
_CfprApStorageFlexFlashDriveConnectionProtocol_Type = CfprApStorageConnectionProtocol
_CfprApStorageFlexFlashDriveConnectionProtocol_Object = MibTableColumn
cfprApStorageFlexFlashDriveConnectionProtocol = _CfprApStorageFlexFlashDriveConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 6),
    _CfprApStorageFlexFlashDriveConnectionProtocol_Type()
)
cfprApStorageFlexFlashDriveConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveConnectionProtocol.setStatus("current")
_CfprApStorageFlexFlashDriveControllerIndex_Type = Gauge32
_CfprApStorageFlexFlashDriveControllerIndex_Object = MibTableColumn
cfprApStorageFlexFlashDriveControllerIndex = _CfprApStorageFlexFlashDriveControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 7),
    _CfprApStorageFlexFlashDriveControllerIndex_Type()
)
cfprApStorageFlexFlashDriveControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveControllerIndex.setStatus("current")
_CfprApStorageFlexFlashDriveDriveState_Type = CfprApStorageFFDriveState
_CfprApStorageFlexFlashDriveDriveState_Object = MibTableColumn
cfprApStorageFlexFlashDriveDriveState = _CfprApStorageFlexFlashDriveDriveState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 8),
    _CfprApStorageFlexFlashDriveDriveState_Type()
)
cfprApStorageFlexFlashDriveDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveDriveState.setStatus("current")
_CfprApStorageFlexFlashDriveDriveType_Type = CfprApStorageFFDriveType
_CfprApStorageFlexFlashDriveDriveType_Object = MibTableColumn
cfprApStorageFlexFlashDriveDriveType = _CfprApStorageFlexFlashDriveDriveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 9),
    _CfprApStorageFlexFlashDriveDriveType_Type()
)
cfprApStorageFlexFlashDriveDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveDriveType.setStatus("current")
_CfprApStorageFlexFlashDriveId_Type = Gauge32
_CfprApStorageFlexFlashDriveId_Object = MibTableColumn
cfprApStorageFlexFlashDriveId = _CfprApStorageFlexFlashDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 10),
    _CfprApStorageFlexFlashDriveId_Type()
)
cfprApStorageFlexFlashDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveId.setStatus("current")
_CfprApStorageFlexFlashDriveLastOperation_Type = CfprApStorageOperationStateType
_CfprApStorageFlexFlashDriveLastOperation_Object = MibTableColumn
cfprApStorageFlexFlashDriveLastOperation = _CfprApStorageFlexFlashDriveLastOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 11),
    _CfprApStorageFlexFlashDriveLastOperation_Type()
)
cfprApStorageFlexFlashDriveLastOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveLastOperation.setStatus("current")
_CfprApStorageFlexFlashDriveModel_Type = SnmpAdminString
_CfprApStorageFlexFlashDriveModel_Object = MibTableColumn
cfprApStorageFlexFlashDriveModel = _CfprApStorageFlexFlashDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 12),
    _CfprApStorageFlexFlashDriveModel_Type()
)
cfprApStorageFlexFlashDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveModel.setStatus("current")
_CfprApStorageFlexFlashDriveName_Type = SnmpAdminString
_CfprApStorageFlexFlashDriveName_Object = MibTableColumn
cfprApStorageFlexFlashDriveName = _CfprApStorageFlexFlashDriveName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 13),
    _CfprApStorageFlexFlashDriveName_Type()
)
cfprApStorageFlexFlashDriveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveName.setStatus("current")
_CfprApStorageFlexFlashDriveNumberOfBlocks_Type = Unsigned64
_CfprApStorageFlexFlashDriveNumberOfBlocks_Object = MibTableColumn
cfprApStorageFlexFlashDriveNumberOfBlocks = _CfprApStorageFlexFlashDriveNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 14),
    _CfprApStorageFlexFlashDriveNumberOfBlocks_Type()
)
cfprApStorageFlexFlashDriveNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveNumberOfBlocks.setStatus("current")
_CfprApStorageFlexFlashDriveOperQualifierReason_Type = SnmpAdminString
_CfprApStorageFlexFlashDriveOperQualifierReason_Object = MibTableColumn
cfprApStorageFlexFlashDriveOperQualifierReason = _CfprApStorageFlexFlashDriveOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 15),
    _CfprApStorageFlexFlashDriveOperQualifierReason_Type()
)
cfprApStorageFlexFlashDriveOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveOperQualifierReason.setStatus("current")
_CfprApStorageFlexFlashDriveOperability_Type = CfprApEquipmentOperability
_CfprApStorageFlexFlashDriveOperability_Object = MibTableColumn
cfprApStorageFlexFlashDriveOperability = _CfprApStorageFlexFlashDriveOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 16),
    _CfprApStorageFlexFlashDriveOperability_Type()
)
cfprApStorageFlexFlashDriveOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveOperability.setStatus("current")
_CfprApStorageFlexFlashDriveOperationState_Type = CfprApStorageOperationStateType
_CfprApStorageFlexFlashDriveOperationState_Object = MibTableColumn
cfprApStorageFlexFlashDriveOperationState = _CfprApStorageFlexFlashDriveOperationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 17),
    _CfprApStorageFlexFlashDriveOperationState_Type()
)
cfprApStorageFlexFlashDriveOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveOperationState.setStatus("current")
_CfprApStorageFlexFlashDrivePresence_Type = CfprApEquipmentPresence
_CfprApStorageFlexFlashDrivePresence_Object = MibTableColumn
cfprApStorageFlexFlashDrivePresence = _CfprApStorageFlexFlashDrivePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 18),
    _CfprApStorageFlexFlashDrivePresence_Type()
)
cfprApStorageFlexFlashDrivePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDrivePresence.setStatus("current")
_CfprApStorageFlexFlashDriveRemovable_Type = CfprApStorageFFDriveRemovable
_CfprApStorageFlexFlashDriveRemovable_Object = MibTableColumn
cfprApStorageFlexFlashDriveRemovable = _CfprApStorageFlexFlashDriveRemovable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 19),
    _CfprApStorageFlexFlashDriveRemovable_Type()
)
cfprApStorageFlexFlashDriveRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveRemovable.setStatus("current")
_CfprApStorageFlexFlashDriveRevision_Type = SnmpAdminString
_CfprApStorageFlexFlashDriveRevision_Object = MibTableColumn
cfprApStorageFlexFlashDriveRevision = _CfprApStorageFlexFlashDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 20),
    _CfprApStorageFlexFlashDriveRevision_Type()
)
cfprApStorageFlexFlashDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveRevision.setStatus("current")
_CfprApStorageFlexFlashDriveSerial_Type = SnmpAdminString
_CfprApStorageFlexFlashDriveSerial_Object = MibTableColumn
cfprApStorageFlexFlashDriveSerial = _CfprApStorageFlexFlashDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 21),
    _CfprApStorageFlexFlashDriveSerial_Type()
)
cfprApStorageFlexFlashDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveSerial.setStatus("current")
_CfprApStorageFlexFlashDriveSize_Type = Unsigned64
_CfprApStorageFlexFlashDriveSize_Object = MibTableColumn
cfprApStorageFlexFlashDriveSize = _CfprApStorageFlexFlashDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 22),
    _CfprApStorageFlexFlashDriveSize_Type()
)
cfprApStorageFlexFlashDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveSize.setStatus("current")
_CfprApStorageFlexFlashDriveSlotNumber_Type = Gauge32
_CfprApStorageFlexFlashDriveSlotNumber_Object = MibTableColumn
cfprApStorageFlexFlashDriveSlotNumber = _CfprApStorageFlexFlashDriveSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 23),
    _CfprApStorageFlexFlashDriveSlotNumber_Type()
)
cfprApStorageFlexFlashDriveSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveSlotNumber.setStatus("current")
_CfprApStorageFlexFlashDriveVendor_Type = SnmpAdminString
_CfprApStorageFlexFlashDriveVendor_Object = MibTableColumn
cfprApStorageFlexFlashDriveVendor = _CfprApStorageFlexFlashDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 24),
    _CfprApStorageFlexFlashDriveVendor_Type()
)
cfprApStorageFlexFlashDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveVendor.setStatus("current")
_CfprApStorageFlexFlashDriveVisible_Type = CfprApStorageFFDriveVisible
_CfprApStorageFlexFlashDriveVisible_Object = MibTableColumn
cfprApStorageFlexFlashDriveVisible = _CfprApStorageFlexFlashDriveVisible_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 15, 1, 25),
    _CfprApStorageFlexFlashDriveVisible_Type()
)
cfprApStorageFlexFlashDriveVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashDriveVisible.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveTable_Object = MibTable
cfprApStorageFlexFlashVirtualDriveTable = _CfprApStorageFlexFlashVirtualDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16)
)
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveTable.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveEntry_Object = MibTableRow
cfprApStorageFlexFlashVirtualDriveEntry = _CfprApStorageFlexFlashVirtualDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1)
)
cfprApStorageFlexFlashVirtualDriveEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageFlexFlashVirtualDriveInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveEntry.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveInstanceId_Type = CfprApManagedObjectId
_CfprApStorageFlexFlashVirtualDriveInstanceId_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveInstanceId = _CfprApStorageFlexFlashVirtualDriveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 1),
    _CfprApStorageFlexFlashVirtualDriveInstanceId_Type()
)
cfprApStorageFlexFlashVirtualDriveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveInstanceId.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveDn_Type = CfprApManagedObjectDn
_CfprApStorageFlexFlashVirtualDriveDn_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveDn = _CfprApStorageFlexFlashVirtualDriveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 2),
    _CfprApStorageFlexFlashVirtualDriveDn_Type()
)
cfprApStorageFlexFlashVirtualDriveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveDn.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveRn_Type = SnmpAdminString
_CfprApStorageFlexFlashVirtualDriveRn_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveRn = _CfprApStorageFlexFlashVirtualDriveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 3),
    _CfprApStorageFlexFlashVirtualDriveRn_Type()
)
cfprApStorageFlexFlashVirtualDriveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveRn.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveBlockSize_Type = Gauge32
_CfprApStorageFlexFlashVirtualDriveBlockSize_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveBlockSize = _CfprApStorageFlexFlashVirtualDriveBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 4),
    _CfprApStorageFlexFlashVirtualDriveBlockSize_Type()
)
cfprApStorageFlexFlashVirtualDriveBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveBlockSize.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveConnectionProtocol_Type = CfprApStorageConnectionProtocol
_CfprApStorageFlexFlashVirtualDriveConnectionProtocol_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveConnectionProtocol = _CfprApStorageFlexFlashVirtualDriveConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 5),
    _CfprApStorageFlexFlashVirtualDriveConnectionProtocol_Type()
)
cfprApStorageFlexFlashVirtualDriveConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveConnectionProtocol.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveId_Type = Gauge32
_CfprApStorageFlexFlashVirtualDriveId_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveId = _CfprApStorageFlexFlashVirtualDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 6),
    _CfprApStorageFlexFlashVirtualDriveId_Type()
)
cfprApStorageFlexFlashVirtualDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveId.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveModel_Type = SnmpAdminString
_CfprApStorageFlexFlashVirtualDriveModel_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveModel = _CfprApStorageFlexFlashVirtualDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 7),
    _CfprApStorageFlexFlashVirtualDriveModel_Type()
)
cfprApStorageFlexFlashVirtualDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveModel.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveNumberOfBlocks_Type = Unsigned64
_CfprApStorageFlexFlashVirtualDriveNumberOfBlocks_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveNumberOfBlocks = _CfprApStorageFlexFlashVirtualDriveNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 8),
    _CfprApStorageFlexFlashVirtualDriveNumberOfBlocks_Type()
)
cfprApStorageFlexFlashVirtualDriveNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveNumberOfBlocks.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveOperQualifierReason_Type = SnmpAdminString
_CfprApStorageFlexFlashVirtualDriveOperQualifierReason_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveOperQualifierReason = _CfprApStorageFlexFlashVirtualDriveOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 9),
    _CfprApStorageFlexFlashVirtualDriveOperQualifierReason_Type()
)
cfprApStorageFlexFlashVirtualDriveOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveOperQualifierReason.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveOperability_Type = CfprApEquipmentOperability
_CfprApStorageFlexFlashVirtualDriveOperability_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveOperability = _CfprApStorageFlexFlashVirtualDriveOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 10),
    _CfprApStorageFlexFlashVirtualDriveOperability_Type()
)
cfprApStorageFlexFlashVirtualDriveOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveOperability.setStatus("current")
_CfprApStorageFlexFlashVirtualDrivePresence_Type = CfprApEquipmentPresence
_CfprApStorageFlexFlashVirtualDrivePresence_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDrivePresence = _CfprApStorageFlexFlashVirtualDrivePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 11),
    _CfprApStorageFlexFlashVirtualDrivePresence_Type()
)
cfprApStorageFlexFlashVirtualDrivePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDrivePresence.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveRaidHealth_Type = CfprApStorageFFRAIDHealth
_CfprApStorageFlexFlashVirtualDriveRaidHealth_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveRaidHealth = _CfprApStorageFlexFlashVirtualDriveRaidHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 12),
    _CfprApStorageFlexFlashVirtualDriveRaidHealth_Type()
)
cfprApStorageFlexFlashVirtualDriveRaidHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveRaidHealth.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveRaidState_Type = CfprApStorageFFRAIDState
_CfprApStorageFlexFlashVirtualDriveRaidState_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveRaidState = _CfprApStorageFlexFlashVirtualDriveRaidState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 13),
    _CfprApStorageFlexFlashVirtualDriveRaidState_Type()
)
cfprApStorageFlexFlashVirtualDriveRaidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveRaidState.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveRevision_Type = SnmpAdminString
_CfprApStorageFlexFlashVirtualDriveRevision_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveRevision = _CfprApStorageFlexFlashVirtualDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 14),
    _CfprApStorageFlexFlashVirtualDriveRevision_Type()
)
cfprApStorageFlexFlashVirtualDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveRevision.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveSerial_Type = SnmpAdminString
_CfprApStorageFlexFlashVirtualDriveSerial_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveSerial = _CfprApStorageFlexFlashVirtualDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 15),
    _CfprApStorageFlexFlashVirtualDriveSerial_Type()
)
cfprApStorageFlexFlashVirtualDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveSerial.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveSize_Type = Unsigned64
_CfprApStorageFlexFlashVirtualDriveSize_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveSize = _CfprApStorageFlexFlashVirtualDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 16),
    _CfprApStorageFlexFlashVirtualDriveSize_Type()
)
cfprApStorageFlexFlashVirtualDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveSize.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveType_Type = CfprApStorageLunType
_CfprApStorageFlexFlashVirtualDriveType_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveType = _CfprApStorageFlexFlashVirtualDriveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 17),
    _CfprApStorageFlexFlashVirtualDriveType_Type()
)
cfprApStorageFlexFlashVirtualDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveType.setStatus("current")
_CfprApStorageFlexFlashVirtualDriveVendor_Type = SnmpAdminString
_CfprApStorageFlexFlashVirtualDriveVendor_Object = MibTableColumn
cfprApStorageFlexFlashVirtualDriveVendor = _CfprApStorageFlexFlashVirtualDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 16, 1, 18),
    _CfprApStorageFlexFlashVirtualDriveVendor_Type()
)
cfprApStorageFlexFlashVirtualDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageFlexFlashVirtualDriveVendor.setStatus("current")
_CfprApStorageIScsiTargetIfTable_Object = MibTable
cfprApStorageIScsiTargetIfTable = _CfprApStorageIScsiTargetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 17)
)
if mibBuilder.loadTexts:
    cfprApStorageIScsiTargetIfTable.setStatus("current")
_CfprApStorageIScsiTargetIfEntry_Object = MibTableRow
cfprApStorageIScsiTargetIfEntry = _CfprApStorageIScsiTargetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 17, 1)
)
cfprApStorageIScsiTargetIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageIScsiTargetIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageIScsiTargetIfEntry.setStatus("current")
_CfprApStorageIScsiTargetIfInstanceId_Type = CfprApManagedObjectId
_CfprApStorageIScsiTargetIfInstanceId_Object = MibTableColumn
cfprApStorageIScsiTargetIfInstanceId = _CfprApStorageIScsiTargetIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 17, 1, 1),
    _CfprApStorageIScsiTargetIfInstanceId_Type()
)
cfprApStorageIScsiTargetIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageIScsiTargetIfInstanceId.setStatus("current")
_CfprApStorageIScsiTargetIfDn_Type = CfprApManagedObjectDn
_CfprApStorageIScsiTargetIfDn_Object = MibTableColumn
cfprApStorageIScsiTargetIfDn = _CfprApStorageIScsiTargetIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 17, 1, 2),
    _CfprApStorageIScsiTargetIfDn_Type()
)
cfprApStorageIScsiTargetIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageIScsiTargetIfDn.setStatus("current")
_CfprApStorageIScsiTargetIfRn_Type = SnmpAdminString
_CfprApStorageIScsiTargetIfRn_Object = MibTableColumn
cfprApStorageIScsiTargetIfRn = _CfprApStorageIScsiTargetIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 17, 1, 3),
    _CfprApStorageIScsiTargetIfRn_Type()
)
cfprApStorageIScsiTargetIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageIScsiTargetIfRn.setStatus("current")
_CfprApStorageIScsiTargetIfName_Type = SnmpAdminString
_CfprApStorageIScsiTargetIfName_Object = MibTableColumn
cfprApStorageIScsiTargetIfName = _CfprApStorageIScsiTargetIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 17, 1, 4),
    _CfprApStorageIScsiTargetIfName_Type()
)
cfprApStorageIScsiTargetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageIScsiTargetIfName.setStatus("current")
_CfprApStorageIScsiTargetIfProt_Type = CfprApStorageProtocol
_CfprApStorageIScsiTargetIfProt_Object = MibTableColumn
cfprApStorageIScsiTargetIfProt = _CfprApStorageIScsiTargetIfProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 17, 1, 5),
    _CfprApStorageIScsiTargetIfProt_Type()
)
cfprApStorageIScsiTargetIfProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageIScsiTargetIfProt.setStatus("current")
_CfprApStorageItemTable_Object = MibTable
cfprApStorageItemTable = _CfprApStorageItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 20)
)
if mibBuilder.loadTexts:
    cfprApStorageItemTable.setStatus("current")
_CfprApStorageItemEntry_Object = MibTableRow
cfprApStorageItemEntry = _CfprApStorageItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 20, 1)
)
cfprApStorageItemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageItemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageItemEntry.setStatus("current")
_CfprApStorageItemInstanceId_Type = CfprApManagedObjectId
_CfprApStorageItemInstanceId_Object = MibTableColumn
cfprApStorageItemInstanceId = _CfprApStorageItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 20, 1, 1),
    _CfprApStorageItemInstanceId_Type()
)
cfprApStorageItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageItemInstanceId.setStatus("current")
_CfprApStorageItemDn_Type = CfprApManagedObjectDn
_CfprApStorageItemDn_Object = MibTableColumn
cfprApStorageItemDn = _CfprApStorageItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 20, 1, 2),
    _CfprApStorageItemDn_Type()
)
cfprApStorageItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageItemDn.setStatus("current")
_CfprApStorageItemRn_Type = SnmpAdminString
_CfprApStorageItemRn_Object = MibTableColumn
cfprApStorageItemRn = _CfprApStorageItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 20, 1, 3),
    _CfprApStorageItemRn_Type()
)
cfprApStorageItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageItemRn.setStatus("current")
_CfprApStorageItemName_Type = SnmpAdminString
_CfprApStorageItemName_Object = MibTableColumn
cfprApStorageItemName = _CfprApStorageItemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 20, 1, 4),
    _CfprApStorageItemName_Type()
)
cfprApStorageItemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageItemName.setStatus("current")
_CfprApStorageItemOperState_Type = CfprApStorageFileSystemStatus
_CfprApStorageItemOperState_Object = MibTableColumn
cfprApStorageItemOperState = _CfprApStorageItemOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 20, 1, 5),
    _CfprApStorageItemOperState_Type()
)
cfprApStorageItemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageItemOperState.setStatus("current")
_CfprApStorageItemSize_Type = Unsigned64
_CfprApStorageItemSize_Object = MibTableColumn
cfprApStorageItemSize = _CfprApStorageItemSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 20, 1, 6),
    _CfprApStorageItemSize_Type()
)
cfprApStorageItemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageItemSize.setStatus("current")
_CfprApStorageItemUsed_Type = Gauge32
_CfprApStorageItemUsed_Object = MibTableColumn
cfprApStorageItemUsed = _CfprApStorageItemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 20, 1, 7),
    _CfprApStorageItemUsed_Type()
)
cfprApStorageItemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageItemUsed.setStatus("current")
_CfprApStorageLocalDiskTable_Object = MibTable
cfprApStorageLocalDiskTable = _CfprApStorageLocalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21)
)
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskTable.setStatus("current")
_CfprApStorageLocalDiskEntry_Object = MibTableRow
cfprApStorageLocalDiskEntry = _CfprApStorageLocalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1)
)
cfprApStorageLocalDiskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageLocalDiskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskEntry.setStatus("current")
_CfprApStorageLocalDiskInstanceId_Type = CfprApManagedObjectId
_CfprApStorageLocalDiskInstanceId_Object = MibTableColumn
cfprApStorageLocalDiskInstanceId = _CfprApStorageLocalDiskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 1),
    _CfprApStorageLocalDiskInstanceId_Type()
)
cfprApStorageLocalDiskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskInstanceId.setStatus("current")
_CfprApStorageLocalDiskDn_Type = CfprApManagedObjectDn
_CfprApStorageLocalDiskDn_Object = MibTableColumn
cfprApStorageLocalDiskDn = _CfprApStorageLocalDiskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 2),
    _CfprApStorageLocalDiskDn_Type()
)
cfprApStorageLocalDiskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskDn.setStatus("current")
_CfprApStorageLocalDiskRn_Type = SnmpAdminString
_CfprApStorageLocalDiskRn_Object = MibTableColumn
cfprApStorageLocalDiskRn = _CfprApStorageLocalDiskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 3),
    _CfprApStorageLocalDiskRn_Type()
)
cfprApStorageLocalDiskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskRn.setStatus("current")
_CfprApStorageLocalDiskBlockSize_Type = Gauge32
_CfprApStorageLocalDiskBlockSize_Object = MibTableColumn
cfprApStorageLocalDiskBlockSize = _CfprApStorageLocalDiskBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 4),
    _CfprApStorageLocalDiskBlockSize_Type()
)
cfprApStorageLocalDiskBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskBlockSize.setStatus("current")
_CfprApStorageLocalDiskConnectionProtocol_Type = CfprApStorageConnectionProtocol
_CfprApStorageLocalDiskConnectionProtocol_Object = MibTableColumn
cfprApStorageLocalDiskConnectionProtocol = _CfprApStorageLocalDiskConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 5),
    _CfprApStorageLocalDiskConnectionProtocol_Type()
)
cfprApStorageLocalDiskConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConnectionProtocol.setStatus("current")
_CfprApStorageLocalDiskDeviceType_Type = CfprApStorageTechnology
_CfprApStorageLocalDiskDeviceType_Object = MibTableColumn
cfprApStorageLocalDiskDeviceType = _CfprApStorageLocalDiskDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 6),
    _CfprApStorageLocalDiskDeviceType_Type()
)
cfprApStorageLocalDiskDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskDeviceType.setStatus("current")
_CfprApStorageLocalDiskDiskState_Type = CfprApStoragePDriveStatus
_CfprApStorageLocalDiskDiskState_Object = MibTableColumn
cfprApStorageLocalDiskDiskState = _CfprApStorageLocalDiskDiskState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 7),
    _CfprApStorageLocalDiskDiskState_Type()
)
cfprApStorageLocalDiskDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskDiskState.setStatus("current")
_CfprApStorageLocalDiskId_Type = Gauge32
_CfprApStorageLocalDiskId_Object = MibTableColumn
cfprApStorageLocalDiskId = _CfprApStorageLocalDiskId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 8),
    _CfprApStorageLocalDiskId_Type()
)
cfprApStorageLocalDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskId.setStatus("current")
_CfprApStorageLocalDiskLc_Type = CfprApFsmLifecycle
_CfprApStorageLocalDiskLc_Object = MibTableColumn
cfprApStorageLocalDiskLc = _CfprApStorageLocalDiskLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 9),
    _CfprApStorageLocalDiskLc_Type()
)
cfprApStorageLocalDiskLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskLc.setStatus("current")
_CfprApStorageLocalDiskLinkSpeed_Type = CfprApStorageLinkSpeed
_CfprApStorageLocalDiskLinkSpeed_Object = MibTableColumn
cfprApStorageLocalDiskLinkSpeed = _CfprApStorageLocalDiskLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 10),
    _CfprApStorageLocalDiskLinkSpeed_Type()
)
cfprApStorageLocalDiskLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskLinkSpeed.setStatus("current")
_CfprApStorageLocalDiskModel_Type = SnmpAdminString
_CfprApStorageLocalDiskModel_Object = MibTableColumn
cfprApStorageLocalDiskModel = _CfprApStorageLocalDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 11),
    _CfprApStorageLocalDiskModel_Type()
)
cfprApStorageLocalDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskModel.setStatus("current")
_CfprApStorageLocalDiskNumberOfBlocks_Type = Unsigned64
_CfprApStorageLocalDiskNumberOfBlocks_Object = MibTableColumn
cfprApStorageLocalDiskNumberOfBlocks = _CfprApStorageLocalDiskNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 12),
    _CfprApStorageLocalDiskNumberOfBlocks_Type()
)
cfprApStorageLocalDiskNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskNumberOfBlocks.setStatus("current")
_CfprApStorageLocalDiskOperQualifierReason_Type = SnmpAdminString
_CfprApStorageLocalDiskOperQualifierReason_Object = MibTableColumn
cfprApStorageLocalDiskOperQualifierReason = _CfprApStorageLocalDiskOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 13),
    _CfprApStorageLocalDiskOperQualifierReason_Type()
)
cfprApStorageLocalDiskOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskOperQualifierReason.setStatus("current")
_CfprApStorageLocalDiskOperability_Type = CfprApEquipmentOperability
_CfprApStorageLocalDiskOperability_Object = MibTableColumn
cfprApStorageLocalDiskOperability = _CfprApStorageLocalDiskOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 14),
    _CfprApStorageLocalDiskOperability_Type()
)
cfprApStorageLocalDiskOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskOperability.setStatus("current")
_CfprApStorageLocalDiskPowerState_Type = CfprApStoragePowerState
_CfprApStorageLocalDiskPowerState_Object = MibTableColumn
cfprApStorageLocalDiskPowerState = _CfprApStorageLocalDiskPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 15),
    _CfprApStorageLocalDiskPowerState_Type()
)
cfprApStorageLocalDiskPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPowerState.setStatus("current")
_CfprApStorageLocalDiskPresence_Type = CfprApEquipmentPresence
_CfprApStorageLocalDiskPresence_Object = MibTableColumn
cfprApStorageLocalDiskPresence = _CfprApStorageLocalDiskPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 16),
    _CfprApStorageLocalDiskPresence_Type()
)
cfprApStorageLocalDiskPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPresence.setStatus("current")
_CfprApStorageLocalDiskRevision_Type = SnmpAdminString
_CfprApStorageLocalDiskRevision_Object = MibTableColumn
cfprApStorageLocalDiskRevision = _CfprApStorageLocalDiskRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 17),
    _CfprApStorageLocalDiskRevision_Type()
)
cfprApStorageLocalDiskRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskRevision.setStatus("current")
_CfprApStorageLocalDiskSerial_Type = SnmpAdminString
_CfprApStorageLocalDiskSerial_Object = MibTableColumn
cfprApStorageLocalDiskSerial = _CfprApStorageLocalDiskSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 18),
    _CfprApStorageLocalDiskSerial_Type()
)
cfprApStorageLocalDiskSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSerial.setStatus("current")
_CfprApStorageLocalDiskSize_Type = Unsigned64
_CfprApStorageLocalDiskSize_Object = MibTableColumn
cfprApStorageLocalDiskSize = _CfprApStorageLocalDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 19),
    _CfprApStorageLocalDiskSize_Type()
)
cfprApStorageLocalDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSize.setStatus("current")
_CfprApStorageLocalDiskVendor_Type = SnmpAdminString
_CfprApStorageLocalDiskVendor_Object = MibTableColumn
cfprApStorageLocalDiskVendor = _CfprApStorageLocalDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 21, 1, 20),
    _CfprApStorageLocalDiskVendor_Type()
)
cfprApStorageLocalDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskVendor.setStatus("current")
_CfprApStorageLocalDiskConfigDefTable_Object = MibTable
cfprApStorageLocalDiskConfigDefTable = _CfprApStorageLocalDiskConfigDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22)
)
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefTable.setStatus("current")
_CfprApStorageLocalDiskConfigDefEntry_Object = MibTableRow
cfprApStorageLocalDiskConfigDefEntry = _CfprApStorageLocalDiskConfigDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1)
)
cfprApStorageLocalDiskConfigDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageLocalDiskConfigDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefEntry.setStatus("current")
_CfprApStorageLocalDiskConfigDefInstanceId_Type = CfprApManagedObjectId
_CfprApStorageLocalDiskConfigDefInstanceId_Object = MibTableColumn
cfprApStorageLocalDiskConfigDefInstanceId = _CfprApStorageLocalDiskConfigDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1, 1),
    _CfprApStorageLocalDiskConfigDefInstanceId_Type()
)
cfprApStorageLocalDiskConfigDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefInstanceId.setStatus("current")
_CfprApStorageLocalDiskConfigDefDn_Type = CfprApManagedObjectDn
_CfprApStorageLocalDiskConfigDefDn_Object = MibTableColumn
cfprApStorageLocalDiskConfigDefDn = _CfprApStorageLocalDiskConfigDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1, 2),
    _CfprApStorageLocalDiskConfigDefDn_Type()
)
cfprApStorageLocalDiskConfigDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefDn.setStatus("current")
_CfprApStorageLocalDiskConfigDefRn_Type = SnmpAdminString
_CfprApStorageLocalDiskConfigDefRn_Object = MibTableColumn
cfprApStorageLocalDiskConfigDefRn = _CfprApStorageLocalDiskConfigDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1, 3),
    _CfprApStorageLocalDiskConfigDefRn_Type()
)
cfprApStorageLocalDiskConfigDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefRn.setStatus("current")
_CfprApStorageLocalDiskConfigDefDescr_Type = SnmpAdminString
_CfprApStorageLocalDiskConfigDefDescr_Object = MibTableColumn
cfprApStorageLocalDiskConfigDefDescr = _CfprApStorageLocalDiskConfigDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1, 4),
    _CfprApStorageLocalDiskConfigDefDescr_Type()
)
cfprApStorageLocalDiskConfigDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefDescr.setStatus("current")
_CfprApStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Type = CfprApStorageLocalDiskConfigFlexFlashRAIDReportingState
_CfprApStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Object = MibTableColumn
cfprApStorageLocalDiskConfigDefFlexFlashRAIDReportingState = _CfprApStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1, 5),
    _CfprApStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Type()
)
cfprApStorageLocalDiskConfigDefFlexFlashRAIDReportingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefFlexFlashRAIDReportingState.setStatus("current")
_CfprApStorageLocalDiskConfigDefFlexFlashState_Type = CfprApStorageLocalDiskConfigFlexFlashState
_CfprApStorageLocalDiskConfigDefFlexFlashState_Object = MibTableColumn
cfprApStorageLocalDiskConfigDefFlexFlashState = _CfprApStorageLocalDiskConfigDefFlexFlashState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1, 6),
    _CfprApStorageLocalDiskConfigDefFlexFlashState_Type()
)
cfprApStorageLocalDiskConfigDefFlexFlashState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefFlexFlashState.setStatus("current")
_CfprApStorageLocalDiskConfigDefIntId_Type = SnmpAdminString
_CfprApStorageLocalDiskConfigDefIntId_Object = MibTableColumn
cfprApStorageLocalDiskConfigDefIntId = _CfprApStorageLocalDiskConfigDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1, 7),
    _CfprApStorageLocalDiskConfigDefIntId_Type()
)
cfprApStorageLocalDiskConfigDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefIntId.setStatus("current")
_CfprApStorageLocalDiskConfigDefMode_Type = CfprApStorageLocalDiskMode
_CfprApStorageLocalDiskConfigDefMode_Object = MibTableColumn
cfprApStorageLocalDiskConfigDefMode = _CfprApStorageLocalDiskConfigDefMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1, 8),
    _CfprApStorageLocalDiskConfigDefMode_Type()
)
cfprApStorageLocalDiskConfigDefMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefMode.setStatus("current")
_CfprApStorageLocalDiskConfigDefName_Type = SnmpAdminString
_CfprApStorageLocalDiskConfigDefName_Object = MibTableColumn
cfprApStorageLocalDiskConfigDefName = _CfprApStorageLocalDiskConfigDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1, 9),
    _CfprApStorageLocalDiskConfigDefName_Type()
)
cfprApStorageLocalDiskConfigDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefName.setStatus("current")
_CfprApStorageLocalDiskConfigDefPolicyLevel_Type = Gauge32
_CfprApStorageLocalDiskConfigDefPolicyLevel_Object = MibTableColumn
cfprApStorageLocalDiskConfigDefPolicyLevel = _CfprApStorageLocalDiskConfigDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1, 10),
    _CfprApStorageLocalDiskConfigDefPolicyLevel_Type()
)
cfprApStorageLocalDiskConfigDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefPolicyLevel.setStatus("current")
_CfprApStorageLocalDiskConfigDefPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApStorageLocalDiskConfigDefPolicyOwner_Object = MibTableColumn
cfprApStorageLocalDiskConfigDefPolicyOwner = _CfprApStorageLocalDiskConfigDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1, 11),
    _CfprApStorageLocalDiskConfigDefPolicyOwner_Type()
)
cfprApStorageLocalDiskConfigDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefPolicyOwner.setStatus("current")
_CfprApStorageLocalDiskConfigDefProtectConfig_Type = TruthValue
_CfprApStorageLocalDiskConfigDefProtectConfig_Object = MibTableColumn
cfprApStorageLocalDiskConfigDefProtectConfig = _CfprApStorageLocalDiskConfigDefProtectConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 22, 1, 12),
    _CfprApStorageLocalDiskConfigDefProtectConfig_Type()
)
cfprApStorageLocalDiskConfigDefProtectConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigDefProtectConfig.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyTable_Object = MibTable
cfprApStorageLocalDiskConfigPolicyTable = _CfprApStorageLocalDiskConfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23)
)
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyTable.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyEntry_Object = MibTableRow
cfprApStorageLocalDiskConfigPolicyEntry = _CfprApStorageLocalDiskConfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1)
)
cfprApStorageLocalDiskConfigPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageLocalDiskConfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyEntry.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApStorageLocalDiskConfigPolicyInstanceId_Object = MibTableColumn
cfprApStorageLocalDiskConfigPolicyInstanceId = _CfprApStorageLocalDiskConfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1, 1),
    _CfprApStorageLocalDiskConfigPolicyInstanceId_Type()
)
cfprApStorageLocalDiskConfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyInstanceId.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyDn_Type = CfprApManagedObjectDn
_CfprApStorageLocalDiskConfigPolicyDn_Object = MibTableColumn
cfprApStorageLocalDiskConfigPolicyDn = _CfprApStorageLocalDiskConfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1, 2),
    _CfprApStorageLocalDiskConfigPolicyDn_Type()
)
cfprApStorageLocalDiskConfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyDn.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyRn_Type = SnmpAdminString
_CfprApStorageLocalDiskConfigPolicyRn_Object = MibTableColumn
cfprApStorageLocalDiskConfigPolicyRn = _CfprApStorageLocalDiskConfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1, 3),
    _CfprApStorageLocalDiskConfigPolicyRn_Type()
)
cfprApStorageLocalDiskConfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyRn.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyDescr_Type = SnmpAdminString
_CfprApStorageLocalDiskConfigPolicyDescr_Object = MibTableColumn
cfprApStorageLocalDiskConfigPolicyDescr = _CfprApStorageLocalDiskConfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1, 4),
    _CfprApStorageLocalDiskConfigPolicyDescr_Type()
)
cfprApStorageLocalDiskConfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyDescr.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Type = CfprApStorageLocalDiskConfigFlexFlashRAIDReportingState
_CfprApStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Object = MibTableColumn
cfprApStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState = _CfprApStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1, 5),
    _CfprApStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Type()
)
cfprApStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyFlexFlashState_Type = CfprApStorageLocalDiskConfigFlexFlashState
_CfprApStorageLocalDiskConfigPolicyFlexFlashState_Object = MibTableColumn
cfprApStorageLocalDiskConfigPolicyFlexFlashState = _CfprApStorageLocalDiskConfigPolicyFlexFlashState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1, 6),
    _CfprApStorageLocalDiskConfigPolicyFlexFlashState_Type()
)
cfprApStorageLocalDiskConfigPolicyFlexFlashState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyFlexFlashState.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyIntId_Type = SnmpAdminString
_CfprApStorageLocalDiskConfigPolicyIntId_Object = MibTableColumn
cfprApStorageLocalDiskConfigPolicyIntId = _CfprApStorageLocalDiskConfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1, 7),
    _CfprApStorageLocalDiskConfigPolicyIntId_Type()
)
cfprApStorageLocalDiskConfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyIntId.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyMode_Type = CfprApStorageLocalDiskMode
_CfprApStorageLocalDiskConfigPolicyMode_Object = MibTableColumn
cfprApStorageLocalDiskConfigPolicyMode = _CfprApStorageLocalDiskConfigPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1, 8),
    _CfprApStorageLocalDiskConfigPolicyMode_Type()
)
cfprApStorageLocalDiskConfigPolicyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyMode.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyName_Type = SnmpAdminString
_CfprApStorageLocalDiskConfigPolicyName_Object = MibTableColumn
cfprApStorageLocalDiskConfigPolicyName = _CfprApStorageLocalDiskConfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1, 9),
    _CfprApStorageLocalDiskConfigPolicyName_Type()
)
cfprApStorageLocalDiskConfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyName.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyPolicyLevel_Type = Gauge32
_CfprApStorageLocalDiskConfigPolicyPolicyLevel_Object = MibTableColumn
cfprApStorageLocalDiskConfigPolicyPolicyLevel = _CfprApStorageLocalDiskConfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1, 10),
    _CfprApStorageLocalDiskConfigPolicyPolicyLevel_Type()
)
cfprApStorageLocalDiskConfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyPolicyLevel.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApStorageLocalDiskConfigPolicyPolicyOwner_Object = MibTableColumn
cfprApStorageLocalDiskConfigPolicyPolicyOwner = _CfprApStorageLocalDiskConfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1, 11),
    _CfprApStorageLocalDiskConfigPolicyPolicyOwner_Type()
)
cfprApStorageLocalDiskConfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyPolicyOwner.setStatus("current")
_CfprApStorageLocalDiskConfigPolicyProtectConfig_Type = TruthValue
_CfprApStorageLocalDiskConfigPolicyProtectConfig_Object = MibTableColumn
cfprApStorageLocalDiskConfigPolicyProtectConfig = _CfprApStorageLocalDiskConfigPolicyProtectConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 23, 1, 12),
    _CfprApStorageLocalDiskConfigPolicyProtectConfig_Type()
)
cfprApStorageLocalDiskConfigPolicyProtectConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskConfigPolicyProtectConfig.setStatus("current")
_CfprApStorageLocalDiskPartitionTable_Object = MibTable
cfprApStorageLocalDiskPartitionTable = _CfprApStorageLocalDiskPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24)
)
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionTable.setStatus("current")
_CfprApStorageLocalDiskPartitionEntry_Object = MibTableRow
cfprApStorageLocalDiskPartitionEntry = _CfprApStorageLocalDiskPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24, 1)
)
cfprApStorageLocalDiskPartitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageLocalDiskPartitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionEntry.setStatus("current")
_CfprApStorageLocalDiskPartitionInstanceId_Type = CfprApManagedObjectId
_CfprApStorageLocalDiskPartitionInstanceId_Object = MibTableColumn
cfprApStorageLocalDiskPartitionInstanceId = _CfprApStorageLocalDiskPartitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24, 1, 1),
    _CfprApStorageLocalDiskPartitionInstanceId_Type()
)
cfprApStorageLocalDiskPartitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionInstanceId.setStatus("current")
_CfprApStorageLocalDiskPartitionDn_Type = CfprApManagedObjectDn
_CfprApStorageLocalDiskPartitionDn_Object = MibTableColumn
cfprApStorageLocalDiskPartitionDn = _CfprApStorageLocalDiskPartitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24, 1, 2),
    _CfprApStorageLocalDiskPartitionDn_Type()
)
cfprApStorageLocalDiskPartitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionDn.setStatus("current")
_CfprApStorageLocalDiskPartitionRn_Type = SnmpAdminString
_CfprApStorageLocalDiskPartitionRn_Object = MibTableColumn
cfprApStorageLocalDiskPartitionRn = _CfprApStorageLocalDiskPartitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24, 1, 3),
    _CfprApStorageLocalDiskPartitionRn_Type()
)
cfprApStorageLocalDiskPartitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionRn.setStatus("current")
_CfprApStorageLocalDiskPartitionDescr_Type = SnmpAdminString
_CfprApStorageLocalDiskPartitionDescr_Object = MibTableColumn
cfprApStorageLocalDiskPartitionDescr = _CfprApStorageLocalDiskPartitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24, 1, 4),
    _CfprApStorageLocalDiskPartitionDescr_Type()
)
cfprApStorageLocalDiskPartitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionDescr.setStatus("current")
_CfprApStorageLocalDiskPartitionIntId_Type = SnmpAdminString
_CfprApStorageLocalDiskPartitionIntId_Object = MibTableColumn
cfprApStorageLocalDiskPartitionIntId = _CfprApStorageLocalDiskPartitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24, 1, 5),
    _CfprApStorageLocalDiskPartitionIntId_Type()
)
cfprApStorageLocalDiskPartitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionIntId.setStatus("current")
_CfprApStorageLocalDiskPartitionName_Type = SnmpAdminString
_CfprApStorageLocalDiskPartitionName_Object = MibTableColumn
cfprApStorageLocalDiskPartitionName = _CfprApStorageLocalDiskPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24, 1, 6),
    _CfprApStorageLocalDiskPartitionName_Type()
)
cfprApStorageLocalDiskPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionName.setStatus("current")
_CfprApStorageLocalDiskPartitionOrder_Type = Gauge32
_CfprApStorageLocalDiskPartitionOrder_Object = MibTableColumn
cfprApStorageLocalDiskPartitionOrder = _CfprApStorageLocalDiskPartitionOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24, 1, 7),
    _CfprApStorageLocalDiskPartitionOrder_Type()
)
cfprApStorageLocalDiskPartitionOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionOrder.setStatus("current")
_CfprApStorageLocalDiskPartitionPolicyLevel_Type = Gauge32
_CfprApStorageLocalDiskPartitionPolicyLevel_Object = MibTableColumn
cfprApStorageLocalDiskPartitionPolicyLevel = _CfprApStorageLocalDiskPartitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24, 1, 8),
    _CfprApStorageLocalDiskPartitionPolicyLevel_Type()
)
cfprApStorageLocalDiskPartitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionPolicyLevel.setStatus("current")
_CfprApStorageLocalDiskPartitionPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApStorageLocalDiskPartitionPolicyOwner_Object = MibTableColumn
cfprApStorageLocalDiskPartitionPolicyOwner = _CfprApStorageLocalDiskPartitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24, 1, 9),
    _CfprApStorageLocalDiskPartitionPolicyOwner_Type()
)
cfprApStorageLocalDiskPartitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionPolicyOwner.setStatus("current")
_CfprApStorageLocalDiskPartitionSize_Type = Unsigned64
_CfprApStorageLocalDiskPartitionSize_Object = MibTableColumn
cfprApStorageLocalDiskPartitionSize = _CfprApStorageLocalDiskPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24, 1, 10),
    _CfprApStorageLocalDiskPartitionSize_Type()
)
cfprApStorageLocalDiskPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionSize.setStatus("current")
_CfprApStorageLocalDiskPartitionType_Type = CfprApStorageLocalDiskPartitionType
_CfprApStorageLocalDiskPartitionType_Object = MibTableColumn
cfprApStorageLocalDiskPartitionType = _CfprApStorageLocalDiskPartitionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 24, 1, 11),
    _CfprApStorageLocalDiskPartitionType_Type()
)
cfprApStorageLocalDiskPartitionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskPartitionType.setStatus("current")
_CfprApStorageLocalDiskSlotEpTable_Object = MibTable
cfprApStorageLocalDiskSlotEpTable = _CfprApStorageLocalDiskSlotEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 25)
)
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSlotEpTable.setStatus("current")
_CfprApStorageLocalDiskSlotEpEntry_Object = MibTableRow
cfprApStorageLocalDiskSlotEpEntry = _CfprApStorageLocalDiskSlotEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 25, 1)
)
cfprApStorageLocalDiskSlotEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageLocalDiskSlotEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSlotEpEntry.setStatus("current")
_CfprApStorageLocalDiskSlotEpInstanceId_Type = CfprApManagedObjectId
_CfprApStorageLocalDiskSlotEpInstanceId_Object = MibTableColumn
cfprApStorageLocalDiskSlotEpInstanceId = _CfprApStorageLocalDiskSlotEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 25, 1, 1),
    _CfprApStorageLocalDiskSlotEpInstanceId_Type()
)
cfprApStorageLocalDiskSlotEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSlotEpInstanceId.setStatus("current")
_CfprApStorageLocalDiskSlotEpDn_Type = CfprApManagedObjectDn
_CfprApStorageLocalDiskSlotEpDn_Object = MibTableColumn
cfprApStorageLocalDiskSlotEpDn = _CfprApStorageLocalDiskSlotEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 25, 1, 2),
    _CfprApStorageLocalDiskSlotEpDn_Type()
)
cfprApStorageLocalDiskSlotEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSlotEpDn.setStatus("current")
_CfprApStorageLocalDiskSlotEpRn_Type = SnmpAdminString
_CfprApStorageLocalDiskSlotEpRn_Object = MibTableColumn
cfprApStorageLocalDiskSlotEpRn = _CfprApStorageLocalDiskSlotEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 25, 1, 3),
    _CfprApStorageLocalDiskSlotEpRn_Type()
)
cfprApStorageLocalDiskSlotEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSlotEpRn.setStatus("current")
_CfprApStorageLocalDiskSlotEpConfiguration_Type = CfprApStorageConfiguration
_CfprApStorageLocalDiskSlotEpConfiguration_Object = MibTableColumn
cfprApStorageLocalDiskSlotEpConfiguration = _CfprApStorageLocalDiskSlotEpConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 25, 1, 4),
    _CfprApStorageLocalDiskSlotEpConfiguration_Type()
)
cfprApStorageLocalDiskSlotEpConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSlotEpConfiguration.setStatus("current")
_CfprApStorageLocalDiskSlotEpId_Type = Gauge32
_CfprApStorageLocalDiskSlotEpId_Object = MibTableColumn
cfprApStorageLocalDiskSlotEpId = _CfprApStorageLocalDiskSlotEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 25, 1, 5),
    _CfprApStorageLocalDiskSlotEpId_Type()
)
cfprApStorageLocalDiskSlotEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSlotEpId.setStatus("current")
_CfprApStorageLocalDiskSlotEpOperQualifierReason_Type = SnmpAdminString
_CfprApStorageLocalDiskSlotEpOperQualifierReason_Object = MibTableColumn
cfprApStorageLocalDiskSlotEpOperQualifierReason = _CfprApStorageLocalDiskSlotEpOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 25, 1, 6),
    _CfprApStorageLocalDiskSlotEpOperQualifierReason_Type()
)
cfprApStorageLocalDiskSlotEpOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSlotEpOperQualifierReason.setStatus("current")
_CfprApStorageLocalDiskSlotEpOperability_Type = CfprApEquipmentOperability
_CfprApStorageLocalDiskSlotEpOperability_Object = MibTableColumn
cfprApStorageLocalDiskSlotEpOperability = _CfprApStorageLocalDiskSlotEpOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 25, 1, 7),
    _CfprApStorageLocalDiskSlotEpOperability_Type()
)
cfprApStorageLocalDiskSlotEpOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSlotEpOperability.setStatus("current")
_CfprApStorageLocalDiskSlotEpPeerDn_Type = SnmpAdminString
_CfprApStorageLocalDiskSlotEpPeerDn_Object = MibTableColumn
cfprApStorageLocalDiskSlotEpPeerDn = _CfprApStorageLocalDiskSlotEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 25, 1, 8),
    _CfprApStorageLocalDiskSlotEpPeerDn_Type()
)
cfprApStorageLocalDiskSlotEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSlotEpPeerDn.setStatus("current")
_CfprApStorageLocalDiskSlotEpPresence_Type = CfprApEquipmentPresence
_CfprApStorageLocalDiskSlotEpPresence_Object = MibTableColumn
cfprApStorageLocalDiskSlotEpPresence = _CfprApStorageLocalDiskSlotEpPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 25, 1, 9),
    _CfprApStorageLocalDiskSlotEpPresence_Type()
)
cfprApStorageLocalDiskSlotEpPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalDiskSlotEpPresence.setStatus("current")
_CfprApStorageLocalLunTable_Object = MibTable
cfprApStorageLocalLunTable = _CfprApStorageLocalLunTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26)
)
if mibBuilder.loadTexts:
    cfprApStorageLocalLunTable.setStatus("current")
_CfprApStorageLocalLunEntry_Object = MibTableRow
cfprApStorageLocalLunEntry = _CfprApStorageLocalLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1)
)
cfprApStorageLocalLunEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageLocalLunInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageLocalLunEntry.setStatus("current")
_CfprApStorageLocalLunInstanceId_Type = CfprApManagedObjectId
_CfprApStorageLocalLunInstanceId_Object = MibTableColumn
cfprApStorageLocalLunInstanceId = _CfprApStorageLocalLunInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 1),
    _CfprApStorageLocalLunInstanceId_Type()
)
cfprApStorageLocalLunInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunInstanceId.setStatus("current")
_CfprApStorageLocalLunDn_Type = CfprApManagedObjectDn
_CfprApStorageLocalLunDn_Object = MibTableColumn
cfprApStorageLocalLunDn = _CfprApStorageLocalLunDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 2),
    _CfprApStorageLocalLunDn_Type()
)
cfprApStorageLocalLunDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunDn.setStatus("current")
_CfprApStorageLocalLunRn_Type = SnmpAdminString
_CfprApStorageLocalLunRn_Object = MibTableColumn
cfprApStorageLocalLunRn = _CfprApStorageLocalLunRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 3),
    _CfprApStorageLocalLunRn_Type()
)
cfprApStorageLocalLunRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunRn.setStatus("current")
_CfprApStorageLocalLunBlockSize_Type = Gauge32
_CfprApStorageLocalLunBlockSize_Object = MibTableColumn
cfprApStorageLocalLunBlockSize = _CfprApStorageLocalLunBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 4),
    _CfprApStorageLocalLunBlockSize_Type()
)
cfprApStorageLocalLunBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunBlockSize.setStatus("current")
_CfprApStorageLocalLunConnectionProtocol_Type = CfprApStorageConnectionProtocol
_CfprApStorageLocalLunConnectionProtocol_Object = MibTableColumn
cfprApStorageLocalLunConnectionProtocol = _CfprApStorageLocalLunConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 5),
    _CfprApStorageLocalLunConnectionProtocol_Type()
)
cfprApStorageLocalLunConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunConnectionProtocol.setStatus("current")
_CfprApStorageLocalLunId_Type = Gauge32
_CfprApStorageLocalLunId_Object = MibTableColumn
cfprApStorageLocalLunId = _CfprApStorageLocalLunId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 6),
    _CfprApStorageLocalLunId_Type()
)
cfprApStorageLocalLunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunId.setStatus("current")
_CfprApStorageLocalLunLc_Type = CfprApFsmLifecycle
_CfprApStorageLocalLunLc_Object = MibTableColumn
cfprApStorageLocalLunLc = _CfprApStorageLocalLunLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 7),
    _CfprApStorageLocalLunLc_Type()
)
cfprApStorageLocalLunLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunLc.setStatus("current")
_CfprApStorageLocalLunModel_Type = SnmpAdminString
_CfprApStorageLocalLunModel_Object = MibTableColumn
cfprApStorageLocalLunModel = _CfprApStorageLocalLunModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 8),
    _CfprApStorageLocalLunModel_Type()
)
cfprApStorageLocalLunModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunModel.setStatus("current")
_CfprApStorageLocalLunNumberOfBlocks_Type = Unsigned64
_CfprApStorageLocalLunNumberOfBlocks_Object = MibTableColumn
cfprApStorageLocalLunNumberOfBlocks = _CfprApStorageLocalLunNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 9),
    _CfprApStorageLocalLunNumberOfBlocks_Type()
)
cfprApStorageLocalLunNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunNumberOfBlocks.setStatus("current")
_CfprApStorageLocalLunOperQualifierReason_Type = SnmpAdminString
_CfprApStorageLocalLunOperQualifierReason_Object = MibTableColumn
cfprApStorageLocalLunOperQualifierReason = _CfprApStorageLocalLunOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 10),
    _CfprApStorageLocalLunOperQualifierReason_Type()
)
cfprApStorageLocalLunOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunOperQualifierReason.setStatus("current")
_CfprApStorageLocalLunOperability_Type = CfprApEquipmentOperability
_CfprApStorageLocalLunOperability_Object = MibTableColumn
cfprApStorageLocalLunOperability = _CfprApStorageLocalLunOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 11),
    _CfprApStorageLocalLunOperability_Type()
)
cfprApStorageLocalLunOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunOperability.setStatus("current")
_CfprApStorageLocalLunPresence_Type = CfprApEquipmentPresence
_CfprApStorageLocalLunPresence_Object = MibTableColumn
cfprApStorageLocalLunPresence = _CfprApStorageLocalLunPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 12),
    _CfprApStorageLocalLunPresence_Type()
)
cfprApStorageLocalLunPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunPresence.setStatus("current")
_CfprApStorageLocalLunRevision_Type = SnmpAdminString
_CfprApStorageLocalLunRevision_Object = MibTableColumn
cfprApStorageLocalLunRevision = _CfprApStorageLocalLunRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 13),
    _CfprApStorageLocalLunRevision_Type()
)
cfprApStorageLocalLunRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunRevision.setStatus("current")
_CfprApStorageLocalLunSerial_Type = SnmpAdminString
_CfprApStorageLocalLunSerial_Object = MibTableColumn
cfprApStorageLocalLunSerial = _CfprApStorageLocalLunSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 14),
    _CfprApStorageLocalLunSerial_Type()
)
cfprApStorageLocalLunSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunSerial.setStatus("current")
_CfprApStorageLocalLunSize_Type = Unsigned64
_CfprApStorageLocalLunSize_Object = MibTableColumn
cfprApStorageLocalLunSize = _CfprApStorageLocalLunSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 15),
    _CfprApStorageLocalLunSize_Type()
)
cfprApStorageLocalLunSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunSize.setStatus("current")
_CfprApStorageLocalLunType_Type = CfprApStorageLunType
_CfprApStorageLocalLunType_Object = MibTableColumn
cfprApStorageLocalLunType = _CfprApStorageLocalLunType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 16),
    _CfprApStorageLocalLunType_Type()
)
cfprApStorageLocalLunType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunType.setStatus("current")
_CfprApStorageLocalLunVendor_Type = SnmpAdminString
_CfprApStorageLocalLunVendor_Object = MibTableColumn
cfprApStorageLocalLunVendor = _CfprApStorageLocalLunVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 26, 1, 17),
    _CfprApStorageLocalLunVendor_Type()
)
cfprApStorageLocalLunVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLocalLunVendor.setStatus("current")
_CfprApStorageLunDiskTable_Object = MibTable
cfprApStorageLunDiskTable = _CfprApStorageLunDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 27)
)
if mibBuilder.loadTexts:
    cfprApStorageLunDiskTable.setStatus("current")
_CfprApStorageLunDiskEntry_Object = MibTableRow
cfprApStorageLunDiskEntry = _CfprApStorageLunDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 27, 1)
)
cfprApStorageLunDiskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageLunDiskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageLunDiskEntry.setStatus("current")
_CfprApStorageLunDiskInstanceId_Type = CfprApManagedObjectId
_CfprApStorageLunDiskInstanceId_Object = MibTableColumn
cfprApStorageLunDiskInstanceId = _CfprApStorageLunDiskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 27, 1, 1),
    _CfprApStorageLunDiskInstanceId_Type()
)
cfprApStorageLunDiskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageLunDiskInstanceId.setStatus("current")
_CfprApStorageLunDiskDn_Type = CfprApManagedObjectDn
_CfprApStorageLunDiskDn_Object = MibTableColumn
cfprApStorageLunDiskDn = _CfprApStorageLunDiskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 27, 1, 2),
    _CfprApStorageLunDiskDn_Type()
)
cfprApStorageLunDiskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLunDiskDn.setStatus("current")
_CfprApStorageLunDiskRn_Type = SnmpAdminString
_CfprApStorageLunDiskRn_Object = MibTableColumn
cfprApStorageLunDiskRn = _CfprApStorageLunDiskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 27, 1, 3),
    _CfprApStorageLunDiskRn_Type()
)
cfprApStorageLunDiskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLunDiskRn.setStatus("current")
_CfprApStorageLunDiskId_Type = Gauge32
_CfprApStorageLunDiskId_Object = MibTableColumn
cfprApStorageLunDiskId = _CfprApStorageLunDiskId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 27, 1, 4),
    _CfprApStorageLunDiskId_Type()
)
cfprApStorageLunDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageLunDiskId.setStatus("current")
_CfprApStorageMezzFlashLifeTable_Object = MibTable
cfprApStorageMezzFlashLifeTable = _CfprApStorageMezzFlashLifeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28)
)
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeTable.setStatus("current")
_CfprApStorageMezzFlashLifeEntry_Object = MibTableRow
cfprApStorageMezzFlashLifeEntry = _CfprApStorageMezzFlashLifeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1)
)
cfprApStorageMezzFlashLifeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageMezzFlashLifeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeEntry.setStatus("current")
_CfprApStorageMezzFlashLifeInstanceId_Type = CfprApManagedObjectId
_CfprApStorageMezzFlashLifeInstanceId_Object = MibTableColumn
cfprApStorageMezzFlashLifeInstanceId = _CfprApStorageMezzFlashLifeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 1),
    _CfprApStorageMezzFlashLifeInstanceId_Type()
)
cfprApStorageMezzFlashLifeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeInstanceId.setStatus("current")
_CfprApStorageMezzFlashLifeDn_Type = CfprApManagedObjectDn
_CfprApStorageMezzFlashLifeDn_Object = MibTableColumn
cfprApStorageMezzFlashLifeDn = _CfprApStorageMezzFlashLifeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 2),
    _CfprApStorageMezzFlashLifeDn_Type()
)
cfprApStorageMezzFlashLifeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeDn.setStatus("current")
_CfprApStorageMezzFlashLifeRn_Type = SnmpAdminString
_CfprApStorageMezzFlashLifeRn_Object = MibTableColumn
cfprApStorageMezzFlashLifeRn = _CfprApStorageMezzFlashLifeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 3),
    _CfprApStorageMezzFlashLifeRn_Type()
)
cfprApStorageMezzFlashLifeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeRn.setStatus("current")
_CfprApStorageMezzFlashLifeBlockSize_Type = Gauge32
_CfprApStorageMezzFlashLifeBlockSize_Object = MibTableColumn
cfprApStorageMezzFlashLifeBlockSize = _CfprApStorageMezzFlashLifeBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 4),
    _CfprApStorageMezzFlashLifeBlockSize_Type()
)
cfprApStorageMezzFlashLifeBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeBlockSize.setStatus("current")
_CfprApStorageMezzFlashLifeConnectionProtocol_Type = CfprApStorageConnectionProtocol
_CfprApStorageMezzFlashLifeConnectionProtocol_Object = MibTableColumn
cfprApStorageMezzFlashLifeConnectionProtocol = _CfprApStorageMezzFlashLifeConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 5),
    _CfprApStorageMezzFlashLifeConnectionProtocol_Type()
)
cfprApStorageMezzFlashLifeConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeConnectionProtocol.setStatus("current")
_CfprApStorageMezzFlashLifeFlashPercentage_Type = SnmpAdminString
_CfprApStorageMezzFlashLifeFlashPercentage_Object = MibTableColumn
cfprApStorageMezzFlashLifeFlashPercentage = _CfprApStorageMezzFlashLifeFlashPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 6),
    _CfprApStorageMezzFlashLifeFlashPercentage_Type()
)
cfprApStorageMezzFlashLifeFlashPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeFlashPercentage.setStatus("current")
_CfprApStorageMezzFlashLifeFlashStatus_Type = SnmpAdminString
_CfprApStorageMezzFlashLifeFlashStatus_Object = MibTableColumn
cfprApStorageMezzFlashLifeFlashStatus = _CfprApStorageMezzFlashLifeFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 7),
    _CfprApStorageMezzFlashLifeFlashStatus_Type()
)
cfprApStorageMezzFlashLifeFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeFlashStatus.setStatus("current")
_CfprApStorageMezzFlashLifeId_Type = Gauge32
_CfprApStorageMezzFlashLifeId_Object = MibTableColumn
cfprApStorageMezzFlashLifeId = _CfprApStorageMezzFlashLifeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 8),
    _CfprApStorageMezzFlashLifeId_Type()
)
cfprApStorageMezzFlashLifeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeId.setStatus("current")
_CfprApStorageMezzFlashLifeModel_Type = SnmpAdminString
_CfprApStorageMezzFlashLifeModel_Object = MibTableColumn
cfprApStorageMezzFlashLifeModel = _CfprApStorageMezzFlashLifeModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 9),
    _CfprApStorageMezzFlashLifeModel_Type()
)
cfprApStorageMezzFlashLifeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeModel.setStatus("current")
_CfprApStorageMezzFlashLifeNumberOfBlocks_Type = Unsigned64
_CfprApStorageMezzFlashLifeNumberOfBlocks_Object = MibTableColumn
cfprApStorageMezzFlashLifeNumberOfBlocks = _CfprApStorageMezzFlashLifeNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 10),
    _CfprApStorageMezzFlashLifeNumberOfBlocks_Type()
)
cfprApStorageMezzFlashLifeNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeNumberOfBlocks.setStatus("current")
_CfprApStorageMezzFlashLifeOperQualifierReason_Type = SnmpAdminString
_CfprApStorageMezzFlashLifeOperQualifierReason_Object = MibTableColumn
cfprApStorageMezzFlashLifeOperQualifierReason = _CfprApStorageMezzFlashLifeOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 11),
    _CfprApStorageMezzFlashLifeOperQualifierReason_Type()
)
cfprApStorageMezzFlashLifeOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeOperQualifierReason.setStatus("current")
_CfprApStorageMezzFlashLifeOperability_Type = CfprApEquipmentOperability
_CfprApStorageMezzFlashLifeOperability_Object = MibTableColumn
cfprApStorageMezzFlashLifeOperability = _CfprApStorageMezzFlashLifeOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 12),
    _CfprApStorageMezzFlashLifeOperability_Type()
)
cfprApStorageMezzFlashLifeOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeOperability.setStatus("current")
_CfprApStorageMezzFlashLifePresence_Type = CfprApEquipmentPresence
_CfprApStorageMezzFlashLifePresence_Object = MibTableColumn
cfprApStorageMezzFlashLifePresence = _CfprApStorageMezzFlashLifePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 13),
    _CfprApStorageMezzFlashLifePresence_Type()
)
cfprApStorageMezzFlashLifePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifePresence.setStatus("current")
_CfprApStorageMezzFlashLifeRevision_Type = SnmpAdminString
_CfprApStorageMezzFlashLifeRevision_Object = MibTableColumn
cfprApStorageMezzFlashLifeRevision = _CfprApStorageMezzFlashLifeRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 14),
    _CfprApStorageMezzFlashLifeRevision_Type()
)
cfprApStorageMezzFlashLifeRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeRevision.setStatus("current")
_CfprApStorageMezzFlashLifeSerial_Type = SnmpAdminString
_CfprApStorageMezzFlashLifeSerial_Object = MibTableColumn
cfprApStorageMezzFlashLifeSerial = _CfprApStorageMezzFlashLifeSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 15),
    _CfprApStorageMezzFlashLifeSerial_Type()
)
cfprApStorageMezzFlashLifeSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeSerial.setStatus("current")
_CfprApStorageMezzFlashLifeSize_Type = Unsigned64
_CfprApStorageMezzFlashLifeSize_Object = MibTableColumn
cfprApStorageMezzFlashLifeSize = _CfprApStorageMezzFlashLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 16),
    _CfprApStorageMezzFlashLifeSize_Type()
)
cfprApStorageMezzFlashLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeSize.setStatus("current")
_CfprApStorageMezzFlashLifeVendor_Type = SnmpAdminString
_CfprApStorageMezzFlashLifeVendor_Object = MibTableColumn
cfprApStorageMezzFlashLifeVendor = _CfprApStorageMezzFlashLifeVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 28, 1, 17),
    _CfprApStorageMezzFlashLifeVendor_Type()
)
cfprApStorageMezzFlashLifeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageMezzFlashLifeVendor.setStatus("current")
_CfprApStorageNodeEpTable_Object = MibTable
cfprApStorageNodeEpTable = _CfprApStorageNodeEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 29)
)
if mibBuilder.loadTexts:
    cfprApStorageNodeEpTable.setStatus("current")
_CfprApStorageNodeEpEntry_Object = MibTableRow
cfprApStorageNodeEpEntry = _CfprApStorageNodeEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 29, 1)
)
cfprApStorageNodeEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageNodeEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageNodeEpEntry.setStatus("current")
_CfprApStorageNodeEpInstanceId_Type = CfprApManagedObjectId
_CfprApStorageNodeEpInstanceId_Object = MibTableColumn
cfprApStorageNodeEpInstanceId = _CfprApStorageNodeEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 29, 1, 1),
    _CfprApStorageNodeEpInstanceId_Type()
)
cfprApStorageNodeEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageNodeEpInstanceId.setStatus("current")
_CfprApStorageNodeEpDn_Type = CfprApManagedObjectDn
_CfprApStorageNodeEpDn_Object = MibTableColumn
cfprApStorageNodeEpDn = _CfprApStorageNodeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 29, 1, 2),
    _CfprApStorageNodeEpDn_Type()
)
cfprApStorageNodeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageNodeEpDn.setStatus("current")
_CfprApStorageNodeEpRn_Type = SnmpAdminString
_CfprApStorageNodeEpRn_Object = MibTableColumn
cfprApStorageNodeEpRn = _CfprApStorageNodeEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 29, 1, 3),
    _CfprApStorageNodeEpRn_Type()
)
cfprApStorageNodeEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageNodeEpRn.setStatus("current")
_CfprApStorageNodeEpEpDn_Type = SnmpAdminString
_CfprApStorageNodeEpEpDn_Object = MibTableColumn
cfprApStorageNodeEpEpDn = _CfprApStorageNodeEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 29, 1, 4),
    _CfprApStorageNodeEpEpDn_Type()
)
cfprApStorageNodeEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageNodeEpEpDn.setStatus("current")
_CfprApStorageNodeEpId_Type = Gauge32
_CfprApStorageNodeEpId_Object = MibTableColumn
cfprApStorageNodeEpId = _CfprApStorageNodeEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 29, 1, 5),
    _CfprApStorageNodeEpId_Type()
)
cfprApStorageNodeEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageNodeEpId.setStatus("current")
_CfprApStorageOperationTable_Object = MibTable
cfprApStorageOperationTable = _CfprApStorageOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 30)
)
if mibBuilder.loadTexts:
    cfprApStorageOperationTable.setStatus("current")
_CfprApStorageOperationEntry_Object = MibTableRow
cfprApStorageOperationEntry = _CfprApStorageOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 30, 1)
)
cfprApStorageOperationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageOperationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageOperationEntry.setStatus("current")
_CfprApStorageOperationInstanceId_Type = CfprApManagedObjectId
_CfprApStorageOperationInstanceId_Object = MibTableColumn
cfprApStorageOperationInstanceId = _CfprApStorageOperationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 30, 1, 1),
    _CfprApStorageOperationInstanceId_Type()
)
cfprApStorageOperationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageOperationInstanceId.setStatus("current")
_CfprApStorageOperationDn_Type = CfprApManagedObjectDn
_CfprApStorageOperationDn_Object = MibTableColumn
cfprApStorageOperationDn = _CfprApStorageOperationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 30, 1, 2),
    _CfprApStorageOperationDn_Type()
)
cfprApStorageOperationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageOperationDn.setStatus("current")
_CfprApStorageOperationRn_Type = SnmpAdminString
_CfprApStorageOperationRn_Object = MibTableColumn
cfprApStorageOperationRn = _CfprApStorageOperationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 30, 1, 3),
    _CfprApStorageOperationRn_Type()
)
cfprApStorageOperationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageOperationRn.setStatus("current")
_CfprApStorageOperationEndTime_Type = DateAndTime
_CfprApStorageOperationEndTime_Object = MibTableColumn
cfprApStorageOperationEndTime = _CfprApStorageOperationEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 30, 1, 4),
    _CfprApStorageOperationEndTime_Type()
)
cfprApStorageOperationEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageOperationEndTime.setStatus("current")
_CfprApStorageOperationName_Type = CfprApStorageOperationType
_CfprApStorageOperationName_Object = MibTableColumn
cfprApStorageOperationName = _CfprApStorageOperationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 30, 1, 5),
    _CfprApStorageOperationName_Type()
)
cfprApStorageOperationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageOperationName.setStatus("current")
_CfprApStorageOperationOperState_Type = CfprApStorageOperationState
_CfprApStorageOperationOperState_Object = MibTableColumn
cfprApStorageOperationOperState = _CfprApStorageOperationOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 30, 1, 6),
    _CfprApStorageOperationOperState_Type()
)
cfprApStorageOperationOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageOperationOperState.setStatus("current")
_CfprApStorageOperationProgress_Type = Gauge32
_CfprApStorageOperationProgress_Object = MibTableColumn
cfprApStorageOperationProgress = _CfprApStorageOperationProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 30, 1, 7),
    _CfprApStorageOperationProgress_Type()
)
cfprApStorageOperationProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageOperationProgress.setStatus("current")
_CfprApStorageOperationStartTime_Type = DateAndTime
_CfprApStorageOperationStartTime_Object = MibTableColumn
cfprApStorageOperationStartTime = _CfprApStorageOperationStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 30, 1, 8),
    _CfprApStorageOperationStartTime_Type()
)
cfprApStorageOperationStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageOperationStartTime.setStatus("current")
_CfprApStorageOperationStatusDescr_Type = SnmpAdminString
_CfprApStorageOperationStatusDescr_Object = MibTableColumn
cfprApStorageOperationStatusDescr = _CfprApStorageOperationStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 30, 1, 9),
    _CfprApStorageOperationStatusDescr_Type()
)
cfprApStorageOperationStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageOperationStatusDescr.setStatus("current")
_CfprApStorageQualTable_Object = MibTable
cfprApStorageQualTable = _CfprApStorageQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31)
)
if mibBuilder.loadTexts:
    cfprApStorageQualTable.setStatus("current")
_CfprApStorageQualEntry_Object = MibTableRow
cfprApStorageQualEntry = _CfprApStorageQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31, 1)
)
cfprApStorageQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageQualEntry.setStatus("current")
_CfprApStorageQualInstanceId_Type = CfprApManagedObjectId
_CfprApStorageQualInstanceId_Object = MibTableColumn
cfprApStorageQualInstanceId = _CfprApStorageQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31, 1, 1),
    _CfprApStorageQualInstanceId_Type()
)
cfprApStorageQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageQualInstanceId.setStatus("current")
_CfprApStorageQualDn_Type = CfprApManagedObjectDn
_CfprApStorageQualDn_Object = MibTableColumn
cfprApStorageQualDn = _CfprApStorageQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31, 1, 2),
    _CfprApStorageQualDn_Type()
)
cfprApStorageQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageQualDn.setStatus("current")
_CfprApStorageQualRn_Type = SnmpAdminString
_CfprApStorageQualRn_Object = MibTableColumn
cfprApStorageQualRn = _CfprApStorageQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31, 1, 3),
    _CfprApStorageQualRn_Type()
)
cfprApStorageQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageQualRn.setStatus("current")
_CfprApStorageQualBlockSize_Type = Gauge32
_CfprApStorageQualBlockSize_Object = MibTableColumn
cfprApStorageQualBlockSize = _CfprApStorageQualBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31, 1, 4),
    _CfprApStorageQualBlockSize_Type()
)
cfprApStorageQualBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageQualBlockSize.setStatus("current")
_CfprApStorageQualDiskless_Type = CfprApStorageDisklessAction
_CfprApStorageQualDiskless_Object = MibTableColumn
cfprApStorageQualDiskless = _CfprApStorageQualDiskless_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31, 1, 5),
    _CfprApStorageQualDiskless_Type()
)
cfprApStorageQualDiskless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageQualDiskless.setStatus("current")
_CfprApStorageQualMaxCap_Type = Unsigned64
_CfprApStorageQualMaxCap_Object = MibTableColumn
cfprApStorageQualMaxCap = _CfprApStorageQualMaxCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31, 1, 6),
    _CfprApStorageQualMaxCap_Type()
)
cfprApStorageQualMaxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageQualMaxCap.setStatus("current")
_CfprApStorageQualMinCap_Type = Unsigned64
_CfprApStorageQualMinCap_Object = MibTableColumn
cfprApStorageQualMinCap = _CfprApStorageQualMinCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31, 1, 7),
    _CfprApStorageQualMinCap_Type()
)
cfprApStorageQualMinCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageQualMinCap.setStatus("current")
_CfprApStorageQualNumberOfBlocks_Type = Unsigned64
_CfprApStorageQualNumberOfBlocks_Object = MibTableColumn
cfprApStorageQualNumberOfBlocks = _CfprApStorageQualNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31, 1, 8),
    _CfprApStorageQualNumberOfBlocks_Type()
)
cfprApStorageQualNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageQualNumberOfBlocks.setStatus("current")
_CfprApStorageQualNumberOfFlexFlashCards_Type = Integer32
_CfprApStorageQualNumberOfFlexFlashCards_Object = MibTableColumn
cfprApStorageQualNumberOfFlexFlashCards = _CfprApStorageQualNumberOfFlexFlashCards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31, 1, 9),
    _CfprApStorageQualNumberOfFlexFlashCards_Type()
)
cfprApStorageQualNumberOfFlexFlashCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageQualNumberOfFlexFlashCards.setStatus("current")
_CfprApStorageQualPerDiskCap_Type = Unsigned64
_CfprApStorageQualPerDiskCap_Object = MibTableColumn
cfprApStorageQualPerDiskCap = _CfprApStorageQualPerDiskCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31, 1, 10),
    _CfprApStorageQualPerDiskCap_Type()
)
cfprApStorageQualPerDiskCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageQualPerDiskCap.setStatus("current")
_CfprApStorageQualUnits_Type = Gauge32
_CfprApStorageQualUnits_Object = MibTableColumn
cfprApStorageQualUnits = _CfprApStorageQualUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 31, 1, 11),
    _CfprApStorageQualUnits_Type()
)
cfprApStorageQualUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageQualUnits.setStatus("current")
_CfprApStorageRaidBatteryTable_Object = MibTable
cfprApStorageRaidBatteryTable = _CfprApStorageRaidBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32)
)
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryTable.setStatus("current")
_CfprApStorageRaidBatteryEntry_Object = MibTableRow
cfprApStorageRaidBatteryEntry = _CfprApStorageRaidBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1)
)
cfprApStorageRaidBatteryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageRaidBatteryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryEntry.setStatus("current")
_CfprApStorageRaidBatteryInstanceId_Type = CfprApManagedObjectId
_CfprApStorageRaidBatteryInstanceId_Object = MibTableColumn
cfprApStorageRaidBatteryInstanceId = _CfprApStorageRaidBatteryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 1),
    _CfprApStorageRaidBatteryInstanceId_Type()
)
cfprApStorageRaidBatteryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryInstanceId.setStatus("current")
_CfprApStorageRaidBatteryDn_Type = CfprApManagedObjectDn
_CfprApStorageRaidBatteryDn_Object = MibTableColumn
cfprApStorageRaidBatteryDn = _CfprApStorageRaidBatteryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 2),
    _CfprApStorageRaidBatteryDn_Type()
)
cfprApStorageRaidBatteryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryDn.setStatus("current")
_CfprApStorageRaidBatteryRn_Type = SnmpAdminString
_CfprApStorageRaidBatteryRn_Object = MibTableColumn
cfprApStorageRaidBatteryRn = _CfprApStorageRaidBatteryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 3),
    _CfprApStorageRaidBatteryRn_Type()
)
cfprApStorageRaidBatteryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryRn.setStatus("current")
_CfprApStorageRaidBatteryBatteryType_Type = CfprApStorageBatteryType
_CfprApStorageRaidBatteryBatteryType_Object = MibTableColumn
cfprApStorageRaidBatteryBatteryType = _CfprApStorageRaidBatteryBatteryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 4),
    _CfprApStorageRaidBatteryBatteryType_Type()
)
cfprApStorageRaidBatteryBatteryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryBatteryType.setStatus("current")
_CfprApStorageRaidBatteryBbuStatus_Type = CfprApStorageBbuStatus
_CfprApStorageRaidBatteryBbuStatus_Object = MibTableColumn
cfprApStorageRaidBatteryBbuStatus = _CfprApStorageRaidBatteryBbuStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 5),
    _CfprApStorageRaidBatteryBbuStatus_Type()
)
cfprApStorageRaidBatteryBbuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryBbuStatus.setStatus("current")
_CfprApStorageRaidBatteryBlockSize_Type = Gauge32
_CfprApStorageRaidBatteryBlockSize_Object = MibTableColumn
cfprApStorageRaidBatteryBlockSize = _CfprApStorageRaidBatteryBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 6),
    _CfprApStorageRaidBatteryBlockSize_Type()
)
cfprApStorageRaidBatteryBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryBlockSize.setStatus("current")
_CfprApStorageRaidBatteryCapacityPercentage_Type = Gauge32
_CfprApStorageRaidBatteryCapacityPercentage_Object = MibTableColumn
cfprApStorageRaidBatteryCapacityPercentage = _CfprApStorageRaidBatteryCapacityPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 7),
    _CfprApStorageRaidBatteryCapacityPercentage_Type()
)
cfprApStorageRaidBatteryCapacityPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryCapacityPercentage.setStatus("current")
_CfprApStorageRaidBatteryConnectionProtocol_Type = CfprApStorageConnectionProtocol
_CfprApStorageRaidBatteryConnectionProtocol_Object = MibTableColumn
cfprApStorageRaidBatteryConnectionProtocol = _CfprApStorageRaidBatteryConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 8),
    _CfprApStorageRaidBatteryConnectionProtocol_Type()
)
cfprApStorageRaidBatteryConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryConnectionProtocol.setStatus("current")
_CfprApStorageRaidBatteryId_Type = Gauge32
_CfprApStorageRaidBatteryId_Object = MibTableColumn
cfprApStorageRaidBatteryId = _CfprApStorageRaidBatteryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 9),
    _CfprApStorageRaidBatteryId_Type()
)
cfprApStorageRaidBatteryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryId.setStatus("current")
_CfprApStorageRaidBatteryLc_Type = CfprApFsmLifecycle
_CfprApStorageRaidBatteryLc_Object = MibTableColumn
cfprApStorageRaidBatteryLc = _CfprApStorageRaidBatteryLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 10),
    _CfprApStorageRaidBatteryLc_Type()
)
cfprApStorageRaidBatteryLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryLc.setStatus("current")
_CfprApStorageRaidBatteryLearnCycleRequested_Type = CfprApStorageLearnCycleRequested
_CfprApStorageRaidBatteryLearnCycleRequested_Object = MibTableColumn
cfprApStorageRaidBatteryLearnCycleRequested = _CfprApStorageRaidBatteryLearnCycleRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 11),
    _CfprApStorageRaidBatteryLearnCycleRequested_Type()
)
cfprApStorageRaidBatteryLearnCycleRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryLearnCycleRequested.setStatus("current")
_CfprApStorageRaidBatteryLearnMode_Type = CfprApStorageLearnMode
_CfprApStorageRaidBatteryLearnMode_Object = MibTableColumn
cfprApStorageRaidBatteryLearnMode = _CfprApStorageRaidBatteryLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 12),
    _CfprApStorageRaidBatteryLearnMode_Type()
)
cfprApStorageRaidBatteryLearnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryLearnMode.setStatus("current")
_CfprApStorageRaidBatteryModel_Type = SnmpAdminString
_CfprApStorageRaidBatteryModel_Object = MibTableColumn
cfprApStorageRaidBatteryModel = _CfprApStorageRaidBatteryModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 13),
    _CfprApStorageRaidBatteryModel_Type()
)
cfprApStorageRaidBatteryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryModel.setStatus("current")
_CfprApStorageRaidBatteryNextLearnCycleTs_Type = DateAndTime
_CfprApStorageRaidBatteryNextLearnCycleTs_Object = MibTableColumn
cfprApStorageRaidBatteryNextLearnCycleTs = _CfprApStorageRaidBatteryNextLearnCycleTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 14),
    _CfprApStorageRaidBatteryNextLearnCycleTs_Type()
)
cfprApStorageRaidBatteryNextLearnCycleTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryNextLearnCycleTs.setStatus("current")
_CfprApStorageRaidBatteryNumberOfBlocks_Type = Unsigned64
_CfprApStorageRaidBatteryNumberOfBlocks_Object = MibTableColumn
cfprApStorageRaidBatteryNumberOfBlocks = _CfprApStorageRaidBatteryNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 15),
    _CfprApStorageRaidBatteryNumberOfBlocks_Type()
)
cfprApStorageRaidBatteryNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryNumberOfBlocks.setStatus("current")
_CfprApStorageRaidBatteryOperQualifierReason_Type = SnmpAdminString
_CfprApStorageRaidBatteryOperQualifierReason_Object = MibTableColumn
cfprApStorageRaidBatteryOperQualifierReason = _CfprApStorageRaidBatteryOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 16),
    _CfprApStorageRaidBatteryOperQualifierReason_Type()
)
cfprApStorageRaidBatteryOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryOperQualifierReason.setStatus("current")
_CfprApStorageRaidBatteryOperability_Type = CfprApEquipmentOperability
_CfprApStorageRaidBatteryOperability_Object = MibTableColumn
cfprApStorageRaidBatteryOperability = _CfprApStorageRaidBatteryOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 17),
    _CfprApStorageRaidBatteryOperability_Type()
)
cfprApStorageRaidBatteryOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryOperability.setStatus("current")
_CfprApStorageRaidBatteryOperabilityQualifier_Type = CfprApStorageRaidBatteryOperabilityQualifier
_CfprApStorageRaidBatteryOperabilityQualifier_Object = MibTableColumn
cfprApStorageRaidBatteryOperabilityQualifier = _CfprApStorageRaidBatteryOperabilityQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 18),
    _CfprApStorageRaidBatteryOperabilityQualifier_Type()
)
cfprApStorageRaidBatteryOperabilityQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryOperabilityQualifier.setStatus("current")
_CfprApStorageRaidBatteryOperabilityQualifierReason_Type = SnmpAdminString
_CfprApStorageRaidBatteryOperabilityQualifierReason_Object = MibTableColumn
cfprApStorageRaidBatteryOperabilityQualifierReason = _CfprApStorageRaidBatteryOperabilityQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 19),
    _CfprApStorageRaidBatteryOperabilityQualifierReason_Type()
)
cfprApStorageRaidBatteryOperabilityQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryOperabilityQualifierReason.setStatus("current")
_CfprApStorageRaidBatteryPresence_Type = CfprApEquipmentPresence
_CfprApStorageRaidBatteryPresence_Object = MibTableColumn
cfprApStorageRaidBatteryPresence = _CfprApStorageRaidBatteryPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 20),
    _CfprApStorageRaidBatteryPresence_Type()
)
cfprApStorageRaidBatteryPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryPresence.setStatus("current")
_CfprApStorageRaidBatteryRevision_Type = SnmpAdminString
_CfprApStorageRaidBatteryRevision_Object = MibTableColumn
cfprApStorageRaidBatteryRevision = _CfprApStorageRaidBatteryRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 21),
    _CfprApStorageRaidBatteryRevision_Type()
)
cfprApStorageRaidBatteryRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryRevision.setStatus("current")
_CfprApStorageRaidBatterySerial_Type = SnmpAdminString
_CfprApStorageRaidBatterySerial_Object = MibTableColumn
cfprApStorageRaidBatterySerial = _CfprApStorageRaidBatterySerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 22),
    _CfprApStorageRaidBatterySerial_Type()
)
cfprApStorageRaidBatterySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatterySerial.setStatus("current")
_CfprApStorageRaidBatterySize_Type = Unsigned64
_CfprApStorageRaidBatterySize_Object = MibTableColumn
cfprApStorageRaidBatterySize = _CfprApStorageRaidBatterySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 23),
    _CfprApStorageRaidBatterySize_Type()
)
cfprApStorageRaidBatterySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatterySize.setStatus("current")
_CfprApStorageRaidBatteryTemperature_Type = Integer32
_CfprApStorageRaidBatteryTemperature_Object = MibTableColumn
cfprApStorageRaidBatteryTemperature = _CfprApStorageRaidBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 24),
    _CfprApStorageRaidBatteryTemperature_Type()
)
cfprApStorageRaidBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryTemperature.setStatus("current")
_CfprApStorageRaidBatteryVendor_Type = SnmpAdminString
_CfprApStorageRaidBatteryVendor_Object = MibTableColumn
cfprApStorageRaidBatteryVendor = _CfprApStorageRaidBatteryVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 32, 1, 25),
    _CfprApStorageRaidBatteryVendor_Type()
)
cfprApStorageRaidBatteryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageRaidBatteryVendor.setStatus("current")
_CfprApStorageSystemTable_Object = MibTable
cfprApStorageSystemTable = _CfprApStorageSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33)
)
if mibBuilder.loadTexts:
    cfprApStorageSystemTable.setStatus("current")
_CfprApStorageSystemEntry_Object = MibTableRow
cfprApStorageSystemEntry = _CfprApStorageSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1)
)
cfprApStorageSystemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageSystemEntry.setStatus("current")
_CfprApStorageSystemInstanceId_Type = CfprApManagedObjectId
_CfprApStorageSystemInstanceId_Object = MibTableColumn
cfprApStorageSystemInstanceId = _CfprApStorageSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 1),
    _CfprApStorageSystemInstanceId_Type()
)
cfprApStorageSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageSystemInstanceId.setStatus("current")
_CfprApStorageSystemDn_Type = CfprApManagedObjectDn
_CfprApStorageSystemDn_Object = MibTableColumn
cfprApStorageSystemDn = _CfprApStorageSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 2),
    _CfprApStorageSystemDn_Type()
)
cfprApStorageSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemDn.setStatus("current")
_CfprApStorageSystemRn_Type = SnmpAdminString
_CfprApStorageSystemRn_Object = MibTableColumn
cfprApStorageSystemRn = _CfprApStorageSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 3),
    _CfprApStorageSystemRn_Type()
)
cfprApStorageSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemRn.setStatus("current")
_CfprApStorageSystemFsmDescr_Type = SnmpAdminString
_CfprApStorageSystemFsmDescr_Object = MibTableColumn
cfprApStorageSystemFsmDescr = _CfprApStorageSystemFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 4),
    _CfprApStorageSystemFsmDescr_Type()
)
cfprApStorageSystemFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmDescr.setStatus("current")
_CfprApStorageSystemFsmPrev_Type = SnmpAdminString
_CfprApStorageSystemFsmPrev_Object = MibTableColumn
cfprApStorageSystemFsmPrev = _CfprApStorageSystemFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 5),
    _CfprApStorageSystemFsmPrev_Type()
)
cfprApStorageSystemFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmPrev.setStatus("current")
_CfprApStorageSystemFsmProgr_Type = Gauge32
_CfprApStorageSystemFsmProgr_Object = MibTableColumn
cfprApStorageSystemFsmProgr = _CfprApStorageSystemFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 6),
    _CfprApStorageSystemFsmProgr_Type()
)
cfprApStorageSystemFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmProgr.setStatus("current")
_CfprApStorageSystemFsmRmtInvErrCode_Type = Gauge32
_CfprApStorageSystemFsmRmtInvErrCode_Object = MibTableColumn
cfprApStorageSystemFsmRmtInvErrCode = _CfprApStorageSystemFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 7),
    _CfprApStorageSystemFsmRmtInvErrCode_Type()
)
cfprApStorageSystemFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmRmtInvErrCode.setStatus("current")
_CfprApStorageSystemFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApStorageSystemFsmRmtInvErrDescr_Object = MibTableColumn
cfprApStorageSystemFsmRmtInvErrDescr = _CfprApStorageSystemFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 8),
    _CfprApStorageSystemFsmRmtInvErrDescr_Type()
)
cfprApStorageSystemFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmRmtInvErrDescr.setStatus("current")
_CfprApStorageSystemFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApStorageSystemFsmRmtInvRslt_Object = MibTableColumn
cfprApStorageSystemFsmRmtInvRslt = _CfprApStorageSystemFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 9),
    _CfprApStorageSystemFsmRmtInvRslt_Type()
)
cfprApStorageSystemFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmRmtInvRslt.setStatus("current")
_CfprApStorageSystemFsmStageDescr_Type = SnmpAdminString
_CfprApStorageSystemFsmStageDescr_Object = MibTableColumn
cfprApStorageSystemFsmStageDescr = _CfprApStorageSystemFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 10),
    _CfprApStorageSystemFsmStageDescr_Type()
)
cfprApStorageSystemFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStageDescr.setStatus("current")
_CfprApStorageSystemFsmStamp_Type = DateAndTime
_CfprApStorageSystemFsmStamp_Object = MibTableColumn
cfprApStorageSystemFsmStamp = _CfprApStorageSystemFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 11),
    _CfprApStorageSystemFsmStamp_Type()
)
cfprApStorageSystemFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStamp.setStatus("current")
_CfprApStorageSystemFsmStatus_Type = SnmpAdminString
_CfprApStorageSystemFsmStatus_Object = MibTableColumn
cfprApStorageSystemFsmStatus = _CfprApStorageSystemFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 12),
    _CfprApStorageSystemFsmStatus_Type()
)
cfprApStorageSystemFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStatus.setStatus("current")
_CfprApStorageSystemFsmTry_Type = Gauge32
_CfprApStorageSystemFsmTry_Object = MibTableColumn
cfprApStorageSystemFsmTry = _CfprApStorageSystemFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 13),
    _CfprApStorageSystemFsmTry_Type()
)
cfprApStorageSystemFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmTry.setStatus("current")
_CfprApStorageSystemId_Type = SnmpAdminString
_CfprApStorageSystemId_Object = MibTableColumn
cfprApStorageSystemId = _CfprApStorageSystemId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 14),
    _CfprApStorageSystemId_Type()
)
cfprApStorageSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemId.setStatus("current")
_CfprApStorageSystemName_Type = SnmpAdminString
_CfprApStorageSystemName_Object = MibTableColumn
cfprApStorageSystemName = _CfprApStorageSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 33, 1, 15),
    _CfprApStorageSystemName_Type()
)
cfprApStorageSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemName.setStatus("current")
_CfprApStorageSystemFsmTable_Object = MibTable
cfprApStorageSystemFsmTable = _CfprApStorageSystemFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34)
)
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmTable.setStatus("current")
_CfprApStorageSystemFsmEntry_Object = MibTableRow
cfprApStorageSystemFsmEntry = _CfprApStorageSystemFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34, 1)
)
cfprApStorageSystemFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageSystemFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmEntry.setStatus("current")
_CfprApStorageSystemFsmInstanceId_Type = CfprApManagedObjectId
_CfprApStorageSystemFsmInstanceId_Object = MibTableColumn
cfprApStorageSystemFsmInstanceId = _CfprApStorageSystemFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34, 1, 1),
    _CfprApStorageSystemFsmInstanceId_Type()
)
cfprApStorageSystemFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmInstanceId.setStatus("current")
_CfprApStorageSystemFsmDn_Type = CfprApManagedObjectDn
_CfprApStorageSystemFsmDn_Object = MibTableColumn
cfprApStorageSystemFsmDn = _CfprApStorageSystemFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34, 1, 2),
    _CfprApStorageSystemFsmDn_Type()
)
cfprApStorageSystemFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmDn.setStatus("current")
_CfprApStorageSystemFsmRn_Type = SnmpAdminString
_CfprApStorageSystemFsmRn_Object = MibTableColumn
cfprApStorageSystemFsmRn = _CfprApStorageSystemFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34, 1, 3),
    _CfprApStorageSystemFsmRn_Type()
)
cfprApStorageSystemFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmRn.setStatus("current")
_CfprApStorageSystemFsmCompletionTime_Type = DateAndTime
_CfprApStorageSystemFsmCompletionTime_Object = MibTableColumn
cfprApStorageSystemFsmCompletionTime = _CfprApStorageSystemFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34, 1, 4),
    _CfprApStorageSystemFsmCompletionTime_Type()
)
cfprApStorageSystemFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmCompletionTime.setStatus("current")
_CfprApStorageSystemFsmCurrentFsm_Type = CfprApStorageSystemFsmCurrentFsm
_CfprApStorageSystemFsmCurrentFsm_Object = MibTableColumn
cfprApStorageSystemFsmCurrentFsm = _CfprApStorageSystemFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34, 1, 5),
    _CfprApStorageSystemFsmCurrentFsm_Type()
)
cfprApStorageSystemFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmCurrentFsm.setStatus("current")
_CfprApStorageSystemFsmDescrData_Type = SnmpAdminString
_CfprApStorageSystemFsmDescrData_Object = MibTableColumn
cfprApStorageSystemFsmDescrData = _CfprApStorageSystemFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34, 1, 6),
    _CfprApStorageSystemFsmDescrData_Type()
)
cfprApStorageSystemFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmDescrData.setStatus("current")
_CfprApStorageSystemFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApStorageSystemFsmFsmStatus_Object = MibTableColumn
cfprApStorageSystemFsmFsmStatus = _CfprApStorageSystemFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34, 1, 7),
    _CfprApStorageSystemFsmFsmStatus_Type()
)
cfprApStorageSystemFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmFsmStatus.setStatus("current")
_CfprApStorageSystemFsmProgress_Type = Gauge32
_CfprApStorageSystemFsmProgress_Object = MibTableColumn
cfprApStorageSystemFsmProgress = _CfprApStorageSystemFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34, 1, 8),
    _CfprApStorageSystemFsmProgress_Type()
)
cfprApStorageSystemFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmProgress.setStatus("current")
_CfprApStorageSystemFsmRmtErrCode_Type = Gauge32
_CfprApStorageSystemFsmRmtErrCode_Object = MibTableColumn
cfprApStorageSystemFsmRmtErrCode = _CfprApStorageSystemFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34, 1, 9),
    _CfprApStorageSystemFsmRmtErrCode_Type()
)
cfprApStorageSystemFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmRmtErrCode.setStatus("current")
_CfprApStorageSystemFsmRmtErrDescr_Type = SnmpAdminString
_CfprApStorageSystemFsmRmtErrDescr_Object = MibTableColumn
cfprApStorageSystemFsmRmtErrDescr = _CfprApStorageSystemFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34, 1, 10),
    _CfprApStorageSystemFsmRmtErrDescr_Type()
)
cfprApStorageSystemFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmRmtErrDescr.setStatus("current")
_CfprApStorageSystemFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApStorageSystemFsmRmtRslt_Object = MibTableColumn
cfprApStorageSystemFsmRmtRslt = _CfprApStorageSystemFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 34, 1, 11),
    _CfprApStorageSystemFsmRmtRslt_Type()
)
cfprApStorageSystemFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmRmtRslt.setStatus("current")
_CfprApStorageSystemFsmStageTable_Object = MibTable
cfprApStorageSystemFsmStageTable = _CfprApStorageSystemFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 35)
)
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStageTable.setStatus("current")
_CfprApStorageSystemFsmStageEntry_Object = MibTableRow
cfprApStorageSystemFsmStageEntry = _CfprApStorageSystemFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 35, 1)
)
cfprApStorageSystemFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageSystemFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStageEntry.setStatus("current")
_CfprApStorageSystemFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApStorageSystemFsmStageInstanceId_Object = MibTableColumn
cfprApStorageSystemFsmStageInstanceId = _CfprApStorageSystemFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 35, 1, 1),
    _CfprApStorageSystemFsmStageInstanceId_Type()
)
cfprApStorageSystemFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStageInstanceId.setStatus("current")
_CfprApStorageSystemFsmStageDn_Type = CfprApManagedObjectDn
_CfprApStorageSystemFsmStageDn_Object = MibTableColumn
cfprApStorageSystemFsmStageDn = _CfprApStorageSystemFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 35, 1, 2),
    _CfprApStorageSystemFsmStageDn_Type()
)
cfprApStorageSystemFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStageDn.setStatus("current")
_CfprApStorageSystemFsmStageRn_Type = SnmpAdminString
_CfprApStorageSystemFsmStageRn_Object = MibTableColumn
cfprApStorageSystemFsmStageRn = _CfprApStorageSystemFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 35, 1, 3),
    _CfprApStorageSystemFsmStageRn_Type()
)
cfprApStorageSystemFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStageRn.setStatus("current")
_CfprApStorageSystemFsmStageDescrData_Type = SnmpAdminString
_CfprApStorageSystemFsmStageDescrData_Object = MibTableColumn
cfprApStorageSystemFsmStageDescrData = _CfprApStorageSystemFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 35, 1, 4),
    _CfprApStorageSystemFsmStageDescrData_Type()
)
cfprApStorageSystemFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStageDescrData.setStatus("current")
_CfprApStorageSystemFsmStageLastUpdateTime_Type = DateAndTime
_CfprApStorageSystemFsmStageLastUpdateTime_Object = MibTableColumn
cfprApStorageSystemFsmStageLastUpdateTime = _CfprApStorageSystemFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 35, 1, 5),
    _CfprApStorageSystemFsmStageLastUpdateTime_Type()
)
cfprApStorageSystemFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStageLastUpdateTime.setStatus("current")
_CfprApStorageSystemFsmStageName_Type = CfprApStorageSystemFsmStageName
_CfprApStorageSystemFsmStageName_Object = MibTableColumn
cfprApStorageSystemFsmStageName = _CfprApStorageSystemFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 35, 1, 6),
    _CfprApStorageSystemFsmStageName_Type()
)
cfprApStorageSystemFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStageName.setStatus("current")
_CfprApStorageSystemFsmStageOrder_Type = Gauge32
_CfprApStorageSystemFsmStageOrder_Object = MibTableColumn
cfprApStorageSystemFsmStageOrder = _CfprApStorageSystemFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 35, 1, 7),
    _CfprApStorageSystemFsmStageOrder_Type()
)
cfprApStorageSystemFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStageOrder.setStatus("current")
_CfprApStorageSystemFsmStageRetry_Type = Gauge32
_CfprApStorageSystemFsmStageRetry_Object = MibTableColumn
cfprApStorageSystemFsmStageRetry = _CfprApStorageSystemFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 35, 1, 8),
    _CfprApStorageSystemFsmStageRetry_Type()
)
cfprApStorageSystemFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStageRetry.setStatus("current")
_CfprApStorageSystemFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApStorageSystemFsmStageStageStatus_Object = MibTableColumn
cfprApStorageSystemFsmStageStageStatus = _CfprApStorageSystemFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 35, 1, 9),
    _CfprApStorageSystemFsmStageStageStatus_Type()
)
cfprApStorageSystemFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmStageStageStatus.setStatus("current")
_CfprApStorageSystemFsmTaskTable_Object = MibTable
cfprApStorageSystemFsmTaskTable = _CfprApStorageSystemFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 36)
)
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmTaskTable.setStatus("current")
_CfprApStorageSystemFsmTaskEntry_Object = MibTableRow
cfprApStorageSystemFsmTaskEntry = _CfprApStorageSystemFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 36, 1)
)
cfprApStorageSystemFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageSystemFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmTaskEntry.setStatus("current")
_CfprApStorageSystemFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApStorageSystemFsmTaskInstanceId_Object = MibTableColumn
cfprApStorageSystemFsmTaskInstanceId = _CfprApStorageSystemFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 36, 1, 1),
    _CfprApStorageSystemFsmTaskInstanceId_Type()
)
cfprApStorageSystemFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmTaskInstanceId.setStatus("current")
_CfprApStorageSystemFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApStorageSystemFsmTaskDn_Object = MibTableColumn
cfprApStorageSystemFsmTaskDn = _CfprApStorageSystemFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 36, 1, 2),
    _CfprApStorageSystemFsmTaskDn_Type()
)
cfprApStorageSystemFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmTaskDn.setStatus("current")
_CfprApStorageSystemFsmTaskRn_Type = SnmpAdminString
_CfprApStorageSystemFsmTaskRn_Object = MibTableColumn
cfprApStorageSystemFsmTaskRn = _CfprApStorageSystemFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 36, 1, 3),
    _CfprApStorageSystemFsmTaskRn_Type()
)
cfprApStorageSystemFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmTaskRn.setStatus("current")
_CfprApStorageSystemFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApStorageSystemFsmTaskCompletion_Object = MibTableColumn
cfprApStorageSystemFsmTaskCompletion = _CfprApStorageSystemFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 36, 1, 4),
    _CfprApStorageSystemFsmTaskCompletion_Type()
)
cfprApStorageSystemFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmTaskCompletion.setStatus("current")
_CfprApStorageSystemFsmTaskFlags_Type = CfprApFsmFlags
_CfprApStorageSystemFsmTaskFlags_Object = MibTableColumn
cfprApStorageSystemFsmTaskFlags = _CfprApStorageSystemFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 36, 1, 5),
    _CfprApStorageSystemFsmTaskFlags_Type()
)
cfprApStorageSystemFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmTaskFlags.setStatus("current")
_CfprApStorageSystemFsmTaskItem_Type = CfprApStorageSystemFsmTaskItem
_CfprApStorageSystemFsmTaskItem_Object = MibTableColumn
cfprApStorageSystemFsmTaskItem = _CfprApStorageSystemFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 36, 1, 6),
    _CfprApStorageSystemFsmTaskItem_Type()
)
cfprApStorageSystemFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmTaskItem.setStatus("current")
_CfprApStorageSystemFsmTaskSeqId_Type = Gauge32
_CfprApStorageSystemFsmTaskSeqId_Object = MibTableColumn
cfprApStorageSystemFsmTaskSeqId = _CfprApStorageSystemFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 36, 1, 7),
    _CfprApStorageSystemFsmTaskSeqId_Type()
)
cfprApStorageSystemFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageSystemFsmTaskSeqId.setStatus("current")
_CfprApStorageTransportableFlashModuleTable_Object = MibTable
cfprApStorageTransportableFlashModuleTable = _CfprApStorageTransportableFlashModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37)
)
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleTable.setStatus("current")
_CfprApStorageTransportableFlashModuleEntry_Object = MibTableRow
cfprApStorageTransportableFlashModuleEntry = _CfprApStorageTransportableFlashModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1)
)
cfprApStorageTransportableFlashModuleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageTransportableFlashModuleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleEntry.setStatus("current")
_CfprApStorageTransportableFlashModuleInstanceId_Type = CfprApManagedObjectId
_CfprApStorageTransportableFlashModuleInstanceId_Object = MibTableColumn
cfprApStorageTransportableFlashModuleInstanceId = _CfprApStorageTransportableFlashModuleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 1),
    _CfprApStorageTransportableFlashModuleInstanceId_Type()
)
cfprApStorageTransportableFlashModuleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleInstanceId.setStatus("current")
_CfprApStorageTransportableFlashModuleDn_Type = CfprApManagedObjectDn
_CfprApStorageTransportableFlashModuleDn_Object = MibTableColumn
cfprApStorageTransportableFlashModuleDn = _CfprApStorageTransportableFlashModuleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 2),
    _CfprApStorageTransportableFlashModuleDn_Type()
)
cfprApStorageTransportableFlashModuleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleDn.setStatus("current")
_CfprApStorageTransportableFlashModuleRn_Type = SnmpAdminString
_CfprApStorageTransportableFlashModuleRn_Object = MibTableColumn
cfprApStorageTransportableFlashModuleRn = _CfprApStorageTransportableFlashModuleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 3),
    _CfprApStorageTransportableFlashModuleRn_Type()
)
cfprApStorageTransportableFlashModuleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleRn.setStatus("current")
_CfprApStorageTransportableFlashModuleBlockSize_Type = Gauge32
_CfprApStorageTransportableFlashModuleBlockSize_Object = MibTableColumn
cfprApStorageTransportableFlashModuleBlockSize = _CfprApStorageTransportableFlashModuleBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 4),
    _CfprApStorageTransportableFlashModuleBlockSize_Type()
)
cfprApStorageTransportableFlashModuleBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleBlockSize.setStatus("current")
_CfprApStorageTransportableFlashModuleConnectionProtocol_Type = CfprApStorageConnectionProtocol
_CfprApStorageTransportableFlashModuleConnectionProtocol_Object = MibTableColumn
cfprApStorageTransportableFlashModuleConnectionProtocol = _CfprApStorageTransportableFlashModuleConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 5),
    _CfprApStorageTransportableFlashModuleConnectionProtocol_Type()
)
cfprApStorageTransportableFlashModuleConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleConnectionProtocol.setStatus("current")
_CfprApStorageTransportableFlashModuleId_Type = Gauge32
_CfprApStorageTransportableFlashModuleId_Object = MibTableColumn
cfprApStorageTransportableFlashModuleId = _CfprApStorageTransportableFlashModuleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 6),
    _CfprApStorageTransportableFlashModuleId_Type()
)
cfprApStorageTransportableFlashModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleId.setStatus("current")
_CfprApStorageTransportableFlashModuleModel_Type = SnmpAdminString
_CfprApStorageTransportableFlashModuleModel_Object = MibTableColumn
cfprApStorageTransportableFlashModuleModel = _CfprApStorageTransportableFlashModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 7),
    _CfprApStorageTransportableFlashModuleModel_Type()
)
cfprApStorageTransportableFlashModuleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleModel.setStatus("current")
_CfprApStorageTransportableFlashModuleNumberOfBlocks_Type = Unsigned64
_CfprApStorageTransportableFlashModuleNumberOfBlocks_Object = MibTableColumn
cfprApStorageTransportableFlashModuleNumberOfBlocks = _CfprApStorageTransportableFlashModuleNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 8),
    _CfprApStorageTransportableFlashModuleNumberOfBlocks_Type()
)
cfprApStorageTransportableFlashModuleNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleNumberOfBlocks.setStatus("current")
_CfprApStorageTransportableFlashModuleOperQualifierReason_Type = SnmpAdminString
_CfprApStorageTransportableFlashModuleOperQualifierReason_Object = MibTableColumn
cfprApStorageTransportableFlashModuleOperQualifierReason = _CfprApStorageTransportableFlashModuleOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 9),
    _CfprApStorageTransportableFlashModuleOperQualifierReason_Type()
)
cfprApStorageTransportableFlashModuleOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleOperQualifierReason.setStatus("current")
_CfprApStorageTransportableFlashModuleOperability_Type = CfprApEquipmentOperability
_CfprApStorageTransportableFlashModuleOperability_Object = MibTableColumn
cfprApStorageTransportableFlashModuleOperability = _CfprApStorageTransportableFlashModuleOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 10),
    _CfprApStorageTransportableFlashModuleOperability_Type()
)
cfprApStorageTransportableFlashModuleOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleOperability.setStatus("current")
_CfprApStorageTransportableFlashModulePresence_Type = CfprApEquipmentPresence
_CfprApStorageTransportableFlashModulePresence_Object = MibTableColumn
cfprApStorageTransportableFlashModulePresence = _CfprApStorageTransportableFlashModulePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 11),
    _CfprApStorageTransportableFlashModulePresence_Type()
)
cfprApStorageTransportableFlashModulePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModulePresence.setStatus("current")
_CfprApStorageTransportableFlashModuleRevision_Type = SnmpAdminString
_CfprApStorageTransportableFlashModuleRevision_Object = MibTableColumn
cfprApStorageTransportableFlashModuleRevision = _CfprApStorageTransportableFlashModuleRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 12),
    _CfprApStorageTransportableFlashModuleRevision_Type()
)
cfprApStorageTransportableFlashModuleRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleRevision.setStatus("current")
_CfprApStorageTransportableFlashModuleSerial_Type = SnmpAdminString
_CfprApStorageTransportableFlashModuleSerial_Object = MibTableColumn
cfprApStorageTransportableFlashModuleSerial = _CfprApStorageTransportableFlashModuleSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 13),
    _CfprApStorageTransportableFlashModuleSerial_Type()
)
cfprApStorageTransportableFlashModuleSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleSerial.setStatus("current")
_CfprApStorageTransportableFlashModuleSize_Type = Unsigned64
_CfprApStorageTransportableFlashModuleSize_Object = MibTableColumn
cfprApStorageTransportableFlashModuleSize = _CfprApStorageTransportableFlashModuleSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 14),
    _CfprApStorageTransportableFlashModuleSize_Type()
)
cfprApStorageTransportableFlashModuleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleSize.setStatus("current")
_CfprApStorageTransportableFlashModuleVendor_Type = SnmpAdminString
_CfprApStorageTransportableFlashModuleVendor_Object = MibTableColumn
cfprApStorageTransportableFlashModuleVendor = _CfprApStorageTransportableFlashModuleVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 37, 1, 15),
    _CfprApStorageTransportableFlashModuleVendor_Type()
)
cfprApStorageTransportableFlashModuleVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageTransportableFlashModuleVendor.setStatus("current")
_CfprApStorageVirtualDriveTable_Object = MibTable
cfprApStorageVirtualDriveTable = _CfprApStorageVirtualDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38)
)
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveTable.setStatus("current")
_CfprApStorageVirtualDriveEntry_Object = MibTableRow
cfprApStorageVirtualDriveEntry = _CfprApStorageVirtualDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1)
)
cfprApStorageVirtualDriveEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageVirtualDriveInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveEntry.setStatus("current")
_CfprApStorageVirtualDriveInstanceId_Type = CfprApManagedObjectId
_CfprApStorageVirtualDriveInstanceId_Object = MibTableColumn
cfprApStorageVirtualDriveInstanceId = _CfprApStorageVirtualDriveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 1),
    _CfprApStorageVirtualDriveInstanceId_Type()
)
cfprApStorageVirtualDriveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveInstanceId.setStatus("current")
_CfprApStorageVirtualDriveDn_Type = CfprApManagedObjectDn
_CfprApStorageVirtualDriveDn_Object = MibTableColumn
cfprApStorageVirtualDriveDn = _CfprApStorageVirtualDriveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 2),
    _CfprApStorageVirtualDriveDn_Type()
)
cfprApStorageVirtualDriveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveDn.setStatus("current")
_CfprApStorageVirtualDriveRn_Type = SnmpAdminString
_CfprApStorageVirtualDriveRn_Object = MibTableColumn
cfprApStorageVirtualDriveRn = _CfprApStorageVirtualDriveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 3),
    _CfprApStorageVirtualDriveRn_Type()
)
cfprApStorageVirtualDriveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveRn.setStatus("current")
_CfprApStorageVirtualDriveAccessPolicy_Type = CfprApStorageAccessType
_CfprApStorageVirtualDriveAccessPolicy_Object = MibTableColumn
cfprApStorageVirtualDriveAccessPolicy = _CfprApStorageVirtualDriveAccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 4),
    _CfprApStorageVirtualDriveAccessPolicy_Type()
)
cfprApStorageVirtualDriveAccessPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveAccessPolicy.setStatus("current")
_CfprApStorageVirtualDriveActualWriteCachePolicy_Type = CfprApStorageActualWriteType
_CfprApStorageVirtualDriveActualWriteCachePolicy_Object = MibTableColumn
cfprApStorageVirtualDriveActualWriteCachePolicy = _CfprApStorageVirtualDriveActualWriteCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 5),
    _CfprApStorageVirtualDriveActualWriteCachePolicy_Type()
)
cfprApStorageVirtualDriveActualWriteCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveActualWriteCachePolicy.setStatus("current")
_CfprApStorageVirtualDriveBlockSize_Type = Gauge32
_CfprApStorageVirtualDriveBlockSize_Object = MibTableColumn
cfprApStorageVirtualDriveBlockSize = _CfprApStorageVirtualDriveBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 6),
    _CfprApStorageVirtualDriveBlockSize_Type()
)
cfprApStorageVirtualDriveBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveBlockSize.setStatus("current")
_CfprApStorageVirtualDriveBootable_Type = CfprApStorageBootableType
_CfprApStorageVirtualDriveBootable_Object = MibTableColumn
cfprApStorageVirtualDriveBootable = _CfprApStorageVirtualDriveBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 7),
    _CfprApStorageVirtualDriveBootable_Type()
)
cfprApStorageVirtualDriveBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveBootable.setStatus("current")
_CfprApStorageVirtualDriveConfiguredWriteCachePolicy_Type = CfprApStorageConfiguredWriteType
_CfprApStorageVirtualDriveConfiguredWriteCachePolicy_Object = MibTableColumn
cfprApStorageVirtualDriveConfiguredWriteCachePolicy = _CfprApStorageVirtualDriveConfiguredWriteCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 8),
    _CfprApStorageVirtualDriveConfiguredWriteCachePolicy_Type()
)
cfprApStorageVirtualDriveConfiguredWriteCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveConfiguredWriteCachePolicy.setStatus("current")
_CfprApStorageVirtualDriveConnectionProtocol_Type = CfprApStorageConnectionProtocol
_CfprApStorageVirtualDriveConnectionProtocol_Object = MibTableColumn
cfprApStorageVirtualDriveConnectionProtocol = _CfprApStorageVirtualDriveConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 9),
    _CfprApStorageVirtualDriveConnectionProtocol_Type()
)
cfprApStorageVirtualDriveConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveConnectionProtocol.setStatus("current")
_CfprApStorageVirtualDriveDriveCache_Type = CfprApStorageCacheType
_CfprApStorageVirtualDriveDriveCache_Object = MibTableColumn
cfprApStorageVirtualDriveDriveCache = _CfprApStorageVirtualDriveDriveCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 10),
    _CfprApStorageVirtualDriveDriveCache_Type()
)
cfprApStorageVirtualDriveDriveCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveDriveCache.setStatus("current")
_CfprApStorageVirtualDriveDriveState_Type = CfprApStorageVDriveState
_CfprApStorageVirtualDriveDriveState_Object = MibTableColumn
cfprApStorageVirtualDriveDriveState = _CfprApStorageVirtualDriveDriveState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 11),
    _CfprApStorageVirtualDriveDriveState_Type()
)
cfprApStorageVirtualDriveDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveDriveState.setStatus("current")
_CfprApStorageVirtualDriveId_Type = Gauge32
_CfprApStorageVirtualDriveId_Object = MibTableColumn
cfprApStorageVirtualDriveId = _CfprApStorageVirtualDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 12),
    _CfprApStorageVirtualDriveId_Type()
)
cfprApStorageVirtualDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveId.setStatus("current")
_CfprApStorageVirtualDriveIoPolicy_Type = CfprApStorageIOType
_CfprApStorageVirtualDriveIoPolicy_Object = MibTableColumn
cfprApStorageVirtualDriveIoPolicy = _CfprApStorageVirtualDriveIoPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 13),
    _CfprApStorageVirtualDriveIoPolicy_Type()
)
cfprApStorageVirtualDriveIoPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveIoPolicy.setStatus("current")
_CfprApStorageVirtualDriveLc_Type = CfprApFsmLifecycle
_CfprApStorageVirtualDriveLc_Object = MibTableColumn
cfprApStorageVirtualDriveLc = _CfprApStorageVirtualDriveLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 14),
    _CfprApStorageVirtualDriveLc_Type()
)
cfprApStorageVirtualDriveLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveLc.setStatus("current")
_CfprApStorageVirtualDriveModel_Type = SnmpAdminString
_CfprApStorageVirtualDriveModel_Object = MibTableColumn
cfprApStorageVirtualDriveModel = _CfprApStorageVirtualDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 15),
    _CfprApStorageVirtualDriveModel_Type()
)
cfprApStorageVirtualDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveModel.setStatus("current")
_CfprApStorageVirtualDriveNumberOfBlocks_Type = Unsigned64
_CfprApStorageVirtualDriveNumberOfBlocks_Object = MibTableColumn
cfprApStorageVirtualDriveNumberOfBlocks = _CfprApStorageVirtualDriveNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 16),
    _CfprApStorageVirtualDriveNumberOfBlocks_Type()
)
cfprApStorageVirtualDriveNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveNumberOfBlocks.setStatus("current")
_CfprApStorageVirtualDriveOperQualifierReason_Type = SnmpAdminString
_CfprApStorageVirtualDriveOperQualifierReason_Object = MibTableColumn
cfprApStorageVirtualDriveOperQualifierReason = _CfprApStorageVirtualDriveOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 17),
    _CfprApStorageVirtualDriveOperQualifierReason_Type()
)
cfprApStorageVirtualDriveOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveOperQualifierReason.setStatus("current")
_CfprApStorageVirtualDriveOperability_Type = CfprApEquipmentOperability
_CfprApStorageVirtualDriveOperability_Object = MibTableColumn
cfprApStorageVirtualDriveOperability = _CfprApStorageVirtualDriveOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 18),
    _CfprApStorageVirtualDriveOperability_Type()
)
cfprApStorageVirtualDriveOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveOperability.setStatus("current")
_CfprApStorageVirtualDrivePresence_Type = CfprApEquipmentPresence
_CfprApStorageVirtualDrivePresence_Object = MibTableColumn
cfprApStorageVirtualDrivePresence = _CfprApStorageVirtualDrivePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 19),
    _CfprApStorageVirtualDrivePresence_Type()
)
cfprApStorageVirtualDrivePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDrivePresence.setStatus("current")
_CfprApStorageVirtualDriveReadPolicy_Type = CfprApStorageReadType
_CfprApStorageVirtualDriveReadPolicy_Object = MibTableColumn
cfprApStorageVirtualDriveReadPolicy = _CfprApStorageVirtualDriveReadPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 20),
    _CfprApStorageVirtualDriveReadPolicy_Type()
)
cfprApStorageVirtualDriveReadPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveReadPolicy.setStatus("current")
_CfprApStorageVirtualDriveRevision_Type = SnmpAdminString
_CfprApStorageVirtualDriveRevision_Object = MibTableColumn
cfprApStorageVirtualDriveRevision = _CfprApStorageVirtualDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 21),
    _CfprApStorageVirtualDriveRevision_Type()
)
cfprApStorageVirtualDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveRevision.setStatus("current")
_CfprApStorageVirtualDriveSerial_Type = SnmpAdminString
_CfprApStorageVirtualDriveSerial_Object = MibTableColumn
cfprApStorageVirtualDriveSerial = _CfprApStorageVirtualDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 22),
    _CfprApStorageVirtualDriveSerial_Type()
)
cfprApStorageVirtualDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveSerial.setStatus("current")
_CfprApStorageVirtualDriveSize_Type = Unsigned64
_CfprApStorageVirtualDriveSize_Object = MibTableColumn
cfprApStorageVirtualDriveSize = _CfprApStorageVirtualDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 23),
    _CfprApStorageVirtualDriveSize_Type()
)
cfprApStorageVirtualDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveSize.setStatus("current")
_CfprApStorageVirtualDriveStripSize_Type = Unsigned64
_CfprApStorageVirtualDriveStripSize_Object = MibTableColumn
cfprApStorageVirtualDriveStripSize = _CfprApStorageVirtualDriveStripSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 24),
    _CfprApStorageVirtualDriveStripSize_Type()
)
cfprApStorageVirtualDriveStripSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveStripSize.setStatus("current")
_CfprApStorageVirtualDriveType_Type = CfprApStorageLunType
_CfprApStorageVirtualDriveType_Object = MibTableColumn
cfprApStorageVirtualDriveType = _CfprApStorageVirtualDriveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 25),
    _CfprApStorageVirtualDriveType_Type()
)
cfprApStorageVirtualDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveType.setStatus("current")
_CfprApStorageVirtualDriveVendor_Type = SnmpAdminString
_CfprApStorageVirtualDriveVendor_Object = MibTableColumn
cfprApStorageVirtualDriveVendor = _CfprApStorageVirtualDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 38, 1, 26),
    _CfprApStorageVirtualDriveVendor_Type()
)
cfprApStorageVirtualDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVirtualDriveVendor.setStatus("current")
_CfprApStorageVsanRefTable_Object = MibTable
cfprApStorageVsanRefTable = _CfprApStorageVsanRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 39)
)
if mibBuilder.loadTexts:
    cfprApStorageVsanRefTable.setStatus("current")
_CfprApStorageVsanRefEntry_Object = MibTableRow
cfprApStorageVsanRefEntry = _CfprApStorageVsanRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 39, 1)
)
cfprApStorageVsanRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STORAGE-MIB", "cfprApStorageVsanRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStorageVsanRefEntry.setStatus("current")
_CfprApStorageVsanRefInstanceId_Type = CfprApManagedObjectId
_CfprApStorageVsanRefInstanceId_Object = MibTableColumn
cfprApStorageVsanRefInstanceId = _CfprApStorageVsanRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 39, 1, 1),
    _CfprApStorageVsanRefInstanceId_Type()
)
cfprApStorageVsanRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStorageVsanRefInstanceId.setStatus("current")
_CfprApStorageVsanRefDn_Type = CfprApManagedObjectDn
_CfprApStorageVsanRefDn_Object = MibTableColumn
cfprApStorageVsanRefDn = _CfprApStorageVsanRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 39, 1, 2),
    _CfprApStorageVsanRefDn_Type()
)
cfprApStorageVsanRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVsanRefDn.setStatus("current")
_CfprApStorageVsanRefRn_Type = SnmpAdminString
_CfprApStorageVsanRefRn_Object = MibTableColumn
cfprApStorageVsanRefRn = _CfprApStorageVsanRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 39, 1, 3),
    _CfprApStorageVsanRefRn_Type()
)
cfprApStorageVsanRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVsanRefRn.setStatus("current")
_CfprApStorageVsanRefConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApStorageVsanRefConfigQualifier_Object = MibTableColumn
cfprApStorageVsanRefConfigQualifier = _CfprApStorageVsanRefConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 39, 1, 4),
    _CfprApStorageVsanRefConfigQualifier_Type()
)
cfprApStorageVsanRefConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVsanRefConfigQualifier.setStatus("current")
_CfprApStorageVsanRefName_Type = SnmpAdminString
_CfprApStorageVsanRefName_Object = MibTableColumn
cfprApStorageVsanRefName = _CfprApStorageVsanRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 39, 1, 5),
    _CfprApStorageVsanRefName_Type()
)
cfprApStorageVsanRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVsanRefName.setStatus("current")
_CfprApStorageVsanRefOperVnetDn_Type = SnmpAdminString
_CfprApStorageVsanRefOperVnetDn_Object = MibTableColumn
cfprApStorageVsanRefOperVnetDn = _CfprApStorageVsanRefOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 39, 1, 6),
    _CfprApStorageVsanRefOperVnetDn_Type()
)
cfprApStorageVsanRefOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVsanRefOperVnetDn.setStatus("current")
_CfprApStorageVsanRefOperVnetName_Type = SnmpAdminString
_CfprApStorageVsanRefOperVnetName_Object = MibTableColumn
cfprApStorageVsanRefOperVnetName = _CfprApStorageVsanRefOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 39, 1, 7),
    _CfprApStorageVsanRefOperVnetName_Type()
)
cfprApStorageVsanRefOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVsanRefOperVnetName.setStatus("current")
_CfprApStorageVsanRefSwitchId_Type = CfprApStorageVsanRefSwitchId
_CfprApStorageVsanRefSwitchId_Object = MibTableColumn
cfprApStorageVsanRefSwitchId = _CfprApStorageVsanRefSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 39, 1, 8),
    _CfprApStorageVsanRefSwitchId_Type()
)
cfprApStorageVsanRefSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVsanRefSwitchId.setStatus("current")
_CfprApStorageVsanRefVnet_Type = Gauge32
_CfprApStorageVsanRefVnet_Object = MibTableColumn
cfprApStorageVsanRefVnet = _CfprApStorageVsanRefVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 39, 1, 9),
    _CfprApStorageVsanRefVnet_Type()
)
cfprApStorageVsanRefVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVsanRefVnet.setStatus("current")
_CfprApStorageVsanRefZoningState_Type = CfprApFabricZoningState
_CfprApStorageVsanRefZoningState_Object = MibTableColumn
cfprApStorageVsanRefZoningState = _CfprApStorageVsanRefZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 74, 39, 1, 10),
    _CfprApStorageVsanRefZoningState_Type()
)
cfprApStorageVsanRefZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStorageVsanRefZoningState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-STORAGE-MIB",
    **{"cfprApStorageObjects": cfprApStorageObjects,
       "cfprApStorageAuthKeyTable": cfprApStorageAuthKeyTable,
       "cfprApStorageAuthKeyEntry": cfprApStorageAuthKeyEntry,
       "cfprApStorageAuthKeyInstanceId": cfprApStorageAuthKeyInstanceId,
       "cfprApStorageAuthKeyDn": cfprApStorageAuthKeyDn,
       "cfprApStorageAuthKeyRn": cfprApStorageAuthKeyRn,
       "cfprApStorageAuthKeyDescr": cfprApStorageAuthKeyDescr,
       "cfprApStorageAuthKeyIntId": cfprApStorageAuthKeyIntId,
       "cfprApStorageAuthKeyName": cfprApStorageAuthKeyName,
       "cfprApStorageAuthKeyPassword": cfprApStorageAuthKeyPassword,
       "cfprApStorageAuthKeyPolicyLevel": cfprApStorageAuthKeyPolicyLevel,
       "cfprApStorageAuthKeyPolicyOwner": cfprApStorageAuthKeyPolicyOwner,
       "cfprApStorageAuthKeyType": cfprApStorageAuthKeyType,
       "cfprApStorageAuthKeyUserId": cfprApStorageAuthKeyUserId,
       "cfprApStorageControllerTable": cfprApStorageControllerTable,
       "cfprApStorageControllerEntry": cfprApStorageControllerEntry,
       "cfprApStorageControllerInstanceId": cfprApStorageControllerInstanceId,
       "cfprApStorageControllerDn": cfprApStorageControllerDn,
       "cfprApStorageControllerRn": cfprApStorageControllerRn,
       "cfprApStorageControllerControllerStatus": cfprApStorageControllerControllerStatus,
       "cfprApStorageControllerDeviceRaidSupport": cfprApStorageControllerDeviceRaidSupport,
       "cfprApStorageControllerFaultMonitoring": cfprApStorageControllerFaultMonitoring,
       "cfprApStorageControllerHwRevision": cfprApStorageControllerHwRevision,
       "cfprApStorageControllerId": cfprApStorageControllerId,
       "cfprApStorageControllerLc": cfprApStorageControllerLc,
       "cfprApStorageControllerLocationDn": cfprApStorageControllerLocationDn,
       "cfprApStorageControllerModel": cfprApStorageControllerModel,
       "cfprApStorageControllerOobControllerId": cfprApStorageControllerOobControllerId,
       "cfprApStorageControllerOobInterfaceSupported": cfprApStorageControllerOobInterfaceSupported,
       "cfprApStorageControllerOperQualifierReason": cfprApStorageControllerOperQualifierReason,
       "cfprApStorageControllerOperState": cfprApStorageControllerOperState,
       "cfprApStorageControllerOperability": cfprApStorageControllerOperability,
       "cfprApStorageControllerPartNumber": cfprApStorageControllerPartNumber,
       "cfprApStorageControllerPciAddr": cfprApStorageControllerPciAddr,
       "cfprApStorageControllerPciSlot": cfprApStorageControllerPciSlot,
       "cfprApStorageControllerPerf": cfprApStorageControllerPerf,
       "cfprApStorageControllerPower": cfprApStorageControllerPower,
       "cfprApStorageControllerPresence": cfprApStorageControllerPresence,
       "cfprApStorageControllerRaidSupport": cfprApStorageControllerRaidSupport,
       "cfprApStorageControllerRebuildRate": cfprApStorageControllerRebuildRate,
       "cfprApStorageControllerRevision": cfprApStorageControllerRevision,
       "cfprApStorageControllerSerial": cfprApStorageControllerSerial,
       "cfprApStorageControllerThermal": cfprApStorageControllerThermal,
       "cfprApStorageControllerType": cfprApStorageControllerType,
       "cfprApStorageControllerVendor": cfprApStorageControllerVendor,
       "cfprApStorageControllerVid": cfprApStorageControllerVid,
       "cfprApStorageControllerVoltage": cfprApStorageControllerVoltage,
       "cfprApStorageDomainEpTable": cfprApStorageDomainEpTable,
       "cfprApStorageDomainEpEntry": cfprApStorageDomainEpEntry,
       "cfprApStorageDomainEpInstanceId": cfprApStorageDomainEpInstanceId,
       "cfprApStorageDomainEpDn": cfprApStorageDomainEpDn,
       "cfprApStorageDomainEpRn": cfprApStorageDomainEpRn,
       "cfprApStorageDriveTable": cfprApStorageDriveTable,
       "cfprApStorageDriveEntry": cfprApStorageDriveEntry,
       "cfprApStorageDriveInstanceId": cfprApStorageDriveInstanceId,
       "cfprApStorageDriveDn": cfprApStorageDriveDn,
       "cfprApStorageDriveRn": cfprApStorageDriveRn,
       "cfprApStorageDriveId": cfprApStorageDriveId,
       "cfprApStorageDriveModel": cfprApStorageDriveModel,
       "cfprApStorageDrivePciAddr": cfprApStorageDrivePciAddr,
       "cfprApStorageDriveRevision": cfprApStorageDriveRevision,
       "cfprApStorageDriveSerial": cfprApStorageDriveSerial,
       "cfprApStorageDriveVendor": cfprApStorageDriveVendor,
       "cfprApStorageEnclosureTable": cfprApStorageEnclosureTable,
       "cfprApStorageEnclosureEntry": cfprApStorageEnclosureEntry,
       "cfprApStorageEnclosureInstanceId": cfprApStorageEnclosureInstanceId,
       "cfprApStorageEnclosureDn": cfprApStorageEnclosureDn,
       "cfprApStorageEnclosureRn": cfprApStorageEnclosureRn,
       "cfprApStorageEnclosureId": cfprApStorageEnclosureId,
       "cfprApStorageEnclosureLc": cfprApStorageEnclosureLc,
       "cfprApStorageEnclosureModel": cfprApStorageEnclosureModel,
       "cfprApStorageEnclosureNumSlots": cfprApStorageEnclosureNumSlots,
       "cfprApStorageEnclosureRevision": cfprApStorageEnclosureRevision,
       "cfprApStorageEnclosureSerial": cfprApStorageEnclosureSerial,
       "cfprApStorageEnclosureVendor": cfprApStorageEnclosureVendor,
       "cfprApStorageEpUserTable": cfprApStorageEpUserTable,
       "cfprApStorageEpUserEntry": cfprApStorageEpUserEntry,
       "cfprApStorageEpUserInstanceId": cfprApStorageEpUserInstanceId,
       "cfprApStorageEpUserDn": cfprApStorageEpUserDn,
       "cfprApStorageEpUserRn": cfprApStorageEpUserRn,
       "cfprApStorageEpUserConfigState": cfprApStorageEpUserConfigState,
       "cfprApStorageEpUserConfigStatusMessage": cfprApStorageEpUserConfigStatusMessage,
       "cfprApStorageEpUserDescr": cfprApStorageEpUserDescr,
       "cfprApStorageEpUserDomain": cfprApStorageEpUserDomain,
       "cfprApStorageEpUserName": cfprApStorageEpUserName,
       "cfprApStorageEpUserPriv": cfprApStorageEpUserPriv,
       "cfprApStorageEpUserPwd": cfprApStorageEpUserPwd,
       "cfprApStorageEpUserPwdSet": cfprApStorageEpUserPwdSet,
       "cfprApStorageEtherIfTable": cfprApStorageEtherIfTable,
       "cfprApStorageEtherIfEntry": cfprApStorageEtherIfEntry,
       "cfprApStorageEtherIfInstanceId": cfprApStorageEtherIfInstanceId,
       "cfprApStorageEtherIfDn": cfprApStorageEtherIfDn,
       "cfprApStorageEtherIfRn": cfprApStorageEtherIfRn,
       "cfprApStorageEtherIfName": cfprApStorageEtherIfName,
       "cfprApStorageEtherIfVlanType": cfprApStorageEtherIfVlanType,
       "cfprApStorageFcIfTable": cfprApStorageFcIfTable,
       "cfprApStorageFcIfEntry": cfprApStorageFcIfEntry,
       "cfprApStorageFcIfInstanceId": cfprApStorageFcIfInstanceId,
       "cfprApStorageFcIfDn": cfprApStorageFcIfDn,
       "cfprApStorageFcIfRn": cfprApStorageFcIfRn,
       "cfprApStorageFcIfName": cfprApStorageFcIfName,
       "cfprApStorageFcTargetIfTable": cfprApStorageFcTargetIfTable,
       "cfprApStorageFcTargetIfEntry": cfprApStorageFcTargetIfEntry,
       "cfprApStorageFcTargetIfInstanceId": cfprApStorageFcTargetIfInstanceId,
       "cfprApStorageFcTargetIfDn": cfprApStorageFcTargetIfDn,
       "cfprApStorageFcTargetIfRn": cfprApStorageFcTargetIfRn,
       "cfprApStorageFcTargetIfId": cfprApStorageFcTargetIfId,
       "cfprApStorageFcTargetIfProt": cfprApStorageFcTargetIfProt,
       "cfprApStorageFlexFlashCardTable": cfprApStorageFlexFlashCardTable,
       "cfprApStorageFlexFlashCardEntry": cfprApStorageFlexFlashCardEntry,
       "cfprApStorageFlexFlashCardInstanceId": cfprApStorageFlexFlashCardInstanceId,
       "cfprApStorageFlexFlashCardDn": cfprApStorageFlexFlashCardDn,
       "cfprApStorageFlexFlashCardRn": cfprApStorageFlexFlashCardRn,
       "cfprApStorageFlexFlashCardBlockSize": cfprApStorageFlexFlashCardBlockSize,
       "cfprApStorageFlexFlashCardCardHealth": cfprApStorageFlexFlashCardCardHealth,
       "cfprApStorageFlexFlashCardCardMode": cfprApStorageFlexFlashCardCardMode,
       "cfprApStorageFlexFlashCardCardState": cfprApStorageFlexFlashCardCardState,
       "cfprApStorageFlexFlashCardCardSync": cfprApStorageFlexFlashCardCardSync,
       "cfprApStorageFlexFlashCardCardType": cfprApStorageFlexFlashCardCardType,
       "cfprApStorageFlexFlashCardConnectionProtocol": cfprApStorageFlexFlashCardConnectionProtocol,
       "cfprApStorageFlexFlashCardControllerIndex": cfprApStorageFlexFlashCardControllerIndex,
       "cfprApStorageFlexFlashCardDrivesEnabled": cfprApStorageFlexFlashCardDrivesEnabled,
       "cfprApStorageFlexFlashCardId": cfprApStorageFlexFlashCardId,
       "cfprApStorageFlexFlashCardMfgDate": cfprApStorageFlexFlashCardMfgDate,
       "cfprApStorageFlexFlashCardMfgId": cfprApStorageFlexFlashCardMfgId,
       "cfprApStorageFlexFlashCardModel": cfprApStorageFlexFlashCardModel,
       "cfprApStorageFlexFlashCardNumberOfBlocks": cfprApStorageFlexFlashCardNumberOfBlocks,
       "cfprApStorageFlexFlashCardOemId": cfprApStorageFlexFlashCardOemId,
       "cfprApStorageFlexFlashCardOperQualifierReason": cfprApStorageFlexFlashCardOperQualifierReason,
       "cfprApStorageFlexFlashCardOperability": cfprApStorageFlexFlashCardOperability,
       "cfprApStorageFlexFlashCardPartitionCount": cfprApStorageFlexFlashCardPartitionCount,
       "cfprApStorageFlexFlashCardPresence": cfprApStorageFlexFlashCardPresence,
       "cfprApStorageFlexFlashCardReadErrorThreshold": cfprApStorageFlexFlashCardReadErrorThreshold,
       "cfprApStorageFlexFlashCardReadIOErrorCount": cfprApStorageFlexFlashCardReadIOErrorCount,
       "cfprApStorageFlexFlashCardRevision": cfprApStorageFlexFlashCardRevision,
       "cfprApStorageFlexFlashCardSerial": cfprApStorageFlexFlashCardSerial,
       "cfprApStorageFlexFlashCardSignature": cfprApStorageFlexFlashCardSignature,
       "cfprApStorageFlexFlashCardSize": cfprApStorageFlexFlashCardSize,
       "cfprApStorageFlexFlashCardSlotNumber": cfprApStorageFlexFlashCardSlotNumber,
       "cfprApStorageFlexFlashCardVendor": cfprApStorageFlexFlashCardVendor,
       "cfprApStorageFlexFlashCardWriteEnable": cfprApStorageFlexFlashCardWriteEnable,
       "cfprApStorageFlexFlashCardWriteErrorThreshold": cfprApStorageFlexFlashCardWriteErrorThreshold,
       "cfprApStorageFlexFlashCardWriteIOErrorCount": cfprApStorageFlexFlashCardWriteIOErrorCount,
       "cfprApStorageFlexFlashControllerTable": cfprApStorageFlexFlashControllerTable,
       "cfprApStorageFlexFlashControllerEntry": cfprApStorageFlexFlashControllerEntry,
       "cfprApStorageFlexFlashControllerInstanceId": cfprApStorageFlexFlashControllerInstanceId,
       "cfprApStorageFlexFlashControllerDn": cfprApStorageFlexFlashControllerDn,
       "cfprApStorageFlexFlashControllerRn": cfprApStorageFlexFlashControllerRn,
       "cfprApStorageFlexFlashControllerAdminSlotNumber": cfprApStorageFlexFlashControllerAdminSlotNumber,
       "cfprApStorageFlexFlashControllerConfiguredMode": cfprApStorageFlexFlashControllerConfiguredMode,
       "cfprApStorageFlexFlashControllerControllerHealth": cfprApStorageFlexFlashControllerControllerHealth,
       "cfprApStorageFlexFlashControllerControllerState": cfprApStorageFlexFlashControllerControllerState,
       "cfprApStorageFlexFlashControllerFirmwareVersion": cfprApStorageFlexFlashControllerFirmwareVersion,
       "cfprApStorageFlexFlashControllerFlexFlashType": cfprApStorageFlexFlashControllerFlexFlashType,
       "cfprApStorageFlexFlashControllerHasError": cfprApStorageFlexFlashControllerHasError,
       "cfprApStorageFlexFlashControllerId": cfprApStorageFlexFlashControllerId,
       "cfprApStorageFlexFlashControllerIsCardMismatch": cfprApStorageFlexFlashControllerIsCardMismatch,
       "cfprApStorageFlexFlashControllerIsFormatFSMRunning": cfprApStorageFlexFlashControllerIsFormatFSMRunning,
       "cfprApStorageFlexFlashControllerLocationDn": cfprApStorageFlexFlashControllerLocationDn,
       "cfprApStorageFlexFlashControllerModel": cfprApStorageFlexFlashControllerModel,
       "cfprApStorageFlexFlashControllerOperQualifierReason": cfprApStorageFlexFlashControllerOperQualifierReason,
       "cfprApStorageFlexFlashControllerOperState": cfprApStorageFlexFlashControllerOperState,
       "cfprApStorageFlexFlashControllerOperability": cfprApStorageFlexFlashControllerOperability,
       "cfprApStorageFlexFlashControllerOperatingMode": cfprApStorageFlexFlashControllerOperatingMode,
       "cfprApStorageFlexFlashControllerOperationRequest": cfprApStorageFlexFlashControllerOperationRequest,
       "cfprApStorageFlexFlashControllerPciAddr": cfprApStorageFlexFlashControllerPciAddr,
       "cfprApStorageFlexFlashControllerPciSlot": cfprApStorageFlexFlashControllerPciSlot,
       "cfprApStorageFlexFlashControllerPerf": cfprApStorageFlexFlashControllerPerf,
       "cfprApStorageFlexFlashControllerPhysicalDriveCount": cfprApStorageFlexFlashControllerPhysicalDriveCount,
       "cfprApStorageFlexFlashControllerPower": cfprApStorageFlexFlashControllerPower,
       "cfprApStorageFlexFlashControllerPresence": cfprApStorageFlexFlashControllerPresence,
       "cfprApStorageFlexFlashControllerPrimarySlotNumber": cfprApStorageFlexFlashControllerPrimarySlotNumber,
       "cfprApStorageFlexFlashControllerRaidSyncSupport": cfprApStorageFlexFlashControllerRaidSyncSupport,
       "cfprApStorageFlexFlashControllerReadErrorThreshold": cfprApStorageFlexFlashControllerReadErrorThreshold,
       "cfprApStorageFlexFlashControllerRevision": cfprApStorageFlexFlashControllerRevision,
       "cfprApStorageFlexFlashControllerSerial": cfprApStorageFlexFlashControllerSerial,
       "cfprApStorageFlexFlashControllerThermal": cfprApStorageFlexFlashControllerThermal,
       "cfprApStorageFlexFlashControllerType": cfprApStorageFlexFlashControllerType,
       "cfprApStorageFlexFlashControllerVendor": cfprApStorageFlexFlashControllerVendor,
       "cfprApStorageFlexFlashControllerVirtualDriveCount": cfprApStorageFlexFlashControllerVirtualDriveCount,
       "cfprApStorageFlexFlashControllerVoltage": cfprApStorageFlexFlashControllerVoltage,
       "cfprApStorageFlexFlashControllerWriteErrorThreshold": cfprApStorageFlexFlashControllerWriteErrorThreshold,
       "cfprApStorageFlexFlashDriveTable": cfprApStorageFlexFlashDriveTable,
       "cfprApStorageFlexFlashDriveEntry": cfprApStorageFlexFlashDriveEntry,
       "cfprApStorageFlexFlashDriveInstanceId": cfprApStorageFlexFlashDriveInstanceId,
       "cfprApStorageFlexFlashDriveDn": cfprApStorageFlexFlashDriveDn,
       "cfprApStorageFlexFlashDriveRn": cfprApStorageFlexFlashDriveRn,
       "cfprApStorageFlexFlashDriveRWType": cfprApStorageFlexFlashDriveRWType,
       "cfprApStorageFlexFlashDriveBlockSize": cfprApStorageFlexFlashDriveBlockSize,
       "cfprApStorageFlexFlashDriveConnectionProtocol": cfprApStorageFlexFlashDriveConnectionProtocol,
       "cfprApStorageFlexFlashDriveControllerIndex": cfprApStorageFlexFlashDriveControllerIndex,
       "cfprApStorageFlexFlashDriveDriveState": cfprApStorageFlexFlashDriveDriveState,
       "cfprApStorageFlexFlashDriveDriveType": cfprApStorageFlexFlashDriveDriveType,
       "cfprApStorageFlexFlashDriveId": cfprApStorageFlexFlashDriveId,
       "cfprApStorageFlexFlashDriveLastOperation": cfprApStorageFlexFlashDriveLastOperation,
       "cfprApStorageFlexFlashDriveModel": cfprApStorageFlexFlashDriveModel,
       "cfprApStorageFlexFlashDriveName": cfprApStorageFlexFlashDriveName,
       "cfprApStorageFlexFlashDriveNumberOfBlocks": cfprApStorageFlexFlashDriveNumberOfBlocks,
       "cfprApStorageFlexFlashDriveOperQualifierReason": cfprApStorageFlexFlashDriveOperQualifierReason,
       "cfprApStorageFlexFlashDriveOperability": cfprApStorageFlexFlashDriveOperability,
       "cfprApStorageFlexFlashDriveOperationState": cfprApStorageFlexFlashDriveOperationState,
       "cfprApStorageFlexFlashDrivePresence": cfprApStorageFlexFlashDrivePresence,
       "cfprApStorageFlexFlashDriveRemovable": cfprApStorageFlexFlashDriveRemovable,
       "cfprApStorageFlexFlashDriveRevision": cfprApStorageFlexFlashDriveRevision,
       "cfprApStorageFlexFlashDriveSerial": cfprApStorageFlexFlashDriveSerial,
       "cfprApStorageFlexFlashDriveSize": cfprApStorageFlexFlashDriveSize,
       "cfprApStorageFlexFlashDriveSlotNumber": cfprApStorageFlexFlashDriveSlotNumber,
       "cfprApStorageFlexFlashDriveVendor": cfprApStorageFlexFlashDriveVendor,
       "cfprApStorageFlexFlashDriveVisible": cfprApStorageFlexFlashDriveVisible,
       "cfprApStorageFlexFlashVirtualDriveTable": cfprApStorageFlexFlashVirtualDriveTable,
       "cfprApStorageFlexFlashVirtualDriveEntry": cfprApStorageFlexFlashVirtualDriveEntry,
       "cfprApStorageFlexFlashVirtualDriveInstanceId": cfprApStorageFlexFlashVirtualDriveInstanceId,
       "cfprApStorageFlexFlashVirtualDriveDn": cfprApStorageFlexFlashVirtualDriveDn,
       "cfprApStorageFlexFlashVirtualDriveRn": cfprApStorageFlexFlashVirtualDriveRn,
       "cfprApStorageFlexFlashVirtualDriveBlockSize": cfprApStorageFlexFlashVirtualDriveBlockSize,
       "cfprApStorageFlexFlashVirtualDriveConnectionProtocol": cfprApStorageFlexFlashVirtualDriveConnectionProtocol,
       "cfprApStorageFlexFlashVirtualDriveId": cfprApStorageFlexFlashVirtualDriveId,
       "cfprApStorageFlexFlashVirtualDriveModel": cfprApStorageFlexFlashVirtualDriveModel,
       "cfprApStorageFlexFlashVirtualDriveNumberOfBlocks": cfprApStorageFlexFlashVirtualDriveNumberOfBlocks,
       "cfprApStorageFlexFlashVirtualDriveOperQualifierReason": cfprApStorageFlexFlashVirtualDriveOperQualifierReason,
       "cfprApStorageFlexFlashVirtualDriveOperability": cfprApStorageFlexFlashVirtualDriveOperability,
       "cfprApStorageFlexFlashVirtualDrivePresence": cfprApStorageFlexFlashVirtualDrivePresence,
       "cfprApStorageFlexFlashVirtualDriveRaidHealth": cfprApStorageFlexFlashVirtualDriveRaidHealth,
       "cfprApStorageFlexFlashVirtualDriveRaidState": cfprApStorageFlexFlashVirtualDriveRaidState,
       "cfprApStorageFlexFlashVirtualDriveRevision": cfprApStorageFlexFlashVirtualDriveRevision,
       "cfprApStorageFlexFlashVirtualDriveSerial": cfprApStorageFlexFlashVirtualDriveSerial,
       "cfprApStorageFlexFlashVirtualDriveSize": cfprApStorageFlexFlashVirtualDriveSize,
       "cfprApStorageFlexFlashVirtualDriveType": cfprApStorageFlexFlashVirtualDriveType,
       "cfprApStorageFlexFlashVirtualDriveVendor": cfprApStorageFlexFlashVirtualDriveVendor,
       "cfprApStorageIScsiTargetIfTable": cfprApStorageIScsiTargetIfTable,
       "cfprApStorageIScsiTargetIfEntry": cfprApStorageIScsiTargetIfEntry,
       "cfprApStorageIScsiTargetIfInstanceId": cfprApStorageIScsiTargetIfInstanceId,
       "cfprApStorageIScsiTargetIfDn": cfprApStorageIScsiTargetIfDn,
       "cfprApStorageIScsiTargetIfRn": cfprApStorageIScsiTargetIfRn,
       "cfprApStorageIScsiTargetIfName": cfprApStorageIScsiTargetIfName,
       "cfprApStorageIScsiTargetIfProt": cfprApStorageIScsiTargetIfProt,
       "cfprApStorageItemTable": cfprApStorageItemTable,
       "cfprApStorageItemEntry": cfprApStorageItemEntry,
       "cfprApStorageItemInstanceId": cfprApStorageItemInstanceId,
       "cfprApStorageItemDn": cfprApStorageItemDn,
       "cfprApStorageItemRn": cfprApStorageItemRn,
       "cfprApStorageItemName": cfprApStorageItemName,
       "cfprApStorageItemOperState": cfprApStorageItemOperState,
       "cfprApStorageItemSize": cfprApStorageItemSize,
       "cfprApStorageItemUsed": cfprApStorageItemUsed,
       "cfprApStorageLocalDiskTable": cfprApStorageLocalDiskTable,
       "cfprApStorageLocalDiskEntry": cfprApStorageLocalDiskEntry,
       "cfprApStorageLocalDiskInstanceId": cfprApStorageLocalDiskInstanceId,
       "cfprApStorageLocalDiskDn": cfprApStorageLocalDiskDn,
       "cfprApStorageLocalDiskRn": cfprApStorageLocalDiskRn,
       "cfprApStorageLocalDiskBlockSize": cfprApStorageLocalDiskBlockSize,
       "cfprApStorageLocalDiskConnectionProtocol": cfprApStorageLocalDiskConnectionProtocol,
       "cfprApStorageLocalDiskDeviceType": cfprApStorageLocalDiskDeviceType,
       "cfprApStorageLocalDiskDiskState": cfprApStorageLocalDiskDiskState,
       "cfprApStorageLocalDiskId": cfprApStorageLocalDiskId,
       "cfprApStorageLocalDiskLc": cfprApStorageLocalDiskLc,
       "cfprApStorageLocalDiskLinkSpeed": cfprApStorageLocalDiskLinkSpeed,
       "cfprApStorageLocalDiskModel": cfprApStorageLocalDiskModel,
       "cfprApStorageLocalDiskNumberOfBlocks": cfprApStorageLocalDiskNumberOfBlocks,
       "cfprApStorageLocalDiskOperQualifierReason": cfprApStorageLocalDiskOperQualifierReason,
       "cfprApStorageLocalDiskOperability": cfprApStorageLocalDiskOperability,
       "cfprApStorageLocalDiskPowerState": cfprApStorageLocalDiskPowerState,
       "cfprApStorageLocalDiskPresence": cfprApStorageLocalDiskPresence,
       "cfprApStorageLocalDiskRevision": cfprApStorageLocalDiskRevision,
       "cfprApStorageLocalDiskSerial": cfprApStorageLocalDiskSerial,
       "cfprApStorageLocalDiskSize": cfprApStorageLocalDiskSize,
       "cfprApStorageLocalDiskVendor": cfprApStorageLocalDiskVendor,
       "cfprApStorageLocalDiskConfigDefTable": cfprApStorageLocalDiskConfigDefTable,
       "cfprApStorageLocalDiskConfigDefEntry": cfprApStorageLocalDiskConfigDefEntry,
       "cfprApStorageLocalDiskConfigDefInstanceId": cfprApStorageLocalDiskConfigDefInstanceId,
       "cfprApStorageLocalDiskConfigDefDn": cfprApStorageLocalDiskConfigDefDn,
       "cfprApStorageLocalDiskConfigDefRn": cfprApStorageLocalDiskConfigDefRn,
       "cfprApStorageLocalDiskConfigDefDescr": cfprApStorageLocalDiskConfigDefDescr,
       "cfprApStorageLocalDiskConfigDefFlexFlashRAIDReportingState": cfprApStorageLocalDiskConfigDefFlexFlashRAIDReportingState,
       "cfprApStorageLocalDiskConfigDefFlexFlashState": cfprApStorageLocalDiskConfigDefFlexFlashState,
       "cfprApStorageLocalDiskConfigDefIntId": cfprApStorageLocalDiskConfigDefIntId,
       "cfprApStorageLocalDiskConfigDefMode": cfprApStorageLocalDiskConfigDefMode,
       "cfprApStorageLocalDiskConfigDefName": cfprApStorageLocalDiskConfigDefName,
       "cfprApStorageLocalDiskConfigDefPolicyLevel": cfprApStorageLocalDiskConfigDefPolicyLevel,
       "cfprApStorageLocalDiskConfigDefPolicyOwner": cfprApStorageLocalDiskConfigDefPolicyOwner,
       "cfprApStorageLocalDiskConfigDefProtectConfig": cfprApStorageLocalDiskConfigDefProtectConfig,
       "cfprApStorageLocalDiskConfigPolicyTable": cfprApStorageLocalDiskConfigPolicyTable,
       "cfprApStorageLocalDiskConfigPolicyEntry": cfprApStorageLocalDiskConfigPolicyEntry,
       "cfprApStorageLocalDiskConfigPolicyInstanceId": cfprApStorageLocalDiskConfigPolicyInstanceId,
       "cfprApStorageLocalDiskConfigPolicyDn": cfprApStorageLocalDiskConfigPolicyDn,
       "cfprApStorageLocalDiskConfigPolicyRn": cfprApStorageLocalDiskConfigPolicyRn,
       "cfprApStorageLocalDiskConfigPolicyDescr": cfprApStorageLocalDiskConfigPolicyDescr,
       "cfprApStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState": cfprApStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState,
       "cfprApStorageLocalDiskConfigPolicyFlexFlashState": cfprApStorageLocalDiskConfigPolicyFlexFlashState,
       "cfprApStorageLocalDiskConfigPolicyIntId": cfprApStorageLocalDiskConfigPolicyIntId,
       "cfprApStorageLocalDiskConfigPolicyMode": cfprApStorageLocalDiskConfigPolicyMode,
       "cfprApStorageLocalDiskConfigPolicyName": cfprApStorageLocalDiskConfigPolicyName,
       "cfprApStorageLocalDiskConfigPolicyPolicyLevel": cfprApStorageLocalDiskConfigPolicyPolicyLevel,
       "cfprApStorageLocalDiskConfigPolicyPolicyOwner": cfprApStorageLocalDiskConfigPolicyPolicyOwner,
       "cfprApStorageLocalDiskConfigPolicyProtectConfig": cfprApStorageLocalDiskConfigPolicyProtectConfig,
       "cfprApStorageLocalDiskPartitionTable": cfprApStorageLocalDiskPartitionTable,
       "cfprApStorageLocalDiskPartitionEntry": cfprApStorageLocalDiskPartitionEntry,
       "cfprApStorageLocalDiskPartitionInstanceId": cfprApStorageLocalDiskPartitionInstanceId,
       "cfprApStorageLocalDiskPartitionDn": cfprApStorageLocalDiskPartitionDn,
       "cfprApStorageLocalDiskPartitionRn": cfprApStorageLocalDiskPartitionRn,
       "cfprApStorageLocalDiskPartitionDescr": cfprApStorageLocalDiskPartitionDescr,
       "cfprApStorageLocalDiskPartitionIntId": cfprApStorageLocalDiskPartitionIntId,
       "cfprApStorageLocalDiskPartitionName": cfprApStorageLocalDiskPartitionName,
       "cfprApStorageLocalDiskPartitionOrder": cfprApStorageLocalDiskPartitionOrder,
       "cfprApStorageLocalDiskPartitionPolicyLevel": cfprApStorageLocalDiskPartitionPolicyLevel,
       "cfprApStorageLocalDiskPartitionPolicyOwner": cfprApStorageLocalDiskPartitionPolicyOwner,
       "cfprApStorageLocalDiskPartitionSize": cfprApStorageLocalDiskPartitionSize,
       "cfprApStorageLocalDiskPartitionType": cfprApStorageLocalDiskPartitionType,
       "cfprApStorageLocalDiskSlotEpTable": cfprApStorageLocalDiskSlotEpTable,
       "cfprApStorageLocalDiskSlotEpEntry": cfprApStorageLocalDiskSlotEpEntry,
       "cfprApStorageLocalDiskSlotEpInstanceId": cfprApStorageLocalDiskSlotEpInstanceId,
       "cfprApStorageLocalDiskSlotEpDn": cfprApStorageLocalDiskSlotEpDn,
       "cfprApStorageLocalDiskSlotEpRn": cfprApStorageLocalDiskSlotEpRn,
       "cfprApStorageLocalDiskSlotEpConfiguration": cfprApStorageLocalDiskSlotEpConfiguration,
       "cfprApStorageLocalDiskSlotEpId": cfprApStorageLocalDiskSlotEpId,
       "cfprApStorageLocalDiskSlotEpOperQualifierReason": cfprApStorageLocalDiskSlotEpOperQualifierReason,
       "cfprApStorageLocalDiskSlotEpOperability": cfprApStorageLocalDiskSlotEpOperability,
       "cfprApStorageLocalDiskSlotEpPeerDn": cfprApStorageLocalDiskSlotEpPeerDn,
       "cfprApStorageLocalDiskSlotEpPresence": cfprApStorageLocalDiskSlotEpPresence,
       "cfprApStorageLocalLunTable": cfprApStorageLocalLunTable,
       "cfprApStorageLocalLunEntry": cfprApStorageLocalLunEntry,
       "cfprApStorageLocalLunInstanceId": cfprApStorageLocalLunInstanceId,
       "cfprApStorageLocalLunDn": cfprApStorageLocalLunDn,
       "cfprApStorageLocalLunRn": cfprApStorageLocalLunRn,
       "cfprApStorageLocalLunBlockSize": cfprApStorageLocalLunBlockSize,
       "cfprApStorageLocalLunConnectionProtocol": cfprApStorageLocalLunConnectionProtocol,
       "cfprApStorageLocalLunId": cfprApStorageLocalLunId,
       "cfprApStorageLocalLunLc": cfprApStorageLocalLunLc,
       "cfprApStorageLocalLunModel": cfprApStorageLocalLunModel,
       "cfprApStorageLocalLunNumberOfBlocks": cfprApStorageLocalLunNumberOfBlocks,
       "cfprApStorageLocalLunOperQualifierReason": cfprApStorageLocalLunOperQualifierReason,
       "cfprApStorageLocalLunOperability": cfprApStorageLocalLunOperability,
       "cfprApStorageLocalLunPresence": cfprApStorageLocalLunPresence,
       "cfprApStorageLocalLunRevision": cfprApStorageLocalLunRevision,
       "cfprApStorageLocalLunSerial": cfprApStorageLocalLunSerial,
       "cfprApStorageLocalLunSize": cfprApStorageLocalLunSize,
       "cfprApStorageLocalLunType": cfprApStorageLocalLunType,
       "cfprApStorageLocalLunVendor": cfprApStorageLocalLunVendor,
       "cfprApStorageLunDiskTable": cfprApStorageLunDiskTable,
       "cfprApStorageLunDiskEntry": cfprApStorageLunDiskEntry,
       "cfprApStorageLunDiskInstanceId": cfprApStorageLunDiskInstanceId,
       "cfprApStorageLunDiskDn": cfprApStorageLunDiskDn,
       "cfprApStorageLunDiskRn": cfprApStorageLunDiskRn,
       "cfprApStorageLunDiskId": cfprApStorageLunDiskId,
       "cfprApStorageMezzFlashLifeTable": cfprApStorageMezzFlashLifeTable,
       "cfprApStorageMezzFlashLifeEntry": cfprApStorageMezzFlashLifeEntry,
       "cfprApStorageMezzFlashLifeInstanceId": cfprApStorageMezzFlashLifeInstanceId,
       "cfprApStorageMezzFlashLifeDn": cfprApStorageMezzFlashLifeDn,
       "cfprApStorageMezzFlashLifeRn": cfprApStorageMezzFlashLifeRn,
       "cfprApStorageMezzFlashLifeBlockSize": cfprApStorageMezzFlashLifeBlockSize,
       "cfprApStorageMezzFlashLifeConnectionProtocol": cfprApStorageMezzFlashLifeConnectionProtocol,
       "cfprApStorageMezzFlashLifeFlashPercentage": cfprApStorageMezzFlashLifeFlashPercentage,
       "cfprApStorageMezzFlashLifeFlashStatus": cfprApStorageMezzFlashLifeFlashStatus,
       "cfprApStorageMezzFlashLifeId": cfprApStorageMezzFlashLifeId,
       "cfprApStorageMezzFlashLifeModel": cfprApStorageMezzFlashLifeModel,
       "cfprApStorageMezzFlashLifeNumberOfBlocks": cfprApStorageMezzFlashLifeNumberOfBlocks,
       "cfprApStorageMezzFlashLifeOperQualifierReason": cfprApStorageMezzFlashLifeOperQualifierReason,
       "cfprApStorageMezzFlashLifeOperability": cfprApStorageMezzFlashLifeOperability,
       "cfprApStorageMezzFlashLifePresence": cfprApStorageMezzFlashLifePresence,
       "cfprApStorageMezzFlashLifeRevision": cfprApStorageMezzFlashLifeRevision,
       "cfprApStorageMezzFlashLifeSerial": cfprApStorageMezzFlashLifeSerial,
       "cfprApStorageMezzFlashLifeSize": cfprApStorageMezzFlashLifeSize,
       "cfprApStorageMezzFlashLifeVendor": cfprApStorageMezzFlashLifeVendor,
       "cfprApStorageNodeEpTable": cfprApStorageNodeEpTable,
       "cfprApStorageNodeEpEntry": cfprApStorageNodeEpEntry,
       "cfprApStorageNodeEpInstanceId": cfprApStorageNodeEpInstanceId,
       "cfprApStorageNodeEpDn": cfprApStorageNodeEpDn,
       "cfprApStorageNodeEpRn": cfprApStorageNodeEpRn,
       "cfprApStorageNodeEpEpDn": cfprApStorageNodeEpEpDn,
       "cfprApStorageNodeEpId": cfprApStorageNodeEpId,
       "cfprApStorageOperationTable": cfprApStorageOperationTable,
       "cfprApStorageOperationEntry": cfprApStorageOperationEntry,
       "cfprApStorageOperationInstanceId": cfprApStorageOperationInstanceId,
       "cfprApStorageOperationDn": cfprApStorageOperationDn,
       "cfprApStorageOperationRn": cfprApStorageOperationRn,
       "cfprApStorageOperationEndTime": cfprApStorageOperationEndTime,
       "cfprApStorageOperationName": cfprApStorageOperationName,
       "cfprApStorageOperationOperState": cfprApStorageOperationOperState,
       "cfprApStorageOperationProgress": cfprApStorageOperationProgress,
       "cfprApStorageOperationStartTime": cfprApStorageOperationStartTime,
       "cfprApStorageOperationStatusDescr": cfprApStorageOperationStatusDescr,
       "cfprApStorageQualTable": cfprApStorageQualTable,
       "cfprApStorageQualEntry": cfprApStorageQualEntry,
       "cfprApStorageQualInstanceId": cfprApStorageQualInstanceId,
       "cfprApStorageQualDn": cfprApStorageQualDn,
       "cfprApStorageQualRn": cfprApStorageQualRn,
       "cfprApStorageQualBlockSize": cfprApStorageQualBlockSize,
       "cfprApStorageQualDiskless": cfprApStorageQualDiskless,
       "cfprApStorageQualMaxCap": cfprApStorageQualMaxCap,
       "cfprApStorageQualMinCap": cfprApStorageQualMinCap,
       "cfprApStorageQualNumberOfBlocks": cfprApStorageQualNumberOfBlocks,
       "cfprApStorageQualNumberOfFlexFlashCards": cfprApStorageQualNumberOfFlexFlashCards,
       "cfprApStorageQualPerDiskCap": cfprApStorageQualPerDiskCap,
       "cfprApStorageQualUnits": cfprApStorageQualUnits,
       "cfprApStorageRaidBatteryTable": cfprApStorageRaidBatteryTable,
       "cfprApStorageRaidBatteryEntry": cfprApStorageRaidBatteryEntry,
       "cfprApStorageRaidBatteryInstanceId": cfprApStorageRaidBatteryInstanceId,
       "cfprApStorageRaidBatteryDn": cfprApStorageRaidBatteryDn,
       "cfprApStorageRaidBatteryRn": cfprApStorageRaidBatteryRn,
       "cfprApStorageRaidBatteryBatteryType": cfprApStorageRaidBatteryBatteryType,
       "cfprApStorageRaidBatteryBbuStatus": cfprApStorageRaidBatteryBbuStatus,
       "cfprApStorageRaidBatteryBlockSize": cfprApStorageRaidBatteryBlockSize,
       "cfprApStorageRaidBatteryCapacityPercentage": cfprApStorageRaidBatteryCapacityPercentage,
       "cfprApStorageRaidBatteryConnectionProtocol": cfprApStorageRaidBatteryConnectionProtocol,
       "cfprApStorageRaidBatteryId": cfprApStorageRaidBatteryId,
       "cfprApStorageRaidBatteryLc": cfprApStorageRaidBatteryLc,
       "cfprApStorageRaidBatteryLearnCycleRequested": cfprApStorageRaidBatteryLearnCycleRequested,
       "cfprApStorageRaidBatteryLearnMode": cfprApStorageRaidBatteryLearnMode,
       "cfprApStorageRaidBatteryModel": cfprApStorageRaidBatteryModel,
       "cfprApStorageRaidBatteryNextLearnCycleTs": cfprApStorageRaidBatteryNextLearnCycleTs,
       "cfprApStorageRaidBatteryNumberOfBlocks": cfprApStorageRaidBatteryNumberOfBlocks,
       "cfprApStorageRaidBatteryOperQualifierReason": cfprApStorageRaidBatteryOperQualifierReason,
       "cfprApStorageRaidBatteryOperability": cfprApStorageRaidBatteryOperability,
       "cfprApStorageRaidBatteryOperabilityQualifier": cfprApStorageRaidBatteryOperabilityQualifier,
       "cfprApStorageRaidBatteryOperabilityQualifierReason": cfprApStorageRaidBatteryOperabilityQualifierReason,
       "cfprApStorageRaidBatteryPresence": cfprApStorageRaidBatteryPresence,
       "cfprApStorageRaidBatteryRevision": cfprApStorageRaidBatteryRevision,
       "cfprApStorageRaidBatterySerial": cfprApStorageRaidBatterySerial,
       "cfprApStorageRaidBatterySize": cfprApStorageRaidBatterySize,
       "cfprApStorageRaidBatteryTemperature": cfprApStorageRaidBatteryTemperature,
       "cfprApStorageRaidBatteryVendor": cfprApStorageRaidBatteryVendor,
       "cfprApStorageSystemTable": cfprApStorageSystemTable,
       "cfprApStorageSystemEntry": cfprApStorageSystemEntry,
       "cfprApStorageSystemInstanceId": cfprApStorageSystemInstanceId,
       "cfprApStorageSystemDn": cfprApStorageSystemDn,
       "cfprApStorageSystemRn": cfprApStorageSystemRn,
       "cfprApStorageSystemFsmDescr": cfprApStorageSystemFsmDescr,
       "cfprApStorageSystemFsmPrev": cfprApStorageSystemFsmPrev,
       "cfprApStorageSystemFsmProgr": cfprApStorageSystemFsmProgr,
       "cfprApStorageSystemFsmRmtInvErrCode": cfprApStorageSystemFsmRmtInvErrCode,
       "cfprApStorageSystemFsmRmtInvErrDescr": cfprApStorageSystemFsmRmtInvErrDescr,
       "cfprApStorageSystemFsmRmtInvRslt": cfprApStorageSystemFsmRmtInvRslt,
       "cfprApStorageSystemFsmStageDescr": cfprApStorageSystemFsmStageDescr,
       "cfprApStorageSystemFsmStamp": cfprApStorageSystemFsmStamp,
       "cfprApStorageSystemFsmStatus": cfprApStorageSystemFsmStatus,
       "cfprApStorageSystemFsmTry": cfprApStorageSystemFsmTry,
       "cfprApStorageSystemId": cfprApStorageSystemId,
       "cfprApStorageSystemName": cfprApStorageSystemName,
       "cfprApStorageSystemFsmTable": cfprApStorageSystemFsmTable,
       "cfprApStorageSystemFsmEntry": cfprApStorageSystemFsmEntry,
       "cfprApStorageSystemFsmInstanceId": cfprApStorageSystemFsmInstanceId,
       "cfprApStorageSystemFsmDn": cfprApStorageSystemFsmDn,
       "cfprApStorageSystemFsmRn": cfprApStorageSystemFsmRn,
       "cfprApStorageSystemFsmCompletionTime": cfprApStorageSystemFsmCompletionTime,
       "cfprApStorageSystemFsmCurrentFsm": cfprApStorageSystemFsmCurrentFsm,
       "cfprApStorageSystemFsmDescrData": cfprApStorageSystemFsmDescrData,
       "cfprApStorageSystemFsmFsmStatus": cfprApStorageSystemFsmFsmStatus,
       "cfprApStorageSystemFsmProgress": cfprApStorageSystemFsmProgress,
       "cfprApStorageSystemFsmRmtErrCode": cfprApStorageSystemFsmRmtErrCode,
       "cfprApStorageSystemFsmRmtErrDescr": cfprApStorageSystemFsmRmtErrDescr,
       "cfprApStorageSystemFsmRmtRslt": cfprApStorageSystemFsmRmtRslt,
       "cfprApStorageSystemFsmStageTable": cfprApStorageSystemFsmStageTable,
       "cfprApStorageSystemFsmStageEntry": cfprApStorageSystemFsmStageEntry,
       "cfprApStorageSystemFsmStageInstanceId": cfprApStorageSystemFsmStageInstanceId,
       "cfprApStorageSystemFsmStageDn": cfprApStorageSystemFsmStageDn,
       "cfprApStorageSystemFsmStageRn": cfprApStorageSystemFsmStageRn,
       "cfprApStorageSystemFsmStageDescrData": cfprApStorageSystemFsmStageDescrData,
       "cfprApStorageSystemFsmStageLastUpdateTime": cfprApStorageSystemFsmStageLastUpdateTime,
       "cfprApStorageSystemFsmStageName": cfprApStorageSystemFsmStageName,
       "cfprApStorageSystemFsmStageOrder": cfprApStorageSystemFsmStageOrder,
       "cfprApStorageSystemFsmStageRetry": cfprApStorageSystemFsmStageRetry,
       "cfprApStorageSystemFsmStageStageStatus": cfprApStorageSystemFsmStageStageStatus,
       "cfprApStorageSystemFsmTaskTable": cfprApStorageSystemFsmTaskTable,
       "cfprApStorageSystemFsmTaskEntry": cfprApStorageSystemFsmTaskEntry,
       "cfprApStorageSystemFsmTaskInstanceId": cfprApStorageSystemFsmTaskInstanceId,
       "cfprApStorageSystemFsmTaskDn": cfprApStorageSystemFsmTaskDn,
       "cfprApStorageSystemFsmTaskRn": cfprApStorageSystemFsmTaskRn,
       "cfprApStorageSystemFsmTaskCompletion": cfprApStorageSystemFsmTaskCompletion,
       "cfprApStorageSystemFsmTaskFlags": cfprApStorageSystemFsmTaskFlags,
       "cfprApStorageSystemFsmTaskItem": cfprApStorageSystemFsmTaskItem,
       "cfprApStorageSystemFsmTaskSeqId": cfprApStorageSystemFsmTaskSeqId,
       "cfprApStorageTransportableFlashModuleTable": cfprApStorageTransportableFlashModuleTable,
       "cfprApStorageTransportableFlashModuleEntry": cfprApStorageTransportableFlashModuleEntry,
       "cfprApStorageTransportableFlashModuleInstanceId": cfprApStorageTransportableFlashModuleInstanceId,
       "cfprApStorageTransportableFlashModuleDn": cfprApStorageTransportableFlashModuleDn,
       "cfprApStorageTransportableFlashModuleRn": cfprApStorageTransportableFlashModuleRn,
       "cfprApStorageTransportableFlashModuleBlockSize": cfprApStorageTransportableFlashModuleBlockSize,
       "cfprApStorageTransportableFlashModuleConnectionProtocol": cfprApStorageTransportableFlashModuleConnectionProtocol,
       "cfprApStorageTransportableFlashModuleId": cfprApStorageTransportableFlashModuleId,
       "cfprApStorageTransportableFlashModuleModel": cfprApStorageTransportableFlashModuleModel,
       "cfprApStorageTransportableFlashModuleNumberOfBlocks": cfprApStorageTransportableFlashModuleNumberOfBlocks,
       "cfprApStorageTransportableFlashModuleOperQualifierReason": cfprApStorageTransportableFlashModuleOperQualifierReason,
       "cfprApStorageTransportableFlashModuleOperability": cfprApStorageTransportableFlashModuleOperability,
       "cfprApStorageTransportableFlashModulePresence": cfprApStorageTransportableFlashModulePresence,
       "cfprApStorageTransportableFlashModuleRevision": cfprApStorageTransportableFlashModuleRevision,
       "cfprApStorageTransportableFlashModuleSerial": cfprApStorageTransportableFlashModuleSerial,
       "cfprApStorageTransportableFlashModuleSize": cfprApStorageTransportableFlashModuleSize,
       "cfprApStorageTransportableFlashModuleVendor": cfprApStorageTransportableFlashModuleVendor,
       "cfprApStorageVirtualDriveTable": cfprApStorageVirtualDriveTable,
       "cfprApStorageVirtualDriveEntry": cfprApStorageVirtualDriveEntry,
       "cfprApStorageVirtualDriveInstanceId": cfprApStorageVirtualDriveInstanceId,
       "cfprApStorageVirtualDriveDn": cfprApStorageVirtualDriveDn,
       "cfprApStorageVirtualDriveRn": cfprApStorageVirtualDriveRn,
       "cfprApStorageVirtualDriveAccessPolicy": cfprApStorageVirtualDriveAccessPolicy,
       "cfprApStorageVirtualDriveActualWriteCachePolicy": cfprApStorageVirtualDriveActualWriteCachePolicy,
       "cfprApStorageVirtualDriveBlockSize": cfprApStorageVirtualDriveBlockSize,
       "cfprApStorageVirtualDriveBootable": cfprApStorageVirtualDriveBootable,
       "cfprApStorageVirtualDriveConfiguredWriteCachePolicy": cfprApStorageVirtualDriveConfiguredWriteCachePolicy,
       "cfprApStorageVirtualDriveConnectionProtocol": cfprApStorageVirtualDriveConnectionProtocol,
       "cfprApStorageVirtualDriveDriveCache": cfprApStorageVirtualDriveDriveCache,
       "cfprApStorageVirtualDriveDriveState": cfprApStorageVirtualDriveDriveState,
       "cfprApStorageVirtualDriveId": cfprApStorageVirtualDriveId,
       "cfprApStorageVirtualDriveIoPolicy": cfprApStorageVirtualDriveIoPolicy,
       "cfprApStorageVirtualDriveLc": cfprApStorageVirtualDriveLc,
       "cfprApStorageVirtualDriveModel": cfprApStorageVirtualDriveModel,
       "cfprApStorageVirtualDriveNumberOfBlocks": cfprApStorageVirtualDriveNumberOfBlocks,
       "cfprApStorageVirtualDriveOperQualifierReason": cfprApStorageVirtualDriveOperQualifierReason,
       "cfprApStorageVirtualDriveOperability": cfprApStorageVirtualDriveOperability,
       "cfprApStorageVirtualDrivePresence": cfprApStorageVirtualDrivePresence,
       "cfprApStorageVirtualDriveReadPolicy": cfprApStorageVirtualDriveReadPolicy,
       "cfprApStorageVirtualDriveRevision": cfprApStorageVirtualDriveRevision,
       "cfprApStorageVirtualDriveSerial": cfprApStorageVirtualDriveSerial,
       "cfprApStorageVirtualDriveSize": cfprApStorageVirtualDriveSize,
       "cfprApStorageVirtualDriveStripSize": cfprApStorageVirtualDriveStripSize,
       "cfprApStorageVirtualDriveType": cfprApStorageVirtualDriveType,
       "cfprApStorageVirtualDriveVendor": cfprApStorageVirtualDriveVendor,
       "cfprApStorageVsanRefTable": cfprApStorageVsanRefTable,
       "cfprApStorageVsanRefEntry": cfprApStorageVsanRefEntry,
       "cfprApStorageVsanRefInstanceId": cfprApStorageVsanRefInstanceId,
       "cfprApStorageVsanRefDn": cfprApStorageVsanRefDn,
       "cfprApStorageVsanRefRn": cfprApStorageVsanRefRn,
       "cfprApStorageVsanRefConfigQualifier": cfprApStorageVsanRefConfigQualifier,
       "cfprApStorageVsanRefName": cfprApStorageVsanRefName,
       "cfprApStorageVsanRefOperVnetDn": cfprApStorageVsanRefOperVnetDn,
       "cfprApStorageVsanRefOperVnetName": cfprApStorageVsanRefOperVnetName,
       "cfprApStorageVsanRefSwitchId": cfprApStorageVsanRefSwitchId,
       "cfprApStorageVsanRefVnet": cfprApStorageVsanRefVnet,
       "cfprApStorageVsanRefZoningState": cfprApStorageVsanRefZoningState}
)
