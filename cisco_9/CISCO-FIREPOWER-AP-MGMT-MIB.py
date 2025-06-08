# SNMP MIB module (CISCO-FIREPOWER-AP-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-MGMT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:14 2025
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

(CfprApCommClientAdminState,
 CfprApConditionRemoteInvRslt,
 CfprApEtherSatelliteConnectionDisc,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApIpProtocol,
 CfprApMgmtAccess,
 CfprApMgmtAdminState,
 CfprApMgmtBackupFsmCurrentFsm,
 CfprApMgmtBackupFsmStageName,
 CfprApMgmtBackupFsmTaskItem,
 CfprApMgmtBackupInterval,
 CfprApMgmtBackupIssue,
 CfprApMgmtBackupJob,
 CfprApMgmtBackupPolicyFsmCurrentFsm,
 CfprApMgmtBackupPolicyFsmStageName,
 CfprApMgmtBackupPostAction,
 CfprApMgmtBackupProto,
 CfprApMgmtBackupStatus,
 CfprApMgmtBackupType,
 CfprApMgmtCfgExportPolicyFsmCurrentFsm,
 CfprApMgmtCfgExportPolicyFsmStageName,
 CfprApMgmtCimcSecureBootAdminState,
 CfprApMgmtConfigState,
 CfprApMgmtConnectionState,
 CfprApMgmtControllerFsmCurrentFsm,
 CfprApMgmtControllerFsmStageName,
 CfprApMgmtControllerFsmTaskFlags,
 CfprApMgmtControllerFsmTaskItem,
 CfprApMgmtDimmBlacklistingOperState,
 CfprApMgmtEntityChassisDeviceIoState1,
 CfprApMgmtEntityChassisDeviceIoState2,
 CfprApMgmtEntityChassisDeviceIoState3,
 CfprApMgmtEntityHaFailureReason,
 CfprApMgmtEntityHaReadiness,
 CfprApMgmtEntityLeadership,
 CfprApMgmtEntityMgmtServicesState,
 CfprApMgmtEntityProblems,
 CfprApMgmtEntityState,
 CfprApMgmtEntityUmbilicalState,
 CfprApMgmtExportPolicyAdminState,
 CfprApMgmtExportPolicyFsmCurrentFsm,
 CfprApMgmtExportPolicyFsmStageName,
 CfprApMgmtExportPolicyFsmTaskItem,
 CfprApMgmtExportPolicyProto,
 CfprApMgmtIPv6IfAddrFsmCurrentFsm,
 CfprApMgmtIPv6IfAddrFsmStageName,
 CfprApMgmtIPv6IfAddrFsmTaskItem,
 CfprApMgmtIfFsmCurrentFsm,
 CfprApMgmtIfFsmStageName,
 CfprApMgmtIfFsmTaskItem,
 CfprApMgmtImportAction,
 CfprApMgmtImportStatus,
 CfprApMgmtImporterFsmCurrentFsm,
 CfprApMgmtImporterFsmStageName,
 CfprApMgmtImporterFsmTaskItem,
 CfprApMgmtImporterPostAction,
 CfprApMgmtImporterProto,
 CfprApMgmtIntAuthPolicyMethod,
 CfprApMgmtMode,
 CfprApMgmtOperState,
 CfprApMgmtPmonEntryState,
 CfprApMgmtSecureBootOperState,
 CfprApMgmtSource,
 CfprApMgmtStateQual,
 CfprApMgmtStorageSubsystemState,
 CfprApMgmtSubject,
 CfprApNetworkConnectionType,
 CfprApNetworkLocale,
 CfprApNetworkPhysEpIfType,
 CfprApNetworkPortRole,
 CfprApNetworkSwitchId,
 CfprApNetworkTransport,
 CfprApPolicyPolicyOwner,
 CfprApTrigAdminState,
 CfprApTrigTrigOperState,
 CfprApVnicExternalMgmtIPMode) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApCommClientAdminState",
    "CfprApConditionRemoteInvRslt",
    "CfprApEtherSatelliteConnectionDisc",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApIpProtocol",
    "CfprApMgmtAccess",
    "CfprApMgmtAdminState",
    "CfprApMgmtBackupFsmCurrentFsm",
    "CfprApMgmtBackupFsmStageName",
    "CfprApMgmtBackupFsmTaskItem",
    "CfprApMgmtBackupInterval",
    "CfprApMgmtBackupIssue",
    "CfprApMgmtBackupJob",
    "CfprApMgmtBackupPolicyFsmCurrentFsm",
    "CfprApMgmtBackupPolicyFsmStageName",
    "CfprApMgmtBackupPostAction",
    "CfprApMgmtBackupProto",
    "CfprApMgmtBackupStatus",
    "CfprApMgmtBackupType",
    "CfprApMgmtCfgExportPolicyFsmCurrentFsm",
    "CfprApMgmtCfgExportPolicyFsmStageName",
    "CfprApMgmtCimcSecureBootAdminState",
    "CfprApMgmtConfigState",
    "CfprApMgmtConnectionState",
    "CfprApMgmtControllerFsmCurrentFsm",
    "CfprApMgmtControllerFsmStageName",
    "CfprApMgmtControllerFsmTaskFlags",
    "CfprApMgmtControllerFsmTaskItem",
    "CfprApMgmtDimmBlacklistingOperState",
    "CfprApMgmtEntityChassisDeviceIoState1",
    "CfprApMgmtEntityChassisDeviceIoState2",
    "CfprApMgmtEntityChassisDeviceIoState3",
    "CfprApMgmtEntityHaFailureReason",
    "CfprApMgmtEntityHaReadiness",
    "CfprApMgmtEntityLeadership",
    "CfprApMgmtEntityMgmtServicesState",
    "CfprApMgmtEntityProblems",
    "CfprApMgmtEntityState",
    "CfprApMgmtEntityUmbilicalState",
    "CfprApMgmtExportPolicyAdminState",
    "CfprApMgmtExportPolicyFsmCurrentFsm",
    "CfprApMgmtExportPolicyFsmStageName",
    "CfprApMgmtExportPolicyFsmTaskItem",
    "CfprApMgmtExportPolicyProto",
    "CfprApMgmtIPv6IfAddrFsmCurrentFsm",
    "CfprApMgmtIPv6IfAddrFsmStageName",
    "CfprApMgmtIPv6IfAddrFsmTaskItem",
    "CfprApMgmtIfFsmCurrentFsm",
    "CfprApMgmtIfFsmStageName",
    "CfprApMgmtIfFsmTaskItem",
    "CfprApMgmtImportAction",
    "CfprApMgmtImportStatus",
    "CfprApMgmtImporterFsmCurrentFsm",
    "CfprApMgmtImporterFsmStageName",
    "CfprApMgmtImporterFsmTaskItem",
    "CfprApMgmtImporterPostAction",
    "CfprApMgmtImporterProto",
    "CfprApMgmtIntAuthPolicyMethod",
    "CfprApMgmtMode",
    "CfprApMgmtOperState",
    "CfprApMgmtPmonEntryState",
    "CfprApMgmtSecureBootOperState",
    "CfprApMgmtSource",
    "CfprApMgmtStateQual",
    "CfprApMgmtStorageSubsystemState",
    "CfprApMgmtSubject",
    "CfprApNetworkConnectionType",
    "CfprApNetworkLocale",
    "CfprApNetworkPhysEpIfType",
    "CfprApNetworkPortRole",
    "CfprApNetworkSwitchId",
    "CfprApNetworkTransport",
    "CfprApPolicyPolicyOwner",
    "CfprApTrigAdminState",
    "CfprApTrigTrigOperState",
    "CfprApVnicExternalMgmtIPMode")

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

cfprApMgmtObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApMgmtAccessPolicyTable_Object = MibTable
cfprApMgmtAccessPolicyTable = _CfprApMgmtAccessPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 1)
)
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyTable.setStatus("current")
_CfprApMgmtAccessPolicyEntry_Object = MibTableRow
cfprApMgmtAccessPolicyEntry = _CfprApMgmtAccessPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 1, 1)
)
cfprApMgmtAccessPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtAccessPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyEntry.setStatus("current")
_CfprApMgmtAccessPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtAccessPolicyInstanceId_Object = MibTableColumn
cfprApMgmtAccessPolicyInstanceId = _CfprApMgmtAccessPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 1, 1, 1),
    _CfprApMgmtAccessPolicyInstanceId_Type()
)
cfprApMgmtAccessPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyInstanceId.setStatus("current")
_CfprApMgmtAccessPolicyDn_Type = CfprApManagedObjectDn
_CfprApMgmtAccessPolicyDn_Object = MibTableColumn
cfprApMgmtAccessPolicyDn = _CfprApMgmtAccessPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 1, 1, 2),
    _CfprApMgmtAccessPolicyDn_Type()
)
cfprApMgmtAccessPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyDn.setStatus("current")
_CfprApMgmtAccessPolicyRn_Type = SnmpAdminString
_CfprApMgmtAccessPolicyRn_Object = MibTableColumn
cfprApMgmtAccessPolicyRn = _CfprApMgmtAccessPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 1, 1, 3),
    _CfprApMgmtAccessPolicyRn_Type()
)
cfprApMgmtAccessPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyRn.setStatus("current")
_CfprApMgmtAccessPolicyItemTable_Object = MibTable
cfprApMgmtAccessPolicyItemTable = _CfprApMgmtAccessPolicyItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 2)
)
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyItemTable.setStatus("current")
_CfprApMgmtAccessPolicyItemEntry_Object = MibTableRow
cfprApMgmtAccessPolicyItemEntry = _CfprApMgmtAccessPolicyItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 2, 1)
)
cfprApMgmtAccessPolicyItemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtAccessPolicyItemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyItemEntry.setStatus("current")
_CfprApMgmtAccessPolicyItemInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtAccessPolicyItemInstanceId_Object = MibTableColumn
cfprApMgmtAccessPolicyItemInstanceId = _CfprApMgmtAccessPolicyItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 2, 1, 1),
    _CfprApMgmtAccessPolicyItemInstanceId_Type()
)
cfprApMgmtAccessPolicyItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyItemInstanceId.setStatus("current")
_CfprApMgmtAccessPolicyItemDn_Type = CfprApManagedObjectDn
_CfprApMgmtAccessPolicyItemDn_Object = MibTableColumn
cfprApMgmtAccessPolicyItemDn = _CfprApMgmtAccessPolicyItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 2, 1, 2),
    _CfprApMgmtAccessPolicyItemDn_Type()
)
cfprApMgmtAccessPolicyItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyItemDn.setStatus("current")
_CfprApMgmtAccessPolicyItemRn_Type = SnmpAdminString
_CfprApMgmtAccessPolicyItemRn_Object = MibTableColumn
cfprApMgmtAccessPolicyItemRn = _CfprApMgmtAccessPolicyItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 2, 1, 3),
    _CfprApMgmtAccessPolicyItemRn_Type()
)
cfprApMgmtAccessPolicyItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyItemRn.setStatus("current")
_CfprApMgmtAccessPolicyItemDescr_Type = SnmpAdminString
_CfprApMgmtAccessPolicyItemDescr_Object = MibTableColumn
cfprApMgmtAccessPolicyItemDescr = _CfprApMgmtAccessPolicyItemDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 2, 1, 4),
    _CfprApMgmtAccessPolicyItemDescr_Type()
)
cfprApMgmtAccessPolicyItemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyItemDescr.setStatus("current")
_CfprApMgmtAccessPolicyItemIntId_Type = SnmpAdminString
_CfprApMgmtAccessPolicyItemIntId_Object = MibTableColumn
cfprApMgmtAccessPolicyItemIntId = _CfprApMgmtAccessPolicyItemIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 2, 1, 5),
    _CfprApMgmtAccessPolicyItemIntId_Type()
)
cfprApMgmtAccessPolicyItemIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyItemIntId.setStatus("current")
_CfprApMgmtAccessPolicyItemIpPoolName_Type = SnmpAdminString
_CfprApMgmtAccessPolicyItemIpPoolName_Object = MibTableColumn
cfprApMgmtAccessPolicyItemIpPoolName = _CfprApMgmtAccessPolicyItemIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 2, 1, 6),
    _CfprApMgmtAccessPolicyItemIpPoolName_Type()
)
cfprApMgmtAccessPolicyItemIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyItemIpPoolName.setStatus("current")
_CfprApMgmtAccessPolicyItemName_Type = SnmpAdminString
_CfprApMgmtAccessPolicyItemName_Object = MibTableColumn
cfprApMgmtAccessPolicyItemName = _CfprApMgmtAccessPolicyItemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 2, 1, 7),
    _CfprApMgmtAccessPolicyItemName_Type()
)
cfprApMgmtAccessPolicyItemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyItemName.setStatus("current")
_CfprApMgmtAccessPolicyItemPolicyLevel_Type = Gauge32
_CfprApMgmtAccessPolicyItemPolicyLevel_Object = MibTableColumn
cfprApMgmtAccessPolicyItemPolicyLevel = _CfprApMgmtAccessPolicyItemPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 2, 1, 8),
    _CfprApMgmtAccessPolicyItemPolicyLevel_Type()
)
cfprApMgmtAccessPolicyItemPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyItemPolicyLevel.setStatus("current")
_CfprApMgmtAccessPolicyItemPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApMgmtAccessPolicyItemPolicyOwner_Object = MibTableColumn
cfprApMgmtAccessPolicyItemPolicyOwner = _CfprApMgmtAccessPolicyItemPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 2, 1, 9),
    _CfprApMgmtAccessPolicyItemPolicyOwner_Type()
)
cfprApMgmtAccessPolicyItemPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyItemPolicyOwner.setStatus("current")
_CfprApMgmtAccessPolicyItemSubject_Type = CfprApMgmtSubject
_CfprApMgmtAccessPolicyItemSubject_Object = MibTableColumn
cfprApMgmtAccessPolicyItemSubject = _CfprApMgmtAccessPolicyItemSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 2, 1, 10),
    _CfprApMgmtAccessPolicyItemSubject_Type()
)
cfprApMgmtAccessPolicyItemSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPolicyItemSubject.setStatus("current")
_CfprApMgmtAccessPortTable_Object = MibTable
cfprApMgmtAccessPortTable = _CfprApMgmtAccessPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 3)
)
if mibBuilder.loadTexts:
    cfprApMgmtAccessPortTable.setStatus("current")
