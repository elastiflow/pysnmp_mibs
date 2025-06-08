# SNMP MIB module (CISCO-FIREPOWER-AP-UUIDPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-UUIDPOOL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:21:40 2025
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

(CfprApAddressUIDSuffxMask,
 CfprApPolicyPolicyOwner,
 CfprApPoolElementOwner,
 CfprApUuidpoolPoolAssignmentOrder) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApAddressUIDSuffxMask",
    "CfprApPolicyPolicyOwner",
    "CfprApPoolElementOwner",
    "CfprApUuidpoolPoolAssignmentOrder")

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

cfprApUuidpoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApUuidpoolAddrTable_Object = MibTable
cfprApUuidpoolAddrTable = _CfprApUuidpoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 1)
)
if mibBuilder.loadTexts:
    cfprApUuidpoolAddrTable.setStatus("current")
_CfprApUuidpoolAddrEntry_Object = MibTableRow
cfprApUuidpoolAddrEntry = _CfprApUuidpoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 1, 1)
)
cfprApUuidpoolAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-UUIDPOOL-MIB", "cfprApUuidpoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApUuidpoolAddrEntry.setStatus("current")
_CfprApUuidpoolAddrInstanceId_Type = CfprApManagedObjectId
_CfprApUuidpoolAddrInstanceId_Object = MibTableColumn
cfprApUuidpoolAddrInstanceId = _CfprApUuidpoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 1, 1, 1),
    _CfprApUuidpoolAddrInstanceId_Type()
)
cfprApUuidpoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApUuidpoolAddrInstanceId.setStatus("current")
_CfprApUuidpoolAddrDn_Type = CfprApManagedObjectDn
_CfprApUuidpoolAddrDn_Object = MibTableColumn
cfprApUuidpoolAddrDn = _CfprApUuidpoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 1, 1, 2),
    _CfprApUuidpoolAddrDn_Type()
)
cfprApUuidpoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolAddrDn.setStatus("current")
_CfprApUuidpoolAddrRn_Type = SnmpAdminString
_CfprApUuidpoolAddrRn_Object = MibTableColumn
cfprApUuidpoolAddrRn = _CfprApUuidpoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 1, 1, 3),
    _CfprApUuidpoolAddrRn_Type()
)
cfprApUuidpoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolAddrRn.setStatus("current")
_CfprApUuidpoolAddrAssigned_Type = TruthValue
_CfprApUuidpoolAddrAssigned_Object = MibTableColumn
cfprApUuidpoolAddrAssigned = _CfprApUuidpoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 1, 1, 4),
    _CfprApUuidpoolAddrAssigned_Type()
)
cfprApUuidpoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolAddrAssigned.setStatus("current")
_CfprApUuidpoolAddrAssignedToDn_Type = SnmpAdminString
_CfprApUuidpoolAddrAssignedToDn_Object = MibTableColumn
cfprApUuidpoolAddrAssignedToDn = _CfprApUuidpoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 1, 1, 5),
    _CfprApUuidpoolAddrAssignedToDn_Type()
)
cfprApUuidpoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolAddrAssignedToDn.setStatus("current")
_CfprApUuidpoolAddrGlobalAssignedCnt_Type = Gauge32
_CfprApUuidpoolAddrGlobalAssignedCnt_Object = MibTableColumn
cfprApUuidpoolAddrGlobalAssignedCnt = _CfprApUuidpoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 1, 1, 6),
    _CfprApUuidpoolAddrGlobalAssignedCnt_Type()
)
cfprApUuidpoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolAddrGlobalAssignedCnt.setStatus("current")
_CfprApUuidpoolAddrGlobalDefinedCnt_Type = Gauge32
_CfprApUuidpoolAddrGlobalDefinedCnt_Object = MibTableColumn
cfprApUuidpoolAddrGlobalDefinedCnt = _CfprApUuidpoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 1, 1, 7),
    _CfprApUuidpoolAddrGlobalDefinedCnt_Type()
)
cfprApUuidpoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolAddrGlobalDefinedCnt.setStatus("current")
_CfprApUuidpoolAddrId_Type = SnmpAdminString
_CfprApUuidpoolAddrId_Object = MibTableColumn
cfprApUuidpoolAddrId = _CfprApUuidpoolAddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 1, 1, 8),
    _CfprApUuidpoolAddrId_Type()
)
cfprApUuidpoolAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolAddrId.setStatus("current")
_CfprApUuidpoolAddrOwner_Type = CfprApPoolElementOwner
_CfprApUuidpoolAddrOwner_Object = MibTableColumn
cfprApUuidpoolAddrOwner = _CfprApUuidpoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 1, 1, 9),
    _CfprApUuidpoolAddrOwner_Type()
)
cfprApUuidpoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolAddrOwner.setStatus("current")
_CfprApUuidpoolBlockTable_Object = MibTable
cfprApUuidpoolBlockTable = _CfprApUuidpoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 2)
)
if mibBuilder.loadTexts:
    cfprApUuidpoolBlockTable.setStatus("current")
