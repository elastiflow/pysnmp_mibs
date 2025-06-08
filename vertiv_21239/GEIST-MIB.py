# SNMP MIB module (GEIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_21239/GEIST-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:17:19 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

geistmfg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21239)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Geist_ObjectIdentity = ObjectIdentity
geist = _Geist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 1)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1)
)
_ProductTitle_Type = DisplayString
_ProductTitle_Object = MibScalar
productTitle = _ProductTitle_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 1),
    _ProductTitle_Type()
)
productTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productTitle.setStatus("current")
_ProductVersion_Type = DisplayString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 2),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")
_ProductFriendlyName_Type = DisplayString
_ProductFriendlyName_Object = MibScalar
productFriendlyName = _ProductFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 3),
    _ProductFriendlyName_Type()
)
productFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productFriendlyName.setStatus("current")
_ProductMacAddress_Type = DisplayString
_ProductMacAddress_Object = MibScalar
productMacAddress = _ProductMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 4),
    _ProductMacAddress_Type()
)
productMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMacAddress.setStatus("current")
_ProductUrl_Type = DisplayString
_ProductUrl_Object = MibScalar
productUrl = _ProductUrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 5),
    _ProductUrl_Type()
)
productUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productUrl.setStatus("current")


class _AlarmTripType_Type(Integer32):
    """Custom type alarmTripType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AlarmTripType_Type.__name__ = "Integer32"
_AlarmTripType_Object = MibScalar
alarmTripType = _AlarmTripType_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 6),
    _AlarmTripType_Type()
)
alarmTripType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTripType.setStatus("current")
_ProductHardware_Type = DisplayString
_ProductHardware_Object = MibScalar
productHardware = _ProductHardware_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 7),
    _ProductHardware_Type()
)
productHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productHardware.setStatus("current")
_SensorCountsBase_ObjectIdentity = ObjectIdentity
sensorCountsBase = _SensorCountsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8)
)
_SensorCounts_ObjectIdentity = ObjectIdentity
sensorCounts = _SensorCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1)
)


class _ClimateCount_Type(Integer32):
    """Custom type climateCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ClimateCount_Type.__name__ = "Integer32"
_ClimateCount_Object = MibScalar
climateCount = _ClimateCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 2),
    _ClimateCount_Type()
)
climateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateCount.setStatus("current")


class _PowerMonitorCount_Type(Integer32):
    """Custom type powerMonitorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PowerMonitorCount_Type.__name__ = "Integer32"
_PowerMonitorCount_Object = MibScalar
powerMonitorCount = _PowerMonitorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 3),
    _PowerMonitorCount_Type()
)
powerMonitorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerMonitorCount.setStatus("current")


class _TempSensorCount_Type(Integer32):
    """Custom type tempSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TempSensorCount_Type.__name__ = "Integer32"
_TempSensorCount_Object = MibScalar
tempSensorCount = _TempSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 4),
    _TempSensorCount_Type()
)
tempSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorCount.setStatus("current")


class _AirflowSensorCount_Type(Integer32):
    """Custom type airflowSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AirflowSensorCount_Type.__name__ = "Integer32"
_AirflowSensorCount_Object = MibScalar
airflowSensorCount = _AirflowSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 5),
    _AirflowSensorCount_Type()
)
airflowSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airflowSensorCount.setStatus("current")


class _PowerOnlyCount_Type(Integer32):
    """Custom type powerOnlyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PowerOnlyCount_Type.__name__ = "Integer32"
_PowerOnlyCount_Object = MibScalar
powerOnlyCount = _PowerOnlyCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 6),
    _PowerOnlyCount_Type()
)
powerOnlyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnlyCount.setStatus("current")


class _DoorSensorCount_Type(Integer32):
    """Custom type doorSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DoorSensorCount_Type.__name__ = "Integer32"
_DoorSensorCount_Object = MibScalar
doorSensorCount = _DoorSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 7),
    _DoorSensorCount_Type()
)
doorSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSensorCount.setStatus("current")


class _WaterSensorCount_Type(Integer32):
    """Custom type waterSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WaterSensorCount_Type.__name__ = "Integer32"
_WaterSensorCount_Object = MibScalar
waterSensorCount = _WaterSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 8),
    _WaterSensorCount_Type()
)
waterSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterSensorCount.setStatus("current")


class _CurrentSensorCount_Type(Integer32):
    """Custom type currentSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CurrentSensorCount_Type.__name__ = "Integer32"
_CurrentSensorCount_Object = MibScalar
currentSensorCount = _CurrentSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 9),
    _CurrentSensorCount_Type()
)
currentSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSensorCount.setStatus("current")


class _MillivoltSensorCount_Type(Integer32):
    """Custom type millivoltSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MillivoltSensorCount_Type.__name__ = "Integer32"
_MillivoltSensorCount_Object = MibScalar
millivoltSensorCount = _MillivoltSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 10),
    _MillivoltSensorCount_Type()
)
millivoltSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    millivoltSensorCount.setStatus("current")


class _Power3ChSensorCount_Type(Integer32):
    """Custom type power3ChSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Power3ChSensorCount_Type.__name__ = "Integer32"
_Power3ChSensorCount_Object = MibScalar
power3ChSensorCount = _Power3ChSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 11),
    _Power3ChSensorCount_Type()
)
power3ChSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power3ChSensorCount.setStatus("current")


class _OutletCount_Type(Integer32):
    """Custom type outletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_OutletCount_Type.__name__ = "Integer32"
_OutletCount_Object = MibScalar
outletCount = _OutletCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 12),
    _OutletCount_Type()
)
outletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCount.setStatus("current")


class _VsfcCount_Type(Integer32):
    """Custom type vsfcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_VsfcCount_Type.__name__ = "Integer32"
_VsfcCount_Object = MibScalar
vsfcCount = _VsfcCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 13),
    _VsfcCount_Type()
)
vsfcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcCount.setStatus("current")


class _Ctrl3ChCount_Type(Integer32):
    """Custom type ctrl3ChCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Ctrl3ChCount_Type.__name__ = "Integer32"
_Ctrl3ChCount_Object = MibScalar
ctrl3ChCount = _Ctrl3ChCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 14),
    _Ctrl3ChCount_Type()
)
ctrl3ChCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChCount.setStatus("current")


class _CtrlGrpAmpsCount_Type(Integer32):
    """Custom type ctrlGrpAmpsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CtrlGrpAmpsCount_Type.__name__ = "Integer32"
_CtrlGrpAmpsCount_Object = MibScalar
ctrlGrpAmpsCount = _CtrlGrpAmpsCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 15),
    _CtrlGrpAmpsCount_Type()
)
ctrlGrpAmpsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsCount.setStatus("current")


class _CtrlOutputCount_Type(Integer32):
    """Custom type ctrlOutputCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CtrlOutputCount_Type.__name__ = "Integer32"
_CtrlOutputCount_Object = MibScalar
ctrlOutputCount = _CtrlOutputCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 16),
    _CtrlOutputCount_Type()
)
ctrlOutputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutputCount.setStatus("current")


class _DewpointSensorCount_Type(Integer32):
    """Custom type dewpointSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DewpointSensorCount_Type.__name__ = "Integer32"
_DewpointSensorCount_Object = MibScalar
dewpointSensorCount = _DewpointSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 17),
    _DewpointSensorCount_Type()
)
dewpointSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpointSensorCount.setStatus("current")


class _DigitalSensorCount_Type(Integer32):
    """Custom type digitalSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DigitalSensorCount_Type.__name__ = "Integer32"
_DigitalSensorCount_Object = MibScalar
digitalSensorCount = _DigitalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 18),
    _DigitalSensorCount_Type()
)
digitalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalSensorCount.setStatus("current")


class _DstsSensorCount_Type(Integer32):
    """Custom type dstsSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DstsSensorCount_Type.__name__ = "Integer32"
_DstsSensorCount_Object = MibScalar
dstsSensorCount = _DstsSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 19),
    _DstsSensorCount_Type()
)
dstsSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsSensorCount.setStatus("current")


class _CpmSensorCount_Type(Integer32):
    """Custom type cpmSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CpmSensorCount_Type.__name__ = "Integer32"
_CpmSensorCount_Object = MibScalar
cpmSensorCount = _CpmSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 20),
    _CpmSensorCount_Type()
)
cpmSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmSensorCount.setStatus("current")


class _SmokeAlarmSensorCount_Type(Integer32):
    """Custom type smokeAlarmSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SmokeAlarmSensorCount_Type.__name__ = "Integer32"
_SmokeAlarmSensorCount_Object = MibScalar
smokeAlarmSensorCount = _SmokeAlarmSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 21),
    _SmokeAlarmSensorCount_Type()
)
smokeAlarmSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeAlarmSensorCount.setStatus("current")


class _Neg48VdcSensorCount_Type(Integer32):
    """Custom type neg48VdcSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Neg48VdcSensorCount_Type.__name__ = "Integer32"
_Neg48VdcSensorCount_Object = MibScalar
neg48VdcSensorCount = _Neg48VdcSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 22),
    _Neg48VdcSensorCount_Type()
)
neg48VdcSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neg48VdcSensorCount.setStatus("current")


class _Pos30VdcSensorCount_Type(Integer32):
    """Custom type pos30VdcSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Pos30VdcSensorCount_Type.__name__ = "Integer32"
_Pos30VdcSensorCount_Object = MibScalar
pos30VdcSensorCount = _Pos30VdcSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 23),
    _Pos30VdcSensorCount_Type()
)
pos30VdcSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos30VdcSensorCount.setStatus("current")


class _AnalogSensorCount_Type(Integer32):
    """Custom type analogSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AnalogSensorCount_Type.__name__ = "Integer32"
_AnalogSensorCount_Object = MibScalar
analogSensorCount = _AnalogSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 24),
    _AnalogSensorCount_Type()
)
analogSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogSensorCount.setStatus("current")


class _Ctrl3ChIECCount_Type(Integer32):
    """Custom type ctrl3ChIECCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Ctrl3ChIECCount_Type.__name__ = "Integer32"
_Ctrl3ChIECCount_Object = MibScalar
ctrl3ChIECCount = _Ctrl3ChIECCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 25),
    _Ctrl3ChIECCount_Type()
)
ctrl3ChIECCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECCount.setStatus("current")


class _AirSpeedSwitchSensorCount_Type(Integer32):
    """Custom type airSpeedSwitchSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AirSpeedSwitchSensorCount_Type.__name__ = "Integer32"
_AirSpeedSwitchSensorCount_Object = MibScalar
airSpeedSwitchSensorCount = _AirSpeedSwitchSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 1, 8, 1, 26),
    _AirSpeedSwitchSensorCount_Type()
)
airSpeedSwitchSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airSpeedSwitchSensorCount.setStatus("current")
_ClimateTable_Object = MibTable
climateTable = _ClimateTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2)
)
if mibBuilder.loadTexts:
    climateTable.setStatus("current")
_ClimateEntry_Object = MibTableRow
climateEntry = _ClimateEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1)
)
climateEntry.setIndexNames(
    (0, "GEIST-MIB", "climateIndex"),
)
if mibBuilder.loadTexts:
    climateEntry.setStatus("current")


class _ClimateIndex_Type(Integer32):
    """Custom type climateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ClimateIndex_Type.__name__ = "Integer32"
_ClimateIndex_Object = MibTableColumn
climateIndex = _ClimateIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 1),
    _ClimateIndex_Type()
)
climateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    climateIndex.setStatus("current")
_ClimateSerial_Type = DisplayString
_ClimateSerial_Object = MibTableColumn
climateSerial = _ClimateSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 2),
    _ClimateSerial_Type()
)
climateSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateSerial.setStatus("current")
_ClimateName_Type = DisplayString
_ClimateName_Object = MibTableColumn
climateName = _ClimateName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 3),
    _ClimateName_Type()
)
climateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateName.setStatus("current")
_ClimateAvail_Type = Unsigned32
_ClimateAvail_Object = MibTableColumn
climateAvail = _ClimateAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 4),
    _ClimateAvail_Type()
)
climateAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateAvail.setStatus("current")


class _ClimateTempC_Type(Integer32):
    """Custom type climateTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 123),
    )


_ClimateTempC_Type.__name__ = "Integer32"
_ClimateTempC_Object = MibTableColumn
climateTempC = _ClimateTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 5),
    _ClimateTempC_Type()
)
climateTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateTempC.setStatus("current")
if mibBuilder.loadTexts:
    climateTempC.setUnits("Degrees Celsius")


class _ClimateHumidity_Type(Integer32):
    """Custom type climateHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateHumidity_Type.__name__ = "Integer32"
_ClimateHumidity_Object = MibTableColumn
climateHumidity = _ClimateHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 6),
    _ClimateHumidity_Type()
)
climateHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateHumidity.setStatus("current")
if mibBuilder.loadTexts:
    climateHumidity.setUnits("%")


class _ClimateAirflow_Type(Integer32):
    """Custom type climateAirflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateAirflow_Type.__name__ = "Integer32"
_ClimateAirflow_Object = MibTableColumn
climateAirflow = _ClimateAirflow_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 7),
    _ClimateAirflow_Type()
)
climateAirflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateAirflow.setStatus("current")


class _ClimateLight_Type(Integer32):
    """Custom type climateLight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateLight_Type.__name__ = "Integer32"
_ClimateLight_Object = MibTableColumn
climateLight = _ClimateLight_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 8),
    _ClimateLight_Type()
)
climateLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateLight.setStatus("current")


class _ClimateSound_Type(Integer32):
    """Custom type climateSound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateSound_Type.__name__ = "Integer32"
_ClimateSound_Object = MibTableColumn
climateSound = _ClimateSound_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 9),
    _ClimateSound_Type()
)
climateSound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateSound.setStatus("current")


class _ClimateIO1_Type(Integer32):
    """Custom type climateIO1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateIO1_Type.__name__ = "Integer32"
_ClimateIO1_Object = MibTableColumn
climateIO1 = _ClimateIO1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 10),
    _ClimateIO1_Type()
)
climateIO1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateIO1.setStatus("current")


class _ClimateIO2_Type(Integer32):
    """Custom type climateIO2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateIO2_Type.__name__ = "Integer32"
_ClimateIO2_Object = MibTableColumn
climateIO2 = _ClimateIO2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 11),
    _ClimateIO2_Type()
)
climateIO2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateIO2.setStatus("current")


class _ClimateIO3_Type(Integer32):
    """Custom type climateIO3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateIO3_Type.__name__ = "Integer32"
_ClimateIO3_Object = MibTableColumn
climateIO3 = _ClimateIO3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 12),
    _ClimateIO3_Type()
)
climateIO3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateIO3.setStatus("current")
_ClimateVolts_Type = Unsigned32
_ClimateVolts_Object = MibTableColumn
climateVolts = _ClimateVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 13),
    _ClimateVolts_Type()
)
climateVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateVolts.setStatus("current")
if mibBuilder.loadTexts:
    climateVolts.setUnits("Volts (rms)")
_ClimateVoltPeak_Type = Unsigned32
_ClimateVoltPeak_Object = MibTableColumn
climateVoltPeak = _ClimateVoltPeak_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 14),
    _ClimateVoltPeak_Type()
)
climateVoltPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateVoltPeak.setStatus("current")
if mibBuilder.loadTexts:
    climateVoltPeak.setUnits("Volts (rms)")
_ClimateDeciAmpsA_Type = Unsigned32
_ClimateDeciAmpsA_Object = MibTableColumn
climateDeciAmpsA = _ClimateDeciAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 15),
    _ClimateDeciAmpsA_Type()
)
climateDeciAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDeciAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    climateDeciAmpsA.setUnits("0.1 Amps (rms)")
_ClimateAmpPeakA_Type = Unsigned32
_ClimateAmpPeakA_Object = MibTableColumn
climateAmpPeakA = _ClimateAmpPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 16),
    _ClimateAmpPeakA_Type()
)
climateAmpPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateAmpPeakA.setStatus("current")
if mibBuilder.loadTexts:
    climateAmpPeakA.setUnits("0.1 Amps (rms)")
_ClimateRealPowerA_Type = Unsigned32
_ClimateRealPowerA_Object = MibTableColumn
climateRealPowerA = _ClimateRealPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 17),
    _ClimateRealPowerA_Type()
)
climateRealPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRealPowerA.setStatus("current")
if mibBuilder.loadTexts:
    climateRealPowerA.setUnits("Watts")
_ClimateApparentPowerA_Type = Unsigned32
_ClimateApparentPowerA_Object = MibTableColumn
climateApparentPowerA = _ClimateApparentPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 18),
    _ClimateApparentPowerA_Type()
)
climateApparentPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateApparentPowerA.setStatus("current")
if mibBuilder.loadTexts:
    climateApparentPowerA.setUnits("Volt-Amps")
_ClimatePowerFactorA_Type = Unsigned32
_ClimatePowerFactorA_Object = MibTableColumn
climatePowerFactorA = _ClimatePowerFactorA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 19),
    _ClimatePowerFactorA_Type()
)
climatePowerFactorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climatePowerFactorA.setStatus("current")
if mibBuilder.loadTexts:
    climatePowerFactorA.setUnits("%")
_ClimateDeciAmpsB_Type = Unsigned32
_ClimateDeciAmpsB_Object = MibTableColumn
climateDeciAmpsB = _ClimateDeciAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 20),
    _ClimateDeciAmpsB_Type()
)
climateDeciAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDeciAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    climateDeciAmpsB.setUnits("0.1 Amps (rms)")
_ClimateDeciAmpPeakB_Type = Unsigned32
_ClimateDeciAmpPeakB_Object = MibTableColumn
climateDeciAmpPeakB = _ClimateDeciAmpPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 21),
    _ClimateDeciAmpPeakB_Type()
)
climateDeciAmpPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDeciAmpPeakB.setStatus("current")
if mibBuilder.loadTexts:
    climateDeciAmpPeakB.setUnits("0.1 Amps (rms)")
_ClimateRealPowerB_Type = Unsigned32
_ClimateRealPowerB_Object = MibTableColumn
climateRealPowerB = _ClimateRealPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 22),
    _ClimateRealPowerB_Type()
)
climateRealPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRealPowerB.setStatus("current")
if mibBuilder.loadTexts:
    climateRealPowerB.setUnits("Watts")
_ClimateApparentPowerB_Type = Unsigned32
_ClimateApparentPowerB_Object = MibTableColumn
climateApparentPowerB = _ClimateApparentPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 23),
    _ClimateApparentPowerB_Type()
)
climateApparentPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateApparentPowerB.setStatus("current")
if mibBuilder.loadTexts:
    climateApparentPowerB.setUnits("Volt-Amps")
_ClimatePowerFactorB_Type = Unsigned32
_ClimatePowerFactorB_Object = MibTableColumn
climatePowerFactorB = _ClimatePowerFactorB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 24),
    _ClimatePowerFactorB_Type()
)
climatePowerFactorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climatePowerFactorB.setStatus("current")
if mibBuilder.loadTexts:
    climatePowerFactorB.setUnits("%")
_ClimateDeciAmpsC_Type = Unsigned32
_ClimateDeciAmpsC_Object = MibTableColumn
climateDeciAmpsC = _ClimateDeciAmpsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 25),
    _ClimateDeciAmpsC_Type()
)
climateDeciAmpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDeciAmpsC.setStatus("current")
if mibBuilder.loadTexts:
    climateDeciAmpsC.setUnits("0.1 Amps (rms)")
_ClimateDeciAmpPeakC_Type = Unsigned32
_ClimateDeciAmpPeakC_Object = MibTableColumn
climateDeciAmpPeakC = _ClimateDeciAmpPeakC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 26),
    _ClimateDeciAmpPeakC_Type()
)
climateDeciAmpPeakC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDeciAmpPeakC.setStatus("current")
if mibBuilder.loadTexts:
    climateDeciAmpPeakC.setUnits("0.1 Amps (rms)")
_ClimateRealPowerC_Type = Unsigned32
_ClimateRealPowerC_Object = MibTableColumn
climateRealPowerC = _ClimateRealPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 27),
    _ClimateRealPowerC_Type()
)
climateRealPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRealPowerC.setStatus("current")
if mibBuilder.loadTexts:
    climateRealPowerC.setUnits("Watts")
_ClimateApparentPowerC_Type = Unsigned32
_ClimateApparentPowerC_Object = MibTableColumn
climateApparentPowerC = _ClimateApparentPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 28),
    _ClimateApparentPowerC_Type()
)
climateApparentPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateApparentPowerC.setStatus("current")
if mibBuilder.loadTexts:
    climateApparentPowerC.setUnits("Volt-Amps")
_ClimatePowerFactorC_Type = Unsigned32
_ClimatePowerFactorC_Object = MibTableColumn
climatePowerFactorC = _ClimatePowerFactorC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 2, 1, 29),
    _ClimatePowerFactorC_Type()
)
climatePowerFactorC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climatePowerFactorC.setStatus("current")
if mibBuilder.loadTexts:
    climatePowerFactorC.setUnits("%")
_PowerMonitorTable_Object = MibTable
powerMonitorTable = _PowerMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3)
)
if mibBuilder.loadTexts:
    powerMonitorTable.setStatus("current")
_PowerMonitorEntry_Object = MibTableRow
powerMonitorEntry = _PowerMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1)
)
powerMonitorEntry.setIndexNames(
    (0, "GEIST-MIB", "powMonIndex"),
)
if mibBuilder.loadTexts:
    powerMonitorEntry.setStatus("current")


class _PowMonIndex_Type(Integer32):
    """Custom type powMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PowMonIndex_Type.__name__ = "Integer32"
_PowMonIndex_Object = MibTableColumn
powMonIndex = _PowMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 1),
    _PowMonIndex_Type()
)
powMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powMonIndex.setStatus("current")
_PowMonSerial_Type = DisplayString
_PowMonSerial_Object = MibTableColumn
powMonSerial = _PowMonSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 2),
    _PowMonSerial_Type()
)
powMonSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonSerial.setStatus("current")
_PowMonName_Type = DisplayString
_PowMonName_Object = MibTableColumn
powMonName = _PowMonName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 3),
    _PowMonName_Type()
)
powMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonName.setStatus("current")
_PowMonAvail_Type = Unsigned32
_PowMonAvail_Object = MibTableColumn
powMonAvail = _PowMonAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 4),
    _PowMonAvail_Type()
)
powMonAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonAvail.setStatus("current")
_PowMonKWattHrs_Type = Unsigned32
_PowMonKWattHrs_Object = MibTableColumn
powMonKWattHrs = _PowMonKWattHrs_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 5),
    _PowMonKWattHrs_Type()
)
powMonKWattHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonKWattHrs.setStatus("current")
if mibBuilder.loadTexts:
    powMonKWattHrs.setUnits("KWh")
_PowMonVolts_Type = Unsigned32
_PowMonVolts_Object = MibTableColumn
powMonVolts = _PowMonVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 6),
    _PowMonVolts_Type()
)
powMonVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonVolts.setStatus("current")
if mibBuilder.loadTexts:
    powMonVolts.setUnits("Volts (rms)")
_PowMonVoltMax_Type = Unsigned32
_PowMonVoltMax_Object = MibTableColumn
powMonVoltMax = _PowMonVoltMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 7),
    _PowMonVoltMax_Type()
)
powMonVoltMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonVoltMax.setStatus("current")
if mibBuilder.loadTexts:
    powMonVoltMax.setUnits("Volts (rms)")
_PowMonVoltMin_Type = Unsigned32
_PowMonVoltMin_Object = MibTableColumn
powMonVoltMin = _PowMonVoltMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 8),
    _PowMonVoltMin_Type()
)
powMonVoltMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonVoltMin.setStatus("current")
if mibBuilder.loadTexts:
    powMonVoltMin.setUnits("Volts (rms)")
_PowMonVoltPeak_Type = Unsigned32
_PowMonVoltPeak_Object = MibTableColumn
powMonVoltPeak = _PowMonVoltPeak_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 9),
    _PowMonVoltPeak_Type()
)
powMonVoltPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonVoltPeak.setStatus("current")
if mibBuilder.loadTexts:
    powMonVoltPeak.setUnits("Volts (rms)")
_PowMonDeciAmps_Type = Unsigned32
_PowMonDeciAmps_Object = MibTableColumn
powMonDeciAmps = _PowMonDeciAmps_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 10),
    _PowMonDeciAmps_Type()
)
powMonDeciAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonDeciAmps.setStatus("current")
if mibBuilder.loadTexts:
    powMonDeciAmps.setUnits("0.1 Amps (rms)")
_PowMonRealPower_Type = Unsigned32
_PowMonRealPower_Object = MibTableColumn
powMonRealPower = _PowMonRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 11),
    _PowMonRealPower_Type()
)
powMonRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonRealPower.setStatus("current")
if mibBuilder.loadTexts:
    powMonRealPower.setUnits("Watts")
_PowMonApparentPower_Type = Unsigned32
_PowMonApparentPower_Object = MibTableColumn
powMonApparentPower = _PowMonApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 12),
    _PowMonApparentPower_Type()
)
powMonApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    powMonApparentPower.setUnits("Volt-Amps")


class _PowMonPowerFactor_Type(Integer32):
    """Custom type powMonPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PowMonPowerFactor_Type.__name__ = "Integer32"
_PowMonPowerFactor_Object = MibTableColumn
powMonPowerFactor = _PowMonPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 13),
    _PowMonPowerFactor_Type()
)
powMonPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    powMonPowerFactor.setUnits("%")


class _PowMonDeciAmpsOutlet1_Type(Integer32):
    """Custom type powMonDeciAmpsOutlet1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PowMonDeciAmpsOutlet1_Type.__name__ = "Integer32"
_PowMonDeciAmpsOutlet1_Object = MibTableColumn
powMonDeciAmpsOutlet1 = _PowMonDeciAmpsOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 14),
    _PowMonDeciAmpsOutlet1_Type()
)
powMonDeciAmpsOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonDeciAmpsOutlet1.setStatus("current")
if mibBuilder.loadTexts:
    powMonDeciAmpsOutlet1.setUnits("0.1 Amps (rms)")


class _PowMonDeciAmpsOutlet2_Type(Integer32):
    """Custom type powMonDeciAmpsOutlet2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PowMonDeciAmpsOutlet2_Type.__name__ = "Integer32"
_PowMonDeciAmpsOutlet2_Object = MibTableColumn
powMonDeciAmpsOutlet2 = _PowMonDeciAmpsOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 3, 1, 15),
    _PowMonDeciAmpsOutlet2_Type()
)
powMonDeciAmpsOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonDeciAmpsOutlet2.setStatus("current")
if mibBuilder.loadTexts:
    powMonDeciAmpsOutlet2.setUnits("0.1 Amps (rms)")
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 4)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("current")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 4, 1)
)
tempSensorEntry.setIndexNames(
    (0, "GEIST-MIB", "tempSensorIndex"),
)
if mibBuilder.loadTexts:
    tempSensorEntry.setStatus("current")


class _TempSensorIndex_Type(Integer32):
    """Custom type tempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TempSensorIndex_Type.__name__ = "Integer32"
_TempSensorIndex_Object = MibTableColumn
tempSensorIndex = _TempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 4, 1, 1),
    _TempSensorIndex_Type()
)
tempSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempSensorIndex.setStatus("current")
_TempSensorSerial_Type = DisplayString
_TempSensorSerial_Object = MibTableColumn
tempSensorSerial = _TempSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 4, 1, 2),
    _TempSensorSerial_Type()
)
tempSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorSerial.setStatus("current")
_TempSensorName_Type = DisplayString
_TempSensorName_Object = MibTableColumn
tempSensorName = _TempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 4, 1, 3),
    _TempSensorName_Type()
)
tempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorName.setStatus("current")
_TempSensorAvail_Type = Unsigned32
_TempSensorAvail_Object = MibTableColumn
tempSensorAvail = _TempSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 4, 1, 4),
    _TempSensorAvail_Type()
)
tempSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorAvail.setStatus("current")


class _TempSensorTempC_Type(Integer32):
    """Custom type tempSensorTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 123),
    )


_TempSensorTempC_Type.__name__ = "Integer32"
_TempSensorTempC_Object = MibTableColumn
tempSensorTempC = _TempSensorTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 4, 1, 5),
    _TempSensorTempC_Type()
)
tempSensorTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorTempC.setStatus("current")
if mibBuilder.loadTexts:
    tempSensorTempC.setUnits("Degrees Celsius")
_AirFlowSensorTable_Object = MibTable
airFlowSensorTable = _AirFlowSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 5)
)
if mibBuilder.loadTexts:
    airFlowSensorTable.setStatus("current")
_AirFlowSensorEntry_Object = MibTableRow
airFlowSensorEntry = _AirFlowSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 5, 1)
)
airFlowSensorEntry.setIndexNames(
    (0, "GEIST-MIB", "airFlowSensorIndex"),
)
if mibBuilder.loadTexts:
    airFlowSensorEntry.setStatus("current")


class _AirFlowSensorIndex_Type(Integer32):
    """Custom type airFlowSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AirFlowSensorIndex_Type.__name__ = "Integer32"
