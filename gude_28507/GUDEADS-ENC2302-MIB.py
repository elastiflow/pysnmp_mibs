# SNMP MIB module (GUDEADS-ENC2302-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-ENC2302-MIB.mib
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

_GadsENC2302_ObjectIdentity = ObjectIdentity
gadsENC2302 = _GadsENC2302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70)
)
_Enc2302Objects_ObjectIdentity = ObjectIdentity
enc2302Objects = _Enc2302Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1)
)
_Enc2302CommonConfig_ObjectIdentity = ObjectIdentity
enc2302CommonConfig = _Enc2302CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 1)
)
_Enc2302SNMPaccess_ObjectIdentity = ObjectIdentity
enc2302SNMPaccess = _Enc2302SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 1, 1)
)


class _Enc2302TrapCtrl_Type(Integer32):
    """Custom type enc2302TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Enc2302TrapCtrl_Type.__name__ = "Integer32"
_Enc2302TrapCtrl_Object = MibScalar
enc2302TrapCtrl = _Enc2302TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 1, 1, 1),
    _Enc2302TrapCtrl_Type()
)
enc2302TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2302TrapCtrl.setStatus("current")
_Enc2302TrapIPTable_Object = MibTable
enc2302TrapIPTable = _Enc2302TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    enc2302TrapIPTable.setStatus("current")
_Enc2302TrapIPEntry_Object = MibTableRow
enc2302TrapIPEntry = _Enc2302TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 1, 1, 2, 1)
)
enc2302TrapIPEntry.setIndexNames(
    (0, "GUDEADS-ENC2302-MIB", "enc2302TrapIPIndex"),
)
if mibBuilder.loadTexts:
    enc2302TrapIPEntry.setStatus("current")


class _Enc2302TrapIPIndex_Type(Integer32):
    """Custom type enc2302TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Enc2302TrapIPIndex_Type.__name__ = "Integer32"
_Enc2302TrapIPIndex_Object = MibTableColumn
enc2302TrapIPIndex = _Enc2302TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 1, 1, 2, 1, 1),
    _Enc2302TrapIPIndex_Type()
)
enc2302TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302TrapIPIndex.setStatus("current")


class _Enc2302TrapAddr_Type(OctetString):
    """Custom type enc2302TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Enc2302TrapAddr_Type.__name__ = "OctetString"
_Enc2302TrapAddr_Object = MibTableColumn
enc2302TrapAddr = _Enc2302TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 1, 1, 2, 1, 2),
    _Enc2302TrapAddr_Type()
)
enc2302TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2302TrapAddr.setStatus("current")
_Enc2302DeviceConfig_ObjectIdentity = ObjectIdentity
enc2302DeviceConfig = _Enc2302DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 2)
)
_Enc2302IntActors_ObjectIdentity = ObjectIdentity
enc2302IntActors = _Enc2302IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 3)
)
_Enc2302relayports_ObjectIdentity = ObjectIdentity
enc2302relayports = _Enc2302relayports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 3, 1)
)


class _Enc2302portNumber_Type(Integer32):
    """Custom type enc2302portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Enc2302portNumber_Type.__name__ = "Integer32"
_Enc2302portNumber_Object = MibScalar
enc2302portNumber = _Enc2302portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 3, 1, 1),
    _Enc2302portNumber_Type()
)
enc2302portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302portNumber.setStatus("current")
_Enc2302portTable_Object = MibTable
enc2302portTable = _Enc2302portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    enc2302portTable.setStatus("current")
_Enc2302portEntry_Object = MibTableRow
enc2302portEntry = _Enc2302portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 3, 1, 2, 1)
)
enc2302portEntry.setIndexNames(
    (0, "GUDEADS-ENC2302-MIB", "enc2302PortIndex"),
)
if mibBuilder.loadTexts:
    enc2302portEntry.setStatus("current")


class _Enc2302PortIndex_Type(Integer32):
    """Custom type enc2302PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Enc2302PortIndex_Type.__name__ = "Integer32"
_Enc2302PortIndex_Object = MibTableColumn
enc2302PortIndex = _Enc2302PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 3, 1, 2, 1, 1),
    _Enc2302PortIndex_Type()
)
enc2302PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302PortIndex.setStatus("current")


class _Enc2302PortName_Type(OctetString):
    """Custom type enc2302PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Enc2302PortName_Type.__name__ = "OctetString"
