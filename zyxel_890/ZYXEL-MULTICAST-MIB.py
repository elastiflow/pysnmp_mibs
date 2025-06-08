# SNMP MIB module (ZYXEL-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-MULTICAST-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:45:43 2025
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

zyxelMulticast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMulticastSetup_ObjectIdentity = ObjectIdentity
zyxelMulticastSetup = _ZyxelMulticastSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1)
)


class _ZyMulticastUnknownMulticastFrameForwarding_Type(Integer32):
    """Custom type zyMulticastUnknownMulticastFrameForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flooding", 1),
          ("drop", 2))
    )


_ZyMulticastUnknownMulticastFrameForwarding_Type.__name__ = "Integer32"
_ZyMulticastUnknownMulticastFrameForwarding_Object = MibScalar
zyMulticastUnknownMulticastFrameForwarding = _ZyMulticastUnknownMulticastFrameForwarding_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 1),
    _ZyMulticastUnknownMulticastFrameForwarding_Type()
)
zyMulticastUnknownMulticastFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastUnknownMulticastFrameForwarding.setStatus("current")


class _ZyMulticastReservedMulticastFrameForwarding_Type(Integer32):
    """Custom type zyMulticastReservedMulticastFrameForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flooding", 1),
          ("drop", 2))
    )


_ZyMulticastReservedMulticastFrameForwarding_Type.__name__ = "Integer32"
_ZyMulticastReservedMulticastFrameForwarding_Object = MibScalar
zyMulticastReservedMulticastFrameForwarding = _ZyMulticastReservedMulticastFrameForwarding_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 2),
    _ZyMulticastReservedMulticastFrameForwarding_Type()
)
zyMulticastReservedMulticastFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastReservedMulticastFrameForwarding.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MULTICAST-MIB",
    **{"zyxelMulticast": zyxelMulticast,
       "zyxelMulticastSetup": zyxelMulticastSetup,
       "zyMulticastUnknownMulticastFrameForwarding": zyMulticastUnknownMulticastFrameForwarding,
       "zyMulticastReservedMulticastFrameForwarding": zyMulticastReservedMulticastFrameForwarding}
)