_AirFlowSensorIndex_Object = MibTableColumn
airFlowSensorIndex = _AirFlowSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 5, 1, 1),
    _AirFlowSensorIndex_Type()
)
airFlowSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    airFlowSensorIndex.setStatus("current")
_AirFlowSensorSerial_Type = DisplayString
_AirFlowSensorSerial_Object = MibTableColumn
airFlowSensorSerial = _AirFlowSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 5, 1, 2),
    _AirFlowSensorSerial_Type()
)
airFlowSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorSerial.setStatus("current")
_AirFlowSensorName_Type = DisplayString
_AirFlowSensorName_Object = MibTableColumn
airFlowSensorName = _AirFlowSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 5, 1, 3),
    _AirFlowSensorName_Type()
)
airFlowSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorName.setStatus("current")
_AirFlowSensorAvail_Type = Unsigned32
_AirFlowSensorAvail_Object = MibTableColumn
airFlowSensorAvail = _AirFlowSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 5, 1, 4),
    _AirFlowSensorAvail_Type()
)
airFlowSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorAvail.setStatus("current")


class _AirFlowSensorFlow_Type(Integer32):
    """Custom type airFlowSensorFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AirFlowSensorFlow_Type.__name__ = "Integer32"
_AirFlowSensorFlow_Object = MibTableColumn
airFlowSensorFlow = _AirFlowSensorFlow_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 5, 1, 5),
    _AirFlowSensorFlow_Type()
)
airFlowSensorFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorFlow.setStatus("current")


class _AirFlowSensorTempC_Type(Integer32):
    """Custom type airFlowSensorTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_AirFlowSensorTempC_Type.__name__ = "Integer32"
_AirFlowSensorTempC_Object = MibTableColumn
airFlowSensorTempC = _AirFlowSensorTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 5, 1, 6),
    _AirFlowSensorTempC_Type()
)
airFlowSensorTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorTempC.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorTempC.setUnits("Degrees Celsius")


class _AirFlowSensorHumidity_Type(Integer32):
    """Custom type airFlowSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AirFlowSensorHumidity_Type.__name__ = "Integer32"
_AirFlowSensorHumidity_Object = MibTableColumn
airFlowSensorHumidity = _AirFlowSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 5, 1, 7),
    _AirFlowSensorHumidity_Type()
)
airFlowSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorHumidity.setUnits("%")


class _AirFlowSensorDewPoint_Type(Integer32):
    """Custom type airFlowSensorDewPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 123),
    )


_AirFlowSensorDewPoint_Type.__name__ = "Integer32"
_AirFlowSensorDewPoint_Object = MibTableColumn
airFlowSensorDewPoint = _AirFlowSensorDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 5, 1, 8),
    _AirFlowSensorDewPoint_Type()
)
airFlowSensorDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorDewPoint.setUnits("Degrees Celsius")
_PowerOnlyTable_Object = MibTable
powerOnlyTable = _PowerOnlyTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 6)
)
if mibBuilder.loadTexts:
    powerOnlyTable.setStatus("current")
_PowerOnlyEntry_Object = MibTableRow
powerOnlyEntry = _PowerOnlyEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 6, 1)
)
powerOnlyEntry.setIndexNames(
    (0, "GEIST-MIB", "powerIndex"),
)
if mibBuilder.loadTexts:
    powerOnlyEntry.setStatus("current")


class _PowerIndex_Type(Integer32):
    """Custom type powerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PowerIndex_Type.__name__ = "Integer32"
_PowerIndex_Object = MibTableColumn
powerIndex = _PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 6, 1, 1),
    _PowerIndex_Type()
)
powerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerIndex.setStatus("current")
_PowerSerial_Type = DisplayString
_PowerSerial_Object = MibTableColumn
powerSerial = _PowerSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 6, 1, 2),
    _PowerSerial_Type()
)
powerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSerial.setStatus("current")
_PowerName_Type = DisplayString
_PowerName_Object = MibTableColumn
powerName = _PowerName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 6, 1, 3),
    _PowerName_Type()
)
powerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerName.setStatus("current")
_PowerAvail_Type = Unsigned32
_PowerAvail_Object = MibTableColumn
powerAvail = _PowerAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 6, 1, 4),
    _PowerAvail_Type()
)
powerAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerAvail.setStatus("current")
_PowerVolts_Type = Unsigned32
_PowerVolts_Object = MibTableColumn
powerVolts = _PowerVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 6, 1, 5),
    _PowerVolts_Type()
)
powerVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerVolts.setStatus("current")
if mibBuilder.loadTexts:
    powerVolts.setUnits("Volts (rms)")
_PowerDeciAmps_Type = Unsigned32
_PowerDeciAmps_Object = MibTableColumn
powerDeciAmps = _PowerDeciAmps_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 6, 1, 6),
    _PowerDeciAmps_Type()
)
powerDeciAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDeciAmps.setStatus("current")
if mibBuilder.loadTexts:
    powerDeciAmps.setUnits("0.1 Amps (rms)")
_PowerRealPower_Type = Unsigned32
_PowerRealPower_Object = MibTableColumn
powerRealPower = _PowerRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 6, 1, 7),
    _PowerRealPower_Type()
)
powerRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerRealPower.setStatus("current")
if mibBuilder.loadTexts:
    powerRealPower.setUnits("Watts")
_PowerApparentPower_Type = Unsigned32
_PowerApparentPower_Object = MibTableColumn
powerApparentPower = _PowerApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 6, 1, 8),
    _PowerApparentPower_Type()
)
powerApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    powerApparentPower.setUnits("Volt-Amps")


class _PowerPowerFactor_Type(Integer32):
    """Custom type powerPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PowerPowerFactor_Type.__name__ = "Integer32"
_PowerPowerFactor_Object = MibTableColumn
powerPowerFactor = _PowerPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 6, 1, 9),
    _PowerPowerFactor_Type()
)
powerPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    powerPowerFactor.setUnits("%")
_DoorSensorTable_Object = MibTable
doorSensorTable = _DoorSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 7)
)
if mibBuilder.loadTexts:
    doorSensorTable.setStatus("current")
_DoorSensorEntry_Object = MibTableRow
doorSensorEntry = _DoorSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 7, 1)
)
doorSensorEntry.setIndexNames(
    (0, "GEIST-MIB", "doorSensorIndex"),
)
if mibBuilder.loadTexts:
    doorSensorEntry.setStatus("current")


class _DoorSensorIndex_Type(Integer32):
    """Custom type doorSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DoorSensorIndex_Type.__name__ = "Integer32"
_DoorSensorIndex_Object = MibTableColumn
doorSensorIndex = _DoorSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 7, 1, 1),
    _DoorSensorIndex_Type()
)
doorSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    doorSensorIndex.setStatus("current")
_DoorSensorSerial_Type = DisplayString
_DoorSensorSerial_Object = MibTableColumn
doorSensorSerial = _DoorSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 7, 1, 2),
    _DoorSensorSerial_Type()
)
doorSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSensorSerial.setStatus("current")
_DoorSensorName_Type = DisplayString
_DoorSensorName_Object = MibTableColumn
doorSensorName = _DoorSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 7, 1, 3),
    _DoorSensorName_Type()
)
doorSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSensorName.setStatus("current")
_DoorSensorAvail_Type = Unsigned32
_DoorSensorAvail_Object = MibTableColumn
doorSensorAvail = _DoorSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 7, 1, 4),
    _DoorSensorAvail_Type()
)
doorSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSensorAvail.setStatus("current")


class _DoorSensorStatus_Type(Integer32):
    """Custom type doorSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DoorSensorStatus_Type.__name__ = "Integer32"
_DoorSensorStatus_Object = MibTableColumn
doorSensorStatus = _DoorSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 7, 1, 5),
    _DoorSensorStatus_Type()
)
doorSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSensorStatus.setStatus("current")
_WaterSensorTable_Object = MibTable
waterSensorTable = _WaterSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 8)
)
if mibBuilder.loadTexts:
    waterSensorTable.setStatus("current")
_WaterSensorEntry_Object = MibTableRow
waterSensorEntry = _WaterSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 8, 1)
)
waterSensorEntry.setIndexNames(
    (0, "GEIST-MIB", "waterSensorIndex"),
)
if mibBuilder.loadTexts:
    waterSensorEntry.setStatus("current")


class _WaterSensorIndex_Type(Integer32):
    """Custom type waterSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WaterSensorIndex_Type.__name__ = "Integer32"
_WaterSensorIndex_Object = MibTableColumn
waterSensorIndex = _WaterSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 8, 1, 1),
    _WaterSensorIndex_Type()
)
waterSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    waterSensorIndex.setStatus("current")
_WaterSensorSerial_Type = DisplayString
_WaterSensorSerial_Object = MibTableColumn
waterSensorSerial = _WaterSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 8, 1, 2),
    _WaterSensorSerial_Type()
)
waterSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterSensorSerial.setStatus("current")
_WaterSensorName_Type = DisplayString
_WaterSensorName_Object = MibTableColumn
waterSensorName = _WaterSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 8, 1, 3),
    _WaterSensorName_Type()
)
waterSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterSensorName.setStatus("current")
_WaterSensorAvail_Type = Unsigned32
_WaterSensorAvail_Object = MibTableColumn
waterSensorAvail = _WaterSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 8, 1, 4),
    _WaterSensorAvail_Type()
)
waterSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterSensorAvail.setStatus("current")


class _WaterSensorDampness_Type(Integer32):
    """Custom type waterSensorDampness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WaterSensorDampness_Type.__name__ = "Integer32"
_WaterSensorDampness_Object = MibTableColumn
waterSensorDampness = _WaterSensorDampness_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 8, 1, 5),
    _WaterSensorDampness_Type()
)
waterSensorDampness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterSensorDampness.setStatus("current")
_CurrentMonitorTable_Object = MibTable
currentMonitorTable = _CurrentMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 9)
)
if mibBuilder.loadTexts:
    currentMonitorTable.setStatus("current")
_CurrentMonitorEntry_Object = MibTableRow
currentMonitorEntry = _CurrentMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 9, 1)
)
currentMonitorEntry.setIndexNames(
    (0, "GEIST-MIB", "currentMonitorIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorEntry.setStatus("current")


class _CurrentMonitorIndex_Type(Integer32):
    """Custom type currentMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CurrentMonitorIndex_Type.__name__ = "Integer32"
_CurrentMonitorIndex_Object = MibTableColumn
currentMonitorIndex = _CurrentMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 9, 1, 1),
    _CurrentMonitorIndex_Type()
)
currentMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorIndex.setStatus("current")
_CurrentMonitorSerial_Type = DisplayString
_CurrentMonitorSerial_Object = MibTableColumn
currentMonitorSerial = _CurrentMonitorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 9, 1, 2),
    _CurrentMonitorSerial_Type()
)
currentMonitorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorSerial.setStatus("current")
_CurrentMonitorName_Type = DisplayString
_CurrentMonitorName_Object = MibTableColumn
currentMonitorName = _CurrentMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 9, 1, 3),
    _CurrentMonitorName_Type()
)
currentMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorName.setStatus("current")
_CurrentMonitorAvail_Type = Unsigned32
_CurrentMonitorAvail_Object = MibTableColumn
currentMonitorAvail = _CurrentMonitorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 9, 1, 4),
    _CurrentMonitorAvail_Type()
)
currentMonitorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorAvail.setStatus("current")


class _CurrentMonitorDeciAmps_Type(Integer32):
    """Custom type currentMonitorDeciAmps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CurrentMonitorDeciAmps_Type.__name__ = "Integer32"
_CurrentMonitorDeciAmps_Object = MibTableColumn
currentMonitorDeciAmps = _CurrentMonitorDeciAmps_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 9, 1, 5),
    _CurrentMonitorDeciAmps_Type()
)
currentMonitorDeciAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorDeciAmps.setStatus("current")
if mibBuilder.loadTexts:
    currentMonitorDeciAmps.setUnits("0.1 Amps")
_MillivoltMonitorTable_Object = MibTable
millivoltMonitorTable = _MillivoltMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 10)
)
if mibBuilder.loadTexts:
    millivoltMonitorTable.setStatus("current")
_MillivoltMonitorEntry_Object = MibTableRow
millivoltMonitorEntry = _MillivoltMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 10, 1)
)
millivoltMonitorEntry.setIndexNames(
    (0, "GEIST-MIB", "millivoltMonitorIndex"),
)
if mibBuilder.loadTexts:
    millivoltMonitorEntry.setStatus("current")


class _MillivoltMonitorIndex_Type(Integer32):
    """Custom type millivoltMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MillivoltMonitorIndex_Type.__name__ = "Integer32"
_MillivoltMonitorIndex_Object = MibTableColumn
millivoltMonitorIndex = _MillivoltMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 10, 1, 1),
    _MillivoltMonitorIndex_Type()
)
millivoltMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    millivoltMonitorIndex.setStatus("current")
_MillivoltMonitorSerial_Type = DisplayString
_MillivoltMonitorSerial_Object = MibTableColumn
millivoltMonitorSerial = _MillivoltMonitorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 10, 1, 2),
    _MillivoltMonitorSerial_Type()
)
millivoltMonitorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    millivoltMonitorSerial.setStatus("current")
_MillivoltMonitorName_Type = DisplayString
_MillivoltMonitorName_Object = MibTableColumn
millivoltMonitorName = _MillivoltMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 10, 1, 3),
    _MillivoltMonitorName_Type()
)
millivoltMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    millivoltMonitorName.setStatus("current")
_MillivoltMonitorAvail_Type = Unsigned32
_MillivoltMonitorAvail_Object = MibTableColumn
millivoltMonitorAvail = _MillivoltMonitorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 10, 1, 4),
    _MillivoltMonitorAvail_Type()
)
millivoltMonitorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    millivoltMonitorAvail.setStatus("current")


class _MillivoltMonitorMV_Type(Integer32):
    """Custom type millivoltMonitorMV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MillivoltMonitorMV_Type.__name__ = "Integer32"
_MillivoltMonitorMV_Object = MibTableColumn
millivoltMonitorMV = _MillivoltMonitorMV_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 10, 1, 5),
    _MillivoltMonitorMV_Type()
)
millivoltMonitorMV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    millivoltMonitorMV.setStatus("current")
if mibBuilder.loadTexts:
    millivoltMonitorMV.setUnits("millivolts")
_Power3ChTable_Object = MibTable
power3ChTable = _Power3ChTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11)
)
if mibBuilder.loadTexts:
    power3ChTable.setStatus("current")
_Power3ChEntry_Object = MibTableRow
power3ChEntry = _Power3ChEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1)
)
power3ChEntry.setIndexNames(
    (0, "GEIST-MIB", "pow3ChIndex"),
)
if mibBuilder.loadTexts:
    power3ChEntry.setStatus("current")


class _Pow3ChIndex_Type(Integer32):
    """Custom type pow3ChIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Pow3ChIndex_Type.__name__ = "Integer32"
_Pow3ChIndex_Object = MibTableColumn
pow3ChIndex = _Pow3ChIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 1),
    _Pow3ChIndex_Type()
)
pow3ChIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pow3ChIndex.setStatus("current")
_Pow3ChSerial_Type = DisplayString
_Pow3ChSerial_Object = MibTableColumn
pow3ChSerial = _Pow3ChSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 2),
    _Pow3ChSerial_Type()
)
pow3ChSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChSerial.setStatus("current")
_Pow3ChName_Type = DisplayString
_Pow3ChName_Object = MibTableColumn
pow3ChName = _Pow3ChName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 3),
    _Pow3ChName_Type()
)
pow3ChName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChName.setStatus("current")
_Pow3ChAvail_Type = Unsigned32
_Pow3ChAvail_Object = MibTableColumn
pow3ChAvail = _Pow3ChAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 4),
    _Pow3ChAvail_Type()
)
pow3ChAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChAvail.setStatus("current")
_Pow3ChKWattHrsA_Type = Unsigned32
_Pow3ChKWattHrsA_Object = MibTableColumn
pow3ChKWattHrsA = _Pow3ChKWattHrsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 5),
    _Pow3ChKWattHrsA_Type()
)
pow3ChKWattHrsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChKWattHrsA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChKWattHrsA.setUnits("KWh")
_Pow3ChVoltsA_Type = Unsigned32
_Pow3ChVoltsA_Object = MibTableColumn
pow3ChVoltsA = _Pow3ChVoltsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 6),
    _Pow3ChVoltsA_Type()
)
pow3ChVoltsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltsA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltsA.setUnits("Volts (rms)")
_Pow3ChVoltMaxA_Type = Unsigned32
_Pow3ChVoltMaxA_Object = MibTableColumn
pow3ChVoltMaxA = _Pow3ChVoltMaxA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 7),
    _Pow3ChVoltMaxA_Type()
)
pow3ChVoltMaxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltMaxA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltMaxA.setUnits("Volts (rms)")
_Pow3ChVoltMinA_Type = Unsigned32
_Pow3ChVoltMinA_Object = MibTableColumn
pow3ChVoltMinA = _Pow3ChVoltMinA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 8),
    _Pow3ChVoltMinA_Type()
)
pow3ChVoltMinA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltMinA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltMinA.setUnits("Volts (rms)")
_Pow3ChVoltPeakA_Type = Unsigned32
_Pow3ChVoltPeakA_Object = MibTableColumn
pow3ChVoltPeakA = _Pow3ChVoltPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 9),
    _Pow3ChVoltPeakA_Type()
)
pow3ChVoltPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltPeakA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltPeakA.setUnits("Volts")
_Pow3ChDeciAmpsA_Type = Unsigned32
_Pow3ChDeciAmpsA_Object = MibTableColumn
pow3ChDeciAmpsA = _Pow3ChDeciAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 10),
    _Pow3ChDeciAmpsA_Type()
)
pow3ChDeciAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChDeciAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChDeciAmpsA.setUnits("0.1 Amps (rms)")
_Pow3ChRealPowerA_Type = Unsigned32
_Pow3ChRealPowerA_Object = MibTableColumn
pow3ChRealPowerA = _Pow3ChRealPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 11),
    _Pow3ChRealPowerA_Type()
)
pow3ChRealPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChRealPowerA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChRealPowerA.setUnits("Watts")
_Pow3ChApparentPowerA_Type = Unsigned32
_Pow3ChApparentPowerA_Object = MibTableColumn
pow3ChApparentPowerA = _Pow3ChApparentPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 12),
    _Pow3ChApparentPowerA_Type()
)
pow3ChApparentPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChApparentPowerA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChApparentPowerA.setUnits("Volt-Amps")


class _Pow3ChPowerFactorA_Type(Integer32):
    """Custom type pow3ChPowerFactorA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pow3ChPowerFactorA_Type.__name__ = "Integer32"
_Pow3ChPowerFactorA_Object = MibTableColumn
pow3ChPowerFactorA = _Pow3ChPowerFactorA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 13),
    _Pow3ChPowerFactorA_Type()
)
pow3ChPowerFactorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChPowerFactorA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChPowerFactorA.setUnits("%")
_Pow3ChKWattHrsB_Type = Unsigned32
_Pow3ChKWattHrsB_Object = MibTableColumn
pow3ChKWattHrsB = _Pow3ChKWattHrsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 14),
    _Pow3ChKWattHrsB_Type()
)
pow3ChKWattHrsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChKWattHrsB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChKWattHrsB.setUnits("KWh")
_Pow3ChVoltsB_Type = Unsigned32
_Pow3ChVoltsB_Object = MibTableColumn
pow3ChVoltsB = _Pow3ChVoltsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 15),
    _Pow3ChVoltsB_Type()
)
pow3ChVoltsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltsB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltsB.setUnits("Volts (rms)")
_Pow3ChVoltMaxB_Type = Unsigned32
_Pow3ChVoltMaxB_Object = MibTableColumn
pow3ChVoltMaxB = _Pow3ChVoltMaxB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 16),
    _Pow3ChVoltMaxB_Type()
)
pow3ChVoltMaxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltMaxB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltMaxB.setUnits("Volts (rms)")
_Pow3ChVoltMinB_Type = Unsigned32
_Pow3ChVoltMinB_Object = MibTableColumn
pow3ChVoltMinB = _Pow3ChVoltMinB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 17),
    _Pow3ChVoltMinB_Type()
)
pow3ChVoltMinB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltMinB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltMinB.setUnits("Volts (rms)")
_Pow3ChVoltPeakB_Type = Unsigned32
_Pow3ChVoltPeakB_Object = MibTableColumn
pow3ChVoltPeakB = _Pow3ChVoltPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 18),
    _Pow3ChVoltPeakB_Type()
)
pow3ChVoltPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltPeakB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltPeakB.setUnits("Volts")
_Pow3ChDeciAmpsB_Type = Unsigned32
_Pow3ChDeciAmpsB_Object = MibTableColumn
pow3ChDeciAmpsB = _Pow3ChDeciAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 19),
    _Pow3ChDeciAmpsB_Type()
)
pow3ChDeciAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChDeciAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChDeciAmpsB.setUnits("0.1 Amps (rms)")
_Pow3ChRealPowerB_Type = Unsigned32
_Pow3ChRealPowerB_Object = MibTableColumn
pow3ChRealPowerB = _Pow3ChRealPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 20),
    _Pow3ChRealPowerB_Type()
)
pow3ChRealPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChRealPowerB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChRealPowerB.setUnits("Watts")
_Pow3ChApparentPowerB_Type = Unsigned32
_Pow3ChApparentPowerB_Object = MibTableColumn
pow3ChApparentPowerB = _Pow3ChApparentPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 21),
    _Pow3ChApparentPowerB_Type()
)
pow3ChApparentPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChApparentPowerB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChApparentPowerB.setUnits("Volt-Amps")


class _Pow3ChPowerFactorB_Type(Integer32):
    """Custom type pow3ChPowerFactorB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pow3ChPowerFactorB_Type.__name__ = "Integer32"
_Pow3ChPowerFactorB_Object = MibTableColumn
pow3ChPowerFactorB = _Pow3ChPowerFactorB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 22),
    _Pow3ChPowerFactorB_Type()
)
pow3ChPowerFactorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChPowerFactorB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChPowerFactorB.setUnits("%")
_Pow3ChKWattHrsC_Type = Unsigned32
_Pow3ChKWattHrsC_Object = MibTableColumn
pow3ChKWattHrsC = _Pow3ChKWattHrsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 23),
    _Pow3ChKWattHrsC_Type()
)
pow3ChKWattHrsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChKWattHrsC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChKWattHrsC.setUnits("KWh")
_Pow3ChVoltsC_Type = Unsigned32
_Pow3ChVoltsC_Object = MibTableColumn
pow3ChVoltsC = _Pow3ChVoltsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 24),
    _Pow3ChVoltsC_Type()
)
pow3ChVoltsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltsC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltsC.setUnits("Volts (rms)")
_Pow3ChVoltMaxC_Type = Unsigned32
_Pow3ChVoltMaxC_Object = MibTableColumn
pow3ChVoltMaxC = _Pow3ChVoltMaxC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 25),
    _Pow3ChVoltMaxC_Type()
)
pow3ChVoltMaxC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltMaxC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltMaxC.setUnits("Volts (rms)")
_Pow3ChVoltMinC_Type = Unsigned32
_Pow3ChVoltMinC_Object = MibTableColumn
pow3ChVoltMinC = _Pow3ChVoltMinC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 26),
    _Pow3ChVoltMinC_Type()
)
pow3ChVoltMinC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltMinC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltMinC.setUnits("Volts (rms)")
_Pow3ChVoltPeakC_Type = Unsigned32
_Pow3ChVoltPeakC_Object = MibTableColumn
pow3ChVoltPeakC = _Pow3ChVoltPeakC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 27),
    _Pow3ChVoltPeakC_Type()
)
pow3ChVoltPeakC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltPeakC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltPeakC.setUnits("Volts")
_Pow3ChDeciAmpsC_Type = Unsigned32
_Pow3ChDeciAmpsC_Object = MibTableColumn
pow3ChDeciAmpsC = _Pow3ChDeciAmpsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 28),
    _Pow3ChDeciAmpsC_Type()
)
pow3ChDeciAmpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChDeciAmpsC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChDeciAmpsC.setUnits("0.1 Amps (rms)")
_Pow3ChRealPowerC_Type = Unsigned32
_Pow3ChRealPowerC_Object = MibTableColumn
pow3ChRealPowerC = _Pow3ChRealPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 29),
    _Pow3ChRealPowerC_Type()
)
pow3ChRealPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChRealPowerC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChRealPowerC.setUnits("Watts")
_Pow3ChApparentPowerC_Type = Unsigned32
_Pow3ChApparentPowerC_Object = MibTableColumn
pow3ChApparentPowerC = _Pow3ChApparentPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 30),
    _Pow3ChApparentPowerC_Type()
)
pow3ChApparentPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChApparentPowerC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChApparentPowerC.setUnits("Volt-Amps")


class _Pow3ChPowerFactorC_Type(Integer32):
    """Custom type pow3ChPowerFactorC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pow3ChPowerFactorC_Type.__name__ = "Integer32"
_Pow3ChPowerFactorC_Object = MibTableColumn
pow3ChPowerFactorC = _Pow3ChPowerFactorC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 11, 1, 31),
    _Pow3ChPowerFactorC_Type()
)
pow3ChPowerFactorC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChPowerFactorC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChPowerFactorC.setUnits("%")
_OutletTable_Object = MibTable
outletTable = _OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 12)
)
if mibBuilder.loadTexts:
    outletTable.setStatus("current")
_OutletEntry_Object = MibTableRow
outletEntry = _OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 12, 1)
)
outletEntry.setIndexNames(
    (0, "GEIST-MIB", "outletIndex"),
)
if mibBuilder.loadTexts:
    outletEntry.setStatus("current")


class _OutletIndex_Type(Integer32):
    """Custom type outletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OutletIndex_Type.__name__ = "Integer32"
_OutletIndex_Object = MibTableColumn
outletIndex = _OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 12, 1, 1),
    _OutletIndex_Type()
)
outletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outletIndex.setStatus("current")
_OutletSerial_Type = DisplayString
_OutletSerial_Object = MibTableColumn
outletSerial = _OutletSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 12, 1, 2),
    _OutletSerial_Type()
)
outletSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSerial.setStatus("current")
_OutletName_Type = DisplayString
_OutletName_Object = MibTableColumn
outletName = _OutletName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 12, 1, 3),
    _OutletName_Type()
)
outletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletName.setStatus("current")
_OutletAvail_Type = Unsigned32
_OutletAvail_Object = MibTableColumn
outletAvail = _OutletAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 12, 1, 4),
    _OutletAvail_Type()
)
outletAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletAvail.setStatus("current")


class _Outlet1Status_Type(Integer32):
    """Custom type outlet1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Outlet1Status_Type.__name__ = "Integer32"
_Outlet1Status_Object = MibTableColumn
outlet1Status = _Outlet1Status_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 12, 1, 5),
    _Outlet1Status_Type()
)
outlet1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet1Status.setStatus("current")


class _Outlet2Status_Type(Integer32):
    """Custom type outlet2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Outlet2Status_Type.__name__ = "Integer32"
_Outlet2Status_Object = MibTableColumn
outlet2Status = _Outlet2Status_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 12, 1, 6),
    _Outlet2Status_Type()
)
outlet2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet2Status.setStatus("current")
_VsfcTable_Object = MibTable
vsfcTable = _VsfcTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13)
)
if mibBuilder.loadTexts:
    vsfcTable.setStatus("current")
_VsfcEntry_Object = MibTableRow
vsfcEntry = _VsfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13, 1)
)
vsfcEntry.setIndexNames(
    (0, "GEIST-MIB", "vsfcIndex"),
)
if mibBuilder.loadTexts:
    vsfcEntry.setStatus("current")


class _VsfcIndex_Type(Integer32):
    """Custom type vsfcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_VsfcIndex_Type.__name__ = "Integer32"
_VsfcIndex_Object = MibTableColumn
vsfcIndex = _VsfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13, 1, 1),
    _VsfcIndex_Type()
)
vsfcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsfcIndex.setStatus("current")
_VsfcSerial_Type = DisplayString
_VsfcSerial_Object = MibTableColumn
vsfcSerial = _VsfcSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13, 1, 2),
    _VsfcSerial_Type()
)
vsfcSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcSerial.setStatus("current")
_VsfcName_Type = DisplayString
_VsfcName_Object = MibTableColumn
vsfcName = _VsfcName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13, 1, 3),
    _VsfcName_Type()
)
vsfcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcName.setStatus("current")
_VsfcAvail_Type = Unsigned32
_VsfcAvail_Object = MibTableColumn
vsfcAvail = _VsfcAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13, 1, 4),
    _VsfcAvail_Type()
)
vsfcAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcAvail.setStatus("current")


class _VsfcSetPointC_Type(Integer32):
    """Custom type vsfcSetPointC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 38),
    )


_VsfcSetPointC_Type.__name__ = "Integer32"
_VsfcSetPointC_Object = MibTableColumn
vsfcSetPointC = _VsfcSetPointC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13, 1, 5),
    _VsfcSetPointC_Type()
)
vsfcSetPointC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcSetPointC.setStatus("current")
if mibBuilder.loadTexts:
    vsfcSetPointC.setUnits("Degrees Celsius")


class _VsfcIntTempC_Type(Integer32):
    """Custom type vsfcIntTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 50),
    )


_VsfcIntTempC_Type.__name__ = "Integer32"
_VsfcIntTempC_Object = MibTableColumn
vsfcIntTempC = _VsfcIntTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13, 1, 6),
    _VsfcIntTempC_Type()
)
vsfcIntTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcIntTempC.setStatus("current")
if mibBuilder.loadTexts:
    vsfcIntTempC.setUnits("Degrees Celsius")


