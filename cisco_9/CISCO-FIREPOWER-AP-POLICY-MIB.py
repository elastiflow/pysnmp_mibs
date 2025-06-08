# SNMP MIB module (CISCO-FIREPOWER-AP-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-POLICY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:27 2025
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
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApPolicyCleanupMode,
 CfprApPolicyControlEpFsmCurrentFsm,
 CfprApPolicyControlEpFsmStageName,
 CfprApPolicyControlEpFsmTaskItem,
 CfprApPolicyControlEpType,
 CfprApPolicyControlSource,
 CfprApPolicyControlledTypeFsmCurrentFsm,
 CfprApPolicyControlledTypeFsmStageName,
 CfprApPolicyControlledTypeFsmTaskItem,
 CfprApPolicyIdResolvePolicyType,
 CfprApPolicyPolicyOperStatus,
 CfprApPolicyPolicyOwner,
 CfprApPolicyPolicyResolveType,
 CfprApPolicyPolicyScopeFsmCurrentFsm,
 CfprApPolicyPolicyScopeFsmStageName,
 CfprApPolicyPolicyScopeFsmTaskItem,
 CfprApPolicyRegistrationStateType,
 CfprApPolicyRepairStateType,
 CfprApPolicyResumeAckState,
 CfprApPolicyState,
 CfprApPolicySuspendState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApPolicyCleanupMode",
    "CfprApPolicyControlEpFsmCurrentFsm",
    "CfprApPolicyControlEpFsmStageName",
    "CfprApPolicyControlEpFsmTaskItem",
    "CfprApPolicyControlEpType",
    "CfprApPolicyControlSource",
    "CfprApPolicyControlledTypeFsmCurrentFsm",
    "CfprApPolicyControlledTypeFsmStageName",
    "CfprApPolicyControlledTypeFsmTaskItem",
    "CfprApPolicyIdResolvePolicyType",
    "CfprApPolicyPolicyOperStatus",
    "CfprApPolicyPolicyOwner",
    "CfprApPolicyPolicyResolveType",
    "CfprApPolicyPolicyScopeFsmCurrentFsm",
    "CfprApPolicyPolicyScopeFsmStageName",
    "CfprApPolicyPolicyScopeFsmTaskItem",
    "CfprApPolicyRegistrationStateType",
    "CfprApPolicyRepairStateType",
    "CfprApPolicyResumeAckState",
    "CfprApPolicyState",
    "CfprApPolicySuspendState")

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

cfprApPolicyObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApPolicyCentraleSyncTable_Object = MibTable
cfprApPolicyCentraleSyncTable = _CfprApPolicyCentraleSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 1)
)
if mibBuilder.loadTexts:
    cfprApPolicyCentraleSyncTable.setStatus("current")
_CfprApPolicyCentraleSyncEntry_Object = MibTableRow
cfprApPolicyCentraleSyncEntry = _CfprApPolicyCentraleSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 1, 1)
)
cfprApPolicyCentraleSyncEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyCentraleSyncInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyCentraleSyncEntry.setStatus("current")
_CfprApPolicyCentraleSyncInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyCentraleSyncInstanceId_Object = MibTableColumn
cfprApPolicyCentraleSyncInstanceId = _CfprApPolicyCentraleSyncInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 1, 1, 1),
    _CfprApPolicyCentraleSyncInstanceId_Type()
)
cfprApPolicyCentraleSyncInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyCentraleSyncInstanceId.setStatus("current")
_CfprApPolicyCentraleSyncDn_Type = CfprApManagedObjectDn
_CfprApPolicyCentraleSyncDn_Object = MibTableColumn
cfprApPolicyCentraleSyncDn = _CfprApPolicyCentraleSyncDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 1, 1, 2),
    _CfprApPolicyCentraleSyncDn_Type()
)
cfprApPolicyCentraleSyncDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyCentraleSyncDn.setStatus("current")
_CfprApPolicyCentraleSyncRn_Type = SnmpAdminString
_CfprApPolicyCentraleSyncRn_Object = MibTableColumn
cfprApPolicyCentraleSyncRn = _CfprApPolicyCentraleSyncRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 1, 1, 3),
    _CfprApPolicyCentraleSyncRn_Type()
)
cfprApPolicyCentraleSyncRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyCentraleSyncRn.setStatus("current")
_CfprApPolicyCentraleSyncLeftData_Type = SnmpAdminString
_CfprApPolicyCentraleSyncLeftData_Object = MibTableColumn
cfprApPolicyCentraleSyncLeftData = _CfprApPolicyCentraleSyncLeftData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 1, 1, 4),
    _CfprApPolicyCentraleSyncLeftData_Type()
)
cfprApPolicyCentraleSyncLeftData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyCentraleSyncLeftData.setStatus("current")
_CfprApPolicyCentraleSyncRightData_Type = SnmpAdminString
_CfprApPolicyCentraleSyncRightData_Object = MibTableColumn
cfprApPolicyCentraleSyncRightData = _CfprApPolicyCentraleSyncRightData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 1, 1, 5),
    _CfprApPolicyCentraleSyncRightData_Type()
)
cfprApPolicyCentraleSyncRightData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyCentraleSyncRightData.setStatus("current")
_CfprApPolicyCommunicationTable_Object = MibTable
cfprApPolicyCommunicationTable = _CfprApPolicyCommunicationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 2)
)
if mibBuilder.loadTexts:
    cfprApPolicyCommunicationTable.setStatus("current")
_CfprApPolicyCommunicationEntry_Object = MibTableRow
cfprApPolicyCommunicationEntry = _CfprApPolicyCommunicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 2, 1)
)
cfprApPolicyCommunicationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyCommunicationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyCommunicationEntry.setStatus("current")
_CfprApPolicyCommunicationInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyCommunicationInstanceId_Object = MibTableColumn
cfprApPolicyCommunicationInstanceId = _CfprApPolicyCommunicationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 2, 1, 1),
    _CfprApPolicyCommunicationInstanceId_Type()
)
cfprApPolicyCommunicationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyCommunicationInstanceId.setStatus("current")
_CfprApPolicyCommunicationDn_Type = CfprApManagedObjectDn
_CfprApPolicyCommunicationDn_Object = MibTableColumn
cfprApPolicyCommunicationDn = _CfprApPolicyCommunicationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 2, 1, 2),
    _CfprApPolicyCommunicationDn_Type()
)
cfprApPolicyCommunicationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyCommunicationDn.setStatus("current")
_CfprApPolicyCommunicationRn_Type = SnmpAdminString
_CfprApPolicyCommunicationRn_Object = MibTableColumn
cfprApPolicyCommunicationRn = _CfprApPolicyCommunicationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 2, 1, 3),
    _CfprApPolicyCommunicationRn_Type()
)
cfprApPolicyCommunicationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyCommunicationRn.setStatus("current")
_CfprApPolicyCommunicationSource_Type = CfprApPolicyControlSource
_CfprApPolicyCommunicationSource_Object = MibTableColumn
cfprApPolicyCommunicationSource = _CfprApPolicyCommunicationSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 2, 1, 4),
    _CfprApPolicyCommunicationSource_Type()
)
cfprApPolicyCommunicationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyCommunicationSource.setStatus("current")
_CfprApPolicyConfigBackupTable_Object = MibTable
cfprApPolicyConfigBackupTable = _CfprApPolicyConfigBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 3)
)
if mibBuilder.loadTexts:
    cfprApPolicyConfigBackupTable.setStatus("current")
_CfprApPolicyConfigBackupEntry_Object = MibTableRow
cfprApPolicyConfigBackupEntry = _CfprApPolicyConfigBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 3, 1)
)
cfprApPolicyConfigBackupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyConfigBackupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyConfigBackupEntry.setStatus("current")
_CfprApPolicyConfigBackupInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyConfigBackupInstanceId_Object = MibTableColumn
cfprApPolicyConfigBackupInstanceId = _CfprApPolicyConfigBackupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 3, 1, 1),
    _CfprApPolicyConfigBackupInstanceId_Type()
)
cfprApPolicyConfigBackupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyConfigBackupInstanceId.setStatus("current")
_CfprApPolicyConfigBackupDn_Type = CfprApManagedObjectDn
_CfprApPolicyConfigBackupDn_Object = MibTableColumn
cfprApPolicyConfigBackupDn = _CfprApPolicyConfigBackupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 3, 1, 2),
    _CfprApPolicyConfigBackupDn_Type()
)
cfprApPolicyConfigBackupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyConfigBackupDn.setStatus("current")
_CfprApPolicyConfigBackupRn_Type = SnmpAdminString
_CfprApPolicyConfigBackupRn_Object = MibTableColumn
cfprApPolicyConfigBackupRn = _CfprApPolicyConfigBackupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 3, 1, 3),
    _CfprApPolicyConfigBackupRn_Type()
)
cfprApPolicyConfigBackupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyConfigBackupRn.setStatus("current")
_CfprApPolicyConfigBackupSource_Type = CfprApPolicyControlSource
_CfprApPolicyConfigBackupSource_Object = MibTableColumn
cfprApPolicyConfigBackupSource = _CfprApPolicyConfigBackupSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 3, 1, 4),
    _CfprApPolicyConfigBackupSource_Type()
)
cfprApPolicyConfigBackupSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyConfigBackupSource.setStatus("current")
_CfprApPolicyControlEpTable_Object = MibTable
cfprApPolicyControlEpTable = _CfprApPolicyControlEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4)
)
if mibBuilder.loadTexts:
    cfprApPolicyControlEpTable.setStatus("current")
