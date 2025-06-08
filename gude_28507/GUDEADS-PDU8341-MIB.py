# SNMP MIB module (GUDEADS-PDU8341-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-PDU8341-MIB.mib
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

_GadsPDU8341_ObjectIdentity = ObjectIdentity
gadsPDU8341 = _GadsPDU8341_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65)
)
_Pdu8341Objects_ObjectIdentity = ObjectIdentity
pdu8341Objects = _Pdu8341Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1)
)
_Pdu8341CommonConfig_ObjectIdentity = ObjectIdentity
pdu8341CommonConfig = _Pdu8341CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 1)
)
_Pdu8341SNMPaccess_ObjectIdentity = ObjectIdentity
pdu8341SNMPaccess = _Pdu8341SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 1, 1)
)


class _Pdu8341TrapCtrl_Type(Integer32):
    """Custom type pdu8341TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Pdu8341TrapCtrl_Type.__name__ = "Integer32"
_Pdu8341TrapCtrl_Object = MibScalar
pdu8341TrapCtrl = _Pdu8341TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 1, 1, 1),
    _Pdu8341TrapCtrl_Type()
)
pdu8341TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8341TrapCtrl.setStatus("current")
_Pdu8341TrapIPTable_Object = MibTable
pdu8341TrapIPTable = _Pdu8341TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pdu8341TrapIPTable.setStatus("current")
_Pdu8341TrapIPEntry_Object = MibTableRow
pdu8341TrapIPEntry = _Pdu8341TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 1, 1, 2, 1)
)
pdu8341TrapIPEntry.setIndexNames(
    (0, "GUDEADS-PDU8341-MIB", "pdu8341TrapIPIndex"),
)
if mibBuilder.loadTexts:
    pdu8341TrapIPEntry.setStatus("current")


class _Pdu8341TrapIPIndex_Type(Integer32):
    """Custom type pdu8341TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Pdu8341TrapIPIndex_Type.__name__ = "Integer32"
_Pdu8341TrapIPIndex_Object = MibTableColumn
pdu8341TrapIPIndex = _Pdu8341TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 1, 1, 2, 1, 1),
    _Pdu8341TrapIPIndex_Type()
)
pdu8341TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341TrapIPIndex.setStatus("current")


class _Pdu8341TrapAddr_Type(OctetString):
    """Custom type pdu8341TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Pdu8341TrapAddr_Type.__name__ = "OctetString"
_Pdu8341TrapAddr_Object = MibTableColumn
pdu8341TrapAddr = _Pdu8341TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 1, 1, 2, 1, 2),
    _Pdu8341TrapAddr_Type()
)
pdu8341TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8341TrapAddr.setStatus("current")
_Pdu8341DeviceConfig_ObjectIdentity = ObjectIdentity
pdu8341DeviceConfig = _Pdu8341DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 2)
)
_Pdu8341IntActors_ObjectIdentity = ObjectIdentity
pdu8341IntActors = _Pdu8341IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 3)
)


class _Pdu8341Buzzer_Type(Integer32):
    """Custom type pdu8341Buzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu8341Buzzer_Type.__name__ = "Integer32"
_Pdu8341Buzzer_Object = MibScalar
pdu8341Buzzer = _Pdu8341Buzzer_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 3, 10),
    _Pdu8341Buzzer_Type()
)
pdu8341Buzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8341Buzzer.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341Buzzer.setUnits("0 = Off, 1 = On")
_Pdu8341ExtActors_ObjectIdentity = ObjectIdentity
pdu8341ExtActors = _Pdu8341ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 4)
)
_Pdu8341IntSensors_ObjectIdentity = ObjectIdentity
pdu8341IntSensors = _Pdu8341IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5)
)
_Pdu8341PowerChan_ObjectIdentity = ObjectIdentity
pdu8341PowerChan = _Pdu8341PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1)
)


