# SNMP MIB module (ZYXEL-DHCPV6-TRUST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-DHCPV6-TRUST-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:26:15 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

zyxelDhcpv6Trust = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 107)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelDhcpv6TrustSetup_ObjectIdentity = ObjectIdentity
zyxelDhcpv6TrustSetup = _ZyxelDhcpv6TrustSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 107, 1)
)
_ZyDhcpv6TrustState_Type = EnabledStatus
_ZyDhcpv6TrustState_Object = MibScalar
zyDhcpv6TrustState = _ZyDhcpv6TrustState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 107, 1, 1),
    _ZyDhcpv6TrustState_Type()
)
zyDhcpv6TrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpv6TrustState.setStatus("current")
_ZyxelDhcpv6TrustPortTable_Object = MibTable
zyxelDhcpv6TrustPortTable = _ZyxelDhcpv6TrustPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 107, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelDhcpv6TrustPortTable.setStatus("current")
_ZyxelDhcpv6TrustPortEntry_Object = MibTableRow
zyxelDhcpv6TrustPortEntry = _ZyxelDhcpv6TrustPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 107, 1, 2, 1)
)
zyxelDhcpv6TrustPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelDhcpv6TrustPortEntry.setStatus("current")
_ZyDhcpv6TrustPortState_Type = EnabledStatus
_ZyDhcpv6TrustPortState_Object = MibTableColumn
zyDhcpv6TrustPortState = _ZyDhcpv6TrustPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 107, 1, 2, 1, 1),
    _ZyDhcpv6TrustPortState_Type()
)
zyDhcpv6TrustPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpv6TrustPortState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-DHCPV6-TRUST-MIB",
    **{"zyxelDhcpv6Trust": zyxelDhcpv6Trust,
       "zyxelDhcpv6TrustSetup": zyxelDhcpv6TrustSetup,
       "zyDhcpv6TrustState": zyDhcpv6TrustState,
       "zyxelDhcpv6TrustPortTable": zyxelDhcpv6TrustPortTable,
       "zyxelDhcpv6TrustPortEntry": zyxelDhcpv6TrustPortEntry,
       "zyDhcpv6TrustPortState": zyDhcpv6TrustPortState}
)
