# SNMP MIB module (GUDEADS-EPC8316-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-EPC8316-MIB.mib
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

_GadsEPC8316_ObjectIdentity = ObjectIdentity
gadsEPC8316 = _GadsEPC8316_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64)
)
_Epc8316Objects_ObjectIdentity = ObjectIdentity
epc8316Objects = _Epc8316Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1)
)
_Epc8316CommonConfig_ObjectIdentity = ObjectIdentity
epc8316CommonConfig = _Epc8316CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 1)
)
_Epc8316SNMPaccess_ObjectIdentity = ObjectIdentity
epc8316SNMPaccess = _Epc8316SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 1, 1)
)


class _Epc8316TrapCtrl_Type(Integer32):
    """Custom type epc8316TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Epc8316TrapCtrl_Type.__name__ = "Integer32"
_Epc8316TrapCtrl_Object = MibScalar
epc8316TrapCtrl = _Epc8316TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 1, 1, 1),
    _Epc8316TrapCtrl_Type()
)
epc8316TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8316TrapCtrl.setStatus("current")
_Epc8316TrapIPTable_Object = MibTable
epc8316TrapIPTable = _Epc8316TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    epc8316TrapIPTable.setStatus("current")
_Epc8316TrapIPEntry_Object = MibTableRow
epc8316TrapIPEntry = _Epc8316TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 1, 1, 2, 1)
)
epc8316TrapIPEntry.setIndexNames(
    (0, "GUDEADS-EPC8316-MIB", "epc8316TrapIPIndex"),
)
if mibBuilder.loadTexts:
    epc8316TrapIPEntry.setStatus("current")


class _Epc8316TrapIPIndex_Type(Integer32):
    """Custom type epc8316TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc8316TrapIPIndex_Type.__name__ = "Integer32"
_Epc8316TrapIPIndex_Object = MibTableColumn
epc8316TrapIPIndex = _Epc8316TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 1, 1, 2, 1, 1),
    _Epc8316TrapIPIndex_Type()
)
epc8316TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316TrapIPIndex.setStatus("current")


class _Epc8316TrapAddr_Type(OctetString):
    """Custom type epc8316TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Epc8316TrapAddr_Type.__name__ = "OctetString"
_Epc8316TrapAddr_Object = MibTableColumn
epc8316TrapAddr = _Epc8316TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 1, 1, 2, 1, 2),
    _Epc8316TrapAddr_Type()
)
epc8316TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8316TrapAddr.setStatus("current")
_Epc8316DeviceConfig_ObjectIdentity = ObjectIdentity
epc8316DeviceConfig = _Epc8316DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 2)
)
_Epc8316IntActors_ObjectIdentity = ObjectIdentity
epc8316IntActors = _Epc8316IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 3)
)
_Epc8316relayports_ObjectIdentity = ObjectIdentity
epc8316relayports = _Epc8316relayports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 3, 1)
)


class _Epc8316portNumber_Type(Integer32):
    """Custom type epc8316portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Epc8316portNumber_Type.__name__ = "Integer32"
_Epc8316portNumber_Object = MibScalar
epc8316portNumber = _Epc8316portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 3, 1, 1),
    _Epc8316portNumber_Type()
)
epc8316portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316portNumber.setStatus("current")
_Epc8316portTable_Object = MibTable
epc8316portTable = _Epc8316portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    epc8316portTable.setStatus("current")
_Epc8316portEntry_Object = MibTableRow
epc8316portEntry = _Epc8316portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 3, 1, 2, 1)
)
epc8316portEntry.setIndexNames(
    (0, "GUDEADS-EPC8316-MIB", "epc8316PortIndex"),
)
if mibBuilder.loadTexts:
    epc8316portEntry.setStatus("current")


class _Epc8316PortIndex_Type(Integer32):
    """Custom type epc8316PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc8316PortIndex_Type.__name__ = "Integer32"
_Epc8316PortIndex_Object = MibTableColumn
epc8316PortIndex = _Epc8316PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 3, 1, 2, 1, 1),
    _Epc8316PortIndex_Type()
)
epc8316PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316PortIndex.setStatus("current")


class _Epc8316PortName_Type(OctetString):
    """Custom type epc8316PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Epc8316PortName_Type.__name__ = "OctetString"
_Epc8316PortName_Object = MibTableColumn
epc8316PortName = _Epc8316PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 3, 1, 2, 1, 2),
    _Epc8316PortName_Type()
)
epc8316PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8316PortName.setStatus("current")


class _Epc8316PortState_Type(Integer32):
    """Custom type epc8316PortState based on Integer32"""
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


_Epc8316PortState_Type.__name__ = "Integer32"
_Epc8316PortState_Object = MibTableColumn
epc8316PortState = _Epc8316PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 3, 1, 2, 1, 3),
    _Epc8316PortState_Type()
)
epc8316PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8316PortState.setStatus("current")
_Epc8316PortSwitchCount_Type = Integer32
_Epc8316PortSwitchCount_Object = MibTableColumn
epc8316PortSwitchCount = _Epc8316PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 3, 1, 2, 1, 4),
    _Epc8316PortSwitchCount_Type()
)
epc8316PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316PortSwitchCount.setStatus("current")


class _Epc8316PortStartupMode_Type(Integer32):
    """Custom type epc8316PortStartupMode based on Integer32"""
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


_Epc8316PortStartupMode_Type.__name__ = "Integer32"
_Epc8316PortStartupMode_Object = MibTableColumn
epc8316PortStartupMode = _Epc8316PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 3, 1, 2, 1, 5),
    _Epc8316PortStartupMode_Type()
)
epc8316PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8316PortStartupMode.setStatus("current")


