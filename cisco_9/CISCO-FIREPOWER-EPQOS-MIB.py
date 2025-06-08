# SNMP MIB module (CISCO-FIREPOWER-EPQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-EPQOS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:10 2025
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
 CfprEpqosDefinitionDelTaskFsmCurrentFsm,
 CfprEpqosDefinitionDelTaskFsmStageName,
 CfprEpqosDefinitionDelTaskFsmTaskItem,
 CfprEpqosDefinitionFsmCurrentFsm,
 CfprEpqosDefinitionFsmStageName,
 CfprEpqosDefinitionFsmTaskItem,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprPolicyPolicyOwner,
 CfprQosHostControl,
 CfprQosPriority) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprEpqosDefinitionDelTaskFsmCurrentFsm",
    "CfprEpqosDefinitionDelTaskFsmStageName",
    "CfprEpqosDefinitionDelTaskFsmTaskItem",
    "CfprEpqosDefinitionFsmCurrentFsm",
    "CfprEpqosDefinitionFsmStageName",
    "CfprEpqosDefinitionFsmTaskItem",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprPolicyPolicyOwner",
    "CfprQosHostControl",
    "CfprQosPriority")

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

cfprEpqosObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprEpqosDefinitionTable_Object = MibTable
cfprEpqosDefinitionTable = _CfprEpqosDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1)
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionTable.setStatus("current")
_CfprEpqosDefinitionEntry_Object = MibTableRow
cfprEpqosDefinitionEntry = _CfprEpqosDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1)
)
cfprEpqosDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EPQOS-MIB", "cfprEpqosDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionEntry.setStatus("current")
_CfprEpqosDefinitionInstanceId_Type = CfprManagedObjectId
_CfprEpqosDefinitionInstanceId_Object = MibTableColumn
cfprEpqosDefinitionInstanceId = _CfprEpqosDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 1),
    _CfprEpqosDefinitionInstanceId_Type()
)
cfprEpqosDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionInstanceId.setStatus("current")
_CfprEpqosDefinitionDn_Type = CfprManagedObjectDn
_CfprEpqosDefinitionDn_Object = MibTableColumn
cfprEpqosDefinitionDn = _CfprEpqosDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 2),
    _CfprEpqosDefinitionDn_Type()
)
cfprEpqosDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDn.setStatus("current")
_CfprEpqosDefinitionRn_Type = SnmpAdminString
_CfprEpqosDefinitionRn_Object = MibTableColumn
cfprEpqosDefinitionRn = _CfprEpqosDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 3),
    _CfprEpqosDefinitionRn_Type()
)
cfprEpqosDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionRn.setStatus("current")
_CfprEpqosDefinitionDescr_Type = SnmpAdminString
_CfprEpqosDefinitionDescr_Object = MibTableColumn
cfprEpqosDefinitionDescr = _CfprEpqosDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 4),
    _CfprEpqosDefinitionDescr_Type()
)
cfprEpqosDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDescr.setStatus("current")
_CfprEpqosDefinitionFsmDescr_Type = SnmpAdminString
_CfprEpqosDefinitionFsmDescr_Object = MibTableColumn
cfprEpqosDefinitionFsmDescr = _CfprEpqosDefinitionFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 5),
    _CfprEpqosDefinitionFsmDescr_Type()
)
cfprEpqosDefinitionFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmDescr.setStatus("current")
_CfprEpqosDefinitionFsmPrev_Type = SnmpAdminString
_CfprEpqosDefinitionFsmPrev_Object = MibTableColumn
cfprEpqosDefinitionFsmPrev = _CfprEpqosDefinitionFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 6),
    _CfprEpqosDefinitionFsmPrev_Type()
)
cfprEpqosDefinitionFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmPrev.setStatus("current")
_CfprEpqosDefinitionFsmProgr_Type = Gauge32
_CfprEpqosDefinitionFsmProgr_Object = MibTableColumn
cfprEpqosDefinitionFsmProgr = _CfprEpqosDefinitionFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 7),
    _CfprEpqosDefinitionFsmProgr_Type()
)
cfprEpqosDefinitionFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmProgr.setStatus("current")
_CfprEpqosDefinitionFsmRmtInvErrCode_Type = Gauge32
_CfprEpqosDefinitionFsmRmtInvErrCode_Object = MibTableColumn
cfprEpqosDefinitionFsmRmtInvErrCode = _CfprEpqosDefinitionFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 8),
    _CfprEpqosDefinitionFsmRmtInvErrCode_Type()
)
cfprEpqosDefinitionFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmRmtInvErrCode.setStatus("current")
_CfprEpqosDefinitionFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprEpqosDefinitionFsmRmtInvErrDescr_Object = MibTableColumn
cfprEpqosDefinitionFsmRmtInvErrDescr = _CfprEpqosDefinitionFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 9),
    _CfprEpqosDefinitionFsmRmtInvErrDescr_Type()
)
cfprEpqosDefinitionFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmRmtInvErrDescr.setStatus("current")
_CfprEpqosDefinitionFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprEpqosDefinitionFsmRmtInvRslt_Object = MibTableColumn
cfprEpqosDefinitionFsmRmtInvRslt = _CfprEpqosDefinitionFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 10),
    _CfprEpqosDefinitionFsmRmtInvRslt_Type()
)
cfprEpqosDefinitionFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmRmtInvRslt.setStatus("current")
_CfprEpqosDefinitionFsmStageDescr_Type = SnmpAdminString
_CfprEpqosDefinitionFsmStageDescr_Object = MibTableColumn
cfprEpqosDefinitionFsmStageDescr = _CfprEpqosDefinitionFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 11),
    _CfprEpqosDefinitionFsmStageDescr_Type()
)
cfprEpqosDefinitionFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStageDescr.setStatus("current")
_CfprEpqosDefinitionFsmStamp_Type = DateAndTime
_CfprEpqosDefinitionFsmStamp_Object = MibTableColumn
cfprEpqosDefinitionFsmStamp = _CfprEpqosDefinitionFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 12),
    _CfprEpqosDefinitionFsmStamp_Type()
)
cfprEpqosDefinitionFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStamp.setStatus("current")
_CfprEpqosDefinitionFsmStatus_Type = SnmpAdminString
_CfprEpqosDefinitionFsmStatus_Object = MibTableColumn
cfprEpqosDefinitionFsmStatus = _CfprEpqosDefinitionFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 13),
    _CfprEpqosDefinitionFsmStatus_Type()
)
cfprEpqosDefinitionFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStatus.setStatus("current")
_CfprEpqosDefinitionFsmTry_Type = Gauge32
_CfprEpqosDefinitionFsmTry_Object = MibTableColumn
cfprEpqosDefinitionFsmTry = _CfprEpqosDefinitionFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 14),
    _CfprEpqosDefinitionFsmTry_Type()
)
cfprEpqosDefinitionFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmTry.setStatus("current")
_CfprEpqosDefinitionIntId_Type = SnmpAdminString
_CfprEpqosDefinitionIntId_Object = MibTableColumn
cfprEpqosDefinitionIntId = _CfprEpqosDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 15),
    _CfprEpqosDefinitionIntId_Type()
)
cfprEpqosDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionIntId.setStatus("current")
_CfprEpqosDefinitionName_Type = SnmpAdminString
_CfprEpqosDefinitionName_Object = MibTableColumn
cfprEpqosDefinitionName = _CfprEpqosDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 16),
    _CfprEpqosDefinitionName_Type()
)
cfprEpqosDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionName.setStatus("current")
_CfprEpqosDefinitionPolicyLevel_Type = Gauge32
_CfprEpqosDefinitionPolicyLevel_Object = MibTableColumn
cfprEpqosDefinitionPolicyLevel = _CfprEpqosDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 17),
    _CfprEpqosDefinitionPolicyLevel_Type()
)
cfprEpqosDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionPolicyLevel.setStatus("current")
_CfprEpqosDefinitionPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprEpqosDefinitionPolicyOwner_Object = MibTableColumn
cfprEpqosDefinitionPolicyOwner = _CfprEpqosDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 1, 1, 18),
    _CfprEpqosDefinitionPolicyOwner_Type()
)
cfprEpqosDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionPolicyOwner.setStatus("current")
_CfprEpqosDefinitionDelTaskTable_Object = MibTable
cfprEpqosDefinitionDelTaskTable = _CfprEpqosDefinitionDelTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2)
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskTable.setStatus("current")
_CfprEpqosDefinitionDelTaskEntry_Object = MibTableRow
cfprEpqosDefinitionDelTaskEntry = _CfprEpqosDefinitionDelTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1)
)
cfprEpqosDefinitionDelTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EPQOS-MIB", "cfprEpqosDefinitionDelTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskEntry.setStatus("current")
_CfprEpqosDefinitionDelTaskInstanceId_Type = CfprManagedObjectId
_CfprEpqosDefinitionDelTaskInstanceId_Object = MibTableColumn
cfprEpqosDefinitionDelTaskInstanceId = _CfprEpqosDefinitionDelTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 1),
    _CfprEpqosDefinitionDelTaskInstanceId_Type()
)
cfprEpqosDefinitionDelTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskInstanceId.setStatus("current")
_CfprEpqosDefinitionDelTaskDn_Type = CfprManagedObjectDn
_CfprEpqosDefinitionDelTaskDn_Object = MibTableColumn
cfprEpqosDefinitionDelTaskDn = _CfprEpqosDefinitionDelTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 2),
    _CfprEpqosDefinitionDelTaskDn_Type()
)
cfprEpqosDefinitionDelTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskDn.setStatus("current")
_CfprEpqosDefinitionDelTaskRn_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskRn_Object = MibTableColumn
cfprEpqosDefinitionDelTaskRn = _CfprEpqosDefinitionDelTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 3),
    _CfprEpqosDefinitionDelTaskRn_Type()
)
cfprEpqosDefinitionDelTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskRn.setStatus("current")
_CfprEpqosDefinitionDelTaskDefDn_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskDefDn_Object = MibTableColumn
cfprEpqosDefinitionDelTaskDefDn = _CfprEpqosDefinitionDelTaskDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 4),
    _CfprEpqosDefinitionDelTaskDefDn_Type()
)
cfprEpqosDefinitionDelTaskDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskDefDn.setStatus("current")
_CfprEpqosDefinitionDelTaskDefIntId_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskDefIntId_Object = MibTableColumn
cfprEpqosDefinitionDelTaskDefIntId = _CfprEpqosDefinitionDelTaskDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 5),
    _CfprEpqosDefinitionDelTaskDefIntId_Type()
)
cfprEpqosDefinitionDelTaskDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskDefIntId.setStatus("current")
_CfprEpqosDefinitionDelTaskDescr_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskDescr_Object = MibTableColumn
cfprEpqosDefinitionDelTaskDescr = _CfprEpqosDefinitionDelTaskDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 6),
    _CfprEpqosDefinitionDelTaskDescr_Type()
)
cfprEpqosDefinitionDelTaskDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskDescr.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmDescr_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskFsmDescr_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmDescr = _CfprEpqosDefinitionDelTaskFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 7),
    _CfprEpqosDefinitionDelTaskFsmDescr_Type()
)
cfprEpqosDefinitionDelTaskFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmDescr.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmPrev_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskFsmPrev_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmPrev = _CfprEpqosDefinitionDelTaskFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 8),
    _CfprEpqosDefinitionDelTaskFsmPrev_Type()
)
cfprEpqosDefinitionDelTaskFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmPrev.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmProgr_Type = Gauge32
_CfprEpqosDefinitionDelTaskFsmProgr_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmProgr = _CfprEpqosDefinitionDelTaskFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 9),
    _CfprEpqosDefinitionDelTaskFsmProgr_Type()
)
cfprEpqosDefinitionDelTaskFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmProgr.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmRmtInvErrCode_Type = Gauge32
_CfprEpqosDefinitionDelTaskFsmRmtInvErrCode_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmRmtInvErrCode = _CfprEpqosDefinitionDelTaskFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 10),
    _CfprEpqosDefinitionDelTaskFsmRmtInvErrCode_Type()
)
cfprEpqosDefinitionDelTaskFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmRmtInvErrCode.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskFsmRmtInvErrDescr_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmRmtInvErrDescr = _CfprEpqosDefinitionDelTaskFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 11),
    _CfprEpqosDefinitionDelTaskFsmRmtInvErrDescr_Type()
)
cfprEpqosDefinitionDelTaskFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmRmtInvErrDescr.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprEpqosDefinitionDelTaskFsmRmtInvRslt_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmRmtInvRslt = _CfprEpqosDefinitionDelTaskFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 12),
    _CfprEpqosDefinitionDelTaskFsmRmtInvRslt_Type()
)
cfprEpqosDefinitionDelTaskFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmRmtInvRslt.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStageDescr_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskFsmStageDescr_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmStageDescr = _CfprEpqosDefinitionDelTaskFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 13),
    _CfprEpqosDefinitionDelTaskFsmStageDescr_Type()
)
cfprEpqosDefinitionDelTaskFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStageDescr.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStamp_Type = DateAndTime
_CfprEpqosDefinitionDelTaskFsmStamp_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmStamp = _CfprEpqosDefinitionDelTaskFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 14),
    _CfprEpqosDefinitionDelTaskFsmStamp_Type()
)
cfprEpqosDefinitionDelTaskFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStamp.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStatus_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskFsmStatus_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmStatus = _CfprEpqosDefinitionDelTaskFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 15),
    _CfprEpqosDefinitionDelTaskFsmStatus_Type()
)
cfprEpqosDefinitionDelTaskFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStatus.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmTry_Type = Gauge32
_CfprEpqosDefinitionDelTaskFsmTry_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmTry = _CfprEpqosDefinitionDelTaskFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 16),
    _CfprEpqosDefinitionDelTaskFsmTry_Type()
)
cfprEpqosDefinitionDelTaskFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmTry.setStatus("current")
_CfprEpqosDefinitionDelTaskIntId_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskIntId_Object = MibTableColumn
cfprEpqosDefinitionDelTaskIntId = _CfprEpqosDefinitionDelTaskIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 17),
    _CfprEpqosDefinitionDelTaskIntId_Type()
)
cfprEpqosDefinitionDelTaskIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskIntId.setStatus("current")
_CfprEpqosDefinitionDelTaskName_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskName_Object = MibTableColumn
cfprEpqosDefinitionDelTaskName = _CfprEpqosDefinitionDelTaskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 18),
    _CfprEpqosDefinitionDelTaskName_Type()
)
cfprEpqosDefinitionDelTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskName.setStatus("current")
_CfprEpqosDefinitionDelTaskPolicyLevel_Type = Gauge32
_CfprEpqosDefinitionDelTaskPolicyLevel_Object = MibTableColumn
cfprEpqosDefinitionDelTaskPolicyLevel = _CfprEpqosDefinitionDelTaskPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 19),
    _CfprEpqosDefinitionDelTaskPolicyLevel_Type()
)
cfprEpqosDefinitionDelTaskPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskPolicyLevel.setStatus("current")
_CfprEpqosDefinitionDelTaskPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprEpqosDefinitionDelTaskPolicyOwner_Object = MibTableColumn
cfprEpqosDefinitionDelTaskPolicyOwner = _CfprEpqosDefinitionDelTaskPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 2, 1, 20),
    _CfprEpqosDefinitionDelTaskPolicyOwner_Type()
)
cfprEpqosDefinitionDelTaskPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskPolicyOwner.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmTable_Object = MibTable
cfprEpqosDefinitionDelTaskFsmTable = _CfprEpqosDefinitionDelTaskFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3)
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmTable.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmEntry_Object = MibTableRow
cfprEpqosDefinitionDelTaskFsmEntry = _CfprEpqosDefinitionDelTaskFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3, 1)
)
cfprEpqosDefinitionDelTaskFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EPQOS-MIB", "cfprEpqosDefinitionDelTaskFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmEntry.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmInstanceId_Type = CfprManagedObjectId
_CfprEpqosDefinitionDelTaskFsmInstanceId_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmInstanceId = _CfprEpqosDefinitionDelTaskFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3, 1, 1),
    _CfprEpqosDefinitionDelTaskFsmInstanceId_Type()
)
cfprEpqosDefinitionDelTaskFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmInstanceId.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmDn_Type = CfprManagedObjectDn
_CfprEpqosDefinitionDelTaskFsmDn_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmDn = _CfprEpqosDefinitionDelTaskFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3, 1, 2),
    _CfprEpqosDefinitionDelTaskFsmDn_Type()
)
cfprEpqosDefinitionDelTaskFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmDn.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmRn_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskFsmRn_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmRn = _CfprEpqosDefinitionDelTaskFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3, 1, 3),
    _CfprEpqosDefinitionDelTaskFsmRn_Type()
)
cfprEpqosDefinitionDelTaskFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmRn.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmCompletionTime_Type = DateAndTime
_CfprEpqosDefinitionDelTaskFsmCompletionTime_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmCompletionTime = _CfprEpqosDefinitionDelTaskFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3, 1, 4),
    _CfprEpqosDefinitionDelTaskFsmCompletionTime_Type()
)
cfprEpqosDefinitionDelTaskFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmCompletionTime.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmCurrentFsm_Type = CfprEpqosDefinitionDelTaskFsmCurrentFsm
_CfprEpqosDefinitionDelTaskFsmCurrentFsm_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmCurrentFsm = _CfprEpqosDefinitionDelTaskFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3, 1, 5),
    _CfprEpqosDefinitionDelTaskFsmCurrentFsm_Type()
)
cfprEpqosDefinitionDelTaskFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmCurrentFsm.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmDescrData_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskFsmDescrData_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmDescrData = _CfprEpqosDefinitionDelTaskFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3, 1, 6),
    _CfprEpqosDefinitionDelTaskFsmDescrData_Type()
)
cfprEpqosDefinitionDelTaskFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmDescrData.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprEpqosDefinitionDelTaskFsmFsmStatus_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmFsmStatus = _CfprEpqosDefinitionDelTaskFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3, 1, 7),
    _CfprEpqosDefinitionDelTaskFsmFsmStatus_Type()
)
cfprEpqosDefinitionDelTaskFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmFsmStatus.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmProgress_Type = Gauge32
_CfprEpqosDefinitionDelTaskFsmProgress_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmProgress = _CfprEpqosDefinitionDelTaskFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3, 1, 8),
    _CfprEpqosDefinitionDelTaskFsmProgress_Type()
)
cfprEpqosDefinitionDelTaskFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmProgress.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmRmtErrCode_Type = Gauge32
_CfprEpqosDefinitionDelTaskFsmRmtErrCode_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmRmtErrCode = _CfprEpqosDefinitionDelTaskFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3, 1, 9),
    _CfprEpqosDefinitionDelTaskFsmRmtErrCode_Type()
)
cfprEpqosDefinitionDelTaskFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmRmtErrCode.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmRmtErrDescr_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskFsmRmtErrDescr_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmRmtErrDescr = _CfprEpqosDefinitionDelTaskFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3, 1, 10),
    _CfprEpqosDefinitionDelTaskFsmRmtErrDescr_Type()
)
cfprEpqosDefinitionDelTaskFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmRmtErrDescr.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprEpqosDefinitionDelTaskFsmRmtRslt_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmRmtRslt = _CfprEpqosDefinitionDelTaskFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 3, 1, 11),
    _CfprEpqosDefinitionDelTaskFsmRmtRslt_Type()
)
cfprEpqosDefinitionDelTaskFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmRmtRslt.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStageTable_Object = MibTable
cfprEpqosDefinitionDelTaskFsmStageTable = _CfprEpqosDefinitionDelTaskFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 4)
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStageTable.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStageEntry_Object = MibTableRow
cfprEpqosDefinitionDelTaskFsmStageEntry = _CfprEpqosDefinitionDelTaskFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 4, 1)
)
cfprEpqosDefinitionDelTaskFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EPQOS-MIB", "cfprEpqosDefinitionDelTaskFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStageEntry.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStageInstanceId_Type = CfprManagedObjectId
_CfprEpqosDefinitionDelTaskFsmStageInstanceId_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmStageInstanceId = _CfprEpqosDefinitionDelTaskFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 4, 1, 1),
    _CfprEpqosDefinitionDelTaskFsmStageInstanceId_Type()
)
cfprEpqosDefinitionDelTaskFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStageInstanceId.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStageDn_Type = CfprManagedObjectDn
_CfprEpqosDefinitionDelTaskFsmStageDn_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmStageDn = _CfprEpqosDefinitionDelTaskFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 4, 1, 2),
    _CfprEpqosDefinitionDelTaskFsmStageDn_Type()
)
cfprEpqosDefinitionDelTaskFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStageDn.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStageRn_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskFsmStageRn_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmStageRn = _CfprEpqosDefinitionDelTaskFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 4, 1, 3),
    _CfprEpqosDefinitionDelTaskFsmStageRn_Type()
)
cfprEpqosDefinitionDelTaskFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStageRn.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStageDescrData_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskFsmStageDescrData_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmStageDescrData = _CfprEpqosDefinitionDelTaskFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 4, 1, 4),
    _CfprEpqosDefinitionDelTaskFsmStageDescrData_Type()
)
cfprEpqosDefinitionDelTaskFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStageDescrData.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStageLastUpdateTime_Type = DateAndTime
_CfprEpqosDefinitionDelTaskFsmStageLastUpdateTime_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmStageLastUpdateTime = _CfprEpqosDefinitionDelTaskFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 4, 1, 5),
    _CfprEpqosDefinitionDelTaskFsmStageLastUpdateTime_Type()
)
cfprEpqosDefinitionDelTaskFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStageLastUpdateTime.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStageName_Type = CfprEpqosDefinitionDelTaskFsmStageName
_CfprEpqosDefinitionDelTaskFsmStageName_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmStageName = _CfprEpqosDefinitionDelTaskFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 4, 1, 6),
    _CfprEpqosDefinitionDelTaskFsmStageName_Type()
)
cfprEpqosDefinitionDelTaskFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStageName.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStageOrder_Type = Gauge32
_CfprEpqosDefinitionDelTaskFsmStageOrder_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmStageOrder = _CfprEpqosDefinitionDelTaskFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 4, 1, 7),
    _CfprEpqosDefinitionDelTaskFsmStageOrder_Type()
)
cfprEpqosDefinitionDelTaskFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStageOrder.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStageRetry_Type = Gauge32
_CfprEpqosDefinitionDelTaskFsmStageRetry_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmStageRetry = _CfprEpqosDefinitionDelTaskFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 4, 1, 8),
    _CfprEpqosDefinitionDelTaskFsmStageRetry_Type()
)
cfprEpqosDefinitionDelTaskFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStageRetry.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprEpqosDefinitionDelTaskFsmStageStageStatus_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmStageStageStatus = _CfprEpqosDefinitionDelTaskFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 4, 1, 9),
    _CfprEpqosDefinitionDelTaskFsmStageStageStatus_Type()
)
cfprEpqosDefinitionDelTaskFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmStageStageStatus.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmTaskTable_Object = MibTable
cfprEpqosDefinitionDelTaskFsmTaskTable = _CfprEpqosDefinitionDelTaskFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 5)
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmTaskTable.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmTaskEntry_Object = MibTableRow
cfprEpqosDefinitionDelTaskFsmTaskEntry = _CfprEpqosDefinitionDelTaskFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 5, 1)
)
cfprEpqosDefinitionDelTaskFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EPQOS-MIB", "cfprEpqosDefinitionDelTaskFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmTaskEntry.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprEpqosDefinitionDelTaskFsmTaskInstanceId_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmTaskInstanceId = _CfprEpqosDefinitionDelTaskFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 5, 1, 1),
    _CfprEpqosDefinitionDelTaskFsmTaskInstanceId_Type()
)
cfprEpqosDefinitionDelTaskFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmTaskInstanceId.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmTaskDn_Type = CfprManagedObjectDn
_CfprEpqosDefinitionDelTaskFsmTaskDn_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmTaskDn = _CfprEpqosDefinitionDelTaskFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 5, 1, 2),
    _CfprEpqosDefinitionDelTaskFsmTaskDn_Type()
)
cfprEpqosDefinitionDelTaskFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmTaskDn.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmTaskRn_Type = SnmpAdminString
_CfprEpqosDefinitionDelTaskFsmTaskRn_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmTaskRn = _CfprEpqosDefinitionDelTaskFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 5, 1, 3),
    _CfprEpqosDefinitionDelTaskFsmTaskRn_Type()
)
cfprEpqosDefinitionDelTaskFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmTaskRn.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmTaskCompletion_Type = CfprFsmCompletion
_CfprEpqosDefinitionDelTaskFsmTaskCompletion_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmTaskCompletion = _CfprEpqosDefinitionDelTaskFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 5, 1, 4),
    _CfprEpqosDefinitionDelTaskFsmTaskCompletion_Type()
)
cfprEpqosDefinitionDelTaskFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmTaskCompletion.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmTaskFlags_Type = CfprFsmFlags
_CfprEpqosDefinitionDelTaskFsmTaskFlags_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmTaskFlags = _CfprEpqosDefinitionDelTaskFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 5, 1, 5),
    _CfprEpqosDefinitionDelTaskFsmTaskFlags_Type()
)
cfprEpqosDefinitionDelTaskFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmTaskFlags.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmTaskItem_Type = CfprEpqosDefinitionDelTaskFsmTaskItem
_CfprEpqosDefinitionDelTaskFsmTaskItem_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmTaskItem = _CfprEpqosDefinitionDelTaskFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 5, 1, 6),
    _CfprEpqosDefinitionDelTaskFsmTaskItem_Type()
)
cfprEpqosDefinitionDelTaskFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmTaskItem.setStatus("current")
_CfprEpqosDefinitionDelTaskFsmTaskSeqId_Type = Gauge32
_CfprEpqosDefinitionDelTaskFsmTaskSeqId_Object = MibTableColumn
cfprEpqosDefinitionDelTaskFsmTaskSeqId = _CfprEpqosDefinitionDelTaskFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 5, 1, 7),
    _CfprEpqosDefinitionDelTaskFsmTaskSeqId_Type()
)
cfprEpqosDefinitionDelTaskFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionDelTaskFsmTaskSeqId.setStatus("current")
_CfprEpqosDefinitionFsmTable_Object = MibTable
cfprEpqosDefinitionFsmTable = _CfprEpqosDefinitionFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6)
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmTable.setStatus("current")
_CfprEpqosDefinitionFsmEntry_Object = MibTableRow
cfprEpqosDefinitionFsmEntry = _CfprEpqosDefinitionFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6, 1)
)
cfprEpqosDefinitionFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EPQOS-MIB", "cfprEpqosDefinitionFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmEntry.setStatus("current")
_CfprEpqosDefinitionFsmInstanceId_Type = CfprManagedObjectId
_CfprEpqosDefinitionFsmInstanceId_Object = MibTableColumn
cfprEpqosDefinitionFsmInstanceId = _CfprEpqosDefinitionFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6, 1, 1),
    _CfprEpqosDefinitionFsmInstanceId_Type()
)
cfprEpqosDefinitionFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmInstanceId.setStatus("current")
_CfprEpqosDefinitionFsmDn_Type = CfprManagedObjectDn
_CfprEpqosDefinitionFsmDn_Object = MibTableColumn
cfprEpqosDefinitionFsmDn = _CfprEpqosDefinitionFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6, 1, 2),
    _CfprEpqosDefinitionFsmDn_Type()
)
cfprEpqosDefinitionFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmDn.setStatus("current")
_CfprEpqosDefinitionFsmRn_Type = SnmpAdminString
_CfprEpqosDefinitionFsmRn_Object = MibTableColumn
cfprEpqosDefinitionFsmRn = _CfprEpqosDefinitionFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6, 1, 3),
    _CfprEpqosDefinitionFsmRn_Type()
)
cfprEpqosDefinitionFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmRn.setStatus("current")
_CfprEpqosDefinitionFsmCompletionTime_Type = DateAndTime
_CfprEpqosDefinitionFsmCompletionTime_Object = MibTableColumn
cfprEpqosDefinitionFsmCompletionTime = _CfprEpqosDefinitionFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6, 1, 4),
    _CfprEpqosDefinitionFsmCompletionTime_Type()
)
cfprEpqosDefinitionFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmCompletionTime.setStatus("current")
_CfprEpqosDefinitionFsmCurrentFsm_Type = CfprEpqosDefinitionFsmCurrentFsm
_CfprEpqosDefinitionFsmCurrentFsm_Object = MibTableColumn
cfprEpqosDefinitionFsmCurrentFsm = _CfprEpqosDefinitionFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6, 1, 5),
    _CfprEpqosDefinitionFsmCurrentFsm_Type()
)
cfprEpqosDefinitionFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmCurrentFsm.setStatus("current")
_CfprEpqosDefinitionFsmDescrData_Type = SnmpAdminString
_CfprEpqosDefinitionFsmDescrData_Object = MibTableColumn
cfprEpqosDefinitionFsmDescrData = _CfprEpqosDefinitionFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6, 1, 6),
    _CfprEpqosDefinitionFsmDescrData_Type()
)
cfprEpqosDefinitionFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmDescrData.setStatus("current")
_CfprEpqosDefinitionFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprEpqosDefinitionFsmFsmStatus_Object = MibTableColumn
cfprEpqosDefinitionFsmFsmStatus = _CfprEpqosDefinitionFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6, 1, 7),
    _CfprEpqosDefinitionFsmFsmStatus_Type()
)
cfprEpqosDefinitionFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmFsmStatus.setStatus("current")
_CfprEpqosDefinitionFsmProgress_Type = Gauge32
_CfprEpqosDefinitionFsmProgress_Object = MibTableColumn
cfprEpqosDefinitionFsmProgress = _CfprEpqosDefinitionFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6, 1, 8),
    _CfprEpqosDefinitionFsmProgress_Type()
)
cfprEpqosDefinitionFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmProgress.setStatus("current")
_CfprEpqosDefinitionFsmRmtErrCode_Type = Gauge32
_CfprEpqosDefinitionFsmRmtErrCode_Object = MibTableColumn
cfprEpqosDefinitionFsmRmtErrCode = _CfprEpqosDefinitionFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6, 1, 9),
    _CfprEpqosDefinitionFsmRmtErrCode_Type()
)
cfprEpqosDefinitionFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmRmtErrCode.setStatus("current")
_CfprEpqosDefinitionFsmRmtErrDescr_Type = SnmpAdminString
_CfprEpqosDefinitionFsmRmtErrDescr_Object = MibTableColumn
cfprEpqosDefinitionFsmRmtErrDescr = _CfprEpqosDefinitionFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6, 1, 10),
    _CfprEpqosDefinitionFsmRmtErrDescr_Type()
)
cfprEpqosDefinitionFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmRmtErrDescr.setStatus("current")
_CfprEpqosDefinitionFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprEpqosDefinitionFsmRmtRslt_Object = MibTableColumn
cfprEpqosDefinitionFsmRmtRslt = _CfprEpqosDefinitionFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 6, 1, 11),
    _CfprEpqosDefinitionFsmRmtRslt_Type()
)
cfprEpqosDefinitionFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmRmtRslt.setStatus("current")
_CfprEpqosDefinitionFsmStageTable_Object = MibTable
cfprEpqosDefinitionFsmStageTable = _CfprEpqosDefinitionFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 7)
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStageTable.setStatus("current")
_CfprEpqosDefinitionFsmStageEntry_Object = MibTableRow
cfprEpqosDefinitionFsmStageEntry = _CfprEpqosDefinitionFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 7, 1)
)
cfprEpqosDefinitionFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EPQOS-MIB", "cfprEpqosDefinitionFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStageEntry.setStatus("current")
_CfprEpqosDefinitionFsmStageInstanceId_Type = CfprManagedObjectId
_CfprEpqosDefinitionFsmStageInstanceId_Object = MibTableColumn
cfprEpqosDefinitionFsmStageInstanceId = _CfprEpqosDefinitionFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 7, 1, 1),
    _CfprEpqosDefinitionFsmStageInstanceId_Type()
)
cfprEpqosDefinitionFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStageInstanceId.setStatus("current")
_CfprEpqosDefinitionFsmStageDn_Type = CfprManagedObjectDn
_CfprEpqosDefinitionFsmStageDn_Object = MibTableColumn
cfprEpqosDefinitionFsmStageDn = _CfprEpqosDefinitionFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 7, 1, 2),
    _CfprEpqosDefinitionFsmStageDn_Type()
)
cfprEpqosDefinitionFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStageDn.setStatus("current")
_CfprEpqosDefinitionFsmStageRn_Type = SnmpAdminString
_CfprEpqosDefinitionFsmStageRn_Object = MibTableColumn
cfprEpqosDefinitionFsmStageRn = _CfprEpqosDefinitionFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 7, 1, 3),
    _CfprEpqosDefinitionFsmStageRn_Type()
)
cfprEpqosDefinitionFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStageRn.setStatus("current")
_CfprEpqosDefinitionFsmStageDescrData_Type = SnmpAdminString
_CfprEpqosDefinitionFsmStageDescrData_Object = MibTableColumn
cfprEpqosDefinitionFsmStageDescrData = _CfprEpqosDefinitionFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 7, 1, 4),
    _CfprEpqosDefinitionFsmStageDescrData_Type()
)
cfprEpqosDefinitionFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStageDescrData.setStatus("current")
_CfprEpqosDefinitionFsmStageLastUpdateTime_Type = DateAndTime
_CfprEpqosDefinitionFsmStageLastUpdateTime_Object = MibTableColumn
cfprEpqosDefinitionFsmStageLastUpdateTime = _CfprEpqosDefinitionFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 7, 1, 5),
    _CfprEpqosDefinitionFsmStageLastUpdateTime_Type()
)
cfprEpqosDefinitionFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStageLastUpdateTime.setStatus("current")
_CfprEpqosDefinitionFsmStageName_Type = CfprEpqosDefinitionFsmStageName
_CfprEpqosDefinitionFsmStageName_Object = MibTableColumn
cfprEpqosDefinitionFsmStageName = _CfprEpqosDefinitionFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 7, 1, 6),
    _CfprEpqosDefinitionFsmStageName_Type()
)
cfprEpqosDefinitionFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStageName.setStatus("current")
_CfprEpqosDefinitionFsmStageOrder_Type = Gauge32
_CfprEpqosDefinitionFsmStageOrder_Object = MibTableColumn
cfprEpqosDefinitionFsmStageOrder = _CfprEpqosDefinitionFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 7, 1, 7),
    _CfprEpqosDefinitionFsmStageOrder_Type()
)
cfprEpqosDefinitionFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStageOrder.setStatus("current")
_CfprEpqosDefinitionFsmStageRetry_Type = Gauge32
_CfprEpqosDefinitionFsmStageRetry_Object = MibTableColumn
cfprEpqosDefinitionFsmStageRetry = _CfprEpqosDefinitionFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 7, 1, 8),
    _CfprEpqosDefinitionFsmStageRetry_Type()
)
cfprEpqosDefinitionFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStageRetry.setStatus("current")
_CfprEpqosDefinitionFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprEpqosDefinitionFsmStageStageStatus_Object = MibTableColumn
cfprEpqosDefinitionFsmStageStageStatus = _CfprEpqosDefinitionFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 7, 1, 9),
    _CfprEpqosDefinitionFsmStageStageStatus_Type()
)
cfprEpqosDefinitionFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmStageStageStatus.setStatus("current")
_CfprEpqosDefinitionFsmTaskTable_Object = MibTable
cfprEpqosDefinitionFsmTaskTable = _CfprEpqosDefinitionFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 8)
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmTaskTable.setStatus("current")
_CfprEpqosDefinitionFsmTaskEntry_Object = MibTableRow
cfprEpqosDefinitionFsmTaskEntry = _CfprEpqosDefinitionFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 8, 1)
)
cfprEpqosDefinitionFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EPQOS-MIB", "cfprEpqosDefinitionFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmTaskEntry.setStatus("current")
_CfprEpqosDefinitionFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprEpqosDefinitionFsmTaskInstanceId_Object = MibTableColumn
cfprEpqosDefinitionFsmTaskInstanceId = _CfprEpqosDefinitionFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 8, 1, 1),
    _CfprEpqosDefinitionFsmTaskInstanceId_Type()
)
cfprEpqosDefinitionFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmTaskInstanceId.setStatus("current")
_CfprEpqosDefinitionFsmTaskDn_Type = CfprManagedObjectDn
_CfprEpqosDefinitionFsmTaskDn_Object = MibTableColumn
cfprEpqosDefinitionFsmTaskDn = _CfprEpqosDefinitionFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 8, 1, 2),
    _CfprEpqosDefinitionFsmTaskDn_Type()
)
cfprEpqosDefinitionFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmTaskDn.setStatus("current")
_CfprEpqosDefinitionFsmTaskRn_Type = SnmpAdminString
_CfprEpqosDefinitionFsmTaskRn_Object = MibTableColumn
cfprEpqosDefinitionFsmTaskRn = _CfprEpqosDefinitionFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 8, 1, 3),
    _CfprEpqosDefinitionFsmTaskRn_Type()
)
cfprEpqosDefinitionFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmTaskRn.setStatus("current")
_CfprEpqosDefinitionFsmTaskCompletion_Type = CfprFsmCompletion
_CfprEpqosDefinitionFsmTaskCompletion_Object = MibTableColumn
cfprEpqosDefinitionFsmTaskCompletion = _CfprEpqosDefinitionFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 8, 1, 4),
    _CfprEpqosDefinitionFsmTaskCompletion_Type()
)
cfprEpqosDefinitionFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmTaskCompletion.setStatus("current")
_CfprEpqosDefinitionFsmTaskFlags_Type = CfprFsmFlags
_CfprEpqosDefinitionFsmTaskFlags_Object = MibTableColumn
cfprEpqosDefinitionFsmTaskFlags = _CfprEpqosDefinitionFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 8, 1, 5),
    _CfprEpqosDefinitionFsmTaskFlags_Type()
)
cfprEpqosDefinitionFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmTaskFlags.setStatus("current")
_CfprEpqosDefinitionFsmTaskItem_Type = CfprEpqosDefinitionFsmTaskItem
_CfprEpqosDefinitionFsmTaskItem_Object = MibTableColumn
cfprEpqosDefinitionFsmTaskItem = _CfprEpqosDefinitionFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 8, 1, 6),
    _CfprEpqosDefinitionFsmTaskItem_Type()
)
cfprEpqosDefinitionFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmTaskItem.setStatus("current")
_CfprEpqosDefinitionFsmTaskSeqId_Type = Gauge32
_CfprEpqosDefinitionFsmTaskSeqId_Object = MibTableColumn
cfprEpqosDefinitionFsmTaskSeqId = _CfprEpqosDefinitionFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 8, 1, 7),
    _CfprEpqosDefinitionFsmTaskSeqId_Type()
)
cfprEpqosDefinitionFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosDefinitionFsmTaskSeqId.setStatus("current")
_CfprEpqosEgressTable_Object = MibTable
cfprEpqosEgressTable = _CfprEpqosEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 9)
)
if mibBuilder.loadTexts:
    cfprEpqosEgressTable.setStatus("current")
