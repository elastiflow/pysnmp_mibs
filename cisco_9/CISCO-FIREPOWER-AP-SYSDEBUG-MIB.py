# SNMP MIB module (CISCO-FIREPOWER-AP-SYSDEBUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-SYSDEBUG-MIB.mib
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

(CfprApCommClientAdminState,
 CfprApConditionRemoteInvRslt,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApNetworkSwitchId,
 CfprApPolicyPolicyOwner,
 CfprApSysdebugAutoCoreFileExportTargetFsmCurrentFsm,
 CfprApSysdebugAutoCoreFileExportTargetFsmStageName,
 CfprApSysdebugAutoCoreFileExportTargetFsmTaskItem,
 CfprApSysdebugAutoCoreFileExportTargetProto,
 CfprApSysdebugBackupBehaviorInterval,
 CfprApSysdebugBackupBehaviorProto,
 CfprApSysdebugBackupFormat,
 CfprApSysdebugCoreExportStatus,
 CfprApSysdebugCoreFileAdminState,
 CfprApSysdebugCoreFileOperState,
 CfprApSysdebugCoreFsmCurrentFsm,
 CfprApSysdebugCoreFsmStageName,
 CfprApSysdebugCoreFsmTaskItem,
 CfprApSysdebugEpLogAdminState,
 CfprApSysdebugEpLogBackupAction,
 CfprApSysdebugEpLogCapacity,
 CfprApSysdebugEpLogType,
 CfprApSysdebugExportStatus,
 CfprApSysdebugLogControlDomainEnum,
 CfprApSysdebugLogControlEpFsmCurrentFsm,
 CfprApSysdebugLogControlEpFsmStageName,
 CfprApSysdebugLogControlEpFsmTaskItem,
 CfprApSysdebugLogControlLevel,
 CfprApSysdebugLogExportPolicyFsmCurrentFsm,
 CfprApSysdebugLogExportPolicyFsmStageName,
 CfprApSysdebugLogExportPolicyFsmTaskItem,
 CfprApSysdebugLogExportPolicyProto,
 CfprApSysdebugMEpLogOperState,
 CfprApSysdebugManualCoreFileExportTargetAdminState,
 CfprApSysdebugManualCoreFileExportTargetFsmCurrentFsm,
 CfprApSysdebugManualCoreFileExportTargetFsmStageName,
 CfprApSysdebugManualCoreFileExportTargetFsmTaskItem,
 CfprApSysdebugManualCoreFileExportTargetProto,
 CfprApSysdebugTSCmdOptMajorType,
 CfprApSysdebugTechSupportAdminState,
 CfprApSysdebugTechSupportFsmCurrentFsm,
 CfprApSysdebugTechSupportFsmStageName,
 CfprApSysdebugTechSupportFsmTaskItem,
 CfprApSysdebugTechSupportOperState,
 CfprApSysfileExporterPostAction) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApCommClientAdminState",
    "CfprApConditionRemoteInvRslt",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApNetworkSwitchId",
    "CfprApPolicyPolicyOwner",
    "CfprApSysdebugAutoCoreFileExportTargetFsmCurrentFsm",
    "CfprApSysdebugAutoCoreFileExportTargetFsmStageName",
    "CfprApSysdebugAutoCoreFileExportTargetFsmTaskItem",
    "CfprApSysdebugAutoCoreFileExportTargetProto",
    "CfprApSysdebugBackupBehaviorInterval",
    "CfprApSysdebugBackupBehaviorProto",
    "CfprApSysdebugBackupFormat",
    "CfprApSysdebugCoreExportStatus",
    "CfprApSysdebugCoreFileAdminState",
    "CfprApSysdebugCoreFileOperState",
    "CfprApSysdebugCoreFsmCurrentFsm",
    "CfprApSysdebugCoreFsmStageName",
    "CfprApSysdebugCoreFsmTaskItem",
    "CfprApSysdebugEpLogAdminState",
    "CfprApSysdebugEpLogBackupAction",
    "CfprApSysdebugEpLogCapacity",
    "CfprApSysdebugEpLogType",
    "CfprApSysdebugExportStatus",
    "CfprApSysdebugLogControlDomainEnum",
    "CfprApSysdebugLogControlEpFsmCurrentFsm",
    "CfprApSysdebugLogControlEpFsmStageName",
    "CfprApSysdebugLogControlEpFsmTaskItem",
    "CfprApSysdebugLogControlLevel",
    "CfprApSysdebugLogExportPolicyFsmCurrentFsm",
    "CfprApSysdebugLogExportPolicyFsmStageName",
    "CfprApSysdebugLogExportPolicyFsmTaskItem",
    "CfprApSysdebugLogExportPolicyProto",
    "CfprApSysdebugMEpLogOperState",
    "CfprApSysdebugManualCoreFileExportTargetAdminState",
    "CfprApSysdebugManualCoreFileExportTargetFsmCurrentFsm",
    "CfprApSysdebugManualCoreFileExportTargetFsmStageName",
    "CfprApSysdebugManualCoreFileExportTargetFsmTaskItem",
    "CfprApSysdebugManualCoreFileExportTargetProto",
    "CfprApSysdebugTSCmdOptMajorType",
    "CfprApSysdebugTechSupportAdminState",
    "CfprApSysdebugTechSupportFsmCurrentFsm",
    "CfprApSysdebugTechSupportFsmStageName",
    "CfprApSysdebugTechSupportFsmTaskItem",
    "CfprApSysdebugTechSupportOperState",
    "CfprApSysfileExporterPostAction")

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

cfprApSysdebugObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApSysdebugAutoCoreFileExportTargetTable_Object = MibTable
cfprApSysdebugAutoCoreFileExportTargetTable = _CfprApSysdebugAutoCoreFileExportTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1)
)
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetTable.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetEntry_Object = MibTableRow
cfprApSysdebugAutoCoreFileExportTargetEntry = _CfprApSysdebugAutoCoreFileExportTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1)
)
cfprApSysdebugAutoCoreFileExportTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugAutoCoreFileExportTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetEntry.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugAutoCoreFileExportTargetInstanceId_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetInstanceId = _CfprApSysdebugAutoCoreFileExportTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 1),
    _CfprApSysdebugAutoCoreFileExportTargetInstanceId_Type()
)
cfprApSysdebugAutoCoreFileExportTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetInstanceId.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetDn_Type = CfprApManagedObjectDn
_CfprApSysdebugAutoCoreFileExportTargetDn_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetDn = _CfprApSysdebugAutoCoreFileExportTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 2),
    _CfprApSysdebugAutoCoreFileExportTargetDn_Type()
)
cfprApSysdebugAutoCoreFileExportTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetDn.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetRn_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetRn_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetRn = _CfprApSysdebugAutoCoreFileExportTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 3),
    _CfprApSysdebugAutoCoreFileExportTargetRn_Type()
)
cfprApSysdebugAutoCoreFileExportTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetRn.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetAdminState_Type = CfprApCommClientAdminState
_CfprApSysdebugAutoCoreFileExportTargetAdminState_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetAdminState = _CfprApSysdebugAutoCoreFileExportTargetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 4),
    _CfprApSysdebugAutoCoreFileExportTargetAdminState_Type()
)
cfprApSysdebugAutoCoreFileExportTargetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetAdminState.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetDescr_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetDescr_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetDescr = _CfprApSysdebugAutoCoreFileExportTargetDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 5),
    _CfprApSysdebugAutoCoreFileExportTargetDescr_Type()
)
cfprApSysdebugAutoCoreFileExportTargetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetDescr.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetExportFailureReason_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetExportFailureReason_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetExportFailureReason = _CfprApSysdebugAutoCoreFileExportTargetExportFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 6),
    _CfprApSysdebugAutoCoreFileExportTargetExportFailureReason_Type()
)
cfprApSysdebugAutoCoreFileExportTargetExportFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetExportFailureReason.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetExportStatus_Type = CfprApSysdebugCoreExportStatus
_CfprApSysdebugAutoCoreFileExportTargetExportStatus_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetExportStatus = _CfprApSysdebugAutoCoreFileExportTargetExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 7),
    _CfprApSysdebugAutoCoreFileExportTargetExportStatus_Type()
)
cfprApSysdebugAutoCoreFileExportTargetExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetExportStatus.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmDescr_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetFsmDescr_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmDescr = _CfprApSysdebugAutoCoreFileExportTargetFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 8),
    _CfprApSysdebugAutoCoreFileExportTargetFsmDescr_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmDescr.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmPrev_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetFsmPrev_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmPrev = _CfprApSysdebugAutoCoreFileExportTargetFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 9),
    _CfprApSysdebugAutoCoreFileExportTargetFsmPrev_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmPrev.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmProgr_Type = Gauge32
_CfprApSysdebugAutoCoreFileExportTargetFsmProgr_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmProgr = _CfprApSysdebugAutoCoreFileExportTargetFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 10),
    _CfprApSysdebugAutoCoreFileExportTargetFsmProgr_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmProgr.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode_Type = Gauge32
_CfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode = _CfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 11),
    _CfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr = _CfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 12),
    _CfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysdebugAutoCoreFileExportTargetFsmRmtInvRslt_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvRslt = _CfprApSysdebugAutoCoreFileExportTargetFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 13),
    _CfprApSysdebugAutoCoreFileExportTargetFsmRmtInvRslt_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvRslt.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStageDescr_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetFsmStageDescr_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmStageDescr = _CfprApSysdebugAutoCoreFileExportTargetFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 14),
    _CfprApSysdebugAutoCoreFileExportTargetFsmStageDescr_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStageDescr.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStamp_Type = DateAndTime
_CfprApSysdebugAutoCoreFileExportTargetFsmStamp_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmStamp = _CfprApSysdebugAutoCoreFileExportTargetFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 15),
    _CfprApSysdebugAutoCoreFileExportTargetFsmStamp_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStamp.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStatus_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetFsmStatus_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmStatus = _CfprApSysdebugAutoCoreFileExportTargetFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 16),
    _CfprApSysdebugAutoCoreFileExportTargetFsmStatus_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStatus.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmTry_Type = Gauge32
_CfprApSysdebugAutoCoreFileExportTargetFsmTry_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmTry = _CfprApSysdebugAutoCoreFileExportTargetFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 17),
    _CfprApSysdebugAutoCoreFileExportTargetFsmTry_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmTry.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetHostname_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetHostname_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetHostname = _CfprApSysdebugAutoCoreFileExportTargetHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 18),
    _CfprApSysdebugAutoCoreFileExportTargetHostname_Type()
)
cfprApSysdebugAutoCoreFileExportTargetHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetHostname.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetIntId_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetIntId_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetIntId = _CfprApSysdebugAutoCoreFileExportTargetIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 19),
    _CfprApSysdebugAutoCoreFileExportTargetIntId_Type()
)
cfprApSysdebugAutoCoreFileExportTargetIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetIntId.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetName_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetName_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetName = _CfprApSysdebugAutoCoreFileExportTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 20),
    _CfprApSysdebugAutoCoreFileExportTargetName_Type()
)
cfprApSysdebugAutoCoreFileExportTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetName.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetPath_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetPath_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetPath = _CfprApSysdebugAutoCoreFileExportTargetPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 21),
    _CfprApSysdebugAutoCoreFileExportTargetPath_Type()
)
cfprApSysdebugAutoCoreFileExportTargetPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetPath.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetPolicyLevel_Type = Gauge32
_CfprApSysdebugAutoCoreFileExportTargetPolicyLevel_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetPolicyLevel = _CfprApSysdebugAutoCoreFileExportTargetPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 22),
    _CfprApSysdebugAutoCoreFileExportTargetPolicyLevel_Type()
)
cfprApSysdebugAutoCoreFileExportTargetPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetPolicyLevel.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApSysdebugAutoCoreFileExportTargetPolicyOwner_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetPolicyOwner = _CfprApSysdebugAutoCoreFileExportTargetPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 23),
    _CfprApSysdebugAutoCoreFileExportTargetPolicyOwner_Type()
)
cfprApSysdebugAutoCoreFileExportTargetPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetPolicyOwner.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetPort_Type = Gauge32
_CfprApSysdebugAutoCoreFileExportTargetPort_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetPort = _CfprApSysdebugAutoCoreFileExportTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 24),
    _CfprApSysdebugAutoCoreFileExportTargetPort_Type()
)
cfprApSysdebugAutoCoreFileExportTargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetPort.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetPostAction_Type = CfprApSysfileExporterPostAction
_CfprApSysdebugAutoCoreFileExportTargetPostAction_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetPostAction = _CfprApSysdebugAutoCoreFileExportTargetPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 25),
    _CfprApSysdebugAutoCoreFileExportTargetPostAction_Type()
)
cfprApSysdebugAutoCoreFileExportTargetPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetPostAction.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetProto_Type = CfprApSysdebugAutoCoreFileExportTargetProto
_CfprApSysdebugAutoCoreFileExportTargetProto_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetProto = _CfprApSysdebugAutoCoreFileExportTargetProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 1, 1, 26),
    _CfprApSysdebugAutoCoreFileExportTargetProto_Type()
)
cfprApSysdebugAutoCoreFileExportTargetProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetProto.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmTable_Object = MibTable
cfprApSysdebugAutoCoreFileExportTargetFsmTable = _CfprApSysdebugAutoCoreFileExportTargetFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2)
)
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmTable.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmEntry_Object = MibTableRow
cfprApSysdebugAutoCoreFileExportTargetFsmEntry = _CfprApSysdebugAutoCoreFileExportTargetFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2, 1)
)
cfprApSysdebugAutoCoreFileExportTargetFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugAutoCoreFileExportTargetFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmEntry.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugAutoCoreFileExportTargetFsmInstanceId_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmInstanceId = _CfprApSysdebugAutoCoreFileExportTargetFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2, 1, 1),
    _CfprApSysdebugAutoCoreFileExportTargetFsmInstanceId_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmInstanceId.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmDn_Type = CfprApManagedObjectDn
_CfprApSysdebugAutoCoreFileExportTargetFsmDn_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmDn = _CfprApSysdebugAutoCoreFileExportTargetFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2, 1, 2),
    _CfprApSysdebugAutoCoreFileExportTargetFsmDn_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmDn.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmRn_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetFsmRn_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmRn = _CfprApSysdebugAutoCoreFileExportTargetFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2, 1, 3),
    _CfprApSysdebugAutoCoreFileExportTargetFsmRn_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmRn.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmCompletionTime_Type = DateAndTime
_CfprApSysdebugAutoCoreFileExportTargetFsmCompletionTime_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmCompletionTime = _CfprApSysdebugAutoCoreFileExportTargetFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2, 1, 4),
    _CfprApSysdebugAutoCoreFileExportTargetFsmCompletionTime_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmCompletionTime.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmCurrentFsm_Type = CfprApSysdebugAutoCoreFileExportTargetFsmCurrentFsm
_CfprApSysdebugAutoCoreFileExportTargetFsmCurrentFsm_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmCurrentFsm = _CfprApSysdebugAutoCoreFileExportTargetFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2, 1, 5),
    _CfprApSysdebugAutoCoreFileExportTargetFsmCurrentFsm_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmCurrentFsm.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmDescrData_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetFsmDescrData_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmDescrData = _CfprApSysdebugAutoCoreFileExportTargetFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2, 1, 6),
    _CfprApSysdebugAutoCoreFileExportTargetFsmDescrData_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmDescrData.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysdebugAutoCoreFileExportTargetFsmFsmStatus_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmFsmStatus = _CfprApSysdebugAutoCoreFileExportTargetFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2, 1, 7),
    _CfprApSysdebugAutoCoreFileExportTargetFsmFsmStatus_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmFsmStatus.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmProgress_Type = Gauge32
_CfprApSysdebugAutoCoreFileExportTargetFsmProgress_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmProgress = _CfprApSysdebugAutoCoreFileExportTargetFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2, 1, 8),
    _CfprApSysdebugAutoCoreFileExportTargetFsmProgress_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmProgress.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmRmtErrCode_Type = Gauge32
_CfprApSysdebugAutoCoreFileExportTargetFsmRmtErrCode_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmRmtErrCode = _CfprApSysdebugAutoCoreFileExportTargetFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2, 1, 9),
    _CfprApSysdebugAutoCoreFileExportTargetFsmRmtErrCode_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmRmtErrCode.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetFsmRmtErrDescr_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmRmtErrDescr = _CfprApSysdebugAutoCoreFileExportTargetFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2, 1, 10),
    _CfprApSysdebugAutoCoreFileExportTargetFsmRmtErrDescr_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmRmtErrDescr.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysdebugAutoCoreFileExportTargetFsmRmtRslt_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmRmtRslt = _CfprApSysdebugAutoCoreFileExportTargetFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 2, 1, 11),
    _CfprApSysdebugAutoCoreFileExportTargetFsmRmtRslt_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmRmtRslt.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStageTable_Object = MibTable
cfprApSysdebugAutoCoreFileExportTargetFsmStageTable = _CfprApSysdebugAutoCoreFileExportTargetFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 3)
)
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStageTable.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStageEntry_Object = MibTableRow
cfprApSysdebugAutoCoreFileExportTargetFsmStageEntry = _CfprApSysdebugAutoCoreFileExportTargetFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 3, 1)
)
cfprApSysdebugAutoCoreFileExportTargetFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugAutoCoreFileExportTargetFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStageEntry.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugAutoCoreFileExportTargetFsmStageInstanceId_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmStageInstanceId = _CfprApSysdebugAutoCoreFileExportTargetFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 3, 1, 1),
    _CfprApSysdebugAutoCoreFileExportTargetFsmStageInstanceId_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStageInstanceId.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSysdebugAutoCoreFileExportTargetFsmStageDn_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmStageDn = _CfprApSysdebugAutoCoreFileExportTargetFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 3, 1, 2),
    _CfprApSysdebugAutoCoreFileExportTargetFsmStageDn_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStageDn.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStageRn_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetFsmStageRn_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmStageRn = _CfprApSysdebugAutoCoreFileExportTargetFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 3, 1, 3),
    _CfprApSysdebugAutoCoreFileExportTargetFsmStageRn_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStageRn.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStageDescrData_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetFsmStageDescrData_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmStageDescrData = _CfprApSysdebugAutoCoreFileExportTargetFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 3, 1, 4),
    _CfprApSysdebugAutoCoreFileExportTargetFsmStageDescrData_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStageDescrData.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime = _CfprApSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 3, 1, 5),
    _CfprApSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStageName_Type = CfprApSysdebugAutoCoreFileExportTargetFsmStageName
_CfprApSysdebugAutoCoreFileExportTargetFsmStageName_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmStageName = _CfprApSysdebugAutoCoreFileExportTargetFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 3, 1, 6),
    _CfprApSysdebugAutoCoreFileExportTargetFsmStageName_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStageName.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStageOrder_Type = Gauge32
_CfprApSysdebugAutoCoreFileExportTargetFsmStageOrder_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmStageOrder = _CfprApSysdebugAutoCoreFileExportTargetFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 3, 1, 7),
    _CfprApSysdebugAutoCoreFileExportTargetFsmStageOrder_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStageOrder.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStageRetry_Type = Gauge32
_CfprApSysdebugAutoCoreFileExportTargetFsmStageRetry_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmStageRetry = _CfprApSysdebugAutoCoreFileExportTargetFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 3, 1, 8),
    _CfprApSysdebugAutoCoreFileExportTargetFsmStageRetry_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStageRetry.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysdebugAutoCoreFileExportTargetFsmStageStageStatus_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmStageStageStatus = _CfprApSysdebugAutoCoreFileExportTargetFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 3, 1, 9),
    _CfprApSysdebugAutoCoreFileExportTargetFsmStageStageStatus_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmStageStageStatus.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskTable_Object = MibTable
cfprApSysdebugAutoCoreFileExportTargetFsmTaskTable = _CfprApSysdebugAutoCoreFileExportTargetFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 4)
)
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmTaskTable.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskEntry_Object = MibTableRow
cfprApSysdebugAutoCoreFileExportTargetFsmTaskEntry = _CfprApSysdebugAutoCoreFileExportTargetFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 4, 1)
)
cfprApSysdebugAutoCoreFileExportTargetFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugAutoCoreFileExportTargetFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmTaskEntry.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskInstanceId_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmTaskInstanceId = _CfprApSysdebugAutoCoreFileExportTargetFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 4, 1, 1),
    _CfprApSysdebugAutoCoreFileExportTargetFsmTaskInstanceId_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmTaskInstanceId.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskDn_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmTaskDn = _CfprApSysdebugAutoCoreFileExportTargetFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 4, 1, 2),
    _CfprApSysdebugAutoCoreFileExportTargetFsmTaskDn_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmTaskDn.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskRn_Type = SnmpAdminString
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskRn_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmTaskRn = _CfprApSysdebugAutoCoreFileExportTargetFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 4, 1, 3),
    _CfprApSysdebugAutoCoreFileExportTargetFsmTaskRn_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmTaskRn.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskCompletion_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmTaskCompletion = _CfprApSysdebugAutoCoreFileExportTargetFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 4, 1, 4),
    _CfprApSysdebugAutoCoreFileExportTargetFsmTaskCompletion_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmTaskCompletion.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskFlags_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmTaskFlags = _CfprApSysdebugAutoCoreFileExportTargetFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 4, 1, 5),
    _CfprApSysdebugAutoCoreFileExportTargetFsmTaskFlags_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmTaskFlags.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskItem_Type = CfprApSysdebugAutoCoreFileExportTargetFsmTaskItem
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskItem_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmTaskItem = _CfprApSysdebugAutoCoreFileExportTargetFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 4, 1, 6),
    _CfprApSysdebugAutoCoreFileExportTargetFsmTaskItem_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmTaskItem.setStatus("current")
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskSeqId_Type = Gauge32
_CfprApSysdebugAutoCoreFileExportTargetFsmTaskSeqId_Object = MibTableColumn
cfprApSysdebugAutoCoreFileExportTargetFsmTaskSeqId = _CfprApSysdebugAutoCoreFileExportTargetFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 4, 1, 7),
    _CfprApSysdebugAutoCoreFileExportTargetFsmTaskSeqId_Type()
)
cfprApSysdebugAutoCoreFileExportTargetFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugAutoCoreFileExportTargetFsmTaskSeqId.setStatus("current")
_CfprApSysdebugBackupBehaviorTable_Object = MibTable
cfprApSysdebugBackupBehaviorTable = _CfprApSysdebugBackupBehaviorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5)
)
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorTable.setStatus("current")
_CfprApSysdebugBackupBehaviorEntry_Object = MibTableRow
cfprApSysdebugBackupBehaviorEntry = _CfprApSysdebugBackupBehaviorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1)
)
cfprApSysdebugBackupBehaviorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugBackupBehaviorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorEntry.setStatus("current")
_CfprApSysdebugBackupBehaviorInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugBackupBehaviorInstanceId_Object = MibTableColumn
cfprApSysdebugBackupBehaviorInstanceId = _CfprApSysdebugBackupBehaviorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1, 1),
    _CfprApSysdebugBackupBehaviorInstanceId_Type()
)
cfprApSysdebugBackupBehaviorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorInstanceId.setStatus("current")
_CfprApSysdebugBackupBehaviorDn_Type = CfprApManagedObjectDn
_CfprApSysdebugBackupBehaviorDn_Object = MibTableColumn
cfprApSysdebugBackupBehaviorDn = _CfprApSysdebugBackupBehaviorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1, 2),
    _CfprApSysdebugBackupBehaviorDn_Type()
)
cfprApSysdebugBackupBehaviorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorDn.setStatus("current")
_CfprApSysdebugBackupBehaviorRn_Type = SnmpAdminString
_CfprApSysdebugBackupBehaviorRn_Object = MibTableColumn
cfprApSysdebugBackupBehaviorRn = _CfprApSysdebugBackupBehaviorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1, 3),
    _CfprApSysdebugBackupBehaviorRn_Type()
)
cfprApSysdebugBackupBehaviorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorRn.setStatus("current")
_CfprApSysdebugBackupBehaviorAction_Type = CfprApSysdebugEpLogBackupAction
_CfprApSysdebugBackupBehaviorAction_Object = MibTableColumn
cfprApSysdebugBackupBehaviorAction = _CfprApSysdebugBackupBehaviorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1, 4),
    _CfprApSysdebugBackupBehaviorAction_Type()
)
cfprApSysdebugBackupBehaviorAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorAction.setStatus("current")
_CfprApSysdebugBackupBehaviorClearOnBackup_Type = TruthValue
_CfprApSysdebugBackupBehaviorClearOnBackup_Object = MibTableColumn
cfprApSysdebugBackupBehaviorClearOnBackup = _CfprApSysdebugBackupBehaviorClearOnBackup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1, 5),
    _CfprApSysdebugBackupBehaviorClearOnBackup_Type()
)
cfprApSysdebugBackupBehaviorClearOnBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorClearOnBackup.setStatus("current")
_CfprApSysdebugBackupBehaviorFormat_Type = CfprApSysdebugBackupFormat
_CfprApSysdebugBackupBehaviorFormat_Object = MibTableColumn
cfprApSysdebugBackupBehaviorFormat = _CfprApSysdebugBackupBehaviorFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1, 6),
    _CfprApSysdebugBackupBehaviorFormat_Type()
)
cfprApSysdebugBackupBehaviorFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorFormat.setStatus("current")
_CfprApSysdebugBackupBehaviorHostname_Type = SnmpAdminString
_CfprApSysdebugBackupBehaviorHostname_Object = MibTableColumn
cfprApSysdebugBackupBehaviorHostname = _CfprApSysdebugBackupBehaviorHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1, 7),
    _CfprApSysdebugBackupBehaviorHostname_Type()
)
cfprApSysdebugBackupBehaviorHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorHostname.setStatus("current")
_CfprApSysdebugBackupBehaviorInterval_Type = CfprApSysdebugBackupBehaviorInterval
_CfprApSysdebugBackupBehaviorInterval_Object = MibTableColumn
cfprApSysdebugBackupBehaviorInterval = _CfprApSysdebugBackupBehaviorInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1, 8),
    _CfprApSysdebugBackupBehaviorInterval_Type()
)
cfprApSysdebugBackupBehaviorInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorInterval.setStatus("current")
_CfprApSysdebugBackupBehaviorProto_Type = CfprApSysdebugBackupBehaviorProto
_CfprApSysdebugBackupBehaviorProto_Object = MibTableColumn
cfprApSysdebugBackupBehaviorProto = _CfprApSysdebugBackupBehaviorProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1, 9),
    _CfprApSysdebugBackupBehaviorProto_Type()
)
cfprApSysdebugBackupBehaviorProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorProto.setStatus("current")
_CfprApSysdebugBackupBehaviorPwd_Type = SnmpAdminString
_CfprApSysdebugBackupBehaviorPwd_Object = MibTableColumn
cfprApSysdebugBackupBehaviorPwd = _CfprApSysdebugBackupBehaviorPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1, 10),
    _CfprApSysdebugBackupBehaviorPwd_Type()
)
cfprApSysdebugBackupBehaviorPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorPwd.setStatus("current")
_CfprApSysdebugBackupBehaviorRemotePath_Type = SnmpAdminString
_CfprApSysdebugBackupBehaviorRemotePath_Object = MibTableColumn
cfprApSysdebugBackupBehaviorRemotePath = _CfprApSysdebugBackupBehaviorRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1, 11),
    _CfprApSysdebugBackupBehaviorRemotePath_Type()
)
cfprApSysdebugBackupBehaviorRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorRemotePath.setStatus("current")
_CfprApSysdebugBackupBehaviorUser_Type = SnmpAdminString
_CfprApSysdebugBackupBehaviorUser_Object = MibTableColumn
cfprApSysdebugBackupBehaviorUser = _CfprApSysdebugBackupBehaviorUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 5, 1, 12),
    _CfprApSysdebugBackupBehaviorUser_Type()
)
cfprApSysdebugBackupBehaviorUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugBackupBehaviorUser.setStatus("current")
_CfprApSysdebugCoreTable_Object = MibTable
cfprApSysdebugCoreTable = _CfprApSysdebugCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6)
)
if mibBuilder.loadTexts:
    cfprApSysdebugCoreTable.setStatus("current")
