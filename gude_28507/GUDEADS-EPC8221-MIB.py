# SNMP MIB module (GUDEADS-EPC8221-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-EPC8221-MIB.mib
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

_GadsEPC8221_ObjectIdentity = ObjectIdentity
gadsEPC8221 = _GadsEPC8221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56)
)
_Epc8221Objects_ObjectIdentity = ObjectIdentity
epc8221Objects = _Epc8221Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1)
)
_Epc8221CommonConfig_ObjectIdentity = ObjectIdentity
epc8221CommonConfig = _Epc8221CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 1)
)
_Epc8221SNMPaccess_ObjectIdentity = ObjectIdentity
epc8221SNMPaccess = _Epc8221SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 1, 1)
)


class _Epc8221TrapCtrl_Type(Integer32):
    """Custom type epc8221TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Epc8221TrapCtrl_Type.__name__ = "Integer32"
_Epc8221TrapCtrl_Object = MibScalar
epc8221TrapCtrl = _Epc8221TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 1, 1, 1),
    _Epc8221TrapCtrl_Type()
)
epc8221TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8221TrapCtrl.setStatus("current")
_Epc8221TrapIPTable_Object = MibTable
epc8221TrapIPTable = _Epc8221TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    epc8221TrapIPTable.setStatus("current")
_Epc8221TrapIPEntry_Object = MibTableRow
epc8221TrapIPEntry = _Epc8221TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 1, 1, 2, 1)
)
epc8221TrapIPEntry.setIndexNames(
    (0, "GUDEADS-EPC8221-MIB", "epc8221TrapIPIndex"),
)
if mibBuilder.loadTexts:
    epc8221TrapIPEntry.setStatus("current")


class _Epc8221TrapIPIndex_Type(Integer32):
    """Custom type epc8221TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc8221TrapIPIndex_Type.__name__ = "Integer32"
_Epc8221TrapIPIndex_Object = MibTableColumn
epc8221TrapIPIndex = _Epc8221TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 1, 1, 2, 1, 1),
    _Epc8221TrapIPIndex_Type()
)
epc8221TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221TrapIPIndex.setStatus("current")


class _Epc8221TrapAddr_Type(OctetString):
    """Custom type epc8221TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Epc8221TrapAddr_Type.__name__ = "OctetString"
_Epc8221TrapAddr_Object = MibTableColumn
epc8221TrapAddr = _Epc8221TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 1, 1, 2, 1, 2),
    _Epc8221TrapAddr_Type()
)
epc8221TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8221TrapAddr.setStatus("current")
_Epc8221DeviceConfig_ObjectIdentity = ObjectIdentity
epc8221DeviceConfig = _Epc8221DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 2)
)
_Epc8221IntActors_ObjectIdentity = ObjectIdentity
epc8221IntActors = _Epc8221IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3)
)
_Epc8221relayports_ObjectIdentity = ObjectIdentity
epc8221relayports = _Epc8221relayports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3, 1)
)


class _Epc8221portNumber_Type(Integer32):
    """Custom type epc8221portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Epc8221portNumber_Type.__name__ = "Integer32"
_Epc8221portNumber_Object = MibScalar
epc8221portNumber = _Epc8221portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3, 1, 1),
    _Epc8221portNumber_Type()
)
epc8221portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221portNumber.setStatus("current")
_Epc8221portTable_Object = MibTable
epc8221portTable = _Epc8221portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    epc8221portTable.setStatus("current")
_Epc8221portEntry_Object = MibTableRow
epc8221portEntry = _Epc8221portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3, 1, 2, 1)
)
epc8221portEntry.setIndexNames(
    (0, "GUDEADS-EPC8221-MIB", "epc8221PortIndex"),
)
if mibBuilder.loadTexts:
    epc8221portEntry.setStatus("current")


class _Epc8221PortIndex_Type(Integer32):
    """Custom type epc8221PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Epc8221PortIndex_Type.__name__ = "Integer32"
_Epc8221PortIndex_Object = MibTableColumn
epc8221PortIndex = _Epc8221PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3, 1, 2, 1, 1),
    _Epc8221PortIndex_Type()
)
epc8221PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221PortIndex.setStatus("current")


class _Epc8221PortName_Type(OctetString):
    """Custom type epc8221PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Epc8221PortName_Type.__name__ = "OctetString"
