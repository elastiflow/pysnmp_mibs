# SNMP MIB module (CISCO-ENTITY-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ENTITY-SENSOR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:13:16 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

entitySensorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 91)
)
if mibBuilder.loadTexts:
    entitySensorMIB.setRevisions(
        ("2020-09-22 00:00",
         "2002-09-18 00:00",
         "2000-06-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SensorDataType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("voltsAC", 3),
          ("voltsDC", 4),
          ("amperes", 5),
          ("watts", 6),
          ("hertz", 7),
          ("celsius", 8),
          ("percentRH", 9),
          ("rpm", 10),
          ("cmm", 11),
          ("truthvalue", 12),
          ("specialEnum", 13))
    )



class SensorDataScale(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("yocto", 1),
          ("zepto", 2),
          ("atto", 3),
          ("femto", 4),
          ("pico", 5),
          ("nano", 6),
          ("micro", 7),
          ("milli", 8),
          ("units", 9),
          ("kilo", 10),
          ("mega", 11),
          ("giga", 12),
          ("tera", 13),
          ("exa", 14),
          ("peta", 15),
          ("zetta", 16),
          ("yotta", 17))
    )



class SensorPrecision(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8, 9),
    )



class SensorValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )



class SensorStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("unavailable", 2),
          ("nonoperational", 3))
    )



class SensorValueUpdateRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )



class SensorThresholdSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("minor", 10),
          ("major", 20),
          ("critical", 30))
    )



class SensorThresholdRelation(TextualConvention, Integer32):
    status = "current"
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
        *(("lessThan", 1),
          ("lessOrEqual", 2),
          ("greaterThan", 3),
          ("greaterOrEqual", 4),
          ("equalTo", 5),
          ("notEqualTo", 6))
    )



# MIB Managed Objects in the order of their OIDs

_EntitySensorMIBObjects_ObjectIdentity = ObjectIdentity
entitySensorMIBObjects = _EntitySensorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1)
)
_EntSensorValues_ObjectIdentity = ObjectIdentity
entSensorValues = _EntSensorValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1)
)
_EntSensorValueTable_Object = MibTable
entSensorValueTable = _EntSensorValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1)
)
if mibBuilder.loadTexts:
    entSensorValueTable.setStatus("current")
_EntSensorValueEntry_Object = MibTableRow
entSensorValueEntry = _EntSensorValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1)
)
entSensorValueEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    entSensorValueEntry.setStatus("current")
_EntSensorType_Type = SensorDataType
_EntSensorType_Object = MibTableColumn
entSensorType = _EntSensorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 1),
    _EntSensorType_Type()
)
entSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSensorType.setStatus("current")
_EntSensorScale_Type = SensorDataScale
_EntSensorScale_Object = MibTableColumn
entSensorScale = _EntSensorScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 2),
    _EntSensorScale_Type()
)
entSensorScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSensorScale.setStatus("current")
_EntSensorPrecision_Type = SensorPrecision
_EntSensorPrecision_Object = MibTableColumn
entSensorPrecision = _EntSensorPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 3),
    _EntSensorPrecision_Type()
)
entSensorPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSensorPrecision.setStatus("current")
_EntSensorValue_Type = SensorValue
_EntSensorValue_Object = MibTableColumn
entSensorValue = _EntSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 4),
    _EntSensorValue_Type()
)
entSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSensorValue.setStatus("current")
_EntSensorStatus_Type = SensorStatus
_EntSensorStatus_Object = MibTableColumn
entSensorStatus = _EntSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 5),
    _EntSensorStatus_Type()
)
entSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSensorStatus.setStatus("current")
_EntSensorValueTimeStamp_Type = TimeStamp
_EntSensorValueTimeStamp_Object = MibTableColumn
entSensorValueTimeStamp = _EntSensorValueTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 6),
    _EntSensorValueTimeStamp_Type()
)
entSensorValueTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSensorValueTimeStamp.setStatus("current")
_EntSensorValueUpdateRate_Type = SensorValueUpdateRate
_EntSensorValueUpdateRate_Object = MibTableColumn
entSensorValueUpdateRate = _EntSensorValueUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 7),
    _EntSensorValueUpdateRate_Type()
)
entSensorValueUpdateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSensorValueUpdateRate.setStatus("current")
if mibBuilder.loadTexts:
    entSensorValueUpdateRate.setUnits("seconds")


