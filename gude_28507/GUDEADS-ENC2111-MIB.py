# SNMP MIB module (GUDEADS-ENC2111-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-ENC2111-MIB.mib
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

_GadsENC2111_ObjectIdentity = ObjectIdentity
gadsENC2111 = _GadsENC2111_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60)
)
_Enc2111Objects_ObjectIdentity = ObjectIdentity
enc2111Objects = _Enc2111Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1)
)
_Enc2111CommonConfig_ObjectIdentity = ObjectIdentity
enc2111CommonConfig = _Enc2111CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 1)
)
_Enc2111SNMPaccess_ObjectIdentity = ObjectIdentity
enc2111SNMPaccess = _Enc2111SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 1, 1)
)


class _Enc2111TrapCtrl_Type(Integer32):
    """Custom type enc2111TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Enc2111TrapCtrl_Type.__name__ = "Integer32"
_Enc2111TrapCtrl_Object = MibScalar
enc2111TrapCtrl = _Enc2111TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 1, 1, 1),
    _Enc2111TrapCtrl_Type()
)
enc2111TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2111TrapCtrl.setStatus("current")
_Enc2111TrapIPTable_Object = MibTable
enc2111TrapIPTable = _Enc2111TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    enc2111TrapIPTable.setStatus("current")
_Enc2111TrapIPEntry_Object = MibTableRow
enc2111TrapIPEntry = _Enc2111TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 1, 1, 2, 1)
)
enc2111TrapIPEntry.setIndexNames(
    (0, "GUDEADS-ENC2111-MIB", "enc2111TrapIPIndex"),
)
if mibBuilder.loadTexts:
    enc2111TrapIPEntry.setStatus("current")


class _Enc2111TrapIPIndex_Type(Integer32):
    """Custom type enc2111TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Enc2111TrapIPIndex_Type.__name__ = "Integer32"
_Enc2111TrapIPIndex_Object = MibTableColumn
enc2111TrapIPIndex = _Enc2111TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 1, 1, 2, 1, 1),
    _Enc2111TrapIPIndex_Type()
)
enc2111TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111TrapIPIndex.setStatus("current")


class _Enc2111TrapAddr_Type(OctetString):
    """Custom type enc2111TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Enc2111TrapAddr_Type.__name__ = "OctetString"
_Enc2111TrapAddr_Object = MibTableColumn
enc2111TrapAddr = _Enc2111TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 1, 1, 2, 1, 2),
    _Enc2111TrapAddr_Type()
)
enc2111TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2111TrapAddr.setStatus("current")
_Enc2111DeviceConfig_ObjectIdentity = ObjectIdentity
enc2111DeviceConfig = _Enc2111DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 2)
)
_Enc2111IntActors_ObjectIdentity = ObjectIdentity
enc2111IntActors = _Enc2111IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 3)
)
_Enc2111relayports_ObjectIdentity = ObjectIdentity
enc2111relayports = _Enc2111relayports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 3, 1)
)


class _Enc2111portNumber_Type(Integer32):
    """Custom type enc2111portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Enc2111portNumber_Type.__name__ = "Integer32"
_Enc2111portNumber_Object = MibScalar
enc2111portNumber = _Enc2111portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 3, 1, 1),
    _Enc2111portNumber_Type()
)
enc2111portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111portNumber.setStatus("current")
_Enc2111portTable_Object = MibTable
enc2111portTable = _Enc2111portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    enc2111portTable.setStatus("current")
_Enc2111portEntry_Object = MibTableRow
enc2111portEntry = _Enc2111portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 3, 1, 2, 1)
)
enc2111portEntry.setIndexNames(
    (0, "GUDEADS-ENC2111-MIB", "enc2111PortIndex"),
)
if mibBuilder.loadTexts:
    enc2111portEntry.setStatus("current")


