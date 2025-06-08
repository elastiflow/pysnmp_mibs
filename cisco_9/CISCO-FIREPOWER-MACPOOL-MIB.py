# SNMP MIB module (CISCO-FIREPOWER-MACPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-MACPOOL-MIB.mib
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

(CfprAddressMACMask,
 CfprMacpoolPoolAssignmentOrder,
 CfprPolicyPolicyOwner,
 CfprPoolElementOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprAddressMACMask",
    "CfprMacpoolPoolAssignmentOrder",
    "CfprPolicyPolicyOwner",
    "CfprPoolElementOwner")

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

cfprMacpoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprMacpoolAddrTable_Object = MibTable
cfprMacpoolAddrTable = _CfprMacpoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 1)
)
if mibBuilder.loadTexts:
    cfprMacpoolAddrTable.setStatus("current")
_CfprMacpoolAddrEntry_Object = MibTableRow
cfprMacpoolAddrEntry = _CfprMacpoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 1, 1)
)
cfprMacpoolAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MACPOOL-MIB", "cfprMacpoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMacpoolAddrEntry.setStatus("current")
_CfprMacpoolAddrInstanceId_Type = CfprManagedObjectId
_CfprMacpoolAddrInstanceId_Object = MibTableColumn
cfprMacpoolAddrInstanceId = _CfprMacpoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 1, 1, 1),
    _CfprMacpoolAddrInstanceId_Type()
)
cfprMacpoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMacpoolAddrInstanceId.setStatus("current")
_CfprMacpoolAddrDn_Type = CfprManagedObjectDn
_CfprMacpoolAddrDn_Object = MibTableColumn
cfprMacpoolAddrDn = _CfprMacpoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 1, 1, 2),
    _CfprMacpoolAddrDn_Type()
)
cfprMacpoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolAddrDn.setStatus("current")
_CfprMacpoolAddrRn_Type = SnmpAdminString
_CfprMacpoolAddrRn_Object = MibTableColumn
cfprMacpoolAddrRn = _CfprMacpoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 1, 1, 3),
    _CfprMacpoolAddrRn_Type()
)
cfprMacpoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolAddrRn.setStatus("current")
_CfprMacpoolAddrAssigned_Type = TruthValue
_CfprMacpoolAddrAssigned_Object = MibTableColumn
cfprMacpoolAddrAssigned = _CfprMacpoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 1, 1, 4),
    _CfprMacpoolAddrAssigned_Type()
)
cfprMacpoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolAddrAssigned.setStatus("current")
_CfprMacpoolAddrAssignedToDn_Type = SnmpAdminString
_CfprMacpoolAddrAssignedToDn_Object = MibTableColumn
cfprMacpoolAddrAssignedToDn = _CfprMacpoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 1, 1, 5),
    _CfprMacpoolAddrAssignedToDn_Type()
)
cfprMacpoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolAddrAssignedToDn.setStatus("current")
_CfprMacpoolAddrGlobalAssignedCnt_Type = Gauge32
_CfprMacpoolAddrGlobalAssignedCnt_Object = MibTableColumn
cfprMacpoolAddrGlobalAssignedCnt = _CfprMacpoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 1, 1, 6),
    _CfprMacpoolAddrGlobalAssignedCnt_Type()
)
cfprMacpoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolAddrGlobalAssignedCnt.setStatus("current")
_CfprMacpoolAddrGlobalDefinedCnt_Type = Gauge32
_CfprMacpoolAddrGlobalDefinedCnt_Object = MibTableColumn
cfprMacpoolAddrGlobalDefinedCnt = _CfprMacpoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 1, 1, 7),
    _CfprMacpoolAddrGlobalDefinedCnt_Type()
)
cfprMacpoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolAddrGlobalDefinedCnt.setStatus("current")
_CfprMacpoolAddrId_Type = MacAddress
_CfprMacpoolAddrId_Object = MibTableColumn
cfprMacpoolAddrId = _CfprMacpoolAddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 1, 1, 8),
    _CfprMacpoolAddrId_Type()
)
cfprMacpoolAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolAddrId.setStatus("current")
_CfprMacpoolAddrOwner_Type = CfprPoolElementOwner
_CfprMacpoolAddrOwner_Object = MibTableColumn
cfprMacpoolAddrOwner = _CfprMacpoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 1, 1, 9),
    _CfprMacpoolAddrOwner_Type()
)
cfprMacpoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolAddrOwner.setStatus("current")
_CfprMacpoolBlockTable_Object = MibTable
cfprMacpoolBlockTable = _CfprMacpoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 2)
)
if mibBuilder.loadTexts:
    cfprMacpoolBlockTable.setStatus("current")