class _EntSensorMeasuredEntity_Type(Integer32):
    """Custom type entSensorMeasuredEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EntSensorMeasuredEntity_Type.__name__ = "Integer32"
_EntSensorMeasuredEntity_Object = MibTableColumn
entSensorMeasuredEntity = _EntSensorMeasuredEntity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 8),
    _EntSensorMeasuredEntity_Type()
)
entSensorMeasuredEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSensorMeasuredEntity.setStatus("current")
_EntSensorThresholds_ObjectIdentity = ObjectIdentity
entSensorThresholds = _EntSensorThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2)
)
_EntSensorThresholdTable_Object = MibTable
entSensorThresholdTable = _EntSensorThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1)
)
if mibBuilder.loadTexts:
    entSensorThresholdTable.setStatus("current")
_EntSensorThresholdEntry_Object = MibTableRow
entSensorThresholdEntry = _EntSensorThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1)
)
entSensorThresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdIndex"),
)
if mibBuilder.loadTexts:
    entSensorThresholdEntry.setStatus("current")


class _EntSensorThresholdIndex_Type(Integer32):
    """Custom type entSensorThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999999),
    )


_EntSensorThresholdIndex_Type.__name__ = "Integer32"
_EntSensorThresholdIndex_Object = MibTableColumn
entSensorThresholdIndex = _EntSensorThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 1),
    _EntSensorThresholdIndex_Type()
)
entSensorThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    entSensorThresholdIndex.setStatus("current")
_EntSensorThresholdSeverity_Type = SensorThresholdSeverity
_EntSensorThresholdSeverity_Object = MibTableColumn
entSensorThresholdSeverity = _EntSensorThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 2),
    _EntSensorThresholdSeverity_Type()
)
entSensorThresholdSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entSensorThresholdSeverity.setStatus("current")
_EntSensorThresholdRelation_Type = SensorThresholdRelation
_EntSensorThresholdRelation_Object = MibTableColumn
entSensorThresholdRelation = _EntSensorThresholdRelation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 3),
    _EntSensorThresholdRelation_Type()
)
entSensorThresholdRelation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entSensorThresholdRelation.setStatus("current")
_EntSensorThresholdValue_Type = SensorValue
_EntSensorThresholdValue_Object = MibTableColumn
entSensorThresholdValue = _EntSensorThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 4),
    _EntSensorThresholdValue_Type()
)
entSensorThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entSensorThresholdValue.setStatus("current")
_EntSensorThresholdEvaluation_Type = TruthValue
_EntSensorThresholdEvaluation_Object = MibTableColumn
entSensorThresholdEvaluation = _EntSensorThresholdEvaluation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 5),
    _EntSensorThresholdEvaluation_Type()
)
entSensorThresholdEvaluation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entSensorThresholdEvaluation.setStatus("current")
_EntSensorThresholdNotificationEnable_Type = TruthValue
_EntSensorThresholdNotificationEnable_Object = MibTableColumn
entSensorThresholdNotificationEnable = _EntSensorThresholdNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 6),
    _EntSensorThresholdNotificationEnable_Type()
)
entSensorThresholdNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entSensorThresholdNotificationEnable.setStatus("current")
_EntitySensorMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
entitySensorMIBNotificationPrefix = _EntitySensorMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 2)
)
_EntitySensorMIBNotifications_ObjectIdentity = ObjectIdentity
entitySensorMIBNotifications = _EntitySensorMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0)
)
_EntitySensorMIBConformance_ObjectIdentity = ObjectIdentity
entitySensorMIBConformance = _EntitySensorMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 3)
)
_EntitySensorMIBCompliances_ObjectIdentity = ObjectIdentity
entitySensorMIBCompliances = _EntitySensorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1)
)
_EntitySensorMIBGroups_ObjectIdentity = ObjectIdentity
entitySensorMIBGroups = _EntitySensorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2)
)

# Managed Objects groups

entitySensorValueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 1)
)
entitySensorValueGroup.setObjects(
      *(("CISCO-ENTITY-SENSOR-MIB", "entSensorType"),
        ("CISCO-ENTITY-SENSOR-MIB", "entSensorScale"),
        ("CISCO-ENTITY-SENSOR-MIB", "entSensorPrecision"),
        ("CISCO-ENTITY-SENSOR-MIB", "entSensorValue"),
        ("CISCO-ENTITY-SENSOR-MIB", "entSensorStatus"),
        ("CISCO-ENTITY-SENSOR-MIB", "entSensorValueTimeStamp"),
        ("CISCO-ENTITY-SENSOR-MIB", "entSensorValueUpdateRate"))
)
if mibBuilder.loadTexts:
    entitySensorValueGroup.setStatus("current")

entitySensorThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 2)
)
entitySensorThresholdGroup.setObjects(
      *(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdSeverity"),
        ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdRelation"),
        ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdValue"),
        ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdEvaluation"),
        ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdNotificationEnable"))
)
if mibBuilder.loadTexts:
    entitySensorThresholdGroup.setStatus("current")


# Notification objects

entSensorThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0, 1)
)
entSensorThresholdNotification.setObjects(
      *(("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdValue"),
        ("CISCO-ENTITY-SENSOR-MIB", "entSensorValue"))
)
if mibBuilder.loadTexts:
    entSensorThresholdNotification.setStatus(
        "current"
    )


# Notifications groups

entitySensorThresholdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 3)
)
entitySensorThresholdNotificationGroup.setObjects(
    ("CISCO-ENTITY-SENSOR-MIB", "entSensorThresholdNotification")
)
if mibBuilder.loadTexts:
    entitySensorThresholdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

entitySensorMIBComplianceV01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 1)
)
entitySensorMIBComplianceV01.setObjects(
      *(("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"),
        ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"),
        ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"))
)
if mibBuilder.loadTexts:
    entitySensorMIBComplianceV01.setStatus(
        "deprecated"
    )

entitySensorMIBComplianceV02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1, 2)
)
entitySensorMIBComplianceV02.setObjects(
      *(("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdGroup"),
        ("CISCO-ENTITY-SENSOR-MIB", "entitySensorValueGroup"),
        ("CISCO-ENTITY-SENSOR-MIB", "entitySensorThresholdNotificationGroup"))
)
if mibBuilder.loadTexts:
    entitySensorMIBComplianceV02.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-SENSOR-MIB",
    **{"SensorDataType": SensorDataType,
       "SensorDataScale": SensorDataScale,
       "SensorPrecision": SensorPrecision,
       "SensorValue": SensorValue,
       "SensorStatus": SensorStatus,
       "SensorValueUpdateRate": SensorValueUpdateRate,
       "SensorThresholdSeverity": SensorThresholdSeverity,
       "SensorThresholdRelation": SensorThresholdRelation,
       "entitySensorMIB": entitySensorMIB,
       "entitySensorMIBObjects": entitySensorMIBObjects,
       "entSensorValues": entSensorValues,
       "entSensorValueTable": entSensorValueTable,
       "entSensorValueEntry": entSensorValueEntry,
       "entSensorType": entSensorType,
       "entSensorScale": entSensorScale,
       "entSensorPrecision": entSensorPrecision,
       "entSensorValue": entSensorValue,
       "entSensorStatus": entSensorStatus,
       "entSensorValueTimeStamp": entSensorValueTimeStamp,
       "entSensorValueUpdateRate": entSensorValueUpdateRate,
       "entSensorMeasuredEntity": entSensorMeasuredEntity,
       "entSensorThresholds": entSensorThresholds,
       "entSensorThresholdTable": entSensorThresholdTable,
       "entSensorThresholdEntry": entSensorThresholdEntry,
       "entSensorThresholdIndex": entSensorThresholdIndex,
       "entSensorThresholdSeverity": entSensorThresholdSeverity,
       "entSensorThresholdRelation": entSensorThresholdRelation,
       "entSensorThresholdValue": entSensorThresholdValue,
       "entSensorThresholdEvaluation": entSensorThresholdEvaluation,
       "entSensorThresholdNotificationEnable": entSensorThresholdNotificationEnable,
       "entitySensorMIBNotificationPrefix": entitySensorMIBNotificationPrefix,
       "entitySensorMIBNotifications": entitySensorMIBNotifications,
       "entSensorThresholdNotification": entSensorThresholdNotification,
       "entitySensorMIBConformance": entitySensorMIBConformance,
       "entitySensorMIBCompliances": entitySensorMIBCompliances,
       "entitySensorMIBComplianceV01": entitySensorMIBComplianceV01,
       "entitySensorMIBComplianceV02": entitySensorMIBComplianceV02,
       "entitySensorMIBGroups": entitySensorMIBGroups,
       "entitySensorValueGroup": entitySensorValueGroup,
       "entitySensorThresholdGroup": entitySensorThresholdGroup,
       "entitySensorThresholdNotificationGroup": entitySensorThresholdNotificationGroup}
)