_Epc8221PortName_Object = MibTableColumn
epc8221PortName = _Epc8221PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3, 1, 2, 1, 2),
    _Epc8221PortName_Type()
)
epc8221PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8221PortName.setStatus("current")


class _Epc8221PortState_Type(Integer32):
    """Custom type epc8221PortState based on Integer32"""
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


_Epc8221PortState_Type.__name__ = "Integer32"
_Epc8221PortState_Object = MibTableColumn
epc8221PortState = _Epc8221PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3, 1, 2, 1, 3),
    _Epc8221PortState_Type()
)
epc8221PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8221PortState.setStatus("current")
_Epc8221PortSwitchCount_Type = Integer32
_Epc8221PortSwitchCount_Object = MibTableColumn
epc8221PortSwitchCount = _Epc8221PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3, 1, 2, 1, 4),
    _Epc8221PortSwitchCount_Type()
)
epc8221PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221PortSwitchCount.setStatus("current")


class _Epc8221PortStartupMode_Type(Integer32):
    """Custom type epc8221PortStartupMode based on Integer32"""
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


_Epc8221PortStartupMode_Type.__name__ = "Integer32"
_Epc8221PortStartupMode_Object = MibTableColumn
epc8221PortStartupMode = _Epc8221PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3, 1, 2, 1, 5),
    _Epc8221PortStartupMode_Type()
)
epc8221PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8221PortStartupMode.setStatus("current")


class _Epc8221PortStartupDelay_Type(Integer32):
    """Custom type epc8221PortStartupDelay based on Integer32"""
    defaultValue = 0


_Epc8221PortStartupDelay_Type.__name__ = "Integer32"
_Epc8221PortStartupDelay_Object = MibTableColumn
epc8221PortStartupDelay = _Epc8221PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3, 1, 2, 1, 6),
    _Epc8221PortStartupDelay_Type()
)
epc8221PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8221PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    epc8221PortStartupDelay.setUnits("seconds")


class _Epc8221PortRepowerTime_Type(Integer32):
    """Custom type epc8221PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Epc8221PortRepowerTime_Type.__name__ = "Integer32"
_Epc8221PortRepowerTime_Object = MibTableColumn
epc8221PortRepowerTime = _Epc8221PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3, 1, 2, 1, 7),
    _Epc8221PortRepowerTime_Type()
)
epc8221PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8221PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    epc8221PortRepowerTime.setUnits("seconds")


class _Epc8221Buzzer_Type(Integer32):
    """Custom type epc8221Buzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc8221Buzzer_Type.__name__ = "Integer32"
_Epc8221Buzzer_Object = MibScalar
epc8221Buzzer = _Epc8221Buzzer_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 3, 10),
    _Epc8221Buzzer_Type()
)
epc8221Buzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8221Buzzer.setStatus("current")
if mibBuilder.loadTexts:
    epc8221Buzzer.setUnits("0 = Off, 1 = On")
_Epc8221ExtActors_ObjectIdentity = ObjectIdentity
epc8221ExtActors = _Epc8221ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 4)
)
_Epc8221IntSensors_ObjectIdentity = ObjectIdentity
epc8221IntSensors = _Epc8221IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5)
)
_Epc8221PowerChan_ObjectIdentity = ObjectIdentity
epc8221PowerChan = _Epc8221PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1)
)


class _Epc8221ActivePowerChan_Type(Unsigned32):
    """Custom type epc8221ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc8221ActivePowerChan_Type.__name__ = "Unsigned32"
_Epc8221ActivePowerChan_Object = MibScalar
epc8221ActivePowerChan = _Epc8221ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 1),
    _Epc8221ActivePowerChan_Type()
)
epc8221ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221ActivePowerChan.setStatus("current")
_Epc8221PowerTable_Object = MibTable
epc8221PowerTable = _Epc8221PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    epc8221PowerTable.setStatus("current")
_Epc8221PowerEntry_Object = MibTableRow
epc8221PowerEntry = _Epc8221PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1)
)
epc8221PowerEntry.setIndexNames(
    (0, "GUDEADS-EPC8221-MIB", "epc8221PowerIndex"),
)
if mibBuilder.loadTexts:
    epc8221PowerEntry.setStatus("current")


class _Epc8221PowerIndex_Type(Integer32):
    """Custom type epc8221PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Epc8221PowerIndex_Type.__name__ = "Integer32"
