# SNMP MIB module (SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB.mib
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

(heOpticalAmplifierGroup,) = mibBuilder.importSymbols(
    "SCTE-HMS-HE-OPTICS-MIB",
    "heOpticalAmplifierGroup")

(HeLaserType,
 HeMilliAmp,
 HeOnOffControl,
 HeOnOffStatus,
 HeTenthCentigrade,
 HeTenthdB,
 HeTenthdBm) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    "HeLaserType",
    "HeMilliAmp",
    "HeOnOffControl",
    "HeOnOffStatus",
    "HeTenthCentigrade",
    "HeTenthdB",
    "HeTenthdBm")

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

heOpticalAmplifierMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HeOpAmpMIBObjects_ObjectIdentity = ObjectIdentity
heOpAmpMIBObjects = _HeOpAmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1)
)
_HeOpAmpUnitTable_Object = MibTable
heOpAmpUnitTable = _HeOpAmpUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    heOpAmpUnitTable.setStatus("current")
_HeOpAmpUnitEntry_Object = MibTableRow
heOpAmpUnitEntry = _HeOpAmpUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 1, 1)
)
heOpAmpUnitEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    heOpAmpUnitEntry.setStatus("current")
_HeOpAmpUnitOutputStatus_Type = HeOnOffStatus
_HeOpAmpUnitOutputStatus_Object = MibTableColumn
heOpAmpUnitOutputStatus = _HeOpAmpUnitOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 1, 1, 1),
    _HeOpAmpUnitOutputStatus_Type()
)
heOpAmpUnitOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpAmpUnitOutputStatus.setStatus("current")
_HeOpAmpUnitOnOffControl_Type = HeOnOffControl
_HeOpAmpUnitOnOffControl_Object = MibTableColumn
heOpAmpUnitOnOffControl = _HeOpAmpUnitOnOffControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 1, 1, 2),
    _HeOpAmpUnitOnOffControl_Type()
)
heOpAmpUnitOnOffControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpAmpUnitOnOffControl.setStatus("current")
_HeOpAmpInputTable_Object = MibTable
heOpAmpInputTable = _HeOpAmpInputTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    heOpAmpInputTable.setStatus("current")
_HeOpAmpInputEntry_Object = MibTableRow
heOpAmpInputEntry = _HeOpAmpInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 2, 1)
)
heOpAmpInputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpInputIndex"),
)
if mibBuilder.loadTexts:
    heOpAmpInputEntry.setStatus("current")
_HeOpAmpInputIndex_Type = Unsigned32
_HeOpAmpInputIndex_Object = MibTableColumn
heOpAmpInputIndex = _HeOpAmpInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 2, 1, 1),
    _HeOpAmpInputIndex_Type()
)
heOpAmpInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heOpAmpInputIndex.setStatus("current")
_HeOpAmpInputPower_Type = HeTenthdBm
_HeOpAmpInputPower_Object = MibTableColumn
heOpAmpInputPower = _HeOpAmpInputPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 2, 1, 2),
    _HeOpAmpInputPower_Type()
)
heOpAmpInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpAmpInputPower.setStatus("current")
if mibBuilder.loadTexts:
    heOpAmpInputPower.setUnits("0.1 dBm")
_HeOpAmpLaserTable_Object = MibTable
heOpAmpLaserTable = _HeOpAmpLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    heOpAmpLaserTable.setStatus("current")
_HeOpAmpLaserEntry_Object = MibTableRow
heOpAmpLaserEntry = _HeOpAmpLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 3, 1)
)
heOpAmpLaserEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpLaserIndex"),
)
if mibBuilder.loadTexts:
    heOpAmpLaserEntry.setStatus("current")
_HeOpAmpLaserIndex_Type = Unsigned32
_HeOpAmpLaserIndex_Object = MibTableColumn
heOpAmpLaserIndex = _HeOpAmpLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 3, 1, 1),
    _HeOpAmpLaserIndex_Type()
)
heOpAmpLaserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heOpAmpLaserIndex.setStatus("current")
_HeOpAmpLaserTemp_Type = HeTenthCentigrade
_HeOpAmpLaserTemp_Object = MibTableColumn
heOpAmpLaserTemp = _HeOpAmpLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 3, 1, 2),
    _HeOpAmpLaserTemp_Type()
)
heOpAmpLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpAmpLaserTemp.setStatus("current")
if mibBuilder.loadTexts:
    heOpAmpLaserTemp.setUnits("0.1 degrees Celsius")
