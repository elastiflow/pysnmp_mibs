# SNMP MIB module (CISCO-FIREPOWER-AP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-STATS-MIB.mib
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
 CfprApConditionSeverity,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApPolicyPolicyOwner,
 CfprApStatsCollectionDomain,
 CfprApStatsCollectionInterval,
 CfprApStatsCollectionPolicyFsmCurrentFsm,
 CfprApStatsCollectionPolicyFsmStageName,
 CfprApStatsCollectionPolicyFsmTaskItem,
 CfprApStatsReportingInterval,
 CfprApStatsThr32DefinitionPropType,
 CfprApStatsThr32ValuePropType,
 CfprApStatsThr64DefinitionPropType,
 CfprApStatsThr64ValuePropType,
 CfprApStatsThrFloatDefinitionPropType,
 CfprApStatsThrFloatValuePropType,
 CfprApStatsThresholdDirection) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApConditionSeverity",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApPolicyPolicyOwner",
    "CfprApStatsCollectionDomain",
    "CfprApStatsCollectionInterval",
    "CfprApStatsCollectionPolicyFsmCurrentFsm",
    "CfprApStatsCollectionPolicyFsmStageName",
    "CfprApStatsCollectionPolicyFsmTaskItem",
    "CfprApStatsReportingInterval",
    "CfprApStatsThr32DefinitionPropType",
    "CfprApStatsThr32ValuePropType",
    "CfprApStatsThr64DefinitionPropType",
    "CfprApStatsThr64ValuePropType",
    "CfprApStatsThrFloatDefinitionPropType",
    "CfprApStatsThrFloatValuePropType",
    "CfprApStatsThresholdDirection")

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

cfprApStatsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApStatsCollectionPolicyTable_Object = MibTable
cfprApStatsCollectionPolicyTable = _CfprApStatsCollectionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1)
)
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyTable.setStatus("current")
_CfprApStatsCollectionPolicyEntry_Object = MibTableRow
cfprApStatsCollectionPolicyEntry = _CfprApStatsCollectionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1)
)
cfprApStatsCollectionPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsCollectionPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyEntry.setStatus("current")
_CfprApStatsCollectionPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApStatsCollectionPolicyInstanceId_Object = MibTableColumn
cfprApStatsCollectionPolicyInstanceId = _CfprApStatsCollectionPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 1),
    _CfprApStatsCollectionPolicyInstanceId_Type()
)
cfprApStatsCollectionPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyInstanceId.setStatus("current")
_CfprApStatsCollectionPolicyDn_Type = CfprApManagedObjectDn
_CfprApStatsCollectionPolicyDn_Object = MibTableColumn
cfprApStatsCollectionPolicyDn = _CfprApStatsCollectionPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 2),
    _CfprApStatsCollectionPolicyDn_Type()
)
cfprApStatsCollectionPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyDn.setStatus("current")
_CfprApStatsCollectionPolicyRn_Type = SnmpAdminString
_CfprApStatsCollectionPolicyRn_Object = MibTableColumn
cfprApStatsCollectionPolicyRn = _CfprApStatsCollectionPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 3),
    _CfprApStatsCollectionPolicyRn_Type()
)
cfprApStatsCollectionPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyRn.setStatus("current")
_CfprApStatsCollectionPolicyCollectionInterval_Type = CfprApStatsCollectionInterval
_CfprApStatsCollectionPolicyCollectionInterval_Object = MibTableColumn
cfprApStatsCollectionPolicyCollectionInterval = _CfprApStatsCollectionPolicyCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 4),
    _CfprApStatsCollectionPolicyCollectionInterval_Type()
)
cfprApStatsCollectionPolicyCollectionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyCollectionInterval.setStatus("current")
_CfprApStatsCollectionPolicyFsmDescr_Type = SnmpAdminString
_CfprApStatsCollectionPolicyFsmDescr_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmDescr = _CfprApStatsCollectionPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 5),
    _CfprApStatsCollectionPolicyFsmDescr_Type()
)
cfprApStatsCollectionPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmDescr.setStatus("current")
_CfprApStatsCollectionPolicyFsmPrev_Type = SnmpAdminString
_CfprApStatsCollectionPolicyFsmPrev_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmPrev = _CfprApStatsCollectionPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 6),
    _CfprApStatsCollectionPolicyFsmPrev_Type()
)
cfprApStatsCollectionPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmPrev.setStatus("current")
_CfprApStatsCollectionPolicyFsmProgr_Type = Gauge32
_CfprApStatsCollectionPolicyFsmProgr_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmProgr = _CfprApStatsCollectionPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 7),
    _CfprApStatsCollectionPolicyFsmProgr_Type()
)
cfprApStatsCollectionPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmProgr.setStatus("current")
_CfprApStatsCollectionPolicyFsmRmtInvErrCode_Type = Gauge32
_CfprApStatsCollectionPolicyFsmRmtInvErrCode_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmRmtInvErrCode = _CfprApStatsCollectionPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 8),
    _CfprApStatsCollectionPolicyFsmRmtInvErrCode_Type()
)
cfprApStatsCollectionPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmRmtInvErrCode.setStatus("current")
_CfprApStatsCollectionPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApStatsCollectionPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmRmtInvErrDescr = _CfprApStatsCollectionPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 9),
    _CfprApStatsCollectionPolicyFsmRmtInvErrDescr_Type()
)
cfprApStatsCollectionPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmRmtInvErrDescr.setStatus("current")
_CfprApStatsCollectionPolicyFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApStatsCollectionPolicyFsmRmtInvRslt_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmRmtInvRslt = _CfprApStatsCollectionPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 10),
    _CfprApStatsCollectionPolicyFsmRmtInvRslt_Type()
)
cfprApStatsCollectionPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmRmtInvRslt.setStatus("current")
_CfprApStatsCollectionPolicyFsmStageDescr_Type = SnmpAdminString
_CfprApStatsCollectionPolicyFsmStageDescr_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmStageDescr = _CfprApStatsCollectionPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 11),
    _CfprApStatsCollectionPolicyFsmStageDescr_Type()
)
cfprApStatsCollectionPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStageDescr.setStatus("current")
_CfprApStatsCollectionPolicyFsmStamp_Type = DateAndTime
_CfprApStatsCollectionPolicyFsmStamp_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmStamp = _CfprApStatsCollectionPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 12),
    _CfprApStatsCollectionPolicyFsmStamp_Type()
)
cfprApStatsCollectionPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStamp.setStatus("current")
_CfprApStatsCollectionPolicyFsmStatus_Type = SnmpAdminString
_CfprApStatsCollectionPolicyFsmStatus_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmStatus = _CfprApStatsCollectionPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 13),
    _CfprApStatsCollectionPolicyFsmStatus_Type()
)
cfprApStatsCollectionPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStatus.setStatus("current")
_CfprApStatsCollectionPolicyFsmTry_Type = Gauge32
_CfprApStatsCollectionPolicyFsmTry_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmTry = _CfprApStatsCollectionPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 14),
    _CfprApStatsCollectionPolicyFsmTry_Type()
)
cfprApStatsCollectionPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmTry.setStatus("current")
_CfprApStatsCollectionPolicyId_Type = Gauge32
_CfprApStatsCollectionPolicyId_Object = MibTableColumn
cfprApStatsCollectionPolicyId = _CfprApStatsCollectionPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 15),
    _CfprApStatsCollectionPolicyId_Type()
)
cfprApStatsCollectionPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyId.setStatus("current")
_CfprApStatsCollectionPolicyName_Type = CfprApStatsCollectionDomain
_CfprApStatsCollectionPolicyName_Object = MibTableColumn
cfprApStatsCollectionPolicyName = _CfprApStatsCollectionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 16),
    _CfprApStatsCollectionPolicyName_Type()
)
cfprApStatsCollectionPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyName.setStatus("current")
_CfprApStatsCollectionPolicyReportingInterval_Type = CfprApStatsReportingInterval
_CfprApStatsCollectionPolicyReportingInterval_Object = MibTableColumn
cfprApStatsCollectionPolicyReportingInterval = _CfprApStatsCollectionPolicyReportingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 1, 1, 17),
    _CfprApStatsCollectionPolicyReportingInterval_Type()
)
cfprApStatsCollectionPolicyReportingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyReportingInterval.setStatus("current")
_CfprApStatsCollectionPolicyFsmTable_Object = MibTable
cfprApStatsCollectionPolicyFsmTable = _CfprApStatsCollectionPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2)
)
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmTable.setStatus("current")
_CfprApStatsCollectionPolicyFsmEntry_Object = MibTableRow
cfprApStatsCollectionPolicyFsmEntry = _CfprApStatsCollectionPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2, 1)
)
cfprApStatsCollectionPolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsCollectionPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmEntry.setStatus("current")
_CfprApStatsCollectionPolicyFsmInstanceId_Type = CfprApManagedObjectId
_CfprApStatsCollectionPolicyFsmInstanceId_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmInstanceId = _CfprApStatsCollectionPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2, 1, 1),
    _CfprApStatsCollectionPolicyFsmInstanceId_Type()
)
cfprApStatsCollectionPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmInstanceId.setStatus("current")
_CfprApStatsCollectionPolicyFsmDn_Type = CfprApManagedObjectDn
_CfprApStatsCollectionPolicyFsmDn_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmDn = _CfprApStatsCollectionPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2, 1, 2),
    _CfprApStatsCollectionPolicyFsmDn_Type()
)
cfprApStatsCollectionPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmDn.setStatus("current")
_CfprApStatsCollectionPolicyFsmRn_Type = SnmpAdminString
_CfprApStatsCollectionPolicyFsmRn_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmRn = _CfprApStatsCollectionPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2, 1, 3),
    _CfprApStatsCollectionPolicyFsmRn_Type()
)
cfprApStatsCollectionPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmRn.setStatus("current")
_CfprApStatsCollectionPolicyFsmCompletionTime_Type = DateAndTime
_CfprApStatsCollectionPolicyFsmCompletionTime_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmCompletionTime = _CfprApStatsCollectionPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2, 1, 4),
    _CfprApStatsCollectionPolicyFsmCompletionTime_Type()
)
cfprApStatsCollectionPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmCompletionTime.setStatus("current")
_CfprApStatsCollectionPolicyFsmCurrentFsm_Type = CfprApStatsCollectionPolicyFsmCurrentFsm
_CfprApStatsCollectionPolicyFsmCurrentFsm_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmCurrentFsm = _CfprApStatsCollectionPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2, 1, 5),
    _CfprApStatsCollectionPolicyFsmCurrentFsm_Type()
)
cfprApStatsCollectionPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmCurrentFsm.setStatus("current")
_CfprApStatsCollectionPolicyFsmDescrData_Type = SnmpAdminString
_CfprApStatsCollectionPolicyFsmDescrData_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmDescrData = _CfprApStatsCollectionPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2, 1, 6),
    _CfprApStatsCollectionPolicyFsmDescrData_Type()
)
cfprApStatsCollectionPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmDescrData.setStatus("current")
_CfprApStatsCollectionPolicyFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApStatsCollectionPolicyFsmFsmStatus_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmFsmStatus = _CfprApStatsCollectionPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2, 1, 7),
    _CfprApStatsCollectionPolicyFsmFsmStatus_Type()
)
cfprApStatsCollectionPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmFsmStatus.setStatus("current")
_CfprApStatsCollectionPolicyFsmProgress_Type = Gauge32
_CfprApStatsCollectionPolicyFsmProgress_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmProgress = _CfprApStatsCollectionPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2, 1, 8),
    _CfprApStatsCollectionPolicyFsmProgress_Type()
)
cfprApStatsCollectionPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmProgress.setStatus("current")
_CfprApStatsCollectionPolicyFsmRmtErrCode_Type = Gauge32
_CfprApStatsCollectionPolicyFsmRmtErrCode_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmRmtErrCode = _CfprApStatsCollectionPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2, 1, 9),
    _CfprApStatsCollectionPolicyFsmRmtErrCode_Type()
)
cfprApStatsCollectionPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmRmtErrCode.setStatus("current")
_CfprApStatsCollectionPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprApStatsCollectionPolicyFsmRmtErrDescr_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmRmtErrDescr = _CfprApStatsCollectionPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2, 1, 10),
    _CfprApStatsCollectionPolicyFsmRmtErrDescr_Type()
)
cfprApStatsCollectionPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmRmtErrDescr.setStatus("current")
_CfprApStatsCollectionPolicyFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApStatsCollectionPolicyFsmRmtRslt_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmRmtRslt = _CfprApStatsCollectionPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 2, 1, 11),
    _CfprApStatsCollectionPolicyFsmRmtRslt_Type()
)
cfprApStatsCollectionPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmRmtRslt.setStatus("current")
_CfprApStatsCollectionPolicyFsmStageTable_Object = MibTable
cfprApStatsCollectionPolicyFsmStageTable = _CfprApStatsCollectionPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 3)
)
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStageTable.setStatus("current")
_CfprApStatsCollectionPolicyFsmStageEntry_Object = MibTableRow
cfprApStatsCollectionPolicyFsmStageEntry = _CfprApStatsCollectionPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 3, 1)
)
cfprApStatsCollectionPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsCollectionPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStageEntry.setStatus("current")
_CfprApStatsCollectionPolicyFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApStatsCollectionPolicyFsmStageInstanceId_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmStageInstanceId = _CfprApStatsCollectionPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 3, 1, 1),
    _CfprApStatsCollectionPolicyFsmStageInstanceId_Type()
)
cfprApStatsCollectionPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStageInstanceId.setStatus("current")
_CfprApStatsCollectionPolicyFsmStageDn_Type = CfprApManagedObjectDn
_CfprApStatsCollectionPolicyFsmStageDn_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmStageDn = _CfprApStatsCollectionPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 3, 1, 2),
    _CfprApStatsCollectionPolicyFsmStageDn_Type()
)
cfprApStatsCollectionPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStageDn.setStatus("current")
_CfprApStatsCollectionPolicyFsmStageRn_Type = SnmpAdminString
_CfprApStatsCollectionPolicyFsmStageRn_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmStageRn = _CfprApStatsCollectionPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 3, 1, 3),
    _CfprApStatsCollectionPolicyFsmStageRn_Type()
)
cfprApStatsCollectionPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStageRn.setStatus("current")
_CfprApStatsCollectionPolicyFsmStageDescrData_Type = SnmpAdminString
_CfprApStatsCollectionPolicyFsmStageDescrData_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmStageDescrData = _CfprApStatsCollectionPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 3, 1, 4),
    _CfprApStatsCollectionPolicyFsmStageDescrData_Type()
)
cfprApStatsCollectionPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStageDescrData.setStatus("current")
_CfprApStatsCollectionPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprApStatsCollectionPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmStageLastUpdateTime = _CfprApStatsCollectionPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 3, 1, 5),
    _CfprApStatsCollectionPolicyFsmStageLastUpdateTime_Type()
)
cfprApStatsCollectionPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStageLastUpdateTime.setStatus("current")
_CfprApStatsCollectionPolicyFsmStageName_Type = CfprApStatsCollectionPolicyFsmStageName
_CfprApStatsCollectionPolicyFsmStageName_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmStageName = _CfprApStatsCollectionPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 3, 1, 6),
    _CfprApStatsCollectionPolicyFsmStageName_Type()
)
cfprApStatsCollectionPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStageName.setStatus("current")
_CfprApStatsCollectionPolicyFsmStageOrder_Type = Gauge32
_CfprApStatsCollectionPolicyFsmStageOrder_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmStageOrder = _CfprApStatsCollectionPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 3, 1, 7),
    _CfprApStatsCollectionPolicyFsmStageOrder_Type()
)
cfprApStatsCollectionPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStageOrder.setStatus("current")
_CfprApStatsCollectionPolicyFsmStageRetry_Type = Gauge32
_CfprApStatsCollectionPolicyFsmStageRetry_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmStageRetry = _CfprApStatsCollectionPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 3, 1, 8),
    _CfprApStatsCollectionPolicyFsmStageRetry_Type()
)
cfprApStatsCollectionPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStageRetry.setStatus("current")
_CfprApStatsCollectionPolicyFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApStatsCollectionPolicyFsmStageStageStatus_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmStageStageStatus = _CfprApStatsCollectionPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 3, 1, 9),
    _CfprApStatsCollectionPolicyFsmStageStageStatus_Type()
)
cfprApStatsCollectionPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmStageStageStatus.setStatus("current")
_CfprApStatsCollectionPolicyFsmTaskTable_Object = MibTable
cfprApStatsCollectionPolicyFsmTaskTable = _CfprApStatsCollectionPolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 4)
)
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmTaskTable.setStatus("current")
_CfprApStatsCollectionPolicyFsmTaskEntry_Object = MibTableRow
cfprApStatsCollectionPolicyFsmTaskEntry = _CfprApStatsCollectionPolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 4, 1)
)
cfprApStatsCollectionPolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsCollectionPolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmTaskEntry.setStatus("current")
_CfprApStatsCollectionPolicyFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApStatsCollectionPolicyFsmTaskInstanceId_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmTaskInstanceId = _CfprApStatsCollectionPolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 4, 1, 1),
    _CfprApStatsCollectionPolicyFsmTaskInstanceId_Type()
)
cfprApStatsCollectionPolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmTaskInstanceId.setStatus("current")
_CfprApStatsCollectionPolicyFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApStatsCollectionPolicyFsmTaskDn_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmTaskDn = _CfprApStatsCollectionPolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 4, 1, 2),
    _CfprApStatsCollectionPolicyFsmTaskDn_Type()
)
cfprApStatsCollectionPolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmTaskDn.setStatus("current")
_CfprApStatsCollectionPolicyFsmTaskRn_Type = SnmpAdminString
_CfprApStatsCollectionPolicyFsmTaskRn_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmTaskRn = _CfprApStatsCollectionPolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 4, 1, 3),
    _CfprApStatsCollectionPolicyFsmTaskRn_Type()
)
cfprApStatsCollectionPolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmTaskRn.setStatus("current")
_CfprApStatsCollectionPolicyFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApStatsCollectionPolicyFsmTaskCompletion_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmTaskCompletion = _CfprApStatsCollectionPolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 4, 1, 4),
    _CfprApStatsCollectionPolicyFsmTaskCompletion_Type()
)
cfprApStatsCollectionPolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmTaskCompletion.setStatus("current")
_CfprApStatsCollectionPolicyFsmTaskFlags_Type = CfprApFsmFlags
_CfprApStatsCollectionPolicyFsmTaskFlags_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmTaskFlags = _CfprApStatsCollectionPolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 4, 1, 5),
    _CfprApStatsCollectionPolicyFsmTaskFlags_Type()
)
cfprApStatsCollectionPolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmTaskFlags.setStatus("current")
_CfprApStatsCollectionPolicyFsmTaskItem_Type = CfprApStatsCollectionPolicyFsmTaskItem
_CfprApStatsCollectionPolicyFsmTaskItem_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmTaskItem = _CfprApStatsCollectionPolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 4, 1, 6),
    _CfprApStatsCollectionPolicyFsmTaskItem_Type()
)
cfprApStatsCollectionPolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmTaskItem.setStatus("current")
_CfprApStatsCollectionPolicyFsmTaskSeqId_Type = Gauge32
_CfprApStatsCollectionPolicyFsmTaskSeqId_Object = MibTableColumn
cfprApStatsCollectionPolicyFsmTaskSeqId = _CfprApStatsCollectionPolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 4, 1, 7),
    _CfprApStatsCollectionPolicyFsmTaskSeqId_Type()
)
cfprApStatsCollectionPolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsCollectionPolicyFsmTaskSeqId.setStatus("current")
_CfprApStatsHolderTable_Object = MibTable
cfprApStatsHolderTable = _CfprApStatsHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 5)
)
if mibBuilder.loadTexts:
    cfprApStatsHolderTable.setStatus("current")
