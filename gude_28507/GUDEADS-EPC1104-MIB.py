# SNMP MIB module (GUDEADS-EPC1104-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-EPC1104-MIB.mib
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

_GadsEPC1104_ObjectIdentity = ObjectIdentity
gadsEPC1104 = _GadsEPC1104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68)
)
_Epc1104Objects_ObjectIdentity = ObjectIdentity
epc1104Objects = _Epc1104Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1)
)
_Epc1104CommonConfig_ObjectIdentity = ObjectIdentity
epc1104CommonConfig = _Epc1104CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 1)
)
_Epc1104SNMPaccess_ObjectIdentity = ObjectIdentity
epc1104SNMPaccess = _Epc1104SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 1, 1)
)


class _Epc1104TrapCtrl_Type(Integer32):
    """Custom type epc1104TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Epc1104TrapCtrl_Type.__name__ = "Integer32"
_Epc1104TrapCtrl_Object = MibScalar
epc1104TrapCtrl = _Epc1104TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 1, 1, 1),
    _Epc1104TrapCtrl_Type()
)
epc1104TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1104TrapCtrl.setStatus("current")
_Epc1104TrapIPTable_Object = MibTable
epc1104TrapIPTable = _Epc1104TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    epc1104TrapIPTable.setStatus("current")
_Epc1104TrapIPEntry_Object = MibTableRow
epc1104TrapIPEntry = _Epc1104TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 1, 1, 2, 1)
)
epc1104TrapIPEntry.setIndexNames(
    (0, "GUDEADS-EPC1104-MIB", "epc1104TrapIPIndex"),
)
if mibBuilder.loadTexts:
    epc1104TrapIPEntry.setStatus("current")


class _Epc1104TrapIPIndex_Type(Integer32):
    """Custom type epc1104TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc1104TrapIPIndex_Type.__name__ = "Integer32"
_Epc1104TrapIPIndex_Object = MibTableColumn
epc1104TrapIPIndex = _Epc1104TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 1, 1, 2, 1, 1),
    _Epc1104TrapIPIndex_Type()
)
epc1104TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1104TrapIPIndex.setStatus("current")


class _Epc1104TrapAddr_Type(OctetString):
    """Custom type epc1104TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Epc1104TrapAddr_Type.__name__ = "OctetString"
_Epc1104TrapAddr_Object = MibTableColumn
epc1104TrapAddr = _Epc1104TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 1, 1, 2, 1, 2),
    _Epc1104TrapAddr_Type()
)
epc1104TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1104TrapAddr.setStatus("current")
_Epc1104DeviceConfig_ObjectIdentity = ObjectIdentity
epc1104DeviceConfig = _Epc1104DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 2)
)
_Epc1104IntActors_ObjectIdentity = ObjectIdentity
epc1104IntActors = _Epc1104IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 3)
)
_Epc1104relayports_ObjectIdentity = ObjectIdentity
epc1104relayports = _Epc1104relayports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 3, 1)
)


class _Epc1104portNumber_Type(Integer32):
    """Custom type epc1104portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1104portNumber_Type.__name__ = "Integer32"
_Epc1104portNumber_Object = MibScalar
epc1104portNumber = _Epc1104portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 3, 1, 1),
    _Epc1104portNumber_Type()
)
epc1104portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1104portNumber.setStatus("current")
_Epc1104portTable_Object = MibTable
epc1104portTable = _Epc1104portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    epc1104portTable.setStatus("current")
_Epc1104portEntry_Object = MibTableRow
epc1104portEntry = _Epc1104portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 3, 1, 2, 1)
)
epc1104portEntry.setIndexNames(
    (0, "GUDEADS-EPC1104-MIB", "epc1104PortIndex"),
)
if mibBuilder.loadTexts:
    epc1104portEntry.setStatus("current")


class _Epc1104PortIndex_Type(Integer32):
    """Custom type epc1104PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1104PortIndex_Type.__name__ = "Integer32"
_Epc1104PortIndex_Object = MibTableColumn
epc1104PortIndex = _Epc1104PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 3, 1, 2, 1, 1),
    _Epc1104PortIndex_Type()
)
epc1104PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1104PortIndex.setStatus("current")


class _Epc1104PortName_Type(OctetString):
    """Custom type epc1104PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Epc1104PortName_Type.__name__ = "OctetString"
_Epc1104PortName_Object = MibTableColumn
epc1104PortName = _Epc1104PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 3, 1, 2, 1, 2),
    _Epc1104PortName_Type()
)
epc1104PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1104PortName.setStatus("current")


