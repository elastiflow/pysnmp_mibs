# SNMP MIB module (GUDEADS-PDU8340-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-PDU8340-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:15:00 2025
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

_GadsPDU8340_ObjectIdentity = ObjectIdentity
gadsPDU8340 = _GadsPDU8340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54)
)
_Pdu8340Objects_ObjectIdentity = ObjectIdentity
pdu8340Objects = _Pdu8340Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1)
)
_Pdu8340CommonConfig_ObjectIdentity = ObjectIdentity
pdu8340CommonConfig = _Pdu8340CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 1)
)
_Pdu8340SNMPaccess_ObjectIdentity = ObjectIdentity
pdu8340SNMPaccess = _Pdu8340SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 1, 1)
)


class _Pdu8340TrapCtrl_Type(Integer32):
    """Custom type pdu8340TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Pdu8340TrapCtrl_Type.__name__ = "Integer32"
_Pdu8340TrapCtrl_Object = MibScalar
pdu8340TrapCtrl = _Pdu8340TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 1, 1, 1),
    _Pdu8340TrapCtrl_Type()
)
pdu8340TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8340TrapCtrl.setStatus("current")
_Pdu8340TrapIPTable_Object = MibTable
pdu8340TrapIPTable = _Pdu8340TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pdu8340TrapIPTable.setStatus("current")
_Pdu8340TrapIPEntry_Object = MibTableRow
pdu8340TrapIPEntry = _Pdu8340TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 1, 1, 2, 1)
)
pdu8340TrapIPEntry.setIndexNames(
    (0, "GUDEADS-PDU8340-MIB", "pdu8340TrapIPIndex"),
)
if mibBuilder.loadTexts:
    pdu8340TrapIPEntry.setStatus("current")


class _Pdu8340TrapIPIndex_Type(Integer32):
    """Custom type pdu8340TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Pdu8340TrapIPIndex_Type.__name__ = "Integer32"
_Pdu8340TrapIPIndex_Object = MibTableColumn
pdu8340TrapIPIndex = _Pdu8340TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 1, 1, 2, 1, 1),
    _Pdu8340TrapIPIndex_Type()
)
pdu8340TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340TrapIPIndex.setStatus("current")


class _Pdu8340TrapAddr_Type(OctetString):
    """Custom type pdu8340TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Pdu8340TrapAddr_Type.__name__ = "OctetString"
_Pdu8340TrapAddr_Object = MibTableColumn
pdu8340TrapAddr = _Pdu8340TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 1, 1, 2, 1, 2),
    _Pdu8340TrapAddr_Type()
)
pdu8340TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8340TrapAddr.setStatus("current")
_Pdu8340DeviceConfig_ObjectIdentity = ObjectIdentity
pdu8340DeviceConfig = _Pdu8340DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 2)
)
_Pdu8340IntActors_ObjectIdentity = ObjectIdentity
pdu8340IntActors = _Pdu8340IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 3)
)


class _Pdu8340Buzzer_Type(Integer32):
    """Custom type pdu8340Buzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu8340Buzzer_Type.__name__ = "Integer32"
_Pdu8340Buzzer_Object = MibScalar
pdu8340Buzzer = _Pdu8340Buzzer_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 3, 10),
    _Pdu8340Buzzer_Type()
)
pdu8340Buzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8340Buzzer.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340Buzzer.setUnits("0 = Off, 1 = On")
_Pdu8340ExtActors_ObjectIdentity = ObjectIdentity
pdu8340ExtActors = _Pdu8340ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 4)
)
_Pdu8340IntSensors_ObjectIdentity = ObjectIdentity
pdu8340IntSensors = _Pdu8340IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5)
)
_Pdu8340PowerChan_ObjectIdentity = ObjectIdentity
pdu8340PowerChan = _Pdu8340PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1)
)