_CfprMacpoolBlockEntry_Object = MibTableRow
cfprMacpoolBlockEntry = _CfprMacpoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 2, 1)
)
cfprMacpoolBlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MACPOOL-MIB", "cfprMacpoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMacpoolBlockEntry.setStatus("current")
_CfprMacpoolBlockInstanceId_Type = CfprManagedObjectId
_CfprMacpoolBlockInstanceId_Object = MibTableColumn
cfprMacpoolBlockInstanceId = _CfprMacpoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 2, 1, 1),
    _CfprMacpoolBlockInstanceId_Type()
)
cfprMacpoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMacpoolBlockInstanceId.setStatus("current")
_CfprMacpoolBlockDn_Type = CfprManagedObjectDn
_CfprMacpoolBlockDn_Object = MibTableColumn
cfprMacpoolBlockDn = _CfprMacpoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 2, 1, 2),
    _CfprMacpoolBlockDn_Type()
)
cfprMacpoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolBlockDn.setStatus("current")
_CfprMacpoolBlockRn_Type = SnmpAdminString
_CfprMacpoolBlockRn_Object = MibTableColumn
cfprMacpoolBlockRn = _CfprMacpoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 2, 1, 3),
    _CfprMacpoolBlockRn_Type()
)
cfprMacpoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolBlockRn.setStatus("current")
_CfprMacpoolBlockFrom_Type = MacAddress
_CfprMacpoolBlockFrom_Object = MibTableColumn
cfprMacpoolBlockFrom = _CfprMacpoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 2, 1, 4),
    _CfprMacpoolBlockFrom_Type()
)
cfprMacpoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolBlockFrom.setStatus("current")
_CfprMacpoolBlockTo_Type = MacAddress
_CfprMacpoolBlockTo_Object = MibTableColumn
cfprMacpoolBlockTo = _CfprMacpoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 2, 1, 5),
    _CfprMacpoolBlockTo_Type()
)
cfprMacpoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolBlockTo.setStatus("current")
_CfprMacpoolFormatTable_Object = MibTable
cfprMacpoolFormatTable = _CfprMacpoolFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 3)
)
if mibBuilder.loadTexts:
    cfprMacpoolFormatTable.setStatus("current")
_CfprMacpoolFormatEntry_Object = MibTableRow
cfprMacpoolFormatEntry = _CfprMacpoolFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 3, 1)
)
cfprMacpoolFormatEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MACPOOL-MIB", "cfprMacpoolFormatInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMacpoolFormatEntry.setStatus("current")
_CfprMacpoolFormatInstanceId_Type = CfprManagedObjectId
_CfprMacpoolFormatInstanceId_Object = MibTableColumn
cfprMacpoolFormatInstanceId = _CfprMacpoolFormatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 3, 1, 1),
    _CfprMacpoolFormatInstanceId_Type()
)
cfprMacpoolFormatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMacpoolFormatInstanceId.setStatus("current")
_CfprMacpoolFormatDn_Type = CfprManagedObjectDn
_CfprMacpoolFormatDn_Object = MibTableColumn
cfprMacpoolFormatDn = _CfprMacpoolFormatDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 3, 1, 2),
    _CfprMacpoolFormatDn_Type()
)
cfprMacpoolFormatDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolFormatDn.setStatus("current")
_CfprMacpoolFormatRn_Type = SnmpAdminString
_CfprMacpoolFormatRn_Object = MibTableColumn
cfprMacpoolFormatRn = _CfprMacpoolFormatRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 3, 1, 3),
    _CfprMacpoolFormatRn_Type()
)
cfprMacpoolFormatRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolFormatRn.setStatus("current")
_CfprMacpoolFormatFormat_Type = MacAddress
_CfprMacpoolFormatFormat_Object = MibTableColumn
cfprMacpoolFormatFormat = _CfprMacpoolFormatFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 3, 1, 4),
    _CfprMacpoolFormatFormat_Type()
)
cfprMacpoolFormatFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolFormatFormat.setStatus("current")
_CfprMacpoolFormatMask_Type = CfprAddressMACMask
_CfprMacpoolFormatMask_Object = MibTableColumn
cfprMacpoolFormatMask = _CfprMacpoolFormatMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 3, 1, 5),
    _CfprMacpoolFormatMask_Type()
)
cfprMacpoolFormatMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolFormatMask.setStatus("current")
_CfprMacpoolPoolTable_Object = MibTable
cfprMacpoolPoolTable = _CfprMacpoolPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4)
)
if mibBuilder.loadTexts:
    cfprMacpoolPoolTable.setStatus("current")
