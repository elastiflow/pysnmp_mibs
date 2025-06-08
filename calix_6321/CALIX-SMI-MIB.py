# SNMP MIB module (CALIX-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/CALIX-SMI-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:36:06 2025
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

calixNetworks = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321)
)
if mibBuilder.loadTexts:
    calixNetworks.setRevisions(
        ("2000-08-31 00:26",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CalixRegistrations_ObjectIdentity = ObjectIdentity
calixRegistrations = _CalixRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1)
)
if mibBuilder.loadTexts:
    calixRegistrations.setStatus("current")
_CalixModules_ObjectIdentity = ObjectIdentity
calixModules = _CalixModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 1)
)
if mibBuilder.loadTexts:
    calixModules.setStatus("current")
_CalixProducts_ObjectIdentity = ObjectIdentity
calixProducts = _CalixProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2)
)
if mibBuilder.loadTexts:
    calixProducts.setStatus("current")
_CalixManagement_ObjectIdentity = ObjectIdentity
calixManagement = _CalixManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2)
)
if mibBuilder.loadTexts:
    calixManagement.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-SMI-MIB",
    **{"calixNetworks": calixNetworks,
       "calixRegistrations": calixRegistrations,
       "calixModules": calixModules,
       "calixProducts": calixProducts,
       "calixManagement": calixManagement}
)