class _Pdu8341ActivePowerChan_Type(Unsigned32):
    """Custom type pdu8341ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu8341ActivePowerChan_Type.__name__ = "Unsigned32"
_Pdu8341ActivePowerChan_Object = MibScalar
pdu8341ActivePowerChan = _Pdu8341ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 1),
    _Pdu8341ActivePowerChan_Type()
)
pdu8341ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341ActivePowerChan.setStatus("current")
_Pdu8341PowerTable_Object = MibTable
pdu8341PowerTable = _Pdu8341PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    pdu8341PowerTable.setStatus("current")
_Pdu8341PowerEntry_Object = MibTableRow
pdu8341PowerEntry = _Pdu8341PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1)
)
pdu8341PowerEntry.setIndexNames(
    (0, "GUDEADS-PDU8341-MIB", "pdu8341PowerIndex"),
)
if mibBuilder.loadTexts:
    pdu8341PowerEntry.setStatus("current")


class _Pdu8341PowerIndex_Type(Integer32):
    """Custom type pdu8341PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Pdu8341PowerIndex_Type.__name__ = "Integer32"
_Pdu8341PowerIndex_Object = MibTableColumn
pdu8341PowerIndex = _Pdu8341PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 1),
    _Pdu8341PowerIndex_Type()
)
pdu8341PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341PowerIndex.setStatus("current")