_HeOpAmpLaserBiasCurrent_Type = HeMilliAmp
_HeOpAmpLaserBiasCurrent_Object = MibTableColumn
heOpAmpLaserBiasCurrent = _HeOpAmpLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 3, 1, 3),
    _HeOpAmpLaserBiasCurrent_Type()
)
heOpAmpLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpAmpLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    heOpAmpLaserBiasCurrent.setUnits("1.0 mA")
_HeOpAmpLaserOutputPower_Type = HeTenthdBm
_HeOpAmpLaserOutputPower_Object = MibTableColumn
heOpAmpLaserOutputPower = _HeOpAmpLaserOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 3, 1, 4),
    _HeOpAmpLaserOutputPower_Type()
)
heOpAmpLaserOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpAmpLaserOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    heOpAmpLaserOutputPower.setUnits("0.1 dBm")
_HeOpAmpLaserTECCurrent_Type = HeMilliAmp
_HeOpAmpLaserTECCurrent_Object = MibTableColumn
heOpAmpLaserTECCurrent = _HeOpAmpLaserTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 3, 1, 5),
    _HeOpAmpLaserTECCurrent_Type()
)
heOpAmpLaserTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpAmpLaserTECCurrent.setStatus("current")
if mibBuilder.loadTexts:
    heOpAmpLaserTECCurrent.setUnits("1.0 mA")
_HeOpAmpLaserType_Type = HeLaserType
_HeOpAmpLaserType_Object = MibTableColumn
heOpAmpLaserType = _HeOpAmpLaserType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 3, 1, 6),
    _HeOpAmpLaserType_Type()
)
heOpAmpLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpAmpLaserType.setStatus("current")
_HeOpAmpOutputTable_Object = MibTable
heOpAmpOutputTable = _HeOpAmpOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    heOpAmpOutputTable.setStatus("current")
_HeOpAmpOutputEntry_Object = MibTableRow
heOpAmpOutputEntry = _HeOpAmpOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 4, 1)
)
heOpAmpOutputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpOutputIndex"),
)
if mibBuilder.loadTexts:
    heOpAmpOutputEntry.setStatus("current")
_HeOpAmpOutputIndex_Type = Unsigned32
_HeOpAmpOutputIndex_Object = MibTableColumn
heOpAmpOutputIndex = _HeOpAmpOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 4, 1, 1),
    _HeOpAmpOutputIndex_Type()
)
heOpAmpOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heOpAmpOutputIndex.setStatus("current")
_HeOpAmpSetOpticalOutputPower_Type = HeTenthdBm
_HeOpAmpSetOpticalOutputPower_Object = MibTableColumn
heOpAmpSetOpticalOutputPower = _HeOpAmpSetOpticalOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 4, 1, 2),
    _HeOpAmpSetOpticalOutputPower_Type()
)
heOpAmpSetOpticalOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpAmpSetOpticalOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    heOpAmpSetOpticalOutputPower.setUnits("0.1 dBm")
_HeOpAmpGainPerWavelength_Type = HeTenthdB
_HeOpAmpGainPerWavelength_Object = MibTableColumn
heOpAmpGainPerWavelength = _HeOpAmpGainPerWavelength_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 4, 1, 3),
    _HeOpAmpGainPerWavelength_Type()
)
heOpAmpGainPerWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpAmpGainPerWavelength.setStatus("current")
if mibBuilder.loadTexts:
    heOpAmpGainPerWavelength.setUnits("0.1 dBm")
_HeOpAmpOutputPower_Type = HeTenthdBm
_HeOpAmpOutputPower_Object = MibTableColumn
heOpAmpOutputPower = _HeOpAmpOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 4, 1, 4),
    _HeOpAmpOutputPower_Type()
)
heOpAmpOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpAmpOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    heOpAmpOutputPower.setUnits("0.1 dBm")