_CfprApPolicyControlEpEntry_Object = MibTableRow
cfprApPolicyControlEpEntry = _CfprApPolicyControlEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1)
)
cfprApPolicyControlEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyControlEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyControlEpEntry.setStatus("current")
_CfprApPolicyControlEpInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyControlEpInstanceId_Object = MibTableColumn
cfprApPolicyControlEpInstanceId = _CfprApPolicyControlEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 1),
    _CfprApPolicyControlEpInstanceId_Type()
)
cfprApPolicyControlEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpInstanceId.setStatus("current")
_CfprApPolicyControlEpDn_Type = CfprApManagedObjectDn
_CfprApPolicyControlEpDn_Object = MibTableColumn
cfprApPolicyControlEpDn = _CfprApPolicyControlEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 2),
    _CfprApPolicyControlEpDn_Type()
)
cfprApPolicyControlEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpDn.setStatus("current")
_CfprApPolicyControlEpRn_Type = SnmpAdminString
_CfprApPolicyControlEpRn_Object = MibTableColumn
cfprApPolicyControlEpRn = _CfprApPolicyControlEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 3),
    _CfprApPolicyControlEpRn_Type()
)
cfprApPolicyControlEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpRn.setStatus("current")
_CfprApPolicyControlEpAckState_Type = CfprApPolicyResumeAckState
_CfprApPolicyControlEpAckState_Object = MibTableColumn
cfprApPolicyControlEpAckState = _CfprApPolicyControlEpAckState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 4),
    _CfprApPolicyControlEpAckState_Type()
)
cfprApPolicyControlEpAckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpAckState.setStatus("current")
_CfprApPolicyControlEpCleanupMode_Type = CfprApPolicyCleanupMode
_CfprApPolicyControlEpCleanupMode_Object = MibTableColumn
cfprApPolicyControlEpCleanupMode = _CfprApPolicyControlEpCleanupMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 5),
    _CfprApPolicyControlEpCleanupMode_Type()
)
cfprApPolicyControlEpCleanupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpCleanupMode.setStatus("current")
_CfprApPolicyControlEpEncSecret_Type = SnmpAdminString
_CfprApPolicyControlEpEncSecret_Object = MibTableColumn
cfprApPolicyControlEpEncSecret = _CfprApPolicyControlEpEncSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 6),
    _CfprApPolicyControlEpEncSecret_Type()
)
cfprApPolicyControlEpEncSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpEncSecret.setStatus("current")
_CfprApPolicyControlEpFsmDescr_Type = SnmpAdminString
_CfprApPolicyControlEpFsmDescr_Object = MibTableColumn
cfprApPolicyControlEpFsmDescr = _CfprApPolicyControlEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 7),
    _CfprApPolicyControlEpFsmDescr_Type()
)
cfprApPolicyControlEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmDescr.setStatus("current")
_CfprApPolicyControlEpFsmPrev_Type = SnmpAdminString
_CfprApPolicyControlEpFsmPrev_Object = MibTableColumn
cfprApPolicyControlEpFsmPrev = _CfprApPolicyControlEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 8),
    _CfprApPolicyControlEpFsmPrev_Type()
)
cfprApPolicyControlEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmPrev.setStatus("current")
_CfprApPolicyControlEpFsmProgr_Type = Gauge32
_CfprApPolicyControlEpFsmProgr_Object = MibTableColumn
cfprApPolicyControlEpFsmProgr = _CfprApPolicyControlEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 9),
    _CfprApPolicyControlEpFsmProgr_Type()
)
cfprApPolicyControlEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmProgr.setStatus("current")
_CfprApPolicyControlEpFsmRmtInvErrCode_Type = Gauge32
_CfprApPolicyControlEpFsmRmtInvErrCode_Object = MibTableColumn
cfprApPolicyControlEpFsmRmtInvErrCode = _CfprApPolicyControlEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 10),
    _CfprApPolicyControlEpFsmRmtInvErrCode_Type()
)
cfprApPolicyControlEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmRmtInvErrCode.setStatus("current")
_CfprApPolicyControlEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApPolicyControlEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprApPolicyControlEpFsmRmtInvErrDescr = _CfprApPolicyControlEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 11),
    _CfprApPolicyControlEpFsmRmtInvErrDescr_Type()
)
cfprApPolicyControlEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmRmtInvErrDescr.setStatus("current")
_CfprApPolicyControlEpFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApPolicyControlEpFsmRmtInvRslt_Object = MibTableColumn
cfprApPolicyControlEpFsmRmtInvRslt = _CfprApPolicyControlEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 12),
    _CfprApPolicyControlEpFsmRmtInvRslt_Type()
)
cfprApPolicyControlEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmRmtInvRslt.setStatus("current")
_CfprApPolicyControlEpFsmStageDescr_Type = SnmpAdminString
_CfprApPolicyControlEpFsmStageDescr_Object = MibTableColumn
cfprApPolicyControlEpFsmStageDescr = _CfprApPolicyControlEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 13),
    _CfprApPolicyControlEpFsmStageDescr_Type()
)
cfprApPolicyControlEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStageDescr.setStatus("current")
_CfprApPolicyControlEpFsmStamp_Type = DateAndTime
_CfprApPolicyControlEpFsmStamp_Object = MibTableColumn
cfprApPolicyControlEpFsmStamp = _CfprApPolicyControlEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 14),
    _CfprApPolicyControlEpFsmStamp_Type()
)
cfprApPolicyControlEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStamp.setStatus("current")
_CfprApPolicyControlEpFsmStatus_Type = SnmpAdminString
_CfprApPolicyControlEpFsmStatus_Object = MibTableColumn
cfprApPolicyControlEpFsmStatus = _CfprApPolicyControlEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 15),
    _CfprApPolicyControlEpFsmStatus_Type()
)
cfprApPolicyControlEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStatus.setStatus("current")
_CfprApPolicyControlEpFsmTry_Type = Gauge32
_CfprApPolicyControlEpFsmTry_Object = MibTableColumn
cfprApPolicyControlEpFsmTry = _CfprApPolicyControlEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 16),
    _CfprApPolicyControlEpFsmTry_Type()
)
cfprApPolicyControlEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmTry.setStatus("current")
_CfprApPolicyControlEpName_Type = SnmpAdminString
_CfprApPolicyControlEpName_Object = MibTableColumn
cfprApPolicyControlEpName = _CfprApPolicyControlEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 17),
    _CfprApPolicyControlEpName_Type()
)
cfprApPolicyControlEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpName.setStatus("current")
_CfprApPolicyControlEpRegistrationState_Type = CfprApPolicyRegistrationStateType
_CfprApPolicyControlEpRegistrationState_Object = MibTableColumn
cfprApPolicyControlEpRegistrationState = _CfprApPolicyControlEpRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 18),
    _CfprApPolicyControlEpRegistrationState_Type()
)
cfprApPolicyControlEpRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpRegistrationState.setStatus("current")
_CfprApPolicyControlEpRepairState_Type = CfprApPolicyRepairStateType
_CfprApPolicyControlEpRepairState_Object = MibTableColumn
cfprApPolicyControlEpRepairState = _CfprApPolicyControlEpRepairState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 19),
    _CfprApPolicyControlEpRepairState_Type()
)
cfprApPolicyControlEpRepairState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpRepairState.setStatus("current")
_CfprApPolicyControlEpSecret_Type = SnmpAdminString
_CfprApPolicyControlEpSecret_Object = MibTableColumn
cfprApPolicyControlEpSecret = _CfprApPolicyControlEpSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 20),
    _CfprApPolicyControlEpSecret_Type()
)
cfprApPolicyControlEpSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpSecret.setStatus("current")
_CfprApPolicyControlEpState_Type = CfprApPolicyState
_CfprApPolicyControlEpState_Object = MibTableColumn
cfprApPolicyControlEpState = _CfprApPolicyControlEpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 21),
    _CfprApPolicyControlEpState_Type()
)
cfprApPolicyControlEpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpState.setStatus("current")
_CfprApPolicyControlEpSuspendState_Type = CfprApPolicySuspendState
_CfprApPolicyControlEpSuspendState_Object = MibTableColumn
cfprApPolicyControlEpSuspendState = _CfprApPolicyControlEpSuspendState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 22),
    _CfprApPolicyControlEpSuspendState_Type()
)
cfprApPolicyControlEpSuspendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpSuspendState.setStatus("current")
_CfprApPolicyControlEpSvcRegIP_Type = InetAddressIPv4
_CfprApPolicyControlEpSvcRegIP_Object = MibTableColumn
cfprApPolicyControlEpSvcRegIP = _CfprApPolicyControlEpSvcRegIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 23),
    _CfprApPolicyControlEpSvcRegIP_Type()
)
cfprApPolicyControlEpSvcRegIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpSvcRegIP.setStatus("current")
_CfprApPolicyControlEpSvcRegName_Type = SnmpAdminString
_CfprApPolicyControlEpSvcRegName_Object = MibTableColumn
cfprApPolicyControlEpSvcRegName = _CfprApPolicyControlEpSvcRegName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 24),
    _CfprApPolicyControlEpSvcRegName_Type()
)
cfprApPolicyControlEpSvcRegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpSvcRegName.setStatus("current")
_CfprApPolicyControlEpType_Type = CfprApPolicyControlEpType
_CfprApPolicyControlEpType_Object = MibTableColumn
cfprApPolicyControlEpType = _CfprApPolicyControlEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 4, 1, 25),
    _CfprApPolicyControlEpType_Type()
)
cfprApPolicyControlEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpType.setStatus("current")
_CfprApPolicyControlEpFsmTable_Object = MibTable
cfprApPolicyControlEpFsmTable = _CfprApPolicyControlEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5)
)
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmTable.setStatus("current")
_CfprApPolicyControlEpFsmEntry_Object = MibTableRow
cfprApPolicyControlEpFsmEntry = _CfprApPolicyControlEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5, 1)
)
cfprApPolicyControlEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyControlEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmEntry.setStatus("current")
_CfprApPolicyControlEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyControlEpFsmInstanceId_Object = MibTableColumn
cfprApPolicyControlEpFsmInstanceId = _CfprApPolicyControlEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5, 1, 1),
    _CfprApPolicyControlEpFsmInstanceId_Type()
)
cfprApPolicyControlEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmInstanceId.setStatus("current")
_CfprApPolicyControlEpFsmDn_Type = CfprApManagedObjectDn
_CfprApPolicyControlEpFsmDn_Object = MibTableColumn
cfprApPolicyControlEpFsmDn = _CfprApPolicyControlEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5, 1, 2),
    _CfprApPolicyControlEpFsmDn_Type()
)
cfprApPolicyControlEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmDn.setStatus("current")
_CfprApPolicyControlEpFsmRn_Type = SnmpAdminString
_CfprApPolicyControlEpFsmRn_Object = MibTableColumn
cfprApPolicyControlEpFsmRn = _CfprApPolicyControlEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5, 1, 3),
    _CfprApPolicyControlEpFsmRn_Type()
)
cfprApPolicyControlEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmRn.setStatus("current")
_CfprApPolicyControlEpFsmCompletionTime_Type = DateAndTime
_CfprApPolicyControlEpFsmCompletionTime_Object = MibTableColumn
cfprApPolicyControlEpFsmCompletionTime = _CfprApPolicyControlEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5, 1, 4),
    _CfprApPolicyControlEpFsmCompletionTime_Type()
)
cfprApPolicyControlEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmCompletionTime.setStatus("current")
_CfprApPolicyControlEpFsmCurrentFsm_Type = CfprApPolicyControlEpFsmCurrentFsm
_CfprApPolicyControlEpFsmCurrentFsm_Object = MibTableColumn
cfprApPolicyControlEpFsmCurrentFsm = _CfprApPolicyControlEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5, 1, 5),
    _CfprApPolicyControlEpFsmCurrentFsm_Type()
)
cfprApPolicyControlEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmCurrentFsm.setStatus("current")
_CfprApPolicyControlEpFsmDescrData_Type = SnmpAdminString
_CfprApPolicyControlEpFsmDescrData_Object = MibTableColumn
cfprApPolicyControlEpFsmDescrData = _CfprApPolicyControlEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5, 1, 6),
    _CfprApPolicyControlEpFsmDescrData_Type()
)
cfprApPolicyControlEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmDescrData.setStatus("current")
_CfprApPolicyControlEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApPolicyControlEpFsmFsmStatus_Object = MibTableColumn
cfprApPolicyControlEpFsmFsmStatus = _CfprApPolicyControlEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5, 1, 7),
    _CfprApPolicyControlEpFsmFsmStatus_Type()
)
cfprApPolicyControlEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmFsmStatus.setStatus("current")
_CfprApPolicyControlEpFsmProgress_Type = Gauge32
_CfprApPolicyControlEpFsmProgress_Object = MibTableColumn
cfprApPolicyControlEpFsmProgress = _CfprApPolicyControlEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5, 1, 8),
    _CfprApPolicyControlEpFsmProgress_Type()
)
cfprApPolicyControlEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmProgress.setStatus("current")
_CfprApPolicyControlEpFsmRmtErrCode_Type = Gauge32
_CfprApPolicyControlEpFsmRmtErrCode_Object = MibTableColumn
cfprApPolicyControlEpFsmRmtErrCode = _CfprApPolicyControlEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5, 1, 9),
    _CfprApPolicyControlEpFsmRmtErrCode_Type()
)
cfprApPolicyControlEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmRmtErrCode.setStatus("current")
_CfprApPolicyControlEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApPolicyControlEpFsmRmtErrDescr_Object = MibTableColumn
cfprApPolicyControlEpFsmRmtErrDescr = _CfprApPolicyControlEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5, 1, 10),
    _CfprApPolicyControlEpFsmRmtErrDescr_Type()
)
cfprApPolicyControlEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmRmtErrDescr.setStatus("current")
_CfprApPolicyControlEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApPolicyControlEpFsmRmtRslt_Object = MibTableColumn
cfprApPolicyControlEpFsmRmtRslt = _CfprApPolicyControlEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 5, 1, 11),
    _CfprApPolicyControlEpFsmRmtRslt_Type()
)
cfprApPolicyControlEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmRmtRslt.setStatus("current")
_CfprApPolicyControlEpFsmStageTable_Object = MibTable
cfprApPolicyControlEpFsmStageTable = _CfprApPolicyControlEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 6)
)
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStageTable.setStatus("current")
_CfprApPolicyControlEpFsmStageEntry_Object = MibTableRow
cfprApPolicyControlEpFsmStageEntry = _CfprApPolicyControlEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 6, 1)
)
cfprApPolicyControlEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyControlEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStageEntry.setStatus("current")
_CfprApPolicyControlEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyControlEpFsmStageInstanceId_Object = MibTableColumn
cfprApPolicyControlEpFsmStageInstanceId = _CfprApPolicyControlEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 6, 1, 1),
    _CfprApPolicyControlEpFsmStageInstanceId_Type()
)
cfprApPolicyControlEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStageInstanceId.setStatus("current")
_CfprApPolicyControlEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApPolicyControlEpFsmStageDn_Object = MibTableColumn
cfprApPolicyControlEpFsmStageDn = _CfprApPolicyControlEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 6, 1, 2),
    _CfprApPolicyControlEpFsmStageDn_Type()
)
cfprApPolicyControlEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStageDn.setStatus("current")
_CfprApPolicyControlEpFsmStageRn_Type = SnmpAdminString
_CfprApPolicyControlEpFsmStageRn_Object = MibTableColumn
cfprApPolicyControlEpFsmStageRn = _CfprApPolicyControlEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 6, 1, 3),
    _CfprApPolicyControlEpFsmStageRn_Type()
)
cfprApPolicyControlEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStageRn.setStatus("current")
_CfprApPolicyControlEpFsmStageDescrData_Type = SnmpAdminString
_CfprApPolicyControlEpFsmStageDescrData_Object = MibTableColumn
cfprApPolicyControlEpFsmStageDescrData = _CfprApPolicyControlEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 6, 1, 4),
    _CfprApPolicyControlEpFsmStageDescrData_Type()
)
cfprApPolicyControlEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStageDescrData.setStatus("current")
_CfprApPolicyControlEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApPolicyControlEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApPolicyControlEpFsmStageLastUpdateTime = _CfprApPolicyControlEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 6, 1, 5),
    _CfprApPolicyControlEpFsmStageLastUpdateTime_Type()
)
cfprApPolicyControlEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStageLastUpdateTime.setStatus("current")
_CfprApPolicyControlEpFsmStageName_Type = CfprApPolicyControlEpFsmStageName
_CfprApPolicyControlEpFsmStageName_Object = MibTableColumn
cfprApPolicyControlEpFsmStageName = _CfprApPolicyControlEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 6, 1, 6),
    _CfprApPolicyControlEpFsmStageName_Type()
)
cfprApPolicyControlEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStageName.setStatus("current")
_CfprApPolicyControlEpFsmStageOrder_Type = Gauge32
_CfprApPolicyControlEpFsmStageOrder_Object = MibTableColumn
cfprApPolicyControlEpFsmStageOrder = _CfprApPolicyControlEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 6, 1, 7),
    _CfprApPolicyControlEpFsmStageOrder_Type()
)
cfprApPolicyControlEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStageOrder.setStatus("current")
_CfprApPolicyControlEpFsmStageRetry_Type = Gauge32
_CfprApPolicyControlEpFsmStageRetry_Object = MibTableColumn
cfprApPolicyControlEpFsmStageRetry = _CfprApPolicyControlEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 6, 1, 8),
    _CfprApPolicyControlEpFsmStageRetry_Type()
)
cfprApPolicyControlEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStageRetry.setStatus("current")
_CfprApPolicyControlEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApPolicyControlEpFsmStageStageStatus_Object = MibTableColumn
cfprApPolicyControlEpFsmStageStageStatus = _CfprApPolicyControlEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 6, 1, 9),
    _CfprApPolicyControlEpFsmStageStageStatus_Type()
)
cfprApPolicyControlEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmStageStageStatus.setStatus("current")
_CfprApPolicyControlEpFsmTaskTable_Object = MibTable
cfprApPolicyControlEpFsmTaskTable = _CfprApPolicyControlEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 7)
)
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmTaskTable.setStatus("current")
_CfprApPolicyControlEpFsmTaskEntry_Object = MibTableRow
cfprApPolicyControlEpFsmTaskEntry = _CfprApPolicyControlEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 7, 1)
)
cfprApPolicyControlEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyControlEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmTaskEntry.setStatus("current")
_CfprApPolicyControlEpFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyControlEpFsmTaskInstanceId_Object = MibTableColumn
cfprApPolicyControlEpFsmTaskInstanceId = _CfprApPolicyControlEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 7, 1, 1),
    _CfprApPolicyControlEpFsmTaskInstanceId_Type()
)
cfprApPolicyControlEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmTaskInstanceId.setStatus("current")
_CfprApPolicyControlEpFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApPolicyControlEpFsmTaskDn_Object = MibTableColumn
cfprApPolicyControlEpFsmTaskDn = _CfprApPolicyControlEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 7, 1, 2),
    _CfprApPolicyControlEpFsmTaskDn_Type()
)
cfprApPolicyControlEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmTaskDn.setStatus("current")
_CfprApPolicyControlEpFsmTaskRn_Type = SnmpAdminString
_CfprApPolicyControlEpFsmTaskRn_Object = MibTableColumn
cfprApPolicyControlEpFsmTaskRn = _CfprApPolicyControlEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 7, 1, 3),
    _CfprApPolicyControlEpFsmTaskRn_Type()
)
cfprApPolicyControlEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmTaskRn.setStatus("current")
_CfprApPolicyControlEpFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApPolicyControlEpFsmTaskCompletion_Object = MibTableColumn
cfprApPolicyControlEpFsmTaskCompletion = _CfprApPolicyControlEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 7, 1, 4),
    _CfprApPolicyControlEpFsmTaskCompletion_Type()
)
cfprApPolicyControlEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmTaskCompletion.setStatus("current")
_CfprApPolicyControlEpFsmTaskFlags_Type = CfprApFsmFlags
_CfprApPolicyControlEpFsmTaskFlags_Object = MibTableColumn
cfprApPolicyControlEpFsmTaskFlags = _CfprApPolicyControlEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 7, 1, 5),
    _CfprApPolicyControlEpFsmTaskFlags_Type()
)
cfprApPolicyControlEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmTaskFlags.setStatus("current")
_CfprApPolicyControlEpFsmTaskItem_Type = CfprApPolicyControlEpFsmTaskItem
_CfprApPolicyControlEpFsmTaskItem_Object = MibTableColumn
cfprApPolicyControlEpFsmTaskItem = _CfprApPolicyControlEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 7, 1, 6),
    _CfprApPolicyControlEpFsmTaskItem_Type()
)
cfprApPolicyControlEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmTaskItem.setStatus("current")
_CfprApPolicyControlEpFsmTaskSeqId_Type = Gauge32
_CfprApPolicyControlEpFsmTaskSeqId_Object = MibTableColumn
cfprApPolicyControlEpFsmTaskSeqId = _CfprApPolicyControlEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 7, 1, 7),
    _CfprApPolicyControlEpFsmTaskSeqId_Type()
)
cfprApPolicyControlEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlEpFsmTaskSeqId.setStatus("current")
_CfprApPolicyControlledInstanceTable_Object = MibTable
cfprApPolicyControlledInstanceTable = _CfprApPolicyControlledInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 8)
)
if mibBuilder.loadTexts:
    cfprApPolicyControlledInstanceTable.setStatus("current")