_CfprApMgmtAccessPortEntry_Object = MibTableRow
cfprApMgmtAccessPortEntry = _CfprApMgmtAccessPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 3, 1)
)
cfprApMgmtAccessPortEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtAccessPortInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtAccessPortEntry.setStatus("current")
_CfprApMgmtAccessPortInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtAccessPortInstanceId_Object = MibTableColumn
cfprApMgmtAccessPortInstanceId = _CfprApMgmtAccessPortInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 3, 1, 1),
    _CfprApMgmtAccessPortInstanceId_Type()
)
cfprApMgmtAccessPortInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPortInstanceId.setStatus("current")
_CfprApMgmtAccessPortDn_Type = CfprApManagedObjectDn
_CfprApMgmtAccessPortDn_Object = MibTableColumn
cfprApMgmtAccessPortDn = _CfprApMgmtAccessPortDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 3, 1, 2),
    _CfprApMgmtAccessPortDn_Type()
)
cfprApMgmtAccessPortDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPortDn.setStatus("current")
_CfprApMgmtAccessPortRn_Type = SnmpAdminString
_CfprApMgmtAccessPortRn_Object = MibTableColumn
cfprApMgmtAccessPortRn = _CfprApMgmtAccessPortRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 3, 1, 3),
    _CfprApMgmtAccessPortRn_Type()
)
cfprApMgmtAccessPortRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPortRn.setStatus("current")
_CfprApMgmtAccessPortPort_Type = Gauge32
_CfprApMgmtAccessPortPort_Object = MibTableColumn
cfprApMgmtAccessPortPort = _CfprApMgmtAccessPortPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 3, 1, 4),
    _CfprApMgmtAccessPortPort_Type()
)
cfprApMgmtAccessPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPortPort.setStatus("current")
_CfprApMgmtAccessPortProtocol_Type = CfprApIpProtocol
_CfprApMgmtAccessPortProtocol_Object = MibTableColumn
cfprApMgmtAccessPortProtocol = _CfprApMgmtAccessPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 3, 1, 5),
    _CfprApMgmtAccessPortProtocol_Type()
)
cfprApMgmtAccessPortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtAccessPortProtocol.setStatus("current")
_CfprApMgmtBackupTable_Object = MibTable
cfprApMgmtBackupTable = _CfprApMgmtBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4)
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupTable.setStatus("current")
_CfprApMgmtBackupEntry_Object = MibTableRow
cfprApMgmtBackupEntry = _CfprApMgmtBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1)
)
cfprApMgmtBackupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtBackupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupEntry.setStatus("current")
_CfprApMgmtBackupInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtBackupInstanceId_Object = MibTableColumn
cfprApMgmtBackupInstanceId = _CfprApMgmtBackupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 1),
    _CfprApMgmtBackupInstanceId_Type()
)
cfprApMgmtBackupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtBackupInstanceId.setStatus("current")
_CfprApMgmtBackupDn_Type = CfprApManagedObjectDn
_CfprApMgmtBackupDn_Object = MibTableColumn
cfprApMgmtBackupDn = _CfprApMgmtBackupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 2),
    _CfprApMgmtBackupDn_Type()
)
cfprApMgmtBackupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupDn.setStatus("current")
_CfprApMgmtBackupRn_Type = SnmpAdminString
_CfprApMgmtBackupRn_Object = MibTableColumn
cfprApMgmtBackupRn = _CfprApMgmtBackupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 3),
    _CfprApMgmtBackupRn_Type()
)
cfprApMgmtBackupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupRn.setStatus("current")
_CfprApMgmtBackupAdminState_Type = CfprApCommClientAdminState
_CfprApMgmtBackupAdminState_Object = MibTableColumn
cfprApMgmtBackupAdminState = _CfprApMgmtBackupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 4),
    _CfprApMgmtBackupAdminState_Type()
)
cfprApMgmtBackupAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupAdminState.setStatus("current")
_CfprApMgmtBackupDescr_Type = SnmpAdminString
_CfprApMgmtBackupDescr_Object = MibTableColumn
cfprApMgmtBackupDescr = _CfprApMgmtBackupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 5),
    _CfprApMgmtBackupDescr_Type()
)
cfprApMgmtBackupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupDescr.setStatus("current")
_CfprApMgmtBackupFsmDescr_Type = SnmpAdminString
_CfprApMgmtBackupFsmDescr_Object = MibTableColumn
cfprApMgmtBackupFsmDescr = _CfprApMgmtBackupFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 6),
    _CfprApMgmtBackupFsmDescr_Type()
)
cfprApMgmtBackupFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmDescr.setStatus("current")
_CfprApMgmtBackupFsmPrev_Type = SnmpAdminString
_CfprApMgmtBackupFsmPrev_Object = MibTableColumn
cfprApMgmtBackupFsmPrev = _CfprApMgmtBackupFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 7),
    _CfprApMgmtBackupFsmPrev_Type()
)
cfprApMgmtBackupFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmPrev.setStatus("current")
_CfprApMgmtBackupFsmProgr_Type = Gauge32
_CfprApMgmtBackupFsmProgr_Object = MibTableColumn
cfprApMgmtBackupFsmProgr = _CfprApMgmtBackupFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 8),
    _CfprApMgmtBackupFsmProgr_Type()
)
cfprApMgmtBackupFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmProgr.setStatus("current")
_CfprApMgmtBackupFsmRmtInvErrCode_Type = Gauge32
_CfprApMgmtBackupFsmRmtInvErrCode_Object = MibTableColumn
cfprApMgmtBackupFsmRmtInvErrCode = _CfprApMgmtBackupFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 9),
    _CfprApMgmtBackupFsmRmtInvErrCode_Type()
)
cfprApMgmtBackupFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmRmtInvErrCode.setStatus("current")
_CfprApMgmtBackupFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApMgmtBackupFsmRmtInvErrDescr_Object = MibTableColumn
cfprApMgmtBackupFsmRmtInvErrDescr = _CfprApMgmtBackupFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 10),
    _CfprApMgmtBackupFsmRmtInvErrDescr_Type()
)
cfprApMgmtBackupFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmRmtInvErrDescr.setStatus("current")
_CfprApMgmtBackupFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtBackupFsmRmtInvRslt_Object = MibTableColumn
cfprApMgmtBackupFsmRmtInvRslt = _CfprApMgmtBackupFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 11),
    _CfprApMgmtBackupFsmRmtInvRslt_Type()
)
cfprApMgmtBackupFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmRmtInvRslt.setStatus("current")
_CfprApMgmtBackupFsmStageDescr_Type = SnmpAdminString
_CfprApMgmtBackupFsmStageDescr_Object = MibTableColumn
cfprApMgmtBackupFsmStageDescr = _CfprApMgmtBackupFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 12),
    _CfprApMgmtBackupFsmStageDescr_Type()
)
cfprApMgmtBackupFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStageDescr.setStatus("current")
_CfprApMgmtBackupFsmStamp_Type = DateAndTime
_CfprApMgmtBackupFsmStamp_Object = MibTableColumn
cfprApMgmtBackupFsmStamp = _CfprApMgmtBackupFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 13),
    _CfprApMgmtBackupFsmStamp_Type()
)
cfprApMgmtBackupFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStamp.setStatus("current")
_CfprApMgmtBackupFsmStatus_Type = SnmpAdminString
_CfprApMgmtBackupFsmStatus_Object = MibTableColumn
cfprApMgmtBackupFsmStatus = _CfprApMgmtBackupFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 14),
    _CfprApMgmtBackupFsmStatus_Type()
)
cfprApMgmtBackupFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStatus.setStatus("current")
_CfprApMgmtBackupFsmTry_Type = Gauge32
_CfprApMgmtBackupFsmTry_Object = MibTableColumn
cfprApMgmtBackupFsmTry = _CfprApMgmtBackupFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 15),
    _CfprApMgmtBackupFsmTry_Type()
)
cfprApMgmtBackupFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmTry.setStatus("current")
_CfprApMgmtBackupHostname_Type = SnmpAdminString
_CfprApMgmtBackupHostname_Object = MibTableColumn
cfprApMgmtBackupHostname = _CfprApMgmtBackupHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 16),
    _CfprApMgmtBackupHostname_Type()
)
cfprApMgmtBackupHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupHostname.setStatus("current")
_CfprApMgmtBackupIntId_Type = SnmpAdminString
_CfprApMgmtBackupIntId_Object = MibTableColumn
cfprApMgmtBackupIntId = _CfprApMgmtBackupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 17),
    _CfprApMgmtBackupIntId_Type()
)
cfprApMgmtBackupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupIntId.setStatus("current")
_CfprApMgmtBackupJob_Type = CfprApMgmtBackupJob
_CfprApMgmtBackupJob_Object = MibTableColumn
cfprApMgmtBackupJob = _CfprApMgmtBackupJob_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 18),
    _CfprApMgmtBackupJob_Type()
)
cfprApMgmtBackupJob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupJob.setStatus("current")
_CfprApMgmtBackupMaxFiles_Type = Gauge32
_CfprApMgmtBackupMaxFiles_Object = MibTableColumn
cfprApMgmtBackupMaxFiles = _CfprApMgmtBackupMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 19),
    _CfprApMgmtBackupMaxFiles_Type()
)
cfprApMgmtBackupMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupMaxFiles.setStatus("current")
_CfprApMgmtBackupName_Type = SnmpAdminString
_CfprApMgmtBackupName_Object = MibTableColumn
cfprApMgmtBackupName = _CfprApMgmtBackupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 20),
    _CfprApMgmtBackupName_Type()
)
cfprApMgmtBackupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupName.setStatus("current")
_CfprApMgmtBackupOperStatus_Type = CfprApMgmtBackupStatus
_CfprApMgmtBackupOperStatus_Object = MibTableColumn
cfprApMgmtBackupOperStatus = _CfprApMgmtBackupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 21),
    _CfprApMgmtBackupOperStatus_Type()
)
cfprApMgmtBackupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupOperStatus.setStatus("current")
_CfprApMgmtBackupOwnerPolicy_Type = SnmpAdminString
_CfprApMgmtBackupOwnerPolicy_Object = MibTableColumn
cfprApMgmtBackupOwnerPolicy = _CfprApMgmtBackupOwnerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 22),
    _CfprApMgmtBackupOwnerPolicy_Type()
)
cfprApMgmtBackupOwnerPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupOwnerPolicy.setStatus("current")
_CfprApMgmtBackupPolicyLevel_Type = Gauge32
_CfprApMgmtBackupPolicyLevel_Object = MibTableColumn
cfprApMgmtBackupPolicyLevel = _CfprApMgmtBackupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 23),
    _CfprApMgmtBackupPolicyLevel_Type()
)
cfprApMgmtBackupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyLevel.setStatus("current")
_CfprApMgmtBackupPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApMgmtBackupPolicyOwner_Object = MibTableColumn
cfprApMgmtBackupPolicyOwner = _CfprApMgmtBackupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 24),
    _CfprApMgmtBackupPolicyOwner_Type()
)
cfprApMgmtBackupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyOwner.setStatus("current")
_CfprApMgmtBackupPort_Type = Gauge32
_CfprApMgmtBackupPort_Object = MibTableColumn
cfprApMgmtBackupPort = _CfprApMgmtBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 25),
    _CfprApMgmtBackupPort_Type()
)
cfprApMgmtBackupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPort.setStatus("current")
_CfprApMgmtBackupPostAction_Type = CfprApMgmtBackupPostAction
_CfprApMgmtBackupPostAction_Object = MibTableColumn
cfprApMgmtBackupPostAction = _CfprApMgmtBackupPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 26),
    _CfprApMgmtBackupPostAction_Type()
)
cfprApMgmtBackupPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPostAction.setStatus("current")
_CfprApMgmtBackupPreservePooledValues_Type = TruthValue
_CfprApMgmtBackupPreservePooledValues_Object = MibTableColumn
cfprApMgmtBackupPreservePooledValues = _CfprApMgmtBackupPreservePooledValues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 27),
    _CfprApMgmtBackupPreservePooledValues_Type()
)
cfprApMgmtBackupPreservePooledValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPreservePooledValues.setStatus("current")
_CfprApMgmtBackupProto_Type = CfprApMgmtBackupProto
_CfprApMgmtBackupProto_Object = MibTableColumn
cfprApMgmtBackupProto = _CfprApMgmtBackupProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 28),
    _CfprApMgmtBackupProto_Type()
)
cfprApMgmtBackupProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupProto.setStatus("current")
_CfprApMgmtBackupPwd_Type = SnmpAdminString
_CfprApMgmtBackupPwd_Object = MibTableColumn
cfprApMgmtBackupPwd = _CfprApMgmtBackupPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 29),
    _CfprApMgmtBackupPwd_Type()
)
cfprApMgmtBackupPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPwd.setStatus("current")
_CfprApMgmtBackupRemoteFile_Type = SnmpAdminString
_CfprApMgmtBackupRemoteFile_Object = MibTableColumn
cfprApMgmtBackupRemoteFile = _CfprApMgmtBackupRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 30),
    _CfprApMgmtBackupRemoteFile_Type()
)
cfprApMgmtBackupRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupRemoteFile.setStatus("current")
_CfprApMgmtBackupType_Type = CfprApMgmtBackupType
_CfprApMgmtBackupType_Object = MibTableColumn
cfprApMgmtBackupType = _CfprApMgmtBackupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 31),
    _CfprApMgmtBackupType_Type()
)
cfprApMgmtBackupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupType.setStatus("current")
_CfprApMgmtBackupUser_Type = SnmpAdminString
_CfprApMgmtBackupUser_Object = MibTableColumn
cfprApMgmtBackupUser = _CfprApMgmtBackupUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 4, 1, 32),
    _CfprApMgmtBackupUser_Type()
)
cfprApMgmtBackupUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupUser.setStatus("current")
_CfprApMgmtBackupExportExtPolicyTable_Object = MibTable
cfprApMgmtBackupExportExtPolicyTable = _CfprApMgmtBackupExportExtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 5)
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupExportExtPolicyTable.setStatus("current")
_CfprApMgmtBackupExportExtPolicyEntry_Object = MibTableRow
cfprApMgmtBackupExportExtPolicyEntry = _CfprApMgmtBackupExportExtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 5, 1)
)
cfprApMgmtBackupExportExtPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtBackupExportExtPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupExportExtPolicyEntry.setStatus("current")
_CfprApMgmtBackupExportExtPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtBackupExportExtPolicyInstanceId_Object = MibTableColumn
cfprApMgmtBackupExportExtPolicyInstanceId = _CfprApMgmtBackupExportExtPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 5, 1, 1),
    _CfprApMgmtBackupExportExtPolicyInstanceId_Type()
)
cfprApMgmtBackupExportExtPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtBackupExportExtPolicyInstanceId.setStatus("current")
_CfprApMgmtBackupExportExtPolicyDn_Type = CfprApManagedObjectDn
_CfprApMgmtBackupExportExtPolicyDn_Object = MibTableColumn
cfprApMgmtBackupExportExtPolicyDn = _CfprApMgmtBackupExportExtPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 5, 1, 2),
    _CfprApMgmtBackupExportExtPolicyDn_Type()
)
cfprApMgmtBackupExportExtPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupExportExtPolicyDn.setStatus("current")
_CfprApMgmtBackupExportExtPolicyRn_Type = SnmpAdminString
_CfprApMgmtBackupExportExtPolicyRn_Object = MibTableColumn
cfprApMgmtBackupExportExtPolicyRn = _CfprApMgmtBackupExportExtPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 5, 1, 3),
    _CfprApMgmtBackupExportExtPolicyRn_Type()
)
cfprApMgmtBackupExportExtPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupExportExtPolicyRn.setStatus("current")
_CfprApMgmtBackupExportExtPolicyAdminState_Type = CfprApMgmtAdminState
_CfprApMgmtBackupExportExtPolicyAdminState_Object = MibTableColumn
cfprApMgmtBackupExportExtPolicyAdminState = _CfprApMgmtBackupExportExtPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 5, 1, 4),
    _CfprApMgmtBackupExportExtPolicyAdminState_Type()
)
cfprApMgmtBackupExportExtPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupExportExtPolicyAdminState.setStatus("current")
_CfprApMgmtBackupExportExtPolicyDescr_Type = SnmpAdminString
_CfprApMgmtBackupExportExtPolicyDescr_Object = MibTableColumn
cfprApMgmtBackupExportExtPolicyDescr = _CfprApMgmtBackupExportExtPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 5, 1, 5),
    _CfprApMgmtBackupExportExtPolicyDescr_Type()
)
cfprApMgmtBackupExportExtPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupExportExtPolicyDescr.setStatus("current")
_CfprApMgmtBackupExportExtPolicyFrequency_Type = Gauge32
_CfprApMgmtBackupExportExtPolicyFrequency_Object = MibTableColumn
cfprApMgmtBackupExportExtPolicyFrequency = _CfprApMgmtBackupExportExtPolicyFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 5, 1, 6),
    _CfprApMgmtBackupExportExtPolicyFrequency_Type()
)
cfprApMgmtBackupExportExtPolicyFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupExportExtPolicyFrequency.setStatus("current")
_CfprApMgmtBackupExportExtPolicyIntId_Type = SnmpAdminString
_CfprApMgmtBackupExportExtPolicyIntId_Object = MibTableColumn
cfprApMgmtBackupExportExtPolicyIntId = _CfprApMgmtBackupExportExtPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 5, 1, 7),
    _CfprApMgmtBackupExportExtPolicyIntId_Type()
)
cfprApMgmtBackupExportExtPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupExportExtPolicyIntId.setStatus("current")
_CfprApMgmtBackupExportExtPolicyName_Type = SnmpAdminString
_CfprApMgmtBackupExportExtPolicyName_Object = MibTableColumn
cfprApMgmtBackupExportExtPolicyName = _CfprApMgmtBackupExportExtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 5, 1, 8),
    _CfprApMgmtBackupExportExtPolicyName_Type()
)
cfprApMgmtBackupExportExtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupExportExtPolicyName.setStatus("current")
_CfprApMgmtBackupExportExtPolicyPolicyLevel_Type = Gauge32
_CfprApMgmtBackupExportExtPolicyPolicyLevel_Object = MibTableColumn
cfprApMgmtBackupExportExtPolicyPolicyLevel = _CfprApMgmtBackupExportExtPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 5, 1, 9),
    _CfprApMgmtBackupExportExtPolicyPolicyLevel_Type()
)
cfprApMgmtBackupExportExtPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupExportExtPolicyPolicyLevel.setStatus("current")
_CfprApMgmtBackupExportExtPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApMgmtBackupExportExtPolicyPolicyOwner_Object = MibTableColumn
cfprApMgmtBackupExportExtPolicyPolicyOwner = _CfprApMgmtBackupExportExtPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 5, 1, 10),
    _CfprApMgmtBackupExportExtPolicyPolicyOwner_Type()
)
cfprApMgmtBackupExportExtPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupExportExtPolicyPolicyOwner.setStatus("current")
_CfprApMgmtBackupFsmTable_Object = MibTable
cfprApMgmtBackupFsmTable = _CfprApMgmtBackupFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6)
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmTable.setStatus("current")
_CfprApMgmtBackupFsmEntry_Object = MibTableRow
cfprApMgmtBackupFsmEntry = _CfprApMgmtBackupFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6, 1)
)
cfprApMgmtBackupFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtBackupFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmEntry.setStatus("current")
_CfprApMgmtBackupFsmInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtBackupFsmInstanceId_Object = MibTableColumn
cfprApMgmtBackupFsmInstanceId = _CfprApMgmtBackupFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6, 1, 1),
    _CfprApMgmtBackupFsmInstanceId_Type()
)
cfprApMgmtBackupFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmInstanceId.setStatus("current")
_CfprApMgmtBackupFsmDn_Type = CfprApManagedObjectDn
_CfprApMgmtBackupFsmDn_Object = MibTableColumn
cfprApMgmtBackupFsmDn = _CfprApMgmtBackupFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6, 1, 2),
    _CfprApMgmtBackupFsmDn_Type()
)
cfprApMgmtBackupFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmDn.setStatus("current")
_CfprApMgmtBackupFsmRn_Type = SnmpAdminString
_CfprApMgmtBackupFsmRn_Object = MibTableColumn
cfprApMgmtBackupFsmRn = _CfprApMgmtBackupFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6, 1, 3),
    _CfprApMgmtBackupFsmRn_Type()
)
cfprApMgmtBackupFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmRn.setStatus("current")
_CfprApMgmtBackupFsmCompletionTime_Type = DateAndTime
_CfprApMgmtBackupFsmCompletionTime_Object = MibTableColumn
cfprApMgmtBackupFsmCompletionTime = _CfprApMgmtBackupFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6, 1, 4),
    _CfprApMgmtBackupFsmCompletionTime_Type()
)
cfprApMgmtBackupFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmCompletionTime.setStatus("current")
_CfprApMgmtBackupFsmCurrentFsm_Type = CfprApMgmtBackupFsmCurrentFsm
_CfprApMgmtBackupFsmCurrentFsm_Object = MibTableColumn
cfprApMgmtBackupFsmCurrentFsm = _CfprApMgmtBackupFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6, 1, 5),
    _CfprApMgmtBackupFsmCurrentFsm_Type()
)
cfprApMgmtBackupFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmCurrentFsm.setStatus("current")
_CfprApMgmtBackupFsmDescrData_Type = SnmpAdminString
_CfprApMgmtBackupFsmDescrData_Object = MibTableColumn
cfprApMgmtBackupFsmDescrData = _CfprApMgmtBackupFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6, 1, 6),
    _CfprApMgmtBackupFsmDescrData_Type()
)
cfprApMgmtBackupFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmDescrData.setStatus("current")
_CfprApMgmtBackupFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtBackupFsmFsmStatus_Object = MibTableColumn
cfprApMgmtBackupFsmFsmStatus = _CfprApMgmtBackupFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6, 1, 7),
    _CfprApMgmtBackupFsmFsmStatus_Type()
)
cfprApMgmtBackupFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmFsmStatus.setStatus("current")
_CfprApMgmtBackupFsmProgress_Type = Gauge32
_CfprApMgmtBackupFsmProgress_Object = MibTableColumn
cfprApMgmtBackupFsmProgress = _CfprApMgmtBackupFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6, 1, 8),
    _CfprApMgmtBackupFsmProgress_Type()
)
cfprApMgmtBackupFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmProgress.setStatus("current")
_CfprApMgmtBackupFsmRmtErrCode_Type = Gauge32
_CfprApMgmtBackupFsmRmtErrCode_Object = MibTableColumn
cfprApMgmtBackupFsmRmtErrCode = _CfprApMgmtBackupFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6, 1, 9),
    _CfprApMgmtBackupFsmRmtErrCode_Type()
)
cfprApMgmtBackupFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmRmtErrCode.setStatus("current")
_CfprApMgmtBackupFsmRmtErrDescr_Type = SnmpAdminString
_CfprApMgmtBackupFsmRmtErrDescr_Object = MibTableColumn
cfprApMgmtBackupFsmRmtErrDescr = _CfprApMgmtBackupFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6, 1, 10),
    _CfprApMgmtBackupFsmRmtErrDescr_Type()
)
cfprApMgmtBackupFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmRmtErrDescr.setStatus("current")
_CfprApMgmtBackupFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtBackupFsmRmtRslt_Object = MibTableColumn
cfprApMgmtBackupFsmRmtRslt = _CfprApMgmtBackupFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 6, 1, 11),
    _CfprApMgmtBackupFsmRmtRslt_Type()
)
cfprApMgmtBackupFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmRmtRslt.setStatus("current")
_CfprApMgmtBackupFsmStageTable_Object = MibTable
cfprApMgmtBackupFsmStageTable = _CfprApMgmtBackupFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 7)
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStageTable.setStatus("current")
_CfprApMgmtBackupFsmStageEntry_Object = MibTableRow
cfprApMgmtBackupFsmStageEntry = _CfprApMgmtBackupFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 7, 1)
)
cfprApMgmtBackupFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtBackupFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStageEntry.setStatus("current")
_CfprApMgmtBackupFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtBackupFsmStageInstanceId_Object = MibTableColumn
cfprApMgmtBackupFsmStageInstanceId = _CfprApMgmtBackupFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 7, 1, 1),
    _CfprApMgmtBackupFsmStageInstanceId_Type()
)
cfprApMgmtBackupFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStageInstanceId.setStatus("current")
_CfprApMgmtBackupFsmStageDn_Type = CfprApManagedObjectDn
_CfprApMgmtBackupFsmStageDn_Object = MibTableColumn
cfprApMgmtBackupFsmStageDn = _CfprApMgmtBackupFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 7, 1, 2),
    _CfprApMgmtBackupFsmStageDn_Type()
)
cfprApMgmtBackupFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStageDn.setStatus("current")
_CfprApMgmtBackupFsmStageRn_Type = SnmpAdminString
_CfprApMgmtBackupFsmStageRn_Object = MibTableColumn
cfprApMgmtBackupFsmStageRn = _CfprApMgmtBackupFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 7, 1, 3),
    _CfprApMgmtBackupFsmStageRn_Type()
)
cfprApMgmtBackupFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStageRn.setStatus("current")
_CfprApMgmtBackupFsmStageDescrData_Type = SnmpAdminString
_CfprApMgmtBackupFsmStageDescrData_Object = MibTableColumn
cfprApMgmtBackupFsmStageDescrData = _CfprApMgmtBackupFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 7, 1, 4),
    _CfprApMgmtBackupFsmStageDescrData_Type()
)
cfprApMgmtBackupFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStageDescrData.setStatus("current")
_CfprApMgmtBackupFsmStageLastUpdateTime_Type = DateAndTime
_CfprApMgmtBackupFsmStageLastUpdateTime_Object = MibTableColumn
cfprApMgmtBackupFsmStageLastUpdateTime = _CfprApMgmtBackupFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 7, 1, 5),
    _CfprApMgmtBackupFsmStageLastUpdateTime_Type()
)
cfprApMgmtBackupFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStageLastUpdateTime.setStatus("current")
_CfprApMgmtBackupFsmStageName_Type = CfprApMgmtBackupFsmStageName
_CfprApMgmtBackupFsmStageName_Object = MibTableColumn
cfprApMgmtBackupFsmStageName = _CfprApMgmtBackupFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 7, 1, 6),
    _CfprApMgmtBackupFsmStageName_Type()
)
cfprApMgmtBackupFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStageName.setStatus("current")
_CfprApMgmtBackupFsmStageOrder_Type = Gauge32
_CfprApMgmtBackupFsmStageOrder_Object = MibTableColumn
cfprApMgmtBackupFsmStageOrder = _CfprApMgmtBackupFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 7, 1, 7),
    _CfprApMgmtBackupFsmStageOrder_Type()
)
cfprApMgmtBackupFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStageOrder.setStatus("current")
_CfprApMgmtBackupFsmStageRetry_Type = Gauge32
_CfprApMgmtBackupFsmStageRetry_Object = MibTableColumn
cfprApMgmtBackupFsmStageRetry = _CfprApMgmtBackupFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 7, 1, 8),
    _CfprApMgmtBackupFsmStageRetry_Type()
)
cfprApMgmtBackupFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStageRetry.setStatus("current")
_CfprApMgmtBackupFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtBackupFsmStageStageStatus_Object = MibTableColumn
cfprApMgmtBackupFsmStageStageStatus = _CfprApMgmtBackupFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 7, 1, 9),
    _CfprApMgmtBackupFsmStageStageStatus_Type()
)
cfprApMgmtBackupFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmStageStageStatus.setStatus("current")
_CfprApMgmtBackupFsmTaskTable_Object = MibTable
cfprApMgmtBackupFsmTaskTable = _CfprApMgmtBackupFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 8)
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmTaskTable.setStatus("current")
_CfprApMgmtBackupFsmTaskEntry_Object = MibTableRow
cfprApMgmtBackupFsmTaskEntry = _CfprApMgmtBackupFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 8, 1)
)
cfprApMgmtBackupFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtBackupFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmTaskEntry.setStatus("current")
_CfprApMgmtBackupFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtBackupFsmTaskInstanceId_Object = MibTableColumn
cfprApMgmtBackupFsmTaskInstanceId = _CfprApMgmtBackupFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 8, 1, 1),
    _CfprApMgmtBackupFsmTaskInstanceId_Type()
)
cfprApMgmtBackupFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmTaskInstanceId.setStatus("current")
_CfprApMgmtBackupFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApMgmtBackupFsmTaskDn_Object = MibTableColumn
cfprApMgmtBackupFsmTaskDn = _CfprApMgmtBackupFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 8, 1, 2),
    _CfprApMgmtBackupFsmTaskDn_Type()
)
cfprApMgmtBackupFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmTaskDn.setStatus("current")
_CfprApMgmtBackupFsmTaskRn_Type = SnmpAdminString
_CfprApMgmtBackupFsmTaskRn_Object = MibTableColumn
cfprApMgmtBackupFsmTaskRn = _CfprApMgmtBackupFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 8, 1, 3),
    _CfprApMgmtBackupFsmTaskRn_Type()
)
cfprApMgmtBackupFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmTaskRn.setStatus("current")
_CfprApMgmtBackupFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApMgmtBackupFsmTaskCompletion_Object = MibTableColumn
cfprApMgmtBackupFsmTaskCompletion = _CfprApMgmtBackupFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 8, 1, 4),
    _CfprApMgmtBackupFsmTaskCompletion_Type()
)
cfprApMgmtBackupFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmTaskCompletion.setStatus("current")
_CfprApMgmtBackupFsmTaskFlags_Type = CfprApFsmFlags
_CfprApMgmtBackupFsmTaskFlags_Object = MibTableColumn
cfprApMgmtBackupFsmTaskFlags = _CfprApMgmtBackupFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 8, 1, 5),
    _CfprApMgmtBackupFsmTaskFlags_Type()
)
cfprApMgmtBackupFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmTaskFlags.setStatus("current")
_CfprApMgmtBackupFsmTaskItem_Type = CfprApMgmtBackupFsmTaskItem
_CfprApMgmtBackupFsmTaskItem_Object = MibTableColumn
cfprApMgmtBackupFsmTaskItem = _CfprApMgmtBackupFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 8, 1, 6),
    _CfprApMgmtBackupFsmTaskItem_Type()
)
cfprApMgmtBackupFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmTaskItem.setStatus("current")
_CfprApMgmtBackupFsmTaskSeqId_Type = Gauge32
_CfprApMgmtBackupFsmTaskSeqId_Object = MibTableColumn
cfprApMgmtBackupFsmTaskSeqId = _CfprApMgmtBackupFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 8, 1, 7),
    _CfprApMgmtBackupFsmTaskSeqId_Type()
)
cfprApMgmtBackupFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupFsmTaskSeqId.setStatus("current")
_CfprApMgmtBackupPolicyTable_Object = MibTable
cfprApMgmtBackupPolicyTable = _CfprApMgmtBackupPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9)
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyTable.setStatus("current")
_CfprApMgmtBackupPolicyEntry_Object = MibTableRow
cfprApMgmtBackupPolicyEntry = _CfprApMgmtBackupPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1)
)
cfprApMgmtBackupPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtBackupPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyEntry.setStatus("current")
_CfprApMgmtBackupPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtBackupPolicyInstanceId_Object = MibTableColumn
cfprApMgmtBackupPolicyInstanceId = _CfprApMgmtBackupPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 1),
    _CfprApMgmtBackupPolicyInstanceId_Type()
)
cfprApMgmtBackupPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyInstanceId.setStatus("current")
_CfprApMgmtBackupPolicyDn_Type = CfprApManagedObjectDn
_CfprApMgmtBackupPolicyDn_Object = MibTableColumn
cfprApMgmtBackupPolicyDn = _CfprApMgmtBackupPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 2),
    _CfprApMgmtBackupPolicyDn_Type()
)
cfprApMgmtBackupPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyDn.setStatus("current")
_CfprApMgmtBackupPolicyRn_Type = SnmpAdminString
_CfprApMgmtBackupPolicyRn_Object = MibTableColumn
cfprApMgmtBackupPolicyRn = _CfprApMgmtBackupPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 3),
    _CfprApMgmtBackupPolicyRn_Type()
)
cfprApMgmtBackupPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyRn.setStatus("current")
_CfprApMgmtBackupPolicyAdminState_Type = CfprApMgmtExportPolicyAdminState
_CfprApMgmtBackupPolicyAdminState_Object = MibTableColumn
cfprApMgmtBackupPolicyAdminState = _CfprApMgmtBackupPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 4),
    _CfprApMgmtBackupPolicyAdminState_Type()
)
cfprApMgmtBackupPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyAdminState.setStatus("current")
_CfprApMgmtBackupPolicyDescr_Type = SnmpAdminString
_CfprApMgmtBackupPolicyDescr_Object = MibTableColumn
cfprApMgmtBackupPolicyDescr = _CfprApMgmtBackupPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 5),
    _CfprApMgmtBackupPolicyDescr_Type()
)
cfprApMgmtBackupPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyDescr.setStatus("current")
_CfprApMgmtBackupPolicyFsmDescr_Type = SnmpAdminString
_CfprApMgmtBackupPolicyFsmDescr_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmDescr = _CfprApMgmtBackupPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 6),
    _CfprApMgmtBackupPolicyFsmDescr_Type()
)
cfprApMgmtBackupPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmDescr.setStatus("current")
_CfprApMgmtBackupPolicyFsmPrev_Type = SnmpAdminString
_CfprApMgmtBackupPolicyFsmPrev_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmPrev = _CfprApMgmtBackupPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 7),
    _CfprApMgmtBackupPolicyFsmPrev_Type()
)
cfprApMgmtBackupPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmPrev.setStatus("current")
_CfprApMgmtBackupPolicyFsmProgr_Type = Gauge32
_CfprApMgmtBackupPolicyFsmProgr_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmProgr = _CfprApMgmtBackupPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 8),
    _CfprApMgmtBackupPolicyFsmProgr_Type()
)
cfprApMgmtBackupPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmProgr.setStatus("current")
_CfprApMgmtBackupPolicyFsmRmtInvErrCode_Type = Gauge32
_CfprApMgmtBackupPolicyFsmRmtInvErrCode_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmRmtInvErrCode = _CfprApMgmtBackupPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 9),
    _CfprApMgmtBackupPolicyFsmRmtInvErrCode_Type()
)
cfprApMgmtBackupPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmRmtInvErrCode.setStatus("current")
_CfprApMgmtBackupPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApMgmtBackupPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmRmtInvErrDescr = _CfprApMgmtBackupPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 10),
    _CfprApMgmtBackupPolicyFsmRmtInvErrDescr_Type()
)
cfprApMgmtBackupPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmRmtInvErrDescr.setStatus("current")
_CfprApMgmtBackupPolicyFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtBackupPolicyFsmRmtInvRslt_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmRmtInvRslt = _CfprApMgmtBackupPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 11),
    _CfprApMgmtBackupPolicyFsmRmtInvRslt_Type()
)
cfprApMgmtBackupPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmRmtInvRslt.setStatus("current")
_CfprApMgmtBackupPolicyFsmStageDescr_Type = SnmpAdminString
_CfprApMgmtBackupPolicyFsmStageDescr_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmStageDescr = _CfprApMgmtBackupPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 12),
    _CfprApMgmtBackupPolicyFsmStageDescr_Type()
)
cfprApMgmtBackupPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStageDescr.setStatus("current")
_CfprApMgmtBackupPolicyFsmStamp_Type = DateAndTime
_CfprApMgmtBackupPolicyFsmStamp_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmStamp = _CfprApMgmtBackupPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 13),
    _CfprApMgmtBackupPolicyFsmStamp_Type()
)
cfprApMgmtBackupPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStamp.setStatus("current")
_CfprApMgmtBackupPolicyFsmStatus_Type = SnmpAdminString
_CfprApMgmtBackupPolicyFsmStatus_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmStatus = _CfprApMgmtBackupPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 14),
    _CfprApMgmtBackupPolicyFsmStatus_Type()
)
cfprApMgmtBackupPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStatus.setStatus("current")
_CfprApMgmtBackupPolicyFsmTry_Type = Gauge32
_CfprApMgmtBackupPolicyFsmTry_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmTry = _CfprApMgmtBackupPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 15),
    _CfprApMgmtBackupPolicyFsmTry_Type()
)
cfprApMgmtBackupPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmTry.setStatus("current")
_CfprApMgmtBackupPolicyHost_Type = SnmpAdminString
_CfprApMgmtBackupPolicyHost_Object = MibTableColumn
cfprApMgmtBackupPolicyHost = _CfprApMgmtBackupPolicyHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 16),
    _CfprApMgmtBackupPolicyHost_Type()
)
cfprApMgmtBackupPolicyHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyHost.setStatus("current")
_CfprApMgmtBackupPolicyIntId_Type = SnmpAdminString
_CfprApMgmtBackupPolicyIntId_Object = MibTableColumn
cfprApMgmtBackupPolicyIntId = _CfprApMgmtBackupPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 17),
    _CfprApMgmtBackupPolicyIntId_Type()
)
cfprApMgmtBackupPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyIntId.setStatus("current")
_CfprApMgmtBackupPolicyLastBackup_Type = DateAndTime
_CfprApMgmtBackupPolicyLastBackup_Object = MibTableColumn
cfprApMgmtBackupPolicyLastBackup = _CfprApMgmtBackupPolicyLastBackup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 18),
    _CfprApMgmtBackupPolicyLastBackup_Type()
)
cfprApMgmtBackupPolicyLastBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyLastBackup.setStatus("current")
_CfprApMgmtBackupPolicyMaxFiles_Type = Gauge32
_CfprApMgmtBackupPolicyMaxFiles_Object = MibTableColumn
cfprApMgmtBackupPolicyMaxFiles = _CfprApMgmtBackupPolicyMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 19),
    _CfprApMgmtBackupPolicyMaxFiles_Type()
)
cfprApMgmtBackupPolicyMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyMaxFiles.setStatus("current")
_CfprApMgmtBackupPolicyName_Type = SnmpAdminString
_CfprApMgmtBackupPolicyName_Object = MibTableColumn
cfprApMgmtBackupPolicyName = _CfprApMgmtBackupPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 20),
    _CfprApMgmtBackupPolicyName_Type()
)
cfprApMgmtBackupPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyName.setStatus("current")
_CfprApMgmtBackupPolicyPolicyLevel_Type = Gauge32
_CfprApMgmtBackupPolicyPolicyLevel_Object = MibTableColumn
cfprApMgmtBackupPolicyPolicyLevel = _CfprApMgmtBackupPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 21),
    _CfprApMgmtBackupPolicyPolicyLevel_Type()
)
cfprApMgmtBackupPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyPolicyLevel.setStatus("current")
_CfprApMgmtBackupPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApMgmtBackupPolicyPolicyOwner_Object = MibTableColumn
cfprApMgmtBackupPolicyPolicyOwner = _CfprApMgmtBackupPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 22),
    _CfprApMgmtBackupPolicyPolicyOwner_Type()
)
cfprApMgmtBackupPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyPolicyOwner.setStatus("current")
_CfprApMgmtBackupPolicyPort_Type = Gauge32
_CfprApMgmtBackupPolicyPort_Object = MibTableColumn
cfprApMgmtBackupPolicyPort = _CfprApMgmtBackupPolicyPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 23),
    _CfprApMgmtBackupPolicyPort_Type()
)
cfprApMgmtBackupPolicyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyPort.setStatus("current")
_CfprApMgmtBackupPolicyProto_Type = CfprApMgmtExportPolicyProto
_CfprApMgmtBackupPolicyProto_Object = MibTableColumn
cfprApMgmtBackupPolicyProto = _CfprApMgmtBackupPolicyProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 24),
    _CfprApMgmtBackupPolicyProto_Type()
)
cfprApMgmtBackupPolicyProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyProto.setStatus("current")
_CfprApMgmtBackupPolicyPwd_Type = SnmpAdminString
_CfprApMgmtBackupPolicyPwd_Object = MibTableColumn
cfprApMgmtBackupPolicyPwd = _CfprApMgmtBackupPolicyPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 25),
    _CfprApMgmtBackupPolicyPwd_Type()
)
cfprApMgmtBackupPolicyPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyPwd.setStatus("current")
_CfprApMgmtBackupPolicyRemoteFile_Type = SnmpAdminString
_CfprApMgmtBackupPolicyRemoteFile_Object = MibTableColumn
cfprApMgmtBackupPolicyRemoteFile = _CfprApMgmtBackupPolicyRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 26),
    _CfprApMgmtBackupPolicyRemoteFile_Type()
)
cfprApMgmtBackupPolicyRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyRemoteFile.setStatus("current")
_CfprApMgmtBackupPolicySchedule_Type = CfprApMgmtBackupInterval
_CfprApMgmtBackupPolicySchedule_Object = MibTableColumn
cfprApMgmtBackupPolicySchedule = _CfprApMgmtBackupPolicySchedule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 27),
    _CfprApMgmtBackupPolicySchedule_Type()
)
cfprApMgmtBackupPolicySchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicySchedule.setStatus("current")
_CfprApMgmtBackupPolicyUser_Type = SnmpAdminString
_CfprApMgmtBackupPolicyUser_Object = MibTableColumn
cfprApMgmtBackupPolicyUser = _CfprApMgmtBackupPolicyUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 9, 1, 28),
    _CfprApMgmtBackupPolicyUser_Type()
)
cfprApMgmtBackupPolicyUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyUser.setStatus("current")
_CfprApMgmtBackupPolicyConfigTable_Object = MibTable
cfprApMgmtBackupPolicyConfigTable = _CfprApMgmtBackupPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10)
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigTable.setStatus("current")
_CfprApMgmtBackupPolicyConfigEntry_Object = MibTableRow
cfprApMgmtBackupPolicyConfigEntry = _CfprApMgmtBackupPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1)
)
cfprApMgmtBackupPolicyConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtBackupPolicyConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigEntry.setStatus("current")
_CfprApMgmtBackupPolicyConfigInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtBackupPolicyConfigInstanceId_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigInstanceId = _CfprApMgmtBackupPolicyConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 1),
    _CfprApMgmtBackupPolicyConfigInstanceId_Type()
)
cfprApMgmtBackupPolicyConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigInstanceId.setStatus("current")
_CfprApMgmtBackupPolicyConfigDn_Type = CfprApManagedObjectDn
_CfprApMgmtBackupPolicyConfigDn_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigDn = _CfprApMgmtBackupPolicyConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 2),
    _CfprApMgmtBackupPolicyConfigDn_Type()
)
cfprApMgmtBackupPolicyConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigDn.setStatus("current")
_CfprApMgmtBackupPolicyConfigRn_Type = SnmpAdminString
_CfprApMgmtBackupPolicyConfigRn_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigRn = _CfprApMgmtBackupPolicyConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 3),
    _CfprApMgmtBackupPolicyConfigRn_Type()
)
cfprApMgmtBackupPolicyConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigRn.setStatus("current")
_CfprApMgmtBackupPolicyConfigAdminState_Type = CfprApTrigAdminState
_CfprApMgmtBackupPolicyConfigAdminState_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigAdminState = _CfprApMgmtBackupPolicyConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 4),
    _CfprApMgmtBackupPolicyConfigAdminState_Type()
)
cfprApMgmtBackupPolicyConfigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigAdminState.setStatus("current")
_CfprApMgmtBackupPolicyConfigAutoDelete_Type = TruthValue
_CfprApMgmtBackupPolicyConfigAutoDelete_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigAutoDelete = _CfprApMgmtBackupPolicyConfigAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 5),
    _CfprApMgmtBackupPolicyConfigAutoDelete_Type()
)
cfprApMgmtBackupPolicyConfigAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigAutoDelete.setStatus("current")
_CfprApMgmtBackupPolicyConfigBackupDate_Type = DateAndTime
_CfprApMgmtBackupPolicyConfigBackupDate_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigBackupDate = _CfprApMgmtBackupPolicyConfigBackupDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 6),
    _CfprApMgmtBackupPolicyConfigBackupDate_Type()
)
cfprApMgmtBackupPolicyConfigBackupDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigBackupDate.setStatus("current")
_CfprApMgmtBackupPolicyConfigBackupIssue_Type = CfprApMgmtBackupIssue
_CfprApMgmtBackupPolicyConfigBackupIssue_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigBackupIssue = _CfprApMgmtBackupPolicyConfigBackupIssue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 7),
    _CfprApMgmtBackupPolicyConfigBackupIssue_Type()
)
cfprApMgmtBackupPolicyConfigBackupIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigBackupIssue.setStatus("current")
_CfprApMgmtBackupPolicyConfigDescr_Type = SnmpAdminString
_CfprApMgmtBackupPolicyConfigDescr_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigDescr = _CfprApMgmtBackupPolicyConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 8),
    _CfprApMgmtBackupPolicyConfigDescr_Type()
)
cfprApMgmtBackupPolicyConfigDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigDescr.setStatus("current")
_CfprApMgmtBackupPolicyConfigIgnoreCap_Type = TruthValue
_CfprApMgmtBackupPolicyConfigIgnoreCap_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigIgnoreCap = _CfprApMgmtBackupPolicyConfigIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 9),
    _CfprApMgmtBackupPolicyConfigIgnoreCap_Type()
)
cfprApMgmtBackupPolicyConfigIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigIgnoreCap.setStatus("current")
_CfprApMgmtBackupPolicyConfigIntId_Type = SnmpAdminString
_CfprApMgmtBackupPolicyConfigIntId_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigIntId = _CfprApMgmtBackupPolicyConfigIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 10),
    _CfprApMgmtBackupPolicyConfigIntId_Type()
)
cfprApMgmtBackupPolicyConfigIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigIntId.setStatus("current")
_CfprApMgmtBackupPolicyConfigName_Type = SnmpAdminString
_CfprApMgmtBackupPolicyConfigName_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigName = _CfprApMgmtBackupPolicyConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 11),
    _CfprApMgmtBackupPolicyConfigName_Type()
)
cfprApMgmtBackupPolicyConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigName.setStatus("current")
_CfprApMgmtBackupPolicyConfigOperScheduler_Type = SnmpAdminString
_CfprApMgmtBackupPolicyConfigOperScheduler_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigOperScheduler = _CfprApMgmtBackupPolicyConfigOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 12),
    _CfprApMgmtBackupPolicyConfigOperScheduler_Type()
)
cfprApMgmtBackupPolicyConfigOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigOperScheduler.setStatus("current")
_CfprApMgmtBackupPolicyConfigOperState_Type = CfprApTrigTrigOperState
_CfprApMgmtBackupPolicyConfigOperState_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigOperState = _CfprApMgmtBackupPolicyConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 13),
    _CfprApMgmtBackupPolicyConfigOperState_Type()
)
cfprApMgmtBackupPolicyConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigOperState.setStatus("current")
_CfprApMgmtBackupPolicyConfigPolicyLevel_Type = Gauge32
_CfprApMgmtBackupPolicyConfigPolicyLevel_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigPolicyLevel = _CfprApMgmtBackupPolicyConfigPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 14),
    _CfprApMgmtBackupPolicyConfigPolicyLevel_Type()
)
cfprApMgmtBackupPolicyConfigPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigPolicyLevel.setStatus("current")
_CfprApMgmtBackupPolicyConfigPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApMgmtBackupPolicyConfigPolicyOwner_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigPolicyOwner = _CfprApMgmtBackupPolicyConfigPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 15),
    _CfprApMgmtBackupPolicyConfigPolicyOwner_Type()
)
cfprApMgmtBackupPolicyConfigPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigPolicyOwner.setStatus("current")
_CfprApMgmtBackupPolicyConfigScheduler_Type = SnmpAdminString
_CfprApMgmtBackupPolicyConfigScheduler_Object = MibTableColumn
cfprApMgmtBackupPolicyConfigScheduler = _CfprApMgmtBackupPolicyConfigScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 10, 1, 16),
    _CfprApMgmtBackupPolicyConfigScheduler_Type()
)
cfprApMgmtBackupPolicyConfigScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyConfigScheduler.setStatus("current")
_CfprApMgmtBackupPolicyFsmTable_Object = MibTable
cfprApMgmtBackupPolicyFsmTable = _CfprApMgmtBackupPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11)
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmTable.setStatus("current")
_CfprApMgmtBackupPolicyFsmEntry_Object = MibTableRow
cfprApMgmtBackupPolicyFsmEntry = _CfprApMgmtBackupPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11, 1)
)
cfprApMgmtBackupPolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtBackupPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmEntry.setStatus("current")
_CfprApMgmtBackupPolicyFsmInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtBackupPolicyFsmInstanceId_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmInstanceId = _CfprApMgmtBackupPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11, 1, 1),
    _CfprApMgmtBackupPolicyFsmInstanceId_Type()
)
cfprApMgmtBackupPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmInstanceId.setStatus("current")
_CfprApMgmtBackupPolicyFsmDn_Type = CfprApManagedObjectDn
_CfprApMgmtBackupPolicyFsmDn_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmDn = _CfprApMgmtBackupPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11, 1, 2),
    _CfprApMgmtBackupPolicyFsmDn_Type()
)
cfprApMgmtBackupPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmDn.setStatus("current")
_CfprApMgmtBackupPolicyFsmRn_Type = SnmpAdminString
_CfprApMgmtBackupPolicyFsmRn_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmRn = _CfprApMgmtBackupPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11, 1, 3),
    _CfprApMgmtBackupPolicyFsmRn_Type()
)
cfprApMgmtBackupPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmRn.setStatus("current")
_CfprApMgmtBackupPolicyFsmCompletionTime_Type = DateAndTime
_CfprApMgmtBackupPolicyFsmCompletionTime_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmCompletionTime = _CfprApMgmtBackupPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11, 1, 4),
    _CfprApMgmtBackupPolicyFsmCompletionTime_Type()
)
cfprApMgmtBackupPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmCompletionTime.setStatus("current")
_CfprApMgmtBackupPolicyFsmCurrentFsm_Type = CfprApMgmtBackupPolicyFsmCurrentFsm
_CfprApMgmtBackupPolicyFsmCurrentFsm_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmCurrentFsm = _CfprApMgmtBackupPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11, 1, 5),
    _CfprApMgmtBackupPolicyFsmCurrentFsm_Type()
)
cfprApMgmtBackupPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmCurrentFsm.setStatus("current")
_CfprApMgmtBackupPolicyFsmDescrData_Type = SnmpAdminString
_CfprApMgmtBackupPolicyFsmDescrData_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmDescrData = _CfprApMgmtBackupPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11, 1, 6),
    _CfprApMgmtBackupPolicyFsmDescrData_Type()
)
cfprApMgmtBackupPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmDescrData.setStatus("current")
_CfprApMgmtBackupPolicyFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtBackupPolicyFsmFsmStatus_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmFsmStatus = _CfprApMgmtBackupPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11, 1, 7),
    _CfprApMgmtBackupPolicyFsmFsmStatus_Type()
)
cfprApMgmtBackupPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmFsmStatus.setStatus("current")
_CfprApMgmtBackupPolicyFsmProgress_Type = Gauge32
_CfprApMgmtBackupPolicyFsmProgress_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmProgress = _CfprApMgmtBackupPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11, 1, 8),
    _CfprApMgmtBackupPolicyFsmProgress_Type()
)
cfprApMgmtBackupPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmProgress.setStatus("current")
_CfprApMgmtBackupPolicyFsmRmtErrCode_Type = Gauge32
_CfprApMgmtBackupPolicyFsmRmtErrCode_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmRmtErrCode = _CfprApMgmtBackupPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11, 1, 9),
    _CfprApMgmtBackupPolicyFsmRmtErrCode_Type()
)
cfprApMgmtBackupPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmRmtErrCode.setStatus("current")
_CfprApMgmtBackupPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprApMgmtBackupPolicyFsmRmtErrDescr_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmRmtErrDescr = _CfprApMgmtBackupPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11, 1, 10),
    _CfprApMgmtBackupPolicyFsmRmtErrDescr_Type()
)
cfprApMgmtBackupPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmRmtErrDescr.setStatus("current")
_CfprApMgmtBackupPolicyFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtBackupPolicyFsmRmtRslt_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmRmtRslt = _CfprApMgmtBackupPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 11, 1, 11),
    _CfprApMgmtBackupPolicyFsmRmtRslt_Type()
)
cfprApMgmtBackupPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmRmtRslt.setStatus("current")
_CfprApMgmtBackupPolicyFsmStageTable_Object = MibTable
cfprApMgmtBackupPolicyFsmStageTable = _CfprApMgmtBackupPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 12)
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStageTable.setStatus("current")
_CfprApMgmtBackupPolicyFsmStageEntry_Object = MibTableRow
cfprApMgmtBackupPolicyFsmStageEntry = _CfprApMgmtBackupPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 12, 1)
)
cfprApMgmtBackupPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtBackupPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStageEntry.setStatus("current")
_CfprApMgmtBackupPolicyFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtBackupPolicyFsmStageInstanceId_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmStageInstanceId = _CfprApMgmtBackupPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 12, 1, 1),
    _CfprApMgmtBackupPolicyFsmStageInstanceId_Type()
)
cfprApMgmtBackupPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStageInstanceId.setStatus("current")
_CfprApMgmtBackupPolicyFsmStageDn_Type = CfprApManagedObjectDn
_CfprApMgmtBackupPolicyFsmStageDn_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmStageDn = _CfprApMgmtBackupPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 12, 1, 2),
    _CfprApMgmtBackupPolicyFsmStageDn_Type()
)
cfprApMgmtBackupPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStageDn.setStatus("current")
_CfprApMgmtBackupPolicyFsmStageRn_Type = SnmpAdminString
_CfprApMgmtBackupPolicyFsmStageRn_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmStageRn = _CfprApMgmtBackupPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 12, 1, 3),
    _CfprApMgmtBackupPolicyFsmStageRn_Type()
)
cfprApMgmtBackupPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStageRn.setStatus("current")
_CfprApMgmtBackupPolicyFsmStageDescrData_Type = SnmpAdminString
_CfprApMgmtBackupPolicyFsmStageDescrData_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmStageDescrData = _CfprApMgmtBackupPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 12, 1, 4),
    _CfprApMgmtBackupPolicyFsmStageDescrData_Type()
)
cfprApMgmtBackupPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStageDescrData.setStatus("current")
_CfprApMgmtBackupPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprApMgmtBackupPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmStageLastUpdateTime = _CfprApMgmtBackupPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 12, 1, 5),
    _CfprApMgmtBackupPolicyFsmStageLastUpdateTime_Type()
)
cfprApMgmtBackupPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStageLastUpdateTime.setStatus("current")
_CfprApMgmtBackupPolicyFsmStageName_Type = CfprApMgmtBackupPolicyFsmStageName
_CfprApMgmtBackupPolicyFsmStageName_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmStageName = _CfprApMgmtBackupPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 12, 1, 6),
    _CfprApMgmtBackupPolicyFsmStageName_Type()
)
cfprApMgmtBackupPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStageName.setStatus("current")
_CfprApMgmtBackupPolicyFsmStageOrder_Type = Gauge32
_CfprApMgmtBackupPolicyFsmStageOrder_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmStageOrder = _CfprApMgmtBackupPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 12, 1, 7),
    _CfprApMgmtBackupPolicyFsmStageOrder_Type()
)
cfprApMgmtBackupPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStageOrder.setStatus("current")
_CfprApMgmtBackupPolicyFsmStageRetry_Type = Gauge32
_CfprApMgmtBackupPolicyFsmStageRetry_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmStageRetry = _CfprApMgmtBackupPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 12, 1, 8),
    _CfprApMgmtBackupPolicyFsmStageRetry_Type()
)
cfprApMgmtBackupPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStageRetry.setStatus("current")
_CfprApMgmtBackupPolicyFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtBackupPolicyFsmStageStageStatus_Object = MibTableColumn
cfprApMgmtBackupPolicyFsmStageStageStatus = _CfprApMgmtBackupPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 12, 1, 9),
    _CfprApMgmtBackupPolicyFsmStageStageStatus_Type()
)
cfprApMgmtBackupPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtBackupPolicyFsmStageStageStatus.setStatus("current")
_CfprApMgmtCfgExportPolicyTable_Object = MibTable
cfprApMgmtCfgExportPolicyTable = _CfprApMgmtCfgExportPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13)
)
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyTable.setStatus("current")
_CfprApMgmtCfgExportPolicyEntry_Object = MibTableRow
cfprApMgmtCfgExportPolicyEntry = _CfprApMgmtCfgExportPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1)
)
cfprApMgmtCfgExportPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtCfgExportPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyEntry.setStatus("current")
_CfprApMgmtCfgExportPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtCfgExportPolicyInstanceId_Object = MibTableColumn
cfprApMgmtCfgExportPolicyInstanceId = _CfprApMgmtCfgExportPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 1),
    _CfprApMgmtCfgExportPolicyInstanceId_Type()
)
cfprApMgmtCfgExportPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyInstanceId.setStatus("current")
_CfprApMgmtCfgExportPolicyDn_Type = CfprApManagedObjectDn
_CfprApMgmtCfgExportPolicyDn_Object = MibTableColumn
cfprApMgmtCfgExportPolicyDn = _CfprApMgmtCfgExportPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 2),
    _CfprApMgmtCfgExportPolicyDn_Type()
)
cfprApMgmtCfgExportPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyDn.setStatus("current")
_CfprApMgmtCfgExportPolicyRn_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyRn_Object = MibTableColumn
cfprApMgmtCfgExportPolicyRn = _CfprApMgmtCfgExportPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 3),
    _CfprApMgmtCfgExportPolicyRn_Type()
)
cfprApMgmtCfgExportPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyRn.setStatus("current")
_CfprApMgmtCfgExportPolicyAdminState_Type = CfprApMgmtExportPolicyAdminState
_CfprApMgmtCfgExportPolicyAdminState_Object = MibTableColumn
cfprApMgmtCfgExportPolicyAdminState = _CfprApMgmtCfgExportPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 4),
    _CfprApMgmtCfgExportPolicyAdminState_Type()
)
cfprApMgmtCfgExportPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyAdminState.setStatus("current")
_CfprApMgmtCfgExportPolicyDescr_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyDescr_Object = MibTableColumn
cfprApMgmtCfgExportPolicyDescr = _CfprApMgmtCfgExportPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 5),
    _CfprApMgmtCfgExportPolicyDescr_Type()
)
cfprApMgmtCfgExportPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyDescr.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmDescr_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyFsmDescr_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmDescr = _CfprApMgmtCfgExportPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 6),
    _CfprApMgmtCfgExportPolicyFsmDescr_Type()
)
cfprApMgmtCfgExportPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmDescr.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmPrev_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyFsmPrev_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmPrev = _CfprApMgmtCfgExportPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 7),
    _CfprApMgmtCfgExportPolicyFsmPrev_Type()
)
cfprApMgmtCfgExportPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmPrev.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmProgr_Type = Gauge32
_CfprApMgmtCfgExportPolicyFsmProgr_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmProgr = _CfprApMgmtCfgExportPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 8),
    _CfprApMgmtCfgExportPolicyFsmProgr_Type()
)
cfprApMgmtCfgExportPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmProgr.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmRmtInvErrCode_Type = Gauge32
_CfprApMgmtCfgExportPolicyFsmRmtInvErrCode_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmRmtInvErrCode = _CfprApMgmtCfgExportPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 9),
    _CfprApMgmtCfgExportPolicyFsmRmtInvErrCode_Type()
)
cfprApMgmtCfgExportPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmRmtInvErrCode.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmRmtInvErrDescr = _CfprApMgmtCfgExportPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 10),
    _CfprApMgmtCfgExportPolicyFsmRmtInvErrDescr_Type()
)
cfprApMgmtCfgExportPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmRmtInvErrDescr.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtCfgExportPolicyFsmRmtInvRslt_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmRmtInvRslt = _CfprApMgmtCfgExportPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 11),
    _CfprApMgmtCfgExportPolicyFsmRmtInvRslt_Type()
)
cfprApMgmtCfgExportPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmRmtInvRslt.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStageDescr_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyFsmStageDescr_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmStageDescr = _CfprApMgmtCfgExportPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 12),
    _CfprApMgmtCfgExportPolicyFsmStageDescr_Type()
)
cfprApMgmtCfgExportPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStageDescr.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStamp_Type = DateAndTime
_CfprApMgmtCfgExportPolicyFsmStamp_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmStamp = _CfprApMgmtCfgExportPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 13),
    _CfprApMgmtCfgExportPolicyFsmStamp_Type()
)
cfprApMgmtCfgExportPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStamp.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStatus_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyFsmStatus_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmStatus = _CfprApMgmtCfgExportPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 14),
    _CfprApMgmtCfgExportPolicyFsmStatus_Type()
)
cfprApMgmtCfgExportPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStatus.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmTry_Type = Gauge32
_CfprApMgmtCfgExportPolicyFsmTry_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmTry = _CfprApMgmtCfgExportPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 15),
    _CfprApMgmtCfgExportPolicyFsmTry_Type()
)
cfprApMgmtCfgExportPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmTry.setStatus("current")
_CfprApMgmtCfgExportPolicyHost_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyHost_Object = MibTableColumn
cfprApMgmtCfgExportPolicyHost = _CfprApMgmtCfgExportPolicyHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 16),
    _CfprApMgmtCfgExportPolicyHost_Type()
)
cfprApMgmtCfgExportPolicyHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyHost.setStatus("current")
_CfprApMgmtCfgExportPolicyIntId_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyIntId_Object = MibTableColumn
cfprApMgmtCfgExportPolicyIntId = _CfprApMgmtCfgExportPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 17),
    _CfprApMgmtCfgExportPolicyIntId_Type()
)
cfprApMgmtCfgExportPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyIntId.setStatus("current")
_CfprApMgmtCfgExportPolicyLastBackup_Type = DateAndTime
_CfprApMgmtCfgExportPolicyLastBackup_Object = MibTableColumn
cfprApMgmtCfgExportPolicyLastBackup = _CfprApMgmtCfgExportPolicyLastBackup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 18),
    _CfprApMgmtCfgExportPolicyLastBackup_Type()
)
cfprApMgmtCfgExportPolicyLastBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyLastBackup.setStatus("current")
_CfprApMgmtCfgExportPolicyMaxFiles_Type = Gauge32
_CfprApMgmtCfgExportPolicyMaxFiles_Object = MibTableColumn
cfprApMgmtCfgExportPolicyMaxFiles = _CfprApMgmtCfgExportPolicyMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 19),
    _CfprApMgmtCfgExportPolicyMaxFiles_Type()
)
cfprApMgmtCfgExportPolicyMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyMaxFiles.setStatus("current")
_CfprApMgmtCfgExportPolicyName_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyName_Object = MibTableColumn
cfprApMgmtCfgExportPolicyName = _CfprApMgmtCfgExportPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 20),
    _CfprApMgmtCfgExportPolicyName_Type()
)
cfprApMgmtCfgExportPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyName.setStatus("current")
_CfprApMgmtCfgExportPolicyPolicyLevel_Type = Gauge32
_CfprApMgmtCfgExportPolicyPolicyLevel_Object = MibTableColumn
cfprApMgmtCfgExportPolicyPolicyLevel = _CfprApMgmtCfgExportPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 21),
    _CfprApMgmtCfgExportPolicyPolicyLevel_Type()
)
cfprApMgmtCfgExportPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyPolicyLevel.setStatus("current")
_CfprApMgmtCfgExportPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApMgmtCfgExportPolicyPolicyOwner_Object = MibTableColumn
cfprApMgmtCfgExportPolicyPolicyOwner = _CfprApMgmtCfgExportPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 22),
    _CfprApMgmtCfgExportPolicyPolicyOwner_Type()
)
cfprApMgmtCfgExportPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyPolicyOwner.setStatus("current")
_CfprApMgmtCfgExportPolicyPort_Type = Gauge32
_CfprApMgmtCfgExportPolicyPort_Object = MibTableColumn
cfprApMgmtCfgExportPolicyPort = _CfprApMgmtCfgExportPolicyPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 23),
    _CfprApMgmtCfgExportPolicyPort_Type()
)
cfprApMgmtCfgExportPolicyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyPort.setStatus("current")
_CfprApMgmtCfgExportPolicyProto_Type = CfprApMgmtExportPolicyProto
_CfprApMgmtCfgExportPolicyProto_Object = MibTableColumn
cfprApMgmtCfgExportPolicyProto = _CfprApMgmtCfgExportPolicyProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 24),
    _CfprApMgmtCfgExportPolicyProto_Type()
)
cfprApMgmtCfgExportPolicyProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyProto.setStatus("current")
_CfprApMgmtCfgExportPolicyPwd_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyPwd_Object = MibTableColumn
cfprApMgmtCfgExportPolicyPwd = _CfprApMgmtCfgExportPolicyPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 25),
    _CfprApMgmtCfgExportPolicyPwd_Type()
)
cfprApMgmtCfgExportPolicyPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyPwd.setStatus("current")
_CfprApMgmtCfgExportPolicyRemoteFile_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyRemoteFile_Object = MibTableColumn
cfprApMgmtCfgExportPolicyRemoteFile = _CfprApMgmtCfgExportPolicyRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 26),
    _CfprApMgmtCfgExportPolicyRemoteFile_Type()
)
cfprApMgmtCfgExportPolicyRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyRemoteFile.setStatus("current")
_CfprApMgmtCfgExportPolicySchedule_Type = CfprApMgmtBackupInterval
_CfprApMgmtCfgExportPolicySchedule_Object = MibTableColumn
cfprApMgmtCfgExportPolicySchedule = _CfprApMgmtCfgExportPolicySchedule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 27),
    _CfprApMgmtCfgExportPolicySchedule_Type()
)
cfprApMgmtCfgExportPolicySchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicySchedule.setStatus("current")
_CfprApMgmtCfgExportPolicyUser_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyUser_Object = MibTableColumn
cfprApMgmtCfgExportPolicyUser = _CfprApMgmtCfgExportPolicyUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 13, 1, 28),
    _CfprApMgmtCfgExportPolicyUser_Type()
)
cfprApMgmtCfgExportPolicyUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyUser.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmTable_Object = MibTable
cfprApMgmtCfgExportPolicyFsmTable = _CfprApMgmtCfgExportPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14)
)
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmTable.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmEntry_Object = MibTableRow
cfprApMgmtCfgExportPolicyFsmEntry = _CfprApMgmtCfgExportPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14, 1)
)
cfprApMgmtCfgExportPolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtCfgExportPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmEntry.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtCfgExportPolicyFsmInstanceId_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmInstanceId = _CfprApMgmtCfgExportPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14, 1, 1),
    _CfprApMgmtCfgExportPolicyFsmInstanceId_Type()
)
cfprApMgmtCfgExportPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmInstanceId.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmDn_Type = CfprApManagedObjectDn
_CfprApMgmtCfgExportPolicyFsmDn_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmDn = _CfprApMgmtCfgExportPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14, 1, 2),
    _CfprApMgmtCfgExportPolicyFsmDn_Type()
)
cfprApMgmtCfgExportPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmDn.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmRn_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyFsmRn_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmRn = _CfprApMgmtCfgExportPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14, 1, 3),
    _CfprApMgmtCfgExportPolicyFsmRn_Type()
)
cfprApMgmtCfgExportPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmRn.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmCompletionTime_Type = DateAndTime
_CfprApMgmtCfgExportPolicyFsmCompletionTime_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmCompletionTime = _CfprApMgmtCfgExportPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14, 1, 4),
    _CfprApMgmtCfgExportPolicyFsmCompletionTime_Type()
)
cfprApMgmtCfgExportPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmCompletionTime.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmCurrentFsm_Type = CfprApMgmtCfgExportPolicyFsmCurrentFsm
_CfprApMgmtCfgExportPolicyFsmCurrentFsm_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmCurrentFsm = _CfprApMgmtCfgExportPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14, 1, 5),
    _CfprApMgmtCfgExportPolicyFsmCurrentFsm_Type()
)
cfprApMgmtCfgExportPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmCurrentFsm.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmDescrData_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyFsmDescrData_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmDescrData = _CfprApMgmtCfgExportPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14, 1, 6),
    _CfprApMgmtCfgExportPolicyFsmDescrData_Type()
)
cfprApMgmtCfgExportPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmDescrData.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtCfgExportPolicyFsmFsmStatus_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmFsmStatus = _CfprApMgmtCfgExportPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14, 1, 7),
    _CfprApMgmtCfgExportPolicyFsmFsmStatus_Type()
)
cfprApMgmtCfgExportPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmFsmStatus.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmProgress_Type = Gauge32
_CfprApMgmtCfgExportPolicyFsmProgress_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmProgress = _CfprApMgmtCfgExportPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14, 1, 8),
    _CfprApMgmtCfgExportPolicyFsmProgress_Type()
)
cfprApMgmtCfgExportPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmProgress.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmRmtErrCode_Type = Gauge32
_CfprApMgmtCfgExportPolicyFsmRmtErrCode_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmRmtErrCode = _CfprApMgmtCfgExportPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14, 1, 9),
    _CfprApMgmtCfgExportPolicyFsmRmtErrCode_Type()
)
cfprApMgmtCfgExportPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmRmtErrCode.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyFsmRmtErrDescr_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmRmtErrDescr = _CfprApMgmtCfgExportPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14, 1, 10),
    _CfprApMgmtCfgExportPolicyFsmRmtErrDescr_Type()
)
cfprApMgmtCfgExportPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmRmtErrDescr.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtCfgExportPolicyFsmRmtRslt_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmRmtRslt = _CfprApMgmtCfgExportPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 14, 1, 11),
    _CfprApMgmtCfgExportPolicyFsmRmtRslt_Type()
)
cfprApMgmtCfgExportPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmRmtRslt.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStageTable_Object = MibTable
cfprApMgmtCfgExportPolicyFsmStageTable = _CfprApMgmtCfgExportPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 15)
)
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStageTable.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStageEntry_Object = MibTableRow
cfprApMgmtCfgExportPolicyFsmStageEntry = _CfprApMgmtCfgExportPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 15, 1)
)
cfprApMgmtCfgExportPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtCfgExportPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStageEntry.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtCfgExportPolicyFsmStageInstanceId_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmStageInstanceId = _CfprApMgmtCfgExportPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 15, 1, 1),
    _CfprApMgmtCfgExportPolicyFsmStageInstanceId_Type()
)
cfprApMgmtCfgExportPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStageInstanceId.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStageDn_Type = CfprApManagedObjectDn
_CfprApMgmtCfgExportPolicyFsmStageDn_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmStageDn = _CfprApMgmtCfgExportPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 15, 1, 2),
    _CfprApMgmtCfgExportPolicyFsmStageDn_Type()
)
cfprApMgmtCfgExportPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStageDn.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStageRn_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyFsmStageRn_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmStageRn = _CfprApMgmtCfgExportPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 15, 1, 3),
    _CfprApMgmtCfgExportPolicyFsmStageRn_Type()
)
cfprApMgmtCfgExportPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStageRn.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStageDescrData_Type = SnmpAdminString
_CfprApMgmtCfgExportPolicyFsmStageDescrData_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmStageDescrData = _CfprApMgmtCfgExportPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 15, 1, 4),
    _CfprApMgmtCfgExportPolicyFsmStageDescrData_Type()
)
cfprApMgmtCfgExportPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStageDescrData.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprApMgmtCfgExportPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmStageLastUpdateTime = _CfprApMgmtCfgExportPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 15, 1, 5),
    _CfprApMgmtCfgExportPolicyFsmStageLastUpdateTime_Type()
)
cfprApMgmtCfgExportPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStageLastUpdateTime.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStageName_Type = CfprApMgmtCfgExportPolicyFsmStageName
_CfprApMgmtCfgExportPolicyFsmStageName_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmStageName = _CfprApMgmtCfgExportPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 15, 1, 6),
    _CfprApMgmtCfgExportPolicyFsmStageName_Type()
)
cfprApMgmtCfgExportPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStageName.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStageOrder_Type = Gauge32
_CfprApMgmtCfgExportPolicyFsmStageOrder_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmStageOrder = _CfprApMgmtCfgExportPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 15, 1, 7),
    _CfprApMgmtCfgExportPolicyFsmStageOrder_Type()
)
cfprApMgmtCfgExportPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStageOrder.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStageRetry_Type = Gauge32
_CfprApMgmtCfgExportPolicyFsmStageRetry_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmStageRetry = _CfprApMgmtCfgExportPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 15, 1, 8),
    _CfprApMgmtCfgExportPolicyFsmStageRetry_Type()
)
cfprApMgmtCfgExportPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStageRetry.setStatus("current")
_CfprApMgmtCfgExportPolicyFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtCfgExportPolicyFsmStageStageStatus_Object = MibTableColumn
cfprApMgmtCfgExportPolicyFsmStageStageStatus = _CfprApMgmtCfgExportPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 15, 1, 9),
    _CfprApMgmtCfgExportPolicyFsmStageStageStatus_Type()
)
cfprApMgmtCfgExportPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCfgExportPolicyFsmStageStageStatus.setStatus("current")
_CfprApMgmtCimcSecureBootTable_Object = MibTable
cfprApMgmtCimcSecureBootTable = _CfprApMgmtCimcSecureBootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 16)
)
if mibBuilder.loadTexts:
    cfprApMgmtCimcSecureBootTable.setStatus("current")
