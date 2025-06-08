# SNMP MIB module (SILVERPEAK-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/silverpeak_23867/SILVERPEAK-SMI.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:54:04 2025
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

silverpeakNW = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23867)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SilverpeakProducts_ObjectIdentity = ObjectIdentity
silverpeakProducts = _SilverpeakProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1)
)
if mibBuilder.loadTexts:
    silverpeakProducts.setStatus("current")
_SilverpeakModules_ObjectIdentity = ObjectIdentity
silverpeakModules = _SilverpeakModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 2)
)
if mibBuilder.loadTexts:
    silverpeakModules.setStatus("current")
_SilverpeakMgmt_ObjectIdentity = ObjectIdentity
silverpeakMgmt = _SilverpeakMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 3)
)
if mibBuilder.loadTexts:
    silverpeakMgmt.setStatus("current")
_SilverpeakNotifications_ObjectIdentity = ObjectIdentity
silverpeakNotifications = _SilverpeakNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 4)
)
if mibBuilder.loadTexts:
    silverpeakNotifications.setStatus("current")
_SilverpeakAgentCapability_ObjectIdentity = ObjectIdentity
silverpeakAgentCapability = _SilverpeakAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 5)
)
if mibBuilder.loadTexts:
    silverpeakAgentCapability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SILVERPEAK-SMI",
    **{"silverpeakNW": silverpeakNW,
       "silverpeakProducts": silverpeakProducts,
       "silverpeakModules": silverpeakModules,
       "silverpeakMgmt": silverpeakMgmt,
       "silverpeakNotifications": silverpeakNotifications,
       "silverpeakAgentCapability": silverpeakAgentCapability}
)