class _Epc1104PortState_Type(Integer32):
    """Custom type epc1104PortState based on Integer32"""
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


_Epc1104PortState_Type.__name__ = "Integer32"
_Epc1104PortState_Object = MibTableColumn
epc1104PortState = _Epc1104PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 3, 1, 2, 1, 3),
    _Epc1104PortState_Type()
)
epc1104PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1104PortState.setStatus("current")
_Epc1104PortSwitchCount_Type = Integer32
_Epc1104PortSwitchCount_Object = MibTableColumn
epc1104PortSwitchCount = _Epc1104PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 3, 1, 2, 1, 4),
    _Epc1104PortSwitchCount_Type()
)
epc1104PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1104PortSwitchCount.setStatus("current")


class _Epc1104PortStartupMode_Type(Integer32):
    """Custom type epc1104PortStartupMode based on Integer32"""
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


_Epc1104PortStartupMode_Type.__name__ = "Integer32"
_Epc1104PortStartupMode_Object = MibTableColumn
epc1104PortStartupMode = _Epc1104PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 3, 1, 2, 1, 5),
    _Epc1104PortStartupMode_Type()
)
epc1104PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1104PortStartupMode.setStatus("current")


class _Epc1104PortStartupDelay_Type(Integer32):
    """Custom type epc1104PortStartupDelay based on Integer32"""
    defaultValue = 0


_Epc1104PortStartupDelay_Type.__name__ = "Integer32"
_Epc1104PortStartupDelay_Object = MibTableColumn
epc1104PortStartupDelay = _Epc1104PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 3, 1, 2, 1, 6),
    _Epc1104PortStartupDelay_Type()
)
epc1104PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1104PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    epc1104PortStartupDelay.setUnits("seconds")


class _Epc1104PortRepowerTime_Type(Integer32):
    """Custom type epc1104PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Epc1104PortRepowerTime_Type.__name__ = "Integer32"
_Epc1104PortRepowerTime_Object = MibTableColumn
epc1104PortRepowerTime = _Epc1104PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 3, 1, 2, 1, 7),
    _Epc1104PortRepowerTime_Type()
)
epc1104PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1104PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    epc1104PortRepowerTime.setUnits("seconds")
_Epc1104ExtActors_ObjectIdentity = ObjectIdentity
epc1104ExtActors = _Epc1104ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 4)
)
_Epc1104IntSensors_ObjectIdentity = ObjectIdentity
epc1104IntSensors = _Epc1104IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 5)
)
_Epc1104ExtSensors_ObjectIdentity = ObjectIdentity
epc1104ExtSensors = _Epc1104ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 6)
)
_Epc1104SensorTable_Object = MibTable
epc1104SensorTable = _Epc1104SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 6, 1)
)
if mibBuilder.loadTexts:
    epc1104SensorTable.setStatus("current")
_Epc1104SensorEntry_Object = MibTableRow
epc1104SensorEntry = _Epc1104SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 6, 1, 1)
)
epc1104SensorEntry.setIndexNames(
    (0, "GUDEADS-EPC1104-MIB", "epc1104SensorIndex"),
)
if mibBuilder.loadTexts:
    epc1104SensorEntry.setStatus("current")


class _Epc1104SensorIndex_Type(Integer32):
    """Custom type epc1104SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1104SensorIndex_Type.__name__ = "Integer32"
_Epc1104SensorIndex_Object = MibTableColumn
epc1104SensorIndex = _Epc1104SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 6, 1, 1, 1),
    _Epc1104SensorIndex_Type()
)
epc1104SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1104SensorIndex.setStatus("current")
_Epc1104TempSensor_Type = Integer32
_Epc1104TempSensor_Object = MibTableColumn
epc1104TempSensor = _Epc1104TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 6, 1, 1, 2),
    _Epc1104TempSensor_Type()
)
epc1104TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1104TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc1104TempSensor.setUnits("0.1 degree Celsius")
_Epc1104HygroSensor_Type = Integer32
_Epc1104HygroSensor_Object = MibTableColumn
epc1104HygroSensor = _Epc1104HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 6, 1, 1, 3),
    _Epc1104HygroSensor_Type()
)
epc1104HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1104HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc1104HygroSensor.setUnits("0.1 percent humidity")


class _Epc1104InputSensor_Type(Integer32):
    """Custom type epc1104InputSensor based on Integer32"""
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