_CfprApStatsHolderEntry_Object = MibTableRow
cfprApStatsHolderEntry = _CfprApStatsHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 5, 1)
)
cfprApStatsHolderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsHolderEntry.setStatus("current")
_CfprApStatsHolderInstanceId_Type = CfprApManagedObjectId
_CfprApStatsHolderInstanceId_Object = MibTableColumn
cfprApStatsHolderInstanceId = _CfprApStatsHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 5, 1, 1),
    _CfprApStatsHolderInstanceId_Type()
)
cfprApStatsHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsHolderInstanceId.setStatus("current")
_CfprApStatsHolderDn_Type = CfprApManagedObjectDn
_CfprApStatsHolderDn_Object = MibTableColumn
cfprApStatsHolderDn = _CfprApStatsHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 5, 1, 2),
    _CfprApStatsHolderDn_Type()
)
cfprApStatsHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsHolderDn.setStatus("current")
_CfprApStatsHolderRn_Type = SnmpAdminString
_CfprApStatsHolderRn_Object = MibTableColumn
cfprApStatsHolderRn = _CfprApStatsHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 5, 1, 3),
    _CfprApStatsHolderRn_Type()
)
cfprApStatsHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsHolderRn.setStatus("current")
_CfprApStatsHolderName_Type = SnmpAdminString
_CfprApStatsHolderName_Object = MibTableColumn
cfprApStatsHolderName = _CfprApStatsHolderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 5, 1, 4),
    _CfprApStatsHolderName_Type()
)
cfprApStatsHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsHolderName.setStatus("current")
_CfprApStatsThr32DefinitionTable_Object = MibTable
cfprApStatsThr32DefinitionTable = _CfprApStatsThr32DefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6)
)
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionTable.setStatus("current")
_CfprApStatsThr32DefinitionEntry_Object = MibTableRow
cfprApStatsThr32DefinitionEntry = _CfprApStatsThr32DefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6, 1)
)
cfprApStatsThr32DefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsThr32DefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionEntry.setStatus("current")
_CfprApStatsThr32DefinitionInstanceId_Type = CfprApManagedObjectId
_CfprApStatsThr32DefinitionInstanceId_Object = MibTableColumn
cfprApStatsThr32DefinitionInstanceId = _CfprApStatsThr32DefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6, 1, 1),
    _CfprApStatsThr32DefinitionInstanceId_Type()
)
cfprApStatsThr32DefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionInstanceId.setStatus("current")
_CfprApStatsThr32DefinitionDn_Type = CfprApManagedObjectDn
_CfprApStatsThr32DefinitionDn_Object = MibTableColumn
cfprApStatsThr32DefinitionDn = _CfprApStatsThr32DefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6, 1, 2),
    _CfprApStatsThr32DefinitionDn_Type()
)
cfprApStatsThr32DefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionDn.setStatus("current")
_CfprApStatsThr32DefinitionRn_Type = SnmpAdminString
_CfprApStatsThr32DefinitionRn_Object = MibTableColumn
cfprApStatsThr32DefinitionRn = _CfprApStatsThr32DefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6, 1, 3),
    _CfprApStatsThr32DefinitionRn_Type()
)
cfprApStatsThr32DefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionRn.setStatus("current")
_CfprApStatsThr32DefinitionDescr_Type = SnmpAdminString
_CfprApStatsThr32DefinitionDescr_Object = MibTableColumn
cfprApStatsThr32DefinitionDescr = _CfprApStatsThr32DefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6, 1, 4),
    _CfprApStatsThr32DefinitionDescr_Type()
)
cfprApStatsThr32DefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionDescr.setStatus("current")
_CfprApStatsThr32DefinitionIntId_Type = SnmpAdminString
_CfprApStatsThr32DefinitionIntId_Object = MibTableColumn
cfprApStatsThr32DefinitionIntId = _CfprApStatsThr32DefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6, 1, 5),
    _CfprApStatsThr32DefinitionIntId_Type()
)
cfprApStatsThr32DefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionIntId.setStatus("current")
_CfprApStatsThr32DefinitionName_Type = SnmpAdminString
_CfprApStatsThr32DefinitionName_Object = MibTableColumn
cfprApStatsThr32DefinitionName = _CfprApStatsThr32DefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6, 1, 6),
    _CfprApStatsThr32DefinitionName_Type()
)
cfprApStatsThr32DefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionName.setStatus("current")
_CfprApStatsThr32DefinitionNormalValue_Type = Gauge32
_CfprApStatsThr32DefinitionNormalValue_Object = MibTableColumn
cfprApStatsThr32DefinitionNormalValue = _CfprApStatsThr32DefinitionNormalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6, 1, 7),
    _CfprApStatsThr32DefinitionNormalValue_Type()
)
cfprApStatsThr32DefinitionNormalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionNormalValue.setStatus("current")
_CfprApStatsThr32DefinitionPolicyLevel_Type = Gauge32
_CfprApStatsThr32DefinitionPolicyLevel_Object = MibTableColumn
cfprApStatsThr32DefinitionPolicyLevel = _CfprApStatsThr32DefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6, 1, 8),
    _CfprApStatsThr32DefinitionPolicyLevel_Type()
)
cfprApStatsThr32DefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionPolicyLevel.setStatus("current")
_CfprApStatsThr32DefinitionPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApStatsThr32DefinitionPolicyOwner_Object = MibTableColumn
cfprApStatsThr32DefinitionPolicyOwner = _CfprApStatsThr32DefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6, 1, 9),
    _CfprApStatsThr32DefinitionPolicyOwner_Type()
)
cfprApStatsThr32DefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionPolicyOwner.setStatus("current")
_CfprApStatsThr32DefinitionPropId_Type = SnmpAdminString
_CfprApStatsThr32DefinitionPropId_Object = MibTableColumn
cfprApStatsThr32DefinitionPropId = _CfprApStatsThr32DefinitionPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6, 1, 10),
    _CfprApStatsThr32DefinitionPropId_Type()
)
cfprApStatsThr32DefinitionPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionPropId.setStatus("current")
_CfprApStatsThr32DefinitionPropType_Type = CfprApStatsThr32DefinitionPropType
_CfprApStatsThr32DefinitionPropType_Object = MibTableColumn
cfprApStatsThr32DefinitionPropType = _CfprApStatsThr32DefinitionPropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 6, 1, 11),
    _CfprApStatsThr32DefinitionPropType_Type()
)
cfprApStatsThr32DefinitionPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32DefinitionPropType.setStatus("current")
_CfprApStatsThr32ValueTable_Object = MibTable
cfprApStatsThr32ValueTable = _CfprApStatsThr32ValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7)
)
if mibBuilder.loadTexts:
    cfprApStatsThr32ValueTable.setStatus("current")