_CfprApMgmtCimcSecureBootEntry_Object = MibTableRow
cfprApMgmtCimcSecureBootEntry = _CfprApMgmtCimcSecureBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 16, 1)
)
cfprApMgmtCimcSecureBootEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtCimcSecureBootInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtCimcSecureBootEntry.setStatus("current")
_CfprApMgmtCimcSecureBootInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtCimcSecureBootInstanceId_Object = MibTableColumn
cfprApMgmtCimcSecureBootInstanceId = _CfprApMgmtCimcSecureBootInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 16, 1, 1),
    _CfprApMgmtCimcSecureBootInstanceId_Type()
)
cfprApMgmtCimcSecureBootInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtCimcSecureBootInstanceId.setStatus("current")
_CfprApMgmtCimcSecureBootDn_Type = CfprApManagedObjectDn
_CfprApMgmtCimcSecureBootDn_Object = MibTableColumn
cfprApMgmtCimcSecureBootDn = _CfprApMgmtCimcSecureBootDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 16, 1, 2),
    _CfprApMgmtCimcSecureBootDn_Type()
)
cfprApMgmtCimcSecureBootDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCimcSecureBootDn.setStatus("current")
_CfprApMgmtCimcSecureBootRn_Type = SnmpAdminString
_CfprApMgmtCimcSecureBootRn_Object = MibTableColumn
cfprApMgmtCimcSecureBootRn = _CfprApMgmtCimcSecureBootRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 16, 1, 3),
    _CfprApMgmtCimcSecureBootRn_Type()
)
cfprApMgmtCimcSecureBootRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCimcSecureBootRn.setStatus("current")
_CfprApMgmtCimcSecureBootAdminState_Type = CfprApMgmtCimcSecureBootAdminState
_CfprApMgmtCimcSecureBootAdminState_Object = MibTableColumn
cfprApMgmtCimcSecureBootAdminState = _CfprApMgmtCimcSecureBootAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 16, 1, 4),
    _CfprApMgmtCimcSecureBootAdminState_Type()
)
cfprApMgmtCimcSecureBootAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCimcSecureBootAdminState.setStatus("current")
_CfprApMgmtCimcSecureBootOperState_Type = CfprApMgmtSecureBootOperState
_CfprApMgmtCimcSecureBootOperState_Object = MibTableColumn
cfprApMgmtCimcSecureBootOperState = _CfprApMgmtCimcSecureBootOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 16, 1, 5),
    _CfprApMgmtCimcSecureBootOperState_Type()
)
cfprApMgmtCimcSecureBootOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtCimcSecureBootOperState.setStatus("current")
_CfprApMgmtConnectionTable_Object = MibTable
cfprApMgmtConnectionTable = _CfprApMgmtConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 17)
)
if mibBuilder.loadTexts:
    cfprApMgmtConnectionTable.setStatus("current")
_CfprApMgmtConnectionEntry_Object = MibTableRow
cfprApMgmtConnectionEntry = _CfprApMgmtConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 17, 1)
)
cfprApMgmtConnectionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtConnectionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtConnectionEntry.setStatus("current")
_CfprApMgmtConnectionInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtConnectionInstanceId_Object = MibTableColumn
cfprApMgmtConnectionInstanceId = _CfprApMgmtConnectionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 17, 1, 1),
    _CfprApMgmtConnectionInstanceId_Type()
)
cfprApMgmtConnectionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtConnectionInstanceId.setStatus("current")
_CfprApMgmtConnectionDn_Type = CfprApManagedObjectDn
_CfprApMgmtConnectionDn_Object = MibTableColumn
cfprApMgmtConnectionDn = _CfprApMgmtConnectionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 17, 1, 2),
    _CfprApMgmtConnectionDn_Type()
)
cfprApMgmtConnectionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtConnectionDn.setStatus("current")
_CfprApMgmtConnectionRn_Type = SnmpAdminString
_CfprApMgmtConnectionRn_Object = MibTableColumn
cfprApMgmtConnectionRn = _CfprApMgmtConnectionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 17, 1, 3),
    _CfprApMgmtConnectionRn_Type()
)
cfprApMgmtConnectionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtConnectionRn.setStatus("current")
_CfprApMgmtConnectionAck_Type = CfprApMgmtConnectionState
_CfprApMgmtConnectionAck_Object = MibTableColumn
cfprApMgmtConnectionAck = _CfprApMgmtConnectionAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 17, 1, 4),
    _CfprApMgmtConnectionAck_Type()
)
cfprApMgmtConnectionAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtConnectionAck.setStatus("current")
_CfprApMgmtConnectionOperState_Type = CfprApMgmtConnectionState
_CfprApMgmtConnectionOperState_Object = MibTableColumn
cfprApMgmtConnectionOperState = _CfprApMgmtConnectionOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 17, 1, 5),
    _CfprApMgmtConnectionOperState_Type()
)
cfprApMgmtConnectionOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtConnectionOperState.setStatus("current")
_CfprApMgmtConnectionType_Type = CfprApMgmtSource
_CfprApMgmtConnectionType_Object = MibTableColumn
cfprApMgmtConnectionType = _CfprApMgmtConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 17, 1, 6),
    _CfprApMgmtConnectionType_Type()
)
cfprApMgmtConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtConnectionType.setStatus("current")
_CfprApMgmtControllerTable_Object = MibTable
cfprApMgmtControllerTable = _CfprApMgmtControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18)
)
if mibBuilder.loadTexts:
    cfprApMgmtControllerTable.setStatus("current")
_CfprApMgmtControllerEntry_Object = MibTableRow
cfprApMgmtControllerEntry = _CfprApMgmtControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1)
)
cfprApMgmtControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtControllerEntry.setStatus("current")
_CfprApMgmtControllerInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtControllerInstanceId_Object = MibTableColumn
cfprApMgmtControllerInstanceId = _CfprApMgmtControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 1),
    _CfprApMgmtControllerInstanceId_Type()
)
cfprApMgmtControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtControllerInstanceId.setStatus("current")
_CfprApMgmtControllerDn_Type = CfprApManagedObjectDn
_CfprApMgmtControllerDn_Object = MibTableColumn
cfprApMgmtControllerDn = _CfprApMgmtControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 2),
    _CfprApMgmtControllerDn_Type()
)
cfprApMgmtControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerDn.setStatus("current")
_CfprApMgmtControllerRn_Type = SnmpAdminString
_CfprApMgmtControllerRn_Object = MibTableColumn
cfprApMgmtControllerRn = _CfprApMgmtControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 3),
    _CfprApMgmtControllerRn_Type()
)
cfprApMgmtControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerRn.setStatus("current")
_CfprApMgmtControllerDbVersion_Type = SnmpAdminString
_CfprApMgmtControllerDbVersion_Object = MibTableColumn
cfprApMgmtControllerDbVersion = _CfprApMgmtControllerDbVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 4),
    _CfprApMgmtControllerDbVersion_Type()
)
cfprApMgmtControllerDbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerDbVersion.setStatus("current")
_CfprApMgmtControllerDimmBlacklistingOperState_Type = CfprApMgmtDimmBlacklistingOperState
_CfprApMgmtControllerDimmBlacklistingOperState_Object = MibTableColumn
cfprApMgmtControllerDimmBlacklistingOperState = _CfprApMgmtControllerDimmBlacklistingOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 5),
    _CfprApMgmtControllerDimmBlacklistingOperState_Type()
)
cfprApMgmtControllerDimmBlacklistingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerDimmBlacklistingOperState.setStatus("current")
_CfprApMgmtControllerFsmDescr_Type = SnmpAdminString
_CfprApMgmtControllerFsmDescr_Object = MibTableColumn
cfprApMgmtControllerFsmDescr = _CfprApMgmtControllerFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 6),
    _CfprApMgmtControllerFsmDescr_Type()
)
cfprApMgmtControllerFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmDescr.setStatus("current")
_CfprApMgmtControllerFsmFlags_Type = SnmpAdminString
_CfprApMgmtControllerFsmFlags_Object = MibTableColumn
cfprApMgmtControllerFsmFlags = _CfprApMgmtControllerFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 7),
    _CfprApMgmtControllerFsmFlags_Type()
)
cfprApMgmtControllerFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmFlags.setStatus("current")
_CfprApMgmtControllerFsmPrev_Type = SnmpAdminString
_CfprApMgmtControllerFsmPrev_Object = MibTableColumn
cfprApMgmtControllerFsmPrev = _CfprApMgmtControllerFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 8),
    _CfprApMgmtControllerFsmPrev_Type()
)
cfprApMgmtControllerFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmPrev.setStatus("current")
_CfprApMgmtControllerFsmProgr_Type = Gauge32
_CfprApMgmtControllerFsmProgr_Object = MibTableColumn
cfprApMgmtControllerFsmProgr = _CfprApMgmtControllerFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 9),
    _CfprApMgmtControllerFsmProgr_Type()
)
cfprApMgmtControllerFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmProgr.setStatus("current")
_CfprApMgmtControllerFsmRmtInvErrCode_Type = Gauge32
_CfprApMgmtControllerFsmRmtInvErrCode_Object = MibTableColumn
cfprApMgmtControllerFsmRmtInvErrCode = _CfprApMgmtControllerFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 10),
    _CfprApMgmtControllerFsmRmtInvErrCode_Type()
)
cfprApMgmtControllerFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmRmtInvErrCode.setStatus("current")
_CfprApMgmtControllerFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApMgmtControllerFsmRmtInvErrDescr_Object = MibTableColumn
cfprApMgmtControllerFsmRmtInvErrDescr = _CfprApMgmtControllerFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 11),
    _CfprApMgmtControllerFsmRmtInvErrDescr_Type()
)
cfprApMgmtControllerFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmRmtInvErrDescr.setStatus("current")
_CfprApMgmtControllerFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtControllerFsmRmtInvRslt_Object = MibTableColumn
cfprApMgmtControllerFsmRmtInvRslt = _CfprApMgmtControllerFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 12),
    _CfprApMgmtControllerFsmRmtInvRslt_Type()
)
cfprApMgmtControllerFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmRmtInvRslt.setStatus("current")
_CfprApMgmtControllerFsmStageDescr_Type = SnmpAdminString
_CfprApMgmtControllerFsmStageDescr_Object = MibTableColumn
cfprApMgmtControllerFsmStageDescr = _CfprApMgmtControllerFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 13),
    _CfprApMgmtControllerFsmStageDescr_Type()
)
cfprApMgmtControllerFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStageDescr.setStatus("current")
_CfprApMgmtControllerFsmStamp_Type = DateAndTime
_CfprApMgmtControllerFsmStamp_Object = MibTableColumn
cfprApMgmtControllerFsmStamp = _CfprApMgmtControllerFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 14),
    _CfprApMgmtControllerFsmStamp_Type()
)
cfprApMgmtControllerFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStamp.setStatus("current")
_CfprApMgmtControllerFsmStatus_Type = SnmpAdminString
_CfprApMgmtControllerFsmStatus_Object = MibTableColumn
cfprApMgmtControllerFsmStatus = _CfprApMgmtControllerFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 15),
    _CfprApMgmtControllerFsmStatus_Type()
)
cfprApMgmtControllerFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStatus.setStatus("current")
_CfprApMgmtControllerFsmTry_Type = Gauge32
_CfprApMgmtControllerFsmTry_Object = MibTableColumn
cfprApMgmtControllerFsmTry = _CfprApMgmtControllerFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 16),
    _CfprApMgmtControllerFsmTry_Type()
)
cfprApMgmtControllerFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmTry.setStatus("current")
_CfprApMgmtControllerGuid_Type = SnmpAdminString
_CfprApMgmtControllerGuid_Object = MibTableColumn
cfprApMgmtControllerGuid = _CfprApMgmtControllerGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 17),
    _CfprApMgmtControllerGuid_Type()
)
cfprApMgmtControllerGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerGuid.setStatus("current")
_CfprApMgmtControllerModel_Type = SnmpAdminString
_CfprApMgmtControllerModel_Object = MibTableColumn
cfprApMgmtControllerModel = _CfprApMgmtControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 18),
    _CfprApMgmtControllerModel_Type()
)
cfprApMgmtControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerModel.setStatus("current")
_CfprApMgmtControllerOperConn_Type = SnmpAdminString
_CfprApMgmtControllerOperConn_Object = MibTableColumn
cfprApMgmtControllerOperConn = _CfprApMgmtControllerOperConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 19),
    _CfprApMgmtControllerOperConn_Type()
)
cfprApMgmtControllerOperConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerOperConn.setStatus("current")
_CfprApMgmtControllerRevision_Type = SnmpAdminString
_CfprApMgmtControllerRevision_Object = MibTableColumn
cfprApMgmtControllerRevision = _CfprApMgmtControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 20),
    _CfprApMgmtControllerRevision_Type()
)
cfprApMgmtControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerRevision.setStatus("current")
_CfprApMgmtControllerSerial_Type = SnmpAdminString
_CfprApMgmtControllerSerial_Object = MibTableColumn
cfprApMgmtControllerSerial = _CfprApMgmtControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 21),
    _CfprApMgmtControllerSerial_Type()
)
cfprApMgmtControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerSerial.setStatus("current")
_CfprApMgmtControllerStorageOobInterfaceSupported_Type = TruthValue
_CfprApMgmtControllerStorageOobInterfaceSupported_Object = MibTableColumn
cfprApMgmtControllerStorageOobInterfaceSupported = _CfprApMgmtControllerStorageOobInterfaceSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 22),
    _CfprApMgmtControllerStorageOobInterfaceSupported_Type()
)
cfprApMgmtControllerStorageOobInterfaceSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerStorageOobInterfaceSupported.setStatus("current")
_CfprApMgmtControllerStorageSubsystemState_Type = CfprApMgmtStorageSubsystemState
_CfprApMgmtControllerStorageSubsystemState_Object = MibTableColumn
cfprApMgmtControllerStorageSubsystemState = _CfprApMgmtControllerStorageSubsystemState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 23),
    _CfprApMgmtControllerStorageSubsystemState_Type()
)
cfprApMgmtControllerStorageSubsystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerStorageSubsystemState.setStatus("current")
_CfprApMgmtControllerSubject_Type = CfprApMgmtSubject
_CfprApMgmtControllerSubject_Object = MibTableColumn
cfprApMgmtControllerSubject = _CfprApMgmtControllerSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 24),
    _CfprApMgmtControllerSubject_Type()
)
cfprApMgmtControllerSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerSubject.setStatus("current")
_CfprApMgmtControllerVendor_Type = SnmpAdminString
_CfprApMgmtControllerVendor_Object = MibTableColumn
cfprApMgmtControllerVendor = _CfprApMgmtControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 18, 1, 25),
    _CfprApMgmtControllerVendor_Type()
)
cfprApMgmtControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerVendor.setStatus("current")
_CfprApMgmtControllerFsmTable_Object = MibTable
cfprApMgmtControllerFsmTable = _CfprApMgmtControllerFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19)
)
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmTable.setStatus("current")
_CfprApMgmtControllerFsmEntry_Object = MibTableRow
cfprApMgmtControllerFsmEntry = _CfprApMgmtControllerFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19, 1)
)
cfprApMgmtControllerFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtControllerFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmEntry.setStatus("current")
_CfprApMgmtControllerFsmInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtControllerFsmInstanceId_Object = MibTableColumn
cfprApMgmtControllerFsmInstanceId = _CfprApMgmtControllerFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19, 1, 1),
    _CfprApMgmtControllerFsmInstanceId_Type()
)
cfprApMgmtControllerFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmInstanceId.setStatus("current")
_CfprApMgmtControllerFsmDn_Type = CfprApManagedObjectDn
_CfprApMgmtControllerFsmDn_Object = MibTableColumn
cfprApMgmtControllerFsmDn = _CfprApMgmtControllerFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19, 1, 2),
    _CfprApMgmtControllerFsmDn_Type()
)
cfprApMgmtControllerFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmDn.setStatus("current")
_CfprApMgmtControllerFsmRn_Type = SnmpAdminString
_CfprApMgmtControllerFsmRn_Object = MibTableColumn
cfprApMgmtControllerFsmRn = _CfprApMgmtControllerFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19, 1, 3),
    _CfprApMgmtControllerFsmRn_Type()
)
cfprApMgmtControllerFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmRn.setStatus("current")
_CfprApMgmtControllerFsmCompletionTime_Type = DateAndTime
_CfprApMgmtControllerFsmCompletionTime_Object = MibTableColumn
cfprApMgmtControllerFsmCompletionTime = _CfprApMgmtControllerFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19, 1, 4),
    _CfprApMgmtControllerFsmCompletionTime_Type()
)
cfprApMgmtControllerFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmCompletionTime.setStatus("current")
_CfprApMgmtControllerFsmCurrentFsm_Type = CfprApMgmtControllerFsmCurrentFsm
_CfprApMgmtControllerFsmCurrentFsm_Object = MibTableColumn
cfprApMgmtControllerFsmCurrentFsm = _CfprApMgmtControllerFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19, 1, 5),
    _CfprApMgmtControllerFsmCurrentFsm_Type()
)
cfprApMgmtControllerFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmCurrentFsm.setStatus("current")
_CfprApMgmtControllerFsmDescrData_Type = SnmpAdminString
_CfprApMgmtControllerFsmDescrData_Object = MibTableColumn
cfprApMgmtControllerFsmDescrData = _CfprApMgmtControllerFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19, 1, 6),
    _CfprApMgmtControllerFsmDescrData_Type()
)
cfprApMgmtControllerFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmDescrData.setStatus("current")
_CfprApMgmtControllerFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtControllerFsmFsmStatus_Object = MibTableColumn
cfprApMgmtControllerFsmFsmStatus = _CfprApMgmtControllerFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19, 1, 7),
    _CfprApMgmtControllerFsmFsmStatus_Type()
)
cfprApMgmtControllerFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmFsmStatus.setStatus("current")
_CfprApMgmtControllerFsmProgress_Type = Gauge32
_CfprApMgmtControllerFsmProgress_Object = MibTableColumn
cfprApMgmtControllerFsmProgress = _CfprApMgmtControllerFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19, 1, 8),
    _CfprApMgmtControllerFsmProgress_Type()
)
cfprApMgmtControllerFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmProgress.setStatus("current")
_CfprApMgmtControllerFsmRmtErrCode_Type = Gauge32
_CfprApMgmtControllerFsmRmtErrCode_Object = MibTableColumn
cfprApMgmtControllerFsmRmtErrCode = _CfprApMgmtControllerFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19, 1, 9),
    _CfprApMgmtControllerFsmRmtErrCode_Type()
)
cfprApMgmtControllerFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmRmtErrCode.setStatus("current")
_CfprApMgmtControllerFsmRmtErrDescr_Type = SnmpAdminString
_CfprApMgmtControllerFsmRmtErrDescr_Object = MibTableColumn
cfprApMgmtControllerFsmRmtErrDescr = _CfprApMgmtControllerFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19, 1, 10),
    _CfprApMgmtControllerFsmRmtErrDescr_Type()
)
cfprApMgmtControllerFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmRmtErrDescr.setStatus("current")
_CfprApMgmtControllerFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtControllerFsmRmtRslt_Object = MibTableColumn
cfprApMgmtControllerFsmRmtRslt = _CfprApMgmtControllerFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 19, 1, 11),
    _CfprApMgmtControllerFsmRmtRslt_Type()
)
cfprApMgmtControllerFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmRmtRslt.setStatus("current")
_CfprApMgmtControllerFsmStageTable_Object = MibTable
cfprApMgmtControllerFsmStageTable = _CfprApMgmtControllerFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 20)
)
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStageTable.setStatus("current")
_CfprApMgmtControllerFsmStageEntry_Object = MibTableRow
cfprApMgmtControllerFsmStageEntry = _CfprApMgmtControllerFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 20, 1)
)
cfprApMgmtControllerFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtControllerFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStageEntry.setStatus("current")
_CfprApMgmtControllerFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtControllerFsmStageInstanceId_Object = MibTableColumn
cfprApMgmtControllerFsmStageInstanceId = _CfprApMgmtControllerFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 20, 1, 1),
    _CfprApMgmtControllerFsmStageInstanceId_Type()
)
cfprApMgmtControllerFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStageInstanceId.setStatus("current")
_CfprApMgmtControllerFsmStageDn_Type = CfprApManagedObjectDn
_CfprApMgmtControllerFsmStageDn_Object = MibTableColumn
cfprApMgmtControllerFsmStageDn = _CfprApMgmtControllerFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 20, 1, 2),
    _CfprApMgmtControllerFsmStageDn_Type()
)
cfprApMgmtControllerFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStageDn.setStatus("current")
_CfprApMgmtControllerFsmStageRn_Type = SnmpAdminString
_CfprApMgmtControllerFsmStageRn_Object = MibTableColumn
cfprApMgmtControllerFsmStageRn = _CfprApMgmtControllerFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 20, 1, 3),
    _CfprApMgmtControllerFsmStageRn_Type()
)
cfprApMgmtControllerFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStageRn.setStatus("current")
_CfprApMgmtControllerFsmStageDescrData_Type = SnmpAdminString
_CfprApMgmtControllerFsmStageDescrData_Object = MibTableColumn
cfprApMgmtControllerFsmStageDescrData = _CfprApMgmtControllerFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 20, 1, 4),
    _CfprApMgmtControllerFsmStageDescrData_Type()
)
cfprApMgmtControllerFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStageDescrData.setStatus("current")
_CfprApMgmtControllerFsmStageLastUpdateTime_Type = DateAndTime
_CfprApMgmtControllerFsmStageLastUpdateTime_Object = MibTableColumn
cfprApMgmtControllerFsmStageLastUpdateTime = _CfprApMgmtControllerFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 20, 1, 5),
    _CfprApMgmtControllerFsmStageLastUpdateTime_Type()
)
cfprApMgmtControllerFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStageLastUpdateTime.setStatus("current")
_CfprApMgmtControllerFsmStageName_Type = CfprApMgmtControllerFsmStageName
_CfprApMgmtControllerFsmStageName_Object = MibTableColumn
cfprApMgmtControllerFsmStageName = _CfprApMgmtControllerFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 20, 1, 6),
    _CfprApMgmtControllerFsmStageName_Type()
)
cfprApMgmtControllerFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStageName.setStatus("current")
_CfprApMgmtControllerFsmStageOrder_Type = Gauge32
_CfprApMgmtControllerFsmStageOrder_Object = MibTableColumn
cfprApMgmtControllerFsmStageOrder = _CfprApMgmtControllerFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 20, 1, 7),
    _CfprApMgmtControllerFsmStageOrder_Type()
)
cfprApMgmtControllerFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStageOrder.setStatus("current")
_CfprApMgmtControllerFsmStageRetry_Type = Gauge32
_CfprApMgmtControllerFsmStageRetry_Object = MibTableColumn
cfprApMgmtControllerFsmStageRetry = _CfprApMgmtControllerFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 20, 1, 8),
    _CfprApMgmtControllerFsmStageRetry_Type()
)
cfprApMgmtControllerFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStageRetry.setStatus("current")
_CfprApMgmtControllerFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtControllerFsmStageStageStatus_Object = MibTableColumn
cfprApMgmtControllerFsmStageStageStatus = _CfprApMgmtControllerFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 20, 1, 9),
    _CfprApMgmtControllerFsmStageStageStatus_Type()
)
cfprApMgmtControllerFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmStageStageStatus.setStatus("current")
_CfprApMgmtControllerFsmTaskTable_Object = MibTable
cfprApMgmtControllerFsmTaskTable = _CfprApMgmtControllerFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 21)
)
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmTaskTable.setStatus("current")
_CfprApMgmtControllerFsmTaskEntry_Object = MibTableRow
cfprApMgmtControllerFsmTaskEntry = _CfprApMgmtControllerFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 21, 1)
)
cfprApMgmtControllerFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtControllerFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmTaskEntry.setStatus("current")
_CfprApMgmtControllerFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtControllerFsmTaskInstanceId_Object = MibTableColumn
cfprApMgmtControllerFsmTaskInstanceId = _CfprApMgmtControllerFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 21, 1, 1),
    _CfprApMgmtControllerFsmTaskInstanceId_Type()
)
cfprApMgmtControllerFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmTaskInstanceId.setStatus("current")
_CfprApMgmtControllerFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApMgmtControllerFsmTaskDn_Object = MibTableColumn
cfprApMgmtControllerFsmTaskDn = _CfprApMgmtControllerFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 21, 1, 2),
    _CfprApMgmtControllerFsmTaskDn_Type()
)
cfprApMgmtControllerFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmTaskDn.setStatus("current")
_CfprApMgmtControllerFsmTaskRn_Type = SnmpAdminString
_CfprApMgmtControllerFsmTaskRn_Object = MibTableColumn
cfprApMgmtControllerFsmTaskRn = _CfprApMgmtControllerFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 21, 1, 3),
    _CfprApMgmtControllerFsmTaskRn_Type()
)
cfprApMgmtControllerFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmTaskRn.setStatus("current")
_CfprApMgmtControllerFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApMgmtControllerFsmTaskCompletion_Object = MibTableColumn
cfprApMgmtControllerFsmTaskCompletion = _CfprApMgmtControllerFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 21, 1, 4),
    _CfprApMgmtControllerFsmTaskCompletion_Type()
)
cfprApMgmtControllerFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmTaskCompletion.setStatus("current")
_CfprApMgmtControllerFsmTaskFlags_Type = CfprApMgmtControllerFsmTaskFlags
_CfprApMgmtControllerFsmTaskFlags_Object = MibTableColumn
cfprApMgmtControllerFsmTaskFlags = _CfprApMgmtControllerFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 21, 1, 5),
    _CfprApMgmtControllerFsmTaskFlags_Type()
)
cfprApMgmtControllerFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmTaskFlags.setStatus("current")
_CfprApMgmtControllerFsmTaskItem_Type = CfprApMgmtControllerFsmTaskItem
_CfprApMgmtControllerFsmTaskItem_Object = MibTableColumn
cfprApMgmtControllerFsmTaskItem = _CfprApMgmtControllerFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 21, 1, 6),
    _CfprApMgmtControllerFsmTaskItem_Type()
)
cfprApMgmtControllerFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmTaskItem.setStatus("current")
_CfprApMgmtControllerFsmTaskSeqId_Type = Gauge32
_CfprApMgmtControllerFsmTaskSeqId_Object = MibTableColumn
cfprApMgmtControllerFsmTaskSeqId = _CfprApMgmtControllerFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 21, 1, 7),
    _CfprApMgmtControllerFsmTaskSeqId_Type()
)
cfprApMgmtControllerFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtControllerFsmTaskSeqId.setStatus("current")
_CfprApMgmtEntityTable_Object = MibTable
cfprApMgmtEntityTable = _CfprApMgmtEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22)
)
if mibBuilder.loadTexts:
    cfprApMgmtEntityTable.setStatus("current")