_CfprApPolicyControlledInstanceEntry_Object = MibTableRow
cfprApPolicyControlledInstanceEntry = _CfprApPolicyControlledInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 8, 1)
)
cfprApPolicyControlledInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyControlledInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyControlledInstanceEntry.setStatus("current")
_CfprApPolicyControlledInstanceInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyControlledInstanceInstanceId_Object = MibTableColumn
cfprApPolicyControlledInstanceInstanceId = _CfprApPolicyControlledInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 8, 1, 1),
    _CfprApPolicyControlledInstanceInstanceId_Type()
)
cfprApPolicyControlledInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyControlledInstanceInstanceId.setStatus("current")
_CfprApPolicyControlledInstanceDn_Type = CfprApManagedObjectDn
_CfprApPolicyControlledInstanceDn_Object = MibTableColumn
cfprApPolicyControlledInstanceDn = _CfprApPolicyControlledInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 8, 1, 2),
    _CfprApPolicyControlledInstanceDn_Type()
)
cfprApPolicyControlledInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledInstanceDn.setStatus("current")
_CfprApPolicyControlledInstanceRn_Type = SnmpAdminString
_CfprApPolicyControlledInstanceRn_Object = MibTableColumn
cfprApPolicyControlledInstanceRn = _CfprApPolicyControlledInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 8, 1, 3),
    _CfprApPolicyControlledInstanceRn_Type()
)
cfprApPolicyControlledInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledInstanceRn.setStatus("current")
_CfprApPolicyControlledInstanceDefDn_Type = SnmpAdminString
_CfprApPolicyControlledInstanceDefDn_Object = MibTableColumn
cfprApPolicyControlledInstanceDefDn = _CfprApPolicyControlledInstanceDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 8, 1, 4),
    _CfprApPolicyControlledInstanceDefDn_Type()
)
cfprApPolicyControlledInstanceDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledInstanceDefDn.setStatus("current")
_CfprApPolicyControlledInstanceExternalResolveName_Type = SnmpAdminString
_CfprApPolicyControlledInstanceExternalResolveName_Object = MibTableColumn
cfprApPolicyControlledInstanceExternalResolveName = _CfprApPolicyControlledInstanceExternalResolveName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 8, 1, 5),
    _CfprApPolicyControlledInstanceExternalResolveName_Type()
)
cfprApPolicyControlledInstanceExternalResolveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledInstanceExternalResolveName.setStatus("current")
_CfprApPolicyControlledInstanceName_Type = SnmpAdminString
_CfprApPolicyControlledInstanceName_Object = MibTableColumn
cfprApPolicyControlledInstanceName = _CfprApPolicyControlledInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 8, 1, 6),
    _CfprApPolicyControlledInstanceName_Type()
)
cfprApPolicyControlledInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledInstanceName.setStatus("current")
_CfprApPolicyControlledInstanceResolveType_Type = CfprApPolicyPolicyResolveType
_CfprApPolicyControlledInstanceResolveType_Object = MibTableColumn
cfprApPolicyControlledInstanceResolveType = _CfprApPolicyControlledInstanceResolveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 8, 1, 7),
    _CfprApPolicyControlledInstanceResolveType_Type()
)
cfprApPolicyControlledInstanceResolveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledInstanceResolveType.setStatus("current")
_CfprApPolicyControlledInstanceType_Type = SnmpAdminString
_CfprApPolicyControlledInstanceType_Object = MibTableColumn
cfprApPolicyControlledInstanceType = _CfprApPolicyControlledInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 8, 1, 8),
    _CfprApPolicyControlledInstanceType_Type()
)
cfprApPolicyControlledInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledInstanceType.setStatus("current")
_CfprApPolicyControlledTypeTable_Object = MibTable
cfprApPolicyControlledTypeTable = _CfprApPolicyControlledTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9)
)
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeTable.setStatus("current")
_CfprApPolicyControlledTypeEntry_Object = MibTableRow
cfprApPolicyControlledTypeEntry = _CfprApPolicyControlledTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1)
)
cfprApPolicyControlledTypeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyControlledTypeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeEntry.setStatus("current")
_CfprApPolicyControlledTypeInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyControlledTypeInstanceId_Object = MibTableColumn
cfprApPolicyControlledTypeInstanceId = _CfprApPolicyControlledTypeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 1),
    _CfprApPolicyControlledTypeInstanceId_Type()
)
cfprApPolicyControlledTypeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeInstanceId.setStatus("current")
_CfprApPolicyControlledTypeDn_Type = CfprApManagedObjectDn
_CfprApPolicyControlledTypeDn_Object = MibTableColumn
cfprApPolicyControlledTypeDn = _CfprApPolicyControlledTypeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 2),
    _CfprApPolicyControlledTypeDn_Type()
)
cfprApPolicyControlledTypeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeDn.setStatus("current")
_CfprApPolicyControlledTypeRn_Type = SnmpAdminString
_CfprApPolicyControlledTypeRn_Object = MibTableColumn
cfprApPolicyControlledTypeRn = _CfprApPolicyControlledTypeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 3),
    _CfprApPolicyControlledTypeRn_Type()
)
cfprApPolicyControlledTypeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeRn.setStatus("current")
_CfprApPolicyControlledTypeFsmDescr_Type = SnmpAdminString
_CfprApPolicyControlledTypeFsmDescr_Object = MibTableColumn
cfprApPolicyControlledTypeFsmDescr = _CfprApPolicyControlledTypeFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 4),
    _CfprApPolicyControlledTypeFsmDescr_Type()
)
cfprApPolicyControlledTypeFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmDescr.setStatus("current")
_CfprApPolicyControlledTypeFsmPrev_Type = SnmpAdminString
_CfprApPolicyControlledTypeFsmPrev_Object = MibTableColumn
cfprApPolicyControlledTypeFsmPrev = _CfprApPolicyControlledTypeFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 5),
    _CfprApPolicyControlledTypeFsmPrev_Type()
)
cfprApPolicyControlledTypeFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmPrev.setStatus("current")
_CfprApPolicyControlledTypeFsmProgr_Type = Gauge32
_CfprApPolicyControlledTypeFsmProgr_Object = MibTableColumn
cfprApPolicyControlledTypeFsmProgr = _CfprApPolicyControlledTypeFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 6),
    _CfprApPolicyControlledTypeFsmProgr_Type()
)
cfprApPolicyControlledTypeFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmProgr.setStatus("current")
_CfprApPolicyControlledTypeFsmRmtInvErrCode_Type = Gauge32
_CfprApPolicyControlledTypeFsmRmtInvErrCode_Object = MibTableColumn
cfprApPolicyControlledTypeFsmRmtInvErrCode = _CfprApPolicyControlledTypeFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 7),
    _CfprApPolicyControlledTypeFsmRmtInvErrCode_Type()
)
cfprApPolicyControlledTypeFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmRmtInvErrCode.setStatus("current")
_CfprApPolicyControlledTypeFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApPolicyControlledTypeFsmRmtInvErrDescr_Object = MibTableColumn
cfprApPolicyControlledTypeFsmRmtInvErrDescr = _CfprApPolicyControlledTypeFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 8),
    _CfprApPolicyControlledTypeFsmRmtInvErrDescr_Type()
)
cfprApPolicyControlledTypeFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmRmtInvErrDescr.setStatus("current")
_CfprApPolicyControlledTypeFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApPolicyControlledTypeFsmRmtInvRslt_Object = MibTableColumn
cfprApPolicyControlledTypeFsmRmtInvRslt = _CfprApPolicyControlledTypeFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 9),
    _CfprApPolicyControlledTypeFsmRmtInvRslt_Type()
)
cfprApPolicyControlledTypeFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmRmtInvRslt.setStatus("current")
_CfprApPolicyControlledTypeFsmStageDescr_Type = SnmpAdminString
_CfprApPolicyControlledTypeFsmStageDescr_Object = MibTableColumn
cfprApPolicyControlledTypeFsmStageDescr = _CfprApPolicyControlledTypeFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 10),
    _CfprApPolicyControlledTypeFsmStageDescr_Type()
)
cfprApPolicyControlledTypeFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStageDescr.setStatus("current")
_CfprApPolicyControlledTypeFsmStamp_Type = DateAndTime
_CfprApPolicyControlledTypeFsmStamp_Object = MibTableColumn
cfprApPolicyControlledTypeFsmStamp = _CfprApPolicyControlledTypeFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 11),
    _CfprApPolicyControlledTypeFsmStamp_Type()
)
cfprApPolicyControlledTypeFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStamp.setStatus("current")
_CfprApPolicyControlledTypeFsmStatus_Type = SnmpAdminString
_CfprApPolicyControlledTypeFsmStatus_Object = MibTableColumn
cfprApPolicyControlledTypeFsmStatus = _CfprApPolicyControlledTypeFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 12),
    _CfprApPolicyControlledTypeFsmStatus_Type()
)
cfprApPolicyControlledTypeFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStatus.setStatus("current")
_CfprApPolicyControlledTypeFsmTry_Type = Gauge32
_CfprApPolicyControlledTypeFsmTry_Object = MibTableColumn
cfprApPolicyControlledTypeFsmTry = _CfprApPolicyControlledTypeFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 13),
    _CfprApPolicyControlledTypeFsmTry_Type()
)
cfprApPolicyControlledTypeFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmTry.setStatus("current")
_CfprApPolicyControlledTypeParentContext_Type = SnmpAdminString
_CfprApPolicyControlledTypeParentContext_Object = MibTableColumn
cfprApPolicyControlledTypeParentContext = _CfprApPolicyControlledTypeParentContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 14),
    _CfprApPolicyControlledTypeParentContext_Type()
)
cfprApPolicyControlledTypeParentContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeParentContext.setStatus("current")
_CfprApPolicyControlledTypeType_Type = SnmpAdminString
_CfprApPolicyControlledTypeType_Object = MibTableColumn
cfprApPolicyControlledTypeType = _CfprApPolicyControlledTypeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 9, 1, 15),
    _CfprApPolicyControlledTypeType_Type()
)
cfprApPolicyControlledTypeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeType.setStatus("current")
_CfprApPolicyControlledTypeFsmTable_Object = MibTable
cfprApPolicyControlledTypeFsmTable = _CfprApPolicyControlledTypeFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10)
)
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmTable.setStatus("current")
_CfprApPolicyControlledTypeFsmEntry_Object = MibTableRow
cfprApPolicyControlledTypeFsmEntry = _CfprApPolicyControlledTypeFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10, 1)
)
cfprApPolicyControlledTypeFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyControlledTypeFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmEntry.setStatus("current")
_CfprApPolicyControlledTypeFsmInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyControlledTypeFsmInstanceId_Object = MibTableColumn
cfprApPolicyControlledTypeFsmInstanceId = _CfprApPolicyControlledTypeFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10, 1, 1),
    _CfprApPolicyControlledTypeFsmInstanceId_Type()
)
cfprApPolicyControlledTypeFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmInstanceId.setStatus("current")
_CfprApPolicyControlledTypeFsmDn_Type = CfprApManagedObjectDn
_CfprApPolicyControlledTypeFsmDn_Object = MibTableColumn
cfprApPolicyControlledTypeFsmDn = _CfprApPolicyControlledTypeFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10, 1, 2),
    _CfprApPolicyControlledTypeFsmDn_Type()
)
cfprApPolicyControlledTypeFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmDn.setStatus("current")
_CfprApPolicyControlledTypeFsmRn_Type = SnmpAdminString
_CfprApPolicyControlledTypeFsmRn_Object = MibTableColumn
cfprApPolicyControlledTypeFsmRn = _CfprApPolicyControlledTypeFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10, 1, 3),
    _CfprApPolicyControlledTypeFsmRn_Type()
)
cfprApPolicyControlledTypeFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmRn.setStatus("current")
_CfprApPolicyControlledTypeFsmCompletionTime_Type = DateAndTime
_CfprApPolicyControlledTypeFsmCompletionTime_Object = MibTableColumn
cfprApPolicyControlledTypeFsmCompletionTime = _CfprApPolicyControlledTypeFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10, 1, 4),
    _CfprApPolicyControlledTypeFsmCompletionTime_Type()
)
cfprApPolicyControlledTypeFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmCompletionTime.setStatus("current")
_CfprApPolicyControlledTypeFsmCurrentFsm_Type = CfprApPolicyControlledTypeFsmCurrentFsm
_CfprApPolicyControlledTypeFsmCurrentFsm_Object = MibTableColumn
cfprApPolicyControlledTypeFsmCurrentFsm = _CfprApPolicyControlledTypeFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10, 1, 5),
    _CfprApPolicyControlledTypeFsmCurrentFsm_Type()
)
cfprApPolicyControlledTypeFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmCurrentFsm.setStatus("current")
_CfprApPolicyControlledTypeFsmDescrData_Type = SnmpAdminString
_CfprApPolicyControlledTypeFsmDescrData_Object = MibTableColumn
cfprApPolicyControlledTypeFsmDescrData = _CfprApPolicyControlledTypeFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10, 1, 6),
    _CfprApPolicyControlledTypeFsmDescrData_Type()
)
cfprApPolicyControlledTypeFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmDescrData.setStatus("current")
_CfprApPolicyControlledTypeFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApPolicyControlledTypeFsmFsmStatus_Object = MibTableColumn
cfprApPolicyControlledTypeFsmFsmStatus = _CfprApPolicyControlledTypeFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10, 1, 7),
    _CfprApPolicyControlledTypeFsmFsmStatus_Type()
)
cfprApPolicyControlledTypeFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmFsmStatus.setStatus("current")
_CfprApPolicyControlledTypeFsmProgress_Type = Gauge32
_CfprApPolicyControlledTypeFsmProgress_Object = MibTableColumn
cfprApPolicyControlledTypeFsmProgress = _CfprApPolicyControlledTypeFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10, 1, 8),
    _CfprApPolicyControlledTypeFsmProgress_Type()
)
cfprApPolicyControlledTypeFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmProgress.setStatus("current")
_CfprApPolicyControlledTypeFsmRmtErrCode_Type = Gauge32
_CfprApPolicyControlledTypeFsmRmtErrCode_Object = MibTableColumn
cfprApPolicyControlledTypeFsmRmtErrCode = _CfprApPolicyControlledTypeFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10, 1, 9),
    _CfprApPolicyControlledTypeFsmRmtErrCode_Type()
)
cfprApPolicyControlledTypeFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmRmtErrCode.setStatus("current")
_CfprApPolicyControlledTypeFsmRmtErrDescr_Type = SnmpAdminString
_CfprApPolicyControlledTypeFsmRmtErrDescr_Object = MibTableColumn
cfprApPolicyControlledTypeFsmRmtErrDescr = _CfprApPolicyControlledTypeFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10, 1, 10),
    _CfprApPolicyControlledTypeFsmRmtErrDescr_Type()
)
cfprApPolicyControlledTypeFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmRmtErrDescr.setStatus("current")
_CfprApPolicyControlledTypeFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApPolicyControlledTypeFsmRmtRslt_Object = MibTableColumn
cfprApPolicyControlledTypeFsmRmtRslt = _CfprApPolicyControlledTypeFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 10, 1, 11),
    _CfprApPolicyControlledTypeFsmRmtRslt_Type()
)
cfprApPolicyControlledTypeFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmRmtRslt.setStatus("current")
_CfprApPolicyControlledTypeFsmStageTable_Object = MibTable
cfprApPolicyControlledTypeFsmStageTable = _CfprApPolicyControlledTypeFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 11)
)
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStageTable.setStatus("current")
_CfprApPolicyControlledTypeFsmStageEntry_Object = MibTableRow
cfprApPolicyControlledTypeFsmStageEntry = _CfprApPolicyControlledTypeFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 11, 1)
)
cfprApPolicyControlledTypeFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyControlledTypeFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStageEntry.setStatus("current")
_CfprApPolicyControlledTypeFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyControlledTypeFsmStageInstanceId_Object = MibTableColumn
cfprApPolicyControlledTypeFsmStageInstanceId = _CfprApPolicyControlledTypeFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 11, 1, 1),
    _CfprApPolicyControlledTypeFsmStageInstanceId_Type()
)
cfprApPolicyControlledTypeFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStageInstanceId.setStatus("current")
_CfprApPolicyControlledTypeFsmStageDn_Type = CfprApManagedObjectDn
_CfprApPolicyControlledTypeFsmStageDn_Object = MibTableColumn
cfprApPolicyControlledTypeFsmStageDn = _CfprApPolicyControlledTypeFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 11, 1, 2),
    _CfprApPolicyControlledTypeFsmStageDn_Type()
)
cfprApPolicyControlledTypeFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStageDn.setStatus("current")
_CfprApPolicyControlledTypeFsmStageRn_Type = SnmpAdminString
_CfprApPolicyControlledTypeFsmStageRn_Object = MibTableColumn
cfprApPolicyControlledTypeFsmStageRn = _CfprApPolicyControlledTypeFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 11, 1, 3),
    _CfprApPolicyControlledTypeFsmStageRn_Type()
)
cfprApPolicyControlledTypeFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStageRn.setStatus("current")
_CfprApPolicyControlledTypeFsmStageDescrData_Type = SnmpAdminString
_CfprApPolicyControlledTypeFsmStageDescrData_Object = MibTableColumn
cfprApPolicyControlledTypeFsmStageDescrData = _CfprApPolicyControlledTypeFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 11, 1, 4),
    _CfprApPolicyControlledTypeFsmStageDescrData_Type()
)
cfprApPolicyControlledTypeFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStageDescrData.setStatus("current")
_CfprApPolicyControlledTypeFsmStageLastUpdateTime_Type = DateAndTime
_CfprApPolicyControlledTypeFsmStageLastUpdateTime_Object = MibTableColumn
cfprApPolicyControlledTypeFsmStageLastUpdateTime = _CfprApPolicyControlledTypeFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 11, 1, 5),
    _CfprApPolicyControlledTypeFsmStageLastUpdateTime_Type()
)
cfprApPolicyControlledTypeFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStageLastUpdateTime.setStatus("current")
_CfprApPolicyControlledTypeFsmStageName_Type = CfprApPolicyControlledTypeFsmStageName
_CfprApPolicyControlledTypeFsmStageName_Object = MibTableColumn
cfprApPolicyControlledTypeFsmStageName = _CfprApPolicyControlledTypeFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 11, 1, 6),
    _CfprApPolicyControlledTypeFsmStageName_Type()
)
cfprApPolicyControlledTypeFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStageName.setStatus("current")
_CfprApPolicyControlledTypeFsmStageOrder_Type = Gauge32
_CfprApPolicyControlledTypeFsmStageOrder_Object = MibTableColumn
cfprApPolicyControlledTypeFsmStageOrder = _CfprApPolicyControlledTypeFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 11, 1, 7),
    _CfprApPolicyControlledTypeFsmStageOrder_Type()
)
cfprApPolicyControlledTypeFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStageOrder.setStatus("current")
_CfprApPolicyControlledTypeFsmStageRetry_Type = Gauge32
_CfprApPolicyControlledTypeFsmStageRetry_Object = MibTableColumn
cfprApPolicyControlledTypeFsmStageRetry = _CfprApPolicyControlledTypeFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 11, 1, 8),
    _CfprApPolicyControlledTypeFsmStageRetry_Type()
)
cfprApPolicyControlledTypeFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStageRetry.setStatus("current")
_CfprApPolicyControlledTypeFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApPolicyControlledTypeFsmStageStageStatus_Object = MibTableColumn
cfprApPolicyControlledTypeFsmStageStageStatus = _CfprApPolicyControlledTypeFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 11, 1, 9),
    _CfprApPolicyControlledTypeFsmStageStageStatus_Type()
)
cfprApPolicyControlledTypeFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmStageStageStatus.setStatus("current")
_CfprApPolicyControlledTypeFsmTaskTable_Object = MibTable
cfprApPolicyControlledTypeFsmTaskTable = _CfprApPolicyControlledTypeFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 12)
)
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmTaskTable.setStatus("current")
_CfprApPolicyControlledTypeFsmTaskEntry_Object = MibTableRow
cfprApPolicyControlledTypeFsmTaskEntry = _CfprApPolicyControlledTypeFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 12, 1)
)
cfprApPolicyControlledTypeFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyControlledTypeFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmTaskEntry.setStatus("current")
_CfprApPolicyControlledTypeFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyControlledTypeFsmTaskInstanceId_Object = MibTableColumn
cfprApPolicyControlledTypeFsmTaskInstanceId = _CfprApPolicyControlledTypeFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 12, 1, 1),
    _CfprApPolicyControlledTypeFsmTaskInstanceId_Type()
)
cfprApPolicyControlledTypeFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmTaskInstanceId.setStatus("current")
_CfprApPolicyControlledTypeFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApPolicyControlledTypeFsmTaskDn_Object = MibTableColumn
cfprApPolicyControlledTypeFsmTaskDn = _CfprApPolicyControlledTypeFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 12, 1, 2),
    _CfprApPolicyControlledTypeFsmTaskDn_Type()
)
cfprApPolicyControlledTypeFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmTaskDn.setStatus("current")
_CfprApPolicyControlledTypeFsmTaskRn_Type = SnmpAdminString
_CfprApPolicyControlledTypeFsmTaskRn_Object = MibTableColumn
cfprApPolicyControlledTypeFsmTaskRn = _CfprApPolicyControlledTypeFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 12, 1, 3),
    _CfprApPolicyControlledTypeFsmTaskRn_Type()
)
cfprApPolicyControlledTypeFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmTaskRn.setStatus("current")
_CfprApPolicyControlledTypeFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApPolicyControlledTypeFsmTaskCompletion_Object = MibTableColumn
cfprApPolicyControlledTypeFsmTaskCompletion = _CfprApPolicyControlledTypeFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 12, 1, 4),
    _CfprApPolicyControlledTypeFsmTaskCompletion_Type()
)
cfprApPolicyControlledTypeFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmTaskCompletion.setStatus("current")
_CfprApPolicyControlledTypeFsmTaskFlags_Type = CfprApFsmFlags
_CfprApPolicyControlledTypeFsmTaskFlags_Object = MibTableColumn
cfprApPolicyControlledTypeFsmTaskFlags = _CfprApPolicyControlledTypeFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 12, 1, 5),
    _CfprApPolicyControlledTypeFsmTaskFlags_Type()
)
cfprApPolicyControlledTypeFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmTaskFlags.setStatus("current")
_CfprApPolicyControlledTypeFsmTaskItem_Type = CfprApPolicyControlledTypeFsmTaskItem
_CfprApPolicyControlledTypeFsmTaskItem_Object = MibTableColumn
cfprApPolicyControlledTypeFsmTaskItem = _CfprApPolicyControlledTypeFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 12, 1, 6),
    _CfprApPolicyControlledTypeFsmTaskItem_Type()
)
cfprApPolicyControlledTypeFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmTaskItem.setStatus("current")
_CfprApPolicyControlledTypeFsmTaskSeqId_Type = Gauge32
_CfprApPolicyControlledTypeFsmTaskSeqId_Object = MibTableColumn
cfprApPolicyControlledTypeFsmTaskSeqId = _CfprApPolicyControlledTypeFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 12, 1, 7),
    _CfprApPolicyControlledTypeFsmTaskSeqId_Type()
)
cfprApPolicyControlledTypeFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyControlledTypeFsmTaskSeqId.setStatus("current")
_CfprApPolicyDateTimeTable_Object = MibTable
cfprApPolicyDateTimeTable = _CfprApPolicyDateTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 13)
)
if mibBuilder.loadTexts:
    cfprApPolicyDateTimeTable.setStatus("current")
_CfprApPolicyDateTimeEntry_Object = MibTableRow
cfprApPolicyDateTimeEntry = _CfprApPolicyDateTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 13, 1)
)
cfprApPolicyDateTimeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyDateTimeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyDateTimeEntry.setStatus("current")
_CfprApPolicyDateTimeInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyDateTimeInstanceId_Object = MibTableColumn
cfprApPolicyDateTimeInstanceId = _CfprApPolicyDateTimeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 13, 1, 1),
    _CfprApPolicyDateTimeInstanceId_Type()
)
cfprApPolicyDateTimeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyDateTimeInstanceId.setStatus("current")
_CfprApPolicyDateTimeDn_Type = CfprApManagedObjectDn
_CfprApPolicyDateTimeDn_Object = MibTableColumn
cfprApPolicyDateTimeDn = _CfprApPolicyDateTimeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 13, 1, 2),
    _CfprApPolicyDateTimeDn_Type()
)
cfprApPolicyDateTimeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDateTimeDn.setStatus("current")
_CfprApPolicyDateTimeRn_Type = SnmpAdminString
_CfprApPolicyDateTimeRn_Object = MibTableColumn
cfprApPolicyDateTimeRn = _CfprApPolicyDateTimeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 13, 1, 3),
    _CfprApPolicyDateTimeRn_Type()
)
cfprApPolicyDateTimeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDateTimeRn.setStatus("current")
_CfprApPolicyDateTimeSource_Type = CfprApPolicyControlSource
_CfprApPolicyDateTimeSource_Object = MibTableColumn
cfprApPolicyDateTimeSource = _CfprApPolicyDateTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 13, 1, 4),
    _CfprApPolicyDateTimeSource_Type()
)
cfprApPolicyDateTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDateTimeSource.setStatus("current")
_CfprApPolicyDigestTable_Object = MibTable
cfprApPolicyDigestTable = _CfprApPolicyDigestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14)
)
if mibBuilder.loadTexts:
    cfprApPolicyDigestTable.setStatus("current")
