# SNMP MIB module (CISCO-FIREPOWER-AP-MACPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-MACPOOL-MIB.mib
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

(CfprApAddressMACMask,
 CfprApMacpoolPoolAssignmentOrder,
 CfprApPolicyPolicyOwner,
 CfprApPoolElementOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApAddressMACMask",
    "CfprApMacpoolPoolAssignmentOrder",
    "CfprApPolicyPolicyOwner",
    "CfprApPoolElementOwner")

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

cfprApMacpoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApMacpoolAddrTable_Object = MibTable
cfprApMacpoolAddrTable = _CfprApMacpoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 1)
)
if mibBuilder.loadTexts:
    cfprApMacpoolAddrTable.setStatus("current")
_CfprApMacpoolAddrEntry_Object = MibTableRow
cfprApMacpoolAddrEntry = _CfprApMacpoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 1, 1)
)
cfprApMacpoolAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MACPOOL-MIB", "cfprApMacpoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMacpoolAddrEntry.setStatus("current")
_CfprApMacpoolAddrInstanceId_Type = CfprApManagedObjectId
_CfprApMacpoolAddrInstanceId_Object = MibTableColumn
cfprApMacpoolAddrInstanceId = _CfprApMacpoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 1, 1, 1),
    _CfprApMacpoolAddrInstanceId_Type()
)
cfprApMacpoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMacpoolAddrInstanceId.setStatus("current")
_CfprApMacpoolAddrDn_Type = CfprApManagedObjectDn
_CfprApMacpoolAddrDn_Object = MibTableColumn
cfprApMacpoolAddrDn = _CfprApMacpoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 1, 1, 2),
    _CfprApMacpoolAddrDn_Type()
)
cfprApMacpoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolAddrDn.setStatus("current")
_CfprApMacpoolAddrRn_Type = SnmpAdminString
_CfprApMacpoolAddrRn_Object = MibTableColumn
cfprApMacpoolAddrRn = _CfprApMacpoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 1, 1, 3),
    _CfprApMacpoolAddrRn_Type()
)
cfprApMacpoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolAddrRn.setStatus("current")
_CfprApMacpoolAddrAssigned_Type = TruthValue
_CfprApMacpoolAddrAssigned_Object = MibTableColumn
cfprApMacpoolAddrAssigned = _CfprApMacpoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 1, 1, 4),
    _CfprApMacpoolAddrAssigned_Type()
)
cfprApMacpoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolAddrAssigned.setStatus("current")
_CfprApMacpoolAddrAssignedToDn_Type = SnmpAdminString
_CfprApMacpoolAddrAssignedToDn_Object = MibTableColumn
cfprApMacpoolAddrAssignedToDn = _CfprApMacpoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 1, 1, 5),
    _CfprApMacpoolAddrAssignedToDn_Type()
)
cfprApMacpoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolAddrAssignedToDn.setStatus("current")
_CfprApMacpoolAddrGlobalAssignedCnt_Type = Gauge32
_CfprApMacpoolAddrGlobalAssignedCnt_Object = MibTableColumn
cfprApMacpoolAddrGlobalAssignedCnt = _CfprApMacpoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 1, 1, 6),
    _CfprApMacpoolAddrGlobalAssignedCnt_Type()
)
cfprApMacpoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolAddrGlobalAssignedCnt.setStatus("current")
_CfprApMacpoolAddrGlobalDefinedCnt_Type = Gauge32
_CfprApMacpoolAddrGlobalDefinedCnt_Object = MibTableColumn
cfprApMacpoolAddrGlobalDefinedCnt = _CfprApMacpoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 1, 1, 7),
    _CfprApMacpoolAddrGlobalDefinedCnt_Type()
)
cfprApMacpoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolAddrGlobalDefinedCnt.setStatus("current")
_CfprApMacpoolAddrId_Type = MacAddress
_CfprApMacpoolAddrId_Object = MibTableColumn
cfprApMacpoolAddrId = _CfprApMacpoolAddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 1, 1, 8),
    _CfprApMacpoolAddrId_Type()
)
cfprApMacpoolAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolAddrId.setStatus("current")
_CfprApMacpoolAddrOwner_Type = CfprApPoolElementOwner
_CfprApMacpoolAddrOwner_Object = MibTableColumn
cfprApMacpoolAddrOwner = _CfprApMacpoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 1, 1, 9),
    _CfprApMacpoolAddrOwner_Type()
)
cfprApMacpoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolAddrOwner.setStatus("current")
_CfprApMacpoolBlockTable_Object = MibTable
cfprApMacpoolBlockTable = _CfprApMacpoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 2)
)
if mibBuilder.loadTexts:
    cfprApMacpoolBlockTable.setStatus("current")
