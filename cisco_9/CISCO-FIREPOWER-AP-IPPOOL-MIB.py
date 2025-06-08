# SNMP MIB module (CISCO-FIREPOWER-AP-IPPOOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-IPPOOL-MIB.mib
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

(CfprApIppoolDHCPMode,
 CfprApIppoolManagementMode,
 CfprApIppoolNetBIOSMode,
 CfprApIppoolPoolAssignmentOrder,
 CfprApPolicyPolicyOwner,
 CfprApPoolElementOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApIppoolDHCPMode",
    "CfprApIppoolManagementMode",
    "CfprApIppoolNetBIOSMode",
    "CfprApIppoolPoolAssignmentOrder",
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

cfprApIppoolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApIppoolAddrTable_Object = MibTable
cfprApIppoolAddrTable = _CfprApIppoolAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 1)
)
if mibBuilder.loadTexts:
    cfprApIppoolAddrTable.setStatus("current")
_CfprApIppoolAddrEntry_Object = MibTableRow
cfprApIppoolAddrEntry = _CfprApIppoolAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 1, 1)
)
cfprApIppoolAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IPPOOL-MIB", "cfprApIppoolAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIppoolAddrEntry.setStatus("current")
_CfprApIppoolAddrInstanceId_Type = CfprApManagedObjectId
_CfprApIppoolAddrInstanceId_Object = MibTableColumn
cfprApIppoolAddrInstanceId = _CfprApIppoolAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 1, 1, 1),
    _CfprApIppoolAddrInstanceId_Type()
)
cfprApIppoolAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIppoolAddrInstanceId.setStatus("current")
_CfprApIppoolAddrDn_Type = CfprApManagedObjectDn
_CfprApIppoolAddrDn_Object = MibTableColumn
cfprApIppoolAddrDn = _CfprApIppoolAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 1, 1, 2),
    _CfprApIppoolAddrDn_Type()
)
cfprApIppoolAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolAddrDn.setStatus("current")
_CfprApIppoolAddrRn_Type = SnmpAdminString
_CfprApIppoolAddrRn_Object = MibTableColumn
cfprApIppoolAddrRn = _CfprApIppoolAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 1, 1, 3),
    _CfprApIppoolAddrRn_Type()
)
cfprApIppoolAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolAddrRn.setStatus("current")
_CfprApIppoolAddrAssigned_Type = TruthValue
_CfprApIppoolAddrAssigned_Object = MibTableColumn
cfprApIppoolAddrAssigned = _CfprApIppoolAddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 1, 1, 4),
    _CfprApIppoolAddrAssigned_Type()
)
cfprApIppoolAddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolAddrAssigned.setStatus("current")
_CfprApIppoolAddrAssignedToDn_Type = SnmpAdminString
_CfprApIppoolAddrAssignedToDn_Object = MibTableColumn
cfprApIppoolAddrAssignedToDn = _CfprApIppoolAddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 1, 1, 5),
    _CfprApIppoolAddrAssignedToDn_Type()
)
cfprApIppoolAddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolAddrAssignedToDn.setStatus("current")
_CfprApIppoolAddrGlobalAssignedCnt_Type = Gauge32
_CfprApIppoolAddrGlobalAssignedCnt_Object = MibTableColumn
cfprApIppoolAddrGlobalAssignedCnt = _CfprApIppoolAddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 1, 1, 6),
    _CfprApIppoolAddrGlobalAssignedCnt_Type()
)
cfprApIppoolAddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolAddrGlobalAssignedCnt.setStatus("current")
_CfprApIppoolAddrGlobalDefinedCnt_Type = Gauge32
_CfprApIppoolAddrGlobalDefinedCnt_Object = MibTableColumn
cfprApIppoolAddrGlobalDefinedCnt = _CfprApIppoolAddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 1, 1, 7),
    _CfprApIppoolAddrGlobalDefinedCnt_Type()
)
cfprApIppoolAddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolAddrGlobalDefinedCnt.setStatus("current")
_CfprApIppoolAddrId_Type = InetAddressIPv4
_CfprApIppoolAddrId_Object = MibTableColumn
cfprApIppoolAddrId = _CfprApIppoolAddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 1, 1, 8),
    _CfprApIppoolAddrId_Type()
)
cfprApIppoolAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolAddrId.setStatus("current")
_CfprApIppoolAddrOwner_Type = CfprApPoolElementOwner
_CfprApIppoolAddrOwner_Object = MibTableColumn
cfprApIppoolAddrOwner = _CfprApIppoolAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 1, 1, 9),
    _CfprApIppoolAddrOwner_Type()
)
cfprApIppoolAddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolAddrOwner.setStatus("current")
_CfprApIppoolBlockTable_Object = MibTable
cfprApIppoolBlockTable = _CfprApIppoolBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 2)
)
if mibBuilder.loadTexts:
    cfprApIppoolBlockTable.setStatus("current")
