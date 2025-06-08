# SNMP MIB module (GUDEADS-EPC1202-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-EPC1202-MIB.mib
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

_GadsEPC1202_ObjectIdentity = ObjectIdentity
gadsEPC1202 = _GadsEPC1202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43)
)
_Epc1202Objects_ObjectIdentity = ObjectIdentity
epc1202Objects = _Epc1202Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1)
)
_Epc1202CommonConfig_ObjectIdentity = ObjectIdentity
epc1202CommonConfig = _Epc1202CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 1)
)
_Epc1202SNMPaccess_ObjectIdentity = ObjectIdentity
epc1202SNMPaccess = _Epc1202SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 1, 1)
)


class _Epc1202TrapCtrl_Type(Integer32):
    """Custom type epc1202TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Epc1202TrapCtrl_Type.__name__ = "Integer32"
_Epc1202TrapCtrl_Object = MibScalar
epc1202TrapCtrl = _Epc1202TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 1, 1, 1),
    _Epc1202TrapCtrl_Type()
)
epc1202TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1202TrapCtrl.setStatus("current")
_Epc1202TrapIPTable_Object = MibTable
epc1202TrapIPTable = _Epc1202TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    epc1202TrapIPTable.setStatus("current")
_Epc1202TrapIPEntry_Object = MibTableRow
epc1202TrapIPEntry = _Epc1202TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 1, 1, 2, 1)
)
epc1202TrapIPEntry.setIndexNames(
    (0, "GUDEADS-EPC1202-MIB", "epc1202TrapIPIndex"),
)
if mibBuilder.loadTexts:
    epc1202TrapIPEntry.setStatus("current")


class _Epc1202TrapIPIndex_Type(Integer32):
    """Custom type epc1202TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc1202TrapIPIndex_Type.__name__ = "Integer32"
_Epc1202TrapIPIndex_Object = MibTableColumn
epc1202TrapIPIndex = _Epc1202TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 1, 1, 2, 1, 1),
    _Epc1202TrapIPIndex_Type()
)
epc1202TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202TrapIPIndex.setStatus("current")


class _Epc1202TrapAddr_Type(OctetString):
    """Custom type epc1202TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Epc1202TrapAddr_Type.__name__ = "OctetString"
_Epc1202TrapAddr_Object = MibTableColumn
epc1202TrapAddr = _Epc1202TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 1, 1, 2, 1, 2),
    _Epc1202TrapAddr_Type()
)
epc1202TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1202TrapAddr.setStatus("current")
_Epc1202DeviceConfig_ObjectIdentity = ObjectIdentity
epc1202DeviceConfig = _Epc1202DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 2)
)
_Epc1202IntActors_ObjectIdentity = ObjectIdentity
epc1202IntActors = _Epc1202IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 3)
)
_Epc1202relayports_ObjectIdentity = ObjectIdentity
epc1202relayports = _Epc1202relayports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 3, 1)
)


class _Epc1202portNumber_Type(Integer32):
    """Custom type epc1202portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Epc1202portNumber_Type.__name__ = "Integer32"
_Epc1202portNumber_Object = MibScalar
epc1202portNumber = _Epc1202portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 3, 1, 1),
    _Epc1202portNumber_Type()
)
epc1202portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202portNumber.setStatus("current")
_Epc1202portTable_Object = MibTable
epc1202portTable = _Epc1202portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    epc1202portTable.setStatus("current")
_Epc1202portEntry_Object = MibTableRow
epc1202portEntry = _Epc1202portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 3, 1, 2, 1)
)
epc1202portEntry.setIndexNames(
    (0, "GUDEADS-EPC1202-MIB", "epc1202PortIndex"),
)
if mibBuilder.loadTexts:
    epc1202portEntry.setStatus("current")


class _Epc1202PortIndex_Type(Integer32):
    """Custom type epc1202PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Epc1202PortIndex_Type.__name__ = "Integer32"
_Epc1202PortIndex_Object = MibTableColumn
epc1202PortIndex = _Epc1202PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 3, 1, 2, 1, 1),
    _Epc1202PortIndex_Type()
)
epc1202PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202PortIndex.setStatus("current")


class _Epc1202PortName_Type(OctetString):
    """Custom type epc1202PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Epc1202PortName_Type.__name__ = "OctetString"
