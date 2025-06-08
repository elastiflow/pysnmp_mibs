# SNMP MIB module (CISCO-FIREPOWER-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-MGMT-MIB.mib
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

(CfprCommClientAdminState,
 CfprConditionRemoteInvRslt,
 CfprEtherSatelliteConnectionDisc,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprIpProtocol,
 CfprMgmtAccess,
 CfprMgmtAdminState,
 CfprMgmtBackupFsmCurrentFsm,
 CfprMgmtBackupFsmStageName,
 CfprMgmtBackupFsmTaskItem,
 CfprMgmtBackupInterval,
 CfprMgmtBackupIssue,
 CfprMgmtBackupJob,
 CfprMgmtBackupPolicyFsmCurrentFsm,
 CfprMgmtBackupPolicyFsmStageName,
 CfprMgmtBackupPostAction,
 CfprMgmtBackupProto,
 CfprMgmtBackupStatus,
 CfprMgmtBackupType,
 CfprMgmtCfgExportPolicyFsmCurrentFsm,
 CfprMgmtCfgExportPolicyFsmStageName,
 CfprMgmtCimcSecureBootAdminState,
 CfprMgmtConfigState,
 CfprMgmtConnectionState,
 CfprMgmtControllerFsmCurrentFsm,
 CfprMgmtControllerFsmStageName,
 CfprMgmtControllerFsmTaskFlags,
 CfprMgmtControllerFsmTaskItem,
 CfprMgmtDimmBlacklistingOperState,
 CfprMgmtEntityChassisDeviceIoState1,
 CfprMgmtEntityChassisDeviceIoState2,
 CfprMgmtEntityChassisDeviceIoState3,
 CfprMgmtEntityHaFailureReason,
 CfprMgmtEntityHaReadiness,
 CfprMgmtEntityLeadership,
 CfprMgmtEntityMgmtServicesState,
 CfprMgmtEntityProblems,
 CfprMgmtEntityState,
 CfprMgmtEntityUmbilicalState,
 CfprMgmtExportPolicyAdminState,
 CfprMgmtExportPolicyFsmCurrentFsm,
 CfprMgmtExportPolicyFsmStageName,
 CfprMgmtExportPolicyFsmTaskItem,
 CfprMgmtExportPolicyProto,
 CfprMgmtIPv6AutoAddrFormat,
 CfprMgmtIPv6Format,
 CfprMgmtIPv6IfAddrFsmCurrentFsm,
 CfprMgmtIPv6IfAddrFsmStageName,
 CfprMgmtIPv6IfAddrFsmTaskItem,
 CfprMgmtIfFsmCurrentFsm,
 CfprMgmtIfFsmStageName,
 CfprMgmtIfFsmTaskItem,
 CfprMgmtImportAction,
 CfprMgmtImportStatus,
 CfprMgmtImporterFsmCurrentFsm,
 CfprMgmtImporterFsmStageName,
 CfprMgmtImporterFsmTaskItem,
 CfprMgmtImporterPostAction,
 CfprMgmtImporterProto,
 CfprMgmtIntAuthPolicyMethod,
 CfprMgmtIpv6AdminState,
 CfprMgmtMode,
 CfprMgmtOperState,
 CfprMgmtPmonEntryState,
 CfprMgmtSecureBootOperState,
 CfprMgmtSource,
 CfprMgmtStateQual,
 CfprMgmtStorageSubsystemState,
 CfprMgmtSubject,
 CfprNetworkConnectionType,
 CfprNetworkLocale,
 CfprNetworkPhysEpIfType,
 CfprNetworkPortRole,
 CfprNetworkSwitchId,
 CfprNetworkTransport,
 CfprPolicyPolicyOwner,
 CfprTrigAdminState,
 CfprTrigTrigOperState,
 CfprVnicExternalMgmtIPMode) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprCommClientAdminState",
    "CfprConditionRemoteInvRslt",
    "CfprEtherSatelliteConnectionDisc",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprIpProtocol",
    "CfprMgmtAccess",
    "CfprMgmtAdminState",
    "CfprMgmtBackupFsmCurrentFsm",
    "CfprMgmtBackupFsmStageName",
    "CfprMgmtBackupFsmTaskItem",
    "CfprMgmtBackupInterval",
    "CfprMgmtBackupIssue",
    "CfprMgmtBackupJob",
    "CfprMgmtBackupPolicyFsmCurrentFsm",
    "CfprMgmtBackupPolicyFsmStageName",
    "CfprMgmtBackupPostAction",
    "CfprMgmtBackupProto",
    "CfprMgmtBackupStatus",
    "CfprMgmtBackupType",
    "CfprMgmtCfgExportPolicyFsmCurrentFsm",
    "CfprMgmtCfgExportPolicyFsmStageName",
    "CfprMgmtCimcSecureBootAdminState",
    "CfprMgmtConfigState",
    "CfprMgmtConnectionState",
    "CfprMgmtControllerFsmCurrentFsm",
    "CfprMgmtControllerFsmStageName",
    "CfprMgmtControllerFsmTaskFlags",
    "CfprMgmtControllerFsmTaskItem",
    "CfprMgmtDimmBlacklistingOperState",
    "CfprMgmtEntityChassisDeviceIoState1",
    "CfprMgmtEntityChassisDeviceIoState2",
    "CfprMgmtEntityChassisDeviceIoState3",
    "CfprMgmtEntityHaFailureReason",
    "CfprMgmtEntityHaReadiness",
    "CfprMgmtEntityLeadership",
    "CfprMgmtEntityMgmtServicesState",
    "CfprMgmtEntityProblems",
    "CfprMgmtEntityState",
    "CfprMgmtEntityUmbilicalState",
    "CfprMgmtExportPolicyAdminState",
    "CfprMgmtExportPolicyFsmCurrentFsm",
    "CfprMgmtExportPolicyFsmStageName",
    "CfprMgmtExportPolicyFsmTaskItem",
    "CfprMgmtExportPolicyProto",
    "CfprMgmtIPv6AutoAddrFormat",
    "CfprMgmtIPv6Format",
    "CfprMgmtIPv6IfAddrFsmCurrentFsm",
    "CfprMgmtIPv6IfAddrFsmStageName",
    "CfprMgmtIPv6IfAddrFsmTaskItem",
    "CfprMgmtIfFsmCurrentFsm",
    "CfprMgmtIfFsmStageName",
    "CfprMgmtIfFsmTaskItem",
    "CfprMgmtImportAction",
    "CfprMgmtImportStatus",
    "CfprMgmtImporterFsmCurrentFsm",
    "CfprMgmtImporterFsmStageName",
    "CfprMgmtImporterFsmTaskItem",
    "CfprMgmtImporterPostAction",
    "CfprMgmtImporterProto",
    "CfprMgmtIntAuthPolicyMethod",
    "CfprMgmtIpv6AdminState",
    "CfprMgmtMode",
    "CfprMgmtOperState",
    "CfprMgmtPmonEntryState",
    "CfprMgmtSecureBootOperState",
    "CfprMgmtSource",
    "CfprMgmtStateQual",
    "CfprMgmtStorageSubsystemState",
    "CfprMgmtSubject",
    "CfprNetworkConnectionType",
    "CfprNetworkLocale",
    "CfprNetworkPhysEpIfType",
    "CfprNetworkPortRole",
    "CfprNetworkSwitchId",
    "CfprNetworkTransport",
    "CfprPolicyPolicyOwner",
    "CfprTrigAdminState",
    "CfprTrigTrigOperState",
    "CfprVnicExternalMgmtIPMode")

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

cfprMgmtObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprMgmtAccessPolicyTable_Object = MibTable
cfprMgmtAccessPolicyTable = _CfprMgmtAccessPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 1)
)
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyTable.setStatus("current")
_CfprMgmtAccessPolicyEntry_Object = MibTableRow
cfprMgmtAccessPolicyEntry = _CfprMgmtAccessPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 1, 1)
)
cfprMgmtAccessPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtAccessPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyEntry.setStatus("current")
_CfprMgmtAccessPolicyInstanceId_Type = CfprManagedObjectId
_CfprMgmtAccessPolicyInstanceId_Object = MibTableColumn
cfprMgmtAccessPolicyInstanceId = _CfprMgmtAccessPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 1, 1, 1),
    _CfprMgmtAccessPolicyInstanceId_Type()
)
cfprMgmtAccessPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyInstanceId.setStatus("current")
_CfprMgmtAccessPolicyDn_Type = CfprManagedObjectDn
_CfprMgmtAccessPolicyDn_Object = MibTableColumn
cfprMgmtAccessPolicyDn = _CfprMgmtAccessPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 1, 1, 2),
    _CfprMgmtAccessPolicyDn_Type()
)
cfprMgmtAccessPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyDn.setStatus("current")
_CfprMgmtAccessPolicyRn_Type = SnmpAdminString
_CfprMgmtAccessPolicyRn_Object = MibTableColumn
cfprMgmtAccessPolicyRn = _CfprMgmtAccessPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 1, 1, 3),
    _CfprMgmtAccessPolicyRn_Type()
)
cfprMgmtAccessPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyRn.setStatus("current")
_CfprMgmtAccessPolicyItemTable_Object = MibTable
cfprMgmtAccessPolicyItemTable = _CfprMgmtAccessPolicyItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 2)
)
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyItemTable.setStatus("current")
_CfprMgmtAccessPolicyItemEntry_Object = MibTableRow
cfprMgmtAccessPolicyItemEntry = _CfprMgmtAccessPolicyItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 2, 1)
)
cfprMgmtAccessPolicyItemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtAccessPolicyItemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyItemEntry.setStatus("current")
_CfprMgmtAccessPolicyItemInstanceId_Type = CfprManagedObjectId
_CfprMgmtAccessPolicyItemInstanceId_Object = MibTableColumn
cfprMgmtAccessPolicyItemInstanceId = _CfprMgmtAccessPolicyItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 2, 1, 1),
    _CfprMgmtAccessPolicyItemInstanceId_Type()
)
cfprMgmtAccessPolicyItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyItemInstanceId.setStatus("current")
_CfprMgmtAccessPolicyItemDn_Type = CfprManagedObjectDn
_CfprMgmtAccessPolicyItemDn_Object = MibTableColumn
cfprMgmtAccessPolicyItemDn = _CfprMgmtAccessPolicyItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 2, 1, 2),
    _CfprMgmtAccessPolicyItemDn_Type()
)
cfprMgmtAccessPolicyItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyItemDn.setStatus("current")
_CfprMgmtAccessPolicyItemRn_Type = SnmpAdminString
_CfprMgmtAccessPolicyItemRn_Object = MibTableColumn
cfprMgmtAccessPolicyItemRn = _CfprMgmtAccessPolicyItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 2, 1, 3),
    _CfprMgmtAccessPolicyItemRn_Type()
)
cfprMgmtAccessPolicyItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyItemRn.setStatus("current")
_CfprMgmtAccessPolicyItemDescr_Type = SnmpAdminString
_CfprMgmtAccessPolicyItemDescr_Object = MibTableColumn
cfprMgmtAccessPolicyItemDescr = _CfprMgmtAccessPolicyItemDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 2, 1, 4),
    _CfprMgmtAccessPolicyItemDescr_Type()
)
cfprMgmtAccessPolicyItemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyItemDescr.setStatus("current")
_CfprMgmtAccessPolicyItemIntId_Type = SnmpAdminString
_CfprMgmtAccessPolicyItemIntId_Object = MibTableColumn
cfprMgmtAccessPolicyItemIntId = _CfprMgmtAccessPolicyItemIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 2, 1, 5),
    _CfprMgmtAccessPolicyItemIntId_Type()
)
cfprMgmtAccessPolicyItemIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyItemIntId.setStatus("current")
_CfprMgmtAccessPolicyItemIpPoolName_Type = SnmpAdminString
_CfprMgmtAccessPolicyItemIpPoolName_Object = MibTableColumn
cfprMgmtAccessPolicyItemIpPoolName = _CfprMgmtAccessPolicyItemIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 2, 1, 6),
    _CfprMgmtAccessPolicyItemIpPoolName_Type()
)
cfprMgmtAccessPolicyItemIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyItemIpPoolName.setStatus("current")
_CfprMgmtAccessPolicyItemName_Type = SnmpAdminString
_CfprMgmtAccessPolicyItemName_Object = MibTableColumn
cfprMgmtAccessPolicyItemName = _CfprMgmtAccessPolicyItemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 2, 1, 7),
    _CfprMgmtAccessPolicyItemName_Type()
)
cfprMgmtAccessPolicyItemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyItemName.setStatus("current")
_CfprMgmtAccessPolicyItemPolicyLevel_Type = Gauge32
_CfprMgmtAccessPolicyItemPolicyLevel_Object = MibTableColumn
cfprMgmtAccessPolicyItemPolicyLevel = _CfprMgmtAccessPolicyItemPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 2, 1, 8),
    _CfprMgmtAccessPolicyItemPolicyLevel_Type()
)
cfprMgmtAccessPolicyItemPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyItemPolicyLevel.setStatus("current")
_CfprMgmtAccessPolicyItemPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprMgmtAccessPolicyItemPolicyOwner_Object = MibTableColumn
cfprMgmtAccessPolicyItemPolicyOwner = _CfprMgmtAccessPolicyItemPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 2, 1, 9),
    _CfprMgmtAccessPolicyItemPolicyOwner_Type()
)
cfprMgmtAccessPolicyItemPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyItemPolicyOwner.setStatus("current")
_CfprMgmtAccessPolicyItemSubject_Type = CfprMgmtSubject
_CfprMgmtAccessPolicyItemSubject_Object = MibTableColumn
cfprMgmtAccessPolicyItemSubject = _CfprMgmtAccessPolicyItemSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 2, 1, 10),
    _CfprMgmtAccessPolicyItemSubject_Type()
)
cfprMgmtAccessPolicyItemSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPolicyItemSubject.setStatus("current")
_CfprMgmtAccessPortTable_Object = MibTable
cfprMgmtAccessPortTable = _CfprMgmtAccessPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 3)
)
if mibBuilder.loadTexts:
    cfprMgmtAccessPortTable.setStatus("current")
_CfprMgmtAccessPortEntry_Object = MibTableRow
cfprMgmtAccessPortEntry = _CfprMgmtAccessPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 3, 1)
)
cfprMgmtAccessPortEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtAccessPortInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtAccessPortEntry.setStatus("current")
_CfprMgmtAccessPortInstanceId_Type = CfprManagedObjectId
_CfprMgmtAccessPortInstanceId_Object = MibTableColumn
cfprMgmtAccessPortInstanceId = _CfprMgmtAccessPortInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 3, 1, 1),
    _CfprMgmtAccessPortInstanceId_Type()
)
cfprMgmtAccessPortInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtAccessPortInstanceId.setStatus("current")
_CfprMgmtAccessPortDn_Type = CfprManagedObjectDn
_CfprMgmtAccessPortDn_Object = MibTableColumn
cfprMgmtAccessPortDn = _CfprMgmtAccessPortDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 3, 1, 2),
    _CfprMgmtAccessPortDn_Type()
)
cfprMgmtAccessPortDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPortDn.setStatus("current")
_CfprMgmtAccessPortRn_Type = SnmpAdminString
_CfprMgmtAccessPortRn_Object = MibTableColumn
cfprMgmtAccessPortRn = _CfprMgmtAccessPortRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 3, 1, 3),
    _CfprMgmtAccessPortRn_Type()
)
cfprMgmtAccessPortRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPortRn.setStatus("current")
_CfprMgmtAccessPortPort_Type = Gauge32
_CfprMgmtAccessPortPort_Object = MibTableColumn
cfprMgmtAccessPortPort = _CfprMgmtAccessPortPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 3, 1, 4),
    _CfprMgmtAccessPortPort_Type()
)
cfprMgmtAccessPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPortPort.setStatus("current")
_CfprMgmtAccessPortProtocol_Type = CfprIpProtocol
_CfprMgmtAccessPortProtocol_Object = MibTableColumn
cfprMgmtAccessPortProtocol = _CfprMgmtAccessPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 3, 1, 5),
    _CfprMgmtAccessPortProtocol_Type()
)
cfprMgmtAccessPortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtAccessPortProtocol.setStatus("current")
_CfprMgmtBackupTable_Object = MibTable
cfprMgmtBackupTable = _CfprMgmtBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4)
)
if mibBuilder.loadTexts:
    cfprMgmtBackupTable.setStatus("current")
_CfprMgmtBackupEntry_Object = MibTableRow
cfprMgmtBackupEntry = _CfprMgmtBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1)
)
cfprMgmtBackupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtBackupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtBackupEntry.setStatus("current")
_CfprMgmtBackupInstanceId_Type = CfprManagedObjectId
_CfprMgmtBackupInstanceId_Object = MibTableColumn
cfprMgmtBackupInstanceId = _CfprMgmtBackupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 1),
    _CfprMgmtBackupInstanceId_Type()
)
cfprMgmtBackupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtBackupInstanceId.setStatus("current")
_CfprMgmtBackupDn_Type = CfprManagedObjectDn
_CfprMgmtBackupDn_Object = MibTableColumn
cfprMgmtBackupDn = _CfprMgmtBackupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 2),
    _CfprMgmtBackupDn_Type()
)
cfprMgmtBackupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupDn.setStatus("current")
_CfprMgmtBackupRn_Type = SnmpAdminString
_CfprMgmtBackupRn_Object = MibTableColumn
cfprMgmtBackupRn = _CfprMgmtBackupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 3),
    _CfprMgmtBackupRn_Type()
)
cfprMgmtBackupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupRn.setStatus("current")
_CfprMgmtBackupAdminState_Type = CfprCommClientAdminState
_CfprMgmtBackupAdminState_Object = MibTableColumn
cfprMgmtBackupAdminState = _CfprMgmtBackupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 4),
    _CfprMgmtBackupAdminState_Type()
)
cfprMgmtBackupAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupAdminState.setStatus("current")
_CfprMgmtBackupDescr_Type = SnmpAdminString
_CfprMgmtBackupDescr_Object = MibTableColumn
cfprMgmtBackupDescr = _CfprMgmtBackupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 5),
    _CfprMgmtBackupDescr_Type()
)
cfprMgmtBackupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupDescr.setStatus("current")
_CfprMgmtBackupFsmDescr_Type = SnmpAdminString
_CfprMgmtBackupFsmDescr_Object = MibTableColumn
cfprMgmtBackupFsmDescr = _CfprMgmtBackupFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 6),
    _CfprMgmtBackupFsmDescr_Type()
)
cfprMgmtBackupFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmDescr.setStatus("current")
_CfprMgmtBackupFsmPrev_Type = SnmpAdminString
_CfprMgmtBackupFsmPrev_Object = MibTableColumn
cfprMgmtBackupFsmPrev = _CfprMgmtBackupFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 7),
    _CfprMgmtBackupFsmPrev_Type()
)
cfprMgmtBackupFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmPrev.setStatus("current")
_CfprMgmtBackupFsmProgr_Type = Gauge32
_CfprMgmtBackupFsmProgr_Object = MibTableColumn
cfprMgmtBackupFsmProgr = _CfprMgmtBackupFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 8),
    _CfprMgmtBackupFsmProgr_Type()
)
cfprMgmtBackupFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmProgr.setStatus("current")
_CfprMgmtBackupFsmRmtInvErrCode_Type = Gauge32
_CfprMgmtBackupFsmRmtInvErrCode_Object = MibTableColumn
cfprMgmtBackupFsmRmtInvErrCode = _CfprMgmtBackupFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 9),
    _CfprMgmtBackupFsmRmtInvErrCode_Type()
)
cfprMgmtBackupFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmRmtInvErrCode.setStatus("current")
_CfprMgmtBackupFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprMgmtBackupFsmRmtInvErrDescr_Object = MibTableColumn
cfprMgmtBackupFsmRmtInvErrDescr = _CfprMgmtBackupFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 10),
    _CfprMgmtBackupFsmRmtInvErrDescr_Type()
)
cfprMgmtBackupFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmRmtInvErrDescr.setStatus("current")
_CfprMgmtBackupFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtBackupFsmRmtInvRslt_Object = MibTableColumn
cfprMgmtBackupFsmRmtInvRslt = _CfprMgmtBackupFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 11),
    _CfprMgmtBackupFsmRmtInvRslt_Type()
)
cfprMgmtBackupFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmRmtInvRslt.setStatus("current")
_CfprMgmtBackupFsmStageDescr_Type = SnmpAdminString
_CfprMgmtBackupFsmStageDescr_Object = MibTableColumn
cfprMgmtBackupFsmStageDescr = _CfprMgmtBackupFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 12),
    _CfprMgmtBackupFsmStageDescr_Type()
)
cfprMgmtBackupFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStageDescr.setStatus("current")
_CfprMgmtBackupFsmStamp_Type = DateAndTime
_CfprMgmtBackupFsmStamp_Object = MibTableColumn
cfprMgmtBackupFsmStamp = _CfprMgmtBackupFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 13),
    _CfprMgmtBackupFsmStamp_Type()
)
cfprMgmtBackupFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStamp.setStatus("current")
_CfprMgmtBackupFsmStatus_Type = SnmpAdminString
_CfprMgmtBackupFsmStatus_Object = MibTableColumn
cfprMgmtBackupFsmStatus = _CfprMgmtBackupFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 14),
    _CfprMgmtBackupFsmStatus_Type()
)
cfprMgmtBackupFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStatus.setStatus("current")
_CfprMgmtBackupFsmTry_Type = Gauge32
_CfprMgmtBackupFsmTry_Object = MibTableColumn
cfprMgmtBackupFsmTry = _CfprMgmtBackupFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 15),
    _CfprMgmtBackupFsmTry_Type()
)
cfprMgmtBackupFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmTry.setStatus("current")
_CfprMgmtBackupHostname_Type = SnmpAdminString
_CfprMgmtBackupHostname_Object = MibTableColumn
cfprMgmtBackupHostname = _CfprMgmtBackupHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 16),
    _CfprMgmtBackupHostname_Type()
)
cfprMgmtBackupHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupHostname.setStatus("current")
_CfprMgmtBackupIntId_Type = SnmpAdminString
_CfprMgmtBackupIntId_Object = MibTableColumn
cfprMgmtBackupIntId = _CfprMgmtBackupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 17),
    _CfprMgmtBackupIntId_Type()
)
cfprMgmtBackupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupIntId.setStatus("current")
_CfprMgmtBackupJob_Type = CfprMgmtBackupJob
_CfprMgmtBackupJob_Object = MibTableColumn
cfprMgmtBackupJob = _CfprMgmtBackupJob_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 18),
    _CfprMgmtBackupJob_Type()
)
cfprMgmtBackupJob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupJob.setStatus("current")
_CfprMgmtBackupMaxFiles_Type = Gauge32
_CfprMgmtBackupMaxFiles_Object = MibTableColumn
cfprMgmtBackupMaxFiles = _CfprMgmtBackupMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 19),
    _CfprMgmtBackupMaxFiles_Type()
)
cfprMgmtBackupMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupMaxFiles.setStatus("current")
_CfprMgmtBackupName_Type = SnmpAdminString
_CfprMgmtBackupName_Object = MibTableColumn
cfprMgmtBackupName = _CfprMgmtBackupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 20),
    _CfprMgmtBackupName_Type()
)
cfprMgmtBackupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupName.setStatus("current")
_CfprMgmtBackupOwnerPolicy_Type = SnmpAdminString
_CfprMgmtBackupOwnerPolicy_Object = MibTableColumn
cfprMgmtBackupOwnerPolicy = _CfprMgmtBackupOwnerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 21),
    _CfprMgmtBackupOwnerPolicy_Type()
)
cfprMgmtBackupOwnerPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupOwnerPolicy.setStatus("current")
_CfprMgmtBackupPolicyLevel_Type = Gauge32
_CfprMgmtBackupPolicyLevel_Object = MibTableColumn
cfprMgmtBackupPolicyLevel = _CfprMgmtBackupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 22),
    _CfprMgmtBackupPolicyLevel_Type()
)
cfprMgmtBackupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyLevel.setStatus("current")
_CfprMgmtBackupPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprMgmtBackupPolicyOwner_Object = MibTableColumn
cfprMgmtBackupPolicyOwner = _CfprMgmtBackupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 23),
    _CfprMgmtBackupPolicyOwner_Type()
)
cfprMgmtBackupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyOwner.setStatus("current")
_CfprMgmtBackupPostAction_Type = CfprMgmtBackupPostAction
_CfprMgmtBackupPostAction_Object = MibTableColumn
cfprMgmtBackupPostAction = _CfprMgmtBackupPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 24),
    _CfprMgmtBackupPostAction_Type()
)
cfprMgmtBackupPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPostAction.setStatus("current")
_CfprMgmtBackupPreservePooledValues_Type = TruthValue
_CfprMgmtBackupPreservePooledValues_Object = MibTableColumn
cfprMgmtBackupPreservePooledValues = _CfprMgmtBackupPreservePooledValues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 25),
    _CfprMgmtBackupPreservePooledValues_Type()
)
cfprMgmtBackupPreservePooledValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPreservePooledValues.setStatus("current")
_CfprMgmtBackupProto_Type = CfprMgmtBackupProto
_CfprMgmtBackupProto_Object = MibTableColumn
cfprMgmtBackupProto = _CfprMgmtBackupProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 26),
    _CfprMgmtBackupProto_Type()
)
cfprMgmtBackupProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupProto.setStatus("current")
_CfprMgmtBackupPwd_Type = SnmpAdminString
_CfprMgmtBackupPwd_Object = MibTableColumn
cfprMgmtBackupPwd = _CfprMgmtBackupPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 27),
    _CfprMgmtBackupPwd_Type()
)
cfprMgmtBackupPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPwd.setStatus("current")
_CfprMgmtBackupRemoteFile_Type = SnmpAdminString
_CfprMgmtBackupRemoteFile_Object = MibTableColumn
cfprMgmtBackupRemoteFile = _CfprMgmtBackupRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 28),
    _CfprMgmtBackupRemoteFile_Type()
)
cfprMgmtBackupRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupRemoteFile.setStatus("current")
_CfprMgmtBackupType_Type = CfprMgmtBackupType
_CfprMgmtBackupType_Object = MibTableColumn
cfprMgmtBackupType = _CfprMgmtBackupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 29),
    _CfprMgmtBackupType_Type()
)
cfprMgmtBackupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupType.setStatus("current")
_CfprMgmtBackupUser_Type = SnmpAdminString
_CfprMgmtBackupUser_Object = MibTableColumn
cfprMgmtBackupUser = _CfprMgmtBackupUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 30),
    _CfprMgmtBackupUser_Type()
)
cfprMgmtBackupUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupUser.setStatus("current")
_CfprMgmtBackupOperStatus_Type = CfprMgmtBackupStatus
_CfprMgmtBackupOperStatus_Object = MibTableColumn
cfprMgmtBackupOperStatus = _CfprMgmtBackupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 31),
    _CfprMgmtBackupOperStatus_Type()
)
cfprMgmtBackupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupOperStatus.setStatus("current")
_CfprMgmtBackupPort_Type = Gauge32
_CfprMgmtBackupPort_Object = MibTableColumn
cfprMgmtBackupPort = _CfprMgmtBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 32),
    _CfprMgmtBackupPort_Type()
)
cfprMgmtBackupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPort.setStatus("current")
_CfprMgmtBackupErrMsg_Type = SnmpAdminString
_CfprMgmtBackupErrMsg_Object = MibTableColumn
cfprMgmtBackupErrMsg = _CfprMgmtBackupErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 4, 1, 33),
    _CfprMgmtBackupErrMsg_Type()
)
cfprMgmtBackupErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupErrMsg.setStatus("current")
_CfprMgmtBackupExportExtPolicyTable_Object = MibTable
cfprMgmtBackupExportExtPolicyTable = _CfprMgmtBackupExportExtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 5)
)
if mibBuilder.loadTexts:
    cfprMgmtBackupExportExtPolicyTable.setStatus("current")
