# SNMP MIB module (BELAIR-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-SMI.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

belairSmiModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 1, 1)
)
if mibBuilder.loadTexts:
    belairSmiModule.setRevisions(
        ("2004-09-20 10:20",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BelairNetworks_ObjectIdentity = ObjectIdentity
belairNetworks = _BelairNetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768)
)
if mibBuilder.loadTexts:
    belairNetworks.setStatus("current")
_BelairModules_ObjectIdentity = ObjectIdentity
belairModules = _BelairModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 1)
)
if mibBuilder.loadTexts:
    belairModules.setStatus("current")
_BelairRegistrations_ObjectIdentity = ObjectIdentity
belairRegistrations = _BelairRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 2)
)
if mibBuilder.loadTexts:
    belairRegistrations.setStatus("current")
_BelairGeneric_ObjectIdentity = ObjectIdentity
belairGeneric = _BelairGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3)
)
if mibBuilder.loadTexts:
    belairGeneric.setStatus("current")
_BelairInterfaces_ObjectIdentity = ObjectIdentity
belairInterfaces = _BelairInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4)
)
if mibBuilder.loadTexts:
    belairInterfaces.setStatus("current")
_BelairProtocols_ObjectIdentity = ObjectIdentity
belairProtocols = _BelairProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 5)
)
if mibBuilder.loadTexts:
    belairProtocols.setStatus("current")
_BelairApplications_ObjectIdentity = ObjectIdentity
belairApplications = _BelairApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 6)
)
if mibBuilder.loadTexts:
    belairApplications.setStatus("current")
_BelairProducts_ObjectIdentity = ObjectIdentity
belairProducts = _BelairProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 7)
)
if mibBuilder.loadTexts:
    belairProducts.setStatus("current")
_BelairExperiment_ObjectIdentity = ObjectIdentity
belairExperiment = _BelairExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 8)
)
if mibBuilder.loadTexts:
    belairExperiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-SMI",
    **{"belairNetworks": belairNetworks,
       "belairModules": belairModules,
       "belairSmiModule": belairSmiModule,
       "belairRegistrations": belairRegistrations,
       "belairGeneric": belairGeneric,
       "belairInterfaces": belairInterfaces,
       "belairProtocols": belairProtocols,
       "belairApplications": belairApplications,
       "belairProducts": belairProducts,
       "belairExperiment": belairExperiment}
)
