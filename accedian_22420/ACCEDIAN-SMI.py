# SNMP MIB module (ACCEDIAN-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/accedian_22420/ACCEDIAN-SMI.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:07:59 2025
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

accedianMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420)
)
if mibBuilder.loadTexts:
    accedianMIB.setRevisions(
        ("2006-08-06 01:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdProducts_ObjectIdentity = ObjectIdentity
acdProducts = _AcdProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 1)
)
if mibBuilder.loadTexts:
    acdProducts.setStatus("current")
_AcdMibs_ObjectIdentity = ObjectIdentity
acdMibs = _AcdMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2)
)
if mibBuilder.loadTexts:
    acdMibs.setStatus("current")
_AcdTraps_ObjectIdentity = ObjectIdentity
acdTraps = _AcdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 3)
)
if mibBuilder.loadTexts:
    acdTraps.setStatus("current")
_AcdExperiment_ObjectIdentity = ObjectIdentity
acdExperiment = _AcdExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 4)
)
_AcdServices_ObjectIdentity = ObjectIdentity
acdServices = _AcdServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 5)
)
if mibBuilder.loadTexts:
    acdServices.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACCEDIAN-SMI",
    **{"accedianMIB": accedianMIB,
       "acdProducts": acdProducts,
       "acdMibs": acdMibs,
       "acdTraps": acdTraps,
       "acdExperiment": acdExperiment,
       "acdServices": acdServices}
)
