# SNMP MIB module (A3COM-HUAWEI-ENTRELATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-ENTRELATION-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:04:11 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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

h3cEntityRelation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cEntRelationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stackport", 1),
          ("comboport", 2))
    )



# MIB Managed Objects in the order of their OIDs

_H3cEntRelationObjects_ObjectIdentity = ObjectIdentity
h3cEntRelationObjects = _H3cEntRelationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1)
)
_H3cEntRelation_ObjectIdentity = ObjectIdentity
h3cEntRelation = _H3cEntRelation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1)
)
_H3cEntRelationTable_Object = MibTable
h3cEntRelationTable = _H3cEntRelationTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cEntRelationTable.setStatus("current")
_H3cEntRelationEntry_Object = MibTableRow
h3cEntRelationEntry = _H3cEntRelationEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1, 1)
)
h3cEntRelationEntry.setIndexNames(
    (0, "A3COM-HUAWEI-ENTRELATION-MIB", "h3cEntRelationType"),
    (0, "A3COM-HUAWEI-ENTRELATION-MIB", "h3cEntityIndex"),
    (0, "A3COM-HUAWEI-ENTRELATION-MIB", "h3cRelatedEntityIndex"),
)
if mibBuilder.loadTexts:
    h3cEntRelationEntry.setStatus("current")
_H3cEntRelationType_Type = H3cEntRelationType
_H3cEntRelationType_Object = MibTableColumn
h3cEntRelationType = _H3cEntRelationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1, 1, 1),
    _H3cEntRelationType_Type()
)
h3cEntRelationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEntRelationType.setStatus("current")
_H3cEntityIndex_Type = PhysicalIndex
_H3cEntityIndex_Object = MibTableColumn
h3cEntityIndex = _H3cEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1, 1, 2),
    _H3cEntityIndex_Type()
)
h3cEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEntityIndex.setStatus("current")
_H3cRelatedEntityIndex_Type = PhysicalIndex
_H3cRelatedEntityIndex_Object = MibTableColumn
h3cRelatedEntityIndex = _H3cRelatedEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 1, 1, 1, 1, 3),
    _H3cRelatedEntityIndex_Type()
)
h3cRelatedEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRelatedEntityIndex.setStatus("current")
_H3cEntRelationConformance_ObjectIdentity = ObjectIdentity
h3cEntRelationConformance = _H3cEntRelationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2)
)
_H3cEntRelationCompliances_ObjectIdentity = ObjectIdentity
h3cEntRelationCompliances = _H3cEntRelationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2, 1)
)
_H3cEntRelationGroups_ObjectIdentity = ObjectIdentity
h3cEntRelationGroups = _H3cEntRelationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2, 2)
)

# Managed Objects groups

h3cEntRelationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2, 2, 1)
)
h3cEntRelationGroup.setObjects(
    ("A3COM-HUAWEI-ENTRELATION-MIB", "h3cRelatedEntityIndex")
)
if mibBuilder.loadTexts:
    h3cEntRelationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h3cEntRelationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 15, 2, 1, 1)
)
h3cEntRelationCompliance.setObjects(
    ("A3COM-HUAWEI-ENTRELATION-MIB", "h3cEntRelationGroup")
)
if mibBuilder.loadTexts:
    h3cEntRelationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-ENTRELATION-MIB",
    **{"H3cEntRelationType": H3cEntRelationType,
       "h3cEntityRelation": h3cEntityRelation,
       "h3cEntRelationObjects": h3cEntRelationObjects,
       "h3cEntRelation": h3cEntRelation,
       "h3cEntRelationTable": h3cEntRelationTable,
       "h3cEntRelationEntry": h3cEntRelationEntry,
       "h3cEntRelationType": h3cEntRelationType,
       "h3cEntityIndex": h3cEntityIndex,
       "h3cRelatedEntityIndex": h3cRelatedEntityIndex,
       "h3cEntRelationConformance": h3cEntRelationConformance,
       "h3cEntRelationCompliances": h3cEntRelationCompliances,
       "h3cEntRelationCompliance": h3cEntRelationCompliance,
       "h3cEntRelationGroups": h3cEntRelationGroups,
       "h3cEntRelationGroup": h3cEntRelationGroup}
)