_CfprMgmtBackupExportExtPolicyEntry_Object = MibTableRow
cfprMgmtBackupExportExtPolicyEntry = _CfprMgmtBackupExportExtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 5, 1)
)
cfprMgmtBackupExportExtPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtBackupExportExtPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtBackupExportExtPolicyEntry.setStatus("current")
_CfprMgmtBackupExportExtPolicyInstanceId_Type = CfprManagedObjectId
_CfprMgmtBackupExportExtPolicyInstanceId_Object = MibTableColumn
cfprMgmtBackupExportExtPolicyInstanceId = _CfprMgmtBackupExportExtPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 5, 1, 1),
    _CfprMgmtBackupExportExtPolicyInstanceId_Type()
)
cfprMgmtBackupExportExtPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtBackupExportExtPolicyInstanceId.setStatus("current")
_CfprMgmtBackupExportExtPolicyDn_Type = CfprManagedObjectDn
_CfprMgmtBackupExportExtPolicyDn_Object = MibTableColumn
cfprMgmtBackupExportExtPolicyDn = _CfprMgmtBackupExportExtPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 5, 1, 2),
    _CfprMgmtBackupExportExtPolicyDn_Type()
)
cfprMgmtBackupExportExtPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupExportExtPolicyDn.setStatus("current")
_CfprMgmtBackupExportExtPolicyRn_Type = SnmpAdminString
_CfprMgmtBackupExportExtPolicyRn_Object = MibTableColumn
cfprMgmtBackupExportExtPolicyRn = _CfprMgmtBackupExportExtPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 5, 1, 3),
    _CfprMgmtBackupExportExtPolicyRn_Type()
)
cfprMgmtBackupExportExtPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupExportExtPolicyRn.setStatus("current")
_CfprMgmtBackupExportExtPolicyAdminState_Type = CfprMgmtAdminState
_CfprMgmtBackupExportExtPolicyAdminState_Object = MibTableColumn
cfprMgmtBackupExportExtPolicyAdminState = _CfprMgmtBackupExportExtPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 5, 1, 4),
    _CfprMgmtBackupExportExtPolicyAdminState_Type()
)
cfprMgmtBackupExportExtPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupExportExtPolicyAdminState.setStatus("current")
_CfprMgmtBackupExportExtPolicyDescr_Type = SnmpAdminString
_CfprMgmtBackupExportExtPolicyDescr_Object = MibTableColumn
cfprMgmtBackupExportExtPolicyDescr = _CfprMgmtBackupExportExtPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 5, 1, 5),
    _CfprMgmtBackupExportExtPolicyDescr_Type()
)
cfprMgmtBackupExportExtPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupExportExtPolicyDescr.setStatus("current")
_CfprMgmtBackupExportExtPolicyFrequency_Type = Gauge32
_CfprMgmtBackupExportExtPolicyFrequency_Object = MibTableColumn
cfprMgmtBackupExportExtPolicyFrequency = _CfprMgmtBackupExportExtPolicyFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 5, 1, 6),
    _CfprMgmtBackupExportExtPolicyFrequency_Type()
)
cfprMgmtBackupExportExtPolicyFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupExportExtPolicyFrequency.setStatus("current")
_CfprMgmtBackupExportExtPolicyIntId_Type = SnmpAdminString
_CfprMgmtBackupExportExtPolicyIntId_Object = MibTableColumn
cfprMgmtBackupExportExtPolicyIntId = _CfprMgmtBackupExportExtPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 5, 1, 7),
    _CfprMgmtBackupExportExtPolicyIntId_Type()
)
cfprMgmtBackupExportExtPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupExportExtPolicyIntId.setStatus("current")
_CfprMgmtBackupExportExtPolicyName_Type = SnmpAdminString
_CfprMgmtBackupExportExtPolicyName_Object = MibTableColumn
cfprMgmtBackupExportExtPolicyName = _CfprMgmtBackupExportExtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 5, 1, 8),
    _CfprMgmtBackupExportExtPolicyName_Type()
)
cfprMgmtBackupExportExtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupExportExtPolicyName.setStatus("current")
_CfprMgmtBackupExportExtPolicyPolicyLevel_Type = Gauge32
_CfprMgmtBackupExportExtPolicyPolicyLevel_Object = MibTableColumn
cfprMgmtBackupExportExtPolicyPolicyLevel = _CfprMgmtBackupExportExtPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 5, 1, 9),
    _CfprMgmtBackupExportExtPolicyPolicyLevel_Type()
)
cfprMgmtBackupExportExtPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupExportExtPolicyPolicyLevel.setStatus("current")
_CfprMgmtBackupExportExtPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprMgmtBackupExportExtPolicyPolicyOwner_Object = MibTableColumn
cfprMgmtBackupExportExtPolicyPolicyOwner = _CfprMgmtBackupExportExtPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 5, 1, 10),
    _CfprMgmtBackupExportExtPolicyPolicyOwner_Type()
)
cfprMgmtBackupExportExtPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupExportExtPolicyPolicyOwner.setStatus("current")
_CfprMgmtBackupFsmTable_Object = MibTable
cfprMgmtBackupFsmTable = _CfprMgmtBackupFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6)
)
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmTable.setStatus("current")
_CfprMgmtBackupFsmEntry_Object = MibTableRow
cfprMgmtBackupFsmEntry = _CfprMgmtBackupFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6, 1)
)
cfprMgmtBackupFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtBackupFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmEntry.setStatus("current")
_CfprMgmtBackupFsmInstanceId_Type = CfprManagedObjectId
_CfprMgmtBackupFsmInstanceId_Object = MibTableColumn
cfprMgmtBackupFsmInstanceId = _CfprMgmtBackupFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6, 1, 1),
    _CfprMgmtBackupFsmInstanceId_Type()
)
cfprMgmtBackupFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmInstanceId.setStatus("current")
_CfprMgmtBackupFsmDn_Type = CfprManagedObjectDn
_CfprMgmtBackupFsmDn_Object = MibTableColumn
cfprMgmtBackupFsmDn = _CfprMgmtBackupFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6, 1, 2),
    _CfprMgmtBackupFsmDn_Type()
)
cfprMgmtBackupFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmDn.setStatus("current")
_CfprMgmtBackupFsmRn_Type = SnmpAdminString
_CfprMgmtBackupFsmRn_Object = MibTableColumn
cfprMgmtBackupFsmRn = _CfprMgmtBackupFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6, 1, 3),
    _CfprMgmtBackupFsmRn_Type()
)
cfprMgmtBackupFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmRn.setStatus("current")
_CfprMgmtBackupFsmCompletionTime_Type = DateAndTime
_CfprMgmtBackupFsmCompletionTime_Object = MibTableColumn
cfprMgmtBackupFsmCompletionTime = _CfprMgmtBackupFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6, 1, 4),
    _CfprMgmtBackupFsmCompletionTime_Type()
)
cfprMgmtBackupFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmCompletionTime.setStatus("current")
_CfprMgmtBackupFsmCurrentFsm_Type = CfprMgmtBackupFsmCurrentFsm
_CfprMgmtBackupFsmCurrentFsm_Object = MibTableColumn
cfprMgmtBackupFsmCurrentFsm = _CfprMgmtBackupFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6, 1, 5),
    _CfprMgmtBackupFsmCurrentFsm_Type()
)
cfprMgmtBackupFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmCurrentFsm.setStatus("current")
_CfprMgmtBackupFsmDescrData_Type = SnmpAdminString
_CfprMgmtBackupFsmDescrData_Object = MibTableColumn
cfprMgmtBackupFsmDescrData = _CfprMgmtBackupFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6, 1, 6),
    _CfprMgmtBackupFsmDescrData_Type()
)
cfprMgmtBackupFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmDescrData.setStatus("current")
_CfprMgmtBackupFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtBackupFsmFsmStatus_Object = MibTableColumn
cfprMgmtBackupFsmFsmStatus = _CfprMgmtBackupFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6, 1, 7),
    _CfprMgmtBackupFsmFsmStatus_Type()
)
cfprMgmtBackupFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmFsmStatus.setStatus("current")
_CfprMgmtBackupFsmProgress_Type = Gauge32
_CfprMgmtBackupFsmProgress_Object = MibTableColumn
cfprMgmtBackupFsmProgress = _CfprMgmtBackupFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6, 1, 8),
    _CfprMgmtBackupFsmProgress_Type()
)
cfprMgmtBackupFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmProgress.setStatus("current")
_CfprMgmtBackupFsmRmtErrCode_Type = Gauge32
_CfprMgmtBackupFsmRmtErrCode_Object = MibTableColumn
cfprMgmtBackupFsmRmtErrCode = _CfprMgmtBackupFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6, 1, 9),
    _CfprMgmtBackupFsmRmtErrCode_Type()
)
cfprMgmtBackupFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmRmtErrCode.setStatus("current")
_CfprMgmtBackupFsmRmtErrDescr_Type = SnmpAdminString
_CfprMgmtBackupFsmRmtErrDescr_Object = MibTableColumn
cfprMgmtBackupFsmRmtErrDescr = _CfprMgmtBackupFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6, 1, 10),
    _CfprMgmtBackupFsmRmtErrDescr_Type()
)
cfprMgmtBackupFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmRmtErrDescr.setStatus("current")
_CfprMgmtBackupFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtBackupFsmRmtRslt_Object = MibTableColumn
cfprMgmtBackupFsmRmtRslt = _CfprMgmtBackupFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 6, 1, 11),
    _CfprMgmtBackupFsmRmtRslt_Type()
)
cfprMgmtBackupFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmRmtRslt.setStatus("current")
_CfprMgmtBackupFsmStageTable_Object = MibTable
cfprMgmtBackupFsmStageTable = _CfprMgmtBackupFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 7)
)
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStageTable.setStatus("current")
_CfprMgmtBackupFsmStageEntry_Object = MibTableRow
cfprMgmtBackupFsmStageEntry = _CfprMgmtBackupFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 7, 1)
)
cfprMgmtBackupFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtBackupFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStageEntry.setStatus("current")
_CfprMgmtBackupFsmStageInstanceId_Type = CfprManagedObjectId
_CfprMgmtBackupFsmStageInstanceId_Object = MibTableColumn
cfprMgmtBackupFsmStageInstanceId = _CfprMgmtBackupFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 7, 1, 1),
    _CfprMgmtBackupFsmStageInstanceId_Type()
)
cfprMgmtBackupFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStageInstanceId.setStatus("current")
_CfprMgmtBackupFsmStageDn_Type = CfprManagedObjectDn
_CfprMgmtBackupFsmStageDn_Object = MibTableColumn
cfprMgmtBackupFsmStageDn = _CfprMgmtBackupFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 7, 1, 2),
    _CfprMgmtBackupFsmStageDn_Type()
)
cfprMgmtBackupFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStageDn.setStatus("current")
_CfprMgmtBackupFsmStageRn_Type = SnmpAdminString
_CfprMgmtBackupFsmStageRn_Object = MibTableColumn
cfprMgmtBackupFsmStageRn = _CfprMgmtBackupFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 7, 1, 3),
    _CfprMgmtBackupFsmStageRn_Type()
)
cfprMgmtBackupFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStageRn.setStatus("current")
_CfprMgmtBackupFsmStageDescrData_Type = SnmpAdminString
_CfprMgmtBackupFsmStageDescrData_Object = MibTableColumn
cfprMgmtBackupFsmStageDescrData = _CfprMgmtBackupFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 7, 1, 4),
    _CfprMgmtBackupFsmStageDescrData_Type()
)
cfprMgmtBackupFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStageDescrData.setStatus("current")
_CfprMgmtBackupFsmStageLastUpdateTime_Type = DateAndTime
_CfprMgmtBackupFsmStageLastUpdateTime_Object = MibTableColumn
cfprMgmtBackupFsmStageLastUpdateTime = _CfprMgmtBackupFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 7, 1, 5),
    _CfprMgmtBackupFsmStageLastUpdateTime_Type()
)
cfprMgmtBackupFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStageLastUpdateTime.setStatus("current")
_CfprMgmtBackupFsmStageName_Type = CfprMgmtBackupFsmStageName
_CfprMgmtBackupFsmStageName_Object = MibTableColumn
cfprMgmtBackupFsmStageName = _CfprMgmtBackupFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 7, 1, 6),
    _CfprMgmtBackupFsmStageName_Type()
)
cfprMgmtBackupFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStageName.setStatus("current")
_CfprMgmtBackupFsmStageOrder_Type = Gauge32
_CfprMgmtBackupFsmStageOrder_Object = MibTableColumn
cfprMgmtBackupFsmStageOrder = _CfprMgmtBackupFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 7, 1, 7),
    _CfprMgmtBackupFsmStageOrder_Type()
)
cfprMgmtBackupFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStageOrder.setStatus("current")
_CfprMgmtBackupFsmStageRetry_Type = Gauge32
_CfprMgmtBackupFsmStageRetry_Object = MibTableColumn
cfprMgmtBackupFsmStageRetry = _CfprMgmtBackupFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 7, 1, 8),
    _CfprMgmtBackupFsmStageRetry_Type()
)
cfprMgmtBackupFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStageRetry.setStatus("current")
_CfprMgmtBackupFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtBackupFsmStageStageStatus_Object = MibTableColumn
cfprMgmtBackupFsmStageStageStatus = _CfprMgmtBackupFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 7, 1, 9),
    _CfprMgmtBackupFsmStageStageStatus_Type()
)
cfprMgmtBackupFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmStageStageStatus.setStatus("current")
_CfprMgmtBackupFsmTaskTable_Object = MibTable
cfprMgmtBackupFsmTaskTable = _CfprMgmtBackupFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 8)
)
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmTaskTable.setStatus("current")
_CfprMgmtBackupFsmTaskEntry_Object = MibTableRow
cfprMgmtBackupFsmTaskEntry = _CfprMgmtBackupFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 8, 1)
)
cfprMgmtBackupFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtBackupFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmTaskEntry.setStatus("current")
_CfprMgmtBackupFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprMgmtBackupFsmTaskInstanceId_Object = MibTableColumn
cfprMgmtBackupFsmTaskInstanceId = _CfprMgmtBackupFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 8, 1, 1),
    _CfprMgmtBackupFsmTaskInstanceId_Type()
)
cfprMgmtBackupFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmTaskInstanceId.setStatus("current")
_CfprMgmtBackupFsmTaskDn_Type = CfprManagedObjectDn
_CfprMgmtBackupFsmTaskDn_Object = MibTableColumn
cfprMgmtBackupFsmTaskDn = _CfprMgmtBackupFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 8, 1, 2),
    _CfprMgmtBackupFsmTaskDn_Type()
)
cfprMgmtBackupFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmTaskDn.setStatus("current")
_CfprMgmtBackupFsmTaskRn_Type = SnmpAdminString
_CfprMgmtBackupFsmTaskRn_Object = MibTableColumn
cfprMgmtBackupFsmTaskRn = _CfprMgmtBackupFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 8, 1, 3),
    _CfprMgmtBackupFsmTaskRn_Type()
)
cfprMgmtBackupFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmTaskRn.setStatus("current")
_CfprMgmtBackupFsmTaskCompletion_Type = CfprFsmCompletion
_CfprMgmtBackupFsmTaskCompletion_Object = MibTableColumn
cfprMgmtBackupFsmTaskCompletion = _CfprMgmtBackupFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 8, 1, 4),
    _CfprMgmtBackupFsmTaskCompletion_Type()
)
cfprMgmtBackupFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmTaskCompletion.setStatus("current")
_CfprMgmtBackupFsmTaskFlags_Type = CfprFsmFlags
_CfprMgmtBackupFsmTaskFlags_Object = MibTableColumn
cfprMgmtBackupFsmTaskFlags = _CfprMgmtBackupFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 8, 1, 5),
    _CfprMgmtBackupFsmTaskFlags_Type()
)
cfprMgmtBackupFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmTaskFlags.setStatus("current")
_CfprMgmtBackupFsmTaskItem_Type = CfprMgmtBackupFsmTaskItem
_CfprMgmtBackupFsmTaskItem_Object = MibTableColumn
cfprMgmtBackupFsmTaskItem = _CfprMgmtBackupFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 8, 1, 6),
    _CfprMgmtBackupFsmTaskItem_Type()
)
cfprMgmtBackupFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmTaskItem.setStatus("current")
_CfprMgmtBackupFsmTaskSeqId_Type = Gauge32
_CfprMgmtBackupFsmTaskSeqId_Object = MibTableColumn
cfprMgmtBackupFsmTaskSeqId = _CfprMgmtBackupFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 8, 1, 7),
    _CfprMgmtBackupFsmTaskSeqId_Type()
)
cfprMgmtBackupFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupFsmTaskSeqId.setStatus("current")
_CfprMgmtBackupPolicyTable_Object = MibTable
cfprMgmtBackupPolicyTable = _CfprMgmtBackupPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9)
)
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyTable.setStatus("current")
_CfprMgmtBackupPolicyEntry_Object = MibTableRow
cfprMgmtBackupPolicyEntry = _CfprMgmtBackupPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1)
)
cfprMgmtBackupPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtBackupPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyEntry.setStatus("current")
_CfprMgmtBackupPolicyInstanceId_Type = CfprManagedObjectId
_CfprMgmtBackupPolicyInstanceId_Object = MibTableColumn
cfprMgmtBackupPolicyInstanceId = _CfprMgmtBackupPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 1),
    _CfprMgmtBackupPolicyInstanceId_Type()
)
cfprMgmtBackupPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyInstanceId.setStatus("current")
_CfprMgmtBackupPolicyDn_Type = CfprManagedObjectDn
_CfprMgmtBackupPolicyDn_Object = MibTableColumn
cfprMgmtBackupPolicyDn = _CfprMgmtBackupPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 2),
    _CfprMgmtBackupPolicyDn_Type()
)
cfprMgmtBackupPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyDn.setStatus("current")
_CfprMgmtBackupPolicyRn_Type = SnmpAdminString
_CfprMgmtBackupPolicyRn_Object = MibTableColumn
cfprMgmtBackupPolicyRn = _CfprMgmtBackupPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 3),
    _CfprMgmtBackupPolicyRn_Type()
)
cfprMgmtBackupPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyRn.setStatus("current")
_CfprMgmtBackupPolicyAdminState_Type = CfprMgmtExportPolicyAdminState
_CfprMgmtBackupPolicyAdminState_Object = MibTableColumn
cfprMgmtBackupPolicyAdminState = _CfprMgmtBackupPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 4),
    _CfprMgmtBackupPolicyAdminState_Type()
)
cfprMgmtBackupPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyAdminState.setStatus("current")
_CfprMgmtBackupPolicyDescr_Type = SnmpAdminString
_CfprMgmtBackupPolicyDescr_Object = MibTableColumn
cfprMgmtBackupPolicyDescr = _CfprMgmtBackupPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 5),
    _CfprMgmtBackupPolicyDescr_Type()
)
cfprMgmtBackupPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyDescr.setStatus("current")
_CfprMgmtBackupPolicyFsmDescr_Type = SnmpAdminString
_CfprMgmtBackupPolicyFsmDescr_Object = MibTableColumn
cfprMgmtBackupPolicyFsmDescr = _CfprMgmtBackupPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 6),
    _CfprMgmtBackupPolicyFsmDescr_Type()
)
cfprMgmtBackupPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmDescr.setStatus("current")
_CfprMgmtBackupPolicyFsmPrev_Type = SnmpAdminString
_CfprMgmtBackupPolicyFsmPrev_Object = MibTableColumn
cfprMgmtBackupPolicyFsmPrev = _CfprMgmtBackupPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 7),
    _CfprMgmtBackupPolicyFsmPrev_Type()
)
cfprMgmtBackupPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmPrev.setStatus("current")
_CfprMgmtBackupPolicyFsmProgr_Type = Gauge32
_CfprMgmtBackupPolicyFsmProgr_Object = MibTableColumn
cfprMgmtBackupPolicyFsmProgr = _CfprMgmtBackupPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 8),
    _CfprMgmtBackupPolicyFsmProgr_Type()
)
cfprMgmtBackupPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmProgr.setStatus("current")
_CfprMgmtBackupPolicyFsmRmtInvErrCode_Type = Gauge32
_CfprMgmtBackupPolicyFsmRmtInvErrCode_Object = MibTableColumn
cfprMgmtBackupPolicyFsmRmtInvErrCode = _CfprMgmtBackupPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 9),
    _CfprMgmtBackupPolicyFsmRmtInvErrCode_Type()
)
cfprMgmtBackupPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmRmtInvErrCode.setStatus("current")
_CfprMgmtBackupPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprMgmtBackupPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cfprMgmtBackupPolicyFsmRmtInvErrDescr = _CfprMgmtBackupPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 10),
    _CfprMgmtBackupPolicyFsmRmtInvErrDescr_Type()
)
cfprMgmtBackupPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmRmtInvErrDescr.setStatus("current")
_CfprMgmtBackupPolicyFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtBackupPolicyFsmRmtInvRslt_Object = MibTableColumn
cfprMgmtBackupPolicyFsmRmtInvRslt = _CfprMgmtBackupPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 11),
    _CfprMgmtBackupPolicyFsmRmtInvRslt_Type()
)
cfprMgmtBackupPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmRmtInvRslt.setStatus("current")
_CfprMgmtBackupPolicyFsmStageDescr_Type = SnmpAdminString
_CfprMgmtBackupPolicyFsmStageDescr_Object = MibTableColumn
cfprMgmtBackupPolicyFsmStageDescr = _CfprMgmtBackupPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 12),
    _CfprMgmtBackupPolicyFsmStageDescr_Type()
)
cfprMgmtBackupPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStageDescr.setStatus("current")
_CfprMgmtBackupPolicyFsmStamp_Type = DateAndTime
_CfprMgmtBackupPolicyFsmStamp_Object = MibTableColumn
cfprMgmtBackupPolicyFsmStamp = _CfprMgmtBackupPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 13),
    _CfprMgmtBackupPolicyFsmStamp_Type()
)
cfprMgmtBackupPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStamp.setStatus("current")
_CfprMgmtBackupPolicyFsmStatus_Type = SnmpAdminString
_CfprMgmtBackupPolicyFsmStatus_Object = MibTableColumn
cfprMgmtBackupPolicyFsmStatus = _CfprMgmtBackupPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 14),
    _CfprMgmtBackupPolicyFsmStatus_Type()
)
cfprMgmtBackupPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStatus.setStatus("current")
_CfprMgmtBackupPolicyFsmTry_Type = Gauge32
_CfprMgmtBackupPolicyFsmTry_Object = MibTableColumn
cfprMgmtBackupPolicyFsmTry = _CfprMgmtBackupPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 15),
    _CfprMgmtBackupPolicyFsmTry_Type()
)
cfprMgmtBackupPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmTry.setStatus("current")
_CfprMgmtBackupPolicyHost_Type = SnmpAdminString
_CfprMgmtBackupPolicyHost_Object = MibTableColumn
cfprMgmtBackupPolicyHost = _CfprMgmtBackupPolicyHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 16),
    _CfprMgmtBackupPolicyHost_Type()
)
cfprMgmtBackupPolicyHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyHost.setStatus("current")
_CfprMgmtBackupPolicyIntId_Type = SnmpAdminString
_CfprMgmtBackupPolicyIntId_Object = MibTableColumn
cfprMgmtBackupPolicyIntId = _CfprMgmtBackupPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 17),
    _CfprMgmtBackupPolicyIntId_Type()
)
cfprMgmtBackupPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyIntId.setStatus("current")
_CfprMgmtBackupPolicyLastBackup_Type = DateAndTime
_CfprMgmtBackupPolicyLastBackup_Object = MibTableColumn
cfprMgmtBackupPolicyLastBackup = _CfprMgmtBackupPolicyLastBackup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 18),
    _CfprMgmtBackupPolicyLastBackup_Type()
)
cfprMgmtBackupPolicyLastBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyLastBackup.setStatus("current")
_CfprMgmtBackupPolicyMaxFiles_Type = Gauge32
_CfprMgmtBackupPolicyMaxFiles_Object = MibTableColumn
cfprMgmtBackupPolicyMaxFiles = _CfprMgmtBackupPolicyMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 19),
    _CfprMgmtBackupPolicyMaxFiles_Type()
)
cfprMgmtBackupPolicyMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyMaxFiles.setStatus("current")
_CfprMgmtBackupPolicyName_Type = SnmpAdminString
_CfprMgmtBackupPolicyName_Object = MibTableColumn
cfprMgmtBackupPolicyName = _CfprMgmtBackupPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 20),
    _CfprMgmtBackupPolicyName_Type()
)
cfprMgmtBackupPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyName.setStatus("current")
_CfprMgmtBackupPolicyPolicyLevel_Type = Gauge32
_CfprMgmtBackupPolicyPolicyLevel_Object = MibTableColumn
cfprMgmtBackupPolicyPolicyLevel = _CfprMgmtBackupPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 21),
    _CfprMgmtBackupPolicyPolicyLevel_Type()
)
cfprMgmtBackupPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyPolicyLevel.setStatus("current")
_CfprMgmtBackupPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprMgmtBackupPolicyPolicyOwner_Object = MibTableColumn
cfprMgmtBackupPolicyPolicyOwner = _CfprMgmtBackupPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 22),
    _CfprMgmtBackupPolicyPolicyOwner_Type()
)
cfprMgmtBackupPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyPolicyOwner.setStatus("current")
_CfprMgmtBackupPolicyProto_Type = CfprMgmtExportPolicyProto
_CfprMgmtBackupPolicyProto_Object = MibTableColumn
cfprMgmtBackupPolicyProto = _CfprMgmtBackupPolicyProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 23),
    _CfprMgmtBackupPolicyProto_Type()
)
cfprMgmtBackupPolicyProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyProto.setStatus("current")
_CfprMgmtBackupPolicyPwd_Type = SnmpAdminString
_CfprMgmtBackupPolicyPwd_Object = MibTableColumn
cfprMgmtBackupPolicyPwd = _CfprMgmtBackupPolicyPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 24),
    _CfprMgmtBackupPolicyPwd_Type()
)
cfprMgmtBackupPolicyPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyPwd.setStatus("current")
_CfprMgmtBackupPolicyRemoteFile_Type = SnmpAdminString
_CfprMgmtBackupPolicyRemoteFile_Object = MibTableColumn
cfprMgmtBackupPolicyRemoteFile = _CfprMgmtBackupPolicyRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 25),
    _CfprMgmtBackupPolicyRemoteFile_Type()
)
cfprMgmtBackupPolicyRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyRemoteFile.setStatus("current")
_CfprMgmtBackupPolicySchedule_Type = CfprMgmtBackupInterval
_CfprMgmtBackupPolicySchedule_Object = MibTableColumn
cfprMgmtBackupPolicySchedule = _CfprMgmtBackupPolicySchedule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 26),
    _CfprMgmtBackupPolicySchedule_Type()
)
cfprMgmtBackupPolicySchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicySchedule.setStatus("current")
_CfprMgmtBackupPolicyUser_Type = SnmpAdminString
_CfprMgmtBackupPolicyUser_Object = MibTableColumn
cfprMgmtBackupPolicyUser = _CfprMgmtBackupPolicyUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 27),
    _CfprMgmtBackupPolicyUser_Type()
)
cfprMgmtBackupPolicyUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyUser.setStatus("current")
_CfprMgmtBackupPolicyPort_Type = Gauge32
_CfprMgmtBackupPolicyPort_Object = MibTableColumn
cfprMgmtBackupPolicyPort = _CfprMgmtBackupPolicyPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 9, 1, 28),
    _CfprMgmtBackupPolicyPort_Type()
)
cfprMgmtBackupPolicyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyPort.setStatus("current")
_CfprMgmtBackupPolicyConfigTable_Object = MibTable
cfprMgmtBackupPolicyConfigTable = _CfprMgmtBackupPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10)
)
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigTable.setStatus("current")
_CfprMgmtBackupPolicyConfigEntry_Object = MibTableRow
cfprMgmtBackupPolicyConfigEntry = _CfprMgmtBackupPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1)
)
cfprMgmtBackupPolicyConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtBackupPolicyConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigEntry.setStatus("current")
_CfprMgmtBackupPolicyConfigInstanceId_Type = CfprManagedObjectId
_CfprMgmtBackupPolicyConfigInstanceId_Object = MibTableColumn
cfprMgmtBackupPolicyConfigInstanceId = _CfprMgmtBackupPolicyConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 1),
    _CfprMgmtBackupPolicyConfigInstanceId_Type()
)
cfprMgmtBackupPolicyConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigInstanceId.setStatus("current")
_CfprMgmtBackupPolicyConfigDn_Type = CfprManagedObjectDn
_CfprMgmtBackupPolicyConfigDn_Object = MibTableColumn
cfprMgmtBackupPolicyConfigDn = _CfprMgmtBackupPolicyConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 2),
    _CfprMgmtBackupPolicyConfigDn_Type()
)
cfprMgmtBackupPolicyConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigDn.setStatus("current")
_CfprMgmtBackupPolicyConfigRn_Type = SnmpAdminString
_CfprMgmtBackupPolicyConfigRn_Object = MibTableColumn
cfprMgmtBackupPolicyConfigRn = _CfprMgmtBackupPolicyConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 3),
    _CfprMgmtBackupPolicyConfigRn_Type()
)
cfprMgmtBackupPolicyConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigRn.setStatus("current")
_CfprMgmtBackupPolicyConfigAdminState_Type = CfprTrigAdminState
_CfprMgmtBackupPolicyConfigAdminState_Object = MibTableColumn
cfprMgmtBackupPolicyConfigAdminState = _CfprMgmtBackupPolicyConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 4),
    _CfprMgmtBackupPolicyConfigAdminState_Type()
)
cfprMgmtBackupPolicyConfigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigAdminState.setStatus("current")
_CfprMgmtBackupPolicyConfigAutoDelete_Type = TruthValue
_CfprMgmtBackupPolicyConfigAutoDelete_Object = MibTableColumn
cfprMgmtBackupPolicyConfigAutoDelete = _CfprMgmtBackupPolicyConfigAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 5),
    _CfprMgmtBackupPolicyConfigAutoDelete_Type()
)
cfprMgmtBackupPolicyConfigAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigAutoDelete.setStatus("current")
_CfprMgmtBackupPolicyConfigBackupDate_Type = DateAndTime
_CfprMgmtBackupPolicyConfigBackupDate_Object = MibTableColumn
cfprMgmtBackupPolicyConfigBackupDate = _CfprMgmtBackupPolicyConfigBackupDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 6),
    _CfprMgmtBackupPolicyConfigBackupDate_Type()
)
cfprMgmtBackupPolicyConfigBackupDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigBackupDate.setStatus("current")
_CfprMgmtBackupPolicyConfigBackupIssue_Type = CfprMgmtBackupIssue
_CfprMgmtBackupPolicyConfigBackupIssue_Object = MibTableColumn
cfprMgmtBackupPolicyConfigBackupIssue = _CfprMgmtBackupPolicyConfigBackupIssue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 7),
    _CfprMgmtBackupPolicyConfigBackupIssue_Type()
)
cfprMgmtBackupPolicyConfigBackupIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigBackupIssue.setStatus("current")
_CfprMgmtBackupPolicyConfigDescr_Type = SnmpAdminString
_CfprMgmtBackupPolicyConfigDescr_Object = MibTableColumn
cfprMgmtBackupPolicyConfigDescr = _CfprMgmtBackupPolicyConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 8),
    _CfprMgmtBackupPolicyConfigDescr_Type()
)
cfprMgmtBackupPolicyConfigDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigDescr.setStatus("current")
_CfprMgmtBackupPolicyConfigIgnoreCap_Type = TruthValue
_CfprMgmtBackupPolicyConfigIgnoreCap_Object = MibTableColumn
cfprMgmtBackupPolicyConfigIgnoreCap = _CfprMgmtBackupPolicyConfigIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 9),
    _CfprMgmtBackupPolicyConfigIgnoreCap_Type()
)
cfprMgmtBackupPolicyConfigIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigIgnoreCap.setStatus("current")
_CfprMgmtBackupPolicyConfigIntId_Type = SnmpAdminString
_CfprMgmtBackupPolicyConfigIntId_Object = MibTableColumn
cfprMgmtBackupPolicyConfigIntId = _CfprMgmtBackupPolicyConfigIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 10),
    _CfprMgmtBackupPolicyConfigIntId_Type()
)
cfprMgmtBackupPolicyConfigIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigIntId.setStatus("current")
_CfprMgmtBackupPolicyConfigName_Type = SnmpAdminString
_CfprMgmtBackupPolicyConfigName_Object = MibTableColumn
cfprMgmtBackupPolicyConfigName = _CfprMgmtBackupPolicyConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 11),
    _CfprMgmtBackupPolicyConfigName_Type()
)
cfprMgmtBackupPolicyConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigName.setStatus("current")
_CfprMgmtBackupPolicyConfigOperScheduler_Type = SnmpAdminString
_CfprMgmtBackupPolicyConfigOperScheduler_Object = MibTableColumn
cfprMgmtBackupPolicyConfigOperScheduler = _CfprMgmtBackupPolicyConfigOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 12),
    _CfprMgmtBackupPolicyConfigOperScheduler_Type()
)
cfprMgmtBackupPolicyConfigOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigOperScheduler.setStatus("current")
_CfprMgmtBackupPolicyConfigOperState_Type = CfprTrigTrigOperState
_CfprMgmtBackupPolicyConfigOperState_Object = MibTableColumn
cfprMgmtBackupPolicyConfigOperState = _CfprMgmtBackupPolicyConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 13),
    _CfprMgmtBackupPolicyConfigOperState_Type()
)
cfprMgmtBackupPolicyConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigOperState.setStatus("current")
_CfprMgmtBackupPolicyConfigPolicyLevel_Type = Gauge32
_CfprMgmtBackupPolicyConfigPolicyLevel_Object = MibTableColumn
cfprMgmtBackupPolicyConfigPolicyLevel = _CfprMgmtBackupPolicyConfigPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 14),
    _CfprMgmtBackupPolicyConfigPolicyLevel_Type()
)
cfprMgmtBackupPolicyConfigPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigPolicyLevel.setStatus("current")
_CfprMgmtBackupPolicyConfigPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprMgmtBackupPolicyConfigPolicyOwner_Object = MibTableColumn
cfprMgmtBackupPolicyConfigPolicyOwner = _CfprMgmtBackupPolicyConfigPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 15),
    _CfprMgmtBackupPolicyConfigPolicyOwner_Type()
)
cfprMgmtBackupPolicyConfigPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigPolicyOwner.setStatus("current")
_CfprMgmtBackupPolicyConfigScheduler_Type = SnmpAdminString
_CfprMgmtBackupPolicyConfigScheduler_Object = MibTableColumn
cfprMgmtBackupPolicyConfigScheduler = _CfprMgmtBackupPolicyConfigScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 10, 1, 16),
    _CfprMgmtBackupPolicyConfigScheduler_Type()
)
cfprMgmtBackupPolicyConfigScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyConfigScheduler.setStatus("current")
_CfprMgmtBackupPolicyFsmTable_Object = MibTable
cfprMgmtBackupPolicyFsmTable = _CfprMgmtBackupPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11)
)
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmTable.setStatus("current")
_CfprMgmtBackupPolicyFsmEntry_Object = MibTableRow
cfprMgmtBackupPolicyFsmEntry = _CfprMgmtBackupPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11, 1)
)
cfprMgmtBackupPolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtBackupPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmEntry.setStatus("current")
_CfprMgmtBackupPolicyFsmInstanceId_Type = CfprManagedObjectId
_CfprMgmtBackupPolicyFsmInstanceId_Object = MibTableColumn
cfprMgmtBackupPolicyFsmInstanceId = _CfprMgmtBackupPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11, 1, 1),
    _CfprMgmtBackupPolicyFsmInstanceId_Type()
)
cfprMgmtBackupPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmInstanceId.setStatus("current")
_CfprMgmtBackupPolicyFsmDn_Type = CfprManagedObjectDn
_CfprMgmtBackupPolicyFsmDn_Object = MibTableColumn
cfprMgmtBackupPolicyFsmDn = _CfprMgmtBackupPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11, 1, 2),
    _CfprMgmtBackupPolicyFsmDn_Type()
)
cfprMgmtBackupPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmDn.setStatus("current")
_CfprMgmtBackupPolicyFsmRn_Type = SnmpAdminString
_CfprMgmtBackupPolicyFsmRn_Object = MibTableColumn
cfprMgmtBackupPolicyFsmRn = _CfprMgmtBackupPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11, 1, 3),
    _CfprMgmtBackupPolicyFsmRn_Type()
)
cfprMgmtBackupPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmRn.setStatus("current")
_CfprMgmtBackupPolicyFsmCompletionTime_Type = DateAndTime
_CfprMgmtBackupPolicyFsmCompletionTime_Object = MibTableColumn
cfprMgmtBackupPolicyFsmCompletionTime = _CfprMgmtBackupPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11, 1, 4),
    _CfprMgmtBackupPolicyFsmCompletionTime_Type()
)
cfprMgmtBackupPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmCompletionTime.setStatus("current")
_CfprMgmtBackupPolicyFsmCurrentFsm_Type = CfprMgmtBackupPolicyFsmCurrentFsm
_CfprMgmtBackupPolicyFsmCurrentFsm_Object = MibTableColumn
cfprMgmtBackupPolicyFsmCurrentFsm = _CfprMgmtBackupPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11, 1, 5),
    _CfprMgmtBackupPolicyFsmCurrentFsm_Type()
)
cfprMgmtBackupPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmCurrentFsm.setStatus("current")
_CfprMgmtBackupPolicyFsmDescrData_Type = SnmpAdminString
_CfprMgmtBackupPolicyFsmDescrData_Object = MibTableColumn
cfprMgmtBackupPolicyFsmDescrData = _CfprMgmtBackupPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11, 1, 6),
    _CfprMgmtBackupPolicyFsmDescrData_Type()
)
cfprMgmtBackupPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmDescrData.setStatus("current")
_CfprMgmtBackupPolicyFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtBackupPolicyFsmFsmStatus_Object = MibTableColumn
cfprMgmtBackupPolicyFsmFsmStatus = _CfprMgmtBackupPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11, 1, 7),
    _CfprMgmtBackupPolicyFsmFsmStatus_Type()
)
cfprMgmtBackupPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmFsmStatus.setStatus("current")
_CfprMgmtBackupPolicyFsmProgress_Type = Gauge32
_CfprMgmtBackupPolicyFsmProgress_Object = MibTableColumn
cfprMgmtBackupPolicyFsmProgress = _CfprMgmtBackupPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11, 1, 8),
    _CfprMgmtBackupPolicyFsmProgress_Type()
)
cfprMgmtBackupPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmProgress.setStatus("current")
_CfprMgmtBackupPolicyFsmRmtErrCode_Type = Gauge32
_CfprMgmtBackupPolicyFsmRmtErrCode_Object = MibTableColumn
cfprMgmtBackupPolicyFsmRmtErrCode = _CfprMgmtBackupPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11, 1, 9),
    _CfprMgmtBackupPolicyFsmRmtErrCode_Type()
)
cfprMgmtBackupPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmRmtErrCode.setStatus("current")
_CfprMgmtBackupPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprMgmtBackupPolicyFsmRmtErrDescr_Object = MibTableColumn
cfprMgmtBackupPolicyFsmRmtErrDescr = _CfprMgmtBackupPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11, 1, 10),
    _CfprMgmtBackupPolicyFsmRmtErrDescr_Type()
)
cfprMgmtBackupPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmRmtErrDescr.setStatus("current")
_CfprMgmtBackupPolicyFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtBackupPolicyFsmRmtRslt_Object = MibTableColumn
cfprMgmtBackupPolicyFsmRmtRslt = _CfprMgmtBackupPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 11, 1, 11),
    _CfprMgmtBackupPolicyFsmRmtRslt_Type()
)
cfprMgmtBackupPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmRmtRslt.setStatus("current")
_CfprMgmtBackupPolicyFsmStageTable_Object = MibTable
cfprMgmtBackupPolicyFsmStageTable = _CfprMgmtBackupPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 12)
)
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStageTable.setStatus("current")
_CfprMgmtBackupPolicyFsmStageEntry_Object = MibTableRow
cfprMgmtBackupPolicyFsmStageEntry = _CfprMgmtBackupPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 12, 1)
)
cfprMgmtBackupPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtBackupPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStageEntry.setStatus("current")
_CfprMgmtBackupPolicyFsmStageInstanceId_Type = CfprManagedObjectId
_CfprMgmtBackupPolicyFsmStageInstanceId_Object = MibTableColumn
cfprMgmtBackupPolicyFsmStageInstanceId = _CfprMgmtBackupPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 12, 1, 1),
    _CfprMgmtBackupPolicyFsmStageInstanceId_Type()
)
cfprMgmtBackupPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStageInstanceId.setStatus("current")
_CfprMgmtBackupPolicyFsmStageDn_Type = CfprManagedObjectDn
_CfprMgmtBackupPolicyFsmStageDn_Object = MibTableColumn
cfprMgmtBackupPolicyFsmStageDn = _CfprMgmtBackupPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 12, 1, 2),
    _CfprMgmtBackupPolicyFsmStageDn_Type()
)
cfprMgmtBackupPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStageDn.setStatus("current")
_CfprMgmtBackupPolicyFsmStageRn_Type = SnmpAdminString
_CfprMgmtBackupPolicyFsmStageRn_Object = MibTableColumn
cfprMgmtBackupPolicyFsmStageRn = _CfprMgmtBackupPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 12, 1, 3),
    _CfprMgmtBackupPolicyFsmStageRn_Type()
)
cfprMgmtBackupPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStageRn.setStatus("current")
_CfprMgmtBackupPolicyFsmStageDescrData_Type = SnmpAdminString
_CfprMgmtBackupPolicyFsmStageDescrData_Object = MibTableColumn
cfprMgmtBackupPolicyFsmStageDescrData = _CfprMgmtBackupPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 12, 1, 4),
    _CfprMgmtBackupPolicyFsmStageDescrData_Type()
)
cfprMgmtBackupPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStageDescrData.setStatus("current")
_CfprMgmtBackupPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprMgmtBackupPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprMgmtBackupPolicyFsmStageLastUpdateTime = _CfprMgmtBackupPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 12, 1, 5),
    _CfprMgmtBackupPolicyFsmStageLastUpdateTime_Type()
)
cfprMgmtBackupPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStageLastUpdateTime.setStatus("current")
_CfprMgmtBackupPolicyFsmStageName_Type = CfprMgmtBackupPolicyFsmStageName
_CfprMgmtBackupPolicyFsmStageName_Object = MibTableColumn
cfprMgmtBackupPolicyFsmStageName = _CfprMgmtBackupPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 12, 1, 6),
    _CfprMgmtBackupPolicyFsmStageName_Type()
)
cfprMgmtBackupPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStageName.setStatus("current")
_CfprMgmtBackupPolicyFsmStageOrder_Type = Gauge32
_CfprMgmtBackupPolicyFsmStageOrder_Object = MibTableColumn
cfprMgmtBackupPolicyFsmStageOrder = _CfprMgmtBackupPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 12, 1, 7),
    _CfprMgmtBackupPolicyFsmStageOrder_Type()
)
cfprMgmtBackupPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStageOrder.setStatus("current")
_CfprMgmtBackupPolicyFsmStageRetry_Type = Gauge32
_CfprMgmtBackupPolicyFsmStageRetry_Object = MibTableColumn
cfprMgmtBackupPolicyFsmStageRetry = _CfprMgmtBackupPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 12, 1, 8),
    _CfprMgmtBackupPolicyFsmStageRetry_Type()
)
cfprMgmtBackupPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStageRetry.setStatus("current")
_CfprMgmtBackupPolicyFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtBackupPolicyFsmStageStageStatus_Object = MibTableColumn
cfprMgmtBackupPolicyFsmStageStageStatus = _CfprMgmtBackupPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 12, 1, 9),
    _CfprMgmtBackupPolicyFsmStageStageStatus_Type()
)
cfprMgmtBackupPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtBackupPolicyFsmStageStageStatus.setStatus("current")
_CfprMgmtCfgExportPolicyTable_Object = MibTable
cfprMgmtCfgExportPolicyTable = _CfprMgmtCfgExportPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13)
)
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyTable.setStatus("current")
_CfprMgmtCfgExportPolicyEntry_Object = MibTableRow
cfprMgmtCfgExportPolicyEntry = _CfprMgmtCfgExportPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1)
)
cfprMgmtCfgExportPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtCfgExportPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyEntry.setStatus("current")
_CfprMgmtCfgExportPolicyInstanceId_Type = CfprManagedObjectId
_CfprMgmtCfgExportPolicyInstanceId_Object = MibTableColumn
cfprMgmtCfgExportPolicyInstanceId = _CfprMgmtCfgExportPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 1),
    _CfprMgmtCfgExportPolicyInstanceId_Type()
)
cfprMgmtCfgExportPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyInstanceId.setStatus("current")
_CfprMgmtCfgExportPolicyDn_Type = CfprManagedObjectDn
_CfprMgmtCfgExportPolicyDn_Object = MibTableColumn
cfprMgmtCfgExportPolicyDn = _CfprMgmtCfgExportPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 2),
    _CfprMgmtCfgExportPolicyDn_Type()
)
cfprMgmtCfgExportPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyDn.setStatus("current")
_CfprMgmtCfgExportPolicyRn_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyRn_Object = MibTableColumn
cfprMgmtCfgExportPolicyRn = _CfprMgmtCfgExportPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 3),
    _CfprMgmtCfgExportPolicyRn_Type()
)
cfprMgmtCfgExportPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyRn.setStatus("current")
_CfprMgmtCfgExportPolicyAdminState_Type = CfprMgmtExportPolicyAdminState
_CfprMgmtCfgExportPolicyAdminState_Object = MibTableColumn
cfprMgmtCfgExportPolicyAdminState = _CfprMgmtCfgExportPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 4),
    _CfprMgmtCfgExportPolicyAdminState_Type()
)
cfprMgmtCfgExportPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyAdminState.setStatus("current")
_CfprMgmtCfgExportPolicyDescr_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyDescr_Object = MibTableColumn
cfprMgmtCfgExportPolicyDescr = _CfprMgmtCfgExportPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 5),
    _CfprMgmtCfgExportPolicyDescr_Type()
)
cfprMgmtCfgExportPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyDescr.setStatus("current")
_CfprMgmtCfgExportPolicyFsmDescr_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyFsmDescr_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmDescr = _CfprMgmtCfgExportPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 6),
    _CfprMgmtCfgExportPolicyFsmDescr_Type()
)
cfprMgmtCfgExportPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmDescr.setStatus("current")
_CfprMgmtCfgExportPolicyFsmPrev_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyFsmPrev_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmPrev = _CfprMgmtCfgExportPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 7),
    _CfprMgmtCfgExportPolicyFsmPrev_Type()
)
cfprMgmtCfgExportPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmPrev.setStatus("current")
_CfprMgmtCfgExportPolicyFsmProgr_Type = Gauge32
_CfprMgmtCfgExportPolicyFsmProgr_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmProgr = _CfprMgmtCfgExportPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 8),
    _CfprMgmtCfgExportPolicyFsmProgr_Type()
)
cfprMgmtCfgExportPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmProgr.setStatus("current")
_CfprMgmtCfgExportPolicyFsmRmtInvErrCode_Type = Gauge32
_CfprMgmtCfgExportPolicyFsmRmtInvErrCode_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmRmtInvErrCode = _CfprMgmtCfgExportPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 9),
    _CfprMgmtCfgExportPolicyFsmRmtInvErrCode_Type()
)
cfprMgmtCfgExportPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmRmtInvErrCode.setStatus("current")
_CfprMgmtCfgExportPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmRmtInvErrDescr = _CfprMgmtCfgExportPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 10),
    _CfprMgmtCfgExportPolicyFsmRmtInvErrDescr_Type()
)
cfprMgmtCfgExportPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmRmtInvErrDescr.setStatus("current")
_CfprMgmtCfgExportPolicyFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtCfgExportPolicyFsmRmtInvRslt_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmRmtInvRslt = _CfprMgmtCfgExportPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 11),
    _CfprMgmtCfgExportPolicyFsmRmtInvRslt_Type()
)
cfprMgmtCfgExportPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmRmtInvRslt.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStageDescr_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyFsmStageDescr_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmStageDescr = _CfprMgmtCfgExportPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 12),
    _CfprMgmtCfgExportPolicyFsmStageDescr_Type()
)
cfprMgmtCfgExportPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStageDescr.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStamp_Type = DateAndTime
_CfprMgmtCfgExportPolicyFsmStamp_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmStamp = _CfprMgmtCfgExportPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 13),
    _CfprMgmtCfgExportPolicyFsmStamp_Type()
)
cfprMgmtCfgExportPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStamp.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStatus_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyFsmStatus_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmStatus = _CfprMgmtCfgExportPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 14),
    _CfprMgmtCfgExportPolicyFsmStatus_Type()
)
cfprMgmtCfgExportPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStatus.setStatus("current")
_CfprMgmtCfgExportPolicyFsmTry_Type = Gauge32
_CfprMgmtCfgExportPolicyFsmTry_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmTry = _CfprMgmtCfgExportPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 15),
    _CfprMgmtCfgExportPolicyFsmTry_Type()
)
cfprMgmtCfgExportPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmTry.setStatus("current")
_CfprMgmtCfgExportPolicyHost_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyHost_Object = MibTableColumn
cfprMgmtCfgExportPolicyHost = _CfprMgmtCfgExportPolicyHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 16),
    _CfprMgmtCfgExportPolicyHost_Type()
)
cfprMgmtCfgExportPolicyHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyHost.setStatus("current")
_CfprMgmtCfgExportPolicyIntId_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyIntId_Object = MibTableColumn
cfprMgmtCfgExportPolicyIntId = _CfprMgmtCfgExportPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 17),
    _CfprMgmtCfgExportPolicyIntId_Type()
)
cfprMgmtCfgExportPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyIntId.setStatus("current")
_CfprMgmtCfgExportPolicyLastBackup_Type = DateAndTime
_CfprMgmtCfgExportPolicyLastBackup_Object = MibTableColumn
cfprMgmtCfgExportPolicyLastBackup = _CfprMgmtCfgExportPolicyLastBackup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 18),
    _CfprMgmtCfgExportPolicyLastBackup_Type()
)
cfprMgmtCfgExportPolicyLastBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyLastBackup.setStatus("current")
_CfprMgmtCfgExportPolicyMaxFiles_Type = Gauge32
_CfprMgmtCfgExportPolicyMaxFiles_Object = MibTableColumn
cfprMgmtCfgExportPolicyMaxFiles = _CfprMgmtCfgExportPolicyMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 19),
    _CfprMgmtCfgExportPolicyMaxFiles_Type()
)
cfprMgmtCfgExportPolicyMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyMaxFiles.setStatus("current")
_CfprMgmtCfgExportPolicyName_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyName_Object = MibTableColumn
cfprMgmtCfgExportPolicyName = _CfprMgmtCfgExportPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 20),
    _CfprMgmtCfgExportPolicyName_Type()
)
cfprMgmtCfgExportPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyName.setStatus("current")
_CfprMgmtCfgExportPolicyPolicyLevel_Type = Gauge32
_CfprMgmtCfgExportPolicyPolicyLevel_Object = MibTableColumn
cfprMgmtCfgExportPolicyPolicyLevel = _CfprMgmtCfgExportPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 21),
    _CfprMgmtCfgExportPolicyPolicyLevel_Type()
)
cfprMgmtCfgExportPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyPolicyLevel.setStatus("current")
_CfprMgmtCfgExportPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprMgmtCfgExportPolicyPolicyOwner_Object = MibTableColumn
cfprMgmtCfgExportPolicyPolicyOwner = _CfprMgmtCfgExportPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 22),
    _CfprMgmtCfgExportPolicyPolicyOwner_Type()
)
cfprMgmtCfgExportPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyPolicyOwner.setStatus("current")
_CfprMgmtCfgExportPolicyProto_Type = CfprMgmtExportPolicyProto
_CfprMgmtCfgExportPolicyProto_Object = MibTableColumn
cfprMgmtCfgExportPolicyProto = _CfprMgmtCfgExportPolicyProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 23),
    _CfprMgmtCfgExportPolicyProto_Type()
)
cfprMgmtCfgExportPolicyProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyProto.setStatus("current")
_CfprMgmtCfgExportPolicyPwd_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyPwd_Object = MibTableColumn
cfprMgmtCfgExportPolicyPwd = _CfprMgmtCfgExportPolicyPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 24),
    _CfprMgmtCfgExportPolicyPwd_Type()
)
cfprMgmtCfgExportPolicyPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyPwd.setStatus("current")
_CfprMgmtCfgExportPolicyRemoteFile_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyRemoteFile_Object = MibTableColumn
cfprMgmtCfgExportPolicyRemoteFile = _CfprMgmtCfgExportPolicyRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 25),
    _CfprMgmtCfgExportPolicyRemoteFile_Type()
)
cfprMgmtCfgExportPolicyRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyRemoteFile.setStatus("current")
_CfprMgmtCfgExportPolicySchedule_Type = CfprMgmtBackupInterval
_CfprMgmtCfgExportPolicySchedule_Object = MibTableColumn
cfprMgmtCfgExportPolicySchedule = _CfprMgmtCfgExportPolicySchedule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 26),
    _CfprMgmtCfgExportPolicySchedule_Type()
)
cfprMgmtCfgExportPolicySchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicySchedule.setStatus("current")
_CfprMgmtCfgExportPolicyUser_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyUser_Object = MibTableColumn
cfprMgmtCfgExportPolicyUser = _CfprMgmtCfgExportPolicyUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 27),
    _CfprMgmtCfgExportPolicyUser_Type()
)
cfprMgmtCfgExportPolicyUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyUser.setStatus("current")
_CfprMgmtCfgExportPolicyPort_Type = Gauge32
_CfprMgmtCfgExportPolicyPort_Object = MibTableColumn
cfprMgmtCfgExportPolicyPort = _CfprMgmtCfgExportPolicyPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 13, 1, 28),
    _CfprMgmtCfgExportPolicyPort_Type()
)
cfprMgmtCfgExportPolicyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyPort.setStatus("current")
_CfprMgmtCfgExportPolicyFsmTable_Object = MibTable
cfprMgmtCfgExportPolicyFsmTable = _CfprMgmtCfgExportPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14)
)
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmTable.setStatus("current")
_CfprMgmtCfgExportPolicyFsmEntry_Object = MibTableRow
cfprMgmtCfgExportPolicyFsmEntry = _CfprMgmtCfgExportPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14, 1)
)
cfprMgmtCfgExportPolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtCfgExportPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmEntry.setStatus("current")
_CfprMgmtCfgExportPolicyFsmInstanceId_Type = CfprManagedObjectId
_CfprMgmtCfgExportPolicyFsmInstanceId_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmInstanceId = _CfprMgmtCfgExportPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14, 1, 1),
    _CfprMgmtCfgExportPolicyFsmInstanceId_Type()
)
cfprMgmtCfgExportPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmInstanceId.setStatus("current")
_CfprMgmtCfgExportPolicyFsmDn_Type = CfprManagedObjectDn
_CfprMgmtCfgExportPolicyFsmDn_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmDn = _CfprMgmtCfgExportPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14, 1, 2),
    _CfprMgmtCfgExportPolicyFsmDn_Type()
)
cfprMgmtCfgExportPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmDn.setStatus("current")
_CfprMgmtCfgExportPolicyFsmRn_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyFsmRn_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmRn = _CfprMgmtCfgExportPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14, 1, 3),
    _CfprMgmtCfgExportPolicyFsmRn_Type()
)
cfprMgmtCfgExportPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmRn.setStatus("current")
_CfprMgmtCfgExportPolicyFsmCompletionTime_Type = DateAndTime
_CfprMgmtCfgExportPolicyFsmCompletionTime_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmCompletionTime = _CfprMgmtCfgExportPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14, 1, 4),
    _CfprMgmtCfgExportPolicyFsmCompletionTime_Type()
)
cfprMgmtCfgExportPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmCompletionTime.setStatus("current")
_CfprMgmtCfgExportPolicyFsmCurrentFsm_Type = CfprMgmtCfgExportPolicyFsmCurrentFsm
_CfprMgmtCfgExportPolicyFsmCurrentFsm_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmCurrentFsm = _CfprMgmtCfgExportPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14, 1, 5),
    _CfprMgmtCfgExportPolicyFsmCurrentFsm_Type()
)
cfprMgmtCfgExportPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmCurrentFsm.setStatus("current")
_CfprMgmtCfgExportPolicyFsmDescrData_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyFsmDescrData_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmDescrData = _CfprMgmtCfgExportPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14, 1, 6),
    _CfprMgmtCfgExportPolicyFsmDescrData_Type()
)
cfprMgmtCfgExportPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmDescrData.setStatus("current")
_CfprMgmtCfgExportPolicyFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtCfgExportPolicyFsmFsmStatus_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmFsmStatus = _CfprMgmtCfgExportPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14, 1, 7),
    _CfprMgmtCfgExportPolicyFsmFsmStatus_Type()
)
cfprMgmtCfgExportPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmFsmStatus.setStatus("current")
_CfprMgmtCfgExportPolicyFsmProgress_Type = Gauge32
_CfprMgmtCfgExportPolicyFsmProgress_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmProgress = _CfprMgmtCfgExportPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14, 1, 8),
    _CfprMgmtCfgExportPolicyFsmProgress_Type()
)
cfprMgmtCfgExportPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmProgress.setStatus("current")
_CfprMgmtCfgExportPolicyFsmRmtErrCode_Type = Gauge32
_CfprMgmtCfgExportPolicyFsmRmtErrCode_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmRmtErrCode = _CfprMgmtCfgExportPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14, 1, 9),
    _CfprMgmtCfgExportPolicyFsmRmtErrCode_Type()
)
cfprMgmtCfgExportPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmRmtErrCode.setStatus("current")
_CfprMgmtCfgExportPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyFsmRmtErrDescr_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmRmtErrDescr = _CfprMgmtCfgExportPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14, 1, 10),
    _CfprMgmtCfgExportPolicyFsmRmtErrDescr_Type()
)
cfprMgmtCfgExportPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmRmtErrDescr.setStatus("current")
_CfprMgmtCfgExportPolicyFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtCfgExportPolicyFsmRmtRslt_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmRmtRslt = _CfprMgmtCfgExportPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 14, 1, 11),
    _CfprMgmtCfgExportPolicyFsmRmtRslt_Type()
)
cfprMgmtCfgExportPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmRmtRslt.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStageTable_Object = MibTable
cfprMgmtCfgExportPolicyFsmStageTable = _CfprMgmtCfgExportPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 15)
)
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStageTable.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStageEntry_Object = MibTableRow
cfprMgmtCfgExportPolicyFsmStageEntry = _CfprMgmtCfgExportPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 15, 1)
)
cfprMgmtCfgExportPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtCfgExportPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStageEntry.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStageInstanceId_Type = CfprManagedObjectId
_CfprMgmtCfgExportPolicyFsmStageInstanceId_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmStageInstanceId = _CfprMgmtCfgExportPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 15, 1, 1),
    _CfprMgmtCfgExportPolicyFsmStageInstanceId_Type()
)
cfprMgmtCfgExportPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStageInstanceId.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStageDn_Type = CfprManagedObjectDn
_CfprMgmtCfgExportPolicyFsmStageDn_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmStageDn = _CfprMgmtCfgExportPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 15, 1, 2),
    _CfprMgmtCfgExportPolicyFsmStageDn_Type()
)
cfprMgmtCfgExportPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStageDn.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStageRn_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyFsmStageRn_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmStageRn = _CfprMgmtCfgExportPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 15, 1, 3),
    _CfprMgmtCfgExportPolicyFsmStageRn_Type()
)
cfprMgmtCfgExportPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStageRn.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStageDescrData_Type = SnmpAdminString
_CfprMgmtCfgExportPolicyFsmStageDescrData_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmStageDescrData = _CfprMgmtCfgExportPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 15, 1, 4),
    _CfprMgmtCfgExportPolicyFsmStageDescrData_Type()
)
cfprMgmtCfgExportPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStageDescrData.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprMgmtCfgExportPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmStageLastUpdateTime = _CfprMgmtCfgExportPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 15, 1, 5),
    _CfprMgmtCfgExportPolicyFsmStageLastUpdateTime_Type()
)
cfprMgmtCfgExportPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStageLastUpdateTime.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStageName_Type = CfprMgmtCfgExportPolicyFsmStageName
_CfprMgmtCfgExportPolicyFsmStageName_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmStageName = _CfprMgmtCfgExportPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 15, 1, 6),
    _CfprMgmtCfgExportPolicyFsmStageName_Type()
)
cfprMgmtCfgExportPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStageName.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStageOrder_Type = Gauge32
_CfprMgmtCfgExportPolicyFsmStageOrder_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmStageOrder = _CfprMgmtCfgExportPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 15, 1, 7),
    _CfprMgmtCfgExportPolicyFsmStageOrder_Type()
)
cfprMgmtCfgExportPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStageOrder.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStageRetry_Type = Gauge32
_CfprMgmtCfgExportPolicyFsmStageRetry_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmStageRetry = _CfprMgmtCfgExportPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 15, 1, 8),
    _CfprMgmtCfgExportPolicyFsmStageRetry_Type()
)
cfprMgmtCfgExportPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStageRetry.setStatus("current")
_CfprMgmtCfgExportPolicyFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtCfgExportPolicyFsmStageStageStatus_Object = MibTableColumn
cfprMgmtCfgExportPolicyFsmStageStageStatus = _CfprMgmtCfgExportPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 15, 1, 9),
    _CfprMgmtCfgExportPolicyFsmStageStageStatus_Type()
)
cfprMgmtCfgExportPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCfgExportPolicyFsmStageStageStatus.setStatus("current")
_CfprMgmtCimcSecureBootTable_Object = MibTable
cfprMgmtCimcSecureBootTable = _CfprMgmtCimcSecureBootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 16)
)
if mibBuilder.loadTexts:
    cfprMgmtCimcSecureBootTable.setStatus("current")