_Epc1202PortName_Object = MibTableColumn
epc1202PortName = _Epc1202PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 3, 1, 2, 1, 2),
    _Epc1202PortName_Type()
)
epc1202PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1202PortName.setStatus("current")


class _Epc1202PortState_Type(Integer32):
    """Custom type epc1202PortState based on Integer32"""
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


_Epc1202PortState_Type.__name__ = "Integer32"
_Epc1202PortState_Object = MibTableColumn
epc1202PortState = _Epc1202PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 3, 1, 2, 1, 3),
    _Epc1202PortState_Type()
)
epc1202PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1202PortState.setStatus("current")
_Epc1202PortSwitchCount_Type = Integer32
_Epc1202PortSwitchCount_Object = MibTableColumn
epc1202PortSwitchCount = _Epc1202PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 3, 1, 2, 1, 4),
    _Epc1202PortSwitchCount_Type()
)
epc1202PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202PortSwitchCount.setStatus("current")


class _Epc1202PortStartupMode_Type(Integer32):
    """Custom type epc1202PortStartupMode based on Integer32"""
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


_Epc1202PortStartupMode_Type.__name__ = "Integer32"
_Epc1202PortStartupMode_Object = MibTableColumn
epc1202PortStartupMode = _Epc1202PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 3, 1, 2, 1, 5),
    _Epc1202PortStartupMode_Type()
)
epc1202PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1202PortStartupMode.setStatus("current")


class _Epc1202PortStartupDelay_Type(Integer32):
    """Custom type epc1202PortStartupDelay based on Integer32"""
    defaultValue = 0


_Epc1202PortStartupDelay_Type.__name__ = "Integer32"
_Epc1202PortStartupDelay_Object = MibTableColumn
epc1202PortStartupDelay = _Epc1202PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 3, 1, 2, 1, 6),
    _Epc1202PortStartupDelay_Type()
)
epc1202PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1202PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    epc1202PortStartupDelay.setUnits("seconds")


class _Epc1202PortRepowerTime_Type(Integer32):
    """Custom type epc1202PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Epc1202PortRepowerTime_Type.__name__ = "Integer32"
_Epc1202PortRepowerTime_Object = MibTableColumn
epc1202PortRepowerTime = _Epc1202PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 3, 1, 2, 1, 7),
    _Epc1202PortRepowerTime_Type()
)
epc1202PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1202PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    epc1202PortRepowerTime.setUnits("seconds")
_Epc1202ExtActors_ObjectIdentity = ObjectIdentity
epc1202ExtActors = _Epc1202ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 4)
)
_Epc1202IntSensors_ObjectIdentity = ObjectIdentity
epc1202IntSensors = _Epc1202IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5)
)
_Epc1202PowerChan_ObjectIdentity = ObjectIdentity
epc1202PowerChan = _Epc1202PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1)
)


class _Epc1202ActivePowerChan_Type(Unsigned32):
    """Custom type epc1202ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1202ActivePowerChan_Type.__name__ = "Unsigned32"
_Epc1202ActivePowerChan_Object = MibScalar
epc1202ActivePowerChan = _Epc1202ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 1),
    _Epc1202ActivePowerChan_Type()
)
epc1202ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202ActivePowerChan.setStatus("current")
_Epc1202PowerTable_Object = MibTable
epc1202PowerTable = _Epc1202PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    epc1202PowerTable.setStatus("current")
_Epc1202PowerEntry_Object = MibTableRow
epc1202PowerEntry = _Epc1202PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1)
)
epc1202PowerEntry.setIndexNames(
    (0, "GUDEADS-EPC1202-MIB", "epc1202PowerIndex"),
)
if mibBuilder.loadTexts:
    epc1202PowerEntry.setStatus("current")


class _Epc1202PowerIndex_Type(Integer32):
    """Custom type epc1202PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1202PowerIndex_Type.__name__ = "Integer32"
_Epc1202PowerIndex_Object = MibTableColumn
epc1202PowerIndex = _Epc1202PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 1),
    _Epc1202PowerIndex_Type()
)
epc1202PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202PowerIndex.setStatus("current")


class _Epc1202ChanStatus_Type(Integer32):
    """Custom type epc1202ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc1202ChanStatus_Type.__name__ = "Integer32"