class _Epc8316PortStartupDelay_Type(Integer32):
    """Custom type epc8316PortStartupDelay based on Integer32"""
    defaultValue = 0


_Epc8316PortStartupDelay_Type.__name__ = "Integer32"
_Epc8316PortStartupDelay_Object = MibTableColumn
epc8316PortStartupDelay = _Epc8316PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 3, 1, 2, 1, 6),
    _Epc8316PortStartupDelay_Type()
)
epc8316PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8316PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    epc8316PortStartupDelay.setUnits("seconds")


class _Epc8316PortRepowerTime_Type(Integer32):
    """Custom type epc8316PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Epc8316PortRepowerTime_Type.__name__ = "Integer32"
_Epc8316PortRepowerTime_Object = MibTableColumn
epc8316PortRepowerTime = _Epc8316PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 3, 1, 2, 1, 7),
    _Epc8316PortRepowerTime_Type()
)
epc8316PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8316PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    epc8316PortRepowerTime.setUnits("seconds")
_Epc8316ExtActors_ObjectIdentity = ObjectIdentity
epc8316ExtActors = _Epc8316ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 4)
)
_Epc8316IntSensors_ObjectIdentity = ObjectIdentity
epc8316IntSensors = _Epc8316IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5)
)
_Epc8316PowerChan_ObjectIdentity = ObjectIdentity
epc8316PowerChan = _Epc8316PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1)
)


class _Epc8316ActivePowerChan_Type(Unsigned32):
    """Custom type epc8316ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc8316ActivePowerChan_Type.__name__ = "Unsigned32"
_Epc8316ActivePowerChan_Object = MibScalar
epc8316ActivePowerChan = _Epc8316ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 1),
    _Epc8316ActivePowerChan_Type()
)
epc8316ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316ActivePowerChan.setStatus("current")
_Epc8316PowerTable_Object = MibTable
epc8316PowerTable = _Epc8316PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    epc8316PowerTable.setStatus("current")
_Epc8316PowerEntry_Object = MibTableRow
epc8316PowerEntry = _Epc8316PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1)
)
epc8316PowerEntry.setIndexNames(
    (0, "GUDEADS-EPC8316-MIB", "epc8316PowerIndex"),
)
if mibBuilder.loadTexts:
    epc8316PowerEntry.setStatus("current")


class _Epc8316PowerIndex_Type(Integer32):
    """Custom type epc8316PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Epc8316PowerIndex_Type.__name__ = "Integer32"
_Epc8316PowerIndex_Object = MibTableColumn
epc8316PowerIndex = _Epc8316PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 1),
    _Epc8316PowerIndex_Type()
)
epc8316PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316PowerIndex.setStatus("current")


class _Epc8316ChanStatus_Type(Integer32):
    """Custom type epc8316ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc8316ChanStatus_Type.__name__ = "Integer32"
_Epc8316ChanStatus_Object = MibTableColumn
epc8316ChanStatus = _Epc8316ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 2),
    _Epc8316ChanStatus_Type()
)
epc8316ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316ChanStatus.setStatus("current")
_Epc8316AbsEnergyActive_Type = Unsigned32
_Epc8316AbsEnergyActive_Object = MibTableColumn
epc8316AbsEnergyActive = _Epc8316AbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 3),
    _Epc8316AbsEnergyActive_Type()
)
epc8316AbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316AbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316AbsEnergyActive.setUnits("Wh")
_Epc8316PowerActive_Type = Integer32
_Epc8316PowerActive_Object = MibTableColumn
epc8316PowerActive = _Epc8316PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 4),
    _Epc8316PowerActive_Type()
)
epc8316PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316PowerActive.setUnits("W")
_Epc8316Current_Type = Unsigned32
_Epc8316Current_Object = MibTableColumn
epc8316Current = _Epc8316Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 5),
    _Epc8316Current_Type()
)
epc8316Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316Current.setStatus("current")
if mibBuilder.loadTexts:
    epc8316Current.setUnits("mA")
_Epc8316Voltage_Type = Unsigned32
_Epc8316Voltage_Object = MibTableColumn
epc8316Voltage = _Epc8316Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 6),
    _Epc8316Voltage_Type()
)
epc8316Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316Voltage.setStatus("current")
if mibBuilder.loadTexts:
    epc8316Voltage.setUnits("V")
_Epc8316Frequency_Type = Unsigned32
_Epc8316Frequency_Object = MibTableColumn
epc8316Frequency = _Epc8316Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 7),
    _Epc8316Frequency_Type()
)
epc8316Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316Frequency.setStatus("current")
if mibBuilder.loadTexts:
    epc8316Frequency.setUnits("0.01 hz")
_Epc8316PowerFactor_Type = Integer32
_Epc8316PowerFactor_Object = MibTableColumn
epc8316PowerFactor = _Epc8316PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 8),
    _Epc8316PowerFactor_Type()
)
epc8316PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    epc8316PowerFactor.setUnits("0.001")
_Epc8316Pangle_Type = Integer32
_Epc8316Pangle_Object = MibTableColumn
epc8316Pangle = _Epc8316Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 9),
    _Epc8316Pangle_Type()
)
epc8316Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316Pangle.setStatus("current")
if mibBuilder.loadTexts:
    epc8316Pangle.setUnits("0.1 degree")
