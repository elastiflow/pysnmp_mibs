# SNMP MIB module (CISCO-FIREPOWER-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-EVENT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:11 2025
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

(CfprConditionActionIndicator,
 CfprConditionCause,
 CfprConditionCode,
 CfprConditionRule,
 CfprConditionSeverity,
 CfprConditionTag,
 CfprConditionType,
 CfprEventEpCtrlLevel,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionActionIndicator",
    "CfprConditionCause",
    "CfprConditionCode",
    "CfprConditionRule",
    "CfprConditionSeverity",
    "CfprConditionTag",
    "CfprConditionType",
    "CfprEventEpCtrlLevel",
    "CfprPolicyPolicyOwner")

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

cfprEventObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprEventEpCtrlTable_Object = MibTable
cfprEventEpCtrlTable = _CfprEventEpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 1)
)
if mibBuilder.loadTexts:
    cfprEventEpCtrlTable.setStatus("current")
_CfprEventEpCtrlEntry_Object = MibTableRow
cfprEventEpCtrlEntry = _CfprEventEpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 1, 1)
)
cfprEventEpCtrlEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EVENT-MIB", "cfprEventEpCtrlInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEventEpCtrlEntry.setStatus("current")
_CfprEventEpCtrlInstanceId_Type = CfprManagedObjectId
_CfprEventEpCtrlInstanceId_Object = MibTableColumn
cfprEventEpCtrlInstanceId = _CfprEventEpCtrlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 1, 1, 1),
    _CfprEventEpCtrlInstanceId_Type()
)
cfprEventEpCtrlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEventEpCtrlInstanceId.setStatus("current")
_CfprEventEpCtrlDn_Type = CfprManagedObjectDn
_CfprEventEpCtrlDn_Object = MibTableColumn
cfprEventEpCtrlDn = _CfprEventEpCtrlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 1, 1, 2),
    _CfprEventEpCtrlDn_Type()
)
cfprEventEpCtrlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventEpCtrlDn.setStatus("current")
_CfprEventEpCtrlRn_Type = SnmpAdminString
_CfprEventEpCtrlRn_Object = MibTableColumn
cfprEventEpCtrlRn = _CfprEventEpCtrlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 1, 1, 3),
    _CfprEventEpCtrlRn_Type()
)
cfprEventEpCtrlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventEpCtrlRn.setStatus("current")
_CfprEventEpCtrlLevel_Type = CfprEventEpCtrlLevel
_CfprEventEpCtrlLevel_Object = MibTableColumn
cfprEventEpCtrlLevel = _CfprEventEpCtrlLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 1, 1, 4),
    _CfprEventEpCtrlLevel_Type()
)
cfprEventEpCtrlLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventEpCtrlLevel.setStatus("current")
_CfprEventEpCtrlRevertTimeout_Type = TimeIntervalSec
_CfprEventEpCtrlRevertTimeout_Object = MibTableColumn
cfprEventEpCtrlRevertTimeout = _CfprEventEpCtrlRevertTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 1, 1, 5),
    _CfprEventEpCtrlRevertTimeout_Type()
)
cfprEventEpCtrlRevertTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventEpCtrlRevertTimeout.setStatus("current")
_CfprEventHolderTable_Object = MibTable
cfprEventHolderTable = _CfprEventHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 2)
)
if mibBuilder.loadTexts:
    cfprEventHolderTable.setStatus("current")
