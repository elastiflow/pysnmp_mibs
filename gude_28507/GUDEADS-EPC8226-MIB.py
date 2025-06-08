# SNMP MIB module (GUDEADS-EPC8226-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-EPC8226-MIB.mib
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

_GadsEPC8226_ObjectIdentity = ObjectIdentity
gadsEPC8226 = _GadsEPC8226_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58)
)
_Epc8226Objects_ObjectIdentity = ObjectIdentity
epc8226Objects = _Epc8226Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1)
)
_Epc8226CommonConfig_ObjectIdentity = ObjectIdentity
epc8226CommonConfig = _Epc8226CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 1)
)
_Epc8226SNMPaccess_ObjectIdentity = ObjectIdentity
epc8226SNMPaccess = _Epc8226SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 1, 1)
)


class _Epc8226TrapCtrl_Type(Integer32):
    """Custom type epc8226TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Epc8226TrapCtrl_Type.__name__ = "Integer32"
_Epc8226TrapCtrl_Object = MibScalar
epc8226TrapCtrl = _Epc8226TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 1, 1, 1),
    _Epc8226TrapCtrl_Type()
)
epc8226TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8226TrapCtrl.setStatus("current")
_Epc8226TrapIPTable_Object = MibTable
epc8226TrapIPTable = _Epc8226TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    epc8226TrapIPTable.setStatus("current")
_Epc8226TrapIPEntry_Object = MibTableRow
epc8226TrapIPEntry = _Epc8226TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 1, 1, 2, 1)
)
epc8226TrapIPEntry.setIndexNames(
    (0, "GUDEADS-EPC8226-MIB", "epc8226TrapIPIndex"),
)
if mibBuilder.loadTexts:
    epc8226TrapIPEntry.setStatus("current")


class _Epc8226TrapIPIndex_Type(Integer32):
    """Custom type epc8226TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc8226TrapIPIndex_Type.__name__ = "Integer32"
_Epc8226TrapIPIndex_Object = MibTableColumn
epc8226TrapIPIndex = _Epc8226TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 1, 1, 2, 1, 1),
    _Epc8226TrapIPIndex_Type()
)
epc8226TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226TrapIPIndex.setStatus("current")


class _Epc8226TrapAddr_Type(OctetString):
    """Custom type epc8226TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Epc8226TrapAddr_Type.__name__ = "OctetString"
_Epc8226TrapAddr_Object = MibTableColumn
epc8226TrapAddr = _Epc8226TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 1, 1, 2, 1, 2),
    _Epc8226TrapAddr_Type()
)
epc8226TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8226TrapAddr.setStatus("current")
_Epc8226DeviceConfig_ObjectIdentity = ObjectIdentity
epc8226DeviceConfig = _Epc8226DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 2)
)
_Epc8226IntActors_ObjectIdentity = ObjectIdentity
epc8226IntActors = _Epc8226IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3)
)
_Epc8226relayports_ObjectIdentity = ObjectIdentity
epc8226relayports = _Epc8226relayports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3, 1)
)


class _Epc8226portNumber_Type(Integer32):
    """Custom type epc8226portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Epc8226portNumber_Type.__name__ = "Integer32"
_Epc8226portNumber_Object = MibScalar
epc8226portNumber = _Epc8226portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3, 1, 1),
    _Epc8226portNumber_Type()
)
epc8226portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226portNumber.setStatus("current")
_Epc8226portTable_Object = MibTable
epc8226portTable = _Epc8226portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    epc8226portTable.setStatus("current")
_Epc8226portEntry_Object = MibTableRow
epc8226portEntry = _Epc8226portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3, 1, 2, 1)
)
epc8226portEntry.setIndexNames(
    (0, "GUDEADS-EPC8226-MIB", "epc8226PortIndex"),
)
if mibBuilder.loadTexts:
    epc8226portEntry.setStatus("current")


class _Epc8226PortIndex_Type(Integer32):
    """Custom type epc8226PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Epc8226PortIndex_Type.__name__ = "Integer32"
_Epc8226PortIndex_Object = MibTableColumn
epc8226PortIndex = _Epc8226PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3, 1, 2, 1, 1),
    _Epc8226PortIndex_Type()
)
epc8226PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226PortIndex.setStatus("current")


class _Epc8226PortName_Type(OctetString):
    """Custom type epc8226PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Epc8226PortName_Type.__name__ = "OctetString"
_Epc8226PortName_Object = MibTableColumn
epc8226PortName = _Epc8226PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3, 1, 2, 1, 2),
    _Epc8226PortName_Type()
)
epc8226PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8226PortName.setStatus("current")


class _Epc8226PortState_Type(Integer32):
    """Custom type epc8226PortState based on Integer32"""
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


_Epc8226PortState_Type.__name__ = "Integer32"
_Epc8226PortState_Object = MibTableColumn
epc8226PortState = _Epc8226PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3, 1, 2, 1, 3),
    _Epc8226PortState_Type()
)
epc8226PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8226PortState.setStatus("current")
_Epc8226PortSwitchCount_Type = Integer32
_Epc8226PortSwitchCount_Object = MibTableColumn
epc8226PortSwitchCount = _Epc8226PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3, 1, 2, 1, 4),
    _Epc8226PortSwitchCount_Type()
)
epc8226PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226PortSwitchCount.setStatus("current")


class _Epc8226PortStartupMode_Type(Integer32):
    """Custom type epc8226PortStartupMode based on Integer32"""
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


_Epc8226PortStartupMode_Type.__name__ = "Integer32"
_Epc8226PortStartupMode_Object = MibTableColumn
epc8226PortStartupMode = _Epc8226PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3, 1, 2, 1, 5),
    _Epc8226PortStartupMode_Type()
)
epc8226PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8226PortStartupMode.setStatus("current")


class _Epc8226PortStartupDelay_Type(Integer32):
    """Custom type epc8226PortStartupDelay based on Integer32"""
    defaultValue = 0