_CfprApSysdebugCoreEntry_Object = MibTableRow
cfprApSysdebugCoreEntry = _CfprApSysdebugCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1)
)
cfprApSysdebugCoreEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugCoreInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugCoreEntry.setStatus("current")
_CfprApSysdebugCoreInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugCoreInstanceId_Object = MibTableColumn
cfprApSysdebugCoreInstanceId = _CfprApSysdebugCoreInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 1),
    _CfprApSysdebugCoreInstanceId_Type()
)
cfprApSysdebugCoreInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreInstanceId.setStatus("current")
_CfprApSysdebugCoreDn_Type = CfprApManagedObjectDn
_CfprApSysdebugCoreDn_Object = MibTableColumn
cfprApSysdebugCoreDn = _CfprApSysdebugCoreDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 2),
    _CfprApSysdebugCoreDn_Type()
)
cfprApSysdebugCoreDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreDn.setStatus("current")
_CfprApSysdebugCoreRn_Type = SnmpAdminString
_CfprApSysdebugCoreRn_Object = MibTableColumn
cfprApSysdebugCoreRn = _CfprApSysdebugCoreRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 3),
    _CfprApSysdebugCoreRn_Type()
)
cfprApSysdebugCoreRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreRn.setStatus("current")
_CfprApSysdebugCoreAdminState_Type = CfprApSysdebugCoreFileAdminState
_CfprApSysdebugCoreAdminState_Object = MibTableColumn
cfprApSysdebugCoreAdminState = _CfprApSysdebugCoreAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 4),
    _CfprApSysdebugCoreAdminState_Type()
)
cfprApSysdebugCoreAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreAdminState.setStatus("current")
_CfprApSysdebugCoreDescr_Type = SnmpAdminString
_CfprApSysdebugCoreDescr_Object = MibTableColumn
cfprApSysdebugCoreDescr = _CfprApSysdebugCoreDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 5),
    _CfprApSysdebugCoreDescr_Type()
)
cfprApSysdebugCoreDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreDescr.setStatus("current")
_CfprApSysdebugCoreFsmDescr_Type = SnmpAdminString
_CfprApSysdebugCoreFsmDescr_Object = MibTableColumn
cfprApSysdebugCoreFsmDescr = _CfprApSysdebugCoreFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 6),
    _CfprApSysdebugCoreFsmDescr_Type()
)
cfprApSysdebugCoreFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmDescr.setStatus("current")
_CfprApSysdebugCoreFsmPrev_Type = SnmpAdminString
_CfprApSysdebugCoreFsmPrev_Object = MibTableColumn
cfprApSysdebugCoreFsmPrev = _CfprApSysdebugCoreFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 7),
    _CfprApSysdebugCoreFsmPrev_Type()
)
cfprApSysdebugCoreFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmPrev.setStatus("current")
_CfprApSysdebugCoreFsmProgr_Type = Gauge32
_CfprApSysdebugCoreFsmProgr_Object = MibTableColumn
cfprApSysdebugCoreFsmProgr = _CfprApSysdebugCoreFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 8),
    _CfprApSysdebugCoreFsmProgr_Type()
)
cfprApSysdebugCoreFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmProgr.setStatus("current")
_CfprApSysdebugCoreFsmRmtInvErrCode_Type = Gauge32
_CfprApSysdebugCoreFsmRmtInvErrCode_Object = MibTableColumn
cfprApSysdebugCoreFsmRmtInvErrCode = _CfprApSysdebugCoreFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 9),
    _CfprApSysdebugCoreFsmRmtInvErrCode_Type()
)
cfprApSysdebugCoreFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmRmtInvErrCode.setStatus("current")
_CfprApSysdebugCoreFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSysdebugCoreFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSysdebugCoreFsmRmtInvErrDescr = _CfprApSysdebugCoreFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 10),
    _CfprApSysdebugCoreFsmRmtInvErrDescr_Type()
)
cfprApSysdebugCoreFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmRmtInvErrDescr.setStatus("current")
_CfprApSysdebugCoreFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysdebugCoreFsmRmtInvRslt_Object = MibTableColumn
cfprApSysdebugCoreFsmRmtInvRslt = _CfprApSysdebugCoreFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 11),
    _CfprApSysdebugCoreFsmRmtInvRslt_Type()
)
cfprApSysdebugCoreFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmRmtInvRslt.setStatus("current")
_CfprApSysdebugCoreFsmStageDescr_Type = SnmpAdminString
_CfprApSysdebugCoreFsmStageDescr_Object = MibTableColumn
cfprApSysdebugCoreFsmStageDescr = _CfprApSysdebugCoreFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 12),
    _CfprApSysdebugCoreFsmStageDescr_Type()
)
cfprApSysdebugCoreFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStageDescr.setStatus("current")
_CfprApSysdebugCoreFsmStamp_Type = DateAndTime
_CfprApSysdebugCoreFsmStamp_Object = MibTableColumn
cfprApSysdebugCoreFsmStamp = _CfprApSysdebugCoreFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 13),
    _CfprApSysdebugCoreFsmStamp_Type()
)
cfprApSysdebugCoreFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStamp.setStatus("current")
_CfprApSysdebugCoreFsmStatus_Type = SnmpAdminString
_CfprApSysdebugCoreFsmStatus_Object = MibTableColumn
cfprApSysdebugCoreFsmStatus = _CfprApSysdebugCoreFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 14),
    _CfprApSysdebugCoreFsmStatus_Type()
)
cfprApSysdebugCoreFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStatus.setStatus("current")
_CfprApSysdebugCoreFsmTry_Type = Gauge32
_CfprApSysdebugCoreFsmTry_Object = MibTableColumn
cfprApSysdebugCoreFsmTry = _CfprApSysdebugCoreFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 15),
    _CfprApSysdebugCoreFsmTry_Type()
)
cfprApSysdebugCoreFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmTry.setStatus("current")
_CfprApSysdebugCoreName_Type = SnmpAdminString
_CfprApSysdebugCoreName_Object = MibTableColumn
cfprApSysdebugCoreName = _CfprApSysdebugCoreName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 16),
    _CfprApSysdebugCoreName_Type()
)
cfprApSysdebugCoreName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreName.setStatus("current")
_CfprApSysdebugCoreOperState_Type = CfprApSysdebugCoreFileOperState
_CfprApSysdebugCoreOperState_Object = MibTableColumn
cfprApSysdebugCoreOperState = _CfprApSysdebugCoreOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 17),
    _CfprApSysdebugCoreOperState_Type()
)
cfprApSysdebugCoreOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreOperState.setStatus("current")
_CfprApSysdebugCoreSize_Type = Gauge32
_CfprApSysdebugCoreSize_Object = MibTableColumn
cfprApSysdebugCoreSize = _CfprApSysdebugCoreSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 18),
    _CfprApSysdebugCoreSize_Type()
)
cfprApSysdebugCoreSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreSize.setStatus("current")
_CfprApSysdebugCoreSwitchId_Type = CfprApNetworkSwitchId
_CfprApSysdebugCoreSwitchId_Object = MibTableColumn
cfprApSysdebugCoreSwitchId = _CfprApSysdebugCoreSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 19),
    _CfprApSysdebugCoreSwitchId_Type()
)
cfprApSysdebugCoreSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreSwitchId.setStatus("current")
_CfprApSysdebugCoreTs_Type = DateAndTime
_CfprApSysdebugCoreTs_Object = MibTableColumn
cfprApSysdebugCoreTs = _CfprApSysdebugCoreTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 20),
    _CfprApSysdebugCoreTs_Type()
)
cfprApSysdebugCoreTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreTs.setStatus("current")
_CfprApSysdebugCoreUri_Type = SnmpAdminString
_CfprApSysdebugCoreUri_Object = MibTableColumn
cfprApSysdebugCoreUri = _CfprApSysdebugCoreUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 6, 1, 21),
    _CfprApSysdebugCoreUri_Type()
)
cfprApSysdebugCoreUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreUri.setStatus("current")
_CfprApSysdebugCoreFileRepositoryTable_Object = MibTable
cfprApSysdebugCoreFileRepositoryTable = _CfprApSysdebugCoreFileRepositoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 7)
)
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFileRepositoryTable.setStatus("current")
_CfprApSysdebugCoreFileRepositoryEntry_Object = MibTableRow
cfprApSysdebugCoreFileRepositoryEntry = _CfprApSysdebugCoreFileRepositoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 7, 1)
)
cfprApSysdebugCoreFileRepositoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugCoreFileRepositoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFileRepositoryEntry.setStatus("current")
_CfprApSysdebugCoreFileRepositoryInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugCoreFileRepositoryInstanceId_Object = MibTableColumn
cfprApSysdebugCoreFileRepositoryInstanceId = _CfprApSysdebugCoreFileRepositoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 7, 1, 1),
    _CfprApSysdebugCoreFileRepositoryInstanceId_Type()
)
cfprApSysdebugCoreFileRepositoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFileRepositoryInstanceId.setStatus("current")
_CfprApSysdebugCoreFileRepositoryDn_Type = CfprApManagedObjectDn
_CfprApSysdebugCoreFileRepositoryDn_Object = MibTableColumn
cfprApSysdebugCoreFileRepositoryDn = _CfprApSysdebugCoreFileRepositoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 7, 1, 2),
    _CfprApSysdebugCoreFileRepositoryDn_Type()
)
cfprApSysdebugCoreFileRepositoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFileRepositoryDn.setStatus("current")
_CfprApSysdebugCoreFileRepositoryRn_Type = SnmpAdminString
_CfprApSysdebugCoreFileRepositoryRn_Object = MibTableColumn
cfprApSysdebugCoreFileRepositoryRn = _CfprApSysdebugCoreFileRepositoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 7, 1, 3),
    _CfprApSysdebugCoreFileRepositoryRn_Type()
)
cfprApSysdebugCoreFileRepositoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFileRepositoryRn.setStatus("current")
_CfprApSysdebugCoreFsmTable_Object = MibTable
cfprApSysdebugCoreFsmTable = _CfprApSysdebugCoreFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8)
)
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmTable.setStatus("current")
_CfprApSysdebugCoreFsmEntry_Object = MibTableRow
cfprApSysdebugCoreFsmEntry = _CfprApSysdebugCoreFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8, 1)
)
cfprApSysdebugCoreFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugCoreFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmEntry.setStatus("current")
_CfprApSysdebugCoreFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugCoreFsmInstanceId_Object = MibTableColumn
cfprApSysdebugCoreFsmInstanceId = _CfprApSysdebugCoreFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8, 1, 1),
    _CfprApSysdebugCoreFsmInstanceId_Type()
)
cfprApSysdebugCoreFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmInstanceId.setStatus("current")
_CfprApSysdebugCoreFsmDn_Type = CfprApManagedObjectDn
_CfprApSysdebugCoreFsmDn_Object = MibTableColumn
cfprApSysdebugCoreFsmDn = _CfprApSysdebugCoreFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8, 1, 2),
    _CfprApSysdebugCoreFsmDn_Type()
)
cfprApSysdebugCoreFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmDn.setStatus("current")
_CfprApSysdebugCoreFsmRn_Type = SnmpAdminString
_CfprApSysdebugCoreFsmRn_Object = MibTableColumn
cfprApSysdebugCoreFsmRn = _CfprApSysdebugCoreFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8, 1, 3),
    _CfprApSysdebugCoreFsmRn_Type()
)
cfprApSysdebugCoreFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmRn.setStatus("current")
_CfprApSysdebugCoreFsmCompletionTime_Type = DateAndTime
_CfprApSysdebugCoreFsmCompletionTime_Object = MibTableColumn
cfprApSysdebugCoreFsmCompletionTime = _CfprApSysdebugCoreFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8, 1, 4),
    _CfprApSysdebugCoreFsmCompletionTime_Type()
)
cfprApSysdebugCoreFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmCompletionTime.setStatus("current")
_CfprApSysdebugCoreFsmCurrentFsm_Type = CfprApSysdebugCoreFsmCurrentFsm
_CfprApSysdebugCoreFsmCurrentFsm_Object = MibTableColumn
cfprApSysdebugCoreFsmCurrentFsm = _CfprApSysdebugCoreFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8, 1, 5),
    _CfprApSysdebugCoreFsmCurrentFsm_Type()
)
cfprApSysdebugCoreFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmCurrentFsm.setStatus("current")
_CfprApSysdebugCoreFsmDescrData_Type = SnmpAdminString
_CfprApSysdebugCoreFsmDescrData_Object = MibTableColumn
cfprApSysdebugCoreFsmDescrData = _CfprApSysdebugCoreFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8, 1, 6),
    _CfprApSysdebugCoreFsmDescrData_Type()
)
cfprApSysdebugCoreFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmDescrData.setStatus("current")
_CfprApSysdebugCoreFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysdebugCoreFsmFsmStatus_Object = MibTableColumn
cfprApSysdebugCoreFsmFsmStatus = _CfprApSysdebugCoreFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8, 1, 7),
    _CfprApSysdebugCoreFsmFsmStatus_Type()
)
cfprApSysdebugCoreFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmFsmStatus.setStatus("current")
_CfprApSysdebugCoreFsmProgress_Type = Gauge32
_CfprApSysdebugCoreFsmProgress_Object = MibTableColumn
cfprApSysdebugCoreFsmProgress = _CfprApSysdebugCoreFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8, 1, 8),
    _CfprApSysdebugCoreFsmProgress_Type()
)
cfprApSysdebugCoreFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmProgress.setStatus("current")
_CfprApSysdebugCoreFsmRmtErrCode_Type = Gauge32
_CfprApSysdebugCoreFsmRmtErrCode_Object = MibTableColumn
cfprApSysdebugCoreFsmRmtErrCode = _CfprApSysdebugCoreFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8, 1, 9),
    _CfprApSysdebugCoreFsmRmtErrCode_Type()
)
cfprApSysdebugCoreFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmRmtErrCode.setStatus("current")
_CfprApSysdebugCoreFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSysdebugCoreFsmRmtErrDescr_Object = MibTableColumn
cfprApSysdebugCoreFsmRmtErrDescr = _CfprApSysdebugCoreFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8, 1, 10),
    _CfprApSysdebugCoreFsmRmtErrDescr_Type()
)
cfprApSysdebugCoreFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmRmtErrDescr.setStatus("current")
_CfprApSysdebugCoreFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysdebugCoreFsmRmtRslt_Object = MibTableColumn
cfprApSysdebugCoreFsmRmtRslt = _CfprApSysdebugCoreFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 8, 1, 11),
    _CfprApSysdebugCoreFsmRmtRslt_Type()
)
cfprApSysdebugCoreFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmRmtRslt.setStatus("current")
_CfprApSysdebugCoreFsmStageTable_Object = MibTable
cfprApSysdebugCoreFsmStageTable = _CfprApSysdebugCoreFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 9)
)
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStageTable.setStatus("current")
_CfprApSysdebugCoreFsmStageEntry_Object = MibTableRow
cfprApSysdebugCoreFsmStageEntry = _CfprApSysdebugCoreFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 9, 1)
)
cfprApSysdebugCoreFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugCoreFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStageEntry.setStatus("current")
_CfprApSysdebugCoreFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugCoreFsmStageInstanceId_Object = MibTableColumn
cfprApSysdebugCoreFsmStageInstanceId = _CfprApSysdebugCoreFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 9, 1, 1),
    _CfprApSysdebugCoreFsmStageInstanceId_Type()
)
cfprApSysdebugCoreFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStageInstanceId.setStatus("current")
_CfprApSysdebugCoreFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSysdebugCoreFsmStageDn_Object = MibTableColumn
cfprApSysdebugCoreFsmStageDn = _CfprApSysdebugCoreFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 9, 1, 2),
    _CfprApSysdebugCoreFsmStageDn_Type()
)
cfprApSysdebugCoreFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStageDn.setStatus("current")
_CfprApSysdebugCoreFsmStageRn_Type = SnmpAdminString
_CfprApSysdebugCoreFsmStageRn_Object = MibTableColumn
cfprApSysdebugCoreFsmStageRn = _CfprApSysdebugCoreFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 9, 1, 3),
    _CfprApSysdebugCoreFsmStageRn_Type()
)
cfprApSysdebugCoreFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStageRn.setStatus("current")
_CfprApSysdebugCoreFsmStageDescrData_Type = SnmpAdminString
_CfprApSysdebugCoreFsmStageDescrData_Object = MibTableColumn
cfprApSysdebugCoreFsmStageDescrData = _CfprApSysdebugCoreFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 9, 1, 4),
    _CfprApSysdebugCoreFsmStageDescrData_Type()
)
cfprApSysdebugCoreFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStageDescrData.setStatus("current")
_CfprApSysdebugCoreFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSysdebugCoreFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSysdebugCoreFsmStageLastUpdateTime = _CfprApSysdebugCoreFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 9, 1, 5),
    _CfprApSysdebugCoreFsmStageLastUpdateTime_Type()
)
cfprApSysdebugCoreFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStageLastUpdateTime.setStatus("current")
_CfprApSysdebugCoreFsmStageName_Type = CfprApSysdebugCoreFsmStageName
_CfprApSysdebugCoreFsmStageName_Object = MibTableColumn
cfprApSysdebugCoreFsmStageName = _CfprApSysdebugCoreFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 9, 1, 6),
    _CfprApSysdebugCoreFsmStageName_Type()
)
cfprApSysdebugCoreFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStageName.setStatus("current")
_CfprApSysdebugCoreFsmStageOrder_Type = Gauge32
_CfprApSysdebugCoreFsmStageOrder_Object = MibTableColumn
cfprApSysdebugCoreFsmStageOrder = _CfprApSysdebugCoreFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 9, 1, 7),
    _CfprApSysdebugCoreFsmStageOrder_Type()
)
cfprApSysdebugCoreFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStageOrder.setStatus("current")
_CfprApSysdebugCoreFsmStageRetry_Type = Gauge32
_CfprApSysdebugCoreFsmStageRetry_Object = MibTableColumn
cfprApSysdebugCoreFsmStageRetry = _CfprApSysdebugCoreFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 9, 1, 8),
    _CfprApSysdebugCoreFsmStageRetry_Type()
)
cfprApSysdebugCoreFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStageRetry.setStatus("current")
_CfprApSysdebugCoreFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysdebugCoreFsmStageStageStatus_Object = MibTableColumn
cfprApSysdebugCoreFsmStageStageStatus = _CfprApSysdebugCoreFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 9, 1, 9),
    _CfprApSysdebugCoreFsmStageStageStatus_Type()
)
cfprApSysdebugCoreFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmStageStageStatus.setStatus("current")
_CfprApSysdebugCoreFsmTaskTable_Object = MibTable
cfprApSysdebugCoreFsmTaskTable = _CfprApSysdebugCoreFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 10)
)
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmTaskTable.setStatus("current")
_CfprApSysdebugCoreFsmTaskEntry_Object = MibTableRow
cfprApSysdebugCoreFsmTaskEntry = _CfprApSysdebugCoreFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 10, 1)
)
cfprApSysdebugCoreFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugCoreFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmTaskEntry.setStatus("current")
_CfprApSysdebugCoreFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugCoreFsmTaskInstanceId_Object = MibTableColumn
cfprApSysdebugCoreFsmTaskInstanceId = _CfprApSysdebugCoreFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 10, 1, 1),
    _CfprApSysdebugCoreFsmTaskInstanceId_Type()
)
cfprApSysdebugCoreFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmTaskInstanceId.setStatus("current")
_CfprApSysdebugCoreFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSysdebugCoreFsmTaskDn_Object = MibTableColumn
cfprApSysdebugCoreFsmTaskDn = _CfprApSysdebugCoreFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 10, 1, 2),
    _CfprApSysdebugCoreFsmTaskDn_Type()
)
cfprApSysdebugCoreFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmTaskDn.setStatus("current")
_CfprApSysdebugCoreFsmTaskRn_Type = SnmpAdminString
_CfprApSysdebugCoreFsmTaskRn_Object = MibTableColumn
cfprApSysdebugCoreFsmTaskRn = _CfprApSysdebugCoreFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 10, 1, 3),
    _CfprApSysdebugCoreFsmTaskRn_Type()
)
cfprApSysdebugCoreFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmTaskRn.setStatus("current")
_CfprApSysdebugCoreFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSysdebugCoreFsmTaskCompletion_Object = MibTableColumn
cfprApSysdebugCoreFsmTaskCompletion = _CfprApSysdebugCoreFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 10, 1, 4),
    _CfprApSysdebugCoreFsmTaskCompletion_Type()
)
cfprApSysdebugCoreFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmTaskCompletion.setStatus("current")
_CfprApSysdebugCoreFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSysdebugCoreFsmTaskFlags_Object = MibTableColumn
cfprApSysdebugCoreFsmTaskFlags = _CfprApSysdebugCoreFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 10, 1, 5),
    _CfprApSysdebugCoreFsmTaskFlags_Type()
)
cfprApSysdebugCoreFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmTaskFlags.setStatus("current")
_CfprApSysdebugCoreFsmTaskItem_Type = CfprApSysdebugCoreFsmTaskItem
_CfprApSysdebugCoreFsmTaskItem_Object = MibTableColumn
cfprApSysdebugCoreFsmTaskItem = _CfprApSysdebugCoreFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 10, 1, 6),
    _CfprApSysdebugCoreFsmTaskItem_Type()
)
cfprApSysdebugCoreFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmTaskItem.setStatus("current")
_CfprApSysdebugCoreFsmTaskSeqId_Type = Gauge32
_CfprApSysdebugCoreFsmTaskSeqId_Object = MibTableColumn
cfprApSysdebugCoreFsmTaskSeqId = _CfprApSysdebugCoreFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 10, 1, 7),
    _CfprApSysdebugCoreFsmTaskSeqId_Type()
)
cfprApSysdebugCoreFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugCoreFsmTaskSeqId.setStatus("current")
_CfprApSysdebugEpTable_Object = MibTable
cfprApSysdebugEpTable = _CfprApSysdebugEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 11)
)
if mibBuilder.loadTexts:
    cfprApSysdebugEpTable.setStatus("current")
