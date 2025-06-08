# SNMP MIB module (SCTE-HMS-HE-OPTICAL-RECEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HE-OPTICAL-RECEIVER-MIB.mib
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

(heOpticalReceiverGroup,) = mibBuilder.importSymbols(
    "SCTE-HMS-HE-OPTICS-MIB",
    "heOpticalReceiverGroup")

(HeFaultStatus,
 HeHundredthNanoMeter,
 HeOnOffControl,
 HeTenthdB,
 HeTenthdBm) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    "HeFaultStatus",
    "HeHundredthNanoMeter",
    "HeOnOffControl",
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

heOpticalReceiverMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HeOpRxMIBObjects_ObjectIdentity = ObjectIdentity
heOpRxMIBObjects = _HeOpRxMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1)
)
_HeOpRxInputTable_Object = MibTable
heOpRxInputTable = _HeOpRxInputTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    heOpRxInputTable.setStatus("current")
_HeOpRxInputEntry_Object = MibTableRow
heOpRxInputEntry = _HeOpRxInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 1, 1)
)
heOpRxInputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-OPTICAL-RECEIVER-MIB", "heOpRxInputIndex"),
)
if mibBuilder.loadTexts:
    heOpRxInputEntry.setStatus("current")
_HeOpRxInputIndex_Type = Unsigned32
_HeOpRxInputIndex_Object = MibTableColumn
heOpRxInputIndex = _HeOpRxInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 1, 1, 1),
    _HeOpRxInputIndex_Type()
)
heOpRxInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heOpRxInputIndex.setStatus("current")
_HeOpRxInputPower_Type = HeTenthdBm
_HeOpRxInputPower_Object = MibTableColumn
heOpRxInputPower = _HeOpRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 1, 1, 2),
    _HeOpRxInputPower_Type()
)
heOpRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    heOpRxInputPower.setUnits("0.1 dBm")
_HeOpRxInputWavelengthControl_Type = HeHundredthNanoMeter
_HeOpRxInputWavelengthControl_Object = MibTableColumn
heOpRxInputWavelengthControl = _HeOpRxInputWavelengthControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 1, 1, 3),
    _HeOpRxInputWavelengthControl_Type()
)
heOpRxInputWavelengthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpRxInputWavelengthControl.setStatus("current")
if mibBuilder.loadTexts:
    heOpRxInputWavelengthControl.setUnits("0.01 nm")
_HeOpRxInputStatus_Type = HeFaultStatus
_HeOpRxInputStatus_Object = MibTableColumn
heOpRxInputStatus = _HeOpRxInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 1, 1, 4),
    _HeOpRxInputStatus_Type()
)
heOpRxInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpRxInputStatus.setStatus("current")
_HeOpRxOutputTable_Object = MibTable
heOpRxOutputTable = _HeOpRxOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    heOpRxOutputTable.setStatus("current")
_HeOpRxOutputEntry_Object = MibTableRow
heOpRxOutputEntry = _HeOpRxOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 2, 1)
)
heOpRxOutputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-OPTICAL-RECEIVER-MIB", "heOpRxOutputIndex"),
)
if mibBuilder.loadTexts:
    heOpRxOutputEntry.setStatus("current")
_HeOpRxOutputIndex_Type = Unsigned32
_HeOpRxOutputIndex_Object = MibTableColumn
heOpRxOutputIndex = _HeOpRxOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 2, 1, 1),
    _HeOpRxOutputIndex_Type()
)
heOpRxOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heOpRxOutputIndex.setStatus("current")
_HeOpRxOutputControl_Type = HeOnOffControl
_HeOpRxOutputControl_Object = MibTableColumn
heOpRxOutputControl = _HeOpRxOutputControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 2, 1, 2),
    _HeOpRxOutputControl_Type()
)
heOpRxOutputControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpRxOutputControl.setStatus("current")


class _HeOpRxOutputGainType_Type(Integer32):
    """Custom type heOpRxOutputGainType based on Integer32"""
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


