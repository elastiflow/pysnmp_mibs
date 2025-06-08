# SNMP MIB module (WS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/WS-SMI.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:41:50 2025
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

(altitude4700,
 wirelessProducts) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "altitude4700",
    "wirelessProducts")

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
 enterprises,
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
    "enterprises",
    "iso")

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

_WingSysoidWm3700_ObjectIdentity = ObjectIdentity
wingSysoidWm3700 = _WingSysoidWm3700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 131, 15)
)
if mibBuilder.loadTexts:
    wingSysoidWm3700.setStatus("current")
_WingSysoidWm3600_ObjectIdentity = ObjectIdentity
wingSysoidWm3600 = _WingSysoidWm3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 131, 16)
)
if mibBuilder.loadTexts:
    wingSysoidWm3600.setStatus("current")
_WingSysoidWm3400_ObjectIdentity = ObjectIdentity
wingSysoidWm3400 = _WingSysoidWm3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 131, 18)
)
if mibBuilder.loadTexts:
    wingSysoidWm3400.setStatus("current")
_Altitude4700Sysoids_ObjectIdentity = ObjectIdentity
altitude4700Sysoids = _Altitude4700Sysoids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 158, 1)
)
_WingSysoidAp4710_ObjectIdentity = ObjectIdentity
wingSysoidAp4710 = _WingSysoidAp4710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 158, 1, 6)
)
if mibBuilder.loadTexts:
    wingSysoidAp4710.setStatus("current")
_WingSysoidAp4750_ObjectIdentity = ObjectIdentity
wingSysoidAp4750 = _WingSysoidAp4750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 158, 1, 7)
)
if mibBuilder.loadTexts:
    wingSysoidAp4750.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-SMI",
    **{"wingSysoidWm3700": wingSysoidWm3700,
       "wingSysoidWm3600": wingSysoidWm3600,
       "wingSysoidWm3400": wingSysoidWm3400,
       "altitude4700Sysoids": altitude4700Sysoids,
       "wingSysoidAp4710": wingSysoidAp4710,
       "wingSysoidAp4750": wingSysoidAp4750}
)
