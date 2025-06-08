# SNMP MIB module (CISCO-FIREPOWER-AP-QOSCLASS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-QOSCLASS-MIB.mib
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
 CfprApPolicyPolicyOwner,
 CfprApQosclassDefinitionFsmCurrentFsm,
 CfprApQosclassDefinitionFsmStageName,
 CfprApQosclassDefinitionFsmTaskItem,
 CfprApQosclassEthBEAdminState,
 CfprApQosclassEthBEDrop,
 CfprApQosclassEthBEPriority,
 CfprApQosclassEthClassifiedAdminState,
 CfprApQosclassEthClassifiedDrop,
 CfprApQosclassEthClassifiedPriority,
 CfprApQosclassFcAdminState,
 CfprApQosclassFcDrop,
 CfprApQosclassFcPriority) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApPolicyPolicyOwner",
    "CfprApQosclassDefinitionFsmCurrentFsm",
    "CfprApQosclassDefinitionFsmStageName",
    "CfprApQosclassDefinitionFsmTaskItem",
    "CfprApQosclassEthBEAdminState",
    "CfprApQosclassEthBEDrop",
    "CfprApQosclassEthBEPriority",
    "CfprApQosclassEthClassifiedAdminState",
    "CfprApQosclassEthClassifiedDrop",
    "CfprApQosclassEthClassifiedPriority",
    "CfprApQosclassFcAdminState",
    "CfprApQosclassFcDrop",
    "CfprApQosclassFcPriority")

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

cfprApQosclassObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApQosclassDefinitionTable_Object = MibTable
cfprApQosclassDefinitionTable = _CfprApQosclassDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1)
)
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionTable.setStatus("current")
_CfprApQosclassDefinitionEntry_Object = MibTableRow
cfprApQosclassDefinitionEntry = _CfprApQosclassDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1)
)
cfprApQosclassDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-QOSCLASS-MIB", "cfprApQosclassDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionEntry.setStatus("current")
_CfprApQosclassDefinitionInstanceId_Type = CfprApManagedObjectId
_CfprApQosclassDefinitionInstanceId_Object = MibTableColumn
cfprApQosclassDefinitionInstanceId = _CfprApQosclassDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 1),
    _CfprApQosclassDefinitionInstanceId_Type()
)
cfprApQosclassDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionInstanceId.setStatus("current")
_CfprApQosclassDefinitionDn_Type = CfprApManagedObjectDn
_CfprApQosclassDefinitionDn_Object = MibTableColumn
cfprApQosclassDefinitionDn = _CfprApQosclassDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 2),
    _CfprApQosclassDefinitionDn_Type()
)
cfprApQosclassDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionDn.setStatus("current")
_CfprApQosclassDefinitionRn_Type = SnmpAdminString
_CfprApQosclassDefinitionRn_Object = MibTableColumn
cfprApQosclassDefinitionRn = _CfprApQosclassDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 3),
    _CfprApQosclassDefinitionRn_Type()
)
cfprApQosclassDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionRn.setStatus("current")
_CfprApQosclassDefinitionDescr_Type = SnmpAdminString
_CfprApQosclassDefinitionDescr_Object = MibTableColumn
cfprApQosclassDefinitionDescr = _CfprApQosclassDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 4),
    _CfprApQosclassDefinitionDescr_Type()
)
cfprApQosclassDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionDescr.setStatus("current")
_CfprApQosclassDefinitionFsmDescr_Type = SnmpAdminString
_CfprApQosclassDefinitionFsmDescr_Object = MibTableColumn
cfprApQosclassDefinitionFsmDescr = _CfprApQosclassDefinitionFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 5),
    _CfprApQosclassDefinitionFsmDescr_Type()
)
cfprApQosclassDefinitionFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmDescr.setStatus("current")
_CfprApQosclassDefinitionFsmPrev_Type = SnmpAdminString
_CfprApQosclassDefinitionFsmPrev_Object = MibTableColumn
cfprApQosclassDefinitionFsmPrev = _CfprApQosclassDefinitionFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 6),
    _CfprApQosclassDefinitionFsmPrev_Type()
)
cfprApQosclassDefinitionFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmPrev.setStatus("current")
_CfprApQosclassDefinitionFsmProgr_Type = Gauge32
_CfprApQosclassDefinitionFsmProgr_Object = MibTableColumn
cfprApQosclassDefinitionFsmProgr = _CfprApQosclassDefinitionFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 7),
    _CfprApQosclassDefinitionFsmProgr_Type()
)
cfprApQosclassDefinitionFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmProgr.setStatus("current")
_CfprApQosclassDefinitionFsmRmtInvErrCode_Type = Gauge32
_CfprApQosclassDefinitionFsmRmtInvErrCode_Object = MibTableColumn
cfprApQosclassDefinitionFsmRmtInvErrCode = _CfprApQosclassDefinitionFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 8),
    _CfprApQosclassDefinitionFsmRmtInvErrCode_Type()
)
cfprApQosclassDefinitionFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmRmtInvErrCode.setStatus("current")
_CfprApQosclassDefinitionFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApQosclassDefinitionFsmRmtInvErrDescr_Object = MibTableColumn
cfprApQosclassDefinitionFsmRmtInvErrDescr = _CfprApQosclassDefinitionFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 9),
    _CfprApQosclassDefinitionFsmRmtInvErrDescr_Type()
)
cfprApQosclassDefinitionFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmRmtInvErrDescr.setStatus("current")
_CfprApQosclassDefinitionFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApQosclassDefinitionFsmRmtInvRslt_Object = MibTableColumn
cfprApQosclassDefinitionFsmRmtInvRslt = _CfprApQosclassDefinitionFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 10),
    _CfprApQosclassDefinitionFsmRmtInvRslt_Type()
)
cfprApQosclassDefinitionFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmRmtInvRslt.setStatus("current")
_CfprApQosclassDefinitionFsmStageDescr_Type = SnmpAdminString
_CfprApQosclassDefinitionFsmStageDescr_Object = MibTableColumn
cfprApQosclassDefinitionFsmStageDescr = _CfprApQosclassDefinitionFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 11),
    _CfprApQosclassDefinitionFsmStageDescr_Type()
)
cfprApQosclassDefinitionFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStageDescr.setStatus("current")
_CfprApQosclassDefinitionFsmStamp_Type = DateAndTime
_CfprApQosclassDefinitionFsmStamp_Object = MibTableColumn
cfprApQosclassDefinitionFsmStamp = _CfprApQosclassDefinitionFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 12),
    _CfprApQosclassDefinitionFsmStamp_Type()
)
cfprApQosclassDefinitionFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStamp.setStatus("current")
_CfprApQosclassDefinitionFsmStatus_Type = SnmpAdminString
_CfprApQosclassDefinitionFsmStatus_Object = MibTableColumn
cfprApQosclassDefinitionFsmStatus = _CfprApQosclassDefinitionFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 13),
    _CfprApQosclassDefinitionFsmStatus_Type()
)
cfprApQosclassDefinitionFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStatus.setStatus("current")
_CfprApQosclassDefinitionFsmTry_Type = Gauge32
_CfprApQosclassDefinitionFsmTry_Object = MibTableColumn
cfprApQosclassDefinitionFsmTry = _CfprApQosclassDefinitionFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 14),
    _CfprApQosclassDefinitionFsmTry_Type()
)
cfprApQosclassDefinitionFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmTry.setStatus("current")
_CfprApQosclassDefinitionIntId_Type = SnmpAdminString
_CfprApQosclassDefinitionIntId_Object = MibTableColumn
cfprApQosclassDefinitionIntId = _CfprApQosclassDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 15),
    _CfprApQosclassDefinitionIntId_Type()
)
cfprApQosclassDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionIntId.setStatus("current")
_CfprApQosclassDefinitionName_Type = SnmpAdminString
_CfprApQosclassDefinitionName_Object = MibTableColumn
cfprApQosclassDefinitionName = _CfprApQosclassDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 16),
    _CfprApQosclassDefinitionName_Type()
)
cfprApQosclassDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionName.setStatus("current")
_CfprApQosclassDefinitionPolicyLevel_Type = Gauge32
_CfprApQosclassDefinitionPolicyLevel_Object = MibTableColumn
cfprApQosclassDefinitionPolicyLevel = _CfprApQosclassDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 17),
    _CfprApQosclassDefinitionPolicyLevel_Type()
)
cfprApQosclassDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionPolicyLevel.setStatus("current")
_CfprApQosclassDefinitionPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApQosclassDefinitionPolicyOwner_Object = MibTableColumn
cfprApQosclassDefinitionPolicyOwner = _CfprApQosclassDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 1, 1, 18),
    _CfprApQosclassDefinitionPolicyOwner_Type()
)
cfprApQosclassDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionPolicyOwner.setStatus("current")
_CfprApQosclassDefinitionFsmTable_Object = MibTable
cfprApQosclassDefinitionFsmTable = _CfprApQosclassDefinitionFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2)
)
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmTable.setStatus("current")
_CfprApQosclassDefinitionFsmEntry_Object = MibTableRow
cfprApQosclassDefinitionFsmEntry = _CfprApQosclassDefinitionFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2, 1)
)
cfprApQosclassDefinitionFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-QOSCLASS-MIB", "cfprApQosclassDefinitionFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmEntry.setStatus("current")
_CfprApQosclassDefinitionFsmInstanceId_Type = CfprApManagedObjectId
_CfprApQosclassDefinitionFsmInstanceId_Object = MibTableColumn
cfprApQosclassDefinitionFsmInstanceId = _CfprApQosclassDefinitionFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2, 1, 1),
    _CfprApQosclassDefinitionFsmInstanceId_Type()
)
cfprApQosclassDefinitionFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmInstanceId.setStatus("current")
_CfprApQosclassDefinitionFsmDn_Type = CfprApManagedObjectDn
_CfprApQosclassDefinitionFsmDn_Object = MibTableColumn
cfprApQosclassDefinitionFsmDn = _CfprApQosclassDefinitionFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2, 1, 2),
    _CfprApQosclassDefinitionFsmDn_Type()
)
cfprApQosclassDefinitionFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmDn.setStatus("current")
_CfprApQosclassDefinitionFsmRn_Type = SnmpAdminString
_CfprApQosclassDefinitionFsmRn_Object = MibTableColumn
cfprApQosclassDefinitionFsmRn = _CfprApQosclassDefinitionFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2, 1, 3),
    _CfprApQosclassDefinitionFsmRn_Type()
)
cfprApQosclassDefinitionFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmRn.setStatus("current")
_CfprApQosclassDefinitionFsmCompletionTime_Type = DateAndTime
_CfprApQosclassDefinitionFsmCompletionTime_Object = MibTableColumn
cfprApQosclassDefinitionFsmCompletionTime = _CfprApQosclassDefinitionFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2, 1, 4),
    _CfprApQosclassDefinitionFsmCompletionTime_Type()
)
cfprApQosclassDefinitionFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmCompletionTime.setStatus("current")
_CfprApQosclassDefinitionFsmCurrentFsm_Type = CfprApQosclassDefinitionFsmCurrentFsm
_CfprApQosclassDefinitionFsmCurrentFsm_Object = MibTableColumn
cfprApQosclassDefinitionFsmCurrentFsm = _CfprApQosclassDefinitionFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2, 1, 5),
    _CfprApQosclassDefinitionFsmCurrentFsm_Type()
)
cfprApQosclassDefinitionFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmCurrentFsm.setStatus("current")
_CfprApQosclassDefinitionFsmDescrData_Type = SnmpAdminString
_CfprApQosclassDefinitionFsmDescrData_Object = MibTableColumn
cfprApQosclassDefinitionFsmDescrData = _CfprApQosclassDefinitionFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2, 1, 6),
    _CfprApQosclassDefinitionFsmDescrData_Type()
)
cfprApQosclassDefinitionFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmDescrData.setStatus("current")
_CfprApQosclassDefinitionFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApQosclassDefinitionFsmFsmStatus_Object = MibTableColumn
cfprApQosclassDefinitionFsmFsmStatus = _CfprApQosclassDefinitionFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2, 1, 7),
    _CfprApQosclassDefinitionFsmFsmStatus_Type()
)
cfprApQosclassDefinitionFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmFsmStatus.setStatus("current")
_CfprApQosclassDefinitionFsmProgress_Type = Gauge32
_CfprApQosclassDefinitionFsmProgress_Object = MibTableColumn
cfprApQosclassDefinitionFsmProgress = _CfprApQosclassDefinitionFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2, 1, 8),
    _CfprApQosclassDefinitionFsmProgress_Type()
)
cfprApQosclassDefinitionFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmProgress.setStatus("current")
_CfprApQosclassDefinitionFsmRmtErrCode_Type = Gauge32
_CfprApQosclassDefinitionFsmRmtErrCode_Object = MibTableColumn
cfprApQosclassDefinitionFsmRmtErrCode = _CfprApQosclassDefinitionFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2, 1, 9),
    _CfprApQosclassDefinitionFsmRmtErrCode_Type()
)
cfprApQosclassDefinitionFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmRmtErrCode.setStatus("current")
_CfprApQosclassDefinitionFsmRmtErrDescr_Type = SnmpAdminString
_CfprApQosclassDefinitionFsmRmtErrDescr_Object = MibTableColumn
cfprApQosclassDefinitionFsmRmtErrDescr = _CfprApQosclassDefinitionFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2, 1, 10),
    _CfprApQosclassDefinitionFsmRmtErrDescr_Type()
)
cfprApQosclassDefinitionFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmRmtErrDescr.setStatus("current")
_CfprApQosclassDefinitionFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApQosclassDefinitionFsmRmtRslt_Object = MibTableColumn
cfprApQosclassDefinitionFsmRmtRslt = _CfprApQosclassDefinitionFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 2, 1, 11),
    _CfprApQosclassDefinitionFsmRmtRslt_Type()
)
cfprApQosclassDefinitionFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmRmtRslt.setStatus("current")
_CfprApQosclassDefinitionFsmStageTable_Object = MibTable
cfprApQosclassDefinitionFsmStageTable = _CfprApQosclassDefinitionFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 3)
)
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStageTable.setStatus("current")
_CfprApQosclassDefinitionFsmStageEntry_Object = MibTableRow
cfprApQosclassDefinitionFsmStageEntry = _CfprApQosclassDefinitionFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 3, 1)
)
cfprApQosclassDefinitionFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-QOSCLASS-MIB", "cfprApQosclassDefinitionFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStageEntry.setStatus("current")
_CfprApQosclassDefinitionFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApQosclassDefinitionFsmStageInstanceId_Object = MibTableColumn
cfprApQosclassDefinitionFsmStageInstanceId = _CfprApQosclassDefinitionFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 3, 1, 1),
    _CfprApQosclassDefinitionFsmStageInstanceId_Type()
)
cfprApQosclassDefinitionFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStageInstanceId.setStatus("current")
_CfprApQosclassDefinitionFsmStageDn_Type = CfprApManagedObjectDn
_CfprApQosclassDefinitionFsmStageDn_Object = MibTableColumn
cfprApQosclassDefinitionFsmStageDn = _CfprApQosclassDefinitionFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 3, 1, 2),
    _CfprApQosclassDefinitionFsmStageDn_Type()
)
cfprApQosclassDefinitionFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStageDn.setStatus("current")
_CfprApQosclassDefinitionFsmStageRn_Type = SnmpAdminString
_CfprApQosclassDefinitionFsmStageRn_Object = MibTableColumn
cfprApQosclassDefinitionFsmStageRn = _CfprApQosclassDefinitionFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 3, 1, 3),
    _CfprApQosclassDefinitionFsmStageRn_Type()
)
cfprApQosclassDefinitionFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStageRn.setStatus("current")
_CfprApQosclassDefinitionFsmStageDescrData_Type = SnmpAdminString
_CfprApQosclassDefinitionFsmStageDescrData_Object = MibTableColumn
cfprApQosclassDefinitionFsmStageDescrData = _CfprApQosclassDefinitionFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 3, 1, 4),
    _CfprApQosclassDefinitionFsmStageDescrData_Type()
)
cfprApQosclassDefinitionFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStageDescrData.setStatus("current")
_CfprApQosclassDefinitionFsmStageLastUpdateTime_Type = DateAndTime
_CfprApQosclassDefinitionFsmStageLastUpdateTime_Object = MibTableColumn
cfprApQosclassDefinitionFsmStageLastUpdateTime = _CfprApQosclassDefinitionFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 3, 1, 5),
    _CfprApQosclassDefinitionFsmStageLastUpdateTime_Type()
)
cfprApQosclassDefinitionFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStageLastUpdateTime.setStatus("current")
_CfprApQosclassDefinitionFsmStageName_Type = CfprApQosclassDefinitionFsmStageName
_CfprApQosclassDefinitionFsmStageName_Object = MibTableColumn
cfprApQosclassDefinitionFsmStageName = _CfprApQosclassDefinitionFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 3, 1, 6),
    _CfprApQosclassDefinitionFsmStageName_Type()
)
cfprApQosclassDefinitionFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStageName.setStatus("current")
_CfprApQosclassDefinitionFsmStageOrder_Type = Gauge32
_CfprApQosclassDefinitionFsmStageOrder_Object = MibTableColumn
cfprApQosclassDefinitionFsmStageOrder = _CfprApQosclassDefinitionFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 3, 1, 7),
    _CfprApQosclassDefinitionFsmStageOrder_Type()
)
cfprApQosclassDefinitionFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStageOrder.setStatus("current")
_CfprApQosclassDefinitionFsmStageRetry_Type = Gauge32
_CfprApQosclassDefinitionFsmStageRetry_Object = MibTableColumn
cfprApQosclassDefinitionFsmStageRetry = _CfprApQosclassDefinitionFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 3, 1, 8),
    _CfprApQosclassDefinitionFsmStageRetry_Type()
)
cfprApQosclassDefinitionFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStageRetry.setStatus("current")
_CfprApQosclassDefinitionFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApQosclassDefinitionFsmStageStageStatus_Object = MibTableColumn
cfprApQosclassDefinitionFsmStageStageStatus = _CfprApQosclassDefinitionFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 3, 1, 9),
    _CfprApQosclassDefinitionFsmStageStageStatus_Type()
)
cfprApQosclassDefinitionFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmStageStageStatus.setStatus("current")
_CfprApQosclassDefinitionFsmTaskTable_Object = MibTable
cfprApQosclassDefinitionFsmTaskTable = _CfprApQosclassDefinitionFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 4)
)
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmTaskTable.setStatus("current")
_CfprApQosclassDefinitionFsmTaskEntry_Object = MibTableRow
cfprApQosclassDefinitionFsmTaskEntry = _CfprApQosclassDefinitionFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 4, 1)
)
cfprApQosclassDefinitionFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-QOSCLASS-MIB", "cfprApQosclassDefinitionFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmTaskEntry.setStatus("current")
_CfprApQosclassDefinitionFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApQosclassDefinitionFsmTaskInstanceId_Object = MibTableColumn
cfprApQosclassDefinitionFsmTaskInstanceId = _CfprApQosclassDefinitionFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 4, 1, 1),
    _CfprApQosclassDefinitionFsmTaskInstanceId_Type()
)
cfprApQosclassDefinitionFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmTaskInstanceId.setStatus("current")
_CfprApQosclassDefinitionFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApQosclassDefinitionFsmTaskDn_Object = MibTableColumn
cfprApQosclassDefinitionFsmTaskDn = _CfprApQosclassDefinitionFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 4, 1, 2),
    _CfprApQosclassDefinitionFsmTaskDn_Type()
)
cfprApQosclassDefinitionFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmTaskDn.setStatus("current")
_CfprApQosclassDefinitionFsmTaskRn_Type = SnmpAdminString
_CfprApQosclassDefinitionFsmTaskRn_Object = MibTableColumn
cfprApQosclassDefinitionFsmTaskRn = _CfprApQosclassDefinitionFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 4, 1, 3),
    _CfprApQosclassDefinitionFsmTaskRn_Type()
)
cfprApQosclassDefinitionFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmTaskRn.setStatus("current")
_CfprApQosclassDefinitionFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApQosclassDefinitionFsmTaskCompletion_Object = MibTableColumn
cfprApQosclassDefinitionFsmTaskCompletion = _CfprApQosclassDefinitionFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 4, 1, 4),
    _CfprApQosclassDefinitionFsmTaskCompletion_Type()
)
cfprApQosclassDefinitionFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmTaskCompletion.setStatus("current")
_CfprApQosclassDefinitionFsmTaskFlags_Type = CfprApFsmFlags
_CfprApQosclassDefinitionFsmTaskFlags_Object = MibTableColumn
cfprApQosclassDefinitionFsmTaskFlags = _CfprApQosclassDefinitionFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 4, 1, 5),
    _CfprApQosclassDefinitionFsmTaskFlags_Type()
)
cfprApQosclassDefinitionFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmTaskFlags.setStatus("current")
_CfprApQosclassDefinitionFsmTaskItem_Type = CfprApQosclassDefinitionFsmTaskItem
_CfprApQosclassDefinitionFsmTaskItem_Object = MibTableColumn
cfprApQosclassDefinitionFsmTaskItem = _CfprApQosclassDefinitionFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 4, 1, 6),
    _CfprApQosclassDefinitionFsmTaskItem_Type()
)
cfprApQosclassDefinitionFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmTaskItem.setStatus("current")
_CfprApQosclassDefinitionFsmTaskSeqId_Type = Gauge32
_CfprApQosclassDefinitionFsmTaskSeqId_Object = MibTableColumn
cfprApQosclassDefinitionFsmTaskSeqId = _CfprApQosclassDefinitionFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 4, 1, 7),
    _CfprApQosclassDefinitionFsmTaskSeqId_Type()
)
cfprApQosclassDefinitionFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassDefinitionFsmTaskSeqId.setStatus("current")
_CfprApQosclassEthBETable_Object = MibTable
cfprApQosclassEthBETable = _CfprApQosclassEthBETable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5)
)
if mibBuilder.loadTexts:
    cfprApQosclassEthBETable.setStatus("current")