_CfprApStatsThr32ValueEntry_Object = MibTableRow
cfprApStatsThr32ValueEntry = _CfprApStatsThr32ValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1)
)
cfprApStatsThr32ValueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsThr32ValueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsThr32ValueEntry.setStatus("current")
_CfprApStatsThr32ValueInstanceId_Type = CfprApManagedObjectId
_CfprApStatsThr32ValueInstanceId_Object = MibTableColumn
cfprApStatsThr32ValueInstanceId = _CfprApStatsThr32ValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 1),
    _CfprApStatsThr32ValueInstanceId_Type()
)
cfprApStatsThr32ValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValueInstanceId.setStatus("current")
_CfprApStatsThr32ValueDn_Type = CfprApManagedObjectDn
_CfprApStatsThr32ValueDn_Object = MibTableColumn
cfprApStatsThr32ValueDn = _CfprApStatsThr32ValueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 2),
    _CfprApStatsThr32ValueDn_Type()
)
cfprApStatsThr32ValueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValueDn.setStatus("current")
_CfprApStatsThr32ValueRn_Type = SnmpAdminString
_CfprApStatsThr32ValueRn_Object = MibTableColumn
cfprApStatsThr32ValueRn = _CfprApStatsThr32ValueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 3),
    _CfprApStatsThr32ValueRn_Type()
)
cfprApStatsThr32ValueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValueRn.setStatus("current")
_CfprApStatsThr32ValueDeescalating_Type = Gauge32
_CfprApStatsThr32ValueDeescalating_Object = MibTableColumn
cfprApStatsThr32ValueDeescalating = _CfprApStatsThr32ValueDeescalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 4),
    _CfprApStatsThr32ValueDeescalating_Type()
)
cfprApStatsThr32ValueDeescalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValueDeescalating.setStatus("current")
_CfprApStatsThr32ValueDescr_Type = SnmpAdminString
_CfprApStatsThr32ValueDescr_Object = MibTableColumn
cfprApStatsThr32ValueDescr = _CfprApStatsThr32ValueDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 5),
    _CfprApStatsThr32ValueDescr_Type()
)
cfprApStatsThr32ValueDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValueDescr.setStatus("current")
_CfprApStatsThr32ValueDirection_Type = CfprApStatsThresholdDirection
_CfprApStatsThr32ValueDirection_Object = MibTableColumn
cfprApStatsThr32ValueDirection = _CfprApStatsThr32ValueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 6),
    _CfprApStatsThr32ValueDirection_Type()
)
cfprApStatsThr32ValueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValueDirection.setStatus("current")
_CfprApStatsThr32ValueEscalating_Type = Gauge32
_CfprApStatsThr32ValueEscalating_Object = MibTableColumn
cfprApStatsThr32ValueEscalating = _CfprApStatsThr32ValueEscalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 7),
    _CfprApStatsThr32ValueEscalating_Type()
)
cfprApStatsThr32ValueEscalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValueEscalating.setStatus("current")
_CfprApStatsThr32ValueIntId_Type = SnmpAdminString
_CfprApStatsThr32ValueIntId_Object = MibTableColumn
cfprApStatsThr32ValueIntId = _CfprApStatsThr32ValueIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 8),
    _CfprApStatsThr32ValueIntId_Type()
)
cfprApStatsThr32ValueIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValueIntId.setStatus("current")
_CfprApStatsThr32ValueName_Type = SnmpAdminString
_CfprApStatsThr32ValueName_Object = MibTableColumn
cfprApStatsThr32ValueName = _CfprApStatsThr32ValueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 9),
    _CfprApStatsThr32ValueName_Type()
)
cfprApStatsThr32ValueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValueName.setStatus("current")
_CfprApStatsThr32ValuePolicyLevel_Type = Gauge32
_CfprApStatsThr32ValuePolicyLevel_Object = MibTableColumn
cfprApStatsThr32ValuePolicyLevel = _CfprApStatsThr32ValuePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 10),
    _CfprApStatsThr32ValuePolicyLevel_Type()
)
cfprApStatsThr32ValuePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValuePolicyLevel.setStatus("current")
_CfprApStatsThr32ValuePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApStatsThr32ValuePolicyOwner_Object = MibTableColumn
cfprApStatsThr32ValuePolicyOwner = _CfprApStatsThr32ValuePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 11),
    _CfprApStatsThr32ValuePolicyOwner_Type()
)
cfprApStatsThr32ValuePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValuePolicyOwner.setStatus("current")
_CfprApStatsThr32ValuePropType_Type = CfprApStatsThr32ValuePropType
_CfprApStatsThr32ValuePropType_Object = MibTableColumn
cfprApStatsThr32ValuePropType = _CfprApStatsThr32ValuePropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 12),
    _CfprApStatsThr32ValuePropType_Type()
)
cfprApStatsThr32ValuePropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValuePropType.setStatus("current")
_CfprApStatsThr32ValueSeverity_Type = CfprApConditionSeverity
_CfprApStatsThr32ValueSeverity_Object = MibTableColumn
cfprApStatsThr32ValueSeverity = _CfprApStatsThr32ValueSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 7, 1, 13),
    _CfprApStatsThr32ValueSeverity_Type()
)
cfprApStatsThr32ValueSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr32ValueSeverity.setStatus("current")
_CfprApStatsThr64DefinitionTable_Object = MibTable
cfprApStatsThr64DefinitionTable = _CfprApStatsThr64DefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8)
)
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionTable.setStatus("current")
_CfprApStatsThr64DefinitionEntry_Object = MibTableRow
cfprApStatsThr64DefinitionEntry = _CfprApStatsThr64DefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8, 1)
)
cfprApStatsThr64DefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsThr64DefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionEntry.setStatus("current")
_CfprApStatsThr64DefinitionInstanceId_Type = CfprApManagedObjectId
_CfprApStatsThr64DefinitionInstanceId_Object = MibTableColumn
cfprApStatsThr64DefinitionInstanceId = _CfprApStatsThr64DefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8, 1, 1),
    _CfprApStatsThr64DefinitionInstanceId_Type()
)
cfprApStatsThr64DefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionInstanceId.setStatus("current")
_CfprApStatsThr64DefinitionDn_Type = CfprApManagedObjectDn
_CfprApStatsThr64DefinitionDn_Object = MibTableColumn
cfprApStatsThr64DefinitionDn = _CfprApStatsThr64DefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8, 1, 2),
    _CfprApStatsThr64DefinitionDn_Type()
)
cfprApStatsThr64DefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionDn.setStatus("current")
_CfprApStatsThr64DefinitionRn_Type = SnmpAdminString
_CfprApStatsThr64DefinitionRn_Object = MibTableColumn
cfprApStatsThr64DefinitionRn = _CfprApStatsThr64DefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8, 1, 3),
    _CfprApStatsThr64DefinitionRn_Type()
)
cfprApStatsThr64DefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionRn.setStatus("current")
_CfprApStatsThr64DefinitionDescr_Type = SnmpAdminString
_CfprApStatsThr64DefinitionDescr_Object = MibTableColumn
cfprApStatsThr64DefinitionDescr = _CfprApStatsThr64DefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8, 1, 4),
    _CfprApStatsThr64DefinitionDescr_Type()
)
cfprApStatsThr64DefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionDescr.setStatus("current")
_CfprApStatsThr64DefinitionIntId_Type = SnmpAdminString
_CfprApStatsThr64DefinitionIntId_Object = MibTableColumn
cfprApStatsThr64DefinitionIntId = _CfprApStatsThr64DefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8, 1, 5),
    _CfprApStatsThr64DefinitionIntId_Type()
)
cfprApStatsThr64DefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionIntId.setStatus("current")
_CfprApStatsThr64DefinitionName_Type = SnmpAdminString
_CfprApStatsThr64DefinitionName_Object = MibTableColumn
cfprApStatsThr64DefinitionName = _CfprApStatsThr64DefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8, 1, 6),
    _CfprApStatsThr64DefinitionName_Type()
)
cfprApStatsThr64DefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionName.setStatus("current")
_CfprApStatsThr64DefinitionNormalValue_Type = Unsigned64
_CfprApStatsThr64DefinitionNormalValue_Object = MibTableColumn
cfprApStatsThr64DefinitionNormalValue = _CfprApStatsThr64DefinitionNormalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8, 1, 7),
    _CfprApStatsThr64DefinitionNormalValue_Type()
)
cfprApStatsThr64DefinitionNormalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionNormalValue.setStatus("current")
_CfprApStatsThr64DefinitionPolicyLevel_Type = Gauge32
_CfprApStatsThr64DefinitionPolicyLevel_Object = MibTableColumn
cfprApStatsThr64DefinitionPolicyLevel = _CfprApStatsThr64DefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8, 1, 8),
    _CfprApStatsThr64DefinitionPolicyLevel_Type()
)
cfprApStatsThr64DefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionPolicyLevel.setStatus("current")
_CfprApStatsThr64DefinitionPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApStatsThr64DefinitionPolicyOwner_Object = MibTableColumn
cfprApStatsThr64DefinitionPolicyOwner = _CfprApStatsThr64DefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8, 1, 9),
    _CfprApStatsThr64DefinitionPolicyOwner_Type()
)
cfprApStatsThr64DefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionPolicyOwner.setStatus("current")
_CfprApStatsThr64DefinitionPropId_Type = SnmpAdminString
_CfprApStatsThr64DefinitionPropId_Object = MibTableColumn
cfprApStatsThr64DefinitionPropId = _CfprApStatsThr64DefinitionPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8, 1, 10),
    _CfprApStatsThr64DefinitionPropId_Type()
)
cfprApStatsThr64DefinitionPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionPropId.setStatus("current")
_CfprApStatsThr64DefinitionPropType_Type = CfprApStatsThr64DefinitionPropType
_CfprApStatsThr64DefinitionPropType_Object = MibTableColumn
cfprApStatsThr64DefinitionPropType = _CfprApStatsThr64DefinitionPropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 8, 1, 11),
    _CfprApStatsThr64DefinitionPropType_Type()
)
cfprApStatsThr64DefinitionPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64DefinitionPropType.setStatus("current")
_CfprApStatsThr64ValueTable_Object = MibTable
cfprApStatsThr64ValueTable = _CfprApStatsThr64ValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9)
)
if mibBuilder.loadTexts:
    cfprApStatsThr64ValueTable.setStatus("current")
