# SNMP MIB module (CISCO-FIREPOWER-SM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-SM-MIB.mib
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

(CfprSdAppInstAdminState,
 CfprSdAppInstState,
 CfprSdJobState,
 CfprSdJobType,
 CfprSmActionStages,
 CfprSmAppClusterOperState,
 CfprSmAppInstanceClusterRole,
 CfprSmAppInstanceCurrentJobProgress) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprSdAppInstAdminState",
    "CfprSdAppInstState",
    "CfprSdJobState",
    "CfprSdJobType",
    "CfprSmActionStages",
    "CfprSmAppClusterOperState",
    "CfprSmAppInstanceClusterRole",
    "CfprSmAppInstanceCurrentJobProgress")

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

cfprSmObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprSmAppTable_Object = MibTable
cfprSmAppTable = _CfprSmAppTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 1)
)
if mibBuilder.loadTexts:
    cfprSmAppTable.setStatus("current")
_CfprSmAppEntry_Object = MibTableRow
cfprSmAppEntry = _CfprSmAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 1, 1)
)
cfprSmAppEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppEntry.setStatus("current")
_CfprSmAppInstanceId_Type = CfprManagedObjectId
_CfprSmAppInstanceId_Object = MibTableColumn
cfprSmAppInstanceId = _CfprSmAppInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 1, 1, 1),
    _CfprSmAppInstanceId_Type()
)
cfprSmAppInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppInstanceId.setStatus("current")
_CfprSmAppAttributeTable_Object = MibTable
cfprSmAppAttributeTable = _CfprSmAppAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 2)
)
if mibBuilder.loadTexts:
    cfprSmAppAttributeTable.setStatus("current")
_CfprSmAppAttributeEntry_Object = MibTableRow
cfprSmAppAttributeEntry = _CfprSmAppAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 2, 1)
)
cfprSmAppAttributeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppAttributeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppAttributeEntry.setStatus("current")
_CfprSmAppAttributeInstanceId_Type = CfprManagedObjectId
_CfprSmAppAttributeInstanceId_Object = MibTableColumn
cfprSmAppAttributeInstanceId = _CfprSmAppAttributeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 2, 1, 1),
    _CfprSmAppAttributeInstanceId_Type()
)
cfprSmAppAttributeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppAttributeInstanceId.setStatus("current")
_CfprSmAppAttributeValueTable_Object = MibTable
cfprSmAppAttributeValueTable = _CfprSmAppAttributeValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 3)
)
if mibBuilder.loadTexts:
    cfprSmAppAttributeValueTable.setStatus("current")
_CfprSmAppAttributeValueEntry_Object = MibTableRow
cfprSmAppAttributeValueEntry = _CfprSmAppAttributeValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 3, 1)
)
cfprSmAppAttributeValueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppAttributeValueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppAttributeValueEntry.setStatus("current")
_CfprSmAppAttributeValueInstanceId_Type = CfprManagedObjectId
_CfprSmAppAttributeValueInstanceId_Object = MibTableColumn
cfprSmAppAttributeValueInstanceId = _CfprSmAppAttributeValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 3, 1, 1),
    _CfprSmAppAttributeValueInstanceId_Type()
)
cfprSmAppAttributeValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppAttributeValueInstanceId.setStatus("current")
_CfprSmAppFsmTable_Object = MibTable
cfprSmAppFsmTable = _CfprSmAppFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 4)
)
if mibBuilder.loadTexts:
    cfprSmAppFsmTable.setStatus("current")
_CfprSmAppFsmEntry_Object = MibTableRow
cfprSmAppFsmEntry = _CfprSmAppFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 4, 1)
)
cfprSmAppFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppFsmEntry.setStatus("current")
_CfprSmAppFsmInstanceId_Type = CfprManagedObjectId
_CfprSmAppFsmInstanceId_Object = MibTableColumn
cfprSmAppFsmInstanceId = _CfprSmAppFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 4, 1, 1),
    _CfprSmAppFsmInstanceId_Type()
)
cfprSmAppFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppFsmInstanceId.setStatus("current")
_CfprSmAppFsmStageTable_Object = MibTable
cfprSmAppFsmStageTable = _CfprSmAppFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 5)
)
if mibBuilder.loadTexts:
    cfprSmAppFsmStageTable.setStatus("current")
_CfprSmAppFsmStageEntry_Object = MibTableRow
cfprSmAppFsmStageEntry = _CfprSmAppFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 5, 1)
)
cfprSmAppFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppFsmStageEntry.setStatus("current")
_CfprSmAppFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSmAppFsmStageInstanceId_Object = MibTableColumn
cfprSmAppFsmStageInstanceId = _CfprSmAppFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 5, 1, 1),
    _CfprSmAppFsmStageInstanceId_Type()
)
cfprSmAppFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppFsmStageInstanceId.setStatus("current")
_CfprSmAppFsmTaskTable_Object = MibTable
cfprSmAppFsmTaskTable = _CfprSmAppFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 6)
)
if mibBuilder.loadTexts:
    cfprSmAppFsmTaskTable.setStatus("current")
_CfprSmAppFsmTaskEntry_Object = MibTableRow
cfprSmAppFsmTaskEntry = _CfprSmAppFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 6, 1)
)
cfprSmAppFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppFsmTaskEntry.setStatus("current")
_CfprSmAppFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSmAppFsmTaskInstanceId_Object = MibTableColumn
cfprSmAppFsmTaskInstanceId = _CfprSmAppFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 6, 1, 1),
    _CfprSmAppFsmTaskInstanceId_Type()
)
cfprSmAppFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppFsmTaskInstanceId.setStatus("current")
_CfprSmAppInstanceTable_Object = MibTable
cfprSmAppInstanceTable = _CfprSmAppInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7)
)
if mibBuilder.loadTexts:
    cfprSmAppInstanceTable.setStatus("current")
_CfprSmAppInstanceEntry_Object = MibTableRow
cfprSmAppInstanceEntry = _CfprSmAppInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1)
)
cfprSmAppInstanceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppInstanceEntry.setStatus("current")
_CfprSmAppInstanceInstanceId_Type = CfprManagedObjectId
_CfprSmAppInstanceInstanceId_Object = MibTableColumn
cfprSmAppInstanceInstanceId = _CfprSmAppInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 1),
    _CfprSmAppInstanceInstanceId_Type()
)
cfprSmAppInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppInstanceInstanceId.setStatus("current")
_CfprSmAppInstanceDn_Type = CfprManagedObjectDn
_CfprSmAppInstanceDn_Object = MibTableColumn
cfprSmAppInstanceDn = _CfprSmAppInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 2),
    _CfprSmAppInstanceDn_Type()
)
cfprSmAppInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceDn.setStatus("current")
_CfprSmAppInstanceRn_Type = SnmpAdminString
_CfprSmAppInstanceRn_Object = MibTableColumn
cfprSmAppInstanceRn = _CfprSmAppInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 3),
    _CfprSmAppInstanceRn_Type()
)
cfprSmAppInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceRn.setStatus("current")
_CfprSmAppInstanceAdminState_Type = CfprSdAppInstAdminState
_CfprSmAppInstanceAdminState_Object = MibTableColumn
cfprSmAppInstanceAdminState = _CfprSmAppInstanceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 4),
    _CfprSmAppInstanceAdminState_Type()
)
cfprSmAppInstanceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceAdminState.setStatus("current")
_CfprSmAppInstanceAppInstId_Type = SnmpAdminString
_CfprSmAppInstanceAppInstId_Object = MibTableColumn
cfprSmAppInstanceAppInstId = _CfprSmAppInstanceAppInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 5),
    _CfprSmAppInstanceAppInstId_Type()
)
cfprSmAppInstanceAppInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceAppInstId.setStatus("current")
_CfprSmAppInstanceAppName_Type = SnmpAdminString
_CfprSmAppInstanceAppName_Object = MibTableColumn
cfprSmAppInstanceAppName = _CfprSmAppInstanceAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 6),
    _CfprSmAppInstanceAppName_Type()
)
cfprSmAppInstanceAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceAppName.setStatus("current")
_CfprSmAppInstanceClearLogData_Type = CfprSmActionStages
_CfprSmAppInstanceClearLogData_Object = MibTableColumn
cfprSmAppInstanceClearLogData = _CfprSmAppInstanceClearLogData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 7),
    _CfprSmAppInstanceClearLogData_Type()
)
cfprSmAppInstanceClearLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceClearLogData.setStatus("current")
_CfprSmAppInstanceClusterOperationalState_Type = CfprSmAppClusterOperState
_CfprSmAppInstanceClusterOperationalState_Object = MibTableColumn
cfprSmAppInstanceClusterOperationalState = _CfprSmAppInstanceClusterOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 8),
    _CfprSmAppInstanceClusterOperationalState_Type()
)
cfprSmAppInstanceClusterOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceClusterOperationalState.setStatus("current")
_CfprSmAppInstanceCurrentJobProgress_Type = CfprSmAppInstanceCurrentJobProgress
_CfprSmAppInstanceCurrentJobProgress_Object = MibTableColumn
cfprSmAppInstanceCurrentJobProgress = _CfprSmAppInstanceCurrentJobProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 9),
    _CfprSmAppInstanceCurrentJobProgress_Type()
)
cfprSmAppInstanceCurrentJobProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceCurrentJobProgress.setStatus("current")
_CfprSmAppInstanceCurrentJobState_Type = CfprSdJobState
_CfprSmAppInstanceCurrentJobState_Object = MibTableColumn
cfprSmAppInstanceCurrentJobState = _CfprSmAppInstanceCurrentJobState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 10),
    _CfprSmAppInstanceCurrentJobState_Type()
)
cfprSmAppInstanceCurrentJobState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceCurrentJobState.setStatus("current")
_CfprSmAppInstanceCurrentJobType_Type = CfprSdJobType
_CfprSmAppInstanceCurrentJobType_Object = MibTableColumn
cfprSmAppInstanceCurrentJobType = _CfprSmAppInstanceCurrentJobType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 11),
    _CfprSmAppInstanceCurrentJobType_Type()
)
cfprSmAppInstanceCurrentJobType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceCurrentJobType.setStatus("current")
_CfprSmAppInstanceErrorMsg_Type = SnmpAdminString
_CfprSmAppInstanceErrorMsg_Object = MibTableColumn
cfprSmAppInstanceErrorMsg = _CfprSmAppInstanceErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 12),
    _CfprSmAppInstanceErrorMsg_Type()
)
cfprSmAppInstanceErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceErrorMsg.setStatus("current")
_CfprSmAppInstanceExecuteCmd_Type = Gauge32
_CfprSmAppInstanceExecuteCmd_Object = MibTableColumn
cfprSmAppInstanceExecuteCmd = _CfprSmAppInstanceExecuteCmd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 13),
    _CfprSmAppInstanceExecuteCmd_Type()
)
cfprSmAppInstanceExecuteCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceExecuteCmd.setStatus("current")
_CfprSmAppInstanceOperationalState_Type = CfprSdAppInstState
_CfprSmAppInstanceOperationalState_Object = MibTableColumn
cfprSmAppInstanceOperationalState = _CfprSmAppInstanceOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 14),
    _CfprSmAppInstanceOperationalState_Type()
)
cfprSmAppInstanceOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceOperationalState.setStatus("current")
_CfprSmAppInstancePeerDn_Type = SnmpAdminString
_CfprSmAppInstancePeerDn_Object = MibTableColumn
cfprSmAppInstancePeerDn = _CfprSmAppInstancePeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 15),
    _CfprSmAppInstancePeerDn_Type()
)
cfprSmAppInstancePeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstancePeerDn.setStatus("current")
_CfprSmAppInstanceRunningVersion_Type = SnmpAdminString
_CfprSmAppInstanceRunningVersion_Object = MibTableColumn
cfprSmAppInstanceRunningVersion = _CfprSmAppInstanceRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 16),
    _CfprSmAppInstanceRunningVersion_Type()
)
cfprSmAppInstanceRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceRunningVersion.setStatus("current")
_CfprSmAppInstanceStartupVersion_Type = SnmpAdminString
_CfprSmAppInstanceStartupVersion_Object = MibTableColumn
cfprSmAppInstanceStartupVersion = _CfprSmAppInstanceStartupVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 17),
    _CfprSmAppInstanceStartupVersion_Type()
)
cfprSmAppInstanceStartupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceStartupVersion.setStatus("current")
_CfprSmAppInstanceExternallyUpgraded_Type = TruthValue
_CfprSmAppInstanceExternallyUpgraded_Object = MibTableColumn
cfprSmAppInstanceExternallyUpgraded = _CfprSmAppInstanceExternallyUpgraded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 18),
    _CfprSmAppInstanceExternallyUpgraded_Type()
)
cfprSmAppInstanceExternallyUpgraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceExternallyUpgraded.setStatus("current")
_CfprSmAppInstanceHotfix_Type = SnmpAdminString
_CfprSmAppInstanceHotfix_Object = MibTableColumn
cfprSmAppInstanceHotfix = _CfprSmAppInstanceHotfix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 29),
    _CfprSmAppInstanceHotfix_Type()
)
cfprSmAppInstanceHotfix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceHotfix.setStatus("current")
_CfprSmAppInstanceAppDn_Type = SnmpAdminString
_CfprSmAppInstanceAppDn_Object = MibTableColumn
cfprSmAppInstanceAppDn = _CfprSmAppInstanceAppDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 30),
    _CfprSmAppInstanceAppDn_Type()
)
cfprSmAppInstanceAppDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceAppDn.setStatus("current")
_CfprSmAppInstanceClusterRole_Type = CfprSmAppInstanceClusterRole
_CfprSmAppInstanceClusterRole_Object = MibTableColumn
cfprSmAppInstanceClusterRole = _CfprSmAppInstanceClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 31),
    _CfprSmAppInstanceClusterRole_Type()
)
cfprSmAppInstanceClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceClusterRole.setStatus("current")
_CfprSmAppInstanceHasFailedReplication_Type = TruthValue
_CfprSmAppInstanceHasFailedReplication_Object = MibTableColumn
cfprSmAppInstanceHasFailedReplication = _CfprSmAppInstanceHasFailedReplication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 32),
    _CfprSmAppInstanceHasFailedReplication_Type()
)
cfprSmAppInstanceHasFailedReplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceHasFailedReplication.setStatus("current")
_CfprSmAppInstanceReasonForDebundle_Type = SnmpAdminString
_CfprSmAppInstanceReasonForDebundle_Object = MibTableColumn
cfprSmAppInstanceReasonForDebundle = _CfprSmAppInstanceReasonForDebundle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 33),
    _CfprSmAppInstanceReasonForDebundle_Type()
)
cfprSmAppInstanceReasonForDebundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceReasonForDebundle.setStatus("current")
_CfprSmAppInstanceResourceProfileName_Type = SnmpAdminString
_CfprSmAppInstanceResourceProfileName_Object = MibTableColumn
cfprSmAppInstanceResourceProfileName = _CfprSmAppInstanceResourceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 34),
    _CfprSmAppInstanceResourceProfileName_Type()
)
cfprSmAppInstanceResourceProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceResourceProfileName.setStatus("current")
_CfprSmAppInstanceVersionIncompatibleErrorMgr_Type = SnmpAdminString
_CfprSmAppInstanceVersionIncompatibleErrorMgr_Object = MibTableColumn
cfprSmAppInstanceVersionIncompatibleErrorMgr = _CfprSmAppInstanceVersionIncompatibleErrorMgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 35),
    _CfprSmAppInstanceVersionIncompatibleErrorMgr_Type()
)
cfprSmAppInstanceVersionIncompatibleErrorMgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceVersionIncompatibleErrorMgr.setStatus("current")
_CfprSmAppInstanceTurboMode_Type = TruthValue
_CfprSmAppInstanceTurboMode_Object = MibTableColumn
cfprSmAppInstanceTurboMode = _CfprSmAppInstanceTurboMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 7, 1, 36),
    _CfprSmAppInstanceTurboMode_Type()
)
cfprSmAppInstanceTurboMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmAppInstanceTurboMode.setStatus("current")
_CfprSmClusterBootstrapTable_Object = MibTable
cfprSmClusterBootstrapTable = _CfprSmClusterBootstrapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 8)
)
if mibBuilder.loadTexts:
    cfprSmClusterBootstrapTable.setStatus("current")