class _VsfcExt1TempC_Type(Integer32):
    """Custom type vsfcExt1TempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 50),
    )


_VsfcExt1TempC_Type.__name__ = "Integer32"
_VsfcExt1TempC_Object = MibTableColumn
vsfcExt1TempC = _VsfcExt1TempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13, 1, 7),
    _VsfcExt1TempC_Type()
)
vsfcExt1TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcExt1TempC.setStatus("current")
if mibBuilder.loadTexts:
    vsfcExt1TempC.setUnits("Degrees Celsius")


class _VsfcExt2TempC_Type(Integer32):
    """Custom type vsfcExt2TempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 50),
    )


_VsfcExt2TempC_Type.__name__ = "Integer32"
_VsfcExt2TempC_Object = MibTableColumn
vsfcExt2TempC = _VsfcExt2TempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13, 1, 8),
    _VsfcExt2TempC_Type()
)
vsfcExt2TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcExt2TempC.setStatus("current")
if mibBuilder.loadTexts:
    vsfcExt2TempC.setUnits("Degrees Celsius")


class _VsfcExt3TempC_Type(Integer32):
    """Custom type vsfcExt3TempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 50),
    )


_VsfcExt3TempC_Type.__name__ = "Integer32"
_VsfcExt3TempC_Object = MibTableColumn
vsfcExt3TempC = _VsfcExt3TempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13, 1, 9),
    _VsfcExt3TempC_Type()
)
vsfcExt3TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcExt3TempC.setStatus("current")
if mibBuilder.loadTexts:
    vsfcExt3TempC.setUnits("Degrees Celsius")


class _VsfcExt4TempC_Type(Integer32):
    """Custom type vsfcExt4TempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 50),
    )


_VsfcExt4TempC_Type.__name__ = "Integer32"
_VsfcExt4TempC_Object = MibTableColumn
vsfcExt4TempC = _VsfcExt4TempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13, 1, 10),
    _VsfcExt4TempC_Type()
)
vsfcExt4TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcExt4TempC.setStatus("current")
if mibBuilder.loadTexts:
    vsfcExt4TempC.setUnits("Degrees Celsius")


class _VsfcFanSpeed_Type(Integer32):
    """Custom type vsfcFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VsfcFanSpeed_Type.__name__ = "Integer32"
_VsfcFanSpeed_Object = MibTableColumn
vsfcFanSpeed = _VsfcFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 13, 1, 11),
    _VsfcFanSpeed_Type()
)
vsfcFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    vsfcFanSpeed.setUnits("%")
_Ctrl3ChTable_Object = MibTable
ctrl3ChTable = _Ctrl3ChTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14)
)
if mibBuilder.loadTexts:
    ctrl3ChTable.setStatus("current")
_Ctrl3ChEntry_Object = MibTableRow
ctrl3ChEntry = _Ctrl3ChEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1)
)
ctrl3ChEntry.setIndexNames(
    (0, "GEIST-MIB", "ctrl3ChIndex"),
)
if mibBuilder.loadTexts:
    ctrl3ChEntry.setStatus("current")


class _Ctrl3ChIndex_Type(Integer32):
    """Custom type ctrl3ChIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Ctrl3ChIndex_Type.__name__ = "Integer32"
_Ctrl3ChIndex_Object = MibTableColumn
ctrl3ChIndex = _Ctrl3ChIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 1),
    _Ctrl3ChIndex_Type()
)
ctrl3ChIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrl3ChIndex.setStatus("current")
_Ctrl3ChSerial_Type = DisplayString
_Ctrl3ChSerial_Object = MibTableColumn
ctrl3ChSerial = _Ctrl3ChSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 2),
    _Ctrl3ChSerial_Type()
)
ctrl3ChSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChSerial.setStatus("current")
_Ctrl3ChName_Type = DisplayString
_Ctrl3ChName_Object = MibTableColumn
ctrl3ChName = _Ctrl3ChName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 3),
    _Ctrl3ChName_Type()
)
ctrl3ChName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChName.setStatus("current")
_Ctrl3ChAvail_Type = Unsigned32
_Ctrl3ChAvail_Object = MibTableColumn
ctrl3ChAvail = _Ctrl3ChAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 4),
    _Ctrl3ChAvail_Type()
)
ctrl3ChAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChAvail.setStatus("current")
_Ctrl3ChVoltsA_Type = Unsigned32
_Ctrl3ChVoltsA_Object = MibTableColumn
ctrl3ChVoltsA = _Ctrl3ChVoltsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 5),
    _Ctrl3ChVoltsA_Type()
)
ctrl3ChVoltsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChVoltsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChVoltsA.setUnits("Volts (rms)")
_Ctrl3ChVoltPeakA_Type = Unsigned32
_Ctrl3ChVoltPeakA_Object = MibTableColumn
ctrl3ChVoltPeakA = _Ctrl3ChVoltPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 6),
    _Ctrl3ChVoltPeakA_Type()
)
ctrl3ChVoltPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChVoltPeakA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChVoltPeakA.setUnits("Volts (rms)")
_Ctrl3ChDeciAmpsA_Type = Unsigned32
_Ctrl3ChDeciAmpsA_Object = MibTableColumn
ctrl3ChDeciAmpsA = _Ctrl3ChDeciAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 7),
    _Ctrl3ChDeciAmpsA_Type()
)
ctrl3ChDeciAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsA.setUnits("0.1 Amps (rms)")
_Ctrl3ChDeciAmpsPeakA_Type = Unsigned32
_Ctrl3ChDeciAmpsPeakA_Object = MibTableColumn
ctrl3ChDeciAmpsPeakA = _Ctrl3ChDeciAmpsPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 8),
    _Ctrl3ChDeciAmpsPeakA_Type()
)
ctrl3ChDeciAmpsPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsPeakA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsPeakA.setUnits("0.1 Amps (rms)")
_Ctrl3ChRealPowerA_Type = Unsigned32
_Ctrl3ChRealPowerA_Object = MibTableColumn
ctrl3ChRealPowerA = _Ctrl3ChRealPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 9),
    _Ctrl3ChRealPowerA_Type()
)
ctrl3ChRealPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChRealPowerA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChRealPowerA.setUnits("Watts")
_Ctrl3ChApparentPowerA_Type = Unsigned32
_Ctrl3ChApparentPowerA_Object = MibTableColumn
ctrl3ChApparentPowerA = _Ctrl3ChApparentPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 10),
    _Ctrl3ChApparentPowerA_Type()
)
ctrl3ChApparentPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChApparentPowerA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChApparentPowerA.setUnits("Volt-Amps")


class _Ctrl3ChPowerFactorA_Type(Integer32):
    """Custom type ctrl3ChPowerFactorA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ctrl3ChPowerFactorA_Type.__name__ = "Integer32"
_Ctrl3ChPowerFactorA_Object = MibTableColumn
ctrl3ChPowerFactorA = _Ctrl3ChPowerFactorA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 11),
    _Ctrl3ChPowerFactorA_Type()
)
ctrl3ChPowerFactorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChPowerFactorA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChPowerFactorA.setUnits("%")
_Ctrl3ChVoltsB_Type = Unsigned32
_Ctrl3ChVoltsB_Object = MibTableColumn
ctrl3ChVoltsB = _Ctrl3ChVoltsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 12),
    _Ctrl3ChVoltsB_Type()
)
ctrl3ChVoltsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChVoltsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChVoltsB.setUnits("Volts (rms)")
_Ctrl3ChVoltPeakB_Type = Unsigned32
_Ctrl3ChVoltPeakB_Object = MibTableColumn
ctrl3ChVoltPeakB = _Ctrl3ChVoltPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 13),
    _Ctrl3ChVoltPeakB_Type()
)
ctrl3ChVoltPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChVoltPeakB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChVoltPeakB.setUnits("Volts (rms)")
_Ctrl3ChDeciAmpsB_Type = Unsigned32
_Ctrl3ChDeciAmpsB_Object = MibTableColumn
ctrl3ChDeciAmpsB = _Ctrl3ChDeciAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 14),
    _Ctrl3ChDeciAmpsB_Type()
)
ctrl3ChDeciAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsB.setUnits("0.1 Amps (rms)")
_Ctrl3ChDeciAmpsPeakB_Type = Unsigned32
_Ctrl3ChDeciAmpsPeakB_Object = MibTableColumn
ctrl3ChDeciAmpsPeakB = _Ctrl3ChDeciAmpsPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 15),
    _Ctrl3ChDeciAmpsPeakB_Type()
)
ctrl3ChDeciAmpsPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsPeakB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsPeakB.setUnits("0.1 Amps (rms)")
_Ctrl3ChRealPowerB_Type = Unsigned32
_Ctrl3ChRealPowerB_Object = MibTableColumn
ctrl3ChRealPowerB = _Ctrl3ChRealPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 16),
    _Ctrl3ChRealPowerB_Type()
)
ctrl3ChRealPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChRealPowerB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChRealPowerB.setUnits("Watts")
_Ctrl3ChApparentPowerB_Type = Unsigned32
_Ctrl3ChApparentPowerB_Object = MibTableColumn
ctrl3ChApparentPowerB = _Ctrl3ChApparentPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 17),
    _Ctrl3ChApparentPowerB_Type()
)
ctrl3ChApparentPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChApparentPowerB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChApparentPowerB.setUnits("Volt-Amps")


class _Ctrl3ChPowerFactorB_Type(Integer32):
    """Custom type ctrl3ChPowerFactorB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ctrl3ChPowerFactorB_Type.__name__ = "Integer32"
_Ctrl3ChPowerFactorB_Object = MibTableColumn
ctrl3ChPowerFactorB = _Ctrl3ChPowerFactorB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 18),
    _Ctrl3ChPowerFactorB_Type()
)
ctrl3ChPowerFactorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChPowerFactorB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChPowerFactorB.setUnits("%")
_Ctrl3ChVoltsC_Type = Unsigned32
_Ctrl3ChVoltsC_Object = MibTableColumn
ctrl3ChVoltsC = _Ctrl3ChVoltsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 19),
    _Ctrl3ChVoltsC_Type()
)
ctrl3ChVoltsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChVoltsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChVoltsC.setUnits("Volts (rms)")
_Ctrl3ChVoltPeakC_Type = Unsigned32
_Ctrl3ChVoltPeakC_Object = MibTableColumn
ctrl3ChVoltPeakC = _Ctrl3ChVoltPeakC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 20),
    _Ctrl3ChVoltPeakC_Type()
)
ctrl3ChVoltPeakC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChVoltPeakC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChVoltPeakC.setUnits("Volts (rms)")
_Ctrl3ChDeciAmpsC_Type = Unsigned32
_Ctrl3ChDeciAmpsC_Object = MibTableColumn
ctrl3ChDeciAmpsC = _Ctrl3ChDeciAmpsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 21),
    _Ctrl3ChDeciAmpsC_Type()
)
ctrl3ChDeciAmpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsC.setUnits("0.1 Amps (rms)")
_Ctrl3ChDeciAmpsPeakC_Type = Unsigned32
_Ctrl3ChDeciAmpsPeakC_Object = MibTableColumn
ctrl3ChDeciAmpsPeakC = _Ctrl3ChDeciAmpsPeakC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 22),
    _Ctrl3ChDeciAmpsPeakC_Type()
)
ctrl3ChDeciAmpsPeakC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsPeakC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsPeakC.setUnits("0.1 Amps (rms)")
_Ctrl3ChRealPowerC_Type = Unsigned32
_Ctrl3ChRealPowerC_Object = MibTableColumn
ctrl3ChRealPowerC = _Ctrl3ChRealPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 23),
    _Ctrl3ChRealPowerC_Type()
)
ctrl3ChRealPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChRealPowerC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChRealPowerC.setUnits("Watts")
_Ctrl3ChApparentPowerC_Type = Unsigned32
_Ctrl3ChApparentPowerC_Object = MibTableColumn
ctrl3ChApparentPowerC = _Ctrl3ChApparentPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 24),
    _Ctrl3ChApparentPowerC_Type()
)
ctrl3ChApparentPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChApparentPowerC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChApparentPowerC.setUnits("Volt-Amps")


class _Ctrl3ChPowerFactorC_Type(Integer32):
    """Custom type ctrl3ChPowerFactorC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ctrl3ChPowerFactorC_Type.__name__ = "Integer32"
_Ctrl3ChPowerFactorC_Object = MibTableColumn
ctrl3ChPowerFactorC = _Ctrl3ChPowerFactorC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 14, 1, 25),
    _Ctrl3ChPowerFactorC_Type()
)
ctrl3ChPowerFactorC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChPowerFactorC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChPowerFactorC.setUnits("%")
_CtrlGrpAmpsTable_Object = MibTable
ctrlGrpAmpsTable = _CtrlGrpAmpsTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 15)
)
if mibBuilder.loadTexts:
    ctrlGrpAmpsTable.setStatus("current")
_CtrlGrpAmpsEntry_Object = MibTableRow
ctrlGrpAmpsEntry = _CtrlGrpAmpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 15, 1)
)
ctrlGrpAmpsEntry.setIndexNames(
    (0, "GEIST-MIB", "ctrlGrpAmpsIndex"),
)
if mibBuilder.loadTexts:
    ctrlGrpAmpsEntry.setStatus("current")


class _CtrlGrpAmpsIndex_Type(Integer32):
    """Custom type ctrlGrpAmpsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CtrlGrpAmpsIndex_Type.__name__ = "Integer32"
_CtrlGrpAmpsIndex_Object = MibTableColumn
ctrlGrpAmpsIndex = _CtrlGrpAmpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 15, 1, 1),
    _CtrlGrpAmpsIndex_Type()
)
ctrlGrpAmpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrlGrpAmpsIndex.setStatus("current")
_CtrlGrpAmpsSerial_Type = DisplayString
_CtrlGrpAmpsSerial_Object = MibTableColumn
ctrlGrpAmpsSerial = _CtrlGrpAmpsSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 15, 1, 2),
    _CtrlGrpAmpsSerial_Type()
)
ctrlGrpAmpsSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsSerial.setStatus("current")
_CtrlGrpAmpsName_Type = DisplayString
_CtrlGrpAmpsName_Object = MibTableColumn
ctrlGrpAmpsName = _CtrlGrpAmpsName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 15, 1, 3),
    _CtrlGrpAmpsName_Type()
)
ctrlGrpAmpsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsName.setStatus("current")
_CtrlGrpAmpsAvail_Type = Unsigned32
_CtrlGrpAmpsAvail_Object = MibTableColumn
ctrlGrpAmpsAvail = _CtrlGrpAmpsAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 15, 1, 4),
    _CtrlGrpAmpsAvail_Type()
)
ctrlGrpAmpsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsAvail.setStatus("current")
_CtrlGrpAmpsA_Type = Unsigned32
_CtrlGrpAmpsA_Object = MibTableColumn
ctrlGrpAmpsA = _CtrlGrpAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 15, 1, 5),
    _CtrlGrpAmpsA_Type()
)
ctrlGrpAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsA.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsB_Type = Unsigned32
_CtrlGrpAmpsB_Object = MibTableColumn
ctrlGrpAmpsB = _CtrlGrpAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 15, 1, 6),
    _CtrlGrpAmpsB_Type()
)
ctrlGrpAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsB.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsC_Type = Unsigned32
_CtrlGrpAmpsC_Object = MibTableColumn
ctrlGrpAmpsC = _CtrlGrpAmpsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 15, 1, 7),
    _CtrlGrpAmpsC_Type()
)
ctrlGrpAmpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsC.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsD_Type = Unsigned32
_CtrlGrpAmpsD_Object = MibTableColumn
ctrlGrpAmpsD = _CtrlGrpAmpsD_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 15, 1, 8),
    _CtrlGrpAmpsD_Type()
)
ctrlGrpAmpsD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsD.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsD.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsE_Type = Unsigned32
_CtrlGrpAmpsE_Object = MibTableColumn
ctrlGrpAmpsE = _CtrlGrpAmpsE_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 15, 1, 9),
    _CtrlGrpAmpsE_Type()
)
ctrlGrpAmpsE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsE.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsE.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsF_Type = Unsigned32
_CtrlGrpAmpsF_Object = MibTableColumn
ctrlGrpAmpsF = _CtrlGrpAmpsF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 15, 1, 10),
    _CtrlGrpAmpsF_Type()
)
ctrlGrpAmpsF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsF.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsF.setUnits("0.1 Amps (rms)")
_CtrlOutletTable_Object = MibTable
ctrlOutletTable = _CtrlOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16)
)
if mibBuilder.loadTexts:
    ctrlOutletTable.setStatus("current")
_CtrlOutletEntry_Object = MibTableRow
ctrlOutletEntry = _CtrlOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1)
)
ctrlOutletEntry.setIndexNames(
    (0, "GEIST-MIB", "ctrlOutletIndex"),
)
if mibBuilder.loadTexts:
    ctrlOutletEntry.setStatus("current")


class _CtrlOutletIndex_Type(Integer32):
    """Custom type ctrlOutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CtrlOutletIndex_Type.__name__ = "Integer32"
_CtrlOutletIndex_Object = MibTableColumn
ctrlOutletIndex = _CtrlOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 1),
    _CtrlOutletIndex_Type()
)
ctrlOutletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrlOutletIndex.setStatus("current")
_CtrlOutletName_Type = DisplayString
_CtrlOutletName_Object = MibTableColumn
ctrlOutletName = _CtrlOutletName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 2),
    _CtrlOutletName_Type()
)
ctrlOutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletName.setStatus("current")
_CtrlOutletStatus_Type = Unsigned32
_CtrlOutletStatus_Object = MibTableColumn
ctrlOutletStatus = _CtrlOutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 3),
    _CtrlOutletStatus_Type()
)
ctrlOutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletStatus.setStatus("current")
_CtrlOutletFeedback_Type = Unsigned32
_CtrlOutletFeedback_Object = MibTableColumn
ctrlOutletFeedback = _CtrlOutletFeedback_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 4),
    _CtrlOutletFeedback_Type()
)
ctrlOutletFeedback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletFeedback.setStatus("current")
_CtrlOutletPending_Type = Unsigned32
_CtrlOutletPending_Object = MibTableColumn
ctrlOutletPending = _CtrlOutletPending_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 5),
    _CtrlOutletPending_Type()
)
ctrlOutletPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletPending.setStatus("current")
_CtrlOutletDeciAmps_Type = Unsigned32
_CtrlOutletDeciAmps_Object = MibTableColumn
ctrlOutletDeciAmps = _CtrlOutletDeciAmps_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 6),
    _CtrlOutletDeciAmps_Type()
)
ctrlOutletDeciAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletDeciAmps.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletDeciAmps.setUnits("0.1 Amps (rms)")
_CtrlOutletGroup_Type = DisplayString
_CtrlOutletGroup_Object = MibTableColumn
ctrlOutletGroup = _CtrlOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 7),
    _CtrlOutletGroup_Type()
)
ctrlOutletGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletGroup.setStatus("current")
_CtrlOutletUpDelay_Type = Unsigned32
_CtrlOutletUpDelay_Object = MibTableColumn
ctrlOutletUpDelay = _CtrlOutletUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 8),
    _CtrlOutletUpDelay_Type()
)
ctrlOutletUpDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletUpDelay.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletUpDelay.setUnits("seconds")
_CtrlOutletDwnDelay_Type = Unsigned32
_CtrlOutletDwnDelay_Object = MibTableColumn
ctrlOutletDwnDelay = _CtrlOutletDwnDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 9),
    _CtrlOutletDwnDelay_Type()
)
ctrlOutletDwnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletDwnDelay.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletDwnDelay.setUnits("seconds")
_CtrlOutletRbtDelay_Type = Unsigned32
_CtrlOutletRbtDelay_Object = MibTableColumn
ctrlOutletRbtDelay = _CtrlOutletRbtDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 10),
    _CtrlOutletRbtDelay_Type()
)
ctrlOutletRbtDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletRbtDelay.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletRbtDelay.setUnits("seconds")
_CtrlOutletURL_Type = DisplayString
_CtrlOutletURL_Object = MibTableColumn
ctrlOutletURL = _CtrlOutletURL_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 11),
    _CtrlOutletURL_Type()
)
ctrlOutletURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletURL.setStatus("current")
_CtrlOutletPOAAction_Type = Unsigned32
_CtrlOutletPOAAction_Object = MibTableColumn
ctrlOutletPOAAction = _CtrlOutletPOAAction_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 12),
    _CtrlOutletPOAAction_Type()
)
ctrlOutletPOAAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletPOAAction.setStatus("current")
_CtrlOutletPOADelay_Type = Unsigned32
_CtrlOutletPOADelay_Object = MibTableColumn
ctrlOutletPOADelay = _CtrlOutletPOADelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 16, 1, 13),
    _CtrlOutletPOADelay_Type()
)
ctrlOutletPOADelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletPOADelay.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletPOADelay.setUnits("seconds")
_DewPointSensorTable_Object = MibTable
dewPointSensorTable = _DewPointSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 17)
)
if mibBuilder.loadTexts:
    dewPointSensorTable.setStatus("current")
_DewPointSensorEntry_Object = MibTableRow
dewPointSensorEntry = _DewPointSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 17, 1)
)
dewPointSensorEntry.setIndexNames(
    (0, "GEIST-MIB", "dewPointSensorIndex"),
)
if mibBuilder.loadTexts:
    dewPointSensorEntry.setStatus("current")


class _DewPointSensorIndex_Type(Integer32):
    """Custom type dewPointSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DewPointSensorIndex_Type.__name__ = "Integer32"
_DewPointSensorIndex_Object = MibTableColumn
dewPointSensorIndex = _DewPointSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 17, 1, 1),
    _DewPointSensorIndex_Type()
)
dewPointSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dewPointSensorIndex.setStatus("current")
_DewPointSensorSerial_Type = DisplayString
_DewPointSensorSerial_Object = MibTableColumn
dewPointSensorSerial = _DewPointSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 17, 1, 2),
    _DewPointSensorSerial_Type()
)
dewPointSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorSerial.setStatus("current")
_DewPointSensorName_Type = DisplayString
_DewPointSensorName_Object = MibTableColumn
dewPointSensorName = _DewPointSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 17, 1, 3),
    _DewPointSensorName_Type()
)
dewPointSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorName.setStatus("current")
_DewPointSensorAvail_Type = Unsigned32
_DewPointSensorAvail_Object = MibTableColumn
dewPointSensorAvail = _DewPointSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 17, 1, 4),
    _DewPointSensorAvail_Type()
)
dewPointSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorAvail.setStatus("current")


class _DewPointSensorDewPoint_Type(Integer32):
    """Custom type dewPointSensorDewPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 123),
    )


_DewPointSensorDewPoint_Type.__name__ = "Integer32"
_DewPointSensorDewPoint_Object = MibTableColumn
dewPointSensorDewPoint = _DewPointSensorDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 17, 1, 5),
    _DewPointSensorDewPoint_Type()
)
dewPointSensorDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorDewPoint.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorDewPoint.setUnits("Degrees Celsius")


class _DewPointSensorTempC_Type(Integer32):
    """Custom type dewPointSensorTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 123),
    )


_DewPointSensorTempC_Type.__name__ = "Integer32"
_DewPointSensorTempC_Object = MibTableColumn
dewPointSensorTempC = _DewPointSensorTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 17, 1, 6),
    _DewPointSensorTempC_Type()
)
dewPointSensorTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorTempC.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorTempC.setUnits("Degrees Celsius")


class _DewPointSensorHumidity_Type(Integer32):
    """Custom type dewPointSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DewPointSensorHumidity_Type.__name__ = "Integer32"
_DewPointSensorHumidity_Object = MibTableColumn
dewPointSensorHumidity = _DewPointSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 17, 1, 7),
    _DewPointSensorHumidity_Type()
)
dewPointSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorHumidity.setUnits("%")
_DigitalSensorTable_Object = MibTable
digitalSensorTable = _DigitalSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 18)
)
if mibBuilder.loadTexts:
    digitalSensorTable.setStatus("current")
_DigitalSensorEntry_Object = MibTableRow
digitalSensorEntry = _DigitalSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 18, 1)
)
digitalSensorEntry.setIndexNames(
    (0, "GEIST-MIB", "digitalSensorIndex"),
)
if mibBuilder.loadTexts:
    digitalSensorEntry.setStatus("current")


class _DigitalSensorIndex_Type(Integer32):
    """Custom type digitalSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DigitalSensorIndex_Type.__name__ = "Integer32"
_DigitalSensorIndex_Object = MibTableColumn
digitalSensorIndex = _DigitalSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 18, 1, 1),
    _DigitalSensorIndex_Type()
)
digitalSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digitalSensorIndex.setStatus("current")
_DigitalSensorSerial_Type = DisplayString
_DigitalSensorSerial_Object = MibTableColumn
digitalSensorSerial = _DigitalSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 18, 1, 2),
    _DigitalSensorSerial_Type()
)
digitalSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalSensorSerial.setStatus("current")
_DigitalSensorName_Type = DisplayString
_DigitalSensorName_Object = MibTableColumn
digitalSensorName = _DigitalSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 18, 1, 3),
    _DigitalSensorName_Type()
)
digitalSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalSensorName.setStatus("current")
_DigitalSensorAvail_Type = Unsigned32
_DigitalSensorAvail_Object = MibTableColumn
digitalSensorAvail = _DigitalSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 18, 1, 4),
    _DigitalSensorAvail_Type()
)
digitalSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalSensorAvail.setStatus("current")


class _DigitalSensorDigital_Type(Integer32):
    """Custom type digitalSensorDigital based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DigitalSensorDigital_Type.__name__ = "Integer32"
_DigitalSensorDigital_Object = MibTableColumn
digitalSensorDigital = _DigitalSensorDigital_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 18, 1, 5),
    _DigitalSensorDigital_Type()
)
digitalSensorDigital.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalSensorDigital.setStatus("current")
_DstsTable_Object = MibTable
dstsTable = _DstsTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19)
)
if mibBuilder.loadTexts:
    dstsTable.setStatus("current")
_DstsEntry_Object = MibTableRow
dstsEntry = _DstsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1)
)
dstsEntry.setIndexNames(
    (0, "GEIST-MIB", "dstsIndex"),
)
if mibBuilder.loadTexts:
    dstsEntry.setStatus("current")


class _DstsIndex_Type(Integer32):
    """Custom type dstsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DstsIndex_Type.__name__ = "Integer32"
_DstsIndex_Object = MibTableColumn
dstsIndex = _DstsIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 1),
    _DstsIndex_Type()
)
dstsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dstsIndex.setStatus("current")
_DstsSerial_Type = DisplayString
_DstsSerial_Object = MibTableColumn
dstsSerial = _DstsSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 2),
    _DstsSerial_Type()
)
dstsSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsSerial.setStatus("current")
_DstsName_Type = DisplayString
_DstsName_Object = MibTableColumn
dstsName = _DstsName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 3),
    _DstsName_Type()
)
dstsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsName.setStatus("current")
_DstsAvail_Type = Unsigned32
_DstsAvail_Object = MibTableColumn
dstsAvail = _DstsAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 4),
    _DstsAvail_Type()
)
dstsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsAvail.setStatus("current")
_DstsVoltsA_Type = Unsigned32
_DstsVoltsA_Object = MibTableColumn
dstsVoltsA = _DstsVoltsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 5),
    _DstsVoltsA_Type()
)
dstsVoltsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsVoltsA.setStatus("current")
if mibBuilder.loadTexts:
    dstsVoltsA.setUnits("Volts (rms)")
_DstsAmpsA_Type = Unsigned32
_DstsAmpsA_Object = MibTableColumn
dstsAmpsA = _DstsAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 6),
    _DstsAmpsA_Type()
)
dstsAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    dstsAmpsA.setUnits("0.1 Amps (rms)")
_DstsVoltsB_Type = Unsigned32
_DstsVoltsB_Object = MibTableColumn
dstsVoltsB = _DstsVoltsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 7),
    _DstsVoltsB_Type()
)
dstsVoltsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsVoltsB.setStatus("current")
if mibBuilder.loadTexts:
    dstsVoltsB.setUnits("Volts (rms)")
_DstsAmpsB_Type = Unsigned32
_DstsAmpsB_Object = MibTableColumn
dstsAmpsB = _DstsAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 8),
    _DstsAmpsB_Type()
)
dstsAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    dstsAmpsB.setUnits("0.1 Amps (rms)")
_DstsSourceAActive_Type = Unsigned32
_DstsSourceAActive_Object = MibTableColumn
dstsSourceAActive = _DstsSourceAActive_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 9),
    _DstsSourceAActive_Type()
)
dstsSourceAActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsSourceAActive.setStatus("current")
_DstsSourceBActive_Type = Unsigned32
_DstsSourceBActive_Object = MibTableColumn
dstsSourceBActive = _DstsSourceBActive_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 10),
    _DstsSourceBActive_Type()
)
dstsSourceBActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsSourceBActive.setStatus("current")
_DstsPowerStatusA_Type = Unsigned32
_DstsPowerStatusA_Object = MibTableColumn
dstsPowerStatusA = _DstsPowerStatusA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 11),
    _DstsPowerStatusA_Type()
)
dstsPowerStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsPowerStatusA.setStatus("current")
_DstsPowerStatusB_Type = Unsigned32
_DstsPowerStatusB_Object = MibTableColumn
dstsPowerStatusB = _DstsPowerStatusB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 12),
    _DstsPowerStatusB_Type()
)
dstsPowerStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsPowerStatusB.setStatus("current")