_CfprApMgmtEntityEntry_Object = MibTableRow
cfprApMgmtEntityEntry = _CfprApMgmtEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1)
)
cfprApMgmtEntityEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtEntityInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtEntityEntry.setStatus("current")
_CfprApMgmtEntityInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtEntityInstanceId_Object = MibTableColumn
cfprApMgmtEntityInstanceId = _CfprApMgmtEntityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 1),
    _CfprApMgmtEntityInstanceId_Type()
)
cfprApMgmtEntityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtEntityInstanceId.setStatus("current")
_CfprApMgmtEntityDn_Type = CfprApManagedObjectDn
_CfprApMgmtEntityDn_Object = MibTableColumn
cfprApMgmtEntityDn = _CfprApMgmtEntityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 2),
    _CfprApMgmtEntityDn_Type()
)
cfprApMgmtEntityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityDn.setStatus("current")
_CfprApMgmtEntityRn_Type = SnmpAdminString
_CfprApMgmtEntityRn_Object = MibTableColumn
cfprApMgmtEntityRn = _CfprApMgmtEntityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 3),
    _CfprApMgmtEntityRn_Type()
)
cfprApMgmtEntityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityRn.setStatus("current")
_CfprApMgmtEntityChassis1_Type = SnmpAdminString
_CfprApMgmtEntityChassis1_Object = MibTableColumn
cfprApMgmtEntityChassis1 = _CfprApMgmtEntityChassis1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 4),
    _CfprApMgmtEntityChassis1_Type()
)
cfprApMgmtEntityChassis1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityChassis1.setStatus("current")
_CfprApMgmtEntityChassis2_Type = SnmpAdminString
_CfprApMgmtEntityChassis2_Object = MibTableColumn
cfprApMgmtEntityChassis2 = _CfprApMgmtEntityChassis2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 5),
    _CfprApMgmtEntityChassis2_Type()
)
cfprApMgmtEntityChassis2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityChassis2.setStatus("current")
_CfprApMgmtEntityChassis3_Type = SnmpAdminString
_CfprApMgmtEntityChassis3_Object = MibTableColumn
cfprApMgmtEntityChassis3 = _CfprApMgmtEntityChassis3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 6),
    _CfprApMgmtEntityChassis3_Type()
)
cfprApMgmtEntityChassis3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityChassis3.setStatus("current")
_CfprApMgmtEntityChassisDeviceIoState1_Type = CfprApMgmtEntityChassisDeviceIoState1
_CfprApMgmtEntityChassisDeviceIoState1_Object = MibTableColumn
cfprApMgmtEntityChassisDeviceIoState1 = _CfprApMgmtEntityChassisDeviceIoState1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 7),
    _CfprApMgmtEntityChassisDeviceIoState1_Type()
)
cfprApMgmtEntityChassisDeviceIoState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityChassisDeviceIoState1.setStatus("current")
_CfprApMgmtEntityChassisDeviceIoState2_Type = CfprApMgmtEntityChassisDeviceIoState2
_CfprApMgmtEntityChassisDeviceIoState2_Object = MibTableColumn
cfprApMgmtEntityChassisDeviceIoState2 = _CfprApMgmtEntityChassisDeviceIoState2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 8),
    _CfprApMgmtEntityChassisDeviceIoState2_Type()
)
cfprApMgmtEntityChassisDeviceIoState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityChassisDeviceIoState2.setStatus("current")
_CfprApMgmtEntityChassisDeviceIoState3_Type = CfprApMgmtEntityChassisDeviceIoState3
_CfprApMgmtEntityChassisDeviceIoState3_Object = MibTableColumn
cfprApMgmtEntityChassisDeviceIoState3 = _CfprApMgmtEntityChassisDeviceIoState3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 9),
    _CfprApMgmtEntityChassisDeviceIoState3_Type()
)
cfprApMgmtEntityChassisDeviceIoState3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityChassisDeviceIoState3.setStatus("current")
_CfprApMgmtEntityHaFailureReason_Type = CfprApMgmtEntityHaFailureReason
_CfprApMgmtEntityHaFailureReason_Object = MibTableColumn
cfprApMgmtEntityHaFailureReason = _CfprApMgmtEntityHaFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 10),
    _CfprApMgmtEntityHaFailureReason_Type()
)
cfprApMgmtEntityHaFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityHaFailureReason.setStatus("current")
_CfprApMgmtEntityHaReadiness_Type = CfprApMgmtEntityHaReadiness
_CfprApMgmtEntityHaReadiness_Object = MibTableColumn
cfprApMgmtEntityHaReadiness = _CfprApMgmtEntityHaReadiness_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 11),
    _CfprApMgmtEntityHaReadiness_Type()
)
cfprApMgmtEntityHaReadiness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityHaReadiness.setStatus("current")
_CfprApMgmtEntityHaReady_Type = TruthValue
_CfprApMgmtEntityHaReady_Object = MibTableColumn
cfprApMgmtEntityHaReady = _CfprApMgmtEntityHaReady_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 12),
    _CfprApMgmtEntityHaReady_Type()
)
cfprApMgmtEntityHaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityHaReady.setStatus("current")
_CfprApMgmtEntityId_Type = CfprApNetworkSwitchId
_CfprApMgmtEntityId_Object = MibTableColumn
cfprApMgmtEntityId = _CfprApMgmtEntityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 13),
    _CfprApMgmtEntityId_Type()
)
cfprApMgmtEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityId.setStatus("current")
_CfprApMgmtEntityLeadership_Type = CfprApMgmtEntityLeadership
_CfprApMgmtEntityLeadership_Object = MibTableColumn
cfprApMgmtEntityLeadership = _CfprApMgmtEntityLeadership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 14),
    _CfprApMgmtEntityLeadership_Type()
)
cfprApMgmtEntityLeadership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityLeadership.setStatus("current")
_CfprApMgmtEntityMgmtServicesState_Type = CfprApMgmtEntityMgmtServicesState
_CfprApMgmtEntityMgmtServicesState_Object = MibTableColumn
cfprApMgmtEntityMgmtServicesState = _CfprApMgmtEntityMgmtServicesState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 15),
    _CfprApMgmtEntityMgmtServicesState_Type()
)
cfprApMgmtEntityMgmtServicesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityMgmtServicesState.setStatus("current")
_CfprApMgmtEntityProblems_Type = CfprApMgmtEntityProblems
_CfprApMgmtEntityProblems_Object = MibTableColumn
cfprApMgmtEntityProblems = _CfprApMgmtEntityProblems_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 16),
    _CfprApMgmtEntityProblems_Type()
)
cfprApMgmtEntityProblems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityProblems.setStatus("current")
_CfprApMgmtEntitySshAuthKeysCsum_Type = SnmpAdminString
_CfprApMgmtEntitySshAuthKeysCsum_Object = MibTableColumn
cfprApMgmtEntitySshAuthKeysCsum = _CfprApMgmtEntitySshAuthKeysCsum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 17),
    _CfprApMgmtEntitySshAuthKeysCsum_Type()
)
cfprApMgmtEntitySshAuthKeysCsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntitySshAuthKeysCsum.setStatus("current")
_CfprApMgmtEntitySshAuthKeysSize_Type = Unsigned64
_CfprApMgmtEntitySshAuthKeysSize_Object = MibTableColumn
cfprApMgmtEntitySshAuthKeysSize = _CfprApMgmtEntitySshAuthKeysSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 18),
    _CfprApMgmtEntitySshAuthKeysSize_Type()
)
cfprApMgmtEntitySshAuthKeysSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntitySshAuthKeysSize.setStatus("current")
_CfprApMgmtEntitySshKeyStatus_Type = Unsigned64
_CfprApMgmtEntitySshKeyStatus_Object = MibTableColumn
cfprApMgmtEntitySshKeyStatus = _CfprApMgmtEntitySshKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 19),
    _CfprApMgmtEntitySshKeyStatus_Type()
)
cfprApMgmtEntitySshKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntitySshKeyStatus.setStatus("current")
_CfprApMgmtEntitySshRootPubKeyCsum_Type = SnmpAdminString
_CfprApMgmtEntitySshRootPubKeyCsum_Object = MibTableColumn
cfprApMgmtEntitySshRootPubKeyCsum = _CfprApMgmtEntitySshRootPubKeyCsum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 20),
    _CfprApMgmtEntitySshRootPubKeyCsum_Type()
)
cfprApMgmtEntitySshRootPubKeyCsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntitySshRootPubKeyCsum.setStatus("current")
_CfprApMgmtEntitySshRootPubKeySize_Type = Unsigned64
_CfprApMgmtEntitySshRootPubKeySize_Object = MibTableColumn
cfprApMgmtEntitySshRootPubKeySize = _CfprApMgmtEntitySshRootPubKeySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 21),
    _CfprApMgmtEntitySshRootPubKeySize_Type()
)
cfprApMgmtEntitySshRootPubKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntitySshRootPubKeySize.setStatus("current")
_CfprApMgmtEntityState_Type = CfprApMgmtEntityState
_CfprApMgmtEntityState_Object = MibTableColumn
cfprApMgmtEntityState = _CfprApMgmtEntityState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 22),
    _CfprApMgmtEntityState_Type()
)
cfprApMgmtEntityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityState.setStatus("current")
_CfprApMgmtEntityUmbilicalState_Type = CfprApMgmtEntityUmbilicalState
_CfprApMgmtEntityUmbilicalState_Object = MibTableColumn
cfprApMgmtEntityUmbilicalState = _CfprApMgmtEntityUmbilicalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 23),
    _CfprApMgmtEntityUmbilicalState_Type()
)
cfprApMgmtEntityUmbilicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityUmbilicalState.setStatus("current")
_CfprApMgmtEntityVersionMismatch_Type = TruthValue
_CfprApMgmtEntityVersionMismatch_Object = MibTableColumn
cfprApMgmtEntityVersionMismatch = _CfprApMgmtEntityVersionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 22, 1, 24),
    _CfprApMgmtEntityVersionMismatch_Type()
)
cfprApMgmtEntityVersionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtEntityVersionMismatch.setStatus("current")
_CfprApMgmtExportPolicyFsmTable_Object = MibTable
cfprApMgmtExportPolicyFsmTable = _CfprApMgmtExportPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23)
)
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmTable.setStatus("current")
_CfprApMgmtExportPolicyFsmEntry_Object = MibTableRow
cfprApMgmtExportPolicyFsmEntry = _CfprApMgmtExportPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23, 1)
)
cfprApMgmtExportPolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtExportPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmEntry.setStatus("current")
_CfprApMgmtExportPolicyFsmInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtExportPolicyFsmInstanceId_Object = MibTableColumn
cfprApMgmtExportPolicyFsmInstanceId = _CfprApMgmtExportPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23, 1, 1),
    _CfprApMgmtExportPolicyFsmInstanceId_Type()
)
cfprApMgmtExportPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmInstanceId.setStatus("current")
_CfprApMgmtExportPolicyFsmDn_Type = CfprApManagedObjectDn
_CfprApMgmtExportPolicyFsmDn_Object = MibTableColumn
cfprApMgmtExportPolicyFsmDn = _CfprApMgmtExportPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23, 1, 2),
    _CfprApMgmtExportPolicyFsmDn_Type()
)
cfprApMgmtExportPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmDn.setStatus("current")
_CfprApMgmtExportPolicyFsmRn_Type = SnmpAdminString
_CfprApMgmtExportPolicyFsmRn_Object = MibTableColumn
cfprApMgmtExportPolicyFsmRn = _CfprApMgmtExportPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23, 1, 3),
    _CfprApMgmtExportPolicyFsmRn_Type()
)
cfprApMgmtExportPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmRn.setStatus("current")
_CfprApMgmtExportPolicyFsmCompletionTime_Type = DateAndTime
_CfprApMgmtExportPolicyFsmCompletionTime_Object = MibTableColumn
cfprApMgmtExportPolicyFsmCompletionTime = _CfprApMgmtExportPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23, 1, 4),
    _CfprApMgmtExportPolicyFsmCompletionTime_Type()
)
cfprApMgmtExportPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmCompletionTime.setStatus("current")
_CfprApMgmtExportPolicyFsmCurrentFsm_Type = CfprApMgmtExportPolicyFsmCurrentFsm
_CfprApMgmtExportPolicyFsmCurrentFsm_Object = MibTableColumn
cfprApMgmtExportPolicyFsmCurrentFsm = _CfprApMgmtExportPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23, 1, 5),
    _CfprApMgmtExportPolicyFsmCurrentFsm_Type()
)
cfprApMgmtExportPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmCurrentFsm.setStatus("current")
_CfprApMgmtExportPolicyFsmDescr_Type = SnmpAdminString
_CfprApMgmtExportPolicyFsmDescr_Object = MibTableColumn
cfprApMgmtExportPolicyFsmDescr = _CfprApMgmtExportPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23, 1, 6),
    _CfprApMgmtExportPolicyFsmDescr_Type()
)
cfprApMgmtExportPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmDescr.setStatus("current")
_CfprApMgmtExportPolicyFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtExportPolicyFsmFsmStatus_Object = MibTableColumn
cfprApMgmtExportPolicyFsmFsmStatus = _CfprApMgmtExportPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23, 1, 7),
    _CfprApMgmtExportPolicyFsmFsmStatus_Type()
)
cfprApMgmtExportPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmFsmStatus.setStatus("current")
_CfprApMgmtExportPolicyFsmProgress_Type = Gauge32
_CfprApMgmtExportPolicyFsmProgress_Object = MibTableColumn
cfprApMgmtExportPolicyFsmProgress = _CfprApMgmtExportPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23, 1, 8),
    _CfprApMgmtExportPolicyFsmProgress_Type()
)
cfprApMgmtExportPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmProgress.setStatus("current")
_CfprApMgmtExportPolicyFsmRmtErrCode_Type = Gauge32
_CfprApMgmtExportPolicyFsmRmtErrCode_Object = MibTableColumn
cfprApMgmtExportPolicyFsmRmtErrCode = _CfprApMgmtExportPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23, 1, 9),
    _CfprApMgmtExportPolicyFsmRmtErrCode_Type()
)
cfprApMgmtExportPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmRmtErrCode.setStatus("current")
_CfprApMgmtExportPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprApMgmtExportPolicyFsmRmtErrDescr_Object = MibTableColumn
cfprApMgmtExportPolicyFsmRmtErrDescr = _CfprApMgmtExportPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23, 1, 10),
    _CfprApMgmtExportPolicyFsmRmtErrDescr_Type()
)
cfprApMgmtExportPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmRmtErrDescr.setStatus("current")
_CfprApMgmtExportPolicyFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtExportPolicyFsmRmtRslt_Object = MibTableColumn
cfprApMgmtExportPolicyFsmRmtRslt = _CfprApMgmtExportPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 23, 1, 11),
    _CfprApMgmtExportPolicyFsmRmtRslt_Type()
)
cfprApMgmtExportPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmRmtRslt.setStatus("current")
_CfprApMgmtExportPolicyFsmStageTable_Object = MibTable
cfprApMgmtExportPolicyFsmStageTable = _CfprApMgmtExportPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 24)
)
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmStageTable.setStatus("current")
_CfprApMgmtExportPolicyFsmStageEntry_Object = MibTableRow
cfprApMgmtExportPolicyFsmStageEntry = _CfprApMgmtExportPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 24, 1)
)
cfprApMgmtExportPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtExportPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmStageEntry.setStatus("current")
_CfprApMgmtExportPolicyFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtExportPolicyFsmStageInstanceId_Object = MibTableColumn
cfprApMgmtExportPolicyFsmStageInstanceId = _CfprApMgmtExportPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 24, 1, 1),
    _CfprApMgmtExportPolicyFsmStageInstanceId_Type()
)
cfprApMgmtExportPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmStageInstanceId.setStatus("current")
_CfprApMgmtExportPolicyFsmStageDn_Type = CfprApManagedObjectDn
_CfprApMgmtExportPolicyFsmStageDn_Object = MibTableColumn
cfprApMgmtExportPolicyFsmStageDn = _CfprApMgmtExportPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 24, 1, 2),
    _CfprApMgmtExportPolicyFsmStageDn_Type()
)
cfprApMgmtExportPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmStageDn.setStatus("current")
_CfprApMgmtExportPolicyFsmStageRn_Type = SnmpAdminString
_CfprApMgmtExportPolicyFsmStageRn_Object = MibTableColumn
cfprApMgmtExportPolicyFsmStageRn = _CfprApMgmtExportPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 24, 1, 3),
    _CfprApMgmtExportPolicyFsmStageRn_Type()
)
cfprApMgmtExportPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmStageRn.setStatus("current")
_CfprApMgmtExportPolicyFsmStageDescr_Type = SnmpAdminString
_CfprApMgmtExportPolicyFsmStageDescr_Object = MibTableColumn
cfprApMgmtExportPolicyFsmStageDescr = _CfprApMgmtExportPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 24, 1, 4),
    _CfprApMgmtExportPolicyFsmStageDescr_Type()
)
cfprApMgmtExportPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmStageDescr.setStatus("current")
_CfprApMgmtExportPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprApMgmtExportPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprApMgmtExportPolicyFsmStageLastUpdateTime = _CfprApMgmtExportPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 24, 1, 5),
    _CfprApMgmtExportPolicyFsmStageLastUpdateTime_Type()
)
cfprApMgmtExportPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmStageLastUpdateTime.setStatus("current")
_CfprApMgmtExportPolicyFsmStageName_Type = CfprApMgmtExportPolicyFsmStageName
_CfprApMgmtExportPolicyFsmStageName_Object = MibTableColumn
cfprApMgmtExportPolicyFsmStageName = _CfprApMgmtExportPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 24, 1, 6),
    _CfprApMgmtExportPolicyFsmStageName_Type()
)
cfprApMgmtExportPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmStageName.setStatus("current")
_CfprApMgmtExportPolicyFsmStageOrder_Type = Gauge32
_CfprApMgmtExportPolicyFsmStageOrder_Object = MibTableColumn
cfprApMgmtExportPolicyFsmStageOrder = _CfprApMgmtExportPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 24, 1, 7),
    _CfprApMgmtExportPolicyFsmStageOrder_Type()
)
cfprApMgmtExportPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmStageOrder.setStatus("current")
_CfprApMgmtExportPolicyFsmStageRetry_Type = Gauge32
_CfprApMgmtExportPolicyFsmStageRetry_Object = MibTableColumn
cfprApMgmtExportPolicyFsmStageRetry = _CfprApMgmtExportPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 24, 1, 8),
    _CfprApMgmtExportPolicyFsmStageRetry_Type()
)
cfprApMgmtExportPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmStageRetry.setStatus("current")
_CfprApMgmtExportPolicyFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtExportPolicyFsmStageStageStatus_Object = MibTableColumn
cfprApMgmtExportPolicyFsmStageStageStatus = _CfprApMgmtExportPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 24, 1, 9),
    _CfprApMgmtExportPolicyFsmStageStageStatus_Type()
)
cfprApMgmtExportPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmStageStageStatus.setStatus("current")
_CfprApMgmtExportPolicyFsmTaskTable_Object = MibTable
cfprApMgmtExportPolicyFsmTaskTable = _CfprApMgmtExportPolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 25)
)
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmTaskTable.setStatus("current")
_CfprApMgmtExportPolicyFsmTaskEntry_Object = MibTableRow
cfprApMgmtExportPolicyFsmTaskEntry = _CfprApMgmtExportPolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 25, 1)
)
cfprApMgmtExportPolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtExportPolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmTaskEntry.setStatus("current")
_CfprApMgmtExportPolicyFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtExportPolicyFsmTaskInstanceId_Object = MibTableColumn
cfprApMgmtExportPolicyFsmTaskInstanceId = _CfprApMgmtExportPolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 25, 1, 1),
    _CfprApMgmtExportPolicyFsmTaskInstanceId_Type()
)
cfprApMgmtExportPolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmTaskInstanceId.setStatus("current")
_CfprApMgmtExportPolicyFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApMgmtExportPolicyFsmTaskDn_Object = MibTableColumn
cfprApMgmtExportPolicyFsmTaskDn = _CfprApMgmtExportPolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 25, 1, 2),
    _CfprApMgmtExportPolicyFsmTaskDn_Type()
)
cfprApMgmtExportPolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmTaskDn.setStatus("current")
_CfprApMgmtExportPolicyFsmTaskRn_Type = SnmpAdminString
_CfprApMgmtExportPolicyFsmTaskRn_Object = MibTableColumn
cfprApMgmtExportPolicyFsmTaskRn = _CfprApMgmtExportPolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 25, 1, 3),
    _CfprApMgmtExportPolicyFsmTaskRn_Type()
)
cfprApMgmtExportPolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmTaskRn.setStatus("current")
_CfprApMgmtExportPolicyFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApMgmtExportPolicyFsmTaskCompletion_Object = MibTableColumn
cfprApMgmtExportPolicyFsmTaskCompletion = _CfprApMgmtExportPolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 25, 1, 4),
    _CfprApMgmtExportPolicyFsmTaskCompletion_Type()
)
cfprApMgmtExportPolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmTaskCompletion.setStatus("current")
_CfprApMgmtExportPolicyFsmTaskFlags_Type = CfprApFsmFlags
_CfprApMgmtExportPolicyFsmTaskFlags_Object = MibTableColumn
cfprApMgmtExportPolicyFsmTaskFlags = _CfprApMgmtExportPolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 25, 1, 5),
    _CfprApMgmtExportPolicyFsmTaskFlags_Type()
)
cfprApMgmtExportPolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmTaskFlags.setStatus("current")
_CfprApMgmtExportPolicyFsmTaskItem_Type = CfprApMgmtExportPolicyFsmTaskItem
_CfprApMgmtExportPolicyFsmTaskItem_Object = MibTableColumn
cfprApMgmtExportPolicyFsmTaskItem = _CfprApMgmtExportPolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 25, 1, 6),
    _CfprApMgmtExportPolicyFsmTaskItem_Type()
)
cfprApMgmtExportPolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmTaskItem.setStatus("current")
_CfprApMgmtExportPolicyFsmTaskSeqId_Type = Gauge32
_CfprApMgmtExportPolicyFsmTaskSeqId_Object = MibTableColumn
cfprApMgmtExportPolicyFsmTaskSeqId = _CfprApMgmtExportPolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 25, 1, 7),
    _CfprApMgmtExportPolicyFsmTaskSeqId_Type()
)
cfprApMgmtExportPolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtExportPolicyFsmTaskSeqId.setStatus("current")
_CfprApMgmtIPv6IfAddrTable_Object = MibTable
cfprApMgmtIPv6IfAddrTable = _CfprApMgmtIPv6IfAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26)
)
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrTable.setStatus("current")
_CfprApMgmtIPv6IfAddrEntry_Object = MibTableRow
cfprApMgmtIPv6IfAddrEntry = _CfprApMgmtIPv6IfAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1)
)
cfprApMgmtIPv6IfAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtIPv6IfAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrEntry.setStatus("current")
_CfprApMgmtIPv6IfAddrInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtIPv6IfAddrInstanceId_Object = MibTableColumn
cfprApMgmtIPv6IfAddrInstanceId = _CfprApMgmtIPv6IfAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 1),
    _CfprApMgmtIPv6IfAddrInstanceId_Type()
)
cfprApMgmtIPv6IfAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrInstanceId.setStatus("current")
_CfprApMgmtIPv6IfAddrDn_Type = CfprApManagedObjectDn
_CfprApMgmtIPv6IfAddrDn_Object = MibTableColumn
cfprApMgmtIPv6IfAddrDn = _CfprApMgmtIPv6IfAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 2),
    _CfprApMgmtIPv6IfAddrDn_Type()
)
cfprApMgmtIPv6IfAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrDn.setStatus("current")
_CfprApMgmtIPv6IfAddrRn_Type = SnmpAdminString
_CfprApMgmtIPv6IfAddrRn_Object = MibTableColumn
cfprApMgmtIPv6IfAddrRn = _CfprApMgmtIPv6IfAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 3),
    _CfprApMgmtIPv6IfAddrRn_Type()
)
cfprApMgmtIPv6IfAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrRn.setStatus("current")
_CfprApMgmtIPv6IfAddrAddr_Type = InetAddressIPv6
_CfprApMgmtIPv6IfAddrAddr_Object = MibTableColumn
cfprApMgmtIPv6IfAddrAddr = _CfprApMgmtIPv6IfAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 4),
    _CfprApMgmtIPv6IfAddrAddr_Type()
)
cfprApMgmtIPv6IfAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrAddr.setStatus("current")
_CfprApMgmtIPv6IfAddrDefGw_Type = InetAddressIPv6
_CfprApMgmtIPv6IfAddrDefGw_Object = MibTableColumn
cfprApMgmtIPv6IfAddrDefGw = _CfprApMgmtIPv6IfAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 5),
    _CfprApMgmtIPv6IfAddrDefGw_Type()
)
cfprApMgmtIPv6IfAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrDefGw.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmDescr_Type = SnmpAdminString
_CfprApMgmtIPv6IfAddrFsmDescr_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmDescr = _CfprApMgmtIPv6IfAddrFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 6),
    _CfprApMgmtIPv6IfAddrFsmDescr_Type()
)
cfprApMgmtIPv6IfAddrFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmDescr.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmPrev_Type = SnmpAdminString
_CfprApMgmtIPv6IfAddrFsmPrev_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmPrev = _CfprApMgmtIPv6IfAddrFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 7),
    _CfprApMgmtIPv6IfAddrFsmPrev_Type()
)
cfprApMgmtIPv6IfAddrFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmPrev.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmProgr_Type = Gauge32
_CfprApMgmtIPv6IfAddrFsmProgr_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmProgr = _CfprApMgmtIPv6IfAddrFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 8),
    _CfprApMgmtIPv6IfAddrFsmProgr_Type()
)
cfprApMgmtIPv6IfAddrFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmProgr.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmRmtInvErrCode_Type = Gauge32
_CfprApMgmtIPv6IfAddrFsmRmtInvErrCode_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmRmtInvErrCode = _CfprApMgmtIPv6IfAddrFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 9),
    _CfprApMgmtIPv6IfAddrFsmRmtInvErrCode_Type()
)
cfprApMgmtIPv6IfAddrFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmRmtInvErrCode.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApMgmtIPv6IfAddrFsmRmtInvErrDescr_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmRmtInvErrDescr = _CfprApMgmtIPv6IfAddrFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 10),
    _CfprApMgmtIPv6IfAddrFsmRmtInvErrDescr_Type()
)
cfprApMgmtIPv6IfAddrFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmRmtInvErrDescr.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtIPv6IfAddrFsmRmtInvRslt_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmRmtInvRslt = _CfprApMgmtIPv6IfAddrFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 11),
    _CfprApMgmtIPv6IfAddrFsmRmtInvRslt_Type()
)
cfprApMgmtIPv6IfAddrFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmRmtInvRslt.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStageDescr_Type = SnmpAdminString
_CfprApMgmtIPv6IfAddrFsmStageDescr_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmStageDescr = _CfprApMgmtIPv6IfAddrFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 12),
    _CfprApMgmtIPv6IfAddrFsmStageDescr_Type()
)
cfprApMgmtIPv6IfAddrFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStageDescr.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStamp_Type = DateAndTime
_CfprApMgmtIPv6IfAddrFsmStamp_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmStamp = _CfprApMgmtIPv6IfAddrFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 13),
    _CfprApMgmtIPv6IfAddrFsmStamp_Type()
)
cfprApMgmtIPv6IfAddrFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStamp.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStatus_Type = SnmpAdminString
_CfprApMgmtIPv6IfAddrFsmStatus_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmStatus = _CfprApMgmtIPv6IfAddrFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 14),
    _CfprApMgmtIPv6IfAddrFsmStatus_Type()
)
cfprApMgmtIPv6IfAddrFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStatus.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmTry_Type = Gauge32
_CfprApMgmtIPv6IfAddrFsmTry_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmTry = _CfprApMgmtIPv6IfAddrFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 15),
    _CfprApMgmtIPv6IfAddrFsmTry_Type()
)
cfprApMgmtIPv6IfAddrFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmTry.setStatus("current")
_CfprApMgmtIPv6IfAddrPrefix_Type = Gauge32
_CfprApMgmtIPv6IfAddrPrefix_Object = MibTableColumn
cfprApMgmtIPv6IfAddrPrefix = _CfprApMgmtIPv6IfAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 26, 1, 16),
    _CfprApMgmtIPv6IfAddrPrefix_Type()
)
cfprApMgmtIPv6IfAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrPrefix.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmTable_Object = MibTable
cfprApMgmtIPv6IfAddrFsmTable = _CfprApMgmtIPv6IfAddrFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27)
)
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmTable.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmEntry_Object = MibTableRow
cfprApMgmtIPv6IfAddrFsmEntry = _CfprApMgmtIPv6IfAddrFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27, 1)
)
cfprApMgmtIPv6IfAddrFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtIPv6IfAddrFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmEntry.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtIPv6IfAddrFsmInstanceId_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmInstanceId = _CfprApMgmtIPv6IfAddrFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27, 1, 1),
    _CfprApMgmtIPv6IfAddrFsmInstanceId_Type()
)
cfprApMgmtIPv6IfAddrFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmInstanceId.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmDn_Type = CfprApManagedObjectDn
_CfprApMgmtIPv6IfAddrFsmDn_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmDn = _CfprApMgmtIPv6IfAddrFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27, 1, 2),
    _CfprApMgmtIPv6IfAddrFsmDn_Type()
)
cfprApMgmtIPv6IfAddrFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmDn.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmRn_Type = SnmpAdminString
_CfprApMgmtIPv6IfAddrFsmRn_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmRn = _CfprApMgmtIPv6IfAddrFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27, 1, 3),
    _CfprApMgmtIPv6IfAddrFsmRn_Type()
)
cfprApMgmtIPv6IfAddrFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmRn.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmCompletionTime_Type = DateAndTime
_CfprApMgmtIPv6IfAddrFsmCompletionTime_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmCompletionTime = _CfprApMgmtIPv6IfAddrFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27, 1, 4),
    _CfprApMgmtIPv6IfAddrFsmCompletionTime_Type()
)
cfprApMgmtIPv6IfAddrFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmCompletionTime.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmCurrentFsm_Type = CfprApMgmtIPv6IfAddrFsmCurrentFsm
_CfprApMgmtIPv6IfAddrFsmCurrentFsm_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmCurrentFsm = _CfprApMgmtIPv6IfAddrFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27, 1, 5),
    _CfprApMgmtIPv6IfAddrFsmCurrentFsm_Type()
)
cfprApMgmtIPv6IfAddrFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmCurrentFsm.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmDescrData_Type = SnmpAdminString
_CfprApMgmtIPv6IfAddrFsmDescrData_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmDescrData = _CfprApMgmtIPv6IfAddrFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27, 1, 6),
    _CfprApMgmtIPv6IfAddrFsmDescrData_Type()
)
cfprApMgmtIPv6IfAddrFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmDescrData.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtIPv6IfAddrFsmFsmStatus_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmFsmStatus = _CfprApMgmtIPv6IfAddrFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27, 1, 7),
    _CfprApMgmtIPv6IfAddrFsmFsmStatus_Type()
)
cfprApMgmtIPv6IfAddrFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmFsmStatus.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmProgress_Type = Gauge32
_CfprApMgmtIPv6IfAddrFsmProgress_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmProgress = _CfprApMgmtIPv6IfAddrFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27, 1, 8),
    _CfprApMgmtIPv6IfAddrFsmProgress_Type()
)
cfprApMgmtIPv6IfAddrFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmProgress.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmRmtErrCode_Type = Gauge32
_CfprApMgmtIPv6IfAddrFsmRmtErrCode_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmRmtErrCode = _CfprApMgmtIPv6IfAddrFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27, 1, 9),
    _CfprApMgmtIPv6IfAddrFsmRmtErrCode_Type()
)
cfprApMgmtIPv6IfAddrFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmRmtErrCode.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmRmtErrDescr_Type = SnmpAdminString
_CfprApMgmtIPv6IfAddrFsmRmtErrDescr_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmRmtErrDescr = _CfprApMgmtIPv6IfAddrFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27, 1, 10),
    _CfprApMgmtIPv6IfAddrFsmRmtErrDescr_Type()
)
cfprApMgmtIPv6IfAddrFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmRmtErrDescr.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtIPv6IfAddrFsmRmtRslt_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmRmtRslt = _CfprApMgmtIPv6IfAddrFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 27, 1, 11),
    _CfprApMgmtIPv6IfAddrFsmRmtRslt_Type()
)
cfprApMgmtIPv6IfAddrFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmRmtRslt.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStageTable_Object = MibTable
cfprApMgmtIPv6IfAddrFsmStageTable = _CfprApMgmtIPv6IfAddrFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 28)
)
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStageTable.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStageEntry_Object = MibTableRow
cfprApMgmtIPv6IfAddrFsmStageEntry = _CfprApMgmtIPv6IfAddrFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 28, 1)
)
cfprApMgmtIPv6IfAddrFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtIPv6IfAddrFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStageEntry.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtIPv6IfAddrFsmStageInstanceId_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmStageInstanceId = _CfprApMgmtIPv6IfAddrFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 28, 1, 1),
    _CfprApMgmtIPv6IfAddrFsmStageInstanceId_Type()
)
cfprApMgmtIPv6IfAddrFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStageInstanceId.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStageDn_Type = CfprApManagedObjectDn
_CfprApMgmtIPv6IfAddrFsmStageDn_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmStageDn = _CfprApMgmtIPv6IfAddrFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 28, 1, 2),
    _CfprApMgmtIPv6IfAddrFsmStageDn_Type()
)
cfprApMgmtIPv6IfAddrFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStageDn.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStageRn_Type = SnmpAdminString
_CfprApMgmtIPv6IfAddrFsmStageRn_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmStageRn = _CfprApMgmtIPv6IfAddrFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 28, 1, 3),
    _CfprApMgmtIPv6IfAddrFsmStageRn_Type()
)
cfprApMgmtIPv6IfAddrFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStageRn.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStageDescrData_Type = SnmpAdminString
_CfprApMgmtIPv6IfAddrFsmStageDescrData_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmStageDescrData = _CfprApMgmtIPv6IfAddrFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 28, 1, 4),
    _CfprApMgmtIPv6IfAddrFsmStageDescrData_Type()
)
cfprApMgmtIPv6IfAddrFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStageDescrData.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStageLastUpdateTime_Type = DateAndTime
_CfprApMgmtIPv6IfAddrFsmStageLastUpdateTime_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmStageLastUpdateTime = _CfprApMgmtIPv6IfAddrFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 28, 1, 5),
    _CfprApMgmtIPv6IfAddrFsmStageLastUpdateTime_Type()
)
cfprApMgmtIPv6IfAddrFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStageLastUpdateTime.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStageName_Type = CfprApMgmtIPv6IfAddrFsmStageName
_CfprApMgmtIPv6IfAddrFsmStageName_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmStageName = _CfprApMgmtIPv6IfAddrFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 28, 1, 6),
    _CfprApMgmtIPv6IfAddrFsmStageName_Type()
)
cfprApMgmtIPv6IfAddrFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStageName.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStageOrder_Type = Gauge32
_CfprApMgmtIPv6IfAddrFsmStageOrder_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmStageOrder = _CfprApMgmtIPv6IfAddrFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 28, 1, 7),
    _CfprApMgmtIPv6IfAddrFsmStageOrder_Type()
)
cfprApMgmtIPv6IfAddrFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStageOrder.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStageRetry_Type = Gauge32
_CfprApMgmtIPv6IfAddrFsmStageRetry_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmStageRetry = _CfprApMgmtIPv6IfAddrFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 28, 1, 8),
    _CfprApMgmtIPv6IfAddrFsmStageRetry_Type()
)
cfprApMgmtIPv6IfAddrFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStageRetry.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtIPv6IfAddrFsmStageStageStatus_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmStageStageStatus = _CfprApMgmtIPv6IfAddrFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 28, 1, 9),
    _CfprApMgmtIPv6IfAddrFsmStageStageStatus_Type()
)
cfprApMgmtIPv6IfAddrFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmStageStageStatus.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmTaskTable_Object = MibTable
cfprApMgmtIPv6IfAddrFsmTaskTable = _CfprApMgmtIPv6IfAddrFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 29)
)
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmTaskTable.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmTaskEntry_Object = MibTableRow
cfprApMgmtIPv6IfAddrFsmTaskEntry = _CfprApMgmtIPv6IfAddrFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 29, 1)
)
cfprApMgmtIPv6IfAddrFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtIPv6IfAddrFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmTaskEntry.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtIPv6IfAddrFsmTaskInstanceId_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmTaskInstanceId = _CfprApMgmtIPv6IfAddrFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 29, 1, 1),
    _CfprApMgmtIPv6IfAddrFsmTaskInstanceId_Type()
)
cfprApMgmtIPv6IfAddrFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmTaskInstanceId.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApMgmtIPv6IfAddrFsmTaskDn_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmTaskDn = _CfprApMgmtIPv6IfAddrFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 29, 1, 2),
    _CfprApMgmtIPv6IfAddrFsmTaskDn_Type()
)
cfprApMgmtIPv6IfAddrFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmTaskDn.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmTaskRn_Type = SnmpAdminString
_CfprApMgmtIPv6IfAddrFsmTaskRn_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmTaskRn = _CfprApMgmtIPv6IfAddrFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 29, 1, 3),
    _CfprApMgmtIPv6IfAddrFsmTaskRn_Type()
)
cfprApMgmtIPv6IfAddrFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmTaskRn.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApMgmtIPv6IfAddrFsmTaskCompletion_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmTaskCompletion = _CfprApMgmtIPv6IfAddrFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 29, 1, 4),
    _CfprApMgmtIPv6IfAddrFsmTaskCompletion_Type()
)
cfprApMgmtIPv6IfAddrFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmTaskCompletion.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmTaskFlags_Type = CfprApFsmFlags
_CfprApMgmtIPv6IfAddrFsmTaskFlags_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmTaskFlags = _CfprApMgmtIPv6IfAddrFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 29, 1, 5),
    _CfprApMgmtIPv6IfAddrFsmTaskFlags_Type()
)
cfprApMgmtIPv6IfAddrFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmTaskFlags.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmTaskItem_Type = CfprApMgmtIPv6IfAddrFsmTaskItem
_CfprApMgmtIPv6IfAddrFsmTaskItem_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmTaskItem = _CfprApMgmtIPv6IfAddrFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 29, 1, 6),
    _CfprApMgmtIPv6IfAddrFsmTaskItem_Type()
)
cfprApMgmtIPv6IfAddrFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmTaskItem.setStatus("current")
_CfprApMgmtIPv6IfAddrFsmTaskSeqId_Type = Gauge32
_CfprApMgmtIPv6IfAddrFsmTaskSeqId_Object = MibTableColumn
cfprApMgmtIPv6IfAddrFsmTaskSeqId = _CfprApMgmtIPv6IfAddrFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 29, 1, 7),
    _CfprApMgmtIPv6IfAddrFsmTaskSeqId_Type()
)
cfprApMgmtIPv6IfAddrFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfAddrFsmTaskSeqId.setStatus("current")
_CfprApMgmtIPv6IfConfigTable_Object = MibTable
cfprApMgmtIPv6IfConfigTable = _CfprApMgmtIPv6IfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 30)
)
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfConfigTable.setStatus("current")
_CfprApMgmtIPv6IfConfigEntry_Object = MibTableRow
cfprApMgmtIPv6IfConfigEntry = _CfprApMgmtIPv6IfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 30, 1)
)
cfprApMgmtIPv6IfConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtIPv6IfConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfConfigEntry.setStatus("current")
_CfprApMgmtIPv6IfConfigInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtIPv6IfConfigInstanceId_Object = MibTableColumn
cfprApMgmtIPv6IfConfigInstanceId = _CfprApMgmtIPv6IfConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 30, 1, 1),
    _CfprApMgmtIPv6IfConfigInstanceId_Type()
)
cfprApMgmtIPv6IfConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfConfigInstanceId.setStatus("current")
_CfprApMgmtIPv6IfConfigDn_Type = CfprApManagedObjectDn
_CfprApMgmtIPv6IfConfigDn_Object = MibTableColumn
cfprApMgmtIPv6IfConfigDn = _CfprApMgmtIPv6IfConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 30, 1, 2),
    _CfprApMgmtIPv6IfConfigDn_Type()
)
cfprApMgmtIPv6IfConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfConfigDn.setStatus("current")
_CfprApMgmtIPv6IfConfigRn_Type = SnmpAdminString
_CfprApMgmtIPv6IfConfigRn_Object = MibTableColumn
cfprApMgmtIPv6IfConfigRn = _CfprApMgmtIPv6IfConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 30, 1, 3),
    _CfprApMgmtIPv6IfConfigRn_Type()
)
cfprApMgmtIPv6IfConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIPv6IfConfigRn.setStatus("current")
_CfprApMgmtIfTable_Object = MibTable
cfprApMgmtIfTable = _CfprApMgmtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31)
)
if mibBuilder.loadTexts:
    cfprApMgmtIfTable.setStatus("current")
