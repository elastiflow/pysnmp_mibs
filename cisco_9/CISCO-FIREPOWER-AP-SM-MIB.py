# SNMP MIB module (CISCO-FIREPOWER-AP-SM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-SM-MIB.mib
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
 CfprApSdAppInstAdminState,
 CfprApSdAppInstState,
 CfprApSdJobState,
 CfprApSdJobType,
 CfprApSmActionStages,
 CfprApSmAppClusterOperState,
 CfprApSmAppCommand,
 CfprApSmAppInstanceCurrentJobProgress) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApSdAppInstAdminState",
    "CfprApSdAppInstState",
    "CfprApSdJobState",
    "CfprApSdJobType",
    "CfprApSmActionStages",
    "CfprApSmAppClusterOperState",
    "CfprApSmAppCommand",
    "CfprApSmAppInstanceCurrentJobProgress")

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

cfprApSmObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApSmAppTable_Object = MibTable
cfprApSmAppTable = _CfprApSmAppTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 1)
)
if mibBuilder.loadTexts:
    cfprApSmAppTable.setStatus("current")
_CfprApSmAppEntry_Object = MibTableRow
cfprApSmAppEntry = _CfprApSmAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 1, 1)
)
cfprApSmAppEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmAppInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmAppEntry.setStatus("current")
_CfprApSmAppInstanceId_Type = CfprApManagedObjectId
_CfprApSmAppInstanceId_Object = MibTableColumn
cfprApSmAppInstanceId = _CfprApSmAppInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 1, 1, 1),
    _CfprApSmAppInstanceId_Type()
)
cfprApSmAppInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceId.setStatus("current")
_CfprApSmAppAttributeTable_Object = MibTable
cfprApSmAppAttributeTable = _CfprApSmAppAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 2)
)
if mibBuilder.loadTexts:
    cfprApSmAppAttributeTable.setStatus("current")
_CfprApSmAppAttributeEntry_Object = MibTableRow
cfprApSmAppAttributeEntry = _CfprApSmAppAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 2, 1)
)
cfprApSmAppAttributeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmAppAttributeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmAppAttributeEntry.setStatus("current")
_CfprApSmAppAttributeInstanceId_Type = CfprApManagedObjectId
_CfprApSmAppAttributeInstanceId_Object = MibTableColumn
cfprApSmAppAttributeInstanceId = _CfprApSmAppAttributeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 2, 1, 1),
    _CfprApSmAppAttributeInstanceId_Type()
)
cfprApSmAppAttributeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmAppAttributeInstanceId.setStatus("current")
_CfprApSmAppAttributeValueTable_Object = MibTable
cfprApSmAppAttributeValueTable = _CfprApSmAppAttributeValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 3)
)
if mibBuilder.loadTexts:
    cfprApSmAppAttributeValueTable.setStatus("current")
_CfprApSmAppAttributeValueEntry_Object = MibTableRow
cfprApSmAppAttributeValueEntry = _CfprApSmAppAttributeValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 3, 1)
)
cfprApSmAppAttributeValueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmAppAttributeValueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmAppAttributeValueEntry.setStatus("current")
_CfprApSmAppAttributeValueInstanceId_Type = CfprApManagedObjectId
_CfprApSmAppAttributeValueInstanceId_Object = MibTableColumn
cfprApSmAppAttributeValueInstanceId = _CfprApSmAppAttributeValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 3, 1, 1),
    _CfprApSmAppAttributeValueInstanceId_Type()
)
cfprApSmAppAttributeValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmAppAttributeValueInstanceId.setStatus("current")
_CfprApSmAppFsmTable_Object = MibTable
cfprApSmAppFsmTable = _CfprApSmAppFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 4)
)
if mibBuilder.loadTexts:
    cfprApSmAppFsmTable.setStatus("current")
_CfprApSmAppFsmEntry_Object = MibTableRow
cfprApSmAppFsmEntry = _CfprApSmAppFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 4, 1)
)
cfprApSmAppFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmAppFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmAppFsmEntry.setStatus("current")
_CfprApSmAppFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSmAppFsmInstanceId_Object = MibTableColumn
cfprApSmAppFsmInstanceId = _CfprApSmAppFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 4, 1, 1),
    _CfprApSmAppFsmInstanceId_Type()
)
cfprApSmAppFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmAppFsmInstanceId.setStatus("current")
_CfprApSmAppFsmStageTable_Object = MibTable
cfprApSmAppFsmStageTable = _CfprApSmAppFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 5)
)
if mibBuilder.loadTexts:
    cfprApSmAppFsmStageTable.setStatus("current")
_CfprApSmAppFsmStageEntry_Object = MibTableRow
cfprApSmAppFsmStageEntry = _CfprApSmAppFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 5, 1)
)
cfprApSmAppFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmAppFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmAppFsmStageEntry.setStatus("current")
_CfprApSmAppFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSmAppFsmStageInstanceId_Object = MibTableColumn
cfprApSmAppFsmStageInstanceId = _CfprApSmAppFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 5, 1, 1),
    _CfprApSmAppFsmStageInstanceId_Type()
)
cfprApSmAppFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmAppFsmStageInstanceId.setStatus("current")
_CfprApSmAppFsmTaskTable_Object = MibTable
cfprApSmAppFsmTaskTable = _CfprApSmAppFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 6)
)
if mibBuilder.loadTexts:
    cfprApSmAppFsmTaskTable.setStatus("current")
_CfprApSmAppFsmTaskEntry_Object = MibTableRow
cfprApSmAppFsmTaskEntry = _CfprApSmAppFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 6, 1)
)
cfprApSmAppFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmAppFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmAppFsmTaskEntry.setStatus("current")
_CfprApSmAppFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSmAppFsmTaskInstanceId_Object = MibTableColumn
cfprApSmAppFsmTaskInstanceId = _CfprApSmAppFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 6, 1, 1),
    _CfprApSmAppFsmTaskInstanceId_Type()
)
cfprApSmAppFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmAppFsmTaskInstanceId.setStatus("current")
_CfprApSmAppInstanceTable_Object = MibTable
cfprApSmAppInstanceTable = _CfprApSmAppInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7)
)
if mibBuilder.loadTexts:
    cfprApSmAppInstanceTable.setStatus("current")
