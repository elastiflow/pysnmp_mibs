# SNMP MIB module (SCTE-HMS-HE-RF-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HE-RF-SWITCH-MIB.mib
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

(heRFSwitchGroup,) = mibBuilder.importSymbols(
    "SCTE-HMS-HE-RF-MIB",
    "heRFSwitchGroup")

(HeFaultStatus,
 HeOnOffControl,
 HeTenthdB,
 HeTenthdBmV) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    "HeFaultStatus",
    "HeOnOffControl",
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

heRFSwitchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HeRFSwitchMIBObjects_ObjectIdentity = ObjectIdentity
heRFSwitchMIBObjects = _HeRFSwitchMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1)
)
_HeRFSwitchUnitTable_Object = MibTable
heRFSwitchUnitTable = _HeRFSwitchUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    heRFSwitchUnitTable.setStatus("current")
_HeRFSwitchUnitEntry_Object = MibTableRow
heRFSwitchUnitEntry = _HeRFSwitchUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 1, 1)
)
heRFSwitchUnitEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    heRFSwitchUnitEntry.setStatus("current")


class _HeRFSwitchMode_Type(Integer32):
    """Custom type heRFSwitchMode based on Integer32"""
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


_HeRFSwitchMode_Type.__name__ = "Integer32"
_HeRFSwitchMode_Object = MibTableColumn
heRFSwitchMode = _HeRFSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 1, 1, 1),
    _HeRFSwitchMode_Type()
)
heRFSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heRFSwitchMode.setStatus("current")


class _HeRFSwitchControl_Type(Integer32):
    """Custom type heRFSwitchControl based on Integer32"""
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


_HeRFSwitchControl_Type.__name__ = "Integer32"
_HeRFSwitchControl_Object = MibTableColumn
heRFSwitchControl = _HeRFSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 1, 1, 2),
    _HeRFSwitchControl_Type()
)
heRFSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heRFSwitchControl.setStatus("current")
_HeRFSwitchRevertEnable_Type = HeOnOffControl
_HeRFSwitchRevertEnable_Object = MibTableColumn
heRFSwitchRevertEnable = _HeRFSwitchRevertEnable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 1, 1, 3),
    _HeRFSwitchRevertEnable_Type()
)
heRFSwitchRevertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heRFSwitchRevertEnable.setStatus("current")


class _HeRFSwitchState_Type(Integer32):
    """Custom type heRFSwitchState based on Integer32"""
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


_HeRFSwitchState_Type.__name__ = "Integer32"
_HeRFSwitchState_Object = MibTableColumn
heRFSwitchState = _HeRFSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 1, 1, 4),
    _HeRFSwitchState_Type()
)
heRFSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heRFSwitchState.setStatus("current")
_HeRFSwitchFailoverStatus_Type = HeFaultStatus
_HeRFSwitchFailoverStatus_Object = MibTableColumn
heRFSwitchFailoverStatus = _HeRFSwitchFailoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 1, 1, 5),
    _HeRFSwitchFailoverStatus_Type()
)
heRFSwitchFailoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heRFSwitchFailoverStatus.setStatus("current")
_HeRFSwitchBothInputStatus_Type = HeFaultStatus
_HeRFSwitchBothInputStatus_Object = MibTableColumn
heRFSwitchBothInputStatus = _HeRFSwitchBothInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 1, 1, 6),
    _HeRFSwitchBothInputStatus_Type()
)
heRFSwitchBothInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heRFSwitchBothInputStatus.setStatus("current")


class _HeRFSwitchHysteresis_Type(HeTenthdB):
    """Custom type heRFSwitchHysteresis based on HeTenthdB"""
    subtypeSpec = HeTenthdB.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_HeRFSwitchHysteresis_Type.__name__ = "HeTenthdB"
_HeRFSwitchHysteresis_Object = MibTableColumn
heRFSwitchHysteresis = _HeRFSwitchHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 1, 1, 7),
    _HeRFSwitchHysteresis_Type()
)
heRFSwitchHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heRFSwitchHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    heRFSwitchHysteresis.setUnits("0.1 dB")
_HeRFSwitchWaitToRestoreTime_Type = Integer32
_HeRFSwitchWaitToRestoreTime_Object = MibTableColumn
heRFSwitchWaitToRestoreTime = _HeRFSwitchWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 1, 1, 8),
    _HeRFSwitchWaitToRestoreTime_Type()
)
heRFSwitchWaitToRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heRFSwitchWaitToRestoreTime.setStatus("current")
if mibBuilder.loadTexts:
    heRFSwitchWaitToRestoreTime.setUnits("1 sec")