_CfprApPolicyDigestEntry_Object = MibTableRow
cfprApPolicyDigestEntry = _CfprApPolicyDigestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1)
)
cfprApPolicyDigestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyDigestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyDigestEntry.setStatus("current")
_CfprApPolicyDigestInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyDigestInstanceId_Object = MibTableColumn
cfprApPolicyDigestInstanceId = _CfprApPolicyDigestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 1),
    _CfprApPolicyDigestInstanceId_Type()
)
cfprApPolicyDigestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyDigestInstanceId.setStatus("current")
_CfprApPolicyDigestDn_Type = CfprApManagedObjectDn
_CfprApPolicyDigestDn_Object = MibTableColumn
cfprApPolicyDigestDn = _CfprApPolicyDigestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 2),
    _CfprApPolicyDigestDn_Type()
)
cfprApPolicyDigestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDigestDn.setStatus("current")
_CfprApPolicyDigestRn_Type = SnmpAdminString
_CfprApPolicyDigestRn_Object = MibTableColumn
cfprApPolicyDigestRn = _CfprApPolicyDigestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 3),
    _CfprApPolicyDigestRn_Type()
)
cfprApPolicyDigestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDigestRn.setStatus("current")
_CfprApPolicyDigestContext_Type = SnmpAdminString
_CfprApPolicyDigestContext_Object = MibTableColumn
cfprApPolicyDigestContext = _CfprApPolicyDigestContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 4),
    _CfprApPolicyDigestContext_Type()
)
cfprApPolicyDigestContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDigestContext.setStatus("current")
_CfprApPolicyDigestDescr_Type = SnmpAdminString
_CfprApPolicyDigestDescr_Object = MibTableColumn
cfprApPolicyDigestDescr = _CfprApPolicyDigestDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 5),
    _CfprApPolicyDigestDescr_Type()
)
cfprApPolicyDigestDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDigestDescr.setStatus("current")
_CfprApPolicyDigestLabel_Type = SnmpAdminString
_CfprApPolicyDigestLabel_Object = MibTableColumn
cfprApPolicyDigestLabel = _CfprApPolicyDigestLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 6),
    _CfprApPolicyDigestLabel_Type()
)
cfprApPolicyDigestLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDigestLabel.setStatus("current")
_CfprApPolicyDigestName_Type = SnmpAdminString
_CfprApPolicyDigestName_Object = MibTableColumn
cfprApPolicyDigestName = _CfprApPolicyDigestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 7),
    _CfprApPolicyDigestName_Type()
)
cfprApPolicyDigestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDigestName.setStatus("current")
_CfprApPolicyDigestOnBehalfOfIdent_Type = SnmpAdminString
_CfprApPolicyDigestOnBehalfOfIdent_Object = MibTableColumn
cfprApPolicyDigestOnBehalfOfIdent = _CfprApPolicyDigestOnBehalfOfIdent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 8),
    _CfprApPolicyDigestOnBehalfOfIdent_Type()
)
cfprApPolicyDigestOnBehalfOfIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDigestOnBehalfOfIdent.setStatus("current")
_CfprApPolicyDigestOnBehalfOfType_Type = SnmpAdminString
_CfprApPolicyDigestOnBehalfOfType_Object = MibTableColumn
cfprApPolicyDigestOnBehalfOfType = _CfprApPolicyDigestOnBehalfOfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 9),
    _CfprApPolicyDigestOnBehalfOfType_Type()
)
cfprApPolicyDigestOnBehalfOfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDigestOnBehalfOfType.setStatus("current")
_CfprApPolicyDigestRequestorOwnership_Type = CfprApPolicyPolicyOwner
_CfprApPolicyDigestRequestorOwnership_Object = MibTableColumn
cfprApPolicyDigestRequestorOwnership = _CfprApPolicyDigestRequestorOwnership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 10),
    _CfprApPolicyDigestRequestorOwnership_Type()
)
cfprApPolicyDigestRequestorOwnership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDigestRequestorOwnership.setStatus("current")
_CfprApPolicyDigestResolveType_Type = CfprApPolicyPolicyResolveType
_CfprApPolicyDigestResolveType_Object = MibTableColumn
cfprApPolicyDigestResolveType = _CfprApPolicyDigestResolveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 11),
    _CfprApPolicyDigestResolveType_Type()
)
cfprApPolicyDigestResolveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDigestResolveType.setStatus("current")
_CfprApPolicyDigestType_Type = SnmpAdminString
_CfprApPolicyDigestType_Object = MibTableColumn
cfprApPolicyDigestType = _CfprApPolicyDigestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 12),
    _CfprApPolicyDigestType_Type()
)
cfprApPolicyDigestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDigestType.setStatus("current")
_CfprApPolicyDigestUsage_Type = SnmpAdminString
_CfprApPolicyDigestUsage_Object = MibTableColumn
cfprApPolicyDigestUsage = _CfprApPolicyDigestUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 14, 1, 13),
    _CfprApPolicyDigestUsage_Type()
)
cfprApPolicyDigestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDigestUsage.setStatus("current")
_CfprApPolicyDiscoveryTable_Object = MibTable
cfprApPolicyDiscoveryTable = _CfprApPolicyDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 15)
)
if mibBuilder.loadTexts:
    cfprApPolicyDiscoveryTable.setStatus("current")
_CfprApPolicyDiscoveryEntry_Object = MibTableRow
cfprApPolicyDiscoveryEntry = _CfprApPolicyDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 15, 1)
)
cfprApPolicyDiscoveryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyDiscoveryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyDiscoveryEntry.setStatus("current")
_CfprApPolicyDiscoveryInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyDiscoveryInstanceId_Object = MibTableColumn
cfprApPolicyDiscoveryInstanceId = _CfprApPolicyDiscoveryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 15, 1, 1),
    _CfprApPolicyDiscoveryInstanceId_Type()
)
cfprApPolicyDiscoveryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyDiscoveryInstanceId.setStatus("current")
_CfprApPolicyDiscoveryDn_Type = CfprApManagedObjectDn
_CfprApPolicyDiscoveryDn_Object = MibTableColumn
cfprApPolicyDiscoveryDn = _CfprApPolicyDiscoveryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 15, 1, 2),
    _CfprApPolicyDiscoveryDn_Type()
)
cfprApPolicyDiscoveryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDiscoveryDn.setStatus("current")
_CfprApPolicyDiscoveryRn_Type = SnmpAdminString
_CfprApPolicyDiscoveryRn_Object = MibTableColumn
cfprApPolicyDiscoveryRn = _CfprApPolicyDiscoveryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 15, 1, 3),
    _CfprApPolicyDiscoveryRn_Type()
)
cfprApPolicyDiscoveryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDiscoveryRn.setStatus("current")
_CfprApPolicyDiscoverySource_Type = CfprApPolicyControlSource
_CfprApPolicyDiscoverySource_Object = MibTableColumn
cfprApPolicyDiscoverySource = _CfprApPolicyDiscoverySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 15, 1, 4),
    _CfprApPolicyDiscoverySource_Type()
)
cfprApPolicyDiscoverySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDiscoverySource.setStatus("current")
_CfprApPolicyDnsTable_Object = MibTable
cfprApPolicyDnsTable = _CfprApPolicyDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 16)
)
if mibBuilder.loadTexts:
    cfprApPolicyDnsTable.setStatus("current")
_CfprApPolicyDnsEntry_Object = MibTableRow
cfprApPolicyDnsEntry = _CfprApPolicyDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 16, 1)
)
cfprApPolicyDnsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyDnsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyDnsEntry.setStatus("current")
_CfprApPolicyDnsInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyDnsInstanceId_Object = MibTableColumn
cfprApPolicyDnsInstanceId = _CfprApPolicyDnsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 16, 1, 1),
    _CfprApPolicyDnsInstanceId_Type()
)
cfprApPolicyDnsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyDnsInstanceId.setStatus("current")
_CfprApPolicyDnsDn_Type = CfprApManagedObjectDn
_CfprApPolicyDnsDn_Object = MibTableColumn
cfprApPolicyDnsDn = _CfprApPolicyDnsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 16, 1, 2),
    _CfprApPolicyDnsDn_Type()
)
cfprApPolicyDnsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDnsDn.setStatus("current")
_CfprApPolicyDnsRn_Type = SnmpAdminString
_CfprApPolicyDnsRn_Object = MibTableColumn
cfprApPolicyDnsRn = _CfprApPolicyDnsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 16, 1, 3),
    _CfprApPolicyDnsRn_Type()
)
cfprApPolicyDnsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDnsRn.setStatus("current")
_CfprApPolicyDnsSource_Type = CfprApPolicyControlSource
_CfprApPolicyDnsSource_Object = MibTableColumn
cfprApPolicyDnsSource = _CfprApPolicyDnsSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 16, 1, 4),
    _CfprApPolicyDnsSource_Type()
)
cfprApPolicyDnsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyDnsSource.setStatus("current")
_CfprApPolicyElementTable_Object = MibTable
cfprApPolicyElementTable = _CfprApPolicyElementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 17)
)
if mibBuilder.loadTexts:
    cfprApPolicyElementTable.setStatus("current")
_CfprApPolicyElementEntry_Object = MibTableRow
cfprApPolicyElementEntry = _CfprApPolicyElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 17, 1)
)
cfprApPolicyElementEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyElementInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyElementEntry.setStatus("current")
_CfprApPolicyElementInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyElementInstanceId_Object = MibTableColumn
cfprApPolicyElementInstanceId = _CfprApPolicyElementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 17, 1, 1),
    _CfprApPolicyElementInstanceId_Type()
)
cfprApPolicyElementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyElementInstanceId.setStatus("current")
_CfprApPolicyElementDn_Type = CfprApManagedObjectDn
_CfprApPolicyElementDn_Object = MibTableColumn
cfprApPolicyElementDn = _CfprApPolicyElementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 17, 1, 2),
    _CfprApPolicyElementDn_Type()
)
cfprApPolicyElementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyElementDn.setStatus("current")
_CfprApPolicyElementRn_Type = SnmpAdminString
_CfprApPolicyElementRn_Object = MibTableColumn
cfprApPolicyElementRn = _CfprApPolicyElementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 17, 1, 3),
    _CfprApPolicyElementRn_Type()
)
cfprApPolicyElementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyElementRn.setStatus("current")
_CfprApPolicyElementClassType_Type = SnmpAdminString
_CfprApPolicyElementClassType_Object = MibTableColumn
cfprApPolicyElementClassType = _CfprApPolicyElementClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 17, 1, 4),
    _CfprApPolicyElementClassType_Type()
)
cfprApPolicyElementClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyElementClassType.setStatus("current")
_CfprApPolicyElementConvertedDn_Type = SnmpAdminString
_CfprApPolicyElementConvertedDn_Object = MibTableColumn
cfprApPolicyElementConvertedDn = _CfprApPolicyElementConvertedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 17, 1, 5),
    _CfprApPolicyElementConvertedDn_Type()
)
cfprApPolicyElementConvertedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyElementConvertedDn.setStatus("current")
_CfprApPolicyElementOwnership_Type = CfprApPolicyPolicyOwner
_CfprApPolicyElementOwnership_Object = MibTableColumn
cfprApPolicyElementOwnership = _CfprApPolicyElementOwnership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 17, 1, 6),
    _CfprApPolicyElementOwnership_Type()
)
cfprApPolicyElementOwnership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyElementOwnership.setStatus("current")
_CfprApPolicyElementPolicyDn_Type = SnmpAdminString
_CfprApPolicyElementPolicyDn_Object = MibTableColumn
cfprApPolicyElementPolicyDn = _CfprApPolicyElementPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 17, 1, 7),
    _CfprApPolicyElementPolicyDn_Type()
)
cfprApPolicyElementPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyElementPolicyDn.setStatus("current")
_CfprApPolicyFaultTable_Object = MibTable
cfprApPolicyFaultTable = _CfprApPolicyFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 18)
)
if mibBuilder.loadTexts:
    cfprApPolicyFaultTable.setStatus("current")
_CfprApPolicyFaultEntry_Object = MibTableRow
cfprApPolicyFaultEntry = _CfprApPolicyFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 18, 1)
)
cfprApPolicyFaultEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyFaultInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyFaultEntry.setStatus("current")
_CfprApPolicyFaultInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyFaultInstanceId_Object = MibTableColumn
cfprApPolicyFaultInstanceId = _CfprApPolicyFaultInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 18, 1, 1),
    _CfprApPolicyFaultInstanceId_Type()
)
cfprApPolicyFaultInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyFaultInstanceId.setStatus("current")
_CfprApPolicyFaultDn_Type = CfprApManagedObjectDn
_CfprApPolicyFaultDn_Object = MibTableColumn
cfprApPolicyFaultDn = _CfprApPolicyFaultDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 18, 1, 2),
    _CfprApPolicyFaultDn_Type()
)
cfprApPolicyFaultDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyFaultDn.setStatus("current")
_CfprApPolicyFaultRn_Type = SnmpAdminString
_CfprApPolicyFaultRn_Object = MibTableColumn
cfprApPolicyFaultRn = _CfprApPolicyFaultRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 18, 1, 3),
    _CfprApPolicyFaultRn_Type()
)
cfprApPolicyFaultRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyFaultRn.setStatus("current")
_CfprApPolicyFaultSource_Type = CfprApPolicyControlSource
_CfprApPolicyFaultSource_Object = MibTableColumn
cfprApPolicyFaultSource = _CfprApPolicyFaultSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 18, 1, 4),
    _CfprApPolicyFaultSource_Type()
)
cfprApPolicyFaultSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyFaultSource.setStatus("current")
_CfprApPolicyIdResolvePolicyTable_Object = MibTable
cfprApPolicyIdResolvePolicyTable = _CfprApPolicyIdResolvePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 19)
)
if mibBuilder.loadTexts:
    cfprApPolicyIdResolvePolicyTable.setStatus("current")
_CfprApPolicyIdResolvePolicyEntry_Object = MibTableRow
cfprApPolicyIdResolvePolicyEntry = _CfprApPolicyIdResolvePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 19, 1)
)
cfprApPolicyIdResolvePolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyIdResolvePolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyIdResolvePolicyEntry.setStatus("current")
_CfprApPolicyIdResolvePolicyInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyIdResolvePolicyInstanceId_Object = MibTableColumn
cfprApPolicyIdResolvePolicyInstanceId = _CfprApPolicyIdResolvePolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 19, 1, 1),
    _CfprApPolicyIdResolvePolicyInstanceId_Type()
)
cfprApPolicyIdResolvePolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyIdResolvePolicyInstanceId.setStatus("current")
_CfprApPolicyIdResolvePolicyDn_Type = CfprApManagedObjectDn
_CfprApPolicyIdResolvePolicyDn_Object = MibTableColumn
cfprApPolicyIdResolvePolicyDn = _CfprApPolicyIdResolvePolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 19, 1, 2),
    _CfprApPolicyIdResolvePolicyDn_Type()
)
cfprApPolicyIdResolvePolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyIdResolvePolicyDn.setStatus("current")
_CfprApPolicyIdResolvePolicyRn_Type = SnmpAdminString
_CfprApPolicyIdResolvePolicyRn_Object = MibTableColumn
cfprApPolicyIdResolvePolicyRn = _CfprApPolicyIdResolvePolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 19, 1, 3),
    _CfprApPolicyIdResolvePolicyRn_Type()
)
cfprApPolicyIdResolvePolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyIdResolvePolicyRn.setStatus("current")
_CfprApPolicyIdResolvePolicyIdAssignmentMode_Type = CfprApPolicyIdResolvePolicyType
_CfprApPolicyIdResolvePolicyIdAssignmentMode_Object = MibTableColumn
cfprApPolicyIdResolvePolicyIdAssignmentMode = _CfprApPolicyIdResolvePolicyIdAssignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 19, 1, 4),
    _CfprApPolicyIdResolvePolicyIdAssignmentMode_Type()
)
cfprApPolicyIdResolvePolicyIdAssignmentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyIdResolvePolicyIdAssignmentMode.setStatus("current")
_CfprApPolicyInfraFirmwareTable_Object = MibTable
cfprApPolicyInfraFirmwareTable = _CfprApPolicyInfraFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 20)
)
if mibBuilder.loadTexts:
    cfprApPolicyInfraFirmwareTable.setStatus("current")
_CfprApPolicyInfraFirmwareEntry_Object = MibTableRow
cfprApPolicyInfraFirmwareEntry = _CfprApPolicyInfraFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 20, 1)
)
cfprApPolicyInfraFirmwareEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyInfraFirmwareInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyInfraFirmwareEntry.setStatus("current")
_CfprApPolicyInfraFirmwareInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyInfraFirmwareInstanceId_Object = MibTableColumn
cfprApPolicyInfraFirmwareInstanceId = _CfprApPolicyInfraFirmwareInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 20, 1, 1),
    _CfprApPolicyInfraFirmwareInstanceId_Type()
)
cfprApPolicyInfraFirmwareInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyInfraFirmwareInstanceId.setStatus("current")
_CfprApPolicyInfraFirmwareDn_Type = CfprApManagedObjectDn
_CfprApPolicyInfraFirmwareDn_Object = MibTableColumn
cfprApPolicyInfraFirmwareDn = _CfprApPolicyInfraFirmwareDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 20, 1, 2),
    _CfprApPolicyInfraFirmwareDn_Type()
)
cfprApPolicyInfraFirmwareDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyInfraFirmwareDn.setStatus("current")
_CfprApPolicyInfraFirmwareRn_Type = SnmpAdminString
_CfprApPolicyInfraFirmwareRn_Object = MibTableColumn
cfprApPolicyInfraFirmwareRn = _CfprApPolicyInfraFirmwareRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 20, 1, 3),
    _CfprApPolicyInfraFirmwareRn_Type()
)
cfprApPolicyInfraFirmwareRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyInfraFirmwareRn.setStatus("current")
_CfprApPolicyInfraFirmwareSource_Type = CfprApPolicyControlSource
_CfprApPolicyInfraFirmwareSource_Object = MibTableColumn
cfprApPolicyInfraFirmwareSource = _CfprApPolicyInfraFirmwareSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 20, 1, 4),
    _CfprApPolicyInfraFirmwareSource_Type()
)
cfprApPolicyInfraFirmwareSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyInfraFirmwareSource.setStatus("current")
_CfprApPolicyLocalMapTable_Object = MibTable
cfprApPolicyLocalMapTable = _CfprApPolicyLocalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 21)
)
if mibBuilder.loadTexts:
    cfprApPolicyLocalMapTable.setStatus("current")
_CfprApPolicyLocalMapEntry_Object = MibTableRow
cfprApPolicyLocalMapEntry = _CfprApPolicyLocalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 21, 1)
)
cfprApPolicyLocalMapEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyLocalMapInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyLocalMapEntry.setStatus("current")
_CfprApPolicyLocalMapInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyLocalMapInstanceId_Object = MibTableColumn
cfprApPolicyLocalMapInstanceId = _CfprApPolicyLocalMapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 21, 1, 1),
    _CfprApPolicyLocalMapInstanceId_Type()
)
cfprApPolicyLocalMapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyLocalMapInstanceId.setStatus("current")
_CfprApPolicyLocalMapDn_Type = CfprApManagedObjectDn
_CfprApPolicyLocalMapDn_Object = MibTableColumn
cfprApPolicyLocalMapDn = _CfprApPolicyLocalMapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 21, 1, 2),
    _CfprApPolicyLocalMapDn_Type()
)
cfprApPolicyLocalMapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyLocalMapDn.setStatus("current")
_CfprApPolicyLocalMapRn_Type = SnmpAdminString
_CfprApPolicyLocalMapRn_Object = MibTableColumn
cfprApPolicyLocalMapRn = _CfprApPolicyLocalMapRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 21, 1, 3),
    _CfprApPolicyLocalMapRn_Type()
)
cfprApPolicyLocalMapRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyLocalMapRn.setStatus("current")
_CfprApPolicyMEpTable_Object = MibTable
cfprApPolicyMEpTable = _CfprApPolicyMEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 22)
)
if mibBuilder.loadTexts:
    cfprApPolicyMEpTable.setStatus("current")
