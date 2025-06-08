# SNMP MIB module (GUDEADS-EPC1105-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-EPC1105-MIB.mib
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

_GadsEPC1105_ObjectIdentity = ObjectIdentity
gadsEPC1105 = _GadsEPC1105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69)
)
_Epc1105Objects_ObjectIdentity = ObjectIdentity
epc1105Objects = _Epc1105Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1)
)
_Epc1105CommonConfig_ObjectIdentity = ObjectIdentity
epc1105CommonConfig = _Epc1105CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 1)
)
_Epc1105SNMPaccess_ObjectIdentity = ObjectIdentity
epc1105SNMPaccess = _Epc1105SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 1, 1)
)


class _Epc1105TrapCtrl_Type(Integer32):
    """Custom type epc1105TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Epc1105TrapCtrl_Type.__name__ = "Integer32"
_Epc1105TrapCtrl_Object = MibScalar
epc1105TrapCtrl = _Epc1105TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 1, 1, 1),
    _Epc1105TrapCtrl_Type()
)
epc1105TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1105TrapCtrl.setStatus("current")
_Epc1105TrapIPTable_Object = MibTable
epc1105TrapIPTable = _Epc1105TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    epc1105TrapIPTable.setStatus("current")
_Epc1105TrapIPEntry_Object = MibTableRow
epc1105TrapIPEntry = _Epc1105TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 1, 1, 2, 1)
)
epc1105TrapIPEntry.setIndexNames(
    (0, "GUDEADS-EPC1105-MIB", "epc1105TrapIPIndex"),
)
if mibBuilder.loadTexts:
    epc1105TrapIPEntry.setStatus("current")


class _Epc1105TrapIPIndex_Type(Integer32):
    """Custom type epc1105TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc1105TrapIPIndex_Type.__name__ = "Integer32"
_Epc1105TrapIPIndex_Object = MibTableColumn
epc1105TrapIPIndex = _Epc1105TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 1, 1, 2, 1, 1),
    _Epc1105TrapIPIndex_Type()
)
epc1105TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105TrapIPIndex.setStatus("current")


class _Epc1105TrapAddr_Type(OctetString):
    """Custom type epc1105TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Epc1105TrapAddr_Type.__name__ = "OctetString"
_Epc1105TrapAddr_Object = MibTableColumn
epc1105TrapAddr = _Epc1105TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 1, 1, 2, 1, 2),
    _Epc1105TrapAddr_Type()
)
epc1105TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1105TrapAddr.setStatus("current")
_Epc1105DeviceConfig_ObjectIdentity = ObjectIdentity
epc1105DeviceConfig = _Epc1105DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 2)
)
_Epc1105IntActors_ObjectIdentity = ObjectIdentity
epc1105IntActors = _Epc1105IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 3)
)
_Epc1105relayports_ObjectIdentity = ObjectIdentity
epc1105relayports = _Epc1105relayports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 3, 1)
)


class _Epc1105portNumber_Type(Integer32):
    """Custom type epc1105portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1105portNumber_Type.__name__ = "Integer32"
_Epc1105portNumber_Object = MibScalar
epc1105portNumber = _Epc1105portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 3, 1, 1),
    _Epc1105portNumber_Type()
)
epc1105portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105portNumber.setStatus("current")
_Epc1105portTable_Object = MibTable
epc1105portTable = _Epc1105portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    epc1105portTable.setStatus("current")
_Epc1105portEntry_Object = MibTableRow
epc1105portEntry = _Epc1105portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 3, 1, 2, 1)
)
epc1105portEntry.setIndexNames(
    (0, "GUDEADS-EPC1105-MIB", "epc1105PortIndex"),
)
if mibBuilder.loadTexts:
    epc1105portEntry.setStatus("current")


class _Epc1105PortIndex_Type(Integer32):
    """Custom type epc1105PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1105PortIndex_Type.__name__ = "Integer32"
_Epc1105PortIndex_Object = MibTableColumn
epc1105PortIndex = _Epc1105PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 3, 1, 2, 1, 1),
    _Epc1105PortIndex_Type()
)
epc1105PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105PortIndex.setStatus("current")


class _Epc1105PortName_Type(OctetString):
    """Custom type epc1105PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Epc1105PortName_Type.__name__ = "OctetString"
