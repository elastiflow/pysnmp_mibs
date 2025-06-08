# SNMP MIB module (CISCO-FIREPOWER-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-STATS-MIB.mib
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
 CfprConditionSeverity,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprPolicyPolicyOwner,
 CfprStatsCollectionDomain,
 CfprStatsCollectionInterval,
 CfprStatsCollectionPolicyFsmCurrentFsm,
 CfprStatsCollectionPolicyFsmStageName,
 CfprStatsCollectionPolicyFsmTaskItem,
 CfprStatsReportingInterval,
 CfprStatsThr32DefinitionPropType,
 CfprStatsThr32ValuePropType,
 CfprStatsThr64DefinitionPropType,
 CfprStatsThr64ValuePropType,
 CfprStatsThrFloatDefinitionPropType,
 CfprStatsThrFloatValuePropType,
 CfprStatsThresholdDirection) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprConditionSeverity",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprPolicyPolicyOwner",
    "CfprStatsCollectionDomain",
    "CfprStatsCollectionInterval",
    "CfprStatsCollectionPolicyFsmCurrentFsm",
    "CfprStatsCollectionPolicyFsmStageName",
    "CfprStatsCollectionPolicyFsmTaskItem",
    "CfprStatsReportingInterval",
    "CfprStatsThr32DefinitionPropType",
    "CfprStatsThr32ValuePropType",
    "CfprStatsThr64DefinitionPropType",
    "CfprStatsThr64ValuePropType",
    "CfprStatsThrFloatDefinitionPropType",
    "CfprStatsThrFloatValuePropType",
    "CfprStatsThresholdDirection")

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

cfprStatsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprStatsCollectionPolicyTable_Object = MibTable
cfprStatsCollectionPolicyTable = _CfprStatsCollectionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1)
)
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyTable.setStatus("current")
_CfprStatsCollectionPolicyEntry_Object = MibTableRow
cfprStatsCollectionPolicyEntry = _CfprStatsCollectionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1)
)
cfprStatsCollectionPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsCollectionPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyEntry.setStatus("current")
_CfprStatsCollectionPolicyInstanceId_Type = CfprManagedObjectId
_CfprStatsCollectionPolicyInstanceId_Object = MibTableColumn
cfprStatsCollectionPolicyInstanceId = _CfprStatsCollectionPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 1),
    _CfprStatsCollectionPolicyInstanceId_Type()
)
cfprStatsCollectionPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyInstanceId.setStatus("current")
_CfprStatsCollectionPolicyDn_Type = CfprManagedObjectDn
_CfprStatsCollectionPolicyDn_Object = MibTableColumn
cfprStatsCollectionPolicyDn = _CfprStatsCollectionPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 2),
    _CfprStatsCollectionPolicyDn_Type()
)
cfprStatsCollectionPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyDn.setStatus("current")
_CfprStatsCollectionPolicyRn_Type = SnmpAdminString
_CfprStatsCollectionPolicyRn_Object = MibTableColumn
cfprStatsCollectionPolicyRn = _CfprStatsCollectionPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 3),
    _CfprStatsCollectionPolicyRn_Type()
)
cfprStatsCollectionPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyRn.setStatus("current")
_CfprStatsCollectionPolicyCollectionInterval_Type = CfprStatsCollectionInterval
_CfprStatsCollectionPolicyCollectionInterval_Object = MibTableColumn
cfprStatsCollectionPolicyCollectionInterval = _CfprStatsCollectionPolicyCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 4),
    _CfprStatsCollectionPolicyCollectionInterval_Type()
)
cfprStatsCollectionPolicyCollectionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyCollectionInterval.setStatus("current")
_CfprStatsCollectionPolicyFsmDescr_Type = SnmpAdminString
_CfprStatsCollectionPolicyFsmDescr_Object = MibTableColumn
cfprStatsCollectionPolicyFsmDescr = _CfprStatsCollectionPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 5),
    _CfprStatsCollectionPolicyFsmDescr_Type()
)
cfprStatsCollectionPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmDescr.setStatus("current")
_CfprStatsCollectionPolicyFsmPrev_Type = SnmpAdminString
_CfprStatsCollectionPolicyFsmPrev_Object = MibTableColumn
cfprStatsCollectionPolicyFsmPrev = _CfprStatsCollectionPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 6),
    _CfprStatsCollectionPolicyFsmPrev_Type()
)
cfprStatsCollectionPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmPrev.setStatus("current")
_CfprStatsCollectionPolicyFsmProgr_Type = Gauge32
_CfprStatsCollectionPolicyFsmProgr_Object = MibTableColumn
cfprStatsCollectionPolicyFsmProgr = _CfprStatsCollectionPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 7),
    _CfprStatsCollectionPolicyFsmProgr_Type()
)
cfprStatsCollectionPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmProgr.setStatus("current")
_CfprStatsCollectionPolicyFsmRmtInvErrCode_Type = Gauge32
_CfprStatsCollectionPolicyFsmRmtInvErrCode_Object = MibTableColumn
cfprStatsCollectionPolicyFsmRmtInvErrCode = _CfprStatsCollectionPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 8),
    _CfprStatsCollectionPolicyFsmRmtInvErrCode_Type()
)
cfprStatsCollectionPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmRmtInvErrCode.setStatus("current")
_CfprStatsCollectionPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprStatsCollectionPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cfprStatsCollectionPolicyFsmRmtInvErrDescr = _CfprStatsCollectionPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 9),
    _CfprStatsCollectionPolicyFsmRmtInvErrDescr_Type()
)
cfprStatsCollectionPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmRmtInvErrDescr.setStatus("current")
_CfprStatsCollectionPolicyFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprStatsCollectionPolicyFsmRmtInvRslt_Object = MibTableColumn
cfprStatsCollectionPolicyFsmRmtInvRslt = _CfprStatsCollectionPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 10),
    _CfprStatsCollectionPolicyFsmRmtInvRslt_Type()
)
cfprStatsCollectionPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmRmtInvRslt.setStatus("current")
_CfprStatsCollectionPolicyFsmStageDescr_Type = SnmpAdminString
_CfprStatsCollectionPolicyFsmStageDescr_Object = MibTableColumn
cfprStatsCollectionPolicyFsmStageDescr = _CfprStatsCollectionPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 11),
    _CfprStatsCollectionPolicyFsmStageDescr_Type()
)
cfprStatsCollectionPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStageDescr.setStatus("current")
_CfprStatsCollectionPolicyFsmStamp_Type = DateAndTime
_CfprStatsCollectionPolicyFsmStamp_Object = MibTableColumn
cfprStatsCollectionPolicyFsmStamp = _CfprStatsCollectionPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 12),
    _CfprStatsCollectionPolicyFsmStamp_Type()
)
cfprStatsCollectionPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStamp.setStatus("current")
_CfprStatsCollectionPolicyFsmStatus_Type = SnmpAdminString
_CfprStatsCollectionPolicyFsmStatus_Object = MibTableColumn
cfprStatsCollectionPolicyFsmStatus = _CfprStatsCollectionPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 13),
    _CfprStatsCollectionPolicyFsmStatus_Type()
)
cfprStatsCollectionPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStatus.setStatus("current")
_CfprStatsCollectionPolicyFsmTry_Type = Gauge32
_CfprStatsCollectionPolicyFsmTry_Object = MibTableColumn
cfprStatsCollectionPolicyFsmTry = _CfprStatsCollectionPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 14),
    _CfprStatsCollectionPolicyFsmTry_Type()
)
cfprStatsCollectionPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmTry.setStatus("current")
_CfprStatsCollectionPolicyId_Type = Gauge32
_CfprStatsCollectionPolicyId_Object = MibTableColumn
cfprStatsCollectionPolicyId = _CfprStatsCollectionPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 15),
    _CfprStatsCollectionPolicyId_Type()
)
cfprStatsCollectionPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyId.setStatus("current")
_CfprStatsCollectionPolicyName_Type = CfprStatsCollectionDomain
_CfprStatsCollectionPolicyName_Object = MibTableColumn
cfprStatsCollectionPolicyName = _CfprStatsCollectionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 16),
    _CfprStatsCollectionPolicyName_Type()
)
cfprStatsCollectionPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyName.setStatus("current")
_CfprStatsCollectionPolicyReportingInterval_Type = CfprStatsReportingInterval
_CfprStatsCollectionPolicyReportingInterval_Object = MibTableColumn
cfprStatsCollectionPolicyReportingInterval = _CfprStatsCollectionPolicyReportingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 1, 1, 17),
    _CfprStatsCollectionPolicyReportingInterval_Type()
)
cfprStatsCollectionPolicyReportingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyReportingInterval.setStatus("current")
_CfprStatsCollectionPolicyFsmTable_Object = MibTable
cfprStatsCollectionPolicyFsmTable = _CfprStatsCollectionPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2)
)
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmTable.setStatus("current")
_CfprStatsCollectionPolicyFsmEntry_Object = MibTableRow
cfprStatsCollectionPolicyFsmEntry = _CfprStatsCollectionPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2, 1)
)
cfprStatsCollectionPolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsCollectionPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmEntry.setStatus("current")
_CfprStatsCollectionPolicyFsmInstanceId_Type = CfprManagedObjectId
_CfprStatsCollectionPolicyFsmInstanceId_Object = MibTableColumn
cfprStatsCollectionPolicyFsmInstanceId = _CfprStatsCollectionPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2, 1, 1),
    _CfprStatsCollectionPolicyFsmInstanceId_Type()
)
cfprStatsCollectionPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmInstanceId.setStatus("current")
_CfprStatsCollectionPolicyFsmDn_Type = CfprManagedObjectDn
_CfprStatsCollectionPolicyFsmDn_Object = MibTableColumn
cfprStatsCollectionPolicyFsmDn = _CfprStatsCollectionPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2, 1, 2),
    _CfprStatsCollectionPolicyFsmDn_Type()
)
cfprStatsCollectionPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmDn.setStatus("current")
_CfprStatsCollectionPolicyFsmRn_Type = SnmpAdminString
_CfprStatsCollectionPolicyFsmRn_Object = MibTableColumn
cfprStatsCollectionPolicyFsmRn = _CfprStatsCollectionPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2, 1, 3),
    _CfprStatsCollectionPolicyFsmRn_Type()
)
cfprStatsCollectionPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmRn.setStatus("current")
_CfprStatsCollectionPolicyFsmCompletionTime_Type = DateAndTime
_CfprStatsCollectionPolicyFsmCompletionTime_Object = MibTableColumn
cfprStatsCollectionPolicyFsmCompletionTime = _CfprStatsCollectionPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2, 1, 4),
    _CfprStatsCollectionPolicyFsmCompletionTime_Type()
)
cfprStatsCollectionPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmCompletionTime.setStatus("current")
_CfprStatsCollectionPolicyFsmCurrentFsm_Type = CfprStatsCollectionPolicyFsmCurrentFsm
_CfprStatsCollectionPolicyFsmCurrentFsm_Object = MibTableColumn
cfprStatsCollectionPolicyFsmCurrentFsm = _CfprStatsCollectionPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2, 1, 5),
    _CfprStatsCollectionPolicyFsmCurrentFsm_Type()
)
cfprStatsCollectionPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmCurrentFsm.setStatus("current")
_CfprStatsCollectionPolicyFsmDescrData_Type = SnmpAdminString
_CfprStatsCollectionPolicyFsmDescrData_Object = MibTableColumn
cfprStatsCollectionPolicyFsmDescrData = _CfprStatsCollectionPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2, 1, 6),
    _CfprStatsCollectionPolicyFsmDescrData_Type()
)
cfprStatsCollectionPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmDescrData.setStatus("current")
_CfprStatsCollectionPolicyFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprStatsCollectionPolicyFsmFsmStatus_Object = MibTableColumn
cfprStatsCollectionPolicyFsmFsmStatus = _CfprStatsCollectionPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2, 1, 7),
    _CfprStatsCollectionPolicyFsmFsmStatus_Type()
)
cfprStatsCollectionPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmFsmStatus.setStatus("current")
_CfprStatsCollectionPolicyFsmProgress_Type = Gauge32
_CfprStatsCollectionPolicyFsmProgress_Object = MibTableColumn
cfprStatsCollectionPolicyFsmProgress = _CfprStatsCollectionPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2, 1, 8),
    _CfprStatsCollectionPolicyFsmProgress_Type()
)
cfprStatsCollectionPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmProgress.setStatus("current")
_CfprStatsCollectionPolicyFsmRmtErrCode_Type = Gauge32
_CfprStatsCollectionPolicyFsmRmtErrCode_Object = MibTableColumn
cfprStatsCollectionPolicyFsmRmtErrCode = _CfprStatsCollectionPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2, 1, 9),
    _CfprStatsCollectionPolicyFsmRmtErrCode_Type()
)
cfprStatsCollectionPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmRmtErrCode.setStatus("current")
_CfprStatsCollectionPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprStatsCollectionPolicyFsmRmtErrDescr_Object = MibTableColumn
cfprStatsCollectionPolicyFsmRmtErrDescr = _CfprStatsCollectionPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2, 1, 10),
    _CfprStatsCollectionPolicyFsmRmtErrDescr_Type()
)
cfprStatsCollectionPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmRmtErrDescr.setStatus("current")
_CfprStatsCollectionPolicyFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprStatsCollectionPolicyFsmRmtRslt_Object = MibTableColumn
cfprStatsCollectionPolicyFsmRmtRslt = _CfprStatsCollectionPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 2, 1, 11),
    _CfprStatsCollectionPolicyFsmRmtRslt_Type()
)
cfprStatsCollectionPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmRmtRslt.setStatus("current")
_CfprStatsCollectionPolicyFsmStageTable_Object = MibTable
cfprStatsCollectionPolicyFsmStageTable = _CfprStatsCollectionPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 3)
)
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStageTable.setStatus("current")
_CfprStatsCollectionPolicyFsmStageEntry_Object = MibTableRow
cfprStatsCollectionPolicyFsmStageEntry = _CfprStatsCollectionPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 3, 1)
)
cfprStatsCollectionPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsCollectionPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStageEntry.setStatus("current")
_CfprStatsCollectionPolicyFsmStageInstanceId_Type = CfprManagedObjectId
_CfprStatsCollectionPolicyFsmStageInstanceId_Object = MibTableColumn
cfprStatsCollectionPolicyFsmStageInstanceId = _CfprStatsCollectionPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 3, 1, 1),
    _CfprStatsCollectionPolicyFsmStageInstanceId_Type()
)
cfprStatsCollectionPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStageInstanceId.setStatus("current")
_CfprStatsCollectionPolicyFsmStageDn_Type = CfprManagedObjectDn
_CfprStatsCollectionPolicyFsmStageDn_Object = MibTableColumn
cfprStatsCollectionPolicyFsmStageDn = _CfprStatsCollectionPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 3, 1, 2),
    _CfprStatsCollectionPolicyFsmStageDn_Type()
)
cfprStatsCollectionPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStageDn.setStatus("current")
_CfprStatsCollectionPolicyFsmStageRn_Type = SnmpAdminString
_CfprStatsCollectionPolicyFsmStageRn_Object = MibTableColumn
cfprStatsCollectionPolicyFsmStageRn = _CfprStatsCollectionPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 3, 1, 3),
    _CfprStatsCollectionPolicyFsmStageRn_Type()
)
cfprStatsCollectionPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStageRn.setStatus("current")
_CfprStatsCollectionPolicyFsmStageDescrData_Type = SnmpAdminString
_CfprStatsCollectionPolicyFsmStageDescrData_Object = MibTableColumn
cfprStatsCollectionPolicyFsmStageDescrData = _CfprStatsCollectionPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 3, 1, 4),
    _CfprStatsCollectionPolicyFsmStageDescrData_Type()
)
cfprStatsCollectionPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStageDescrData.setStatus("current")
_CfprStatsCollectionPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprStatsCollectionPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprStatsCollectionPolicyFsmStageLastUpdateTime = _CfprStatsCollectionPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 3, 1, 5),
    _CfprStatsCollectionPolicyFsmStageLastUpdateTime_Type()
)
cfprStatsCollectionPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStageLastUpdateTime.setStatus("current")
_CfprStatsCollectionPolicyFsmStageName_Type = CfprStatsCollectionPolicyFsmStageName
_CfprStatsCollectionPolicyFsmStageName_Object = MibTableColumn
cfprStatsCollectionPolicyFsmStageName = _CfprStatsCollectionPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 3, 1, 6),
    _CfprStatsCollectionPolicyFsmStageName_Type()
)
cfprStatsCollectionPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStageName.setStatus("current")
_CfprStatsCollectionPolicyFsmStageOrder_Type = Gauge32
_CfprStatsCollectionPolicyFsmStageOrder_Object = MibTableColumn
cfprStatsCollectionPolicyFsmStageOrder = _CfprStatsCollectionPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 3, 1, 7),
    _CfprStatsCollectionPolicyFsmStageOrder_Type()
)
cfprStatsCollectionPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStageOrder.setStatus("current")
_CfprStatsCollectionPolicyFsmStageRetry_Type = Gauge32
_CfprStatsCollectionPolicyFsmStageRetry_Object = MibTableColumn
cfprStatsCollectionPolicyFsmStageRetry = _CfprStatsCollectionPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 3, 1, 8),
    _CfprStatsCollectionPolicyFsmStageRetry_Type()
)
cfprStatsCollectionPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStageRetry.setStatus("current")
_CfprStatsCollectionPolicyFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprStatsCollectionPolicyFsmStageStageStatus_Object = MibTableColumn
cfprStatsCollectionPolicyFsmStageStageStatus = _CfprStatsCollectionPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 3, 1, 9),
    _CfprStatsCollectionPolicyFsmStageStageStatus_Type()
)
cfprStatsCollectionPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmStageStageStatus.setStatus("current")
_CfprStatsCollectionPolicyFsmTaskTable_Object = MibTable
cfprStatsCollectionPolicyFsmTaskTable = _CfprStatsCollectionPolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 4)
)
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmTaskTable.setStatus("current")
_CfprStatsCollectionPolicyFsmTaskEntry_Object = MibTableRow
cfprStatsCollectionPolicyFsmTaskEntry = _CfprStatsCollectionPolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 4, 1)
)
cfprStatsCollectionPolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsCollectionPolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmTaskEntry.setStatus("current")
_CfprStatsCollectionPolicyFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprStatsCollectionPolicyFsmTaskInstanceId_Object = MibTableColumn
cfprStatsCollectionPolicyFsmTaskInstanceId = _CfprStatsCollectionPolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 4, 1, 1),
    _CfprStatsCollectionPolicyFsmTaskInstanceId_Type()
)
cfprStatsCollectionPolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmTaskInstanceId.setStatus("current")
_CfprStatsCollectionPolicyFsmTaskDn_Type = CfprManagedObjectDn
_CfprStatsCollectionPolicyFsmTaskDn_Object = MibTableColumn
cfprStatsCollectionPolicyFsmTaskDn = _CfprStatsCollectionPolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 4, 1, 2),
    _CfprStatsCollectionPolicyFsmTaskDn_Type()
)
cfprStatsCollectionPolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmTaskDn.setStatus("current")
_CfprStatsCollectionPolicyFsmTaskRn_Type = SnmpAdminString
_CfprStatsCollectionPolicyFsmTaskRn_Object = MibTableColumn
cfprStatsCollectionPolicyFsmTaskRn = _CfprStatsCollectionPolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 4, 1, 3),
    _CfprStatsCollectionPolicyFsmTaskRn_Type()
)
cfprStatsCollectionPolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmTaskRn.setStatus("current")
_CfprStatsCollectionPolicyFsmTaskCompletion_Type = CfprFsmCompletion
_CfprStatsCollectionPolicyFsmTaskCompletion_Object = MibTableColumn
cfprStatsCollectionPolicyFsmTaskCompletion = _CfprStatsCollectionPolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 4, 1, 4),
    _CfprStatsCollectionPolicyFsmTaskCompletion_Type()
)
cfprStatsCollectionPolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmTaskCompletion.setStatus("current")
_CfprStatsCollectionPolicyFsmTaskFlags_Type = CfprFsmFlags
_CfprStatsCollectionPolicyFsmTaskFlags_Object = MibTableColumn
cfprStatsCollectionPolicyFsmTaskFlags = _CfprStatsCollectionPolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 4, 1, 5),
    _CfprStatsCollectionPolicyFsmTaskFlags_Type()
)
cfprStatsCollectionPolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmTaskFlags.setStatus("current")
_CfprStatsCollectionPolicyFsmTaskItem_Type = CfprStatsCollectionPolicyFsmTaskItem
_CfprStatsCollectionPolicyFsmTaskItem_Object = MibTableColumn
cfprStatsCollectionPolicyFsmTaskItem = _CfprStatsCollectionPolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 4, 1, 6),
    _CfprStatsCollectionPolicyFsmTaskItem_Type()
)
cfprStatsCollectionPolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmTaskItem.setStatus("current")
_CfprStatsCollectionPolicyFsmTaskSeqId_Type = Gauge32
_CfprStatsCollectionPolicyFsmTaskSeqId_Object = MibTableColumn
cfprStatsCollectionPolicyFsmTaskSeqId = _CfprStatsCollectionPolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 4, 1, 7),
    _CfprStatsCollectionPolicyFsmTaskSeqId_Type()
)
cfprStatsCollectionPolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsCollectionPolicyFsmTaskSeqId.setStatus("current")
_CfprStatsHolderTable_Object = MibTable
cfprStatsHolderTable = _CfprStatsHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 5)
)
if mibBuilder.loadTexts:
    cfprStatsHolderTable.setStatus("current")