class _DstsSourceATempC_Type(Integer32):
    """Custom type dstsSourceATempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 50),
    )


_DstsSourceATempC_Type.__name__ = "Integer32"
_DstsSourceATempC_Object = MibTableColumn
dstsSourceATempC = _DstsSourceATempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 13),
    _DstsSourceATempC_Type()
)
dstsSourceATempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsSourceATempC.setStatus("current")
if mibBuilder.loadTexts:
    dstsSourceATempC.setUnits("Degrees Celsius")


class _DstsSourceBTempC_Type(Integer32):
    """Custom type dstsSourceBTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 50),
    )


_DstsSourceBTempC_Type.__name__ = "Integer32"
_DstsSourceBTempC_Object = MibTableColumn
dstsSourceBTempC = _DstsSourceBTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 19, 1, 14),
    _DstsSourceBTempC_Type()
)
dstsSourceBTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsSourceBTempC.setStatus("current")
if mibBuilder.loadTexts:
    dstsSourceBTempC.setUnits("Degrees Celsius")
_CpmSensorTable_Object = MibTable
cpmSensorTable = _CpmSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 20)
)
if mibBuilder.loadTexts:
    cpmSensorTable.setStatus("current")
_CpmSensorEntry_Object = MibTableRow
cpmSensorEntry = _CpmSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 20, 1)
)
cpmSensorEntry.setIndexNames(
    (0, "GEIST-MIB", "cpmSensorIndex"),
)
if mibBuilder.loadTexts:
    cpmSensorEntry.setStatus("current")


class _CpmSensorIndex_Type(Integer32):
    """Custom type cpmSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpmSensorIndex_Type.__name__ = "Integer32"
_CpmSensorIndex_Object = MibTableColumn
cpmSensorIndex = _CpmSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 20, 1, 1),
    _CpmSensorIndex_Type()
)
cpmSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmSensorIndex.setStatus("current")
_CpmSensorSerial_Type = DisplayString
_CpmSensorSerial_Object = MibTableColumn
cpmSensorSerial = _CpmSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 20, 1, 2),
    _CpmSensorSerial_Type()
)
cpmSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmSensorSerial.setStatus("current")
_CpmSensorName_Type = DisplayString
_CpmSensorName_Object = MibTableColumn
cpmSensorName = _CpmSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 20, 1, 3),
    _CpmSensorName_Type()
)
cpmSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmSensorName.setStatus("current")
_CpmSensorAvail_Type = Unsigned32
_CpmSensorAvail_Object = MibTableColumn
cpmSensorAvail = _CpmSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 20, 1, 4),
    _CpmSensorAvail_Type()
)
cpmSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmSensorAvail.setStatus("current")


class _CpmSensorStatus_Type(Integer32):
    """Custom type cpmSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpmSensorStatus_Type.__name__ = "Integer32"
_CpmSensorStatus_Object = MibTableColumn
cpmSensorStatus = _CpmSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 20, 1, 5),
    _CpmSensorStatus_Type()
)
cpmSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmSensorStatus.setStatus("current")
_SmokeAlarmTable_Object = MibTable
smokeAlarmTable = _SmokeAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 21)
)
if mibBuilder.loadTexts:
    smokeAlarmTable.setStatus("current")
_SmokeAlarmEntry_Object = MibTableRow
smokeAlarmEntry = _SmokeAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 21, 1)
)
smokeAlarmEntry.setIndexNames(
    (0, "GEIST-MIB", "smokeAlarmIndex"),
)
if mibBuilder.loadTexts:
    smokeAlarmEntry.setStatus("current")


class _SmokeAlarmIndex_Type(Integer32):
    """Custom type smokeAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SmokeAlarmIndex_Type.__name__ = "Integer32"
_SmokeAlarmIndex_Object = MibTableColumn
smokeAlarmIndex = _SmokeAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 21, 1, 1),
    _SmokeAlarmIndex_Type()
)
smokeAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smokeAlarmIndex.setStatus("current")
_SmokeAlarmSerial_Type = DisplayString
_SmokeAlarmSerial_Object = MibTableColumn
smokeAlarmSerial = _SmokeAlarmSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 21, 1, 2),
    _SmokeAlarmSerial_Type()
)
smokeAlarmSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeAlarmSerial.setStatus("current")
_SmokeAlarmName_Type = DisplayString
_SmokeAlarmName_Object = MibTableColumn
smokeAlarmName = _SmokeAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 21, 1, 3),
    _SmokeAlarmName_Type()
)
smokeAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeAlarmName.setStatus("current")
_SmokeAlarmAvail_Type = Unsigned32
_SmokeAlarmAvail_Object = MibTableColumn
smokeAlarmAvail = _SmokeAlarmAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 21, 1, 4),
    _SmokeAlarmAvail_Type()
)
smokeAlarmAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeAlarmAvail.setStatus("current")


class _SmokeAlarmStatus_Type(Integer32):
    """Custom type smokeAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SmokeAlarmStatus_Type.__name__ = "Integer32"
_SmokeAlarmStatus_Object = MibTableColumn
smokeAlarmStatus = _SmokeAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 21, 1, 5),
    _SmokeAlarmStatus_Type()
)
smokeAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeAlarmStatus.setStatus("current")
_Neg48VdcSensorTable_Object = MibTable
neg48VdcSensorTable = _Neg48VdcSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 22)
)
if mibBuilder.loadTexts:
    neg48VdcSensorTable.setStatus("current")
_Neg48VdcSensorEntry_Object = MibTableRow
neg48VdcSensorEntry = _Neg48VdcSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 22, 1)
)
neg48VdcSensorEntry.setIndexNames(
    (0, "GEIST-MIB", "neg48VdcSensorIndex"),
)
if mibBuilder.loadTexts:
    neg48VdcSensorEntry.setStatus("current")


class _Neg48VdcSensorIndex_Type(Integer32):
    """Custom type neg48VdcSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Neg48VdcSensorIndex_Type.__name__ = "Integer32"
_Neg48VdcSensorIndex_Object = MibTableColumn
neg48VdcSensorIndex = _Neg48VdcSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 22, 1, 1),
    _Neg48VdcSensorIndex_Type()
)
neg48VdcSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neg48VdcSensorIndex.setStatus("current")
_Neg48VdcSensorSerial_Type = DisplayString
_Neg48VdcSensorSerial_Object = MibTableColumn
neg48VdcSensorSerial = _Neg48VdcSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 22, 1, 2),
    _Neg48VdcSensorSerial_Type()
)
neg48VdcSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neg48VdcSensorSerial.setStatus("current")
_Neg48VdcSensorName_Type = DisplayString
_Neg48VdcSensorName_Object = MibTableColumn
neg48VdcSensorName = _Neg48VdcSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 22, 1, 3),
    _Neg48VdcSensorName_Type()
)
neg48VdcSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neg48VdcSensorName.setStatus("current")
_Neg48VdcSensorAvail_Type = Unsigned32
_Neg48VdcSensorAvail_Object = MibTableColumn
neg48VdcSensorAvail = _Neg48VdcSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 22, 1, 4),
    _Neg48VdcSensorAvail_Type()
)
neg48VdcSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neg48VdcSensorAvail.setStatus("current")


class _Neg48VdcSensorVoltage_Type(Integer32):
    """Custom type neg48VdcSensorVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 10),
    )


_Neg48VdcSensorVoltage_Type.__name__ = "Integer32"
_Neg48VdcSensorVoltage_Object = MibTableColumn
neg48VdcSensorVoltage = _Neg48VdcSensorVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 22, 1, 5),
    _Neg48VdcSensorVoltage_Type()
)
neg48VdcSensorVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neg48VdcSensorVoltage.setStatus("current")
if mibBuilder.loadTexts:
    neg48VdcSensorVoltage.setUnits("Volts")
_Pos30VdcSensorTable_Object = MibTable
pos30VdcSensorTable = _Pos30VdcSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 23)
)
if mibBuilder.loadTexts:
    pos30VdcSensorTable.setStatus("current")
_Pos30VdcSensorEntry_Object = MibTableRow
pos30VdcSensorEntry = _Pos30VdcSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 23, 1)
)
pos30VdcSensorEntry.setIndexNames(
    (0, "GEIST-MIB", "pos30VdcSensorIndex"),
)
if mibBuilder.loadTexts:
    pos30VdcSensorEntry.setStatus("current")


class _Pos30VdcSensorIndex_Type(Integer32):
    """Custom type pos30VdcSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Pos30VdcSensorIndex_Type.__name__ = "Integer32"
_Pos30VdcSensorIndex_Object = MibTableColumn
pos30VdcSensorIndex = _Pos30VdcSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 23, 1, 1),
    _Pos30VdcSensorIndex_Type()
)
pos30VdcSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pos30VdcSensorIndex.setStatus("current")
_Pos30VdcSensorSerial_Type = DisplayString
_Pos30VdcSensorSerial_Object = MibTableColumn
pos30VdcSensorSerial = _Pos30VdcSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 23, 1, 2),
    _Pos30VdcSensorSerial_Type()
)
pos30VdcSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos30VdcSensorSerial.setStatus("current")
_Pos30VdcSensorName_Type = DisplayString
_Pos30VdcSensorName_Object = MibTableColumn
pos30VdcSensorName = _Pos30VdcSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 23, 1, 3),
    _Pos30VdcSensorName_Type()
)
pos30VdcSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos30VdcSensorName.setStatus("current")
_Pos30VdcSensorAvail_Type = Unsigned32
_Pos30VdcSensorAvail_Object = MibTableColumn
pos30VdcSensorAvail = _Pos30VdcSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 23, 1, 4),
    _Pos30VdcSensorAvail_Type()
)
pos30VdcSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos30VdcSensorAvail.setStatus("current")


class _Pos30VdcSensorVoltage_Type(Integer32):
    """Custom type pos30VdcSensorVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 100),
    )


_Pos30VdcSensorVoltage_Type.__name__ = "Integer32"
_Pos30VdcSensorVoltage_Object = MibTableColumn
pos30VdcSensorVoltage = _Pos30VdcSensorVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 23, 1, 5),
    _Pos30VdcSensorVoltage_Type()
)
pos30VdcSensorVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos30VdcSensorVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pos30VdcSensorVoltage.setUnits("Volts")
_AnalogSensorTable_Object = MibTable
analogSensorTable = _AnalogSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 24)
)
if mibBuilder.loadTexts:
    analogSensorTable.setStatus("current")
_AnalogSensorEntry_Object = MibTableRow
analogSensorEntry = _AnalogSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 24, 1)
)
analogSensorEntry.setIndexNames(
    (0, "GEIST-MIB", "analogSensorIndex"),
)
if mibBuilder.loadTexts:
    analogSensorEntry.setStatus("current")


class _AnalogSensorIndex_Type(Integer32):
    """Custom type analogSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AnalogSensorIndex_Type.__name__ = "Integer32"
_AnalogSensorIndex_Object = MibTableColumn
analogSensorIndex = _AnalogSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 24, 1, 1),
    _AnalogSensorIndex_Type()
)
analogSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    analogSensorIndex.setStatus("current")
_AnalogSensorSerial_Type = DisplayString
_AnalogSensorSerial_Object = MibTableColumn
analogSensorSerial = _AnalogSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 24, 1, 2),
    _AnalogSensorSerial_Type()
)
analogSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogSensorSerial.setStatus("current")
_AnalogSensorName_Type = DisplayString
_AnalogSensorName_Object = MibTableColumn
analogSensorName = _AnalogSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 24, 1, 3),
    _AnalogSensorName_Type()
)
analogSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogSensorName.setStatus("current")
_AnalogSensorAvail_Type = Unsigned32
_AnalogSensorAvail_Object = MibTableColumn
analogSensorAvail = _AnalogSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 24, 1, 4),
    _AnalogSensorAvail_Type()
)
analogSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogSensorAvail.setStatus("current")


class _AnalogSensorAnalog_Type(Integer32):
    """Custom type analogSensorAnalog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AnalogSensorAnalog_Type.__name__ = "Integer32"
_AnalogSensorAnalog_Object = MibTableColumn
analogSensorAnalog = _AnalogSensorAnalog_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 24, 1, 5),
    _AnalogSensorAnalog_Type()
)
analogSensorAnalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogSensorAnalog.setStatus("current")
_Ctrl3ChIECTable_Object = MibTable
ctrl3ChIECTable = _Ctrl3ChIECTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25)
)
if mibBuilder.loadTexts:
    ctrl3ChIECTable.setStatus("current")
_Ctrl3ChIECEntry_Object = MibTableRow
ctrl3ChIECEntry = _Ctrl3ChIECEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1)
)
ctrl3ChIECEntry.setIndexNames(
    (0, "GEIST-MIB", "ctrl3ChIECIndex"),
)
if mibBuilder.loadTexts:
    ctrl3ChIECEntry.setStatus("current")


class _Ctrl3ChIECIndex_Type(Integer32):
    """Custom type ctrl3ChIECIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Ctrl3ChIECIndex_Type.__name__ = "Integer32"
_Ctrl3ChIECIndex_Object = MibTableColumn
ctrl3ChIECIndex = _Ctrl3ChIECIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 1),
    _Ctrl3ChIECIndex_Type()
)
ctrl3ChIECIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrl3ChIECIndex.setStatus("current")
_Ctrl3ChIECSerial_Type = DisplayString
_Ctrl3ChIECSerial_Object = MibTableColumn
ctrl3ChIECSerial = _Ctrl3ChIECSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 2),
    _Ctrl3ChIECSerial_Type()
)
ctrl3ChIECSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECSerial.setStatus("current")
_Ctrl3ChIECName_Type = DisplayString
_Ctrl3ChIECName_Object = MibTableColumn
ctrl3ChIECName = _Ctrl3ChIECName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 3),
    _Ctrl3ChIECName_Type()
)
ctrl3ChIECName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECName.setStatus("current")
_Ctrl3ChIECAvail_Type = Unsigned32
_Ctrl3ChIECAvail_Object = MibTableColumn
ctrl3ChIECAvail = _Ctrl3ChIECAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 4),
    _Ctrl3ChIECAvail_Type()
)
ctrl3ChIECAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECAvail.setStatus("current")
_Ctrl3ChIECKWattHrsA_Type = Unsigned32
_Ctrl3ChIECKWattHrsA_Object = MibTableColumn
ctrl3ChIECKWattHrsA = _Ctrl3ChIECKWattHrsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 5),
    _Ctrl3ChIECKWattHrsA_Type()
)
ctrl3ChIECKWattHrsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECKWattHrsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECKWattHrsA.setUnits("KWh")
_Ctrl3ChIECVoltsA_Type = Unsigned32
_Ctrl3ChIECVoltsA_Object = MibTableColumn
ctrl3ChIECVoltsA = _Ctrl3ChIECVoltsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 6),
    _Ctrl3ChIECVoltsA_Type()
)
ctrl3ChIECVoltsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltsA.setUnits("Volts (rms)")
_Ctrl3ChIECVoltPeakA_Type = Unsigned32
_Ctrl3ChIECVoltPeakA_Object = MibTableColumn
ctrl3ChIECVoltPeakA = _Ctrl3ChIECVoltPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 7),
    _Ctrl3ChIECVoltPeakA_Type()
)
ctrl3ChIECVoltPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltPeakA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltPeakA.setUnits("Volts (rms)")
_Ctrl3ChIECDeciAmpsA_Type = Unsigned32
_Ctrl3ChIECDeciAmpsA_Object = MibTableColumn
ctrl3ChIECDeciAmpsA = _Ctrl3ChIECDeciAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 8),
    _Ctrl3ChIECDeciAmpsA_Type()
)
ctrl3ChIECDeciAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsA.setUnits("0.1 Amps (rms)")
_Ctrl3ChIECDeciAmpsPeakA_Type = Unsigned32
_Ctrl3ChIECDeciAmpsPeakA_Object = MibTableColumn
ctrl3ChIECDeciAmpsPeakA = _Ctrl3ChIECDeciAmpsPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 9),
    _Ctrl3ChIECDeciAmpsPeakA_Type()
)
ctrl3ChIECDeciAmpsPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsPeakA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsPeakA.setUnits("0.1 Amps (rms)")
_Ctrl3ChIECRealPowerA_Type = Unsigned32
_Ctrl3ChIECRealPowerA_Object = MibTableColumn
ctrl3ChIECRealPowerA = _Ctrl3ChIECRealPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 10),
    _Ctrl3ChIECRealPowerA_Type()
)
ctrl3ChIECRealPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerA.setUnits("Watts")
_Ctrl3ChIECApparentPowerA_Type = Unsigned32
_Ctrl3ChIECApparentPowerA_Object = MibTableColumn
ctrl3ChIECApparentPowerA = _Ctrl3ChIECApparentPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 11),
    _Ctrl3ChIECApparentPowerA_Type()
)
ctrl3ChIECApparentPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECApparentPowerA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECApparentPowerA.setUnits("Volt-Amps")


class _Ctrl3ChIECPowerFactorA_Type(Integer32):
    """Custom type ctrl3ChIECPowerFactorA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ctrl3ChIECPowerFactorA_Type.__name__ = "Integer32"
_Ctrl3ChIECPowerFactorA_Object = MibTableColumn
ctrl3ChIECPowerFactorA = _Ctrl3ChIECPowerFactorA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 12),
    _Ctrl3ChIECPowerFactorA_Type()
)
ctrl3ChIECPowerFactorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECPowerFactorA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECPowerFactorA.setUnits("%")
_Ctrl3ChIECKWattHrsB_Type = Unsigned32
_Ctrl3ChIECKWattHrsB_Object = MibTableColumn
ctrl3ChIECKWattHrsB = _Ctrl3ChIECKWattHrsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 13),
    _Ctrl3ChIECKWattHrsB_Type()
)
ctrl3ChIECKWattHrsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECKWattHrsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECKWattHrsB.setUnits("KWh")
_Ctrl3ChIECVoltsB_Type = Unsigned32
_Ctrl3ChIECVoltsB_Object = MibTableColumn
ctrl3ChIECVoltsB = _Ctrl3ChIECVoltsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 14),
    _Ctrl3ChIECVoltsB_Type()
)
ctrl3ChIECVoltsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltsB.setUnits("Volts (rms)")
_Ctrl3ChIECVoltPeakB_Type = Unsigned32
_Ctrl3ChIECVoltPeakB_Object = MibTableColumn
ctrl3ChIECVoltPeakB = _Ctrl3ChIECVoltPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 15),
    _Ctrl3ChIECVoltPeakB_Type()
)
ctrl3ChIECVoltPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltPeakB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltPeakB.setUnits("Volts (rms)")
_Ctrl3ChIECDeciAmpsB_Type = Unsigned32
_Ctrl3ChIECDeciAmpsB_Object = MibTableColumn
ctrl3ChIECDeciAmpsB = _Ctrl3ChIECDeciAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 16),
    _Ctrl3ChIECDeciAmpsB_Type()
)
ctrl3ChIECDeciAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsB.setUnits("0.1 Amps (rms)")
_Ctrl3ChIECDeciAmpsPeakB_Type = Unsigned32
_Ctrl3ChIECDeciAmpsPeakB_Object = MibTableColumn
ctrl3ChIECDeciAmpsPeakB = _Ctrl3ChIECDeciAmpsPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 17),
    _Ctrl3ChIECDeciAmpsPeakB_Type()
)
ctrl3ChIECDeciAmpsPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsPeakB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsPeakB.setUnits("0.1 Amps (rms)")
_Ctrl3ChIECRealPowerB_Type = Unsigned32
_Ctrl3ChIECRealPowerB_Object = MibTableColumn
ctrl3ChIECRealPowerB = _Ctrl3ChIECRealPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 18),
    _Ctrl3ChIECRealPowerB_Type()
)
ctrl3ChIECRealPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerB.setUnits("Watts")
_Ctrl3ChIECApparentPowerB_Type = Unsigned32
_Ctrl3ChIECApparentPowerB_Object = MibTableColumn
ctrl3ChIECApparentPowerB = _Ctrl3ChIECApparentPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 19),
    _Ctrl3ChIECApparentPowerB_Type()
)
ctrl3ChIECApparentPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECApparentPowerB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECApparentPowerB.setUnits("Volt-Amps")


class _Ctrl3ChIECPowerFactorB_Type(Integer32):
    """Custom type ctrl3ChIECPowerFactorB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ctrl3ChIECPowerFactorB_Type.__name__ = "Integer32"
_Ctrl3ChIECPowerFactorB_Object = MibTableColumn
ctrl3ChIECPowerFactorB = _Ctrl3ChIECPowerFactorB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 20),
    _Ctrl3ChIECPowerFactorB_Type()
)
ctrl3ChIECPowerFactorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECPowerFactorB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECPowerFactorB.setUnits("%")
_Ctrl3ChIECKWattHrsC_Type = Unsigned32
_Ctrl3ChIECKWattHrsC_Object = MibTableColumn
ctrl3ChIECKWattHrsC = _Ctrl3ChIECKWattHrsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 21),
    _Ctrl3ChIECKWattHrsC_Type()
)
ctrl3ChIECKWattHrsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECKWattHrsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECKWattHrsC.setUnits("KWh")
_Ctrl3ChIECVoltsC_Type = Unsigned32
_Ctrl3ChIECVoltsC_Object = MibTableColumn
ctrl3ChIECVoltsC = _Ctrl3ChIECVoltsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 22),
    _Ctrl3ChIECVoltsC_Type()
)
ctrl3ChIECVoltsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltsC.setUnits("Volts (rms)")
_Ctrl3ChIECVoltPeakC_Type = Unsigned32
_Ctrl3ChIECVoltPeakC_Object = MibTableColumn
ctrl3ChIECVoltPeakC = _Ctrl3ChIECVoltPeakC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 23),
    _Ctrl3ChIECVoltPeakC_Type()
)
ctrl3ChIECVoltPeakC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltPeakC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltPeakC.setUnits("Volts (rms)")
_Ctrl3ChIECDeciAmpsC_Type = Unsigned32
_Ctrl3ChIECDeciAmpsC_Object = MibTableColumn
ctrl3ChIECDeciAmpsC = _Ctrl3ChIECDeciAmpsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 24),
    _Ctrl3ChIECDeciAmpsC_Type()
)
ctrl3ChIECDeciAmpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsC.setUnits("0.1 Amps (rms)")
_Ctrl3ChIECDeciAmpsPeakC_Type = Unsigned32
_Ctrl3ChIECDeciAmpsPeakC_Object = MibTableColumn
ctrl3ChIECDeciAmpsPeakC = _Ctrl3ChIECDeciAmpsPeakC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 25),
    _Ctrl3ChIECDeciAmpsPeakC_Type()
)
ctrl3ChIECDeciAmpsPeakC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsPeakC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsPeakC.setUnits("0.1 Amps (rms)")
_Ctrl3ChIECRealPowerC_Type = Unsigned32
_Ctrl3ChIECRealPowerC_Object = MibTableColumn
ctrl3ChIECRealPowerC = _Ctrl3ChIECRealPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 26),
    _Ctrl3ChIECRealPowerC_Type()
)
ctrl3ChIECRealPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerC.setUnits("Watts")
_Ctrl3ChIECApparentPowerC_Type = Unsigned32
_Ctrl3ChIECApparentPowerC_Object = MibTableColumn
ctrl3ChIECApparentPowerC = _Ctrl3ChIECApparentPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 27),
    _Ctrl3ChIECApparentPowerC_Type()
)
ctrl3ChIECApparentPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECApparentPowerC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECApparentPowerC.setUnits("Volt-Amps")


class _Ctrl3ChIECPowerFactorC_Type(Integer32):
    """Custom type ctrl3ChIECPowerFactorC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ctrl3ChIECPowerFactorC_Type.__name__ = "Integer32"
_Ctrl3ChIECPowerFactorC_Object = MibTableColumn
ctrl3ChIECPowerFactorC = _Ctrl3ChIECPowerFactorC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 25, 1, 28),
    _Ctrl3ChIECPowerFactorC_Type()
)
ctrl3ChIECPowerFactorC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECPowerFactorC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECPowerFactorC.setUnits("%")
_AirSpeedSwitchSensorTable_Object = MibTable
airSpeedSwitchSensorTable = _AirSpeedSwitchSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 26)
)
if mibBuilder.loadTexts:
    airSpeedSwitchSensorTable.setStatus("current")
_AirSpeedSwitchSensorEntry_Object = MibTableRow
airSpeedSwitchSensorEntry = _AirSpeedSwitchSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 26, 1)
)
airSpeedSwitchSensorEntry.setIndexNames(
    (0, "GEIST-MIB", "airSpeedSwitchSensorIndex"),
)
if mibBuilder.loadTexts:
    airSpeedSwitchSensorEntry.setStatus("current")


class _AirSpeedSwitchSensorIndex_Type(Integer32):
    """Custom type airSpeedSwitchSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AirSpeedSwitchSensorIndex_Type.__name__ = "Integer32"
_AirSpeedSwitchSensorIndex_Object = MibTableColumn
airSpeedSwitchSensorIndex = _AirSpeedSwitchSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 26, 1, 1),
    _AirSpeedSwitchSensorIndex_Type()
)
airSpeedSwitchSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    airSpeedSwitchSensorIndex.setStatus("current")
_AirSpeedSwitchSensorSerial_Type = DisplayString
_AirSpeedSwitchSensorSerial_Object = MibTableColumn
airSpeedSwitchSensorSerial = _AirSpeedSwitchSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 26, 1, 2),
    _AirSpeedSwitchSensorSerial_Type()
)
airSpeedSwitchSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airSpeedSwitchSensorSerial.setStatus("current")
_AirSpeedSwitchSensorName_Type = DisplayString
_AirSpeedSwitchSensorName_Object = MibTableColumn
airSpeedSwitchSensorName = _AirSpeedSwitchSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 26, 1, 3),
    _AirSpeedSwitchSensorName_Type()
)
airSpeedSwitchSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airSpeedSwitchSensorName.setStatus("current")
_AirSpeedSwitchSensorAvail_Type = Unsigned32
_AirSpeedSwitchSensorAvail_Object = MibTableColumn
airSpeedSwitchSensorAvail = _AirSpeedSwitchSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 26, 1, 4),
    _AirSpeedSwitchSensorAvail_Type()
)
airSpeedSwitchSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airSpeedSwitchSensorAvail.setStatus("current")


class _AirSpeedSwitchSensorAirSpeed_Type(Integer32):
    """Custom type airSpeedSwitchSensorAirSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AirSpeedSwitchSensorAirSpeed_Type.__name__ = "Integer32"
_AirSpeedSwitchSensorAirSpeed_Object = MibTableColumn
airSpeedSwitchSensorAirSpeed = _AirSpeedSwitchSensorAirSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21239, 1, 26, 1, 5),
    _AirSpeedSwitchSensorAirSpeed_Type()
)
airSpeedSwitchSensorAirSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airSpeedSwitchSensorAirSpeed.setStatus("current")

# Managed Objects groups


# Notification objects

gstTestTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10101)
)
if mibBuilder.loadTexts:
    gstTestTRAP.setStatus(
        ""
    )

gstClimateTempCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10205)
)
gstClimateTempCTRAP.setObjects(
      *(("GEIST-MIB", "climateTempC"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateTempCTRAP.setStatus(
        ""
    )

gstClimateHumidityTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10206)
)
gstClimateHumidityTRAP.setObjects(
      *(("GEIST-MIB", "climateHumidity"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateHumidityTRAP.setStatus(
        ""
    )

gstClimateAirflowTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10207)
)
gstClimateAirflowTRAP.setObjects(
      *(("GEIST-MIB", "climateAirflow"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateAirflowTRAP.setStatus(
        ""
    )

gstClimateLightTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10208)
)
gstClimateLightTRAP.setObjects(
      *(("GEIST-MIB", "climateLight"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateLightTRAP.setStatus(
        ""
    )

gstClimateSoundTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10209)
)
gstClimateSoundTRAP.setObjects(
      *(("GEIST-MIB", "climateSound"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateSoundTRAP.setStatus(
        ""
    )

gstClimateIO1TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10210)
)
gstClimateIO1TRAP.setObjects(
      *(("GEIST-MIB", "climateIO1"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateIO1TRAP.setStatus(
        ""
    )

gstClimateIO2TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10211)
)
gstClimateIO2TRAP.setObjects(
      *(("GEIST-MIB", "climateIO2"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateIO2TRAP.setStatus(
        ""
    )

gstClimateIO3TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10212)
)
gstClimateIO3TRAP.setObjects(
      *(("GEIST-MIB", "climateIO3"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateIO3TRAP.setStatus(
        ""
    )

gstClimateVoltsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10213)
)
gstClimateVoltsTRAP.setObjects(
      *(("GEIST-MIB", "climateVolts"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateVoltsTRAP.setStatus(
        ""
    )

gstClimateVoltPeakTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10214)
)
gstClimateVoltPeakTRAP.setObjects(
      *(("GEIST-MIB", "climateVoltPeak"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateVoltPeakTRAP.setStatus(
        ""
    )

gstClimateDeciAmpsATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10215)
)
gstClimateDeciAmpsATRAP.setObjects(
      *(("GEIST-MIB", "climateDeciAmpsA"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpsATRAP.setStatus(
        ""
    )

gstClimateAmpPeakATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10216)
)
gstClimateAmpPeakATRAP.setObjects(
      *(("GEIST-MIB", "climateAmpPeakA"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateAmpPeakATRAP.setStatus(
        ""
    )

gstClimateRealPowerATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10217)
)
gstClimateRealPowerATRAP.setObjects(
      *(("GEIST-MIB", "climateRealPowerA"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateRealPowerATRAP.setStatus(
        ""
    )

gstClimateApparentPowerATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10218)
)
gstClimateApparentPowerATRAP.setObjects(
      *(("GEIST-MIB", "climateApparentPowerA"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateApparentPowerATRAP.setStatus(
        ""
    )

gstClimatePowerFactorATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10219)
)
gstClimatePowerFactorATRAP.setObjects(
      *(("GEIST-MIB", "climatePowerFactorA"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimatePowerFactorATRAP.setStatus(
        ""
    )

gstClimateDeciAmpsBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10220)
)
gstClimateDeciAmpsBTRAP.setObjects(
      *(("GEIST-MIB", "climateDeciAmpsB"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpsBTRAP.setStatus(
        ""
    )

gstClimateDeciAmpPeakBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10221)
)
gstClimateDeciAmpPeakBTRAP.setObjects(
      *(("GEIST-MIB", "climateDeciAmpPeakB"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpPeakBTRAP.setStatus(
        ""
    )

gstClimateRealPowerBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10222)
)
gstClimateRealPowerBTRAP.setObjects(
      *(("GEIST-MIB", "climateRealPowerB"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateRealPowerBTRAP.setStatus(
        ""
    )

gstClimateApparentPowerBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10223)
)
gstClimateApparentPowerBTRAP.setObjects(
      *(("GEIST-MIB", "climateApparentPowerB"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateApparentPowerBTRAP.setStatus(
        ""
    )

gstClimatePowerFactorBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10224)
)
gstClimatePowerFactorBTRAP.setObjects(
      *(("GEIST-MIB", "climatePowerFactorB"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimatePowerFactorBTRAP.setStatus(
        ""
    )

gstClimateDeciAmpsCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10225)
)
gstClimateDeciAmpsCTRAP.setObjects(
      *(("GEIST-MIB", "climateDeciAmpsC"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpsCTRAP.setStatus(
        ""
    )

gstClimateDeciAmpPeakCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10226)
)
gstClimateDeciAmpPeakCTRAP.setObjects(
      *(("GEIST-MIB", "climateDeciAmpPeakC"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpPeakCTRAP.setStatus(
        ""
    )

gstClimateRealPowerCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10227)
)
gstClimateRealPowerCTRAP.setObjects(
      *(("GEIST-MIB", "climateRealPowerC"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateRealPowerCTRAP.setStatus(
        ""
    )

gstClimateApparentPowerCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10228)
)
gstClimateApparentPowerCTRAP.setObjects(
      *(("GEIST-MIB", "climateApparentPowerC"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateApparentPowerCTRAP.setStatus(
        ""
    )

gstClimatePowerFactorCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10229)
)
gstClimatePowerFactorCTRAP.setObjects(
      *(("GEIST-MIB", "climatePowerFactorC"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimatePowerFactorCTRAP.setStatus(
        ""
    )

gstPowMonKWattHrsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10305)
)
gstPowMonKWattHrsTRAP.setObjects(
      *(("GEIST-MIB", "powMonKWattHrs"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonKWattHrsTRAP.setStatus(
        ""
    )

gstPowMonVoltsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10306)
)
gstPowMonVoltsTRAP.setObjects(
      *(("GEIST-MIB", "powMonVolts"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltsTRAP.setStatus(
        ""
    )

gstPowMonVoltMaxTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10307)
)
gstPowMonVoltMaxTRAP.setObjects(
      *(("GEIST-MIB", "powMonVoltMax"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltMaxTRAP.setStatus(
        ""
    )

gstPowMonVoltMinTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10308)
)
gstPowMonVoltMinTRAP.setObjects(
      *(("GEIST-MIB", "powMonVoltMin"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltMinTRAP.setStatus(
        ""
    )

gstPowMonVoltPeakTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10309)
)
gstPowMonVoltPeakTRAP.setObjects(
      *(("GEIST-MIB", "powMonVoltPeak"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltPeakTRAP.setStatus(
        ""
    )

gstPowMonDeciAmpsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10310)
)
gstPowMonDeciAmpsTRAP.setObjects(
      *(("GEIST-MIB", "powMonDeciAmps"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonDeciAmpsTRAP.setStatus(
        ""
    )

gstPowMonRealPowerTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10311)
)
gstPowMonRealPowerTRAP.setObjects(
      *(("GEIST-MIB", "powMonRealPower"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonRealPowerTRAP.setStatus(
        ""
    )

gstPowMonApparentPowerTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10312)
)
gstPowMonApparentPowerTRAP.setObjects(
      *(("GEIST-MIB", "powMonApparentPower"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonApparentPowerTRAP.setStatus(
        ""
    )

gstPowMonPowerFactorTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10313)
)
gstPowMonPowerFactorTRAP.setObjects(
      *(("GEIST-MIB", "powMonPowerFactor"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonPowerFactorTRAP.setStatus(
        ""
    )

gstPowMonDeciAmpsOutlet1TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10314)
)
gstPowMonDeciAmpsOutlet1TRAP.setObjects(
      *(("GEIST-MIB", "powMonDeciAmpsOutlet1"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonDeciAmpsOutlet1TRAP.setStatus(
        ""
    )

gstPowMonDeciAmpsOutlet2TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10315)
)
gstPowMonDeciAmpsOutlet2TRAP.setObjects(
      *(("GEIST-MIB", "powMonDeciAmpsOutlet2"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonDeciAmpsOutlet2TRAP.setStatus(
        ""
    )

gstTempSensorTempCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10405)
)
gstTempSensorTempCTRAP.setObjects(
      *(("GEIST-MIB", "tempSensorTempC"),
        ("GEIST-MIB", "tempSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstTempSensorTempCTRAP.setStatus(
        ""
    )

gstAirFlowSensorFlowTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10505)
)
gstAirFlowSensorFlowTRAP.setObjects(
      *(("GEIST-MIB", "airFlowSensorFlow"),
        ("GEIST-MIB", "airFlowSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorFlowTRAP.setStatus(
        ""
    )

gstAirFlowSensorTempCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10506)
)
gstAirFlowSensorTempCTRAP.setObjects(
      *(("GEIST-MIB", "airFlowSensorTempC"),
        ("GEIST-MIB", "airFlowSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorTempCTRAP.setStatus(
        ""
    )

gstAirFlowSensorHumidityTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10507)
)
gstAirFlowSensorHumidityTRAP.setObjects(
      *(("GEIST-MIB", "airFlowSensorHumidity"),
        ("GEIST-MIB", "airFlowSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorHumidityTRAP.setStatus(
        ""
    )

gstAirFlowSensorDewPointTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10508)
)
gstAirFlowSensorDewPointTRAP.setObjects(
      *(("GEIST-MIB", "airFlowSensorDewPoint"),
        ("GEIST-MIB", "airFlowSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorDewPointTRAP.setStatus(
        ""
    )

gstPowerVoltsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10605)
)
gstPowerVoltsTRAP.setObjects(
      *(("GEIST-MIB", "powerVolts"),
        ("GEIST-MIB", "powerName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowerVoltsTRAP.setStatus(
        ""
    )

gstPowerDeciAmpsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10606)
)
gstPowerDeciAmpsTRAP.setObjects(
      *(("GEIST-MIB", "powerDeciAmps"),
        ("GEIST-MIB", "powerName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowerDeciAmpsTRAP.setStatus(
        ""
    )

gstPowerRealPowerTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10607)
)
gstPowerRealPowerTRAP.setObjects(
      *(("GEIST-MIB", "powerRealPower"),
        ("GEIST-MIB", "powerName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowerRealPowerTRAP.setStatus(
        ""
    )

gstPowerApparentPowerTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10608)
)
gstPowerApparentPowerTRAP.setObjects(
      *(("GEIST-MIB", "powerApparentPower"),
        ("GEIST-MIB", "powerName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowerApparentPowerTRAP.setStatus(
        ""
    )

gstPowerPowerFactorTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10609)
)
gstPowerPowerFactorTRAP.setObjects(
      *(("GEIST-MIB", "powerPowerFactor"),
        ("GEIST-MIB", "powerName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowerPowerFactorTRAP.setStatus(
        ""
    )

gstDoorSensorStatusTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10705)
)
gstDoorSensorStatusTRAP.setObjects(
      *(("GEIST-MIB", "doorSensorStatus"),
        ("GEIST-MIB", "doorSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDoorSensorStatusTRAP.setStatus(
        ""
    )

gstWaterSensorDampnessTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10805)
)
gstWaterSensorDampnessTRAP.setObjects(
      *(("GEIST-MIB", "waterSensorDampness"),
        ("GEIST-MIB", "waterSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstWaterSensorDampnessTRAP.setStatus(
        ""
    )

gstCurrentMonitorDeciAmpsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 10905)
)
gstCurrentMonitorDeciAmpsTRAP.setObjects(
      *(("GEIST-MIB", "currentMonitorDeciAmps"),
        ("GEIST-MIB", "currentMonitorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCurrentMonitorDeciAmpsTRAP.setStatus(
        ""
    )

gstMillivoltMonitorMVTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11005)
)
gstMillivoltMonitorMVTRAP.setObjects(
      *(("GEIST-MIB", "millivoltMonitorMV"),
        ("GEIST-MIB", "millivoltMonitorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstMillivoltMonitorMVTRAP.setStatus(
        ""
    )

gstPow3ChKWattHrsATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11105)
)
gstPow3ChKWattHrsATRAP.setObjects(
      *(("GEIST-MIB", "pow3ChKWattHrsA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChKWattHrsATRAP.setStatus(
        ""
    )

gstPow3ChVoltsATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11106)
)
gstPow3ChVoltsATRAP.setObjects(
      *(("GEIST-MIB", "pow3ChVoltsA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltsATRAP.setStatus(
        ""
    )

gstPow3ChVoltMaxATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11107)
)
gstPow3ChVoltMaxATRAP.setObjects(
      *(("GEIST-MIB", "pow3ChVoltMaxA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMaxATRAP.setStatus(
        ""
    )

gstPow3ChVoltMinATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11108)
)
gstPow3ChVoltMinATRAP.setObjects(
      *(("GEIST-MIB", "pow3ChVoltMinA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMinATRAP.setStatus(
        ""
    )

gstPow3ChVoltPeakATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11109)
)
gstPow3ChVoltPeakATRAP.setObjects(
      *(("GEIST-MIB", "pow3ChVoltPeakA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltPeakATRAP.setStatus(
        ""
    )

gstPow3ChDeciAmpsATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11110)
)
gstPow3ChDeciAmpsATRAP.setObjects(
      *(("GEIST-MIB", "pow3ChDeciAmpsA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChDeciAmpsATRAP.setStatus(
        ""
    )

gstPow3ChRealPowerATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11111)
)
gstPow3ChRealPowerATRAP.setObjects(
      *(("GEIST-MIB", "pow3ChRealPowerA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerATRAP.setStatus(
        ""
    )

gstPow3ChApparentPowerATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11112)
)
gstPow3ChApparentPowerATRAP.setObjects(
      *(("GEIST-MIB", "pow3ChApparentPowerA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChApparentPowerATRAP.setStatus(
        ""
    )

gstPow3ChPowerFactorATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11113)
)
gstPow3ChPowerFactorATRAP.setObjects(
      *(("GEIST-MIB", "pow3ChPowerFactorA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChPowerFactorATRAP.setStatus(
        ""
    )

gstPow3ChKWattHrsBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11114)
)
gstPow3ChKWattHrsBTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChKWattHrsB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChKWattHrsBTRAP.setStatus(
        ""
    )

gstPow3ChVoltsBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11115)
)
gstPow3ChVoltsBTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChVoltsB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltsBTRAP.setStatus(
        ""
    )

gstPow3ChVoltMaxBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11116)
)
gstPow3ChVoltMaxBTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChVoltMaxB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMaxBTRAP.setStatus(
        ""
    )

gstPow3ChVoltMinBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11117)
)
gstPow3ChVoltMinBTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChVoltMinB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMinBTRAP.setStatus(
        ""
    )

gstPow3ChVoltPeakBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11118)
)
gstPow3ChVoltPeakBTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChVoltPeakB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltPeakBTRAP.setStatus(
        ""
    )

gstPow3ChDeciAmpsBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11119)
)
gstPow3ChDeciAmpsBTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChDeciAmpsB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChDeciAmpsBTRAP.setStatus(
        ""
    )

gstPow3ChRealPowerBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11120)
)
gstPow3ChRealPowerBTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChRealPowerB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerBTRAP.setStatus(
        ""
    )

gstPow3ChApparentPowerBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11121)
)
gstPow3ChApparentPowerBTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChApparentPowerB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChApparentPowerBTRAP.setStatus(
        ""
    )

gstPow3ChPowerFactorBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11122)
)
gstPow3ChPowerFactorBTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChPowerFactorB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChPowerFactorBTRAP.setStatus(
        ""
    )

gstPow3ChKWattHrsCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11123)
)
gstPow3ChKWattHrsCTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChKWattHrsC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChKWattHrsCTRAP.setStatus(
        ""
    )

gstPow3ChVoltsCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11124)
)
gstPow3ChVoltsCTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChVoltsC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltsCTRAP.setStatus(
        ""
    )

gstPow3ChVoltMaxCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11125)
)
gstPow3ChVoltMaxCTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChVoltMaxC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMaxCTRAP.setStatus(
        ""
    )

gstPow3ChVoltMinCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11126)
)
gstPow3ChVoltMinCTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChVoltMinC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMinCTRAP.setStatus(
        ""
    )

gstPow3ChVoltPeakCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11127)
)
gstPow3ChVoltPeakCTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChVoltPeakC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltPeakCTRAP.setStatus(
        ""
    )

gstPow3ChDeciAmpsCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11128)
)
gstPow3ChDeciAmpsCTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChDeciAmpsC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChDeciAmpsCTRAP.setStatus(
        ""
    )

gstPow3ChRealPowerCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11129)
)
gstPow3ChRealPowerCTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChRealPowerC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerCTRAP.setStatus(
        ""
    )

gstPow3ChApparentPowerCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11130)
)
gstPow3ChApparentPowerCTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChApparentPowerC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChApparentPowerCTRAP.setStatus(
        ""
    )

gstPow3ChPowerFactorCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11131)
)
gstPow3ChPowerFactorCTRAP.setObjects(
      *(("GEIST-MIB", "pow3ChPowerFactorC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChPowerFactorCTRAP.setStatus(
        ""
    )

gstOutlet1StatusTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11205)
)
gstOutlet1StatusTRAP.setObjects(
      *(("GEIST-MIB", "outlet1Status"),
        ("GEIST-MIB", "outletName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstOutlet1StatusTRAP.setStatus(
        ""
    )

gstOutlet2StatusTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11206)
)
gstOutlet2StatusTRAP.setObjects(
      *(("GEIST-MIB", "outlet2Status"),
        ("GEIST-MIB", "outletName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstOutlet2StatusTRAP.setStatus(
        ""
    )

gstVsfcSetPointCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11305)
)
gstVsfcSetPointCTRAP.setObjects(
      *(("GEIST-MIB", "vsfcSetPointC"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcSetPointCTRAP.setStatus(
        ""
    )

gstVsfcIntTempCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11306)
)
gstVsfcIntTempCTRAP.setObjects(
      *(("GEIST-MIB", "vsfcIntTempC"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcIntTempCTRAP.setStatus(
        ""
    )

gstVsfcExt1TempCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11307)
)
gstVsfcExt1TempCTRAP.setObjects(
      *(("GEIST-MIB", "vsfcExt1TempC"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcExt1TempCTRAP.setStatus(
        ""
    )

gstVsfcExt2TempCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11308)
)
gstVsfcExt2TempCTRAP.setObjects(
      *(("GEIST-MIB", "vsfcExt2TempC"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcExt2TempCTRAP.setStatus(
        ""
    )

gstVsfcExt3TempCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11309)
)
gstVsfcExt3TempCTRAP.setObjects(
      *(("GEIST-MIB", "vsfcExt3TempC"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcExt3TempCTRAP.setStatus(
        ""
    )

gstVsfcExt4TempCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11310)
)
gstVsfcExt4TempCTRAP.setObjects(
      *(("GEIST-MIB", "vsfcExt4TempC"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcExt4TempCTRAP.setStatus(
        ""
    )

gstVsfcFanSpeedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11311)
)
gstVsfcFanSpeedTRAP.setObjects(
      *(("GEIST-MIB", "vsfcFanSpeed"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcFanSpeedTRAP.setStatus(
        ""
    )

gstCtrl3ChVoltsATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11405)
)
gstCtrl3ChVoltsATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChVoltsA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltsATRAP.setStatus(
        ""
    )

gstCtrl3ChVoltPeakATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11406)
)
gstCtrl3ChVoltPeakATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChVoltPeakA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltPeakATRAP.setStatus(
        ""
    )

gstCtrl3ChDeciAmpsATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11407)
)
gstCtrl3ChDeciAmpsATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChDeciAmpsA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsATRAP.setStatus(
        ""
    )

gstCtrl3ChDeciAmpsPeakATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11408)
)
gstCtrl3ChDeciAmpsPeakATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChDeciAmpsPeakA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsPeakATRAP.setStatus(
        ""
    )

gstCtrl3ChRealPowerATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11409)
)
gstCtrl3ChRealPowerATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChRealPowerA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChRealPowerATRAP.setStatus(
        ""
    )

gstCtrl3ChApparentPowerATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11410)
)
gstCtrl3ChApparentPowerATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChApparentPowerA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChApparentPowerATRAP.setStatus(
        ""
    )

gstCtrl3ChPowerFactorATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11411)
)
gstCtrl3ChPowerFactorATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChPowerFactorA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChPowerFactorATRAP.setStatus(
        ""
    )

gstCtrl3ChVoltsBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11412)
)
gstCtrl3ChVoltsBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChVoltsB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltsBTRAP.setStatus(
        ""
    )

gstCtrl3ChVoltPeakBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11413)
)
gstCtrl3ChVoltPeakBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChVoltPeakB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltPeakBTRAP.setStatus(
        ""
    )

gstCtrl3ChDeciAmpsBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11414)
)
gstCtrl3ChDeciAmpsBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChDeciAmpsB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsBTRAP.setStatus(
        ""
    )

gstCtrl3ChDeciAmpsPeakBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11415)
)
gstCtrl3ChDeciAmpsPeakBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChDeciAmpsPeakB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsPeakBTRAP.setStatus(
        ""
    )

gstCtrl3ChRealPowerBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11416)
)
gstCtrl3ChRealPowerBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChRealPowerB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChRealPowerBTRAP.setStatus(
        ""
    )

gstCtrl3ChApparentPowerBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11417)
)
gstCtrl3ChApparentPowerBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChApparentPowerB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChApparentPowerBTRAP.setStatus(
        ""
    )

gstCtrl3ChPowerFactorBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11418)
)
gstCtrl3ChPowerFactorBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChPowerFactorB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChPowerFactorBTRAP.setStatus(
        ""
    )

gstCtrl3ChVoltsCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11419)
)
gstCtrl3ChVoltsCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChVoltsC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltsCTRAP.setStatus(
        ""
    )

gstCtrl3ChVoltPeakCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11420)
)
gstCtrl3ChVoltPeakCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChVoltPeakC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltPeakCTRAP.setStatus(
        ""
    )

gstCtrl3ChDeciAmpsCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11421)
)
gstCtrl3ChDeciAmpsCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChDeciAmpsC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsCTRAP.setStatus(
        ""
    )

gstCtrl3ChDeciAmpsPeakCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11422)
)
gstCtrl3ChDeciAmpsPeakCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChDeciAmpsPeakC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsPeakCTRAP.setStatus(
        ""
    )

gstCtrl3ChRealPowerCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11423)
)
gstCtrl3ChRealPowerCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChRealPowerC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChRealPowerCTRAP.setStatus(
        ""
    )

gstCtrl3ChApparentPowerCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11424)
)
gstCtrl3ChApparentPowerCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChApparentPowerC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChApparentPowerCTRAP.setStatus(
        ""
    )

gstCtrl3ChPowerFactorCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11425)
)
gstCtrl3ChPowerFactorCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChPowerFactorC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChPowerFactorCTRAP.setStatus(
        ""
    )

gstCtrlGrpAmpsATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11505)
)
gstCtrlGrpAmpsATRAP.setObjects(
      *(("GEIST-MIB", "ctrlGrpAmpsA"),
        ("GEIST-MIB", "ctrlGrpAmpsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsATRAP.setStatus(
        ""
    )

gstCtrlGrpAmpsBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11506)
)
gstCtrlGrpAmpsBTRAP.setObjects(
      *(("GEIST-MIB", "ctrlGrpAmpsB"),
        ("GEIST-MIB", "ctrlGrpAmpsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsBTRAP.setStatus(
        ""
    )

gstCtrlGrpAmpsCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11507)
)
gstCtrlGrpAmpsCTRAP.setObjects(
      *(("GEIST-MIB", "ctrlGrpAmpsC"),
        ("GEIST-MIB", "ctrlGrpAmpsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsCTRAP.setStatus(
        ""
    )

gstCtrlGrpAmpsDTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11508)
)
gstCtrlGrpAmpsDTRAP.setObjects(
      *(("GEIST-MIB", "ctrlGrpAmpsD"),
        ("GEIST-MIB", "ctrlGrpAmpsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsDTRAP.setStatus(
        ""
    )

gstCtrlGrpAmpsETRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11509)
)
gstCtrlGrpAmpsETRAP.setObjects(
      *(("GEIST-MIB", "ctrlGrpAmpsE"),
        ("GEIST-MIB", "ctrlGrpAmpsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsETRAP.setStatus(
        ""
    )

gstCtrlGrpAmpsFTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11510)
)
gstCtrlGrpAmpsFTRAP.setObjects(
      *(("GEIST-MIB", "ctrlGrpAmpsF"),
        ("GEIST-MIB", "ctrlGrpAmpsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsFTRAP.setStatus(
        ""
    )

gstDewPointSensorDewPointTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11705)
)
gstDewPointSensorDewPointTRAP.setObjects(
      *(("GEIST-MIB", "dewPointSensorDewPoint"),
        ("GEIST-MIB", "dewPointSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorDewPointTRAP.setStatus(
        ""
    )

gstDewPointSensorTempCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11706)
)
gstDewPointSensorTempCTRAP.setObjects(
      *(("GEIST-MIB", "dewPointSensorTempC"),
        ("GEIST-MIB", "dewPointSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorTempCTRAP.setStatus(
        ""
    )

gstDewPointSensorHumidityTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11707)
)
gstDewPointSensorHumidityTRAP.setObjects(
      *(("GEIST-MIB", "dewPointSensorHumidity"),
        ("GEIST-MIB", "dewPointSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorHumidityTRAP.setStatus(
        ""
    )

gstDigitalSensorDigitalTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11805)
)
gstDigitalSensorDigitalTRAP.setObjects(
      *(("GEIST-MIB", "digitalSensorDigital"),
        ("GEIST-MIB", "digitalSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDigitalSensorDigitalTRAP.setStatus(
        ""
    )

gstDstsVoltsATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11905)
)
gstDstsVoltsATRAP.setObjects(
      *(("GEIST-MIB", "dstsVoltsA"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsVoltsATRAP.setStatus(
        ""
    )

gstDstsAmpsATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11906)
)
gstDstsAmpsATRAP.setObjects(
      *(("GEIST-MIB", "dstsAmpsA"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsAmpsATRAP.setStatus(
        ""
    )

gstDstsVoltsBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11907)
)
gstDstsVoltsBTRAP.setObjects(
      *(("GEIST-MIB", "dstsVoltsB"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsVoltsBTRAP.setStatus(
        ""
    )

gstDstsAmpsBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11908)
)
gstDstsAmpsBTRAP.setObjects(
      *(("GEIST-MIB", "dstsAmpsB"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsAmpsBTRAP.setStatus(
        ""
    )

gstDstsSourceAActiveTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11909)
)
gstDstsSourceAActiveTRAP.setObjects(
      *(("GEIST-MIB", "dstsSourceAActive"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsSourceAActiveTRAP.setStatus(
        ""
    )

gstDstsSourceBActiveTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11910)
)
gstDstsSourceBActiveTRAP.setObjects(
      *(("GEIST-MIB", "dstsSourceBActive"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsSourceBActiveTRAP.setStatus(
        ""
    )

gstDstsPowerStatusATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11911)
)
gstDstsPowerStatusATRAP.setObjects(
      *(("GEIST-MIB", "dstsPowerStatusA"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsPowerStatusATRAP.setStatus(
        ""
    )

gstDstsPowerStatusBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11912)
)
gstDstsPowerStatusBTRAP.setObjects(
      *(("GEIST-MIB", "dstsPowerStatusB"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsPowerStatusBTRAP.setStatus(
        ""
    )

gstDstsSourceATempCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11913)
)
gstDstsSourceATempCTRAP.setObjects(
      *(("GEIST-MIB", "dstsSourceATempC"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsSourceATempCTRAP.setStatus(
        ""
    )

gstDstsSourceBTempCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 11914)
)
gstDstsSourceBTempCTRAP.setObjects(
      *(("GEIST-MIB", "dstsSourceBTempC"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsSourceBTempCTRAP.setStatus(
        ""
    )

gstCpmSensorStatusTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12005)
)
gstCpmSensorStatusTRAP.setObjects(
      *(("GEIST-MIB", "cpmSensorStatus"),
        ("GEIST-MIB", "cpmSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCpmSensorStatusTRAP.setStatus(
        ""
    )

gstSmokeAlarmStatusTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12105)
)
gstSmokeAlarmStatusTRAP.setObjects(
      *(("GEIST-MIB", "smokeAlarmStatus"),
        ("GEIST-MIB", "smokeAlarmName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstSmokeAlarmStatusTRAP.setStatus(
        ""
    )

gstNeg48VdcSensorVoltageTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12205)
)
gstNeg48VdcSensorVoltageTRAP.setObjects(
      *(("GEIST-MIB", "neg48VdcSensorVoltage"),
        ("GEIST-MIB", "neg48VdcSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstNeg48VdcSensorVoltageTRAP.setStatus(
        ""
    )

gstPos30VdcSensorVoltageTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12305)
)
gstPos30VdcSensorVoltageTRAP.setObjects(
      *(("GEIST-MIB", "pos30VdcSensorVoltage"),
        ("GEIST-MIB", "pos30VdcSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPos30VdcSensorVoltageTRAP.setStatus(
        ""
    )

gstAnalogSensorAnalogTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12405)
)
gstAnalogSensorAnalogTRAP.setObjects(
      *(("GEIST-MIB", "analogSensorAnalog"),
        ("GEIST-MIB", "analogSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstAnalogSensorAnalogTRAP.setStatus(
        ""
    )

gstCtrl3ChIECKWattHrsATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12505)
)
gstCtrl3ChIECKWattHrsATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECKWattHrsA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECKWattHrsATRAP.setStatus(
        ""
    )

gstCtrl3ChIECVoltsATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12506)
)
gstCtrl3ChIECVoltsATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECVoltsA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltsATRAP.setStatus(
        ""
    )

gstCtrl3ChIECVoltPeakATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12507)
)
gstCtrl3ChIECVoltPeakATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECVoltPeakA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltPeakATRAP.setStatus(
        ""
    )

gstCtrl3ChIECDeciAmpsATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12508)
)
gstCtrl3ChIECDeciAmpsATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECDeciAmpsA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsATRAP.setStatus(
        ""
    )

gstCtrl3ChIECDeciAmpsPeakATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12509)
)
gstCtrl3ChIECDeciAmpsPeakATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECDeciAmpsPeakA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsPeakATRAP.setStatus(
        ""
    )

gstCtrl3ChIECRealPowerATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12510)
)
gstCtrl3ChIECRealPowerATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECRealPowerA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerATRAP.setStatus(
        ""
    )

gstCtrl3ChIECApparentPowerATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12511)
)
gstCtrl3ChIECApparentPowerATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECApparentPowerA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECApparentPowerATRAP.setStatus(
        ""
    )

gstCtrl3ChIECPowerFactorATRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12512)
)
gstCtrl3ChIECPowerFactorATRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECPowerFactorA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECPowerFactorATRAP.setStatus(
        ""
    )

gstCtrl3ChIECKWattHrsBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12513)
)
gstCtrl3ChIECKWattHrsBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECKWattHrsB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECKWattHrsBTRAP.setStatus(
        ""
    )

gstCtrl3ChIECVoltsBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12514)
)
gstCtrl3ChIECVoltsBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECVoltsB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltsBTRAP.setStatus(
        ""
    )

gstCtrl3ChIECVoltPeakBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12515)
)
gstCtrl3ChIECVoltPeakBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECVoltPeakB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltPeakBTRAP.setStatus(
        ""
    )

gstCtrl3ChIECDeciAmpsBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12516)
)
gstCtrl3ChIECDeciAmpsBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECDeciAmpsB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsBTRAP.setStatus(
        ""
    )

gstCtrl3ChIECDeciAmpsPeakBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12517)
)
gstCtrl3ChIECDeciAmpsPeakBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECDeciAmpsPeakB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsPeakBTRAP.setStatus(
        ""
    )