_Epc8316PowerApparent_Type = Integer32
_Epc8316PowerApparent_Object = MibTableColumn
epc8316PowerApparent = _Epc8316PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 10),
    _Epc8316PowerApparent_Type()
)
epc8316PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    epc8316PowerApparent.setUnits("VA")
_Epc8316PowerReactive_Type = Integer32
_Epc8316PowerReactive_Object = MibTableColumn
epc8316PowerReactive = _Epc8316PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 11),
    _Epc8316PowerReactive_Type()
)
epc8316PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316PowerReactive.setUnits("VAR")
_Epc8316AbsEnergyReactive_Type = Unsigned32
_Epc8316AbsEnergyReactive_Object = MibTableColumn
epc8316AbsEnergyReactive = _Epc8316AbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 12),
    _Epc8316AbsEnergyReactive_Type()
)
epc8316AbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316AbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316AbsEnergyReactive.setUnits("VARh")
_Epc8316AbsEnergyActiveResettable_Type = Unsigned32
_Epc8316AbsEnergyActiveResettable_Object = MibTableColumn
epc8316AbsEnergyActiveResettable = _Epc8316AbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 13),
    _Epc8316AbsEnergyActiveResettable_Type()
)
epc8316AbsEnergyActiveResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8316AbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8316AbsEnergyActiveResettable.setUnits("Wh")
_Epc8316AbsEnergyReactiveResettable_Type = Unsigned32
_Epc8316AbsEnergyReactiveResettable_Object = MibTableColumn
epc8316AbsEnergyReactiveResettable = _Epc8316AbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 14),
    _Epc8316AbsEnergyReactiveResettable_Type()
)
epc8316AbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316AbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8316AbsEnergyReactiveResettable.setUnits("VARh")
_Epc8316ResetTime_Type = Unsigned32
_Epc8316ResetTime_Object = MibTableColumn
epc8316ResetTime = _Epc8316ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 15),
    _Epc8316ResetTime_Type()
)
epc8316ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    epc8316ResetTime.setUnits("s")
_Epc8316ForwEnergyActive_Type = Unsigned32
_Epc8316ForwEnergyActive_Object = MibTableColumn
epc8316ForwEnergyActive = _Epc8316ForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 16),
    _Epc8316ForwEnergyActive_Type()
)
epc8316ForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316ForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316ForwEnergyActive.setUnits("Wh")
_Epc8316ForwEnergyReactive_Type = Unsigned32
_Epc8316ForwEnergyReactive_Object = MibTableColumn
epc8316ForwEnergyReactive = _Epc8316ForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 17),
    _Epc8316ForwEnergyReactive_Type()
)
epc8316ForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316ForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316ForwEnergyReactive.setUnits("VARh")
_Epc8316ForwEnergyActiveResettable_Type = Unsigned32
_Epc8316ForwEnergyActiveResettable_Object = MibTableColumn
epc8316ForwEnergyActiveResettable = _Epc8316ForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 18),
    _Epc8316ForwEnergyActiveResettable_Type()
)
epc8316ForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316ForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8316ForwEnergyActiveResettable.setUnits("Wh")
_Epc8316ForwEnergyReactiveResettable_Type = Unsigned32
_Epc8316ForwEnergyReactiveResettable_Object = MibTableColumn
epc8316ForwEnergyReactiveResettable = _Epc8316ForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 19),
    _Epc8316ForwEnergyReactiveResettable_Type()
)
epc8316ForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316ForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8316ForwEnergyReactiveResettable.setUnits("VARh")
_Epc8316RevEnergyActive_Type = Unsigned32
_Epc8316RevEnergyActive_Object = MibTableColumn
epc8316RevEnergyActive = _Epc8316RevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 20),
    _Epc8316RevEnergyActive_Type()
)
epc8316RevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316RevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316RevEnergyActive.setUnits("Wh")
_Epc8316RevEnergyReactive_Type = Unsigned32
_Epc8316RevEnergyReactive_Object = MibTableColumn
epc8316RevEnergyReactive = _Epc8316RevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 21),
    _Epc8316RevEnergyReactive_Type()
)
epc8316RevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316RevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316RevEnergyReactive.setUnits("VARh")
_Epc8316RevEnergyActiveResettable_Type = Unsigned32
_Epc8316RevEnergyActiveResettable_Object = MibTableColumn
epc8316RevEnergyActiveResettable = _Epc8316RevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 22),
    _Epc8316RevEnergyActiveResettable_Type()
)
epc8316RevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316RevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8316RevEnergyActiveResettable.setUnits("Wh")
_Epc8316RevEnergyReactiveResettable_Type = Unsigned32
_Epc8316RevEnergyReactiveResettable_Object = MibTableColumn
epc8316RevEnergyReactiveResettable = _Epc8316RevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 1, 2, 1, 23),
    _Epc8316RevEnergyReactiveResettable_Type()
)
epc8316RevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316RevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8316RevEnergyReactiveResettable.setUnits("VARh")
_Epc8316SinglePortPowerChan_ObjectIdentity = ObjectIdentity
epc8316SinglePortPowerChan = _Epc8316SinglePortPowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5)
)


class _Epc8316spActivePowerChan_Type(Unsigned32):
    """Custom type epc8316spActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc8316spActivePowerChan_Type.__name__ = "Unsigned32"
_Epc8316spActivePowerChan_Object = MibScalar
epc8316spActivePowerChan = _Epc8316spActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 1),
    _Epc8316spActivePowerChan_Type()
)
epc8316spActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spActivePowerChan.setStatus("current")
_Epc8316spPowerTable_Object = MibTable
epc8316spPowerTable = _Epc8316spPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    epc8316spPowerTable.setStatus("current")
_Epc8316spPowerEntry_Object = MibTableRow
epc8316spPowerEntry = _Epc8316spPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1)
)
epc8316spPowerEntry.setIndexNames(
    (0, "GUDEADS-EPC8316-MIB", "epc8316spPowerIndex"),
)
if mibBuilder.loadTexts:
    epc8316spPowerEntry.setStatus("current")


class _Epc8316spPowerIndex_Type(Integer32):
    """Custom type epc8316spPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc8316spPowerIndex_Type.__name__ = "Integer32"
