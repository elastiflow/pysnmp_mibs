# SNMP MIB module (FOX-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/abb_17268/FOX-SMI-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:23:57 2025
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

(fox,) = mibBuilder.importSymbols(
    "ABB-ROOT-MIB",
    "fox")

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

fox61x = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 1, 20)
)
if mibBuilder.loadTexts:
    fox61x.setRevisions(
        ("2016-09-28 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FoxMgmt_ObjectIdentity = ObjectIdentity
foxMgmt = _FoxMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 1, 20, 2)
)
if mibBuilder.loadTexts:
    foxMgmt.setStatus("current")
_FoxConfig_ObjectIdentity = ObjectIdentity
foxConfig = _FoxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 1, 20, 3)
)
if mibBuilder.loadTexts:
    foxConfig.setStatus("current")
_FoxExperiment_ObjectIdentity = ObjectIdentity
foxExperiment = _FoxExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 1, 20, 4)
)
if mibBuilder.loadTexts:
    foxExperiment.setStatus("current")
_FoxAdmin_ObjectIdentity = ObjectIdentity
foxAdmin = _FoxAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 1, 20, 5)
)
if mibBuilder.loadTexts:
    foxAdmin.setStatus("current")
_FoxModules_ObjectIdentity = ObjectIdentity
foxModules = _FoxModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 1, 20, 6)
)
if mibBuilder.loadTexts:
    foxModules.setStatus("current")
_FoxTraps_ObjectIdentity = ObjectIdentity
foxTraps = _FoxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 1, 20, 7)
)
if mibBuilder.loadTexts:
    foxTraps.setStatus("current")
_FoxMob2MibModules_ObjectIdentity = ObjectIdentity
foxMob2MibModules = _FoxMob2MibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 1, 20, 8)
)
if mibBuilder.loadTexts:
    foxMob2MibModules.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOX-SMI-MIB",
    **{"fox61x": fox61x,
       "foxMgmt": foxMgmt,
       "foxConfig": foxConfig,
       "foxExperiment": foxExperiment,
       "foxAdmin": foxAdmin,
       "foxModules": foxModules,
       "foxTraps": foxTraps,
       "foxMob2MibModules": foxMob2MibModules}
)