class _Pdu8340ActivePowerChan_Type(Unsigned32):
    """Custom type pdu8340ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu8340ActivePowerChan_Type.__name__ = "Unsigned32"
_Pdu8340ActivePowerChan_Object = MibScalar
pdu8340ActivePowerChan = _Pdu8340ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 1),
    _Pdu8340ActivePowerChan_Type()
)
pdu8340ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340ActivePowerChan.setStatus("current")
_Pdu8340PowerTable_Object = MibTable
pdu8340PowerTable = _Pdu8340PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    pdu8340PowerTable.setStatus("current")
_Pdu8340PowerEntry_Object = MibTableRow
pdu8340PowerEntry = _Pdu8340PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1)
)
pdu8340PowerEntry.setIndexNames(
    (0, "GUDEADS-PDU8340-MIB", "pdu8340PowerIndex"),
)
if mibBuilder.loadTexts:
    pdu8340PowerEntry.setStatus("current")


class _Pdu8340PowerIndex_Type(Integer32):
    """Custom type pdu8340PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu8340PowerIndex_Type.__name__ = "Integer32"
_Pdu8340PowerIndex_Object = MibTableColumn
pdu8340PowerIndex = _Pdu8340PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 1),
    _Pdu8340PowerIndex_Type()
)
pdu8340PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340PowerIndex.setStatus("current")