_Epc8316spPowerIndex_Object = MibTableColumn
epc8316spPowerIndex = _Epc8316spPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 1),
    _Epc8316spPowerIndex_Type()
)
epc8316spPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spPowerIndex.setStatus("current")


class _Epc8316spChanStatus_Type(Integer32):
    """Custom type epc8316spChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Epc8316spChanStatus_Type.__name__ = "Integer32"
_Epc8316spChanStatus_Object = MibTableColumn
epc8316spChanStatus = _Epc8316spChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 2),
    _Epc8316spChanStatus_Type()
)
epc8316spChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spChanStatus.setStatus("current")
_Epc8316spAbsEnergyActive_Type = Unsigned32
_Epc8316spAbsEnergyActive_Object = MibTableColumn
epc8316spAbsEnergyActive = _Epc8316spAbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 3),
    _Epc8316spAbsEnergyActive_Type()
)
epc8316spAbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spAbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spAbsEnergyActive.setUnits("Wh")
_Epc8316spPowerActive_Type = Integer32
_Epc8316spPowerActive_Object = MibTableColumn
epc8316spPowerActive = _Epc8316spPowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 4),
    _Epc8316spPowerActive_Type()
)
epc8316spPowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spPowerActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spPowerActive.setUnits("W")
_Epc8316spCurrent_Type = Unsigned32
_Epc8316spCurrent_Object = MibTableColumn
epc8316spCurrent = _Epc8316spCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 5),
    _Epc8316spCurrent_Type()
)
epc8316spCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spCurrent.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spCurrent.setUnits("mA")
_Epc8316spVoltage_Type = Unsigned32
_Epc8316spVoltage_Object = MibTableColumn
epc8316spVoltage = _Epc8316spVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 6),
    _Epc8316spVoltage_Type()
)
epc8316spVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spVoltage.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spVoltage.setUnits("V")
_Epc8316spFrequency_Type = Unsigned32
_Epc8316spFrequency_Object = MibTableColumn
epc8316spFrequency = _Epc8316spFrequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 7),
    _Epc8316spFrequency_Type()
)
epc8316spFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spFrequency.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spFrequency.setUnits("0.01 hz")
_Epc8316spPowerFactor_Type = Integer32
_Epc8316spPowerFactor_Object = MibTableColumn
epc8316spPowerFactor = _Epc8316spPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 8),
    _Epc8316spPowerFactor_Type()
)
epc8316spPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spPowerFactor.setUnits("0.001")
_Epc8316spPangle_Type = Integer32
_Epc8316spPangle_Object = MibTableColumn
epc8316spPangle = _Epc8316spPangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 9),
    _Epc8316spPangle_Type()
)
epc8316spPangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spPangle.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spPangle.setUnits("0.1 degree")
_Epc8316spPowerApparent_Type = Integer32
_Epc8316spPowerApparent_Object = MibTableColumn
epc8316spPowerApparent = _Epc8316spPowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 10),
    _Epc8316spPowerApparent_Type()
)
epc8316spPowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spPowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spPowerApparent.setUnits("VA")
_Epc8316spPowerReactive_Type = Integer32
_Epc8316spPowerReactive_Object = MibTableColumn
epc8316spPowerReactive = _Epc8316spPowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 11),
    _Epc8316spPowerReactive_Type()
)
epc8316spPowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spPowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spPowerReactive.setUnits("VAR")
_Epc8316spAbsEnergyReactive_Type = Unsigned32
_Epc8316spAbsEnergyReactive_Object = MibTableColumn
epc8316spAbsEnergyReactive = _Epc8316spAbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 12),
    _Epc8316spAbsEnergyReactive_Type()
)
epc8316spAbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spAbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spAbsEnergyReactive.setUnits("VARh")
_Epc8316spAbsEnergyActiveResettable_Type = Unsigned32
_Epc8316spAbsEnergyActiveResettable_Object = MibTableColumn
epc8316spAbsEnergyActiveResettable = _Epc8316spAbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 13),
    _Epc8316spAbsEnergyActiveResettable_Type()
)
epc8316spAbsEnergyActiveResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8316spAbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spAbsEnergyActiveResettable.setUnits("Wh")
_Epc8316spAbsEnergyReactiveResettable_Type = Unsigned32
_Epc8316spAbsEnergyReactiveResettable_Object = MibTableColumn
epc8316spAbsEnergyReactiveResettable = _Epc8316spAbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 14),
    _Epc8316spAbsEnergyReactiveResettable_Type()
)
epc8316spAbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spAbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spAbsEnergyReactiveResettable.setUnits("VARh")
_Epc8316spResetTime_Type = Unsigned32
_Epc8316spResetTime_Object = MibTableColumn
epc8316spResetTime = _Epc8316spResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 15),
    _Epc8316spResetTime_Type()
)
epc8316spResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spResetTime.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spResetTime.setUnits("s")
_Epc8316spForwEnergyActive_Type = Unsigned32
_Epc8316spForwEnergyActive_Object = MibTableColumn
epc8316spForwEnergyActive = _Epc8316spForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 16),
    _Epc8316spForwEnergyActive_Type()
)
epc8316spForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spForwEnergyActive.setUnits("Wh")
_Epc8316spForwEnergyReactive_Type = Unsigned32
_Epc8316spForwEnergyReactive_Object = MibTableColumn
epc8316spForwEnergyReactive = _Epc8316spForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 17),
    _Epc8316spForwEnergyReactive_Type()
)
epc8316spForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spForwEnergyReactive.setUnits("VARh")
_Epc8316spForwEnergyActiveResettable_Type = Unsigned32
_Epc8316spForwEnergyActiveResettable_Object = MibTableColumn
epc8316spForwEnergyActiveResettable = _Epc8316spForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 18),
    _Epc8316spForwEnergyActiveResettable_Type()
)
epc8316spForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spForwEnergyActiveResettable.setUnits("Wh")
_Epc8316spForwEnergyReactiveResettable_Type = Unsigned32
_Epc8316spForwEnergyReactiveResettable_Object = MibTableColumn
epc8316spForwEnergyReactiveResettable = _Epc8316spForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 19),
    _Epc8316spForwEnergyReactiveResettable_Type()
)
epc8316spForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spForwEnergyReactiveResettable.setUnits("VARh")
_Epc8316spRevEnergyActive_Type = Unsigned32
_Epc8316spRevEnergyActive_Object = MibTableColumn
epc8316spRevEnergyActive = _Epc8316spRevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 20),
    _Epc8316spRevEnergyActive_Type()
)
epc8316spRevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spRevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spRevEnergyActive.setUnits("Wh")
_Epc8316spRevEnergyReactive_Type = Unsigned32
_Epc8316spRevEnergyReactive_Object = MibTableColumn
epc8316spRevEnergyReactive = _Epc8316spRevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 21),
    _Epc8316spRevEnergyReactive_Type()
)
epc8316spRevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spRevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spRevEnergyReactive.setUnits("VARh")
_Epc8316spRevEnergyActiveResettable_Type = Unsigned32
_Epc8316spRevEnergyActiveResettable_Object = MibTableColumn
epc8316spRevEnergyActiveResettable = _Epc8316spRevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 22),
    _Epc8316spRevEnergyActiveResettable_Type()
)
epc8316spRevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spRevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spRevEnergyActiveResettable.setUnits("Wh")
_Epc8316spRevEnergyReactiveResettable_Type = Unsigned32
_Epc8316spRevEnergyReactiveResettable_Object = MibTableColumn
epc8316spRevEnergyReactiveResettable = _Epc8316spRevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 5, 5, 2, 1, 23),
    _Epc8316spRevEnergyReactiveResettable_Type()
)
epc8316spRevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316spRevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    epc8316spRevEnergyReactiveResettable.setUnits("VARh")
_Epc8316ExtSensors_ObjectIdentity = ObjectIdentity
epc8316ExtSensors = _Epc8316ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 6)
)
_Epc8316SensorTable_Object = MibTable
epc8316SensorTable = _Epc8316SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 6, 1)
)
if mibBuilder.loadTexts:
    epc8316SensorTable.setStatus("current")
_Epc8316SensorEntry_Object = MibTableRow
epc8316SensorEntry = _Epc8316SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 6, 1, 1)
)
epc8316SensorEntry.setIndexNames(
    (0, "GUDEADS-EPC8316-MIB", "epc8316SensorIndex"),
)
if mibBuilder.loadTexts:
    epc8316SensorEntry.setStatus("current")


class _Epc8316SensorIndex_Type(Integer32):
    """Custom type epc8316SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Epc8316SensorIndex_Type.__name__ = "Integer32"
