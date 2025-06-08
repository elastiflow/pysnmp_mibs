# SNMP MIB module (GUDEADS-ETS8801-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-ETS8801-MIB.mib
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
        ("2019-04-04 16:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GadsETS8801_ObjectIdentity = ObjectIdentity
gadsETS8801 = _GadsETS8801_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41)
)
_Ets8801Objects_ObjectIdentity = ObjectIdentity
ets8801Objects = _Ets8801Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1)
)
_Ets8801CommonConfig_ObjectIdentity = ObjectIdentity
ets8801CommonConfig = _Ets8801CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 1)
)
_Ets8801SNMPaccess_ObjectIdentity = ObjectIdentity
ets8801SNMPaccess = _Ets8801SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 1, 1)
)


class _Ets8801TrapCtrl_Type(Integer32):
    """Custom type ets8801TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Ets8801TrapCtrl_Type.__name__ = "Integer32"
_Ets8801TrapCtrl_Object = MibScalar
ets8801TrapCtrl = _Ets8801TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 1, 1, 1),
    _Ets8801TrapCtrl_Type()
)
ets8801TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ets8801TrapCtrl.setStatus("current")
_Ets8801TrapIPTable_Object = MibTable
ets8801TrapIPTable = _Ets8801TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ets8801TrapIPTable.setStatus("current")
_Ets8801TrapIPEntry_Object = MibTableRow
ets8801TrapIPEntry = _Ets8801TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 1, 1, 2, 1)
)
ets8801TrapIPEntry.setIndexNames(
    (0, "GUDEADS-ETS8801-MIB", "ets8801TrapIPIndex"),
)
if mibBuilder.loadTexts:
    ets8801TrapIPEntry.setStatus("current")


class _Ets8801TrapIPIndex_Type(Integer32):
    """Custom type ets8801TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Ets8801TrapIPIndex_Type.__name__ = "Integer32"
_Ets8801TrapIPIndex_Object = MibTableColumn
ets8801TrapIPIndex = _Ets8801TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 1, 1, 2, 1, 1),
    _Ets8801TrapIPIndex_Type()
)
ets8801TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801TrapIPIndex.setStatus("current")


class _Ets8801TrapAddr_Type(OctetString):
    """Custom type ets8801TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Ets8801TrapAddr_Type.__name__ = "OctetString"
_Ets8801TrapAddr_Object = MibTableColumn
ets8801TrapAddr = _Ets8801TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 1, 1, 2, 1, 2),
    _Ets8801TrapAddr_Type()
)
ets8801TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ets8801TrapAddr.setStatus("current")
_Ets8801IntActors_ObjectIdentity = ObjectIdentity
ets8801IntActors = _Ets8801IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 3)
)


class _Ets8801Buzzer_Type(Integer32):
    """Custom type ets8801Buzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ets8801Buzzer_Type.__name__ = "Integer32"
_Ets8801Buzzer_Object = MibScalar
ets8801Buzzer = _Ets8801Buzzer_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 3, 10),
    _Ets8801Buzzer_Type()
)
ets8801Buzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ets8801Buzzer.setStatus("current")
if mibBuilder.loadTexts:
    ets8801Buzzer.setUnits("0 = Off, 1 = On")
_Ets8801IntSensors_ObjectIdentity = ObjectIdentity
ets8801IntSensors = _Ets8801IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5)
)
_Ets8801PowerChan_ObjectIdentity = ObjectIdentity
ets8801PowerChan = _Ets8801PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1)
)


class _Ets8801ActivePowerChan_Type(Unsigned32):
    """Custom type ets8801ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Ets8801ActivePowerChan_Type.__name__ = "Unsigned32"
_Ets8801ActivePowerChan_Object = MibScalar
ets8801ActivePowerChan = _Ets8801ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 1),
    _Ets8801ActivePowerChan_Type()
)
ets8801ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801ActivePowerChan.setStatus("current")
_Ets8801PowerTable_Object = MibTable
ets8801PowerTable = _Ets8801PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ets8801PowerTable.setStatus("current")
_Ets8801PowerEntry_Object = MibTableRow
ets8801PowerEntry = _Ets8801PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1)
)
ets8801PowerEntry.setIndexNames(
    (0, "GUDEADS-ETS8801-MIB", "ets8801PowerIndex"),
)
if mibBuilder.loadTexts:
    ets8801PowerEntry.setStatus("current")


class _Ets8801PowerIndex_Type(Integer32):
    """Custom type ets8801PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Ets8801PowerIndex_Type.__name__ = "Integer32"