_CfprApSmAppInstanceEntry_Object = MibTableRow
cfprApSmAppInstanceEntry = _CfprApSmAppInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1)
)
cfprApSmAppInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmAppInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmAppInstanceEntry.setStatus("current")
_CfprApSmAppInstanceInstanceId_Type = CfprApManagedObjectId
_CfprApSmAppInstanceInstanceId_Object = MibTableColumn
cfprApSmAppInstanceInstanceId = _CfprApSmAppInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 1),
    _CfprApSmAppInstanceInstanceId_Type()
)
cfprApSmAppInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceInstanceId.setStatus("current")
_CfprApSmAppInstanceDn_Type = CfprApManagedObjectDn
_CfprApSmAppInstanceDn_Object = MibTableColumn
cfprApSmAppInstanceDn = _CfprApSmAppInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 2),
    _CfprApSmAppInstanceDn_Type()
)
cfprApSmAppInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceDn.setStatus("current")
_CfprApSmAppInstanceRn_Type = SnmpAdminString
_CfprApSmAppInstanceRn_Object = MibTableColumn
cfprApSmAppInstanceRn = _CfprApSmAppInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 3),
    _CfprApSmAppInstanceRn_Type()
)
cfprApSmAppInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceRn.setStatus("current")
_CfprApSmAppInstanceAdminState_Type = CfprApSdAppInstAdminState
_CfprApSmAppInstanceAdminState_Object = MibTableColumn
cfprApSmAppInstanceAdminState = _CfprApSmAppInstanceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 4),
    _CfprApSmAppInstanceAdminState_Type()
)
cfprApSmAppInstanceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceAdminState.setStatus("current")
_CfprApSmAppInstanceAppInstId_Type = SnmpAdminString
_CfprApSmAppInstanceAppInstId_Object = MibTableColumn
cfprApSmAppInstanceAppInstId = _CfprApSmAppInstanceAppInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 5),
    _CfprApSmAppInstanceAppInstId_Type()
)
cfprApSmAppInstanceAppInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceAppInstId.setStatus("current")
_CfprApSmAppInstanceAppName_Type = SnmpAdminString
_CfprApSmAppInstanceAppName_Object = MibTableColumn
cfprApSmAppInstanceAppName = _CfprApSmAppInstanceAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 6),
    _CfprApSmAppInstanceAppName_Type()
)
cfprApSmAppInstanceAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceAppName.setStatus("current")
_CfprApSmAppInstanceClearLogData_Type = CfprApSmActionStages
_CfprApSmAppInstanceClearLogData_Object = MibTableColumn
cfprApSmAppInstanceClearLogData = _CfprApSmAppInstanceClearLogData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 7),
    _CfprApSmAppInstanceClearLogData_Type()
)
cfprApSmAppInstanceClearLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceClearLogData.setStatus("current")
_CfprApSmAppInstanceClusterOperationalState_Type = CfprApSmAppClusterOperState
_CfprApSmAppInstanceClusterOperationalState_Object = MibTableColumn
cfprApSmAppInstanceClusterOperationalState = _CfprApSmAppInstanceClusterOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 8),
    _CfprApSmAppInstanceClusterOperationalState_Type()
)
cfprApSmAppInstanceClusterOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceClusterOperationalState.setStatus("current")
_CfprApSmAppInstanceCurrentJobProgress_Type = CfprApSmAppInstanceCurrentJobProgress
_CfprApSmAppInstanceCurrentJobProgress_Object = MibTableColumn
cfprApSmAppInstanceCurrentJobProgress = _CfprApSmAppInstanceCurrentJobProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 9),
    _CfprApSmAppInstanceCurrentJobProgress_Type()
)
cfprApSmAppInstanceCurrentJobProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceCurrentJobProgress.setStatus("current")
_CfprApSmAppInstanceCurrentJobState_Type = CfprApSdJobState
_CfprApSmAppInstanceCurrentJobState_Object = MibTableColumn
cfprApSmAppInstanceCurrentJobState = _CfprApSmAppInstanceCurrentJobState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 10),
    _CfprApSmAppInstanceCurrentJobState_Type()
)
cfprApSmAppInstanceCurrentJobState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceCurrentJobState.setStatus("current")
_CfprApSmAppInstanceCurrentJobType_Type = CfprApSdJobType
_CfprApSmAppInstanceCurrentJobType_Object = MibTableColumn
cfprApSmAppInstanceCurrentJobType = _CfprApSmAppInstanceCurrentJobType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 11),
    _CfprApSmAppInstanceCurrentJobType_Type()
)
cfprApSmAppInstanceCurrentJobType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceCurrentJobType.setStatus("current")
_CfprApSmAppInstanceErrorMsg_Type = SnmpAdminString
_CfprApSmAppInstanceErrorMsg_Object = MibTableColumn
cfprApSmAppInstanceErrorMsg = _CfprApSmAppInstanceErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 12),
    _CfprApSmAppInstanceErrorMsg_Type()
)
cfprApSmAppInstanceErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceErrorMsg.setStatus("current")
_CfprApSmAppInstanceExecuteCmd_Type = CfprApSmAppCommand
_CfprApSmAppInstanceExecuteCmd_Object = MibTableColumn
cfprApSmAppInstanceExecuteCmd = _CfprApSmAppInstanceExecuteCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 13),
    _CfprApSmAppInstanceExecuteCmd_Type()
)
cfprApSmAppInstanceExecuteCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceExecuteCmd.setStatus("current")
_CfprApSmAppInstanceExternallyUpgraded_Type = TruthValue
_CfprApSmAppInstanceExternallyUpgraded_Object = MibTableColumn
cfprApSmAppInstanceExternallyUpgraded = _CfprApSmAppInstanceExternallyUpgraded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 14),
    _CfprApSmAppInstanceExternallyUpgraded_Type()
)
cfprApSmAppInstanceExternallyUpgraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceExternallyUpgraded.setStatus("current")
_CfprApSmAppInstanceFsmDescr_Type = SnmpAdminString
_CfprApSmAppInstanceFsmDescr_Object = MibTableColumn
cfprApSmAppInstanceFsmDescr = _CfprApSmAppInstanceFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 15),
    _CfprApSmAppInstanceFsmDescr_Type()
)
cfprApSmAppInstanceFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmDescr.setStatus("current")
_CfprApSmAppInstanceFsmPrev_Type = SnmpAdminString
_CfprApSmAppInstanceFsmPrev_Object = MibTableColumn
cfprApSmAppInstanceFsmPrev = _CfprApSmAppInstanceFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 16),
    _CfprApSmAppInstanceFsmPrev_Type()
)
cfprApSmAppInstanceFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmPrev.setStatus("current")
_CfprApSmAppInstanceFsmProgr_Type = Gauge32
_CfprApSmAppInstanceFsmProgr_Object = MibTableColumn
cfprApSmAppInstanceFsmProgr = _CfprApSmAppInstanceFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 17),
    _CfprApSmAppInstanceFsmProgr_Type()
)
cfprApSmAppInstanceFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmProgr.setStatus("current")
_CfprApSmAppInstanceFsmRmtInvErrCode_Type = Gauge32
_CfprApSmAppInstanceFsmRmtInvErrCode_Object = MibTableColumn
cfprApSmAppInstanceFsmRmtInvErrCode = _CfprApSmAppInstanceFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 18),
    _CfprApSmAppInstanceFsmRmtInvErrCode_Type()
)
cfprApSmAppInstanceFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmRmtInvErrCode.setStatus("current")
_CfprApSmAppInstanceFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSmAppInstanceFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSmAppInstanceFsmRmtInvErrDescr = _CfprApSmAppInstanceFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 19),
    _CfprApSmAppInstanceFsmRmtInvErrDescr_Type()
)
cfprApSmAppInstanceFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmRmtInvErrDescr.setStatus("current")
_CfprApSmAppInstanceFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSmAppInstanceFsmRmtInvRslt_Object = MibTableColumn
cfprApSmAppInstanceFsmRmtInvRslt = _CfprApSmAppInstanceFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 20),
    _CfprApSmAppInstanceFsmRmtInvRslt_Type()
)
cfprApSmAppInstanceFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmRmtInvRslt.setStatus("current")
_CfprApSmAppInstanceFsmStageDescr_Type = SnmpAdminString
_CfprApSmAppInstanceFsmStageDescr_Object = MibTableColumn
cfprApSmAppInstanceFsmStageDescr = _CfprApSmAppInstanceFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 21),
    _CfprApSmAppInstanceFsmStageDescr_Type()
)
cfprApSmAppInstanceFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmStageDescr.setStatus("current")
_CfprApSmAppInstanceFsmStamp_Type = DateAndTime
_CfprApSmAppInstanceFsmStamp_Object = MibTableColumn
cfprApSmAppInstanceFsmStamp = _CfprApSmAppInstanceFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 22),
    _CfprApSmAppInstanceFsmStamp_Type()
)
cfprApSmAppInstanceFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmStamp.setStatus("current")
_CfprApSmAppInstanceFsmStatus_Type = SnmpAdminString
_CfprApSmAppInstanceFsmStatus_Object = MibTableColumn
cfprApSmAppInstanceFsmStatus = _CfprApSmAppInstanceFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 23),
    _CfprApSmAppInstanceFsmStatus_Type()
)
cfprApSmAppInstanceFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmStatus.setStatus("current")
_CfprApSmAppInstanceFsmTry_Type = Gauge32
_CfprApSmAppInstanceFsmTry_Object = MibTableColumn
cfprApSmAppInstanceFsmTry = _CfprApSmAppInstanceFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 24),
    _CfprApSmAppInstanceFsmTry_Type()
)
cfprApSmAppInstanceFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmTry.setStatus("current")
_CfprApSmAppInstanceHotfix_Type = SnmpAdminString
_CfprApSmAppInstanceHotfix_Object = MibTableColumn
cfprApSmAppInstanceHotfix = _CfprApSmAppInstanceHotfix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 25),
    _CfprApSmAppInstanceHotfix_Type()
)
cfprApSmAppInstanceHotfix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceHotfix.setStatus("current")
_CfprApSmAppInstanceOperationalState_Type = CfprApSdAppInstState
_CfprApSmAppInstanceOperationalState_Object = MibTableColumn
cfprApSmAppInstanceOperationalState = _CfprApSmAppInstanceOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 26),
    _CfprApSmAppInstanceOperationalState_Type()
)
cfprApSmAppInstanceOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceOperationalState.setStatus("current")
_CfprApSmAppInstancePeerDn_Type = SnmpAdminString
_CfprApSmAppInstancePeerDn_Object = MibTableColumn
cfprApSmAppInstancePeerDn = _CfprApSmAppInstancePeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 27),
    _CfprApSmAppInstancePeerDn_Type()
)
cfprApSmAppInstancePeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstancePeerDn.setStatus("current")
_CfprApSmAppInstanceRunningVersion_Type = SnmpAdminString
_CfprApSmAppInstanceRunningVersion_Object = MibTableColumn
cfprApSmAppInstanceRunningVersion = _CfprApSmAppInstanceRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 28),
    _CfprApSmAppInstanceRunningVersion_Type()
)
cfprApSmAppInstanceRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceRunningVersion.setStatus("current")
_CfprApSmAppInstanceStartupVersion_Type = SnmpAdminString
_CfprApSmAppInstanceStartupVersion_Object = MibTableColumn
cfprApSmAppInstanceStartupVersion = _CfprApSmAppInstanceStartupVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 7, 1, 29),
    _CfprApSmAppInstanceStartupVersion_Type()
)
cfprApSmAppInstanceStartupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceStartupVersion.setStatus("current")
_CfprApSmAppInstanceFsmTable_Object = MibTable
cfprApSmAppInstanceFsmTable = _CfprApSmAppInstanceFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 8)
)
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmTable.setStatus("current")
_CfprApSmAppInstanceFsmEntry_Object = MibTableRow
cfprApSmAppInstanceFsmEntry = _CfprApSmAppInstanceFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 8, 1)
)
cfprApSmAppInstanceFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmAppInstanceFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmEntry.setStatus("current")
_CfprApSmAppInstanceFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSmAppInstanceFsmInstanceId_Object = MibTableColumn
cfprApSmAppInstanceFsmInstanceId = _CfprApSmAppInstanceFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 8, 1, 1),
    _CfprApSmAppInstanceFsmInstanceId_Type()
)
cfprApSmAppInstanceFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmInstanceId.setStatus("current")
_CfprApSmAppInstanceFsmStageTable_Object = MibTable
cfprApSmAppInstanceFsmStageTable = _CfprApSmAppInstanceFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 9)
)
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmStageTable.setStatus("current")
_CfprApSmAppInstanceFsmStageEntry_Object = MibTableRow
cfprApSmAppInstanceFsmStageEntry = _CfprApSmAppInstanceFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 9, 1)
)
cfprApSmAppInstanceFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmAppInstanceFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmStageEntry.setStatus("current")
_CfprApSmAppInstanceFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSmAppInstanceFsmStageInstanceId_Object = MibTableColumn
cfprApSmAppInstanceFsmStageInstanceId = _CfprApSmAppInstanceFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 9, 1, 1),
    _CfprApSmAppInstanceFsmStageInstanceId_Type()
)
cfprApSmAppInstanceFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmStageInstanceId.setStatus("current")
_CfprApSmAppInstanceFsmTaskTable_Object = MibTable
cfprApSmAppInstanceFsmTaskTable = _CfprApSmAppInstanceFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 10)
)
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmTaskTable.setStatus("current")
_CfprApSmAppInstanceFsmTaskEntry_Object = MibTableRow
cfprApSmAppInstanceFsmTaskEntry = _CfprApSmAppInstanceFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 10, 1)
)
cfprApSmAppInstanceFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmAppInstanceFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmTaskEntry.setStatus("current")
_CfprApSmAppInstanceFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSmAppInstanceFsmTaskInstanceId_Object = MibTableColumn
cfprApSmAppInstanceFsmTaskInstanceId = _CfprApSmAppInstanceFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 10, 1, 1),
    _CfprApSmAppInstanceFsmTaskInstanceId_Type()
)
cfprApSmAppInstanceFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmAppInstanceFsmTaskInstanceId.setStatus("current")
_CfprApSmClusterBootstrapTable_Object = MibTable
cfprApSmClusterBootstrapTable = _CfprApSmClusterBootstrapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 11)
)
if mibBuilder.loadTexts:
    cfprApSmClusterBootstrapTable.setStatus("current")
