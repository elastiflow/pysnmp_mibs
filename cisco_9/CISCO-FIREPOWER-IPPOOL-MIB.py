# SNMP MIB module (CISCO-FIREPOWER-IPPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-IPPOOL-MIB.mib
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

(CfprIppoolDHCPMode,
 CfprIppoolManagementMode,
 CfprIppoolNetBIOSMode,
 CfprIppoolPoolAssignmentOrder,
 CfprPolicyPolicyOwner,
 CfprPoolElementOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprIppoolDHCPMode",
    "CfprIppoolManagementMode",
    "CfprIppoolNetBIOSMode",
    "CfprIppoolPoolAssignmentOrder",
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

cfprIppoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprIppoolAddrTable_Object = MibTable
cfprIppoolAddrTable = _CfprIppoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 1)
)
if mibBuilder.loadTexts:
    cfprIppoolAddrTable.setStatus("current")
_CfprIppoolAddrEntry_Object = MibTableRow
cfprIppoolAddrEntry = _CfprIppoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 1, 1)
)
cfprIppoolAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPPOOL-MIB", "cfprIppoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIppoolAddrEntry.setStatus("current")
_CfprIppoolAddrInstanceId_Type = CfprManagedObjectId
_CfprIppoolAddrInstanceId_Object = MibTableColumn
cfprIppoolAddrInstanceId = _CfprIppoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 1, 1, 1),
    _CfprIppoolAddrInstanceId_Type()
)
cfprIppoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIppoolAddrInstanceId.setStatus("current")
_CfprIppoolAddrDn_Type = CfprManagedObjectDn
_CfprIppoolAddrDn_Object = MibTableColumn
cfprIppoolAddrDn = _CfprIppoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 1, 1, 2),
    _CfprIppoolAddrDn_Type()
)
cfprIppoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolAddrDn.setStatus("current")
_CfprIppoolAddrRn_Type = SnmpAdminString
_CfprIppoolAddrRn_Object = MibTableColumn
cfprIppoolAddrRn = _CfprIppoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 1, 1, 3),
    _CfprIppoolAddrRn_Type()
)
cfprIppoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolAddrRn.setStatus("current")
_CfprIppoolAddrAssigned_Type = TruthValue
_CfprIppoolAddrAssigned_Object = MibTableColumn
cfprIppoolAddrAssigned = _CfprIppoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 1, 1, 4),
    _CfprIppoolAddrAssigned_Type()
)
cfprIppoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolAddrAssigned.setStatus("current")
_CfprIppoolAddrAssignedToDn_Type = SnmpAdminString
_CfprIppoolAddrAssignedToDn_Object = MibTableColumn
cfprIppoolAddrAssignedToDn = _CfprIppoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 1, 1, 5),
    _CfprIppoolAddrAssignedToDn_Type()
)
cfprIppoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolAddrAssignedToDn.setStatus("current")
_CfprIppoolAddrGlobalAssignedCnt_Type = Gauge32
_CfprIppoolAddrGlobalAssignedCnt_Object = MibTableColumn
cfprIppoolAddrGlobalAssignedCnt = _CfprIppoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 1, 1, 6),
    _CfprIppoolAddrGlobalAssignedCnt_Type()
)
cfprIppoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolAddrGlobalAssignedCnt.setStatus("current")
_CfprIppoolAddrGlobalDefinedCnt_Type = Gauge32
_CfprIppoolAddrGlobalDefinedCnt_Object = MibTableColumn
cfprIppoolAddrGlobalDefinedCnt = _CfprIppoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 1, 1, 7),
    _CfprIppoolAddrGlobalDefinedCnt_Type()
)
cfprIppoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolAddrGlobalDefinedCnt.setStatus("current")
_CfprIppoolAddrId_Type = InetAddressIPv4
_CfprIppoolAddrId_Object = MibTableColumn
cfprIppoolAddrId = _CfprIppoolAddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 1, 1, 8),
    _CfprIppoolAddrId_Type()
)
cfprIppoolAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolAddrId.setStatus("current")
_CfprIppoolAddrOwner_Type = CfprPoolElementOwner
_CfprIppoolAddrOwner_Object = MibTableColumn
cfprIppoolAddrOwner = _CfprIppoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 1, 1, 9),
    _CfprIppoolAddrOwner_Type()
)
cfprIppoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolAddrOwner.setStatus("current")
_CfprIppoolBlockTable_Object = MibTable
cfprIppoolBlockTable = _CfprIppoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 2)
)
if mibBuilder.loadTexts:
    cfprIppoolBlockTable.setStatus("current")