_CfprApMacpoolBlockEntry_Object = MibTableRow
cfprApMacpoolBlockEntry = _CfprApMacpoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 2, 1)
)
cfprApMacpoolBlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MACPOOL-MIB", "cfprApMacpoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMacpoolBlockEntry.setStatus("current")
_CfprApMacpoolBlockInstanceId_Type = CfprApManagedObjectId
_CfprApMacpoolBlockInstanceId_Object = MibTableColumn
cfprApMacpoolBlockInstanceId = _CfprApMacpoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 2, 1, 1),
    _CfprApMacpoolBlockInstanceId_Type()
)
cfprApMacpoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMacpoolBlockInstanceId.setStatus("current")
_CfprApMacpoolBlockDn_Type = CfprApManagedObjectDn
_CfprApMacpoolBlockDn_Object = MibTableColumn
cfprApMacpoolBlockDn = _CfprApMacpoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 2, 1, 2),
    _CfprApMacpoolBlockDn_Type()
)
cfprApMacpoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolBlockDn.setStatus("current")
_CfprApMacpoolBlockRn_Type = SnmpAdminString
_CfprApMacpoolBlockRn_Object = MibTableColumn
cfprApMacpoolBlockRn = _CfprApMacpoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 2, 1, 3),
    _CfprApMacpoolBlockRn_Type()
)
cfprApMacpoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolBlockRn.setStatus("current")
_CfprApMacpoolBlockFrom_Type = MacAddress
_CfprApMacpoolBlockFrom_Object = MibTableColumn
cfprApMacpoolBlockFrom = _CfprApMacpoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 2, 1, 4),
    _CfprApMacpoolBlockFrom_Type()
)
cfprApMacpoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolBlockFrom.setStatus("current")
_CfprApMacpoolBlockTo_Type = MacAddress
_CfprApMacpoolBlockTo_Object = MibTableColumn
cfprApMacpoolBlockTo = _CfprApMacpoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 2, 1, 5),
    _CfprApMacpoolBlockTo_Type()
)
cfprApMacpoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolBlockTo.setStatus("current")
_CfprApMacpoolFormatTable_Object = MibTable
cfprApMacpoolFormatTable = _CfprApMacpoolFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 3)
)
if mibBuilder.loadTexts:
    cfprApMacpoolFormatTable.setStatus("current")