_CfprApSmClusterBootstrapEntry_Object = MibTableRow
cfprApSmClusterBootstrapEntry = _CfprApSmClusterBootstrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 11, 1)
)
cfprApSmClusterBootstrapEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmClusterBootstrapInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmClusterBootstrapEntry.setStatus("current")
_CfprApSmClusterBootstrapInstanceId_Type = CfprApManagedObjectId
_CfprApSmClusterBootstrapInstanceId_Object = MibTableColumn
cfprApSmClusterBootstrapInstanceId = _CfprApSmClusterBootstrapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 11, 1, 1),
    _CfprApSmClusterBootstrapInstanceId_Type()
)
cfprApSmClusterBootstrapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmClusterBootstrapInstanceId.setStatus("current")
_CfprApSmDiskFileSystemTable_Object = MibTable
cfprApSmDiskFileSystemTable = _CfprApSmDiskFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 12)
)
if mibBuilder.loadTexts:
    cfprApSmDiskFileSystemTable.setStatus("current")
_CfprApSmDiskFileSystemEntry_Object = MibTableRow
cfprApSmDiskFileSystemEntry = _CfprApSmDiskFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 12, 1)
)
cfprApSmDiskFileSystemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmDiskFileSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmDiskFileSystemEntry.setStatus("current")
_CfprApSmDiskFileSystemInstanceId_Type = CfprApManagedObjectId
_CfprApSmDiskFileSystemInstanceId_Object = MibTableColumn
cfprApSmDiskFileSystemInstanceId = _CfprApSmDiskFileSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 12, 1, 1),
    _CfprApSmDiskFileSystemInstanceId_Type()
)
cfprApSmDiskFileSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmDiskFileSystemInstanceId.setStatus("current")
_CfprApSmDiskFileSystemDn_Type = CfprApManagedObjectDn
_CfprApSmDiskFileSystemDn_Object = MibTableColumn
cfprApSmDiskFileSystemDn = _CfprApSmDiskFileSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 12, 1, 2),
    _CfprApSmDiskFileSystemDn_Type()
)
cfprApSmDiskFileSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmDiskFileSystemDn.setStatus("current")
_CfprApSmDiskFileSystemRn_Type = SnmpAdminString
_CfprApSmDiskFileSystemRn_Object = MibTableColumn
cfprApSmDiskFileSystemRn = _CfprApSmDiskFileSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 12, 1, 3),
    _CfprApSmDiskFileSystemRn_Type()
)
cfprApSmDiskFileSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmDiskFileSystemRn.setStatus("current")
_CfprApSmDiskFileSystemDiskName_Type = SnmpAdminString
_CfprApSmDiskFileSystemDiskName_Object = MibTableColumn
cfprApSmDiskFileSystemDiskName = _CfprApSmDiskFileSystemDiskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 12, 1, 4),
    _CfprApSmDiskFileSystemDiskName_Type()
)
cfprApSmDiskFileSystemDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmDiskFileSystemDiskName.setStatus("current")
_CfprApSmDiskFileSystemFileSystem_Type = SnmpAdminString
_CfprApSmDiskFileSystemFileSystem_Object = MibTableColumn
cfprApSmDiskFileSystemFileSystem = _CfprApSmDiskFileSystemFileSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 12, 1, 5),
    _CfprApSmDiskFileSystemFileSystem_Type()
)
cfprApSmDiskFileSystemFileSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmDiskFileSystemFileSystem.setStatus("current")
_CfprApSmDiskFileSystemMountPoint_Type = SnmpAdminString
_CfprApSmDiskFileSystemMountPoint_Object = MibTableColumn
cfprApSmDiskFileSystemMountPoint = _CfprApSmDiskFileSystemMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 12, 1, 7),
    _CfprApSmDiskFileSystemMountPoint_Type()
)
cfprApSmDiskFileSystemMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmDiskFileSystemMountPoint.setStatus("current")
_CfprApSmEncryptedKeyTable_Object = MibTable
cfprApSmEncryptedKeyTable = _CfprApSmEncryptedKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 13)
)
if mibBuilder.loadTexts:
    cfprApSmEncryptedKeyTable.setStatus("current")
_CfprApSmEncryptedKeyEntry_Object = MibTableRow
cfprApSmEncryptedKeyEntry = _CfprApSmEncryptedKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 13, 1)
)
cfprApSmEncryptedKeyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmEncryptedKeyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmEncryptedKeyEntry.setStatus("current")
_CfprApSmEncryptedKeyInstanceId_Type = CfprApManagedObjectId
_CfprApSmEncryptedKeyInstanceId_Object = MibTableColumn
cfprApSmEncryptedKeyInstanceId = _CfprApSmEncryptedKeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 13, 1, 1),
    _CfprApSmEncryptedKeyInstanceId_Type()
)
cfprApSmEncryptedKeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmEncryptedKeyInstanceId.setStatus("current")
_CfprApSmExternalPortLinkTable_Object = MibTable
cfprApSmExternalPortLinkTable = _CfprApSmExternalPortLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 14)
)
if mibBuilder.loadTexts:
    cfprApSmExternalPortLinkTable.setStatus("current")
