# SNMP MIB module (CISCO-FIREPOWER-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-IP-MIB.mib
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

(CfprIpIPv4DnsPref,
 CfprIpIpV4StaticAddrPref,
 CfprIpServiceIfPref) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprIpIPv4DnsPref",
    "CfprIpIpV4StaticAddrPref",
    "CfprIpServiceIfPref")

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

cfprIpObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprIpDnsSuffixTable_Object = MibTable
cfprIpDnsSuffixTable = _CfprIpDnsSuffixTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 1)
)
if mibBuilder.loadTexts:
    cfprIpDnsSuffixTable.setStatus("current")
_CfprIpDnsSuffixEntry_Object = MibTableRow
cfprIpDnsSuffixEntry = _CfprIpDnsSuffixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 1, 1)
)
cfprIpDnsSuffixEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IP-MIB", "cfprIpDnsSuffixInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIpDnsSuffixEntry.setStatus("current")
_CfprIpDnsSuffixInstanceId_Type = CfprManagedObjectId
_CfprIpDnsSuffixInstanceId_Object = MibTableColumn
cfprIpDnsSuffixInstanceId = _CfprIpDnsSuffixInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 1, 1, 1),
    _CfprIpDnsSuffixInstanceId_Type()
)
cfprIpDnsSuffixInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIpDnsSuffixInstanceId.setStatus("current")
_CfprIpDnsSuffixDn_Type = CfprManagedObjectDn
_CfprIpDnsSuffixDn_Object = MibTableColumn
cfprIpDnsSuffixDn = _CfprIpDnsSuffixDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 1, 1, 2),
    _CfprIpDnsSuffixDn_Type()
)
cfprIpDnsSuffixDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpDnsSuffixDn.setStatus("current")
_CfprIpDnsSuffixRn_Type = SnmpAdminString
_CfprIpDnsSuffixRn_Object = MibTableColumn
cfprIpDnsSuffixRn = _CfprIpDnsSuffixRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 1, 1, 3),
    _CfprIpDnsSuffixRn_Type()
)
cfprIpDnsSuffixRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpDnsSuffixRn.setStatus("current")
_CfprIpDnsSuffixGuid_Type = SnmpAdminString
_CfprIpDnsSuffixGuid_Object = MibTableColumn
cfprIpDnsSuffixGuid = _CfprIpDnsSuffixGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 1, 1, 4),
    _CfprIpDnsSuffixGuid_Type()
)
cfprIpDnsSuffixGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpDnsSuffixGuid.setStatus("current")
_CfprIpDnsSuffixHost_Type = SnmpAdminString
_CfprIpDnsSuffixHost_Object = MibTableColumn
cfprIpDnsSuffixHost = _CfprIpDnsSuffixHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 1, 1, 5),
    _CfprIpDnsSuffixHost_Type()
)
cfprIpDnsSuffixHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpDnsSuffixHost.setStatus("current")
_CfprIpDnsSuffixName_Type = SnmpAdminString
_CfprIpDnsSuffixName_Object = MibTableColumn
cfprIpDnsSuffixName = _CfprIpDnsSuffixName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 1, 1, 6),
    _CfprIpDnsSuffixName_Type()
)
cfprIpDnsSuffixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpDnsSuffixName.setStatus("current")
_CfprIpIPv4DnsTable_Object = MibTable
cfprIpIPv4DnsTable = _CfprIpIPv4DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 2)
)
if mibBuilder.loadTexts:
    cfprIpIPv4DnsTable.setStatus("current")
