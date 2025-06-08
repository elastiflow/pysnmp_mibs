# SNMP MIB module (EXFO-SMI-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exfo_6718/EXFO-SMI-REG.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:54:13 2025
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

exfoSmi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Exfo_ObjectIdentity = ObjectIdentity
exfo = _Exfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718)
)
_ExfoRegistration_ObjectIdentity = ObjectIdentity
exfoRegistration = _ExfoRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 1)
)
if mibBuilder.loadTexts:
    exfoRegistration.setStatus("current")
_ExfoModules_ObjectIdentity = ObjectIdentity
exfoModules = _ExfoModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 1, 1)
)
if mibBuilder.loadTexts:
    exfoModules.setStatus("current")
_ExfoCommonMib_ObjectIdentity = ObjectIdentity
exfoCommonMib = _ExfoCommonMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2)
)
if mibBuilder.loadTexts:
    exfoCommonMib.setStatus("current")
_ExfoProductMib_ObjectIdentity = ObjectIdentity
exfoProductMib = _ExfoProductMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 3)
)
if mibBuilder.loadTexts:
    exfoProductMib.setStatus("current")
_ExfoAgentCapability_ObjectIdentity = ObjectIdentity
exfoAgentCapability = _ExfoAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 4)
)
if mibBuilder.loadTexts:
    exfoAgentCapability.setStatus("current")
_ExfoRequirements_ObjectIdentity = ObjectIdentity
exfoRequirements = _ExfoRequirements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 5)
)
if mibBuilder.loadTexts:
    exfoRequirements.setStatus("current")
_ExfoExperiment_ObjectIdentity = ObjectIdentity
exfoExperiment = _ExfoExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 6)
)
if mibBuilder.loadTexts:
    exfoExperiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXFO-SMI-REG",
    **{"exfo": exfo,
       "exfoRegistration": exfoRegistration,
       "exfoModules": exfoModules,
       "exfoSmi": exfoSmi,
       "exfoCommonMib": exfoCommonMib,
       "exfoProductMib": exfoProductMib,
       "exfoAgentCapability": exfoAgentCapability,
       "exfoRequirements": exfoRequirements,
       "exfoExperiment": exfoExperiment}
)
