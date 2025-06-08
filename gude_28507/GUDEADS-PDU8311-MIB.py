# SNMP MIB module (GUDEADS-PDU8311-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gude_28507/GUDEADS-PDU8311-MIB.mib
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

_GadsPDU8311_ObjectIdentity = ObjectIdentity
gadsPDU8311 = _GadsPDU8311_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62)
)
_Pdu8311Objects_ObjectIdentity = ObjectIdentity
pdu8311Objects = _Pdu8311Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1)
)
_Pdu8311CommonConfig_ObjectIdentity = ObjectIdentity
pdu8311CommonConfig = _Pdu8311CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 1)
)
_Pdu8311SNMPaccess_ObjectIdentity = ObjectIdentity
pdu8311SNMPaccess = _Pdu8311SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 1, 1)
)


class _Pdu8311TrapCtrl_Type(Integer32):
    """Custom type pdu8311TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Pdu8311TrapCtrl_Type.__name__ = "Integer32"
_Pdu8311TrapCtrl_Object = MibScalar
pdu8311TrapCtrl = _Pdu8311TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 1, 1, 1),
    _Pdu8311TrapCtrl_Type()
)
pdu8311TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8311TrapCtrl.setStatus("current")
_Pdu8311TrapIPTable_Object = MibTable
pdu8311TrapIPTable = _Pdu8311TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pdu8311TrapIPTable.setStatus("current")
_Pdu8311TrapIPEntry_Object = MibTableRow
pdu8311TrapIPEntry = _Pdu8311TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 1, 1, 2, 1)
)
pdu8311TrapIPEntry.setIndexNames(
    (0, "GUDEADS-PDU8311-MIB", "pdu8311TrapIPIndex"),
)
if mibBuilder.loadTexts:
    pdu8311TrapIPEntry.setStatus("current")


class _Pdu8311TrapIPIndex_Type(Integer32):
    """Custom type pdu8311TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Pdu8311TrapIPIndex_Type.__name__ = "Integer32"
_Pdu8311TrapIPIndex_Object = MibTableColumn
pdu8311TrapIPIndex = _Pdu8311TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 1, 1, 2, 1, 1),
    _Pdu8311TrapIPIndex_Type()
)
pdu8311TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311TrapIPIndex.setStatus("current")


class _Pdu8311TrapAddr_Type(OctetString):
    """Custom type pdu8311TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Pdu8311TrapAddr_Type.__name__ = "OctetString"
_Pdu8311TrapAddr_Object = MibTableColumn
pdu8311TrapAddr = _Pdu8311TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 1, 1, 2, 1, 2),
    _Pdu8311TrapAddr_Type()
)
pdu8311TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8311TrapAddr.setStatus("current")
_Pdu8311DeviceConfig_ObjectIdentity = ObjectIdentity
pdu8311DeviceConfig = _Pdu8311DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 2)
)
_Pdu8311IntActors_ObjectIdentity = ObjectIdentity
pdu8311IntActors = _Pdu8311IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 3)
)
_Pdu8311ExtActors_ObjectIdentity = ObjectIdentity
pdu8311ExtActors = _Pdu8311ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 4)
)
_Pdu8311IntSensors_ObjectIdentity = ObjectIdentity
pdu8311IntSensors = _Pdu8311IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5)
)
_Pdu8311PowerChan_ObjectIdentity = ObjectIdentity
pdu8311PowerChan = _Pdu8311PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1)
)


class _Pdu8311ActivePowerChan_Type(Unsigned32):
    """Custom type pdu8311ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Pdu8311ActivePowerChan_Type.__name__ = "Unsigned32"
_Pdu8311ActivePowerChan_Object = MibScalar
pdu8311ActivePowerChan = _Pdu8311ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 1),
    _Pdu8311ActivePowerChan_Type()
)
pdu8311ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311ActivePowerChan.setStatus("current")
_Pdu8311PowerTable_Object = MibTable
pdu8311PowerTable = _Pdu8311PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    pdu8311PowerTable.setStatus("current")
_Pdu8311PowerEntry_Object = MibTableRow
pdu8311PowerEntry = _Pdu8311PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1)
)
pdu8311PowerEntry.setIndexNames(
    (0, "GUDEADS-PDU8311-MIB", "pdu8311PowerIndex"),
)
if mibBuilder.loadTexts:
    pdu8311PowerEntry.setStatus("current")