class _Pdu8340ChanStatus_Type(Integer32):
    """Custom type pdu8340ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu8340ChanStatus_Type.__name__ = "Integer32"
_Pdu8340ChanStatus_Object = MibTableColumn
pdu8340ChanStatus = _Pdu8340ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 2),
    _Pdu8340ChanStatus_Type()
)
pdu8340ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340ChanStatus.setStatus("current")
_Pdu8340AbsEnergyActive_Type = Unsigned32
_Pdu8340AbsEnergyActive_Object = MibTableColumn
pdu8340AbsEnergyActive = _Pdu8340AbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 3),
    _Pdu8340AbsEnergyActive_Type()
)
pdu8340AbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340AbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340AbsEnergyActive.setUnits("Wh")
_Pdu8340PowerActive_Type = Integer32
_Pdu8340PowerActive_Object = MibTableColumn
pdu8340PowerActive = _Pdu8340PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 4),
    _Pdu8340PowerActive_Type()
)
pdu8340PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340PowerActive.setUnits("W")
_Pdu8340Current_Type = Unsigned32
_Pdu8340Current_Object = MibTableColumn
pdu8340Current = _Pdu8340Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 5),
    _Pdu8340Current_Type()
)
pdu8340Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340Current.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340Current.setUnits("mA")
_Pdu8340Voltage_Type = Unsigned32
_Pdu8340Voltage_Object = MibTableColumn
pdu8340Voltage = _Pdu8340Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 6),
    _Pdu8340Voltage_Type()
)
pdu8340Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340Voltage.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340Voltage.setUnits("V")
_Pdu8340Frequency_Type = Unsigned32
_Pdu8340Frequency_Object = MibTableColumn
pdu8340Frequency = _Pdu8340Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 7),
    _Pdu8340Frequency_Type()
)
pdu8340Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340Frequency.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340Frequency.setUnits("0.01 hz")
_Pdu8340PowerFactor_Type = Integer32
_Pdu8340PowerFactor_Object = MibTableColumn
pdu8340PowerFactor = _Pdu8340PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 8),
    _Pdu8340PowerFactor_Type()
)
pdu8340PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340PowerFactor.setUnits("0.001")
_Pdu8340Pangle_Type = Integer32
_Pdu8340Pangle_Object = MibTableColumn
pdu8340Pangle = _Pdu8340Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 9),
    _Pdu8340Pangle_Type()
)
pdu8340Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340Pangle.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340Pangle.setUnits("0.1 degree")
_Pdu8340PowerApparent_Type = Integer32
_Pdu8340PowerApparent_Object = MibTableColumn
pdu8340PowerApparent = _Pdu8340PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 10),
    _Pdu8340PowerApparent_Type()
)
pdu8340PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340PowerApparent.setUnits("VA")
_Pdu8340PowerReactive_Type = Integer32
_Pdu8340PowerReactive_Object = MibTableColumn
pdu8340PowerReactive = _Pdu8340PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 11),
    _Pdu8340PowerReactive_Type()
)
pdu8340PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340PowerReactive.setUnits("VAR")
_Pdu8340AbsEnergyReactive_Type = Unsigned32
_Pdu8340AbsEnergyReactive_Object = MibTableColumn
pdu8340AbsEnergyReactive = _Pdu8340AbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 12),
    _Pdu8340AbsEnergyReactive_Type()
)
pdu8340AbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340AbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340AbsEnergyReactive.setUnits("VARh")
_Pdu8340AbsEnergyActiveResettable_Type = Unsigned32
_Pdu8340AbsEnergyActiveResettable_Object = MibTableColumn
pdu8340AbsEnergyActiveResettable = _Pdu8340AbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 13),
    _Pdu8340AbsEnergyActiveResettable_Type()
)
pdu8340AbsEnergyActiveResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8340AbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340AbsEnergyActiveResettable.setUnits("Wh")
_Pdu8340AbsEnergyReactiveResettable_Type = Unsigned32
_Pdu8340AbsEnergyReactiveResettable_Object = MibTableColumn
pdu8340AbsEnergyReactiveResettable = _Pdu8340AbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 14),
    _Pdu8340AbsEnergyReactiveResettable_Type()
)
pdu8340AbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340AbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340AbsEnergyReactiveResettable.setUnits("VARh")
_Pdu8340ResetTime_Type = Unsigned32
_Pdu8340ResetTime_Object = MibTableColumn
pdu8340ResetTime = _Pdu8340ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 15),
    _Pdu8340ResetTime_Type()
)
pdu8340ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340ResetTime.setUnits("s")
_Pdu8340ForwEnergyActive_Type = Unsigned32
_Pdu8340ForwEnergyActive_Object = MibTableColumn
pdu8340ForwEnergyActive = _Pdu8340ForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 16),
    _Pdu8340ForwEnergyActive_Type()
)
pdu8340ForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340ForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340ForwEnergyActive.setUnits("Wh")
_Pdu8340ForwEnergyReactive_Type = Unsigned32
_Pdu8340ForwEnergyReactive_Object = MibTableColumn
pdu8340ForwEnergyReactive = _Pdu8340ForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 17),
    _Pdu8340ForwEnergyReactive_Type()
)
pdu8340ForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340ForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340ForwEnergyReactive.setUnits("VARh")
_Pdu8340ForwEnergyActiveResettable_Type = Unsigned32
_Pdu8340ForwEnergyActiveResettable_Object = MibTableColumn
pdu8340ForwEnergyActiveResettable = _Pdu8340ForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 18),
    _Pdu8340ForwEnergyActiveResettable_Type()
)
pdu8340ForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340ForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340ForwEnergyActiveResettable.setUnits("Wh")
_Pdu8340ForwEnergyReactiveResettable_Type = Unsigned32
_Pdu8340ForwEnergyReactiveResettable_Object = MibTableColumn
pdu8340ForwEnergyReactiveResettable = _Pdu8340ForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 19),
    _Pdu8340ForwEnergyReactiveResettable_Type()
)
pdu8340ForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340ForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340ForwEnergyReactiveResettable.setUnits("VARh")
_Pdu8340RevEnergyActive_Type = Unsigned32
_Pdu8340RevEnergyActive_Object = MibTableColumn
pdu8340RevEnergyActive = _Pdu8340RevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 20),
    _Pdu8340RevEnergyActive_Type()
)
pdu8340RevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340RevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340RevEnergyActive.setUnits("Wh")
_Pdu8340RevEnergyReactive_Type = Unsigned32
_Pdu8340RevEnergyReactive_Object = MibTableColumn
pdu8340RevEnergyReactive = _Pdu8340RevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 21),
    _Pdu8340RevEnergyReactive_Type()
)
pdu8340RevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340RevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340RevEnergyReactive.setUnits("VARh")
_Pdu8340RevEnergyActiveResettable_Type = Unsigned32
_Pdu8340RevEnergyActiveResettable_Object = MibTableColumn
pdu8340RevEnergyActiveResettable = _Pdu8340RevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 22),
    _Pdu8340RevEnergyActiveResettable_Type()
)
pdu8340RevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340RevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340RevEnergyActiveResettable.setUnits("Wh")
_Pdu8340RevEnergyReactiveResettable_Type = Unsigned32
_Pdu8340RevEnergyReactiveResettable_Object = MibTableColumn
pdu8340RevEnergyReactiveResettable = _Pdu8340RevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 23),
    _Pdu8340RevEnergyReactiveResettable_Type()
)
pdu8340RevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340RevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340RevEnergyReactiveResettable.setUnits("VARh")
_Pdu8340ResidualCurrent_Type = Unsigned32
_Pdu8340ResidualCurrent_Object = MibTableColumn
pdu8340ResidualCurrent = _Pdu8340ResidualCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 5, 1, 2, 1, 24),
    _Pdu8340ResidualCurrent_Type()
)
pdu8340ResidualCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340ResidualCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340ResidualCurrent.setUnits("mA")
_Pdu8340ExtSensors_ObjectIdentity = ObjectIdentity
pdu8340ExtSensors = _Pdu8340ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 6)
)
_Pdu8340SensorTable_Object = MibTable
pdu8340SensorTable = _Pdu8340SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 6, 1)
)
if mibBuilder.loadTexts:
    pdu8340SensorTable.setStatus("current")
_Pdu8340SensorEntry_Object = MibTableRow
pdu8340SensorEntry = _Pdu8340SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 6, 1, 1)
)
pdu8340SensorEntry.setIndexNames(
    (0, "GUDEADS-PDU8340-MIB", "pdu8340SensorIndex"),
)
if mibBuilder.loadTexts:
    pdu8340SensorEntry.setStatus("current")


class _Pdu8340SensorIndex_Type(Integer32):
    """Custom type pdu8340SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu8340SensorIndex_Type.__name__ = "Integer32"