_Epc1104InputSensor_Type.__name__ = "Integer32"
_Epc1104InputSensor_Object = MibTableColumn
epc1104InputSensor = _Epc1104InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 6, 1, 1, 4),
    _Epc1104InputSensor_Type()
)
epc1104InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1104InputSensor.setStatus("current")
_Epc1104AirPressure_Type = Integer32
_Epc1104AirPressure_Object = MibTableColumn
epc1104AirPressure = _Epc1104AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 6, 1, 1, 5),
    _Epc1104AirPressure_Type()
)
epc1104AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1104AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    epc1104AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Epc1104DewPoint_Type = Integer32
_Epc1104DewPoint_Object = MibTableColumn
epc1104DewPoint = _Epc1104DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 6, 1, 1, 6),
    _Epc1104DewPoint_Type()
)
epc1104DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1104DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    epc1104DewPoint.setUnits("0.1 degree Celsius")
_Epc1104DewPointDiff_Type = Integer32
_Epc1104DewPointDiff_Object = MibTableColumn
epc1104DewPointDiff = _Epc1104DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 68, 1, 6, 1, 1, 7),
    _Epc1104DewPointDiff_Type()
)
epc1104DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1104DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    epc1104DewPointDiff.setUnits("0.1 degree Celsius")
_Epc1104Conf_ObjectIdentity = ObjectIdentity
epc1104Conf = _Epc1104Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 2)
)
_Epc1104Groups_ObjectIdentity = ObjectIdentity
epc1104Groups = _Epc1104Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 2, 1)
)
_Epc1104Compls_ObjectIdentity = ObjectIdentity
epc1104Compls = _Epc1104Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 68, 3)
)

# Managed Objects groups

epc1104BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 68, 2, 1, 1)
)
epc1104BasicGroup.setObjects(
      *(("GUDEADS-EPC1104-MIB", "epc1104TrapCtrl"),
        ("GUDEADS-EPC1104-MIB", "epc1104TrapIPIndex"),
        ("GUDEADS-EPC1104-MIB", "epc1104TrapAddr"),
        ("GUDEADS-EPC1104-MIB", "epc1104portNumber"),
        ("GUDEADS-EPC1104-MIB", "epc1104PortIndex"),
        ("GUDEADS-EPC1104-MIB", "epc1104PortName"),
        ("GUDEADS-EPC1104-MIB", "epc1104PortState"),
        ("GUDEADS-EPC1104-MIB", "epc1104PortSwitchCount"),
        ("GUDEADS-EPC1104-MIB", "epc1104PortStartupMode"),
        ("GUDEADS-EPC1104-MIB", "epc1104PortStartupDelay"),
        ("GUDEADS-EPC1104-MIB", "epc1104PortRepowerTime"),
        ("GUDEADS-EPC1104-MIB", "epc1104SensorIndex"),
        ("GUDEADS-EPC1104-MIB", "epc1104TempSensor"),
        ("GUDEADS-EPC1104-MIB", "epc1104HygroSensor"),
        ("GUDEADS-EPC1104-MIB", "epc1104InputSensor"),
        ("GUDEADS-EPC1104-MIB", "epc1104AirPressure"),
        ("GUDEADS-EPC1104-MIB", "epc1104DewPoint"),
        ("GUDEADS-EPC1104-MIB", "epc1104DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc1104BasicGroup.setStatus("current")


# Notification objects

epc1104SwitchEvtPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 68, 3, 1)
)
epc1104SwitchEvtPort.setObjects(
      *(("GUDEADS-EPC1104-MIB", "epc1104PortIndex"),
        ("GUDEADS-EPC1104-MIB", "epc1104PortName"),
        ("GUDEADS-EPC1104-MIB", "epc1104PortState"),
        ("GUDEADS-EPC1104-MIB", "epc1104PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc1104SwitchEvtPort.setStatus(
        "current"
    )

epc1104TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 68, 3, 2)
)
epc1104TempEvtSen.setObjects(
      *(("GUDEADS-EPC1104-MIB", "epc1104SensorIndex"),
        ("GUDEADS-EPC1104-MIB", "epc1104TempSensor"))
)
if mibBuilder.loadTexts:
    epc1104TempEvtSen.setStatus(
        "current"
    )

epc1104HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 68, 3, 3)
)
epc1104HygroEvtSen.setObjects(
      *(("GUDEADS-EPC1104-MIB", "epc1104SensorIndex"),
        ("GUDEADS-EPC1104-MIB", "epc1104HygroSensor"))
)
if mibBuilder.loadTexts:
    epc1104HygroEvtSen.setStatus(
        "current"
    )

