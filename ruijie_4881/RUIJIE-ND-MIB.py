# SNMP MIB module (RUIJIE-ND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-ND-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:06 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ruijieNDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 125)
)
if mibBuilder.loadTexts:
    ruijieNDMIB.setRevisions(
        ("2013-12-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieNDMIBObjects_ObjectIdentity = ObjectIdentity
ruijieNDMIBObjects = _RuijieNDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 125, 1)
)
_RuijieNDTotalActiveNeighbors_Type = Counter32
_RuijieNDTotalActiveNeighbors_Object = MibScalar
ruijieNDTotalActiveNeighbors = _RuijieNDTotalActiveNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 125, 1, 1),
    _RuijieNDTotalActiveNeighbors_Type()
)
ruijieNDTotalActiveNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNDTotalActiveNeighbors.setStatus("current")
_RuijieNDTotalActiveDynamicNeighbors_Type = Counter32
_RuijieNDTotalActiveDynamicNeighbors_Object = MibScalar
ruijieNDTotalActiveDynamicNeighbors = _RuijieNDTotalActiveDynamicNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 125, 1, 2),
    _RuijieNDTotalActiveDynamicNeighbors_Type()
)
ruijieNDTotalActiveDynamicNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNDTotalActiveDynamicNeighbors.setStatus("current")
_RuijieNDTotalStaticNeighbors_Type = Counter32
_RuijieNDTotalStaticNeighbors_Object = MibScalar
ruijieNDTotalStaticNeighbors = _RuijieNDTotalStaticNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 125, 1, 3),
    _RuijieNDTotalStaticNeighbors_Type()
)
ruijieNDTotalStaticNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNDTotalStaticNeighbors.setStatus("current")
_RuijieNDTotalActiveStaticNeighbors_Type = Counter32
_RuijieNDTotalActiveStaticNeighbors_Object = MibScalar
ruijieNDTotalActiveStaticNeighbors = _RuijieNDTotalActiveStaticNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 125, 1, 4),
    _RuijieNDTotalActiveStaticNeighbors_Type()
)
ruijieNDTotalActiveStaticNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieNDTotalActiveStaticNeighbors.setStatus("current")
_RuijieNDMIBConformance_ObjectIdentity = ObjectIdentity
ruijieNDMIBConformance = _RuijieNDMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 125, 2)
)
_RuijieNDMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieNDMIBCompliances = _RuijieNDMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 125, 2, 1)
)
_RuijieNDMIBGroups_ObjectIdentity = ObjectIdentity
ruijieNDMIBGroups = _RuijieNDMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 125, 2, 2)
)

# Managed Objects groups

ruijieNDObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 125, 2, 2, 1)
)
ruijieNDObjectsGroup.setObjects(
      *(("RUIJIE-ND-MIB", "ruijieNDTotalActiveNeighbors"),
        ("RUIJIE-ND-MIB", "ruijieNDTotalActiveDynamicNeighbors"),
        ("RUIJIE-ND-MIB", "ruijieNDTotalStaticNeighbors"),
        ("RUIJIE-ND-MIB", "ruijieNDTotalActiveStaticNeighbors"))
)
if mibBuilder.loadTexts:
    ruijieNDObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieNDMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 125, 2, 1, 1)
)
ruijieNDMIBCompliance.setObjects(
    ("RUIJIE-ND-MIB", "ruijieNDObjectsGroup")
)
if mibBuilder.loadTexts:
    ruijieNDMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ND-MIB",
    **{"ruijieNDMIB": ruijieNDMIB,
       "ruijieNDMIBObjects": ruijieNDMIBObjects,
       "ruijieNDTotalActiveNeighbors": ruijieNDTotalActiveNeighbors,
       "ruijieNDTotalActiveDynamicNeighbors": ruijieNDTotalActiveDynamicNeighbors,
       "ruijieNDTotalStaticNeighbors": ruijieNDTotalStaticNeighbors,
       "ruijieNDTotalActiveStaticNeighbors": ruijieNDTotalActiveStaticNeighbors,
       "ruijieNDMIBConformance": ruijieNDMIBConformance,
       "ruijieNDMIBCompliances": ruijieNDMIBCompliances,
       "ruijieNDMIBCompliance": ruijieNDMIBCompliance,
       "ruijieNDMIBGroups": ruijieNDMIBGroups,
       "ruijieNDObjectsGroup": ruijieNDObjectsGroup}
)