_CfprApMacpoolFormatEntry_Object = MibTableRow
cfprApMacpoolFormatEntry = _CfprApMacpoolFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 3, 1)
)
cfprApMacpoolFormatEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MACPOOL-MIB", "cfprApMacpoolFormatInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMacpoolFormatEntry.setStatus("current")
_CfprApMacpoolFormatInstanceId_Type = CfprApManagedObjectId
_CfprApMacpoolFormatInstanceId_Object = MibTableColumn
cfprApMacpoolFormatInstanceId = _CfprApMacpoolFormatInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 3, 1, 1),
    _CfprApMacpoolFormatInstanceId_Type()
)
cfprApMacpoolFormatInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMacpoolFormatInstanceId.setStatus("current")
_CfprApMacpoolFormatDn_Type = CfprApManagedObjectDn
_CfprApMacpoolFormatDn_Object = MibTableColumn
cfprApMacpoolFormatDn = _CfprApMacpoolFormatDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 3, 1, 2),
    _CfprApMacpoolFormatDn_Type()
)
cfprApMacpoolFormatDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolFormatDn.setStatus("current")
_CfprApMacpoolFormatRn_Type = SnmpAdminString
_CfprApMacpoolFormatRn_Object = MibTableColumn
cfprApMacpoolFormatRn = _CfprApMacpoolFormatRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 3, 1, 3),
    _CfprApMacpoolFormatRn_Type()
)
cfprApMacpoolFormatRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolFormatRn.setStatus("current")
_CfprApMacpoolFormatFormat_Type = MacAddress
_CfprApMacpoolFormatFormat_Object = MibTableColumn
cfprApMacpoolFormatFormat = _CfprApMacpoolFormatFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 3, 1, 4),
    _CfprApMacpoolFormatFormat_Type()
)
cfprApMacpoolFormatFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolFormatFormat.setStatus("current")
_CfprApMacpoolFormatMask_Type = CfprApAddressMACMask
_CfprApMacpoolFormatMask_Object = MibTableColumn
cfprApMacpoolFormatMask = _CfprApMacpoolFormatMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 3, 1, 5),
    _CfprApMacpoolFormatMask_Type()
)
cfprApMacpoolFormatMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolFormatMask.setStatus("current")
_CfprApMacpoolPoolTable_Object = MibTable
cfprApMacpoolPoolTable = _CfprApMacpoolPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4)
)
if mibBuilder.loadTexts:
    cfprApMacpoolPoolTable.setStatus("current")
