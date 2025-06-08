# SNMP MIB module (SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB.mib
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

(heOpticalTransmitterGroup,) = mibBuilder.importSymbols(
    "SCTE-HMS-HE-OPTICS-MIB",
    "heOpticalTransmitterGroup")

(HeHundredthNanoMeter,
 HeLaserType,
 HeOnOffControl,
 HeOnOffStatus,
 HeTenthCentigrade,
 HeTenthVolt,
 HeTenthdB,
 HeTenthdBm) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    "HeHundredthNanoMeter",
    "HeLaserType",
    "HeOnOffControl",
    "HeOnOffStatus",
    "HeTenthCentigrade",
    "HeTenthVolt",
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

heOpticalTransmitterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HeOpTxMIBObjects_ObjectIdentity = ObjectIdentity
heOpTxMIBObjects = _HeOpTxMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1)
)
_HeOpTxUnitTable_Object = MibTable
heOpTxUnitTable = _HeOpTxUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    heOpTxUnitTable.setStatus("current")
_HeOpTxUnitEntry_Object = MibTableRow
heOpTxUnitEntry = _HeOpTxUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 1, 1)
)
heOpTxUnitEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    heOpTxUnitEntry.setStatus("current")
_HeOpTxUnitOutputStatus_Type = HeOnOffStatus
_HeOpTxUnitOutputStatus_Object = MibTableColumn
heOpTxUnitOutputStatus = _HeOpTxUnitOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 1, 1, 1),
    _HeOpTxUnitOutputStatus_Type()
)
heOpTxUnitOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpTxUnitOutputStatus.setStatus("current")
_HeOpTxUnitOnOffControl_Type = HeOnOffControl
_HeOpTxUnitOnOffControl_Object = MibTableColumn
heOpTxUnitOnOffControl = _HeOpTxUnitOnOffControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 1, 1, 2),
    _HeOpTxUnitOnOffControl_Type()
)
heOpTxUnitOnOffControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpTxUnitOnOffControl.setStatus("current")
_HeOpTxInputTable_Object = MibTable
heOpTxInputTable = _HeOpTxInputTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    heOpTxInputTable.setStatus("current")
_HeOpTxInputEntry_Object = MibTableRow
heOpTxInputEntry = _HeOpTxInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 2, 1)
)
heOpTxInputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxInputIndex"),
)
if mibBuilder.loadTexts:
    heOpTxInputEntry.setStatus("current")
_HeOpTxInputIndex_Type = Unsigned32
_HeOpTxInputIndex_Object = MibTableColumn
heOpTxInputIndex = _HeOpTxInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 2, 1, 1),
    _HeOpTxInputIndex_Type()
)
heOpTxInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heOpTxInputIndex.setStatus("current")
_HeOpTxInputRFPower_Type = HeTenthdBm
_HeOpTxInputRFPower_Object = MibTableColumn
heOpTxInputRFPower = _HeOpTxInputRFPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 2, 1, 2),
    _HeOpTxInputRFPower_Type()
)
heOpTxInputRFPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpTxInputRFPower.setStatus("current")
if mibBuilder.loadTexts:
    heOpTxInputRFPower.setUnits("0.1 dBm")
_HeOpTxInputModulatorBias_Type = HeTenthVolt
_HeOpTxInputModulatorBias_Object = MibTableColumn
heOpTxInputModulatorBias = _HeOpTxInputModulatorBias_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 2, 1, 3),
    _HeOpTxInputModulatorBias_Type()
)
heOpTxInputModulatorBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpTxInputModulatorBias.setStatus("current")
if mibBuilder.loadTexts:
    heOpTxInputModulatorBias.setUnits("0.1 Volt")
_HeOpTxInputAGCMode_Type = HeOnOffStatus
_HeOpTxInputAGCMode_Object = MibTableColumn
heOpTxInputAGCMode = _HeOpTxInputAGCMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 2, 1, 4),
    _HeOpTxInputAGCMode_Type()
)
heOpTxInputAGCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpTxInputAGCMode.setStatus("current")