class _HeRFSwitchSensorMode_Type(Integer32):
    """Custom type heRFSwitchSensorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_HeRFSwitchSensorMode_Type.__name__ = "Integer32"
_HeRFSwitchSensorMode_Object = MibTableColumn
heRFSwitchSensorMode = _HeRFSwitchSensorMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 1, 1, 9),
    _HeRFSwitchSensorMode_Type()
)
heRFSwitchSensorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heRFSwitchSensorMode.setStatus("current")
_HeRFSwitchInputTable_Object = MibTable
heRFSwitchInputTable = _HeRFSwitchInputTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    heRFSwitchInputTable.setStatus("current")
_HeRFSwitchInputEntry_Object = MibTableRow
heRFSwitchInputEntry = _HeRFSwitchInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 2, 1)
)
heRFSwitchInputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchInputIndex"),
)
if mibBuilder.loadTexts:
    heRFSwitchInputEntry.setStatus("current")
_HeRFSwitchInputIndex_Type = Unsigned32
_HeRFSwitchInputIndex_Object = MibTableColumn
heRFSwitchInputIndex = _HeRFSwitchInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 2, 1, 1),
    _HeRFSwitchInputIndex_Type()
)
heRFSwitchInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heRFSwitchInputIndex.setStatus("current")
_HeRFSwitchInputRFLevel_Type = HeTenthdBmV
_HeRFSwitchInputRFLevel_Object = MibTableColumn
heRFSwitchInputRFLevel = _HeRFSwitchInputRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 2, 1, 2),
    _HeRFSwitchInputRFLevel_Type()
)
heRFSwitchInputRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heRFSwitchInputRFLevel.setStatus("current")
if mibBuilder.loadTexts:
    heRFSwitchInputRFLevel.setUnits("0.1 dBmV")
_HeRFSwitchSetInputPowerThreshold_Type = HeTenthdBmV
_HeRFSwitchSetInputPowerThreshold_Object = MibTableColumn
heRFSwitchSetInputPowerThreshold = _HeRFSwitchSetInputPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 2, 1, 3),
    _HeRFSwitchSetInputPowerThreshold_Type()
)
heRFSwitchSetInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heRFSwitchSetInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    heRFSwitchSetInputPowerThreshold.setUnits("0.1 dBmV")
_HeRFSwitchInputStatus_Type = HeFaultStatus
_HeRFSwitchInputStatus_Object = MibTableColumn
heRFSwitchInputStatus = _HeRFSwitchInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 2, 1, 4),
    _HeRFSwitchInputStatus_Type()
)
heRFSwitchInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heRFSwitchInputStatus.setStatus("current")


class _HeRFSwitchInputDescription_Type(DisplayString):
    """Custom type heRFSwitchInputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HeRFSwitchInputDescription_Type.__name__ = "DisplayString"
_HeRFSwitchInputDescription_Object = MibTableColumn
heRFSwitchInputDescription = _HeRFSwitchInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 2, 1, 5),
    _HeRFSwitchInputDescription_Type()
)
heRFSwitchInputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heRFSwitchInputDescription.setStatus("current")
_HeRFSwitchInputExternalControl_Type = HeFaultStatus
_HeRFSwitchInputExternalControl_Object = MibTableColumn
heRFSwitchInputExternalControl = _HeRFSwitchInputExternalControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 2, 1, 6),
    _HeRFSwitchInputExternalControl_Type()
)
heRFSwitchInputExternalControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heRFSwitchInputExternalControl.setStatus("current")
_HeRFSwitchOutputTable_Object = MibTable
heRFSwitchOutputTable = _HeRFSwitchOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    heRFSwitchOutputTable.setStatus("current")
_HeRFSwitchOutputEntry_Object = MibTableRow
heRFSwitchOutputEntry = _HeRFSwitchOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 3, 1)
)
heRFSwitchOutputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchOutputIndex"),
)
if mibBuilder.loadTexts:
    heRFSwitchOutputEntry.setStatus("current")
_HeRFSwitchOutputIndex_Type = Unsigned32
_HeRFSwitchOutputIndex_Object = MibTableColumn
heRFSwitchOutputIndex = _HeRFSwitchOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 3, 1, 1),
    _HeRFSwitchOutputIndex_Type()
)
heRFSwitchOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heRFSwitchOutputIndex.setStatus("current")