_CfprSmClusterBootstrapEntry_Object = MibTableRow
cfprSmClusterBootstrapEntry = _CfprSmClusterBootstrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 8, 1)
)
cfprSmClusterBootstrapEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmClusterBootstrapInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmClusterBootstrapEntry.setStatus("current")
_CfprSmClusterBootstrapInstanceId_Type = CfprManagedObjectId
_CfprSmClusterBootstrapInstanceId_Object = MibTableColumn
cfprSmClusterBootstrapInstanceId = _CfprSmClusterBootstrapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 8, 1, 1),
    _CfprSmClusterBootstrapInstanceId_Type()
)
cfprSmClusterBootstrapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmClusterBootstrapInstanceId.setStatus("current")
_CfprSmDiskFileSystemTable_Object = MibTable
cfprSmDiskFileSystemTable = _CfprSmDiskFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9)
)
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemTable.setStatus("current")
_CfprSmDiskFileSystemEntry_Object = MibTableRow
cfprSmDiskFileSystemEntry = _CfprSmDiskFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1)
)
cfprSmDiskFileSystemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmDiskFileSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemEntry.setStatus("current")
_CfprSmDiskFileSystemInstanceId_Type = CfprManagedObjectId
_CfprSmDiskFileSystemInstanceId_Object = MibTableColumn
cfprSmDiskFileSystemInstanceId = _CfprSmDiskFileSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1, 1),
    _CfprSmDiskFileSystemInstanceId_Type()
)
cfprSmDiskFileSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemInstanceId.setStatus("current")
_CfprSmDiskFileSystemDn_Type = CfprManagedObjectDn
_CfprSmDiskFileSystemDn_Object = MibTableColumn
cfprSmDiskFileSystemDn = _CfprSmDiskFileSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1, 2),
    _CfprSmDiskFileSystemDn_Type()
)
cfprSmDiskFileSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemDn.setStatus("current")
_CfprSmDiskFileSystemRn_Type = SnmpAdminString
_CfprSmDiskFileSystemRn_Object = MibTableColumn
cfprSmDiskFileSystemRn = _CfprSmDiskFileSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1, 3),
    _CfprSmDiskFileSystemRn_Type()
)
cfprSmDiskFileSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemRn.setStatus("current")
_CfprSmDiskFileSystemDiskName_Type = SnmpAdminString
_CfprSmDiskFileSystemDiskName_Object = MibTableColumn
cfprSmDiskFileSystemDiskName = _CfprSmDiskFileSystemDiskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1, 4),
    _CfprSmDiskFileSystemDiskName_Type()
)
cfprSmDiskFileSystemDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemDiskName.setStatus("current")
_CfprSmDiskFileSystemFileSystem_Type = SnmpAdminString
_CfprSmDiskFileSystemFileSystem_Object = MibTableColumn
cfprSmDiskFileSystemFileSystem = _CfprSmDiskFileSystemFileSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1, 5),
    _CfprSmDiskFileSystemFileSystem_Type()
)
cfprSmDiskFileSystemFileSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemFileSystem.setStatus("current")
_CfprSmDiskFileSystemFreeKb_Type = Gauge32
_CfprSmDiskFileSystemFreeKb_Object = MibTableColumn
cfprSmDiskFileSystemFreeKb = _CfprSmDiskFileSystemFreeKb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1, 6),
    _CfprSmDiskFileSystemFreeKb_Type()
)
cfprSmDiskFileSystemFreeKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemFreeKb.setStatus("current")
_CfprSmDiskFileSystemMountPoint_Type = SnmpAdminString
_CfprSmDiskFileSystemMountPoint_Object = MibTableColumn
cfprSmDiskFileSystemMountPoint = _CfprSmDiskFileSystemMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1, 7),
    _CfprSmDiskFileSystemMountPoint_Type()
)
cfprSmDiskFileSystemMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemMountPoint.setStatus("current")
_CfprSmDiskFileSystemTotalKb_Type = Gauge32
_CfprSmDiskFileSystemTotalKb_Object = MibTableColumn
cfprSmDiskFileSystemTotalKb = _CfprSmDiskFileSystemTotalKb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1, 8),
    _CfprSmDiskFileSystemTotalKb_Type()
)
cfprSmDiskFileSystemTotalKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemTotalKb.setStatus("current")
_CfprSmDiskFileSystemUsedKb_Type = Gauge32
_CfprSmDiskFileSystemUsedKb_Object = MibTableColumn
cfprSmDiskFileSystemUsedKb = _CfprSmDiskFileSystemUsedKb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1, 9),
    _CfprSmDiskFileSystemUsedKb_Type()
)
cfprSmDiskFileSystemUsedKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemUsedKb.setStatus("current")
_CfprSmDiskFileSystemFree_Type = Gauge32
_CfprSmDiskFileSystemFree_Object = MibTableColumn
cfprSmDiskFileSystemFree = _CfprSmDiskFileSystemFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1, 10),
    _CfprSmDiskFileSystemFree_Type()
)
cfprSmDiskFileSystemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemFree.setStatus("current")
_CfprSmDiskFileSystemTotal_Type = Gauge32
_CfprSmDiskFileSystemTotal_Object = MibTableColumn
cfprSmDiskFileSystemTotal = _CfprSmDiskFileSystemTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1, 11),
    _CfprSmDiskFileSystemTotal_Type()
)
cfprSmDiskFileSystemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemTotal.setStatus("current")
_CfprSmDiskFileSystemUsed_Type = Gauge32
_CfprSmDiskFileSystemUsed_Object = MibTableColumn
cfprSmDiskFileSystemUsed = _CfprSmDiskFileSystemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 9, 1, 12),
    _CfprSmDiskFileSystemUsed_Type()
)
cfprSmDiskFileSystemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmDiskFileSystemUsed.setStatus("current")
_CfprSmEncryptedKeyTable_Object = MibTable
cfprSmEncryptedKeyTable = _CfprSmEncryptedKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 10)
)
if mibBuilder.loadTexts:
    cfprSmEncryptedKeyTable.setStatus("current")
_CfprSmEncryptedKeyEntry_Object = MibTableRow
cfprSmEncryptedKeyEntry = _CfprSmEncryptedKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 10, 1)
)
cfprSmEncryptedKeyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmEncryptedKeyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmEncryptedKeyEntry.setStatus("current")
_CfprSmEncryptedKeyInstanceId_Type = CfprManagedObjectId
_CfprSmEncryptedKeyInstanceId_Object = MibTableColumn
cfprSmEncryptedKeyInstanceId = _CfprSmEncryptedKeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 10, 1, 1),
    _CfprSmEncryptedKeyInstanceId_Type()
)
cfprSmEncryptedKeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmEncryptedKeyInstanceId.setStatus("current")
_CfprSmExternalPortLinkTable_Object = MibTable
cfprSmExternalPortLinkTable = _CfprSmExternalPortLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 11)
)
if mibBuilder.loadTexts:
    cfprSmExternalPortLinkTable.setStatus("current")
_CfprSmExternalPortLinkEntry_Object = MibTableRow
cfprSmExternalPortLinkEntry = _CfprSmExternalPortLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 11, 1)
)
cfprSmExternalPortLinkEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmExternalPortLinkInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmExternalPortLinkEntry.setStatus("current")
_CfprSmExternalPortLinkInstanceId_Type = CfprManagedObjectId
_CfprSmExternalPortLinkInstanceId_Object = MibTableColumn
cfprSmExternalPortLinkInstanceId = _CfprSmExternalPortLinkInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 11, 1, 1),
    _CfprSmExternalPortLinkInstanceId_Type()
)
cfprSmExternalPortLinkInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmExternalPortLinkInstanceId.setStatus("current")
_CfprSmHeartbeatTable_Object = MibTable
cfprSmHeartbeatTable = _CfprSmHeartbeatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 12)
)
if mibBuilder.loadTexts:
    cfprSmHeartbeatTable.setStatus("current")
_CfprSmHeartbeatEntry_Object = MibTableRow
cfprSmHeartbeatEntry = _CfprSmHeartbeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 12, 1)
)
cfprSmHeartbeatEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmHeartbeatInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmHeartbeatEntry.setStatus("current")
_CfprSmHeartbeatInstanceId_Type = CfprManagedObjectId
_CfprSmHeartbeatInstanceId_Object = MibTableColumn
cfprSmHeartbeatInstanceId = _CfprSmHeartbeatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 12, 1, 1),
    _CfprSmHeartbeatInstanceId_Type()
)
cfprSmHeartbeatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmHeartbeatInstanceId.setStatus("current")
_CfprSmHeartbeatConfigTable_Object = MibTable
cfprSmHeartbeatConfigTable = _CfprSmHeartbeatConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 13)
)
if mibBuilder.loadTexts:
    cfprSmHeartbeatConfigTable.setStatus("current")
_CfprSmHeartbeatConfigEntry_Object = MibTableRow
cfprSmHeartbeatConfigEntry = _CfprSmHeartbeatConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 13, 1)
)
cfprSmHeartbeatConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmHeartbeatConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmHeartbeatConfigEntry.setStatus("current")
_CfprSmHeartbeatConfigInstanceId_Type = CfprManagedObjectId
_CfprSmHeartbeatConfigInstanceId_Object = MibTableColumn
cfprSmHeartbeatConfigInstanceId = _CfprSmHeartbeatConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 13, 1, 1),
    _CfprSmHeartbeatConfigInstanceId_Type()
)
cfprSmHeartbeatConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmHeartbeatConfigInstanceId.setStatus("current")
_CfprSmIPTable_Object = MibTable
cfprSmIPTable = _CfprSmIPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 14)
)
if mibBuilder.loadTexts:
    cfprSmIPTable.setStatus("current")
_CfprSmIPEntry_Object = MibTableRow
cfprSmIPEntry = _CfprSmIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 14, 1)
)
cfprSmIPEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmIPInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmIPEntry.setStatus("current")
_CfprSmIPInstanceId_Type = CfprManagedObjectId
_CfprSmIPInstanceId_Object = MibTableColumn
cfprSmIPInstanceId = _CfprSmIPInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 14, 1, 1),
    _CfprSmIPInstanceId_Type()
)
cfprSmIPInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmIPInstanceId.setStatus("current")
_CfprSmIPV6Table_Object = MibTable
cfprSmIPV6Table = _CfprSmIPV6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 15)
)
if mibBuilder.loadTexts:
    cfprSmIPV6Table.setStatus("current")
_CfprSmIPV6Entry_Object = MibTableRow
cfprSmIPV6Entry = _CfprSmIPV6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 15, 1)
)
cfprSmIPV6Entry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmIPV6InstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmIPV6Entry.setStatus("current")
_CfprSmIPV6InstanceId_Type = CfprManagedObjectId
_CfprSmIPV6InstanceId_Object = MibTableColumn
cfprSmIPV6InstanceId = _CfprSmIPV6InstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 15, 1, 1),
    _CfprSmIPV6InstanceId_Type()
)
cfprSmIPV6InstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmIPV6InstanceId.setStatus("current")
_CfprSmKeyTable_Object = MibTable
cfprSmKeyTable = _CfprSmKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 16)
)
if mibBuilder.loadTexts:
    cfprSmKeyTable.setStatus("current")