_Epc8226PortStartupDelay_Type.__name__ = "Integer32"
_Epc8226PortStartupDelay_Object = MibTableColumn
epc8226PortStartupDelay = _Epc8226PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3, 1, 2, 1, 6),
    _Epc8226PortStartupDelay_Type()
)
epc8226PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8226PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    epc8226PortStartupDelay.setUnits("seconds")


class _Epc8226PortRepowerTime_Type(Integer32):
    """Custom type epc8226PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Epc8226PortRepowerTime_Type.__name__ = "Integer32"
_Epc8226PortRepowerTime_Object = MibTableColumn
epc8226PortRepowerTime = _Epc8226PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3, 1, 2, 1, 7),
    _Epc8226PortRepowerTime_Type()
)
epc8226PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8226PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    epc8226PortRepowerTime.setUnits("seconds")


class _Epc8226Buzzer_Type(Integer32):
    """Custom type epc8226Buzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc8226Buzzer_Type.__name__ = "Integer32"
_Epc8226Buzzer_Object = MibScalar
epc8226Buzzer = _Epc8226Buzzer_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 3, 10),
    _Epc8226Buzzer_Type()
)
epc8226Buzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8226Buzzer.setStatus("current")
if mibBuilder.loadTexts:
    epc8226Buzzer.setUnits("0 = Off, 1 = On")
_Epc8226ExtActors_ObjectIdentity = ObjectIdentity
epc8226ExtActors = _Epc8226ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 4)
)
_Epc8226IntSensors_ObjectIdentity = ObjectIdentity
epc8226IntSensors = _Epc8226IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5)
)
_Epc8226PowerChan_ObjectIdentity = ObjectIdentity
epc8226PowerChan = _Epc8226PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1)
)


class _Epc8226ActivePowerChan_Type(Unsigned32):
    """Custom type epc8226ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc8226ActivePowerChan_Type.__name__ = "Unsigned32"
_Epc8226ActivePowerChan_Object = MibScalar
epc8226ActivePowerChan = _Epc8226ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 1),
    _Epc8226ActivePowerChan_Type()
)
epc8226ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226ActivePowerChan.setStatus("current")
_Epc8226PowerTable_Object = MibTable
epc8226PowerTable = _Epc8226PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    epc8226PowerTable.setStatus("current")
_Epc8226PowerEntry_Object = MibTableRow
epc8226PowerEntry = _Epc8226PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1)
)
epc8226PowerEntry.setIndexNames(
    (0, "GUDEADS-EPC8226-MIB", "epc8226PowerIndex"),
)
if mibBuilder.loadTexts:
    epc8226PowerEntry.setStatus("current")


class _Epc8226PowerIndex_Type(Integer32):
    """Custom type epc8226PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Epc8226PowerIndex_Type.__name__ = "Integer32"
_Epc8226PowerIndex_Object = MibTableColumn
epc8226PowerIndex = _Epc8226PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 1),
    _Epc8226PowerIndex_Type()
)
epc8226PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226PowerIndex.setStatus("current")