_CfprApSysdebugEpEntry_Object = MibTableRow
cfprApSysdebugEpEntry = _CfprApSysdebugEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 11, 1)
)
cfprApSysdebugEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugEpEntry.setStatus("current")
_CfprApSysdebugEpInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugEpInstanceId_Object = MibTableColumn
cfprApSysdebugEpInstanceId = _CfprApSysdebugEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 11, 1, 1),
    _CfprApSysdebugEpInstanceId_Type()
)
cfprApSysdebugEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugEpInstanceId.setStatus("current")
_CfprApSysdebugEpDn_Type = CfprApManagedObjectDn
_CfprApSysdebugEpDn_Object = MibTableColumn
cfprApSysdebugEpDn = _CfprApSysdebugEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 11, 1, 2),
    _CfprApSysdebugEpDn_Type()
)
cfprApSysdebugEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugEpDn.setStatus("current")
_CfprApSysdebugEpRn_Type = SnmpAdminString
_CfprApSysdebugEpRn_Object = MibTableColumn
cfprApSysdebugEpRn = _CfprApSysdebugEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 11, 1, 3),
    _CfprApSysdebugEpRn_Type()
)
cfprApSysdebugEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugEpRn.setStatus("current")
_CfprApSysdebugLogControlDestinationFileTable_Object = MibTable
cfprApSysdebugLogControlDestinationFileTable = _CfprApSysdebugLogControlDestinationFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 12)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationFileTable.setStatus("current")
_CfprApSysdebugLogControlDestinationFileEntry_Object = MibTableRow
cfprApSysdebugLogControlDestinationFileEntry = _CfprApSysdebugLogControlDestinationFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 12, 1)
)
cfprApSysdebugLogControlDestinationFileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogControlDestinationFileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationFileEntry.setStatus("current")
_CfprApSysdebugLogControlDestinationFileInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogControlDestinationFileInstanceId_Object = MibTableColumn
cfprApSysdebugLogControlDestinationFileInstanceId = _CfprApSysdebugLogControlDestinationFileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 12, 1, 1),
    _CfprApSysdebugLogControlDestinationFileInstanceId_Type()
)
cfprApSysdebugLogControlDestinationFileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationFileInstanceId.setStatus("current")
_CfprApSysdebugLogControlDestinationFileDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogControlDestinationFileDn_Object = MibTableColumn
cfprApSysdebugLogControlDestinationFileDn = _CfprApSysdebugLogControlDestinationFileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 12, 1, 2),
    _CfprApSysdebugLogControlDestinationFileDn_Type()
)
cfprApSysdebugLogControlDestinationFileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationFileDn.setStatus("current")
_CfprApSysdebugLogControlDestinationFileRn_Type = SnmpAdminString
_CfprApSysdebugLogControlDestinationFileRn_Object = MibTableColumn
cfprApSysdebugLogControlDestinationFileRn = _CfprApSysdebugLogControlDestinationFileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 12, 1, 3),
    _CfprApSysdebugLogControlDestinationFileRn_Type()
)
cfprApSysdebugLogControlDestinationFileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationFileRn.setStatus("current")
_CfprApSysdebugLogControlDestinationFileBackupCount_Type = Gauge32
_CfprApSysdebugLogControlDestinationFileBackupCount_Object = MibTableColumn
cfprApSysdebugLogControlDestinationFileBackupCount = _CfprApSysdebugLogControlDestinationFileBackupCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 12, 1, 4),
    _CfprApSysdebugLogControlDestinationFileBackupCount_Type()
)
cfprApSysdebugLogControlDestinationFileBackupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationFileBackupCount.setStatus("current")
_CfprApSysdebugLogControlDestinationFileDefaultLevel_Type = CfprApSysdebugLogControlLevel
_CfprApSysdebugLogControlDestinationFileDefaultLevel_Object = MibTableColumn
cfprApSysdebugLogControlDestinationFileDefaultLevel = _CfprApSysdebugLogControlDestinationFileDefaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 12, 1, 5),
    _CfprApSysdebugLogControlDestinationFileDefaultLevel_Type()
)
cfprApSysdebugLogControlDestinationFileDefaultLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationFileDefaultLevel.setStatus("current")
_CfprApSysdebugLogControlDestinationFileDefaultSize_Type = Gauge32
_CfprApSysdebugLogControlDestinationFileDefaultSize_Object = MibTableColumn
cfprApSysdebugLogControlDestinationFileDefaultSize = _CfprApSysdebugLogControlDestinationFileDefaultSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 12, 1, 6),
    _CfprApSysdebugLogControlDestinationFileDefaultSize_Type()
)
cfprApSysdebugLogControlDestinationFileDefaultSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationFileDefaultSize.setStatus("current")
_CfprApSysdebugLogControlDestinationFileLevel_Type = CfprApSysdebugLogControlLevel
_CfprApSysdebugLogControlDestinationFileLevel_Object = MibTableColumn
cfprApSysdebugLogControlDestinationFileLevel = _CfprApSysdebugLogControlDestinationFileLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 12, 1, 7),
    _CfprApSysdebugLogControlDestinationFileLevel_Type()
)
cfprApSysdebugLogControlDestinationFileLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationFileLevel.setStatus("current")
_CfprApSysdebugLogControlDestinationFileSize_Type = Gauge32
_CfprApSysdebugLogControlDestinationFileSize_Object = MibTableColumn
cfprApSysdebugLogControlDestinationFileSize = _CfprApSysdebugLogControlDestinationFileSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 12, 1, 8),
    _CfprApSysdebugLogControlDestinationFileSize_Type()
)
cfprApSysdebugLogControlDestinationFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationFileSize.setStatus("current")
_CfprApSysdebugLogControlDestinationSyslogTable_Object = MibTable
cfprApSysdebugLogControlDestinationSyslogTable = _CfprApSysdebugLogControlDestinationSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 13)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationSyslogTable.setStatus("current")
_CfprApSysdebugLogControlDestinationSyslogEntry_Object = MibTableRow
cfprApSysdebugLogControlDestinationSyslogEntry = _CfprApSysdebugLogControlDestinationSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 13, 1)
)
cfprApSysdebugLogControlDestinationSyslogEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogControlDestinationSyslogInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationSyslogEntry.setStatus("current")
_CfprApSysdebugLogControlDestinationSyslogInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogControlDestinationSyslogInstanceId_Object = MibTableColumn
cfprApSysdebugLogControlDestinationSyslogInstanceId = _CfprApSysdebugLogControlDestinationSyslogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 13, 1, 1),
    _CfprApSysdebugLogControlDestinationSyslogInstanceId_Type()
)
cfprApSysdebugLogControlDestinationSyslogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationSyslogInstanceId.setStatus("current")
_CfprApSysdebugLogControlDestinationSyslogDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogControlDestinationSyslogDn_Object = MibTableColumn
cfprApSysdebugLogControlDestinationSyslogDn = _CfprApSysdebugLogControlDestinationSyslogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 13, 1, 2),
    _CfprApSysdebugLogControlDestinationSyslogDn_Type()
)
cfprApSysdebugLogControlDestinationSyslogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationSyslogDn.setStatus("current")
_CfprApSysdebugLogControlDestinationSyslogRn_Type = SnmpAdminString
_CfprApSysdebugLogControlDestinationSyslogRn_Object = MibTableColumn
cfprApSysdebugLogControlDestinationSyslogRn = _CfprApSysdebugLogControlDestinationSyslogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 13, 1, 3),
    _CfprApSysdebugLogControlDestinationSyslogRn_Type()
)
cfprApSysdebugLogControlDestinationSyslogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationSyslogRn.setStatus("current")
_CfprApSysdebugLogControlDestinationSyslogDefaultLevel_Type = CfprApSysdebugLogControlLevel
_CfprApSysdebugLogControlDestinationSyslogDefaultLevel_Object = MibTableColumn
cfprApSysdebugLogControlDestinationSyslogDefaultLevel = _CfprApSysdebugLogControlDestinationSyslogDefaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 13, 1, 4),
    _CfprApSysdebugLogControlDestinationSyslogDefaultLevel_Type()
)
cfprApSysdebugLogControlDestinationSyslogDefaultLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationSyslogDefaultLevel.setStatus("current")
_CfprApSysdebugLogControlDestinationSyslogLevel_Type = CfprApSysdebugLogControlLevel
_CfprApSysdebugLogControlDestinationSyslogLevel_Object = MibTableColumn
cfprApSysdebugLogControlDestinationSyslogLevel = _CfprApSysdebugLogControlDestinationSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 13, 1, 5),
    _CfprApSysdebugLogControlDestinationSyslogLevel_Type()
)
cfprApSysdebugLogControlDestinationSyslogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDestinationSyslogLevel.setStatus("current")
_CfprApSysdebugLogControlDomainTable_Object = MibTable
cfprApSysdebugLogControlDomainTable = _CfprApSysdebugLogControlDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 14)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDomainTable.setStatus("current")
_CfprApSysdebugLogControlDomainEntry_Object = MibTableRow
cfprApSysdebugLogControlDomainEntry = _CfprApSysdebugLogControlDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 14, 1)
)
cfprApSysdebugLogControlDomainEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogControlDomainInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDomainEntry.setStatus("current")
_CfprApSysdebugLogControlDomainInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogControlDomainInstanceId_Object = MibTableColumn
cfprApSysdebugLogControlDomainInstanceId = _CfprApSysdebugLogControlDomainInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 14, 1, 1),
    _CfprApSysdebugLogControlDomainInstanceId_Type()
)
cfprApSysdebugLogControlDomainInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDomainInstanceId.setStatus("current")
_CfprApSysdebugLogControlDomainDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogControlDomainDn_Object = MibTableColumn
cfprApSysdebugLogControlDomainDn = _CfprApSysdebugLogControlDomainDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 14, 1, 2),
    _CfprApSysdebugLogControlDomainDn_Type()
)
cfprApSysdebugLogControlDomainDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDomainDn.setStatus("current")
_CfprApSysdebugLogControlDomainRn_Type = SnmpAdminString
_CfprApSysdebugLogControlDomainRn_Object = MibTableColumn
cfprApSysdebugLogControlDomainRn = _CfprApSysdebugLogControlDomainRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 14, 1, 3),
    _CfprApSysdebugLogControlDomainRn_Type()
)
cfprApSysdebugLogControlDomainRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDomainRn.setStatus("current")
_CfprApSysdebugLogControlDomainLevel_Type = CfprApSysdebugLogControlLevel
_CfprApSysdebugLogControlDomainLevel_Object = MibTableColumn
cfprApSysdebugLogControlDomainLevel = _CfprApSysdebugLogControlDomainLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 14, 1, 4),
    _CfprApSysdebugLogControlDomainLevel_Type()
)
cfprApSysdebugLogControlDomainLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDomainLevel.setStatus("current")
_CfprApSysdebugLogControlDomainLevelFlag_Type = TruthValue
_CfprApSysdebugLogControlDomainLevelFlag_Object = MibTableColumn
cfprApSysdebugLogControlDomainLevelFlag = _CfprApSysdebugLogControlDomainLevelFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 14, 1, 5),
    _CfprApSysdebugLogControlDomainLevelFlag_Type()
)
cfprApSysdebugLogControlDomainLevelFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDomainLevelFlag.setStatus("current")
_CfprApSysdebugLogControlDomainName_Type = CfprApSysdebugLogControlDomainEnum
_CfprApSysdebugLogControlDomainName_Object = MibTableColumn
cfprApSysdebugLogControlDomainName = _CfprApSysdebugLogControlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 14, 1, 6),
    _CfprApSysdebugLogControlDomainName_Type()
)
cfprApSysdebugLogControlDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDomainName.setStatus("current")
_CfprApSysdebugLogControlDomainPersist_Type = TruthValue
_CfprApSysdebugLogControlDomainPersist_Object = MibTableColumn
cfprApSysdebugLogControlDomainPersist = _CfprApSysdebugLogControlDomainPersist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 14, 1, 7),
    _CfprApSysdebugLogControlDomainPersist_Type()
)
cfprApSysdebugLogControlDomainPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDomainPersist.setStatus("current")
_CfprApSysdebugLogControlDomainReset_Type = TruthValue
_CfprApSysdebugLogControlDomainReset_Object = MibTableColumn
cfprApSysdebugLogControlDomainReset = _CfprApSysdebugLogControlDomainReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 14, 1, 8),
    _CfprApSysdebugLogControlDomainReset_Type()
)
cfprApSysdebugLogControlDomainReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlDomainReset.setStatus("current")
_CfprApSysdebugLogControlEpTable_Object = MibTable
cfprApSysdebugLogControlEpTable = _CfprApSysdebugLogControlEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpTable.setStatus("current")
_CfprApSysdebugLogControlEpEntry_Object = MibTableRow
cfprApSysdebugLogControlEpEntry = _CfprApSysdebugLogControlEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1)
)
cfprApSysdebugLogControlEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogControlEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpEntry.setStatus("current")
_CfprApSysdebugLogControlEpInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogControlEpInstanceId_Object = MibTableColumn
cfprApSysdebugLogControlEpInstanceId = _CfprApSysdebugLogControlEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 1),
    _CfprApSysdebugLogControlEpInstanceId_Type()
)
cfprApSysdebugLogControlEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpInstanceId.setStatus("current")
_CfprApSysdebugLogControlEpDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogControlEpDn_Object = MibTableColumn
cfprApSysdebugLogControlEpDn = _CfprApSysdebugLogControlEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 2),
    _CfprApSysdebugLogControlEpDn_Type()
)
cfprApSysdebugLogControlEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpDn.setStatus("current")
_CfprApSysdebugLogControlEpRn_Type = SnmpAdminString
_CfprApSysdebugLogControlEpRn_Object = MibTableColumn
cfprApSysdebugLogControlEpRn = _CfprApSysdebugLogControlEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 3),
    _CfprApSysdebugLogControlEpRn_Type()
)
cfprApSysdebugLogControlEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpRn.setStatus("current")
_CfprApSysdebugLogControlEpFsmDescr_Type = SnmpAdminString
_CfprApSysdebugLogControlEpFsmDescr_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmDescr = _CfprApSysdebugLogControlEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 4),
    _CfprApSysdebugLogControlEpFsmDescr_Type()
)
cfprApSysdebugLogControlEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmDescr.setStatus("current")
_CfprApSysdebugLogControlEpFsmPrev_Type = SnmpAdminString
_CfprApSysdebugLogControlEpFsmPrev_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmPrev = _CfprApSysdebugLogControlEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 5),
    _CfprApSysdebugLogControlEpFsmPrev_Type()
)
cfprApSysdebugLogControlEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmPrev.setStatus("current")
_CfprApSysdebugLogControlEpFsmProgr_Type = Gauge32
_CfprApSysdebugLogControlEpFsmProgr_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmProgr = _CfprApSysdebugLogControlEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 6),
    _CfprApSysdebugLogControlEpFsmProgr_Type()
)
cfprApSysdebugLogControlEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmProgr.setStatus("current")
_CfprApSysdebugLogControlEpFsmRmtInvErrCode_Type = Gauge32
_CfprApSysdebugLogControlEpFsmRmtInvErrCode_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmRmtInvErrCode = _CfprApSysdebugLogControlEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 7),
    _CfprApSysdebugLogControlEpFsmRmtInvErrCode_Type()
)
cfprApSysdebugLogControlEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmRmtInvErrCode.setStatus("current")
_CfprApSysdebugLogControlEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSysdebugLogControlEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmRmtInvErrDescr = _CfprApSysdebugLogControlEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 8),
    _CfprApSysdebugLogControlEpFsmRmtInvErrDescr_Type()
)
cfprApSysdebugLogControlEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmRmtInvErrDescr.setStatus("current")
_CfprApSysdebugLogControlEpFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysdebugLogControlEpFsmRmtInvRslt_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmRmtInvRslt = _CfprApSysdebugLogControlEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 9),
    _CfprApSysdebugLogControlEpFsmRmtInvRslt_Type()
)
cfprApSysdebugLogControlEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmRmtInvRslt.setStatus("current")
_CfprApSysdebugLogControlEpFsmStageDescr_Type = SnmpAdminString
_CfprApSysdebugLogControlEpFsmStageDescr_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmStageDescr = _CfprApSysdebugLogControlEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 10),
    _CfprApSysdebugLogControlEpFsmStageDescr_Type()
)
cfprApSysdebugLogControlEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStageDescr.setStatus("current")
_CfprApSysdebugLogControlEpFsmStamp_Type = DateAndTime
_CfprApSysdebugLogControlEpFsmStamp_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmStamp = _CfprApSysdebugLogControlEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 11),
    _CfprApSysdebugLogControlEpFsmStamp_Type()
)
cfprApSysdebugLogControlEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStamp.setStatus("current")
_CfprApSysdebugLogControlEpFsmStatus_Type = SnmpAdminString
_CfprApSysdebugLogControlEpFsmStatus_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmStatus = _CfprApSysdebugLogControlEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 12),
    _CfprApSysdebugLogControlEpFsmStatus_Type()
)
cfprApSysdebugLogControlEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStatus.setStatus("current")
_CfprApSysdebugLogControlEpFsmTry_Type = Gauge32
_CfprApSysdebugLogControlEpFsmTry_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmTry = _CfprApSysdebugLogControlEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 13),
    _CfprApSysdebugLogControlEpFsmTry_Type()
)
cfprApSysdebugLogControlEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmTry.setStatus("current")
_CfprApSysdebugLogControlEpLevel_Type = CfprApSysdebugLogControlLevel
_CfprApSysdebugLogControlEpLevel_Object = MibTableColumn
cfprApSysdebugLogControlEpLevel = _CfprApSysdebugLogControlEpLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 14),
    _CfprApSysdebugLogControlEpLevel_Type()
)
cfprApSysdebugLogControlEpLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpLevel.setStatus("current")
_CfprApSysdebugLogControlEpLevelFlag_Type = TruthValue
_CfprApSysdebugLogControlEpLevelFlag_Object = MibTableColumn
cfprApSysdebugLogControlEpLevelFlag = _CfprApSysdebugLogControlEpLevelFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 15),
    _CfprApSysdebugLogControlEpLevelFlag_Type()
)
cfprApSysdebugLogControlEpLevelFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpLevelFlag.setStatus("current")
_CfprApSysdebugLogControlEpPersist_Type = TruthValue
_CfprApSysdebugLogControlEpPersist_Object = MibTableColumn
cfprApSysdebugLogControlEpPersist = _CfprApSysdebugLogControlEpPersist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 16),
    _CfprApSysdebugLogControlEpPersist_Type()
)
cfprApSysdebugLogControlEpPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpPersist.setStatus("current")
_CfprApSysdebugLogControlEpReset_Type = TruthValue
_CfprApSysdebugLogControlEpReset_Object = MibTableColumn
cfprApSysdebugLogControlEpReset = _CfprApSysdebugLogControlEpReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 15, 1, 17),
    _CfprApSysdebugLogControlEpReset_Type()
)
cfprApSysdebugLogControlEpReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpReset.setStatus("current")
_CfprApSysdebugLogControlEpFsmTable_Object = MibTable
cfprApSysdebugLogControlEpFsmTable = _CfprApSysdebugLogControlEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmTable.setStatus("current")
_CfprApSysdebugLogControlEpFsmEntry_Object = MibTableRow
cfprApSysdebugLogControlEpFsmEntry = _CfprApSysdebugLogControlEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16, 1)
)
cfprApSysdebugLogControlEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogControlEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmEntry.setStatus("current")
_CfprApSysdebugLogControlEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogControlEpFsmInstanceId_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmInstanceId = _CfprApSysdebugLogControlEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16, 1, 1),
    _CfprApSysdebugLogControlEpFsmInstanceId_Type()
)
cfprApSysdebugLogControlEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmInstanceId.setStatus("current")
_CfprApSysdebugLogControlEpFsmDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogControlEpFsmDn_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmDn = _CfprApSysdebugLogControlEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16, 1, 2),
    _CfprApSysdebugLogControlEpFsmDn_Type()
)
cfprApSysdebugLogControlEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmDn.setStatus("current")
_CfprApSysdebugLogControlEpFsmRn_Type = SnmpAdminString
_CfprApSysdebugLogControlEpFsmRn_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmRn = _CfprApSysdebugLogControlEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16, 1, 3),
    _CfprApSysdebugLogControlEpFsmRn_Type()
)
cfprApSysdebugLogControlEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmRn.setStatus("current")
_CfprApSysdebugLogControlEpFsmCompletionTime_Type = DateAndTime
_CfprApSysdebugLogControlEpFsmCompletionTime_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmCompletionTime = _CfprApSysdebugLogControlEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16, 1, 4),
    _CfprApSysdebugLogControlEpFsmCompletionTime_Type()
)
cfprApSysdebugLogControlEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmCompletionTime.setStatus("current")
_CfprApSysdebugLogControlEpFsmCurrentFsm_Type = CfprApSysdebugLogControlEpFsmCurrentFsm
_CfprApSysdebugLogControlEpFsmCurrentFsm_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmCurrentFsm = _CfprApSysdebugLogControlEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16, 1, 5),
    _CfprApSysdebugLogControlEpFsmCurrentFsm_Type()
)
cfprApSysdebugLogControlEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmCurrentFsm.setStatus("current")
_CfprApSysdebugLogControlEpFsmDescrData_Type = SnmpAdminString
_CfprApSysdebugLogControlEpFsmDescrData_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmDescrData = _CfprApSysdebugLogControlEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16, 1, 6),
    _CfprApSysdebugLogControlEpFsmDescrData_Type()
)
cfprApSysdebugLogControlEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmDescrData.setStatus("current")
_CfprApSysdebugLogControlEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysdebugLogControlEpFsmFsmStatus_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmFsmStatus = _CfprApSysdebugLogControlEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16, 1, 7),
    _CfprApSysdebugLogControlEpFsmFsmStatus_Type()
)
cfprApSysdebugLogControlEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmFsmStatus.setStatus("current")
_CfprApSysdebugLogControlEpFsmProgress_Type = Gauge32
_CfprApSysdebugLogControlEpFsmProgress_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmProgress = _CfprApSysdebugLogControlEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16, 1, 8),
    _CfprApSysdebugLogControlEpFsmProgress_Type()
)
cfprApSysdebugLogControlEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmProgress.setStatus("current")
_CfprApSysdebugLogControlEpFsmRmtErrCode_Type = Gauge32
_CfprApSysdebugLogControlEpFsmRmtErrCode_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmRmtErrCode = _CfprApSysdebugLogControlEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16, 1, 9),
    _CfprApSysdebugLogControlEpFsmRmtErrCode_Type()
)
cfprApSysdebugLogControlEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmRmtErrCode.setStatus("current")
_CfprApSysdebugLogControlEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSysdebugLogControlEpFsmRmtErrDescr_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmRmtErrDescr = _CfprApSysdebugLogControlEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16, 1, 10),
    _CfprApSysdebugLogControlEpFsmRmtErrDescr_Type()
)
cfprApSysdebugLogControlEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmRmtErrDescr.setStatus("current")
_CfprApSysdebugLogControlEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysdebugLogControlEpFsmRmtRslt_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmRmtRslt = _CfprApSysdebugLogControlEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 16, 1, 11),
    _CfprApSysdebugLogControlEpFsmRmtRslt_Type()
)
cfprApSysdebugLogControlEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmRmtRslt.setStatus("current")
_CfprApSysdebugLogControlEpFsmStageTable_Object = MibTable
cfprApSysdebugLogControlEpFsmStageTable = _CfprApSysdebugLogControlEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 17)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStageTable.setStatus("current")
_CfprApSysdebugLogControlEpFsmStageEntry_Object = MibTableRow
cfprApSysdebugLogControlEpFsmStageEntry = _CfprApSysdebugLogControlEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 17, 1)
)
cfprApSysdebugLogControlEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogControlEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStageEntry.setStatus("current")
_CfprApSysdebugLogControlEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogControlEpFsmStageInstanceId_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmStageInstanceId = _CfprApSysdebugLogControlEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 17, 1, 1),
    _CfprApSysdebugLogControlEpFsmStageInstanceId_Type()
)
cfprApSysdebugLogControlEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStageInstanceId.setStatus("current")
_CfprApSysdebugLogControlEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogControlEpFsmStageDn_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmStageDn = _CfprApSysdebugLogControlEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 17, 1, 2),
    _CfprApSysdebugLogControlEpFsmStageDn_Type()
)
cfprApSysdebugLogControlEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStageDn.setStatus("current")
_CfprApSysdebugLogControlEpFsmStageRn_Type = SnmpAdminString
_CfprApSysdebugLogControlEpFsmStageRn_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmStageRn = _CfprApSysdebugLogControlEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 17, 1, 3),
    _CfprApSysdebugLogControlEpFsmStageRn_Type()
)
cfprApSysdebugLogControlEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStageRn.setStatus("current")
_CfprApSysdebugLogControlEpFsmStageDescrData_Type = SnmpAdminString
_CfprApSysdebugLogControlEpFsmStageDescrData_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmStageDescrData = _CfprApSysdebugLogControlEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 17, 1, 4),
    _CfprApSysdebugLogControlEpFsmStageDescrData_Type()
)
cfprApSysdebugLogControlEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStageDescrData.setStatus("current")
_CfprApSysdebugLogControlEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSysdebugLogControlEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmStageLastUpdateTime = _CfprApSysdebugLogControlEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 17, 1, 5),
    _CfprApSysdebugLogControlEpFsmStageLastUpdateTime_Type()
)
cfprApSysdebugLogControlEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStageLastUpdateTime.setStatus("current")
_CfprApSysdebugLogControlEpFsmStageName_Type = CfprApSysdebugLogControlEpFsmStageName
_CfprApSysdebugLogControlEpFsmStageName_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmStageName = _CfprApSysdebugLogControlEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 17, 1, 6),
    _CfprApSysdebugLogControlEpFsmStageName_Type()
)
cfprApSysdebugLogControlEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStageName.setStatus("current")
_CfprApSysdebugLogControlEpFsmStageOrder_Type = Gauge32
_CfprApSysdebugLogControlEpFsmStageOrder_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmStageOrder = _CfprApSysdebugLogControlEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 17, 1, 7),
    _CfprApSysdebugLogControlEpFsmStageOrder_Type()
)
cfprApSysdebugLogControlEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStageOrder.setStatus("current")
_CfprApSysdebugLogControlEpFsmStageRetry_Type = Gauge32
_CfprApSysdebugLogControlEpFsmStageRetry_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmStageRetry = _CfprApSysdebugLogControlEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 17, 1, 8),
    _CfprApSysdebugLogControlEpFsmStageRetry_Type()
)
cfprApSysdebugLogControlEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStageRetry.setStatus("current")
_CfprApSysdebugLogControlEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysdebugLogControlEpFsmStageStageStatus_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmStageStageStatus = _CfprApSysdebugLogControlEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 17, 1, 9),
    _CfprApSysdebugLogControlEpFsmStageStageStatus_Type()
)
cfprApSysdebugLogControlEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmStageStageStatus.setStatus("current")
_CfprApSysdebugLogControlEpFsmTaskTable_Object = MibTable
cfprApSysdebugLogControlEpFsmTaskTable = _CfprApSysdebugLogControlEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 18)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmTaskTable.setStatus("current")
_CfprApSysdebugLogControlEpFsmTaskEntry_Object = MibTableRow
cfprApSysdebugLogControlEpFsmTaskEntry = _CfprApSysdebugLogControlEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 18, 1)
)
cfprApSysdebugLogControlEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogControlEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmTaskEntry.setStatus("current")
_CfprApSysdebugLogControlEpFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogControlEpFsmTaskInstanceId_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmTaskInstanceId = _CfprApSysdebugLogControlEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 18, 1, 1),
    _CfprApSysdebugLogControlEpFsmTaskInstanceId_Type()
)
cfprApSysdebugLogControlEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmTaskInstanceId.setStatus("current")
_CfprApSysdebugLogControlEpFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogControlEpFsmTaskDn_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmTaskDn = _CfprApSysdebugLogControlEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 18, 1, 2),
    _CfprApSysdebugLogControlEpFsmTaskDn_Type()
)
cfprApSysdebugLogControlEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmTaskDn.setStatus("current")
_CfprApSysdebugLogControlEpFsmTaskRn_Type = SnmpAdminString
_CfprApSysdebugLogControlEpFsmTaskRn_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmTaskRn = _CfprApSysdebugLogControlEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 18, 1, 3),
    _CfprApSysdebugLogControlEpFsmTaskRn_Type()
)
cfprApSysdebugLogControlEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmTaskRn.setStatus("current")
_CfprApSysdebugLogControlEpFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSysdebugLogControlEpFsmTaskCompletion_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmTaskCompletion = _CfprApSysdebugLogControlEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 18, 1, 4),
    _CfprApSysdebugLogControlEpFsmTaskCompletion_Type()
)
cfprApSysdebugLogControlEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmTaskCompletion.setStatus("current")
_CfprApSysdebugLogControlEpFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSysdebugLogControlEpFsmTaskFlags_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmTaskFlags = _CfprApSysdebugLogControlEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 18, 1, 5),
    _CfprApSysdebugLogControlEpFsmTaskFlags_Type()
)
cfprApSysdebugLogControlEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmTaskFlags.setStatus("current")
_CfprApSysdebugLogControlEpFsmTaskItem_Type = CfprApSysdebugLogControlEpFsmTaskItem
_CfprApSysdebugLogControlEpFsmTaskItem_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmTaskItem = _CfprApSysdebugLogControlEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 18, 1, 6),
    _CfprApSysdebugLogControlEpFsmTaskItem_Type()
)
cfprApSysdebugLogControlEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmTaskItem.setStatus("current")
_CfprApSysdebugLogControlEpFsmTaskSeqId_Type = Gauge32
_CfprApSysdebugLogControlEpFsmTaskSeqId_Object = MibTableColumn
cfprApSysdebugLogControlEpFsmTaskSeqId = _CfprApSysdebugLogControlEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 18, 1, 7),
    _CfprApSysdebugLogControlEpFsmTaskSeqId_Type()
)
cfprApSysdebugLogControlEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlEpFsmTaskSeqId.setStatus("current")
_CfprApSysdebugLogControlModuleTable_Object = MibTable
cfprApSysdebugLogControlModuleTable = _CfprApSysdebugLogControlModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 19)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlModuleTable.setStatus("current")
_CfprApSysdebugLogControlModuleEntry_Object = MibTableRow
cfprApSysdebugLogControlModuleEntry = _CfprApSysdebugLogControlModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 19, 1)
)
cfprApSysdebugLogControlModuleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogControlModuleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlModuleEntry.setStatus("current")
_CfprApSysdebugLogControlModuleInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogControlModuleInstanceId_Object = MibTableColumn
cfprApSysdebugLogControlModuleInstanceId = _CfprApSysdebugLogControlModuleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 19, 1, 1),
    _CfprApSysdebugLogControlModuleInstanceId_Type()
)
cfprApSysdebugLogControlModuleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlModuleInstanceId.setStatus("current")
_CfprApSysdebugLogControlModuleDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogControlModuleDn_Object = MibTableColumn
cfprApSysdebugLogControlModuleDn = _CfprApSysdebugLogControlModuleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 19, 1, 2),
    _CfprApSysdebugLogControlModuleDn_Type()
)
cfprApSysdebugLogControlModuleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlModuleDn.setStatus("current")
_CfprApSysdebugLogControlModuleRn_Type = SnmpAdminString
_CfprApSysdebugLogControlModuleRn_Object = MibTableColumn
cfprApSysdebugLogControlModuleRn = _CfprApSysdebugLogControlModuleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 19, 1, 3),
    _CfprApSysdebugLogControlModuleRn_Type()
)
cfprApSysdebugLogControlModuleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlModuleRn.setStatus("current")
_CfprApSysdebugLogControlModuleDefaultLevel_Type = CfprApSysdebugLogControlLevel
_CfprApSysdebugLogControlModuleDefaultLevel_Object = MibTableColumn
cfprApSysdebugLogControlModuleDefaultLevel = _CfprApSysdebugLogControlModuleDefaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 19, 1, 4),
    _CfprApSysdebugLogControlModuleDefaultLevel_Type()
)
cfprApSysdebugLogControlModuleDefaultLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlModuleDefaultLevel.setStatus("current")
_CfprApSysdebugLogControlModuleLevel_Type = CfprApSysdebugLogControlLevel
_CfprApSysdebugLogControlModuleLevel_Object = MibTableColumn
cfprApSysdebugLogControlModuleLevel = _CfprApSysdebugLogControlModuleLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 19, 1, 5),
    _CfprApSysdebugLogControlModuleLevel_Type()
)
cfprApSysdebugLogControlModuleLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlModuleLevel.setStatus("current")
_CfprApSysdebugLogControlModuleName_Type = SnmpAdminString
_CfprApSysdebugLogControlModuleName_Object = MibTableColumn
cfprApSysdebugLogControlModuleName = _CfprApSysdebugLogControlModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 19, 1, 6),
    _CfprApSysdebugLogControlModuleName_Type()
)
cfprApSysdebugLogControlModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlModuleName.setStatus("current")
_CfprApSysdebugLogControlModuleReset_Type = TruthValue
_CfprApSysdebugLogControlModuleReset_Object = MibTableColumn
cfprApSysdebugLogControlModuleReset = _CfprApSysdebugLogControlModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 19, 1, 7),
    _CfprApSysdebugLogControlModuleReset_Type()
)
cfprApSysdebugLogControlModuleReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogControlModuleReset.setStatus("current")
_CfprApSysdebugLogExportPolicyTable_Object = MibTable
cfprApSysdebugLogExportPolicyTable = _CfprApSysdebugLogExportPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyTable.setStatus("current")
_CfprApSysdebugLogExportPolicyEntry_Object = MibTableRow
cfprApSysdebugLogExportPolicyEntry = _CfprApSysdebugLogExportPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1)
)
cfprApSysdebugLogExportPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogExportPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyEntry.setStatus("current")
_CfprApSysdebugLogExportPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogExportPolicyInstanceId_Object = MibTableColumn
cfprApSysdebugLogExportPolicyInstanceId = _CfprApSysdebugLogExportPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 1),
    _CfprApSysdebugLogExportPolicyInstanceId_Type()
)
cfprApSysdebugLogExportPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyInstanceId.setStatus("current")
_CfprApSysdebugLogExportPolicyDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogExportPolicyDn_Object = MibTableColumn
cfprApSysdebugLogExportPolicyDn = _CfprApSysdebugLogExportPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 2),
    _CfprApSysdebugLogExportPolicyDn_Type()
)
cfprApSysdebugLogExportPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyDn.setStatus("current")
_CfprApSysdebugLogExportPolicyRn_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyRn_Object = MibTableColumn
cfprApSysdebugLogExportPolicyRn = _CfprApSysdebugLogExportPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 3),
    _CfprApSysdebugLogExportPolicyRn_Type()
)
cfprApSysdebugLogExportPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyRn.setStatus("current")
_CfprApSysdebugLogExportPolicyAdminState_Type = CfprApCommClientAdminState
_CfprApSysdebugLogExportPolicyAdminState_Object = MibTableColumn
cfprApSysdebugLogExportPolicyAdminState = _CfprApSysdebugLogExportPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 4),
    _CfprApSysdebugLogExportPolicyAdminState_Type()
)
cfprApSysdebugLogExportPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyAdminState.setStatus("current")
_CfprApSysdebugLogExportPolicyDescr_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyDescr_Object = MibTableColumn
cfprApSysdebugLogExportPolicyDescr = _CfprApSysdebugLogExportPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 5),
    _CfprApSysdebugLogExportPolicyDescr_Type()
)
cfprApSysdebugLogExportPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyDescr.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmDescr_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyFsmDescr_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmDescr = _CfprApSysdebugLogExportPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 6),
    _CfprApSysdebugLogExportPolicyFsmDescr_Type()
)
cfprApSysdebugLogExportPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmDescr.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmPrev_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyFsmPrev_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmPrev = _CfprApSysdebugLogExportPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 7),
    _CfprApSysdebugLogExportPolicyFsmPrev_Type()
)
cfprApSysdebugLogExportPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmPrev.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmProgr_Type = Gauge32
_CfprApSysdebugLogExportPolicyFsmProgr_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmProgr = _CfprApSysdebugLogExportPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 8),
    _CfprApSysdebugLogExportPolicyFsmProgr_Type()
)
cfprApSysdebugLogExportPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmProgr.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmRmtInvErrCode_Type = Gauge32
_CfprApSysdebugLogExportPolicyFsmRmtInvErrCode_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmRmtInvErrCode = _CfprApSysdebugLogExportPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 9),
    _CfprApSysdebugLogExportPolicyFsmRmtInvErrCode_Type()
)
cfprApSysdebugLogExportPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmRmtInvErrCode.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmRmtInvErrDescr = _CfprApSysdebugLogExportPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 10),
    _CfprApSysdebugLogExportPolicyFsmRmtInvErrDescr_Type()
)
cfprApSysdebugLogExportPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmRmtInvErrDescr.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysdebugLogExportPolicyFsmRmtInvRslt_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmRmtInvRslt = _CfprApSysdebugLogExportPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 11),
    _CfprApSysdebugLogExportPolicyFsmRmtInvRslt_Type()
)
cfprApSysdebugLogExportPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmRmtInvRslt.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStageDescr_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyFsmStageDescr_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmStageDescr = _CfprApSysdebugLogExportPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 12),
    _CfprApSysdebugLogExportPolicyFsmStageDescr_Type()
)
cfprApSysdebugLogExportPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStageDescr.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStamp_Type = DateAndTime
_CfprApSysdebugLogExportPolicyFsmStamp_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmStamp = _CfprApSysdebugLogExportPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 13),
    _CfprApSysdebugLogExportPolicyFsmStamp_Type()
)
cfprApSysdebugLogExportPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStamp.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStatus_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyFsmStatus_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmStatus = _CfprApSysdebugLogExportPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 14),
    _CfprApSysdebugLogExportPolicyFsmStatus_Type()
)
cfprApSysdebugLogExportPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStatus.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmTry_Type = Gauge32
_CfprApSysdebugLogExportPolicyFsmTry_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmTry = _CfprApSysdebugLogExportPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 15),
    _CfprApSysdebugLogExportPolicyFsmTry_Type()
)
cfprApSysdebugLogExportPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmTry.setStatus("current")
_CfprApSysdebugLogExportPolicyHostname_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyHostname_Object = MibTableColumn
cfprApSysdebugLogExportPolicyHostname = _CfprApSysdebugLogExportPolicyHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 16),
    _CfprApSysdebugLogExportPolicyHostname_Type()
)
cfprApSysdebugLogExportPolicyHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyHostname.setStatus("current")
_CfprApSysdebugLogExportPolicyIntId_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyIntId_Object = MibTableColumn
cfprApSysdebugLogExportPolicyIntId = _CfprApSysdebugLogExportPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 17),
    _CfprApSysdebugLogExportPolicyIntId_Type()
)
cfprApSysdebugLogExportPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyIntId.setStatus("current")
_CfprApSysdebugLogExportPolicyName_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyName_Object = MibTableColumn
cfprApSysdebugLogExportPolicyName = _CfprApSysdebugLogExportPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 18),
    _CfprApSysdebugLogExportPolicyName_Type()
)
cfprApSysdebugLogExportPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyName.setStatus("current")
_CfprApSysdebugLogExportPolicyPasswordlessSsh_Type = TruthValue
_CfprApSysdebugLogExportPolicyPasswordlessSsh_Object = MibTableColumn
cfprApSysdebugLogExportPolicyPasswordlessSsh = _CfprApSysdebugLogExportPolicyPasswordlessSsh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 19),
    _CfprApSysdebugLogExportPolicyPasswordlessSsh_Type()
)
cfprApSysdebugLogExportPolicyPasswordlessSsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyPasswordlessSsh.setStatus("current")
_CfprApSysdebugLogExportPolicyPath_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyPath_Object = MibTableColumn
cfprApSysdebugLogExportPolicyPath = _CfprApSysdebugLogExportPolicyPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 20),
    _CfprApSysdebugLogExportPolicyPath_Type()
)
cfprApSysdebugLogExportPolicyPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyPath.setStatus("current")
_CfprApSysdebugLogExportPolicyPolicyLevel_Type = Gauge32
_CfprApSysdebugLogExportPolicyPolicyLevel_Object = MibTableColumn
cfprApSysdebugLogExportPolicyPolicyLevel = _CfprApSysdebugLogExportPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 21),
    _CfprApSysdebugLogExportPolicyPolicyLevel_Type()
)
cfprApSysdebugLogExportPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyPolicyLevel.setStatus("current")
_CfprApSysdebugLogExportPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApSysdebugLogExportPolicyPolicyOwner_Object = MibTableColumn
cfprApSysdebugLogExportPolicyPolicyOwner = _CfprApSysdebugLogExportPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 22),
    _CfprApSysdebugLogExportPolicyPolicyOwner_Type()
)
cfprApSysdebugLogExportPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyPolicyOwner.setStatus("current")
_CfprApSysdebugLogExportPolicyPostAction_Type = CfprApSysfileExporterPostAction
_CfprApSysdebugLogExportPolicyPostAction_Object = MibTableColumn
cfprApSysdebugLogExportPolicyPostAction = _CfprApSysdebugLogExportPolicyPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 23),
    _CfprApSysdebugLogExportPolicyPostAction_Type()
)
cfprApSysdebugLogExportPolicyPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyPostAction.setStatus("current")
_CfprApSysdebugLogExportPolicyProto_Type = CfprApSysdebugLogExportPolicyProto
_CfprApSysdebugLogExportPolicyProto_Object = MibTableColumn
cfprApSysdebugLogExportPolicyProto = _CfprApSysdebugLogExportPolicyProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 24),
    _CfprApSysdebugLogExportPolicyProto_Type()
)
cfprApSysdebugLogExportPolicyProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyProto.setStatus("current")
_CfprApSysdebugLogExportPolicyPwd_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyPwd_Object = MibTableColumn
cfprApSysdebugLogExportPolicyPwd = _CfprApSysdebugLogExportPolicyPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 25),
    _CfprApSysdebugLogExportPolicyPwd_Type()
)
cfprApSysdebugLogExportPolicyPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyPwd.setStatus("current")
_CfprApSysdebugLogExportPolicyUser_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyUser_Object = MibTableColumn
cfprApSysdebugLogExportPolicyUser = _CfprApSysdebugLogExportPolicyUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 20, 1, 26),
    _CfprApSysdebugLogExportPolicyUser_Type()
)
cfprApSysdebugLogExportPolicyUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyUser.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmTable_Object = MibTable
cfprApSysdebugLogExportPolicyFsmTable = _CfprApSysdebugLogExportPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmTable.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmEntry_Object = MibTableRow
cfprApSysdebugLogExportPolicyFsmEntry = _CfprApSysdebugLogExportPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21, 1)
)
cfprApSysdebugLogExportPolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogExportPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmEntry.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogExportPolicyFsmInstanceId_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmInstanceId = _CfprApSysdebugLogExportPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21, 1, 1),
    _CfprApSysdebugLogExportPolicyFsmInstanceId_Type()
)
cfprApSysdebugLogExportPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmInstanceId.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogExportPolicyFsmDn_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmDn = _CfprApSysdebugLogExportPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21, 1, 2),
    _CfprApSysdebugLogExportPolicyFsmDn_Type()
)
cfprApSysdebugLogExportPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmDn.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmRn_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyFsmRn_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmRn = _CfprApSysdebugLogExportPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21, 1, 3),
    _CfprApSysdebugLogExportPolicyFsmRn_Type()
)
cfprApSysdebugLogExportPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmRn.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmCompletionTime_Type = DateAndTime
_CfprApSysdebugLogExportPolicyFsmCompletionTime_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmCompletionTime = _CfprApSysdebugLogExportPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21, 1, 4),
    _CfprApSysdebugLogExportPolicyFsmCompletionTime_Type()
)
cfprApSysdebugLogExportPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmCompletionTime.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmCurrentFsm_Type = CfprApSysdebugLogExportPolicyFsmCurrentFsm
_CfprApSysdebugLogExportPolicyFsmCurrentFsm_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmCurrentFsm = _CfprApSysdebugLogExportPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21, 1, 5),
    _CfprApSysdebugLogExportPolicyFsmCurrentFsm_Type()
)
cfprApSysdebugLogExportPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmCurrentFsm.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmDescrData_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyFsmDescrData_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmDescrData = _CfprApSysdebugLogExportPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21, 1, 6),
    _CfprApSysdebugLogExportPolicyFsmDescrData_Type()
)
cfprApSysdebugLogExportPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmDescrData.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysdebugLogExportPolicyFsmFsmStatus_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmFsmStatus = _CfprApSysdebugLogExportPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21, 1, 7),
    _CfprApSysdebugLogExportPolicyFsmFsmStatus_Type()
)
cfprApSysdebugLogExportPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmFsmStatus.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmProgress_Type = Gauge32
_CfprApSysdebugLogExportPolicyFsmProgress_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmProgress = _CfprApSysdebugLogExportPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21, 1, 8),
    _CfprApSysdebugLogExportPolicyFsmProgress_Type()
)
cfprApSysdebugLogExportPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmProgress.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmRmtErrCode_Type = Gauge32
_CfprApSysdebugLogExportPolicyFsmRmtErrCode_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmRmtErrCode = _CfprApSysdebugLogExportPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21, 1, 9),
    _CfprApSysdebugLogExportPolicyFsmRmtErrCode_Type()
)
cfprApSysdebugLogExportPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmRmtErrCode.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyFsmRmtErrDescr_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmRmtErrDescr = _CfprApSysdebugLogExportPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21, 1, 10),
    _CfprApSysdebugLogExportPolicyFsmRmtErrDescr_Type()
)
cfprApSysdebugLogExportPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmRmtErrDescr.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysdebugLogExportPolicyFsmRmtRslt_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmRmtRslt = _CfprApSysdebugLogExportPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 21, 1, 11),
    _CfprApSysdebugLogExportPolicyFsmRmtRslt_Type()
)
cfprApSysdebugLogExportPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmRmtRslt.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStageTable_Object = MibTable
cfprApSysdebugLogExportPolicyFsmStageTable = _CfprApSysdebugLogExportPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 22)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStageTable.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStageEntry_Object = MibTableRow
cfprApSysdebugLogExportPolicyFsmStageEntry = _CfprApSysdebugLogExportPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 22, 1)
)
cfprApSysdebugLogExportPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogExportPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStageEntry.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogExportPolicyFsmStageInstanceId_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmStageInstanceId = _CfprApSysdebugLogExportPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 22, 1, 1),
    _CfprApSysdebugLogExportPolicyFsmStageInstanceId_Type()
)
cfprApSysdebugLogExportPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStageInstanceId.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogExportPolicyFsmStageDn_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmStageDn = _CfprApSysdebugLogExportPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 22, 1, 2),
    _CfprApSysdebugLogExportPolicyFsmStageDn_Type()
)
cfprApSysdebugLogExportPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStageDn.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStageRn_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyFsmStageRn_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmStageRn = _CfprApSysdebugLogExportPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 22, 1, 3),
    _CfprApSysdebugLogExportPolicyFsmStageRn_Type()
)
cfprApSysdebugLogExportPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStageRn.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStageDescrData_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyFsmStageDescrData_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmStageDescrData = _CfprApSysdebugLogExportPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 22, 1, 4),
    _CfprApSysdebugLogExportPolicyFsmStageDescrData_Type()
)
cfprApSysdebugLogExportPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStageDescrData.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSysdebugLogExportPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmStageLastUpdateTime = _CfprApSysdebugLogExportPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 22, 1, 5),
    _CfprApSysdebugLogExportPolicyFsmStageLastUpdateTime_Type()
)
cfprApSysdebugLogExportPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStageLastUpdateTime.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStageName_Type = CfprApSysdebugLogExportPolicyFsmStageName
_CfprApSysdebugLogExportPolicyFsmStageName_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmStageName = _CfprApSysdebugLogExportPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 22, 1, 6),
    _CfprApSysdebugLogExportPolicyFsmStageName_Type()
)
cfprApSysdebugLogExportPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStageName.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStageOrder_Type = Gauge32
_CfprApSysdebugLogExportPolicyFsmStageOrder_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmStageOrder = _CfprApSysdebugLogExportPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 22, 1, 7),
    _CfprApSysdebugLogExportPolicyFsmStageOrder_Type()
)
cfprApSysdebugLogExportPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStageOrder.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStageRetry_Type = Gauge32
_CfprApSysdebugLogExportPolicyFsmStageRetry_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmStageRetry = _CfprApSysdebugLogExportPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 22, 1, 8),
    _CfprApSysdebugLogExportPolicyFsmStageRetry_Type()
)
cfprApSysdebugLogExportPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStageRetry.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysdebugLogExportPolicyFsmStageStageStatus_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmStageStageStatus = _CfprApSysdebugLogExportPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 22, 1, 9),
    _CfprApSysdebugLogExportPolicyFsmStageStageStatus_Type()
)
cfprApSysdebugLogExportPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmStageStageStatus.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmTaskTable_Object = MibTable
cfprApSysdebugLogExportPolicyFsmTaskTable = _CfprApSysdebugLogExportPolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 23)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmTaskTable.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmTaskEntry_Object = MibTableRow
cfprApSysdebugLogExportPolicyFsmTaskEntry = _CfprApSysdebugLogExportPolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 23, 1)
)
cfprApSysdebugLogExportPolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogExportPolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmTaskEntry.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogExportPolicyFsmTaskInstanceId_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmTaskInstanceId = _CfprApSysdebugLogExportPolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 23, 1, 1),
    _CfprApSysdebugLogExportPolicyFsmTaskInstanceId_Type()
)
cfprApSysdebugLogExportPolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmTaskInstanceId.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogExportPolicyFsmTaskDn_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmTaskDn = _CfprApSysdebugLogExportPolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 23, 1, 2),
    _CfprApSysdebugLogExportPolicyFsmTaskDn_Type()
)
cfprApSysdebugLogExportPolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmTaskDn.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmTaskRn_Type = SnmpAdminString
_CfprApSysdebugLogExportPolicyFsmTaskRn_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmTaskRn = _CfprApSysdebugLogExportPolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 23, 1, 3),
    _CfprApSysdebugLogExportPolicyFsmTaskRn_Type()
)
cfprApSysdebugLogExportPolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmTaskRn.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSysdebugLogExportPolicyFsmTaskCompletion_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmTaskCompletion = _CfprApSysdebugLogExportPolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 23, 1, 4),
    _CfprApSysdebugLogExportPolicyFsmTaskCompletion_Type()
)
cfprApSysdebugLogExportPolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmTaskCompletion.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSysdebugLogExportPolicyFsmTaskFlags_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmTaskFlags = _CfprApSysdebugLogExportPolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 23, 1, 5),
    _CfprApSysdebugLogExportPolicyFsmTaskFlags_Type()
)
cfprApSysdebugLogExportPolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmTaskFlags.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmTaskItem_Type = CfprApSysdebugLogExportPolicyFsmTaskItem
_CfprApSysdebugLogExportPolicyFsmTaskItem_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmTaskItem = _CfprApSysdebugLogExportPolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 23, 1, 6),
    _CfprApSysdebugLogExportPolicyFsmTaskItem_Type()
)
cfprApSysdebugLogExportPolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmTaskItem.setStatus("current")
_CfprApSysdebugLogExportPolicyFsmTaskSeqId_Type = Gauge32
_CfprApSysdebugLogExportPolicyFsmTaskSeqId_Object = MibTableColumn
cfprApSysdebugLogExportPolicyFsmTaskSeqId = _CfprApSysdebugLogExportPolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 23, 1, 7),
    _CfprApSysdebugLogExportPolicyFsmTaskSeqId_Type()
)
cfprApSysdebugLogExportPolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportPolicyFsmTaskSeqId.setStatus("current")
_CfprApSysdebugLogExportStatusTable_Object = MibTable
cfprApSysdebugLogExportStatusTable = _CfprApSysdebugLogExportStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 24)
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportStatusTable.setStatus("current")
_CfprApSysdebugLogExportStatusEntry_Object = MibTableRow
cfprApSysdebugLogExportStatusEntry = _CfprApSysdebugLogExportStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 24, 1)
)
cfprApSysdebugLogExportStatusEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugLogExportStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportStatusEntry.setStatus("current")
_CfprApSysdebugLogExportStatusInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugLogExportStatusInstanceId_Object = MibTableColumn
cfprApSysdebugLogExportStatusInstanceId = _CfprApSysdebugLogExportStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 24, 1, 1),
    _CfprApSysdebugLogExportStatusInstanceId_Type()
)
cfprApSysdebugLogExportStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportStatusInstanceId.setStatus("current")
_CfprApSysdebugLogExportStatusDn_Type = CfprApManagedObjectDn
_CfprApSysdebugLogExportStatusDn_Object = MibTableColumn
cfprApSysdebugLogExportStatusDn = _CfprApSysdebugLogExportStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 24, 1, 2),
    _CfprApSysdebugLogExportStatusDn_Type()
)
cfprApSysdebugLogExportStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportStatusDn.setStatus("current")
_CfprApSysdebugLogExportStatusRn_Type = SnmpAdminString
_CfprApSysdebugLogExportStatusRn_Object = MibTableColumn
cfprApSysdebugLogExportStatusRn = _CfprApSysdebugLogExportStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 24, 1, 3),
    _CfprApSysdebugLogExportStatusRn_Type()
)
cfprApSysdebugLogExportStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportStatusRn.setStatus("current")
_CfprApSysdebugLogExportStatusExportFailureReason_Type = SnmpAdminString
_CfprApSysdebugLogExportStatusExportFailureReason_Object = MibTableColumn
cfprApSysdebugLogExportStatusExportFailureReason = _CfprApSysdebugLogExportStatusExportFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 24, 1, 4),
    _CfprApSysdebugLogExportStatusExportFailureReason_Type()
)
cfprApSysdebugLogExportStatusExportFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportStatusExportFailureReason.setStatus("current")
_CfprApSysdebugLogExportStatusExportStatus_Type = CfprApSysdebugExportStatus
_CfprApSysdebugLogExportStatusExportStatus_Object = MibTableColumn
cfprApSysdebugLogExportStatusExportStatus = _CfprApSysdebugLogExportStatusExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 24, 1, 5),
    _CfprApSysdebugLogExportStatusExportStatus_Type()
)
cfprApSysdebugLogExportStatusExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportStatusExportStatus.setStatus("current")
_CfprApSysdebugLogExportStatusSwitchId_Type = CfprApNetworkSwitchId
_CfprApSysdebugLogExportStatusSwitchId_Object = MibTableColumn
cfprApSysdebugLogExportStatusSwitchId = _CfprApSysdebugLogExportStatusSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 24, 1, 6),
    _CfprApSysdebugLogExportStatusSwitchId_Type()
)
cfprApSysdebugLogExportStatusSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugLogExportStatusSwitchId.setStatus("current")
_CfprApSysdebugMEpLogTable_Object = MibTable
cfprApSysdebugMEpLogTable = _CfprApSysdebugMEpLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 25)
)
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogTable.setStatus("current")
_CfprApSysdebugMEpLogEntry_Object = MibTableRow
cfprApSysdebugMEpLogEntry = _CfprApSysdebugMEpLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 25, 1)
)
cfprApSysdebugMEpLogEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugMEpLogInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogEntry.setStatus("current")
_CfprApSysdebugMEpLogInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugMEpLogInstanceId_Object = MibTableColumn
cfprApSysdebugMEpLogInstanceId = _CfprApSysdebugMEpLogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 25, 1, 1),
    _CfprApSysdebugMEpLogInstanceId_Type()
)
cfprApSysdebugMEpLogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogInstanceId.setStatus("current")
_CfprApSysdebugMEpLogDn_Type = CfprApManagedObjectDn
_CfprApSysdebugMEpLogDn_Object = MibTableColumn
cfprApSysdebugMEpLogDn = _CfprApSysdebugMEpLogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 25, 1, 2),
    _CfprApSysdebugMEpLogDn_Type()
)
cfprApSysdebugMEpLogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogDn.setStatus("current")
_CfprApSysdebugMEpLogRn_Type = SnmpAdminString
_CfprApSysdebugMEpLogRn_Object = MibTableColumn
cfprApSysdebugMEpLogRn = _CfprApSysdebugMEpLogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 25, 1, 3),
    _CfprApSysdebugMEpLogRn_Type()
)
cfprApSysdebugMEpLogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogRn.setStatus("current")
_CfprApSysdebugMEpLogAdminState_Type = CfprApSysdebugEpLogAdminState
_CfprApSysdebugMEpLogAdminState_Object = MibTableColumn
cfprApSysdebugMEpLogAdminState = _CfprApSysdebugMEpLogAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 25, 1, 4),
    _CfprApSysdebugMEpLogAdminState_Type()
)
cfprApSysdebugMEpLogAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogAdminState.setStatus("current")
_CfprApSysdebugMEpLogCapacity_Type = CfprApSysdebugEpLogCapacity
_CfprApSysdebugMEpLogCapacity_Object = MibTableColumn
cfprApSysdebugMEpLogCapacity = _CfprApSysdebugMEpLogCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 25, 1, 5),
    _CfprApSysdebugMEpLogCapacity_Type()
)
cfprApSysdebugMEpLogCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogCapacity.setStatus("current")
_CfprApSysdebugMEpLogId_Type = Gauge32
_CfprApSysdebugMEpLogId_Object = MibTableColumn
cfprApSysdebugMEpLogId = _CfprApSysdebugMEpLogId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 25, 1, 6),
    _CfprApSysdebugMEpLogId_Type()
)
cfprApSysdebugMEpLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogId.setStatus("current")
_CfprApSysdebugMEpLogLastUpdate_Type = DateAndTime
_CfprApSysdebugMEpLogLastUpdate_Object = MibTableColumn
cfprApSysdebugMEpLogLastUpdate = _CfprApSysdebugMEpLogLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 25, 1, 7),
    _CfprApSysdebugMEpLogLastUpdate_Type()
)
cfprApSysdebugMEpLogLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogLastUpdate.setStatus("current")
_CfprApSysdebugMEpLogOperState_Type = CfprApSysdebugMEpLogOperState
_CfprApSysdebugMEpLogOperState_Object = MibTableColumn
cfprApSysdebugMEpLogOperState = _CfprApSysdebugMEpLogOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 25, 1, 8),
    _CfprApSysdebugMEpLogOperState_Type()
)
cfprApSysdebugMEpLogOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogOperState.setStatus("current")
_CfprApSysdebugMEpLogType_Type = CfprApSysdebugEpLogType
_CfprApSysdebugMEpLogType_Object = MibTableColumn
cfprApSysdebugMEpLogType = _CfprApSysdebugMEpLogType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 25, 1, 9),
    _CfprApSysdebugMEpLogType_Type()
)
cfprApSysdebugMEpLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogType.setStatus("current")
_CfprApSysdebugMEpLogPolicyTable_Object = MibTable
cfprApSysdebugMEpLogPolicyTable = _CfprApSysdebugMEpLogPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 26)
)
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogPolicyTable.setStatus("current")
_CfprApSysdebugMEpLogPolicyEntry_Object = MibTableRow
cfprApSysdebugMEpLogPolicyEntry = _CfprApSysdebugMEpLogPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 26, 1)
)
cfprApSysdebugMEpLogPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugMEpLogPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogPolicyEntry.setStatus("current")
_CfprApSysdebugMEpLogPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugMEpLogPolicyInstanceId_Object = MibTableColumn
cfprApSysdebugMEpLogPolicyInstanceId = _CfprApSysdebugMEpLogPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 26, 1, 1),
    _CfprApSysdebugMEpLogPolicyInstanceId_Type()
)
cfprApSysdebugMEpLogPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogPolicyInstanceId.setStatus("current")
_CfprApSysdebugMEpLogPolicyDn_Type = CfprApManagedObjectDn
_CfprApSysdebugMEpLogPolicyDn_Object = MibTableColumn
cfprApSysdebugMEpLogPolicyDn = _CfprApSysdebugMEpLogPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 26, 1, 2),
    _CfprApSysdebugMEpLogPolicyDn_Type()
)
cfprApSysdebugMEpLogPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogPolicyDn.setStatus("current")
_CfprApSysdebugMEpLogPolicyRn_Type = SnmpAdminString
_CfprApSysdebugMEpLogPolicyRn_Object = MibTableColumn
cfprApSysdebugMEpLogPolicyRn = _CfprApSysdebugMEpLogPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 26, 1, 3),
    _CfprApSysdebugMEpLogPolicyRn_Type()
)
cfprApSysdebugMEpLogPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogPolicyRn.setStatus("current")
_CfprApSysdebugMEpLogPolicyDescr_Type = SnmpAdminString
_CfprApSysdebugMEpLogPolicyDescr_Object = MibTableColumn
cfprApSysdebugMEpLogPolicyDescr = _CfprApSysdebugMEpLogPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 26, 1, 4),
    _CfprApSysdebugMEpLogPolicyDescr_Type()
)
cfprApSysdebugMEpLogPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogPolicyDescr.setStatus("current")
_CfprApSysdebugMEpLogPolicyIntId_Type = SnmpAdminString
_CfprApSysdebugMEpLogPolicyIntId_Object = MibTableColumn
cfprApSysdebugMEpLogPolicyIntId = _CfprApSysdebugMEpLogPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 26, 1, 5),
    _CfprApSysdebugMEpLogPolicyIntId_Type()
)
cfprApSysdebugMEpLogPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogPolicyIntId.setStatus("current")
_CfprApSysdebugMEpLogPolicyName_Type = SnmpAdminString
_CfprApSysdebugMEpLogPolicyName_Object = MibTableColumn
cfprApSysdebugMEpLogPolicyName = _CfprApSysdebugMEpLogPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 26, 1, 6),
    _CfprApSysdebugMEpLogPolicyName_Type()
)
cfprApSysdebugMEpLogPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogPolicyName.setStatus("current")
_CfprApSysdebugMEpLogPolicyPolicyLevel_Type = Gauge32
_CfprApSysdebugMEpLogPolicyPolicyLevel_Object = MibTableColumn
cfprApSysdebugMEpLogPolicyPolicyLevel = _CfprApSysdebugMEpLogPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 26, 1, 7),
    _CfprApSysdebugMEpLogPolicyPolicyLevel_Type()
)
cfprApSysdebugMEpLogPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogPolicyPolicyLevel.setStatus("current")
_CfprApSysdebugMEpLogPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApSysdebugMEpLogPolicyPolicyOwner_Object = MibTableColumn
cfprApSysdebugMEpLogPolicyPolicyOwner = _CfprApSysdebugMEpLogPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 26, 1, 8),
    _CfprApSysdebugMEpLogPolicyPolicyOwner_Type()
)
cfprApSysdebugMEpLogPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogPolicyPolicyOwner.setStatus("current")
_CfprApSysdebugMEpLogPolicyType_Type = CfprApSysdebugEpLogType
_CfprApSysdebugMEpLogPolicyType_Object = MibTableColumn
cfprApSysdebugMEpLogPolicyType = _CfprApSysdebugMEpLogPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 26, 1, 9),
    _CfprApSysdebugMEpLogPolicyType_Type()
)
cfprApSysdebugMEpLogPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugMEpLogPolicyType.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetTable_Object = MibTable
cfprApSysdebugManualCoreFileExportTargetTable = _CfprApSysdebugManualCoreFileExportTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27)
)
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetTable.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetEntry_Object = MibTableRow
cfprApSysdebugManualCoreFileExportTargetEntry = _CfprApSysdebugManualCoreFileExportTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1)
)
cfprApSysdebugManualCoreFileExportTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugManualCoreFileExportTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetEntry.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugManualCoreFileExportTargetInstanceId_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetInstanceId = _CfprApSysdebugManualCoreFileExportTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 1),
    _CfprApSysdebugManualCoreFileExportTargetInstanceId_Type()
)
cfprApSysdebugManualCoreFileExportTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetInstanceId.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetDn_Type = CfprApManagedObjectDn
_CfprApSysdebugManualCoreFileExportTargetDn_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetDn = _CfprApSysdebugManualCoreFileExportTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 2),
    _CfprApSysdebugManualCoreFileExportTargetDn_Type()
)
cfprApSysdebugManualCoreFileExportTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetDn.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetRn_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetRn_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetRn = _CfprApSysdebugManualCoreFileExportTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 3),
    _CfprApSysdebugManualCoreFileExportTargetRn_Type()
)
cfprApSysdebugManualCoreFileExportTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetRn.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetAdminState_Type = CfprApSysdebugManualCoreFileExportTargetAdminState
_CfprApSysdebugManualCoreFileExportTargetAdminState_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetAdminState = _CfprApSysdebugManualCoreFileExportTargetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 4),
    _CfprApSysdebugManualCoreFileExportTargetAdminState_Type()
)
cfprApSysdebugManualCoreFileExportTargetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetAdminState.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetDescr_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetDescr_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetDescr = _CfprApSysdebugManualCoreFileExportTargetDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 5),
    _CfprApSysdebugManualCoreFileExportTargetDescr_Type()
)
cfprApSysdebugManualCoreFileExportTargetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetDescr.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetExportFailureReason_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetExportFailureReason_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetExportFailureReason = _CfprApSysdebugManualCoreFileExportTargetExportFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 6),
    _CfprApSysdebugManualCoreFileExportTargetExportFailureReason_Type()
)
cfprApSysdebugManualCoreFileExportTargetExportFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetExportFailureReason.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetExportStatus_Type = CfprApSysdebugCoreExportStatus
_CfprApSysdebugManualCoreFileExportTargetExportStatus_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetExportStatus = _CfprApSysdebugManualCoreFileExportTargetExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 7),
    _CfprApSysdebugManualCoreFileExportTargetExportStatus_Type()
)
cfprApSysdebugManualCoreFileExportTargetExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetExportStatus.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmDescr_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetFsmDescr_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmDescr = _CfprApSysdebugManualCoreFileExportTargetFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 8),
    _CfprApSysdebugManualCoreFileExportTargetFsmDescr_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmDescr.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmPrev_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetFsmPrev_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmPrev = _CfprApSysdebugManualCoreFileExportTargetFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 9),
    _CfprApSysdebugManualCoreFileExportTargetFsmPrev_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmPrev.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmProgr_Type = Gauge32