_CfprMacpoolPoolEntry_Object = MibTableRow
cfprMacpoolPoolEntry = _CfprMacpoolPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4, 1)
)
cfprMacpoolPoolEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MACPOOL-MIB", "cfprMacpoolPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMacpoolPoolEntry.setStatus("current")
_CfprMacpoolPoolInstanceId_Type = CfprManagedObjectId
_CfprMacpoolPoolInstanceId_Object = MibTableColumn
cfprMacpoolPoolInstanceId = _CfprMacpoolPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4, 1, 1),
    _CfprMacpoolPoolInstanceId_Type()
)
cfprMacpoolPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMacpoolPoolInstanceId.setStatus("current")
_CfprMacpoolPoolDn_Type = CfprManagedObjectDn
_CfprMacpoolPoolDn_Object = MibTableColumn
cfprMacpoolPoolDn = _CfprMacpoolPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4, 1, 2),
    _CfprMacpoolPoolDn_Type()
)
cfprMacpoolPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolDn.setStatus("current")
_CfprMacpoolPoolRn_Type = SnmpAdminString
_CfprMacpoolPoolRn_Object = MibTableColumn
cfprMacpoolPoolRn = _CfprMacpoolPoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4, 1, 3),
    _CfprMacpoolPoolRn_Type()
)
cfprMacpoolPoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolRn.setStatus("current")
_CfprMacpoolPoolAssigned_Type = Gauge32
_CfprMacpoolPoolAssigned_Object = MibTableColumn
cfprMacpoolPoolAssigned = _CfprMacpoolPoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4, 1, 4),
    _CfprMacpoolPoolAssigned_Type()
)
cfprMacpoolPoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolAssigned.setStatus("current")
_CfprMacpoolPoolAssignmentOrder_Type = CfprMacpoolPoolAssignmentOrder
_CfprMacpoolPoolAssignmentOrder_Object = MibTableColumn
cfprMacpoolPoolAssignmentOrder = _CfprMacpoolPoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4, 1, 5),
    _CfprMacpoolPoolAssignmentOrder_Type()
)
cfprMacpoolPoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolAssignmentOrder.setStatus("current")
_CfprMacpoolPoolDescr_Type = SnmpAdminString
_CfprMacpoolPoolDescr_Object = MibTableColumn
cfprMacpoolPoolDescr = _CfprMacpoolPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4, 1, 6),
    _CfprMacpoolPoolDescr_Type()
)
cfprMacpoolPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolDescr.setStatus("current")
_CfprMacpoolPoolIntId_Type = SnmpAdminString
_CfprMacpoolPoolIntId_Object = MibTableColumn
cfprMacpoolPoolIntId = _CfprMacpoolPoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4, 1, 7),
    _CfprMacpoolPoolIntId_Type()
)
cfprMacpoolPoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolIntId.setStatus("current")
_CfprMacpoolPoolName_Type = SnmpAdminString
_CfprMacpoolPoolName_Object = MibTableColumn
cfprMacpoolPoolName = _CfprMacpoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4, 1, 8),
    _CfprMacpoolPoolName_Type()
)
cfprMacpoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolName.setStatus("current")
_CfprMacpoolPoolPolicyLevel_Type = Gauge32
_CfprMacpoolPoolPolicyLevel_Object = MibTableColumn
cfprMacpoolPoolPolicyLevel = _CfprMacpoolPoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4, 1, 9),
    _CfprMacpoolPoolPolicyLevel_Type()
)
cfprMacpoolPoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolPolicyLevel.setStatus("current")
_CfprMacpoolPoolPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprMacpoolPoolPolicyOwner_Object = MibTableColumn
cfprMacpoolPoolPolicyOwner = _CfprMacpoolPoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4, 1, 10),
    _CfprMacpoolPoolPolicyOwner_Type()
)
cfprMacpoolPoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolPolicyOwner.setStatus("current")
_CfprMacpoolPoolSize_Type = Gauge32
_CfprMacpoolPoolSize_Object = MibTableColumn
cfprMacpoolPoolSize = _CfprMacpoolPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 4, 1, 11),
    _CfprMacpoolPoolSize_Type()
)
cfprMacpoolPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolSize.setStatus("current")
_CfprMacpoolPoolableTable_Object = MibTable
cfprMacpoolPoolableTable = _CfprMacpoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 5)
)
if mibBuilder.loadTexts:
    cfprMacpoolPoolableTable.setStatus("current")