class _Pdu8341ChanStatus_Type(Integer32):
    """Custom type pdu8341ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu8341ChanStatus_Type.__name__ = "Integer32"
_Pdu8341ChanStatus_Object = MibTableColumn
pdu8341ChanStatus = _Pdu8341ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 2),
    _Pdu8341ChanStatus_Type()
)
pdu8341ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341ChanStatus.setStatus("current")
_Pdu8341AbsEnergyActive_Type = Unsigned32
_Pdu8341AbsEnergyActive_Object = MibTableColumn
pdu8341AbsEnergyActive = _Pdu8341AbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 3),
    _Pdu8341AbsEnergyActive_Type()
)
pdu8341AbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341AbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341AbsEnergyActive.setUnits("Wh")
_Pdu8341PowerActive_Type = Integer32
_Pdu8341PowerActive_Object = MibTableColumn
pdu8341PowerActive = _Pdu8341PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 4),
    _Pdu8341PowerActive_Type()
)
pdu8341PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341PowerActive.setUnits("W")
_Pdu8341Current_Type = Unsigned32
_Pdu8341Current_Object = MibTableColumn
pdu8341Current = _Pdu8341Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 5),
    _Pdu8341Current_Type()
)
pdu8341Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341Current.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341Current.setUnits("mA")
_Pdu8341Voltage_Type = Unsigned32
_Pdu8341Voltage_Object = MibTableColumn
pdu8341Voltage = _Pdu8341Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 6),
    _Pdu8341Voltage_Type()
)
pdu8341Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341Voltage.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341Voltage.setUnits("V")
_Pdu8341Frequency_Type = Unsigned32
_Pdu8341Frequency_Object = MibTableColumn
pdu8341Frequency = _Pdu8341Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 7),
    _Pdu8341Frequency_Type()
)
pdu8341Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341Frequency.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341Frequency.setUnits("0.01 hz")
_Pdu8341PowerFactor_Type = Integer32
_Pdu8341PowerFactor_Object = MibTableColumn
pdu8341PowerFactor = _Pdu8341PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 8),
    _Pdu8341PowerFactor_Type()
)
pdu8341PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341PowerFactor.setUnits("0.001")
_Pdu8341Pangle_Type = Integer32
_Pdu8341Pangle_Object = MibTableColumn
pdu8341Pangle = _Pdu8341Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 9),
    _Pdu8341Pangle_Type()
)
pdu8341Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341Pangle.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341Pangle.setUnits("0.1 degree")
_Pdu8341PowerApparent_Type = Integer32
_Pdu8341PowerApparent_Object = MibTableColumn
pdu8341PowerApparent = _Pdu8341PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 10),
    _Pdu8341PowerApparent_Type()
)
pdu8341PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341PowerApparent.setUnits("VA")
_Pdu8341PowerReactive_Type = Integer32
_Pdu8341PowerReactive_Object = MibTableColumn
pdu8341PowerReactive = _Pdu8341PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 11),
    _Pdu8341PowerReactive_Type()
)
pdu8341PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341PowerReactive.setUnits("VAR")
_Pdu8341AbsEnergyReactive_Type = Unsigned32
_Pdu8341AbsEnergyReactive_Object = MibTableColumn
pdu8341AbsEnergyReactive = _Pdu8341AbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 12),
    _Pdu8341AbsEnergyReactive_Type()
)
pdu8341AbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341AbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341AbsEnergyReactive.setUnits("VARh")
_Pdu8341AbsEnergyActiveResettable_Type = Unsigned32
_Pdu8341AbsEnergyActiveResettable_Object = MibTableColumn
pdu8341AbsEnergyActiveResettable = _Pdu8341AbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 13),
    _Pdu8341AbsEnergyActiveResettable_Type()
)
pdu8341AbsEnergyActiveResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8341AbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341AbsEnergyActiveResettable.setUnits("Wh")
_Pdu8341AbsEnergyReactiveResettable_Type = Unsigned32
_Pdu8341AbsEnergyReactiveResettable_Object = MibTableColumn
pdu8341AbsEnergyReactiveResettable = _Pdu8341AbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 14),
    _Pdu8341AbsEnergyReactiveResettable_Type()
)
pdu8341AbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341AbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341AbsEnergyReactiveResettable.setUnits("VARh")
_Pdu8341ResetTime_Type = Unsigned32
_Pdu8341ResetTime_Object = MibTableColumn
pdu8341ResetTime = _Pdu8341ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 15),
    _Pdu8341ResetTime_Type()
)
pdu8341ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341ResetTime.setUnits("s")
_Pdu8341ForwEnergyActive_Type = Unsigned32
_Pdu8341ForwEnergyActive_Object = MibTableColumn
pdu8341ForwEnergyActive = _Pdu8341ForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 16),
    _Pdu8341ForwEnergyActive_Type()
)
pdu8341ForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341ForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341ForwEnergyActive.setUnits("Wh")
_Pdu8341ForwEnergyReactive_Type = Unsigned32
_Pdu8341ForwEnergyReactive_Object = MibTableColumn
pdu8341ForwEnergyReactive = _Pdu8341ForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 17),
    _Pdu8341ForwEnergyReactive_Type()
)
pdu8341ForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341ForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341ForwEnergyReactive.setUnits("VARh")
_Pdu8341ForwEnergyActiveResettable_Type = Unsigned32
_Pdu8341ForwEnergyActiveResettable_Object = MibTableColumn
pdu8341ForwEnergyActiveResettable = _Pdu8341ForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 18),
    _Pdu8341ForwEnergyActiveResettable_Type()
)
pdu8341ForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341ForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341ForwEnergyActiveResettable.setUnits("Wh")
_Pdu8341ForwEnergyReactiveResettable_Type = Unsigned32
_Pdu8341ForwEnergyReactiveResettable_Object = MibTableColumn
pdu8341ForwEnergyReactiveResettable = _Pdu8341ForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 19),
    _Pdu8341ForwEnergyReactiveResettable_Type()
)
pdu8341ForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341ForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341ForwEnergyReactiveResettable.setUnits("VARh")
_Pdu8341RevEnergyActive_Type = Unsigned32
_Pdu8341RevEnergyActive_Object = MibTableColumn
pdu8341RevEnergyActive = _Pdu8341RevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 20),
    _Pdu8341RevEnergyActive_Type()
)
pdu8341RevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341RevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341RevEnergyActive.setUnits("Wh")
_Pdu8341RevEnergyReactive_Type = Unsigned32
_Pdu8341RevEnergyReactive_Object = MibTableColumn
pdu8341RevEnergyReactive = _Pdu8341RevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 21),
    _Pdu8341RevEnergyReactive_Type()
)
pdu8341RevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341RevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341RevEnergyReactive.setUnits("VARh")
_Pdu8341RevEnergyActiveResettable_Type = Unsigned32
_Pdu8341RevEnergyActiveResettable_Object = MibTableColumn
pdu8341RevEnergyActiveResettable = _Pdu8341RevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 22),
    _Pdu8341RevEnergyActiveResettable_Type()
)
pdu8341RevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341RevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341RevEnergyActiveResettable.setUnits("Wh")
_Pdu8341RevEnergyReactiveResettable_Type = Unsigned32
_Pdu8341RevEnergyReactiveResettable_Object = MibTableColumn
pdu8341RevEnergyReactiveResettable = _Pdu8341RevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 23),
    _Pdu8341RevEnergyReactiveResettable_Type()
)
pdu8341RevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341RevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341RevEnergyReactiveResettable.setUnits("VARh")
_Pdu8341ResidualCurrent_Type = Unsigned32
_Pdu8341ResidualCurrent_Object = MibTableColumn
pdu8341ResidualCurrent = _Pdu8341ResidualCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 5, 1, 2, 1, 24),
    _Pdu8341ResidualCurrent_Type()
)
pdu8341ResidualCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341ResidualCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341ResidualCurrent.setUnits("mA")
_Pdu8341ExtSensors_ObjectIdentity = ObjectIdentity
pdu8341ExtSensors = _Pdu8341ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 6)
)
_Pdu8341SensorTable_Object = MibTable
pdu8341SensorTable = _Pdu8341SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 6, 1)
)
if mibBuilder.loadTexts:
    pdu8341SensorTable.setStatus("current")
_Pdu8341SensorEntry_Object = MibTableRow
pdu8341SensorEntry = _Pdu8341SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 6, 1, 1)
)
pdu8341SensorEntry.setIndexNames(
    (0, "GUDEADS-PDU8341-MIB", "pdu8341SensorIndex"),
)
if mibBuilder.loadTexts:
    pdu8341SensorEntry.setStatus("current")


class _Pdu8341SensorIndex_Type(Integer32):
    """Custom type pdu8341SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu8341SensorIndex_Type.__name__ = "Integer32"
