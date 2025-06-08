# SNMP MIB module (BELAIR-PHYIF-MAPPING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-PHYIF-MAPPING.mib
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

(belairGeneric,) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairGeneric")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

belairPhyIfMappingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 3)
)
if mibBuilder.loadTexts:
    belairPhyIfMappingMib.setRevisions(
        ("2007-05-30 16:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BelairPhyMappingObjects_ObjectIdentity = ObjectIdentity
belairPhyMappingObjects = _BelairPhyMappingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 3, 1)
)
_BelairPhyIfMappingTable_Object = MibTable
belairPhyIfMappingTable = _BelairPhyIfMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    belairPhyIfMappingTable.setStatus("current")
_BelairPhyIfMappingEntry_Object = MibTableRow
belairPhyIfMappingEntry = _BelairPhyIfMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 3, 1, 1, 1)
)
belairPhyIfMappingEntry.setIndexNames(
    (0, "BELAIR-PHYIF-MAPPING", "belairPhyIfSlot"),
    (0, "BELAIR-PHYIF-MAPPING", "belairPhyIfPort"),
    (0, "BELAIR-PHYIF-MAPPING", "belairPhyIfSubPort"),
)
if mibBuilder.loadTexts:
    belairPhyIfMappingEntry.setStatus("current")


class _BelairPhyIfSlot_Type(Integer32):
    """Custom type belairPhyIfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BelairPhyIfSlot_Type.__name__ = "Integer32"
_BelairPhyIfSlot_Object = MibTableColumn
belairPhyIfSlot = _BelairPhyIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 3, 1, 1, 1, 1),
    _BelairPhyIfSlot_Type()
)
belairPhyIfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairPhyIfSlot.setStatus("current")


class _BelairPhyIfPort_Type(Integer32):
    """Custom type belairPhyIfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BelairPhyIfPort_Type.__name__ = "Integer32"
_BelairPhyIfPort_Object = MibTableColumn
belairPhyIfPort = _BelairPhyIfPort_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 3, 1, 1, 1, 2),
    _BelairPhyIfPort_Type()
)
belairPhyIfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairPhyIfPort.setStatus("current")


class _BelairPhyIfSubPort_Type(Integer32):
    """Custom type belairPhyIfSubPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_BelairPhyIfSubPort_Type.__name__ = "Integer32"
_BelairPhyIfSubPort_Object = MibTableColumn
belairPhyIfSubPort = _BelairPhyIfSubPort_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 3, 1, 1, 1, 3),
    _BelairPhyIfSubPort_Type()
)
belairPhyIfSubPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairPhyIfSubPort.setStatus("current")
_BelairPhyIfIndex_Type = InterfaceIndex
_BelairPhyIfIndex_Object = MibTableColumn
belairPhyIfIndex = _BelairPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 3, 1, 1, 1, 4),
    _BelairPhyIfIndex_Type()
)
belairPhyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairPhyIfIndex.setStatus("current")
_BelairPhyMappingTraps_ObjectIdentity = ObjectIdentity
belairPhyMappingTraps = _BelairPhyMappingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 3, 2)
)
_BelairPhyMappingConformance_ObjectIdentity = ObjectIdentity
belairPhyMappingConformance = _BelairPhyMappingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 3, 3)
)

# Managed Objects groups

belairPhyIfMappingObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 3, 3, 3, 1)
)
belairPhyIfMappingObjGroup.setObjects(
    ("BELAIR-PHYIF-MAPPING", "belairPhyIfIndex")
)
if mibBuilder.loadTexts:
    belairPhyIfMappingObjGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-PHYIF-MAPPING",
    **{"belairPhyIfMappingMib": belairPhyIfMappingMib,
       "belairPhyMappingObjects": belairPhyMappingObjects,
       "belairPhyIfMappingTable": belairPhyIfMappingTable,
       "belairPhyIfMappingEntry": belairPhyIfMappingEntry,
       "belairPhyIfSlot": belairPhyIfSlot,
       "belairPhyIfPort": belairPhyIfPort,
       "belairPhyIfSubPort": belairPhyIfSubPort,
       "belairPhyIfIndex": belairPhyIfIndex,
       "belairPhyMappingTraps": belairPhyMappingTraps,
       "belairPhyMappingConformance": belairPhyMappingConformance,
       "belairPhyIfMappingObjGroup": belairPhyIfMappingObjGroup}
)