_CfprApIppoolBlockEntry_Object = MibTableRow
cfprApIppoolBlockEntry = _CfprApIppoolBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 2, 1)
)
cfprApIppoolBlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IPPOOL-MIB", "cfprApIppoolBlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIppoolBlockEntry.setStatus("current")
_CfprApIppoolBlockInstanceId_Type = CfprApManagedObjectId
_CfprApIppoolBlockInstanceId_Object = MibTableColumn
cfprApIppoolBlockInstanceId = _CfprApIppoolBlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 2, 1, 1),
    _CfprApIppoolBlockInstanceId_Type()
)
cfprApIppoolBlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIppoolBlockInstanceId.setStatus("current")
_CfprApIppoolBlockDn_Type = CfprApManagedObjectDn
_CfprApIppoolBlockDn_Object = MibTableColumn
cfprApIppoolBlockDn = _CfprApIppoolBlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 2, 1, 2),
    _CfprApIppoolBlockDn_Type()
)
cfprApIppoolBlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolBlockDn.setStatus("current")
_CfprApIppoolBlockRn_Type = SnmpAdminString
_CfprApIppoolBlockRn_Object = MibTableColumn
cfprApIppoolBlockRn = _CfprApIppoolBlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 2, 1, 3),
    _CfprApIppoolBlockRn_Type()
)
cfprApIppoolBlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolBlockRn.setStatus("current")
_CfprApIppoolBlockDefGw_Type = InetAddressIPv4
_CfprApIppoolBlockDefGw_Object = MibTableColumn
cfprApIppoolBlockDefGw = _CfprApIppoolBlockDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 2, 1, 4),
    _CfprApIppoolBlockDefGw_Type()
)
cfprApIppoolBlockDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolBlockDefGw.setStatus("current")
_CfprApIppoolBlockFrom_Type = InetAddressIPv4
_CfprApIppoolBlockFrom_Object = MibTableColumn
cfprApIppoolBlockFrom = _CfprApIppoolBlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 2, 1, 5),
    _CfprApIppoolBlockFrom_Type()
)
cfprApIppoolBlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolBlockFrom.setStatus("current")
_CfprApIppoolBlockPrimDns_Type = InetAddressIPv4
_CfprApIppoolBlockPrimDns_Object = MibTableColumn
cfprApIppoolBlockPrimDns = _CfprApIppoolBlockPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 2, 1, 6),
    _CfprApIppoolBlockPrimDns_Type()
)
cfprApIppoolBlockPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolBlockPrimDns.setStatus("current")
_CfprApIppoolBlockSecDns_Type = InetAddressIPv4
_CfprApIppoolBlockSecDns_Object = MibTableColumn
cfprApIppoolBlockSecDns = _CfprApIppoolBlockSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 2, 1, 7),
    _CfprApIppoolBlockSecDns_Type()
)
cfprApIppoolBlockSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolBlockSecDns.setStatus("current")
_CfprApIppoolBlockSubnet_Type = InetAddressIPv4
_CfprApIppoolBlockSubnet_Object = MibTableColumn
cfprApIppoolBlockSubnet = _CfprApIppoolBlockSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 2, 1, 8),
    _CfprApIppoolBlockSubnet_Type()
)
cfprApIppoolBlockSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolBlockSubnet.setStatus("current")
_CfprApIppoolBlockTo_Type = InetAddressIPv4
_CfprApIppoolBlockTo_Object = MibTableColumn
cfprApIppoolBlockTo = _CfprApIppoolBlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 2, 1, 9),
    _CfprApIppoolBlockTo_Type()
)
cfprApIppoolBlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolBlockTo.setStatus("current")
_CfprApIppoolIpV6AddrTable_Object = MibTable
cfprApIppoolIpV6AddrTable = _CfprApIppoolIpV6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 3)
)
if mibBuilder.loadTexts:
    cfprApIppoolIpV6AddrTable.setStatus("current")
_CfprApIppoolIpV6AddrEntry_Object = MibTableRow
cfprApIppoolIpV6AddrEntry = _CfprApIppoolIpV6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 3, 1)
)
cfprApIppoolIpV6AddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IPPOOL-MIB", "cfprApIppoolIpV6AddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIppoolIpV6AddrEntry.setStatus("current")
_CfprApIppoolIpV6AddrInstanceId_Type = CfprApManagedObjectId
_CfprApIppoolIpV6AddrInstanceId_Object = MibTableColumn
cfprApIppoolIpV6AddrInstanceId = _CfprApIppoolIpV6AddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 3, 1, 1),
    _CfprApIppoolIpV6AddrInstanceId_Type()
)
cfprApIppoolIpV6AddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6AddrInstanceId.setStatus("current")
_CfprApIppoolIpV6AddrDn_Type = CfprApManagedObjectDn
_CfprApIppoolIpV6AddrDn_Object = MibTableColumn
cfprApIppoolIpV6AddrDn = _CfprApIppoolIpV6AddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 3, 1, 2),
    _CfprApIppoolIpV6AddrDn_Type()
)
cfprApIppoolIpV6AddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6AddrDn.setStatus("current")
_CfprApIppoolIpV6AddrRn_Type = SnmpAdminString
_CfprApIppoolIpV6AddrRn_Object = MibTableColumn
cfprApIppoolIpV6AddrRn = _CfprApIppoolIpV6AddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 3, 1, 3),
    _CfprApIppoolIpV6AddrRn_Type()
)
cfprApIppoolIpV6AddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6AddrRn.setStatus("current")
_CfprApIppoolIpV6AddrAssigned_Type = TruthValue
_CfprApIppoolIpV6AddrAssigned_Object = MibTableColumn
cfprApIppoolIpV6AddrAssigned = _CfprApIppoolIpV6AddrAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 3, 1, 4),
    _CfprApIppoolIpV6AddrAssigned_Type()
)
cfprApIppoolIpV6AddrAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6AddrAssigned.setStatus("current")
_CfprApIppoolIpV6AddrAssignedToDn_Type = SnmpAdminString
_CfprApIppoolIpV6AddrAssignedToDn_Object = MibTableColumn
cfprApIppoolIpV6AddrAssignedToDn = _CfprApIppoolIpV6AddrAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 3, 1, 5),
    _CfprApIppoolIpV6AddrAssignedToDn_Type()
)
cfprApIppoolIpV6AddrAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6AddrAssignedToDn.setStatus("current")
_CfprApIppoolIpV6AddrGlobalAssignedCnt_Type = Gauge32
_CfprApIppoolIpV6AddrGlobalAssignedCnt_Object = MibTableColumn
cfprApIppoolIpV6AddrGlobalAssignedCnt = _CfprApIppoolIpV6AddrGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 3, 1, 6),
    _CfprApIppoolIpV6AddrGlobalAssignedCnt_Type()
)
cfprApIppoolIpV6AddrGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6AddrGlobalAssignedCnt.setStatus("current")
_CfprApIppoolIpV6AddrGlobalDefinedCnt_Type = Gauge32
_CfprApIppoolIpV6AddrGlobalDefinedCnt_Object = MibTableColumn
cfprApIppoolIpV6AddrGlobalDefinedCnt = _CfprApIppoolIpV6AddrGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 3, 1, 7),
    _CfprApIppoolIpV6AddrGlobalDefinedCnt_Type()
)
cfprApIppoolIpV6AddrGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6AddrGlobalDefinedCnt.setStatus("current")
_CfprApIppoolIpV6AddrId_Type = InetAddressIPv6
_CfprApIppoolIpV6AddrId_Object = MibTableColumn
cfprApIppoolIpV6AddrId = _CfprApIppoolIpV6AddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 3, 1, 8),
    _CfprApIppoolIpV6AddrId_Type()
)
cfprApIppoolIpV6AddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6AddrId.setStatus("current")
_CfprApIppoolIpV6AddrOwner_Type = CfprApPoolElementOwner
_CfprApIppoolIpV6AddrOwner_Object = MibTableColumn
cfprApIppoolIpV6AddrOwner = _CfprApIppoolIpV6AddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 3, 1, 9),
    _CfprApIppoolIpV6AddrOwner_Type()
)
cfprApIppoolIpV6AddrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6AddrOwner.setStatus("current")
_CfprApIppoolIpV6BlockTable_Object = MibTable
cfprApIppoolIpV6BlockTable = _CfprApIppoolIpV6BlockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 4)
)
if mibBuilder.loadTexts:
    cfprApIppoolIpV6BlockTable.setStatus("current")