_CfprApStatsThr64ValueEntry_Object = MibTableRow
cfprApStatsThr64ValueEntry = _CfprApStatsThr64ValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1)
)
cfprApStatsThr64ValueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsThr64ValueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsThr64ValueEntry.setStatus("current")
_CfprApStatsThr64ValueInstanceId_Type = CfprApManagedObjectId
_CfprApStatsThr64ValueInstanceId_Object = MibTableColumn
cfprApStatsThr64ValueInstanceId = _CfprApStatsThr64ValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 1),
    _CfprApStatsThr64ValueInstanceId_Type()
)
cfprApStatsThr64ValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValueInstanceId.setStatus("current")
_CfprApStatsThr64ValueDn_Type = CfprApManagedObjectDn
_CfprApStatsThr64ValueDn_Object = MibTableColumn
cfprApStatsThr64ValueDn = _CfprApStatsThr64ValueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 2),
    _CfprApStatsThr64ValueDn_Type()
)
cfprApStatsThr64ValueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValueDn.setStatus("current")
_CfprApStatsThr64ValueRn_Type = SnmpAdminString
_CfprApStatsThr64ValueRn_Object = MibTableColumn
cfprApStatsThr64ValueRn = _CfprApStatsThr64ValueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 3),
    _CfprApStatsThr64ValueRn_Type()
)
cfprApStatsThr64ValueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValueRn.setStatus("current")
_CfprApStatsThr64ValueDeescalating_Type = Unsigned64
_CfprApStatsThr64ValueDeescalating_Object = MibTableColumn
cfprApStatsThr64ValueDeescalating = _CfprApStatsThr64ValueDeescalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 4),
    _CfprApStatsThr64ValueDeescalating_Type()
)
cfprApStatsThr64ValueDeescalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValueDeescalating.setStatus("current")
_CfprApStatsThr64ValueDescr_Type = SnmpAdminString
_CfprApStatsThr64ValueDescr_Object = MibTableColumn
cfprApStatsThr64ValueDescr = _CfprApStatsThr64ValueDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 5),
    _CfprApStatsThr64ValueDescr_Type()
)
cfprApStatsThr64ValueDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValueDescr.setStatus("current")
_CfprApStatsThr64ValueDirection_Type = CfprApStatsThresholdDirection
_CfprApStatsThr64ValueDirection_Object = MibTableColumn
cfprApStatsThr64ValueDirection = _CfprApStatsThr64ValueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 6),
    _CfprApStatsThr64ValueDirection_Type()
)
cfprApStatsThr64ValueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValueDirection.setStatus("current")
_CfprApStatsThr64ValueEscalating_Type = Unsigned64
_CfprApStatsThr64ValueEscalating_Object = MibTableColumn
cfprApStatsThr64ValueEscalating = _CfprApStatsThr64ValueEscalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 7),
    _CfprApStatsThr64ValueEscalating_Type()
)
cfprApStatsThr64ValueEscalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValueEscalating.setStatus("current")
_CfprApStatsThr64ValueIntId_Type = SnmpAdminString
_CfprApStatsThr64ValueIntId_Object = MibTableColumn
cfprApStatsThr64ValueIntId = _CfprApStatsThr64ValueIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 8),
    _CfprApStatsThr64ValueIntId_Type()
)
cfprApStatsThr64ValueIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValueIntId.setStatus("current")
_CfprApStatsThr64ValueName_Type = SnmpAdminString
_CfprApStatsThr64ValueName_Object = MibTableColumn
cfprApStatsThr64ValueName = _CfprApStatsThr64ValueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 9),
    _CfprApStatsThr64ValueName_Type()
)
cfprApStatsThr64ValueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValueName.setStatus("current")
_CfprApStatsThr64ValuePolicyLevel_Type = Gauge32
_CfprApStatsThr64ValuePolicyLevel_Object = MibTableColumn
cfprApStatsThr64ValuePolicyLevel = _CfprApStatsThr64ValuePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 10),
    _CfprApStatsThr64ValuePolicyLevel_Type()
)
cfprApStatsThr64ValuePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValuePolicyLevel.setStatus("current")
_CfprApStatsThr64ValuePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApStatsThr64ValuePolicyOwner_Object = MibTableColumn
cfprApStatsThr64ValuePolicyOwner = _CfprApStatsThr64ValuePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 11),
    _CfprApStatsThr64ValuePolicyOwner_Type()
)
cfprApStatsThr64ValuePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValuePolicyOwner.setStatus("current")
_CfprApStatsThr64ValuePropType_Type = CfprApStatsThr64ValuePropType
_CfprApStatsThr64ValuePropType_Object = MibTableColumn
cfprApStatsThr64ValuePropType = _CfprApStatsThr64ValuePropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 12),
    _CfprApStatsThr64ValuePropType_Type()
)
cfprApStatsThr64ValuePropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValuePropType.setStatus("current")
_CfprApStatsThr64ValueSeverity_Type = CfprApConditionSeverity
_CfprApStatsThr64ValueSeverity_Object = MibTableColumn
cfprApStatsThr64ValueSeverity = _CfprApStatsThr64ValueSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 9, 1, 13),
    _CfprApStatsThr64ValueSeverity_Type()
)
cfprApStatsThr64ValueSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThr64ValueSeverity.setStatus("current")
_CfprApStatsThrFloatDefinitionTable_Object = MibTable
cfprApStatsThrFloatDefinitionTable = _CfprApStatsThrFloatDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10)
)
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionTable.setStatus("current")
_CfprApStatsThrFloatDefinitionEntry_Object = MibTableRow
cfprApStatsThrFloatDefinitionEntry = _CfprApStatsThrFloatDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10, 1)
)
cfprApStatsThrFloatDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsThrFloatDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionEntry.setStatus("current")
_CfprApStatsThrFloatDefinitionInstanceId_Type = CfprApManagedObjectId
_CfprApStatsThrFloatDefinitionInstanceId_Object = MibTableColumn
cfprApStatsThrFloatDefinitionInstanceId = _CfprApStatsThrFloatDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10, 1, 1),
    _CfprApStatsThrFloatDefinitionInstanceId_Type()
)
cfprApStatsThrFloatDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionInstanceId.setStatus("current")
_CfprApStatsThrFloatDefinitionDn_Type = CfprApManagedObjectDn
_CfprApStatsThrFloatDefinitionDn_Object = MibTableColumn
cfprApStatsThrFloatDefinitionDn = _CfprApStatsThrFloatDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10, 1, 2),
    _CfprApStatsThrFloatDefinitionDn_Type()
)
cfprApStatsThrFloatDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionDn.setStatus("current")
_CfprApStatsThrFloatDefinitionRn_Type = SnmpAdminString
_CfprApStatsThrFloatDefinitionRn_Object = MibTableColumn
cfprApStatsThrFloatDefinitionRn = _CfprApStatsThrFloatDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10, 1, 3),
    _CfprApStatsThrFloatDefinitionRn_Type()
)
cfprApStatsThrFloatDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionRn.setStatus("current")
_CfprApStatsThrFloatDefinitionDescr_Type = SnmpAdminString
_CfprApStatsThrFloatDefinitionDescr_Object = MibTableColumn
cfprApStatsThrFloatDefinitionDescr = _CfprApStatsThrFloatDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10, 1, 4),
    _CfprApStatsThrFloatDefinitionDescr_Type()
)
cfprApStatsThrFloatDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionDescr.setStatus("current")
_CfprApStatsThrFloatDefinitionIntId_Type = SnmpAdminString
_CfprApStatsThrFloatDefinitionIntId_Object = MibTableColumn
cfprApStatsThrFloatDefinitionIntId = _CfprApStatsThrFloatDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10, 1, 5),
    _CfprApStatsThrFloatDefinitionIntId_Type()
)
cfprApStatsThrFloatDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionIntId.setStatus("current")
_CfprApStatsThrFloatDefinitionName_Type = SnmpAdminString
_CfprApStatsThrFloatDefinitionName_Object = MibTableColumn
cfprApStatsThrFloatDefinitionName = _CfprApStatsThrFloatDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10, 1, 6),
    _CfprApStatsThrFloatDefinitionName_Type()
)
cfprApStatsThrFloatDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionName.setStatus("current")
_CfprApStatsThrFloatDefinitionNormalValue_Type = Integer32
_CfprApStatsThrFloatDefinitionNormalValue_Object = MibTableColumn
cfprApStatsThrFloatDefinitionNormalValue = _CfprApStatsThrFloatDefinitionNormalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10, 1, 7),
    _CfprApStatsThrFloatDefinitionNormalValue_Type()
)
cfprApStatsThrFloatDefinitionNormalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionNormalValue.setStatus("current")
_CfprApStatsThrFloatDefinitionPolicyLevel_Type = Gauge32
_CfprApStatsThrFloatDefinitionPolicyLevel_Object = MibTableColumn
cfprApStatsThrFloatDefinitionPolicyLevel = _CfprApStatsThrFloatDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10, 1, 8),
    _CfprApStatsThrFloatDefinitionPolicyLevel_Type()
)
cfprApStatsThrFloatDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionPolicyLevel.setStatus("current")
_CfprApStatsThrFloatDefinitionPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApStatsThrFloatDefinitionPolicyOwner_Object = MibTableColumn
cfprApStatsThrFloatDefinitionPolicyOwner = _CfprApStatsThrFloatDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10, 1, 9),
    _CfprApStatsThrFloatDefinitionPolicyOwner_Type()
)
cfprApStatsThrFloatDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionPolicyOwner.setStatus("current")
_CfprApStatsThrFloatDefinitionPropId_Type = SnmpAdminString
_CfprApStatsThrFloatDefinitionPropId_Object = MibTableColumn
cfprApStatsThrFloatDefinitionPropId = _CfprApStatsThrFloatDefinitionPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10, 1, 10),
    _CfprApStatsThrFloatDefinitionPropId_Type()
)
cfprApStatsThrFloatDefinitionPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionPropId.setStatus("current")
_CfprApStatsThrFloatDefinitionPropType_Type = CfprApStatsThrFloatDefinitionPropType
_CfprApStatsThrFloatDefinitionPropType_Object = MibTableColumn
cfprApStatsThrFloatDefinitionPropType = _CfprApStatsThrFloatDefinitionPropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 10, 1, 11),
    _CfprApStatsThrFloatDefinitionPropType_Type()
)
cfprApStatsThrFloatDefinitionPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatDefinitionPropType.setStatus("current")
_CfprApStatsThrFloatValueTable_Object = MibTable
cfprApStatsThrFloatValueTable = _CfprApStatsThrFloatValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11)
)
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValueTable.setStatus("current")
_CfprApStatsThrFloatValueEntry_Object = MibTableRow
cfprApStatsThrFloatValueEntry = _CfprApStatsThrFloatValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1)
)
cfprApStatsThrFloatValueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsThrFloatValueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValueEntry.setStatus("current")
_CfprApStatsThrFloatValueInstanceId_Type = CfprApManagedObjectId
_CfprApStatsThrFloatValueInstanceId_Object = MibTableColumn
cfprApStatsThrFloatValueInstanceId = _CfprApStatsThrFloatValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 1),
    _CfprApStatsThrFloatValueInstanceId_Type()
)
cfprApStatsThrFloatValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValueInstanceId.setStatus("current")
_CfprApStatsThrFloatValueDn_Type = CfprApManagedObjectDn
_CfprApStatsThrFloatValueDn_Object = MibTableColumn
cfprApStatsThrFloatValueDn = _CfprApStatsThrFloatValueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 2),
    _CfprApStatsThrFloatValueDn_Type()
)
cfprApStatsThrFloatValueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValueDn.setStatus("current")
_CfprApStatsThrFloatValueRn_Type = SnmpAdminString
_CfprApStatsThrFloatValueRn_Object = MibTableColumn
cfprApStatsThrFloatValueRn = _CfprApStatsThrFloatValueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 3),
    _CfprApStatsThrFloatValueRn_Type()
)
cfprApStatsThrFloatValueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValueRn.setStatus("current")
_CfprApStatsThrFloatValueDeescalating_Type = Integer32
_CfprApStatsThrFloatValueDeescalating_Object = MibTableColumn
cfprApStatsThrFloatValueDeescalating = _CfprApStatsThrFloatValueDeescalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 4),
    _CfprApStatsThrFloatValueDeescalating_Type()
)
cfprApStatsThrFloatValueDeescalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValueDeescalating.setStatus("current")
_CfprApStatsThrFloatValueDescr_Type = SnmpAdminString
_CfprApStatsThrFloatValueDescr_Object = MibTableColumn
cfprApStatsThrFloatValueDescr = _CfprApStatsThrFloatValueDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 5),
    _CfprApStatsThrFloatValueDescr_Type()
)
cfprApStatsThrFloatValueDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValueDescr.setStatus("current")
_CfprApStatsThrFloatValueDirection_Type = CfprApStatsThresholdDirection
_CfprApStatsThrFloatValueDirection_Object = MibTableColumn
cfprApStatsThrFloatValueDirection = _CfprApStatsThrFloatValueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 6),
    _CfprApStatsThrFloatValueDirection_Type()
)
cfprApStatsThrFloatValueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValueDirection.setStatus("current")
_CfprApStatsThrFloatValueEscalating_Type = Integer32
_CfprApStatsThrFloatValueEscalating_Object = MibTableColumn
cfprApStatsThrFloatValueEscalating = _CfprApStatsThrFloatValueEscalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 7),
    _CfprApStatsThrFloatValueEscalating_Type()
)
cfprApStatsThrFloatValueEscalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValueEscalating.setStatus("current")
_CfprApStatsThrFloatValueIntId_Type = SnmpAdminString
_CfprApStatsThrFloatValueIntId_Object = MibTableColumn
cfprApStatsThrFloatValueIntId = _CfprApStatsThrFloatValueIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 8),
    _CfprApStatsThrFloatValueIntId_Type()
)
cfprApStatsThrFloatValueIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValueIntId.setStatus("current")
_CfprApStatsThrFloatValueName_Type = SnmpAdminString
_CfprApStatsThrFloatValueName_Object = MibTableColumn
cfprApStatsThrFloatValueName = _CfprApStatsThrFloatValueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 9),
    _CfprApStatsThrFloatValueName_Type()
)
cfprApStatsThrFloatValueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValueName.setStatus("current")
_CfprApStatsThrFloatValuePolicyLevel_Type = Gauge32
_CfprApStatsThrFloatValuePolicyLevel_Object = MibTableColumn
cfprApStatsThrFloatValuePolicyLevel = _CfprApStatsThrFloatValuePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 10),
    _CfprApStatsThrFloatValuePolicyLevel_Type()
)
cfprApStatsThrFloatValuePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValuePolicyLevel.setStatus("current")
_CfprApStatsThrFloatValuePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApStatsThrFloatValuePolicyOwner_Object = MibTableColumn
cfprApStatsThrFloatValuePolicyOwner = _CfprApStatsThrFloatValuePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 11),
    _CfprApStatsThrFloatValuePolicyOwner_Type()
)
cfprApStatsThrFloatValuePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValuePolicyOwner.setStatus("current")
_CfprApStatsThrFloatValuePropType_Type = CfprApStatsThrFloatValuePropType
_CfprApStatsThrFloatValuePropType_Object = MibTableColumn
cfprApStatsThrFloatValuePropType = _CfprApStatsThrFloatValuePropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 12),
    _CfprApStatsThrFloatValuePropType_Type()
)
cfprApStatsThrFloatValuePropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValuePropType.setStatus("current")
_CfprApStatsThrFloatValueSeverity_Type = CfprApConditionSeverity
_CfprApStatsThrFloatValueSeverity_Object = MibTableColumn
cfprApStatsThrFloatValueSeverity = _CfprApStatsThrFloatValueSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 11, 1, 13),
    _CfprApStatsThrFloatValueSeverity_Type()
)
cfprApStatsThrFloatValueSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThrFloatValueSeverity.setStatus("current")
_CfprApStatsThresholdClassTable_Object = MibTable
cfprApStatsThresholdClassTable = _CfprApStatsThresholdClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 12)
)
if mibBuilder.loadTexts:
    cfprApStatsThresholdClassTable.setStatus("current")
