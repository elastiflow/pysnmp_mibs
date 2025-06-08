# SNMP MIB module (GUDEADS-ENC2191-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-ENC2191-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:14:59 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

gudeads = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28507)
)
if mibBuilder.loadTexts:
    gudeads.setRevisions(
        ("2007-03-05 13:56",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GadsENC2191_ObjectIdentity = ObjectIdentity
gadsENC2191 = _GadsENC2191_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61)
)
_Enc2191Objects_ObjectIdentity = ObjectIdentity
enc2191Objects = _Enc2191Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1)
)
_Enc2191CommonConfig_ObjectIdentity = ObjectIdentity
enc2191CommonConfig = _Enc2191CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 1)
)
_Enc2191SNMPaccess_ObjectIdentity = ObjectIdentity
enc2191SNMPaccess = _Enc2191SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 1, 1)
)


class _Enc2191TrapCtrl_Type(Integer32):
    """Custom type enc2191TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Enc2191TrapCtrl_Type.__name__ = "Integer32"
_Enc2191TrapCtrl_Object = MibScalar
enc2191TrapCtrl = _Enc2191TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 1, 1, 1),
    _Enc2191TrapCtrl_Type()
)
enc2191TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2191TrapCtrl.setStatus("current")
_Enc2191TrapIPTable_Object = MibTable
enc2191TrapIPTable = _Enc2191TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    enc2191TrapIPTable.setStatus("current")
_Enc2191TrapIPEntry_Object = MibTableRow
enc2191TrapIPEntry = _Enc2191TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 1, 1, 2, 1)
)
enc2191TrapIPEntry.setIndexNames(
    (0, "GUDEADS-ENC2191-MIB", "enc2191TrapIPIndex"),
)
if mibBuilder.loadTexts:
    enc2191TrapIPEntry.setStatus("current")


class _Enc2191TrapIPIndex_Type(Integer32):
    """Custom type enc2191TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Enc2191TrapIPIndex_Type.__name__ = "Integer32"
_Enc2191TrapIPIndex_Object = MibTableColumn
enc2191TrapIPIndex = _Enc2191TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 1, 1, 2, 1, 1),
    _Enc2191TrapIPIndex_Type()
)
enc2191TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191TrapIPIndex.setStatus("current")


class _Enc2191TrapAddr_Type(OctetString):
    """Custom type enc2191TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Enc2191TrapAddr_Type.__name__ = "OctetString"
_Enc2191TrapAddr_Object = MibTableColumn
enc2191TrapAddr = _Enc2191TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 1, 1, 2, 1, 2),
    _Enc2191TrapAddr_Type()
)
enc2191TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2191TrapAddr.setStatus("current")
_Enc2191DeviceConfig_ObjectIdentity = ObjectIdentity
enc2191DeviceConfig = _Enc2191DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 2)
)
_Enc2191IntActors_ObjectIdentity = ObjectIdentity
enc2191IntActors = _Enc2191IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 3)
)
_Enc2191relayports_ObjectIdentity = ObjectIdentity
enc2191relayports = _Enc2191relayports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 3, 1)
)


class _Enc2191portNumber_Type(Integer32):
    """Custom type enc2191portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Enc2191portNumber_Type.__name__ = "Integer32"
_Enc2191portNumber_Object = MibScalar
enc2191portNumber = _Enc2191portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 3, 1, 1),
    _Enc2191portNumber_Type()
)
enc2191portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191portNumber.setStatus("current")
_Enc2191portTable_Object = MibTable
enc2191portTable = _Enc2191portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    enc2191portTable.setStatus("current")
_Enc2191portEntry_Object = MibTableRow
enc2191portEntry = _Enc2191portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 3, 1, 2, 1)
)
enc2191portEntry.setIndexNames(
    (0, "GUDEADS-ENC2191-MIB", "enc2191PortIndex"),
)
if mibBuilder.loadTexts:
    enc2191portEntry.setStatus("current")


