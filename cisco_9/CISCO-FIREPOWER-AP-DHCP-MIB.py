# SNMP MIB module (CISCO-FIREPOWER-AP-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-DHCP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:14 2025
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

cfprApDhcpObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApDhcpAcquiredTable_Object = MibTable
cfprApDhcpAcquiredTable = _CfprApDhcpAcquiredTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 1)
)
if mibBuilder.loadTexts:
    cfprApDhcpAcquiredTable.setStatus("current")
_CfprApDhcpAcquiredEntry_Object = MibTableRow
cfprApDhcpAcquiredEntry = _CfprApDhcpAcquiredEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 1, 1)
)
cfprApDhcpAcquiredEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DHCP-MIB", "cfprApDhcpAcquiredInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDhcpAcquiredEntry.setStatus("current")
_CfprApDhcpAcquiredInstanceId_Type = CfprApManagedObjectId
_CfprApDhcpAcquiredInstanceId_Object = MibTableColumn
cfprApDhcpAcquiredInstanceId = _CfprApDhcpAcquiredInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 1, 1, 1),
    _CfprApDhcpAcquiredInstanceId_Type()
)
cfprApDhcpAcquiredInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDhcpAcquiredInstanceId.setStatus("current")
_CfprApDhcpAcquiredDn_Type = CfprApManagedObjectDn
_CfprApDhcpAcquiredDn_Object = MibTableColumn
cfprApDhcpAcquiredDn = _CfprApDhcpAcquiredDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 1, 1, 2),
    _CfprApDhcpAcquiredDn_Type()
)
cfprApDhcpAcquiredDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpAcquiredDn.setStatus("current")
_CfprApDhcpAcquiredRn_Type = SnmpAdminString
_CfprApDhcpAcquiredRn_Object = MibTableColumn
cfprApDhcpAcquiredRn = _CfprApDhcpAcquiredRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 1, 1, 3),
    _CfprApDhcpAcquiredRn_Type()
)
cfprApDhcpAcquiredRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpAcquiredRn.setStatus("current")
_CfprApDhcpAcquiredAcqts_Type = DateAndTime
_CfprApDhcpAcquiredAcqts_Object = MibTableColumn
cfprApDhcpAcquiredAcqts = _CfprApDhcpAcquiredAcqts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 1, 1, 4),
    _CfprApDhcpAcquiredAcqts_Type()
)
cfprApDhcpAcquiredAcqts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpAcquiredAcqts.setStatus("current")
_CfprApDhcpAcquiredCookie_Type = SnmpAdminString
_CfprApDhcpAcquiredCookie_Object = MibTableColumn
cfprApDhcpAcquiredCookie = _CfprApDhcpAcquiredCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 1, 1, 5),
    _CfprApDhcpAcquiredCookie_Type()
)
cfprApDhcpAcquiredCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpAcquiredCookie.setStatus("current")
_CfprApDhcpAcquiredEnds_Type = DateAndTime
_CfprApDhcpAcquiredEnds_Object = MibTableColumn
cfprApDhcpAcquiredEnds = _CfprApDhcpAcquiredEnds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 1, 1, 6),
    _CfprApDhcpAcquiredEnds_Type()
)
cfprApDhcpAcquiredEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpAcquiredEnds.setStatus("current")
_CfprApDhcpAcquiredIp_Type = InetAddressIPv4
_CfprApDhcpAcquiredIp_Object = MibTableColumn
cfprApDhcpAcquiredIp = _CfprApDhcpAcquiredIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 1, 1, 7),
    _CfprApDhcpAcquiredIp_Type()
)
cfprApDhcpAcquiredIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpAcquiredIp.setStatus("current")
_CfprApDhcpAcquiredMac_Type = MacAddress
_CfprApDhcpAcquiredMac_Object = MibTableColumn
cfprApDhcpAcquiredMac = _CfprApDhcpAcquiredMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 1, 1, 8),
    _CfprApDhcpAcquiredMac_Type()
)
cfprApDhcpAcquiredMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpAcquiredMac.setStatus("current")
_CfprApDhcpAcquiredSysId_Type = SnmpAdminString
_CfprApDhcpAcquiredSysId_Object = MibTableColumn
cfprApDhcpAcquiredSysId = _CfprApDhcpAcquiredSysId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 1, 1, 9),
    _CfprApDhcpAcquiredSysId_Type()
)
cfprApDhcpAcquiredSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpAcquiredSysId.setStatus("current")
_CfprApDhcpInstTable_Object = MibTable
cfprApDhcpInstTable = _CfprApDhcpInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 2)
)
if mibBuilder.loadTexts:
    cfprApDhcpInstTable.setStatus("current")