_CfprApMacpoolPoolEntry_Object = MibTableRow
cfprApMacpoolPoolEntry = _CfprApMacpoolPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4, 1)
)
cfprApMacpoolPoolEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MACPOOL-MIB", "cfprApMacpoolPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMacpoolPoolEntry.setStatus("current")
_CfprApMacpoolPoolInstanceId_Type = CfprApManagedObjectId
_CfprApMacpoolPoolInstanceId_Object = MibTableColumn
cfprApMacpoolPoolInstanceId = _CfprApMacpoolPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4, 1, 1),
    _CfprApMacpoolPoolInstanceId_Type()
)
cfprApMacpoolPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolInstanceId.setStatus("current")
_CfprApMacpoolPoolDn_Type = CfprApManagedObjectDn
_CfprApMacpoolPoolDn_Object = MibTableColumn
cfprApMacpoolPoolDn = _CfprApMacpoolPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4, 1, 2),
    _CfprApMacpoolPoolDn_Type()
)
cfprApMacpoolPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolDn.setStatus("current")
_CfprApMacpoolPoolRn_Type = SnmpAdminString
_CfprApMacpoolPoolRn_Object = MibTableColumn
cfprApMacpoolPoolRn = _CfprApMacpoolPoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4, 1, 3),
    _CfprApMacpoolPoolRn_Type()
)
cfprApMacpoolPoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolRn.setStatus("current")
_CfprApMacpoolPoolAssigned_Type = Gauge32
_CfprApMacpoolPoolAssigned_Object = MibTableColumn
cfprApMacpoolPoolAssigned = _CfprApMacpoolPoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4, 1, 4),
    _CfprApMacpoolPoolAssigned_Type()
)
cfprApMacpoolPoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolAssigned.setStatus("current")
_CfprApMacpoolPoolAssignmentOrder_Type = CfprApMacpoolPoolAssignmentOrder
_CfprApMacpoolPoolAssignmentOrder_Object = MibTableColumn
cfprApMacpoolPoolAssignmentOrder = _CfprApMacpoolPoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4, 1, 5),
    _CfprApMacpoolPoolAssignmentOrder_Type()
)
cfprApMacpoolPoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolAssignmentOrder.setStatus("current")
_CfprApMacpoolPoolDescr_Type = SnmpAdminString
_CfprApMacpoolPoolDescr_Object = MibTableColumn
cfprApMacpoolPoolDescr = _CfprApMacpoolPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4, 1, 6),
    _CfprApMacpoolPoolDescr_Type()
)
cfprApMacpoolPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolDescr.setStatus("current")
_CfprApMacpoolPoolIntId_Type = SnmpAdminString
_CfprApMacpoolPoolIntId_Object = MibTableColumn
cfprApMacpoolPoolIntId = _CfprApMacpoolPoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4, 1, 7),
    _CfprApMacpoolPoolIntId_Type()
)
cfprApMacpoolPoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolIntId.setStatus("current")
_CfprApMacpoolPoolName_Type = SnmpAdminString
_CfprApMacpoolPoolName_Object = MibTableColumn
cfprApMacpoolPoolName = _CfprApMacpoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4, 1, 8),
    _CfprApMacpoolPoolName_Type()
)
cfprApMacpoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolName.setStatus("current")
_CfprApMacpoolPoolPolicyLevel_Type = Gauge32
_CfprApMacpoolPoolPolicyLevel_Object = MibTableColumn
cfprApMacpoolPoolPolicyLevel = _CfprApMacpoolPoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4, 1, 9),
    _CfprApMacpoolPoolPolicyLevel_Type()
)
cfprApMacpoolPoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolPolicyLevel.setStatus("current")
_CfprApMacpoolPoolPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApMacpoolPoolPolicyOwner_Object = MibTableColumn
cfprApMacpoolPoolPolicyOwner = _CfprApMacpoolPoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4, 1, 10),
    _CfprApMacpoolPoolPolicyOwner_Type()
)
cfprApMacpoolPoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolPolicyOwner.setStatus("current")
_CfprApMacpoolPoolSize_Type = Gauge32
_CfprApMacpoolPoolSize_Object = MibTableColumn
cfprApMacpoolPoolSize = _CfprApMacpoolPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 4, 1, 11),
    _CfprApMacpoolPoolSize_Type()
)
cfprApMacpoolPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolSize.setStatus("current")
_CfprApMacpoolPoolableTable_Object = MibTable
cfprApMacpoolPoolableTable = _CfprApMacpoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 5)
)
if mibBuilder.loadTexts:
    cfprApMacpoolPoolableTable.setStatus("current")
_CfprApMacpoolPoolableEntry_Object = MibTableRow
cfprApMacpoolPoolableEntry = _CfprApMacpoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 5, 1)
)
cfprApMacpoolPoolableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MACPOOL-MIB", "cfprApMacpoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMacpoolPoolableEntry.setStatus("current")
_CfprApMacpoolPoolableInstanceId_Type = CfprApManagedObjectId
_CfprApMacpoolPoolableInstanceId_Object = MibTableColumn
cfprApMacpoolPoolableInstanceId = _CfprApMacpoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 5, 1, 1),
    _CfprApMacpoolPoolableInstanceId_Type()
)
cfprApMacpoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolableInstanceId.setStatus("current")
_CfprApMacpoolPoolableDn_Type = CfprApManagedObjectDn
_CfprApMacpoolPoolableDn_Object = MibTableColumn
cfprApMacpoolPoolableDn = _CfprApMacpoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 5, 1, 2),
    _CfprApMacpoolPoolableDn_Type()
)
cfprApMacpoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolableDn.setStatus("current")
_CfprApMacpoolPoolableRn_Type = SnmpAdminString
_CfprApMacpoolPoolableRn_Object = MibTableColumn
cfprApMacpoolPoolableRn = _CfprApMacpoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 5, 1, 3),
    _CfprApMacpoolPoolableRn_Type()
)
cfprApMacpoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolableRn.setStatus("current")
_CfprApMacpoolPoolableId_Type = Unsigned64
_CfprApMacpoolPoolableId_Object = MibTableColumn
cfprApMacpoolPoolableId = _CfprApMacpoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 5, 1, 4),
    _CfprApMacpoolPoolableId_Type()
)
cfprApMacpoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolableId.setStatus("current")
_CfprApMacpoolPoolablePoolDn_Type = SnmpAdminString
_CfprApMacpoolPoolablePoolDn_Object = MibTableColumn
cfprApMacpoolPoolablePoolDn = _CfprApMacpoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 5, 1, 5),
    _CfprApMacpoolPoolablePoolDn_Type()
)
cfprApMacpoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPoolablePoolDn.setStatus("current")
_CfprApMacpoolPooledTable_Object = MibTable
cfprApMacpoolPooledTable = _CfprApMacpoolPooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 6)
)
if mibBuilder.loadTexts:
    cfprApMacpoolPooledTable.setStatus("current")
