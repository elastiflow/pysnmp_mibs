# SNMP MIB module (TRANSPORT-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/TRANSPORT-ADDRESS-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 13:29:22 2025
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

transportAddressMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 100)
)
if mibBuilder.loadTexts:
    transportAddressMIB.setRevisions(
        ("2002-11-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TransportDomain(TextualConvention, ObjectIdentifier):
    status = "current"


class TransportAddressType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("udpIpv4", 1),
          ("udpIpv6", 2),
          ("udpIpv4z", 3),
          ("udpIpv6z", 4),
          ("tcpIpv4", 5),
          ("tcpIpv6", 6),
          ("tcpIpv4z", 7),
          ("tcpIpv6z", 8),
          ("sctpIpv4", 9),
          ("sctpIpv6", 10),
          ("sctpIpv4z", 11),
          ("sctpIpv6z", 12),
          ("local", 13),
          ("udpDns", 14),
          ("tcpDns", 15),
          ("sctpDns", 16))
    )



class TransportAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TransportAddressIPv4(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d.1d.1d.1d:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6



class TransportAddressIPv6(TextualConvention, OctetString):
    status = "current"
    displayHint = "0a[2x:2x:2x:2x:2x:2x:2x:2x]0a:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )
    fixedLength = 18



class TransportAddressIPv4z(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d.1d.1d.1d%4d:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixedLength = 10



class TransportAddressIPv6z(TextualConvention, OctetString):
    status = "current"
    displayHint = "0a[2x:2x:2x:2x:2x:2x:2x:2x%4d]0a:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )
    fixedLength = 22



class TransportAddressLocal(TextualConvention, OctetString):
    status = "current"
    displayHint = "1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class TransportAddressDns(TextualConvention, OctetString):
    status = "current"
    displayHint = "1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_TransportDomains_ObjectIdentity = ObjectIdentity
transportDomains = _TransportDomains_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1)
)
_TransportDomainUdpIpv4_ObjectIdentity = ObjectIdentity
transportDomainUdpIpv4 = _TransportDomainUdpIpv4_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 1)
)
if mibBuilder.loadTexts:
    transportDomainUdpIpv4.setStatus("current")
_TransportDomainUdpIpv6_ObjectIdentity = ObjectIdentity
transportDomainUdpIpv6 = _TransportDomainUdpIpv6_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 2)
)
if mibBuilder.loadTexts:
    transportDomainUdpIpv6.setStatus("current")
_TransportDomainUdpIpv4z_ObjectIdentity = ObjectIdentity
transportDomainUdpIpv4z = _TransportDomainUdpIpv4z_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 3)
)
if mibBuilder.loadTexts:
    transportDomainUdpIpv4z.setStatus("current")
_TransportDomainUdpIpv6z_ObjectIdentity = ObjectIdentity
transportDomainUdpIpv6z = _TransportDomainUdpIpv6z_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 4)
)
if mibBuilder.loadTexts:
    transportDomainUdpIpv6z.setStatus("current")
_TransportDomainTcpIpv4_ObjectIdentity = ObjectIdentity
transportDomainTcpIpv4 = _TransportDomainTcpIpv4_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 5)
)
if mibBuilder.loadTexts:
    transportDomainTcpIpv4.setStatus("current")
_TransportDomainTcpIpv6_ObjectIdentity = ObjectIdentity
transportDomainTcpIpv6 = _TransportDomainTcpIpv6_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 6)
)
if mibBuilder.loadTexts:
    transportDomainTcpIpv6.setStatus("current")
_TransportDomainTcpIpv4z_ObjectIdentity = ObjectIdentity
transportDomainTcpIpv4z = _TransportDomainTcpIpv4z_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 7)
)
if mibBuilder.loadTexts:
    transportDomainTcpIpv4z.setStatus("current")
_TransportDomainTcpIpv6z_ObjectIdentity = ObjectIdentity
transportDomainTcpIpv6z = _TransportDomainTcpIpv6z_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 8)
)
if mibBuilder.loadTexts:
    transportDomainTcpIpv6z.setStatus("current")