class _Epc8226ChanStatus_Type(Integer32):
    """Custom type epc8226ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc8226ChanStatus_Type.__name__ = "Integer32"
_Epc8226ChanStatus_Object = MibTableColumn
epc8226ChanStatus = _Epc8226ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 2),
    _Epc8226ChanStatus_Type()
)
epc8226ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226ChanStatus.setStatus("current")
_Epc8226AbsEnergyActive_Type = Gauge32
_Epc8226AbsEnergyActive_Object = MibTableColumn
epc8226AbsEnergyActive = _Epc8226AbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 3),
    _Epc8226AbsEnergyActive_Type()
)
epc8226AbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226AbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226AbsEnergyActive.setUnits("Wh")
_Epc8226PowerActive_Type = Integer32
_Epc8226PowerActive_Object = MibTableColumn
epc8226PowerActive = _Epc8226PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 4),
    _Epc8226PowerActive_Type()
)
epc8226PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226PowerActive.setUnits("W")
_Epc8226Current_Type = Gauge32
_Epc8226Current_Object = MibTableColumn
epc8226Current = _Epc8226Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 5),
    _Epc8226Current_Type()
)
epc8226Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226Current.setStatus("current")
if mibBuilder.loadTexts:
    epc8226Current.setUnits("mA")
_Epc8226Voltage_Type = Gauge32
_Epc8226Voltage_Object = MibTableColumn
epc8226Voltage = _Epc8226Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 6),
    _Epc8226Voltage_Type()
)
epc8226Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226Voltage.setStatus("current")
if mibBuilder.loadTexts:
    epc8226Voltage.setUnits("V")
_Epc8226Frequency_Type = Gauge32
_Epc8226Frequency_Object = MibTableColumn
epc8226Frequency = _Epc8226Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 7),
    _Epc8226Frequency_Type()
)
epc8226Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226Frequency.setStatus("current")
if mibBuilder.loadTexts:
    epc8226Frequency.setUnits("0.01 hz")
_Epc8226PowerFactor_Type = Integer32
_Epc8226PowerFactor_Object = MibTableColumn
epc8226PowerFactor = _Epc8226PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 8),
    _Epc8226PowerFactor_Type()
)
epc8226PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    epc8226PowerFactor.setUnits("0.001")
_Epc8226Pangle_Type = Integer32
_Epc8226Pangle_Object = MibTableColumn
epc8226Pangle = _Epc8226Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 9),
    _Epc8226Pangle_Type()
)
epc8226Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226Pangle.setStatus("current")
if mibBuilder.loadTexts:
    epc8226Pangle.setUnits("0.1 degree")
_Epc8226PowerApparent_Type = Integer32
_Epc8226PowerApparent_Object = MibTableColumn
epc8226PowerApparent = _Epc8226PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 10),
    _Epc8226PowerApparent_Type()
)
epc8226PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    epc8226PowerApparent.setUnits("VA")
_Epc8226PowerReactive_Type = Integer32
_Epc8226PowerReactive_Object = MibTableColumn
epc8226PowerReactive = _Epc8226PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 11),
    _Epc8226PowerReactive_Type()
)
epc8226PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226PowerReactive.setUnits("VAR")
_Epc8226AbsEnergyReactive_Type = Gauge32
_Epc8226AbsEnergyReactive_Object = MibTableColumn
epc8226AbsEnergyReactive = _Epc8226AbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 12),
    _Epc8226AbsEnergyReactive_Type()
)
epc8226AbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226AbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226AbsEnergyReactive.setUnits("VARh")
_Epc8226AbsEnergyActiveResettable_Type = Gauge32
_Epc8226AbsEnergyActiveResettable_Object = MibTableColumn
epc8226AbsEnergyActiveResettable = _Epc8226AbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 13),
    _Epc8226AbsEnergyActiveResettable_Type()
)
epc8226AbsEnergyActiveResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8226AbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8226AbsEnergyActiveResettable.setUnits("Wh")
_Epc8226AbsEnergyReactiveResettable_Type = Gauge32
_Epc8226AbsEnergyReactiveResettable_Object = MibTableColumn
epc8226AbsEnergyReactiveResettable = _Epc8226AbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 14),
    _Epc8226AbsEnergyReactiveResettable_Type()
)
epc8226AbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226AbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8226AbsEnergyReactiveResettable.setUnits("VARh")
_Epc8226ResetTime_Type = Gauge32
_Epc8226ResetTime_Object = MibTableColumn
epc8226ResetTime = _Epc8226ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 15),
    _Epc8226ResetTime_Type()
)
epc8226ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    epc8226ResetTime.setUnits("s")
_Epc8226ForwEnergyActive_Type = Gauge32
_Epc8226ForwEnergyActive_Object = MibTableColumn
epc8226ForwEnergyActive = _Epc8226ForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 16),
    _Epc8226ForwEnergyActive_Type()
)
epc8226ForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226ForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226ForwEnergyActive.setUnits("Wh")
_Epc8226ForwEnergyReactive_Type = Gauge32
_Epc8226ForwEnergyReactive_Object = MibTableColumn
epc8226ForwEnergyReactive = _Epc8226ForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 17),
    _Epc8226ForwEnergyReactive_Type()
)
epc8226ForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226ForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226ForwEnergyReactive.setUnits("VARh")
_Epc8226ForwEnergyActiveResettable_Type = Gauge32
_Epc8226ForwEnergyActiveResettable_Object = MibTableColumn
epc8226ForwEnergyActiveResettable = _Epc8226ForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 18),
    _Epc8226ForwEnergyActiveResettable_Type()
)
epc8226ForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226ForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8226ForwEnergyActiveResettable.setUnits("Wh")
_Epc8226ForwEnergyReactiveResettable_Type = Gauge32
_Epc8226ForwEnergyReactiveResettable_Object = MibTableColumn
epc8226ForwEnergyReactiveResettable = _Epc8226ForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 19),
    _Epc8226ForwEnergyReactiveResettable_Type()
)
epc8226ForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226ForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8226ForwEnergyReactiveResettable.setUnits("VARh")
_Epc8226RevEnergyActive_Type = Gauge32
_Epc8226RevEnergyActive_Object = MibTableColumn
epc8226RevEnergyActive = _Epc8226RevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 20),
    _Epc8226RevEnergyActive_Type()
)
epc8226RevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226RevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226RevEnergyActive.setUnits("Wh")
_Epc8226RevEnergyReactive_Type = Gauge32
_Epc8226RevEnergyReactive_Object = MibTableColumn
epc8226RevEnergyReactive = _Epc8226RevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 21),
    _Epc8226RevEnergyReactive_Type()
)
epc8226RevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226RevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226RevEnergyReactive.setUnits("VARh")
_Epc8226RevEnergyActiveResettable_Type = Gauge32
_Epc8226RevEnergyActiveResettable_Object = MibTableColumn
epc8226RevEnergyActiveResettable = _Epc8226RevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 22),
    _Epc8226RevEnergyActiveResettable_Type()
)
epc8226RevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226RevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8226RevEnergyActiveResettable.setUnits("Wh")
_Epc8226RevEnergyReactiveResettable_Type = Gauge32
_Epc8226RevEnergyReactiveResettable_Object = MibTableColumn
epc8226RevEnergyReactiveResettable = _Epc8226RevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 1, 2, 1, 23),
    _Epc8226RevEnergyReactiveResettable_Type()
)
epc8226RevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226RevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8226RevEnergyReactiveResettable.setUnits("VARh")
_Epc8226OVPTable_Object = MibTable
epc8226OVPTable = _Epc8226OVPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 2)
)
if mibBuilder.loadTexts:
    epc8226OVPTable.setStatus("current")
_Epc8226OVPEntry_Object = MibTableRow
epc8226OVPEntry = _Epc8226OVPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 2, 1)
)
epc8226OVPEntry.setIndexNames(
    (0, "GUDEADS-EPC8226-MIB", "epc8226OVPIndex"),
)
if mibBuilder.loadTexts:
    epc8226OVPEntry.setStatus("current")


class _Epc8226OVPIndex_Type(Integer32):
    """Custom type epc8226OVPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Epc8226OVPIndex_Type.__name__ = "Integer32"
_Epc8226OVPIndex_Object = MibTableColumn
epc8226OVPIndex = _Epc8226OVPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 2, 1, 1),
    _Epc8226OVPIndex_Type()
)
epc8226OVPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226OVPIndex.setStatus("current")


class _Epc8226OVPStatus_Type(Integer32):
    """Custom type epc8226OVPStatus based on Integer32"""
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


_Epc8226OVPStatus_Type.__name__ = "Integer32"
_Epc8226OVPStatus_Object = MibTableColumn
epc8226OVPStatus = _Epc8226OVPStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 2, 1, 2),
    _Epc8226OVPStatus_Type()
)
epc8226OVPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226OVPStatus.setStatus("current")
_Epc8226SinglePortPowerChan_ObjectIdentity = ObjectIdentity
epc8226SinglePortPowerChan = _Epc8226SinglePortPowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5)
)


