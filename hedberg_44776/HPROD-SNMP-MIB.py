# SNMP MIB module (HPROD-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/hedberg_44776/HPROD-SNMP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:32:02 2025
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

hPsnmpRootMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44776, 1, 2, 0)
)
if mibBuilder.loadTexts:
    hPsnmpRootMIB.setRevisions(
        ("2015-03-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HedbergProductions_ObjectIdentity = ObjectIdentity
hedbergProductions = _HedbergProductions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44776)
)
_HPsnmpRoot_ObjectIdentity = ObjectIdentity
hPsnmpRoot = _HPsnmpRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44776, 1)
)
_HPsnmpMIBgroups_ObjectIdentity = ObjectIdentity
hPsnmpMIBgroups = _HPsnmpMIBgroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44776, 1, 1)
)
_HPsnmpModuleIdentity_ObjectIdentity = ObjectIdentity
hPsnmpModuleIdentity = _HPsnmpModuleIdentity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44776, 1, 2)
)
_HPsnmpMIBS_ObjectIdentity = ObjectIdentity
hPsnmpMIBS = _HPsnmpMIBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44776, 1, 3)
)
_HPsnmpRootRoot_ObjectIdentity = ObjectIdentity
hPsnmpRootRoot = _HPsnmpRootRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44776, 1, 3, 0)
)
_HPsnmpModuleCompliances_ObjectIdentity = ObjectIdentity
hPsnmpModuleCompliances = _HPsnmpModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44776, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hPsnmpRootMIBcompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 44776, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hPsnmpRootMIBcompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPROD-SNMP-MIB",
    **{"hedbergProductions": hedbergProductions,
       "hPsnmpRoot": hPsnmpRoot,
       "hPsnmpMIBgroups": hPsnmpMIBgroups,
       "hPsnmpModuleIdentity": hPsnmpModuleIdentity,
       "hPsnmpRootMIB": hPsnmpRootMIB,
       "hPsnmpMIBS": hPsnmpMIBS,
       "hPsnmpRootRoot": hPsnmpRootRoot,
       "hPsnmpModuleCompliances": hPsnmpModuleCompliances,
       "hPsnmpRootMIBcompliance": hPsnmpRootMIBcompliance}
)