_Pdu8341SensorIndex_Object = MibTableColumn
pdu8341SensorIndex = _Pdu8341SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 6, 1, 1, 1),
    _Pdu8341SensorIndex_Type()
)
pdu8341SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341SensorIndex.setStatus("current")
_Pdu8341TempSensor_Type = Integer32
_Pdu8341TempSensor_Object = MibTableColumn
pdu8341TempSensor = _Pdu8341TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 6, 1, 1, 2),
    _Pdu8341TempSensor_Type()
)
pdu8341TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341TempSensor.setUnits("0.1 degree Celsius")
_Pdu8341HygroSensor_Type = Integer32
_Pdu8341HygroSensor_Object = MibTableColumn
pdu8341HygroSensor = _Pdu8341HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 6, 1, 1, 3),
    _Pdu8341HygroSensor_Type()
)
pdu8341HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341HygroSensor.setUnits("0.1 percent humidity")


class _Pdu8341InputSensor_Type(Integer32):
    """Custom type pdu8341InputSensor based on Integer32"""
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


_Pdu8341InputSensor_Type.__name__ = "Integer32"
_Pdu8341InputSensor_Object = MibTableColumn
pdu8341InputSensor = _Pdu8341InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 6, 1, 1, 4),
    _Pdu8341InputSensor_Type()
)
pdu8341InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341InputSensor.setStatus("current")
_Pdu8341AirPressure_Type = Integer32
_Pdu8341AirPressure_Object = MibTableColumn
pdu8341AirPressure = _Pdu8341AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 6, 1, 1, 5),
    _Pdu8341AirPressure_Type()
)
pdu8341AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Pdu8341DewPoint_Type = Integer32
_Pdu8341DewPoint_Object = MibTableColumn
pdu8341DewPoint = _Pdu8341DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 6, 1, 1, 6),
    _Pdu8341DewPoint_Type()
)
pdu8341DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341DewPoint.setUnits("0.1 degree Celsius")
_Pdu8341DewPointDiff_Type = Integer32
_Pdu8341DewPointDiff_Object = MibTableColumn
pdu8341DewPointDiff = _Pdu8341DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 65, 1, 6, 1, 1, 7),
    _Pdu8341DewPointDiff_Type()
)
pdu8341DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8341DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    pdu8341DewPointDiff.setUnits("0.1 degree Celsius")
_Pdu8341Conf_ObjectIdentity = ObjectIdentity
pdu8341Conf = _Pdu8341Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 2)
)
_Pdu8341Groups_ObjectIdentity = ObjectIdentity
pdu8341Groups = _Pdu8341Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 2, 1)
)
_Pdu8341Compls_ObjectIdentity = ObjectIdentity
pdu8341Compls = _Pdu8341Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 65, 3)
)