_CfprApPolicyMEpEntry_Object = MibTableRow
cfprApPolicyMEpEntry = _CfprApPolicyMEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 22, 1)
)
cfprApPolicyMEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyMEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyMEpEntry.setStatus("current")
_CfprApPolicyMEpInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyMEpInstanceId_Object = MibTableColumn
cfprApPolicyMEpInstanceId = _CfprApPolicyMEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 22, 1, 1),
    _CfprApPolicyMEpInstanceId_Type()
)
cfprApPolicyMEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyMEpInstanceId.setStatus("current")
_CfprApPolicyMEpDn_Type = CfprApManagedObjectDn
_CfprApPolicyMEpDn_Object = MibTableColumn
cfprApPolicyMEpDn = _CfprApPolicyMEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 22, 1, 2),
    _CfprApPolicyMEpDn_Type()
)
cfprApPolicyMEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyMEpDn.setStatus("current")
_CfprApPolicyMEpRn_Type = SnmpAdminString
_CfprApPolicyMEpRn_Object = MibTableColumn
cfprApPolicyMEpRn = _CfprApPolicyMEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 22, 1, 3),
    _CfprApPolicyMEpRn_Type()
)
cfprApPolicyMEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyMEpRn.setStatus("current")
_CfprApPolicyMEpSource_Type = CfprApPolicyControlSource
_CfprApPolicyMEpSource_Object = MibTableColumn
cfprApPolicyMEpSource = _CfprApPolicyMEpSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 22, 1, 4),
    _CfprApPolicyMEpSource_Type()
)
cfprApPolicyMEpSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyMEpSource.setStatus("current")
_CfprApPolicyMonitoringTable_Object = MibTable
cfprApPolicyMonitoringTable = _CfprApPolicyMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 23)
)
if mibBuilder.loadTexts:
    cfprApPolicyMonitoringTable.setStatus("current")
_CfprApPolicyMonitoringEntry_Object = MibTableRow
cfprApPolicyMonitoringEntry = _CfprApPolicyMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 23, 1)
)
cfprApPolicyMonitoringEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyMonitoringInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyMonitoringEntry.setStatus("current")
_CfprApPolicyMonitoringInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyMonitoringInstanceId_Object = MibTableColumn
cfprApPolicyMonitoringInstanceId = _CfprApPolicyMonitoringInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 23, 1, 1),
    _CfprApPolicyMonitoringInstanceId_Type()
)
cfprApPolicyMonitoringInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyMonitoringInstanceId.setStatus("current")
_CfprApPolicyMonitoringDn_Type = CfprApManagedObjectDn
_CfprApPolicyMonitoringDn_Object = MibTableColumn
cfprApPolicyMonitoringDn = _CfprApPolicyMonitoringDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 23, 1, 2),
    _CfprApPolicyMonitoringDn_Type()
)
cfprApPolicyMonitoringDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyMonitoringDn.setStatus("current")
_CfprApPolicyMonitoringRn_Type = SnmpAdminString
_CfprApPolicyMonitoringRn_Object = MibTableColumn
cfprApPolicyMonitoringRn = _CfprApPolicyMonitoringRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 23, 1, 3),
    _CfprApPolicyMonitoringRn_Type()
)
cfprApPolicyMonitoringRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyMonitoringRn.setStatus("current")
_CfprApPolicyMonitoringSource_Type = CfprApPolicyControlSource
_CfprApPolicyMonitoringSource_Object = MibTableColumn
cfprApPolicyMonitoringSource = _CfprApPolicyMonitoringSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 23, 1, 4),
    _CfprApPolicyMonitoringSource_Type()
)
cfprApPolicyMonitoringSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyMonitoringSource.setStatus("current")
_CfprApPolicyPolicyEpTable_Object = MibTable
cfprApPolicyPolicyEpTable = _CfprApPolicyPolicyEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 24)
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyEpTable.setStatus("current")
_CfprApPolicyPolicyEpEntry_Object = MibTableRow
cfprApPolicyPolicyEpEntry = _CfprApPolicyPolicyEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 24, 1)
)
cfprApPolicyPolicyEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyPolicyEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyEpEntry.setStatus("current")
_CfprApPolicyPolicyEpInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyPolicyEpInstanceId_Object = MibTableColumn
cfprApPolicyPolicyEpInstanceId = _CfprApPolicyPolicyEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 24, 1, 1),
    _CfprApPolicyPolicyEpInstanceId_Type()
)
cfprApPolicyPolicyEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyEpInstanceId.setStatus("current")
_CfprApPolicyPolicyEpDn_Type = CfprApManagedObjectDn
_CfprApPolicyPolicyEpDn_Object = MibTableColumn
cfprApPolicyPolicyEpDn = _CfprApPolicyPolicyEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 24, 1, 2),
    _CfprApPolicyPolicyEpDn_Type()
)
cfprApPolicyPolicyEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyEpDn.setStatus("current")
_CfprApPolicyPolicyEpRn_Type = SnmpAdminString
_CfprApPolicyPolicyEpRn_Object = MibTableColumn
cfprApPolicyPolicyEpRn = _CfprApPolicyPolicyEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 24, 1, 3),
    _CfprApPolicyPolicyEpRn_Type()
)
cfprApPolicyPolicyEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyEpRn.setStatus("current")
_CfprApPolicyPolicyRequestorTable_Object = MibTable
cfprApPolicyPolicyRequestorTable = _CfprApPolicyPolicyRequestorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 25)
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyRequestorTable.setStatus("current")
_CfprApPolicyPolicyRequestorEntry_Object = MibTableRow
cfprApPolicyPolicyRequestorEntry = _CfprApPolicyPolicyRequestorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 25, 1)
)
cfprApPolicyPolicyRequestorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyPolicyRequestorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyRequestorEntry.setStatus("current")
_CfprApPolicyPolicyRequestorInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyPolicyRequestorInstanceId_Object = MibTableColumn
cfprApPolicyPolicyRequestorInstanceId = _CfprApPolicyPolicyRequestorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 25, 1, 1),
    _CfprApPolicyPolicyRequestorInstanceId_Type()
)
cfprApPolicyPolicyRequestorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyRequestorInstanceId.setStatus("current")
_CfprApPolicyPolicyRequestorDn_Type = CfprApManagedObjectDn
_CfprApPolicyPolicyRequestorDn_Object = MibTableColumn
cfprApPolicyPolicyRequestorDn = _CfprApPolicyPolicyRequestorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 25, 1, 2),
    _CfprApPolicyPolicyRequestorDn_Type()
)
cfprApPolicyPolicyRequestorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyRequestorDn.setStatus("current")
_CfprApPolicyPolicyRequestorRn_Type = SnmpAdminString
_CfprApPolicyPolicyRequestorRn_Object = MibTableColumn
cfprApPolicyPolicyRequestorRn = _CfprApPolicyPolicyRequestorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 25, 1, 3),
    _CfprApPolicyPolicyRequestorRn_Type()
)
cfprApPolicyPolicyRequestorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyRequestorRn.setStatus("current")
_CfprApPolicyPolicyRequestorName_Type = SnmpAdminString
_CfprApPolicyPolicyRequestorName_Object = MibTableColumn
cfprApPolicyPolicyRequestorName = _CfprApPolicyPolicyRequestorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 25, 1, 4),
    _CfprApPolicyPolicyRequestorName_Type()
)
cfprApPolicyPolicyRequestorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyRequestorName.setStatus("current")
_CfprApPolicyPolicyRequestorOnBehalfOfIdent_Type = SnmpAdminString
_CfprApPolicyPolicyRequestorOnBehalfOfIdent_Object = MibTableColumn
cfprApPolicyPolicyRequestorOnBehalfOfIdent = _CfprApPolicyPolicyRequestorOnBehalfOfIdent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 25, 1, 5),
    _CfprApPolicyPolicyRequestorOnBehalfOfIdent_Type()
)
cfprApPolicyPolicyRequestorOnBehalfOfIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyRequestorOnBehalfOfIdent.setStatus("current")
_CfprApPolicyPolicyRequestorOnBehalfOfType_Type = SnmpAdminString
_CfprApPolicyPolicyRequestorOnBehalfOfType_Object = MibTableColumn
cfprApPolicyPolicyRequestorOnBehalfOfType = _CfprApPolicyPolicyRequestorOnBehalfOfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 25, 1, 6),
    _CfprApPolicyPolicyRequestorOnBehalfOfType_Type()
)
cfprApPolicyPolicyRequestorOnBehalfOfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyRequestorOnBehalfOfType.setStatus("current")
_CfprApPolicyPolicyRequestorResolvedClassType_Type = SnmpAdminString
_CfprApPolicyPolicyRequestorResolvedClassType_Object = MibTableColumn
cfprApPolicyPolicyRequestorResolvedClassType = _CfprApPolicyPolicyRequestorResolvedClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 25, 1, 7),
    _CfprApPolicyPolicyRequestorResolvedClassType_Type()
)
cfprApPolicyPolicyRequestorResolvedClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyRequestorResolvedClassType.setStatus("current")
_CfprApPolicyPolicyScopeTable_Object = MibTable
cfprApPolicyPolicyScopeTable = _CfprApPolicyPolicyScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26)
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeTable.setStatus("current")
_CfprApPolicyPolicyScopeEntry_Object = MibTableRow
cfprApPolicyPolicyScopeEntry = _CfprApPolicyPolicyScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1)
)
cfprApPolicyPolicyScopeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyPolicyScopeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeEntry.setStatus("current")
_CfprApPolicyPolicyScopeInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyPolicyScopeInstanceId_Object = MibTableColumn
cfprApPolicyPolicyScopeInstanceId = _CfprApPolicyPolicyScopeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 1),
    _CfprApPolicyPolicyScopeInstanceId_Type()
)
cfprApPolicyPolicyScopeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeInstanceId.setStatus("current")
_CfprApPolicyPolicyScopeDn_Type = CfprApManagedObjectDn
_CfprApPolicyPolicyScopeDn_Object = MibTableColumn
cfprApPolicyPolicyScopeDn = _CfprApPolicyPolicyScopeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 2),
    _CfprApPolicyPolicyScopeDn_Type()
)
cfprApPolicyPolicyScopeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeDn.setStatus("current")
_CfprApPolicyPolicyScopeRn_Type = SnmpAdminString
_CfprApPolicyPolicyScopeRn_Object = MibTableColumn
cfprApPolicyPolicyScopeRn = _CfprApPolicyPolicyScopeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 3),
    _CfprApPolicyPolicyScopeRn_Type()
)
cfprApPolicyPolicyScopeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeRn.setStatus("current")
_CfprApPolicyPolicyScopeAppType_Type = SnmpAdminString
_CfprApPolicyPolicyScopeAppType_Object = MibTableColumn
cfprApPolicyPolicyScopeAppType = _CfprApPolicyPolicyScopeAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 4),
    _CfprApPolicyPolicyScopeAppType_Type()
)
cfprApPolicyPolicyScopeAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeAppType.setStatus("current")
_CfprApPolicyPolicyScopeDefaultPolicyName_Type = SnmpAdminString
_CfprApPolicyPolicyScopeDefaultPolicyName_Object = MibTableColumn
cfprApPolicyPolicyScopeDefaultPolicyName = _CfprApPolicyPolicyScopeDefaultPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 5),
    _CfprApPolicyPolicyScopeDefaultPolicyName_Type()
)
cfprApPolicyPolicyScopeDefaultPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeDefaultPolicyName.setStatus("current")
_CfprApPolicyPolicyScopeFsmDescr_Type = SnmpAdminString
_CfprApPolicyPolicyScopeFsmDescr_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmDescr = _CfprApPolicyPolicyScopeFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 6),
    _CfprApPolicyPolicyScopeFsmDescr_Type()
)
cfprApPolicyPolicyScopeFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmDescr.setStatus("current")
_CfprApPolicyPolicyScopeFsmPrev_Type = SnmpAdminString
_CfprApPolicyPolicyScopeFsmPrev_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmPrev = _CfprApPolicyPolicyScopeFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 7),
    _CfprApPolicyPolicyScopeFsmPrev_Type()
)
cfprApPolicyPolicyScopeFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmPrev.setStatus("current")
_CfprApPolicyPolicyScopeFsmProgr_Type = Gauge32
_CfprApPolicyPolicyScopeFsmProgr_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmProgr = _CfprApPolicyPolicyScopeFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 8),
    _CfprApPolicyPolicyScopeFsmProgr_Type()
)
cfprApPolicyPolicyScopeFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmProgr.setStatus("current")
_CfprApPolicyPolicyScopeFsmRmtInvErrCode_Type = Gauge32
_CfprApPolicyPolicyScopeFsmRmtInvErrCode_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmRmtInvErrCode = _CfprApPolicyPolicyScopeFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 9),
    _CfprApPolicyPolicyScopeFsmRmtInvErrCode_Type()
)
cfprApPolicyPolicyScopeFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmRmtInvErrCode.setStatus("current")
_CfprApPolicyPolicyScopeFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApPolicyPolicyScopeFsmRmtInvErrDescr_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmRmtInvErrDescr = _CfprApPolicyPolicyScopeFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 10),
    _CfprApPolicyPolicyScopeFsmRmtInvErrDescr_Type()
)
cfprApPolicyPolicyScopeFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmRmtInvErrDescr.setStatus("current")
_CfprApPolicyPolicyScopeFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApPolicyPolicyScopeFsmRmtInvRslt_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmRmtInvRslt = _CfprApPolicyPolicyScopeFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 11),
    _CfprApPolicyPolicyScopeFsmRmtInvRslt_Type()
)
cfprApPolicyPolicyScopeFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmRmtInvRslt.setStatus("current")
_CfprApPolicyPolicyScopeFsmStageDescr_Type = SnmpAdminString
_CfprApPolicyPolicyScopeFsmStageDescr_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmStageDescr = _CfprApPolicyPolicyScopeFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 12),
    _CfprApPolicyPolicyScopeFsmStageDescr_Type()
)
cfprApPolicyPolicyScopeFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStageDescr.setStatus("current")
_CfprApPolicyPolicyScopeFsmStamp_Type = DateAndTime
_CfprApPolicyPolicyScopeFsmStamp_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmStamp = _CfprApPolicyPolicyScopeFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 13),
    _CfprApPolicyPolicyScopeFsmStamp_Type()
)
cfprApPolicyPolicyScopeFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStamp.setStatus("current")
_CfprApPolicyPolicyScopeFsmStatus_Type = SnmpAdminString
_CfprApPolicyPolicyScopeFsmStatus_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmStatus = _CfprApPolicyPolicyScopeFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 14),
    _CfprApPolicyPolicyScopeFsmStatus_Type()
)
cfprApPolicyPolicyScopeFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStatus.setStatus("current")
_CfprApPolicyPolicyScopeFsmTry_Type = Gauge32
_CfprApPolicyPolicyScopeFsmTry_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmTry = _CfprApPolicyPolicyScopeFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 15),
    _CfprApPolicyPolicyScopeFsmTry_Type()
)
cfprApPolicyPolicyScopeFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmTry.setStatus("current")
_CfprApPolicyPolicyScopeOperStatus_Type = CfprApPolicyPolicyOperStatus
_CfprApPolicyPolicyScopeOperStatus_Object = MibTableColumn
cfprApPolicyPolicyScopeOperStatus = _CfprApPolicyPolicyScopeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 16),
    _CfprApPolicyPolicyScopeOperStatus_Type()
)
cfprApPolicyPolicyScopeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeOperStatus.setStatus("current")
_CfprApPolicyPolicyScopeOwner_Type = CfprApPolicyPolicyOwner
_CfprApPolicyPolicyScopeOwner_Object = MibTableColumn
cfprApPolicyPolicyScopeOwner = _CfprApPolicyPolicyScopeOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 17),
    _CfprApPolicyPolicyScopeOwner_Type()
)
cfprApPolicyPolicyScopeOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeOwner.setStatus("current")
_CfprApPolicyPolicyScopePolicyName_Type = SnmpAdminString
_CfprApPolicyPolicyScopePolicyName_Object = MibTableColumn
cfprApPolicyPolicyScopePolicyName = _CfprApPolicyPolicyScopePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 18),
    _CfprApPolicyPolicyScopePolicyName_Type()
)
cfprApPolicyPolicyScopePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopePolicyName.setStatus("current")
_CfprApPolicyPolicyScopePolicyType_Type = SnmpAdminString
_CfprApPolicyPolicyScopePolicyType_Object = MibTableColumn
cfprApPolicyPolicyScopePolicyType = _CfprApPolicyPolicyScopePolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 19),
    _CfprApPolicyPolicyScopePolicyType_Type()
)
cfprApPolicyPolicyScopePolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopePolicyType.setStatus("current")
_CfprApPolicyPolicyScopeRecursive_Type = TruthValue
_CfprApPolicyPolicyScopeRecursive_Object = MibTableColumn
cfprApPolicyPolicyScopeRecursive = _CfprApPolicyPolicyScopeRecursive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 20),
    _CfprApPolicyPolicyScopeRecursive_Type()
)
cfprApPolicyPolicyScopeRecursive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeRecursive.setStatus("current")
_CfprApPolicyPolicyScopeResolveType_Type = CfprApPolicyPolicyResolveType
_CfprApPolicyPolicyScopeResolveType_Object = MibTableColumn
cfprApPolicyPolicyScopeResolveType = _CfprApPolicyPolicyScopeResolveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 26, 1, 21),
    _CfprApPolicyPolicyScopeResolveType_Type()
)
cfprApPolicyPolicyScopeResolveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeResolveType.setStatus("current")
_CfprApPolicyPolicyScopeContTable_Object = MibTable
cfprApPolicyPolicyScopeContTable = _CfprApPolicyPolicyScopeContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 27)
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContTable.setStatus("current")
_CfprApPolicyPolicyScopeContEntry_Object = MibTableRow
cfprApPolicyPolicyScopeContEntry = _CfprApPolicyPolicyScopeContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 27, 1)
)
cfprApPolicyPolicyScopeContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyPolicyScopeContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContEntry.setStatus("current")
_CfprApPolicyPolicyScopeContInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyPolicyScopeContInstanceId_Object = MibTableColumn
cfprApPolicyPolicyScopeContInstanceId = _CfprApPolicyPolicyScopeContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 27, 1, 1),
    _CfprApPolicyPolicyScopeContInstanceId_Type()
)
cfprApPolicyPolicyScopeContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContInstanceId.setStatus("current")
_CfprApPolicyPolicyScopeContDn_Type = CfprApManagedObjectDn
_CfprApPolicyPolicyScopeContDn_Object = MibTableColumn
cfprApPolicyPolicyScopeContDn = _CfprApPolicyPolicyScopeContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 27, 1, 2),
    _CfprApPolicyPolicyScopeContDn_Type()
)
cfprApPolicyPolicyScopeContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContDn.setStatus("current")
_CfprApPolicyPolicyScopeContRn_Type = SnmpAdminString
_CfprApPolicyPolicyScopeContRn_Object = MibTableColumn
cfprApPolicyPolicyScopeContRn = _CfprApPolicyPolicyScopeContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 27, 1, 3),
    _CfprApPolicyPolicyScopeContRn_Type()
)
cfprApPolicyPolicyScopeContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContRn.setStatus("current")
_CfprApPolicyPolicyScopeContAppType_Type = SnmpAdminString
_CfprApPolicyPolicyScopeContAppType_Object = MibTableColumn
cfprApPolicyPolicyScopeContAppType = _CfprApPolicyPolicyScopeContAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 27, 1, 4),
    _CfprApPolicyPolicyScopeContAppType_Type()
)
cfprApPolicyPolicyScopeContAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContAppType.setStatus("current")
_CfprApPolicyPolicyScopeContGenNum_Type = Gauge32
_CfprApPolicyPolicyScopeContGenNum_Object = MibTableColumn
cfprApPolicyPolicyScopeContGenNum = _CfprApPolicyPolicyScopeContGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 27, 1, 5),
    _CfprApPolicyPolicyScopeContGenNum_Type()
)
cfprApPolicyPolicyScopeContGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContGenNum.setStatus("current")
_CfprApPolicyPolicyScopeContNeedRecovery_Type = TruthValue
_CfprApPolicyPolicyScopeContNeedRecovery_Object = MibTableColumn
cfprApPolicyPolicyScopeContNeedRecovery = _CfprApPolicyPolicyScopeContNeedRecovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 27, 1, 6),
    _CfprApPolicyPolicyScopeContNeedRecovery_Type()
)
cfprApPolicyPolicyScopeContNeedRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContNeedRecovery.setStatus("current")
_CfprApPolicyPolicyScopeContextTable_Object = MibTable
cfprApPolicyPolicyScopeContextTable = _CfprApPolicyPolicyScopeContextTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 28)
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContextTable.setStatus("current")
_CfprApPolicyPolicyScopeContextEntry_Object = MibTableRow
cfprApPolicyPolicyScopeContextEntry = _CfprApPolicyPolicyScopeContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 28, 1)
)
cfprApPolicyPolicyScopeContextEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyPolicyScopeContextInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContextEntry.setStatus("current")
_CfprApPolicyPolicyScopeContextInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyPolicyScopeContextInstanceId_Object = MibTableColumn
cfprApPolicyPolicyScopeContextInstanceId = _CfprApPolicyPolicyScopeContextInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 28, 1, 1),
    _CfprApPolicyPolicyScopeContextInstanceId_Type()
)
cfprApPolicyPolicyScopeContextInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContextInstanceId.setStatus("current")
_CfprApPolicyPolicyScopeContextDn_Type = CfprApManagedObjectDn
_CfprApPolicyPolicyScopeContextDn_Object = MibTableColumn
cfprApPolicyPolicyScopeContextDn = _CfprApPolicyPolicyScopeContextDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 28, 1, 2),
    _CfprApPolicyPolicyScopeContextDn_Type()
)
cfprApPolicyPolicyScopeContextDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContextDn.setStatus("current")
_CfprApPolicyPolicyScopeContextRn_Type = SnmpAdminString
_CfprApPolicyPolicyScopeContextRn_Object = MibTableColumn
cfprApPolicyPolicyScopeContextRn = _CfprApPolicyPolicyScopeContextRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 28, 1, 3),
    _CfprApPolicyPolicyScopeContextRn_Type()
)
cfprApPolicyPolicyScopeContextRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContextRn.setStatus("current")
_CfprApPolicyPolicyScopeContextContext_Type = SnmpAdminString
_CfprApPolicyPolicyScopeContextContext_Object = MibTableColumn
cfprApPolicyPolicyScopeContextContext = _CfprApPolicyPolicyScopeContextContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 28, 1, 4),
    _CfprApPolicyPolicyScopeContextContext_Type()
)
cfprApPolicyPolicyScopeContextContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContextContext.setStatus("current")
_CfprApPolicyPolicyScopeContextName_Type = SnmpAdminString
_CfprApPolicyPolicyScopeContextName_Object = MibTableColumn
cfprApPolicyPolicyScopeContextName = _CfprApPolicyPolicyScopeContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 28, 1, 5),
    _CfprApPolicyPolicyScopeContextName_Type()
)
cfprApPolicyPolicyScopeContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeContextName.setStatus("current")
_CfprApPolicyPolicyScopeFsmTable_Object = MibTable
cfprApPolicyPolicyScopeFsmTable = _CfprApPolicyPolicyScopeFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29)
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmTable.setStatus("current")
_CfprApPolicyPolicyScopeFsmEntry_Object = MibTableRow
cfprApPolicyPolicyScopeFsmEntry = _CfprApPolicyPolicyScopeFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29, 1)
)
cfprApPolicyPolicyScopeFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyPolicyScopeFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmEntry.setStatus("current")
_CfprApPolicyPolicyScopeFsmInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyPolicyScopeFsmInstanceId_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmInstanceId = _CfprApPolicyPolicyScopeFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29, 1, 1),
    _CfprApPolicyPolicyScopeFsmInstanceId_Type()
)
cfprApPolicyPolicyScopeFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmInstanceId.setStatus("current")
_CfprApPolicyPolicyScopeFsmDn_Type = CfprApManagedObjectDn
_CfprApPolicyPolicyScopeFsmDn_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmDn = _CfprApPolicyPolicyScopeFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29, 1, 2),
    _CfprApPolicyPolicyScopeFsmDn_Type()
)
cfprApPolicyPolicyScopeFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmDn.setStatus("current")
_CfprApPolicyPolicyScopeFsmRn_Type = SnmpAdminString
_CfprApPolicyPolicyScopeFsmRn_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmRn = _CfprApPolicyPolicyScopeFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29, 1, 3),
    _CfprApPolicyPolicyScopeFsmRn_Type()
)
cfprApPolicyPolicyScopeFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmRn.setStatus("current")
_CfprApPolicyPolicyScopeFsmCompletionTime_Type = DateAndTime
_CfprApPolicyPolicyScopeFsmCompletionTime_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmCompletionTime = _CfprApPolicyPolicyScopeFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29, 1, 4),
    _CfprApPolicyPolicyScopeFsmCompletionTime_Type()
)
cfprApPolicyPolicyScopeFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmCompletionTime.setStatus("current")
_CfprApPolicyPolicyScopeFsmCurrentFsm_Type = CfprApPolicyPolicyScopeFsmCurrentFsm
_CfprApPolicyPolicyScopeFsmCurrentFsm_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmCurrentFsm = _CfprApPolicyPolicyScopeFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29, 1, 5),
    _CfprApPolicyPolicyScopeFsmCurrentFsm_Type()
)
cfprApPolicyPolicyScopeFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmCurrentFsm.setStatus("current")
_CfprApPolicyPolicyScopeFsmDescrData_Type = SnmpAdminString
_CfprApPolicyPolicyScopeFsmDescrData_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmDescrData = _CfprApPolicyPolicyScopeFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29, 1, 6),
    _CfprApPolicyPolicyScopeFsmDescrData_Type()
)
cfprApPolicyPolicyScopeFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmDescrData.setStatus("current")
_CfprApPolicyPolicyScopeFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApPolicyPolicyScopeFsmFsmStatus_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmFsmStatus = _CfprApPolicyPolicyScopeFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29, 1, 7),
    _CfprApPolicyPolicyScopeFsmFsmStatus_Type()
)
cfprApPolicyPolicyScopeFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmFsmStatus.setStatus("current")
_CfprApPolicyPolicyScopeFsmProgress_Type = Gauge32
_CfprApPolicyPolicyScopeFsmProgress_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmProgress = _CfprApPolicyPolicyScopeFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29, 1, 8),
    _CfprApPolicyPolicyScopeFsmProgress_Type()
)
cfprApPolicyPolicyScopeFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmProgress.setStatus("current")
_CfprApPolicyPolicyScopeFsmRmtErrCode_Type = Gauge32
_CfprApPolicyPolicyScopeFsmRmtErrCode_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmRmtErrCode = _CfprApPolicyPolicyScopeFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29, 1, 9),
    _CfprApPolicyPolicyScopeFsmRmtErrCode_Type()
)
cfprApPolicyPolicyScopeFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmRmtErrCode.setStatus("current")
_CfprApPolicyPolicyScopeFsmRmtErrDescr_Type = SnmpAdminString
_CfprApPolicyPolicyScopeFsmRmtErrDescr_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmRmtErrDescr = _CfprApPolicyPolicyScopeFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29, 1, 10),
    _CfprApPolicyPolicyScopeFsmRmtErrDescr_Type()
)
cfprApPolicyPolicyScopeFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmRmtErrDescr.setStatus("current")
_CfprApPolicyPolicyScopeFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApPolicyPolicyScopeFsmRmtRslt_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmRmtRslt = _CfprApPolicyPolicyScopeFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 29, 1, 11),
    _CfprApPolicyPolicyScopeFsmRmtRslt_Type()
)
cfprApPolicyPolicyScopeFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmRmtRslt.setStatus("current")
_CfprApPolicyPolicyScopeFsmStageTable_Object = MibTable
cfprApPolicyPolicyScopeFsmStageTable = _CfprApPolicyPolicyScopeFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 30)
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStageTable.setStatus("current")
_CfprApPolicyPolicyScopeFsmStageEntry_Object = MibTableRow
cfprApPolicyPolicyScopeFsmStageEntry = _CfprApPolicyPolicyScopeFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 30, 1)
)
cfprApPolicyPolicyScopeFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyPolicyScopeFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStageEntry.setStatus("current")
_CfprApPolicyPolicyScopeFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyPolicyScopeFsmStageInstanceId_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmStageInstanceId = _CfprApPolicyPolicyScopeFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 30, 1, 1),
    _CfprApPolicyPolicyScopeFsmStageInstanceId_Type()
)
cfprApPolicyPolicyScopeFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStageInstanceId.setStatus("current")
_CfprApPolicyPolicyScopeFsmStageDn_Type = CfprApManagedObjectDn
_CfprApPolicyPolicyScopeFsmStageDn_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmStageDn = _CfprApPolicyPolicyScopeFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 30, 1, 2),
    _CfprApPolicyPolicyScopeFsmStageDn_Type()
)
cfprApPolicyPolicyScopeFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStageDn.setStatus("current")
_CfprApPolicyPolicyScopeFsmStageRn_Type = SnmpAdminString
_CfprApPolicyPolicyScopeFsmStageRn_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmStageRn = _CfprApPolicyPolicyScopeFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 30, 1, 3),
    _CfprApPolicyPolicyScopeFsmStageRn_Type()
)
cfprApPolicyPolicyScopeFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStageRn.setStatus("current")
_CfprApPolicyPolicyScopeFsmStageDescrData_Type = SnmpAdminString
_CfprApPolicyPolicyScopeFsmStageDescrData_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmStageDescrData = _CfprApPolicyPolicyScopeFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 30, 1, 4),
    _CfprApPolicyPolicyScopeFsmStageDescrData_Type()
)
cfprApPolicyPolicyScopeFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStageDescrData.setStatus("current")
_CfprApPolicyPolicyScopeFsmStageLastUpdateTime_Type = DateAndTime
_CfprApPolicyPolicyScopeFsmStageLastUpdateTime_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmStageLastUpdateTime = _CfprApPolicyPolicyScopeFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 30, 1, 5),
    _CfprApPolicyPolicyScopeFsmStageLastUpdateTime_Type()
)
cfprApPolicyPolicyScopeFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStageLastUpdateTime.setStatus("current")
_CfprApPolicyPolicyScopeFsmStageName_Type = CfprApPolicyPolicyScopeFsmStageName
_CfprApPolicyPolicyScopeFsmStageName_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmStageName = _CfprApPolicyPolicyScopeFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 30, 1, 6),
    _CfprApPolicyPolicyScopeFsmStageName_Type()
)
cfprApPolicyPolicyScopeFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStageName.setStatus("current")
_CfprApPolicyPolicyScopeFsmStageOrder_Type = Gauge32
_CfprApPolicyPolicyScopeFsmStageOrder_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmStageOrder = _CfprApPolicyPolicyScopeFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 30, 1, 7),
    _CfprApPolicyPolicyScopeFsmStageOrder_Type()
)
cfprApPolicyPolicyScopeFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStageOrder.setStatus("current")
_CfprApPolicyPolicyScopeFsmStageRetry_Type = Gauge32
_CfprApPolicyPolicyScopeFsmStageRetry_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmStageRetry = _CfprApPolicyPolicyScopeFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 30, 1, 8),
    _CfprApPolicyPolicyScopeFsmStageRetry_Type()
)
cfprApPolicyPolicyScopeFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStageRetry.setStatus("current")
_CfprApPolicyPolicyScopeFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApPolicyPolicyScopeFsmStageStageStatus_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmStageStageStatus = _CfprApPolicyPolicyScopeFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 30, 1, 9),
    _CfprApPolicyPolicyScopeFsmStageStageStatus_Type()
)
cfprApPolicyPolicyScopeFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmStageStageStatus.setStatus("current")
_CfprApPolicyPolicyScopeFsmTaskTable_Object = MibTable
cfprApPolicyPolicyScopeFsmTaskTable = _CfprApPolicyPolicyScopeFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 31)
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmTaskTable.setStatus("current")
_CfprApPolicyPolicyScopeFsmTaskEntry_Object = MibTableRow
cfprApPolicyPolicyScopeFsmTaskEntry = _CfprApPolicyPolicyScopeFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 31, 1)
)
cfprApPolicyPolicyScopeFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyPolicyScopeFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmTaskEntry.setStatus("current")
_CfprApPolicyPolicyScopeFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyPolicyScopeFsmTaskInstanceId_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmTaskInstanceId = _CfprApPolicyPolicyScopeFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 31, 1, 1),
    _CfprApPolicyPolicyScopeFsmTaskInstanceId_Type()
)
cfprApPolicyPolicyScopeFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmTaskInstanceId.setStatus("current")
_CfprApPolicyPolicyScopeFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApPolicyPolicyScopeFsmTaskDn_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmTaskDn = _CfprApPolicyPolicyScopeFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 31, 1, 2),
    _CfprApPolicyPolicyScopeFsmTaskDn_Type()
)
cfprApPolicyPolicyScopeFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmTaskDn.setStatus("current")
_CfprApPolicyPolicyScopeFsmTaskRn_Type = SnmpAdminString
_CfprApPolicyPolicyScopeFsmTaskRn_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmTaskRn = _CfprApPolicyPolicyScopeFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 31, 1, 3),
    _CfprApPolicyPolicyScopeFsmTaskRn_Type()
)
cfprApPolicyPolicyScopeFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmTaskRn.setStatus("current")
_CfprApPolicyPolicyScopeFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApPolicyPolicyScopeFsmTaskCompletion_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmTaskCompletion = _CfprApPolicyPolicyScopeFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 31, 1, 4),
    _CfprApPolicyPolicyScopeFsmTaskCompletion_Type()
)
cfprApPolicyPolicyScopeFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmTaskCompletion.setStatus("current")
_CfprApPolicyPolicyScopeFsmTaskFlags_Type = CfprApFsmFlags
_CfprApPolicyPolicyScopeFsmTaskFlags_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmTaskFlags = _CfprApPolicyPolicyScopeFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 31, 1, 5),
    _CfprApPolicyPolicyScopeFsmTaskFlags_Type()
)
cfprApPolicyPolicyScopeFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmTaskFlags.setStatus("current")
_CfprApPolicyPolicyScopeFsmTaskItem_Type = CfprApPolicyPolicyScopeFsmTaskItem
_CfprApPolicyPolicyScopeFsmTaskItem_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmTaskItem = _CfprApPolicyPolicyScopeFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 31, 1, 6),
    _CfprApPolicyPolicyScopeFsmTaskItem_Type()
)
cfprApPolicyPolicyScopeFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmTaskItem.setStatus("current")
_CfprApPolicyPolicyScopeFsmTaskSeqId_Type = Gauge32
_CfprApPolicyPolicyScopeFsmTaskSeqId_Object = MibTableColumn
cfprApPolicyPolicyScopeFsmTaskSeqId = _CfprApPolicyPolicyScopeFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 31, 1, 7),
    _CfprApPolicyPolicyScopeFsmTaskSeqId_Type()
)
cfprApPolicyPolicyScopeFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPolicyScopeFsmTaskSeqId.setStatus("current")
_CfprApPolicyPowerMgmtTable_Object = MibTable
cfprApPolicyPowerMgmtTable = _CfprApPolicyPowerMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 32)
)
if mibBuilder.loadTexts:
    cfprApPolicyPowerMgmtTable.setStatus("current")
