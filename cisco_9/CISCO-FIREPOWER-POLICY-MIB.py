# SNMP MIB module (CISCO-FIREPOWER-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-POLICY-MIB.mib
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

(CfprConditionRemoteInvRslt,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprPolicyCleanupMode,
 CfprPolicyControlEpFsmCurrentFsm,
 CfprPolicyControlEpFsmStageName,
 CfprPolicyControlEpFsmTaskItem,
 CfprPolicyControlEpType,
 CfprPolicyControlSource,
 CfprPolicyControlledTypeFsmCurrentFsm,
 CfprPolicyControlledTypeFsmStageName,
 CfprPolicyControlledTypeFsmTaskItem,
 CfprPolicyIdResolvePolicyType,
 CfprPolicyPolicyOperStatus,
 CfprPolicyPolicyOwner,
 CfprPolicyPolicyResolveType,
 CfprPolicyPolicyScopeFsmCurrentFsm,
 CfprPolicyPolicyScopeFsmStageName,
 CfprPolicyPolicyScopeFsmTaskItem,
 CfprPolicyRegistrationStateType,
 CfprPolicyRepairStateType,
 CfprPolicyResumeAckState,
 CfprPolicyState,
 CfprPolicySuspendState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprPolicyCleanupMode",
    "CfprPolicyControlEpFsmCurrentFsm",
    "CfprPolicyControlEpFsmStageName",
    "CfprPolicyControlEpFsmTaskItem",
    "CfprPolicyControlEpType",
    "CfprPolicyControlSource",
    "CfprPolicyControlledTypeFsmCurrentFsm",
    "CfprPolicyControlledTypeFsmStageName",
    "CfprPolicyControlledTypeFsmTaskItem",
    "CfprPolicyIdResolvePolicyType",
    "CfprPolicyPolicyOperStatus",
    "CfprPolicyPolicyOwner",
    "CfprPolicyPolicyResolveType",
    "CfprPolicyPolicyScopeFsmCurrentFsm",
    "CfprPolicyPolicyScopeFsmStageName",
    "CfprPolicyPolicyScopeFsmTaskItem",
    "CfprPolicyRegistrationStateType",
    "CfprPolicyRepairStateType",
    "CfprPolicyResumeAckState",
    "CfprPolicyState",
    "CfprPolicySuspendState")

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

cfprPolicyObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprPolicyCentraleSyncTable_Object = MibTable
cfprPolicyCentraleSyncTable = _CfprPolicyCentraleSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 1)
)
if mibBuilder.loadTexts:
    cfprPolicyCentraleSyncTable.setStatus("current")
_CfprPolicyCentraleSyncEntry_Object = MibTableRow
cfprPolicyCentraleSyncEntry = _CfprPolicyCentraleSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 1, 1)
)
cfprPolicyCentraleSyncEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyCentraleSyncInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyCentraleSyncEntry.setStatus("current")
_CfprPolicyCentraleSyncInstanceId_Type = CfprManagedObjectId
_CfprPolicyCentraleSyncInstanceId_Object = MibTableColumn
cfprPolicyCentraleSyncInstanceId = _CfprPolicyCentraleSyncInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 1, 1, 1),
    _CfprPolicyCentraleSyncInstanceId_Type()
)
cfprPolicyCentraleSyncInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyCentraleSyncInstanceId.setStatus("current")
_CfprPolicyCentraleSyncDn_Type = CfprManagedObjectDn
_CfprPolicyCentraleSyncDn_Object = MibTableColumn
cfprPolicyCentraleSyncDn = _CfprPolicyCentraleSyncDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 1, 1, 2),
    _CfprPolicyCentraleSyncDn_Type()
)
cfprPolicyCentraleSyncDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyCentraleSyncDn.setStatus("current")
_CfprPolicyCentraleSyncRn_Type = SnmpAdminString
_CfprPolicyCentraleSyncRn_Object = MibTableColumn
cfprPolicyCentraleSyncRn = _CfprPolicyCentraleSyncRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 1, 1, 3),
    _CfprPolicyCentraleSyncRn_Type()
)
cfprPolicyCentraleSyncRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyCentraleSyncRn.setStatus("current")
_CfprPolicyCentraleSyncLeftData_Type = SnmpAdminString
_CfprPolicyCentraleSyncLeftData_Object = MibTableColumn
cfprPolicyCentraleSyncLeftData = _CfprPolicyCentraleSyncLeftData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 1, 1, 4),
    _CfprPolicyCentraleSyncLeftData_Type()
)
cfprPolicyCentraleSyncLeftData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyCentraleSyncLeftData.setStatus("current")
_CfprPolicyCentraleSyncRightData_Type = SnmpAdminString
_CfprPolicyCentraleSyncRightData_Object = MibTableColumn
cfprPolicyCentraleSyncRightData = _CfprPolicyCentraleSyncRightData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 1, 1, 5),
    _CfprPolicyCentraleSyncRightData_Type()
)
cfprPolicyCentraleSyncRightData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyCentraleSyncRightData.setStatus("current")
_CfprPolicyCommunicationTable_Object = MibTable
cfprPolicyCommunicationTable = _CfprPolicyCommunicationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 2)
)
if mibBuilder.loadTexts:
    cfprPolicyCommunicationTable.setStatus("current")
_CfprPolicyCommunicationEntry_Object = MibTableRow
cfprPolicyCommunicationEntry = _CfprPolicyCommunicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 2, 1)
)
cfprPolicyCommunicationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyCommunicationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyCommunicationEntry.setStatus("current")
_CfprPolicyCommunicationInstanceId_Type = CfprManagedObjectId
_CfprPolicyCommunicationInstanceId_Object = MibTableColumn
cfprPolicyCommunicationInstanceId = _CfprPolicyCommunicationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 2, 1, 1),
    _CfprPolicyCommunicationInstanceId_Type()
)
cfprPolicyCommunicationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyCommunicationInstanceId.setStatus("current")
_CfprPolicyCommunicationDn_Type = CfprManagedObjectDn
_CfprPolicyCommunicationDn_Object = MibTableColumn
cfprPolicyCommunicationDn = _CfprPolicyCommunicationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 2, 1, 2),
    _CfprPolicyCommunicationDn_Type()
)
cfprPolicyCommunicationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyCommunicationDn.setStatus("current")
_CfprPolicyCommunicationRn_Type = SnmpAdminString
_CfprPolicyCommunicationRn_Object = MibTableColumn
cfprPolicyCommunicationRn = _CfprPolicyCommunicationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 2, 1, 3),
    _CfprPolicyCommunicationRn_Type()
)
cfprPolicyCommunicationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyCommunicationRn.setStatus("current")
_CfprPolicyCommunicationSource_Type = CfprPolicyControlSource
_CfprPolicyCommunicationSource_Object = MibTableColumn
cfprPolicyCommunicationSource = _CfprPolicyCommunicationSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 2, 1, 4),
    _CfprPolicyCommunicationSource_Type()
)
cfprPolicyCommunicationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyCommunicationSource.setStatus("current")
_CfprPolicyConfigBackupTable_Object = MibTable
cfprPolicyConfigBackupTable = _CfprPolicyConfigBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 3)
)
if mibBuilder.loadTexts:
    cfprPolicyConfigBackupTable.setStatus("current")
_CfprPolicyConfigBackupEntry_Object = MibTableRow
cfprPolicyConfigBackupEntry = _CfprPolicyConfigBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 3, 1)
)
cfprPolicyConfigBackupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyConfigBackupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyConfigBackupEntry.setStatus("current")
_CfprPolicyConfigBackupInstanceId_Type = CfprManagedObjectId
_CfprPolicyConfigBackupInstanceId_Object = MibTableColumn
cfprPolicyConfigBackupInstanceId = _CfprPolicyConfigBackupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 3, 1, 1),
    _CfprPolicyConfigBackupInstanceId_Type()
)
cfprPolicyConfigBackupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyConfigBackupInstanceId.setStatus("current")
_CfprPolicyConfigBackupDn_Type = CfprManagedObjectDn
_CfprPolicyConfigBackupDn_Object = MibTableColumn
cfprPolicyConfigBackupDn = _CfprPolicyConfigBackupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 3, 1, 2),
    _CfprPolicyConfigBackupDn_Type()
)
cfprPolicyConfigBackupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyConfigBackupDn.setStatus("current")
_CfprPolicyConfigBackupRn_Type = SnmpAdminString
_CfprPolicyConfigBackupRn_Object = MibTableColumn
cfprPolicyConfigBackupRn = _CfprPolicyConfigBackupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 3, 1, 3),
    _CfprPolicyConfigBackupRn_Type()
)
cfprPolicyConfigBackupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyConfigBackupRn.setStatus("current")
_CfprPolicyConfigBackupSource_Type = CfprPolicyControlSource
_CfprPolicyConfigBackupSource_Object = MibTableColumn
cfprPolicyConfigBackupSource = _CfprPolicyConfigBackupSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 3, 1, 4),
    _CfprPolicyConfigBackupSource_Type()
)
cfprPolicyConfigBackupSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyConfigBackupSource.setStatus("current")
_CfprPolicyControlEpTable_Object = MibTable
cfprPolicyControlEpTable = _CfprPolicyControlEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4)
)
if mibBuilder.loadTexts:
    cfprPolicyControlEpTable.setStatus("current")