_CfprApUuidpoolBlockEntry_Object = MibTableRow
cfprApUuidpoolBlockEntry = _CfprApUuidpoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 2, 1)
)
cfprApUuidpoolBlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-UUIDPOOL-MIB", "cfprApUuidpoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApUuidpoolBlockEntry.setStatus("current")
_CfprApUuidpoolBlockInstanceId_Type = CfprApManagedObjectId
_CfprApUuidpoolBlockInstanceId_Object = MibTableColumn
cfprApUuidpoolBlockInstanceId = _CfprApUuidpoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 2, 1, 1),
    _CfprApUuidpoolBlockInstanceId_Type()
)
cfprApUuidpoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApUuidpoolBlockInstanceId.setStatus("current")
_CfprApUuidpoolBlockDn_Type = CfprApManagedObjectDn
_CfprApUuidpoolBlockDn_Object = MibTableColumn
cfprApUuidpoolBlockDn = _CfprApUuidpoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 2, 1, 2),
    _CfprApUuidpoolBlockDn_Type()
)
cfprApUuidpoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolBlockDn.setStatus("current")
_CfprApUuidpoolBlockRn_Type = SnmpAdminString
_CfprApUuidpoolBlockRn_Object = MibTableColumn
cfprApUuidpoolBlockRn = _CfprApUuidpoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 2, 1, 3),
    _CfprApUuidpoolBlockRn_Type()
)
cfprApUuidpoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolBlockRn.setStatus("current")
_CfprApUuidpoolBlockFrom_Type = Unsigned64
_CfprApUuidpoolBlockFrom_Object = MibTableColumn
cfprApUuidpoolBlockFrom = _CfprApUuidpoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 2, 1, 4),
    _CfprApUuidpoolBlockFrom_Type()
)
cfprApUuidpoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolBlockFrom.setStatus("current")
_CfprApUuidpoolBlockTo_Type = Unsigned64
_CfprApUuidpoolBlockTo_Object = MibTableColumn
cfprApUuidpoolBlockTo = _CfprApUuidpoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 2, 1, 5),
    _CfprApUuidpoolBlockTo_Type()
)
cfprApUuidpoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolBlockTo.setStatus("current")
_CfprApUuidpoolFormatTable_Object = MibTable
cfprApUuidpoolFormatTable = _CfprApUuidpoolFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 3)
)
if mibBuilder.loadTexts:
    cfprApUuidpoolFormatTable.setStatus("current")