_TransportDomainSctpIpv4_ObjectIdentity = ObjectIdentity
transportDomainSctpIpv4 = _TransportDomainSctpIpv4_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 9)
)
if mibBuilder.loadTexts:
    transportDomainSctpIpv4.setStatus("current")
_TransportDomainSctpIpv6_ObjectIdentity = ObjectIdentity
transportDomainSctpIpv6 = _TransportDomainSctpIpv6_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 10)
)
if mibBuilder.loadTexts:
    transportDomainSctpIpv6.setStatus("current")
_TransportDomainSctpIpv4z_ObjectIdentity = ObjectIdentity
transportDomainSctpIpv4z = _TransportDomainSctpIpv4z_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 11)
)
if mibBuilder.loadTexts:
    transportDomainSctpIpv4z.setStatus("current")
_TransportDomainSctpIpv6z_ObjectIdentity = ObjectIdentity
transportDomainSctpIpv6z = _TransportDomainSctpIpv6z_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 12)
)
if mibBuilder.loadTexts:
    transportDomainSctpIpv6z.setStatus("current")
_TransportDomainLocal_ObjectIdentity = ObjectIdentity
transportDomainLocal = _TransportDomainLocal_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 13)
)
if mibBuilder.loadTexts:
    transportDomainLocal.setStatus("current")
_TransportDomainUdpDns_ObjectIdentity = ObjectIdentity
transportDomainUdpDns = _TransportDomainUdpDns_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 14)
)
if mibBuilder.loadTexts:
    transportDomainUdpDns.setStatus("current")
_TransportDomainTcpDns_ObjectIdentity = ObjectIdentity
transportDomainTcpDns = _TransportDomainTcpDns_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 15)
)
if mibBuilder.loadTexts:
    transportDomainTcpDns.setStatus("current")
_TransportDomainSctpDns_ObjectIdentity = ObjectIdentity
transportDomainSctpDns = _TransportDomainSctpDns_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 100, 1, 16)
)
if mibBuilder.loadTexts:
    transportDomainSctpDns.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRANSPORT-ADDRESS-MIB",
    **{"TransportDomain": TransportDomain,
       "TransportAddressType": TransportAddressType,
       "TransportAddress": TransportAddress,
       "TransportAddressIPv4": TransportAddressIPv4,
       "TransportAddressIPv6": TransportAddressIPv6,
       "TransportAddressIPv4z": TransportAddressIPv4z,
       "TransportAddressIPv6z": TransportAddressIPv6z,
       "TransportAddressLocal": TransportAddressLocal,
       "TransportAddressDns": TransportAddressDns,
       "transportAddressMIB": transportAddressMIB,
       "transportDomains": transportDomains,
       "transportDomainUdpIpv4": transportDomainUdpIpv4,
       "transportDomainUdpIpv6": transportDomainUdpIpv6,
       "transportDomainUdpIpv4z": transportDomainUdpIpv4z,
       "transportDomainUdpIpv6z": transportDomainUdpIpv6z,
       "transportDomainTcpIpv4": transportDomainTcpIpv4,
       "transportDomainTcpIpv6": transportDomainTcpIpv6,
       "transportDomainTcpIpv4z": transportDomainTcpIpv4z,
       "transportDomainTcpIpv6z": transportDomainTcpIpv6z,
       "transportDomainSctpIpv4": transportDomainSctpIpv4,
       "transportDomainSctpIpv6": transportDomainSctpIpv6,
       "transportDomainSctpIpv4z": transportDomainSctpIpv4z,
       "transportDomainSctpIpv6z": transportDomainSctpIpv6z,
       "transportDomainLocal": transportDomainLocal,
       "transportDomainUdpDns": transportDomainUdpDns,
       "transportDomainTcpDns": transportDomainTcpDns,
       "transportDomainSctpDns": transportDomainSctpDns}
)