_Ets8801PowerIndex_Object = MibTableColumn
ets8801PowerIndex = _Ets8801PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 1),
    _Ets8801PowerIndex_Type()
)
ets8801PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801PowerIndex.setStatus("current")


class _Ets8801ChanStatus_Type(Integer32):
    """Custom type ets8801ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ets8801ChanStatus_Type.__name__ = "Integer32"
_Ets8801ChanStatus_Object = MibTableColumn
ets8801ChanStatus = _Ets8801ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 2),
    _Ets8801ChanStatus_Type()
)
ets8801ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801ChanStatus.setStatus("current")
_Ets8801AbsEnergyActive_Type = Unsigned32
_Ets8801AbsEnergyActive_Object = MibTableColumn
ets8801AbsEnergyActive = _Ets8801AbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 3),
    _Ets8801AbsEnergyActive_Type()
)
ets8801AbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801AbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    ets8801AbsEnergyActive.setUnits("Wh")
_Ets8801PowerActive_Type = Integer32
_Ets8801PowerActive_Object = MibTableColumn
ets8801PowerActive = _Ets8801PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 4),
    _Ets8801PowerActive_Type()
)
ets8801PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    ets8801PowerActive.setUnits("W")
_Ets8801Current_Type = Unsigned32
_Ets8801Current_Object = MibTableColumn
ets8801Current = _Ets8801Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 5),
    _Ets8801Current_Type()
)
ets8801Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801Current.setStatus("current")
if mibBuilder.loadTexts:
    ets8801Current.setUnits("mA")
_Ets8801Voltage_Type = Unsigned32
_Ets8801Voltage_Object = MibTableColumn
ets8801Voltage = _Ets8801Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 6),
    _Ets8801Voltage_Type()
)
ets8801Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801Voltage.setStatus("current")
if mibBuilder.loadTexts:
    ets8801Voltage.setUnits("V")
_Ets8801Frequency_Type = Unsigned32
_Ets8801Frequency_Object = MibTableColumn
ets8801Frequency = _Ets8801Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 7),
    _Ets8801Frequency_Type()
)
ets8801Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801Frequency.setStatus("current")
if mibBuilder.loadTexts:
    ets8801Frequency.setUnits("0.01 hz")
_Ets8801PowerFactor_Type = Integer32
_Ets8801PowerFactor_Object = MibTableColumn
ets8801PowerFactor = _Ets8801PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 8),
    _Ets8801PowerFactor_Type()
)
ets8801PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    ets8801PowerFactor.setUnits("0.001")
_Ets8801Pangle_Type = Integer32
_Ets8801Pangle_Object = MibTableColumn
ets8801Pangle = _Ets8801Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 9),
    _Ets8801Pangle_Type()
)
ets8801Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801Pangle.setStatus("current")
if mibBuilder.loadTexts:
    ets8801Pangle.setUnits("0.1 degree")
_Ets8801PowerApparent_Type = Integer32
_Ets8801PowerApparent_Object = MibTableColumn
ets8801PowerApparent = _Ets8801PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 10),
    _Ets8801PowerApparent_Type()
)
ets8801PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    ets8801PowerApparent.setUnits("VA")
_Ets8801PowerReactive_Type = Integer32
_Ets8801PowerReactive_Object = MibTableColumn
ets8801PowerReactive = _Ets8801PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 11),
    _Ets8801PowerReactive_Type()
)
ets8801PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    ets8801PowerReactive.setUnits("VAR")
_Ets8801AbsEnergyReactive_Type = Unsigned32
_Ets8801AbsEnergyReactive_Object = MibTableColumn
ets8801AbsEnergyReactive = _Ets8801AbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 12),
    _Ets8801AbsEnergyReactive_Type()
)
ets8801AbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801AbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    ets8801AbsEnergyReactive.setUnits("VARh")
_Ets8801AbsEnergyActiveResettable_Type = Unsigned32
_Ets8801AbsEnergyActiveResettable_Object = MibTableColumn
ets8801AbsEnergyActiveResettable = _Ets8801AbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 13),
    _Ets8801AbsEnergyActiveResettable_Type()
)
ets8801AbsEnergyActiveResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ets8801AbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    ets8801AbsEnergyActiveResettable.setUnits("Wh")
_Ets8801AbsEnergyReactiveResettable_Type = Unsigned32
_Ets8801AbsEnergyReactiveResettable_Object = MibTableColumn
ets8801AbsEnergyReactiveResettable = _Ets8801AbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 14),
    _Ets8801AbsEnergyReactiveResettable_Type()
)
ets8801AbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801AbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    ets8801AbsEnergyReactiveResettable.setUnits("VARh")
_Ets8801ResetTime_Type = Unsigned32
_Ets8801ResetTime_Object = MibTableColumn
ets8801ResetTime = _Ets8801ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 15),
    _Ets8801ResetTime_Type()
)
ets8801ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    ets8801ResetTime.setUnits("s")
_Ets8801ForwEnergyActive_Type = Unsigned32
_Ets8801ForwEnergyActive_Object = MibTableColumn
ets8801ForwEnergyActive = _Ets8801ForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 16),
    _Ets8801ForwEnergyActive_Type()
)
ets8801ForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801ForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    ets8801ForwEnergyActive.setUnits("Wh")
_Ets8801ForwEnergyReactive_Type = Unsigned32
_Ets8801ForwEnergyReactive_Object = MibTableColumn
ets8801ForwEnergyReactive = _Ets8801ForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 17),
    _Ets8801ForwEnergyReactive_Type()
)
ets8801ForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801ForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    ets8801ForwEnergyReactive.setUnits("VARh")
_Ets8801ForwEnergyActiveResettable_Type = Unsigned32
_Ets8801ForwEnergyActiveResettable_Object = MibTableColumn
ets8801ForwEnergyActiveResettable = _Ets8801ForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 18),
    _Ets8801ForwEnergyActiveResettable_Type()
)
ets8801ForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801ForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    ets8801ForwEnergyActiveResettable.setUnits("Wh")
_Ets8801ForwEnergyReactiveResettable_Type = Unsigned32
_Ets8801ForwEnergyReactiveResettable_Object = MibTableColumn
ets8801ForwEnergyReactiveResettable = _Ets8801ForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 19),
    _Ets8801ForwEnergyReactiveResettable_Type()
)
ets8801ForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801ForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    ets8801ForwEnergyReactiveResettable.setUnits("VARh")
_Ets8801RevEnergyActive_Type = Unsigned32
_Ets8801RevEnergyActive_Object = MibTableColumn
ets8801RevEnergyActive = _Ets8801RevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 20),
    _Ets8801RevEnergyActive_Type()
)
ets8801RevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801RevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    ets8801RevEnergyActive.setUnits("Wh")
_Ets8801RevEnergyReactive_Type = Unsigned32
_Ets8801RevEnergyReactive_Object = MibTableColumn
ets8801RevEnergyReactive = _Ets8801RevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 21),
    _Ets8801RevEnergyReactive_Type()
)
ets8801RevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801RevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    ets8801RevEnergyReactive.setUnits("VARh")
_Ets8801RevEnergyActiveResettable_Type = Unsigned32
_Ets8801RevEnergyActiveResettable_Object = MibTableColumn
ets8801RevEnergyActiveResettable = _Ets8801RevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 22),
    _Ets8801RevEnergyActiveResettable_Type()
)
ets8801RevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801RevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    ets8801RevEnergyActiveResettable.setUnits("Wh")
_Ets8801RevEnergyReactiveResettable_Type = Unsigned32
_Ets8801RevEnergyReactiveResettable_Object = MibTableColumn
ets8801RevEnergyReactiveResettable = _Ets8801RevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 23),
    _Ets8801RevEnergyReactiveResettable_Type()
)
ets8801RevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801RevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    ets8801RevEnergyReactiveResettable.setUnits("VARh")
_Ets8801ResidualCurrent_Type = Unsigned32
_Ets8801ResidualCurrent_Object = MibTableColumn
ets8801ResidualCurrent = _Ets8801ResidualCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 24),
    _Ets8801ResidualCurrent_Type()
)
ets8801ResidualCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801ResidualCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ets8801ResidualCurrent.setUnits("mA")


class _Ets8801LineSensorName_Type(OctetString):
    """Custom type ets8801LineSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ets8801LineSensorName_Type.__name__ = "OctetString"