_CfprApUuidpoolFormatEntry_Object = MibTableRow
cfprApUuidpoolFormatEntry = _CfprApUuidpoolFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 3, 1)
)
cfprApUuidpoolFormatEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-UUIDPOOL-MIB", "cfprApUuidpoolFormatInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApUuidpoolFormatEntry.setStatus("current")
_CfprApUuidpoolFormatInstanceId_Type = CfprApManagedObjectId
_CfprApUuidpoolFormatInstanceId_Object = MibTableColumn
cfprApUuidpoolFormatInstanceId = _CfprApUuidpoolFormatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 3, 1, 1),
    _CfprApUuidpoolFormatInstanceId_Type()
)
cfprApUuidpoolFormatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApUuidpoolFormatInstanceId.setStatus("current")
_CfprApUuidpoolFormatDn_Type = CfprApManagedObjectDn
_CfprApUuidpoolFormatDn_Object = MibTableColumn
cfprApUuidpoolFormatDn = _CfprApUuidpoolFormatDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 3, 1, 2),
    _CfprApUuidpoolFormatDn_Type()
)
cfprApUuidpoolFormatDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolFormatDn.setStatus("current")
_CfprApUuidpoolFormatRn_Type = SnmpAdminString
_CfprApUuidpoolFormatRn_Object = MibTableColumn
cfprApUuidpoolFormatRn = _CfprApUuidpoolFormatRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 3, 1, 3),
    _CfprApUuidpoolFormatRn_Type()
)
cfprApUuidpoolFormatRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolFormatRn.setStatus("current")
_CfprApUuidpoolFormatFormat_Type = Unsigned64
_CfprApUuidpoolFormatFormat_Object = MibTableColumn
cfprApUuidpoolFormatFormat = _CfprApUuidpoolFormatFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 3, 1, 4),
    _CfprApUuidpoolFormatFormat_Type()
)
cfprApUuidpoolFormatFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolFormatFormat.setStatus("current")
_CfprApUuidpoolFormatMask_Type = CfprApAddressUIDSuffxMask
_CfprApUuidpoolFormatMask_Object = MibTableColumn
cfprApUuidpoolFormatMask = _CfprApUuidpoolFormatMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 3, 1, 5),
    _CfprApUuidpoolFormatMask_Type()
)
cfprApUuidpoolFormatMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolFormatMask.setStatus("current")
_CfprApUuidpoolPoolTable_Object = MibTable
cfprApUuidpoolPoolTable = _CfprApUuidpoolPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4)
)
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolTable.setStatus("current")
_CfprApUuidpoolPoolEntry_Object = MibTableRow
cfprApUuidpoolPoolEntry = _CfprApUuidpoolPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1)
)
cfprApUuidpoolPoolEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-UUIDPOOL-MIB", "cfprApUuidpoolPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolEntry.setStatus("current")
_CfprApUuidpoolPoolInstanceId_Type = CfprApManagedObjectId
_CfprApUuidpoolPoolInstanceId_Object = MibTableColumn
cfprApUuidpoolPoolInstanceId = _CfprApUuidpoolPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1, 1),
    _CfprApUuidpoolPoolInstanceId_Type()
)
cfprApUuidpoolPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolInstanceId.setStatus("current")
_CfprApUuidpoolPoolDn_Type = CfprApManagedObjectDn
_CfprApUuidpoolPoolDn_Object = MibTableColumn
cfprApUuidpoolPoolDn = _CfprApUuidpoolPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1, 2),
    _CfprApUuidpoolPoolDn_Type()
)
cfprApUuidpoolPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolDn.setStatus("current")
_CfprApUuidpoolPoolRn_Type = SnmpAdminString
_CfprApUuidpoolPoolRn_Object = MibTableColumn
cfprApUuidpoolPoolRn = _CfprApUuidpoolPoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1, 3),
    _CfprApUuidpoolPoolRn_Type()
)
cfprApUuidpoolPoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolRn.setStatus("current")
_CfprApUuidpoolPoolAssigned_Type = Gauge32
_CfprApUuidpoolPoolAssigned_Object = MibTableColumn
cfprApUuidpoolPoolAssigned = _CfprApUuidpoolPoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1, 4),
    _CfprApUuidpoolPoolAssigned_Type()
)
cfprApUuidpoolPoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolAssigned.setStatus("current")
_CfprApUuidpoolPoolAssignmentOrder_Type = CfprApUuidpoolPoolAssignmentOrder
_CfprApUuidpoolPoolAssignmentOrder_Object = MibTableColumn
cfprApUuidpoolPoolAssignmentOrder = _CfprApUuidpoolPoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1, 5),
    _CfprApUuidpoolPoolAssignmentOrder_Type()
)
cfprApUuidpoolPoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolAssignmentOrder.setStatus("current")
_CfprApUuidpoolPoolDescr_Type = SnmpAdminString
_CfprApUuidpoolPoolDescr_Object = MibTableColumn
cfprApUuidpoolPoolDescr = _CfprApUuidpoolPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1, 6),
    _CfprApUuidpoolPoolDescr_Type()
)
cfprApUuidpoolPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolDescr.setStatus("current")
_CfprApUuidpoolPoolIntId_Type = SnmpAdminString
_CfprApUuidpoolPoolIntId_Object = MibTableColumn
cfprApUuidpoolPoolIntId = _CfprApUuidpoolPoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1, 7),
    _CfprApUuidpoolPoolIntId_Type()
)
cfprApUuidpoolPoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolIntId.setStatus("current")
_CfprApUuidpoolPoolName_Type = SnmpAdminString
_CfprApUuidpoolPoolName_Object = MibTableColumn
cfprApUuidpoolPoolName = _CfprApUuidpoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1, 8),
    _CfprApUuidpoolPoolName_Type()
)
cfprApUuidpoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolName.setStatus("current")
_CfprApUuidpoolPoolPolicyLevel_Type = Gauge32
_CfprApUuidpoolPoolPolicyLevel_Object = MibTableColumn
cfprApUuidpoolPoolPolicyLevel = _CfprApUuidpoolPoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1, 9),
    _CfprApUuidpoolPoolPolicyLevel_Type()
)
cfprApUuidpoolPoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolPolicyLevel.setStatus("current")
_CfprApUuidpoolPoolPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApUuidpoolPoolPolicyOwner_Object = MibTableColumn
cfprApUuidpoolPoolPolicyOwner = _CfprApUuidpoolPoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1, 10),
    _CfprApUuidpoolPoolPolicyOwner_Type()
)
cfprApUuidpoolPoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolPolicyOwner.setStatus("current")
_CfprApUuidpoolPoolPrefix_Type = Unsigned64
_CfprApUuidpoolPoolPrefix_Object = MibTableColumn
cfprApUuidpoolPoolPrefix = _CfprApUuidpoolPoolPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1, 11),
    _CfprApUuidpoolPoolPrefix_Type()
)
cfprApUuidpoolPoolPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolPrefix.setStatus("current")
_CfprApUuidpoolPoolSize_Type = Gauge32
_CfprApUuidpoolPoolSize_Object = MibTableColumn
cfprApUuidpoolPoolSize = _CfprApUuidpoolPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 4, 1, 12),
    _CfprApUuidpoolPoolSize_Type()
)
cfprApUuidpoolPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolSize.setStatus("current")
_CfprApUuidpoolPoolableTable_Object = MibTable
cfprApUuidpoolPoolableTable = _CfprApUuidpoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 5)
)
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolableTable.setStatus("current")
_CfprApUuidpoolPoolableEntry_Object = MibTableRow
cfprApUuidpoolPoolableEntry = _CfprApUuidpoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 5, 1)
)
cfprApUuidpoolPoolableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-UUIDPOOL-MIB", "cfprApUuidpoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolableEntry.setStatus("current")
_CfprApUuidpoolPoolableInstanceId_Type = CfprApManagedObjectId
_CfprApUuidpoolPoolableInstanceId_Object = MibTableColumn
cfprApUuidpoolPoolableInstanceId = _CfprApUuidpoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 5, 1, 1),
    _CfprApUuidpoolPoolableInstanceId_Type()
)
cfprApUuidpoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolableInstanceId.setStatus("current")
_CfprApUuidpoolPoolableDn_Type = CfprApManagedObjectDn
_CfprApUuidpoolPoolableDn_Object = MibTableColumn
cfprApUuidpoolPoolableDn = _CfprApUuidpoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 5, 1, 2),
    _CfprApUuidpoolPoolableDn_Type()
)
cfprApUuidpoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolableDn.setStatus("current")
_CfprApUuidpoolPoolableRn_Type = SnmpAdminString
_CfprApUuidpoolPoolableRn_Object = MibTableColumn
cfprApUuidpoolPoolableRn = _CfprApUuidpoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 5, 1, 3),
    _CfprApUuidpoolPoolableRn_Type()
)
cfprApUuidpoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolableRn.setStatus("current")
_CfprApUuidpoolPoolableId_Type = Unsigned64
_CfprApUuidpoolPoolableId_Object = MibTableColumn
cfprApUuidpoolPoolableId = _CfprApUuidpoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 5, 1, 4),
    _CfprApUuidpoolPoolableId_Type()
)
cfprApUuidpoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolableId.setStatus("current")
_CfprApUuidpoolPoolablePoolDn_Type = SnmpAdminString
_CfprApUuidpoolPoolablePoolDn_Object = MibTableColumn
cfprApUuidpoolPoolablePoolDn = _CfprApUuidpoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 5, 1, 5),
    _CfprApUuidpoolPoolablePoolDn_Type()
)
cfprApUuidpoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPoolablePoolDn.setStatus("current")
_CfprApUuidpoolPooledTable_Object = MibTable
cfprApUuidpoolPooledTable = _CfprApUuidpoolPooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 6)
)
if mibBuilder.loadTexts:
    cfprApUuidpoolPooledTable.setStatus("current")
