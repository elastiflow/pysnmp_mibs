# SNMP MIB module (CISCO-FIREPOWER-UUIDPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-UUIDPOOL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:13 2025
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

(CfprAddressUIDSuffxMask,
 CfprPolicyPolicyOwner,
 CfprPoolElementOwner,
 CfprUuidpoolPoolAssignmentOrder) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprAddressUIDSuffxMask",
    "CfprPolicyPolicyOwner",
    "CfprPoolElementOwner",
    "CfprUuidpoolPoolAssignmentOrder")

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

cfprUuidpoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprUuidpoolAddrTable_Object = MibTable
cfprUuidpoolAddrTable = _CfprUuidpoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 1)
)
if mibBuilder.loadTexts:
    cfprUuidpoolAddrTable.setStatus("current")
_CfprUuidpoolAddrEntry_Object = MibTableRow
cfprUuidpoolAddrEntry = _CfprUuidpoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 1, 1)
)
cfprUuidpoolAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-UUIDPOOL-MIB", "cfprUuidpoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprUuidpoolAddrEntry.setStatus("current")
_CfprUuidpoolAddrInstanceId_Type = CfprManagedObjectId
_CfprUuidpoolAddrInstanceId_Object = MibTableColumn
cfprUuidpoolAddrInstanceId = _CfprUuidpoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 1, 1, 1),
    _CfprUuidpoolAddrInstanceId_Type()
)
cfprUuidpoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprUuidpoolAddrInstanceId.setStatus("current")
_CfprUuidpoolAddrDn_Type = CfprManagedObjectDn
_CfprUuidpoolAddrDn_Object = MibTableColumn
cfprUuidpoolAddrDn = _CfprUuidpoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 1, 1, 2),
    _CfprUuidpoolAddrDn_Type()
)
cfprUuidpoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolAddrDn.setStatus("current")
_CfprUuidpoolAddrRn_Type = SnmpAdminString
_CfprUuidpoolAddrRn_Object = MibTableColumn
cfprUuidpoolAddrRn = _CfprUuidpoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 1, 1, 3),
    _CfprUuidpoolAddrRn_Type()
)
cfprUuidpoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolAddrRn.setStatus("current")
_CfprUuidpoolAddrAssigned_Type = TruthValue
_CfprUuidpoolAddrAssigned_Object = MibTableColumn
cfprUuidpoolAddrAssigned = _CfprUuidpoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 1, 1, 4),
    _CfprUuidpoolAddrAssigned_Type()
)
cfprUuidpoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolAddrAssigned.setStatus("current")
_CfprUuidpoolAddrAssignedToDn_Type = SnmpAdminString
_CfprUuidpoolAddrAssignedToDn_Object = MibTableColumn
cfprUuidpoolAddrAssignedToDn = _CfprUuidpoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 1, 1, 5),
    _CfprUuidpoolAddrAssignedToDn_Type()
)
cfprUuidpoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolAddrAssignedToDn.setStatus("current")
_CfprUuidpoolAddrGlobalAssignedCnt_Type = Gauge32
_CfprUuidpoolAddrGlobalAssignedCnt_Object = MibTableColumn
cfprUuidpoolAddrGlobalAssignedCnt = _CfprUuidpoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 1, 1, 6),
    _CfprUuidpoolAddrGlobalAssignedCnt_Type()
)
cfprUuidpoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolAddrGlobalAssignedCnt.setStatus("current")
_CfprUuidpoolAddrGlobalDefinedCnt_Type = Gauge32
_CfprUuidpoolAddrGlobalDefinedCnt_Object = MibTableColumn
cfprUuidpoolAddrGlobalDefinedCnt = _CfprUuidpoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 1, 1, 7),
    _CfprUuidpoolAddrGlobalDefinedCnt_Type()
)
cfprUuidpoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolAddrGlobalDefinedCnt.setStatus("current")
_CfprUuidpoolAddrId_Type = SnmpAdminString
_CfprUuidpoolAddrId_Object = MibTableColumn
cfprUuidpoolAddrId = _CfprUuidpoolAddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 1, 1, 8),
    _CfprUuidpoolAddrId_Type()
)
cfprUuidpoolAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolAddrId.setStatus("current")
_CfprUuidpoolAddrOwner_Type = CfprPoolElementOwner
_CfprUuidpoolAddrOwner_Object = MibTableColumn
cfprUuidpoolAddrOwner = _CfprUuidpoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 1, 1, 9),
    _CfprUuidpoolAddrOwner_Type()
)
cfprUuidpoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolAddrOwner.setStatus("current")
_CfprUuidpoolBlockTable_Object = MibTable
cfprUuidpoolBlockTable = _CfprUuidpoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 2)
)
if mibBuilder.loadTexts:
    cfprUuidpoolBlockTable.setStatus("current")