_Epc8316SensorIndex_Object = MibTableColumn
epc8316SensorIndex = _Epc8316SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 6, 1, 1, 1),
    _Epc8316SensorIndex_Type()
)
epc8316SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316SensorIndex.setStatus("current")
_Epc8316TempSensor_Type = Integer32
_Epc8316TempSensor_Object = MibTableColumn
epc8316TempSensor = _Epc8316TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 6, 1, 1, 2),
    _Epc8316TempSensor_Type()
)
epc8316TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc8316TempSensor.setUnits("0.1 degree Celsius")
_Epc8316HygroSensor_Type = Integer32
_Epc8316HygroSensor_Object = MibTableColumn
epc8316HygroSensor = _Epc8316HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 6, 1, 1, 3),
    _Epc8316HygroSensor_Type()
)
epc8316HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc8316HygroSensor.setUnits("0.1 percent humidity")


class _Epc8316InputSensor_Type(Integer32):
    """Custom type epc8316InputSensor based on Integer32"""
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


_Epc8316InputSensor_Type.__name__ = "Integer32"
_Epc8316InputSensor_Object = MibTableColumn
epc8316InputSensor = _Epc8316InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 6, 1, 1, 4),
    _Epc8316InputSensor_Type()
)
epc8316InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316InputSensor.setStatus("current")
_Epc8316AirPressure_Type = Integer32
_Epc8316AirPressure_Object = MibTableColumn
epc8316AirPressure = _Epc8316AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 6, 1, 1, 5),
    _Epc8316AirPressure_Type()
)
epc8316AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    epc8316AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Epc8316DewPoint_Type = Integer32
_Epc8316DewPoint_Object = MibTableColumn
epc8316DewPoint = _Epc8316DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 6, 1, 1, 6),
    _Epc8316DewPoint_Type()
)
epc8316DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    epc8316DewPoint.setUnits("0.1 degree Celsius")
_Epc8316DewPointDiff_Type = Integer32
_Epc8316DewPointDiff_Object = MibTableColumn
epc8316DewPointDiff = _Epc8316DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 64, 1, 6, 1, 1, 7),
    _Epc8316DewPointDiff_Type()
)
epc8316DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8316DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    epc8316DewPointDiff.setUnits("0.1 degree Celsius")
_Epc8316Conf_ObjectIdentity = ObjectIdentity
epc8316Conf = _Epc8316Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 2)
)
_Epc8316Groups_ObjectIdentity = ObjectIdentity
epc8316Groups = _Epc8316Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 2, 1)
)
_Epc8316Compls_ObjectIdentity = ObjectIdentity
epc8316Compls = _Epc8316Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 64, 3)
)

# Managed Objects groups