class _Epc8226spActivePowerChan_Type(Unsigned32):
    """Custom type epc8226spActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc8226spActivePowerChan_Type.__name__ = "Unsigned32"
_Epc8226spActivePowerChan_Object = MibScalar
epc8226spActivePowerChan = _Epc8226spActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 1),
    _Epc8226spActivePowerChan_Type()
)
epc8226spActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spActivePowerChan.setStatus("current")
_Epc8226spPowerTable_Object = MibTable
epc8226spPowerTable = _Epc8226spPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    epc8226spPowerTable.setStatus("current")
_Epc8226spPowerEntry_Object = MibTableRow
epc8226spPowerEntry = _Epc8226spPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1)
)
epc8226spPowerEntry.setIndexNames(
    (0, "GUDEADS-EPC8226-MIB", "epc8226spPowerIndex"),
)
if mibBuilder.loadTexts:
    epc8226spPowerEntry.setStatus("current")


class _Epc8226spPowerIndex_Type(Integer32):
    """Custom type epc8226spPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Epc8226spPowerIndex_Type.__name__ = "Integer32"
_Epc8226spPowerIndex_Object = MibTableColumn
epc8226spPowerIndex = _Epc8226spPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 1),
    _Epc8226spPowerIndex_Type()
)
epc8226spPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spPowerIndex.setStatus("current")


class _Epc8226spChanStatus_Type(Integer32):
    """Custom type epc8226spChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc8226spChanStatus_Type.__name__ = "Integer32"
_Epc8226spChanStatus_Object = MibTableColumn
epc8226spChanStatus = _Epc8226spChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 2),
    _Epc8226spChanStatus_Type()
)
epc8226spChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spChanStatus.setStatus("current")
_Epc8226spAbsEnergyActive_Type = Gauge32
_Epc8226spAbsEnergyActive_Object = MibTableColumn
epc8226spAbsEnergyActive = _Epc8226spAbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 3),
    _Epc8226spAbsEnergyActive_Type()
)
epc8226spAbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spAbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spAbsEnergyActive.setUnits("Wh")
_Epc8226spPowerActive_Type = Integer32
_Epc8226spPowerActive_Object = MibTableColumn
epc8226spPowerActive = _Epc8226spPowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 4),
    _Epc8226spPowerActive_Type()
)
epc8226spPowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spPowerActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spPowerActive.setUnits("W")
_Epc8226spCurrent_Type = Gauge32
_Epc8226spCurrent_Object = MibTableColumn
epc8226spCurrent = _Epc8226spCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 5),
    _Epc8226spCurrent_Type()
)
epc8226spCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spCurrent.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spCurrent.setUnits("mA")
_Epc8226spVoltage_Type = Gauge32
_Epc8226spVoltage_Object = MibTableColumn
epc8226spVoltage = _Epc8226spVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 6),
    _Epc8226spVoltage_Type()
)
epc8226spVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spVoltage.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spVoltage.setUnits("V")
_Epc8226spFrequency_Type = Gauge32
_Epc8226spFrequency_Object = MibTableColumn
epc8226spFrequency = _Epc8226spFrequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 7),
    _Epc8226spFrequency_Type()
)
epc8226spFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spFrequency.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spFrequency.setUnits("0.01 hz")
_Epc8226spPowerFactor_Type = Integer32
_Epc8226spPowerFactor_Object = MibTableColumn
epc8226spPowerFactor = _Epc8226spPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 8),
    _Epc8226spPowerFactor_Type()
)
epc8226spPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spPowerFactor.setUnits("0.001")
_Epc8226spPangle_Type = Integer32
_Epc8226spPangle_Object = MibTableColumn
epc8226spPangle = _Epc8226spPangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 9),
    _Epc8226spPangle_Type()
)
epc8226spPangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spPangle.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spPangle.setUnits("0.1 degree")
_Epc8226spPowerApparent_Type = Integer32
_Epc8226spPowerApparent_Object = MibTableColumn
epc8226spPowerApparent = _Epc8226spPowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 10),
    _Epc8226spPowerApparent_Type()
)
epc8226spPowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spPowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spPowerApparent.setUnits("VA")
_Epc8226spPowerReactive_Type = Integer32
_Epc8226spPowerReactive_Object = MibTableColumn
epc8226spPowerReactive = _Epc8226spPowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 11),
    _Epc8226spPowerReactive_Type()
)
epc8226spPowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spPowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spPowerReactive.setUnits("VAR")
_Epc8226spAbsEnergyReactive_Type = Gauge32
_Epc8226spAbsEnergyReactive_Object = MibTableColumn
epc8226spAbsEnergyReactive = _Epc8226spAbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 12),
    _Epc8226spAbsEnergyReactive_Type()
)
epc8226spAbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spAbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spAbsEnergyReactive.setUnits("VARh")
_Epc8226spAbsEnergyActiveResettable_Type = Gauge32
_Epc8226spAbsEnergyActiveResettable_Object = MibTableColumn
epc8226spAbsEnergyActiveResettable = _Epc8226spAbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 13),
    _Epc8226spAbsEnergyActiveResettable_Type()
)
epc8226spAbsEnergyActiveResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8226spAbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spAbsEnergyActiveResettable.setUnits("Wh")
_Epc8226spAbsEnergyReactiveResettable_Type = Gauge32
_Epc8226spAbsEnergyReactiveResettable_Object = MibTableColumn
epc8226spAbsEnergyReactiveResettable = _Epc8226spAbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 14),
    _Epc8226spAbsEnergyReactiveResettable_Type()
)
epc8226spAbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spAbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spAbsEnergyReactiveResettable.setUnits("VARh")
_Epc8226spResetTime_Type = Gauge32
_Epc8226spResetTime_Object = MibTableColumn
epc8226spResetTime = _Epc8226spResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 15),
    _Epc8226spResetTime_Type()
)
epc8226spResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spResetTime.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spResetTime.setUnits("s")
_Epc8226spForwEnergyActive_Type = Gauge32
_Epc8226spForwEnergyActive_Object = MibTableColumn
epc8226spForwEnergyActive = _Epc8226spForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 16),
    _Epc8226spForwEnergyActive_Type()
)
epc8226spForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spForwEnergyActive.setUnits("Wh")
_Epc8226spForwEnergyReactive_Type = Gauge32
_Epc8226spForwEnergyReactive_Object = MibTableColumn
epc8226spForwEnergyReactive = _Epc8226spForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 17),
    _Epc8226spForwEnergyReactive_Type()
)
epc8226spForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spForwEnergyReactive.setUnits("VARh")
_Epc8226spForwEnergyActiveResettable_Type = Gauge32
_Epc8226spForwEnergyActiveResettable_Object = MibTableColumn
epc8226spForwEnergyActiveResettable = _Epc8226spForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 18),
    _Epc8226spForwEnergyActiveResettable_Type()
)
epc8226spForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spForwEnergyActiveResettable.setUnits("Wh")
_Epc8226spForwEnergyReactiveResettable_Type = Gauge32
_Epc8226spForwEnergyReactiveResettable_Object = MibTableColumn
epc8226spForwEnergyReactiveResettable = _Epc8226spForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 19),
    _Epc8226spForwEnergyReactiveResettable_Type()
)
epc8226spForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spForwEnergyReactiveResettable.setUnits("VARh")
_Epc8226spRevEnergyActive_Type = Gauge32
_Epc8226spRevEnergyActive_Object = MibTableColumn
epc8226spRevEnergyActive = _Epc8226spRevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 20),
    _Epc8226spRevEnergyActive_Type()
)
epc8226spRevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spRevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spRevEnergyActive.setUnits("Wh")
_Epc8226spRevEnergyReactive_Type = Gauge32
_Epc8226spRevEnergyReactive_Object = MibTableColumn
epc8226spRevEnergyReactive = _Epc8226spRevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 21),
    _Epc8226spRevEnergyReactive_Type()
)
epc8226spRevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spRevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spRevEnergyReactive.setUnits("VARh")
_Epc8226spRevEnergyActiveResettable_Type = Gauge32
_Epc8226spRevEnergyActiveResettable_Object = MibTableColumn
epc8226spRevEnergyActiveResettable = _Epc8226spRevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 22),
    _Epc8226spRevEnergyActiveResettable_Type()
)
epc8226spRevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spRevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spRevEnergyActiveResettable.setUnits("Wh")
_Epc8226spRevEnergyReactiveResettable_Type = Gauge32
_Epc8226spRevEnergyReactiveResettable_Object = MibTableColumn
epc8226spRevEnergyReactiveResettable = _Epc8226spRevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 5, 5, 2, 1, 23),
    _Epc8226spRevEnergyReactiveResettable_Type()
)
epc8226spRevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226spRevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8226spRevEnergyReactiveResettable.setUnits("VARh")
_Epc8226ExtSensors_ObjectIdentity = ObjectIdentity
epc8226ExtSensors = _Epc8226ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 6)
)
_Epc8226SensorTable_Object = MibTable
epc8226SensorTable = _Epc8226SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 6, 1)
)
if mibBuilder.loadTexts:
    epc8226SensorTable.setStatus("current")
_Epc8226SensorEntry_Object = MibTableRow
epc8226SensorEntry = _Epc8226SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 6, 1, 1)
)
epc8226SensorEntry.setIndexNames(
    (0, "GUDEADS-EPC8226-MIB", "epc8226SensorIndex"),
)
if mibBuilder.loadTexts:
    epc8226SensorEntry.setStatus("current")


class _Epc8226SensorIndex_Type(Integer32):
    """Custom type epc8226SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Epc8226SensorIndex_Type.__name__ = "Integer32"