# Managed Objects groups

pdu8341BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 65, 2, 1, 1)
)
pdu8341BasicGroup.setObjects(
      *(("GUDEADS-PDU8341-MIB", "pdu8341TrapCtrl"),
        ("GUDEADS-PDU8341-MIB", "pdu8341TrapIPIndex"),
        ("GUDEADS-PDU8341-MIB", "pdu8341TrapAddr"),
        ("GUDEADS-PDU8341-MIB", "pdu8341Buzzer"),
        ("GUDEADS-PDU8341-MIB", "pdu8341ActivePowerChan"),
        ("GUDEADS-PDU8341-MIB", "pdu8341PowerIndex"),
        ("GUDEADS-PDU8341-MIB", "pdu8341ChanStatus"),
        ("GUDEADS-PDU8341-MIB", "pdu8341AbsEnergyActive"),
        ("GUDEADS-PDU8341-MIB", "pdu8341PowerActive"),
        ("GUDEADS-PDU8341-MIB", "pdu8341Current"),
        ("GUDEADS-PDU8341-MIB", "pdu8341Voltage"),
        ("GUDEADS-PDU8341-MIB", "pdu8341Frequency"),
        ("GUDEADS-PDU8341-MIB", "pdu8341PowerFactor"),
        ("GUDEADS-PDU8341-MIB", "pdu8341Pangle"),
        ("GUDEADS-PDU8341-MIB", "pdu8341PowerApparent"),
        ("GUDEADS-PDU8341-MIB", "pdu8341PowerReactive"),
        ("GUDEADS-PDU8341-MIB", "pdu8341AbsEnergyReactive"),
        ("GUDEADS-PDU8341-MIB", "pdu8341AbsEnergyActiveResettable"),
        ("GUDEADS-PDU8341-MIB", "pdu8341AbsEnergyReactiveResettable"),
        ("GUDEADS-PDU8341-MIB", "pdu8341ResetTime"),
        ("GUDEADS-PDU8341-MIB", "pdu8341ForwEnergyActive"),
        ("GUDEADS-PDU8341-MIB", "pdu8341ForwEnergyReactive"),
        ("GUDEADS-PDU8341-MIB", "pdu8341ForwEnergyActiveResettable"),
        ("GUDEADS-PDU8341-MIB", "pdu8341ForwEnergyReactiveResettable"),
        ("GUDEADS-PDU8341-MIB", "pdu8341RevEnergyActive"),
        ("GUDEADS-PDU8341-MIB", "pdu8341RevEnergyReactive"),
        ("GUDEADS-PDU8341-MIB", "pdu8341RevEnergyActiveResettable"),
        ("GUDEADS-PDU8341-MIB", "pdu8341RevEnergyReactiveResettable"),
        ("GUDEADS-PDU8341-MIB", "pdu8341ResidualCurrent"),
        ("GUDEADS-PDU8341-MIB", "pdu8341SensorIndex"),
        ("GUDEADS-PDU8341-MIB", "pdu8341TempSensor"),
        ("GUDEADS-PDU8341-MIB", "pdu8341HygroSensor"),
        ("GUDEADS-PDU8341-MIB", "pdu8341InputSensor"),
        ("GUDEADS-PDU8341-MIB", "pdu8341AirPressure"),
        ("GUDEADS-PDU8341-MIB", "pdu8341DewPoint"),
        ("GUDEADS-PDU8341-MIB", "pdu8341DewPointDiff"))
)
if mibBuilder.loadTexts:
    pdu8341BasicGroup.setStatus("current")


# Notification objects