_CfprApPolicyPowerMgmtEntry_Object = MibTableRow
cfprApPolicyPowerMgmtEntry = _CfprApPolicyPowerMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 32, 1)
)
cfprApPolicyPowerMgmtEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyPowerMgmtInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyPowerMgmtEntry.setStatus("current")
_CfprApPolicyPowerMgmtInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyPowerMgmtInstanceId_Object = MibTableColumn
cfprApPolicyPowerMgmtInstanceId = _CfprApPolicyPowerMgmtInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 32, 1, 1),
    _CfprApPolicyPowerMgmtInstanceId_Type()
)
cfprApPolicyPowerMgmtInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyPowerMgmtInstanceId.setStatus("current")
_CfprApPolicyPowerMgmtDn_Type = CfprApManagedObjectDn
_CfprApPolicyPowerMgmtDn_Object = MibTableColumn
cfprApPolicyPowerMgmtDn = _CfprApPolicyPowerMgmtDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 32, 1, 2),
    _CfprApPolicyPowerMgmtDn_Type()
)
cfprApPolicyPowerMgmtDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPowerMgmtDn.setStatus("current")
_CfprApPolicyPowerMgmtRn_Type = SnmpAdminString
_CfprApPolicyPowerMgmtRn_Object = MibTableColumn
cfprApPolicyPowerMgmtRn = _CfprApPolicyPowerMgmtRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 32, 1, 3),
    _CfprApPolicyPowerMgmtRn_Type()
)
cfprApPolicyPowerMgmtRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPowerMgmtRn.setStatus("current")
_CfprApPolicyPowerMgmtSource_Type = CfprApPolicyControlSource
_CfprApPolicyPowerMgmtSource_Object = MibTableColumn
cfprApPolicyPowerMgmtSource = _CfprApPolicyPowerMgmtSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 32, 1, 4),
    _CfprApPolicyPowerMgmtSource_Type()
)
cfprApPolicyPowerMgmtSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPowerMgmtSource.setStatus("current")
_CfprApPolicyPsuTable_Object = MibTable
cfprApPolicyPsuTable = _CfprApPolicyPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 33)
)
if mibBuilder.loadTexts:
    cfprApPolicyPsuTable.setStatus("current")
_CfprApPolicyPsuEntry_Object = MibTableRow
cfprApPolicyPsuEntry = _CfprApPolicyPsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 33, 1)
)
cfprApPolicyPsuEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyPsuInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyPsuEntry.setStatus("current")
_CfprApPolicyPsuInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyPsuInstanceId_Object = MibTableColumn
cfprApPolicyPsuInstanceId = _CfprApPolicyPsuInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 33, 1, 1),
    _CfprApPolicyPsuInstanceId_Type()
)
cfprApPolicyPsuInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyPsuInstanceId.setStatus("current")
_CfprApPolicyPsuDn_Type = CfprApManagedObjectDn
_CfprApPolicyPsuDn_Object = MibTableColumn
cfprApPolicyPsuDn = _CfprApPolicyPsuDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 33, 1, 2),
    _CfprApPolicyPsuDn_Type()
)
cfprApPolicyPsuDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPsuDn.setStatus("current")
_CfprApPolicyPsuRn_Type = SnmpAdminString
_CfprApPolicyPsuRn_Object = MibTableColumn
cfprApPolicyPsuRn = _CfprApPolicyPsuRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 33, 1, 3),
    _CfprApPolicyPsuRn_Type()
)
cfprApPolicyPsuRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPsuRn.setStatus("current")
_CfprApPolicyPsuSource_Type = CfprApPolicyControlSource
_CfprApPolicyPsuSource_Object = MibTableColumn
cfprApPolicyPsuSource = _CfprApPolicyPsuSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 33, 1, 4),
    _CfprApPolicyPsuSource_Type()
)
cfprApPolicyPsuSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyPsuSource.setStatus("current")
_CfprApPolicyRefReqTable_Object = MibTable
cfprApPolicyRefReqTable = _CfprApPolicyRefReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 34)
)
if mibBuilder.loadTexts:
    cfprApPolicyRefReqTable.setStatus("current")
