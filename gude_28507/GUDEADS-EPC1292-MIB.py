# SNMP MIB module (GUDEADS-EPC1292-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-EPC1292-MIB.mib
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

_GadsEPC1292_ObjectIdentity = ObjectIdentity
gadsEPC1292 = _GadsEPC1292_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50)
)
_Epc1292Objects_ObjectIdentity = ObjectIdentity
epc1292Objects = _Epc1292Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1)
)
_Epc1292CommonConfig_ObjectIdentity = ObjectIdentity
epc1292CommonConfig = _Epc1292CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 1)
)
_Epc1292SNMPaccess_ObjectIdentity = ObjectIdentity
epc1292SNMPaccess = _Epc1292SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 1, 1)
)


class _Epc1292TrapCtrl_Type(Integer32):
    """Custom type epc1292TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Epc1292TrapCtrl_Type.__name__ = "Integer32"
_Epc1292TrapCtrl_Object = MibScalar
epc1292TrapCtrl = _Epc1292TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 1, 1, 1),
    _Epc1292TrapCtrl_Type()
)
epc1292TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1292TrapCtrl.setStatus("current")
_Epc1292TrapIPTable_Object = MibTable
epc1292TrapIPTable = _Epc1292TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    epc1292TrapIPTable.setStatus("current")
_Epc1292TrapIPEntry_Object = MibTableRow
epc1292TrapIPEntry = _Epc1292TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 1, 1, 2, 1)
)
epc1292TrapIPEntry.setIndexNames(
    (0, "GUDEADS-EPC1292-MIB", "epc1292TrapIPIndex"),
)
if mibBuilder.loadTexts:
    epc1292TrapIPEntry.setStatus("current")


class _Epc1292TrapIPIndex_Type(Integer32):
    """Custom type epc1292TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc1292TrapIPIndex_Type.__name__ = "Integer32"
_Epc1292TrapIPIndex_Object = MibTableColumn
epc1292TrapIPIndex = _Epc1292TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 1, 1, 2, 1, 1),
    _Epc1292TrapIPIndex_Type()
)
epc1292TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292TrapIPIndex.setStatus("current")


class _Epc1292TrapAddr_Type(OctetString):
    """Custom type epc1292TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Epc1292TrapAddr_Type.__name__ = "OctetString"
_Epc1292TrapAddr_Object = MibTableColumn
epc1292TrapAddr = _Epc1292TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 1, 1, 2, 1, 2),
    _Epc1292TrapAddr_Type()
)
epc1292TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1292TrapAddr.setStatus("current")
_Epc1292DeviceConfig_ObjectIdentity = ObjectIdentity
epc1292DeviceConfig = _Epc1292DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 2)
)
_Epc1292IntActors_ObjectIdentity = ObjectIdentity
epc1292IntActors = _Epc1292IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 3)
)
_Epc1292relayports_ObjectIdentity = ObjectIdentity
epc1292relayports = _Epc1292relayports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 3, 1)
)


class _Epc1292portNumber_Type(Integer32):
    """Custom type epc1292portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Epc1292portNumber_Type.__name__ = "Integer32"
_Epc1292portNumber_Object = MibScalar
epc1292portNumber = _Epc1292portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 3, 1, 1),
    _Epc1292portNumber_Type()
)
epc1292portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292portNumber.setStatus("current")
_Epc1292portTable_Object = MibTable
epc1292portTable = _Epc1292portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    epc1292portTable.setStatus("current")
_Epc1292portEntry_Object = MibTableRow
epc1292portEntry = _Epc1292portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 3, 1, 2, 1)
)
epc1292portEntry.setIndexNames(
    (0, "GUDEADS-EPC1292-MIB", "epc1292PortIndex"),
)
if mibBuilder.loadTexts:
    epc1292portEntry.setStatus("current")


class _Epc1292PortIndex_Type(Integer32):
    """Custom type epc1292PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Epc1292PortIndex_Type.__name__ = "Integer32"
_Epc1292PortIndex_Object = MibTableColumn
epc1292PortIndex = _Epc1292PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 3, 1, 2, 1, 1),
    _Epc1292PortIndex_Type()
)
epc1292PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292PortIndex.setStatus("current")


class _Epc1292PortName_Type(OctetString):
    """Custom type epc1292PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Epc1292PortName_Type.__name__ = "OctetString"