_CfprUuidpoolBlockEntry_Object = MibTableRow
cfprUuidpoolBlockEntry = _CfprUuidpoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 2, 1)
)
cfprUuidpoolBlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-UUIDPOOL-MIB", "cfprUuidpoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprUuidpoolBlockEntry.setStatus("current")
_CfprUuidpoolBlockInstanceId_Type = CfprManagedObjectId
_CfprUuidpoolBlockInstanceId_Object = MibTableColumn
cfprUuidpoolBlockInstanceId = _CfprUuidpoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 2, 1, 1),
    _CfprUuidpoolBlockInstanceId_Type()
)
cfprUuidpoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprUuidpoolBlockInstanceId.setStatus("current")
_CfprUuidpoolBlockDn_Type = CfprManagedObjectDn
_CfprUuidpoolBlockDn_Object = MibTableColumn
cfprUuidpoolBlockDn = _CfprUuidpoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 2, 1, 2),
    _CfprUuidpoolBlockDn_Type()
)
cfprUuidpoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolBlockDn.setStatus("current")
_CfprUuidpoolBlockRn_Type = SnmpAdminString
_CfprUuidpoolBlockRn_Object = MibTableColumn
cfprUuidpoolBlockRn = _CfprUuidpoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 2, 1, 3),
    _CfprUuidpoolBlockRn_Type()
)
cfprUuidpoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolBlockRn.setStatus("current")
_CfprUuidpoolBlockFrom_Type = Unsigned64
_CfprUuidpoolBlockFrom_Object = MibTableColumn
cfprUuidpoolBlockFrom = _CfprUuidpoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 2, 1, 4),
    _CfprUuidpoolBlockFrom_Type()
)
cfprUuidpoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolBlockFrom.setStatus("current")
_CfprUuidpoolBlockTo_Type = Unsigned64
_CfprUuidpoolBlockTo_Object = MibTableColumn
cfprUuidpoolBlockTo = _CfprUuidpoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 2, 1, 5),
    _CfprUuidpoolBlockTo_Type()
)
cfprUuidpoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolBlockTo.setStatus("current")
_CfprUuidpoolFormatTable_Object = MibTable
cfprUuidpoolFormatTable = _CfprUuidpoolFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 3)
)
if mibBuilder.loadTexts:
    cfprUuidpoolFormatTable.setStatus("current")
_CfprUuidpoolFormatEntry_Object = MibTableRow
cfprUuidpoolFormatEntry = _CfprUuidpoolFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 3, 1)
)
cfprUuidpoolFormatEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-UUIDPOOL-MIB", "cfprUuidpoolFormatInstanceId"),
)
if mibBuilder.loadTexts:
    cfprUuidpoolFormatEntry.setStatus("current")