_CfprApPolicyRefReqEntry_Object = MibTableRow
cfprApPolicyRefReqEntry = _CfprApPolicyRefReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 34, 1)
)
cfprApPolicyRefReqEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicyRefReqInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicyRefReqEntry.setStatus("current")
_CfprApPolicyRefReqInstanceId_Type = CfprApManagedObjectId
_CfprApPolicyRefReqInstanceId_Object = MibTableColumn
cfprApPolicyRefReqInstanceId = _CfprApPolicyRefReqInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 34, 1, 1),
    _CfprApPolicyRefReqInstanceId_Type()
)
cfprApPolicyRefReqInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicyRefReqInstanceId.setStatus("current")
_CfprApPolicyRefReqDn_Type = CfprApManagedObjectDn
_CfprApPolicyRefReqDn_Object = MibTableColumn
cfprApPolicyRefReqDn = _CfprApPolicyRefReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 34, 1, 2),
    _CfprApPolicyRefReqDn_Type()
)
cfprApPolicyRefReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyRefReqDn.setStatus("current")
_CfprApPolicyRefReqRn_Type = SnmpAdminString
_CfprApPolicyRefReqRn_Object = MibTableColumn
cfprApPolicyRefReqRn = _CfprApPolicyRefReqRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 34, 1, 3),
    _CfprApPolicyRefReqRn_Type()
)
cfprApPolicyRefReqRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyRefReqRn.setStatus("current")
_CfprApPolicyRefReqPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApPolicyRefReqPolicyOwner_Object = MibTableColumn
cfprApPolicyRefReqPolicyOwner = _CfprApPolicyRefReqPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 34, 1, 4),
    _CfprApPolicyRefReqPolicyOwner_Type()
)
cfprApPolicyRefReqPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyRefReqPolicyOwner.setStatus("current")
_CfprApPolicyRefReqRefConvertedDn_Type = SnmpAdminString
_CfprApPolicyRefReqRefConvertedDn_Object = MibTableColumn
cfprApPolicyRefReqRefConvertedDn = _CfprApPolicyRefReqRefConvertedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 34, 1, 5),
    _CfprApPolicyRefReqRefConvertedDn_Type()
)
cfprApPolicyRefReqRefConvertedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyRefReqRefConvertedDn.setStatus("current")
_CfprApPolicyRefReqRefPolicyDn_Type = SnmpAdminString
_CfprApPolicyRefReqRefPolicyDn_Object = MibTableColumn
cfprApPolicyRefReqRefPolicyDn = _CfprApPolicyRefReqRefPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 34, 1, 6),
    _CfprApPolicyRefReqRefPolicyDn_Type()
)
cfprApPolicyRefReqRefPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicyRefReqRefPolicyDn.setStatus("current")
_CfprApPolicySecurityTable_Object = MibTable
cfprApPolicySecurityTable = _CfprApPolicySecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 35)
)
if mibBuilder.loadTexts:
    cfprApPolicySecurityTable.setStatus("current")