_Pdu8340SensorIndex_Object = MibTableColumn
pdu8340SensorIndex = _Pdu8340SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 6, 1, 1, 1),
    _Pdu8340SensorIndex_Type()
)
pdu8340SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340SensorIndex.setStatus("current")
_Pdu8340TempSensor_Type = Integer32
_Pdu8340TempSensor_Object = MibTableColumn
pdu8340TempSensor = _Pdu8340TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 6, 1, 1, 2),
    _Pdu8340TempSensor_Type()
)
pdu8340TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340TempSensor.setUnits("0.1 degree Celsius")
_Pdu8340HygroSensor_Type = Integer32
_Pdu8340HygroSensor_Object = MibTableColumn
pdu8340HygroSensor = _Pdu8340HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 6, 1, 1, 3),
    _Pdu8340HygroSensor_Type()
)
pdu8340HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340HygroSensor.setUnits("0.1 percent humidity")


class _Pdu8340InputSensor_Type(Integer32):
    """Custom type pdu8340InputSensor based on Integer32"""
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


_Pdu8340InputSensor_Type.__name__ = "Integer32"
_Pdu8340InputSensor_Object = MibTableColumn
pdu8340InputSensor = _Pdu8340InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 6, 1, 1, 4),
    _Pdu8340InputSensor_Type()
)
pdu8340InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340InputSensor.setStatus("current")
_Pdu8340AirPressure_Type = Integer32
_Pdu8340AirPressure_Object = MibTableColumn
pdu8340AirPressure = _Pdu8340AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 6, 1, 1, 5),
    _Pdu8340AirPressure_Type()
)
pdu8340AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Pdu8340DewPoint_Type = Integer32
_Pdu8340DewPoint_Object = MibTableColumn
pdu8340DewPoint = _Pdu8340DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 6, 1, 1, 6),
    _Pdu8340DewPoint_Type()
)
pdu8340DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340DewPoint.setUnits("0.1 degree Celsius")
_Pdu8340DewPointDiff_Type = Integer32
_Pdu8340DewPointDiff_Object = MibTableColumn
pdu8340DewPointDiff = _Pdu8340DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 54, 1, 6, 1, 1, 7),
    _Pdu8340DewPointDiff_Type()
)
pdu8340DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8340DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    pdu8340DewPointDiff.setUnits("0.1 degree Celsius")
_Pdu8340Conf_ObjectIdentity = ObjectIdentity
pdu8340Conf = _Pdu8340Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 2)
)
_Pdu8340Groups_ObjectIdentity = ObjectIdentity
pdu8340Groups = _Pdu8340Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 2, 1)
)
_Pdu8340Compls_ObjectIdentity = ObjectIdentity
pdu8340Compls = _Pdu8340Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 54, 3)
)