class _Enc2191PortIndex_Type(Integer32):
    """Custom type enc2191PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Enc2191PortIndex_Type.__name__ = "Integer32"
_Enc2191PortIndex_Object = MibTableColumn
enc2191PortIndex = _Enc2191PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 3, 1, 2, 1, 1),
    _Enc2191PortIndex_Type()
)
enc2191PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191PortIndex.setStatus("current")


class _Enc2191PortName_Type(OctetString):
    """Custom type enc2191PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Enc2191PortName_Type.__name__ = "OctetString"
_Enc2191PortName_Object = MibTableColumn
enc2191PortName = _Enc2191PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 3, 1, 2, 1, 2),
    _Enc2191PortName_Type()
)
enc2191PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2191PortName.setStatus("current")


class _Enc2191PortState_Type(Integer32):
    """Custom type enc2191PortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Enc2191PortState_Type.__name__ = "Integer32"
_Enc2191PortState_Object = MibTableColumn
enc2191PortState = _Enc2191PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 3, 1, 2, 1, 3),
    _Enc2191PortState_Type()
)
enc2191PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2191PortState.setStatus("current")
_Enc2191PortSwitchCount_Type = Integer32
_Enc2191PortSwitchCount_Object = MibTableColumn
enc2191PortSwitchCount = _Enc2191PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 3, 1, 2, 1, 4),
    _Enc2191PortSwitchCount_Type()
)
enc2191PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191PortSwitchCount.setStatus("current")


class _Enc2191PortStartupMode_Type(Integer32):
    """Custom type enc2191PortStartupMode based on Integer32"""
    defaultValue = 0

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
          ("laststate", 2))
    )


_Enc2191PortStartupMode_Type.__name__ = "Integer32"
_Enc2191PortStartupMode_Object = MibTableColumn
enc2191PortStartupMode = _Enc2191PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 3, 1, 2, 1, 5),
    _Enc2191PortStartupMode_Type()
)
enc2191PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2191PortStartupMode.setStatus("current")


class _Enc2191PortStartupDelay_Type(Integer32):
    """Custom type enc2191PortStartupDelay based on Integer32"""
    defaultValue = 0


_Enc2191PortStartupDelay_Type.__name__ = "Integer32"
_Enc2191PortStartupDelay_Object = MibTableColumn
enc2191PortStartupDelay = _Enc2191PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 3, 1, 2, 1, 6),
    _Enc2191PortStartupDelay_Type()
)
enc2191PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2191PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    enc2191PortStartupDelay.setUnits("seconds")


class _Enc2191PortRepowerTime_Type(Integer32):
    """Custom type enc2191PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Enc2191PortRepowerTime_Type.__name__ = "Integer32"
_Enc2191PortRepowerTime_Object = MibTableColumn
enc2191PortRepowerTime = _Enc2191PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 3, 1, 2, 1, 7),
    _Enc2191PortRepowerTime_Type()
)
enc2191PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2191PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    enc2191PortRepowerTime.setUnits("seconds")
_Enc2191ExtActors_ObjectIdentity = ObjectIdentity
enc2191ExtActors = _Enc2191ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 4)
)
_Enc2191IntSensors_ObjectIdentity = ObjectIdentity
enc2191IntSensors = _Enc2191IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 5)
)
_Enc2191Inputs_ObjectIdentity = ObjectIdentity
enc2191Inputs = _Enc2191Inputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 5, 6)
)


class _Enc2191ActiveInputs_Type(Unsigned32):
    """Custom type enc2191ActiveInputs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Enc2191ActiveInputs_Type.__name__ = "Unsigned32"
_Enc2191ActiveInputs_Object = MibScalar
enc2191ActiveInputs = _Enc2191ActiveInputs_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 5, 6, 1),
    _Enc2191ActiveInputs_Type()
)
enc2191ActiveInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191ActiveInputs.setStatus("current")
_Enc2191InputTable_Object = MibTable
enc2191InputTable = _Enc2191InputTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    enc2191InputTable.setStatus("current")
_Enc2191InputEntry_Object = MibTableRow
enc2191InputEntry = _Enc2191InputEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 5, 6, 2, 1)
)
enc2191InputEntry.setIndexNames(
    (0, "GUDEADS-ENC2191-MIB", "enc2191InputIndex"),
)
if mibBuilder.loadTexts:
    enc2191InputEntry.setStatus("current")


class _Enc2191InputIndex_Type(Integer32):
    """Custom type enc2191InputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Enc2191InputIndex_Type.__name__ = "Integer32"