_CfprMgmtCimcSecureBootEntry_Object = MibTableRow
cfprMgmtCimcSecureBootEntry = _CfprMgmtCimcSecureBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 16, 1)
)
cfprMgmtCimcSecureBootEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtCimcSecureBootInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtCimcSecureBootEntry.setStatus("current")
_CfprMgmtCimcSecureBootInstanceId_Type = CfprManagedObjectId
_CfprMgmtCimcSecureBootInstanceId_Object = MibTableColumn
cfprMgmtCimcSecureBootInstanceId = _CfprMgmtCimcSecureBootInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 16, 1, 1),
    _CfprMgmtCimcSecureBootInstanceId_Type()
)
cfprMgmtCimcSecureBootInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtCimcSecureBootInstanceId.setStatus("current")
_CfprMgmtCimcSecureBootDn_Type = CfprManagedObjectDn
_CfprMgmtCimcSecureBootDn_Object = MibTableColumn
cfprMgmtCimcSecureBootDn = _CfprMgmtCimcSecureBootDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 16, 1, 2),
    _CfprMgmtCimcSecureBootDn_Type()
)
cfprMgmtCimcSecureBootDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCimcSecureBootDn.setStatus("current")
_CfprMgmtCimcSecureBootRn_Type = SnmpAdminString
_CfprMgmtCimcSecureBootRn_Object = MibTableColumn
cfprMgmtCimcSecureBootRn = _CfprMgmtCimcSecureBootRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 16, 1, 3),
    _CfprMgmtCimcSecureBootRn_Type()
)
cfprMgmtCimcSecureBootRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCimcSecureBootRn.setStatus("current")
_CfprMgmtCimcSecureBootAdminState_Type = CfprMgmtCimcSecureBootAdminState
_CfprMgmtCimcSecureBootAdminState_Object = MibTableColumn
cfprMgmtCimcSecureBootAdminState = _CfprMgmtCimcSecureBootAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 16, 1, 4),
    _CfprMgmtCimcSecureBootAdminState_Type()
)
cfprMgmtCimcSecureBootAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCimcSecureBootAdminState.setStatus("current")
_CfprMgmtCimcSecureBootOperState_Type = CfprMgmtSecureBootOperState
_CfprMgmtCimcSecureBootOperState_Object = MibTableColumn
cfprMgmtCimcSecureBootOperState = _CfprMgmtCimcSecureBootOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 16, 1, 5),
    _CfprMgmtCimcSecureBootOperState_Type()
)
cfprMgmtCimcSecureBootOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtCimcSecureBootOperState.setStatus("current")
_CfprMgmtConnectionTable_Object = MibTable
cfprMgmtConnectionTable = _CfprMgmtConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 17)
)
if mibBuilder.loadTexts:
    cfprMgmtConnectionTable.setStatus("current")
_CfprMgmtConnectionEntry_Object = MibTableRow
cfprMgmtConnectionEntry = _CfprMgmtConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 17, 1)
)
cfprMgmtConnectionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtConnectionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtConnectionEntry.setStatus("current")
_CfprMgmtConnectionInstanceId_Type = CfprManagedObjectId
_CfprMgmtConnectionInstanceId_Object = MibTableColumn
cfprMgmtConnectionInstanceId = _CfprMgmtConnectionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 17, 1, 1),
    _CfprMgmtConnectionInstanceId_Type()
)
cfprMgmtConnectionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtConnectionInstanceId.setStatus("current")
_CfprMgmtConnectionDn_Type = CfprManagedObjectDn
_CfprMgmtConnectionDn_Object = MibTableColumn
cfprMgmtConnectionDn = _CfprMgmtConnectionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 17, 1, 2),
    _CfprMgmtConnectionDn_Type()
)
cfprMgmtConnectionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtConnectionDn.setStatus("current")
_CfprMgmtConnectionRn_Type = SnmpAdminString
_CfprMgmtConnectionRn_Object = MibTableColumn
cfprMgmtConnectionRn = _CfprMgmtConnectionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 17, 1, 3),
    _CfprMgmtConnectionRn_Type()
)
cfprMgmtConnectionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtConnectionRn.setStatus("current")
_CfprMgmtConnectionAck_Type = CfprMgmtConnectionState
_CfprMgmtConnectionAck_Object = MibTableColumn
cfprMgmtConnectionAck = _CfprMgmtConnectionAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 17, 1, 4),
    _CfprMgmtConnectionAck_Type()
)
cfprMgmtConnectionAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtConnectionAck.setStatus("current")
_CfprMgmtConnectionOperState_Type = CfprMgmtConnectionState
_CfprMgmtConnectionOperState_Object = MibTableColumn
cfprMgmtConnectionOperState = _CfprMgmtConnectionOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 17, 1, 5),
    _CfprMgmtConnectionOperState_Type()
)
cfprMgmtConnectionOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtConnectionOperState.setStatus("current")
_CfprMgmtConnectionType_Type = CfprMgmtSource
_CfprMgmtConnectionType_Object = MibTableColumn
cfprMgmtConnectionType = _CfprMgmtConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 17, 1, 6),
    _CfprMgmtConnectionType_Type()
)
cfprMgmtConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtConnectionType.setStatus("current")
_CfprMgmtControllerTable_Object = MibTable
cfprMgmtControllerTable = _CfprMgmtControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18)
)
if mibBuilder.loadTexts:
    cfprMgmtControllerTable.setStatus("current")
_CfprMgmtControllerEntry_Object = MibTableRow
cfprMgmtControllerEntry = _CfprMgmtControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1)
)
cfprMgmtControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtControllerEntry.setStatus("current")
_CfprMgmtControllerInstanceId_Type = CfprManagedObjectId
_CfprMgmtControllerInstanceId_Object = MibTableColumn
cfprMgmtControllerInstanceId = _CfprMgmtControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 1),
    _CfprMgmtControllerInstanceId_Type()
)
cfprMgmtControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtControllerInstanceId.setStatus("current")
_CfprMgmtControllerDn_Type = CfprManagedObjectDn
_CfprMgmtControllerDn_Object = MibTableColumn
cfprMgmtControllerDn = _CfprMgmtControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 2),
    _CfprMgmtControllerDn_Type()
)
cfprMgmtControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerDn.setStatus("current")
_CfprMgmtControllerRn_Type = SnmpAdminString
_CfprMgmtControllerRn_Object = MibTableColumn
cfprMgmtControllerRn = _CfprMgmtControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 3),
    _CfprMgmtControllerRn_Type()
)
cfprMgmtControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerRn.setStatus("current")
_CfprMgmtControllerDimmBlacklistingOperState_Type = CfprMgmtDimmBlacklistingOperState
_CfprMgmtControllerDimmBlacklistingOperState_Object = MibTableColumn
cfprMgmtControllerDimmBlacklistingOperState = _CfprMgmtControllerDimmBlacklistingOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 4),
    _CfprMgmtControllerDimmBlacklistingOperState_Type()
)
cfprMgmtControllerDimmBlacklistingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerDimmBlacklistingOperState.setStatus("current")
_CfprMgmtControllerFsmDescr_Type = SnmpAdminString
_CfprMgmtControllerFsmDescr_Object = MibTableColumn
cfprMgmtControllerFsmDescr = _CfprMgmtControllerFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 5),
    _CfprMgmtControllerFsmDescr_Type()
)
cfprMgmtControllerFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmDescr.setStatus("current")
_CfprMgmtControllerFsmFlags_Type = SnmpAdminString
_CfprMgmtControllerFsmFlags_Object = MibTableColumn
cfprMgmtControllerFsmFlags = _CfprMgmtControllerFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 6),
    _CfprMgmtControllerFsmFlags_Type()
)
cfprMgmtControllerFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmFlags.setStatus("current")
_CfprMgmtControllerFsmPrev_Type = SnmpAdminString
_CfprMgmtControllerFsmPrev_Object = MibTableColumn
cfprMgmtControllerFsmPrev = _CfprMgmtControllerFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 7),
    _CfprMgmtControllerFsmPrev_Type()
)
cfprMgmtControllerFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmPrev.setStatus("current")
_CfprMgmtControllerFsmProgr_Type = Gauge32
_CfprMgmtControllerFsmProgr_Object = MibTableColumn
cfprMgmtControllerFsmProgr = _CfprMgmtControllerFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 8),
    _CfprMgmtControllerFsmProgr_Type()
)
cfprMgmtControllerFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmProgr.setStatus("current")
_CfprMgmtControllerFsmRmtInvErrCode_Type = Gauge32
_CfprMgmtControllerFsmRmtInvErrCode_Object = MibTableColumn
cfprMgmtControllerFsmRmtInvErrCode = _CfprMgmtControllerFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 9),
    _CfprMgmtControllerFsmRmtInvErrCode_Type()
)
cfprMgmtControllerFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmRmtInvErrCode.setStatus("current")
_CfprMgmtControllerFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprMgmtControllerFsmRmtInvErrDescr_Object = MibTableColumn
cfprMgmtControllerFsmRmtInvErrDescr = _CfprMgmtControllerFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 10),
    _CfprMgmtControllerFsmRmtInvErrDescr_Type()
)
cfprMgmtControllerFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmRmtInvErrDescr.setStatus("current")
_CfprMgmtControllerFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtControllerFsmRmtInvRslt_Object = MibTableColumn
cfprMgmtControllerFsmRmtInvRslt = _CfprMgmtControllerFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 11),
    _CfprMgmtControllerFsmRmtInvRslt_Type()
)
cfprMgmtControllerFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmRmtInvRslt.setStatus("current")
_CfprMgmtControllerFsmStageDescr_Type = SnmpAdminString
_CfprMgmtControllerFsmStageDescr_Object = MibTableColumn
cfprMgmtControllerFsmStageDescr = _CfprMgmtControllerFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 12),
    _CfprMgmtControllerFsmStageDescr_Type()
)
cfprMgmtControllerFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStageDescr.setStatus("current")
_CfprMgmtControllerFsmStamp_Type = DateAndTime
_CfprMgmtControllerFsmStamp_Object = MibTableColumn
cfprMgmtControllerFsmStamp = _CfprMgmtControllerFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 13),
    _CfprMgmtControllerFsmStamp_Type()
)
cfprMgmtControllerFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStamp.setStatus("current")
_CfprMgmtControllerFsmStatus_Type = SnmpAdminString
_CfprMgmtControllerFsmStatus_Object = MibTableColumn
cfprMgmtControllerFsmStatus = _CfprMgmtControllerFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 14),
    _CfprMgmtControllerFsmStatus_Type()
)
cfprMgmtControllerFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStatus.setStatus("current")
_CfprMgmtControllerFsmTry_Type = Gauge32
_CfprMgmtControllerFsmTry_Object = MibTableColumn
cfprMgmtControllerFsmTry = _CfprMgmtControllerFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 15),
    _CfprMgmtControllerFsmTry_Type()
)
cfprMgmtControllerFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmTry.setStatus("current")
_CfprMgmtControllerGuid_Type = SnmpAdminString
_CfprMgmtControllerGuid_Object = MibTableColumn
cfprMgmtControllerGuid = _CfprMgmtControllerGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 16),
    _CfprMgmtControllerGuid_Type()
)
cfprMgmtControllerGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerGuid.setStatus("current")
_CfprMgmtControllerModel_Type = SnmpAdminString
_CfprMgmtControllerModel_Object = MibTableColumn
cfprMgmtControllerModel = _CfprMgmtControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 17),
    _CfprMgmtControllerModel_Type()
)
cfprMgmtControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerModel.setStatus("current")
_CfprMgmtControllerOperConn_Type = SnmpAdminString
_CfprMgmtControllerOperConn_Object = MibTableColumn
cfprMgmtControllerOperConn = _CfprMgmtControllerOperConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 18),
    _CfprMgmtControllerOperConn_Type()
)
cfprMgmtControllerOperConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerOperConn.setStatus("current")
_CfprMgmtControllerRevision_Type = SnmpAdminString
_CfprMgmtControllerRevision_Object = MibTableColumn
cfprMgmtControllerRevision = _CfprMgmtControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 19),
    _CfprMgmtControllerRevision_Type()
)
cfprMgmtControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerRevision.setStatus("current")
_CfprMgmtControllerSerial_Type = SnmpAdminString
_CfprMgmtControllerSerial_Object = MibTableColumn
cfprMgmtControllerSerial = _CfprMgmtControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 20),
    _CfprMgmtControllerSerial_Type()
)
cfprMgmtControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerSerial.setStatus("current")
_CfprMgmtControllerStorageOobInterfaceSupported_Type = TruthValue
_CfprMgmtControllerStorageOobInterfaceSupported_Object = MibTableColumn
cfprMgmtControllerStorageOobInterfaceSupported = _CfprMgmtControllerStorageOobInterfaceSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 21),
    _CfprMgmtControllerStorageOobInterfaceSupported_Type()
)
cfprMgmtControllerStorageOobInterfaceSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerStorageOobInterfaceSupported.setStatus("current")
_CfprMgmtControllerStorageSubsystemState_Type = CfprMgmtStorageSubsystemState
_CfprMgmtControllerStorageSubsystemState_Object = MibTableColumn
cfprMgmtControllerStorageSubsystemState = _CfprMgmtControllerStorageSubsystemState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 22),
    _CfprMgmtControllerStorageSubsystemState_Type()
)
cfprMgmtControllerStorageSubsystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerStorageSubsystemState.setStatus("current")
_CfprMgmtControllerSubject_Type = CfprMgmtSubject
_CfprMgmtControllerSubject_Object = MibTableColumn
cfprMgmtControllerSubject = _CfprMgmtControllerSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 23),
    _CfprMgmtControllerSubject_Type()
)
cfprMgmtControllerSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerSubject.setStatus("current")
_CfprMgmtControllerVendor_Type = SnmpAdminString
_CfprMgmtControllerVendor_Object = MibTableColumn
cfprMgmtControllerVendor = _CfprMgmtControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 18, 1, 24),
    _CfprMgmtControllerVendor_Type()
)
cfprMgmtControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerVendor.setStatus("current")
_CfprMgmtControllerFsmTable_Object = MibTable
cfprMgmtControllerFsmTable = _CfprMgmtControllerFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19)
)
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmTable.setStatus("current")
_CfprMgmtControllerFsmEntry_Object = MibTableRow
cfprMgmtControllerFsmEntry = _CfprMgmtControllerFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19, 1)
)
cfprMgmtControllerFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtControllerFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmEntry.setStatus("current")
_CfprMgmtControllerFsmInstanceId_Type = CfprManagedObjectId
_CfprMgmtControllerFsmInstanceId_Object = MibTableColumn
cfprMgmtControllerFsmInstanceId = _CfprMgmtControllerFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19, 1, 1),
    _CfprMgmtControllerFsmInstanceId_Type()
)
cfprMgmtControllerFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmInstanceId.setStatus("current")
_CfprMgmtControllerFsmDn_Type = CfprManagedObjectDn
_CfprMgmtControllerFsmDn_Object = MibTableColumn
cfprMgmtControllerFsmDn = _CfprMgmtControllerFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19, 1, 2),
    _CfprMgmtControllerFsmDn_Type()
)
cfprMgmtControllerFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmDn.setStatus("current")
_CfprMgmtControllerFsmRn_Type = SnmpAdminString
_CfprMgmtControllerFsmRn_Object = MibTableColumn
cfprMgmtControllerFsmRn = _CfprMgmtControllerFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19, 1, 3),
    _CfprMgmtControllerFsmRn_Type()
)
cfprMgmtControllerFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmRn.setStatus("current")
_CfprMgmtControllerFsmCompletionTime_Type = DateAndTime
_CfprMgmtControllerFsmCompletionTime_Object = MibTableColumn
cfprMgmtControllerFsmCompletionTime = _CfprMgmtControllerFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19, 1, 4),
    _CfprMgmtControllerFsmCompletionTime_Type()
)
cfprMgmtControllerFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmCompletionTime.setStatus("current")
_CfprMgmtControllerFsmCurrentFsm_Type = CfprMgmtControllerFsmCurrentFsm
_CfprMgmtControllerFsmCurrentFsm_Object = MibTableColumn
cfprMgmtControllerFsmCurrentFsm = _CfprMgmtControllerFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19, 1, 5),
    _CfprMgmtControllerFsmCurrentFsm_Type()
)
cfprMgmtControllerFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmCurrentFsm.setStatus("current")
_CfprMgmtControllerFsmDescrData_Type = SnmpAdminString
_CfprMgmtControllerFsmDescrData_Object = MibTableColumn
cfprMgmtControllerFsmDescrData = _CfprMgmtControllerFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19, 1, 6),
    _CfprMgmtControllerFsmDescrData_Type()
)
cfprMgmtControllerFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmDescrData.setStatus("current")
_CfprMgmtControllerFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtControllerFsmFsmStatus_Object = MibTableColumn
cfprMgmtControllerFsmFsmStatus = _CfprMgmtControllerFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19, 1, 7),
    _CfprMgmtControllerFsmFsmStatus_Type()
)
cfprMgmtControllerFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmFsmStatus.setStatus("current")
_CfprMgmtControllerFsmProgress_Type = Gauge32
_CfprMgmtControllerFsmProgress_Object = MibTableColumn
cfprMgmtControllerFsmProgress = _CfprMgmtControllerFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19, 1, 8),
    _CfprMgmtControllerFsmProgress_Type()
)
cfprMgmtControllerFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmProgress.setStatus("current")
_CfprMgmtControllerFsmRmtErrCode_Type = Gauge32
_CfprMgmtControllerFsmRmtErrCode_Object = MibTableColumn
cfprMgmtControllerFsmRmtErrCode = _CfprMgmtControllerFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19, 1, 9),
    _CfprMgmtControllerFsmRmtErrCode_Type()
)
cfprMgmtControllerFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmRmtErrCode.setStatus("current")
_CfprMgmtControllerFsmRmtErrDescr_Type = SnmpAdminString
_CfprMgmtControllerFsmRmtErrDescr_Object = MibTableColumn
cfprMgmtControllerFsmRmtErrDescr = _CfprMgmtControllerFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19, 1, 10),
    _CfprMgmtControllerFsmRmtErrDescr_Type()
)
cfprMgmtControllerFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmRmtErrDescr.setStatus("current")
_CfprMgmtControllerFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtControllerFsmRmtRslt_Object = MibTableColumn
cfprMgmtControllerFsmRmtRslt = _CfprMgmtControllerFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 19, 1, 11),
    _CfprMgmtControllerFsmRmtRslt_Type()
)
cfprMgmtControllerFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmRmtRslt.setStatus("current")
_CfprMgmtControllerFsmStageTable_Object = MibTable
cfprMgmtControllerFsmStageTable = _CfprMgmtControllerFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 20)
)
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStageTable.setStatus("current")
_CfprMgmtControllerFsmStageEntry_Object = MibTableRow
cfprMgmtControllerFsmStageEntry = _CfprMgmtControllerFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 20, 1)
)
cfprMgmtControllerFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtControllerFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStageEntry.setStatus("current")
_CfprMgmtControllerFsmStageInstanceId_Type = CfprManagedObjectId
_CfprMgmtControllerFsmStageInstanceId_Object = MibTableColumn
cfprMgmtControllerFsmStageInstanceId = _CfprMgmtControllerFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 20, 1, 1),
    _CfprMgmtControllerFsmStageInstanceId_Type()
)
cfprMgmtControllerFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStageInstanceId.setStatus("current")
_CfprMgmtControllerFsmStageDn_Type = CfprManagedObjectDn
_CfprMgmtControllerFsmStageDn_Object = MibTableColumn
cfprMgmtControllerFsmStageDn = _CfprMgmtControllerFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 20, 1, 2),
    _CfprMgmtControllerFsmStageDn_Type()
)
cfprMgmtControllerFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStageDn.setStatus("current")
_CfprMgmtControllerFsmStageRn_Type = SnmpAdminString
_CfprMgmtControllerFsmStageRn_Object = MibTableColumn
cfprMgmtControllerFsmStageRn = _CfprMgmtControllerFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 20, 1, 3),
    _CfprMgmtControllerFsmStageRn_Type()
)
cfprMgmtControllerFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStageRn.setStatus("current")
_CfprMgmtControllerFsmStageDescrData_Type = SnmpAdminString
_CfprMgmtControllerFsmStageDescrData_Object = MibTableColumn
cfprMgmtControllerFsmStageDescrData = _CfprMgmtControllerFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 20, 1, 4),
    _CfprMgmtControllerFsmStageDescrData_Type()
)
cfprMgmtControllerFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStageDescrData.setStatus("current")
_CfprMgmtControllerFsmStageLastUpdateTime_Type = DateAndTime
_CfprMgmtControllerFsmStageLastUpdateTime_Object = MibTableColumn
cfprMgmtControllerFsmStageLastUpdateTime = _CfprMgmtControllerFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 20, 1, 5),
    _CfprMgmtControllerFsmStageLastUpdateTime_Type()
)
cfprMgmtControllerFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStageLastUpdateTime.setStatus("current")
_CfprMgmtControllerFsmStageName_Type = CfprMgmtControllerFsmStageName
_CfprMgmtControllerFsmStageName_Object = MibTableColumn
cfprMgmtControllerFsmStageName = _CfprMgmtControllerFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 20, 1, 6),
    _CfprMgmtControllerFsmStageName_Type()
)
cfprMgmtControllerFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStageName.setStatus("current")
_CfprMgmtControllerFsmStageOrder_Type = Gauge32
_CfprMgmtControllerFsmStageOrder_Object = MibTableColumn
cfprMgmtControllerFsmStageOrder = _CfprMgmtControllerFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 20, 1, 7),
    _CfprMgmtControllerFsmStageOrder_Type()
)
cfprMgmtControllerFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStageOrder.setStatus("current")
_CfprMgmtControllerFsmStageRetry_Type = Gauge32
_CfprMgmtControllerFsmStageRetry_Object = MibTableColumn
cfprMgmtControllerFsmStageRetry = _CfprMgmtControllerFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 20, 1, 8),
    _CfprMgmtControllerFsmStageRetry_Type()
)
cfprMgmtControllerFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStageRetry.setStatus("current")
_CfprMgmtControllerFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtControllerFsmStageStageStatus_Object = MibTableColumn
cfprMgmtControllerFsmStageStageStatus = _CfprMgmtControllerFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 20, 1, 9),
    _CfprMgmtControllerFsmStageStageStatus_Type()
)
cfprMgmtControllerFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmStageStageStatus.setStatus("current")
_CfprMgmtControllerFsmTaskTable_Object = MibTable
cfprMgmtControllerFsmTaskTable = _CfprMgmtControllerFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 21)
)
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmTaskTable.setStatus("current")
_CfprMgmtControllerFsmTaskEntry_Object = MibTableRow
cfprMgmtControllerFsmTaskEntry = _CfprMgmtControllerFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 21, 1)
)
cfprMgmtControllerFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtControllerFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmTaskEntry.setStatus("current")
_CfprMgmtControllerFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprMgmtControllerFsmTaskInstanceId_Object = MibTableColumn
cfprMgmtControllerFsmTaskInstanceId = _CfprMgmtControllerFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 21, 1, 1),
    _CfprMgmtControllerFsmTaskInstanceId_Type()
)
cfprMgmtControllerFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmTaskInstanceId.setStatus("current")
_CfprMgmtControllerFsmTaskDn_Type = CfprManagedObjectDn
_CfprMgmtControllerFsmTaskDn_Object = MibTableColumn
cfprMgmtControllerFsmTaskDn = _CfprMgmtControllerFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 21, 1, 2),
    _CfprMgmtControllerFsmTaskDn_Type()
)
cfprMgmtControllerFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmTaskDn.setStatus("current")
_CfprMgmtControllerFsmTaskRn_Type = SnmpAdminString
_CfprMgmtControllerFsmTaskRn_Object = MibTableColumn
cfprMgmtControllerFsmTaskRn = _CfprMgmtControllerFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 21, 1, 3),
    _CfprMgmtControllerFsmTaskRn_Type()
)
cfprMgmtControllerFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmTaskRn.setStatus("current")
_CfprMgmtControllerFsmTaskCompletion_Type = CfprFsmCompletion
_CfprMgmtControllerFsmTaskCompletion_Object = MibTableColumn
cfprMgmtControllerFsmTaskCompletion = _CfprMgmtControllerFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 21, 1, 4),
    _CfprMgmtControllerFsmTaskCompletion_Type()
)
cfprMgmtControllerFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmTaskCompletion.setStatus("current")
_CfprMgmtControllerFsmTaskFlags_Type = CfprMgmtControllerFsmTaskFlags
_CfprMgmtControllerFsmTaskFlags_Object = MibTableColumn
cfprMgmtControllerFsmTaskFlags = _CfprMgmtControllerFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 21, 1, 5),
    _CfprMgmtControllerFsmTaskFlags_Type()
)
cfprMgmtControllerFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmTaskFlags.setStatus("current")
_CfprMgmtControllerFsmTaskItem_Type = CfprMgmtControllerFsmTaskItem
_CfprMgmtControllerFsmTaskItem_Object = MibTableColumn
cfprMgmtControllerFsmTaskItem = _CfprMgmtControllerFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 21, 1, 6),
    _CfprMgmtControllerFsmTaskItem_Type()
)
cfprMgmtControllerFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmTaskItem.setStatus("current")
_CfprMgmtControllerFsmTaskSeqId_Type = Gauge32
_CfprMgmtControllerFsmTaskSeqId_Object = MibTableColumn
cfprMgmtControllerFsmTaskSeqId = _CfprMgmtControllerFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 21, 1, 7),
    _CfprMgmtControllerFsmTaskSeqId_Type()
)
cfprMgmtControllerFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtControllerFsmTaskSeqId.setStatus("current")
_CfprMgmtEntityTable_Object = MibTable
cfprMgmtEntityTable = _CfprMgmtEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22)
)
if mibBuilder.loadTexts:
    cfprMgmtEntityTable.setStatus("current")