_Epc1292PortName_Object = MibTableColumn
epc1292PortName = _Epc1292PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 3, 1, 2, 1, 2),
    _Epc1292PortName_Type()
)
epc1292PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1292PortName.setStatus("current")


class _Epc1292PortState_Type(Integer32):
    """Custom type epc1292PortState based on Integer32"""
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


_Epc1292PortState_Type.__name__ = "Integer32"
_Epc1292PortState_Object = MibTableColumn
epc1292PortState = _Epc1292PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 3, 1, 2, 1, 3),
    _Epc1292PortState_Type()
)
epc1292PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1292PortState.setStatus("current")
_Epc1292PortSwitchCount_Type = Integer32
_Epc1292PortSwitchCount_Object = MibTableColumn
epc1292PortSwitchCount = _Epc1292PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 3, 1, 2, 1, 4),
    _Epc1292PortSwitchCount_Type()
)
epc1292PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292PortSwitchCount.setStatus("current")


class _Epc1292PortStartupMode_Type(Integer32):
    """Custom type epc1292PortStartupMode based on Integer32"""
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


_Epc1292PortStartupMode_Type.__name__ = "Integer32"
_Epc1292PortStartupMode_Object = MibTableColumn
epc1292PortStartupMode = _Epc1292PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 3, 1, 2, 1, 5),
    _Epc1292PortStartupMode_Type()
)
epc1292PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1292PortStartupMode.setStatus("current")


class _Epc1292PortStartupDelay_Type(Integer32):
    """Custom type epc1292PortStartupDelay based on Integer32"""
    defaultValue = 0


_Epc1292PortStartupDelay_Type.__name__ = "Integer32"
_Epc1292PortStartupDelay_Object = MibTableColumn
epc1292PortStartupDelay = _Epc1292PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 3, 1, 2, 1, 6),
    _Epc1292PortStartupDelay_Type()
)
epc1292PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1292PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    epc1292PortStartupDelay.setUnits("seconds")


class _Epc1292PortRepowerTime_Type(Integer32):
    """Custom type epc1292PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Epc1292PortRepowerTime_Type.__name__ = "Integer32"
_Epc1292PortRepowerTime_Object = MibTableColumn
epc1292PortRepowerTime = _Epc1292PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 3, 1, 2, 1, 7),
    _Epc1292PortRepowerTime_Type()
)
epc1292PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1292PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    epc1292PortRepowerTime.setUnits("seconds")
_Epc1292ExtActors_ObjectIdentity = ObjectIdentity
epc1292ExtActors = _Epc1292ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 4)
)
_Epc1292IntSensors_ObjectIdentity = ObjectIdentity
epc1292IntSensors = _Epc1292IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5)
)
_Epc1292PowerChan_ObjectIdentity = ObjectIdentity
epc1292PowerChan = _Epc1292PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1)
)


class _Epc1292ActivePowerChan_Type(Unsigned32):
    """Custom type epc1292ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1292ActivePowerChan_Type.__name__ = "Unsigned32"
_Epc1292ActivePowerChan_Object = MibScalar
epc1292ActivePowerChan = _Epc1292ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 1),
    _Epc1292ActivePowerChan_Type()
)
epc1292ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292ActivePowerChan.setStatus("current")
_Epc1292PowerTable_Object = MibTable
epc1292PowerTable = _Epc1292PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    epc1292PowerTable.setStatus("current")
_Epc1292PowerEntry_Object = MibTableRow
epc1292PowerEntry = _Epc1292PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1)
)
epc1292PowerEntry.setIndexNames(
    (0, "GUDEADS-EPC1292-MIB", "epc1292PowerIndex"),
)
if mibBuilder.loadTexts:
    epc1292PowerEntry.setStatus("current")


class _Epc1292PowerIndex_Type(Integer32):
    """Custom type epc1292PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1292PowerIndex_Type.__name__ = "Integer32"
_Epc1292PowerIndex_Object = MibTableColumn
epc1292PowerIndex = _Epc1292PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 1),
    _Epc1292PowerIndex_Type()
)
epc1292PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292PowerIndex.setStatus("current")


class _Epc1292ChanStatus_Type(Integer32):
    """Custom type epc1292ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc1292ChanStatus_Type.__name__ = "Integer32"