_CfprPolicyControlEpEntry_Object = MibTableRow
cfprPolicyControlEpEntry = _CfprPolicyControlEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1)
)
cfprPolicyControlEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyControlEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyControlEpEntry.setStatus("current")
_CfprPolicyControlEpInstanceId_Type = CfprManagedObjectId
_CfprPolicyControlEpInstanceId_Object = MibTableColumn
cfprPolicyControlEpInstanceId = _CfprPolicyControlEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 1),
    _CfprPolicyControlEpInstanceId_Type()
)
cfprPolicyControlEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyControlEpInstanceId.setStatus("current")
_CfprPolicyControlEpDn_Type = CfprManagedObjectDn
_CfprPolicyControlEpDn_Object = MibTableColumn
cfprPolicyControlEpDn = _CfprPolicyControlEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 2),
    _CfprPolicyControlEpDn_Type()
)
cfprPolicyControlEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpDn.setStatus("current")
_CfprPolicyControlEpRn_Type = SnmpAdminString
_CfprPolicyControlEpRn_Object = MibTableColumn
cfprPolicyControlEpRn = _CfprPolicyControlEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 3),
    _CfprPolicyControlEpRn_Type()
)
cfprPolicyControlEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpRn.setStatus("current")
_CfprPolicyControlEpAckState_Type = CfprPolicyResumeAckState
_CfprPolicyControlEpAckState_Object = MibTableColumn
cfprPolicyControlEpAckState = _CfprPolicyControlEpAckState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 4),
    _CfprPolicyControlEpAckState_Type()
)
cfprPolicyControlEpAckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpAckState.setStatus("current")
_CfprPolicyControlEpCleanupMode_Type = CfprPolicyCleanupMode
_CfprPolicyControlEpCleanupMode_Object = MibTableColumn
cfprPolicyControlEpCleanupMode = _CfprPolicyControlEpCleanupMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 5),
    _CfprPolicyControlEpCleanupMode_Type()
)
cfprPolicyControlEpCleanupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpCleanupMode.setStatus("current")
_CfprPolicyControlEpEncSecret_Type = SnmpAdminString
_CfprPolicyControlEpEncSecret_Object = MibTableColumn
cfprPolicyControlEpEncSecret = _CfprPolicyControlEpEncSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 6),
    _CfprPolicyControlEpEncSecret_Type()
)
cfprPolicyControlEpEncSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpEncSecret.setStatus("current")
_CfprPolicyControlEpFsmDescr_Type = SnmpAdminString
_CfprPolicyControlEpFsmDescr_Object = MibTableColumn
cfprPolicyControlEpFsmDescr = _CfprPolicyControlEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 7),
    _CfprPolicyControlEpFsmDescr_Type()
)
cfprPolicyControlEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmDescr.setStatus("current")
_CfprPolicyControlEpFsmPrev_Type = SnmpAdminString
_CfprPolicyControlEpFsmPrev_Object = MibTableColumn
cfprPolicyControlEpFsmPrev = _CfprPolicyControlEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 8),
    _CfprPolicyControlEpFsmPrev_Type()
)
cfprPolicyControlEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmPrev.setStatus("current")
_CfprPolicyControlEpFsmProgr_Type = Gauge32
_CfprPolicyControlEpFsmProgr_Object = MibTableColumn
cfprPolicyControlEpFsmProgr = _CfprPolicyControlEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 9),
    _CfprPolicyControlEpFsmProgr_Type()
)
cfprPolicyControlEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmProgr.setStatus("current")
_CfprPolicyControlEpFsmRmtInvErrCode_Type = Gauge32
_CfprPolicyControlEpFsmRmtInvErrCode_Object = MibTableColumn
cfprPolicyControlEpFsmRmtInvErrCode = _CfprPolicyControlEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 10),
    _CfprPolicyControlEpFsmRmtInvErrCode_Type()
)
cfprPolicyControlEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmRmtInvErrCode.setStatus("current")
_CfprPolicyControlEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprPolicyControlEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprPolicyControlEpFsmRmtInvErrDescr = _CfprPolicyControlEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 11),
    _CfprPolicyControlEpFsmRmtInvErrDescr_Type()
)
cfprPolicyControlEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmRmtInvErrDescr.setStatus("current")
_CfprPolicyControlEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprPolicyControlEpFsmRmtInvRslt_Object = MibTableColumn
cfprPolicyControlEpFsmRmtInvRslt = _CfprPolicyControlEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 12),
    _CfprPolicyControlEpFsmRmtInvRslt_Type()
)
cfprPolicyControlEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmRmtInvRslt.setStatus("current")
_CfprPolicyControlEpFsmStageDescr_Type = SnmpAdminString
_CfprPolicyControlEpFsmStageDescr_Object = MibTableColumn
cfprPolicyControlEpFsmStageDescr = _CfprPolicyControlEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 13),
    _CfprPolicyControlEpFsmStageDescr_Type()
)
cfprPolicyControlEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStageDescr.setStatus("current")
_CfprPolicyControlEpFsmStamp_Type = DateAndTime
_CfprPolicyControlEpFsmStamp_Object = MibTableColumn
cfprPolicyControlEpFsmStamp = _CfprPolicyControlEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 14),
    _CfprPolicyControlEpFsmStamp_Type()
)
cfprPolicyControlEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStamp.setStatus("current")
_CfprPolicyControlEpFsmStatus_Type = SnmpAdminString
_CfprPolicyControlEpFsmStatus_Object = MibTableColumn
cfprPolicyControlEpFsmStatus = _CfprPolicyControlEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 15),
    _CfprPolicyControlEpFsmStatus_Type()
)
cfprPolicyControlEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStatus.setStatus("current")
_CfprPolicyControlEpFsmTry_Type = Gauge32
_CfprPolicyControlEpFsmTry_Object = MibTableColumn
cfprPolicyControlEpFsmTry = _CfprPolicyControlEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 16),
    _CfprPolicyControlEpFsmTry_Type()
)
cfprPolicyControlEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmTry.setStatus("current")
_CfprPolicyControlEpName_Type = SnmpAdminString
_CfprPolicyControlEpName_Object = MibTableColumn
cfprPolicyControlEpName = _CfprPolicyControlEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 17),
    _CfprPolicyControlEpName_Type()
)
cfprPolicyControlEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpName.setStatus("current")
_CfprPolicyControlEpRegistrationState_Type = CfprPolicyRegistrationStateType
_CfprPolicyControlEpRegistrationState_Object = MibTableColumn
cfprPolicyControlEpRegistrationState = _CfprPolicyControlEpRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 18),
    _CfprPolicyControlEpRegistrationState_Type()
)
cfprPolicyControlEpRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpRegistrationState.setStatus("current")
_CfprPolicyControlEpRepairState_Type = CfprPolicyRepairStateType
_CfprPolicyControlEpRepairState_Object = MibTableColumn
cfprPolicyControlEpRepairState = _CfprPolicyControlEpRepairState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 19),
    _CfprPolicyControlEpRepairState_Type()
)
cfprPolicyControlEpRepairState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpRepairState.setStatus("current")
_CfprPolicyControlEpSecret_Type = SnmpAdminString
_CfprPolicyControlEpSecret_Object = MibTableColumn
cfprPolicyControlEpSecret = _CfprPolicyControlEpSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 20),
    _CfprPolicyControlEpSecret_Type()
)
cfprPolicyControlEpSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpSecret.setStatus("current")
_CfprPolicyControlEpState_Type = CfprPolicyState
_CfprPolicyControlEpState_Object = MibTableColumn
cfprPolicyControlEpState = _CfprPolicyControlEpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 21),
    _CfprPolicyControlEpState_Type()
)
cfprPolicyControlEpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpState.setStatus("current")
_CfprPolicyControlEpSuspendState_Type = CfprPolicySuspendState
_CfprPolicyControlEpSuspendState_Object = MibTableColumn
cfprPolicyControlEpSuspendState = _CfprPolicyControlEpSuspendState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 22),
    _CfprPolicyControlEpSuspendState_Type()
)
cfprPolicyControlEpSuspendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpSuspendState.setStatus("current")
_CfprPolicyControlEpSvcRegIP_Type = InetAddressIPv4
_CfprPolicyControlEpSvcRegIP_Object = MibTableColumn
cfprPolicyControlEpSvcRegIP = _CfprPolicyControlEpSvcRegIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 23),
    _CfprPolicyControlEpSvcRegIP_Type()
)
cfprPolicyControlEpSvcRegIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpSvcRegIP.setStatus("current")
_CfprPolicyControlEpSvcRegName_Type = SnmpAdminString
_CfprPolicyControlEpSvcRegName_Object = MibTableColumn
cfprPolicyControlEpSvcRegName = _CfprPolicyControlEpSvcRegName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 24),
    _CfprPolicyControlEpSvcRegName_Type()
)
cfprPolicyControlEpSvcRegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpSvcRegName.setStatus("current")
_CfprPolicyControlEpType_Type = CfprPolicyControlEpType
_CfprPolicyControlEpType_Object = MibTableColumn
cfprPolicyControlEpType = _CfprPolicyControlEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 4, 1, 25),
    _CfprPolicyControlEpType_Type()
)
cfprPolicyControlEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpType.setStatus("current")
_CfprPolicyControlEpFsmTable_Object = MibTable
cfprPolicyControlEpFsmTable = _CfprPolicyControlEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5)
)
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmTable.setStatus("current")
_CfprPolicyControlEpFsmEntry_Object = MibTableRow
cfprPolicyControlEpFsmEntry = _CfprPolicyControlEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5, 1)
)
cfprPolicyControlEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyControlEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmEntry.setStatus("current")
_CfprPolicyControlEpFsmInstanceId_Type = CfprManagedObjectId
_CfprPolicyControlEpFsmInstanceId_Object = MibTableColumn
cfprPolicyControlEpFsmInstanceId = _CfprPolicyControlEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5, 1, 1),
    _CfprPolicyControlEpFsmInstanceId_Type()
)
cfprPolicyControlEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmInstanceId.setStatus("current")
_CfprPolicyControlEpFsmDn_Type = CfprManagedObjectDn
_CfprPolicyControlEpFsmDn_Object = MibTableColumn
cfprPolicyControlEpFsmDn = _CfprPolicyControlEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5, 1, 2),
    _CfprPolicyControlEpFsmDn_Type()
)
cfprPolicyControlEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmDn.setStatus("current")
_CfprPolicyControlEpFsmRn_Type = SnmpAdminString
_CfprPolicyControlEpFsmRn_Object = MibTableColumn
cfprPolicyControlEpFsmRn = _CfprPolicyControlEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5, 1, 3),
    _CfprPolicyControlEpFsmRn_Type()
)
cfprPolicyControlEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmRn.setStatus("current")
_CfprPolicyControlEpFsmCompletionTime_Type = DateAndTime
_CfprPolicyControlEpFsmCompletionTime_Object = MibTableColumn
cfprPolicyControlEpFsmCompletionTime = _CfprPolicyControlEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5, 1, 4),
    _CfprPolicyControlEpFsmCompletionTime_Type()
)
cfprPolicyControlEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmCompletionTime.setStatus("current")
_CfprPolicyControlEpFsmCurrentFsm_Type = CfprPolicyControlEpFsmCurrentFsm
_CfprPolicyControlEpFsmCurrentFsm_Object = MibTableColumn
cfprPolicyControlEpFsmCurrentFsm = _CfprPolicyControlEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5, 1, 5),
    _CfprPolicyControlEpFsmCurrentFsm_Type()
)
cfprPolicyControlEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmCurrentFsm.setStatus("current")
_CfprPolicyControlEpFsmDescrData_Type = SnmpAdminString
_CfprPolicyControlEpFsmDescrData_Object = MibTableColumn
cfprPolicyControlEpFsmDescrData = _CfprPolicyControlEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5, 1, 6),
    _CfprPolicyControlEpFsmDescrData_Type()
)
cfprPolicyControlEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmDescrData.setStatus("current")
_CfprPolicyControlEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprPolicyControlEpFsmFsmStatus_Object = MibTableColumn
cfprPolicyControlEpFsmFsmStatus = _CfprPolicyControlEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5, 1, 7),
    _CfprPolicyControlEpFsmFsmStatus_Type()
)
cfprPolicyControlEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmFsmStatus.setStatus("current")
_CfprPolicyControlEpFsmProgress_Type = Gauge32
_CfprPolicyControlEpFsmProgress_Object = MibTableColumn
cfprPolicyControlEpFsmProgress = _CfprPolicyControlEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5, 1, 8),
    _CfprPolicyControlEpFsmProgress_Type()
)
cfprPolicyControlEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmProgress.setStatus("current")
_CfprPolicyControlEpFsmRmtErrCode_Type = Gauge32
_CfprPolicyControlEpFsmRmtErrCode_Object = MibTableColumn
cfprPolicyControlEpFsmRmtErrCode = _CfprPolicyControlEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5, 1, 9),
    _CfprPolicyControlEpFsmRmtErrCode_Type()
)
cfprPolicyControlEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmRmtErrCode.setStatus("current")
_CfprPolicyControlEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprPolicyControlEpFsmRmtErrDescr_Object = MibTableColumn
cfprPolicyControlEpFsmRmtErrDescr = _CfprPolicyControlEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5, 1, 10),
    _CfprPolicyControlEpFsmRmtErrDescr_Type()
)
cfprPolicyControlEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmRmtErrDescr.setStatus("current")
_CfprPolicyControlEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprPolicyControlEpFsmRmtRslt_Object = MibTableColumn
cfprPolicyControlEpFsmRmtRslt = _CfprPolicyControlEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 5, 1, 11),
    _CfprPolicyControlEpFsmRmtRslt_Type()
)
cfprPolicyControlEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmRmtRslt.setStatus("current")
_CfprPolicyControlEpFsmStageTable_Object = MibTable
cfprPolicyControlEpFsmStageTable = _CfprPolicyControlEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 6)
)
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStageTable.setStatus("current")
_CfprPolicyControlEpFsmStageEntry_Object = MibTableRow
cfprPolicyControlEpFsmStageEntry = _CfprPolicyControlEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 6, 1)
)
cfprPolicyControlEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyControlEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStageEntry.setStatus("current")
_CfprPolicyControlEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprPolicyControlEpFsmStageInstanceId_Object = MibTableColumn
cfprPolicyControlEpFsmStageInstanceId = _CfprPolicyControlEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 6, 1, 1),
    _CfprPolicyControlEpFsmStageInstanceId_Type()
)
cfprPolicyControlEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStageInstanceId.setStatus("current")
_CfprPolicyControlEpFsmStageDn_Type = CfprManagedObjectDn
_CfprPolicyControlEpFsmStageDn_Object = MibTableColumn
cfprPolicyControlEpFsmStageDn = _CfprPolicyControlEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 6, 1, 2),
    _CfprPolicyControlEpFsmStageDn_Type()
)
cfprPolicyControlEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStageDn.setStatus("current")
_CfprPolicyControlEpFsmStageRn_Type = SnmpAdminString
_CfprPolicyControlEpFsmStageRn_Object = MibTableColumn
cfprPolicyControlEpFsmStageRn = _CfprPolicyControlEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 6, 1, 3),
    _CfprPolicyControlEpFsmStageRn_Type()
)
cfprPolicyControlEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStageRn.setStatus("current")
_CfprPolicyControlEpFsmStageDescrData_Type = SnmpAdminString
_CfprPolicyControlEpFsmStageDescrData_Object = MibTableColumn
cfprPolicyControlEpFsmStageDescrData = _CfprPolicyControlEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 6, 1, 4),
    _CfprPolicyControlEpFsmStageDescrData_Type()
)
cfprPolicyControlEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStageDescrData.setStatus("current")
_CfprPolicyControlEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprPolicyControlEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprPolicyControlEpFsmStageLastUpdateTime = _CfprPolicyControlEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 6, 1, 5),
    _CfprPolicyControlEpFsmStageLastUpdateTime_Type()
)
cfprPolicyControlEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStageLastUpdateTime.setStatus("current")
_CfprPolicyControlEpFsmStageName_Type = CfprPolicyControlEpFsmStageName
_CfprPolicyControlEpFsmStageName_Object = MibTableColumn
cfprPolicyControlEpFsmStageName = _CfprPolicyControlEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 6, 1, 6),
    _CfprPolicyControlEpFsmStageName_Type()
)
cfprPolicyControlEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStageName.setStatus("current")
_CfprPolicyControlEpFsmStageOrder_Type = Gauge32
_CfprPolicyControlEpFsmStageOrder_Object = MibTableColumn
cfprPolicyControlEpFsmStageOrder = _CfprPolicyControlEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 6, 1, 7),
    _CfprPolicyControlEpFsmStageOrder_Type()
)
cfprPolicyControlEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStageOrder.setStatus("current")
_CfprPolicyControlEpFsmStageRetry_Type = Gauge32
_CfprPolicyControlEpFsmStageRetry_Object = MibTableColumn
cfprPolicyControlEpFsmStageRetry = _CfprPolicyControlEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 6, 1, 8),
    _CfprPolicyControlEpFsmStageRetry_Type()
)
cfprPolicyControlEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStageRetry.setStatus("current")
_CfprPolicyControlEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprPolicyControlEpFsmStageStageStatus_Object = MibTableColumn
cfprPolicyControlEpFsmStageStageStatus = _CfprPolicyControlEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 6, 1, 9),
    _CfprPolicyControlEpFsmStageStageStatus_Type()
)
cfprPolicyControlEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmStageStageStatus.setStatus("current")
_CfprPolicyControlEpFsmTaskTable_Object = MibTable
cfprPolicyControlEpFsmTaskTable = _CfprPolicyControlEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 7)
)
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmTaskTable.setStatus("current")
_CfprPolicyControlEpFsmTaskEntry_Object = MibTableRow
cfprPolicyControlEpFsmTaskEntry = _CfprPolicyControlEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 7, 1)
)
cfprPolicyControlEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyControlEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmTaskEntry.setStatus("current")
_CfprPolicyControlEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprPolicyControlEpFsmTaskInstanceId_Object = MibTableColumn
cfprPolicyControlEpFsmTaskInstanceId = _CfprPolicyControlEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 7, 1, 1),
    _CfprPolicyControlEpFsmTaskInstanceId_Type()
)
cfprPolicyControlEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmTaskInstanceId.setStatus("current")
_CfprPolicyControlEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprPolicyControlEpFsmTaskDn_Object = MibTableColumn
cfprPolicyControlEpFsmTaskDn = _CfprPolicyControlEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 7, 1, 2),
    _CfprPolicyControlEpFsmTaskDn_Type()
)
cfprPolicyControlEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmTaskDn.setStatus("current")
_CfprPolicyControlEpFsmTaskRn_Type = SnmpAdminString
_CfprPolicyControlEpFsmTaskRn_Object = MibTableColumn
cfprPolicyControlEpFsmTaskRn = _CfprPolicyControlEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 7, 1, 3),
    _CfprPolicyControlEpFsmTaskRn_Type()
)
cfprPolicyControlEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmTaskRn.setStatus("current")
_CfprPolicyControlEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprPolicyControlEpFsmTaskCompletion_Object = MibTableColumn
cfprPolicyControlEpFsmTaskCompletion = _CfprPolicyControlEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 7, 1, 4),
    _CfprPolicyControlEpFsmTaskCompletion_Type()
)
cfprPolicyControlEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmTaskCompletion.setStatus("current")
_CfprPolicyControlEpFsmTaskFlags_Type = CfprFsmFlags
_CfprPolicyControlEpFsmTaskFlags_Object = MibTableColumn
cfprPolicyControlEpFsmTaskFlags = _CfprPolicyControlEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 7, 1, 5),
    _CfprPolicyControlEpFsmTaskFlags_Type()
)
cfprPolicyControlEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmTaskFlags.setStatus("current")
_CfprPolicyControlEpFsmTaskItem_Type = CfprPolicyControlEpFsmTaskItem
_CfprPolicyControlEpFsmTaskItem_Object = MibTableColumn
cfprPolicyControlEpFsmTaskItem = _CfprPolicyControlEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 7, 1, 6),
    _CfprPolicyControlEpFsmTaskItem_Type()
)
cfprPolicyControlEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmTaskItem.setStatus("current")
_CfprPolicyControlEpFsmTaskSeqId_Type = Gauge32
_CfprPolicyControlEpFsmTaskSeqId_Object = MibTableColumn
cfprPolicyControlEpFsmTaskSeqId = _CfprPolicyControlEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 7, 1, 7),
    _CfprPolicyControlEpFsmTaskSeqId_Type()
)
cfprPolicyControlEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlEpFsmTaskSeqId.setStatus("current")
_CfprPolicyControlledInstanceTable_Object = MibTable
cfprPolicyControlledInstanceTable = _CfprPolicyControlledInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 8)
)
if mibBuilder.loadTexts:
    cfprPolicyControlledInstanceTable.setStatus("current")
