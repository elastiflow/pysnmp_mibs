# SNMP MIB module (CISCO-FIREPOWER-LSMAINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-LSMAINT-MIB.mib
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

(CfprLsConfigIssues,
 CfprLsmaintAckChangeDetails,
 CfprLsmaintAckChanges,
 CfprLsmaintAckDisr,
 CfprLsmaintChangeMode,
 CfprPolicyPolicyOwner,
 CfprTrigAckMode,
 CfprTrigAckOperState,
 CfprTrigAckPrevOperState,
 CfprTrigAdminState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprLsConfigIssues",
    "CfprLsmaintAckChangeDetails",
    "CfprLsmaintAckChanges",
    "CfprLsmaintAckDisr",
    "CfprLsmaintChangeMode",
    "CfprPolicyPolicyOwner",
    "CfprTrigAckMode",
    "CfprTrigAckOperState",
    "CfprTrigAckPrevOperState",
    "CfprTrigAdminState")

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

cfprLsmaintObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprLsmaintAckTable_Object = MibTable
cfprLsmaintAckTable = _CfprLsmaintAckTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1)
)
if mibBuilder.loadTexts:
    cfprLsmaintAckTable.setStatus("current")
_CfprLsmaintAckEntry_Object = MibTableRow
cfprLsmaintAckEntry = _CfprLsmaintAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1)
)
cfprLsmaintAckEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSMAINT-MIB", "cfprLsmaintAckInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsmaintAckEntry.setStatus("current")
_CfprLsmaintAckInstanceId_Type = CfprManagedObjectId
_CfprLsmaintAckInstanceId_Object = MibTableColumn
cfprLsmaintAckInstanceId = _CfprLsmaintAckInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 1),
    _CfprLsmaintAckInstanceId_Type()
)
cfprLsmaintAckInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsmaintAckInstanceId.setStatus("current")
_CfprLsmaintAckDn_Type = CfprManagedObjectDn
_CfprLsmaintAckDn_Object = MibTableColumn
cfprLsmaintAckDn = _CfprLsmaintAckDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 2),
    _CfprLsmaintAckDn_Type()
)
cfprLsmaintAckDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckDn.setStatus("current")
_CfprLsmaintAckRn_Type = SnmpAdminString
_CfprLsmaintAckRn_Object = MibTableColumn
cfprLsmaintAckRn = _CfprLsmaintAckRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 3),
    _CfprLsmaintAckRn_Type()
)
cfprLsmaintAckRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckRn.setStatus("current")
_CfprLsmaintAckAcked_Type = DateAndTime
_CfprLsmaintAckAcked_Object = MibTableColumn
cfprLsmaintAckAcked = _CfprLsmaintAckAcked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 4),
    _CfprLsmaintAckAcked_Type()
)
cfprLsmaintAckAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckAcked.setStatus("current")
_CfprLsmaintAckAckedBy_Type = SnmpAdminString
_CfprLsmaintAckAckedBy_Object = MibTableColumn
cfprLsmaintAckAckedBy = _CfprLsmaintAckAckedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 5),
    _CfprLsmaintAckAckedBy_Type()
)
cfprLsmaintAckAckedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckAckedBy.setStatus("current")
_CfprLsmaintAckAdminState_Type = CfprTrigAdminState
_CfprLsmaintAckAdminState_Object = MibTableColumn
cfprLsmaintAckAdminState = _CfprLsmaintAckAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 6),
    _CfprLsmaintAckAdminState_Type()
)
cfprLsmaintAckAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckAdminState.setStatus("current")
_CfprLsmaintAckAutoDelete_Type = TruthValue
_CfprLsmaintAckAutoDelete_Object = MibTableColumn
cfprLsmaintAckAutoDelete = _CfprLsmaintAckAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 7),
    _CfprLsmaintAckAutoDelete_Type()
)
cfprLsmaintAckAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckAutoDelete.setStatus("current")
_CfprLsmaintAckChangeBy_Type = SnmpAdminString
_CfprLsmaintAckChangeBy_Object = MibTableColumn
cfprLsmaintAckChangeBy = _CfprLsmaintAckChangeBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 8),
    _CfprLsmaintAckChangeBy_Type()
)
cfprLsmaintAckChangeBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckChangeBy.setStatus("current")
_CfprLsmaintAckChangeDetails_Type = CfprLsmaintAckChangeDetails
_CfprLsmaintAckChangeDetails_Object = MibTableColumn
cfprLsmaintAckChangeDetails = _CfprLsmaintAckChangeDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 9),
    _CfprLsmaintAckChangeDetails_Type()
)
cfprLsmaintAckChangeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckChangeDetails.setStatus("current")
_CfprLsmaintAckChangeMode_Type = CfprLsmaintChangeMode
_CfprLsmaintAckChangeMode_Object = MibTableColumn
cfprLsmaintAckChangeMode = _CfprLsmaintAckChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 10),
    _CfprLsmaintAckChangeMode_Type()
)
cfprLsmaintAckChangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckChangeMode.setStatus("current")
_CfprLsmaintAckChanges_Type = CfprLsmaintAckChanges
_CfprLsmaintAckChanges_Object = MibTableColumn
cfprLsmaintAckChanges = _CfprLsmaintAckChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 11),
    _CfprLsmaintAckChanges_Type()
)
cfprLsmaintAckChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckChanges.setStatus("current")
_CfprLsmaintAckConfigIssues_Type = CfprLsConfigIssues
_CfprLsmaintAckConfigIssues_Object = MibTableColumn
cfprLsmaintAckConfigIssues = _CfprLsmaintAckConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 12),
    _CfprLsmaintAckConfigIssues_Type()
)
cfprLsmaintAckConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckConfigIssues.setStatus("current")
_CfprLsmaintAckDeploymentMode_Type = CfprTrigAckMode
_CfprLsmaintAckDeploymentMode_Object = MibTableColumn
cfprLsmaintAckDeploymentMode = _CfprLsmaintAckDeploymentMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 13),
    _CfprLsmaintAckDeploymentMode_Type()
)
cfprLsmaintAckDeploymentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckDeploymentMode.setStatus("current")
_CfprLsmaintAckDescr_Type = SnmpAdminString
_CfprLsmaintAckDescr_Object = MibTableColumn
cfprLsmaintAckDescr = _CfprLsmaintAckDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 14),
    _CfprLsmaintAckDescr_Type()
)
cfprLsmaintAckDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckDescr.setStatus("current")
_CfprLsmaintAckDisr_Type = CfprLsmaintAckDisr
_CfprLsmaintAckDisr_Object = MibTableColumn
cfprLsmaintAckDisr = _CfprLsmaintAckDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 15),
    _CfprLsmaintAckDisr_Type()
)
cfprLsmaintAckDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckDisr.setStatus("current")
_CfprLsmaintAckIgnoreCap_Type = TruthValue
_CfprLsmaintAckIgnoreCap_Object = MibTableColumn
cfprLsmaintAckIgnoreCap = _CfprLsmaintAckIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 16),
    _CfprLsmaintAckIgnoreCap_Type()
)
cfprLsmaintAckIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckIgnoreCap.setStatus("current")
_CfprLsmaintAckIntId_Type = SnmpAdminString
_CfprLsmaintAckIntId_Object = MibTableColumn
cfprLsmaintAckIntId = _CfprLsmaintAckIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 17),
    _CfprLsmaintAckIntId_Type()
)
cfprLsmaintAckIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckIntId.setStatus("current")
_CfprLsmaintAckModified_Type = DateAndTime
_CfprLsmaintAckModified_Object = MibTableColumn
cfprLsmaintAckModified = _CfprLsmaintAckModified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 18),
    _CfprLsmaintAckModified_Type()
)
cfprLsmaintAckModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckModified.setStatus("current")
_CfprLsmaintAckName_Type = SnmpAdminString
_CfprLsmaintAckName_Object = MibTableColumn
cfprLsmaintAckName = _CfprLsmaintAckName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 19),
    _CfprLsmaintAckName_Type()
)
cfprLsmaintAckName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckName.setStatus("current")
_CfprLsmaintAckOldPnDn_Type = SnmpAdminString
_CfprLsmaintAckOldPnDn_Object = MibTableColumn
cfprLsmaintAckOldPnDn = _CfprLsmaintAckOldPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 20),
    _CfprLsmaintAckOldPnDn_Type()
)
cfprLsmaintAckOldPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckOldPnDn.setStatus("current")
_CfprLsmaintAckOperScheduler_Type = SnmpAdminString
_CfprLsmaintAckOperScheduler_Object = MibTableColumn
cfprLsmaintAckOperScheduler = _CfprLsmaintAckOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 21),
    _CfprLsmaintAckOperScheduler_Type()
)
cfprLsmaintAckOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckOperScheduler.setStatus("current")
_CfprLsmaintAckOperState_Type = CfprTrigAckOperState
_CfprLsmaintAckOperState_Object = MibTableColumn
cfprLsmaintAckOperState = _CfprLsmaintAckOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 22),
    _CfprLsmaintAckOperState_Type()
)
cfprLsmaintAckOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckOperState.setStatus("current")
_CfprLsmaintAckPolicyLevel_Type = Gauge32
_CfprLsmaintAckPolicyLevel_Object = MibTableColumn
cfprLsmaintAckPolicyLevel = _CfprLsmaintAckPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 23),
    _CfprLsmaintAckPolicyLevel_Type()
)
cfprLsmaintAckPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckPolicyLevel.setStatus("current")
_CfprLsmaintAckPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprLsmaintAckPolicyOwner_Object = MibTableColumn
cfprLsmaintAckPolicyOwner = _CfprLsmaintAckPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 24),
    _CfprLsmaintAckPolicyOwner_Type()
)
cfprLsmaintAckPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckPolicyOwner.setStatus("current")
_CfprLsmaintAckPrevOperState_Type = CfprTrigAckPrevOperState
_CfprLsmaintAckPrevOperState_Object = MibTableColumn
cfprLsmaintAckPrevOperState = _CfprLsmaintAckPrevOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 25),
    _CfprLsmaintAckPrevOperState_Type()
)
cfprLsmaintAckPrevOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckPrevOperState.setStatus("current")
_CfprLsmaintAckScheduler_Type = SnmpAdminString
_CfprLsmaintAckScheduler_Object = MibTableColumn
cfprLsmaintAckScheduler = _CfprLsmaintAckScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 1, 1, 26),
    _CfprLsmaintAckScheduler_Type()
)
cfprLsmaintAckScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintAckScheduler.setStatus("current")
_CfprLsmaintMaintPolicyTable_Object = MibTable
cfprLsmaintMaintPolicyTable = _CfprLsmaintMaintPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2)
)
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicyTable.setStatus("current")
_CfprLsmaintMaintPolicyEntry_Object = MibTableRow
cfprLsmaintMaintPolicyEntry = _CfprLsmaintMaintPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2, 1)
)
cfprLsmaintMaintPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LSMAINT-MIB", "cfprLsmaintMaintPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicyEntry.setStatus("current")
_CfprLsmaintMaintPolicyInstanceId_Type = CfprManagedObjectId
_CfprLsmaintMaintPolicyInstanceId_Object = MibTableColumn
cfprLsmaintMaintPolicyInstanceId = _CfprLsmaintMaintPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2, 1, 1),
    _CfprLsmaintMaintPolicyInstanceId_Type()
)
cfprLsmaintMaintPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicyInstanceId.setStatus("current")
_CfprLsmaintMaintPolicyDn_Type = CfprManagedObjectDn
_CfprLsmaintMaintPolicyDn_Object = MibTableColumn
cfprLsmaintMaintPolicyDn = _CfprLsmaintMaintPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2, 1, 2),
    _CfprLsmaintMaintPolicyDn_Type()
)
cfprLsmaintMaintPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicyDn.setStatus("current")
_CfprLsmaintMaintPolicyRn_Type = SnmpAdminString
_CfprLsmaintMaintPolicyRn_Object = MibTableColumn
cfprLsmaintMaintPolicyRn = _CfprLsmaintMaintPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2, 1, 3),
    _CfprLsmaintMaintPolicyRn_Type()
)
cfprLsmaintMaintPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicyRn.setStatus("current")
_CfprLsmaintMaintPolicyDescr_Type = SnmpAdminString
_CfprLsmaintMaintPolicyDescr_Object = MibTableColumn
cfprLsmaintMaintPolicyDescr = _CfprLsmaintMaintPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2, 1, 4),
    _CfprLsmaintMaintPolicyDescr_Type()
)
cfprLsmaintMaintPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicyDescr.setStatus("current")
_CfprLsmaintMaintPolicyIntId_Type = SnmpAdminString
_CfprLsmaintMaintPolicyIntId_Object = MibTableColumn
cfprLsmaintMaintPolicyIntId = _CfprLsmaintMaintPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2, 1, 5),
    _CfprLsmaintMaintPolicyIntId_Type()
)
cfprLsmaintMaintPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicyIntId.setStatus("current")
_CfprLsmaintMaintPolicyName_Type = SnmpAdminString
_CfprLsmaintMaintPolicyName_Object = MibTableColumn
cfprLsmaintMaintPolicyName = _CfprLsmaintMaintPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2, 1, 6),
    _CfprLsmaintMaintPolicyName_Type()
)
cfprLsmaintMaintPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicyName.setStatus("current")
_CfprLsmaintMaintPolicyOperSchedName_Type = SnmpAdminString
_CfprLsmaintMaintPolicyOperSchedName_Object = MibTableColumn
cfprLsmaintMaintPolicyOperSchedName = _CfprLsmaintMaintPolicyOperSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2, 1, 7),
    _CfprLsmaintMaintPolicyOperSchedName_Type()
)
cfprLsmaintMaintPolicyOperSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicyOperSchedName.setStatus("current")
_CfprLsmaintMaintPolicyPolicyLevel_Type = Gauge32
_CfprLsmaintMaintPolicyPolicyLevel_Object = MibTableColumn
cfprLsmaintMaintPolicyPolicyLevel = _CfprLsmaintMaintPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2, 1, 8),
    _CfprLsmaintMaintPolicyPolicyLevel_Type()
)
cfprLsmaintMaintPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicyPolicyLevel.setStatus("current")
_CfprLsmaintMaintPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprLsmaintMaintPolicyPolicyOwner_Object = MibTableColumn
cfprLsmaintMaintPolicyPolicyOwner = _CfprLsmaintMaintPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2, 1, 9),
    _CfprLsmaintMaintPolicyPolicyOwner_Type()
)
cfprLsmaintMaintPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicyPolicyOwner.setStatus("current")
_CfprLsmaintMaintPolicySchedName_Type = SnmpAdminString
_CfprLsmaintMaintPolicySchedName_Object = MibTableColumn
cfprLsmaintMaintPolicySchedName = _CfprLsmaintMaintPolicySchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2, 1, 10),
    _CfprLsmaintMaintPolicySchedName_Type()
)
cfprLsmaintMaintPolicySchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicySchedName.setStatus("current")
_CfprLsmaintMaintPolicyUptimeDisr_Type = CfprTrigAckMode
_CfprLsmaintMaintPolicyUptimeDisr_Object = MibTableColumn
cfprLsmaintMaintPolicyUptimeDisr = _CfprLsmaintMaintPolicyUptimeDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 48, 2, 1, 11),
    _CfprLsmaintMaintPolicyUptimeDisr_Type()
)
cfprLsmaintMaintPolicyUptimeDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLsmaintMaintPolicyUptimeDisr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-LSMAINT-MIB",
    **{"cfprLsmaintObjects": cfprLsmaintObjects,
       "cfprLsmaintAckTable": cfprLsmaintAckTable,
       "cfprLsmaintAckEntry": cfprLsmaintAckEntry,
       "cfprLsmaintAckInstanceId": cfprLsmaintAckInstanceId,
       "cfprLsmaintAckDn": cfprLsmaintAckDn,
       "cfprLsmaintAckRn": cfprLsmaintAckRn,
       "cfprLsmaintAckAcked": cfprLsmaintAckAcked,
       "cfprLsmaintAckAckedBy": cfprLsmaintAckAckedBy,
       "cfprLsmaintAckAdminState": cfprLsmaintAckAdminState,
       "cfprLsmaintAckAutoDelete": cfprLsmaintAckAutoDelete,
       "cfprLsmaintAckChangeBy": cfprLsmaintAckChangeBy,
       "cfprLsmaintAckChangeDetails": cfprLsmaintAckChangeDetails,
       "cfprLsmaintAckChangeMode": cfprLsmaintAckChangeMode,
       "cfprLsmaintAckChanges": cfprLsmaintAckChanges,
       "cfprLsmaintAckConfigIssues": cfprLsmaintAckConfigIssues,
       "cfprLsmaintAckDeploymentMode": cfprLsmaintAckDeploymentMode,
       "cfprLsmaintAckDescr": cfprLsmaintAckDescr,
       "cfprLsmaintAckDisr": cfprLsmaintAckDisr,
       "cfprLsmaintAckIgnoreCap": cfprLsmaintAckIgnoreCap,
       "cfprLsmaintAckIntId": cfprLsmaintAckIntId,
       "cfprLsmaintAckModified": cfprLsmaintAckModified,
       "cfprLsmaintAckName": cfprLsmaintAckName,
       "cfprLsmaintAckOldPnDn": cfprLsmaintAckOldPnDn,
       "cfprLsmaintAckOperScheduler": cfprLsmaintAckOperScheduler,
       "cfprLsmaintAckOperState": cfprLsmaintAckOperState,
       "cfprLsmaintAckPolicyLevel": cfprLsmaintAckPolicyLevel,
       "cfprLsmaintAckPolicyOwner": cfprLsmaintAckPolicyOwner,
       "cfprLsmaintAckPrevOperState": cfprLsmaintAckPrevOperState,
       "cfprLsmaintAckScheduler": cfprLsmaintAckScheduler,
       "cfprLsmaintMaintPolicyTable": cfprLsmaintMaintPolicyTable,
       "cfprLsmaintMaintPolicyEntry": cfprLsmaintMaintPolicyEntry,
       "cfprLsmaintMaintPolicyInstanceId": cfprLsmaintMaintPolicyInstanceId,
       "cfprLsmaintMaintPolicyDn": cfprLsmaintMaintPolicyDn,
       "cfprLsmaintMaintPolicyRn": cfprLsmaintMaintPolicyRn,
       "cfprLsmaintMaintPolicyDescr": cfprLsmaintMaintPolicyDescr,
       "cfprLsmaintMaintPolicyIntId": cfprLsmaintMaintPolicyIntId,
       "cfprLsmaintMaintPolicyName": cfprLsmaintMaintPolicyName,
       "cfprLsmaintMaintPolicyOperSchedName": cfprLsmaintMaintPolicyOperSchedName,
       "cfprLsmaintMaintPolicyPolicyLevel": cfprLsmaintMaintPolicyPolicyLevel,
       "cfprLsmaintMaintPolicyPolicyOwner": cfprLsmaintMaintPolicyPolicyOwner,
       "cfprLsmaintMaintPolicySchedName": cfprLsmaintMaintPolicySchedName,
       "cfprLsmaintMaintPolicyUptimeDisr": cfprLsmaintMaintPolicyUptimeDisr}
)