_CfprApSmExternalPortLinkEntry_Object = MibTableRow
cfprApSmExternalPortLinkEntry = _CfprApSmExternalPortLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 14, 1)
)
cfprApSmExternalPortLinkEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmExternalPortLinkInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmExternalPortLinkEntry.setStatus("current")
_CfprApSmExternalPortLinkInstanceId_Type = CfprApManagedObjectId
_CfprApSmExternalPortLinkInstanceId_Object = MibTableColumn
cfprApSmExternalPortLinkInstanceId = _CfprApSmExternalPortLinkInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 14, 1, 1),
    _CfprApSmExternalPortLinkInstanceId_Type()
)
cfprApSmExternalPortLinkInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmExternalPortLinkInstanceId.setStatus("current")
_CfprApSmHeartbeatTable_Object = MibTable
cfprApSmHeartbeatTable = _CfprApSmHeartbeatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 15)
)
if mibBuilder.loadTexts:
    cfprApSmHeartbeatTable.setStatus("current")
_CfprApSmHeartbeatEntry_Object = MibTableRow
cfprApSmHeartbeatEntry = _CfprApSmHeartbeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 15, 1)
)
cfprApSmHeartbeatEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmHeartbeatInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmHeartbeatEntry.setStatus("current")
_CfprApSmHeartbeatInstanceId_Type = CfprApManagedObjectId
_CfprApSmHeartbeatInstanceId_Object = MibTableColumn
cfprApSmHeartbeatInstanceId = _CfprApSmHeartbeatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 15, 1, 1),
    _CfprApSmHeartbeatInstanceId_Type()
)
cfprApSmHeartbeatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmHeartbeatInstanceId.setStatus("current")
_CfprApSmHeartbeatConfigTable_Object = MibTable
cfprApSmHeartbeatConfigTable = _CfprApSmHeartbeatConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 16)
)
if mibBuilder.loadTexts:
    cfprApSmHeartbeatConfigTable.setStatus("current")
_CfprApSmHeartbeatConfigEntry_Object = MibTableRow
cfprApSmHeartbeatConfigEntry = _CfprApSmHeartbeatConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 16, 1)
)
cfprApSmHeartbeatConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmHeartbeatConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmHeartbeatConfigEntry.setStatus("current")
_CfprApSmHeartbeatConfigInstanceId_Type = CfprApManagedObjectId
_CfprApSmHeartbeatConfigInstanceId_Object = MibTableColumn
cfprApSmHeartbeatConfigInstanceId = _CfprApSmHeartbeatConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 16, 1, 1),
    _CfprApSmHeartbeatConfigInstanceId_Type()
)
cfprApSmHeartbeatConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmHeartbeatConfigInstanceId.setStatus("current")
_CfprApSmIPTable_Object = MibTable
cfprApSmIPTable = _CfprApSmIPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 17)
)
if mibBuilder.loadTexts:
    cfprApSmIPTable.setStatus("current")
_CfprApSmIPEntry_Object = MibTableRow
cfprApSmIPEntry = _CfprApSmIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 17, 1)
)
cfprApSmIPEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmIPInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmIPEntry.setStatus("current")
_CfprApSmIPInstanceId_Type = CfprApManagedObjectId
_CfprApSmIPInstanceId_Object = MibTableColumn
cfprApSmIPInstanceId = _CfprApSmIPInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 17, 1, 1),
    _CfprApSmIPInstanceId_Type()
)
cfprApSmIPInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmIPInstanceId.setStatus("current")
_CfprApSmIPV6Table_Object = MibTable
cfprApSmIPV6Table = _CfprApSmIPV6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 18)
)
if mibBuilder.loadTexts:
    cfprApSmIPV6Table.setStatus("current")
_CfprApSmIPV6Entry_Object = MibTableRow
cfprApSmIPV6Entry = _CfprApSmIPV6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 18, 1)
)
cfprApSmIPV6Entry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmIPV6InstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmIPV6Entry.setStatus("current")
_CfprApSmIPV6InstanceId_Type = CfprApManagedObjectId
_CfprApSmIPV6InstanceId_Object = MibTableColumn
cfprApSmIPV6InstanceId = _CfprApSmIPV6InstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 18, 1, 1),
    _CfprApSmIPV6InstanceId_Type()
)
cfprApSmIPV6InstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmIPV6InstanceId.setStatus("current")
_CfprApSmKeyTable_Object = MibTable
cfprApSmKeyTable = _CfprApSmKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 19)
)
if mibBuilder.loadTexts:
    cfprApSmKeyTable.setStatus("current")
_CfprApSmKeyEntry_Object = MibTableRow
cfprApSmKeyEntry = _CfprApSmKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 19, 1)
)
cfprApSmKeyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmKeyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmKeyEntry.setStatus("current")
_CfprApSmKeyInstanceId_Type = CfprApManagedObjectId
_CfprApSmKeyInstanceId_Object = MibTableColumn
cfprApSmKeyInstanceId = _CfprApSmKeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 19, 1, 1),
    _CfprApSmKeyInstanceId_Type()
)
cfprApSmKeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmKeyInstanceId.setStatus("current")
_CfprApSmLDTemplateTable_Object = MibTable
cfprApSmLDTemplateTable = _CfprApSmLDTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 20)
)
if mibBuilder.loadTexts:
    cfprApSmLDTemplateTable.setStatus("current")
_CfprApSmLDTemplateEntry_Object = MibTableRow
cfprApSmLDTemplateEntry = _CfprApSmLDTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 20, 1)
)
cfprApSmLDTemplateEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmLDTemplateInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmLDTemplateEntry.setStatus("current")
_CfprApSmLDTemplateInstanceId_Type = CfprApManagedObjectId
_CfprApSmLDTemplateInstanceId_Object = MibTableColumn
cfprApSmLDTemplateInstanceId = _CfprApSmLDTemplateInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 20, 1, 1),
    _CfprApSmLDTemplateInstanceId_Type()
)
cfprApSmLDTemplateInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmLDTemplateInstanceId.setStatus("current")
_CfprApSmLogicalDeviceTable_Object = MibTable
cfprApSmLogicalDeviceTable = _CfprApSmLogicalDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 21)
)
if mibBuilder.loadTexts:
    cfprApSmLogicalDeviceTable.setStatus("current")
_CfprApSmLogicalDeviceEntry_Object = MibTableRow
cfprApSmLogicalDeviceEntry = _CfprApSmLogicalDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 21, 1)
)
cfprApSmLogicalDeviceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmLogicalDeviceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmLogicalDeviceEntry.setStatus("current")
_CfprApSmLogicalDeviceInstanceId_Type = CfprApManagedObjectId
_CfprApSmLogicalDeviceInstanceId_Object = MibTableColumn
cfprApSmLogicalDeviceInstanceId = _CfprApSmLogicalDeviceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 21, 1, 1),
    _CfprApSmLogicalDeviceInstanceId_Type()
)
cfprApSmLogicalDeviceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmLogicalDeviceInstanceId.setStatus("current")
_CfprApSmMgmtBootstrapTable_Object = MibTable
cfprApSmMgmtBootstrapTable = _CfprApSmMgmtBootstrapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 22)
)
if mibBuilder.loadTexts:
    cfprApSmMgmtBootstrapTable.setStatus("current")
_CfprApSmMgmtBootstrapEntry_Object = MibTableRow
cfprApSmMgmtBootstrapEntry = _CfprApSmMgmtBootstrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 22, 1)
)
cfprApSmMgmtBootstrapEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmMgmtBootstrapInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmMgmtBootstrapEntry.setStatus("current")
_CfprApSmMgmtBootstrapInstanceId_Type = CfprApManagedObjectId
_CfprApSmMgmtBootstrapInstanceId_Object = MibTableColumn
cfprApSmMgmtBootstrapInstanceId = _CfprApSmMgmtBootstrapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 22, 1, 1),
    _CfprApSmMgmtBootstrapInstanceId_Type()
)
cfprApSmMgmtBootstrapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmMgmtBootstrapInstanceId.setStatus("current")
_CfprApSmMonitorTable_Object = MibTable
cfprApSmMonitorTable = _CfprApSmMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23)
)
if mibBuilder.loadTexts:
    cfprApSmMonitorTable.setStatus("current")