_Epc8226SensorIndex_Object = MibTableColumn
epc8226SensorIndex = _Epc8226SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 6, 1, 1, 1),
    _Epc8226SensorIndex_Type()
)
epc8226SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226SensorIndex.setStatus("current")
_Epc8226TempSensor_Type = Integer32
_Epc8226TempSensor_Object = MibTableColumn
epc8226TempSensor = _Epc8226TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 6, 1, 1, 2),
    _Epc8226TempSensor_Type()
)
epc8226TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc8226TempSensor.setUnits("0.1 degree Celsius")
_Epc8226HygroSensor_Type = Integer32
_Epc8226HygroSensor_Object = MibTableColumn
epc8226HygroSensor = _Epc8226HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 6, 1, 1, 3),
    _Epc8226HygroSensor_Type()
)
epc8226HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc8226HygroSensor.setUnits("0.1 percent humidity")


class _Epc8226InputSensor_Type(Integer32):
    """Custom type epc8226InputSensor based on Integer32"""
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


_Epc8226InputSensor_Type.__name__ = "Integer32"
_Epc8226InputSensor_Object = MibTableColumn
epc8226InputSensor = _Epc8226InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 6, 1, 1, 4),
    _Epc8226InputSensor_Type()
)
epc8226InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226InputSensor.setStatus("current")
_Epc8226AirPressure_Type = Integer32
_Epc8226AirPressure_Object = MibTableColumn
epc8226AirPressure = _Epc8226AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 6, 1, 1, 5),
    _Epc8226AirPressure_Type()
)
epc8226AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    epc8226AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Epc8226DewPoint_Type = Integer32
_Epc8226DewPoint_Object = MibTableColumn
epc8226DewPoint = _Epc8226DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 6, 1, 1, 6),
    _Epc8226DewPoint_Type()
)
epc8226DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    epc8226DewPoint.setUnits("0.1 degree Celsius")
_Epc8226DewPointDiff_Type = Integer32
_Epc8226DewPointDiff_Object = MibTableColumn
epc8226DewPointDiff = _Epc8226DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 58, 1, 6, 1, 1, 7),
    _Epc8226DewPointDiff_Type()
)
epc8226DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8226DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    epc8226DewPointDiff.setUnits("0.1 degree Celsius")
_Epc8226Conf_ObjectIdentity = ObjectIdentity
epc8226Conf = _Epc8226Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 2)
)
_Epc8226Groups_ObjectIdentity = ObjectIdentity
epc8226Groups = _Epc8226Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 2, 1)
)
_Epc8226Compls_ObjectIdentity = ObjectIdentity
epc8226Compls = _Epc8226Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 58, 3)
)