_CfprMgmtEntityEntry_Object = MibTableRow
cfprMgmtEntityEntry = _CfprMgmtEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1)
)
cfprMgmtEntityEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtEntityInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtEntityEntry.setStatus("current")
_CfprMgmtEntityInstanceId_Type = CfprManagedObjectId
_CfprMgmtEntityInstanceId_Object = MibTableColumn
cfprMgmtEntityInstanceId = _CfprMgmtEntityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 1),
    _CfprMgmtEntityInstanceId_Type()
)
cfprMgmtEntityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtEntityInstanceId.setStatus("current")
_CfprMgmtEntityDn_Type = CfprManagedObjectDn
_CfprMgmtEntityDn_Object = MibTableColumn
cfprMgmtEntityDn = _CfprMgmtEntityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 2),
    _CfprMgmtEntityDn_Type()
)
cfprMgmtEntityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityDn.setStatus("current")
_CfprMgmtEntityRn_Type = SnmpAdminString
_CfprMgmtEntityRn_Object = MibTableColumn
cfprMgmtEntityRn = _CfprMgmtEntityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 3),
    _CfprMgmtEntityRn_Type()
)
cfprMgmtEntityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityRn.setStatus("current")
_CfprMgmtEntityChassis1_Type = SnmpAdminString
_CfprMgmtEntityChassis1_Object = MibTableColumn
cfprMgmtEntityChassis1 = _CfprMgmtEntityChassis1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 4),
    _CfprMgmtEntityChassis1_Type()
)
cfprMgmtEntityChassis1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityChassis1.setStatus("current")
_CfprMgmtEntityChassis2_Type = SnmpAdminString
_CfprMgmtEntityChassis2_Object = MibTableColumn
cfprMgmtEntityChassis2 = _CfprMgmtEntityChassis2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 5),
    _CfprMgmtEntityChassis2_Type()
)
cfprMgmtEntityChassis2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityChassis2.setStatus("current")
_CfprMgmtEntityChassis3_Type = SnmpAdminString
_CfprMgmtEntityChassis3_Object = MibTableColumn
cfprMgmtEntityChassis3 = _CfprMgmtEntityChassis3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 6),
    _CfprMgmtEntityChassis3_Type()
)
cfprMgmtEntityChassis3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityChassis3.setStatus("current")
_CfprMgmtEntityChassisDeviceIoState1_Type = CfprMgmtEntityChassisDeviceIoState1
_CfprMgmtEntityChassisDeviceIoState1_Object = MibTableColumn
cfprMgmtEntityChassisDeviceIoState1 = _CfprMgmtEntityChassisDeviceIoState1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 7),
    _CfprMgmtEntityChassisDeviceIoState1_Type()
)
cfprMgmtEntityChassisDeviceIoState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityChassisDeviceIoState1.setStatus("current")
_CfprMgmtEntityChassisDeviceIoState2_Type = CfprMgmtEntityChassisDeviceIoState2
_CfprMgmtEntityChassisDeviceIoState2_Object = MibTableColumn
cfprMgmtEntityChassisDeviceIoState2 = _CfprMgmtEntityChassisDeviceIoState2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 8),
    _CfprMgmtEntityChassisDeviceIoState2_Type()
)
cfprMgmtEntityChassisDeviceIoState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityChassisDeviceIoState2.setStatus("current")
_CfprMgmtEntityChassisDeviceIoState3_Type = CfprMgmtEntityChassisDeviceIoState3
_CfprMgmtEntityChassisDeviceIoState3_Object = MibTableColumn
cfprMgmtEntityChassisDeviceIoState3 = _CfprMgmtEntityChassisDeviceIoState3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 9),
    _CfprMgmtEntityChassisDeviceIoState3_Type()
)
cfprMgmtEntityChassisDeviceIoState3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityChassisDeviceIoState3.setStatus("current")
_CfprMgmtEntityHaFailureReason_Type = CfprMgmtEntityHaFailureReason
_CfprMgmtEntityHaFailureReason_Object = MibTableColumn
cfprMgmtEntityHaFailureReason = _CfprMgmtEntityHaFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 10),
    _CfprMgmtEntityHaFailureReason_Type()
)
cfprMgmtEntityHaFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityHaFailureReason.setStatus("current")
_CfprMgmtEntityHaReadiness_Type = CfprMgmtEntityHaReadiness
_CfprMgmtEntityHaReadiness_Object = MibTableColumn
cfprMgmtEntityHaReadiness = _CfprMgmtEntityHaReadiness_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 11),
    _CfprMgmtEntityHaReadiness_Type()
)
cfprMgmtEntityHaReadiness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityHaReadiness.setStatus("current")
_CfprMgmtEntityHaReady_Type = TruthValue
_CfprMgmtEntityHaReady_Object = MibTableColumn
cfprMgmtEntityHaReady = _CfprMgmtEntityHaReady_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 12),
    _CfprMgmtEntityHaReady_Type()
)
cfprMgmtEntityHaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityHaReady.setStatus("current")
_CfprMgmtEntityId_Type = CfprNetworkSwitchId
_CfprMgmtEntityId_Object = MibTableColumn
cfprMgmtEntityId = _CfprMgmtEntityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 13),
    _CfprMgmtEntityId_Type()
)
cfprMgmtEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityId.setStatus("current")
_CfprMgmtEntityLeadership_Type = CfprMgmtEntityLeadership
_CfprMgmtEntityLeadership_Object = MibTableColumn
cfprMgmtEntityLeadership = _CfprMgmtEntityLeadership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 14),
    _CfprMgmtEntityLeadership_Type()
)
cfprMgmtEntityLeadership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityLeadership.setStatus("current")
_CfprMgmtEntityMgmtServicesState_Type = CfprMgmtEntityMgmtServicesState
_CfprMgmtEntityMgmtServicesState_Object = MibTableColumn
cfprMgmtEntityMgmtServicesState = _CfprMgmtEntityMgmtServicesState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 15),
    _CfprMgmtEntityMgmtServicesState_Type()
)
cfprMgmtEntityMgmtServicesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityMgmtServicesState.setStatus("current")
_CfprMgmtEntityProblems_Type = CfprMgmtEntityProblems
_CfprMgmtEntityProblems_Object = MibTableColumn
cfprMgmtEntityProblems = _CfprMgmtEntityProblems_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 16),
    _CfprMgmtEntityProblems_Type()
)
cfprMgmtEntityProblems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityProblems.setStatus("current")
_CfprMgmtEntitySshAuthKeysCsum_Type = SnmpAdminString
_CfprMgmtEntitySshAuthKeysCsum_Object = MibTableColumn
cfprMgmtEntitySshAuthKeysCsum = _CfprMgmtEntitySshAuthKeysCsum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 17),
    _CfprMgmtEntitySshAuthKeysCsum_Type()
)
cfprMgmtEntitySshAuthKeysCsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntitySshAuthKeysCsum.setStatus("current")
_CfprMgmtEntitySshAuthKeysSize_Type = Unsigned64
_CfprMgmtEntitySshAuthKeysSize_Object = MibTableColumn
cfprMgmtEntitySshAuthKeysSize = _CfprMgmtEntitySshAuthKeysSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 18),
    _CfprMgmtEntitySshAuthKeysSize_Type()
)
cfprMgmtEntitySshAuthKeysSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntitySshAuthKeysSize.setStatus("current")
_CfprMgmtEntitySshKeyStatus_Type = Unsigned64
_CfprMgmtEntitySshKeyStatus_Object = MibTableColumn
cfprMgmtEntitySshKeyStatus = _CfprMgmtEntitySshKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 19),
    _CfprMgmtEntitySshKeyStatus_Type()
)
cfprMgmtEntitySshKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntitySshKeyStatus.setStatus("current")
_CfprMgmtEntitySshRootPubKeyCsum_Type = SnmpAdminString
_CfprMgmtEntitySshRootPubKeyCsum_Object = MibTableColumn
cfprMgmtEntitySshRootPubKeyCsum = _CfprMgmtEntitySshRootPubKeyCsum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 20),
    _CfprMgmtEntitySshRootPubKeyCsum_Type()
)
cfprMgmtEntitySshRootPubKeyCsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntitySshRootPubKeyCsum.setStatus("current")
_CfprMgmtEntitySshRootPubKeySize_Type = Unsigned64
_CfprMgmtEntitySshRootPubKeySize_Object = MibTableColumn
cfprMgmtEntitySshRootPubKeySize = _CfprMgmtEntitySshRootPubKeySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 21),
    _CfprMgmtEntitySshRootPubKeySize_Type()
)
cfprMgmtEntitySshRootPubKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntitySshRootPubKeySize.setStatus("current")
_CfprMgmtEntityState_Type = CfprMgmtEntityState
_CfprMgmtEntityState_Object = MibTableColumn
cfprMgmtEntityState = _CfprMgmtEntityState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 22),
    _CfprMgmtEntityState_Type()
)
cfprMgmtEntityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityState.setStatus("current")
_CfprMgmtEntityUmbilicalState_Type = CfprMgmtEntityUmbilicalState
_CfprMgmtEntityUmbilicalState_Object = MibTableColumn
cfprMgmtEntityUmbilicalState = _CfprMgmtEntityUmbilicalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 23),
    _CfprMgmtEntityUmbilicalState_Type()
)
cfprMgmtEntityUmbilicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityUmbilicalState.setStatus("current")
_CfprMgmtEntityVersionMismatch_Type = TruthValue
_CfprMgmtEntityVersionMismatch_Object = MibTableColumn
cfprMgmtEntityVersionMismatch = _CfprMgmtEntityVersionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 22, 1, 24),
    _CfprMgmtEntityVersionMismatch_Type()
)
cfprMgmtEntityVersionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtEntityVersionMismatch.setStatus("current")
_CfprMgmtExportPolicyFsmTable_Object = MibTable
cfprMgmtExportPolicyFsmTable = _CfprMgmtExportPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23)
)
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmTable.setStatus("current")
_CfprMgmtExportPolicyFsmEntry_Object = MibTableRow
cfprMgmtExportPolicyFsmEntry = _CfprMgmtExportPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23, 1)
)
cfprMgmtExportPolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtExportPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmEntry.setStatus("current")
_CfprMgmtExportPolicyFsmInstanceId_Type = CfprManagedObjectId
_CfprMgmtExportPolicyFsmInstanceId_Object = MibTableColumn
cfprMgmtExportPolicyFsmInstanceId = _CfprMgmtExportPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23, 1, 1),
    _CfprMgmtExportPolicyFsmInstanceId_Type()
)
cfprMgmtExportPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmInstanceId.setStatus("current")
_CfprMgmtExportPolicyFsmDn_Type = CfprManagedObjectDn
_CfprMgmtExportPolicyFsmDn_Object = MibTableColumn
cfprMgmtExportPolicyFsmDn = _CfprMgmtExportPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23, 1, 2),
    _CfprMgmtExportPolicyFsmDn_Type()
)
cfprMgmtExportPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmDn.setStatus("current")
_CfprMgmtExportPolicyFsmRn_Type = SnmpAdminString
_CfprMgmtExportPolicyFsmRn_Object = MibTableColumn
cfprMgmtExportPolicyFsmRn = _CfprMgmtExportPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23, 1, 3),
    _CfprMgmtExportPolicyFsmRn_Type()
)
cfprMgmtExportPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmRn.setStatus("current")
_CfprMgmtExportPolicyFsmCompletionTime_Type = DateAndTime
_CfprMgmtExportPolicyFsmCompletionTime_Object = MibTableColumn
cfprMgmtExportPolicyFsmCompletionTime = _CfprMgmtExportPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23, 1, 4),
    _CfprMgmtExportPolicyFsmCompletionTime_Type()
)
cfprMgmtExportPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmCompletionTime.setStatus("current")
_CfprMgmtExportPolicyFsmCurrentFsm_Type = CfprMgmtExportPolicyFsmCurrentFsm
_CfprMgmtExportPolicyFsmCurrentFsm_Object = MibTableColumn
cfprMgmtExportPolicyFsmCurrentFsm = _CfprMgmtExportPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23, 1, 5),
    _CfprMgmtExportPolicyFsmCurrentFsm_Type()
)
cfprMgmtExportPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmCurrentFsm.setStatus("current")
_CfprMgmtExportPolicyFsmDescr_Type = SnmpAdminString
_CfprMgmtExportPolicyFsmDescr_Object = MibTableColumn
cfprMgmtExportPolicyFsmDescr = _CfprMgmtExportPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23, 1, 6),
    _CfprMgmtExportPolicyFsmDescr_Type()
)
cfprMgmtExportPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmDescr.setStatus("current")
_CfprMgmtExportPolicyFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtExportPolicyFsmFsmStatus_Object = MibTableColumn
cfprMgmtExportPolicyFsmFsmStatus = _CfprMgmtExportPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23, 1, 7),
    _CfprMgmtExportPolicyFsmFsmStatus_Type()
)
cfprMgmtExportPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmFsmStatus.setStatus("current")
_CfprMgmtExportPolicyFsmProgress_Type = Gauge32
_CfprMgmtExportPolicyFsmProgress_Object = MibTableColumn
cfprMgmtExportPolicyFsmProgress = _CfprMgmtExportPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23, 1, 8),
    _CfprMgmtExportPolicyFsmProgress_Type()
)
cfprMgmtExportPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmProgress.setStatus("current")
_CfprMgmtExportPolicyFsmRmtErrCode_Type = Gauge32
_CfprMgmtExportPolicyFsmRmtErrCode_Object = MibTableColumn
cfprMgmtExportPolicyFsmRmtErrCode = _CfprMgmtExportPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23, 1, 9),
    _CfprMgmtExportPolicyFsmRmtErrCode_Type()
)
cfprMgmtExportPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmRmtErrCode.setStatus("current")
_CfprMgmtExportPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprMgmtExportPolicyFsmRmtErrDescr_Object = MibTableColumn
cfprMgmtExportPolicyFsmRmtErrDescr = _CfprMgmtExportPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23, 1, 10),
    _CfprMgmtExportPolicyFsmRmtErrDescr_Type()
)
cfprMgmtExportPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmRmtErrDescr.setStatus("current")
_CfprMgmtExportPolicyFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtExportPolicyFsmRmtRslt_Object = MibTableColumn
cfprMgmtExportPolicyFsmRmtRslt = _CfprMgmtExportPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 23, 1, 11),
    _CfprMgmtExportPolicyFsmRmtRslt_Type()
)
cfprMgmtExportPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmRmtRslt.setStatus("current")
_CfprMgmtExportPolicyFsmStageTable_Object = MibTable
cfprMgmtExportPolicyFsmStageTable = _CfprMgmtExportPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 24)
)
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmStageTable.setStatus("current")
_CfprMgmtExportPolicyFsmStageEntry_Object = MibTableRow
cfprMgmtExportPolicyFsmStageEntry = _CfprMgmtExportPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 24, 1)
)
cfprMgmtExportPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtExportPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmStageEntry.setStatus("current")
_CfprMgmtExportPolicyFsmStageInstanceId_Type = CfprManagedObjectId
_CfprMgmtExportPolicyFsmStageInstanceId_Object = MibTableColumn
cfprMgmtExportPolicyFsmStageInstanceId = _CfprMgmtExportPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 24, 1, 1),
    _CfprMgmtExportPolicyFsmStageInstanceId_Type()
)
cfprMgmtExportPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmStageInstanceId.setStatus("current")
_CfprMgmtExportPolicyFsmStageDn_Type = CfprManagedObjectDn
_CfprMgmtExportPolicyFsmStageDn_Object = MibTableColumn
cfprMgmtExportPolicyFsmStageDn = _CfprMgmtExportPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 24, 1, 2),
    _CfprMgmtExportPolicyFsmStageDn_Type()
)
cfprMgmtExportPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmStageDn.setStatus("current")
_CfprMgmtExportPolicyFsmStageRn_Type = SnmpAdminString
_CfprMgmtExportPolicyFsmStageRn_Object = MibTableColumn
cfprMgmtExportPolicyFsmStageRn = _CfprMgmtExportPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 24, 1, 3),
    _CfprMgmtExportPolicyFsmStageRn_Type()
)
cfprMgmtExportPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmStageRn.setStatus("current")
_CfprMgmtExportPolicyFsmStageDescr_Type = SnmpAdminString
_CfprMgmtExportPolicyFsmStageDescr_Object = MibTableColumn
cfprMgmtExportPolicyFsmStageDescr = _CfprMgmtExportPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 24, 1, 4),
    _CfprMgmtExportPolicyFsmStageDescr_Type()
)
cfprMgmtExportPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmStageDescr.setStatus("current")
_CfprMgmtExportPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprMgmtExportPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprMgmtExportPolicyFsmStageLastUpdateTime = _CfprMgmtExportPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 24, 1, 5),
    _CfprMgmtExportPolicyFsmStageLastUpdateTime_Type()
)
cfprMgmtExportPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmStageLastUpdateTime.setStatus("current")
_CfprMgmtExportPolicyFsmStageName_Type = CfprMgmtExportPolicyFsmStageName
_CfprMgmtExportPolicyFsmStageName_Object = MibTableColumn
cfprMgmtExportPolicyFsmStageName = _CfprMgmtExportPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 24, 1, 6),
    _CfprMgmtExportPolicyFsmStageName_Type()
)
cfprMgmtExportPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmStageName.setStatus("current")
_CfprMgmtExportPolicyFsmStageOrder_Type = Gauge32
_CfprMgmtExportPolicyFsmStageOrder_Object = MibTableColumn
cfprMgmtExportPolicyFsmStageOrder = _CfprMgmtExportPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 24, 1, 7),
    _CfprMgmtExportPolicyFsmStageOrder_Type()
)
cfprMgmtExportPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmStageOrder.setStatus("current")
_CfprMgmtExportPolicyFsmStageRetry_Type = Gauge32
_CfprMgmtExportPolicyFsmStageRetry_Object = MibTableColumn
cfprMgmtExportPolicyFsmStageRetry = _CfprMgmtExportPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 24, 1, 8),
    _CfprMgmtExportPolicyFsmStageRetry_Type()
)
cfprMgmtExportPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmStageRetry.setStatus("current")
_CfprMgmtExportPolicyFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtExportPolicyFsmStageStageStatus_Object = MibTableColumn
cfprMgmtExportPolicyFsmStageStageStatus = _CfprMgmtExportPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 24, 1, 9),
    _CfprMgmtExportPolicyFsmStageStageStatus_Type()
)
cfprMgmtExportPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmStageStageStatus.setStatus("current")
_CfprMgmtExportPolicyFsmTaskTable_Object = MibTable
cfprMgmtExportPolicyFsmTaskTable = _CfprMgmtExportPolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 25)
)
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmTaskTable.setStatus("current")
_CfprMgmtExportPolicyFsmTaskEntry_Object = MibTableRow
cfprMgmtExportPolicyFsmTaskEntry = _CfprMgmtExportPolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 25, 1)
)
cfprMgmtExportPolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtExportPolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmTaskEntry.setStatus("current")
_CfprMgmtExportPolicyFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprMgmtExportPolicyFsmTaskInstanceId_Object = MibTableColumn
cfprMgmtExportPolicyFsmTaskInstanceId = _CfprMgmtExportPolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 25, 1, 1),
    _CfprMgmtExportPolicyFsmTaskInstanceId_Type()
)
cfprMgmtExportPolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmTaskInstanceId.setStatus("current")
_CfprMgmtExportPolicyFsmTaskDn_Type = CfprManagedObjectDn
_CfprMgmtExportPolicyFsmTaskDn_Object = MibTableColumn
cfprMgmtExportPolicyFsmTaskDn = _CfprMgmtExportPolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 25, 1, 2),
    _CfprMgmtExportPolicyFsmTaskDn_Type()
)
cfprMgmtExportPolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmTaskDn.setStatus("current")
_CfprMgmtExportPolicyFsmTaskRn_Type = SnmpAdminString
_CfprMgmtExportPolicyFsmTaskRn_Object = MibTableColumn
cfprMgmtExportPolicyFsmTaskRn = _CfprMgmtExportPolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 25, 1, 3),
    _CfprMgmtExportPolicyFsmTaskRn_Type()
)
cfprMgmtExportPolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmTaskRn.setStatus("current")
_CfprMgmtExportPolicyFsmTaskCompletion_Type = CfprFsmCompletion
_CfprMgmtExportPolicyFsmTaskCompletion_Object = MibTableColumn
cfprMgmtExportPolicyFsmTaskCompletion = _CfprMgmtExportPolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 25, 1, 4),
    _CfprMgmtExportPolicyFsmTaskCompletion_Type()
)
cfprMgmtExportPolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmTaskCompletion.setStatus("current")
_CfprMgmtExportPolicyFsmTaskFlags_Type = CfprFsmFlags
_CfprMgmtExportPolicyFsmTaskFlags_Object = MibTableColumn
cfprMgmtExportPolicyFsmTaskFlags = _CfprMgmtExportPolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 25, 1, 5),
    _CfprMgmtExportPolicyFsmTaskFlags_Type()
)
cfprMgmtExportPolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmTaskFlags.setStatus("current")
_CfprMgmtExportPolicyFsmTaskItem_Type = CfprMgmtExportPolicyFsmTaskItem
_CfprMgmtExportPolicyFsmTaskItem_Object = MibTableColumn
cfprMgmtExportPolicyFsmTaskItem = _CfprMgmtExportPolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 25, 1, 6),
    _CfprMgmtExportPolicyFsmTaskItem_Type()
)
cfprMgmtExportPolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmTaskItem.setStatus("current")
_CfprMgmtExportPolicyFsmTaskSeqId_Type = Gauge32
_CfprMgmtExportPolicyFsmTaskSeqId_Object = MibTableColumn
cfprMgmtExportPolicyFsmTaskSeqId = _CfprMgmtExportPolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 25, 1, 7),
    _CfprMgmtExportPolicyFsmTaskSeqId_Type()
)
cfprMgmtExportPolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtExportPolicyFsmTaskSeqId.setStatus("current")
_CfprMgmtIPv6IfAddrTable_Object = MibTable
cfprMgmtIPv6IfAddrTable = _CfprMgmtIPv6IfAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26)
)
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrTable.setStatus("current")
_CfprMgmtIPv6IfAddrEntry_Object = MibTableRow
cfprMgmtIPv6IfAddrEntry = _CfprMgmtIPv6IfAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1)
)
cfprMgmtIPv6IfAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtIPv6IfAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrEntry.setStatus("current")
_CfprMgmtIPv6IfAddrInstanceId_Type = CfprManagedObjectId
_CfprMgmtIPv6IfAddrInstanceId_Object = MibTableColumn
cfprMgmtIPv6IfAddrInstanceId = _CfprMgmtIPv6IfAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 1),
    _CfprMgmtIPv6IfAddrInstanceId_Type()
)
cfprMgmtIPv6IfAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrInstanceId.setStatus("current")
_CfprMgmtIPv6IfAddrDn_Type = CfprManagedObjectDn
_CfprMgmtIPv6IfAddrDn_Object = MibTableColumn
cfprMgmtIPv6IfAddrDn = _CfprMgmtIPv6IfAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 2),
    _CfprMgmtIPv6IfAddrDn_Type()
)
cfprMgmtIPv6IfAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrDn.setStatus("current")
_CfprMgmtIPv6IfAddrRn_Type = SnmpAdminString
_CfprMgmtIPv6IfAddrRn_Object = MibTableColumn
cfprMgmtIPv6IfAddrRn = _CfprMgmtIPv6IfAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 3),
    _CfprMgmtIPv6IfAddrRn_Type()
)
cfprMgmtIPv6IfAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrRn.setStatus("current")
_CfprMgmtIPv6IfAddrAddr_Type = InetAddressIPv6
_CfprMgmtIPv6IfAddrAddr_Object = MibTableColumn
cfprMgmtIPv6IfAddrAddr = _CfprMgmtIPv6IfAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 4),
    _CfprMgmtIPv6IfAddrAddr_Type()
)
cfprMgmtIPv6IfAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrAddr.setStatus("current")
_CfprMgmtIPv6IfAddrDefGw_Type = InetAddressIPv6
_CfprMgmtIPv6IfAddrDefGw_Object = MibTableColumn
cfprMgmtIPv6IfAddrDefGw = _CfprMgmtIPv6IfAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 5),
    _CfprMgmtIPv6IfAddrDefGw_Type()
)
cfprMgmtIPv6IfAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrDefGw.setStatus("current")
_CfprMgmtIPv6IfAddrFsmDescr_Type = SnmpAdminString
_CfprMgmtIPv6IfAddrFsmDescr_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmDescr = _CfprMgmtIPv6IfAddrFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 6),
    _CfprMgmtIPv6IfAddrFsmDescr_Type()
)
cfprMgmtIPv6IfAddrFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmDescr.setStatus("current")
_CfprMgmtIPv6IfAddrFsmPrev_Type = SnmpAdminString
_CfprMgmtIPv6IfAddrFsmPrev_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmPrev = _CfprMgmtIPv6IfAddrFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 7),
    _CfprMgmtIPv6IfAddrFsmPrev_Type()
)
cfprMgmtIPv6IfAddrFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmPrev.setStatus("current")
_CfprMgmtIPv6IfAddrFsmProgr_Type = Gauge32
_CfprMgmtIPv6IfAddrFsmProgr_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmProgr = _CfprMgmtIPv6IfAddrFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 8),
    _CfprMgmtIPv6IfAddrFsmProgr_Type()
)
cfprMgmtIPv6IfAddrFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmProgr.setStatus("current")
_CfprMgmtIPv6IfAddrFsmRmtInvErrCode_Type = Gauge32
_CfprMgmtIPv6IfAddrFsmRmtInvErrCode_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmRmtInvErrCode = _CfprMgmtIPv6IfAddrFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 9),
    _CfprMgmtIPv6IfAddrFsmRmtInvErrCode_Type()
)
cfprMgmtIPv6IfAddrFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmRmtInvErrCode.setStatus("current")
_CfprMgmtIPv6IfAddrFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprMgmtIPv6IfAddrFsmRmtInvErrDescr_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmRmtInvErrDescr = _CfprMgmtIPv6IfAddrFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 10),
    _CfprMgmtIPv6IfAddrFsmRmtInvErrDescr_Type()
)
cfprMgmtIPv6IfAddrFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmRmtInvErrDescr.setStatus("current")
_CfprMgmtIPv6IfAddrFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtIPv6IfAddrFsmRmtInvRslt_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmRmtInvRslt = _CfprMgmtIPv6IfAddrFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 11),
    _CfprMgmtIPv6IfAddrFsmRmtInvRslt_Type()
)
cfprMgmtIPv6IfAddrFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmRmtInvRslt.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStageDescr_Type = SnmpAdminString
_CfprMgmtIPv6IfAddrFsmStageDescr_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmStageDescr = _CfprMgmtIPv6IfAddrFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 12),
    _CfprMgmtIPv6IfAddrFsmStageDescr_Type()
)
cfprMgmtIPv6IfAddrFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStageDescr.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStamp_Type = DateAndTime
_CfprMgmtIPv6IfAddrFsmStamp_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmStamp = _CfprMgmtIPv6IfAddrFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 13),
    _CfprMgmtIPv6IfAddrFsmStamp_Type()
)
cfprMgmtIPv6IfAddrFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStamp.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStatus_Type = SnmpAdminString
_CfprMgmtIPv6IfAddrFsmStatus_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmStatus = _CfprMgmtIPv6IfAddrFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 14),
    _CfprMgmtIPv6IfAddrFsmStatus_Type()
)
cfprMgmtIPv6IfAddrFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStatus.setStatus("current")
_CfprMgmtIPv6IfAddrFsmTry_Type = Gauge32
_CfprMgmtIPv6IfAddrFsmTry_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmTry = _CfprMgmtIPv6IfAddrFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 15),
    _CfprMgmtIPv6IfAddrFsmTry_Type()
)
cfprMgmtIPv6IfAddrFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmTry.setStatus("current")
_CfprMgmtIPv6IfAddrPrefix_Type = Gauge32
_CfprMgmtIPv6IfAddrPrefix_Object = MibTableColumn
cfprMgmtIPv6IfAddrPrefix = _CfprMgmtIPv6IfAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 16),
    _CfprMgmtIPv6IfAddrPrefix_Type()
)
cfprMgmtIPv6IfAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrPrefix.setStatus("current")
_CfprMgmtIPv6IfAddrIpv6autocfg_Type = CfprMgmtIPv6Format
_CfprMgmtIPv6IfAddrIpv6autocfg_Object = MibTableColumn
cfprMgmtIPv6IfAddrIpv6autocfg = _CfprMgmtIPv6IfAddrIpv6autocfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 17),
    _CfprMgmtIPv6IfAddrIpv6autocfg_Type()
)
cfprMgmtIPv6IfAddrIpv6autocfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrIpv6autocfg.setStatus("current")
_CfprMgmtIPv6IfAddrIpv6dirtyint_Type = CfprMgmtIPv6AutoAddrFormat
_CfprMgmtIPv6IfAddrIpv6dirtyint_Object = MibTableColumn
cfprMgmtIPv6IfAddrIpv6dirtyint = _CfprMgmtIPv6IfAddrIpv6dirtyint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 18),
    _CfprMgmtIPv6IfAddrIpv6dirtyint_Type()
)
cfprMgmtIPv6IfAddrIpv6dirtyint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrIpv6dirtyint.setStatus("current")
_CfprMgmtIPv6IfAddrIpv6readyaddr_Type = InetAddressIPv6
_CfprMgmtIPv6IfAddrIpv6readyaddr_Object = MibTableColumn
cfprMgmtIPv6IfAddrIpv6readyaddr = _CfprMgmtIPv6IfAddrIpv6readyaddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 19),
    _CfprMgmtIPv6IfAddrIpv6readyaddr_Type()
)
cfprMgmtIPv6IfAddrIpv6readyaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrIpv6readyaddr.setStatus("current")
_CfprMgmtIPv6IfAddrIpv6readycfg_Type = CfprMgmtIPv6Format
_CfprMgmtIPv6IfAddrIpv6readycfg_Object = MibTableColumn
cfprMgmtIPv6IfAddrIpv6readycfg = _CfprMgmtIPv6IfAddrIpv6readycfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 20),
    _CfprMgmtIPv6IfAddrIpv6readycfg_Type()
)
cfprMgmtIPv6IfAddrIpv6readycfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrIpv6readycfg.setStatus("current")
_CfprMgmtIPv6IfAddrIpv6readyprefix_Type = Gauge32
_CfprMgmtIPv6IfAddrIpv6readyprefix_Object = MibTableColumn
cfprMgmtIPv6IfAddrIpv6readyprefix = _CfprMgmtIPv6IfAddrIpv6readyprefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 21),
    _CfprMgmtIPv6IfAddrIpv6readyprefix_Type()
)
cfprMgmtIPv6IfAddrIpv6readyprefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrIpv6readyprefix.setStatus("current")
_CfprMgmtIPv6IfAddrIpv6val_Type = CfprMgmtIpv6AdminState
_CfprMgmtIPv6IfAddrIpv6val_Object = MibTableColumn
cfprMgmtIPv6IfAddrIpv6val = _CfprMgmtIPv6IfAddrIpv6val_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 22),
    _CfprMgmtIPv6IfAddrIpv6val_Type()
)
cfprMgmtIPv6IfAddrIpv6val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrIpv6val.setStatus("current")
_CfprMgmtIPv6IfAddrNdval_Type = CfprMgmtIpv6AdminState
_CfprMgmtIPv6IfAddrNdval_Object = MibTableColumn
cfprMgmtIPv6IfAddrNdval = _CfprMgmtIPv6IfAddrNdval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 26, 1, 23),
    _CfprMgmtIPv6IfAddrNdval_Type()
)
cfprMgmtIPv6IfAddrNdval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrNdval.setStatus("current")
_CfprMgmtIPv6IfAddrFsmTable_Object = MibTable
cfprMgmtIPv6IfAddrFsmTable = _CfprMgmtIPv6IfAddrFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27)
)
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmTable.setStatus("current")
_CfprMgmtIPv6IfAddrFsmEntry_Object = MibTableRow
cfprMgmtIPv6IfAddrFsmEntry = _CfprMgmtIPv6IfAddrFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27, 1)
)
cfprMgmtIPv6IfAddrFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtIPv6IfAddrFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmEntry.setStatus("current")
_CfprMgmtIPv6IfAddrFsmInstanceId_Type = CfprManagedObjectId
_CfprMgmtIPv6IfAddrFsmInstanceId_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmInstanceId = _CfprMgmtIPv6IfAddrFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27, 1, 1),
    _CfprMgmtIPv6IfAddrFsmInstanceId_Type()
)
cfprMgmtIPv6IfAddrFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmInstanceId.setStatus("current")
_CfprMgmtIPv6IfAddrFsmDn_Type = CfprManagedObjectDn
_CfprMgmtIPv6IfAddrFsmDn_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmDn = _CfprMgmtIPv6IfAddrFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27, 1, 2),
    _CfprMgmtIPv6IfAddrFsmDn_Type()
)
cfprMgmtIPv6IfAddrFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmDn.setStatus("current")
_CfprMgmtIPv6IfAddrFsmRn_Type = SnmpAdminString
_CfprMgmtIPv6IfAddrFsmRn_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmRn = _CfprMgmtIPv6IfAddrFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27, 1, 3),
    _CfprMgmtIPv6IfAddrFsmRn_Type()
)
cfprMgmtIPv6IfAddrFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmRn.setStatus("current")
_CfprMgmtIPv6IfAddrFsmCompletionTime_Type = DateAndTime
_CfprMgmtIPv6IfAddrFsmCompletionTime_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmCompletionTime = _CfprMgmtIPv6IfAddrFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27, 1, 4),
    _CfprMgmtIPv6IfAddrFsmCompletionTime_Type()
)
cfprMgmtIPv6IfAddrFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmCompletionTime.setStatus("current")
_CfprMgmtIPv6IfAddrFsmCurrentFsm_Type = CfprMgmtIPv6IfAddrFsmCurrentFsm
_CfprMgmtIPv6IfAddrFsmCurrentFsm_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmCurrentFsm = _CfprMgmtIPv6IfAddrFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27, 1, 5),
    _CfprMgmtIPv6IfAddrFsmCurrentFsm_Type()
)
cfprMgmtIPv6IfAddrFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmCurrentFsm.setStatus("current")
_CfprMgmtIPv6IfAddrFsmDescrData_Type = SnmpAdminString
_CfprMgmtIPv6IfAddrFsmDescrData_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmDescrData = _CfprMgmtIPv6IfAddrFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27, 1, 6),
    _CfprMgmtIPv6IfAddrFsmDescrData_Type()
)
cfprMgmtIPv6IfAddrFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmDescrData.setStatus("current")
_CfprMgmtIPv6IfAddrFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtIPv6IfAddrFsmFsmStatus_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmFsmStatus = _CfprMgmtIPv6IfAddrFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27, 1, 7),
    _CfprMgmtIPv6IfAddrFsmFsmStatus_Type()
)
cfprMgmtIPv6IfAddrFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmFsmStatus.setStatus("current")
_CfprMgmtIPv6IfAddrFsmProgress_Type = Gauge32
_CfprMgmtIPv6IfAddrFsmProgress_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmProgress = _CfprMgmtIPv6IfAddrFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27, 1, 8),
    _CfprMgmtIPv6IfAddrFsmProgress_Type()
)
cfprMgmtIPv6IfAddrFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmProgress.setStatus("current")
_CfprMgmtIPv6IfAddrFsmRmtErrCode_Type = Gauge32
_CfprMgmtIPv6IfAddrFsmRmtErrCode_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmRmtErrCode = _CfprMgmtIPv6IfAddrFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27, 1, 9),
    _CfprMgmtIPv6IfAddrFsmRmtErrCode_Type()
)
cfprMgmtIPv6IfAddrFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmRmtErrCode.setStatus("current")
_CfprMgmtIPv6IfAddrFsmRmtErrDescr_Type = SnmpAdminString
_CfprMgmtIPv6IfAddrFsmRmtErrDescr_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmRmtErrDescr = _CfprMgmtIPv6IfAddrFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27, 1, 10),
    _CfprMgmtIPv6IfAddrFsmRmtErrDescr_Type()
)
cfprMgmtIPv6IfAddrFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmRmtErrDescr.setStatus("current")
_CfprMgmtIPv6IfAddrFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtIPv6IfAddrFsmRmtRslt_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmRmtRslt = _CfprMgmtIPv6IfAddrFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 27, 1, 11),
    _CfprMgmtIPv6IfAddrFsmRmtRslt_Type()
)
cfprMgmtIPv6IfAddrFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmRmtRslt.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStageTable_Object = MibTable
cfprMgmtIPv6IfAddrFsmStageTable = _CfprMgmtIPv6IfAddrFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 28)
)
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStageTable.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStageEntry_Object = MibTableRow
cfprMgmtIPv6IfAddrFsmStageEntry = _CfprMgmtIPv6IfAddrFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 28, 1)
)
cfprMgmtIPv6IfAddrFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtIPv6IfAddrFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStageEntry.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStageInstanceId_Type = CfprManagedObjectId
_CfprMgmtIPv6IfAddrFsmStageInstanceId_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmStageInstanceId = _CfprMgmtIPv6IfAddrFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 28, 1, 1),
    _CfprMgmtIPv6IfAddrFsmStageInstanceId_Type()
)
cfprMgmtIPv6IfAddrFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStageInstanceId.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStageDn_Type = CfprManagedObjectDn
_CfprMgmtIPv6IfAddrFsmStageDn_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmStageDn = _CfprMgmtIPv6IfAddrFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 28, 1, 2),
    _CfprMgmtIPv6IfAddrFsmStageDn_Type()
)
cfprMgmtIPv6IfAddrFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStageDn.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStageRn_Type = SnmpAdminString
_CfprMgmtIPv6IfAddrFsmStageRn_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmStageRn = _CfprMgmtIPv6IfAddrFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 28, 1, 3),
    _CfprMgmtIPv6IfAddrFsmStageRn_Type()
)
cfprMgmtIPv6IfAddrFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStageRn.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStageDescrData_Type = SnmpAdminString
_CfprMgmtIPv6IfAddrFsmStageDescrData_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmStageDescrData = _CfprMgmtIPv6IfAddrFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 28, 1, 4),
    _CfprMgmtIPv6IfAddrFsmStageDescrData_Type()
)
cfprMgmtIPv6IfAddrFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStageDescrData.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStageLastUpdateTime_Type = DateAndTime
_CfprMgmtIPv6IfAddrFsmStageLastUpdateTime_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmStageLastUpdateTime = _CfprMgmtIPv6IfAddrFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 28, 1, 5),
    _CfprMgmtIPv6IfAddrFsmStageLastUpdateTime_Type()
)
cfprMgmtIPv6IfAddrFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStageLastUpdateTime.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStageName_Type = CfprMgmtIPv6IfAddrFsmStageName
_CfprMgmtIPv6IfAddrFsmStageName_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmStageName = _CfprMgmtIPv6IfAddrFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 28, 1, 6),
    _CfprMgmtIPv6IfAddrFsmStageName_Type()
)
cfprMgmtIPv6IfAddrFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStageName.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStageOrder_Type = Gauge32
_CfprMgmtIPv6IfAddrFsmStageOrder_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmStageOrder = _CfprMgmtIPv6IfAddrFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 28, 1, 7),
    _CfprMgmtIPv6IfAddrFsmStageOrder_Type()
)
cfprMgmtIPv6IfAddrFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStageOrder.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStageRetry_Type = Gauge32
_CfprMgmtIPv6IfAddrFsmStageRetry_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmStageRetry = _CfprMgmtIPv6IfAddrFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 28, 1, 8),
    _CfprMgmtIPv6IfAddrFsmStageRetry_Type()
)
cfprMgmtIPv6IfAddrFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStageRetry.setStatus("current")
_CfprMgmtIPv6IfAddrFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtIPv6IfAddrFsmStageStageStatus_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmStageStageStatus = _CfprMgmtIPv6IfAddrFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 28, 1, 9),
    _CfprMgmtIPv6IfAddrFsmStageStageStatus_Type()
)
cfprMgmtIPv6IfAddrFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmStageStageStatus.setStatus("current")
_CfprMgmtIPv6IfAddrFsmTaskTable_Object = MibTable
cfprMgmtIPv6IfAddrFsmTaskTable = _CfprMgmtIPv6IfAddrFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 29)
)
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmTaskTable.setStatus("current")
_CfprMgmtIPv6IfAddrFsmTaskEntry_Object = MibTableRow
cfprMgmtIPv6IfAddrFsmTaskEntry = _CfprMgmtIPv6IfAddrFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 29, 1)
)
cfprMgmtIPv6IfAddrFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtIPv6IfAddrFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmTaskEntry.setStatus("current")
_CfprMgmtIPv6IfAddrFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprMgmtIPv6IfAddrFsmTaskInstanceId_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmTaskInstanceId = _CfprMgmtIPv6IfAddrFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 29, 1, 1),
    _CfprMgmtIPv6IfAddrFsmTaskInstanceId_Type()
)
cfprMgmtIPv6IfAddrFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmTaskInstanceId.setStatus("current")
_CfprMgmtIPv6IfAddrFsmTaskDn_Type = CfprManagedObjectDn
_CfprMgmtIPv6IfAddrFsmTaskDn_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmTaskDn = _CfprMgmtIPv6IfAddrFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 29, 1, 2),
    _CfprMgmtIPv6IfAddrFsmTaskDn_Type()
)
cfprMgmtIPv6IfAddrFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmTaskDn.setStatus("current")
_CfprMgmtIPv6IfAddrFsmTaskRn_Type = SnmpAdminString
_CfprMgmtIPv6IfAddrFsmTaskRn_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmTaskRn = _CfprMgmtIPv6IfAddrFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 29, 1, 3),
    _CfprMgmtIPv6IfAddrFsmTaskRn_Type()
)
cfprMgmtIPv6IfAddrFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmTaskRn.setStatus("current")
_CfprMgmtIPv6IfAddrFsmTaskCompletion_Type = CfprFsmCompletion
_CfprMgmtIPv6IfAddrFsmTaskCompletion_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmTaskCompletion = _CfprMgmtIPv6IfAddrFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 29, 1, 4),
    _CfprMgmtIPv6IfAddrFsmTaskCompletion_Type()
)
cfprMgmtIPv6IfAddrFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmTaskCompletion.setStatus("current")
_CfprMgmtIPv6IfAddrFsmTaskFlags_Type = CfprFsmFlags
_CfprMgmtIPv6IfAddrFsmTaskFlags_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmTaskFlags = _CfprMgmtIPv6IfAddrFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 29, 1, 5),
    _CfprMgmtIPv6IfAddrFsmTaskFlags_Type()
)
cfprMgmtIPv6IfAddrFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmTaskFlags.setStatus("current")
_CfprMgmtIPv6IfAddrFsmTaskItem_Type = CfprMgmtIPv6IfAddrFsmTaskItem
_CfprMgmtIPv6IfAddrFsmTaskItem_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmTaskItem = _CfprMgmtIPv6IfAddrFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 29, 1, 6),
    _CfprMgmtIPv6IfAddrFsmTaskItem_Type()
)
cfprMgmtIPv6IfAddrFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmTaskItem.setStatus("current")
_CfprMgmtIPv6IfAddrFsmTaskSeqId_Type = Gauge32
_CfprMgmtIPv6IfAddrFsmTaskSeqId_Object = MibTableColumn
cfprMgmtIPv6IfAddrFsmTaskSeqId = _CfprMgmtIPv6IfAddrFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 29, 1, 7),
    _CfprMgmtIPv6IfAddrFsmTaskSeqId_Type()
)
cfprMgmtIPv6IfAddrFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfAddrFsmTaskSeqId.setStatus("current")
_CfprMgmtIPv6IfConfigTable_Object = MibTable
cfprMgmtIPv6IfConfigTable = _CfprMgmtIPv6IfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 30)
)
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfConfigTable.setStatus("current")
_CfprMgmtIPv6IfConfigEntry_Object = MibTableRow
cfprMgmtIPv6IfConfigEntry = _CfprMgmtIPv6IfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 30, 1)
)
cfprMgmtIPv6IfConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtIPv6IfConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfConfigEntry.setStatus("current")
_CfprMgmtIPv6IfConfigInstanceId_Type = CfprManagedObjectId
_CfprMgmtIPv6IfConfigInstanceId_Object = MibTableColumn
cfprMgmtIPv6IfConfigInstanceId = _CfprMgmtIPv6IfConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 30, 1, 1),
    _CfprMgmtIPv6IfConfigInstanceId_Type()
)
cfprMgmtIPv6IfConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfConfigInstanceId.setStatus("current")
_CfprMgmtIPv6IfConfigDn_Type = CfprManagedObjectDn
_CfprMgmtIPv6IfConfigDn_Object = MibTableColumn
cfprMgmtIPv6IfConfigDn = _CfprMgmtIPv6IfConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 30, 1, 2),
    _CfprMgmtIPv6IfConfigDn_Type()
)
cfprMgmtIPv6IfConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfConfigDn.setStatus("current")
_CfprMgmtIPv6IfConfigRn_Type = SnmpAdminString
_CfprMgmtIPv6IfConfigRn_Object = MibTableColumn
cfprMgmtIPv6IfConfigRn = _CfprMgmtIPv6IfConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 30, 1, 3),
    _CfprMgmtIPv6IfConfigRn_Type()
)
cfprMgmtIPv6IfConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIPv6IfConfigRn.setStatus("current")
_CfprMgmtIfTable_Object = MibTable
cfprMgmtIfTable = _CfprMgmtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31)
)
if mibBuilder.loadTexts:
    cfprMgmtIfTable.setStatus("current")