class _Enc2111PortIndex_Type(Integer32):
    """Custom type enc2111PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Enc2111PortIndex_Type.__name__ = "Integer32"
_Enc2111PortIndex_Object = MibTableColumn
enc2111PortIndex = _Enc2111PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 3, 1, 2, 1, 1),
    _Enc2111PortIndex_Type()
)
enc2111PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111PortIndex.setStatus("current")


class _Enc2111PortName_Type(OctetString):
    """Custom type enc2111PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Enc2111PortName_Type.__name__ = "OctetString"
_Enc2111PortName_Object = MibTableColumn
enc2111PortName = _Enc2111PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 3, 1, 2, 1, 2),
    _Enc2111PortName_Type()
)
enc2111PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2111PortName.setStatus("current")


class _Enc2111PortState_Type(Integer32):
    """Custom type enc2111PortState based on Integer32"""
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


_Enc2111PortState_Type.__name__ = "Integer32"
_Enc2111PortState_Object = MibTableColumn
enc2111PortState = _Enc2111PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 3, 1, 2, 1, 3),
    _Enc2111PortState_Type()
)
enc2111PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2111PortState.setStatus("current")
_Enc2111PortSwitchCount_Type = Integer32
_Enc2111PortSwitchCount_Object = MibTableColumn
enc2111PortSwitchCount = _Enc2111PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 3, 1, 2, 1, 4),
    _Enc2111PortSwitchCount_Type()
)
enc2111PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111PortSwitchCount.setStatus("current")


class _Enc2111PortStartupMode_Type(Integer32):
    """Custom type enc2111PortStartupMode based on Integer32"""
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


_Enc2111PortStartupMode_Type.__name__ = "Integer32"
_Enc2111PortStartupMode_Object = MibTableColumn
enc2111PortStartupMode = _Enc2111PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 3, 1, 2, 1, 5),
    _Enc2111PortStartupMode_Type()
)
enc2111PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2111PortStartupMode.setStatus("current")


class _Enc2111PortStartupDelay_Type(Integer32):
    """Custom type enc2111PortStartupDelay based on Integer32"""
    defaultValue = 0


_Enc2111PortStartupDelay_Type.__name__ = "Integer32"
_Enc2111PortStartupDelay_Object = MibTableColumn
enc2111PortStartupDelay = _Enc2111PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 3, 1, 2, 1, 6),
    _Enc2111PortStartupDelay_Type()
)
enc2111PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2111PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    enc2111PortStartupDelay.setUnits("seconds")


class _Enc2111PortRepowerTime_Type(Integer32):
    """Custom type enc2111PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Enc2111PortRepowerTime_Type.__name__ = "Integer32"
_Enc2111PortRepowerTime_Object = MibTableColumn
enc2111PortRepowerTime = _Enc2111PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 3, 1, 2, 1, 7),
    _Enc2111PortRepowerTime_Type()
)
enc2111PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enc2111PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    enc2111PortRepowerTime.setUnits("seconds")
_Enc2111ExtActors_ObjectIdentity = ObjectIdentity
enc2111ExtActors = _Enc2111ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 4)
)
_Enc2111IntSensors_ObjectIdentity = ObjectIdentity
enc2111IntSensors = _Enc2111IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 5)
)
_Enc2111Inputs_ObjectIdentity = ObjectIdentity
enc2111Inputs = _Enc2111Inputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 5, 6)
)


class _Enc2111ActiveInputs_Type(Unsigned32):
    """Custom type enc2111ActiveInputs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Enc2111ActiveInputs_Type.__name__ = "Unsigned32"
_Enc2111ActiveInputs_Object = MibScalar
enc2111ActiveInputs = _Enc2111ActiveInputs_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 5, 6, 1),
    _Enc2111ActiveInputs_Type()
)
enc2111ActiveInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111ActiveInputs.setStatus("current")
_Enc2111InputTable_Object = MibTable
enc2111InputTable = _Enc2111InputTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 5, 6, 2)
)
if mibBuilder.loadTexts:
    enc2111InputTable.setStatus("current")