# Managed Objects groups

epc8226BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 58, 2, 1, 1)
)
epc8226BasicGroup.setObjects(
      *(("GUDEADS-EPC8226-MIB", "epc8226TrapCtrl"),
        ("GUDEADS-EPC8226-MIB", "epc8226TrapAddr"),
        ("GUDEADS-EPC8226-MIB", "epc8226portNumber"),
        ("GUDEADS-EPC8226-MIB", "epc8226PortName"),
        ("GUDEADS-EPC8226-MIB", "epc8226PortState"),
        ("GUDEADS-EPC8226-MIB", "epc8226PortSwitchCount"),
        ("GUDEADS-EPC8226-MIB", "epc8226PortStartupMode"),
        ("GUDEADS-EPC8226-MIB", "epc8226PortStartupDelay"),
        ("GUDEADS-EPC8226-MIB", "epc8226PortRepowerTime"),
        ("GUDEADS-EPC8226-MIB", "epc8226Buzzer"),
        ("GUDEADS-EPC8226-MIB", "epc8226ActivePowerChan"),
        ("GUDEADS-EPC8226-MIB", "epc8226ChanStatus"),
        ("GUDEADS-EPC8226-MIB", "epc8226AbsEnergyActive"),
        ("GUDEADS-EPC8226-MIB", "epc8226PowerActive"),
        ("GUDEADS-EPC8226-MIB", "epc8226Current"),
        ("GUDEADS-EPC8226-MIB", "epc8226Voltage"),
        ("GUDEADS-EPC8226-MIB", "epc8226Frequency"),
        ("GUDEADS-EPC8226-MIB", "epc8226PowerFactor"),
        ("GUDEADS-EPC8226-MIB", "epc8226Pangle"),
        ("GUDEADS-EPC8226-MIB", "epc8226PowerApparent"),
        ("GUDEADS-EPC8226-MIB", "epc8226PowerReactive"),
        ("GUDEADS-EPC8226-MIB", "epc8226AbsEnergyReactive"),
        ("GUDEADS-EPC8226-MIB", "epc8226AbsEnergyActiveResettable"),
        ("GUDEADS-EPC8226-MIB", "epc8226AbsEnergyReactiveResettable"),
        ("GUDEADS-EPC8226-MIB", "epc8226ResetTime"),
        ("GUDEADS-EPC8226-MIB", "epc8226ForwEnergyActive"),
        ("GUDEADS-EPC8226-MIB", "epc8226ForwEnergyReactive"),
        ("GUDEADS-EPC8226-MIB", "epc8226ForwEnergyActiveResettable"),
        ("GUDEADS-EPC8226-MIB", "epc8226ForwEnergyReactiveResettable"),
        ("GUDEADS-EPC8226-MIB", "epc8226RevEnergyActive"),
        ("GUDEADS-EPC8226-MIB", "epc8226RevEnergyReactive"),
        ("GUDEADS-EPC8226-MIB", "epc8226RevEnergyActiveResettable"),
        ("GUDEADS-EPC8226-MIB", "epc8226RevEnergyReactiveResettable"),
        ("GUDEADS-EPC8226-MIB", "epc8226OVPStatus"),
        ("GUDEADS-EPC8226-MIB", "epc8226spActivePowerChan"),
        ("GUDEADS-EPC8226-MIB", "epc8226spChanStatus"),
        ("GUDEADS-EPC8226-MIB", "epc8226spAbsEnergyActive"),
        ("GUDEADS-EPC8226-MIB", "epc8226spPowerActive"),
        ("GUDEADS-EPC8226-MIB", "epc8226spCurrent"),
        ("GUDEADS-EPC8226-MIB", "epc8226spVoltage"),
        ("GUDEADS-EPC8226-MIB", "epc8226spFrequency"),
        ("GUDEADS-EPC8226-MIB", "epc8226spPowerFactor"),
        ("GUDEADS-EPC8226-MIB", "epc8226spPangle"),
        ("GUDEADS-EPC8226-MIB", "epc8226spPowerApparent"),
        ("GUDEADS-EPC8226-MIB", "epc8226spPowerReactive"),
        ("GUDEADS-EPC8226-MIB", "epc8226spAbsEnergyReactive"),
        ("GUDEADS-EPC8226-MIB", "epc8226spAbsEnergyActiveResettable"),
        ("GUDEADS-EPC8226-MIB", "epc8226spAbsEnergyReactiveResettable"),
        ("GUDEADS-EPC8226-MIB", "epc8226spResetTime"),
        ("GUDEADS-EPC8226-MIB", "epc8226spForwEnergyActive"),
        ("GUDEADS-EPC8226-MIB", "epc8226spForwEnergyReactive"),
        ("GUDEADS-EPC8226-MIB", "epc8226spForwEnergyActiveResettable"),
        ("GUDEADS-EPC8226-MIB", "epc8226spForwEnergyReactiveResettable"),
        ("GUDEADS-EPC8226-MIB", "epc8226spRevEnergyActive"),
        ("GUDEADS-EPC8226-MIB", "epc8226spRevEnergyReactive"),
        ("GUDEADS-EPC8226-MIB", "epc8226spRevEnergyActiveResettable"),
        ("GUDEADS-EPC8226-MIB", "epc8226spRevEnergyReactiveResettable"),
        ("GUDEADS-EPC8226-MIB", "epc8226TempSensor"),
        ("GUDEADS-EPC8226-MIB", "epc8226HygroSensor"),
        ("GUDEADS-EPC8226-MIB", "epc8226InputSensor"),
        ("GUDEADS-EPC8226-MIB", "epc8226TrapIPIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226PortIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226PowerIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226OVPIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226spPowerIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226SensorIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226AirPressure"),
        ("GUDEADS-EPC8226-MIB", "epc8226DewPoint"),
        ("GUDEADS-EPC8226-MIB", "epc8226DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc8226BasicGroup.setStatus("current")


# Notification objects

epc8226SwitchEvtPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 58, 3, 1)
)
epc8226SwitchEvtPort.setObjects(
      *(("GUDEADS-EPC8226-MIB", "epc8226PortIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226PortName"),
        ("GUDEADS-EPC8226-MIB", "epc8226PortState"),
        ("GUDEADS-EPC8226-MIB", "epc8226PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc8226SwitchEvtPort.setStatus(
        "current"
    )

epc8226TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 58, 3, 2)
)
epc8226TempEvtSen.setObjects(
      *(("GUDEADS-EPC8226-MIB", "epc8226SensorIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226TempSensor"))
)
if mibBuilder.loadTexts:
    epc8226TempEvtSen.setStatus(
        "current"
    )

epc8226HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 58, 3, 3)
)
epc8226HygroEvtSen.setObjects(
      *(("GUDEADS-EPC8226-MIB", "epc8226SensorIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226HygroSensor"))
)
if mibBuilder.loadTexts:
    epc8226HygroEvtSen.setStatus(
        "current"
    )

