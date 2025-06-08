# SNMP MIB module (RUIJIE-WIRELESS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-WIRELESS-SMI.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

(products,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "products")

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


# MODULE-IDENTITY

wirelessMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wirelessMib.setRevisions(
        ("2007-07-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3)
)
_RuijieWirelessProducts_ObjectIdentity = ObjectIdentity
ruijieWirelessProducts = _RuijieWirelessProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieWirelessProducts.setStatus("current")
_RuijieWirelessMgmt_ObjectIdentity = ObjectIdentity
ruijieWirelessMgmt = _RuijieWirelessMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieWirelessMgmt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-WIRELESS-SMI",
    **{"wireless": wireless,
       "wirelessMib": wirelessMib,
       "ruijieWirelessProducts": ruijieWirelessProducts,
       "ruijieWirelessMgmt": ruijieWirelessMgmt}
)
