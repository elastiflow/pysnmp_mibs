# SNMP MIB module (CISCOSB-DHCPv6) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCOSB-DHCPv6.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:12:45 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlDhcpv6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlDhcpv6Common_ObjectIdentity = ObjectIdentity
rlDhcpv6Common = _RlDhcpv6Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 1)
)


class _RlDhcpv6DuidEn_Type(OctetString):
    """Custom type rlDhcpv6DuidEn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 38),
    )


_RlDhcpv6DuidEn_Type.__name__ = "OctetString"
_RlDhcpv6DuidEn_Object = MibScalar
rlDhcpv6DuidEn = _RlDhcpv6DuidEn_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 1, 1),
    _RlDhcpv6DuidEn_Type()
)
rlDhcpv6DuidEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpv6DuidEn.setStatus("current")
_RlDhcpv6Client_ObjectIdentity = ObjectIdentity
rlDhcpv6Client = _RlDhcpv6Client_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 2)
)
_RlDhcpv6Relay_ObjectIdentity = ObjectIdentity
rlDhcpv6Relay = _RlDhcpv6Relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-DHCPv6",
    **{"rlDhcpv6": rlDhcpv6,
       "rlDhcpv6Common": rlDhcpv6Common,
       "rlDhcpv6DuidEn": rlDhcpv6DuidEn,
       "rlDhcpv6Client": rlDhcpv6Client,
       "rlDhcpv6Relay": rlDhcpv6Relay}
)
