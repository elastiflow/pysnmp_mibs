# SNMP MIB module (SCTE-HMS-HE-RF-AMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HE-RF-AMP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:31:48 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(heRFAmplifierGroup,) = mibBuilder.importSymbols(
    "SCTE-HMS-HE-RF-MIB",
    "heRFAmplifierGroup")

(HeTenthdB,
 HeTenthdBmV) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    "HeTenthdB",
    "HeTenthdBmV")

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

heRFAmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HeRFAmpMIBObjects_ObjectIdentity = ObjectIdentity
heRFAmpMIBObjects = _HeRFAmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 1)
)
_HeRFAmpUnitTable_Object = MibTable
heRFAmpUnitTable = _HeRFAmpUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    heRFAmpUnitTable.setStatus("current")
_HeRFAmpUnitEntry_Object = MibTableRow
heRFAmpUnitEntry = _HeRFAmpUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 1, 1, 1)
)
heRFAmpUnitEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    heRFAmpUnitEntry.setStatus("current")


class _HeRFAmpGainControlMode_Type(Integer32):
    """Custom type heRFAmpGainControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("alc", 2),
          ("asc", 3),
          ("agc", 4),
          ("alsc", 5))
    )


_HeRFAmpGainControlMode_Type.__name__ = "Integer32"
_HeRFAmpGainControlMode_Object = MibTableColumn
heRFAmpGainControlMode = _HeRFAmpGainControlMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 1, 1, 1, 1),
    _HeRFAmpGainControlMode_Type()
)
heRFAmpGainControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heRFAmpGainControlMode.setStatus("current")
_HeRFAmpAttenuatorControl_Type = HeTenthdB
_HeRFAmpAttenuatorControl_Object = MibTableColumn
heRFAmpAttenuatorControl = _HeRFAmpAttenuatorControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 1, 1, 1, 2),
    _HeRFAmpAttenuatorControl_Type()
)
heRFAmpAttenuatorControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heRFAmpAttenuatorControl.setStatus("current")
_HeRFAmpSlopeControl_Type = HeTenthdB
_HeRFAmpSlopeControl_Object = MibTableColumn
heRFAmpSlopeControl = _HeRFAmpSlopeControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 1, 1, 1, 3),
    _HeRFAmpSlopeControl_Type()
)
heRFAmpSlopeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heRFAmpSlopeControl.setStatus("current")
_HeRFAmpOutputTable_Object = MibTable
heRFAmpOutputTable = _HeRFAmpOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    heRFAmpOutputTable.setStatus("current")
_HeRFAmpOutputEntry_Object = MibTableRow
heRFAmpOutputEntry = _HeRFAmpOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 1, 2, 1)
)
heRFAmpOutputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-RF-AMP-MIB", "heRFAmpOutputIndex"),
)
if mibBuilder.loadTexts:
    heRFAmpOutputEntry.setStatus("current")
_HeRFAmpOutputIndex_Type = Unsigned32
_HeRFAmpOutputIndex_Object = MibTableColumn
heRFAmpOutputIndex = _HeRFAmpOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 1, 2, 1, 1),
    _HeRFAmpOutputIndex_Type()
)
heRFAmpOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heRFAmpOutputIndex.setStatus("current")


class _HeRFAmpOutputDescription_Type(DisplayString):
    """Custom type heRFAmpOutputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HeRFAmpOutputDescription_Type.__name__ = "DisplayString"