_HeOpRxOutputGainType_Type.__name__ = "Integer32"
_HeOpRxOutputGainType_Object = MibTableColumn
heOpRxOutputGainType = _HeOpRxOutputGainType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 2, 1, 3),
    _HeOpRxOutputGainType_Type()
)
heOpRxOutputGainType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpRxOutputGainType.setStatus("current")
_HeOpRxOutputPower_Type = HeTenthdBm
_HeOpRxOutputPower_Object = MibTableColumn
heOpRxOutputPower = _HeOpRxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 2, 1, 4),
    _HeOpRxOutputPower_Type()
)
heOpRxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpRxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    heOpRxOutputPower.setUnits("0.1 dBm")
_HeOpRxOutputRFPadLevel_Type = HeTenthdB
_HeOpRxOutputRFPadLevel_Object = MibTableColumn
heOpRxOutputRFPadLevel = _HeOpRxOutputRFPadLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 1, 2, 1, 5),
    _HeOpRxOutputRFPadLevel_Type()
)
heOpRxOutputRFPadLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpRxOutputRFPadLevel.setStatus("current")
if mibBuilder.loadTexts:
    heOpRxOutputRFPadLevel.setUnits("0.1 dB")
_HeOpRxMIBConformance_ObjectIdentity = ObjectIdentity
heOpRxMIBConformance = _HeOpRxMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 2)
)
_HeOpRxMIBCompliances_ObjectIdentity = ObjectIdentity
heOpRxMIBCompliances = _HeOpRxMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 2, 1)
)
_HeOpRxMIBGroups_ObjectIdentity = ObjectIdentity
heOpRxMIBGroups = _HeOpRxMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 2, 2)
)

# Managed Objects groups

heOpRxInputMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 2, 2, 1)
)
heOpRxInputMandatoryGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-RECEIVER-MIB", "heOpRxInputStatus"),
        ("SCTE-HMS-HE-OPTICAL-RECEIVER-MIB", "heOpRxInputWavelengthControl"))
)
if mibBuilder.loadTexts:
    heOpRxInputMandatoryGroup.setStatus("current")

heOpRxInputTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 2, 2, 2)
)
heOpRxInputTableGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-RECEIVER-MIB", "heOpRxInputPower"),
        ("SCTE-HMS-HE-OPTICAL-RECEIVER-MIB", "heOpRxInputWavelengthControl"),
        ("SCTE-HMS-HE-OPTICAL-RECEIVER-MIB", "heOpRxInputStatus"))
)
if mibBuilder.loadTexts:
    heOpRxInputTableGroup.setStatus("current")

heOpRxOutputTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 2, 2, 3)
)
heOpRxOutputTableGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-RECEIVER-MIB", "heOpRxOutputControl"),
        ("SCTE-HMS-HE-OPTICAL-RECEIVER-MIB", "heOpRxOutputGainType"),
        ("SCTE-HMS-HE-OPTICAL-RECEIVER-MIB", "heOpRxOutputPower"),
        ("SCTE-HMS-HE-OPTICAL-RECEIVER-MIB", "heOpRxOutputRFPadLevel"))
)
if mibBuilder.loadTexts:
    heOpRxOutputTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

heOpRxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 2, 1, 2, 1, 1)
)
heOpRxCompliance.setObjects(
    ("SCTE-HMS-HE-OPTICAL-RECEIVER-MIB", "heOpRxInputMandatoryGroup")
)
if mibBuilder.loadTexts:
    heOpRxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HE-OPTICAL-RECEIVER-MIB",
    **{"heOpticalReceiverMIB": heOpticalReceiverMIB,
       "heOpRxMIBObjects": heOpRxMIBObjects,
       "heOpRxInputTable": heOpRxInputTable,
       "heOpRxInputEntry": heOpRxInputEntry,
       "heOpRxInputIndex": heOpRxInputIndex,
       "heOpRxInputPower": heOpRxInputPower,
       "heOpRxInputWavelengthControl": heOpRxInputWavelengthControl,
       "heOpRxInputStatus": heOpRxInputStatus,
       "heOpRxOutputTable": heOpRxOutputTable,
       "heOpRxOutputEntry": heOpRxOutputEntry,
       "heOpRxOutputIndex": heOpRxOutputIndex,
       "heOpRxOutputControl": heOpRxOutputControl,
       "heOpRxOutputGainType": heOpRxOutputGainType,
       "heOpRxOutputPower": heOpRxOutputPower,
       "heOpRxOutputRFPadLevel": heOpRxOutputRFPadLevel,
       "heOpRxMIBConformance": heOpRxMIBConformance,
       "heOpRxMIBCompliances": heOpRxMIBCompliances,
       "heOpRxCompliance": heOpRxCompliance,
       "heOpRxMIBGroups": heOpRxMIBGroups,
       "heOpRxInputMandatoryGroup": heOpRxInputMandatoryGroup,
       "heOpRxInputTableGroup": heOpRxInputTableGroup,
       "heOpRxOutputTableGroup": heOpRxOutputTableGroup}
)