_Epc8221PowerIndex_Object = MibTableColumn
epc8221PowerIndex = _Epc8221PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 1),
    _Epc8221PowerIndex_Type()
)
epc8221PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221PowerIndex.setStatus("current")


class _Epc8221ChanStatus_Type(Integer32):
    """Custom type epc8221ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc8221ChanStatus_Type.__name__ = "Integer32"
_Epc8221ChanStatus_Object = MibTableColumn
epc8221ChanStatus = _Epc8221ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 2),
    _Epc8221ChanStatus_Type()
)
epc8221ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221ChanStatus.setStatus("current")
_Epc8221AbsEnergyActive_Type = Gauge32
_Epc8221AbsEnergyActive_Object = MibTableColumn
epc8221AbsEnergyActive = _Epc8221AbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 3),
    _Epc8221AbsEnergyActive_Type()
)
epc8221AbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221AbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8221AbsEnergyActive.setUnits("Wh")
_Epc8221PowerActive_Type = Integer32
_Epc8221PowerActive_Object = MibTableColumn
epc8221PowerActive = _Epc8221PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 4),
    _Epc8221PowerActive_Type()
)
epc8221PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8221PowerActive.setUnits("W")
_Epc8221Current_Type = Gauge32
_Epc8221Current_Object = MibTableColumn
epc8221Current = _Epc8221Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 5),
    _Epc8221Current_Type()
)
epc8221Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221Current.setStatus("current")
if mibBuilder.loadTexts:
    epc8221Current.setUnits("mA")
_Epc8221Voltage_Type = Gauge32
_Epc8221Voltage_Object = MibTableColumn
epc8221Voltage = _Epc8221Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 6),
    _Epc8221Voltage_Type()
)
epc8221Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221Voltage.setStatus("current")
if mibBuilder.loadTexts:
    epc8221Voltage.setUnits("V")
_Epc8221Frequency_Type = Gauge32
_Epc8221Frequency_Object = MibTableColumn
epc8221Frequency = _Epc8221Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 7),
    _Epc8221Frequency_Type()
)
epc8221Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221Frequency.setStatus("current")
if mibBuilder.loadTexts:
    epc8221Frequency.setUnits("0.01 hz")
_Epc8221PowerFactor_Type = Integer32
_Epc8221PowerFactor_Object = MibTableColumn
epc8221PowerFactor = _Epc8221PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 8),
    _Epc8221PowerFactor_Type()
)
epc8221PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    epc8221PowerFactor.setUnits("0.001")
_Epc8221Pangle_Type = Integer32
_Epc8221Pangle_Object = MibTableColumn
epc8221Pangle = _Epc8221Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 9),
    _Epc8221Pangle_Type()
)
epc8221Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221Pangle.setStatus("current")
if mibBuilder.loadTexts:
    epc8221Pangle.setUnits("0.1 degree")
_Epc8221PowerApparent_Type = Integer32
_Epc8221PowerApparent_Object = MibTableColumn
epc8221PowerApparent = _Epc8221PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 10),
    _Epc8221PowerApparent_Type()
)
epc8221PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    epc8221PowerApparent.setUnits("VA")
_Epc8221PowerReactive_Type = Integer32
_Epc8221PowerReactive_Object = MibTableColumn
epc8221PowerReactive = _Epc8221PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 11),
    _Epc8221PowerReactive_Type()
)
epc8221PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8221PowerReactive.setUnits("VAR")
_Epc8221AbsEnergyReactive_Type = Gauge32
_Epc8221AbsEnergyReactive_Object = MibTableColumn
epc8221AbsEnergyReactive = _Epc8221AbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 12),
    _Epc8221AbsEnergyReactive_Type()
)
epc8221AbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221AbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8221AbsEnergyReactive.setUnits("VARh")
_Epc8221AbsEnergyActiveResettable_Type = Gauge32
_Epc8221AbsEnergyActiveResettable_Object = MibTableColumn
epc8221AbsEnergyActiveResettable = _Epc8221AbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 13),
    _Epc8221AbsEnergyActiveResettable_Type()
)
epc8221AbsEnergyActiveResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8221AbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8221AbsEnergyActiveResettable.setUnits("Wh")
_Epc8221AbsEnergyReactiveResettable_Type = Gauge32
_Epc8221AbsEnergyReactiveResettable_Object = MibTableColumn
epc8221AbsEnergyReactiveResettable = _Epc8221AbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 14),
    _Epc8221AbsEnergyReactiveResettable_Type()
)
epc8221AbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221AbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8221AbsEnergyReactiveResettable.setUnits("VARh")
_Epc8221ResetTime_Type = Gauge32
_Epc8221ResetTime_Object = MibTableColumn
epc8221ResetTime = _Epc8221ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 15),
    _Epc8221ResetTime_Type()
)
epc8221ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    epc8221ResetTime.setUnits("s")
_Epc8221ForwEnergyActive_Type = Gauge32
_Epc8221ForwEnergyActive_Object = MibTableColumn
epc8221ForwEnergyActive = _Epc8221ForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 16),
    _Epc8221ForwEnergyActive_Type()
)
epc8221ForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221ForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8221ForwEnergyActive.setUnits("Wh")
_Epc8221ForwEnergyReactive_Type = Gauge32
_Epc8221ForwEnergyReactive_Object = MibTableColumn
epc8221ForwEnergyReactive = _Epc8221ForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 17),
    _Epc8221ForwEnergyReactive_Type()
)
epc8221ForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221ForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8221ForwEnergyReactive.setUnits("VARh")
_Epc8221ForwEnergyActiveResettable_Type = Gauge32
_Epc8221ForwEnergyActiveResettable_Object = MibTableColumn
epc8221ForwEnergyActiveResettable = _Epc8221ForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 18),
    _Epc8221ForwEnergyActiveResettable_Type()
)
epc8221ForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221ForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8221ForwEnergyActiveResettable.setUnits("Wh")
_Epc8221ForwEnergyReactiveResettable_Type = Gauge32
_Epc8221ForwEnergyReactiveResettable_Object = MibTableColumn
epc8221ForwEnergyReactiveResettable = _Epc8221ForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 19),
    _Epc8221ForwEnergyReactiveResettable_Type()
)
epc8221ForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221ForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8221ForwEnergyReactiveResettable.setUnits("VARh")
_Epc8221RevEnergyActive_Type = Gauge32
_Epc8221RevEnergyActive_Object = MibTableColumn
epc8221RevEnergyActive = _Epc8221RevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 20),
    _Epc8221RevEnergyActive_Type()
)
epc8221RevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221RevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8221RevEnergyActive.setUnits("Wh")
_Epc8221RevEnergyReactive_Type = Gauge32
_Epc8221RevEnergyReactive_Object = MibTableColumn
epc8221RevEnergyReactive = _Epc8221RevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 21),
    _Epc8221RevEnergyReactive_Type()
)
epc8221RevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221RevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8221RevEnergyReactive.setUnits("VARh")
_Epc8221RevEnergyActiveResettable_Type = Gauge32
_Epc8221RevEnergyActiveResettable_Object = MibTableColumn
epc8221RevEnergyActiveResettable = _Epc8221RevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 22),
    _Epc8221RevEnergyActiveResettable_Type()
)
epc8221RevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221RevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8221RevEnergyActiveResettable.setUnits("Wh")
_Epc8221RevEnergyReactiveResettable_Type = Gauge32
_Epc8221RevEnergyReactiveResettable_Object = MibTableColumn
epc8221RevEnergyReactiveResettable = _Epc8221RevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 1, 2, 1, 23),
    _Epc8221RevEnergyReactiveResettable_Type()
)
epc8221RevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221RevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8221RevEnergyReactiveResettable.setUnits("VARh")
_Epc8221OVPTable_Object = MibTable
epc8221OVPTable = _Epc8221OVPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 2)
)
if mibBuilder.loadTexts:
    epc8221OVPTable.setStatus("current")
_Epc8221OVPEntry_Object = MibTableRow
epc8221OVPEntry = _Epc8221OVPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 2, 1)
)
epc8221OVPEntry.setIndexNames(
    (0, "GUDEADS-EPC8221-MIB", "epc8221OVPIndex"),
)
if mibBuilder.loadTexts:
    epc8221OVPEntry.setStatus("current")


class _Epc8221OVPIndex_Type(Integer32):
    """Custom type epc8221OVPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Epc8221OVPIndex_Type.__name__ = "Integer32"