epc1104InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 68, 3, 4)
)
epc1104InputEvtSen.setObjects(
      *(("GUDEADS-EPC1104-MIB", "epc1104SensorIndex"),
        ("GUDEADS-EPC1104-MIB", "epc1104InputSensor"))
)
if mibBuilder.loadTexts:
    epc1104InputEvtSen.setStatus(
        "current"
    )

epc1104AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 68, 3, 5)
)
epc1104AirPressureEvtSen.setObjects(
      *(("GUDEADS-EPC1104-MIB", "epc1104SensorIndex"),
        ("GUDEADS-EPC1104-MIB", "epc1104AirPressure"))
)
if mibBuilder.loadTexts:
    epc1104AirPressureEvtSen.setStatus(
        "current"
    )

epc1104DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 68, 3, 6)
)
epc1104DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-EPC1104-MIB", "epc1104SensorIndex"),
        ("GUDEADS-EPC1104-MIB", "epc1104DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc1104DewPtDiffEvtSen.setStatus(
        "current"
    )


# Notifications groups

epc1104NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 68, 2, 1, 2)
)
epc1104NotificationGroup.setObjects(
      *(("GUDEADS-EPC1104-MIB", "epc1104SwitchEvtPort"),
        ("GUDEADS-EPC1104-MIB", "epc1104TempEvtSen"),
        ("GUDEADS-EPC1104-MIB", "epc1104HygroEvtSen"),
        ("GUDEADS-EPC1104-MIB", "epc1104InputEvtSen"),
        ("GUDEADS-EPC1104-MIB", "epc1104AirPressureEvtSen"),
        ("GUDEADS-EPC1104-MIB", "epc1104DewPtDiffEvtSen"))
)
if mibBuilder.loadTexts:
    epc1104NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-EPC1104-MIB",
    **{"gudeads": gudeads,
       "gadsEPC1104": gadsEPC1104,
       "epc1104Objects": epc1104Objects,
       "epc1104CommonConfig": epc1104CommonConfig,
       "epc1104SNMPaccess": epc1104SNMPaccess,
       "epc1104TrapCtrl": epc1104TrapCtrl,
       "epc1104TrapIPTable": epc1104TrapIPTable,
       "epc1104TrapIPEntry": epc1104TrapIPEntry,
       "epc1104TrapIPIndex": epc1104TrapIPIndex,
       "epc1104TrapAddr": epc1104TrapAddr,
       "epc1104DeviceConfig": epc1104DeviceConfig,
       "epc1104IntActors": epc1104IntActors,
       "epc1104relayports": epc1104relayports,
       "epc1104portNumber": epc1104portNumber,
       "epc1104portTable": epc1104portTable,
       "epc1104portEntry": epc1104portEntry,
       "epc1104PortIndex": epc1104PortIndex,
       "epc1104PortName": epc1104PortName,
       "epc1104PortState": epc1104PortState,
       "epc1104PortSwitchCount": epc1104PortSwitchCount,
       "epc1104PortStartupMode": epc1104PortStartupMode,
       "epc1104PortStartupDelay": epc1104PortStartupDelay,
       "epc1104PortRepowerTime": epc1104PortRepowerTime,
       "epc1104ExtActors": epc1104ExtActors,
       "epc1104IntSensors": epc1104IntSensors,
       "epc1104ExtSensors": epc1104ExtSensors,
       "epc1104SensorTable": epc1104SensorTable,
       "epc1104SensorEntry": epc1104SensorEntry,
       "epc1104SensorIndex": epc1104SensorIndex,
       "epc1104TempSensor": epc1104TempSensor,
       "epc1104HygroSensor": epc1104HygroSensor,
       "epc1104InputSensor": epc1104InputSensor,
       "epc1104AirPressure": epc1104AirPressure,
       "epc1104DewPoint": epc1104DewPoint,
       "epc1104DewPointDiff": epc1104DewPointDiff,
       "epc1104Conf": epc1104Conf,
       "epc1104Groups": epc1104Groups,
       "epc1104BasicGroup": epc1104BasicGroup,
       "epc1104NotificationGroup": epc1104NotificationGroup,
       "epc1104Compls": epc1104Compls,
       "events": events,
       "epc1104SwitchEvtPort": epc1104SwitchEvtPort,
       "epc1104TempEvtSen": epc1104TempEvtSen,
       "epc1104HygroEvtSen": epc1104HygroEvtSen,
       "epc1104InputEvtSen": epc1104InputEvtSen,
       "epc1104AirPressureEvtSen": epc1104AirPressureEvtSen,
       "epc1104DewPtDiffEvtSen": epc1104DewPtDiffEvtSen}
)