_CfprIppoolBlockEntry_Object = MibTableRow
cfprIppoolBlockEntry = _CfprIppoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 2, 1)
)
cfprIppoolBlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPPOOL-MIB", "cfprIppoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIppoolBlockEntry.setStatus("current")
_CfprIppoolBlockInstanceId_Type = CfprManagedObjectId
_CfprIppoolBlockInstanceId_Object = MibTableColumn
cfprIppoolBlockInstanceId = _CfprIppoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 2, 1, 1),
    _CfprIppoolBlockInstanceId_Type()
)
cfprIppoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIppoolBlockInstanceId.setStatus("current")
_CfprIppoolBlockDn_Type = CfprManagedObjectDn
_CfprIppoolBlockDn_Object = MibTableColumn
cfprIppoolBlockDn = _CfprIppoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 2, 1, 2),
    _CfprIppoolBlockDn_Type()
)
cfprIppoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolBlockDn.setStatus("current")
_CfprIppoolBlockRn_Type = SnmpAdminString
_CfprIppoolBlockRn_Object = MibTableColumn
cfprIppoolBlockRn = _CfprIppoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 2, 1, 3),
    _CfprIppoolBlockRn_Type()
)
cfprIppoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolBlockRn.setStatus("current")
_CfprIppoolBlockDefGw_Type = InetAddressIPv4
_CfprIppoolBlockDefGw_Object = MibTableColumn
cfprIppoolBlockDefGw = _CfprIppoolBlockDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 2, 1, 4),
    _CfprIppoolBlockDefGw_Type()
)
cfprIppoolBlockDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolBlockDefGw.setStatus("current")
_CfprIppoolBlockFrom_Type = InetAddressIPv4
_CfprIppoolBlockFrom_Object = MibTableColumn
cfprIppoolBlockFrom = _CfprIppoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 2, 1, 5),
    _CfprIppoolBlockFrom_Type()
)
cfprIppoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolBlockFrom.setStatus("current")
_CfprIppoolBlockPrimDns_Type = InetAddressIPv4
_CfprIppoolBlockPrimDns_Object = MibTableColumn
cfprIppoolBlockPrimDns = _CfprIppoolBlockPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 2, 1, 6),
    _CfprIppoolBlockPrimDns_Type()
)
cfprIppoolBlockPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolBlockPrimDns.setStatus("current")
_CfprIppoolBlockSecDns_Type = InetAddressIPv4
_CfprIppoolBlockSecDns_Object = MibTableColumn
cfprIppoolBlockSecDns = _CfprIppoolBlockSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 2, 1, 7),
    _CfprIppoolBlockSecDns_Type()
)
cfprIppoolBlockSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolBlockSecDns.setStatus("current")
_CfprIppoolBlockSubnet_Type = InetAddressIPv4
_CfprIppoolBlockSubnet_Object = MibTableColumn
cfprIppoolBlockSubnet = _CfprIppoolBlockSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 2, 1, 8),
    _CfprIppoolBlockSubnet_Type()
)
cfprIppoolBlockSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolBlockSubnet.setStatus("current")
_CfprIppoolBlockTo_Type = InetAddressIPv4
_CfprIppoolBlockTo_Object = MibTableColumn
cfprIppoolBlockTo = _CfprIppoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 2, 1, 9),
    _CfprIppoolBlockTo_Type()
)
cfprIppoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolBlockTo.setStatus("current")
_CfprIppoolIpV6AddrTable_Object = MibTable
cfprIppoolIpV6AddrTable = _CfprIppoolIpV6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 3)
)
if mibBuilder.loadTexts:
    cfprIppoolIpV6AddrTable.setStatus("current")
_CfprIppoolIpV6AddrEntry_Object = MibTableRow
cfprIppoolIpV6AddrEntry = _CfprIppoolIpV6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 3, 1)
)
cfprIppoolIpV6AddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPPOOL-MIB", "cfprIppoolIpV6AddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIppoolIpV6AddrEntry.setStatus("current")
_CfprIppoolIpV6AddrInstanceId_Type = CfprManagedObjectId
_CfprIppoolIpV6AddrInstanceId_Object = MibTableColumn
cfprIppoolIpV6AddrInstanceId = _CfprIppoolIpV6AddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 3, 1, 1),
    _CfprIppoolIpV6AddrInstanceId_Type()
)
cfprIppoolIpV6AddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIppoolIpV6AddrInstanceId.setStatus("current")
_CfprIppoolIpV6AddrDn_Type = CfprManagedObjectDn
_CfprIppoolIpV6AddrDn_Object = MibTableColumn
cfprIppoolIpV6AddrDn = _CfprIppoolIpV6AddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 3, 1, 2),
    _CfprIppoolIpV6AddrDn_Type()
)
cfprIppoolIpV6AddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6AddrDn.setStatus("current")
_CfprIppoolIpV6AddrRn_Type = SnmpAdminString
_CfprIppoolIpV6AddrRn_Object = MibTableColumn
cfprIppoolIpV6AddrRn = _CfprIppoolIpV6AddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 3, 1, 3),
    _CfprIppoolIpV6AddrRn_Type()
)
cfprIppoolIpV6AddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6AddrRn.setStatus("current")
_CfprIppoolIpV6AddrAssigned_Type = TruthValue
_CfprIppoolIpV6AddrAssigned_Object = MibTableColumn
cfprIppoolIpV6AddrAssigned = _CfprIppoolIpV6AddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 3, 1, 4),
    _CfprIppoolIpV6AddrAssigned_Type()
)
cfprIppoolIpV6AddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6AddrAssigned.setStatus("current")
_CfprIppoolIpV6AddrAssignedToDn_Type = SnmpAdminString
_CfprIppoolIpV6AddrAssignedToDn_Object = MibTableColumn
cfprIppoolIpV6AddrAssignedToDn = _CfprIppoolIpV6AddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 3, 1, 5),
    _CfprIppoolIpV6AddrAssignedToDn_Type()
)
cfprIppoolIpV6AddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6AddrAssignedToDn.setStatus("current")
_CfprIppoolIpV6AddrGlobalAssignedCnt_Type = Gauge32
_CfprIppoolIpV6AddrGlobalAssignedCnt_Object = MibTableColumn
cfprIppoolIpV6AddrGlobalAssignedCnt = _CfprIppoolIpV6AddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 3, 1, 6),
    _CfprIppoolIpV6AddrGlobalAssignedCnt_Type()
)
cfprIppoolIpV6AddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6AddrGlobalAssignedCnt.setStatus("current")
_CfprIppoolIpV6AddrGlobalDefinedCnt_Type = Gauge32
_CfprIppoolIpV6AddrGlobalDefinedCnt_Object = MibTableColumn
cfprIppoolIpV6AddrGlobalDefinedCnt = _CfprIppoolIpV6AddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 3, 1, 7),
    _CfprIppoolIpV6AddrGlobalDefinedCnt_Type()
)
cfprIppoolIpV6AddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6AddrGlobalDefinedCnt.setStatus("current")
_CfprIppoolIpV6AddrId_Type = InetAddressIPv6
_CfprIppoolIpV6AddrId_Object = MibTableColumn
cfprIppoolIpV6AddrId = _CfprIppoolIpV6AddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 3, 1, 8),
    _CfprIppoolIpV6AddrId_Type()
)
cfprIppoolIpV6AddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6AddrId.setStatus("current")
_CfprIppoolIpV6AddrOwner_Type = CfprPoolElementOwner
_CfprIppoolIpV6AddrOwner_Object = MibTableColumn
cfprIppoolIpV6AddrOwner = _CfprIppoolIpV6AddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 3, 1, 9),
    _CfprIppoolIpV6AddrOwner_Type()
)
cfprIppoolIpV6AddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6AddrOwner.setStatus("current")
_CfprIppoolIpV6BlockTable_Object = MibTable
cfprIppoolIpV6BlockTable = _CfprIppoolIpV6BlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 4)
)
if mibBuilder.loadTexts:
    cfprIppoolIpV6BlockTable.setStatus("current")