_CfprApMacpoolPooledEntry_Object = MibTableRow
cfprApMacpoolPooledEntry = _CfprApMacpoolPooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 6, 1)
)
cfprApMacpoolPooledEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MACPOOL-MIB", "cfprApMacpoolPooledInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMacpoolPooledEntry.setStatus("current")
_CfprApMacpoolPooledInstanceId_Type = CfprApManagedObjectId
_CfprApMacpoolPooledInstanceId_Object = MibTableColumn
cfprApMacpoolPooledInstanceId = _CfprApMacpoolPooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 6, 1, 1),
    _CfprApMacpoolPooledInstanceId_Type()
)
cfprApMacpoolPooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMacpoolPooledInstanceId.setStatus("current")
_CfprApMacpoolPooledDn_Type = CfprApManagedObjectDn
_CfprApMacpoolPooledDn_Object = MibTableColumn
cfprApMacpoolPooledDn = _CfprApMacpoolPooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 6, 1, 2),
    _CfprApMacpoolPooledDn_Type()
)
cfprApMacpoolPooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPooledDn.setStatus("current")
_CfprApMacpoolPooledRn_Type = SnmpAdminString
_CfprApMacpoolPooledRn_Object = MibTableColumn
cfprApMacpoolPooledRn = _CfprApMacpoolPooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 6, 1, 3),
    _CfprApMacpoolPooledRn_Type()
)
cfprApMacpoolPooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPooledRn.setStatus("current")
_CfprApMacpoolPooledAssigned_Type = TruthValue
_CfprApMacpoolPooledAssigned_Object = MibTableColumn
cfprApMacpoolPooledAssigned = _CfprApMacpoolPooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 6, 1, 4),
    _CfprApMacpoolPooledAssigned_Type()
)
cfprApMacpoolPooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPooledAssigned.setStatus("current")
_CfprApMacpoolPooledAssignedToDn_Type = SnmpAdminString
_CfprApMacpoolPooledAssignedToDn_Object = MibTableColumn
cfprApMacpoolPooledAssignedToDn = _CfprApMacpoolPooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 6, 1, 5),
    _CfprApMacpoolPooledAssignedToDn_Type()
)
cfprApMacpoolPooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPooledAssignedToDn.setStatus("current")
_CfprApMacpoolPooledId_Type = MacAddress
_CfprApMacpoolPooledId_Object = MibTableColumn
cfprApMacpoolPooledId = _CfprApMacpoolPooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 6, 1, 6),
    _CfprApMacpoolPooledId_Type()
)
cfprApMacpoolPooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPooledId.setStatus("current")
_CfprApMacpoolPooledPoolableDn_Type = SnmpAdminString
_CfprApMacpoolPooledPoolableDn_Object = MibTableColumn
cfprApMacpoolPooledPoolableDn = _CfprApMacpoolPooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 6, 1, 7),
    _CfprApMacpoolPooledPoolableDn_Type()
)
cfprApMacpoolPooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPooledPoolableDn.setStatus("current")
_CfprApMacpoolPooledPrevAssignedToDn_Type = SnmpAdminString
_CfprApMacpoolPooledPrevAssignedToDn_Object = MibTableColumn
cfprApMacpoolPooledPrevAssignedToDn = _CfprApMacpoolPooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 6, 1, 8),
    _CfprApMacpoolPooledPrevAssignedToDn_Type()
)
cfprApMacpoolPooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolPooledPrevAssignedToDn.setStatus("current")
_CfprApMacpoolUniverseTable_Object = MibTable
cfprApMacpoolUniverseTable = _CfprApMacpoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 7)
)
if mibBuilder.loadTexts:
    cfprApMacpoolUniverseTable.setStatus("current")