_Ets8801LineSensorName_Object = MibTableColumn
ets8801LineSensorName = _Ets8801LineSensorName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 1, 2, 1, 100),
    _Ets8801LineSensorName_Type()
)
ets8801LineSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ets8801LineSensorName.setStatus("current")
_Ets8801FuseTable_Object = MibTable
ets8801FuseTable = _Ets8801FuseTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ets8801FuseTable.setStatus("current")
_Ets8801FuseEntry_Object = MibTableRow
ets8801FuseEntry = _Ets8801FuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 2, 1)
)
ets8801FuseEntry.setIndexNames(
    (0, "GUDEADS-ETS8801-MIB", "ets8801FuseIndex"),
)
if mibBuilder.loadTexts:
    ets8801FuseEntry.setStatus("current")


class _Ets8801FuseIndex_Type(Integer32):
    """Custom type ets8801FuseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Ets8801FuseIndex_Type.__name__ = "Integer32"
_Ets8801FuseIndex_Object = MibTableColumn
ets8801FuseIndex = _Ets8801FuseIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 2, 1, 1),
    _Ets8801FuseIndex_Type()
)
ets8801FuseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801FuseIndex.setStatus("current")


class _Ets8801FuseStatus_Type(Integer32):
    """Custom type ets8801FuseStatus based on Integer32"""
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


_Ets8801FuseStatus_Type.__name__ = "Integer32"
_Ets8801FuseStatus_Object = MibTableColumn
ets8801FuseStatus = _Ets8801FuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 2, 1, 2),
    _Ets8801FuseStatus_Type()
)
ets8801FuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801FuseStatus.setStatus("current")
_Ets8801ETSPowerInfo_ObjectIdentity = ObjectIdentity
ets8801ETSPowerInfo = _Ets8801ETSPowerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 11)
)


class _Ets8801PrimaryPowerAvail_Type(Integer32):
    """Custom type ets8801PrimaryPowerAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("void", 0),
          ("power", 1))
    )


