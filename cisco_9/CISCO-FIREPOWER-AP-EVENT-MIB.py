# SNMP MIB module (CISCO-FIREPOWER-AP-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-EVENT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:16:52 2025
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

(CfprApConditionActionIndicator,
 CfprApConditionCause,
 CfprApConditionCode,
 CfprApConditionRule,
 CfprApConditionSeverity,
 CfprApConditionTag,
 CfprApConditionType,
 CfprApEventEpCtrlLevel,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionActionIndicator",
    "CfprApConditionCause",
    "CfprApConditionCode",
    "CfprApConditionRule",
    "CfprApConditionSeverity",
    "CfprApConditionTag",
    "CfprApConditionType",
    "CfprApEventEpCtrlLevel",
    "CfprApPolicyPolicyOwner")

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

cfprApEventObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApEventEpCtrlTable_Object = MibTable
cfprApEventEpCtrlTable = _CfprApEventEpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 1)
)
if mibBuilder.loadTexts:
    cfprApEventEpCtrlTable.setStatus("current")
_CfprApEventEpCtrlEntry_Object = MibTableRow
cfprApEventEpCtrlEntry = _CfprApEventEpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 1, 1)
)
cfprApEventEpCtrlEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EVENT-MIB", "cfprApEventEpCtrlInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEventEpCtrlEntry.setStatus("current")
_CfprApEventEpCtrlInstanceId_Type = CfprApManagedObjectId
_CfprApEventEpCtrlInstanceId_Object = MibTableColumn
cfprApEventEpCtrlInstanceId = _CfprApEventEpCtrlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 1, 1, 1),
    _CfprApEventEpCtrlInstanceId_Type()
)
cfprApEventEpCtrlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEventEpCtrlInstanceId.setStatus("current")
_CfprApEventEpCtrlDn_Type = CfprApManagedObjectDn
_CfprApEventEpCtrlDn_Object = MibTableColumn
cfprApEventEpCtrlDn = _CfprApEventEpCtrlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 1, 1, 2),
    _CfprApEventEpCtrlDn_Type()
)
cfprApEventEpCtrlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventEpCtrlDn.setStatus("current")
_CfprApEventEpCtrlRn_Type = SnmpAdminString
_CfprApEventEpCtrlRn_Object = MibTableColumn
cfprApEventEpCtrlRn = _CfprApEventEpCtrlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 1, 1, 3),
    _CfprApEventEpCtrlRn_Type()
)
cfprApEventEpCtrlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventEpCtrlRn.setStatus("current")
_CfprApEventEpCtrlLevel_Type = CfprApEventEpCtrlLevel
_CfprApEventEpCtrlLevel_Object = MibTableColumn
cfprApEventEpCtrlLevel = _CfprApEventEpCtrlLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 1, 1, 4),
    _CfprApEventEpCtrlLevel_Type()
)
cfprApEventEpCtrlLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventEpCtrlLevel.setStatus("current")
_CfprApEventEpCtrlRevertTimeout_Type = TimeIntervalSec
_CfprApEventEpCtrlRevertTimeout_Object = MibTableColumn
cfprApEventEpCtrlRevertTimeout = _CfprApEventEpCtrlRevertTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 1, 1, 5),
    _CfprApEventEpCtrlRevertTimeout_Type()
)
cfprApEventEpCtrlRevertTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventEpCtrlRevertTimeout.setStatus("current")
_CfprApEventHolderTable_Object = MibTable
cfprApEventHolderTable = _CfprApEventHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 2)
)
if mibBuilder.loadTexts:
    cfprApEventHolderTable.setStatus("current")