_CfprApIppoolIpV6BlockEntry_Object = MibTableRow
cfprApIppoolIpV6BlockEntry = _CfprApIppoolIpV6BlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 4, 1)
)
cfprApIppoolIpV6BlockEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IPPOOL-MIB", "cfprApIppoolIpV6BlockInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIppoolIpV6BlockEntry.setStatus("current")
_CfprApIppoolIpV6BlockInstanceId_Type = CfprApManagedObjectId
_CfprApIppoolIpV6BlockInstanceId_Object = MibTableColumn
cfprApIppoolIpV6BlockInstanceId = _CfprApIppoolIpV6BlockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 4, 1, 1),
    _CfprApIppoolIpV6BlockInstanceId_Type()
)
cfprApIppoolIpV6BlockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6BlockInstanceId.setStatus("current")
_CfprApIppoolIpV6BlockDn_Type = CfprApManagedObjectDn
_CfprApIppoolIpV6BlockDn_Object = MibTableColumn
cfprApIppoolIpV6BlockDn = _CfprApIppoolIpV6BlockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 4, 1, 2),
    _CfprApIppoolIpV6BlockDn_Type()
)
cfprApIppoolIpV6BlockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6BlockDn.setStatus("current")
_CfprApIppoolIpV6BlockRn_Type = SnmpAdminString
_CfprApIppoolIpV6BlockRn_Object = MibTableColumn
cfprApIppoolIpV6BlockRn = _CfprApIppoolIpV6BlockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 4, 1, 3),
    _CfprApIppoolIpV6BlockRn_Type()
)
cfprApIppoolIpV6BlockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6BlockRn.setStatus("current")
_CfprApIppoolIpV6BlockDefGw_Type = InetAddressIPv6
_CfprApIppoolIpV6BlockDefGw_Object = MibTableColumn
cfprApIppoolIpV6BlockDefGw = _CfprApIppoolIpV6BlockDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 4, 1, 4),
    _CfprApIppoolIpV6BlockDefGw_Type()
)
cfprApIppoolIpV6BlockDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6BlockDefGw.setStatus("current")
_CfprApIppoolIpV6BlockFrom_Type = InetAddressIPv6
_CfprApIppoolIpV6BlockFrom_Object = MibTableColumn
cfprApIppoolIpV6BlockFrom = _CfprApIppoolIpV6BlockFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 4, 1, 5),
    _CfprApIppoolIpV6BlockFrom_Type()
)
cfprApIppoolIpV6BlockFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6BlockFrom.setStatus("current")
_CfprApIppoolIpV6BlockPrefix_Type = Gauge32
_CfprApIppoolIpV6BlockPrefix_Object = MibTableColumn
cfprApIppoolIpV6BlockPrefix = _CfprApIppoolIpV6BlockPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 4, 1, 6),
    _CfprApIppoolIpV6BlockPrefix_Type()
)
cfprApIppoolIpV6BlockPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6BlockPrefix.setStatus("current")
_CfprApIppoolIpV6BlockPrimDns_Type = InetAddressIPv6
_CfprApIppoolIpV6BlockPrimDns_Object = MibTableColumn
cfprApIppoolIpV6BlockPrimDns = _CfprApIppoolIpV6BlockPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 4, 1, 7),
    _CfprApIppoolIpV6BlockPrimDns_Type()
)
cfprApIppoolIpV6BlockPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6BlockPrimDns.setStatus("current")
_CfprApIppoolIpV6BlockSecDns_Type = InetAddressIPv6
_CfprApIppoolIpV6BlockSecDns_Object = MibTableColumn
cfprApIppoolIpV6BlockSecDns = _CfprApIppoolIpV6BlockSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 4, 1, 8),
    _CfprApIppoolIpV6BlockSecDns_Type()
)
cfprApIppoolIpV6BlockSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6BlockSecDns.setStatus("current")
_CfprApIppoolIpV6BlockTo_Type = InetAddressIPv6
_CfprApIppoolIpV6BlockTo_Object = MibTableColumn
cfprApIppoolIpV6BlockTo = _CfprApIppoolIpV6BlockTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 4, 1, 9),
    _CfprApIppoolIpV6BlockTo_Type()
)
cfprApIppoolIpV6BlockTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6BlockTo.setStatus("current")
_CfprApIppoolIpV6PooledTable_Object = MibTable
cfprApIppoolIpV6PooledTable = _CfprApIppoolIpV6PooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5)
)
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledTable.setStatus("current")
_CfprApIppoolIpV6PooledEntry_Object = MibTableRow
cfprApIppoolIpV6PooledEntry = _CfprApIppoolIpV6PooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1)
)
cfprApIppoolIpV6PooledEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IPPOOL-MIB", "cfprApIppoolIpV6PooledInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledEntry.setStatus("current")
_CfprApIppoolIpV6PooledInstanceId_Type = CfprApManagedObjectId
_CfprApIppoolIpV6PooledInstanceId_Object = MibTableColumn
cfprApIppoolIpV6PooledInstanceId = _CfprApIppoolIpV6PooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1, 1),
    _CfprApIppoolIpV6PooledInstanceId_Type()
)
cfprApIppoolIpV6PooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledInstanceId.setStatus("current")
_CfprApIppoolIpV6PooledDn_Type = CfprApManagedObjectDn
_CfprApIppoolIpV6PooledDn_Object = MibTableColumn
cfprApIppoolIpV6PooledDn = _CfprApIppoolIpV6PooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1, 2),
    _CfprApIppoolIpV6PooledDn_Type()
)
cfprApIppoolIpV6PooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledDn.setStatus("current")
_CfprApIppoolIpV6PooledRn_Type = SnmpAdminString
_CfprApIppoolIpV6PooledRn_Object = MibTableColumn
cfprApIppoolIpV6PooledRn = _CfprApIppoolIpV6PooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1, 3),
    _CfprApIppoolIpV6PooledRn_Type()
)
cfprApIppoolIpV6PooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledRn.setStatus("current")
_CfprApIppoolIpV6PooledAssigned_Type = TruthValue
_CfprApIppoolIpV6PooledAssigned_Object = MibTableColumn
cfprApIppoolIpV6PooledAssigned = _CfprApIppoolIpV6PooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1, 4),
    _CfprApIppoolIpV6PooledAssigned_Type()
)
cfprApIppoolIpV6PooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledAssigned.setStatus("current")
_CfprApIppoolIpV6PooledAssignedToDn_Type = SnmpAdminString
_CfprApIppoolIpV6PooledAssignedToDn_Object = MibTableColumn
cfprApIppoolIpV6PooledAssignedToDn = _CfprApIppoolIpV6PooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1, 5),
    _CfprApIppoolIpV6PooledAssignedToDn_Type()
)
cfprApIppoolIpV6PooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledAssignedToDn.setStatus("current")
_CfprApIppoolIpV6PooledDefGw_Type = InetAddressIPv6
_CfprApIppoolIpV6PooledDefGw_Object = MibTableColumn
cfprApIppoolIpV6PooledDefGw = _CfprApIppoolIpV6PooledDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1, 6),
    _CfprApIppoolIpV6PooledDefGw_Type()
)
cfprApIppoolIpV6PooledDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledDefGw.setStatus("current")
_CfprApIppoolIpV6PooledId_Type = InetAddressIPv6
_CfprApIppoolIpV6PooledId_Object = MibTableColumn
cfprApIppoolIpV6PooledId = _CfprApIppoolIpV6PooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1, 7),
    _CfprApIppoolIpV6PooledId_Type()
)
cfprApIppoolIpV6PooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledId.setStatus("current")
_CfprApIppoolIpV6PooledPoolableDn_Type = SnmpAdminString
_CfprApIppoolIpV6PooledPoolableDn_Object = MibTableColumn
cfprApIppoolIpV6PooledPoolableDn = _CfprApIppoolIpV6PooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1, 8),
    _CfprApIppoolIpV6PooledPoolableDn_Type()
)
cfprApIppoolIpV6PooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledPoolableDn.setStatus("current")
_CfprApIppoolIpV6PooledPrefix_Type = Gauge32
_CfprApIppoolIpV6PooledPrefix_Object = MibTableColumn
cfprApIppoolIpV6PooledPrefix = _CfprApIppoolIpV6PooledPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1, 9),
    _CfprApIppoolIpV6PooledPrefix_Type()
)
cfprApIppoolIpV6PooledPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledPrefix.setStatus("current")
_CfprApIppoolIpV6PooledPrevAssignedToDn_Type = SnmpAdminString
_CfprApIppoolIpV6PooledPrevAssignedToDn_Object = MibTableColumn
cfprApIppoolIpV6PooledPrevAssignedToDn = _CfprApIppoolIpV6PooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1, 10),
    _CfprApIppoolIpV6PooledPrevAssignedToDn_Type()
)
cfprApIppoolIpV6PooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledPrevAssignedToDn.setStatus("current")
_CfprApIppoolIpV6PooledPrimDns_Type = InetAddressIPv6
_CfprApIppoolIpV6PooledPrimDns_Object = MibTableColumn
cfprApIppoolIpV6PooledPrimDns = _CfprApIppoolIpV6PooledPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1, 11),
    _CfprApIppoolIpV6PooledPrimDns_Type()
)
cfprApIppoolIpV6PooledPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledPrimDns.setStatus("current")
_CfprApIppoolIpV6PooledSecDns_Type = InetAddressIPv6
_CfprApIppoolIpV6PooledSecDns_Object = MibTableColumn
cfprApIppoolIpV6PooledSecDns = _CfprApIppoolIpV6PooledSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 5, 1, 12),
    _CfprApIppoolIpV6PooledSecDns_Type()
)
cfprApIppoolIpV6PooledSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolIpV6PooledSecDns.setStatus("current")
_CfprApIppoolPoolTable_Object = MibTable
cfprApIppoolPoolTable = _CfprApIppoolPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6)
)
if mibBuilder.loadTexts:
    cfprApIppoolPoolTable.setStatus("current")