_CfprMacpoolPoolableEntry_Object = MibTableRow
cfprMacpoolPoolableEntry = _CfprMacpoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 5, 1)
)
cfprMacpoolPoolableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MACPOOL-MIB", "cfprMacpoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMacpoolPoolableEntry.setStatus("current")
_CfprMacpoolPoolableInstanceId_Type = CfprManagedObjectId
_CfprMacpoolPoolableInstanceId_Object = MibTableColumn
cfprMacpoolPoolableInstanceId = _CfprMacpoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 5, 1, 1),
    _CfprMacpoolPoolableInstanceId_Type()
)
cfprMacpoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMacpoolPoolableInstanceId.setStatus("current")
_CfprMacpoolPoolableDn_Type = CfprManagedObjectDn
_CfprMacpoolPoolableDn_Object = MibTableColumn
cfprMacpoolPoolableDn = _CfprMacpoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 5, 1, 2),
    _CfprMacpoolPoolableDn_Type()
)
cfprMacpoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolableDn.setStatus("current")
_CfprMacpoolPoolableRn_Type = SnmpAdminString
_CfprMacpoolPoolableRn_Object = MibTableColumn
cfprMacpoolPoolableRn = _CfprMacpoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 5, 1, 3),
    _CfprMacpoolPoolableRn_Type()
)
cfprMacpoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolableRn.setStatus("current")
_CfprMacpoolPoolableId_Type = Unsigned64
_CfprMacpoolPoolableId_Object = MibTableColumn
cfprMacpoolPoolableId = _CfprMacpoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 5, 1, 4),
    _CfprMacpoolPoolableId_Type()
)
cfprMacpoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolableId.setStatus("current")
_CfprMacpoolPoolablePoolDn_Type = SnmpAdminString
_CfprMacpoolPoolablePoolDn_Object = MibTableColumn
cfprMacpoolPoolablePoolDn = _CfprMacpoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 5, 1, 5),
    _CfprMacpoolPoolablePoolDn_Type()
)
cfprMacpoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPoolablePoolDn.setStatus("current")
_CfprMacpoolPooledTable_Object = MibTable
cfprMacpoolPooledTable = _CfprMacpoolPooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 6)
)
if mibBuilder.loadTexts:
    cfprMacpoolPooledTable.setStatus("current")