_Epc8221OVPIndex_Object = MibTableColumn
epc8221OVPIndex = _Epc8221OVPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 2, 1, 1),
    _Epc8221OVPIndex_Type()
)
epc8221OVPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221OVPIndex.setStatus("current")


class _Epc8221OVPStatus_Type(Integer32):
    """Custom type epc8221OVPStatus based on Integer32"""
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


_Epc8221OVPStatus_Type.__name__ = "Integer32"
_Epc8221OVPStatus_Object = MibTableColumn
epc8221OVPStatus = _Epc8221OVPStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 5, 2, 1, 2),
    _Epc8221OVPStatus_Type()
)
epc8221OVPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221OVPStatus.setStatus("current")
_Epc8221ExtSensors_ObjectIdentity = ObjectIdentity
epc8221ExtSensors = _Epc8221ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 6)
)
_Epc8221SensorTable_Object = MibTable
epc8221SensorTable = _Epc8221SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 6, 1)
)
if mibBuilder.loadTexts:
    epc8221SensorTable.setStatus("current")
_Epc8221SensorEntry_Object = MibTableRow
epc8221SensorEntry = _Epc8221SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 6, 1, 1)
)
epc8221SensorEntry.setIndexNames(
    (0, "GUDEADS-EPC8221-MIB", "epc8221SensorIndex"),
)
if mibBuilder.loadTexts:
    epc8221SensorEntry.setStatus("current")