_CfprApIppoolPoolEntry_Object = MibTableRow
cfprApIppoolPoolEntry = _CfprApIppoolPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1)
)
cfprApIppoolPoolEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IPPOOL-MIB", "cfprApIppoolPoolInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIppoolPoolEntry.setStatus("current")
_CfprApIppoolPoolInstanceId_Type = CfprApManagedObjectId
_CfprApIppoolPoolInstanceId_Object = MibTableColumn
cfprApIppoolPoolInstanceId = _CfprApIppoolPoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 1),
    _CfprApIppoolPoolInstanceId_Type()
)
cfprApIppoolPoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIppoolPoolInstanceId.setStatus("current")
_CfprApIppoolPoolDn_Type = CfprApManagedObjectDn
_CfprApIppoolPoolDn_Object = MibTableColumn
cfprApIppoolPoolDn = _CfprApIppoolPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 2),
    _CfprApIppoolPoolDn_Type()
)
cfprApIppoolPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolDn.setStatus("current")
_CfprApIppoolPoolRn_Type = SnmpAdminString
_CfprApIppoolPoolRn_Object = MibTableColumn
cfprApIppoolPoolRn = _CfprApIppoolPoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 3),
    _CfprApIppoolPoolRn_Type()
)
cfprApIppoolPoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolRn.setStatus("current")
_CfprApIppoolPoolAssigned_Type = Gauge32
_CfprApIppoolPoolAssigned_Object = MibTableColumn
cfprApIppoolPoolAssigned = _CfprApIppoolPoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 4),
    _CfprApIppoolPoolAssigned_Type()
)
cfprApIppoolPoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolAssigned.setStatus("current")
_CfprApIppoolPoolAssignmentOrder_Type = CfprApIppoolPoolAssignmentOrder
_CfprApIppoolPoolAssignmentOrder_Object = MibTableColumn
cfprApIppoolPoolAssignmentOrder = _CfprApIppoolPoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 5),
    _CfprApIppoolPoolAssignmentOrder_Type()
)
cfprApIppoolPoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolAssignmentOrder.setStatus("current")
_CfprApIppoolPoolDescr_Type = SnmpAdminString
_CfprApIppoolPoolDescr_Object = MibTableColumn
cfprApIppoolPoolDescr = _CfprApIppoolPoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 6),
    _CfprApIppoolPoolDescr_Type()
)
cfprApIppoolPoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolDescr.setStatus("current")
_CfprApIppoolPoolExtManaged_Type = CfprApIppoolManagementMode
_CfprApIppoolPoolExtManaged_Object = MibTableColumn
cfprApIppoolPoolExtManaged = _CfprApIppoolPoolExtManaged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 7),
    _CfprApIppoolPoolExtManaged_Type()
)
cfprApIppoolPoolExtManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolExtManaged.setStatus("current")
_CfprApIppoolPoolGuid_Type = SnmpAdminString
_CfprApIppoolPoolGuid_Object = MibTableColumn
cfprApIppoolPoolGuid = _CfprApIppoolPoolGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 8),
    _CfprApIppoolPoolGuid_Type()
)
cfprApIppoolPoolGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolGuid.setStatus("current")
_CfprApIppoolPoolIntId_Type = SnmpAdminString
_CfprApIppoolPoolIntId_Object = MibTableColumn
cfprApIppoolPoolIntId = _CfprApIppoolPoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 9),
    _CfprApIppoolPoolIntId_Type()
)
cfprApIppoolPoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolIntId.setStatus("current")
_CfprApIppoolPoolIsNetBIOSEnabled_Type = CfprApIppoolNetBIOSMode
_CfprApIppoolPoolIsNetBIOSEnabled_Object = MibTableColumn
cfprApIppoolPoolIsNetBIOSEnabled = _CfprApIppoolPoolIsNetBIOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 10),
    _CfprApIppoolPoolIsNetBIOSEnabled_Type()
)
cfprApIppoolPoolIsNetBIOSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolIsNetBIOSEnabled.setStatus("current")
_CfprApIppoolPoolName_Type = SnmpAdminString
_CfprApIppoolPoolName_Object = MibTableColumn
cfprApIppoolPoolName = _CfprApIppoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 11),
    _CfprApIppoolPoolName_Type()
)
cfprApIppoolPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolName.setStatus("current")
_CfprApIppoolPoolPolicyLevel_Type = Gauge32
_CfprApIppoolPoolPolicyLevel_Object = MibTableColumn
cfprApIppoolPoolPolicyLevel = _CfprApIppoolPoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 12),
    _CfprApIppoolPoolPolicyLevel_Type()
)
cfprApIppoolPoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolPolicyLevel.setStatus("current")
_CfprApIppoolPoolPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApIppoolPoolPolicyOwner_Object = MibTableColumn
cfprApIppoolPoolPolicyOwner = _CfprApIppoolPoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 13),
    _CfprApIppoolPoolPolicyOwner_Type()
)
cfprApIppoolPoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolPolicyOwner.setStatus("current")
_CfprApIppoolPoolSize_Type = Gauge32
_CfprApIppoolPoolSize_Object = MibTableColumn
cfprApIppoolPoolSize = _CfprApIppoolPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 14),
    _CfprApIppoolPoolSize_Type()
)
cfprApIppoolPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolSize.setStatus("current")
_CfprApIppoolPoolSupportsDHCP_Type = CfprApIppoolDHCPMode
_CfprApIppoolPoolSupportsDHCP_Object = MibTableColumn
cfprApIppoolPoolSupportsDHCP = _CfprApIppoolPoolSupportsDHCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 15),
    _CfprApIppoolPoolSupportsDHCP_Type()
)
cfprApIppoolPoolSupportsDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolSupportsDHCP.setStatus("current")
_CfprApIppoolPoolV4Assigned_Type = Gauge32
_CfprApIppoolPoolV4Assigned_Object = MibTableColumn
cfprApIppoolPoolV4Assigned = _CfprApIppoolPoolV4Assigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 16),
    _CfprApIppoolPoolV4Assigned_Type()
)
cfprApIppoolPoolV4Assigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolV4Assigned.setStatus("current")
_CfprApIppoolPoolV4Size_Type = Gauge32
_CfprApIppoolPoolV4Size_Object = MibTableColumn
cfprApIppoolPoolV4Size = _CfprApIppoolPoolV4Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 17),
    _CfprApIppoolPoolV4Size_Type()
)
cfprApIppoolPoolV4Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolV4Size.setStatus("current")
_CfprApIppoolPoolV6Assigned_Type = Gauge32
_CfprApIppoolPoolV6Assigned_Object = MibTableColumn
cfprApIppoolPoolV6Assigned = _CfprApIppoolPoolV6Assigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 18),
    _CfprApIppoolPoolV6Assigned_Type()
)
cfprApIppoolPoolV6Assigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolV6Assigned.setStatus("current")
_CfprApIppoolPoolV6Size_Type = Gauge32
_CfprApIppoolPoolV6Size_Object = MibTableColumn
cfprApIppoolPoolV6Size = _CfprApIppoolPoolV6Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 6, 1, 19),
    _CfprApIppoolPoolV6Size_Type()
)
cfprApIppoolPoolV6Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolV6Size.setStatus("current")
_CfprApIppoolPoolableTable_Object = MibTable
cfprApIppoolPoolableTable = _CfprApIppoolPoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 7)
)
if mibBuilder.loadTexts:
    cfprApIppoolPoolableTable.setStatus("current")