_CfprMgmtIfEntry_Object = MibTableRow
cfprMgmtIfEntry = _CfprMgmtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1)
)
cfprMgmtIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtIfEntry.setStatus("current")
_CfprMgmtIfInstanceId_Type = CfprManagedObjectId
_CfprMgmtIfInstanceId_Object = MibTableColumn
cfprMgmtIfInstanceId = _CfprMgmtIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 1),
    _CfprMgmtIfInstanceId_Type()
)
cfprMgmtIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtIfInstanceId.setStatus("current")
_CfprMgmtIfDn_Type = CfprManagedObjectDn
_CfprMgmtIfDn_Object = MibTableColumn
cfprMgmtIfDn = _CfprMgmtIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 2),
    _CfprMgmtIfDn_Type()
)
cfprMgmtIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfDn.setStatus("current")
_CfprMgmtIfRn_Type = SnmpAdminString
_CfprMgmtIfRn_Object = MibTableColumn
cfprMgmtIfRn = _CfprMgmtIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 3),
    _CfprMgmtIfRn_Type()
)
cfprMgmtIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfRn.setStatus("current")
_CfprMgmtIfAccess_Type = CfprMgmtAccess
_CfprMgmtIfAccess_Object = MibTableColumn
cfprMgmtIfAccess = _CfprMgmtIfAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 4),
    _CfprMgmtIfAccess_Type()
)
cfprMgmtIfAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfAccess.setStatus("current")
_CfprMgmtIfAdminState_Type = CfprMgmtAdminState
_CfprMgmtIfAdminState_Object = MibTableColumn
cfprMgmtIfAdminState = _CfprMgmtIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 5),
    _CfprMgmtIfAdminState_Type()
)
cfprMgmtIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfAdminState.setStatus("current")
_CfprMgmtIfAggrPortId_Type = Gauge32
_CfprMgmtIfAggrPortId_Object = MibTableColumn
cfprMgmtIfAggrPortId = _CfprMgmtIfAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 6),
    _CfprMgmtIfAggrPortId_Type()
)
cfprMgmtIfAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfAggrPortId.setStatus("current")
_CfprMgmtIfChassisId_Type = Gauge32
_CfprMgmtIfChassisId_Object = MibTableColumn
cfprMgmtIfChassisId = _CfprMgmtIfChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 7),
    _CfprMgmtIfChassisId_Type()
)
cfprMgmtIfChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfChassisId.setStatus("current")
_CfprMgmtIfDiscovery_Type = CfprEtherSatelliteConnectionDisc
_CfprMgmtIfDiscovery_Object = MibTableColumn
cfprMgmtIfDiscovery = _CfprMgmtIfDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 8),
    _CfprMgmtIfDiscovery_Type()
)
cfprMgmtIfDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfDiscovery.setStatus("current")
_CfprMgmtIfEpDn_Type = SnmpAdminString
_CfprMgmtIfEpDn_Object = MibTableColumn
cfprMgmtIfEpDn = _CfprMgmtIfEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 9),
    _CfprMgmtIfEpDn_Type()
)
cfprMgmtIfEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfEpDn.setStatus("current")
_CfprMgmtIfExtBroadcast_Type = InetAddressIPv4
_CfprMgmtIfExtBroadcast_Object = MibTableColumn
cfprMgmtIfExtBroadcast = _CfprMgmtIfExtBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 10),
    _CfprMgmtIfExtBroadcast_Type()
)
cfprMgmtIfExtBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfExtBroadcast.setStatus("current")
_CfprMgmtIfExtGw_Type = InetAddressIPv4
_CfprMgmtIfExtGw_Object = MibTableColumn
cfprMgmtIfExtGw = _CfprMgmtIfExtGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 11),
    _CfprMgmtIfExtGw_Type()
)
cfprMgmtIfExtGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfExtGw.setStatus("current")
_CfprMgmtIfExtIp_Type = InetAddressIPv4
_CfprMgmtIfExtIp_Object = MibTableColumn
cfprMgmtIfExtIp = _CfprMgmtIfExtIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 12),
    _CfprMgmtIfExtIp_Type()
)
cfprMgmtIfExtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfExtIp.setStatus("current")
_CfprMgmtIfExtMask_Type = InetAddressIPv4
_CfprMgmtIfExtMask_Object = MibTableColumn
cfprMgmtIfExtMask = _CfprMgmtIfExtMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 13),
    _CfprMgmtIfExtMask_Type()
)
cfprMgmtIfExtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfExtMask.setStatus("current")
_CfprMgmtIfFsmDescr_Type = SnmpAdminString
_CfprMgmtIfFsmDescr_Object = MibTableColumn
cfprMgmtIfFsmDescr = _CfprMgmtIfFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 14),
    _CfprMgmtIfFsmDescr_Type()
)
cfprMgmtIfFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmDescr.setStatus("current")
_CfprMgmtIfFsmPrev_Type = SnmpAdminString
_CfprMgmtIfFsmPrev_Object = MibTableColumn
cfprMgmtIfFsmPrev = _CfprMgmtIfFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 15),
    _CfprMgmtIfFsmPrev_Type()
)
cfprMgmtIfFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmPrev.setStatus("current")
_CfprMgmtIfFsmProgr_Type = Gauge32
_CfprMgmtIfFsmProgr_Object = MibTableColumn
cfprMgmtIfFsmProgr = _CfprMgmtIfFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 16),
    _CfprMgmtIfFsmProgr_Type()
)
cfprMgmtIfFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmProgr.setStatus("current")
_CfprMgmtIfFsmRmtInvErrCode_Type = Gauge32
_CfprMgmtIfFsmRmtInvErrCode_Object = MibTableColumn
cfprMgmtIfFsmRmtInvErrCode = _CfprMgmtIfFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 17),
    _CfprMgmtIfFsmRmtInvErrCode_Type()
)
cfprMgmtIfFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmRmtInvErrCode.setStatus("current")
_CfprMgmtIfFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprMgmtIfFsmRmtInvErrDescr_Object = MibTableColumn
cfprMgmtIfFsmRmtInvErrDescr = _CfprMgmtIfFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 18),
    _CfprMgmtIfFsmRmtInvErrDescr_Type()
)
cfprMgmtIfFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmRmtInvErrDescr.setStatus("current")
_CfprMgmtIfFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtIfFsmRmtInvRslt_Object = MibTableColumn
cfprMgmtIfFsmRmtInvRslt = _CfprMgmtIfFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 19),
    _CfprMgmtIfFsmRmtInvRslt_Type()
)
cfprMgmtIfFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmRmtInvRslt.setStatus("current")
_CfprMgmtIfFsmStageDescr_Type = SnmpAdminString
_CfprMgmtIfFsmStageDescr_Object = MibTableColumn
cfprMgmtIfFsmStageDescr = _CfprMgmtIfFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 20),
    _CfprMgmtIfFsmStageDescr_Type()
)
cfprMgmtIfFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStageDescr.setStatus("current")
_CfprMgmtIfFsmStamp_Type = DateAndTime
_CfprMgmtIfFsmStamp_Object = MibTableColumn
cfprMgmtIfFsmStamp = _CfprMgmtIfFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 21),
    _CfprMgmtIfFsmStamp_Type()
)
cfprMgmtIfFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStamp.setStatus("current")
_CfprMgmtIfFsmStatus_Type = SnmpAdminString
_CfprMgmtIfFsmStatus_Object = MibTableColumn
cfprMgmtIfFsmStatus = _CfprMgmtIfFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 22),
    _CfprMgmtIfFsmStatus_Type()
)
cfprMgmtIfFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStatus.setStatus("current")
_CfprMgmtIfFsmTry_Type = Gauge32
_CfprMgmtIfFsmTry_Object = MibTableColumn
cfprMgmtIfFsmTry = _CfprMgmtIfFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 23),
    _CfprMgmtIfFsmTry_Type()
)
cfprMgmtIfFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmTry.setStatus("current")
_CfprMgmtIfId_Type = Gauge32
_CfprMgmtIfId_Object = MibTableColumn
cfprMgmtIfId = _CfprMgmtIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 24),
    _CfprMgmtIfId_Type()
)
cfprMgmtIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfId.setStatus("current")
_CfprMgmtIfIfRole_Type = CfprNetworkPortRole
_CfprMgmtIfIfRole_Object = MibTableColumn
cfprMgmtIfIfRole = _CfprMgmtIfIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 25),
    _CfprMgmtIfIfRole_Type()
)
cfprMgmtIfIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfIfRole.setStatus("current")
_CfprMgmtIfIfType_Type = CfprNetworkPhysEpIfType
_CfprMgmtIfIfType_Object = MibTableColumn
cfprMgmtIfIfType = _CfprMgmtIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 26),
    _CfprMgmtIfIfType_Type()
)
cfprMgmtIfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfIfType.setStatus("current")
_CfprMgmtIfIp_Type = InetAddressIPv4
_CfprMgmtIfIp_Object = MibTableColumn
cfprMgmtIfIp = _CfprMgmtIfIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 27),
    _CfprMgmtIfIp_Type()
)
cfprMgmtIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfIp.setStatus("current")
_CfprMgmtIfLocale_Type = CfprNetworkLocale
_CfprMgmtIfLocale_Object = MibTableColumn
cfprMgmtIfLocale = _CfprMgmtIfLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 28),
    _CfprMgmtIfLocale_Type()
)
cfprMgmtIfLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfLocale.setStatus("current")
_CfprMgmtIfMac_Type = MacAddress
_CfprMgmtIfMac_Object = MibTableColumn
cfprMgmtIfMac = _CfprMgmtIfMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 29),
    _CfprMgmtIfMac_Type()
)
cfprMgmtIfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfMac.setStatus("current")
_CfprMgmtIfMask_Type = InetAddressIPv4
_CfprMgmtIfMask_Object = MibTableColumn
cfprMgmtIfMask = _CfprMgmtIfMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 30),
    _CfprMgmtIfMask_Type()
)
cfprMgmtIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfMask.setStatus("current")
_CfprMgmtIfName_Type = SnmpAdminString
_CfprMgmtIfName_Object = MibTableColumn
cfprMgmtIfName = _CfprMgmtIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 31),
    _CfprMgmtIfName_Type()
)
cfprMgmtIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfName.setStatus("current")
_CfprMgmtIfPeerAggrPortId_Type = Gauge32
_CfprMgmtIfPeerAggrPortId_Object = MibTableColumn
cfprMgmtIfPeerAggrPortId = _CfprMgmtIfPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 32),
    _CfprMgmtIfPeerAggrPortId_Type()
)
cfprMgmtIfPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfPeerAggrPortId.setStatus("current")
_CfprMgmtIfPeerChassisId_Type = Gauge32
_CfprMgmtIfPeerChassisId_Object = MibTableColumn
cfprMgmtIfPeerChassisId = _CfprMgmtIfPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 33),
    _CfprMgmtIfPeerChassisId_Type()
)
cfprMgmtIfPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfPeerChassisId.setStatus("current")
_CfprMgmtIfPeerDn_Type = SnmpAdminString
_CfprMgmtIfPeerDn_Object = MibTableColumn
cfprMgmtIfPeerDn = _CfprMgmtIfPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 34),
    _CfprMgmtIfPeerDn_Type()
)
cfprMgmtIfPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfPeerDn.setStatus("current")
_CfprMgmtIfPeerPortId_Type = Gauge32
_CfprMgmtIfPeerPortId_Object = MibTableColumn
cfprMgmtIfPeerPortId = _CfprMgmtIfPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 35),
    _CfprMgmtIfPeerPortId_Type()
)
cfprMgmtIfPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfPeerPortId.setStatus("current")
_CfprMgmtIfPeerSlotId_Type = Gauge32
_CfprMgmtIfPeerSlotId_Object = MibTableColumn
cfprMgmtIfPeerSlotId = _CfprMgmtIfPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 36),
    _CfprMgmtIfPeerSlotId_Type()
)
cfprMgmtIfPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfPeerSlotId.setStatus("current")
_CfprMgmtIfPortId_Type = Gauge32
_CfprMgmtIfPortId_Object = MibTableColumn
cfprMgmtIfPortId = _CfprMgmtIfPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 37),
    _CfprMgmtIfPortId_Type()
)
cfprMgmtIfPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfPortId.setStatus("current")
_CfprMgmtIfSlotId_Type = Gauge32
_CfprMgmtIfSlotId_Object = MibTableColumn
cfprMgmtIfSlotId = _CfprMgmtIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 38),
    _CfprMgmtIfSlotId_Type()
)
cfprMgmtIfSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfSlotId.setStatus("current")
_CfprMgmtIfStateQual_Type = CfprMgmtStateQual
_CfprMgmtIfStateQual_Object = MibTableColumn
cfprMgmtIfStateQual = _CfprMgmtIfStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 39),
    _CfprMgmtIfStateQual_Type()
)
cfprMgmtIfStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfStateQual.setStatus("current")
_CfprMgmtIfSubject_Type = CfprMgmtSubject
_CfprMgmtIfSubject_Object = MibTableColumn
cfprMgmtIfSubject = _CfprMgmtIfSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 40),
    _CfprMgmtIfSubject_Type()
)
cfprMgmtIfSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfSubject.setStatus("current")
_CfprMgmtIfSwitchId_Type = CfprNetworkSwitchId
_CfprMgmtIfSwitchId_Object = MibTableColumn
cfprMgmtIfSwitchId = _CfprMgmtIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 41),
    _CfprMgmtIfSwitchId_Type()
)
cfprMgmtIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfSwitchId.setStatus("current")
_CfprMgmtIfTransport_Type = CfprNetworkTransport
_CfprMgmtIfTransport_Object = MibTableColumn
cfprMgmtIfTransport = _CfprMgmtIfTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 42),
    _CfprMgmtIfTransport_Type()
)
cfprMgmtIfTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfTransport.setStatus("current")
_CfprMgmtIfType_Type = CfprNetworkConnectionType
_CfprMgmtIfType_Object = MibTableColumn
cfprMgmtIfType = _CfprMgmtIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 43),
    _CfprMgmtIfType_Type()
)
cfprMgmtIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfType.setStatus("current")
_CfprMgmtIfVnet_Type = Gauge32
_CfprMgmtIfVnet_Object = MibTableColumn
cfprMgmtIfVnet = _CfprMgmtIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 31, 1, 44),
    _CfprMgmtIfVnet_Type()
)
cfprMgmtIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfVnet.setStatus("current")
_CfprMgmtIfFsmTable_Object = MibTable
cfprMgmtIfFsmTable = _CfprMgmtIfFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32)
)
if mibBuilder.loadTexts:
    cfprMgmtIfFsmTable.setStatus("current")
_CfprMgmtIfFsmEntry_Object = MibTableRow
cfprMgmtIfFsmEntry = _CfprMgmtIfFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32, 1)
)
cfprMgmtIfFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtIfFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtIfFsmEntry.setStatus("current")
_CfprMgmtIfFsmInstanceId_Type = CfprManagedObjectId
_CfprMgmtIfFsmInstanceId_Object = MibTableColumn
cfprMgmtIfFsmInstanceId = _CfprMgmtIfFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32, 1, 1),
    _CfprMgmtIfFsmInstanceId_Type()
)
cfprMgmtIfFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmInstanceId.setStatus("current")
_CfprMgmtIfFsmDn_Type = CfprManagedObjectDn
_CfprMgmtIfFsmDn_Object = MibTableColumn
cfprMgmtIfFsmDn = _CfprMgmtIfFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32, 1, 2),
    _CfprMgmtIfFsmDn_Type()
)
cfprMgmtIfFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmDn.setStatus("current")
_CfprMgmtIfFsmRn_Type = SnmpAdminString
_CfprMgmtIfFsmRn_Object = MibTableColumn
cfprMgmtIfFsmRn = _CfprMgmtIfFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32, 1, 3),
    _CfprMgmtIfFsmRn_Type()
)
cfprMgmtIfFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmRn.setStatus("current")
_CfprMgmtIfFsmCompletionTime_Type = DateAndTime
_CfprMgmtIfFsmCompletionTime_Object = MibTableColumn
cfprMgmtIfFsmCompletionTime = _CfprMgmtIfFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32, 1, 4),
    _CfprMgmtIfFsmCompletionTime_Type()
)
cfprMgmtIfFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmCompletionTime.setStatus("current")
_CfprMgmtIfFsmCurrentFsm_Type = CfprMgmtIfFsmCurrentFsm
_CfprMgmtIfFsmCurrentFsm_Object = MibTableColumn
cfprMgmtIfFsmCurrentFsm = _CfprMgmtIfFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32, 1, 5),
    _CfprMgmtIfFsmCurrentFsm_Type()
)
cfprMgmtIfFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmCurrentFsm.setStatus("current")
_CfprMgmtIfFsmDescrData_Type = SnmpAdminString
_CfprMgmtIfFsmDescrData_Object = MibTableColumn
cfprMgmtIfFsmDescrData = _CfprMgmtIfFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32, 1, 6),
    _CfprMgmtIfFsmDescrData_Type()
)
cfprMgmtIfFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmDescrData.setStatus("current")
_CfprMgmtIfFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtIfFsmFsmStatus_Object = MibTableColumn
cfprMgmtIfFsmFsmStatus = _CfprMgmtIfFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32, 1, 7),
    _CfprMgmtIfFsmFsmStatus_Type()
)
cfprMgmtIfFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmFsmStatus.setStatus("current")
_CfprMgmtIfFsmProgress_Type = Gauge32
_CfprMgmtIfFsmProgress_Object = MibTableColumn
cfprMgmtIfFsmProgress = _CfprMgmtIfFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32, 1, 8),
    _CfprMgmtIfFsmProgress_Type()
)
cfprMgmtIfFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmProgress.setStatus("current")
_CfprMgmtIfFsmRmtErrCode_Type = Gauge32
_CfprMgmtIfFsmRmtErrCode_Object = MibTableColumn
cfprMgmtIfFsmRmtErrCode = _CfprMgmtIfFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32, 1, 9),
    _CfprMgmtIfFsmRmtErrCode_Type()
)
cfprMgmtIfFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmRmtErrCode.setStatus("current")
_CfprMgmtIfFsmRmtErrDescr_Type = SnmpAdminString
_CfprMgmtIfFsmRmtErrDescr_Object = MibTableColumn
cfprMgmtIfFsmRmtErrDescr = _CfprMgmtIfFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32, 1, 10),
    _CfprMgmtIfFsmRmtErrDescr_Type()
)
cfprMgmtIfFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmRmtErrDescr.setStatus("current")
_CfprMgmtIfFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtIfFsmRmtRslt_Object = MibTableColumn
cfprMgmtIfFsmRmtRslt = _CfprMgmtIfFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 32, 1, 11),
    _CfprMgmtIfFsmRmtRslt_Type()
)
cfprMgmtIfFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmRmtRslt.setStatus("current")
_CfprMgmtIfFsmStageTable_Object = MibTable
cfprMgmtIfFsmStageTable = _CfprMgmtIfFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 33)
)
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStageTable.setStatus("current")
_CfprMgmtIfFsmStageEntry_Object = MibTableRow
cfprMgmtIfFsmStageEntry = _CfprMgmtIfFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 33, 1)
)
cfprMgmtIfFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtIfFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStageEntry.setStatus("current")
_CfprMgmtIfFsmStageInstanceId_Type = CfprManagedObjectId
_CfprMgmtIfFsmStageInstanceId_Object = MibTableColumn
cfprMgmtIfFsmStageInstanceId = _CfprMgmtIfFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 33, 1, 1),
    _CfprMgmtIfFsmStageInstanceId_Type()
)
cfprMgmtIfFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStageInstanceId.setStatus("current")
_CfprMgmtIfFsmStageDn_Type = CfprManagedObjectDn
_CfprMgmtIfFsmStageDn_Object = MibTableColumn
cfprMgmtIfFsmStageDn = _CfprMgmtIfFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 33, 1, 2),
    _CfprMgmtIfFsmStageDn_Type()
)
cfprMgmtIfFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStageDn.setStatus("current")
_CfprMgmtIfFsmStageRn_Type = SnmpAdminString
_CfprMgmtIfFsmStageRn_Object = MibTableColumn
cfprMgmtIfFsmStageRn = _CfprMgmtIfFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 33, 1, 3),
    _CfprMgmtIfFsmStageRn_Type()
)
cfprMgmtIfFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStageRn.setStatus("current")
_CfprMgmtIfFsmStageDescrData_Type = SnmpAdminString
_CfprMgmtIfFsmStageDescrData_Object = MibTableColumn
cfprMgmtIfFsmStageDescrData = _CfprMgmtIfFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 33, 1, 4),
    _CfprMgmtIfFsmStageDescrData_Type()
)
cfprMgmtIfFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStageDescrData.setStatus("current")
_CfprMgmtIfFsmStageLastUpdateTime_Type = DateAndTime
_CfprMgmtIfFsmStageLastUpdateTime_Object = MibTableColumn
cfprMgmtIfFsmStageLastUpdateTime = _CfprMgmtIfFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 33, 1, 5),
    _CfprMgmtIfFsmStageLastUpdateTime_Type()
)
cfprMgmtIfFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStageLastUpdateTime.setStatus("current")
_CfprMgmtIfFsmStageName_Type = CfprMgmtIfFsmStageName
_CfprMgmtIfFsmStageName_Object = MibTableColumn
cfprMgmtIfFsmStageName = _CfprMgmtIfFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 33, 1, 6),
    _CfprMgmtIfFsmStageName_Type()
)
cfprMgmtIfFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStageName.setStatus("current")
_CfprMgmtIfFsmStageOrder_Type = Gauge32
_CfprMgmtIfFsmStageOrder_Object = MibTableColumn
cfprMgmtIfFsmStageOrder = _CfprMgmtIfFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 33, 1, 7),
    _CfprMgmtIfFsmStageOrder_Type()
)
cfprMgmtIfFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStageOrder.setStatus("current")
_CfprMgmtIfFsmStageRetry_Type = Gauge32
_CfprMgmtIfFsmStageRetry_Object = MibTableColumn
cfprMgmtIfFsmStageRetry = _CfprMgmtIfFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 33, 1, 8),
    _CfprMgmtIfFsmStageRetry_Type()
)
cfprMgmtIfFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStageRetry.setStatus("current")
_CfprMgmtIfFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtIfFsmStageStageStatus_Object = MibTableColumn
cfprMgmtIfFsmStageStageStatus = _CfprMgmtIfFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 33, 1, 9),
    _CfprMgmtIfFsmStageStageStatus_Type()
)
cfprMgmtIfFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmStageStageStatus.setStatus("current")
_CfprMgmtIfFsmTaskTable_Object = MibTable
cfprMgmtIfFsmTaskTable = _CfprMgmtIfFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 34)
)
if mibBuilder.loadTexts:
    cfprMgmtIfFsmTaskTable.setStatus("current")
_CfprMgmtIfFsmTaskEntry_Object = MibTableRow
cfprMgmtIfFsmTaskEntry = _CfprMgmtIfFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 34, 1)
)
cfprMgmtIfFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtIfFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtIfFsmTaskEntry.setStatus("current")
_CfprMgmtIfFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprMgmtIfFsmTaskInstanceId_Object = MibTableColumn
cfprMgmtIfFsmTaskInstanceId = _CfprMgmtIfFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 34, 1, 1),
    _CfprMgmtIfFsmTaskInstanceId_Type()
)
cfprMgmtIfFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmTaskInstanceId.setStatus("current")
_CfprMgmtIfFsmTaskDn_Type = CfprManagedObjectDn
_CfprMgmtIfFsmTaskDn_Object = MibTableColumn
cfprMgmtIfFsmTaskDn = _CfprMgmtIfFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 34, 1, 2),
    _CfprMgmtIfFsmTaskDn_Type()
)
cfprMgmtIfFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmTaskDn.setStatus("current")
_CfprMgmtIfFsmTaskRn_Type = SnmpAdminString
_CfprMgmtIfFsmTaskRn_Object = MibTableColumn
cfprMgmtIfFsmTaskRn = _CfprMgmtIfFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 34, 1, 3),
    _CfprMgmtIfFsmTaskRn_Type()
)
cfprMgmtIfFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmTaskRn.setStatus("current")
_CfprMgmtIfFsmTaskCompletion_Type = CfprFsmCompletion
_CfprMgmtIfFsmTaskCompletion_Object = MibTableColumn
cfprMgmtIfFsmTaskCompletion = _CfprMgmtIfFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 34, 1, 4),
    _CfprMgmtIfFsmTaskCompletion_Type()
)
cfprMgmtIfFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmTaskCompletion.setStatus("current")
_CfprMgmtIfFsmTaskFlags_Type = CfprFsmFlags
_CfprMgmtIfFsmTaskFlags_Object = MibTableColumn
cfprMgmtIfFsmTaskFlags = _CfprMgmtIfFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 34, 1, 5),
    _CfprMgmtIfFsmTaskFlags_Type()
)
cfprMgmtIfFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmTaskFlags.setStatus("current")
_CfprMgmtIfFsmTaskItem_Type = CfprMgmtIfFsmTaskItem
_CfprMgmtIfFsmTaskItem_Object = MibTableColumn
cfprMgmtIfFsmTaskItem = _CfprMgmtIfFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 34, 1, 6),
    _CfprMgmtIfFsmTaskItem_Type()
)
cfprMgmtIfFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmTaskItem.setStatus("current")
_CfprMgmtIfFsmTaskSeqId_Type = Gauge32
_CfprMgmtIfFsmTaskSeqId_Object = MibTableColumn
cfprMgmtIfFsmTaskSeqId = _CfprMgmtIfFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 34, 1, 7),
    _CfprMgmtIfFsmTaskSeqId_Type()
)
cfprMgmtIfFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIfFsmTaskSeqId.setStatus("current")
_CfprMgmtImporterTable_Object = MibTable
cfprMgmtImporterTable = _CfprMgmtImporterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35)
)
if mibBuilder.loadTexts:
    cfprMgmtImporterTable.setStatus("current")
