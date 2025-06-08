# SNMP MIB module (ZYXEL-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-DNS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:25:24 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelDns = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelDnsSetup_ObjectIdentity = ObjectIdentity
zyxelDnsSetup = _ZyxelDnsSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 1)
)
_ZyxelDnsStaticNameServerTable_Object = MibTable
zyxelDnsStaticNameServerTable = _ZyxelDnsStaticNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelDnsStaticNameServerTable.setStatus("current")
_ZyxelDnsStaticNameServerEntry_Object = MibTableRow
zyxelDnsStaticNameServerEntry = _ZyxelDnsStaticNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 1, 1, 1)
)
zyxelDnsStaticNameServerEntry.setIndexNames(
    (0, "ZYXEL-DNS-MIB", "zyDnsStaticNameServerPreference"),
)
if mibBuilder.loadTexts:
    zyxelDnsStaticNameServerEntry.setStatus("current")
_ZyDnsStaticNameServerPreference_Type = Integer32
_ZyDnsStaticNameServerPreference_Object = MibTableColumn
zyDnsStaticNameServerPreference = _ZyDnsStaticNameServerPreference_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 1, 1, 1, 1),
    _ZyDnsStaticNameServerPreference_Type()
)
zyDnsStaticNameServerPreference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyDnsStaticNameServerPreference.setStatus("current")
_ZyDnsStaticNameServerInetAddressType_Type = InetAddressType
_ZyDnsStaticNameServerInetAddressType_Object = MibTableColumn
zyDnsStaticNameServerInetAddressType = _ZyDnsStaticNameServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 1, 1, 1, 2),
    _ZyDnsStaticNameServerInetAddressType_Type()
)
zyDnsStaticNameServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDnsStaticNameServerInetAddressType.setStatus("current")
_ZyDnsStaticNameServerInetAddress_Type = InetAddress
_ZyDnsStaticNameServerInetAddress_Object = MibTableColumn
zyDnsStaticNameServerInetAddress = _ZyDnsStaticNameServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 1, 1, 1, 3),
    _ZyDnsStaticNameServerInetAddress_Type()
)
zyDnsStaticNameServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDnsStaticNameServerInetAddress.setStatus("current")
_ZyxelDnsStatus_ObjectIdentity = ObjectIdentity
zyxelDnsStatus = _ZyxelDnsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 2)
)
_ZyxelDnsNameServerTable_Object = MibTable
zyxelDnsNameServerTable = _ZyxelDnsNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelDnsNameServerTable.setStatus("current")
_ZyxelDnsNameServerEntry_Object = MibTableRow
zyxelDnsNameServerEntry = _ZyxelDnsNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 2, 1, 1)
)
zyxelDnsNameServerEntry.setIndexNames(
    (0, "ZYXEL-DNS-MIB", "zyDnsNameServerIndex"),
)
if mibBuilder.loadTexts:
    zyxelDnsNameServerEntry.setStatus("current")
_ZyDnsNameServerIndex_Type = Integer32
_ZyDnsNameServerIndex_Object = MibTableColumn
zyDnsNameServerIndex = _ZyDnsNameServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 2, 1, 1, 1),
    _ZyDnsNameServerIndex_Type()
)
zyDnsNameServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyDnsNameServerIndex.setStatus("current")
_ZyDnsNameServerInetAddressType_Type = InetAddressType
_ZyDnsNameServerInetAddressType_Object = MibTableColumn
zyDnsNameServerInetAddressType = _ZyDnsNameServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 2, 1, 1, 2),
    _ZyDnsNameServerInetAddressType_Type()
)
zyDnsNameServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDnsNameServerInetAddressType.setStatus("current")
_ZyDnsNameServerInetAddress_Type = InetAddress
_ZyDnsNameServerInetAddress_Object = MibTableColumn
zyDnsNameServerInetAddress = _ZyDnsNameServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 2, 1, 1, 3),
    _ZyDnsNameServerInetAddress_Type()
)
zyDnsNameServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDnsNameServerInetAddress.setStatus("current")


class _ZyDnsNameServerSource_Type(Integer32):
    """Custom type zyDnsNameServerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dhcpv4", 1),
          ("dhcpv6", 2))
    )


_ZyDnsNameServerSource_Type.__name__ = "Integer32"
_ZyDnsNameServerSource_Object = MibTableColumn
zyDnsNameServerSource = _ZyDnsNameServerSource_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 111, 2, 1, 1, 4),
    _ZyDnsNameServerSource_Type()
)
zyDnsNameServerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDnsNameServerSource.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-DNS-MIB",
    **{"zyxelDns": zyxelDns,
       "zyxelDnsSetup": zyxelDnsSetup,
       "zyxelDnsStaticNameServerTable": zyxelDnsStaticNameServerTable,
       "zyxelDnsStaticNameServerEntry": zyxelDnsStaticNameServerEntry,
       "zyDnsStaticNameServerPreference": zyDnsStaticNameServerPreference,
       "zyDnsStaticNameServerInetAddressType": zyDnsStaticNameServerInetAddressType,
       "zyDnsStaticNameServerInetAddress": zyDnsStaticNameServerInetAddress,
       "zyxelDnsStatus": zyxelDnsStatus,
       "zyxelDnsNameServerTable": zyxelDnsNameServerTable,
       "zyxelDnsNameServerEntry": zyxelDnsNameServerEntry,
       "zyDnsNameServerIndex": zyDnsNameServerIndex,
       "zyDnsNameServerInetAddressType": zyDnsNameServerInetAddressType,
       "zyDnsNameServerInetAddress": zyDnsNameServerInetAddress,
       "zyDnsNameServerSource": zyDnsNameServerSource}
)