_Epc1105PortName_Object = MibTableColumn
epc1105PortName = _Epc1105PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 3, 1, 2, 1, 2),
    _Epc1105PortName_Type()
)
epc1105PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1105PortName.setStatus("current")


class _Epc1105PortState_Type(Integer32):
    """Custom type epc1105PortState based on Integer32"""
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


_Epc1105PortState_Type.__name__ = "Integer32"
_Epc1105PortState_Object = MibTableColumn
epc1105PortState = _Epc1105PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 3, 1, 2, 1, 3),
    _Epc1105PortState_Type()
)
epc1105PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1105PortState.setStatus("current")
_Epc1105PortSwitchCount_Type = Integer32
_Epc1105PortSwitchCount_Object = MibTableColumn
epc1105PortSwitchCount = _Epc1105PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 3, 1, 2, 1, 4),
    _Epc1105PortSwitchCount_Type()
)
epc1105PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105PortSwitchCount.setStatus("current")


class _Epc1105PortStartupMode_Type(Integer32):
    """Custom type epc1105PortStartupMode based on Integer32"""
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


_Epc1105PortStartupMode_Type.__name__ = "Integer32"
_Epc1105PortStartupMode_Object = MibTableColumn
epc1105PortStartupMode = _Epc1105PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 3, 1, 2, 1, 5),
    _Epc1105PortStartupMode_Type()
)
epc1105PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1105PortStartupMode.setStatus("current")


class _Epc1105PortStartupDelay_Type(Integer32):
    """Custom type epc1105PortStartupDelay based on Integer32"""
    defaultValue = 0


_Epc1105PortStartupDelay_Type.__name__ = "Integer32"
_Epc1105PortStartupDelay_Object = MibTableColumn
epc1105PortStartupDelay = _Epc1105PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 3, 1, 2, 1, 6),
    _Epc1105PortStartupDelay_Type()
)
epc1105PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1105PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    epc1105PortStartupDelay.setUnits("seconds")


class _Epc1105PortRepowerTime_Type(Integer32):
    """Custom type epc1105PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Epc1105PortRepowerTime_Type.__name__ = "Integer32"
_Epc1105PortRepowerTime_Object = MibTableColumn
epc1105PortRepowerTime = _Epc1105PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 3, 1, 2, 1, 7),
    _Epc1105PortRepowerTime_Type()
)
epc1105PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1105PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    epc1105PortRepowerTime.setUnits("seconds")
_Epc1105ExtActors_ObjectIdentity = ObjectIdentity
epc1105ExtActors = _Epc1105ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 4)
)
_Epc1105IntSensors_ObjectIdentity = ObjectIdentity
epc1105IntSensors = _Epc1105IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5)
)
_Epc1105PowerChan_ObjectIdentity = ObjectIdentity
epc1105PowerChan = _Epc1105PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1)
)


class _Epc1105ActivePowerChan_Type(Unsigned32):
    """Custom type epc1105ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1105ActivePowerChan_Type.__name__ = "Unsigned32"
_Epc1105ActivePowerChan_Object = MibScalar
epc1105ActivePowerChan = _Epc1105ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 1),
    _Epc1105ActivePowerChan_Type()
)
epc1105ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105ActivePowerChan.setStatus("current")
_Epc1105PowerTable_Object = MibTable
epc1105PowerTable = _Epc1105PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    epc1105PowerTable.setStatus("current")
_Epc1105PowerEntry_Object = MibTableRow
epc1105PowerEntry = _Epc1105PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1)
)
epc1105PowerEntry.setIndexNames(
    (0, "GUDEADS-EPC1105-MIB", "epc1105PowerIndex"),
)
if mibBuilder.loadTexts:
    epc1105PowerEntry.setStatus("current")