_CfprMgmtImporterEntry_Object = MibTableRow
cfprMgmtImporterEntry = _CfprMgmtImporterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1)
)
cfprMgmtImporterEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtImporterInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtImporterEntry.setStatus("current")
_CfprMgmtImporterInstanceId_Type = CfprManagedObjectId
_CfprMgmtImporterInstanceId_Object = MibTableColumn
cfprMgmtImporterInstanceId = _CfprMgmtImporterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 1),
    _CfprMgmtImporterInstanceId_Type()
)
cfprMgmtImporterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtImporterInstanceId.setStatus("current")
_CfprMgmtImporterDn_Type = CfprManagedObjectDn
_CfprMgmtImporterDn_Object = MibTableColumn
cfprMgmtImporterDn = _CfprMgmtImporterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 2),
    _CfprMgmtImporterDn_Type()
)
cfprMgmtImporterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterDn.setStatus("current")
_CfprMgmtImporterRn_Type = SnmpAdminString
_CfprMgmtImporterRn_Object = MibTableColumn
cfprMgmtImporterRn = _CfprMgmtImporterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 3),
    _CfprMgmtImporterRn_Type()
)
cfprMgmtImporterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterRn.setStatus("current")
_CfprMgmtImporterAction_Type = CfprMgmtImportAction
_CfprMgmtImporterAction_Object = MibTableColumn
cfprMgmtImporterAction = _CfprMgmtImporterAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 4),
    _CfprMgmtImporterAction_Type()
)
cfprMgmtImporterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterAction.setStatus("current")
_CfprMgmtImporterAdminState_Type = CfprCommClientAdminState
_CfprMgmtImporterAdminState_Object = MibTableColumn
cfprMgmtImporterAdminState = _CfprMgmtImporterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 5),
    _CfprMgmtImporterAdminState_Type()
)
cfprMgmtImporterAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterAdminState.setStatus("current")
_CfprMgmtImporterDescr_Type = SnmpAdminString
_CfprMgmtImporterDescr_Object = MibTableColumn
cfprMgmtImporterDescr = _CfprMgmtImporterDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 6),
    _CfprMgmtImporterDescr_Type()
)
cfprMgmtImporterDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterDescr.setStatus("current")
_CfprMgmtImporterFsmDescr_Type = SnmpAdminString
_CfprMgmtImporterFsmDescr_Object = MibTableColumn
cfprMgmtImporterFsmDescr = _CfprMgmtImporterFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 7),
    _CfprMgmtImporterFsmDescr_Type()
)
cfprMgmtImporterFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmDescr.setStatus("current")
_CfprMgmtImporterFsmPrev_Type = SnmpAdminString
_CfprMgmtImporterFsmPrev_Object = MibTableColumn
cfprMgmtImporterFsmPrev = _CfprMgmtImporterFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 8),
    _CfprMgmtImporterFsmPrev_Type()
)
cfprMgmtImporterFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmPrev.setStatus("current")
_CfprMgmtImporterFsmProgr_Type = Gauge32
_CfprMgmtImporterFsmProgr_Object = MibTableColumn
cfprMgmtImporterFsmProgr = _CfprMgmtImporterFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 9),
    _CfprMgmtImporterFsmProgr_Type()
)
cfprMgmtImporterFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmProgr.setStatus("current")
_CfprMgmtImporterFsmRmtInvErrCode_Type = Gauge32
_CfprMgmtImporterFsmRmtInvErrCode_Object = MibTableColumn
cfprMgmtImporterFsmRmtInvErrCode = _CfprMgmtImporterFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 10),
    _CfprMgmtImporterFsmRmtInvErrCode_Type()
)
cfprMgmtImporterFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmRmtInvErrCode.setStatus("current")
_CfprMgmtImporterFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprMgmtImporterFsmRmtInvErrDescr_Object = MibTableColumn
cfprMgmtImporterFsmRmtInvErrDescr = _CfprMgmtImporterFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 11),
    _CfprMgmtImporterFsmRmtInvErrDescr_Type()
)
cfprMgmtImporterFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmRmtInvErrDescr.setStatus("current")
_CfprMgmtImporterFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtImporterFsmRmtInvRslt_Object = MibTableColumn
cfprMgmtImporterFsmRmtInvRslt = _CfprMgmtImporterFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 12),
    _CfprMgmtImporterFsmRmtInvRslt_Type()
)
cfprMgmtImporterFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmRmtInvRslt.setStatus("current")
_CfprMgmtImporterFsmStageDescr_Type = SnmpAdminString
_CfprMgmtImporterFsmStageDescr_Object = MibTableColumn
cfprMgmtImporterFsmStageDescr = _CfprMgmtImporterFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 13),
    _CfprMgmtImporterFsmStageDescr_Type()
)
cfprMgmtImporterFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStageDescr.setStatus("current")
_CfprMgmtImporterFsmStamp_Type = DateAndTime
_CfprMgmtImporterFsmStamp_Object = MibTableColumn
cfprMgmtImporterFsmStamp = _CfprMgmtImporterFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 14),
    _CfprMgmtImporterFsmStamp_Type()
)
cfprMgmtImporterFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStamp.setStatus("current")
_CfprMgmtImporterFsmStatus_Type = SnmpAdminString
_CfprMgmtImporterFsmStatus_Object = MibTableColumn
cfprMgmtImporterFsmStatus = _CfprMgmtImporterFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 15),
    _CfprMgmtImporterFsmStatus_Type()
)
cfprMgmtImporterFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStatus.setStatus("current")
_CfprMgmtImporterFsmTry_Type = Gauge32
_CfprMgmtImporterFsmTry_Object = MibTableColumn
cfprMgmtImporterFsmTry = _CfprMgmtImporterFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 16),
    _CfprMgmtImporterFsmTry_Type()
)
cfprMgmtImporterFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmTry.setStatus("current")
_CfprMgmtImporterHostname_Type = SnmpAdminString
_CfprMgmtImporterHostname_Object = MibTableColumn
cfprMgmtImporterHostname = _CfprMgmtImporterHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 17),
    _CfprMgmtImporterHostname_Type()
)
cfprMgmtImporterHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterHostname.setStatus("current")
_CfprMgmtImporterIntId_Type = SnmpAdminString
_CfprMgmtImporterIntId_Object = MibTableColumn
cfprMgmtImporterIntId = _CfprMgmtImporterIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 18),
    _CfprMgmtImporterIntId_Type()
)
cfprMgmtImporterIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterIntId.setStatus("current")
_CfprMgmtImporterName_Type = SnmpAdminString
_CfprMgmtImporterName_Object = MibTableColumn
cfprMgmtImporterName = _CfprMgmtImporterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 19),
    _CfprMgmtImporterName_Type()
)
cfprMgmtImporterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterName.setStatus("current")
_CfprMgmtImporterOperStatus_Type = CfprMgmtImportStatus
_CfprMgmtImporterOperStatus_Object = MibTableColumn
cfprMgmtImporterOperStatus = _CfprMgmtImporterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 20),
    _CfprMgmtImporterOperStatus_Type()
)
cfprMgmtImporterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterOperStatus.setStatus("current")
_CfprMgmtImporterPolicyLevel_Type = Gauge32
_CfprMgmtImporterPolicyLevel_Object = MibTableColumn
cfprMgmtImporterPolicyLevel = _CfprMgmtImporterPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 21),
    _CfprMgmtImporterPolicyLevel_Type()
)
cfprMgmtImporterPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterPolicyLevel.setStatus("current")
_CfprMgmtImporterPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprMgmtImporterPolicyOwner_Object = MibTableColumn
cfprMgmtImporterPolicyOwner = _CfprMgmtImporterPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 22),
    _CfprMgmtImporterPolicyOwner_Type()
)
cfprMgmtImporterPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterPolicyOwner.setStatus("current")
_CfprMgmtImporterPostAction_Type = CfprMgmtImporterPostAction
_CfprMgmtImporterPostAction_Object = MibTableColumn
cfprMgmtImporterPostAction = _CfprMgmtImporterPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 23),
    _CfprMgmtImporterPostAction_Type()
)
cfprMgmtImporterPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterPostAction.setStatus("current")
_CfprMgmtImporterProto_Type = CfprMgmtImporterProto
_CfprMgmtImporterProto_Object = MibTableColumn
cfprMgmtImporterProto = _CfprMgmtImporterProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 24),
    _CfprMgmtImporterProto_Type()
)
cfprMgmtImporterProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterProto.setStatus("current")
_CfprMgmtImporterPwd_Type = SnmpAdminString
_CfprMgmtImporterPwd_Object = MibTableColumn
cfprMgmtImporterPwd = _CfprMgmtImporterPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 25),
    _CfprMgmtImporterPwd_Type()
)
cfprMgmtImporterPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterPwd.setStatus("current")
_CfprMgmtImporterRemoteFile_Type = SnmpAdminString
_CfprMgmtImporterRemoteFile_Object = MibTableColumn
cfprMgmtImporterRemoteFile = _CfprMgmtImporterRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 26),
    _CfprMgmtImporterRemoteFile_Type()
)
cfprMgmtImporterRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterRemoteFile.setStatus("current")
_CfprMgmtImporterUser_Type = SnmpAdminString
_CfprMgmtImporterUser_Object = MibTableColumn
cfprMgmtImporterUser = _CfprMgmtImporterUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 27),
    _CfprMgmtImporterUser_Type()
)
cfprMgmtImporterUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterUser.setStatus("current")
_CfprMgmtImporterApplyingBreakoutCfg_Type = TruthValue
_CfprMgmtImporterApplyingBreakoutCfg_Object = MibTableColumn
cfprMgmtImporterApplyingBreakoutCfg = _CfprMgmtImporterApplyingBreakoutCfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 28),
    _CfprMgmtImporterApplyingBreakoutCfg_Type()
)
cfprMgmtImporterApplyingBreakoutCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterApplyingBreakoutCfg.setStatus("current")
_CfprMgmtImporterPort_Type = Gauge32
_CfprMgmtImporterPort_Object = MibTableColumn
cfprMgmtImporterPort = _CfprMgmtImporterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 29),
    _CfprMgmtImporterPort_Type()
)
cfprMgmtImporterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterPort.setStatus("current")
_CfprMgmtImporterErrMsg_Type = SnmpAdminString
_CfprMgmtImporterErrMsg_Object = MibTableColumn
cfprMgmtImporterErrMsg = _CfprMgmtImporterErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 35, 1, 30),
    _CfprMgmtImporterErrMsg_Type()
)
cfprMgmtImporterErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterErrMsg.setStatus("current")
_CfprMgmtImporterFsmTable_Object = MibTable
cfprMgmtImporterFsmTable = _CfprMgmtImporterFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36)
)
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmTable.setStatus("current")
_CfprMgmtImporterFsmEntry_Object = MibTableRow
cfprMgmtImporterFsmEntry = _CfprMgmtImporterFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36, 1)
)
cfprMgmtImporterFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtImporterFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmEntry.setStatus("current")
_CfprMgmtImporterFsmInstanceId_Type = CfprManagedObjectId
_CfprMgmtImporterFsmInstanceId_Object = MibTableColumn
cfprMgmtImporterFsmInstanceId = _CfprMgmtImporterFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36, 1, 1),
    _CfprMgmtImporterFsmInstanceId_Type()
)
cfprMgmtImporterFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmInstanceId.setStatus("current")
_CfprMgmtImporterFsmDn_Type = CfprManagedObjectDn
_CfprMgmtImporterFsmDn_Object = MibTableColumn
cfprMgmtImporterFsmDn = _CfprMgmtImporterFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36, 1, 2),
    _CfprMgmtImporterFsmDn_Type()
)
cfprMgmtImporterFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmDn.setStatus("current")
_CfprMgmtImporterFsmRn_Type = SnmpAdminString
_CfprMgmtImporterFsmRn_Object = MibTableColumn
cfprMgmtImporterFsmRn = _CfprMgmtImporterFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36, 1, 3),
    _CfprMgmtImporterFsmRn_Type()
)
cfprMgmtImporterFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmRn.setStatus("current")
_CfprMgmtImporterFsmCompletionTime_Type = DateAndTime
_CfprMgmtImporterFsmCompletionTime_Object = MibTableColumn
cfprMgmtImporterFsmCompletionTime = _CfprMgmtImporterFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36, 1, 4),
    _CfprMgmtImporterFsmCompletionTime_Type()
)
cfprMgmtImporterFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmCompletionTime.setStatus("current")
_CfprMgmtImporterFsmCurrentFsm_Type = CfprMgmtImporterFsmCurrentFsm
_CfprMgmtImporterFsmCurrentFsm_Object = MibTableColumn
cfprMgmtImporterFsmCurrentFsm = _CfprMgmtImporterFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36, 1, 5),
    _CfprMgmtImporterFsmCurrentFsm_Type()
)
cfprMgmtImporterFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmCurrentFsm.setStatus("current")
_CfprMgmtImporterFsmDescrData_Type = SnmpAdminString
_CfprMgmtImporterFsmDescrData_Object = MibTableColumn
cfprMgmtImporterFsmDescrData = _CfprMgmtImporterFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36, 1, 6),
    _CfprMgmtImporterFsmDescrData_Type()
)
cfprMgmtImporterFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmDescrData.setStatus("current")
_CfprMgmtImporterFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtImporterFsmFsmStatus_Object = MibTableColumn
cfprMgmtImporterFsmFsmStatus = _CfprMgmtImporterFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36, 1, 7),
    _CfprMgmtImporterFsmFsmStatus_Type()
)
cfprMgmtImporterFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmFsmStatus.setStatus("current")
_CfprMgmtImporterFsmProgress_Type = Gauge32
_CfprMgmtImporterFsmProgress_Object = MibTableColumn
cfprMgmtImporterFsmProgress = _CfprMgmtImporterFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36, 1, 8),
    _CfprMgmtImporterFsmProgress_Type()
)
cfprMgmtImporterFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmProgress.setStatus("current")
_CfprMgmtImporterFsmRmtErrCode_Type = Gauge32
_CfprMgmtImporterFsmRmtErrCode_Object = MibTableColumn
cfprMgmtImporterFsmRmtErrCode = _CfprMgmtImporterFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36, 1, 9),
    _CfprMgmtImporterFsmRmtErrCode_Type()
)
cfprMgmtImporterFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmRmtErrCode.setStatus("current")
_CfprMgmtImporterFsmRmtErrDescr_Type = SnmpAdminString
_CfprMgmtImporterFsmRmtErrDescr_Object = MibTableColumn
cfprMgmtImporterFsmRmtErrDescr = _CfprMgmtImporterFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36, 1, 10),
    _CfprMgmtImporterFsmRmtErrDescr_Type()
)
cfprMgmtImporterFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmRmtErrDescr.setStatus("current")
_CfprMgmtImporterFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprMgmtImporterFsmRmtRslt_Object = MibTableColumn
cfprMgmtImporterFsmRmtRslt = _CfprMgmtImporterFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 36, 1, 11),
    _CfprMgmtImporterFsmRmtRslt_Type()
)
cfprMgmtImporterFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmRmtRslt.setStatus("current")
_CfprMgmtImporterFsmStageTable_Object = MibTable
cfprMgmtImporterFsmStageTable = _CfprMgmtImporterFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 37)
)
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStageTable.setStatus("current")
_CfprMgmtImporterFsmStageEntry_Object = MibTableRow
cfprMgmtImporterFsmStageEntry = _CfprMgmtImporterFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 37, 1)
)
cfprMgmtImporterFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtImporterFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStageEntry.setStatus("current")
_CfprMgmtImporterFsmStageInstanceId_Type = CfprManagedObjectId
_CfprMgmtImporterFsmStageInstanceId_Object = MibTableColumn
cfprMgmtImporterFsmStageInstanceId = _CfprMgmtImporterFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 37, 1, 1),
    _CfprMgmtImporterFsmStageInstanceId_Type()
)
cfprMgmtImporterFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStageInstanceId.setStatus("current")
_CfprMgmtImporterFsmStageDn_Type = CfprManagedObjectDn
_CfprMgmtImporterFsmStageDn_Object = MibTableColumn
cfprMgmtImporterFsmStageDn = _CfprMgmtImporterFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 37, 1, 2),
    _CfprMgmtImporterFsmStageDn_Type()
)
cfprMgmtImporterFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStageDn.setStatus("current")
_CfprMgmtImporterFsmStageRn_Type = SnmpAdminString
_CfprMgmtImporterFsmStageRn_Object = MibTableColumn
cfprMgmtImporterFsmStageRn = _CfprMgmtImporterFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 37, 1, 3),
    _CfprMgmtImporterFsmStageRn_Type()
)
cfprMgmtImporterFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStageRn.setStatus("current")
_CfprMgmtImporterFsmStageDescrData_Type = SnmpAdminString
_CfprMgmtImporterFsmStageDescrData_Object = MibTableColumn
cfprMgmtImporterFsmStageDescrData = _CfprMgmtImporterFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 37, 1, 4),
    _CfprMgmtImporterFsmStageDescrData_Type()
)
cfprMgmtImporterFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStageDescrData.setStatus("current")
_CfprMgmtImporterFsmStageLastUpdateTime_Type = DateAndTime
_CfprMgmtImporterFsmStageLastUpdateTime_Object = MibTableColumn
cfprMgmtImporterFsmStageLastUpdateTime = _CfprMgmtImporterFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 37, 1, 5),
    _CfprMgmtImporterFsmStageLastUpdateTime_Type()
)
cfprMgmtImporterFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStageLastUpdateTime.setStatus("current")
_CfprMgmtImporterFsmStageName_Type = CfprMgmtImporterFsmStageName
_CfprMgmtImporterFsmStageName_Object = MibTableColumn
cfprMgmtImporterFsmStageName = _CfprMgmtImporterFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 37, 1, 6),
    _CfprMgmtImporterFsmStageName_Type()
)
cfprMgmtImporterFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStageName.setStatus("current")
_CfprMgmtImporterFsmStageOrder_Type = Gauge32
_CfprMgmtImporterFsmStageOrder_Object = MibTableColumn
cfprMgmtImporterFsmStageOrder = _CfprMgmtImporterFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 37, 1, 7),
    _CfprMgmtImporterFsmStageOrder_Type()
)
cfprMgmtImporterFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStageOrder.setStatus("current")
_CfprMgmtImporterFsmStageRetry_Type = Gauge32
_CfprMgmtImporterFsmStageRetry_Object = MibTableColumn
cfprMgmtImporterFsmStageRetry = _CfprMgmtImporterFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 37, 1, 8),
    _CfprMgmtImporterFsmStageRetry_Type()
)
cfprMgmtImporterFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStageRetry.setStatus("current")
_CfprMgmtImporterFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprMgmtImporterFsmStageStageStatus_Object = MibTableColumn
cfprMgmtImporterFsmStageStageStatus = _CfprMgmtImporterFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 37, 1, 9),
    _CfprMgmtImporterFsmStageStageStatus_Type()
)
cfprMgmtImporterFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmStageStageStatus.setStatus("current")
_CfprMgmtImporterFsmTaskTable_Object = MibTable
cfprMgmtImporterFsmTaskTable = _CfprMgmtImporterFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 38)
)
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmTaskTable.setStatus("current")
_CfprMgmtImporterFsmTaskEntry_Object = MibTableRow
cfprMgmtImporterFsmTaskEntry = _CfprMgmtImporterFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 38, 1)
)
cfprMgmtImporterFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtImporterFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmTaskEntry.setStatus("current")
_CfprMgmtImporterFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprMgmtImporterFsmTaskInstanceId_Object = MibTableColumn
cfprMgmtImporterFsmTaskInstanceId = _CfprMgmtImporterFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 38, 1, 1),
    _CfprMgmtImporterFsmTaskInstanceId_Type()
)
cfprMgmtImporterFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmTaskInstanceId.setStatus("current")
_CfprMgmtImporterFsmTaskDn_Type = CfprManagedObjectDn
_CfprMgmtImporterFsmTaskDn_Object = MibTableColumn
cfprMgmtImporterFsmTaskDn = _CfprMgmtImporterFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 38, 1, 2),
    _CfprMgmtImporterFsmTaskDn_Type()
)
cfprMgmtImporterFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmTaskDn.setStatus("current")
_CfprMgmtImporterFsmTaskRn_Type = SnmpAdminString
_CfprMgmtImporterFsmTaskRn_Object = MibTableColumn
cfprMgmtImporterFsmTaskRn = _CfprMgmtImporterFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 38, 1, 3),
    _CfprMgmtImporterFsmTaskRn_Type()
)
cfprMgmtImporterFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmTaskRn.setStatus("current")
_CfprMgmtImporterFsmTaskCompletion_Type = CfprFsmCompletion
_CfprMgmtImporterFsmTaskCompletion_Object = MibTableColumn
cfprMgmtImporterFsmTaskCompletion = _CfprMgmtImporterFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 38, 1, 4),
    _CfprMgmtImporterFsmTaskCompletion_Type()
)
cfprMgmtImporterFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmTaskCompletion.setStatus("current")
_CfprMgmtImporterFsmTaskFlags_Type = CfprFsmFlags
_CfprMgmtImporterFsmTaskFlags_Object = MibTableColumn
cfprMgmtImporterFsmTaskFlags = _CfprMgmtImporterFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 38, 1, 5),
    _CfprMgmtImporterFsmTaskFlags_Type()
)
cfprMgmtImporterFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmTaskFlags.setStatus("current")
_CfprMgmtImporterFsmTaskItem_Type = CfprMgmtImporterFsmTaskItem
_CfprMgmtImporterFsmTaskItem_Object = MibTableColumn
cfprMgmtImporterFsmTaskItem = _CfprMgmtImporterFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 38, 1, 6),
    _CfprMgmtImporterFsmTaskItem_Type()
)
cfprMgmtImporterFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmTaskItem.setStatus("current")
_CfprMgmtImporterFsmTaskSeqId_Type = Gauge32
_CfprMgmtImporterFsmTaskSeqId_Object = MibTableColumn
cfprMgmtImporterFsmTaskSeqId = _CfprMgmtImporterFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 38, 1, 7),
    _CfprMgmtImporterFsmTaskSeqId_Type()
)
cfprMgmtImporterFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImporterFsmTaskSeqId.setStatus("current")
_CfprMgmtInbandProfileTable_Object = MibTable
cfprMgmtInbandProfileTable = _CfprMgmtInbandProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 39)
)
if mibBuilder.loadTexts:
    cfprMgmtInbandProfileTable.setStatus("current")
_CfprMgmtInbandProfileEntry_Object = MibTableRow
cfprMgmtInbandProfileEntry = _CfprMgmtInbandProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 39, 1)
)
cfprMgmtInbandProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtInbandProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtInbandProfileEntry.setStatus("current")
_CfprMgmtInbandProfileInstanceId_Type = CfprManagedObjectId
_CfprMgmtInbandProfileInstanceId_Object = MibTableColumn
cfprMgmtInbandProfileInstanceId = _CfprMgmtInbandProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 39, 1, 1),
    _CfprMgmtInbandProfileInstanceId_Type()
)
cfprMgmtInbandProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtInbandProfileInstanceId.setStatus("current")
_CfprMgmtInbandProfileDn_Type = CfprManagedObjectDn
_CfprMgmtInbandProfileDn_Object = MibTableColumn
cfprMgmtInbandProfileDn = _CfprMgmtInbandProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 39, 1, 2),
    _CfprMgmtInbandProfileDn_Type()
)
cfprMgmtInbandProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInbandProfileDn.setStatus("current")
_CfprMgmtInbandProfileRn_Type = SnmpAdminString
_CfprMgmtInbandProfileRn_Object = MibTableColumn
cfprMgmtInbandProfileRn = _CfprMgmtInbandProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 39, 1, 3),
    _CfprMgmtInbandProfileRn_Type()
)
cfprMgmtInbandProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInbandProfileRn.setStatus("current")
_CfprMgmtInbandProfileDefaultVlanName_Type = SnmpAdminString
_CfprMgmtInbandProfileDefaultVlanName_Object = MibTableColumn
cfprMgmtInbandProfileDefaultVlanName = _CfprMgmtInbandProfileDefaultVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 39, 1, 4),
    _CfprMgmtInbandProfileDefaultVlanName_Type()
)
cfprMgmtInbandProfileDefaultVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInbandProfileDefaultVlanName.setStatus("current")
_CfprMgmtInbandProfileName_Type = SnmpAdminString
_CfprMgmtInbandProfileName_Object = MibTableColumn
cfprMgmtInbandProfileName = _CfprMgmtInbandProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 39, 1, 5),
    _CfprMgmtInbandProfileName_Type()
)
cfprMgmtInbandProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInbandProfileName.setStatus("current")
_CfprMgmtInbandProfilePoolName_Type = SnmpAdminString
_CfprMgmtInbandProfilePoolName_Object = MibTableColumn
cfprMgmtInbandProfilePoolName = _CfprMgmtInbandProfilePoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 39, 1, 6),
    _CfprMgmtInbandProfilePoolName_Type()
)
cfprMgmtInbandProfilePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInbandProfilePoolName.setStatus("current")
_CfprMgmtIntAuthPolicyTable_Object = MibTable
cfprMgmtIntAuthPolicyTable = _CfprMgmtIntAuthPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 40)
)
if mibBuilder.loadTexts:
    cfprMgmtIntAuthPolicyTable.setStatus("current")
_CfprMgmtIntAuthPolicyEntry_Object = MibTableRow
cfprMgmtIntAuthPolicyEntry = _CfprMgmtIntAuthPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 40, 1)
)
cfprMgmtIntAuthPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtIntAuthPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtIntAuthPolicyEntry.setStatus("current")
_CfprMgmtIntAuthPolicyInstanceId_Type = CfprManagedObjectId
_CfprMgmtIntAuthPolicyInstanceId_Object = MibTableColumn
cfprMgmtIntAuthPolicyInstanceId = _CfprMgmtIntAuthPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 40, 1, 1),
    _CfprMgmtIntAuthPolicyInstanceId_Type()
)
cfprMgmtIntAuthPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtIntAuthPolicyInstanceId.setStatus("current")
_CfprMgmtIntAuthPolicyDn_Type = CfprManagedObjectDn
_CfprMgmtIntAuthPolicyDn_Object = MibTableColumn
cfprMgmtIntAuthPolicyDn = _CfprMgmtIntAuthPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 40, 1, 2),
    _CfprMgmtIntAuthPolicyDn_Type()
)
cfprMgmtIntAuthPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIntAuthPolicyDn.setStatus("current")
_CfprMgmtIntAuthPolicyRn_Type = SnmpAdminString
_CfprMgmtIntAuthPolicyRn_Object = MibTableColumn
cfprMgmtIntAuthPolicyRn = _CfprMgmtIntAuthPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 40, 1, 3),
    _CfprMgmtIntAuthPolicyRn_Type()
)
cfprMgmtIntAuthPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIntAuthPolicyRn.setStatus("current")
_CfprMgmtIntAuthPolicyMethod_Type = CfprMgmtIntAuthPolicyMethod
_CfprMgmtIntAuthPolicyMethod_Object = MibTableColumn
cfprMgmtIntAuthPolicyMethod = _CfprMgmtIntAuthPolicyMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 40, 1, 4),
    _CfprMgmtIntAuthPolicyMethod_Type()
)
cfprMgmtIntAuthPolicyMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIntAuthPolicyMethod.setStatus("current")
_CfprMgmtIntAuthPolicyName_Type = SnmpAdminString
_CfprMgmtIntAuthPolicyName_Object = MibTableColumn
cfprMgmtIntAuthPolicyName = _CfprMgmtIntAuthPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 40, 1, 5),
    _CfprMgmtIntAuthPolicyName_Type()
)
cfprMgmtIntAuthPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIntAuthPolicyName.setStatus("current")
_CfprMgmtIntAuthPolicyPwd_Type = SnmpAdminString
_CfprMgmtIntAuthPolicyPwd_Object = MibTableColumn
cfprMgmtIntAuthPolicyPwd = _CfprMgmtIntAuthPolicyPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 40, 1, 6),
    _CfprMgmtIntAuthPolicyPwd_Type()
)
cfprMgmtIntAuthPolicyPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtIntAuthPolicyPwd.setStatus("current")
_CfprMgmtInterfaceTable_Object = MibTable
cfprMgmtInterfaceTable = _CfprMgmtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 41)
)
if mibBuilder.loadTexts:
    cfprMgmtInterfaceTable.setStatus("current")
_CfprMgmtInterfaceEntry_Object = MibTableRow
cfprMgmtInterfaceEntry = _CfprMgmtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 41, 1)
)
cfprMgmtInterfaceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtInterfaceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtInterfaceEntry.setStatus("current")
_CfprMgmtInterfaceInstanceId_Type = CfprManagedObjectId
_CfprMgmtInterfaceInstanceId_Object = MibTableColumn
cfprMgmtInterfaceInstanceId = _CfprMgmtInterfaceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 41, 1, 1),
    _CfprMgmtInterfaceInstanceId_Type()
)
cfprMgmtInterfaceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtInterfaceInstanceId.setStatus("current")
_CfprMgmtInterfaceDn_Type = CfprManagedObjectDn
_CfprMgmtInterfaceDn_Object = MibTableColumn
cfprMgmtInterfaceDn = _CfprMgmtInterfaceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 41, 1, 2),
    _CfprMgmtInterfaceDn_Type()
)
cfprMgmtInterfaceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInterfaceDn.setStatus("current")
_CfprMgmtInterfaceRn_Type = SnmpAdminString
_CfprMgmtInterfaceRn_Object = MibTableColumn
cfprMgmtInterfaceRn = _CfprMgmtInterfaceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 41, 1, 3),
    _CfprMgmtInterfaceRn_Type()
)
cfprMgmtInterfaceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInterfaceRn.setStatus("current")
_CfprMgmtInterfaceConfigMessage_Type = SnmpAdminString
_CfprMgmtInterfaceConfigMessage_Object = MibTableColumn
cfprMgmtInterfaceConfigMessage = _CfprMgmtInterfaceConfigMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 41, 1, 4),
    _CfprMgmtInterfaceConfigMessage_Type()
)
cfprMgmtInterfaceConfigMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInterfaceConfigMessage.setStatus("current")
_CfprMgmtInterfaceConfigState_Type = CfprMgmtConfigState
_CfprMgmtInterfaceConfigState_Object = MibTableColumn
cfprMgmtInterfaceConfigState = _CfprMgmtInterfaceConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 41, 1, 5),
    _CfprMgmtInterfaceConfigState_Type()
)
cfprMgmtInterfaceConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInterfaceConfigState.setStatus("current")
_CfprMgmtInterfaceIpV4State_Type = CfprVnicExternalMgmtIPMode
_CfprMgmtInterfaceIpV4State_Object = MibTableColumn
cfprMgmtInterfaceIpV4State = _CfprMgmtInterfaceIpV4State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 41, 1, 6),
    _CfprMgmtInterfaceIpV4State_Type()
)
cfprMgmtInterfaceIpV4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInterfaceIpV4State.setStatus("current")
_CfprMgmtInterfaceIpV6State_Type = CfprVnicExternalMgmtIPMode
_CfprMgmtInterfaceIpV6State_Object = MibTableColumn
cfprMgmtInterfaceIpV6State = _CfprMgmtInterfaceIpV6State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 41, 1, 7),
    _CfprMgmtInterfaceIpV6State_Type()
)
cfprMgmtInterfaceIpV6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInterfaceIpV6State.setStatus("current")
_CfprMgmtInterfaceIsDefaultDerived_Type = TruthValue
_CfprMgmtInterfaceIsDefaultDerived_Object = MibTableColumn
cfprMgmtInterfaceIsDefaultDerived = _CfprMgmtInterfaceIsDefaultDerived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 41, 1, 8),
    _CfprMgmtInterfaceIsDefaultDerived_Type()
)
cfprMgmtInterfaceIsDefaultDerived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInterfaceIsDefaultDerived.setStatus("current")
_CfprMgmtInterfaceMode_Type = CfprMgmtMode
_CfprMgmtInterfaceMode_Object = MibTableColumn
cfprMgmtInterfaceMode = _CfprMgmtInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 41, 1, 9),
    _CfprMgmtInterfaceMode_Type()
)
cfprMgmtInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInterfaceMode.setStatus("current")
_CfprMgmtInterfaceOperState_Type = CfprMgmtOperState
_CfprMgmtInterfaceOperState_Object = MibTableColumn
cfprMgmtInterfaceOperState = _CfprMgmtInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 41, 1, 10),
    _CfprMgmtInterfaceOperState_Type()
)
cfprMgmtInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtInterfaceOperState.setStatus("current")
_CfprMgmtPmonEntryTable_Object = MibTable
cfprMgmtPmonEntryTable = _CfprMgmtPmonEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42)
)
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryTable.setStatus("current")
_CfprMgmtPmonEntryEntry_Object = MibTableRow
cfprMgmtPmonEntryEntry = _CfprMgmtPmonEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1)
)
cfprMgmtPmonEntryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtPmonEntryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryEntry.setStatus("current")
_CfprMgmtPmonEntryInstanceId_Type = CfprManagedObjectId
_CfprMgmtPmonEntryInstanceId_Object = MibTableColumn
cfprMgmtPmonEntryInstanceId = _CfprMgmtPmonEntryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 1),
    _CfprMgmtPmonEntryInstanceId_Type()
)
cfprMgmtPmonEntryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryInstanceId.setStatus("current")
_CfprMgmtPmonEntryDn_Type = CfprManagedObjectDn
_CfprMgmtPmonEntryDn_Object = MibTableColumn
cfprMgmtPmonEntryDn = _CfprMgmtPmonEntryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 2),
    _CfprMgmtPmonEntryDn_Type()
)
cfprMgmtPmonEntryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryDn.setStatus("current")
_CfprMgmtPmonEntryRn_Type = SnmpAdminString
_CfprMgmtPmonEntryRn_Object = MibTableColumn
cfprMgmtPmonEntryRn = _CfprMgmtPmonEntryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 3),
    _CfprMgmtPmonEntryRn_Type()
)
cfprMgmtPmonEntryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryRn.setStatus("current")
_CfprMgmtPmonEntryExitSignal_Type = Gauge32
_CfprMgmtPmonEntryExitSignal_Object = MibTableColumn
cfprMgmtPmonEntryExitSignal = _CfprMgmtPmonEntryExitSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 4),
    _CfprMgmtPmonEntryExitSignal_Type()
)
cfprMgmtPmonEntryExitSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryExitSignal.setStatus("current")
_CfprMgmtPmonEntryFullPathname_Type = SnmpAdminString
_CfprMgmtPmonEntryFullPathname_Object = MibTableColumn
cfprMgmtPmonEntryFullPathname = _CfprMgmtPmonEntryFullPathname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 5),
    _CfprMgmtPmonEntryFullPathname_Type()
)
cfprMgmtPmonEntryFullPathname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryFullPathname.setStatus("current")
_CfprMgmtPmonEntryHeapSize_Type = Unsigned64
_CfprMgmtPmonEntryHeapSize_Object = MibTableColumn
cfprMgmtPmonEntryHeapSize = _CfprMgmtPmonEntryHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 6),
    _CfprMgmtPmonEntryHeapSize_Type()
)
cfprMgmtPmonEntryHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryHeapSize.setStatus("current")
_CfprMgmtPmonEntryHeapSize16Gb_Type = Unsigned64
_CfprMgmtPmonEntryHeapSize16Gb_Object = MibTableColumn
cfprMgmtPmonEntryHeapSize16Gb = _CfprMgmtPmonEntryHeapSize16Gb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 7),
    _CfprMgmtPmonEntryHeapSize16Gb_Type()
)
cfprMgmtPmonEntryHeapSize16Gb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryHeapSize16Gb.setStatus("current")
_CfprMgmtPmonEntryLastExitCode_Type = Gauge32
_CfprMgmtPmonEntryLastExitCode_Object = MibTableColumn
cfprMgmtPmonEntryLastExitCode = _CfprMgmtPmonEntryLastExitCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 8),
    _CfprMgmtPmonEntryLastExitCode_Type()
)
cfprMgmtPmonEntryLastExitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryLastExitCode.setStatus("current")
_CfprMgmtPmonEntryMaxRetries_Type = Gauge32
_CfprMgmtPmonEntryMaxRetries_Object = MibTableColumn
cfprMgmtPmonEntryMaxRetries = _CfprMgmtPmonEntryMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 9),
    _CfprMgmtPmonEntryMaxRetries_Type()
)
cfprMgmtPmonEntryMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryMaxRetries.setStatus("current")
_CfprMgmtPmonEntryName_Type = SnmpAdminString
_CfprMgmtPmonEntryName_Object = MibTableColumn
cfprMgmtPmonEntryName = _CfprMgmtPmonEntryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 10),
    _CfprMgmtPmonEntryName_Type()
)
cfprMgmtPmonEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryName.setStatus("current")
_CfprMgmtPmonEntryRetries_Type = Gauge32
_CfprMgmtPmonEntryRetries_Object = MibTableColumn
cfprMgmtPmonEntryRetries = _CfprMgmtPmonEntryRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 11),
    _CfprMgmtPmonEntryRetries_Type()
)
cfprMgmtPmonEntryRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryRetries.setStatus("current")
_CfprMgmtPmonEntrySpuriousRetries_Type = Gauge32
_CfprMgmtPmonEntrySpuriousRetries_Object = MibTableColumn
cfprMgmtPmonEntrySpuriousRetries = _CfprMgmtPmonEntrySpuriousRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 12),
    _CfprMgmtPmonEntrySpuriousRetries_Type()
)
cfprMgmtPmonEntrySpuriousRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntrySpuriousRetries.setStatus("current")
_CfprMgmtPmonEntryState_Type = CfprMgmtPmonEntryState
_CfprMgmtPmonEntryState_Object = MibTableColumn
cfprMgmtPmonEntryState = _CfprMgmtPmonEntryState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 13),
    _CfprMgmtPmonEntryState_Type()
)
cfprMgmtPmonEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryState.setStatus("current")
_CfprMgmtPmonEntrySwitchId_Type = CfprNetworkSwitchId
_CfprMgmtPmonEntrySwitchId_Object = MibTableColumn
cfprMgmtPmonEntrySwitchId = _CfprMgmtPmonEntrySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 14),
    _CfprMgmtPmonEntrySwitchId_Type()
)
cfprMgmtPmonEntrySwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntrySwitchId.setStatus("current")
_CfprMgmtPmonEntryWorkingDirectory_Type = SnmpAdminString
_CfprMgmtPmonEntryWorkingDirectory_Object = MibTableColumn
cfprMgmtPmonEntryWorkingDirectory = _CfprMgmtPmonEntryWorkingDirectory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 15),
    _CfprMgmtPmonEntryWorkingDirectory_Type()
)
cfprMgmtPmonEntryWorkingDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryWorkingDirectory.setStatus("current")
_CfprMgmtPmonEntryIsProcRestarted_Type = TruthValue
_CfprMgmtPmonEntryIsProcRestarted_Object = MibTableColumn
cfprMgmtPmonEntryIsProcRestarted = _CfprMgmtPmonEntryIsProcRestarted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 42, 1, 16),
    _CfprMgmtPmonEntryIsProcRestarted_Type()
)
cfprMgmtPmonEntryIsProcRestarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtPmonEntryIsProcRestarted.setStatus("current")
_CfprMgmtProfDerivedInterfaceTable_Object = MibTable
cfprMgmtProfDerivedInterfaceTable = _CfprMgmtProfDerivedInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 43)
)
if mibBuilder.loadTexts:
    cfprMgmtProfDerivedInterfaceTable.setStatus("current")
