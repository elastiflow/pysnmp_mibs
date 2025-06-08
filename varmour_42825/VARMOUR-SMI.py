# SNMP MIB module (VARMOUR-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/varmour_42825/VARMOUR-SMI.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:05:54 2025
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

varmour = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42825)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1)
)
if mibBuilder.loadTexts:
    mgmt.setStatus("current")
_VarmourMibs_ObjectIdentity = ObjectIdentity
varmourMibs = _VarmourMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 1, 1)
)
if mibBuilder.loadTexts:
    varmourMibs.setStatus("current")
_VamourProducts_ObjectIdentity = ObjectIdentity
vamourProducts = _VamourProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 2)
)
if mibBuilder.loadTexts:
    vamourProducts.setStatus("current")
_VaFirewall_ObjectIdentity = ObjectIdentity
vaFirewall = _VaFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42825, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VARMOUR-SMI",
    **{"varmour": varmour,
       "mgmt": mgmt,
       "varmourMibs": varmourMibs,
       "vamourProducts": vamourProducts,
       "vaFirewall": vaFirewall}
)
