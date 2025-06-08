# SNMP MIB module (CISCO-FIREPOWER-AP-FAULT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-FAULT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:16:53 2025
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

(CfprApConditionAckAction,
 CfprApConditionCause,
 CfprApConditionCode,
 CfprApConditionLifecycle,
 CfprApConditionRule,
 CfprApConditionSeverity,
 CfprApConditionTag,
 CfprApConditionType,
 CfprApFaultBasePolicyClearAction,
 CfprApFaultBasePolicySoakingSeverity,
 CfprApMoMoClassId,
 CfprApPolicyPolicyOwner,
 CfprApTrigAdminState,
 CfprApTrigTrigOperState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionAckAction",
    "CfprApConditionCause",
    "CfprApConditionCode",
    "CfprApConditionLifecycle",
    "CfprApConditionRule",
    "CfprApConditionSeverity",
    "CfprApConditionTag",
    "CfprApConditionType",
    "CfprApFaultBasePolicyClearAction",
    "CfprApFaultBasePolicySoakingSeverity",
    "CfprApMoMoClassId",
    "CfprApPolicyPolicyOwner",
    "CfprApTrigAdminState",
    "CfprApTrigTrigOperState")

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

cfprApFaultObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApFaultInstTable_Object = MibTable
cfprApFaultInstTable = _CfprApFaultInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfprApFaultInstTable.setStatus("current")
_CfprApFaultInstEntry_Object = MibTableRow
cfprApFaultInstEntry = _CfprApFaultInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1)
)
cfprApFaultInstEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultInstInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFaultInstEntry.setStatus("current")
_CfprApFaultInstInstanceId_Type = CfprApManagedObjectId
_CfprApFaultInstInstanceId_Object = MibTableColumn
cfprApFaultInstInstanceId = _CfprApFaultInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 1),
    _CfprApFaultInstInstanceId_Type()
)
cfprApFaultInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFaultInstInstanceId.setStatus("current")
_CfprApFaultInstDn_Type = CfprApManagedObjectDn
_CfprApFaultInstDn_Object = MibTableColumn
cfprApFaultInstDn = _CfprApFaultInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 2),
    _CfprApFaultInstDn_Type()
)
cfprApFaultInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstDn.setStatus("current")
_CfprApFaultInstRn_Type = SnmpAdminString
_CfprApFaultInstRn_Object = MibTableColumn
cfprApFaultInstRn = _CfprApFaultInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 3),
    _CfprApFaultInstRn_Type()
)
cfprApFaultInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstRn.setStatus("current")
_CfprApFaultInstAffectedObjectId_Type = RowPointer
_CfprApFaultInstAffectedObjectId_Object = MibTableColumn
cfprApFaultInstAffectedObjectId = _CfprApFaultInstAffectedObjectId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 4),
    _CfprApFaultInstAffectedObjectId_Type()
)
cfprApFaultInstAffectedObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstAffectedObjectId.setStatus("current")
_CfprApFaultInstAffectedObjectDn_Type = CfprApManagedObjectDn
_CfprApFaultInstAffectedObjectDn_Object = MibTableColumn
cfprApFaultInstAffectedObjectDn = _CfprApFaultInstAffectedObjectDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 5),
    _CfprApFaultInstAffectedObjectDn_Type()
)
cfprApFaultInstAffectedObjectDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstAffectedObjectDn.setStatus("current")
_CfprApFaultInstAck_Type = TruthValue
_CfprApFaultInstAck_Object = MibTableColumn
cfprApFaultInstAck = _CfprApFaultInstAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 6),
    _CfprApFaultInstAck_Type()
)
cfprApFaultInstAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstAck.setStatus("current")
_CfprApFaultInstCause_Type = CfprApConditionCause
_CfprApFaultInstCause_Object = MibTableColumn
cfprApFaultInstCause = _CfprApFaultInstCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 7),
    _CfprApFaultInstCause_Type()
)
cfprApFaultInstCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstCause.setStatus("current")
_CfprApFaultInstChangeSet_Type = SnmpAdminString
_CfprApFaultInstChangeSet_Object = MibTableColumn
cfprApFaultInstChangeSet = _CfprApFaultInstChangeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 8),
    _CfprApFaultInstChangeSet_Type()
)
cfprApFaultInstChangeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstChangeSet.setStatus("current")
_CfprApFaultInstCode_Type = CfprApConditionCode
_CfprApFaultInstCode_Object = MibTableColumn
cfprApFaultInstCode = _CfprApFaultInstCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 9),
    _CfprApFaultInstCode_Type()
)
cfprApFaultInstCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstCode.setStatus("current")
_CfprApFaultInstCreated_Type = DateAndTime
_CfprApFaultInstCreated_Object = MibTableColumn
cfprApFaultInstCreated = _CfprApFaultInstCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 10),
    _CfprApFaultInstCreated_Type()
)
cfprApFaultInstCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstCreated.setStatus("current")
_CfprApFaultInstDescr_Type = SnmpAdminString
_CfprApFaultInstDescr_Object = MibTableColumn
cfprApFaultInstDescr = _CfprApFaultInstDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 11),
    _CfprApFaultInstDescr_Type()
)
cfprApFaultInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstDescr.setStatus("current")
_CfprApFaultInstHighestSeverity_Type = CfprApConditionSeverity
_CfprApFaultInstHighestSeverity_Object = MibTableColumn
cfprApFaultInstHighestSeverity = _CfprApFaultInstHighestSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 12),
    _CfprApFaultInstHighestSeverity_Type()
)
cfprApFaultInstHighestSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstHighestSeverity.setStatus("current")
_CfprApFaultInstId_Type = Unsigned64
_CfprApFaultInstId_Object = MibTableColumn
cfprApFaultInstId = _CfprApFaultInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 13),
    _CfprApFaultInstId_Type()
)
cfprApFaultInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstId.setStatus("current")
_CfprApFaultInstLastTransition_Type = DateAndTime
_CfprApFaultInstLastTransition_Object = MibTableColumn
cfprApFaultInstLastTransition = _CfprApFaultInstLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 14),
    _CfprApFaultInstLastTransition_Type()
)
cfprApFaultInstLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstLastTransition.setStatus("current")
_CfprApFaultInstLc_Type = CfprApConditionLifecycle
_CfprApFaultInstLc_Object = MibTableColumn
cfprApFaultInstLc = _CfprApFaultInstLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 15),
    _CfprApFaultInstLc_Type()
)
cfprApFaultInstLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstLc.setStatus("current")
_CfprApFaultInstOccur_Type = Gauge32
_CfprApFaultInstOccur_Object = MibTableColumn
cfprApFaultInstOccur = _CfprApFaultInstOccur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 16),
    _CfprApFaultInstOccur_Type()
)
cfprApFaultInstOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstOccur.setStatus("current")
_CfprApFaultInstOrigSeverity_Type = CfprApConditionSeverity
_CfprApFaultInstOrigSeverity_Object = MibTableColumn
cfprApFaultInstOrigSeverity = _CfprApFaultInstOrigSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 17),
    _CfprApFaultInstOrigSeverity_Type()
)
cfprApFaultInstOrigSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstOrigSeverity.setStatus("current")
_CfprApFaultInstPrevSeverity_Type = CfprApConditionSeverity
_CfprApFaultInstPrevSeverity_Object = MibTableColumn
cfprApFaultInstPrevSeverity = _CfprApFaultInstPrevSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 18),
    _CfprApFaultInstPrevSeverity_Type()
)
cfprApFaultInstPrevSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstPrevSeverity.setStatus("current")
_CfprApFaultInstRule_Type = CfprApConditionRule
_CfprApFaultInstRule_Object = MibTableColumn
cfprApFaultInstRule = _CfprApFaultInstRule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 19),
    _CfprApFaultInstRule_Type()
)
cfprApFaultInstRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstRule.setStatus("current")
_CfprApFaultInstSeverity_Type = CfprApConditionSeverity
_CfprApFaultInstSeverity_Object = MibTableColumn
cfprApFaultInstSeverity = _CfprApFaultInstSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 20),
    _CfprApFaultInstSeverity_Type()
)
cfprApFaultInstSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstSeverity.setStatus("current")
_CfprApFaultInstTags_Type = CfprApConditionTag
_CfprApFaultInstTags_Object = MibTableColumn
cfprApFaultInstTags = _CfprApFaultInstTags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 21),
    _CfprApFaultInstTags_Type()
)
cfprApFaultInstTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstTags.setStatus("current")
_CfprApFaultInstType_Type = CfprApConditionType
_CfprApFaultInstType_Object = MibTableColumn
cfprApFaultInstType = _CfprApFaultInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 1, 1, 22),
    _CfprApFaultInstType_Type()
)
cfprApFaultInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultInstType.setStatus("current")
_CfprApFaultAffectedClassTable_Object = MibTable
cfprApFaultAffectedClassTable = _CfprApFaultAffectedClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cfprApFaultAffectedClassTable.setStatus("current")
_CfprApFaultAffectedClassEntry_Object = MibTableRow
cfprApFaultAffectedClassEntry = _CfprApFaultAffectedClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 2, 1)
)
cfprApFaultAffectedClassEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultAffectedClassInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFaultAffectedClassEntry.setStatus("current")
_CfprApFaultAffectedClassInstanceId_Type = CfprApManagedObjectId
_CfprApFaultAffectedClassInstanceId_Object = MibTableColumn
cfprApFaultAffectedClassInstanceId = _CfprApFaultAffectedClassInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 2, 1, 1),
    _CfprApFaultAffectedClassInstanceId_Type()
)
cfprApFaultAffectedClassInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFaultAffectedClassInstanceId.setStatus("current")
_CfprApFaultAffectedClassDn_Type = CfprApManagedObjectDn
_CfprApFaultAffectedClassDn_Object = MibTableColumn
cfprApFaultAffectedClassDn = _CfprApFaultAffectedClassDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 2, 1, 2),
    _CfprApFaultAffectedClassDn_Type()
)
cfprApFaultAffectedClassDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultAffectedClassDn.setStatus("current")
_CfprApFaultAffectedClassRn_Type = SnmpAdminString
_CfprApFaultAffectedClassRn_Object = MibTableColumn
cfprApFaultAffectedClassRn = _CfprApFaultAffectedClassRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 2, 1, 3),
    _CfprApFaultAffectedClassRn_Type()
)
cfprApFaultAffectedClassRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultAffectedClassRn.setStatus("current")
_CfprApFaultAffectedClassMoClassId_Type = CfprApMoMoClassId
_CfprApFaultAffectedClassMoClassId_Object = MibTableColumn
cfprApFaultAffectedClassMoClassId = _CfprApFaultAffectedClassMoClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 2, 1, 4),
    _CfprApFaultAffectedClassMoClassId_Type()
)
cfprApFaultAffectedClassMoClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultAffectedClassMoClassId.setStatus("current")
_CfprApFaultHolderTable_Object = MibTable
cfprApFaultHolderTable = _CfprApFaultHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfprApFaultHolderTable.setStatus("current")
_CfprApFaultHolderEntry_Object = MibTableRow
cfprApFaultHolderEntry = _CfprApFaultHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 3, 1)
)
cfprApFaultHolderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFaultHolderEntry.setStatus("current")
_CfprApFaultHolderInstanceId_Type = CfprApManagedObjectId
_CfprApFaultHolderInstanceId_Object = MibTableColumn
cfprApFaultHolderInstanceId = _CfprApFaultHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 3, 1, 1),
    _CfprApFaultHolderInstanceId_Type()
)
cfprApFaultHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFaultHolderInstanceId.setStatus("current")
_CfprApFaultHolderDn_Type = CfprApManagedObjectDn
_CfprApFaultHolderDn_Object = MibTableColumn
cfprApFaultHolderDn = _CfprApFaultHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 3, 1, 2),
    _CfprApFaultHolderDn_Type()
)
cfprApFaultHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultHolderDn.setStatus("current")
_CfprApFaultHolderRn_Type = SnmpAdminString
_CfprApFaultHolderRn_Object = MibTableColumn
cfprApFaultHolderRn = _CfprApFaultHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 3, 1, 3),
    _CfprApFaultHolderRn_Type()
)
cfprApFaultHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultHolderRn.setStatus("current")
_CfprApFaultHolderName_Type = SnmpAdminString
_CfprApFaultHolderName_Object = MibTableColumn
cfprApFaultHolderName = _CfprApFaultHolderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 3, 1, 4),
    _CfprApFaultHolderName_Type()
)
cfprApFaultHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultHolderName.setStatus("current")
_CfprApFaultHolderTotalFaults_Type = Unsigned64
_CfprApFaultHolderTotalFaults_Object = MibTableColumn
cfprApFaultHolderTotalFaults = _CfprApFaultHolderTotalFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 3, 1, 5),
    _CfprApFaultHolderTotalFaults_Type()
)
cfprApFaultHolderTotalFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultHolderTotalFaults.setStatus("current")
_CfprApFaultLocalTypedHolderTable_Object = MibTable
cfprApFaultLocalTypedHolderTable = _CfprApFaultLocalTypedHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cfprApFaultLocalTypedHolderTable.setStatus("current")
_CfprApFaultLocalTypedHolderEntry_Object = MibTableRow
cfprApFaultLocalTypedHolderEntry = _CfprApFaultLocalTypedHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 4, 1)
)
cfprApFaultLocalTypedHolderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultLocalTypedHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFaultLocalTypedHolderEntry.setStatus("current")
_CfprApFaultLocalTypedHolderInstanceId_Type = CfprApManagedObjectId
_CfprApFaultLocalTypedHolderInstanceId_Object = MibTableColumn
cfprApFaultLocalTypedHolderInstanceId = _CfprApFaultLocalTypedHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 4, 1, 1),
    _CfprApFaultLocalTypedHolderInstanceId_Type()
)
cfprApFaultLocalTypedHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFaultLocalTypedHolderInstanceId.setStatus("current")
_CfprApFaultLocalTypedHolderDn_Type = CfprApManagedObjectDn
_CfprApFaultLocalTypedHolderDn_Object = MibTableColumn
cfprApFaultLocalTypedHolderDn = _CfprApFaultLocalTypedHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 4, 1, 2),
    _CfprApFaultLocalTypedHolderDn_Type()
)
cfprApFaultLocalTypedHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultLocalTypedHolderDn.setStatus("current")
_CfprApFaultLocalTypedHolderRn_Type = SnmpAdminString
_CfprApFaultLocalTypedHolderRn_Object = MibTableColumn
cfprApFaultLocalTypedHolderRn = _CfprApFaultLocalTypedHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 4, 1, 3),
    _CfprApFaultLocalTypedHolderRn_Type()
)
cfprApFaultLocalTypedHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultLocalTypedHolderRn.setStatus("current")
_CfprApFaultLocalTypedHolderName_Type = SnmpAdminString
_CfprApFaultLocalTypedHolderName_Object = MibTableColumn
cfprApFaultLocalTypedHolderName = _CfprApFaultLocalTypedHolderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 4, 1, 4),
    _CfprApFaultLocalTypedHolderName_Type()
)
cfprApFaultLocalTypedHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultLocalTypedHolderName.setStatus("current")
_CfprApFaultLocalTypedHolderTotalFaults_Type = Unsigned64
_CfprApFaultLocalTypedHolderTotalFaults_Object = MibTableColumn
cfprApFaultLocalTypedHolderTotalFaults = _CfprApFaultLocalTypedHolderTotalFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 4, 1, 5),
    _CfprApFaultLocalTypedHolderTotalFaults_Type()
)
cfprApFaultLocalTypedHolderTotalFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultLocalTypedHolderTotalFaults.setStatus("current")
_CfprApFaultLocalTypedHolderType_Type = CfprApConditionType
_CfprApFaultLocalTypedHolderType_Object = MibTableColumn
cfprApFaultLocalTypedHolderType = _CfprApFaultLocalTypedHolderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 4, 1, 6),
    _CfprApFaultLocalTypedHolderType_Type()
)
cfprApFaultLocalTypedHolderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultLocalTypedHolderType.setStatus("current")
_CfprApFaultPolicyTable_Object = MibTable
cfprApFaultPolicyTable = _CfprApFaultPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cfprApFaultPolicyTable.setStatus("current")
_CfprApFaultPolicyEntry_Object = MibTableRow
cfprApFaultPolicyEntry = _CfprApFaultPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1)
)
cfprApFaultPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFaultPolicyEntry.setStatus("current")
_CfprApFaultPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApFaultPolicyInstanceId_Object = MibTableColumn
cfprApFaultPolicyInstanceId = _CfprApFaultPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 1),
    _CfprApFaultPolicyInstanceId_Type()
)
cfprApFaultPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFaultPolicyInstanceId.setStatus("current")
_CfprApFaultPolicyDn_Type = CfprApManagedObjectDn
_CfprApFaultPolicyDn_Object = MibTableColumn
cfprApFaultPolicyDn = _CfprApFaultPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 2),
    _CfprApFaultPolicyDn_Type()
)
cfprApFaultPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicyDn.setStatus("current")
_CfprApFaultPolicyRn_Type = SnmpAdminString
_CfprApFaultPolicyRn_Object = MibTableColumn
cfprApFaultPolicyRn = _CfprApFaultPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 3),
    _CfprApFaultPolicyRn_Type()
)
cfprApFaultPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicyRn.setStatus("current")
_CfprApFaultPolicyAckAction_Type = CfprApConditionAckAction
_CfprApFaultPolicyAckAction_Object = MibTableColumn
cfprApFaultPolicyAckAction = _CfprApFaultPolicyAckAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 4),
    _CfprApFaultPolicyAckAction_Type()
)
cfprApFaultPolicyAckAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicyAckAction.setStatus("current")
_CfprApFaultPolicyClearAction_Type = CfprApFaultBasePolicyClearAction
_CfprApFaultPolicyClearAction_Object = MibTableColumn
cfprApFaultPolicyClearAction = _CfprApFaultPolicyClearAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 5),
    _CfprApFaultPolicyClearAction_Type()
)
cfprApFaultPolicyClearAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicyClearAction.setStatus("current")
_CfprApFaultPolicyClearInterval_Type = TimeIntervalSec
_CfprApFaultPolicyClearInterval_Object = MibTableColumn
cfprApFaultPolicyClearInterval = _CfprApFaultPolicyClearInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 6),
    _CfprApFaultPolicyClearInterval_Type()
)
cfprApFaultPolicyClearInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicyClearInterval.setStatus("current")
_CfprApFaultPolicyDescr_Type = SnmpAdminString
_CfprApFaultPolicyDescr_Object = MibTableColumn
cfprApFaultPolicyDescr = _CfprApFaultPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 7),
    _CfprApFaultPolicyDescr_Type()
)
cfprApFaultPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicyDescr.setStatus("current")
_CfprApFaultPolicyFlapInterval_Type = Unsigned64
_CfprApFaultPolicyFlapInterval_Object = MibTableColumn
cfprApFaultPolicyFlapInterval = _CfprApFaultPolicyFlapInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 8),
    _CfprApFaultPolicyFlapInterval_Type()
)
cfprApFaultPolicyFlapInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicyFlapInterval.setStatus("current")
_CfprApFaultPolicyIntId_Type = SnmpAdminString
_CfprApFaultPolicyIntId_Object = MibTableColumn
cfprApFaultPolicyIntId = _CfprApFaultPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 9),
    _CfprApFaultPolicyIntId_Type()
)
cfprApFaultPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicyIntId.setStatus("current")
_CfprApFaultPolicyName_Type = SnmpAdminString
_CfprApFaultPolicyName_Object = MibTableColumn
cfprApFaultPolicyName = _CfprApFaultPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 10),
    _CfprApFaultPolicyName_Type()
)
cfprApFaultPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicyName.setStatus("current")
_CfprApFaultPolicyPolicyLevel_Type = Gauge32
_CfprApFaultPolicyPolicyLevel_Object = MibTableColumn
cfprApFaultPolicyPolicyLevel = _CfprApFaultPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 11),
    _CfprApFaultPolicyPolicyLevel_Type()
)
cfprApFaultPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicyPolicyLevel.setStatus("current")
_CfprApFaultPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFaultPolicyPolicyOwner_Object = MibTableColumn
cfprApFaultPolicyPolicyOwner = _CfprApFaultPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 12),
    _CfprApFaultPolicyPolicyOwner_Type()
)
cfprApFaultPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicyPolicyOwner.setStatus("current")
_CfprApFaultPolicyRetentionInterval_Type = TimeIntervalSec
_CfprApFaultPolicyRetentionInterval_Object = MibTableColumn
cfprApFaultPolicyRetentionInterval = _CfprApFaultPolicyRetentionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 13),
    _CfprApFaultPolicyRetentionInterval_Type()
)
cfprApFaultPolicyRetentionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicyRetentionInterval.setStatus("current")
_CfprApFaultPolicySizeLimit_Type = Gauge32
_CfprApFaultPolicySizeLimit_Object = MibTableColumn
cfprApFaultPolicySizeLimit = _CfprApFaultPolicySizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 14),
    _CfprApFaultPolicySizeLimit_Type()
)
cfprApFaultPolicySizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicySizeLimit.setStatus("current")
_CfprApFaultPolicySoakInterval_Type = TimeIntervalSec
_CfprApFaultPolicySoakInterval_Object = MibTableColumn
cfprApFaultPolicySoakInterval = _CfprApFaultPolicySoakInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 15),
    _CfprApFaultPolicySoakInterval_Type()
)
cfprApFaultPolicySoakInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicySoakInterval.setStatus("current")
_CfprApFaultPolicySoakingSeverity_Type = CfprApFaultBasePolicySoakingSeverity
_CfprApFaultPolicySoakingSeverity_Object = MibTableColumn
cfprApFaultPolicySoakingSeverity = _CfprApFaultPolicySoakingSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 5, 1, 16),
    _CfprApFaultPolicySoakingSeverity_Type()
)
cfprApFaultPolicySoakingSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultPolicySoakingSeverity.setStatus("current")
_CfprApFaultSuppressPolicyTable_Object = MibTable
cfprApFaultSuppressPolicyTable = _CfprApFaultSuppressPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyTable.setStatus("current")
_CfprApFaultSuppressPolicyEntry_Object = MibTableRow
cfprApFaultSuppressPolicyEntry = _CfprApFaultSuppressPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 6, 1)
)
cfprApFaultSuppressPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultSuppressPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyEntry.setStatus("current")
_CfprApFaultSuppressPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApFaultSuppressPolicyInstanceId_Object = MibTableColumn
cfprApFaultSuppressPolicyInstanceId = _CfprApFaultSuppressPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 6, 1, 1),
    _CfprApFaultSuppressPolicyInstanceId_Type()
)
cfprApFaultSuppressPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyInstanceId.setStatus("current")
_CfprApFaultSuppressPolicyDn_Type = CfprApManagedObjectDn
_CfprApFaultSuppressPolicyDn_Object = MibTableColumn
cfprApFaultSuppressPolicyDn = _CfprApFaultSuppressPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 6, 1, 2),
    _CfprApFaultSuppressPolicyDn_Type()
)
cfprApFaultSuppressPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyDn.setStatus("current")
_CfprApFaultSuppressPolicyRn_Type = SnmpAdminString
_CfprApFaultSuppressPolicyRn_Object = MibTableColumn
cfprApFaultSuppressPolicyRn = _CfprApFaultSuppressPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 6, 1, 3),
    _CfprApFaultSuppressPolicyRn_Type()
)
cfprApFaultSuppressPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyRn.setStatus("current")
_CfprApFaultSuppressPolicyDescr_Type = SnmpAdminString
_CfprApFaultSuppressPolicyDescr_Object = MibTableColumn
cfprApFaultSuppressPolicyDescr = _CfprApFaultSuppressPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 6, 1, 4),
    _CfprApFaultSuppressPolicyDescr_Type()
)
cfprApFaultSuppressPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyDescr.setStatus("current")
_CfprApFaultSuppressPolicyIntId_Type = SnmpAdminString
_CfprApFaultSuppressPolicyIntId_Object = MibTableColumn
cfprApFaultSuppressPolicyIntId = _CfprApFaultSuppressPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 6, 1, 5),
    _CfprApFaultSuppressPolicyIntId_Type()
)
cfprApFaultSuppressPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyIntId.setStatus("current")
_CfprApFaultSuppressPolicyName_Type = SnmpAdminString
_CfprApFaultSuppressPolicyName_Object = MibTableColumn
cfprApFaultSuppressPolicyName = _CfprApFaultSuppressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 6, 1, 6),
    _CfprApFaultSuppressPolicyName_Type()
)
cfprApFaultSuppressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyName.setStatus("current")
_CfprApFaultSuppressPolicyPolicyLevel_Type = Gauge32
_CfprApFaultSuppressPolicyPolicyLevel_Object = MibTableColumn
cfprApFaultSuppressPolicyPolicyLevel = _CfprApFaultSuppressPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 6, 1, 7),
    _CfprApFaultSuppressPolicyPolicyLevel_Type()
)
cfprApFaultSuppressPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyPolicyLevel.setStatus("current")
_CfprApFaultSuppressPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFaultSuppressPolicyPolicyOwner_Object = MibTableColumn
cfprApFaultSuppressPolicyPolicyOwner = _CfprApFaultSuppressPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 6, 1, 8),
    _CfprApFaultSuppressPolicyPolicyOwner_Type()
)
cfprApFaultSuppressPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyPolicyOwner.setStatus("current")
_CfprApFaultSuppressPolicyItemTable_Object = MibTable
cfprApFaultSuppressPolicyItemTable = _CfprApFaultSuppressPolicyItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyItemTable.setStatus("current")
_CfprApFaultSuppressPolicyItemEntry_Object = MibTableRow
cfprApFaultSuppressPolicyItemEntry = _CfprApFaultSuppressPolicyItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 7, 1)
)
cfprApFaultSuppressPolicyItemEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultSuppressPolicyItemInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyItemEntry.setStatus("current")
_CfprApFaultSuppressPolicyItemInstanceId_Type = CfprApManagedObjectId
_CfprApFaultSuppressPolicyItemInstanceId_Object = MibTableColumn
cfprApFaultSuppressPolicyItemInstanceId = _CfprApFaultSuppressPolicyItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 7, 1, 1),
    _CfprApFaultSuppressPolicyItemInstanceId_Type()
)
cfprApFaultSuppressPolicyItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyItemInstanceId.setStatus("current")
_CfprApFaultSuppressPolicyItemDn_Type = CfprApManagedObjectDn
_CfprApFaultSuppressPolicyItemDn_Object = MibTableColumn
cfprApFaultSuppressPolicyItemDn = _CfprApFaultSuppressPolicyItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 7, 1, 2),
    _CfprApFaultSuppressPolicyItemDn_Type()
)
cfprApFaultSuppressPolicyItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyItemDn.setStatus("current")
_CfprApFaultSuppressPolicyItemRn_Type = SnmpAdminString
_CfprApFaultSuppressPolicyItemRn_Object = MibTableColumn
cfprApFaultSuppressPolicyItemRn = _CfprApFaultSuppressPolicyItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 7, 1, 3),
    _CfprApFaultSuppressPolicyItemRn_Type()
)
cfprApFaultSuppressPolicyItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyItemRn.setStatus("current")
_CfprApFaultSuppressPolicyItemCause_Type = CfprApConditionCause
_CfprApFaultSuppressPolicyItemCause_Object = MibTableColumn
cfprApFaultSuppressPolicyItemCause = _CfprApFaultSuppressPolicyItemCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 7, 1, 4),
    _CfprApFaultSuppressPolicyItemCause_Type()
)
cfprApFaultSuppressPolicyItemCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyItemCause.setStatus("current")
_CfprApFaultSuppressPolicyItemDescr_Type = SnmpAdminString
_CfprApFaultSuppressPolicyItemDescr_Object = MibTableColumn
cfprApFaultSuppressPolicyItemDescr = _CfprApFaultSuppressPolicyItemDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 7, 1, 5),
    _CfprApFaultSuppressPolicyItemDescr_Type()
)
cfprApFaultSuppressPolicyItemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyItemDescr.setStatus("current")
_CfprApFaultSuppressPolicyItemType_Type = CfprApConditionType
_CfprApFaultSuppressPolicyItemType_Object = MibTableColumn
cfprApFaultSuppressPolicyItemType = _CfprApFaultSuppressPolicyItemType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 7, 1, 6),
    _CfprApFaultSuppressPolicyItemType_Type()
)
cfprApFaultSuppressPolicyItemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressPolicyItemType.setStatus("current")
_CfprApFaultSuppressTaskTable_Object = MibTable
cfprApFaultSuppressTaskTable = _CfprApFaultSuppressTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskTable.setStatus("current")
_CfprApFaultSuppressTaskEntry_Object = MibTableRow
cfprApFaultSuppressTaskEntry = _CfprApFaultSuppressTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1)
)
cfprApFaultSuppressTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FAULT-MIB", "cfprApFaultSuppressTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskEntry.setStatus("current")
_CfprApFaultSuppressTaskInstanceId_Type = CfprApManagedObjectId
_CfprApFaultSuppressTaskInstanceId_Object = MibTableColumn
cfprApFaultSuppressTaskInstanceId = _CfprApFaultSuppressTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 1),
    _CfprApFaultSuppressTaskInstanceId_Type()
)
cfprApFaultSuppressTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskInstanceId.setStatus("current")
_CfprApFaultSuppressTaskDn_Type = CfprApManagedObjectDn
_CfprApFaultSuppressTaskDn_Object = MibTableColumn
cfprApFaultSuppressTaskDn = _CfprApFaultSuppressTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 2),
    _CfprApFaultSuppressTaskDn_Type()
)
cfprApFaultSuppressTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskDn.setStatus("current")
_CfprApFaultSuppressTaskRn_Type = SnmpAdminString
_CfprApFaultSuppressTaskRn_Object = MibTableColumn
cfprApFaultSuppressTaskRn = _CfprApFaultSuppressTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 3),
    _CfprApFaultSuppressTaskRn_Type()
)
cfprApFaultSuppressTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskRn.setStatus("current")
_CfprApFaultSuppressTaskAdminState_Type = CfprApTrigAdminState
_CfprApFaultSuppressTaskAdminState_Object = MibTableColumn
cfprApFaultSuppressTaskAdminState = _CfprApFaultSuppressTaskAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 4),
    _CfprApFaultSuppressTaskAdminState_Type()
)
cfprApFaultSuppressTaskAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskAdminState.setStatus("current")
_CfprApFaultSuppressTaskAutoDelete_Type = TruthValue
_CfprApFaultSuppressTaskAutoDelete_Object = MibTableColumn
cfprApFaultSuppressTaskAutoDelete = _CfprApFaultSuppressTaskAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 5),
    _CfprApFaultSuppressTaskAutoDelete_Type()
)
cfprApFaultSuppressTaskAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskAutoDelete.setStatus("current")
_CfprApFaultSuppressTaskDescr_Type = SnmpAdminString
_CfprApFaultSuppressTaskDescr_Object = MibTableColumn
cfprApFaultSuppressTaskDescr = _CfprApFaultSuppressTaskDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 6),
    _CfprApFaultSuppressTaskDescr_Type()
)
cfprApFaultSuppressTaskDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskDescr.setStatus("current")
_CfprApFaultSuppressTaskIgnoreCap_Type = TruthValue
_CfprApFaultSuppressTaskIgnoreCap_Object = MibTableColumn
cfprApFaultSuppressTaskIgnoreCap = _CfprApFaultSuppressTaskIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 7),
    _CfprApFaultSuppressTaskIgnoreCap_Type()
)
cfprApFaultSuppressTaskIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskIgnoreCap.setStatus("current")
_CfprApFaultSuppressTaskIntId_Type = SnmpAdminString
_CfprApFaultSuppressTaskIntId_Object = MibTableColumn
cfprApFaultSuppressTaskIntId = _CfprApFaultSuppressTaskIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 8),
    _CfprApFaultSuppressTaskIntId_Type()
)
cfprApFaultSuppressTaskIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskIntId.setStatus("current")
_CfprApFaultSuppressTaskName_Type = SnmpAdminString
_CfprApFaultSuppressTaskName_Object = MibTableColumn
cfprApFaultSuppressTaskName = _CfprApFaultSuppressTaskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 9),
    _CfprApFaultSuppressTaskName_Type()
)
cfprApFaultSuppressTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskName.setStatus("current")
_CfprApFaultSuppressTaskOperScheduler_Type = SnmpAdminString
_CfprApFaultSuppressTaskOperScheduler_Object = MibTableColumn
cfprApFaultSuppressTaskOperScheduler = _CfprApFaultSuppressTaskOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 10),
    _CfprApFaultSuppressTaskOperScheduler_Type()
)
cfprApFaultSuppressTaskOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskOperScheduler.setStatus("current")
_CfprApFaultSuppressTaskOperState_Type = CfprApTrigTrigOperState
_CfprApFaultSuppressTaskOperState_Object = MibTableColumn
cfprApFaultSuppressTaskOperState = _CfprApFaultSuppressTaskOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 11),
    _CfprApFaultSuppressTaskOperState_Type()
)
cfprApFaultSuppressTaskOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskOperState.setStatus("current")
_CfprApFaultSuppressTaskOperSuppressPolicyName_Type = SnmpAdminString
_CfprApFaultSuppressTaskOperSuppressPolicyName_Object = MibTableColumn
cfprApFaultSuppressTaskOperSuppressPolicyName = _CfprApFaultSuppressTaskOperSuppressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 12),
    _CfprApFaultSuppressTaskOperSuppressPolicyName_Type()
)
cfprApFaultSuppressTaskOperSuppressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskOperSuppressPolicyName.setStatus("current")
_CfprApFaultSuppressTaskPolicyLevel_Type = Gauge32
_CfprApFaultSuppressTaskPolicyLevel_Object = MibTableColumn
cfprApFaultSuppressTaskPolicyLevel = _CfprApFaultSuppressTaskPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 13),
    _CfprApFaultSuppressTaskPolicyLevel_Type()
)
cfprApFaultSuppressTaskPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskPolicyLevel.setStatus("current")
_CfprApFaultSuppressTaskPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFaultSuppressTaskPolicyOwner_Object = MibTableColumn
cfprApFaultSuppressTaskPolicyOwner = _CfprApFaultSuppressTaskPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 14),
    _CfprApFaultSuppressTaskPolicyOwner_Type()
)
cfprApFaultSuppressTaskPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskPolicyOwner.setStatus("current")
_CfprApFaultSuppressTaskScheduler_Type = SnmpAdminString
_CfprApFaultSuppressTaskScheduler_Object = MibTableColumn
cfprApFaultSuppressTaskScheduler = _CfprApFaultSuppressTaskScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 15),
    _CfprApFaultSuppressTaskScheduler_Type()
)
cfprApFaultSuppressTaskScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskScheduler.setStatus("current")
_CfprApFaultSuppressTaskSuppressPolicyName_Type = SnmpAdminString
_CfprApFaultSuppressTaskSuppressPolicyName_Object = MibTableColumn
cfprApFaultSuppressTaskSuppressPolicyName = _CfprApFaultSuppressTaskSuppressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 1, 8, 1, 16),
    _CfprApFaultSuppressTaskSuppressPolicyName_Type()
)
cfprApFaultSuppressTaskSuppressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFaultSuppressTaskSuppressPolicyName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-FAULT-MIB",
    **{"cfprApFaultObjects": cfprApFaultObjects,
       "cfprApFaultInstTable": cfprApFaultInstTable,
       "cfprApFaultInstEntry": cfprApFaultInstEntry,
       "cfprApFaultInstInstanceId": cfprApFaultInstInstanceId,
       "cfprApFaultInstDn": cfprApFaultInstDn,
       "cfprApFaultInstRn": cfprApFaultInstRn,
       "cfprApFaultInstAffectedObjectId": cfprApFaultInstAffectedObjectId,
       "cfprApFaultInstAffectedObjectDn": cfprApFaultInstAffectedObjectDn,
       "cfprApFaultInstAck": cfprApFaultInstAck,
       "cfprApFaultInstCause": cfprApFaultInstCause,
       "cfprApFaultInstChangeSet": cfprApFaultInstChangeSet,
       "cfprApFaultInstCode": cfprApFaultInstCode,
       "cfprApFaultInstCreated": cfprApFaultInstCreated,
       "cfprApFaultInstDescr": cfprApFaultInstDescr,
       "cfprApFaultInstHighestSeverity": cfprApFaultInstHighestSeverity,
       "cfprApFaultInstId": cfprApFaultInstId,
       "cfprApFaultInstLastTransition": cfprApFaultInstLastTransition,
       "cfprApFaultInstLc": cfprApFaultInstLc,
       "cfprApFaultInstOccur": cfprApFaultInstOccur,
       "cfprApFaultInstOrigSeverity": cfprApFaultInstOrigSeverity,
       "cfprApFaultInstPrevSeverity": cfprApFaultInstPrevSeverity,
       "cfprApFaultInstRule": cfprApFaultInstRule,
       "cfprApFaultInstSeverity": cfprApFaultInstSeverity,
       "cfprApFaultInstTags": cfprApFaultInstTags,
       "cfprApFaultInstType": cfprApFaultInstType,
       "cfprApFaultAffectedClassTable": cfprApFaultAffectedClassTable,
       "cfprApFaultAffectedClassEntry": cfprApFaultAffectedClassEntry,
       "cfprApFaultAffectedClassInstanceId": cfprApFaultAffectedClassInstanceId,
       "cfprApFaultAffectedClassDn": cfprApFaultAffectedClassDn,
       "cfprApFaultAffectedClassRn": cfprApFaultAffectedClassRn,
       "cfprApFaultAffectedClassMoClassId": cfprApFaultAffectedClassMoClassId,
       "cfprApFaultHolderTable": cfprApFaultHolderTable,
       "cfprApFaultHolderEntry": cfprApFaultHolderEntry,
       "cfprApFaultHolderInstanceId": cfprApFaultHolderInstanceId,
       "cfprApFaultHolderDn": cfprApFaultHolderDn,
       "cfprApFaultHolderRn": cfprApFaultHolderRn,
       "cfprApFaultHolderName": cfprApFaultHolderName,
       "cfprApFaultHolderTotalFaults": cfprApFaultHolderTotalFaults,
       "cfprApFaultLocalTypedHolderTable": cfprApFaultLocalTypedHolderTable,
       "cfprApFaultLocalTypedHolderEntry": cfprApFaultLocalTypedHolderEntry,
       "cfprApFaultLocalTypedHolderInstanceId": cfprApFaultLocalTypedHolderInstanceId,
       "cfprApFaultLocalTypedHolderDn": cfprApFaultLocalTypedHolderDn,
       "cfprApFaultLocalTypedHolderRn": cfprApFaultLocalTypedHolderRn,
       "cfprApFaultLocalTypedHolderName": cfprApFaultLocalTypedHolderName,
       "cfprApFaultLocalTypedHolderTotalFaults": cfprApFaultLocalTypedHolderTotalFaults,
       "cfprApFaultLocalTypedHolderType": cfprApFaultLocalTypedHolderType,
       "cfprApFaultPolicyTable": cfprApFaultPolicyTable,
       "cfprApFaultPolicyEntry": cfprApFaultPolicyEntry,
       "cfprApFaultPolicyInstanceId": cfprApFaultPolicyInstanceId,
       "cfprApFaultPolicyDn": cfprApFaultPolicyDn,
       "cfprApFaultPolicyRn": cfprApFaultPolicyRn,
       "cfprApFaultPolicyAckAction": cfprApFaultPolicyAckAction,
       "cfprApFaultPolicyClearAction": cfprApFaultPolicyClearAction,
       "cfprApFaultPolicyClearInterval": cfprApFaultPolicyClearInterval,
       "cfprApFaultPolicyDescr": cfprApFaultPolicyDescr,
       "cfprApFaultPolicyFlapInterval": cfprApFaultPolicyFlapInterval,
       "cfprApFaultPolicyIntId": cfprApFaultPolicyIntId,
       "cfprApFaultPolicyName": cfprApFaultPolicyName,
       "cfprApFaultPolicyPolicyLevel": cfprApFaultPolicyPolicyLevel,
       "cfprApFaultPolicyPolicyOwner": cfprApFaultPolicyPolicyOwner,
       "cfprApFaultPolicyRetentionInterval": cfprApFaultPolicyRetentionInterval,
       "cfprApFaultPolicySizeLimit": cfprApFaultPolicySizeLimit,
       "cfprApFaultPolicySoakInterval": cfprApFaultPolicySoakInterval,
       "cfprApFaultPolicySoakingSeverity": cfprApFaultPolicySoakingSeverity,
       "cfprApFaultSuppressPolicyTable": cfprApFaultSuppressPolicyTable,
       "cfprApFaultSuppressPolicyEntry": cfprApFaultSuppressPolicyEntry,
       "cfprApFaultSuppressPolicyInstanceId": cfprApFaultSuppressPolicyInstanceId,
       "cfprApFaultSuppressPolicyDn": cfprApFaultSuppressPolicyDn,
       "cfprApFaultSuppressPolicyRn": cfprApFaultSuppressPolicyRn,
       "cfprApFaultSuppressPolicyDescr": cfprApFaultSuppressPolicyDescr,
       "cfprApFaultSuppressPolicyIntId": cfprApFaultSuppressPolicyIntId,
       "cfprApFaultSuppressPolicyName": cfprApFaultSuppressPolicyName,
       "cfprApFaultSuppressPolicyPolicyLevel": cfprApFaultSuppressPolicyPolicyLevel,
       "cfprApFaultSuppressPolicyPolicyOwner": cfprApFaultSuppressPolicyPolicyOwner,
       "cfprApFaultSuppressPolicyItemTable": cfprApFaultSuppressPolicyItemTable,
       "cfprApFaultSuppressPolicyItemEntry": cfprApFaultSuppressPolicyItemEntry,
       "cfprApFaultSuppressPolicyItemInstanceId": cfprApFaultSuppressPolicyItemInstanceId,
       "cfprApFaultSuppressPolicyItemDn": cfprApFaultSuppressPolicyItemDn,
       "cfprApFaultSuppressPolicyItemRn": cfprApFaultSuppressPolicyItemRn,
       "cfprApFaultSuppressPolicyItemCause": cfprApFaultSuppressPolicyItemCause,
       "cfprApFaultSuppressPolicyItemDescr": cfprApFaultSuppressPolicyItemDescr,
       "cfprApFaultSuppressPolicyItemType": cfprApFaultSuppressPolicyItemType,
       "cfprApFaultSuppressTaskTable": cfprApFaultSuppressTaskTable,
       "cfprApFaultSuppressTaskEntry": cfprApFaultSuppressTaskEntry,
       "cfprApFaultSuppressTaskInstanceId": cfprApFaultSuppressTaskInstanceId,
       "cfprApFaultSuppressTaskDn": cfprApFaultSuppressTaskDn,
       "cfprApFaultSuppressTaskRn": cfprApFaultSuppressTaskRn,
       "cfprApFaultSuppressTaskAdminState": cfprApFaultSuppressTaskAdminState,
       "cfprApFaultSuppressTaskAutoDelete": cfprApFaultSuppressTaskAutoDelete,
       "cfprApFaultSuppressTaskDescr": cfprApFaultSuppressTaskDescr,
       "cfprApFaultSuppressTaskIgnoreCap": cfprApFaultSuppressTaskIgnoreCap,
       "cfprApFaultSuppressTaskIntId": cfprApFaultSuppressTaskIntId,
       "cfprApFaultSuppressTaskName": cfprApFaultSuppressTaskName,
       "cfprApFaultSuppressTaskOperScheduler": cfprApFaultSuppressTaskOperScheduler,
       "cfprApFaultSuppressTaskOperState": cfprApFaultSuppressTaskOperState,
       "cfprApFaultSuppressTaskOperSuppressPolicyName": cfprApFaultSuppressTaskOperSuppressPolicyName,
       "cfprApFaultSuppressTaskPolicyLevel": cfprApFaultSuppressTaskPolicyLevel,
       "cfprApFaultSuppressTaskPolicyOwner": cfprApFaultSuppressTaskPolicyOwner,
       "cfprApFaultSuppressTaskScheduler": cfprApFaultSuppressTaskScheduler,
       "cfprApFaultSuppressTaskSuppressPolicyName": cfprApFaultSuppressTaskSuppressPolicyName}
)