epc8316BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 64, 2, 1, 1)
)
epc8316BasicGroup.setObjects(
      *(("GUDEADS-EPC8316-MIB", "epc8316TrapCtrl"),
        ("GUDEADS-EPC8316-MIB", "epc8316TrapIPIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316TrapAddr"),
        ("GUDEADS-EPC8316-MIB", "epc8316portNumber"),
        ("GUDEADS-EPC8316-MIB", "epc8316PortIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316PortName"),
        ("GUDEADS-EPC8316-MIB", "epc8316PortState"),
        ("GUDEADS-EPC8316-MIB", "epc8316PortSwitchCount"),
        ("GUDEADS-EPC8316-MIB", "epc8316PortStartupMode"),
        ("GUDEADS-EPC8316-MIB", "epc8316PortStartupDelay"),
        ("GUDEADS-EPC8316-MIB", "epc8316PortRepowerTime"),
        ("GUDEADS-EPC8316-MIB", "epc8316ActivePowerChan"),
        ("GUDEADS-EPC8316-MIB", "epc8316PowerIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316ChanStatus"),
        ("GUDEADS-EPC8316-MIB", "epc8316AbsEnergyActive"),
        ("GUDEADS-EPC8316-MIB", "epc8316PowerActive"),
        ("GUDEADS-EPC8316-MIB", "epc8316Current"),
        ("GUDEADS-EPC8316-MIB", "epc8316Voltage"),
        ("GUDEADS-EPC8316-MIB", "epc8316Frequency"),
        ("GUDEADS-EPC8316-MIB", "epc8316PowerFactor"),
        ("GUDEADS-EPC8316-MIB", "epc8316Pangle"),
        ("GUDEADS-EPC8316-MIB", "epc8316PowerApparent"),
        ("GUDEADS-EPC8316-MIB", "epc8316PowerReactive"),
        ("GUDEADS-EPC8316-MIB", "epc8316AbsEnergyReactive"),
        ("GUDEADS-EPC8316-MIB", "epc8316AbsEnergyActiveResettable"),
        ("GUDEADS-EPC8316-MIB", "epc8316AbsEnergyReactiveResettable"),
        ("GUDEADS-EPC8316-MIB", "epc8316ResetTime"),
        ("GUDEADS-EPC8316-MIB", "epc8316ForwEnergyActive"),
        ("GUDEADS-EPC8316-MIB", "epc8316ForwEnergyReactive"),
        ("GUDEADS-EPC8316-MIB", "epc8316ForwEnergyActiveResettable"),
        ("GUDEADS-EPC8316-MIB", "epc8316ForwEnergyReactiveResettable"),
        ("GUDEADS-EPC8316-MIB", "epc8316RevEnergyActive"),
        ("GUDEADS-EPC8316-MIB", "epc8316RevEnergyReactive"),
        ("GUDEADS-EPC8316-MIB", "epc8316RevEnergyActiveResettable"),
        ("GUDEADS-EPC8316-MIB", "epc8316RevEnergyReactiveResettable"),
        ("GUDEADS-EPC8316-MIB", "epc8316spActivePowerChan"),
        ("GUDEADS-EPC8316-MIB", "epc8316spPowerIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316spChanStatus"),
        ("GUDEADS-EPC8316-MIB", "epc8316spAbsEnergyActive"),
        ("GUDEADS-EPC8316-MIB", "epc8316spPowerActive"),
        ("GUDEADS-EPC8316-MIB", "epc8316spCurrent"),
        ("GUDEADS-EPC8316-MIB", "epc8316spVoltage"),
        ("GUDEADS-EPC8316-MIB", "epc8316spFrequency"),
        ("GUDEADS-EPC8316-MIB", "epc8316spPowerFactor"),
        ("GUDEADS-EPC8316-MIB", "epc8316spPangle"),
        ("GUDEADS-EPC8316-MIB", "epc8316spPowerApparent"),
        ("GUDEADS-EPC8316-MIB", "epc8316spPowerReactive"),
        ("GUDEADS-EPC8316-MIB", "epc8316spAbsEnergyReactive"),
        ("GUDEADS-EPC8316-MIB", "epc8316spAbsEnergyActiveResettable"),
        ("GUDEADS-EPC8316-MIB", "epc8316spAbsEnergyReactiveResettable"),
        ("GUDEADS-EPC8316-MIB", "epc8316spResetTime"),
        ("GUDEADS-EPC8316-MIB", "epc8316spForwEnergyActive"),
        ("GUDEADS-EPC8316-MIB", "epc8316spForwEnergyReactive"),
        ("GUDEADS-EPC8316-MIB", "epc8316spForwEnergyActiveResettable"),
        ("GUDEADS-EPC8316-MIB", "epc8316spForwEnergyReactiveResettable"),
        ("GUDEADS-EPC8316-MIB", "epc8316spRevEnergyActive"),
        ("GUDEADS-EPC8316-MIB", "epc8316spRevEnergyReactive"),
        ("GUDEADS-EPC8316-MIB", "epc8316spRevEnergyActiveResettable"),
        ("GUDEADS-EPC8316-MIB", "epc8316spRevEnergyReactiveResettable"),
        ("GUDEADS-EPC8316-MIB", "epc8316SensorIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316TempSensor"),
        ("GUDEADS-EPC8316-MIB", "epc8316HygroSensor"),
        ("GUDEADS-EPC8316-MIB", "epc8316InputSensor"),
        ("GUDEADS-EPC8316-MIB", "epc8316AirPressure"),
        ("GUDEADS-EPC8316-MIB", "epc8316DewPoint"),
        ("GUDEADS-EPC8316-MIB", "epc8316DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc8316BasicGroup.setStatus("current")


# Notification objects

epc8316SwitchEvtPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 64, 3, 1)
)
epc8316SwitchEvtPort.setObjects(
      *(("GUDEADS-EPC8316-MIB", "epc8316PortIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316PortName"),
        ("GUDEADS-EPC8316-MIB", "epc8316PortState"),
        ("GUDEADS-EPC8316-MIB", "epc8316PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc8316SwitchEvtPort.setStatus(
        "current"
    )

epc8316TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 64, 3, 2)
)
epc8316TempEvtSen.setObjects(
      *(("GUDEADS-EPC8316-MIB", "epc8316SensorIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316TempSensor"))
)
if mibBuilder.loadTexts:
    epc8316TempEvtSen.setStatus(
        "current"
    )

epc8316HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 64, 3, 3)
)
epc8316HygroEvtSen.setObjects(
      *(("GUDEADS-EPC8316-MIB", "epc8316SensorIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316HygroSensor"))
)
if mibBuilder.loadTexts:
    epc8316HygroEvtSen.setStatus(
        "current"
    )