class _Epc1105PowerIndex_Type(Integer32):
    """Custom type epc1105PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1105PowerIndex_Type.__name__ = "Integer32"
_Epc1105PowerIndex_Object = MibTableColumn
epc1105PowerIndex = _Epc1105PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 1),
    _Epc1105PowerIndex_Type()
)
epc1105PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105PowerIndex.setStatus("current")


class _Epc1105ChanStatus_Type(Integer32):
    """Custom type epc1105ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc1105ChanStatus_Type.__name__ = "Integer32"
_Epc1105ChanStatus_Object = MibTableColumn
epc1105ChanStatus = _Epc1105ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 2),
    _Epc1105ChanStatus_Type()
)
epc1105ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105ChanStatus.setStatus("current")
_Epc1105AbsEnergyActive_Type = Unsigned32
_Epc1105AbsEnergyActive_Object = MibTableColumn
epc1105AbsEnergyActive = _Epc1105AbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 3),
    _Epc1105AbsEnergyActive_Type()
)
epc1105AbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105AbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc1105AbsEnergyActive.setUnits("Wh")
_Epc1105PowerActive_Type = Integer32
_Epc1105PowerActive_Object = MibTableColumn
epc1105PowerActive = _Epc1105PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 4),
    _Epc1105PowerActive_Type()
)
epc1105PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    epc1105PowerActive.setUnits("W")
_Epc1105Current_Type = Unsigned32
_Epc1105Current_Object = MibTableColumn
epc1105Current = _Epc1105Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 5),
    _Epc1105Current_Type()
)
epc1105Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105Current.setStatus("current")
if mibBuilder.loadTexts:
    epc1105Current.setUnits("mA")
_Epc1105Voltage_Type = Unsigned32
_Epc1105Voltage_Object = MibTableColumn
epc1105Voltage = _Epc1105Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 6),
    _Epc1105Voltage_Type()
)
epc1105Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105Voltage.setStatus("current")
if mibBuilder.loadTexts:
    epc1105Voltage.setUnits("V")
_Epc1105Frequency_Type = Unsigned32
_Epc1105Frequency_Object = MibTableColumn
epc1105Frequency = _Epc1105Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 7),
    _Epc1105Frequency_Type()
)
epc1105Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105Frequency.setStatus("current")
if mibBuilder.loadTexts:
    epc1105Frequency.setUnits("0.01 hz")
_Epc1105PowerFactor_Type = Integer32
_Epc1105PowerFactor_Object = MibTableColumn
epc1105PowerFactor = _Epc1105PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 8),
    _Epc1105PowerFactor_Type()
)
epc1105PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    epc1105PowerFactor.setUnits("0.001")
_Epc1105Pangle_Type = Integer32
_Epc1105Pangle_Object = MibTableColumn
epc1105Pangle = _Epc1105Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 9),
    _Epc1105Pangle_Type()
)
epc1105Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105Pangle.setStatus("current")
if mibBuilder.loadTexts:
    epc1105Pangle.setUnits("0.1 degree")