_CfprApIppoolPoolableEntry_Object = MibTableRow
cfprApIppoolPoolableEntry = _CfprApIppoolPoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 7, 1)
)
cfprApIppoolPoolableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IPPOOL-MIB", "cfprApIppoolPoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIppoolPoolableEntry.setStatus("current")
_CfprApIppoolPoolableInstanceId_Type = CfprApManagedObjectId
_CfprApIppoolPoolableInstanceId_Object = MibTableColumn
cfprApIppoolPoolableInstanceId = _CfprApIppoolPoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 7, 1, 1),
    _CfprApIppoolPoolableInstanceId_Type()
)
cfprApIppoolPoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIppoolPoolableInstanceId.setStatus("current")
_CfprApIppoolPoolableDn_Type = CfprApManagedObjectDn
_CfprApIppoolPoolableDn_Object = MibTableColumn
cfprApIppoolPoolableDn = _CfprApIppoolPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 7, 1, 2),
    _CfprApIppoolPoolableDn_Type()
)
cfprApIppoolPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolableDn.setStatus("current")
_CfprApIppoolPoolableRn_Type = SnmpAdminString
_CfprApIppoolPoolableRn_Object = MibTableColumn
cfprApIppoolPoolableRn = _CfprApIppoolPoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 7, 1, 3),
    _CfprApIppoolPoolableRn_Type()
)
cfprApIppoolPoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolableRn.setStatus("current")
_CfprApIppoolPoolableId_Type = Unsigned64
_CfprApIppoolPoolableId_Object = MibTableColumn
cfprApIppoolPoolableId = _CfprApIppoolPoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 7, 1, 4),
    _CfprApIppoolPoolableId_Type()
)
cfprApIppoolPoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolableId.setStatus("current")
_CfprApIppoolPoolablePoolDn_Type = SnmpAdminString
_CfprApIppoolPoolablePoolDn_Object = MibTableColumn
cfprApIppoolPoolablePoolDn = _CfprApIppoolPoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 7, 1, 5),
    _CfprApIppoolPoolablePoolDn_Type()
)
cfprApIppoolPoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPoolablePoolDn.setStatus("current")
_CfprApIppoolPooledTable_Object = MibTable
cfprApIppoolPooledTable = _CfprApIppoolPooledTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8)
)
if mibBuilder.loadTexts:
    cfprApIppoolPooledTable.setStatus("current")