_HeRFAmpOutputDescription_Object = MibTableColumn
heRFAmpOutputDescription = _HeRFAmpOutputDescription_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 1, 2, 1, 2),
    _HeRFAmpOutputDescription_Type()
)
heRFAmpOutputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heRFAmpOutputDescription.setStatus("current")
_HeRFAmpOutputLevel_Type = HeTenthdBmV
_HeRFAmpOutputLevel_Object = MibTableColumn
heRFAmpOutputLevel = _HeRFAmpOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 1, 2, 1, 3),
    _HeRFAmpOutputLevel_Type()
)
heRFAmpOutputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heRFAmpOutputLevel.setStatus("current")
_HeRFAmpOutputAttenuatorControl_Type = HeTenthdB
_HeRFAmpOutputAttenuatorControl_Object = MibTableColumn
heRFAmpOutputAttenuatorControl = _HeRFAmpOutputAttenuatorControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 1, 2, 1, 4),
    _HeRFAmpOutputAttenuatorControl_Type()
)
heRFAmpOutputAttenuatorControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heRFAmpOutputAttenuatorControl.setStatus("current")
_HeRFAmpMIBConformance_ObjectIdentity = ObjectIdentity
heRFAmpMIBConformance = _HeRFAmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 2)
)
_HeRFAmpMIBCompliances_ObjectIdentity = ObjectIdentity
heRFAmpMIBCompliances = _HeRFAmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 2, 1)
)
_HeRFAmpMIBGroups_ObjectIdentity = ObjectIdentity
heRFAmpMIBGroups = _HeRFAmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 2, 2)
)

# Managed Objects groups

heRFAmpOutputMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 2, 2, 1)
)
heRFAmpOutputMandatoryGroup.setObjects(
    ("SCTE-HMS-HE-RF-AMP-MIB", "heRFAmpOutputDescription")
)
if mibBuilder.loadTexts:
    heRFAmpOutputMandatoryGroup.setStatus("current")

heRFAmpUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 2, 2, 2)
)
heRFAmpUnitGroup.setObjects(
      *(("SCTE-HMS-HE-RF-AMP-MIB", "heRFAmpGainControlMode"),
        ("SCTE-HMS-HE-RF-AMP-MIB", "heRFAmpAttenuatorControl"),
        ("SCTE-HMS-HE-RF-AMP-MIB", "heRFAmpSlopeControl"))
)
if mibBuilder.loadTexts:
    heRFAmpUnitGroup.setStatus("current")

heRFAmpOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 2, 2, 3)
)
heRFAmpOutputGroup.setObjects(
      *(("SCTE-HMS-HE-RF-AMP-MIB", "heRFAmpOutputLevel"),
        ("SCTE-HMS-HE-RF-AMP-MIB", "heRFAmpOutputAttenuatorControl"))
)
if mibBuilder.loadTexts:
    heRFAmpOutputGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

heRFAmpBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 1, 1, 2, 1, 1)
)
heRFAmpBasicCompliance.setObjects(
    ("SCTE-HMS-HE-RF-AMP-MIB", "heRFAmpOutputMandatoryGroup")
)
if mibBuilder.loadTexts:
    heRFAmpBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HE-RF-AMP-MIB",
    **{"heRFAmpMIB": heRFAmpMIB,
       "heRFAmpMIBObjects": heRFAmpMIBObjects,
       "heRFAmpUnitTable": heRFAmpUnitTable,
       "heRFAmpUnitEntry": heRFAmpUnitEntry,
       "heRFAmpGainControlMode": heRFAmpGainControlMode,
       "heRFAmpAttenuatorControl": heRFAmpAttenuatorControl,
       "heRFAmpSlopeControl": heRFAmpSlopeControl,
       "heRFAmpOutputTable": heRFAmpOutputTable,
       "heRFAmpOutputEntry": heRFAmpOutputEntry,
       "heRFAmpOutputIndex": heRFAmpOutputIndex,
       "heRFAmpOutputDescription": heRFAmpOutputDescription,
       "heRFAmpOutputLevel": heRFAmpOutputLevel,
       "heRFAmpOutputAttenuatorControl": heRFAmpOutputAttenuatorControl,
       "heRFAmpMIBConformance": heRFAmpMIBConformance,
       "heRFAmpMIBCompliances": heRFAmpMIBCompliances,
       "heRFAmpBasicCompliance": heRFAmpBasicCompliance,
       "heRFAmpMIBGroups": heRFAmpMIBGroups,
       "heRFAmpOutputMandatoryGroup": heRFAmpOutputMandatoryGroup,
       "heRFAmpUnitGroup": heRFAmpUnitGroup,
       "heRFAmpOutputGroup": heRFAmpOutputGroup}
)