_CfprApSmMonitorEntry_Object = MibTableRow
cfprApSmMonitorEntry = _CfprApSmMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1)
)
cfprApSmMonitorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmMonitorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmMonitorEntry.setStatus("current")
_CfprApSmMonitorInstanceId_Type = CfprApManagedObjectId
_CfprApSmMonitorInstanceId_Object = MibTableColumn
cfprApSmMonitorInstanceId = _CfprApSmMonitorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 1),
    _CfprApSmMonitorInstanceId_Type()
)
cfprApSmMonitorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmMonitorInstanceId.setStatus("current")
_CfprApSmMonitorDn_Type = CfprApManagedObjectDn
_CfprApSmMonitorDn_Object = MibTableColumn
cfprApSmMonitorDn = _CfprApSmMonitorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 2),
    _CfprApSmMonitorDn_Type()
)
cfprApSmMonitorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorDn.setStatus("current")
_CfprApSmMonitorRn_Type = SnmpAdminString
_CfprApSmMonitorRn_Object = MibTableColumn
cfprApSmMonitorRn = _CfprApSmMonitorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 3),
    _CfprApSmMonitorRn_Type()
)
cfprApSmMonitorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorRn.setStatus("current")
_CfprApSmMonitorBladeUptime_Type = SnmpAdminString
_CfprApSmMonitorBladeUptime_Object = MibTableColumn
cfprApSmMonitorBladeUptime = _CfprApSmMonitorBladeUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 4),
    _CfprApSmMonitorBladeUptime_Type()
)
cfprApSmMonitorBladeUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorBladeUptime.setStatus("current")
_CfprApSmMonitorCpuTotalLoadAvg15min_Type = Integer32
_CfprApSmMonitorCpuTotalLoadAvg15min_Object = MibTableColumn
cfprApSmMonitorCpuTotalLoadAvg15min = _CfprApSmMonitorCpuTotalLoadAvg15min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 5),
    _CfprApSmMonitorCpuTotalLoadAvg15min_Type()
)
cfprApSmMonitorCpuTotalLoadAvg15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorCpuTotalLoadAvg15min.setStatus("current")
_CfprApSmMonitorCpuTotalLoadAvg1min_Type = Integer32
_CfprApSmMonitorCpuTotalLoadAvg1min_Object = MibTableColumn
cfprApSmMonitorCpuTotalLoadAvg1min = _CfprApSmMonitorCpuTotalLoadAvg1min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 6),
    _CfprApSmMonitorCpuTotalLoadAvg1min_Type()
)
cfprApSmMonitorCpuTotalLoadAvg1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorCpuTotalLoadAvg1min.setStatus("current")
_CfprApSmMonitorCpuTotalLoadAvg5min_Type = Integer32
_CfprApSmMonitorCpuTotalLoadAvg5min_Object = MibTableColumn
cfprApSmMonitorCpuTotalLoadAvg5min = _CfprApSmMonitorCpuTotalLoadAvg5min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 7),
    _CfprApSmMonitorCpuTotalLoadAvg5min_Type()
)
cfprApSmMonitorCpuTotalLoadAvg5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorCpuTotalLoadAvg5min.setStatus("current")
_CfprApSmMonitorDiskFileSystemCount_Type = Gauge32
_CfprApSmMonitorDiskFileSystemCount_Object = MibTableColumn
cfprApSmMonitorDiskFileSystemCount = _CfprApSmMonitorDiskFileSystemCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 8),
    _CfprApSmMonitorDiskFileSystemCount_Type()
)
cfprApSmMonitorDiskFileSystemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorDiskFileSystemCount.setStatus("current")
_CfprApSmMonitorOsVersion_Type = SnmpAdminString
_CfprApSmMonitorOsVersion_Object = MibTableColumn
cfprApSmMonitorOsVersion = _CfprApSmMonitorOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 13),
    _CfprApSmMonitorOsVersion_Type()
)
cfprApSmMonitorOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorOsVersion.setStatus("current")
_CfprApSmMonitorUpdateTimestamp_Type = DateAndTime
_CfprApSmMonitorUpdateTimestamp_Object = MibTableColumn
cfprApSmMonitorUpdateTimestamp = _CfprApSmMonitorUpdateTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 14),
    _CfprApSmMonitorUpdateTimestamp_Type()
)
cfprApSmMonitorUpdateTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorUpdateTimestamp.setStatus("current")
_CfprApSmMonitorMemAppTotal_Type = Gauge32
_CfprApSmMonitorMemAppTotal_Object = MibTableColumn
cfprApSmMonitorMemAppTotal = _CfprApSmMonitorMemAppTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 15),
    _CfprApSmMonitorMemAppTotal_Type()
)
cfprApSmMonitorMemAppTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorMemAppTotal.setStatus("current")
_CfprApSmMonitorMemFree_Type = Gauge32
_CfprApSmMonitorMemFree_Object = MibTableColumn
cfprApSmMonitorMemFree = _CfprApSmMonitorMemFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 16),
    _CfprApSmMonitorMemFree_Type()
)
cfprApSmMonitorMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorMemFree.setStatus("current")
_CfprApSmMonitorMemTotal_Type = Gauge32
_CfprApSmMonitorMemTotal_Object = MibTableColumn
cfprApSmMonitorMemTotal = _CfprApSmMonitorMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 17),
    _CfprApSmMonitorMemTotal_Type()
)
cfprApSmMonitorMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorMemTotal.setStatus("current")
_CfprApSmMonitorMemUsed_Type = Gauge32
_CfprApSmMonitorMemUsed_Object = MibTableColumn
cfprApSmMonitorMemUsed = _CfprApSmMonitorMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 23, 1, 18),
    _CfprApSmMonitorMemUsed_Type()
)
cfprApSmMonitorMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSmMonitorMemUsed.setStatus("current")
_CfprApSmNetMgmtBootstrapKeyEnumValueTable_Object = MibTable
cfprApSmNetMgmtBootstrapKeyEnumValueTable = _CfprApSmNetMgmtBootstrapKeyEnumValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 24)
)
if mibBuilder.loadTexts:
    cfprApSmNetMgmtBootstrapKeyEnumValueTable.setStatus("current")
_CfprApSmNetMgmtBootstrapKeyEnumValueEntry_Object = MibTableRow
cfprApSmNetMgmtBootstrapKeyEnumValueEntry = _CfprApSmNetMgmtBootstrapKeyEnumValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 24, 1)
)
cfprApSmNetMgmtBootstrapKeyEnumValueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmNetMgmtBootstrapKeyEnumValueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmNetMgmtBootstrapKeyEnumValueEntry.setStatus("current")
_CfprApSmNetMgmtBootstrapKeyEnumValueInstanceId_Type = CfprApManagedObjectId
_CfprApSmNetMgmtBootstrapKeyEnumValueInstanceId_Object = MibTableColumn
cfprApSmNetMgmtBootstrapKeyEnumValueInstanceId = _CfprApSmNetMgmtBootstrapKeyEnumValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 24, 1, 1),
    _CfprApSmNetMgmtBootstrapKeyEnumValueInstanceId_Type()
)
cfprApSmNetMgmtBootstrapKeyEnumValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmNetMgmtBootstrapKeyEnumValueInstanceId.setStatus("current")
_CfprApSmNetMgmtBootstrapKeyLimitsTable_Object = MibTable
cfprApSmNetMgmtBootstrapKeyLimitsTable = _CfprApSmNetMgmtBootstrapKeyLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 25)
)
if mibBuilder.loadTexts:
    cfprApSmNetMgmtBootstrapKeyLimitsTable.setStatus("current")
_CfprApSmNetMgmtBootstrapKeyLimitsEntry_Object = MibTableRow
cfprApSmNetMgmtBootstrapKeyLimitsEntry = _CfprApSmNetMgmtBootstrapKeyLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 25, 1)
)
cfprApSmNetMgmtBootstrapKeyLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmNetMgmtBootstrapKeyLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmNetMgmtBootstrapKeyLimitsEntry.setStatus("current")
_CfprApSmNetMgmtBootstrapKeyLimitsInstanceId_Type = CfprApManagedObjectId
_CfprApSmNetMgmtBootstrapKeyLimitsInstanceId_Object = MibTableColumn
cfprApSmNetMgmtBootstrapKeyLimitsInstanceId = _CfprApSmNetMgmtBootstrapKeyLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 25, 1, 1),
    _CfprApSmNetMgmtBootstrapKeyLimitsInstanceId_Type()
)
cfprApSmNetMgmtBootstrapKeyLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmNetMgmtBootstrapKeyLimitsInstanceId.setStatus("current")
_CfprApSmNetMgmtBootstrapValueTable_Object = MibTable
cfprApSmNetMgmtBootstrapValueTable = _CfprApSmNetMgmtBootstrapValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 26)
)
if mibBuilder.loadTexts:
    cfprApSmNetMgmtBootstrapValueTable.setStatus("current")