_CfprIpIPv4DnsEntry_Object = MibTableRow
cfprIpIPv4DnsEntry = _CfprIpIPv4DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 2, 1)
)
cfprIpIPv4DnsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IP-MIB", "cfprIpIPv4DnsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIpIPv4DnsEntry.setStatus("current")
_CfprIpIPv4DnsInstanceId_Type = CfprManagedObjectId
_CfprIpIPv4DnsInstanceId_Object = MibTableColumn
cfprIpIPv4DnsInstanceId = _CfprIpIPv4DnsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 2, 1, 1),
    _CfprIpIPv4DnsInstanceId_Type()
)
cfprIpIPv4DnsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIpIPv4DnsInstanceId.setStatus("current")
_CfprIpIPv4DnsDn_Type = CfprManagedObjectDn
_CfprIpIPv4DnsDn_Object = MibTableColumn
cfprIpIPv4DnsDn = _CfprIpIPv4DnsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 2, 1, 2),
    _CfprIpIPv4DnsDn_Type()
)
cfprIpIPv4DnsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIPv4DnsDn.setStatus("current")
_CfprIpIPv4DnsRn_Type = SnmpAdminString
_CfprIpIPv4DnsRn_Object = MibTableColumn
cfprIpIPv4DnsRn = _CfprIpIPv4DnsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 2, 1, 3),
    _CfprIpIPv4DnsRn_Type()
)
cfprIpIPv4DnsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIPv4DnsRn.setStatus("current")
_CfprIpIPv4DnsAddr_Type = InetAddressIPv4
_CfprIpIPv4DnsAddr_Object = MibTableColumn
cfprIpIPv4DnsAddr = _CfprIpIPv4DnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 2, 1, 4),
    _CfprIpIPv4DnsAddr_Type()
)
cfprIpIPv4DnsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIPv4DnsAddr.setStatus("current")
_CfprIpIPv4DnsDefGw_Type = InetAddressIPv4
_CfprIpIPv4DnsDefGw_Object = MibTableColumn
cfprIpIPv4DnsDefGw = _CfprIpIPv4DnsDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 2, 1, 5),
    _CfprIpIPv4DnsDefGw_Type()
)
cfprIpIPv4DnsDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIPv4DnsDefGw.setStatus("current")
_CfprIpIPv4DnsPref_Type = CfprIpIPv4DnsPref
_CfprIpIPv4DnsPref_Object = MibTableColumn
cfprIpIPv4DnsPref = _CfprIpIPv4DnsPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 2, 1, 6),
    _CfprIpIPv4DnsPref_Type()
)
cfprIpIPv4DnsPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIPv4DnsPref.setStatus("current")
_CfprIpIPv4DnsSubnet_Type = InetAddressIPv4
_CfprIpIPv4DnsSubnet_Object = MibTableColumn
cfprIpIPv4DnsSubnet = _CfprIpIPv4DnsSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 2, 1, 7),
    _CfprIpIPv4DnsSubnet_Type()
)
cfprIpIPv4DnsSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIPv4DnsSubnet.setStatus("current")
_CfprIpIPv4WinsServerTable_Object = MibTable
cfprIpIPv4WinsServerTable = _CfprIpIPv4WinsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 3)
)
if mibBuilder.loadTexts:
    cfprIpIPv4WinsServerTable.setStatus("current")