_Enc2111InputEntry_Object = MibTableRow
enc2111InputEntry = _Enc2111InputEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 5, 6, 2, 1)
)
enc2111InputEntry.setIndexNames(
    (0, "GUDEADS-ENC2111-MIB", "enc2111InputIndex"),
)
if mibBuilder.loadTexts:
    enc2111InputEntry.setStatus("current")


class _Enc2111InputIndex_Type(Integer32):
    """Custom type enc2111InputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Enc2111InputIndex_Type.__name__ = "Integer32"
_Enc2111InputIndex_Object = MibTableColumn
enc2111InputIndex = _Enc2111InputIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 5, 6, 2, 1, 1),
    _Enc2111InputIndex_Type()
)
enc2111InputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111InputIndex.setStatus("current")


class _Enc2111Input_Type(Integer32):
    """Custom type enc2111Input based on Integer32"""
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


_Enc2111Input_Type.__name__ = "Integer32"
_Enc2111Input_Object = MibTableColumn
enc2111Input = _Enc2111Input_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 5, 6, 2, 1, 2),
    _Enc2111Input_Type()
)
enc2111Input.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111Input.setStatus("current")
_Enc2111VoltageInfo_ObjectIdentity = ObjectIdentity
enc2111VoltageInfo = _Enc2111VoltageInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 5, 7)
)


class _Enc2111State12V_Type(Integer32):
    """Custom type enc2111State12V based on Integer32"""
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


_Enc2111State12V_Type.__name__ = "Integer32"
_Enc2111State12V_Object = MibScalar
enc2111State12V = _Enc2111State12V_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 5, 7, 1),
    _Enc2111State12V_Type()
)
enc2111State12V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111State12V.setStatus("current")


class _Enc2111State3V_Type(Integer32):
    """Custom type enc2111State3V based on Integer32"""
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


_Enc2111State3V_Type.__name__ = "Integer32"
_Enc2111State3V_Object = MibScalar
enc2111State3V = _Enc2111State3V_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 5, 7, 2),
    _Enc2111State3V_Type()
)
enc2111State3V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111State3V.setStatus("current")


class _Enc2111POE_Type(Integer32):
    """Custom type enc2111POE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Enc2111POE_Type.__name__ = "Integer32"
_Enc2111POE_Object = MibScalar
enc2111POE = _Enc2111POE_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 5, 10),
    _Enc2111POE_Type()
)
enc2111POE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111POE.setStatus("current")
if mibBuilder.loadTexts:
    enc2111POE.setUnits("0 = no POE, 1 = POE available")
_Enc2111ExtSensors_ObjectIdentity = ObjectIdentity
enc2111ExtSensors = _Enc2111ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 6)
)
_Enc2111SensorTable_Object = MibTable
enc2111SensorTable = _Enc2111SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 6, 1)
)
if mibBuilder.loadTexts:
    enc2111SensorTable.setStatus("current")
_Enc2111SensorEntry_Object = MibTableRow
enc2111SensorEntry = _Enc2111SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 6, 1, 1)
)
enc2111SensorEntry.setIndexNames(
    (0, "GUDEADS-ENC2111-MIB", "enc2111SensorIndex"),
)
if mibBuilder.loadTexts:
    enc2111SensorEntry.setStatus("current")