_CfprApEventHolderEntry_Object = MibTableRow
cfprApEventHolderEntry = _CfprApEventHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 2, 1)
)
cfprApEventHolderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EVENT-MIB", "cfprApEventHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEventHolderEntry.setStatus("current")
_CfprApEventHolderInstanceId_Type = CfprApManagedObjectId
_CfprApEventHolderInstanceId_Object = MibTableColumn
cfprApEventHolderInstanceId = _CfprApEventHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 2, 1, 1),
    _CfprApEventHolderInstanceId_Type()
)
cfprApEventHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEventHolderInstanceId.setStatus("current")
_CfprApEventHolderDn_Type = CfprApManagedObjectDn
_CfprApEventHolderDn_Object = MibTableColumn
cfprApEventHolderDn = _CfprApEventHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 2, 1, 2),
    _CfprApEventHolderDn_Type()
)
cfprApEventHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventHolderDn.setStatus("current")
_CfprApEventHolderRn_Type = SnmpAdminString
_CfprApEventHolderRn_Object = MibTableColumn
cfprApEventHolderRn = _CfprApEventHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 2, 1, 3),
    _CfprApEventHolderRn_Type()
)
cfprApEventHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventHolderRn.setStatus("current")
_CfprApEventHolderName_Type = SnmpAdminString
_CfprApEventHolderName_Object = MibTableColumn
cfprApEventHolderName = _CfprApEventHolderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 2, 1, 4),
    _CfprApEventHolderName_Type()
)
cfprApEventHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventHolderName.setStatus("current")
_CfprApEventInstTable_Object = MibTable
cfprApEventInstTable = _CfprApEventInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3)
)
if mibBuilder.loadTexts:
    cfprApEventInstTable.setStatus("current")
_CfprApEventInstEntry_Object = MibTableRow
cfprApEventInstEntry = _CfprApEventInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1)
)
cfprApEventInstEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EVENT-MIB", "cfprApEventInstInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEventInstEntry.setStatus("current")
_CfprApEventInstInstanceId_Type = CfprApManagedObjectId
_CfprApEventInstInstanceId_Object = MibTableColumn
cfprApEventInstInstanceId = _CfprApEventInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 1),
    _CfprApEventInstInstanceId_Type()
)
cfprApEventInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEventInstInstanceId.setStatus("current")
_CfprApEventInstDn_Type = CfprApManagedObjectDn
_CfprApEventInstDn_Object = MibTableColumn
cfprApEventInstDn = _CfprApEventInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 2),
    _CfprApEventInstDn_Type()
)
cfprApEventInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventInstDn.setStatus("current")
_CfprApEventInstRn_Type = SnmpAdminString
_CfprApEventInstRn_Object = MibTableColumn
cfprApEventInstRn = _CfprApEventInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 3),
    _CfprApEventInstRn_Type()
)
cfprApEventInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventInstRn.setStatus("current")
_CfprApEventInstCause_Type = CfprApConditionCause
_CfprApEventInstCause_Object = MibTableColumn
cfprApEventInstCause = _CfprApEventInstCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 4),
    _CfprApEventInstCause_Type()
)
cfprApEventInstCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventInstCause.setStatus("current")
_CfprApEventInstChangeSet_Type = SnmpAdminString
_CfprApEventInstChangeSet_Object = MibTableColumn
cfprApEventInstChangeSet = _CfprApEventInstChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 5),
    _CfprApEventInstChangeSet_Type()
)
cfprApEventInstChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventInstChangeSet.setStatus("current")
_CfprApEventInstCode_Type = CfprApConditionCode
_CfprApEventInstCode_Object = MibTableColumn
cfprApEventInstCode = _CfprApEventInstCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 6),
    _CfprApEventInstCode_Type()
)
cfprApEventInstCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventInstCode.setStatus("current")
_CfprApEventInstCreated_Type = DateAndTime
_CfprApEventInstCreated_Object = MibTableColumn
cfprApEventInstCreated = _CfprApEventInstCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 7),
    _CfprApEventInstCreated_Type()
)
cfprApEventInstCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventInstCreated.setStatus("current")
_CfprApEventInstDescr_Type = SnmpAdminString
_CfprApEventInstDescr_Object = MibTableColumn
cfprApEventInstDescr = _CfprApEventInstDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 8),
    _CfprApEventInstDescr_Type()
)
cfprApEventInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventInstDescr.setStatus("current")
_CfprApEventInstId_Type = Unsigned64
_CfprApEventInstId_Object = MibTableColumn
cfprApEventInstId = _CfprApEventInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 9),
    _CfprApEventInstId_Type()
)
cfprApEventInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventInstId.setStatus("current")
_CfprApEventInstRule_Type = CfprApConditionRule
_CfprApEventInstRule_Object = MibTableColumn
cfprApEventInstRule = _CfprApEventInstRule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 10),
    _CfprApEventInstRule_Type()
)
cfprApEventInstRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventInstRule.setStatus("current")
_CfprApEventInstSeverity_Type = CfprApConditionSeverity
_CfprApEventInstSeverity_Object = MibTableColumn
cfprApEventInstSeverity = _CfprApEventInstSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 11),
    _CfprApEventInstSeverity_Type()
)
cfprApEventInstSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventInstSeverity.setStatus("current")
_CfprApEventInstTags_Type = CfprApConditionTag
_CfprApEventInstTags_Object = MibTableColumn
cfprApEventInstTags = _CfprApEventInstTags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 12),
    _CfprApEventInstTags_Type()
)
cfprApEventInstTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventInstTags.setStatus("current")
_CfprApEventInstType_Type = CfprApConditionType
_CfprApEventInstType_Object = MibTableColumn
cfprApEventInstType = _CfprApEventInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 3, 1, 13),
    _CfprApEventInstType_Type()
)
cfprApEventInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventInstType.setStatus("current")
_CfprApEventLogTable_Object = MibTable
cfprApEventLogTable = _CfprApEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 4)
)
if mibBuilder.loadTexts:
    cfprApEventLogTable.setStatus("current")