_CfprPolicyControlledInstanceEntry_Object = MibTableRow
cfprPolicyControlledInstanceEntry = _CfprPolicyControlledInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 8, 1)
)
cfprPolicyControlledInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyControlledInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyControlledInstanceEntry.setStatus("current")
_CfprPolicyControlledInstanceInstanceId_Type = CfprManagedObjectId
_CfprPolicyControlledInstanceInstanceId_Object = MibTableColumn
cfprPolicyControlledInstanceInstanceId = _CfprPolicyControlledInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 8, 1, 1),
    _CfprPolicyControlledInstanceInstanceId_Type()
)
cfprPolicyControlledInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyControlledInstanceInstanceId.setStatus("current")
_CfprPolicyControlledInstanceDn_Type = CfprManagedObjectDn
_CfprPolicyControlledInstanceDn_Object = MibTableColumn
cfprPolicyControlledInstanceDn = _CfprPolicyControlledInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 8, 1, 2),
    _CfprPolicyControlledInstanceDn_Type()
)
cfprPolicyControlledInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledInstanceDn.setStatus("current")
_CfprPolicyControlledInstanceRn_Type = SnmpAdminString
_CfprPolicyControlledInstanceRn_Object = MibTableColumn
cfprPolicyControlledInstanceRn = _CfprPolicyControlledInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 8, 1, 3),
    _CfprPolicyControlledInstanceRn_Type()
)
cfprPolicyControlledInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledInstanceRn.setStatus("current")
_CfprPolicyControlledInstanceDefDn_Type = SnmpAdminString
_CfprPolicyControlledInstanceDefDn_Object = MibTableColumn
cfprPolicyControlledInstanceDefDn = _CfprPolicyControlledInstanceDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 8, 1, 4),
    _CfprPolicyControlledInstanceDefDn_Type()
)
cfprPolicyControlledInstanceDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledInstanceDefDn.setStatus("current")
_CfprPolicyControlledInstanceExternalResolveName_Type = SnmpAdminString
_CfprPolicyControlledInstanceExternalResolveName_Object = MibTableColumn
cfprPolicyControlledInstanceExternalResolveName = _CfprPolicyControlledInstanceExternalResolveName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 8, 1, 5),
    _CfprPolicyControlledInstanceExternalResolveName_Type()
)
cfprPolicyControlledInstanceExternalResolveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledInstanceExternalResolveName.setStatus("current")
_CfprPolicyControlledInstanceName_Type = SnmpAdminString
_CfprPolicyControlledInstanceName_Object = MibTableColumn
cfprPolicyControlledInstanceName = _CfprPolicyControlledInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 8, 1, 6),
    _CfprPolicyControlledInstanceName_Type()
)
cfprPolicyControlledInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledInstanceName.setStatus("current")
_CfprPolicyControlledInstanceResolveType_Type = CfprPolicyPolicyResolveType
_CfprPolicyControlledInstanceResolveType_Object = MibTableColumn
cfprPolicyControlledInstanceResolveType = _CfprPolicyControlledInstanceResolveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 8, 1, 7),
    _CfprPolicyControlledInstanceResolveType_Type()
)
cfprPolicyControlledInstanceResolveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledInstanceResolveType.setStatus("current")
_CfprPolicyControlledInstanceType_Type = SnmpAdminString
_CfprPolicyControlledInstanceType_Object = MibTableColumn
cfprPolicyControlledInstanceType = _CfprPolicyControlledInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 8, 1, 8),
    _CfprPolicyControlledInstanceType_Type()
)
cfprPolicyControlledInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledInstanceType.setStatus("current")
_CfprPolicyControlledTypeTable_Object = MibTable
cfprPolicyControlledTypeTable = _CfprPolicyControlledTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9)
)
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeTable.setStatus("current")
_CfprPolicyControlledTypeEntry_Object = MibTableRow
cfprPolicyControlledTypeEntry = _CfprPolicyControlledTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1)
)
cfprPolicyControlledTypeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyControlledTypeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeEntry.setStatus("current")
_CfprPolicyControlledTypeInstanceId_Type = CfprManagedObjectId
_CfprPolicyControlledTypeInstanceId_Object = MibTableColumn
cfprPolicyControlledTypeInstanceId = _CfprPolicyControlledTypeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 1),
    _CfprPolicyControlledTypeInstanceId_Type()
)
cfprPolicyControlledTypeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeInstanceId.setStatus("current")
_CfprPolicyControlledTypeDn_Type = CfprManagedObjectDn
_CfprPolicyControlledTypeDn_Object = MibTableColumn
cfprPolicyControlledTypeDn = _CfprPolicyControlledTypeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 2),
    _CfprPolicyControlledTypeDn_Type()
)
cfprPolicyControlledTypeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeDn.setStatus("current")
_CfprPolicyControlledTypeRn_Type = SnmpAdminString
_CfprPolicyControlledTypeRn_Object = MibTableColumn
cfprPolicyControlledTypeRn = _CfprPolicyControlledTypeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 3),
    _CfprPolicyControlledTypeRn_Type()
)
cfprPolicyControlledTypeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeRn.setStatus("current")
_CfprPolicyControlledTypeFsmDescr_Type = SnmpAdminString
_CfprPolicyControlledTypeFsmDescr_Object = MibTableColumn
cfprPolicyControlledTypeFsmDescr = _CfprPolicyControlledTypeFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 4),
    _CfprPolicyControlledTypeFsmDescr_Type()
)
cfprPolicyControlledTypeFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmDescr.setStatus("current")
_CfprPolicyControlledTypeFsmPrev_Type = SnmpAdminString
_CfprPolicyControlledTypeFsmPrev_Object = MibTableColumn
cfprPolicyControlledTypeFsmPrev = _CfprPolicyControlledTypeFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 5),
    _CfprPolicyControlledTypeFsmPrev_Type()
)
cfprPolicyControlledTypeFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmPrev.setStatus("current")
_CfprPolicyControlledTypeFsmProgr_Type = Gauge32
_CfprPolicyControlledTypeFsmProgr_Object = MibTableColumn
cfprPolicyControlledTypeFsmProgr = _CfprPolicyControlledTypeFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 6),
    _CfprPolicyControlledTypeFsmProgr_Type()
)
cfprPolicyControlledTypeFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmProgr.setStatus("current")
_CfprPolicyControlledTypeFsmRmtInvErrCode_Type = Gauge32
_CfprPolicyControlledTypeFsmRmtInvErrCode_Object = MibTableColumn
cfprPolicyControlledTypeFsmRmtInvErrCode = _CfprPolicyControlledTypeFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 7),
    _CfprPolicyControlledTypeFsmRmtInvErrCode_Type()
)
cfprPolicyControlledTypeFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmRmtInvErrCode.setStatus("current")
_CfprPolicyControlledTypeFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprPolicyControlledTypeFsmRmtInvErrDescr_Object = MibTableColumn
cfprPolicyControlledTypeFsmRmtInvErrDescr = _CfprPolicyControlledTypeFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 8),
    _CfprPolicyControlledTypeFsmRmtInvErrDescr_Type()
)
cfprPolicyControlledTypeFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmRmtInvErrDescr.setStatus("current")
_CfprPolicyControlledTypeFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprPolicyControlledTypeFsmRmtInvRslt_Object = MibTableColumn
cfprPolicyControlledTypeFsmRmtInvRslt = _CfprPolicyControlledTypeFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 9),
    _CfprPolicyControlledTypeFsmRmtInvRslt_Type()
)
cfprPolicyControlledTypeFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmRmtInvRslt.setStatus("current")
_CfprPolicyControlledTypeFsmStageDescr_Type = SnmpAdminString
_CfprPolicyControlledTypeFsmStageDescr_Object = MibTableColumn
cfprPolicyControlledTypeFsmStageDescr = _CfprPolicyControlledTypeFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 10),
    _CfprPolicyControlledTypeFsmStageDescr_Type()
)
cfprPolicyControlledTypeFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStageDescr.setStatus("current")
_CfprPolicyControlledTypeFsmStamp_Type = DateAndTime
_CfprPolicyControlledTypeFsmStamp_Object = MibTableColumn
cfprPolicyControlledTypeFsmStamp = _CfprPolicyControlledTypeFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 11),
    _CfprPolicyControlledTypeFsmStamp_Type()
)
cfprPolicyControlledTypeFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStamp.setStatus("current")
_CfprPolicyControlledTypeFsmStatus_Type = SnmpAdminString
_CfprPolicyControlledTypeFsmStatus_Object = MibTableColumn
cfprPolicyControlledTypeFsmStatus = _CfprPolicyControlledTypeFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 12),
    _CfprPolicyControlledTypeFsmStatus_Type()
)
cfprPolicyControlledTypeFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStatus.setStatus("current")
_CfprPolicyControlledTypeFsmTry_Type = Gauge32
_CfprPolicyControlledTypeFsmTry_Object = MibTableColumn
cfprPolicyControlledTypeFsmTry = _CfprPolicyControlledTypeFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 13),
    _CfprPolicyControlledTypeFsmTry_Type()
)
cfprPolicyControlledTypeFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmTry.setStatus("current")
_CfprPolicyControlledTypeParentContext_Type = SnmpAdminString
_CfprPolicyControlledTypeParentContext_Object = MibTableColumn
cfprPolicyControlledTypeParentContext = _CfprPolicyControlledTypeParentContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 14),
    _CfprPolicyControlledTypeParentContext_Type()
)
cfprPolicyControlledTypeParentContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeParentContext.setStatus("current")
_CfprPolicyControlledTypeType_Type = SnmpAdminString
_CfprPolicyControlledTypeType_Object = MibTableColumn
cfprPolicyControlledTypeType = _CfprPolicyControlledTypeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 9, 1, 15),
    _CfprPolicyControlledTypeType_Type()
)
cfprPolicyControlledTypeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeType.setStatus("current")
_CfprPolicyControlledTypeFsmTable_Object = MibTable
cfprPolicyControlledTypeFsmTable = _CfprPolicyControlledTypeFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10)
)
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmTable.setStatus("current")
_CfprPolicyControlledTypeFsmEntry_Object = MibTableRow
cfprPolicyControlledTypeFsmEntry = _CfprPolicyControlledTypeFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10, 1)
)
cfprPolicyControlledTypeFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyControlledTypeFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmEntry.setStatus("current")
_CfprPolicyControlledTypeFsmInstanceId_Type = CfprManagedObjectId
_CfprPolicyControlledTypeFsmInstanceId_Object = MibTableColumn
cfprPolicyControlledTypeFsmInstanceId = _CfprPolicyControlledTypeFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10, 1, 1),
    _CfprPolicyControlledTypeFsmInstanceId_Type()
)
cfprPolicyControlledTypeFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmInstanceId.setStatus("current")
_CfprPolicyControlledTypeFsmDn_Type = CfprManagedObjectDn
_CfprPolicyControlledTypeFsmDn_Object = MibTableColumn
cfprPolicyControlledTypeFsmDn = _CfprPolicyControlledTypeFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10, 1, 2),
    _CfprPolicyControlledTypeFsmDn_Type()
)
cfprPolicyControlledTypeFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmDn.setStatus("current")
_CfprPolicyControlledTypeFsmRn_Type = SnmpAdminString
_CfprPolicyControlledTypeFsmRn_Object = MibTableColumn
cfprPolicyControlledTypeFsmRn = _CfprPolicyControlledTypeFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10, 1, 3),
    _CfprPolicyControlledTypeFsmRn_Type()
)
cfprPolicyControlledTypeFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmRn.setStatus("current")
_CfprPolicyControlledTypeFsmCompletionTime_Type = DateAndTime
_CfprPolicyControlledTypeFsmCompletionTime_Object = MibTableColumn
cfprPolicyControlledTypeFsmCompletionTime = _CfprPolicyControlledTypeFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10, 1, 4),
    _CfprPolicyControlledTypeFsmCompletionTime_Type()
)
cfprPolicyControlledTypeFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmCompletionTime.setStatus("current")
_CfprPolicyControlledTypeFsmCurrentFsm_Type = CfprPolicyControlledTypeFsmCurrentFsm
_CfprPolicyControlledTypeFsmCurrentFsm_Object = MibTableColumn
cfprPolicyControlledTypeFsmCurrentFsm = _CfprPolicyControlledTypeFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10, 1, 5),
    _CfprPolicyControlledTypeFsmCurrentFsm_Type()
)
cfprPolicyControlledTypeFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmCurrentFsm.setStatus("current")
_CfprPolicyControlledTypeFsmDescrData_Type = SnmpAdminString
_CfprPolicyControlledTypeFsmDescrData_Object = MibTableColumn
cfprPolicyControlledTypeFsmDescrData = _CfprPolicyControlledTypeFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10, 1, 6),
    _CfprPolicyControlledTypeFsmDescrData_Type()
)
cfprPolicyControlledTypeFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmDescrData.setStatus("current")
_CfprPolicyControlledTypeFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprPolicyControlledTypeFsmFsmStatus_Object = MibTableColumn
cfprPolicyControlledTypeFsmFsmStatus = _CfprPolicyControlledTypeFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10, 1, 7),
    _CfprPolicyControlledTypeFsmFsmStatus_Type()
)
cfprPolicyControlledTypeFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmFsmStatus.setStatus("current")
_CfprPolicyControlledTypeFsmProgress_Type = Gauge32
_CfprPolicyControlledTypeFsmProgress_Object = MibTableColumn
cfprPolicyControlledTypeFsmProgress = _CfprPolicyControlledTypeFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10, 1, 8),
    _CfprPolicyControlledTypeFsmProgress_Type()
)
cfprPolicyControlledTypeFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmProgress.setStatus("current")
_CfprPolicyControlledTypeFsmRmtErrCode_Type = Gauge32
_CfprPolicyControlledTypeFsmRmtErrCode_Object = MibTableColumn
cfprPolicyControlledTypeFsmRmtErrCode = _CfprPolicyControlledTypeFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10, 1, 9),
    _CfprPolicyControlledTypeFsmRmtErrCode_Type()
)
cfprPolicyControlledTypeFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmRmtErrCode.setStatus("current")
_CfprPolicyControlledTypeFsmRmtErrDescr_Type = SnmpAdminString
_CfprPolicyControlledTypeFsmRmtErrDescr_Object = MibTableColumn
cfprPolicyControlledTypeFsmRmtErrDescr = _CfprPolicyControlledTypeFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10, 1, 10),
    _CfprPolicyControlledTypeFsmRmtErrDescr_Type()
)
cfprPolicyControlledTypeFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmRmtErrDescr.setStatus("current")
_CfprPolicyControlledTypeFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprPolicyControlledTypeFsmRmtRslt_Object = MibTableColumn
cfprPolicyControlledTypeFsmRmtRslt = _CfprPolicyControlledTypeFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 10, 1, 11),
    _CfprPolicyControlledTypeFsmRmtRslt_Type()
)
cfprPolicyControlledTypeFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmRmtRslt.setStatus("current")
_CfprPolicyControlledTypeFsmStageTable_Object = MibTable
cfprPolicyControlledTypeFsmStageTable = _CfprPolicyControlledTypeFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 11)
)
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStageTable.setStatus("current")
_CfprPolicyControlledTypeFsmStageEntry_Object = MibTableRow
cfprPolicyControlledTypeFsmStageEntry = _CfprPolicyControlledTypeFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 11, 1)
)
cfprPolicyControlledTypeFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyControlledTypeFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStageEntry.setStatus("current")
_CfprPolicyControlledTypeFsmStageInstanceId_Type = CfprManagedObjectId
_CfprPolicyControlledTypeFsmStageInstanceId_Object = MibTableColumn
cfprPolicyControlledTypeFsmStageInstanceId = _CfprPolicyControlledTypeFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 11, 1, 1),
    _CfprPolicyControlledTypeFsmStageInstanceId_Type()
)
cfprPolicyControlledTypeFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStageInstanceId.setStatus("current")
_CfprPolicyControlledTypeFsmStageDn_Type = CfprManagedObjectDn
_CfprPolicyControlledTypeFsmStageDn_Object = MibTableColumn
cfprPolicyControlledTypeFsmStageDn = _CfprPolicyControlledTypeFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 11, 1, 2),
    _CfprPolicyControlledTypeFsmStageDn_Type()
)
cfprPolicyControlledTypeFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStageDn.setStatus("current")
_CfprPolicyControlledTypeFsmStageRn_Type = SnmpAdminString
_CfprPolicyControlledTypeFsmStageRn_Object = MibTableColumn
cfprPolicyControlledTypeFsmStageRn = _CfprPolicyControlledTypeFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 11, 1, 3),
    _CfprPolicyControlledTypeFsmStageRn_Type()
)
cfprPolicyControlledTypeFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStageRn.setStatus("current")
_CfprPolicyControlledTypeFsmStageDescrData_Type = SnmpAdminString
_CfprPolicyControlledTypeFsmStageDescrData_Object = MibTableColumn
cfprPolicyControlledTypeFsmStageDescrData = _CfprPolicyControlledTypeFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 11, 1, 4),
    _CfprPolicyControlledTypeFsmStageDescrData_Type()
)
cfprPolicyControlledTypeFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStageDescrData.setStatus("current")
_CfprPolicyControlledTypeFsmStageLastUpdateTime_Type = DateAndTime
_CfprPolicyControlledTypeFsmStageLastUpdateTime_Object = MibTableColumn
cfprPolicyControlledTypeFsmStageLastUpdateTime = _CfprPolicyControlledTypeFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 11, 1, 5),
    _CfprPolicyControlledTypeFsmStageLastUpdateTime_Type()
)
cfprPolicyControlledTypeFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStageLastUpdateTime.setStatus("current")
_CfprPolicyControlledTypeFsmStageName_Type = CfprPolicyControlledTypeFsmStageName
_CfprPolicyControlledTypeFsmStageName_Object = MibTableColumn
cfprPolicyControlledTypeFsmStageName = _CfprPolicyControlledTypeFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 11, 1, 6),
    _CfprPolicyControlledTypeFsmStageName_Type()
)
cfprPolicyControlledTypeFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStageName.setStatus("current")
_CfprPolicyControlledTypeFsmStageOrder_Type = Gauge32
_CfprPolicyControlledTypeFsmStageOrder_Object = MibTableColumn
cfprPolicyControlledTypeFsmStageOrder = _CfprPolicyControlledTypeFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 11, 1, 7),
    _CfprPolicyControlledTypeFsmStageOrder_Type()
)
cfprPolicyControlledTypeFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStageOrder.setStatus("current")
_CfprPolicyControlledTypeFsmStageRetry_Type = Gauge32
_CfprPolicyControlledTypeFsmStageRetry_Object = MibTableColumn
cfprPolicyControlledTypeFsmStageRetry = _CfprPolicyControlledTypeFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 11, 1, 8),
    _CfprPolicyControlledTypeFsmStageRetry_Type()
)
cfprPolicyControlledTypeFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStageRetry.setStatus("current")
_CfprPolicyControlledTypeFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprPolicyControlledTypeFsmStageStageStatus_Object = MibTableColumn
cfprPolicyControlledTypeFsmStageStageStatus = _CfprPolicyControlledTypeFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 11, 1, 9),
    _CfprPolicyControlledTypeFsmStageStageStatus_Type()
)
cfprPolicyControlledTypeFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmStageStageStatus.setStatus("current")
_CfprPolicyControlledTypeFsmTaskTable_Object = MibTable
cfprPolicyControlledTypeFsmTaskTable = _CfprPolicyControlledTypeFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 12)
)
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmTaskTable.setStatus("current")
_CfprPolicyControlledTypeFsmTaskEntry_Object = MibTableRow
cfprPolicyControlledTypeFsmTaskEntry = _CfprPolicyControlledTypeFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 12, 1)
)
cfprPolicyControlledTypeFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyControlledTypeFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmTaskEntry.setStatus("current")
_CfprPolicyControlledTypeFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprPolicyControlledTypeFsmTaskInstanceId_Object = MibTableColumn
cfprPolicyControlledTypeFsmTaskInstanceId = _CfprPolicyControlledTypeFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 12, 1, 1),
    _CfprPolicyControlledTypeFsmTaskInstanceId_Type()
)
cfprPolicyControlledTypeFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmTaskInstanceId.setStatus("current")
_CfprPolicyControlledTypeFsmTaskDn_Type = CfprManagedObjectDn
_CfprPolicyControlledTypeFsmTaskDn_Object = MibTableColumn
cfprPolicyControlledTypeFsmTaskDn = _CfprPolicyControlledTypeFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 12, 1, 2),
    _CfprPolicyControlledTypeFsmTaskDn_Type()
)
cfprPolicyControlledTypeFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmTaskDn.setStatus("current")
_CfprPolicyControlledTypeFsmTaskRn_Type = SnmpAdminString
_CfprPolicyControlledTypeFsmTaskRn_Object = MibTableColumn
cfprPolicyControlledTypeFsmTaskRn = _CfprPolicyControlledTypeFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 12, 1, 3),
    _CfprPolicyControlledTypeFsmTaskRn_Type()
)
cfprPolicyControlledTypeFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmTaskRn.setStatus("current")
_CfprPolicyControlledTypeFsmTaskCompletion_Type = CfprFsmCompletion
_CfprPolicyControlledTypeFsmTaskCompletion_Object = MibTableColumn
cfprPolicyControlledTypeFsmTaskCompletion = _CfprPolicyControlledTypeFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 12, 1, 4),
    _CfprPolicyControlledTypeFsmTaskCompletion_Type()
)
cfprPolicyControlledTypeFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmTaskCompletion.setStatus("current")
_CfprPolicyControlledTypeFsmTaskFlags_Type = CfprFsmFlags
_CfprPolicyControlledTypeFsmTaskFlags_Object = MibTableColumn
cfprPolicyControlledTypeFsmTaskFlags = _CfprPolicyControlledTypeFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 12, 1, 5),
    _CfprPolicyControlledTypeFsmTaskFlags_Type()
)
cfprPolicyControlledTypeFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmTaskFlags.setStatus("current")
_CfprPolicyControlledTypeFsmTaskItem_Type = CfprPolicyControlledTypeFsmTaskItem
_CfprPolicyControlledTypeFsmTaskItem_Object = MibTableColumn
cfprPolicyControlledTypeFsmTaskItem = _CfprPolicyControlledTypeFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 12, 1, 6),
    _CfprPolicyControlledTypeFsmTaskItem_Type()
)
cfprPolicyControlledTypeFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmTaskItem.setStatus("current")
_CfprPolicyControlledTypeFsmTaskSeqId_Type = Gauge32
_CfprPolicyControlledTypeFsmTaskSeqId_Object = MibTableColumn
cfprPolicyControlledTypeFsmTaskSeqId = _CfprPolicyControlledTypeFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 12, 1, 7),
    _CfprPolicyControlledTypeFsmTaskSeqId_Type()
)
cfprPolicyControlledTypeFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyControlledTypeFsmTaskSeqId.setStatus("current")
_CfprPolicyDateTimeTable_Object = MibTable
cfprPolicyDateTimeTable = _CfprPolicyDateTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 13)
)
if mibBuilder.loadTexts:
    cfprPolicyDateTimeTable.setStatus("current")
_CfprPolicyDateTimeEntry_Object = MibTableRow
cfprPolicyDateTimeEntry = _CfprPolicyDateTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 13, 1)
)
cfprPolicyDateTimeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyDateTimeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyDateTimeEntry.setStatus("current")
_CfprPolicyDateTimeInstanceId_Type = CfprManagedObjectId
_CfprPolicyDateTimeInstanceId_Object = MibTableColumn
cfprPolicyDateTimeInstanceId = _CfprPolicyDateTimeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 13, 1, 1),
    _CfprPolicyDateTimeInstanceId_Type()
)
cfprPolicyDateTimeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyDateTimeInstanceId.setStatus("current")
_CfprPolicyDateTimeDn_Type = CfprManagedObjectDn
_CfprPolicyDateTimeDn_Object = MibTableColumn
cfprPolicyDateTimeDn = _CfprPolicyDateTimeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 13, 1, 2),
    _CfprPolicyDateTimeDn_Type()
)
cfprPolicyDateTimeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDateTimeDn.setStatus("current")
_CfprPolicyDateTimeRn_Type = SnmpAdminString
_CfprPolicyDateTimeRn_Object = MibTableColumn
cfprPolicyDateTimeRn = _CfprPolicyDateTimeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 13, 1, 3),
    _CfprPolicyDateTimeRn_Type()
)
cfprPolicyDateTimeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDateTimeRn.setStatus("current")
_CfprPolicyDateTimeSource_Type = CfprPolicyControlSource
_CfprPolicyDateTimeSource_Object = MibTableColumn
cfprPolicyDateTimeSource = _CfprPolicyDateTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 13, 1, 4),
    _CfprPolicyDateTimeSource_Type()
)
cfprPolicyDateTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDateTimeSource.setStatus("current")
_CfprPolicyDigestTable_Object = MibTable
cfprPolicyDigestTable = _CfprPolicyDigestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14)
)
if mibBuilder.loadTexts:
    cfprPolicyDigestTable.setStatus("current")