_CfprApPolicySecurityEntry_Object = MibTableRow
cfprApPolicySecurityEntry = _CfprApPolicySecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 35, 1)
)
cfprApPolicySecurityEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-POLICY-MIB", "cfprApPolicySecurityInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApPolicySecurityEntry.setStatus("current")
_CfprApPolicySecurityInstanceId_Type = CfprApManagedObjectId
_CfprApPolicySecurityInstanceId_Object = MibTableColumn
cfprApPolicySecurityInstanceId = _CfprApPolicySecurityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 35, 1, 1),
    _CfprApPolicySecurityInstanceId_Type()
)
cfprApPolicySecurityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApPolicySecurityInstanceId.setStatus("current")
_CfprApPolicySecurityDn_Type = CfprApManagedObjectDn
_CfprApPolicySecurityDn_Object = MibTableColumn
cfprApPolicySecurityDn = _CfprApPolicySecurityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 35, 1, 2),
    _CfprApPolicySecurityDn_Type()
)
cfprApPolicySecurityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicySecurityDn.setStatus("current")
_CfprApPolicySecurityRn_Type = SnmpAdminString
_CfprApPolicySecurityRn_Object = MibTableColumn
cfprApPolicySecurityRn = _CfprApPolicySecurityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 35, 1, 3),
    _CfprApPolicySecurityRn_Type()
)
cfprApPolicySecurityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicySecurityRn.setStatus("current")
_CfprApPolicySecuritySource_Type = CfprApPolicyControlSource
_CfprApPolicySecuritySource_Object = MibTableColumn
cfprApPolicySecuritySource = _CfprApPolicySecuritySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 62, 35, 1, 4),
    _CfprApPolicySecuritySource_Type()
)
cfprApPolicySecuritySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApPolicySecuritySource.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-POLICY-MIB",
    **{"cfprApPolicyObjects": cfprApPolicyObjects,
       "cfprApPolicyCentraleSyncTable": cfprApPolicyCentraleSyncTable,
       "cfprApPolicyCentraleSyncEntry": cfprApPolicyCentraleSyncEntry,
       "cfprApPolicyCentraleSyncInstanceId": cfprApPolicyCentraleSyncInstanceId,
       "cfprApPolicyCentraleSyncDn": cfprApPolicyCentraleSyncDn,
       "cfprApPolicyCentraleSyncRn": cfprApPolicyCentraleSyncRn,
       "cfprApPolicyCentraleSyncLeftData": cfprApPolicyCentraleSyncLeftData,
       "cfprApPolicyCentraleSyncRightData": cfprApPolicyCentraleSyncRightData,
       "cfprApPolicyCommunicationTable": cfprApPolicyCommunicationTable,
       "cfprApPolicyCommunicationEntry": cfprApPolicyCommunicationEntry,
       "cfprApPolicyCommunicationInstanceId": cfprApPolicyCommunicationInstanceId,
       "cfprApPolicyCommunicationDn": cfprApPolicyCommunicationDn,
       "cfprApPolicyCommunicationRn": cfprApPolicyCommunicationRn,
       "cfprApPolicyCommunicationSource": cfprApPolicyCommunicationSource,
       "cfprApPolicyConfigBackupTable": cfprApPolicyConfigBackupTable,
       "cfprApPolicyConfigBackupEntry": cfprApPolicyConfigBackupEntry,
       "cfprApPolicyConfigBackupInstanceId": cfprApPolicyConfigBackupInstanceId,
       "cfprApPolicyConfigBackupDn": cfprApPolicyConfigBackupDn,
       "cfprApPolicyConfigBackupRn": cfprApPolicyConfigBackupRn,
       "cfprApPolicyConfigBackupSource": cfprApPolicyConfigBackupSource,
       "cfprApPolicyControlEpTable": cfprApPolicyControlEpTable,
       "cfprApPolicyControlEpEntry": cfprApPolicyControlEpEntry,
       "cfprApPolicyControlEpInstanceId": cfprApPolicyControlEpInstanceId,
       "cfprApPolicyControlEpDn": cfprApPolicyControlEpDn,
       "cfprApPolicyControlEpRn": cfprApPolicyControlEpRn,
       "cfprApPolicyControlEpAckState": cfprApPolicyControlEpAckState,
       "cfprApPolicyControlEpCleanupMode": cfprApPolicyControlEpCleanupMode,
       "cfprApPolicyControlEpEncSecret": cfprApPolicyControlEpEncSecret,
       "cfprApPolicyControlEpFsmDescr": cfprApPolicyControlEpFsmDescr,
       "cfprApPolicyControlEpFsmPrev": cfprApPolicyControlEpFsmPrev,
       "cfprApPolicyControlEpFsmProgr": cfprApPolicyControlEpFsmProgr,
       "cfprApPolicyControlEpFsmRmtInvErrCode": cfprApPolicyControlEpFsmRmtInvErrCode,
       "cfprApPolicyControlEpFsmRmtInvErrDescr": cfprApPolicyControlEpFsmRmtInvErrDescr,
       "cfprApPolicyControlEpFsmRmtInvRslt": cfprApPolicyControlEpFsmRmtInvRslt,
       "cfprApPolicyControlEpFsmStageDescr": cfprApPolicyControlEpFsmStageDescr,
       "cfprApPolicyControlEpFsmStamp": cfprApPolicyControlEpFsmStamp,
       "cfprApPolicyControlEpFsmStatus": cfprApPolicyControlEpFsmStatus,
       "cfprApPolicyControlEpFsmTry": cfprApPolicyControlEpFsmTry,
       "cfprApPolicyControlEpName": cfprApPolicyControlEpName,
       "cfprApPolicyControlEpRegistrationState": cfprApPolicyControlEpRegistrationState,
       "cfprApPolicyControlEpRepairState": cfprApPolicyControlEpRepairState,
       "cfprApPolicyControlEpSecret": cfprApPolicyControlEpSecret,
       "cfprApPolicyControlEpState": cfprApPolicyControlEpState,
       "cfprApPolicyControlEpSuspendState": cfprApPolicyControlEpSuspendState,
       "cfprApPolicyControlEpSvcRegIP": cfprApPolicyControlEpSvcRegIP,
       "cfprApPolicyControlEpSvcRegName": cfprApPolicyControlEpSvcRegName,
       "cfprApPolicyControlEpType": cfprApPolicyControlEpType,
       "cfprApPolicyControlEpFsmTable": cfprApPolicyControlEpFsmTable,
       "cfprApPolicyControlEpFsmEntry": cfprApPolicyControlEpFsmEntry,
       "cfprApPolicyControlEpFsmInstanceId": cfprApPolicyControlEpFsmInstanceId,
       "cfprApPolicyControlEpFsmDn": cfprApPolicyControlEpFsmDn,
       "cfprApPolicyControlEpFsmRn": cfprApPolicyControlEpFsmRn,
       "cfprApPolicyControlEpFsmCompletionTime": cfprApPolicyControlEpFsmCompletionTime,
       "cfprApPolicyControlEpFsmCurrentFsm": cfprApPolicyControlEpFsmCurrentFsm,
       "cfprApPolicyControlEpFsmDescrData": cfprApPolicyControlEpFsmDescrData,
       "cfprApPolicyControlEpFsmFsmStatus": cfprApPolicyControlEpFsmFsmStatus,
       "cfprApPolicyControlEpFsmProgress": cfprApPolicyControlEpFsmProgress,
       "cfprApPolicyControlEpFsmRmtErrCode": cfprApPolicyControlEpFsmRmtErrCode,
       "cfprApPolicyControlEpFsmRmtErrDescr": cfprApPolicyControlEpFsmRmtErrDescr,
       "cfprApPolicyControlEpFsmRmtRslt": cfprApPolicyControlEpFsmRmtRslt,
       "cfprApPolicyControlEpFsmStageTable": cfprApPolicyControlEpFsmStageTable,
       "cfprApPolicyControlEpFsmStageEntry": cfprApPolicyControlEpFsmStageEntry,
       "cfprApPolicyControlEpFsmStageInstanceId": cfprApPolicyControlEpFsmStageInstanceId,
       "cfprApPolicyControlEpFsmStageDn": cfprApPolicyControlEpFsmStageDn,
       "cfprApPolicyControlEpFsmStageRn": cfprApPolicyControlEpFsmStageRn,
       "cfprApPolicyControlEpFsmStageDescrData": cfprApPolicyControlEpFsmStageDescrData,
       "cfprApPolicyControlEpFsmStageLastUpdateTime": cfprApPolicyControlEpFsmStageLastUpdateTime,
       "cfprApPolicyControlEpFsmStageName": cfprApPolicyControlEpFsmStageName,
       "cfprApPolicyControlEpFsmStageOrder": cfprApPolicyControlEpFsmStageOrder,
       "cfprApPolicyControlEpFsmStageRetry": cfprApPolicyControlEpFsmStageRetry,
       "cfprApPolicyControlEpFsmStageStageStatus": cfprApPolicyControlEpFsmStageStageStatus,
       "cfprApPolicyControlEpFsmTaskTable": cfprApPolicyControlEpFsmTaskTable,
       "cfprApPolicyControlEpFsmTaskEntry": cfprApPolicyControlEpFsmTaskEntry,
       "cfprApPolicyControlEpFsmTaskInstanceId": cfprApPolicyControlEpFsmTaskInstanceId,
       "cfprApPolicyControlEpFsmTaskDn": cfprApPolicyControlEpFsmTaskDn,
       "cfprApPolicyControlEpFsmTaskRn": cfprApPolicyControlEpFsmTaskRn,
       "cfprApPolicyControlEpFsmTaskCompletion": cfprApPolicyControlEpFsmTaskCompletion,
       "cfprApPolicyControlEpFsmTaskFlags": cfprApPolicyControlEpFsmTaskFlags,
       "cfprApPolicyControlEpFsmTaskItem": cfprApPolicyControlEpFsmTaskItem,
       "cfprApPolicyControlEpFsmTaskSeqId": cfprApPolicyControlEpFsmTaskSeqId,
       "cfprApPolicyControlledInstanceTable": cfprApPolicyControlledInstanceTable,
       "cfprApPolicyControlledInstanceEntry": cfprApPolicyControlledInstanceEntry,
       "cfprApPolicyControlledInstanceInstanceId": cfprApPolicyControlledInstanceInstanceId,
       "cfprApPolicyControlledInstanceDn": cfprApPolicyControlledInstanceDn,
       "cfprApPolicyControlledInstanceRn": cfprApPolicyControlledInstanceRn,
       "cfprApPolicyControlledInstanceDefDn": cfprApPolicyControlledInstanceDefDn,
       "cfprApPolicyControlledInstanceExternalResolveName": cfprApPolicyControlledInstanceExternalResolveName,
       "cfprApPolicyControlledInstanceName": cfprApPolicyControlledInstanceName,
       "cfprApPolicyControlledInstanceResolveType": cfprApPolicyControlledInstanceResolveType,
       "cfprApPolicyControlledInstanceType": cfprApPolicyControlledInstanceType,
       "cfprApPolicyControlledTypeTable": cfprApPolicyControlledTypeTable,
       "cfprApPolicyControlledTypeEntry": cfprApPolicyControlledTypeEntry,
       "cfprApPolicyControlledTypeInstanceId": cfprApPolicyControlledTypeInstanceId,
       "cfprApPolicyControlledTypeDn": cfprApPolicyControlledTypeDn,
       "cfprApPolicyControlledTypeRn": cfprApPolicyControlledTypeRn,
       "cfprApPolicyControlledTypeFsmDescr": cfprApPolicyControlledTypeFsmDescr,
       "cfprApPolicyControlledTypeFsmPrev": cfprApPolicyControlledTypeFsmPrev,
       "cfprApPolicyControlledTypeFsmProgr": cfprApPolicyControlledTypeFsmProgr,
       "cfprApPolicyControlledTypeFsmRmtInvErrCode": cfprApPolicyControlledTypeFsmRmtInvErrCode,
       "cfprApPolicyControlledTypeFsmRmtInvErrDescr": cfprApPolicyControlledTypeFsmRmtInvErrDescr,
       "cfprApPolicyControlledTypeFsmRmtInvRslt": cfprApPolicyControlledTypeFsmRmtInvRslt,
       "cfprApPolicyControlledTypeFsmStageDescr": cfprApPolicyControlledTypeFsmStageDescr,
       "cfprApPolicyControlledTypeFsmStamp": cfprApPolicyControlledTypeFsmStamp,
       "cfprApPolicyControlledTypeFsmStatus": cfprApPolicyControlledTypeFsmStatus,
       "cfprApPolicyControlledTypeFsmTry": cfprApPolicyControlledTypeFsmTry,
       "cfprApPolicyControlledTypeParentContext": cfprApPolicyControlledTypeParentContext,
       "cfprApPolicyControlledTypeType": cfprApPolicyControlledTypeType,
       "cfprApPolicyControlledTypeFsmTable": cfprApPolicyControlledTypeFsmTable,
       "cfprApPolicyControlledTypeFsmEntry": cfprApPolicyControlledTypeFsmEntry,
       "cfprApPolicyControlledTypeFsmInstanceId": cfprApPolicyControlledTypeFsmInstanceId,
       "cfprApPolicyControlledTypeFsmDn": cfprApPolicyControlledTypeFsmDn,
       "cfprApPolicyControlledTypeFsmRn": cfprApPolicyControlledTypeFsmRn,
       "cfprApPolicyControlledTypeFsmCompletionTime": cfprApPolicyControlledTypeFsmCompletionTime,
       "cfprApPolicyControlledTypeFsmCurrentFsm": cfprApPolicyControlledTypeFsmCurrentFsm,
       "cfprApPolicyControlledTypeFsmDescrData": cfprApPolicyControlledTypeFsmDescrData,
       "cfprApPolicyControlledTypeFsmFsmStatus": cfprApPolicyControlledTypeFsmFsmStatus,
       "cfprApPolicyControlledTypeFsmProgress": cfprApPolicyControlledTypeFsmProgress,
       "cfprApPolicyControlledTypeFsmRmtErrCode": cfprApPolicyControlledTypeFsmRmtErrCode,
       "cfprApPolicyControlledTypeFsmRmtErrDescr": cfprApPolicyControlledTypeFsmRmtErrDescr,
       "cfprApPolicyControlledTypeFsmRmtRslt": cfprApPolicyControlledTypeFsmRmtRslt,
       "cfprApPolicyControlledTypeFsmStageTable": cfprApPolicyControlledTypeFsmStageTable,
       "cfprApPolicyControlledTypeFsmStageEntry": cfprApPolicyControlledTypeFsmStageEntry,
       "cfprApPolicyControlledTypeFsmStageInstanceId": cfprApPolicyControlledTypeFsmStageInstanceId,
       "cfprApPolicyControlledTypeFsmStageDn": cfprApPolicyControlledTypeFsmStageDn,
       "cfprApPolicyControlledTypeFsmStageRn": cfprApPolicyControlledTypeFsmStageRn,
       "cfprApPolicyControlledTypeFsmStageDescrData": cfprApPolicyControlledTypeFsmStageDescrData,
       "cfprApPolicyControlledTypeFsmStageLastUpdateTime": cfprApPolicyControlledTypeFsmStageLastUpdateTime,
       "cfprApPolicyControlledTypeFsmStageName": cfprApPolicyControlledTypeFsmStageName,
       "cfprApPolicyControlledTypeFsmStageOrder": cfprApPolicyControlledTypeFsmStageOrder,
       "cfprApPolicyControlledTypeFsmStageRetry": cfprApPolicyControlledTypeFsmStageRetry,
       "cfprApPolicyControlledTypeFsmStageStageStatus": cfprApPolicyControlledTypeFsmStageStageStatus,
       "cfprApPolicyControlledTypeFsmTaskTable": cfprApPolicyControlledTypeFsmTaskTable,
       "cfprApPolicyControlledTypeFsmTaskEntry": cfprApPolicyControlledTypeFsmTaskEntry,
       "cfprApPolicyControlledTypeFsmTaskInstanceId": cfprApPolicyControlledTypeFsmTaskInstanceId,
       "cfprApPolicyControlledTypeFsmTaskDn": cfprApPolicyControlledTypeFsmTaskDn,
       "cfprApPolicyControlledTypeFsmTaskRn": cfprApPolicyControlledTypeFsmTaskRn,
       "cfprApPolicyControlledTypeFsmTaskCompletion": cfprApPolicyControlledTypeFsmTaskCompletion,
       "cfprApPolicyControlledTypeFsmTaskFlags": cfprApPolicyControlledTypeFsmTaskFlags,
       "cfprApPolicyControlledTypeFsmTaskItem": cfprApPolicyControlledTypeFsmTaskItem,
       "cfprApPolicyControlledTypeFsmTaskSeqId": cfprApPolicyControlledTypeFsmTaskSeqId,
       "cfprApPolicyDateTimeTable": cfprApPolicyDateTimeTable,
       "cfprApPolicyDateTimeEntry": cfprApPolicyDateTimeEntry,
       "cfprApPolicyDateTimeInstanceId": cfprApPolicyDateTimeInstanceId,
       "cfprApPolicyDateTimeDn": cfprApPolicyDateTimeDn,
       "cfprApPolicyDateTimeRn": cfprApPolicyDateTimeRn,
       "cfprApPolicyDateTimeSource": cfprApPolicyDateTimeSource,
       "cfprApPolicyDigestTable": cfprApPolicyDigestTable,
       "cfprApPolicyDigestEntry": cfprApPolicyDigestEntry,
       "cfprApPolicyDigestInstanceId": cfprApPolicyDigestInstanceId,
       "cfprApPolicyDigestDn": cfprApPolicyDigestDn,
       "cfprApPolicyDigestRn": cfprApPolicyDigestRn,
       "cfprApPolicyDigestContext": cfprApPolicyDigestContext,
       "cfprApPolicyDigestDescr": cfprApPolicyDigestDescr,
       "cfprApPolicyDigestLabel": cfprApPolicyDigestLabel,
       "cfprApPolicyDigestName": cfprApPolicyDigestName,
       "cfprApPolicyDigestOnBehalfOfIdent": cfprApPolicyDigestOnBehalfOfIdent,
       "cfprApPolicyDigestOnBehalfOfType": cfprApPolicyDigestOnBehalfOfType,
       "cfprApPolicyDigestRequestorOwnership": cfprApPolicyDigestRequestorOwnership,
       "cfprApPolicyDigestResolveType": cfprApPolicyDigestResolveType,
       "cfprApPolicyDigestType": cfprApPolicyDigestType,
       "cfprApPolicyDigestUsage": cfprApPolicyDigestUsage,
       "cfprApPolicyDiscoveryTable": cfprApPolicyDiscoveryTable,
       "cfprApPolicyDiscoveryEntry": cfprApPolicyDiscoveryEntry,
       "cfprApPolicyDiscoveryInstanceId": cfprApPolicyDiscoveryInstanceId,
       "cfprApPolicyDiscoveryDn": cfprApPolicyDiscoveryDn,
       "cfprApPolicyDiscoveryRn": cfprApPolicyDiscoveryRn,
       "cfprApPolicyDiscoverySource": cfprApPolicyDiscoverySource,
       "cfprApPolicyDnsTable": cfprApPolicyDnsTable,
       "cfprApPolicyDnsEntry": cfprApPolicyDnsEntry,
       "cfprApPolicyDnsInstanceId": cfprApPolicyDnsInstanceId,
       "cfprApPolicyDnsDn": cfprApPolicyDnsDn,
       "cfprApPolicyDnsRn": cfprApPolicyDnsRn,
       "cfprApPolicyDnsSource": cfprApPolicyDnsSource,
       "cfprApPolicyElementTable": cfprApPolicyElementTable,
       "cfprApPolicyElementEntry": cfprApPolicyElementEntry,
       "cfprApPolicyElementInstanceId": cfprApPolicyElementInstanceId,
       "cfprApPolicyElementDn": cfprApPolicyElementDn,
       "cfprApPolicyElementRn": cfprApPolicyElementRn,
       "cfprApPolicyElementClassType": cfprApPolicyElementClassType,
       "cfprApPolicyElementConvertedDn": cfprApPolicyElementConvertedDn,
       "cfprApPolicyElementOwnership": cfprApPolicyElementOwnership,
       "cfprApPolicyElementPolicyDn": cfprApPolicyElementPolicyDn,
       "cfprApPolicyFaultTable": cfprApPolicyFaultTable,
       "cfprApPolicyFaultEntry": cfprApPolicyFaultEntry,
       "cfprApPolicyFaultInstanceId": cfprApPolicyFaultInstanceId,
       "cfprApPolicyFaultDn": cfprApPolicyFaultDn,
       "cfprApPolicyFaultRn": cfprApPolicyFaultRn,
       "cfprApPolicyFaultSource": cfprApPolicyFaultSource,
       "cfprApPolicyIdResolvePolicyTable": cfprApPolicyIdResolvePolicyTable,
       "cfprApPolicyIdResolvePolicyEntry": cfprApPolicyIdResolvePolicyEntry,
       "cfprApPolicyIdResolvePolicyInstanceId": cfprApPolicyIdResolvePolicyInstanceId,
       "cfprApPolicyIdResolvePolicyDn": cfprApPolicyIdResolvePolicyDn,
       "cfprApPolicyIdResolvePolicyRn": cfprApPolicyIdResolvePolicyRn,
       "cfprApPolicyIdResolvePolicyIdAssignmentMode": cfprApPolicyIdResolvePolicyIdAssignmentMode,
       "cfprApPolicyInfraFirmwareTable": cfprApPolicyInfraFirmwareTable,
       "cfprApPolicyInfraFirmwareEntry": cfprApPolicyInfraFirmwareEntry,
       "cfprApPolicyInfraFirmwareInstanceId": cfprApPolicyInfraFirmwareInstanceId,
       "cfprApPolicyInfraFirmwareDn": cfprApPolicyInfraFirmwareDn,
       "cfprApPolicyInfraFirmwareRn": cfprApPolicyInfraFirmwareRn,
       "cfprApPolicyInfraFirmwareSource": cfprApPolicyInfraFirmwareSource,
       "cfprApPolicyLocalMapTable": cfprApPolicyLocalMapTable,
       "cfprApPolicyLocalMapEntry": cfprApPolicyLocalMapEntry,
       "cfprApPolicyLocalMapInstanceId": cfprApPolicyLocalMapInstanceId,
       "cfprApPolicyLocalMapDn": cfprApPolicyLocalMapDn,
       "cfprApPolicyLocalMapRn": cfprApPolicyLocalMapRn,
       "cfprApPolicyMEpTable": cfprApPolicyMEpTable,
       "cfprApPolicyMEpEntry": cfprApPolicyMEpEntry,
       "cfprApPolicyMEpInstanceId": cfprApPolicyMEpInstanceId,
       "cfprApPolicyMEpDn": cfprApPolicyMEpDn,
       "cfprApPolicyMEpRn": cfprApPolicyMEpRn,
       "cfprApPolicyMEpSource": cfprApPolicyMEpSource,
       "cfprApPolicyMonitoringTable": cfprApPolicyMonitoringTable,
       "cfprApPolicyMonitoringEntry": cfprApPolicyMonitoringEntry,
       "cfprApPolicyMonitoringInstanceId": cfprApPolicyMonitoringInstanceId,
       "cfprApPolicyMonitoringDn": cfprApPolicyMonitoringDn,
       "cfprApPolicyMonitoringRn": cfprApPolicyMonitoringRn,
       "cfprApPolicyMonitoringSource": cfprApPolicyMonitoringSource,
       "cfprApPolicyPolicyEpTable": cfprApPolicyPolicyEpTable,
       "cfprApPolicyPolicyEpEntry": cfprApPolicyPolicyEpEntry,
       "cfprApPolicyPolicyEpInstanceId": cfprApPolicyPolicyEpInstanceId,
       "cfprApPolicyPolicyEpDn": cfprApPolicyPolicyEpDn,
       "cfprApPolicyPolicyEpRn": cfprApPolicyPolicyEpRn,
       "cfprApPolicyPolicyRequestorTable": cfprApPolicyPolicyRequestorTable,
       "cfprApPolicyPolicyRequestorEntry": cfprApPolicyPolicyRequestorEntry,
       "cfprApPolicyPolicyRequestorInstanceId": cfprApPolicyPolicyRequestorInstanceId,
       "cfprApPolicyPolicyRequestorDn": cfprApPolicyPolicyRequestorDn,
       "cfprApPolicyPolicyRequestorRn": cfprApPolicyPolicyRequestorRn,
       "cfprApPolicyPolicyRequestorName": cfprApPolicyPolicyRequestorName,
       "cfprApPolicyPolicyRequestorOnBehalfOfIdent": cfprApPolicyPolicyRequestorOnBehalfOfIdent,
       "cfprApPolicyPolicyRequestorOnBehalfOfType": cfprApPolicyPolicyRequestorOnBehalfOfType,
       "cfprApPolicyPolicyRequestorResolvedClassType": cfprApPolicyPolicyRequestorResolvedClassType,
       "cfprApPolicyPolicyScopeTable": cfprApPolicyPolicyScopeTable,
       "cfprApPolicyPolicyScopeEntry": cfprApPolicyPolicyScopeEntry,
       "cfprApPolicyPolicyScopeInstanceId": cfprApPolicyPolicyScopeInstanceId,
       "cfprApPolicyPolicyScopeDn": cfprApPolicyPolicyScopeDn,
       "cfprApPolicyPolicyScopeRn": cfprApPolicyPolicyScopeRn,
       "cfprApPolicyPolicyScopeAppType": cfprApPolicyPolicyScopeAppType,
       "cfprApPolicyPolicyScopeDefaultPolicyName": cfprApPolicyPolicyScopeDefaultPolicyName,
       "cfprApPolicyPolicyScopeFsmDescr": cfprApPolicyPolicyScopeFsmDescr,
       "cfprApPolicyPolicyScopeFsmPrev": cfprApPolicyPolicyScopeFsmPrev,
       "cfprApPolicyPolicyScopeFsmProgr": cfprApPolicyPolicyScopeFsmProgr,
       "cfprApPolicyPolicyScopeFsmRmtInvErrCode": cfprApPolicyPolicyScopeFsmRmtInvErrCode,
       "cfprApPolicyPolicyScopeFsmRmtInvErrDescr": cfprApPolicyPolicyScopeFsmRmtInvErrDescr,
       "cfprApPolicyPolicyScopeFsmRmtInvRslt": cfprApPolicyPolicyScopeFsmRmtInvRslt,
       "cfprApPolicyPolicyScopeFsmStageDescr": cfprApPolicyPolicyScopeFsmStageDescr,
       "cfprApPolicyPolicyScopeFsmStamp": cfprApPolicyPolicyScopeFsmStamp,
       "cfprApPolicyPolicyScopeFsmStatus": cfprApPolicyPolicyScopeFsmStatus,
       "cfprApPolicyPolicyScopeFsmTry": cfprApPolicyPolicyScopeFsmTry,
       "cfprApPolicyPolicyScopeOperStatus": cfprApPolicyPolicyScopeOperStatus,
       "cfprApPolicyPolicyScopeOwner": cfprApPolicyPolicyScopeOwner,
       "cfprApPolicyPolicyScopePolicyName": cfprApPolicyPolicyScopePolicyName,
       "cfprApPolicyPolicyScopePolicyType": cfprApPolicyPolicyScopePolicyType,
       "cfprApPolicyPolicyScopeRecursive": cfprApPolicyPolicyScopeRecursive,
       "cfprApPolicyPolicyScopeResolveType": cfprApPolicyPolicyScopeResolveType,
       "cfprApPolicyPolicyScopeContTable": cfprApPolicyPolicyScopeContTable,
       "cfprApPolicyPolicyScopeContEntry": cfprApPolicyPolicyScopeContEntry,
       "cfprApPolicyPolicyScopeContInstanceId": cfprApPolicyPolicyScopeContInstanceId,
       "cfprApPolicyPolicyScopeContDn": cfprApPolicyPolicyScopeContDn,
       "cfprApPolicyPolicyScopeContRn": cfprApPolicyPolicyScopeContRn,
       "cfprApPolicyPolicyScopeContAppType": cfprApPolicyPolicyScopeContAppType,
       "cfprApPolicyPolicyScopeContGenNum": cfprApPolicyPolicyScopeContGenNum,
       "cfprApPolicyPolicyScopeContNeedRecovery": cfprApPolicyPolicyScopeContNeedRecovery,
       "cfprApPolicyPolicyScopeContextTable": cfprApPolicyPolicyScopeContextTable,
       "cfprApPolicyPolicyScopeContextEntry": cfprApPolicyPolicyScopeContextEntry,
       "cfprApPolicyPolicyScopeContextInstanceId": cfprApPolicyPolicyScopeContextInstanceId,
       "cfprApPolicyPolicyScopeContextDn": cfprApPolicyPolicyScopeContextDn,
       "cfprApPolicyPolicyScopeContextRn": cfprApPolicyPolicyScopeContextRn,
       "cfprApPolicyPolicyScopeContextContext": cfprApPolicyPolicyScopeContextContext,
       "cfprApPolicyPolicyScopeContextName": cfprApPolicyPolicyScopeContextName,
       "cfprApPolicyPolicyScopeFsmTable": cfprApPolicyPolicyScopeFsmTable,
       "cfprApPolicyPolicyScopeFsmEntry": cfprApPolicyPolicyScopeFsmEntry,
       "cfprApPolicyPolicyScopeFsmInstanceId": cfprApPolicyPolicyScopeFsmInstanceId,
       "cfprApPolicyPolicyScopeFsmDn": cfprApPolicyPolicyScopeFsmDn,
       "cfprApPolicyPolicyScopeFsmRn": cfprApPolicyPolicyScopeFsmRn,
       "cfprApPolicyPolicyScopeFsmCompletionTime": cfprApPolicyPolicyScopeFsmCompletionTime,
       "cfprApPolicyPolicyScopeFsmCurrentFsm": cfprApPolicyPolicyScopeFsmCurrentFsm,
       "cfprApPolicyPolicyScopeFsmDescrData": cfprApPolicyPolicyScopeFsmDescrData,
       "cfprApPolicyPolicyScopeFsmFsmStatus": cfprApPolicyPolicyScopeFsmFsmStatus,
       "cfprApPolicyPolicyScopeFsmProgress": cfprApPolicyPolicyScopeFsmProgress,
       "cfprApPolicyPolicyScopeFsmRmtErrCode": cfprApPolicyPolicyScopeFsmRmtErrCode,
       "cfprApPolicyPolicyScopeFsmRmtErrDescr": cfprApPolicyPolicyScopeFsmRmtErrDescr,
       "cfprApPolicyPolicyScopeFsmRmtRslt": cfprApPolicyPolicyScopeFsmRmtRslt,
       "cfprApPolicyPolicyScopeFsmStageTable": cfprApPolicyPolicyScopeFsmStageTable,
       "cfprApPolicyPolicyScopeFsmStageEntry": cfprApPolicyPolicyScopeFsmStageEntry,
       "cfprApPolicyPolicyScopeFsmStageInstanceId": cfprApPolicyPolicyScopeFsmStageInstanceId,
       "cfprApPolicyPolicyScopeFsmStageDn": cfprApPolicyPolicyScopeFsmStageDn,
       "cfprApPolicyPolicyScopeFsmStageRn": cfprApPolicyPolicyScopeFsmStageRn,
       "cfprApPolicyPolicyScopeFsmStageDescrData": cfprApPolicyPolicyScopeFsmStageDescrData,
       "cfprApPolicyPolicyScopeFsmStageLastUpdateTime": cfprApPolicyPolicyScopeFsmStageLastUpdateTime,
       "cfprApPolicyPolicyScopeFsmStageName": cfprApPolicyPolicyScopeFsmStageName,
       "cfprApPolicyPolicyScopeFsmStageOrder": cfprApPolicyPolicyScopeFsmStageOrder,
       "cfprApPolicyPolicyScopeFsmStageRetry": cfprApPolicyPolicyScopeFsmStageRetry,
       "cfprApPolicyPolicyScopeFsmStageStageStatus": cfprApPolicyPolicyScopeFsmStageStageStatus,
       "cfprApPolicyPolicyScopeFsmTaskTable": cfprApPolicyPolicyScopeFsmTaskTable,
       "cfprApPolicyPolicyScopeFsmTaskEntry": cfprApPolicyPolicyScopeFsmTaskEntry,
       "cfprApPolicyPolicyScopeFsmTaskInstanceId": cfprApPolicyPolicyScopeFsmTaskInstanceId,
       "cfprApPolicyPolicyScopeFsmTaskDn": cfprApPolicyPolicyScopeFsmTaskDn,
       "cfprApPolicyPolicyScopeFsmTaskRn": cfprApPolicyPolicyScopeFsmTaskRn,
       "cfprApPolicyPolicyScopeFsmTaskCompletion": cfprApPolicyPolicyScopeFsmTaskCompletion,
       "cfprApPolicyPolicyScopeFsmTaskFlags": cfprApPolicyPolicyScopeFsmTaskFlags,
       "cfprApPolicyPolicyScopeFsmTaskItem": cfprApPolicyPolicyScopeFsmTaskItem,
       "cfprApPolicyPolicyScopeFsmTaskSeqId": cfprApPolicyPolicyScopeFsmTaskSeqId,
       "cfprApPolicyPowerMgmtTable": cfprApPolicyPowerMgmtTable,
       "cfprApPolicyPowerMgmtEntry": cfprApPolicyPowerMgmtEntry,
       "cfprApPolicyPowerMgmtInstanceId": cfprApPolicyPowerMgmtInstanceId,
       "cfprApPolicyPowerMgmtDn": cfprApPolicyPowerMgmtDn,
       "cfprApPolicyPowerMgmtRn": cfprApPolicyPowerMgmtRn,
       "cfprApPolicyPowerMgmtSource": cfprApPolicyPowerMgmtSource,
       "cfprApPolicyPsuTable": cfprApPolicyPsuTable,
       "cfprApPolicyPsuEntry": cfprApPolicyPsuEntry,
       "cfprApPolicyPsuInstanceId": cfprApPolicyPsuInstanceId,
       "cfprApPolicyPsuDn": cfprApPolicyPsuDn,
       "cfprApPolicyPsuRn": cfprApPolicyPsuRn,
       "cfprApPolicyPsuSource": cfprApPolicyPsuSource,
       "cfprApPolicyRefReqTable": cfprApPolicyRefReqTable,
       "cfprApPolicyRefReqEntry": cfprApPolicyRefReqEntry,
       "cfprApPolicyRefReqInstanceId": cfprApPolicyRefReqInstanceId,
       "cfprApPolicyRefReqDn": cfprApPolicyRefReqDn,
       "cfprApPolicyRefReqRn": cfprApPolicyRefReqRn,
       "cfprApPolicyRefReqPolicyOwner": cfprApPolicyRefReqPolicyOwner,
       "cfprApPolicyRefReqRefConvertedDn": cfprApPolicyRefReqRefConvertedDn,
       "cfprApPolicyRefReqRefPolicyDn": cfprApPolicyRefReqRefPolicyDn,
       "cfprApPolicySecurityTable": cfprApPolicySecurityTable,
       "cfprApPolicySecurityEntry": cfprApPolicySecurityEntry,
       "cfprApPolicySecurityInstanceId": cfprApPolicySecurityInstanceId,
       "cfprApPolicySecurityDn": cfprApPolicySecurityDn,
       "cfprApPolicySecurityRn": cfprApPolicySecurityRn,
       "cfprApPolicySecuritySource": cfprApPolicySecuritySource}
)