_CfprApStatsThresholdClassEntry_Object = MibTableRow
cfprApStatsThresholdClassEntry = _CfprApStatsThresholdClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 12, 1)
)
cfprApStatsThresholdClassEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsThresholdClassInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsThresholdClassEntry.setStatus("current")
_CfprApStatsThresholdClassInstanceId_Type = CfprApManagedObjectId
_CfprApStatsThresholdClassInstanceId_Object = MibTableColumn
cfprApStatsThresholdClassInstanceId = _CfprApStatsThresholdClassInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 12, 1, 1),
    _CfprApStatsThresholdClassInstanceId_Type()
)
cfprApStatsThresholdClassInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsThresholdClassInstanceId.setStatus("current")
_CfprApStatsThresholdClassDn_Type = CfprApManagedObjectDn
_CfprApStatsThresholdClassDn_Object = MibTableColumn
cfprApStatsThresholdClassDn = _CfprApStatsThresholdClassDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 12, 1, 2),
    _CfprApStatsThresholdClassDn_Type()
)
cfprApStatsThresholdClassDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdClassDn.setStatus("current")
_CfprApStatsThresholdClassRn_Type = SnmpAdminString
_CfprApStatsThresholdClassRn_Object = MibTableColumn
cfprApStatsThresholdClassRn = _CfprApStatsThresholdClassRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 12, 1, 3),
    _CfprApStatsThresholdClassRn_Type()
)
cfprApStatsThresholdClassRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdClassRn.setStatus("current")
_CfprApStatsThresholdClassDescr_Type = SnmpAdminString
_CfprApStatsThresholdClassDescr_Object = MibTableColumn
cfprApStatsThresholdClassDescr = _CfprApStatsThresholdClassDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 12, 1, 4),
    _CfprApStatsThresholdClassDescr_Type()
)
cfprApStatsThresholdClassDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdClassDescr.setStatus("current")
_CfprApStatsThresholdClassIntId_Type = SnmpAdminString
_CfprApStatsThresholdClassIntId_Object = MibTableColumn
cfprApStatsThresholdClassIntId = _CfprApStatsThresholdClassIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 12, 1, 5),
    _CfprApStatsThresholdClassIntId_Type()
)
cfprApStatsThresholdClassIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdClassIntId.setStatus("current")
_CfprApStatsThresholdClassName_Type = SnmpAdminString
_CfprApStatsThresholdClassName_Object = MibTableColumn
cfprApStatsThresholdClassName = _CfprApStatsThresholdClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 12, 1, 6),
    _CfprApStatsThresholdClassName_Type()
)
cfprApStatsThresholdClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdClassName.setStatus("current")
_CfprApStatsThresholdClassPolicyLevel_Type = Gauge32
_CfprApStatsThresholdClassPolicyLevel_Object = MibTableColumn
cfprApStatsThresholdClassPolicyLevel = _CfprApStatsThresholdClassPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 12, 1, 7),
    _CfprApStatsThresholdClassPolicyLevel_Type()
)
cfprApStatsThresholdClassPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdClassPolicyLevel.setStatus("current")
_CfprApStatsThresholdClassPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApStatsThresholdClassPolicyOwner_Object = MibTableColumn
cfprApStatsThresholdClassPolicyOwner = _CfprApStatsThresholdClassPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 12, 1, 8),
    _CfprApStatsThresholdClassPolicyOwner_Type()
)
cfprApStatsThresholdClassPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdClassPolicyOwner.setStatus("current")
_CfprApStatsThresholdClassStatsClassId_Type = SnmpAdminString
_CfprApStatsThresholdClassStatsClassId_Object = MibTableColumn
cfprApStatsThresholdClassStatsClassId = _CfprApStatsThresholdClassStatsClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 12, 1, 9),
    _CfprApStatsThresholdClassStatsClassId_Type()
)
cfprApStatsThresholdClassStatsClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdClassStatsClassId.setStatus("current")
_CfprApStatsThresholdPolicyTable_Object = MibTable
cfprApStatsThresholdPolicyTable = _CfprApStatsThresholdPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 13)
)
if mibBuilder.loadTexts:
    cfprApStatsThresholdPolicyTable.setStatus("current")