_CfprApSysdebugManualCoreFileExportTargetFsmProgr_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmProgr = _CfprApSysdebugManualCoreFileExportTargetFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 10),
    _CfprApSysdebugManualCoreFileExportTargetFsmProgr_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmProgr.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrCode_Type = Gauge32
_CfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrCode_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrCode = _CfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 11),
    _CfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrCode_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrCode.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr = _CfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 12),
    _CfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysdebugManualCoreFileExportTargetFsmRmtInvRslt_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmRmtInvRslt = _CfprApSysdebugManualCoreFileExportTargetFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 13),
    _CfprApSysdebugManualCoreFileExportTargetFsmRmtInvRslt_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmRmtInvRslt.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStageDescr_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetFsmStageDescr_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmStageDescr = _CfprApSysdebugManualCoreFileExportTargetFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 14),
    _CfprApSysdebugManualCoreFileExportTargetFsmStageDescr_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStageDescr.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStamp_Type = DateAndTime
_CfprApSysdebugManualCoreFileExportTargetFsmStamp_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmStamp = _CfprApSysdebugManualCoreFileExportTargetFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 15),
    _CfprApSysdebugManualCoreFileExportTargetFsmStamp_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStamp.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStatus_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetFsmStatus_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmStatus = _CfprApSysdebugManualCoreFileExportTargetFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 16),
    _CfprApSysdebugManualCoreFileExportTargetFsmStatus_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStatus.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmTry_Type = Gauge32