class _HeOpAmpOutputGainType_Type(Integer32):
    """Custom type heOpAmpOutputGainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constantPower", 1),
          ("constantGain", 2))
    )


_HeOpAmpOutputGainType_Type.__name__ = "Integer32"
_HeOpAmpOutputGainType_Object = MibTableColumn
heOpAmpOutputGainType = _HeOpAmpOutputGainType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 1, 4, 1, 5),
    _HeOpAmpOutputGainType_Type()
)
heOpAmpOutputGainType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpAmpOutputGainType.setStatus("current")
_HeOpAmpMIBConformance_ObjectIdentity = ObjectIdentity
heOpAmpMIBConformance = _HeOpAmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 2)
)
_HeOpAmpMIBCompliances_ObjectIdentity = ObjectIdentity
heOpAmpMIBCompliances = _HeOpAmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 2, 1)
)
_HeOpAmpMIBGroups_ObjectIdentity = ObjectIdentity
heOpAmpMIBGroups = _HeOpAmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 2, 2)
)

# Managed Objects groups

heOpAmpUnitMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 2, 2, 1)
)
heOpAmpUnitMandatoryGroup.setObjects(
    ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpUnitOutputStatus")
)
if mibBuilder.loadTexts:
    heOpAmpUnitMandatoryGroup.setStatus("current")

heOpAmpInputMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 2, 2, 2)
)
heOpAmpInputMandatoryGroup.setObjects(
    ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpInputPower")
)
if mibBuilder.loadTexts:
    heOpAmpInputMandatoryGroup.setStatus("current")

heOpAmpOutputMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 2, 2, 3)
)
heOpAmpOutputMandatoryGroup.setObjects(
    ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpOutputPower")
)
if mibBuilder.loadTexts:
    heOpAmpOutputMandatoryGroup.setStatus("current")

heOpAmpUnitTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 2, 2, 4)
)
heOpAmpUnitTableGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpUnitOutputStatus"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpUnitOnOffControl"))
)
if mibBuilder.loadTexts:
    heOpAmpUnitTableGroup.setStatus("current")

heOpAmpInputTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 2, 2, 5)
)
heOpAmpInputTableGroup.setObjects(
    ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpInputPower")
)
if mibBuilder.loadTexts:
    heOpAmpInputTableGroup.setStatus("current")

heOpAmpLaserTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 2, 2, 6)
)
heOpAmpLaserTableGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpLaserTemp"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpLaserBiasCurrent"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpLaserOutputPower"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpLaserTECCurrent"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpLaserType"))
)
if mibBuilder.loadTexts:
    heOpAmpLaserTableGroup.setStatus("current")

heOpAmpOutputTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 2, 2, 7)
)
heOpAmpOutputTableGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpSetOpticalOutputPower"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpGainPerWavelength"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpOutputPower"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpOutputGainType"))
)
if mibBuilder.loadTexts:
    heOpAmpOutputTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

heOpAmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 3, 1, 2, 1, 1)
)
heOpAmpCompliance.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpUnitMandatoryGroup"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpInputMandatoryGroup"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpOutputMandatoryGroup"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpUnitTableGroup"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpInputTableGroup"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpLaserTableGroup"),
        ("SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB", "heOpAmpOutputTableGroup"))
)
if mibBuilder.loadTexts:
    heOpAmpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB",
    **{"heOpticalAmplifierMIB": heOpticalAmplifierMIB,
       "heOpAmpMIBObjects": heOpAmpMIBObjects,
       "heOpAmpUnitTable": heOpAmpUnitTable,
       "heOpAmpUnitEntry": heOpAmpUnitEntry,
       "heOpAmpUnitOutputStatus": heOpAmpUnitOutputStatus,
       "heOpAmpUnitOnOffControl": heOpAmpUnitOnOffControl,
       "heOpAmpInputTable": heOpAmpInputTable,
       "heOpAmpInputEntry": heOpAmpInputEntry,
       "heOpAmpInputIndex": heOpAmpInputIndex,
       "heOpAmpInputPower": heOpAmpInputPower,
       "heOpAmpLaserTable": heOpAmpLaserTable,
       "heOpAmpLaserEntry": heOpAmpLaserEntry,
       "heOpAmpLaserIndex": heOpAmpLaserIndex,
       "heOpAmpLaserTemp": heOpAmpLaserTemp,
       "heOpAmpLaserBiasCurrent": heOpAmpLaserBiasCurrent,
       "heOpAmpLaserOutputPower": heOpAmpLaserOutputPower,
       "heOpAmpLaserTECCurrent": heOpAmpLaserTECCurrent,
       "heOpAmpLaserType": heOpAmpLaserType,
       "heOpAmpOutputTable": heOpAmpOutputTable,
       "heOpAmpOutputEntry": heOpAmpOutputEntry,
       "heOpAmpOutputIndex": heOpAmpOutputIndex,
       "heOpAmpSetOpticalOutputPower": heOpAmpSetOpticalOutputPower,
       "heOpAmpGainPerWavelength": heOpAmpGainPerWavelength,
       "heOpAmpOutputPower": heOpAmpOutputPower,
       "heOpAmpOutputGainType": heOpAmpOutputGainType,
       "heOpAmpMIBConformance": heOpAmpMIBConformance,
       "heOpAmpMIBCompliances": heOpAmpMIBCompliances,
       "heOpAmpCompliance": heOpAmpCompliance,
       "heOpAmpMIBGroups": heOpAmpMIBGroups,
       "heOpAmpUnitMandatoryGroup": heOpAmpUnitMandatoryGroup,
       "heOpAmpInputMandatoryGroup": heOpAmpInputMandatoryGroup,
       "heOpAmpOutputMandatoryGroup": heOpAmpOutputMandatoryGroup,
       "heOpAmpUnitTableGroup": heOpAmpUnitTableGroup,
       "heOpAmpInputTableGroup": heOpAmpInputTableGroup,
       "heOpAmpLaserTableGroup": heOpAmpLaserTableGroup,
       "heOpAmpOutputTableGroup": heOpAmpOutputTableGroup}
)