_Enc2191InputIndex_Object = MibTableColumn
enc2191InputIndex = _Enc2191InputIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 5, 6, 2, 1, 1),
    _Enc2191InputIndex_Type()
)
enc2191InputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191InputIndex.setStatus("current")


class _Enc2191Input_Type(Integer32):
    """Custom type enc2191Input based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lo", 0),
          ("hi", 1))
    )


_Enc2191Input_Type.__name__ = "Integer32"
_Enc2191Input_Object = MibTableColumn
enc2191Input = _Enc2191Input_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 5, 6, 2, 1, 2),
    _Enc2191Input_Type()
)
enc2191Input.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191Input.setStatus("current")
_Enc2191VoltageInfo_ObjectIdentity = ObjectIdentity
enc2191VoltageInfo = _Enc2191VoltageInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 5, 7)
)


class _Enc2191State12V_Type(Integer32):
    """Custom type enc2191State12V based on Integer32"""
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
        *(("off", 0),
          ("low", 1),
          ("high", 2),
          ("error", 3))
    )


_Enc2191State12V_Type.__name__ = "Integer32"
_Enc2191State12V_Object = MibScalar
enc2191State12V = _Enc2191State12V_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 5, 7, 1),
    _Enc2191State12V_Type()
)
enc2191State12V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191State12V.setStatus("current")


class _Enc2191State3V_Type(Integer32):
    """Custom type enc2191State3V based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("error", 3))
    )


_Enc2191State3V_Type.__name__ = "Integer32"
_Enc2191State3V_Object = MibScalar
enc2191State3V = _Enc2191State3V_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 5, 7, 2),
    _Enc2191State3V_Type()
)
enc2191State3V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191State3V.setStatus("current")


class _Enc2191POE_Type(Integer32):
    """Custom type enc2191POE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enc2191POE_Type.__name__ = "Integer32"
_Enc2191POE_Object = MibScalar
enc2191POE = _Enc2191POE_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 5, 10),
    _Enc2191POE_Type()
)
enc2191POE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191POE.setStatus("current")
if mibBuilder.loadTexts:
    enc2191POE.setUnits("0 = no POE, 1 = POE available")
_Enc2191ExtSensors_ObjectIdentity = ObjectIdentity
enc2191ExtSensors = _Enc2191ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 6)
)
_Enc2191SensorTable_Object = MibTable
enc2191SensorTable = _Enc2191SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 6, 1)
)
if mibBuilder.loadTexts:
    enc2191SensorTable.setStatus("current")
_Enc2191SensorEntry_Object = MibTableRow
enc2191SensorEntry = _Enc2191SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 6, 1, 1)
)
enc2191SensorEntry.setIndexNames(
    (0, "GUDEADS-ENC2191-MIB", "enc2191SensorIndex"),
)
if mibBuilder.loadTexts:
    enc2191SensorEntry.setStatus("current")


class _Enc2191SensorIndex_Type(Integer32):
    """Custom type enc2191SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Enc2191SensorIndex_Type.__name__ = "Integer32"