gstCtrl3ChIECRealPowerBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12518)
)
gstCtrl3ChIECRealPowerBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECRealPowerB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerBTRAP.setStatus(
        ""
    )

gstCtrl3ChIECApparentPowerBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12519)
)
gstCtrl3ChIECApparentPowerBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECApparentPowerB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECApparentPowerBTRAP.setStatus(
        ""
    )

gstCtrl3ChIECPowerFactorBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12520)
)
gstCtrl3ChIECPowerFactorBTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECPowerFactorB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECPowerFactorBTRAP.setStatus(
        ""
    )

gstCtrl3ChIECKWattHrsCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12521)
)
gstCtrl3ChIECKWattHrsCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECKWattHrsC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECKWattHrsCTRAP.setStatus(
        ""
    )

gstCtrl3ChIECVoltsCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12522)
)
gstCtrl3ChIECVoltsCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECVoltsC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltsCTRAP.setStatus(
        ""
    )

gstCtrl3ChIECVoltPeakCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12523)
)
gstCtrl3ChIECVoltPeakCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECVoltPeakC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltPeakCTRAP.setStatus(
        ""
    )

gstCtrl3ChIECDeciAmpsCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12524)
)
gstCtrl3ChIECDeciAmpsCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECDeciAmpsC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsCTRAP.setStatus(
        ""
    )

gstCtrl3ChIECDeciAmpsPeakCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12525)
)
gstCtrl3ChIECDeciAmpsPeakCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECDeciAmpsPeakC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsPeakCTRAP.setStatus(
        ""
    )

gstCtrl3ChIECRealPowerCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12526)
)
gstCtrl3ChIECRealPowerCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECRealPowerC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerCTRAP.setStatus(
        ""
    )

gstCtrl3ChIECApparentPowerCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12527)
)
gstCtrl3ChIECApparentPowerCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECApparentPowerC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECApparentPowerCTRAP.setStatus(
        ""
    )

gstCtrl3ChIECPowerFactorCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12528)
)
gstCtrl3ChIECPowerFactorCTRAP.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECPowerFactorC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECPowerFactorCTRAP.setStatus(
        ""
    )

gstAirSpeedSwitchSensorAirSpeedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 12605)
)
gstAirSpeedSwitchSensorAirSpeedTRAP.setObjects(
      *(("GEIST-MIB", "airSpeedSwitchSensorAirSpeed"),
        ("GEIST-MIB", "airSpeedSwitchSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstAirSpeedSwitchSensorAirSpeedTRAP.setStatus(
        ""
    )

gstClimateTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20205)
)
gstClimateTempCCLEAR.setObjects(
      *(("GEIST-MIB", "climateTempC"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateTempCCLEAR.setStatus(
        ""
    )

gstClimateHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20206)
)
gstClimateHumidityCLEAR.setObjects(
      *(("GEIST-MIB", "climateHumidity"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateHumidityCLEAR.setStatus(
        ""
    )

gstClimateAirflowCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20207)
)
gstClimateAirflowCLEAR.setObjects(
      *(("GEIST-MIB", "climateAirflow"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateAirflowCLEAR.setStatus(
        ""
    )

gstClimateLightCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20208)
)
gstClimateLightCLEAR.setObjects(
      *(("GEIST-MIB", "climateLight"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateLightCLEAR.setStatus(
        ""
    )

gstClimateSoundCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20209)
)
gstClimateSoundCLEAR.setObjects(
      *(("GEIST-MIB", "climateSound"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateSoundCLEAR.setStatus(
        ""
    )

gstClimateIO1CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20210)
)
gstClimateIO1CLEAR.setObjects(
      *(("GEIST-MIB", "climateIO1"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateIO1CLEAR.setStatus(
        ""
    )

gstClimateIO2CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20211)
)
gstClimateIO2CLEAR.setObjects(
      *(("GEIST-MIB", "climateIO2"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateIO2CLEAR.setStatus(
        ""
    )

gstClimateIO3CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20212)
)
gstClimateIO3CLEAR.setObjects(
      *(("GEIST-MIB", "climateIO3"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateIO3CLEAR.setStatus(
        ""
    )

gstClimateVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20213)
)
gstClimateVoltsCLEAR.setObjects(
      *(("GEIST-MIB", "climateVolts"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateVoltsCLEAR.setStatus(
        ""
    )

gstClimateVoltPeakCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20214)
)
gstClimateVoltPeakCLEAR.setObjects(
      *(("GEIST-MIB", "climateVoltPeak"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateVoltPeakCLEAR.setStatus(
        ""
    )

gstClimateDeciAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20215)
)
gstClimateDeciAmpsACLEAR.setObjects(
      *(("GEIST-MIB", "climateDeciAmpsA"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpsACLEAR.setStatus(
        ""
    )

gstClimateAmpPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20216)
)
gstClimateAmpPeakACLEAR.setObjects(
      *(("GEIST-MIB", "climateAmpPeakA"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateAmpPeakACLEAR.setStatus(
        ""
    )

gstClimateRealPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20217)
)
gstClimateRealPowerACLEAR.setObjects(
      *(("GEIST-MIB", "climateRealPowerA"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateRealPowerACLEAR.setStatus(
        ""
    )

gstClimateApparentPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20218)
)
gstClimateApparentPowerACLEAR.setObjects(
      *(("GEIST-MIB", "climateApparentPowerA"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateApparentPowerACLEAR.setStatus(
        ""
    )

gstClimatePowerFactorACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20219)
)
gstClimatePowerFactorACLEAR.setObjects(
      *(("GEIST-MIB", "climatePowerFactorA"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimatePowerFactorACLEAR.setStatus(
        ""
    )

gstClimateDeciAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20220)
)
gstClimateDeciAmpsBCLEAR.setObjects(
      *(("GEIST-MIB", "climateDeciAmpsB"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpsBCLEAR.setStatus(
        ""
    )

gstClimateDeciAmpPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20221)
)
gstClimateDeciAmpPeakBCLEAR.setObjects(
      *(("GEIST-MIB", "climateDeciAmpPeakB"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpPeakBCLEAR.setStatus(
        ""
    )

gstClimateRealPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20222)
)
gstClimateRealPowerBCLEAR.setObjects(
      *(("GEIST-MIB", "climateRealPowerB"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateRealPowerBCLEAR.setStatus(
        ""
    )

gstClimateApparentPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20223)
)
gstClimateApparentPowerBCLEAR.setObjects(
      *(("GEIST-MIB", "climateApparentPowerB"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateApparentPowerBCLEAR.setStatus(
        ""
    )

gstClimatePowerFactorBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20224)
)
gstClimatePowerFactorBCLEAR.setObjects(
      *(("GEIST-MIB", "climatePowerFactorB"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimatePowerFactorBCLEAR.setStatus(
        ""
    )

gstClimateDeciAmpsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20225)
)
gstClimateDeciAmpsCCLEAR.setObjects(
      *(("GEIST-MIB", "climateDeciAmpsC"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpsCCLEAR.setStatus(
        ""
    )

gstClimateDeciAmpPeakCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20226)
)
gstClimateDeciAmpPeakCCLEAR.setObjects(
      *(("GEIST-MIB", "climateDeciAmpPeakC"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpPeakCCLEAR.setStatus(
        ""
    )

gstClimateRealPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20227)
)
gstClimateRealPowerCCLEAR.setObjects(
      *(("GEIST-MIB", "climateRealPowerC"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateRealPowerCCLEAR.setStatus(
        ""
    )

gstClimateApparentPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20228)
)
gstClimateApparentPowerCCLEAR.setObjects(
      *(("GEIST-MIB", "climateApparentPowerC"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimateApparentPowerCCLEAR.setStatus(
        ""
    )

gstClimatePowerFactorCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20229)
)
gstClimatePowerFactorCCLEAR.setObjects(
      *(("GEIST-MIB", "climatePowerFactorC"),
        ("GEIST-MIB", "climateName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstClimatePowerFactorCCLEAR.setStatus(
        ""
    )

gstPowMonKWattHrsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20305)
)
gstPowMonKWattHrsCLEAR.setObjects(
      *(("GEIST-MIB", "powMonKWattHrs"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonKWattHrsCLEAR.setStatus(
        ""
    )

gstPowMonVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20306)
)
gstPowMonVoltsCLEAR.setObjects(
      *(("GEIST-MIB", "powMonVolts"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltsCLEAR.setStatus(
        ""
    )

gstPowMonVoltMaxCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20307)
)
gstPowMonVoltMaxCLEAR.setObjects(
      *(("GEIST-MIB", "powMonVoltMax"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltMaxCLEAR.setStatus(
        ""
    )

gstPowMonVoltMinCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20308)
)
gstPowMonVoltMinCLEAR.setObjects(
      *(("GEIST-MIB", "powMonVoltMin"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltMinCLEAR.setStatus(
        ""
    )

gstPowMonVoltPeakCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20309)
)
gstPowMonVoltPeakCLEAR.setObjects(
      *(("GEIST-MIB", "powMonVoltPeak"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltPeakCLEAR.setStatus(
        ""
    )

gstPowMonDeciAmpsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20310)
)
gstPowMonDeciAmpsCLEAR.setObjects(
      *(("GEIST-MIB", "powMonDeciAmps"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonDeciAmpsCLEAR.setStatus(
        ""
    )

gstPowMonRealPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20311)
)
gstPowMonRealPowerCLEAR.setObjects(
      *(("GEIST-MIB", "powMonRealPower"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonRealPowerCLEAR.setStatus(
        ""
    )

gstPowMonApparentPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20312)
)
gstPowMonApparentPowerCLEAR.setObjects(
      *(("GEIST-MIB", "powMonApparentPower"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonApparentPowerCLEAR.setStatus(
        ""
    )

gstPowMonPowerFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20313)
)
gstPowMonPowerFactorCLEAR.setObjects(
      *(("GEIST-MIB", "powMonPowerFactor"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonPowerFactorCLEAR.setStatus(
        ""
    )

gstPowMonDeciAmpsOutlet1CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20314)
)
gstPowMonDeciAmpsOutlet1CLEAR.setObjects(
      *(("GEIST-MIB", "powMonDeciAmpsOutlet1"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonDeciAmpsOutlet1CLEAR.setStatus(
        ""
    )

gstPowMonDeciAmpsOutlet2CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20315)
)
gstPowMonDeciAmpsOutlet2CLEAR.setObjects(
      *(("GEIST-MIB", "powMonDeciAmpsOutlet2"),
        ("GEIST-MIB", "powMonName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowMonDeciAmpsOutlet2CLEAR.setStatus(
        ""
    )

gstTempSensorTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20405)
)
gstTempSensorTempCCLEAR.setObjects(
      *(("GEIST-MIB", "tempSensorTempC"),
        ("GEIST-MIB", "tempSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstTempSensorTempCCLEAR.setStatus(
        ""
    )

gstAirFlowSensorFlowCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20505)
)
gstAirFlowSensorFlowCLEAR.setObjects(
      *(("GEIST-MIB", "airFlowSensorFlow"),
        ("GEIST-MIB", "airFlowSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorFlowCLEAR.setStatus(
        ""
    )

gstAirFlowSensorTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20506)
)
gstAirFlowSensorTempCCLEAR.setObjects(
      *(("GEIST-MIB", "airFlowSensorTempC"),
        ("GEIST-MIB", "airFlowSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorTempCCLEAR.setStatus(
        ""
    )

gstAirFlowSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20507)
)
gstAirFlowSensorHumidityCLEAR.setObjects(
      *(("GEIST-MIB", "airFlowSensorHumidity"),
        ("GEIST-MIB", "airFlowSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorHumidityCLEAR.setStatus(
        ""
    )

gstAirFlowSensorDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20508)
)
gstAirFlowSensorDewPointCLEAR.setObjects(
      *(("GEIST-MIB", "airFlowSensorDewPoint"),
        ("GEIST-MIB", "airFlowSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorDewPointCLEAR.setStatus(
        ""
    )

gstPowerVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20605)
)
gstPowerVoltsCLEAR.setObjects(
      *(("GEIST-MIB", "powerVolts"),
        ("GEIST-MIB", "powerName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowerVoltsCLEAR.setStatus(
        ""
    )

gstPowerDeciAmpsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20606)
)
gstPowerDeciAmpsCLEAR.setObjects(
      *(("GEIST-MIB", "powerDeciAmps"),
        ("GEIST-MIB", "powerName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowerDeciAmpsCLEAR.setStatus(
        ""
    )

gstPowerRealPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20607)
)
gstPowerRealPowerCLEAR.setObjects(
      *(("GEIST-MIB", "powerRealPower"),
        ("GEIST-MIB", "powerName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowerRealPowerCLEAR.setStatus(
        ""
    )

gstPowerApparentPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20608)
)
gstPowerApparentPowerCLEAR.setObjects(
      *(("GEIST-MIB", "powerApparentPower"),
        ("GEIST-MIB", "powerName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowerApparentPowerCLEAR.setStatus(
        ""
    )

gstPowerPowerFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20609)
)
gstPowerPowerFactorCLEAR.setObjects(
      *(("GEIST-MIB", "powerPowerFactor"),
        ("GEIST-MIB", "powerName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPowerPowerFactorCLEAR.setStatus(
        ""
    )

gstDoorSensorStatusCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20705)
)
gstDoorSensorStatusCLEAR.setObjects(
      *(("GEIST-MIB", "doorSensorStatus"),
        ("GEIST-MIB", "doorSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDoorSensorStatusCLEAR.setStatus(
        ""
    )

gstWaterSensorDampnessCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20805)
)
gstWaterSensorDampnessCLEAR.setObjects(
      *(("GEIST-MIB", "waterSensorDampness"),
        ("GEIST-MIB", "waterSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstWaterSensorDampnessCLEAR.setStatus(
        ""
    )

gstCurrentMonitorDeciAmpsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 20905)
)
gstCurrentMonitorDeciAmpsCLEAR.setObjects(
      *(("GEIST-MIB", "currentMonitorDeciAmps"),
        ("GEIST-MIB", "currentMonitorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCurrentMonitorDeciAmpsCLEAR.setStatus(
        ""
    )

gstMillivoltMonitorMVCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21005)
)
gstMillivoltMonitorMVCLEAR.setObjects(
      *(("GEIST-MIB", "millivoltMonitorMV"),
        ("GEIST-MIB", "millivoltMonitorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstMillivoltMonitorMVCLEAR.setStatus(
        ""
    )

gstPow3ChKWattHrsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21105)
)
gstPow3ChKWattHrsACLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChKWattHrsA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChKWattHrsACLEAR.setStatus(
        ""
    )

gstPow3ChVoltsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21106)
)
gstPow3ChVoltsACLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChVoltsA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltsACLEAR.setStatus(
        ""
    )

gstPow3ChVoltMaxACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21107)
)
gstPow3ChVoltMaxACLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChVoltMaxA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMaxACLEAR.setStatus(
        ""
    )

gstPow3ChVoltMinACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21108)
)
gstPow3ChVoltMinACLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChVoltMinA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMinACLEAR.setStatus(
        ""
    )

gstPow3ChVoltPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21109)
)
gstPow3ChVoltPeakACLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChVoltPeakA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltPeakACLEAR.setStatus(
        ""
    )

gstPow3ChDeciAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21110)
)
gstPow3ChDeciAmpsACLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChDeciAmpsA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChDeciAmpsACLEAR.setStatus(
        ""
    )

gstPow3ChRealPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21111)
)
gstPow3ChRealPowerACLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChRealPowerA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerACLEAR.setStatus(
        ""
    )

gstPow3ChApparentPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21112)
)
gstPow3ChApparentPowerACLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChApparentPowerA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChApparentPowerACLEAR.setStatus(
        ""
    )

gstPow3ChPowerFactorACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21113)
)
gstPow3ChPowerFactorACLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChPowerFactorA"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChPowerFactorACLEAR.setStatus(
        ""
    )

gstPow3ChKWattHrsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21114)
)
gstPow3ChKWattHrsBCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChKWattHrsB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChKWattHrsBCLEAR.setStatus(
        ""
    )

gstPow3ChVoltsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21115)
)
gstPow3ChVoltsBCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChVoltsB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltsBCLEAR.setStatus(
        ""
    )

gstPow3ChVoltMaxBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21116)
)
gstPow3ChVoltMaxBCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChVoltMaxB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMaxBCLEAR.setStatus(
        ""
    )

gstPow3ChVoltMinBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21117)
)
gstPow3ChVoltMinBCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChVoltMinB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMinBCLEAR.setStatus(
        ""
    )

gstPow3ChVoltPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21118)
)
gstPow3ChVoltPeakBCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChVoltPeakB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltPeakBCLEAR.setStatus(
        ""
    )

gstPow3ChDeciAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21119)
)
gstPow3ChDeciAmpsBCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChDeciAmpsB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChDeciAmpsBCLEAR.setStatus(
        ""
    )

gstPow3ChRealPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21120)
)
gstPow3ChRealPowerBCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChRealPowerB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerBCLEAR.setStatus(
        ""
    )

gstPow3ChApparentPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21121)
)
gstPow3ChApparentPowerBCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChApparentPowerB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChApparentPowerBCLEAR.setStatus(
        ""
    )

gstPow3ChPowerFactorBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21122)
)
gstPow3ChPowerFactorBCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChPowerFactorB"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChPowerFactorBCLEAR.setStatus(
        ""
    )

gstPow3ChKWattHrsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21123)
)
gstPow3ChKWattHrsCCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChKWattHrsC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChKWattHrsCCLEAR.setStatus(
        ""
    )

gstPow3ChVoltsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21124)
)
gstPow3ChVoltsCCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChVoltsC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltsCCLEAR.setStatus(
        ""
    )

gstPow3ChVoltMaxCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21125)
)
gstPow3ChVoltMaxCCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChVoltMaxC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMaxCCLEAR.setStatus(
        ""
    )

gstPow3ChVoltMinCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21126)
)
gstPow3ChVoltMinCCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChVoltMinC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMinCCLEAR.setStatus(
        ""
    )

gstPow3ChVoltPeakCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21127)
)
gstPow3ChVoltPeakCCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChVoltPeakC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltPeakCCLEAR.setStatus(
        ""
    )

gstPow3ChDeciAmpsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21128)
)
gstPow3ChDeciAmpsCCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChDeciAmpsC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChDeciAmpsCCLEAR.setStatus(
        ""
    )

gstPow3ChRealPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21129)
)
gstPow3ChRealPowerCCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChRealPowerC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerCCLEAR.setStatus(
        ""
    )

gstPow3ChApparentPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21130)
)
gstPow3ChApparentPowerCCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChApparentPowerC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChApparentPowerCCLEAR.setStatus(
        ""
    )

gstPow3ChPowerFactorCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21131)
)
gstPow3ChPowerFactorCCLEAR.setObjects(
      *(("GEIST-MIB", "pow3ChPowerFactorC"),
        ("GEIST-MIB", "pow3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPow3ChPowerFactorCCLEAR.setStatus(
        ""
    )

gstOutlet1StatusCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21205)
)
gstOutlet1StatusCLEAR.setObjects(
      *(("GEIST-MIB", "outlet1Status"),
        ("GEIST-MIB", "outletName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstOutlet1StatusCLEAR.setStatus(
        ""
    )

gstOutlet2StatusCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21206)
)
gstOutlet2StatusCLEAR.setObjects(
      *(("GEIST-MIB", "outlet2Status"),
        ("GEIST-MIB", "outletName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstOutlet2StatusCLEAR.setStatus(
        ""
    )

gstVsfcSetPointCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21305)
)
gstVsfcSetPointCCLEAR.setObjects(
      *(("GEIST-MIB", "vsfcSetPointC"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcSetPointCCLEAR.setStatus(
        ""
    )

gstVsfcIntTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21306)
)
gstVsfcIntTempCCLEAR.setObjects(
      *(("GEIST-MIB", "vsfcIntTempC"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcIntTempCCLEAR.setStatus(
        ""
    )

gstVsfcExt1TempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21307)
)
gstVsfcExt1TempCCLEAR.setObjects(
      *(("GEIST-MIB", "vsfcExt1TempC"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcExt1TempCCLEAR.setStatus(
        ""
    )

gstVsfcExt2TempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21308)
)
gstVsfcExt2TempCCLEAR.setObjects(
      *(("GEIST-MIB", "vsfcExt2TempC"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcExt2TempCCLEAR.setStatus(
        ""
    )

gstVsfcExt3TempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21309)
)
gstVsfcExt3TempCCLEAR.setObjects(
      *(("GEIST-MIB", "vsfcExt3TempC"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcExt3TempCCLEAR.setStatus(
        ""
    )

gstVsfcExt4TempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21310)
)
gstVsfcExt4TempCCLEAR.setObjects(
      *(("GEIST-MIB", "vsfcExt4TempC"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcExt4TempCCLEAR.setStatus(
        ""
    )

gstVsfcFanSpeedCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21311)
)
gstVsfcFanSpeedCLEAR.setObjects(
      *(("GEIST-MIB", "vsfcFanSpeed"),
        ("GEIST-MIB", "vsfcName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstVsfcFanSpeedCLEAR.setStatus(
        ""
    )

gstCtrl3ChVoltsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21405)
)
gstCtrl3ChVoltsACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChVoltsA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltsACLEAR.setStatus(
        ""
    )

gstCtrl3ChVoltPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21406)
)
gstCtrl3ChVoltPeakACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChVoltPeakA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltPeakACLEAR.setStatus(
        ""
    )

gstCtrl3ChDeciAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21407)
)
gstCtrl3ChDeciAmpsACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChDeciAmpsA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsACLEAR.setStatus(
        ""
    )

gstCtrl3ChDeciAmpsPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21408)
)
gstCtrl3ChDeciAmpsPeakACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChDeciAmpsPeakA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsPeakACLEAR.setStatus(
        ""
    )

gstCtrl3ChRealPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21409)
)
gstCtrl3ChRealPowerACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChRealPowerA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChRealPowerACLEAR.setStatus(
        ""
    )

gstCtrl3ChApparentPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21410)
)
gstCtrl3ChApparentPowerACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChApparentPowerA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChApparentPowerACLEAR.setStatus(
        ""
    )

gstCtrl3ChPowerFactorACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21411)
)
gstCtrl3ChPowerFactorACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChPowerFactorA"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChPowerFactorACLEAR.setStatus(
        ""
    )

gstCtrl3ChVoltsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21412)
)
gstCtrl3ChVoltsBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChVoltsB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltsBCLEAR.setStatus(
        ""
    )

gstCtrl3ChVoltPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21413)
)
gstCtrl3ChVoltPeakBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChVoltPeakB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltPeakBCLEAR.setStatus(
        ""
    )

gstCtrl3ChDeciAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21414)
)
gstCtrl3ChDeciAmpsBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChDeciAmpsB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsBCLEAR.setStatus(
        ""
    )

gstCtrl3ChDeciAmpsPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21415)
)
gstCtrl3ChDeciAmpsPeakBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChDeciAmpsPeakB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsPeakBCLEAR.setStatus(
        ""
    )

gstCtrl3ChRealPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21416)
)
gstCtrl3ChRealPowerBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChRealPowerB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChRealPowerBCLEAR.setStatus(
        ""
    )

gstCtrl3ChApparentPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21417)
)
gstCtrl3ChApparentPowerBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChApparentPowerB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChApparentPowerBCLEAR.setStatus(
        ""
    )

gstCtrl3ChPowerFactorBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21418)
)
gstCtrl3ChPowerFactorBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChPowerFactorB"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChPowerFactorBCLEAR.setStatus(
        ""
    )

gstCtrl3ChVoltsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21419)
)
gstCtrl3ChVoltsCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChVoltsC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltsCCLEAR.setStatus(
        ""
    )

gstCtrl3ChVoltPeakCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21420)
)
gstCtrl3ChVoltPeakCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChVoltPeakC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltPeakCCLEAR.setStatus(
        ""
    )

gstCtrl3ChDeciAmpsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21421)
)
gstCtrl3ChDeciAmpsCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChDeciAmpsC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsCCLEAR.setStatus(
        ""
    )

gstCtrl3ChDeciAmpsPeakCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21422)
)
gstCtrl3ChDeciAmpsPeakCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChDeciAmpsPeakC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsPeakCCLEAR.setStatus(
        ""
    )

gstCtrl3ChRealPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21423)
)
gstCtrl3ChRealPowerCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChRealPowerC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChRealPowerCCLEAR.setStatus(
        ""
    )

gstCtrl3ChApparentPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21424)
)
gstCtrl3ChApparentPowerCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChApparentPowerC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChApparentPowerCCLEAR.setStatus(
        ""
    )

gstCtrl3ChPowerFactorCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21425)
)
gstCtrl3ChPowerFactorCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChPowerFactorC"),
        ("GEIST-MIB", "ctrl3ChName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChPowerFactorCCLEAR.setStatus(
        ""
    )

gstCtrlGrpAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21505)
)
gstCtrlGrpAmpsACLEAR.setObjects(
      *(("GEIST-MIB", "ctrlGrpAmpsA"),
        ("GEIST-MIB", "ctrlGrpAmpsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsACLEAR.setStatus(
        ""
    )

gstCtrlGrpAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21506)
)
gstCtrlGrpAmpsBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrlGrpAmpsB"),
        ("GEIST-MIB", "ctrlGrpAmpsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsBCLEAR.setStatus(
        ""
    )

gstCtrlGrpAmpsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21507)
)
gstCtrlGrpAmpsCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrlGrpAmpsC"),
        ("GEIST-MIB", "ctrlGrpAmpsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsCCLEAR.setStatus(
        ""
    )

gstCtrlGrpAmpsDCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21508)
)
gstCtrlGrpAmpsDCLEAR.setObjects(
      *(("GEIST-MIB", "ctrlGrpAmpsD"),
        ("GEIST-MIB", "ctrlGrpAmpsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsDCLEAR.setStatus(
        ""
    )

gstCtrlGrpAmpsECLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21509)
)
gstCtrlGrpAmpsECLEAR.setObjects(
      *(("GEIST-MIB", "ctrlGrpAmpsE"),
        ("GEIST-MIB", "ctrlGrpAmpsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsECLEAR.setStatus(
        ""
    )

gstCtrlGrpAmpsFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21510)
)
gstCtrlGrpAmpsFCLEAR.setObjects(
      *(("GEIST-MIB", "ctrlGrpAmpsF"),
        ("GEIST-MIB", "ctrlGrpAmpsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsFCLEAR.setStatus(
        ""
    )

gstDewPointSensorDewPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21705)
)
gstDewPointSensorDewPointCLEAR.setObjects(
      *(("GEIST-MIB", "dewPointSensorDewPoint"),
        ("GEIST-MIB", "dewPointSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorDewPointCLEAR.setStatus(
        ""
    )

gstDewPointSensorTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21706)
)
gstDewPointSensorTempCCLEAR.setObjects(
      *(("GEIST-MIB", "dewPointSensorTempC"),
        ("GEIST-MIB", "dewPointSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorTempCCLEAR.setStatus(
        ""
    )

gstDewPointSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21707)
)
gstDewPointSensorHumidityCLEAR.setObjects(
      *(("GEIST-MIB", "dewPointSensorHumidity"),
        ("GEIST-MIB", "dewPointSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorHumidityCLEAR.setStatus(
        ""
    )

gstDigitalSensorDigitalCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21805)
)
gstDigitalSensorDigitalCLEAR.setObjects(
      *(("GEIST-MIB", "digitalSensorDigital"),
        ("GEIST-MIB", "digitalSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDigitalSensorDigitalCLEAR.setStatus(
        ""
    )

gstDstsVoltsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21905)
)
gstDstsVoltsACLEAR.setObjects(
      *(("GEIST-MIB", "dstsVoltsA"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsVoltsACLEAR.setStatus(
        ""
    )

gstDstsAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21906)
)
gstDstsAmpsACLEAR.setObjects(
      *(("GEIST-MIB", "dstsAmpsA"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsAmpsACLEAR.setStatus(
        ""
    )

gstDstsVoltsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21907)
)
gstDstsVoltsBCLEAR.setObjects(
      *(("GEIST-MIB", "dstsVoltsB"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsVoltsBCLEAR.setStatus(
        ""
    )

gstDstsAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21908)
)
gstDstsAmpsBCLEAR.setObjects(
      *(("GEIST-MIB", "dstsAmpsB"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsAmpsBCLEAR.setStatus(
        ""
    )

gstDstsSourceAActiveCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21909)
)
gstDstsSourceAActiveCLEAR.setObjects(
      *(("GEIST-MIB", "dstsSourceAActive"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsSourceAActiveCLEAR.setStatus(
        ""
    )

gstDstsSourceBActiveCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21910)
)
gstDstsSourceBActiveCLEAR.setObjects(
      *(("GEIST-MIB", "dstsSourceBActive"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsSourceBActiveCLEAR.setStatus(
        ""
    )

gstDstsPowerStatusACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21911)
)
gstDstsPowerStatusACLEAR.setObjects(
      *(("GEIST-MIB", "dstsPowerStatusA"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsPowerStatusACLEAR.setStatus(
        ""
    )

gstDstsPowerStatusBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21912)
)
gstDstsPowerStatusBCLEAR.setObjects(
      *(("GEIST-MIB", "dstsPowerStatusB"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsPowerStatusBCLEAR.setStatus(
        ""
    )

gstDstsSourceATempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21913)
)
gstDstsSourceATempCCLEAR.setObjects(
      *(("GEIST-MIB", "dstsSourceATempC"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsSourceATempCCLEAR.setStatus(
        ""
    )

gstDstsSourceBTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 21914)
)
gstDstsSourceBTempCCLEAR.setObjects(
      *(("GEIST-MIB", "dstsSourceBTempC"),
        ("GEIST-MIB", "dstsName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstDstsSourceBTempCCLEAR.setStatus(
        ""
    )

gstCpmSensorStatusCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22005)
)
gstCpmSensorStatusCLEAR.setObjects(
      *(("GEIST-MIB", "cpmSensorStatus"),
        ("GEIST-MIB", "cpmSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCpmSensorStatusCLEAR.setStatus(
        ""
    )

gstSmokeAlarmStatusCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22105)
)
gstSmokeAlarmStatusCLEAR.setObjects(
      *(("GEIST-MIB", "smokeAlarmStatus"),
        ("GEIST-MIB", "smokeAlarmName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstSmokeAlarmStatusCLEAR.setStatus(
        ""
    )

gstNeg48VdcSensorVoltageCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22205)
)
gstNeg48VdcSensorVoltageCLEAR.setObjects(
      *(("GEIST-MIB", "neg48VdcSensorVoltage"),
        ("GEIST-MIB", "neg48VdcSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstNeg48VdcSensorVoltageCLEAR.setStatus(
        ""
    )

gstPos30VdcSensorVoltageCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22305)
)
gstPos30VdcSensorVoltageCLEAR.setObjects(
      *(("GEIST-MIB", "pos30VdcSensorVoltage"),
        ("GEIST-MIB", "pos30VdcSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstPos30VdcSensorVoltageCLEAR.setStatus(
        ""
    )

gstAnalogSensorAnalogCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22405)
)
gstAnalogSensorAnalogCLEAR.setObjects(
      *(("GEIST-MIB", "analogSensorAnalog"),
        ("GEIST-MIB", "analogSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstAnalogSensorAnalogCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECKWattHrsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22505)
)
gstCtrl3ChIECKWattHrsACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECKWattHrsA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECKWattHrsACLEAR.setStatus(
        ""
    )

gstCtrl3ChIECVoltsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22506)
)
gstCtrl3ChIECVoltsACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECVoltsA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltsACLEAR.setStatus(
        ""
    )

gstCtrl3ChIECVoltPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22507)
)
gstCtrl3ChIECVoltPeakACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECVoltPeakA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltPeakACLEAR.setStatus(
        ""
    )

gstCtrl3ChIECDeciAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22508)
)
gstCtrl3ChIECDeciAmpsACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECDeciAmpsA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsACLEAR.setStatus(
        ""
    )

gstCtrl3ChIECDeciAmpsPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22509)
)
gstCtrl3ChIECDeciAmpsPeakACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECDeciAmpsPeakA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsPeakACLEAR.setStatus(
        ""
    )

gstCtrl3ChIECRealPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22510)
)
gstCtrl3ChIECRealPowerACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECRealPowerA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerACLEAR.setStatus(
        ""
    )

gstCtrl3ChIECApparentPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22511)
)
gstCtrl3ChIECApparentPowerACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECApparentPowerA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECApparentPowerACLEAR.setStatus(
        ""
    )

