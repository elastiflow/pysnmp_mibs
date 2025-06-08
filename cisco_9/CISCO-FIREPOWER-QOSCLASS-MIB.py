# SNMP MIB module (CISCO-FIREPOWER-QOSCLASS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-QOSCLASS-MIB.mib
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
 CfprPolicyPolicyOwner,
 CfprQosclassDefinitionFsmCurrentFsm,
 CfprQosclassDefinitionFsmStageName,
 CfprQosclassDefinitionFsmTaskItem,
 CfprQosclassEthBEAdminState,
 CfprQosclassEthBEDrop,
 CfprQosclassEthBEPriority,
 CfprQosclassEthClassifiedAdminState,
 CfprQosclassEthClassifiedDrop,
 CfprQosclassEthClassifiedPriority,
 CfprQosclassFcAdminState,
 CfprQosclassFcDrop,
 CfprQosclassFcPriority) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprPolicyPolicyOwner",
    "CfprQosclassDefinitionFsmCurrentFsm",
    "CfprQosclassDefinitionFsmStageName",
    "CfprQosclassDefinitionFsmTaskItem",
    "CfprQosclassEthBEAdminState",
    "CfprQosclassEthBEDrop",
    "CfprQosclassEthBEPriority",
    "CfprQosclassEthClassifiedAdminState",
    "CfprQosclassEthClassifiedDrop",
    "CfprQosclassEthClassifiedPriority",
    "CfprQosclassFcAdminState",
    "CfprQosclassFcDrop",
    "CfprQosclassFcPriority")

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

cfprQosclassObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprQosclassDefinitionTable_Object = MibTable
cfprQosclassDefinitionTable = _CfprQosclassDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1)
)
if mibBuilder.loadTexts:
    cfprQosclassDefinitionTable.setStatus("current")