_CfprStatsHolderEntry_Object = MibTableRow
cfprStatsHolderEntry = _CfprStatsHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 5, 1)
)
cfprStatsHolderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsHolderEntry.setStatus("current")
_CfprStatsHolderInstanceId_Type = CfprManagedObjectId
_CfprStatsHolderInstanceId_Object = MibTableColumn
cfprStatsHolderInstanceId = _CfprStatsHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 5, 1, 1),
    _CfprStatsHolderInstanceId_Type()
)
cfprStatsHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsHolderInstanceId.setStatus("current")
_CfprStatsHolderDn_Type = CfprManagedObjectDn
_CfprStatsHolderDn_Object = MibTableColumn
cfprStatsHolderDn = _CfprStatsHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 5, 1, 2),
    _CfprStatsHolderDn_Type()
)
cfprStatsHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsHolderDn.setStatus("current")
_CfprStatsHolderRn_Type = SnmpAdminString
_CfprStatsHolderRn_Object = MibTableColumn
cfprStatsHolderRn = _CfprStatsHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 5, 1, 3),
    _CfprStatsHolderRn_Type()
)
cfprStatsHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsHolderRn.setStatus("current")
_CfprStatsHolderName_Type = SnmpAdminString
_CfprStatsHolderName_Object = MibTableColumn
cfprStatsHolderName = _CfprStatsHolderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 5, 1, 4),
    _CfprStatsHolderName_Type()
)
cfprStatsHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsHolderName.setStatus("current")
_CfprStatsThr32DefinitionTable_Object = MibTable
cfprStatsThr32DefinitionTable = _CfprStatsThr32DefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6)
)
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionTable.setStatus("current")
_CfprStatsThr32DefinitionEntry_Object = MibTableRow
cfprStatsThr32DefinitionEntry = _CfprStatsThr32DefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6, 1)
)
cfprStatsThr32DefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsThr32DefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionEntry.setStatus("current")
_CfprStatsThr32DefinitionInstanceId_Type = CfprManagedObjectId
_CfprStatsThr32DefinitionInstanceId_Object = MibTableColumn
cfprStatsThr32DefinitionInstanceId = _CfprStatsThr32DefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6, 1, 1),
    _CfprStatsThr32DefinitionInstanceId_Type()
)
cfprStatsThr32DefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionInstanceId.setStatus("current")
_CfprStatsThr32DefinitionDn_Type = CfprManagedObjectDn
_CfprStatsThr32DefinitionDn_Object = MibTableColumn
cfprStatsThr32DefinitionDn = _CfprStatsThr32DefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6, 1, 2),
    _CfprStatsThr32DefinitionDn_Type()
)
cfprStatsThr32DefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionDn.setStatus("current")
_CfprStatsThr32DefinitionRn_Type = SnmpAdminString
_CfprStatsThr32DefinitionRn_Object = MibTableColumn
cfprStatsThr32DefinitionRn = _CfprStatsThr32DefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6, 1, 3),
    _CfprStatsThr32DefinitionRn_Type()
)
cfprStatsThr32DefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionRn.setStatus("current")
_CfprStatsThr32DefinitionDescr_Type = SnmpAdminString
_CfprStatsThr32DefinitionDescr_Object = MibTableColumn
cfprStatsThr32DefinitionDescr = _CfprStatsThr32DefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6, 1, 4),
    _CfprStatsThr32DefinitionDescr_Type()
)
cfprStatsThr32DefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionDescr.setStatus("current")
_CfprStatsThr32DefinitionIntId_Type = SnmpAdminString
_CfprStatsThr32DefinitionIntId_Object = MibTableColumn
cfprStatsThr32DefinitionIntId = _CfprStatsThr32DefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6, 1, 5),
    _CfprStatsThr32DefinitionIntId_Type()
)
cfprStatsThr32DefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionIntId.setStatus("current")
_CfprStatsThr32DefinitionName_Type = SnmpAdminString
_CfprStatsThr32DefinitionName_Object = MibTableColumn
cfprStatsThr32DefinitionName = _CfprStatsThr32DefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6, 1, 6),
    _CfprStatsThr32DefinitionName_Type()
)
cfprStatsThr32DefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionName.setStatus("current")
_CfprStatsThr32DefinitionNormalValue_Type = Gauge32
_CfprStatsThr32DefinitionNormalValue_Object = MibTableColumn
cfprStatsThr32DefinitionNormalValue = _CfprStatsThr32DefinitionNormalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6, 1, 7),
    _CfprStatsThr32DefinitionNormalValue_Type()
)
cfprStatsThr32DefinitionNormalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionNormalValue.setStatus("current")
_CfprStatsThr32DefinitionPolicyLevel_Type = Gauge32
_CfprStatsThr32DefinitionPolicyLevel_Object = MibTableColumn
cfprStatsThr32DefinitionPolicyLevel = _CfprStatsThr32DefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6, 1, 8),
    _CfprStatsThr32DefinitionPolicyLevel_Type()
)
cfprStatsThr32DefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionPolicyLevel.setStatus("current")
_CfprStatsThr32DefinitionPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStatsThr32DefinitionPolicyOwner_Object = MibTableColumn
cfprStatsThr32DefinitionPolicyOwner = _CfprStatsThr32DefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6, 1, 9),
    _CfprStatsThr32DefinitionPolicyOwner_Type()
)
cfprStatsThr32DefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionPolicyOwner.setStatus("current")
_CfprStatsThr32DefinitionPropId_Type = SnmpAdminString
_CfprStatsThr32DefinitionPropId_Object = MibTableColumn
cfprStatsThr32DefinitionPropId = _CfprStatsThr32DefinitionPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6, 1, 10),
    _CfprStatsThr32DefinitionPropId_Type()
)
cfprStatsThr32DefinitionPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionPropId.setStatus("current")
_CfprStatsThr32DefinitionPropType_Type = CfprStatsThr32DefinitionPropType
_CfprStatsThr32DefinitionPropType_Object = MibTableColumn
cfprStatsThr32DefinitionPropType = _CfprStatsThr32DefinitionPropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 6, 1, 11),
    _CfprStatsThr32DefinitionPropType_Type()
)
cfprStatsThr32DefinitionPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32DefinitionPropType.setStatus("current")
_CfprStatsThr32ValueTable_Object = MibTable
cfprStatsThr32ValueTable = _CfprStatsThr32ValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7)
)
if mibBuilder.loadTexts:
    cfprStatsThr32ValueTable.setStatus("current")
