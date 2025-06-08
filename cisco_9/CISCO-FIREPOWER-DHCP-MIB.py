# SNMP MIB module (CISCO-FIREPOWER-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-DHCP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:10 2025
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

cfprDhcpObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprDhcpAcquiredTable_Object = MibTable
cfprDhcpAcquiredTable = _CfprDhcpAcquiredTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 1)
)
if mibBuilder.loadTexts:
    cfprDhcpAcquiredTable.setStatus("current")
_CfprDhcpAcquiredEntry_Object = MibTableRow
cfprDhcpAcquiredEntry = _CfprDhcpAcquiredEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 1, 1)
)
cfprDhcpAcquiredEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DHCP-MIB", "cfprDhcpAcquiredInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDhcpAcquiredEntry.setStatus("current")
_CfprDhcpAcquiredInstanceId_Type = CfprManagedObjectId
_CfprDhcpAcquiredInstanceId_Object = MibTableColumn
cfprDhcpAcquiredInstanceId = _CfprDhcpAcquiredInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 1, 1, 1),
    _CfprDhcpAcquiredInstanceId_Type()
)
cfprDhcpAcquiredInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDhcpAcquiredInstanceId.setStatus("current")
_CfprDhcpAcquiredDn_Type = CfprManagedObjectDn
_CfprDhcpAcquiredDn_Object = MibTableColumn
cfprDhcpAcquiredDn = _CfprDhcpAcquiredDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 1, 1, 2),
    _CfprDhcpAcquiredDn_Type()
)
cfprDhcpAcquiredDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpAcquiredDn.setStatus("current")
_CfprDhcpAcquiredRn_Type = SnmpAdminString
_CfprDhcpAcquiredRn_Object = MibTableColumn
cfprDhcpAcquiredRn = _CfprDhcpAcquiredRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 1, 1, 3),
    _CfprDhcpAcquiredRn_Type()
)
cfprDhcpAcquiredRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpAcquiredRn.setStatus("current")
_CfprDhcpAcquiredAcqts_Type = DateAndTime
_CfprDhcpAcquiredAcqts_Object = MibTableColumn
cfprDhcpAcquiredAcqts = _CfprDhcpAcquiredAcqts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 1, 1, 4),
    _CfprDhcpAcquiredAcqts_Type()
)
cfprDhcpAcquiredAcqts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpAcquiredAcqts.setStatus("current")
_CfprDhcpAcquiredCookie_Type = SnmpAdminString
_CfprDhcpAcquiredCookie_Object = MibTableColumn
cfprDhcpAcquiredCookie = _CfprDhcpAcquiredCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 1, 1, 5),
    _CfprDhcpAcquiredCookie_Type()
)
cfprDhcpAcquiredCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpAcquiredCookie.setStatus("current")
_CfprDhcpAcquiredEnds_Type = DateAndTime
_CfprDhcpAcquiredEnds_Object = MibTableColumn
cfprDhcpAcquiredEnds = _CfprDhcpAcquiredEnds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 1, 1, 6),
    _CfprDhcpAcquiredEnds_Type()
)
cfprDhcpAcquiredEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpAcquiredEnds.setStatus("current")
_CfprDhcpAcquiredIp_Type = InetAddressIPv4
_CfprDhcpAcquiredIp_Object = MibTableColumn
cfprDhcpAcquiredIp = _CfprDhcpAcquiredIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 1, 1, 7),
    _CfprDhcpAcquiredIp_Type()
)
cfprDhcpAcquiredIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpAcquiredIp.setStatus("current")
_CfprDhcpAcquiredMac_Type = MacAddress
_CfprDhcpAcquiredMac_Object = MibTableColumn
cfprDhcpAcquiredMac = _CfprDhcpAcquiredMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 1, 1, 8),
    _CfprDhcpAcquiredMac_Type()
)
cfprDhcpAcquiredMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpAcquiredMac.setStatus("current")
_CfprDhcpAcquiredSysId_Type = SnmpAdminString
_CfprDhcpAcquiredSysId_Object = MibTableColumn
cfprDhcpAcquiredSysId = _CfprDhcpAcquiredSysId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 1, 1, 9),
    _CfprDhcpAcquiredSysId_Type()
)
cfprDhcpAcquiredSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpAcquiredSysId.setStatus("current")
_CfprDhcpInstTable_Object = MibTable
cfprDhcpInstTable = _CfprDhcpInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 2)
)
if mibBuilder.loadTexts:
    cfprDhcpInstTable.setStatus("current")
