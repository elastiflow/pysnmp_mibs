# SNMP MIB module (DIGI-POWER-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-POWER-MANAGEMENT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:30 2025
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

(digiPowerMgmt,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiPowerMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PowerMgmtTable_Object = MibTable
powerMgmtTable = _PowerMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 11)
)
if mibBuilder.loadTexts:
    powerMgmtTable.setStatus("mandatory")
_PowerMgmtEntry_Object = MibTableRow
powerMgmtEntry = _PowerMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 11, 1)
)
if mibBuilder.loadTexts:
    powerMgmtEntry.setStatus("mandatory")
_PowerMgmtNumPorts_Type = Integer32
_PowerMgmtNumPorts_Object = MibTableColumn
powerMgmtNumPorts = _PowerMgmtNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 11, 1, 1),
    _PowerMgmtNumPorts_Type()
)
powerMgmtNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerMgmtNumPorts.setStatus("mandatory")


class _PowerMgmtCurrThreshExcTraps_Type(Integer32):
    """Custom type powerMgmtCurrThreshExcTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PowerMgmtCurrThreshExcTraps_Type.__name__ = "Integer32"
_PowerMgmtCurrThreshExcTraps_Object = MibTableColumn
powerMgmtCurrThreshExcTraps = _PowerMgmtCurrThreshExcTraps_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 11, 1, 2),
    _PowerMgmtCurrThreshExcTraps_Type()
)
powerMgmtCurrThreshExcTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtCurrThreshExcTraps.setStatus("mandatory")


class _PowerMgmtTempThreshExcTraps_Type(Integer32):
    """Custom type powerMgmtTempThreshExcTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PowerMgmtTempThreshExcTraps_Type.__name__ = "Integer32"
_PowerMgmtTempThreshExcTraps_Object = MibTableColumn
powerMgmtTempThreshExcTraps = _PowerMgmtTempThreshExcTraps_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 11, 1, 3),
    _PowerMgmtTempThreshExcTraps_Type()
)
powerMgmtTempThreshExcTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMgmtTempThreshExcTraps.setStatus("mandatory")
_PowerMgmtPowerUnitTable_Object = MibTable
powerMgmtPowerUnitTable = _PowerMgmtPowerUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 12)
)
if mibBuilder.loadTexts:
    powerMgmtPowerUnitTable.setStatus("mandatory")
_PowerMgmtPowerUnitEntry_Object = MibTableRow
powerMgmtPowerUnitEntry = _PowerMgmtPowerUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 12, 1)
)
powerMgmtPowerUnitEntry.setIndexNames(
    (0, "DIGI-POWER-MANAGEMENT-MIB", "powerUnitPort"),
)
if mibBuilder.loadTexts:
    powerMgmtPowerUnitEntry.setStatus("mandatory")


class _PowerUnitPort_Type(Integer32):
    """Custom type powerUnitPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PowerUnitPort_Type.__name__ = "Integer32"
_PowerUnitPort_Object = MibTableColumn
powerUnitPort = _PowerUnitPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 12, 1, 1),
    _PowerUnitPort_Type()
)
powerUnitPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitPort.setStatus("mandatory")


class _PowerUnitStatus_Type(Integer32):
    """Custom type powerUnitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not_configured", 0),
          ("disconnected", 1),
          ("connecting", 2),
          ("connected", 3))
    )


_PowerUnitStatus_Type.__name__ = "Integer32"
_PowerUnitStatus_Object = MibTableColumn
powerUnitStatus = _PowerUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 12, 1, 2),
    _PowerUnitStatus_Type()
)
powerUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitStatus.setStatus("mandatory")
_PowerUnitType_Type = OctetString
_PowerUnitType_Object = MibTableColumn
powerUnitType = _PowerUnitType_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 12, 1, 3),
    _PowerUnitType_Type()
)
powerUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitType.setStatus("mandatory")
_PowerUnitNumOutlets_Type = Integer32
_PowerUnitNumOutlets_Object = MibTableColumn
powerUnitNumOutlets = _PowerUnitNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 12, 1, 4),
    _PowerUnitNumOutlets_Type()
)
powerUnitNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitNumOutlets.setStatus("mandatory")
_PowerUnitNumCurrSensors_Type = Integer32
_PowerUnitNumCurrSensors_Object = MibTableColumn
powerUnitNumCurrSensors = _PowerUnitNumCurrSensors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 12, 1, 5),
    _PowerUnitNumCurrSensors_Type()
)
powerUnitNumCurrSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitNumCurrSensors.setStatus("mandatory")
_PowerUnitNumTempSensors_Type = Integer32
_PowerUnitNumTempSensors_Object = MibTableColumn
powerUnitNumTempSensors = _PowerUnitNumTempSensors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 12, 1, 6),
    _PowerUnitNumTempSensors_Type()
)
powerUnitNumTempSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitNumTempSensors.setStatus("mandatory")
_PowerMgmtCurrSensorsTable_Object = MibTable
powerMgmtCurrSensorsTable = _PowerMgmtCurrSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 13)
)
if mibBuilder.loadTexts:
    powerMgmtCurrSensorsTable.setStatus("mandatory")
_PowerMgmtCurrSensorsEntry_Object = MibTableRow
powerMgmtCurrSensorsEntry = _PowerMgmtCurrSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 13, 1)
)
powerMgmtCurrSensorsEntry.setIndexNames(
    (0, "DIGI-POWER-MANAGEMENT-MIB", "sesnorCurrPort"),
    (0, "DIGI-POWER-MANAGEMENT-MIB", "sensorCurrIndex"),
)
if mibBuilder.loadTexts:
    powerMgmtCurrSensorsEntry.setStatus("mandatory")