_CfprPolicyDigestEntry_Object = MibTableRow
cfprPolicyDigestEntry = _CfprPolicyDigestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1)
)
cfprPolicyDigestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyDigestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyDigestEntry.setStatus("current")
_CfprPolicyDigestInstanceId_Type = CfprManagedObjectId
_CfprPolicyDigestInstanceId_Object = MibTableColumn
cfprPolicyDigestInstanceId = _CfprPolicyDigestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 1),
    _CfprPolicyDigestInstanceId_Type()
)
cfprPolicyDigestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyDigestInstanceId.setStatus("current")
_CfprPolicyDigestDn_Type = CfprManagedObjectDn
_CfprPolicyDigestDn_Object = MibTableColumn
cfprPolicyDigestDn = _CfprPolicyDigestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 2),
    _CfprPolicyDigestDn_Type()
)
cfprPolicyDigestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDigestDn.setStatus("current")
_CfprPolicyDigestRn_Type = SnmpAdminString
_CfprPolicyDigestRn_Object = MibTableColumn
cfprPolicyDigestRn = _CfprPolicyDigestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 3),
    _CfprPolicyDigestRn_Type()
)
cfprPolicyDigestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDigestRn.setStatus("current")
_CfprPolicyDigestContext_Type = SnmpAdminString
_CfprPolicyDigestContext_Object = MibTableColumn
cfprPolicyDigestContext = _CfprPolicyDigestContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 4),
    _CfprPolicyDigestContext_Type()
)
cfprPolicyDigestContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDigestContext.setStatus("current")
_CfprPolicyDigestDescr_Type = SnmpAdminString
_CfprPolicyDigestDescr_Object = MibTableColumn
cfprPolicyDigestDescr = _CfprPolicyDigestDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 5),
    _CfprPolicyDigestDescr_Type()
)
cfprPolicyDigestDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDigestDescr.setStatus("current")
_CfprPolicyDigestLabel_Type = SnmpAdminString
_CfprPolicyDigestLabel_Object = MibTableColumn
cfprPolicyDigestLabel = _CfprPolicyDigestLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 6),
    _CfprPolicyDigestLabel_Type()
)
cfprPolicyDigestLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDigestLabel.setStatus("current")
_CfprPolicyDigestName_Type = SnmpAdminString
_CfprPolicyDigestName_Object = MibTableColumn
cfprPolicyDigestName = _CfprPolicyDigestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 7),
    _CfprPolicyDigestName_Type()
)
cfprPolicyDigestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDigestName.setStatus("current")
_CfprPolicyDigestOnBehalfOfIdent_Type = SnmpAdminString
_CfprPolicyDigestOnBehalfOfIdent_Object = MibTableColumn
cfprPolicyDigestOnBehalfOfIdent = _CfprPolicyDigestOnBehalfOfIdent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 8),
    _CfprPolicyDigestOnBehalfOfIdent_Type()
)
cfprPolicyDigestOnBehalfOfIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDigestOnBehalfOfIdent.setStatus("current")
_CfprPolicyDigestOnBehalfOfType_Type = SnmpAdminString
_CfprPolicyDigestOnBehalfOfType_Object = MibTableColumn
cfprPolicyDigestOnBehalfOfType = _CfprPolicyDigestOnBehalfOfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 9),
    _CfprPolicyDigestOnBehalfOfType_Type()
)
cfprPolicyDigestOnBehalfOfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDigestOnBehalfOfType.setStatus("current")
_CfprPolicyDigestRequestorOwnership_Type = CfprPolicyPolicyOwner
_CfprPolicyDigestRequestorOwnership_Object = MibTableColumn
cfprPolicyDigestRequestorOwnership = _CfprPolicyDigestRequestorOwnership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 10),
    _CfprPolicyDigestRequestorOwnership_Type()
)
cfprPolicyDigestRequestorOwnership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDigestRequestorOwnership.setStatus("current")
_CfprPolicyDigestResolveType_Type = CfprPolicyPolicyResolveType
_CfprPolicyDigestResolveType_Object = MibTableColumn
cfprPolicyDigestResolveType = _CfprPolicyDigestResolveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 11),
    _CfprPolicyDigestResolveType_Type()
)
cfprPolicyDigestResolveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDigestResolveType.setStatus("current")
_CfprPolicyDigestType_Type = SnmpAdminString
_CfprPolicyDigestType_Object = MibTableColumn
cfprPolicyDigestType = _CfprPolicyDigestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 12),
    _CfprPolicyDigestType_Type()
)
cfprPolicyDigestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDigestType.setStatus("current")
_CfprPolicyDigestUsage_Type = SnmpAdminString
_CfprPolicyDigestUsage_Object = MibTableColumn
cfprPolicyDigestUsage = _CfprPolicyDigestUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 14, 1, 13),
    _CfprPolicyDigestUsage_Type()
)
cfprPolicyDigestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDigestUsage.setStatus("current")
_CfprPolicyDiscoveryTable_Object = MibTable
cfprPolicyDiscoveryTable = _CfprPolicyDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 15)
)
if mibBuilder.loadTexts:
    cfprPolicyDiscoveryTable.setStatus("current")
_CfprPolicyDiscoveryEntry_Object = MibTableRow
cfprPolicyDiscoveryEntry = _CfprPolicyDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 15, 1)
)
cfprPolicyDiscoveryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyDiscoveryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyDiscoveryEntry.setStatus("current")
_CfprPolicyDiscoveryInstanceId_Type = CfprManagedObjectId
_CfprPolicyDiscoveryInstanceId_Object = MibTableColumn
cfprPolicyDiscoveryInstanceId = _CfprPolicyDiscoveryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 15, 1, 1),
    _CfprPolicyDiscoveryInstanceId_Type()
)
cfprPolicyDiscoveryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyDiscoveryInstanceId.setStatus("current")
_CfprPolicyDiscoveryDn_Type = CfprManagedObjectDn
_CfprPolicyDiscoveryDn_Object = MibTableColumn
cfprPolicyDiscoveryDn = _CfprPolicyDiscoveryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 15, 1, 2),
    _CfprPolicyDiscoveryDn_Type()
)
cfprPolicyDiscoveryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDiscoveryDn.setStatus("current")
_CfprPolicyDiscoveryRn_Type = SnmpAdminString
_CfprPolicyDiscoveryRn_Object = MibTableColumn
cfprPolicyDiscoveryRn = _CfprPolicyDiscoveryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 15, 1, 3),
    _CfprPolicyDiscoveryRn_Type()
)
cfprPolicyDiscoveryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDiscoveryRn.setStatus("current")
_CfprPolicyDiscoverySource_Type = CfprPolicyControlSource
_CfprPolicyDiscoverySource_Object = MibTableColumn
cfprPolicyDiscoverySource = _CfprPolicyDiscoverySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 15, 1, 4),
    _CfprPolicyDiscoverySource_Type()
)
cfprPolicyDiscoverySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDiscoverySource.setStatus("current")
_CfprPolicyDnsTable_Object = MibTable
cfprPolicyDnsTable = _CfprPolicyDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 16)
)
if mibBuilder.loadTexts:
    cfprPolicyDnsTable.setStatus("current")
_CfprPolicyDnsEntry_Object = MibTableRow
cfprPolicyDnsEntry = _CfprPolicyDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 16, 1)
)
cfprPolicyDnsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyDnsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyDnsEntry.setStatus("current")
_CfprPolicyDnsInstanceId_Type = CfprManagedObjectId
_CfprPolicyDnsInstanceId_Object = MibTableColumn
cfprPolicyDnsInstanceId = _CfprPolicyDnsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 16, 1, 1),
    _CfprPolicyDnsInstanceId_Type()
)
cfprPolicyDnsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyDnsInstanceId.setStatus("current")
_CfprPolicyDnsDn_Type = CfprManagedObjectDn
_CfprPolicyDnsDn_Object = MibTableColumn
cfprPolicyDnsDn = _CfprPolicyDnsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 16, 1, 2),
    _CfprPolicyDnsDn_Type()
)
cfprPolicyDnsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDnsDn.setStatus("current")
_CfprPolicyDnsRn_Type = SnmpAdminString
_CfprPolicyDnsRn_Object = MibTableColumn
cfprPolicyDnsRn = _CfprPolicyDnsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 16, 1, 3),
    _CfprPolicyDnsRn_Type()
)
cfprPolicyDnsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDnsRn.setStatus("current")
_CfprPolicyDnsSource_Type = CfprPolicyControlSource
_CfprPolicyDnsSource_Object = MibTableColumn
cfprPolicyDnsSource = _CfprPolicyDnsSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 16, 1, 4),
    _CfprPolicyDnsSource_Type()
)
cfprPolicyDnsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyDnsSource.setStatus("current")
_CfprPolicyElementTable_Object = MibTable
cfprPolicyElementTable = _CfprPolicyElementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 17)
)
if mibBuilder.loadTexts:
    cfprPolicyElementTable.setStatus("current")
_CfprPolicyElementEntry_Object = MibTableRow
cfprPolicyElementEntry = _CfprPolicyElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 17, 1)
)
cfprPolicyElementEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyElementInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyElementEntry.setStatus("current")
_CfprPolicyElementInstanceId_Type = CfprManagedObjectId
_CfprPolicyElementInstanceId_Object = MibTableColumn
cfprPolicyElementInstanceId = _CfprPolicyElementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 17, 1, 1),
    _CfprPolicyElementInstanceId_Type()
)
cfprPolicyElementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyElementInstanceId.setStatus("current")
_CfprPolicyElementDn_Type = CfprManagedObjectDn
_CfprPolicyElementDn_Object = MibTableColumn
cfprPolicyElementDn = _CfprPolicyElementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 17, 1, 2),
    _CfprPolicyElementDn_Type()
)
cfprPolicyElementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyElementDn.setStatus("current")
_CfprPolicyElementRn_Type = SnmpAdminString
_CfprPolicyElementRn_Object = MibTableColumn
cfprPolicyElementRn = _CfprPolicyElementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 17, 1, 3),
    _CfprPolicyElementRn_Type()
)
cfprPolicyElementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyElementRn.setStatus("current")
_CfprPolicyElementClassType_Type = SnmpAdminString
_CfprPolicyElementClassType_Object = MibTableColumn
cfprPolicyElementClassType = _CfprPolicyElementClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 17, 1, 4),
    _CfprPolicyElementClassType_Type()
)
cfprPolicyElementClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyElementClassType.setStatus("current")
_CfprPolicyElementConvertedDn_Type = SnmpAdminString
_CfprPolicyElementConvertedDn_Object = MibTableColumn
cfprPolicyElementConvertedDn = _CfprPolicyElementConvertedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 17, 1, 5),
    _CfprPolicyElementConvertedDn_Type()
)
cfprPolicyElementConvertedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyElementConvertedDn.setStatus("current")
_CfprPolicyElementOwnership_Type = CfprPolicyPolicyOwner
_CfprPolicyElementOwnership_Object = MibTableColumn
cfprPolicyElementOwnership = _CfprPolicyElementOwnership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 17, 1, 6),
    _CfprPolicyElementOwnership_Type()
)
cfprPolicyElementOwnership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyElementOwnership.setStatus("current")
_CfprPolicyElementPolicyDn_Type = SnmpAdminString
_CfprPolicyElementPolicyDn_Object = MibTableColumn
cfprPolicyElementPolicyDn = _CfprPolicyElementPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 17, 1, 7),
    _CfprPolicyElementPolicyDn_Type()
)
cfprPolicyElementPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyElementPolicyDn.setStatus("current")
_CfprPolicyFaultTable_Object = MibTable
cfprPolicyFaultTable = _CfprPolicyFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 18)
)
if mibBuilder.loadTexts:
    cfprPolicyFaultTable.setStatus("current")
_CfprPolicyFaultEntry_Object = MibTableRow
cfprPolicyFaultEntry = _CfprPolicyFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 18, 1)
)
cfprPolicyFaultEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyFaultInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyFaultEntry.setStatus("current")
_CfprPolicyFaultInstanceId_Type = CfprManagedObjectId
_CfprPolicyFaultInstanceId_Object = MibTableColumn
cfprPolicyFaultInstanceId = _CfprPolicyFaultInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 18, 1, 1),
    _CfprPolicyFaultInstanceId_Type()
)
cfprPolicyFaultInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyFaultInstanceId.setStatus("current")
_CfprPolicyFaultDn_Type = CfprManagedObjectDn
_CfprPolicyFaultDn_Object = MibTableColumn
cfprPolicyFaultDn = _CfprPolicyFaultDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 18, 1, 2),
    _CfprPolicyFaultDn_Type()
)
cfprPolicyFaultDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyFaultDn.setStatus("current")
_CfprPolicyFaultRn_Type = SnmpAdminString
_CfprPolicyFaultRn_Object = MibTableColumn
cfprPolicyFaultRn = _CfprPolicyFaultRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 18, 1, 3),
    _CfprPolicyFaultRn_Type()
)
cfprPolicyFaultRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyFaultRn.setStatus("current")
_CfprPolicyFaultSource_Type = CfprPolicyControlSource
_CfprPolicyFaultSource_Object = MibTableColumn
cfprPolicyFaultSource = _CfprPolicyFaultSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 18, 1, 4),
    _CfprPolicyFaultSource_Type()
)
cfprPolicyFaultSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyFaultSource.setStatus("current")
_CfprPolicyIdResolvePolicyTable_Object = MibTable
cfprPolicyIdResolvePolicyTable = _CfprPolicyIdResolvePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 19)
)
if mibBuilder.loadTexts:
    cfprPolicyIdResolvePolicyTable.setStatus("current")
_CfprPolicyIdResolvePolicyEntry_Object = MibTableRow
cfprPolicyIdResolvePolicyEntry = _CfprPolicyIdResolvePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 19, 1)
)
cfprPolicyIdResolvePolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyIdResolvePolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyIdResolvePolicyEntry.setStatus("current")
_CfprPolicyIdResolvePolicyInstanceId_Type = CfprManagedObjectId
_CfprPolicyIdResolvePolicyInstanceId_Object = MibTableColumn
cfprPolicyIdResolvePolicyInstanceId = _CfprPolicyIdResolvePolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 19, 1, 1),
    _CfprPolicyIdResolvePolicyInstanceId_Type()
)
cfprPolicyIdResolvePolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyIdResolvePolicyInstanceId.setStatus("current")
_CfprPolicyIdResolvePolicyDn_Type = CfprManagedObjectDn
_CfprPolicyIdResolvePolicyDn_Object = MibTableColumn
cfprPolicyIdResolvePolicyDn = _CfprPolicyIdResolvePolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 19, 1, 2),
    _CfprPolicyIdResolvePolicyDn_Type()
)
cfprPolicyIdResolvePolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyIdResolvePolicyDn.setStatus("current")
_CfprPolicyIdResolvePolicyRn_Type = SnmpAdminString
_CfprPolicyIdResolvePolicyRn_Object = MibTableColumn
cfprPolicyIdResolvePolicyRn = _CfprPolicyIdResolvePolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 19, 1, 3),
    _CfprPolicyIdResolvePolicyRn_Type()
)
cfprPolicyIdResolvePolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyIdResolvePolicyRn.setStatus("current")
_CfprPolicyIdResolvePolicyIdAssignmentMode_Type = CfprPolicyIdResolvePolicyType
_CfprPolicyIdResolvePolicyIdAssignmentMode_Object = MibTableColumn
cfprPolicyIdResolvePolicyIdAssignmentMode = _CfprPolicyIdResolvePolicyIdAssignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 19, 1, 4),
    _CfprPolicyIdResolvePolicyIdAssignmentMode_Type()
)
cfprPolicyIdResolvePolicyIdAssignmentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyIdResolvePolicyIdAssignmentMode.setStatus("current")
_CfprPolicyInfraFirmwareTable_Object = MibTable
cfprPolicyInfraFirmwareTable = _CfprPolicyInfraFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 20)
)
if mibBuilder.loadTexts:
    cfprPolicyInfraFirmwareTable.setStatus("current")
_CfprPolicyInfraFirmwareEntry_Object = MibTableRow
cfprPolicyInfraFirmwareEntry = _CfprPolicyInfraFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 20, 1)
)
cfprPolicyInfraFirmwareEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyInfraFirmwareInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyInfraFirmwareEntry.setStatus("current")
_CfprPolicyInfraFirmwareInstanceId_Type = CfprManagedObjectId
_CfprPolicyInfraFirmwareInstanceId_Object = MibTableColumn
cfprPolicyInfraFirmwareInstanceId = _CfprPolicyInfraFirmwareInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 20, 1, 1),
    _CfprPolicyInfraFirmwareInstanceId_Type()
)
cfprPolicyInfraFirmwareInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyInfraFirmwareInstanceId.setStatus("current")
_CfprPolicyInfraFirmwareDn_Type = CfprManagedObjectDn
_CfprPolicyInfraFirmwareDn_Object = MibTableColumn
cfprPolicyInfraFirmwareDn = _CfprPolicyInfraFirmwareDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 20, 1, 2),
    _CfprPolicyInfraFirmwareDn_Type()
)
cfprPolicyInfraFirmwareDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyInfraFirmwareDn.setStatus("current")
_CfprPolicyInfraFirmwareRn_Type = SnmpAdminString
_CfprPolicyInfraFirmwareRn_Object = MibTableColumn
cfprPolicyInfraFirmwareRn = _CfprPolicyInfraFirmwareRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 20, 1, 3),
    _CfprPolicyInfraFirmwareRn_Type()
)
cfprPolicyInfraFirmwareRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyInfraFirmwareRn.setStatus("current")
_CfprPolicyInfraFirmwareSource_Type = CfprPolicyControlSource
_CfprPolicyInfraFirmwareSource_Object = MibTableColumn
cfprPolicyInfraFirmwareSource = _CfprPolicyInfraFirmwareSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 20, 1, 4),
    _CfprPolicyInfraFirmwareSource_Type()
)
cfprPolicyInfraFirmwareSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyInfraFirmwareSource.setStatus("current")
_CfprPolicyLocalMapTable_Object = MibTable
cfprPolicyLocalMapTable = _CfprPolicyLocalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 21)
)
if mibBuilder.loadTexts:
    cfprPolicyLocalMapTable.setStatus("current")
_CfprPolicyLocalMapEntry_Object = MibTableRow
cfprPolicyLocalMapEntry = _CfprPolicyLocalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 21, 1)
)
cfprPolicyLocalMapEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyLocalMapInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyLocalMapEntry.setStatus("current")
_CfprPolicyLocalMapInstanceId_Type = CfprManagedObjectId
_CfprPolicyLocalMapInstanceId_Object = MibTableColumn
cfprPolicyLocalMapInstanceId = _CfprPolicyLocalMapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 21, 1, 1),
    _CfprPolicyLocalMapInstanceId_Type()
)
cfprPolicyLocalMapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyLocalMapInstanceId.setStatus("current")
_CfprPolicyLocalMapDn_Type = CfprManagedObjectDn
_CfprPolicyLocalMapDn_Object = MibTableColumn
cfprPolicyLocalMapDn = _CfprPolicyLocalMapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 21, 1, 2),
    _CfprPolicyLocalMapDn_Type()
)
cfprPolicyLocalMapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyLocalMapDn.setStatus("current")
_CfprPolicyLocalMapRn_Type = SnmpAdminString
_CfprPolicyLocalMapRn_Object = MibTableColumn
cfprPolicyLocalMapRn = _CfprPolicyLocalMapRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 21, 1, 3),
    _CfprPolicyLocalMapRn_Type()
)
cfprPolicyLocalMapRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyLocalMapRn.setStatus("current")
_CfprPolicyMEpTable_Object = MibTable
cfprPolicyMEpTable = _CfprPolicyMEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 22)
)
if mibBuilder.loadTexts:
    cfprPolicyMEpTable.setStatus("current")
_CfprPolicyMEpEntry_Object = MibTableRow
cfprPolicyMEpEntry = _CfprPolicyMEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 22, 1)
)
cfprPolicyMEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyMEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyMEpEntry.setStatus("current")
_CfprPolicyMEpInstanceId_Type = CfprManagedObjectId
_CfprPolicyMEpInstanceId_Object = MibTableColumn
cfprPolicyMEpInstanceId = _CfprPolicyMEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 22, 1, 1),
    _CfprPolicyMEpInstanceId_Type()
)
cfprPolicyMEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyMEpInstanceId.setStatus("current")
_CfprPolicyMEpDn_Type = CfprManagedObjectDn
_CfprPolicyMEpDn_Object = MibTableColumn
cfprPolicyMEpDn = _CfprPolicyMEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 22, 1, 2),
    _CfprPolicyMEpDn_Type()
)
cfprPolicyMEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyMEpDn.setStatus("current")
_CfprPolicyMEpRn_Type = SnmpAdminString
_CfprPolicyMEpRn_Object = MibTableColumn
cfprPolicyMEpRn = _CfprPolicyMEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 22, 1, 3),
    _CfprPolicyMEpRn_Type()
)
cfprPolicyMEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyMEpRn.setStatus("current")
_CfprPolicyMEpSource_Type = CfprPolicyControlSource
_CfprPolicyMEpSource_Object = MibTableColumn
cfprPolicyMEpSource = _CfprPolicyMEpSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 22, 1, 4),
    _CfprPolicyMEpSource_Type()
)
cfprPolicyMEpSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyMEpSource.setStatus("current")
_CfprPolicyMonitoringTable_Object = MibTable
cfprPolicyMonitoringTable = _CfprPolicyMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 23)
)
if mibBuilder.loadTexts:
    cfprPolicyMonitoringTable.setStatus("current")