_Epc1202ChanStatus_Object = MibTableColumn
epc1202ChanStatus = _Epc1202ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 2),
    _Epc1202ChanStatus_Type()
)
epc1202ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202ChanStatus.setStatus("current")
_Epc1202AbsEnergyActive_Type = Gauge32
_Epc1202AbsEnergyActive_Object = MibTableColumn
epc1202AbsEnergyActive = _Epc1202AbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 3),
    _Epc1202AbsEnergyActive_Type()
)
epc1202AbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202AbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc1202AbsEnergyActive.setUnits("Wh")
_Epc1202PowerActive_Type = Integer32
_Epc1202PowerActive_Object = MibTableColumn
epc1202PowerActive = _Epc1202PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 4),
    _Epc1202PowerActive_Type()
)
epc1202PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    epc1202PowerActive.setUnits("W")
_Epc1202Current_Type = Gauge32
_Epc1202Current_Object = MibTableColumn
epc1202Current = _Epc1202Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 5),
    _Epc1202Current_Type()
)
epc1202Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202Current.setStatus("current")
if mibBuilder.loadTexts:
    epc1202Current.setUnits("mA")
_Epc1202Voltage_Type = Gauge32
_Epc1202Voltage_Object = MibTableColumn
epc1202Voltage = _Epc1202Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 6),
    _Epc1202Voltage_Type()
)
epc1202Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202Voltage.setStatus("current")
if mibBuilder.loadTexts:
    epc1202Voltage.setUnits("V")
_Epc1202Frequency_Type = Gauge32
_Epc1202Frequency_Object = MibTableColumn
epc1202Frequency = _Epc1202Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 7),
    _Epc1202Frequency_Type()
)
epc1202Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202Frequency.setStatus("current")
if mibBuilder.loadTexts:
    epc1202Frequency.setUnits("0.01 hz")
_Epc1202PowerFactor_Type = Integer32
_Epc1202PowerFactor_Object = MibTableColumn
epc1202PowerFactor = _Epc1202PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 8),
    _Epc1202PowerFactor_Type()
)
epc1202PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    epc1202PowerFactor.setUnits("0.001")
_Epc1202Pangle_Type = Integer32
_Epc1202Pangle_Object = MibTableColumn
epc1202Pangle = _Epc1202Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 9),
    _Epc1202Pangle_Type()
)
epc1202Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202Pangle.setStatus("current")
if mibBuilder.loadTexts:
    epc1202Pangle.setUnits("0.1 degree")