class _HeRFSwitchOutputDescription_Type(DisplayString):
    """Custom type heRFSwitchOutputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HeRFSwitchOutputDescription_Type.__name__ = "DisplayString"
_HeRFSwitchOutputDescription_Object = MibTableColumn
heRFSwitchOutputDescription = _HeRFSwitchOutputDescription_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 1, 3, 1, 2),
    _HeRFSwitchOutputDescription_Type()
)
heRFSwitchOutputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heRFSwitchOutputDescription.setStatus("current")
_HeRFSwitchMIBConformance_ObjectIdentity = ObjectIdentity
heRFSwitchMIBConformance = _HeRFSwitchMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 2)
)
_HeRFSwitchMIBCompliances_ObjectIdentity = ObjectIdentity
heRFSwitchMIBCompliances = _HeRFSwitchMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 2, 1)
)
_HeRFSwitchMIBGroups_ObjectIdentity = ObjectIdentity
heRFSwitchMIBGroups = _HeRFSwitchMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 2, 2)
)

# Managed Objects groups

heRFSwitchUnitMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 2, 2, 1)
)
heRFSwitchUnitMandatoryGroup.setObjects(
      *(("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchMode"),
        ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchControl"),
        ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchRevertEnable"),
        ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchState"),
        ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchFailoverStatus"))
)
if mibBuilder.loadTexts:
    heRFSwitchUnitMandatoryGroup.setStatus("current")

heRFSwitchInputMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 2, 2, 2)
)
heRFSwitchInputMandatoryGroup.setObjects(
      *(("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchInputStatus"),
        ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchInputDescription"))
)
if mibBuilder.loadTexts:
    heRFSwitchInputMandatoryGroup.setStatus("current")

heRFSwitchOutputMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 2, 2, 3)
)
heRFSwitchOutputMandatoryGroup.setObjects(
    ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchOutputDescription")
)
if mibBuilder.loadTexts:
    heRFSwitchOutputMandatoryGroup.setStatus("current")

heRFSwitchUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 2, 2, 4)
)
heRFSwitchUnitGroup.setObjects(
      *(("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchBothInputStatus"),
        ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchHysteresis"),
        ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchWaitToRestoreTime"),
        ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchSensorMode"))
)
if mibBuilder.loadTexts:
    heRFSwitchUnitGroup.setStatus("current")

heRFSwitchInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 2, 2, 5)
)
heRFSwitchInputGroup.setObjects(
      *(("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchInputRFLevel"),
        ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchSetInputPowerThreshold"),
        ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchInputExternalControl"))
)
if mibBuilder.loadTexts:
    heRFSwitchInputGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

heRFSwitchBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4, 2, 1, 2, 1, 1)
)
heRFSwitchBasicCompliance.setObjects(
      *(("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchUnitMandatoryGroup"),
        ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchInputMandatoryGroup"),
        ("SCTE-HMS-HE-RF-SWITCH-MIB", "heRFSwitchOutputMandatoryGroup"))
)
if mibBuilder.loadTexts:
    heRFSwitchBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HE-RF-SWITCH-MIB",
    **{"heRFSwitchMIB": heRFSwitchMIB,
       "heRFSwitchMIBObjects": heRFSwitchMIBObjects,
       "heRFSwitchUnitTable": heRFSwitchUnitTable,
       "heRFSwitchUnitEntry": heRFSwitchUnitEntry,
       "heRFSwitchMode": heRFSwitchMode,
       "heRFSwitchControl": heRFSwitchControl,
       "heRFSwitchRevertEnable": heRFSwitchRevertEnable,
       "heRFSwitchState": heRFSwitchState,
       "heRFSwitchFailoverStatus": heRFSwitchFailoverStatus,
       "heRFSwitchBothInputStatus": heRFSwitchBothInputStatus,
       "heRFSwitchHysteresis": heRFSwitchHysteresis,
       "heRFSwitchWaitToRestoreTime": heRFSwitchWaitToRestoreTime,
       "heRFSwitchSensorMode": heRFSwitchSensorMode,
       "heRFSwitchInputTable": heRFSwitchInputTable,
       "heRFSwitchInputEntry": heRFSwitchInputEntry,
       "heRFSwitchInputIndex": heRFSwitchInputIndex,
       "heRFSwitchInputRFLevel": heRFSwitchInputRFLevel,
       "heRFSwitchSetInputPowerThreshold": heRFSwitchSetInputPowerThreshold,
       "heRFSwitchInputStatus": heRFSwitchInputStatus,
       "heRFSwitchInputDescription": heRFSwitchInputDescription,
       "heRFSwitchInputExternalControl": heRFSwitchInputExternalControl,
       "heRFSwitchOutputTable": heRFSwitchOutputTable,
       "heRFSwitchOutputEntry": heRFSwitchOutputEntry,
       "heRFSwitchOutputIndex": heRFSwitchOutputIndex,
       "heRFSwitchOutputDescription": heRFSwitchOutputDescription,
       "heRFSwitchMIBConformance": heRFSwitchMIBConformance,
       "heRFSwitchMIBCompliances": heRFSwitchMIBCompliances,
       "heRFSwitchBasicCompliance": heRFSwitchBasicCompliance,
       "heRFSwitchMIBGroups": heRFSwitchMIBGroups,
       "heRFSwitchUnitMandatoryGroup": heRFSwitchUnitMandatoryGroup,
       "heRFSwitchInputMandatoryGroup": heRFSwitchInputMandatoryGroup,
       "heRFSwitchOutputMandatoryGroup": heRFSwitchOutputMandatoryGroup,
       "heRFSwitchUnitGroup": heRFSwitchUnitGroup,
       "heRFSwitchInputGroup": heRFSwitchInputGroup}
)
