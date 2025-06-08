# SNMP MIB module (CUMULUS-SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cumulus_40310/CUMULUS-SENSOR-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:08:37 2025
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

(cumulusMib,) = mibBuilder.importSymbols(
    "CUMULUS-SNMP-MIB",
    "cumulusMib")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

agentSwitchSensorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EntitySensorDataType(TextualConvention, Integer32):
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
              12)
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
          ("truthvalue", 12))
    )



class EntitySensorDataScale(TextualConvention, Integer32):
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



class EntitySensorPrecision(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8, 9),
    )



class EntitySensorValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )



class EntitySensorStatus(TextualConvention, Integer32):
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



class EntitySensorAlarm(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("normal", 3),
          ("warning", 4),
          ("alert", 5),
          ("critical", 6),
          ("NotPresent", 7),
          ("NotOperational", 8),
          ("unavailable", 9))
    )



class EntityAdminStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("notApplicable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EntitySensorObjects_ObjectIdentity = ObjectIdentity
entitySensorObjects = _EntitySensorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1)
)
_EntPhySensorTable_Object = MibTable
entPhySensorTable = _EntPhySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1)
)
if mibBuilder.loadTexts:
    entPhySensorTable.setStatus("current")
_EntPhySensorEntry_Object = MibTableRow
entPhySensorEntry = _EntPhySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1)
)
entPhySensorEntry.setIndexNames(
    (0, "CUMULUS-SENSOR-MIB", "entPhySensorIndex"),
)
if mibBuilder.loadTexts:
    entPhySensorEntry.setStatus("current")
_EntPhySensorIndex_Type = Integer32
_EntPhySensorIndex_Object = MibTableColumn
entPhySensorIndex = _EntPhySensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 1),
    _EntPhySensorIndex_Type()
)
entPhySensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorIndex.setStatus("current")
_EntPhySensorType_Type = EntitySensorDataType
_EntPhySensorType_Object = MibTableColumn
entPhySensorType = _EntPhySensorType_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 2),
    _EntPhySensorType_Type()
)
entPhySensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorType.setStatus("current")
_EntPhySensorScale_Type = EntitySensorDataScale
_EntPhySensorScale_Object = MibTableColumn
entPhySensorScale = _EntPhySensorScale_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 3),
    _EntPhySensorScale_Type()
)
entPhySensorScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorScale.setStatus("current")
_EntPhySensorPrecision_Type = EntitySensorPrecision
_EntPhySensorPrecision_Object = MibTableColumn
entPhySensorPrecision = _EntPhySensorPrecision_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 4),
    _EntPhySensorPrecision_Type()
)
entPhySensorPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorPrecision.setStatus("current")
_EntPhySensorValue_Type = EntitySensorValue
_EntPhySensorValue_Object = MibTableColumn
entPhySensorValue = _EntPhySensorValue_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 5),
    _EntPhySensorValue_Type()
)
entPhySensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorValue.setStatus("current")
_EntPhySensorOperStatus_Type = EntitySensorStatus
_EntPhySensorOperStatus_Object = MibTableColumn
entPhySensorOperStatus = _EntPhySensorOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 6),
    _EntPhySensorOperStatus_Type()
)
entPhySensorOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorOperStatus.setStatus("current")
_EntPhySensorUnitsDisplay_Type = SnmpAdminString
_EntPhySensorUnitsDisplay_Object = MibTableColumn
entPhySensorUnitsDisplay = _EntPhySensorUnitsDisplay_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 7),
    _EntPhySensorUnitsDisplay_Type()
)
entPhySensorUnitsDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorUnitsDisplay.setStatus("current")
_EntPhySensorValueTimeStamp_Type = TimeStamp
_EntPhySensorValueTimeStamp_Object = MibTableColumn
entPhySensorValueTimeStamp = _EntPhySensorValueTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 8),
    _EntPhySensorValueTimeStamp_Type()
)
entPhySensorValueTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorValueTimeStamp.setStatus("current")
_EntPhySensorValueUpdateRate_Type = Unsigned32
_EntPhySensorValueUpdateRate_Object = MibTableColumn
entPhySensorValueUpdateRate = _EntPhySensorValueUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 9),
    _EntPhySensorValueUpdateRate_Type()
)
entPhySensorValueUpdateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorValueUpdateRate.setStatus("current")
if mibBuilder.loadTexts:
    entPhySensorValueUpdateRate.setUnits("milliseconds")
_EntPhySensorDescr_Type = SnmpAdminString
_EntPhySensorDescr_Object = MibTableColumn
entPhySensorDescr = _EntPhySensorDescr_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 10),
    _EntPhySensorDescr_Type()
)
entPhySensorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorDescr.setStatus("current")
_EntPhySensorMin_Type = EntitySensorValue
_EntPhySensorMin_Object = MibTableColumn
entPhySensorMin = _EntPhySensorMin_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 11),
    _EntPhySensorMin_Type()
)
entPhySensorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorMin.setStatus("current")
_EntPhySensorMax_Type = EntitySensorValue
_EntPhySensorMax_Object = MibTableColumn
entPhySensorMax = _EntPhySensorMax_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 12),
    _EntPhySensorMax_Type()
)
entPhySensorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorMax.setStatus("current")
_EntPhySensorAlarm_Type = EntitySensorAlarm
_EntPhySensorAlarm_Object = MibTableColumn
entPhySensorAlarm = _EntPhySensorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 13),
    _EntPhySensorAlarm_Type()
)
entPhySensorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorAlarm.setStatus("current")
_EntPhySensorAdminStatus_Type = EntityAdminStatus
_EntPhySensorAdminStatus_Object = MibTableColumn
entPhySensorAdminStatus = _EntPhySensorAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 40310, 6, 1, 1, 1, 14),
    _EntPhySensorAdminStatus_Type()
)
entPhySensorAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySensorAdminStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CUMULUS-SENSOR-MIB",
    **{"EntitySensorDataType": EntitySensorDataType,
       "EntitySensorDataScale": EntitySensorDataScale,
       "EntitySensorPrecision": EntitySensorPrecision,
       "EntitySensorValue": EntitySensorValue,
       "EntitySensorStatus": EntitySensorStatus,
       "EntitySensorAlarm": EntitySensorAlarm,
       "EntityAdminStatus": EntityAdminStatus,
       "agentSwitchSensorMIB": agentSwitchSensorMIB,
       "entitySensorObjects": entitySensorObjects,
       "entPhySensorTable": entPhySensorTable,
       "entPhySensorEntry": entPhySensorEntry,
       "entPhySensorIndex": entPhySensorIndex,
       "entPhySensorType": entPhySensorType,
       "entPhySensorScale": entPhySensorScale,
       "entPhySensorPrecision": entPhySensorPrecision,
       "entPhySensorValue": entPhySensorValue,
       "entPhySensorOperStatus": entPhySensorOperStatus,
       "entPhySensorUnitsDisplay": entPhySensorUnitsDisplay,
       "entPhySensorValueTimeStamp": entPhySensorValueTimeStamp,
       "entPhySensorValueUpdateRate": entPhySensorValueUpdateRate,
       "entPhySensorDescr": entPhySensorDescr,
       "entPhySensorMin": entPhySensorMin,
       "entPhySensorMax": entPhySensorMax,
       "entPhySensorAlarm": entPhySensorAlarm,
       "entPhySensorAdminStatus": entPhySensorAdminStatus}
)
