# SNMP MIB module (ARISTA-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-SMI-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

arista = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065)
)
if mibBuilder.loadTexts:
    arista.setRevisions(
        ("2014-08-15 00:00",
         "2011-03-31 13:00",
         "2008-10-27 18:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaProducts_ObjectIdentity = ObjectIdentity
aristaProducts = _AristaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1)
)
if mibBuilder.loadTexts:
    aristaProducts.setStatus("current")
_AristaModules_ObjectIdentity = ObjectIdentity
aristaModules = _AristaModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 2)
)
if mibBuilder.loadTexts:
    aristaModules.setStatus("current")
_AristaMibs_ObjectIdentity = ObjectIdentity
aristaMibs = _AristaMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3)
)
if mibBuilder.loadTexts:
    aristaMibs.setStatus("current")
_AristaExperiment_ObjectIdentity = ObjectIdentity
aristaExperiment = _AristaExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 4)
)
if mibBuilder.loadTexts:
    aristaExperiment.setStatus("current")
_AristaInternalUse_ObjectIdentity = ObjectIdentity
aristaInternalUse = _AristaInternalUse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 5)
)
if mibBuilder.loadTexts:
    aristaInternalUse.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-SMI-MIB",
    **{"arista": arista,
       "aristaProducts": aristaProducts,
       "aristaModules": aristaModules,
       "aristaMibs": aristaMibs,
       "aristaExperiment": aristaExperiment,
       "aristaInternalUse": aristaInternalUse}
)