_Ets8801PrimaryPowerAvail_Type.__name__ = "Integer32"
_Ets8801PrimaryPowerAvail_Object = MibScalar
ets8801PrimaryPowerAvail = _Ets8801PrimaryPowerAvail_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 11, 1),
    _Ets8801PrimaryPowerAvail_Type()
)
ets8801PrimaryPowerAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801PrimaryPowerAvail.setStatus("current")


class _Ets8801SecondaryPowerAvail_Type(Integer32):
    """Custom type ets8801SecondaryPowerAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("void", 0),
          ("power", 1))
    )


_Ets8801SecondaryPowerAvail_Type.__name__ = "Integer32"
_Ets8801SecondaryPowerAvail_Object = MibScalar
ets8801SecondaryPowerAvail = _Ets8801SecondaryPowerAvail_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 11, 2),
    _Ets8801SecondaryPowerAvail_Type()
)
ets8801SecondaryPowerAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801SecondaryPowerAvail.setStatus("current")


class _Ets8801LineSelectRequest_Type(Integer32):
    """Custom type ets8801LineSelectRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norequest", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_Ets8801LineSelectRequest_Type.__name__ = "Integer32"
_Ets8801LineSelectRequest_Object = MibScalar
ets8801LineSelectRequest = _Ets8801LineSelectRequest_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 11, 3),
    _Ets8801LineSelectRequest_Type()
)
ets8801LineSelectRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ets8801LineSelectRequest.setStatus("current")


class _Ets8801PowerLineSelected_Type(Integer32):
    """Custom type ets8801PowerLineSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_Ets8801PowerLineSelected_Type.__name__ = "Integer32"
_Ets8801PowerLineSelected_Object = MibScalar
ets8801PowerLineSelected = _Ets8801PowerLineSelected_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 5, 11, 4),
    _Ets8801PowerLineSelected_Type()
)
ets8801PowerLineSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801PowerLineSelected.setStatus("current")
_Ets8801ExtSensors_ObjectIdentity = ObjectIdentity
ets8801ExtSensors = _Ets8801ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 6)
)
_Ets8801SensorTable_Object = MibTable
ets8801SensorTable = _Ets8801SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ets8801SensorTable.setStatus("current")
_Ets8801SensorEntry_Object = MibTableRow
ets8801SensorEntry = _Ets8801SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 6, 1, 1)
)
ets8801SensorEntry.setIndexNames(
    (0, "GUDEADS-ETS8801-MIB", "ets8801SensorIndex"),
)
if mibBuilder.loadTexts:
    ets8801SensorEntry.setStatus("current")


class _Ets8801SensorIndex_Type(Integer32):
    """Custom type ets8801SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Ets8801SensorIndex_Type.__name__ = "Integer32"