class _Enc2111SensorIndex_Type(Integer32):
    """Custom type enc2111SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Enc2111SensorIndex_Type.__name__ = "Integer32"
_Enc2111SensorIndex_Object = MibTableColumn
enc2111SensorIndex = _Enc2111SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 6, 1, 1, 1),
    _Enc2111SensorIndex_Type()
)
enc2111SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111SensorIndex.setStatus("current")
_Enc2111TempSensor_Type = Integer32
_Enc2111TempSensor_Object = MibTableColumn
enc2111TempSensor = _Enc2111TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 6, 1, 1, 2),
    _Enc2111TempSensor_Type()
)
enc2111TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    enc2111TempSensor.setUnits("0.1 degree Celsius")
_Enc2111HygroSensor_Type = Integer32
_Enc2111HygroSensor_Object = MibTableColumn
enc2111HygroSensor = _Enc2111HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 6, 1, 1, 3),
    _Enc2111HygroSensor_Type()
)
enc2111HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    enc2111HygroSensor.setUnits("0.1 percent humidity")


class _Enc2111InputSensor_Type(Integer32):
    """Custom type enc2111InputSensor based on Integer32"""
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


_Enc2111InputSensor_Type.__name__ = "Integer32"
_Enc2111InputSensor_Object = MibTableColumn
enc2111InputSensor = _Enc2111InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 6, 1, 1, 4),
    _Enc2111InputSensor_Type()
)
enc2111InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111InputSensor.setStatus("current")
_Enc2111AirPressure_Type = Integer32
_Enc2111AirPressure_Object = MibTableColumn
enc2111AirPressure = _Enc2111AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 6, 1, 1, 5),
    _Enc2111AirPressure_Type()
)
enc2111AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    enc2111AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Enc2111DewPoint_Type = Integer32
_Enc2111DewPoint_Object = MibTableColumn
enc2111DewPoint = _Enc2111DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 6, 1, 1, 6),
    _Enc2111DewPoint_Type()
)
enc2111DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    enc2111DewPoint.setUnits("0.1 degree Celsius")
_Enc2111DewPointDiff_Type = Integer32
_Enc2111DewPointDiff_Object = MibTableColumn
enc2111DewPointDiff = _Enc2111DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 60, 1, 6, 1, 1, 7),
    _Enc2111DewPointDiff_Type()
)
enc2111DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enc2111DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    enc2111DewPointDiff.setUnits("0.1 degree Celsius")
_Enc2111Conf_ObjectIdentity = ObjectIdentity
enc2111Conf = _Enc2111Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 2)
)
_Enc2111Groups_ObjectIdentity = ObjectIdentity
enc2111Groups = _Enc2111Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 2, 1)
)
_Enc2111Compls_ObjectIdentity = ObjectIdentity
enc2111Compls = _Enc2111Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 60, 3)
)

# Managed Objects groups

enc2111BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 60, 2, 1, 1)
)
enc2111BasicGroup.setObjects(
      *(("GUDEADS-ENC2111-MIB", "enc2111TrapCtrl"),
        ("GUDEADS-ENC2111-MIB", "enc2111TrapIPIndex"),
        ("GUDEADS-ENC2111-MIB", "enc2111TrapAddr"),
        ("GUDEADS-ENC2111-MIB", "enc2111portNumber"),
        ("GUDEADS-ENC2111-MIB", "enc2111PortIndex"),
        ("GUDEADS-ENC2111-MIB", "enc2111PortName"),
        ("GUDEADS-ENC2111-MIB", "enc2111PortState"),
        ("GUDEADS-ENC2111-MIB", "enc2111PortSwitchCount"),
        ("GUDEADS-ENC2111-MIB", "enc2111PortStartupMode"),
        ("GUDEADS-ENC2111-MIB", "enc2111PortStartupDelay"),
        ("GUDEADS-ENC2111-MIB", "enc2111PortRepowerTime"),
        ("GUDEADS-ENC2111-MIB", "enc2111ActiveInputs"),
        ("GUDEADS-ENC2111-MIB", "enc2111InputIndex"),
        ("GUDEADS-ENC2111-MIB", "enc2111Input"),
        ("GUDEADS-ENC2111-MIB", "enc2111State12V"),
        ("GUDEADS-ENC2111-MIB", "enc2111State3V"),
        ("GUDEADS-ENC2111-MIB", "enc2111POE"),
        ("GUDEADS-ENC2111-MIB", "enc2111SensorIndex"),
        ("GUDEADS-ENC2111-MIB", "enc2111TempSensor"),
        ("GUDEADS-ENC2111-MIB", "enc2111HygroSensor"),
        ("GUDEADS-ENC2111-MIB", "enc2111InputSensor"),
        ("GUDEADS-ENC2111-MIB", "enc2111AirPressure"),
        ("GUDEADS-ENC2111-MIB", "enc2111DewPoint"),
        ("GUDEADS-ENC2111-MIB", "enc2111DewPointDiff"))
)
if mibBuilder.loadTexts:
    enc2111BasicGroup.setStatus("current")


# Notification objects

enc2111SwitchEvtPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 60, 3, 1)
)
enc2111SwitchEvtPort.setObjects(
      *(("GUDEADS-ENC2111-MIB", "enc2111PortIndex"),
        ("GUDEADS-ENC2111-MIB", "enc2111PortName"),
        ("GUDEADS-ENC2111-MIB", "enc2111PortState"),
        ("GUDEADS-ENC2111-MIB", "enc2111PortSwitchCount"))
)
if mibBuilder.loadTexts:
    enc2111SwitchEvtPort.setStatus(
        "current"
    )

enc2111InputEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 60, 3, 2)
)
enc2111InputEvt.setObjects(
      *(("GUDEADS-ENC2111-MIB", "enc2111InputIndex"),
        ("GUDEADS-ENC2111-MIB", "enc2111Input"))
)
if mibBuilder.loadTexts:
    enc2111InputEvt.setStatus(
        "current"
    )

enc2111TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 60, 3, 3)
)
enc2111TempEvtSen.setObjects(
      *(("GUDEADS-ENC2111-MIB", "enc2111SensorIndex"),
        ("GUDEADS-ENC2111-MIB", "enc2111TempSensor"))
)
if mibBuilder.loadTexts:
    enc2111TempEvtSen.setStatus(
        "current"
    )

enc2111HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 60, 3, 4)
)
enc2111HygroEvtSen.setObjects(
      *(("GUDEADS-ENC2111-MIB", "enc2111SensorIndex"),
        ("GUDEADS-ENC2111-MIB", "enc2111HygroSensor"))
)
if mibBuilder.loadTexts:
    enc2111HygroEvtSen.setStatus(
        "current"
    )

enc2111InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 60, 3, 5)
)
enc2111InputEvtSen.setObjects(
      *(("GUDEADS-ENC2111-MIB", "enc2111SensorIndex"),
        ("GUDEADS-ENC2111-MIB", "enc2111InputSensor"))
)
if mibBuilder.loadTexts:
    enc2111InputEvtSen.setStatus(
        "current"
    )

enc2111AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 60, 3, 6)
)
enc2111AirPressureEvtSen.setObjects(
      *(("GUDEADS-ENC2111-MIB", "enc2111SensorIndex"),
        ("GUDEADS-ENC2111-MIB", "enc2111AirPressure"))
)
if mibBuilder.loadTexts:
    enc2111AirPressureEvtSen.setStatus(
        "current"
    )

enc2111DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 60, 3, 7)
)
enc2111DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-ENC2111-MIB", "enc2111SensorIndex"),
        ("GUDEADS-ENC2111-MIB", "enc2111DewPointDiff"))
)
if mibBuilder.loadTexts:
    enc2111DewPtDiffEvtSen.setStatus(
        "current"
    )

enc2111POEEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 60, 3, 8)
)
enc2111POEEvt.setObjects(
    ("GUDEADS-ENC2111-MIB", "enc2111POE")
)
if mibBuilder.loadTexts:
    enc2111POEEvt.setStatus(
        "current"
    )


# Notifications groups

enc2111NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 60, 2, 1, 2)
)
enc2111NotificationGroup.setObjects(
      *(("GUDEADS-ENC2111-MIB", "enc2111SwitchEvtPort"),
        ("GUDEADS-ENC2111-MIB", "enc2111InputEvt"),
        ("GUDEADS-ENC2111-MIB", "enc2111TempEvtSen"),
        ("GUDEADS-ENC2111-MIB", "enc2111HygroEvtSen"),
        ("GUDEADS-ENC2111-MIB", "enc2111InputEvtSen"),
        ("GUDEADS-ENC2111-MIB", "enc2111AirPressureEvtSen"),
        ("GUDEADS-ENC2111-MIB", "enc2111DewPtDiffEvtSen"),
        ("GUDEADS-ENC2111-MIB", "enc2111POEEvt"))
)
if mibBuilder.loadTexts:
    enc2111NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-ENC2111-MIB",
    **{"gudeads": gudeads,
       "gadsENC2111": gadsENC2111,
       "enc2111Objects": enc2111Objects,
       "enc2111CommonConfig": enc2111CommonConfig,
       "enc2111SNMPaccess": enc2111SNMPaccess,
       "enc2111TrapCtrl": enc2111TrapCtrl,
       "enc2111TrapIPTable": enc2111TrapIPTable,
       "enc2111TrapIPEntry": enc2111TrapIPEntry,
       "enc2111TrapIPIndex": enc2111TrapIPIndex,
       "enc2111TrapAddr": enc2111TrapAddr,
       "enc2111DeviceConfig": enc2111DeviceConfig,
       "enc2111IntActors": enc2111IntActors,
       "enc2111relayports": enc2111relayports,
       "enc2111portNumber": enc2111portNumber,
       "enc2111portTable": enc2111portTable,
       "enc2111portEntry": enc2111portEntry,
       "enc2111PortIndex": enc2111PortIndex,
       "enc2111PortName": enc2111PortName,
       "enc2111PortState": enc2111PortState,
       "enc2111PortSwitchCount": enc2111PortSwitchCount,
       "enc2111PortStartupMode": enc2111PortStartupMode,
       "enc2111PortStartupDelay": enc2111PortStartupDelay,
       "enc2111PortRepowerTime": enc2111PortRepowerTime,
       "enc2111ExtActors": enc2111ExtActors,
       "enc2111IntSensors": enc2111IntSensors,
       "enc2111Inputs": enc2111Inputs,
       "enc2111ActiveInputs": enc2111ActiveInputs,
       "enc2111InputTable": enc2111InputTable,
       "enc2111InputEntry": enc2111InputEntry,
       "enc2111InputIndex": enc2111InputIndex,
       "enc2111Input": enc2111Input,
       "enc2111VoltageInfo": enc2111VoltageInfo,
       "enc2111State12V": enc2111State12V,
       "enc2111State3V": enc2111State3V,
       "enc2111POE": enc2111POE,
       "enc2111ExtSensors": enc2111ExtSensors,
       "enc2111SensorTable": enc2111SensorTable,
       "enc2111SensorEntry": enc2111SensorEntry,
       "enc2111SensorIndex": enc2111SensorIndex,
       "enc2111TempSensor": enc2111TempSensor,
       "enc2111HygroSensor": enc2111HygroSensor,
       "enc2111InputSensor": enc2111InputSensor,
       "enc2111AirPressure": enc2111AirPressure,
       "enc2111DewPoint": enc2111DewPoint,
       "enc2111DewPointDiff": enc2111DewPointDiff,
       "enc2111Conf": enc2111Conf,
       "enc2111Groups": enc2111Groups,
       "enc2111BasicGroup": enc2111BasicGroup,
       "enc2111NotificationGroup": enc2111NotificationGroup,
       "enc2111Compls": enc2111Compls,
       "events": events,
       "enc2111SwitchEvtPort": enc2111SwitchEvtPort,
       "enc2111InputEvt": enc2111InputEvt,
       "enc2111TempEvtSen": enc2111TempEvtSen,
       "enc2111HygroEvtSen": enc2111HygroEvtSen,
       "enc2111InputEvtSen": enc2111InputEvtSen,
       "enc2111AirPressureEvtSen": enc2111AirPressureEvtSen,
       "enc2111DewPtDiffEvtSen": enc2111DewPtDiffEvtSen,
       "enc2111POEEvt": enc2111POEEvt}
)