epc8316InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 64, 3, 4)
)
epc8316InputEvtSen.setObjects(
      *(("GUDEADS-EPC8316-MIB", "epc8316SensorIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316InputSensor"))
)
if mibBuilder.loadTexts:
    epc8316InputEvtSen.setStatus(
        "current"
    )

epc8316AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 64, 3, 5)
)
epc8316AirPressureEvtSen.setObjects(
      *(("GUDEADS-EPC8316-MIB", "epc8316SensorIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316AirPressure"))
)
if mibBuilder.loadTexts:
    epc8316AirPressureEvtSen.setStatus(
        "current"
    )

epc8316DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 64, 3, 6)
)
epc8316DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-EPC8316-MIB", "epc8316SensorIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316DewPointDiff"))
)
if mibBuilder.loadTexts:
    epc8316DewPtDiffEvtSen.setStatus(
        "current"
    )

epc8316LineAmperageEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 64, 3, 7)
)
epc8316LineAmperageEvt.setObjects(
      *(("GUDEADS-EPC8316-MIB", "epc8316PowerIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316PowerActive"),
        ("GUDEADS-EPC8316-MIB", "epc8316Current"),
        ("GUDEADS-EPC8316-MIB", "epc8316Voltage"),
        ("GUDEADS-EPC8316-MIB", "epc8316Frequency"),
        ("GUDEADS-EPC8316-MIB", "epc8316PowerApparent"),
        ("GUDEADS-EPC8316-MIB", "epc8316PowerReactive"))
)
if mibBuilder.loadTexts:
    epc8316LineAmperageEvt.setStatus(
        "current"
    )

epc8316PortAmperageEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 64, 3, 8)
)
epc8316PortAmperageEvt.setObjects(
      *(("GUDEADS-EPC8316-MIB", "epc8316spPowerIndex"),
        ("GUDEADS-EPC8316-MIB", "epc8316spPowerActive"),
        ("GUDEADS-EPC8316-MIB", "epc8316spCurrent"),
        ("GUDEADS-EPC8316-MIB", "epc8316spVoltage"),
        ("GUDEADS-EPC8316-MIB", "epc8316spFrequency"),
        ("GUDEADS-EPC8316-MIB", "epc8316spPowerApparent"),
        ("GUDEADS-EPC8316-MIB", "epc8316spPowerReactive"))
)
if mibBuilder.loadTexts:
    epc8316PortAmperageEvt.setStatus(
        "current"
    )


# Notifications groups

