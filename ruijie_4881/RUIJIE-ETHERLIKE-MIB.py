# SNMP MIB module (RUIJIE-ETHERLIKE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-EHTERLIKE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:21 2025
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

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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

ruijieEtherlikeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 55)
)
if mibBuilder.loadTexts:
    ruijieEtherlikeMIB.setRevisions(
        ("2009-09-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieEtherlikeMIBObjects_ObjectIdentity = ObjectIdentity
ruijieEtherlikeMIBObjects = _RuijieEtherlikeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 55, 1)
)
_RuijieEtherlikeTable_Object = MibTable
ruijieEtherlikeTable = _RuijieEtherlikeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 55, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieEtherlikeTable.setStatus("current")
_RuijieEtherlikeEntry_Object = MibTableRow
ruijieEtherlikeEntry = _RuijieEtherlikeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 55, 1, 1, 1)
)
ruijieEtherlikeEntry.setIndexNames(
    (0, "RUIJIE-ETHERLIKE-MIB", "ruijieEtherlikeIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieEtherlikeEntry.setStatus("current")
_RuijieEtherlikeIfIndex_Type = IfIndex
_RuijieEtherlikeIfIndex_Object = MibTableColumn
ruijieEtherlikeIfIndex = _RuijieEtherlikeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 55, 1, 1, 1, 1),
    _RuijieEtherlikeIfIndex_Type()
)
ruijieEtherlikeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEtherlikeIfIndex.setStatus("current")
_RuijieLocIfCollisions_Type = Counter64
_RuijieLocIfCollisions_Object = MibTableColumn
ruijieLocIfCollisions = _RuijieLocIfCollisions_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 55, 1, 1, 1, 2),
    _RuijieLocIfCollisions_Type()
)
ruijieLocIfCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieLocIfCollisions.setStatus("current")
_RuijieEtherlikeMIBConformance_ObjectIdentity = ObjectIdentity
ruijieEtherlikeMIBConformance = _RuijieEtherlikeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 55, 3)
)
_RuijieEtherlikeMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieEtherlikeMIBCompliances = _RuijieEtherlikeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 55, 3, 1)
)
_RuijieEtherlikeMIBGroups_ObjectIdentity = ObjectIdentity
ruijieEtherlikeMIBGroups = _RuijieEtherlikeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 55, 3, 2)
)

# Managed Objects groups

ruijiecollisionMIBGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 55, 3, 2, 1)
)
ruijiecollisionMIBGroups.setObjects(
      *(("RUIJIE-ETHERLIKE-MIB", "ruijieEtherlikeIfIndex"),
        ("RUIJIE-ETHERLIKE-MIB", "ruijieLocIfCollisions"))
)
if mibBuilder.loadTexts:
    ruijiecollisionMIBGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieEtherlikeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 55, 3, 1, 1)
)
ruijieEtherlikeMIBCompliance.setObjects(
    ("RUIJIE-ETHERLIKE-MIB", "ruijiecollisionMIBGroups")
)
if mibBuilder.loadTexts:
    ruijieEtherlikeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ETHERLIKE-MIB",
    **{"ruijieEtherlikeMIB": ruijieEtherlikeMIB,
       "ruijieEtherlikeMIBObjects": ruijieEtherlikeMIBObjects,
       "ruijieEtherlikeTable": ruijieEtherlikeTable,
       "ruijieEtherlikeEntry": ruijieEtherlikeEntry,
       "ruijieEtherlikeIfIndex": ruijieEtherlikeIfIndex,
       "ruijieLocIfCollisions": ruijieLocIfCollisions,
       "ruijieEtherlikeMIBConformance": ruijieEtherlikeMIBConformance,
       "ruijieEtherlikeMIBCompliances": ruijieEtherlikeMIBCompliances,
       "ruijieEtherlikeMIBCompliance": ruijieEtherlikeMIBCompliance,
       "ruijieEtherlikeMIBGroups": ruijieEtherlikeMIBGroups,
       "ruijiecollisionMIBGroups": ruijiecollisionMIBGroups}
)