epc8226InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 58, 3, 4)
)
epc8226InputEvtSen.setObjects(
      *(("GUDEADS-EPC8226-MIB", "epc8226SensorIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226InputSensor"))
)
if mibBuilder.loadTexts:
    epc8226InputEvtSen.setStatus(
        "current"
    )

epc8226AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 58, 3, 5)
)
epc8226AirPressureEvtSen.setObjects(
      *(("GUDEADS-EPC8226-MIB", "epc8226SensorIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226AirPressure"))
)
if mibBuilder.loadTexts:
    epc8226AirPressureEvtSen.setStatus(
        "current"
    )

epc8226DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 58, 3, 6)
)
epc8226DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-EPC8226-MIB", "epc8226SensorIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc8226DewPtDiffEvtSen.setStatus(
        "current"
    )

epc8226OVPEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 58, 3, 7)
)
epc8226OVPEvt.setObjects(
      *(("GUDEADS-EPC8226-MIB", "epc8226OVPIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226OVPStatus"))
)
if mibBuilder.loadTexts:
    epc8226OVPEvt.setStatus(
        "current"
    )

epc8226LineAmperageEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 58, 3, 8)
)
epc8226LineAmperageEvt.setObjects(
      *(("GUDEADS-EPC8226-MIB", "epc8226PowerIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226PowerActive"),
        ("GUDEADS-EPC8226-MIB", "epc8226Current"),
        ("GUDEADS-EPC8226-MIB", "epc8226Voltage"),
        ("GUDEADS-EPC8226-MIB", "epc8226Frequency"),
        ("GUDEADS-EPC8226-MIB", "epc8226PowerApparent"),
        ("GUDEADS-EPC8226-MIB", "epc8226PowerReactive"))
)
if mibBuilder.loadTexts:
    epc8226LineAmperageEvt.setStatus(
        "current"
    )

epc8226PortAmperageEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 58, 3, 9)
)
epc8226PortAmperageEvt.setObjects(
      *(("GUDEADS-EPC8226-MIB", "epc8226spPowerIndex"),
        ("GUDEADS-EPC8226-MIB", "epc8226spPowerActive"),
        ("GUDEADS-EPC8226-MIB", "epc8226spCurrent"),
        ("GUDEADS-EPC8226-MIB", "epc8226spVoltage"),
        ("GUDEADS-EPC8226-MIB", "epc8226spFrequency"),
        ("GUDEADS-EPC8226-MIB", "epc8226spPowerApparent"),
        ("GUDEADS-EPC8226-MIB", "epc8226spPowerReactive"))
)
if mibBuilder.loadTexts:
    epc8226PortAmperageEvt.setStatus(
        "current"
    )


# Notifications groups