class _Pdu8311PowerIndex_Type(Integer32):
    """Custom type pdu8311PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Pdu8311PowerIndex_Type.__name__ = "Integer32"
_Pdu8311PowerIndex_Object = MibTableColumn
pdu8311PowerIndex = _Pdu8311PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 1),
    _Pdu8311PowerIndex_Type()
)
pdu8311PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311PowerIndex.setStatus("current")


class _Pdu8311ChanStatus_Type(Integer32):
    """Custom type pdu8311ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu8311ChanStatus_Type.__name__ = "Integer32"
_Pdu8311ChanStatus_Object = MibTableColumn
pdu8311ChanStatus = _Pdu8311ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 2),
    _Pdu8311ChanStatus_Type()
)
pdu8311ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311ChanStatus.setStatus("current")
_Pdu8311AbsEnergyActive_Type = Unsigned32
_Pdu8311AbsEnergyActive_Object = MibTableColumn
pdu8311AbsEnergyActive = _Pdu8311AbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 3),
    _Pdu8311AbsEnergyActive_Type()
)
pdu8311AbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311AbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311AbsEnergyActive.setUnits("Wh")
_Pdu8311PowerActive_Type = Integer32
_Pdu8311PowerActive_Object = MibTableColumn
pdu8311PowerActive = _Pdu8311PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 4),
    _Pdu8311PowerActive_Type()
)
pdu8311PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311PowerActive.setUnits("W")
_Pdu8311Current_Type = Unsigned32
_Pdu8311Current_Object = MibTableColumn
pdu8311Current = _Pdu8311Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 5),
    _Pdu8311Current_Type()
)
pdu8311Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311Current.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311Current.setUnits("mA")
_Pdu8311Voltage_Type = Unsigned32
_Pdu8311Voltage_Object = MibTableColumn
pdu8311Voltage = _Pdu8311Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 6),
    _Pdu8311Voltage_Type()
)
pdu8311Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311Voltage.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311Voltage.setUnits("V")
_Pdu8311Frequency_Type = Unsigned32
_Pdu8311Frequency_Object = MibTableColumn
pdu8311Frequency = _Pdu8311Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 7),
    _Pdu8311Frequency_Type()
)
pdu8311Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311Frequency.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311Frequency.setUnits("0.01 hz")
_Pdu8311PowerFactor_Type = Integer32
_Pdu8311PowerFactor_Object = MibTableColumn
pdu8311PowerFactor = _Pdu8311PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 8),
    _Pdu8311PowerFactor_Type()
)
pdu8311PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311PowerFactor.setUnits("0.001")
_Pdu8311Pangle_Type = Integer32
_Pdu8311Pangle_Object = MibTableColumn
pdu8311Pangle = _Pdu8311Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 9),
    _Pdu8311Pangle_Type()
)
pdu8311Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311Pangle.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311Pangle.setUnits("0.1 degree")
_Pdu8311PowerApparent_Type = Integer32
_Pdu8311PowerApparent_Object = MibTableColumn
pdu8311PowerApparent = _Pdu8311PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 10),
    _Pdu8311PowerApparent_Type()
)
pdu8311PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311PowerApparent.setUnits("VA")
_Pdu8311PowerReactive_Type = Integer32
_Pdu8311PowerReactive_Object = MibTableColumn
pdu8311PowerReactive = _Pdu8311PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 11),
    _Pdu8311PowerReactive_Type()
)
pdu8311PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311PowerReactive.setUnits("VAR")
_Pdu8311AbsEnergyReactive_Type = Unsigned32
_Pdu8311AbsEnergyReactive_Object = MibTableColumn
pdu8311AbsEnergyReactive = _Pdu8311AbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 12),
    _Pdu8311AbsEnergyReactive_Type()
)
pdu8311AbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311AbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311AbsEnergyReactive.setUnits("VARh")
_Pdu8311AbsEnergyActiveResettable_Type = Unsigned32
_Pdu8311AbsEnergyActiveResettable_Object = MibTableColumn
pdu8311AbsEnergyActiveResettable = _Pdu8311AbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 13),
    _Pdu8311AbsEnergyActiveResettable_Type()
)
pdu8311AbsEnergyActiveResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8311AbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311AbsEnergyActiveResettable.setUnits("Wh")
_Pdu8311AbsEnergyReactiveResettable_Type = Unsigned32
_Pdu8311AbsEnergyReactiveResettable_Object = MibTableColumn
pdu8311AbsEnergyReactiveResettable = _Pdu8311AbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 14),
    _Pdu8311AbsEnergyReactiveResettable_Type()
)
pdu8311AbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311AbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311AbsEnergyReactiveResettable.setUnits("VARh")
_Pdu8311ResetTime_Type = Unsigned32
_Pdu8311ResetTime_Object = MibTableColumn
pdu8311ResetTime = _Pdu8311ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 15),
    _Pdu8311ResetTime_Type()
)
pdu8311ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311ResetTime.setUnits("s")
_Pdu8311ForwEnergyActive_Type = Unsigned32
_Pdu8311ForwEnergyActive_Object = MibTableColumn
pdu8311ForwEnergyActive = _Pdu8311ForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 16),
    _Pdu8311ForwEnergyActive_Type()
)
pdu8311ForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311ForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311ForwEnergyActive.setUnits("Wh")
_Pdu8311ForwEnergyReactive_Type = Unsigned32
_Pdu8311ForwEnergyReactive_Object = MibTableColumn
pdu8311ForwEnergyReactive = _Pdu8311ForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 17),
    _Pdu8311ForwEnergyReactive_Type()
)
pdu8311ForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311ForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311ForwEnergyReactive.setUnits("VARh")
_Pdu8311ForwEnergyActiveResettable_Type = Unsigned32
_Pdu8311ForwEnergyActiveResettable_Object = MibTableColumn
pdu8311ForwEnergyActiveResettable = _Pdu8311ForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 18),
    _Pdu8311ForwEnergyActiveResettable_Type()
)
pdu8311ForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311ForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311ForwEnergyActiveResettable.setUnits("Wh")
_Pdu8311ForwEnergyReactiveResettable_Type = Unsigned32
_Pdu8311ForwEnergyReactiveResettable_Object = MibTableColumn
pdu8311ForwEnergyReactiveResettable = _Pdu8311ForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 19),
    _Pdu8311ForwEnergyReactiveResettable_Type()
)
pdu8311ForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311ForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311ForwEnergyReactiveResettable.setUnits("VARh")
_Pdu8311RevEnergyActive_Type = Unsigned32
_Pdu8311RevEnergyActive_Object = MibTableColumn
pdu8311RevEnergyActive = _Pdu8311RevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 20),
    _Pdu8311RevEnergyActive_Type()
)
pdu8311RevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311RevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311RevEnergyActive.setUnits("Wh")
_Pdu8311RevEnergyReactive_Type = Unsigned32
_Pdu8311RevEnergyReactive_Object = MibTableColumn
pdu8311RevEnergyReactive = _Pdu8311RevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 21),
    _Pdu8311RevEnergyReactive_Type()
)
pdu8311RevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311RevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311RevEnergyReactive.setUnits("VARh")
_Pdu8311RevEnergyActiveResettable_Type = Unsigned32
_Pdu8311RevEnergyActiveResettable_Object = MibTableColumn
pdu8311RevEnergyActiveResettable = _Pdu8311RevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 22),
    _Pdu8311RevEnergyActiveResettable_Type()
)
pdu8311RevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311RevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311RevEnergyActiveResettable.setUnits("Wh")
_Pdu8311RevEnergyReactiveResettable_Type = Unsigned32
_Pdu8311RevEnergyReactiveResettable_Object = MibTableColumn
pdu8311RevEnergyReactiveResettable = _Pdu8311RevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 23),
    _Pdu8311RevEnergyReactiveResettable_Type()
)
pdu8311RevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311RevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311RevEnergyReactiveResettable.setUnits("VARh")
_Pdu8311ResidualCurrent_Type = Unsigned32
_Pdu8311ResidualCurrent_Object = MibTableColumn
pdu8311ResidualCurrent = _Pdu8311ResidualCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 5, 1, 2, 1, 24),
    _Pdu8311ResidualCurrent_Type()
)
pdu8311ResidualCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311ResidualCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311ResidualCurrent.setUnits("mA")
_Pdu8311ExtSensors_ObjectIdentity = ObjectIdentity
pdu8311ExtSensors = _Pdu8311ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 6)
)
_Pdu8311SensorTable_Object = MibTable
pdu8311SensorTable = _Pdu8311SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 6, 1)
)
if mibBuilder.loadTexts:
    pdu8311SensorTable.setStatus("current")
