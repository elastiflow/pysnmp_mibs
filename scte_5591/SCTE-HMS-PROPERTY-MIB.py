# SNMP MIB module (SCTE-HMS-PROPERTY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-PROPERTY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:32:18 2025
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

(propertyIdent,) = mibBuilder.importSymbols(
    "SCTE-HMS-ROOTS",
    "propertyIdent")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

propertyMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 0)
)
if mibBuilder.loadTexts:
    propertyMib.setRevisions(
        ("2009-02-13 15:14",
         "2008-04-03 13:45")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PropertyTable_Object = MibTable
propertyTable = _PropertyTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 1)
)
if mibBuilder.loadTexts:
    propertyTable.setStatus("current")
_PropertyEntry_Object = MibTableRow
propertyEntry = _PropertyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 1, 1)
)
propertyEntry.setIndexNames(
    (0, "SCTE-HMS-PROPERTY-MIB", "parameterOID"),
)
if mibBuilder.loadTexts:
    propertyEntry.setStatus("current")
_ParameterOID_Type = ObjectIdentifier
_ParameterOID_Object = MibTableColumn
parameterOID = _ParameterOID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 1, 1, 1),
    _ParameterOID_Type()
)
parameterOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameterOID.setStatus("current")


class _AlarmEnable_Type(OctetString):
    """Custom type alarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_AlarmEnable_Type.__name__ = "OctetString"
_AlarmEnable_Object = MibTableColumn
alarmEnable = _AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 1, 1, 2),
    _AlarmEnable_Type()
)
alarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmEnable.setStatus("current")


class _CurrentAlarmState_Type(Integer32):
    """Custom type currentAlarmState based on Integer32"""
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
        *(("casNominal", 1),
          ("casHIHI", 2),
          ("casHI", 3),
          ("casLO", 4),
          ("casLOLO", 5))
    )


_CurrentAlarmState_Type.__name__ = "Integer32"
_CurrentAlarmState_Object = MibTableColumn
currentAlarmState = _CurrentAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 1, 1, 3),
    _CurrentAlarmState_Type()
)
currentAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmState.setStatus("current")
_AnalogAlarmHIHI_Type = Integer32
_AnalogAlarmHIHI_Object = MibTableColumn
analogAlarmHIHI = _AnalogAlarmHIHI_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 1, 1, 4),
    _AnalogAlarmHIHI_Type()
)
analogAlarmHIHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmHIHI.setStatus("current")
_AnalogAlarmHI_Type = Integer32
_AnalogAlarmHI_Object = MibTableColumn
analogAlarmHI = _AnalogAlarmHI_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 1, 1, 5),
    _AnalogAlarmHI_Type()
)
analogAlarmHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmHI.setStatus("current")
_AnalogAlarmLO_Type = Integer32
_AnalogAlarmLO_Object = MibTableColumn
analogAlarmLO = _AnalogAlarmLO_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 1, 1, 6),
    _AnalogAlarmLO_Type()
)
analogAlarmLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmLO.setStatus("current")
_AnalogAlarmLOLO_Type = Integer32
_AnalogAlarmLOLO_Object = MibTableColumn
analogAlarmLOLO = _AnalogAlarmLOLO_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 1, 1, 7),
    _AnalogAlarmLOLO_Type()
)
analogAlarmLOLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmLOLO.setStatus("current")
_AnalogAlarmDeadband_Type = Integer32
_AnalogAlarmDeadband_Object = MibTableColumn
analogAlarmDeadband = _AnalogAlarmDeadband_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 1, 1, 9),
    _AnalogAlarmDeadband_Type()
)
analogAlarmDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmDeadband.setStatus("current")
_CurrentAlarmTable_Object = MibTable
currentAlarmTable = _CurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 2)
)
if mibBuilder.loadTexts:
    currentAlarmTable.setStatus("current")
_CurrentAlarmEntry_Object = MibTableRow
currentAlarmEntry = _CurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 2, 1)
)
currentAlarmEntry.setIndexNames(
    (0, "SCTE-HMS-PROPERTY-MIB", "currentAlarmOID"),
)
if mibBuilder.loadTexts:
    currentAlarmEntry.setStatus("current")
_CurrentAlarmOID_Type = ObjectIdentifier
_CurrentAlarmOID_Object = MibTableColumn
currentAlarmOID = _CurrentAlarmOID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 2, 1, 1),
    _CurrentAlarmOID_Type()
)
currentAlarmOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmOID.setStatus("current")


class _CurrentAlarmAlarmState_Type(Integer32):
    """Custom type currentAlarmAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("caasHIHI", 2),
          ("caasHI", 3),
          ("caasLO", 4),
          ("caasLOLO", 5),
          ("caasDiscreteMajor", 6),
          ("caasDiscreteMinor", 7))
    )