_Enc2302PortName_Object = MibTableColumn
enc2302PortName = _Enc2302PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 3, 1, 2, 1, 2),
    _Enc2302PortName_Type()
)
enc2302PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2302PortName.setStatus("current")


class _Enc2302PortState_Type(Integer32):
    """Custom type enc2302PortState based on Integer32"""
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


_Enc2302PortState_Type.__name__ = "Integer32"
_Enc2302PortState_Object = MibTableColumn
enc2302PortState = _Enc2302PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 3, 1, 2, 1, 3),
    _Enc2302PortState_Type()
)
enc2302PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2302PortState.setStatus("current")
_Enc2302PortSwitchCount_Type = Integer32
_Enc2302PortSwitchCount_Object = MibTableColumn
enc2302PortSwitchCount = _Enc2302PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 3, 1, 2, 1, 4),
    _Enc2302PortSwitchCount_Type()
)
enc2302PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302PortSwitchCount.setStatus("current")


class _Enc2302PortStartupMode_Type(Integer32):
    """Custom type enc2302PortStartupMode based on Integer32"""
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


_Enc2302PortStartupMode_Type.__name__ = "Integer32"
_Enc2302PortStartupMode_Object = MibTableColumn
enc2302PortStartupMode = _Enc2302PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 3, 1, 2, 1, 5),
    _Enc2302PortStartupMode_Type()
)
enc2302PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2302PortStartupMode.setStatus("current")


class _Enc2302PortStartupDelay_Type(Integer32):
    """Custom type enc2302PortStartupDelay based on Integer32"""
    defaultValue = 0


_Enc2302PortStartupDelay_Type.__name__ = "Integer32"
_Enc2302PortStartupDelay_Object = MibTableColumn
enc2302PortStartupDelay = _Enc2302PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 3, 1, 2, 1, 6),
    _Enc2302PortStartupDelay_Type()
)
enc2302PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2302PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    enc2302PortStartupDelay.setUnits("seconds")


class _Enc2302PortRepowerTime_Type(Integer32):
    """Custom type enc2302PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Enc2302PortRepowerTime_Type.__name__ = "Integer32"
_Enc2302PortRepowerTime_Object = MibTableColumn
enc2302PortRepowerTime = _Enc2302PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 3, 1, 2, 1, 7),
    _Enc2302PortRepowerTime_Type()
)
enc2302PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2302PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    enc2302PortRepowerTime.setUnits("seconds")
_Enc2302ExtActors_ObjectIdentity = ObjectIdentity
enc2302ExtActors = _Enc2302ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 4)
)
_Enc2302IntSensors_ObjectIdentity = ObjectIdentity
enc2302IntSensors = _Enc2302IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 5)
)
_Enc2302Inputs_ObjectIdentity = ObjectIdentity
enc2302Inputs = _Enc2302Inputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 5, 6)
)


class _Enc2302ActiveInputs_Type(Unsigned32):
    """Custom type enc2302ActiveInputs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Enc2302ActiveInputs_Type.__name__ = "Unsigned32"
_Enc2302ActiveInputs_Object = MibScalar
enc2302ActiveInputs = _Enc2302ActiveInputs_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 5, 6, 1),
    _Enc2302ActiveInputs_Type()
)
enc2302ActiveInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302ActiveInputs.setStatus("current")
_Enc2302InputTable_Object = MibTable
enc2302InputTable = _Enc2302InputTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    enc2302InputTable.setStatus("current")
_Enc2302InputEntry_Object = MibTableRow
enc2302InputEntry = _Enc2302InputEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 5, 6, 2, 1)
)
enc2302InputEntry.setIndexNames(
    (0, "GUDEADS-ENC2302-MIB", "enc2302InputIndex"),
)
if mibBuilder.loadTexts:
    enc2302InputEntry.setStatus("current")