_Ets8801SensorIndex_Object = MibTableColumn
ets8801SensorIndex = _Ets8801SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 6, 1, 1, 1),
    _Ets8801SensorIndex_Type()
)
ets8801SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801SensorIndex.setStatus("current")
_Ets8801TempSensor_Type = Integer32
_Ets8801TempSensor_Object = MibTableColumn
ets8801TempSensor = _Ets8801TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 6, 1, 1, 2),
    _Ets8801TempSensor_Type()
)
ets8801TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    ets8801TempSensor.setUnits("0.1 degree Celsius")
_Ets8801HygroSensor_Type = Integer32
_Ets8801HygroSensor_Object = MibTableColumn
ets8801HygroSensor = _Ets8801HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 6, 1, 1, 3),
    _Ets8801HygroSensor_Type()
)
ets8801HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    ets8801HygroSensor.setUnits("0.1 percent humidity")


class _Ets8801InputSensor_Type(Integer32):
    """Custom type ets8801InputSensor based on Integer32"""
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


_Ets8801InputSensor_Type.__name__ = "Integer32"
_Ets8801InputSensor_Object = MibTableColumn
ets8801InputSensor = _Ets8801InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 6, 1, 1, 4),
    _Ets8801InputSensor_Type()
)
ets8801InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801InputSensor.setStatus("current")
_Ets8801AirPressure_Type = Integer32
_Ets8801AirPressure_Object = MibTableColumn
ets8801AirPressure = _Ets8801AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 6, 1, 1, 5),
    _Ets8801AirPressure_Type()
)
ets8801AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    ets8801AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Ets8801DewPoint_Type = Integer32
_Ets8801DewPoint_Object = MibTableColumn
ets8801DewPoint = _Ets8801DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 6, 1, 1, 6),
    _Ets8801DewPoint_Type()
)
ets8801DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    ets8801DewPoint.setUnits("0.1 degree Celsius")
_Ets8801DewPointDiff_Type = Integer32
_Ets8801DewPointDiff_Object = MibTableColumn
ets8801DewPointDiff = _Ets8801DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 6, 1, 1, 7),
    _Ets8801DewPointDiff_Type()
)
ets8801DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ets8801DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    ets8801DewPointDiff.setUnits("0.1 degree Celsius")