_CfprSmKeyEntry_Object = MibTableRow
cfprSmKeyEntry = _CfprSmKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 16, 1)
)
cfprSmKeyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmKeyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmKeyEntry.setStatus("current")
_CfprSmKeyInstanceId_Type = CfprManagedObjectId
_CfprSmKeyInstanceId_Object = MibTableColumn
cfprSmKeyInstanceId = _CfprSmKeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 16, 1, 1),
    _CfprSmKeyInstanceId_Type()
)
cfprSmKeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmKeyInstanceId.setStatus("current")
_CfprSmLDTemplateTable_Object = MibTable
cfprSmLDTemplateTable = _CfprSmLDTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 17)
)
if mibBuilder.loadTexts:
    cfprSmLDTemplateTable.setStatus("current")
_CfprSmLDTemplateEntry_Object = MibTableRow
cfprSmLDTemplateEntry = _CfprSmLDTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 17, 1)
)
cfprSmLDTemplateEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmLDTemplateInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmLDTemplateEntry.setStatus("current")
_CfprSmLDTemplateInstanceId_Type = CfprManagedObjectId
_CfprSmLDTemplateInstanceId_Object = MibTableColumn
cfprSmLDTemplateInstanceId = _CfprSmLDTemplateInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 17, 1, 1),
    _CfprSmLDTemplateInstanceId_Type()
)
cfprSmLDTemplateInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmLDTemplateInstanceId.setStatus("current")
_CfprSmLogicalDeviceTable_Object = MibTable
cfprSmLogicalDeviceTable = _CfprSmLogicalDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 18)
)
if mibBuilder.loadTexts:
    cfprSmLogicalDeviceTable.setStatus("current")
_CfprSmLogicalDeviceEntry_Object = MibTableRow
cfprSmLogicalDeviceEntry = _CfprSmLogicalDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 18, 1)
)
cfprSmLogicalDeviceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmLogicalDeviceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmLogicalDeviceEntry.setStatus("current")
_CfprSmLogicalDeviceInstanceId_Type = CfprManagedObjectId
_CfprSmLogicalDeviceInstanceId_Object = MibTableColumn
cfprSmLogicalDeviceInstanceId = _CfprSmLogicalDeviceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 18, 1, 1),
    _CfprSmLogicalDeviceInstanceId_Type()
)
cfprSmLogicalDeviceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmLogicalDeviceInstanceId.setStatus("current")
_CfprSmMgmtBootstrapTable_Object = MibTable
cfprSmMgmtBootstrapTable = _CfprSmMgmtBootstrapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 19)
)
if mibBuilder.loadTexts:
    cfprSmMgmtBootstrapTable.setStatus("current")
_CfprSmMgmtBootstrapEntry_Object = MibTableRow
cfprSmMgmtBootstrapEntry = _CfprSmMgmtBootstrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 19, 1)
)
cfprSmMgmtBootstrapEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmMgmtBootstrapInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmMgmtBootstrapEntry.setStatus("current")
_CfprSmMgmtBootstrapInstanceId_Type = CfprManagedObjectId
_CfprSmMgmtBootstrapInstanceId_Object = MibTableColumn
cfprSmMgmtBootstrapInstanceId = _CfprSmMgmtBootstrapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 19, 1, 1),
    _CfprSmMgmtBootstrapInstanceId_Type()
)
cfprSmMgmtBootstrapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmMgmtBootstrapInstanceId.setStatus("current")
_CfprSmMonitorTable_Object = MibTable
cfprSmMonitorTable = _CfprSmMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20)
)
if mibBuilder.loadTexts:
    cfprSmMonitorTable.setStatus("current")
_CfprSmMonitorEntry_Object = MibTableRow
cfprSmMonitorEntry = _CfprSmMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1)
)
cfprSmMonitorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmMonitorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmMonitorEntry.setStatus("current")
_CfprSmMonitorInstanceId_Type = CfprManagedObjectId
_CfprSmMonitorInstanceId_Object = MibTableColumn
cfprSmMonitorInstanceId = _CfprSmMonitorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 1),
    _CfprSmMonitorInstanceId_Type()
)
cfprSmMonitorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmMonitorInstanceId.setStatus("current")
_CfprSmMonitorDn_Type = CfprManagedObjectDn
_CfprSmMonitorDn_Object = MibTableColumn
cfprSmMonitorDn = _CfprSmMonitorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 2),
    _CfprSmMonitorDn_Type()
)
cfprSmMonitorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorDn.setStatus("current")
_CfprSmMonitorRn_Type = SnmpAdminString
_CfprSmMonitorRn_Object = MibTableColumn
cfprSmMonitorRn = _CfprSmMonitorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 3),
    _CfprSmMonitorRn_Type()
)
cfprSmMonitorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorRn.setStatus("current")
_CfprSmMonitorBladeUptime_Type = SnmpAdminString
_CfprSmMonitorBladeUptime_Object = MibTableColumn
cfprSmMonitorBladeUptime = _CfprSmMonitorBladeUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 4),
    _CfprSmMonitorBladeUptime_Type()
)
cfprSmMonitorBladeUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorBladeUptime.setStatus("current")
_CfprSmMonitorCpuTotalLoadAvg15min_Type = Integer32
_CfprSmMonitorCpuTotalLoadAvg15min_Object = MibTableColumn
cfprSmMonitorCpuTotalLoadAvg15min = _CfprSmMonitorCpuTotalLoadAvg15min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 5),
    _CfprSmMonitorCpuTotalLoadAvg15min_Type()
)
cfprSmMonitorCpuTotalLoadAvg15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorCpuTotalLoadAvg15min.setStatus("current")
_CfprSmMonitorCpuTotalLoadAvg1min_Type = Integer32
_CfprSmMonitorCpuTotalLoadAvg1min_Object = MibTableColumn
cfprSmMonitorCpuTotalLoadAvg1min = _CfprSmMonitorCpuTotalLoadAvg1min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 6),
    _CfprSmMonitorCpuTotalLoadAvg1min_Type()
)
cfprSmMonitorCpuTotalLoadAvg1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorCpuTotalLoadAvg1min.setStatus("current")
_CfprSmMonitorCpuTotalLoadAvg5min_Type = Integer32
_CfprSmMonitorCpuTotalLoadAvg5min_Object = MibTableColumn
cfprSmMonitorCpuTotalLoadAvg5min = _CfprSmMonitorCpuTotalLoadAvg5min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 7),
    _CfprSmMonitorCpuTotalLoadAvg5min_Type()
)
cfprSmMonitorCpuTotalLoadAvg5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorCpuTotalLoadAvg5min.setStatus("current")
_CfprSmMonitorDiskFileSystemCount_Type = Gauge32
_CfprSmMonitorDiskFileSystemCount_Object = MibTableColumn
cfprSmMonitorDiskFileSystemCount = _CfprSmMonitorDiskFileSystemCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 8),
    _CfprSmMonitorDiskFileSystemCount_Type()
)
cfprSmMonitorDiskFileSystemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorDiskFileSystemCount.setStatus("current")
_CfprSmMonitorMemFreeKb_Type = Gauge32
_CfprSmMonitorMemFreeKb_Object = MibTableColumn
cfprSmMonitorMemFreeKb = _CfprSmMonitorMemFreeKb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 9),
    _CfprSmMonitorMemFreeKb_Type()
)
cfprSmMonitorMemFreeKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorMemFreeKb.setStatus("current")
_CfprSmMonitorMemTotalKb_Type = Gauge32
_CfprSmMonitorMemTotalKb_Object = MibTableColumn
cfprSmMonitorMemTotalKb = _CfprSmMonitorMemTotalKb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 10),
    _CfprSmMonitorMemTotalKb_Type()
)
cfprSmMonitorMemTotalKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorMemTotalKb.setStatus("current")
_CfprSmMonitorMemUsedKb_Type = Gauge32
_CfprSmMonitorMemUsedKb_Object = MibTableColumn
cfprSmMonitorMemUsedKb = _CfprSmMonitorMemUsedKb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 11),
    _CfprSmMonitorMemUsedKb_Type()
)
cfprSmMonitorMemUsedKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorMemUsedKb.setStatus("current")
_CfprSmMonitorOsVersion_Type = SnmpAdminString
_CfprSmMonitorOsVersion_Object = MibTableColumn
cfprSmMonitorOsVersion = _CfprSmMonitorOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 12),
    _CfprSmMonitorOsVersion_Type()
)
cfprSmMonitorOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorOsVersion.setStatus("current")
_CfprSmMonitorUpdateTimestamp_Type = DateAndTime
_CfprSmMonitorUpdateTimestamp_Object = MibTableColumn
cfprSmMonitorUpdateTimestamp = _CfprSmMonitorUpdateTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 13),
    _CfprSmMonitorUpdateTimestamp_Type()
)
cfprSmMonitorUpdateTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorUpdateTimestamp.setStatus("current")
_CfprSmMonitorMemAppTotalKb_Type = Gauge32
_CfprSmMonitorMemAppTotalKb_Object = MibTableColumn
cfprSmMonitorMemAppTotalKb = _CfprSmMonitorMemAppTotalKb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 14),
    _CfprSmMonitorMemAppTotalKb_Type()
)
cfprSmMonitorMemAppTotalKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorMemAppTotalKb.setStatus("current")
_CfprSmMonitorCpuAvailable_Type = Gauge32
_CfprSmMonitorCpuAvailable_Object = MibTableColumn
cfprSmMonitorCpuAvailable = _CfprSmMonitorCpuAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 15),
    _CfprSmMonitorCpuAvailable_Type()
)
cfprSmMonitorCpuAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorCpuAvailable.setStatus("current")
_CfprSmMonitorCpuTotal_Type = Gauge32
_CfprSmMonitorCpuTotal_Object = MibTableColumn
cfprSmMonitorCpuTotal = _CfprSmMonitorCpuTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 16),
    _CfprSmMonitorCpuTotal_Type()
)
cfprSmMonitorCpuTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorCpuTotal.setStatus("current")
_CfprSmMonitorDataDiskAvailable_Type = Gauge32
_CfprSmMonitorDataDiskAvailable_Object = MibTableColumn
cfprSmMonitorDataDiskAvailable = _CfprSmMonitorDataDiskAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 17),
    _CfprSmMonitorDataDiskAvailable_Type()
)
cfprSmMonitorDataDiskAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorDataDiskAvailable.setStatus("current")
_CfprSmMonitorDataDiskTotal_Type = Gauge32
_CfprSmMonitorDataDiskTotal_Object = MibTableColumn
cfprSmMonitorDataDiskTotal = _CfprSmMonitorDataDiskTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 18),
    _CfprSmMonitorDataDiskTotal_Type()
)
cfprSmMonitorDataDiskTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorDataDiskTotal.setStatus("current")
_CfprSmMonitorMemAppAvailable_Type = Gauge32
_CfprSmMonitorMemAppAvailable_Object = MibTableColumn
cfprSmMonitorMemAppAvailable = _CfprSmMonitorMemAppAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 19),
    _CfprSmMonitorMemAppAvailable_Type()
)
cfprSmMonitorMemAppAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorMemAppAvailable.setStatus("current")
_CfprSmMonitorMemAppTotal_Type = Gauge32
_CfprSmMonitorMemAppTotal_Object = MibTableColumn
cfprSmMonitorMemAppTotal = _CfprSmMonitorMemAppTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 20),
    _CfprSmMonitorMemAppTotal_Type()
)
cfprSmMonitorMemAppTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorMemAppTotal.setStatus("current")
_CfprSmMonitorMemFree_Type = Gauge32
_CfprSmMonitorMemFree_Object = MibTableColumn
cfprSmMonitorMemFree = _CfprSmMonitorMemFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 21),
    _CfprSmMonitorMemFree_Type()
)
cfprSmMonitorMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorMemFree.setStatus("current")
_CfprSmMonitorMemTotal_Type = Gauge32
_CfprSmMonitorMemTotal_Object = MibTableColumn
cfprSmMonitorMemTotal = _CfprSmMonitorMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 22),
    _CfprSmMonitorMemTotal_Type()
)
cfprSmMonitorMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorMemTotal.setStatus("current")
_CfprSmMonitorMemUsed_Type = Gauge32
_CfprSmMonitorMemUsed_Object = MibTableColumn
cfprSmMonitorMemUsed = _CfprSmMonitorMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 23),
    _CfprSmMonitorMemUsed_Type()
)
cfprSmMonitorMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorMemUsed.setStatus("current")
_CfprSmMonitorSecondaryDiskAvailable_Type = Gauge32
_CfprSmMonitorSecondaryDiskAvailable_Object = MibTableColumn
cfprSmMonitorSecondaryDiskAvailable = _CfprSmMonitorSecondaryDiskAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 24),
    _CfprSmMonitorSecondaryDiskAvailable_Type()
)
cfprSmMonitorSecondaryDiskAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorSecondaryDiskAvailable.setStatus("current")
_CfprSmMonitorSecondaryDiskTotal_Type = Gauge32
_CfprSmMonitorSecondaryDiskTotal_Object = MibTableColumn
cfprSmMonitorSecondaryDiskTotal = _CfprSmMonitorSecondaryDiskTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 25),
    _CfprSmMonitorSecondaryDiskTotal_Type()
)
cfprSmMonitorSecondaryDiskTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorSecondaryDiskTotal.setStatus("current")
_CfprSmMonitorDiskAvailForInstall_Type = Gauge32
_CfprSmMonitorDiskAvailForInstall_Object = MibTableColumn
cfprSmMonitorDiskAvailForInstall = _CfprSmMonitorDiskAvailForInstall_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 26),
    _CfprSmMonitorDiskAvailForInstall_Type()
)
cfprSmMonitorDiskAvailForInstall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorDiskAvailForInstall.setStatus("current")
_CfprSmMonitorLastUpdateMonoTime_Type = DateAndTime
_CfprSmMonitorLastUpdateMonoTime_Object = MibTableColumn
cfprSmMonitorLastUpdateMonoTime = _CfprSmMonitorLastUpdateMonoTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 20, 1, 27),
    _CfprSmMonitorLastUpdateMonoTime_Type()
)
cfprSmMonitorLastUpdateMonoTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSmMonitorLastUpdateMonoTime.setStatus("current")
_CfprSmNetMgmtBootstrapKeyEnumValueTable_Object = MibTable
cfprSmNetMgmtBootstrapKeyEnumValueTable = _CfprSmNetMgmtBootstrapKeyEnumValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 24)
)
if mibBuilder.loadTexts:
    cfprSmNetMgmtBootstrapKeyEnumValueTable.setStatus("current")