# Managed Objects groups

pdu8340BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 54, 2, 1, 1)
)
pdu8340BasicGroup.setObjects(
      *(("GUDEADS-PDU8340-MIB", "pdu8340TrapCtrl"),
        ("GUDEADS-PDU8340-MIB", "pdu8340TrapIPIndex"),
        ("GUDEADS-PDU8340-MIB", "pdu8340TrapAddr"),
        ("GUDEADS-PDU8340-MIB", "pdu8340Buzzer"),
        ("GUDEADS-PDU8340-MIB", "pdu8340ActivePowerChan"),
        ("GUDEADS-PDU8340-MIB", "pdu8340PowerIndex"),
        ("GUDEADS-PDU8340-MIB", "pdu8340ChanStatus"),
        ("GUDEADS-PDU8340-MIB", "pdu8340AbsEnergyActive"),
        ("GUDEADS-PDU8340-MIB", "pdu8340PowerActive"),
        ("GUDEADS-PDU8340-MIB", "pdu8340Current"),
        ("GUDEADS-PDU8340-MIB", "pdu8340Voltage"),
        ("GUDEADS-PDU8340-MIB", "pdu8340Frequency"),
        ("GUDEADS-PDU8340-MIB", "pdu8340PowerFactor"),
        ("GUDEADS-PDU8340-MIB", "pdu8340Pangle"),
        ("GUDEADS-PDU8340-MIB", "pdu8340PowerApparent"),
        ("GUDEADS-PDU8340-MIB", "pdu8340PowerReactive"),
        ("GUDEADS-PDU8340-MIB", "pdu8340AbsEnergyReactive"),
        ("GUDEADS-PDU8340-MIB", "pdu8340AbsEnergyActiveResettable"),
        ("GUDEADS-PDU8340-MIB", "pdu8340AbsEnergyReactiveResettable"),
        ("GUDEADS-PDU8340-MIB", "pdu8340ResetTime"),
        ("GUDEADS-PDU8340-MIB", "pdu8340ForwEnergyActive"),
        ("GUDEADS-PDU8340-MIB", "pdu8340ForwEnergyReactive"),
        ("GUDEADS-PDU8340-MIB", "pdu8340ForwEnergyActiveResettable"),
        ("GUDEADS-PDU8340-MIB", "pdu8340ForwEnergyReactiveResettable"),
        ("GUDEADS-PDU8340-MIB", "pdu8340RevEnergyActive"),
        ("GUDEADS-PDU8340-MIB", "pdu8340RevEnergyReactive"),
        ("GUDEADS-PDU8340-MIB", "pdu8340RevEnergyActiveResettable"),
        ("GUDEADS-PDU8340-MIB", "pdu8340RevEnergyReactiveResettable"),
        ("GUDEADS-PDU8340-MIB", "pdu8340ResidualCurrent"),
        ("GUDEADS-PDU8340-MIB", "pdu8340SensorIndex"),
        ("GUDEADS-PDU8340-MIB", "pdu8340TempSensor"),
        ("GUDEADS-PDU8340-MIB", "pdu8340HygroSensor"),
        ("GUDEADS-PDU8340-MIB", "pdu8340InputSensor"),
        ("GUDEADS-PDU8340-MIB", "pdu8340AirPressure"),
        ("GUDEADS-PDU8340-MIB", "pdu8340DewPoint"),
        ("GUDEADS-PDU8340-MIB", "pdu8340DewPointDiff"))
)
if mibBuilder.loadTexts:
    pdu8340BasicGroup.setStatus("current")


# Notification objects

