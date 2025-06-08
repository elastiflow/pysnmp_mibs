# SNMP MIB module (CISCO-FIREPOWER-AP-EPQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-EPQOS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:14 2025
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
 CfprApEpqosDefinitionDelTaskFsmCurrentFsm,
 CfprApEpqosDefinitionDelTaskFsmStageName,
 CfprApEpqosDefinitionDelTaskFsmTaskItem,
 CfprApEpqosDefinitionFsmCurrentFsm,
 CfprApEpqosDefinitionFsmStageName,
 CfprApEpqosDefinitionFsmTaskItem,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApPolicyPolicyOwner,
 CfprApQosHostControl,
 CfprApQosPriority) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApEpqosDefinitionDelTaskFsmCurrentFsm",
    "CfprApEpqosDefinitionDelTaskFsmStageName",
    "CfprApEpqosDefinitionDelTaskFsmTaskItem",
    "CfprApEpqosDefinitionFsmCurrentFsm",
    "CfprApEpqosDefinitionFsmStageName",
    "CfprApEpqosDefinitionFsmTaskItem",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApPolicyPolicyOwner",
    "CfprApQosHostControl",
    "CfprApQosPriority")

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

cfprApEpqosObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApEpqosDefinitionTable_Object = MibTable
cfprApEpqosDefinitionTable = _CfprApEpqosDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1)
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionTable.setStatus("current")
_CfprApEpqosDefinitionEntry_Object = MibTableRow
cfprApEpqosDefinitionEntry = _CfprApEpqosDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1)
)
cfprApEpqosDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EPQOS-MIB", "cfprApEpqosDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionEntry.setStatus("current")
_CfprApEpqosDefinitionInstanceId_Type = CfprApManagedObjectId
_CfprApEpqosDefinitionInstanceId_Object = MibTableColumn
cfprApEpqosDefinitionInstanceId = _CfprApEpqosDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 1),
    _CfprApEpqosDefinitionInstanceId_Type()
)
cfprApEpqosDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionInstanceId.setStatus("current")
_CfprApEpqosDefinitionDn_Type = CfprApManagedObjectDn
_CfprApEpqosDefinitionDn_Object = MibTableColumn
cfprApEpqosDefinitionDn = _CfprApEpqosDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 2),
    _CfprApEpqosDefinitionDn_Type()
)
cfprApEpqosDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDn.setStatus("current")
_CfprApEpqosDefinitionRn_Type = SnmpAdminString
_CfprApEpqosDefinitionRn_Object = MibTableColumn
cfprApEpqosDefinitionRn = _CfprApEpqosDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 3),
    _CfprApEpqosDefinitionRn_Type()
)
cfprApEpqosDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionRn.setStatus("current")
_CfprApEpqosDefinitionDescr_Type = SnmpAdminString
_CfprApEpqosDefinitionDescr_Object = MibTableColumn
cfprApEpqosDefinitionDescr = _CfprApEpqosDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 4),
    _CfprApEpqosDefinitionDescr_Type()
)
cfprApEpqosDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDescr.setStatus("current")
_CfprApEpqosDefinitionFsmDescr_Type = SnmpAdminString
_CfprApEpqosDefinitionFsmDescr_Object = MibTableColumn
cfprApEpqosDefinitionFsmDescr = _CfprApEpqosDefinitionFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 5),
    _CfprApEpqosDefinitionFsmDescr_Type()
)
cfprApEpqosDefinitionFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmDescr.setStatus("current")
_CfprApEpqosDefinitionFsmPrev_Type = SnmpAdminString
_CfprApEpqosDefinitionFsmPrev_Object = MibTableColumn
cfprApEpqosDefinitionFsmPrev = _CfprApEpqosDefinitionFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 6),
    _CfprApEpqosDefinitionFsmPrev_Type()
)
cfprApEpqosDefinitionFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmPrev.setStatus("current")
_CfprApEpqosDefinitionFsmProgr_Type = Gauge32
_CfprApEpqosDefinitionFsmProgr_Object = MibTableColumn
cfprApEpqosDefinitionFsmProgr = _CfprApEpqosDefinitionFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 7),
    _CfprApEpqosDefinitionFsmProgr_Type()
)
cfprApEpqosDefinitionFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmProgr.setStatus("current")
_CfprApEpqosDefinitionFsmRmtInvErrCode_Type = Gauge32
_CfprApEpqosDefinitionFsmRmtInvErrCode_Object = MibTableColumn
cfprApEpqosDefinitionFsmRmtInvErrCode = _CfprApEpqosDefinitionFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 8),
    _CfprApEpqosDefinitionFsmRmtInvErrCode_Type()
)
cfprApEpqosDefinitionFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmRmtInvErrCode.setStatus("current")
_CfprApEpqosDefinitionFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApEpqosDefinitionFsmRmtInvErrDescr_Object = MibTableColumn
cfprApEpqosDefinitionFsmRmtInvErrDescr = _CfprApEpqosDefinitionFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 9),
    _CfprApEpqosDefinitionFsmRmtInvErrDescr_Type()
)
cfprApEpqosDefinitionFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmRmtInvErrDescr.setStatus("current")
_CfprApEpqosDefinitionFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApEpqosDefinitionFsmRmtInvRslt_Object = MibTableColumn
cfprApEpqosDefinitionFsmRmtInvRslt = _CfprApEpqosDefinitionFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 10),
    _CfprApEpqosDefinitionFsmRmtInvRslt_Type()
)
cfprApEpqosDefinitionFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmRmtInvRslt.setStatus("current")
_CfprApEpqosDefinitionFsmStageDescr_Type = SnmpAdminString
_CfprApEpqosDefinitionFsmStageDescr_Object = MibTableColumn
cfprApEpqosDefinitionFsmStageDescr = _CfprApEpqosDefinitionFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 11),
    _CfprApEpqosDefinitionFsmStageDescr_Type()
)
cfprApEpqosDefinitionFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStageDescr.setStatus("current")
_CfprApEpqosDefinitionFsmStamp_Type = DateAndTime
_CfprApEpqosDefinitionFsmStamp_Object = MibTableColumn
cfprApEpqosDefinitionFsmStamp = _CfprApEpqosDefinitionFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 12),
    _CfprApEpqosDefinitionFsmStamp_Type()
)
cfprApEpqosDefinitionFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStamp.setStatus("current")
_CfprApEpqosDefinitionFsmStatus_Type = SnmpAdminString
_CfprApEpqosDefinitionFsmStatus_Object = MibTableColumn
cfprApEpqosDefinitionFsmStatus = _CfprApEpqosDefinitionFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 13),
    _CfprApEpqosDefinitionFsmStatus_Type()
)
cfprApEpqosDefinitionFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStatus.setStatus("current")
_CfprApEpqosDefinitionFsmTry_Type = Gauge32
_CfprApEpqosDefinitionFsmTry_Object = MibTableColumn
cfprApEpqosDefinitionFsmTry = _CfprApEpqosDefinitionFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 14),
    _CfprApEpqosDefinitionFsmTry_Type()
)
cfprApEpqosDefinitionFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmTry.setStatus("current")
_CfprApEpqosDefinitionIntId_Type = SnmpAdminString
_CfprApEpqosDefinitionIntId_Object = MibTableColumn
cfprApEpqosDefinitionIntId = _CfprApEpqosDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 15),
    _CfprApEpqosDefinitionIntId_Type()
)
cfprApEpqosDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionIntId.setStatus("current")
_CfprApEpqosDefinitionName_Type = SnmpAdminString
_CfprApEpqosDefinitionName_Object = MibTableColumn
cfprApEpqosDefinitionName = _CfprApEpqosDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 16),
    _CfprApEpqosDefinitionName_Type()
)
cfprApEpqosDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionName.setStatus("current")
_CfprApEpqosDefinitionPolicyLevel_Type = Gauge32
_CfprApEpqosDefinitionPolicyLevel_Object = MibTableColumn
cfprApEpqosDefinitionPolicyLevel = _CfprApEpqosDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 17),
    _CfprApEpqosDefinitionPolicyLevel_Type()
)
cfprApEpqosDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionPolicyLevel.setStatus("current")
_CfprApEpqosDefinitionPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApEpqosDefinitionPolicyOwner_Object = MibTableColumn
cfprApEpqosDefinitionPolicyOwner = _CfprApEpqosDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 1, 1, 18),
    _CfprApEpqosDefinitionPolicyOwner_Type()
)
cfprApEpqosDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionPolicyOwner.setStatus("current")
_CfprApEpqosDefinitionDelTaskTable_Object = MibTable
cfprApEpqosDefinitionDelTaskTable = _CfprApEpqosDefinitionDelTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2)
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskTable.setStatus("current")
_CfprApEpqosDefinitionDelTaskEntry_Object = MibTableRow
cfprApEpqosDefinitionDelTaskEntry = _CfprApEpqosDefinitionDelTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1)
)
cfprApEpqosDefinitionDelTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EPQOS-MIB", "cfprApEpqosDefinitionDelTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskEntry.setStatus("current")
_CfprApEpqosDefinitionDelTaskInstanceId_Type = CfprApManagedObjectId
_CfprApEpqosDefinitionDelTaskInstanceId_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskInstanceId = _CfprApEpqosDefinitionDelTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 1),
    _CfprApEpqosDefinitionDelTaskInstanceId_Type()
)
cfprApEpqosDefinitionDelTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskInstanceId.setStatus("current")
_CfprApEpqosDefinitionDelTaskDn_Type = CfprApManagedObjectDn
_CfprApEpqosDefinitionDelTaskDn_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskDn = _CfprApEpqosDefinitionDelTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 2),
    _CfprApEpqosDefinitionDelTaskDn_Type()
)
cfprApEpqosDefinitionDelTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskDn.setStatus("current")
_CfprApEpqosDefinitionDelTaskRn_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskRn_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskRn = _CfprApEpqosDefinitionDelTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 3),
    _CfprApEpqosDefinitionDelTaskRn_Type()
)
cfprApEpqosDefinitionDelTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskRn.setStatus("current")
_CfprApEpqosDefinitionDelTaskDefDn_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskDefDn_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskDefDn = _CfprApEpqosDefinitionDelTaskDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 4),
    _CfprApEpqosDefinitionDelTaskDefDn_Type()
)
cfprApEpqosDefinitionDelTaskDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskDefDn.setStatus("current")
_CfprApEpqosDefinitionDelTaskDefIntId_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskDefIntId_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskDefIntId = _CfprApEpqosDefinitionDelTaskDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 5),
    _CfprApEpqosDefinitionDelTaskDefIntId_Type()
)
cfprApEpqosDefinitionDelTaskDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskDefIntId.setStatus("current")
_CfprApEpqosDefinitionDelTaskDescr_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskDescr_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskDescr = _CfprApEpqosDefinitionDelTaskDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 6),
    _CfprApEpqosDefinitionDelTaskDescr_Type()
)
cfprApEpqosDefinitionDelTaskDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskDescr.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmDescr_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskFsmDescr_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmDescr = _CfprApEpqosDefinitionDelTaskFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 7),
    _CfprApEpqosDefinitionDelTaskFsmDescr_Type()
)
cfprApEpqosDefinitionDelTaskFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmDescr.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmPrev_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskFsmPrev_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmPrev = _CfprApEpqosDefinitionDelTaskFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 8),
    _CfprApEpqosDefinitionDelTaskFsmPrev_Type()
)
cfprApEpqosDefinitionDelTaskFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmPrev.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmProgr_Type = Gauge32
_CfprApEpqosDefinitionDelTaskFsmProgr_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmProgr = _CfprApEpqosDefinitionDelTaskFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 9),
    _CfprApEpqosDefinitionDelTaskFsmProgr_Type()
)
cfprApEpqosDefinitionDelTaskFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmProgr.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmRmtInvErrCode_Type = Gauge32
_CfprApEpqosDefinitionDelTaskFsmRmtInvErrCode_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmRmtInvErrCode = _CfprApEpqosDefinitionDelTaskFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 10),
    _CfprApEpqosDefinitionDelTaskFsmRmtInvErrCode_Type()
)
cfprApEpqosDefinitionDelTaskFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmRmtInvErrCode.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskFsmRmtInvErrDescr_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmRmtInvErrDescr = _CfprApEpqosDefinitionDelTaskFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 11),
    _CfprApEpqosDefinitionDelTaskFsmRmtInvErrDescr_Type()
)
cfprApEpqosDefinitionDelTaskFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmRmtInvErrDescr.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApEpqosDefinitionDelTaskFsmRmtInvRslt_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmRmtInvRslt = _CfprApEpqosDefinitionDelTaskFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 12),
    _CfprApEpqosDefinitionDelTaskFsmRmtInvRslt_Type()
)
cfprApEpqosDefinitionDelTaskFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmRmtInvRslt.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStageDescr_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskFsmStageDescr_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmStageDescr = _CfprApEpqosDefinitionDelTaskFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 13),
    _CfprApEpqosDefinitionDelTaskFsmStageDescr_Type()
)
cfprApEpqosDefinitionDelTaskFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStageDescr.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStamp_Type = DateAndTime
_CfprApEpqosDefinitionDelTaskFsmStamp_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmStamp = _CfprApEpqosDefinitionDelTaskFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 14),
    _CfprApEpqosDefinitionDelTaskFsmStamp_Type()
)
cfprApEpqosDefinitionDelTaskFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStamp.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStatus_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskFsmStatus_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmStatus = _CfprApEpqosDefinitionDelTaskFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 15),
    _CfprApEpqosDefinitionDelTaskFsmStatus_Type()
)
cfprApEpqosDefinitionDelTaskFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStatus.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmTry_Type = Gauge32
_CfprApEpqosDefinitionDelTaskFsmTry_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmTry = _CfprApEpqosDefinitionDelTaskFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 16),
    _CfprApEpqosDefinitionDelTaskFsmTry_Type()
)
cfprApEpqosDefinitionDelTaskFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmTry.setStatus("current")
_CfprApEpqosDefinitionDelTaskIntId_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskIntId_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskIntId = _CfprApEpqosDefinitionDelTaskIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 17),
    _CfprApEpqosDefinitionDelTaskIntId_Type()
)
cfprApEpqosDefinitionDelTaskIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskIntId.setStatus("current")
_CfprApEpqosDefinitionDelTaskName_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskName_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskName = _CfprApEpqosDefinitionDelTaskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 18),
    _CfprApEpqosDefinitionDelTaskName_Type()
)
cfprApEpqosDefinitionDelTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskName.setStatus("current")
_CfprApEpqosDefinitionDelTaskPolicyLevel_Type = Gauge32
_CfprApEpqosDefinitionDelTaskPolicyLevel_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskPolicyLevel = _CfprApEpqosDefinitionDelTaskPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 19),
    _CfprApEpqosDefinitionDelTaskPolicyLevel_Type()
)
cfprApEpqosDefinitionDelTaskPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskPolicyLevel.setStatus("current")
_CfprApEpqosDefinitionDelTaskPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApEpqosDefinitionDelTaskPolicyOwner_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskPolicyOwner = _CfprApEpqosDefinitionDelTaskPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 2, 1, 20),
    _CfprApEpqosDefinitionDelTaskPolicyOwner_Type()
)
cfprApEpqosDefinitionDelTaskPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskPolicyOwner.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmTable_Object = MibTable
cfprApEpqosDefinitionDelTaskFsmTable = _CfprApEpqosDefinitionDelTaskFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3)
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmTable.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmEntry_Object = MibTableRow
cfprApEpqosDefinitionDelTaskFsmEntry = _CfprApEpqosDefinitionDelTaskFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3, 1)
)
cfprApEpqosDefinitionDelTaskFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EPQOS-MIB", "cfprApEpqosDefinitionDelTaskFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmEntry.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmInstanceId_Type = CfprApManagedObjectId
_CfprApEpqosDefinitionDelTaskFsmInstanceId_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmInstanceId = _CfprApEpqosDefinitionDelTaskFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3, 1, 1),
    _CfprApEpqosDefinitionDelTaskFsmInstanceId_Type()
)
cfprApEpqosDefinitionDelTaskFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmInstanceId.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmDn_Type = CfprApManagedObjectDn
_CfprApEpqosDefinitionDelTaskFsmDn_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmDn = _CfprApEpqosDefinitionDelTaskFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3, 1, 2),
    _CfprApEpqosDefinitionDelTaskFsmDn_Type()
)
cfprApEpqosDefinitionDelTaskFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmDn.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmRn_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskFsmRn_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmRn = _CfprApEpqosDefinitionDelTaskFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3, 1, 3),
    _CfprApEpqosDefinitionDelTaskFsmRn_Type()
)
cfprApEpqosDefinitionDelTaskFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmRn.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmCompletionTime_Type = DateAndTime
_CfprApEpqosDefinitionDelTaskFsmCompletionTime_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmCompletionTime = _CfprApEpqosDefinitionDelTaskFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3, 1, 4),
    _CfprApEpqosDefinitionDelTaskFsmCompletionTime_Type()
)
cfprApEpqosDefinitionDelTaskFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmCompletionTime.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmCurrentFsm_Type = CfprApEpqosDefinitionDelTaskFsmCurrentFsm
_CfprApEpqosDefinitionDelTaskFsmCurrentFsm_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmCurrentFsm = _CfprApEpqosDefinitionDelTaskFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3, 1, 5),
    _CfprApEpqosDefinitionDelTaskFsmCurrentFsm_Type()
)
cfprApEpqosDefinitionDelTaskFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmCurrentFsm.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmDescrData_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskFsmDescrData_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmDescrData = _CfprApEpqosDefinitionDelTaskFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3, 1, 6),
    _CfprApEpqosDefinitionDelTaskFsmDescrData_Type()
)
cfprApEpqosDefinitionDelTaskFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmDescrData.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApEpqosDefinitionDelTaskFsmFsmStatus_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmFsmStatus = _CfprApEpqosDefinitionDelTaskFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3, 1, 7),
    _CfprApEpqosDefinitionDelTaskFsmFsmStatus_Type()
)
cfprApEpqosDefinitionDelTaskFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmFsmStatus.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmProgress_Type = Gauge32
_CfprApEpqosDefinitionDelTaskFsmProgress_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmProgress = _CfprApEpqosDefinitionDelTaskFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3, 1, 8),
    _CfprApEpqosDefinitionDelTaskFsmProgress_Type()
)
cfprApEpqosDefinitionDelTaskFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmProgress.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmRmtErrCode_Type = Gauge32
_CfprApEpqosDefinitionDelTaskFsmRmtErrCode_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmRmtErrCode = _CfprApEpqosDefinitionDelTaskFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3, 1, 9),
    _CfprApEpqosDefinitionDelTaskFsmRmtErrCode_Type()
)
cfprApEpqosDefinitionDelTaskFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmRmtErrCode.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmRmtErrDescr_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskFsmRmtErrDescr_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmRmtErrDescr = _CfprApEpqosDefinitionDelTaskFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3, 1, 10),
    _CfprApEpqosDefinitionDelTaskFsmRmtErrDescr_Type()
)
cfprApEpqosDefinitionDelTaskFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmRmtErrDescr.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApEpqosDefinitionDelTaskFsmRmtRslt_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmRmtRslt = _CfprApEpqosDefinitionDelTaskFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 3, 1, 11),
    _CfprApEpqosDefinitionDelTaskFsmRmtRslt_Type()
)
cfprApEpqosDefinitionDelTaskFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmRmtRslt.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStageTable_Object = MibTable
cfprApEpqosDefinitionDelTaskFsmStageTable = _CfprApEpqosDefinitionDelTaskFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 4)
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStageTable.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStageEntry_Object = MibTableRow
cfprApEpqosDefinitionDelTaskFsmStageEntry = _CfprApEpqosDefinitionDelTaskFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 4, 1)
)
cfprApEpqosDefinitionDelTaskFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EPQOS-MIB", "cfprApEpqosDefinitionDelTaskFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStageEntry.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApEpqosDefinitionDelTaskFsmStageInstanceId_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmStageInstanceId = _CfprApEpqosDefinitionDelTaskFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 4, 1, 1),
    _CfprApEpqosDefinitionDelTaskFsmStageInstanceId_Type()
)
cfprApEpqosDefinitionDelTaskFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStageInstanceId.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStageDn_Type = CfprApManagedObjectDn
_CfprApEpqosDefinitionDelTaskFsmStageDn_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmStageDn = _CfprApEpqosDefinitionDelTaskFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 4, 1, 2),
    _CfprApEpqosDefinitionDelTaskFsmStageDn_Type()
)
cfprApEpqosDefinitionDelTaskFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStageDn.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStageRn_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskFsmStageRn_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmStageRn = _CfprApEpqosDefinitionDelTaskFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 4, 1, 3),
    _CfprApEpqosDefinitionDelTaskFsmStageRn_Type()
)
cfprApEpqosDefinitionDelTaskFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStageRn.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStageDescrData_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskFsmStageDescrData_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmStageDescrData = _CfprApEpqosDefinitionDelTaskFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 4, 1, 4),
    _CfprApEpqosDefinitionDelTaskFsmStageDescrData_Type()
)
cfprApEpqosDefinitionDelTaskFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStageDescrData.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStageLastUpdateTime_Type = DateAndTime
_CfprApEpqosDefinitionDelTaskFsmStageLastUpdateTime_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmStageLastUpdateTime = _CfprApEpqosDefinitionDelTaskFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 4, 1, 5),
    _CfprApEpqosDefinitionDelTaskFsmStageLastUpdateTime_Type()
)
cfprApEpqosDefinitionDelTaskFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStageLastUpdateTime.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStageName_Type = CfprApEpqosDefinitionDelTaskFsmStageName
_CfprApEpqosDefinitionDelTaskFsmStageName_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmStageName = _CfprApEpqosDefinitionDelTaskFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 4, 1, 6),
    _CfprApEpqosDefinitionDelTaskFsmStageName_Type()
)
cfprApEpqosDefinitionDelTaskFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStageName.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStageOrder_Type = Gauge32
_CfprApEpqosDefinitionDelTaskFsmStageOrder_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmStageOrder = _CfprApEpqosDefinitionDelTaskFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 4, 1, 7),
    _CfprApEpqosDefinitionDelTaskFsmStageOrder_Type()
)
cfprApEpqosDefinitionDelTaskFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStageOrder.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStageRetry_Type = Gauge32
_CfprApEpqosDefinitionDelTaskFsmStageRetry_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmStageRetry = _CfprApEpqosDefinitionDelTaskFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 4, 1, 8),
    _CfprApEpqosDefinitionDelTaskFsmStageRetry_Type()
)
cfprApEpqosDefinitionDelTaskFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStageRetry.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApEpqosDefinitionDelTaskFsmStageStageStatus_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmStageStageStatus = _CfprApEpqosDefinitionDelTaskFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 4, 1, 9),
    _CfprApEpqosDefinitionDelTaskFsmStageStageStatus_Type()
)
cfprApEpqosDefinitionDelTaskFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmStageStageStatus.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmTaskTable_Object = MibTable
cfprApEpqosDefinitionDelTaskFsmTaskTable = _CfprApEpqosDefinitionDelTaskFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 5)
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmTaskTable.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmTaskEntry_Object = MibTableRow
cfprApEpqosDefinitionDelTaskFsmTaskEntry = _CfprApEpqosDefinitionDelTaskFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 5, 1)
)
cfprApEpqosDefinitionDelTaskFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EPQOS-MIB", "cfprApEpqosDefinitionDelTaskFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmTaskEntry.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApEpqosDefinitionDelTaskFsmTaskInstanceId_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmTaskInstanceId = _CfprApEpqosDefinitionDelTaskFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 5, 1, 1),
    _CfprApEpqosDefinitionDelTaskFsmTaskInstanceId_Type()
)
cfprApEpqosDefinitionDelTaskFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmTaskInstanceId.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApEpqosDefinitionDelTaskFsmTaskDn_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmTaskDn = _CfprApEpqosDefinitionDelTaskFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 5, 1, 2),
    _CfprApEpqosDefinitionDelTaskFsmTaskDn_Type()
)
cfprApEpqosDefinitionDelTaskFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmTaskDn.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmTaskRn_Type = SnmpAdminString
_CfprApEpqosDefinitionDelTaskFsmTaskRn_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmTaskRn = _CfprApEpqosDefinitionDelTaskFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 5, 1, 3),
    _CfprApEpqosDefinitionDelTaskFsmTaskRn_Type()
)
cfprApEpqosDefinitionDelTaskFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmTaskRn.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApEpqosDefinitionDelTaskFsmTaskCompletion_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmTaskCompletion = _CfprApEpqosDefinitionDelTaskFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 5, 1, 4),
    _CfprApEpqosDefinitionDelTaskFsmTaskCompletion_Type()
)
cfprApEpqosDefinitionDelTaskFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmTaskCompletion.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmTaskFlags_Type = CfprApFsmFlags
_CfprApEpqosDefinitionDelTaskFsmTaskFlags_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmTaskFlags = _CfprApEpqosDefinitionDelTaskFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 5, 1, 5),
    _CfprApEpqosDefinitionDelTaskFsmTaskFlags_Type()
)
cfprApEpqosDefinitionDelTaskFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmTaskFlags.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmTaskItem_Type = CfprApEpqosDefinitionDelTaskFsmTaskItem
_CfprApEpqosDefinitionDelTaskFsmTaskItem_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmTaskItem = _CfprApEpqosDefinitionDelTaskFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 5, 1, 6),
    _CfprApEpqosDefinitionDelTaskFsmTaskItem_Type()
)
cfprApEpqosDefinitionDelTaskFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmTaskItem.setStatus("current")
_CfprApEpqosDefinitionDelTaskFsmTaskSeqId_Type = Gauge32
_CfprApEpqosDefinitionDelTaskFsmTaskSeqId_Object = MibTableColumn
cfprApEpqosDefinitionDelTaskFsmTaskSeqId = _CfprApEpqosDefinitionDelTaskFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 5, 1, 7),
    _CfprApEpqosDefinitionDelTaskFsmTaskSeqId_Type()
)
cfprApEpqosDefinitionDelTaskFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionDelTaskFsmTaskSeqId.setStatus("current")
_CfprApEpqosDefinitionFsmTable_Object = MibTable
cfprApEpqosDefinitionFsmTable = _CfprApEpqosDefinitionFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6)
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmTable.setStatus("current")
_CfprApEpqosDefinitionFsmEntry_Object = MibTableRow
cfprApEpqosDefinitionFsmEntry = _CfprApEpqosDefinitionFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6, 1)
)
cfprApEpqosDefinitionFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EPQOS-MIB", "cfprApEpqosDefinitionFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmEntry.setStatus("current")
_CfprApEpqosDefinitionFsmInstanceId_Type = CfprApManagedObjectId
_CfprApEpqosDefinitionFsmInstanceId_Object = MibTableColumn
cfprApEpqosDefinitionFsmInstanceId = _CfprApEpqosDefinitionFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6, 1, 1),
    _CfprApEpqosDefinitionFsmInstanceId_Type()
)
cfprApEpqosDefinitionFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmInstanceId.setStatus("current")
_CfprApEpqosDefinitionFsmDn_Type = CfprApManagedObjectDn
_CfprApEpqosDefinitionFsmDn_Object = MibTableColumn
cfprApEpqosDefinitionFsmDn = _CfprApEpqosDefinitionFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6, 1, 2),
    _CfprApEpqosDefinitionFsmDn_Type()
)
cfprApEpqosDefinitionFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmDn.setStatus("current")
_CfprApEpqosDefinitionFsmRn_Type = SnmpAdminString
_CfprApEpqosDefinitionFsmRn_Object = MibTableColumn
cfprApEpqosDefinitionFsmRn = _CfprApEpqosDefinitionFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6, 1, 3),
    _CfprApEpqosDefinitionFsmRn_Type()
)
cfprApEpqosDefinitionFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmRn.setStatus("current")
_CfprApEpqosDefinitionFsmCompletionTime_Type = DateAndTime
_CfprApEpqosDefinitionFsmCompletionTime_Object = MibTableColumn
cfprApEpqosDefinitionFsmCompletionTime = _CfprApEpqosDefinitionFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6, 1, 4),
    _CfprApEpqosDefinitionFsmCompletionTime_Type()
)
cfprApEpqosDefinitionFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmCompletionTime.setStatus("current")
_CfprApEpqosDefinitionFsmCurrentFsm_Type = CfprApEpqosDefinitionFsmCurrentFsm
_CfprApEpqosDefinitionFsmCurrentFsm_Object = MibTableColumn
cfprApEpqosDefinitionFsmCurrentFsm = _CfprApEpqosDefinitionFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6, 1, 5),
    _CfprApEpqosDefinitionFsmCurrentFsm_Type()
)
cfprApEpqosDefinitionFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmCurrentFsm.setStatus("current")
_CfprApEpqosDefinitionFsmDescrData_Type = SnmpAdminString
_CfprApEpqosDefinitionFsmDescrData_Object = MibTableColumn
cfprApEpqosDefinitionFsmDescrData = _CfprApEpqosDefinitionFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6, 1, 6),
    _CfprApEpqosDefinitionFsmDescrData_Type()
)
cfprApEpqosDefinitionFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmDescrData.setStatus("current")
_CfprApEpqosDefinitionFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApEpqosDefinitionFsmFsmStatus_Object = MibTableColumn
cfprApEpqosDefinitionFsmFsmStatus = _CfprApEpqosDefinitionFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6, 1, 7),
    _CfprApEpqosDefinitionFsmFsmStatus_Type()
)
cfprApEpqosDefinitionFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmFsmStatus.setStatus("current")
_CfprApEpqosDefinitionFsmProgress_Type = Gauge32
_CfprApEpqosDefinitionFsmProgress_Object = MibTableColumn
cfprApEpqosDefinitionFsmProgress = _CfprApEpqosDefinitionFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6, 1, 8),
    _CfprApEpqosDefinitionFsmProgress_Type()
)
cfprApEpqosDefinitionFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmProgress.setStatus("current")
_CfprApEpqosDefinitionFsmRmtErrCode_Type = Gauge32
_CfprApEpqosDefinitionFsmRmtErrCode_Object = MibTableColumn
cfprApEpqosDefinitionFsmRmtErrCode = _CfprApEpqosDefinitionFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6, 1, 9),
    _CfprApEpqosDefinitionFsmRmtErrCode_Type()
)
cfprApEpqosDefinitionFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmRmtErrCode.setStatus("current")
_CfprApEpqosDefinitionFsmRmtErrDescr_Type = SnmpAdminString
_CfprApEpqosDefinitionFsmRmtErrDescr_Object = MibTableColumn
cfprApEpqosDefinitionFsmRmtErrDescr = _CfprApEpqosDefinitionFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6, 1, 10),
    _CfprApEpqosDefinitionFsmRmtErrDescr_Type()
)
cfprApEpqosDefinitionFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmRmtErrDescr.setStatus("current")
_CfprApEpqosDefinitionFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApEpqosDefinitionFsmRmtRslt_Object = MibTableColumn
cfprApEpqosDefinitionFsmRmtRslt = _CfprApEpqosDefinitionFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 6, 1, 11),
    _CfprApEpqosDefinitionFsmRmtRslt_Type()
)
cfprApEpqosDefinitionFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmRmtRslt.setStatus("current")
_CfprApEpqosDefinitionFsmStageTable_Object = MibTable
cfprApEpqosDefinitionFsmStageTable = _CfprApEpqosDefinitionFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 7)
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStageTable.setStatus("current")
_CfprApEpqosDefinitionFsmStageEntry_Object = MibTableRow
cfprApEpqosDefinitionFsmStageEntry = _CfprApEpqosDefinitionFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 7, 1)
)
cfprApEpqosDefinitionFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EPQOS-MIB", "cfprApEpqosDefinitionFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStageEntry.setStatus("current")
_CfprApEpqosDefinitionFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApEpqosDefinitionFsmStageInstanceId_Object = MibTableColumn
cfprApEpqosDefinitionFsmStageInstanceId = _CfprApEpqosDefinitionFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 7, 1, 1),
    _CfprApEpqosDefinitionFsmStageInstanceId_Type()
)
cfprApEpqosDefinitionFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStageInstanceId.setStatus("current")
_CfprApEpqosDefinitionFsmStageDn_Type = CfprApManagedObjectDn
_CfprApEpqosDefinitionFsmStageDn_Object = MibTableColumn
cfprApEpqosDefinitionFsmStageDn = _CfprApEpqosDefinitionFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 7, 1, 2),
    _CfprApEpqosDefinitionFsmStageDn_Type()
)
cfprApEpqosDefinitionFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStageDn.setStatus("current")
_CfprApEpqosDefinitionFsmStageRn_Type = SnmpAdminString
_CfprApEpqosDefinitionFsmStageRn_Object = MibTableColumn
cfprApEpqosDefinitionFsmStageRn = _CfprApEpqosDefinitionFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 7, 1, 3),
    _CfprApEpqosDefinitionFsmStageRn_Type()
)
cfprApEpqosDefinitionFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStageRn.setStatus("current")
_CfprApEpqosDefinitionFsmStageDescrData_Type = SnmpAdminString
_CfprApEpqosDefinitionFsmStageDescrData_Object = MibTableColumn
cfprApEpqosDefinitionFsmStageDescrData = _CfprApEpqosDefinitionFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 7, 1, 4),
    _CfprApEpqosDefinitionFsmStageDescrData_Type()
)
cfprApEpqosDefinitionFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStageDescrData.setStatus("current")
_CfprApEpqosDefinitionFsmStageLastUpdateTime_Type = DateAndTime
_CfprApEpqosDefinitionFsmStageLastUpdateTime_Object = MibTableColumn
cfprApEpqosDefinitionFsmStageLastUpdateTime = _CfprApEpqosDefinitionFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 7, 1, 5),
    _CfprApEpqosDefinitionFsmStageLastUpdateTime_Type()
)
cfprApEpqosDefinitionFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStageLastUpdateTime.setStatus("current")
_CfprApEpqosDefinitionFsmStageName_Type = CfprApEpqosDefinitionFsmStageName
_CfprApEpqosDefinitionFsmStageName_Object = MibTableColumn
cfprApEpqosDefinitionFsmStageName = _CfprApEpqosDefinitionFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 7, 1, 6),
    _CfprApEpqosDefinitionFsmStageName_Type()
)
cfprApEpqosDefinitionFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStageName.setStatus("current")
_CfprApEpqosDefinitionFsmStageOrder_Type = Gauge32
_CfprApEpqosDefinitionFsmStageOrder_Object = MibTableColumn
cfprApEpqosDefinitionFsmStageOrder = _CfprApEpqosDefinitionFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 7, 1, 7),
    _CfprApEpqosDefinitionFsmStageOrder_Type()
)
cfprApEpqosDefinitionFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStageOrder.setStatus("current")
_CfprApEpqosDefinitionFsmStageRetry_Type = Gauge32
_CfprApEpqosDefinitionFsmStageRetry_Object = MibTableColumn
cfprApEpqosDefinitionFsmStageRetry = _CfprApEpqosDefinitionFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 7, 1, 8),
    _CfprApEpqosDefinitionFsmStageRetry_Type()
)
cfprApEpqosDefinitionFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStageRetry.setStatus("current")
_CfprApEpqosDefinitionFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApEpqosDefinitionFsmStageStageStatus_Object = MibTableColumn
cfprApEpqosDefinitionFsmStageStageStatus = _CfprApEpqosDefinitionFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 7, 1, 9),
    _CfprApEpqosDefinitionFsmStageStageStatus_Type()
)
cfprApEpqosDefinitionFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmStageStageStatus.setStatus("current")
_CfprApEpqosDefinitionFsmTaskTable_Object = MibTable
cfprApEpqosDefinitionFsmTaskTable = _CfprApEpqosDefinitionFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 8)
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmTaskTable.setStatus("current")
_CfprApEpqosDefinitionFsmTaskEntry_Object = MibTableRow
cfprApEpqosDefinitionFsmTaskEntry = _CfprApEpqosDefinitionFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 8, 1)
)
cfprApEpqosDefinitionFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EPQOS-MIB", "cfprApEpqosDefinitionFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmTaskEntry.setStatus("current")
_CfprApEpqosDefinitionFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApEpqosDefinitionFsmTaskInstanceId_Object = MibTableColumn
cfprApEpqosDefinitionFsmTaskInstanceId = _CfprApEpqosDefinitionFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 8, 1, 1),
    _CfprApEpqosDefinitionFsmTaskInstanceId_Type()
)
cfprApEpqosDefinitionFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmTaskInstanceId.setStatus("current")
_CfprApEpqosDefinitionFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApEpqosDefinitionFsmTaskDn_Object = MibTableColumn
cfprApEpqosDefinitionFsmTaskDn = _CfprApEpqosDefinitionFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 8, 1, 2),
    _CfprApEpqosDefinitionFsmTaskDn_Type()
)
cfprApEpqosDefinitionFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmTaskDn.setStatus("current")
_CfprApEpqosDefinitionFsmTaskRn_Type = SnmpAdminString
_CfprApEpqosDefinitionFsmTaskRn_Object = MibTableColumn
cfprApEpqosDefinitionFsmTaskRn = _CfprApEpqosDefinitionFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 8, 1, 3),
    _CfprApEpqosDefinitionFsmTaskRn_Type()
)
cfprApEpqosDefinitionFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmTaskRn.setStatus("current")
_CfprApEpqosDefinitionFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApEpqosDefinitionFsmTaskCompletion_Object = MibTableColumn
cfprApEpqosDefinitionFsmTaskCompletion = _CfprApEpqosDefinitionFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 8, 1, 4),
    _CfprApEpqosDefinitionFsmTaskCompletion_Type()
)
cfprApEpqosDefinitionFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmTaskCompletion.setStatus("current")
_CfprApEpqosDefinitionFsmTaskFlags_Type = CfprApFsmFlags
_CfprApEpqosDefinitionFsmTaskFlags_Object = MibTableColumn
cfprApEpqosDefinitionFsmTaskFlags = _CfprApEpqosDefinitionFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 8, 1, 5),
    _CfprApEpqosDefinitionFsmTaskFlags_Type()
)
cfprApEpqosDefinitionFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmTaskFlags.setStatus("current")
_CfprApEpqosDefinitionFsmTaskItem_Type = CfprApEpqosDefinitionFsmTaskItem
_CfprApEpqosDefinitionFsmTaskItem_Object = MibTableColumn
cfprApEpqosDefinitionFsmTaskItem = _CfprApEpqosDefinitionFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 8, 1, 6),
    _CfprApEpqosDefinitionFsmTaskItem_Type()
)
cfprApEpqosDefinitionFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmTaskItem.setStatus("current")
_CfprApEpqosDefinitionFsmTaskSeqId_Type = Gauge32
_CfprApEpqosDefinitionFsmTaskSeqId_Object = MibTableColumn
cfprApEpqosDefinitionFsmTaskSeqId = _CfprApEpqosDefinitionFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 8, 1, 7),
    _CfprApEpqosDefinitionFsmTaskSeqId_Type()
)
cfprApEpqosDefinitionFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosDefinitionFsmTaskSeqId.setStatus("current")
_CfprApEpqosEgressTable_Object = MibTable
cfprApEpqosEgressTable = _CfprApEpqosEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 9)
)
if mibBuilder.loadTexts:
    cfprApEpqosEgressTable.setStatus("current")