class _Enc2302InputIndex_Type(Integer32):
    """Custom type enc2302InputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Enc2302InputIndex_Type.__name__ = "Integer32"
_Enc2302InputIndex_Object = MibTableColumn
enc2302InputIndex = _Enc2302InputIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 5, 6, 2, 1, 1),
    _Enc2302InputIndex_Type()
)
enc2302InputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302InputIndex.setStatus("current")


class _Enc2302Input_Type(Integer32):
    """Custom type enc2302Input based on Integer32"""
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


_Enc2302Input_Type.__name__ = "Integer32"
_Enc2302Input_Object = MibTableColumn
enc2302Input = _Enc2302Input_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 5, 6, 2, 1, 2),
    _Enc2302Input_Type()
)
enc2302Input.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302Input.setStatus("current")
_Enc2302ExtSensors_ObjectIdentity = ObjectIdentity
enc2302ExtSensors = _Enc2302ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 6)
)
_Enc2302SensorTable_Object = MibTable
enc2302SensorTable = _Enc2302SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 6, 1)
)
if mibBuilder.loadTexts:
    enc2302SensorTable.setStatus("current")
_Enc2302SensorEntry_Object = MibTableRow
enc2302SensorEntry = _Enc2302SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 6, 1, 1)
)
enc2302SensorEntry.setIndexNames(
    (0, "GUDEADS-ENC2302-MIB", "enc2302SensorIndex"),
)
if mibBuilder.loadTexts:
    enc2302SensorEntry.setStatus("current")


class _Enc2302SensorIndex_Type(Integer32):
    """Custom type enc2302SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Enc2302SensorIndex_Type.__name__ = "Integer32"
_Enc2302SensorIndex_Object = MibTableColumn
enc2302SensorIndex = _Enc2302SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 6, 1, 1, 1),
    _Enc2302SensorIndex_Type()
)
enc2302SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302SensorIndex.setStatus("current")
_Enc2302TempSensor_Type = Integer32
_Enc2302TempSensor_Object = MibTableColumn
enc2302TempSensor = _Enc2302TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 6, 1, 1, 2),
    _Enc2302TempSensor_Type()
)
enc2302TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    enc2302TempSensor.setUnits("0.1 degree Celsius")
_Enc2302HygroSensor_Type = Integer32
_Enc2302HygroSensor_Object = MibTableColumn
enc2302HygroSensor = _Enc2302HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 6, 1, 1, 3),
    _Enc2302HygroSensor_Type()
)
enc2302HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    enc2302HygroSensor.setUnits("0.1 percent humidity")


class _Enc2302InputSensor_Type(Integer32):
    """Custom type enc2302InputSensor based on Integer32"""
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


_Enc2302InputSensor_Type.__name__ = "Integer32"
_Enc2302InputSensor_Object = MibTableColumn
enc2302InputSensor = _Enc2302InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 6, 1, 1, 4),
    _Enc2302InputSensor_Type()
)
enc2302InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302InputSensor.setStatus("current")
_Enc2302AirPressure_Type = Integer32
_Enc2302AirPressure_Object = MibTableColumn
enc2302AirPressure = _Enc2302AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 6, 1, 1, 5),
    _Enc2302AirPressure_Type()
)
enc2302AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    enc2302AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Enc2302DewPoint_Type = Integer32
_Enc2302DewPoint_Object = MibTableColumn
enc2302DewPoint = _Enc2302DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 6, 1, 1, 6),
    _Enc2302DewPoint_Type()
)
enc2302DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    enc2302DewPoint.setUnits("0.1 degree Celsius")
_Enc2302DewPointDiff_Type = Integer32
_Enc2302DewPointDiff_Object = MibTableColumn
enc2302DewPointDiff = _Enc2302DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 70, 1, 6, 1, 1, 7),
    _Enc2302DewPointDiff_Type()
)
enc2302DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2302DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    enc2302DewPointDiff.setUnits("0.1 degree Celsius")
_Enc2302Conf_ObjectIdentity = ObjectIdentity
enc2302Conf = _Enc2302Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 2)
)
_Enc2302Groups_ObjectIdentity = ObjectIdentity
enc2302Groups = _Enc2302Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 2, 1)
)
_Enc2302Compls_ObjectIdentity = ObjectIdentity
enc2302Compls = _Enc2302Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 70, 3)
)

# Managed Objects groups