_CfprApDhcpInstEntry_Object = MibTableRow
cfprApDhcpInstEntry = _CfprApDhcpInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 2, 1)
)
cfprApDhcpInstEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DHCP-MIB", "cfprApDhcpInstInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDhcpInstEntry.setStatus("current")
_CfprApDhcpInstInstanceId_Type = CfprApManagedObjectId
_CfprApDhcpInstInstanceId_Object = MibTableColumn
cfprApDhcpInstInstanceId = _CfprApDhcpInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 2, 1, 1),
    _CfprApDhcpInstInstanceId_Type()
)
cfprApDhcpInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDhcpInstInstanceId.setStatus("current")
_CfprApDhcpInstDn_Type = CfprApManagedObjectDn
_CfprApDhcpInstDn_Object = MibTableColumn
cfprApDhcpInstDn = _CfprApDhcpInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 2, 1, 2),
    _CfprApDhcpInstDn_Type()
)
cfprApDhcpInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpInstDn.setStatus("current")
_CfprApDhcpInstRn_Type = SnmpAdminString
_CfprApDhcpInstRn_Object = MibTableColumn
cfprApDhcpInstRn = _CfprApDhcpInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 2, 1, 3),
    _CfprApDhcpInstRn_Type()
)
cfprApDhcpInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpInstRn.setStatus("current")
_CfprApDhcpLeaseTable_Object = MibTable
cfprApDhcpLeaseTable = _CfprApDhcpLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3)
)
if mibBuilder.loadTexts:
    cfprApDhcpLeaseTable.setStatus("current")
