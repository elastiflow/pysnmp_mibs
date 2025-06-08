# SNMP MIB module (SCTE-HMS-HE-OPTICAL-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HE-OPTICAL-SWITCH-MIB.mib
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

(heOpticalSwitchGroup,) = mibBuilder.importSymbols(
    "SCTE-HMS-HE-OPTICS-MIB",
    "heOpticalSwitchGroup")

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

heOpticalSwitchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HeOpSwitchMIBObjects_ObjectIdentity = ObjectIdentity
heOpSwitchMIBObjects = _HeOpSwitchMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1)
)
_HeOpSwitchUnitTable_Object = MibTable
heOpSwitchUnitTable = _HeOpSwitchUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    heOpSwitchUnitTable.setStatus("current")
_HeOpSwitchUnitEntry_Object = MibTableRow
heOpSwitchUnitEntry = _HeOpSwitchUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 1, 1)
)
heOpSwitchUnitEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    heOpSwitchUnitEntry.setStatus("current")


class _HeOpSwitchMode_Type(Integer32):
    """Custom type heOpSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_HeOpSwitchMode_Type.__name__ = "Integer32"
_HeOpSwitchMode_Object = MibTableColumn
heOpSwitchMode = _HeOpSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 1, 1, 1),
    _HeOpSwitchMode_Type()
)
heOpSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpSwitchMode.setStatus("current")


class _HeOpSwitchControl_Type(Integer32):
    """Custom type heOpSwitchControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pathA", 1),
          ("pathB", 2),
          ("cross", 3),
          ("bar", 4),
          ("bothA", 5),
          ("bothB", 6))
    )


_HeOpSwitchControl_Type.__name__ = "Integer32"
_HeOpSwitchControl_Object = MibTableColumn
heOpSwitchControl = _HeOpSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 1, 1, 2),
    _HeOpSwitchControl_Type()
)
heOpSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpSwitchControl.setStatus("current")
_HeOpSwitchRevertEnable_Type = HeOnOffControl
_HeOpSwitchRevertEnable_Object = MibTableColumn
heOpSwitchRevertEnable = _HeOpSwitchRevertEnable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 1, 1, 3),
    _HeOpSwitchRevertEnable_Type()
)
heOpSwitchRevertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpSwitchRevertEnable.setStatus("current")