_CfprPolicyMonitoringEntry_Object = MibTableRow
cfprPolicyMonitoringEntry = _CfprPolicyMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 23, 1)
)
cfprPolicyMonitoringEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyMonitoringInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyMonitoringEntry.setStatus("current")
_CfprPolicyMonitoringInstanceId_Type = CfprManagedObjectId
_CfprPolicyMonitoringInstanceId_Object = MibTableColumn
cfprPolicyMonitoringInstanceId = _CfprPolicyMonitoringInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 23, 1, 1),
    _CfprPolicyMonitoringInstanceId_Type()
)
cfprPolicyMonitoringInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyMonitoringInstanceId.setStatus("current")
_CfprPolicyMonitoringDn_Type = CfprManagedObjectDn
_CfprPolicyMonitoringDn_Object = MibTableColumn
cfprPolicyMonitoringDn = _CfprPolicyMonitoringDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 23, 1, 2),
    _CfprPolicyMonitoringDn_Type()
)
cfprPolicyMonitoringDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyMonitoringDn.setStatus("current")
_CfprPolicyMonitoringRn_Type = SnmpAdminString
_CfprPolicyMonitoringRn_Object = MibTableColumn
cfprPolicyMonitoringRn = _CfprPolicyMonitoringRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 23, 1, 3),
    _CfprPolicyMonitoringRn_Type()
)
cfprPolicyMonitoringRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyMonitoringRn.setStatus("current")
_CfprPolicyMonitoringSource_Type = CfprPolicyControlSource
_CfprPolicyMonitoringSource_Object = MibTableColumn
cfprPolicyMonitoringSource = _CfprPolicyMonitoringSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 23, 1, 4),
    _CfprPolicyMonitoringSource_Type()
)
cfprPolicyMonitoringSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyMonitoringSource.setStatus("current")
_CfprPolicyPolicyEpTable_Object = MibTable
cfprPolicyPolicyEpTable = _CfprPolicyPolicyEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 24)
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyEpTable.setStatus("current")
_CfprPolicyPolicyEpEntry_Object = MibTableRow
cfprPolicyPolicyEpEntry = _CfprPolicyPolicyEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 24, 1)
)
cfprPolicyPolicyEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyPolicyEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyEpEntry.setStatus("current")
_CfprPolicyPolicyEpInstanceId_Type = CfprManagedObjectId
_CfprPolicyPolicyEpInstanceId_Object = MibTableColumn
cfprPolicyPolicyEpInstanceId = _CfprPolicyPolicyEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 24, 1, 1),
    _CfprPolicyPolicyEpInstanceId_Type()
)
cfprPolicyPolicyEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyPolicyEpInstanceId.setStatus("current")
_CfprPolicyPolicyEpDn_Type = CfprManagedObjectDn
_CfprPolicyPolicyEpDn_Object = MibTableColumn
cfprPolicyPolicyEpDn = _CfprPolicyPolicyEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 24, 1, 2),
    _CfprPolicyPolicyEpDn_Type()
)
cfprPolicyPolicyEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyEpDn.setStatus("current")
_CfprPolicyPolicyEpRn_Type = SnmpAdminString
_CfprPolicyPolicyEpRn_Object = MibTableColumn
cfprPolicyPolicyEpRn = _CfprPolicyPolicyEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 24, 1, 3),
    _CfprPolicyPolicyEpRn_Type()
)
cfprPolicyPolicyEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyEpRn.setStatus("current")
_CfprPolicyPolicyRequestorTable_Object = MibTable
cfprPolicyPolicyRequestorTable = _CfprPolicyPolicyRequestorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 25)
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyRequestorTable.setStatus("current")
_CfprPolicyPolicyRequestorEntry_Object = MibTableRow
cfprPolicyPolicyRequestorEntry = _CfprPolicyPolicyRequestorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 25, 1)
)
cfprPolicyPolicyRequestorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyPolicyRequestorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyRequestorEntry.setStatus("current")
_CfprPolicyPolicyRequestorInstanceId_Type = CfprManagedObjectId
_CfprPolicyPolicyRequestorInstanceId_Object = MibTableColumn
cfprPolicyPolicyRequestorInstanceId = _CfprPolicyPolicyRequestorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 25, 1, 1),
    _CfprPolicyPolicyRequestorInstanceId_Type()
)
cfprPolicyPolicyRequestorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyPolicyRequestorInstanceId.setStatus("current")
_CfprPolicyPolicyRequestorDn_Type = CfprManagedObjectDn
_CfprPolicyPolicyRequestorDn_Object = MibTableColumn
cfprPolicyPolicyRequestorDn = _CfprPolicyPolicyRequestorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 25, 1, 2),
    _CfprPolicyPolicyRequestorDn_Type()
)
cfprPolicyPolicyRequestorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyRequestorDn.setStatus("current")
_CfprPolicyPolicyRequestorRn_Type = SnmpAdminString
_CfprPolicyPolicyRequestorRn_Object = MibTableColumn
cfprPolicyPolicyRequestorRn = _CfprPolicyPolicyRequestorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 25, 1, 3),
    _CfprPolicyPolicyRequestorRn_Type()
)
cfprPolicyPolicyRequestorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyRequestorRn.setStatus("current")
_CfprPolicyPolicyRequestorName_Type = SnmpAdminString
_CfprPolicyPolicyRequestorName_Object = MibTableColumn
cfprPolicyPolicyRequestorName = _CfprPolicyPolicyRequestorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 25, 1, 4),
    _CfprPolicyPolicyRequestorName_Type()
)
cfprPolicyPolicyRequestorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyRequestorName.setStatus("current")
_CfprPolicyPolicyRequestorOnBehalfOfIdent_Type = SnmpAdminString
_CfprPolicyPolicyRequestorOnBehalfOfIdent_Object = MibTableColumn
cfprPolicyPolicyRequestorOnBehalfOfIdent = _CfprPolicyPolicyRequestorOnBehalfOfIdent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 25, 1, 5),
    _CfprPolicyPolicyRequestorOnBehalfOfIdent_Type()
)
cfprPolicyPolicyRequestorOnBehalfOfIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyRequestorOnBehalfOfIdent.setStatus("current")
_CfprPolicyPolicyRequestorOnBehalfOfType_Type = SnmpAdminString
_CfprPolicyPolicyRequestorOnBehalfOfType_Object = MibTableColumn
cfprPolicyPolicyRequestorOnBehalfOfType = _CfprPolicyPolicyRequestorOnBehalfOfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 25, 1, 6),
    _CfprPolicyPolicyRequestorOnBehalfOfType_Type()
)
cfprPolicyPolicyRequestorOnBehalfOfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyRequestorOnBehalfOfType.setStatus("current")
_CfprPolicyPolicyRequestorResolvedClassType_Type = SnmpAdminString
_CfprPolicyPolicyRequestorResolvedClassType_Object = MibTableColumn
cfprPolicyPolicyRequestorResolvedClassType = _CfprPolicyPolicyRequestorResolvedClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 25, 1, 7),
    _CfprPolicyPolicyRequestorResolvedClassType_Type()
)
cfprPolicyPolicyRequestorResolvedClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyRequestorResolvedClassType.setStatus("current")
_CfprPolicyPolicyScopeTable_Object = MibTable
cfprPolicyPolicyScopeTable = _CfprPolicyPolicyScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26)
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeTable.setStatus("current")
_CfprPolicyPolicyScopeEntry_Object = MibTableRow
cfprPolicyPolicyScopeEntry = _CfprPolicyPolicyScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1)
)
cfprPolicyPolicyScopeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyPolicyScopeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeEntry.setStatus("current")
_CfprPolicyPolicyScopeInstanceId_Type = CfprManagedObjectId
_CfprPolicyPolicyScopeInstanceId_Object = MibTableColumn
cfprPolicyPolicyScopeInstanceId = _CfprPolicyPolicyScopeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 1),
    _CfprPolicyPolicyScopeInstanceId_Type()
)
cfprPolicyPolicyScopeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeInstanceId.setStatus("current")
_CfprPolicyPolicyScopeDn_Type = CfprManagedObjectDn
_CfprPolicyPolicyScopeDn_Object = MibTableColumn
cfprPolicyPolicyScopeDn = _CfprPolicyPolicyScopeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 2),
    _CfprPolicyPolicyScopeDn_Type()
)
cfprPolicyPolicyScopeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeDn.setStatus("current")
_CfprPolicyPolicyScopeRn_Type = SnmpAdminString
_CfprPolicyPolicyScopeRn_Object = MibTableColumn
cfprPolicyPolicyScopeRn = _CfprPolicyPolicyScopeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 3),
    _CfprPolicyPolicyScopeRn_Type()
)
cfprPolicyPolicyScopeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeRn.setStatus("current")
_CfprPolicyPolicyScopeAppType_Type = SnmpAdminString
_CfprPolicyPolicyScopeAppType_Object = MibTableColumn
cfprPolicyPolicyScopeAppType = _CfprPolicyPolicyScopeAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 4),
    _CfprPolicyPolicyScopeAppType_Type()
)
cfprPolicyPolicyScopeAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeAppType.setStatus("current")
_CfprPolicyPolicyScopeDefaultPolicyName_Type = SnmpAdminString
_CfprPolicyPolicyScopeDefaultPolicyName_Object = MibTableColumn
cfprPolicyPolicyScopeDefaultPolicyName = _CfprPolicyPolicyScopeDefaultPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 5),
    _CfprPolicyPolicyScopeDefaultPolicyName_Type()
)
cfprPolicyPolicyScopeDefaultPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeDefaultPolicyName.setStatus("current")
_CfprPolicyPolicyScopeFsmDescr_Type = SnmpAdminString
_CfprPolicyPolicyScopeFsmDescr_Object = MibTableColumn
cfprPolicyPolicyScopeFsmDescr = _CfprPolicyPolicyScopeFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 6),
    _CfprPolicyPolicyScopeFsmDescr_Type()
)
cfprPolicyPolicyScopeFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmDescr.setStatus("current")
_CfprPolicyPolicyScopeFsmPrev_Type = SnmpAdminString
_CfprPolicyPolicyScopeFsmPrev_Object = MibTableColumn
cfprPolicyPolicyScopeFsmPrev = _CfprPolicyPolicyScopeFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 7),
    _CfprPolicyPolicyScopeFsmPrev_Type()
)
cfprPolicyPolicyScopeFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmPrev.setStatus("current")
_CfprPolicyPolicyScopeFsmProgr_Type = Gauge32
_CfprPolicyPolicyScopeFsmProgr_Object = MibTableColumn
cfprPolicyPolicyScopeFsmProgr = _CfprPolicyPolicyScopeFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 8),
    _CfprPolicyPolicyScopeFsmProgr_Type()
)
cfprPolicyPolicyScopeFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmProgr.setStatus("current")
_CfprPolicyPolicyScopeFsmRmtInvErrCode_Type = Gauge32
_CfprPolicyPolicyScopeFsmRmtInvErrCode_Object = MibTableColumn
cfprPolicyPolicyScopeFsmRmtInvErrCode = _CfprPolicyPolicyScopeFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 9),
    _CfprPolicyPolicyScopeFsmRmtInvErrCode_Type()
)
cfprPolicyPolicyScopeFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmRmtInvErrCode.setStatus("current")
_CfprPolicyPolicyScopeFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprPolicyPolicyScopeFsmRmtInvErrDescr_Object = MibTableColumn
cfprPolicyPolicyScopeFsmRmtInvErrDescr = _CfprPolicyPolicyScopeFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 10),
    _CfprPolicyPolicyScopeFsmRmtInvErrDescr_Type()
)
cfprPolicyPolicyScopeFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmRmtInvErrDescr.setStatus("current")
_CfprPolicyPolicyScopeFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprPolicyPolicyScopeFsmRmtInvRslt_Object = MibTableColumn
cfprPolicyPolicyScopeFsmRmtInvRslt = _CfprPolicyPolicyScopeFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 11),
    _CfprPolicyPolicyScopeFsmRmtInvRslt_Type()
)
cfprPolicyPolicyScopeFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmRmtInvRslt.setStatus("current")
_CfprPolicyPolicyScopeFsmStageDescr_Type = SnmpAdminString
_CfprPolicyPolicyScopeFsmStageDescr_Object = MibTableColumn
cfprPolicyPolicyScopeFsmStageDescr = _CfprPolicyPolicyScopeFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 12),
    _CfprPolicyPolicyScopeFsmStageDescr_Type()
)
cfprPolicyPolicyScopeFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStageDescr.setStatus("current")
_CfprPolicyPolicyScopeFsmStamp_Type = DateAndTime
_CfprPolicyPolicyScopeFsmStamp_Object = MibTableColumn
cfprPolicyPolicyScopeFsmStamp = _CfprPolicyPolicyScopeFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 13),
    _CfprPolicyPolicyScopeFsmStamp_Type()
)
cfprPolicyPolicyScopeFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStamp.setStatus("current")
_CfprPolicyPolicyScopeFsmStatus_Type = SnmpAdminString
_CfprPolicyPolicyScopeFsmStatus_Object = MibTableColumn
cfprPolicyPolicyScopeFsmStatus = _CfprPolicyPolicyScopeFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 14),
    _CfprPolicyPolicyScopeFsmStatus_Type()
)
cfprPolicyPolicyScopeFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStatus.setStatus("current")
_CfprPolicyPolicyScopeFsmTry_Type = Gauge32
_CfprPolicyPolicyScopeFsmTry_Object = MibTableColumn
cfprPolicyPolicyScopeFsmTry = _CfprPolicyPolicyScopeFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 15),
    _CfprPolicyPolicyScopeFsmTry_Type()
)
cfprPolicyPolicyScopeFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmTry.setStatus("current")
_CfprPolicyPolicyScopeOperStatus_Type = CfprPolicyPolicyOperStatus
_CfprPolicyPolicyScopeOperStatus_Object = MibTableColumn
cfprPolicyPolicyScopeOperStatus = _CfprPolicyPolicyScopeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 16),
    _CfprPolicyPolicyScopeOperStatus_Type()
)
cfprPolicyPolicyScopeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeOperStatus.setStatus("current")
_CfprPolicyPolicyScopeOwner_Type = CfprPolicyPolicyOwner
_CfprPolicyPolicyScopeOwner_Object = MibTableColumn
cfprPolicyPolicyScopeOwner = _CfprPolicyPolicyScopeOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 17),
    _CfprPolicyPolicyScopeOwner_Type()
)
cfprPolicyPolicyScopeOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeOwner.setStatus("current")
_CfprPolicyPolicyScopePolicyName_Type = SnmpAdminString
_CfprPolicyPolicyScopePolicyName_Object = MibTableColumn
cfprPolicyPolicyScopePolicyName = _CfprPolicyPolicyScopePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 18),
    _CfprPolicyPolicyScopePolicyName_Type()
)
cfprPolicyPolicyScopePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopePolicyName.setStatus("current")
_CfprPolicyPolicyScopePolicyType_Type = SnmpAdminString
_CfprPolicyPolicyScopePolicyType_Object = MibTableColumn
cfprPolicyPolicyScopePolicyType = _CfprPolicyPolicyScopePolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 19),
    _CfprPolicyPolicyScopePolicyType_Type()
)
cfprPolicyPolicyScopePolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopePolicyType.setStatus("current")
_CfprPolicyPolicyScopeRecursive_Type = TruthValue
_CfprPolicyPolicyScopeRecursive_Object = MibTableColumn
cfprPolicyPolicyScopeRecursive = _CfprPolicyPolicyScopeRecursive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 20),
    _CfprPolicyPolicyScopeRecursive_Type()
)
cfprPolicyPolicyScopeRecursive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeRecursive.setStatus("current")
_CfprPolicyPolicyScopeResolveType_Type = CfprPolicyPolicyResolveType
_CfprPolicyPolicyScopeResolveType_Object = MibTableColumn
cfprPolicyPolicyScopeResolveType = _CfprPolicyPolicyScopeResolveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 26, 1, 21),
    _CfprPolicyPolicyScopeResolveType_Type()
)
cfprPolicyPolicyScopeResolveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeResolveType.setStatus("current")
_CfprPolicyPolicyScopeContTable_Object = MibTable
cfprPolicyPolicyScopeContTable = _CfprPolicyPolicyScopeContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 27)
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContTable.setStatus("current")
_CfprPolicyPolicyScopeContEntry_Object = MibTableRow
cfprPolicyPolicyScopeContEntry = _CfprPolicyPolicyScopeContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 27, 1)
)
cfprPolicyPolicyScopeContEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyPolicyScopeContInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContEntry.setStatus("current")
_CfprPolicyPolicyScopeContInstanceId_Type = CfprManagedObjectId
_CfprPolicyPolicyScopeContInstanceId_Object = MibTableColumn
cfprPolicyPolicyScopeContInstanceId = _CfprPolicyPolicyScopeContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 27, 1, 1),
    _CfprPolicyPolicyScopeContInstanceId_Type()
)
cfprPolicyPolicyScopeContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContInstanceId.setStatus("current")
_CfprPolicyPolicyScopeContDn_Type = CfprManagedObjectDn
_CfprPolicyPolicyScopeContDn_Object = MibTableColumn
cfprPolicyPolicyScopeContDn = _CfprPolicyPolicyScopeContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 27, 1, 2),
    _CfprPolicyPolicyScopeContDn_Type()
)
cfprPolicyPolicyScopeContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContDn.setStatus("current")
_CfprPolicyPolicyScopeContRn_Type = SnmpAdminString
_CfprPolicyPolicyScopeContRn_Object = MibTableColumn
cfprPolicyPolicyScopeContRn = _CfprPolicyPolicyScopeContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 27, 1, 3),
    _CfprPolicyPolicyScopeContRn_Type()
)
cfprPolicyPolicyScopeContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContRn.setStatus("current")
_CfprPolicyPolicyScopeContAppType_Type = SnmpAdminString
_CfprPolicyPolicyScopeContAppType_Object = MibTableColumn
cfprPolicyPolicyScopeContAppType = _CfprPolicyPolicyScopeContAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 27, 1, 4),
    _CfprPolicyPolicyScopeContAppType_Type()
)
cfprPolicyPolicyScopeContAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContAppType.setStatus("current")
_CfprPolicyPolicyScopeContGenNum_Type = Gauge32
_CfprPolicyPolicyScopeContGenNum_Object = MibTableColumn
cfprPolicyPolicyScopeContGenNum = _CfprPolicyPolicyScopeContGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 27, 1, 5),
    _CfprPolicyPolicyScopeContGenNum_Type()
)
cfprPolicyPolicyScopeContGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContGenNum.setStatus("current")
_CfprPolicyPolicyScopeContNeedRecovery_Type = TruthValue
_CfprPolicyPolicyScopeContNeedRecovery_Object = MibTableColumn
cfprPolicyPolicyScopeContNeedRecovery = _CfprPolicyPolicyScopeContNeedRecovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 27, 1, 6),
    _CfprPolicyPolicyScopeContNeedRecovery_Type()
)
cfprPolicyPolicyScopeContNeedRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContNeedRecovery.setStatus("current")
_CfprPolicyPolicyScopeContextTable_Object = MibTable
cfprPolicyPolicyScopeContextTable = _CfprPolicyPolicyScopeContextTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 28)
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContextTable.setStatus("current")
_CfprPolicyPolicyScopeContextEntry_Object = MibTableRow
cfprPolicyPolicyScopeContextEntry = _CfprPolicyPolicyScopeContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 28, 1)
)
cfprPolicyPolicyScopeContextEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyPolicyScopeContextInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContextEntry.setStatus("current")
_CfprPolicyPolicyScopeContextInstanceId_Type = CfprManagedObjectId
_CfprPolicyPolicyScopeContextInstanceId_Object = MibTableColumn
cfprPolicyPolicyScopeContextInstanceId = _CfprPolicyPolicyScopeContextInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 28, 1, 1),
    _CfprPolicyPolicyScopeContextInstanceId_Type()
)
cfprPolicyPolicyScopeContextInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContextInstanceId.setStatus("current")
_CfprPolicyPolicyScopeContextDn_Type = CfprManagedObjectDn
_CfprPolicyPolicyScopeContextDn_Object = MibTableColumn
cfprPolicyPolicyScopeContextDn = _CfprPolicyPolicyScopeContextDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 28, 1, 2),
    _CfprPolicyPolicyScopeContextDn_Type()
)
cfprPolicyPolicyScopeContextDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContextDn.setStatus("current")
_CfprPolicyPolicyScopeContextRn_Type = SnmpAdminString
_CfprPolicyPolicyScopeContextRn_Object = MibTableColumn
cfprPolicyPolicyScopeContextRn = _CfprPolicyPolicyScopeContextRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 28, 1, 3),
    _CfprPolicyPolicyScopeContextRn_Type()
)
cfprPolicyPolicyScopeContextRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContextRn.setStatus("current")
_CfprPolicyPolicyScopeContextContext_Type = SnmpAdminString
_CfprPolicyPolicyScopeContextContext_Object = MibTableColumn
cfprPolicyPolicyScopeContextContext = _CfprPolicyPolicyScopeContextContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 28, 1, 4),
    _CfprPolicyPolicyScopeContextContext_Type()
)
cfprPolicyPolicyScopeContextContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContextContext.setStatus("current")
_CfprPolicyPolicyScopeContextName_Type = SnmpAdminString
_CfprPolicyPolicyScopeContextName_Object = MibTableColumn
cfprPolicyPolicyScopeContextName = _CfprPolicyPolicyScopeContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 28, 1, 5),
    _CfprPolicyPolicyScopeContextName_Type()
)
cfprPolicyPolicyScopeContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeContextName.setStatus("current")
_CfprPolicyPolicyScopeFsmTable_Object = MibTable
cfprPolicyPolicyScopeFsmTable = _CfprPolicyPolicyScopeFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29)
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmTable.setStatus("current")
_CfprPolicyPolicyScopeFsmEntry_Object = MibTableRow
cfprPolicyPolicyScopeFsmEntry = _CfprPolicyPolicyScopeFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29, 1)
)
cfprPolicyPolicyScopeFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyPolicyScopeFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmEntry.setStatus("current")
_CfprPolicyPolicyScopeFsmInstanceId_Type = CfprManagedObjectId
_CfprPolicyPolicyScopeFsmInstanceId_Object = MibTableColumn
cfprPolicyPolicyScopeFsmInstanceId = _CfprPolicyPolicyScopeFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29, 1, 1),
    _CfprPolicyPolicyScopeFsmInstanceId_Type()
)
cfprPolicyPolicyScopeFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmInstanceId.setStatus("current")
_CfprPolicyPolicyScopeFsmDn_Type = CfprManagedObjectDn
_CfprPolicyPolicyScopeFsmDn_Object = MibTableColumn
cfprPolicyPolicyScopeFsmDn = _CfprPolicyPolicyScopeFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29, 1, 2),
    _CfprPolicyPolicyScopeFsmDn_Type()
)
cfprPolicyPolicyScopeFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmDn.setStatus("current")
_CfprPolicyPolicyScopeFsmRn_Type = SnmpAdminString
_CfprPolicyPolicyScopeFsmRn_Object = MibTableColumn
cfprPolicyPolicyScopeFsmRn = _CfprPolicyPolicyScopeFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29, 1, 3),
    _CfprPolicyPolicyScopeFsmRn_Type()
)
cfprPolicyPolicyScopeFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmRn.setStatus("current")
_CfprPolicyPolicyScopeFsmCompletionTime_Type = DateAndTime
_CfprPolicyPolicyScopeFsmCompletionTime_Object = MibTableColumn
cfprPolicyPolicyScopeFsmCompletionTime = _CfprPolicyPolicyScopeFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29, 1, 4),
    _CfprPolicyPolicyScopeFsmCompletionTime_Type()
)
cfprPolicyPolicyScopeFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmCompletionTime.setStatus("current")
_CfprPolicyPolicyScopeFsmCurrentFsm_Type = CfprPolicyPolicyScopeFsmCurrentFsm
_CfprPolicyPolicyScopeFsmCurrentFsm_Object = MibTableColumn
cfprPolicyPolicyScopeFsmCurrentFsm = _CfprPolicyPolicyScopeFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29, 1, 5),
    _CfprPolicyPolicyScopeFsmCurrentFsm_Type()
)
cfprPolicyPolicyScopeFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmCurrentFsm.setStatus("current")
_CfprPolicyPolicyScopeFsmDescrData_Type = SnmpAdminString
_CfprPolicyPolicyScopeFsmDescrData_Object = MibTableColumn
cfprPolicyPolicyScopeFsmDescrData = _CfprPolicyPolicyScopeFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29, 1, 6),
    _CfprPolicyPolicyScopeFsmDescrData_Type()
)
cfprPolicyPolicyScopeFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmDescrData.setStatus("current")
_CfprPolicyPolicyScopeFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprPolicyPolicyScopeFsmFsmStatus_Object = MibTableColumn
cfprPolicyPolicyScopeFsmFsmStatus = _CfprPolicyPolicyScopeFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29, 1, 7),
    _CfprPolicyPolicyScopeFsmFsmStatus_Type()
)
cfprPolicyPolicyScopeFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmFsmStatus.setStatus("current")
_CfprPolicyPolicyScopeFsmProgress_Type = Gauge32
_CfprPolicyPolicyScopeFsmProgress_Object = MibTableColumn
cfprPolicyPolicyScopeFsmProgress = _CfprPolicyPolicyScopeFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29, 1, 8),
    _CfprPolicyPolicyScopeFsmProgress_Type()
)
cfprPolicyPolicyScopeFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmProgress.setStatus("current")
_CfprPolicyPolicyScopeFsmRmtErrCode_Type = Gauge32
_CfprPolicyPolicyScopeFsmRmtErrCode_Object = MibTableColumn
cfprPolicyPolicyScopeFsmRmtErrCode = _CfprPolicyPolicyScopeFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29, 1, 9),
    _CfprPolicyPolicyScopeFsmRmtErrCode_Type()
)
cfprPolicyPolicyScopeFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmRmtErrCode.setStatus("current")
_CfprPolicyPolicyScopeFsmRmtErrDescr_Type = SnmpAdminString
_CfprPolicyPolicyScopeFsmRmtErrDescr_Object = MibTableColumn
cfprPolicyPolicyScopeFsmRmtErrDescr = _CfprPolicyPolicyScopeFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29, 1, 10),
    _CfprPolicyPolicyScopeFsmRmtErrDescr_Type()
)
cfprPolicyPolicyScopeFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmRmtErrDescr.setStatus("current")
_CfprPolicyPolicyScopeFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprPolicyPolicyScopeFsmRmtRslt_Object = MibTableColumn
cfprPolicyPolicyScopeFsmRmtRslt = _CfprPolicyPolicyScopeFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 29, 1, 11),
    _CfprPolicyPolicyScopeFsmRmtRslt_Type()
)
cfprPolicyPolicyScopeFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmRmtRslt.setStatus("current")
_CfprPolicyPolicyScopeFsmStageTable_Object = MibTable
cfprPolicyPolicyScopeFsmStageTable = _CfprPolicyPolicyScopeFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 30)
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStageTable.setStatus("current")
_CfprPolicyPolicyScopeFsmStageEntry_Object = MibTableRow
cfprPolicyPolicyScopeFsmStageEntry = _CfprPolicyPolicyScopeFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 30, 1)
)
cfprPolicyPolicyScopeFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyPolicyScopeFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStageEntry.setStatus("current")
_CfprPolicyPolicyScopeFsmStageInstanceId_Type = CfprManagedObjectId
_CfprPolicyPolicyScopeFsmStageInstanceId_Object = MibTableColumn
cfprPolicyPolicyScopeFsmStageInstanceId = _CfprPolicyPolicyScopeFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 30, 1, 1),
    _CfprPolicyPolicyScopeFsmStageInstanceId_Type()
)
cfprPolicyPolicyScopeFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStageInstanceId.setStatus("current")
_CfprPolicyPolicyScopeFsmStageDn_Type = CfprManagedObjectDn
_CfprPolicyPolicyScopeFsmStageDn_Object = MibTableColumn
cfprPolicyPolicyScopeFsmStageDn = _CfprPolicyPolicyScopeFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 30, 1, 2),
    _CfprPolicyPolicyScopeFsmStageDn_Type()
)
cfprPolicyPolicyScopeFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStageDn.setStatus("current")
_CfprPolicyPolicyScopeFsmStageRn_Type = SnmpAdminString
_CfprPolicyPolicyScopeFsmStageRn_Object = MibTableColumn
cfprPolicyPolicyScopeFsmStageRn = _CfprPolicyPolicyScopeFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 30, 1, 3),
    _CfprPolicyPolicyScopeFsmStageRn_Type()
)
cfprPolicyPolicyScopeFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStageRn.setStatus("current")
_CfprPolicyPolicyScopeFsmStageDescrData_Type = SnmpAdminString
_CfprPolicyPolicyScopeFsmStageDescrData_Object = MibTableColumn
cfprPolicyPolicyScopeFsmStageDescrData = _CfprPolicyPolicyScopeFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 30, 1, 4),
    _CfprPolicyPolicyScopeFsmStageDescrData_Type()
)
cfprPolicyPolicyScopeFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStageDescrData.setStatus("current")
_CfprPolicyPolicyScopeFsmStageLastUpdateTime_Type = DateAndTime
_CfprPolicyPolicyScopeFsmStageLastUpdateTime_Object = MibTableColumn
cfprPolicyPolicyScopeFsmStageLastUpdateTime = _CfprPolicyPolicyScopeFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 30, 1, 5),
    _CfprPolicyPolicyScopeFsmStageLastUpdateTime_Type()
)
cfprPolicyPolicyScopeFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStageLastUpdateTime.setStatus("current")
_CfprPolicyPolicyScopeFsmStageName_Type = CfprPolicyPolicyScopeFsmStageName
_CfprPolicyPolicyScopeFsmStageName_Object = MibTableColumn
cfprPolicyPolicyScopeFsmStageName = _CfprPolicyPolicyScopeFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 30, 1, 6),
    _CfprPolicyPolicyScopeFsmStageName_Type()
)
cfprPolicyPolicyScopeFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStageName.setStatus("current")
_CfprPolicyPolicyScopeFsmStageOrder_Type = Gauge32
_CfprPolicyPolicyScopeFsmStageOrder_Object = MibTableColumn
cfprPolicyPolicyScopeFsmStageOrder = _CfprPolicyPolicyScopeFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 30, 1, 7),
    _CfprPolicyPolicyScopeFsmStageOrder_Type()
)
cfprPolicyPolicyScopeFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStageOrder.setStatus("current")
_CfprPolicyPolicyScopeFsmStageRetry_Type = Gauge32
_CfprPolicyPolicyScopeFsmStageRetry_Object = MibTableColumn
cfprPolicyPolicyScopeFsmStageRetry = _CfprPolicyPolicyScopeFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 30, 1, 8),
    _CfprPolicyPolicyScopeFsmStageRetry_Type()
)
cfprPolicyPolicyScopeFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStageRetry.setStatus("current")
_CfprPolicyPolicyScopeFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprPolicyPolicyScopeFsmStageStageStatus_Object = MibTableColumn
cfprPolicyPolicyScopeFsmStageStageStatus = _CfprPolicyPolicyScopeFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 30, 1, 9),
    _CfprPolicyPolicyScopeFsmStageStageStatus_Type()
)
cfprPolicyPolicyScopeFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmStageStageStatus.setStatus("current")
_CfprPolicyPolicyScopeFsmTaskTable_Object = MibTable
cfprPolicyPolicyScopeFsmTaskTable = _CfprPolicyPolicyScopeFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 31)
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmTaskTable.setStatus("current")
_CfprPolicyPolicyScopeFsmTaskEntry_Object = MibTableRow
cfprPolicyPolicyScopeFsmTaskEntry = _CfprPolicyPolicyScopeFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 31, 1)
)
cfprPolicyPolicyScopeFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyPolicyScopeFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmTaskEntry.setStatus("current")
_CfprPolicyPolicyScopeFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprPolicyPolicyScopeFsmTaskInstanceId_Object = MibTableColumn
cfprPolicyPolicyScopeFsmTaskInstanceId = _CfprPolicyPolicyScopeFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 31, 1, 1),
    _CfprPolicyPolicyScopeFsmTaskInstanceId_Type()
)
cfprPolicyPolicyScopeFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmTaskInstanceId.setStatus("current")
_CfprPolicyPolicyScopeFsmTaskDn_Type = CfprManagedObjectDn
_CfprPolicyPolicyScopeFsmTaskDn_Object = MibTableColumn
cfprPolicyPolicyScopeFsmTaskDn = _CfprPolicyPolicyScopeFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 31, 1, 2),
    _CfprPolicyPolicyScopeFsmTaskDn_Type()
)
cfprPolicyPolicyScopeFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmTaskDn.setStatus("current")
_CfprPolicyPolicyScopeFsmTaskRn_Type = SnmpAdminString
_CfprPolicyPolicyScopeFsmTaskRn_Object = MibTableColumn
cfprPolicyPolicyScopeFsmTaskRn = _CfprPolicyPolicyScopeFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 31, 1, 3),
    _CfprPolicyPolicyScopeFsmTaskRn_Type()
)
cfprPolicyPolicyScopeFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmTaskRn.setStatus("current")
_CfprPolicyPolicyScopeFsmTaskCompletion_Type = CfprFsmCompletion
_CfprPolicyPolicyScopeFsmTaskCompletion_Object = MibTableColumn
cfprPolicyPolicyScopeFsmTaskCompletion = _CfprPolicyPolicyScopeFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 31, 1, 4),
    _CfprPolicyPolicyScopeFsmTaskCompletion_Type()
)
cfprPolicyPolicyScopeFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmTaskCompletion.setStatus("current")
_CfprPolicyPolicyScopeFsmTaskFlags_Type = CfprFsmFlags
_CfprPolicyPolicyScopeFsmTaskFlags_Object = MibTableColumn
cfprPolicyPolicyScopeFsmTaskFlags = _CfprPolicyPolicyScopeFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 31, 1, 5),
    _CfprPolicyPolicyScopeFsmTaskFlags_Type()
)
cfprPolicyPolicyScopeFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmTaskFlags.setStatus("current")
_CfprPolicyPolicyScopeFsmTaskItem_Type = CfprPolicyPolicyScopeFsmTaskItem
_CfprPolicyPolicyScopeFsmTaskItem_Object = MibTableColumn
cfprPolicyPolicyScopeFsmTaskItem = _CfprPolicyPolicyScopeFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 31, 1, 6),
    _CfprPolicyPolicyScopeFsmTaskItem_Type()
)
cfprPolicyPolicyScopeFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmTaskItem.setStatus("current")
_CfprPolicyPolicyScopeFsmTaskSeqId_Type = Gauge32
_CfprPolicyPolicyScopeFsmTaskSeqId_Object = MibTableColumn
cfprPolicyPolicyScopeFsmTaskSeqId = _CfprPolicyPolicyScopeFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 31, 1, 7),
    _CfprPolicyPolicyScopeFsmTaskSeqId_Type()
)
cfprPolicyPolicyScopeFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPolicyScopeFsmTaskSeqId.setStatus("current")
_CfprPolicyPowerMgmtTable_Object = MibTable
cfprPolicyPowerMgmtTable = _CfprPolicyPowerMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 32)
)
if mibBuilder.loadTexts:
    cfprPolicyPowerMgmtTable.setStatus("current")