epc8226NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 58, 2, 1, 2)
)
epc8226NotificationGroup.setObjects(
      *(("GUDEADS-EPC8226-MIB", "epc8226SwitchEvtPort"),
        ("GUDEADS-EPC8226-MIB", "epc8226TempEvtSen"),
        ("GUDEADS-EPC8226-MIB", "epc8226HygroEvtSen"),
        ("GUDEADS-EPC8226-MIB", "epc8226InputEvtSen"),
        ("GUDEADS-EPC8226-MIB", "epc8226AirPressureEvtSen"),
        ("GUDEADS-EPC8226-MIB", "epc8226DewPtDiffEvtSen"),
        ("GUDEADS-EPC8226-MIB", "epc8226OVPEvt"),
        ("GUDEADS-EPC8226-MIB", "epc8226LineAmperageEvt"),
        ("GUDEADS-EPC8226-MIB", "epc8226PortAmperageEvt"))
)
if mibBuilder.loadTexts:
    epc8226NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-EPC8226-MIB",
    **{"gudeads": gudeads,
       "gadsEPC8226": gadsEPC8226,
       "epc8226Objects": epc8226Objects,
       "epc8226CommonConfig": epc8226CommonConfig,
       "epc8226SNMPaccess": epc8226SNMPaccess,
       "epc8226TrapCtrl": epc8226TrapCtrl,
       "epc8226TrapIPTable": epc8226TrapIPTable,
       "epc8226TrapIPEntry": epc8226TrapIPEntry,
       "epc8226TrapIPIndex": epc8226TrapIPIndex,
       "epc8226TrapAddr": epc8226TrapAddr,
       "epc8226DeviceConfig": epc8226DeviceConfig,
       "epc8226IntActors": epc8226IntActors,
       "epc8226relayports": epc8226relayports,
       "epc8226portNumber": epc8226portNumber,
       "epc8226portTable": epc8226portTable,
       "epc8226portEntry": epc8226portEntry,
       "epc8226PortIndex": epc8226PortIndex,
       "epc8226PortName": epc8226PortName,
       "epc8226PortState": epc8226PortState,
       "epc8226PortSwitchCount": epc8226PortSwitchCount,
       "epc8226PortStartupMode": epc8226PortStartupMode,
       "epc8226PortStartupDelay": epc8226PortStartupDelay,
       "epc8226PortRepowerTime": epc8226PortRepowerTime,
       "epc8226Buzzer": epc8226Buzzer,
       "epc8226ExtActors": epc8226ExtActors,
       "epc8226IntSensors": epc8226IntSensors,
       "epc8226PowerChan": epc8226PowerChan,
       "epc8226ActivePowerChan": epc8226ActivePowerChan,
       "epc8226PowerTable": epc8226PowerTable,
       "epc8226PowerEntry": epc8226PowerEntry,
       "epc8226PowerIndex": epc8226PowerIndex,
       "epc8226ChanStatus": epc8226ChanStatus,
       "epc8226AbsEnergyActive": epc8226AbsEnergyActive,
       "epc8226PowerActive": epc8226PowerActive,
       "epc8226Current": epc8226Current,
       "epc8226Voltage": epc8226Voltage,
       "epc8226Frequency": epc8226Frequency,
       "epc8226PowerFactor": epc8226PowerFactor,
       "epc8226Pangle": epc8226Pangle,
       "epc8226PowerApparent": epc8226PowerApparent,
       "epc8226PowerReactive": epc8226PowerReactive,
       "epc8226AbsEnergyReactive": epc8226AbsEnergyReactive,
       "epc8226AbsEnergyActiveResettable": epc8226AbsEnergyActiveResettable,
       "epc8226AbsEnergyReactiveResettable": epc8226AbsEnergyReactiveResettable,
       "epc8226ResetTime": epc8226ResetTime,
       "epc8226ForwEnergyActive": epc8226ForwEnergyActive,
       "epc8226ForwEnergyReactive": epc8226ForwEnergyReactive,
       "epc8226ForwEnergyActiveResettable": epc8226ForwEnergyActiveResettable,
       "epc8226ForwEnergyReactiveResettable": epc8226ForwEnergyReactiveResettable,
       "epc8226RevEnergyActive": epc8226RevEnergyActive,
       "epc8226RevEnergyReactive": epc8226RevEnergyReactive,
       "epc8226RevEnergyActiveResettable": epc8226RevEnergyActiveResettable,
       "epc8226RevEnergyReactiveResettable": epc8226RevEnergyReactiveResettable,
       "epc8226OVPTable": epc8226OVPTable,
       "epc8226OVPEntry": epc8226OVPEntry,
       "epc8226OVPIndex": epc8226OVPIndex,
       "epc8226OVPStatus": epc8226OVPStatus,
       "epc8226SinglePortPowerChan": epc8226SinglePortPowerChan,
       "epc8226spActivePowerChan": epc8226spActivePowerChan,
       "epc8226spPowerTable": epc8226spPowerTable,
       "epc8226spPowerEntry": epc8226spPowerEntry,
       "epc8226spPowerIndex": epc8226spPowerIndex,
       "epc8226spChanStatus": epc8226spChanStatus,
       "epc8226spAbsEnergyActive": epc8226spAbsEnergyActive,
       "epc8226spPowerActive": epc8226spPowerActive,
       "epc8226spCurrent": epc8226spCurrent,
       "epc8226spVoltage": epc8226spVoltage,
       "epc8226spFrequency": epc8226spFrequency,
       "epc8226spPowerFactor": epc8226spPowerFactor,
       "epc8226spPangle": epc8226spPangle,
       "epc8226spPowerApparent": epc8226spPowerApparent,
       "epc8226spPowerReactive": epc8226spPowerReactive,
       "epc8226spAbsEnergyReactive": epc8226spAbsEnergyReactive,
       "epc8226spAbsEnergyActiveResettable": epc8226spAbsEnergyActiveResettable,
       "epc8226spAbsEnergyReactiveResettable": epc8226spAbsEnergyReactiveResettable,
       "epc8226spResetTime": epc8226spResetTime,
       "epc8226spForwEnergyActive": epc8226spForwEnergyActive,
       "epc8226spForwEnergyReactive": epc8226spForwEnergyReactive,
       "epc8226spForwEnergyActiveResettable": epc8226spForwEnergyActiveResettable,
       "epc8226spForwEnergyReactiveResettable": epc8226spForwEnergyReactiveResettable,
       "epc8226spRevEnergyActive": epc8226spRevEnergyActive,
       "epc8226spRevEnergyReactive": epc8226spRevEnergyReactive,
       "epc8226spRevEnergyActiveResettable": epc8226spRevEnergyActiveResettable,
       "epc8226spRevEnergyReactiveResettable": epc8226spRevEnergyReactiveResettable,
       "epc8226ExtSensors": epc8226ExtSensors,
       "epc8226SensorTable": epc8226SensorTable,
       "epc8226SensorEntry": epc8226SensorEntry,
       "epc8226SensorIndex": epc8226SensorIndex,
       "epc8226TempSensor": epc8226TempSensor,
       "epc8226HygroSensor": epc8226HygroSensor,
       "epc8226InputSensor": epc8226InputSensor,
       "epc8226AirPressure": epc8226AirPressure,
       "epc8226DewPoint": epc8226DewPoint,
       "epc8226DewPointDiff": epc8226DewPointDiff,
       "epc8226Conf": epc8226Conf,
       "epc8226Groups": epc8226Groups,
       "epc8226BasicGroup": epc8226BasicGroup,
       "epc8226NotificationGroup": epc8226NotificationGroup,
       "epc8226Compls": epc8226Compls,
       "events": events,
       "epc8226SwitchEvtPort": epc8226SwitchEvtPort,
       "epc8226TempEvtSen": epc8226TempEvtSen,
       "epc8226HygroEvtSen": epc8226HygroEvtSen,
       "epc8226InputEvtSen": epc8226InputEvtSen,
       "epc8226AirPressureEvtSen": epc8226AirPressureEvtSen,
       "epc8226DewPtDiffEvtSen": epc8226DewPtDiffEvtSen,
       "epc8226OVPEvt": epc8226OVPEvt,
       "epc8226LineAmperageEvt": epc8226LineAmperageEvt,
       "epc8226PortAmperageEvt": epc8226PortAmperageEvt}
)