class _HeOpSwitchState_Type(Integer32):
    """Custom type heOpSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pathA", 1),
          ("pathB", 2),
          ("cross", 3),
          ("bar", 4),
          ("bothA", 5),
          ("bothB", 6))
    )


_HeOpSwitchState_Type.__name__ = "Integer32"
_HeOpSwitchState_Object = MibTableColumn
heOpSwitchState = _HeOpSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 1, 1, 4),
    _HeOpSwitchState_Type()
)
heOpSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpSwitchState.setStatus("current")
_HeOpSwitchFailoverStatus_Type = HeFaultStatus
_HeOpSwitchFailoverStatus_Object = MibTableColumn
heOpSwitchFailoverStatus = _HeOpSwitchFailoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 1, 1, 5),
    _HeOpSwitchFailoverStatus_Type()
)
heOpSwitchFailoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpSwitchFailoverStatus.setStatus("current")
_HeOpSwitchBothInputStatus_Type = HeFaultStatus
_HeOpSwitchBothInputStatus_Object = MibTableColumn
heOpSwitchBothInputStatus = _HeOpSwitchBothInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 1, 1, 6),
    _HeOpSwitchBothInputStatus_Type()
)
heOpSwitchBothInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpSwitchBothInputStatus.setStatus("current")
_HeOpSwitchSelectWavelength_Type = HeHundredthNanoMeter
_HeOpSwitchSelectWavelength_Object = MibTableColumn
heOpSwitchSelectWavelength = _HeOpSwitchSelectWavelength_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 1, 1, 7),
    _HeOpSwitchSelectWavelength_Type()
)
heOpSwitchSelectWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpSwitchSelectWavelength.setStatus("current")
if mibBuilder.loadTexts:
    heOpSwitchSelectWavelength.setUnits("0.01 nm")


class _HeOpSwitchHysteresis_Type(HeTenthdB):
    """Custom type heOpSwitchHysteresis based on HeTenthdB"""
    subtypeSpec = HeTenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_HeOpSwitchHysteresis_Type.__name__ = "HeTenthdB"
_HeOpSwitchHysteresis_Object = MibTableColumn
heOpSwitchHysteresis = _HeOpSwitchHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 1, 1, 8),
    _HeOpSwitchHysteresis_Type()
)
heOpSwitchHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpSwitchHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    heOpSwitchHysteresis.setUnits("0.1 dB")
_HeOpSwitchWaitToRestoreTime_Type = Integer32
_HeOpSwitchWaitToRestoreTime_Object = MibTableColumn
heOpSwitchWaitToRestoreTime = _HeOpSwitchWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 1, 1, 9),
    _HeOpSwitchWaitToRestoreTime_Type()
)
heOpSwitchWaitToRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpSwitchWaitToRestoreTime.setStatus("current")
if mibBuilder.loadTexts:
    heOpSwitchWaitToRestoreTime.setUnits("1 sec")
_HeOpSwitchInputTable_Object = MibTable
heOpSwitchInputTable = _HeOpSwitchInputTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    heOpSwitchInputTable.setStatus("current")
_HeOpSwitchInputEntry_Object = MibTableRow
heOpSwitchInputEntry = _HeOpSwitchInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 2, 1)
)
heOpSwitchInputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchInputIndex"),
)
if mibBuilder.loadTexts:
    heOpSwitchInputEntry.setStatus("current")
_HeOpSwitchInputIndex_Type = Unsigned32
_HeOpSwitchInputIndex_Object = MibTableColumn
heOpSwitchInputIndex = _HeOpSwitchInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 2, 1, 1),
    _HeOpSwitchInputIndex_Type()
)
heOpSwitchInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heOpSwitchInputIndex.setStatus("current")
_HeOpSwitchInputOpticalLevel_Type = HeTenthdBm
_HeOpSwitchInputOpticalLevel_Object = MibTableColumn
heOpSwitchInputOpticalLevel = _HeOpSwitchInputOpticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 2, 1, 2),
    _HeOpSwitchInputOpticalLevel_Type()
)
heOpSwitchInputOpticalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpSwitchInputOpticalLevel.setStatus("current")
if mibBuilder.loadTexts:
    heOpSwitchInputOpticalLevel.setUnits("0.1 dBm")
_HeOpSwitchSetInputPowerThreshold_Type = HeTenthdBm
_HeOpSwitchSetInputPowerThreshold_Object = MibTableColumn
heOpSwitchSetInputPowerThreshold = _HeOpSwitchSetInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 2, 1, 3),
    _HeOpSwitchSetInputPowerThreshold_Type()
)
heOpSwitchSetInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heOpSwitchSetInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    heOpSwitchSetInputPowerThreshold.setUnits("0.1 dBm")
_HeOpSwitchInputStatus_Type = HeFaultStatus
_HeOpSwitchInputStatus_Object = MibTableColumn
heOpSwitchInputStatus = _HeOpSwitchInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 2, 1, 4),
    _HeOpSwitchInputStatus_Type()
)
heOpSwitchInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpSwitchInputStatus.setStatus("current")


class _HeOpSwitchInputDescription_Type(DisplayString):
    """Custom type heOpSwitchInputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HeOpSwitchInputDescription_Type.__name__ = "DisplayString"
_HeOpSwitchInputDescription_Object = MibTableColumn
heOpSwitchInputDescription = _HeOpSwitchInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 2, 1, 5),
    _HeOpSwitchInputDescription_Type()
)
heOpSwitchInputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpSwitchInputDescription.setStatus("current")
_HeOpSwitchOutputTable_Object = MibTable
heOpSwitchOutputTable = _HeOpSwitchOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    heOpSwitchOutputTable.setStatus("current")
_HeOpSwitchOutputEntry_Object = MibTableRow
heOpSwitchOutputEntry = _HeOpSwitchOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 3, 1)
)
heOpSwitchOutputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchOutputIndex"),
)
if mibBuilder.loadTexts:
    heOpSwitchOutputEntry.setStatus("current")
_HeOpSwitchOutputIndex_Type = Unsigned32
_HeOpSwitchOutputIndex_Object = MibTableColumn
heOpSwitchOutputIndex = _HeOpSwitchOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 3, 1, 1),
    _HeOpSwitchOutputIndex_Type()
)
heOpSwitchOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heOpSwitchOutputIndex.setStatus("current")