_CfprApMgmtIfEntry_Object = MibTableRow
cfprApMgmtIfEntry = _CfprApMgmtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1)
)
cfprApMgmtIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtIfEntry.setStatus("current")
_CfprApMgmtIfInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtIfInstanceId_Object = MibTableColumn
cfprApMgmtIfInstanceId = _CfprApMgmtIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 1),
    _CfprApMgmtIfInstanceId_Type()
)
cfprApMgmtIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtIfInstanceId.setStatus("current")
_CfprApMgmtIfDn_Type = CfprApManagedObjectDn
_CfprApMgmtIfDn_Object = MibTableColumn
cfprApMgmtIfDn = _CfprApMgmtIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 2),
    _CfprApMgmtIfDn_Type()
)
cfprApMgmtIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfDn.setStatus("current")
_CfprApMgmtIfRn_Type = SnmpAdminString
_CfprApMgmtIfRn_Object = MibTableColumn
cfprApMgmtIfRn = _CfprApMgmtIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 3),
    _CfprApMgmtIfRn_Type()
)
cfprApMgmtIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfRn.setStatus("current")
_CfprApMgmtIfAccess_Type = CfprApMgmtAccess
_CfprApMgmtIfAccess_Object = MibTableColumn
cfprApMgmtIfAccess = _CfprApMgmtIfAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 4),
    _CfprApMgmtIfAccess_Type()
)
cfprApMgmtIfAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfAccess.setStatus("current")
_CfprApMgmtIfAdminState_Type = CfprApMgmtAdminState
_CfprApMgmtIfAdminState_Object = MibTableColumn
cfprApMgmtIfAdminState = _CfprApMgmtIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 5),
    _CfprApMgmtIfAdminState_Type()
)
cfprApMgmtIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfAdminState.setStatus("current")
_CfprApMgmtIfAggrPortId_Type = Gauge32
_CfprApMgmtIfAggrPortId_Object = MibTableColumn
cfprApMgmtIfAggrPortId = _CfprApMgmtIfAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 6),
    _CfprApMgmtIfAggrPortId_Type()
)
cfprApMgmtIfAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfAggrPortId.setStatus("current")
_CfprApMgmtIfChassisId_Type = Gauge32
_CfprApMgmtIfChassisId_Object = MibTableColumn
cfprApMgmtIfChassisId = _CfprApMgmtIfChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 7),
    _CfprApMgmtIfChassisId_Type()
)
cfprApMgmtIfChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfChassisId.setStatus("current")
_CfprApMgmtIfDiscovery_Type = CfprApEtherSatelliteConnectionDisc
_CfprApMgmtIfDiscovery_Object = MibTableColumn
cfprApMgmtIfDiscovery = _CfprApMgmtIfDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 8),
    _CfprApMgmtIfDiscovery_Type()
)
cfprApMgmtIfDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfDiscovery.setStatus("current")
_CfprApMgmtIfEpDn_Type = SnmpAdminString
_CfprApMgmtIfEpDn_Object = MibTableColumn
cfprApMgmtIfEpDn = _CfprApMgmtIfEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 9),
    _CfprApMgmtIfEpDn_Type()
)
cfprApMgmtIfEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfEpDn.setStatus("current")
_CfprApMgmtIfExtBroadcast_Type = InetAddressIPv4
_CfprApMgmtIfExtBroadcast_Object = MibTableColumn
cfprApMgmtIfExtBroadcast = _CfprApMgmtIfExtBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 10),
    _CfprApMgmtIfExtBroadcast_Type()
)
cfprApMgmtIfExtBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfExtBroadcast.setStatus("current")
_CfprApMgmtIfExtGw_Type = InetAddressIPv4
_CfprApMgmtIfExtGw_Object = MibTableColumn
cfprApMgmtIfExtGw = _CfprApMgmtIfExtGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 11),
    _CfprApMgmtIfExtGw_Type()
)
cfprApMgmtIfExtGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfExtGw.setStatus("current")
_CfprApMgmtIfExtIp_Type = InetAddressIPv4
_CfprApMgmtIfExtIp_Object = MibTableColumn
cfprApMgmtIfExtIp = _CfprApMgmtIfExtIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 12),
    _CfprApMgmtIfExtIp_Type()
)
cfprApMgmtIfExtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfExtIp.setStatus("current")
_CfprApMgmtIfExtMask_Type = InetAddressIPv4
_CfprApMgmtIfExtMask_Object = MibTableColumn
cfprApMgmtIfExtMask = _CfprApMgmtIfExtMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 13),
    _CfprApMgmtIfExtMask_Type()
)
cfprApMgmtIfExtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfExtMask.setStatus("current")
_CfprApMgmtIfFsmDescr_Type = SnmpAdminString
_CfprApMgmtIfFsmDescr_Object = MibTableColumn
cfprApMgmtIfFsmDescr = _CfprApMgmtIfFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 14),
    _CfprApMgmtIfFsmDescr_Type()
)
cfprApMgmtIfFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmDescr.setStatus("current")
_CfprApMgmtIfFsmPrev_Type = SnmpAdminString
_CfprApMgmtIfFsmPrev_Object = MibTableColumn
cfprApMgmtIfFsmPrev = _CfprApMgmtIfFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 15),
    _CfprApMgmtIfFsmPrev_Type()
)
cfprApMgmtIfFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmPrev.setStatus("current")
_CfprApMgmtIfFsmProgr_Type = Gauge32
_CfprApMgmtIfFsmProgr_Object = MibTableColumn
cfprApMgmtIfFsmProgr = _CfprApMgmtIfFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 16),
    _CfprApMgmtIfFsmProgr_Type()
)
cfprApMgmtIfFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmProgr.setStatus("current")
_CfprApMgmtIfFsmRmtInvErrCode_Type = Gauge32
_CfprApMgmtIfFsmRmtInvErrCode_Object = MibTableColumn
cfprApMgmtIfFsmRmtInvErrCode = _CfprApMgmtIfFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 17),
    _CfprApMgmtIfFsmRmtInvErrCode_Type()
)
cfprApMgmtIfFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmRmtInvErrCode.setStatus("current")
_CfprApMgmtIfFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApMgmtIfFsmRmtInvErrDescr_Object = MibTableColumn
cfprApMgmtIfFsmRmtInvErrDescr = _CfprApMgmtIfFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 18),
    _CfprApMgmtIfFsmRmtInvErrDescr_Type()
)
cfprApMgmtIfFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmRmtInvErrDescr.setStatus("current")
_CfprApMgmtIfFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtIfFsmRmtInvRslt_Object = MibTableColumn
cfprApMgmtIfFsmRmtInvRslt = _CfprApMgmtIfFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 19),
    _CfprApMgmtIfFsmRmtInvRslt_Type()
)
cfprApMgmtIfFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmRmtInvRslt.setStatus("current")
_CfprApMgmtIfFsmStageDescr_Type = SnmpAdminString
_CfprApMgmtIfFsmStageDescr_Object = MibTableColumn
cfprApMgmtIfFsmStageDescr = _CfprApMgmtIfFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 20),
    _CfprApMgmtIfFsmStageDescr_Type()
)
cfprApMgmtIfFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStageDescr.setStatus("current")
_CfprApMgmtIfFsmStamp_Type = DateAndTime
_CfprApMgmtIfFsmStamp_Object = MibTableColumn
cfprApMgmtIfFsmStamp = _CfprApMgmtIfFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 21),
    _CfprApMgmtIfFsmStamp_Type()
)
cfprApMgmtIfFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStamp.setStatus("current")
_CfprApMgmtIfFsmStatus_Type = SnmpAdminString
_CfprApMgmtIfFsmStatus_Object = MibTableColumn
cfprApMgmtIfFsmStatus = _CfprApMgmtIfFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 22),
    _CfprApMgmtIfFsmStatus_Type()
)
cfprApMgmtIfFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStatus.setStatus("current")
_CfprApMgmtIfFsmTry_Type = Gauge32
_CfprApMgmtIfFsmTry_Object = MibTableColumn
cfprApMgmtIfFsmTry = _CfprApMgmtIfFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 23),
    _CfprApMgmtIfFsmTry_Type()
)
cfprApMgmtIfFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmTry.setStatus("current")
_CfprApMgmtIfId_Type = Gauge32
_CfprApMgmtIfId_Object = MibTableColumn
cfprApMgmtIfId = _CfprApMgmtIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 24),
    _CfprApMgmtIfId_Type()
)
cfprApMgmtIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfId.setStatus("current")
_CfprApMgmtIfIfRole_Type = CfprApNetworkPortRole
_CfprApMgmtIfIfRole_Object = MibTableColumn
cfprApMgmtIfIfRole = _CfprApMgmtIfIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 25),
    _CfprApMgmtIfIfRole_Type()
)
cfprApMgmtIfIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfIfRole.setStatus("current")
_CfprApMgmtIfIfType_Type = CfprApNetworkPhysEpIfType
_CfprApMgmtIfIfType_Object = MibTableColumn
cfprApMgmtIfIfType = _CfprApMgmtIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 26),
    _CfprApMgmtIfIfType_Type()
)
cfprApMgmtIfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfIfType.setStatus("current")
_CfprApMgmtIfIp_Type = InetAddressIPv4
_CfprApMgmtIfIp_Object = MibTableColumn
cfprApMgmtIfIp = _CfprApMgmtIfIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 27),
    _CfprApMgmtIfIp_Type()
)
cfprApMgmtIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfIp.setStatus("current")
_CfprApMgmtIfLocale_Type = CfprApNetworkLocale
_CfprApMgmtIfLocale_Object = MibTableColumn
cfprApMgmtIfLocale = _CfprApMgmtIfLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 28),
    _CfprApMgmtIfLocale_Type()
)
cfprApMgmtIfLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfLocale.setStatus("current")
_CfprApMgmtIfMac_Type = MacAddress
_CfprApMgmtIfMac_Object = MibTableColumn
cfprApMgmtIfMac = _CfprApMgmtIfMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 29),
    _CfprApMgmtIfMac_Type()
)
cfprApMgmtIfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfMac.setStatus("current")
_CfprApMgmtIfMask_Type = InetAddressIPv4
_CfprApMgmtIfMask_Object = MibTableColumn
cfprApMgmtIfMask = _CfprApMgmtIfMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 30),
    _CfprApMgmtIfMask_Type()
)
cfprApMgmtIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfMask.setStatus("current")
_CfprApMgmtIfName_Type = SnmpAdminString
_CfprApMgmtIfName_Object = MibTableColumn
cfprApMgmtIfName = _CfprApMgmtIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 31),
    _CfprApMgmtIfName_Type()
)
cfprApMgmtIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfName.setStatus("current")
_CfprApMgmtIfPeerAggrPortId_Type = Gauge32
_CfprApMgmtIfPeerAggrPortId_Object = MibTableColumn
cfprApMgmtIfPeerAggrPortId = _CfprApMgmtIfPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 32),
    _CfprApMgmtIfPeerAggrPortId_Type()
)
cfprApMgmtIfPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfPeerAggrPortId.setStatus("current")
_CfprApMgmtIfPeerChassisId_Type = Gauge32
_CfprApMgmtIfPeerChassisId_Object = MibTableColumn
cfprApMgmtIfPeerChassisId = _CfprApMgmtIfPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 33),
    _CfprApMgmtIfPeerChassisId_Type()
)
cfprApMgmtIfPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfPeerChassisId.setStatus("current")
_CfprApMgmtIfPeerDn_Type = SnmpAdminString
_CfprApMgmtIfPeerDn_Object = MibTableColumn
cfprApMgmtIfPeerDn = _CfprApMgmtIfPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 34),
    _CfprApMgmtIfPeerDn_Type()
)
cfprApMgmtIfPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfPeerDn.setStatus("current")
_CfprApMgmtIfPeerPortId_Type = Gauge32
_CfprApMgmtIfPeerPortId_Object = MibTableColumn
cfprApMgmtIfPeerPortId = _CfprApMgmtIfPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 35),
    _CfprApMgmtIfPeerPortId_Type()
)
cfprApMgmtIfPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfPeerPortId.setStatus("current")
_CfprApMgmtIfPeerSlotId_Type = Gauge32
_CfprApMgmtIfPeerSlotId_Object = MibTableColumn
cfprApMgmtIfPeerSlotId = _CfprApMgmtIfPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 36),
    _CfprApMgmtIfPeerSlotId_Type()
)
cfprApMgmtIfPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfPeerSlotId.setStatus("current")
_CfprApMgmtIfPortId_Type = Gauge32
_CfprApMgmtIfPortId_Object = MibTableColumn
cfprApMgmtIfPortId = _CfprApMgmtIfPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 37),
    _CfprApMgmtIfPortId_Type()
)
cfprApMgmtIfPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfPortId.setStatus("current")
_CfprApMgmtIfSlotId_Type = Gauge32
_CfprApMgmtIfSlotId_Object = MibTableColumn
cfprApMgmtIfSlotId = _CfprApMgmtIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 38),
    _CfprApMgmtIfSlotId_Type()
)
cfprApMgmtIfSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfSlotId.setStatus("current")
_CfprApMgmtIfStateQual_Type = CfprApMgmtStateQual
_CfprApMgmtIfStateQual_Object = MibTableColumn
cfprApMgmtIfStateQual = _CfprApMgmtIfStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 39),
    _CfprApMgmtIfStateQual_Type()
)
cfprApMgmtIfStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfStateQual.setStatus("current")
_CfprApMgmtIfSubject_Type = CfprApMgmtSubject
_CfprApMgmtIfSubject_Object = MibTableColumn
cfprApMgmtIfSubject = _CfprApMgmtIfSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 40),
    _CfprApMgmtIfSubject_Type()
)
cfprApMgmtIfSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfSubject.setStatus("current")
_CfprApMgmtIfSwitchId_Type = CfprApNetworkSwitchId
_CfprApMgmtIfSwitchId_Object = MibTableColumn
cfprApMgmtIfSwitchId = _CfprApMgmtIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 41),
    _CfprApMgmtIfSwitchId_Type()
)
cfprApMgmtIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfSwitchId.setStatus("current")
_CfprApMgmtIfTransport_Type = CfprApNetworkTransport
_CfprApMgmtIfTransport_Object = MibTableColumn
cfprApMgmtIfTransport = _CfprApMgmtIfTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 42),
    _CfprApMgmtIfTransport_Type()
)
cfprApMgmtIfTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfTransport.setStatus("current")
_CfprApMgmtIfType_Type = CfprApNetworkConnectionType
_CfprApMgmtIfType_Object = MibTableColumn
cfprApMgmtIfType = _CfprApMgmtIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 43),
    _CfprApMgmtIfType_Type()
)
cfprApMgmtIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfType.setStatus("current")
_CfprApMgmtIfVnet_Type = Gauge32
_CfprApMgmtIfVnet_Object = MibTableColumn
cfprApMgmtIfVnet = _CfprApMgmtIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 31, 1, 44),
    _CfprApMgmtIfVnet_Type()
)
cfprApMgmtIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfVnet.setStatus("current")
_CfprApMgmtIfFsmTable_Object = MibTable
cfprApMgmtIfFsmTable = _CfprApMgmtIfFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32)
)
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmTable.setStatus("current")
_CfprApMgmtIfFsmEntry_Object = MibTableRow
cfprApMgmtIfFsmEntry = _CfprApMgmtIfFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32, 1)
)
cfprApMgmtIfFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtIfFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmEntry.setStatus("current")
_CfprApMgmtIfFsmInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtIfFsmInstanceId_Object = MibTableColumn
cfprApMgmtIfFsmInstanceId = _CfprApMgmtIfFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32, 1, 1),
    _CfprApMgmtIfFsmInstanceId_Type()
)
cfprApMgmtIfFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmInstanceId.setStatus("current")
_CfprApMgmtIfFsmDn_Type = CfprApManagedObjectDn
_CfprApMgmtIfFsmDn_Object = MibTableColumn
cfprApMgmtIfFsmDn = _CfprApMgmtIfFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32, 1, 2),
    _CfprApMgmtIfFsmDn_Type()
)
cfprApMgmtIfFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmDn.setStatus("current")
_CfprApMgmtIfFsmRn_Type = SnmpAdminString
_CfprApMgmtIfFsmRn_Object = MibTableColumn
cfprApMgmtIfFsmRn = _CfprApMgmtIfFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32, 1, 3),
    _CfprApMgmtIfFsmRn_Type()
)
cfprApMgmtIfFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmRn.setStatus("current")
_CfprApMgmtIfFsmCompletionTime_Type = DateAndTime
_CfprApMgmtIfFsmCompletionTime_Object = MibTableColumn
cfprApMgmtIfFsmCompletionTime = _CfprApMgmtIfFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32, 1, 4),
    _CfprApMgmtIfFsmCompletionTime_Type()
)
cfprApMgmtIfFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmCompletionTime.setStatus("current")
_CfprApMgmtIfFsmCurrentFsm_Type = CfprApMgmtIfFsmCurrentFsm
_CfprApMgmtIfFsmCurrentFsm_Object = MibTableColumn
cfprApMgmtIfFsmCurrentFsm = _CfprApMgmtIfFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32, 1, 5),
    _CfprApMgmtIfFsmCurrentFsm_Type()
)
cfprApMgmtIfFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmCurrentFsm.setStatus("current")
_CfprApMgmtIfFsmDescrData_Type = SnmpAdminString
_CfprApMgmtIfFsmDescrData_Object = MibTableColumn
cfprApMgmtIfFsmDescrData = _CfprApMgmtIfFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32, 1, 6),
    _CfprApMgmtIfFsmDescrData_Type()
)
cfprApMgmtIfFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmDescrData.setStatus("current")
_CfprApMgmtIfFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtIfFsmFsmStatus_Object = MibTableColumn
cfprApMgmtIfFsmFsmStatus = _CfprApMgmtIfFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32, 1, 7),
    _CfprApMgmtIfFsmFsmStatus_Type()
)
cfprApMgmtIfFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmFsmStatus.setStatus("current")
_CfprApMgmtIfFsmProgress_Type = Gauge32
_CfprApMgmtIfFsmProgress_Object = MibTableColumn
cfprApMgmtIfFsmProgress = _CfprApMgmtIfFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32, 1, 8),
    _CfprApMgmtIfFsmProgress_Type()
)
cfprApMgmtIfFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmProgress.setStatus("current")
_CfprApMgmtIfFsmRmtErrCode_Type = Gauge32
_CfprApMgmtIfFsmRmtErrCode_Object = MibTableColumn
cfprApMgmtIfFsmRmtErrCode = _CfprApMgmtIfFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32, 1, 9),
    _CfprApMgmtIfFsmRmtErrCode_Type()
)
cfprApMgmtIfFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmRmtErrCode.setStatus("current")
_CfprApMgmtIfFsmRmtErrDescr_Type = SnmpAdminString
_CfprApMgmtIfFsmRmtErrDescr_Object = MibTableColumn
cfprApMgmtIfFsmRmtErrDescr = _CfprApMgmtIfFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32, 1, 10),
    _CfprApMgmtIfFsmRmtErrDescr_Type()
)
cfprApMgmtIfFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmRmtErrDescr.setStatus("current")
_CfprApMgmtIfFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtIfFsmRmtRslt_Object = MibTableColumn
cfprApMgmtIfFsmRmtRslt = _CfprApMgmtIfFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 32, 1, 11),
    _CfprApMgmtIfFsmRmtRslt_Type()
)
cfprApMgmtIfFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmRmtRslt.setStatus("current")
_CfprApMgmtIfFsmStageTable_Object = MibTable
cfprApMgmtIfFsmStageTable = _CfprApMgmtIfFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 33)
)
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStageTable.setStatus("current")
_CfprApMgmtIfFsmStageEntry_Object = MibTableRow
cfprApMgmtIfFsmStageEntry = _CfprApMgmtIfFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 33, 1)
)
cfprApMgmtIfFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtIfFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStageEntry.setStatus("current")
_CfprApMgmtIfFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtIfFsmStageInstanceId_Object = MibTableColumn
cfprApMgmtIfFsmStageInstanceId = _CfprApMgmtIfFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 33, 1, 1),
    _CfprApMgmtIfFsmStageInstanceId_Type()
)
cfprApMgmtIfFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStageInstanceId.setStatus("current")
_CfprApMgmtIfFsmStageDn_Type = CfprApManagedObjectDn
_CfprApMgmtIfFsmStageDn_Object = MibTableColumn
cfprApMgmtIfFsmStageDn = _CfprApMgmtIfFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 33, 1, 2),
    _CfprApMgmtIfFsmStageDn_Type()
)
cfprApMgmtIfFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStageDn.setStatus("current")
_CfprApMgmtIfFsmStageRn_Type = SnmpAdminString
_CfprApMgmtIfFsmStageRn_Object = MibTableColumn
cfprApMgmtIfFsmStageRn = _CfprApMgmtIfFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 33, 1, 3),
    _CfprApMgmtIfFsmStageRn_Type()
)
cfprApMgmtIfFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStageRn.setStatus("current")
_CfprApMgmtIfFsmStageDescrData_Type = SnmpAdminString
_CfprApMgmtIfFsmStageDescrData_Object = MibTableColumn
cfprApMgmtIfFsmStageDescrData = _CfprApMgmtIfFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 33, 1, 4),
    _CfprApMgmtIfFsmStageDescrData_Type()
)
cfprApMgmtIfFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStageDescrData.setStatus("current")
_CfprApMgmtIfFsmStageLastUpdateTime_Type = DateAndTime
_CfprApMgmtIfFsmStageLastUpdateTime_Object = MibTableColumn
cfprApMgmtIfFsmStageLastUpdateTime = _CfprApMgmtIfFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 33, 1, 5),
    _CfprApMgmtIfFsmStageLastUpdateTime_Type()
)
cfprApMgmtIfFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStageLastUpdateTime.setStatus("current")
_CfprApMgmtIfFsmStageName_Type = CfprApMgmtIfFsmStageName
_CfprApMgmtIfFsmStageName_Object = MibTableColumn
cfprApMgmtIfFsmStageName = _CfprApMgmtIfFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 33, 1, 6),
    _CfprApMgmtIfFsmStageName_Type()
)
cfprApMgmtIfFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStageName.setStatus("current")
_CfprApMgmtIfFsmStageOrder_Type = Gauge32
_CfprApMgmtIfFsmStageOrder_Object = MibTableColumn
cfprApMgmtIfFsmStageOrder = _CfprApMgmtIfFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 33, 1, 7),
    _CfprApMgmtIfFsmStageOrder_Type()
)
cfprApMgmtIfFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStageOrder.setStatus("current")
_CfprApMgmtIfFsmStageRetry_Type = Gauge32
_CfprApMgmtIfFsmStageRetry_Object = MibTableColumn
cfprApMgmtIfFsmStageRetry = _CfprApMgmtIfFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 33, 1, 8),
    _CfprApMgmtIfFsmStageRetry_Type()
)
cfprApMgmtIfFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStageRetry.setStatus("current")
_CfprApMgmtIfFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtIfFsmStageStageStatus_Object = MibTableColumn
cfprApMgmtIfFsmStageStageStatus = _CfprApMgmtIfFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 33, 1, 9),
    _CfprApMgmtIfFsmStageStageStatus_Type()
)
cfprApMgmtIfFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmStageStageStatus.setStatus("current")
_CfprApMgmtIfFsmTaskTable_Object = MibTable
cfprApMgmtIfFsmTaskTable = _CfprApMgmtIfFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 34)
)
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmTaskTable.setStatus("current")
_CfprApMgmtIfFsmTaskEntry_Object = MibTableRow
cfprApMgmtIfFsmTaskEntry = _CfprApMgmtIfFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 34, 1)
)
cfprApMgmtIfFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtIfFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmTaskEntry.setStatus("current")
_CfprApMgmtIfFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtIfFsmTaskInstanceId_Object = MibTableColumn
cfprApMgmtIfFsmTaskInstanceId = _CfprApMgmtIfFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 34, 1, 1),
    _CfprApMgmtIfFsmTaskInstanceId_Type()
)
cfprApMgmtIfFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmTaskInstanceId.setStatus("current")
_CfprApMgmtIfFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApMgmtIfFsmTaskDn_Object = MibTableColumn
cfprApMgmtIfFsmTaskDn = _CfprApMgmtIfFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 34, 1, 2),
    _CfprApMgmtIfFsmTaskDn_Type()
)
cfprApMgmtIfFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmTaskDn.setStatus("current")
_CfprApMgmtIfFsmTaskRn_Type = SnmpAdminString
_CfprApMgmtIfFsmTaskRn_Object = MibTableColumn
cfprApMgmtIfFsmTaskRn = _CfprApMgmtIfFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 34, 1, 3),
    _CfprApMgmtIfFsmTaskRn_Type()
)
cfprApMgmtIfFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmTaskRn.setStatus("current")
_CfprApMgmtIfFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApMgmtIfFsmTaskCompletion_Object = MibTableColumn
cfprApMgmtIfFsmTaskCompletion = _CfprApMgmtIfFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 34, 1, 4),
    _CfprApMgmtIfFsmTaskCompletion_Type()
)
cfprApMgmtIfFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmTaskCompletion.setStatus("current")
_CfprApMgmtIfFsmTaskFlags_Type = CfprApFsmFlags
_CfprApMgmtIfFsmTaskFlags_Object = MibTableColumn
cfprApMgmtIfFsmTaskFlags = _CfprApMgmtIfFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 34, 1, 5),
    _CfprApMgmtIfFsmTaskFlags_Type()
)
cfprApMgmtIfFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmTaskFlags.setStatus("current")
_CfprApMgmtIfFsmTaskItem_Type = CfprApMgmtIfFsmTaskItem
_CfprApMgmtIfFsmTaskItem_Object = MibTableColumn
cfprApMgmtIfFsmTaskItem = _CfprApMgmtIfFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 34, 1, 6),
    _CfprApMgmtIfFsmTaskItem_Type()
)
cfprApMgmtIfFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmTaskItem.setStatus("current")
_CfprApMgmtIfFsmTaskSeqId_Type = Gauge32
_CfprApMgmtIfFsmTaskSeqId_Object = MibTableColumn
cfprApMgmtIfFsmTaskSeqId = _CfprApMgmtIfFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 34, 1, 7),
    _CfprApMgmtIfFsmTaskSeqId_Type()
)
cfprApMgmtIfFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIfFsmTaskSeqId.setStatus("current")
_CfprApMgmtImportConfigInfoTable_Object = MibTable
cfprApMgmtImportConfigInfoTable = _CfprApMgmtImportConfigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 35)
)
if mibBuilder.loadTexts:
    cfprApMgmtImportConfigInfoTable.setStatus("current")
_CfprApMgmtImportConfigInfoEntry_Object = MibTableRow
cfprApMgmtImportConfigInfoEntry = _CfprApMgmtImportConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 35, 1)
)
cfprApMgmtImportConfigInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtImportConfigInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtImportConfigInfoEntry.setStatus("current")
_CfprApMgmtImportConfigInfoInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtImportConfigInfoInstanceId_Object = MibTableColumn
cfprApMgmtImportConfigInfoInstanceId = _CfprApMgmtImportConfigInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 35, 1, 1),
    _CfprApMgmtImportConfigInfoInstanceId_Type()
)
cfprApMgmtImportConfigInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtImportConfigInfoInstanceId.setStatus("current")
_CfprApMgmtImportConfigInfoDn_Type = CfprApManagedObjectDn
_CfprApMgmtImportConfigInfoDn_Object = MibTableColumn
cfprApMgmtImportConfigInfoDn = _CfprApMgmtImportConfigInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 35, 1, 2),
    _CfprApMgmtImportConfigInfoDn_Type()
)
cfprApMgmtImportConfigInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImportConfigInfoDn.setStatus("current")
_CfprApMgmtImportConfigInfoRn_Type = SnmpAdminString
_CfprApMgmtImportConfigInfoRn_Object = MibTableColumn
cfprApMgmtImportConfigInfoRn = _CfprApMgmtImportConfigInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 35, 1, 3),
    _CfprApMgmtImportConfigInfoRn_Type()
)
cfprApMgmtImportConfigInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImportConfigInfoRn.setStatus("current")
_CfprApMgmtImportConfigInfoImportDate_Type = DateAndTime
_CfprApMgmtImportConfigInfoImportDate_Object = MibTableColumn
cfprApMgmtImportConfigInfoImportDate = _CfprApMgmtImportConfigInfoImportDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 35, 1, 4),
    _CfprApMgmtImportConfigInfoImportDate_Type()
)
cfprApMgmtImportConfigInfoImportDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImportConfigInfoImportDate.setStatus("current")
_CfprApMgmtImporterTable_Object = MibTable
cfprApMgmtImporterTable = _CfprApMgmtImporterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36)
)
if mibBuilder.loadTexts:
    cfprApMgmtImporterTable.setStatus("current")