_CfprApMacpoolUniverseEntry_Object = MibTableRow
cfprApMacpoolUniverseEntry = _CfprApMacpoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 7, 1)
)
cfprApMacpoolUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-MACPOOL-MIB", "cfprApMacpoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApMacpoolUniverseEntry.setStatus("current")
_CfprApMacpoolUniverseInstanceId_Type = CfprApManagedObjectId
_CfprApMacpoolUniverseInstanceId_Object = MibTableColumn
cfprApMacpoolUniverseInstanceId = _CfprApMacpoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 7, 1, 1),
    _CfprApMacpoolUniverseInstanceId_Type()
)
cfprApMacpoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApMacpoolUniverseInstanceId.setStatus("current")
_CfprApMacpoolUniverseDn_Type = CfprApManagedObjectDn
_CfprApMacpoolUniverseDn_Object = MibTableColumn
cfprApMacpoolUniverseDn = _CfprApMacpoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 7, 1, 2),
    _CfprApMacpoolUniverseDn_Type()
)
cfprApMacpoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolUniverseDn.setStatus("current")
_CfprApMacpoolUniverseRn_Type = SnmpAdminString
_CfprApMacpoolUniverseRn_Object = MibTableColumn
cfprApMacpoolUniverseRn = _CfprApMacpoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 49, 7, 1, 3),
    _CfprApMacpoolUniverseRn_Type()
)
cfprApMacpoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApMacpoolUniverseRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-MACPOOL-MIB",
    **{"cfprApMacpoolObjects": cfprApMacpoolObjects,
       "cfprApMacpoolAddrTable": cfprApMacpoolAddrTable,
       "cfprApMacpoolAddrEntry": cfprApMacpoolAddrEntry,
       "cfprApMacpoolAddrInstanceId": cfprApMacpoolAddrInstanceId,
       "cfprApMacpoolAddrDn": cfprApMacpoolAddrDn,
       "cfprApMacpoolAddrRn": cfprApMacpoolAddrRn,
       "cfprApMacpoolAddrAssigned": cfprApMacpoolAddrAssigned,
       "cfprApMacpoolAddrAssignedToDn": cfprApMacpoolAddrAssignedToDn,
       "cfprApMacpoolAddrGlobalAssignedCnt": cfprApMacpoolAddrGlobalAssignedCnt,
       "cfprApMacpoolAddrGlobalDefinedCnt": cfprApMacpoolAddrGlobalDefinedCnt,
       "cfprApMacpoolAddrId": cfprApMacpoolAddrId,
       "cfprApMacpoolAddrOwner": cfprApMacpoolAddrOwner,
       "cfprApMacpoolBlockTable": cfprApMacpoolBlockTable,
       "cfprApMacpoolBlockEntry": cfprApMacpoolBlockEntry,
       "cfprApMacpoolBlockInstanceId": cfprApMacpoolBlockInstanceId,
       "cfprApMacpoolBlockDn": cfprApMacpoolBlockDn,
       "cfprApMacpoolBlockRn": cfprApMacpoolBlockRn,
       "cfprApMacpoolBlockFrom": cfprApMacpoolBlockFrom,
       "cfprApMacpoolBlockTo": cfprApMacpoolBlockTo,
       "cfprApMacpoolFormatTable": cfprApMacpoolFormatTable,
       "cfprApMacpoolFormatEntry": cfprApMacpoolFormatEntry,
       "cfprApMacpoolFormatInstanceId": cfprApMacpoolFormatInstanceId,
       "cfprApMacpoolFormatDn": cfprApMacpoolFormatDn,
       "cfprApMacpoolFormatRn": cfprApMacpoolFormatRn,
       "cfprApMacpoolFormatFormat": cfprApMacpoolFormatFormat,
       "cfprApMacpoolFormatMask": cfprApMacpoolFormatMask,
       "cfprApMacpoolPoolTable": cfprApMacpoolPoolTable,
       "cfprApMacpoolPoolEntry": cfprApMacpoolPoolEntry,
       "cfprApMacpoolPoolInstanceId": cfprApMacpoolPoolInstanceId,
       "cfprApMacpoolPoolDn": cfprApMacpoolPoolDn,
       "cfprApMacpoolPoolRn": cfprApMacpoolPoolRn,
       "cfprApMacpoolPoolAssigned": cfprApMacpoolPoolAssigned,
       "cfprApMacpoolPoolAssignmentOrder": cfprApMacpoolPoolAssignmentOrder,
       "cfprApMacpoolPoolDescr": cfprApMacpoolPoolDescr,
       "cfprApMacpoolPoolIntId": cfprApMacpoolPoolIntId,
       "cfprApMacpoolPoolName": cfprApMacpoolPoolName,
       "cfprApMacpoolPoolPolicyLevel": cfprApMacpoolPoolPolicyLevel,
       "cfprApMacpoolPoolPolicyOwner": cfprApMacpoolPoolPolicyOwner,
       "cfprApMacpoolPoolSize": cfprApMacpoolPoolSize,
       "cfprApMacpoolPoolableTable": cfprApMacpoolPoolableTable,
       "cfprApMacpoolPoolableEntry": cfprApMacpoolPoolableEntry,
       "cfprApMacpoolPoolableInstanceId": cfprApMacpoolPoolableInstanceId,
       "cfprApMacpoolPoolableDn": cfprApMacpoolPoolableDn,
       "cfprApMacpoolPoolableRn": cfprApMacpoolPoolableRn,
       "cfprApMacpoolPoolableId": cfprApMacpoolPoolableId,
       "cfprApMacpoolPoolablePoolDn": cfprApMacpoolPoolablePoolDn,
       "cfprApMacpoolPooledTable": cfprApMacpoolPooledTable,
       "cfprApMacpoolPooledEntry": cfprApMacpoolPooledEntry,
       "cfprApMacpoolPooledInstanceId": cfprApMacpoolPooledInstanceId,
       "cfprApMacpoolPooledDn": cfprApMacpoolPooledDn,
       "cfprApMacpoolPooledRn": cfprApMacpoolPooledRn,
       "cfprApMacpoolPooledAssigned": cfprApMacpoolPooledAssigned,
       "cfprApMacpoolPooledAssignedToDn": cfprApMacpoolPooledAssignedToDn,
       "cfprApMacpoolPooledId": cfprApMacpoolPooledId,
       "cfprApMacpoolPooledPoolableDn": cfprApMacpoolPooledPoolableDn,
       "cfprApMacpoolPooledPrevAssignedToDn": cfprApMacpoolPooledPrevAssignedToDn,
       "cfprApMacpoolUniverseTable": cfprApMacpoolUniverseTable,
       "cfprApMacpoolUniverseEntry": cfprApMacpoolUniverseEntry,
       "cfprApMacpoolUniverseInstanceId": cfprApMacpoolUniverseInstanceId,
       "cfprApMacpoolUniverseDn": cfprApMacpoolUniverseDn,
       "cfprApMacpoolUniverseRn": cfprApMacpoolUniverseRn}
)