_Epc1292ChanStatus_Object = MibTableColumn
epc1292ChanStatus = _Epc1292ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 2),
    _Epc1292ChanStatus_Type()
)
epc1292ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292ChanStatus.setStatus("current")
_Epc1292AbsEnergyActive_Type = Gauge32
_Epc1292AbsEnergyActive_Object = MibTableColumn
epc1292AbsEnergyActive = _Epc1292AbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 3),
    _Epc1292AbsEnergyActive_Type()
)
epc1292AbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292AbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc1292AbsEnergyActive.setUnits("Wh")
_Epc1292PowerActive_Type = Integer32
_Epc1292PowerActive_Object = MibTableColumn
epc1292PowerActive = _Epc1292PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 4),
    _Epc1292PowerActive_Type()
)
epc1292PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    epc1292PowerActive.setUnits("W")
_Epc1292Current_Type = Gauge32
_Epc1292Current_Object = MibTableColumn
epc1292Current = _Epc1292Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 5),
    _Epc1292Current_Type()
)
epc1292Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292Current.setStatus("current")
if mibBuilder.loadTexts:
    epc1292Current.setUnits("mA")
_Epc1292Voltage_Type = Gauge32
_Epc1292Voltage_Object = MibTableColumn
epc1292Voltage = _Epc1292Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 6),
    _Epc1292Voltage_Type()
)
epc1292Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292Voltage.setStatus("current")
if mibBuilder.loadTexts:
    epc1292Voltage.setUnits("V")
_Epc1292Frequency_Type = Gauge32
_Epc1292Frequency_Object = MibTableColumn
epc1292Frequency = _Epc1292Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 7),
    _Epc1292Frequency_Type()
)
epc1292Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292Frequency.setStatus("current")
if mibBuilder.loadTexts:
    epc1292Frequency.setUnits("0.01 hz")
_Epc1292PowerFactor_Type = Integer32
_Epc1292PowerFactor_Object = MibTableColumn
epc1292PowerFactor = _Epc1292PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 8),
    _Epc1292PowerFactor_Type()
)
epc1292PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    epc1292PowerFactor.setUnits("0.001")
_Epc1292Pangle_Type = Integer32
_Epc1292Pangle_Object = MibTableColumn
epc1292Pangle = _Epc1292Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 9),
    _Epc1292Pangle_Type()
)
epc1292Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292Pangle.setStatus("current")
if mibBuilder.loadTexts:
    epc1292Pangle.setUnits("0.1 degree")