_CfprApQosclassEthBEEntry_Object = MibTableRow
cfprApQosclassEthBEEntry = _CfprApQosclassEthBEEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1)
)
cfprApQosclassEthBEEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-QOSCLASS-MIB", "cfprApQosclassEthBEInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApQosclassEthBEEntry.setStatus("current")
_CfprApQosclassEthBEInstanceId_Type = CfprApManagedObjectId
_CfprApQosclassEthBEInstanceId_Object = MibTableColumn
cfprApQosclassEthBEInstanceId = _CfprApQosclassEthBEInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1, 1),
    _CfprApQosclassEthBEInstanceId_Type()
)
cfprApQosclassEthBEInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApQosclassEthBEInstanceId.setStatus("current")
_CfprApQosclassEthBEDn_Type = CfprApManagedObjectDn
_CfprApQosclassEthBEDn_Object = MibTableColumn
cfprApQosclassEthBEDn = _CfprApQosclassEthBEDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1, 2),
    _CfprApQosclassEthBEDn_Type()
)
cfprApQosclassEthBEDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthBEDn.setStatus("current")
_CfprApQosclassEthBERn_Type = SnmpAdminString
_CfprApQosclassEthBERn_Object = MibTableColumn
cfprApQosclassEthBERn = _CfprApQosclassEthBERn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1, 3),
    _CfprApQosclassEthBERn_Type()
)
cfprApQosclassEthBERn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthBERn.setStatus("current")
_CfprApQosclassEthBEAdminState_Type = CfprApQosclassEthBEAdminState
_CfprApQosclassEthBEAdminState_Object = MibTableColumn
cfprApQosclassEthBEAdminState = _CfprApQosclassEthBEAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1, 4),
    _CfprApQosclassEthBEAdminState_Type()
)
cfprApQosclassEthBEAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthBEAdminState.setStatus("current")
_CfprApQosclassEthBEBwPercent_Type = Gauge32
_CfprApQosclassEthBEBwPercent_Object = MibTableColumn
cfprApQosclassEthBEBwPercent = _CfprApQosclassEthBEBwPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1, 5),
    _CfprApQosclassEthBEBwPercent_Type()
)
cfprApQosclassEthBEBwPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthBEBwPercent.setStatus("current")
_CfprApQosclassEthBECos_Type = Gauge32
_CfprApQosclassEthBECos_Object = MibTableColumn
cfprApQosclassEthBECos = _CfprApQosclassEthBECos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1, 6),
    _CfprApQosclassEthBECos_Type()
)
cfprApQosclassEthBECos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthBECos.setStatus("current")
_CfprApQosclassEthBEDrop_Type = CfprApQosclassEthBEDrop
_CfprApQosclassEthBEDrop_Object = MibTableColumn
cfprApQosclassEthBEDrop = _CfprApQosclassEthBEDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1, 7),
    _CfprApQosclassEthBEDrop_Type()
)
cfprApQosclassEthBEDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthBEDrop.setStatus("current")
_CfprApQosclassEthBEMtu_Type = SnmpAdminString
_CfprApQosclassEthBEMtu_Object = MibTableColumn
cfprApQosclassEthBEMtu = _CfprApQosclassEthBEMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1, 8),
    _CfprApQosclassEthBEMtu_Type()
)
cfprApQosclassEthBEMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthBEMtu.setStatus("current")
_CfprApQosclassEthBEMulticastOptimize_Type = TruthValue
_CfprApQosclassEthBEMulticastOptimize_Object = MibTableColumn
cfprApQosclassEthBEMulticastOptimize = _CfprApQosclassEthBEMulticastOptimize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1, 9),
    _CfprApQosclassEthBEMulticastOptimize_Type()
)
cfprApQosclassEthBEMulticastOptimize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthBEMulticastOptimize.setStatus("current")
_CfprApQosclassEthBEName_Type = SnmpAdminString
_CfprApQosclassEthBEName_Object = MibTableColumn
cfprApQosclassEthBEName = _CfprApQosclassEthBEName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1, 10),
    _CfprApQosclassEthBEName_Type()
)
cfprApQosclassEthBEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthBEName.setStatus("current")
_CfprApQosclassEthBEPriority_Type = CfprApQosclassEthBEPriority
_CfprApQosclassEthBEPriority_Object = MibTableColumn
cfprApQosclassEthBEPriority = _CfprApQosclassEthBEPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1, 11),
    _CfprApQosclassEthBEPriority_Type()
)
cfprApQosclassEthBEPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthBEPriority.setStatus("current")
_CfprApQosclassEthBEWeight_Type = Gauge32
_CfprApQosclassEthBEWeight_Object = MibTableColumn
cfprApQosclassEthBEWeight = _CfprApQosclassEthBEWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 5, 1, 12),
    _CfprApQosclassEthBEWeight_Type()
)
cfprApQosclassEthBEWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthBEWeight.setStatus("current")
_CfprApQosclassEthClassifiedTable_Object = MibTable
cfprApQosclassEthClassifiedTable = _CfprApQosclassEthClassifiedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6)
)
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedTable.setStatus("current")
_CfprApQosclassEthClassifiedEntry_Object = MibTableRow
cfprApQosclassEthClassifiedEntry = _CfprApQosclassEthClassifiedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1)
)
cfprApQosclassEthClassifiedEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-QOSCLASS-MIB", "cfprApQosclassEthClassifiedInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedEntry.setStatus("current")
_CfprApQosclassEthClassifiedInstanceId_Type = CfprApManagedObjectId
_CfprApQosclassEthClassifiedInstanceId_Object = MibTableColumn
cfprApQosclassEthClassifiedInstanceId = _CfprApQosclassEthClassifiedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1, 1),
    _CfprApQosclassEthClassifiedInstanceId_Type()
)
cfprApQosclassEthClassifiedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedInstanceId.setStatus("current")
_CfprApQosclassEthClassifiedDn_Type = CfprApManagedObjectDn
_CfprApQosclassEthClassifiedDn_Object = MibTableColumn
cfprApQosclassEthClassifiedDn = _CfprApQosclassEthClassifiedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1, 2),
    _CfprApQosclassEthClassifiedDn_Type()
)
cfprApQosclassEthClassifiedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedDn.setStatus("current")
_CfprApQosclassEthClassifiedRn_Type = SnmpAdminString
_CfprApQosclassEthClassifiedRn_Object = MibTableColumn
cfprApQosclassEthClassifiedRn = _CfprApQosclassEthClassifiedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1, 3),
    _CfprApQosclassEthClassifiedRn_Type()
)
cfprApQosclassEthClassifiedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedRn.setStatus("current")
_CfprApQosclassEthClassifiedAdminState_Type = CfprApQosclassEthClassifiedAdminState
_CfprApQosclassEthClassifiedAdminState_Object = MibTableColumn
cfprApQosclassEthClassifiedAdminState = _CfprApQosclassEthClassifiedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1, 4),
    _CfprApQosclassEthClassifiedAdminState_Type()
)
cfprApQosclassEthClassifiedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedAdminState.setStatus("current")
_CfprApQosclassEthClassifiedBwPercent_Type = Gauge32
_CfprApQosclassEthClassifiedBwPercent_Object = MibTableColumn
cfprApQosclassEthClassifiedBwPercent = _CfprApQosclassEthClassifiedBwPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1, 5),
    _CfprApQosclassEthClassifiedBwPercent_Type()
)
cfprApQosclassEthClassifiedBwPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedBwPercent.setStatus("current")
_CfprApQosclassEthClassifiedCos_Type = Gauge32
_CfprApQosclassEthClassifiedCos_Object = MibTableColumn
cfprApQosclassEthClassifiedCos = _CfprApQosclassEthClassifiedCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1, 6),
    _CfprApQosclassEthClassifiedCos_Type()
)
cfprApQosclassEthClassifiedCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedCos.setStatus("current")
_CfprApQosclassEthClassifiedDrop_Type = CfprApQosclassEthClassifiedDrop
_CfprApQosclassEthClassifiedDrop_Object = MibTableColumn
cfprApQosclassEthClassifiedDrop = _CfprApQosclassEthClassifiedDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1, 7),
    _CfprApQosclassEthClassifiedDrop_Type()
)
cfprApQosclassEthClassifiedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedDrop.setStatus("current")
_CfprApQosclassEthClassifiedMtu_Type = SnmpAdminString
_CfprApQosclassEthClassifiedMtu_Object = MibTableColumn
cfprApQosclassEthClassifiedMtu = _CfprApQosclassEthClassifiedMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1, 8),
    _CfprApQosclassEthClassifiedMtu_Type()
)
cfprApQosclassEthClassifiedMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedMtu.setStatus("current")
_CfprApQosclassEthClassifiedMulticastOptimize_Type = TruthValue
_CfprApQosclassEthClassifiedMulticastOptimize_Object = MibTableColumn
cfprApQosclassEthClassifiedMulticastOptimize = _CfprApQosclassEthClassifiedMulticastOptimize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1, 9),
    _CfprApQosclassEthClassifiedMulticastOptimize_Type()
)
cfprApQosclassEthClassifiedMulticastOptimize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedMulticastOptimize.setStatus("current")
_CfprApQosclassEthClassifiedName_Type = SnmpAdminString
_CfprApQosclassEthClassifiedName_Object = MibTableColumn
cfprApQosclassEthClassifiedName = _CfprApQosclassEthClassifiedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1, 10),
    _CfprApQosclassEthClassifiedName_Type()
)
cfprApQosclassEthClassifiedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedName.setStatus("current")
_CfprApQosclassEthClassifiedPriority_Type = CfprApQosclassEthClassifiedPriority
_CfprApQosclassEthClassifiedPriority_Object = MibTableColumn
cfprApQosclassEthClassifiedPriority = _CfprApQosclassEthClassifiedPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1, 11),
    _CfprApQosclassEthClassifiedPriority_Type()
)
cfprApQosclassEthClassifiedPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedPriority.setStatus("current")
_CfprApQosclassEthClassifiedWeight_Type = Gauge32
_CfprApQosclassEthClassifiedWeight_Object = MibTableColumn
cfprApQosclassEthClassifiedWeight = _CfprApQosclassEthClassifiedWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 6, 1, 12),
    _CfprApQosclassEthClassifiedWeight_Type()
)
cfprApQosclassEthClassifiedWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassEthClassifiedWeight.setStatus("current")
_CfprApQosclassFcTable_Object = MibTable
cfprApQosclassFcTable = _CfprApQosclassFcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7)
)
if mibBuilder.loadTexts:
    cfprApQosclassFcTable.setStatus("current")