_CfprIpIPv4WinsServerEntry_Object = MibTableRow
cfprIpIPv4WinsServerEntry = _CfprIpIPv4WinsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 3, 1)
)
cfprIpIPv4WinsServerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IP-MIB", "cfprIpIPv4WinsServerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIpIPv4WinsServerEntry.setStatus("current")
_CfprIpIPv4WinsServerInstanceId_Type = CfprManagedObjectId
_CfprIpIPv4WinsServerInstanceId_Object = MibTableColumn
cfprIpIPv4WinsServerInstanceId = _CfprIpIPv4WinsServerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 3, 1, 1),
    _CfprIpIPv4WinsServerInstanceId_Type()
)
cfprIpIPv4WinsServerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIpIPv4WinsServerInstanceId.setStatus("current")
_CfprIpIPv4WinsServerDn_Type = CfprManagedObjectDn
_CfprIpIPv4WinsServerDn_Object = MibTableColumn
cfprIpIPv4WinsServerDn = _CfprIpIPv4WinsServerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 3, 1, 2),
    _CfprIpIPv4WinsServerDn_Type()
)
cfprIpIPv4WinsServerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIPv4WinsServerDn.setStatus("current")
_CfprIpIPv4WinsServerRn_Type = SnmpAdminString
_CfprIpIPv4WinsServerRn_Object = MibTableColumn
cfprIpIPv4WinsServerRn = _CfprIpIPv4WinsServerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 3, 1, 3),
    _CfprIpIPv4WinsServerRn_Type()
)
cfprIpIPv4WinsServerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIPv4WinsServerRn.setStatus("current")
_CfprIpIPv4WinsServerIPv4Address_Type = InetAddressIPv4
_CfprIpIPv4WinsServerIPv4Address_Object = MibTableColumn
cfprIpIPv4WinsServerIPv4Address = _CfprIpIPv4WinsServerIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 3, 1, 4),
    _CfprIpIPv4WinsServerIPv4Address_Type()
)
cfprIpIPv4WinsServerIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIPv4WinsServerIPv4Address.setStatus("current")
_CfprIpIPv4WinsServerGuid_Type = SnmpAdminString
_CfprIpIPv4WinsServerGuid_Object = MibTableColumn
cfprIpIPv4WinsServerGuid = _CfprIpIPv4WinsServerGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 3, 1, 5),
    _CfprIpIPv4WinsServerGuid_Type()
)
cfprIpIPv4WinsServerGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIPv4WinsServerGuid.setStatus("current")
_CfprIpIPv4WinsServerHost_Type = SnmpAdminString
_CfprIpIPv4WinsServerHost_Object = MibTableColumn
cfprIpIPv4WinsServerHost = _CfprIpIPv4WinsServerHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 3, 1, 6),
    _CfprIpIPv4WinsServerHost_Type()
)
cfprIpIPv4WinsServerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIPv4WinsServerHost.setStatus("current")
_CfprIpIPv4WinsServerName_Type = SnmpAdminString
_CfprIpIPv4WinsServerName_Object = MibTableColumn
cfprIpIPv4WinsServerName = _CfprIpIPv4WinsServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 3, 1, 7),
    _CfprIpIPv4WinsServerName_Type()
)
cfprIpIPv4WinsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIPv4WinsServerName.setStatus("current")
_CfprIpIpV4StaticAddrTable_Object = MibTable
cfprIpIpV4StaticAddrTable = _CfprIpIpV4StaticAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 4)
)
if mibBuilder.loadTexts:
    cfprIpIpV4StaticAddrTable.setStatus("current")
_CfprIpIpV4StaticAddrEntry_Object = MibTableRow
cfprIpIpV4StaticAddrEntry = _CfprIpIpV4StaticAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 4, 1)
)
cfprIpIpV4StaticAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IP-MIB", "cfprIpIpV4StaticAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIpIpV4StaticAddrEntry.setStatus("current")
_CfprIpIpV4StaticAddrInstanceId_Type = CfprManagedObjectId
_CfprIpIpV4StaticAddrInstanceId_Object = MibTableColumn
cfprIpIpV4StaticAddrInstanceId = _CfprIpIpV4StaticAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 4, 1, 1),
    _CfprIpIpV4StaticAddrInstanceId_Type()
)
cfprIpIpV4StaticAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIpIpV4StaticAddrInstanceId.setStatus("current")
_CfprIpIpV4StaticAddrDn_Type = CfprManagedObjectDn
_CfprIpIpV4StaticAddrDn_Object = MibTableColumn
cfprIpIpV4StaticAddrDn = _CfprIpIpV4StaticAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 4, 1, 2),
    _CfprIpIpV4StaticAddrDn_Type()
)
cfprIpIpV4StaticAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIpV4StaticAddrDn.setStatus("current")
_CfprIpIpV4StaticAddrRn_Type = SnmpAdminString
_CfprIpIpV4StaticAddrRn_Object = MibTableColumn
cfprIpIpV4StaticAddrRn = _CfprIpIpV4StaticAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 4, 1, 3),
    _CfprIpIpV4StaticAddrRn_Type()
)
cfprIpIpV4StaticAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIpV4StaticAddrRn.setStatus("current")
_CfprIpIpV4StaticAddrAddr_Type = InetAddressIPv4
_CfprIpIpV4StaticAddrAddr_Object = MibTableColumn
cfprIpIpV4StaticAddrAddr = _CfprIpIpV4StaticAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 4, 1, 4),
    _CfprIpIpV4StaticAddrAddr_Type()
)
cfprIpIpV4StaticAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIpV4StaticAddrAddr.setStatus("current")
_CfprIpIpV4StaticAddrDefGw_Type = InetAddressIPv4
_CfprIpIpV4StaticAddrDefGw_Object = MibTableColumn
cfprIpIpV4StaticAddrDefGw = _CfprIpIpV4StaticAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 4, 1, 5),
    _CfprIpIpV4StaticAddrDefGw_Type()
)
cfprIpIpV4StaticAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIpV4StaticAddrDefGw.setStatus("current")
_CfprIpIpV4StaticAddrPref_Type = CfprIpIpV4StaticAddrPref
_CfprIpIpV4StaticAddrPref_Object = MibTableColumn
cfprIpIpV4StaticAddrPref = _CfprIpIpV4StaticAddrPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 4, 1, 6),
    _CfprIpIpV4StaticAddrPref_Type()
)
cfprIpIpV4StaticAddrPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIpV4StaticAddrPref.setStatus("current")
_CfprIpIpV4StaticAddrSubnet_Type = InetAddressIPv4
_CfprIpIpV4StaticAddrSubnet_Object = MibTableColumn
cfprIpIpV4StaticAddrSubnet = _CfprIpIpV4StaticAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 4, 1, 7),
    _CfprIpIpV4StaticAddrSubnet_Type()
)
cfprIpIpV4StaticAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpIpV4StaticAddrSubnet.setStatus("current")
_CfprIpServiceIfTable_Object = MibTable
cfprIpServiceIfTable = _CfprIpServiceIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 6)
)
if mibBuilder.loadTexts:
    cfprIpServiceIfTable.setStatus("current")