pdu8341TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 65, 3, 1)
)
pdu8341TempEvtSen.setObjects(
      *(("GUDEADS-PDU8341-MIB", "pdu8341SensorIndex"),
        ("GUDEADS-PDU8341-MIB", "pdu8341TempSensor"))
)
if mibBuilder.loadTexts:
    pdu8341TempEvtSen.setStatus(
        "current"
    )

pdu8341HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 65, 3, 2)
)
pdu8341HygroEvtSen.setObjects(
      *(("GUDEADS-PDU8341-MIB", "pdu8341SensorIndex"),
        ("GUDEADS-PDU8341-MIB", "pdu8341HygroSensor"))
)
if mibBuilder.loadTexts:
    pdu8341HygroEvtSen.setStatus(
        "current"
    )

pdu8341InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 65, 3, 3)
)
pdu8341InputEvtSen.setObjects(
      *(("GUDEADS-PDU8341-MIB", "pdu8341SensorIndex"),
        ("GUDEADS-PDU8341-MIB", "pdu8341InputSensor"))
)
if mibBuilder.loadTexts:
    pdu8341InputEvtSen.setStatus(
        "current"
    )

pdu8341AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 65, 3, 4)
)
pdu8341AirPressureEvtSen.setObjects(
      *(("GUDEADS-PDU8341-MIB", "pdu8341SensorIndex"),
        ("GUDEADS-PDU8341-MIB", "pdu8341AirPressure"))
)
if mibBuilder.loadTexts:
    pdu8341AirPressureEvtSen.setStatus(
        "current"
    )

pdu8341DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 65, 3, 5)
)
pdu8341DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-PDU8341-MIB", "pdu8341SensorIndex"),
        ("GUDEADS-PDU8341-MIB", "pdu8341DewPointDiff"))
)
if mibBuilder.loadTexts:
    pdu8341DewPtDiffEvtSen.setStatus(
        "current"
    )

pdu8341LineAmperageEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 65, 3, 6)
)
pdu8341LineAmperageEvt.setObjects(
      *(("GUDEADS-PDU8341-MIB", "pdu8341PowerIndex"),
        ("GUDEADS-PDU8341-MIB", "pdu8341PowerActive"),
        ("GUDEADS-PDU8341-MIB", "pdu8341Current"),
        ("GUDEADS-PDU8341-MIB", "pdu8341Voltage"),
        ("GUDEADS-PDU8341-MIB", "pdu8341Frequency"),
        ("GUDEADS-PDU8341-MIB", "pdu8341PowerApparent"),
        ("GUDEADS-PDU8341-MIB", "pdu8341PowerReactive"))
)
if mibBuilder.loadTexts:
    pdu8341LineAmperageEvt.setStatus(
        "current"
    )


# Notifications groups