_CfprSmNetMgmtBootstrapKeyEnumValueEntry_Object = MibTableRow
cfprSmNetMgmtBootstrapKeyEnumValueEntry = _CfprSmNetMgmtBootstrapKeyEnumValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 24, 1)
)
cfprSmNetMgmtBootstrapKeyEnumValueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmNetMgmtBootstrapKeyEnumValueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmNetMgmtBootstrapKeyEnumValueEntry.setStatus("current")
_CfprSmNetMgmtBootstrapKeyEnumValueInstanceId_Type = CfprManagedObjectId
_CfprSmNetMgmtBootstrapKeyEnumValueInstanceId_Object = MibTableColumn
cfprSmNetMgmtBootstrapKeyEnumValueInstanceId = _CfprSmNetMgmtBootstrapKeyEnumValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 24, 1, 1),
    _CfprSmNetMgmtBootstrapKeyEnumValueInstanceId_Type()
)
cfprSmNetMgmtBootstrapKeyEnumValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmNetMgmtBootstrapKeyEnumValueInstanceId.setStatus("current")
_CfprSmNetMgmtBootstrapValueTable_Object = MibTable
cfprSmNetMgmtBootstrapValueTable = _CfprSmNetMgmtBootstrapValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 25)
)
if mibBuilder.loadTexts:
    cfprSmNetMgmtBootstrapValueTable.setStatus("current")
_CfprSmNetMgmtBootstrapValueEntry_Object = MibTableRow
cfprSmNetMgmtBootstrapValueEntry = _CfprSmNetMgmtBootstrapValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 25, 1)
)
cfprSmNetMgmtBootstrapValueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmNetMgmtBootstrapValueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmNetMgmtBootstrapValueEntry.setStatus("current")
_CfprSmNetMgmtBootstrapValueInstanceId_Type = CfprManagedObjectId
_CfprSmNetMgmtBootstrapValueInstanceId_Object = MibTableColumn
cfprSmNetMgmtBootstrapValueInstanceId = _CfprSmNetMgmtBootstrapValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 25, 1, 1),
    _CfprSmNetMgmtBootstrapValueInstanceId_Type()
)
cfprSmNetMgmtBootstrapValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmNetMgmtBootstrapValueInstanceId.setStatus("current")
_CfprSmPortRequirementTable_Object = MibTable
cfprSmPortRequirementTable = _CfprSmPortRequirementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 26)
)
if mibBuilder.loadTexts:
    cfprSmPortRequirementTable.setStatus("current")
_CfprSmPortRequirementEntry_Object = MibTableRow
cfprSmPortRequirementEntry = _CfprSmPortRequirementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 26, 1)
)
cfprSmPortRequirementEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmPortRequirementInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmPortRequirementEntry.setStatus("current")
_CfprSmPortRequirementInstanceId_Type = CfprManagedObjectId
_CfprSmPortRequirementInstanceId_Object = MibTableColumn
cfprSmPortRequirementInstanceId = _CfprSmPortRequirementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 26, 1, 1),
    _CfprSmPortRequirementInstanceId_Type()
)
cfprSmPortRequirementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmPortRequirementInstanceId.setStatus("current")
_CfprSmPortSubTypeTable_Object = MibTable
cfprSmPortSubTypeTable = _CfprSmPortSubTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 27)
)
if mibBuilder.loadTexts:
    cfprSmPortSubTypeTable.setStatus("current")
_CfprSmPortSubTypeEntry_Object = MibTableRow
cfprSmPortSubTypeEntry = _CfprSmPortSubTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 27, 1)
)
cfprSmPortSubTypeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmPortSubTypeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmPortSubTypeEntry.setStatus("current")
_CfprSmPortSubTypeInstanceId_Type = CfprManagedObjectId
_CfprSmPortSubTypeInstanceId_Object = MibTableColumn
cfprSmPortSubTypeInstanceId = _CfprSmPortSubTypeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 27, 1, 1),
    _CfprSmPortSubTypeInstanceId_Type()
)
cfprSmPortSubTypeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmPortSubTypeInstanceId.setStatus("current")
_CfprSmResourceTable_Object = MibTable
cfprSmResourceTable = _CfprSmResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 28)
)
if mibBuilder.loadTexts:
    cfprSmResourceTable.setStatus("current")
_CfprSmResourceEntry_Object = MibTableRow
cfprSmResourceEntry = _CfprSmResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 28, 1)
)
cfprSmResourceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmResourceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmResourceEntry.setStatus("current")
_CfprSmResourceInstanceId_Type = CfprManagedObjectId
_CfprSmResourceInstanceId_Object = MibTableColumn
cfprSmResourceInstanceId = _CfprSmResourceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 28, 1, 1),
    _CfprSmResourceInstanceId_Type()
)
cfprSmResourceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmResourceInstanceId.setStatus("current")
_CfprSmSecSvcTable_Object = MibTable
cfprSmSecSvcTable = _CfprSmSecSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 29)
)
if mibBuilder.loadTexts:
    cfprSmSecSvcTable.setStatus("current")
_CfprSmSecSvcEntry_Object = MibTableRow
cfprSmSecSvcEntry = _CfprSmSecSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 29, 1)
)
cfprSmSecSvcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmSecSvcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmSecSvcEntry.setStatus("current")
_CfprSmSecSvcInstanceId_Type = CfprManagedObjectId
_CfprSmSecSvcInstanceId_Object = MibTableColumn
cfprSmSecSvcInstanceId = _CfprSmSecSvcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 29, 1, 1),
    _CfprSmSecSvcInstanceId_Type()
)
cfprSmSecSvcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmSecSvcInstanceId.setStatus("current")
_CfprSmSlotTable_Object = MibTable
cfprSmSlotTable = _CfprSmSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 33)
)
if mibBuilder.loadTexts:
    cfprSmSlotTable.setStatus("current")
_CfprSmSlotEntry_Object = MibTableRow
cfprSmSlotEntry = _CfprSmSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 33, 1)
)
cfprSmSlotEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmSlotInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmSlotEntry.setStatus("current")
_CfprSmSlotInstanceId_Type = CfprManagedObjectId
_CfprSmSlotInstanceId_Object = MibTableColumn
cfprSmSlotInstanceId = _CfprSmSlotInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 33, 1, 1),
    _CfprSmSlotInstanceId_Type()
)
cfprSmSlotInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmSlotInstanceId.setStatus("current")
_CfprSmSystemMacTable_Object = MibTable
cfprSmSystemMacTable = _CfprSmSystemMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 34)
)
if mibBuilder.loadTexts:
    cfprSmSystemMacTable.setStatus("current")
_CfprSmSystemMacEntry_Object = MibTableRow
cfprSmSystemMacEntry = _CfprSmSystemMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 34, 1)
)
cfprSmSystemMacEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmSystemMacInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmSystemMacEntry.setStatus("current")
_CfprSmSystemMacInstanceId_Type = CfprManagedObjectId
_CfprSmSystemMacInstanceId_Object = MibTableColumn
cfprSmSystemMacInstanceId = _CfprSmSystemMacInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 34, 1, 1),
    _CfprSmSystemMacInstanceId_Type()
)
cfprSmSystemMacInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmSystemMacInstanceId.setStatus("current")
_CfprSmTemplateAppTable_Object = MibTable
cfprSmTemplateAppTable = _CfprSmTemplateAppTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 35)
)
if mibBuilder.loadTexts:
    cfprSmTemplateAppTable.setStatus("current")
_CfprSmTemplateAppEntry_Object = MibTableRow
cfprSmTemplateAppEntry = _CfprSmTemplateAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 35, 1)
)
cfprSmTemplateAppEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmTemplateAppInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmTemplateAppEntry.setStatus("current")
_CfprSmTemplateAppInstanceId_Type = CfprManagedObjectId
_CfprSmTemplateAppInstanceId_Object = MibTableColumn
cfprSmTemplateAppInstanceId = _CfprSmTemplateAppInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 35, 1, 1),
    _CfprSmTemplateAppInstanceId_Type()
)
cfprSmTemplateAppInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmTemplateAppInstanceId.setStatus("current")
_CfprSmUserMacTable_Object = MibTable
cfprSmUserMacTable = _CfprSmUserMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 36)
)
if mibBuilder.loadTexts:
    cfprSmUserMacTable.setStatus("current")
_CfprSmUserMacEntry_Object = MibTableRow
cfprSmUserMacEntry = _CfprSmUserMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 36, 1)
)
cfprSmUserMacEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmUserMacInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmUserMacEntry.setStatus("current")
_CfprSmUserMacInstanceId_Type = CfprManagedObjectId
_CfprSmUserMacInstanceId_Object = MibTableColumn
cfprSmUserMacInstanceId = _CfprSmUserMacInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 36, 1, 1),
    _CfprSmUserMacInstanceId_Type()
)
cfprSmUserMacInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmUserMacInstanceId.setStatus("current")
_CfprSmAppInfoTable_Object = MibTable
cfprSmAppInfoTable = _CfprSmAppInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 37)
)
if mibBuilder.loadTexts:
    cfprSmAppInfoTable.setStatus("current")
_CfprSmAppInfoEntry_Object = MibTableRow
cfprSmAppInfoEntry = _CfprSmAppInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 37, 1)
)
cfprSmAppInfoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppInfoEntry.setStatus("current")
_CfprSmAppInfoInstanceId_Type = CfprManagedObjectId
_CfprSmAppInfoInstanceId_Object = MibTableColumn
cfprSmAppInfoInstanceId = _CfprSmAppInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 37, 1, 1),
    _CfprSmAppInfoInstanceId_Type()
)
cfprSmAppInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppInfoInstanceId.setStatus("current")
_CfprSmAppInstance2Table_Object = MibTable
cfprSmAppInstance2Table = _CfprSmAppInstance2Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 38)
)
if mibBuilder.loadTexts:
    cfprSmAppInstance2Table.setStatus("current")
_CfprSmAppInstance2Entry_Object = MibTableRow
cfprSmAppInstance2Entry = _CfprSmAppInstance2Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 38, 1)
)
cfprSmAppInstance2Entry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppInstance2InstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppInstance2Entry.setStatus("current")
_CfprSmAppInstance2InstanceId_Type = CfprManagedObjectId
_CfprSmAppInstance2InstanceId_Object = MibTableColumn
cfprSmAppInstance2InstanceId = _CfprSmAppInstance2InstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 38, 1, 1),
    _CfprSmAppInstance2InstanceId_Type()
)
cfprSmAppInstance2InstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppInstance2InstanceId.setStatus("current")
_CfprSmAppInstance2FsmTable_Object = MibTable
cfprSmAppInstance2FsmTable = _CfprSmAppInstance2FsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 39)
)
if mibBuilder.loadTexts:
    cfprSmAppInstance2FsmTable.setStatus("current")
_CfprSmAppInstance2FsmEntry_Object = MibTableRow
cfprSmAppInstance2FsmEntry = _CfprSmAppInstance2FsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 39, 1)
)
cfprSmAppInstance2FsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppInstance2FsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppInstance2FsmEntry.setStatus("current")
_CfprSmAppInstance2FsmInstanceId_Type = CfprManagedObjectId
_CfprSmAppInstance2FsmInstanceId_Object = MibTableColumn
cfprSmAppInstance2FsmInstanceId = _CfprSmAppInstance2FsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 39, 1, 1),
    _CfprSmAppInstance2FsmInstanceId_Type()
)
cfprSmAppInstance2FsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppInstance2FsmInstanceId.setStatus("current")
_CfprSmAppInstance2FsmStageTable_Object = MibTable
cfprSmAppInstance2FsmStageTable = _CfprSmAppInstance2FsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 40)
)
if mibBuilder.loadTexts:
    cfprSmAppInstance2FsmStageTable.setStatus("current")
_CfprSmAppInstance2FsmStageEntry_Object = MibTableRow
cfprSmAppInstance2FsmStageEntry = _CfprSmAppInstance2FsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 40, 1)
)
cfprSmAppInstance2FsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppInstance2FsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppInstance2FsmStageEntry.setStatus("current")
_CfprSmAppInstance2FsmStageInstanceId_Type = CfprManagedObjectId
_CfprSmAppInstance2FsmStageInstanceId_Object = MibTableColumn
cfprSmAppInstance2FsmStageInstanceId = _CfprSmAppInstance2FsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 40, 1, 1),
    _CfprSmAppInstance2FsmStageInstanceId_Type()
)
cfprSmAppInstance2FsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppInstance2FsmStageInstanceId.setStatus("current")
_CfprSmAppInstance2FsmTaskTable_Object = MibTable
cfprSmAppInstance2FsmTaskTable = _CfprSmAppInstance2FsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 41)
)
if mibBuilder.loadTexts:
    cfprSmAppInstance2FsmTaskTable.setStatus("current")