_CfprApUuidpoolPooledEntry_Object = MibTableRow
cfprApUuidpoolPooledEntry = _CfprApUuidpoolPooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 6, 1)
)
cfprApUuidpoolPooledEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-UUIDPOOL-MIB", "cfprApUuidpoolPooledInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApUuidpoolPooledEntry.setStatus("current")
_CfprApUuidpoolPooledInstanceId_Type = CfprApManagedObjectId
_CfprApUuidpoolPooledInstanceId_Object = MibTableColumn
cfprApUuidpoolPooledInstanceId = _CfprApUuidpoolPooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 6, 1, 1),
    _CfprApUuidpoolPooledInstanceId_Type()
)
cfprApUuidpoolPooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApUuidpoolPooledInstanceId.setStatus("current")
_CfprApUuidpoolPooledDn_Type = CfprApManagedObjectDn
_CfprApUuidpoolPooledDn_Object = MibTableColumn
cfprApUuidpoolPooledDn = _CfprApUuidpoolPooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 6, 1, 2),
    _CfprApUuidpoolPooledDn_Type()
)
cfprApUuidpoolPooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPooledDn.setStatus("current")
_CfprApUuidpoolPooledRn_Type = SnmpAdminString
_CfprApUuidpoolPooledRn_Object = MibTableColumn
cfprApUuidpoolPooledRn = _CfprApUuidpoolPooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 6, 1, 3),
    _CfprApUuidpoolPooledRn_Type()
)
cfprApUuidpoolPooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPooledRn.setStatus("current")
_CfprApUuidpoolPooledAssigned_Type = TruthValue
_CfprApUuidpoolPooledAssigned_Object = MibTableColumn
cfprApUuidpoolPooledAssigned = _CfprApUuidpoolPooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 6, 1, 4),
    _CfprApUuidpoolPooledAssigned_Type()
)
cfprApUuidpoolPooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPooledAssigned.setStatus("current")
_CfprApUuidpoolPooledAssignedToDn_Type = SnmpAdminString
_CfprApUuidpoolPooledAssignedToDn_Object = MibTableColumn
cfprApUuidpoolPooledAssignedToDn = _CfprApUuidpoolPooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 6, 1, 5),
    _CfprApUuidpoolPooledAssignedToDn_Type()
)
cfprApUuidpoolPooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPooledAssignedToDn.setStatus("current")
_CfprApUuidpoolPooledId_Type = Unsigned64
_CfprApUuidpoolPooledId_Object = MibTableColumn
cfprApUuidpoolPooledId = _CfprApUuidpoolPooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 6, 1, 6),
    _CfprApUuidpoolPooledId_Type()
)
cfprApUuidpoolPooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPooledId.setStatus("current")
_CfprApUuidpoolPooledPoolableDn_Type = SnmpAdminString
_CfprApUuidpoolPooledPoolableDn_Object = MibTableColumn
cfprApUuidpoolPooledPoolableDn = _CfprApUuidpoolPooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 6, 1, 7),
    _CfprApUuidpoolPooledPoolableDn_Type()
)
cfprApUuidpoolPooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPooledPoolableDn.setStatus("current")
_CfprApUuidpoolPooledPrevAssignedToDn_Type = SnmpAdminString
_CfprApUuidpoolPooledPrevAssignedToDn_Object = MibTableColumn
cfprApUuidpoolPooledPrevAssignedToDn = _CfprApUuidpoolPooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 6, 1, 8),
    _CfprApUuidpoolPooledPrevAssignedToDn_Type()
)
cfprApUuidpoolPooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolPooledPrevAssignedToDn.setStatus("current")
_CfprApUuidpoolUniverseTable_Object = MibTable
cfprApUuidpoolUniverseTable = _CfprApUuidpoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 7)
)
if mibBuilder.loadTexts:
    cfprApUuidpoolUniverseTable.setStatus("current")