_Epc1105PowerApparent_Type = Integer32
_Epc1105PowerApparent_Object = MibTableColumn
epc1105PowerApparent = _Epc1105PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 10),
    _Epc1105PowerApparent_Type()
)
epc1105PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    epc1105PowerApparent.setUnits("VA")
_Epc1105PowerReactive_Type = Integer32
_Epc1105PowerReactive_Object = MibTableColumn
epc1105PowerReactive = _Epc1105PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 11),
    _Epc1105PowerReactive_Type()
)
epc1105PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc1105PowerReactive.setUnits("VAR")
_Epc1105AbsEnergyReactive_Type = Unsigned32
_Epc1105AbsEnergyReactive_Object = MibTableColumn
epc1105AbsEnergyReactive = _Epc1105AbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 12),
    _Epc1105AbsEnergyReactive_Type()
)
epc1105AbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105AbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc1105AbsEnergyReactive.setUnits("VARh")
_Epc1105AbsEnergyActiveResettable_Type = Unsigned32
_Epc1105AbsEnergyActiveResettable_Object = MibTableColumn
epc1105AbsEnergyActiveResettable = _Epc1105AbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 13),
    _Epc1105AbsEnergyActiveResettable_Type()
)
epc1105AbsEnergyActiveResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1105AbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1105AbsEnergyActiveResettable.setUnits("Wh")
_Epc1105AbsEnergyReactiveResettable_Type = Unsigned32
_Epc1105AbsEnergyReactiveResettable_Object = MibTableColumn
epc1105AbsEnergyReactiveResettable = _Epc1105AbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 14),
    _Epc1105AbsEnergyReactiveResettable_Type()
)
epc1105AbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105AbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1105AbsEnergyReactiveResettable.setUnits("VARh")
_Epc1105ResetTime_Type = Unsigned32
_Epc1105ResetTime_Object = MibTableColumn
epc1105ResetTime = _Epc1105ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 15),
    _Epc1105ResetTime_Type()
)
epc1105ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    epc1105ResetTime.setUnits("s")
_Epc1105ForwEnergyActive_Type = Unsigned32
_Epc1105ForwEnergyActive_Object = MibTableColumn
epc1105ForwEnergyActive = _Epc1105ForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 16),
    _Epc1105ForwEnergyActive_Type()
)
epc1105ForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105ForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc1105ForwEnergyActive.setUnits("Wh")
_Epc1105ForwEnergyReactive_Type = Unsigned32
_Epc1105ForwEnergyReactive_Object = MibTableColumn
epc1105ForwEnergyReactive = _Epc1105ForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 17),
    _Epc1105ForwEnergyReactive_Type()
)
epc1105ForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105ForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc1105ForwEnergyReactive.setUnits("VARh")
_Epc1105ForwEnergyActiveResettable_Type = Unsigned32
_Epc1105ForwEnergyActiveResettable_Object = MibTableColumn
epc1105ForwEnergyActiveResettable = _Epc1105ForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 18),
    _Epc1105ForwEnergyActiveResettable_Type()
)
epc1105ForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105ForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1105ForwEnergyActiveResettable.setUnits("Wh")
_Epc1105ForwEnergyReactiveResettable_Type = Unsigned32
_Epc1105ForwEnergyReactiveResettable_Object = MibTableColumn
epc1105ForwEnergyReactiveResettable = _Epc1105ForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 19),
    _Epc1105ForwEnergyReactiveResettable_Type()
)
epc1105ForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105ForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1105ForwEnergyReactiveResettable.setUnits("VARh")
_Epc1105RevEnergyActive_Type = Unsigned32
_Epc1105RevEnergyActive_Object = MibTableColumn
epc1105RevEnergyActive = _Epc1105RevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 20),
    _Epc1105RevEnergyActive_Type()
)
epc1105RevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105RevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc1105RevEnergyActive.setUnits("Wh")
_Epc1105RevEnergyReactive_Type = Unsigned32
_Epc1105RevEnergyReactive_Object = MibTableColumn
epc1105RevEnergyReactive = _Epc1105RevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 21),
    _Epc1105RevEnergyReactive_Type()
)
epc1105RevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105RevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc1105RevEnergyReactive.setUnits("VARh")
_Epc1105RevEnergyActiveResettable_Type = Unsigned32
_Epc1105RevEnergyActiveResettable_Object = MibTableColumn
epc1105RevEnergyActiveResettable = _Epc1105RevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 22),
    _Epc1105RevEnergyActiveResettable_Type()
)
epc1105RevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105RevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1105RevEnergyActiveResettable.setUnits("Wh")
_Epc1105RevEnergyReactiveResettable_Type = Unsigned32
_Epc1105RevEnergyReactiveResettable_Object = MibTableColumn
epc1105RevEnergyReactiveResettable = _Epc1105RevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 5, 1, 2, 1, 23),
    _Epc1105RevEnergyReactiveResettable_Type()
)
epc1105RevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105RevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1105RevEnergyReactiveResettable.setUnits("VARh")
_Epc1105ExtSensors_ObjectIdentity = ObjectIdentity
epc1105ExtSensors = _Epc1105ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 6)
)
_Epc1105SensorTable_Object = MibTable
epc1105SensorTable = _Epc1105SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 6, 1)
)
if mibBuilder.loadTexts:
    epc1105SensorTable.setStatus("current")