_CfprStatsThr32ValueEntry_Object = MibTableRow
cfprStatsThr32ValueEntry = _CfprStatsThr32ValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1)
)
cfprStatsThr32ValueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsThr32ValueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsThr32ValueEntry.setStatus("current")
_CfprStatsThr32ValueInstanceId_Type = CfprManagedObjectId
_CfprStatsThr32ValueInstanceId_Object = MibTableColumn
cfprStatsThr32ValueInstanceId = _CfprStatsThr32ValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 1),
    _CfprStatsThr32ValueInstanceId_Type()
)
cfprStatsThr32ValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsThr32ValueInstanceId.setStatus("current")
_CfprStatsThr32ValueDn_Type = CfprManagedObjectDn
_CfprStatsThr32ValueDn_Object = MibTableColumn
cfprStatsThr32ValueDn = _CfprStatsThr32ValueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 2),
    _CfprStatsThr32ValueDn_Type()
)
cfprStatsThr32ValueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32ValueDn.setStatus("current")
_CfprStatsThr32ValueRn_Type = SnmpAdminString
_CfprStatsThr32ValueRn_Object = MibTableColumn
cfprStatsThr32ValueRn = _CfprStatsThr32ValueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 3),
    _CfprStatsThr32ValueRn_Type()
)
cfprStatsThr32ValueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32ValueRn.setStatus("current")
_CfprStatsThr32ValueDeescalating_Type = Gauge32
_CfprStatsThr32ValueDeescalating_Object = MibTableColumn
cfprStatsThr32ValueDeescalating = _CfprStatsThr32ValueDeescalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 4),
    _CfprStatsThr32ValueDeescalating_Type()
)
cfprStatsThr32ValueDeescalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32ValueDeescalating.setStatus("current")
_CfprStatsThr32ValueDescr_Type = SnmpAdminString
_CfprStatsThr32ValueDescr_Object = MibTableColumn
cfprStatsThr32ValueDescr = _CfprStatsThr32ValueDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 5),
    _CfprStatsThr32ValueDescr_Type()
)
cfprStatsThr32ValueDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32ValueDescr.setStatus("current")
_CfprStatsThr32ValueDirection_Type = CfprStatsThresholdDirection
_CfprStatsThr32ValueDirection_Object = MibTableColumn
cfprStatsThr32ValueDirection = _CfprStatsThr32ValueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 6),
    _CfprStatsThr32ValueDirection_Type()
)
cfprStatsThr32ValueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32ValueDirection.setStatus("current")
_CfprStatsThr32ValueEscalating_Type = Gauge32
_CfprStatsThr32ValueEscalating_Object = MibTableColumn
cfprStatsThr32ValueEscalating = _CfprStatsThr32ValueEscalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 7),
    _CfprStatsThr32ValueEscalating_Type()
)
cfprStatsThr32ValueEscalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32ValueEscalating.setStatus("current")
_CfprStatsThr32ValueIntId_Type = SnmpAdminString
_CfprStatsThr32ValueIntId_Object = MibTableColumn
cfprStatsThr32ValueIntId = _CfprStatsThr32ValueIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 8),
    _CfprStatsThr32ValueIntId_Type()
)
cfprStatsThr32ValueIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32ValueIntId.setStatus("current")
_CfprStatsThr32ValueName_Type = SnmpAdminString
_CfprStatsThr32ValueName_Object = MibTableColumn
cfprStatsThr32ValueName = _CfprStatsThr32ValueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 9),
    _CfprStatsThr32ValueName_Type()
)
cfprStatsThr32ValueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32ValueName.setStatus("current")
_CfprStatsThr32ValuePolicyLevel_Type = Gauge32
_CfprStatsThr32ValuePolicyLevel_Object = MibTableColumn
cfprStatsThr32ValuePolicyLevel = _CfprStatsThr32ValuePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 10),
    _CfprStatsThr32ValuePolicyLevel_Type()
)
cfprStatsThr32ValuePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32ValuePolicyLevel.setStatus("current")
_CfprStatsThr32ValuePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStatsThr32ValuePolicyOwner_Object = MibTableColumn
cfprStatsThr32ValuePolicyOwner = _CfprStatsThr32ValuePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 11),
    _CfprStatsThr32ValuePolicyOwner_Type()
)
cfprStatsThr32ValuePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32ValuePolicyOwner.setStatus("current")
_CfprStatsThr32ValuePropType_Type = CfprStatsThr32ValuePropType
_CfprStatsThr32ValuePropType_Object = MibTableColumn
cfprStatsThr32ValuePropType = _CfprStatsThr32ValuePropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 12),
    _CfprStatsThr32ValuePropType_Type()
)
cfprStatsThr32ValuePropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32ValuePropType.setStatus("current")
_CfprStatsThr32ValueSeverity_Type = CfprConditionSeverity
_CfprStatsThr32ValueSeverity_Object = MibTableColumn
cfprStatsThr32ValueSeverity = _CfprStatsThr32ValueSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 7, 1, 13),
    _CfprStatsThr32ValueSeverity_Type()
)
cfprStatsThr32ValueSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr32ValueSeverity.setStatus("current")
_CfprStatsThr64DefinitionTable_Object = MibTable
cfprStatsThr64DefinitionTable = _CfprStatsThr64DefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8)
)
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionTable.setStatus("current")
_CfprStatsThr64DefinitionEntry_Object = MibTableRow
cfprStatsThr64DefinitionEntry = _CfprStatsThr64DefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8, 1)
)
cfprStatsThr64DefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsThr64DefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionEntry.setStatus("current")
_CfprStatsThr64DefinitionInstanceId_Type = CfprManagedObjectId
_CfprStatsThr64DefinitionInstanceId_Object = MibTableColumn
cfprStatsThr64DefinitionInstanceId = _CfprStatsThr64DefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8, 1, 1),
    _CfprStatsThr64DefinitionInstanceId_Type()
)
cfprStatsThr64DefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionInstanceId.setStatus("current")
_CfprStatsThr64DefinitionDn_Type = CfprManagedObjectDn
_CfprStatsThr64DefinitionDn_Object = MibTableColumn
cfprStatsThr64DefinitionDn = _CfprStatsThr64DefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8, 1, 2),
    _CfprStatsThr64DefinitionDn_Type()
)
cfprStatsThr64DefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionDn.setStatus("current")
_CfprStatsThr64DefinitionRn_Type = SnmpAdminString
_CfprStatsThr64DefinitionRn_Object = MibTableColumn
cfprStatsThr64DefinitionRn = _CfprStatsThr64DefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8, 1, 3),
    _CfprStatsThr64DefinitionRn_Type()
)
cfprStatsThr64DefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionRn.setStatus("current")
_CfprStatsThr64DefinitionDescr_Type = SnmpAdminString
_CfprStatsThr64DefinitionDescr_Object = MibTableColumn
cfprStatsThr64DefinitionDescr = _CfprStatsThr64DefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8, 1, 4),
    _CfprStatsThr64DefinitionDescr_Type()
)
cfprStatsThr64DefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionDescr.setStatus("current")
_CfprStatsThr64DefinitionIntId_Type = SnmpAdminString
_CfprStatsThr64DefinitionIntId_Object = MibTableColumn
cfprStatsThr64DefinitionIntId = _CfprStatsThr64DefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8, 1, 5),
    _CfprStatsThr64DefinitionIntId_Type()
)
cfprStatsThr64DefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionIntId.setStatus("current")
_CfprStatsThr64DefinitionName_Type = SnmpAdminString
_CfprStatsThr64DefinitionName_Object = MibTableColumn
cfprStatsThr64DefinitionName = _CfprStatsThr64DefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8, 1, 6),
    _CfprStatsThr64DefinitionName_Type()
)
cfprStatsThr64DefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionName.setStatus("current")
_CfprStatsThr64DefinitionNormalValue_Type = Unsigned64
_CfprStatsThr64DefinitionNormalValue_Object = MibTableColumn
cfprStatsThr64DefinitionNormalValue = _CfprStatsThr64DefinitionNormalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8, 1, 7),
    _CfprStatsThr64DefinitionNormalValue_Type()
)
cfprStatsThr64DefinitionNormalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionNormalValue.setStatus("current")
_CfprStatsThr64DefinitionPolicyLevel_Type = Gauge32
_CfprStatsThr64DefinitionPolicyLevel_Object = MibTableColumn
cfprStatsThr64DefinitionPolicyLevel = _CfprStatsThr64DefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8, 1, 8),
    _CfprStatsThr64DefinitionPolicyLevel_Type()
)
cfprStatsThr64DefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionPolicyLevel.setStatus("current")
_CfprStatsThr64DefinitionPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStatsThr64DefinitionPolicyOwner_Object = MibTableColumn
cfprStatsThr64DefinitionPolicyOwner = _CfprStatsThr64DefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8, 1, 9),
    _CfprStatsThr64DefinitionPolicyOwner_Type()
)
cfprStatsThr64DefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionPolicyOwner.setStatus("current")
_CfprStatsThr64DefinitionPropId_Type = SnmpAdminString
_CfprStatsThr64DefinitionPropId_Object = MibTableColumn
cfprStatsThr64DefinitionPropId = _CfprStatsThr64DefinitionPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8, 1, 10),
    _CfprStatsThr64DefinitionPropId_Type()
)
cfprStatsThr64DefinitionPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionPropId.setStatus("current")
_CfprStatsThr64DefinitionPropType_Type = CfprStatsThr64DefinitionPropType
_CfprStatsThr64DefinitionPropType_Object = MibTableColumn
cfprStatsThr64DefinitionPropType = _CfprStatsThr64DefinitionPropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 8, 1, 11),
    _CfprStatsThr64DefinitionPropType_Type()
)
cfprStatsThr64DefinitionPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64DefinitionPropType.setStatus("current")
_CfprStatsThr64ValueTable_Object = MibTable
cfprStatsThr64ValueTable = _CfprStatsThr64ValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9)
)
if mibBuilder.loadTexts:
    cfprStatsThr64ValueTable.setStatus("current")