_CfprMacpoolPooledEntry_Object = MibTableRow
cfprMacpoolPooledEntry = _CfprMacpoolPooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 6, 1)
)
cfprMacpoolPooledEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MACPOOL-MIB", "cfprMacpoolPooledInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMacpoolPooledEntry.setStatus("current")
_CfprMacpoolPooledInstanceId_Type = CfprManagedObjectId
_CfprMacpoolPooledInstanceId_Object = MibTableColumn
cfprMacpoolPooledInstanceId = _CfprMacpoolPooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 6, 1, 1),
    _CfprMacpoolPooledInstanceId_Type()
)
cfprMacpoolPooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMacpoolPooledInstanceId.setStatus("current")
_CfprMacpoolPooledDn_Type = CfprManagedObjectDn
_CfprMacpoolPooledDn_Object = MibTableColumn
cfprMacpoolPooledDn = _CfprMacpoolPooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 6, 1, 2),
    _CfprMacpoolPooledDn_Type()
)
cfprMacpoolPooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPooledDn.setStatus("current")
_CfprMacpoolPooledRn_Type = SnmpAdminString
_CfprMacpoolPooledRn_Object = MibTableColumn
cfprMacpoolPooledRn = _CfprMacpoolPooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 6, 1, 3),
    _CfprMacpoolPooledRn_Type()
)
cfprMacpoolPooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPooledRn.setStatus("current")
_CfprMacpoolPooledAssigned_Type = TruthValue
_CfprMacpoolPooledAssigned_Object = MibTableColumn
cfprMacpoolPooledAssigned = _CfprMacpoolPooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 6, 1, 4),
    _CfprMacpoolPooledAssigned_Type()
)
cfprMacpoolPooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPooledAssigned.setStatus("current")
_CfprMacpoolPooledAssignedToDn_Type = SnmpAdminString
_CfprMacpoolPooledAssignedToDn_Object = MibTableColumn
cfprMacpoolPooledAssignedToDn = _CfprMacpoolPooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 6, 1, 5),
    _CfprMacpoolPooledAssignedToDn_Type()
)
cfprMacpoolPooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPooledAssignedToDn.setStatus("current")
_CfprMacpoolPooledId_Type = MacAddress
_CfprMacpoolPooledId_Object = MibTableColumn
cfprMacpoolPooledId = _CfprMacpoolPooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 6, 1, 6),
    _CfprMacpoolPooledId_Type()
)
cfprMacpoolPooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPooledId.setStatus("current")
_CfprMacpoolPooledPoolableDn_Type = SnmpAdminString
_CfprMacpoolPooledPoolableDn_Object = MibTableColumn
cfprMacpoolPooledPoolableDn = _CfprMacpoolPooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 6, 1, 7),
    _CfprMacpoolPooledPoolableDn_Type()
)
cfprMacpoolPooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPooledPoolableDn.setStatus("current")
_CfprMacpoolPooledPrevAssignedToDn_Type = SnmpAdminString
_CfprMacpoolPooledPrevAssignedToDn_Object = MibTableColumn
cfprMacpoolPooledPrevAssignedToDn = _CfprMacpoolPooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 6, 1, 8),
    _CfprMacpoolPooledPrevAssignedToDn_Type()
)
cfprMacpoolPooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolPooledPrevAssignedToDn.setStatus("current")
_CfprMacpoolUniverseTable_Object = MibTable
cfprMacpoolUniverseTable = _CfprMacpoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 7)
)
if mibBuilder.loadTexts:
    cfprMacpoolUniverseTable.setStatus("current")