_Epc1105SensorEntry_Object = MibTableRow
epc1105SensorEntry = _Epc1105SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 6, 1, 1)
)
epc1105SensorEntry.setIndexNames(
    (0, "GUDEADS-EPC1105-MIB", "epc1105SensorIndex"),
)
if mibBuilder.loadTexts:
    epc1105SensorEntry.setStatus("current")


class _Epc1105SensorIndex_Type(Integer32):
    """Custom type epc1105SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1105SensorIndex_Type.__name__ = "Integer32"
_Epc1105SensorIndex_Object = MibTableColumn
epc1105SensorIndex = _Epc1105SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 6, 1, 1, 1),
    _Epc1105SensorIndex_Type()
)
epc1105SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105SensorIndex.setStatus("current")
_Epc1105TempSensor_Type = Integer32
_Epc1105TempSensor_Object = MibTableColumn
epc1105TempSensor = _Epc1105TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 6, 1, 1, 2),
    _Epc1105TempSensor_Type()
)
epc1105TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc1105TempSensor.setUnits("0.1 degree Celsius")
_Epc1105HygroSensor_Type = Integer32
_Epc1105HygroSensor_Object = MibTableColumn
epc1105HygroSensor = _Epc1105HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 6, 1, 1, 3),
    _Epc1105HygroSensor_Type()
)
epc1105HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc1105HygroSensor.setUnits("0.1 percent humidity")


class _Epc1105InputSensor_Type(Integer32):
    """Custom type epc1105InputSensor based on Integer32"""
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


_Epc1105InputSensor_Type.__name__ = "Integer32"
_Epc1105InputSensor_Object = MibTableColumn
epc1105InputSensor = _Epc1105InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 6, 1, 1, 4),
    _Epc1105InputSensor_Type()
)
epc1105InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105InputSensor.setStatus("current")
_Epc1105AirPressure_Type = Integer32
_Epc1105AirPressure_Object = MibTableColumn
epc1105AirPressure = _Epc1105AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 6, 1, 1, 5),
    _Epc1105AirPressure_Type()
)
epc1105AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    epc1105AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Epc1105DewPoint_Type = Integer32
_Epc1105DewPoint_Object = MibTableColumn
epc1105DewPoint = _Epc1105DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 6, 1, 1, 6),
    _Epc1105DewPoint_Type()
)
epc1105DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    epc1105DewPoint.setUnits("0.1 degree Celsius")
_Epc1105DewPointDiff_Type = Integer32
_Epc1105DewPointDiff_Object = MibTableColumn
epc1105DewPointDiff = _Epc1105DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 69, 1, 6, 1, 1, 7),
    _Epc1105DewPointDiff_Type()
)
epc1105DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1105DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    epc1105DewPointDiff.setUnits("0.1 degree Celsius")
_Epc1105Conf_ObjectIdentity = ObjectIdentity
epc1105Conf = _Epc1105Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 2)
)
_Epc1105Groups_ObjectIdentity = ObjectIdentity
epc1105Groups = _Epc1105Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 2, 1)
)
_Epc1105Compls_ObjectIdentity = ObjectIdentity
epc1105Compls = _Epc1105Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 69, 3)
)

# Managed Objects groups

epc1105BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 69, 2, 1, 1)
)
epc1105BasicGroup.setObjects(
      *(("GUDEADS-EPC1105-MIB", "epc1105TrapCtrl"),
        ("GUDEADS-EPC1105-MIB", "epc1105TrapIPIndex"),
        ("GUDEADS-EPC1105-MIB", "epc1105TrapAddr"),
        ("GUDEADS-EPC1105-MIB", "epc1105portNumber"),
        ("GUDEADS-EPC1105-MIB", "epc1105PortIndex"),
        ("GUDEADS-EPC1105-MIB", "epc1105PortName"),
        ("GUDEADS-EPC1105-MIB", "epc1105PortState"),
        ("GUDEADS-EPC1105-MIB", "epc1105PortSwitchCount"),
        ("GUDEADS-EPC1105-MIB", "epc1105PortStartupMode"),
        ("GUDEADS-EPC1105-MIB", "epc1105PortStartupDelay"),
        ("GUDEADS-EPC1105-MIB", "epc1105PortRepowerTime"),
        ("GUDEADS-EPC1105-MIB", "epc1105ActivePowerChan"),
        ("GUDEADS-EPC1105-MIB", "epc1105PowerIndex"),
        ("GUDEADS-EPC1105-MIB", "epc1105ChanStatus"),
        ("GUDEADS-EPC1105-MIB", "epc1105AbsEnergyActive"),
        ("GUDEADS-EPC1105-MIB", "epc1105PowerActive"),
        ("GUDEADS-EPC1105-MIB", "epc1105Current"),
        ("GUDEADS-EPC1105-MIB", "epc1105Voltage"),
        ("GUDEADS-EPC1105-MIB", "epc1105Frequency"),
        ("GUDEADS-EPC1105-MIB", "epc1105PowerFactor"),
        ("GUDEADS-EPC1105-MIB", "epc1105Pangle"),
        ("GUDEADS-EPC1105-MIB", "epc1105PowerApparent"),
        ("GUDEADS-EPC1105-MIB", "epc1105PowerReactive"),
        ("GUDEADS-EPC1105-MIB", "epc1105AbsEnergyReactive"),
        ("GUDEADS-EPC1105-MIB", "epc1105AbsEnergyActiveResettable"),
        ("GUDEADS-EPC1105-MIB", "epc1105AbsEnergyReactiveResettable"),
        ("GUDEADS-EPC1105-MIB", "epc1105ResetTime"),
        ("GUDEADS-EPC1105-MIB", "epc1105ForwEnergyActive"),
        ("GUDEADS-EPC1105-MIB", "epc1105ForwEnergyReactive"),
        ("GUDEADS-EPC1105-MIB", "epc1105ForwEnergyActiveResettable"),
        ("GUDEADS-EPC1105-MIB", "epc1105ForwEnergyReactiveResettable"),
        ("GUDEADS-EPC1105-MIB", "epc1105RevEnergyActive"),
        ("GUDEADS-EPC1105-MIB", "epc1105RevEnergyReactive"),
        ("GUDEADS-EPC1105-MIB", "epc1105RevEnergyActiveResettable"),
        ("GUDEADS-EPC1105-MIB", "epc1105RevEnergyReactiveResettable"),
        ("GUDEADS-EPC1105-MIB", "epc1105SensorIndex"),
        ("GUDEADS-EPC1105-MIB", "epc1105TempSensor"),
        ("GUDEADS-EPC1105-MIB", "epc1105HygroSensor"),
        ("GUDEADS-EPC1105-MIB", "epc1105InputSensor"),
        ("GUDEADS-EPC1105-MIB", "epc1105AirPressure"),
        ("GUDEADS-EPC1105-MIB", "epc1105DewPoint"),
        ("GUDEADS-EPC1105-MIB", "epc1105DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc1105BasicGroup.setStatus("current")


# Notification objects

epc1105SwitchEvtPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 69, 3, 1)
)
epc1105SwitchEvtPort.setObjects(
      *(("GUDEADS-EPC1105-MIB", "epc1105PortIndex"),
        ("GUDEADS-EPC1105-MIB", "epc1105PortName"),
        ("GUDEADS-EPC1105-MIB", "epc1105PortState"),
        ("GUDEADS-EPC1105-MIB", "epc1105PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc1105SwitchEvtPort.setStatus(
        "current"
    )

epc1105TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 69, 3, 2)
)
epc1105TempEvtSen.setObjects(
      *(("GUDEADS-EPC1105-MIB", "epc1105SensorIndex"),
        ("GUDEADS-EPC1105-MIB", "epc1105TempSensor"))
)
if mibBuilder.loadTexts:
    epc1105TempEvtSen.setStatus(
        "current"
    )

epc1105HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 69, 3, 3)
)
epc1105HygroEvtSen.setObjects(
      *(("GUDEADS-EPC1105-MIB", "epc1105SensorIndex"),
        ("GUDEADS-EPC1105-MIB", "epc1105HygroSensor"))
)
if mibBuilder.loadTexts:
    epc1105HygroEvtSen.setStatus(
        "current"
    )

epc1105InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 69, 3, 4)
)
epc1105InputEvtSen.setObjects(
      *(("GUDEADS-EPC1105-MIB", "epc1105SensorIndex"),
        ("GUDEADS-EPC1105-MIB", "epc1105InputSensor"))
)
if mibBuilder.loadTexts:
    epc1105InputEvtSen.setStatus(
        "current"
    )

epc1105AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 69, 3, 5)
)
epc1105AirPressureEvtSen.setObjects(
      *(("GUDEADS-EPC1105-MIB", "epc1105SensorIndex"),
        ("GUDEADS-EPC1105-MIB", "epc1105AirPressure"))
)
if mibBuilder.loadTexts:
    epc1105AirPressureEvtSen.setStatus(
        "current"
    )

epc1105DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 69, 3, 6)
)
epc1105DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-EPC1105-MIB", "epc1105SensorIndex"),
        ("GUDEADS-EPC1105-MIB", "epc1105DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc1105DewPtDiffEvtSen.setStatus(
        "current"
    )

epc1105LineAmperageEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 69, 3, 7)
)
epc1105LineAmperageEvt.setObjects(
      *(("GUDEADS-EPC1105-MIB", "epc1105PowerIndex"),
        ("GUDEADS-EPC1105-MIB", "epc1105PowerActive"),
        ("GUDEADS-EPC1105-MIB", "epc1105Current"),
        ("GUDEADS-EPC1105-MIB", "epc1105Voltage"),
        ("GUDEADS-EPC1105-MIB", "epc1105Frequency"),
        ("GUDEADS-EPC1105-MIB", "epc1105PowerApparent"),
        ("GUDEADS-EPC1105-MIB", "epc1105PowerReactive"))
)
if mibBuilder.loadTexts:
    epc1105LineAmperageEvt.setStatus(
        "current"
    )


# Notifications groups

epc1105NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 69, 2, 1, 2)
)
epc1105NotificationGroup.setObjects(
      *(("GUDEADS-EPC1105-MIB", "epc1105HygroEvtSen"),
        ("GUDEADS-EPC1105-MIB", "epc1105SwitchEvtPort"),
        ("GUDEADS-EPC1105-MIB", "epc1105TempEvtSen"),
        ("GUDEADS-EPC1105-MIB", "epc1105InputEvtSen"),
        ("GUDEADS-EPC1105-MIB", "epc1105AirPressureEvtSen"),
        ("GUDEADS-EPC1105-MIB", "epc1105DewPtDiffEvtSen"),
        ("GUDEADS-EPC1105-MIB", "epc1105LineAmperageEvt"))
)
if mibBuilder.loadTexts:
    epc1105NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-EPC1105-MIB",
    **{"gudeads": gudeads,
       "gadsEPC1105": gadsEPC1105,
       "epc1105Objects": epc1105Objects,
       "epc1105CommonConfig": epc1105CommonConfig,
       "epc1105SNMPaccess": epc1105SNMPaccess,
       "epc1105TrapCtrl": epc1105TrapCtrl,
       "epc1105TrapIPTable": epc1105TrapIPTable,
       "epc1105TrapIPEntry": epc1105TrapIPEntry,
       "epc1105TrapIPIndex": epc1105TrapIPIndex,
       "epc1105TrapAddr": epc1105TrapAddr,
       "epc1105DeviceConfig": epc1105DeviceConfig,
       "epc1105IntActors": epc1105IntActors,
       "epc1105relayports": epc1105relayports,
       "epc1105portNumber": epc1105portNumber,
       "epc1105portTable": epc1105portTable,
       "epc1105portEntry": epc1105portEntry,
       "epc1105PortIndex": epc1105PortIndex,
       "epc1105PortName": epc1105PortName,
       "epc1105PortState": epc1105PortState,
       "epc1105PortSwitchCount": epc1105PortSwitchCount,
       "epc1105PortStartupMode": epc1105PortStartupMode,
       "epc1105PortStartupDelay": epc1105PortStartupDelay,
       "epc1105PortRepowerTime": epc1105PortRepowerTime,
       "epc1105ExtActors": epc1105ExtActors,
       "epc1105IntSensors": epc1105IntSensors,
       "epc1105PowerChan": epc1105PowerChan,
       "epc1105ActivePowerChan": epc1105ActivePowerChan,
       "epc1105PowerTable": epc1105PowerTable,
       "epc1105PowerEntry": epc1105PowerEntry,
       "epc1105PowerIndex": epc1105PowerIndex,
       "epc1105ChanStatus": epc1105ChanStatus,
       "epc1105AbsEnergyActive": epc1105AbsEnergyActive,
       "epc1105PowerActive": epc1105PowerActive,
       "epc1105Current": epc1105Current,
       "epc1105Voltage": epc1105Voltage,
       "epc1105Frequency": epc1105Frequency,
       "epc1105PowerFactor": epc1105PowerFactor,
       "epc1105Pangle": epc1105Pangle,
       "epc1105PowerApparent": epc1105PowerApparent,
       "epc1105PowerReactive": epc1105PowerReactive,
       "epc1105AbsEnergyReactive": epc1105AbsEnergyReactive,
       "epc1105AbsEnergyActiveResettable": epc1105AbsEnergyActiveResettable,
       "epc1105AbsEnergyReactiveResettable": epc1105AbsEnergyReactiveResettable,
       "epc1105ResetTime": epc1105ResetTime,
       "epc1105ForwEnergyActive": epc1105ForwEnergyActive,
       "epc1105ForwEnergyReactive": epc1105ForwEnergyReactive,
       "epc1105ForwEnergyActiveResettable": epc1105ForwEnergyActiveResettable,
       "epc1105ForwEnergyReactiveResettable": epc1105ForwEnergyReactiveResettable,
       "epc1105RevEnergyActive": epc1105RevEnergyActive,
       "epc1105RevEnergyReactive": epc1105RevEnergyReactive,
       "epc1105RevEnergyActiveResettable": epc1105RevEnergyActiveResettable,
       "epc1105RevEnergyReactiveResettable": epc1105RevEnergyReactiveResettable,
       "epc1105ExtSensors": epc1105ExtSensors,
       "epc1105SensorTable": epc1105SensorTable,
       "epc1105SensorEntry": epc1105SensorEntry,
       "epc1105SensorIndex": epc1105SensorIndex,
       "epc1105TempSensor": epc1105TempSensor,
       "epc1105HygroSensor": epc1105HygroSensor,
       "epc1105InputSensor": epc1105InputSensor,
       "epc1105AirPressure": epc1105AirPressure,
       "epc1105DewPoint": epc1105DewPoint,
       "epc1105DewPointDiff": epc1105DewPointDiff,
       "epc1105Conf": epc1105Conf,
       "epc1105Groups": epc1105Groups,
       "epc1105BasicGroup": epc1105BasicGroup,
       "epc1105NotificationGroup": epc1105NotificationGroup,
       "epc1105Compls": epc1105Compls,
       "events": events,
       "epc1105SwitchEvtPort": epc1105SwitchEvtPort,
       "epc1105TempEvtSen": epc1105TempEvtSen,
       "epc1105HygroEvtSen": epc1105HygroEvtSen,
       "epc1105InputEvtSen": epc1105InputEvtSen,
       "epc1105AirPressureEvtSen": epc1105AirPressureEvtSen,
       "epc1105DewPtDiffEvtSen": epc1105DewPtDiffEvtSen,
       "epc1105LineAmperageEvt": epc1105LineAmperageEvt}
)