_CfprApMgmtImporterEntry_Object = MibTableRow
cfprApMgmtImporterEntry = _CfprApMgmtImporterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1)
)
cfprApMgmtImporterEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtImporterInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtImporterEntry.setStatus("current")
_CfprApMgmtImporterInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtImporterInstanceId_Object = MibTableColumn
cfprApMgmtImporterInstanceId = _CfprApMgmtImporterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 1),
    _CfprApMgmtImporterInstanceId_Type()
)
cfprApMgmtImporterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtImporterInstanceId.setStatus("current")
_CfprApMgmtImporterDn_Type = CfprApManagedObjectDn
_CfprApMgmtImporterDn_Object = MibTableColumn
cfprApMgmtImporterDn = _CfprApMgmtImporterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 2),
    _CfprApMgmtImporterDn_Type()
)
cfprApMgmtImporterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterDn.setStatus("current")
_CfprApMgmtImporterRn_Type = SnmpAdminString
_CfprApMgmtImporterRn_Object = MibTableColumn
cfprApMgmtImporterRn = _CfprApMgmtImporterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 3),
    _CfprApMgmtImporterRn_Type()
)
cfprApMgmtImporterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterRn.setStatus("current")
_CfprApMgmtImporterAction_Type = CfprApMgmtImportAction
_CfprApMgmtImporterAction_Object = MibTableColumn
cfprApMgmtImporterAction = _CfprApMgmtImporterAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 4),
    _CfprApMgmtImporterAction_Type()
)
cfprApMgmtImporterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterAction.setStatus("current")
_CfprApMgmtImporterAdminState_Type = CfprApCommClientAdminState
_CfprApMgmtImporterAdminState_Object = MibTableColumn
cfprApMgmtImporterAdminState = _CfprApMgmtImporterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 5),
    _CfprApMgmtImporterAdminState_Type()
)
cfprApMgmtImporterAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterAdminState.setStatus("current")
_CfprApMgmtImporterApplyingBreakoutCfg_Type = TruthValue
_CfprApMgmtImporterApplyingBreakoutCfg_Object = MibTableColumn
cfprApMgmtImporterApplyingBreakoutCfg = _CfprApMgmtImporterApplyingBreakoutCfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 6),
    _CfprApMgmtImporterApplyingBreakoutCfg_Type()
)
cfprApMgmtImporterApplyingBreakoutCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterApplyingBreakoutCfg.setStatus("current")
_CfprApMgmtImporterDescr_Type = SnmpAdminString
_CfprApMgmtImporterDescr_Object = MibTableColumn
cfprApMgmtImporterDescr = _CfprApMgmtImporterDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 7),
    _CfprApMgmtImporterDescr_Type()
)
cfprApMgmtImporterDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterDescr.setStatus("current")
_CfprApMgmtImporterFsmDescr_Type = SnmpAdminString
_CfprApMgmtImporterFsmDescr_Object = MibTableColumn
cfprApMgmtImporterFsmDescr = _CfprApMgmtImporterFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 8),
    _CfprApMgmtImporterFsmDescr_Type()
)
cfprApMgmtImporterFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmDescr.setStatus("current")
_CfprApMgmtImporterFsmPrev_Type = SnmpAdminString
_CfprApMgmtImporterFsmPrev_Object = MibTableColumn
cfprApMgmtImporterFsmPrev = _CfprApMgmtImporterFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 9),
    _CfprApMgmtImporterFsmPrev_Type()
)
cfprApMgmtImporterFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmPrev.setStatus("current")
_CfprApMgmtImporterFsmProgr_Type = Gauge32
_CfprApMgmtImporterFsmProgr_Object = MibTableColumn
cfprApMgmtImporterFsmProgr = _CfprApMgmtImporterFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 10),
    _CfprApMgmtImporterFsmProgr_Type()
)
cfprApMgmtImporterFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmProgr.setStatus("current")
_CfprApMgmtImporterFsmRmtInvErrCode_Type = Gauge32
_CfprApMgmtImporterFsmRmtInvErrCode_Object = MibTableColumn
cfprApMgmtImporterFsmRmtInvErrCode = _CfprApMgmtImporterFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 11),
    _CfprApMgmtImporterFsmRmtInvErrCode_Type()
)
cfprApMgmtImporterFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmRmtInvErrCode.setStatus("current")
_CfprApMgmtImporterFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApMgmtImporterFsmRmtInvErrDescr_Object = MibTableColumn
cfprApMgmtImporterFsmRmtInvErrDescr = _CfprApMgmtImporterFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 12),
    _CfprApMgmtImporterFsmRmtInvErrDescr_Type()
)
cfprApMgmtImporterFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmRmtInvErrDescr.setStatus("current")
_CfprApMgmtImporterFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtImporterFsmRmtInvRslt_Object = MibTableColumn
cfprApMgmtImporterFsmRmtInvRslt = _CfprApMgmtImporterFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 13),
    _CfprApMgmtImporterFsmRmtInvRslt_Type()
)
cfprApMgmtImporterFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmRmtInvRslt.setStatus("current")
_CfprApMgmtImporterFsmStageDescr_Type = SnmpAdminString
_CfprApMgmtImporterFsmStageDescr_Object = MibTableColumn
cfprApMgmtImporterFsmStageDescr = _CfprApMgmtImporterFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 14),
    _CfprApMgmtImporterFsmStageDescr_Type()
)
cfprApMgmtImporterFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStageDescr.setStatus("current")
_CfprApMgmtImporterFsmStamp_Type = DateAndTime
_CfprApMgmtImporterFsmStamp_Object = MibTableColumn
cfprApMgmtImporterFsmStamp = _CfprApMgmtImporterFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 15),
    _CfprApMgmtImporterFsmStamp_Type()
)
cfprApMgmtImporterFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStamp.setStatus("current")
_CfprApMgmtImporterFsmStatus_Type = SnmpAdminString
_CfprApMgmtImporterFsmStatus_Object = MibTableColumn
cfprApMgmtImporterFsmStatus = _CfprApMgmtImporterFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 16),
    _CfprApMgmtImporterFsmStatus_Type()
)
cfprApMgmtImporterFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStatus.setStatus("current")
_CfprApMgmtImporterFsmTry_Type = Gauge32
_CfprApMgmtImporterFsmTry_Object = MibTableColumn
cfprApMgmtImporterFsmTry = _CfprApMgmtImporterFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 17),
    _CfprApMgmtImporterFsmTry_Type()
)
cfprApMgmtImporterFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmTry.setStatus("current")
_CfprApMgmtImporterHostname_Type = SnmpAdminString
_CfprApMgmtImporterHostname_Object = MibTableColumn
cfprApMgmtImporterHostname = _CfprApMgmtImporterHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 18),
    _CfprApMgmtImporterHostname_Type()
)
cfprApMgmtImporterHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterHostname.setStatus("current")
_CfprApMgmtImporterIntId_Type = SnmpAdminString
_CfprApMgmtImporterIntId_Object = MibTableColumn
cfprApMgmtImporterIntId = _CfprApMgmtImporterIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 19),
    _CfprApMgmtImporterIntId_Type()
)
cfprApMgmtImporterIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterIntId.setStatus("current")
_CfprApMgmtImporterName_Type = SnmpAdminString
_CfprApMgmtImporterName_Object = MibTableColumn
cfprApMgmtImporterName = _CfprApMgmtImporterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 20),
    _CfprApMgmtImporterName_Type()
)
cfprApMgmtImporterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterName.setStatus("current")
_CfprApMgmtImporterOperStatus_Type = CfprApMgmtImportStatus
_CfprApMgmtImporterOperStatus_Object = MibTableColumn
cfprApMgmtImporterOperStatus = _CfprApMgmtImporterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 21),
    _CfprApMgmtImporterOperStatus_Type()
)
cfprApMgmtImporterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterOperStatus.setStatus("current")
_CfprApMgmtImporterPolicyLevel_Type = Gauge32
_CfprApMgmtImporterPolicyLevel_Object = MibTableColumn
cfprApMgmtImporterPolicyLevel = _CfprApMgmtImporterPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 22),
    _CfprApMgmtImporterPolicyLevel_Type()
)
cfprApMgmtImporterPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterPolicyLevel.setStatus("current")
_CfprApMgmtImporterPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApMgmtImporterPolicyOwner_Object = MibTableColumn
cfprApMgmtImporterPolicyOwner = _CfprApMgmtImporterPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 23),
    _CfprApMgmtImporterPolicyOwner_Type()
)
cfprApMgmtImporterPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterPolicyOwner.setStatus("current")
_CfprApMgmtImporterPort_Type = Gauge32
_CfprApMgmtImporterPort_Object = MibTableColumn
cfprApMgmtImporterPort = _CfprApMgmtImporterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 24),
    _CfprApMgmtImporterPort_Type()
)
cfprApMgmtImporterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterPort.setStatus("current")
_CfprApMgmtImporterPostAction_Type = CfprApMgmtImporterPostAction
_CfprApMgmtImporterPostAction_Object = MibTableColumn
cfprApMgmtImporterPostAction = _CfprApMgmtImporterPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 25),
    _CfprApMgmtImporterPostAction_Type()
)
cfprApMgmtImporterPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterPostAction.setStatus("current")
_CfprApMgmtImporterProto_Type = CfprApMgmtImporterProto
_CfprApMgmtImporterProto_Object = MibTableColumn
cfprApMgmtImporterProto = _CfprApMgmtImporterProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 26),
    _CfprApMgmtImporterProto_Type()
)
cfprApMgmtImporterProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterProto.setStatus("current")
_CfprApMgmtImporterPwd_Type = SnmpAdminString
_CfprApMgmtImporterPwd_Object = MibTableColumn
cfprApMgmtImporterPwd = _CfprApMgmtImporterPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 27),
    _CfprApMgmtImporterPwd_Type()
)
cfprApMgmtImporterPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterPwd.setStatus("current")
_CfprApMgmtImporterRemoteFile_Type = SnmpAdminString
_CfprApMgmtImporterRemoteFile_Object = MibTableColumn
cfprApMgmtImporterRemoteFile = _CfprApMgmtImporterRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 28),
    _CfprApMgmtImporterRemoteFile_Type()
)
cfprApMgmtImporterRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterRemoteFile.setStatus("current")
_CfprApMgmtImporterUser_Type = SnmpAdminString
_CfprApMgmtImporterUser_Object = MibTableColumn
cfprApMgmtImporterUser = _CfprApMgmtImporterUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 36, 1, 29),
    _CfprApMgmtImporterUser_Type()
)
cfprApMgmtImporterUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterUser.setStatus("current")
_CfprApMgmtImporterFsmTable_Object = MibTable
cfprApMgmtImporterFsmTable = _CfprApMgmtImporterFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37)
)
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmTable.setStatus("current")
_CfprApMgmtImporterFsmEntry_Object = MibTableRow
cfprApMgmtImporterFsmEntry = _CfprApMgmtImporterFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37, 1)
)
cfprApMgmtImporterFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtImporterFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmEntry.setStatus("current")
_CfprApMgmtImporterFsmInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtImporterFsmInstanceId_Object = MibTableColumn
cfprApMgmtImporterFsmInstanceId = _CfprApMgmtImporterFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37, 1, 1),
    _CfprApMgmtImporterFsmInstanceId_Type()
)
cfprApMgmtImporterFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmInstanceId.setStatus("current")
_CfprApMgmtImporterFsmDn_Type = CfprApManagedObjectDn
_CfprApMgmtImporterFsmDn_Object = MibTableColumn
cfprApMgmtImporterFsmDn = _CfprApMgmtImporterFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37, 1, 2),
    _CfprApMgmtImporterFsmDn_Type()
)
cfprApMgmtImporterFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmDn.setStatus("current")
_CfprApMgmtImporterFsmRn_Type = SnmpAdminString
_CfprApMgmtImporterFsmRn_Object = MibTableColumn
cfprApMgmtImporterFsmRn = _CfprApMgmtImporterFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37, 1, 3),
    _CfprApMgmtImporterFsmRn_Type()
)
cfprApMgmtImporterFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmRn.setStatus("current")
_CfprApMgmtImporterFsmCompletionTime_Type = DateAndTime
_CfprApMgmtImporterFsmCompletionTime_Object = MibTableColumn
cfprApMgmtImporterFsmCompletionTime = _CfprApMgmtImporterFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37, 1, 4),
    _CfprApMgmtImporterFsmCompletionTime_Type()
)
cfprApMgmtImporterFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmCompletionTime.setStatus("current")
_CfprApMgmtImporterFsmCurrentFsm_Type = CfprApMgmtImporterFsmCurrentFsm
_CfprApMgmtImporterFsmCurrentFsm_Object = MibTableColumn
cfprApMgmtImporterFsmCurrentFsm = _CfprApMgmtImporterFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37, 1, 5),
    _CfprApMgmtImporterFsmCurrentFsm_Type()
)
cfprApMgmtImporterFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmCurrentFsm.setStatus("current")
_CfprApMgmtImporterFsmDescrData_Type = SnmpAdminString
_CfprApMgmtImporterFsmDescrData_Object = MibTableColumn
cfprApMgmtImporterFsmDescrData = _CfprApMgmtImporterFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37, 1, 6),
    _CfprApMgmtImporterFsmDescrData_Type()
)
cfprApMgmtImporterFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmDescrData.setStatus("current")
_CfprApMgmtImporterFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtImporterFsmFsmStatus_Object = MibTableColumn
cfprApMgmtImporterFsmFsmStatus = _CfprApMgmtImporterFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37, 1, 7),
    _CfprApMgmtImporterFsmFsmStatus_Type()
)
cfprApMgmtImporterFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmFsmStatus.setStatus("current")
_CfprApMgmtImporterFsmProgress_Type = Gauge32
_CfprApMgmtImporterFsmProgress_Object = MibTableColumn
cfprApMgmtImporterFsmProgress = _CfprApMgmtImporterFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37, 1, 8),
    _CfprApMgmtImporterFsmProgress_Type()
)
cfprApMgmtImporterFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmProgress.setStatus("current")
_CfprApMgmtImporterFsmRmtErrCode_Type = Gauge32
_CfprApMgmtImporterFsmRmtErrCode_Object = MibTableColumn
cfprApMgmtImporterFsmRmtErrCode = _CfprApMgmtImporterFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37, 1, 9),
    _CfprApMgmtImporterFsmRmtErrCode_Type()
)
cfprApMgmtImporterFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmRmtErrCode.setStatus("current")
_CfprApMgmtImporterFsmRmtErrDescr_Type = SnmpAdminString
_CfprApMgmtImporterFsmRmtErrDescr_Object = MibTableColumn
cfprApMgmtImporterFsmRmtErrDescr = _CfprApMgmtImporterFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37, 1, 10),
    _CfprApMgmtImporterFsmRmtErrDescr_Type()
)
cfprApMgmtImporterFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmRmtErrDescr.setStatus("current")
_CfprApMgmtImporterFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApMgmtImporterFsmRmtRslt_Object = MibTableColumn
cfprApMgmtImporterFsmRmtRslt = _CfprApMgmtImporterFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 37, 1, 11),
    _CfprApMgmtImporterFsmRmtRslt_Type()
)
cfprApMgmtImporterFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmRmtRslt.setStatus("current")
_CfprApMgmtImporterFsmStageTable_Object = MibTable
cfprApMgmtImporterFsmStageTable = _CfprApMgmtImporterFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 38)
)
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStageTable.setStatus("current")
_CfprApMgmtImporterFsmStageEntry_Object = MibTableRow
cfprApMgmtImporterFsmStageEntry = _CfprApMgmtImporterFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 38, 1)
)
cfprApMgmtImporterFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtImporterFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStageEntry.setStatus("current")
_CfprApMgmtImporterFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtImporterFsmStageInstanceId_Object = MibTableColumn
cfprApMgmtImporterFsmStageInstanceId = _CfprApMgmtImporterFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 38, 1, 1),
    _CfprApMgmtImporterFsmStageInstanceId_Type()
)
cfprApMgmtImporterFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStageInstanceId.setStatus("current")
_CfprApMgmtImporterFsmStageDn_Type = CfprApManagedObjectDn
_CfprApMgmtImporterFsmStageDn_Object = MibTableColumn
cfprApMgmtImporterFsmStageDn = _CfprApMgmtImporterFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 38, 1, 2),
    _CfprApMgmtImporterFsmStageDn_Type()
)
cfprApMgmtImporterFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStageDn.setStatus("current")
_CfprApMgmtImporterFsmStageRn_Type = SnmpAdminString
_CfprApMgmtImporterFsmStageRn_Object = MibTableColumn
cfprApMgmtImporterFsmStageRn = _CfprApMgmtImporterFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 38, 1, 3),
    _CfprApMgmtImporterFsmStageRn_Type()
)
cfprApMgmtImporterFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStageRn.setStatus("current")
_CfprApMgmtImporterFsmStageDescrData_Type = SnmpAdminString
_CfprApMgmtImporterFsmStageDescrData_Object = MibTableColumn
cfprApMgmtImporterFsmStageDescrData = _CfprApMgmtImporterFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 38, 1, 4),
    _CfprApMgmtImporterFsmStageDescrData_Type()
)
cfprApMgmtImporterFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStageDescrData.setStatus("current")
_CfprApMgmtImporterFsmStageLastUpdateTime_Type = DateAndTime
_CfprApMgmtImporterFsmStageLastUpdateTime_Object = MibTableColumn
cfprApMgmtImporterFsmStageLastUpdateTime = _CfprApMgmtImporterFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 38, 1, 5),
    _CfprApMgmtImporterFsmStageLastUpdateTime_Type()
)
cfprApMgmtImporterFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStageLastUpdateTime.setStatus("current")
_CfprApMgmtImporterFsmStageName_Type = CfprApMgmtImporterFsmStageName
_CfprApMgmtImporterFsmStageName_Object = MibTableColumn
cfprApMgmtImporterFsmStageName = _CfprApMgmtImporterFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 38, 1, 6),
    _CfprApMgmtImporterFsmStageName_Type()
)
cfprApMgmtImporterFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStageName.setStatus("current")
_CfprApMgmtImporterFsmStageOrder_Type = Gauge32
_CfprApMgmtImporterFsmStageOrder_Object = MibTableColumn
cfprApMgmtImporterFsmStageOrder = _CfprApMgmtImporterFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 38, 1, 7),
    _CfprApMgmtImporterFsmStageOrder_Type()
)
cfprApMgmtImporterFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStageOrder.setStatus("current")
_CfprApMgmtImporterFsmStageRetry_Type = Gauge32
_CfprApMgmtImporterFsmStageRetry_Object = MibTableColumn
cfprApMgmtImporterFsmStageRetry = _CfprApMgmtImporterFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 38, 1, 8),
    _CfprApMgmtImporterFsmStageRetry_Type()
)
cfprApMgmtImporterFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStageRetry.setStatus("current")
_CfprApMgmtImporterFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApMgmtImporterFsmStageStageStatus_Object = MibTableColumn
cfprApMgmtImporterFsmStageStageStatus = _CfprApMgmtImporterFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 38, 1, 9),
    _CfprApMgmtImporterFsmStageStageStatus_Type()
)
cfprApMgmtImporterFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmStageStageStatus.setStatus("current")
_CfprApMgmtImporterFsmTaskTable_Object = MibTable
cfprApMgmtImporterFsmTaskTable = _CfprApMgmtImporterFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 39)
)
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmTaskTable.setStatus("current")
_CfprApMgmtImporterFsmTaskEntry_Object = MibTableRow
cfprApMgmtImporterFsmTaskEntry = _CfprApMgmtImporterFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 39, 1)
)
cfprApMgmtImporterFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtImporterFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmTaskEntry.setStatus("current")
_CfprApMgmtImporterFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtImporterFsmTaskInstanceId_Object = MibTableColumn
cfprApMgmtImporterFsmTaskInstanceId = _CfprApMgmtImporterFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 39, 1, 1),
    _CfprApMgmtImporterFsmTaskInstanceId_Type()
)
cfprApMgmtImporterFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmTaskInstanceId.setStatus("current")
_CfprApMgmtImporterFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApMgmtImporterFsmTaskDn_Object = MibTableColumn
cfprApMgmtImporterFsmTaskDn = _CfprApMgmtImporterFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 39, 1, 2),
    _CfprApMgmtImporterFsmTaskDn_Type()
)
cfprApMgmtImporterFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmTaskDn.setStatus("current")
_CfprApMgmtImporterFsmTaskRn_Type = SnmpAdminString
_CfprApMgmtImporterFsmTaskRn_Object = MibTableColumn
cfprApMgmtImporterFsmTaskRn = _CfprApMgmtImporterFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 39, 1, 3),
    _CfprApMgmtImporterFsmTaskRn_Type()
)
cfprApMgmtImporterFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmTaskRn.setStatus("current")
_CfprApMgmtImporterFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApMgmtImporterFsmTaskCompletion_Object = MibTableColumn
cfprApMgmtImporterFsmTaskCompletion = _CfprApMgmtImporterFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 39, 1, 4),
    _CfprApMgmtImporterFsmTaskCompletion_Type()
)
cfprApMgmtImporterFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmTaskCompletion.setStatus("current")
_CfprApMgmtImporterFsmTaskFlags_Type = CfprApFsmFlags
_CfprApMgmtImporterFsmTaskFlags_Object = MibTableColumn
cfprApMgmtImporterFsmTaskFlags = _CfprApMgmtImporterFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 39, 1, 5),
    _CfprApMgmtImporterFsmTaskFlags_Type()
)
cfprApMgmtImporterFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmTaskFlags.setStatus("current")
_CfprApMgmtImporterFsmTaskItem_Type = CfprApMgmtImporterFsmTaskItem
_CfprApMgmtImporterFsmTaskItem_Object = MibTableColumn
cfprApMgmtImporterFsmTaskItem = _CfprApMgmtImporterFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 39, 1, 6),
    _CfprApMgmtImporterFsmTaskItem_Type()
)
cfprApMgmtImporterFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmTaskItem.setStatus("current")
_CfprApMgmtImporterFsmTaskSeqId_Type = Gauge32
_CfprApMgmtImporterFsmTaskSeqId_Object = MibTableColumn
cfprApMgmtImporterFsmTaskSeqId = _CfprApMgmtImporterFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 39, 1, 7),
    _CfprApMgmtImporterFsmTaskSeqId_Type()
)
cfprApMgmtImporterFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtImporterFsmTaskSeqId.setStatus("current")
_CfprApMgmtInbandProfileTable_Object = MibTable
cfprApMgmtInbandProfileTable = _CfprApMgmtInbandProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 40)
)
if mibBuilder.loadTexts:
    cfprApMgmtInbandProfileTable.setStatus("current")
_CfprApMgmtInbandProfileEntry_Object = MibTableRow
cfprApMgmtInbandProfileEntry = _CfprApMgmtInbandProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 40, 1)
)
cfprApMgmtInbandProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtInbandProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtInbandProfileEntry.setStatus("current")
_CfprApMgmtInbandProfileInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtInbandProfileInstanceId_Object = MibTableColumn
cfprApMgmtInbandProfileInstanceId = _CfprApMgmtInbandProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 40, 1, 1),
    _CfprApMgmtInbandProfileInstanceId_Type()
)
cfprApMgmtInbandProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtInbandProfileInstanceId.setStatus("current")
_CfprApMgmtInbandProfileDn_Type = CfprApManagedObjectDn
_CfprApMgmtInbandProfileDn_Object = MibTableColumn
cfprApMgmtInbandProfileDn = _CfprApMgmtInbandProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 40, 1, 2),
    _CfprApMgmtInbandProfileDn_Type()
)
cfprApMgmtInbandProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInbandProfileDn.setStatus("current")
_CfprApMgmtInbandProfileRn_Type = SnmpAdminString
_CfprApMgmtInbandProfileRn_Object = MibTableColumn
cfprApMgmtInbandProfileRn = _CfprApMgmtInbandProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 40, 1, 3),
    _CfprApMgmtInbandProfileRn_Type()
)
cfprApMgmtInbandProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInbandProfileRn.setStatus("current")
_CfprApMgmtInbandProfileDefaultVlanName_Type = SnmpAdminString
_CfprApMgmtInbandProfileDefaultVlanName_Object = MibTableColumn
cfprApMgmtInbandProfileDefaultVlanName = _CfprApMgmtInbandProfileDefaultVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 40, 1, 4),
    _CfprApMgmtInbandProfileDefaultVlanName_Type()
)
cfprApMgmtInbandProfileDefaultVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInbandProfileDefaultVlanName.setStatus("current")
_CfprApMgmtInbandProfileName_Type = SnmpAdminString
_CfprApMgmtInbandProfileName_Object = MibTableColumn
cfprApMgmtInbandProfileName = _CfprApMgmtInbandProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 40, 1, 5),
    _CfprApMgmtInbandProfileName_Type()
)
cfprApMgmtInbandProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInbandProfileName.setStatus("current")
_CfprApMgmtInbandProfilePoolName_Type = SnmpAdminString
_CfprApMgmtInbandProfilePoolName_Object = MibTableColumn
cfprApMgmtInbandProfilePoolName = _CfprApMgmtInbandProfilePoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 40, 1, 6),
    _CfprApMgmtInbandProfilePoolName_Type()
)
cfprApMgmtInbandProfilePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInbandProfilePoolName.setStatus("current")
_CfprApMgmtIntAuthPolicyTable_Object = MibTable
cfprApMgmtIntAuthPolicyTable = _CfprApMgmtIntAuthPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 41)
)
if mibBuilder.loadTexts:
    cfprApMgmtIntAuthPolicyTable.setStatus("current")
_CfprApMgmtIntAuthPolicyEntry_Object = MibTableRow
cfprApMgmtIntAuthPolicyEntry = _CfprApMgmtIntAuthPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 41, 1)
)
cfprApMgmtIntAuthPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtIntAuthPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtIntAuthPolicyEntry.setStatus("current")
_CfprApMgmtIntAuthPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtIntAuthPolicyInstanceId_Object = MibTableColumn
cfprApMgmtIntAuthPolicyInstanceId = _CfprApMgmtIntAuthPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 41, 1, 1),
    _CfprApMgmtIntAuthPolicyInstanceId_Type()
)
cfprApMgmtIntAuthPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtIntAuthPolicyInstanceId.setStatus("current")
_CfprApMgmtIntAuthPolicyDn_Type = CfprApManagedObjectDn
_CfprApMgmtIntAuthPolicyDn_Object = MibTableColumn
cfprApMgmtIntAuthPolicyDn = _CfprApMgmtIntAuthPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 41, 1, 2),
    _CfprApMgmtIntAuthPolicyDn_Type()
)
cfprApMgmtIntAuthPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIntAuthPolicyDn.setStatus("current")
_CfprApMgmtIntAuthPolicyRn_Type = SnmpAdminString
_CfprApMgmtIntAuthPolicyRn_Object = MibTableColumn
cfprApMgmtIntAuthPolicyRn = _CfprApMgmtIntAuthPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 41, 1, 3),
    _CfprApMgmtIntAuthPolicyRn_Type()
)
cfprApMgmtIntAuthPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIntAuthPolicyRn.setStatus("current")
_CfprApMgmtIntAuthPolicyMethod_Type = CfprApMgmtIntAuthPolicyMethod
_CfprApMgmtIntAuthPolicyMethod_Object = MibTableColumn
cfprApMgmtIntAuthPolicyMethod = _CfprApMgmtIntAuthPolicyMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 41, 1, 4),
    _CfprApMgmtIntAuthPolicyMethod_Type()
)
cfprApMgmtIntAuthPolicyMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIntAuthPolicyMethod.setStatus("current")
_CfprApMgmtIntAuthPolicyName_Type = SnmpAdminString
_CfprApMgmtIntAuthPolicyName_Object = MibTableColumn
cfprApMgmtIntAuthPolicyName = _CfprApMgmtIntAuthPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 41, 1, 5),
    _CfprApMgmtIntAuthPolicyName_Type()
)
cfprApMgmtIntAuthPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIntAuthPolicyName.setStatus("current")
_CfprApMgmtIntAuthPolicyPwd_Type = SnmpAdminString
_CfprApMgmtIntAuthPolicyPwd_Object = MibTableColumn
cfprApMgmtIntAuthPolicyPwd = _CfprApMgmtIntAuthPolicyPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 41, 1, 6),
    _CfprApMgmtIntAuthPolicyPwd_Type()
)
cfprApMgmtIntAuthPolicyPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtIntAuthPolicyPwd.setStatus("current")
_CfprApMgmtInterfaceTable_Object = MibTable
cfprApMgmtInterfaceTable = _CfprApMgmtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 42)
)
if mibBuilder.loadTexts:
    cfprApMgmtInterfaceTable.setStatus("current")
_CfprApMgmtInterfaceEntry_Object = MibTableRow
cfprApMgmtInterfaceEntry = _CfprApMgmtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 42, 1)
)
cfprApMgmtInterfaceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtInterfaceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtInterfaceEntry.setStatus("current")
_CfprApMgmtInterfaceInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtInterfaceInstanceId_Object = MibTableColumn
cfprApMgmtInterfaceInstanceId = _CfprApMgmtInterfaceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 42, 1, 1),
    _CfprApMgmtInterfaceInstanceId_Type()
)
cfprApMgmtInterfaceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtInterfaceInstanceId.setStatus("current")
_CfprApMgmtInterfaceDn_Type = CfprApManagedObjectDn
_CfprApMgmtInterfaceDn_Object = MibTableColumn
cfprApMgmtInterfaceDn = _CfprApMgmtInterfaceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 42, 1, 2),
    _CfprApMgmtInterfaceDn_Type()
)
cfprApMgmtInterfaceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInterfaceDn.setStatus("current")
_CfprApMgmtInterfaceRn_Type = SnmpAdminString
_CfprApMgmtInterfaceRn_Object = MibTableColumn
cfprApMgmtInterfaceRn = _CfprApMgmtInterfaceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 42, 1, 3),
    _CfprApMgmtInterfaceRn_Type()
)
cfprApMgmtInterfaceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInterfaceRn.setStatus("current")
_CfprApMgmtInterfaceConfigMessage_Type = SnmpAdminString
_CfprApMgmtInterfaceConfigMessage_Object = MibTableColumn
cfprApMgmtInterfaceConfigMessage = _CfprApMgmtInterfaceConfigMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 42, 1, 4),
    _CfprApMgmtInterfaceConfigMessage_Type()
)
cfprApMgmtInterfaceConfigMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInterfaceConfigMessage.setStatus("current")
_CfprApMgmtInterfaceConfigState_Type = CfprApMgmtConfigState
_CfprApMgmtInterfaceConfigState_Object = MibTableColumn
cfprApMgmtInterfaceConfigState = _CfprApMgmtInterfaceConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 42, 1, 5),
    _CfprApMgmtInterfaceConfigState_Type()
)
cfprApMgmtInterfaceConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInterfaceConfigState.setStatus("current")
_CfprApMgmtInterfaceIpV4State_Type = CfprApVnicExternalMgmtIPMode
_CfprApMgmtInterfaceIpV4State_Object = MibTableColumn
cfprApMgmtInterfaceIpV4State = _CfprApMgmtInterfaceIpV4State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 42, 1, 6),
    _CfprApMgmtInterfaceIpV4State_Type()
)
cfprApMgmtInterfaceIpV4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInterfaceIpV4State.setStatus("current")
_CfprApMgmtInterfaceIpV6State_Type = CfprApVnicExternalMgmtIPMode
_CfprApMgmtInterfaceIpV6State_Object = MibTableColumn
cfprApMgmtInterfaceIpV6State = _CfprApMgmtInterfaceIpV6State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 42, 1, 7),
    _CfprApMgmtInterfaceIpV6State_Type()
)
cfprApMgmtInterfaceIpV6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInterfaceIpV6State.setStatus("current")
_CfprApMgmtInterfaceIsDefaultDerived_Type = TruthValue
_CfprApMgmtInterfaceIsDefaultDerived_Object = MibTableColumn
cfprApMgmtInterfaceIsDefaultDerived = _CfprApMgmtInterfaceIsDefaultDerived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 42, 1, 8),
    _CfprApMgmtInterfaceIsDefaultDerived_Type()
)
cfprApMgmtInterfaceIsDefaultDerived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInterfaceIsDefaultDerived.setStatus("current")
_CfprApMgmtInterfaceMode_Type = CfprApMgmtMode
_CfprApMgmtInterfaceMode_Object = MibTableColumn
cfprApMgmtInterfaceMode = _CfprApMgmtInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 42, 1, 9),
    _CfprApMgmtInterfaceMode_Type()
)
cfprApMgmtInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInterfaceMode.setStatus("current")
_CfprApMgmtInterfaceOperState_Type = CfprApMgmtOperState
_CfprApMgmtInterfaceOperState_Object = MibTableColumn
cfprApMgmtInterfaceOperState = _CfprApMgmtInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 42, 1, 10),
    _CfprApMgmtInterfaceOperState_Type()
)
cfprApMgmtInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtInterfaceOperState.setStatus("current")
_CfprApMgmtPmonEntryTable_Object = MibTable
cfprApMgmtPmonEntryTable = _CfprApMgmtPmonEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43)
)
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryTable.setStatus("current")
_CfprApMgmtPmonEntryEntry_Object = MibTableRow
cfprApMgmtPmonEntryEntry = _CfprApMgmtPmonEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1)
)
cfprApMgmtPmonEntryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtPmonEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryEntry.setStatus("current")
_CfprApMgmtPmonEntryInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtPmonEntryInstanceId_Object = MibTableColumn
cfprApMgmtPmonEntryInstanceId = _CfprApMgmtPmonEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 1),
    _CfprApMgmtPmonEntryInstanceId_Type()
)
cfprApMgmtPmonEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryInstanceId.setStatus("current")
_CfprApMgmtPmonEntryDn_Type = CfprApManagedObjectDn
_CfprApMgmtPmonEntryDn_Object = MibTableColumn
cfprApMgmtPmonEntryDn = _CfprApMgmtPmonEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 2),
    _CfprApMgmtPmonEntryDn_Type()
)
cfprApMgmtPmonEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryDn.setStatus("current")
_CfprApMgmtPmonEntryRn_Type = SnmpAdminString
_CfprApMgmtPmonEntryRn_Object = MibTableColumn
cfprApMgmtPmonEntryRn = _CfprApMgmtPmonEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 3),
    _CfprApMgmtPmonEntryRn_Type()
)
cfprApMgmtPmonEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryRn.setStatus("current")
_CfprApMgmtPmonEntryExitSignal_Type = Gauge32
_CfprApMgmtPmonEntryExitSignal_Object = MibTableColumn
cfprApMgmtPmonEntryExitSignal = _CfprApMgmtPmonEntryExitSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 4),
    _CfprApMgmtPmonEntryExitSignal_Type()
)
cfprApMgmtPmonEntryExitSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryExitSignal.setStatus("current")
_CfprApMgmtPmonEntryFullPathname_Type = SnmpAdminString
_CfprApMgmtPmonEntryFullPathname_Object = MibTableColumn
cfprApMgmtPmonEntryFullPathname = _CfprApMgmtPmonEntryFullPathname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 5),
    _CfprApMgmtPmonEntryFullPathname_Type()
)
cfprApMgmtPmonEntryFullPathname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryFullPathname.setStatus("current")
_CfprApMgmtPmonEntryHeapSize_Type = Unsigned64
_CfprApMgmtPmonEntryHeapSize_Object = MibTableColumn
cfprApMgmtPmonEntryHeapSize = _CfprApMgmtPmonEntryHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 6),
    _CfprApMgmtPmonEntryHeapSize_Type()
)
cfprApMgmtPmonEntryHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryHeapSize.setStatus("current")
_CfprApMgmtPmonEntryHeapSize16Gb_Type = Unsigned64
_CfprApMgmtPmonEntryHeapSize16Gb_Object = MibTableColumn
cfprApMgmtPmonEntryHeapSize16Gb = _CfprApMgmtPmonEntryHeapSize16Gb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 7),
    _CfprApMgmtPmonEntryHeapSize16Gb_Type()
)
cfprApMgmtPmonEntryHeapSize16Gb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryHeapSize16Gb.setStatus("current")
_CfprApMgmtPmonEntryLastExitCode_Type = Gauge32
_CfprApMgmtPmonEntryLastExitCode_Object = MibTableColumn
cfprApMgmtPmonEntryLastExitCode = _CfprApMgmtPmonEntryLastExitCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 8),
    _CfprApMgmtPmonEntryLastExitCode_Type()
)
cfprApMgmtPmonEntryLastExitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryLastExitCode.setStatus("current")
_CfprApMgmtPmonEntryMaxRetries_Type = Gauge32
_CfprApMgmtPmonEntryMaxRetries_Object = MibTableColumn
cfprApMgmtPmonEntryMaxRetries = _CfprApMgmtPmonEntryMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 9),
    _CfprApMgmtPmonEntryMaxRetries_Type()
)
cfprApMgmtPmonEntryMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryMaxRetries.setStatus("current")
_CfprApMgmtPmonEntryName_Type = SnmpAdminString
_CfprApMgmtPmonEntryName_Object = MibTableColumn
cfprApMgmtPmonEntryName = _CfprApMgmtPmonEntryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 10),
    _CfprApMgmtPmonEntryName_Type()
)
cfprApMgmtPmonEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryName.setStatus("current")
_CfprApMgmtPmonEntryRetries_Type = Gauge32
_CfprApMgmtPmonEntryRetries_Object = MibTableColumn
cfprApMgmtPmonEntryRetries = _CfprApMgmtPmonEntryRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 11),
    _CfprApMgmtPmonEntryRetries_Type()
)
cfprApMgmtPmonEntryRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryRetries.setStatus("current")
_CfprApMgmtPmonEntrySpuriousRetries_Type = Gauge32
_CfprApMgmtPmonEntrySpuriousRetries_Object = MibTableColumn
cfprApMgmtPmonEntrySpuriousRetries = _CfprApMgmtPmonEntrySpuriousRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 12),
    _CfprApMgmtPmonEntrySpuriousRetries_Type()
)
cfprApMgmtPmonEntrySpuriousRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntrySpuriousRetries.setStatus("current")
_CfprApMgmtPmonEntryState_Type = CfprApMgmtPmonEntryState
_CfprApMgmtPmonEntryState_Object = MibTableColumn
cfprApMgmtPmonEntryState = _CfprApMgmtPmonEntryState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 13),
    _CfprApMgmtPmonEntryState_Type()
)
cfprApMgmtPmonEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryState.setStatus("current")
_CfprApMgmtPmonEntrySwitchId_Type = CfprApNetworkSwitchId
_CfprApMgmtPmonEntrySwitchId_Object = MibTableColumn
cfprApMgmtPmonEntrySwitchId = _CfprApMgmtPmonEntrySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 14),
    _CfprApMgmtPmonEntrySwitchId_Type()
)
cfprApMgmtPmonEntrySwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntrySwitchId.setStatus("current")
_CfprApMgmtPmonEntryWorkingDirectory_Type = SnmpAdminString
_CfprApMgmtPmonEntryWorkingDirectory_Object = MibTableColumn
cfprApMgmtPmonEntryWorkingDirectory = _CfprApMgmtPmonEntryWorkingDirectory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 43, 1, 15),
    _CfprApMgmtPmonEntryWorkingDirectory_Type()
)
cfprApMgmtPmonEntryWorkingDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtPmonEntryWorkingDirectory.setStatus("current")
_CfprApMgmtProfDerivedInterfaceTable_Object = MibTable
cfprApMgmtProfDerivedInterfaceTable = _CfprApMgmtProfDerivedInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 44)
)
if mibBuilder.loadTexts:
    cfprApMgmtProfDerivedInterfaceTable.setStatus("current")