_CfprStatsThr64ValueEntry_Object = MibTableRow
cfprStatsThr64ValueEntry = _CfprStatsThr64ValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1)
)
cfprStatsThr64ValueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsThr64ValueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsThr64ValueEntry.setStatus("current")
_CfprStatsThr64ValueInstanceId_Type = CfprManagedObjectId
_CfprStatsThr64ValueInstanceId_Object = MibTableColumn
cfprStatsThr64ValueInstanceId = _CfprStatsThr64ValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 1),
    _CfprStatsThr64ValueInstanceId_Type()
)
cfprStatsThr64ValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsThr64ValueInstanceId.setStatus("current")
_CfprStatsThr64ValueDn_Type = CfprManagedObjectDn
_CfprStatsThr64ValueDn_Object = MibTableColumn
cfprStatsThr64ValueDn = _CfprStatsThr64ValueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 2),
    _CfprStatsThr64ValueDn_Type()
)
cfprStatsThr64ValueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64ValueDn.setStatus("current")
_CfprStatsThr64ValueRn_Type = SnmpAdminString
_CfprStatsThr64ValueRn_Object = MibTableColumn
cfprStatsThr64ValueRn = _CfprStatsThr64ValueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 3),
    _CfprStatsThr64ValueRn_Type()
)
cfprStatsThr64ValueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64ValueRn.setStatus("current")
_CfprStatsThr64ValueDeescalating_Type = Unsigned64
_CfprStatsThr64ValueDeescalating_Object = MibTableColumn
cfprStatsThr64ValueDeescalating = _CfprStatsThr64ValueDeescalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 4),
    _CfprStatsThr64ValueDeescalating_Type()
)
cfprStatsThr64ValueDeescalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64ValueDeescalating.setStatus("current")
_CfprStatsThr64ValueDescr_Type = SnmpAdminString
_CfprStatsThr64ValueDescr_Object = MibTableColumn
cfprStatsThr64ValueDescr = _CfprStatsThr64ValueDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 5),
    _CfprStatsThr64ValueDescr_Type()
)
cfprStatsThr64ValueDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64ValueDescr.setStatus("current")
_CfprStatsThr64ValueDirection_Type = CfprStatsThresholdDirection
_CfprStatsThr64ValueDirection_Object = MibTableColumn
cfprStatsThr64ValueDirection = _CfprStatsThr64ValueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 6),
    _CfprStatsThr64ValueDirection_Type()
)
cfprStatsThr64ValueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64ValueDirection.setStatus("current")
_CfprStatsThr64ValueEscalating_Type = Unsigned64
_CfprStatsThr64ValueEscalating_Object = MibTableColumn
cfprStatsThr64ValueEscalating = _CfprStatsThr64ValueEscalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 7),
    _CfprStatsThr64ValueEscalating_Type()
)
cfprStatsThr64ValueEscalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64ValueEscalating.setStatus("current")
_CfprStatsThr64ValueIntId_Type = SnmpAdminString
_CfprStatsThr64ValueIntId_Object = MibTableColumn
cfprStatsThr64ValueIntId = _CfprStatsThr64ValueIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 8),
    _CfprStatsThr64ValueIntId_Type()
)
cfprStatsThr64ValueIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64ValueIntId.setStatus("current")
_CfprStatsThr64ValueName_Type = SnmpAdminString
_CfprStatsThr64ValueName_Object = MibTableColumn
cfprStatsThr64ValueName = _CfprStatsThr64ValueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 9),
    _CfprStatsThr64ValueName_Type()
)
cfprStatsThr64ValueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64ValueName.setStatus("current")
_CfprStatsThr64ValuePolicyLevel_Type = Gauge32
_CfprStatsThr64ValuePolicyLevel_Object = MibTableColumn
cfprStatsThr64ValuePolicyLevel = _CfprStatsThr64ValuePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 10),
    _CfprStatsThr64ValuePolicyLevel_Type()
)
cfprStatsThr64ValuePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64ValuePolicyLevel.setStatus("current")
_CfprStatsThr64ValuePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStatsThr64ValuePolicyOwner_Object = MibTableColumn
cfprStatsThr64ValuePolicyOwner = _CfprStatsThr64ValuePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 11),
    _CfprStatsThr64ValuePolicyOwner_Type()
)
cfprStatsThr64ValuePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64ValuePolicyOwner.setStatus("current")
_CfprStatsThr64ValuePropType_Type = CfprStatsThr64ValuePropType
_CfprStatsThr64ValuePropType_Object = MibTableColumn
cfprStatsThr64ValuePropType = _CfprStatsThr64ValuePropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 12),
    _CfprStatsThr64ValuePropType_Type()
)
cfprStatsThr64ValuePropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64ValuePropType.setStatus("current")
_CfprStatsThr64ValueSeverity_Type = CfprConditionSeverity
_CfprStatsThr64ValueSeverity_Object = MibTableColumn
cfprStatsThr64ValueSeverity = _CfprStatsThr64ValueSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 9, 1, 13),
    _CfprStatsThr64ValueSeverity_Type()
)
cfprStatsThr64ValueSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThr64ValueSeverity.setStatus("current")
_CfprStatsThrFloatDefinitionTable_Object = MibTable
cfprStatsThrFloatDefinitionTable = _CfprStatsThrFloatDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10)
)
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionTable.setStatus("current")
_CfprStatsThrFloatDefinitionEntry_Object = MibTableRow
cfprStatsThrFloatDefinitionEntry = _CfprStatsThrFloatDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10, 1)
)
cfprStatsThrFloatDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsThrFloatDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionEntry.setStatus("current")
_CfprStatsThrFloatDefinitionInstanceId_Type = CfprManagedObjectId
_CfprStatsThrFloatDefinitionInstanceId_Object = MibTableColumn
cfprStatsThrFloatDefinitionInstanceId = _CfprStatsThrFloatDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10, 1, 1),
    _CfprStatsThrFloatDefinitionInstanceId_Type()
)
cfprStatsThrFloatDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionInstanceId.setStatus("current")
_CfprStatsThrFloatDefinitionDn_Type = CfprManagedObjectDn
_CfprStatsThrFloatDefinitionDn_Object = MibTableColumn
cfprStatsThrFloatDefinitionDn = _CfprStatsThrFloatDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10, 1, 2),
    _CfprStatsThrFloatDefinitionDn_Type()
)
cfprStatsThrFloatDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionDn.setStatus("current")
_CfprStatsThrFloatDefinitionRn_Type = SnmpAdminString
_CfprStatsThrFloatDefinitionRn_Object = MibTableColumn
cfprStatsThrFloatDefinitionRn = _CfprStatsThrFloatDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10, 1, 3),
    _CfprStatsThrFloatDefinitionRn_Type()
)
cfprStatsThrFloatDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionRn.setStatus("current")
_CfprStatsThrFloatDefinitionDescr_Type = SnmpAdminString
_CfprStatsThrFloatDefinitionDescr_Object = MibTableColumn
cfprStatsThrFloatDefinitionDescr = _CfprStatsThrFloatDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10, 1, 4),
    _CfprStatsThrFloatDefinitionDescr_Type()
)
cfprStatsThrFloatDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionDescr.setStatus("current")
_CfprStatsThrFloatDefinitionIntId_Type = SnmpAdminString
_CfprStatsThrFloatDefinitionIntId_Object = MibTableColumn
cfprStatsThrFloatDefinitionIntId = _CfprStatsThrFloatDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10, 1, 5),
    _CfprStatsThrFloatDefinitionIntId_Type()
)
cfprStatsThrFloatDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionIntId.setStatus("current")
_CfprStatsThrFloatDefinitionName_Type = SnmpAdminString
_CfprStatsThrFloatDefinitionName_Object = MibTableColumn
cfprStatsThrFloatDefinitionName = _CfprStatsThrFloatDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10, 1, 6),
    _CfprStatsThrFloatDefinitionName_Type()
)
cfprStatsThrFloatDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionName.setStatus("current")
_CfprStatsThrFloatDefinitionNormalValue_Type = Integer32
_CfprStatsThrFloatDefinitionNormalValue_Object = MibTableColumn
cfprStatsThrFloatDefinitionNormalValue = _CfprStatsThrFloatDefinitionNormalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10, 1, 7),
    _CfprStatsThrFloatDefinitionNormalValue_Type()
)
cfprStatsThrFloatDefinitionNormalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionNormalValue.setStatus("current")
_CfprStatsThrFloatDefinitionPolicyLevel_Type = Gauge32
_CfprStatsThrFloatDefinitionPolicyLevel_Object = MibTableColumn
cfprStatsThrFloatDefinitionPolicyLevel = _CfprStatsThrFloatDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10, 1, 8),
    _CfprStatsThrFloatDefinitionPolicyLevel_Type()
)
cfprStatsThrFloatDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionPolicyLevel.setStatus("current")
_CfprStatsThrFloatDefinitionPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStatsThrFloatDefinitionPolicyOwner_Object = MibTableColumn
cfprStatsThrFloatDefinitionPolicyOwner = _CfprStatsThrFloatDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10, 1, 9),
    _CfprStatsThrFloatDefinitionPolicyOwner_Type()
)
cfprStatsThrFloatDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionPolicyOwner.setStatus("current")
_CfprStatsThrFloatDefinitionPropId_Type = SnmpAdminString
_CfprStatsThrFloatDefinitionPropId_Object = MibTableColumn
cfprStatsThrFloatDefinitionPropId = _CfprStatsThrFloatDefinitionPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10, 1, 10),
    _CfprStatsThrFloatDefinitionPropId_Type()
)
cfprStatsThrFloatDefinitionPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionPropId.setStatus("current")
_CfprStatsThrFloatDefinitionPropType_Type = CfprStatsThrFloatDefinitionPropType
_CfprStatsThrFloatDefinitionPropType_Object = MibTableColumn
cfprStatsThrFloatDefinitionPropType = _CfprStatsThrFloatDefinitionPropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 10, 1, 11),
    _CfprStatsThrFloatDefinitionPropType_Type()
)
cfprStatsThrFloatDefinitionPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatDefinitionPropType.setStatus("current")
_CfprStatsThrFloatValueTable_Object = MibTable
cfprStatsThrFloatValueTable = _CfprStatsThrFloatValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11)
)
if mibBuilder.loadTexts:
    cfprStatsThrFloatValueTable.setStatus("current")