_CfprApSysdebugManualCoreFileExportTargetFsmTry_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmTry = _CfprApSysdebugManualCoreFileExportTargetFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 17),
    _CfprApSysdebugManualCoreFileExportTargetFsmTry_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmTry.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetHostname_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetHostname_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetHostname = _CfprApSysdebugManualCoreFileExportTargetHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 18),
    _CfprApSysdebugManualCoreFileExportTargetHostname_Type()
)
cfprApSysdebugManualCoreFileExportTargetHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetHostname.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetIntId_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetIntId_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetIntId = _CfprApSysdebugManualCoreFileExportTargetIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 19),
    _CfprApSysdebugManualCoreFileExportTargetIntId_Type()
)
cfprApSysdebugManualCoreFileExportTargetIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetIntId.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetName_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetName_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetName = _CfprApSysdebugManualCoreFileExportTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 20),
    _CfprApSysdebugManualCoreFileExportTargetName_Type()
)
cfprApSysdebugManualCoreFileExportTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetName.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetPath_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetPath_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetPath = _CfprApSysdebugManualCoreFileExportTargetPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 21),
    _CfprApSysdebugManualCoreFileExportTargetPath_Type()
)
cfprApSysdebugManualCoreFileExportTargetPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetPath.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetPolicyLevel_Type = Gauge32
_CfprApSysdebugManualCoreFileExportTargetPolicyLevel_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetPolicyLevel = _CfprApSysdebugManualCoreFileExportTargetPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 22),
    _CfprApSysdebugManualCoreFileExportTargetPolicyLevel_Type()
)
cfprApSysdebugManualCoreFileExportTargetPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetPolicyLevel.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApSysdebugManualCoreFileExportTargetPolicyOwner_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetPolicyOwner = _CfprApSysdebugManualCoreFileExportTargetPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 23),
    _CfprApSysdebugManualCoreFileExportTargetPolicyOwner_Type()
)
cfprApSysdebugManualCoreFileExportTargetPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetPolicyOwner.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetPort_Type = Gauge32
_CfprApSysdebugManualCoreFileExportTargetPort_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetPort = _CfprApSysdebugManualCoreFileExportTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 24),
    _CfprApSysdebugManualCoreFileExportTargetPort_Type()
)
cfprApSysdebugManualCoreFileExportTargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetPort.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetPostAction_Type = CfprApSysfileExporterPostAction
_CfprApSysdebugManualCoreFileExportTargetPostAction_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetPostAction = _CfprApSysdebugManualCoreFileExportTargetPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 25),
    _CfprApSysdebugManualCoreFileExportTargetPostAction_Type()
)
cfprApSysdebugManualCoreFileExportTargetPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetPostAction.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetProto_Type = CfprApSysdebugManualCoreFileExportTargetProto
_CfprApSysdebugManualCoreFileExportTargetProto_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetProto = _CfprApSysdebugManualCoreFileExportTargetProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 27, 1, 26),
    _CfprApSysdebugManualCoreFileExportTargetProto_Type()
)
cfprApSysdebugManualCoreFileExportTargetProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetProto.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmTable_Object = MibTable
cfprApSysdebugManualCoreFileExportTargetFsmTable = _CfprApSysdebugManualCoreFileExportTargetFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28)
)
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmTable.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmEntry_Object = MibTableRow
cfprApSysdebugManualCoreFileExportTargetFsmEntry = _CfprApSysdebugManualCoreFileExportTargetFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28, 1)
)
cfprApSysdebugManualCoreFileExportTargetFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugManualCoreFileExportTargetFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmEntry.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugManualCoreFileExportTargetFsmInstanceId_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmInstanceId = _CfprApSysdebugManualCoreFileExportTargetFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28, 1, 1),
    _CfprApSysdebugManualCoreFileExportTargetFsmInstanceId_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmInstanceId.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmDn_Type = CfprApManagedObjectDn
_CfprApSysdebugManualCoreFileExportTargetFsmDn_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmDn = _CfprApSysdebugManualCoreFileExportTargetFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28, 1, 2),
    _CfprApSysdebugManualCoreFileExportTargetFsmDn_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmDn.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmRn_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetFsmRn_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmRn = _CfprApSysdebugManualCoreFileExportTargetFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28, 1, 3),
    _CfprApSysdebugManualCoreFileExportTargetFsmRn_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmRn.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmCompletionTime_Type = DateAndTime
_CfprApSysdebugManualCoreFileExportTargetFsmCompletionTime_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmCompletionTime = _CfprApSysdebugManualCoreFileExportTargetFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28, 1, 4),
    _CfprApSysdebugManualCoreFileExportTargetFsmCompletionTime_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmCompletionTime.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmCurrentFsm_Type = CfprApSysdebugManualCoreFileExportTargetFsmCurrentFsm
_CfprApSysdebugManualCoreFileExportTargetFsmCurrentFsm_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmCurrentFsm = _CfprApSysdebugManualCoreFileExportTargetFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28, 1, 5),
    _CfprApSysdebugManualCoreFileExportTargetFsmCurrentFsm_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmCurrentFsm.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmDescrData_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetFsmDescrData_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmDescrData = _CfprApSysdebugManualCoreFileExportTargetFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28, 1, 6),
    _CfprApSysdebugManualCoreFileExportTargetFsmDescrData_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmDescrData.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysdebugManualCoreFileExportTargetFsmFsmStatus_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmFsmStatus = _CfprApSysdebugManualCoreFileExportTargetFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28, 1, 7),
    _CfprApSysdebugManualCoreFileExportTargetFsmFsmStatus_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmFsmStatus.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmProgress_Type = Gauge32
_CfprApSysdebugManualCoreFileExportTargetFsmProgress_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmProgress = _CfprApSysdebugManualCoreFileExportTargetFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28, 1, 8),
    _CfprApSysdebugManualCoreFileExportTargetFsmProgress_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmProgress.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmRmtErrCode_Type = Gauge32
_CfprApSysdebugManualCoreFileExportTargetFsmRmtErrCode_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmRmtErrCode = _CfprApSysdebugManualCoreFileExportTargetFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28, 1, 9),
    _CfprApSysdebugManualCoreFileExportTargetFsmRmtErrCode_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmRmtErrCode.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetFsmRmtErrDescr_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmRmtErrDescr = _CfprApSysdebugManualCoreFileExportTargetFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28, 1, 10),
    _CfprApSysdebugManualCoreFileExportTargetFsmRmtErrDescr_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmRmtErrDescr.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysdebugManualCoreFileExportTargetFsmRmtRslt_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmRmtRslt = _CfprApSysdebugManualCoreFileExportTargetFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 28, 1, 11),
    _CfprApSysdebugManualCoreFileExportTargetFsmRmtRslt_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmRmtRslt.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStageTable_Object = MibTable
cfprApSysdebugManualCoreFileExportTargetFsmStageTable = _CfprApSysdebugManualCoreFileExportTargetFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 29)
)
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStageTable.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStageEntry_Object = MibTableRow
cfprApSysdebugManualCoreFileExportTargetFsmStageEntry = _CfprApSysdebugManualCoreFileExportTargetFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 29, 1)
)
cfprApSysdebugManualCoreFileExportTargetFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugManualCoreFileExportTargetFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStageEntry.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugManualCoreFileExportTargetFsmStageInstanceId_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmStageInstanceId = _CfprApSysdebugManualCoreFileExportTargetFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 29, 1, 1),
    _CfprApSysdebugManualCoreFileExportTargetFsmStageInstanceId_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStageInstanceId.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSysdebugManualCoreFileExportTargetFsmStageDn_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmStageDn = _CfprApSysdebugManualCoreFileExportTargetFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 29, 1, 2),
    _CfprApSysdebugManualCoreFileExportTargetFsmStageDn_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStageDn.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStageRn_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetFsmStageRn_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmStageRn = _CfprApSysdebugManualCoreFileExportTargetFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 29, 1, 3),
    _CfprApSysdebugManualCoreFileExportTargetFsmStageRn_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStageRn.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStageDescrData_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetFsmStageDescrData_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmStageDescrData = _CfprApSysdebugManualCoreFileExportTargetFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 29, 1, 4),
    _CfprApSysdebugManualCoreFileExportTargetFsmStageDescrData_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStageDescrData.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime = _CfprApSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 29, 1, 5),
    _CfprApSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStageName_Type = CfprApSysdebugManualCoreFileExportTargetFsmStageName
_CfprApSysdebugManualCoreFileExportTargetFsmStageName_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmStageName = _CfprApSysdebugManualCoreFileExportTargetFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 29, 1, 6),
    _CfprApSysdebugManualCoreFileExportTargetFsmStageName_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStageName.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStageOrder_Type = Gauge32
_CfprApSysdebugManualCoreFileExportTargetFsmStageOrder_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmStageOrder = _CfprApSysdebugManualCoreFileExportTargetFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 29, 1, 7),
    _CfprApSysdebugManualCoreFileExportTargetFsmStageOrder_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStageOrder.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStageRetry_Type = Gauge32
_CfprApSysdebugManualCoreFileExportTargetFsmStageRetry_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmStageRetry = _CfprApSysdebugManualCoreFileExportTargetFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 29, 1, 8),
    _CfprApSysdebugManualCoreFileExportTargetFsmStageRetry_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStageRetry.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysdebugManualCoreFileExportTargetFsmStageStageStatus_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmStageStageStatus = _CfprApSysdebugManualCoreFileExportTargetFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 29, 1, 9),
    _CfprApSysdebugManualCoreFileExportTargetFsmStageStageStatus_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmStageStageStatus.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmTaskTable_Object = MibTable
cfprApSysdebugManualCoreFileExportTargetFsmTaskTable = _CfprApSysdebugManualCoreFileExportTargetFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 30)
)
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmTaskTable.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmTaskEntry_Object = MibTableRow
cfprApSysdebugManualCoreFileExportTargetFsmTaskEntry = _CfprApSysdebugManualCoreFileExportTargetFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 30, 1)
)
cfprApSysdebugManualCoreFileExportTargetFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugManualCoreFileExportTargetFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmTaskEntry.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugManualCoreFileExportTargetFsmTaskInstanceId_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmTaskInstanceId = _CfprApSysdebugManualCoreFileExportTargetFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 30, 1, 1),
    _CfprApSysdebugManualCoreFileExportTargetFsmTaskInstanceId_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmTaskInstanceId.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSysdebugManualCoreFileExportTargetFsmTaskDn_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmTaskDn = _CfprApSysdebugManualCoreFileExportTargetFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 30, 1, 2),
    _CfprApSysdebugManualCoreFileExportTargetFsmTaskDn_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmTaskDn.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmTaskRn_Type = SnmpAdminString
_CfprApSysdebugManualCoreFileExportTargetFsmTaskRn_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmTaskRn = _CfprApSysdebugManualCoreFileExportTargetFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 30, 1, 3),
    _CfprApSysdebugManualCoreFileExportTargetFsmTaskRn_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmTaskRn.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSysdebugManualCoreFileExportTargetFsmTaskCompletion_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmTaskCompletion = _CfprApSysdebugManualCoreFileExportTargetFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 30, 1, 4),
    _CfprApSysdebugManualCoreFileExportTargetFsmTaskCompletion_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmTaskCompletion.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSysdebugManualCoreFileExportTargetFsmTaskFlags_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmTaskFlags = _CfprApSysdebugManualCoreFileExportTargetFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 30, 1, 5),
    _CfprApSysdebugManualCoreFileExportTargetFsmTaskFlags_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmTaskFlags.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmTaskItem_Type = CfprApSysdebugManualCoreFileExportTargetFsmTaskItem
_CfprApSysdebugManualCoreFileExportTargetFsmTaskItem_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmTaskItem = _CfprApSysdebugManualCoreFileExportTargetFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 30, 1, 6),
    _CfprApSysdebugManualCoreFileExportTargetFsmTaskItem_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmTaskItem.setStatus("current")