enc2302BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 70, 2, 1, 1)
)
enc2302BasicGroup.setObjects(
      *(("GUDEADS-ENC2302-MIB", "enc2302TrapCtrl"),
        ("GUDEADS-ENC2302-MIB", "enc2302TrapIPIndex"),
        ("GUDEADS-ENC2302-MIB", "enc2302TrapAddr"),
        ("GUDEADS-ENC2302-MIB", "enc2302portNumber"),
        ("GUDEADS-ENC2302-MIB", "enc2302PortIndex"),
        ("GUDEADS-ENC2302-MIB", "enc2302PortName"),
        ("GUDEADS-ENC2302-MIB", "enc2302PortState"),
        ("GUDEADS-ENC2302-MIB", "enc2302PortSwitchCount"),
        ("GUDEADS-ENC2302-MIB", "enc2302PortStartupMode"),
        ("GUDEADS-ENC2302-MIB", "enc2302PortStartupDelay"),
        ("GUDEADS-ENC2302-MIB", "enc2302PortRepowerTime"),
        ("GUDEADS-ENC2302-MIB", "enc2302ActiveInputs"),
        ("GUDEADS-ENC2302-MIB", "enc2302InputIndex"),
        ("GUDEADS-ENC2302-MIB", "enc2302Input"),
        ("GUDEADS-ENC2302-MIB", "enc2302SensorIndex"),
        ("GUDEADS-ENC2302-MIB", "enc2302TempSensor"),
        ("GUDEADS-ENC2302-MIB", "enc2302HygroSensor"),
        ("GUDEADS-ENC2302-MIB", "enc2302InputSensor"),
        ("GUDEADS-ENC2302-MIB", "enc2302AirPressure"),
        ("GUDEADS-ENC2302-MIB", "enc2302DewPoint"),
        ("GUDEADS-ENC2302-MIB", "enc2302DewPointDiff"))
)
if mibBuilder.loadTexts:
    enc2302BasicGroup.setStatus("current")


# Notification objects

enc2302SwitchEvtPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 70, 3, 1)
)
enc2302SwitchEvtPort.setObjects(
      *(("GUDEADS-ENC2302-MIB", "enc2302PortIndex"),
        ("GUDEADS-ENC2302-MIB", "enc2302PortName"),
        ("GUDEADS-ENC2302-MIB", "enc2302PortState"),
        ("GUDEADS-ENC2302-MIB", "enc2302PortSwitchCount"))
)
if mibBuilder.loadTexts:
    enc2302SwitchEvtPort.setStatus(
        "current"
    )

enc2302InputEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 70, 3, 2)
)
enc2302InputEvt.setObjects(
      *(("GUDEADS-ENC2302-MIB", "enc2302InputIndex"),
        ("GUDEADS-ENC2302-MIB", "enc2302Input"))
)
if mibBuilder.loadTexts:
    enc2302InputEvt.setStatus(
        "current"
    )

enc2302TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 70, 3, 3)
)
enc2302TempEvtSen.setObjects(
      *(("GUDEADS-ENC2302-MIB", "enc2302SensorIndex"),
        ("GUDEADS-ENC2302-MIB", "enc2302TempSensor"))
)
if mibBuilder.loadTexts:
    enc2302TempEvtSen.setStatus(
        "current"
    )

enc2302HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 70, 3, 4)
)
enc2302HygroEvtSen.setObjects(
      *(("GUDEADS-ENC2302-MIB", "enc2302SensorIndex"),
        ("GUDEADS-ENC2302-MIB", "enc2302HygroSensor"))
)
if mibBuilder.loadTexts:
    enc2302HygroEvtSen.setStatus(
        "current"
    )

enc2302InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 70, 3, 5)
)
enc2302InputEvtSen.setObjects(
      *(("GUDEADS-ENC2302-MIB", "enc2302SensorIndex"),
        ("GUDEADS-ENC2302-MIB", "enc2302InputSensor"))
)
if mibBuilder.loadTexts:
    enc2302InputEvtSen.setStatus(
        "current"
    )

enc2302AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 70, 3, 6)
)
enc2302AirPressureEvtSen.setObjects(
      *(("GUDEADS-ENC2302-MIB", "enc2302SensorIndex"),
        ("GUDEADS-ENC2302-MIB", "enc2302AirPressure"))
)
if mibBuilder.loadTexts:
    enc2302AirPressureEvtSen.setStatus(
        "current"
    )