_Epc1292PowerApparent_Type = Integer32
_Epc1292PowerApparent_Object = MibTableColumn
epc1292PowerApparent = _Epc1292PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 10),
    _Epc1292PowerApparent_Type()
)
epc1292PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    epc1292PowerApparent.setUnits("VA")
_Epc1292PowerReactive_Type = Integer32
_Epc1292PowerReactive_Object = MibTableColumn
epc1292PowerReactive = _Epc1292PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 11),
    _Epc1292PowerReactive_Type()
)
epc1292PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc1292PowerReactive.setUnits("VAR")
_Epc1292AbsEnergyReactive_Type = Gauge32
_Epc1292AbsEnergyReactive_Object = MibTableColumn
epc1292AbsEnergyReactive = _Epc1292AbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 12),
    _Epc1292AbsEnergyReactive_Type()
)
epc1292AbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292AbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc1292AbsEnergyReactive.setUnits("VARh")
_Epc1292AbsEnergyActiveResettable_Type = Gauge32
_Epc1292AbsEnergyActiveResettable_Object = MibTableColumn
epc1292AbsEnergyActiveResettable = _Epc1292AbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 13),
    _Epc1292AbsEnergyActiveResettable_Type()
)
epc1292AbsEnergyActiveResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1292AbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1292AbsEnergyActiveResettable.setUnits("Wh")
_Epc1292AbsEnergyReactiveResettable_Type = Gauge32
_Epc1292AbsEnergyReactiveResettable_Object = MibTableColumn
epc1292AbsEnergyReactiveResettable = _Epc1292AbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 14),
    _Epc1292AbsEnergyReactiveResettable_Type()
)
epc1292AbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292AbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1292AbsEnergyReactiveResettable.setUnits("VARh")
_Epc1292ResetTime_Type = Gauge32
_Epc1292ResetTime_Object = MibTableColumn
epc1292ResetTime = _Epc1292ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 15),
    _Epc1292ResetTime_Type()
)
epc1292ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    epc1292ResetTime.setUnits("s")
_Epc1292ForwEnergyActive_Type = Gauge32
_Epc1292ForwEnergyActive_Object = MibTableColumn
epc1292ForwEnergyActive = _Epc1292ForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 16),
    _Epc1292ForwEnergyActive_Type()
)
epc1292ForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292ForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc1292ForwEnergyActive.setUnits("Wh")
_Epc1292ForwEnergyReactive_Type = Gauge32
_Epc1292ForwEnergyReactive_Object = MibTableColumn
epc1292ForwEnergyReactive = _Epc1292ForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 17),
    _Epc1292ForwEnergyReactive_Type()
)
epc1292ForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292ForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc1292ForwEnergyReactive.setUnits("VARh")
_Epc1292ForwEnergyActiveResettable_Type = Gauge32
_Epc1292ForwEnergyActiveResettable_Object = MibTableColumn
epc1292ForwEnergyActiveResettable = _Epc1292ForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 18),
    _Epc1292ForwEnergyActiveResettable_Type()
)
epc1292ForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292ForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1292ForwEnergyActiveResettable.setUnits("Wh")
_Epc1292ForwEnergyReactiveResettable_Type = Gauge32
_Epc1292ForwEnergyReactiveResettable_Object = MibTableColumn
epc1292ForwEnergyReactiveResettable = _Epc1292ForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 19),
    _Epc1292ForwEnergyReactiveResettable_Type()
)
epc1292ForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292ForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1292ForwEnergyReactiveResettable.setUnits("VARh")
_Epc1292RevEnergyActive_Type = Gauge32
_Epc1292RevEnergyActive_Object = MibTableColumn
epc1292RevEnergyActive = _Epc1292RevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 20),
    _Epc1292RevEnergyActive_Type()
)
epc1292RevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292RevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc1292RevEnergyActive.setUnits("Wh")
_Epc1292RevEnergyReactive_Type = Gauge32
_Epc1292RevEnergyReactive_Object = MibTableColumn
epc1292RevEnergyReactive = _Epc1292RevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 21),
    _Epc1292RevEnergyReactive_Type()
)
epc1292RevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292RevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc1292RevEnergyReactive.setUnits("VARh")
_Epc1292RevEnergyActiveResettable_Type = Gauge32
_Epc1292RevEnergyActiveResettable_Object = MibTableColumn
epc1292RevEnergyActiveResettable = _Epc1292RevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 22),
    _Epc1292RevEnergyActiveResettable_Type()
)
epc1292RevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292RevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1292RevEnergyActiveResettable.setUnits("Wh")
_Epc1292RevEnergyReactiveResettable_Type = Gauge32
_Epc1292RevEnergyReactiveResettable_Object = MibTableColumn
epc1292RevEnergyReactiveResettable = _Epc1292RevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 1, 2, 1, 23),
    _Epc1292RevEnergyReactiveResettable_Type()
)
epc1292RevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292RevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1292RevEnergyReactiveResettable.setUnits("VARh")
_Epc1292OVPTable_Object = MibTable
epc1292OVPTable = _Epc1292OVPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 2)
)
if mibBuilder.loadTexts:
    epc1292OVPTable.setStatus("current")
_Epc1292OVPEntry_Object = MibTableRow
epc1292OVPEntry = _Epc1292OVPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 2, 1)
)
epc1292OVPEntry.setIndexNames(
    (0, "GUDEADS-EPC1292-MIB", "epc1292OVPIndex"),
)
if mibBuilder.loadTexts:
    epc1292OVPEntry.setStatus("current")


class _Epc1292OVPIndex_Type(Integer32):
    """Custom type epc1292OVPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1292OVPIndex_Type.__name__ = "Integer32"
_Epc1292OVPIndex_Object = MibTableColumn
epc1292OVPIndex = _Epc1292OVPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 2, 1, 1),
    _Epc1292OVPIndex_Type()
)
epc1292OVPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292OVPIndex.setStatus("current")


class _Epc1292OVPStatus_Type(Integer32):
    """Custom type epc1292OVPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 0),
          ("ok", 1),
          ("unknown", 2))
    )