_CfprQosclassDefinitionEntry_Object = MibTableRow
cfprQosclassDefinitionEntry = _CfprQosclassDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1)
)
cfprQosclassDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-QOSCLASS-MIB", "cfprQosclassDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprQosclassDefinitionEntry.setStatus("current")
_CfprQosclassDefinitionInstanceId_Type = CfprManagedObjectId
_CfprQosclassDefinitionInstanceId_Object = MibTableColumn
cfprQosclassDefinitionInstanceId = _CfprQosclassDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 1),
    _CfprQosclassDefinitionInstanceId_Type()
)
cfprQosclassDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionInstanceId.setStatus("current")
_CfprQosclassDefinitionDn_Type = CfprManagedObjectDn
_CfprQosclassDefinitionDn_Object = MibTableColumn
cfprQosclassDefinitionDn = _CfprQosclassDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 2),
    _CfprQosclassDefinitionDn_Type()
)
cfprQosclassDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionDn.setStatus("current")
_CfprQosclassDefinitionRn_Type = SnmpAdminString
_CfprQosclassDefinitionRn_Object = MibTableColumn
cfprQosclassDefinitionRn = _CfprQosclassDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 3),
    _CfprQosclassDefinitionRn_Type()
)
cfprQosclassDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionRn.setStatus("current")
_CfprQosclassDefinitionDescr_Type = SnmpAdminString
_CfprQosclassDefinitionDescr_Object = MibTableColumn
cfprQosclassDefinitionDescr = _CfprQosclassDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 4),
    _CfprQosclassDefinitionDescr_Type()
)
cfprQosclassDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionDescr.setStatus("current")
_CfprQosclassDefinitionFsmDescr_Type = SnmpAdminString
_CfprQosclassDefinitionFsmDescr_Object = MibTableColumn
cfprQosclassDefinitionFsmDescr = _CfprQosclassDefinitionFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 5),
    _CfprQosclassDefinitionFsmDescr_Type()
)
cfprQosclassDefinitionFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmDescr.setStatus("current")
_CfprQosclassDefinitionFsmPrev_Type = SnmpAdminString
_CfprQosclassDefinitionFsmPrev_Object = MibTableColumn
cfprQosclassDefinitionFsmPrev = _CfprQosclassDefinitionFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 6),
    _CfprQosclassDefinitionFsmPrev_Type()
)
cfprQosclassDefinitionFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmPrev.setStatus("current")
_CfprQosclassDefinitionFsmProgr_Type = Gauge32
_CfprQosclassDefinitionFsmProgr_Object = MibTableColumn
cfprQosclassDefinitionFsmProgr = _CfprQosclassDefinitionFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 7),
    _CfprQosclassDefinitionFsmProgr_Type()
)
cfprQosclassDefinitionFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmProgr.setStatus("current")
_CfprQosclassDefinitionFsmRmtInvErrCode_Type = Gauge32
_CfprQosclassDefinitionFsmRmtInvErrCode_Object = MibTableColumn
cfprQosclassDefinitionFsmRmtInvErrCode = _CfprQosclassDefinitionFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 8),
    _CfprQosclassDefinitionFsmRmtInvErrCode_Type()
)
cfprQosclassDefinitionFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmRmtInvErrCode.setStatus("current")
_CfprQosclassDefinitionFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprQosclassDefinitionFsmRmtInvErrDescr_Object = MibTableColumn
cfprQosclassDefinitionFsmRmtInvErrDescr = _CfprQosclassDefinitionFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 9),
    _CfprQosclassDefinitionFsmRmtInvErrDescr_Type()
)
cfprQosclassDefinitionFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmRmtInvErrDescr.setStatus("current")
_CfprQosclassDefinitionFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprQosclassDefinitionFsmRmtInvRslt_Object = MibTableColumn
cfprQosclassDefinitionFsmRmtInvRslt = _CfprQosclassDefinitionFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 10),
    _CfprQosclassDefinitionFsmRmtInvRslt_Type()
)
cfprQosclassDefinitionFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmRmtInvRslt.setStatus("current")
_CfprQosclassDefinitionFsmStageDescr_Type = SnmpAdminString
_CfprQosclassDefinitionFsmStageDescr_Object = MibTableColumn
cfprQosclassDefinitionFsmStageDescr = _CfprQosclassDefinitionFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 11),
    _CfprQosclassDefinitionFsmStageDescr_Type()
)
cfprQosclassDefinitionFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStageDescr.setStatus("current")
_CfprQosclassDefinitionFsmStamp_Type = DateAndTime
_CfprQosclassDefinitionFsmStamp_Object = MibTableColumn
cfprQosclassDefinitionFsmStamp = _CfprQosclassDefinitionFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 12),
    _CfprQosclassDefinitionFsmStamp_Type()
)
cfprQosclassDefinitionFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStamp.setStatus("current")
_CfprQosclassDefinitionFsmStatus_Type = SnmpAdminString
_CfprQosclassDefinitionFsmStatus_Object = MibTableColumn
cfprQosclassDefinitionFsmStatus = _CfprQosclassDefinitionFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 13),
    _CfprQosclassDefinitionFsmStatus_Type()
)
cfprQosclassDefinitionFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStatus.setStatus("current")
_CfprQosclassDefinitionFsmTry_Type = Gauge32
_CfprQosclassDefinitionFsmTry_Object = MibTableColumn
cfprQosclassDefinitionFsmTry = _CfprQosclassDefinitionFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 14),
    _CfprQosclassDefinitionFsmTry_Type()
)
cfprQosclassDefinitionFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmTry.setStatus("current")
_CfprQosclassDefinitionIntId_Type = SnmpAdminString
_CfprQosclassDefinitionIntId_Object = MibTableColumn
cfprQosclassDefinitionIntId = _CfprQosclassDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 15),
    _CfprQosclassDefinitionIntId_Type()
)
cfprQosclassDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionIntId.setStatus("current")
_CfprQosclassDefinitionName_Type = SnmpAdminString
_CfprQosclassDefinitionName_Object = MibTableColumn
cfprQosclassDefinitionName = _CfprQosclassDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 16),
    _CfprQosclassDefinitionName_Type()
)
cfprQosclassDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionName.setStatus("current")
_CfprQosclassDefinitionPolicyLevel_Type = Gauge32
_CfprQosclassDefinitionPolicyLevel_Object = MibTableColumn
cfprQosclassDefinitionPolicyLevel = _CfprQosclassDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 17),
    _CfprQosclassDefinitionPolicyLevel_Type()
)
cfprQosclassDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionPolicyLevel.setStatus("current")
_CfprQosclassDefinitionPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprQosclassDefinitionPolicyOwner_Object = MibTableColumn
cfprQosclassDefinitionPolicyOwner = _CfprQosclassDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 1, 1, 18),
    _CfprQosclassDefinitionPolicyOwner_Type()
)
cfprQosclassDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionPolicyOwner.setStatus("current")
_CfprQosclassDefinitionFsmTable_Object = MibTable
cfprQosclassDefinitionFsmTable = _CfprQosclassDefinitionFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2)
)
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmTable.setStatus("current")
_CfprQosclassDefinitionFsmEntry_Object = MibTableRow
cfprQosclassDefinitionFsmEntry = _CfprQosclassDefinitionFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2, 1)
)
cfprQosclassDefinitionFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-QOSCLASS-MIB", "cfprQosclassDefinitionFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmEntry.setStatus("current")
_CfprQosclassDefinitionFsmInstanceId_Type = CfprManagedObjectId
_CfprQosclassDefinitionFsmInstanceId_Object = MibTableColumn
cfprQosclassDefinitionFsmInstanceId = _CfprQosclassDefinitionFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2, 1, 1),
    _CfprQosclassDefinitionFsmInstanceId_Type()
)
cfprQosclassDefinitionFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmInstanceId.setStatus("current")
_CfprQosclassDefinitionFsmDn_Type = CfprManagedObjectDn
_CfprQosclassDefinitionFsmDn_Object = MibTableColumn
cfprQosclassDefinitionFsmDn = _CfprQosclassDefinitionFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2, 1, 2),
    _CfprQosclassDefinitionFsmDn_Type()
)
cfprQosclassDefinitionFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmDn.setStatus("current")
_CfprQosclassDefinitionFsmRn_Type = SnmpAdminString
_CfprQosclassDefinitionFsmRn_Object = MibTableColumn
cfprQosclassDefinitionFsmRn = _CfprQosclassDefinitionFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2, 1, 3),
    _CfprQosclassDefinitionFsmRn_Type()
)
cfprQosclassDefinitionFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmRn.setStatus("current")
_CfprQosclassDefinitionFsmCompletionTime_Type = DateAndTime
_CfprQosclassDefinitionFsmCompletionTime_Object = MibTableColumn
cfprQosclassDefinitionFsmCompletionTime = _CfprQosclassDefinitionFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2, 1, 4),
    _CfprQosclassDefinitionFsmCompletionTime_Type()
)
cfprQosclassDefinitionFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmCompletionTime.setStatus("current")
_CfprQosclassDefinitionFsmCurrentFsm_Type = CfprQosclassDefinitionFsmCurrentFsm
_CfprQosclassDefinitionFsmCurrentFsm_Object = MibTableColumn
cfprQosclassDefinitionFsmCurrentFsm = _CfprQosclassDefinitionFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2, 1, 5),
    _CfprQosclassDefinitionFsmCurrentFsm_Type()
)
cfprQosclassDefinitionFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmCurrentFsm.setStatus("current")
_CfprQosclassDefinitionFsmDescrData_Type = SnmpAdminString
_CfprQosclassDefinitionFsmDescrData_Object = MibTableColumn
cfprQosclassDefinitionFsmDescrData = _CfprQosclassDefinitionFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2, 1, 6),
    _CfprQosclassDefinitionFsmDescrData_Type()
)
cfprQosclassDefinitionFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmDescrData.setStatus("current")
_CfprQosclassDefinitionFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprQosclassDefinitionFsmFsmStatus_Object = MibTableColumn
cfprQosclassDefinitionFsmFsmStatus = _CfprQosclassDefinitionFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2, 1, 7),
    _CfprQosclassDefinitionFsmFsmStatus_Type()
)
cfprQosclassDefinitionFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmFsmStatus.setStatus("current")
_CfprQosclassDefinitionFsmProgress_Type = Gauge32
_CfprQosclassDefinitionFsmProgress_Object = MibTableColumn
cfprQosclassDefinitionFsmProgress = _CfprQosclassDefinitionFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2, 1, 8),
    _CfprQosclassDefinitionFsmProgress_Type()
)
cfprQosclassDefinitionFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmProgress.setStatus("current")
_CfprQosclassDefinitionFsmRmtErrCode_Type = Gauge32
_CfprQosclassDefinitionFsmRmtErrCode_Object = MibTableColumn
cfprQosclassDefinitionFsmRmtErrCode = _CfprQosclassDefinitionFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2, 1, 9),
    _CfprQosclassDefinitionFsmRmtErrCode_Type()
)
cfprQosclassDefinitionFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmRmtErrCode.setStatus("current")
_CfprQosclassDefinitionFsmRmtErrDescr_Type = SnmpAdminString
_CfprQosclassDefinitionFsmRmtErrDescr_Object = MibTableColumn
cfprQosclassDefinitionFsmRmtErrDescr = _CfprQosclassDefinitionFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2, 1, 10),
    _CfprQosclassDefinitionFsmRmtErrDescr_Type()
)
cfprQosclassDefinitionFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmRmtErrDescr.setStatus("current")
_CfprQosclassDefinitionFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprQosclassDefinitionFsmRmtRslt_Object = MibTableColumn
cfprQosclassDefinitionFsmRmtRslt = _CfprQosclassDefinitionFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 2, 1, 11),
    _CfprQosclassDefinitionFsmRmtRslt_Type()
)
cfprQosclassDefinitionFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmRmtRslt.setStatus("current")
_CfprQosclassDefinitionFsmStageTable_Object = MibTable
cfprQosclassDefinitionFsmStageTable = _CfprQosclassDefinitionFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 3)
)
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStageTable.setStatus("current")
_CfprQosclassDefinitionFsmStageEntry_Object = MibTableRow
cfprQosclassDefinitionFsmStageEntry = _CfprQosclassDefinitionFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 3, 1)
)
cfprQosclassDefinitionFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-QOSCLASS-MIB", "cfprQosclassDefinitionFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStageEntry.setStatus("current")
_CfprQosclassDefinitionFsmStageInstanceId_Type = CfprManagedObjectId
_CfprQosclassDefinitionFsmStageInstanceId_Object = MibTableColumn
cfprQosclassDefinitionFsmStageInstanceId = _CfprQosclassDefinitionFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 3, 1, 1),
    _CfprQosclassDefinitionFsmStageInstanceId_Type()
)
cfprQosclassDefinitionFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStageInstanceId.setStatus("current")
_CfprQosclassDefinitionFsmStageDn_Type = CfprManagedObjectDn
_CfprQosclassDefinitionFsmStageDn_Object = MibTableColumn
cfprQosclassDefinitionFsmStageDn = _CfprQosclassDefinitionFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 3, 1, 2),
    _CfprQosclassDefinitionFsmStageDn_Type()
)
cfprQosclassDefinitionFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStageDn.setStatus("current")
_CfprQosclassDefinitionFsmStageRn_Type = SnmpAdminString
_CfprQosclassDefinitionFsmStageRn_Object = MibTableColumn
cfprQosclassDefinitionFsmStageRn = _CfprQosclassDefinitionFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 3, 1, 3),
    _CfprQosclassDefinitionFsmStageRn_Type()
)
cfprQosclassDefinitionFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStageRn.setStatus("current")
_CfprQosclassDefinitionFsmStageDescrData_Type = SnmpAdminString
_CfprQosclassDefinitionFsmStageDescrData_Object = MibTableColumn
cfprQosclassDefinitionFsmStageDescrData = _CfprQosclassDefinitionFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 3, 1, 4),
    _CfprQosclassDefinitionFsmStageDescrData_Type()
)
cfprQosclassDefinitionFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStageDescrData.setStatus("current")
_CfprQosclassDefinitionFsmStageLastUpdateTime_Type = DateAndTime
_CfprQosclassDefinitionFsmStageLastUpdateTime_Object = MibTableColumn
cfprQosclassDefinitionFsmStageLastUpdateTime = _CfprQosclassDefinitionFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 3, 1, 5),
    _CfprQosclassDefinitionFsmStageLastUpdateTime_Type()
)
cfprQosclassDefinitionFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStageLastUpdateTime.setStatus("current")
_CfprQosclassDefinitionFsmStageName_Type = CfprQosclassDefinitionFsmStageName
_CfprQosclassDefinitionFsmStageName_Object = MibTableColumn
cfprQosclassDefinitionFsmStageName = _CfprQosclassDefinitionFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 3, 1, 6),
    _CfprQosclassDefinitionFsmStageName_Type()
)
cfprQosclassDefinitionFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStageName.setStatus("current")
_CfprQosclassDefinitionFsmStageOrder_Type = Gauge32
_CfprQosclassDefinitionFsmStageOrder_Object = MibTableColumn
cfprQosclassDefinitionFsmStageOrder = _CfprQosclassDefinitionFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 3, 1, 7),
    _CfprQosclassDefinitionFsmStageOrder_Type()
)
cfprQosclassDefinitionFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStageOrder.setStatus("current")
_CfprQosclassDefinitionFsmStageRetry_Type = Gauge32
_CfprQosclassDefinitionFsmStageRetry_Object = MibTableColumn
cfprQosclassDefinitionFsmStageRetry = _CfprQosclassDefinitionFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 3, 1, 8),
    _CfprQosclassDefinitionFsmStageRetry_Type()
)
cfprQosclassDefinitionFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStageRetry.setStatus("current")
_CfprQosclassDefinitionFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprQosclassDefinitionFsmStageStageStatus_Object = MibTableColumn
cfprQosclassDefinitionFsmStageStageStatus = _CfprQosclassDefinitionFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 3, 1, 9),
    _CfprQosclassDefinitionFsmStageStageStatus_Type()
)
cfprQosclassDefinitionFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmStageStageStatus.setStatus("current")
_CfprQosclassDefinitionFsmTaskTable_Object = MibTable
cfprQosclassDefinitionFsmTaskTable = _CfprQosclassDefinitionFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 4)
)
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmTaskTable.setStatus("current")
_CfprQosclassDefinitionFsmTaskEntry_Object = MibTableRow
cfprQosclassDefinitionFsmTaskEntry = _CfprQosclassDefinitionFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 4, 1)
)
cfprQosclassDefinitionFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-QOSCLASS-MIB", "cfprQosclassDefinitionFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmTaskEntry.setStatus("current")
_CfprQosclassDefinitionFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprQosclassDefinitionFsmTaskInstanceId_Object = MibTableColumn
cfprQosclassDefinitionFsmTaskInstanceId = _CfprQosclassDefinitionFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 4, 1, 1),
    _CfprQosclassDefinitionFsmTaskInstanceId_Type()
)
cfprQosclassDefinitionFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmTaskInstanceId.setStatus("current")
_CfprQosclassDefinitionFsmTaskDn_Type = CfprManagedObjectDn
_CfprQosclassDefinitionFsmTaskDn_Object = MibTableColumn
cfprQosclassDefinitionFsmTaskDn = _CfprQosclassDefinitionFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 4, 1, 2),
    _CfprQosclassDefinitionFsmTaskDn_Type()
)
cfprQosclassDefinitionFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmTaskDn.setStatus("current")
_CfprQosclassDefinitionFsmTaskRn_Type = SnmpAdminString
_CfprQosclassDefinitionFsmTaskRn_Object = MibTableColumn
cfprQosclassDefinitionFsmTaskRn = _CfprQosclassDefinitionFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 4, 1, 3),
    _CfprQosclassDefinitionFsmTaskRn_Type()
)
cfprQosclassDefinitionFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmTaskRn.setStatus("current")
_CfprQosclassDefinitionFsmTaskCompletion_Type = CfprFsmCompletion
_CfprQosclassDefinitionFsmTaskCompletion_Object = MibTableColumn
cfprQosclassDefinitionFsmTaskCompletion = _CfprQosclassDefinitionFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 4, 1, 4),
    _CfprQosclassDefinitionFsmTaskCompletion_Type()
)
cfprQosclassDefinitionFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmTaskCompletion.setStatus("current")
_CfprQosclassDefinitionFsmTaskFlags_Type = CfprFsmFlags
_CfprQosclassDefinitionFsmTaskFlags_Object = MibTableColumn
cfprQosclassDefinitionFsmTaskFlags = _CfprQosclassDefinitionFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 4, 1, 5),
    _CfprQosclassDefinitionFsmTaskFlags_Type()
)
cfprQosclassDefinitionFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmTaskFlags.setStatus("current")
_CfprQosclassDefinitionFsmTaskItem_Type = CfprQosclassDefinitionFsmTaskItem
_CfprQosclassDefinitionFsmTaskItem_Object = MibTableColumn
cfprQosclassDefinitionFsmTaskItem = _CfprQosclassDefinitionFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 4, 1, 6),
    _CfprQosclassDefinitionFsmTaskItem_Type()
)
cfprQosclassDefinitionFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmTaskItem.setStatus("current")
_CfprQosclassDefinitionFsmTaskSeqId_Type = Gauge32
_CfprQosclassDefinitionFsmTaskSeqId_Object = MibTableColumn
cfprQosclassDefinitionFsmTaskSeqId = _CfprQosclassDefinitionFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 4, 1, 7),
    _CfprQosclassDefinitionFsmTaskSeqId_Type()
)
cfprQosclassDefinitionFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassDefinitionFsmTaskSeqId.setStatus("current")
_CfprQosclassEthBETable_Object = MibTable
cfprQosclassEthBETable = _CfprQosclassEthBETable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5)
)
if mibBuilder.loadTexts:
    cfprQosclassEthBETable.setStatus("current")