_Epc1202PowerApparent_Type = Integer32
_Epc1202PowerApparent_Object = MibTableColumn
epc1202PowerApparent = _Epc1202PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 10),
    _Epc1202PowerApparent_Type()
)
epc1202PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    epc1202PowerApparent.setUnits("VA")
_Epc1202PowerReactive_Type = Integer32
_Epc1202PowerReactive_Object = MibTableColumn
epc1202PowerReactive = _Epc1202PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 11),
    _Epc1202PowerReactive_Type()
)
epc1202PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc1202PowerReactive.setUnits("VAR")
_Epc1202AbsEnergyReactive_Type = Gauge32
_Epc1202AbsEnergyReactive_Object = MibTableColumn
epc1202AbsEnergyReactive = _Epc1202AbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 12),
    _Epc1202AbsEnergyReactive_Type()
)
epc1202AbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202AbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc1202AbsEnergyReactive.setUnits("VARh")
_Epc1202AbsEnergyActiveResettable_Type = Gauge32
_Epc1202AbsEnergyActiveResettable_Object = MibTableColumn
epc1202AbsEnergyActiveResettable = _Epc1202AbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 13),
    _Epc1202AbsEnergyActiveResettable_Type()
)
epc1202AbsEnergyActiveResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc1202AbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1202AbsEnergyActiveResettable.setUnits("Wh")
_Epc1202AbsEnergyReactiveResettable_Type = Gauge32
_Epc1202AbsEnergyReactiveResettable_Object = MibTableColumn
epc1202AbsEnergyReactiveResettable = _Epc1202AbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 14),
    _Epc1202AbsEnergyReactiveResettable_Type()
)
epc1202AbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202AbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1202AbsEnergyReactiveResettable.setUnits("VARh")
_Epc1202ResetTime_Type = Gauge32
_Epc1202ResetTime_Object = MibTableColumn
epc1202ResetTime = _Epc1202ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 15),
    _Epc1202ResetTime_Type()
)
epc1202ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    epc1202ResetTime.setUnits("s")
_Epc1202ForwEnergyActive_Type = Gauge32
_Epc1202ForwEnergyActive_Object = MibTableColumn
epc1202ForwEnergyActive = _Epc1202ForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 16),
    _Epc1202ForwEnergyActive_Type()
)
epc1202ForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202ForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc1202ForwEnergyActive.setUnits("Wh")
_Epc1202ForwEnergyReactive_Type = Gauge32
_Epc1202ForwEnergyReactive_Object = MibTableColumn
epc1202ForwEnergyReactive = _Epc1202ForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 17),
    _Epc1202ForwEnergyReactive_Type()
)
epc1202ForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202ForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc1202ForwEnergyReactive.setUnits("VARh")
_Epc1202ForwEnergyActiveResettable_Type = Gauge32
_Epc1202ForwEnergyActiveResettable_Object = MibTableColumn
epc1202ForwEnergyActiveResettable = _Epc1202ForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 18),
    _Epc1202ForwEnergyActiveResettable_Type()
)
epc1202ForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202ForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1202ForwEnergyActiveResettable.setUnits("Wh")
_Epc1202ForwEnergyReactiveResettable_Type = Gauge32
_Epc1202ForwEnergyReactiveResettable_Object = MibTableColumn
epc1202ForwEnergyReactiveResettable = _Epc1202ForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 19),
    _Epc1202ForwEnergyReactiveResettable_Type()
)
epc1202ForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202ForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1202ForwEnergyReactiveResettable.setUnits("VARh")
_Epc1202RevEnergyActive_Type = Gauge32
_Epc1202RevEnergyActive_Object = MibTableColumn
epc1202RevEnergyActive = _Epc1202RevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 20),
    _Epc1202RevEnergyActive_Type()
)
epc1202RevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202RevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc1202RevEnergyActive.setUnits("Wh")
_Epc1202RevEnergyReactive_Type = Gauge32
_Epc1202RevEnergyReactive_Object = MibTableColumn
epc1202RevEnergyReactive = _Epc1202RevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 21),
    _Epc1202RevEnergyReactive_Type()
)
epc1202RevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202RevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc1202RevEnergyReactive.setUnits("VARh")
_Epc1202RevEnergyActiveResettable_Type = Gauge32
_Epc1202RevEnergyActiveResettable_Object = MibTableColumn
epc1202RevEnergyActiveResettable = _Epc1202RevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 22),
    _Epc1202RevEnergyActiveResettable_Type()
)
epc1202RevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202RevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1202RevEnergyActiveResettable.setUnits("Wh")
_Epc1202RevEnergyReactiveResettable_Type = Gauge32
_Epc1202RevEnergyReactiveResettable_Object = MibTableColumn
epc1202RevEnergyReactiveResettable = _Epc1202RevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 1, 2, 1, 23),
    _Epc1202RevEnergyReactiveResettable_Type()
)
epc1202RevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202RevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc1202RevEnergyReactiveResettable.setUnits("VARh")
_Epc1202OVPTable_Object = MibTable
epc1202OVPTable = _Epc1202OVPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 2)
)
if mibBuilder.loadTexts:
    epc1202OVPTable.setStatus("current")
_Epc1202OVPEntry_Object = MibTableRow
epc1202OVPEntry = _Epc1202OVPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 2, 1)
)
epc1202OVPEntry.setIndexNames(
    (0, "GUDEADS-EPC1202-MIB", "epc1202OVPIndex"),
)
if mibBuilder.loadTexts:
    epc1202OVPEntry.setStatus("current")