epc8316NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 64, 2, 1, 2)
)
epc8316NotificationGroup.setObjects(
      *(("GUDEADS-EPC8316-MIB", "epc8316SwitchEvtPort"),
        ("GUDEADS-EPC8316-MIB", "epc8316TempEvtSen"),
        ("GUDEADS-EPC8316-MIB", "epc8316HygroEvtSen"),
        ("GUDEADS-EPC8316-MIB", "epc8316InputEvtSen"),
        ("GUDEADS-EPC8316-MIB", "epc8316AirPressureEvtSen"),
        ("GUDEADS-EPC8316-MIB", "epc8316DewPtDiffEvtSen"),
        ("GUDEADS-EPC8316-MIB", "epc8316LineAmperageEvt"),
        ("GUDEADS-EPC8316-MIB", "epc8316PortAmperageEvt"))
)
if mibBuilder.loadTexts:
    epc8316NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-EPC8316-MIB",
    **{"gudeads": gudeads,
       "gadsEPC8316": gadsEPC8316,
       "epc8316Objects": epc8316Objects,
       "epc8316CommonConfig": epc8316CommonConfig,
       "epc8316SNMPaccess": epc8316SNMPaccess,
       "epc8316TrapCtrl": epc8316TrapCtrl,
       "epc8316TrapIPTable": epc8316TrapIPTable,
       "epc8316TrapIPEntry": epc8316TrapIPEntry,
       "epc8316TrapIPIndex": epc8316TrapIPIndex,
       "epc8316TrapAddr": epc8316TrapAddr,
       "epc8316DeviceConfig": epc8316DeviceConfig,
       "epc8316IntActors": epc8316IntActors,
       "epc8316relayports": epc8316relayports,
       "epc8316portNumber": epc8316portNumber,
       "epc8316portTable": epc8316portTable,
       "epc8316portEntry": epc8316portEntry,
       "epc8316PortIndex": epc8316PortIndex,
       "epc8316PortName": epc8316PortName,
       "epc8316PortState": epc8316PortState,
       "epc8316PortSwitchCount": epc8316PortSwitchCount,
       "epc8316PortStartupMode": epc8316PortStartupMode,
       "epc8316PortStartupDelay": epc8316PortStartupDelay,
       "epc8316PortRepowerTime": epc8316PortRepowerTime,
       "epc8316ExtActors": epc8316ExtActors,
       "epc8316IntSensors": epc8316IntSensors,
       "epc8316PowerChan": epc8316PowerChan,
       "epc8316ActivePowerChan": epc8316ActivePowerChan,
       "epc8316PowerTable": epc8316PowerTable,
       "epc8316PowerEntry": epc8316PowerEntry,
       "epc8316PowerIndex": epc8316PowerIndex,
       "epc8316ChanStatus": epc8316ChanStatus,
       "epc8316AbsEnergyActive": epc8316AbsEnergyActive,
       "epc8316PowerActive": epc8316PowerActive,
       "epc8316Current": epc8316Current,
       "epc8316Voltage": epc8316Voltage,
       "epc8316Frequency": epc8316Frequency,
       "epc8316PowerFactor": epc8316PowerFactor,
       "epc8316Pangle": epc8316Pangle,
       "epc8316PowerApparent": epc8316PowerApparent,
       "epc8316PowerReactive": epc8316PowerReactive,
       "epc8316AbsEnergyReactive": epc8316AbsEnergyReactive,
       "epc8316AbsEnergyActiveResettable": epc8316AbsEnergyActiveResettable,
       "epc8316AbsEnergyReactiveResettable": epc8316AbsEnergyReactiveResettable,
       "epc8316ResetTime": epc8316ResetTime,
       "epc8316ForwEnergyActive": epc8316ForwEnergyActive,
       "epc8316ForwEnergyReactive": epc8316ForwEnergyReactive,
       "epc8316ForwEnergyActiveResettable": epc8316ForwEnergyActiveResettable,
       "epc8316ForwEnergyReactiveResettable": epc8316ForwEnergyReactiveResettable,
       "epc8316RevEnergyActive": epc8316RevEnergyActive,
       "epc8316RevEnergyReactive": epc8316RevEnergyReactive,
       "epc8316RevEnergyActiveResettable": epc8316RevEnergyActiveResettable,
       "epc8316RevEnergyReactiveResettable": epc8316RevEnergyReactiveResettable,
       "epc8316SinglePortPowerChan": epc8316SinglePortPowerChan,
       "epc8316spActivePowerChan": epc8316spActivePowerChan,
       "epc8316spPowerTable": epc8316spPowerTable,
       "epc8316spPowerEntry": epc8316spPowerEntry,
       "epc8316spPowerIndex": epc8316spPowerIndex,
       "epc8316spChanStatus": epc8316spChanStatus,
       "epc8316spAbsEnergyActive": epc8316spAbsEnergyActive,
       "epc8316spPowerActive": epc8316spPowerActive,
       "epc8316spCurrent": epc8316spCurrent,
       "epc8316spVoltage": epc8316spVoltage,
       "epc8316spFrequency": epc8316spFrequency,
       "epc8316spPowerFactor": epc8316spPowerFactor,
       "epc8316spPangle": epc8316spPangle,
       "epc8316spPowerApparent": epc8316spPowerApparent,
       "epc8316spPowerReactive": epc8316spPowerReactive,
       "epc8316spAbsEnergyReactive": epc8316spAbsEnergyReactive,
       "epc8316spAbsEnergyActiveResettable": epc8316spAbsEnergyActiveResettable,
       "epc8316spAbsEnergyReactiveResettable": epc8316spAbsEnergyReactiveResettable,
       "epc8316spResetTime": epc8316spResetTime,
       "epc8316spForwEnergyActive": epc8316spForwEnergyActive,
       "epc8316spForwEnergyReactive": epc8316spForwEnergyReactive,
       "epc8316spForwEnergyActiveResettable": epc8316spForwEnergyActiveResettable,
       "epc8316spForwEnergyReactiveResettable": epc8316spForwEnergyReactiveResettable,
       "epc8316spRevEnergyActive": epc8316spRevEnergyActive,
       "epc8316spRevEnergyReactive": epc8316spRevEnergyReactive,
       "epc8316spRevEnergyActiveResettable": epc8316spRevEnergyActiveResettable,
       "epc8316spRevEnergyReactiveResettable": epc8316spRevEnergyReactiveResettable,
       "epc8316ExtSensors": epc8316ExtSensors,
       "epc8316SensorTable": epc8316SensorTable,
       "epc8316SensorEntry": epc8316SensorEntry,
       "epc8316SensorIndex": epc8316SensorIndex,
       "epc8316TempSensor": epc8316TempSensor,
       "epc8316HygroSensor": epc8316HygroSensor,
       "epc8316InputSensor": epc8316InputSensor,
       "epc8316AirPressure": epc8316AirPressure,
       "epc8316DewPoint": epc8316DewPoint,
       "epc8316DewPointDiff": epc8316DewPointDiff,
       "epc8316Conf": epc8316Conf,
       "epc8316Groups": epc8316Groups,
       "epc8316BasicGroup": epc8316BasicGroup,
       "epc8316NotificationGroup": epc8316NotificationGroup,
       "epc8316Compls": epc8316Compls,
       "events": events,
       "epc8316SwitchEvtPort": epc8316SwitchEvtPort,
       "epc8316TempEvtSen": epc8316TempEvtSen,
       "epc8316HygroEvtSen": epc8316HygroEvtSen,
       "epc8316InputEvtSen": epc8316InputEvtSen,
       "epc8316AirPressureEvtSen": epc8316AirPressureEvtSen,
       "epc8316DewPtDiffEvtSen": epc8316DewPtDiffEvtSen,
       "epc8316LineAmperageEvt": epc8316LineAmperageEvt,
       "epc8316PortAmperageEvt": epc8316PortAmperageEvt}
)