_CfprApSmNetMgmtBootstrapValueEntry_Object = MibTableRow
cfprApSmNetMgmtBootstrapValueEntry = _CfprApSmNetMgmtBootstrapValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 26, 1)
)
cfprApSmNetMgmtBootstrapValueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmNetMgmtBootstrapValueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmNetMgmtBootstrapValueEntry.setStatus("current")
_CfprApSmNetMgmtBootstrapValueInstanceId_Type = CfprApManagedObjectId
_CfprApSmNetMgmtBootstrapValueInstanceId_Object = MibTableColumn
cfprApSmNetMgmtBootstrapValueInstanceId = _CfprApSmNetMgmtBootstrapValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 26, 1, 1),
    _CfprApSmNetMgmtBootstrapValueInstanceId_Type()
)
cfprApSmNetMgmtBootstrapValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmNetMgmtBootstrapValueInstanceId.setStatus("current")
_CfprApSmPortRequirementTable_Object = MibTable
cfprApSmPortRequirementTable = _CfprApSmPortRequirementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 27)
)
if mibBuilder.loadTexts:
    cfprApSmPortRequirementTable.setStatus("current")
_CfprApSmPortRequirementEntry_Object = MibTableRow
cfprApSmPortRequirementEntry = _CfprApSmPortRequirementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 27, 1)
)
cfprApSmPortRequirementEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmPortRequirementInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmPortRequirementEntry.setStatus("current")
_CfprApSmPortRequirementInstanceId_Type = CfprApManagedObjectId
_CfprApSmPortRequirementInstanceId_Object = MibTableColumn
cfprApSmPortRequirementInstanceId = _CfprApSmPortRequirementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 27, 1, 1),
    _CfprApSmPortRequirementInstanceId_Type()
)
cfprApSmPortRequirementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmPortRequirementInstanceId.setStatus("current")
_CfprApSmPortSubTypeTable_Object = MibTable
cfprApSmPortSubTypeTable = _CfprApSmPortSubTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 28)
)
if mibBuilder.loadTexts:
    cfprApSmPortSubTypeTable.setStatus("current")
_CfprApSmPortSubTypeEntry_Object = MibTableRow
cfprApSmPortSubTypeEntry = _CfprApSmPortSubTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 28, 1)
)
cfprApSmPortSubTypeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmPortSubTypeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmPortSubTypeEntry.setStatus("current")
_CfprApSmPortSubTypeInstanceId_Type = CfprApManagedObjectId
_CfprApSmPortSubTypeInstanceId_Object = MibTableColumn
cfprApSmPortSubTypeInstanceId = _CfprApSmPortSubTypeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 28, 1, 1),
    _CfprApSmPortSubTypeInstanceId_Type()
)
cfprApSmPortSubTypeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmPortSubTypeInstanceId.setStatus("current")
_CfprApSmResourceTable_Object = MibTable
cfprApSmResourceTable = _CfprApSmResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 29)
)
if mibBuilder.loadTexts:
    cfprApSmResourceTable.setStatus("current")
_CfprApSmResourceEntry_Object = MibTableRow
cfprApSmResourceEntry = _CfprApSmResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 29, 1)
)
cfprApSmResourceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmResourceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmResourceEntry.setStatus("current")
_CfprApSmResourceInstanceId_Type = CfprApManagedObjectId
_CfprApSmResourceInstanceId_Object = MibTableColumn
cfprApSmResourceInstanceId = _CfprApSmResourceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 29, 1, 1),
    _CfprApSmResourceInstanceId_Type()
)
cfprApSmResourceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmResourceInstanceId.setStatus("current")
_CfprApSmSecSvcTable_Object = MibTable
cfprApSmSecSvcTable = _CfprApSmSecSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 30)
)
if mibBuilder.loadTexts:
    cfprApSmSecSvcTable.setStatus("current")
_CfprApSmSecSvcEntry_Object = MibTableRow
cfprApSmSecSvcEntry = _CfprApSmSecSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 30, 1)
)
cfprApSmSecSvcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmSecSvcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmSecSvcEntry.setStatus("current")
_CfprApSmSecSvcInstanceId_Type = CfprApManagedObjectId
_CfprApSmSecSvcInstanceId_Object = MibTableColumn
cfprApSmSecSvcInstanceId = _CfprApSmSecSvcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 30, 1, 1),
    _CfprApSmSecSvcInstanceId_Type()
)
cfprApSmSecSvcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmSecSvcInstanceId.setStatus("current")
_CfprApSmSecSvcFsmTable_Object = MibTable
cfprApSmSecSvcFsmTable = _CfprApSmSecSvcFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 31)
)
if mibBuilder.loadTexts:
    cfprApSmSecSvcFsmTable.setStatus("current")
_CfprApSmSecSvcFsmEntry_Object = MibTableRow
cfprApSmSecSvcFsmEntry = _CfprApSmSecSvcFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 31, 1)
)
cfprApSmSecSvcFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmSecSvcFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmSecSvcFsmEntry.setStatus("current")
_CfprApSmSecSvcFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSmSecSvcFsmInstanceId_Object = MibTableColumn
cfprApSmSecSvcFsmInstanceId = _CfprApSmSecSvcFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 31, 1, 1),
    _CfprApSmSecSvcFsmInstanceId_Type()
)
cfprApSmSecSvcFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmSecSvcFsmInstanceId.setStatus("current")
_CfprApSmSecSvcFsmStageTable_Object = MibTable
cfprApSmSecSvcFsmStageTable = _CfprApSmSecSvcFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 32)
)
if mibBuilder.loadTexts:
    cfprApSmSecSvcFsmStageTable.setStatus("current")
_CfprApSmSecSvcFsmStageEntry_Object = MibTableRow
cfprApSmSecSvcFsmStageEntry = _CfprApSmSecSvcFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 32, 1)
)
cfprApSmSecSvcFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmSecSvcFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmSecSvcFsmStageEntry.setStatus("current")
_CfprApSmSecSvcFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSmSecSvcFsmStageInstanceId_Object = MibTableColumn
cfprApSmSecSvcFsmStageInstanceId = _CfprApSmSecSvcFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 32, 1, 1),
    _CfprApSmSecSvcFsmStageInstanceId_Type()
)
cfprApSmSecSvcFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmSecSvcFsmStageInstanceId.setStatus("current")
_CfprApSmSecSvcFsmTaskTable_Object = MibTable
cfprApSmSecSvcFsmTaskTable = _CfprApSmSecSvcFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 33)
)
if mibBuilder.loadTexts:
    cfprApSmSecSvcFsmTaskTable.setStatus("current")
_CfprApSmSecSvcFsmTaskEntry_Object = MibTableRow
cfprApSmSecSvcFsmTaskEntry = _CfprApSmSecSvcFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 33, 1)
)
cfprApSmSecSvcFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmSecSvcFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmSecSvcFsmTaskEntry.setStatus("current")
_CfprApSmSecSvcFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSmSecSvcFsmTaskInstanceId_Object = MibTableColumn
cfprApSmSecSvcFsmTaskInstanceId = _CfprApSmSecSvcFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 33, 1, 1),
    _CfprApSmSecSvcFsmTaskInstanceId_Type()
)
cfprApSmSecSvcFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmSecSvcFsmTaskInstanceId.setStatus("current")
_CfprApSmSlotTable_Object = MibTable
cfprApSmSlotTable = _CfprApSmSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 34)
)
if mibBuilder.loadTexts:
    cfprApSmSlotTable.setStatus("current")
_CfprApSmSlotEntry_Object = MibTableRow
cfprApSmSlotEntry = _CfprApSmSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 34, 1)
)
cfprApSmSlotEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmSlotInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmSlotEntry.setStatus("current")
_CfprApSmSlotInstanceId_Type = CfprApManagedObjectId
_CfprApSmSlotInstanceId_Object = MibTableColumn
cfprApSmSlotInstanceId = _CfprApSmSlotInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 34, 1, 1),
    _CfprApSmSlotInstanceId_Type()
)
cfprApSmSlotInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmSlotInstanceId.setStatus("current")
_CfprApSmSystemMacTable_Object = MibTable
cfprApSmSystemMacTable = _CfprApSmSystemMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 35)
)
if mibBuilder.loadTexts:
    cfprApSmSystemMacTable.setStatus("current")
_CfprApSmSystemMacEntry_Object = MibTableRow
cfprApSmSystemMacEntry = _CfprApSmSystemMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 35, 1)
)
cfprApSmSystemMacEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmSystemMacInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmSystemMacEntry.setStatus("current")
_CfprApSmSystemMacInstanceId_Type = CfprApManagedObjectId
_CfprApSmSystemMacInstanceId_Object = MibTableColumn
cfprApSmSystemMacInstanceId = _CfprApSmSystemMacInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 35, 1, 1),
    _CfprApSmSystemMacInstanceId_Type()
)
cfprApSmSystemMacInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmSystemMacInstanceId.setStatus("current")
_CfprApSmTemplateAppTable_Object = MibTable
cfprApSmTemplateAppTable = _CfprApSmTemplateAppTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 36)
)
if mibBuilder.loadTexts:
    cfprApSmTemplateAppTable.setStatus("current")