_CfprIppoolIpV6BlockEntry_Object = MibTableRow
cfprIppoolIpV6BlockEntry = _CfprIppoolIpV6BlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 4, 1)
)
cfprIppoolIpV6BlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPPOOL-MIB", "cfprIppoolIpV6BlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIppoolIpV6BlockEntry.setStatus("current")
_CfprIppoolIpV6BlockInstanceId_Type = CfprManagedObjectId
_CfprIppoolIpV6BlockInstanceId_Object = MibTableColumn
cfprIppoolIpV6BlockInstanceId = _CfprIppoolIpV6BlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 4, 1, 1),
    _CfprIppoolIpV6BlockInstanceId_Type()
)
cfprIppoolIpV6BlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIppoolIpV6BlockInstanceId.setStatus("current")
_CfprIppoolIpV6BlockDn_Type = CfprManagedObjectDn
_CfprIppoolIpV6BlockDn_Object = MibTableColumn
cfprIppoolIpV6BlockDn = _CfprIppoolIpV6BlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 4, 1, 2),
    _CfprIppoolIpV6BlockDn_Type()
)
cfprIppoolIpV6BlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6BlockDn.setStatus("current")
_CfprIppoolIpV6BlockRn_Type = SnmpAdminString
_CfprIppoolIpV6BlockRn_Object = MibTableColumn
cfprIppoolIpV6BlockRn = _CfprIppoolIpV6BlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 4, 1, 3),
    _CfprIppoolIpV6BlockRn_Type()
)
cfprIppoolIpV6BlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6BlockRn.setStatus("current")
_CfprIppoolIpV6BlockDefGw_Type = InetAddressIPv6
_CfprIppoolIpV6BlockDefGw_Object = MibTableColumn
cfprIppoolIpV6BlockDefGw = _CfprIppoolIpV6BlockDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 4, 1, 4),
    _CfprIppoolIpV6BlockDefGw_Type()
)
cfprIppoolIpV6BlockDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6BlockDefGw.setStatus("current")
_CfprIppoolIpV6BlockFrom_Type = InetAddressIPv6
_CfprIppoolIpV6BlockFrom_Object = MibTableColumn
cfprIppoolIpV6BlockFrom = _CfprIppoolIpV6BlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 4, 1, 5),
    _CfprIppoolIpV6BlockFrom_Type()
)
cfprIppoolIpV6BlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6BlockFrom.setStatus("current")
_CfprIppoolIpV6BlockPrefix_Type = Gauge32
_CfprIppoolIpV6BlockPrefix_Object = MibTableColumn
cfprIppoolIpV6BlockPrefix = _CfprIppoolIpV6BlockPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 4, 1, 6),
    _CfprIppoolIpV6BlockPrefix_Type()
)
cfprIppoolIpV6BlockPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6BlockPrefix.setStatus("current")
_CfprIppoolIpV6BlockPrimDns_Type = InetAddressIPv6
_CfprIppoolIpV6BlockPrimDns_Object = MibTableColumn
cfprIppoolIpV6BlockPrimDns = _CfprIppoolIpV6BlockPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 4, 1, 7),
    _CfprIppoolIpV6BlockPrimDns_Type()
)
cfprIppoolIpV6BlockPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6BlockPrimDns.setStatus("current")
_CfprIppoolIpV6BlockSecDns_Type = InetAddressIPv6
_CfprIppoolIpV6BlockSecDns_Object = MibTableColumn
cfprIppoolIpV6BlockSecDns = _CfprIppoolIpV6BlockSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 4, 1, 8),
    _CfprIppoolIpV6BlockSecDns_Type()
)
cfprIppoolIpV6BlockSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6BlockSecDns.setStatus("current")
_CfprIppoolIpV6BlockTo_Type = InetAddressIPv6
_CfprIppoolIpV6BlockTo_Object = MibTableColumn
cfprIppoolIpV6BlockTo = _CfprIppoolIpV6BlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 4, 1, 9),
    _CfprIppoolIpV6BlockTo_Type()
)
cfprIppoolIpV6BlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6BlockTo.setStatus("current")
_CfprIppoolIpV6PooledTable_Object = MibTable
cfprIppoolIpV6PooledTable = _CfprIppoolIpV6PooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5)
)
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledTable.setStatus("current")
_CfprIppoolIpV6PooledEntry_Object = MibTableRow
cfprIppoolIpV6PooledEntry = _CfprIppoolIpV6PooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1)
)
cfprIppoolIpV6PooledEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPPOOL-MIB", "cfprIppoolIpV6PooledInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledEntry.setStatus("current")
_CfprIppoolIpV6PooledInstanceId_Type = CfprManagedObjectId
_CfprIppoolIpV6PooledInstanceId_Object = MibTableColumn
cfprIppoolIpV6PooledInstanceId = _CfprIppoolIpV6PooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1, 1),
    _CfprIppoolIpV6PooledInstanceId_Type()
)
cfprIppoolIpV6PooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledInstanceId.setStatus("current")
_CfprIppoolIpV6PooledDn_Type = CfprManagedObjectDn
_CfprIppoolIpV6PooledDn_Object = MibTableColumn
cfprIppoolIpV6PooledDn = _CfprIppoolIpV6PooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1, 2),
    _CfprIppoolIpV6PooledDn_Type()
)
cfprIppoolIpV6PooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledDn.setStatus("current")
_CfprIppoolIpV6PooledRn_Type = SnmpAdminString
_CfprIppoolIpV6PooledRn_Object = MibTableColumn
cfprIppoolIpV6PooledRn = _CfprIppoolIpV6PooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1, 3),
    _CfprIppoolIpV6PooledRn_Type()
)
cfprIppoolIpV6PooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledRn.setStatus("current")
_CfprIppoolIpV6PooledAssigned_Type = TruthValue
_CfprIppoolIpV6PooledAssigned_Object = MibTableColumn
cfprIppoolIpV6PooledAssigned = _CfprIppoolIpV6PooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1, 4),
    _CfprIppoolIpV6PooledAssigned_Type()
)
cfprIppoolIpV6PooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledAssigned.setStatus("current")
_CfprIppoolIpV6PooledAssignedToDn_Type = SnmpAdminString
_CfprIppoolIpV6PooledAssignedToDn_Object = MibTableColumn
cfprIppoolIpV6PooledAssignedToDn = _CfprIppoolIpV6PooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1, 5),
    _CfprIppoolIpV6PooledAssignedToDn_Type()
)
cfprIppoolIpV6PooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledAssignedToDn.setStatus("current")
_CfprIppoolIpV6PooledDefGw_Type = InetAddressIPv6
_CfprIppoolIpV6PooledDefGw_Object = MibTableColumn
cfprIppoolIpV6PooledDefGw = _CfprIppoolIpV6PooledDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1, 6),
    _CfprIppoolIpV6PooledDefGw_Type()
)
cfprIppoolIpV6PooledDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledDefGw.setStatus("current")
_CfprIppoolIpV6PooledId_Type = InetAddressIPv6
_CfprIppoolIpV6PooledId_Object = MibTableColumn
cfprIppoolIpV6PooledId = _CfprIppoolIpV6PooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1, 7),
    _CfprIppoolIpV6PooledId_Type()
)
cfprIppoolIpV6PooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledId.setStatus("current")
_CfprIppoolIpV6PooledPoolableDn_Type = SnmpAdminString
_CfprIppoolIpV6PooledPoolableDn_Object = MibTableColumn
cfprIppoolIpV6PooledPoolableDn = _CfprIppoolIpV6PooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1, 8),
    _CfprIppoolIpV6PooledPoolableDn_Type()
)
cfprIppoolIpV6PooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledPoolableDn.setStatus("current")
_CfprIppoolIpV6PooledPrefix_Type = Gauge32
_CfprIppoolIpV6PooledPrefix_Object = MibTableColumn
cfprIppoolIpV6PooledPrefix = _CfprIppoolIpV6PooledPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1, 9),
    _CfprIppoolIpV6PooledPrefix_Type()
)
cfprIppoolIpV6PooledPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledPrefix.setStatus("current")
_CfprIppoolIpV6PooledPrevAssignedToDn_Type = SnmpAdminString
_CfprIppoolIpV6PooledPrevAssignedToDn_Object = MibTableColumn
cfprIppoolIpV6PooledPrevAssignedToDn = _CfprIppoolIpV6PooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1, 10),
    _CfprIppoolIpV6PooledPrevAssignedToDn_Type()
)
cfprIppoolIpV6PooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledPrevAssignedToDn.setStatus("current")
_CfprIppoolIpV6PooledPrimDns_Type = InetAddressIPv6
_CfprIppoolIpV6PooledPrimDns_Object = MibTableColumn
cfprIppoolIpV6PooledPrimDns = _CfprIppoolIpV6PooledPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1, 11),
    _CfprIppoolIpV6PooledPrimDns_Type()
)
cfprIppoolIpV6PooledPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledPrimDns.setStatus("current")
_CfprIppoolIpV6PooledSecDns_Type = InetAddressIPv6
_CfprIppoolIpV6PooledSecDns_Object = MibTableColumn
cfprIppoolIpV6PooledSecDns = _CfprIppoolIpV6PooledSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 5, 1, 12),
    _CfprIppoolIpV6PooledSecDns_Type()
)
cfprIppoolIpV6PooledSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolIpV6PooledSecDns.setStatus("current")
_CfprIppoolPoolTable_Object = MibTable
cfprIppoolPoolTable = _CfprIppoolPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6)
)
if mibBuilder.loadTexts:
    cfprIppoolPoolTable.setStatus("current")