_CfprSmAppInstance2FsmTaskEntry_Object = MibTableRow
cfprSmAppInstance2FsmTaskEntry = _CfprSmAppInstance2FsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 41, 1)
)
cfprSmAppInstance2FsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppInstance2FsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppInstance2FsmTaskEntry.setStatus("current")
_CfprSmAppInstance2FsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSmAppInstance2FsmTaskInstanceId_Object = MibTableColumn
cfprSmAppInstance2FsmTaskInstanceId = _CfprSmAppInstance2FsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 41, 1, 1),
    _CfprSmAppInstance2FsmTaskInstanceId_Type()
)
cfprSmAppInstance2FsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppInstance2FsmTaskInstanceId.setStatus("current")
_CfprSmAppRscProfListTable_Object = MibTable
cfprSmAppRscProfListTable = _CfprSmAppRscProfListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 42)
)
if mibBuilder.loadTexts:
    cfprSmAppRscProfListTable.setStatus("current")
_CfprSmAppRscProfListEntry_Object = MibTableRow
cfprSmAppRscProfListEntry = _CfprSmAppRscProfListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 42, 1)
)
cfprSmAppRscProfListEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppRscProfListInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppRscProfListEntry.setStatus("current")
_CfprSmAppRscProfListInstanceId_Type = CfprManagedObjectId
_CfprSmAppRscProfListInstanceId_Object = MibTableColumn
cfprSmAppRscProfListInstanceId = _CfprSmAppRscProfListInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 42, 1, 1),
    _CfprSmAppRscProfListInstanceId_Type()
)
cfprSmAppRscProfListInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppRscProfListInstanceId.setStatus("current")
_CfprSmAppRscProfileTable_Object = MibTable
cfprSmAppRscProfileTable = _CfprSmAppRscProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 43)
)
if mibBuilder.loadTexts:
    cfprSmAppRscProfileTable.setStatus("current")
_CfprSmAppRscProfileEntry_Object = MibTableRow
cfprSmAppRscProfileEntry = _CfprSmAppRscProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 43, 1)
)
cfprSmAppRscProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAppRscProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAppRscProfileEntry.setStatus("current")
_CfprSmAppRscProfileInstanceId_Type = CfprManagedObjectId
_CfprSmAppRscProfileInstanceId_Object = MibTableColumn
cfprSmAppRscProfileInstanceId = _CfprSmAppRscProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 43, 1, 1),
    _CfprSmAppRscProfileInstanceId_Type()
)
cfprSmAppRscProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAppRscProfileInstanceId.setStatus("current")
_CfprSmAutoMacPoolTable_Object = MibTable
cfprSmAutoMacPoolTable = _CfprSmAutoMacPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 44)
)
if mibBuilder.loadTexts:
    cfprSmAutoMacPoolTable.setStatus("current")
_CfprSmAutoMacPoolEntry_Object = MibTableRow
cfprSmAutoMacPoolEntry = _CfprSmAutoMacPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 44, 1)
)
cfprSmAutoMacPoolEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmAutoMacPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmAutoMacPoolEntry.setStatus("current")
_CfprSmAutoMacPoolInstanceId_Type = CfprManagedObjectId
_CfprSmAutoMacPoolInstanceId_Object = MibTableColumn
cfprSmAutoMacPoolInstanceId = _CfprSmAutoMacPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 44, 1, 1),
    _CfprSmAutoMacPoolInstanceId_Type()
)
cfprSmAutoMacPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmAutoMacPoolInstanceId.setStatus("current")
_CfprSmBatchHeartbeatTable_Object = MibTable
cfprSmBatchHeartbeatTable = _CfprSmBatchHeartbeatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 45)
)
if mibBuilder.loadTexts:
    cfprSmBatchHeartbeatTable.setStatus("current")
_CfprSmBatchHeartbeatEntry_Object = MibTableRow
cfprSmBatchHeartbeatEntry = _CfprSmBatchHeartbeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 45, 1)
)
cfprSmBatchHeartbeatEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmBatchHeartbeatInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmBatchHeartbeatEntry.setStatus("current")
_CfprSmBatchHeartbeatInstanceId_Type = CfprManagedObjectId
_CfprSmBatchHeartbeatInstanceId_Object = MibTableColumn
cfprSmBatchHeartbeatInstanceId = _CfprSmBatchHeartbeatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 45, 1, 1),
    _CfprSmBatchHeartbeatInstanceId_Type()
)
cfprSmBatchHeartbeatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmBatchHeartbeatInstanceId.setStatus("current")
_CfprSmCloudConnectorTable_Object = MibTable
cfprSmCloudConnectorTable = _CfprSmCloudConnectorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 46)
)
if mibBuilder.loadTexts:
    cfprSmCloudConnectorTable.setStatus("current")
_CfprSmCloudConnectorEntry_Object = MibTableRow
cfprSmCloudConnectorEntry = _CfprSmCloudConnectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 46, 1)
)
cfprSmCloudConnectorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmCloudConnectorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmCloudConnectorEntry.setStatus("current")
_CfprSmCloudConnectorInstanceId_Type = CfprManagedObjectId
_CfprSmCloudConnectorInstanceId_Object = MibTableColumn
cfprSmCloudConnectorInstanceId = _CfprSmCloudConnectorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 46, 1, 1),
    _CfprSmCloudConnectorInstanceId_Type()
)
cfprSmCloudConnectorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmCloudConnectorInstanceId.setStatus("current")
_CfprSmCloudConnectorFsmTable_Object = MibTable
cfprSmCloudConnectorFsmTable = _CfprSmCloudConnectorFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 47)
)
if mibBuilder.loadTexts:
    cfprSmCloudConnectorFsmTable.setStatus("current")
_CfprSmCloudConnectorFsmEntry_Object = MibTableRow
cfprSmCloudConnectorFsmEntry = _CfprSmCloudConnectorFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 47, 1)
)
cfprSmCloudConnectorFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmCloudConnectorFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmCloudConnectorFsmEntry.setStatus("current")
_CfprSmCloudConnectorFsmInstanceId_Type = CfprManagedObjectId
_CfprSmCloudConnectorFsmInstanceId_Object = MibTableColumn
cfprSmCloudConnectorFsmInstanceId = _CfprSmCloudConnectorFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 47, 1, 1),
    _CfprSmCloudConnectorFsmInstanceId_Type()
)
cfprSmCloudConnectorFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmCloudConnectorFsmInstanceId.setStatus("current")
_CfprSmCloudConnectorFsmStageTable_Object = MibTable
cfprSmCloudConnectorFsmStageTable = _CfprSmCloudConnectorFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 48)
)
if mibBuilder.loadTexts:
    cfprSmCloudConnectorFsmStageTable.setStatus("current")
_CfprSmCloudConnectorFsmStageEntry_Object = MibTableRow
cfprSmCloudConnectorFsmStageEntry = _CfprSmCloudConnectorFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 48, 1)
)
cfprSmCloudConnectorFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmCloudConnectorFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmCloudConnectorFsmStageEntry.setStatus("current")
_CfprSmCloudConnectorFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSmCloudConnectorFsmStageInstanceId_Object = MibTableColumn
cfprSmCloudConnectorFsmStageInstanceId = _CfprSmCloudConnectorFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 48, 1, 1),
    _CfprSmCloudConnectorFsmStageInstanceId_Type()
)
cfprSmCloudConnectorFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmCloudConnectorFsmStageInstanceId.setStatus("current")
_CfprSmCloudConnectorFsmTaskTable_Object = MibTable
cfprSmCloudConnectorFsmTaskTable = _CfprSmCloudConnectorFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 49)
)
if mibBuilder.loadTexts:
    cfprSmCloudConnectorFsmTaskTable.setStatus("current")
_CfprSmCloudConnectorFsmTaskEntry_Object = MibTableRow
cfprSmCloudConnectorFsmTaskEntry = _CfprSmCloudConnectorFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 49, 1)
)
cfprSmCloudConnectorFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmCloudConnectorFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmCloudConnectorFsmTaskEntry.setStatus("current")
_CfprSmCloudConnectorFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSmCloudConnectorFsmTaskInstanceId_Object = MibTableColumn
cfprSmCloudConnectorFsmTaskInstanceId = _CfprSmCloudConnectorFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 49, 1, 1),
    _CfprSmCloudConnectorFsmTaskInstanceId_Type()
)
cfprSmCloudConnectorFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmCloudConnectorFsmTaskInstanceId.setStatus("current")
_CfprSmCompatibilityMatrixTable_Object = MibTable
cfprSmCompatibilityMatrixTable = _CfprSmCompatibilityMatrixTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 50)
)
if mibBuilder.loadTexts:
    cfprSmCompatibilityMatrixTable.setStatus("current")
_CfprSmCompatibilityMatrixEntry_Object = MibTableRow
cfprSmCompatibilityMatrixEntry = _CfprSmCompatibilityMatrixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 50, 1)
)
cfprSmCompatibilityMatrixEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmCompatibilityMatrixInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmCompatibilityMatrixEntry.setStatus("current")
_CfprSmCompatibilityMatrixInstanceId_Type = CfprManagedObjectId
_CfprSmCompatibilityMatrixInstanceId_Object = MibTableColumn
cfprSmCompatibilityMatrixInstanceId = _CfprSmCompatibilityMatrixInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 50, 1, 1),
    _CfprSmCompatibilityMatrixInstanceId_Type()
)
cfprSmCompatibilityMatrixInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmCompatibilityMatrixInstanceId.setStatus("current")
_CfprSmConfigIssueTable_Object = MibTable
cfprSmConfigIssueTable = _CfprSmConfigIssueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 51)
)
if mibBuilder.loadTexts:
    cfprSmConfigIssueTable.setStatus("current")
_CfprSmConfigIssueEntry_Object = MibTableRow
cfprSmConfigIssueEntry = _CfprSmConfigIssueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 51, 1)
)
cfprSmConfigIssueEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmConfigIssueInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmConfigIssueEntry.setStatus("current")
_CfprSmConfigIssueInstanceId_Type = CfprManagedObjectId
_CfprSmConfigIssueInstanceId_Object = MibTableColumn
cfprSmConfigIssueInstanceId = _CfprSmConfigIssueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 51, 1, 1),
    _CfprSmConfigIssueInstanceId_Type()
)
cfprSmConfigIssueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmConfigIssueInstanceId.setStatus("current")
_CfprSmErrorTable_Object = MibTable
cfprSmErrorTable = _CfprSmErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 52)
)
if mibBuilder.loadTexts:
    cfprSmErrorTable.setStatus("current")
_CfprSmErrorEntry_Object = MibTableRow
cfprSmErrorEntry = _CfprSmErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 52, 1)
)
cfprSmErrorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmErrorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmErrorEntry.setStatus("current")
_CfprSmErrorInstanceId_Type = CfprManagedObjectId
_CfprSmErrorInstanceId_Object = MibTableColumn
cfprSmErrorInstanceId = _CfprSmErrorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 52, 1, 1),
    _CfprSmErrorInstanceId_Type()
)
cfprSmErrorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmErrorInstanceId.setStatus("current")
_CfprSmHotfixTable_Object = MibTable
cfprSmHotfixTable = _CfprSmHotfixTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 53)
)
if mibBuilder.loadTexts:
    cfprSmHotfixTable.setStatus("current")
_CfprSmHotfixEntry_Object = MibTableRow
cfprSmHotfixEntry = _CfprSmHotfixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 53, 1)
)
cfprSmHotfixEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmHotfixInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmHotfixEntry.setStatus("current")
_CfprSmHotfixInstanceId_Type = CfprManagedObjectId
_CfprSmHotfixInstanceId_Object = MibTableColumn
cfprSmHotfixInstanceId = _CfprSmHotfixInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 53, 1, 1),
    _CfprSmHotfixInstanceId_Type()
)
cfprSmHotfixInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmHotfixInstanceId.setStatus("current")
_CfprSmLicenseDeviceTable_Object = MibTable
cfprSmLicenseDeviceTable = _CfprSmLicenseDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 54)
)
if mibBuilder.loadTexts:
    cfprSmLicenseDeviceTable.setStatus("current")
_CfprSmLicenseDeviceEntry_Object = MibTableRow
cfprSmLicenseDeviceEntry = _CfprSmLicenseDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 54, 1)
)
cfprSmLicenseDeviceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmLicenseDeviceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmLicenseDeviceEntry.setStatus("current")
_CfprSmLicenseDeviceInstanceId_Type = CfprManagedObjectId
_CfprSmLicenseDeviceInstanceId_Object = MibTableColumn
cfprSmLicenseDeviceInstanceId = _CfprSmLicenseDeviceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 54, 1, 1),
    _CfprSmLicenseDeviceInstanceId_Type()
)
cfprSmLicenseDeviceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmLicenseDeviceInstanceId.setStatus("current")
_CfprSmLicenseFileTable_Object = MibTable
cfprSmLicenseFileTable = _CfprSmLicenseFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 55)
)
if mibBuilder.loadTexts:
    cfprSmLicenseFileTable.setStatus("current")