gstCtrl3ChIECPowerFactorACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22512)
)
gstCtrl3ChIECPowerFactorACLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECPowerFactorA"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECPowerFactorACLEAR.setStatus(
        ""
    )

gstCtrl3ChIECKWattHrsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22513)
)
gstCtrl3ChIECKWattHrsBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECKWattHrsB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECKWattHrsBCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECVoltsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22514)
)
gstCtrl3ChIECVoltsBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECVoltsB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltsBCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECVoltPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22515)
)
gstCtrl3ChIECVoltPeakBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECVoltPeakB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltPeakBCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECDeciAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22516)
)
gstCtrl3ChIECDeciAmpsBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECDeciAmpsB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsBCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECDeciAmpsPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22517)
)
gstCtrl3ChIECDeciAmpsPeakBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECDeciAmpsPeakB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsPeakBCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECRealPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22518)
)
gstCtrl3ChIECRealPowerBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECRealPowerB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerBCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECApparentPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22519)
)
gstCtrl3ChIECApparentPowerBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECApparentPowerB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECApparentPowerBCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECPowerFactorBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22520)
)
gstCtrl3ChIECPowerFactorBCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECPowerFactorB"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECPowerFactorBCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECKWattHrsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22521)
)
gstCtrl3ChIECKWattHrsCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECKWattHrsC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECKWattHrsCCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECVoltsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22522)
)
gstCtrl3ChIECVoltsCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECVoltsC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltsCCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECVoltPeakCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22523)
)
gstCtrl3ChIECVoltPeakCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECVoltPeakC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltPeakCCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECDeciAmpsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22524)
)
gstCtrl3ChIECDeciAmpsCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECDeciAmpsC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsCCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECDeciAmpsPeakCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22525)
)
gstCtrl3ChIECDeciAmpsPeakCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECDeciAmpsPeakC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsPeakCCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECRealPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22526)
)
gstCtrl3ChIECRealPowerCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECRealPowerC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerCCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECApparentPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22527)
)
gstCtrl3ChIECApparentPowerCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECApparentPowerC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECApparentPowerCCLEAR.setStatus(
        ""
    )