_CfprApUuidpoolUniverseEntry_Object = MibTableRow
cfprApUuidpoolUniverseEntry = _CfprApUuidpoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 7, 1)
)
cfprApUuidpoolUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-UUIDPOOL-MIB", "cfprApUuidpoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApUuidpoolUniverseEntry.setStatus("current")
_CfprApUuidpoolUniverseInstanceId_Type = CfprApManagedObjectId
_CfprApUuidpoolUniverseInstanceId_Object = MibTableColumn
cfprApUuidpoolUniverseInstanceId = _CfprApUuidpoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 7, 1, 1),
    _CfprApUuidpoolUniverseInstanceId_Type()
)
cfprApUuidpoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApUuidpoolUniverseInstanceId.setStatus("current")
_CfprApUuidpoolUniverseDn_Type = CfprApManagedObjectDn
_CfprApUuidpoolUniverseDn_Object = MibTableColumn
cfprApUuidpoolUniverseDn = _CfprApUuidpoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 7, 1, 2),
    _CfprApUuidpoolUniverseDn_Type()
)
cfprApUuidpoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolUniverseDn.setStatus("current")
_CfprApUuidpoolUniverseRn_Type = SnmpAdminString
_CfprApUuidpoolUniverseRn_Object = MibTableColumn
cfprApUuidpoolUniverseRn = _CfprApUuidpoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 80, 7, 1, 3),
    _CfprApUuidpoolUniverseRn_Type()
)
cfprApUuidpoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApUuidpoolUniverseRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-UUIDPOOL-MIB",
    **{"cfprApUuidpoolObjects": cfprApUuidpoolObjects,
       "cfprApUuidpoolAddrTable": cfprApUuidpoolAddrTable,
       "cfprApUuidpoolAddrEntry": cfprApUuidpoolAddrEntry,
       "cfprApUuidpoolAddrInstanceId": cfprApUuidpoolAddrInstanceId,
       "cfprApUuidpoolAddrDn": cfprApUuidpoolAddrDn,
       "cfprApUuidpoolAddrRn": cfprApUuidpoolAddrRn,
       "cfprApUuidpoolAddrAssigned": cfprApUuidpoolAddrAssigned,
       "cfprApUuidpoolAddrAssignedToDn": cfprApUuidpoolAddrAssignedToDn,
       "cfprApUuidpoolAddrGlobalAssignedCnt": cfprApUuidpoolAddrGlobalAssignedCnt,
       "cfprApUuidpoolAddrGlobalDefinedCnt": cfprApUuidpoolAddrGlobalDefinedCnt,
       "cfprApUuidpoolAddrId": cfprApUuidpoolAddrId,
       "cfprApUuidpoolAddrOwner": cfprApUuidpoolAddrOwner,
       "cfprApUuidpoolBlockTable": cfprApUuidpoolBlockTable,
       "cfprApUuidpoolBlockEntry": cfprApUuidpoolBlockEntry,
       "cfprApUuidpoolBlockInstanceId": cfprApUuidpoolBlockInstanceId,
       "cfprApUuidpoolBlockDn": cfprApUuidpoolBlockDn,
       "cfprApUuidpoolBlockRn": cfprApUuidpoolBlockRn,
       "cfprApUuidpoolBlockFrom": cfprApUuidpoolBlockFrom,
       "cfprApUuidpoolBlockTo": cfprApUuidpoolBlockTo,
       "cfprApUuidpoolFormatTable": cfprApUuidpoolFormatTable,
       "cfprApUuidpoolFormatEntry": cfprApUuidpoolFormatEntry,
       "cfprApUuidpoolFormatInstanceId": cfprApUuidpoolFormatInstanceId,
       "cfprApUuidpoolFormatDn": cfprApUuidpoolFormatDn,
       "cfprApUuidpoolFormatRn": cfprApUuidpoolFormatRn,
       "cfprApUuidpoolFormatFormat": cfprApUuidpoolFormatFormat,
       "cfprApUuidpoolFormatMask": cfprApUuidpoolFormatMask,
       "cfprApUuidpoolPoolTable": cfprApUuidpoolPoolTable,
       "cfprApUuidpoolPoolEntry": cfprApUuidpoolPoolEntry,
       "cfprApUuidpoolPoolInstanceId": cfprApUuidpoolPoolInstanceId,
       "cfprApUuidpoolPoolDn": cfprApUuidpoolPoolDn,
       "cfprApUuidpoolPoolRn": cfprApUuidpoolPoolRn,
       "cfprApUuidpoolPoolAssigned": cfprApUuidpoolPoolAssigned,
       "cfprApUuidpoolPoolAssignmentOrder": cfprApUuidpoolPoolAssignmentOrder,
       "cfprApUuidpoolPoolDescr": cfprApUuidpoolPoolDescr,
       "cfprApUuidpoolPoolIntId": cfprApUuidpoolPoolIntId,
       "cfprApUuidpoolPoolName": cfprApUuidpoolPoolName,
       "cfprApUuidpoolPoolPolicyLevel": cfprApUuidpoolPoolPolicyLevel,
       "cfprApUuidpoolPoolPolicyOwner": cfprApUuidpoolPoolPolicyOwner,
       "cfprApUuidpoolPoolPrefix": cfprApUuidpoolPoolPrefix,
       "cfprApUuidpoolPoolSize": cfprApUuidpoolPoolSize,
       "cfprApUuidpoolPoolableTable": cfprApUuidpoolPoolableTable,
       "cfprApUuidpoolPoolableEntry": cfprApUuidpoolPoolableEntry,
       "cfprApUuidpoolPoolableInstanceId": cfprApUuidpoolPoolableInstanceId,
       "cfprApUuidpoolPoolableDn": cfprApUuidpoolPoolableDn,
       "cfprApUuidpoolPoolableRn": cfprApUuidpoolPoolableRn,
       "cfprApUuidpoolPoolableId": cfprApUuidpoolPoolableId,
       "cfprApUuidpoolPoolablePoolDn": cfprApUuidpoolPoolablePoolDn,
       "cfprApUuidpoolPooledTable": cfprApUuidpoolPooledTable,
       "cfprApUuidpoolPooledEntry": cfprApUuidpoolPooledEntry,
       "cfprApUuidpoolPooledInstanceId": cfprApUuidpoolPooledInstanceId,
       "cfprApUuidpoolPooledDn": cfprApUuidpoolPooledDn,
       "cfprApUuidpoolPooledRn": cfprApUuidpoolPooledRn,
       "cfprApUuidpoolPooledAssigned": cfprApUuidpoolPooledAssigned,
       "cfprApUuidpoolPooledAssignedToDn": cfprApUuidpoolPooledAssignedToDn,
       "cfprApUuidpoolPooledId": cfprApUuidpoolPooledId,
       "cfprApUuidpoolPooledPoolableDn": cfprApUuidpoolPooledPoolableDn,
       "cfprApUuidpoolPooledPrevAssignedToDn": cfprApUuidpoolPooledPrevAssignedToDn,
       "cfprApUuidpoolUniverseTable": cfprApUuidpoolUniverseTable,
       "cfprApUuidpoolUniverseEntry": cfprApUuidpoolUniverseEntry,
       "cfprApUuidpoolUniverseInstanceId": cfprApUuidpoolUniverseInstanceId,
       "cfprApUuidpoolUniverseDn": cfprApUuidpoolUniverseDn,
       "cfprApUuidpoolUniverseRn": cfprApUuidpoolUniverseRn}
)