class _Epc8221SensorIndex_Type(Integer32):
    """Custom type epc8221SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Epc8221SensorIndex_Type.__name__ = "Integer32"
_Epc8221SensorIndex_Object = MibTableColumn
epc8221SensorIndex = _Epc8221SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 6, 1, 1, 1),
    _Epc8221SensorIndex_Type()
)
epc8221SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221SensorIndex.setStatus("current")
_Epc8221TempSensor_Type = Integer32
_Epc8221TempSensor_Object = MibTableColumn
epc8221TempSensor = _Epc8221TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 6, 1, 1, 2),
    _Epc8221TempSensor_Type()
)
epc8221TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc8221TempSensor.setUnits("0.1 degree Celsius")
_Epc8221HygroSensor_Type = Integer32
_Epc8221HygroSensor_Object = MibTableColumn
epc8221HygroSensor = _Epc8221HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 6, 1, 1, 3),
    _Epc8221HygroSensor_Type()
)
epc8221HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc8221HygroSensor.setUnits("0.1 percent humidity")


class _Epc8221InputSensor_Type(Integer32):
    """Custom type epc8221InputSensor based on Integer32"""
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


_Epc8221InputSensor_Type.__name__ = "Integer32"
_Epc8221InputSensor_Object = MibTableColumn
epc8221InputSensor = _Epc8221InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 6, 1, 1, 4),
    _Epc8221InputSensor_Type()
)
epc8221InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221InputSensor.setStatus("current")
_Epc8221AirPressure_Type = Integer32
_Epc8221AirPressure_Object = MibTableColumn
epc8221AirPressure = _Epc8221AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 6, 1, 1, 5),
    _Epc8221AirPressure_Type()
)
epc8221AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    epc8221AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Epc8221DewPoint_Type = Integer32
_Epc8221DewPoint_Object = MibTableColumn
epc8221DewPoint = _Epc8221DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 6, 1, 1, 6),
    _Epc8221DewPoint_Type()
)
epc8221DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    epc8221DewPoint.setUnits("0.1 degree Celsius")
_Epc8221DewPointDiff_Type = Integer32
_Epc8221DewPointDiff_Object = MibTableColumn
epc8221DewPointDiff = _Epc8221DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 56, 1, 6, 1, 1, 7),
    _Epc8221DewPointDiff_Type()
)
epc8221DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8221DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    epc8221DewPointDiff.setUnits("0.1 degree Celsius")
_Epc8221Conf_ObjectIdentity = ObjectIdentity
epc8221Conf = _Epc8221Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 2)
)
_Epc8221Groups_ObjectIdentity = ObjectIdentity
epc8221Groups = _Epc8221Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 2, 1)
)
_Epc8221Compls_ObjectIdentity = ObjectIdentity
epc8221Compls = _Epc8221Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 56, 3)
)

# Managed Objects groups

epc8221BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 56, 2, 1, 1)
)
epc8221BasicGroup.setObjects(
      *(("GUDEADS-EPC8221-MIB", "epc8221TrapCtrl"),
        ("GUDEADS-EPC8221-MIB", "epc8221TrapIPIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221TrapAddr"),
        ("GUDEADS-EPC8221-MIB", "epc8221portNumber"),
        ("GUDEADS-EPC8221-MIB", "epc8221PortIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221PortName"),
        ("GUDEADS-EPC8221-MIB", "epc8221PortState"),
        ("GUDEADS-EPC8221-MIB", "epc8221PortSwitchCount"),
        ("GUDEADS-EPC8221-MIB", "epc8221PortStartupMode"),
        ("GUDEADS-EPC8221-MIB", "epc8221PortStartupDelay"),
        ("GUDEADS-EPC8221-MIB", "epc8221PortRepowerTime"),
        ("GUDEADS-EPC8221-MIB", "epc8221Buzzer"),
        ("GUDEADS-EPC8221-MIB", "epc8221ActivePowerChan"),
        ("GUDEADS-EPC8221-MIB", "epc8221PowerIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221ChanStatus"),
        ("GUDEADS-EPC8221-MIB", "epc8221AbsEnergyActive"),
        ("GUDEADS-EPC8221-MIB", "epc8221PowerActive"),
        ("GUDEADS-EPC8221-MIB", "epc8221Current"),
        ("GUDEADS-EPC8221-MIB", "epc8221Voltage"),
        ("GUDEADS-EPC8221-MIB", "epc8221Frequency"),
        ("GUDEADS-EPC8221-MIB", "epc8221PowerFactor"),
        ("GUDEADS-EPC8221-MIB", "epc8221Pangle"),
        ("GUDEADS-EPC8221-MIB", "epc8221PowerApparent"),
        ("GUDEADS-EPC8221-MIB", "epc8221PowerReactive"),
        ("GUDEADS-EPC8221-MIB", "epc8221AbsEnergyReactive"),
        ("GUDEADS-EPC8221-MIB", "epc8221AbsEnergyActiveResettable"),
        ("GUDEADS-EPC8221-MIB", "epc8221AbsEnergyReactiveResettable"),
        ("GUDEADS-EPC8221-MIB", "epc8221ResetTime"),
        ("GUDEADS-EPC8221-MIB", "epc8221ForwEnergyActive"),
        ("GUDEADS-EPC8221-MIB", "epc8221ForwEnergyReactive"),
        ("GUDEADS-EPC8221-MIB", "epc8221ForwEnergyActiveResettable"),
        ("GUDEADS-EPC8221-MIB", "epc8221ForwEnergyReactiveResettable"),
        ("GUDEADS-EPC8221-MIB", "epc8221RevEnergyActive"),
        ("GUDEADS-EPC8221-MIB", "epc8221RevEnergyReactive"),
        ("GUDEADS-EPC8221-MIB", "epc8221RevEnergyActiveResettable"),
        ("GUDEADS-EPC8221-MIB", "epc8221RevEnergyReactiveResettable"),
        ("GUDEADS-EPC8221-MIB", "epc8221OVPIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221OVPStatus"),
        ("GUDEADS-EPC8221-MIB", "epc8221SensorIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221TempSensor"),
        ("GUDEADS-EPC8221-MIB", "epc8221HygroSensor"),
        ("GUDEADS-EPC8221-MIB", "epc8221InputSensor"),
        ("GUDEADS-EPC8221-MIB", "epc8221AirPressure"),
        ("GUDEADS-EPC8221-MIB", "epc8221DewPoint"),
        ("GUDEADS-EPC8221-MIB", "epc8221DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc8221BasicGroup.setStatus("current")


# Notification objects

epc8221SwitchEvtPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 56, 3, 1)
)
epc8221SwitchEvtPort.setObjects(
      *(("GUDEADS-EPC8221-MIB", "epc8221PortIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221PortName"),
        ("GUDEADS-EPC8221-MIB", "epc8221PortState"),
        ("GUDEADS-EPC8221-MIB", "epc8221PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc8221SwitchEvtPort.setStatus(
        "current"
    )

epc8221TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 56, 3, 2)
)
epc8221TempEvtSen.setObjects(
      *(("GUDEADS-EPC8221-MIB", "epc8221SensorIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221TempSensor"))
)
if mibBuilder.loadTexts:
    epc8221TempEvtSen.setStatus(
        "current"
    )

epc8221HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 56, 3, 3)
)
epc8221HygroEvtSen.setObjects(
      *(("GUDEADS-EPC8221-MIB", "epc8221SensorIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221HygroSensor"))
)
if mibBuilder.loadTexts:
    epc8221HygroEvtSen.setStatus(
        "current"
    )

epc8221InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 56, 3, 4)
)
epc8221InputEvtSen.setObjects(
      *(("GUDEADS-EPC8221-MIB", "epc8221SensorIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221InputSensor"))
)
if mibBuilder.loadTexts:
    epc8221InputEvtSen.setStatus(
        "current"
    )

epc8221AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 56, 3, 5)
)
epc8221AirPressureEvtSen.setObjects(
      *(("GUDEADS-EPC8221-MIB", "epc8221SensorIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221AirPressure"))
)
if mibBuilder.loadTexts:
    epc8221AirPressureEvtSen.setStatus(
        "current"
    )

epc8221DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 56, 3, 6)
)
epc8221DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-EPC8221-MIB", "epc8221SensorIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc8221DewPtDiffEvtSen.setStatus(
        "current"
    )

epc8221OVPEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 56, 3, 7)
)
epc8221OVPEvt.setObjects(
      *(("GUDEADS-EPC8221-MIB", "epc8221OVPIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221OVPStatus"))
)
if mibBuilder.loadTexts:
    epc8221OVPEvt.setStatus(
        "current"
    )

epc8221LineAmperageEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 56, 3, 8)
)
epc8221LineAmperageEvt.setObjects(
      *(("GUDEADS-EPC8221-MIB", "epc8221PowerIndex"),
        ("GUDEADS-EPC8221-MIB", "epc8221PowerActive"),
        ("GUDEADS-EPC8221-MIB", "epc8221Current"),
        ("GUDEADS-EPC8221-MIB", "epc8221Voltage"),
        ("GUDEADS-EPC8221-MIB", "epc8221Frequency"),
        ("GUDEADS-EPC8221-MIB", "epc8221PowerApparent"),
        ("GUDEADS-EPC8221-MIB", "epc8221PowerReactive"))
)
if mibBuilder.loadTexts:
    epc8221LineAmperageEvt.setStatus(
        "current"
    )


# Notifications groups

epc8221NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 56, 2, 1, 2)
)
epc8221NotificationGroup.setObjects(
      *(("GUDEADS-EPC8221-MIB", "epc8221SwitchEvtPort"),
        ("GUDEADS-EPC8221-MIB", "epc8221TempEvtSen"),
        ("GUDEADS-EPC8221-MIB", "epc8221HygroEvtSen"),
        ("GUDEADS-EPC8221-MIB", "epc8221InputEvtSen"),
        ("GUDEADS-EPC8221-MIB", "epc8221AirPressureEvtSen"),
        ("GUDEADS-EPC8221-MIB", "epc8221DewPtDiffEvtSen"),
        ("GUDEADS-EPC8221-MIB", "epc8221OVPEvt"),
        ("GUDEADS-EPC8221-MIB", "epc8221LineAmperageEvt"))
)
if mibBuilder.loadTexts:
    epc8221NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-EPC8221-MIB",
    **{"gudeads": gudeads,
       "gadsEPC8221": gadsEPC8221,
       "epc8221Objects": epc8221Objects,
       "epc8221CommonConfig": epc8221CommonConfig,
       "epc8221SNMPaccess": epc8221SNMPaccess,
       "epc8221TrapCtrl": epc8221TrapCtrl,
       "epc8221TrapIPTable": epc8221TrapIPTable,
       "epc8221TrapIPEntry": epc8221TrapIPEntry,
       "epc8221TrapIPIndex": epc8221TrapIPIndex,
       "epc8221TrapAddr": epc8221TrapAddr,
       "epc8221DeviceConfig": epc8221DeviceConfig,
       "epc8221IntActors": epc8221IntActors,
       "epc8221relayports": epc8221relayports,
       "epc8221portNumber": epc8221portNumber,
       "epc8221portTable": epc8221portTable,
       "epc8221portEntry": epc8221portEntry,
       "epc8221PortIndex": epc8221PortIndex,
       "epc8221PortName": epc8221PortName,
       "epc8221PortState": epc8221PortState,
       "epc8221PortSwitchCount": epc8221PortSwitchCount,
       "epc8221PortStartupMode": epc8221PortStartupMode,
       "epc8221PortStartupDelay": epc8221PortStartupDelay,
       "epc8221PortRepowerTime": epc8221PortRepowerTime,
       "epc8221Buzzer": epc8221Buzzer,
       "epc8221ExtActors": epc8221ExtActors,
       "epc8221IntSensors": epc8221IntSensors,
       "epc8221PowerChan": epc8221PowerChan,
       "epc8221ActivePowerChan": epc8221ActivePowerChan,
       "epc8221PowerTable": epc8221PowerTable,
       "epc8221PowerEntry": epc8221PowerEntry,
       "epc8221PowerIndex": epc8221PowerIndex,
       "epc8221ChanStatus": epc8221ChanStatus,
       "epc8221AbsEnergyActive": epc8221AbsEnergyActive,
       "epc8221PowerActive": epc8221PowerActive,
       "epc8221Current": epc8221Current,
       "epc8221Voltage": epc8221Voltage,
       "epc8221Frequency": epc8221Frequency,
       "epc8221PowerFactor": epc8221PowerFactor,
       "epc8221Pangle": epc8221Pangle,
       "epc8221PowerApparent": epc8221PowerApparent,
       "epc8221PowerReactive": epc8221PowerReactive,
       "epc8221AbsEnergyReactive": epc8221AbsEnergyReactive,
       "epc8221AbsEnergyActiveResettable": epc8221AbsEnergyActiveResettable,
       "epc8221AbsEnergyReactiveResettable": epc8221AbsEnergyReactiveResettable,
       "epc8221ResetTime": epc8221ResetTime,
       "epc8221ForwEnergyActive": epc8221ForwEnergyActive,
       "epc8221ForwEnergyReactive": epc8221ForwEnergyReactive,
       "epc8221ForwEnergyActiveResettable": epc8221ForwEnergyActiveResettable,
       "epc8221ForwEnergyReactiveResettable": epc8221ForwEnergyReactiveResettable,
       "epc8221RevEnergyActive": epc8221RevEnergyActive,
       "epc8221RevEnergyReactive": epc8221RevEnergyReactive,
       "epc8221RevEnergyActiveResettable": epc8221RevEnergyActiveResettable,
       "epc8221RevEnergyReactiveResettable": epc8221RevEnergyReactiveResettable,
       "epc8221OVPTable": epc8221OVPTable,
       "epc8221OVPEntry": epc8221OVPEntry,
       "epc8221OVPIndex": epc8221OVPIndex,
       "epc8221OVPStatus": epc8221OVPStatus,
       "epc8221ExtSensors": epc8221ExtSensors,
       "epc8221SensorTable": epc8221SensorTable,
       "epc8221SensorEntry": epc8221SensorEntry,
       "epc8221SensorIndex": epc8221SensorIndex,
       "epc8221TempSensor": epc8221TempSensor,
       "epc8221HygroSensor": epc8221HygroSensor,
       "epc8221InputSensor": epc8221InputSensor,
       "epc8221AirPressure": epc8221AirPressure,
       "epc8221DewPoint": epc8221DewPoint,
       "epc8221DewPointDiff": epc8221DewPointDiff,
       "epc8221Conf": epc8221Conf,
       "epc8221Groups": epc8221Groups,
       "epc8221BasicGroup": epc8221BasicGroup,
       "epc8221NotificationGroup": epc8221NotificationGroup,
       "epc8221Compls": epc8221Compls,
       "events": events,
       "epc8221SwitchEvtPort": epc8221SwitchEvtPort,
       "epc8221TempEvtSen": epc8221TempEvtSen,
       "epc8221HygroEvtSen": epc8221HygroEvtSen,
       "epc8221InputEvtSen": epc8221InputEvtSen,
       "epc8221AirPressureEvtSen": epc8221AirPressureEvtSen,
       "epc8221DewPtDiffEvtSen": epc8221DewPtDiffEvtSen,
       "epc8221OVPEvt": epc8221OVPEvt,
       "epc8221LineAmperageEvt": epc8221LineAmperageEvt}
)