_CfprUuidpoolFormatInstanceId_Type = CfprManagedObjectId
_CfprUuidpoolFormatInstanceId_Object = MibTableColumn
cfprUuidpoolFormatInstanceId = _CfprUuidpoolFormatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 3, 1, 1),
    _CfprUuidpoolFormatInstanceId_Type()
)
cfprUuidpoolFormatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprUuidpoolFormatInstanceId.setStatus("current")
_CfprUuidpoolFormatDn_Type = CfprManagedObjectDn
_CfprUuidpoolFormatDn_Object = MibTableColumn
cfprUuidpoolFormatDn = _CfprUuidpoolFormatDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 3, 1, 2),
    _CfprUuidpoolFormatDn_Type()
)
cfprUuidpoolFormatDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolFormatDn.setStatus("current")
_CfprUuidpoolFormatRn_Type = SnmpAdminString
_CfprUuidpoolFormatRn_Object = MibTableColumn
cfprUuidpoolFormatRn = _CfprUuidpoolFormatRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 3, 1, 3),
    _CfprUuidpoolFormatRn_Type()
)
cfprUuidpoolFormatRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolFormatRn.setStatus("current")
_CfprUuidpoolFormatFormat_Type = Unsigned64
_CfprUuidpoolFormatFormat_Object = MibTableColumn
cfprUuidpoolFormatFormat = _CfprUuidpoolFormatFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 3, 1, 4),
    _CfprUuidpoolFormatFormat_Type()
)
cfprUuidpoolFormatFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolFormatFormat.setStatus("current")
_CfprUuidpoolFormatMask_Type = CfprAddressUIDSuffxMask
_CfprUuidpoolFormatMask_Object = MibTableColumn
cfprUuidpoolFormatMask = _CfprUuidpoolFormatMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 3, 1, 5),
    _CfprUuidpoolFormatMask_Type()
)
cfprUuidpoolFormatMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolFormatMask.setStatus("current")
_CfprUuidpoolPoolTable_Object = MibTable
cfprUuidpoolPoolTable = _CfprUuidpoolPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4)
)
if mibBuilder.loadTexts:
    cfprUuidpoolPoolTable.setStatus("current")