_CfprSmLicenseFileEntry_Object = MibTableRow
cfprSmLicenseFileEntry = _CfprSmLicenseFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 55, 1)
)
cfprSmLicenseFileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmLicenseFileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmLicenseFileEntry.setStatus("current")
_CfprSmLicenseFileInstanceId_Type = CfprManagedObjectId
_CfprSmLicenseFileInstanceId_Object = MibTableColumn
cfprSmLicenseFileInstanceId = _CfprSmLicenseFileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 55, 1, 1),
    _CfprSmLicenseFileInstanceId_Type()
)
cfprSmLicenseFileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmLicenseFileInstanceId.setStatus("current")
_CfprSmLicenseFileFsmTable_Object = MibTable
cfprSmLicenseFileFsmTable = _CfprSmLicenseFileFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 56)
)
if mibBuilder.loadTexts:
    cfprSmLicenseFileFsmTable.setStatus("current")
_CfprSmLicenseFileFsmEntry_Object = MibTableRow
cfprSmLicenseFileFsmEntry = _CfprSmLicenseFileFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 56, 1)
)
cfprSmLicenseFileFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmLicenseFileFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmLicenseFileFsmEntry.setStatus("current")
_CfprSmLicenseFileFsmInstanceId_Type = CfprManagedObjectId
_CfprSmLicenseFileFsmInstanceId_Object = MibTableColumn
cfprSmLicenseFileFsmInstanceId = _CfprSmLicenseFileFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 56, 1, 1),
    _CfprSmLicenseFileFsmInstanceId_Type()
)
cfprSmLicenseFileFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmLicenseFileFsmInstanceId.setStatus("current")
_CfprSmLicenseFileFsmStageTable_Object = MibTable
cfprSmLicenseFileFsmStageTable = _CfprSmLicenseFileFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 57)
)
if mibBuilder.loadTexts:
    cfprSmLicenseFileFsmStageTable.setStatus("current")
_CfprSmLicenseFileFsmStageEntry_Object = MibTableRow
cfprSmLicenseFileFsmStageEntry = _CfprSmLicenseFileFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 57, 1)
)
cfprSmLicenseFileFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmLicenseFileFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmLicenseFileFsmStageEntry.setStatus("current")
_CfprSmLicenseFileFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSmLicenseFileFsmStageInstanceId_Object = MibTableColumn
cfprSmLicenseFileFsmStageInstanceId = _CfprSmLicenseFileFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 57, 1, 1),
    _CfprSmLicenseFileFsmStageInstanceId_Type()
)
cfprSmLicenseFileFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmLicenseFileFsmStageInstanceId.setStatus("current")
_CfprSmLicenseFileFsmTaskTable_Object = MibTable
cfprSmLicenseFileFsmTaskTable = _CfprSmLicenseFileFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 58)
)
if mibBuilder.loadTexts:
    cfprSmLicenseFileFsmTaskTable.setStatus("current")
_CfprSmLicenseFileFsmTaskEntry_Object = MibTableRow
cfprSmLicenseFileFsmTaskEntry = _CfprSmLicenseFileFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 58, 1)
)
cfprSmLicenseFileFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmLicenseFileFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmLicenseFileFsmTaskEntry.setStatus("current")
_CfprSmLicenseFileFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSmLicenseFileFsmTaskInstanceId_Object = MibTableColumn
cfprSmLicenseFileFsmTaskInstanceId = _CfprSmLicenseFileFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 58, 1, 1),
    _CfprSmLicenseFileFsmTaskInstanceId_Type()
)
cfprSmLicenseFileFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmLicenseFileFsmTaskInstanceId.setStatus("current")
_CfprSmLogicalDeviceFsmTable_Object = MibTable
cfprSmLogicalDeviceFsmTable = _CfprSmLogicalDeviceFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 59)
)
if mibBuilder.loadTexts:
    cfprSmLogicalDeviceFsmTable.setStatus("current")
_CfprSmLogicalDeviceFsmEntry_Object = MibTableRow
cfprSmLogicalDeviceFsmEntry = _CfprSmLogicalDeviceFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 59, 1)
)
cfprSmLogicalDeviceFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmLogicalDeviceFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmLogicalDeviceFsmEntry.setStatus("current")
_CfprSmLogicalDeviceFsmInstanceId_Type = CfprManagedObjectId
_CfprSmLogicalDeviceFsmInstanceId_Object = MibTableColumn
cfprSmLogicalDeviceFsmInstanceId = _CfprSmLogicalDeviceFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 59, 1, 1),
    _CfprSmLogicalDeviceFsmInstanceId_Type()
)
cfprSmLogicalDeviceFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmLogicalDeviceFsmInstanceId.setStatus("current")
_CfprSmLogicalDeviceFsmStageTable_Object = MibTable
cfprSmLogicalDeviceFsmStageTable = _CfprSmLogicalDeviceFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 60)
)
if mibBuilder.loadTexts:
    cfprSmLogicalDeviceFsmStageTable.setStatus("current")
_CfprSmLogicalDeviceFsmStageEntry_Object = MibTableRow
cfprSmLogicalDeviceFsmStageEntry = _CfprSmLogicalDeviceFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 60, 1)
)
cfprSmLogicalDeviceFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmLogicalDeviceFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmLogicalDeviceFsmStageEntry.setStatus("current")
_CfprSmLogicalDeviceFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSmLogicalDeviceFsmStageInstanceId_Object = MibTableColumn
cfprSmLogicalDeviceFsmStageInstanceId = _CfprSmLogicalDeviceFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 60, 1, 1),
    _CfprSmLogicalDeviceFsmStageInstanceId_Type()
)
cfprSmLogicalDeviceFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmLogicalDeviceFsmStageInstanceId.setStatus("current")
_CfprSmLogicalDeviceFsmTaskTable_Object = MibTable
cfprSmLogicalDeviceFsmTaskTable = _CfprSmLogicalDeviceFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 61)
)
if mibBuilder.loadTexts:
    cfprSmLogicalDeviceFsmTaskTable.setStatus("current")
_CfprSmLogicalDeviceFsmTaskEntry_Object = MibTableRow
cfprSmLogicalDeviceFsmTaskEntry = _CfprSmLogicalDeviceFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 61, 1)
)
cfprSmLogicalDeviceFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmLogicalDeviceFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmLogicalDeviceFsmTaskEntry.setStatus("current")
_CfprSmLogicalDeviceFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSmLogicalDeviceFsmTaskInstanceId_Object = MibTableColumn
cfprSmLogicalDeviceFsmTaskInstanceId = _CfprSmLogicalDeviceFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 61, 1, 1),
    _CfprSmLogicalDeviceFsmTaskInstanceId_Type()
)
cfprSmLogicalDeviceFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmLogicalDeviceFsmTaskInstanceId.setStatus("current")
_CfprSmMacItemTable_Object = MibTable
cfprSmMacItemTable = _CfprSmMacItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 62)
)
if mibBuilder.loadTexts:
    cfprSmMacItemTable.setStatus("current")
_CfprSmMacItemEntry_Object = MibTableRow
cfprSmMacItemEntry = _CfprSmMacItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 62, 1)
)
cfprSmMacItemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmMacItemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmMacItemEntry.setStatus("current")
_CfprSmMacItemInstanceId_Type = CfprManagedObjectId
_CfprSmMacItemInstanceId_Object = MibTableColumn
cfprSmMacItemInstanceId = _CfprSmMacItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 62, 1, 1),
    _CfprSmMacItemInstanceId_Type()
)
cfprSmMacItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmMacItemInstanceId.setStatus("current")
_CfprSmNetMgmtBootstrapKeyLimitsTable_Object = MibTable
cfprSmNetMgmtBootstrapKeyLimitsTable = _CfprSmNetMgmtBootstrapKeyLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 63)
)
if mibBuilder.loadTexts:
    cfprSmNetMgmtBootstrapKeyLimitsTable.setStatus("current")
_CfprSmNetMgmtBootstrapKeyLimitsEntry_Object = MibTableRow
cfprSmNetMgmtBootstrapKeyLimitsEntry = _CfprSmNetMgmtBootstrapKeyLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 63, 1)
)
cfprSmNetMgmtBootstrapKeyLimitsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmNetMgmtBootstrapKeyLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmNetMgmtBootstrapKeyLimitsEntry.setStatus("current")
_CfprSmNetMgmtBootstrapKeyLimitsInstanceId_Type = CfprManagedObjectId
_CfprSmNetMgmtBootstrapKeyLimitsInstanceId_Object = MibTableColumn
cfprSmNetMgmtBootstrapKeyLimitsInstanceId = _CfprSmNetMgmtBootstrapKeyLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 63, 1, 1),
    _CfprSmNetMgmtBootstrapKeyLimitsInstanceId_Type()
)
cfprSmNetMgmtBootstrapKeyLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmNetMgmtBootstrapKeyLimitsInstanceId.setStatus("current")
_CfprSmPreRequisiteTable_Object = MibTable
cfprSmPreRequisiteTable = _CfprSmPreRequisiteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 64)
)
if mibBuilder.loadTexts:
    cfprSmPreRequisiteTable.setStatus("current")
_CfprSmPreRequisiteEntry_Object = MibTableRow
cfprSmPreRequisiteEntry = _CfprSmPreRequisiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 64, 1)
)
cfprSmPreRequisiteEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmPreRequisiteInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmPreRequisiteEntry.setStatus("current")
_CfprSmPreRequisiteInstanceId_Type = CfprManagedObjectId
_CfprSmPreRequisiteInstanceId_Object = MibTableColumn
cfprSmPreRequisiteInstanceId = _CfprSmPreRequisiteInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 64, 1, 1),
    _CfprSmPreRequisiteInstanceId_Type()
)
cfprSmPreRequisiteInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmPreRequisiteInstanceId.setStatus("current")
_CfprSmReplyInterfaceCfgTable_Object = MibTable
cfprSmReplyInterfaceCfgTable = _CfprSmReplyInterfaceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 65)
)
if mibBuilder.loadTexts:
    cfprSmReplyInterfaceCfgTable.setStatus("current")
_CfprSmReplyInterfaceCfgEntry_Object = MibTableRow
cfprSmReplyInterfaceCfgEntry = _CfprSmReplyInterfaceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 65, 1)
)
cfprSmReplyInterfaceCfgEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmReplyInterfaceCfgInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmReplyInterfaceCfgEntry.setStatus("current")
_CfprSmReplyInterfaceCfgInstanceId_Type = CfprManagedObjectId
_CfprSmReplyInterfaceCfgInstanceId_Object = MibTableColumn
cfprSmReplyInterfaceCfgInstanceId = _CfprSmReplyInterfaceCfgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 65, 1, 1),
    _CfprSmReplyInterfaceCfgInstanceId_Type()
)
cfprSmReplyInterfaceCfgInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmReplyInterfaceCfgInstanceId.setStatus("current")
_CfprSmSupportedHardwareTable_Object = MibTable
cfprSmSupportedHardwareTable = _CfprSmSupportedHardwareTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 66)
)
if mibBuilder.loadTexts:
    cfprSmSupportedHardwareTable.setStatus("current")
_CfprSmSupportedHardwareEntry_Object = MibTableRow
cfprSmSupportedHardwareEntry = _CfprSmSupportedHardwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 66, 1)
)
cfprSmSupportedHardwareEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmSupportedHardwareInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmSupportedHardwareEntry.setStatus("current")
_CfprSmSupportedHardwareInstanceId_Type = CfprManagedObjectId
_CfprSmSupportedHardwareInstanceId_Object = MibTableColumn
cfprSmSupportedHardwareInstanceId = _CfprSmSupportedHardwareInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 66, 1, 1),
    _CfprSmSupportedHardwareInstanceId_Type()
)
cfprSmSupportedHardwareInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmSupportedHardwareInstanceId.setStatus("current")
_CfprSmUnsignedCspLicenseTable_Object = MibTable
cfprSmUnsignedCspLicenseTable = _CfprSmUnsignedCspLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 67)
)
if mibBuilder.loadTexts:
    cfprSmUnsignedCspLicenseTable.setStatus("current")
_CfprSmUnsignedCspLicenseEntry_Object = MibTableRow
cfprSmUnsignedCspLicenseEntry = _CfprSmUnsignedCspLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 67, 1)
)
cfprSmUnsignedCspLicenseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmUnsignedCspLicenseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmUnsignedCspLicenseEntry.setStatus("current")
_CfprSmUnsignedCspLicenseInstanceId_Type = CfprManagedObjectId
_CfprSmUnsignedCspLicenseInstanceId_Object = MibTableColumn
cfprSmUnsignedCspLicenseInstanceId = _CfprSmUnsignedCspLicenseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 67, 1, 1),
    _CfprSmUnsignedCspLicenseInstanceId_Type()
)
cfprSmUnsignedCspLicenseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmUnsignedCspLicenseInstanceId.setStatus("current")
_CfprSmUnsignedCspLicenseFsmTable_Object = MibTable
cfprSmUnsignedCspLicenseFsmTable = _CfprSmUnsignedCspLicenseFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 68)
)
if mibBuilder.loadTexts:
    cfprSmUnsignedCspLicenseFsmTable.setStatus("current")
_CfprSmUnsignedCspLicenseFsmEntry_Object = MibTableRow
cfprSmUnsignedCspLicenseFsmEntry = _CfprSmUnsignedCspLicenseFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 68, 1)
)
cfprSmUnsignedCspLicenseFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmUnsignedCspLicenseFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmUnsignedCspLicenseFsmEntry.setStatus("current")
_CfprSmUnsignedCspLicenseFsmInstanceId_Type = CfprManagedObjectId
_CfprSmUnsignedCspLicenseFsmInstanceId_Object = MibTableColumn
cfprSmUnsignedCspLicenseFsmInstanceId = _CfprSmUnsignedCspLicenseFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 68, 1, 1),
    _CfprSmUnsignedCspLicenseFsmInstanceId_Type()
)
cfprSmUnsignedCspLicenseFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmUnsignedCspLicenseFsmInstanceId.setStatus("current")
_CfprSmUnsignedCspLicenseFsmStageTable_Object = MibTable
cfprSmUnsignedCspLicenseFsmStageTable = _CfprSmUnsignedCspLicenseFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 69)
)
if mibBuilder.loadTexts:
    cfprSmUnsignedCspLicenseFsmStageTable.setStatus("current")