_CfprStatsThrFloatValueEntry_Object = MibTableRow
cfprStatsThrFloatValueEntry = _CfprStatsThrFloatValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1)
)
cfprStatsThrFloatValueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsThrFloatValueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsThrFloatValueEntry.setStatus("current")
_CfprStatsThrFloatValueInstanceId_Type = CfprManagedObjectId
_CfprStatsThrFloatValueInstanceId_Object = MibTableColumn
cfprStatsThrFloatValueInstanceId = _CfprStatsThrFloatValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 1),
    _CfprStatsThrFloatValueInstanceId_Type()
)
cfprStatsThrFloatValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValueInstanceId.setStatus("current")
_CfprStatsThrFloatValueDn_Type = CfprManagedObjectDn
_CfprStatsThrFloatValueDn_Object = MibTableColumn
cfprStatsThrFloatValueDn = _CfprStatsThrFloatValueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 2),
    _CfprStatsThrFloatValueDn_Type()
)
cfprStatsThrFloatValueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValueDn.setStatus("current")
_CfprStatsThrFloatValueRn_Type = SnmpAdminString
_CfprStatsThrFloatValueRn_Object = MibTableColumn
cfprStatsThrFloatValueRn = _CfprStatsThrFloatValueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 3),
    _CfprStatsThrFloatValueRn_Type()
)
cfprStatsThrFloatValueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValueRn.setStatus("current")
_CfprStatsThrFloatValueDeescalating_Type = Integer32
_CfprStatsThrFloatValueDeescalating_Object = MibTableColumn
cfprStatsThrFloatValueDeescalating = _CfprStatsThrFloatValueDeescalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 4),
    _CfprStatsThrFloatValueDeescalating_Type()
)
cfprStatsThrFloatValueDeescalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValueDeescalating.setStatus("current")
_CfprStatsThrFloatValueDescr_Type = SnmpAdminString
_CfprStatsThrFloatValueDescr_Object = MibTableColumn
cfprStatsThrFloatValueDescr = _CfprStatsThrFloatValueDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 5),
    _CfprStatsThrFloatValueDescr_Type()
)
cfprStatsThrFloatValueDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValueDescr.setStatus("current")
_CfprStatsThrFloatValueDirection_Type = CfprStatsThresholdDirection
_CfprStatsThrFloatValueDirection_Object = MibTableColumn
cfprStatsThrFloatValueDirection = _CfprStatsThrFloatValueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 6),
    _CfprStatsThrFloatValueDirection_Type()
)
cfprStatsThrFloatValueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValueDirection.setStatus("current")
_CfprStatsThrFloatValueEscalating_Type = Integer32
_CfprStatsThrFloatValueEscalating_Object = MibTableColumn
cfprStatsThrFloatValueEscalating = _CfprStatsThrFloatValueEscalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 7),
    _CfprStatsThrFloatValueEscalating_Type()
)
cfprStatsThrFloatValueEscalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValueEscalating.setStatus("current")
_CfprStatsThrFloatValueIntId_Type = SnmpAdminString
_CfprStatsThrFloatValueIntId_Object = MibTableColumn
cfprStatsThrFloatValueIntId = _CfprStatsThrFloatValueIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 8),
    _CfprStatsThrFloatValueIntId_Type()
)
cfprStatsThrFloatValueIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValueIntId.setStatus("current")
_CfprStatsThrFloatValueName_Type = SnmpAdminString
_CfprStatsThrFloatValueName_Object = MibTableColumn
cfprStatsThrFloatValueName = _CfprStatsThrFloatValueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 9),
    _CfprStatsThrFloatValueName_Type()
)
cfprStatsThrFloatValueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValueName.setStatus("current")
_CfprStatsThrFloatValuePolicyLevel_Type = Gauge32
_CfprStatsThrFloatValuePolicyLevel_Object = MibTableColumn
cfprStatsThrFloatValuePolicyLevel = _CfprStatsThrFloatValuePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 10),
    _CfprStatsThrFloatValuePolicyLevel_Type()
)
cfprStatsThrFloatValuePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValuePolicyLevel.setStatus("current")
_CfprStatsThrFloatValuePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStatsThrFloatValuePolicyOwner_Object = MibTableColumn
cfprStatsThrFloatValuePolicyOwner = _CfprStatsThrFloatValuePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 11),
    _CfprStatsThrFloatValuePolicyOwner_Type()
)
cfprStatsThrFloatValuePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValuePolicyOwner.setStatus("current")
_CfprStatsThrFloatValuePropType_Type = CfprStatsThrFloatValuePropType
_CfprStatsThrFloatValuePropType_Object = MibTableColumn
cfprStatsThrFloatValuePropType = _CfprStatsThrFloatValuePropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 12),
    _CfprStatsThrFloatValuePropType_Type()
)
cfprStatsThrFloatValuePropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValuePropType.setStatus("current")
_CfprStatsThrFloatValueSeverity_Type = CfprConditionSeverity
_CfprStatsThrFloatValueSeverity_Object = MibTableColumn
cfprStatsThrFloatValueSeverity = _CfprStatsThrFloatValueSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 11, 1, 13),
    _CfprStatsThrFloatValueSeverity_Type()
)
cfprStatsThrFloatValueSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThrFloatValueSeverity.setStatus("current")
_CfprStatsThresholdClassTable_Object = MibTable
cfprStatsThresholdClassTable = _CfprStatsThresholdClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 12)
)
if mibBuilder.loadTexts:
    cfprStatsThresholdClassTable.setStatus("current")
_CfprStatsThresholdClassEntry_Object = MibTableRow
cfprStatsThresholdClassEntry = _CfprStatsThresholdClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 12, 1)
)
cfprStatsThresholdClassEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsThresholdClassInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsThresholdClassEntry.setStatus("current")
_CfprStatsThresholdClassInstanceId_Type = CfprManagedObjectId
_CfprStatsThresholdClassInstanceId_Object = MibTableColumn
cfprStatsThresholdClassInstanceId = _CfprStatsThresholdClassInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 12, 1, 1),
    _CfprStatsThresholdClassInstanceId_Type()
)
cfprStatsThresholdClassInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsThresholdClassInstanceId.setStatus("current")
_CfprStatsThresholdClassDn_Type = CfprManagedObjectDn
_CfprStatsThresholdClassDn_Object = MibTableColumn
cfprStatsThresholdClassDn = _CfprStatsThresholdClassDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 12, 1, 2),
    _CfprStatsThresholdClassDn_Type()
)
cfprStatsThresholdClassDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdClassDn.setStatus("current")
_CfprStatsThresholdClassRn_Type = SnmpAdminString
_CfprStatsThresholdClassRn_Object = MibTableColumn
cfprStatsThresholdClassRn = _CfprStatsThresholdClassRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 12, 1, 3),
    _CfprStatsThresholdClassRn_Type()
)
cfprStatsThresholdClassRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdClassRn.setStatus("current")
_CfprStatsThresholdClassDescr_Type = SnmpAdminString
_CfprStatsThresholdClassDescr_Object = MibTableColumn
cfprStatsThresholdClassDescr = _CfprStatsThresholdClassDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 12, 1, 4),
    _CfprStatsThresholdClassDescr_Type()
)
cfprStatsThresholdClassDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdClassDescr.setStatus("current")
_CfprStatsThresholdClassIntId_Type = SnmpAdminString
_CfprStatsThresholdClassIntId_Object = MibTableColumn
cfprStatsThresholdClassIntId = _CfprStatsThresholdClassIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 12, 1, 5),
    _CfprStatsThresholdClassIntId_Type()
)
cfprStatsThresholdClassIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdClassIntId.setStatus("current")
_CfprStatsThresholdClassName_Type = SnmpAdminString
_CfprStatsThresholdClassName_Object = MibTableColumn
cfprStatsThresholdClassName = _CfprStatsThresholdClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 12, 1, 6),
    _CfprStatsThresholdClassName_Type()
)
cfprStatsThresholdClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdClassName.setStatus("current")
_CfprStatsThresholdClassPolicyLevel_Type = Gauge32
_CfprStatsThresholdClassPolicyLevel_Object = MibTableColumn
cfprStatsThresholdClassPolicyLevel = _CfprStatsThresholdClassPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 12, 1, 7),
    _CfprStatsThresholdClassPolicyLevel_Type()
)
cfprStatsThresholdClassPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdClassPolicyLevel.setStatus("current")
_CfprStatsThresholdClassPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStatsThresholdClassPolicyOwner_Object = MibTableColumn
cfprStatsThresholdClassPolicyOwner = _CfprStatsThresholdClassPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 12, 1, 8),
    _CfprStatsThresholdClassPolicyOwner_Type()
)
cfprStatsThresholdClassPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdClassPolicyOwner.setStatus("current")
_CfprStatsThresholdClassStatsClassId_Type = SnmpAdminString
_CfprStatsThresholdClassStatsClassId_Object = MibTableColumn
cfprStatsThresholdClassStatsClassId = _CfprStatsThresholdClassStatsClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 12, 1, 9),
    _CfprStatsThresholdClassStatsClassId_Type()
)
cfprStatsThresholdClassStatsClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdClassStatsClassId.setStatus("current")
_CfprStatsThresholdPolicyTable_Object = MibTable
cfprStatsThresholdPolicyTable = _CfprStatsThresholdPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 13)
)
if mibBuilder.loadTexts:
    cfprStatsThresholdPolicyTable.setStatus("current")