_CfprApEpqosEgressEntry_Object = MibTableRow
cfprApEpqosEgressEntry = _CfprApEpqosEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 9, 1)
)
cfprApEpqosEgressEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EPQOS-MIB", "cfprApEpqosEgressInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEpqosEgressEntry.setStatus("current")
_CfprApEpqosEgressInstanceId_Type = CfprApManagedObjectId
_CfprApEpqosEgressInstanceId_Object = MibTableColumn
cfprApEpqosEgressInstanceId = _CfprApEpqosEgressInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 9, 1, 1),
    _CfprApEpqosEgressInstanceId_Type()
)
cfprApEpqosEgressInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEpqosEgressInstanceId.setStatus("current")
_CfprApEpqosEgressDn_Type = CfprApManagedObjectDn
_CfprApEpqosEgressDn_Object = MibTableColumn
cfprApEpqosEgressDn = _CfprApEpqosEgressDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 9, 1, 2),
    _CfprApEpqosEgressDn_Type()
)
cfprApEpqosEgressDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosEgressDn.setStatus("current")
_CfprApEpqosEgressRn_Type = SnmpAdminString
_CfprApEpqosEgressRn_Object = MibTableColumn
cfprApEpqosEgressRn = _CfprApEpqosEgressRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 9, 1, 3),
    _CfprApEpqosEgressRn_Type()
)
cfprApEpqosEgressRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosEgressRn.setStatus("current")
_CfprApEpqosEgressBurst_Type = Gauge32
_CfprApEpqosEgressBurst_Object = MibTableColumn
cfprApEpqosEgressBurst = _CfprApEpqosEgressBurst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 9, 1, 4),
    _CfprApEpqosEgressBurst_Type()
)
cfprApEpqosEgressBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosEgressBurst.setStatus("current")
_CfprApEpqosEgressHostControl_Type = CfprApQosHostControl
_CfprApEpqosEgressHostControl_Object = MibTableColumn
cfprApEpqosEgressHostControl = _CfprApEpqosEgressHostControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 9, 1, 5),
    _CfprApEpqosEgressHostControl_Type()
)
cfprApEpqosEgressHostControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosEgressHostControl.setStatus("current")
_CfprApEpqosEgressName_Type = SnmpAdminString
_CfprApEpqosEgressName_Object = MibTableColumn
cfprApEpqosEgressName = _CfprApEpqosEgressName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 9, 1, 6),
    _CfprApEpqosEgressName_Type()
)
cfprApEpqosEgressName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosEgressName.setStatus("current")
_CfprApEpqosEgressOperPrio_Type = CfprApQosPriority
_CfprApEpqosEgressOperPrio_Object = MibTableColumn
cfprApEpqosEgressOperPrio = _CfprApEpqosEgressOperPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 9, 1, 7),
    _CfprApEpqosEgressOperPrio_Type()
)
cfprApEpqosEgressOperPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosEgressOperPrio.setStatus("current")
_CfprApEpqosEgressPrio_Type = CfprApQosPriority
_CfprApEpqosEgressPrio_Object = MibTableColumn
cfprApEpqosEgressPrio = _CfprApEpqosEgressPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 9, 1, 8),
    _CfprApEpqosEgressPrio_Type()
)
cfprApEpqosEgressPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosEgressPrio.setStatus("current")
_CfprApEpqosEgressRate_Type = Gauge32
_CfprApEpqosEgressRate_Object = MibTableColumn
cfprApEpqosEgressRate = _CfprApEpqosEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 19, 9, 1, 9),
    _CfprApEpqosEgressRate_Type()
)
cfprApEpqosEgressRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEpqosEgressRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-EPQOS-MIB",
    **{"cfprApEpqosObjects": cfprApEpqosObjects,
       "cfprApEpqosDefinitionTable": cfprApEpqosDefinitionTable,
       "cfprApEpqosDefinitionEntry": cfprApEpqosDefinitionEntry,
       "cfprApEpqosDefinitionInstanceId": cfprApEpqosDefinitionInstanceId,
       "cfprApEpqosDefinitionDn": cfprApEpqosDefinitionDn,
       "cfprApEpqosDefinitionRn": cfprApEpqosDefinitionRn,
       "cfprApEpqosDefinitionDescr": cfprApEpqosDefinitionDescr,
       "cfprApEpqosDefinitionFsmDescr": cfprApEpqosDefinitionFsmDescr,
       "cfprApEpqosDefinitionFsmPrev": cfprApEpqosDefinitionFsmPrev,
       "cfprApEpqosDefinitionFsmProgr": cfprApEpqosDefinitionFsmProgr,
       "cfprApEpqosDefinitionFsmRmtInvErrCode": cfprApEpqosDefinitionFsmRmtInvErrCode,
       "cfprApEpqosDefinitionFsmRmtInvErrDescr": cfprApEpqosDefinitionFsmRmtInvErrDescr,
       "cfprApEpqosDefinitionFsmRmtInvRslt": cfprApEpqosDefinitionFsmRmtInvRslt,
       "cfprApEpqosDefinitionFsmStageDescr": cfprApEpqosDefinitionFsmStageDescr,
       "cfprApEpqosDefinitionFsmStamp": cfprApEpqosDefinitionFsmStamp,
       "cfprApEpqosDefinitionFsmStatus": cfprApEpqosDefinitionFsmStatus,
       "cfprApEpqosDefinitionFsmTry": cfprApEpqosDefinitionFsmTry,
       "cfprApEpqosDefinitionIntId": cfprApEpqosDefinitionIntId,
       "cfprApEpqosDefinitionName": cfprApEpqosDefinitionName,
       "cfprApEpqosDefinitionPolicyLevel": cfprApEpqosDefinitionPolicyLevel,
       "cfprApEpqosDefinitionPolicyOwner": cfprApEpqosDefinitionPolicyOwner,
       "cfprApEpqosDefinitionDelTaskTable": cfprApEpqosDefinitionDelTaskTable,
       "cfprApEpqosDefinitionDelTaskEntry": cfprApEpqosDefinitionDelTaskEntry,
       "cfprApEpqosDefinitionDelTaskInstanceId": cfprApEpqosDefinitionDelTaskInstanceId,
       "cfprApEpqosDefinitionDelTaskDn": cfprApEpqosDefinitionDelTaskDn,
       "cfprApEpqosDefinitionDelTaskRn": cfprApEpqosDefinitionDelTaskRn,
       "cfprApEpqosDefinitionDelTaskDefDn": cfprApEpqosDefinitionDelTaskDefDn,
       "cfprApEpqosDefinitionDelTaskDefIntId": cfprApEpqosDefinitionDelTaskDefIntId,
       "cfprApEpqosDefinitionDelTaskDescr": cfprApEpqosDefinitionDelTaskDescr,
       "cfprApEpqosDefinitionDelTaskFsmDescr": cfprApEpqosDefinitionDelTaskFsmDescr,
       "cfprApEpqosDefinitionDelTaskFsmPrev": cfprApEpqosDefinitionDelTaskFsmPrev,
       "cfprApEpqosDefinitionDelTaskFsmProgr": cfprApEpqosDefinitionDelTaskFsmProgr,
       "cfprApEpqosDefinitionDelTaskFsmRmtInvErrCode": cfprApEpqosDefinitionDelTaskFsmRmtInvErrCode,
       "cfprApEpqosDefinitionDelTaskFsmRmtInvErrDescr": cfprApEpqosDefinitionDelTaskFsmRmtInvErrDescr,
       "cfprApEpqosDefinitionDelTaskFsmRmtInvRslt": cfprApEpqosDefinitionDelTaskFsmRmtInvRslt,
       "cfprApEpqosDefinitionDelTaskFsmStageDescr": cfprApEpqosDefinitionDelTaskFsmStageDescr,
       "cfprApEpqosDefinitionDelTaskFsmStamp": cfprApEpqosDefinitionDelTaskFsmStamp,
       "cfprApEpqosDefinitionDelTaskFsmStatus": cfprApEpqosDefinitionDelTaskFsmStatus,
       "cfprApEpqosDefinitionDelTaskFsmTry": cfprApEpqosDefinitionDelTaskFsmTry,
       "cfprApEpqosDefinitionDelTaskIntId": cfprApEpqosDefinitionDelTaskIntId,
       "cfprApEpqosDefinitionDelTaskName": cfprApEpqosDefinitionDelTaskName,
       "cfprApEpqosDefinitionDelTaskPolicyLevel": cfprApEpqosDefinitionDelTaskPolicyLevel,
       "cfprApEpqosDefinitionDelTaskPolicyOwner": cfprApEpqosDefinitionDelTaskPolicyOwner,
       "cfprApEpqosDefinitionDelTaskFsmTable": cfprApEpqosDefinitionDelTaskFsmTable,
       "cfprApEpqosDefinitionDelTaskFsmEntry": cfprApEpqosDefinitionDelTaskFsmEntry,
       "cfprApEpqosDefinitionDelTaskFsmInstanceId": cfprApEpqosDefinitionDelTaskFsmInstanceId,
       "cfprApEpqosDefinitionDelTaskFsmDn": cfprApEpqosDefinitionDelTaskFsmDn,
       "cfprApEpqosDefinitionDelTaskFsmRn": cfprApEpqosDefinitionDelTaskFsmRn,
       "cfprApEpqosDefinitionDelTaskFsmCompletionTime": cfprApEpqosDefinitionDelTaskFsmCompletionTime,
       "cfprApEpqosDefinitionDelTaskFsmCurrentFsm": cfprApEpqosDefinitionDelTaskFsmCurrentFsm,
       "cfprApEpqosDefinitionDelTaskFsmDescrData": cfprApEpqosDefinitionDelTaskFsmDescrData,
       "cfprApEpqosDefinitionDelTaskFsmFsmStatus": cfprApEpqosDefinitionDelTaskFsmFsmStatus,
       "cfprApEpqosDefinitionDelTaskFsmProgress": cfprApEpqosDefinitionDelTaskFsmProgress,
       "cfprApEpqosDefinitionDelTaskFsmRmtErrCode": cfprApEpqosDefinitionDelTaskFsmRmtErrCode,
       "cfprApEpqosDefinitionDelTaskFsmRmtErrDescr": cfprApEpqosDefinitionDelTaskFsmRmtErrDescr,
       "cfprApEpqosDefinitionDelTaskFsmRmtRslt": cfprApEpqosDefinitionDelTaskFsmRmtRslt,
       "cfprApEpqosDefinitionDelTaskFsmStageTable": cfprApEpqosDefinitionDelTaskFsmStageTable,
       "cfprApEpqosDefinitionDelTaskFsmStageEntry": cfprApEpqosDefinitionDelTaskFsmStageEntry,
       "cfprApEpqosDefinitionDelTaskFsmStageInstanceId": cfprApEpqosDefinitionDelTaskFsmStageInstanceId,
       "cfprApEpqosDefinitionDelTaskFsmStageDn": cfprApEpqosDefinitionDelTaskFsmStageDn,
       "cfprApEpqosDefinitionDelTaskFsmStageRn": cfprApEpqosDefinitionDelTaskFsmStageRn,
       "cfprApEpqosDefinitionDelTaskFsmStageDescrData": cfprApEpqosDefinitionDelTaskFsmStageDescrData,
       "cfprApEpqosDefinitionDelTaskFsmStageLastUpdateTime": cfprApEpqosDefinitionDelTaskFsmStageLastUpdateTime,
       "cfprApEpqosDefinitionDelTaskFsmStageName": cfprApEpqosDefinitionDelTaskFsmStageName,
       "cfprApEpqosDefinitionDelTaskFsmStageOrder": cfprApEpqosDefinitionDelTaskFsmStageOrder,
       "cfprApEpqosDefinitionDelTaskFsmStageRetry": cfprApEpqosDefinitionDelTaskFsmStageRetry,
       "cfprApEpqosDefinitionDelTaskFsmStageStageStatus": cfprApEpqosDefinitionDelTaskFsmStageStageStatus,
       "cfprApEpqosDefinitionDelTaskFsmTaskTable": cfprApEpqosDefinitionDelTaskFsmTaskTable,
       "cfprApEpqosDefinitionDelTaskFsmTaskEntry": cfprApEpqosDefinitionDelTaskFsmTaskEntry,
       "cfprApEpqosDefinitionDelTaskFsmTaskInstanceId": cfprApEpqosDefinitionDelTaskFsmTaskInstanceId,
       "cfprApEpqosDefinitionDelTaskFsmTaskDn": cfprApEpqosDefinitionDelTaskFsmTaskDn,
       "cfprApEpqosDefinitionDelTaskFsmTaskRn": cfprApEpqosDefinitionDelTaskFsmTaskRn,
       "cfprApEpqosDefinitionDelTaskFsmTaskCompletion": cfprApEpqosDefinitionDelTaskFsmTaskCompletion,
       "cfprApEpqosDefinitionDelTaskFsmTaskFlags": cfprApEpqosDefinitionDelTaskFsmTaskFlags,
       "cfprApEpqosDefinitionDelTaskFsmTaskItem": cfprApEpqosDefinitionDelTaskFsmTaskItem,
       "cfprApEpqosDefinitionDelTaskFsmTaskSeqId": cfprApEpqosDefinitionDelTaskFsmTaskSeqId,
       "cfprApEpqosDefinitionFsmTable": cfprApEpqosDefinitionFsmTable,
       "cfprApEpqosDefinitionFsmEntry": cfprApEpqosDefinitionFsmEntry,
       "cfprApEpqosDefinitionFsmInstanceId": cfprApEpqosDefinitionFsmInstanceId,
       "cfprApEpqosDefinitionFsmDn": cfprApEpqosDefinitionFsmDn,
       "cfprApEpqosDefinitionFsmRn": cfprApEpqosDefinitionFsmRn,
       "cfprApEpqosDefinitionFsmCompletionTime": cfprApEpqosDefinitionFsmCompletionTime,
       "cfprApEpqosDefinitionFsmCurrentFsm": cfprApEpqosDefinitionFsmCurrentFsm,
       "cfprApEpqosDefinitionFsmDescrData": cfprApEpqosDefinitionFsmDescrData,
       "cfprApEpqosDefinitionFsmFsmStatus": cfprApEpqosDefinitionFsmFsmStatus,
       "cfprApEpqosDefinitionFsmProgress": cfprApEpqosDefinitionFsmProgress,
       "cfprApEpqosDefinitionFsmRmtErrCode": cfprApEpqosDefinitionFsmRmtErrCode,
       "cfprApEpqosDefinitionFsmRmtErrDescr": cfprApEpqosDefinitionFsmRmtErrDescr,
       "cfprApEpqosDefinitionFsmRmtRslt": cfprApEpqosDefinitionFsmRmtRslt,
       "cfprApEpqosDefinitionFsmStageTable": cfprApEpqosDefinitionFsmStageTable,
       "cfprApEpqosDefinitionFsmStageEntry": cfprApEpqosDefinitionFsmStageEntry,
       "cfprApEpqosDefinitionFsmStageInstanceId": cfprApEpqosDefinitionFsmStageInstanceId,
       "cfprApEpqosDefinitionFsmStageDn": cfprApEpqosDefinitionFsmStageDn,
       "cfprApEpqosDefinitionFsmStageRn": cfprApEpqosDefinitionFsmStageRn,
       "cfprApEpqosDefinitionFsmStageDescrData": cfprApEpqosDefinitionFsmStageDescrData,
       "cfprApEpqosDefinitionFsmStageLastUpdateTime": cfprApEpqosDefinitionFsmStageLastUpdateTime,
       "cfprApEpqosDefinitionFsmStageName": cfprApEpqosDefinitionFsmStageName,
       "cfprApEpqosDefinitionFsmStageOrder": cfprApEpqosDefinitionFsmStageOrder,
       "cfprApEpqosDefinitionFsmStageRetry": cfprApEpqosDefinitionFsmStageRetry,
       "cfprApEpqosDefinitionFsmStageStageStatus": cfprApEpqosDefinitionFsmStageStageStatus,
       "cfprApEpqosDefinitionFsmTaskTable": cfprApEpqosDefinitionFsmTaskTable,
       "cfprApEpqosDefinitionFsmTaskEntry": cfprApEpqosDefinitionFsmTaskEntry,
       "cfprApEpqosDefinitionFsmTaskInstanceId": cfprApEpqosDefinitionFsmTaskInstanceId,
       "cfprApEpqosDefinitionFsmTaskDn": cfprApEpqosDefinitionFsmTaskDn,
       "cfprApEpqosDefinitionFsmTaskRn": cfprApEpqosDefinitionFsmTaskRn,
       "cfprApEpqosDefinitionFsmTaskCompletion": cfprApEpqosDefinitionFsmTaskCompletion,
       "cfprApEpqosDefinitionFsmTaskFlags": cfprApEpqosDefinitionFsmTaskFlags,
       "cfprApEpqosDefinitionFsmTaskItem": cfprApEpqosDefinitionFsmTaskItem,
       "cfprApEpqosDefinitionFsmTaskSeqId": cfprApEpqosDefinitionFsmTaskSeqId,
       "cfprApEpqosEgressTable": cfprApEpqosEgressTable,
       "cfprApEpqosEgressEntry": cfprApEpqosEgressEntry,
       "cfprApEpqosEgressInstanceId": cfprApEpqosEgressInstanceId,
       "cfprApEpqosEgressDn": cfprApEpqosEgressDn,
       "cfprApEpqosEgressRn": cfprApEpqosEgressRn,
       "cfprApEpqosEgressBurst": cfprApEpqosEgressBurst,
       "cfprApEpqosEgressHostControl": cfprApEpqosEgressHostControl,
       "cfprApEpqosEgressName": cfprApEpqosEgressName,
       "cfprApEpqosEgressOperPrio": cfprApEpqosEgressOperPrio,
       "cfprApEpqosEgressPrio": cfprApEpqosEgressPrio,
       "cfprApEpqosEgressRate": cfprApEpqosEgressRate}
)