class _HeOpTxInputModulationMode_Type(Integer32):
    """Custom type heOpTxInputModulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cw", 1),
          ("modulated", 2))
    )


_HeOpTxInputModulationMode_Type.__name__ = "Integer32"
_HeOpTxInputModulationMode_Object = MibTableColumn
heOpTxInputModulationMode = _HeOpTxInputModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 2, 1, 5),
    _HeOpTxInputModulationMode_Type()
)
heOpTxInputModulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpTxInputModulationMode.setStatus("current")
_HeOpTxInputRFPadLevel_Type = HeTenthdB
_HeOpTxInputRFPadLevel_Object = MibTableColumn
heOpTxInputRFPadLevel = _HeOpTxInputRFPadLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 2, 1, 6),
    _HeOpTxInputRFPadLevel_Type()
)
heOpTxInputRFPadLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpTxInputRFPadLevel.setStatus("current")
if mibBuilder.loadTexts:
    heOpTxInputRFPadLevel.setUnits("0.1 dB")
_HeOpTxLaserTable_Object = MibTable
heOpTxLaserTable = _HeOpTxLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    heOpTxLaserTable.setStatus("current")
_HeOpTxLaserEntry_Object = MibTableRow
heOpTxLaserEntry = _HeOpTxLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 3, 1)
)
heOpTxLaserEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserIndex"),
)
if mibBuilder.loadTexts:
    heOpTxLaserEntry.setStatus("current")
_HeOpTxLaserIndex_Type = Unsigned32
_HeOpTxLaserIndex_Object = MibTableColumn
heOpTxLaserIndex = _HeOpTxLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 3, 1, 1),
    _HeOpTxLaserIndex_Type()
)
heOpTxLaserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heOpTxLaserIndex.setStatus("current")


class _HeOpTxLaserTemp_Type(HeTenthCentigrade):
    """Custom type heOpTxLaserTemp based on HeTenthCentigrade"""
    subtypeSpec = HeTenthCentigrade.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, 1000),
    )


_HeOpTxLaserTemp_Type.__name__ = "HeTenthCentigrade"
_HeOpTxLaserTemp_Object = MibTableColumn
heOpTxLaserTemp = _HeOpTxLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 3, 1, 2),
    _HeOpTxLaserTemp_Type()
)
heOpTxLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpTxLaserTemp.setStatus("current")
if mibBuilder.loadTexts:
    heOpTxLaserTemp.setUnits("0.1 degrees Celsius")


class _HeOpTxLaserBiasCurrent_Type(Integer32):
    """Custom type heOpTxLaserBiasCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HeOpTxLaserBiasCurrent_Type.__name__ = "Integer32"
_HeOpTxLaserBiasCurrent_Object = MibTableColumn
heOpTxLaserBiasCurrent = _HeOpTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 3, 1, 3),
    _HeOpTxLaserBiasCurrent_Type()
)
heOpTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    heOpTxLaserBiasCurrent.setUnits("milli Amperes")
_HeOpTxLaserOutputPower_Type = HeTenthdBm
_HeOpTxLaserOutputPower_Object = MibTableColumn
heOpTxLaserOutputPower = _HeOpTxLaserOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 3, 1, 4),
    _HeOpTxLaserOutputPower_Type()
)
heOpTxLaserOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpTxLaserOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    heOpTxLaserOutputPower.setUnits("0.1 dBm")
_HeOpTxLaserTECCurrent_Type = Integer32
_HeOpTxLaserTECCurrent_Object = MibTableColumn
heOpTxLaserTECCurrent = _HeOpTxLaserTECCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 3, 1, 5),
    _HeOpTxLaserTECCurrent_Type()
)
heOpTxLaserTECCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpTxLaserTECCurrent.setStatus("current")
if mibBuilder.loadTexts:
    heOpTxLaserTECCurrent.setUnits("milli Amperes")
_HeOpTxLaserType_Type = HeLaserType
_HeOpTxLaserType_Object = MibTableColumn
heOpTxLaserType = _HeOpTxLaserType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 3, 1, 6),
    _HeOpTxLaserType_Type()
)
heOpTxLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpTxLaserType.setStatus("current")
_HeOpTxLaserWavelength_Type = HeHundredthNanoMeter
_HeOpTxLaserWavelength_Object = MibTableColumn
heOpTxLaserWavelength = _HeOpTxLaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 3, 1, 7),
    _HeOpTxLaserWavelength_Type()
)
heOpTxLaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpTxLaserWavelength.setStatus("current")
if mibBuilder.loadTexts:
    heOpTxLaserWavelength.setUnits("0.01 nanometer")
_HeOpTxLaserOutputStatus_Type = HeOnOffStatus
_HeOpTxLaserOutputStatus_Object = MibTableColumn
heOpTxLaserOutputStatus = _HeOpTxLaserOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 3, 1, 8),
    _HeOpTxLaserOutputStatus_Type()
)
heOpTxLaserOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpTxLaserOutputStatus.setStatus("current")
_HeOpTxLaserOnOffControl_Type = HeOnOffControl
_HeOpTxLaserOnOffControl_Object = MibTableColumn
heOpTxLaserOnOffControl = _HeOpTxLaserOnOffControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 1, 3, 1, 9),
    _HeOpTxLaserOnOffControl_Type()
)
heOpTxLaserOnOffControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpTxLaserOnOffControl.setStatus("current")
_HeOpTxMIBConformance_ObjectIdentity = ObjectIdentity
heOpTxMIBConformance = _HeOpTxMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 2)
)
_HeOpTxMIBCompliances_ObjectIdentity = ObjectIdentity
heOpTxMIBCompliances = _HeOpTxMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 2, 1)
)
_HeOpTxMIBGroups_ObjectIdentity = ObjectIdentity
heOpTxMIBGroups = _HeOpTxMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 2, 2)
)

