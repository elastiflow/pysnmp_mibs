# SNMP MIB module (CISCO-FIREPOWER-FAULT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-FAULT-MIB.mib
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

(CfprConditionAckAction,
 CfprConditionCause,
 CfprConditionCode,
 CfprConditionLifecycle,
 CfprConditionRule,
 CfprConditionSeverity,
 CfprConditionTag,
 CfprConditionType,
 CfprFaultBasePolicyClearAction,
 CfprFaultBasePolicySoakingSeverity,
 CfprMoMoClassId,
 CfprPolicyPolicyOwner,
 CfprTrigAdminState,
 CfprTrigTrigOperState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionAckAction",
    "CfprConditionCause",
    "CfprConditionCode",
    "CfprConditionLifecycle",
    "CfprConditionRule",
    "CfprConditionSeverity",
    "CfprConditionTag",
    "CfprConditionType",
    "CfprFaultBasePolicyClearAction",
    "CfprFaultBasePolicySoakingSeverity",
    "CfprMoMoClassId",
    "CfprPolicyPolicyOwner",
    "CfprTrigAdminState",
    "CfprTrigTrigOperState")

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

cfprFaultObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprFaultInstTable_Object = MibTable
cfprFaultInstTable = _CfprFaultInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfprFaultInstTable.setStatus("current")
_CfprFaultInstEntry_Object = MibTableRow
cfprFaultInstEntry = _CfprFaultInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1)
)
cfprFaultInstEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FAULT-MIB", "cfprFaultInstInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFaultInstEntry.setStatus("current")
_CfprFaultInstInstanceId_Type = CfprManagedObjectId
_CfprFaultInstInstanceId_Object = MibTableColumn
cfprFaultInstInstanceId = _CfprFaultInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 1),
    _CfprFaultInstInstanceId_Type()
)
cfprFaultInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFaultInstInstanceId.setStatus("current")
_CfprFaultInstDn_Type = CfprManagedObjectDn
_CfprFaultInstDn_Object = MibTableColumn
cfprFaultInstDn = _CfprFaultInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 2),
    _CfprFaultInstDn_Type()
)
cfprFaultInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstDn.setStatus("current")
_CfprFaultInstRn_Type = SnmpAdminString
_CfprFaultInstRn_Object = MibTableColumn
cfprFaultInstRn = _CfprFaultInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 3),
    _CfprFaultInstRn_Type()
)
cfprFaultInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstRn.setStatus("current")
_CfprFaultInstAffectedObjectId_Type = RowPointer
_CfprFaultInstAffectedObjectId_Object = MibTableColumn
cfprFaultInstAffectedObjectId = _CfprFaultInstAffectedObjectId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 4),
    _CfprFaultInstAffectedObjectId_Type()
)
cfprFaultInstAffectedObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstAffectedObjectId.setStatus("current")
_CfprFaultInstAffectedObjectDn_Type = CfprManagedObjectDn
_CfprFaultInstAffectedObjectDn_Object = MibTableColumn
cfprFaultInstAffectedObjectDn = _CfprFaultInstAffectedObjectDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 5),
    _CfprFaultInstAffectedObjectDn_Type()
)
cfprFaultInstAffectedObjectDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstAffectedObjectDn.setStatus("current")
_CfprFaultInstAck_Type = TruthValue
_CfprFaultInstAck_Object = MibTableColumn
cfprFaultInstAck = _CfprFaultInstAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 6),
    _CfprFaultInstAck_Type()
)
cfprFaultInstAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstAck.setStatus("current")
_CfprFaultInstCause_Type = CfprConditionCause
_CfprFaultInstCause_Object = MibTableColumn
cfprFaultInstCause = _CfprFaultInstCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 7),
    _CfprFaultInstCause_Type()
)
cfprFaultInstCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstCause.setStatus("current")
_CfprFaultInstChangeSet_Type = SnmpAdminString
_CfprFaultInstChangeSet_Object = MibTableColumn
cfprFaultInstChangeSet = _CfprFaultInstChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 8),
    _CfprFaultInstChangeSet_Type()
)
cfprFaultInstChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstChangeSet.setStatus("current")
_CfprFaultInstCode_Type = CfprConditionCode
_CfprFaultInstCode_Object = MibTableColumn
cfprFaultInstCode = _CfprFaultInstCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 9),
    _CfprFaultInstCode_Type()
)
cfprFaultInstCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstCode.setStatus("current")
_CfprFaultInstCreated_Type = DateAndTime
_CfprFaultInstCreated_Object = MibTableColumn
cfprFaultInstCreated = _CfprFaultInstCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 10),
    _CfprFaultInstCreated_Type()
)
cfprFaultInstCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstCreated.setStatus("current")
_CfprFaultInstDescr_Type = SnmpAdminString
_CfprFaultInstDescr_Object = MibTableColumn
cfprFaultInstDescr = _CfprFaultInstDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 11),
    _CfprFaultInstDescr_Type()
)
cfprFaultInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstDescr.setStatus("current")
_CfprFaultInstHighestSeverity_Type = CfprConditionSeverity
_CfprFaultInstHighestSeverity_Object = MibTableColumn
cfprFaultInstHighestSeverity = _CfprFaultInstHighestSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 12),
    _CfprFaultInstHighestSeverity_Type()
)
cfprFaultInstHighestSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstHighestSeverity.setStatus("current")
_CfprFaultInstId_Type = Unsigned64
_CfprFaultInstId_Object = MibTableColumn
cfprFaultInstId = _CfprFaultInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 13),
    _CfprFaultInstId_Type()
)
cfprFaultInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstId.setStatus("current")
_CfprFaultInstLastTransition_Type = DateAndTime
_CfprFaultInstLastTransition_Object = MibTableColumn
cfprFaultInstLastTransition = _CfprFaultInstLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 14),
    _CfprFaultInstLastTransition_Type()
)
cfprFaultInstLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstLastTransition.setStatus("current")
_CfprFaultInstLc_Type = CfprConditionLifecycle
_CfprFaultInstLc_Object = MibTableColumn
cfprFaultInstLc = _CfprFaultInstLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 15),
    _CfprFaultInstLc_Type()
)
cfprFaultInstLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstLc.setStatus("current")
_CfprFaultInstOccur_Type = Gauge32
_CfprFaultInstOccur_Object = MibTableColumn
cfprFaultInstOccur = _CfprFaultInstOccur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 16),
    _CfprFaultInstOccur_Type()
)
cfprFaultInstOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstOccur.setStatus("current")
_CfprFaultInstOrigSeverity_Type = CfprConditionSeverity
_CfprFaultInstOrigSeverity_Object = MibTableColumn
cfprFaultInstOrigSeverity = _CfprFaultInstOrigSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 17),
    _CfprFaultInstOrigSeverity_Type()
)
cfprFaultInstOrigSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstOrigSeverity.setStatus("current")
_CfprFaultInstPrevSeverity_Type = CfprConditionSeverity
_CfprFaultInstPrevSeverity_Object = MibTableColumn
cfprFaultInstPrevSeverity = _CfprFaultInstPrevSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 18),
    _CfprFaultInstPrevSeverity_Type()
)
cfprFaultInstPrevSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstPrevSeverity.setStatus("current")
_CfprFaultInstRule_Type = CfprConditionRule
_CfprFaultInstRule_Object = MibTableColumn
cfprFaultInstRule = _CfprFaultInstRule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 19),
    _CfprFaultInstRule_Type()
)
cfprFaultInstRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstRule.setStatus("current")
_CfprFaultInstSeverity_Type = CfprConditionSeverity
_CfprFaultInstSeverity_Object = MibTableColumn
cfprFaultInstSeverity = _CfprFaultInstSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 20),
    _CfprFaultInstSeverity_Type()
)
cfprFaultInstSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstSeverity.setStatus("current")
_CfprFaultInstTags_Type = CfprConditionTag
_CfprFaultInstTags_Object = MibTableColumn
cfprFaultInstTags = _CfprFaultInstTags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 21),
    _CfprFaultInstTags_Type()
)
cfprFaultInstTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstTags.setStatus("current")
_CfprFaultInstType_Type = CfprConditionType
_CfprFaultInstType_Object = MibTableColumn
cfprFaultInstType = _CfprFaultInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 1, 1, 22),
    _CfprFaultInstType_Type()
)
cfprFaultInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultInstType.setStatus("current")
_CfprFaultAffectedClassTable_Object = MibTable
cfprFaultAffectedClassTable = _CfprFaultAffectedClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cfprFaultAffectedClassTable.setStatus("current")
_CfprFaultAffectedClassEntry_Object = MibTableRow
cfprFaultAffectedClassEntry = _CfprFaultAffectedClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 2, 1)
)
cfprFaultAffectedClassEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FAULT-MIB", "cfprFaultAffectedClassInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFaultAffectedClassEntry.setStatus("current")
_CfprFaultAffectedClassInstanceId_Type = CfprManagedObjectId
_CfprFaultAffectedClassInstanceId_Object = MibTableColumn
cfprFaultAffectedClassInstanceId = _CfprFaultAffectedClassInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 2, 1, 1),
    _CfprFaultAffectedClassInstanceId_Type()
)
cfprFaultAffectedClassInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFaultAffectedClassInstanceId.setStatus("current")
_CfprFaultAffectedClassDn_Type = CfprManagedObjectDn
_CfprFaultAffectedClassDn_Object = MibTableColumn
cfprFaultAffectedClassDn = _CfprFaultAffectedClassDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 2, 1, 2),
    _CfprFaultAffectedClassDn_Type()
)
cfprFaultAffectedClassDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultAffectedClassDn.setStatus("current")
_CfprFaultAffectedClassRn_Type = SnmpAdminString
_CfprFaultAffectedClassRn_Object = MibTableColumn
cfprFaultAffectedClassRn = _CfprFaultAffectedClassRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 2, 1, 3),
    _CfprFaultAffectedClassRn_Type()
)
cfprFaultAffectedClassRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultAffectedClassRn.setStatus("current")
_CfprFaultAffectedClassMoClassId_Type = CfprMoMoClassId
_CfprFaultAffectedClassMoClassId_Object = MibTableColumn
cfprFaultAffectedClassMoClassId = _CfprFaultAffectedClassMoClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 2, 1, 4),
    _CfprFaultAffectedClassMoClassId_Type()
)
cfprFaultAffectedClassMoClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultAffectedClassMoClassId.setStatus("current")
_CfprFaultHolderTable_Object = MibTable
cfprFaultHolderTable = _CfprFaultHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfprFaultHolderTable.setStatus("current")
_CfprFaultHolderEntry_Object = MibTableRow
cfprFaultHolderEntry = _CfprFaultHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 3, 1)
)
cfprFaultHolderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FAULT-MIB", "cfprFaultHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFaultHolderEntry.setStatus("current")
_CfprFaultHolderInstanceId_Type = CfprManagedObjectId
_CfprFaultHolderInstanceId_Object = MibTableColumn
cfprFaultHolderInstanceId = _CfprFaultHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 3, 1, 1),
    _CfprFaultHolderInstanceId_Type()
)
cfprFaultHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFaultHolderInstanceId.setStatus("current")
_CfprFaultHolderDn_Type = CfprManagedObjectDn
_CfprFaultHolderDn_Object = MibTableColumn
cfprFaultHolderDn = _CfprFaultHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 3, 1, 2),
    _CfprFaultHolderDn_Type()
)
cfprFaultHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultHolderDn.setStatus("current")
_CfprFaultHolderRn_Type = SnmpAdminString
_CfprFaultHolderRn_Object = MibTableColumn
cfprFaultHolderRn = _CfprFaultHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 3, 1, 3),
    _CfprFaultHolderRn_Type()
)
cfprFaultHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultHolderRn.setStatus("current")
_CfprFaultHolderName_Type = SnmpAdminString
_CfprFaultHolderName_Object = MibTableColumn
cfprFaultHolderName = _CfprFaultHolderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 3, 1, 4),
    _CfprFaultHolderName_Type()
)
cfprFaultHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultHolderName.setStatus("current")
_CfprFaultHolderTotalFaults_Type = Unsigned64
_CfprFaultHolderTotalFaults_Object = MibTableColumn
cfprFaultHolderTotalFaults = _CfprFaultHolderTotalFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 3, 1, 5),
    _CfprFaultHolderTotalFaults_Type()
)
cfprFaultHolderTotalFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultHolderTotalFaults.setStatus("current")
_CfprFaultLocalTypedHolderTable_Object = MibTable
cfprFaultLocalTypedHolderTable = _CfprFaultLocalTypedHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cfprFaultLocalTypedHolderTable.setStatus("current")
_CfprFaultLocalTypedHolderEntry_Object = MibTableRow
cfprFaultLocalTypedHolderEntry = _CfprFaultLocalTypedHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 4, 1)
)
cfprFaultLocalTypedHolderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FAULT-MIB", "cfprFaultLocalTypedHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFaultLocalTypedHolderEntry.setStatus("current")
_CfprFaultLocalTypedHolderInstanceId_Type = CfprManagedObjectId
_CfprFaultLocalTypedHolderInstanceId_Object = MibTableColumn
cfprFaultLocalTypedHolderInstanceId = _CfprFaultLocalTypedHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 4, 1, 1),
    _CfprFaultLocalTypedHolderInstanceId_Type()
)
cfprFaultLocalTypedHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFaultLocalTypedHolderInstanceId.setStatus("current")
_CfprFaultLocalTypedHolderDn_Type = CfprManagedObjectDn
_CfprFaultLocalTypedHolderDn_Object = MibTableColumn
cfprFaultLocalTypedHolderDn = _CfprFaultLocalTypedHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 4, 1, 2),
    _CfprFaultLocalTypedHolderDn_Type()
)
cfprFaultLocalTypedHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultLocalTypedHolderDn.setStatus("current")
_CfprFaultLocalTypedHolderRn_Type = SnmpAdminString
_CfprFaultLocalTypedHolderRn_Object = MibTableColumn
cfprFaultLocalTypedHolderRn = _CfprFaultLocalTypedHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 4, 1, 3),
    _CfprFaultLocalTypedHolderRn_Type()
)
cfprFaultLocalTypedHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultLocalTypedHolderRn.setStatus("current")
_CfprFaultLocalTypedHolderName_Type = SnmpAdminString
_CfprFaultLocalTypedHolderName_Object = MibTableColumn
cfprFaultLocalTypedHolderName = _CfprFaultLocalTypedHolderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 4, 1, 4),
    _CfprFaultLocalTypedHolderName_Type()
)
cfprFaultLocalTypedHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultLocalTypedHolderName.setStatus("current")
_CfprFaultLocalTypedHolderTotalFaults_Type = Unsigned64
_CfprFaultLocalTypedHolderTotalFaults_Object = MibTableColumn
cfprFaultLocalTypedHolderTotalFaults = _CfprFaultLocalTypedHolderTotalFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 4, 1, 5),
    _CfprFaultLocalTypedHolderTotalFaults_Type()
)
cfprFaultLocalTypedHolderTotalFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultLocalTypedHolderTotalFaults.setStatus("current")
_CfprFaultLocalTypedHolderType_Type = CfprConditionType
_CfprFaultLocalTypedHolderType_Object = MibTableColumn
cfprFaultLocalTypedHolderType = _CfprFaultLocalTypedHolderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 4, 1, 6),
    _CfprFaultLocalTypedHolderType_Type()
)
cfprFaultLocalTypedHolderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultLocalTypedHolderType.setStatus("current")
_CfprFaultPolicyTable_Object = MibTable
cfprFaultPolicyTable = _CfprFaultPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cfprFaultPolicyTable.setStatus("current")
_CfprFaultPolicyEntry_Object = MibTableRow
cfprFaultPolicyEntry = _CfprFaultPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1)
)
cfprFaultPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FAULT-MIB", "cfprFaultPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFaultPolicyEntry.setStatus("current")
_CfprFaultPolicyInstanceId_Type = CfprManagedObjectId
_CfprFaultPolicyInstanceId_Object = MibTableColumn
cfprFaultPolicyInstanceId = _CfprFaultPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 1),
    _CfprFaultPolicyInstanceId_Type()
)
cfprFaultPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFaultPolicyInstanceId.setStatus("current")
_CfprFaultPolicyDn_Type = CfprManagedObjectDn
_CfprFaultPolicyDn_Object = MibTableColumn
cfprFaultPolicyDn = _CfprFaultPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 2),
    _CfprFaultPolicyDn_Type()
)
cfprFaultPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicyDn.setStatus("current")
_CfprFaultPolicyRn_Type = SnmpAdminString
_CfprFaultPolicyRn_Object = MibTableColumn
cfprFaultPolicyRn = _CfprFaultPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 3),
    _CfprFaultPolicyRn_Type()
)
cfprFaultPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicyRn.setStatus("current")
_CfprFaultPolicyAckAction_Type = CfprConditionAckAction
_CfprFaultPolicyAckAction_Object = MibTableColumn
cfprFaultPolicyAckAction = _CfprFaultPolicyAckAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 4),
    _CfprFaultPolicyAckAction_Type()
)
cfprFaultPolicyAckAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicyAckAction.setStatus("current")
_CfprFaultPolicyClearAction_Type = CfprFaultBasePolicyClearAction
_CfprFaultPolicyClearAction_Object = MibTableColumn
cfprFaultPolicyClearAction = _CfprFaultPolicyClearAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 5),
    _CfprFaultPolicyClearAction_Type()
)
cfprFaultPolicyClearAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicyClearAction.setStatus("current")
_CfprFaultPolicyClearInterval_Type = TimeIntervalSec
_CfprFaultPolicyClearInterval_Object = MibTableColumn
cfprFaultPolicyClearInterval = _CfprFaultPolicyClearInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 6),
    _CfprFaultPolicyClearInterval_Type()
)
cfprFaultPolicyClearInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicyClearInterval.setStatus("current")
_CfprFaultPolicyDescr_Type = SnmpAdminString
_CfprFaultPolicyDescr_Object = MibTableColumn
cfprFaultPolicyDescr = _CfprFaultPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 7),
    _CfprFaultPolicyDescr_Type()
)
cfprFaultPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicyDescr.setStatus("current")
_CfprFaultPolicyFlapInterval_Type = Unsigned64
_CfprFaultPolicyFlapInterval_Object = MibTableColumn
cfprFaultPolicyFlapInterval = _CfprFaultPolicyFlapInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 8),
    _CfprFaultPolicyFlapInterval_Type()
)
cfprFaultPolicyFlapInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicyFlapInterval.setStatus("current")
_CfprFaultPolicyIntId_Type = SnmpAdminString
_CfprFaultPolicyIntId_Object = MibTableColumn
cfprFaultPolicyIntId = _CfprFaultPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 9),
    _CfprFaultPolicyIntId_Type()
)
cfprFaultPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicyIntId.setStatus("current")
_CfprFaultPolicyName_Type = SnmpAdminString
_CfprFaultPolicyName_Object = MibTableColumn
cfprFaultPolicyName = _CfprFaultPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 10),
    _CfprFaultPolicyName_Type()
)
cfprFaultPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicyName.setStatus("current")
_CfprFaultPolicyPolicyLevel_Type = Gauge32
_CfprFaultPolicyPolicyLevel_Object = MibTableColumn
cfprFaultPolicyPolicyLevel = _CfprFaultPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 11),
    _CfprFaultPolicyPolicyLevel_Type()
)
cfprFaultPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicyPolicyLevel.setStatus("current")
_CfprFaultPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFaultPolicyPolicyOwner_Object = MibTableColumn
cfprFaultPolicyPolicyOwner = _CfprFaultPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 12),
    _CfprFaultPolicyPolicyOwner_Type()
)
cfprFaultPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicyPolicyOwner.setStatus("current")
_CfprFaultPolicyRetentionInterval_Type = TimeIntervalSec
_CfprFaultPolicyRetentionInterval_Object = MibTableColumn
cfprFaultPolicyRetentionInterval = _CfprFaultPolicyRetentionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 13),
    _CfprFaultPolicyRetentionInterval_Type()
)
cfprFaultPolicyRetentionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicyRetentionInterval.setStatus("current")
_CfprFaultPolicySizeLimit_Type = Gauge32
_CfprFaultPolicySizeLimit_Object = MibTableColumn
cfprFaultPolicySizeLimit = _CfprFaultPolicySizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 14),
    _CfprFaultPolicySizeLimit_Type()
)
cfprFaultPolicySizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicySizeLimit.setStatus("current")
_CfprFaultPolicySoakInterval_Type = TimeIntervalSec
_CfprFaultPolicySoakInterval_Object = MibTableColumn
cfprFaultPolicySoakInterval = _CfprFaultPolicySoakInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 15),
    _CfprFaultPolicySoakInterval_Type()
)
cfprFaultPolicySoakInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicySoakInterval.setStatus("current")
_CfprFaultPolicySoakingSeverity_Type = CfprFaultBasePolicySoakingSeverity
_CfprFaultPolicySoakingSeverity_Object = MibTableColumn
cfprFaultPolicySoakingSeverity = _CfprFaultPolicySoakingSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 5, 1, 16),
    _CfprFaultPolicySoakingSeverity_Type()
)
cfprFaultPolicySoakingSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultPolicySoakingSeverity.setStatus("current")
_CfprFaultSuppressPolicyTable_Object = MibTable
cfprFaultSuppressPolicyTable = _CfprFaultSuppressPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyTable.setStatus("current")
_CfprFaultSuppressPolicyEntry_Object = MibTableRow
cfprFaultSuppressPolicyEntry = _CfprFaultSuppressPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 6, 1)
)
cfprFaultSuppressPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FAULT-MIB", "cfprFaultSuppressPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyEntry.setStatus("current")
_CfprFaultSuppressPolicyInstanceId_Type = CfprManagedObjectId
_CfprFaultSuppressPolicyInstanceId_Object = MibTableColumn
cfprFaultSuppressPolicyInstanceId = _CfprFaultSuppressPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 6, 1, 1),
    _CfprFaultSuppressPolicyInstanceId_Type()
)
cfprFaultSuppressPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyInstanceId.setStatus("current")
_CfprFaultSuppressPolicyDn_Type = CfprManagedObjectDn
_CfprFaultSuppressPolicyDn_Object = MibTableColumn
cfprFaultSuppressPolicyDn = _CfprFaultSuppressPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 6, 1, 2),
    _CfprFaultSuppressPolicyDn_Type()
)
cfprFaultSuppressPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyDn.setStatus("current")
_CfprFaultSuppressPolicyRn_Type = SnmpAdminString
_CfprFaultSuppressPolicyRn_Object = MibTableColumn
cfprFaultSuppressPolicyRn = _CfprFaultSuppressPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 6, 1, 3),
    _CfprFaultSuppressPolicyRn_Type()
)
cfprFaultSuppressPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyRn.setStatus("current")
_CfprFaultSuppressPolicyDescr_Type = SnmpAdminString
_CfprFaultSuppressPolicyDescr_Object = MibTableColumn
cfprFaultSuppressPolicyDescr = _CfprFaultSuppressPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 6, 1, 4),
    _CfprFaultSuppressPolicyDescr_Type()
)
cfprFaultSuppressPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyDescr.setStatus("current")
_CfprFaultSuppressPolicyIntId_Type = SnmpAdminString
_CfprFaultSuppressPolicyIntId_Object = MibTableColumn
cfprFaultSuppressPolicyIntId = _CfprFaultSuppressPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 6, 1, 5),
    _CfprFaultSuppressPolicyIntId_Type()
)
cfprFaultSuppressPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyIntId.setStatus("current")
_CfprFaultSuppressPolicyName_Type = SnmpAdminString
_CfprFaultSuppressPolicyName_Object = MibTableColumn
cfprFaultSuppressPolicyName = _CfprFaultSuppressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 6, 1, 6),
    _CfprFaultSuppressPolicyName_Type()
)
cfprFaultSuppressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyName.setStatus("current")
_CfprFaultSuppressPolicyPolicyLevel_Type = Gauge32
_CfprFaultSuppressPolicyPolicyLevel_Object = MibTableColumn
cfprFaultSuppressPolicyPolicyLevel = _CfprFaultSuppressPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 6, 1, 7),
    _CfprFaultSuppressPolicyPolicyLevel_Type()
)
cfprFaultSuppressPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyPolicyLevel.setStatus("current")
_CfprFaultSuppressPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFaultSuppressPolicyPolicyOwner_Object = MibTableColumn
cfprFaultSuppressPolicyPolicyOwner = _CfprFaultSuppressPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 6, 1, 8),
    _CfprFaultSuppressPolicyPolicyOwner_Type()
)
cfprFaultSuppressPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyPolicyOwner.setStatus("current")
_CfprFaultSuppressPolicyItemTable_Object = MibTable
cfprFaultSuppressPolicyItemTable = _CfprFaultSuppressPolicyItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyItemTable.setStatus("current")
_CfprFaultSuppressPolicyItemEntry_Object = MibTableRow
cfprFaultSuppressPolicyItemEntry = _CfprFaultSuppressPolicyItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 7, 1)
)
cfprFaultSuppressPolicyItemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FAULT-MIB", "cfprFaultSuppressPolicyItemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyItemEntry.setStatus("current")
_CfprFaultSuppressPolicyItemInstanceId_Type = CfprManagedObjectId
_CfprFaultSuppressPolicyItemInstanceId_Object = MibTableColumn
cfprFaultSuppressPolicyItemInstanceId = _CfprFaultSuppressPolicyItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 7, 1, 1),
    _CfprFaultSuppressPolicyItemInstanceId_Type()
)
cfprFaultSuppressPolicyItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyItemInstanceId.setStatus("current")
_CfprFaultSuppressPolicyItemDn_Type = CfprManagedObjectDn
_CfprFaultSuppressPolicyItemDn_Object = MibTableColumn
cfprFaultSuppressPolicyItemDn = _CfprFaultSuppressPolicyItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 7, 1, 2),
    _CfprFaultSuppressPolicyItemDn_Type()
)
cfprFaultSuppressPolicyItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyItemDn.setStatus("current")
_CfprFaultSuppressPolicyItemRn_Type = SnmpAdminString
_CfprFaultSuppressPolicyItemRn_Object = MibTableColumn
cfprFaultSuppressPolicyItemRn = _CfprFaultSuppressPolicyItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 7, 1, 3),
    _CfprFaultSuppressPolicyItemRn_Type()
)
cfprFaultSuppressPolicyItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyItemRn.setStatus("current")
_CfprFaultSuppressPolicyItemCause_Type = CfprConditionCause
_CfprFaultSuppressPolicyItemCause_Object = MibTableColumn
cfprFaultSuppressPolicyItemCause = _CfprFaultSuppressPolicyItemCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 7, 1, 4),
    _CfprFaultSuppressPolicyItemCause_Type()
)
cfprFaultSuppressPolicyItemCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyItemCause.setStatus("current")
_CfprFaultSuppressPolicyItemDescr_Type = SnmpAdminString
_CfprFaultSuppressPolicyItemDescr_Object = MibTableColumn
cfprFaultSuppressPolicyItemDescr = _CfprFaultSuppressPolicyItemDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 7, 1, 5),
    _CfprFaultSuppressPolicyItemDescr_Type()
)
cfprFaultSuppressPolicyItemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyItemDescr.setStatus("current")
_CfprFaultSuppressPolicyItemType_Type = CfprConditionType
_CfprFaultSuppressPolicyItemType_Object = MibTableColumn
cfprFaultSuppressPolicyItemType = _CfprFaultSuppressPolicyItemType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 7, 1, 6),
    _CfprFaultSuppressPolicyItemType_Type()
)
cfprFaultSuppressPolicyItemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressPolicyItemType.setStatus("current")
_CfprFaultSuppressTaskTable_Object = MibTable
cfprFaultSuppressTaskTable = _CfprFaultSuppressTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskTable.setStatus("current")
_CfprFaultSuppressTaskEntry_Object = MibTableRow
cfprFaultSuppressTaskEntry = _CfprFaultSuppressTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1)
)
cfprFaultSuppressTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FAULT-MIB", "cfprFaultSuppressTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskEntry.setStatus("current")
_CfprFaultSuppressTaskInstanceId_Type = CfprManagedObjectId
_CfprFaultSuppressTaskInstanceId_Object = MibTableColumn
cfprFaultSuppressTaskInstanceId = _CfprFaultSuppressTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 1),
    _CfprFaultSuppressTaskInstanceId_Type()
)
cfprFaultSuppressTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskInstanceId.setStatus("current")
_CfprFaultSuppressTaskDn_Type = CfprManagedObjectDn
_CfprFaultSuppressTaskDn_Object = MibTableColumn
cfprFaultSuppressTaskDn = _CfprFaultSuppressTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 2),
    _CfprFaultSuppressTaskDn_Type()
)
cfprFaultSuppressTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskDn.setStatus("current")
_CfprFaultSuppressTaskRn_Type = SnmpAdminString
_CfprFaultSuppressTaskRn_Object = MibTableColumn
cfprFaultSuppressTaskRn = _CfprFaultSuppressTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 3),
    _CfprFaultSuppressTaskRn_Type()
)
cfprFaultSuppressTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskRn.setStatus("current")
_CfprFaultSuppressTaskAdminState_Type = CfprTrigAdminState
_CfprFaultSuppressTaskAdminState_Object = MibTableColumn
cfprFaultSuppressTaskAdminState = _CfprFaultSuppressTaskAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 4),
    _CfprFaultSuppressTaskAdminState_Type()
)
cfprFaultSuppressTaskAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskAdminState.setStatus("current")
_CfprFaultSuppressTaskAutoDelete_Type = TruthValue
_CfprFaultSuppressTaskAutoDelete_Object = MibTableColumn
cfprFaultSuppressTaskAutoDelete = _CfprFaultSuppressTaskAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 5),
    _CfprFaultSuppressTaskAutoDelete_Type()
)
cfprFaultSuppressTaskAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskAutoDelete.setStatus("current")
_CfprFaultSuppressTaskDescr_Type = SnmpAdminString
_CfprFaultSuppressTaskDescr_Object = MibTableColumn
cfprFaultSuppressTaskDescr = _CfprFaultSuppressTaskDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 6),
    _CfprFaultSuppressTaskDescr_Type()
)
cfprFaultSuppressTaskDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskDescr.setStatus("current")
_CfprFaultSuppressTaskIgnoreCap_Type = TruthValue
_CfprFaultSuppressTaskIgnoreCap_Object = MibTableColumn
cfprFaultSuppressTaskIgnoreCap = _CfprFaultSuppressTaskIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 7),
    _CfprFaultSuppressTaskIgnoreCap_Type()
)
cfprFaultSuppressTaskIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskIgnoreCap.setStatus("current")
_CfprFaultSuppressTaskIntId_Type = SnmpAdminString
_CfprFaultSuppressTaskIntId_Object = MibTableColumn
cfprFaultSuppressTaskIntId = _CfprFaultSuppressTaskIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 8),
    _CfprFaultSuppressTaskIntId_Type()
)
cfprFaultSuppressTaskIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskIntId.setStatus("current")
_CfprFaultSuppressTaskName_Type = SnmpAdminString
_CfprFaultSuppressTaskName_Object = MibTableColumn
cfprFaultSuppressTaskName = _CfprFaultSuppressTaskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 9),
    _CfprFaultSuppressTaskName_Type()
)
cfprFaultSuppressTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskName.setStatus("current")
_CfprFaultSuppressTaskOperScheduler_Type = SnmpAdminString
_CfprFaultSuppressTaskOperScheduler_Object = MibTableColumn
cfprFaultSuppressTaskOperScheduler = _CfprFaultSuppressTaskOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 10),
    _CfprFaultSuppressTaskOperScheduler_Type()
)
cfprFaultSuppressTaskOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskOperScheduler.setStatus("current")
_CfprFaultSuppressTaskOperState_Type = CfprTrigTrigOperState
_CfprFaultSuppressTaskOperState_Object = MibTableColumn
cfprFaultSuppressTaskOperState = _CfprFaultSuppressTaskOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 11),
    _CfprFaultSuppressTaskOperState_Type()
)
cfprFaultSuppressTaskOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskOperState.setStatus("current")
_CfprFaultSuppressTaskOperSuppressPolicyName_Type = SnmpAdminString
_CfprFaultSuppressTaskOperSuppressPolicyName_Object = MibTableColumn
cfprFaultSuppressTaskOperSuppressPolicyName = _CfprFaultSuppressTaskOperSuppressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 12),
    _CfprFaultSuppressTaskOperSuppressPolicyName_Type()
)
cfprFaultSuppressTaskOperSuppressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskOperSuppressPolicyName.setStatus("current")
_CfprFaultSuppressTaskPolicyLevel_Type = Gauge32
_CfprFaultSuppressTaskPolicyLevel_Object = MibTableColumn
cfprFaultSuppressTaskPolicyLevel = _CfprFaultSuppressTaskPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 13),
    _CfprFaultSuppressTaskPolicyLevel_Type()
)
cfprFaultSuppressTaskPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskPolicyLevel.setStatus("current")
_CfprFaultSuppressTaskPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFaultSuppressTaskPolicyOwner_Object = MibTableColumn
cfprFaultSuppressTaskPolicyOwner = _CfprFaultSuppressTaskPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 14),
    _CfprFaultSuppressTaskPolicyOwner_Type()
)
cfprFaultSuppressTaskPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskPolicyOwner.setStatus("current")
_CfprFaultSuppressTaskScheduler_Type = SnmpAdminString
_CfprFaultSuppressTaskScheduler_Object = MibTableColumn
cfprFaultSuppressTaskScheduler = _CfprFaultSuppressTaskScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 15),
    _CfprFaultSuppressTaskScheduler_Type()
)
cfprFaultSuppressTaskScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskScheduler.setStatus("current")
_CfprFaultSuppressTaskSuppressPolicyName_Type = SnmpAdminString
_CfprFaultSuppressTaskSuppressPolicyName_Object = MibTableColumn
cfprFaultSuppressTaskSuppressPolicyName = _CfprFaultSuppressTaskSuppressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 1, 8, 1, 16),
    _CfprFaultSuppressTaskSuppressPolicyName_Type()
)
cfprFaultSuppressTaskSuppressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFaultSuppressTaskSuppressPolicyName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-FAULT-MIB",
    **{"cfprFaultObjects": cfprFaultObjects,
       "cfprFaultInstTable": cfprFaultInstTable,
       "cfprFaultInstEntry": cfprFaultInstEntry,
       "cfprFaultInstInstanceId": cfprFaultInstInstanceId,
       "cfprFaultInstDn": cfprFaultInstDn,
       "cfprFaultInstRn": cfprFaultInstRn,
       "cfprFaultInstAffectedObjectId": cfprFaultInstAffectedObjectId,
       "cfprFaultInstAffectedObjectDn": cfprFaultInstAffectedObjectDn,
       "cfprFaultInstAck": cfprFaultInstAck,
       "cfprFaultInstCause": cfprFaultInstCause,
       "cfprFaultInstChangeSet": cfprFaultInstChangeSet,
       "cfprFaultInstCode": cfprFaultInstCode,
       "cfprFaultInstCreated": cfprFaultInstCreated,
       "cfprFaultInstDescr": cfprFaultInstDescr,
       "cfprFaultInstHighestSeverity": cfprFaultInstHighestSeverity,
       "cfprFaultInstId": cfprFaultInstId,
       "cfprFaultInstLastTransition": cfprFaultInstLastTransition,
       "cfprFaultInstLc": cfprFaultInstLc,
       "cfprFaultInstOccur": cfprFaultInstOccur,
       "cfprFaultInstOrigSeverity": cfprFaultInstOrigSeverity,
       "cfprFaultInstPrevSeverity": cfprFaultInstPrevSeverity,
       "cfprFaultInstRule": cfprFaultInstRule,
       "cfprFaultInstSeverity": cfprFaultInstSeverity,
       "cfprFaultInstTags": cfprFaultInstTags,
       "cfprFaultInstType": cfprFaultInstType,
       "cfprFaultAffectedClassTable": cfprFaultAffectedClassTable,
       "cfprFaultAffectedClassEntry": cfprFaultAffectedClassEntry,
       "cfprFaultAffectedClassInstanceId": cfprFaultAffectedClassInstanceId,
       "cfprFaultAffectedClassDn": cfprFaultAffectedClassDn,
       "cfprFaultAffectedClassRn": cfprFaultAffectedClassRn,
       "cfprFaultAffectedClassMoClassId": cfprFaultAffectedClassMoClassId,
       "cfprFaultHolderTable": cfprFaultHolderTable,
       "cfprFaultHolderEntry": cfprFaultHolderEntry,
       "cfprFaultHolderInstanceId": cfprFaultHolderInstanceId,
       "cfprFaultHolderDn": cfprFaultHolderDn,
       "cfprFaultHolderRn": cfprFaultHolderRn,
       "cfprFaultHolderName": cfprFaultHolderName,
       "cfprFaultHolderTotalFaults": cfprFaultHolderTotalFaults,
       "cfprFaultLocalTypedHolderTable": cfprFaultLocalTypedHolderTable,
       "cfprFaultLocalTypedHolderEntry": cfprFaultLocalTypedHolderEntry,
       "cfprFaultLocalTypedHolderInstanceId": cfprFaultLocalTypedHolderInstanceId,
       "cfprFaultLocalTypedHolderDn": cfprFaultLocalTypedHolderDn,
       "cfprFaultLocalTypedHolderRn": cfprFaultLocalTypedHolderRn,
       "cfprFaultLocalTypedHolderName": cfprFaultLocalTypedHolderName,
       "cfprFaultLocalTypedHolderTotalFaults": cfprFaultLocalTypedHolderTotalFaults,
       "cfprFaultLocalTypedHolderType": cfprFaultLocalTypedHolderType,
       "cfprFaultPolicyTable": cfprFaultPolicyTable,
       "cfprFaultPolicyEntry": cfprFaultPolicyEntry,
       "cfprFaultPolicyInstanceId": cfprFaultPolicyInstanceId,
       "cfprFaultPolicyDn": cfprFaultPolicyDn,
       "cfprFaultPolicyRn": cfprFaultPolicyRn,
       "cfprFaultPolicyAckAction": cfprFaultPolicyAckAction,
       "cfprFaultPolicyClearAction": cfprFaultPolicyClearAction,
       "cfprFaultPolicyClearInterval": cfprFaultPolicyClearInterval,
       "cfprFaultPolicyDescr": cfprFaultPolicyDescr,
       "cfprFaultPolicyFlapInterval": cfprFaultPolicyFlapInterval,
       "cfprFaultPolicyIntId": cfprFaultPolicyIntId,
       "cfprFaultPolicyName": cfprFaultPolicyName,
       "cfprFaultPolicyPolicyLevel": cfprFaultPolicyPolicyLevel,
       "cfprFaultPolicyPolicyOwner": cfprFaultPolicyPolicyOwner,
       "cfprFaultPolicyRetentionInterval": cfprFaultPolicyRetentionInterval,
       "cfprFaultPolicySizeLimit": cfprFaultPolicySizeLimit,
       "cfprFaultPolicySoakInterval": cfprFaultPolicySoakInterval,
       "cfprFaultPolicySoakingSeverity": cfprFaultPolicySoakingSeverity,
       "cfprFaultSuppressPolicyTable": cfprFaultSuppressPolicyTable,
       "cfprFaultSuppressPolicyEntry": cfprFaultSuppressPolicyEntry,
       "cfprFaultSuppressPolicyInstanceId": cfprFaultSuppressPolicyInstanceId,
       "cfprFaultSuppressPolicyDn": cfprFaultSuppressPolicyDn,
       "cfprFaultSuppressPolicyRn": cfprFaultSuppressPolicyRn,
       "cfprFaultSuppressPolicyDescr": cfprFaultSuppressPolicyDescr,
       "cfprFaultSuppressPolicyIntId": cfprFaultSuppressPolicyIntId,
       "cfprFaultSuppressPolicyName": cfprFaultSuppressPolicyName,
       "cfprFaultSuppressPolicyPolicyLevel": cfprFaultSuppressPolicyPolicyLevel,
       "cfprFaultSuppressPolicyPolicyOwner": cfprFaultSuppressPolicyPolicyOwner,
       "cfprFaultSuppressPolicyItemTable": cfprFaultSuppressPolicyItemTable,
       "cfprFaultSuppressPolicyItemEntry": cfprFaultSuppressPolicyItemEntry,
       "cfprFaultSuppressPolicyItemInstanceId": cfprFaultSuppressPolicyItemInstanceId,
       "cfprFaultSuppressPolicyItemDn": cfprFaultSuppressPolicyItemDn,
       "cfprFaultSuppressPolicyItemRn": cfprFaultSuppressPolicyItemRn,
       "cfprFaultSuppressPolicyItemCause": cfprFaultSuppressPolicyItemCause,
       "cfprFaultSuppressPolicyItemDescr": cfprFaultSuppressPolicyItemDescr,
       "cfprFaultSuppressPolicyItemType": cfprFaultSuppressPolicyItemType,
       "cfprFaultSuppressTaskTable": cfprFaultSuppressTaskTable,
       "cfprFaultSuppressTaskEntry": cfprFaultSuppressTaskEntry,
       "cfprFaultSuppressTaskInstanceId": cfprFaultSuppressTaskInstanceId,
       "cfprFaultSuppressTaskDn": cfprFaultSuppressTaskDn,
       "cfprFaultSuppressTaskRn": cfprFaultSuppressTaskRn,
       "cfprFaultSuppressTaskAdminState": cfprFaultSuppressTaskAdminState,
       "cfprFaultSuppressTaskAutoDelete": cfprFaultSuppressTaskAutoDelete,
       "cfprFaultSuppressTaskDescr": cfprFaultSuppressTaskDescr,
       "cfprFaultSuppressTaskIgnoreCap": cfprFaultSuppressTaskIgnoreCap,
       "cfprFaultSuppressTaskIntId": cfprFaultSuppressTaskIntId,
       "cfprFaultSuppressTaskName": cfprFaultSuppressTaskName,
       "cfprFaultSuppressTaskOperScheduler": cfprFaultSuppressTaskOperScheduler,
       "cfprFaultSuppressTaskOperState": cfprFaultSuppressTaskOperState,
       "cfprFaultSuppressTaskOperSuppressPolicyName": cfprFaultSuppressTaskOperSuppressPolicyName,
       "cfprFaultSuppressTaskPolicyLevel": cfprFaultSuppressTaskPolicyLevel,
       "cfprFaultSuppressTaskPolicyOwner": cfprFaultSuppressTaskPolicyOwner,
       "cfprFaultSuppressTaskScheduler": cfprFaultSuppressTaskScheduler,
       "cfprFaultSuppressTaskSuppressPolicyName": cfprFaultSuppressTaskSuppressPolicyName}
)