_CfprMgmtProfDerivedInterfaceEntry_Object = MibTableRow
cfprMgmtProfDerivedInterfaceEntry = _CfprMgmtProfDerivedInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 43, 1)
)
cfprMgmtProfDerivedInterfaceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtProfDerivedInterfaceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtProfDerivedInterfaceEntry.setStatus("current")
_CfprMgmtProfDerivedInterfaceInstanceId_Type = CfprManagedObjectId
_CfprMgmtProfDerivedInterfaceInstanceId_Object = MibTableColumn
cfprMgmtProfDerivedInterfaceInstanceId = _CfprMgmtProfDerivedInterfaceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 43, 1, 1),
    _CfprMgmtProfDerivedInterfaceInstanceId_Type()
)
cfprMgmtProfDerivedInterfaceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtProfDerivedInterfaceInstanceId.setStatus("current")
_CfprMgmtProfDerivedInterfaceDn_Type = CfprManagedObjectDn
_CfprMgmtProfDerivedInterfaceDn_Object = MibTableColumn
cfprMgmtProfDerivedInterfaceDn = _CfprMgmtProfDerivedInterfaceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 43, 1, 2),
    _CfprMgmtProfDerivedInterfaceDn_Type()
)
cfprMgmtProfDerivedInterfaceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtProfDerivedInterfaceDn.setStatus("current")
_CfprMgmtProfDerivedInterfaceRn_Type = SnmpAdminString
_CfprMgmtProfDerivedInterfaceRn_Object = MibTableColumn
cfprMgmtProfDerivedInterfaceRn = _CfprMgmtProfDerivedInterfaceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 43, 1, 3),
    _CfprMgmtProfDerivedInterfaceRn_Type()
)
cfprMgmtProfDerivedInterfaceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtProfDerivedInterfaceRn.setStatus("current")
_CfprMgmtProfDerivedInterfaceConfigMessage_Type = SnmpAdminString
_CfprMgmtProfDerivedInterfaceConfigMessage_Object = MibTableColumn
cfprMgmtProfDerivedInterfaceConfigMessage = _CfprMgmtProfDerivedInterfaceConfigMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 43, 1, 4),
    _CfprMgmtProfDerivedInterfaceConfigMessage_Type()
)
cfprMgmtProfDerivedInterfaceConfigMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtProfDerivedInterfaceConfigMessage.setStatus("current")
_CfprMgmtProfDerivedInterfaceConfigState_Type = CfprMgmtConfigState
_CfprMgmtProfDerivedInterfaceConfigState_Object = MibTableColumn
cfprMgmtProfDerivedInterfaceConfigState = _CfprMgmtProfDerivedInterfaceConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 43, 1, 5),
    _CfprMgmtProfDerivedInterfaceConfigState_Type()
)
cfprMgmtProfDerivedInterfaceConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtProfDerivedInterfaceConfigState.setStatus("current")
_CfprMgmtProfDerivedInterfaceIpV4State_Type = CfprVnicExternalMgmtIPMode
_CfprMgmtProfDerivedInterfaceIpV4State_Object = MibTableColumn
cfprMgmtProfDerivedInterfaceIpV4State = _CfprMgmtProfDerivedInterfaceIpV4State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 43, 1, 6),
    _CfprMgmtProfDerivedInterfaceIpV4State_Type()
)
cfprMgmtProfDerivedInterfaceIpV4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtProfDerivedInterfaceIpV4State.setStatus("current")
_CfprMgmtProfDerivedInterfaceIpV6State_Type = CfprVnicExternalMgmtIPMode
_CfprMgmtProfDerivedInterfaceIpV6State_Object = MibTableColumn
cfprMgmtProfDerivedInterfaceIpV6State = _CfprMgmtProfDerivedInterfaceIpV6State_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 43, 1, 7),
    _CfprMgmtProfDerivedInterfaceIpV6State_Type()
)
cfprMgmtProfDerivedInterfaceIpV6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtProfDerivedInterfaceIpV6State.setStatus("current")
_CfprMgmtProfDerivedInterfaceMode_Type = CfprMgmtMode
_CfprMgmtProfDerivedInterfaceMode_Object = MibTableColumn
cfprMgmtProfDerivedInterfaceMode = _CfprMgmtProfDerivedInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 43, 1, 8),
    _CfprMgmtProfDerivedInterfaceMode_Type()
)
cfprMgmtProfDerivedInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtProfDerivedInterfaceMode.setStatus("current")
_CfprMgmtProfDerivedInterfaceOperState_Type = CfprMgmtOperState
_CfprMgmtProfDerivedInterfaceOperState_Object = MibTableColumn
cfprMgmtProfDerivedInterfaceOperState = _CfprMgmtProfDerivedInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 43, 1, 9),
    _CfprMgmtProfDerivedInterfaceOperState_Type()
)
cfprMgmtProfDerivedInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtProfDerivedInterfaceOperState.setStatus("current")
_CfprMgmtVnetTable_Object = MibTable
cfprMgmtVnetTable = _CfprMgmtVnetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 44)
)
if mibBuilder.loadTexts:
    cfprMgmtVnetTable.setStatus("current")
_CfprMgmtVnetEntry_Object = MibTableRow
cfprMgmtVnetEntry = _CfprMgmtVnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 44, 1)
)
cfprMgmtVnetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtVnetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtVnetEntry.setStatus("current")
_CfprMgmtVnetInstanceId_Type = CfprManagedObjectId
_CfprMgmtVnetInstanceId_Object = MibTableColumn
cfprMgmtVnetInstanceId = _CfprMgmtVnetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 44, 1, 1),
    _CfprMgmtVnetInstanceId_Type()
)
cfprMgmtVnetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtVnetInstanceId.setStatus("current")
_CfprMgmtVnetDn_Type = CfprManagedObjectDn
_CfprMgmtVnetDn_Object = MibTableColumn
cfprMgmtVnetDn = _CfprMgmtVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 44, 1, 2),
    _CfprMgmtVnetDn_Type()
)
cfprMgmtVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtVnetDn.setStatus("current")
_CfprMgmtVnetRn_Type = SnmpAdminString
_CfprMgmtVnetRn_Object = MibTableColumn
cfprMgmtVnetRn = _CfprMgmtVnetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 44, 1, 3),
    _CfprMgmtVnetRn_Type()
)
cfprMgmtVnetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtVnetRn.setStatus("current")
_CfprMgmtVnetConfigState_Type = CfprMgmtConfigState
_CfprMgmtVnetConfigState_Object = MibTableColumn
cfprMgmtVnetConfigState = _CfprMgmtVnetConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 44, 1, 4),
    _CfprMgmtVnetConfigState_Type()
)
cfprMgmtVnetConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtVnetConfigState.setStatus("current")
_CfprMgmtVnetId_Type = Gauge32
_CfprMgmtVnetId_Object = MibTableColumn
cfprMgmtVnetId = _CfprMgmtVnetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 44, 1, 5),
    _CfprMgmtVnetId_Type()
)
cfprMgmtVnetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtVnetId.setStatus("current")
_CfprMgmtVnetName_Type = SnmpAdminString
_CfprMgmtVnetName_Object = MibTableColumn
cfprMgmtVnetName = _CfprMgmtVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 44, 1, 6),
    _CfprMgmtVnetName_Type()
)
cfprMgmtVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtVnetName.setStatus("current")
_CfprMgmtImportConfigInfoTable_Object = MibTable
cfprMgmtImportConfigInfoTable = _CfprMgmtImportConfigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 45)
)
if mibBuilder.loadTexts:
    cfprMgmtImportConfigInfoTable.setStatus("current")