class _SensorCurrPort_Type(Integer32):
    """Custom type sensorCurrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SensorCurrPort_Type.__name__ = "Integer32"
_SensorCurrPort_Object = MibTableColumn
sensorCurrPort = _SensorCurrPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 13, 1, 1),
    _SensorCurrPort_Type()
)
sensorCurrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorCurrPort.setStatus("mandatory")


class _SensorCurrIndex_Type(Integer32):
    """Custom type sensorCurrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SensorCurrIndex_Type.__name__ = "Integer32"
_SensorCurrIndex_Object = MibTableColumn
sensorCurrIndex = _SensorCurrIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 13, 1, 2),
    _SensorCurrIndex_Type()
)
sensorCurrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorCurrIndex.setStatus("mandatory")
_SensorActualCurr_Type = Integer32
_SensorActualCurr_Object = MibTableColumn
sensorActualCurr = _SensorActualCurr_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 13, 1, 3),
    _SensorActualCurr_Type()
)
sensorActualCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorActualCurr.setStatus("mandatory")
_SensorMaxCurr_Type = Integer32
_SensorMaxCurr_Object = MibTableColumn
sensorMaxCurr = _SensorMaxCurr_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 13, 1, 4),
    _SensorMaxCurr_Type()
)
sensorMaxCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorMaxCurr.setStatus("mandatory")
_SensorThreshCurr_Type = Integer32
_SensorThreshCurr_Object = MibTableColumn
sensorThreshCurr = _SensorThreshCurr_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 13, 1, 5),
    _SensorThreshCurr_Type()
)
sensorThreshCurr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorThreshCurr.setStatus("mandatory")
_PowerMgmtTempSensorsTable_Object = MibTable
powerMgmtTempSensorsTable = _PowerMgmtTempSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 14)
)
if mibBuilder.loadTexts:
    powerMgmtTempSensorsTable.setStatus("mandatory")
_PowerMgmtTempSensorsEntry_Object = MibTableRow
powerMgmtTempSensorsEntry = _PowerMgmtTempSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 14, 1)
)
powerMgmtTempSensorsEntry.setIndexNames(
    (0, "DIGI-POWER-MANAGEMENT-MIB", "sensorTempPort"),
    (0, "DIGI-POWER-MANAGEMENT-MIB", "sensorTempIndex"),
)
if mibBuilder.loadTexts:
    powerMgmtTempSensorsEntry.setStatus("mandatory")


class _SensorTempPort_Type(Integer32):
    """Custom type sensorTempPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SensorTempPort_Type.__name__ = "Integer32"
_SensorTempPort_Object = MibTableColumn
sensorTempPort = _SensorTempPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 14, 1, 1),
    _SensorTempPort_Type()
)
sensorTempPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempPort.setStatus("mandatory")


class _SensorTempIndex_Type(Integer32):
    """Custom type sensorTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SensorTempIndex_Type.__name__ = "Integer32"
_SensorTempIndex_Object = MibTableColumn
sensorTempIndex = _SensorTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 14, 1, 2),
    _SensorTempIndex_Type()
)
sensorTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorTempIndex.setStatus("mandatory")
_SensorActualTemp_Type = Integer32
_SensorActualTemp_Object = MibTableColumn
sensorActualTemp = _SensorActualTemp_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 14, 1, 3),
    _SensorActualTemp_Type()
)
sensorActualTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorActualTemp.setStatus("mandatory")
_SensorThreshTemp_Type = Integer32
_SensorThreshTemp_Object = MibTableColumn
sensorThreshTemp = _SensorThreshTemp_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 14, 14, 1, 4),
    _SensorThreshTemp_Type()
)
sensorThreshTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorThreshTemp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-POWER-MANAGEMENT-MIB",
    **{"DisplayString": DisplayString,
       "powerMgmtTable": powerMgmtTable,
       "powerMgmtEntry": powerMgmtEntry,
       "powerMgmtNumPorts": powerMgmtNumPorts,
       "powerMgmtCurrThreshExcTraps": powerMgmtCurrThreshExcTraps,
       "powerMgmtTempThreshExcTraps": powerMgmtTempThreshExcTraps,
       "powerMgmtPowerUnitTable": powerMgmtPowerUnitTable,
       "powerMgmtPowerUnitEntry": powerMgmtPowerUnitEntry,
       "powerUnitPort": powerUnitPort,
       "powerUnitStatus": powerUnitStatus,
       "powerUnitType": powerUnitType,
       "powerUnitNumOutlets": powerUnitNumOutlets,
       "powerUnitNumCurrSensors": powerUnitNumCurrSensors,
       "powerUnitNumTempSensors": powerUnitNumTempSensors,
       "powerMgmtCurrSensorsTable": powerMgmtCurrSensorsTable,
       "powerMgmtCurrSensorsEntry": powerMgmtCurrSensorsEntry,
       "sensorCurrPort": sensorCurrPort,
       "sensorCurrIndex": sensorCurrIndex,
       "sensorActualCurr": sensorActualCurr,
       "sensorMaxCurr": sensorMaxCurr,
       "sensorThreshCurr": sensorThreshCurr,
       "powerMgmtTempSensorsTable": powerMgmtTempSensorsTable,
       "powerMgmtTempSensorsEntry": powerMgmtTempSensorsEntry,
       "sensorTempPort": sensorTempPort,
       "sensorTempIndex": sensorTempIndex,
       "sensorActualTemp": sensorActualTemp,
       "sensorThreshTemp": sensorThreshTemp}
)