_CfprApIppoolPooledEntry_Object = MibTableRow
cfprApIppoolPooledEntry = _CfprApIppoolPooledEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1)
)
cfprApIppoolPooledEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IPPOOL-MIB", "cfprApIppoolPooledInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIppoolPooledEntry.setStatus("current")
_CfprApIppoolPooledInstanceId_Type = CfprApManagedObjectId
_CfprApIppoolPooledInstanceId_Object = MibTableColumn
cfprApIppoolPooledInstanceId = _CfprApIppoolPooledInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1, 1),
    _CfprApIppoolPooledInstanceId_Type()
)
cfprApIppoolPooledInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIppoolPooledInstanceId.setStatus("current")
_CfprApIppoolPooledDn_Type = CfprApManagedObjectDn
_CfprApIppoolPooledDn_Object = MibTableColumn
cfprApIppoolPooledDn = _CfprApIppoolPooledDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1, 2),
    _CfprApIppoolPooledDn_Type()
)
cfprApIppoolPooledDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPooledDn.setStatus("current")
_CfprApIppoolPooledRn_Type = SnmpAdminString
_CfprApIppoolPooledRn_Object = MibTableColumn
cfprApIppoolPooledRn = _CfprApIppoolPooledRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1, 3),
    _CfprApIppoolPooledRn_Type()
)
cfprApIppoolPooledRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPooledRn.setStatus("current")
_CfprApIppoolPooledAssigned_Type = TruthValue
_CfprApIppoolPooledAssigned_Object = MibTableColumn
cfprApIppoolPooledAssigned = _CfprApIppoolPooledAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1, 4),
    _CfprApIppoolPooledAssigned_Type()
)
cfprApIppoolPooledAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPooledAssigned.setStatus("current")
_CfprApIppoolPooledAssignedToDn_Type = SnmpAdminString
_CfprApIppoolPooledAssignedToDn_Object = MibTableColumn
cfprApIppoolPooledAssignedToDn = _CfprApIppoolPooledAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1, 5),
    _CfprApIppoolPooledAssignedToDn_Type()
)
cfprApIppoolPooledAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPooledAssignedToDn.setStatus("current")
_CfprApIppoolPooledDefGw_Type = InetAddressIPv4
_CfprApIppoolPooledDefGw_Object = MibTableColumn
cfprApIppoolPooledDefGw = _CfprApIppoolPooledDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1, 6),
    _CfprApIppoolPooledDefGw_Type()
)
cfprApIppoolPooledDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPooledDefGw.setStatus("current")
_CfprApIppoolPooledId_Type = InetAddressIPv4
_CfprApIppoolPooledId_Object = MibTableColumn
cfprApIppoolPooledId = _CfprApIppoolPooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1, 7),
    _CfprApIppoolPooledId_Type()
)
cfprApIppoolPooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPooledId.setStatus("current")
_CfprApIppoolPooledPoolableDn_Type = SnmpAdminString
_CfprApIppoolPooledPoolableDn_Object = MibTableColumn
cfprApIppoolPooledPoolableDn = _CfprApIppoolPooledPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1, 8),
    _CfprApIppoolPooledPoolableDn_Type()
)
cfprApIppoolPooledPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPooledPoolableDn.setStatus("current")
_CfprApIppoolPooledPrevAssignedToDn_Type = SnmpAdminString
_CfprApIppoolPooledPrevAssignedToDn_Object = MibTableColumn
cfprApIppoolPooledPrevAssignedToDn = _CfprApIppoolPooledPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1, 9),
    _CfprApIppoolPooledPrevAssignedToDn_Type()
)
cfprApIppoolPooledPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPooledPrevAssignedToDn.setStatus("current")
_CfprApIppoolPooledPrimDns_Type = InetAddressIPv4
_CfprApIppoolPooledPrimDns_Object = MibTableColumn
cfprApIppoolPooledPrimDns = _CfprApIppoolPooledPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1, 10),
    _CfprApIppoolPooledPrimDns_Type()
)
cfprApIppoolPooledPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPooledPrimDns.setStatus("current")
_CfprApIppoolPooledSecDns_Type = InetAddressIPv4
_CfprApIppoolPooledSecDns_Object = MibTableColumn
cfprApIppoolPooledSecDns = _CfprApIppoolPooledSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1, 11),
    _CfprApIppoolPooledSecDns_Type()
)
cfprApIppoolPooledSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPooledSecDns.setStatus("current")
_CfprApIppoolPooledSubnet_Type = InetAddressIPv4
_CfprApIppoolPooledSubnet_Object = MibTableColumn
cfprApIppoolPooledSubnet = _CfprApIppoolPooledSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 8, 1, 12),
    _CfprApIppoolPooledSubnet_Type()
)
cfprApIppoolPooledSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolPooledSubnet.setStatus("current")
_CfprApIppoolUniverseTable_Object = MibTable
cfprApIppoolUniverseTable = _CfprApIppoolUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 9)
)
if mibBuilder.loadTexts:
    cfprApIppoolUniverseTable.setStatus("current")