enc2302DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 70, 3, 7)
)
enc2302DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-ENC2302-MIB", "enc2302SensorIndex"),
        ("GUDEADS-ENC2302-MIB", "enc2302DewPointDiff"))
)
if mibBuilder.loadTexts:
    enc2302DewPtDiffEvtSen.setStatus(
        "current"
    )


# Notifications groups

enc2302NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 70, 2, 1, 2)
)
enc2302NotificationGroup.setObjects(
      *(("GUDEADS-ENC2302-MIB", "enc2302SwitchEvtPort"),
        ("GUDEADS-ENC2302-MIB", "enc2302InputEvt"),
        ("GUDEADS-ENC2302-MIB", "enc2302TempEvtSen"),
        ("GUDEADS-ENC2302-MIB", "enc2302HygroEvtSen"),
        ("GUDEADS-ENC2302-MIB", "enc2302InputEvtSen"),
        ("GUDEADS-ENC2302-MIB", "enc2302AirPressureEvtSen"),
        ("GUDEADS-ENC2302-MIB", "enc2302DewPtDiffEvtSen"))
)
if mibBuilder.loadTexts:
    enc2302NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-ENC2302-MIB",
    **{"gudeads": gudeads,
       "gadsENC2302": gadsENC2302,
       "enc2302Objects": enc2302Objects,
       "enc2302CommonConfig": enc2302CommonConfig,
       "enc2302SNMPaccess": enc2302SNMPaccess,
       "enc2302TrapCtrl": enc2302TrapCtrl,
       "enc2302TrapIPTable": enc2302TrapIPTable,
       "enc2302TrapIPEntry": enc2302TrapIPEntry,
       "enc2302TrapIPIndex": enc2302TrapIPIndex,
       "enc2302TrapAddr": enc2302TrapAddr,
       "enc2302DeviceConfig": enc2302DeviceConfig,
       "enc2302IntActors": enc2302IntActors,
       "enc2302relayports": enc2302relayports,
       "enc2302portNumber": enc2302portNumber,
       "enc2302portTable": enc2302portTable,
       "enc2302portEntry": enc2302portEntry,
       "enc2302PortIndex": enc2302PortIndex,
       "enc2302PortName": enc2302PortName,
       "enc2302PortState": enc2302PortState,
       "enc2302PortSwitchCount": enc2302PortSwitchCount,
       "enc2302PortStartupMode": enc2302PortStartupMode,
       "enc2302PortStartupDelay": enc2302PortStartupDelay,
       "enc2302PortRepowerTime": enc2302PortRepowerTime,
       "enc2302ExtActors": enc2302ExtActors,
       "enc2302IntSensors": enc2302IntSensors,
       "enc2302Inputs": enc2302Inputs,
       "enc2302ActiveInputs": enc2302ActiveInputs,
       "enc2302InputTable": enc2302InputTable,
       "enc2302InputEntry": enc2302InputEntry,
       "enc2302InputIndex": enc2302InputIndex,
       "enc2302Input": enc2302Input,
       "enc2302ExtSensors": enc2302ExtSensors,
       "enc2302SensorTable": enc2302SensorTable,
       "enc2302SensorEntry": enc2302SensorEntry,
       "enc2302SensorIndex": enc2302SensorIndex,
       "enc2302TempSensor": enc2302TempSensor,
       "enc2302HygroSensor": enc2302HygroSensor,
       "enc2302InputSensor": enc2302InputSensor,
       "enc2302AirPressure": enc2302AirPressure,
       "enc2302DewPoint": enc2302DewPoint,
       "enc2302DewPointDiff": enc2302DewPointDiff,
       "enc2302Conf": enc2302Conf,
       "enc2302Groups": enc2302Groups,
       "enc2302BasicGroup": enc2302BasicGroup,
       "enc2302NotificationGroup": enc2302NotificationGroup,
       "enc2302Compls": enc2302Compls,
       "events": events,
       "enc2302SwitchEvtPort": enc2302SwitchEvtPort,
       "enc2302InputEvt": enc2302InputEvt,
       "enc2302TempEvtSen": enc2302TempEvtSen,
       "enc2302HygroEvtSen": enc2302HygroEvtSen,
       "enc2302InputEvtSen": enc2302InputEvtSen,
       "enc2302AirPressureEvtSen": enc2302AirPressureEvtSen,
       "enc2302DewPtDiffEvtSen": enc2302DewPtDiffEvtSen}
)
