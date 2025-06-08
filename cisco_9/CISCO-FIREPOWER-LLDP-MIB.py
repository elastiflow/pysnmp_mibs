# SNMP MIB module (CISCO-FIREPOWER-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-LLDP-MIB.mib
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

cfprLldpObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 45)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprLldpAcquiredTable_Object = MibTable
cfprLldpAcquiredTable = _CfprLldpAcquiredTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 45, 1)
)
if mibBuilder.loadTexts:
    cfprLldpAcquiredTable.setStatus("current")
_CfprLldpAcquiredEntry_Object = MibTableRow
cfprLldpAcquiredEntry = _CfprLldpAcquiredEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 45, 1, 1)
)
cfprLldpAcquiredEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-LLDP-MIB", "cfprLldpAcquiredInstanceId"),
)
if mibBuilder.loadTexts:
    cfprLldpAcquiredEntry.setStatus("current")
_CfprLldpAcquiredInstanceId_Type = CfprManagedObjectId
_CfprLldpAcquiredInstanceId_Object = MibTableColumn
cfprLldpAcquiredInstanceId = _CfprLldpAcquiredInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 45, 1, 1, 1),
    _CfprLldpAcquiredInstanceId_Type()
)
cfprLldpAcquiredInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprLldpAcquiredInstanceId.setStatus("current")
_CfprLldpAcquiredDn_Type = CfprManagedObjectDn
_CfprLldpAcquiredDn_Object = MibTableColumn
cfprLldpAcquiredDn = _CfprLldpAcquiredDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 45, 1, 1, 2),
    _CfprLldpAcquiredDn_Type()
)
cfprLldpAcquiredDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLldpAcquiredDn.setStatus("current")
_CfprLldpAcquiredRn_Type = SnmpAdminString
_CfprLldpAcquiredRn_Object = MibTableColumn
cfprLldpAcquiredRn = _CfprLldpAcquiredRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 45, 1, 1, 3),
    _CfprLldpAcquiredRn_Type()
)
cfprLldpAcquiredRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLldpAcquiredRn.setStatus("current")
_CfprLldpAcquiredAcqts_Type = DateAndTime
_CfprLldpAcquiredAcqts_Object = MibTableColumn
cfprLldpAcquiredAcqts = _CfprLldpAcquiredAcqts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 45, 1, 1, 4),
    _CfprLldpAcquiredAcqts_Type()
)
cfprLldpAcquiredAcqts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLldpAcquiredAcqts.setStatus("current")
_CfprLldpAcquiredChassisMac_Type = MacAddress
_CfprLldpAcquiredChassisMac_Object = MibTableColumn
cfprLldpAcquiredChassisMac = _CfprLldpAcquiredChassisMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 45, 1, 1, 5),
    _CfprLldpAcquiredChassisMac_Type()
)
cfprLldpAcquiredChassisMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLldpAcquiredChassisMac.setStatus("current")
_CfprLldpAcquiredPeerDn_Type = SnmpAdminString
_CfprLldpAcquiredPeerDn_Object = MibTableColumn
cfprLldpAcquiredPeerDn = _CfprLldpAcquiredPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 45, 1, 1, 6),
    _CfprLldpAcquiredPeerDn_Type()
)
cfprLldpAcquiredPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLldpAcquiredPeerDn.setStatus("current")
_CfprLldpAcquiredPortMac_Type = MacAddress
_CfprLldpAcquiredPortMac_Object = MibTableColumn
cfprLldpAcquiredPortMac = _CfprLldpAcquiredPortMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 45, 1, 1, 7),
    _CfprLldpAcquiredPortMac_Type()
)
cfprLldpAcquiredPortMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprLldpAcquiredPortMac.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-LLDP-MIB",
    **{"cfprLldpObjects": cfprLldpObjects,
       "cfprLldpAcquiredTable": cfprLldpAcquiredTable,
       "cfprLldpAcquiredEntry": cfprLldpAcquiredEntry,
       "cfprLldpAcquiredInstanceId": cfprLldpAcquiredInstanceId,
       "cfprLldpAcquiredDn": cfprLldpAcquiredDn,
       "cfprLldpAcquiredRn": cfprLldpAcquiredRn,
       "cfprLldpAcquiredAcqts": cfprLldpAcquiredAcqts,
       "cfprLldpAcquiredChassisMac": cfprLldpAcquiredChassisMac,
       "cfprLldpAcquiredPeerDn": cfprLldpAcquiredPeerDn,
       "cfprLldpAcquiredPortMac": cfprLldpAcquiredPortMac}
)