_CfprEpqosEgressEntry_Object = MibTableRow
cfprEpqosEgressEntry = _CfprEpqosEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 9, 1)
)
cfprEpqosEgressEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EPQOS-MIB", "cfprEpqosEgressInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEpqosEgressEntry.setStatus("current")
_CfprEpqosEgressInstanceId_Type = CfprManagedObjectId
_CfprEpqosEgressInstanceId_Object = MibTableColumn
cfprEpqosEgressInstanceId = _CfprEpqosEgressInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 9, 1, 1),
    _CfprEpqosEgressInstanceId_Type()
)
cfprEpqosEgressInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEpqosEgressInstanceId.setStatus("current")
_CfprEpqosEgressDn_Type = CfprManagedObjectDn
_CfprEpqosEgressDn_Object = MibTableColumn
cfprEpqosEgressDn = _CfprEpqosEgressDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 9, 1, 2),
    _CfprEpqosEgressDn_Type()
)
cfprEpqosEgressDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosEgressDn.setStatus("current")
_CfprEpqosEgressRn_Type = SnmpAdminString
_CfprEpqosEgressRn_Object = MibTableColumn
cfprEpqosEgressRn = _CfprEpqosEgressRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 9, 1, 3),
    _CfprEpqosEgressRn_Type()
)
cfprEpqosEgressRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosEgressRn.setStatus("current")
_CfprEpqosEgressBurst_Type = Gauge32
_CfprEpqosEgressBurst_Object = MibTableColumn
cfprEpqosEgressBurst = _CfprEpqosEgressBurst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 9, 1, 4),
    _CfprEpqosEgressBurst_Type()
)
cfprEpqosEgressBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosEgressBurst.setStatus("current")
_CfprEpqosEgressHostControl_Type = CfprQosHostControl
_CfprEpqosEgressHostControl_Object = MibTableColumn
cfprEpqosEgressHostControl = _CfprEpqosEgressHostControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 9, 1, 5),
    _CfprEpqosEgressHostControl_Type()
)
cfprEpqosEgressHostControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosEgressHostControl.setStatus("current")
_CfprEpqosEgressName_Type = SnmpAdminString
_CfprEpqosEgressName_Object = MibTableColumn
cfprEpqosEgressName = _CfprEpqosEgressName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 9, 1, 6),
    _CfprEpqosEgressName_Type()
)
cfprEpqosEgressName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosEgressName.setStatus("current")
_CfprEpqosEgressOperPrio_Type = CfprQosPriority
_CfprEpqosEgressOperPrio_Object = MibTableColumn
cfprEpqosEgressOperPrio = _CfprEpqosEgressOperPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 9, 1, 7),
    _CfprEpqosEgressOperPrio_Type()
)
cfprEpqosEgressOperPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosEgressOperPrio.setStatus("current")
_CfprEpqosEgressPrio_Type = CfprQosPriority
_CfprEpqosEgressPrio_Object = MibTableColumn
cfprEpqosEgressPrio = _CfprEpqosEgressPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 9, 1, 8),
    _CfprEpqosEgressPrio_Type()
)
cfprEpqosEgressPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosEgressPrio.setStatus("current")
_CfprEpqosEgressRate_Type = Gauge32
_CfprEpqosEgressRate_Object = MibTableColumn
cfprEpqosEgressRate = _CfprEpqosEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 19, 9, 1, 9),
    _CfprEpqosEgressRate_Type()
)
cfprEpqosEgressRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEpqosEgressRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-EPQOS-MIB",
    **{"cfprEpqosObjects": cfprEpqosObjects,
       "cfprEpqosDefinitionTable": cfprEpqosDefinitionTable,
       "cfprEpqosDefinitionEntry": cfprEpqosDefinitionEntry,
       "cfprEpqosDefinitionInstanceId": cfprEpqosDefinitionInstanceId,
       "cfprEpqosDefinitionDn": cfprEpqosDefinitionDn,
       "cfprEpqosDefinitionRn": cfprEpqosDefinitionRn,
       "cfprEpqosDefinitionDescr": cfprEpqosDefinitionDescr,
       "cfprEpqosDefinitionFsmDescr": cfprEpqosDefinitionFsmDescr,
       "cfprEpqosDefinitionFsmPrev": cfprEpqosDefinitionFsmPrev,
       "cfprEpqosDefinitionFsmProgr": cfprEpqosDefinitionFsmProgr,
       "cfprEpqosDefinitionFsmRmtInvErrCode": cfprEpqosDefinitionFsmRmtInvErrCode,
       "cfprEpqosDefinitionFsmRmtInvErrDescr": cfprEpqosDefinitionFsmRmtInvErrDescr,
       "cfprEpqosDefinitionFsmRmtInvRslt": cfprEpqosDefinitionFsmRmtInvRslt,
       "cfprEpqosDefinitionFsmStageDescr": cfprEpqosDefinitionFsmStageDescr,
       "cfprEpqosDefinitionFsmStamp": cfprEpqosDefinitionFsmStamp,
       "cfprEpqosDefinitionFsmStatus": cfprEpqosDefinitionFsmStatus,
       "cfprEpqosDefinitionFsmTry": cfprEpqosDefinitionFsmTry,
       "cfprEpqosDefinitionIntId": cfprEpqosDefinitionIntId,
       "cfprEpqosDefinitionName": cfprEpqosDefinitionName,
       "cfprEpqosDefinitionPolicyLevel": cfprEpqosDefinitionPolicyLevel,
       "cfprEpqosDefinitionPolicyOwner": cfprEpqosDefinitionPolicyOwner,
       "cfprEpqosDefinitionDelTaskTable": cfprEpqosDefinitionDelTaskTable,
       "cfprEpqosDefinitionDelTaskEntry": cfprEpqosDefinitionDelTaskEntry,
       "cfprEpqosDefinitionDelTaskInstanceId": cfprEpqosDefinitionDelTaskInstanceId,
       "cfprEpqosDefinitionDelTaskDn": cfprEpqosDefinitionDelTaskDn,
       "cfprEpqosDefinitionDelTaskRn": cfprEpqosDefinitionDelTaskRn,
       "cfprEpqosDefinitionDelTaskDefDn": cfprEpqosDefinitionDelTaskDefDn,
       "cfprEpqosDefinitionDelTaskDefIntId": cfprEpqosDefinitionDelTaskDefIntId,
       "cfprEpqosDefinitionDelTaskDescr": cfprEpqosDefinitionDelTaskDescr,
       "cfprEpqosDefinitionDelTaskFsmDescr": cfprEpqosDefinitionDelTaskFsmDescr,
       "cfprEpqosDefinitionDelTaskFsmPrev": cfprEpqosDefinitionDelTaskFsmPrev,
       "cfprEpqosDefinitionDelTaskFsmProgr": cfprEpqosDefinitionDelTaskFsmProgr,
       "cfprEpqosDefinitionDelTaskFsmRmtInvErrCode": cfprEpqosDefinitionDelTaskFsmRmtInvErrCode,
       "cfprEpqosDefinitionDelTaskFsmRmtInvErrDescr": cfprEpqosDefinitionDelTaskFsmRmtInvErrDescr,
       "cfprEpqosDefinitionDelTaskFsmRmtInvRslt": cfprEpqosDefinitionDelTaskFsmRmtInvRslt,
       "cfprEpqosDefinitionDelTaskFsmStageDescr": cfprEpqosDefinitionDelTaskFsmStageDescr,
       "cfprEpqosDefinitionDelTaskFsmStamp": cfprEpqosDefinitionDelTaskFsmStamp,
       "cfprEpqosDefinitionDelTaskFsmStatus": cfprEpqosDefinitionDelTaskFsmStatus,
       "cfprEpqosDefinitionDelTaskFsmTry": cfprEpqosDefinitionDelTaskFsmTry,
       "cfprEpqosDefinitionDelTaskIntId": cfprEpqosDefinitionDelTaskIntId,
       "cfprEpqosDefinitionDelTaskName": cfprEpqosDefinitionDelTaskName,
       "cfprEpqosDefinitionDelTaskPolicyLevel": cfprEpqosDefinitionDelTaskPolicyLevel,
       "cfprEpqosDefinitionDelTaskPolicyOwner": cfprEpqosDefinitionDelTaskPolicyOwner,
       "cfprEpqosDefinitionDelTaskFsmTable": cfprEpqosDefinitionDelTaskFsmTable,
       "cfprEpqosDefinitionDelTaskFsmEntry": cfprEpqosDefinitionDelTaskFsmEntry,
       "cfprEpqosDefinitionDelTaskFsmInstanceId": cfprEpqosDefinitionDelTaskFsmInstanceId,
       "cfprEpqosDefinitionDelTaskFsmDn": cfprEpqosDefinitionDelTaskFsmDn,
       "cfprEpqosDefinitionDelTaskFsmRn": cfprEpqosDefinitionDelTaskFsmRn,
       "cfprEpqosDefinitionDelTaskFsmCompletionTime": cfprEpqosDefinitionDelTaskFsmCompletionTime,
       "cfprEpqosDefinitionDelTaskFsmCurrentFsm": cfprEpqosDefinitionDelTaskFsmCurrentFsm,
       "cfprEpqosDefinitionDelTaskFsmDescrData": cfprEpqosDefinitionDelTaskFsmDescrData,
       "cfprEpqosDefinitionDelTaskFsmFsmStatus": cfprEpqosDefinitionDelTaskFsmFsmStatus,
       "cfprEpqosDefinitionDelTaskFsmProgress": cfprEpqosDefinitionDelTaskFsmProgress,
       "cfprEpqosDefinitionDelTaskFsmRmtErrCode": cfprEpqosDefinitionDelTaskFsmRmtErrCode,
       "cfprEpqosDefinitionDelTaskFsmRmtErrDescr": cfprEpqosDefinitionDelTaskFsmRmtErrDescr,
       "cfprEpqosDefinitionDelTaskFsmRmtRslt": cfprEpqosDefinitionDelTaskFsmRmtRslt,
       "cfprEpqosDefinitionDelTaskFsmStageTable": cfprEpqosDefinitionDelTaskFsmStageTable,
       "cfprEpqosDefinitionDelTaskFsmStageEntry": cfprEpqosDefinitionDelTaskFsmStageEntry,
       "cfprEpqosDefinitionDelTaskFsmStageInstanceId": cfprEpqosDefinitionDelTaskFsmStageInstanceId,
       "cfprEpqosDefinitionDelTaskFsmStageDn": cfprEpqosDefinitionDelTaskFsmStageDn,
       "cfprEpqosDefinitionDelTaskFsmStageRn": cfprEpqosDefinitionDelTaskFsmStageRn,
       "cfprEpqosDefinitionDelTaskFsmStageDescrData": cfprEpqosDefinitionDelTaskFsmStageDescrData,
       "cfprEpqosDefinitionDelTaskFsmStageLastUpdateTime": cfprEpqosDefinitionDelTaskFsmStageLastUpdateTime,
       "cfprEpqosDefinitionDelTaskFsmStageName": cfprEpqosDefinitionDelTaskFsmStageName,
       "cfprEpqosDefinitionDelTaskFsmStageOrder": cfprEpqosDefinitionDelTaskFsmStageOrder,
       "cfprEpqosDefinitionDelTaskFsmStageRetry": cfprEpqosDefinitionDelTaskFsmStageRetry,
       "cfprEpqosDefinitionDelTaskFsmStageStageStatus": cfprEpqosDefinitionDelTaskFsmStageStageStatus,
       "cfprEpqosDefinitionDelTaskFsmTaskTable": cfprEpqosDefinitionDelTaskFsmTaskTable,
       "cfprEpqosDefinitionDelTaskFsmTaskEntry": cfprEpqosDefinitionDelTaskFsmTaskEntry,
       "cfprEpqosDefinitionDelTaskFsmTaskInstanceId": cfprEpqosDefinitionDelTaskFsmTaskInstanceId,
       "cfprEpqosDefinitionDelTaskFsmTaskDn": cfprEpqosDefinitionDelTaskFsmTaskDn,
       "cfprEpqosDefinitionDelTaskFsmTaskRn": cfprEpqosDefinitionDelTaskFsmTaskRn,
       "cfprEpqosDefinitionDelTaskFsmTaskCompletion": cfprEpqosDefinitionDelTaskFsmTaskCompletion,
       "cfprEpqosDefinitionDelTaskFsmTaskFlags": cfprEpqosDefinitionDelTaskFsmTaskFlags,
       "cfprEpqosDefinitionDelTaskFsmTaskItem": cfprEpqosDefinitionDelTaskFsmTaskItem,
       "cfprEpqosDefinitionDelTaskFsmTaskSeqId": cfprEpqosDefinitionDelTaskFsmTaskSeqId,
       "cfprEpqosDefinitionFsmTable": cfprEpqosDefinitionFsmTable,
       "cfprEpqosDefinitionFsmEntry": cfprEpqosDefinitionFsmEntry,
       "cfprEpqosDefinitionFsmInstanceId": cfprEpqosDefinitionFsmInstanceId,
       "cfprEpqosDefinitionFsmDn": cfprEpqosDefinitionFsmDn,
       "cfprEpqosDefinitionFsmRn": cfprEpqosDefinitionFsmRn,
       "cfprEpqosDefinitionFsmCompletionTime": cfprEpqosDefinitionFsmCompletionTime,
       "cfprEpqosDefinitionFsmCurrentFsm": cfprEpqosDefinitionFsmCurrentFsm,
       "cfprEpqosDefinitionFsmDescrData": cfprEpqosDefinitionFsmDescrData,
       "cfprEpqosDefinitionFsmFsmStatus": cfprEpqosDefinitionFsmFsmStatus,
       "cfprEpqosDefinitionFsmProgress": cfprEpqosDefinitionFsmProgress,
       "cfprEpqosDefinitionFsmRmtErrCode": cfprEpqosDefinitionFsmRmtErrCode,
       "cfprEpqosDefinitionFsmRmtErrDescr": cfprEpqosDefinitionFsmRmtErrDescr,
       "cfprEpqosDefinitionFsmRmtRslt": cfprEpqosDefinitionFsmRmtRslt,
       "cfprEpqosDefinitionFsmStageTable": cfprEpqosDefinitionFsmStageTable,
       "cfprEpqosDefinitionFsmStageEntry": cfprEpqosDefinitionFsmStageEntry,
       "cfprEpqosDefinitionFsmStageInstanceId": cfprEpqosDefinitionFsmStageInstanceId,
       "cfprEpqosDefinitionFsmStageDn": cfprEpqosDefinitionFsmStageDn,
       "cfprEpqosDefinitionFsmStageRn": cfprEpqosDefinitionFsmStageRn,
       "cfprEpqosDefinitionFsmStageDescrData": cfprEpqosDefinitionFsmStageDescrData,
       "cfprEpqosDefinitionFsmStageLastUpdateTime": cfprEpqosDefinitionFsmStageLastUpdateTime,
       "cfprEpqosDefinitionFsmStageName": cfprEpqosDefinitionFsmStageName,
       "cfprEpqosDefinitionFsmStageOrder": cfprEpqosDefinitionFsmStageOrder,
       "cfprEpqosDefinitionFsmStageRetry": cfprEpqosDefinitionFsmStageRetry,
       "cfprEpqosDefinitionFsmStageStageStatus": cfprEpqosDefinitionFsmStageStageStatus,
       "cfprEpqosDefinitionFsmTaskTable": cfprEpqosDefinitionFsmTaskTable,
       "cfprEpqosDefinitionFsmTaskEntry": cfprEpqosDefinitionFsmTaskEntry,
       "cfprEpqosDefinitionFsmTaskInstanceId": cfprEpqosDefinitionFsmTaskInstanceId,
       "cfprEpqosDefinitionFsmTaskDn": cfprEpqosDefinitionFsmTaskDn,
       "cfprEpqosDefinitionFsmTaskRn": cfprEpqosDefinitionFsmTaskRn,
       "cfprEpqosDefinitionFsmTaskCompletion": cfprEpqosDefinitionFsmTaskCompletion,
       "cfprEpqosDefinitionFsmTaskFlags": cfprEpqosDefinitionFsmTaskFlags,
       "cfprEpqosDefinitionFsmTaskItem": cfprEpqosDefinitionFsmTaskItem,
       "cfprEpqosDefinitionFsmTaskSeqId": cfprEpqosDefinitionFsmTaskSeqId,
       "cfprEpqosEgressTable": cfprEpqosEgressTable,
       "cfprEpqosEgressEntry": cfprEpqosEgressEntry,
       "cfprEpqosEgressInstanceId": cfprEpqosEgressInstanceId,
       "cfprEpqosEgressDn": cfprEpqosEgressDn,
       "cfprEpqosEgressRn": cfprEpqosEgressRn,
       "cfprEpqosEgressBurst": cfprEpqosEgressBurst,
       "cfprEpqosEgressHostControl": cfprEpqosEgressHostControl,
       "cfprEpqosEgressName": cfprEpqosEgressName,
       "cfprEpqosEgressOperPrio": cfprEpqosEgressOperPrio,
       "cfprEpqosEgressPrio": cfprEpqosEgressPrio,
       "cfprEpqosEgressRate": cfprEpqosEgressRate}
)