_CfprApEventLogEntry_Object = MibTableRow
cfprApEventLogEntry = _CfprApEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 4, 1)
)
cfprApEventLogEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EVENT-MIB", "cfprApEventLogInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEventLogEntry.setStatus("current")
_CfprApEventLogInstanceId_Type = CfprApManagedObjectId
_CfprApEventLogInstanceId_Object = MibTableColumn
cfprApEventLogInstanceId = _CfprApEventLogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 4, 1, 1),
    _CfprApEventLogInstanceId_Type()
)
cfprApEventLogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEventLogInstanceId.setStatus("current")
_CfprApEventLogDn_Type = CfprApManagedObjectDn
_CfprApEventLogDn_Object = MibTableColumn
cfprApEventLogDn = _CfprApEventLogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 4, 1, 2),
    _CfprApEventLogDn_Type()
)
cfprApEventLogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventLogDn.setStatus("current")
_CfprApEventLogRn_Type = SnmpAdminString
_CfprApEventLogRn_Object = MibTableColumn
cfprApEventLogRn = _CfprApEventLogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 4, 1, 3),
    _CfprApEventLogRn_Type()
)
cfprApEventLogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventLogRn.setStatus("current")
_CfprApEventLogMaxSize_Type = Gauge32
_CfprApEventLogMaxSize_Object = MibTableColumn
cfprApEventLogMaxSize = _CfprApEventLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 4, 1, 4),
    _CfprApEventLogMaxSize_Type()
)
cfprApEventLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventLogMaxSize.setStatus("current")
_CfprApEventLogPurgeWindow_Type = Gauge32
_CfprApEventLogPurgeWindow_Object = MibTableColumn
cfprApEventLogPurgeWindow = _CfprApEventLogPurgeWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 4, 1, 5),
    _CfprApEventLogPurgeWindow_Type()
)
cfprApEventLogPurgeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventLogPurgeWindow.setStatus("current")
_CfprApEventLogSize_Type = Gauge32
_CfprApEventLogSize_Object = MibTableColumn
cfprApEventLogSize = _CfprApEventLogSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 4, 1, 6),
    _CfprApEventLogSize_Type()
)
cfprApEventLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventLogSize.setStatus("current")
_CfprApEventPolicyTable_Object = MibTable
cfprApEventPolicyTable = _CfprApEventPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 5)
)
if mibBuilder.loadTexts:
    cfprApEventPolicyTable.setStatus("current")