_CfprEventHolderEntry_Object = MibTableRow
cfprEventHolderEntry = _CfprEventHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 2, 1)
)
cfprEventHolderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EVENT-MIB", "cfprEventHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEventHolderEntry.setStatus("current")
_CfprEventHolderInstanceId_Type = CfprManagedObjectId
_CfprEventHolderInstanceId_Object = MibTableColumn
cfprEventHolderInstanceId = _CfprEventHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 2, 1, 1),
    _CfprEventHolderInstanceId_Type()
)
cfprEventHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEventHolderInstanceId.setStatus("current")
_CfprEventHolderDn_Type = CfprManagedObjectDn
_CfprEventHolderDn_Object = MibTableColumn
cfprEventHolderDn = _CfprEventHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 2, 1, 2),
    _CfprEventHolderDn_Type()
)
cfprEventHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventHolderDn.setStatus("current")
_CfprEventHolderRn_Type = SnmpAdminString
_CfprEventHolderRn_Object = MibTableColumn
cfprEventHolderRn = _CfprEventHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 2, 1, 3),
    _CfprEventHolderRn_Type()
)
cfprEventHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventHolderRn.setStatus("current")
_CfprEventHolderName_Type = SnmpAdminString
_CfprEventHolderName_Object = MibTableColumn
cfprEventHolderName = _CfprEventHolderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 2, 1, 4),
    _CfprEventHolderName_Type()
)
cfprEventHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventHolderName.setStatus("current")
_CfprEventInstTable_Object = MibTable
cfprEventInstTable = _CfprEventInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3)
)
if mibBuilder.loadTexts:
    cfprEventInstTable.setStatus("current")
_CfprEventInstEntry_Object = MibTableRow
cfprEventInstEntry = _CfprEventInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1)
)
cfprEventInstEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EVENT-MIB", "cfprEventInstInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEventInstEntry.setStatus("current")
_CfprEventInstInstanceId_Type = CfprManagedObjectId
_CfprEventInstInstanceId_Object = MibTableColumn
cfprEventInstInstanceId = _CfprEventInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 1),
    _CfprEventInstInstanceId_Type()
)
cfprEventInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEventInstInstanceId.setStatus("current")
_CfprEventInstDn_Type = CfprManagedObjectDn
_CfprEventInstDn_Object = MibTableColumn
cfprEventInstDn = _CfprEventInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 2),
    _CfprEventInstDn_Type()
)
cfprEventInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventInstDn.setStatus("current")
_CfprEventInstRn_Type = SnmpAdminString
_CfprEventInstRn_Object = MibTableColumn
cfprEventInstRn = _CfprEventInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 3),
    _CfprEventInstRn_Type()
)
cfprEventInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventInstRn.setStatus("current")
_CfprEventInstCause_Type = CfprConditionCause
_CfprEventInstCause_Object = MibTableColumn
cfprEventInstCause = _CfprEventInstCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 4),
    _CfprEventInstCause_Type()
)
cfprEventInstCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventInstCause.setStatus("current")
_CfprEventInstChangeSet_Type = SnmpAdminString
_CfprEventInstChangeSet_Object = MibTableColumn
cfprEventInstChangeSet = _CfprEventInstChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 5),
    _CfprEventInstChangeSet_Type()
)
cfprEventInstChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventInstChangeSet.setStatus("current")
_CfprEventInstCode_Type = CfprConditionCode
_CfprEventInstCode_Object = MibTableColumn
cfprEventInstCode = _CfprEventInstCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 6),
    _CfprEventInstCode_Type()
)
cfprEventInstCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventInstCode.setStatus("current")
_CfprEventInstCreated_Type = DateAndTime
_CfprEventInstCreated_Object = MibTableColumn
cfprEventInstCreated = _CfprEventInstCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 7),
    _CfprEventInstCreated_Type()
)
cfprEventInstCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventInstCreated.setStatus("current")
_CfprEventInstDescr_Type = SnmpAdminString
_CfprEventInstDescr_Object = MibTableColumn
cfprEventInstDescr = _CfprEventInstDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 8),
    _CfprEventInstDescr_Type()
)
cfprEventInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventInstDescr.setStatus("current")
_CfprEventInstId_Type = Unsigned64
_CfprEventInstId_Object = MibTableColumn
cfprEventInstId = _CfprEventInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 9),
    _CfprEventInstId_Type()
)
cfprEventInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventInstId.setStatus("current")
_CfprEventInstRule_Type = CfprConditionRule
_CfprEventInstRule_Object = MibTableColumn
cfprEventInstRule = _CfprEventInstRule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 10),
    _CfprEventInstRule_Type()
)
cfprEventInstRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventInstRule.setStatus("current")
_CfprEventInstSeverity_Type = CfprConditionSeverity
_CfprEventInstSeverity_Object = MibTableColumn
cfprEventInstSeverity = _CfprEventInstSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 11),
    _CfprEventInstSeverity_Type()
)
cfprEventInstSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventInstSeverity.setStatus("current")
_CfprEventInstTags_Type = CfprConditionTag
_CfprEventInstTags_Object = MibTableColumn
cfprEventInstTags = _CfprEventInstTags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 12),
    _CfprEventInstTags_Type()
)
cfprEventInstTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventInstTags.setStatus("current")
_CfprEventInstType_Type = CfprConditionType
_CfprEventInstType_Object = MibTableColumn
cfprEventInstType = _CfprEventInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 3, 1, 13),
    _CfprEventInstType_Type()
)
cfprEventInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventInstType.setStatus("current")
_CfprEventLogTable_Object = MibTable
cfprEventLogTable = _CfprEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 4)
)
if mibBuilder.loadTexts:
    cfprEventLogTable.setStatus("current")