_CfprIppoolPoolEntry_Object = MibTableRow
cfprIppoolPoolEntry = _CfprIppoolPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1)
)
cfprIppoolPoolEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPPOOL-MIB", "cfprIppoolPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIppoolPoolEntry.setStatus("current")
_CfprIppoolPoolInstanceId_Type = CfprManagedObjectId
_CfprIppoolPoolInstanceId_Object = MibTableColumn
cfprIppoolPoolInstanceId = _CfprIppoolPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 1),
    _CfprIppoolPoolInstanceId_Type()
)
cfprIppoolPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIppoolPoolInstanceId.setStatus("current")
_CfprIppoolPoolDn_Type = CfprManagedObjectDn
_CfprIppoolPoolDn_Object = MibTableColumn
cfprIppoolPoolDn = _CfprIppoolPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 2),
    _CfprIppoolPoolDn_Type()
)
cfprIppoolPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolDn.setStatus("current")
_CfprIppoolPoolRn_Type = SnmpAdminString
_CfprIppoolPoolRn_Object = MibTableColumn
cfprIppoolPoolRn = _CfprIppoolPoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 3),
    _CfprIppoolPoolRn_Type()
)
cfprIppoolPoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolRn.setStatus("current")
_CfprIppoolPoolAssigned_Type = Gauge32
_CfprIppoolPoolAssigned_Object = MibTableColumn
cfprIppoolPoolAssigned = _CfprIppoolPoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 4),
    _CfprIppoolPoolAssigned_Type()
)
cfprIppoolPoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolAssigned.setStatus("current")
_CfprIppoolPoolAssignmentOrder_Type = CfprIppoolPoolAssignmentOrder
_CfprIppoolPoolAssignmentOrder_Object = MibTableColumn
cfprIppoolPoolAssignmentOrder = _CfprIppoolPoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 5),
    _CfprIppoolPoolAssignmentOrder_Type()
)
cfprIppoolPoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolAssignmentOrder.setStatus("current")
_CfprIppoolPoolDescr_Type = SnmpAdminString
_CfprIppoolPoolDescr_Object = MibTableColumn
cfprIppoolPoolDescr = _CfprIppoolPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 6),
    _CfprIppoolPoolDescr_Type()
)
cfprIppoolPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolDescr.setStatus("current")
_CfprIppoolPoolExtManaged_Type = CfprIppoolManagementMode
_CfprIppoolPoolExtManaged_Object = MibTableColumn
cfprIppoolPoolExtManaged = _CfprIppoolPoolExtManaged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 7),
    _CfprIppoolPoolExtManaged_Type()
)
cfprIppoolPoolExtManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolExtManaged.setStatus("current")
_CfprIppoolPoolGuid_Type = SnmpAdminString
_CfprIppoolPoolGuid_Object = MibTableColumn
cfprIppoolPoolGuid = _CfprIppoolPoolGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 8),
    _CfprIppoolPoolGuid_Type()
)
cfprIppoolPoolGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolGuid.setStatus("current")
_CfprIppoolPoolIntId_Type = SnmpAdminString
_CfprIppoolPoolIntId_Object = MibTableColumn
cfprIppoolPoolIntId = _CfprIppoolPoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 9),
    _CfprIppoolPoolIntId_Type()
)
cfprIppoolPoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolIntId.setStatus("current")
_CfprIppoolPoolIsNetBIOSEnabled_Type = CfprIppoolNetBIOSMode
_CfprIppoolPoolIsNetBIOSEnabled_Object = MibTableColumn
cfprIppoolPoolIsNetBIOSEnabled = _CfprIppoolPoolIsNetBIOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 10),
    _CfprIppoolPoolIsNetBIOSEnabled_Type()
)
cfprIppoolPoolIsNetBIOSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolIsNetBIOSEnabled.setStatus("current")
_CfprIppoolPoolName_Type = SnmpAdminString
_CfprIppoolPoolName_Object = MibTableColumn
cfprIppoolPoolName = _CfprIppoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 11),
    _CfprIppoolPoolName_Type()
)
cfprIppoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolName.setStatus("current")
_CfprIppoolPoolPolicyLevel_Type = Gauge32
_CfprIppoolPoolPolicyLevel_Object = MibTableColumn
cfprIppoolPoolPolicyLevel = _CfprIppoolPoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 12),
    _CfprIppoolPoolPolicyLevel_Type()
)
cfprIppoolPoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolPolicyLevel.setStatus("current")
_CfprIppoolPoolPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprIppoolPoolPolicyOwner_Object = MibTableColumn
cfprIppoolPoolPolicyOwner = _CfprIppoolPoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 13),
    _CfprIppoolPoolPolicyOwner_Type()
)
cfprIppoolPoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolPolicyOwner.setStatus("current")
_CfprIppoolPoolSize_Type = Gauge32
_CfprIppoolPoolSize_Object = MibTableColumn
cfprIppoolPoolSize = _CfprIppoolPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 14),
    _CfprIppoolPoolSize_Type()
)
cfprIppoolPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolSize.setStatus("current")
_CfprIppoolPoolSupportsDHCP_Type = CfprIppoolDHCPMode
_CfprIppoolPoolSupportsDHCP_Object = MibTableColumn
cfprIppoolPoolSupportsDHCP = _CfprIppoolPoolSupportsDHCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 15),
    _CfprIppoolPoolSupportsDHCP_Type()
)
cfprIppoolPoolSupportsDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolSupportsDHCP.setStatus("current")
_CfprIppoolPoolV4Assigned_Type = Gauge32
_CfprIppoolPoolV4Assigned_Object = MibTableColumn
cfprIppoolPoolV4Assigned = _CfprIppoolPoolV4Assigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 16),
    _CfprIppoolPoolV4Assigned_Type()
)
cfprIppoolPoolV4Assigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolV4Assigned.setStatus("current")
_CfprIppoolPoolV4Size_Type = Gauge32
_CfprIppoolPoolV4Size_Object = MibTableColumn
cfprIppoolPoolV4Size = _CfprIppoolPoolV4Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 17),
    _CfprIppoolPoolV4Size_Type()
)
cfprIppoolPoolV4Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolV4Size.setStatus("current")
_CfprIppoolPoolV6Assigned_Type = Gauge32
_CfprIppoolPoolV6Assigned_Object = MibTableColumn
cfprIppoolPoolV6Assigned = _CfprIppoolPoolV6Assigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 18),
    _CfprIppoolPoolV6Assigned_Type()
)
cfprIppoolPoolV6Assigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolV6Assigned.setStatus("current")
_CfprIppoolPoolV6Size_Type = Gauge32
_CfprIppoolPoolV6Size_Object = MibTableColumn
cfprIppoolPoolV6Size = _CfprIppoolPoolV6Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 6, 1, 19),
    _CfprIppoolPoolV6Size_Type()
)
cfprIppoolPoolV6Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolV6Size.setStatus("current")
_CfprIppoolPoolableTable_Object = MibTable
cfprIppoolPoolableTable = _CfprIppoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 7)
)
if mibBuilder.loadTexts:
    cfprIppoolPoolableTable.setStatus("current")