class _Epc1202OVPIndex_Type(Integer32):
    """Custom type epc1202OVPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1202OVPIndex_Type.__name__ = "Integer32"
_Epc1202OVPIndex_Object = MibTableColumn
epc1202OVPIndex = _Epc1202OVPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 2, 1, 1),
    _Epc1202OVPIndex_Type()
)
epc1202OVPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202OVPIndex.setStatus("current")


class _Epc1202OVPStatus_Type(Integer32):
    """Custom type epc1202OVPStatus based on Integer32"""
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


_Epc1202OVPStatus_Type.__name__ = "Integer32"
_Epc1202OVPStatus_Object = MibTableColumn
epc1202OVPStatus = _Epc1202OVPStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 5, 2, 1, 2),
    _Epc1202OVPStatus_Type()
)
epc1202OVPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202OVPStatus.setStatus("current")
_Epc1202ExtSensors_ObjectIdentity = ObjectIdentity
epc1202ExtSensors = _Epc1202ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 6)
)
_Epc1202SensorTable_Object = MibTable
epc1202SensorTable = _Epc1202SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 6, 1)
)
if mibBuilder.loadTexts:
    epc1202SensorTable.setStatus("current")
_Epc1202SensorEntry_Object = MibTableRow
epc1202SensorEntry = _Epc1202SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 6, 1, 1)
)
epc1202SensorEntry.setIndexNames(
    (0, "GUDEADS-EPC1202-MIB", "epc1202SensorIndex"),
)
if mibBuilder.loadTexts:
    epc1202SensorEntry.setStatus("current")


class _Epc1202SensorIndex_Type(Integer32):
    """Custom type epc1202SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc1202SensorIndex_Type.__name__ = "Integer32"
_Epc1202SensorIndex_Object = MibTableColumn
epc1202SensorIndex = _Epc1202SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 6, 1, 1, 1),
    _Epc1202SensorIndex_Type()
)
epc1202SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202SensorIndex.setStatus("current")
_Epc1202TempSensor_Type = Integer32
_Epc1202TempSensor_Object = MibTableColumn
epc1202TempSensor = _Epc1202TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 6, 1, 1, 2),
    _Epc1202TempSensor_Type()
)
epc1202TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc1202TempSensor.setUnits("0.1 degree Celsius")
_Epc1202HygroSensor_Type = Integer32
_Epc1202HygroSensor_Object = MibTableColumn
epc1202HygroSensor = _Epc1202HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 6, 1, 1, 3),
    _Epc1202HygroSensor_Type()
)
epc1202HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc1202HygroSensor.setUnits("0.1 percent humidity")


class _Epc1202InputSensor_Type(Integer32):
    """Custom type epc1202InputSensor based on Integer32"""
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


_Epc1202InputSensor_Type.__name__ = "Integer32"
_Epc1202InputSensor_Object = MibTableColumn
epc1202InputSensor = _Epc1202InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 6, 1, 1, 4),
    _Epc1202InputSensor_Type()
)
epc1202InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202InputSensor.setStatus("current")
_Epc1202AirPressure_Type = Integer32
_Epc1202AirPressure_Object = MibTableColumn
epc1202AirPressure = _Epc1202AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 6, 1, 1, 5),
    _Epc1202AirPressure_Type()
)
epc1202AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    epc1202AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Epc1202DewPoint_Type = Integer32
_Epc1202DewPoint_Object = MibTableColumn
epc1202DewPoint = _Epc1202DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 6, 1, 1, 6),
    _Epc1202DewPoint_Type()
)
epc1202DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    epc1202DewPoint.setUnits("0.1 degree Celsius")
_Epc1202DewPointDiff_Type = Integer32
_Epc1202DewPointDiff_Object = MibTableColumn
epc1202DewPointDiff = _Epc1202DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 43, 1, 6, 1, 1, 7),
    _Epc1202DewPointDiff_Type()
)
epc1202DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc1202DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    epc1202DewPointDiff.setUnits("0.1 degree Celsius")
_Epc1202Conf_ObjectIdentity = ObjectIdentity
epc1202Conf = _Epc1202Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 2)
)
_Epc1202Groups_ObjectIdentity = ObjectIdentity
epc1202Groups = _Epc1202Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 2, 1)
)
_Epc1202Compls_ObjectIdentity = ObjectIdentity
epc1202Compls = _Epc1202Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 43, 3)
)

# Managed Objects groups