_CfprApMgmtProfDerivedInterfaceEntry_Object = MibTableRow
cfprApMgmtProfDerivedInterfaceEntry = _CfprApMgmtProfDerivedInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 44, 1)
)
cfprApMgmtProfDerivedInterfaceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtProfDerivedInterfaceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtProfDerivedInterfaceEntry.setStatus("current")
_CfprApMgmtProfDerivedInterfaceInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtProfDerivedInterfaceInstanceId_Object = MibTableColumn
cfprApMgmtProfDerivedInterfaceInstanceId = _CfprApMgmtProfDerivedInterfaceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 44, 1, 1),
    _CfprApMgmtProfDerivedInterfaceInstanceId_Type()
)
cfprApMgmtProfDerivedInterfaceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtProfDerivedInterfaceInstanceId.setStatus("current")
_CfprApMgmtProfDerivedInterfaceDn_Type = CfprApManagedObjectDn
_CfprApMgmtProfDerivedInterfaceDn_Object = MibTableColumn
cfprApMgmtProfDerivedInterfaceDn = _CfprApMgmtProfDerivedInterfaceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 44, 1, 2),
    _CfprApMgmtProfDerivedInterfaceDn_Type()
)
cfprApMgmtProfDerivedInterfaceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtProfDerivedInterfaceDn.setStatus("current")
_CfprApMgmtProfDerivedInterfaceRn_Type = SnmpAdminString
_CfprApMgmtProfDerivedInterfaceRn_Object = MibTableColumn
cfprApMgmtProfDerivedInterfaceRn = _CfprApMgmtProfDerivedInterfaceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 44, 1, 3),
    _CfprApMgmtProfDerivedInterfaceRn_Type()
)
cfprApMgmtProfDerivedInterfaceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtProfDerivedInterfaceRn.setStatus("current")
_CfprApMgmtProfDerivedInterfaceConfigMessage_Type = SnmpAdminString
_CfprApMgmtProfDerivedInterfaceConfigMessage_Object = MibTableColumn
cfprApMgmtProfDerivedInterfaceConfigMessage = _CfprApMgmtProfDerivedInterfaceConfigMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 44, 1, 4),
    _CfprApMgmtProfDerivedInterfaceConfigMessage_Type()
)
cfprApMgmtProfDerivedInterfaceConfigMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtProfDerivedInterfaceConfigMessage.setStatus("current")
_CfprApMgmtProfDerivedInterfaceConfigState_Type = CfprApMgmtConfigState
_CfprApMgmtProfDerivedInterfaceConfigState_Object = MibTableColumn
cfprApMgmtProfDerivedInterfaceConfigState = _CfprApMgmtProfDerivedInterfaceConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 44, 1, 5),
    _CfprApMgmtProfDerivedInterfaceConfigState_Type()
)
cfprApMgmtProfDerivedInterfaceConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtProfDerivedInterfaceConfigState.setStatus("current")
_CfprApMgmtProfDerivedInterfaceIpV4State_Type = CfprApVnicExternalMgmtIPMode
_CfprApMgmtProfDerivedInterfaceIpV4State_Object = MibTableColumn
cfprApMgmtProfDerivedInterfaceIpV4State = _CfprApMgmtProfDerivedInterfaceIpV4State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 44, 1, 6),
    _CfprApMgmtProfDerivedInterfaceIpV4State_Type()
)
cfprApMgmtProfDerivedInterfaceIpV4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtProfDerivedInterfaceIpV4State.setStatus("current")
_CfprApMgmtProfDerivedInterfaceIpV6State_Type = CfprApVnicExternalMgmtIPMode
_CfprApMgmtProfDerivedInterfaceIpV6State_Object = MibTableColumn
cfprApMgmtProfDerivedInterfaceIpV6State = _CfprApMgmtProfDerivedInterfaceIpV6State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 44, 1, 7),
    _CfprApMgmtProfDerivedInterfaceIpV6State_Type()
)
cfprApMgmtProfDerivedInterfaceIpV6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtProfDerivedInterfaceIpV6State.setStatus("current")
_CfprApMgmtProfDerivedInterfaceMode_Type = CfprApMgmtMode
_CfprApMgmtProfDerivedInterfaceMode_Object = MibTableColumn
cfprApMgmtProfDerivedInterfaceMode = _CfprApMgmtProfDerivedInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 44, 1, 8),
    _CfprApMgmtProfDerivedInterfaceMode_Type()
)
cfprApMgmtProfDerivedInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtProfDerivedInterfaceMode.setStatus("current")
_CfprApMgmtProfDerivedInterfaceOperState_Type = CfprApMgmtOperState
_CfprApMgmtProfDerivedInterfaceOperState_Object = MibTableColumn
cfprApMgmtProfDerivedInterfaceOperState = _CfprApMgmtProfDerivedInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 44, 1, 9),
    _CfprApMgmtProfDerivedInterfaceOperState_Type()
)
cfprApMgmtProfDerivedInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtProfDerivedInterfaceOperState.setStatus("current")
_CfprApMgmtVnetTable_Object = MibTable
cfprApMgmtVnetTable = _CfprApMgmtVnetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 45)
)
if mibBuilder.loadTexts:
    cfprApMgmtVnetTable.setStatus("current")