_CfprIppoolPoolableEntry_Object = MibTableRow
cfprIppoolPoolableEntry = _CfprIppoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 7, 1)
)
cfprIppoolPoolableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPPOOL-MIB", "cfprIppoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIppoolPoolableEntry.setStatus("current")
_CfprIppoolPoolableInstanceId_Type = CfprManagedObjectId
_CfprIppoolPoolableInstanceId_Object = MibTableColumn
cfprIppoolPoolableInstanceId = _CfprIppoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 7, 1, 1),
    _CfprIppoolPoolableInstanceId_Type()
)
cfprIppoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIppoolPoolableInstanceId.setStatus("current")
_CfprIppoolPoolableDn_Type = CfprManagedObjectDn
_CfprIppoolPoolableDn_Object = MibTableColumn
cfprIppoolPoolableDn = _CfprIppoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 7, 1, 2),
    _CfprIppoolPoolableDn_Type()
)
cfprIppoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolableDn.setStatus("current")
_CfprIppoolPoolableRn_Type = SnmpAdminString
_CfprIppoolPoolableRn_Object = MibTableColumn
cfprIppoolPoolableRn = _CfprIppoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 7, 1, 3),
    _CfprIppoolPoolableRn_Type()
)
cfprIppoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolableRn.setStatus("current")
_CfprIppoolPoolableId_Type = Unsigned64
_CfprIppoolPoolableId_Object = MibTableColumn
cfprIppoolPoolableId = _CfprIppoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 7, 1, 4),
    _CfprIppoolPoolableId_Type()
)
cfprIppoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolableId.setStatus("current")
_CfprIppoolPoolablePoolDn_Type = SnmpAdminString
_CfprIppoolPoolablePoolDn_Object = MibTableColumn
cfprIppoolPoolablePoolDn = _CfprIppoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 7, 1, 5),
    _CfprIppoolPoolablePoolDn_Type()
)
cfprIppoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPoolablePoolDn.setStatus("current")
_CfprIppoolPooledTable_Object = MibTable
cfprIppoolPooledTable = _CfprIppoolPooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8)
)
if mibBuilder.loadTexts:
    cfprIppoolPooledTable.setStatus("current")
