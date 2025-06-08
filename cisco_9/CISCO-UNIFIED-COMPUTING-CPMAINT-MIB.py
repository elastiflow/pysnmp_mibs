# SNMP MIB module (CISCO-UNIFIED-COMPUTING-CPMAINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-UNIFIED-COMPUTING-CPMAINT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 08:58:45 2025
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

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsCpmaintAckChangeDetails,
 CucsCpmaintAckChanges,
 CucsCpmaintAckDisr,
 CucsCpmaintChangeMode,
 CucsEquipmentChassisConfigIssues,
 CucsPolicyPolicyOwner,
 CucsTrigAckOperState,
 CucsTrigAckPrevOperState,
 CucsTrigAdminState,
 CucsTrigChassisAckMode,
 CucsTrigTrigState,
 CucsTrigTrigger) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsCpmaintAckChangeDetails",
    "CucsCpmaintAckChanges",
    "CucsCpmaintAckDisr",
    "CucsCpmaintChangeMode",
    "CucsEquipmentChassisConfigIssues",
    "CucsPolicyPolicyOwner",
    "CucsTrigAckOperState",
    "CucsTrigAckPrevOperState",
    "CucsTrigAdminState",
    "CucsTrigChassisAckMode",
    "CucsTrigTrigState",
    "CucsTrigTrigger")

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

cucsCpmaintObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsCpmaintAckTable_Object = MibTable
cucsCpmaintAckTable = _CucsCpmaintAckTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1)
)
if mibBuilder.loadTexts:
    cucsCpmaintAckTable.setStatus("current")