_CfprPolicyPowerMgmtEntry_Object = MibTableRow
cfprPolicyPowerMgmtEntry = _CfprPolicyPowerMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 32, 1)
)
cfprPolicyPowerMgmtEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyPowerMgmtInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyPowerMgmtEntry.setStatus("current")
_CfprPolicyPowerMgmtInstanceId_Type = CfprManagedObjectId
_CfprPolicyPowerMgmtInstanceId_Object = MibTableColumn
cfprPolicyPowerMgmtInstanceId = _CfprPolicyPowerMgmtInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 32, 1, 1),
    _CfprPolicyPowerMgmtInstanceId_Type()
)
cfprPolicyPowerMgmtInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyPowerMgmtInstanceId.setStatus("current")
_CfprPolicyPowerMgmtDn_Type = CfprManagedObjectDn
_CfprPolicyPowerMgmtDn_Object = MibTableColumn
cfprPolicyPowerMgmtDn = _CfprPolicyPowerMgmtDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 32, 1, 2),
    _CfprPolicyPowerMgmtDn_Type()
)
cfprPolicyPowerMgmtDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPowerMgmtDn.setStatus("current")
_CfprPolicyPowerMgmtRn_Type = SnmpAdminString
_CfprPolicyPowerMgmtRn_Object = MibTableColumn
cfprPolicyPowerMgmtRn = _CfprPolicyPowerMgmtRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 32, 1, 3),
    _CfprPolicyPowerMgmtRn_Type()
)
cfprPolicyPowerMgmtRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPowerMgmtRn.setStatus("current")
_CfprPolicyPowerMgmtSource_Type = CfprPolicyControlSource
_CfprPolicyPowerMgmtSource_Object = MibTableColumn
cfprPolicyPowerMgmtSource = _CfprPolicyPowerMgmtSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 32, 1, 4),
    _CfprPolicyPowerMgmtSource_Type()
)
cfprPolicyPowerMgmtSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPowerMgmtSource.setStatus("current")
_CfprPolicyPsuTable_Object = MibTable
cfprPolicyPsuTable = _CfprPolicyPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 33)
)
if mibBuilder.loadTexts:
    cfprPolicyPsuTable.setStatus("current")