_CfprEventLogEntry_Object = MibTableRow
cfprEventLogEntry = _CfprEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 4, 1)
)
cfprEventLogEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EVENT-MIB", "cfprEventLogInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEventLogEntry.setStatus("current")
_CfprEventLogInstanceId_Type = CfprManagedObjectId
_CfprEventLogInstanceId_Object = MibTableColumn
cfprEventLogInstanceId = _CfprEventLogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 4, 1, 1),
    _CfprEventLogInstanceId_Type()
)
cfprEventLogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEventLogInstanceId.setStatus("current")
_CfprEventLogDn_Type = CfprManagedObjectDn
_CfprEventLogDn_Object = MibTableColumn
cfprEventLogDn = _CfprEventLogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 4, 1, 2),
    _CfprEventLogDn_Type()
)
cfprEventLogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventLogDn.setStatus("current")
_CfprEventLogRn_Type = SnmpAdminString
_CfprEventLogRn_Object = MibTableColumn
cfprEventLogRn = _CfprEventLogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 4, 1, 3),
    _CfprEventLogRn_Type()
)
cfprEventLogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventLogRn.setStatus("current")
_CfprEventLogMaxSize_Type = Gauge32
_CfprEventLogMaxSize_Object = MibTableColumn
cfprEventLogMaxSize = _CfprEventLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 4, 1, 4),
    _CfprEventLogMaxSize_Type()
)
cfprEventLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventLogMaxSize.setStatus("current")
_CfprEventLogPurgeWindow_Type = Gauge32
_CfprEventLogPurgeWindow_Object = MibTableColumn
cfprEventLogPurgeWindow = _CfprEventLogPurgeWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 4, 1, 5),
    _CfprEventLogPurgeWindow_Type()
)
cfprEventLogPurgeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventLogPurgeWindow.setStatus("current")
_CfprEventLogSize_Type = Gauge32
_CfprEventLogSize_Object = MibTableColumn
cfprEventLogSize = _CfprEventLogSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 4, 1, 6),
    _CfprEventLogSize_Type()
)
cfprEventLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventLogSize.setStatus("current")
_CfprEventPolicyTable_Object = MibTable
cfprEventPolicyTable = _CfprEventPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 5)
)
if mibBuilder.loadTexts:
    cfprEventPolicyTable.setStatus("current")