_CucsCpmaintAckEntry_Object = MibTableRow
cucsCpmaintAckEntry = _CucsCpmaintAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1)
)
cucsCpmaintAckEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CPMAINT-MIB", "cucsCpmaintAckInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCpmaintAckEntry.setStatus("current")
_CucsCpmaintAckInstanceId_Type = CucsManagedObjectId
_CucsCpmaintAckInstanceId_Object = MibTableColumn
cucsCpmaintAckInstanceId = _CucsCpmaintAckInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 1),
    _CucsCpmaintAckInstanceId_Type()
)
cucsCpmaintAckInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCpmaintAckInstanceId.setStatus("current")
_CucsCpmaintAckDn_Type = CucsManagedObjectDn
_CucsCpmaintAckDn_Object = MibTableColumn
cucsCpmaintAckDn = _CucsCpmaintAckDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 2),
    _CucsCpmaintAckDn_Type()
)
cucsCpmaintAckDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckDn.setStatus("current")
_CucsCpmaintAckRn_Type = SnmpAdminString
_CucsCpmaintAckRn_Object = MibTableColumn
cucsCpmaintAckRn = _CucsCpmaintAckRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 3),
    _CucsCpmaintAckRn_Type()
)
cucsCpmaintAckRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckRn.setStatus("current")
_CucsCpmaintAckAcked_Type = DateAndTime
_CucsCpmaintAckAcked_Object = MibTableColumn
cucsCpmaintAckAcked = _CucsCpmaintAckAcked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 4),
    _CucsCpmaintAckAcked_Type()
)
cucsCpmaintAckAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckAcked.setStatus("current")
_CucsCpmaintAckAckedBy_Type = SnmpAdminString
_CucsCpmaintAckAckedBy_Object = MibTableColumn
cucsCpmaintAckAckedBy = _CucsCpmaintAckAckedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 5),
    _CucsCpmaintAckAckedBy_Type()
)
cucsCpmaintAckAckedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckAckedBy.setStatus("current")
_CucsCpmaintAckAdminState_Type = CucsTrigAdminState
_CucsCpmaintAckAdminState_Object = MibTableColumn
cucsCpmaintAckAdminState = _CucsCpmaintAckAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 6),
    _CucsCpmaintAckAdminState_Type()
)
cucsCpmaintAckAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckAdminState.setStatus("current")
_CucsCpmaintAckAutoDelete_Type = TruthValue
_CucsCpmaintAckAutoDelete_Object = MibTableColumn
cucsCpmaintAckAutoDelete = _CucsCpmaintAckAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 7),
    _CucsCpmaintAckAutoDelete_Type()
)
cucsCpmaintAckAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckAutoDelete.setStatus("current")
_CucsCpmaintAckChangeBy_Type = SnmpAdminString
_CucsCpmaintAckChangeBy_Object = MibTableColumn
cucsCpmaintAckChangeBy = _CucsCpmaintAckChangeBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 8),
    _CucsCpmaintAckChangeBy_Type()
)
cucsCpmaintAckChangeBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckChangeBy.setStatus("current")
_CucsCpmaintAckChangeDetails_Type = CucsCpmaintAckChangeDetails
_CucsCpmaintAckChangeDetails_Object = MibTableColumn
cucsCpmaintAckChangeDetails = _CucsCpmaintAckChangeDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 9),
    _CucsCpmaintAckChangeDetails_Type()
)
cucsCpmaintAckChangeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckChangeDetails.setStatus("current")
_CucsCpmaintAckChangeMode_Type = CucsCpmaintChangeMode
_CucsCpmaintAckChangeMode_Object = MibTableColumn
cucsCpmaintAckChangeMode = _CucsCpmaintAckChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 10),
    _CucsCpmaintAckChangeMode_Type()
)
cucsCpmaintAckChangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckChangeMode.setStatus("current")
_CucsCpmaintAckChanges_Type = CucsCpmaintAckChanges
_CucsCpmaintAckChanges_Object = MibTableColumn
cucsCpmaintAckChanges = _CucsCpmaintAckChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 11),
    _CucsCpmaintAckChanges_Type()
)
cucsCpmaintAckChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckChanges.setStatus("current")
_CucsCpmaintAckConfigIssues_Type = CucsEquipmentChassisConfigIssues
_CucsCpmaintAckConfigIssues_Object = MibTableColumn
cucsCpmaintAckConfigIssues = _CucsCpmaintAckConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 12),
    _CucsCpmaintAckConfigIssues_Type()
)
cucsCpmaintAckConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckConfigIssues.setStatus("current")
_CucsCpmaintAckDeploymentMode_Type = CucsTrigChassisAckMode
_CucsCpmaintAckDeploymentMode_Object = MibTableColumn
cucsCpmaintAckDeploymentMode = _CucsCpmaintAckDeploymentMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 13),
    _CucsCpmaintAckDeploymentMode_Type()
)
cucsCpmaintAckDeploymentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckDeploymentMode.setStatus("current")
_CucsCpmaintAckDescr_Type = SnmpAdminString
_CucsCpmaintAckDescr_Object = MibTableColumn
cucsCpmaintAckDescr = _CucsCpmaintAckDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 14),
    _CucsCpmaintAckDescr_Type()
)
cucsCpmaintAckDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckDescr.setStatus("current")
_CucsCpmaintAckDisr_Type = CucsCpmaintAckDisr
_CucsCpmaintAckDisr_Object = MibTableColumn
cucsCpmaintAckDisr = _CucsCpmaintAckDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 15),
    _CucsCpmaintAckDisr_Type()
)
cucsCpmaintAckDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckDisr.setStatus("current")
_CucsCpmaintAckIgnoreCap_Type = TruthValue
_CucsCpmaintAckIgnoreCap_Object = MibTableColumn
cucsCpmaintAckIgnoreCap = _CucsCpmaintAckIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 16),
    _CucsCpmaintAckIgnoreCap_Type()
)
cucsCpmaintAckIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckIgnoreCap.setStatus("current")
_CucsCpmaintAckIntId_Type = SnmpAdminString
_CucsCpmaintAckIntId_Object = MibTableColumn
cucsCpmaintAckIntId = _CucsCpmaintAckIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 17),
    _CucsCpmaintAckIntId_Type()
)
cucsCpmaintAckIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckIntId.setStatus("current")
_CucsCpmaintAckModified_Type = DateAndTime
_CucsCpmaintAckModified_Object = MibTableColumn
cucsCpmaintAckModified = _CucsCpmaintAckModified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 18),
    _CucsCpmaintAckModified_Type()
)
cucsCpmaintAckModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckModified.setStatus("current")
_CucsCpmaintAckName_Type = SnmpAdminString
_CucsCpmaintAckName_Object = MibTableColumn
cucsCpmaintAckName = _CucsCpmaintAckName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 19),
    _CucsCpmaintAckName_Type()
)
cucsCpmaintAckName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckName.setStatus("current")
_CucsCpmaintAckOldChassisDn_Type = SnmpAdminString
_CucsCpmaintAckOldChassisDn_Object = MibTableColumn
cucsCpmaintAckOldChassisDn = _CucsCpmaintAckOldChassisDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 20),
    _CucsCpmaintAckOldChassisDn_Type()
)
cucsCpmaintAckOldChassisDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckOldChassisDn.setStatus("current")
_CucsCpmaintAckOperScheduler_Type = SnmpAdminString
_CucsCpmaintAckOperScheduler_Object = MibTableColumn
cucsCpmaintAckOperScheduler = _CucsCpmaintAckOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 21),
    _CucsCpmaintAckOperScheduler_Type()
)
cucsCpmaintAckOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckOperScheduler.setStatus("current")
_CucsCpmaintAckOperState_Type = CucsTrigAckOperState
_CucsCpmaintAckOperState_Object = MibTableColumn
cucsCpmaintAckOperState = _CucsCpmaintAckOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 22),
    _CucsCpmaintAckOperState_Type()
)
cucsCpmaintAckOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckOperState.setStatus("current")
_CucsCpmaintAckPolicyLevel_Type = Gauge32
_CucsCpmaintAckPolicyLevel_Object = MibTableColumn
cucsCpmaintAckPolicyLevel = _CucsCpmaintAckPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 23),
    _CucsCpmaintAckPolicyLevel_Type()
)
cucsCpmaintAckPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckPolicyLevel.setStatus("current")
_CucsCpmaintAckPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCpmaintAckPolicyOwner_Object = MibTableColumn
cucsCpmaintAckPolicyOwner = _CucsCpmaintAckPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 24),
    _CucsCpmaintAckPolicyOwner_Type()
)
cucsCpmaintAckPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckPolicyOwner.setStatus("current")
_CucsCpmaintAckPrevOperState_Type = CucsTrigAckPrevOperState
_CucsCpmaintAckPrevOperState_Object = MibTableColumn
cucsCpmaintAckPrevOperState = _CucsCpmaintAckPrevOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 25),
    _CucsCpmaintAckPrevOperState_Type()
)
cucsCpmaintAckPrevOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckPrevOperState.setStatus("current")
_CucsCpmaintAckScheduler_Type = SnmpAdminString
_CucsCpmaintAckScheduler_Object = MibTableColumn
cucsCpmaintAckScheduler = _CucsCpmaintAckScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 26),
    _CucsCpmaintAckScheduler_Type()
)
cucsCpmaintAckScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckScheduler.setStatus("current")
_CucsCpmaintAckTriggerConfigState_Type = CucsTrigTrigState
_CucsCpmaintAckTriggerConfigState_Object = MibTableColumn
cucsCpmaintAckTriggerConfigState = _CucsCpmaintAckTriggerConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 27),
    _CucsCpmaintAckTriggerConfigState_Type()
)
cucsCpmaintAckTriggerConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckTriggerConfigState.setStatus("current")
_CucsCpmaintAckPropAcl_Type = Unsigned64
_CucsCpmaintAckPropAcl_Object = MibTableColumn
cucsCpmaintAckPropAcl = _CucsCpmaintAckPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 1, 1, 28),
    _CucsCpmaintAckPropAcl_Type()
)
cucsCpmaintAckPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintAckPropAcl.setStatus("current")
_CucsCpmaintMaintPolicyTable_Object = MibTable
cucsCpmaintMaintPolicyTable = _CucsCpmaintMaintPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2)
)
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyTable.setStatus("current")
_CucsCpmaintMaintPolicyEntry_Object = MibTableRow
cucsCpmaintMaintPolicyEntry = _CucsCpmaintMaintPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1)
)
cucsCpmaintMaintPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CPMAINT-MIB", "cucsCpmaintMaintPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyEntry.setStatus("current")
_CucsCpmaintMaintPolicyInstanceId_Type = CucsManagedObjectId
_CucsCpmaintMaintPolicyInstanceId_Object = MibTableColumn
cucsCpmaintMaintPolicyInstanceId = _CucsCpmaintMaintPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1, 1),
    _CucsCpmaintMaintPolicyInstanceId_Type()
)
cucsCpmaintMaintPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyInstanceId.setStatus("current")
_CucsCpmaintMaintPolicyDn_Type = CucsManagedObjectDn
_CucsCpmaintMaintPolicyDn_Object = MibTableColumn
cucsCpmaintMaintPolicyDn = _CucsCpmaintMaintPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1, 2),
    _CucsCpmaintMaintPolicyDn_Type()
)
cucsCpmaintMaintPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyDn.setStatus("current")
_CucsCpmaintMaintPolicyRn_Type = SnmpAdminString
_CucsCpmaintMaintPolicyRn_Object = MibTableColumn
cucsCpmaintMaintPolicyRn = _CucsCpmaintMaintPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1, 3),
    _CucsCpmaintMaintPolicyRn_Type()
)
cucsCpmaintMaintPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyRn.setStatus("current")
_CucsCpmaintMaintPolicyDescr_Type = SnmpAdminString
_CucsCpmaintMaintPolicyDescr_Object = MibTableColumn
cucsCpmaintMaintPolicyDescr = _CucsCpmaintMaintPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1, 4),
    _CucsCpmaintMaintPolicyDescr_Type()
)
cucsCpmaintMaintPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyDescr.setStatus("current")
_CucsCpmaintMaintPolicyIntId_Type = SnmpAdminString
_CucsCpmaintMaintPolicyIntId_Object = MibTableColumn
cucsCpmaintMaintPolicyIntId = _CucsCpmaintMaintPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1, 5),
    _CucsCpmaintMaintPolicyIntId_Type()
)
cucsCpmaintMaintPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyIntId.setStatus("current")
_CucsCpmaintMaintPolicyName_Type = SnmpAdminString
_CucsCpmaintMaintPolicyName_Object = MibTableColumn
cucsCpmaintMaintPolicyName = _CucsCpmaintMaintPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1, 6),
    _CucsCpmaintMaintPolicyName_Type()
)
cucsCpmaintMaintPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyName.setStatus("current")
_CucsCpmaintMaintPolicyOperSchedName_Type = SnmpAdminString
_CucsCpmaintMaintPolicyOperSchedName_Object = MibTableColumn
cucsCpmaintMaintPolicyOperSchedName = _CucsCpmaintMaintPolicyOperSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1, 7),
    _CucsCpmaintMaintPolicyOperSchedName_Type()
)
cucsCpmaintMaintPolicyOperSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyOperSchedName.setStatus("current")
_CucsCpmaintMaintPolicyPolicyLevel_Type = Gauge32
_CucsCpmaintMaintPolicyPolicyLevel_Object = MibTableColumn
cucsCpmaintMaintPolicyPolicyLevel = _CucsCpmaintMaintPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1, 8),
    _CucsCpmaintMaintPolicyPolicyLevel_Type()
)
cucsCpmaintMaintPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyPolicyLevel.setStatus("current")
_CucsCpmaintMaintPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCpmaintMaintPolicyPolicyOwner_Object = MibTableColumn
cucsCpmaintMaintPolicyPolicyOwner = _CucsCpmaintMaintPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1, 9),
    _CucsCpmaintMaintPolicyPolicyOwner_Type()
)
cucsCpmaintMaintPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyPolicyOwner.setStatus("current")
_CucsCpmaintMaintPolicySchedName_Type = SnmpAdminString
_CucsCpmaintMaintPolicySchedName_Object = MibTableColumn
cucsCpmaintMaintPolicySchedName = _CucsCpmaintMaintPolicySchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1, 10),
    _CucsCpmaintMaintPolicySchedName_Type()
)
cucsCpmaintMaintPolicySchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicySchedName.setStatus("current")
_CucsCpmaintMaintPolicyTriggerConfig_Type = CucsTrigTrigger
_CucsCpmaintMaintPolicyTriggerConfig_Object = MibTableColumn
cucsCpmaintMaintPolicyTriggerConfig = _CucsCpmaintMaintPolicyTriggerConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1, 11),
    _CucsCpmaintMaintPolicyTriggerConfig_Type()
)
cucsCpmaintMaintPolicyTriggerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyTriggerConfig.setStatus("current")
_CucsCpmaintMaintPolicyUptimeDisr_Type = CucsTrigChassisAckMode
_CucsCpmaintMaintPolicyUptimeDisr_Object = MibTableColumn
cucsCpmaintMaintPolicyUptimeDisr = _CucsCpmaintMaintPolicyUptimeDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 93, 2, 1, 12),
    _CucsCpmaintMaintPolicyUptimeDisr_Type()
)
cucsCpmaintMaintPolicyUptimeDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCpmaintMaintPolicyUptimeDisr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-CPMAINT-MIB",
    **{"cucsCpmaintObjects": cucsCpmaintObjects,
       "cucsCpmaintAckTable": cucsCpmaintAckTable,
       "cucsCpmaintAckEntry": cucsCpmaintAckEntry,
       "cucsCpmaintAckInstanceId": cucsCpmaintAckInstanceId,
       "cucsCpmaintAckDn": cucsCpmaintAckDn,
       "cucsCpmaintAckRn": cucsCpmaintAckRn,
       "cucsCpmaintAckAcked": cucsCpmaintAckAcked,
       "cucsCpmaintAckAckedBy": cucsCpmaintAckAckedBy,
       "cucsCpmaintAckAdminState": cucsCpmaintAckAdminState,
       "cucsCpmaintAckAutoDelete": cucsCpmaintAckAutoDelete,
       "cucsCpmaintAckChangeBy": cucsCpmaintAckChangeBy,
       "cucsCpmaintAckChangeDetails": cucsCpmaintAckChangeDetails,
       "cucsCpmaintAckChangeMode": cucsCpmaintAckChangeMode,
       "cucsCpmaintAckChanges": cucsCpmaintAckChanges,
       "cucsCpmaintAckConfigIssues": cucsCpmaintAckConfigIssues,
       "cucsCpmaintAckDeploymentMode": cucsCpmaintAckDeploymentMode,
       "cucsCpmaintAckDescr": cucsCpmaintAckDescr,
       "cucsCpmaintAckDisr": cucsCpmaintAckDisr,
       "cucsCpmaintAckIgnoreCap": cucsCpmaintAckIgnoreCap,
       "cucsCpmaintAckIntId": cucsCpmaintAckIntId,
       "cucsCpmaintAckModified": cucsCpmaintAckModified,
       "cucsCpmaintAckName": cucsCpmaintAckName,
       "cucsCpmaintAckOldChassisDn": cucsCpmaintAckOldChassisDn,
       "cucsCpmaintAckOperScheduler": cucsCpmaintAckOperScheduler,
       "cucsCpmaintAckOperState": cucsCpmaintAckOperState,
       "cucsCpmaintAckPolicyLevel": cucsCpmaintAckPolicyLevel,
       "cucsCpmaintAckPolicyOwner": cucsCpmaintAckPolicyOwner,
       "cucsCpmaintAckPrevOperState": cucsCpmaintAckPrevOperState,
       "cucsCpmaintAckScheduler": cucsCpmaintAckScheduler,
       "cucsCpmaintAckTriggerConfigState": cucsCpmaintAckTriggerConfigState,
       "cucsCpmaintAckPropAcl": cucsCpmaintAckPropAcl,
       "cucsCpmaintMaintPolicyTable": cucsCpmaintMaintPolicyTable,
       "cucsCpmaintMaintPolicyEntry": cucsCpmaintMaintPolicyEntry,
       "cucsCpmaintMaintPolicyInstanceId": cucsCpmaintMaintPolicyInstanceId,
       "cucsCpmaintMaintPolicyDn": cucsCpmaintMaintPolicyDn,
       "cucsCpmaintMaintPolicyRn": cucsCpmaintMaintPolicyRn,
       "cucsCpmaintMaintPolicyDescr": cucsCpmaintMaintPolicyDescr,
       "cucsCpmaintMaintPolicyIntId": cucsCpmaintMaintPolicyIntId,
       "cucsCpmaintMaintPolicyName": cucsCpmaintMaintPolicyName,
       "cucsCpmaintMaintPolicyOperSchedName": cucsCpmaintMaintPolicyOperSchedName,
       "cucsCpmaintMaintPolicyPolicyLevel": cucsCpmaintMaintPolicyPolicyLevel,
       "cucsCpmaintMaintPolicyPolicyOwner": cucsCpmaintMaintPolicyPolicyOwner,
       "cucsCpmaintMaintPolicySchedName": cucsCpmaintMaintPolicySchedName,
       "cucsCpmaintMaintPolicyTriggerConfig": cucsCpmaintMaintPolicyTriggerConfig,
       "cucsCpmaintMaintPolicyUptimeDisr": cucsCpmaintMaintPolicyUptimeDisr}
)