_CfprPolicyPsuEntry_Object = MibTableRow
cfprPolicyPsuEntry = _CfprPolicyPsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 33, 1)
)
cfprPolicyPsuEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyPsuInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyPsuEntry.setStatus("current")
_CfprPolicyPsuInstanceId_Type = CfprManagedObjectId
_CfprPolicyPsuInstanceId_Object = MibTableColumn
cfprPolicyPsuInstanceId = _CfprPolicyPsuInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 33, 1, 1),
    _CfprPolicyPsuInstanceId_Type()
)
cfprPolicyPsuInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyPsuInstanceId.setStatus("current")
_CfprPolicyPsuDn_Type = CfprManagedObjectDn
_CfprPolicyPsuDn_Object = MibTableColumn
cfprPolicyPsuDn = _CfprPolicyPsuDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 33, 1, 2),
    _CfprPolicyPsuDn_Type()
)
cfprPolicyPsuDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPsuDn.setStatus("current")
_CfprPolicyPsuRn_Type = SnmpAdminString
_CfprPolicyPsuRn_Object = MibTableColumn
cfprPolicyPsuRn = _CfprPolicyPsuRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 33, 1, 3),
    _CfprPolicyPsuRn_Type()
)
cfprPolicyPsuRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPsuRn.setStatus("current")
_CfprPolicyPsuSource_Type = CfprPolicyControlSource
_CfprPolicyPsuSource_Object = MibTableColumn
cfprPolicyPsuSource = _CfprPolicyPsuSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 33, 1, 4),
    _CfprPolicyPsuSource_Type()
)
cfprPolicyPsuSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyPsuSource.setStatus("current")
_CfprPolicyRefReqTable_Object = MibTable
cfprPolicyRefReqTable = _CfprPolicyRefReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 34)
)
if mibBuilder.loadTexts:
    cfprPolicyRefReqTable.setStatus("current")
_CfprPolicyRefReqEntry_Object = MibTableRow
cfprPolicyRefReqEntry = _CfprPolicyRefReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 34, 1)
)
cfprPolicyRefReqEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicyRefReqInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicyRefReqEntry.setStatus("current")
_CfprPolicyRefReqInstanceId_Type = CfprManagedObjectId
_CfprPolicyRefReqInstanceId_Object = MibTableColumn
cfprPolicyRefReqInstanceId = _CfprPolicyRefReqInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 34, 1, 1),
    _CfprPolicyRefReqInstanceId_Type()
)
cfprPolicyRefReqInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicyRefReqInstanceId.setStatus("current")
_CfprPolicyRefReqDn_Type = CfprManagedObjectDn
_CfprPolicyRefReqDn_Object = MibTableColumn
cfprPolicyRefReqDn = _CfprPolicyRefReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 34, 1, 2),
    _CfprPolicyRefReqDn_Type()
)
cfprPolicyRefReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyRefReqDn.setStatus("current")
_CfprPolicyRefReqRn_Type = SnmpAdminString
_CfprPolicyRefReqRn_Object = MibTableColumn
cfprPolicyRefReqRn = _CfprPolicyRefReqRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 34, 1, 3),
    _CfprPolicyRefReqRn_Type()
)
cfprPolicyRefReqRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyRefReqRn.setStatus("current")
_CfprPolicyRefReqPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprPolicyRefReqPolicyOwner_Object = MibTableColumn
cfprPolicyRefReqPolicyOwner = _CfprPolicyRefReqPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 34, 1, 4),
    _CfprPolicyRefReqPolicyOwner_Type()
)
cfprPolicyRefReqPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyRefReqPolicyOwner.setStatus("current")
_CfprPolicyRefReqRefConvertedDn_Type = SnmpAdminString
_CfprPolicyRefReqRefConvertedDn_Object = MibTableColumn
cfprPolicyRefReqRefConvertedDn = _CfprPolicyRefReqRefConvertedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 34, 1, 5),
    _CfprPolicyRefReqRefConvertedDn_Type()
)
cfprPolicyRefReqRefConvertedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyRefReqRefConvertedDn.setStatus("current")
_CfprPolicyRefReqRefPolicyDn_Type = SnmpAdminString
_CfprPolicyRefReqRefPolicyDn_Object = MibTableColumn
cfprPolicyRefReqRefPolicyDn = _CfprPolicyRefReqRefPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 34, 1, 6),
    _CfprPolicyRefReqRefPolicyDn_Type()
)
cfprPolicyRefReqRefPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicyRefReqRefPolicyDn.setStatus("current")
_CfprPolicySecurityTable_Object = MibTable
cfprPolicySecurityTable = _CfprPolicySecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 35)
)
if mibBuilder.loadTexts:
    cfprPolicySecurityTable.setStatus("current")
_CfprPolicySecurityEntry_Object = MibTableRow
cfprPolicySecurityEntry = _CfprPolicySecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 35, 1)
)
cfprPolicySecurityEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-POLICY-MIB", "cfprPolicySecurityInstanceId"),
)
if mibBuilder.loadTexts:
    cfprPolicySecurityEntry.setStatus("current")