_CfprApEventPolicyEntry_Object = MibTableRow
cfprApEventPolicyEntry = _CfprApEventPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 5, 1)
)
cfprApEventPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EVENT-MIB", "cfprApEventPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEventPolicyEntry.setStatus("current")
_CfprApEventPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApEventPolicyInstanceId_Object = MibTableColumn
cfprApEventPolicyInstanceId = _CfprApEventPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 5, 1, 1),
    _CfprApEventPolicyInstanceId_Type()
)
cfprApEventPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEventPolicyInstanceId.setStatus("current")
_CfprApEventPolicyDn_Type = CfprApManagedObjectDn
_CfprApEventPolicyDn_Object = MibTableColumn
cfprApEventPolicyDn = _CfprApEventPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 5, 1, 2),
    _CfprApEventPolicyDn_Type()
)
cfprApEventPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventPolicyDn.setStatus("current")
_CfprApEventPolicyRn_Type = SnmpAdminString
_CfprApEventPolicyRn_Object = MibTableColumn
cfprApEventPolicyRn = _CfprApEventPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 5, 1, 3),
    _CfprApEventPolicyRn_Type()
)
cfprApEventPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventPolicyRn.setStatus("current")
_CfprApEventPolicyDescr_Type = SnmpAdminString
_CfprApEventPolicyDescr_Object = MibTableColumn
cfprApEventPolicyDescr = _CfprApEventPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 5, 1, 4),
    _CfprApEventPolicyDescr_Type()
)
cfprApEventPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventPolicyDescr.setStatus("current")
_CfprApEventPolicyIntId_Type = SnmpAdminString
_CfprApEventPolicyIntId_Object = MibTableColumn
cfprApEventPolicyIntId = _CfprApEventPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 5, 1, 5),
    _CfprApEventPolicyIntId_Type()
)
cfprApEventPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventPolicyIntId.setStatus("current")
_CfprApEventPolicyName_Type = SnmpAdminString
_CfprApEventPolicyName_Object = MibTableColumn
cfprApEventPolicyName = _CfprApEventPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 5, 1, 6),
    _CfprApEventPolicyName_Type()
)
cfprApEventPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventPolicyName.setStatus("current")
_CfprApEventPolicyPolicyLevel_Type = Gauge32
_CfprApEventPolicyPolicyLevel_Object = MibTableColumn
cfprApEventPolicyPolicyLevel = _CfprApEventPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 5, 1, 7),
    _CfprApEventPolicyPolicyLevel_Type()
)
cfprApEventPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventPolicyPolicyLevel.setStatus("current")
_CfprApEventPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApEventPolicyPolicyOwner_Object = MibTableColumn
cfprApEventPolicyPolicyOwner = _CfprApEventPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 5, 1, 8),
    _CfprApEventPolicyPolicyOwner_Type()
)
cfprApEventPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventPolicyPolicyOwner.setStatus("current")
_CfprApEventPolicyRetentionInterval_Type = TimeIntervalSec
_CfprApEventPolicyRetentionInterval_Object = MibTableColumn
cfprApEventPolicyRetentionInterval = _CfprApEventPolicyRetentionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 5, 1, 9),
    _CfprApEventPolicyRetentionInterval_Type()
)
cfprApEventPolicyRetentionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventPolicyRetentionInterval.setStatus("current")
_CfprApEventPolicySizeLimit_Type = Gauge32
_CfprApEventPolicySizeLimit_Object = MibTableColumn
cfprApEventPolicySizeLimit = _CfprApEventPolicySizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 5, 1, 10),
    _CfprApEventPolicySizeLimit_Type()
)
cfprApEventPolicySizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventPolicySizeLimit.setStatus("current")
_CfprApEventRecordTable_Object = MibTable
cfprApEventRecordTable = _CfprApEventRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6)
)
if mibBuilder.loadTexts:
    cfprApEventRecordTable.setStatus("current")