_CfprIpServiceIfEntry_Object = MibTableRow
cfprIpServiceIfEntry = _CfprIpServiceIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 6, 1)
)
cfprIpServiceIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IP-MIB", "cfprIpServiceIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprIpServiceIfEntry.setStatus("current")
_CfprIpServiceIfInstanceId_Type = CfprManagedObjectId
_CfprIpServiceIfInstanceId_Object = MibTableColumn
cfprIpServiceIfInstanceId = _CfprIpServiceIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 6, 1, 1),
    _CfprIpServiceIfInstanceId_Type()
)
cfprIpServiceIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprIpServiceIfInstanceId.setStatus("current")
_CfprIpServiceIfDn_Type = CfprManagedObjectDn
_CfprIpServiceIfDn_Object = MibTableColumn
cfprIpServiceIfDn = _CfprIpServiceIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 6, 1, 2),
    _CfprIpServiceIfDn_Type()
)
cfprIpServiceIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpServiceIfDn.setStatus("current")
_CfprIpServiceIfRn_Type = SnmpAdminString
_CfprIpServiceIfRn_Object = MibTableColumn
cfprIpServiceIfRn = _CfprIpServiceIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 6, 1, 3),
    _CfprIpServiceIfRn_Type()
)
cfprIpServiceIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpServiceIfRn.setStatus("current")
_CfprIpServiceIfAddr_Type = InetAddressIPv4
_CfprIpServiceIfAddr_Object = MibTableColumn
cfprIpServiceIfAddr = _CfprIpServiceIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 6, 1, 4),
    _CfprIpServiceIfAddr_Type()
)
cfprIpServiceIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpServiceIfAddr.setStatus("current")
_CfprIpServiceIfDefGw_Type = InetAddressIPv4
_CfprIpServiceIfDefGw_Object = MibTableColumn
cfprIpServiceIfDefGw = _CfprIpServiceIfDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 6, 1, 5),
    _CfprIpServiceIfDefGw_Type()
)
cfprIpServiceIfDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpServiceIfDefGw.setStatus("current")
_CfprIpServiceIfPort_Type = Gauge32
_CfprIpServiceIfPort_Object = MibTableColumn
cfprIpServiceIfPort = _CfprIpServiceIfPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 6, 1, 6),
    _CfprIpServiceIfPort_Type()
)
cfprIpServiceIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpServiceIfPort.setStatus("current")
_CfprIpServiceIfPref_Type = CfprIpServiceIfPref
_CfprIpServiceIfPref_Object = MibTableColumn
cfprIpServiceIfPref = _CfprIpServiceIfPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 6, 1, 7),
    _CfprIpServiceIfPref_Type()
)
cfprIpServiceIfPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpServiceIfPref.setStatus("current")
_CfprIpServiceIfSubnet_Type = InetAddressIPv4
_CfprIpServiceIfSubnet_Object = MibTableColumn
cfprIpServiceIfSubnet = _CfprIpServiceIfSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 40, 6, 1, 8),
    _CfprIpServiceIfSubnet_Type()
)
cfprIpServiceIfSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprIpServiceIfSubnet.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-IP-MIB",
    **{"cfprIpObjects": cfprIpObjects,
       "cfprIpDnsSuffixTable": cfprIpDnsSuffixTable,
       "cfprIpDnsSuffixEntry": cfprIpDnsSuffixEntry,
       "cfprIpDnsSuffixInstanceId": cfprIpDnsSuffixInstanceId,
       "cfprIpDnsSuffixDn": cfprIpDnsSuffixDn,
       "cfprIpDnsSuffixRn": cfprIpDnsSuffixRn,
       "cfprIpDnsSuffixGuid": cfprIpDnsSuffixGuid,
       "cfprIpDnsSuffixHost": cfprIpDnsSuffixHost,
       "cfprIpDnsSuffixName": cfprIpDnsSuffixName,
       "cfprIpIPv4DnsTable": cfprIpIPv4DnsTable,
       "cfprIpIPv4DnsEntry": cfprIpIPv4DnsEntry,
       "cfprIpIPv4DnsInstanceId": cfprIpIPv4DnsInstanceId,
       "cfprIpIPv4DnsDn": cfprIpIPv4DnsDn,
       "cfprIpIPv4DnsRn": cfprIpIPv4DnsRn,
       "cfprIpIPv4DnsAddr": cfprIpIPv4DnsAddr,
       "cfprIpIPv4DnsDefGw": cfprIpIPv4DnsDefGw,
       "cfprIpIPv4DnsPref": cfprIpIPv4DnsPref,
       "cfprIpIPv4DnsSubnet": cfprIpIPv4DnsSubnet,
       "cfprIpIPv4WinsServerTable": cfprIpIPv4WinsServerTable,
       "cfprIpIPv4WinsServerEntry": cfprIpIPv4WinsServerEntry,
       "cfprIpIPv4WinsServerInstanceId": cfprIpIPv4WinsServerInstanceId,
       "cfprIpIPv4WinsServerDn": cfprIpIPv4WinsServerDn,
       "cfprIpIPv4WinsServerRn": cfprIpIPv4WinsServerRn,
       "cfprIpIPv4WinsServerIPv4Address": cfprIpIPv4WinsServerIPv4Address,
       "cfprIpIPv4WinsServerGuid": cfprIpIPv4WinsServerGuid,
       "cfprIpIPv4WinsServerHost": cfprIpIPv4WinsServerHost,
       "cfprIpIPv4WinsServerName": cfprIpIPv4WinsServerName,
       "cfprIpIpV4StaticAddrTable": cfprIpIpV4StaticAddrTable,
       "cfprIpIpV4StaticAddrEntry": cfprIpIpV4StaticAddrEntry,
       "cfprIpIpV4StaticAddrInstanceId": cfprIpIpV4StaticAddrInstanceId,
       "cfprIpIpV4StaticAddrDn": cfprIpIpV4StaticAddrDn,
       "cfprIpIpV4StaticAddrRn": cfprIpIpV4StaticAddrRn,
       "cfprIpIpV4StaticAddrAddr": cfprIpIpV4StaticAddrAddr,
       "cfprIpIpV4StaticAddrDefGw": cfprIpIpV4StaticAddrDefGw,
       "cfprIpIpV4StaticAddrPref": cfprIpIpV4StaticAddrPref,
       "cfprIpIpV4StaticAddrSubnet": cfprIpIpV4StaticAddrSubnet,
       "cfprIpServiceIfTable": cfprIpServiceIfTable,
       "cfprIpServiceIfEntry": cfprIpServiceIfEntry,
       "cfprIpServiceIfInstanceId": cfprIpServiceIfInstanceId,
       "cfprIpServiceIfDn": cfprIpServiceIfDn,
       "cfprIpServiceIfRn": cfprIpServiceIfRn,
       "cfprIpServiceIfAddr": cfprIpServiceIfAddr,
       "cfprIpServiceIfDefGw": cfprIpServiceIfDefGw,
       "cfprIpServiceIfPort": cfprIpServiceIfPort,
       "cfprIpServiceIfPref": cfprIpServiceIfPref,
       "cfprIpServiceIfSubnet": cfprIpServiceIfSubnet}
)