_CfprUuidpoolPoolEntry_Object = MibTableRow
cfprUuidpoolPoolEntry = _CfprUuidpoolPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1)
)
cfprUuidpoolPoolEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-UUIDPOOL-MIB", "cfprUuidpoolPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cfprUuidpoolPoolEntry.setStatus("current")
_CfprUuidpoolPoolInstanceId_Type = CfprManagedObjectId
_CfprUuidpoolPoolInstanceId_Object = MibTableColumn
cfprUuidpoolPoolInstanceId = _CfprUuidpoolPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1, 1),
    _CfprUuidpoolPoolInstanceId_Type()
)
cfprUuidpoolPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolInstanceId.setStatus("current")
_CfprUuidpoolPoolDn_Type = CfprManagedObjectDn
_CfprUuidpoolPoolDn_Object = MibTableColumn
cfprUuidpoolPoolDn = _CfprUuidpoolPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1, 2),
    _CfprUuidpoolPoolDn_Type()
)
cfprUuidpoolPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolDn.setStatus("current")
_CfprUuidpoolPoolRn_Type = SnmpAdminString
_CfprUuidpoolPoolRn_Object = MibTableColumn
cfprUuidpoolPoolRn = _CfprUuidpoolPoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1, 3),
    _CfprUuidpoolPoolRn_Type()
)
cfprUuidpoolPoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolRn.setStatus("current")
_CfprUuidpoolPoolAssigned_Type = Gauge32
_CfprUuidpoolPoolAssigned_Object = MibTableColumn
cfprUuidpoolPoolAssigned = _CfprUuidpoolPoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1, 4),
    _CfprUuidpoolPoolAssigned_Type()
)
cfprUuidpoolPoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolAssigned.setStatus("current")
_CfprUuidpoolPoolAssignmentOrder_Type = CfprUuidpoolPoolAssignmentOrder
_CfprUuidpoolPoolAssignmentOrder_Object = MibTableColumn
cfprUuidpoolPoolAssignmentOrder = _CfprUuidpoolPoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1, 5),
    _CfprUuidpoolPoolAssignmentOrder_Type()
)
cfprUuidpoolPoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolAssignmentOrder.setStatus("current")
_CfprUuidpoolPoolDescr_Type = SnmpAdminString
_CfprUuidpoolPoolDescr_Object = MibTableColumn
cfprUuidpoolPoolDescr = _CfprUuidpoolPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1, 6),
    _CfprUuidpoolPoolDescr_Type()
)
cfprUuidpoolPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolDescr.setStatus("current")
_CfprUuidpoolPoolIntId_Type = SnmpAdminString
_CfprUuidpoolPoolIntId_Object = MibTableColumn
cfprUuidpoolPoolIntId = _CfprUuidpoolPoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1, 7),
    _CfprUuidpoolPoolIntId_Type()
)
cfprUuidpoolPoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolIntId.setStatus("current")
_CfprUuidpoolPoolName_Type = SnmpAdminString
_CfprUuidpoolPoolName_Object = MibTableColumn
cfprUuidpoolPoolName = _CfprUuidpoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1, 8),
    _CfprUuidpoolPoolName_Type()
)
cfprUuidpoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolName.setStatus("current")
_CfprUuidpoolPoolPolicyLevel_Type = Gauge32
_CfprUuidpoolPoolPolicyLevel_Object = MibTableColumn
cfprUuidpoolPoolPolicyLevel = _CfprUuidpoolPoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1, 9),
    _CfprUuidpoolPoolPolicyLevel_Type()
)
cfprUuidpoolPoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolPolicyLevel.setStatus("current")
_CfprUuidpoolPoolPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprUuidpoolPoolPolicyOwner_Object = MibTableColumn
cfprUuidpoolPoolPolicyOwner = _CfprUuidpoolPoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1, 10),
    _CfprUuidpoolPoolPolicyOwner_Type()
)
cfprUuidpoolPoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolPolicyOwner.setStatus("current")
_CfprUuidpoolPoolPrefix_Type = Unsigned64
_CfprUuidpoolPoolPrefix_Object = MibTableColumn
cfprUuidpoolPoolPrefix = _CfprUuidpoolPoolPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1, 11),
    _CfprUuidpoolPoolPrefix_Type()
)
cfprUuidpoolPoolPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolPrefix.setStatus("current")
_CfprUuidpoolPoolSize_Type = Gauge32
_CfprUuidpoolPoolSize_Object = MibTableColumn
cfprUuidpoolPoolSize = _CfprUuidpoolPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 4, 1, 12),
    _CfprUuidpoolPoolSize_Type()
)
cfprUuidpoolPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolSize.setStatus("current")
_CfprUuidpoolPoolableTable_Object = MibTable
cfprUuidpoolPoolableTable = _CfprUuidpoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 5)
)
if mibBuilder.loadTexts:
    cfprUuidpoolPoolableTable.setStatus("current")
_CfprUuidpoolPoolableEntry_Object = MibTableRow
cfprUuidpoolPoolableEntry = _CfprUuidpoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 5, 1)
)
cfprUuidpoolPoolableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-UUIDPOOL-MIB", "cfprUuidpoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprUuidpoolPoolableEntry.setStatus("current")
_CfprUuidpoolPoolableInstanceId_Type = CfprManagedObjectId
_CfprUuidpoolPoolableInstanceId_Object = MibTableColumn
cfprUuidpoolPoolableInstanceId = _CfprUuidpoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 5, 1, 1),
    _CfprUuidpoolPoolableInstanceId_Type()
)
cfprUuidpoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolableInstanceId.setStatus("current")
_CfprUuidpoolPoolableDn_Type = CfprManagedObjectDn
_CfprUuidpoolPoolableDn_Object = MibTableColumn
cfprUuidpoolPoolableDn = _CfprUuidpoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 5, 1, 2),
    _CfprUuidpoolPoolableDn_Type()
)
cfprUuidpoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolableDn.setStatus("current")
_CfprUuidpoolPoolableRn_Type = SnmpAdminString
_CfprUuidpoolPoolableRn_Object = MibTableColumn
cfprUuidpoolPoolableRn = _CfprUuidpoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 5, 1, 3),
    _CfprUuidpoolPoolableRn_Type()
)
cfprUuidpoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolableRn.setStatus("current")
_CfprUuidpoolPoolableId_Type = Unsigned64
_CfprUuidpoolPoolableId_Object = MibTableColumn
cfprUuidpoolPoolableId = _CfprUuidpoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 5, 1, 4),
    _CfprUuidpoolPoolableId_Type()
)
cfprUuidpoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolableId.setStatus("current")
_CfprUuidpoolPoolablePoolDn_Type = SnmpAdminString
_CfprUuidpoolPoolablePoolDn_Object = MibTableColumn
cfprUuidpoolPoolablePoolDn = _CfprUuidpoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 5, 1, 5),
    _CfprUuidpoolPoolablePoolDn_Type()
)
cfprUuidpoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPoolablePoolDn.setStatus("current")
_CfprUuidpoolPooledTable_Object = MibTable
cfprUuidpoolPooledTable = _CfprUuidpoolPooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 6)
)
if mibBuilder.loadTexts:
    cfprUuidpoolPooledTable.setStatus("current")