# Managed Objects groups

heOpTxUnitMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 2, 2, 1)
)
heOpTxUnitMandatoryGroup.setObjects(
    ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxUnitOutputStatus")
)
if mibBuilder.loadTexts:
    heOpTxUnitMandatoryGroup.setStatus("current")

heOpTxLaserMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 2, 2, 2)
)
heOpTxLaserMandatoryGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserType"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserWavelength"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserOutputStatus"))
)
if mibBuilder.loadTexts:
    heOpTxLaserMandatoryGroup.setStatus("current")

heOpTxUnitTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 2, 2, 3)
)
heOpTxUnitTableGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxUnitOutputStatus"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxUnitOnOffControl"))
)
if mibBuilder.loadTexts:
    heOpTxUnitTableGroup.setStatus("current")

heOpTxInputTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 2, 2, 4)
)
heOpTxInputTableGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxInputRFPower"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxInputModulatorBias"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxInputAGCMode"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxInputModulationMode"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxInputRFPadLevel"))
)
if mibBuilder.loadTexts:
    heOpTxInputTableGroup.setStatus("current")

heOpTxLaserTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 2, 2, 5)
)
heOpTxLaserTableGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserTemp"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserBiasCurrent"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserOutputPower"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserTECCurrent"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserType"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserWavelength"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserOutputStatus"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserOnOffControl"))
)
if mibBuilder.loadTexts:
    heOpTxLaserTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

heOpTxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 1, 1, 2, 1, 1)
)
heOpTxCompliance.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxUnitMandatoryGroup"),
        ("SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB", "heOpTxLaserMandatoryGroup"))
)
if mibBuilder.loadTexts:
    heOpTxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB",
    **{"heOpticalTransmitterMIB": heOpticalTransmitterMIB,
       "heOpTxMIBObjects": heOpTxMIBObjects,
       "heOpTxUnitTable": heOpTxUnitTable,
       "heOpTxUnitEntry": heOpTxUnitEntry,
       "heOpTxUnitOutputStatus": heOpTxUnitOutputStatus,
       "heOpTxUnitOnOffControl": heOpTxUnitOnOffControl,
       "heOpTxInputTable": heOpTxInputTable,
       "heOpTxInputEntry": heOpTxInputEntry,
       "heOpTxInputIndex": heOpTxInputIndex,
       "heOpTxInputRFPower": heOpTxInputRFPower,
       "heOpTxInputModulatorBias": heOpTxInputModulatorBias,
       "heOpTxInputAGCMode": heOpTxInputAGCMode,
       "heOpTxInputModulationMode": heOpTxInputModulationMode,
       "heOpTxInputRFPadLevel": heOpTxInputRFPadLevel,
       "heOpTxLaserTable": heOpTxLaserTable,
       "heOpTxLaserEntry": heOpTxLaserEntry,
       "heOpTxLaserIndex": heOpTxLaserIndex,
       "heOpTxLaserTemp": heOpTxLaserTemp,
       "heOpTxLaserBiasCurrent": heOpTxLaserBiasCurrent,
       "heOpTxLaserOutputPower": heOpTxLaserOutputPower,
       "heOpTxLaserTECCurrent": heOpTxLaserTECCurrent,
       "heOpTxLaserType": heOpTxLaserType,
       "heOpTxLaserWavelength": heOpTxLaserWavelength,
       "heOpTxLaserOutputStatus": heOpTxLaserOutputStatus,
       "heOpTxLaserOnOffControl": heOpTxLaserOnOffControl,
       "heOpTxMIBConformance": heOpTxMIBConformance,
       "heOpTxMIBCompliances": heOpTxMIBCompliances,
       "heOpTxCompliance": heOpTxCompliance,
       "heOpTxMIBGroups": heOpTxMIBGroups,
       "heOpTxUnitMandatoryGroup": heOpTxUnitMandatoryGroup,
       "heOpTxLaserMandatoryGroup": heOpTxLaserMandatoryGroup,
       "heOpTxUnitTableGroup": heOpTxUnitTableGroup,
       "heOpTxInputTableGroup": heOpTxInputTableGroup,
       "heOpTxLaserTableGroup": heOpTxLaserTableGroup}
)
