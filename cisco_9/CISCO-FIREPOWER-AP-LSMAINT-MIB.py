# SNMP MIB module (CISCO-FIREPOWER-AP-LSMAINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-LSMAINT-MIB.mib
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

(CfprApLsConfigIssues,
 CfprApLsmaintAckChangeDetails,
 CfprApLsmaintAckChanges,
 CfprApLsmaintAckDisr,
 CfprApLsmaintChangeMode,
 CfprApPolicyPolicyOwner,
 CfprApTrigAckMode,
 CfprApTrigAckOperState,
 CfprApTrigAckPrevOperState,
 CfprApTrigAdminState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApLsConfigIssues",
    "CfprApLsmaintAckChangeDetails",
    "CfprApLsmaintAckChanges",
    "CfprApLsmaintAckDisr",
    "CfprApLsmaintChangeMode",
    "CfprApPolicyPolicyOwner",
    "CfprApTrigAckMode",
    "CfprApTrigAckOperState",
    "CfprApTrigAckPrevOperState",
    "CfprApTrigAdminState")

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

cfprApLsmaintObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApLsmaintAckTable_Object = MibTable
cfprApLsmaintAckTable = _CfprApLsmaintAckTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1)
)
if mibBuilder.loadTexts:
    cfprApLsmaintAckTable.setStatus("current")