_CfprApDhcpLeaseEntry_Object = MibTableRow
cfprApDhcpLeaseEntry = _CfprApDhcpLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3, 1)
)
cfprApDhcpLeaseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DHCP-MIB", "cfprApDhcpLeaseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDhcpLeaseEntry.setStatus("current")
_CfprApDhcpLeaseInstanceId_Type = CfprApManagedObjectId
_CfprApDhcpLeaseInstanceId_Object = MibTableColumn
cfprApDhcpLeaseInstanceId = _CfprApDhcpLeaseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3, 1, 1),
    _CfprApDhcpLeaseInstanceId_Type()
)
cfprApDhcpLeaseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDhcpLeaseInstanceId.setStatus("current")
_CfprApDhcpLeaseDn_Type = CfprApManagedObjectDn
_CfprApDhcpLeaseDn_Object = MibTableColumn
cfprApDhcpLeaseDn = _CfprApDhcpLeaseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3, 1, 2),
    _CfprApDhcpLeaseDn_Type()
)
cfprApDhcpLeaseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpLeaseDn.setStatus("current")
_CfprApDhcpLeaseRn_Type = SnmpAdminString
_CfprApDhcpLeaseRn_Object = MibTableColumn
cfprApDhcpLeaseRn = _CfprApDhcpLeaseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3, 1, 3),
    _CfprApDhcpLeaseRn_Type()
)
cfprApDhcpLeaseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpLeaseRn.setStatus("current")
_CfprApDhcpLeaseCliId_Type = SnmpAdminString
_CfprApDhcpLeaseCliId_Object = MibTableColumn
cfprApDhcpLeaseCliId = _CfprApDhcpLeaseCliId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3, 1, 4),
    _CfprApDhcpLeaseCliId_Type()
)
cfprApDhcpLeaseCliId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpLeaseCliId.setStatus("current")
_CfprApDhcpLeaseCookie_Type = SnmpAdminString
_CfprApDhcpLeaseCookie_Object = MibTableColumn
cfprApDhcpLeaseCookie = _CfprApDhcpLeaseCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3, 1, 5),
    _CfprApDhcpLeaseCookie_Type()
)
cfprApDhcpLeaseCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpLeaseCookie.setStatus("current")
_CfprApDhcpLeaseEnds_Type = DateAndTime
_CfprApDhcpLeaseEnds_Object = MibTableColumn
cfprApDhcpLeaseEnds = _CfprApDhcpLeaseEnds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3, 1, 6),
    _CfprApDhcpLeaseEnds_Type()
)
cfprApDhcpLeaseEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpLeaseEnds.setStatus("current")
_CfprApDhcpLeaseHostname_Type = SnmpAdminString
_CfprApDhcpLeaseHostname_Object = MibTableColumn
cfprApDhcpLeaseHostname = _CfprApDhcpLeaseHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3, 1, 7),
    _CfprApDhcpLeaseHostname_Type()
)
cfprApDhcpLeaseHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpLeaseHostname.setStatus("current")
_CfprApDhcpLeaseIntf_Type = SnmpAdminString
_CfprApDhcpLeaseIntf_Object = MibTableColumn
cfprApDhcpLeaseIntf = _CfprApDhcpLeaseIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3, 1, 8),
    _CfprApDhcpLeaseIntf_Type()
)
cfprApDhcpLeaseIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpLeaseIntf.setStatus("current")
_CfprApDhcpLeaseIp_Type = InetAddressIPv4
_CfprApDhcpLeaseIp_Object = MibTableColumn
cfprApDhcpLeaseIp = _CfprApDhcpLeaseIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3, 1, 9),
    _CfprApDhcpLeaseIp_Type()
)
cfprApDhcpLeaseIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpLeaseIp.setStatus("current")
_CfprApDhcpLeaseMac_Type = MacAddress
_CfprApDhcpLeaseMac_Object = MibTableColumn
cfprApDhcpLeaseMac = _CfprApDhcpLeaseMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3, 1, 10),
    _CfprApDhcpLeaseMac_Type()
)
cfprApDhcpLeaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpLeaseMac.setStatus("current")
_CfprApDhcpLeaseStarts_Type = DateAndTime
_CfprApDhcpLeaseStarts_Object = MibTableColumn
cfprApDhcpLeaseStarts = _CfprApDhcpLeaseStarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 15, 3, 1, 11),
    _CfprApDhcpLeaseStarts_Type()
)
cfprApDhcpLeaseStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDhcpLeaseStarts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-DHCP-MIB",
    **{"cfprApDhcpObjects": cfprApDhcpObjects,
       "cfprApDhcpAcquiredTable": cfprApDhcpAcquiredTable,
       "cfprApDhcpAcquiredEntry": cfprApDhcpAcquiredEntry,
       "cfprApDhcpAcquiredInstanceId": cfprApDhcpAcquiredInstanceId,
       "cfprApDhcpAcquiredDn": cfprApDhcpAcquiredDn,
       "cfprApDhcpAcquiredRn": cfprApDhcpAcquiredRn,
       "cfprApDhcpAcquiredAcqts": cfprApDhcpAcquiredAcqts,
       "cfprApDhcpAcquiredCookie": cfprApDhcpAcquiredCookie,
       "cfprApDhcpAcquiredEnds": cfprApDhcpAcquiredEnds,
       "cfprApDhcpAcquiredIp": cfprApDhcpAcquiredIp,
       "cfprApDhcpAcquiredMac": cfprApDhcpAcquiredMac,
       "cfprApDhcpAcquiredSysId": cfprApDhcpAcquiredSysId,
       "cfprApDhcpInstTable": cfprApDhcpInstTable,
       "cfprApDhcpInstEntry": cfprApDhcpInstEntry,
       "cfprApDhcpInstInstanceId": cfprApDhcpInstInstanceId,
       "cfprApDhcpInstDn": cfprApDhcpInstDn,
       "cfprApDhcpInstRn": cfprApDhcpInstRn,
       "cfprApDhcpLeaseTable": cfprApDhcpLeaseTable,
       "cfprApDhcpLeaseEntry": cfprApDhcpLeaseEntry,
       "cfprApDhcpLeaseInstanceId": cfprApDhcpLeaseInstanceId,
       "cfprApDhcpLeaseDn": cfprApDhcpLeaseDn,
       "cfprApDhcpLeaseRn": cfprApDhcpLeaseRn,
       "cfprApDhcpLeaseCliId": cfprApDhcpLeaseCliId,
       "cfprApDhcpLeaseCookie": cfprApDhcpLeaseCookie,
       "cfprApDhcpLeaseEnds": cfprApDhcpLeaseEnds,
       "cfprApDhcpLeaseHostname": cfprApDhcpLeaseHostname,
       "cfprApDhcpLeaseIntf": cfprApDhcpLeaseIntf,
       "cfprApDhcpLeaseIp": cfprApDhcpLeaseIp,
       "cfprApDhcpLeaseMac": cfprApDhcpLeaseMac,
       "cfprApDhcpLeaseStarts": cfprApDhcpLeaseStarts}
)