_CfprMacpoolUniverseEntry_Object = MibTableRow
cfprMacpoolUniverseEntry = _CfprMacpoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 7, 1)
)
cfprMacpoolUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-MACPOOL-MIB", "cfprMacpoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprMacpoolUniverseEntry.setStatus("current")
_CfprMacpoolUniverseInstanceId_Type = CfprManagedObjectId
_CfprMacpoolUniverseInstanceId_Object = MibTableColumn
cfprMacpoolUniverseInstanceId = _CfprMacpoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 7, 1, 1),
    _CfprMacpoolUniverseInstanceId_Type()
)
cfprMacpoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprMacpoolUniverseInstanceId.setStatus("current")
_CfprMacpoolUniverseDn_Type = CfprManagedObjectDn
_CfprMacpoolUniverseDn_Object = MibTableColumn
cfprMacpoolUniverseDn = _CfprMacpoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 7, 1, 2),
    _CfprMacpoolUniverseDn_Type()
)
cfprMacpoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolUniverseDn.setStatus("current")
_CfprMacpoolUniverseRn_Type = SnmpAdminString
_CfprMacpoolUniverseRn_Object = MibTableColumn
cfprMacpoolUniverseRn = _CfprMacpoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 49, 7, 1, 3),
    _CfprMacpoolUniverseRn_Type()
)
cfprMacpoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprMacpoolUniverseRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-MACPOOL-MIB",
    **{"cfprMacpoolObjects": cfprMacpoolObjects,
       "cfprMacpoolAddrTable": cfprMacpoolAddrTable,
       "cfprMacpoolAddrEntry": cfprMacpoolAddrEntry,
       "cfprMacpoolAddrInstanceId": cfprMacpoolAddrInstanceId,
       "cfprMacpoolAddrDn": cfprMacpoolAddrDn,
       "cfprMacpoolAddrRn": cfprMacpoolAddrRn,
       "cfprMacpoolAddrAssigned": cfprMacpoolAddrAssigned,
       "cfprMacpoolAddrAssignedToDn": cfprMacpoolAddrAssignedToDn,
       "cfprMacpoolAddrGlobalAssignedCnt": cfprMacpoolAddrGlobalAssignedCnt,
       "cfprMacpoolAddrGlobalDefinedCnt": cfprMacpoolAddrGlobalDefinedCnt,
       "cfprMacpoolAddrId": cfprMacpoolAddrId,
       "cfprMacpoolAddrOwner": cfprMacpoolAddrOwner,
       "cfprMacpoolBlockTable": cfprMacpoolBlockTable,
       "cfprMacpoolBlockEntry": cfprMacpoolBlockEntry,
       "cfprMacpoolBlockInstanceId": cfprMacpoolBlockInstanceId,
       "cfprMacpoolBlockDn": cfprMacpoolBlockDn,
       "cfprMacpoolBlockRn": cfprMacpoolBlockRn,
       "cfprMacpoolBlockFrom": cfprMacpoolBlockFrom,
       "cfprMacpoolBlockTo": cfprMacpoolBlockTo,
       "cfprMacpoolFormatTable": cfprMacpoolFormatTable,
       "cfprMacpoolFormatEntry": cfprMacpoolFormatEntry,
       "cfprMacpoolFormatInstanceId": cfprMacpoolFormatInstanceId,
       "cfprMacpoolFormatDn": cfprMacpoolFormatDn,
       "cfprMacpoolFormatRn": cfprMacpoolFormatRn,
       "cfprMacpoolFormatFormat": cfprMacpoolFormatFormat,
       "cfprMacpoolFormatMask": cfprMacpoolFormatMask,
       "cfprMacpoolPoolTable": cfprMacpoolPoolTable,
       "cfprMacpoolPoolEntry": cfprMacpoolPoolEntry,
       "cfprMacpoolPoolInstanceId": cfprMacpoolPoolInstanceId,
       "cfprMacpoolPoolDn": cfprMacpoolPoolDn,
       "cfprMacpoolPoolRn": cfprMacpoolPoolRn,
       "cfprMacpoolPoolAssigned": cfprMacpoolPoolAssigned,
       "cfprMacpoolPoolAssignmentOrder": cfprMacpoolPoolAssignmentOrder,
       "cfprMacpoolPoolDescr": cfprMacpoolPoolDescr,
       "cfprMacpoolPoolIntId": cfprMacpoolPoolIntId,
       "cfprMacpoolPoolName": cfprMacpoolPoolName,
       "cfprMacpoolPoolPolicyLevel": cfprMacpoolPoolPolicyLevel,
       "cfprMacpoolPoolPolicyOwner": cfprMacpoolPoolPolicyOwner,
       "cfprMacpoolPoolSize": cfprMacpoolPoolSize,
       "cfprMacpoolPoolableTable": cfprMacpoolPoolableTable,
       "cfprMacpoolPoolableEntry": cfprMacpoolPoolableEntry,
       "cfprMacpoolPoolableInstanceId": cfprMacpoolPoolableInstanceId,
       "cfprMacpoolPoolableDn": cfprMacpoolPoolableDn,
       "cfprMacpoolPoolableRn": cfprMacpoolPoolableRn,
       "cfprMacpoolPoolableId": cfprMacpoolPoolableId,
       "cfprMacpoolPoolablePoolDn": cfprMacpoolPoolablePoolDn,
       "cfprMacpoolPooledTable": cfprMacpoolPooledTable,
       "cfprMacpoolPooledEntry": cfprMacpoolPooledEntry,
       "cfprMacpoolPooledInstanceId": cfprMacpoolPooledInstanceId,
       "cfprMacpoolPooledDn": cfprMacpoolPooledDn,
       "cfprMacpoolPooledRn": cfprMacpoolPooledRn,
       "cfprMacpoolPooledAssigned": cfprMacpoolPooledAssigned,
       "cfprMacpoolPooledAssignedToDn": cfprMacpoolPooledAssignedToDn,
       "cfprMacpoolPooledId": cfprMacpoolPooledId,
       "cfprMacpoolPooledPoolableDn": cfprMacpoolPooledPoolableDn,
       "cfprMacpoolPooledPrevAssignedToDn": cfprMacpoolPooledPrevAssignedToDn,
       "cfprMacpoolUniverseTable": cfprMacpoolUniverseTable,
       "cfprMacpoolUniverseEntry": cfprMacpoolUniverseEntry,
       "cfprMacpoolUniverseInstanceId": cfprMacpoolUniverseInstanceId,
       "cfprMacpoolUniverseDn": cfprMacpoolUniverseDn,
       "cfprMacpoolUniverseRn": cfprMacpoolUniverseRn}
)