pdu8340TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 54, 3, 1)
)
pdu8340TempEvtSen.setObjects(
      *(("GUDEADS-PDU8340-MIB", "pdu8340SensorIndex"),
        ("GUDEADS-PDU8340-MIB", "pdu8340TempSensor"))
)
if mibBuilder.loadTexts:
    pdu8340TempEvtSen.setStatus(
        "current"
    )

pdu8340HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 54, 3, 2)
)
pdu8340HygroEvtSen.setObjects(
      *(("GUDEADS-PDU8340-MIB", "pdu8340SensorIndex"),
        ("GUDEADS-PDU8340-MIB", "pdu8340HygroSensor"))
)
if mibBuilder.loadTexts:
    pdu8340HygroEvtSen.setStatus(
        "current"
    )

pdu8340InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 54, 3, 3)
)
pdu8340InputEvtSen.setObjects(
      *(("GUDEADS-PDU8340-MIB", "pdu8340SensorIndex"),
        ("GUDEADS-PDU8340-MIB", "pdu8340InputSensor"))
)
if mibBuilder.loadTexts:
    pdu8340InputEvtSen.setStatus(
        "current"
    )

pdu8340AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 54, 3, 4)
)
pdu8340AirPressureEvtSen.setObjects(
      *(("GUDEADS-PDU8340-MIB", "pdu8340SensorIndex"),
        ("GUDEADS-PDU8340-MIB", "pdu8340AirPressure"))
)
if mibBuilder.loadTexts:
    pdu8340AirPressureEvtSen.setStatus(
        "current"
    )

pdu8340DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 54, 3, 5)
)
pdu8340DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-PDU8340-MIB", "pdu8340SensorIndex"),
        ("GUDEADS-PDU8340-MIB", "pdu8340DewPointDiff"))
)
if mibBuilder.loadTexts:
    pdu8340DewPtDiffEvtSen.setStatus(
        "current"
    )

pdu8340LineAmperageEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 54, 3, 6)
)
pdu8340LineAmperageEvt.setObjects(
      *(("GUDEADS-PDU8340-MIB", "pdu8340PowerIndex"),
        ("GUDEADS-PDU8340-MIB", "pdu8340PowerActive"),
        ("GUDEADS-PDU8340-MIB", "pdu8340Current"),
        ("GUDEADS-PDU8340-MIB", "pdu8340Voltage"),
        ("GUDEADS-PDU8340-MIB", "pdu8340Frequency"),
        ("GUDEADS-PDU8340-MIB", "pdu8340PowerApparent"),
        ("GUDEADS-PDU8340-MIB", "pdu8340PowerReactive"))
)
if mibBuilder.loadTexts:
    pdu8340LineAmperageEvt.setStatus(
        "current"
    )


# Notifications groups