class _Ets8801ExtSensorName_Type(OctetString):
    """Custom type ets8801ExtSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ets8801ExtSensorName_Type.__name__ = "OctetString"
_Ets8801ExtSensorName_Object = MibTableColumn
ets8801ExtSensorName = _Ets8801ExtSensorName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 41, 1, 6, 1, 1, 32),
    _Ets8801ExtSensorName_Type()
)
ets8801ExtSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ets8801ExtSensorName.setStatus("current")
_Ets8801Conf_ObjectIdentity = ObjectIdentity
ets8801Conf = _Ets8801Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41, 2)
)
_Ets8801Groups_ObjectIdentity = ObjectIdentity
ets8801Groups = _Ets8801Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41, 2, 1)
)
_Ets8801Compls_ObjectIdentity = ObjectIdentity
ets8801Compls = _Ets8801Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41, 2, 2)
)
_Ets8801Events_ObjectIdentity = ObjectIdentity
ets8801Events = _Ets8801Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 41, 3)
)

# Managed Objects groups

ets8801BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 41, 2, 1, 1)
)
ets8801BasicGroup.setObjects(
      *(("GUDEADS-ETS8801-MIB", "ets8801TrapCtrl"),
        ("GUDEADS-ETS8801-MIB", "ets8801TrapIPIndex"),
        ("GUDEADS-ETS8801-MIB", "ets8801TrapAddr"),
        ("GUDEADS-ETS8801-MIB", "ets8801Buzzer"),
        ("GUDEADS-ETS8801-MIB", "ets8801ActivePowerChan"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerIndex"),
        ("GUDEADS-ETS8801-MIB", "ets8801ChanStatus"),
        ("GUDEADS-ETS8801-MIB", "ets8801AbsEnergyActive"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerActive"),
        ("GUDEADS-ETS8801-MIB", "ets8801Current"),
        ("GUDEADS-ETS8801-MIB", "ets8801Voltage"),
        ("GUDEADS-ETS8801-MIB", "ets8801Frequency"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerFactor"),
        ("GUDEADS-ETS8801-MIB", "ets8801Pangle"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerApparent"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerReactive"),
        ("GUDEADS-ETS8801-MIB", "ets8801AbsEnergyReactive"),
        ("GUDEADS-ETS8801-MIB", "ets8801AbsEnergyActiveResettable"),
        ("GUDEADS-ETS8801-MIB", "ets8801AbsEnergyReactiveResettable"),
        ("GUDEADS-ETS8801-MIB", "ets8801ResetTime"),
        ("GUDEADS-ETS8801-MIB", "ets8801ForwEnergyActive"),
        ("GUDEADS-ETS8801-MIB", "ets8801ForwEnergyReactive"),
        ("GUDEADS-ETS8801-MIB", "ets8801ForwEnergyActiveResettable"),
        ("GUDEADS-ETS8801-MIB", "ets8801ForwEnergyReactiveResettable"),
        ("GUDEADS-ETS8801-MIB", "ets8801RevEnergyActive"),
        ("GUDEADS-ETS8801-MIB", "ets8801RevEnergyReactive"),
        ("GUDEADS-ETS8801-MIB", "ets8801RevEnergyActiveResettable"),
        ("GUDEADS-ETS8801-MIB", "ets8801RevEnergyReactiveResettable"),
        ("GUDEADS-ETS8801-MIB", "ets8801ResidualCurrent"),
        ("GUDEADS-ETS8801-MIB", "ets8801PrimaryPowerAvail"),
        ("GUDEADS-ETS8801-MIB", "ets8801SecondaryPowerAvail"),
        ("GUDEADS-ETS8801-MIB", "ets8801LineSelectRequest"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerLineSelected"),
        ("GUDEADS-ETS8801-MIB", "ets8801SensorIndex"),
        ("GUDEADS-ETS8801-MIB", "ets8801TempSensor"),
        ("GUDEADS-ETS8801-MIB", "ets8801HygroSensor"),
        ("GUDEADS-ETS8801-MIB", "ets8801InputSensor"),
        ("GUDEADS-ETS8801-MIB", "ets8801AirPressure"),
        ("GUDEADS-ETS8801-MIB", "ets8801DewPoint"),
        ("GUDEADS-ETS8801-MIB", "ets8801DewPointDiff"),
        ("GUDEADS-ETS8801-MIB", "ets8801LineSensorName"),
        ("GUDEADS-ETS8801-MIB", "ets8801ExtSensorName"),
        ("GUDEADS-ETS8801-MIB", "ets8801FuseIndex"),
        ("GUDEADS-ETS8801-MIB", "ets8801FuseStatus"))
)
if mibBuilder.loadTexts:
    ets8801BasicGroup.setStatus("current")


# Notification objects

ets8801PrimaryPowerChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 41, 3, 1)
)
ets8801PrimaryPowerChangeEvt.setObjects(
      *(("GUDEADS-ETS8801-MIB", "ets8801PrimaryPowerAvail"),
        ("GUDEADS-ETS8801-MIB", "ets8801SecondaryPowerAvail"))
)
if mibBuilder.loadTexts:
    ets8801PrimaryPowerChangeEvt.setStatus(
        "current"
    )

ets8801SecondaryPowerChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 41, 3, 2)
)
ets8801SecondaryPowerChangeEvt.setObjects(
      *(("GUDEADS-ETS8801-MIB", "ets8801PrimaryPowerAvail"),
        ("GUDEADS-ETS8801-MIB", "ets8801SecondaryPowerAvail"))
)
if mibBuilder.loadTexts:
    ets8801SecondaryPowerChangeEvt.setStatus(
        "current"
    )

ets8801PowerSelectEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 41, 3, 3)
)
ets8801PowerSelectEvt.setObjects(
    ("GUDEADS-ETS8801-MIB", "ets8801PowerLineSelected")
)
if mibBuilder.loadTexts:
    ets8801PowerSelectEvt.setStatus(
        "current"
    )

ets8801TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 41, 3, 4)
)
ets8801TempEvtSen.setObjects(
      *(("GUDEADS-ETS8801-MIB", "ets8801SensorIndex"),
        ("GUDEADS-ETS8801-MIB", "ets8801TempSensor"))
)
if mibBuilder.loadTexts:
    ets8801TempEvtSen.setStatus(
        "current"
    )

ets8801HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 41, 3, 5)
)
ets8801HygroEvtSen.setObjects(
      *(("GUDEADS-ETS8801-MIB", "ets8801SensorIndex"),
        ("GUDEADS-ETS8801-MIB", "ets8801HygroSensor"))
)
if mibBuilder.loadTexts:
    ets8801HygroEvtSen.setStatus(
        "current"
    )

ets8801InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 41, 3, 6)
)
ets8801InputEvtSen.setObjects(
      *(("GUDEADS-ETS8801-MIB", "ets8801SensorIndex"),
        ("GUDEADS-ETS8801-MIB", "ets8801InputSensor"))
)
if mibBuilder.loadTexts:
    ets8801InputEvtSen.setStatus(
        "current"
    )

ets8801AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 41, 3, 7)
)
ets8801AirPressureEvtSen.setObjects(
      *(("GUDEADS-ETS8801-MIB", "ets8801SensorIndex"),
        ("GUDEADS-ETS8801-MIB", "ets8801AirPressure"))
)
if mibBuilder.loadTexts:
    ets8801AirPressureEvtSen.setStatus(
        "current"
    )

ets8801DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 41, 3, 8)
)
ets8801DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-ETS8801-MIB", "ets8801SensorIndex"),
        ("GUDEADS-ETS8801-MIB", "ets8801DewPointDiff"))
)
if mibBuilder.loadTexts:
    ets8801DewPtDiffEvtSen.setStatus(
        "current"
    )

ets8801LineAmperageEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 41, 3, 9)
)
ets8801LineAmperageEvt.setObjects(
      *(("GUDEADS-ETS8801-MIB", "ets8801PowerIndex"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerActive"),
        ("GUDEADS-ETS8801-MIB", "ets8801Current"),
        ("GUDEADS-ETS8801-MIB", "ets8801Voltage"),
        ("GUDEADS-ETS8801-MIB", "ets8801Frequency"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerApparent"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerReactive"))
)
if mibBuilder.loadTexts:
    ets8801LineAmperageEvt.setStatus(
        "current"
    )

ets8801LineResidualCurrentEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 41, 3, 10)
)
ets8801LineResidualCurrentEvt.setObjects(
      *(("GUDEADS-ETS8801-MIB", "ets8801PowerIndex"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerActive"),
        ("GUDEADS-ETS8801-MIB", "ets8801Current"),
        ("GUDEADS-ETS8801-MIB", "ets8801ResidualCurrent"),
        ("GUDEADS-ETS8801-MIB", "ets8801Voltage"),
        ("GUDEADS-ETS8801-MIB", "ets8801Frequency"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerApparent"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerReactive"))
)
if mibBuilder.loadTexts:
    ets8801LineResidualCurrentEvt.setStatus(
        "current"
    )

ets8801FuseEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 41, 3, 11)
)
ets8801FuseEvt.setObjects(
      *(("GUDEADS-ETS8801-MIB", "ets8801FuseIndex"),
        ("GUDEADS-ETS8801-MIB", "ets8801FuseStatus"))
)
if mibBuilder.loadTexts:
    ets8801FuseEvt.setStatus(
        "current"
    )


# Notifications groups

ets8801NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 41, 2, 1, 2)
)
ets8801NotificationGroup.setObjects(
      *(("GUDEADS-ETS8801-MIB", "ets8801PrimaryPowerChangeEvt"),
        ("GUDEADS-ETS8801-MIB", "ets8801SecondaryPowerChangeEvt"),
        ("GUDEADS-ETS8801-MIB", "ets8801PowerSelectEvt"),
        ("GUDEADS-ETS8801-MIB", "ets8801LineAmperageEvt"),
        ("GUDEADS-ETS8801-MIB", "ets8801TempEvtSen"),
        ("GUDEADS-ETS8801-MIB", "ets8801HygroEvtSen"),
        ("GUDEADS-ETS8801-MIB", "ets8801InputEvtSen"),
        ("GUDEADS-ETS8801-MIB", "ets8801AirPressureEvtSen"),
        ("GUDEADS-ETS8801-MIB", "ets8801DewPtDiffEvtSen"),
        ("GUDEADS-ETS8801-MIB", "ets8801LineResidualCurrentEvt"),
        ("GUDEADS-ETS8801-MIB", "ets8801FuseEvt"))
)
if mibBuilder.loadTexts:
    ets8801NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-ETS8801-MIB",
    **{"gudeads": gudeads,
       "gadsETS8801": gadsETS8801,
       "ets8801Objects": ets8801Objects,
       "ets8801CommonConfig": ets8801CommonConfig,
       "ets8801SNMPaccess": ets8801SNMPaccess,
       "ets8801TrapCtrl": ets8801TrapCtrl,
       "ets8801TrapIPTable": ets8801TrapIPTable,
       "ets8801TrapIPEntry": ets8801TrapIPEntry,
       "ets8801TrapIPIndex": ets8801TrapIPIndex,
       "ets8801TrapAddr": ets8801TrapAddr,
       "ets8801IntActors": ets8801IntActors,
       "ets8801Buzzer": ets8801Buzzer,
       "ets8801IntSensors": ets8801IntSensors,
       "ets8801PowerChan": ets8801PowerChan,
       "ets8801ActivePowerChan": ets8801ActivePowerChan,
       "ets8801PowerTable": ets8801PowerTable,
       "ets8801PowerEntry": ets8801PowerEntry,
       "ets8801PowerIndex": ets8801PowerIndex,
       "ets8801ChanStatus": ets8801ChanStatus,
       "ets8801AbsEnergyActive": ets8801AbsEnergyActive,
       "ets8801PowerActive": ets8801PowerActive,
       "ets8801Current": ets8801Current,
       "ets8801Voltage": ets8801Voltage,
       "ets8801Frequency": ets8801Frequency,
       "ets8801PowerFactor": ets8801PowerFactor,
       "ets8801Pangle": ets8801Pangle,
       "ets8801PowerApparent": ets8801PowerApparent,
       "ets8801PowerReactive": ets8801PowerReactive,
       "ets8801AbsEnergyReactive": ets8801AbsEnergyReactive,
       "ets8801AbsEnergyActiveResettable": ets8801AbsEnergyActiveResettable,
       "ets8801AbsEnergyReactiveResettable": ets8801AbsEnergyReactiveResettable,
       "ets8801ResetTime": ets8801ResetTime,
       "ets8801ForwEnergyActive": ets8801ForwEnergyActive,
       "ets8801ForwEnergyReactive": ets8801ForwEnergyReactive,
       "ets8801ForwEnergyActiveResettable": ets8801ForwEnergyActiveResettable,
       "ets8801ForwEnergyReactiveResettable": ets8801ForwEnergyReactiveResettable,
       "ets8801RevEnergyActive": ets8801RevEnergyActive,
       "ets8801RevEnergyReactive": ets8801RevEnergyReactive,
       "ets8801RevEnergyActiveResettable": ets8801RevEnergyActiveResettable,
       "ets8801RevEnergyReactiveResettable": ets8801RevEnergyReactiveResettable,
       "ets8801ResidualCurrent": ets8801ResidualCurrent,
       "ets8801LineSensorName": ets8801LineSensorName,
       "ets8801FuseTable": ets8801FuseTable,
       "ets8801FuseEntry": ets8801FuseEntry,
       "ets8801FuseIndex": ets8801FuseIndex,
       "ets8801FuseStatus": ets8801FuseStatus,
       "ets8801ETSPowerInfo": ets8801ETSPowerInfo,
       "ets8801PrimaryPowerAvail": ets8801PrimaryPowerAvail,
       "ets8801SecondaryPowerAvail": ets8801SecondaryPowerAvail,
       "ets8801LineSelectRequest": ets8801LineSelectRequest,
       "ets8801PowerLineSelected": ets8801PowerLineSelected,
       "ets8801ExtSensors": ets8801ExtSensors,
       "ets8801SensorTable": ets8801SensorTable,
       "ets8801SensorEntry": ets8801SensorEntry,
       "ets8801SensorIndex": ets8801SensorIndex,
       "ets8801TempSensor": ets8801TempSensor,
       "ets8801HygroSensor": ets8801HygroSensor,
       "ets8801InputSensor": ets8801InputSensor,
       "ets8801AirPressure": ets8801AirPressure,
       "ets8801DewPoint": ets8801DewPoint,
       "ets8801DewPointDiff": ets8801DewPointDiff,
       "ets8801ExtSensorName": ets8801ExtSensorName,
       "ets8801Conf": ets8801Conf,
       "ets8801Groups": ets8801Groups,
       "ets8801BasicGroup": ets8801BasicGroup,
       "ets8801NotificationGroup": ets8801NotificationGroup,
       "ets8801Compls": ets8801Compls,
       "ets8801Events": ets8801Events,
       "ets8801PrimaryPowerChangeEvt": ets8801PrimaryPowerChangeEvt,
       "ets8801SecondaryPowerChangeEvt": ets8801SecondaryPowerChangeEvt,
       "ets8801PowerSelectEvt": ets8801PowerSelectEvt,
       "ets8801TempEvtSen": ets8801TempEvtSen,
       "ets8801HygroEvtSen": ets8801HygroEvtSen,
       "ets8801InputEvtSen": ets8801InputEvtSen,
       "ets8801AirPressureEvtSen": ets8801AirPressureEvtSen,
       "ets8801DewPtDiffEvtSen": ets8801DewPtDiffEvtSen,
       "ets8801LineAmperageEvt": ets8801LineAmperageEvt,
       "ets8801LineResidualCurrentEvt": ets8801LineResidualCurrentEvt,
       "ets8801FuseEvt": ets8801FuseEvt}
)