gstCtrl3ChIECPowerFactorCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22528)
)
gstCtrl3ChIECPowerFactorCCLEAR.setObjects(
      *(("GEIST-MIB", "ctrl3ChIECPowerFactorC"),
        ("GEIST-MIB", "ctrl3ChIECName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECPowerFactorCCLEAR.setStatus(
        ""
    )

gstAirSpeedSwitchSensorAirSpeedCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 0, 22605)
)
gstAirSpeedSwitchSensorAirSpeedCLEAR.setObjects(
      *(("GEIST-MIB", "airSpeedSwitchSensorAirSpeed"),
        ("GEIST-MIB", "airSpeedSwitchSensorName"),
        ("GEIST-MIB", "productFriendlyName"),
        ("GEIST-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    gstAirSpeedSwitchSensorAirSpeedCLEAR.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GEIST-MIB",
    **{"geistmfg": geistmfg,
       "gstTestTRAP": gstTestTRAP,
       "gstClimateTempCTRAP": gstClimateTempCTRAP,
       "gstClimateHumidityTRAP": gstClimateHumidityTRAP,
       "gstClimateAirflowTRAP": gstClimateAirflowTRAP,
       "gstClimateLightTRAP": gstClimateLightTRAP,
       "gstClimateSoundTRAP": gstClimateSoundTRAP,
       "gstClimateIO1TRAP": gstClimateIO1TRAP,
       "gstClimateIO2TRAP": gstClimateIO2TRAP,
       "gstClimateIO3TRAP": gstClimateIO3TRAP,
       "gstClimateVoltsTRAP": gstClimateVoltsTRAP,
       "gstClimateVoltPeakTRAP": gstClimateVoltPeakTRAP,
       "gstClimateDeciAmpsATRAP": gstClimateDeciAmpsATRAP,
       "gstClimateAmpPeakATRAP": gstClimateAmpPeakATRAP,
       "gstClimateRealPowerATRAP": gstClimateRealPowerATRAP,
       "gstClimateApparentPowerATRAP": gstClimateApparentPowerATRAP,
       "gstClimatePowerFactorATRAP": gstClimatePowerFactorATRAP,
       "gstClimateDeciAmpsBTRAP": gstClimateDeciAmpsBTRAP,
       "gstClimateDeciAmpPeakBTRAP": gstClimateDeciAmpPeakBTRAP,
       "gstClimateRealPowerBTRAP": gstClimateRealPowerBTRAP,
       "gstClimateApparentPowerBTRAP": gstClimateApparentPowerBTRAP,
       "gstClimatePowerFactorBTRAP": gstClimatePowerFactorBTRAP,
       "gstClimateDeciAmpsCTRAP": gstClimateDeciAmpsCTRAP,
       "gstClimateDeciAmpPeakCTRAP": gstClimateDeciAmpPeakCTRAP,
       "gstClimateRealPowerCTRAP": gstClimateRealPowerCTRAP,
       "gstClimateApparentPowerCTRAP": gstClimateApparentPowerCTRAP,
       "gstClimatePowerFactorCTRAP": gstClimatePowerFactorCTRAP,
       "gstPowMonKWattHrsTRAP": gstPowMonKWattHrsTRAP,
       "gstPowMonVoltsTRAP": gstPowMonVoltsTRAP,
       "gstPowMonVoltMaxTRAP": gstPowMonVoltMaxTRAP,
       "gstPowMonVoltMinTRAP": gstPowMonVoltMinTRAP,
       "gstPowMonVoltPeakTRAP": gstPowMonVoltPeakTRAP,
       "gstPowMonDeciAmpsTRAP": gstPowMonDeciAmpsTRAP,
       "gstPowMonRealPowerTRAP": gstPowMonRealPowerTRAP,
       "gstPowMonApparentPowerTRAP": gstPowMonApparentPowerTRAP,
       "gstPowMonPowerFactorTRAP": gstPowMonPowerFactorTRAP,
       "gstPowMonDeciAmpsOutlet1TRAP": gstPowMonDeciAmpsOutlet1TRAP,
       "gstPowMonDeciAmpsOutlet2TRAP": gstPowMonDeciAmpsOutlet2TRAP,
       "gstTempSensorTempCTRAP": gstTempSensorTempCTRAP,
       "gstAirFlowSensorFlowTRAP": gstAirFlowSensorFlowTRAP,
       "gstAirFlowSensorTempCTRAP": gstAirFlowSensorTempCTRAP,
       "gstAirFlowSensorHumidityTRAP": gstAirFlowSensorHumidityTRAP,
       "gstAirFlowSensorDewPointTRAP": gstAirFlowSensorDewPointTRAP,
       "gstPowerVoltsTRAP": gstPowerVoltsTRAP,
       "gstPowerDeciAmpsTRAP": gstPowerDeciAmpsTRAP,
       "gstPowerRealPowerTRAP": gstPowerRealPowerTRAP,
       "gstPowerApparentPowerTRAP": gstPowerApparentPowerTRAP,
       "gstPowerPowerFactorTRAP": gstPowerPowerFactorTRAP,
       "gstDoorSensorStatusTRAP": gstDoorSensorStatusTRAP,
       "gstWaterSensorDampnessTRAP": gstWaterSensorDampnessTRAP,
       "gstCurrentMonitorDeciAmpsTRAP": gstCurrentMonitorDeciAmpsTRAP,
       "gstMillivoltMonitorMVTRAP": gstMillivoltMonitorMVTRAP,
       "gstPow3ChKWattHrsATRAP": gstPow3ChKWattHrsATRAP,
       "gstPow3ChVoltsATRAP": gstPow3ChVoltsATRAP,
       "gstPow3ChVoltMaxATRAP": gstPow3ChVoltMaxATRAP,
       "gstPow3ChVoltMinATRAP": gstPow3ChVoltMinATRAP,
       "gstPow3ChVoltPeakATRAP": gstPow3ChVoltPeakATRAP,
       "gstPow3ChDeciAmpsATRAP": gstPow3ChDeciAmpsATRAP,
       "gstPow3ChRealPowerATRAP": gstPow3ChRealPowerATRAP,
       "gstPow3ChApparentPowerATRAP": gstPow3ChApparentPowerATRAP,
       "gstPow3ChPowerFactorATRAP": gstPow3ChPowerFactorATRAP,
       "gstPow3ChKWattHrsBTRAP": gstPow3ChKWattHrsBTRAP,
       "gstPow3ChVoltsBTRAP": gstPow3ChVoltsBTRAP,
       "gstPow3ChVoltMaxBTRAP": gstPow3ChVoltMaxBTRAP,
       "gstPow3ChVoltMinBTRAP": gstPow3ChVoltMinBTRAP,
       "gstPow3ChVoltPeakBTRAP": gstPow3ChVoltPeakBTRAP,
       "gstPow3ChDeciAmpsBTRAP": gstPow3ChDeciAmpsBTRAP,
       "gstPow3ChRealPowerBTRAP": gstPow3ChRealPowerBTRAP,
       "gstPow3ChApparentPowerBTRAP": gstPow3ChApparentPowerBTRAP,
       "gstPow3ChPowerFactorBTRAP": gstPow3ChPowerFactorBTRAP,
       "gstPow3ChKWattHrsCTRAP": gstPow3ChKWattHrsCTRAP,
       "gstPow3ChVoltsCTRAP": gstPow3ChVoltsCTRAP,
       "gstPow3ChVoltMaxCTRAP": gstPow3ChVoltMaxCTRAP,
       "gstPow3ChVoltMinCTRAP": gstPow3ChVoltMinCTRAP,
       "gstPow3ChVoltPeakCTRAP": gstPow3ChVoltPeakCTRAP,
       "gstPow3ChDeciAmpsCTRAP": gstPow3ChDeciAmpsCTRAP,
       "gstPow3ChRealPowerCTRAP": gstPow3ChRealPowerCTRAP,
       "gstPow3ChApparentPowerCTRAP": gstPow3ChApparentPowerCTRAP,
       "gstPow3ChPowerFactorCTRAP": gstPow3ChPowerFactorCTRAP,
       "gstOutlet1StatusTRAP": gstOutlet1StatusTRAP,
       "gstOutlet2StatusTRAP": gstOutlet2StatusTRAP,
       "gstVsfcSetPointCTRAP": gstVsfcSetPointCTRAP,
       "gstVsfcIntTempCTRAP": gstVsfcIntTempCTRAP,
       "gstVsfcExt1TempCTRAP": gstVsfcExt1TempCTRAP,
       "gstVsfcExt2TempCTRAP": gstVsfcExt2TempCTRAP,
       "gstVsfcExt3TempCTRAP": gstVsfcExt3TempCTRAP,
       "gstVsfcExt4TempCTRAP": gstVsfcExt4TempCTRAP,
       "gstVsfcFanSpeedTRAP": gstVsfcFanSpeedTRAP,
       "gstCtrl3ChVoltsATRAP": gstCtrl3ChVoltsATRAP,
       "gstCtrl3ChVoltPeakATRAP": gstCtrl3ChVoltPeakATRAP,
       "gstCtrl3ChDeciAmpsATRAP": gstCtrl3ChDeciAmpsATRAP,
       "gstCtrl3ChDeciAmpsPeakATRAP": gstCtrl3ChDeciAmpsPeakATRAP,
       "gstCtrl3ChRealPowerATRAP": gstCtrl3ChRealPowerATRAP,
       "gstCtrl3ChApparentPowerATRAP": gstCtrl3ChApparentPowerATRAP,
       "gstCtrl3ChPowerFactorATRAP": gstCtrl3ChPowerFactorATRAP,
       "gstCtrl3ChVoltsBTRAP": gstCtrl3ChVoltsBTRAP,
       "gstCtrl3ChVoltPeakBTRAP": gstCtrl3ChVoltPeakBTRAP,
       "gstCtrl3ChDeciAmpsBTRAP": gstCtrl3ChDeciAmpsBTRAP,
       "gstCtrl3ChDeciAmpsPeakBTRAP": gstCtrl3ChDeciAmpsPeakBTRAP,
       "gstCtrl3ChRealPowerBTRAP": gstCtrl3ChRealPowerBTRAP,
       "gstCtrl3ChApparentPowerBTRAP": gstCtrl3ChApparentPowerBTRAP,
       "gstCtrl3ChPowerFactorBTRAP": gstCtrl3ChPowerFactorBTRAP,
       "gstCtrl3ChVoltsCTRAP": gstCtrl3ChVoltsCTRAP,
       "gstCtrl3ChVoltPeakCTRAP": gstCtrl3ChVoltPeakCTRAP,
       "gstCtrl3ChDeciAmpsCTRAP": gstCtrl3ChDeciAmpsCTRAP,
       "gstCtrl3ChDeciAmpsPeakCTRAP": gstCtrl3ChDeciAmpsPeakCTRAP,
       "gstCtrl3ChRealPowerCTRAP": gstCtrl3ChRealPowerCTRAP,
       "gstCtrl3ChApparentPowerCTRAP": gstCtrl3ChApparentPowerCTRAP,
       "gstCtrl3ChPowerFactorCTRAP": gstCtrl3ChPowerFactorCTRAP,
       "gstCtrlGrpAmpsATRAP": gstCtrlGrpAmpsATRAP,
       "gstCtrlGrpAmpsBTRAP": gstCtrlGrpAmpsBTRAP,
       "gstCtrlGrpAmpsCTRAP": gstCtrlGrpAmpsCTRAP,
       "gstCtrlGrpAmpsDTRAP": gstCtrlGrpAmpsDTRAP,
       "gstCtrlGrpAmpsETRAP": gstCtrlGrpAmpsETRAP,
       "gstCtrlGrpAmpsFTRAP": gstCtrlGrpAmpsFTRAP,
       "gstDewPointSensorDewPointTRAP": gstDewPointSensorDewPointTRAP,
       "gstDewPointSensorTempCTRAP": gstDewPointSensorTempCTRAP,
       "gstDewPointSensorHumidityTRAP": gstDewPointSensorHumidityTRAP,
       "gstDigitalSensorDigitalTRAP": gstDigitalSensorDigitalTRAP,
       "gstDstsVoltsATRAP": gstDstsVoltsATRAP,
       "gstDstsAmpsATRAP": gstDstsAmpsATRAP,
       "gstDstsVoltsBTRAP": gstDstsVoltsBTRAP,
       "gstDstsAmpsBTRAP": gstDstsAmpsBTRAP,
       "gstDstsSourceAActiveTRAP": gstDstsSourceAActiveTRAP,
       "gstDstsSourceBActiveTRAP": gstDstsSourceBActiveTRAP,
       "gstDstsPowerStatusATRAP": gstDstsPowerStatusATRAP,
       "gstDstsPowerStatusBTRAP": gstDstsPowerStatusBTRAP,
       "gstDstsSourceATempCTRAP": gstDstsSourceATempCTRAP,
       "gstDstsSourceBTempCTRAP": gstDstsSourceBTempCTRAP,
       "gstCpmSensorStatusTRAP": gstCpmSensorStatusTRAP,
       "gstSmokeAlarmStatusTRAP": gstSmokeAlarmStatusTRAP,
       "gstNeg48VdcSensorVoltageTRAP": gstNeg48VdcSensorVoltageTRAP,
       "gstPos30VdcSensorVoltageTRAP": gstPos30VdcSensorVoltageTRAP,
       "gstAnalogSensorAnalogTRAP": gstAnalogSensorAnalogTRAP,
       "gstCtrl3ChIECKWattHrsATRAP": gstCtrl3ChIECKWattHrsATRAP,
       "gstCtrl3ChIECVoltsATRAP": gstCtrl3ChIECVoltsATRAP,
       "gstCtrl3ChIECVoltPeakATRAP": gstCtrl3ChIECVoltPeakATRAP,
       "gstCtrl3ChIECDeciAmpsATRAP": gstCtrl3ChIECDeciAmpsATRAP,
       "gstCtrl3ChIECDeciAmpsPeakATRAP": gstCtrl3ChIECDeciAmpsPeakATRAP,
       "gstCtrl3ChIECRealPowerATRAP": gstCtrl3ChIECRealPowerATRAP,
       "gstCtrl3ChIECApparentPowerATRAP": gstCtrl3ChIECApparentPowerATRAP,
       "gstCtrl3ChIECPowerFactorATRAP": gstCtrl3ChIECPowerFactorATRAP,
       "gstCtrl3ChIECKWattHrsBTRAP": gstCtrl3ChIECKWattHrsBTRAP,
       "gstCtrl3ChIECVoltsBTRAP": gstCtrl3ChIECVoltsBTRAP,
       "gstCtrl3ChIECVoltPeakBTRAP": gstCtrl3ChIECVoltPeakBTRAP,
       "gstCtrl3ChIECDeciAmpsBTRAP": gstCtrl3ChIECDeciAmpsBTRAP,
       "gstCtrl3ChIECDeciAmpsPeakBTRAP": gstCtrl3ChIECDeciAmpsPeakBTRAP,
       "gstCtrl3ChIECRealPowerBTRAP": gstCtrl3ChIECRealPowerBTRAP,
       "gstCtrl3ChIECApparentPowerBTRAP": gstCtrl3ChIECApparentPowerBTRAP,
       "gstCtrl3ChIECPowerFactorBTRAP": gstCtrl3ChIECPowerFactorBTRAP,
       "gstCtrl3ChIECKWattHrsCTRAP": gstCtrl3ChIECKWattHrsCTRAP,
       "gstCtrl3ChIECVoltsCTRAP": gstCtrl3ChIECVoltsCTRAP,
       "gstCtrl3ChIECVoltPeakCTRAP": gstCtrl3ChIECVoltPeakCTRAP,
       "gstCtrl3ChIECDeciAmpsCTRAP": gstCtrl3ChIECDeciAmpsCTRAP,
       "gstCtrl3ChIECDeciAmpsPeakCTRAP": gstCtrl3ChIECDeciAmpsPeakCTRAP,
       "gstCtrl3ChIECRealPowerCTRAP": gstCtrl3ChIECRealPowerCTRAP,
       "gstCtrl3ChIECApparentPowerCTRAP": gstCtrl3ChIECApparentPowerCTRAP,
       "gstCtrl3ChIECPowerFactorCTRAP": gstCtrl3ChIECPowerFactorCTRAP,
       "gstAirSpeedSwitchSensorAirSpeedTRAP": gstAirSpeedSwitchSensorAirSpeedTRAP,
       "gstClimateTempCCLEAR": gstClimateTempCCLEAR,
       "gstClimateHumidityCLEAR": gstClimateHumidityCLEAR,
       "gstClimateAirflowCLEAR": gstClimateAirflowCLEAR,
       "gstClimateLightCLEAR": gstClimateLightCLEAR,
       "gstClimateSoundCLEAR": gstClimateSoundCLEAR,
       "gstClimateIO1CLEAR": gstClimateIO1CLEAR,
       "gstClimateIO2CLEAR": gstClimateIO2CLEAR,
       "gstClimateIO3CLEAR": gstClimateIO3CLEAR,
       "gstClimateVoltsCLEAR": gstClimateVoltsCLEAR,
       "gstClimateVoltPeakCLEAR": gstClimateVoltPeakCLEAR,
       "gstClimateDeciAmpsACLEAR": gstClimateDeciAmpsACLEAR,
       "gstClimateAmpPeakACLEAR": gstClimateAmpPeakACLEAR,
       "gstClimateRealPowerACLEAR": gstClimateRealPowerACLEAR,
       "gstClimateApparentPowerACLEAR": gstClimateApparentPowerACLEAR,
       "gstClimatePowerFactorACLEAR": gstClimatePowerFactorACLEAR,
       "gstClimateDeciAmpsBCLEAR": gstClimateDeciAmpsBCLEAR,
       "gstClimateDeciAmpPeakBCLEAR": gstClimateDeciAmpPeakBCLEAR,
       "gstClimateRealPowerBCLEAR": gstClimateRealPowerBCLEAR,
       "gstClimateApparentPowerBCLEAR": gstClimateApparentPowerBCLEAR,
       "gstClimatePowerFactorBCLEAR": gstClimatePowerFactorBCLEAR,
       "gstClimateDeciAmpsCCLEAR": gstClimateDeciAmpsCCLEAR,
       "gstClimateDeciAmpPeakCCLEAR": gstClimateDeciAmpPeakCCLEAR,
       "gstClimateRealPowerCCLEAR": gstClimateRealPowerCCLEAR,
       "gstClimateApparentPowerCCLEAR": gstClimateApparentPowerCCLEAR,
       "gstClimatePowerFactorCCLEAR": gstClimatePowerFactorCCLEAR,
       "gstPowMonKWattHrsCLEAR": gstPowMonKWattHrsCLEAR,
       "gstPowMonVoltsCLEAR": gstPowMonVoltsCLEAR,
       "gstPowMonVoltMaxCLEAR": gstPowMonVoltMaxCLEAR,
       "gstPowMonVoltMinCLEAR": gstPowMonVoltMinCLEAR,
       "gstPowMonVoltPeakCLEAR": gstPowMonVoltPeakCLEAR,
       "gstPowMonDeciAmpsCLEAR": gstPowMonDeciAmpsCLEAR,
       "gstPowMonRealPowerCLEAR": gstPowMonRealPowerCLEAR,
       "gstPowMonApparentPowerCLEAR": gstPowMonApparentPowerCLEAR,
       "gstPowMonPowerFactorCLEAR": gstPowMonPowerFactorCLEAR,
       "gstPowMonDeciAmpsOutlet1CLEAR": gstPowMonDeciAmpsOutlet1CLEAR,
       "gstPowMonDeciAmpsOutlet2CLEAR": gstPowMonDeciAmpsOutlet2CLEAR,
       "gstTempSensorTempCCLEAR": gstTempSensorTempCCLEAR,
       "gstAirFlowSensorFlowCLEAR": gstAirFlowSensorFlowCLEAR,
       "gstAirFlowSensorTempCCLEAR": gstAirFlowSensorTempCCLEAR,
       "gstAirFlowSensorHumidityCLEAR": gstAirFlowSensorHumidityCLEAR,
       "gstAirFlowSensorDewPointCLEAR": gstAirFlowSensorDewPointCLEAR,
       "gstPowerVoltsCLEAR": gstPowerVoltsCLEAR,
       "gstPowerDeciAmpsCLEAR": gstPowerDeciAmpsCLEAR,
       "gstPowerRealPowerCLEAR": gstPowerRealPowerCLEAR,
       "gstPowerApparentPowerCLEAR": gstPowerApparentPowerCLEAR,
       "gstPowerPowerFactorCLEAR": gstPowerPowerFactorCLEAR,
       "gstDoorSensorStatusCLEAR": gstDoorSensorStatusCLEAR,
       "gstWaterSensorDampnessCLEAR": gstWaterSensorDampnessCLEAR,
       "gstCurrentMonitorDeciAmpsCLEAR": gstCurrentMonitorDeciAmpsCLEAR,
       "gstMillivoltMonitorMVCLEAR": gstMillivoltMonitorMVCLEAR,
       "gstPow3ChKWattHrsACLEAR": gstPow3ChKWattHrsACLEAR,
       "gstPow3ChVoltsACLEAR": gstPow3ChVoltsACLEAR,
       "gstPow3ChVoltMaxACLEAR": gstPow3ChVoltMaxACLEAR,
       "gstPow3ChVoltMinACLEAR": gstPow3ChVoltMinACLEAR,
       "gstPow3ChVoltPeakACLEAR": gstPow3ChVoltPeakACLEAR,
       "gstPow3ChDeciAmpsACLEAR": gstPow3ChDeciAmpsACLEAR,
       "gstPow3ChRealPowerACLEAR": gstPow3ChRealPowerACLEAR,
       "gstPow3ChApparentPowerACLEAR": gstPow3ChApparentPowerACLEAR,
       "gstPow3ChPowerFactorACLEAR": gstPow3ChPowerFactorACLEAR,
       "gstPow3ChKWattHrsBCLEAR": gstPow3ChKWattHrsBCLEAR,
       "gstPow3ChVoltsBCLEAR": gstPow3ChVoltsBCLEAR,
       "gstPow3ChVoltMaxBCLEAR": gstPow3ChVoltMaxBCLEAR,
       "gstPow3ChVoltMinBCLEAR": gstPow3ChVoltMinBCLEAR,
       "gstPow3ChVoltPeakBCLEAR": gstPow3ChVoltPeakBCLEAR,
       "gstPow3ChDeciAmpsBCLEAR": gstPow3ChDeciAmpsBCLEAR,
       "gstPow3ChRealPowerBCLEAR": gstPow3ChRealPowerBCLEAR,
       "gstPow3ChApparentPowerBCLEAR": gstPow3ChApparentPowerBCLEAR,
       "gstPow3ChPowerFactorBCLEAR": gstPow3ChPowerFactorBCLEAR,
       "gstPow3ChKWattHrsCCLEAR": gstPow3ChKWattHrsCCLEAR,
       "gstPow3ChVoltsCCLEAR": gstPow3ChVoltsCCLEAR,
       "gstPow3ChVoltMaxCCLEAR": gstPow3ChVoltMaxCCLEAR,
       "gstPow3ChVoltMinCCLEAR": gstPow3ChVoltMinCCLEAR,
       "gstPow3ChVoltPeakCCLEAR": gstPow3ChVoltPeakCCLEAR,
       "gstPow3ChDeciAmpsCCLEAR": gstPow3ChDeciAmpsCCLEAR,
       "gstPow3ChRealPowerCCLEAR": gstPow3ChRealPowerCCLEAR,
       "gstPow3ChApparentPowerCCLEAR": gstPow3ChApparentPowerCCLEAR,
       "gstPow3ChPowerFactorCCLEAR": gstPow3ChPowerFactorCCLEAR,
       "gstOutlet1StatusCLEAR": gstOutlet1StatusCLEAR,
       "gstOutlet2StatusCLEAR": gstOutlet2StatusCLEAR,
       "gstVsfcSetPointCCLEAR": gstVsfcSetPointCCLEAR,
       "gstVsfcIntTempCCLEAR": gstVsfcIntTempCCLEAR,
       "gstVsfcExt1TempCCLEAR": gstVsfcExt1TempCCLEAR,
       "gstVsfcExt2TempCCLEAR": gstVsfcExt2TempCCLEAR,
       "gstVsfcExt3TempCCLEAR": gstVsfcExt3TempCCLEAR,
       "gstVsfcExt4TempCCLEAR": gstVsfcExt4TempCCLEAR,
       "gstVsfcFanSpeedCLEAR": gstVsfcFanSpeedCLEAR,
       "gstCtrl3ChVoltsACLEAR": gstCtrl3ChVoltsACLEAR,
       "gstCtrl3ChVoltPeakACLEAR": gstCtrl3ChVoltPeakACLEAR,
       "gstCtrl3ChDeciAmpsACLEAR": gstCtrl3ChDeciAmpsACLEAR,
       "gstCtrl3ChDeciAmpsPeakACLEAR": gstCtrl3ChDeciAmpsPeakACLEAR,
       "gstCtrl3ChRealPowerACLEAR": gstCtrl3ChRealPowerACLEAR,
       "gstCtrl3ChApparentPowerACLEAR": gstCtrl3ChApparentPowerACLEAR,
       "gstCtrl3ChPowerFactorACLEAR": gstCtrl3ChPowerFactorACLEAR,
       "gstCtrl3ChVoltsBCLEAR": gstCtrl3ChVoltsBCLEAR,
       "gstCtrl3ChVoltPeakBCLEAR": gstCtrl3ChVoltPeakBCLEAR,
       "gstCtrl3ChDeciAmpsBCLEAR": gstCtrl3ChDeciAmpsBCLEAR,
       "gstCtrl3ChDeciAmpsPeakBCLEAR": gstCtrl3ChDeciAmpsPeakBCLEAR,
       "gstCtrl3ChRealPowerBCLEAR": gstCtrl3ChRealPowerBCLEAR,
       "gstCtrl3ChApparentPowerBCLEAR": gstCtrl3ChApparentPowerBCLEAR,
       "gstCtrl3ChPowerFactorBCLEAR": gstCtrl3ChPowerFactorBCLEAR,
       "gstCtrl3ChVoltsCCLEAR": gstCtrl3ChVoltsCCLEAR,
       "gstCtrl3ChVoltPeakCCLEAR": gstCtrl3ChVoltPeakCCLEAR,
       "gstCtrl3ChDeciAmpsCCLEAR": gstCtrl3ChDeciAmpsCCLEAR,
       "gstCtrl3ChDeciAmpsPeakCCLEAR": gstCtrl3ChDeciAmpsPeakCCLEAR,
       "gstCtrl3ChRealPowerCCLEAR": gstCtrl3ChRealPowerCCLEAR,
       "gstCtrl3ChApparentPowerCCLEAR": gstCtrl3ChApparentPowerCCLEAR,
       "gstCtrl3ChPowerFactorCCLEAR": gstCtrl3ChPowerFactorCCLEAR,
       "gstCtrlGrpAmpsACLEAR": gstCtrlGrpAmpsACLEAR,
       "gstCtrlGrpAmpsBCLEAR": gstCtrlGrpAmpsBCLEAR,
       "gstCtrlGrpAmpsCCLEAR": gstCtrlGrpAmpsCCLEAR,
       "gstCtrlGrpAmpsDCLEAR": gstCtrlGrpAmpsDCLEAR,
       "gstCtrlGrpAmpsECLEAR": gstCtrlGrpAmpsECLEAR,
       "gstCtrlGrpAmpsFCLEAR": gstCtrlGrpAmpsFCLEAR,
       "gstDewPointSensorDewPointCLEAR": gstDewPointSensorDewPointCLEAR,
       "gstDewPointSensorTempCCLEAR": gstDewPointSensorTempCCLEAR,
       "gstDewPointSensorHumidityCLEAR": gstDewPointSensorHumidityCLEAR,
       "gstDigitalSensorDigitalCLEAR": gstDigitalSensorDigitalCLEAR,
       "gstDstsVoltsACLEAR": gstDstsVoltsACLEAR,
       "gstDstsAmpsACLEAR": gstDstsAmpsACLEAR,
       "gstDstsVoltsBCLEAR": gstDstsVoltsBCLEAR,
       "gstDstsAmpsBCLEAR": gstDstsAmpsBCLEAR,
       "gstDstsSourceAActiveCLEAR": gstDstsSourceAActiveCLEAR,
       "gstDstsSourceBActiveCLEAR": gstDstsSourceBActiveCLEAR,
       "gstDstsPowerStatusACLEAR": gstDstsPowerStatusACLEAR,
       "gstDstsPowerStatusBCLEAR": gstDstsPowerStatusBCLEAR,
       "gstDstsSourceATempCCLEAR": gstDstsSourceATempCCLEAR,
       "gstDstsSourceBTempCCLEAR": gstDstsSourceBTempCCLEAR,
       "gstCpmSensorStatusCLEAR": gstCpmSensorStatusCLEAR,
       "gstSmokeAlarmStatusCLEAR": gstSmokeAlarmStatusCLEAR,
       "gstNeg48VdcSensorVoltageCLEAR": gstNeg48VdcSensorVoltageCLEAR,
       "gstPos30VdcSensorVoltageCLEAR": gstPos30VdcSensorVoltageCLEAR,
       "gstAnalogSensorAnalogCLEAR": gstAnalogSensorAnalogCLEAR,
       "gstCtrl3ChIECKWattHrsACLEAR": gstCtrl3ChIECKWattHrsACLEAR,
       "gstCtrl3ChIECVoltsACLEAR": gstCtrl3ChIECVoltsACLEAR,
       "gstCtrl3ChIECVoltPeakACLEAR": gstCtrl3ChIECVoltPeakACLEAR,
       "gstCtrl3ChIECDeciAmpsACLEAR": gstCtrl3ChIECDeciAmpsACLEAR,
       "gstCtrl3ChIECDeciAmpsPeakACLEAR": gstCtrl3ChIECDeciAmpsPeakACLEAR,
       "gstCtrl3ChIECRealPowerACLEAR": gstCtrl3ChIECRealPowerACLEAR,
       "gstCtrl3ChIECApparentPowerACLEAR": gstCtrl3ChIECApparentPowerACLEAR,
       "gstCtrl3ChIECPowerFactorACLEAR": gstCtrl3ChIECPowerFactorACLEAR,
       "gstCtrl3ChIECKWattHrsBCLEAR": gstCtrl3ChIECKWattHrsBCLEAR,
       "gstCtrl3ChIECVoltsBCLEAR": gstCtrl3ChIECVoltsBCLEAR,
       "gstCtrl3ChIECVoltPeakBCLEAR": gstCtrl3ChIECVoltPeakBCLEAR,
       "gstCtrl3ChIECDeciAmpsBCLEAR": gstCtrl3ChIECDeciAmpsBCLEAR,
       "gstCtrl3ChIECDeciAmpsPeakBCLEAR": gstCtrl3ChIECDeciAmpsPeakBCLEAR,
       "gstCtrl3ChIECRealPowerBCLEAR": gstCtrl3ChIECRealPowerBCLEAR,
       "gstCtrl3ChIECApparentPowerBCLEAR": gstCtrl3ChIECApparentPowerBCLEAR,
       "gstCtrl3ChIECPowerFactorBCLEAR": gstCtrl3ChIECPowerFactorBCLEAR,
       "gstCtrl3ChIECKWattHrsCCLEAR": gstCtrl3ChIECKWattHrsCCLEAR,
       "gstCtrl3ChIECVoltsCCLEAR": gstCtrl3ChIECVoltsCCLEAR,
       "gstCtrl3ChIECVoltPeakCCLEAR": gstCtrl3ChIECVoltPeakCCLEAR,
       "gstCtrl3ChIECDeciAmpsCCLEAR": gstCtrl3ChIECDeciAmpsCCLEAR,
       "gstCtrl3ChIECDeciAmpsPeakCCLEAR": gstCtrl3ChIECDeciAmpsPeakCCLEAR,
       "gstCtrl3ChIECRealPowerCCLEAR": gstCtrl3ChIECRealPowerCCLEAR,
       "gstCtrl3ChIECApparentPowerCCLEAR": gstCtrl3ChIECApparentPowerCCLEAR,
       "gstCtrl3ChIECPowerFactorCCLEAR": gstCtrl3ChIECPowerFactorCCLEAR,
       "gstAirSpeedSwitchSensorAirSpeedCLEAR": gstAirSpeedSwitchSensorAirSpeedCLEAR,
       "geist": geist,
       "deviceInfo": deviceInfo,
       "productTitle": productTitle,
       "productVersion": productVersion,
       "productFriendlyName": productFriendlyName,
       "productMacAddress": productMacAddress,
       "productUrl": productUrl,
       "alarmTripType": alarmTripType,
       "productHardware": productHardware,
       "sensorCountsBase": sensorCountsBase,
       "sensorCounts": sensorCounts,
       "climateCount": climateCount,
       "powerMonitorCount": powerMonitorCount,
       "tempSensorCount": tempSensorCount,
       "airflowSensorCount": airflowSensorCount,
       "powerOnlyCount": powerOnlyCount,
       "doorSensorCount": doorSensorCount,
       "waterSensorCount": waterSensorCount,
       "currentSensorCount": currentSensorCount,
       "millivoltSensorCount": millivoltSensorCount,
       "power3ChSensorCount": power3ChSensorCount,
       "outletCount": outletCount,
       "vsfcCount": vsfcCount,
       "ctrl3ChCount": ctrl3ChCount,
       "ctrlGrpAmpsCount": ctrlGrpAmpsCount,
       "ctrlOutputCount": ctrlOutputCount,
       "dewpointSensorCount": dewpointSensorCount,
       "digitalSensorCount": digitalSensorCount,
       "dstsSensorCount": dstsSensorCount,
       "cpmSensorCount": cpmSensorCount,
       "smokeAlarmSensorCount": smokeAlarmSensorCount,
       "neg48VdcSensorCount": neg48VdcSensorCount,
       "pos30VdcSensorCount": pos30VdcSensorCount,
       "analogSensorCount": analogSensorCount,
       "ctrl3ChIECCount": ctrl3ChIECCount,
       "airSpeedSwitchSensorCount": airSpeedSwitchSensorCount,
       "climateTable": climateTable,
       "climateEntry": climateEntry,
       "climateIndex": climateIndex,
       "climateSerial": climateSerial,
       "climateName": climateName,
       "climateAvail": climateAvail,
       "climateTempC": climateTempC,
       "climateHumidity": climateHumidity,
       "climateAirflow": climateAirflow,
       "climateLight": climateLight,
       "climateSound": climateSound,
       "climateIO1": climateIO1,
       "climateIO2": climateIO2,
       "climateIO3": climateIO3,
       "climateVolts": climateVolts,
       "climateVoltPeak": climateVoltPeak,
       "climateDeciAmpsA": climateDeciAmpsA,
       "climateAmpPeakA": climateAmpPeakA,
       "climateRealPowerA": climateRealPowerA,
       "climateApparentPowerA": climateApparentPowerA,
       "climatePowerFactorA": climatePowerFactorA,
       "climateDeciAmpsB": climateDeciAmpsB,
       "climateDeciAmpPeakB": climateDeciAmpPeakB,
       "climateRealPowerB": climateRealPowerB,
       "climateApparentPowerB": climateApparentPowerB,
       "climatePowerFactorB": climatePowerFactorB,
       "climateDeciAmpsC": climateDeciAmpsC,
       "climateDeciAmpPeakC": climateDeciAmpPeakC,
       "climateRealPowerC": climateRealPowerC,
       "climateApparentPowerC": climateApparentPowerC,
       "climatePowerFactorC": climatePowerFactorC,
       "powerMonitorTable": powerMonitorTable,
       "powerMonitorEntry": powerMonitorEntry,
       "powMonIndex": powMonIndex,
       "powMonSerial": powMonSerial,
       "powMonName": powMonName,
       "powMonAvail": powMonAvail,
       "powMonKWattHrs": powMonKWattHrs,
       "powMonVolts": powMonVolts,
       "powMonVoltMax": powMonVoltMax,
       "powMonVoltMin": powMonVoltMin,
       "powMonVoltPeak": powMonVoltPeak,
       "powMonDeciAmps": powMonDeciAmps,
       "powMonRealPower": powMonRealPower,
       "powMonApparentPower": powMonApparentPower,
       "powMonPowerFactor": powMonPowerFactor,
       "powMonDeciAmpsOutlet1": powMonDeciAmpsOutlet1,
       "powMonDeciAmpsOutlet2": powMonDeciAmpsOutlet2,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorIndex": tempSensorIndex,
       "tempSensorSerial": tempSensorSerial,
       "tempSensorName": tempSensorName,
       "tempSensorAvail": tempSensorAvail,
       "tempSensorTempC": tempSensorTempC,
       "airFlowSensorTable": airFlowSensorTable,
       "airFlowSensorEntry": airFlowSensorEntry,
       "airFlowSensorIndex": airFlowSensorIndex,
       "airFlowSensorSerial": airFlowSensorSerial,
       "airFlowSensorName": airFlowSensorName,
       "airFlowSensorAvail": airFlowSensorAvail,
       "airFlowSensorFlow": airFlowSensorFlow,
       "airFlowSensorTempC": airFlowSensorTempC,
       "airFlowSensorHumidity": airFlowSensorHumidity,
       "airFlowSensorDewPoint": airFlowSensorDewPoint,
       "powerOnlyTable": powerOnlyTable,
       "powerOnlyEntry": powerOnlyEntry,
       "powerIndex": powerIndex,
       "powerSerial": powerSerial,
       "powerName": powerName,
       "powerAvail": powerAvail,
       "powerVolts": powerVolts,
       "powerDeciAmps": powerDeciAmps,
       "powerRealPower": powerRealPower,
       "powerApparentPower": powerApparentPower,
       "powerPowerFactor": powerPowerFactor,
       "doorSensorTable": doorSensorTable,
       "doorSensorEntry": doorSensorEntry,
       "doorSensorIndex": doorSensorIndex,
       "doorSensorSerial": doorSensorSerial,
       "doorSensorName": doorSensorName,
       "doorSensorAvail": doorSensorAvail,
       "doorSensorStatus": doorSensorStatus,
       "waterSensorTable": waterSensorTable,
       "waterSensorEntry": waterSensorEntry,
       "waterSensorIndex": waterSensorIndex,
       "waterSensorSerial": waterSensorSerial,
       "waterSensorName": waterSensorName,
       "waterSensorAvail": waterSensorAvail,
       "waterSensorDampness": waterSensorDampness,
       "currentMonitorTable": currentMonitorTable,
       "currentMonitorEntry": currentMonitorEntry,
       "currentMonitorIndex": currentMonitorIndex,
       "currentMonitorSerial": currentMonitorSerial,
       "currentMonitorName": currentMonitorName,
       "currentMonitorAvail": currentMonitorAvail,
       "currentMonitorDeciAmps": currentMonitorDeciAmps,
       "millivoltMonitorTable": millivoltMonitorTable,
       "millivoltMonitorEntry": millivoltMonitorEntry,
       "millivoltMonitorIndex": millivoltMonitorIndex,
       "millivoltMonitorSerial": millivoltMonitorSerial,
       "millivoltMonitorName": millivoltMonitorName,
       "millivoltMonitorAvail": millivoltMonitorAvail,
       "millivoltMonitorMV": millivoltMonitorMV,
       "power3ChTable": power3ChTable,
       "power3ChEntry": power3ChEntry,
       "pow3ChIndex": pow3ChIndex,
       "pow3ChSerial": pow3ChSerial,
       "pow3ChName": pow3ChName,
       "pow3ChAvail": pow3ChAvail,
       "pow3ChKWattHrsA": pow3ChKWattHrsA,
       "pow3ChVoltsA": pow3ChVoltsA,
       "pow3ChVoltMaxA": pow3ChVoltMaxA,
       "pow3ChVoltMinA": pow3ChVoltMinA,
       "pow3ChVoltPeakA": pow3ChVoltPeakA,
       "pow3ChDeciAmpsA": pow3ChDeciAmpsA,
       "pow3ChRealPowerA": pow3ChRealPowerA,
       "pow3ChApparentPowerA": pow3ChApparentPowerA,
       "pow3ChPowerFactorA": pow3ChPowerFactorA,
       "pow3ChKWattHrsB": pow3ChKWattHrsB,
       "pow3ChVoltsB": pow3ChVoltsB,
       "pow3ChVoltMaxB": pow3ChVoltMaxB,
       "pow3ChVoltMinB": pow3ChVoltMinB,
       "pow3ChVoltPeakB": pow3ChVoltPeakB,
       "pow3ChDeciAmpsB": pow3ChDeciAmpsB,
       "pow3ChRealPowerB": pow3ChRealPowerB,
       "pow3ChApparentPowerB": pow3ChApparentPowerB,
       "pow3ChPowerFactorB": pow3ChPowerFactorB,
       "pow3ChKWattHrsC": pow3ChKWattHrsC,
       "pow3ChVoltsC": pow3ChVoltsC,
       "pow3ChVoltMaxC": pow3ChVoltMaxC,
       "pow3ChVoltMinC": pow3ChVoltMinC,
       "pow3ChVoltPeakC": pow3ChVoltPeakC,
       "pow3ChDeciAmpsC": pow3ChDeciAmpsC,
       "pow3ChRealPowerC": pow3ChRealPowerC,
       "pow3ChApparentPowerC": pow3ChApparentPowerC,
       "pow3ChPowerFactorC": pow3ChPowerFactorC,
       "outletTable": outletTable,
       "outletEntry": outletEntry,
       "outletIndex": outletIndex,
       "outletSerial": outletSerial,
       "outletName": outletName,
       "outletAvail": outletAvail,
       "outlet1Status": outlet1Status,
       "outlet2Status": outlet2Status,
       "vsfcTable": vsfcTable,
       "vsfcEntry": vsfcEntry,
       "vsfcIndex": vsfcIndex,
       "vsfcSerial": vsfcSerial,
       "vsfcName": vsfcName,
       "vsfcAvail": vsfcAvail,
       "vsfcSetPointC": vsfcSetPointC,
       "vsfcIntTempC": vsfcIntTempC,
       "vsfcExt1TempC": vsfcExt1TempC,
       "vsfcExt2TempC": vsfcExt2TempC,
       "vsfcExt3TempC": vsfcExt3TempC,
       "vsfcExt4TempC": vsfcExt4TempC,
       "vsfcFanSpeed": vsfcFanSpeed,
       "ctrl3ChTable": ctrl3ChTable,
       "ctrl3ChEntry": ctrl3ChEntry,
       "ctrl3ChIndex": ctrl3ChIndex,
       "ctrl3ChSerial": ctrl3ChSerial,
       "ctrl3ChName": ctrl3ChName,
       "ctrl3ChAvail": ctrl3ChAvail,
       "ctrl3ChVoltsA": ctrl3ChVoltsA,
       "ctrl3ChVoltPeakA": ctrl3ChVoltPeakA,
       "ctrl3ChDeciAmpsA": ctrl3ChDeciAmpsA,
       "ctrl3ChDeciAmpsPeakA": ctrl3ChDeciAmpsPeakA,
       "ctrl3ChRealPowerA": ctrl3ChRealPowerA,
       "ctrl3ChApparentPowerA": ctrl3ChApparentPowerA,
       "ctrl3ChPowerFactorA": ctrl3ChPowerFactorA,
       "ctrl3ChVoltsB": ctrl3ChVoltsB,
       "ctrl3ChVoltPeakB": ctrl3ChVoltPeakB,
       "ctrl3ChDeciAmpsB": ctrl3ChDeciAmpsB,
       "ctrl3ChDeciAmpsPeakB": ctrl3ChDeciAmpsPeakB,
       "ctrl3ChRealPowerB": ctrl3ChRealPowerB,
       "ctrl3ChApparentPowerB": ctrl3ChApparentPowerB,
       "ctrl3ChPowerFactorB": ctrl3ChPowerFactorB,
       "ctrl3ChVoltsC": ctrl3ChVoltsC,
       "ctrl3ChVoltPeakC": ctrl3ChVoltPeakC,
       "ctrl3ChDeciAmpsC": ctrl3ChDeciAmpsC,
       "ctrl3ChDeciAmpsPeakC": ctrl3ChDeciAmpsPeakC,
       "ctrl3ChRealPowerC": ctrl3ChRealPowerC,
       "ctrl3ChApparentPowerC": ctrl3ChApparentPowerC,
       "ctrl3ChPowerFactorC": ctrl3ChPowerFactorC,
       "ctrlGrpAmpsTable": ctrlGrpAmpsTable,
       "ctrlGrpAmpsEntry": ctrlGrpAmpsEntry,
       "ctrlGrpAmpsIndex": ctrlGrpAmpsIndex,
       "ctrlGrpAmpsSerial": ctrlGrpAmpsSerial,
       "ctrlGrpAmpsName": ctrlGrpAmpsName,
       "ctrlGrpAmpsAvail": ctrlGrpAmpsAvail,
       "ctrlGrpAmpsA": ctrlGrpAmpsA,
       "ctrlGrpAmpsB": ctrlGrpAmpsB,
       "ctrlGrpAmpsC": ctrlGrpAmpsC,
       "ctrlGrpAmpsD": ctrlGrpAmpsD,
       "ctrlGrpAmpsE": ctrlGrpAmpsE,
       "ctrlGrpAmpsF": ctrlGrpAmpsF,
       "ctrlOutletTable": ctrlOutletTable,
       "ctrlOutletEntry": ctrlOutletEntry,
       "ctrlOutletIndex": ctrlOutletIndex,
       "ctrlOutletName": ctrlOutletName,
       "ctrlOutletStatus": ctrlOutletStatus,
       "ctrlOutletFeedback": ctrlOutletFeedback,
       "ctrlOutletPending": ctrlOutletPending,
       "ctrlOutletDeciAmps": ctrlOutletDeciAmps,
       "ctrlOutletGroup": ctrlOutletGroup,
       "ctrlOutletUpDelay": ctrlOutletUpDelay,
       "ctrlOutletDwnDelay": ctrlOutletDwnDelay,
       "ctrlOutletRbtDelay": ctrlOutletRbtDelay,
       "ctrlOutletURL": ctrlOutletURL,
       "ctrlOutletPOAAction": ctrlOutletPOAAction,
       "ctrlOutletPOADelay": ctrlOutletPOADelay,
       "dewPointSensorTable": dewPointSensorTable,
       "dewPointSensorEntry": dewPointSensorEntry,
       "dewPointSensorIndex": dewPointSensorIndex,
       "dewPointSensorSerial": dewPointSensorSerial,
       "dewPointSensorName": dewPointSensorName,
       "dewPointSensorAvail": dewPointSensorAvail,
       "dewPointSensorDewPoint": dewPointSensorDewPoint,
       "dewPointSensorTempC": dewPointSensorTempC,
       "dewPointSensorHumidity": dewPointSensorHumidity,
       "digitalSensorTable": digitalSensorTable,
       "digitalSensorEntry": digitalSensorEntry,
       "digitalSensorIndex": digitalSensorIndex,
       "digitalSensorSerial": digitalSensorSerial,
       "digitalSensorName": digitalSensorName,
       "digitalSensorAvail": digitalSensorAvail,
       "digitalSensorDigital": digitalSensorDigital,
       "dstsTable": dstsTable,
       "dstsEntry": dstsEntry,
       "dstsIndex": dstsIndex,
       "dstsSerial": dstsSerial,
       "dstsName": dstsName,
       "dstsAvail": dstsAvail,
       "dstsVoltsA": dstsVoltsA,
       "dstsAmpsA": dstsAmpsA,
       "dstsVoltsB": dstsVoltsB,
       "dstsAmpsB": dstsAmpsB,
       "dstsSourceAActive": dstsSourceAActive,
       "dstsSourceBActive": dstsSourceBActive,
       "dstsPowerStatusA": dstsPowerStatusA,
       "dstsPowerStatusB": dstsPowerStatusB,
       "dstsSourceATempC": dstsSourceATempC,
       "dstsSourceBTempC": dstsSourceBTempC,
       "cpmSensorTable": cpmSensorTable,
       "cpmSensorEntry": cpmSensorEntry,
       "cpmSensorIndex": cpmSensorIndex,
       "cpmSensorSerial": cpmSensorSerial,
       "cpmSensorName": cpmSensorName,
       "cpmSensorAvail": cpmSensorAvail,
       "cpmSensorStatus": cpmSensorStatus,
       "smokeAlarmTable": smokeAlarmTable,
       "smokeAlarmEntry": smokeAlarmEntry,
       "smokeAlarmIndex": smokeAlarmIndex,
       "smokeAlarmSerial": smokeAlarmSerial,
       "smokeAlarmName": smokeAlarmName,
       "smokeAlarmAvail": smokeAlarmAvail,
       "smokeAlarmStatus": smokeAlarmStatus,
       "neg48VdcSensorTable": neg48VdcSensorTable,
       "neg48VdcSensorEntry": neg48VdcSensorEntry,
       "neg48VdcSensorIndex": neg48VdcSensorIndex,
       "neg48VdcSensorSerial": neg48VdcSensorSerial,
       "neg48VdcSensorName": neg48VdcSensorName,
       "neg48VdcSensorAvail": neg48VdcSensorAvail,
       "neg48VdcSensorVoltage": neg48VdcSensorVoltage,
       "pos30VdcSensorTable": pos30VdcSensorTable,
       "pos30VdcSensorEntry": pos30VdcSensorEntry,
       "pos30VdcSensorIndex": pos30VdcSensorIndex,
       "pos30VdcSensorSerial": pos30VdcSensorSerial,
       "pos30VdcSensorName": pos30VdcSensorName,
       "pos30VdcSensorAvail": pos30VdcSensorAvail,
       "pos30VdcSensorVoltage": pos30VdcSensorVoltage,
       "analogSensorTable": analogSensorTable,
       "analogSensorEntry": analogSensorEntry,
       "analogSensorIndex": analogSensorIndex,
       "analogSensorSerial": analogSensorSerial,
       "analogSensorName": analogSensorName,
       "analogSensorAvail": analogSensorAvail,
       "analogSensorAnalog": analogSensorAnalog,
       "ctrl3ChIECTable": ctrl3ChIECTable,
       "ctrl3ChIECEntry": ctrl3ChIECEntry,
       "ctrl3ChIECIndex": ctrl3ChIECIndex,
       "ctrl3ChIECSerial": ctrl3ChIECSerial,
       "ctrl3ChIECName": ctrl3ChIECName,
       "ctrl3ChIECAvail": ctrl3ChIECAvail,
       "ctrl3ChIECKWattHrsA": ctrl3ChIECKWattHrsA,
       "ctrl3ChIECVoltsA": ctrl3ChIECVoltsA,
       "ctrl3ChIECVoltPeakA": ctrl3ChIECVoltPeakA,
       "ctrl3ChIECDeciAmpsA": ctrl3ChIECDeciAmpsA,
       "ctrl3ChIECDeciAmpsPeakA": ctrl3ChIECDeciAmpsPeakA,
       "ctrl3ChIECRealPowerA": ctrl3ChIECRealPowerA,
       "ctrl3ChIECApparentPowerA": ctrl3ChIECApparentPowerA,
       "ctrl3ChIECPowerFactorA": ctrl3ChIECPowerFactorA,
       "ctrl3ChIECKWattHrsB": ctrl3ChIECKWattHrsB,
       "ctrl3ChIECVoltsB": ctrl3ChIECVoltsB,
       "ctrl3ChIECVoltPeakB": ctrl3ChIECVoltPeakB,
       "ctrl3ChIECDeciAmpsB": ctrl3ChIECDeciAmpsB,
       "ctrl3ChIECDeciAmpsPeakB": ctrl3ChIECDeciAmpsPeakB,
       "ctrl3ChIECRealPowerB": ctrl3ChIECRealPowerB,
       "ctrl3ChIECApparentPowerB": ctrl3ChIECApparentPowerB,
       "ctrl3ChIECPowerFactorB": ctrl3ChIECPowerFactorB,
       "ctrl3ChIECKWattHrsC": ctrl3ChIECKWattHrsC,
       "ctrl3ChIECVoltsC": ctrl3ChIECVoltsC,
       "ctrl3ChIECVoltPeakC": ctrl3ChIECVoltPeakC,
       "ctrl3ChIECDeciAmpsC": ctrl3ChIECDeciAmpsC,
       "ctrl3ChIECDeciAmpsPeakC": ctrl3ChIECDeciAmpsPeakC,
       "ctrl3ChIECRealPowerC": ctrl3ChIECRealPowerC,
       "ctrl3ChIECApparentPowerC": ctrl3ChIECApparentPowerC,
       "ctrl3ChIECPowerFactorC": ctrl3ChIECPowerFactorC,
       "airSpeedSwitchSensorTable": airSpeedSwitchSensorTable,
       "airSpeedSwitchSensorEntry": airSpeedSwitchSensorEntry,
       "airSpeedSwitchSensorIndex": airSpeedSwitchSensorIndex,
       "airSpeedSwitchSensorSerial": airSpeedSwitchSensorSerial,
       "airSpeedSwitchSensorName": airSpeedSwitchSensorName,
       "airSpeedSwitchSensorAvail": airSpeedSwitchSensorAvail,
       "airSpeedSwitchSensorAirSpeed": airSpeedSwitchSensorAirSpeed}
)
