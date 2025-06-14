# SNMP MIB module (RBN-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-SMI.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:42 2025
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

rbnSMI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352)
)
if mibBuilder.loadTexts:
    rbnSMI.setRevisions(
        ("2011-01-19 18:00",
         "2002-06-06 00:00",
         "2001-06-27 00:00",
         "1998-04-18 23:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnProducts_ObjectIdentity = ObjectIdentity
rbnProducts = _RbnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 1)
)
if mibBuilder.loadTexts:
    rbnProducts.setStatus("current")
_RbnMgmt_ObjectIdentity = ObjectIdentity
rbnMgmt = _RbnMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2)
)
if mibBuilder.loadTexts:
    rbnMgmt.setStatus("current")
_RbnExperiment_ObjectIdentity = ObjectIdentity
rbnExperiment = _RbnExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 3)
)
if mibBuilder.loadTexts:
    rbnExperiment.setStatus("current")
_RbnCapabilities_ObjectIdentity = ObjectIdentity
rbnCapabilities = _RbnCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 4)
)
if mibBuilder.loadTexts:
    rbnCapabilities.setStatus("current")
_RbnModules_ObjectIdentity = ObjectIdentity
rbnModules = _RbnModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5)
)
if mibBuilder.loadTexts:
    rbnModules.setStatus("current")
_RbnEntities_ObjectIdentity = ObjectIdentity
rbnEntities = _RbnEntities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 6)
)
if mibBuilder.loadTexts:
    rbnEntities.setStatus("current")
_RbnInternal_ObjectIdentity = ObjectIdentity
rbnInternal = _RbnInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 7)
)
if mibBuilder.loadTexts:
    rbnInternal.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-SMI",
    **{"rbnSMI": rbnSMI,
       "rbnProducts": rbnProducts,
       "rbnMgmt": rbnMgmt,
       "rbnExperiment": rbnExperiment,
       "rbnCapabilities": rbnCapabilities,
       "rbnModules": rbnModules,
       "rbnEntities": rbnEntities,
       "rbnInternal": rbnInternal}
)