_Enc2191SensorIndex_Object = MibTableColumn
enc2191SensorIndex = _Enc2191SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 6, 1, 1, 1),
    _Enc2191SensorIndex_Type()
)
enc2191SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191SensorIndex.setStatus("current")
_Enc2191TempSensor_Type = Integer32
_Enc2191TempSensor_Object = MibTableColumn
enc2191TempSensor = _Enc2191TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 6, 1, 1, 2),
    _Enc2191TempSensor_Type()
)
enc2191TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    enc2191TempSensor.setUnits("0.1 degree Celsius")
_Enc2191HygroSensor_Type = Integer32
_Enc2191HygroSensor_Object = MibTableColumn
enc2191HygroSensor = _Enc2191HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 6, 1, 1, 3),
    _Enc2191HygroSensor_Type()
)
enc2191HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    enc2191HygroSensor.setUnits("0.1 percent humidity")


class _Enc2191InputSensor_Type(Integer32):
    """Custom type enc2191InputSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Enc2191InputSensor_Type.__name__ = "Integer32"
_Enc2191InputSensor_Object = MibTableColumn
enc2191InputSensor = _Enc2191InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 6, 1, 1, 4),
    _Enc2191InputSensor_Type()
)
enc2191InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191InputSensor.setStatus("current")
_Enc2191AirPressure_Type = Integer32
_Enc2191AirPressure_Object = MibTableColumn
enc2191AirPressure = _Enc2191AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 6, 1, 1, 5),
    _Enc2191AirPressure_Type()
)
enc2191AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    enc2191AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Enc2191DewPoint_Type = Integer32
_Enc2191DewPoint_Object = MibTableColumn
enc2191DewPoint = _Enc2191DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 6, 1, 1, 6),
    _Enc2191DewPoint_Type()
)
enc2191DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    enc2191DewPoint.setUnits("0.1 degree Celsius")
_Enc2191DewPointDiff_Type = Integer32
_Enc2191DewPointDiff_Object = MibTableColumn
enc2191DewPointDiff = _Enc2191DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 61, 1, 6, 1, 1, 7),
    _Enc2191DewPointDiff_Type()
)
enc2191DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2191DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    enc2191DewPointDiff.setUnits("0.1 degree Celsius")
_Enc2191Conf_ObjectIdentity = ObjectIdentity
enc2191Conf = _Enc2191Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 2)
)
_Enc2191Groups_ObjectIdentity = ObjectIdentity
enc2191Groups = _Enc2191Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 2, 1)
)
_Enc2191Compls_ObjectIdentity = ObjectIdentity
enc2191Compls = _Enc2191Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 61, 3)
)

# Managed Objects groups

enc2191BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 61, 2, 1, 1)
)
enc2191BasicGroup.setObjects(
      *(("GUDEADS-ENC2191-MIB", "enc2191TrapCtrl"),
        ("GUDEADS-ENC2191-MIB", "enc2191TrapIPIndex"),
        ("GUDEADS-ENC2191-MIB", "enc2191TrapAddr"),
        ("GUDEADS-ENC2191-MIB", "enc2191portNumber"),
        ("GUDEADS-ENC2191-MIB", "enc2191PortIndex"),
        ("GUDEADS-ENC2191-MIB", "enc2191PortName"),
        ("GUDEADS-ENC2191-MIB", "enc2191PortState"),
        ("GUDEADS-ENC2191-MIB", "enc2191PortSwitchCount"),
        ("GUDEADS-ENC2191-MIB", "enc2191PortStartupMode"),
        ("GUDEADS-ENC2191-MIB", "enc2191PortStartupDelay"),
        ("GUDEADS-ENC2191-MIB", "enc2191PortRepowerTime"),
        ("GUDEADS-ENC2191-MIB", "enc2191ActiveInputs"),
        ("GUDEADS-ENC2191-MIB", "enc2191InputIndex"),
        ("GUDEADS-ENC2191-MIB", "enc2191Input"),
        ("GUDEADS-ENC2191-MIB", "enc2191State12V"),
        ("GUDEADS-ENC2191-MIB", "enc2191State3V"),
        ("GUDEADS-ENC2191-MIB", "enc2191POE"),
        ("GUDEADS-ENC2191-MIB", "enc2191SensorIndex"),
        ("GUDEADS-ENC2191-MIB", "enc2191TempSensor"),
        ("GUDEADS-ENC2191-MIB", "enc2191HygroSensor"),
        ("GUDEADS-ENC2191-MIB", "enc2191InputSensor"),
        ("GUDEADS-ENC2191-MIB", "enc2191AirPressure"),
        ("GUDEADS-ENC2191-MIB", "enc2191DewPoint"),
        ("GUDEADS-ENC2191-MIB", "enc2191DewPointDiff"))
)
if mibBuilder.loadTexts:
    enc2191BasicGroup.setStatus("current")


# Notification objects

enc2191SwitchEvtPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 61, 3, 1)
)
enc2191SwitchEvtPort.setObjects(
      *(("GUDEADS-ENC2191-MIB", "enc2191PortIndex"),
        ("GUDEADS-ENC2191-MIB", "enc2191PortName"),
        ("GUDEADS-ENC2191-MIB", "enc2191PortState"),
        ("GUDEADS-ENC2191-MIB", "enc2191PortSwitchCount"))
)
if mibBuilder.loadTexts:
    enc2191SwitchEvtPort.setStatus(
        "current"
    )

enc2191InputEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 61, 3, 2)
)
enc2191InputEvt.setObjects(
      *(("GUDEADS-ENC2191-MIB", "enc2191InputIndex"),
        ("GUDEADS-ENC2191-MIB", "enc2191Input"))
)
if mibBuilder.loadTexts:
    enc2191InputEvt.setStatus(
        "current"
    )

enc2191TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 61, 3, 3)
)
enc2191TempEvtSen.setObjects(
      *(("GUDEADS-ENC2191-MIB", "enc2191SensorIndex"),
        ("GUDEADS-ENC2191-MIB", "enc2191TempSensor"))
)
if mibBuilder.loadTexts:
    enc2191TempEvtSen.setStatus(
        "current"
    )

enc2191HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 61, 3, 4)
)
enc2191HygroEvtSen.setObjects(
      *(("GUDEADS-ENC2191-MIB", "enc2191SensorIndex"),
        ("GUDEADS-ENC2191-MIB", "enc2191HygroSensor"))
)
if mibBuilder.loadTexts:
    enc2191HygroEvtSen.setStatus(
        "current"
    )

enc2191InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 61, 3, 5)
)
enc2191InputEvtSen.setObjects(
      *(("GUDEADS-ENC2191-MIB", "enc2191SensorIndex"),
        ("GUDEADS-ENC2191-MIB", "enc2191InputSensor"))
)
if mibBuilder.loadTexts:
    enc2191InputEvtSen.setStatus(
        "current"
    )

enc2191AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 61, 3, 6)
)
enc2191AirPressureEvtSen.setObjects(
      *(("GUDEADS-ENC2191-MIB", "enc2191SensorIndex"),
        ("GUDEADS-ENC2191-MIB", "enc2191AirPressure"))
)
if mibBuilder.loadTexts:
    enc2191AirPressureEvtSen.setStatus(
        "current"
    )

enc2191DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 61, 3, 7)
)
enc2191DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-ENC2191-MIB", "enc2191SensorIndex"),
        ("GUDEADS-ENC2191-MIB", "enc2191DewPointDiff"))
)
if mibBuilder.loadTexts:
    enc2191DewPtDiffEvtSen.setStatus(
        "current"
    )

enc2191POEEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 61, 3, 8)
)
enc2191POEEvt.setObjects(
    ("GUDEADS-ENC2191-MIB", "enc2191POE")
)
if mibBuilder.loadTexts:
    enc2191POEEvt.setStatus(
        "current"
    )


# Notifications groups

enc2191NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 61, 2, 1, 2)
)
enc2191NotificationGroup.setObjects(
      *(("GUDEADS-ENC2191-MIB", "enc2191SwitchEvtPort"),
        ("GUDEADS-ENC2191-MIB", "enc2191InputEvt"),
        ("GUDEADS-ENC2191-MIB", "enc2191TempEvtSen"),
        ("GUDEADS-ENC2191-MIB", "enc2191HygroEvtSen"),
        ("GUDEADS-ENC2191-MIB", "enc2191InputEvtSen"),
        ("GUDEADS-ENC2191-MIB", "enc2191AirPressureEvtSen"),
        ("GUDEADS-ENC2191-MIB", "enc2191DewPtDiffEvtSen"),
        ("GUDEADS-ENC2191-MIB", "enc2191POEEvt"))
)
if mibBuilder.loadTexts:
    enc2191NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-ENC2191-MIB",
    **{"gudeads": gudeads,
       "gadsENC2191": gadsENC2191,
       "enc2191Objects": enc2191Objects,
       "enc2191CommonConfig": enc2191CommonConfig,
       "enc2191SNMPaccess": enc2191SNMPaccess,
       "enc2191TrapCtrl": enc2191TrapCtrl,
       "enc2191TrapIPTable": enc2191TrapIPTable,
       "enc2191TrapIPEntry": enc2191TrapIPEntry,
       "enc2191TrapIPIndex": enc2191TrapIPIndex,
       "enc2191TrapAddr": enc2191TrapAddr,
       "enc2191DeviceConfig": enc2191DeviceConfig,
       "enc2191IntActors": enc2191IntActors,
       "enc2191relayports": enc2191relayports,
       "enc2191portNumber": enc2191portNumber,
       "enc2191portTable": enc2191portTable,
       "enc2191portEntry": enc2191portEntry,
       "enc2191PortIndex": enc2191PortIndex,
       "enc2191PortName": enc2191PortName,
       "enc2191PortState": enc2191PortState,
       "enc2191PortSwitchCount": enc2191PortSwitchCount,
       "enc2191PortStartupMode": enc2191PortStartupMode,
       "enc2191PortStartupDelay": enc2191PortStartupDelay,
       "enc2191PortRepowerTime": enc2191PortRepowerTime,
       "enc2191ExtActors": enc2191ExtActors,
       "enc2191IntSensors": enc2191IntSensors,
       "enc2191Inputs": enc2191Inputs,
       "enc2191ActiveInputs": enc2191ActiveInputs,
       "enc2191InputTable": enc2191InputTable,
       "enc2191InputEntry": enc2191InputEntry,
       "enc2191InputIndex": enc2191InputIndex,
       "enc2191Input": enc2191Input,
       "enc2191VoltageInfo": enc2191VoltageInfo,
       "enc2191State12V": enc2191State12V,
       "enc2191State3V": enc2191State3V,
       "enc2191POE": enc2191POE,
       "enc2191ExtSensors": enc2191ExtSensors,
       "enc2191SensorTable": enc2191SensorTable,
       "enc2191SensorEntry": enc2191SensorEntry,
       "enc2191SensorIndex": enc2191SensorIndex,
       "enc2191TempSensor": enc2191TempSensor,
       "enc2191HygroSensor": enc2191HygroSensor,
       "enc2191InputSensor": enc2191InputSensor,
       "enc2191AirPressure": enc2191AirPressure,
       "enc2191DewPoint": enc2191DewPoint,
       "enc2191DewPointDiff": enc2191DewPointDiff,
       "enc2191Conf": enc2191Conf,
       "enc2191Groups": enc2191Groups,
       "enc2191BasicGroup": enc2191BasicGroup,
       "enc2191NotificationGroup": enc2191NotificationGroup,
       "enc2191Compls": enc2191Compls,
       "events": events,
       "enc2191SwitchEvtPort": enc2191SwitchEvtPort,
       "enc2191InputEvt": enc2191InputEvt,
       "enc2191TempEvtSen": enc2191TempEvtSen,
       "enc2191HygroEvtSen": enc2191HygroEvtSen,
       "enc2191InputEvtSen": enc2191InputEvtSen,
       "enc2191AirPressureEvtSen": enc2191AirPressureEvtSen,
       "enc2191DewPtDiffEvtSen": enc2191DewPtDiffEvtSen,
       "enc2191POEEvt": enc2191POEEvt}
)