_CfprEventPolicyEntry_Object = MibTableRow
cfprEventPolicyEntry = _CfprEventPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 5, 1)
)
cfprEventPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EVENT-MIB", "cfprEventPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEventPolicyEntry.setStatus("current")
_CfprEventPolicyInstanceId_Type = CfprManagedObjectId
_CfprEventPolicyInstanceId_Object = MibTableColumn
cfprEventPolicyInstanceId = _CfprEventPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 5, 1, 1),
    _CfprEventPolicyInstanceId_Type()
)
cfprEventPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEventPolicyInstanceId.setStatus("current")
_CfprEventPolicyDn_Type = CfprManagedObjectDn
_CfprEventPolicyDn_Object = MibTableColumn
cfprEventPolicyDn = _CfprEventPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 5, 1, 2),
    _CfprEventPolicyDn_Type()
)
cfprEventPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventPolicyDn.setStatus("current")
_CfprEventPolicyRn_Type = SnmpAdminString
_CfprEventPolicyRn_Object = MibTableColumn
cfprEventPolicyRn = _CfprEventPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 5, 1, 3),
    _CfprEventPolicyRn_Type()
)
cfprEventPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventPolicyRn.setStatus("current")
_CfprEventPolicyDescr_Type = SnmpAdminString
_CfprEventPolicyDescr_Object = MibTableColumn
cfprEventPolicyDescr = _CfprEventPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 5, 1, 4),
    _CfprEventPolicyDescr_Type()
)
cfprEventPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventPolicyDescr.setStatus("current")
_CfprEventPolicyIntId_Type = SnmpAdminString
_CfprEventPolicyIntId_Object = MibTableColumn
cfprEventPolicyIntId = _CfprEventPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 5, 1, 5),
    _CfprEventPolicyIntId_Type()
)
cfprEventPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventPolicyIntId.setStatus("current")
_CfprEventPolicyName_Type = SnmpAdminString
_CfprEventPolicyName_Object = MibTableColumn
cfprEventPolicyName = _CfprEventPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 5, 1, 6),
    _CfprEventPolicyName_Type()
)
cfprEventPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventPolicyName.setStatus("current")
_CfprEventPolicyPolicyLevel_Type = Gauge32
_CfprEventPolicyPolicyLevel_Object = MibTableColumn
cfprEventPolicyPolicyLevel = _CfprEventPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 5, 1, 7),
    _CfprEventPolicyPolicyLevel_Type()
)
cfprEventPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventPolicyPolicyLevel.setStatus("current")
_CfprEventPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprEventPolicyPolicyOwner_Object = MibTableColumn
cfprEventPolicyPolicyOwner = _CfprEventPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 5, 1, 8),
    _CfprEventPolicyPolicyOwner_Type()
)
cfprEventPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventPolicyPolicyOwner.setStatus("current")
_CfprEventPolicyRetentionInterval_Type = TimeIntervalSec
_CfprEventPolicyRetentionInterval_Object = MibTableColumn
cfprEventPolicyRetentionInterval = _CfprEventPolicyRetentionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 5, 1, 9),
    _CfprEventPolicyRetentionInterval_Type()
)
cfprEventPolicyRetentionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventPolicyRetentionInterval.setStatus("current")
_CfprEventPolicySizeLimit_Type = Gauge32
_CfprEventPolicySizeLimit_Object = MibTableColumn
cfprEventPolicySizeLimit = _CfprEventPolicySizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 5, 1, 10),
    _CfprEventPolicySizeLimit_Type()
)
cfprEventPolicySizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventPolicySizeLimit.setStatus("current")
_CfprEventRecordTable_Object = MibTable
cfprEventRecordTable = _CfprEventRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6)
)
if mibBuilder.loadTexts:
    cfprEventRecordTable.setStatus("current")
_CfprEventRecordEntry_Object = MibTableRow
cfprEventRecordEntry = _CfprEventRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1)
)
cfprEventRecordEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-EVENT-MIB", "cfprEventRecordInstanceId"),
)
if mibBuilder.loadTexts:
    cfprEventRecordEntry.setStatus("current")