_CfprApLsmaintAckEntry_Object = MibTableRow
cfprApLsmaintAckEntry = _CfprApLsmaintAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1)
)
cfprApLsmaintAckEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSMAINT-MIB", "cfprApLsmaintAckInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsmaintAckEntry.setStatus("current")
_CfprApLsmaintAckInstanceId_Type = CfprApManagedObjectId
_CfprApLsmaintAckInstanceId_Object = MibTableColumn
cfprApLsmaintAckInstanceId = _CfprApLsmaintAckInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 1),
    _CfprApLsmaintAckInstanceId_Type()
)
cfprApLsmaintAckInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsmaintAckInstanceId.setStatus("current")
_CfprApLsmaintAckDn_Type = CfprApManagedObjectDn
_CfprApLsmaintAckDn_Object = MibTableColumn
cfprApLsmaintAckDn = _CfprApLsmaintAckDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 2),
    _CfprApLsmaintAckDn_Type()
)
cfprApLsmaintAckDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckDn.setStatus("current")
_CfprApLsmaintAckRn_Type = SnmpAdminString
_CfprApLsmaintAckRn_Object = MibTableColumn
cfprApLsmaintAckRn = _CfprApLsmaintAckRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 3),
    _CfprApLsmaintAckRn_Type()
)
cfprApLsmaintAckRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckRn.setStatus("current")
_CfprApLsmaintAckAcked_Type = DateAndTime
_CfprApLsmaintAckAcked_Object = MibTableColumn
cfprApLsmaintAckAcked = _CfprApLsmaintAckAcked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 4),
    _CfprApLsmaintAckAcked_Type()
)
cfprApLsmaintAckAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckAcked.setStatus("current")
_CfprApLsmaintAckAckedBy_Type = SnmpAdminString
_CfprApLsmaintAckAckedBy_Object = MibTableColumn
cfprApLsmaintAckAckedBy = _CfprApLsmaintAckAckedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 5),
    _CfprApLsmaintAckAckedBy_Type()
)
cfprApLsmaintAckAckedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckAckedBy.setStatus("current")
_CfprApLsmaintAckAdminState_Type = CfprApTrigAdminState
_CfprApLsmaintAckAdminState_Object = MibTableColumn
cfprApLsmaintAckAdminState = _CfprApLsmaintAckAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 6),
    _CfprApLsmaintAckAdminState_Type()
)
cfprApLsmaintAckAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckAdminState.setStatus("current")
_CfprApLsmaintAckAutoDelete_Type = TruthValue
_CfprApLsmaintAckAutoDelete_Object = MibTableColumn
cfprApLsmaintAckAutoDelete = _CfprApLsmaintAckAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 7),
    _CfprApLsmaintAckAutoDelete_Type()
)
cfprApLsmaintAckAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckAutoDelete.setStatus("current")
_CfprApLsmaintAckChangeBy_Type = SnmpAdminString
_CfprApLsmaintAckChangeBy_Object = MibTableColumn
cfprApLsmaintAckChangeBy = _CfprApLsmaintAckChangeBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 8),
    _CfprApLsmaintAckChangeBy_Type()
)
cfprApLsmaintAckChangeBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckChangeBy.setStatus("current")
_CfprApLsmaintAckChangeDetails_Type = CfprApLsmaintAckChangeDetails
_CfprApLsmaintAckChangeDetails_Object = MibTableColumn
cfprApLsmaintAckChangeDetails = _CfprApLsmaintAckChangeDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 9),
    _CfprApLsmaintAckChangeDetails_Type()
)
cfprApLsmaintAckChangeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckChangeDetails.setStatus("current")
_CfprApLsmaintAckChangeMode_Type = CfprApLsmaintChangeMode
_CfprApLsmaintAckChangeMode_Object = MibTableColumn
cfprApLsmaintAckChangeMode = _CfprApLsmaintAckChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 10),
    _CfprApLsmaintAckChangeMode_Type()
)
cfprApLsmaintAckChangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckChangeMode.setStatus("current")
_CfprApLsmaintAckChanges_Type = CfprApLsmaintAckChanges
_CfprApLsmaintAckChanges_Object = MibTableColumn
cfprApLsmaintAckChanges = _CfprApLsmaintAckChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 11),
    _CfprApLsmaintAckChanges_Type()
)
cfprApLsmaintAckChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckChanges.setStatus("current")
_CfprApLsmaintAckConfigIssues_Type = CfprApLsConfigIssues
_CfprApLsmaintAckConfigIssues_Object = MibTableColumn
cfprApLsmaintAckConfigIssues = _CfprApLsmaintAckConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 12),
    _CfprApLsmaintAckConfigIssues_Type()
)
cfprApLsmaintAckConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckConfigIssues.setStatus("current")
_CfprApLsmaintAckDeploymentMode_Type = CfprApTrigAckMode
_CfprApLsmaintAckDeploymentMode_Object = MibTableColumn
cfprApLsmaintAckDeploymentMode = _CfprApLsmaintAckDeploymentMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 13),
    _CfprApLsmaintAckDeploymentMode_Type()
)
cfprApLsmaintAckDeploymentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckDeploymentMode.setStatus("current")
_CfprApLsmaintAckDescr_Type = SnmpAdminString
_CfprApLsmaintAckDescr_Object = MibTableColumn
cfprApLsmaintAckDescr = _CfprApLsmaintAckDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 14),
    _CfprApLsmaintAckDescr_Type()
)
cfprApLsmaintAckDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckDescr.setStatus("current")
_CfprApLsmaintAckDisr_Type = CfprApLsmaintAckDisr
_CfprApLsmaintAckDisr_Object = MibTableColumn
cfprApLsmaintAckDisr = _CfprApLsmaintAckDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 15),
    _CfprApLsmaintAckDisr_Type()
)
cfprApLsmaintAckDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckDisr.setStatus("current")
_CfprApLsmaintAckIgnoreCap_Type = TruthValue
_CfprApLsmaintAckIgnoreCap_Object = MibTableColumn
cfprApLsmaintAckIgnoreCap = _CfprApLsmaintAckIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 16),
    _CfprApLsmaintAckIgnoreCap_Type()
)
cfprApLsmaintAckIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckIgnoreCap.setStatus("current")
_CfprApLsmaintAckIntId_Type = SnmpAdminString
_CfprApLsmaintAckIntId_Object = MibTableColumn
cfprApLsmaintAckIntId = _CfprApLsmaintAckIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 17),
    _CfprApLsmaintAckIntId_Type()
)
cfprApLsmaintAckIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckIntId.setStatus("current")
_CfprApLsmaintAckModified_Type = DateAndTime
_CfprApLsmaintAckModified_Object = MibTableColumn
cfprApLsmaintAckModified = _CfprApLsmaintAckModified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 18),
    _CfprApLsmaintAckModified_Type()
)
cfprApLsmaintAckModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckModified.setStatus("current")
_CfprApLsmaintAckName_Type = SnmpAdminString
_CfprApLsmaintAckName_Object = MibTableColumn
cfprApLsmaintAckName = _CfprApLsmaintAckName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 19),
    _CfprApLsmaintAckName_Type()
)
cfprApLsmaintAckName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckName.setStatus("current")
_CfprApLsmaintAckOldPnDn_Type = SnmpAdminString
_CfprApLsmaintAckOldPnDn_Object = MibTableColumn
cfprApLsmaintAckOldPnDn = _CfprApLsmaintAckOldPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 20),
    _CfprApLsmaintAckOldPnDn_Type()
)
cfprApLsmaintAckOldPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckOldPnDn.setStatus("current")
_CfprApLsmaintAckOperScheduler_Type = SnmpAdminString
_CfprApLsmaintAckOperScheduler_Object = MibTableColumn
cfprApLsmaintAckOperScheduler = _CfprApLsmaintAckOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 21),
    _CfprApLsmaintAckOperScheduler_Type()
)
cfprApLsmaintAckOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckOperScheduler.setStatus("current")
_CfprApLsmaintAckOperState_Type = CfprApTrigAckOperState
_CfprApLsmaintAckOperState_Object = MibTableColumn
cfprApLsmaintAckOperState = _CfprApLsmaintAckOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 22),
    _CfprApLsmaintAckOperState_Type()
)
cfprApLsmaintAckOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckOperState.setStatus("current")
_CfprApLsmaintAckPolicyLevel_Type = Gauge32
_CfprApLsmaintAckPolicyLevel_Object = MibTableColumn
cfprApLsmaintAckPolicyLevel = _CfprApLsmaintAckPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 23),
    _CfprApLsmaintAckPolicyLevel_Type()
)
cfprApLsmaintAckPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckPolicyLevel.setStatus("current")
_CfprApLsmaintAckPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApLsmaintAckPolicyOwner_Object = MibTableColumn
cfprApLsmaintAckPolicyOwner = _CfprApLsmaintAckPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 24),
    _CfprApLsmaintAckPolicyOwner_Type()
)
cfprApLsmaintAckPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckPolicyOwner.setStatus("current")
_CfprApLsmaintAckPrevOperState_Type = CfprApTrigAckPrevOperState
_CfprApLsmaintAckPrevOperState_Object = MibTableColumn
cfprApLsmaintAckPrevOperState = _CfprApLsmaintAckPrevOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 25),
    _CfprApLsmaintAckPrevOperState_Type()
)
cfprApLsmaintAckPrevOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckPrevOperState.setStatus("current")
_CfprApLsmaintAckScheduler_Type = SnmpAdminString
_CfprApLsmaintAckScheduler_Object = MibTableColumn
cfprApLsmaintAckScheduler = _CfprApLsmaintAckScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 1, 1, 26),
    _CfprApLsmaintAckScheduler_Type()
)
cfprApLsmaintAckScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintAckScheduler.setStatus("current")
_CfprApLsmaintMaintPolicyTable_Object = MibTable
cfprApLsmaintMaintPolicyTable = _CfprApLsmaintMaintPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2)
)
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicyTable.setStatus("current")
_CfprApLsmaintMaintPolicyEntry_Object = MibTableRow
cfprApLsmaintMaintPolicyEntry = _CfprApLsmaintMaintPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2, 1)
)
cfprApLsmaintMaintPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-LSMAINT-MIB", "cfprApLsmaintMaintPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicyEntry.setStatus("current")
_CfprApLsmaintMaintPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApLsmaintMaintPolicyInstanceId_Object = MibTableColumn
cfprApLsmaintMaintPolicyInstanceId = _CfprApLsmaintMaintPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2, 1, 1),
    _CfprApLsmaintMaintPolicyInstanceId_Type()
)
cfprApLsmaintMaintPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicyInstanceId.setStatus("current")
_CfprApLsmaintMaintPolicyDn_Type = CfprApManagedObjectDn
_CfprApLsmaintMaintPolicyDn_Object = MibTableColumn
cfprApLsmaintMaintPolicyDn = _CfprApLsmaintMaintPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2, 1, 2),
    _CfprApLsmaintMaintPolicyDn_Type()
)
cfprApLsmaintMaintPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicyDn.setStatus("current")
_CfprApLsmaintMaintPolicyRn_Type = SnmpAdminString
_CfprApLsmaintMaintPolicyRn_Object = MibTableColumn
cfprApLsmaintMaintPolicyRn = _CfprApLsmaintMaintPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2, 1, 3),
    _CfprApLsmaintMaintPolicyRn_Type()
)
cfprApLsmaintMaintPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicyRn.setStatus("current")
_CfprApLsmaintMaintPolicyDescr_Type = SnmpAdminString
_CfprApLsmaintMaintPolicyDescr_Object = MibTableColumn
cfprApLsmaintMaintPolicyDescr = _CfprApLsmaintMaintPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2, 1, 4),
    _CfprApLsmaintMaintPolicyDescr_Type()
)
cfprApLsmaintMaintPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicyDescr.setStatus("current")
_CfprApLsmaintMaintPolicyIntId_Type = SnmpAdminString
_CfprApLsmaintMaintPolicyIntId_Object = MibTableColumn
cfprApLsmaintMaintPolicyIntId = _CfprApLsmaintMaintPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2, 1, 5),
    _CfprApLsmaintMaintPolicyIntId_Type()
)
cfprApLsmaintMaintPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicyIntId.setStatus("current")
_CfprApLsmaintMaintPolicyName_Type = SnmpAdminString
_CfprApLsmaintMaintPolicyName_Object = MibTableColumn
cfprApLsmaintMaintPolicyName = _CfprApLsmaintMaintPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2, 1, 6),
    _CfprApLsmaintMaintPolicyName_Type()
)
cfprApLsmaintMaintPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicyName.setStatus("current")
_CfprApLsmaintMaintPolicyOperSchedName_Type = SnmpAdminString
_CfprApLsmaintMaintPolicyOperSchedName_Object = MibTableColumn
cfprApLsmaintMaintPolicyOperSchedName = _CfprApLsmaintMaintPolicyOperSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2, 1, 7),
    _CfprApLsmaintMaintPolicyOperSchedName_Type()
)
cfprApLsmaintMaintPolicyOperSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicyOperSchedName.setStatus("current")
_CfprApLsmaintMaintPolicyPolicyLevel_Type = Gauge32
_CfprApLsmaintMaintPolicyPolicyLevel_Object = MibTableColumn
cfprApLsmaintMaintPolicyPolicyLevel = _CfprApLsmaintMaintPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2, 1, 8),
    _CfprApLsmaintMaintPolicyPolicyLevel_Type()
)
cfprApLsmaintMaintPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicyPolicyLevel.setStatus("current")
_CfprApLsmaintMaintPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApLsmaintMaintPolicyPolicyOwner_Object = MibTableColumn
cfprApLsmaintMaintPolicyPolicyOwner = _CfprApLsmaintMaintPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2, 1, 9),
    _CfprApLsmaintMaintPolicyPolicyOwner_Type()
)
cfprApLsmaintMaintPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicyPolicyOwner.setStatus("current")
_CfprApLsmaintMaintPolicySchedName_Type = SnmpAdminString
_CfprApLsmaintMaintPolicySchedName_Object = MibTableColumn
cfprApLsmaintMaintPolicySchedName = _CfprApLsmaintMaintPolicySchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2, 1, 10),
    _CfprApLsmaintMaintPolicySchedName_Type()
)
cfprApLsmaintMaintPolicySchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicySchedName.setStatus("current")
_CfprApLsmaintMaintPolicyUptimeDisr_Type = CfprApTrigAckMode
_CfprApLsmaintMaintPolicyUptimeDisr_Object = MibTableColumn
cfprApLsmaintMaintPolicyUptimeDisr = _CfprApLsmaintMaintPolicyUptimeDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 48, 2, 1, 11),
    _CfprApLsmaintMaintPolicyUptimeDisr_Type()
)
cfprApLsmaintMaintPolicyUptimeDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApLsmaintMaintPolicyUptimeDisr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-LSMAINT-MIB",
    **{"cfprApLsmaintObjects": cfprApLsmaintObjects,
       "cfprApLsmaintAckTable": cfprApLsmaintAckTable,
       "cfprApLsmaintAckEntry": cfprApLsmaintAckEntry,
       "cfprApLsmaintAckInstanceId": cfprApLsmaintAckInstanceId,
       "cfprApLsmaintAckDn": cfprApLsmaintAckDn,
       "cfprApLsmaintAckRn": cfprApLsmaintAckRn,
       "cfprApLsmaintAckAcked": cfprApLsmaintAckAcked,
       "cfprApLsmaintAckAckedBy": cfprApLsmaintAckAckedBy,
       "cfprApLsmaintAckAdminState": cfprApLsmaintAckAdminState,
       "cfprApLsmaintAckAutoDelete": cfprApLsmaintAckAutoDelete,
       "cfprApLsmaintAckChangeBy": cfprApLsmaintAckChangeBy,
       "cfprApLsmaintAckChangeDetails": cfprApLsmaintAckChangeDetails,
       "cfprApLsmaintAckChangeMode": cfprApLsmaintAckChangeMode,
       "cfprApLsmaintAckChanges": cfprApLsmaintAckChanges,
       "cfprApLsmaintAckConfigIssues": cfprApLsmaintAckConfigIssues,
       "cfprApLsmaintAckDeploymentMode": cfprApLsmaintAckDeploymentMode,
       "cfprApLsmaintAckDescr": cfprApLsmaintAckDescr,
       "cfprApLsmaintAckDisr": cfprApLsmaintAckDisr,
       "cfprApLsmaintAckIgnoreCap": cfprApLsmaintAckIgnoreCap,
       "cfprApLsmaintAckIntId": cfprApLsmaintAckIntId,
       "cfprApLsmaintAckModified": cfprApLsmaintAckModified,
       "cfprApLsmaintAckName": cfprApLsmaintAckName,
       "cfprApLsmaintAckOldPnDn": cfprApLsmaintAckOldPnDn,
       "cfprApLsmaintAckOperScheduler": cfprApLsmaintAckOperScheduler,
       "cfprApLsmaintAckOperState": cfprApLsmaintAckOperState,
       "cfprApLsmaintAckPolicyLevel": cfprApLsmaintAckPolicyLevel,
       "cfprApLsmaintAckPolicyOwner": cfprApLsmaintAckPolicyOwner,
       "cfprApLsmaintAckPrevOperState": cfprApLsmaintAckPrevOperState,
       "cfprApLsmaintAckScheduler": cfprApLsmaintAckScheduler,
       "cfprApLsmaintMaintPolicyTable": cfprApLsmaintMaintPolicyTable,
       "cfprApLsmaintMaintPolicyEntry": cfprApLsmaintMaintPolicyEntry,
       "cfprApLsmaintMaintPolicyInstanceId": cfprApLsmaintMaintPolicyInstanceId,
       "cfprApLsmaintMaintPolicyDn": cfprApLsmaintMaintPolicyDn,
       "cfprApLsmaintMaintPolicyRn": cfprApLsmaintMaintPolicyRn,
       "cfprApLsmaintMaintPolicyDescr": cfprApLsmaintMaintPolicyDescr,
       "cfprApLsmaintMaintPolicyIntId": cfprApLsmaintMaintPolicyIntId,
       "cfprApLsmaintMaintPolicyName": cfprApLsmaintMaintPolicyName,
       "cfprApLsmaintMaintPolicyOperSchedName": cfprApLsmaintMaintPolicyOperSchedName,
       "cfprApLsmaintMaintPolicyPolicyLevel": cfprApLsmaintMaintPolicyPolicyLevel,
       "cfprApLsmaintMaintPolicyPolicyOwner": cfprApLsmaintMaintPolicyPolicyOwner,
       "cfprApLsmaintMaintPolicySchedName": cfprApLsmaintMaintPolicySchedName,
       "cfprApLsmaintMaintPolicyUptimeDisr": cfprApLsmaintMaintPolicyUptimeDisr}
)
