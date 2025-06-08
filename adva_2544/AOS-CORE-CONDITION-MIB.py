# SNMP MIB module (AOS-CORE-CONDITION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/AOS-CORE-CONDITION-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:56 2025
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

(aosCommon,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "aosCommon")

(ConditionDescr,
 ConditionEntityTranslation,
 ConditionType) = mibBuilder.importSymbols(
    "AOS-CORE-ALARM-MIB",
    "ConditionDescr",
    "ConditionEntityTranslation",
    "ConditionType")

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
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

aosCoreConditionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2)
)
if mibBuilder.loadTexts:
    aosCoreConditionMIB.setRevisions(
        ("2015-10-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ConditionObjects_ObjectIdentity = ObjectIdentity
conditionObjects = _ConditionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1)
)
_AosCoreConditionTable_Object = MibTable
aosCoreConditionTable = _AosCoreConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aosCoreConditionTable.setStatus("current")
_AosCoreConditionEntry_Object = MibTableRow
aosCoreConditionEntry = _AosCoreConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1)
)
aosCoreConditionEntry.setIndexNames(
    (0, "AOS-CORE-CONDITION-MIB", "aosCoreConditionIndex"),
)
if mibBuilder.loadTexts:
    aosCoreConditionEntry.setStatus("current")
_AosCoreConditionIndex_Type = Integer32
_AosCoreConditionIndex_Object = MibTableColumn
aosCoreConditionIndex = _AosCoreConditionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1, 1),
    _AosCoreConditionIndex_Type()
)
aosCoreConditionIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aosCoreConditionIndex.setStatus("current")
_AosCoreConditionType_Type = ConditionType
_AosCoreConditionType_Object = MibTableColumn
aosCoreConditionType = _AosCoreConditionType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1, 2),
    _AosCoreConditionType_Type()
)
aosCoreConditionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreConditionType.setStatus("current")
_AosCoreConditionEntityTranslation_Type = ConditionEntityTranslation
_AosCoreConditionEntityTranslation_Object = MibTableColumn
aosCoreConditionEntityTranslation = _AosCoreConditionEntityTranslation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1, 3),
    _AosCoreConditionEntityTranslation_Type()
)
aosCoreConditionEntityTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreConditionEntityTranslation.setStatus("current")
_AosCoreConditionEntity_Type = RowPointer
_AosCoreConditionEntity_Object = MibTableColumn
aosCoreConditionEntity = _AosCoreConditionEntity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1, 4),
    _AosCoreConditionEntity_Type()
)
aosCoreConditionEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreConditionEntity.setStatus("current")
_AosCoreConditionDescr_Type = ConditionDescr
_AosCoreConditionDescr_Object = MibTableColumn
aosCoreConditionDescr = _AosCoreConditionDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1, 5),
    _AosCoreConditionDescr_Type()
)
aosCoreConditionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreConditionDescr.setStatus("current")
_AosCoreConditionTimestamp_Type = DisplayString
_AosCoreConditionTimestamp_Object = MibTableColumn
aosCoreConditionTimestamp = _AosCoreConditionTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1, 6),
    _AosCoreConditionTimestamp_Type()
)
aosCoreConditionTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreConditionTimestamp.setStatus("current")
_ConditionConformance_ObjectIdentity = ObjectIdentity
conditionConformance = _ConditionConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 2)
)
_AosCoreConditionCompliances_ObjectIdentity = ObjectIdentity
aosCoreConditionCompliances = _AosCoreConditionCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 2, 1)
)
_AosCoreConditionGroups_ObjectIdentity = ObjectIdentity
aosCoreConditionGroups = _AosCoreConditionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 2, 2)
)

# Managed Objects groups

aosCoreConditionObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 2, 2, 1)
)
aosCoreConditionObjectGroup.setObjects(
      *(("AOS-CORE-CONDITION-MIB", "aosCoreConditionIndex"),
        ("AOS-CORE-CONDITION-MIB", "aosCoreConditionType"),
        ("AOS-CORE-CONDITION-MIB", "aosCoreConditionEntityTranslation"),
        ("AOS-CORE-CONDITION-MIB", "aosCoreConditionEntity"),
        ("AOS-CORE-CONDITION-MIB", "aosCoreConditionDescr"),
        ("AOS-CORE-CONDITION-MIB", "aosCoreConditionTimestamp"))
)
if mibBuilder.loadTexts:
    aosCoreConditionObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aosCoreConditionCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 2, 1, 1)
)
aosCoreConditionCompliance.setObjects(
    ("AOS-CORE-CONDITION-MIB", "aosCoreConditionObjectGroup")
)
if mibBuilder.loadTexts:
    aosCoreConditionCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AOS-CORE-CONDITION-MIB",
    **{"aosCoreConditionMIB": aosCoreConditionMIB,
       "conditionObjects": conditionObjects,
       "aosCoreConditionTable": aosCoreConditionTable,
       "aosCoreConditionEntry": aosCoreConditionEntry,
       "aosCoreConditionIndex": aosCoreConditionIndex,
       "aosCoreConditionType": aosCoreConditionType,
       "aosCoreConditionEntityTranslation": aosCoreConditionEntityTranslation,
       "aosCoreConditionEntity": aosCoreConditionEntity,
       "aosCoreConditionDescr": aosCoreConditionDescr,
       "aosCoreConditionTimestamp": aosCoreConditionTimestamp,
       "conditionConformance": conditionConformance,
       "aosCoreConditionCompliances": aosCoreConditionCompliances,
       "aosCoreConditionCompliance": aosCoreConditionCompliance,
       "aosCoreConditionGroups": aosCoreConditionGroups,
       "aosCoreConditionObjectGroup": aosCoreConditionObjectGroup}
)