_CfprIppoolPooledEntry_Object = MibTableRow
cfprIppoolPooledEntry = _CfprIppoolPooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1)
)
cfprIppoolPooledEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPPOOL-MIB", "cfprIppoolPooledInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIppoolPooledEntry.setStatus("current")
_CfprIppoolPooledInstanceId_Type = CfprManagedObjectId
_CfprIppoolPooledInstanceId_Object = MibTableColumn
cfprIppoolPooledInstanceId = _CfprIppoolPooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1, 1),
    _CfprIppoolPooledInstanceId_Type()
)
cfprIppoolPooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIppoolPooledInstanceId.setStatus("current")
_CfprIppoolPooledDn_Type = CfprManagedObjectDn
_CfprIppoolPooledDn_Object = MibTableColumn
cfprIppoolPooledDn = _CfprIppoolPooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1, 2),
    _CfprIppoolPooledDn_Type()
)
cfprIppoolPooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPooledDn.setStatus("current")
_CfprIppoolPooledRn_Type = SnmpAdminString
_CfprIppoolPooledRn_Object = MibTableColumn
cfprIppoolPooledRn = _CfprIppoolPooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1, 3),
    _CfprIppoolPooledRn_Type()
)
cfprIppoolPooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPooledRn.setStatus("current")
_CfprIppoolPooledAssigned_Type = TruthValue
_CfprIppoolPooledAssigned_Object = MibTableColumn
cfprIppoolPooledAssigned = _CfprIppoolPooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1, 4),
    _CfprIppoolPooledAssigned_Type()
)
cfprIppoolPooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPooledAssigned.setStatus("current")
_CfprIppoolPooledAssignedToDn_Type = SnmpAdminString
_CfprIppoolPooledAssignedToDn_Object = MibTableColumn
cfprIppoolPooledAssignedToDn = _CfprIppoolPooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1, 5),
    _CfprIppoolPooledAssignedToDn_Type()
)
cfprIppoolPooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPooledAssignedToDn.setStatus("current")
_CfprIppoolPooledDefGw_Type = InetAddressIPv4
_CfprIppoolPooledDefGw_Object = MibTableColumn
cfprIppoolPooledDefGw = _CfprIppoolPooledDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1, 6),
    _CfprIppoolPooledDefGw_Type()
)
cfprIppoolPooledDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPooledDefGw.setStatus("current")
_CfprIppoolPooledId_Type = InetAddressIPv4
_CfprIppoolPooledId_Object = MibTableColumn
cfprIppoolPooledId = _CfprIppoolPooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1, 7),
    _CfprIppoolPooledId_Type()
)
cfprIppoolPooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPooledId.setStatus("current")
_CfprIppoolPooledPoolableDn_Type = SnmpAdminString
_CfprIppoolPooledPoolableDn_Object = MibTableColumn
cfprIppoolPooledPoolableDn = _CfprIppoolPooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1, 8),
    _CfprIppoolPooledPoolableDn_Type()
)
cfprIppoolPooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPooledPoolableDn.setStatus("current")
_CfprIppoolPooledPrevAssignedToDn_Type = SnmpAdminString
_CfprIppoolPooledPrevAssignedToDn_Object = MibTableColumn
cfprIppoolPooledPrevAssignedToDn = _CfprIppoolPooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1, 9),
    _CfprIppoolPooledPrevAssignedToDn_Type()
)
cfprIppoolPooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPooledPrevAssignedToDn.setStatus("current")
_CfprIppoolPooledPrimDns_Type = InetAddressIPv4
_CfprIppoolPooledPrimDns_Object = MibTableColumn
cfprIppoolPooledPrimDns = _CfprIppoolPooledPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1, 10),
    _CfprIppoolPooledPrimDns_Type()
)
cfprIppoolPooledPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPooledPrimDns.setStatus("current")
_CfprIppoolPooledSecDns_Type = InetAddressIPv4
_CfprIppoolPooledSecDns_Object = MibTableColumn
cfprIppoolPooledSecDns = _CfprIppoolPooledSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1, 11),
    _CfprIppoolPooledSecDns_Type()
)
cfprIppoolPooledSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPooledSecDns.setStatus("current")
_CfprIppoolPooledSubnet_Type = InetAddressIPv4
_CfprIppoolPooledSubnet_Object = MibTableColumn
cfprIppoolPooledSubnet = _CfprIppoolPooledSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 8, 1, 12),
    _CfprIppoolPooledSubnet_Type()
)
cfprIppoolPooledSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolPooledSubnet.setStatus("current")
_CfprIppoolUniverseTable_Object = MibTable
cfprIppoolUniverseTable = _CfprIppoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 9)
)
if mibBuilder.loadTexts:
    cfprIppoolUniverseTable.setStatus("current")
