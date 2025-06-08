# SNMP MIB module (JUNIPER-V1-TRAPS-BGP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-V1-TRAPS-BGP.mib
# Produced by pysmi-1.5.11 at Sat May 31 15:31:34 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bgp_ObjectIdentity = ObjectIdentity
bgp = _Bgp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 15)
)
_BgpPeerTable_ObjectIdentity = ObjectIdentity
bgpPeerTable = _BgpPeerTable_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 15, 3)
)
_BgpPeerEntry_ObjectIdentity = ObjectIdentity
bgpPeerEntry = _BgpPeerEntry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 15, 3, 1)
)
_BgpPeerState_ObjectIdentity = ObjectIdentity
bgpPeerState = _BgpPeerState_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 2)
)
_BgpPeerLastError_ObjectIdentity = ObjectIdentity
bgpPeerLastError = _BgpPeerLastError_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 15, 3, 1, 14)
)
_JuniperMIB_ObjectIdentity = ObjectIdentity
juniperMIB = _JuniperMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636)
)

# Managed Objects groups


# Notification objects

bgpEstablishedV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 1)
)
bgpEstablishedV1.setObjects(
      *(("JUNIPER-V1-TRAPS-BGP", "bgpPeerLastError"),
        ("JUNIPER-V1-TRAPS-BGP", "bgpPeerState"))
)
if mibBuilder.loadTexts:
    bgpEstablishedV1.setStatus(
        ""
    )

bgpBackwardTransitionV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 2)
)
bgpBackwardTransitionV1.setObjects(
      *(("JUNIPER-V1-TRAPS-BGP", "bgpPeerLastError"),
        ("JUNIPER-V1-TRAPS-BGP", "bgpPeerState"))
)
if mibBuilder.loadTexts:
    bgpBackwardTransitionV1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-V1-TRAPS-BGP",
    **{"bgp": bgp,
       "bgpPeerTable": bgpPeerTable,
       "bgpPeerEntry": bgpPeerEntry,
       "bgpPeerState": bgpPeerState,
       "bgpPeerLastError": bgpPeerLastError,
       "juniperMIB": juniperMIB,
       "bgpEstablishedV1": bgpEstablishedV1,
       "bgpBackwardTransitionV1": bgpBackwardTransitionV1}
)