_CfprStatsThresholdPolicyEntry_Object = MibTableRow
cfprStatsThresholdPolicyEntry = _CfprStatsThresholdPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 13, 1)
)
cfprStatsThresholdPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-STATS-MIB", "cfprStatsThresholdPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprStatsThresholdPolicyEntry.setStatus("current")
_CfprStatsThresholdPolicyInstanceId_Type = CfprManagedObjectId
_CfprStatsThresholdPolicyInstanceId_Object = MibTableColumn
cfprStatsThresholdPolicyInstanceId = _CfprStatsThresholdPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 13, 1, 1),
    _CfprStatsThresholdPolicyInstanceId_Type()
)
cfprStatsThresholdPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprStatsThresholdPolicyInstanceId.setStatus("current")
_CfprStatsThresholdPolicyDn_Type = CfprManagedObjectDn
_CfprStatsThresholdPolicyDn_Object = MibTableColumn
cfprStatsThresholdPolicyDn = _CfprStatsThresholdPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 13, 1, 2),
    _CfprStatsThresholdPolicyDn_Type()
)
cfprStatsThresholdPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdPolicyDn.setStatus("current")
_CfprStatsThresholdPolicyRn_Type = SnmpAdminString
_CfprStatsThresholdPolicyRn_Object = MibTableColumn
cfprStatsThresholdPolicyRn = _CfprStatsThresholdPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 13, 1, 3),
    _CfprStatsThresholdPolicyRn_Type()
)
cfprStatsThresholdPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdPolicyRn.setStatus("current")
_CfprStatsThresholdPolicyDescr_Type = SnmpAdminString
_CfprStatsThresholdPolicyDescr_Object = MibTableColumn
cfprStatsThresholdPolicyDescr = _CfprStatsThresholdPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 13, 1, 4),
    _CfprStatsThresholdPolicyDescr_Type()
)
cfprStatsThresholdPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdPolicyDescr.setStatus("current")
_CfprStatsThresholdPolicyIntId_Type = SnmpAdminString
_CfprStatsThresholdPolicyIntId_Object = MibTableColumn
cfprStatsThresholdPolicyIntId = _CfprStatsThresholdPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 13, 1, 5),
    _CfprStatsThresholdPolicyIntId_Type()
)
cfprStatsThresholdPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdPolicyIntId.setStatus("current")
_CfprStatsThresholdPolicyName_Type = SnmpAdminString
_CfprStatsThresholdPolicyName_Object = MibTableColumn
cfprStatsThresholdPolicyName = _CfprStatsThresholdPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 13, 1, 6),
    _CfprStatsThresholdPolicyName_Type()
)
cfprStatsThresholdPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdPolicyName.setStatus("current")
_CfprStatsThresholdPolicyPolicyLevel_Type = Gauge32
_CfprStatsThresholdPolicyPolicyLevel_Object = MibTableColumn
cfprStatsThresholdPolicyPolicyLevel = _CfprStatsThresholdPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 13, 1, 7),
    _CfprStatsThresholdPolicyPolicyLevel_Type()
)
cfprStatsThresholdPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdPolicyPolicyLevel.setStatus("current")
_CfprStatsThresholdPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprStatsThresholdPolicyPolicyOwner_Object = MibTableColumn
cfprStatsThresholdPolicyPolicyOwner = _CfprStatsThresholdPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 73, 13, 1, 8),
    _CfprStatsThresholdPolicyPolicyOwner_Type()
)
cfprStatsThresholdPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprStatsThresholdPolicyPolicyOwner.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-STATS-MIB",
    **{"cfprStatsObjects": cfprStatsObjects,
       "cfprStatsCollectionPolicyTable": cfprStatsCollectionPolicyTable,
       "cfprStatsCollectionPolicyEntry": cfprStatsCollectionPolicyEntry,
       "cfprStatsCollectionPolicyInstanceId": cfprStatsCollectionPolicyInstanceId,
       "cfprStatsCollectionPolicyDn": cfprStatsCollectionPolicyDn,
       "cfprStatsCollectionPolicyRn": cfprStatsCollectionPolicyRn,
       "cfprStatsCollectionPolicyCollectionInterval": cfprStatsCollectionPolicyCollectionInterval,
       "cfprStatsCollectionPolicyFsmDescr": cfprStatsCollectionPolicyFsmDescr,
       "cfprStatsCollectionPolicyFsmPrev": cfprStatsCollectionPolicyFsmPrev,
       "cfprStatsCollectionPolicyFsmProgr": cfprStatsCollectionPolicyFsmProgr,
       "cfprStatsCollectionPolicyFsmRmtInvErrCode": cfprStatsCollectionPolicyFsmRmtInvErrCode,
       "cfprStatsCollectionPolicyFsmRmtInvErrDescr": cfprStatsCollectionPolicyFsmRmtInvErrDescr,
       "cfprStatsCollectionPolicyFsmRmtInvRslt": cfprStatsCollectionPolicyFsmRmtInvRslt,
       "cfprStatsCollectionPolicyFsmStageDescr": cfprStatsCollectionPolicyFsmStageDescr,
       "cfprStatsCollectionPolicyFsmStamp": cfprStatsCollectionPolicyFsmStamp,
       "cfprStatsCollectionPolicyFsmStatus": cfprStatsCollectionPolicyFsmStatus,
       "cfprStatsCollectionPolicyFsmTry": cfprStatsCollectionPolicyFsmTry,
       "cfprStatsCollectionPolicyId": cfprStatsCollectionPolicyId,
       "cfprStatsCollectionPolicyName": cfprStatsCollectionPolicyName,
       "cfprStatsCollectionPolicyReportingInterval": cfprStatsCollectionPolicyReportingInterval,
       "cfprStatsCollectionPolicyFsmTable": cfprStatsCollectionPolicyFsmTable,
       "cfprStatsCollectionPolicyFsmEntry": cfprStatsCollectionPolicyFsmEntry,
       "cfprStatsCollectionPolicyFsmInstanceId": cfprStatsCollectionPolicyFsmInstanceId,
       "cfprStatsCollectionPolicyFsmDn": cfprStatsCollectionPolicyFsmDn,
       "cfprStatsCollectionPolicyFsmRn": cfprStatsCollectionPolicyFsmRn,
       "cfprStatsCollectionPolicyFsmCompletionTime": cfprStatsCollectionPolicyFsmCompletionTime,
       "cfprStatsCollectionPolicyFsmCurrentFsm": cfprStatsCollectionPolicyFsmCurrentFsm,
       "cfprStatsCollectionPolicyFsmDescrData": cfprStatsCollectionPolicyFsmDescrData,
       "cfprStatsCollectionPolicyFsmFsmStatus": cfprStatsCollectionPolicyFsmFsmStatus,
       "cfprStatsCollectionPolicyFsmProgress": cfprStatsCollectionPolicyFsmProgress,
       "cfprStatsCollectionPolicyFsmRmtErrCode": cfprStatsCollectionPolicyFsmRmtErrCode,
       "cfprStatsCollectionPolicyFsmRmtErrDescr": cfprStatsCollectionPolicyFsmRmtErrDescr,
       "cfprStatsCollectionPolicyFsmRmtRslt": cfprStatsCollectionPolicyFsmRmtRslt,
       "cfprStatsCollectionPolicyFsmStageTable": cfprStatsCollectionPolicyFsmStageTable,
       "cfprStatsCollectionPolicyFsmStageEntry": cfprStatsCollectionPolicyFsmStageEntry,
       "cfprStatsCollectionPolicyFsmStageInstanceId": cfprStatsCollectionPolicyFsmStageInstanceId,
       "cfprStatsCollectionPolicyFsmStageDn": cfprStatsCollectionPolicyFsmStageDn,
       "cfprStatsCollectionPolicyFsmStageRn": cfprStatsCollectionPolicyFsmStageRn,
       "cfprStatsCollectionPolicyFsmStageDescrData": cfprStatsCollectionPolicyFsmStageDescrData,
       "cfprStatsCollectionPolicyFsmStageLastUpdateTime": cfprStatsCollectionPolicyFsmStageLastUpdateTime,
       "cfprStatsCollectionPolicyFsmStageName": cfprStatsCollectionPolicyFsmStageName,
       "cfprStatsCollectionPolicyFsmStageOrder": cfprStatsCollectionPolicyFsmStageOrder,
       "cfprStatsCollectionPolicyFsmStageRetry": cfprStatsCollectionPolicyFsmStageRetry,
       "cfprStatsCollectionPolicyFsmStageStageStatus": cfprStatsCollectionPolicyFsmStageStageStatus,
       "cfprStatsCollectionPolicyFsmTaskTable": cfprStatsCollectionPolicyFsmTaskTable,
       "cfprStatsCollectionPolicyFsmTaskEntry": cfprStatsCollectionPolicyFsmTaskEntry,
       "cfprStatsCollectionPolicyFsmTaskInstanceId": cfprStatsCollectionPolicyFsmTaskInstanceId,
       "cfprStatsCollectionPolicyFsmTaskDn": cfprStatsCollectionPolicyFsmTaskDn,
       "cfprStatsCollectionPolicyFsmTaskRn": cfprStatsCollectionPolicyFsmTaskRn,
       "cfprStatsCollectionPolicyFsmTaskCompletion": cfprStatsCollectionPolicyFsmTaskCompletion,
       "cfprStatsCollectionPolicyFsmTaskFlags": cfprStatsCollectionPolicyFsmTaskFlags,
       "cfprStatsCollectionPolicyFsmTaskItem": cfprStatsCollectionPolicyFsmTaskItem,
       "cfprStatsCollectionPolicyFsmTaskSeqId": cfprStatsCollectionPolicyFsmTaskSeqId,
       "cfprStatsHolderTable": cfprStatsHolderTable,
       "cfprStatsHolderEntry": cfprStatsHolderEntry,
       "cfprStatsHolderInstanceId": cfprStatsHolderInstanceId,
       "cfprStatsHolderDn": cfprStatsHolderDn,
       "cfprStatsHolderRn": cfprStatsHolderRn,
       "cfprStatsHolderName": cfprStatsHolderName,
       "cfprStatsThr32DefinitionTable": cfprStatsThr32DefinitionTable,
       "cfprStatsThr32DefinitionEntry": cfprStatsThr32DefinitionEntry,
       "cfprStatsThr32DefinitionInstanceId": cfprStatsThr32DefinitionInstanceId,
       "cfprStatsThr32DefinitionDn": cfprStatsThr32DefinitionDn,
       "cfprStatsThr32DefinitionRn": cfprStatsThr32DefinitionRn,
       "cfprStatsThr32DefinitionDescr": cfprStatsThr32DefinitionDescr,
       "cfprStatsThr32DefinitionIntId": cfprStatsThr32DefinitionIntId,
       "cfprStatsThr32DefinitionName": cfprStatsThr32DefinitionName,
       "cfprStatsThr32DefinitionNormalValue": cfprStatsThr32DefinitionNormalValue,
       "cfprStatsThr32DefinitionPolicyLevel": cfprStatsThr32DefinitionPolicyLevel,
       "cfprStatsThr32DefinitionPolicyOwner": cfprStatsThr32DefinitionPolicyOwner,
       "cfprStatsThr32DefinitionPropId": cfprStatsThr32DefinitionPropId,
       "cfprStatsThr32DefinitionPropType": cfprStatsThr32DefinitionPropType,
       "cfprStatsThr32ValueTable": cfprStatsThr32ValueTable,
       "cfprStatsThr32ValueEntry": cfprStatsThr32ValueEntry,
       "cfprStatsThr32ValueInstanceId": cfprStatsThr32ValueInstanceId,
       "cfprStatsThr32ValueDn": cfprStatsThr32ValueDn,
       "cfprStatsThr32ValueRn": cfprStatsThr32ValueRn,
       "cfprStatsThr32ValueDeescalating": cfprStatsThr32ValueDeescalating,
       "cfprStatsThr32ValueDescr": cfprStatsThr32ValueDescr,
       "cfprStatsThr32ValueDirection": cfprStatsThr32ValueDirection,
       "cfprStatsThr32ValueEscalating": cfprStatsThr32ValueEscalating,
       "cfprStatsThr32ValueIntId": cfprStatsThr32ValueIntId,
       "cfprStatsThr32ValueName": cfprStatsThr32ValueName,
       "cfprStatsThr32ValuePolicyLevel": cfprStatsThr32ValuePolicyLevel,
       "cfprStatsThr32ValuePolicyOwner": cfprStatsThr32ValuePolicyOwner,
       "cfprStatsThr32ValuePropType": cfprStatsThr32ValuePropType,
       "cfprStatsThr32ValueSeverity": cfprStatsThr32ValueSeverity,
       "cfprStatsThr64DefinitionTable": cfprStatsThr64DefinitionTable,
       "cfprStatsThr64DefinitionEntry": cfprStatsThr64DefinitionEntry,
       "cfprStatsThr64DefinitionInstanceId": cfprStatsThr64DefinitionInstanceId,
       "cfprStatsThr64DefinitionDn": cfprStatsThr64DefinitionDn,
       "cfprStatsThr64DefinitionRn": cfprStatsThr64DefinitionRn,
       "cfprStatsThr64DefinitionDescr": cfprStatsThr64DefinitionDescr,
       "cfprStatsThr64DefinitionIntId": cfprStatsThr64DefinitionIntId,
       "cfprStatsThr64DefinitionName": cfprStatsThr64DefinitionName,
       "cfprStatsThr64DefinitionNormalValue": cfprStatsThr64DefinitionNormalValue,
       "cfprStatsThr64DefinitionPolicyLevel": cfprStatsThr64DefinitionPolicyLevel,
       "cfprStatsThr64DefinitionPolicyOwner": cfprStatsThr64DefinitionPolicyOwner,
       "cfprStatsThr64DefinitionPropId": cfprStatsThr64DefinitionPropId,
       "cfprStatsThr64DefinitionPropType": cfprStatsThr64DefinitionPropType,
       "cfprStatsThr64ValueTable": cfprStatsThr64ValueTable,
       "cfprStatsThr64ValueEntry": cfprStatsThr64ValueEntry,
       "cfprStatsThr64ValueInstanceId": cfprStatsThr64ValueInstanceId,
       "cfprStatsThr64ValueDn": cfprStatsThr64ValueDn,
       "cfprStatsThr64ValueRn": cfprStatsThr64ValueRn,
       "cfprStatsThr64ValueDeescalating": cfprStatsThr64ValueDeescalating,
       "cfprStatsThr64ValueDescr": cfprStatsThr64ValueDescr,
       "cfprStatsThr64ValueDirection": cfprStatsThr64ValueDirection,
       "cfprStatsThr64ValueEscalating": cfprStatsThr64ValueEscalating,
       "cfprStatsThr64ValueIntId": cfprStatsThr64ValueIntId,
       "cfprStatsThr64ValueName": cfprStatsThr64ValueName,
       "cfprStatsThr64ValuePolicyLevel": cfprStatsThr64ValuePolicyLevel,
       "cfprStatsThr64ValuePolicyOwner": cfprStatsThr64ValuePolicyOwner,
       "cfprStatsThr64ValuePropType": cfprStatsThr64ValuePropType,
       "cfprStatsThr64ValueSeverity": cfprStatsThr64ValueSeverity,
       "cfprStatsThrFloatDefinitionTable": cfprStatsThrFloatDefinitionTable,
       "cfprStatsThrFloatDefinitionEntry": cfprStatsThrFloatDefinitionEntry,
       "cfprStatsThrFloatDefinitionInstanceId": cfprStatsThrFloatDefinitionInstanceId,
       "cfprStatsThrFloatDefinitionDn": cfprStatsThrFloatDefinitionDn,
       "cfprStatsThrFloatDefinitionRn": cfprStatsThrFloatDefinitionRn,
       "cfprStatsThrFloatDefinitionDescr": cfprStatsThrFloatDefinitionDescr,
       "cfprStatsThrFloatDefinitionIntId": cfprStatsThrFloatDefinitionIntId,
       "cfprStatsThrFloatDefinitionName": cfprStatsThrFloatDefinitionName,
       "cfprStatsThrFloatDefinitionNormalValue": cfprStatsThrFloatDefinitionNormalValue,
       "cfprStatsThrFloatDefinitionPolicyLevel": cfprStatsThrFloatDefinitionPolicyLevel,
       "cfprStatsThrFloatDefinitionPolicyOwner": cfprStatsThrFloatDefinitionPolicyOwner,
       "cfprStatsThrFloatDefinitionPropId": cfprStatsThrFloatDefinitionPropId,
       "cfprStatsThrFloatDefinitionPropType": cfprStatsThrFloatDefinitionPropType,
       "cfprStatsThrFloatValueTable": cfprStatsThrFloatValueTable,
       "cfprStatsThrFloatValueEntry": cfprStatsThrFloatValueEntry,
       "cfprStatsThrFloatValueInstanceId": cfprStatsThrFloatValueInstanceId,
       "cfprStatsThrFloatValueDn": cfprStatsThrFloatValueDn,
       "cfprStatsThrFloatValueRn": cfprStatsThrFloatValueRn,
       "cfprStatsThrFloatValueDeescalating": cfprStatsThrFloatValueDeescalating,
       "cfprStatsThrFloatValueDescr": cfprStatsThrFloatValueDescr,
       "cfprStatsThrFloatValueDirection": cfprStatsThrFloatValueDirection,
       "cfprStatsThrFloatValueEscalating": cfprStatsThrFloatValueEscalating,
       "cfprStatsThrFloatValueIntId": cfprStatsThrFloatValueIntId,
       "cfprStatsThrFloatValueName": cfprStatsThrFloatValueName,
       "cfprStatsThrFloatValuePolicyLevel": cfprStatsThrFloatValuePolicyLevel,
       "cfprStatsThrFloatValuePolicyOwner": cfprStatsThrFloatValuePolicyOwner,
       "cfprStatsThrFloatValuePropType": cfprStatsThrFloatValuePropType,
       "cfprStatsThrFloatValueSeverity": cfprStatsThrFloatValueSeverity,
       "cfprStatsThresholdClassTable": cfprStatsThresholdClassTable,
       "cfprStatsThresholdClassEntry": cfprStatsThresholdClassEntry,
       "cfprStatsThresholdClassInstanceId": cfprStatsThresholdClassInstanceId,
       "cfprStatsThresholdClassDn": cfprStatsThresholdClassDn,
       "cfprStatsThresholdClassRn": cfprStatsThresholdClassRn,
       "cfprStatsThresholdClassDescr": cfprStatsThresholdClassDescr,
       "cfprStatsThresholdClassIntId": cfprStatsThresholdClassIntId,
       "cfprStatsThresholdClassName": cfprStatsThresholdClassName,
       "cfprStatsThresholdClassPolicyLevel": cfprStatsThresholdClassPolicyLevel,
       "cfprStatsThresholdClassPolicyOwner": cfprStatsThresholdClassPolicyOwner,
       "cfprStatsThresholdClassStatsClassId": cfprStatsThresholdClassStatsClassId,
       "cfprStatsThresholdPolicyTable": cfprStatsThresholdPolicyTable,
       "cfprStatsThresholdPolicyEntry": cfprStatsThresholdPolicyEntry,
       "cfprStatsThresholdPolicyInstanceId": cfprStatsThresholdPolicyInstanceId,
       "cfprStatsThresholdPolicyDn": cfprStatsThresholdPolicyDn,
       "cfprStatsThresholdPolicyRn": cfprStatsThresholdPolicyRn,
       "cfprStatsThresholdPolicyDescr": cfprStatsThresholdPolicyDescr,
       "cfprStatsThresholdPolicyIntId": cfprStatsThresholdPolicyIntId,
       "cfprStatsThresholdPolicyName": cfprStatsThresholdPolicyName,
       "cfprStatsThresholdPolicyPolicyLevel": cfprStatsThresholdPolicyPolicyLevel,
       "cfprStatsThresholdPolicyPolicyOwner": cfprStatsThresholdPolicyPolicyOwner}
)