_CfprApSysdebugManualCoreFileExportTargetFsmTaskSeqId_Type = Gauge32
_CfprApSysdebugManualCoreFileExportTargetFsmTaskSeqId_Object = MibTableColumn
cfprApSysdebugManualCoreFileExportTargetFsmTaskSeqId = _CfprApSysdebugManualCoreFileExportTargetFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 30, 1, 7),
    _CfprApSysdebugManualCoreFileExportTargetFsmTaskSeqId_Type()
)
cfprApSysdebugManualCoreFileExportTargetFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugManualCoreFileExportTargetFsmTaskSeqId.setStatus("current")
_CfprApSysdebugTechSupFileRepositoryTable_Object = MibTable
cfprApSysdebugTechSupFileRepositoryTable = _CfprApSysdebugTechSupFileRepositoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 31)
)
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupFileRepositoryTable.setStatus("current")
_CfprApSysdebugTechSupFileRepositoryEntry_Object = MibTableRow
cfprApSysdebugTechSupFileRepositoryEntry = _CfprApSysdebugTechSupFileRepositoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 31, 1)
)
cfprApSysdebugTechSupFileRepositoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugTechSupFileRepositoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupFileRepositoryEntry.setStatus("current")
_CfprApSysdebugTechSupFileRepositoryInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugTechSupFileRepositoryInstanceId_Object = MibTableColumn
cfprApSysdebugTechSupFileRepositoryInstanceId = _CfprApSysdebugTechSupFileRepositoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 31, 1, 1),
    _CfprApSysdebugTechSupFileRepositoryInstanceId_Type()
)
cfprApSysdebugTechSupFileRepositoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupFileRepositoryInstanceId.setStatus("current")
_CfprApSysdebugTechSupFileRepositoryDn_Type = CfprApManagedObjectDn
_CfprApSysdebugTechSupFileRepositoryDn_Object = MibTableColumn
cfprApSysdebugTechSupFileRepositoryDn = _CfprApSysdebugTechSupFileRepositoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 31, 1, 2),
    _CfprApSysdebugTechSupFileRepositoryDn_Type()
)
cfprApSysdebugTechSupFileRepositoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupFileRepositoryDn.setStatus("current")
_CfprApSysdebugTechSupFileRepositoryRn_Type = SnmpAdminString
_CfprApSysdebugTechSupFileRepositoryRn_Object = MibTableColumn
cfprApSysdebugTechSupFileRepositoryRn = _CfprApSysdebugTechSupFileRepositoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 31, 1, 3),
    _CfprApSysdebugTechSupFileRepositoryRn_Type()
)
cfprApSysdebugTechSupFileRepositoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupFileRepositoryRn.setStatus("current")
_CfprApSysdebugTechSupportTable_Object = MibTable
cfprApSysdebugTechSupportTable = _CfprApSysdebugTechSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32)
)
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportTable.setStatus("current")
_CfprApSysdebugTechSupportEntry_Object = MibTableRow
cfprApSysdebugTechSupportEntry = _CfprApSysdebugTechSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1)
)
cfprApSysdebugTechSupportEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugTechSupportInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportEntry.setStatus("current")
_CfprApSysdebugTechSupportInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugTechSupportInstanceId_Object = MibTableColumn
cfprApSysdebugTechSupportInstanceId = _CfprApSysdebugTechSupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 1),
    _CfprApSysdebugTechSupportInstanceId_Type()
)
cfprApSysdebugTechSupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportInstanceId.setStatus("current")
_CfprApSysdebugTechSupportDn_Type = CfprApManagedObjectDn
_CfprApSysdebugTechSupportDn_Object = MibTableColumn
cfprApSysdebugTechSupportDn = _CfprApSysdebugTechSupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 2),
    _CfprApSysdebugTechSupportDn_Type()
)
cfprApSysdebugTechSupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportDn.setStatus("current")
_CfprApSysdebugTechSupportRn_Type = SnmpAdminString
_CfprApSysdebugTechSupportRn_Object = MibTableColumn
cfprApSysdebugTechSupportRn = _CfprApSysdebugTechSupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 3),
    _CfprApSysdebugTechSupportRn_Type()
)
cfprApSysdebugTechSupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportRn.setStatus("current")
_CfprApSysdebugTechSupportAdminState_Type = CfprApSysdebugTechSupportAdminState
_CfprApSysdebugTechSupportAdminState_Object = MibTableColumn
cfprApSysdebugTechSupportAdminState = _CfprApSysdebugTechSupportAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 4),
    _CfprApSysdebugTechSupportAdminState_Type()
)
cfprApSysdebugTechSupportAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportAdminState.setStatus("current")
_CfprApSysdebugTechSupportCreationTS_Type = Unsigned64
_CfprApSysdebugTechSupportCreationTS_Object = MibTableColumn
cfprApSysdebugTechSupportCreationTS = _CfprApSysdebugTechSupportCreationTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 5),
    _CfprApSysdebugTechSupportCreationTS_Type()
)
cfprApSysdebugTechSupportCreationTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCreationTS.setStatus("current")
_CfprApSysdebugTechSupportDescr_Type = SnmpAdminString
_CfprApSysdebugTechSupportDescr_Object = MibTableColumn
cfprApSysdebugTechSupportDescr = _CfprApSysdebugTechSupportDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 6),
    _CfprApSysdebugTechSupportDescr_Type()
)
cfprApSysdebugTechSupportDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportDescr.setStatus("current")
_CfprApSysdebugTechSupportFsmDescr_Type = SnmpAdminString
_CfprApSysdebugTechSupportFsmDescr_Object = MibTableColumn
cfprApSysdebugTechSupportFsmDescr = _CfprApSysdebugTechSupportFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 7),
    _CfprApSysdebugTechSupportFsmDescr_Type()
)
cfprApSysdebugTechSupportFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmDescr.setStatus("current")
_CfprApSysdebugTechSupportFsmPrev_Type = SnmpAdminString
_CfprApSysdebugTechSupportFsmPrev_Object = MibTableColumn
cfprApSysdebugTechSupportFsmPrev = _CfprApSysdebugTechSupportFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 8),
    _CfprApSysdebugTechSupportFsmPrev_Type()
)
cfprApSysdebugTechSupportFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmPrev.setStatus("current")
_CfprApSysdebugTechSupportFsmProgr_Type = Gauge32
_CfprApSysdebugTechSupportFsmProgr_Object = MibTableColumn
cfprApSysdebugTechSupportFsmProgr = _CfprApSysdebugTechSupportFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 9),
    _CfprApSysdebugTechSupportFsmProgr_Type()
)
cfprApSysdebugTechSupportFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmProgr.setStatus("current")
_CfprApSysdebugTechSupportFsmRmtInvErrCode_Type = Gauge32
_CfprApSysdebugTechSupportFsmRmtInvErrCode_Object = MibTableColumn
cfprApSysdebugTechSupportFsmRmtInvErrCode = _CfprApSysdebugTechSupportFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 10),
    _CfprApSysdebugTechSupportFsmRmtInvErrCode_Type()
)
cfprApSysdebugTechSupportFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmRmtInvErrCode.setStatus("current")
_CfprApSysdebugTechSupportFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSysdebugTechSupportFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSysdebugTechSupportFsmRmtInvErrDescr = _CfprApSysdebugTechSupportFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 11),
    _CfprApSysdebugTechSupportFsmRmtInvErrDescr_Type()
)
cfprApSysdebugTechSupportFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmRmtInvErrDescr.setStatus("current")
_CfprApSysdebugTechSupportFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysdebugTechSupportFsmRmtInvRslt_Object = MibTableColumn
cfprApSysdebugTechSupportFsmRmtInvRslt = _CfprApSysdebugTechSupportFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 12),
    _CfprApSysdebugTechSupportFsmRmtInvRslt_Type()
)
cfprApSysdebugTechSupportFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmRmtInvRslt.setStatus("current")
_CfprApSysdebugTechSupportFsmStageDescr_Type = SnmpAdminString
_CfprApSysdebugTechSupportFsmStageDescr_Object = MibTableColumn
cfprApSysdebugTechSupportFsmStageDescr = _CfprApSysdebugTechSupportFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 13),
    _CfprApSysdebugTechSupportFsmStageDescr_Type()
)
cfprApSysdebugTechSupportFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStageDescr.setStatus("current")
_CfprApSysdebugTechSupportFsmStamp_Type = DateAndTime
_CfprApSysdebugTechSupportFsmStamp_Object = MibTableColumn
cfprApSysdebugTechSupportFsmStamp = _CfprApSysdebugTechSupportFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 14),
    _CfprApSysdebugTechSupportFsmStamp_Type()
)
cfprApSysdebugTechSupportFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStamp.setStatus("current")
_CfprApSysdebugTechSupportFsmStatus_Type = SnmpAdminString
_CfprApSysdebugTechSupportFsmStatus_Object = MibTableColumn
cfprApSysdebugTechSupportFsmStatus = _CfprApSysdebugTechSupportFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 15),
    _CfprApSysdebugTechSupportFsmStatus_Type()
)
cfprApSysdebugTechSupportFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStatus.setStatus("current")
_CfprApSysdebugTechSupportFsmTry_Type = Gauge32
_CfprApSysdebugTechSupportFsmTry_Object = MibTableColumn
cfprApSysdebugTechSupportFsmTry = _CfprApSysdebugTechSupportFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 16),
    _CfprApSysdebugTechSupportFsmTry_Type()
)
cfprApSysdebugTechSupportFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmTry.setStatus("current")
_CfprApSysdebugTechSupportName_Type = SnmpAdminString
_CfprApSysdebugTechSupportName_Object = MibTableColumn
cfprApSysdebugTechSupportName = _CfprApSysdebugTechSupportName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 17),
    _CfprApSysdebugTechSupportName_Type()
)
cfprApSysdebugTechSupportName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportName.setStatus("current")
_CfprApSysdebugTechSupportOperState_Type = CfprApSysdebugTechSupportOperState
_CfprApSysdebugTechSupportOperState_Object = MibTableColumn
cfprApSysdebugTechSupportOperState = _CfprApSysdebugTechSupportOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 18),
    _CfprApSysdebugTechSupportOperState_Type()
)
cfprApSysdebugTechSupportOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportOperState.setStatus("current")
_CfprApSysdebugTechSupportSize_Type = Gauge32
_CfprApSysdebugTechSupportSize_Object = MibTableColumn
cfprApSysdebugTechSupportSize = _CfprApSysdebugTechSupportSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 19),
    _CfprApSysdebugTechSupportSize_Type()
)
cfprApSysdebugTechSupportSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportSize.setStatus("current")
_CfprApSysdebugTechSupportSwitchId_Type = CfprApNetworkSwitchId
_CfprApSysdebugTechSupportSwitchId_Object = MibTableColumn
cfprApSysdebugTechSupportSwitchId = _CfprApSysdebugTechSupportSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 20),
    _CfprApSysdebugTechSupportSwitchId_Type()
)
cfprApSysdebugTechSupportSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportSwitchId.setStatus("current")
_CfprApSysdebugTechSupportTs_Type = DateAndTime
_CfprApSysdebugTechSupportTs_Object = MibTableColumn
cfprApSysdebugTechSupportTs = _CfprApSysdebugTechSupportTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 21),
    _CfprApSysdebugTechSupportTs_Type()
)
cfprApSysdebugTechSupportTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportTs.setStatus("current")
_CfprApSysdebugTechSupportUri_Type = SnmpAdminString
_CfprApSysdebugTechSupportUri_Object = MibTableColumn
cfprApSysdebugTechSupportUri = _CfprApSysdebugTechSupportUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 32, 1, 22),
    _CfprApSysdebugTechSupportUri_Type()
)
cfprApSysdebugTechSupportUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportUri.setStatus("current")
_CfprApSysdebugTechSupportCmdOptTable_Object = MibTable
cfprApSysdebugTechSupportCmdOptTable = _CfprApSysdebugTechSupportCmdOptTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33)
)
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptTable.setStatus("current")
_CfprApSysdebugTechSupportCmdOptEntry_Object = MibTableRow
cfprApSysdebugTechSupportCmdOptEntry = _CfprApSysdebugTechSupportCmdOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33, 1)
)
cfprApSysdebugTechSupportCmdOptEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugTechSupportCmdOptInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptEntry.setStatus("current")
_CfprApSysdebugTechSupportCmdOptInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugTechSupportCmdOptInstanceId_Object = MibTableColumn
cfprApSysdebugTechSupportCmdOptInstanceId = _CfprApSysdebugTechSupportCmdOptInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33, 1, 1),
    _CfprApSysdebugTechSupportCmdOptInstanceId_Type()
)
cfprApSysdebugTechSupportCmdOptInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptInstanceId.setStatus("current")
_CfprApSysdebugTechSupportCmdOptDn_Type = CfprApManagedObjectDn
_CfprApSysdebugTechSupportCmdOptDn_Object = MibTableColumn
cfprApSysdebugTechSupportCmdOptDn = _CfprApSysdebugTechSupportCmdOptDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33, 1, 2),
    _CfprApSysdebugTechSupportCmdOptDn_Type()
)
cfprApSysdebugTechSupportCmdOptDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptDn.setStatus("current")
_CfprApSysdebugTechSupportCmdOptRn_Type = SnmpAdminString
_CfprApSysdebugTechSupportCmdOptRn_Object = MibTableColumn
cfprApSysdebugTechSupportCmdOptRn = _CfprApSysdebugTechSupportCmdOptRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33, 1, 3),
    _CfprApSysdebugTechSupportCmdOptRn_Type()
)
cfprApSysdebugTechSupportCmdOptRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptRn.setStatus("current")
_CfprApSysdebugTechSupportCmdOptChassisCimcId_Type = Gauge32
_CfprApSysdebugTechSupportCmdOptChassisCimcId_Object = MibTableColumn
cfprApSysdebugTechSupportCmdOptChassisCimcId = _CfprApSysdebugTechSupportCmdOptChassisCimcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33, 1, 4),
    _CfprApSysdebugTechSupportCmdOptChassisCimcId_Type()
)
cfprApSysdebugTechSupportCmdOptChassisCimcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptChassisCimcId.setStatus("current")
_CfprApSysdebugTechSupportCmdOptChassisId_Type = Gauge32
_CfprApSysdebugTechSupportCmdOptChassisId_Object = MibTableColumn
cfprApSysdebugTechSupportCmdOptChassisId = _CfprApSysdebugTechSupportCmdOptChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33, 1, 5),
    _CfprApSysdebugTechSupportCmdOptChassisId_Type()
)
cfprApSysdebugTechSupportCmdOptChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptChassisId.setStatus("current")
_CfprApSysdebugTechSupportCmdOptChassisIomId_Type = Gauge32
_CfprApSysdebugTechSupportCmdOptChassisIomId_Object = MibTableColumn
cfprApSysdebugTechSupportCmdOptChassisIomId = _CfprApSysdebugTechSupportCmdOptChassisIomId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33, 1, 6),
    _CfprApSysdebugTechSupportCmdOptChassisIomId_Type()
)
cfprApSysdebugTechSupportCmdOptChassisIomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptChassisIomId.setStatus("current")
_CfprApSysdebugTechSupportCmdOptCimcAdapterId_Type = Gauge32
_CfprApSysdebugTechSupportCmdOptCimcAdapterId_Object = MibTableColumn
cfprApSysdebugTechSupportCmdOptCimcAdapterId = _CfprApSysdebugTechSupportCmdOptCimcAdapterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33, 1, 7),
    _CfprApSysdebugTechSupportCmdOptCimcAdapterId_Type()
)
cfprApSysdebugTechSupportCmdOptCimcAdapterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptCimcAdapterId.setStatus("current")
_CfprApSysdebugTechSupportCmdOptFabExtId_Type = Gauge32
_CfprApSysdebugTechSupportCmdOptFabExtId_Object = MibTableColumn
cfprApSysdebugTechSupportCmdOptFabExtId = _CfprApSysdebugTechSupportCmdOptFabExtId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33, 1, 8),
    _CfprApSysdebugTechSupportCmdOptFabExtId_Type()
)
cfprApSysdebugTechSupportCmdOptFabExtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptFabExtId.setStatus("current")
_CfprApSysdebugTechSupportCmdOptMajorOptType_Type = CfprApSysdebugTSCmdOptMajorType
_CfprApSysdebugTechSupportCmdOptMajorOptType_Object = MibTableColumn
cfprApSysdebugTechSupportCmdOptMajorOptType = _CfprApSysdebugTechSupportCmdOptMajorOptType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33, 1, 9),
    _CfprApSysdebugTechSupportCmdOptMajorOptType_Type()
)
cfprApSysdebugTechSupportCmdOptMajorOptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptMajorOptType.setStatus("current")
_CfprApSysdebugTechSupportCmdOptRackServerAdapterId_Type = Gauge32
_CfprApSysdebugTechSupportCmdOptRackServerAdapterId_Object = MibTableColumn
cfprApSysdebugTechSupportCmdOptRackServerAdapterId = _CfprApSysdebugTechSupportCmdOptRackServerAdapterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33, 1, 10),
    _CfprApSysdebugTechSupportCmdOptRackServerAdapterId_Type()
)
cfprApSysdebugTechSupportCmdOptRackServerAdapterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptRackServerAdapterId.setStatus("current")
_CfprApSysdebugTechSupportCmdOptRackServerId_Type = Gauge32
_CfprApSysdebugTechSupportCmdOptRackServerId_Object = MibTableColumn
cfprApSysdebugTechSupportCmdOptRackServerId = _CfprApSysdebugTechSupportCmdOptRackServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 33, 1, 11),
    _CfprApSysdebugTechSupportCmdOptRackServerId_Type()
)
cfprApSysdebugTechSupportCmdOptRackServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportCmdOptRackServerId.setStatus("current")
_CfprApSysdebugTechSupportFsmTable_Object = MibTable
cfprApSysdebugTechSupportFsmTable = _CfprApSysdebugTechSupportFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34)
)
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmTable.setStatus("current")
_CfprApSysdebugTechSupportFsmEntry_Object = MibTableRow
cfprApSysdebugTechSupportFsmEntry = _CfprApSysdebugTechSupportFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34, 1)
)
cfprApSysdebugTechSupportFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugTechSupportFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmEntry.setStatus("current")
_CfprApSysdebugTechSupportFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugTechSupportFsmInstanceId_Object = MibTableColumn
cfprApSysdebugTechSupportFsmInstanceId = _CfprApSysdebugTechSupportFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34, 1, 1),
    _CfprApSysdebugTechSupportFsmInstanceId_Type()
)
cfprApSysdebugTechSupportFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmInstanceId.setStatus("current")
_CfprApSysdebugTechSupportFsmDn_Type = CfprApManagedObjectDn
_CfprApSysdebugTechSupportFsmDn_Object = MibTableColumn
cfprApSysdebugTechSupportFsmDn = _CfprApSysdebugTechSupportFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34, 1, 2),
    _CfprApSysdebugTechSupportFsmDn_Type()
)
cfprApSysdebugTechSupportFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmDn.setStatus("current")
_CfprApSysdebugTechSupportFsmRn_Type = SnmpAdminString
_CfprApSysdebugTechSupportFsmRn_Object = MibTableColumn
cfprApSysdebugTechSupportFsmRn = _CfprApSysdebugTechSupportFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34, 1, 3),
    _CfprApSysdebugTechSupportFsmRn_Type()
)
cfprApSysdebugTechSupportFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmRn.setStatus("current")
_CfprApSysdebugTechSupportFsmCompletionTime_Type = DateAndTime
_CfprApSysdebugTechSupportFsmCompletionTime_Object = MibTableColumn
cfprApSysdebugTechSupportFsmCompletionTime = _CfprApSysdebugTechSupportFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34, 1, 4),
    _CfprApSysdebugTechSupportFsmCompletionTime_Type()
)
cfprApSysdebugTechSupportFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmCompletionTime.setStatus("current")
_CfprApSysdebugTechSupportFsmCurrentFsm_Type = CfprApSysdebugTechSupportFsmCurrentFsm
_CfprApSysdebugTechSupportFsmCurrentFsm_Object = MibTableColumn
cfprApSysdebugTechSupportFsmCurrentFsm = _CfprApSysdebugTechSupportFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34, 1, 5),
    _CfprApSysdebugTechSupportFsmCurrentFsm_Type()
)
cfprApSysdebugTechSupportFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmCurrentFsm.setStatus("current")
_CfprApSysdebugTechSupportFsmDescrData_Type = SnmpAdminString
_CfprApSysdebugTechSupportFsmDescrData_Object = MibTableColumn
cfprApSysdebugTechSupportFsmDescrData = _CfprApSysdebugTechSupportFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34, 1, 6),
    _CfprApSysdebugTechSupportFsmDescrData_Type()
)
cfprApSysdebugTechSupportFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmDescrData.setStatus("current")
_CfprApSysdebugTechSupportFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysdebugTechSupportFsmFsmStatus_Object = MibTableColumn
cfprApSysdebugTechSupportFsmFsmStatus = _CfprApSysdebugTechSupportFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34, 1, 7),
    _CfprApSysdebugTechSupportFsmFsmStatus_Type()
)
cfprApSysdebugTechSupportFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmFsmStatus.setStatus("current")
_CfprApSysdebugTechSupportFsmProgress_Type = Gauge32
_CfprApSysdebugTechSupportFsmProgress_Object = MibTableColumn
cfprApSysdebugTechSupportFsmProgress = _CfprApSysdebugTechSupportFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34, 1, 8),
    _CfprApSysdebugTechSupportFsmProgress_Type()
)
cfprApSysdebugTechSupportFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmProgress.setStatus("current")
_CfprApSysdebugTechSupportFsmRmtErrCode_Type = Gauge32
_CfprApSysdebugTechSupportFsmRmtErrCode_Object = MibTableColumn
cfprApSysdebugTechSupportFsmRmtErrCode = _CfprApSysdebugTechSupportFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34, 1, 9),
    _CfprApSysdebugTechSupportFsmRmtErrCode_Type()
)
cfprApSysdebugTechSupportFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmRmtErrCode.setStatus("current")
_CfprApSysdebugTechSupportFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSysdebugTechSupportFsmRmtErrDescr_Object = MibTableColumn
cfprApSysdebugTechSupportFsmRmtErrDescr = _CfprApSysdebugTechSupportFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34, 1, 10),
    _CfprApSysdebugTechSupportFsmRmtErrDescr_Type()
)
cfprApSysdebugTechSupportFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmRmtErrDescr.setStatus("current")
_CfprApSysdebugTechSupportFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSysdebugTechSupportFsmRmtRslt_Object = MibTableColumn
cfprApSysdebugTechSupportFsmRmtRslt = _CfprApSysdebugTechSupportFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 34, 1, 11),
    _CfprApSysdebugTechSupportFsmRmtRslt_Type()
)
cfprApSysdebugTechSupportFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmRmtRslt.setStatus("current")
_CfprApSysdebugTechSupportFsmStageTable_Object = MibTable
cfprApSysdebugTechSupportFsmStageTable = _CfprApSysdebugTechSupportFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 35)
)
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStageTable.setStatus("current")
_CfprApSysdebugTechSupportFsmStageEntry_Object = MibTableRow
cfprApSysdebugTechSupportFsmStageEntry = _CfprApSysdebugTechSupportFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 35, 1)
)
cfprApSysdebugTechSupportFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugTechSupportFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStageEntry.setStatus("current")
_CfprApSysdebugTechSupportFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugTechSupportFsmStageInstanceId_Object = MibTableColumn
cfprApSysdebugTechSupportFsmStageInstanceId = _CfprApSysdebugTechSupportFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 35, 1, 1),
    _CfprApSysdebugTechSupportFsmStageInstanceId_Type()
)
cfprApSysdebugTechSupportFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStageInstanceId.setStatus("current")
_CfprApSysdebugTechSupportFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSysdebugTechSupportFsmStageDn_Object = MibTableColumn
cfprApSysdebugTechSupportFsmStageDn = _CfprApSysdebugTechSupportFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 35, 1, 2),
    _CfprApSysdebugTechSupportFsmStageDn_Type()
)
cfprApSysdebugTechSupportFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStageDn.setStatus("current")
_CfprApSysdebugTechSupportFsmStageRn_Type = SnmpAdminString
_CfprApSysdebugTechSupportFsmStageRn_Object = MibTableColumn
cfprApSysdebugTechSupportFsmStageRn = _CfprApSysdebugTechSupportFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 35, 1, 3),
    _CfprApSysdebugTechSupportFsmStageRn_Type()
)
cfprApSysdebugTechSupportFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStageRn.setStatus("current")
_CfprApSysdebugTechSupportFsmStageDescrData_Type = SnmpAdminString
_CfprApSysdebugTechSupportFsmStageDescrData_Object = MibTableColumn
cfprApSysdebugTechSupportFsmStageDescrData = _CfprApSysdebugTechSupportFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 35, 1, 4),
    _CfprApSysdebugTechSupportFsmStageDescrData_Type()
)
cfprApSysdebugTechSupportFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStageDescrData.setStatus("current")
_CfprApSysdebugTechSupportFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSysdebugTechSupportFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSysdebugTechSupportFsmStageLastUpdateTime = _CfprApSysdebugTechSupportFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 35, 1, 5),
    _CfprApSysdebugTechSupportFsmStageLastUpdateTime_Type()
)
cfprApSysdebugTechSupportFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStageLastUpdateTime.setStatus("current")
_CfprApSysdebugTechSupportFsmStageName_Type = CfprApSysdebugTechSupportFsmStageName
_CfprApSysdebugTechSupportFsmStageName_Object = MibTableColumn
cfprApSysdebugTechSupportFsmStageName = _CfprApSysdebugTechSupportFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 35, 1, 6),
    _CfprApSysdebugTechSupportFsmStageName_Type()
)
cfprApSysdebugTechSupportFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStageName.setStatus("current")
_CfprApSysdebugTechSupportFsmStageOrder_Type = Gauge32
_CfprApSysdebugTechSupportFsmStageOrder_Object = MibTableColumn
cfprApSysdebugTechSupportFsmStageOrder = _CfprApSysdebugTechSupportFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 35, 1, 7),
    _CfprApSysdebugTechSupportFsmStageOrder_Type()
)
cfprApSysdebugTechSupportFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStageOrder.setStatus("current")
_CfprApSysdebugTechSupportFsmStageRetry_Type = Gauge32
_CfprApSysdebugTechSupportFsmStageRetry_Object = MibTableColumn
cfprApSysdebugTechSupportFsmStageRetry = _CfprApSysdebugTechSupportFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 35, 1, 8),
    _CfprApSysdebugTechSupportFsmStageRetry_Type()
)
cfprApSysdebugTechSupportFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStageRetry.setStatus("current")
_CfprApSysdebugTechSupportFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSysdebugTechSupportFsmStageStageStatus_Object = MibTableColumn
cfprApSysdebugTechSupportFsmStageStageStatus = _CfprApSysdebugTechSupportFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 35, 1, 9),
    _CfprApSysdebugTechSupportFsmStageStageStatus_Type()
)
cfprApSysdebugTechSupportFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmStageStageStatus.setStatus("current")
_CfprApSysdebugTechSupportFsmTaskTable_Object = MibTable
cfprApSysdebugTechSupportFsmTaskTable = _CfprApSysdebugTechSupportFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 36)
)
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmTaskTable.setStatus("current")
_CfprApSysdebugTechSupportFsmTaskEntry_Object = MibTableRow
cfprApSysdebugTechSupportFsmTaskEntry = _CfprApSysdebugTechSupportFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 36, 1)
)
cfprApSysdebugTechSupportFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SYSDEBUG-MIB", "cfprApSysdebugTechSupportFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmTaskEntry.setStatus("current")
_CfprApSysdebugTechSupportFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSysdebugTechSupportFsmTaskInstanceId_Object = MibTableColumn
cfprApSysdebugTechSupportFsmTaskInstanceId = _CfprApSysdebugTechSupportFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 36, 1, 1),
    _CfprApSysdebugTechSupportFsmTaskInstanceId_Type()
)
cfprApSysdebugTechSupportFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmTaskInstanceId.setStatus("current")
_CfprApSysdebugTechSupportFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSysdebugTechSupportFsmTaskDn_Object = MibTableColumn
cfprApSysdebugTechSupportFsmTaskDn = _CfprApSysdebugTechSupportFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 36, 1, 2),
    _CfprApSysdebugTechSupportFsmTaskDn_Type()
)
cfprApSysdebugTechSupportFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmTaskDn.setStatus("current")
_CfprApSysdebugTechSupportFsmTaskRn_Type = SnmpAdminString
_CfprApSysdebugTechSupportFsmTaskRn_Object = MibTableColumn
cfprApSysdebugTechSupportFsmTaskRn = _CfprApSysdebugTechSupportFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 36, 1, 3),
    _CfprApSysdebugTechSupportFsmTaskRn_Type()
)
cfprApSysdebugTechSupportFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmTaskRn.setStatus("current")
_CfprApSysdebugTechSupportFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSysdebugTechSupportFsmTaskCompletion_Object = MibTableColumn
cfprApSysdebugTechSupportFsmTaskCompletion = _CfprApSysdebugTechSupportFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 36, 1, 4),
    _CfprApSysdebugTechSupportFsmTaskCompletion_Type()
)
cfprApSysdebugTechSupportFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmTaskCompletion.setStatus("current")
_CfprApSysdebugTechSupportFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSysdebugTechSupportFsmTaskFlags_Object = MibTableColumn
cfprApSysdebugTechSupportFsmTaskFlags = _CfprApSysdebugTechSupportFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 36, 1, 5),
    _CfprApSysdebugTechSupportFsmTaskFlags_Type()
)
cfprApSysdebugTechSupportFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmTaskFlags.setStatus("current")
_CfprApSysdebugTechSupportFsmTaskItem_Type = CfprApSysdebugTechSupportFsmTaskItem
_CfprApSysdebugTechSupportFsmTaskItem_Object = MibTableColumn
cfprApSysdebugTechSupportFsmTaskItem = _CfprApSysdebugTechSupportFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 36, 1, 6),
    _CfprApSysdebugTechSupportFsmTaskItem_Type()
)
cfprApSysdebugTechSupportFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmTaskItem.setStatus("current")
_CfprApSysdebugTechSupportFsmTaskSeqId_Type = Gauge32
_CfprApSysdebugTechSupportFsmTaskSeqId_Object = MibTableColumn
cfprApSysdebugTechSupportFsmTaskSeqId = _CfprApSysdebugTechSupportFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 76, 36, 1, 7),
    _CfprApSysdebugTechSupportFsmTaskSeqId_Type()
)
cfprApSysdebugTechSupportFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSysdebugTechSupportFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-SYSDEBUG-MIB",
    **{"cfprApSysdebugObjects": cfprApSysdebugObjects,
       "cfprApSysdebugAutoCoreFileExportTargetTable": cfprApSysdebugAutoCoreFileExportTargetTable,
       "cfprApSysdebugAutoCoreFileExportTargetEntry": cfprApSysdebugAutoCoreFileExportTargetEntry,
       "cfprApSysdebugAutoCoreFileExportTargetInstanceId": cfprApSysdebugAutoCoreFileExportTargetInstanceId,
       "cfprApSysdebugAutoCoreFileExportTargetDn": cfprApSysdebugAutoCoreFileExportTargetDn,
       "cfprApSysdebugAutoCoreFileExportTargetRn": cfprApSysdebugAutoCoreFileExportTargetRn,
       "cfprApSysdebugAutoCoreFileExportTargetAdminState": cfprApSysdebugAutoCoreFileExportTargetAdminState,
       "cfprApSysdebugAutoCoreFileExportTargetDescr": cfprApSysdebugAutoCoreFileExportTargetDescr,
       "cfprApSysdebugAutoCoreFileExportTargetExportFailureReason": cfprApSysdebugAutoCoreFileExportTargetExportFailureReason,
       "cfprApSysdebugAutoCoreFileExportTargetExportStatus": cfprApSysdebugAutoCoreFileExportTargetExportStatus,
       "cfprApSysdebugAutoCoreFileExportTargetFsmDescr": cfprApSysdebugAutoCoreFileExportTargetFsmDescr,
       "cfprApSysdebugAutoCoreFileExportTargetFsmPrev": cfprApSysdebugAutoCoreFileExportTargetFsmPrev,
       "cfprApSysdebugAutoCoreFileExportTargetFsmProgr": cfprApSysdebugAutoCoreFileExportTargetFsmProgr,
       "cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode": cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode,
       "cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr": cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr,
       "cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvRslt": cfprApSysdebugAutoCoreFileExportTargetFsmRmtInvRslt,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStageDescr": cfprApSysdebugAutoCoreFileExportTargetFsmStageDescr,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStamp": cfprApSysdebugAutoCoreFileExportTargetFsmStamp,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStatus": cfprApSysdebugAutoCoreFileExportTargetFsmStatus,
       "cfprApSysdebugAutoCoreFileExportTargetFsmTry": cfprApSysdebugAutoCoreFileExportTargetFsmTry,
       "cfprApSysdebugAutoCoreFileExportTargetHostname": cfprApSysdebugAutoCoreFileExportTargetHostname,
       "cfprApSysdebugAutoCoreFileExportTargetIntId": cfprApSysdebugAutoCoreFileExportTargetIntId,
       "cfprApSysdebugAutoCoreFileExportTargetName": cfprApSysdebugAutoCoreFileExportTargetName,
       "cfprApSysdebugAutoCoreFileExportTargetPath": cfprApSysdebugAutoCoreFileExportTargetPath,
       "cfprApSysdebugAutoCoreFileExportTargetPolicyLevel": cfprApSysdebugAutoCoreFileExportTargetPolicyLevel,
       "cfprApSysdebugAutoCoreFileExportTargetPolicyOwner": cfprApSysdebugAutoCoreFileExportTargetPolicyOwner,
       "cfprApSysdebugAutoCoreFileExportTargetPort": cfprApSysdebugAutoCoreFileExportTargetPort,
       "cfprApSysdebugAutoCoreFileExportTargetPostAction": cfprApSysdebugAutoCoreFileExportTargetPostAction,
       "cfprApSysdebugAutoCoreFileExportTargetProto": cfprApSysdebugAutoCoreFileExportTargetProto,
       "cfprApSysdebugAutoCoreFileExportTargetFsmTable": cfprApSysdebugAutoCoreFileExportTargetFsmTable,
       "cfprApSysdebugAutoCoreFileExportTargetFsmEntry": cfprApSysdebugAutoCoreFileExportTargetFsmEntry,
       "cfprApSysdebugAutoCoreFileExportTargetFsmInstanceId": cfprApSysdebugAutoCoreFileExportTargetFsmInstanceId,
       "cfprApSysdebugAutoCoreFileExportTargetFsmDn": cfprApSysdebugAutoCoreFileExportTargetFsmDn,
       "cfprApSysdebugAutoCoreFileExportTargetFsmRn": cfprApSysdebugAutoCoreFileExportTargetFsmRn,
       "cfprApSysdebugAutoCoreFileExportTargetFsmCompletionTime": cfprApSysdebugAutoCoreFileExportTargetFsmCompletionTime,
       "cfprApSysdebugAutoCoreFileExportTargetFsmCurrentFsm": cfprApSysdebugAutoCoreFileExportTargetFsmCurrentFsm,
       "cfprApSysdebugAutoCoreFileExportTargetFsmDescrData": cfprApSysdebugAutoCoreFileExportTargetFsmDescrData,
       "cfprApSysdebugAutoCoreFileExportTargetFsmFsmStatus": cfprApSysdebugAutoCoreFileExportTargetFsmFsmStatus,
       "cfprApSysdebugAutoCoreFileExportTargetFsmProgress": cfprApSysdebugAutoCoreFileExportTargetFsmProgress,
       "cfprApSysdebugAutoCoreFileExportTargetFsmRmtErrCode": cfprApSysdebugAutoCoreFileExportTargetFsmRmtErrCode,
       "cfprApSysdebugAutoCoreFileExportTargetFsmRmtErrDescr": cfprApSysdebugAutoCoreFileExportTargetFsmRmtErrDescr,
       "cfprApSysdebugAutoCoreFileExportTargetFsmRmtRslt": cfprApSysdebugAutoCoreFileExportTargetFsmRmtRslt,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStageTable": cfprApSysdebugAutoCoreFileExportTargetFsmStageTable,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStageEntry": cfprApSysdebugAutoCoreFileExportTargetFsmStageEntry,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStageInstanceId": cfprApSysdebugAutoCoreFileExportTargetFsmStageInstanceId,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStageDn": cfprApSysdebugAutoCoreFileExportTargetFsmStageDn,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStageRn": cfprApSysdebugAutoCoreFileExportTargetFsmStageRn,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStageDescrData": cfprApSysdebugAutoCoreFileExportTargetFsmStageDescrData,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime": cfprApSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStageName": cfprApSysdebugAutoCoreFileExportTargetFsmStageName,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStageOrder": cfprApSysdebugAutoCoreFileExportTargetFsmStageOrder,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStageRetry": cfprApSysdebugAutoCoreFileExportTargetFsmStageRetry,
       "cfprApSysdebugAutoCoreFileExportTargetFsmStageStageStatus": cfprApSysdebugAutoCoreFileExportTargetFsmStageStageStatus,
       "cfprApSysdebugAutoCoreFileExportTargetFsmTaskTable": cfprApSysdebugAutoCoreFileExportTargetFsmTaskTable,
       "cfprApSysdebugAutoCoreFileExportTargetFsmTaskEntry": cfprApSysdebugAutoCoreFileExportTargetFsmTaskEntry,
       "cfprApSysdebugAutoCoreFileExportTargetFsmTaskInstanceId": cfprApSysdebugAutoCoreFileExportTargetFsmTaskInstanceId,
       "cfprApSysdebugAutoCoreFileExportTargetFsmTaskDn": cfprApSysdebugAutoCoreFileExportTargetFsmTaskDn,
       "cfprApSysdebugAutoCoreFileExportTargetFsmTaskRn": cfprApSysdebugAutoCoreFileExportTargetFsmTaskRn,
       "cfprApSysdebugAutoCoreFileExportTargetFsmTaskCompletion": cfprApSysdebugAutoCoreFileExportTargetFsmTaskCompletion,
       "cfprApSysdebugAutoCoreFileExportTargetFsmTaskFlags": cfprApSysdebugAutoCoreFileExportTargetFsmTaskFlags,
       "cfprApSysdebugAutoCoreFileExportTargetFsmTaskItem": cfprApSysdebugAutoCoreFileExportTargetFsmTaskItem,
       "cfprApSysdebugAutoCoreFileExportTargetFsmTaskSeqId": cfprApSysdebugAutoCoreFileExportTargetFsmTaskSeqId,
       "cfprApSysdebugBackupBehaviorTable": cfprApSysdebugBackupBehaviorTable,
       "cfprApSysdebugBackupBehaviorEntry": cfprApSysdebugBackupBehaviorEntry,
       "cfprApSysdebugBackupBehaviorInstanceId": cfprApSysdebugBackupBehaviorInstanceId,
       "cfprApSysdebugBackupBehaviorDn": cfprApSysdebugBackupBehaviorDn,
       "cfprApSysdebugBackupBehaviorRn": cfprApSysdebugBackupBehaviorRn,
       "cfprApSysdebugBackupBehaviorAction": cfprApSysdebugBackupBehaviorAction,
       "cfprApSysdebugBackupBehaviorClearOnBackup": cfprApSysdebugBackupBehaviorClearOnBackup,
       "cfprApSysdebugBackupBehaviorFormat": cfprApSysdebugBackupBehaviorFormat,
       "cfprApSysdebugBackupBehaviorHostname": cfprApSysdebugBackupBehaviorHostname,
       "cfprApSysdebugBackupBehaviorInterval": cfprApSysdebugBackupBehaviorInterval,
       "cfprApSysdebugBackupBehaviorProto": cfprApSysdebugBackupBehaviorProto,
       "cfprApSysdebugBackupBehaviorPwd": cfprApSysdebugBackupBehaviorPwd,
       "cfprApSysdebugBackupBehaviorRemotePath": cfprApSysdebugBackupBehaviorRemotePath,
       "cfprApSysdebugBackupBehaviorUser": cfprApSysdebugBackupBehaviorUser,
       "cfprApSysdebugCoreTable": cfprApSysdebugCoreTable,
       "cfprApSysdebugCoreEntry": cfprApSysdebugCoreEntry,
       "cfprApSysdebugCoreInstanceId": cfprApSysdebugCoreInstanceId,
       "cfprApSysdebugCoreDn": cfprApSysdebugCoreDn,
       "cfprApSysdebugCoreRn": cfprApSysdebugCoreRn,
       "cfprApSysdebugCoreAdminState": cfprApSysdebugCoreAdminState,
       "cfprApSysdebugCoreDescr": cfprApSysdebugCoreDescr,
       "cfprApSysdebugCoreFsmDescr": cfprApSysdebugCoreFsmDescr,
       "cfprApSysdebugCoreFsmPrev": cfprApSysdebugCoreFsmPrev,
       "cfprApSysdebugCoreFsmProgr": cfprApSysdebugCoreFsmProgr,
       "cfprApSysdebugCoreFsmRmtInvErrCode": cfprApSysdebugCoreFsmRmtInvErrCode,
       "cfprApSysdebugCoreFsmRmtInvErrDescr": cfprApSysdebugCoreFsmRmtInvErrDescr,
       "cfprApSysdebugCoreFsmRmtInvRslt": cfprApSysdebugCoreFsmRmtInvRslt,
       "cfprApSysdebugCoreFsmStageDescr": cfprApSysdebugCoreFsmStageDescr,
       "cfprApSysdebugCoreFsmStamp": cfprApSysdebugCoreFsmStamp,
       "cfprApSysdebugCoreFsmStatus": cfprApSysdebugCoreFsmStatus,
       "cfprApSysdebugCoreFsmTry": cfprApSysdebugCoreFsmTry,
       "cfprApSysdebugCoreName": cfprApSysdebugCoreName,
       "cfprApSysdebugCoreOperState": cfprApSysdebugCoreOperState,
       "cfprApSysdebugCoreSize": cfprApSysdebugCoreSize,
       "cfprApSysdebugCoreSwitchId": cfprApSysdebugCoreSwitchId,
       "cfprApSysdebugCoreTs": cfprApSysdebugCoreTs,
       "cfprApSysdebugCoreUri": cfprApSysdebugCoreUri,
       "cfprApSysdebugCoreFileRepositoryTable": cfprApSysdebugCoreFileRepositoryTable,
       "cfprApSysdebugCoreFileRepositoryEntry": cfprApSysdebugCoreFileRepositoryEntry,
       "cfprApSysdebugCoreFileRepositoryInstanceId": cfprApSysdebugCoreFileRepositoryInstanceId,
       "cfprApSysdebugCoreFileRepositoryDn": cfprApSysdebugCoreFileRepositoryDn,
       "cfprApSysdebugCoreFileRepositoryRn": cfprApSysdebugCoreFileRepositoryRn,
       "cfprApSysdebugCoreFsmTable": cfprApSysdebugCoreFsmTable,
       "cfprApSysdebugCoreFsmEntry": cfprApSysdebugCoreFsmEntry,
       "cfprApSysdebugCoreFsmInstanceId": cfprApSysdebugCoreFsmInstanceId,
       "cfprApSysdebugCoreFsmDn": cfprApSysdebugCoreFsmDn,
       "cfprApSysdebugCoreFsmRn": cfprApSysdebugCoreFsmRn,
       "cfprApSysdebugCoreFsmCompletionTime": cfprApSysdebugCoreFsmCompletionTime,
       "cfprApSysdebugCoreFsmCurrentFsm": cfprApSysdebugCoreFsmCurrentFsm,
       "cfprApSysdebugCoreFsmDescrData": cfprApSysdebugCoreFsmDescrData,
       "cfprApSysdebugCoreFsmFsmStatus": cfprApSysdebugCoreFsmFsmStatus,
       "cfprApSysdebugCoreFsmProgress": cfprApSysdebugCoreFsmProgress,
       "cfprApSysdebugCoreFsmRmtErrCode": cfprApSysdebugCoreFsmRmtErrCode,
       "cfprApSysdebugCoreFsmRmtErrDescr": cfprApSysdebugCoreFsmRmtErrDescr,
       "cfprApSysdebugCoreFsmRmtRslt": cfprApSysdebugCoreFsmRmtRslt,
       "cfprApSysdebugCoreFsmStageTable": cfprApSysdebugCoreFsmStageTable,
       "cfprApSysdebugCoreFsmStageEntry": cfprApSysdebugCoreFsmStageEntry,
       "cfprApSysdebugCoreFsmStageInstanceId": cfprApSysdebugCoreFsmStageInstanceId,
       "cfprApSysdebugCoreFsmStageDn": cfprApSysdebugCoreFsmStageDn,
       "cfprApSysdebugCoreFsmStageRn": cfprApSysdebugCoreFsmStageRn,
       "cfprApSysdebugCoreFsmStageDescrData": cfprApSysdebugCoreFsmStageDescrData,
       "cfprApSysdebugCoreFsmStageLastUpdateTime": cfprApSysdebugCoreFsmStageLastUpdateTime,
       "cfprApSysdebugCoreFsmStageName": cfprApSysdebugCoreFsmStageName,
       "cfprApSysdebugCoreFsmStageOrder": cfprApSysdebugCoreFsmStageOrder,
       "cfprApSysdebugCoreFsmStageRetry": cfprApSysdebugCoreFsmStageRetry,
       "cfprApSysdebugCoreFsmStageStageStatus": cfprApSysdebugCoreFsmStageStageStatus,
       "cfprApSysdebugCoreFsmTaskTable": cfprApSysdebugCoreFsmTaskTable,
       "cfprApSysdebugCoreFsmTaskEntry": cfprApSysdebugCoreFsmTaskEntry,
       "cfprApSysdebugCoreFsmTaskInstanceId": cfprApSysdebugCoreFsmTaskInstanceId,
       "cfprApSysdebugCoreFsmTaskDn": cfprApSysdebugCoreFsmTaskDn,
       "cfprApSysdebugCoreFsmTaskRn": cfprApSysdebugCoreFsmTaskRn,
       "cfprApSysdebugCoreFsmTaskCompletion": cfprApSysdebugCoreFsmTaskCompletion,
       "cfprApSysdebugCoreFsmTaskFlags": cfprApSysdebugCoreFsmTaskFlags,
       "cfprApSysdebugCoreFsmTaskItem": cfprApSysdebugCoreFsmTaskItem,
       "cfprApSysdebugCoreFsmTaskSeqId": cfprApSysdebugCoreFsmTaskSeqId,
       "cfprApSysdebugEpTable": cfprApSysdebugEpTable,
       "cfprApSysdebugEpEntry": cfprApSysdebugEpEntry,
       "cfprApSysdebugEpInstanceId": cfprApSysdebugEpInstanceId,
       "cfprApSysdebugEpDn": cfprApSysdebugEpDn,
       "cfprApSysdebugEpRn": cfprApSysdebugEpRn,
       "cfprApSysdebugLogControlDestinationFileTable": cfprApSysdebugLogControlDestinationFileTable,
       "cfprApSysdebugLogControlDestinationFileEntry": cfprApSysdebugLogControlDestinationFileEntry,
       "cfprApSysdebugLogControlDestinationFileInstanceId": cfprApSysdebugLogControlDestinationFileInstanceId,
       "cfprApSysdebugLogControlDestinationFileDn": cfprApSysdebugLogControlDestinationFileDn,
       "cfprApSysdebugLogControlDestinationFileRn": cfprApSysdebugLogControlDestinationFileRn,
       "cfprApSysdebugLogControlDestinationFileBackupCount": cfprApSysdebugLogControlDestinationFileBackupCount,
       "cfprApSysdebugLogControlDestinationFileDefaultLevel": cfprApSysdebugLogControlDestinationFileDefaultLevel,
       "cfprApSysdebugLogControlDestinationFileDefaultSize": cfprApSysdebugLogControlDestinationFileDefaultSize,
       "cfprApSysdebugLogControlDestinationFileLevel": cfprApSysdebugLogControlDestinationFileLevel,
       "cfprApSysdebugLogControlDestinationFileSize": cfprApSysdebugLogControlDestinationFileSize,
       "cfprApSysdebugLogControlDestinationSyslogTable": cfprApSysdebugLogControlDestinationSyslogTable,
       "cfprApSysdebugLogControlDestinationSyslogEntry": cfprApSysdebugLogControlDestinationSyslogEntry,
       "cfprApSysdebugLogControlDestinationSyslogInstanceId": cfprApSysdebugLogControlDestinationSyslogInstanceId,
       "cfprApSysdebugLogControlDestinationSyslogDn": cfprApSysdebugLogControlDestinationSyslogDn,
       "cfprApSysdebugLogControlDestinationSyslogRn": cfprApSysdebugLogControlDestinationSyslogRn,
       "cfprApSysdebugLogControlDestinationSyslogDefaultLevel": cfprApSysdebugLogControlDestinationSyslogDefaultLevel,
       "cfprApSysdebugLogControlDestinationSyslogLevel": cfprApSysdebugLogControlDestinationSyslogLevel,
       "cfprApSysdebugLogControlDomainTable": cfprApSysdebugLogControlDomainTable,
       "cfprApSysdebugLogControlDomainEntry": cfprApSysdebugLogControlDomainEntry,
       "cfprApSysdebugLogControlDomainInstanceId": cfprApSysdebugLogControlDomainInstanceId,
       "cfprApSysdebugLogControlDomainDn": cfprApSysdebugLogControlDomainDn,
       "cfprApSysdebugLogControlDomainRn": cfprApSysdebugLogControlDomainRn,
       "cfprApSysdebugLogControlDomainLevel": cfprApSysdebugLogControlDomainLevel,
       "cfprApSysdebugLogControlDomainLevelFlag": cfprApSysdebugLogControlDomainLevelFlag,
       "cfprApSysdebugLogControlDomainName": cfprApSysdebugLogControlDomainName,
       "cfprApSysdebugLogControlDomainPersist": cfprApSysdebugLogControlDomainPersist,
       "cfprApSysdebugLogControlDomainReset": cfprApSysdebugLogControlDomainReset,
       "cfprApSysdebugLogControlEpTable": cfprApSysdebugLogControlEpTable,
       "cfprApSysdebugLogControlEpEntry": cfprApSysdebugLogControlEpEntry,
       "cfprApSysdebugLogControlEpInstanceId": cfprApSysdebugLogControlEpInstanceId,
       "cfprApSysdebugLogControlEpDn": cfprApSysdebugLogControlEpDn,
       "cfprApSysdebugLogControlEpRn": cfprApSysdebugLogControlEpRn,
       "cfprApSysdebugLogControlEpFsmDescr": cfprApSysdebugLogControlEpFsmDescr,
       "cfprApSysdebugLogControlEpFsmPrev": cfprApSysdebugLogControlEpFsmPrev,
       "cfprApSysdebugLogControlEpFsmProgr": cfprApSysdebugLogControlEpFsmProgr,
       "cfprApSysdebugLogControlEpFsmRmtInvErrCode": cfprApSysdebugLogControlEpFsmRmtInvErrCode,
       "cfprApSysdebugLogControlEpFsmRmtInvErrDescr": cfprApSysdebugLogControlEpFsmRmtInvErrDescr,
       "cfprApSysdebugLogControlEpFsmRmtInvRslt": cfprApSysdebugLogControlEpFsmRmtInvRslt,
       "cfprApSysdebugLogControlEpFsmStageDescr": cfprApSysdebugLogControlEpFsmStageDescr,
       "cfprApSysdebugLogControlEpFsmStamp": cfprApSysdebugLogControlEpFsmStamp,
       "cfprApSysdebugLogControlEpFsmStatus": cfprApSysdebugLogControlEpFsmStatus,
       "cfprApSysdebugLogControlEpFsmTry": cfprApSysdebugLogControlEpFsmTry,
       "cfprApSysdebugLogControlEpLevel": cfprApSysdebugLogControlEpLevel,
       "cfprApSysdebugLogControlEpLevelFlag": cfprApSysdebugLogControlEpLevelFlag,
       "cfprApSysdebugLogControlEpPersist": cfprApSysdebugLogControlEpPersist,
       "cfprApSysdebugLogControlEpReset": cfprApSysdebugLogControlEpReset,
       "cfprApSysdebugLogControlEpFsmTable": cfprApSysdebugLogControlEpFsmTable,
       "cfprApSysdebugLogControlEpFsmEntry": cfprApSysdebugLogControlEpFsmEntry,
       "cfprApSysdebugLogControlEpFsmInstanceId": cfprApSysdebugLogControlEpFsmInstanceId,
       "cfprApSysdebugLogControlEpFsmDn": cfprApSysdebugLogControlEpFsmDn,
       "cfprApSysdebugLogControlEpFsmRn": cfprApSysdebugLogControlEpFsmRn,
       "cfprApSysdebugLogControlEpFsmCompletionTime": cfprApSysdebugLogControlEpFsmCompletionTime,
       "cfprApSysdebugLogControlEpFsmCurrentFsm": cfprApSysdebugLogControlEpFsmCurrentFsm,
       "cfprApSysdebugLogControlEpFsmDescrData": cfprApSysdebugLogControlEpFsmDescrData,
       "cfprApSysdebugLogControlEpFsmFsmStatus": cfprApSysdebugLogControlEpFsmFsmStatus,
       "cfprApSysdebugLogControlEpFsmProgress": cfprApSysdebugLogControlEpFsmProgress,
       "cfprApSysdebugLogControlEpFsmRmtErrCode": cfprApSysdebugLogControlEpFsmRmtErrCode,
       "cfprApSysdebugLogControlEpFsmRmtErrDescr": cfprApSysdebugLogControlEpFsmRmtErrDescr,
       "cfprApSysdebugLogControlEpFsmRmtRslt": cfprApSysdebugLogControlEpFsmRmtRslt,
       "cfprApSysdebugLogControlEpFsmStageTable": cfprApSysdebugLogControlEpFsmStageTable,
       "cfprApSysdebugLogControlEpFsmStageEntry": cfprApSysdebugLogControlEpFsmStageEntry,
       "cfprApSysdebugLogControlEpFsmStageInstanceId": cfprApSysdebugLogControlEpFsmStageInstanceId,
       "cfprApSysdebugLogControlEpFsmStageDn": cfprApSysdebugLogControlEpFsmStageDn,
       "cfprApSysdebugLogControlEpFsmStageRn": cfprApSysdebugLogControlEpFsmStageRn,
       "cfprApSysdebugLogControlEpFsmStageDescrData": cfprApSysdebugLogControlEpFsmStageDescrData,
       "cfprApSysdebugLogControlEpFsmStageLastUpdateTime": cfprApSysdebugLogControlEpFsmStageLastUpdateTime,
       "cfprApSysdebugLogControlEpFsmStageName": cfprApSysdebugLogControlEpFsmStageName,
       "cfprApSysdebugLogControlEpFsmStageOrder": cfprApSysdebugLogControlEpFsmStageOrder,
       "cfprApSysdebugLogControlEpFsmStageRetry": cfprApSysdebugLogControlEpFsmStageRetry,
       "cfprApSysdebugLogControlEpFsmStageStageStatus": cfprApSysdebugLogControlEpFsmStageStageStatus,
       "cfprApSysdebugLogControlEpFsmTaskTable": cfprApSysdebugLogControlEpFsmTaskTable,
       "cfprApSysdebugLogControlEpFsmTaskEntry": cfprApSysdebugLogControlEpFsmTaskEntry,
       "cfprApSysdebugLogControlEpFsmTaskInstanceId": cfprApSysdebugLogControlEpFsmTaskInstanceId,
       "cfprApSysdebugLogControlEpFsmTaskDn": cfprApSysdebugLogControlEpFsmTaskDn,
       "cfprApSysdebugLogControlEpFsmTaskRn": cfprApSysdebugLogControlEpFsmTaskRn,
       "cfprApSysdebugLogControlEpFsmTaskCompletion": cfprApSysdebugLogControlEpFsmTaskCompletion,
       "cfprApSysdebugLogControlEpFsmTaskFlags": cfprApSysdebugLogControlEpFsmTaskFlags,
       "cfprApSysdebugLogControlEpFsmTaskItem": cfprApSysdebugLogControlEpFsmTaskItem,
       "cfprApSysdebugLogControlEpFsmTaskSeqId": cfprApSysdebugLogControlEpFsmTaskSeqId,
       "cfprApSysdebugLogControlModuleTable": cfprApSysdebugLogControlModuleTable,
       "cfprApSysdebugLogControlModuleEntry": cfprApSysdebugLogControlModuleEntry,
       "cfprApSysdebugLogControlModuleInstanceId": cfprApSysdebugLogControlModuleInstanceId,
       "cfprApSysdebugLogControlModuleDn": cfprApSysdebugLogControlModuleDn,
       "cfprApSysdebugLogControlModuleRn": cfprApSysdebugLogControlModuleRn,
       "cfprApSysdebugLogControlModuleDefaultLevel": cfprApSysdebugLogControlModuleDefaultLevel,
       "cfprApSysdebugLogControlModuleLevel": cfprApSysdebugLogControlModuleLevel,
       "cfprApSysdebugLogControlModuleName": cfprApSysdebugLogControlModuleName,
       "cfprApSysdebugLogControlModuleReset": cfprApSysdebugLogControlModuleReset,
       "cfprApSysdebugLogExportPolicyTable": cfprApSysdebugLogExportPolicyTable,
       "cfprApSysdebugLogExportPolicyEntry": cfprApSysdebugLogExportPolicyEntry,
       "cfprApSysdebugLogExportPolicyInstanceId": cfprApSysdebugLogExportPolicyInstanceId,
       "cfprApSysdebugLogExportPolicyDn": cfprApSysdebugLogExportPolicyDn,
       "cfprApSysdebugLogExportPolicyRn": cfprApSysdebugLogExportPolicyRn,
       "cfprApSysdebugLogExportPolicyAdminState": cfprApSysdebugLogExportPolicyAdminState,
       "cfprApSysdebugLogExportPolicyDescr": cfprApSysdebugLogExportPolicyDescr,
       "cfprApSysdebugLogExportPolicyFsmDescr": cfprApSysdebugLogExportPolicyFsmDescr,
       "cfprApSysdebugLogExportPolicyFsmPrev": cfprApSysdebugLogExportPolicyFsmPrev,
       "cfprApSysdebugLogExportPolicyFsmProgr": cfprApSysdebugLogExportPolicyFsmProgr,
       "cfprApSysdebugLogExportPolicyFsmRmtInvErrCode": cfprApSysdebugLogExportPolicyFsmRmtInvErrCode,
       "cfprApSysdebugLogExportPolicyFsmRmtInvErrDescr": cfprApSysdebugLogExportPolicyFsmRmtInvErrDescr,
       "cfprApSysdebugLogExportPolicyFsmRmtInvRslt": cfprApSysdebugLogExportPolicyFsmRmtInvRslt,
       "cfprApSysdebugLogExportPolicyFsmStageDescr": cfprApSysdebugLogExportPolicyFsmStageDescr,
       "cfprApSysdebugLogExportPolicyFsmStamp": cfprApSysdebugLogExportPolicyFsmStamp,
       "cfprApSysdebugLogExportPolicyFsmStatus": cfprApSysdebugLogExportPolicyFsmStatus,
       "cfprApSysdebugLogExportPolicyFsmTry": cfprApSysdebugLogExportPolicyFsmTry,
       "cfprApSysdebugLogExportPolicyHostname": cfprApSysdebugLogExportPolicyHostname,
       "cfprApSysdebugLogExportPolicyIntId": cfprApSysdebugLogExportPolicyIntId,
       "cfprApSysdebugLogExportPolicyName": cfprApSysdebugLogExportPolicyName,
       "cfprApSysdebugLogExportPolicyPasswordlessSsh": cfprApSysdebugLogExportPolicyPasswordlessSsh,
       "cfprApSysdebugLogExportPolicyPath": cfprApSysdebugLogExportPolicyPath,
       "cfprApSysdebugLogExportPolicyPolicyLevel": cfprApSysdebugLogExportPolicyPolicyLevel,
       "cfprApSysdebugLogExportPolicyPolicyOwner": cfprApSysdebugLogExportPolicyPolicyOwner,
       "cfprApSysdebugLogExportPolicyPostAction": cfprApSysdebugLogExportPolicyPostAction,
       "cfprApSysdebugLogExportPolicyProto": cfprApSysdebugLogExportPolicyProto,
       "cfprApSysdebugLogExportPolicyPwd": cfprApSysdebugLogExportPolicyPwd,
       "cfprApSysdebugLogExportPolicyUser": cfprApSysdebugLogExportPolicyUser,
       "cfprApSysdebugLogExportPolicyFsmTable": cfprApSysdebugLogExportPolicyFsmTable,
       "cfprApSysdebugLogExportPolicyFsmEntry": cfprApSysdebugLogExportPolicyFsmEntry,
       "cfprApSysdebugLogExportPolicyFsmInstanceId": cfprApSysdebugLogExportPolicyFsmInstanceId,
       "cfprApSysdebugLogExportPolicyFsmDn": cfprApSysdebugLogExportPolicyFsmDn,
       "cfprApSysdebugLogExportPolicyFsmRn": cfprApSysdebugLogExportPolicyFsmRn,
       "cfprApSysdebugLogExportPolicyFsmCompletionTime": cfprApSysdebugLogExportPolicyFsmCompletionTime,
       "cfprApSysdebugLogExportPolicyFsmCurrentFsm": cfprApSysdebugLogExportPolicyFsmCurrentFsm,
       "cfprApSysdebugLogExportPolicyFsmDescrData": cfprApSysdebugLogExportPolicyFsmDescrData,
       "cfprApSysdebugLogExportPolicyFsmFsmStatus": cfprApSysdebugLogExportPolicyFsmFsmStatus,
       "cfprApSysdebugLogExportPolicyFsmProgress": cfprApSysdebugLogExportPolicyFsmProgress,
       "cfprApSysdebugLogExportPolicyFsmRmtErrCode": cfprApSysdebugLogExportPolicyFsmRmtErrCode,
       "cfprApSysdebugLogExportPolicyFsmRmtErrDescr": cfprApSysdebugLogExportPolicyFsmRmtErrDescr,
       "cfprApSysdebugLogExportPolicyFsmRmtRslt": cfprApSysdebugLogExportPolicyFsmRmtRslt,
       "cfprApSysdebugLogExportPolicyFsmStageTable": cfprApSysdebugLogExportPolicyFsmStageTable,
       "cfprApSysdebugLogExportPolicyFsmStageEntry": cfprApSysdebugLogExportPolicyFsmStageEntry,
       "cfprApSysdebugLogExportPolicyFsmStageInstanceId": cfprApSysdebugLogExportPolicyFsmStageInstanceId,
       "cfprApSysdebugLogExportPolicyFsmStageDn": cfprApSysdebugLogExportPolicyFsmStageDn,
       "cfprApSysdebugLogExportPolicyFsmStageRn": cfprApSysdebugLogExportPolicyFsmStageRn,
       "cfprApSysdebugLogExportPolicyFsmStageDescrData": cfprApSysdebugLogExportPolicyFsmStageDescrData,
       "cfprApSysdebugLogExportPolicyFsmStageLastUpdateTime": cfprApSysdebugLogExportPolicyFsmStageLastUpdateTime,
       "cfprApSysdebugLogExportPolicyFsmStageName": cfprApSysdebugLogExportPolicyFsmStageName,
       "cfprApSysdebugLogExportPolicyFsmStageOrder": cfprApSysdebugLogExportPolicyFsmStageOrder,
       "cfprApSysdebugLogExportPolicyFsmStageRetry": cfprApSysdebugLogExportPolicyFsmStageRetry,
       "cfprApSysdebugLogExportPolicyFsmStageStageStatus": cfprApSysdebugLogExportPolicyFsmStageStageStatus,
       "cfprApSysdebugLogExportPolicyFsmTaskTable": cfprApSysdebugLogExportPolicyFsmTaskTable,
       "cfprApSysdebugLogExportPolicyFsmTaskEntry": cfprApSysdebugLogExportPolicyFsmTaskEntry,
       "cfprApSysdebugLogExportPolicyFsmTaskInstanceId": cfprApSysdebugLogExportPolicyFsmTaskInstanceId,
       "cfprApSysdebugLogExportPolicyFsmTaskDn": cfprApSysdebugLogExportPolicyFsmTaskDn,
       "cfprApSysdebugLogExportPolicyFsmTaskRn": cfprApSysdebugLogExportPolicyFsmTaskRn,
       "cfprApSysdebugLogExportPolicyFsmTaskCompletion": cfprApSysdebugLogExportPolicyFsmTaskCompletion,
       "cfprApSysdebugLogExportPolicyFsmTaskFlags": cfprApSysdebugLogExportPolicyFsmTaskFlags,
       "cfprApSysdebugLogExportPolicyFsmTaskItem": cfprApSysdebugLogExportPolicyFsmTaskItem,
       "cfprApSysdebugLogExportPolicyFsmTaskSeqId": cfprApSysdebugLogExportPolicyFsmTaskSeqId,
       "cfprApSysdebugLogExportStatusTable": cfprApSysdebugLogExportStatusTable,
       "cfprApSysdebugLogExportStatusEntry": cfprApSysdebugLogExportStatusEntry,
       "cfprApSysdebugLogExportStatusInstanceId": cfprApSysdebugLogExportStatusInstanceId,
       "cfprApSysdebugLogExportStatusDn": cfprApSysdebugLogExportStatusDn,
       "cfprApSysdebugLogExportStatusRn": cfprApSysdebugLogExportStatusRn,
       "cfprApSysdebugLogExportStatusExportFailureReason": cfprApSysdebugLogExportStatusExportFailureReason,
       "cfprApSysdebugLogExportStatusExportStatus": cfprApSysdebugLogExportStatusExportStatus,
       "cfprApSysdebugLogExportStatusSwitchId": cfprApSysdebugLogExportStatusSwitchId,
       "cfprApSysdebugMEpLogTable": cfprApSysdebugMEpLogTable,
       "cfprApSysdebugMEpLogEntry": cfprApSysdebugMEpLogEntry,
       "cfprApSysdebugMEpLogInstanceId": cfprApSysdebugMEpLogInstanceId,
       "cfprApSysdebugMEpLogDn": cfprApSysdebugMEpLogDn,
       "cfprApSysdebugMEpLogRn": cfprApSysdebugMEpLogRn,
       "cfprApSysdebugMEpLogAdminState": cfprApSysdebugMEpLogAdminState,
       "cfprApSysdebugMEpLogCapacity": cfprApSysdebugMEpLogCapacity,
       "cfprApSysdebugMEpLogId": cfprApSysdebugMEpLogId,
       "cfprApSysdebugMEpLogLastUpdate": cfprApSysdebugMEpLogLastUpdate,
       "cfprApSysdebugMEpLogOperState": cfprApSysdebugMEpLogOperState,
       "cfprApSysdebugMEpLogType": cfprApSysdebugMEpLogType,
       "cfprApSysdebugMEpLogPolicyTable": cfprApSysdebugMEpLogPolicyTable,
       "cfprApSysdebugMEpLogPolicyEntry": cfprApSysdebugMEpLogPolicyEntry,
       "cfprApSysdebugMEpLogPolicyInstanceId": cfprApSysdebugMEpLogPolicyInstanceId,
       "cfprApSysdebugMEpLogPolicyDn": cfprApSysdebugMEpLogPolicyDn,
       "cfprApSysdebugMEpLogPolicyRn": cfprApSysdebugMEpLogPolicyRn,
       "cfprApSysdebugMEpLogPolicyDescr": cfprApSysdebugMEpLogPolicyDescr,
       "cfprApSysdebugMEpLogPolicyIntId": cfprApSysdebugMEpLogPolicyIntId,
       "cfprApSysdebugMEpLogPolicyName": cfprApSysdebugMEpLogPolicyName,
       "cfprApSysdebugMEpLogPolicyPolicyLevel": cfprApSysdebugMEpLogPolicyPolicyLevel,
       "cfprApSysdebugMEpLogPolicyPolicyOwner": cfprApSysdebugMEpLogPolicyPolicyOwner,
       "cfprApSysdebugMEpLogPolicyType": cfprApSysdebugMEpLogPolicyType,
       "cfprApSysdebugManualCoreFileExportTargetTable": cfprApSysdebugManualCoreFileExportTargetTable,
       "cfprApSysdebugManualCoreFileExportTargetEntry": cfprApSysdebugManualCoreFileExportTargetEntry,
       "cfprApSysdebugManualCoreFileExportTargetInstanceId": cfprApSysdebugManualCoreFileExportTargetInstanceId,
       "cfprApSysdebugManualCoreFileExportTargetDn": cfprApSysdebugManualCoreFileExportTargetDn,
       "cfprApSysdebugManualCoreFileExportTargetRn": cfprApSysdebugManualCoreFileExportTargetRn,
       "cfprApSysdebugManualCoreFileExportTargetAdminState": cfprApSysdebugManualCoreFileExportTargetAdminState,
       "cfprApSysdebugManualCoreFileExportTargetDescr": cfprApSysdebugManualCoreFileExportTargetDescr,
       "cfprApSysdebugManualCoreFileExportTargetExportFailureReason": cfprApSysdebugManualCoreFileExportTargetExportFailureReason,
       "cfprApSysdebugManualCoreFileExportTargetExportStatus": cfprApSysdebugManualCoreFileExportTargetExportStatus,
       "cfprApSysdebugManualCoreFileExportTargetFsmDescr": cfprApSysdebugManualCoreFileExportTargetFsmDescr,
       "cfprApSysdebugManualCoreFileExportTargetFsmPrev": cfprApSysdebugManualCoreFileExportTargetFsmPrev,
       "cfprApSysdebugManualCoreFileExportTargetFsmProgr": cfprApSysdebugManualCoreFileExportTargetFsmProgr,
       "cfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrCode": cfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrCode,
       "cfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr": cfprApSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr,
       "cfprApSysdebugManualCoreFileExportTargetFsmRmtInvRslt": cfprApSysdebugManualCoreFileExportTargetFsmRmtInvRslt,
       "cfprApSysdebugManualCoreFileExportTargetFsmStageDescr": cfprApSysdebugManualCoreFileExportTargetFsmStageDescr,
       "cfprApSysdebugManualCoreFileExportTargetFsmStamp": cfprApSysdebugManualCoreFileExportTargetFsmStamp,
       "cfprApSysdebugManualCoreFileExportTargetFsmStatus": cfprApSysdebugManualCoreFileExportTargetFsmStatus,
       "cfprApSysdebugManualCoreFileExportTargetFsmTry": cfprApSysdebugManualCoreFileExportTargetFsmTry,
       "cfprApSysdebugManualCoreFileExportTargetHostname": cfprApSysdebugManualCoreFileExportTargetHostname,
       "cfprApSysdebugManualCoreFileExportTargetIntId": cfprApSysdebugManualCoreFileExportTargetIntId,
       "cfprApSysdebugManualCoreFileExportTargetName": cfprApSysdebugManualCoreFileExportTargetName,
       "cfprApSysdebugManualCoreFileExportTargetPath": cfprApSysdebugManualCoreFileExportTargetPath,
       "cfprApSysdebugManualCoreFileExportTargetPolicyLevel": cfprApSysdebugManualCoreFileExportTargetPolicyLevel,
       "cfprApSysdebugManualCoreFileExportTargetPolicyOwner": cfprApSysdebugManualCoreFileExportTargetPolicyOwner,
       "cfprApSysdebugManualCoreFileExportTargetPort": cfprApSysdebugManualCoreFileExportTargetPort,
       "cfprApSysdebugManualCoreFileExportTargetPostAction": cfprApSysdebugManualCoreFileExportTargetPostAction,
       "cfprApSysdebugManualCoreFileExportTargetProto": cfprApSysdebugManualCoreFileExportTargetProto,
       "cfprApSysdebugManualCoreFileExportTargetFsmTable": cfprApSysdebugManualCoreFileExportTargetFsmTable,
       "cfprApSysdebugManualCoreFileExportTargetFsmEntry": cfprApSysdebugManualCoreFileExportTargetFsmEntry,
       "cfprApSysdebugManualCoreFileExportTargetFsmInstanceId": cfprApSysdebugManualCoreFileExportTargetFsmInstanceId,
       "cfprApSysdebugManualCoreFileExportTargetFsmDn": cfprApSysdebugManualCoreFileExportTargetFsmDn,
       "cfprApSysdebugManualCoreFileExportTargetFsmRn": cfprApSysdebugManualCoreFileExportTargetFsmRn,
       "cfprApSysdebugManualCoreFileExportTargetFsmCompletionTime": cfprApSysdebugManualCoreFileExportTargetFsmCompletionTime,
       "cfprApSysdebugManualCoreFileExportTargetFsmCurrentFsm": cfprApSysdebugManualCoreFileExportTargetFsmCurrentFsm,
       "cfprApSysdebugManualCoreFileExportTargetFsmDescrData": cfprApSysdebugManualCoreFileExportTargetFsmDescrData,
       "cfprApSysdebugManualCoreFileExportTargetFsmFsmStatus": cfprApSysdebugManualCoreFileExportTargetFsmFsmStatus,
       "cfprApSysdebugManualCoreFileExportTargetFsmProgress": cfprApSysdebugManualCoreFileExportTargetFsmProgress,
       "cfprApSysdebugManualCoreFileExportTargetFsmRmtErrCode": cfprApSysdebugManualCoreFileExportTargetFsmRmtErrCode,
       "cfprApSysdebugManualCoreFileExportTargetFsmRmtErrDescr": cfprApSysdebugManualCoreFileExportTargetFsmRmtErrDescr,
       "cfprApSysdebugManualCoreFileExportTargetFsmRmtRslt": cfprApSysdebugManualCoreFileExportTargetFsmRmtRslt,
       "cfprApSysdebugManualCoreFileExportTargetFsmStageTable": cfprApSysdebugManualCoreFileExportTargetFsmStageTable,
       "cfprApSysdebugManualCoreFileExportTargetFsmStageEntry": cfprApSysdebugManualCoreFileExportTargetFsmStageEntry,
       "cfprApSysdebugManualCoreFileExportTargetFsmStageInstanceId": cfprApSysdebugManualCoreFileExportTargetFsmStageInstanceId,
       "cfprApSysdebugManualCoreFileExportTargetFsmStageDn": cfprApSysdebugManualCoreFileExportTargetFsmStageDn,
       "cfprApSysdebugManualCoreFileExportTargetFsmStageRn": cfprApSysdebugManualCoreFileExportTargetFsmStageRn,
       "cfprApSysdebugManualCoreFileExportTargetFsmStageDescrData": cfprApSysdebugManualCoreFileExportTargetFsmStageDescrData,
       "cfprApSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime": cfprApSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime,
       "cfprApSysdebugManualCoreFileExportTargetFsmStageName": cfprApSysdebugManualCoreFileExportTargetFsmStageName,
       "cfprApSysdebugManualCoreFileExportTargetFsmStageOrder": cfprApSysdebugManualCoreFileExportTargetFsmStageOrder,
       "cfprApSysdebugManualCoreFileExportTargetFsmStageRetry": cfprApSysdebugManualCoreFileExportTargetFsmStageRetry,
       "cfprApSysdebugManualCoreFileExportTargetFsmStageStageStatus": cfprApSysdebugManualCoreFileExportTargetFsmStageStageStatus,
       "cfprApSysdebugManualCoreFileExportTargetFsmTaskTable": cfprApSysdebugManualCoreFileExportTargetFsmTaskTable,
       "cfprApSysdebugManualCoreFileExportTargetFsmTaskEntry": cfprApSysdebugManualCoreFileExportTargetFsmTaskEntry,
       "cfprApSysdebugManualCoreFileExportTargetFsmTaskInstanceId": cfprApSysdebugManualCoreFileExportTargetFsmTaskInstanceId,
       "cfprApSysdebugManualCoreFileExportTargetFsmTaskDn": cfprApSysdebugManualCoreFileExportTargetFsmTaskDn,
       "cfprApSysdebugManualCoreFileExportTargetFsmTaskRn": cfprApSysdebugManualCoreFileExportTargetFsmTaskRn,
       "cfprApSysdebugManualCoreFileExportTargetFsmTaskCompletion": cfprApSysdebugManualCoreFileExportTargetFsmTaskCompletion,
       "cfprApSysdebugManualCoreFileExportTargetFsmTaskFlags": cfprApSysdebugManualCoreFileExportTargetFsmTaskFlags,
       "cfprApSysdebugManualCoreFileExportTargetFsmTaskItem": cfprApSysdebugManualCoreFileExportTargetFsmTaskItem,
       "cfprApSysdebugManualCoreFileExportTargetFsmTaskSeqId": cfprApSysdebugManualCoreFileExportTargetFsmTaskSeqId,
       "cfprApSysdebugTechSupFileRepositoryTable": cfprApSysdebugTechSupFileRepositoryTable,
       "cfprApSysdebugTechSupFileRepositoryEntry": cfprApSysdebugTechSupFileRepositoryEntry,
       "cfprApSysdebugTechSupFileRepositoryInstanceId": cfprApSysdebugTechSupFileRepositoryInstanceId,
       "cfprApSysdebugTechSupFileRepositoryDn": cfprApSysdebugTechSupFileRepositoryDn,
       "cfprApSysdebugTechSupFileRepositoryRn": cfprApSysdebugTechSupFileRepositoryRn,
       "cfprApSysdebugTechSupportTable": cfprApSysdebugTechSupportTable,
       "cfprApSysdebugTechSupportEntry": cfprApSysdebugTechSupportEntry,
       "cfprApSysdebugTechSupportInstanceId": cfprApSysdebugTechSupportInstanceId,
       "cfprApSysdebugTechSupportDn": cfprApSysdebugTechSupportDn,
       "cfprApSysdebugTechSupportRn": cfprApSysdebugTechSupportRn,
       "cfprApSysdebugTechSupportAdminState": cfprApSysdebugTechSupportAdminState,
       "cfprApSysdebugTechSupportCreationTS": cfprApSysdebugTechSupportCreationTS,
       "cfprApSysdebugTechSupportDescr": cfprApSysdebugTechSupportDescr,
       "cfprApSysdebugTechSupportFsmDescr": cfprApSysdebugTechSupportFsmDescr,
       "cfprApSysdebugTechSupportFsmPrev": cfprApSysdebugTechSupportFsmPrev,
       "cfprApSysdebugTechSupportFsmProgr": cfprApSysdebugTechSupportFsmProgr,
       "cfprApSysdebugTechSupportFsmRmtInvErrCode": cfprApSysdebugTechSupportFsmRmtInvErrCode,
       "cfprApSysdebugTechSupportFsmRmtInvErrDescr": cfprApSysdebugTechSupportFsmRmtInvErrDescr,
       "cfprApSysdebugTechSupportFsmRmtInvRslt": cfprApSysdebugTechSupportFsmRmtInvRslt,
       "cfprApSysdebugTechSupportFsmStageDescr": cfprApSysdebugTechSupportFsmStageDescr,
       "cfprApSysdebugTechSupportFsmStamp": cfprApSysdebugTechSupportFsmStamp,
       "cfprApSysdebugTechSupportFsmStatus": cfprApSysdebugTechSupportFsmStatus,
       "cfprApSysdebugTechSupportFsmTry": cfprApSysdebugTechSupportFsmTry,
       "cfprApSysdebugTechSupportName": cfprApSysdebugTechSupportName,
       "cfprApSysdebugTechSupportOperState": cfprApSysdebugTechSupportOperState,
       "cfprApSysdebugTechSupportSize": cfprApSysdebugTechSupportSize,
       "cfprApSysdebugTechSupportSwitchId": cfprApSysdebugTechSupportSwitchId,
       "cfprApSysdebugTechSupportTs": cfprApSysdebugTechSupportTs,
       "cfprApSysdebugTechSupportUri": cfprApSysdebugTechSupportUri,
       "cfprApSysdebugTechSupportCmdOptTable": cfprApSysdebugTechSupportCmdOptTable,
       "cfprApSysdebugTechSupportCmdOptEntry": cfprApSysdebugTechSupportCmdOptEntry,
       "cfprApSysdebugTechSupportCmdOptInstanceId": cfprApSysdebugTechSupportCmdOptInstanceId,
       "cfprApSysdebugTechSupportCmdOptDn": cfprApSysdebugTechSupportCmdOptDn,
       "cfprApSysdebugTechSupportCmdOptRn": cfprApSysdebugTechSupportCmdOptRn,
       "cfprApSysdebugTechSupportCmdOptChassisCimcId": cfprApSysdebugTechSupportCmdOptChassisCimcId,
       "cfprApSysdebugTechSupportCmdOptChassisId": cfprApSysdebugTechSupportCmdOptChassisId,
       "cfprApSysdebugTechSupportCmdOptChassisIomId": cfprApSysdebugTechSupportCmdOptChassisIomId,
       "cfprApSysdebugTechSupportCmdOptCimcAdapterId": cfprApSysdebugTechSupportCmdOptCimcAdapterId,
       "cfprApSysdebugTechSupportCmdOptFabExtId": cfprApSysdebugTechSupportCmdOptFabExtId,
       "cfprApSysdebugTechSupportCmdOptMajorOptType": cfprApSysdebugTechSupportCmdOptMajorOptType,
       "cfprApSysdebugTechSupportCmdOptRackServerAdapterId": cfprApSysdebugTechSupportCmdOptRackServerAdapterId,
       "cfprApSysdebugTechSupportCmdOptRackServerId": cfprApSysdebugTechSupportCmdOptRackServerId,
       "cfprApSysdebugTechSupportFsmTable": cfprApSysdebugTechSupportFsmTable,
       "cfprApSysdebugTechSupportFsmEntry": cfprApSysdebugTechSupportFsmEntry,
       "cfprApSysdebugTechSupportFsmInstanceId": cfprApSysdebugTechSupportFsmInstanceId,
       "cfprApSysdebugTechSupportFsmDn": cfprApSysdebugTechSupportFsmDn,
       "cfprApSysdebugTechSupportFsmRn": cfprApSysdebugTechSupportFsmRn,
       "cfprApSysdebugTechSupportFsmCompletionTime": cfprApSysdebugTechSupportFsmCompletionTime,
       "cfprApSysdebugTechSupportFsmCurrentFsm": cfprApSysdebugTechSupportFsmCurrentFsm,
       "cfprApSysdebugTechSupportFsmDescrData": cfprApSysdebugTechSupportFsmDescrData,
       "cfprApSysdebugTechSupportFsmFsmStatus": cfprApSysdebugTechSupportFsmFsmStatus,
       "cfprApSysdebugTechSupportFsmProgress": cfprApSysdebugTechSupportFsmProgress,
       "cfprApSysdebugTechSupportFsmRmtErrCode": cfprApSysdebugTechSupportFsmRmtErrCode,
       "cfprApSysdebugTechSupportFsmRmtErrDescr": cfprApSysdebugTechSupportFsmRmtErrDescr,
       "cfprApSysdebugTechSupportFsmRmtRslt": cfprApSysdebugTechSupportFsmRmtRslt,
       "cfprApSysdebugTechSupportFsmStageTable": cfprApSysdebugTechSupportFsmStageTable,
       "cfprApSysdebugTechSupportFsmStageEntry": cfprApSysdebugTechSupportFsmStageEntry,
       "cfprApSysdebugTechSupportFsmStageInstanceId": cfprApSysdebugTechSupportFsmStageInstanceId,
       "cfprApSysdebugTechSupportFsmStageDn": cfprApSysdebugTechSupportFsmStageDn,
       "cfprApSysdebugTechSupportFsmStageRn": cfprApSysdebugTechSupportFsmStageRn,
       "cfprApSysdebugTechSupportFsmStageDescrData": cfprApSysdebugTechSupportFsmStageDescrData,
       "cfprApSysdebugTechSupportFsmStageLastUpdateTime": cfprApSysdebugTechSupportFsmStageLastUpdateTime,
       "cfprApSysdebugTechSupportFsmStageName": cfprApSysdebugTechSupportFsmStageName,
       "cfprApSysdebugTechSupportFsmStageOrder": cfprApSysdebugTechSupportFsmStageOrder,
       "cfprApSysdebugTechSupportFsmStageRetry": cfprApSysdebugTechSupportFsmStageRetry,
       "cfprApSysdebugTechSupportFsmStageStageStatus": cfprApSysdebugTechSupportFsmStageStageStatus,
       "cfprApSysdebugTechSupportFsmTaskTable": cfprApSysdebugTechSupportFsmTaskTable,
       "cfprApSysdebugTechSupportFsmTaskEntry": cfprApSysdebugTechSupportFsmTaskEntry,
       "cfprApSysdebugTechSupportFsmTaskInstanceId": cfprApSysdebugTechSupportFsmTaskInstanceId,
       "cfprApSysdebugTechSupportFsmTaskDn": cfprApSysdebugTechSupportFsmTaskDn,
       "cfprApSysdebugTechSupportFsmTaskRn": cfprApSysdebugTechSupportFsmTaskRn,
       "cfprApSysdebugTechSupportFsmTaskCompletion": cfprApSysdebugTechSupportFsmTaskCompletion,
       "cfprApSysdebugTechSupportFsmTaskFlags": cfprApSysdebugTechSupportFsmTaskFlags,
       "cfprApSysdebugTechSupportFsmTaskItem": cfprApSysdebugTechSupportFsmTaskItem,
       "cfprApSysdebugTechSupportFsmTaskSeqId": cfprApSysdebugTechSupportFsmTaskSeqId}
)