_CfprEventRecordInstanceId_Type = CfprManagedObjectId
_CfprEventRecordInstanceId_Object = MibTableColumn
cfprEventRecordInstanceId = _CfprEventRecordInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 1),
    _CfprEventRecordInstanceId_Type()
)
cfprEventRecordInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprEventRecordInstanceId.setStatus("current")
_CfprEventRecordDn_Type = CfprManagedObjectDn
_CfprEventRecordDn_Object = MibTableColumn
cfprEventRecordDn = _CfprEventRecordDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 2),
    _CfprEventRecordDn_Type()
)
cfprEventRecordDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordDn.setStatus("current")
_CfprEventRecordRn_Type = SnmpAdminString
_CfprEventRecordRn_Object = MibTableColumn
cfprEventRecordRn = _CfprEventRecordRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 3),
    _CfprEventRecordRn_Type()
)
cfprEventRecordRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordRn.setStatus("current")
_CfprEventRecordAffected_Type = SnmpAdminString
_CfprEventRecordAffected_Object = MibTableColumn
cfprEventRecordAffected = _CfprEventRecordAffected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 4),
    _CfprEventRecordAffected_Type()
)
cfprEventRecordAffected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordAffected.setStatus("current")
_CfprEventRecordCause_Type = CfprConditionCause
_CfprEventRecordCause_Object = MibTableColumn
cfprEventRecordCause = _CfprEventRecordCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 5),
    _CfprEventRecordCause_Type()
)
cfprEventRecordCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordCause.setStatus("current")
_CfprEventRecordChangeSet_Type = SnmpAdminString
_CfprEventRecordChangeSet_Object = MibTableColumn
cfprEventRecordChangeSet = _CfprEventRecordChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 6),
    _CfprEventRecordChangeSet_Type()
)
cfprEventRecordChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordChangeSet.setStatus("current")
_CfprEventRecordCode_Type = CfprConditionCode
_CfprEventRecordCode_Object = MibTableColumn
cfprEventRecordCode = _CfprEventRecordCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 7),
    _CfprEventRecordCode_Type()
)
cfprEventRecordCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordCode.setStatus("current")
_CfprEventRecordCreated_Type = DateAndTime
_CfprEventRecordCreated_Object = MibTableColumn
cfprEventRecordCreated = _CfprEventRecordCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 8),
    _CfprEventRecordCreated_Type()
)
cfprEventRecordCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordCreated.setStatus("current")
_CfprEventRecordDescr_Type = SnmpAdminString
_CfprEventRecordDescr_Object = MibTableColumn
cfprEventRecordDescr = _CfprEventRecordDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 9),
    _CfprEventRecordDescr_Type()
)
cfprEventRecordDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordDescr.setStatus("current")
_CfprEventRecordId_Type = Gauge32
_CfprEventRecordId_Object = MibTableColumn
cfprEventRecordId = _CfprEventRecordId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 10),
    _CfprEventRecordId_Type()
)
cfprEventRecordId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordId.setStatus("current")
_CfprEventRecordInd_Type = CfprConditionActionIndicator
_CfprEventRecordInd_Object = MibTableColumn
cfprEventRecordInd = _CfprEventRecordInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 11),
    _CfprEventRecordInd_Type()
)
cfprEventRecordInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordInd.setStatus("current")
_CfprEventRecordSessionId_Type = SnmpAdminString
_CfprEventRecordSessionId_Object = MibTableColumn
cfprEventRecordSessionId = _CfprEventRecordSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 12),
    _CfprEventRecordSessionId_Type()
)
cfprEventRecordSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordSessionId.setStatus("current")
_CfprEventRecordSeverity_Type = CfprConditionSeverity
_CfprEventRecordSeverity_Object = MibTableColumn
cfprEventRecordSeverity = _CfprEventRecordSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 13),
    _CfprEventRecordSeverity_Type()
)
cfprEventRecordSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordSeverity.setStatus("current")
_CfprEventRecordTrig_Type = Gauge32
_CfprEventRecordTrig_Object = MibTableColumn
cfprEventRecordTrig = _CfprEventRecordTrig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 14),
    _CfprEventRecordTrig_Type()
)
cfprEventRecordTrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordTrig.setStatus("current")
_CfprEventRecordTxId_Type = Unsigned64
_CfprEventRecordTxId_Object = MibTableColumn
cfprEventRecordTxId = _CfprEventRecordTxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 15),
    _CfprEventRecordTxId_Type()
)
cfprEventRecordTxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordTxId.setStatus("current")
_CfprEventRecordUser_Type = SnmpAdminString
_CfprEventRecordUser_Object = MibTableColumn
cfprEventRecordUser = _CfprEventRecordUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 22, 6, 1, 16),
    _CfprEventRecordUser_Type()
)
cfprEventRecordUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprEventRecordUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-EVENT-MIB",
    **{"cfprEventObjects": cfprEventObjects,
       "cfprEventEpCtrlTable": cfprEventEpCtrlTable,
       "cfprEventEpCtrlEntry": cfprEventEpCtrlEntry,
       "cfprEventEpCtrlInstanceId": cfprEventEpCtrlInstanceId,
       "cfprEventEpCtrlDn": cfprEventEpCtrlDn,
       "cfprEventEpCtrlRn": cfprEventEpCtrlRn,
       "cfprEventEpCtrlLevel": cfprEventEpCtrlLevel,
       "cfprEventEpCtrlRevertTimeout": cfprEventEpCtrlRevertTimeout,
       "cfprEventHolderTable": cfprEventHolderTable,
       "cfprEventHolderEntry": cfprEventHolderEntry,
       "cfprEventHolderInstanceId": cfprEventHolderInstanceId,
       "cfprEventHolderDn": cfprEventHolderDn,
       "cfprEventHolderRn": cfprEventHolderRn,
       "cfprEventHolderName": cfprEventHolderName,
       "cfprEventInstTable": cfprEventInstTable,
       "cfprEventInstEntry": cfprEventInstEntry,
       "cfprEventInstInstanceId": cfprEventInstInstanceId,
       "cfprEventInstDn": cfprEventInstDn,
       "cfprEventInstRn": cfprEventInstRn,
       "cfprEventInstCause": cfprEventInstCause,
       "cfprEventInstChangeSet": cfprEventInstChangeSet,
       "cfprEventInstCode": cfprEventInstCode,
       "cfprEventInstCreated": cfprEventInstCreated,
       "cfprEventInstDescr": cfprEventInstDescr,
       "cfprEventInstId": cfprEventInstId,
       "cfprEventInstRule": cfprEventInstRule,
       "cfprEventInstSeverity": cfprEventInstSeverity,
       "cfprEventInstTags": cfprEventInstTags,
       "cfprEventInstType": cfprEventInstType,
       "cfprEventLogTable": cfprEventLogTable,
       "cfprEventLogEntry": cfprEventLogEntry,
       "cfprEventLogInstanceId": cfprEventLogInstanceId,
       "cfprEventLogDn": cfprEventLogDn,
       "cfprEventLogRn": cfprEventLogRn,
       "cfprEventLogMaxSize": cfprEventLogMaxSize,
       "cfprEventLogPurgeWindow": cfprEventLogPurgeWindow,
       "cfprEventLogSize": cfprEventLogSize,
       "cfprEventPolicyTable": cfprEventPolicyTable,
       "cfprEventPolicyEntry": cfprEventPolicyEntry,
       "cfprEventPolicyInstanceId": cfprEventPolicyInstanceId,
       "cfprEventPolicyDn": cfprEventPolicyDn,
       "cfprEventPolicyRn": cfprEventPolicyRn,
       "cfprEventPolicyDescr": cfprEventPolicyDescr,
       "cfprEventPolicyIntId": cfprEventPolicyIntId,
       "cfprEventPolicyName": cfprEventPolicyName,
       "cfprEventPolicyPolicyLevel": cfprEventPolicyPolicyLevel,
       "cfprEventPolicyPolicyOwner": cfprEventPolicyPolicyOwner,
       "cfprEventPolicyRetentionInterval": cfprEventPolicyRetentionInterval,
       "cfprEventPolicySizeLimit": cfprEventPolicySizeLimit,
       "cfprEventRecordTable": cfprEventRecordTable,
       "cfprEventRecordEntry": cfprEventRecordEntry,
       "cfprEventRecordInstanceId": cfprEventRecordInstanceId,
       "cfprEventRecordDn": cfprEventRecordDn,
       "cfprEventRecordRn": cfprEventRecordRn,
       "cfprEventRecordAffected": cfprEventRecordAffected,
       "cfprEventRecordCause": cfprEventRecordCause,
       "cfprEventRecordChangeSet": cfprEventRecordChangeSet,
       "cfprEventRecordCode": cfprEventRecordCode,
       "cfprEventRecordCreated": cfprEventRecordCreated,
       "cfprEventRecordDescr": cfprEventRecordDescr,
       "cfprEventRecordId": cfprEventRecordId,
       "cfprEventRecordInd": cfprEventRecordInd,
       "cfprEventRecordSessionId": cfprEventRecordSessionId,
       "cfprEventRecordSeverity": cfprEventRecordSeverity,
       "cfprEventRecordTrig": cfprEventRecordTrig,
       "cfprEventRecordTxId": cfprEventRecordTxId,
       "cfprEventRecordUser": cfprEventRecordUser}
)