_CfprSmUnsignedCspLicenseFsmStageEntry_Object = MibTableRow
cfprSmUnsignedCspLicenseFsmStageEntry = _CfprSmUnsignedCspLicenseFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 69, 1)
)
cfprSmUnsignedCspLicenseFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmUnsignedCspLicenseFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmUnsignedCspLicenseFsmStageEntry.setStatus("current")
_CfprSmUnsignedCspLicenseFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSmUnsignedCspLicenseFsmStageInstanceId_Object = MibTableColumn
cfprSmUnsignedCspLicenseFsmStageInstanceId = _CfprSmUnsignedCspLicenseFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 69, 1, 1),
    _CfprSmUnsignedCspLicenseFsmStageInstanceId_Type()
)
cfprSmUnsignedCspLicenseFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmUnsignedCspLicenseFsmStageInstanceId.setStatus("current")
_CfprSmUnsignedCspLicenseFsmTaskTable_Object = MibTable
cfprSmUnsignedCspLicenseFsmTaskTable = _CfprSmUnsignedCspLicenseFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 70)
)
if mibBuilder.loadTexts:
    cfprSmUnsignedCspLicenseFsmTaskTable.setStatus("current")
_CfprSmUnsignedCspLicenseFsmTaskEntry_Object = MibTableRow
cfprSmUnsignedCspLicenseFsmTaskEntry = _CfprSmUnsignedCspLicenseFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 70, 1)
)
cfprSmUnsignedCspLicenseFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmUnsignedCspLicenseFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmUnsignedCspLicenseFsmTaskEntry.setStatus("current")
_CfprSmUnsignedCspLicenseFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSmUnsignedCspLicenseFsmTaskInstanceId_Object = MibTableColumn
cfprSmUnsignedCspLicenseFsmTaskInstanceId = _CfprSmUnsignedCspLicenseFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 70, 1, 1),
    _CfprSmUnsignedCspLicenseFsmTaskInstanceId_Type()
)
cfprSmUnsignedCspLicenseFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmUnsignedCspLicenseFsmTaskInstanceId.setStatus("current")
_CfprSmHwCryptoTable_Object = MibTable
cfprSmHwCryptoTable = _CfprSmHwCryptoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 71)
)
if mibBuilder.loadTexts:
    cfprSmHwCryptoTable.setStatus("current")