_CfprApSmTemplateAppEntry_Object = MibTableRow
cfprApSmTemplateAppEntry = _CfprApSmTemplateAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 36, 1)
)
cfprApSmTemplateAppEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmTemplateAppInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmTemplateAppEntry.setStatus("current")
_CfprApSmTemplateAppInstanceId_Type = CfprApManagedObjectId
_CfprApSmTemplateAppInstanceId_Object = MibTableColumn
cfprApSmTemplateAppInstanceId = _CfprApSmTemplateAppInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 36, 1, 1),
    _CfprApSmTemplateAppInstanceId_Type()
)
cfprApSmTemplateAppInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmTemplateAppInstanceId.setStatus("current")
_CfprApSmUserMacTable_Object = MibTable
cfprApSmUserMacTable = _CfprApSmUserMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 37)
)
if mibBuilder.loadTexts:
    cfprApSmUserMacTable.setStatus("current")
_CfprApSmUserMacEntry_Object = MibTableRow
cfprApSmUserMacEntry = _CfprApSmUserMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 37, 1)
)
cfprApSmUserMacEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SM-MIB", "cfprApSmUserMacInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSmUserMacEntry.setStatus("current")
_CfprApSmUserMacInstanceId_Type = CfprApManagedObjectId
_CfprApSmUserMacInstanceId_Object = MibTableColumn
cfprApSmUserMacInstanceId = _CfprApSmUserMacInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 71, 37, 1, 1),
    _CfprApSmUserMacInstanceId_Type()
)
cfprApSmUserMacInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSmUserMacInstanceId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-SM-MIB",
    **{"cfprApSmObjects": cfprApSmObjects,
       "cfprApSmAppTable": cfprApSmAppTable,
       "cfprApSmAppEntry": cfprApSmAppEntry,
       "cfprApSmAppInstanceId": cfprApSmAppInstanceId,
       "cfprApSmAppAttributeTable": cfprApSmAppAttributeTable,
       "cfprApSmAppAttributeEntry": cfprApSmAppAttributeEntry,
       "cfprApSmAppAttributeInstanceId": cfprApSmAppAttributeInstanceId,
       "cfprApSmAppAttributeValueTable": cfprApSmAppAttributeValueTable,
       "cfprApSmAppAttributeValueEntry": cfprApSmAppAttributeValueEntry,
       "cfprApSmAppAttributeValueInstanceId": cfprApSmAppAttributeValueInstanceId,
       "cfprApSmAppFsmTable": cfprApSmAppFsmTable,
       "cfprApSmAppFsmEntry": cfprApSmAppFsmEntry,
       "cfprApSmAppFsmInstanceId": cfprApSmAppFsmInstanceId,
       "cfprApSmAppFsmStageTable": cfprApSmAppFsmStageTable,
       "cfprApSmAppFsmStageEntry": cfprApSmAppFsmStageEntry,
       "cfprApSmAppFsmStageInstanceId": cfprApSmAppFsmStageInstanceId,
       "cfprApSmAppFsmTaskTable": cfprApSmAppFsmTaskTable,
       "cfprApSmAppFsmTaskEntry": cfprApSmAppFsmTaskEntry,
       "cfprApSmAppFsmTaskInstanceId": cfprApSmAppFsmTaskInstanceId,
       "cfprApSmAppInstanceTable": cfprApSmAppInstanceTable,
       "cfprApSmAppInstanceEntry": cfprApSmAppInstanceEntry,
       "cfprApSmAppInstanceInstanceId": cfprApSmAppInstanceInstanceId,
       "cfprApSmAppInstanceDn": cfprApSmAppInstanceDn,
       "cfprApSmAppInstanceRn": cfprApSmAppInstanceRn,
       "cfprApSmAppInstanceAdminState": cfprApSmAppInstanceAdminState,
       "cfprApSmAppInstanceAppInstId": cfprApSmAppInstanceAppInstId,
       "cfprApSmAppInstanceAppName": cfprApSmAppInstanceAppName,
       "cfprApSmAppInstanceClearLogData": cfprApSmAppInstanceClearLogData,
       "cfprApSmAppInstanceClusterOperationalState": cfprApSmAppInstanceClusterOperationalState,
       "cfprApSmAppInstanceCurrentJobProgress": cfprApSmAppInstanceCurrentJobProgress,
       "cfprApSmAppInstanceCurrentJobState": cfprApSmAppInstanceCurrentJobState,
       "cfprApSmAppInstanceCurrentJobType": cfprApSmAppInstanceCurrentJobType,
       "cfprApSmAppInstanceErrorMsg": cfprApSmAppInstanceErrorMsg,
       "cfprApSmAppInstanceExecuteCmd": cfprApSmAppInstanceExecuteCmd,
       "cfprApSmAppInstanceExternallyUpgraded": cfprApSmAppInstanceExternallyUpgraded,
       "cfprApSmAppInstanceFsmDescr": cfprApSmAppInstanceFsmDescr,
       "cfprApSmAppInstanceFsmPrev": cfprApSmAppInstanceFsmPrev,
       "cfprApSmAppInstanceFsmProgr": cfprApSmAppInstanceFsmProgr,
       "cfprApSmAppInstanceFsmRmtInvErrCode": cfprApSmAppInstanceFsmRmtInvErrCode,
       "cfprApSmAppInstanceFsmRmtInvErrDescr": cfprApSmAppInstanceFsmRmtInvErrDescr,
       "cfprApSmAppInstanceFsmRmtInvRslt": cfprApSmAppInstanceFsmRmtInvRslt,
       "cfprApSmAppInstanceFsmStageDescr": cfprApSmAppInstanceFsmStageDescr,
       "cfprApSmAppInstanceFsmStamp": cfprApSmAppInstanceFsmStamp,
       "cfprApSmAppInstanceFsmStatus": cfprApSmAppInstanceFsmStatus,
       "cfprApSmAppInstanceFsmTry": cfprApSmAppInstanceFsmTry,
       "cfprApSmAppInstanceHotfix": cfprApSmAppInstanceHotfix,
       "cfprApSmAppInstanceOperationalState": cfprApSmAppInstanceOperationalState,
       "cfprApSmAppInstancePeerDn": cfprApSmAppInstancePeerDn,
       "cfprApSmAppInstanceRunningVersion": cfprApSmAppInstanceRunningVersion,
       "cfprApSmAppInstanceStartupVersion": cfprApSmAppInstanceStartupVersion,
       "cfprApSmAppInstanceFsmTable": cfprApSmAppInstanceFsmTable,
       "cfprApSmAppInstanceFsmEntry": cfprApSmAppInstanceFsmEntry,
       "cfprApSmAppInstanceFsmInstanceId": cfprApSmAppInstanceFsmInstanceId,
       "cfprApSmAppInstanceFsmStageTable": cfprApSmAppInstanceFsmStageTable,
       "cfprApSmAppInstanceFsmStageEntry": cfprApSmAppInstanceFsmStageEntry,
       "cfprApSmAppInstanceFsmStageInstanceId": cfprApSmAppInstanceFsmStageInstanceId,
       "cfprApSmAppInstanceFsmTaskTable": cfprApSmAppInstanceFsmTaskTable,
       "cfprApSmAppInstanceFsmTaskEntry": cfprApSmAppInstanceFsmTaskEntry,
       "cfprApSmAppInstanceFsmTaskInstanceId": cfprApSmAppInstanceFsmTaskInstanceId,
       "cfprApSmClusterBootstrapTable": cfprApSmClusterBootstrapTable,
       "cfprApSmClusterBootstrapEntry": cfprApSmClusterBootstrapEntry,
       "cfprApSmClusterBootstrapInstanceId": cfprApSmClusterBootstrapInstanceId,
       "cfprApSmDiskFileSystemTable": cfprApSmDiskFileSystemTable,
       "cfprApSmDiskFileSystemEntry": cfprApSmDiskFileSystemEntry,
       "cfprApSmDiskFileSystemInstanceId": cfprApSmDiskFileSystemInstanceId,
       "cfprApSmDiskFileSystemDn": cfprApSmDiskFileSystemDn,
       "cfprApSmDiskFileSystemRn": cfprApSmDiskFileSystemRn,
       "cfprApSmDiskFileSystemDiskName": cfprApSmDiskFileSystemDiskName,
       "cfprApSmDiskFileSystemFileSystem": cfprApSmDiskFileSystemFileSystem,
       "cfprApSmDiskFileSystemMountPoint": cfprApSmDiskFileSystemMountPoint,
       "cfprApSmEncryptedKeyTable": cfprApSmEncryptedKeyTable,
       "cfprApSmEncryptedKeyEntry": cfprApSmEncryptedKeyEntry,
       "cfprApSmEncryptedKeyInstanceId": cfprApSmEncryptedKeyInstanceId,
       "cfprApSmExternalPortLinkTable": cfprApSmExternalPortLinkTable,
       "cfprApSmExternalPortLinkEntry": cfprApSmExternalPortLinkEntry,
       "cfprApSmExternalPortLinkInstanceId": cfprApSmExternalPortLinkInstanceId,
       "cfprApSmHeartbeatTable": cfprApSmHeartbeatTable,
       "cfprApSmHeartbeatEntry": cfprApSmHeartbeatEntry,
       "cfprApSmHeartbeatInstanceId": cfprApSmHeartbeatInstanceId,
       "cfprApSmHeartbeatConfigTable": cfprApSmHeartbeatConfigTable,
       "cfprApSmHeartbeatConfigEntry": cfprApSmHeartbeatConfigEntry,
       "cfprApSmHeartbeatConfigInstanceId": cfprApSmHeartbeatConfigInstanceId,
       "cfprApSmIPTable": cfprApSmIPTable,
       "cfprApSmIPEntry": cfprApSmIPEntry,
       "cfprApSmIPInstanceId": cfprApSmIPInstanceId,
       "cfprApSmIPV6Table": cfprApSmIPV6Table,
       "cfprApSmIPV6Entry": cfprApSmIPV6Entry,
       "cfprApSmIPV6InstanceId": cfprApSmIPV6InstanceId,
       "cfprApSmKeyTable": cfprApSmKeyTable,
       "cfprApSmKeyEntry": cfprApSmKeyEntry,
       "cfprApSmKeyInstanceId": cfprApSmKeyInstanceId,
       "cfprApSmLDTemplateTable": cfprApSmLDTemplateTable,
       "cfprApSmLDTemplateEntry": cfprApSmLDTemplateEntry,
       "cfprApSmLDTemplateInstanceId": cfprApSmLDTemplateInstanceId,
       "cfprApSmLogicalDeviceTable": cfprApSmLogicalDeviceTable,
       "cfprApSmLogicalDeviceEntry": cfprApSmLogicalDeviceEntry,
       "cfprApSmLogicalDeviceInstanceId": cfprApSmLogicalDeviceInstanceId,
       "cfprApSmMgmtBootstrapTable": cfprApSmMgmtBootstrapTable,
       "cfprApSmMgmtBootstrapEntry": cfprApSmMgmtBootstrapEntry,
       "cfprApSmMgmtBootstrapInstanceId": cfprApSmMgmtBootstrapInstanceId,
       "cfprApSmMonitorTable": cfprApSmMonitorTable,
       "cfprApSmMonitorEntry": cfprApSmMonitorEntry,
       "cfprApSmMonitorInstanceId": cfprApSmMonitorInstanceId,
       "cfprApSmMonitorDn": cfprApSmMonitorDn,
       "cfprApSmMonitorRn": cfprApSmMonitorRn,
       "cfprApSmMonitorBladeUptime": cfprApSmMonitorBladeUptime,
       "cfprApSmMonitorCpuTotalLoadAvg15min": cfprApSmMonitorCpuTotalLoadAvg15min,
       "cfprApSmMonitorCpuTotalLoadAvg1min": cfprApSmMonitorCpuTotalLoadAvg1min,
       "cfprApSmMonitorCpuTotalLoadAvg5min": cfprApSmMonitorCpuTotalLoadAvg5min,
       "cfprApSmMonitorDiskFileSystemCount": cfprApSmMonitorDiskFileSystemCount,
       "cfprApSmMonitorOsVersion": cfprApSmMonitorOsVersion,
       "cfprApSmMonitorUpdateTimestamp": cfprApSmMonitorUpdateTimestamp,
       "cfprApSmMonitorMemAppTotal": cfprApSmMonitorMemAppTotal,
       "cfprApSmMonitorMemFree": cfprApSmMonitorMemFree,
       "cfprApSmMonitorMemTotal": cfprApSmMonitorMemTotal,
       "cfprApSmMonitorMemUsed": cfprApSmMonitorMemUsed,
       "cfprApSmNetMgmtBootstrapKeyEnumValueTable": cfprApSmNetMgmtBootstrapKeyEnumValueTable,
       "cfprApSmNetMgmtBootstrapKeyEnumValueEntry": cfprApSmNetMgmtBootstrapKeyEnumValueEntry,
       "cfprApSmNetMgmtBootstrapKeyEnumValueInstanceId": cfprApSmNetMgmtBootstrapKeyEnumValueInstanceId,
       "cfprApSmNetMgmtBootstrapKeyLimitsTable": cfprApSmNetMgmtBootstrapKeyLimitsTable,
       "cfprApSmNetMgmtBootstrapKeyLimitsEntry": cfprApSmNetMgmtBootstrapKeyLimitsEntry,
       "cfprApSmNetMgmtBootstrapKeyLimitsInstanceId": cfprApSmNetMgmtBootstrapKeyLimitsInstanceId,
       "cfprApSmNetMgmtBootstrapValueTable": cfprApSmNetMgmtBootstrapValueTable,
       "cfprApSmNetMgmtBootstrapValueEntry": cfprApSmNetMgmtBootstrapValueEntry,
       "cfprApSmNetMgmtBootstrapValueInstanceId": cfprApSmNetMgmtBootstrapValueInstanceId,
       "cfprApSmPortRequirementTable": cfprApSmPortRequirementTable,
       "cfprApSmPortRequirementEntry": cfprApSmPortRequirementEntry,
       "cfprApSmPortRequirementInstanceId": cfprApSmPortRequirementInstanceId,
       "cfprApSmPortSubTypeTable": cfprApSmPortSubTypeTable,
       "cfprApSmPortSubTypeEntry": cfprApSmPortSubTypeEntry,
       "cfprApSmPortSubTypeInstanceId": cfprApSmPortSubTypeInstanceId,
       "cfprApSmResourceTable": cfprApSmResourceTable,
       "cfprApSmResourceEntry": cfprApSmResourceEntry,
       "cfprApSmResourceInstanceId": cfprApSmResourceInstanceId,
       "cfprApSmSecSvcTable": cfprApSmSecSvcTable,
       "cfprApSmSecSvcEntry": cfprApSmSecSvcEntry,
       "cfprApSmSecSvcInstanceId": cfprApSmSecSvcInstanceId,
       "cfprApSmSecSvcFsmTable": cfprApSmSecSvcFsmTable,
       "cfprApSmSecSvcFsmEntry": cfprApSmSecSvcFsmEntry,
       "cfprApSmSecSvcFsmInstanceId": cfprApSmSecSvcFsmInstanceId,
       "cfprApSmSecSvcFsmStageTable": cfprApSmSecSvcFsmStageTable,
       "cfprApSmSecSvcFsmStageEntry": cfprApSmSecSvcFsmStageEntry,
       "cfprApSmSecSvcFsmStageInstanceId": cfprApSmSecSvcFsmStageInstanceId,
       "cfprApSmSecSvcFsmTaskTable": cfprApSmSecSvcFsmTaskTable,
       "cfprApSmSecSvcFsmTaskEntry": cfprApSmSecSvcFsmTaskEntry,
       "cfprApSmSecSvcFsmTaskInstanceId": cfprApSmSecSvcFsmTaskInstanceId,
       "cfprApSmSlotTable": cfprApSmSlotTable,
       "cfprApSmSlotEntry": cfprApSmSlotEntry,
       "cfprApSmSlotInstanceId": cfprApSmSlotInstanceId,
       "cfprApSmSystemMacTable": cfprApSmSystemMacTable,
       "cfprApSmSystemMacEntry": cfprApSmSystemMacEntry,
       "cfprApSmSystemMacInstanceId": cfprApSmSystemMacInstanceId,
       "cfprApSmTemplateAppTable": cfprApSmTemplateAppTable,
       "cfprApSmTemplateAppEntry": cfprApSmTemplateAppEntry,
       "cfprApSmTemplateAppInstanceId": cfprApSmTemplateAppInstanceId,
       "cfprApSmUserMacTable": cfprApSmUserMacTable,
       "cfprApSmUserMacEntry": cfprApSmUserMacEntry,
       "cfprApSmUserMacInstanceId": cfprApSmUserMacInstanceId}
)