_CfprQosclassEthBEEntry_Object = MibTableRow
cfprQosclassEthBEEntry = _CfprQosclassEthBEEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1)
)
cfprQosclassEthBEEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-QOSCLASS-MIB", "cfprQosclassEthBEInstanceId"),
)
if mibBuilder.loadTexts:
    cfprQosclassEthBEEntry.setStatus("current")
_CfprQosclassEthBEInstanceId_Type = CfprManagedObjectId
_CfprQosclassEthBEInstanceId_Object = MibTableColumn
cfprQosclassEthBEInstanceId = _CfprQosclassEthBEInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1, 1),
    _CfprQosclassEthBEInstanceId_Type()
)
cfprQosclassEthBEInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprQosclassEthBEInstanceId.setStatus("current")
_CfprQosclassEthBEDn_Type = CfprManagedObjectDn
_CfprQosclassEthBEDn_Object = MibTableColumn
cfprQosclassEthBEDn = _CfprQosclassEthBEDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1, 2),
    _CfprQosclassEthBEDn_Type()
)
cfprQosclassEthBEDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthBEDn.setStatus("current")
_CfprQosclassEthBERn_Type = SnmpAdminString
_CfprQosclassEthBERn_Object = MibTableColumn
cfprQosclassEthBERn = _CfprQosclassEthBERn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1, 3),
    _CfprQosclassEthBERn_Type()
)
cfprQosclassEthBERn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthBERn.setStatus("current")
_CfprQosclassEthBEAdminState_Type = CfprQosclassEthBEAdminState
_CfprQosclassEthBEAdminState_Object = MibTableColumn
cfprQosclassEthBEAdminState = _CfprQosclassEthBEAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1, 4),
    _CfprQosclassEthBEAdminState_Type()
)
cfprQosclassEthBEAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthBEAdminState.setStatus("current")
_CfprQosclassEthBEBwPercent_Type = Gauge32
_CfprQosclassEthBEBwPercent_Object = MibTableColumn
cfprQosclassEthBEBwPercent = _CfprQosclassEthBEBwPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1, 5),
    _CfprQosclassEthBEBwPercent_Type()
)
cfprQosclassEthBEBwPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthBEBwPercent.setStatus("current")
_CfprQosclassEthBECos_Type = Gauge32
_CfprQosclassEthBECos_Object = MibTableColumn
cfprQosclassEthBECos = _CfprQosclassEthBECos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1, 6),
    _CfprQosclassEthBECos_Type()
)
cfprQosclassEthBECos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthBECos.setStatus("current")
_CfprQosclassEthBEDrop_Type = CfprQosclassEthBEDrop
_CfprQosclassEthBEDrop_Object = MibTableColumn
cfprQosclassEthBEDrop = _CfprQosclassEthBEDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1, 7),
    _CfprQosclassEthBEDrop_Type()
)
cfprQosclassEthBEDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthBEDrop.setStatus("current")
_CfprQosclassEthBEMtu_Type = SnmpAdminString
_CfprQosclassEthBEMtu_Object = MibTableColumn
cfprQosclassEthBEMtu = _CfprQosclassEthBEMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1, 8),
    _CfprQosclassEthBEMtu_Type()
)
cfprQosclassEthBEMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthBEMtu.setStatus("current")
_CfprQosclassEthBEMulticastOptimize_Type = TruthValue
_CfprQosclassEthBEMulticastOptimize_Object = MibTableColumn
cfprQosclassEthBEMulticastOptimize = _CfprQosclassEthBEMulticastOptimize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1, 9),
    _CfprQosclassEthBEMulticastOptimize_Type()
)
cfprQosclassEthBEMulticastOptimize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthBEMulticastOptimize.setStatus("current")
_CfprQosclassEthBEName_Type = SnmpAdminString
_CfprQosclassEthBEName_Object = MibTableColumn
cfprQosclassEthBEName = _CfprQosclassEthBEName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1, 10),
    _CfprQosclassEthBEName_Type()
)
cfprQosclassEthBEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthBEName.setStatus("current")
_CfprQosclassEthBEPriority_Type = CfprQosclassEthBEPriority
_CfprQosclassEthBEPriority_Object = MibTableColumn
cfprQosclassEthBEPriority = _CfprQosclassEthBEPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1, 11),
    _CfprQosclassEthBEPriority_Type()
)
cfprQosclassEthBEPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthBEPriority.setStatus("current")
_CfprQosclassEthBEWeight_Type = Gauge32
_CfprQosclassEthBEWeight_Object = MibTableColumn
cfprQosclassEthBEWeight = _CfprQosclassEthBEWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 5, 1, 12),
    _CfprQosclassEthBEWeight_Type()
)
cfprQosclassEthBEWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthBEWeight.setStatus("current")
_CfprQosclassEthClassifiedTable_Object = MibTable
cfprQosclassEthClassifiedTable = _CfprQosclassEthClassifiedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6)
)
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedTable.setStatus("current")
_CfprQosclassEthClassifiedEntry_Object = MibTableRow
cfprQosclassEthClassifiedEntry = _CfprQosclassEthClassifiedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1)
)
cfprQosclassEthClassifiedEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-QOSCLASS-MIB", "cfprQosclassEthClassifiedInstanceId"),
)
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedEntry.setStatus("current")
_CfprQosclassEthClassifiedInstanceId_Type = CfprManagedObjectId
_CfprQosclassEthClassifiedInstanceId_Object = MibTableColumn
cfprQosclassEthClassifiedInstanceId = _CfprQosclassEthClassifiedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1, 1),
    _CfprQosclassEthClassifiedInstanceId_Type()
)
cfprQosclassEthClassifiedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedInstanceId.setStatus("current")
_CfprQosclassEthClassifiedDn_Type = CfprManagedObjectDn
_CfprQosclassEthClassifiedDn_Object = MibTableColumn
cfprQosclassEthClassifiedDn = _CfprQosclassEthClassifiedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1, 2),
    _CfprQosclassEthClassifiedDn_Type()
)
cfprQosclassEthClassifiedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedDn.setStatus("current")
_CfprQosclassEthClassifiedRn_Type = SnmpAdminString
_CfprQosclassEthClassifiedRn_Object = MibTableColumn
cfprQosclassEthClassifiedRn = _CfprQosclassEthClassifiedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1, 3),
    _CfprQosclassEthClassifiedRn_Type()
)
cfprQosclassEthClassifiedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedRn.setStatus("current")
_CfprQosclassEthClassifiedAdminState_Type = CfprQosclassEthClassifiedAdminState
_CfprQosclassEthClassifiedAdminState_Object = MibTableColumn
cfprQosclassEthClassifiedAdminState = _CfprQosclassEthClassifiedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1, 4),
    _CfprQosclassEthClassifiedAdminState_Type()
)
cfprQosclassEthClassifiedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedAdminState.setStatus("current")
_CfprQosclassEthClassifiedBwPercent_Type = Gauge32
_CfprQosclassEthClassifiedBwPercent_Object = MibTableColumn
cfprQosclassEthClassifiedBwPercent = _CfprQosclassEthClassifiedBwPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1, 5),
    _CfprQosclassEthClassifiedBwPercent_Type()
)
cfprQosclassEthClassifiedBwPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedBwPercent.setStatus("current")
_CfprQosclassEthClassifiedCos_Type = Gauge32
_CfprQosclassEthClassifiedCos_Object = MibTableColumn
cfprQosclassEthClassifiedCos = _CfprQosclassEthClassifiedCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1, 6),
    _CfprQosclassEthClassifiedCos_Type()
)
cfprQosclassEthClassifiedCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedCos.setStatus("current")
_CfprQosclassEthClassifiedDrop_Type = CfprQosclassEthClassifiedDrop
_CfprQosclassEthClassifiedDrop_Object = MibTableColumn
cfprQosclassEthClassifiedDrop = _CfprQosclassEthClassifiedDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1, 7),
    _CfprQosclassEthClassifiedDrop_Type()
)
cfprQosclassEthClassifiedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedDrop.setStatus("current")
_CfprQosclassEthClassifiedMtu_Type = SnmpAdminString
_CfprQosclassEthClassifiedMtu_Object = MibTableColumn
cfprQosclassEthClassifiedMtu = _CfprQosclassEthClassifiedMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1, 8),
    _CfprQosclassEthClassifiedMtu_Type()
)
cfprQosclassEthClassifiedMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedMtu.setStatus("current")
_CfprQosclassEthClassifiedMulticastOptimize_Type = TruthValue
_CfprQosclassEthClassifiedMulticastOptimize_Object = MibTableColumn
cfprQosclassEthClassifiedMulticastOptimize = _CfprQosclassEthClassifiedMulticastOptimize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1, 9),
    _CfprQosclassEthClassifiedMulticastOptimize_Type()
)
cfprQosclassEthClassifiedMulticastOptimize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedMulticastOptimize.setStatus("current")
_CfprQosclassEthClassifiedName_Type = SnmpAdminString
_CfprQosclassEthClassifiedName_Object = MibTableColumn
cfprQosclassEthClassifiedName = _CfprQosclassEthClassifiedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1, 10),
    _CfprQosclassEthClassifiedName_Type()
)
cfprQosclassEthClassifiedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedName.setStatus("current")
_CfprQosclassEthClassifiedPriority_Type = CfprQosclassEthClassifiedPriority
_CfprQosclassEthClassifiedPriority_Object = MibTableColumn
cfprQosclassEthClassifiedPriority = _CfprQosclassEthClassifiedPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1, 11),
    _CfprQosclassEthClassifiedPriority_Type()
)
cfprQosclassEthClassifiedPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedPriority.setStatus("current")
_CfprQosclassEthClassifiedWeight_Type = Gauge32
_CfprQosclassEthClassifiedWeight_Object = MibTableColumn
cfprQosclassEthClassifiedWeight = _CfprQosclassEthClassifiedWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 6, 1, 12),
    _CfprQosclassEthClassifiedWeight_Type()
)
cfprQosclassEthClassifiedWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassEthClassifiedWeight.setStatus("current")
_CfprQosclassFcTable_Object = MibTable
cfprQosclassFcTable = _CfprQosclassFcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7)
)
if mibBuilder.loadTexts:
    cfprQosclassFcTable.setStatus("current")