_CfprPolicySecurityInstanceId_Type = CfprManagedObjectId
_CfprPolicySecurityInstanceId_Object = MibTableColumn
cfprPolicySecurityInstanceId = _CfprPolicySecurityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 35, 1, 1),
    _CfprPolicySecurityInstanceId_Type()
)
cfprPolicySecurityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprPolicySecurityInstanceId.setStatus("current")
_CfprPolicySecurityDn_Type = CfprManagedObjectDn
_CfprPolicySecurityDn_Object = MibTableColumn
cfprPolicySecurityDn = _CfprPolicySecurityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 35, 1, 2),
    _CfprPolicySecurityDn_Type()
)
cfprPolicySecurityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicySecurityDn.setStatus("current")
_CfprPolicySecurityRn_Type = SnmpAdminString
_CfprPolicySecurityRn_Object = MibTableColumn
cfprPolicySecurityRn = _CfprPolicySecurityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 35, 1, 3),
    _CfprPolicySecurityRn_Type()
)
cfprPolicySecurityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicySecurityRn.setStatus("current")
_CfprPolicySecuritySource_Type = CfprPolicyControlSource
_CfprPolicySecuritySource_Object = MibTableColumn
cfprPolicySecuritySource = _CfprPolicySecuritySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 62, 35, 1, 4),
    _CfprPolicySecuritySource_Type()
)
cfprPolicySecuritySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprPolicySecuritySource.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-POLICY-MIB",
    **{"cfprPolicyObjects": cfprPolicyObjects,
       "cfprPolicyCentraleSyncTable": cfprPolicyCentraleSyncTable,
       "cfprPolicyCentraleSyncEntry": cfprPolicyCentraleSyncEntry,
       "cfprPolicyCentraleSyncInstanceId": cfprPolicyCentraleSyncInstanceId,
       "cfprPolicyCentraleSyncDn": cfprPolicyCentraleSyncDn,
       "cfprPolicyCentraleSyncRn": cfprPolicyCentraleSyncRn,
       "cfprPolicyCentraleSyncLeftData": cfprPolicyCentraleSyncLeftData,
       "cfprPolicyCentraleSyncRightData": cfprPolicyCentraleSyncRightData,
       "cfprPolicyCommunicationTable": cfprPolicyCommunicationTable,
       "cfprPolicyCommunicationEntry": cfprPolicyCommunicationEntry,
       "cfprPolicyCommunicationInstanceId": cfprPolicyCommunicationInstanceId,
       "cfprPolicyCommunicationDn": cfprPolicyCommunicationDn,
       "cfprPolicyCommunicationRn": cfprPolicyCommunicationRn,
       "cfprPolicyCommunicationSource": cfprPolicyCommunicationSource,
       "cfprPolicyConfigBackupTable": cfprPolicyConfigBackupTable,
       "cfprPolicyConfigBackupEntry": cfprPolicyConfigBackupEntry,
       "cfprPolicyConfigBackupInstanceId": cfprPolicyConfigBackupInstanceId,
       "cfprPolicyConfigBackupDn": cfprPolicyConfigBackupDn,
       "cfprPolicyConfigBackupRn": cfprPolicyConfigBackupRn,
       "cfprPolicyConfigBackupSource": cfprPolicyConfigBackupSource,
       "cfprPolicyControlEpTable": cfprPolicyControlEpTable,
       "cfprPolicyControlEpEntry": cfprPolicyControlEpEntry,
       "cfprPolicyControlEpInstanceId": cfprPolicyControlEpInstanceId,
       "cfprPolicyControlEpDn": cfprPolicyControlEpDn,
       "cfprPolicyControlEpRn": cfprPolicyControlEpRn,
       "cfprPolicyControlEpAckState": cfprPolicyControlEpAckState,
       "cfprPolicyControlEpCleanupMode": cfprPolicyControlEpCleanupMode,
       "cfprPolicyControlEpEncSecret": cfprPolicyControlEpEncSecret,
       "cfprPolicyControlEpFsmDescr": cfprPolicyControlEpFsmDescr,
       "cfprPolicyControlEpFsmPrev": cfprPolicyControlEpFsmPrev,
       "cfprPolicyControlEpFsmProgr": cfprPolicyControlEpFsmProgr,
       "cfprPolicyControlEpFsmRmtInvErrCode": cfprPolicyControlEpFsmRmtInvErrCode,
       "cfprPolicyControlEpFsmRmtInvErrDescr": cfprPolicyControlEpFsmRmtInvErrDescr,
       "cfprPolicyControlEpFsmRmtInvRslt": cfprPolicyControlEpFsmRmtInvRslt,
       "cfprPolicyControlEpFsmStageDescr": cfprPolicyControlEpFsmStageDescr,
       "cfprPolicyControlEpFsmStamp": cfprPolicyControlEpFsmStamp,
       "cfprPolicyControlEpFsmStatus": cfprPolicyControlEpFsmStatus,
       "cfprPolicyControlEpFsmTry": cfprPolicyControlEpFsmTry,
       "cfprPolicyControlEpName": cfprPolicyControlEpName,
       "cfprPolicyControlEpRegistrationState": cfprPolicyControlEpRegistrationState,
       "cfprPolicyControlEpRepairState": cfprPolicyControlEpRepairState,
       "cfprPolicyControlEpSecret": cfprPolicyControlEpSecret,
       "cfprPolicyControlEpState": cfprPolicyControlEpState,
       "cfprPolicyControlEpSuspendState": cfprPolicyControlEpSuspendState,
       "cfprPolicyControlEpSvcRegIP": cfprPolicyControlEpSvcRegIP,
       "cfprPolicyControlEpSvcRegName": cfprPolicyControlEpSvcRegName,
       "cfprPolicyControlEpType": cfprPolicyControlEpType,
       "cfprPolicyControlEpFsmTable": cfprPolicyControlEpFsmTable,
       "cfprPolicyControlEpFsmEntry": cfprPolicyControlEpFsmEntry,
       "cfprPolicyControlEpFsmInstanceId": cfprPolicyControlEpFsmInstanceId,
       "cfprPolicyControlEpFsmDn": cfprPolicyControlEpFsmDn,
       "cfprPolicyControlEpFsmRn": cfprPolicyControlEpFsmRn,
       "cfprPolicyControlEpFsmCompletionTime": cfprPolicyControlEpFsmCompletionTime,
       "cfprPolicyControlEpFsmCurrentFsm": cfprPolicyControlEpFsmCurrentFsm,
       "cfprPolicyControlEpFsmDescrData": cfprPolicyControlEpFsmDescrData,
       "cfprPolicyControlEpFsmFsmStatus": cfprPolicyControlEpFsmFsmStatus,
       "cfprPolicyControlEpFsmProgress": cfprPolicyControlEpFsmProgress,
       "cfprPolicyControlEpFsmRmtErrCode": cfprPolicyControlEpFsmRmtErrCode,
       "cfprPolicyControlEpFsmRmtErrDescr": cfprPolicyControlEpFsmRmtErrDescr,
       "cfprPolicyControlEpFsmRmtRslt": cfprPolicyControlEpFsmRmtRslt,
       "cfprPolicyControlEpFsmStageTable": cfprPolicyControlEpFsmStageTable,
       "cfprPolicyControlEpFsmStageEntry": cfprPolicyControlEpFsmStageEntry,
       "cfprPolicyControlEpFsmStageInstanceId": cfprPolicyControlEpFsmStageInstanceId,
       "cfprPolicyControlEpFsmStageDn": cfprPolicyControlEpFsmStageDn,
       "cfprPolicyControlEpFsmStageRn": cfprPolicyControlEpFsmStageRn,
       "cfprPolicyControlEpFsmStageDescrData": cfprPolicyControlEpFsmStageDescrData,
       "cfprPolicyControlEpFsmStageLastUpdateTime": cfprPolicyControlEpFsmStageLastUpdateTime,
       "cfprPolicyControlEpFsmStageName": cfprPolicyControlEpFsmStageName,
       "cfprPolicyControlEpFsmStageOrder": cfprPolicyControlEpFsmStageOrder,
       "cfprPolicyControlEpFsmStageRetry": cfprPolicyControlEpFsmStageRetry,
       "cfprPolicyControlEpFsmStageStageStatus": cfprPolicyControlEpFsmStageStageStatus,
       "cfprPolicyControlEpFsmTaskTable": cfprPolicyControlEpFsmTaskTable,
       "cfprPolicyControlEpFsmTaskEntry": cfprPolicyControlEpFsmTaskEntry,
       "cfprPolicyControlEpFsmTaskInstanceId": cfprPolicyControlEpFsmTaskInstanceId,
       "cfprPolicyControlEpFsmTaskDn": cfprPolicyControlEpFsmTaskDn,
       "cfprPolicyControlEpFsmTaskRn": cfprPolicyControlEpFsmTaskRn,
       "cfprPolicyControlEpFsmTaskCompletion": cfprPolicyControlEpFsmTaskCompletion,
       "cfprPolicyControlEpFsmTaskFlags": cfprPolicyControlEpFsmTaskFlags,
       "cfprPolicyControlEpFsmTaskItem": cfprPolicyControlEpFsmTaskItem,
       "cfprPolicyControlEpFsmTaskSeqId": cfprPolicyControlEpFsmTaskSeqId,
       "cfprPolicyControlledInstanceTable": cfprPolicyControlledInstanceTable,
       "cfprPolicyControlledInstanceEntry": cfprPolicyControlledInstanceEntry,
       "cfprPolicyControlledInstanceInstanceId": cfprPolicyControlledInstanceInstanceId,
       "cfprPolicyControlledInstanceDn": cfprPolicyControlledInstanceDn,
       "cfprPolicyControlledInstanceRn": cfprPolicyControlledInstanceRn,
       "cfprPolicyControlledInstanceDefDn": cfprPolicyControlledInstanceDefDn,
       "cfprPolicyControlledInstanceExternalResolveName": cfprPolicyControlledInstanceExternalResolveName,
       "cfprPolicyControlledInstanceName": cfprPolicyControlledInstanceName,
       "cfprPolicyControlledInstanceResolveType": cfprPolicyControlledInstanceResolveType,
       "cfprPolicyControlledInstanceType": cfprPolicyControlledInstanceType,
       "cfprPolicyControlledTypeTable": cfprPolicyControlledTypeTable,
       "cfprPolicyControlledTypeEntry": cfprPolicyControlledTypeEntry,
       "cfprPolicyControlledTypeInstanceId": cfprPolicyControlledTypeInstanceId,
       "cfprPolicyControlledTypeDn": cfprPolicyControlledTypeDn,
       "cfprPolicyControlledTypeRn": cfprPolicyControlledTypeRn,
       "cfprPolicyControlledTypeFsmDescr": cfprPolicyControlledTypeFsmDescr,
       "cfprPolicyControlledTypeFsmPrev": cfprPolicyControlledTypeFsmPrev,
       "cfprPolicyControlledTypeFsmProgr": cfprPolicyControlledTypeFsmProgr,
       "cfprPolicyControlledTypeFsmRmtInvErrCode": cfprPolicyControlledTypeFsmRmtInvErrCode,
       "cfprPolicyControlledTypeFsmRmtInvErrDescr": cfprPolicyControlledTypeFsmRmtInvErrDescr,
       "cfprPolicyControlledTypeFsmRmtInvRslt": cfprPolicyControlledTypeFsmRmtInvRslt,
       "cfprPolicyControlledTypeFsmStageDescr": cfprPolicyControlledTypeFsmStageDescr,
       "cfprPolicyControlledTypeFsmStamp": cfprPolicyControlledTypeFsmStamp,
       "cfprPolicyControlledTypeFsmStatus": cfprPolicyControlledTypeFsmStatus,
       "cfprPolicyControlledTypeFsmTry": cfprPolicyControlledTypeFsmTry,
       "cfprPolicyControlledTypeParentContext": cfprPolicyControlledTypeParentContext,
       "cfprPolicyControlledTypeType": cfprPolicyControlledTypeType,
       "cfprPolicyControlledTypeFsmTable": cfprPolicyControlledTypeFsmTable,
       "cfprPolicyControlledTypeFsmEntry": cfprPolicyControlledTypeFsmEntry,
       "cfprPolicyControlledTypeFsmInstanceId": cfprPolicyControlledTypeFsmInstanceId,
       "cfprPolicyControlledTypeFsmDn": cfprPolicyControlledTypeFsmDn,
       "cfprPolicyControlledTypeFsmRn": cfprPolicyControlledTypeFsmRn,
       "cfprPolicyControlledTypeFsmCompletionTime": cfprPolicyControlledTypeFsmCompletionTime,
       "cfprPolicyControlledTypeFsmCurrentFsm": cfprPolicyControlledTypeFsmCurrentFsm,
       "cfprPolicyControlledTypeFsmDescrData": cfprPolicyControlledTypeFsmDescrData,
       "cfprPolicyControlledTypeFsmFsmStatus": cfprPolicyControlledTypeFsmFsmStatus,
       "cfprPolicyControlledTypeFsmProgress": cfprPolicyControlledTypeFsmProgress,
       "cfprPolicyControlledTypeFsmRmtErrCode": cfprPolicyControlledTypeFsmRmtErrCode,
       "cfprPolicyControlledTypeFsmRmtErrDescr": cfprPolicyControlledTypeFsmRmtErrDescr,
       "cfprPolicyControlledTypeFsmRmtRslt": cfprPolicyControlledTypeFsmRmtRslt,
       "cfprPolicyControlledTypeFsmStageTable": cfprPolicyControlledTypeFsmStageTable,
       "cfprPolicyControlledTypeFsmStageEntry": cfprPolicyControlledTypeFsmStageEntry,
       "cfprPolicyControlledTypeFsmStageInstanceId": cfprPolicyControlledTypeFsmStageInstanceId,
       "cfprPolicyControlledTypeFsmStageDn": cfprPolicyControlledTypeFsmStageDn,
       "cfprPolicyControlledTypeFsmStageRn": cfprPolicyControlledTypeFsmStageRn,
       "cfprPolicyControlledTypeFsmStageDescrData": cfprPolicyControlledTypeFsmStageDescrData,
       "cfprPolicyControlledTypeFsmStageLastUpdateTime": cfprPolicyControlledTypeFsmStageLastUpdateTime,
       "cfprPolicyControlledTypeFsmStageName": cfprPolicyControlledTypeFsmStageName,
       "cfprPolicyControlledTypeFsmStageOrder": cfprPolicyControlledTypeFsmStageOrder,
       "cfprPolicyControlledTypeFsmStageRetry": cfprPolicyControlledTypeFsmStageRetry,
       "cfprPolicyControlledTypeFsmStageStageStatus": cfprPolicyControlledTypeFsmStageStageStatus,
       "cfprPolicyControlledTypeFsmTaskTable": cfprPolicyControlledTypeFsmTaskTable,
       "cfprPolicyControlledTypeFsmTaskEntry": cfprPolicyControlledTypeFsmTaskEntry,
       "cfprPolicyControlledTypeFsmTaskInstanceId": cfprPolicyControlledTypeFsmTaskInstanceId,
       "cfprPolicyControlledTypeFsmTaskDn": cfprPolicyControlledTypeFsmTaskDn,
       "cfprPolicyControlledTypeFsmTaskRn": cfprPolicyControlledTypeFsmTaskRn,
       "cfprPolicyControlledTypeFsmTaskCompletion": cfprPolicyControlledTypeFsmTaskCompletion,
       "cfprPolicyControlledTypeFsmTaskFlags": cfprPolicyControlledTypeFsmTaskFlags,
       "cfprPolicyControlledTypeFsmTaskItem": cfprPolicyControlledTypeFsmTaskItem,
       "cfprPolicyControlledTypeFsmTaskSeqId": cfprPolicyControlledTypeFsmTaskSeqId,
       "cfprPolicyDateTimeTable": cfprPolicyDateTimeTable,
       "cfprPolicyDateTimeEntry": cfprPolicyDateTimeEntry,
       "cfprPolicyDateTimeInstanceId": cfprPolicyDateTimeInstanceId,
       "cfprPolicyDateTimeDn": cfprPolicyDateTimeDn,
       "cfprPolicyDateTimeRn": cfprPolicyDateTimeRn,
       "cfprPolicyDateTimeSource": cfprPolicyDateTimeSource,
       "cfprPolicyDigestTable": cfprPolicyDigestTable,
       "cfprPolicyDigestEntry": cfprPolicyDigestEntry,
       "cfprPolicyDigestInstanceId": cfprPolicyDigestInstanceId,
       "cfprPolicyDigestDn": cfprPolicyDigestDn,
       "cfprPolicyDigestRn": cfprPolicyDigestRn,
       "cfprPolicyDigestContext": cfprPolicyDigestContext,
       "cfprPolicyDigestDescr": cfprPolicyDigestDescr,
       "cfprPolicyDigestLabel": cfprPolicyDigestLabel,
       "cfprPolicyDigestName": cfprPolicyDigestName,
       "cfprPolicyDigestOnBehalfOfIdent": cfprPolicyDigestOnBehalfOfIdent,
       "cfprPolicyDigestOnBehalfOfType": cfprPolicyDigestOnBehalfOfType,
       "cfprPolicyDigestRequestorOwnership": cfprPolicyDigestRequestorOwnership,
       "cfprPolicyDigestResolveType": cfprPolicyDigestResolveType,
       "cfprPolicyDigestType": cfprPolicyDigestType,
       "cfprPolicyDigestUsage": cfprPolicyDigestUsage,
       "cfprPolicyDiscoveryTable": cfprPolicyDiscoveryTable,
       "cfprPolicyDiscoveryEntry": cfprPolicyDiscoveryEntry,
       "cfprPolicyDiscoveryInstanceId": cfprPolicyDiscoveryInstanceId,
       "cfprPolicyDiscoveryDn": cfprPolicyDiscoveryDn,
       "cfprPolicyDiscoveryRn": cfprPolicyDiscoveryRn,
       "cfprPolicyDiscoverySource": cfprPolicyDiscoverySource,
       "cfprPolicyDnsTable": cfprPolicyDnsTable,
       "cfprPolicyDnsEntry": cfprPolicyDnsEntry,
       "cfprPolicyDnsInstanceId": cfprPolicyDnsInstanceId,
       "cfprPolicyDnsDn": cfprPolicyDnsDn,
       "cfprPolicyDnsRn": cfprPolicyDnsRn,
       "cfprPolicyDnsSource": cfprPolicyDnsSource,
       "cfprPolicyElementTable": cfprPolicyElementTable,
       "cfprPolicyElementEntry": cfprPolicyElementEntry,
       "cfprPolicyElementInstanceId": cfprPolicyElementInstanceId,
       "cfprPolicyElementDn": cfprPolicyElementDn,
       "cfprPolicyElementRn": cfprPolicyElementRn,
       "cfprPolicyElementClassType": cfprPolicyElementClassType,
       "cfprPolicyElementConvertedDn": cfprPolicyElementConvertedDn,
       "cfprPolicyElementOwnership": cfprPolicyElementOwnership,
       "cfprPolicyElementPolicyDn": cfprPolicyElementPolicyDn,
       "cfprPolicyFaultTable": cfprPolicyFaultTable,
       "cfprPolicyFaultEntry": cfprPolicyFaultEntry,
       "cfprPolicyFaultInstanceId": cfprPolicyFaultInstanceId,
       "cfprPolicyFaultDn": cfprPolicyFaultDn,
       "cfprPolicyFaultRn": cfprPolicyFaultRn,
       "cfprPolicyFaultSource": cfprPolicyFaultSource,
       "cfprPolicyIdResolvePolicyTable": cfprPolicyIdResolvePolicyTable,
       "cfprPolicyIdResolvePolicyEntry": cfprPolicyIdResolvePolicyEntry,
       "cfprPolicyIdResolvePolicyInstanceId": cfprPolicyIdResolvePolicyInstanceId,
       "cfprPolicyIdResolvePolicyDn": cfprPolicyIdResolvePolicyDn,
       "cfprPolicyIdResolvePolicyRn": cfprPolicyIdResolvePolicyRn,
       "cfprPolicyIdResolvePolicyIdAssignmentMode": cfprPolicyIdResolvePolicyIdAssignmentMode,
       "cfprPolicyInfraFirmwareTable": cfprPolicyInfraFirmwareTable,
       "cfprPolicyInfraFirmwareEntry": cfprPolicyInfraFirmwareEntry,
       "cfprPolicyInfraFirmwareInstanceId": cfprPolicyInfraFirmwareInstanceId,
       "cfprPolicyInfraFirmwareDn": cfprPolicyInfraFirmwareDn,
       "cfprPolicyInfraFirmwareRn": cfprPolicyInfraFirmwareRn,
       "cfprPolicyInfraFirmwareSource": cfprPolicyInfraFirmwareSource,
       "cfprPolicyLocalMapTable": cfprPolicyLocalMapTable,
       "cfprPolicyLocalMapEntry": cfprPolicyLocalMapEntry,
       "cfprPolicyLocalMapInstanceId": cfprPolicyLocalMapInstanceId,
       "cfprPolicyLocalMapDn": cfprPolicyLocalMapDn,
       "cfprPolicyLocalMapRn": cfprPolicyLocalMapRn,
       "cfprPolicyMEpTable": cfprPolicyMEpTable,
       "cfprPolicyMEpEntry": cfprPolicyMEpEntry,
       "cfprPolicyMEpInstanceId": cfprPolicyMEpInstanceId,
       "cfprPolicyMEpDn": cfprPolicyMEpDn,
       "cfprPolicyMEpRn": cfprPolicyMEpRn,
       "cfprPolicyMEpSource": cfprPolicyMEpSource,
       "cfprPolicyMonitoringTable": cfprPolicyMonitoringTable,
       "cfprPolicyMonitoringEntry": cfprPolicyMonitoringEntry,
       "cfprPolicyMonitoringInstanceId": cfprPolicyMonitoringInstanceId,
       "cfprPolicyMonitoringDn": cfprPolicyMonitoringDn,
       "cfprPolicyMonitoringRn": cfprPolicyMonitoringRn,
       "cfprPolicyMonitoringSource": cfprPolicyMonitoringSource,
       "cfprPolicyPolicyEpTable": cfprPolicyPolicyEpTable,
       "cfprPolicyPolicyEpEntry": cfprPolicyPolicyEpEntry,
       "cfprPolicyPolicyEpInstanceId": cfprPolicyPolicyEpInstanceId,
       "cfprPolicyPolicyEpDn": cfprPolicyPolicyEpDn,
       "cfprPolicyPolicyEpRn": cfprPolicyPolicyEpRn,
       "cfprPolicyPolicyRequestorTable": cfprPolicyPolicyRequestorTable,
       "cfprPolicyPolicyRequestorEntry": cfprPolicyPolicyRequestorEntry,
       "cfprPolicyPolicyRequestorInstanceId": cfprPolicyPolicyRequestorInstanceId,
       "cfprPolicyPolicyRequestorDn": cfprPolicyPolicyRequestorDn,
       "cfprPolicyPolicyRequestorRn": cfprPolicyPolicyRequestorRn,
       "cfprPolicyPolicyRequestorName": cfprPolicyPolicyRequestorName,
       "cfprPolicyPolicyRequestorOnBehalfOfIdent": cfprPolicyPolicyRequestorOnBehalfOfIdent,
       "cfprPolicyPolicyRequestorOnBehalfOfType": cfprPolicyPolicyRequestorOnBehalfOfType,
       "cfprPolicyPolicyRequestorResolvedClassType": cfprPolicyPolicyRequestorResolvedClassType,
       "cfprPolicyPolicyScopeTable": cfprPolicyPolicyScopeTable,
       "cfprPolicyPolicyScopeEntry": cfprPolicyPolicyScopeEntry,
       "cfprPolicyPolicyScopeInstanceId": cfprPolicyPolicyScopeInstanceId,
       "cfprPolicyPolicyScopeDn": cfprPolicyPolicyScopeDn,
       "cfprPolicyPolicyScopeRn": cfprPolicyPolicyScopeRn,
       "cfprPolicyPolicyScopeAppType": cfprPolicyPolicyScopeAppType,
       "cfprPolicyPolicyScopeDefaultPolicyName": cfprPolicyPolicyScopeDefaultPolicyName,
       "cfprPolicyPolicyScopeFsmDescr": cfprPolicyPolicyScopeFsmDescr,
       "cfprPolicyPolicyScopeFsmPrev": cfprPolicyPolicyScopeFsmPrev,
       "cfprPolicyPolicyScopeFsmProgr": cfprPolicyPolicyScopeFsmProgr,
       "cfprPolicyPolicyScopeFsmRmtInvErrCode": cfprPolicyPolicyScopeFsmRmtInvErrCode,
       "cfprPolicyPolicyScopeFsmRmtInvErrDescr": cfprPolicyPolicyScopeFsmRmtInvErrDescr,
       "cfprPolicyPolicyScopeFsmRmtInvRslt": cfprPolicyPolicyScopeFsmRmtInvRslt,
       "cfprPolicyPolicyScopeFsmStageDescr": cfprPolicyPolicyScopeFsmStageDescr,
       "cfprPolicyPolicyScopeFsmStamp": cfprPolicyPolicyScopeFsmStamp,
       "cfprPolicyPolicyScopeFsmStatus": cfprPolicyPolicyScopeFsmStatus,
       "cfprPolicyPolicyScopeFsmTry": cfprPolicyPolicyScopeFsmTry,
       "cfprPolicyPolicyScopeOperStatus": cfprPolicyPolicyScopeOperStatus,
       "cfprPolicyPolicyScopeOwner": cfprPolicyPolicyScopeOwner,
       "cfprPolicyPolicyScopePolicyName": cfprPolicyPolicyScopePolicyName,
       "cfprPolicyPolicyScopePolicyType": cfprPolicyPolicyScopePolicyType,
       "cfprPolicyPolicyScopeRecursive": cfprPolicyPolicyScopeRecursive,
       "cfprPolicyPolicyScopeResolveType": cfprPolicyPolicyScopeResolveType,
       "cfprPolicyPolicyScopeContTable": cfprPolicyPolicyScopeContTable,
       "cfprPolicyPolicyScopeContEntry": cfprPolicyPolicyScopeContEntry,
       "cfprPolicyPolicyScopeContInstanceId": cfprPolicyPolicyScopeContInstanceId,
       "cfprPolicyPolicyScopeContDn": cfprPolicyPolicyScopeContDn,
       "cfprPolicyPolicyScopeContRn": cfprPolicyPolicyScopeContRn,
       "cfprPolicyPolicyScopeContAppType": cfprPolicyPolicyScopeContAppType,
       "cfprPolicyPolicyScopeContGenNum": cfprPolicyPolicyScopeContGenNum,
       "cfprPolicyPolicyScopeContNeedRecovery": cfprPolicyPolicyScopeContNeedRecovery,
       "cfprPolicyPolicyScopeContextTable": cfprPolicyPolicyScopeContextTable,
       "cfprPolicyPolicyScopeContextEntry": cfprPolicyPolicyScopeContextEntry,
       "cfprPolicyPolicyScopeContextInstanceId": cfprPolicyPolicyScopeContextInstanceId,
       "cfprPolicyPolicyScopeContextDn": cfprPolicyPolicyScopeContextDn,
       "cfprPolicyPolicyScopeContextRn": cfprPolicyPolicyScopeContextRn,
       "cfprPolicyPolicyScopeContextContext": cfprPolicyPolicyScopeContextContext,
       "cfprPolicyPolicyScopeContextName": cfprPolicyPolicyScopeContextName,
       "cfprPolicyPolicyScopeFsmTable": cfprPolicyPolicyScopeFsmTable,
       "cfprPolicyPolicyScopeFsmEntry": cfprPolicyPolicyScopeFsmEntry,
       "cfprPolicyPolicyScopeFsmInstanceId": cfprPolicyPolicyScopeFsmInstanceId,
       "cfprPolicyPolicyScopeFsmDn": cfprPolicyPolicyScopeFsmDn,
       "cfprPolicyPolicyScopeFsmRn": cfprPolicyPolicyScopeFsmRn,
       "cfprPolicyPolicyScopeFsmCompletionTime": cfprPolicyPolicyScopeFsmCompletionTime,
       "cfprPolicyPolicyScopeFsmCurrentFsm": cfprPolicyPolicyScopeFsmCurrentFsm,
       "cfprPolicyPolicyScopeFsmDescrData": cfprPolicyPolicyScopeFsmDescrData,
       "cfprPolicyPolicyScopeFsmFsmStatus": cfprPolicyPolicyScopeFsmFsmStatus,
       "cfprPolicyPolicyScopeFsmProgress": cfprPolicyPolicyScopeFsmProgress,
       "cfprPolicyPolicyScopeFsmRmtErrCode": cfprPolicyPolicyScopeFsmRmtErrCode,
       "cfprPolicyPolicyScopeFsmRmtErrDescr": cfprPolicyPolicyScopeFsmRmtErrDescr,
       "cfprPolicyPolicyScopeFsmRmtRslt": cfprPolicyPolicyScopeFsmRmtRslt,
       "cfprPolicyPolicyScopeFsmStageTable": cfprPolicyPolicyScopeFsmStageTable,
       "cfprPolicyPolicyScopeFsmStageEntry": cfprPolicyPolicyScopeFsmStageEntry,
       "cfprPolicyPolicyScopeFsmStageInstanceId": cfprPolicyPolicyScopeFsmStageInstanceId,
       "cfprPolicyPolicyScopeFsmStageDn": cfprPolicyPolicyScopeFsmStageDn,
       "cfprPolicyPolicyScopeFsmStageRn": cfprPolicyPolicyScopeFsmStageRn,
       "cfprPolicyPolicyScopeFsmStageDescrData": cfprPolicyPolicyScopeFsmStageDescrData,
       "cfprPolicyPolicyScopeFsmStageLastUpdateTime": cfprPolicyPolicyScopeFsmStageLastUpdateTime,
       "cfprPolicyPolicyScopeFsmStageName": cfprPolicyPolicyScopeFsmStageName,
       "cfprPolicyPolicyScopeFsmStageOrder": cfprPolicyPolicyScopeFsmStageOrder,
       "cfprPolicyPolicyScopeFsmStageRetry": cfprPolicyPolicyScopeFsmStageRetry,
       "cfprPolicyPolicyScopeFsmStageStageStatus": cfprPolicyPolicyScopeFsmStageStageStatus,
       "cfprPolicyPolicyScopeFsmTaskTable": cfprPolicyPolicyScopeFsmTaskTable,
       "cfprPolicyPolicyScopeFsmTaskEntry": cfprPolicyPolicyScopeFsmTaskEntry,
       "cfprPolicyPolicyScopeFsmTaskInstanceId": cfprPolicyPolicyScopeFsmTaskInstanceId,
       "cfprPolicyPolicyScopeFsmTaskDn": cfprPolicyPolicyScopeFsmTaskDn,
       "cfprPolicyPolicyScopeFsmTaskRn": cfprPolicyPolicyScopeFsmTaskRn,
       "cfprPolicyPolicyScopeFsmTaskCompletion": cfprPolicyPolicyScopeFsmTaskCompletion,
       "cfprPolicyPolicyScopeFsmTaskFlags": cfprPolicyPolicyScopeFsmTaskFlags,
       "cfprPolicyPolicyScopeFsmTaskItem": cfprPolicyPolicyScopeFsmTaskItem,
       "cfprPolicyPolicyScopeFsmTaskSeqId": cfprPolicyPolicyScopeFsmTaskSeqId,
       "cfprPolicyPowerMgmtTable": cfprPolicyPowerMgmtTable,
       "cfprPolicyPowerMgmtEntry": cfprPolicyPowerMgmtEntry,
       "cfprPolicyPowerMgmtInstanceId": cfprPolicyPowerMgmtInstanceId,
       "cfprPolicyPowerMgmtDn": cfprPolicyPowerMgmtDn,
       "cfprPolicyPowerMgmtRn": cfprPolicyPowerMgmtRn,
       "cfprPolicyPowerMgmtSource": cfprPolicyPowerMgmtSource,
       "cfprPolicyPsuTable": cfprPolicyPsuTable,
       "cfprPolicyPsuEntry": cfprPolicyPsuEntry,
       "cfprPolicyPsuInstanceId": cfprPolicyPsuInstanceId,
       "cfprPolicyPsuDn": cfprPolicyPsuDn,
       "cfprPolicyPsuRn": cfprPolicyPsuRn,
       "cfprPolicyPsuSource": cfprPolicyPsuSource,
       "cfprPolicyRefReqTable": cfprPolicyRefReqTable,
       "cfprPolicyRefReqEntry": cfprPolicyRefReqEntry,
       "cfprPolicyRefReqInstanceId": cfprPolicyRefReqInstanceId,
       "cfprPolicyRefReqDn": cfprPolicyRefReqDn,
       "cfprPolicyRefReqRn": cfprPolicyRefReqRn,
       "cfprPolicyRefReqPolicyOwner": cfprPolicyRefReqPolicyOwner,
       "cfprPolicyRefReqRefConvertedDn": cfprPolicyRefReqRefConvertedDn,
       "cfprPolicyRefReqRefPolicyDn": cfprPolicyRefReqRefPolicyDn,
       "cfprPolicySecurityTable": cfprPolicySecurityTable,
       "cfprPolicySecurityEntry": cfprPolicySecurityEntry,
       "cfprPolicySecurityInstanceId": cfprPolicySecurityInstanceId,
       "cfprPolicySecurityDn": cfprPolicySecurityDn,
       "cfprPolicySecurityRn": cfprPolicySecurityRn,
       "cfprPolicySecuritySource": cfprPolicySecuritySource}
)