_CfprUuidpoolPooledEntry_Object = MibTableRow
cfprUuidpoolPooledEntry = _CfprUuidpoolPooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 6, 1)
)
cfprUuidpoolPooledEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-UUIDPOOL-MIB", "cfprUuidpoolPooledInstanceId"),
)
if mibBuilder.loadTexts:
    cfprUuidpoolPooledEntry.setStatus("current")
_CfprUuidpoolPooledInstanceId_Type = CfprManagedObjectId
_CfprUuidpoolPooledInstanceId_Object = MibTableColumn
cfprUuidpoolPooledInstanceId = _CfprUuidpoolPooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 6, 1, 1),
    _CfprUuidpoolPooledInstanceId_Type()
)
cfprUuidpoolPooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprUuidpoolPooledInstanceId.setStatus("current")
_CfprUuidpoolPooledDn_Type = CfprManagedObjectDn
_CfprUuidpoolPooledDn_Object = MibTableColumn
cfprUuidpoolPooledDn = _CfprUuidpoolPooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 6, 1, 2),
    _CfprUuidpoolPooledDn_Type()
)
cfprUuidpoolPooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPooledDn.setStatus("current")
_CfprUuidpoolPooledRn_Type = SnmpAdminString
_CfprUuidpoolPooledRn_Object = MibTableColumn
cfprUuidpoolPooledRn = _CfprUuidpoolPooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 6, 1, 3),
    _CfprUuidpoolPooledRn_Type()
)
cfprUuidpoolPooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPooledRn.setStatus("current")
_CfprUuidpoolPooledAssigned_Type = TruthValue
_CfprUuidpoolPooledAssigned_Object = MibTableColumn
cfprUuidpoolPooledAssigned = _CfprUuidpoolPooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 6, 1, 4),
    _CfprUuidpoolPooledAssigned_Type()
)
cfprUuidpoolPooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPooledAssigned.setStatus("current")
_CfprUuidpoolPooledAssignedToDn_Type = SnmpAdminString
_CfprUuidpoolPooledAssignedToDn_Object = MibTableColumn
cfprUuidpoolPooledAssignedToDn = _CfprUuidpoolPooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 6, 1, 5),
    _CfprUuidpoolPooledAssignedToDn_Type()
)
cfprUuidpoolPooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPooledAssignedToDn.setStatus("current")
_CfprUuidpoolPooledId_Type = Unsigned64
_CfprUuidpoolPooledId_Object = MibTableColumn
cfprUuidpoolPooledId = _CfprUuidpoolPooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 6, 1, 6),
    _CfprUuidpoolPooledId_Type()
)
cfprUuidpoolPooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPooledId.setStatus("current")
_CfprUuidpoolPooledPoolableDn_Type = SnmpAdminString
_CfprUuidpoolPooledPoolableDn_Object = MibTableColumn
cfprUuidpoolPooledPoolableDn = _CfprUuidpoolPooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 6, 1, 7),
    _CfprUuidpoolPooledPoolableDn_Type()
)
cfprUuidpoolPooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPooledPoolableDn.setStatus("current")
_CfprUuidpoolPooledPrevAssignedToDn_Type = SnmpAdminString
_CfprUuidpoolPooledPrevAssignedToDn_Object = MibTableColumn
cfprUuidpoolPooledPrevAssignedToDn = _CfprUuidpoolPooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 6, 1, 8),
    _CfprUuidpoolPooledPrevAssignedToDn_Type()
)
cfprUuidpoolPooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolPooledPrevAssignedToDn.setStatus("current")
_CfprUuidpoolUniverseTable_Object = MibTable
cfprUuidpoolUniverseTable = _CfprUuidpoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 7)
)
if mibBuilder.loadTexts:
    cfprUuidpoolUniverseTable.setStatus("current")