_CfprMgmtImportConfigInfoEntry_Object = MibTableRow
cfprMgmtImportConfigInfoEntry = _CfprMgmtImportConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 45, 1)
)
cfprMgmtImportConfigInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MGMT-MIB", "cfprMgmtImportConfigInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMgmtImportConfigInfoEntry.setStatus("current")
_CfprMgmtImportConfigInfoInstanceId_Type = CfprManagedObjectId
_CfprMgmtImportConfigInfoInstanceId_Object = MibTableColumn
cfprMgmtImportConfigInfoInstanceId = _CfprMgmtImportConfigInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 45, 1, 1),
    _CfprMgmtImportConfigInfoInstanceId_Type()
)
cfprMgmtImportConfigInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMgmtImportConfigInfoInstanceId.setStatus("current")
_CfprMgmtImportConfigInfoDn_Type = CfprManagedObjectDn
_CfprMgmtImportConfigInfoDn_Object = MibTableColumn
cfprMgmtImportConfigInfoDn = _CfprMgmtImportConfigInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 45, 1, 2),
    _CfprMgmtImportConfigInfoDn_Type()
)
cfprMgmtImportConfigInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImportConfigInfoDn.setStatus("current")
_CfprMgmtImportConfigInfoRn_Type = SnmpAdminString
_CfprMgmtImportConfigInfoRn_Object = MibTableColumn
cfprMgmtImportConfigInfoRn = _CfprMgmtImportConfigInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 45, 1, 3),
    _CfprMgmtImportConfigInfoRn_Type()
)
cfprMgmtImportConfigInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImportConfigInfoRn.setStatus("current")
_CfprMgmtImportConfigInfoImportDate_Type = DateAndTime
_CfprMgmtImportConfigInfoImportDate_Object = MibTableColumn
cfprMgmtImportConfigInfoImportDate = _CfprMgmtImportConfigInfoImportDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 51, 45, 1, 4),
    _CfprMgmtImportConfigInfoImportDate_Type()
)
cfprMgmtImportConfigInfoImportDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMgmtImportConfigInfoImportDate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-MGMT-MIB",
    **{"cfprMgmtObjects": cfprMgmtObjects,
       "cfprMgmtAccessPolicyTable": cfprMgmtAccessPolicyTable,
       "cfprMgmtAccessPolicyEntry": cfprMgmtAccessPolicyEntry,
       "cfprMgmtAccessPolicyInstanceId": cfprMgmtAccessPolicyInstanceId,
       "cfprMgmtAccessPolicyDn": cfprMgmtAccessPolicyDn,
       "cfprMgmtAccessPolicyRn": cfprMgmtAccessPolicyRn,
       "cfprMgmtAccessPolicyItemTable": cfprMgmtAccessPolicyItemTable,
       "cfprMgmtAccessPolicyItemEntry": cfprMgmtAccessPolicyItemEntry,
       "cfprMgmtAccessPolicyItemInstanceId": cfprMgmtAccessPolicyItemInstanceId,
       "cfprMgmtAccessPolicyItemDn": cfprMgmtAccessPolicyItemDn,
       "cfprMgmtAccessPolicyItemRn": cfprMgmtAccessPolicyItemRn,
       "cfprMgmtAccessPolicyItemDescr": cfprMgmtAccessPolicyItemDescr,
       "cfprMgmtAccessPolicyItemIntId": cfprMgmtAccessPolicyItemIntId,
       "cfprMgmtAccessPolicyItemIpPoolName": cfprMgmtAccessPolicyItemIpPoolName,
       "cfprMgmtAccessPolicyItemName": cfprMgmtAccessPolicyItemName,
       "cfprMgmtAccessPolicyItemPolicyLevel": cfprMgmtAccessPolicyItemPolicyLevel,
       "cfprMgmtAccessPolicyItemPolicyOwner": cfprMgmtAccessPolicyItemPolicyOwner,
       "cfprMgmtAccessPolicyItemSubject": cfprMgmtAccessPolicyItemSubject,
       "cfprMgmtAccessPortTable": cfprMgmtAccessPortTable,
       "cfprMgmtAccessPortEntry": cfprMgmtAccessPortEntry,
       "cfprMgmtAccessPortInstanceId": cfprMgmtAccessPortInstanceId,
       "cfprMgmtAccessPortDn": cfprMgmtAccessPortDn,
       "cfprMgmtAccessPortRn": cfprMgmtAccessPortRn,
       "cfprMgmtAccessPortPort": cfprMgmtAccessPortPort,
       "cfprMgmtAccessPortProtocol": cfprMgmtAccessPortProtocol,
       "cfprMgmtBackupTable": cfprMgmtBackupTable,
       "cfprMgmtBackupEntry": cfprMgmtBackupEntry,
       "cfprMgmtBackupInstanceId": cfprMgmtBackupInstanceId,
       "cfprMgmtBackupDn": cfprMgmtBackupDn,
       "cfprMgmtBackupRn": cfprMgmtBackupRn,
       "cfprMgmtBackupAdminState": cfprMgmtBackupAdminState,
       "cfprMgmtBackupDescr": cfprMgmtBackupDescr,
       "cfprMgmtBackupFsmDescr": cfprMgmtBackupFsmDescr,
       "cfprMgmtBackupFsmPrev": cfprMgmtBackupFsmPrev,
       "cfprMgmtBackupFsmProgr": cfprMgmtBackupFsmProgr,
       "cfprMgmtBackupFsmRmtInvErrCode": cfprMgmtBackupFsmRmtInvErrCode,
       "cfprMgmtBackupFsmRmtInvErrDescr": cfprMgmtBackupFsmRmtInvErrDescr,
       "cfprMgmtBackupFsmRmtInvRslt": cfprMgmtBackupFsmRmtInvRslt,
       "cfprMgmtBackupFsmStageDescr": cfprMgmtBackupFsmStageDescr,
       "cfprMgmtBackupFsmStamp": cfprMgmtBackupFsmStamp,
       "cfprMgmtBackupFsmStatus": cfprMgmtBackupFsmStatus,
       "cfprMgmtBackupFsmTry": cfprMgmtBackupFsmTry,
       "cfprMgmtBackupHostname": cfprMgmtBackupHostname,
       "cfprMgmtBackupIntId": cfprMgmtBackupIntId,
       "cfprMgmtBackupJob": cfprMgmtBackupJob,
       "cfprMgmtBackupMaxFiles": cfprMgmtBackupMaxFiles,
       "cfprMgmtBackupName": cfprMgmtBackupName,
       "cfprMgmtBackupOwnerPolicy": cfprMgmtBackupOwnerPolicy,
       "cfprMgmtBackupPolicyLevel": cfprMgmtBackupPolicyLevel,
       "cfprMgmtBackupPolicyOwner": cfprMgmtBackupPolicyOwner,
       "cfprMgmtBackupPostAction": cfprMgmtBackupPostAction,
       "cfprMgmtBackupPreservePooledValues": cfprMgmtBackupPreservePooledValues,
       "cfprMgmtBackupProto": cfprMgmtBackupProto,
       "cfprMgmtBackupPwd": cfprMgmtBackupPwd,
       "cfprMgmtBackupRemoteFile": cfprMgmtBackupRemoteFile,
       "cfprMgmtBackupType": cfprMgmtBackupType,
       "cfprMgmtBackupUser": cfprMgmtBackupUser,
       "cfprMgmtBackupOperStatus": cfprMgmtBackupOperStatus,
       "cfprMgmtBackupPort": cfprMgmtBackupPort,
       "cfprMgmtBackupErrMsg": cfprMgmtBackupErrMsg,
       "cfprMgmtBackupExportExtPolicyTable": cfprMgmtBackupExportExtPolicyTable,
       "cfprMgmtBackupExportExtPolicyEntry": cfprMgmtBackupExportExtPolicyEntry,
       "cfprMgmtBackupExportExtPolicyInstanceId": cfprMgmtBackupExportExtPolicyInstanceId,
       "cfprMgmtBackupExportExtPolicyDn": cfprMgmtBackupExportExtPolicyDn,
       "cfprMgmtBackupExportExtPolicyRn": cfprMgmtBackupExportExtPolicyRn,
       "cfprMgmtBackupExportExtPolicyAdminState": cfprMgmtBackupExportExtPolicyAdminState,
       "cfprMgmtBackupExportExtPolicyDescr": cfprMgmtBackupExportExtPolicyDescr,
       "cfprMgmtBackupExportExtPolicyFrequency": cfprMgmtBackupExportExtPolicyFrequency,
       "cfprMgmtBackupExportExtPolicyIntId": cfprMgmtBackupExportExtPolicyIntId,
       "cfprMgmtBackupExportExtPolicyName": cfprMgmtBackupExportExtPolicyName,
       "cfprMgmtBackupExportExtPolicyPolicyLevel": cfprMgmtBackupExportExtPolicyPolicyLevel,
       "cfprMgmtBackupExportExtPolicyPolicyOwner": cfprMgmtBackupExportExtPolicyPolicyOwner,
       "cfprMgmtBackupFsmTable": cfprMgmtBackupFsmTable,
       "cfprMgmtBackupFsmEntry": cfprMgmtBackupFsmEntry,
       "cfprMgmtBackupFsmInstanceId": cfprMgmtBackupFsmInstanceId,
       "cfprMgmtBackupFsmDn": cfprMgmtBackupFsmDn,
       "cfprMgmtBackupFsmRn": cfprMgmtBackupFsmRn,
       "cfprMgmtBackupFsmCompletionTime": cfprMgmtBackupFsmCompletionTime,
       "cfprMgmtBackupFsmCurrentFsm": cfprMgmtBackupFsmCurrentFsm,
       "cfprMgmtBackupFsmDescrData": cfprMgmtBackupFsmDescrData,
       "cfprMgmtBackupFsmFsmStatus": cfprMgmtBackupFsmFsmStatus,
       "cfprMgmtBackupFsmProgress": cfprMgmtBackupFsmProgress,
       "cfprMgmtBackupFsmRmtErrCode": cfprMgmtBackupFsmRmtErrCode,
       "cfprMgmtBackupFsmRmtErrDescr": cfprMgmtBackupFsmRmtErrDescr,
       "cfprMgmtBackupFsmRmtRslt": cfprMgmtBackupFsmRmtRslt,
       "cfprMgmtBackupFsmStageTable": cfprMgmtBackupFsmStageTable,
       "cfprMgmtBackupFsmStageEntry": cfprMgmtBackupFsmStageEntry,
       "cfprMgmtBackupFsmStageInstanceId": cfprMgmtBackupFsmStageInstanceId,
       "cfprMgmtBackupFsmStageDn": cfprMgmtBackupFsmStageDn,
       "cfprMgmtBackupFsmStageRn": cfprMgmtBackupFsmStageRn,
       "cfprMgmtBackupFsmStageDescrData": cfprMgmtBackupFsmStageDescrData,
       "cfprMgmtBackupFsmStageLastUpdateTime": cfprMgmtBackupFsmStageLastUpdateTime,
       "cfprMgmtBackupFsmStageName": cfprMgmtBackupFsmStageName,
       "cfprMgmtBackupFsmStageOrder": cfprMgmtBackupFsmStageOrder,
       "cfprMgmtBackupFsmStageRetry": cfprMgmtBackupFsmStageRetry,
       "cfprMgmtBackupFsmStageStageStatus": cfprMgmtBackupFsmStageStageStatus,
       "cfprMgmtBackupFsmTaskTable": cfprMgmtBackupFsmTaskTable,
       "cfprMgmtBackupFsmTaskEntry": cfprMgmtBackupFsmTaskEntry,
       "cfprMgmtBackupFsmTaskInstanceId": cfprMgmtBackupFsmTaskInstanceId,
       "cfprMgmtBackupFsmTaskDn": cfprMgmtBackupFsmTaskDn,
       "cfprMgmtBackupFsmTaskRn": cfprMgmtBackupFsmTaskRn,
       "cfprMgmtBackupFsmTaskCompletion": cfprMgmtBackupFsmTaskCompletion,
       "cfprMgmtBackupFsmTaskFlags": cfprMgmtBackupFsmTaskFlags,
       "cfprMgmtBackupFsmTaskItem": cfprMgmtBackupFsmTaskItem,
       "cfprMgmtBackupFsmTaskSeqId": cfprMgmtBackupFsmTaskSeqId,
       "cfprMgmtBackupPolicyTable": cfprMgmtBackupPolicyTable,
       "cfprMgmtBackupPolicyEntry": cfprMgmtBackupPolicyEntry,
       "cfprMgmtBackupPolicyInstanceId": cfprMgmtBackupPolicyInstanceId,
       "cfprMgmtBackupPolicyDn": cfprMgmtBackupPolicyDn,
       "cfprMgmtBackupPolicyRn": cfprMgmtBackupPolicyRn,
       "cfprMgmtBackupPolicyAdminState": cfprMgmtBackupPolicyAdminState,
       "cfprMgmtBackupPolicyDescr": cfprMgmtBackupPolicyDescr,
       "cfprMgmtBackupPolicyFsmDescr": cfprMgmtBackupPolicyFsmDescr,
       "cfprMgmtBackupPolicyFsmPrev": cfprMgmtBackupPolicyFsmPrev,
       "cfprMgmtBackupPolicyFsmProgr": cfprMgmtBackupPolicyFsmProgr,
       "cfprMgmtBackupPolicyFsmRmtInvErrCode": cfprMgmtBackupPolicyFsmRmtInvErrCode,
       "cfprMgmtBackupPolicyFsmRmtInvErrDescr": cfprMgmtBackupPolicyFsmRmtInvErrDescr,
       "cfprMgmtBackupPolicyFsmRmtInvRslt": cfprMgmtBackupPolicyFsmRmtInvRslt,
       "cfprMgmtBackupPolicyFsmStageDescr": cfprMgmtBackupPolicyFsmStageDescr,
       "cfprMgmtBackupPolicyFsmStamp": cfprMgmtBackupPolicyFsmStamp,
       "cfprMgmtBackupPolicyFsmStatus": cfprMgmtBackupPolicyFsmStatus,
       "cfprMgmtBackupPolicyFsmTry": cfprMgmtBackupPolicyFsmTry,
       "cfprMgmtBackupPolicyHost": cfprMgmtBackupPolicyHost,
       "cfprMgmtBackupPolicyIntId": cfprMgmtBackupPolicyIntId,
       "cfprMgmtBackupPolicyLastBackup": cfprMgmtBackupPolicyLastBackup,
       "cfprMgmtBackupPolicyMaxFiles": cfprMgmtBackupPolicyMaxFiles,
       "cfprMgmtBackupPolicyName": cfprMgmtBackupPolicyName,
       "cfprMgmtBackupPolicyPolicyLevel": cfprMgmtBackupPolicyPolicyLevel,
       "cfprMgmtBackupPolicyPolicyOwner": cfprMgmtBackupPolicyPolicyOwner,
       "cfprMgmtBackupPolicyProto": cfprMgmtBackupPolicyProto,
       "cfprMgmtBackupPolicyPwd": cfprMgmtBackupPolicyPwd,
       "cfprMgmtBackupPolicyRemoteFile": cfprMgmtBackupPolicyRemoteFile,
       "cfprMgmtBackupPolicySchedule": cfprMgmtBackupPolicySchedule,
       "cfprMgmtBackupPolicyUser": cfprMgmtBackupPolicyUser,
       "cfprMgmtBackupPolicyPort": cfprMgmtBackupPolicyPort,
       "cfprMgmtBackupPolicyConfigTable": cfprMgmtBackupPolicyConfigTable,
       "cfprMgmtBackupPolicyConfigEntry": cfprMgmtBackupPolicyConfigEntry,
       "cfprMgmtBackupPolicyConfigInstanceId": cfprMgmtBackupPolicyConfigInstanceId,
       "cfprMgmtBackupPolicyConfigDn": cfprMgmtBackupPolicyConfigDn,
       "cfprMgmtBackupPolicyConfigRn": cfprMgmtBackupPolicyConfigRn,
       "cfprMgmtBackupPolicyConfigAdminState": cfprMgmtBackupPolicyConfigAdminState,
       "cfprMgmtBackupPolicyConfigAutoDelete": cfprMgmtBackupPolicyConfigAutoDelete,
       "cfprMgmtBackupPolicyConfigBackupDate": cfprMgmtBackupPolicyConfigBackupDate,
       "cfprMgmtBackupPolicyConfigBackupIssue": cfprMgmtBackupPolicyConfigBackupIssue,
       "cfprMgmtBackupPolicyConfigDescr": cfprMgmtBackupPolicyConfigDescr,
       "cfprMgmtBackupPolicyConfigIgnoreCap": cfprMgmtBackupPolicyConfigIgnoreCap,
       "cfprMgmtBackupPolicyConfigIntId": cfprMgmtBackupPolicyConfigIntId,
       "cfprMgmtBackupPolicyConfigName": cfprMgmtBackupPolicyConfigName,
       "cfprMgmtBackupPolicyConfigOperScheduler": cfprMgmtBackupPolicyConfigOperScheduler,
       "cfprMgmtBackupPolicyConfigOperState": cfprMgmtBackupPolicyConfigOperState,
       "cfprMgmtBackupPolicyConfigPolicyLevel": cfprMgmtBackupPolicyConfigPolicyLevel,
       "cfprMgmtBackupPolicyConfigPolicyOwner": cfprMgmtBackupPolicyConfigPolicyOwner,
       "cfprMgmtBackupPolicyConfigScheduler": cfprMgmtBackupPolicyConfigScheduler,
       "cfprMgmtBackupPolicyFsmTable": cfprMgmtBackupPolicyFsmTable,
       "cfprMgmtBackupPolicyFsmEntry": cfprMgmtBackupPolicyFsmEntry,
       "cfprMgmtBackupPolicyFsmInstanceId": cfprMgmtBackupPolicyFsmInstanceId,
       "cfprMgmtBackupPolicyFsmDn": cfprMgmtBackupPolicyFsmDn,
       "cfprMgmtBackupPolicyFsmRn": cfprMgmtBackupPolicyFsmRn,
       "cfprMgmtBackupPolicyFsmCompletionTime": cfprMgmtBackupPolicyFsmCompletionTime,
       "cfprMgmtBackupPolicyFsmCurrentFsm": cfprMgmtBackupPolicyFsmCurrentFsm,
       "cfprMgmtBackupPolicyFsmDescrData": cfprMgmtBackupPolicyFsmDescrData,
       "cfprMgmtBackupPolicyFsmFsmStatus": cfprMgmtBackupPolicyFsmFsmStatus,
       "cfprMgmtBackupPolicyFsmProgress": cfprMgmtBackupPolicyFsmProgress,
       "cfprMgmtBackupPolicyFsmRmtErrCode": cfprMgmtBackupPolicyFsmRmtErrCode,
       "cfprMgmtBackupPolicyFsmRmtErrDescr": cfprMgmtBackupPolicyFsmRmtErrDescr,
       "cfprMgmtBackupPolicyFsmRmtRslt": cfprMgmtBackupPolicyFsmRmtRslt,
       "cfprMgmtBackupPolicyFsmStageTable": cfprMgmtBackupPolicyFsmStageTable,
       "cfprMgmtBackupPolicyFsmStageEntry": cfprMgmtBackupPolicyFsmStageEntry,
       "cfprMgmtBackupPolicyFsmStageInstanceId": cfprMgmtBackupPolicyFsmStageInstanceId,
       "cfprMgmtBackupPolicyFsmStageDn": cfprMgmtBackupPolicyFsmStageDn,
       "cfprMgmtBackupPolicyFsmStageRn": cfprMgmtBackupPolicyFsmStageRn,
       "cfprMgmtBackupPolicyFsmStageDescrData": cfprMgmtBackupPolicyFsmStageDescrData,
       "cfprMgmtBackupPolicyFsmStageLastUpdateTime": cfprMgmtBackupPolicyFsmStageLastUpdateTime,
       "cfprMgmtBackupPolicyFsmStageName": cfprMgmtBackupPolicyFsmStageName,
       "cfprMgmtBackupPolicyFsmStageOrder": cfprMgmtBackupPolicyFsmStageOrder,
       "cfprMgmtBackupPolicyFsmStageRetry": cfprMgmtBackupPolicyFsmStageRetry,
       "cfprMgmtBackupPolicyFsmStageStageStatus": cfprMgmtBackupPolicyFsmStageStageStatus,
       "cfprMgmtCfgExportPolicyTable": cfprMgmtCfgExportPolicyTable,
       "cfprMgmtCfgExportPolicyEntry": cfprMgmtCfgExportPolicyEntry,
       "cfprMgmtCfgExportPolicyInstanceId": cfprMgmtCfgExportPolicyInstanceId,
       "cfprMgmtCfgExportPolicyDn": cfprMgmtCfgExportPolicyDn,
       "cfprMgmtCfgExportPolicyRn": cfprMgmtCfgExportPolicyRn,
       "cfprMgmtCfgExportPolicyAdminState": cfprMgmtCfgExportPolicyAdminState,
       "cfprMgmtCfgExportPolicyDescr": cfprMgmtCfgExportPolicyDescr,
       "cfprMgmtCfgExportPolicyFsmDescr": cfprMgmtCfgExportPolicyFsmDescr,
       "cfprMgmtCfgExportPolicyFsmPrev": cfprMgmtCfgExportPolicyFsmPrev,
       "cfprMgmtCfgExportPolicyFsmProgr": cfprMgmtCfgExportPolicyFsmProgr,
       "cfprMgmtCfgExportPolicyFsmRmtInvErrCode": cfprMgmtCfgExportPolicyFsmRmtInvErrCode,
       "cfprMgmtCfgExportPolicyFsmRmtInvErrDescr": cfprMgmtCfgExportPolicyFsmRmtInvErrDescr,
       "cfprMgmtCfgExportPolicyFsmRmtInvRslt": cfprMgmtCfgExportPolicyFsmRmtInvRslt,
       "cfprMgmtCfgExportPolicyFsmStageDescr": cfprMgmtCfgExportPolicyFsmStageDescr,
       "cfprMgmtCfgExportPolicyFsmStamp": cfprMgmtCfgExportPolicyFsmStamp,
       "cfprMgmtCfgExportPolicyFsmStatus": cfprMgmtCfgExportPolicyFsmStatus,
       "cfprMgmtCfgExportPolicyFsmTry": cfprMgmtCfgExportPolicyFsmTry,
       "cfprMgmtCfgExportPolicyHost": cfprMgmtCfgExportPolicyHost,
       "cfprMgmtCfgExportPolicyIntId": cfprMgmtCfgExportPolicyIntId,
       "cfprMgmtCfgExportPolicyLastBackup": cfprMgmtCfgExportPolicyLastBackup,
       "cfprMgmtCfgExportPolicyMaxFiles": cfprMgmtCfgExportPolicyMaxFiles,
       "cfprMgmtCfgExportPolicyName": cfprMgmtCfgExportPolicyName,
       "cfprMgmtCfgExportPolicyPolicyLevel": cfprMgmtCfgExportPolicyPolicyLevel,
       "cfprMgmtCfgExportPolicyPolicyOwner": cfprMgmtCfgExportPolicyPolicyOwner,
       "cfprMgmtCfgExportPolicyProto": cfprMgmtCfgExportPolicyProto,
       "cfprMgmtCfgExportPolicyPwd": cfprMgmtCfgExportPolicyPwd,
       "cfprMgmtCfgExportPolicyRemoteFile": cfprMgmtCfgExportPolicyRemoteFile,
       "cfprMgmtCfgExportPolicySchedule": cfprMgmtCfgExportPolicySchedule,
       "cfprMgmtCfgExportPolicyUser": cfprMgmtCfgExportPolicyUser,
       "cfprMgmtCfgExportPolicyPort": cfprMgmtCfgExportPolicyPort,
       "cfprMgmtCfgExportPolicyFsmTable": cfprMgmtCfgExportPolicyFsmTable,
       "cfprMgmtCfgExportPolicyFsmEntry": cfprMgmtCfgExportPolicyFsmEntry,
       "cfprMgmtCfgExportPolicyFsmInstanceId": cfprMgmtCfgExportPolicyFsmInstanceId,
       "cfprMgmtCfgExportPolicyFsmDn": cfprMgmtCfgExportPolicyFsmDn,
       "cfprMgmtCfgExportPolicyFsmRn": cfprMgmtCfgExportPolicyFsmRn,
       "cfprMgmtCfgExportPolicyFsmCompletionTime": cfprMgmtCfgExportPolicyFsmCompletionTime,
       "cfprMgmtCfgExportPolicyFsmCurrentFsm": cfprMgmtCfgExportPolicyFsmCurrentFsm,
       "cfprMgmtCfgExportPolicyFsmDescrData": cfprMgmtCfgExportPolicyFsmDescrData,
       "cfprMgmtCfgExportPolicyFsmFsmStatus": cfprMgmtCfgExportPolicyFsmFsmStatus,
       "cfprMgmtCfgExportPolicyFsmProgress": cfprMgmtCfgExportPolicyFsmProgress,
       "cfprMgmtCfgExportPolicyFsmRmtErrCode": cfprMgmtCfgExportPolicyFsmRmtErrCode,
       "cfprMgmtCfgExportPolicyFsmRmtErrDescr": cfprMgmtCfgExportPolicyFsmRmtErrDescr,
       "cfprMgmtCfgExportPolicyFsmRmtRslt": cfprMgmtCfgExportPolicyFsmRmtRslt,
       "cfprMgmtCfgExportPolicyFsmStageTable": cfprMgmtCfgExportPolicyFsmStageTable,
       "cfprMgmtCfgExportPolicyFsmStageEntry": cfprMgmtCfgExportPolicyFsmStageEntry,
       "cfprMgmtCfgExportPolicyFsmStageInstanceId": cfprMgmtCfgExportPolicyFsmStageInstanceId,
       "cfprMgmtCfgExportPolicyFsmStageDn": cfprMgmtCfgExportPolicyFsmStageDn,
       "cfprMgmtCfgExportPolicyFsmStageRn": cfprMgmtCfgExportPolicyFsmStageRn,
       "cfprMgmtCfgExportPolicyFsmStageDescrData": cfprMgmtCfgExportPolicyFsmStageDescrData,
       "cfprMgmtCfgExportPolicyFsmStageLastUpdateTime": cfprMgmtCfgExportPolicyFsmStageLastUpdateTime,
       "cfprMgmtCfgExportPolicyFsmStageName": cfprMgmtCfgExportPolicyFsmStageName,
       "cfprMgmtCfgExportPolicyFsmStageOrder": cfprMgmtCfgExportPolicyFsmStageOrder,
       "cfprMgmtCfgExportPolicyFsmStageRetry": cfprMgmtCfgExportPolicyFsmStageRetry,
       "cfprMgmtCfgExportPolicyFsmStageStageStatus": cfprMgmtCfgExportPolicyFsmStageStageStatus,
       "cfprMgmtCimcSecureBootTable": cfprMgmtCimcSecureBootTable,
       "cfprMgmtCimcSecureBootEntry": cfprMgmtCimcSecureBootEntry,
       "cfprMgmtCimcSecureBootInstanceId": cfprMgmtCimcSecureBootInstanceId,
       "cfprMgmtCimcSecureBootDn": cfprMgmtCimcSecureBootDn,
       "cfprMgmtCimcSecureBootRn": cfprMgmtCimcSecureBootRn,
       "cfprMgmtCimcSecureBootAdminState": cfprMgmtCimcSecureBootAdminState,
       "cfprMgmtCimcSecureBootOperState": cfprMgmtCimcSecureBootOperState,
       "cfprMgmtConnectionTable": cfprMgmtConnectionTable,
       "cfprMgmtConnectionEntry": cfprMgmtConnectionEntry,
       "cfprMgmtConnectionInstanceId": cfprMgmtConnectionInstanceId,
       "cfprMgmtConnectionDn": cfprMgmtConnectionDn,
       "cfprMgmtConnectionRn": cfprMgmtConnectionRn,
       "cfprMgmtConnectionAck": cfprMgmtConnectionAck,
       "cfprMgmtConnectionOperState": cfprMgmtConnectionOperState,
       "cfprMgmtConnectionType": cfprMgmtConnectionType,
       "cfprMgmtControllerTable": cfprMgmtControllerTable,
       "cfprMgmtControllerEntry": cfprMgmtControllerEntry,
       "cfprMgmtControllerInstanceId": cfprMgmtControllerInstanceId,
       "cfprMgmtControllerDn": cfprMgmtControllerDn,
       "cfprMgmtControllerRn": cfprMgmtControllerRn,
       "cfprMgmtControllerDimmBlacklistingOperState": cfprMgmtControllerDimmBlacklistingOperState,
       "cfprMgmtControllerFsmDescr": cfprMgmtControllerFsmDescr,
       "cfprMgmtControllerFsmFlags": cfprMgmtControllerFsmFlags,
       "cfprMgmtControllerFsmPrev": cfprMgmtControllerFsmPrev,
       "cfprMgmtControllerFsmProgr": cfprMgmtControllerFsmProgr,
       "cfprMgmtControllerFsmRmtInvErrCode": cfprMgmtControllerFsmRmtInvErrCode,
       "cfprMgmtControllerFsmRmtInvErrDescr": cfprMgmtControllerFsmRmtInvErrDescr,
       "cfprMgmtControllerFsmRmtInvRslt": cfprMgmtControllerFsmRmtInvRslt,
       "cfprMgmtControllerFsmStageDescr": cfprMgmtControllerFsmStageDescr,
       "cfprMgmtControllerFsmStamp": cfprMgmtControllerFsmStamp,
       "cfprMgmtControllerFsmStatus": cfprMgmtControllerFsmStatus,
       "cfprMgmtControllerFsmTry": cfprMgmtControllerFsmTry,
       "cfprMgmtControllerGuid": cfprMgmtControllerGuid,
       "cfprMgmtControllerModel": cfprMgmtControllerModel,
       "cfprMgmtControllerOperConn": cfprMgmtControllerOperConn,
       "cfprMgmtControllerRevision": cfprMgmtControllerRevision,
       "cfprMgmtControllerSerial": cfprMgmtControllerSerial,
       "cfprMgmtControllerStorageOobInterfaceSupported": cfprMgmtControllerStorageOobInterfaceSupported,
       "cfprMgmtControllerStorageSubsystemState": cfprMgmtControllerStorageSubsystemState,
       "cfprMgmtControllerSubject": cfprMgmtControllerSubject,
       "cfprMgmtControllerVendor": cfprMgmtControllerVendor,
       "cfprMgmtControllerFsmTable": cfprMgmtControllerFsmTable,
       "cfprMgmtControllerFsmEntry": cfprMgmtControllerFsmEntry,
       "cfprMgmtControllerFsmInstanceId": cfprMgmtControllerFsmInstanceId,
       "cfprMgmtControllerFsmDn": cfprMgmtControllerFsmDn,
       "cfprMgmtControllerFsmRn": cfprMgmtControllerFsmRn,
       "cfprMgmtControllerFsmCompletionTime": cfprMgmtControllerFsmCompletionTime,
       "cfprMgmtControllerFsmCurrentFsm": cfprMgmtControllerFsmCurrentFsm,
       "cfprMgmtControllerFsmDescrData": cfprMgmtControllerFsmDescrData,
       "cfprMgmtControllerFsmFsmStatus": cfprMgmtControllerFsmFsmStatus,
       "cfprMgmtControllerFsmProgress": cfprMgmtControllerFsmProgress,
       "cfprMgmtControllerFsmRmtErrCode": cfprMgmtControllerFsmRmtErrCode,
       "cfprMgmtControllerFsmRmtErrDescr": cfprMgmtControllerFsmRmtErrDescr,
       "cfprMgmtControllerFsmRmtRslt": cfprMgmtControllerFsmRmtRslt,
       "cfprMgmtControllerFsmStageTable": cfprMgmtControllerFsmStageTable,
       "cfprMgmtControllerFsmStageEntry": cfprMgmtControllerFsmStageEntry,
       "cfprMgmtControllerFsmStageInstanceId": cfprMgmtControllerFsmStageInstanceId,
       "cfprMgmtControllerFsmStageDn": cfprMgmtControllerFsmStageDn,
       "cfprMgmtControllerFsmStageRn": cfprMgmtControllerFsmStageRn,
       "cfprMgmtControllerFsmStageDescrData": cfprMgmtControllerFsmStageDescrData,
       "cfprMgmtControllerFsmStageLastUpdateTime": cfprMgmtControllerFsmStageLastUpdateTime,
       "cfprMgmtControllerFsmStageName": cfprMgmtControllerFsmStageName,
       "cfprMgmtControllerFsmStageOrder": cfprMgmtControllerFsmStageOrder,
       "cfprMgmtControllerFsmStageRetry": cfprMgmtControllerFsmStageRetry,
       "cfprMgmtControllerFsmStageStageStatus": cfprMgmtControllerFsmStageStageStatus,
       "cfprMgmtControllerFsmTaskTable": cfprMgmtControllerFsmTaskTable,
       "cfprMgmtControllerFsmTaskEntry": cfprMgmtControllerFsmTaskEntry,
       "cfprMgmtControllerFsmTaskInstanceId": cfprMgmtControllerFsmTaskInstanceId,
       "cfprMgmtControllerFsmTaskDn": cfprMgmtControllerFsmTaskDn,
       "cfprMgmtControllerFsmTaskRn": cfprMgmtControllerFsmTaskRn,
       "cfprMgmtControllerFsmTaskCompletion": cfprMgmtControllerFsmTaskCompletion,
       "cfprMgmtControllerFsmTaskFlags": cfprMgmtControllerFsmTaskFlags,
       "cfprMgmtControllerFsmTaskItem": cfprMgmtControllerFsmTaskItem,
       "cfprMgmtControllerFsmTaskSeqId": cfprMgmtControllerFsmTaskSeqId,
       "cfprMgmtEntityTable": cfprMgmtEntityTable,
       "cfprMgmtEntityEntry": cfprMgmtEntityEntry,
       "cfprMgmtEntityInstanceId": cfprMgmtEntityInstanceId,
       "cfprMgmtEntityDn": cfprMgmtEntityDn,
       "cfprMgmtEntityRn": cfprMgmtEntityRn,
       "cfprMgmtEntityChassis1": cfprMgmtEntityChassis1,
       "cfprMgmtEntityChassis2": cfprMgmtEntityChassis2,
       "cfprMgmtEntityChassis3": cfprMgmtEntityChassis3,
       "cfprMgmtEntityChassisDeviceIoState1": cfprMgmtEntityChassisDeviceIoState1,
       "cfprMgmtEntityChassisDeviceIoState2": cfprMgmtEntityChassisDeviceIoState2,
       "cfprMgmtEntityChassisDeviceIoState3": cfprMgmtEntityChassisDeviceIoState3,
       "cfprMgmtEntityHaFailureReason": cfprMgmtEntityHaFailureReason,
       "cfprMgmtEntityHaReadiness": cfprMgmtEntityHaReadiness,
       "cfprMgmtEntityHaReady": cfprMgmtEntityHaReady,
       "cfprMgmtEntityId": cfprMgmtEntityId,
       "cfprMgmtEntityLeadership": cfprMgmtEntityLeadership,
       "cfprMgmtEntityMgmtServicesState": cfprMgmtEntityMgmtServicesState,
       "cfprMgmtEntityProblems": cfprMgmtEntityProblems,
       "cfprMgmtEntitySshAuthKeysCsum": cfprMgmtEntitySshAuthKeysCsum,
       "cfprMgmtEntitySshAuthKeysSize": cfprMgmtEntitySshAuthKeysSize,
       "cfprMgmtEntitySshKeyStatus": cfprMgmtEntitySshKeyStatus,
       "cfprMgmtEntitySshRootPubKeyCsum": cfprMgmtEntitySshRootPubKeyCsum,
       "cfprMgmtEntitySshRootPubKeySize": cfprMgmtEntitySshRootPubKeySize,
       "cfprMgmtEntityState": cfprMgmtEntityState,
       "cfprMgmtEntityUmbilicalState": cfprMgmtEntityUmbilicalState,
       "cfprMgmtEntityVersionMismatch": cfprMgmtEntityVersionMismatch,
       "cfprMgmtExportPolicyFsmTable": cfprMgmtExportPolicyFsmTable,
       "cfprMgmtExportPolicyFsmEntry": cfprMgmtExportPolicyFsmEntry,
       "cfprMgmtExportPolicyFsmInstanceId": cfprMgmtExportPolicyFsmInstanceId,
       "cfprMgmtExportPolicyFsmDn": cfprMgmtExportPolicyFsmDn,
       "cfprMgmtExportPolicyFsmRn": cfprMgmtExportPolicyFsmRn,
       "cfprMgmtExportPolicyFsmCompletionTime": cfprMgmtExportPolicyFsmCompletionTime,
       "cfprMgmtExportPolicyFsmCurrentFsm": cfprMgmtExportPolicyFsmCurrentFsm,
       "cfprMgmtExportPolicyFsmDescr": cfprMgmtExportPolicyFsmDescr,
       "cfprMgmtExportPolicyFsmFsmStatus": cfprMgmtExportPolicyFsmFsmStatus,
       "cfprMgmtExportPolicyFsmProgress": cfprMgmtExportPolicyFsmProgress,
       "cfprMgmtExportPolicyFsmRmtErrCode": cfprMgmtExportPolicyFsmRmtErrCode,
       "cfprMgmtExportPolicyFsmRmtErrDescr": cfprMgmtExportPolicyFsmRmtErrDescr,
       "cfprMgmtExportPolicyFsmRmtRslt": cfprMgmtExportPolicyFsmRmtRslt,
       "cfprMgmtExportPolicyFsmStageTable": cfprMgmtExportPolicyFsmStageTable,
       "cfprMgmtExportPolicyFsmStageEntry": cfprMgmtExportPolicyFsmStageEntry,
       "cfprMgmtExportPolicyFsmStageInstanceId": cfprMgmtExportPolicyFsmStageInstanceId,
       "cfprMgmtExportPolicyFsmStageDn": cfprMgmtExportPolicyFsmStageDn,
       "cfprMgmtExportPolicyFsmStageRn": cfprMgmtExportPolicyFsmStageRn,
       "cfprMgmtExportPolicyFsmStageDescr": cfprMgmtExportPolicyFsmStageDescr,
       "cfprMgmtExportPolicyFsmStageLastUpdateTime": cfprMgmtExportPolicyFsmStageLastUpdateTime,
       "cfprMgmtExportPolicyFsmStageName": cfprMgmtExportPolicyFsmStageName,
       "cfprMgmtExportPolicyFsmStageOrder": cfprMgmtExportPolicyFsmStageOrder,
       "cfprMgmtExportPolicyFsmStageRetry": cfprMgmtExportPolicyFsmStageRetry,
       "cfprMgmtExportPolicyFsmStageStageStatus": cfprMgmtExportPolicyFsmStageStageStatus,
       "cfprMgmtExportPolicyFsmTaskTable": cfprMgmtExportPolicyFsmTaskTable,
       "cfprMgmtExportPolicyFsmTaskEntry": cfprMgmtExportPolicyFsmTaskEntry,
       "cfprMgmtExportPolicyFsmTaskInstanceId": cfprMgmtExportPolicyFsmTaskInstanceId,
       "cfprMgmtExportPolicyFsmTaskDn": cfprMgmtExportPolicyFsmTaskDn,
       "cfprMgmtExportPolicyFsmTaskRn": cfprMgmtExportPolicyFsmTaskRn,
       "cfprMgmtExportPolicyFsmTaskCompletion": cfprMgmtExportPolicyFsmTaskCompletion,
       "cfprMgmtExportPolicyFsmTaskFlags": cfprMgmtExportPolicyFsmTaskFlags,
       "cfprMgmtExportPolicyFsmTaskItem": cfprMgmtExportPolicyFsmTaskItem,
       "cfprMgmtExportPolicyFsmTaskSeqId": cfprMgmtExportPolicyFsmTaskSeqId,
       "cfprMgmtIPv6IfAddrTable": cfprMgmtIPv6IfAddrTable,
       "cfprMgmtIPv6IfAddrEntry": cfprMgmtIPv6IfAddrEntry,
       "cfprMgmtIPv6IfAddrInstanceId": cfprMgmtIPv6IfAddrInstanceId,
       "cfprMgmtIPv6IfAddrDn": cfprMgmtIPv6IfAddrDn,
       "cfprMgmtIPv6IfAddrRn": cfprMgmtIPv6IfAddrRn,
       "cfprMgmtIPv6IfAddrAddr": cfprMgmtIPv6IfAddrAddr,
       "cfprMgmtIPv6IfAddrDefGw": cfprMgmtIPv6IfAddrDefGw,
       "cfprMgmtIPv6IfAddrFsmDescr": cfprMgmtIPv6IfAddrFsmDescr,
       "cfprMgmtIPv6IfAddrFsmPrev": cfprMgmtIPv6IfAddrFsmPrev,
       "cfprMgmtIPv6IfAddrFsmProgr": cfprMgmtIPv6IfAddrFsmProgr,
       "cfprMgmtIPv6IfAddrFsmRmtInvErrCode": cfprMgmtIPv6IfAddrFsmRmtInvErrCode,
       "cfprMgmtIPv6IfAddrFsmRmtInvErrDescr": cfprMgmtIPv6IfAddrFsmRmtInvErrDescr,
       "cfprMgmtIPv6IfAddrFsmRmtInvRslt": cfprMgmtIPv6IfAddrFsmRmtInvRslt,
       "cfprMgmtIPv6IfAddrFsmStageDescr": cfprMgmtIPv6IfAddrFsmStageDescr,
       "cfprMgmtIPv6IfAddrFsmStamp": cfprMgmtIPv6IfAddrFsmStamp,
       "cfprMgmtIPv6IfAddrFsmStatus": cfprMgmtIPv6IfAddrFsmStatus,
       "cfprMgmtIPv6IfAddrFsmTry": cfprMgmtIPv6IfAddrFsmTry,
       "cfprMgmtIPv6IfAddrPrefix": cfprMgmtIPv6IfAddrPrefix,
       "cfprMgmtIPv6IfAddrIpv6autocfg": cfprMgmtIPv6IfAddrIpv6autocfg,
       "cfprMgmtIPv6IfAddrIpv6dirtyint": cfprMgmtIPv6IfAddrIpv6dirtyint,
       "cfprMgmtIPv6IfAddrIpv6readyaddr": cfprMgmtIPv6IfAddrIpv6readyaddr,
       "cfprMgmtIPv6IfAddrIpv6readycfg": cfprMgmtIPv6IfAddrIpv6readycfg,
       "cfprMgmtIPv6IfAddrIpv6readyprefix": cfprMgmtIPv6IfAddrIpv6readyprefix,
       "cfprMgmtIPv6IfAddrIpv6val": cfprMgmtIPv6IfAddrIpv6val,
       "cfprMgmtIPv6IfAddrNdval": cfprMgmtIPv6IfAddrNdval,
       "cfprMgmtIPv6IfAddrFsmTable": cfprMgmtIPv6IfAddrFsmTable,
       "cfprMgmtIPv6IfAddrFsmEntry": cfprMgmtIPv6IfAddrFsmEntry,
       "cfprMgmtIPv6IfAddrFsmInstanceId": cfprMgmtIPv6IfAddrFsmInstanceId,
       "cfprMgmtIPv6IfAddrFsmDn": cfprMgmtIPv6IfAddrFsmDn,
       "cfprMgmtIPv6IfAddrFsmRn": cfprMgmtIPv6IfAddrFsmRn,
       "cfprMgmtIPv6IfAddrFsmCompletionTime": cfprMgmtIPv6IfAddrFsmCompletionTime,
       "cfprMgmtIPv6IfAddrFsmCurrentFsm": cfprMgmtIPv6IfAddrFsmCurrentFsm,
       "cfprMgmtIPv6IfAddrFsmDescrData": cfprMgmtIPv6IfAddrFsmDescrData,
       "cfprMgmtIPv6IfAddrFsmFsmStatus": cfprMgmtIPv6IfAddrFsmFsmStatus,
       "cfprMgmtIPv6IfAddrFsmProgress": cfprMgmtIPv6IfAddrFsmProgress,
       "cfprMgmtIPv6IfAddrFsmRmtErrCode": cfprMgmtIPv6IfAddrFsmRmtErrCode,
       "cfprMgmtIPv6IfAddrFsmRmtErrDescr": cfprMgmtIPv6IfAddrFsmRmtErrDescr,
       "cfprMgmtIPv6IfAddrFsmRmtRslt": cfprMgmtIPv6IfAddrFsmRmtRslt,
       "cfprMgmtIPv6IfAddrFsmStageTable": cfprMgmtIPv6IfAddrFsmStageTable,
       "cfprMgmtIPv6IfAddrFsmStageEntry": cfprMgmtIPv6IfAddrFsmStageEntry,
       "cfprMgmtIPv6IfAddrFsmStageInstanceId": cfprMgmtIPv6IfAddrFsmStageInstanceId,
       "cfprMgmtIPv6IfAddrFsmStageDn": cfprMgmtIPv6IfAddrFsmStageDn,
       "cfprMgmtIPv6IfAddrFsmStageRn": cfprMgmtIPv6IfAddrFsmStageRn,
       "cfprMgmtIPv6IfAddrFsmStageDescrData": cfprMgmtIPv6IfAddrFsmStageDescrData,
       "cfprMgmtIPv6IfAddrFsmStageLastUpdateTime": cfprMgmtIPv6IfAddrFsmStageLastUpdateTime,
       "cfprMgmtIPv6IfAddrFsmStageName": cfprMgmtIPv6IfAddrFsmStageName,
       "cfprMgmtIPv6IfAddrFsmStageOrder": cfprMgmtIPv6IfAddrFsmStageOrder,
       "cfprMgmtIPv6IfAddrFsmStageRetry": cfprMgmtIPv6IfAddrFsmStageRetry,
       "cfprMgmtIPv6IfAddrFsmStageStageStatus": cfprMgmtIPv6IfAddrFsmStageStageStatus,
       "cfprMgmtIPv6IfAddrFsmTaskTable": cfprMgmtIPv6IfAddrFsmTaskTable,
       "cfprMgmtIPv6IfAddrFsmTaskEntry": cfprMgmtIPv6IfAddrFsmTaskEntry,
       "cfprMgmtIPv6IfAddrFsmTaskInstanceId": cfprMgmtIPv6IfAddrFsmTaskInstanceId,
       "cfprMgmtIPv6IfAddrFsmTaskDn": cfprMgmtIPv6IfAddrFsmTaskDn,
       "cfprMgmtIPv6IfAddrFsmTaskRn": cfprMgmtIPv6IfAddrFsmTaskRn,
       "cfprMgmtIPv6IfAddrFsmTaskCompletion": cfprMgmtIPv6IfAddrFsmTaskCompletion,
       "cfprMgmtIPv6IfAddrFsmTaskFlags": cfprMgmtIPv6IfAddrFsmTaskFlags,
       "cfprMgmtIPv6IfAddrFsmTaskItem": cfprMgmtIPv6IfAddrFsmTaskItem,
       "cfprMgmtIPv6IfAddrFsmTaskSeqId": cfprMgmtIPv6IfAddrFsmTaskSeqId,
       "cfprMgmtIPv6IfConfigTable": cfprMgmtIPv6IfConfigTable,
       "cfprMgmtIPv6IfConfigEntry": cfprMgmtIPv6IfConfigEntry,
       "cfprMgmtIPv6IfConfigInstanceId": cfprMgmtIPv6IfConfigInstanceId,
       "cfprMgmtIPv6IfConfigDn": cfprMgmtIPv6IfConfigDn,
       "cfprMgmtIPv6IfConfigRn": cfprMgmtIPv6IfConfigRn,
       "cfprMgmtIfTable": cfprMgmtIfTable,
       "cfprMgmtIfEntry": cfprMgmtIfEntry,
       "cfprMgmtIfInstanceId": cfprMgmtIfInstanceId,
       "cfprMgmtIfDn": cfprMgmtIfDn,
       "cfprMgmtIfRn": cfprMgmtIfRn,
       "cfprMgmtIfAccess": cfprMgmtIfAccess,
       "cfprMgmtIfAdminState": cfprMgmtIfAdminState,
       "cfprMgmtIfAggrPortId": cfprMgmtIfAggrPortId,
       "cfprMgmtIfChassisId": cfprMgmtIfChassisId,
       "cfprMgmtIfDiscovery": cfprMgmtIfDiscovery,
       "cfprMgmtIfEpDn": cfprMgmtIfEpDn,
       "cfprMgmtIfExtBroadcast": cfprMgmtIfExtBroadcast,
       "cfprMgmtIfExtGw": cfprMgmtIfExtGw,
       "cfprMgmtIfExtIp": cfprMgmtIfExtIp,
       "cfprMgmtIfExtMask": cfprMgmtIfExtMask,
       "cfprMgmtIfFsmDescr": cfprMgmtIfFsmDescr,
       "cfprMgmtIfFsmPrev": cfprMgmtIfFsmPrev,
       "cfprMgmtIfFsmProgr": cfprMgmtIfFsmProgr,
       "cfprMgmtIfFsmRmtInvErrCode": cfprMgmtIfFsmRmtInvErrCode,
       "cfprMgmtIfFsmRmtInvErrDescr": cfprMgmtIfFsmRmtInvErrDescr,
       "cfprMgmtIfFsmRmtInvRslt": cfprMgmtIfFsmRmtInvRslt,
       "cfprMgmtIfFsmStageDescr": cfprMgmtIfFsmStageDescr,
       "cfprMgmtIfFsmStamp": cfprMgmtIfFsmStamp,
       "cfprMgmtIfFsmStatus": cfprMgmtIfFsmStatus,
       "cfprMgmtIfFsmTry": cfprMgmtIfFsmTry,
       "cfprMgmtIfId": cfprMgmtIfId,
       "cfprMgmtIfIfRole": cfprMgmtIfIfRole,
       "cfprMgmtIfIfType": cfprMgmtIfIfType,
       "cfprMgmtIfIp": cfprMgmtIfIp,
       "cfprMgmtIfLocale": cfprMgmtIfLocale,
       "cfprMgmtIfMac": cfprMgmtIfMac,
       "cfprMgmtIfMask": cfprMgmtIfMask,
       "cfprMgmtIfName": cfprMgmtIfName,
       "cfprMgmtIfPeerAggrPortId": cfprMgmtIfPeerAggrPortId,
       "cfprMgmtIfPeerChassisId": cfprMgmtIfPeerChassisId,
       "cfprMgmtIfPeerDn": cfprMgmtIfPeerDn,
       "cfprMgmtIfPeerPortId": cfprMgmtIfPeerPortId,
       "cfprMgmtIfPeerSlotId": cfprMgmtIfPeerSlotId,
       "cfprMgmtIfPortId": cfprMgmtIfPortId,
       "cfprMgmtIfSlotId": cfprMgmtIfSlotId,
       "cfprMgmtIfStateQual": cfprMgmtIfStateQual,
       "cfprMgmtIfSubject": cfprMgmtIfSubject,
       "cfprMgmtIfSwitchId": cfprMgmtIfSwitchId,
       "cfprMgmtIfTransport": cfprMgmtIfTransport,
       "cfprMgmtIfType": cfprMgmtIfType,
       "cfprMgmtIfVnet": cfprMgmtIfVnet,
       "cfprMgmtIfFsmTable": cfprMgmtIfFsmTable,
       "cfprMgmtIfFsmEntry": cfprMgmtIfFsmEntry,
       "cfprMgmtIfFsmInstanceId": cfprMgmtIfFsmInstanceId,
       "cfprMgmtIfFsmDn": cfprMgmtIfFsmDn,
       "cfprMgmtIfFsmRn": cfprMgmtIfFsmRn,
       "cfprMgmtIfFsmCompletionTime": cfprMgmtIfFsmCompletionTime,
       "cfprMgmtIfFsmCurrentFsm": cfprMgmtIfFsmCurrentFsm,
       "cfprMgmtIfFsmDescrData": cfprMgmtIfFsmDescrData,
       "cfprMgmtIfFsmFsmStatus": cfprMgmtIfFsmFsmStatus,
       "cfprMgmtIfFsmProgress": cfprMgmtIfFsmProgress,
       "cfprMgmtIfFsmRmtErrCode": cfprMgmtIfFsmRmtErrCode,
       "cfprMgmtIfFsmRmtErrDescr": cfprMgmtIfFsmRmtErrDescr,
       "cfprMgmtIfFsmRmtRslt": cfprMgmtIfFsmRmtRslt,
       "cfprMgmtIfFsmStageTable": cfprMgmtIfFsmStageTable,
       "cfprMgmtIfFsmStageEntry": cfprMgmtIfFsmStageEntry,
       "cfprMgmtIfFsmStageInstanceId": cfprMgmtIfFsmStageInstanceId,
       "cfprMgmtIfFsmStageDn": cfprMgmtIfFsmStageDn,
       "cfprMgmtIfFsmStageRn": cfprMgmtIfFsmStageRn,
       "cfprMgmtIfFsmStageDescrData": cfprMgmtIfFsmStageDescrData,
       "cfprMgmtIfFsmStageLastUpdateTime": cfprMgmtIfFsmStageLastUpdateTime,
       "cfprMgmtIfFsmStageName": cfprMgmtIfFsmStageName,
       "cfprMgmtIfFsmStageOrder": cfprMgmtIfFsmStageOrder,
       "cfprMgmtIfFsmStageRetry": cfprMgmtIfFsmStageRetry,
       "cfprMgmtIfFsmStageStageStatus": cfprMgmtIfFsmStageStageStatus,
       "cfprMgmtIfFsmTaskTable": cfprMgmtIfFsmTaskTable,
       "cfprMgmtIfFsmTaskEntry": cfprMgmtIfFsmTaskEntry,
       "cfprMgmtIfFsmTaskInstanceId": cfprMgmtIfFsmTaskInstanceId,
       "cfprMgmtIfFsmTaskDn": cfprMgmtIfFsmTaskDn,
       "cfprMgmtIfFsmTaskRn": cfprMgmtIfFsmTaskRn,
       "cfprMgmtIfFsmTaskCompletion": cfprMgmtIfFsmTaskCompletion,
       "cfprMgmtIfFsmTaskFlags": cfprMgmtIfFsmTaskFlags,
       "cfprMgmtIfFsmTaskItem": cfprMgmtIfFsmTaskItem,
       "cfprMgmtIfFsmTaskSeqId": cfprMgmtIfFsmTaskSeqId,
       "cfprMgmtImporterTable": cfprMgmtImporterTable,
       "cfprMgmtImporterEntry": cfprMgmtImporterEntry,
       "cfprMgmtImporterInstanceId": cfprMgmtImporterInstanceId,
       "cfprMgmtImporterDn": cfprMgmtImporterDn,
       "cfprMgmtImporterRn": cfprMgmtImporterRn,
       "cfprMgmtImporterAction": cfprMgmtImporterAction,
       "cfprMgmtImporterAdminState": cfprMgmtImporterAdminState,
       "cfprMgmtImporterDescr": cfprMgmtImporterDescr,
       "cfprMgmtImporterFsmDescr": cfprMgmtImporterFsmDescr,
       "cfprMgmtImporterFsmPrev": cfprMgmtImporterFsmPrev,
       "cfprMgmtImporterFsmProgr": cfprMgmtImporterFsmProgr,
       "cfprMgmtImporterFsmRmtInvErrCode": cfprMgmtImporterFsmRmtInvErrCode,
       "cfprMgmtImporterFsmRmtInvErrDescr": cfprMgmtImporterFsmRmtInvErrDescr,
       "cfprMgmtImporterFsmRmtInvRslt": cfprMgmtImporterFsmRmtInvRslt,
       "cfprMgmtImporterFsmStageDescr": cfprMgmtImporterFsmStageDescr,
       "cfprMgmtImporterFsmStamp": cfprMgmtImporterFsmStamp,
       "cfprMgmtImporterFsmStatus": cfprMgmtImporterFsmStatus,
       "cfprMgmtImporterFsmTry": cfprMgmtImporterFsmTry,
       "cfprMgmtImporterHostname": cfprMgmtImporterHostname,
       "cfprMgmtImporterIntId": cfprMgmtImporterIntId,
       "cfprMgmtImporterName": cfprMgmtImporterName,
       "cfprMgmtImporterOperStatus": cfprMgmtImporterOperStatus,
       "cfprMgmtImporterPolicyLevel": cfprMgmtImporterPolicyLevel,
       "cfprMgmtImporterPolicyOwner": cfprMgmtImporterPolicyOwner,
       "cfprMgmtImporterPostAction": cfprMgmtImporterPostAction,
       "cfprMgmtImporterProto": cfprMgmtImporterProto,
       "cfprMgmtImporterPwd": cfprMgmtImporterPwd,
       "cfprMgmtImporterRemoteFile": cfprMgmtImporterRemoteFile,
       "cfprMgmtImporterUser": cfprMgmtImporterUser,
       "cfprMgmtImporterApplyingBreakoutCfg": cfprMgmtImporterApplyingBreakoutCfg,
       "cfprMgmtImporterPort": cfprMgmtImporterPort,
       "cfprMgmtImporterErrMsg": cfprMgmtImporterErrMsg,
       "cfprMgmtImporterFsmTable": cfprMgmtImporterFsmTable,
       "cfprMgmtImporterFsmEntry": cfprMgmtImporterFsmEntry,
       "cfprMgmtImporterFsmInstanceId": cfprMgmtImporterFsmInstanceId,
       "cfprMgmtImporterFsmDn": cfprMgmtImporterFsmDn,
       "cfprMgmtImporterFsmRn": cfprMgmtImporterFsmRn,
       "cfprMgmtImporterFsmCompletionTime": cfprMgmtImporterFsmCompletionTime,
       "cfprMgmtImporterFsmCurrentFsm": cfprMgmtImporterFsmCurrentFsm,
       "cfprMgmtImporterFsmDescrData": cfprMgmtImporterFsmDescrData,
       "cfprMgmtImporterFsmFsmStatus": cfprMgmtImporterFsmFsmStatus,
       "cfprMgmtImporterFsmProgress": cfprMgmtImporterFsmProgress,
       "cfprMgmtImporterFsmRmtErrCode": cfprMgmtImporterFsmRmtErrCode,
       "cfprMgmtImporterFsmRmtErrDescr": cfprMgmtImporterFsmRmtErrDescr,
       "cfprMgmtImporterFsmRmtRslt": cfprMgmtImporterFsmRmtRslt,
       "cfprMgmtImporterFsmStageTable": cfprMgmtImporterFsmStageTable,
       "cfprMgmtImporterFsmStageEntry": cfprMgmtImporterFsmStageEntry,
       "cfprMgmtImporterFsmStageInstanceId": cfprMgmtImporterFsmStageInstanceId,
       "cfprMgmtImporterFsmStageDn": cfprMgmtImporterFsmStageDn,
       "cfprMgmtImporterFsmStageRn": cfprMgmtImporterFsmStageRn,
       "cfprMgmtImporterFsmStageDescrData": cfprMgmtImporterFsmStageDescrData,
       "cfprMgmtImporterFsmStageLastUpdateTime": cfprMgmtImporterFsmStageLastUpdateTime,
       "cfprMgmtImporterFsmStageName": cfprMgmtImporterFsmStageName,
       "cfprMgmtImporterFsmStageOrder": cfprMgmtImporterFsmStageOrder,
       "cfprMgmtImporterFsmStageRetry": cfprMgmtImporterFsmStageRetry,
       "cfprMgmtImporterFsmStageStageStatus": cfprMgmtImporterFsmStageStageStatus,
       "cfprMgmtImporterFsmTaskTable": cfprMgmtImporterFsmTaskTable,
       "cfprMgmtImporterFsmTaskEntry": cfprMgmtImporterFsmTaskEntry,
       "cfprMgmtImporterFsmTaskInstanceId": cfprMgmtImporterFsmTaskInstanceId,
       "cfprMgmtImporterFsmTaskDn": cfprMgmtImporterFsmTaskDn,
       "cfprMgmtImporterFsmTaskRn": cfprMgmtImporterFsmTaskRn,
       "cfprMgmtImporterFsmTaskCompletion": cfprMgmtImporterFsmTaskCompletion,
       "cfprMgmtImporterFsmTaskFlags": cfprMgmtImporterFsmTaskFlags,
       "cfprMgmtImporterFsmTaskItem": cfprMgmtImporterFsmTaskItem,
       "cfprMgmtImporterFsmTaskSeqId": cfprMgmtImporterFsmTaskSeqId,
       "cfprMgmtInbandProfileTable": cfprMgmtInbandProfileTable,
       "cfprMgmtInbandProfileEntry": cfprMgmtInbandProfileEntry,
       "cfprMgmtInbandProfileInstanceId": cfprMgmtInbandProfileInstanceId,
       "cfprMgmtInbandProfileDn": cfprMgmtInbandProfileDn,
       "cfprMgmtInbandProfileRn": cfprMgmtInbandProfileRn,
       "cfprMgmtInbandProfileDefaultVlanName": cfprMgmtInbandProfileDefaultVlanName,
       "cfprMgmtInbandProfileName": cfprMgmtInbandProfileName,
       "cfprMgmtInbandProfilePoolName": cfprMgmtInbandProfilePoolName,
       "cfprMgmtIntAuthPolicyTable": cfprMgmtIntAuthPolicyTable,
       "cfprMgmtIntAuthPolicyEntry": cfprMgmtIntAuthPolicyEntry,
       "cfprMgmtIntAuthPolicyInstanceId": cfprMgmtIntAuthPolicyInstanceId,
       "cfprMgmtIntAuthPolicyDn": cfprMgmtIntAuthPolicyDn,
       "cfprMgmtIntAuthPolicyRn": cfprMgmtIntAuthPolicyRn,
       "cfprMgmtIntAuthPolicyMethod": cfprMgmtIntAuthPolicyMethod,
       "cfprMgmtIntAuthPolicyName": cfprMgmtIntAuthPolicyName,
       "cfprMgmtIntAuthPolicyPwd": cfprMgmtIntAuthPolicyPwd,
       "cfprMgmtInterfaceTable": cfprMgmtInterfaceTable,
       "cfprMgmtInterfaceEntry": cfprMgmtInterfaceEntry,
       "cfprMgmtInterfaceInstanceId": cfprMgmtInterfaceInstanceId,
       "cfprMgmtInterfaceDn": cfprMgmtInterfaceDn,
       "cfprMgmtInterfaceRn": cfprMgmtInterfaceRn,
       "cfprMgmtInterfaceConfigMessage": cfprMgmtInterfaceConfigMessage,
       "cfprMgmtInterfaceConfigState": cfprMgmtInterfaceConfigState,
       "cfprMgmtInterfaceIpV4State": cfprMgmtInterfaceIpV4State,
       "cfprMgmtInterfaceIpV6State": cfprMgmtInterfaceIpV6State,
       "cfprMgmtInterfaceIsDefaultDerived": cfprMgmtInterfaceIsDefaultDerived,
       "cfprMgmtInterfaceMode": cfprMgmtInterfaceMode,
       "cfprMgmtInterfaceOperState": cfprMgmtInterfaceOperState,
       "cfprMgmtPmonEntryTable": cfprMgmtPmonEntryTable,
       "cfprMgmtPmonEntryEntry": cfprMgmtPmonEntryEntry,
       "cfprMgmtPmonEntryInstanceId": cfprMgmtPmonEntryInstanceId,
       "cfprMgmtPmonEntryDn": cfprMgmtPmonEntryDn,
       "cfprMgmtPmonEntryRn": cfprMgmtPmonEntryRn,
       "cfprMgmtPmonEntryExitSignal": cfprMgmtPmonEntryExitSignal,
       "cfprMgmtPmonEntryFullPathname": cfprMgmtPmonEntryFullPathname,
       "cfprMgmtPmonEntryHeapSize": cfprMgmtPmonEntryHeapSize,
       "cfprMgmtPmonEntryHeapSize16Gb": cfprMgmtPmonEntryHeapSize16Gb,
       "cfprMgmtPmonEntryLastExitCode": cfprMgmtPmonEntryLastExitCode,
       "cfprMgmtPmonEntryMaxRetries": cfprMgmtPmonEntryMaxRetries,
       "cfprMgmtPmonEntryName": cfprMgmtPmonEntryName,
       "cfprMgmtPmonEntryRetries": cfprMgmtPmonEntryRetries,
       "cfprMgmtPmonEntrySpuriousRetries": cfprMgmtPmonEntrySpuriousRetries,
       "cfprMgmtPmonEntryState": cfprMgmtPmonEntryState,
       "cfprMgmtPmonEntrySwitchId": cfprMgmtPmonEntrySwitchId,
       "cfprMgmtPmonEntryWorkingDirectory": cfprMgmtPmonEntryWorkingDirectory,
       "cfprMgmtPmonEntryIsProcRestarted": cfprMgmtPmonEntryIsProcRestarted,
       "cfprMgmtProfDerivedInterfaceTable": cfprMgmtProfDerivedInterfaceTable,
       "cfprMgmtProfDerivedInterfaceEntry": cfprMgmtProfDerivedInterfaceEntry,
       "cfprMgmtProfDerivedInterfaceInstanceId": cfprMgmtProfDerivedInterfaceInstanceId,
       "cfprMgmtProfDerivedInterfaceDn": cfprMgmtProfDerivedInterfaceDn,
       "cfprMgmtProfDerivedInterfaceRn": cfprMgmtProfDerivedInterfaceRn,
       "cfprMgmtProfDerivedInterfaceConfigMessage": cfprMgmtProfDerivedInterfaceConfigMessage,
       "cfprMgmtProfDerivedInterfaceConfigState": cfprMgmtProfDerivedInterfaceConfigState,
       "cfprMgmtProfDerivedInterfaceIpV4State": cfprMgmtProfDerivedInterfaceIpV4State,
       "cfprMgmtProfDerivedInterfaceIpV6State": cfprMgmtProfDerivedInterfaceIpV6State,
       "cfprMgmtProfDerivedInterfaceMode": cfprMgmtProfDerivedInterfaceMode,
       "cfprMgmtProfDerivedInterfaceOperState": cfprMgmtProfDerivedInterfaceOperState,
       "cfprMgmtVnetTable": cfprMgmtVnetTable,
       "cfprMgmtVnetEntry": cfprMgmtVnetEntry,
       "cfprMgmtVnetInstanceId": cfprMgmtVnetInstanceId,
       "cfprMgmtVnetDn": cfprMgmtVnetDn,
       "cfprMgmtVnetRn": cfprMgmtVnetRn,
       "cfprMgmtVnetConfigState": cfprMgmtVnetConfigState,
       "cfprMgmtVnetId": cfprMgmtVnetId,
       "cfprMgmtVnetName": cfprMgmtVnetName,
       "cfprMgmtImportConfigInfoTable": cfprMgmtImportConfigInfoTable,
       "cfprMgmtImportConfigInfoEntry": cfprMgmtImportConfigInfoEntry,
       "cfprMgmtImportConfigInfoInstanceId": cfprMgmtImportConfigInfoInstanceId,
       "cfprMgmtImportConfigInfoDn": cfprMgmtImportConfigInfoDn,
       "cfprMgmtImportConfigInfoRn": cfprMgmtImportConfigInfoRn,
       "cfprMgmtImportConfigInfoImportDate": cfprMgmtImportConfigInfoImportDate}
)