pdu8341NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 65, 2, 1, 2)
)
pdu8341NotificationGroup.setObjects(
      *(("GUDEADS-PDU8341-MIB", "pdu8341TempEvtSen"),
        ("GUDEADS-PDU8341-MIB", "pdu8341HygroEvtSen"),
        ("GUDEADS-PDU8341-MIB", "pdu8341InputEvtSen"),
        ("GUDEADS-PDU8341-MIB", "pdu8341AirPressureEvtSen"),
        ("GUDEADS-PDU8341-MIB", "pdu8341DewPtDiffEvtSen"),
        ("GUDEADS-PDU8341-MIB", "pdu8341LineAmperageEvt"))
)
if mibBuilder.loadTexts:
    pdu8341NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-PDU8341-MIB",
    **{"gudeads": gudeads,
       "gadsPDU8341": gadsPDU8341,
       "pdu8341Objects": pdu8341Objects,
       "pdu8341CommonConfig": pdu8341CommonConfig,
       "pdu8341SNMPaccess": pdu8341SNMPaccess,
       "pdu8341TrapCtrl": pdu8341TrapCtrl,
       "pdu8341TrapIPTable": pdu8341TrapIPTable,
       "pdu8341TrapIPEntry": pdu8341TrapIPEntry,
       "pdu8341TrapIPIndex": pdu8341TrapIPIndex,
       "pdu8341TrapAddr": pdu8341TrapAddr,
       "pdu8341DeviceConfig": pdu8341DeviceConfig,
       "pdu8341IntActors": pdu8341IntActors,
       "pdu8341Buzzer": pdu8341Buzzer,
       "pdu8341ExtActors": pdu8341ExtActors,
       "pdu8341IntSensors": pdu8341IntSensors,
       "pdu8341PowerChan": pdu8341PowerChan,
       "pdu8341ActivePowerChan": pdu8341ActivePowerChan,
       "pdu8341PowerTable": pdu8341PowerTable,
       "pdu8341PowerEntry": pdu8341PowerEntry,
       "pdu8341PowerIndex": pdu8341PowerIndex,
       "pdu8341ChanStatus": pdu8341ChanStatus,
       "pdu8341AbsEnergyActive": pdu8341AbsEnergyActive,
       "pdu8341PowerActive": pdu8341PowerActive,
       "pdu8341Current": pdu8341Current,
       "pdu8341Voltage": pdu8341Voltage,
       "pdu8341Frequency": pdu8341Frequency,
       "pdu8341PowerFactor": pdu8341PowerFactor,
       "pdu8341Pangle": pdu8341Pangle,
       "pdu8341PowerApparent": pdu8341PowerApparent,
       "pdu8341PowerReactive": pdu8341PowerReactive,
       "pdu8341AbsEnergyReactive": pdu8341AbsEnergyReactive,
       "pdu8341AbsEnergyActiveResettable": pdu8341AbsEnergyActiveResettable,
       "pdu8341AbsEnergyReactiveResettable": pdu8341AbsEnergyReactiveResettable,
       "pdu8341ResetTime": pdu8341ResetTime,
       "pdu8341ForwEnergyActive": pdu8341ForwEnergyActive,
       "pdu8341ForwEnergyReactive": pdu8341ForwEnergyReactive,
       "pdu8341ForwEnergyActiveResettable": pdu8341ForwEnergyActiveResettable,
       "pdu8341ForwEnergyReactiveResettable": pdu8341ForwEnergyReactiveResettable,
       "pdu8341RevEnergyActive": pdu8341RevEnergyActive,
       "pdu8341RevEnergyReactive": pdu8341RevEnergyReactive,
       "pdu8341RevEnergyActiveResettable": pdu8341RevEnergyActiveResettable,
       "pdu8341RevEnergyReactiveResettable": pdu8341RevEnergyReactiveResettable,
       "pdu8341ResidualCurrent": pdu8341ResidualCurrent,
       "pdu8341ExtSensors": pdu8341ExtSensors,
       "pdu8341SensorTable": pdu8341SensorTable,
       "pdu8341SensorEntry": pdu8341SensorEntry,
       "pdu8341SensorIndex": pdu8341SensorIndex,
       "pdu8341TempSensor": pdu8341TempSensor,
       "pdu8341HygroSensor": pdu8341HygroSensor,
       "pdu8341InputSensor": pdu8341InputSensor,
       "pdu8341AirPressure": pdu8341AirPressure,
       "pdu8341DewPoint": pdu8341DewPoint,
       "pdu8341DewPointDiff": pdu8341DewPointDiff,
       "pdu8341Conf": pdu8341Conf,
       "pdu8341Groups": pdu8341Groups,
       "pdu8341BasicGroup": pdu8341BasicGroup,
       "pdu8341NotificationGroup": pdu8341NotificationGroup,
       "pdu8341Compls": pdu8341Compls,
       "events": events,
       "pdu8341TempEvtSen": pdu8341TempEvtSen,
       "pdu8341HygroEvtSen": pdu8341HygroEvtSen,
       "pdu8341InputEvtSen": pdu8341InputEvtSen,
       "pdu8341AirPressureEvtSen": pdu8341AirPressureEvtSen,
       "pdu8341DewPtDiffEvtSen": pdu8341DewPtDiffEvtSen,
       "pdu8341LineAmperageEvt": pdu8341LineAmperageEvt}
)