class _HeOpSwitchOutputDescription_Type(DisplayString):
    """Custom type heOpSwitchOutputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HeOpSwitchOutputDescription_Type.__name__ = "DisplayString"
_HeOpSwitchOutputDescription_Object = MibTableColumn
heOpSwitchOutputDescription = _HeOpSwitchOutputDescription_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 1, 3, 1, 2),
    _HeOpSwitchOutputDescription_Type()
)
heOpSwitchOutputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heOpSwitchOutputDescription.setStatus("current")
_HeOpSwitchMIBConformance_ObjectIdentity = ObjectIdentity
heOpSwitchMIBConformance = _HeOpSwitchMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 2)
)
_HeOpSwitchMIBCompliances_ObjectIdentity = ObjectIdentity
heOpSwitchMIBCompliances = _HeOpSwitchMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 2, 1)
)
_HeOpSwitchMIBGroups_ObjectIdentity = ObjectIdentity
heOpSwitchMIBGroups = _HeOpSwitchMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 2, 2)
)

# Managed Objects groups

heOpSwitchUnitMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 2, 2, 1)
)
heOpSwitchUnitMandatoryGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchMode"),
        ("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchControl"),
        ("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchState"),
        ("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchFailoverStatus"))
)
if mibBuilder.loadTexts:
    heOpSwitchUnitMandatoryGroup.setStatus("current")

heOpSwitchInputMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 2, 2, 2)
)
heOpSwitchInputMandatoryGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchInputStatus"),
        ("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchInputDescription"))
)
if mibBuilder.loadTexts:
    heOpSwitchInputMandatoryGroup.setStatus("current")

heOpSwitchOutputMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 2, 2, 3)
)
heOpSwitchOutputMandatoryGroup.setObjects(
    ("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchOutputDescription")
)
if mibBuilder.loadTexts:
    heOpSwitchOutputMandatoryGroup.setStatus("current")

heOpSwitchUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 2, 2, 4)
)
heOpSwitchUnitGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchRevertEnable"),
        ("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchBothInputStatus"),
        ("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchSelectWavelength"),
        ("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchHysteresis"),
        ("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchWaitToRestoreTime"))
)
if mibBuilder.loadTexts:
    heOpSwitchUnitGroup.setStatus("current")

heOpSwitchInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 2, 2, 5)
)
heOpSwitchInputGroup.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchInputOpticalLevel"),
        ("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchSetInputPowerThreshold"))
)
if mibBuilder.loadTexts:
    heOpSwitchInputGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

heOpSwitchBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1, 4, 1, 2, 1, 1)
)
heOpSwitchBasicCompliance.setObjects(
      *(("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchUnitMandatoryGroup"),
        ("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchInputMandatoryGroup"),
        ("SCTE-HMS-HE-OPTICAL-SWITCH-MIB", "heOpSwitchOutputMandatoryGroup"))
)
if mibBuilder.loadTexts:
    heOpSwitchBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HE-OPTICAL-SWITCH-MIB",
    **{"heOpticalSwitchMIB": heOpticalSwitchMIB,
       "heOpSwitchMIBObjects": heOpSwitchMIBObjects,
       "heOpSwitchUnitTable": heOpSwitchUnitTable,
       "heOpSwitchUnitEntry": heOpSwitchUnitEntry,
       "heOpSwitchMode": heOpSwitchMode,
       "heOpSwitchControl": heOpSwitchControl,
       "heOpSwitchRevertEnable": heOpSwitchRevertEnable,
       "heOpSwitchState": heOpSwitchState,
       "heOpSwitchFailoverStatus": heOpSwitchFailoverStatus,
       "heOpSwitchBothInputStatus": heOpSwitchBothInputStatus,
       "heOpSwitchSelectWavelength": heOpSwitchSelectWavelength,
       "heOpSwitchHysteresis": heOpSwitchHysteresis,
       "heOpSwitchWaitToRestoreTime": heOpSwitchWaitToRestoreTime,
       "heOpSwitchInputTable": heOpSwitchInputTable,
       "heOpSwitchInputEntry": heOpSwitchInputEntry,
       "heOpSwitchInputIndex": heOpSwitchInputIndex,
       "heOpSwitchInputOpticalLevel": heOpSwitchInputOpticalLevel,
       "heOpSwitchSetInputPowerThreshold": heOpSwitchSetInputPowerThreshold,
       "heOpSwitchInputStatus": heOpSwitchInputStatus,
       "heOpSwitchInputDescription": heOpSwitchInputDescription,
       "heOpSwitchOutputTable": heOpSwitchOutputTable,
       "heOpSwitchOutputEntry": heOpSwitchOutputEntry,
       "heOpSwitchOutputIndex": heOpSwitchOutputIndex,
       "heOpSwitchOutputDescription": heOpSwitchOutputDescription,
       "heOpSwitchMIBConformance": heOpSwitchMIBConformance,
       "heOpSwitchMIBCompliances": heOpSwitchMIBCompliances,
       "heOpSwitchBasicCompliance": heOpSwitchBasicCompliance,
       "heOpSwitchMIBGroups": heOpSwitchMIBGroups,
       "heOpSwitchUnitMandatoryGroup": heOpSwitchUnitMandatoryGroup,
       "heOpSwitchInputMandatoryGroup": heOpSwitchInputMandatoryGroup,
       "heOpSwitchOutputMandatoryGroup": heOpSwitchOutputMandatoryGroup,
       "heOpSwitchUnitGroup": heOpSwitchUnitGroup,
       "heOpSwitchInputGroup": heOpSwitchInputGroup}
)