_Pdu8311SensorEntry_Object = MibTableRow
pdu8311SensorEntry = _Pdu8311SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 6, 1, 1)
)
pdu8311SensorEntry.setIndexNames(
    (0, "GUDEADS-PDU8311-MIB", "pdu8311SensorIndex"),
)
if mibBuilder.loadTexts:
    pdu8311SensorEntry.setStatus("current")


class _Pdu8311SensorIndex_Type(Integer32):
    """Custom type pdu8311SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu8311SensorIndex_Type.__name__ = "Integer32"
_Pdu8311SensorIndex_Object = MibTableColumn
pdu8311SensorIndex = _Pdu8311SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 6, 1, 1, 1),
    _Pdu8311SensorIndex_Type()
)
pdu8311SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311SensorIndex.setStatus("current")
_Pdu8311TempSensor_Type = Integer32
_Pdu8311TempSensor_Object = MibTableColumn
pdu8311TempSensor = _Pdu8311TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 6, 1, 1, 2),
    _Pdu8311TempSensor_Type()
)
pdu8311TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311TempSensor.setUnits("0.1 degree Celsius")
_Pdu8311HygroSensor_Type = Integer32
_Pdu8311HygroSensor_Object = MibTableColumn
pdu8311HygroSensor = _Pdu8311HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 6, 1, 1, 3),
    _Pdu8311HygroSensor_Type()
)
pdu8311HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311HygroSensor.setUnits("0.1 percent humidity")


class _Pdu8311InputSensor_Type(Integer32):
    """Custom type pdu8311InputSensor based on Integer32"""
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


_Pdu8311InputSensor_Type.__name__ = "Integer32"
_Pdu8311InputSensor_Object = MibTableColumn
pdu8311InputSensor = _Pdu8311InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 6, 1, 1, 4),
    _Pdu8311InputSensor_Type()
)
pdu8311InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311InputSensor.setStatus("current")
_Pdu8311AirPressure_Type = Integer32
_Pdu8311AirPressure_Object = MibTableColumn
pdu8311AirPressure = _Pdu8311AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 6, 1, 1, 5),
    _Pdu8311AirPressure_Type()
)
pdu8311AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Pdu8311DewPoint_Type = Integer32
_Pdu8311DewPoint_Object = MibTableColumn
pdu8311DewPoint = _Pdu8311DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 6, 1, 1, 6),
    _Pdu8311DewPoint_Type()
)
pdu8311DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311DewPoint.setUnits("0.1 degree Celsius")
_Pdu8311DewPointDiff_Type = Integer32
_Pdu8311DewPointDiff_Object = MibTableColumn
pdu8311DewPointDiff = _Pdu8311DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 62, 1, 6, 1, 1, 7),
    _Pdu8311DewPointDiff_Type()
)
pdu8311DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8311DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    pdu8311DewPointDiff.setUnits("0.1 degree Celsius")
_Pdu8311Conf_ObjectIdentity = ObjectIdentity
pdu8311Conf = _Pdu8311Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 2)
)
_Pdu8311Groups_ObjectIdentity = ObjectIdentity
pdu8311Groups = _Pdu8311Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 2, 1)
)
_Pdu8311Compls_ObjectIdentity = ObjectIdentity
pdu8311Compls = _Pdu8311Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 62, 3)
)

# Managed Objects groups

pdu8311BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 62, 2, 1, 1)
)
pdu8311BasicGroup.setObjects(
      *(("GUDEADS-PDU8311-MIB", "pdu8311TrapCtrl"),
        ("GUDEADS-PDU8311-MIB", "pdu8311TrapIPIndex"),
        ("GUDEADS-PDU8311-MIB", "pdu8311TrapAddr"),
        ("GUDEADS-PDU8311-MIB", "pdu8311ActivePowerChan"),
        ("GUDEADS-PDU8311-MIB", "pdu8311PowerIndex"),
        ("GUDEADS-PDU8311-MIB", "pdu8311ChanStatus"),
        ("GUDEADS-PDU8311-MIB", "pdu8311AbsEnergyActive"),
        ("GUDEADS-PDU8311-MIB", "pdu8311PowerActive"),
        ("GUDEADS-PDU8311-MIB", "pdu8311Current"),
        ("GUDEADS-PDU8311-MIB", "pdu8311Voltage"),
        ("GUDEADS-PDU8311-MIB", "pdu8311Frequency"),
        ("GUDEADS-PDU8311-MIB", "pdu8311PowerFactor"),
        ("GUDEADS-PDU8311-MIB", "pdu8311Pangle"),
        ("GUDEADS-PDU8311-MIB", "pdu8311PowerApparent"),
        ("GUDEADS-PDU8311-MIB", "pdu8311PowerReactive"),
        ("GUDEADS-PDU8311-MIB", "pdu8311AbsEnergyReactive"),
        ("GUDEADS-PDU8311-MIB", "pdu8311AbsEnergyActiveResettable"),
        ("GUDEADS-PDU8311-MIB", "pdu8311AbsEnergyReactiveResettable"),
        ("GUDEADS-PDU8311-MIB", "pdu8311ResetTime"),
        ("GUDEADS-PDU8311-MIB", "pdu8311ForwEnergyActive"),
        ("GUDEADS-PDU8311-MIB", "pdu8311ForwEnergyReactive"),
        ("GUDEADS-PDU8311-MIB", "pdu8311ForwEnergyActiveResettable"),
        ("GUDEADS-PDU8311-MIB", "pdu8311ForwEnergyReactiveResettable"),
        ("GUDEADS-PDU8311-MIB", "pdu8311RevEnergyActive"),
        ("GUDEADS-PDU8311-MIB", "pdu8311RevEnergyReactive"),
        ("GUDEADS-PDU8311-MIB", "pdu8311RevEnergyActiveResettable"),
        ("GUDEADS-PDU8311-MIB", "pdu8311RevEnergyReactiveResettable"),
        ("GUDEADS-PDU8311-MIB", "pdu8311ResidualCurrent"),
        ("GUDEADS-PDU8311-MIB", "pdu8311SensorIndex"),
        ("GUDEADS-PDU8311-MIB", "pdu8311TempSensor"),
        ("GUDEADS-PDU8311-MIB", "pdu8311HygroSensor"),
        ("GUDEADS-PDU8311-MIB", "pdu8311InputSensor"),
        ("GUDEADS-PDU8311-MIB", "pdu8311AirPressure"),
        ("GUDEADS-PDU8311-MIB", "pdu8311DewPoint"),
        ("GUDEADS-PDU8311-MIB", "pdu8311DewPointDiff"))
)
if mibBuilder.loadTexts:
    pdu8311BasicGroup.setStatus("current")


# Notification objects

pdu8311TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 62, 3, 1)
)
pdu8311TempEvtSen.setObjects(
      *(("GUDEADS-PDU8311-MIB", "pdu8311SensorIndex"),
        ("GUDEADS-PDU8311-MIB", "pdu8311TempSensor"))
)
if mibBuilder.loadTexts:
    pdu8311TempEvtSen.setStatus(
        "current"
    )

pdu8311HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 62, 3, 2)
)
pdu8311HygroEvtSen.setObjects(
      *(("GUDEADS-PDU8311-MIB", "pdu8311SensorIndex"),
        ("GUDEADS-PDU8311-MIB", "pdu8311HygroSensor"))
)
if mibBuilder.loadTexts:
    pdu8311HygroEvtSen.setStatus(
        "current"
    )

pdu8311InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 62, 3, 3)
)
pdu8311InputEvtSen.setObjects(
      *(("GUDEADS-PDU8311-MIB", "pdu8311SensorIndex"),
        ("GUDEADS-PDU8311-MIB", "pdu8311InputSensor"))
)
if mibBuilder.loadTexts:
    pdu8311InputEvtSen.setStatus(
        "current"
    )

pdu8311AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 62, 3, 4)
)
pdu8311AirPressureEvtSen.setObjects(
      *(("GUDEADS-PDU8311-MIB", "pdu8311SensorIndex"),
        ("GUDEADS-PDU8311-MIB", "pdu8311AirPressure"))
)
if mibBuilder.loadTexts:
    pdu8311AirPressureEvtSen.setStatus(
        "current"
    )

pdu8311DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 62, 3, 5)
)
pdu8311DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-PDU8311-MIB", "pdu8311SensorIndex"),
        ("GUDEADS-PDU8311-MIB", "pdu8311DewPointDiff"))
)
if mibBuilder.loadTexts:
    pdu8311DewPtDiffEvtSen.setStatus(
        "current"
    )

pdu8311LineAmperageEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 62, 3, 6)
)
pdu8311LineAmperageEvt.setObjects(
      *(("GUDEADS-PDU8311-MIB", "pdu8311PowerIndex"),
        ("GUDEADS-PDU8311-MIB", "pdu8311PowerActive"),
        ("GUDEADS-PDU8311-MIB", "pdu8311Current"),
        ("GUDEADS-PDU8311-MIB", "pdu8311Voltage"),
        ("GUDEADS-PDU8311-MIB", "pdu8311Frequency"),
        ("GUDEADS-PDU8311-MIB", "pdu8311PowerApparent"),
        ("GUDEADS-PDU8311-MIB", "pdu8311PowerReactive"))
)
if mibBuilder.loadTexts:
    pdu8311LineAmperageEvt.setStatus(
        "current"
    )


# Notifications groups

pdu8311NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 62, 2, 1, 2)
)
pdu8311NotificationGroup.setObjects(
      *(("GUDEADS-PDU8311-MIB", "pdu8311TempEvtSen"),
        ("GUDEADS-PDU8311-MIB", "pdu8311HygroEvtSen"),
        ("GUDEADS-PDU8311-MIB", "pdu8311InputEvtSen"),
        ("GUDEADS-PDU8311-MIB", "pdu8311LineAmperageEvt"),
        ("GUDEADS-PDU8311-MIB", "pdu8311AirPressureEvtSen"),
        ("GUDEADS-PDU8311-MIB", "pdu8311DewPtDiffEvtSen"))
)
if mibBuilder.loadTexts:
    pdu8311NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-PDU8311-MIB",
    **{"gudeads": gudeads,
       "gadsPDU8311": gadsPDU8311,
       "pdu8311Objects": pdu8311Objects,
       "pdu8311CommonConfig": pdu8311CommonConfig,
       "pdu8311SNMPaccess": pdu8311SNMPaccess,
       "pdu8311TrapCtrl": pdu8311TrapCtrl,
       "pdu8311TrapIPTable": pdu8311TrapIPTable,
       "pdu8311TrapIPEntry": pdu8311TrapIPEntry,
       "pdu8311TrapIPIndex": pdu8311TrapIPIndex,
       "pdu8311TrapAddr": pdu8311TrapAddr,
       "pdu8311DeviceConfig": pdu8311DeviceConfig,
       "pdu8311IntActors": pdu8311IntActors,
       "pdu8311ExtActors": pdu8311ExtActors,
       "pdu8311IntSensors": pdu8311IntSensors,
       "pdu8311PowerChan": pdu8311PowerChan,
       "pdu8311ActivePowerChan": pdu8311ActivePowerChan,
       "pdu8311PowerTable": pdu8311PowerTable,
       "pdu8311PowerEntry": pdu8311PowerEntry,
       "pdu8311PowerIndex": pdu8311PowerIndex,
       "pdu8311ChanStatus": pdu8311ChanStatus,
       "pdu8311AbsEnergyActive": pdu8311AbsEnergyActive,
       "pdu8311PowerActive": pdu8311PowerActive,
       "pdu8311Current": pdu8311Current,
       "pdu8311Voltage": pdu8311Voltage,
       "pdu8311Frequency": pdu8311Frequency,
       "pdu8311PowerFactor": pdu8311PowerFactor,
       "pdu8311Pangle": pdu8311Pangle,
       "pdu8311PowerApparent": pdu8311PowerApparent,
       "pdu8311PowerReactive": pdu8311PowerReactive,
       "pdu8311AbsEnergyReactive": pdu8311AbsEnergyReactive,
       "pdu8311AbsEnergyActiveResettable": pdu8311AbsEnergyActiveResettable,
       "pdu8311AbsEnergyReactiveResettable": pdu8311AbsEnergyReactiveResettable,
       "pdu8311ResetTime": pdu8311ResetTime,
       "pdu8311ForwEnergyActive": pdu8311ForwEnergyActive,
       "pdu8311ForwEnergyReactive": pdu8311ForwEnergyReactive,
       "pdu8311ForwEnergyActiveResettable": pdu8311ForwEnergyActiveResettable,
       "pdu8311ForwEnergyReactiveResettable": pdu8311ForwEnergyReactiveResettable,
       "pdu8311RevEnergyActive": pdu8311RevEnergyActive,
       "pdu8311RevEnergyReactive": pdu8311RevEnergyReactive,
       "pdu8311RevEnergyActiveResettable": pdu8311RevEnergyActiveResettable,
       "pdu8311RevEnergyReactiveResettable": pdu8311RevEnergyReactiveResettable,
       "pdu8311ResidualCurrent": pdu8311ResidualCurrent,
       "pdu8311ExtSensors": pdu8311ExtSensors,
       "pdu8311SensorTable": pdu8311SensorTable,
       "pdu8311SensorEntry": pdu8311SensorEntry,
       "pdu8311SensorIndex": pdu8311SensorIndex,
       "pdu8311TempSensor": pdu8311TempSensor,
       "pdu8311HygroSensor": pdu8311HygroSensor,
       "pdu8311InputSensor": pdu8311InputSensor,
       "pdu8311AirPressure": pdu8311AirPressure,
       "pdu8311DewPoint": pdu8311DewPoint,
       "pdu8311DewPointDiff": pdu8311DewPointDiff,
       "pdu8311Conf": pdu8311Conf,
       "pdu8311Groups": pdu8311Groups,
       "pdu8311BasicGroup": pdu8311BasicGroup,
       "pdu8311NotificationGroup": pdu8311NotificationGroup,
       "pdu8311Compls": pdu8311Compls,
       "events": events,
       "pdu8311TempEvtSen": pdu8311TempEvtSen,
       "pdu8311HygroEvtSen": pdu8311HygroEvtSen,
       "pdu8311InputEvtSen": pdu8311InputEvtSen,
       "pdu8311AirPressureEvtSen": pdu8311AirPressureEvtSen,
       "pdu8311DewPtDiffEvtSen": pdu8311DewPtDiffEvtSen,
       "pdu8311LineAmperageEvt": pdu8311LineAmperageEvt}
)