_CurrentAlarmAlarmState_Type.__name__ = "Integer32"
_CurrentAlarmAlarmState_Object = MibTableColumn
currentAlarmAlarmState = _CurrentAlarmAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 2, 1, 2),
    _CurrentAlarmAlarmState_Type()
)
currentAlarmAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmAlarmState.setStatus("current")
_CurrentAlarmAlarmValue_Type = Integer32
_CurrentAlarmAlarmValue_Object = MibTableColumn
currentAlarmAlarmValue = _CurrentAlarmAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 2, 1, 3),
    _CurrentAlarmAlarmValue_Type()
)
currentAlarmAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmAlarmValue.setStatus("current")
_CurrentAlarmLogTime_Type = DateAndTime
_CurrentAlarmLogTime_Object = MibTableColumn
currentAlarmLogTime = _CurrentAlarmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 2, 1, 4),
    _CurrentAlarmLogTime_Type()
)
currentAlarmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmLogTime.setStatus("current")
_DiscretePropertyTable_Object = MibTable
discretePropertyTable = _DiscretePropertyTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 3)
)
if mibBuilder.loadTexts:
    discretePropertyTable.setStatus("current")
_DiscretePropertyEntry_Object = MibTableRow
discretePropertyEntry = _DiscretePropertyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 3, 1)
)
discretePropertyEntry.setIndexNames(
    (0, "SCTE-HMS-PROPERTY-MIB", "discreteParameterOID"),
    (0, "SCTE-HMS-PROPERTY-MIB", "discreteAlarmValue"),
)
if mibBuilder.loadTexts:
    discretePropertyEntry.setStatus("current")
_DiscreteParameterOID_Type = ObjectIdentifier
_DiscreteParameterOID_Object = MibTableColumn
discreteParameterOID = _DiscreteParameterOID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 3, 1, 1),
    _DiscreteParameterOID_Type()
)
discreteParameterOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discreteParameterOID.setStatus("current")


class _DiscreteAlarmValue_Type(Integer32):
    """Custom type discreteAlarmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DiscreteAlarmValue_Type.__name__ = "Integer32"
_DiscreteAlarmValue_Object = MibTableColumn
discreteAlarmValue = _DiscreteAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 3, 1, 2),
    _DiscreteAlarmValue_Type()
)
discreteAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discreteAlarmValue.setStatus("current")


class _DiscreteAlarmEnable_Type(Integer32):
    """Custom type discreteAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableMajor", 2),
          ("enableMinor", 3))
    )


_DiscreteAlarmEnable_Type.__name__ = "Integer32"
_DiscreteAlarmEnable_Object = MibTableColumn
discreteAlarmEnable = _DiscreteAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 3, 1, 3),
    _DiscreteAlarmEnable_Type()
)
discreteAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discreteAlarmEnable.setStatus("current")