epc1202BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 43, 2, 1, 1)
)
epc1202BasicGroup.setObjects(
      *(("GUDEADS-EPC1202-MIB", "epc1202TrapCtrl"),
        ("GUDEADS-EPC1202-MIB", "epc1202TrapIPIndex"),
        ("GUDEADS-EPC1202-MIB", "epc1202TrapAddr"),
        ("GUDEADS-EPC1202-MIB", "epc1202portNumber"),
        ("GUDEADS-EPC1202-MIB", "epc1202PortIndex"),
        ("GUDEADS-EPC1202-MIB", "epc1202PortName"),
        ("GUDEADS-EPC1202-MIB", "epc1202PortState"),
        ("GUDEADS-EPC1202-MIB", "epc1202PortSwitchCount"),
        ("GUDEADS-EPC1202-MIB", "epc1202PortStartupMode"),
        ("GUDEADS-EPC1202-MIB", "epc1202PortStartupDelay"),
        ("GUDEADS-EPC1202-MIB", "epc1202PortRepowerTime"),
        ("GUDEADS-EPC1202-MIB", "epc1202ActivePowerChan"),
        ("GUDEADS-EPC1202-MIB", "epc1202PowerIndex"),
        ("GUDEADS-EPC1202-MIB", "epc1202ChanStatus"),
        ("GUDEADS-EPC1202-MIB", "epc1202AbsEnergyActive"),
        ("GUDEADS-EPC1202-MIB", "epc1202PowerActive"),
        ("GUDEADS-EPC1202-MIB", "epc1202Current"),
        ("GUDEADS-EPC1202-MIB", "epc1202Voltage"),
        ("GUDEADS-EPC1202-MIB", "epc1202Frequency"),
        ("GUDEADS-EPC1202-MIB", "epc1202PowerFactor"),
        ("GUDEADS-EPC1202-MIB", "epc1202Pangle"),
        ("GUDEADS-EPC1202-MIB", "epc1202PowerApparent"),
        ("GUDEADS-EPC1202-MIB", "epc1202PowerReactive"),
        ("GUDEADS-EPC1202-MIB", "epc1202AbsEnergyReactive"),
        ("GUDEADS-EPC1202-MIB", "epc1202AbsEnergyActiveResettable"),
        ("GUDEADS-EPC1202-MIB", "epc1202AbsEnergyReactiveResettable"),
        ("GUDEADS-EPC1202-MIB", "epc1202ResetTime"),
        ("GUDEADS-EPC1202-MIB", "epc1202ForwEnergyActive"),
        ("GUDEADS-EPC1202-MIB", "epc1202ForwEnergyReactive"),
        ("GUDEADS-EPC1202-MIB", "epc1202ForwEnergyActiveResettable"),
        ("GUDEADS-EPC1202-MIB", "epc1202ForwEnergyReactiveResettable"),
        ("GUDEADS-EPC1202-MIB", "epc1202RevEnergyActive"),
        ("GUDEADS-EPC1202-MIB", "epc1202RevEnergyReactive"),
        ("GUDEADS-EPC1202-MIB", "epc1202RevEnergyActiveResettable"),
        ("GUDEADS-EPC1202-MIB", "epc1202RevEnergyReactiveResettable"),
        ("GUDEADS-EPC1202-MIB", "epc1202OVPIndex"),
        ("GUDEADS-EPC1202-MIB", "epc1202OVPStatus"),
        ("GUDEADS-EPC1202-MIB", "epc1202SensorIndex"),
        ("GUDEADS-EPC1202-MIB", "epc1202TempSensor"),
        ("GUDEADS-EPC1202-MIB", "epc1202HygroSensor"),
        ("GUDEADS-EPC1202-MIB", "epc1202InputSensor"),
        ("GUDEADS-EPC1202-MIB", "epc1202AirPressure"),
        ("GUDEADS-EPC1202-MIB", "epc1202DewPoint"),
        ("GUDEADS-EPC1202-MIB", "epc1202DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc1202BasicGroup.setStatus("current")


# Notification objects

epc1202SwitchEvtPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 43, 3, 1)
)
epc1202SwitchEvtPort.setObjects(
      *(("GUDEADS-EPC1202-MIB", "epc1202PortIndex"),
        ("GUDEADS-EPC1202-MIB", "epc1202PortName"),
        ("GUDEADS-EPC1202-MIB", "epc1202PortState"),
        ("GUDEADS-EPC1202-MIB", "epc1202PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc1202SwitchEvtPort.setStatus(
        "current"
    )

epc1202TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 43, 3, 2)
)
epc1202TempEvtSen.setObjects(
      *(("GUDEADS-EPC1202-MIB", "epc1202SensorIndex"),
        ("GUDEADS-EPC1202-MIB", "epc1202TempSensor"))
)
if mibBuilder.loadTexts:
    epc1202TempEvtSen.setStatus(
        "current"
    )

epc1202HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 43, 3, 3)
)
epc1202HygroEvtSen.setObjects(
      *(("GUDEADS-EPC1202-MIB", "epc1202SensorIndex"),
        ("GUDEADS-EPC1202-MIB", "epc1202HygroSensor"))
)
if mibBuilder.loadTexts:
    epc1202HygroEvtSen.setStatus(
        "current"
    )