_CfprQosclassFcEntry_Object = MibTableRow
cfprQosclassFcEntry = _CfprQosclassFcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7, 1)
)
cfprQosclassFcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-QOSCLASS-MIB", "cfprQosclassFcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprQosclassFcEntry.setStatus("current")
_CfprQosclassFcInstanceId_Type = CfprManagedObjectId
_CfprQosclassFcInstanceId_Object = MibTableColumn
cfprQosclassFcInstanceId = _CfprQosclassFcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7, 1, 1),
    _CfprQosclassFcInstanceId_Type()
)
cfprQosclassFcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprQosclassFcInstanceId.setStatus("current")
_CfprQosclassFcDn_Type = CfprManagedObjectDn
_CfprQosclassFcDn_Object = MibTableColumn
cfprQosclassFcDn = _CfprQosclassFcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7, 1, 2),
    _CfprQosclassFcDn_Type()
)
cfprQosclassFcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassFcDn.setStatus("current")
_CfprQosclassFcRn_Type = SnmpAdminString
_CfprQosclassFcRn_Object = MibTableColumn
cfprQosclassFcRn = _CfprQosclassFcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7, 1, 3),
    _CfprQosclassFcRn_Type()
)
cfprQosclassFcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassFcRn.setStatus("current")
_CfprQosclassFcAdminState_Type = CfprQosclassFcAdminState
_CfprQosclassFcAdminState_Object = MibTableColumn
cfprQosclassFcAdminState = _CfprQosclassFcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7, 1, 4),
    _CfprQosclassFcAdminState_Type()
)
cfprQosclassFcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassFcAdminState.setStatus("current")
_CfprQosclassFcBwPercent_Type = Gauge32
_CfprQosclassFcBwPercent_Object = MibTableColumn
cfprQosclassFcBwPercent = _CfprQosclassFcBwPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7, 1, 5),
    _CfprQosclassFcBwPercent_Type()
)
cfprQosclassFcBwPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassFcBwPercent.setStatus("current")
_CfprQosclassFcCos_Type = Gauge32
_CfprQosclassFcCos_Object = MibTableColumn
cfprQosclassFcCos = _CfprQosclassFcCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7, 1, 6),
    _CfprQosclassFcCos_Type()
)
cfprQosclassFcCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassFcCos.setStatus("current")
_CfprQosclassFcDrop_Type = CfprQosclassFcDrop
_CfprQosclassFcDrop_Object = MibTableColumn
cfprQosclassFcDrop = _CfprQosclassFcDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7, 1, 7),
    _CfprQosclassFcDrop_Type()
)
cfprQosclassFcDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassFcDrop.setStatus("current")
_CfprQosclassFcMtu_Type = SnmpAdminString
_CfprQosclassFcMtu_Object = MibTableColumn
cfprQosclassFcMtu = _CfprQosclassFcMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7, 1, 8),
    _CfprQosclassFcMtu_Type()
)
cfprQosclassFcMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassFcMtu.setStatus("current")
_CfprQosclassFcName_Type = SnmpAdminString
_CfprQosclassFcName_Object = MibTableColumn
cfprQosclassFcName = _CfprQosclassFcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7, 1, 9),
    _CfprQosclassFcName_Type()
)
cfprQosclassFcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassFcName.setStatus("current")
_CfprQosclassFcPriority_Type = CfprQosclassFcPriority
_CfprQosclassFcPriority_Object = MibTableColumn
cfprQosclassFcPriority = _CfprQosclassFcPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7, 1, 10),
    _CfprQosclassFcPriority_Type()
)
cfprQosclassFcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassFcPriority.setStatus("current")
_CfprQosclassFcWeight_Type = Gauge32
_CfprQosclassFcWeight_Object = MibTableColumn
cfprQosclassFcWeight = _CfprQosclassFcWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 67, 7, 1, 11),
    _CfprQosclassFcWeight_Type()
)
cfprQosclassFcWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprQosclassFcWeight.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-QOSCLASS-MIB",
    **{"cfprQosclassObjects": cfprQosclassObjects,
       "cfprQosclassDefinitionTable": cfprQosclassDefinitionTable,
       "cfprQosclassDefinitionEntry": cfprQosclassDefinitionEntry,
       "cfprQosclassDefinitionInstanceId": cfprQosclassDefinitionInstanceId,
       "cfprQosclassDefinitionDn": cfprQosclassDefinitionDn,
       "cfprQosclassDefinitionRn": cfprQosclassDefinitionRn,
       "cfprQosclassDefinitionDescr": cfprQosclassDefinitionDescr,
       "cfprQosclassDefinitionFsmDescr": cfprQosclassDefinitionFsmDescr,
       "cfprQosclassDefinitionFsmPrev": cfprQosclassDefinitionFsmPrev,
       "cfprQosclassDefinitionFsmProgr": cfprQosclassDefinitionFsmProgr,
       "cfprQosclassDefinitionFsmRmtInvErrCode": cfprQosclassDefinitionFsmRmtInvErrCode,
       "cfprQosclassDefinitionFsmRmtInvErrDescr": cfprQosclassDefinitionFsmRmtInvErrDescr,
       "cfprQosclassDefinitionFsmRmtInvRslt": cfprQosclassDefinitionFsmRmtInvRslt,
       "cfprQosclassDefinitionFsmStageDescr": cfprQosclassDefinitionFsmStageDescr,
       "cfprQosclassDefinitionFsmStamp": cfprQosclassDefinitionFsmStamp,
       "cfprQosclassDefinitionFsmStatus": cfprQosclassDefinitionFsmStatus,
       "cfprQosclassDefinitionFsmTry": cfprQosclassDefinitionFsmTry,
       "cfprQosclassDefinitionIntId": cfprQosclassDefinitionIntId,
       "cfprQosclassDefinitionName": cfprQosclassDefinitionName,
       "cfprQosclassDefinitionPolicyLevel": cfprQosclassDefinitionPolicyLevel,
       "cfprQosclassDefinitionPolicyOwner": cfprQosclassDefinitionPolicyOwner,
       "cfprQosclassDefinitionFsmTable": cfprQosclassDefinitionFsmTable,
       "cfprQosclassDefinitionFsmEntry": cfprQosclassDefinitionFsmEntry,
       "cfprQosclassDefinitionFsmInstanceId": cfprQosclassDefinitionFsmInstanceId,
       "cfprQosclassDefinitionFsmDn": cfprQosclassDefinitionFsmDn,
       "cfprQosclassDefinitionFsmRn": cfprQosclassDefinitionFsmRn,
       "cfprQosclassDefinitionFsmCompletionTime": cfprQosclassDefinitionFsmCompletionTime,
       "cfprQosclassDefinitionFsmCurrentFsm": cfprQosclassDefinitionFsmCurrentFsm,
       "cfprQosclassDefinitionFsmDescrData": cfprQosclassDefinitionFsmDescrData,
       "cfprQosclassDefinitionFsmFsmStatus": cfprQosclassDefinitionFsmFsmStatus,
       "cfprQosclassDefinitionFsmProgress": cfprQosclassDefinitionFsmProgress,
       "cfprQosclassDefinitionFsmRmtErrCode": cfprQosclassDefinitionFsmRmtErrCode,
       "cfprQosclassDefinitionFsmRmtErrDescr": cfprQosclassDefinitionFsmRmtErrDescr,
       "cfprQosclassDefinitionFsmRmtRslt": cfprQosclassDefinitionFsmRmtRslt,
       "cfprQosclassDefinitionFsmStageTable": cfprQosclassDefinitionFsmStageTable,
       "cfprQosclassDefinitionFsmStageEntry": cfprQosclassDefinitionFsmStageEntry,
       "cfprQosclassDefinitionFsmStageInstanceId": cfprQosclassDefinitionFsmStageInstanceId,
       "cfprQosclassDefinitionFsmStageDn": cfprQosclassDefinitionFsmStageDn,
       "cfprQosclassDefinitionFsmStageRn": cfprQosclassDefinitionFsmStageRn,
       "cfprQosclassDefinitionFsmStageDescrData": cfprQosclassDefinitionFsmStageDescrData,
       "cfprQosclassDefinitionFsmStageLastUpdateTime": cfprQosclassDefinitionFsmStageLastUpdateTime,
       "cfprQosclassDefinitionFsmStageName": cfprQosclassDefinitionFsmStageName,
       "cfprQosclassDefinitionFsmStageOrder": cfprQosclassDefinitionFsmStageOrder,
       "cfprQosclassDefinitionFsmStageRetry": cfprQosclassDefinitionFsmStageRetry,
       "cfprQosclassDefinitionFsmStageStageStatus": cfprQosclassDefinitionFsmStageStageStatus,
       "cfprQosclassDefinitionFsmTaskTable": cfprQosclassDefinitionFsmTaskTable,
       "cfprQosclassDefinitionFsmTaskEntry": cfprQosclassDefinitionFsmTaskEntry,
       "cfprQosclassDefinitionFsmTaskInstanceId": cfprQosclassDefinitionFsmTaskInstanceId,
       "cfprQosclassDefinitionFsmTaskDn": cfprQosclassDefinitionFsmTaskDn,
       "cfprQosclassDefinitionFsmTaskRn": cfprQosclassDefinitionFsmTaskRn,
       "cfprQosclassDefinitionFsmTaskCompletion": cfprQosclassDefinitionFsmTaskCompletion,
       "cfprQosclassDefinitionFsmTaskFlags": cfprQosclassDefinitionFsmTaskFlags,
       "cfprQosclassDefinitionFsmTaskItem": cfprQosclassDefinitionFsmTaskItem,
       "cfprQosclassDefinitionFsmTaskSeqId": cfprQosclassDefinitionFsmTaskSeqId,
       "cfprQosclassEthBETable": cfprQosclassEthBETable,
       "cfprQosclassEthBEEntry": cfprQosclassEthBEEntry,
       "cfprQosclassEthBEInstanceId": cfprQosclassEthBEInstanceId,
       "cfprQosclassEthBEDn": cfprQosclassEthBEDn,
       "cfprQosclassEthBERn": cfprQosclassEthBERn,
       "cfprQosclassEthBEAdminState": cfprQosclassEthBEAdminState,
       "cfprQosclassEthBEBwPercent": cfprQosclassEthBEBwPercent,
       "cfprQosclassEthBECos": cfprQosclassEthBECos,
       "cfprQosclassEthBEDrop": cfprQosclassEthBEDrop,
       "cfprQosclassEthBEMtu": cfprQosclassEthBEMtu,
       "cfprQosclassEthBEMulticastOptimize": cfprQosclassEthBEMulticastOptimize,
       "cfprQosclassEthBEName": cfprQosclassEthBEName,
       "cfprQosclassEthBEPriority": cfprQosclassEthBEPriority,
       "cfprQosclassEthBEWeight": cfprQosclassEthBEWeight,
       "cfprQosclassEthClassifiedTable": cfprQosclassEthClassifiedTable,
       "cfprQosclassEthClassifiedEntry": cfprQosclassEthClassifiedEntry,
       "cfprQosclassEthClassifiedInstanceId": cfprQosclassEthClassifiedInstanceId,
       "cfprQosclassEthClassifiedDn": cfprQosclassEthClassifiedDn,
       "cfprQosclassEthClassifiedRn": cfprQosclassEthClassifiedRn,
       "cfprQosclassEthClassifiedAdminState": cfprQosclassEthClassifiedAdminState,
       "cfprQosclassEthClassifiedBwPercent": cfprQosclassEthClassifiedBwPercent,
       "cfprQosclassEthClassifiedCos": cfprQosclassEthClassifiedCos,
       "cfprQosclassEthClassifiedDrop": cfprQosclassEthClassifiedDrop,
       "cfprQosclassEthClassifiedMtu": cfprQosclassEthClassifiedMtu,
       "cfprQosclassEthClassifiedMulticastOptimize": cfprQosclassEthClassifiedMulticastOptimize,
       "cfprQosclassEthClassifiedName": cfprQosclassEthClassifiedName,
       "cfprQosclassEthClassifiedPriority": cfprQosclassEthClassifiedPriority,
       "cfprQosclassEthClassifiedWeight": cfprQosclassEthClassifiedWeight,
       "cfprQosclassFcTable": cfprQosclassFcTable,
       "cfprQosclassFcEntry": cfprQosclassFcEntry,
       "cfprQosclassFcInstanceId": cfprQosclassFcInstanceId,
       "cfprQosclassFcDn": cfprQosclassFcDn,
       "cfprQosclassFcRn": cfprQosclassFcRn,
       "cfprQosclassFcAdminState": cfprQosclassFcAdminState,
       "cfprQosclassFcBwPercent": cfprQosclassFcBwPercent,
       "cfprQosclassFcCos": cfprQosclassFcCos,
       "cfprQosclassFcDrop": cfprQosclassFcDrop,
       "cfprQosclassFcMtu": cfprQosclassFcMtu,
       "cfprQosclassFcName": cfprQosclassFcName,
       "cfprQosclassFcPriority": cfprQosclassFcPriority,
       "cfprQosclassFcWeight": cfprQosclassFcWeight}
)