class _DiscreteAlarmState_Type(Integer32):
    """Custom type discreteAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dasNominal", 1),
          ("dasDiscreteMajor", 6),
          ("dasDiscreteMinor", 7))
    )


_DiscreteAlarmState_Type.__name__ = "Integer32"
_DiscreteAlarmState_Object = MibTableColumn
discreteAlarmState = _DiscreteAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 3, 1, 4),
    _DiscreteAlarmState_Type()
)
discreteAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discreteAlarmState.setStatus("current")
_PropertyConformance_ObjectIdentity = ObjectIdentity
propertyConformance = _PropertyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 4)
)
_PropertyCompliances_ObjectIdentity = ObjectIdentity
propertyCompliances = _PropertyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 4, 1)
)
_PropertyGroups_ObjectIdentity = ObjectIdentity
propertyGroups = _PropertyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 4, 2)
)

# Managed Objects groups

propertyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 4, 2, 1)
)
propertyGroup.setObjects(
      *(("SCTE-HMS-PROPERTY-MIB", "alarmEnable"),
        ("SCTE-HMS-PROPERTY-MIB", "analogAlarmDeadband"),
        ("SCTE-HMS-PROPERTY-MIB", "analogAlarmHI"),
        ("SCTE-HMS-PROPERTY-MIB", "analogAlarmHIHI"),
        ("SCTE-HMS-PROPERTY-MIB", "analogAlarmLO"),
        ("SCTE-HMS-PROPERTY-MIB", "analogAlarmLOLO"),
        ("SCTE-HMS-PROPERTY-MIB", "currentAlarmState"),
        ("SCTE-HMS-PROPERTY-MIB", "parameterOID"))
)
if mibBuilder.loadTexts:
    propertyGroup.setStatus("current")

currentAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 4, 2, 2)
)
currentAlarmGroup.setObjects(
      *(("SCTE-HMS-PROPERTY-MIB", "currentAlarmAlarmState"),
        ("SCTE-HMS-PROPERTY-MIB", "currentAlarmAlarmValue"),
        ("SCTE-HMS-PROPERTY-MIB", "currentAlarmLogTime"),
        ("SCTE-HMS-PROPERTY-MIB", "currentAlarmOID"))
)
if mibBuilder.loadTexts:
    currentAlarmGroup.setStatus("current")

discretePropertyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 4, 2, 3)
)
discretePropertyGroup.setObjects(
      *(("SCTE-HMS-PROPERTY-MIB", "discreteAlarmEnable"),
        ("SCTE-HMS-PROPERTY-MIB", "discreteAlarmState"),
        ("SCTE-HMS-PROPERTY-MIB", "discreteAlarmValue"),
        ("SCTE-HMS-PROPERTY-MIB", "discreteParameterOID"))
)
if mibBuilder.loadTexts:
    discretePropertyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

propertyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1, 4, 1, 1)
)
propertyCompliance.setObjects(
      *(("SCTE-HMS-PROPERTY-MIB", "propertyGroup"),
        ("SCTE-HMS-PROPERTY-MIB", "discretePropertyGroup"),
        ("SCTE-HMS-PROPERTY-MIB", "currentAlarmGroup"))
)
if mibBuilder.loadTexts:
    propertyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-PROPERTY-MIB",
    **{"propertyMib": propertyMib,
       "propertyTable": propertyTable,
       "propertyEntry": propertyEntry,
       "parameterOID": parameterOID,
       "alarmEnable": alarmEnable,
       "currentAlarmState": currentAlarmState,
       "analogAlarmHIHI": analogAlarmHIHI,
       "analogAlarmHI": analogAlarmHI,
       "analogAlarmLO": analogAlarmLO,
       "analogAlarmLOLO": analogAlarmLOLO,
       "analogAlarmDeadband": analogAlarmDeadband,
       "currentAlarmTable": currentAlarmTable,
       "currentAlarmEntry": currentAlarmEntry,
       "currentAlarmOID": currentAlarmOID,
       "currentAlarmAlarmState": currentAlarmAlarmState,
       "currentAlarmAlarmValue": currentAlarmAlarmValue,
       "currentAlarmLogTime": currentAlarmLogTime,
       "discretePropertyTable": discretePropertyTable,
       "discretePropertyEntry": discretePropertyEntry,
       "discreteParameterOID": discreteParameterOID,
       "discreteAlarmValue": discreteAlarmValue,
       "discreteAlarmEnable": discreteAlarmEnable,
       "discreteAlarmState": discreteAlarmState,
       "propertyConformance": propertyConformance,
       "propertyCompliances": propertyCompliances,
       "propertyCompliance": propertyCompliance,
       "propertyGroups": propertyGroups,
       "propertyGroup": propertyGroup,
       "currentAlarmGroup": currentAlarmGroup,
       "discretePropertyGroup": discretePropertyGroup}
)
