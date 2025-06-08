# SNMP MIB module (L2L3-VPN-MULTICAST-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/L2L3-VPN-MULTICAST-TC-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:25:01 2025
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

l2L3VpnMcastTCMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 244)
)
if mibBuilder.loadTexts:
    l2L3VpnMcastTCMIB.setRevisions(
        ("2018-12-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class L2L3VpnMcastProviderTunnelType(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("noTunnelInfo", 0),
          ("rsvpP2mp", 1),
          ("ldpP2mp", 2),
          ("pimSsm", 3),
          ("pimAsm", 4),
          ("pimBidir", 5),
          ("ingressReplication", 6),
          ("ldpMp2mp", 7),
          ("transportTunnel", 8))
    )



class L2L3VpnMcastProviderTunnelId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(12, 12),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(17, 17),
        ValueSizeConstraint(24, 24),
        ValueSizeConstraint(29, 29),
        ValueSizeConstraint(32, 32),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "L2L3-VPN-MULTICAST-TC-MIB",
    **{"L2L3VpnMcastProviderTunnelType": L2L3VpnMcastProviderTunnelType,
       "L2L3VpnMcastProviderTunnelId": L2L3VpnMcastProviderTunnelId,
       "l2L3VpnMcastTCMIB": l2L3VpnMcastTCMIB}
)