_CfprUuidpoolUniverseEntry_Object = MibTableRow
cfprUuidpoolUniverseEntry = _CfprUuidpoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 7, 1)
)
cfprUuidpoolUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-UUIDPOOL-MIB", "cfprUuidpoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprUuidpoolUniverseEntry.setStatus("current")
_CfprUuidpoolUniverseInstanceId_Type = CfprManagedObjectId
_CfprUuidpoolUniverseInstanceId_Object = MibTableColumn
cfprUuidpoolUniverseInstanceId = _CfprUuidpoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 7, 1, 1),
    _CfprUuidpoolUniverseInstanceId_Type()
)
cfprUuidpoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprUuidpoolUniverseInstanceId.setStatus("current")
_CfprUuidpoolUniverseDn_Type = CfprManagedObjectDn
_CfprUuidpoolUniverseDn_Object = MibTableColumn
cfprUuidpoolUniverseDn = _CfprUuidpoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 7, 1, 2),
    _CfprUuidpoolUniverseDn_Type()
)
cfprUuidpoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolUniverseDn.setStatus("current")
_CfprUuidpoolUniverseRn_Type = SnmpAdminString
_CfprUuidpoolUniverseRn_Object = MibTableColumn
cfprUuidpoolUniverseRn = _CfprUuidpoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 80, 7, 1, 3),
    _CfprUuidpoolUniverseRn_Type()
)
cfprUuidpoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprUuidpoolUniverseRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-UUIDPOOL-MIB",
    **{"cfprUuidpoolObjects": cfprUuidpoolObjects,
       "cfprUuidpoolAddrTable": cfprUuidpoolAddrTable,
       "cfprUuidpoolAddrEntry": cfprUuidpoolAddrEntry,
       "cfprUuidpoolAddrInstanceId": cfprUuidpoolAddrInstanceId,
       "cfprUuidpoolAddrDn": cfprUuidpoolAddrDn,
       "cfprUuidpoolAddrRn": cfprUuidpoolAddrRn,
       "cfprUuidpoolAddrAssigned": cfprUuidpoolAddrAssigned,
       "cfprUuidpoolAddrAssignedToDn": cfprUuidpoolAddrAssignedToDn,
       "cfprUuidpoolAddrGlobalAssignedCnt": cfprUuidpoolAddrGlobalAssignedCnt,
       "cfprUuidpoolAddrGlobalDefinedCnt": cfprUuidpoolAddrGlobalDefinedCnt,
       "cfprUuidpoolAddrId": cfprUuidpoolAddrId,
       "cfprUuidpoolAddrOwner": cfprUuidpoolAddrOwner,
       "cfprUuidpoolBlockTable": cfprUuidpoolBlockTable,
       "cfprUuidpoolBlockEntry": cfprUuidpoolBlockEntry,
       "cfprUuidpoolBlockInstanceId": cfprUuidpoolBlockInstanceId,
       "cfprUuidpoolBlockDn": cfprUuidpoolBlockDn,
       "cfprUuidpoolBlockRn": cfprUuidpoolBlockRn,
       "cfprUuidpoolBlockFrom": cfprUuidpoolBlockFrom,
       "cfprUuidpoolBlockTo": cfprUuidpoolBlockTo,
       "cfprUuidpoolFormatTable": cfprUuidpoolFormatTable,
       "cfprUuidpoolFormatEntry": cfprUuidpoolFormatEntry,
       "cfprUuidpoolFormatInstanceId": cfprUuidpoolFormatInstanceId,
       "cfprUuidpoolFormatDn": cfprUuidpoolFormatDn,
       "cfprUuidpoolFormatRn": cfprUuidpoolFormatRn,
       "cfprUuidpoolFormatFormat": cfprUuidpoolFormatFormat,
       "cfprUuidpoolFormatMask": cfprUuidpoolFormatMask,
       "cfprUuidpoolPoolTable": cfprUuidpoolPoolTable,
       "cfprUuidpoolPoolEntry": cfprUuidpoolPoolEntry,
       "cfprUuidpoolPoolInstanceId": cfprUuidpoolPoolInstanceId,
       "cfprUuidpoolPoolDn": cfprUuidpoolPoolDn,
       "cfprUuidpoolPoolRn": cfprUuidpoolPoolRn,
       "cfprUuidpoolPoolAssigned": cfprUuidpoolPoolAssigned,
       "cfprUuidpoolPoolAssignmentOrder": cfprUuidpoolPoolAssignmentOrder,
       "cfprUuidpoolPoolDescr": cfprUuidpoolPoolDescr,
       "cfprUuidpoolPoolIntId": cfprUuidpoolPoolIntId,
       "cfprUuidpoolPoolName": cfprUuidpoolPoolName,
       "cfprUuidpoolPoolPolicyLevel": cfprUuidpoolPoolPolicyLevel,
       "cfprUuidpoolPoolPolicyOwner": cfprUuidpoolPoolPolicyOwner,
       "cfprUuidpoolPoolPrefix": cfprUuidpoolPoolPrefix,
       "cfprUuidpoolPoolSize": cfprUuidpoolPoolSize,
       "cfprUuidpoolPoolableTable": cfprUuidpoolPoolableTable,
       "cfprUuidpoolPoolableEntry": cfprUuidpoolPoolableEntry,
       "cfprUuidpoolPoolableInstanceId": cfprUuidpoolPoolableInstanceId,
       "cfprUuidpoolPoolableDn": cfprUuidpoolPoolableDn,
       "cfprUuidpoolPoolableRn": cfprUuidpoolPoolableRn,
       "cfprUuidpoolPoolableId": cfprUuidpoolPoolableId,
       "cfprUuidpoolPoolablePoolDn": cfprUuidpoolPoolablePoolDn,
       "cfprUuidpoolPooledTable": cfprUuidpoolPooledTable,
       "cfprUuidpoolPooledEntry": cfprUuidpoolPooledEntry,
       "cfprUuidpoolPooledInstanceId": cfprUuidpoolPooledInstanceId,
       "cfprUuidpoolPooledDn": cfprUuidpoolPooledDn,
       "cfprUuidpoolPooledRn": cfprUuidpoolPooledRn,
       "cfprUuidpoolPooledAssigned": cfprUuidpoolPooledAssigned,
       "cfprUuidpoolPooledAssignedToDn": cfprUuidpoolPooledAssignedToDn,
       "cfprUuidpoolPooledId": cfprUuidpoolPooledId,
       "cfprUuidpoolPooledPoolableDn": cfprUuidpoolPooledPoolableDn,
       "cfprUuidpoolPooledPrevAssignedToDn": cfprUuidpoolPooledPrevAssignedToDn,
       "cfprUuidpoolUniverseTable": cfprUuidpoolUniverseTable,
       "cfprUuidpoolUniverseEntry": cfprUuidpoolUniverseEntry,
       "cfprUuidpoolUniverseInstanceId": cfprUuidpoolUniverseInstanceId,
       "cfprUuidpoolUniverseDn": cfprUuidpoolUniverseDn,
       "cfprUuidpoolUniverseRn": cfprUuidpoolUniverseRn}
)