_CfprApStatsThresholdPolicyEntry_Object = MibTableRow
cfprApStatsThresholdPolicyEntry = _CfprApStatsThresholdPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 13, 1)
)
cfprApStatsThresholdPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-STATS-MIB", "cfprApStatsThresholdPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApStatsThresholdPolicyEntry.setStatus("current")
_CfprApStatsThresholdPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApStatsThresholdPolicyInstanceId_Object = MibTableColumn
cfprApStatsThresholdPolicyInstanceId = _CfprApStatsThresholdPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 13, 1, 1),
    _CfprApStatsThresholdPolicyInstanceId_Type()
)
cfprApStatsThresholdPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApStatsThresholdPolicyInstanceId.setStatus("current")
_CfprApStatsThresholdPolicyDn_Type = CfprApManagedObjectDn
_CfprApStatsThresholdPolicyDn_Object = MibTableColumn
cfprApStatsThresholdPolicyDn = _CfprApStatsThresholdPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 13, 1, 2),
    _CfprApStatsThresholdPolicyDn_Type()
)
cfprApStatsThresholdPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdPolicyDn.setStatus("current")
_CfprApStatsThresholdPolicyRn_Type = SnmpAdminString
_CfprApStatsThresholdPolicyRn_Object = MibTableColumn
cfprApStatsThresholdPolicyRn = _CfprApStatsThresholdPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 13, 1, 3),
    _CfprApStatsThresholdPolicyRn_Type()
)
cfprApStatsThresholdPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdPolicyRn.setStatus("current")
_CfprApStatsThresholdPolicyDescr_Type = SnmpAdminString
_CfprApStatsThresholdPolicyDescr_Object = MibTableColumn
cfprApStatsThresholdPolicyDescr = _CfprApStatsThresholdPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 13, 1, 4),
    _CfprApStatsThresholdPolicyDescr_Type()
)
cfprApStatsThresholdPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdPolicyDescr.setStatus("current")
_CfprApStatsThresholdPolicyIntId_Type = SnmpAdminString
_CfprApStatsThresholdPolicyIntId_Object = MibTableColumn
cfprApStatsThresholdPolicyIntId = _CfprApStatsThresholdPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 13, 1, 5),
    _CfprApStatsThresholdPolicyIntId_Type()
)
cfprApStatsThresholdPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdPolicyIntId.setStatus("current")
_CfprApStatsThresholdPolicyName_Type = SnmpAdminString
_CfprApStatsThresholdPolicyName_Object = MibTableColumn
cfprApStatsThresholdPolicyName = _CfprApStatsThresholdPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 13, 1, 6),
    _CfprApStatsThresholdPolicyName_Type()
)
cfprApStatsThresholdPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdPolicyName.setStatus("current")
_CfprApStatsThresholdPolicyPolicyLevel_Type = Gauge32
_CfprApStatsThresholdPolicyPolicyLevel_Object = MibTableColumn
cfprApStatsThresholdPolicyPolicyLevel = _CfprApStatsThresholdPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 13, 1, 7),
    _CfprApStatsThresholdPolicyPolicyLevel_Type()
)
cfprApStatsThresholdPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdPolicyPolicyLevel.setStatus("current")
_CfprApStatsThresholdPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApStatsThresholdPolicyPolicyOwner_Object = MibTableColumn
cfprApStatsThresholdPolicyPolicyOwner = _CfprApStatsThresholdPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 73, 13, 1, 8),
    _CfprApStatsThresholdPolicyPolicyOwner_Type()
)
cfprApStatsThresholdPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApStatsThresholdPolicyPolicyOwner.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-STATS-MIB",
    **{"cfprApStatsObjects": cfprApStatsObjects,
       "cfprApStatsCollectionPolicyTable": cfprApStatsCollectionPolicyTable,
       "cfprApStatsCollectionPolicyEntry": cfprApStatsCollectionPolicyEntry,
       "cfprApStatsCollectionPolicyInstanceId": cfprApStatsCollectionPolicyInstanceId,
       "cfprApStatsCollectionPolicyDn": cfprApStatsCollectionPolicyDn,
       "cfprApStatsCollectionPolicyRn": cfprApStatsCollectionPolicyRn,
       "cfprApStatsCollectionPolicyCollectionInterval": cfprApStatsCollectionPolicyCollectionInterval,
       "cfprApStatsCollectionPolicyFsmDescr": cfprApStatsCollectionPolicyFsmDescr,
       "cfprApStatsCollectionPolicyFsmPrev": cfprApStatsCollectionPolicyFsmPrev,
       "cfprApStatsCollectionPolicyFsmProgr": cfprApStatsCollectionPolicyFsmProgr,
       "cfprApStatsCollectionPolicyFsmRmtInvErrCode": cfprApStatsCollectionPolicyFsmRmtInvErrCode,
       "cfprApStatsCollectionPolicyFsmRmtInvErrDescr": cfprApStatsCollectionPolicyFsmRmtInvErrDescr,
       "cfprApStatsCollectionPolicyFsmRmtInvRslt": cfprApStatsCollectionPolicyFsmRmtInvRslt,
       "cfprApStatsCollectionPolicyFsmStageDescr": cfprApStatsCollectionPolicyFsmStageDescr,
       "cfprApStatsCollectionPolicyFsmStamp": cfprApStatsCollectionPolicyFsmStamp,
       "cfprApStatsCollectionPolicyFsmStatus": cfprApStatsCollectionPolicyFsmStatus,
       "cfprApStatsCollectionPolicyFsmTry": cfprApStatsCollectionPolicyFsmTry,
       "cfprApStatsCollectionPolicyId": cfprApStatsCollectionPolicyId,
       "cfprApStatsCollectionPolicyName": cfprApStatsCollectionPolicyName,
       "cfprApStatsCollectionPolicyReportingInterval": cfprApStatsCollectionPolicyReportingInterval,
       "cfprApStatsCollectionPolicyFsmTable": cfprApStatsCollectionPolicyFsmTable,
       "cfprApStatsCollectionPolicyFsmEntry": cfprApStatsCollectionPolicyFsmEntry,
       "cfprApStatsCollectionPolicyFsmInstanceId": cfprApStatsCollectionPolicyFsmInstanceId,
       "cfprApStatsCollectionPolicyFsmDn": cfprApStatsCollectionPolicyFsmDn,
       "cfprApStatsCollectionPolicyFsmRn": cfprApStatsCollectionPolicyFsmRn,
       "cfprApStatsCollectionPolicyFsmCompletionTime": cfprApStatsCollectionPolicyFsmCompletionTime,
       "cfprApStatsCollectionPolicyFsmCurrentFsm": cfprApStatsCollectionPolicyFsmCurrentFsm,
       "cfprApStatsCollectionPolicyFsmDescrData": cfprApStatsCollectionPolicyFsmDescrData,
       "cfprApStatsCollectionPolicyFsmFsmStatus": cfprApStatsCollectionPolicyFsmFsmStatus,
       "cfprApStatsCollectionPolicyFsmProgress": cfprApStatsCollectionPolicyFsmProgress,
       "cfprApStatsCollectionPolicyFsmRmtErrCode": cfprApStatsCollectionPolicyFsmRmtErrCode,
       "cfprApStatsCollectionPolicyFsmRmtErrDescr": cfprApStatsCollectionPolicyFsmRmtErrDescr,
       "cfprApStatsCollectionPolicyFsmRmtRslt": cfprApStatsCollectionPolicyFsmRmtRslt,
       "cfprApStatsCollectionPolicyFsmStageTable": cfprApStatsCollectionPolicyFsmStageTable,
       "cfprApStatsCollectionPolicyFsmStageEntry": cfprApStatsCollectionPolicyFsmStageEntry,
       "cfprApStatsCollectionPolicyFsmStageInstanceId": cfprApStatsCollectionPolicyFsmStageInstanceId,
       "cfprApStatsCollectionPolicyFsmStageDn": cfprApStatsCollectionPolicyFsmStageDn,
       "cfprApStatsCollectionPolicyFsmStageRn": cfprApStatsCollectionPolicyFsmStageRn,
       "cfprApStatsCollectionPolicyFsmStageDescrData": cfprApStatsCollectionPolicyFsmStageDescrData,
       "cfprApStatsCollectionPolicyFsmStageLastUpdateTime": cfprApStatsCollectionPolicyFsmStageLastUpdateTime,
       "cfprApStatsCollectionPolicyFsmStageName": cfprApStatsCollectionPolicyFsmStageName,
       "cfprApStatsCollectionPolicyFsmStageOrder": cfprApStatsCollectionPolicyFsmStageOrder,
       "cfprApStatsCollectionPolicyFsmStageRetry": cfprApStatsCollectionPolicyFsmStageRetry,
       "cfprApStatsCollectionPolicyFsmStageStageStatus": cfprApStatsCollectionPolicyFsmStageStageStatus,
       "cfprApStatsCollectionPolicyFsmTaskTable": cfprApStatsCollectionPolicyFsmTaskTable,
       "cfprApStatsCollectionPolicyFsmTaskEntry": cfprApStatsCollectionPolicyFsmTaskEntry,
       "cfprApStatsCollectionPolicyFsmTaskInstanceId": cfprApStatsCollectionPolicyFsmTaskInstanceId,
       "cfprApStatsCollectionPolicyFsmTaskDn": cfprApStatsCollectionPolicyFsmTaskDn,
       "cfprApStatsCollectionPolicyFsmTaskRn": cfprApStatsCollectionPolicyFsmTaskRn,
       "cfprApStatsCollectionPolicyFsmTaskCompletion": cfprApStatsCollectionPolicyFsmTaskCompletion,
       "cfprApStatsCollectionPolicyFsmTaskFlags": cfprApStatsCollectionPolicyFsmTaskFlags,
       "cfprApStatsCollectionPolicyFsmTaskItem": cfprApStatsCollectionPolicyFsmTaskItem,
       "cfprApStatsCollectionPolicyFsmTaskSeqId": cfprApStatsCollectionPolicyFsmTaskSeqId,
       "cfprApStatsHolderTable": cfprApStatsHolderTable,
       "cfprApStatsHolderEntry": cfprApStatsHolderEntry,
       "cfprApStatsHolderInstanceId": cfprApStatsHolderInstanceId,
       "cfprApStatsHolderDn": cfprApStatsHolderDn,
       "cfprApStatsHolderRn": cfprApStatsHolderRn,
       "cfprApStatsHolderName": cfprApStatsHolderName,
       "cfprApStatsThr32DefinitionTable": cfprApStatsThr32DefinitionTable,
       "cfprApStatsThr32DefinitionEntry": cfprApStatsThr32DefinitionEntry,
       "cfprApStatsThr32DefinitionInstanceId": cfprApStatsThr32DefinitionInstanceId,
       "cfprApStatsThr32DefinitionDn": cfprApStatsThr32DefinitionDn,
       "cfprApStatsThr32DefinitionRn": cfprApStatsThr32DefinitionRn,
       "cfprApStatsThr32DefinitionDescr": cfprApStatsThr32DefinitionDescr,
       "cfprApStatsThr32DefinitionIntId": cfprApStatsThr32DefinitionIntId,
       "cfprApStatsThr32DefinitionName": cfprApStatsThr32DefinitionName,
       "cfprApStatsThr32DefinitionNormalValue": cfprApStatsThr32DefinitionNormalValue,
       "cfprApStatsThr32DefinitionPolicyLevel": cfprApStatsThr32DefinitionPolicyLevel,
       "cfprApStatsThr32DefinitionPolicyOwner": cfprApStatsThr32DefinitionPolicyOwner,
       "cfprApStatsThr32DefinitionPropId": cfprApStatsThr32DefinitionPropId,
       "cfprApStatsThr32DefinitionPropType": cfprApStatsThr32DefinitionPropType,
       "cfprApStatsThr32ValueTable": cfprApStatsThr32ValueTable,
       "cfprApStatsThr32ValueEntry": cfprApStatsThr32ValueEntry,
       "cfprApStatsThr32ValueInstanceId": cfprApStatsThr32ValueInstanceId,
       "cfprApStatsThr32ValueDn": cfprApStatsThr32ValueDn,
       "cfprApStatsThr32ValueRn": cfprApStatsThr32ValueRn,
       "cfprApStatsThr32ValueDeescalating": cfprApStatsThr32ValueDeescalating,
       "cfprApStatsThr32ValueDescr": cfprApStatsThr32ValueDescr,
       "cfprApStatsThr32ValueDirection": cfprApStatsThr32ValueDirection,
       "cfprApStatsThr32ValueEscalating": cfprApStatsThr32ValueEscalating,
       "cfprApStatsThr32ValueIntId": cfprApStatsThr32ValueIntId,
       "cfprApStatsThr32ValueName": cfprApStatsThr32ValueName,
       "cfprApStatsThr32ValuePolicyLevel": cfprApStatsThr32ValuePolicyLevel,
       "cfprApStatsThr32ValuePolicyOwner": cfprApStatsThr32ValuePolicyOwner,
       "cfprApStatsThr32ValuePropType": cfprApStatsThr32ValuePropType,
       "cfprApStatsThr32ValueSeverity": cfprApStatsThr32ValueSeverity,
       "cfprApStatsThr64DefinitionTable": cfprApStatsThr64DefinitionTable,
       "cfprApStatsThr64DefinitionEntry": cfprApStatsThr64DefinitionEntry,
       "cfprApStatsThr64DefinitionInstanceId": cfprApStatsThr64DefinitionInstanceId,
       "cfprApStatsThr64DefinitionDn": cfprApStatsThr64DefinitionDn,
       "cfprApStatsThr64DefinitionRn": cfprApStatsThr64DefinitionRn,
       "cfprApStatsThr64DefinitionDescr": cfprApStatsThr64DefinitionDescr,
       "cfprApStatsThr64DefinitionIntId": cfprApStatsThr64DefinitionIntId,
       "cfprApStatsThr64DefinitionName": cfprApStatsThr64DefinitionName,
       "cfprApStatsThr64DefinitionNormalValue": cfprApStatsThr64DefinitionNormalValue,
       "cfprApStatsThr64DefinitionPolicyLevel": cfprApStatsThr64DefinitionPolicyLevel,
       "cfprApStatsThr64DefinitionPolicyOwner": cfprApStatsThr64DefinitionPolicyOwner,
       "cfprApStatsThr64DefinitionPropId": cfprApStatsThr64DefinitionPropId,
       "cfprApStatsThr64DefinitionPropType": cfprApStatsThr64DefinitionPropType,
       "cfprApStatsThr64ValueTable": cfprApStatsThr64ValueTable,
       "cfprApStatsThr64ValueEntry": cfprApStatsThr64ValueEntry,
       "cfprApStatsThr64ValueInstanceId": cfprApStatsThr64ValueInstanceId,
       "cfprApStatsThr64ValueDn": cfprApStatsThr64ValueDn,
       "cfprApStatsThr64ValueRn": cfprApStatsThr64ValueRn,
       "cfprApStatsThr64ValueDeescalating": cfprApStatsThr64ValueDeescalating,
       "cfprApStatsThr64ValueDescr": cfprApStatsThr64ValueDescr,
       "cfprApStatsThr64ValueDirection": cfprApStatsThr64ValueDirection,
       "cfprApStatsThr64ValueEscalating": cfprApStatsThr64ValueEscalating,
       "cfprApStatsThr64ValueIntId": cfprApStatsThr64ValueIntId,
       "cfprApStatsThr64ValueName": cfprApStatsThr64ValueName,
       "cfprApStatsThr64ValuePolicyLevel": cfprApStatsThr64ValuePolicyLevel,
       "cfprApStatsThr64ValuePolicyOwner": cfprApStatsThr64ValuePolicyOwner,
       "cfprApStatsThr64ValuePropType": cfprApStatsThr64ValuePropType,
       "cfprApStatsThr64ValueSeverity": cfprApStatsThr64ValueSeverity,
       "cfprApStatsThrFloatDefinitionTable": cfprApStatsThrFloatDefinitionTable,
       "cfprApStatsThrFloatDefinitionEntry": cfprApStatsThrFloatDefinitionEntry,
       "cfprApStatsThrFloatDefinitionInstanceId": cfprApStatsThrFloatDefinitionInstanceId,
       "cfprApStatsThrFloatDefinitionDn": cfprApStatsThrFloatDefinitionDn,
       "cfprApStatsThrFloatDefinitionRn": cfprApStatsThrFloatDefinitionRn,
       "cfprApStatsThrFloatDefinitionDescr": cfprApStatsThrFloatDefinitionDescr,
       "cfprApStatsThrFloatDefinitionIntId": cfprApStatsThrFloatDefinitionIntId,
       "cfprApStatsThrFloatDefinitionName": cfprApStatsThrFloatDefinitionName,
       "cfprApStatsThrFloatDefinitionNormalValue": cfprApStatsThrFloatDefinitionNormalValue,
       "cfprApStatsThrFloatDefinitionPolicyLevel": cfprApStatsThrFloatDefinitionPolicyLevel,
       "cfprApStatsThrFloatDefinitionPolicyOwner": cfprApStatsThrFloatDefinitionPolicyOwner,
       "cfprApStatsThrFloatDefinitionPropId": cfprApStatsThrFloatDefinitionPropId,
       "cfprApStatsThrFloatDefinitionPropType": cfprApStatsThrFloatDefinitionPropType,
       "cfprApStatsThrFloatValueTable": cfprApStatsThrFloatValueTable,
       "cfprApStatsThrFloatValueEntry": cfprApStatsThrFloatValueEntry,
       "cfprApStatsThrFloatValueInstanceId": cfprApStatsThrFloatValueInstanceId,
       "cfprApStatsThrFloatValueDn": cfprApStatsThrFloatValueDn,
       "cfprApStatsThrFloatValueRn": cfprApStatsThrFloatValueRn,
       "cfprApStatsThrFloatValueDeescalating": cfprApStatsThrFloatValueDeescalating,
       "cfprApStatsThrFloatValueDescr": cfprApStatsThrFloatValueDescr,
       "cfprApStatsThrFloatValueDirection": cfprApStatsThrFloatValueDirection,
       "cfprApStatsThrFloatValueEscalating": cfprApStatsThrFloatValueEscalating,
       "cfprApStatsThrFloatValueIntId": cfprApStatsThrFloatValueIntId,
       "cfprApStatsThrFloatValueName": cfprApStatsThrFloatValueName,
       "cfprApStatsThrFloatValuePolicyLevel": cfprApStatsThrFloatValuePolicyLevel,
       "cfprApStatsThrFloatValuePolicyOwner": cfprApStatsThrFloatValuePolicyOwner,
       "cfprApStatsThrFloatValuePropType": cfprApStatsThrFloatValuePropType,
       "cfprApStatsThrFloatValueSeverity": cfprApStatsThrFloatValueSeverity,
       "cfprApStatsThresholdClassTable": cfprApStatsThresholdClassTable,
       "cfprApStatsThresholdClassEntry": cfprApStatsThresholdClassEntry,
       "cfprApStatsThresholdClassInstanceId": cfprApStatsThresholdClassInstanceId,
       "cfprApStatsThresholdClassDn": cfprApStatsThresholdClassDn,
       "cfprApStatsThresholdClassRn": cfprApStatsThresholdClassRn,
       "cfprApStatsThresholdClassDescr": cfprApStatsThresholdClassDescr,
       "cfprApStatsThresholdClassIntId": cfprApStatsThresholdClassIntId,
       "cfprApStatsThresholdClassName": cfprApStatsThresholdClassName,
       "cfprApStatsThresholdClassPolicyLevel": cfprApStatsThresholdClassPolicyLevel,
       "cfprApStatsThresholdClassPolicyOwner": cfprApStatsThresholdClassPolicyOwner,
       "cfprApStatsThresholdClassStatsClassId": cfprApStatsThresholdClassStatsClassId,
       "cfprApStatsThresholdPolicyTable": cfprApStatsThresholdPolicyTable,
       "cfprApStatsThresholdPolicyEntry": cfprApStatsThresholdPolicyEntry,
       "cfprApStatsThresholdPolicyInstanceId": cfprApStatsThresholdPolicyInstanceId,
       "cfprApStatsThresholdPolicyDn": cfprApStatsThresholdPolicyDn,
       "cfprApStatsThresholdPolicyRn": cfprApStatsThresholdPolicyRn,
       "cfprApStatsThresholdPolicyDescr": cfprApStatsThresholdPolicyDescr,
       "cfprApStatsThresholdPolicyIntId": cfprApStatsThresholdPolicyIntId,
       "cfprApStatsThresholdPolicyName": cfprApStatsThresholdPolicyName,
       "cfprApStatsThresholdPolicyPolicyLevel": cfprApStatsThresholdPolicyPolicyLevel,
       "cfprApStatsThresholdPolicyPolicyOwner": cfprApStatsThresholdPolicyPolicyOwner}
)
