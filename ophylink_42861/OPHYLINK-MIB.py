# SNMP MIB module (OPHYLINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ophylink_42861/OPHYLINK-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:48:30 2025
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

ophylinkGlobalModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OphylinkRoot_ObjectIdentity = ObjectIdentity
ophylinkRoot = _OphylinkRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861)
)
if mibBuilder.loadTexts:
    ophylinkRoot.setStatus("current")
_OphylinkReg_ObjectIdentity = ObjectIdentity
ophylinkReg = _OphylinkReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 1)
)
if mibBuilder.loadTexts:
    ophylinkReg.setStatus("current")
_OphylinkModules_ObjectIdentity = ObjectIdentity
ophylinkModules = _OphylinkModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 1, 1)
)
if mibBuilder.loadTexts:
    ophylinkModules.setStatus("current")
_OphylinkGeneric_ObjectIdentity = ObjectIdentity
ophylinkGeneric = _OphylinkGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 2)
)
if mibBuilder.loadTexts:
    ophylinkGeneric.setStatus("current")
_OphylinkProducts_ObjectIdentity = ObjectIdentity
ophylinkProducts = _OphylinkProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 3)
)
if mibBuilder.loadTexts:
    ophylinkProducts.setStatus("current")
_OphylinkCaps_ObjectIdentity = ObjectIdentity
ophylinkCaps = _OphylinkCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 4)
)
if mibBuilder.loadTexts:
    ophylinkCaps.setStatus("current")
_OphylinkReqs_ObjectIdentity = ObjectIdentity
ophylinkReqs = _OphylinkReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 5)
)
if mibBuilder.loadTexts:
    ophylinkReqs.setStatus("current")
_OphylinkExpr_ObjectIdentity = ObjectIdentity
ophylinkExpr = _OphylinkExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42861, 6)
)
if mibBuilder.loadTexts:
    ophylinkExpr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPHYLINK-MIB",
    **{"ophylinkRoot": ophylinkRoot,
       "ophylinkReg": ophylinkReg,
       "ophylinkModules": ophylinkModules,
       "ophylinkGlobalModule": ophylinkGlobalModule,
       "ophylinkGeneric": ophylinkGeneric,
       "ophylinkProducts": ophylinkProducts,
       "ophylinkCaps": ophylinkCaps,
       "ophylinkReqs": ophylinkReqs,
       "ophylinkExpr": ophylinkExpr}
)