_CfprDhcpInstEntry_Object = MibTableRow
cfprDhcpInstEntry = _CfprDhcpInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 2, 1)
)
cfprDhcpInstEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DHCP-MIB", "cfprDhcpInstInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDhcpInstEntry.setStatus("current")
_CfprDhcpInstInstanceId_Type = CfprManagedObjectId
_CfprDhcpInstInstanceId_Object = MibTableColumn
cfprDhcpInstInstanceId = _CfprDhcpInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 2, 1, 1),
    _CfprDhcpInstInstanceId_Type()
)
cfprDhcpInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDhcpInstInstanceId.setStatus("current")
_CfprDhcpInstDn_Type = CfprManagedObjectDn
_CfprDhcpInstDn_Object = MibTableColumn
cfprDhcpInstDn = _CfprDhcpInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 2, 1, 2),
    _CfprDhcpInstDn_Type()
)
cfprDhcpInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpInstDn.setStatus("current")
_CfprDhcpInstRn_Type = SnmpAdminString
_CfprDhcpInstRn_Object = MibTableColumn
cfprDhcpInstRn = _CfprDhcpInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 2, 1, 3),
    _CfprDhcpInstRn_Type()
)
cfprDhcpInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpInstRn.setStatus("current")
_CfprDhcpLeaseTable_Object = MibTable
cfprDhcpLeaseTable = _CfprDhcpLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3)
)
if mibBuilder.loadTexts:
    cfprDhcpLeaseTable.setStatus("current")