_CfprApQosclassFcEntry_Object = MibTableRow
cfprApQosclassFcEntry = _CfprApQosclassFcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7, 1)
)
cfprApQosclassFcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-QOSCLASS-MIB", "cfprApQosclassFcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApQosclassFcEntry.setStatus("current")
_CfprApQosclassFcInstanceId_Type = CfprApManagedObjectId
_CfprApQosclassFcInstanceId_Object = MibTableColumn
cfprApQosclassFcInstanceId = _CfprApQosclassFcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7, 1, 1),
    _CfprApQosclassFcInstanceId_Type()
)
cfprApQosclassFcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApQosclassFcInstanceId.setStatus("current")
_CfprApQosclassFcDn_Type = CfprApManagedObjectDn
_CfprApQosclassFcDn_Object = MibTableColumn
cfprApQosclassFcDn = _CfprApQosclassFcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7, 1, 2),
    _CfprApQosclassFcDn_Type()
)
cfprApQosclassFcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassFcDn.setStatus("current")
_CfprApQosclassFcRn_Type = SnmpAdminString
_CfprApQosclassFcRn_Object = MibTableColumn
cfprApQosclassFcRn = _CfprApQosclassFcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7, 1, 3),
    _CfprApQosclassFcRn_Type()
)
cfprApQosclassFcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassFcRn.setStatus("current")
_CfprApQosclassFcAdminState_Type = CfprApQosclassFcAdminState
_CfprApQosclassFcAdminState_Object = MibTableColumn
cfprApQosclassFcAdminState = _CfprApQosclassFcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7, 1, 4),
    _CfprApQosclassFcAdminState_Type()
)
cfprApQosclassFcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassFcAdminState.setStatus("current")
_CfprApQosclassFcBwPercent_Type = Gauge32
_CfprApQosclassFcBwPercent_Object = MibTableColumn
cfprApQosclassFcBwPercent = _CfprApQosclassFcBwPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7, 1, 5),
    _CfprApQosclassFcBwPercent_Type()
)
cfprApQosclassFcBwPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassFcBwPercent.setStatus("current")
_CfprApQosclassFcCos_Type = Gauge32
_CfprApQosclassFcCos_Object = MibTableColumn
cfprApQosclassFcCos = _CfprApQosclassFcCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7, 1, 6),
    _CfprApQosclassFcCos_Type()
)
cfprApQosclassFcCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassFcCos.setStatus("current")
_CfprApQosclassFcDrop_Type = CfprApQosclassFcDrop
_CfprApQosclassFcDrop_Object = MibTableColumn
cfprApQosclassFcDrop = _CfprApQosclassFcDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7, 1, 7),
    _CfprApQosclassFcDrop_Type()
)
cfprApQosclassFcDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassFcDrop.setStatus("current")
_CfprApQosclassFcMtu_Type = SnmpAdminString
_CfprApQosclassFcMtu_Object = MibTableColumn
cfprApQosclassFcMtu = _CfprApQosclassFcMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7, 1, 8),
    _CfprApQosclassFcMtu_Type()
)
cfprApQosclassFcMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassFcMtu.setStatus("current")
_CfprApQosclassFcName_Type = SnmpAdminString
_CfprApQosclassFcName_Object = MibTableColumn
cfprApQosclassFcName = _CfprApQosclassFcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7, 1, 9),
    _CfprApQosclassFcName_Type()
)
cfprApQosclassFcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassFcName.setStatus("current")
_CfprApQosclassFcPriority_Type = CfprApQosclassFcPriority
_CfprApQosclassFcPriority_Object = MibTableColumn
cfprApQosclassFcPriority = _CfprApQosclassFcPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7, 1, 10),
    _CfprApQosclassFcPriority_Type()
)
cfprApQosclassFcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassFcPriority.setStatus("current")
_CfprApQosclassFcWeight_Type = Gauge32
_CfprApQosclassFcWeight_Object = MibTableColumn
cfprApQosclassFcWeight = _CfprApQosclassFcWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 67, 7, 1, 11),
    _CfprApQosclassFcWeight_Type()
)
cfprApQosclassFcWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApQosclassFcWeight.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-QOSCLASS-MIB",
    **{"cfprApQosclassObjects": cfprApQosclassObjects,
       "cfprApQosclassDefinitionTable": cfprApQosclassDefinitionTable,
       "cfprApQosclassDefinitionEntry": cfprApQosclassDefinitionEntry,
       "cfprApQosclassDefinitionInstanceId": cfprApQosclassDefinitionInstanceId,
       "cfprApQosclassDefinitionDn": cfprApQosclassDefinitionDn,
       "cfprApQosclassDefinitionRn": cfprApQosclassDefinitionRn,
       "cfprApQosclassDefinitionDescr": cfprApQosclassDefinitionDescr,
       "cfprApQosclassDefinitionFsmDescr": cfprApQosclassDefinitionFsmDescr,
       "cfprApQosclassDefinitionFsmPrev": cfprApQosclassDefinitionFsmPrev,
       "cfprApQosclassDefinitionFsmProgr": cfprApQosclassDefinitionFsmProgr,
       "cfprApQosclassDefinitionFsmRmtInvErrCode": cfprApQosclassDefinitionFsmRmtInvErrCode,
       "cfprApQosclassDefinitionFsmRmtInvErrDescr": cfprApQosclassDefinitionFsmRmtInvErrDescr,
       "cfprApQosclassDefinitionFsmRmtInvRslt": cfprApQosclassDefinitionFsmRmtInvRslt,
       "cfprApQosclassDefinitionFsmStageDescr": cfprApQosclassDefinitionFsmStageDescr,
       "cfprApQosclassDefinitionFsmStamp": cfprApQosclassDefinitionFsmStamp,
       "cfprApQosclassDefinitionFsmStatus": cfprApQosclassDefinitionFsmStatus,
       "cfprApQosclassDefinitionFsmTry": cfprApQosclassDefinitionFsmTry,
       "cfprApQosclassDefinitionIntId": cfprApQosclassDefinitionIntId,
       "cfprApQosclassDefinitionName": cfprApQosclassDefinitionName,
       "cfprApQosclassDefinitionPolicyLevel": cfprApQosclassDefinitionPolicyLevel,
       "cfprApQosclassDefinitionPolicyOwner": cfprApQosclassDefinitionPolicyOwner,
       "cfprApQosclassDefinitionFsmTable": cfprApQosclassDefinitionFsmTable,
       "cfprApQosclassDefinitionFsmEntry": cfprApQosclassDefinitionFsmEntry,
       "cfprApQosclassDefinitionFsmInstanceId": cfprApQosclassDefinitionFsmInstanceId,
       "cfprApQosclassDefinitionFsmDn": cfprApQosclassDefinitionFsmDn,
       "cfprApQosclassDefinitionFsmRn": cfprApQosclassDefinitionFsmRn,
       "cfprApQosclassDefinitionFsmCompletionTime": cfprApQosclassDefinitionFsmCompletionTime,
       "cfprApQosclassDefinitionFsmCurrentFsm": cfprApQosclassDefinitionFsmCurrentFsm,
       "cfprApQosclassDefinitionFsmDescrData": cfprApQosclassDefinitionFsmDescrData,
       "cfprApQosclassDefinitionFsmFsmStatus": cfprApQosclassDefinitionFsmFsmStatus,
       "cfprApQosclassDefinitionFsmProgress": cfprApQosclassDefinitionFsmProgress,
       "cfprApQosclassDefinitionFsmRmtErrCode": cfprApQosclassDefinitionFsmRmtErrCode,
       "cfprApQosclassDefinitionFsmRmtErrDescr": cfprApQosclassDefinitionFsmRmtErrDescr,
       "cfprApQosclassDefinitionFsmRmtRslt": cfprApQosclassDefinitionFsmRmtRslt,
       "cfprApQosclassDefinitionFsmStageTable": cfprApQosclassDefinitionFsmStageTable,
       "cfprApQosclassDefinitionFsmStageEntry": cfprApQosclassDefinitionFsmStageEntry,
       "cfprApQosclassDefinitionFsmStageInstanceId": cfprApQosclassDefinitionFsmStageInstanceId,
       "cfprApQosclassDefinitionFsmStageDn": cfprApQosclassDefinitionFsmStageDn,
       "cfprApQosclassDefinitionFsmStageRn": cfprApQosclassDefinitionFsmStageRn,
       "cfprApQosclassDefinitionFsmStageDescrData": cfprApQosclassDefinitionFsmStageDescrData,
       "cfprApQosclassDefinitionFsmStageLastUpdateTime": cfprApQosclassDefinitionFsmStageLastUpdateTime,
       "cfprApQosclassDefinitionFsmStageName": cfprApQosclassDefinitionFsmStageName,
       "cfprApQosclassDefinitionFsmStageOrder": cfprApQosclassDefinitionFsmStageOrder,
       "cfprApQosclassDefinitionFsmStageRetry": cfprApQosclassDefinitionFsmStageRetry,
       "cfprApQosclassDefinitionFsmStageStageStatus": cfprApQosclassDefinitionFsmStageStageStatus,
       "cfprApQosclassDefinitionFsmTaskTable": cfprApQosclassDefinitionFsmTaskTable,
       "cfprApQosclassDefinitionFsmTaskEntry": cfprApQosclassDefinitionFsmTaskEntry,
       "cfprApQosclassDefinitionFsmTaskInstanceId": cfprApQosclassDefinitionFsmTaskInstanceId,
       "cfprApQosclassDefinitionFsmTaskDn": cfprApQosclassDefinitionFsmTaskDn,
       "cfprApQosclassDefinitionFsmTaskRn": cfprApQosclassDefinitionFsmTaskRn,
       "cfprApQosclassDefinitionFsmTaskCompletion": cfprApQosclassDefinitionFsmTaskCompletion,
       "cfprApQosclassDefinitionFsmTaskFlags": cfprApQosclassDefinitionFsmTaskFlags,
       "cfprApQosclassDefinitionFsmTaskItem": cfprApQosclassDefinitionFsmTaskItem,
       "cfprApQosclassDefinitionFsmTaskSeqId": cfprApQosclassDefinitionFsmTaskSeqId,
       "cfprApQosclassEthBETable": cfprApQosclassEthBETable,
       "cfprApQosclassEthBEEntry": cfprApQosclassEthBEEntry,
       "cfprApQosclassEthBEInstanceId": cfprApQosclassEthBEInstanceId,
       "cfprApQosclassEthBEDn": cfprApQosclassEthBEDn,
       "cfprApQosclassEthBERn": cfprApQosclassEthBERn,
       "cfprApQosclassEthBEAdminState": cfprApQosclassEthBEAdminState,
       "cfprApQosclassEthBEBwPercent": cfprApQosclassEthBEBwPercent,
       "cfprApQosclassEthBECos": cfprApQosclassEthBECos,
       "cfprApQosclassEthBEDrop": cfprApQosclassEthBEDrop,
       "cfprApQosclassEthBEMtu": cfprApQosclassEthBEMtu,
       "cfprApQosclassEthBEMulticastOptimize": cfprApQosclassEthBEMulticastOptimize,
       "cfprApQosclassEthBEName": cfprApQosclassEthBEName,
       "cfprApQosclassEthBEPriority": cfprApQosclassEthBEPriority,
       "cfprApQosclassEthBEWeight": cfprApQosclassEthBEWeight,
       "cfprApQosclassEthClassifiedTable": cfprApQosclassEthClassifiedTable,
       "cfprApQosclassEthClassifiedEntry": cfprApQosclassEthClassifiedEntry,
       "cfprApQosclassEthClassifiedInstanceId": cfprApQosclassEthClassifiedInstanceId,
       "cfprApQosclassEthClassifiedDn": cfprApQosclassEthClassifiedDn,
       "cfprApQosclassEthClassifiedRn": cfprApQosclassEthClassifiedRn,
       "cfprApQosclassEthClassifiedAdminState": cfprApQosclassEthClassifiedAdminState,
       "cfprApQosclassEthClassifiedBwPercent": cfprApQosclassEthClassifiedBwPercent,
       "cfprApQosclassEthClassifiedCos": cfprApQosclassEthClassifiedCos,
       "cfprApQosclassEthClassifiedDrop": cfprApQosclassEthClassifiedDrop,
       "cfprApQosclassEthClassifiedMtu": cfprApQosclassEthClassifiedMtu,
       "cfprApQosclassEthClassifiedMulticastOptimize": cfprApQosclassEthClassifiedMulticastOptimize,
       "cfprApQosclassEthClassifiedName": cfprApQosclassEthClassifiedName,
       "cfprApQosclassEthClassifiedPriority": cfprApQosclassEthClassifiedPriority,
       "cfprApQosclassEthClassifiedWeight": cfprApQosclassEthClassifiedWeight,
       "cfprApQosclassFcTable": cfprApQosclassFcTable,
       "cfprApQosclassFcEntry": cfprApQosclassFcEntry,
       "cfprApQosclassFcInstanceId": cfprApQosclassFcInstanceId,
       "cfprApQosclassFcDn": cfprApQosclassFcDn,
       "cfprApQosclassFcRn": cfprApQosclassFcRn,
       "cfprApQosclassFcAdminState": cfprApQosclassFcAdminState,
       "cfprApQosclassFcBwPercent": cfprApQosclassFcBwPercent,
       "cfprApQosclassFcCos": cfprApQosclassFcCos,
       "cfprApQosclassFcDrop": cfprApQosclassFcDrop,
       "cfprApQosclassFcMtu": cfprApQosclassFcMtu,
       "cfprApQosclassFcName": cfprApQosclassFcName,
       "cfprApQosclassFcPriority": cfprApQosclassFcPriority,
       "cfprApQosclassFcWeight": cfprApQosclassFcWeight}
)