_CfprApMgmtVnetEntry_Object = MibTableRow
cfprApMgmtVnetEntry = _CfprApMgmtVnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 45, 1)
)
cfprApMgmtVnetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MGMT-MIB", "cfprApMgmtVnetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMgmtVnetEntry.setStatus("current")
_CfprApMgmtVnetInstanceId_Type = CfprApManagedObjectId
_CfprApMgmtVnetInstanceId_Object = MibTableColumn
cfprApMgmtVnetInstanceId = _CfprApMgmtVnetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 45, 1, 1),
    _CfprApMgmtVnetInstanceId_Type()
)
cfprApMgmtVnetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMgmtVnetInstanceId.setStatus("current")
_CfprApMgmtVnetDn_Type = CfprApManagedObjectDn
_CfprApMgmtVnetDn_Object = MibTableColumn
cfprApMgmtVnetDn = _CfprApMgmtVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 45, 1, 2),
    _CfprApMgmtVnetDn_Type()
)
cfprApMgmtVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtVnetDn.setStatus("current")
_CfprApMgmtVnetRn_Type = SnmpAdminString
_CfprApMgmtVnetRn_Object = MibTableColumn
cfprApMgmtVnetRn = _CfprApMgmtVnetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 45, 1, 3),
    _CfprApMgmtVnetRn_Type()
)
cfprApMgmtVnetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtVnetRn.setStatus("current")
_CfprApMgmtVnetConfigState_Type = CfprApMgmtConfigState
_CfprApMgmtVnetConfigState_Object = MibTableColumn
cfprApMgmtVnetConfigState = _CfprApMgmtVnetConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 45, 1, 4),
    _CfprApMgmtVnetConfigState_Type()
)
cfprApMgmtVnetConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtVnetConfigState.setStatus("current")
_CfprApMgmtVnetId_Type = Gauge32
_CfprApMgmtVnetId_Object = MibTableColumn
cfprApMgmtVnetId = _CfprApMgmtVnetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 45, 1, 5),
    _CfprApMgmtVnetId_Type()
)
cfprApMgmtVnetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtVnetId.setStatus("current")
_CfprApMgmtVnetName_Type = SnmpAdminString
_CfprApMgmtVnetName_Object = MibTableColumn
cfprApMgmtVnetName = _CfprApMgmtVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 51, 45, 1, 6),
    _CfprApMgmtVnetName_Type()
)
cfprApMgmtVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMgmtVnetName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-MGMT-MIB",
    **{"cfprApMgmtObjects": cfprApMgmtObjects,
       "cfprApMgmtAccessPolicyTable": cfprApMgmtAccessPolicyTable,
       "cfprApMgmtAccessPolicyEntry": cfprApMgmtAccessPolicyEntry,
       "cfprApMgmtAccessPolicyInstanceId": cfprApMgmtAccessPolicyInstanceId,
       "cfprApMgmtAccessPolicyDn": cfprApMgmtAccessPolicyDn,
       "cfprApMgmtAccessPolicyRn": cfprApMgmtAccessPolicyRn,
       "cfprApMgmtAccessPolicyItemTable": cfprApMgmtAccessPolicyItemTable,
       "cfprApMgmtAccessPolicyItemEntry": cfprApMgmtAccessPolicyItemEntry,
       "cfprApMgmtAccessPolicyItemInstanceId": cfprApMgmtAccessPolicyItemInstanceId,
       "cfprApMgmtAccessPolicyItemDn": cfprApMgmtAccessPolicyItemDn,
       "cfprApMgmtAccessPolicyItemRn": cfprApMgmtAccessPolicyItemRn,
       "cfprApMgmtAccessPolicyItemDescr": cfprApMgmtAccessPolicyItemDescr,
       "cfprApMgmtAccessPolicyItemIntId": cfprApMgmtAccessPolicyItemIntId,
       "cfprApMgmtAccessPolicyItemIpPoolName": cfprApMgmtAccessPolicyItemIpPoolName,
       "cfprApMgmtAccessPolicyItemName": cfprApMgmtAccessPolicyItemName,
       "cfprApMgmtAccessPolicyItemPolicyLevel": cfprApMgmtAccessPolicyItemPolicyLevel,
       "cfprApMgmtAccessPolicyItemPolicyOwner": cfprApMgmtAccessPolicyItemPolicyOwner,
       "cfprApMgmtAccessPolicyItemSubject": cfprApMgmtAccessPolicyItemSubject,
       "cfprApMgmtAccessPortTable": cfprApMgmtAccessPortTable,
       "cfprApMgmtAccessPortEntry": cfprApMgmtAccessPortEntry,
       "cfprApMgmtAccessPortInstanceId": cfprApMgmtAccessPortInstanceId,
       "cfprApMgmtAccessPortDn": cfprApMgmtAccessPortDn,
       "cfprApMgmtAccessPortRn": cfprApMgmtAccessPortRn,
       "cfprApMgmtAccessPortPort": cfprApMgmtAccessPortPort,
       "cfprApMgmtAccessPortProtocol": cfprApMgmtAccessPortProtocol,
       "cfprApMgmtBackupTable": cfprApMgmtBackupTable,
       "cfprApMgmtBackupEntry": cfprApMgmtBackupEntry,
       "cfprApMgmtBackupInstanceId": cfprApMgmtBackupInstanceId,
       "cfprApMgmtBackupDn": cfprApMgmtBackupDn,
       "cfprApMgmtBackupRn": cfprApMgmtBackupRn,
       "cfprApMgmtBackupAdminState": cfprApMgmtBackupAdminState,
       "cfprApMgmtBackupDescr": cfprApMgmtBackupDescr,
       "cfprApMgmtBackupFsmDescr": cfprApMgmtBackupFsmDescr,
       "cfprApMgmtBackupFsmPrev": cfprApMgmtBackupFsmPrev,
       "cfprApMgmtBackupFsmProgr": cfprApMgmtBackupFsmProgr,
       "cfprApMgmtBackupFsmRmtInvErrCode": cfprApMgmtBackupFsmRmtInvErrCode,
       "cfprApMgmtBackupFsmRmtInvErrDescr": cfprApMgmtBackupFsmRmtInvErrDescr,
       "cfprApMgmtBackupFsmRmtInvRslt": cfprApMgmtBackupFsmRmtInvRslt,
       "cfprApMgmtBackupFsmStageDescr": cfprApMgmtBackupFsmStageDescr,
       "cfprApMgmtBackupFsmStamp": cfprApMgmtBackupFsmStamp,
       "cfprApMgmtBackupFsmStatus": cfprApMgmtBackupFsmStatus,
       "cfprApMgmtBackupFsmTry": cfprApMgmtBackupFsmTry,
       "cfprApMgmtBackupHostname": cfprApMgmtBackupHostname,
       "cfprApMgmtBackupIntId": cfprApMgmtBackupIntId,
       "cfprApMgmtBackupJob": cfprApMgmtBackupJob,
       "cfprApMgmtBackupMaxFiles": cfprApMgmtBackupMaxFiles,
       "cfprApMgmtBackupName": cfprApMgmtBackupName,
       "cfprApMgmtBackupOperStatus": cfprApMgmtBackupOperStatus,
       "cfprApMgmtBackupOwnerPolicy": cfprApMgmtBackupOwnerPolicy,
       "cfprApMgmtBackupPolicyLevel": cfprApMgmtBackupPolicyLevel,
       "cfprApMgmtBackupPolicyOwner": cfprApMgmtBackupPolicyOwner,
       "cfprApMgmtBackupPort": cfprApMgmtBackupPort,
       "cfprApMgmtBackupPostAction": cfprApMgmtBackupPostAction,
       "cfprApMgmtBackupPreservePooledValues": cfprApMgmtBackupPreservePooledValues,
       "cfprApMgmtBackupProto": cfprApMgmtBackupProto,
       "cfprApMgmtBackupPwd": cfprApMgmtBackupPwd,
       "cfprApMgmtBackupRemoteFile": cfprApMgmtBackupRemoteFile,
       "cfprApMgmtBackupType": cfprApMgmtBackupType,
       "cfprApMgmtBackupUser": cfprApMgmtBackupUser,
       "cfprApMgmtBackupExportExtPolicyTable": cfprApMgmtBackupExportExtPolicyTable,
       "cfprApMgmtBackupExportExtPolicyEntry": cfprApMgmtBackupExportExtPolicyEntry,
       "cfprApMgmtBackupExportExtPolicyInstanceId": cfprApMgmtBackupExportExtPolicyInstanceId,
       "cfprApMgmtBackupExportExtPolicyDn": cfprApMgmtBackupExportExtPolicyDn,
       "cfprApMgmtBackupExportExtPolicyRn": cfprApMgmtBackupExportExtPolicyRn,
       "cfprApMgmtBackupExportExtPolicyAdminState": cfprApMgmtBackupExportExtPolicyAdminState,
       "cfprApMgmtBackupExportExtPolicyDescr": cfprApMgmtBackupExportExtPolicyDescr,
       "cfprApMgmtBackupExportExtPolicyFrequency": cfprApMgmtBackupExportExtPolicyFrequency,
       "cfprApMgmtBackupExportExtPolicyIntId": cfprApMgmtBackupExportExtPolicyIntId,
       "cfprApMgmtBackupExportExtPolicyName": cfprApMgmtBackupExportExtPolicyName,
       "cfprApMgmtBackupExportExtPolicyPolicyLevel": cfprApMgmtBackupExportExtPolicyPolicyLevel,
       "cfprApMgmtBackupExportExtPolicyPolicyOwner": cfprApMgmtBackupExportExtPolicyPolicyOwner,
       "cfprApMgmtBackupFsmTable": cfprApMgmtBackupFsmTable,
       "cfprApMgmtBackupFsmEntry": cfprApMgmtBackupFsmEntry,
       "cfprApMgmtBackupFsmInstanceId": cfprApMgmtBackupFsmInstanceId,
       "cfprApMgmtBackupFsmDn": cfprApMgmtBackupFsmDn,
       "cfprApMgmtBackupFsmRn": cfprApMgmtBackupFsmRn,
       "cfprApMgmtBackupFsmCompletionTime": cfprApMgmtBackupFsmCompletionTime,
       "cfprApMgmtBackupFsmCurrentFsm": cfprApMgmtBackupFsmCurrentFsm,
       "cfprApMgmtBackupFsmDescrData": cfprApMgmtBackupFsmDescrData,
       "cfprApMgmtBackupFsmFsmStatus": cfprApMgmtBackupFsmFsmStatus,
       "cfprApMgmtBackupFsmProgress": cfprApMgmtBackupFsmProgress,
       "cfprApMgmtBackupFsmRmtErrCode": cfprApMgmtBackupFsmRmtErrCode,
       "cfprApMgmtBackupFsmRmtErrDescr": cfprApMgmtBackupFsmRmtErrDescr,
       "cfprApMgmtBackupFsmRmtRslt": cfprApMgmtBackupFsmRmtRslt,
       "cfprApMgmtBackupFsmStageTable": cfprApMgmtBackupFsmStageTable,
       "cfprApMgmtBackupFsmStageEntry": cfprApMgmtBackupFsmStageEntry,
       "cfprApMgmtBackupFsmStageInstanceId": cfprApMgmtBackupFsmStageInstanceId,
       "cfprApMgmtBackupFsmStageDn": cfprApMgmtBackupFsmStageDn,
       "cfprApMgmtBackupFsmStageRn": cfprApMgmtBackupFsmStageRn,
       "cfprApMgmtBackupFsmStageDescrData": cfprApMgmtBackupFsmStageDescrData,
       "cfprApMgmtBackupFsmStageLastUpdateTime": cfprApMgmtBackupFsmStageLastUpdateTime,
       "cfprApMgmtBackupFsmStageName": cfprApMgmtBackupFsmStageName,
       "cfprApMgmtBackupFsmStageOrder": cfprApMgmtBackupFsmStageOrder,
       "cfprApMgmtBackupFsmStageRetry": cfprApMgmtBackupFsmStageRetry,
       "cfprApMgmtBackupFsmStageStageStatus": cfprApMgmtBackupFsmStageStageStatus,
       "cfprApMgmtBackupFsmTaskTable": cfprApMgmtBackupFsmTaskTable,
       "cfprApMgmtBackupFsmTaskEntry": cfprApMgmtBackupFsmTaskEntry,
       "cfprApMgmtBackupFsmTaskInstanceId": cfprApMgmtBackupFsmTaskInstanceId,
       "cfprApMgmtBackupFsmTaskDn": cfprApMgmtBackupFsmTaskDn,
       "cfprApMgmtBackupFsmTaskRn": cfprApMgmtBackupFsmTaskRn,
       "cfprApMgmtBackupFsmTaskCompletion": cfprApMgmtBackupFsmTaskCompletion,
       "cfprApMgmtBackupFsmTaskFlags": cfprApMgmtBackupFsmTaskFlags,
       "cfprApMgmtBackupFsmTaskItem": cfprApMgmtBackupFsmTaskItem,
       "cfprApMgmtBackupFsmTaskSeqId": cfprApMgmtBackupFsmTaskSeqId,
       "cfprApMgmtBackupPolicyTable": cfprApMgmtBackupPolicyTable,
       "cfprApMgmtBackupPolicyEntry": cfprApMgmtBackupPolicyEntry,
       "cfprApMgmtBackupPolicyInstanceId": cfprApMgmtBackupPolicyInstanceId,
       "cfprApMgmtBackupPolicyDn": cfprApMgmtBackupPolicyDn,
       "cfprApMgmtBackupPolicyRn": cfprApMgmtBackupPolicyRn,
       "cfprApMgmtBackupPolicyAdminState": cfprApMgmtBackupPolicyAdminState,
       "cfprApMgmtBackupPolicyDescr": cfprApMgmtBackupPolicyDescr,
       "cfprApMgmtBackupPolicyFsmDescr": cfprApMgmtBackupPolicyFsmDescr,
       "cfprApMgmtBackupPolicyFsmPrev": cfprApMgmtBackupPolicyFsmPrev,
       "cfprApMgmtBackupPolicyFsmProgr": cfprApMgmtBackupPolicyFsmProgr,
       "cfprApMgmtBackupPolicyFsmRmtInvErrCode": cfprApMgmtBackupPolicyFsmRmtInvErrCode,
       "cfprApMgmtBackupPolicyFsmRmtInvErrDescr": cfprApMgmtBackupPolicyFsmRmtInvErrDescr,
       "cfprApMgmtBackupPolicyFsmRmtInvRslt": cfprApMgmtBackupPolicyFsmRmtInvRslt,
       "cfprApMgmtBackupPolicyFsmStageDescr": cfprApMgmtBackupPolicyFsmStageDescr,
       "cfprApMgmtBackupPolicyFsmStamp": cfprApMgmtBackupPolicyFsmStamp,
       "cfprApMgmtBackupPolicyFsmStatus": cfprApMgmtBackupPolicyFsmStatus,
       "cfprApMgmtBackupPolicyFsmTry": cfprApMgmtBackupPolicyFsmTry,
       "cfprApMgmtBackupPolicyHost": cfprApMgmtBackupPolicyHost,
       "cfprApMgmtBackupPolicyIntId": cfprApMgmtBackupPolicyIntId,
       "cfprApMgmtBackupPolicyLastBackup": cfprApMgmtBackupPolicyLastBackup,
       "cfprApMgmtBackupPolicyMaxFiles": cfprApMgmtBackupPolicyMaxFiles,
       "cfprApMgmtBackupPolicyName": cfprApMgmtBackupPolicyName,
       "cfprApMgmtBackupPolicyPolicyLevel": cfprApMgmtBackupPolicyPolicyLevel,
       "cfprApMgmtBackupPolicyPolicyOwner": cfprApMgmtBackupPolicyPolicyOwner,
       "cfprApMgmtBackupPolicyPort": cfprApMgmtBackupPolicyPort,
       "cfprApMgmtBackupPolicyProto": cfprApMgmtBackupPolicyProto,
       "cfprApMgmtBackupPolicyPwd": cfprApMgmtBackupPolicyPwd,
       "cfprApMgmtBackupPolicyRemoteFile": cfprApMgmtBackupPolicyRemoteFile,
       "cfprApMgmtBackupPolicySchedule": cfprApMgmtBackupPolicySchedule,
       "cfprApMgmtBackupPolicyUser": cfprApMgmtBackupPolicyUser,
       "cfprApMgmtBackupPolicyConfigTable": cfprApMgmtBackupPolicyConfigTable,
       "cfprApMgmtBackupPolicyConfigEntry": cfprApMgmtBackupPolicyConfigEntry,
       "cfprApMgmtBackupPolicyConfigInstanceId": cfprApMgmtBackupPolicyConfigInstanceId,
       "cfprApMgmtBackupPolicyConfigDn": cfprApMgmtBackupPolicyConfigDn,
       "cfprApMgmtBackupPolicyConfigRn": cfprApMgmtBackupPolicyConfigRn,
       "cfprApMgmtBackupPolicyConfigAdminState": cfprApMgmtBackupPolicyConfigAdminState,
       "cfprApMgmtBackupPolicyConfigAutoDelete": cfprApMgmtBackupPolicyConfigAutoDelete,
       "cfprApMgmtBackupPolicyConfigBackupDate": cfprApMgmtBackupPolicyConfigBackupDate,
       "cfprApMgmtBackupPolicyConfigBackupIssue": cfprApMgmtBackupPolicyConfigBackupIssue,
       "cfprApMgmtBackupPolicyConfigDescr": cfprApMgmtBackupPolicyConfigDescr,
       "cfprApMgmtBackupPolicyConfigIgnoreCap": cfprApMgmtBackupPolicyConfigIgnoreCap,
       "cfprApMgmtBackupPolicyConfigIntId": cfprApMgmtBackupPolicyConfigIntId,
       "cfprApMgmtBackupPolicyConfigName": cfprApMgmtBackupPolicyConfigName,
       "cfprApMgmtBackupPolicyConfigOperScheduler": cfprApMgmtBackupPolicyConfigOperScheduler,
       "cfprApMgmtBackupPolicyConfigOperState": cfprApMgmtBackupPolicyConfigOperState,
       "cfprApMgmtBackupPolicyConfigPolicyLevel": cfprApMgmtBackupPolicyConfigPolicyLevel,
       "cfprApMgmtBackupPolicyConfigPolicyOwner": cfprApMgmtBackupPolicyConfigPolicyOwner,
       "cfprApMgmtBackupPolicyConfigScheduler": cfprApMgmtBackupPolicyConfigScheduler,
       "cfprApMgmtBackupPolicyFsmTable": cfprApMgmtBackupPolicyFsmTable,
       "cfprApMgmtBackupPolicyFsmEntry": cfprApMgmtBackupPolicyFsmEntry,
       "cfprApMgmtBackupPolicyFsmInstanceId": cfprApMgmtBackupPolicyFsmInstanceId,
       "cfprApMgmtBackupPolicyFsmDn": cfprApMgmtBackupPolicyFsmDn,
       "cfprApMgmtBackupPolicyFsmRn": cfprApMgmtBackupPolicyFsmRn,
       "cfprApMgmtBackupPolicyFsmCompletionTime": cfprApMgmtBackupPolicyFsmCompletionTime,
       "cfprApMgmtBackupPolicyFsmCurrentFsm": cfprApMgmtBackupPolicyFsmCurrentFsm,
       "cfprApMgmtBackupPolicyFsmDescrData": cfprApMgmtBackupPolicyFsmDescrData,
       "cfprApMgmtBackupPolicyFsmFsmStatus": cfprApMgmtBackupPolicyFsmFsmStatus,
       "cfprApMgmtBackupPolicyFsmProgress": cfprApMgmtBackupPolicyFsmProgress,
       "cfprApMgmtBackupPolicyFsmRmtErrCode": cfprApMgmtBackupPolicyFsmRmtErrCode,
       "cfprApMgmtBackupPolicyFsmRmtErrDescr": cfprApMgmtBackupPolicyFsmRmtErrDescr,
       "cfprApMgmtBackupPolicyFsmRmtRslt": cfprApMgmtBackupPolicyFsmRmtRslt,
       "cfprApMgmtBackupPolicyFsmStageTable": cfprApMgmtBackupPolicyFsmStageTable,
       "cfprApMgmtBackupPolicyFsmStageEntry": cfprApMgmtBackupPolicyFsmStageEntry,
       "cfprApMgmtBackupPolicyFsmStageInstanceId": cfprApMgmtBackupPolicyFsmStageInstanceId,
       "cfprApMgmtBackupPolicyFsmStageDn": cfprApMgmtBackupPolicyFsmStageDn,
       "cfprApMgmtBackupPolicyFsmStageRn": cfprApMgmtBackupPolicyFsmStageRn,
       "cfprApMgmtBackupPolicyFsmStageDescrData": cfprApMgmtBackupPolicyFsmStageDescrData,
       "cfprApMgmtBackupPolicyFsmStageLastUpdateTime": cfprApMgmtBackupPolicyFsmStageLastUpdateTime,
       "cfprApMgmtBackupPolicyFsmStageName": cfprApMgmtBackupPolicyFsmStageName,
       "cfprApMgmtBackupPolicyFsmStageOrder": cfprApMgmtBackupPolicyFsmStageOrder,
       "cfprApMgmtBackupPolicyFsmStageRetry": cfprApMgmtBackupPolicyFsmStageRetry,
       "cfprApMgmtBackupPolicyFsmStageStageStatus": cfprApMgmtBackupPolicyFsmStageStageStatus,
       "cfprApMgmtCfgExportPolicyTable": cfprApMgmtCfgExportPolicyTable,
       "cfprApMgmtCfgExportPolicyEntry": cfprApMgmtCfgExportPolicyEntry,
       "cfprApMgmtCfgExportPolicyInstanceId": cfprApMgmtCfgExportPolicyInstanceId,
       "cfprApMgmtCfgExportPolicyDn": cfprApMgmtCfgExportPolicyDn,
       "cfprApMgmtCfgExportPolicyRn": cfprApMgmtCfgExportPolicyRn,
       "cfprApMgmtCfgExportPolicyAdminState": cfprApMgmtCfgExportPolicyAdminState,
       "cfprApMgmtCfgExportPolicyDescr": cfprApMgmtCfgExportPolicyDescr,
       "cfprApMgmtCfgExportPolicyFsmDescr": cfprApMgmtCfgExportPolicyFsmDescr,
       "cfprApMgmtCfgExportPolicyFsmPrev": cfprApMgmtCfgExportPolicyFsmPrev,
       "cfprApMgmtCfgExportPolicyFsmProgr": cfprApMgmtCfgExportPolicyFsmProgr,
       "cfprApMgmtCfgExportPolicyFsmRmtInvErrCode": cfprApMgmtCfgExportPolicyFsmRmtInvErrCode,
       "cfprApMgmtCfgExportPolicyFsmRmtInvErrDescr": cfprApMgmtCfgExportPolicyFsmRmtInvErrDescr,
       "cfprApMgmtCfgExportPolicyFsmRmtInvRslt": cfprApMgmtCfgExportPolicyFsmRmtInvRslt,
       "cfprApMgmtCfgExportPolicyFsmStageDescr": cfprApMgmtCfgExportPolicyFsmStageDescr,
       "cfprApMgmtCfgExportPolicyFsmStamp": cfprApMgmtCfgExportPolicyFsmStamp,
       "cfprApMgmtCfgExportPolicyFsmStatus": cfprApMgmtCfgExportPolicyFsmStatus,
       "cfprApMgmtCfgExportPolicyFsmTry": cfprApMgmtCfgExportPolicyFsmTry,
       "cfprApMgmtCfgExportPolicyHost": cfprApMgmtCfgExportPolicyHost,
       "cfprApMgmtCfgExportPolicyIntId": cfprApMgmtCfgExportPolicyIntId,
       "cfprApMgmtCfgExportPolicyLastBackup": cfprApMgmtCfgExportPolicyLastBackup,
       "cfprApMgmtCfgExportPolicyMaxFiles": cfprApMgmtCfgExportPolicyMaxFiles,
       "cfprApMgmtCfgExportPolicyName": cfprApMgmtCfgExportPolicyName,
       "cfprApMgmtCfgExportPolicyPolicyLevel": cfprApMgmtCfgExportPolicyPolicyLevel,
       "cfprApMgmtCfgExportPolicyPolicyOwner": cfprApMgmtCfgExportPolicyPolicyOwner,
       "cfprApMgmtCfgExportPolicyPort": cfprApMgmtCfgExportPolicyPort,
       "cfprApMgmtCfgExportPolicyProto": cfprApMgmtCfgExportPolicyProto,
       "cfprApMgmtCfgExportPolicyPwd": cfprApMgmtCfgExportPolicyPwd,
       "cfprApMgmtCfgExportPolicyRemoteFile": cfprApMgmtCfgExportPolicyRemoteFile,
       "cfprApMgmtCfgExportPolicySchedule": cfprApMgmtCfgExportPolicySchedule,
       "cfprApMgmtCfgExportPolicyUser": cfprApMgmtCfgExportPolicyUser,
       "cfprApMgmtCfgExportPolicyFsmTable": cfprApMgmtCfgExportPolicyFsmTable,
       "cfprApMgmtCfgExportPolicyFsmEntry": cfprApMgmtCfgExportPolicyFsmEntry,
       "cfprApMgmtCfgExportPolicyFsmInstanceId": cfprApMgmtCfgExportPolicyFsmInstanceId,
       "cfprApMgmtCfgExportPolicyFsmDn": cfprApMgmtCfgExportPolicyFsmDn,
       "cfprApMgmtCfgExportPolicyFsmRn": cfprApMgmtCfgExportPolicyFsmRn,
       "cfprApMgmtCfgExportPolicyFsmCompletionTime": cfprApMgmtCfgExportPolicyFsmCompletionTime,
       "cfprApMgmtCfgExportPolicyFsmCurrentFsm": cfprApMgmtCfgExportPolicyFsmCurrentFsm,
       "cfprApMgmtCfgExportPolicyFsmDescrData": cfprApMgmtCfgExportPolicyFsmDescrData,
       "cfprApMgmtCfgExportPolicyFsmFsmStatus": cfprApMgmtCfgExportPolicyFsmFsmStatus,
       "cfprApMgmtCfgExportPolicyFsmProgress": cfprApMgmtCfgExportPolicyFsmProgress,
       "cfprApMgmtCfgExportPolicyFsmRmtErrCode": cfprApMgmtCfgExportPolicyFsmRmtErrCode,
       "cfprApMgmtCfgExportPolicyFsmRmtErrDescr": cfprApMgmtCfgExportPolicyFsmRmtErrDescr,
       "cfprApMgmtCfgExportPolicyFsmRmtRslt": cfprApMgmtCfgExportPolicyFsmRmtRslt,
       "cfprApMgmtCfgExportPolicyFsmStageTable": cfprApMgmtCfgExportPolicyFsmStageTable,
       "cfprApMgmtCfgExportPolicyFsmStageEntry": cfprApMgmtCfgExportPolicyFsmStageEntry,
       "cfprApMgmtCfgExportPolicyFsmStageInstanceId": cfprApMgmtCfgExportPolicyFsmStageInstanceId,
       "cfprApMgmtCfgExportPolicyFsmStageDn": cfprApMgmtCfgExportPolicyFsmStageDn,
       "cfprApMgmtCfgExportPolicyFsmStageRn": cfprApMgmtCfgExportPolicyFsmStageRn,
       "cfprApMgmtCfgExportPolicyFsmStageDescrData": cfprApMgmtCfgExportPolicyFsmStageDescrData,
       "cfprApMgmtCfgExportPolicyFsmStageLastUpdateTime": cfprApMgmtCfgExportPolicyFsmStageLastUpdateTime,
       "cfprApMgmtCfgExportPolicyFsmStageName": cfprApMgmtCfgExportPolicyFsmStageName,
       "cfprApMgmtCfgExportPolicyFsmStageOrder": cfprApMgmtCfgExportPolicyFsmStageOrder,
       "cfprApMgmtCfgExportPolicyFsmStageRetry": cfprApMgmtCfgExportPolicyFsmStageRetry,
       "cfprApMgmtCfgExportPolicyFsmStageStageStatus": cfprApMgmtCfgExportPolicyFsmStageStageStatus,
       "cfprApMgmtCimcSecureBootTable": cfprApMgmtCimcSecureBootTable,
       "cfprApMgmtCimcSecureBootEntry": cfprApMgmtCimcSecureBootEntry,
       "cfprApMgmtCimcSecureBootInstanceId": cfprApMgmtCimcSecureBootInstanceId,
       "cfprApMgmtCimcSecureBootDn": cfprApMgmtCimcSecureBootDn,
       "cfprApMgmtCimcSecureBootRn": cfprApMgmtCimcSecureBootRn,
       "cfprApMgmtCimcSecureBootAdminState": cfprApMgmtCimcSecureBootAdminState,
       "cfprApMgmtCimcSecureBootOperState": cfprApMgmtCimcSecureBootOperState,
       "cfprApMgmtConnectionTable": cfprApMgmtConnectionTable,
       "cfprApMgmtConnectionEntry": cfprApMgmtConnectionEntry,
       "cfprApMgmtConnectionInstanceId": cfprApMgmtConnectionInstanceId,
       "cfprApMgmtConnectionDn": cfprApMgmtConnectionDn,
       "cfprApMgmtConnectionRn": cfprApMgmtConnectionRn,
       "cfprApMgmtConnectionAck": cfprApMgmtConnectionAck,
       "cfprApMgmtConnectionOperState": cfprApMgmtConnectionOperState,
       "cfprApMgmtConnectionType": cfprApMgmtConnectionType,
       "cfprApMgmtControllerTable": cfprApMgmtControllerTable,
       "cfprApMgmtControllerEntry": cfprApMgmtControllerEntry,
       "cfprApMgmtControllerInstanceId": cfprApMgmtControllerInstanceId,
       "cfprApMgmtControllerDn": cfprApMgmtControllerDn,
       "cfprApMgmtControllerRn": cfprApMgmtControllerRn,
       "cfprApMgmtControllerDbVersion": cfprApMgmtControllerDbVersion,
       "cfprApMgmtControllerDimmBlacklistingOperState": cfprApMgmtControllerDimmBlacklistingOperState,
       "cfprApMgmtControllerFsmDescr": cfprApMgmtControllerFsmDescr,
       "cfprApMgmtControllerFsmFlags": cfprApMgmtControllerFsmFlags,
       "cfprApMgmtControllerFsmPrev": cfprApMgmtControllerFsmPrev,
       "cfprApMgmtControllerFsmProgr": cfprApMgmtControllerFsmProgr,
       "cfprApMgmtControllerFsmRmtInvErrCode": cfprApMgmtControllerFsmRmtInvErrCode,
       "cfprApMgmtControllerFsmRmtInvErrDescr": cfprApMgmtControllerFsmRmtInvErrDescr,
       "cfprApMgmtControllerFsmRmtInvRslt": cfprApMgmtControllerFsmRmtInvRslt,
       "cfprApMgmtControllerFsmStageDescr": cfprApMgmtControllerFsmStageDescr,
       "cfprApMgmtControllerFsmStamp": cfprApMgmtControllerFsmStamp,
       "cfprApMgmtControllerFsmStatus": cfprApMgmtControllerFsmStatus,
       "cfprApMgmtControllerFsmTry": cfprApMgmtControllerFsmTry,
       "cfprApMgmtControllerGuid": cfprApMgmtControllerGuid,
       "cfprApMgmtControllerModel": cfprApMgmtControllerModel,
       "cfprApMgmtControllerOperConn": cfprApMgmtControllerOperConn,
       "cfprApMgmtControllerRevision": cfprApMgmtControllerRevision,
       "cfprApMgmtControllerSerial": cfprApMgmtControllerSerial,
       "cfprApMgmtControllerStorageOobInterfaceSupported": cfprApMgmtControllerStorageOobInterfaceSupported,
       "cfprApMgmtControllerStorageSubsystemState": cfprApMgmtControllerStorageSubsystemState,
       "cfprApMgmtControllerSubject": cfprApMgmtControllerSubject,
       "cfprApMgmtControllerVendor": cfprApMgmtControllerVendor,
       "cfprApMgmtControllerFsmTable": cfprApMgmtControllerFsmTable,
       "cfprApMgmtControllerFsmEntry": cfprApMgmtControllerFsmEntry,
       "cfprApMgmtControllerFsmInstanceId": cfprApMgmtControllerFsmInstanceId,
       "cfprApMgmtControllerFsmDn": cfprApMgmtControllerFsmDn,
       "cfprApMgmtControllerFsmRn": cfprApMgmtControllerFsmRn,
       "cfprApMgmtControllerFsmCompletionTime": cfprApMgmtControllerFsmCompletionTime,
       "cfprApMgmtControllerFsmCurrentFsm": cfprApMgmtControllerFsmCurrentFsm,
       "cfprApMgmtControllerFsmDescrData": cfprApMgmtControllerFsmDescrData,
       "cfprApMgmtControllerFsmFsmStatus": cfprApMgmtControllerFsmFsmStatus,
       "cfprApMgmtControllerFsmProgress": cfprApMgmtControllerFsmProgress,
       "cfprApMgmtControllerFsmRmtErrCode": cfprApMgmtControllerFsmRmtErrCode,
       "cfprApMgmtControllerFsmRmtErrDescr": cfprApMgmtControllerFsmRmtErrDescr,
       "cfprApMgmtControllerFsmRmtRslt": cfprApMgmtControllerFsmRmtRslt,
       "cfprApMgmtControllerFsmStageTable": cfprApMgmtControllerFsmStageTable,
       "cfprApMgmtControllerFsmStageEntry": cfprApMgmtControllerFsmStageEntry,
       "cfprApMgmtControllerFsmStageInstanceId": cfprApMgmtControllerFsmStageInstanceId,
       "cfprApMgmtControllerFsmStageDn": cfprApMgmtControllerFsmStageDn,
       "cfprApMgmtControllerFsmStageRn": cfprApMgmtControllerFsmStageRn,
       "cfprApMgmtControllerFsmStageDescrData": cfprApMgmtControllerFsmStageDescrData,
       "cfprApMgmtControllerFsmStageLastUpdateTime": cfprApMgmtControllerFsmStageLastUpdateTime,
       "cfprApMgmtControllerFsmStageName": cfprApMgmtControllerFsmStageName,
       "cfprApMgmtControllerFsmStageOrder": cfprApMgmtControllerFsmStageOrder,
       "cfprApMgmtControllerFsmStageRetry": cfprApMgmtControllerFsmStageRetry,
       "cfprApMgmtControllerFsmStageStageStatus": cfprApMgmtControllerFsmStageStageStatus,
       "cfprApMgmtControllerFsmTaskTable": cfprApMgmtControllerFsmTaskTable,
       "cfprApMgmtControllerFsmTaskEntry": cfprApMgmtControllerFsmTaskEntry,
       "cfprApMgmtControllerFsmTaskInstanceId": cfprApMgmtControllerFsmTaskInstanceId,
       "cfprApMgmtControllerFsmTaskDn": cfprApMgmtControllerFsmTaskDn,
       "cfprApMgmtControllerFsmTaskRn": cfprApMgmtControllerFsmTaskRn,
       "cfprApMgmtControllerFsmTaskCompletion": cfprApMgmtControllerFsmTaskCompletion,
       "cfprApMgmtControllerFsmTaskFlags": cfprApMgmtControllerFsmTaskFlags,
       "cfprApMgmtControllerFsmTaskItem": cfprApMgmtControllerFsmTaskItem,
       "cfprApMgmtControllerFsmTaskSeqId": cfprApMgmtControllerFsmTaskSeqId,
       "cfprApMgmtEntityTable": cfprApMgmtEntityTable,
       "cfprApMgmtEntityEntry": cfprApMgmtEntityEntry,
       "cfprApMgmtEntityInstanceId": cfprApMgmtEntityInstanceId,
       "cfprApMgmtEntityDn": cfprApMgmtEntityDn,
       "cfprApMgmtEntityRn": cfprApMgmtEntityRn,
       "cfprApMgmtEntityChassis1": cfprApMgmtEntityChassis1,
       "cfprApMgmtEntityChassis2": cfprApMgmtEntityChassis2,
       "cfprApMgmtEntityChassis3": cfprApMgmtEntityChassis3,
       "cfprApMgmtEntityChassisDeviceIoState1": cfprApMgmtEntityChassisDeviceIoState1,
       "cfprApMgmtEntityChassisDeviceIoState2": cfprApMgmtEntityChassisDeviceIoState2,
       "cfprApMgmtEntityChassisDeviceIoState3": cfprApMgmtEntityChassisDeviceIoState3,
       "cfprApMgmtEntityHaFailureReason": cfprApMgmtEntityHaFailureReason,
       "cfprApMgmtEntityHaReadiness": cfprApMgmtEntityHaReadiness,
       "cfprApMgmtEntityHaReady": cfprApMgmtEntityHaReady,
       "cfprApMgmtEntityId": cfprApMgmtEntityId,
       "cfprApMgmtEntityLeadership": cfprApMgmtEntityLeadership,
       "cfprApMgmtEntityMgmtServicesState": cfprApMgmtEntityMgmtServicesState,
       "cfprApMgmtEntityProblems": cfprApMgmtEntityProblems,
       "cfprApMgmtEntitySshAuthKeysCsum": cfprApMgmtEntitySshAuthKeysCsum,
       "cfprApMgmtEntitySshAuthKeysSize": cfprApMgmtEntitySshAuthKeysSize,
       "cfprApMgmtEntitySshKeyStatus": cfprApMgmtEntitySshKeyStatus,
       "cfprApMgmtEntitySshRootPubKeyCsum": cfprApMgmtEntitySshRootPubKeyCsum,
       "cfprApMgmtEntitySshRootPubKeySize": cfprApMgmtEntitySshRootPubKeySize,
       "cfprApMgmtEntityState": cfprApMgmtEntityState,
       "cfprApMgmtEntityUmbilicalState": cfprApMgmtEntityUmbilicalState,
       "cfprApMgmtEntityVersionMismatch": cfprApMgmtEntityVersionMismatch,
       "cfprApMgmtExportPolicyFsmTable": cfprApMgmtExportPolicyFsmTable,
       "cfprApMgmtExportPolicyFsmEntry": cfprApMgmtExportPolicyFsmEntry,
       "cfprApMgmtExportPolicyFsmInstanceId": cfprApMgmtExportPolicyFsmInstanceId,
       "cfprApMgmtExportPolicyFsmDn": cfprApMgmtExportPolicyFsmDn,
       "cfprApMgmtExportPolicyFsmRn": cfprApMgmtExportPolicyFsmRn,
       "cfprApMgmtExportPolicyFsmCompletionTime": cfprApMgmtExportPolicyFsmCompletionTime,
       "cfprApMgmtExportPolicyFsmCurrentFsm": cfprApMgmtExportPolicyFsmCurrentFsm,
       "cfprApMgmtExportPolicyFsmDescr": cfprApMgmtExportPolicyFsmDescr,
       "cfprApMgmtExportPolicyFsmFsmStatus": cfprApMgmtExportPolicyFsmFsmStatus,
       "cfprApMgmtExportPolicyFsmProgress": cfprApMgmtExportPolicyFsmProgress,
       "cfprApMgmtExportPolicyFsmRmtErrCode": cfprApMgmtExportPolicyFsmRmtErrCode,
       "cfprApMgmtExportPolicyFsmRmtErrDescr": cfprApMgmtExportPolicyFsmRmtErrDescr,
       "cfprApMgmtExportPolicyFsmRmtRslt": cfprApMgmtExportPolicyFsmRmtRslt,
       "cfprApMgmtExportPolicyFsmStageTable": cfprApMgmtExportPolicyFsmStageTable,
       "cfprApMgmtExportPolicyFsmStageEntry": cfprApMgmtExportPolicyFsmStageEntry,
       "cfprApMgmtExportPolicyFsmStageInstanceId": cfprApMgmtExportPolicyFsmStageInstanceId,
       "cfprApMgmtExportPolicyFsmStageDn": cfprApMgmtExportPolicyFsmStageDn,
       "cfprApMgmtExportPolicyFsmStageRn": cfprApMgmtExportPolicyFsmStageRn,
       "cfprApMgmtExportPolicyFsmStageDescr": cfprApMgmtExportPolicyFsmStageDescr,
       "cfprApMgmtExportPolicyFsmStageLastUpdateTime": cfprApMgmtExportPolicyFsmStageLastUpdateTime,
       "cfprApMgmtExportPolicyFsmStageName": cfprApMgmtExportPolicyFsmStageName,
       "cfprApMgmtExportPolicyFsmStageOrder": cfprApMgmtExportPolicyFsmStageOrder,
       "cfprApMgmtExportPolicyFsmStageRetry": cfprApMgmtExportPolicyFsmStageRetry,
       "cfprApMgmtExportPolicyFsmStageStageStatus": cfprApMgmtExportPolicyFsmStageStageStatus,
       "cfprApMgmtExportPolicyFsmTaskTable": cfprApMgmtExportPolicyFsmTaskTable,
       "cfprApMgmtExportPolicyFsmTaskEntry": cfprApMgmtExportPolicyFsmTaskEntry,
       "cfprApMgmtExportPolicyFsmTaskInstanceId": cfprApMgmtExportPolicyFsmTaskInstanceId,
       "cfprApMgmtExportPolicyFsmTaskDn": cfprApMgmtExportPolicyFsmTaskDn,
       "cfprApMgmtExportPolicyFsmTaskRn": cfprApMgmtExportPolicyFsmTaskRn,
       "cfprApMgmtExportPolicyFsmTaskCompletion": cfprApMgmtExportPolicyFsmTaskCompletion,
       "cfprApMgmtExportPolicyFsmTaskFlags": cfprApMgmtExportPolicyFsmTaskFlags,
       "cfprApMgmtExportPolicyFsmTaskItem": cfprApMgmtExportPolicyFsmTaskItem,
       "cfprApMgmtExportPolicyFsmTaskSeqId": cfprApMgmtExportPolicyFsmTaskSeqId,
       "cfprApMgmtIPv6IfAddrTable": cfprApMgmtIPv6IfAddrTable,
       "cfprApMgmtIPv6IfAddrEntry": cfprApMgmtIPv6IfAddrEntry,
       "cfprApMgmtIPv6IfAddrInstanceId": cfprApMgmtIPv6IfAddrInstanceId,
       "cfprApMgmtIPv6IfAddrDn": cfprApMgmtIPv6IfAddrDn,
       "cfprApMgmtIPv6IfAddrRn": cfprApMgmtIPv6IfAddrRn,
       "cfprApMgmtIPv6IfAddrAddr": cfprApMgmtIPv6IfAddrAddr,
       "cfprApMgmtIPv6IfAddrDefGw": cfprApMgmtIPv6IfAddrDefGw,
       "cfprApMgmtIPv6IfAddrFsmDescr": cfprApMgmtIPv6IfAddrFsmDescr,
       "cfprApMgmtIPv6IfAddrFsmPrev": cfprApMgmtIPv6IfAddrFsmPrev,
       "cfprApMgmtIPv6IfAddrFsmProgr": cfprApMgmtIPv6IfAddrFsmProgr,
       "cfprApMgmtIPv6IfAddrFsmRmtInvErrCode": cfprApMgmtIPv6IfAddrFsmRmtInvErrCode,
       "cfprApMgmtIPv6IfAddrFsmRmtInvErrDescr": cfprApMgmtIPv6IfAddrFsmRmtInvErrDescr,
       "cfprApMgmtIPv6IfAddrFsmRmtInvRslt": cfprApMgmtIPv6IfAddrFsmRmtInvRslt,
       "cfprApMgmtIPv6IfAddrFsmStageDescr": cfprApMgmtIPv6IfAddrFsmStageDescr,
       "cfprApMgmtIPv6IfAddrFsmStamp": cfprApMgmtIPv6IfAddrFsmStamp,
       "cfprApMgmtIPv6IfAddrFsmStatus": cfprApMgmtIPv6IfAddrFsmStatus,
       "cfprApMgmtIPv6IfAddrFsmTry": cfprApMgmtIPv6IfAddrFsmTry,
       "cfprApMgmtIPv6IfAddrPrefix": cfprApMgmtIPv6IfAddrPrefix,
       "cfprApMgmtIPv6IfAddrFsmTable": cfprApMgmtIPv6IfAddrFsmTable,
       "cfprApMgmtIPv6IfAddrFsmEntry": cfprApMgmtIPv6IfAddrFsmEntry,
       "cfprApMgmtIPv6IfAddrFsmInstanceId": cfprApMgmtIPv6IfAddrFsmInstanceId,
       "cfprApMgmtIPv6IfAddrFsmDn": cfprApMgmtIPv6IfAddrFsmDn,
       "cfprApMgmtIPv6IfAddrFsmRn": cfprApMgmtIPv6IfAddrFsmRn,
       "cfprApMgmtIPv6IfAddrFsmCompletionTime": cfprApMgmtIPv6IfAddrFsmCompletionTime,
       "cfprApMgmtIPv6IfAddrFsmCurrentFsm": cfprApMgmtIPv6IfAddrFsmCurrentFsm,
       "cfprApMgmtIPv6IfAddrFsmDescrData": cfprApMgmtIPv6IfAddrFsmDescrData,
       "cfprApMgmtIPv6IfAddrFsmFsmStatus": cfprApMgmtIPv6IfAddrFsmFsmStatus,
       "cfprApMgmtIPv6IfAddrFsmProgress": cfprApMgmtIPv6IfAddrFsmProgress,
       "cfprApMgmtIPv6IfAddrFsmRmtErrCode": cfprApMgmtIPv6IfAddrFsmRmtErrCode,
       "cfprApMgmtIPv6IfAddrFsmRmtErrDescr": cfprApMgmtIPv6IfAddrFsmRmtErrDescr,
       "cfprApMgmtIPv6IfAddrFsmRmtRslt": cfprApMgmtIPv6IfAddrFsmRmtRslt,
       "cfprApMgmtIPv6IfAddrFsmStageTable": cfprApMgmtIPv6IfAddrFsmStageTable,
       "cfprApMgmtIPv6IfAddrFsmStageEntry": cfprApMgmtIPv6IfAddrFsmStageEntry,
       "cfprApMgmtIPv6IfAddrFsmStageInstanceId": cfprApMgmtIPv6IfAddrFsmStageInstanceId,
       "cfprApMgmtIPv6IfAddrFsmStageDn": cfprApMgmtIPv6IfAddrFsmStageDn,
       "cfprApMgmtIPv6IfAddrFsmStageRn": cfprApMgmtIPv6IfAddrFsmStageRn,
       "cfprApMgmtIPv6IfAddrFsmStageDescrData": cfprApMgmtIPv6IfAddrFsmStageDescrData,
       "cfprApMgmtIPv6IfAddrFsmStageLastUpdateTime": cfprApMgmtIPv6IfAddrFsmStageLastUpdateTime,
       "cfprApMgmtIPv6IfAddrFsmStageName": cfprApMgmtIPv6IfAddrFsmStageName,
       "cfprApMgmtIPv6IfAddrFsmStageOrder": cfprApMgmtIPv6IfAddrFsmStageOrder,
       "cfprApMgmtIPv6IfAddrFsmStageRetry": cfprApMgmtIPv6IfAddrFsmStageRetry,
       "cfprApMgmtIPv6IfAddrFsmStageStageStatus": cfprApMgmtIPv6IfAddrFsmStageStageStatus,
       "cfprApMgmtIPv6IfAddrFsmTaskTable": cfprApMgmtIPv6IfAddrFsmTaskTable,
       "cfprApMgmtIPv6IfAddrFsmTaskEntry": cfprApMgmtIPv6IfAddrFsmTaskEntry,
       "cfprApMgmtIPv6IfAddrFsmTaskInstanceId": cfprApMgmtIPv6IfAddrFsmTaskInstanceId,
       "cfprApMgmtIPv6IfAddrFsmTaskDn": cfprApMgmtIPv6IfAddrFsmTaskDn,
       "cfprApMgmtIPv6IfAddrFsmTaskRn": cfprApMgmtIPv6IfAddrFsmTaskRn,
       "cfprApMgmtIPv6IfAddrFsmTaskCompletion": cfprApMgmtIPv6IfAddrFsmTaskCompletion,
       "cfprApMgmtIPv6IfAddrFsmTaskFlags": cfprApMgmtIPv6IfAddrFsmTaskFlags,
       "cfprApMgmtIPv6IfAddrFsmTaskItem": cfprApMgmtIPv6IfAddrFsmTaskItem,
       "cfprApMgmtIPv6IfAddrFsmTaskSeqId": cfprApMgmtIPv6IfAddrFsmTaskSeqId,
       "cfprApMgmtIPv6IfConfigTable": cfprApMgmtIPv6IfConfigTable,
       "cfprApMgmtIPv6IfConfigEntry": cfprApMgmtIPv6IfConfigEntry,
       "cfprApMgmtIPv6IfConfigInstanceId": cfprApMgmtIPv6IfConfigInstanceId,
       "cfprApMgmtIPv6IfConfigDn": cfprApMgmtIPv6IfConfigDn,
       "cfprApMgmtIPv6IfConfigRn": cfprApMgmtIPv6IfConfigRn,
       "cfprApMgmtIfTable": cfprApMgmtIfTable,
       "cfprApMgmtIfEntry": cfprApMgmtIfEntry,
       "cfprApMgmtIfInstanceId": cfprApMgmtIfInstanceId,
       "cfprApMgmtIfDn": cfprApMgmtIfDn,
       "cfprApMgmtIfRn": cfprApMgmtIfRn,
       "cfprApMgmtIfAccess": cfprApMgmtIfAccess,
       "cfprApMgmtIfAdminState": cfprApMgmtIfAdminState,
       "cfprApMgmtIfAggrPortId": cfprApMgmtIfAggrPortId,
       "cfprApMgmtIfChassisId": cfprApMgmtIfChassisId,
       "cfprApMgmtIfDiscovery": cfprApMgmtIfDiscovery,
       "cfprApMgmtIfEpDn": cfprApMgmtIfEpDn,
       "cfprApMgmtIfExtBroadcast": cfprApMgmtIfExtBroadcast,
       "cfprApMgmtIfExtGw": cfprApMgmtIfExtGw,
       "cfprApMgmtIfExtIp": cfprApMgmtIfExtIp,
       "cfprApMgmtIfExtMask": cfprApMgmtIfExtMask,
       "cfprApMgmtIfFsmDescr": cfprApMgmtIfFsmDescr,
       "cfprApMgmtIfFsmPrev": cfprApMgmtIfFsmPrev,
       "cfprApMgmtIfFsmProgr": cfprApMgmtIfFsmProgr,
       "cfprApMgmtIfFsmRmtInvErrCode": cfprApMgmtIfFsmRmtInvErrCode,
       "cfprApMgmtIfFsmRmtInvErrDescr": cfprApMgmtIfFsmRmtInvErrDescr,
       "cfprApMgmtIfFsmRmtInvRslt": cfprApMgmtIfFsmRmtInvRslt,
       "cfprApMgmtIfFsmStageDescr": cfprApMgmtIfFsmStageDescr,
       "cfprApMgmtIfFsmStamp": cfprApMgmtIfFsmStamp,
       "cfprApMgmtIfFsmStatus": cfprApMgmtIfFsmStatus,
       "cfprApMgmtIfFsmTry": cfprApMgmtIfFsmTry,
       "cfprApMgmtIfId": cfprApMgmtIfId,
       "cfprApMgmtIfIfRole": cfprApMgmtIfIfRole,
       "cfprApMgmtIfIfType": cfprApMgmtIfIfType,
       "cfprApMgmtIfIp": cfprApMgmtIfIp,
       "cfprApMgmtIfLocale": cfprApMgmtIfLocale,
       "cfprApMgmtIfMac": cfprApMgmtIfMac,
       "cfprApMgmtIfMask": cfprApMgmtIfMask,
       "cfprApMgmtIfName": cfprApMgmtIfName,
       "cfprApMgmtIfPeerAggrPortId": cfprApMgmtIfPeerAggrPortId,
       "cfprApMgmtIfPeerChassisId": cfprApMgmtIfPeerChassisId,
       "cfprApMgmtIfPeerDn": cfprApMgmtIfPeerDn,
       "cfprApMgmtIfPeerPortId": cfprApMgmtIfPeerPortId,
       "cfprApMgmtIfPeerSlotId": cfprApMgmtIfPeerSlotId,
       "cfprApMgmtIfPortId": cfprApMgmtIfPortId,
       "cfprApMgmtIfSlotId": cfprApMgmtIfSlotId,
       "cfprApMgmtIfStateQual": cfprApMgmtIfStateQual,
       "cfprApMgmtIfSubject": cfprApMgmtIfSubject,
       "cfprApMgmtIfSwitchId": cfprApMgmtIfSwitchId,
       "cfprApMgmtIfTransport": cfprApMgmtIfTransport,
       "cfprApMgmtIfType": cfprApMgmtIfType,
       "cfprApMgmtIfVnet": cfprApMgmtIfVnet,
       "cfprApMgmtIfFsmTable": cfprApMgmtIfFsmTable,
       "cfprApMgmtIfFsmEntry": cfprApMgmtIfFsmEntry,
       "cfprApMgmtIfFsmInstanceId": cfprApMgmtIfFsmInstanceId,
       "cfprApMgmtIfFsmDn": cfprApMgmtIfFsmDn,
       "cfprApMgmtIfFsmRn": cfprApMgmtIfFsmRn,
       "cfprApMgmtIfFsmCompletionTime": cfprApMgmtIfFsmCompletionTime,
       "cfprApMgmtIfFsmCurrentFsm": cfprApMgmtIfFsmCurrentFsm,
       "cfprApMgmtIfFsmDescrData": cfprApMgmtIfFsmDescrData,
       "cfprApMgmtIfFsmFsmStatus": cfprApMgmtIfFsmFsmStatus,
       "cfprApMgmtIfFsmProgress": cfprApMgmtIfFsmProgress,
       "cfprApMgmtIfFsmRmtErrCode": cfprApMgmtIfFsmRmtErrCode,
       "cfprApMgmtIfFsmRmtErrDescr": cfprApMgmtIfFsmRmtErrDescr,
       "cfprApMgmtIfFsmRmtRslt": cfprApMgmtIfFsmRmtRslt,
       "cfprApMgmtIfFsmStageTable": cfprApMgmtIfFsmStageTable,
       "cfprApMgmtIfFsmStageEntry": cfprApMgmtIfFsmStageEntry,
       "cfprApMgmtIfFsmStageInstanceId": cfprApMgmtIfFsmStageInstanceId,
       "cfprApMgmtIfFsmStageDn": cfprApMgmtIfFsmStageDn,
       "cfprApMgmtIfFsmStageRn": cfprApMgmtIfFsmStageRn,
       "cfprApMgmtIfFsmStageDescrData": cfprApMgmtIfFsmStageDescrData,
       "cfprApMgmtIfFsmStageLastUpdateTime": cfprApMgmtIfFsmStageLastUpdateTime,
       "cfprApMgmtIfFsmStageName": cfprApMgmtIfFsmStageName,
       "cfprApMgmtIfFsmStageOrder": cfprApMgmtIfFsmStageOrder,
       "cfprApMgmtIfFsmStageRetry": cfprApMgmtIfFsmStageRetry,
       "cfprApMgmtIfFsmStageStageStatus": cfprApMgmtIfFsmStageStageStatus,
       "cfprApMgmtIfFsmTaskTable": cfprApMgmtIfFsmTaskTable,
       "cfprApMgmtIfFsmTaskEntry": cfprApMgmtIfFsmTaskEntry,
       "cfprApMgmtIfFsmTaskInstanceId": cfprApMgmtIfFsmTaskInstanceId,
       "cfprApMgmtIfFsmTaskDn": cfprApMgmtIfFsmTaskDn,
       "cfprApMgmtIfFsmTaskRn": cfprApMgmtIfFsmTaskRn,
       "cfprApMgmtIfFsmTaskCompletion": cfprApMgmtIfFsmTaskCompletion,
       "cfprApMgmtIfFsmTaskFlags": cfprApMgmtIfFsmTaskFlags,
       "cfprApMgmtIfFsmTaskItem": cfprApMgmtIfFsmTaskItem,
       "cfprApMgmtIfFsmTaskSeqId": cfprApMgmtIfFsmTaskSeqId,
       "cfprApMgmtImportConfigInfoTable": cfprApMgmtImportConfigInfoTable,
       "cfprApMgmtImportConfigInfoEntry": cfprApMgmtImportConfigInfoEntry,
       "cfprApMgmtImportConfigInfoInstanceId": cfprApMgmtImportConfigInfoInstanceId,
       "cfprApMgmtImportConfigInfoDn": cfprApMgmtImportConfigInfoDn,
       "cfprApMgmtImportConfigInfoRn": cfprApMgmtImportConfigInfoRn,
       "cfprApMgmtImportConfigInfoImportDate": cfprApMgmtImportConfigInfoImportDate,
       "cfprApMgmtImporterTable": cfprApMgmtImporterTable,
       "cfprApMgmtImporterEntry": cfprApMgmtImporterEntry,
       "cfprApMgmtImporterInstanceId": cfprApMgmtImporterInstanceId,
       "cfprApMgmtImporterDn": cfprApMgmtImporterDn,
       "cfprApMgmtImporterRn": cfprApMgmtImporterRn,
       "cfprApMgmtImporterAction": cfprApMgmtImporterAction,
       "cfprApMgmtImporterAdminState": cfprApMgmtImporterAdminState,
       "cfprApMgmtImporterApplyingBreakoutCfg": cfprApMgmtImporterApplyingBreakoutCfg,
       "cfprApMgmtImporterDescr": cfprApMgmtImporterDescr,
       "cfprApMgmtImporterFsmDescr": cfprApMgmtImporterFsmDescr,
       "cfprApMgmtImporterFsmPrev": cfprApMgmtImporterFsmPrev,
       "cfprApMgmtImporterFsmProgr": cfprApMgmtImporterFsmProgr,
       "cfprApMgmtImporterFsmRmtInvErrCode": cfprApMgmtImporterFsmRmtInvErrCode,
       "cfprApMgmtImporterFsmRmtInvErrDescr": cfprApMgmtImporterFsmRmtInvErrDescr,
       "cfprApMgmtImporterFsmRmtInvRslt": cfprApMgmtImporterFsmRmtInvRslt,
       "cfprApMgmtImporterFsmStageDescr": cfprApMgmtImporterFsmStageDescr,
       "cfprApMgmtImporterFsmStamp": cfprApMgmtImporterFsmStamp,
       "cfprApMgmtImporterFsmStatus": cfprApMgmtImporterFsmStatus,
       "cfprApMgmtImporterFsmTry": cfprApMgmtImporterFsmTry,
       "cfprApMgmtImporterHostname": cfprApMgmtImporterHostname,
       "cfprApMgmtImporterIntId": cfprApMgmtImporterIntId,
       "cfprApMgmtImporterName": cfprApMgmtImporterName,
       "cfprApMgmtImporterOperStatus": cfprApMgmtImporterOperStatus,
       "cfprApMgmtImporterPolicyLevel": cfprApMgmtImporterPolicyLevel,
       "cfprApMgmtImporterPolicyOwner": cfprApMgmtImporterPolicyOwner,
       "cfprApMgmtImporterPort": cfprApMgmtImporterPort,
       "cfprApMgmtImporterPostAction": cfprApMgmtImporterPostAction,
       "cfprApMgmtImporterProto": cfprApMgmtImporterProto,
       "cfprApMgmtImporterPwd": cfprApMgmtImporterPwd,
       "cfprApMgmtImporterRemoteFile": cfprApMgmtImporterRemoteFile,
       "cfprApMgmtImporterUser": cfprApMgmtImporterUser,
       "cfprApMgmtImporterFsmTable": cfprApMgmtImporterFsmTable,
       "cfprApMgmtImporterFsmEntry": cfprApMgmtImporterFsmEntry,
       "cfprApMgmtImporterFsmInstanceId": cfprApMgmtImporterFsmInstanceId,
       "cfprApMgmtImporterFsmDn": cfprApMgmtImporterFsmDn,
       "cfprApMgmtImporterFsmRn": cfprApMgmtImporterFsmRn,
       "cfprApMgmtImporterFsmCompletionTime": cfprApMgmtImporterFsmCompletionTime,
       "cfprApMgmtImporterFsmCurrentFsm": cfprApMgmtImporterFsmCurrentFsm,
       "cfprApMgmtImporterFsmDescrData": cfprApMgmtImporterFsmDescrData,
       "cfprApMgmtImporterFsmFsmStatus": cfprApMgmtImporterFsmFsmStatus,
       "cfprApMgmtImporterFsmProgress": cfprApMgmtImporterFsmProgress,
       "cfprApMgmtImporterFsmRmtErrCode": cfprApMgmtImporterFsmRmtErrCode,
       "cfprApMgmtImporterFsmRmtErrDescr": cfprApMgmtImporterFsmRmtErrDescr,
       "cfprApMgmtImporterFsmRmtRslt": cfprApMgmtImporterFsmRmtRslt,
       "cfprApMgmtImporterFsmStageTable": cfprApMgmtImporterFsmStageTable,
       "cfprApMgmtImporterFsmStageEntry": cfprApMgmtImporterFsmStageEntry,
       "cfprApMgmtImporterFsmStageInstanceId": cfprApMgmtImporterFsmStageInstanceId,
       "cfprApMgmtImporterFsmStageDn": cfprApMgmtImporterFsmStageDn,
       "cfprApMgmtImporterFsmStageRn": cfprApMgmtImporterFsmStageRn,
       "cfprApMgmtImporterFsmStageDescrData": cfprApMgmtImporterFsmStageDescrData,
       "cfprApMgmtImporterFsmStageLastUpdateTime": cfprApMgmtImporterFsmStageLastUpdateTime,
       "cfprApMgmtImporterFsmStageName": cfprApMgmtImporterFsmStageName,
       "cfprApMgmtImporterFsmStageOrder": cfprApMgmtImporterFsmStageOrder,
       "cfprApMgmtImporterFsmStageRetry": cfprApMgmtImporterFsmStageRetry,
       "cfprApMgmtImporterFsmStageStageStatus": cfprApMgmtImporterFsmStageStageStatus,
       "cfprApMgmtImporterFsmTaskTable": cfprApMgmtImporterFsmTaskTable,
       "cfprApMgmtImporterFsmTaskEntry": cfprApMgmtImporterFsmTaskEntry,
       "cfprApMgmtImporterFsmTaskInstanceId": cfprApMgmtImporterFsmTaskInstanceId,
       "cfprApMgmtImporterFsmTaskDn": cfprApMgmtImporterFsmTaskDn,
       "cfprApMgmtImporterFsmTaskRn": cfprApMgmtImporterFsmTaskRn,
       "cfprApMgmtImporterFsmTaskCompletion": cfprApMgmtImporterFsmTaskCompletion,
       "cfprApMgmtImporterFsmTaskFlags": cfprApMgmtImporterFsmTaskFlags,
       "cfprApMgmtImporterFsmTaskItem": cfprApMgmtImporterFsmTaskItem,
       "cfprApMgmtImporterFsmTaskSeqId": cfprApMgmtImporterFsmTaskSeqId,
       "cfprApMgmtInbandProfileTable": cfprApMgmtInbandProfileTable,
       "cfprApMgmtInbandProfileEntry": cfprApMgmtInbandProfileEntry,
       "cfprApMgmtInbandProfileInstanceId": cfprApMgmtInbandProfileInstanceId,
       "cfprApMgmtInbandProfileDn": cfprApMgmtInbandProfileDn,
       "cfprApMgmtInbandProfileRn": cfprApMgmtInbandProfileRn,
       "cfprApMgmtInbandProfileDefaultVlanName": cfprApMgmtInbandProfileDefaultVlanName,
       "cfprApMgmtInbandProfileName": cfprApMgmtInbandProfileName,
       "cfprApMgmtInbandProfilePoolName": cfprApMgmtInbandProfilePoolName,
       "cfprApMgmtIntAuthPolicyTable": cfprApMgmtIntAuthPolicyTable,
       "cfprApMgmtIntAuthPolicyEntry": cfprApMgmtIntAuthPolicyEntry,
       "cfprApMgmtIntAuthPolicyInstanceId": cfprApMgmtIntAuthPolicyInstanceId,
       "cfprApMgmtIntAuthPolicyDn": cfprApMgmtIntAuthPolicyDn,
       "cfprApMgmtIntAuthPolicyRn": cfprApMgmtIntAuthPolicyRn,
       "cfprApMgmtIntAuthPolicyMethod": cfprApMgmtIntAuthPolicyMethod,
       "cfprApMgmtIntAuthPolicyName": cfprApMgmtIntAuthPolicyName,
       "cfprApMgmtIntAuthPolicyPwd": cfprApMgmtIntAuthPolicyPwd,
       "cfprApMgmtInterfaceTable": cfprApMgmtInterfaceTable,
       "cfprApMgmtInterfaceEntry": cfprApMgmtInterfaceEntry,
       "cfprApMgmtInterfaceInstanceId": cfprApMgmtInterfaceInstanceId,
       "cfprApMgmtInterfaceDn": cfprApMgmtInterfaceDn,
       "cfprApMgmtInterfaceRn": cfprApMgmtInterfaceRn,
       "cfprApMgmtInterfaceConfigMessage": cfprApMgmtInterfaceConfigMessage,
       "cfprApMgmtInterfaceConfigState": cfprApMgmtInterfaceConfigState,
       "cfprApMgmtInterfaceIpV4State": cfprApMgmtInterfaceIpV4State,
       "cfprApMgmtInterfaceIpV6State": cfprApMgmtInterfaceIpV6State,
       "cfprApMgmtInterfaceIsDefaultDerived": cfprApMgmtInterfaceIsDefaultDerived,
       "cfprApMgmtInterfaceMode": cfprApMgmtInterfaceMode,
       "cfprApMgmtInterfaceOperState": cfprApMgmtInterfaceOperState,
       "cfprApMgmtPmonEntryTable": cfprApMgmtPmonEntryTable,
       "cfprApMgmtPmonEntryEntry": cfprApMgmtPmonEntryEntry,
       "cfprApMgmtPmonEntryInstanceId": cfprApMgmtPmonEntryInstanceId,
       "cfprApMgmtPmonEntryDn": cfprApMgmtPmonEntryDn,
       "cfprApMgmtPmonEntryRn": cfprApMgmtPmonEntryRn,
       "cfprApMgmtPmonEntryExitSignal": cfprApMgmtPmonEntryExitSignal,
       "cfprApMgmtPmonEntryFullPathname": cfprApMgmtPmonEntryFullPathname,
       "cfprApMgmtPmonEntryHeapSize": cfprApMgmtPmonEntryHeapSize,
       "cfprApMgmtPmonEntryHeapSize16Gb": cfprApMgmtPmonEntryHeapSize16Gb,
       "cfprApMgmtPmonEntryLastExitCode": cfprApMgmtPmonEntryLastExitCode,
       "cfprApMgmtPmonEntryMaxRetries": cfprApMgmtPmonEntryMaxRetries,
       "cfprApMgmtPmonEntryName": cfprApMgmtPmonEntryName,
       "cfprApMgmtPmonEntryRetries": cfprApMgmtPmonEntryRetries,
       "cfprApMgmtPmonEntrySpuriousRetries": cfprApMgmtPmonEntrySpuriousRetries,
       "cfprApMgmtPmonEntryState": cfprApMgmtPmonEntryState,
       "cfprApMgmtPmonEntrySwitchId": cfprApMgmtPmonEntrySwitchId,
       "cfprApMgmtPmonEntryWorkingDirectory": cfprApMgmtPmonEntryWorkingDirectory,
       "cfprApMgmtProfDerivedInterfaceTable": cfprApMgmtProfDerivedInterfaceTable,
       "cfprApMgmtProfDerivedInterfaceEntry": cfprApMgmtProfDerivedInterfaceEntry,
       "cfprApMgmtProfDerivedInterfaceInstanceId": cfprApMgmtProfDerivedInterfaceInstanceId,
       "cfprApMgmtProfDerivedInterfaceDn": cfprApMgmtProfDerivedInterfaceDn,
       "cfprApMgmtProfDerivedInterfaceRn": cfprApMgmtProfDerivedInterfaceRn,
       "cfprApMgmtProfDerivedInterfaceConfigMessage": cfprApMgmtProfDerivedInterfaceConfigMessage,
       "cfprApMgmtProfDerivedInterfaceConfigState": cfprApMgmtProfDerivedInterfaceConfigState,
       "cfprApMgmtProfDerivedInterfaceIpV4State": cfprApMgmtProfDerivedInterfaceIpV4State,
       "cfprApMgmtProfDerivedInterfaceIpV6State": cfprApMgmtProfDerivedInterfaceIpV6State,
       "cfprApMgmtProfDerivedInterfaceMode": cfprApMgmtProfDerivedInterfaceMode,
       "cfprApMgmtProfDerivedInterfaceOperState": cfprApMgmtProfDerivedInterfaceOperState,
       "cfprApMgmtVnetTable": cfprApMgmtVnetTable,
       "cfprApMgmtVnetEntry": cfprApMgmtVnetEntry,
       "cfprApMgmtVnetInstanceId": cfprApMgmtVnetInstanceId,
       "cfprApMgmtVnetDn": cfprApMgmtVnetDn,
       "cfprApMgmtVnetRn": cfprApMgmtVnetRn,
       "cfprApMgmtVnetConfigState": cfprApMgmtVnetConfigState,
       "cfprApMgmtVnetId": cfprApMgmtVnetId,
       "cfprApMgmtVnetName": cfprApMgmtVnetName}
)