_Epc1292OVPStatus_Type.__name__ = "Integer32"
_Epc1292OVPStatus_Object = MibTableColumn
epc1292OVPStatus = _Epc1292OVPStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 5, 2, 1, 2),
    _Epc1292OVPStatus_Type()
)
epc1292OVPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292OVPStatus.setStatus("current")
_Epc1292ExtSensors_ObjectIdentity = ObjectIdentity
epc1292ExtSensors = _Epc1292ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 6)
)
_Epc1292SensorTable_Object = MibTable
epc1292SensorTable = _Epc1292SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 6, 1)
)
if mibBuilder.loadTexts:
    epc1292SensorTable.setStatus("current")
_Epc1292SensorEntry_Object = MibTableRow
epc1292SensorEntry = _Epc1292SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 6, 1, 1)
)
epc1292SensorEntry.setIndexNames(
    (0, "GUDEADS-EPC1292-MIB", "epc1292SensorIndex"),
)
if mibBuilder.loadTexts:
    epc1292SensorEntry.setStatus("current")


class _Epc1292SensorIndex_Type(Integer32):
    """Custom type epc1292SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1292SensorIndex_Type.__name__ = "Integer32"
_Epc1292SensorIndex_Object = MibTableColumn
epc1292SensorIndex = _Epc1292SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 6, 1, 1, 1),
    _Epc1292SensorIndex_Type()
)
epc1292SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292SensorIndex.setStatus("current")
_Epc1292TempSensor_Type = Integer32
_Epc1292TempSensor_Object = MibTableColumn
epc1292TempSensor = _Epc1292TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 6, 1, 1, 2),
    _Epc1292TempSensor_Type()
)
epc1292TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc1292TempSensor.setUnits("0.1 degree Celsius")
_Epc1292HygroSensor_Type = Integer32
_Epc1292HygroSensor_Object = MibTableColumn
epc1292HygroSensor = _Epc1292HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 6, 1, 1, 3),
    _Epc1292HygroSensor_Type()
)
epc1292HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc1292HygroSensor.setUnits("0.1 percent humidity")


class _Epc1292InputSensor_Type(Integer32):
    """Custom type epc1292InputSensor based on Integer32"""
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


_Epc1292InputSensor_Type.__name__ = "Integer32"
_Epc1292InputSensor_Object = MibTableColumn
epc1292InputSensor = _Epc1292InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 6, 1, 1, 4),
    _Epc1292InputSensor_Type()
)
epc1292InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292InputSensor.setStatus("current")
_Epc1292AirPressure_Type = Integer32
_Epc1292AirPressure_Object = MibTableColumn
epc1292AirPressure = _Epc1292AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 6, 1, 1, 5),
    _Epc1292AirPressure_Type()
)
epc1292AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    epc1292AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Epc1292DewPoint_Type = Integer32
_Epc1292DewPoint_Object = MibTableColumn
epc1292DewPoint = _Epc1292DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 6, 1, 1, 6),
    _Epc1292DewPoint_Type()
)
epc1292DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    epc1292DewPoint.setUnits("0.1 degree Celsius")
_Epc1292DewPointDiff_Type = Integer32
_Epc1292DewPointDiff_Object = MibTableColumn
epc1292DewPointDiff = _Epc1292DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 50, 1, 6, 1, 1, 7),
    _Epc1292DewPointDiff_Type()
)
epc1292DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1292DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    epc1292DewPointDiff.setUnits("0.1 degree Celsius")
_Epc1292Conf_ObjectIdentity = ObjectIdentity
epc1292Conf = _Epc1292Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 2)
)
_Epc1292Groups_ObjectIdentity = ObjectIdentity
epc1292Groups = _Epc1292Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 2, 1)
)
_Epc1292Compls_ObjectIdentity = ObjectIdentity
epc1292Compls = _Epc1292Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 50, 3)
)

# Managed Objects groups

epc1292BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 50, 2, 1, 1)
)
epc1292BasicGroup.setObjects(
      *(("GUDEADS-EPC1292-MIB", "epc1292TrapCtrl"),
        ("GUDEADS-EPC1292-MIB", "epc1292TrapIPIndex"),
        ("GUDEADS-EPC1292-MIB", "epc1292TrapAddr"),
        ("GUDEADS-EPC1292-MIB", "epc1292portNumber"),
        ("GUDEADS-EPC1292-MIB", "epc1292PortIndex"),
        ("GUDEADS-EPC1292-MIB", "epc1292PortName"),
        ("GUDEADS-EPC1292-MIB", "epc1292PortState"),
        ("GUDEADS-EPC1292-MIB", "epc1292PortSwitchCount"),
        ("GUDEADS-EPC1292-MIB", "epc1292PortStartupMode"),
        ("GUDEADS-EPC1292-MIB", "epc1292PortStartupDelay"),
        ("GUDEADS-EPC1292-MIB", "epc1292PortRepowerTime"),
        ("GUDEADS-EPC1292-MIB", "epc1292ActivePowerChan"),
        ("GUDEADS-EPC1292-MIB", "epc1292PowerIndex"),
        ("GUDEADS-EPC1292-MIB", "epc1292ChanStatus"),
        ("GUDEADS-EPC1292-MIB", "epc1292AbsEnergyActive"),
        ("GUDEADS-EPC1292-MIB", "epc1292PowerActive"),
        ("GUDEADS-EPC1292-MIB", "epc1292Current"),
        ("GUDEADS-EPC1292-MIB", "epc1292Voltage"),
        ("GUDEADS-EPC1292-MIB", "epc1292Frequency"),
        ("GUDEADS-EPC1292-MIB", "epc1292PowerFactor"),
        ("GUDEADS-EPC1292-MIB", "epc1292Pangle"),
        ("GUDEADS-EPC1292-MIB", "epc1292PowerApparent"),
        ("GUDEADS-EPC1292-MIB", "epc1292PowerReactive"),
        ("GUDEADS-EPC1292-MIB", "epc1292AbsEnergyReactive"),
        ("GUDEADS-EPC1292-MIB", "epc1292AbsEnergyActiveResettable"),
        ("GUDEADS-EPC1292-MIB", "epc1292AbsEnergyReactiveResettable"),
        ("GUDEADS-EPC1292-MIB", "epc1292ResetTime"),
        ("GUDEADS-EPC1292-MIB", "epc1292ForwEnergyActive"),
        ("GUDEADS-EPC1292-MIB", "epc1292ForwEnergyReactive"),
        ("GUDEADS-EPC1292-MIB", "epc1292ForwEnergyActiveResettable"),
        ("GUDEADS-EPC1292-MIB", "epc1292ForwEnergyReactiveResettable"),
        ("GUDEADS-EPC1292-MIB", "epc1292RevEnergyActive"),
        ("GUDEADS-EPC1292-MIB", "epc1292RevEnergyReactive"),
        ("GUDEADS-EPC1292-MIB", "epc1292RevEnergyActiveResettable"),
        ("GUDEADS-EPC1292-MIB", "epc1292RevEnergyReactiveResettable"),
        ("GUDEADS-EPC1292-MIB", "epc1292OVPIndex"),
        ("GUDEADS-EPC1292-MIB", "epc1292OVPStatus"),
        ("GUDEADS-EPC1292-MIB", "epc1292SensorIndex"),
        ("GUDEADS-EPC1292-MIB", "epc1292TempSensor"),
        ("GUDEADS-EPC1292-MIB", "epc1292HygroSensor"),
        ("GUDEADS-EPC1292-MIB", "epc1292InputSensor"),
        ("GUDEADS-EPC1292-MIB", "epc1292AirPressure"),
        ("GUDEADS-EPC1292-MIB", "epc1292DewPoint"),
        ("GUDEADS-EPC1292-MIB", "epc1292DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc1292BasicGroup.setStatus("current")


# Notification objects

epc1292SwitchEvtPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 50, 3, 1)
)
epc1292SwitchEvtPort.setObjects(
      *(("GUDEADS-EPC1292-MIB", "epc1292PortIndex"),
        ("GUDEADS-EPC1292-MIB", "epc1292PortName"),
        ("GUDEADS-EPC1292-MIB", "epc1292PortState"),
        ("GUDEADS-EPC1292-MIB", "epc1292PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc1292SwitchEvtPort.setStatus(
        "current"
    )

epc1292TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 50, 3, 2)
)
epc1292TempEvtSen.setObjects(
      *(("GUDEADS-EPC1292-MIB", "epc1292SensorIndex"),
        ("GUDEADS-EPC1292-MIB", "epc1292TempSensor"))
)
if mibBuilder.loadTexts:
    epc1292TempEvtSen.setStatus(
        "current"
    )

epc1292HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 50, 3, 3)
)
epc1292HygroEvtSen.setObjects(
      *(("GUDEADS-EPC1292-MIB", "epc1292SensorIndex"),
        ("GUDEADS-EPC1292-MIB", "epc1292HygroSensor"))
)
if mibBuilder.loadTexts:
    epc1292HygroEvtSen.setStatus(
        "current"
    )

epc1292InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 50, 3, 4)
)
epc1292InputEvtSen.setObjects(
      *(("GUDEADS-EPC1292-MIB", "epc1292SensorIndex"),
        ("GUDEADS-EPC1292-MIB", "epc1292InputSensor"))
)
if mibBuilder.loadTexts:
    epc1292InputEvtSen.setStatus(
        "current"
    )

epc1292AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 50, 3, 5)
)
epc1292AirPressureEvtSen.setObjects(
      *(("GUDEADS-EPC1292-MIB", "epc1292SensorIndex"),
        ("GUDEADS-EPC1292-MIB", "epc1292AirPressure"))
)
if mibBuilder.loadTexts:
    epc1292AirPressureEvtSen.setStatus(
        "current"
    )

epc1292DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 50, 3, 6)
)
epc1292DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-EPC1292-MIB", "epc1292SensorIndex"),
        ("GUDEADS-EPC1292-MIB", "epc1292DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc1292DewPtDiffEvtSen.setStatus(
        "current"
    )

epc1292OVPEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 50, 3, 7)
)
epc1292OVPEvt.setObjects(
    ("GUDEADS-EPC1292-MIB", "epc1292OVPStatus")
)
if mibBuilder.loadTexts:
    epc1292OVPEvt.setStatus(
        "current"
    )

epc1292LineAmperageEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 50, 3, 8)
)
epc1292LineAmperageEvt.setObjects(
      *(("GUDEADS-EPC1292-MIB", "epc1292PowerIndex"),
        ("GUDEADS-EPC1292-MIB", "epc1292PowerActive"),
        ("GUDEADS-EPC1292-MIB", "epc1292Current"),
        ("GUDEADS-EPC1292-MIB", "epc1292Voltage"),
        ("GUDEADS-EPC1292-MIB", "epc1292Frequency"),
        ("GUDEADS-EPC1292-MIB", "epc1292PowerApparent"),
        ("GUDEADS-EPC1292-MIB", "epc1292PowerReactive"))
)
if mibBuilder.loadTexts:
    epc1292LineAmperageEvt.setStatus(
        "current"
    )


# Notifications groups

epc1292NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 50, 2, 1, 2)
)
epc1292NotificationGroup.setObjects(
      *(("GUDEADS-EPC1292-MIB", "epc1292SwitchEvtPort"),
        ("GUDEADS-EPC1292-MIB", "epc1292TempEvtSen"),
        ("GUDEADS-EPC1292-MIB", "epc1292InputEvtSen"),
        ("GUDEADS-EPC1292-MIB", "epc1292AirPressureEvtSen"),
        ("GUDEADS-EPC1292-MIB", "epc1292DewPtDiffEvtSen"),
        ("GUDEADS-EPC1292-MIB", "epc1292OVPEvt"),
        ("GUDEADS-EPC1292-MIB", "epc1292LineAmperageEvt"),
        ("GUDEADS-EPC1292-MIB", "epc1292HygroEvtSen"))
)
if mibBuilder.loadTexts:
    epc1292NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-EPC1292-MIB",
    **{"gudeads": gudeads,
       "gadsEPC1292": gadsEPC1292,
       "epc1292Objects": epc1292Objects,
       "epc1292CommonConfig": epc1292CommonConfig,
       "epc1292SNMPaccess": epc1292SNMPaccess,
       "epc1292TrapCtrl": epc1292TrapCtrl,
       "epc1292TrapIPTable": epc1292TrapIPTable,
       "epc1292TrapIPEntry": epc1292TrapIPEntry,
       "epc1292TrapIPIndex": epc1292TrapIPIndex,
       "epc1292TrapAddr": epc1292TrapAddr,
       "epc1292DeviceConfig": epc1292DeviceConfig,
       "epc1292IntActors": epc1292IntActors,
       "epc1292relayports": epc1292relayports,
       "epc1292portNumber": epc1292portNumber,
       "epc1292portTable": epc1292portTable,
       "epc1292portEntry": epc1292portEntry,
       "epc1292PortIndex": epc1292PortIndex,
       "epc1292PortName": epc1292PortName,
       "epc1292PortState": epc1292PortState,
       "epc1292PortSwitchCount": epc1292PortSwitchCount,
       "epc1292PortStartupMode": epc1292PortStartupMode,
       "epc1292PortStartupDelay": epc1292PortStartupDelay,
       "epc1292PortRepowerTime": epc1292PortRepowerTime,
       "epc1292ExtActors": epc1292ExtActors,
       "epc1292IntSensors": epc1292IntSensors,
       "epc1292PowerChan": epc1292PowerChan,
       "epc1292ActivePowerChan": epc1292ActivePowerChan,
       "epc1292PowerTable": epc1292PowerTable,
       "epc1292PowerEntry": epc1292PowerEntry,
       "epc1292PowerIndex": epc1292PowerIndex,
       "epc1292ChanStatus": epc1292ChanStatus,
       "epc1292AbsEnergyActive": epc1292AbsEnergyActive,
       "epc1292PowerActive": epc1292PowerActive,
       "epc1292Current": epc1292Current,
       "epc1292Voltage": epc1292Voltage,
       "epc1292Frequency": epc1292Frequency,
       "epc1292PowerFactor": epc1292PowerFactor,
       "epc1292Pangle": epc1292Pangle,
       "epc1292PowerApparent": epc1292PowerApparent,
       "epc1292PowerReactive": epc1292PowerReactive,
       "epc1292AbsEnergyReactive": epc1292AbsEnergyReactive,
       "epc1292AbsEnergyActiveResettable": epc1292AbsEnergyActiveResettable,
       "epc1292AbsEnergyReactiveResettable": epc1292AbsEnergyReactiveResettable,
       "epc1292ResetTime": epc1292ResetTime,
       "epc1292ForwEnergyActive": epc1292ForwEnergyActive,
       "epc1292ForwEnergyReactive": epc1292ForwEnergyReactive,
       "epc1292ForwEnergyActiveResettable": epc1292ForwEnergyActiveResettable,
       "epc1292ForwEnergyReactiveResettable": epc1292ForwEnergyReactiveResettable,
       "epc1292RevEnergyActive": epc1292RevEnergyActive,
       "epc1292RevEnergyReactive": epc1292RevEnergyReactive,
       "epc1292RevEnergyActiveResettable": epc1292RevEnergyActiveResettable,
       "epc1292RevEnergyReactiveResettable": epc1292RevEnergyReactiveResettable,
       "epc1292OVPTable": epc1292OVPTable,
       "epc1292OVPEntry": epc1292OVPEntry,
       "epc1292OVPIndex": epc1292OVPIndex,
       "epc1292OVPStatus": epc1292OVPStatus,
       "epc1292ExtSensors": epc1292ExtSensors,
       "epc1292SensorTable": epc1292SensorTable,
       "epc1292SensorEntry": epc1292SensorEntry,
       "epc1292SensorIndex": epc1292SensorIndex,
       "epc1292TempSensor": epc1292TempSensor,
       "epc1292HygroSensor": epc1292HygroSensor,
       "epc1292InputSensor": epc1292InputSensor,
       "epc1292AirPressure": epc1292AirPressure,
       "epc1292DewPoint": epc1292DewPoint,
       "epc1292DewPointDiff": epc1292DewPointDiff,
       "epc1292Conf": epc1292Conf,
       "epc1292Groups": epc1292Groups,
       "epc1292BasicGroup": epc1292BasicGroup,
       "epc1292NotificationGroup": epc1292NotificationGroup,
       "epc1292Compls": epc1292Compls,
       "events": events,
       "epc1292SwitchEvtPort": epc1292SwitchEvtPort,
       "epc1292TempEvtSen": epc1292TempEvtSen,
       "epc1292HygroEvtSen": epc1292HygroEvtSen,
       "epc1292InputEvtSen": epc1292InputEvtSen,
       "epc1292AirPressureEvtSen": epc1292AirPressureEvtSen,
       "epc1292DewPtDiffEvtSen": epc1292DewPtDiffEvtSen,
       "epc1292OVPEvt": epc1292OVPEvt,
       "epc1292LineAmperageEvt": epc1292LineAmperageEvt}
)