_CfprApIppoolUniverseEntry_Object = MibTableRow
cfprApIppoolUniverseEntry = _CfprApIppoolUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 9, 1)
)
cfprApIppoolUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-IPPOOL-MIB", "cfprApIppoolUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApIppoolUniverseEntry.setStatus("current")
_CfprApIppoolUniverseInstanceId_Type = CfprApManagedObjectId
_CfprApIppoolUniverseInstanceId_Object = MibTableColumn
cfprApIppoolUniverseInstanceId = _CfprApIppoolUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 9, 1, 1),
    _CfprApIppoolUniverseInstanceId_Type()
)
cfprApIppoolUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApIppoolUniverseInstanceId.setStatus("current")
_CfprApIppoolUniverseDn_Type = CfprApManagedObjectDn
_CfprApIppoolUniverseDn_Object = MibTableColumn
cfprApIppoolUniverseDn = _CfprApIppoolUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 9, 1, 2),
    _CfprApIppoolUniverseDn_Type()
)
cfprApIppoolUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolUniverseDn.setStatus("current")
_CfprApIppoolUniverseRn_Type = SnmpAdminString
_CfprApIppoolUniverseRn_Object = MibTableColumn
cfprApIppoolUniverseRn = _CfprApIppoolUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 41, 9, 1, 3),
    _CfprApIppoolUniverseRn_Type()
)
cfprApIppoolUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApIppoolUniverseRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-IPPOOL-MIB",
    **{"cfprApIppoolObjects": cfprApIppoolObjects,
       "cfprApIppoolAddrTable": cfprApIppoolAddrTable,
       "cfprApIppoolAddrEntry": cfprApIppoolAddrEntry,
       "cfprApIppoolAddrInstanceId": cfprApIppoolAddrInstanceId,
       "cfprApIppoolAddrDn": cfprApIppoolAddrDn,
       "cfprApIppoolAddrRn": cfprApIppoolAddrRn,
       "cfprApIppoolAddrAssigned": cfprApIppoolAddrAssigned,
       "cfprApIppoolAddrAssignedToDn": cfprApIppoolAddrAssignedToDn,
       "cfprApIppoolAddrGlobalAssignedCnt": cfprApIppoolAddrGlobalAssignedCnt,
       "cfprApIppoolAddrGlobalDefinedCnt": cfprApIppoolAddrGlobalDefinedCnt,
       "cfprApIppoolAddrId": cfprApIppoolAddrId,
       "cfprApIppoolAddrOwner": cfprApIppoolAddrOwner,
       "cfprApIppoolBlockTable": cfprApIppoolBlockTable,
       "cfprApIppoolBlockEntry": cfprApIppoolBlockEntry,
       "cfprApIppoolBlockInstanceId": cfprApIppoolBlockInstanceId,
       "cfprApIppoolBlockDn": cfprApIppoolBlockDn,
       "cfprApIppoolBlockRn": cfprApIppoolBlockRn,
       "cfprApIppoolBlockDefGw": cfprApIppoolBlockDefGw,
       "cfprApIppoolBlockFrom": cfprApIppoolBlockFrom,
       "cfprApIppoolBlockPrimDns": cfprApIppoolBlockPrimDns,
       "cfprApIppoolBlockSecDns": cfprApIppoolBlockSecDns,
       "cfprApIppoolBlockSubnet": cfprApIppoolBlockSubnet,
       "cfprApIppoolBlockTo": cfprApIppoolBlockTo,
       "cfprApIppoolIpV6AddrTable": cfprApIppoolIpV6AddrTable,
       "cfprApIppoolIpV6AddrEntry": cfprApIppoolIpV6AddrEntry,
       "cfprApIppoolIpV6AddrInstanceId": cfprApIppoolIpV6AddrInstanceId,
       "cfprApIppoolIpV6AddrDn": cfprApIppoolIpV6AddrDn,
       "cfprApIppoolIpV6AddrRn": cfprApIppoolIpV6AddrRn,
       "cfprApIppoolIpV6AddrAssigned": cfprApIppoolIpV6AddrAssigned,
       "cfprApIppoolIpV6AddrAssignedToDn": cfprApIppoolIpV6AddrAssignedToDn,
       "cfprApIppoolIpV6AddrGlobalAssignedCnt": cfprApIppoolIpV6AddrGlobalAssignedCnt,
       "cfprApIppoolIpV6AddrGlobalDefinedCnt": cfprApIppoolIpV6AddrGlobalDefinedCnt,
       "cfprApIppoolIpV6AddrId": cfprApIppoolIpV6AddrId,
       "cfprApIppoolIpV6AddrOwner": cfprApIppoolIpV6AddrOwner,
       "cfprApIppoolIpV6BlockTable": cfprApIppoolIpV6BlockTable,
       "cfprApIppoolIpV6BlockEntry": cfprApIppoolIpV6BlockEntry,
       "cfprApIppoolIpV6BlockInstanceId": cfprApIppoolIpV6BlockInstanceId,
       "cfprApIppoolIpV6BlockDn": cfprApIppoolIpV6BlockDn,
       "cfprApIppoolIpV6BlockRn": cfprApIppoolIpV6BlockRn,
       "cfprApIppoolIpV6BlockDefGw": cfprApIppoolIpV6BlockDefGw,
       "cfprApIppoolIpV6BlockFrom": cfprApIppoolIpV6BlockFrom,
       "cfprApIppoolIpV6BlockPrefix": cfprApIppoolIpV6BlockPrefix,
       "cfprApIppoolIpV6BlockPrimDns": cfprApIppoolIpV6BlockPrimDns,
       "cfprApIppoolIpV6BlockSecDns": cfprApIppoolIpV6BlockSecDns,
       "cfprApIppoolIpV6BlockTo": cfprApIppoolIpV6BlockTo,
       "cfprApIppoolIpV6PooledTable": cfprApIppoolIpV6PooledTable,
       "cfprApIppoolIpV6PooledEntry": cfprApIppoolIpV6PooledEntry,
       "cfprApIppoolIpV6PooledInstanceId": cfprApIppoolIpV6PooledInstanceId,
       "cfprApIppoolIpV6PooledDn": cfprApIppoolIpV6PooledDn,
       "cfprApIppoolIpV6PooledRn": cfprApIppoolIpV6PooledRn,
       "cfprApIppoolIpV6PooledAssigned": cfprApIppoolIpV6PooledAssigned,
       "cfprApIppoolIpV6PooledAssignedToDn": cfprApIppoolIpV6PooledAssignedToDn,
       "cfprApIppoolIpV6PooledDefGw": cfprApIppoolIpV6PooledDefGw,
       "cfprApIppoolIpV6PooledId": cfprApIppoolIpV6PooledId,
       "cfprApIppoolIpV6PooledPoolableDn": cfprApIppoolIpV6PooledPoolableDn,
       "cfprApIppoolIpV6PooledPrefix": cfprApIppoolIpV6PooledPrefix,
       "cfprApIppoolIpV6PooledPrevAssignedToDn": cfprApIppoolIpV6PooledPrevAssignedToDn,
       "cfprApIppoolIpV6PooledPrimDns": cfprApIppoolIpV6PooledPrimDns,
       "cfprApIppoolIpV6PooledSecDns": cfprApIppoolIpV6PooledSecDns,
       "cfprApIppoolPoolTable": cfprApIppoolPoolTable,
       "cfprApIppoolPoolEntry": cfprApIppoolPoolEntry,
       "cfprApIppoolPoolInstanceId": cfprApIppoolPoolInstanceId,
       "cfprApIppoolPoolDn": cfprApIppoolPoolDn,
       "cfprApIppoolPoolRn": cfprApIppoolPoolRn,
       "cfprApIppoolPoolAssigned": cfprApIppoolPoolAssigned,
       "cfprApIppoolPoolAssignmentOrder": cfprApIppoolPoolAssignmentOrder,
       "cfprApIppoolPoolDescr": cfprApIppoolPoolDescr,
       "cfprApIppoolPoolExtManaged": cfprApIppoolPoolExtManaged,
       "cfprApIppoolPoolGuid": cfprApIppoolPoolGuid,
       "cfprApIppoolPoolIntId": cfprApIppoolPoolIntId,
       "cfprApIppoolPoolIsNetBIOSEnabled": cfprApIppoolPoolIsNetBIOSEnabled,
       "cfprApIppoolPoolName": cfprApIppoolPoolName,
       "cfprApIppoolPoolPolicyLevel": cfprApIppoolPoolPolicyLevel,
       "cfprApIppoolPoolPolicyOwner": cfprApIppoolPoolPolicyOwner,
       "cfprApIppoolPoolSize": cfprApIppoolPoolSize,
       "cfprApIppoolPoolSupportsDHCP": cfprApIppoolPoolSupportsDHCP,
       "cfprApIppoolPoolV4Assigned": cfprApIppoolPoolV4Assigned,
       "cfprApIppoolPoolV4Size": cfprApIppoolPoolV4Size,
       "cfprApIppoolPoolV6Assigned": cfprApIppoolPoolV6Assigned,
       "cfprApIppoolPoolV6Size": cfprApIppoolPoolV6Size,
       "cfprApIppoolPoolableTable": cfprApIppoolPoolableTable,
       "cfprApIppoolPoolableEntry": cfprApIppoolPoolableEntry,
       "cfprApIppoolPoolableInstanceId": cfprApIppoolPoolableInstanceId,
       "cfprApIppoolPoolableDn": cfprApIppoolPoolableDn,
       "cfprApIppoolPoolableRn": cfprApIppoolPoolableRn,
       "cfprApIppoolPoolableId": cfprApIppoolPoolableId,
       "cfprApIppoolPoolablePoolDn": cfprApIppoolPoolablePoolDn,
       "cfprApIppoolPooledTable": cfprApIppoolPooledTable,
       "cfprApIppoolPooledEntry": cfprApIppoolPooledEntry,
       "cfprApIppoolPooledInstanceId": cfprApIppoolPooledInstanceId,
       "cfprApIppoolPooledDn": cfprApIppoolPooledDn,
       "cfprApIppoolPooledRn": cfprApIppoolPooledRn,
       "cfprApIppoolPooledAssigned": cfprApIppoolPooledAssigned,
       "cfprApIppoolPooledAssignedToDn": cfprApIppoolPooledAssignedToDn,
       "cfprApIppoolPooledDefGw": cfprApIppoolPooledDefGw,
       "cfprApIppoolPooledId": cfprApIppoolPooledId,
       "cfprApIppoolPooledPoolableDn": cfprApIppoolPooledPoolableDn,
       "cfprApIppoolPooledPrevAssignedToDn": cfprApIppoolPooledPrevAssignedToDn,
       "cfprApIppoolPooledPrimDns": cfprApIppoolPooledPrimDns,
       "cfprApIppoolPooledSecDns": cfprApIppoolPooledSecDns,
       "cfprApIppoolPooledSubnet": cfprApIppoolPooledSubnet,
       "cfprApIppoolUniverseTable": cfprApIppoolUniverseTable,
       "cfprApIppoolUniverseEntry": cfprApIppoolUniverseEntry,
       "cfprApIppoolUniverseInstanceId": cfprApIppoolUniverseInstanceId,
       "cfprApIppoolUniverseDn": cfprApIppoolUniverseDn,
       "cfprApIppoolUniverseRn": cfprApIppoolUniverseRn}
)