_CfprDhcpLeaseEntry_Object = MibTableRow
cfprDhcpLeaseEntry = _CfprDhcpLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3, 1)
)
cfprDhcpLeaseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DHCP-MIB", "cfprDhcpLeaseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDhcpLeaseEntry.setStatus("current")
_CfprDhcpLeaseInstanceId_Type = CfprManagedObjectId
_CfprDhcpLeaseInstanceId_Object = MibTableColumn
cfprDhcpLeaseInstanceId = _CfprDhcpLeaseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3, 1, 1),
    _CfprDhcpLeaseInstanceId_Type()
)
cfprDhcpLeaseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDhcpLeaseInstanceId.setStatus("current")
_CfprDhcpLeaseDn_Type = CfprManagedObjectDn
_CfprDhcpLeaseDn_Object = MibTableColumn
cfprDhcpLeaseDn = _CfprDhcpLeaseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3, 1, 2),
    _CfprDhcpLeaseDn_Type()
)
cfprDhcpLeaseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpLeaseDn.setStatus("current")
_CfprDhcpLeaseRn_Type = SnmpAdminString
_CfprDhcpLeaseRn_Object = MibTableColumn
cfprDhcpLeaseRn = _CfprDhcpLeaseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3, 1, 3),
    _CfprDhcpLeaseRn_Type()
)
cfprDhcpLeaseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpLeaseRn.setStatus("current")
_CfprDhcpLeaseCliId_Type = SnmpAdminString
_CfprDhcpLeaseCliId_Object = MibTableColumn
cfprDhcpLeaseCliId = _CfprDhcpLeaseCliId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3, 1, 4),
    _CfprDhcpLeaseCliId_Type()
)
cfprDhcpLeaseCliId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpLeaseCliId.setStatus("current")
_CfprDhcpLeaseCookie_Type = SnmpAdminString
_CfprDhcpLeaseCookie_Object = MibTableColumn
cfprDhcpLeaseCookie = _CfprDhcpLeaseCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3, 1, 5),
    _CfprDhcpLeaseCookie_Type()
)
cfprDhcpLeaseCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpLeaseCookie.setStatus("current")
_CfprDhcpLeaseEnds_Type = DateAndTime
_CfprDhcpLeaseEnds_Object = MibTableColumn
cfprDhcpLeaseEnds = _CfprDhcpLeaseEnds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3, 1, 6),
    _CfprDhcpLeaseEnds_Type()
)
cfprDhcpLeaseEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpLeaseEnds.setStatus("current")
_CfprDhcpLeaseHostname_Type = SnmpAdminString
_CfprDhcpLeaseHostname_Object = MibTableColumn
cfprDhcpLeaseHostname = _CfprDhcpLeaseHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3, 1, 7),
    _CfprDhcpLeaseHostname_Type()
)
cfprDhcpLeaseHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpLeaseHostname.setStatus("current")
_CfprDhcpLeaseIntf_Type = SnmpAdminString
_CfprDhcpLeaseIntf_Object = MibTableColumn
cfprDhcpLeaseIntf = _CfprDhcpLeaseIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3, 1, 8),
    _CfprDhcpLeaseIntf_Type()
)
cfprDhcpLeaseIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpLeaseIntf.setStatus("current")
_CfprDhcpLeaseIp_Type = InetAddressIPv4
_CfprDhcpLeaseIp_Object = MibTableColumn
cfprDhcpLeaseIp = _CfprDhcpLeaseIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3, 1, 9),
    _CfprDhcpLeaseIp_Type()
)
cfprDhcpLeaseIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpLeaseIp.setStatus("current")
_CfprDhcpLeaseMac_Type = MacAddress
_CfprDhcpLeaseMac_Object = MibTableColumn
cfprDhcpLeaseMac = _CfprDhcpLeaseMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3, 1, 10),
    _CfprDhcpLeaseMac_Type()
)
cfprDhcpLeaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpLeaseMac.setStatus("current")
_CfprDhcpLeaseStarts_Type = DateAndTime
_CfprDhcpLeaseStarts_Object = MibTableColumn
cfprDhcpLeaseStarts = _CfprDhcpLeaseStarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 15, 3, 1, 11),
    _CfprDhcpLeaseStarts_Type()
)
cfprDhcpLeaseStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDhcpLeaseStarts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-DHCP-MIB",
    **{"cfprDhcpObjects": cfprDhcpObjects,
       "cfprDhcpAcquiredTable": cfprDhcpAcquiredTable,
       "cfprDhcpAcquiredEntry": cfprDhcpAcquiredEntry,
       "cfprDhcpAcquiredInstanceId": cfprDhcpAcquiredInstanceId,
       "cfprDhcpAcquiredDn": cfprDhcpAcquiredDn,
       "cfprDhcpAcquiredRn": cfprDhcpAcquiredRn,
       "cfprDhcpAcquiredAcqts": cfprDhcpAcquiredAcqts,
       "cfprDhcpAcquiredCookie": cfprDhcpAcquiredCookie,
       "cfprDhcpAcquiredEnds": cfprDhcpAcquiredEnds,
       "cfprDhcpAcquiredIp": cfprDhcpAcquiredIp,
       "cfprDhcpAcquiredMac": cfprDhcpAcquiredMac,
       "cfprDhcpAcquiredSysId": cfprDhcpAcquiredSysId,
       "cfprDhcpInstTable": cfprDhcpInstTable,
       "cfprDhcpInstEntry": cfprDhcpInstEntry,
       "cfprDhcpInstInstanceId": cfprDhcpInstInstanceId,
       "cfprDhcpInstDn": cfprDhcpInstDn,
       "cfprDhcpInstRn": cfprDhcpInstRn,
       "cfprDhcpLeaseTable": cfprDhcpLeaseTable,
       "cfprDhcpLeaseEntry": cfprDhcpLeaseEntry,
       "cfprDhcpLeaseInstanceId": cfprDhcpLeaseInstanceId,
       "cfprDhcpLeaseDn": cfprDhcpLeaseDn,
       "cfprDhcpLeaseRn": cfprDhcpLeaseRn,
       "cfprDhcpLeaseCliId": cfprDhcpLeaseCliId,
       "cfprDhcpLeaseCookie": cfprDhcpLeaseCookie,
       "cfprDhcpLeaseEnds": cfprDhcpLeaseEnds,
       "cfprDhcpLeaseHostname": cfprDhcpLeaseHostname,
       "cfprDhcpLeaseIntf": cfprDhcpLeaseIntf,
       "cfprDhcpLeaseIp": cfprDhcpLeaseIp,
       "cfprDhcpLeaseMac": cfprDhcpLeaseMac,
       "cfprDhcpLeaseStarts": cfprDhcpLeaseStarts}
)