pdu8340NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 54, 2, 1, 2)
)
pdu8340NotificationGroup.setObjects(
      *(("GUDEADS-PDU8340-MIB", "pdu8340TempEvtSen"),
        ("GUDEADS-PDU8340-MIB", "pdu8340HygroEvtSen"),
        ("GUDEADS-PDU8340-MIB", "pdu8340InputEvtSen"),
        ("GUDEADS-PDU8340-MIB", "pdu8340AirPressureEvtSen"),
        ("GUDEADS-PDU8340-MIB", "pdu8340DewPtDiffEvtSen"),
        ("GUDEADS-PDU8340-MIB", "pdu8340LineAmperageEvt"))
)
if mibBuilder.loadTexts:
    pdu8340NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-PDU8340-MIB",
    **{"gudeads": gudeads,
       "gadsPDU8340": gadsPDU8340,
       "pdu8340Objects": pdu8340Objects,
       "pdu8340CommonConfig": pdu8340CommonConfig,
       "pdu8340SNMPaccess": pdu8340SNMPaccess,
       "pdu8340TrapCtrl": pdu8340TrapCtrl,
       "pdu8340TrapIPTable": pdu8340TrapIPTable,
       "pdu8340TrapIPEntry": pdu8340TrapIPEntry,
       "pdu8340TrapIPIndex": pdu8340TrapIPIndex,
       "pdu8340TrapAddr": pdu8340TrapAddr,
       "pdu8340DeviceConfig": pdu8340DeviceConfig,
       "pdu8340IntActors": pdu8340IntActors,
       "pdu8340Buzzer": pdu8340Buzzer,
       "pdu8340ExtActors": pdu8340ExtActors,
       "pdu8340IntSensors": pdu8340IntSensors,
       "pdu8340PowerChan": pdu8340PowerChan,
       "pdu8340ActivePowerChan": pdu8340ActivePowerChan,
       "pdu8340PowerTable": pdu8340PowerTable,
       "pdu8340PowerEntry": pdu8340PowerEntry,
       "pdu8340PowerIndex": pdu8340PowerIndex,
       "pdu8340ChanStatus": pdu8340ChanStatus,
       "pdu8340AbsEnergyActive": pdu8340AbsEnergyActive,
       "pdu8340PowerActive": pdu8340PowerActive,
       "pdu8340Current": pdu8340Current,
       "pdu8340Voltage": pdu8340Voltage,
       "pdu8340Frequency": pdu8340Frequency,
       "pdu8340PowerFactor": pdu8340PowerFactor,
       "pdu8340Pangle": pdu8340Pangle,
       "pdu8340PowerApparent": pdu8340PowerApparent,
       "pdu8340PowerReactive": pdu8340PowerReactive,
       "pdu8340AbsEnergyReactive": pdu8340AbsEnergyReactive,
       "pdu8340AbsEnergyActiveResettable": pdu8340AbsEnergyActiveResettable,
       "pdu8340AbsEnergyReactiveResettable": pdu8340AbsEnergyReactiveResettable,
       "pdu8340ResetTime": pdu8340ResetTime,
       "pdu8340ForwEnergyActive": pdu8340ForwEnergyActive,
       "pdu8340ForwEnergyReactive": pdu8340ForwEnergyReactive,
       "pdu8340ForwEnergyActiveResettable": pdu8340ForwEnergyActiveResettable,
       "pdu8340ForwEnergyReactiveResettable": pdu8340ForwEnergyReactiveResettable,
       "pdu8340RevEnergyActive": pdu8340RevEnergyActive,
       "pdu8340RevEnergyReactive": pdu8340RevEnergyReactive,
       "pdu8340RevEnergyActiveResettable": pdu8340RevEnergyActiveResettable,
       "pdu8340RevEnergyReactiveResettable": pdu8340RevEnergyReactiveResettable,
       "pdu8340ResidualCurrent": pdu8340ResidualCurrent,
       "pdu8340ExtSensors": pdu8340ExtSensors,
       "pdu8340SensorTable": pdu8340SensorTable,
       "pdu8340SensorEntry": pdu8340SensorEntry,
       "pdu8340SensorIndex": pdu8340SensorIndex,
       "pdu8340TempSensor": pdu8340TempSensor,
       "pdu8340HygroSensor": pdu8340HygroSensor,
       "pdu8340InputSensor": pdu8340InputSensor,
       "pdu8340AirPressure": pdu8340AirPressure,
       "pdu8340DewPoint": pdu8340DewPoint,
       "pdu8340DewPointDiff": pdu8340DewPointDiff,
       "pdu8340Conf": pdu8340Conf,
       "pdu8340Groups": pdu8340Groups,
       "pdu8340BasicGroup": pdu8340BasicGroup,
       "pdu8340NotificationGroup": pdu8340NotificationGroup,
       "pdu8340Compls": pdu8340Compls,
       "events": events,
       "pdu8340TempEvtSen": pdu8340TempEvtSen,
       "pdu8340HygroEvtSen": pdu8340HygroEvtSen,
       "pdu8340InputEvtSen": pdu8340InputEvtSen,
       "pdu8340AirPressureEvtSen": pdu8340AirPressureEvtSen,
       "pdu8340DewPtDiffEvtSen": pdu8340DewPtDiffEvtSen,
       "pdu8340LineAmperageEvt": pdu8340LineAmperageEvt}
)