_CfprApEventRecordEntry_Object = MibTableRow
cfprApEventRecordEntry = _CfprApEventRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1)
)
cfprApEventRecordEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EVENT-MIB", "cfprApEventRecordInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApEventRecordEntry.setStatus("current")
_CfprApEventRecordInstanceId_Type = CfprApManagedObjectId
_CfprApEventRecordInstanceId_Object = MibTableColumn
cfprApEventRecordInstanceId = _CfprApEventRecordInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 1),
    _CfprApEventRecordInstanceId_Type()
)
cfprApEventRecordInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApEventRecordInstanceId.setStatus("current")
_CfprApEventRecordDn_Type = CfprApManagedObjectDn
_CfprApEventRecordDn_Object = MibTableColumn
cfprApEventRecordDn = _CfprApEventRecordDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 2),
    _CfprApEventRecordDn_Type()
)
cfprApEventRecordDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordDn.setStatus("current")
_CfprApEventRecordRn_Type = SnmpAdminString
_CfprApEventRecordRn_Object = MibTableColumn
cfprApEventRecordRn = _CfprApEventRecordRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 3),
    _CfprApEventRecordRn_Type()
)
cfprApEventRecordRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordRn.setStatus("current")
_CfprApEventRecordAffected_Type = SnmpAdminString
_CfprApEventRecordAffected_Object = MibTableColumn
cfprApEventRecordAffected = _CfprApEventRecordAffected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 4),
    _CfprApEventRecordAffected_Type()
)
cfprApEventRecordAffected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordAffected.setStatus("current")
_CfprApEventRecordCause_Type = CfprApConditionCause
_CfprApEventRecordCause_Object = MibTableColumn
cfprApEventRecordCause = _CfprApEventRecordCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 5),
    _CfprApEventRecordCause_Type()
)
cfprApEventRecordCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordCause.setStatus("current")
_CfprApEventRecordChangeSet_Type = SnmpAdminString
_CfprApEventRecordChangeSet_Object = MibTableColumn
cfprApEventRecordChangeSet = _CfprApEventRecordChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 6),
    _CfprApEventRecordChangeSet_Type()
)
cfprApEventRecordChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordChangeSet.setStatus("current")
_CfprApEventRecordCode_Type = CfprApConditionCode
_CfprApEventRecordCode_Object = MibTableColumn
cfprApEventRecordCode = _CfprApEventRecordCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 7),
    _CfprApEventRecordCode_Type()
)
cfprApEventRecordCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordCode.setStatus("current")
_CfprApEventRecordCreated_Type = DateAndTime
_CfprApEventRecordCreated_Object = MibTableColumn
cfprApEventRecordCreated = _CfprApEventRecordCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 8),
    _CfprApEventRecordCreated_Type()
)
cfprApEventRecordCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordCreated.setStatus("current")
_CfprApEventRecordDescr_Type = SnmpAdminString
_CfprApEventRecordDescr_Object = MibTableColumn
cfprApEventRecordDescr = _CfprApEventRecordDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 9),
    _CfprApEventRecordDescr_Type()
)
cfprApEventRecordDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordDescr.setStatus("current")
_CfprApEventRecordId_Type = Gauge32
_CfprApEventRecordId_Object = MibTableColumn
cfprApEventRecordId = _CfprApEventRecordId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 10),
    _CfprApEventRecordId_Type()
)
cfprApEventRecordId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordId.setStatus("current")
_CfprApEventRecordInd_Type = CfprApConditionActionIndicator
_CfprApEventRecordInd_Object = MibTableColumn
cfprApEventRecordInd = _CfprApEventRecordInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 11),
    _CfprApEventRecordInd_Type()
)
cfprApEventRecordInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordInd.setStatus("current")
_CfprApEventRecordSessionId_Type = SnmpAdminString
_CfprApEventRecordSessionId_Object = MibTableColumn
cfprApEventRecordSessionId = _CfprApEventRecordSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 12),
    _CfprApEventRecordSessionId_Type()
)
cfprApEventRecordSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordSessionId.setStatus("current")
_CfprApEventRecordSeverity_Type = CfprApConditionSeverity
_CfprApEventRecordSeverity_Object = MibTableColumn
cfprApEventRecordSeverity = _CfprApEventRecordSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 13),
    _CfprApEventRecordSeverity_Type()
)
cfprApEventRecordSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordSeverity.setStatus("current")
_CfprApEventRecordTrig_Type = Gauge32
_CfprApEventRecordTrig_Object = MibTableColumn
cfprApEventRecordTrig = _CfprApEventRecordTrig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 14),
    _CfprApEventRecordTrig_Type()
)
cfprApEventRecordTrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordTrig.setStatus("current")
_CfprApEventRecordTxId_Type = Unsigned64
_CfprApEventRecordTxId_Object = MibTableColumn
cfprApEventRecordTxId = _CfprApEventRecordTxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 15),
    _CfprApEventRecordTxId_Type()
)
cfprApEventRecordTxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordTxId.setStatus("current")
_CfprApEventRecordUser_Type = SnmpAdminString
_CfprApEventRecordUser_Object = MibTableColumn
cfprApEventRecordUser = _CfprApEventRecordUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 22, 6, 1, 16),
    _CfprApEventRecordUser_Type()
)
cfprApEventRecordUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApEventRecordUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-EVENT-MIB",
    **{"cfprApEventObjects": cfprApEventObjects,
       "cfprApEventEpCtrlTable": cfprApEventEpCtrlTable,
       "cfprApEventEpCtrlEntry": cfprApEventEpCtrlEntry,
       "cfprApEventEpCtrlInstanceId": cfprApEventEpCtrlInstanceId,
       "cfprApEventEpCtrlDn": cfprApEventEpCtrlDn,
       "cfprApEventEpCtrlRn": cfprApEventEpCtrlRn,
       "cfprApEventEpCtrlLevel": cfprApEventEpCtrlLevel,
       "cfprApEventEpCtrlRevertTimeout": cfprApEventEpCtrlRevertTimeout,
       "cfprApEventHolderTable": cfprApEventHolderTable,
       "cfprApEventHolderEntry": cfprApEventHolderEntry,
       "cfprApEventHolderInstanceId": cfprApEventHolderInstanceId,
       "cfprApEventHolderDn": cfprApEventHolderDn,
       "cfprApEventHolderRn": cfprApEventHolderRn,
       "cfprApEventHolderName": cfprApEventHolderName,
       "cfprApEventInstTable": cfprApEventInstTable,
       "cfprApEventInstEntry": cfprApEventInstEntry,
       "cfprApEventInstInstanceId": cfprApEventInstInstanceId,
       "cfprApEventInstDn": cfprApEventInstDn,
       "cfprApEventInstRn": cfprApEventInstRn,
       "cfprApEventInstCause": cfprApEventInstCause,
       "cfprApEventInstChangeSet": cfprApEventInstChangeSet,
       "cfprApEventInstCode": cfprApEventInstCode,
       "cfprApEventInstCreated": cfprApEventInstCreated,
       "cfprApEventInstDescr": cfprApEventInstDescr,
       "cfprApEventInstId": cfprApEventInstId,
       "cfprApEventInstRule": cfprApEventInstRule,
       "cfprApEventInstSeverity": cfprApEventInstSeverity,
       "cfprApEventInstTags": cfprApEventInstTags,
       "cfprApEventInstType": cfprApEventInstType,
       "cfprApEventLogTable": cfprApEventLogTable,
       "cfprApEventLogEntry": cfprApEventLogEntry,
       "cfprApEventLogInstanceId": cfprApEventLogInstanceId,
       "cfprApEventLogDn": cfprApEventLogDn,
       "cfprApEventLogRn": cfprApEventLogRn,
       "cfprApEventLogMaxSize": cfprApEventLogMaxSize,
       "cfprApEventLogPurgeWindow": cfprApEventLogPurgeWindow,
       "cfprApEventLogSize": cfprApEventLogSize,
       "cfprApEventPolicyTable": cfprApEventPolicyTable,
       "cfprApEventPolicyEntry": cfprApEventPolicyEntry,
       "cfprApEventPolicyInstanceId": cfprApEventPolicyInstanceId,
       "cfprApEventPolicyDn": cfprApEventPolicyDn,
       "cfprApEventPolicyRn": cfprApEventPolicyRn,
       "cfprApEventPolicyDescr": cfprApEventPolicyDescr,
       "cfprApEventPolicyIntId": cfprApEventPolicyIntId,
       "cfprApEventPolicyName": cfprApEventPolicyName,
       "cfprApEventPolicyPolicyLevel": cfprApEventPolicyPolicyLevel,
       "cfprApEventPolicyPolicyOwner": cfprApEventPolicyPolicyOwner,
       "cfprApEventPolicyRetentionInterval": cfprApEventPolicyRetentionInterval,
       "cfprApEventPolicySizeLimit": cfprApEventPolicySizeLimit,
       "cfprApEventRecordTable": cfprApEventRecordTable,
       "cfprApEventRecordEntry": cfprApEventRecordEntry,
       "cfprApEventRecordInstanceId": cfprApEventRecordInstanceId,
       "cfprApEventRecordDn": cfprApEventRecordDn,
       "cfprApEventRecordRn": cfprApEventRecordRn,
       "cfprApEventRecordAffected": cfprApEventRecordAffected,
       "cfprApEventRecordCause": cfprApEventRecordCause,
       "cfprApEventRecordChangeSet": cfprApEventRecordChangeSet,
       "cfprApEventRecordCode": cfprApEventRecordCode,
       "cfprApEventRecordCreated": cfprApEventRecordCreated,
       "cfprApEventRecordDescr": cfprApEventRecordDescr,
       "cfprApEventRecordId": cfprApEventRecordId,
       "cfprApEventRecordInd": cfprApEventRecordInd,
       "cfprApEventRecordSessionId": cfprApEventRecordSessionId,
       "cfprApEventRecordSeverity": cfprApEventRecordSeverity,
       "cfprApEventRecordTrig": cfprApEventRecordTrig,
       "cfprApEventRecordTxId": cfprApEventRecordTxId,
       "cfprApEventRecordUser": cfprApEventRecordUser}
)