_CfprIppoolUniverseEntry_Object = MibTableRow
cfprIppoolUniverseEntry = _CfprIppoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 9, 1)
)
cfprIppoolUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IPPOOL-MIB", "cfprIppoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIppoolUniverseEntry.setStatus("current")
_CfprIppoolUniverseInstanceId_Type = CfprManagedObjectId
_CfprIppoolUniverseInstanceId_Object = MibTableColumn
cfprIppoolUniverseInstanceId = _CfprIppoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 9, 1, 1),
    _CfprIppoolUniverseInstanceId_Type()
)
cfprIppoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIppoolUniverseInstanceId.setStatus("current")
_CfprIppoolUniverseDn_Type = CfprManagedObjectDn
_CfprIppoolUniverseDn_Object = MibTableColumn
cfprIppoolUniverseDn = _CfprIppoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 9, 1, 2),
    _CfprIppoolUniverseDn_Type()
)
cfprIppoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolUniverseDn.setStatus("current")
_CfprIppoolUniverseRn_Type = SnmpAdminString
_CfprIppoolUniverseRn_Object = MibTableColumn
cfprIppoolUniverseRn = _CfprIppoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 41, 9, 1, 3),
    _CfprIppoolUniverseRn_Type()
)
cfprIppoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIppoolUniverseRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-IPPOOL-MIB",
    **{"cfprIppoolObjects": cfprIppoolObjects,
       "cfprIppoolAddrTable": cfprIppoolAddrTable,
       "cfprIppoolAddrEntry": cfprIppoolAddrEntry,
       "cfprIppoolAddrInstanceId": cfprIppoolAddrInstanceId,
       "cfprIppoolAddrDn": cfprIppoolAddrDn,
       "cfprIppoolAddrRn": cfprIppoolAddrRn,
       "cfprIppoolAddrAssigned": cfprIppoolAddrAssigned,
       "cfprIppoolAddrAssignedToDn": cfprIppoolAddrAssignedToDn,
       "cfprIppoolAddrGlobalAssignedCnt": cfprIppoolAddrGlobalAssignedCnt,
       "cfprIppoolAddrGlobalDefinedCnt": cfprIppoolAddrGlobalDefinedCnt,
       "cfprIppoolAddrId": cfprIppoolAddrId,
       "cfprIppoolAddrOwner": cfprIppoolAddrOwner,
       "cfprIppoolBlockTable": cfprIppoolBlockTable,
       "cfprIppoolBlockEntry": cfprIppoolBlockEntry,
       "cfprIppoolBlockInstanceId": cfprIppoolBlockInstanceId,
       "cfprIppoolBlockDn": cfprIppoolBlockDn,
       "cfprIppoolBlockRn": cfprIppoolBlockRn,
       "cfprIppoolBlockDefGw": cfprIppoolBlockDefGw,
       "cfprIppoolBlockFrom": cfprIppoolBlockFrom,
       "cfprIppoolBlockPrimDns": cfprIppoolBlockPrimDns,
       "cfprIppoolBlockSecDns": cfprIppoolBlockSecDns,
       "cfprIppoolBlockSubnet": cfprIppoolBlockSubnet,
       "cfprIppoolBlockTo": cfprIppoolBlockTo,
       "cfprIppoolIpV6AddrTable": cfprIppoolIpV6AddrTable,
       "cfprIppoolIpV6AddrEntry": cfprIppoolIpV6AddrEntry,
       "cfprIppoolIpV6AddrInstanceId": cfprIppoolIpV6AddrInstanceId,
       "cfprIppoolIpV6AddrDn": cfprIppoolIpV6AddrDn,
       "cfprIppoolIpV6AddrRn": cfprIppoolIpV6AddrRn,
       "cfprIppoolIpV6AddrAssigned": cfprIppoolIpV6AddrAssigned,
       "cfprIppoolIpV6AddrAssignedToDn": cfprIppoolIpV6AddrAssignedToDn,
       "cfprIppoolIpV6AddrGlobalAssignedCnt": cfprIppoolIpV6AddrGlobalAssignedCnt,
       "cfprIppoolIpV6AddrGlobalDefinedCnt": cfprIppoolIpV6AddrGlobalDefinedCnt,
       "cfprIppoolIpV6AddrId": cfprIppoolIpV6AddrId,
       "cfprIppoolIpV6AddrOwner": cfprIppoolIpV6AddrOwner,
       "cfprIppoolIpV6BlockTable": cfprIppoolIpV6BlockTable,
       "cfprIppoolIpV6BlockEntry": cfprIppoolIpV6BlockEntry,
       "cfprIppoolIpV6BlockInstanceId": cfprIppoolIpV6BlockInstanceId,
       "cfprIppoolIpV6BlockDn": cfprIppoolIpV6BlockDn,
       "cfprIppoolIpV6BlockRn": cfprIppoolIpV6BlockRn,
       "cfprIppoolIpV6BlockDefGw": cfprIppoolIpV6BlockDefGw,
       "cfprIppoolIpV6BlockFrom": cfprIppoolIpV6BlockFrom,
       "cfprIppoolIpV6BlockPrefix": cfprIppoolIpV6BlockPrefix,
       "cfprIppoolIpV6BlockPrimDns": cfprIppoolIpV6BlockPrimDns,
       "cfprIppoolIpV6BlockSecDns": cfprIppoolIpV6BlockSecDns,
       "cfprIppoolIpV6BlockTo": cfprIppoolIpV6BlockTo,
       "cfprIppoolIpV6PooledTable": cfprIppoolIpV6PooledTable,
       "cfprIppoolIpV6PooledEntry": cfprIppoolIpV6PooledEntry,
       "cfprIppoolIpV6PooledInstanceId": cfprIppoolIpV6PooledInstanceId,
       "cfprIppoolIpV6PooledDn": cfprIppoolIpV6PooledDn,
       "cfprIppoolIpV6PooledRn": cfprIppoolIpV6PooledRn,
       "cfprIppoolIpV6PooledAssigned": cfprIppoolIpV6PooledAssigned,
       "cfprIppoolIpV6PooledAssignedToDn": cfprIppoolIpV6PooledAssignedToDn,
       "cfprIppoolIpV6PooledDefGw": cfprIppoolIpV6PooledDefGw,
       "cfprIppoolIpV6PooledId": cfprIppoolIpV6PooledId,
       "cfprIppoolIpV6PooledPoolableDn": cfprIppoolIpV6PooledPoolableDn,
       "cfprIppoolIpV6PooledPrefix": cfprIppoolIpV6PooledPrefix,
       "cfprIppoolIpV6PooledPrevAssignedToDn": cfprIppoolIpV6PooledPrevAssignedToDn,
       "cfprIppoolIpV6PooledPrimDns": cfprIppoolIpV6PooledPrimDns,
       "cfprIppoolIpV6PooledSecDns": cfprIppoolIpV6PooledSecDns,
       "cfprIppoolPoolTable": cfprIppoolPoolTable,
       "cfprIppoolPoolEntry": cfprIppoolPoolEntry,
       "cfprIppoolPoolInstanceId": cfprIppoolPoolInstanceId,
       "cfprIppoolPoolDn": cfprIppoolPoolDn,
       "cfprIppoolPoolRn": cfprIppoolPoolRn,
       "cfprIppoolPoolAssigned": cfprIppoolPoolAssigned,
       "cfprIppoolPoolAssignmentOrder": cfprIppoolPoolAssignmentOrder,
       "cfprIppoolPoolDescr": cfprIppoolPoolDescr,
       "cfprIppoolPoolExtManaged": cfprIppoolPoolExtManaged,
       "cfprIppoolPoolGuid": cfprIppoolPoolGuid,
       "cfprIppoolPoolIntId": cfprIppoolPoolIntId,
       "cfprIppoolPoolIsNetBIOSEnabled": cfprIppoolPoolIsNetBIOSEnabled,
       "cfprIppoolPoolName": cfprIppoolPoolName,
       "cfprIppoolPoolPolicyLevel": cfprIppoolPoolPolicyLevel,
       "cfprIppoolPoolPolicyOwner": cfprIppoolPoolPolicyOwner,
       "cfprIppoolPoolSize": cfprIppoolPoolSize,
       "cfprIppoolPoolSupportsDHCP": cfprIppoolPoolSupportsDHCP,
       "cfprIppoolPoolV4Assigned": cfprIppoolPoolV4Assigned,
       "cfprIppoolPoolV4Size": cfprIppoolPoolV4Size,
       "cfprIppoolPoolV6Assigned": cfprIppoolPoolV6Assigned,
       "cfprIppoolPoolV6Size": cfprIppoolPoolV6Size,
       "cfprIppoolPoolableTable": cfprIppoolPoolableTable,
       "cfprIppoolPoolableEntry": cfprIppoolPoolableEntry,
       "cfprIppoolPoolableInstanceId": cfprIppoolPoolableInstanceId,
       "cfprIppoolPoolableDn": cfprIppoolPoolableDn,
       "cfprIppoolPoolableRn": cfprIppoolPoolableRn,
       "cfprIppoolPoolableId": cfprIppoolPoolableId,
       "cfprIppoolPoolablePoolDn": cfprIppoolPoolablePoolDn,
       "cfprIppoolPooledTable": cfprIppoolPooledTable,
       "cfprIppoolPooledEntry": cfprIppoolPooledEntry,
       "cfprIppoolPooledInstanceId": cfprIppoolPooledInstanceId,
       "cfprIppoolPooledDn": cfprIppoolPooledDn,
       "cfprIppoolPooledRn": cfprIppoolPooledRn,
       "cfprIppoolPooledAssigned": cfprIppoolPooledAssigned,
       "cfprIppoolPooledAssignedToDn": cfprIppoolPooledAssignedToDn,
       "cfprIppoolPooledDefGw": cfprIppoolPooledDefGw,
       "cfprIppoolPooledId": cfprIppoolPooledId,
       "cfprIppoolPooledPoolableDn": cfprIppoolPooledPoolableDn,
       "cfprIppoolPooledPrevAssignedToDn": cfprIppoolPooledPrevAssignedToDn,
       "cfprIppoolPooledPrimDns": cfprIppoolPooledPrimDns,
       "cfprIppoolPooledSecDns": cfprIppoolPooledSecDns,
       "cfprIppoolPooledSubnet": cfprIppoolPooledSubnet,
       "cfprIppoolUniverseTable": cfprIppoolUniverseTable,
       "cfprIppoolUniverseEntry": cfprIppoolUniverseEntry,
       "cfprIppoolUniverseInstanceId": cfprIppoolUniverseInstanceId,
       "cfprIppoolUniverseDn": cfprIppoolUniverseDn,
       "cfprIppoolUniverseRn": cfprIppoolUniverseRn}
)