epc1202InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 43, 3, 4)
)
epc1202InputEvtSen.setObjects(
      *(("GUDEADS-EPC1202-MIB", "epc1202SensorIndex"),
        ("GUDEADS-EPC1202-MIB", "epc1202InputSensor"))
)
if mibBuilder.loadTexts:
    epc1202InputEvtSen.setStatus(
        "current"
    )

epc1202AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 43, 3, 5)
)
epc1202AirPressureEvtSen.setObjects(
      *(("GUDEADS-EPC1202-MIB", "epc1202SensorIndex"),
        ("GUDEADS-EPC1202-MIB", "epc1202AirPressure"))
)
if mibBuilder.loadTexts:
    epc1202AirPressureEvtSen.setStatus(
        "current"
    )

epc1202DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 43, 3, 6)
)
epc1202DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-EPC1202-MIB", "epc1202SensorIndex"),
        ("GUDEADS-EPC1202-MIB", "epc1202DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc1202DewPtDiffEvtSen.setStatus(
        "current"
    )

epc1202OVPEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 43, 3, 7)
)
epc1202OVPEvt.setObjects(
    ("GUDEADS-EPC1202-MIB", "epc1202OVPStatus")
)
if mibBuilder.loadTexts:
    epc1202OVPEvt.setStatus(
        "current"
    )

epc1202LineAmperageEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 43, 3, 8)
)
epc1202LineAmperageEvt.setObjects(
      *(("GUDEADS-EPC1202-MIB", "epc1202PowerIndex"),
        ("GUDEADS-EPC1202-MIB", "epc1202PowerActive"),
        ("GUDEADS-EPC1202-MIB", "epc1202Current"),
        ("GUDEADS-EPC1202-MIB", "epc1202Voltage"),
        ("GUDEADS-EPC1202-MIB", "epc1202Frequency"),
        ("GUDEADS-EPC1202-MIB", "epc1202PowerApparent"),
        ("GUDEADS-EPC1202-MIB", "epc1202PowerReactive"))
)
if mibBuilder.loadTexts:
    epc1202LineAmperageEvt.setStatus(
        "current"
    )


# Notifications groups