_CfprSmHwCryptoEntry_Object = MibTableRow
cfprSmHwCryptoEntry = _CfprSmHwCryptoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 71, 1)
)
cfprSmHwCryptoEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SM-MIB", "cfprSmHwCryptoInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSmHwCryptoEntry.setStatus("current")
_CfprSmHwCryptoInstanceId_Type = CfprManagedObjectId
_CfprSmHwCryptoInstanceId_Object = MibTableColumn
cfprSmHwCryptoInstanceId = _CfprSmHwCryptoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 71, 71, 1, 1),
    _CfprSmHwCryptoInstanceId_Type()
)
cfprSmHwCryptoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSmHwCryptoInstanceId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-SM-MIB",
    **{"cfprSmObjects": cfprSmObjects,
       "cfprSmAppTable": cfprSmAppTable,
       "cfprSmAppEntry": cfprSmAppEntry,
       "cfprSmAppInstanceId": cfprSmAppInstanceId,
       "cfprSmAppAttributeTable": cfprSmAppAttributeTable,
       "cfprSmAppAttributeEntry": cfprSmAppAttributeEntry,
       "cfprSmAppAttributeInstanceId": cfprSmAppAttributeInstanceId,
       "cfprSmAppAttributeValueTable": cfprSmAppAttributeValueTable,
       "cfprSmAppAttributeValueEntry": cfprSmAppAttributeValueEntry,
       "cfprSmAppAttributeValueInstanceId": cfprSmAppAttributeValueInstanceId,
       "cfprSmAppFsmTable": cfprSmAppFsmTable,
       "cfprSmAppFsmEntry": cfprSmAppFsmEntry,
       "cfprSmAppFsmInstanceId": cfprSmAppFsmInstanceId,
       "cfprSmAppFsmStageTable": cfprSmAppFsmStageTable,
       "cfprSmAppFsmStageEntry": cfprSmAppFsmStageEntry,
       "cfprSmAppFsmStageInstanceId": cfprSmAppFsmStageInstanceId,
       "cfprSmAppFsmTaskTable": cfprSmAppFsmTaskTable,
       "cfprSmAppFsmTaskEntry": cfprSmAppFsmTaskEntry,
       "cfprSmAppFsmTaskInstanceId": cfprSmAppFsmTaskInstanceId,
       "cfprSmAppInstanceTable": cfprSmAppInstanceTable,
       "cfprSmAppInstanceEntry": cfprSmAppInstanceEntry,
       "cfprSmAppInstanceInstanceId": cfprSmAppInstanceInstanceId,
       "cfprSmAppInstanceDn": cfprSmAppInstanceDn,
       "cfprSmAppInstanceRn": cfprSmAppInstanceRn,
       "cfprSmAppInstanceAdminState": cfprSmAppInstanceAdminState,
       "cfprSmAppInstanceAppInstId": cfprSmAppInstanceAppInstId,
       "cfprSmAppInstanceAppName": cfprSmAppInstanceAppName,
       "cfprSmAppInstanceClearLogData": cfprSmAppInstanceClearLogData,
       "cfprSmAppInstanceClusterOperationalState": cfprSmAppInstanceClusterOperationalState,
       "cfprSmAppInstanceCurrentJobProgress": cfprSmAppInstanceCurrentJobProgress,
       "cfprSmAppInstanceCurrentJobState": cfprSmAppInstanceCurrentJobState,
       "cfprSmAppInstanceCurrentJobType": cfprSmAppInstanceCurrentJobType,
       "cfprSmAppInstanceErrorMsg": cfprSmAppInstanceErrorMsg,
       "cfprSmAppInstanceExecuteCmd": cfprSmAppInstanceExecuteCmd,
       "cfprSmAppInstanceOperationalState": cfprSmAppInstanceOperationalState,
       "cfprSmAppInstancePeerDn": cfprSmAppInstancePeerDn,
       "cfprSmAppInstanceRunningVersion": cfprSmAppInstanceRunningVersion,
       "cfprSmAppInstanceStartupVersion": cfprSmAppInstanceStartupVersion,
       "cfprSmAppInstanceExternallyUpgraded": cfprSmAppInstanceExternallyUpgraded,
       "cfprSmAppInstanceHotfix": cfprSmAppInstanceHotfix,
       "cfprSmAppInstanceAppDn": cfprSmAppInstanceAppDn,
       "cfprSmAppInstanceClusterRole": cfprSmAppInstanceClusterRole,
       "cfprSmAppInstanceHasFailedReplication": cfprSmAppInstanceHasFailedReplication,
       "cfprSmAppInstanceReasonForDebundle": cfprSmAppInstanceReasonForDebundle,
       "cfprSmAppInstanceResourceProfileName": cfprSmAppInstanceResourceProfileName,
       "cfprSmAppInstanceVersionIncompatibleErrorMgr": cfprSmAppInstanceVersionIncompatibleErrorMgr,
       "cfprSmAppInstanceTurboMode": cfprSmAppInstanceTurboMode,
       "cfprSmClusterBootstrapTable": cfprSmClusterBootstrapTable,
       "cfprSmClusterBootstrapEntry": cfprSmClusterBootstrapEntry,
       "cfprSmClusterBootstrapInstanceId": cfprSmClusterBootstrapInstanceId,
       "cfprSmDiskFileSystemTable": cfprSmDiskFileSystemTable,
       "cfprSmDiskFileSystemEntry": cfprSmDiskFileSystemEntry,
       "cfprSmDiskFileSystemInstanceId": cfprSmDiskFileSystemInstanceId,
       "cfprSmDiskFileSystemDn": cfprSmDiskFileSystemDn,
       "cfprSmDiskFileSystemRn": cfprSmDiskFileSystemRn,
       "cfprSmDiskFileSystemDiskName": cfprSmDiskFileSystemDiskName,
       "cfprSmDiskFileSystemFileSystem": cfprSmDiskFileSystemFileSystem,
       "cfprSmDiskFileSystemFreeKb": cfprSmDiskFileSystemFreeKb,
       "cfprSmDiskFileSystemMountPoint": cfprSmDiskFileSystemMountPoint,
       "cfprSmDiskFileSystemTotalKb": cfprSmDiskFileSystemTotalKb,
       "cfprSmDiskFileSystemUsedKb": cfprSmDiskFileSystemUsedKb,
       "cfprSmDiskFileSystemFree": cfprSmDiskFileSystemFree,
       "cfprSmDiskFileSystemTotal": cfprSmDiskFileSystemTotal,
       "cfprSmDiskFileSystemUsed": cfprSmDiskFileSystemUsed,
       "cfprSmEncryptedKeyTable": cfprSmEncryptedKeyTable,
       "cfprSmEncryptedKeyEntry": cfprSmEncryptedKeyEntry,
       "cfprSmEncryptedKeyInstanceId": cfprSmEncryptedKeyInstanceId,
       "cfprSmExternalPortLinkTable": cfprSmExternalPortLinkTable,
       "cfprSmExternalPortLinkEntry": cfprSmExternalPortLinkEntry,
       "cfprSmExternalPortLinkInstanceId": cfprSmExternalPortLinkInstanceId,
       "cfprSmHeartbeatTable": cfprSmHeartbeatTable,
       "cfprSmHeartbeatEntry": cfprSmHeartbeatEntry,
       "cfprSmHeartbeatInstanceId": cfprSmHeartbeatInstanceId,
       "cfprSmHeartbeatConfigTable": cfprSmHeartbeatConfigTable,
       "cfprSmHeartbeatConfigEntry": cfprSmHeartbeatConfigEntry,
       "cfprSmHeartbeatConfigInstanceId": cfprSmHeartbeatConfigInstanceId,
       "cfprSmIPTable": cfprSmIPTable,
       "cfprSmIPEntry": cfprSmIPEntry,
       "cfprSmIPInstanceId": cfprSmIPInstanceId,
       "cfprSmIPV6Table": cfprSmIPV6Table,
       "cfprSmIPV6Entry": cfprSmIPV6Entry,
       "cfprSmIPV6InstanceId": cfprSmIPV6InstanceId,
       "cfprSmKeyTable": cfprSmKeyTable,
       "cfprSmKeyEntry": cfprSmKeyEntry,
       "cfprSmKeyInstanceId": cfprSmKeyInstanceId,
       "cfprSmLDTemplateTable": cfprSmLDTemplateTable,
       "cfprSmLDTemplateEntry": cfprSmLDTemplateEntry,
       "cfprSmLDTemplateInstanceId": cfprSmLDTemplateInstanceId,
       "cfprSmLogicalDeviceTable": cfprSmLogicalDeviceTable,
       "cfprSmLogicalDeviceEntry": cfprSmLogicalDeviceEntry,
       "cfprSmLogicalDeviceInstanceId": cfprSmLogicalDeviceInstanceId,
       "cfprSmMgmtBootstrapTable": cfprSmMgmtBootstrapTable,
       "cfprSmMgmtBootstrapEntry": cfprSmMgmtBootstrapEntry,
       "cfprSmMgmtBootstrapInstanceId": cfprSmMgmtBootstrapInstanceId,
       "cfprSmMonitorTable": cfprSmMonitorTable,
       "cfprSmMonitorEntry": cfprSmMonitorEntry,
       "cfprSmMonitorInstanceId": cfprSmMonitorInstanceId,
       "cfprSmMonitorDn": cfprSmMonitorDn,
       "cfprSmMonitorRn": cfprSmMonitorRn,
       "cfprSmMonitorBladeUptime": cfprSmMonitorBladeUptime,
       "cfprSmMonitorCpuTotalLoadAvg15min": cfprSmMonitorCpuTotalLoadAvg15min,
       "cfprSmMonitorCpuTotalLoadAvg1min": cfprSmMonitorCpuTotalLoadAvg1min,
       "cfprSmMonitorCpuTotalLoadAvg5min": cfprSmMonitorCpuTotalLoadAvg5min,
       "cfprSmMonitorDiskFileSystemCount": cfprSmMonitorDiskFileSystemCount,
       "cfprSmMonitorMemFreeKb": cfprSmMonitorMemFreeKb,
       "cfprSmMonitorMemTotalKb": cfprSmMonitorMemTotalKb,
       "cfprSmMonitorMemUsedKb": cfprSmMonitorMemUsedKb,
       "cfprSmMonitorOsVersion": cfprSmMonitorOsVersion,
       "cfprSmMonitorUpdateTimestamp": cfprSmMonitorUpdateTimestamp,
       "cfprSmMonitorMemAppTotalKb": cfprSmMonitorMemAppTotalKb,
       "cfprSmMonitorCpuAvailable": cfprSmMonitorCpuAvailable,
       "cfprSmMonitorCpuTotal": cfprSmMonitorCpuTotal,
       "cfprSmMonitorDataDiskAvailable": cfprSmMonitorDataDiskAvailable,
       "cfprSmMonitorDataDiskTotal": cfprSmMonitorDataDiskTotal,
       "cfprSmMonitorMemAppAvailable": cfprSmMonitorMemAppAvailable,
       "cfprSmMonitorMemAppTotal": cfprSmMonitorMemAppTotal,
       "cfprSmMonitorMemFree": cfprSmMonitorMemFree,
       "cfprSmMonitorMemTotal": cfprSmMonitorMemTotal,
       "cfprSmMonitorMemUsed": cfprSmMonitorMemUsed,
       "cfprSmMonitorSecondaryDiskAvailable": cfprSmMonitorSecondaryDiskAvailable,
       "cfprSmMonitorSecondaryDiskTotal": cfprSmMonitorSecondaryDiskTotal,
       "cfprSmMonitorDiskAvailForInstall": cfprSmMonitorDiskAvailForInstall,
       "cfprSmMonitorLastUpdateMonoTime": cfprSmMonitorLastUpdateMonoTime,
       "cfprSmNetMgmtBootstrapKeyEnumValueTable": cfprSmNetMgmtBootstrapKeyEnumValueTable,
       "cfprSmNetMgmtBootstrapKeyEnumValueEntry": cfprSmNetMgmtBootstrapKeyEnumValueEntry,
       "cfprSmNetMgmtBootstrapKeyEnumValueInstanceId": cfprSmNetMgmtBootstrapKeyEnumValueInstanceId,
       "cfprSmNetMgmtBootstrapValueTable": cfprSmNetMgmtBootstrapValueTable,
       "cfprSmNetMgmtBootstrapValueEntry": cfprSmNetMgmtBootstrapValueEntry,
       "cfprSmNetMgmtBootstrapValueInstanceId": cfprSmNetMgmtBootstrapValueInstanceId,
       "cfprSmPortRequirementTable": cfprSmPortRequirementTable,
       "cfprSmPortRequirementEntry": cfprSmPortRequirementEntry,
       "cfprSmPortRequirementInstanceId": cfprSmPortRequirementInstanceId,
       "cfprSmPortSubTypeTable": cfprSmPortSubTypeTable,
       "cfprSmPortSubTypeEntry": cfprSmPortSubTypeEntry,
       "cfprSmPortSubTypeInstanceId": cfprSmPortSubTypeInstanceId,
       "cfprSmResourceTable": cfprSmResourceTable,
       "cfprSmResourceEntry": cfprSmResourceEntry,
       "cfprSmResourceInstanceId": cfprSmResourceInstanceId,
       "cfprSmSecSvcTable": cfprSmSecSvcTable,
       "cfprSmSecSvcEntry": cfprSmSecSvcEntry,
       "cfprSmSecSvcInstanceId": cfprSmSecSvcInstanceId,
       "cfprSmSlotTable": cfprSmSlotTable,
       "cfprSmSlotEntry": cfprSmSlotEntry,
       "cfprSmSlotInstanceId": cfprSmSlotInstanceId,
       "cfprSmSystemMacTable": cfprSmSystemMacTable,
       "cfprSmSystemMacEntry": cfprSmSystemMacEntry,
       "cfprSmSystemMacInstanceId": cfprSmSystemMacInstanceId,
       "cfprSmTemplateAppTable": cfprSmTemplateAppTable,
       "cfprSmTemplateAppEntry": cfprSmTemplateAppEntry,
       "cfprSmTemplateAppInstanceId": cfprSmTemplateAppInstanceId,
       "cfprSmUserMacTable": cfprSmUserMacTable,
       "cfprSmUserMacEntry": cfprSmUserMacEntry,
       "cfprSmUserMacInstanceId": cfprSmUserMacInstanceId,
       "cfprSmAppInfoTable": cfprSmAppInfoTable,
       "cfprSmAppInfoEntry": cfprSmAppInfoEntry,
       "cfprSmAppInfoInstanceId": cfprSmAppInfoInstanceId,
       "cfprSmAppInstance2Table": cfprSmAppInstance2Table,
       "cfprSmAppInstance2Entry": cfprSmAppInstance2Entry,
       "cfprSmAppInstance2InstanceId": cfprSmAppInstance2InstanceId,
       "cfprSmAppInstance2FsmTable": cfprSmAppInstance2FsmTable,
       "cfprSmAppInstance2FsmEntry": cfprSmAppInstance2FsmEntry,
       "cfprSmAppInstance2FsmInstanceId": cfprSmAppInstance2FsmInstanceId,
       "cfprSmAppInstance2FsmStageTable": cfprSmAppInstance2FsmStageTable,
       "cfprSmAppInstance2FsmStageEntry": cfprSmAppInstance2FsmStageEntry,
       "cfprSmAppInstance2FsmStageInstanceId": cfprSmAppInstance2FsmStageInstanceId,
       "cfprSmAppInstance2FsmTaskTable": cfprSmAppInstance2FsmTaskTable,
       "cfprSmAppInstance2FsmTaskEntry": cfprSmAppInstance2FsmTaskEntry,
       "cfprSmAppInstance2FsmTaskInstanceId": cfprSmAppInstance2FsmTaskInstanceId,
       "cfprSmAppRscProfListTable": cfprSmAppRscProfListTable,
       "cfprSmAppRscProfListEntry": cfprSmAppRscProfListEntry,
       "cfprSmAppRscProfListInstanceId": cfprSmAppRscProfListInstanceId,
       "cfprSmAppRscProfileTable": cfprSmAppRscProfileTable,
       "cfprSmAppRscProfileEntry": cfprSmAppRscProfileEntry,
       "cfprSmAppRscProfileInstanceId": cfprSmAppRscProfileInstanceId,
       "cfprSmAutoMacPoolTable": cfprSmAutoMacPoolTable,
       "cfprSmAutoMacPoolEntry": cfprSmAutoMacPoolEntry,
       "cfprSmAutoMacPoolInstanceId": cfprSmAutoMacPoolInstanceId,
       "cfprSmBatchHeartbeatTable": cfprSmBatchHeartbeatTable,
       "cfprSmBatchHeartbeatEntry": cfprSmBatchHeartbeatEntry,
       "cfprSmBatchHeartbeatInstanceId": cfprSmBatchHeartbeatInstanceId,
       "cfprSmCloudConnectorTable": cfprSmCloudConnectorTable,
       "cfprSmCloudConnectorEntry": cfprSmCloudConnectorEntry,
       "cfprSmCloudConnectorInstanceId": cfprSmCloudConnectorInstanceId,
       "cfprSmCloudConnectorFsmTable": cfprSmCloudConnectorFsmTable,
       "cfprSmCloudConnectorFsmEntry": cfprSmCloudConnectorFsmEntry,
       "cfprSmCloudConnectorFsmInstanceId": cfprSmCloudConnectorFsmInstanceId,
       "cfprSmCloudConnectorFsmStageTable": cfprSmCloudConnectorFsmStageTable,
       "cfprSmCloudConnectorFsmStageEntry": cfprSmCloudConnectorFsmStageEntry,
       "cfprSmCloudConnectorFsmStageInstanceId": cfprSmCloudConnectorFsmStageInstanceId,
       "cfprSmCloudConnectorFsmTaskTable": cfprSmCloudConnectorFsmTaskTable,
       "cfprSmCloudConnectorFsmTaskEntry": cfprSmCloudConnectorFsmTaskEntry,
       "cfprSmCloudConnectorFsmTaskInstanceId": cfprSmCloudConnectorFsmTaskInstanceId,
       "cfprSmCompatibilityMatrixTable": cfprSmCompatibilityMatrixTable,
       "cfprSmCompatibilityMatrixEntry": cfprSmCompatibilityMatrixEntry,
       "cfprSmCompatibilityMatrixInstanceId": cfprSmCompatibilityMatrixInstanceId,
       "cfprSmConfigIssueTable": cfprSmConfigIssueTable,
       "cfprSmConfigIssueEntry": cfprSmConfigIssueEntry,
       "cfprSmConfigIssueInstanceId": cfprSmConfigIssueInstanceId,
       "cfprSmErrorTable": cfprSmErrorTable,
       "cfprSmErrorEntry": cfprSmErrorEntry,
       "cfprSmErrorInstanceId": cfprSmErrorInstanceId,
       "cfprSmHotfixTable": cfprSmHotfixTable,
       "cfprSmHotfixEntry": cfprSmHotfixEntry,
       "cfprSmHotfixInstanceId": cfprSmHotfixInstanceId,
       "cfprSmLicenseDeviceTable": cfprSmLicenseDeviceTable,
       "cfprSmLicenseDeviceEntry": cfprSmLicenseDeviceEntry,
       "cfprSmLicenseDeviceInstanceId": cfprSmLicenseDeviceInstanceId,
       "cfprSmLicenseFileTable": cfprSmLicenseFileTable,
       "cfprSmLicenseFileEntry": cfprSmLicenseFileEntry,
       "cfprSmLicenseFileInstanceId": cfprSmLicenseFileInstanceId,
       "cfprSmLicenseFileFsmTable": cfprSmLicenseFileFsmTable,
       "cfprSmLicenseFileFsmEntry": cfprSmLicenseFileFsmEntry,
       "cfprSmLicenseFileFsmInstanceId": cfprSmLicenseFileFsmInstanceId,
       "cfprSmLicenseFileFsmStageTable": cfprSmLicenseFileFsmStageTable,
       "cfprSmLicenseFileFsmStageEntry": cfprSmLicenseFileFsmStageEntry,
       "cfprSmLicenseFileFsmStageInstanceId": cfprSmLicenseFileFsmStageInstanceId,
       "cfprSmLicenseFileFsmTaskTable": cfprSmLicenseFileFsmTaskTable,
       "cfprSmLicenseFileFsmTaskEntry": cfprSmLicenseFileFsmTaskEntry,
       "cfprSmLicenseFileFsmTaskInstanceId": cfprSmLicenseFileFsmTaskInstanceId,
       "cfprSmLogicalDeviceFsmTable": cfprSmLogicalDeviceFsmTable,
       "cfprSmLogicalDeviceFsmEntry": cfprSmLogicalDeviceFsmEntry,
       "cfprSmLogicalDeviceFsmInstanceId": cfprSmLogicalDeviceFsmInstanceId,
       "cfprSmLogicalDeviceFsmStageTable": cfprSmLogicalDeviceFsmStageTable,
       "cfprSmLogicalDeviceFsmStageEntry": cfprSmLogicalDeviceFsmStageEntry,
       "cfprSmLogicalDeviceFsmStageInstanceId": cfprSmLogicalDeviceFsmStageInstanceId,
       "cfprSmLogicalDeviceFsmTaskTable": cfprSmLogicalDeviceFsmTaskTable,
       "cfprSmLogicalDeviceFsmTaskEntry": cfprSmLogicalDeviceFsmTaskEntry,
       "cfprSmLogicalDeviceFsmTaskInstanceId": cfprSmLogicalDeviceFsmTaskInstanceId,
       "cfprSmMacItemTable": cfprSmMacItemTable,
       "cfprSmMacItemEntry": cfprSmMacItemEntry,
       "cfprSmMacItemInstanceId": cfprSmMacItemInstanceId,
       "cfprSmNetMgmtBootstrapKeyLimitsTable": cfprSmNetMgmtBootstrapKeyLimitsTable,
       "cfprSmNetMgmtBootstrapKeyLimitsEntry": cfprSmNetMgmtBootstrapKeyLimitsEntry,
       "cfprSmNetMgmtBootstrapKeyLimitsInstanceId": cfprSmNetMgmtBootstrapKeyLimitsInstanceId,
       "cfprSmPreRequisiteTable": cfprSmPreRequisiteTable,
       "cfprSmPreRequisiteEntry": cfprSmPreRequisiteEntry,
       "cfprSmPreRequisiteInstanceId": cfprSmPreRequisiteInstanceId,
       "cfprSmReplyInterfaceCfgTable": cfprSmReplyInterfaceCfgTable,
       "cfprSmReplyInterfaceCfgEntry": cfprSmReplyInterfaceCfgEntry,
       "cfprSmReplyInterfaceCfgInstanceId": cfprSmReplyInterfaceCfgInstanceId,
       "cfprSmSupportedHardwareTable": cfprSmSupportedHardwareTable,
       "cfprSmSupportedHardwareEntry": cfprSmSupportedHardwareEntry,
       "cfprSmSupportedHardwareInstanceId": cfprSmSupportedHardwareInstanceId,
       "cfprSmUnsignedCspLicenseTable": cfprSmUnsignedCspLicenseTable,
       "cfprSmUnsignedCspLicenseEntry": cfprSmUnsignedCspLicenseEntry,
       "cfprSmUnsignedCspLicenseInstanceId": cfprSmUnsignedCspLicenseInstanceId,
       "cfprSmUnsignedCspLicenseFsmTable": cfprSmUnsignedCspLicenseFsmTable,
       "cfprSmUnsignedCspLicenseFsmEntry": cfprSmUnsignedCspLicenseFsmEntry,
       "cfprSmUnsignedCspLicenseFsmInstanceId": cfprSmUnsignedCspLicenseFsmInstanceId,
       "cfprSmUnsignedCspLicenseFsmStageTable": cfprSmUnsignedCspLicenseFsmStageTable,
       "cfprSmUnsignedCspLicenseFsmStageEntry": cfprSmUnsignedCspLicenseFsmStageEntry,
       "cfprSmUnsignedCspLicenseFsmStageInstanceId": cfprSmUnsignedCspLicenseFsmStageInstanceId,
       "cfprSmUnsignedCspLicenseFsmTaskTable": cfprSmUnsignedCspLicenseFsmTaskTable,
       "cfprSmUnsignedCspLicenseFsmTaskEntry": cfprSmUnsignedCspLicenseFsmTaskEntry,
       "cfprSmUnsignedCspLicenseFsmTaskInstanceId": cfprSmUnsignedCspLicenseFsmTaskInstanceId,
       "cfprSmHwCryptoTable": cfprSmHwCryptoTable,
       "cfprSmHwCryptoEntry": cfprSmHwCryptoEntry,
       "cfprSmHwCryptoInstanceId": cfprSmHwCryptoInstanceId}
)