epc1202NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 43, 2, 1, 2)
)
epc1202NotificationGroup.setObjects(
      *(("GUDEADS-EPC1202-MIB", "epc1202SwitchEvtPort"),
        ("GUDEADS-EPC1202-MIB", "epc1202TempEvtSen"),
        ("GUDEADS-EPC1202-MIB", "epc1202InputEvtSen"),
        ("GUDEADS-EPC1202-MIB", "epc1202AirPressureEvtSen"),
        ("GUDEADS-EPC1202-MIB", "epc1202DewPtDiffEvtSen"),
        ("GUDEADS-EPC1202-MIB", "epc1202OVPEvt"),
        ("GUDEADS-EPC1202-MIB", "epc1202LineAmperageEvt"),
        ("GUDEADS-EPC1202-MIB", "epc1202HygroEvtSen"))
)
if mibBuilder.loadTexts:
    epc1202NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-EPC1202-MIB",
    **{"gudeads": gudeads,
       "gadsEPC1202": gadsEPC1202,
       "epc1202Objects": epc1202Objects,
       "epc1202CommonConfig": epc1202CommonConfig,
       "epc1202SNMPaccess": epc1202SNMPaccess,
       "epc1202TrapCtrl": epc1202TrapCtrl,
       "epc1202TrapIPTable": epc1202TrapIPTable,
       "epc1202TrapIPEntry": epc1202TrapIPEntry,
       "epc1202TrapIPIndex": epc1202TrapIPIndex,
       "epc1202TrapAddr": epc1202TrapAddr,
       "epc1202DeviceConfig": epc1202DeviceConfig,
       "epc1202IntActors": epc1202IntActors,
       "epc1202relayports": epc1202relayports,
       "epc1202portNumber": epc1202portNumber,
       "epc1202portTable": epc1202portTable,
       "epc1202portEntry": epc1202portEntry,
       "epc1202PortIndex": epc1202PortIndex,
       "epc1202PortName": epc1202PortName,
       "epc1202PortState": epc1202PortState,
       "epc1202PortSwitchCount": epc1202PortSwitchCount,
       "epc1202PortStartupMode": epc1202PortStartupMode,
       "epc1202PortStartupDelay": epc1202PortStartupDelay,
       "epc1202PortRepowerTime": epc1202PortRepowerTime,
       "epc1202ExtActors": epc1202ExtActors,
       "epc1202IntSensors": epc1202IntSensors,
       "epc1202PowerChan": epc1202PowerChan,
       "epc1202ActivePowerChan": epc1202ActivePowerChan,
       "epc1202PowerTable": epc1202PowerTable,
       "epc1202PowerEntry": epc1202PowerEntry,
       "epc1202PowerIndex": epc1202PowerIndex,
       "epc1202ChanStatus": epc1202ChanStatus,
       "epc1202AbsEnergyActive": epc1202AbsEnergyActive,
       "epc1202PowerActive": epc1202PowerActive,
       "epc1202Current": epc1202Current,
       "epc1202Voltage": epc1202Voltage,
       "epc1202Frequency": epc1202Frequency,
       "epc1202PowerFactor": epc1202PowerFactor,
       "epc1202Pangle": epc1202Pangle,
       "epc1202PowerApparent": epc1202PowerApparent,
       "epc1202PowerReactive": epc1202PowerReactive,
       "epc1202AbsEnergyReactive": epc1202AbsEnergyReactive,
       "epc1202AbsEnergyActiveResettable": epc1202AbsEnergyActiveResettable,
       "epc1202AbsEnergyReactiveResettable": epc1202AbsEnergyReactiveResettable,
       "epc1202ResetTime": epc1202ResetTime,
       "epc1202ForwEnergyActive": epc1202ForwEnergyActive,
       "epc1202ForwEnergyReactive": epc1202ForwEnergyReactive,
       "epc1202ForwEnergyActiveResettable": epc1202ForwEnergyActiveResettable,
       "epc1202ForwEnergyReactiveResettable": epc1202ForwEnergyReactiveResettable,
       "epc1202RevEnergyActive": epc1202RevEnergyActive,
       "epc1202RevEnergyReactive": epc1202RevEnergyReactive,
       "epc1202RevEnergyActiveResettable": epc1202RevEnergyActiveResettable,
       "epc1202RevEnergyReactiveResettable": epc1202RevEnergyReactiveResettable,
       "epc1202OVPTable": epc1202OVPTable,
       "epc1202OVPEntry": epc1202OVPEntry,
       "epc1202OVPIndex": epc1202OVPIndex,
       "epc1202OVPStatus": epc1202OVPStatus,
       "epc1202ExtSensors": epc1202ExtSensors,
       "epc1202SensorTable": epc1202SensorTable,
       "epc1202SensorEntry": epc1202SensorEntry,
       "epc1202SensorIndex": epc1202SensorIndex,
       "epc1202TempSensor": epc1202TempSensor,
       "epc1202HygroSensor": epc1202HygroSensor,
       "epc1202InputSensor": epc1202InputSensor,
       "epc1202AirPressure": epc1202AirPressure,
       "epc1202DewPoint": epc1202DewPoint,
       "epc1202DewPointDiff": epc1202DewPointDiff,
       "epc1202Conf": epc1202Conf,
       "epc1202Groups": epc1202Groups,
       "epc1202BasicGroup": epc1202BasicGroup,
       "epc1202NotificationGroup": epc1202NotificationGroup,
       "epc1202Compls": epc1202Compls,
       "events": events,
       "epc1202SwitchEvtPort": epc1202SwitchEvtPort,
       "epc1202TempEvtSen": epc1202TempEvtSen,
       "epc1202HygroEvtSen": epc1202HygroEvtSen,
       "epc1202InputEvtSen": epc1202InputEvtSen,
       "epc1202AirPressureEvtSen": epc1202AirPressureEvtSen,
       "epc1202DewPtDiffEvtSen": epc1202DewPtDiffEvtSen,
       "epc1202OVPEvt": epc1202OVPEvt,
       "epc1202LineAmperageEvt": epc1202LineAmperageEvt}
)
