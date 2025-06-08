# SNMP MIB module (GEIST-MIB-V3) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_21239/GEIST-MIB-V3.mib
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

geist = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21239)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GeistV3_ObjectIdentity = ObjectIdentity
geistV3 = _GeistV3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 2)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1)
)
_ProductTitle_Type = DisplayString
_ProductTitle_Object = MibScalar
productTitle = _ProductTitle_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 1),
    _ProductTitle_Type()
)
productTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productTitle.setStatus("current")
_ProductVersion_Type = DisplayString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 2),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")
_ProductFriendlyName_Type = DisplayString
_ProductFriendlyName_Object = MibScalar
productFriendlyName = _ProductFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 3),
    _ProductFriendlyName_Type()
)
productFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productFriendlyName.setStatus("current")
_ProductMacAddress_Type = DisplayString
_ProductMacAddress_Object = MibScalar
productMacAddress = _ProductMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 4),
    _ProductMacAddress_Type()
)
productMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMacAddress.setStatus("current")
_ProductUrl_Type = DisplayString
_ProductUrl_Object = MibScalar
productUrl = _ProductUrl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 5),
    _ProductUrl_Type()
)
productUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productUrl.setStatus("current")


class _AlarmTripType_Type(Integer32):
    """Custom type alarmTripType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("low", 1),
          ("high", 2),
          ("unplugged", 3))
    )


_AlarmTripType_Type.__name__ = "Integer32"
_AlarmTripType_Object = MibScalar
alarmTripType = _AlarmTripType_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 6),
    _AlarmTripType_Type()
)
alarmTripType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTripType.setStatus("current")
_ProductHardware_Type = DisplayString
_ProductHardware_Object = MibScalar
productHardware = _ProductHardware_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 7),
    _ProductHardware_Type()
)
productHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productHardware.setStatus("current")
_SensorCountsBase_ObjectIdentity = ObjectIdentity
sensorCountsBase = _SensorCountsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8)
)
_SensorCounts_ObjectIdentity = ObjectIdentity
sensorCounts = _SensorCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1)
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 5),
    _AirflowSensorCount_Type()
)
airflowSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airflowSensorCount.setStatus("current")


class _Ctrl3ChDELTACount_Type(Integer32):
    """Custom type ctrl3ChDELTACount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Ctrl3ChDELTACount_Type.__name__ = "Integer32"
_Ctrl3ChDELTACount_Object = MibScalar
ctrl3ChDELTACount = _Ctrl3ChDELTACount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 6),
    _Ctrl3ChDELTACount_Type()
)
ctrl3ChDELTACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTACount.setStatus("current")


class _DoorSensorCount_Type(Integer32):
    """Custom type doorSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DoorSensorCount_Type.__name__ = "Integer32"
_DoorSensorCount_Object = MibScalar
doorSensorCount = _DoorSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 15),
    _CtrlGrpAmpsCount_Type()
)
ctrlGrpAmpsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsCount.setStatus("current")


class _CtrlOutletCount_Type(Integer32):
    """Custom type ctrlOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CtrlOutletCount_Type.__name__ = "Integer32"
_CtrlOutletCount_Object = MibScalar
ctrlOutletCount = _CtrlOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 16),
    _CtrlOutletCount_Type()
)
ctrlOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletCount.setStatus("current")


class _DewpointSensorCount_Type(Integer32):
    """Custom type dewpointSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DewpointSensorCount_Type.__name__ = "Integer32"
_DewpointSensorCount_Object = MibScalar
dewpointSensorCount = _DewpointSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 22),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 25),
    _Ctrl3ChIECCount_Type()
)
ctrl3ChIECCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECCount.setStatus("current")


class _ClimateRelayCount_Type(Integer32):
    """Custom type climateRelayCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ClimateRelayCount_Type.__name__ = "Integer32"
_ClimateRelayCount_Object = MibScalar
climateRelayCount = _ClimateRelayCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 26),
    _ClimateRelayCount_Type()
)
climateRelayCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRelayCount.setStatus("current")


class _CtrlRelayCount_Type(Integer32):
    """Custom type ctrlRelayCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CtrlRelayCount_Type.__name__ = "Integer32"
_CtrlRelayCount_Object = MibScalar
ctrlRelayCount = _CtrlRelayCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 27),
    _CtrlRelayCount_Type()
)
ctrlRelayCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlRelayCount.setStatus("current")


class _AirSpeedSwitchSensorCount_Type(Integer32):
    """Custom type airSpeedSwitchSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AirSpeedSwitchSensorCount_Type.__name__ = "Integer32"
_AirSpeedSwitchSensorCount_Object = MibScalar
airSpeedSwitchSensorCount = _AirSpeedSwitchSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 28),
    _AirSpeedSwitchSensorCount_Type()
)
airSpeedSwitchSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airSpeedSwitchSensorCount.setStatus("current")


class _PowerDMCount_Type(Integer32):
    """Custom type powerDMCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PowerDMCount_Type.__name__ = "Integer32"
_PowerDMCount_Object = MibScalar
powerDMCount = _PowerDMCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 29),
    _PowerDMCount_Type()
)
powerDMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMCount.setStatus("current")


class _IoExpanderCount_Type(Integer32):
    """Custom type ioExpanderCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_IoExpanderCount_Type.__name__ = "Integer32"
_IoExpanderCount_Object = MibScalar
ioExpanderCount = _IoExpanderCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 30),
    _IoExpanderCount_Type()
)
ioExpanderCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderCount.setStatus("current")


class _T3hdSensorCount_Type(Integer32):
    """Custom type t3hdSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_T3hdSensorCount_Type.__name__ = "Integer32"
_T3hdSensorCount_Object = MibScalar
t3hdSensorCount = _T3hdSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 31),
    _T3hdSensorCount_Type()
)
t3hdSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorCount.setStatus("current")


class _ThdSensorCount_Type(Integer32):
    """Custom type thdSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ThdSensorCount_Type.__name__ = "Integer32"
_ThdSensorCount_Object = MibScalar
thdSensorCount = _ThdSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 32),
    _ThdSensorCount_Type()
)
thdSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorCount.setStatus("current")


class _Pos60VdcSensorCount_Type(Integer32):
    """Custom type pos60VdcSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Pos60VdcSensorCount_Type.__name__ = "Integer32"
_Pos60VdcSensorCount_Object = MibScalar
pos60VdcSensorCount = _Pos60VdcSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 33),
    _Pos60VdcSensorCount_Type()
)
pos60VdcSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos60VdcSensorCount.setStatus("current")


class _Ctrl2CirTotCount_Type(Integer32):
    """Custom type ctrl2CirTotCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Ctrl2CirTotCount_Type.__name__ = "Integer32"
_Ctrl2CirTotCount_Object = MibScalar
ctrl2CirTotCount = _Ctrl2CirTotCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 34),
    _Ctrl2CirTotCount_Type()
)
ctrl2CirTotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotCount.setStatus("current")


class _Sc10Count_Type(Integer32):
    """Custom type sc10Count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Sc10Count_Type.__name__ = "Integer32"
_Sc10Count_Object = MibScalar
sc10Count = _Sc10Count_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 8, 1, 35),
    _Sc10Count_Type()
)
sc10Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc10Count.setStatus("current")


class _TemperaturePrecision_Type(Integer32):
    """Custom type temperaturePrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("degree", 0),
          ("deciDegree", 1))
    )


_TemperaturePrecision_Type.__name__ = "Integer32"
_TemperaturePrecision_Object = MibScalar
temperaturePrecision = _TemperaturePrecision_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 9),
    _TemperaturePrecision_Type()
)
temperaturePrecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperaturePrecision.setStatus("current")
_AlarmTrigger_Type = DisplayString
_AlarmTrigger_Object = MibScalar
alarmTrigger = _AlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 11),
    _AlarmTrigger_Type()
)
alarmTrigger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmTrigger.setStatus("current")


class _AlarmInstance_Type(Integer32):
    """Custom type alarmInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AlarmInstance_Type.__name__ = "Integer32"
_AlarmInstance_Object = MibScalar
alarmInstance = _AlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 1, 12),
    _AlarmInstance_Type()
)
alarmInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmInstance.setStatus("current")
_ClimateTable_Object = MibTable
climateTable = _ClimateTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2)
)
if mibBuilder.loadTexts:
    climateTable.setStatus("current")
_ClimateEntry_Object = MibTableRow
climateEntry = _ClimateEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1)
)
climateEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "climateIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 1),
    _ClimateIndex_Type()
)
climateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    climateIndex.setStatus("current")
_ClimateSerial_Type = DisplayString
_ClimateSerial_Object = MibTableColumn
climateSerial = _ClimateSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 2),
    _ClimateSerial_Type()
)
climateSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateSerial.setStatus("current")
_ClimateName_Type = DisplayString
_ClimateName_Object = MibTableColumn
climateName = _ClimateName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 3),
    _ClimateName_Type()
)
climateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateName.setStatus("current")
_ClimateAvail_Type = Gauge32
_ClimateAvail_Object = MibTableColumn
climateAvail = _ClimateAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 4),
    _ClimateAvail_Type()
)
climateAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateAvail.setStatus("current")


class _ClimateTempC_Type(Integer32):
    """Custom type climateTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_ClimateTempC_Type.__name__ = "Integer32"
_ClimateTempC_Object = MibTableColumn
climateTempC = _ClimateTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 5),
    _ClimateTempC_Type()
)
climateTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateTempC.setStatus("current")
if mibBuilder.loadTexts:
    climateTempC.setUnits("Degrees Celsius")


class _ClimateTempF_Type(Integer32):
    """Custom type climateTempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_ClimateTempF_Type.__name__ = "Integer32"
_ClimateTempF_Object = MibTableColumn
climateTempF = _ClimateTempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 6),
    _ClimateTempF_Type()
)
climateTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateTempF.setStatus("current")
if mibBuilder.loadTexts:
    climateTempF.setUnits("Degress Fahrenheit")


class _ClimateHumidity_Type(Integer32):
    """Custom type climateHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateHumidity_Type.__name__ = "Integer32"
_ClimateHumidity_Object = MibTableColumn
climateHumidity = _ClimateHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 7),
    _ClimateHumidity_Type()
)
climateHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateHumidity.setStatus("current")
if mibBuilder.loadTexts:
    climateHumidity.setUnits("%")


class _ClimateLight_Type(Integer32):
    """Custom type climateLight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateLight_Type.__name__ = "Integer32"
_ClimateLight_Object = MibTableColumn
climateLight = _ClimateLight_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 8),
    _ClimateLight_Type()
)
climateLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateLight.setStatus("current")


class _ClimateAirflow_Type(Integer32):
    """Custom type climateAirflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateAirflow_Type.__name__ = "Integer32"
_ClimateAirflow_Object = MibTableColumn
climateAirflow = _ClimateAirflow_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 9),
    _ClimateAirflow_Type()
)
climateAirflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateAirflow.setStatus("current")


class _ClimateSound_Type(Integer32):
    """Custom type climateSound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateSound_Type.__name__ = "Integer32"
_ClimateSound_Object = MibTableColumn
climateSound = _ClimateSound_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 13),
    _ClimateIO3_Type()
)
climateIO3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateIO3.setStatus("current")
_ClimateVolts_Type = Gauge32
_ClimateVolts_Object = MibTableColumn
climateVolts = _ClimateVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 14),
    _ClimateVolts_Type()
)
climateVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateVolts.setStatus("current")
if mibBuilder.loadTexts:
    climateVolts.setUnits("Volts (rms)")
_ClimateVoltPeak_Type = Gauge32
_ClimateVoltPeak_Object = MibTableColumn
climateVoltPeak = _ClimateVoltPeak_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 15),
    _ClimateVoltPeak_Type()
)
climateVoltPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateVoltPeak.setStatus("current")
if mibBuilder.loadTexts:
    climateVoltPeak.setUnits("Volts (rms)")
_ClimateDeciAmpsA_Type = Gauge32
_ClimateDeciAmpsA_Object = MibTableColumn
climateDeciAmpsA = _ClimateDeciAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 16),
    _ClimateDeciAmpsA_Type()
)
climateDeciAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDeciAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    climateDeciAmpsA.setUnits("0.1 Amps (rms)")
_ClimateDeciAmpPeakA_Type = Gauge32
_ClimateDeciAmpPeakA_Object = MibTableColumn
climateDeciAmpPeakA = _ClimateDeciAmpPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 17),
    _ClimateDeciAmpPeakA_Type()
)
climateDeciAmpPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDeciAmpPeakA.setStatus("current")
if mibBuilder.loadTexts:
    climateDeciAmpPeakA.setUnits("0.1 Amps (rms)")
_ClimateRealPowerA_Type = Gauge32
_ClimateRealPowerA_Object = MibTableColumn
climateRealPowerA = _ClimateRealPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 18),
    _ClimateRealPowerA_Type()
)
climateRealPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRealPowerA.setStatus("current")
if mibBuilder.loadTexts:
    climateRealPowerA.setUnits("Watts")
_ClimateApparentPowerA_Type = Gauge32
_ClimateApparentPowerA_Object = MibTableColumn
climateApparentPowerA = _ClimateApparentPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 19),
    _ClimateApparentPowerA_Type()
)
climateApparentPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateApparentPowerA.setStatus("current")
if mibBuilder.loadTexts:
    climateApparentPowerA.setUnits("Volt-Amps")
_ClimatePowerFactorA_Type = Gauge32
_ClimatePowerFactorA_Object = MibTableColumn
climatePowerFactorA = _ClimatePowerFactorA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 20),
    _ClimatePowerFactorA_Type()
)
climatePowerFactorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climatePowerFactorA.setStatus("current")
if mibBuilder.loadTexts:
    climatePowerFactorA.setUnits("%")
_ClimateDeciAmpsB_Type = Gauge32
_ClimateDeciAmpsB_Object = MibTableColumn
climateDeciAmpsB = _ClimateDeciAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 21),
    _ClimateDeciAmpsB_Type()
)
climateDeciAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDeciAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    climateDeciAmpsB.setUnits("0.1 Amps (rms)")
_ClimateDeciAmpPeakB_Type = Gauge32
_ClimateDeciAmpPeakB_Object = MibTableColumn
climateDeciAmpPeakB = _ClimateDeciAmpPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 22),
    _ClimateDeciAmpPeakB_Type()
)
climateDeciAmpPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDeciAmpPeakB.setStatus("current")
if mibBuilder.loadTexts:
    climateDeciAmpPeakB.setUnits("0.1 Amps (rms)")
_ClimateRealPowerB_Type = Gauge32
_ClimateRealPowerB_Object = MibTableColumn
climateRealPowerB = _ClimateRealPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 23),
    _ClimateRealPowerB_Type()
)
climateRealPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRealPowerB.setStatus("current")
if mibBuilder.loadTexts:
    climateRealPowerB.setUnits("Watts")
_ClimateApparentPowerB_Type = Gauge32
_ClimateApparentPowerB_Object = MibTableColumn
climateApparentPowerB = _ClimateApparentPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 24),
    _ClimateApparentPowerB_Type()
)
climateApparentPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateApparentPowerB.setStatus("current")
if mibBuilder.loadTexts:
    climateApparentPowerB.setUnits("Volt-Amps")
_ClimatePowerFactorB_Type = Gauge32
_ClimatePowerFactorB_Object = MibTableColumn
climatePowerFactorB = _ClimatePowerFactorB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 25),
    _ClimatePowerFactorB_Type()
)
climatePowerFactorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climatePowerFactorB.setStatus("current")
if mibBuilder.loadTexts:
    climatePowerFactorB.setUnits("%")
_ClimateDeciAmpsC_Type = Gauge32
_ClimateDeciAmpsC_Object = MibTableColumn
climateDeciAmpsC = _ClimateDeciAmpsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 26),
    _ClimateDeciAmpsC_Type()
)
climateDeciAmpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDeciAmpsC.setStatus("current")
if mibBuilder.loadTexts:
    climateDeciAmpsC.setUnits("0.1 Amps (rms)")
_ClimateDeciAmpPeakC_Type = Gauge32
_ClimateDeciAmpPeakC_Object = MibTableColumn
climateDeciAmpPeakC = _ClimateDeciAmpPeakC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 27),
    _ClimateDeciAmpPeakC_Type()
)
climateDeciAmpPeakC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDeciAmpPeakC.setStatus("current")
if mibBuilder.loadTexts:
    climateDeciAmpPeakC.setUnits("0.1 Amps (rms)")
_ClimateRealPowerC_Type = Gauge32
_ClimateRealPowerC_Object = MibTableColumn
climateRealPowerC = _ClimateRealPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 28),
    _ClimateRealPowerC_Type()
)
climateRealPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRealPowerC.setStatus("current")
if mibBuilder.loadTexts:
    climateRealPowerC.setUnits("Watts")
_ClimateApparentPowerC_Type = Gauge32
_ClimateApparentPowerC_Object = MibTableColumn
climateApparentPowerC = _ClimateApparentPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 29),
    _ClimateApparentPowerC_Type()
)
climateApparentPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateApparentPowerC.setStatus("current")
if mibBuilder.loadTexts:
    climateApparentPowerC.setUnits("Volt-Amps")
_ClimatePowerFactorC_Type = Gauge32
_ClimatePowerFactorC_Object = MibTableColumn
climatePowerFactorC = _ClimatePowerFactorC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 30),
    _ClimatePowerFactorC_Type()
)
climatePowerFactorC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climatePowerFactorC.setStatus("current")
if mibBuilder.loadTexts:
    climatePowerFactorC.setUnits("%")


class _ClimateDewPointC_Type(Integer32):
    """Custom type climateDewPointC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_ClimateDewPointC_Type.__name__ = "Integer32"
_ClimateDewPointC_Object = MibTableColumn
climateDewPointC = _ClimateDewPointC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 31),
    _ClimateDewPointC_Type()
)
climateDewPointC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDewPointC.setStatus("current")
if mibBuilder.loadTexts:
    climateDewPointC.setUnits("Degrees Celsius")


class _ClimateDewPointF_Type(Integer32):
    """Custom type climateDewPointF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_ClimateDewPointF_Type.__name__ = "Integer32"
_ClimateDewPointF_Object = MibTableColumn
climateDewPointF = _ClimateDewPointF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 2, 1, 32),
    _ClimateDewPointF_Type()
)
climateDewPointF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateDewPointF.setStatus("current")
if mibBuilder.loadTexts:
    climateDewPointF.setUnits("Degress Fahrenheit")
_PowMonTable_Object = MibTable
powMonTable = _PowMonTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3)
)
if mibBuilder.loadTexts:
    powMonTable.setStatus("current")
_PowMonEntry_Object = MibTableRow
powMonEntry = _PowMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1)
)
powMonEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "powMonIndex"),
)
if mibBuilder.loadTexts:
    powMonEntry.setStatus("current")


class _PowMonIndex_Type(Integer32):
    """Custom type powMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PowMonIndex_Type.__name__ = "Integer32"
_PowMonIndex_Object = MibTableColumn
powMonIndex = _PowMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 1),
    _PowMonIndex_Type()
)
powMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powMonIndex.setStatus("current")
_PowMonSerial_Type = DisplayString
_PowMonSerial_Object = MibTableColumn
powMonSerial = _PowMonSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 2),
    _PowMonSerial_Type()
)
powMonSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonSerial.setStatus("current")
_PowMonName_Type = DisplayString
_PowMonName_Object = MibTableColumn
powMonName = _PowMonName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 3),
    _PowMonName_Type()
)
powMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonName.setStatus("current")
_PowMonAvail_Type = Gauge32
_PowMonAvail_Object = MibTableColumn
powMonAvail = _PowMonAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 4),
    _PowMonAvail_Type()
)
powMonAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonAvail.setStatus("current")
_PowMonkWattHrs_Type = Gauge32
_PowMonkWattHrs_Object = MibTableColumn
powMonkWattHrs = _PowMonkWattHrs_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 5),
    _PowMonkWattHrs_Type()
)
powMonkWattHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonkWattHrs.setStatus("current")
if mibBuilder.loadTexts:
    powMonkWattHrs.setUnits("kWh")
_PowMonVolts_Type = Gauge32
_PowMonVolts_Object = MibTableColumn
powMonVolts = _PowMonVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 6),
    _PowMonVolts_Type()
)
powMonVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonVolts.setStatus("current")
if mibBuilder.loadTexts:
    powMonVolts.setUnits("Volts (rms)")
_PowMonVoltMax_Type = Gauge32
_PowMonVoltMax_Object = MibTableColumn
powMonVoltMax = _PowMonVoltMax_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 7),
    _PowMonVoltMax_Type()
)
powMonVoltMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonVoltMax.setStatus("current")
if mibBuilder.loadTexts:
    powMonVoltMax.setUnits("Volts (rms)")
_PowMonVoltMin_Type = Gauge32
_PowMonVoltMin_Object = MibTableColumn
powMonVoltMin = _PowMonVoltMin_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 8),
    _PowMonVoltMin_Type()
)
powMonVoltMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonVoltMin.setStatus("current")
if mibBuilder.loadTexts:
    powMonVoltMin.setUnits("Volts (rms)")
_PowMonVoltPeak_Type = Gauge32
_PowMonVoltPeak_Object = MibTableColumn
powMonVoltPeak = _PowMonVoltPeak_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 9),
    _PowMonVoltPeak_Type()
)
powMonVoltPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonVoltPeak.setStatus("current")
if mibBuilder.loadTexts:
    powMonVoltPeak.setUnits("Volts (rms)")
_PowMonDeciAmps_Type = Gauge32
_PowMonDeciAmps_Object = MibTableColumn
powMonDeciAmps = _PowMonDeciAmps_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 10),
    _PowMonDeciAmps_Type()
)
powMonDeciAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonDeciAmps.setStatus("current")
if mibBuilder.loadTexts:
    powMonDeciAmps.setUnits("0.1 Amps (rms)")
_PowMonRealPower_Type = Gauge32
_PowMonRealPower_Object = MibTableColumn
powMonRealPower = _PowMonRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 11),
    _PowMonRealPower_Type()
)
powMonRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonRealPower.setStatus("current")
if mibBuilder.loadTexts:
    powMonRealPower.setUnits("Watts")
_PowMonApparentPower_Type = Gauge32
_PowMonApparentPower_Object = MibTableColumn
powMonApparentPower = _PowMonApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 13),
    _PowMonPowerFactor_Type()
)
powMonPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    powMonPowerFactor.setUnits("%")


class _PowMonOutlet1_Type(Integer32):
    """Custom type powMonOutlet1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PowMonOutlet1_Type.__name__ = "Integer32"
_PowMonOutlet1_Object = MibTableColumn
powMonOutlet1 = _PowMonOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 14),
    _PowMonOutlet1_Type()
)
powMonOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonOutlet1.setStatus("current")
if mibBuilder.loadTexts:
    powMonOutlet1.setUnits("Outlet 1")


class _PowMonOutlet2_Type(Integer32):
    """Custom type powMonOutlet2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PowMonOutlet2_Type.__name__ = "Integer32"
_PowMonOutlet2_Object = MibTableColumn
powMonOutlet2 = _PowMonOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 15),
    _PowMonOutlet2_Type()
)
powMonOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonOutlet2.setStatus("current")
if mibBuilder.loadTexts:
    powMonOutlet2.setUnits("Outlet 2")
_PowMonOutlet1StatusTime_Type = Gauge32
_PowMonOutlet1StatusTime_Object = MibTableColumn
powMonOutlet1StatusTime = _PowMonOutlet1StatusTime_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 16),
    _PowMonOutlet1StatusTime_Type()
)
powMonOutlet1StatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonOutlet1StatusTime.setStatus("current")
if mibBuilder.loadTexts:
    powMonOutlet1StatusTime.setUnits("seconds")
_PowMonOutlet2StatusTime_Type = Gauge32
_PowMonOutlet2StatusTime_Object = MibTableColumn
powMonOutlet2StatusTime = _PowMonOutlet2StatusTime_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 3, 1, 17),
    _PowMonOutlet2StatusTime_Type()
)
powMonOutlet2StatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powMonOutlet2StatusTime.setStatus("current")
if mibBuilder.loadTexts:
    powMonOutlet2StatusTime.setUnits("seconds")
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 4)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("current")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 4, 1)
)
tempSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "tempSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 4, 1, 1),
    _TempSensorIndex_Type()
)
tempSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempSensorIndex.setStatus("current")
_TempSensorSerial_Type = DisplayString
_TempSensorSerial_Object = MibTableColumn
tempSensorSerial = _TempSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 4, 1, 2),
    _TempSensorSerial_Type()
)
tempSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorSerial.setStatus("current")
_TempSensorName_Type = DisplayString
_TempSensorName_Object = MibTableColumn
tempSensorName = _TempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 4, 1, 3),
    _TempSensorName_Type()
)
tempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorName.setStatus("current")
_TempSensorAvail_Type = Gauge32
_TempSensorAvail_Object = MibTableColumn
tempSensorAvail = _TempSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 4, 1, 4),
    _TempSensorAvail_Type()
)
tempSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorAvail.setStatus("current")


class _TempSensorTempC_Type(Integer32):
    """Custom type tempSensorTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_TempSensorTempC_Type.__name__ = "Integer32"
_TempSensorTempC_Object = MibTableColumn
tempSensorTempC = _TempSensorTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 4, 1, 5),
    _TempSensorTempC_Type()
)
tempSensorTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorTempC.setStatus("current")
if mibBuilder.loadTexts:
    tempSensorTempC.setUnits("Degrees Celsius")


class _TempSensorTempF_Type(Integer32):
    """Custom type tempSensorTempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_TempSensorTempF_Type.__name__ = "Integer32"
_TempSensorTempF_Object = MibTableColumn
tempSensorTempF = _TempSensorTempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 4, 1, 6),
    _TempSensorTempF_Type()
)
tempSensorTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorTempF.setStatus("current")
if mibBuilder.loadTexts:
    tempSensorTempF.setUnits("Degrees Fahrenheit")
_AirFlowSensorTable_Object = MibTable
airFlowSensorTable = _AirFlowSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 5)
)
if mibBuilder.loadTexts:
    airFlowSensorTable.setStatus("current")
_AirFlowSensorEntry_Object = MibTableRow
airFlowSensorEntry = _AirFlowSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 5, 1)
)
airFlowSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "airFlowSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 5, 1, 1),
    _AirFlowSensorIndex_Type()
)
airFlowSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    airFlowSensorIndex.setStatus("current")
_AirFlowSensorSerial_Type = DisplayString
_AirFlowSensorSerial_Object = MibTableColumn
airFlowSensorSerial = _AirFlowSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 5, 1, 2),
    _AirFlowSensorSerial_Type()
)
airFlowSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorSerial.setStatus("current")
_AirFlowSensorName_Type = DisplayString
_AirFlowSensorName_Object = MibTableColumn
airFlowSensorName = _AirFlowSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 5, 1, 3),
    _AirFlowSensorName_Type()
)
airFlowSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorName.setStatus("current")
_AirFlowSensorAvail_Type = Gauge32
_AirFlowSensorAvail_Object = MibTableColumn
airFlowSensorAvail = _AirFlowSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 5, 1, 4),
    _AirFlowSensorAvail_Type()
)
airFlowSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorAvail.setStatus("current")


class _AirFlowSensorTempC_Type(Integer32):
    """Custom type airFlowSensorTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_AirFlowSensorTempC_Type.__name__ = "Integer32"
_AirFlowSensorTempC_Object = MibTableColumn
airFlowSensorTempC = _AirFlowSensorTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 5, 1, 5),
    _AirFlowSensorTempC_Type()
)
airFlowSensorTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorTempC.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorTempC.setUnits("Degrees Celsius")


class _AirFlowSensorTempF_Type(Integer32):
    """Custom type airFlowSensorTempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_AirFlowSensorTempF_Type.__name__ = "Integer32"
_AirFlowSensorTempF_Object = MibTableColumn
airFlowSensorTempF = _AirFlowSensorTempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 5, 1, 6),
    _AirFlowSensorTempF_Type()
)
airFlowSensorTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorTempF.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorTempF.setUnits("Degrees Fahrenheit")


class _AirFlowSensorFlow_Type(Integer32):
    """Custom type airFlowSensorFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AirFlowSensorFlow_Type.__name__ = "Integer32"
_AirFlowSensorFlow_Object = MibTableColumn
airFlowSensorFlow = _AirFlowSensorFlow_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 5, 1, 7),
    _AirFlowSensorFlow_Type()
)
airFlowSensorFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorFlow.setStatus("current")


class _AirFlowSensorHumidity_Type(Integer32):
    """Custom type airFlowSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AirFlowSensorHumidity_Type.__name__ = "Integer32"
_AirFlowSensorHumidity_Object = MibTableColumn
airFlowSensorHumidity = _AirFlowSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 5, 1, 8),
    _AirFlowSensorHumidity_Type()
)
airFlowSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorHumidity.setUnits("%")


class _AirFlowSensorDewPointC_Type(Integer32):
    """Custom type airFlowSensorDewPointC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_AirFlowSensorDewPointC_Type.__name__ = "Integer32"
_AirFlowSensorDewPointC_Object = MibTableColumn
airFlowSensorDewPointC = _AirFlowSensorDewPointC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 5, 1, 9),
    _AirFlowSensorDewPointC_Type()
)
airFlowSensorDewPointC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorDewPointC.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorDewPointC.setUnits("Degrees Celsius")


class _AirFlowSensorDewPointF_Type(Integer32):
    """Custom type airFlowSensorDewPointF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_AirFlowSensorDewPointF_Type.__name__ = "Integer32"
_AirFlowSensorDewPointF_Object = MibTableColumn
airFlowSensorDewPointF = _AirFlowSensorDewPointF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 5, 1, 10),
    _AirFlowSensorDewPointF_Type()
)
airFlowSensorDewPointF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorDewPointF.setStatus("current")
if mibBuilder.loadTexts:
    airFlowSensorDewPointF.setUnits("Degress Fahrenheit")
_Ctrl3ChDELTATable_Object = MibTable
ctrl3ChDELTATable = _Ctrl3ChDELTATable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6)
)
if mibBuilder.loadTexts:
    ctrl3ChDELTATable.setStatus("current")
_Ctrl3ChDELTAEntry_Object = MibTableRow
ctrl3ChDELTAEntry = _Ctrl3ChDELTAEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1)
)
ctrl3ChDELTAEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "ctrl3ChDELTAIndex"),
)
if mibBuilder.loadTexts:
    ctrl3ChDELTAEntry.setStatus("current")


class _Ctrl3ChDELTAIndex_Type(Integer32):
    """Custom type ctrl3ChDELTAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Ctrl3ChDELTAIndex_Type.__name__ = "Integer32"
_Ctrl3ChDELTAIndex_Object = MibTableColumn
ctrl3ChDELTAIndex = _Ctrl3ChDELTAIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 1),
    _Ctrl3ChDELTAIndex_Type()
)
ctrl3ChDELTAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrl3ChDELTAIndex.setStatus("current")
_Ctrl3ChDELTASerial_Type = DisplayString
_Ctrl3ChDELTASerial_Object = MibTableColumn
ctrl3ChDELTASerial = _Ctrl3ChDELTASerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 2),
    _Ctrl3ChDELTASerial_Type()
)
ctrl3ChDELTASerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTASerial.setStatus("current")
_Ctrl3ChDELTAName_Type = DisplayString
_Ctrl3ChDELTAName_Object = MibTableColumn
ctrl3ChDELTAName = _Ctrl3ChDELTAName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 3),
    _Ctrl3ChDELTAName_Type()
)
ctrl3ChDELTAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAName.setStatus("current")
_Ctrl3ChDELTAAvail_Type = Gauge32
_Ctrl3ChDELTAAvail_Object = MibTableColumn
ctrl3ChDELTAAvail = _Ctrl3ChDELTAAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 4),
    _Ctrl3ChDELTAAvail_Type()
)
ctrl3ChDELTAAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAAvail.setStatus("current")


class _Ctrl3ChDELTAPowerChCount_Type(Integer32):
    """Custom type ctrl3ChDELTAPowerChCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Ctrl3ChDELTAPowerChCount_Type.__name__ = "Integer32"
_Ctrl3ChDELTAPowerChCount_Object = MibTableColumn
ctrl3ChDELTAPowerChCount = _Ctrl3ChDELTAPowerChCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 5),
    _Ctrl3ChDELTAPowerChCount_Type()
)
ctrl3ChDELTAPowerChCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAPowerChCount.setStatus("current")
_Ctrl3ChDELTADeciAmpsA_Type = Gauge32
_Ctrl3ChDELTADeciAmpsA_Object = MibTableColumn
ctrl3ChDELTADeciAmpsA = _Ctrl3ChDELTADeciAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 6),
    _Ctrl3ChDELTADeciAmpsA_Type()
)
ctrl3ChDELTADeciAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTADeciAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTADeciAmpsA.setUnits("0.1 Amps (rms)")
_Ctrl3ChDELTADeciAmpsB_Type = Gauge32
_Ctrl3ChDELTADeciAmpsB_Object = MibTableColumn
ctrl3ChDELTADeciAmpsB = _Ctrl3ChDELTADeciAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 7),
    _Ctrl3ChDELTADeciAmpsB_Type()
)
ctrl3ChDELTADeciAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTADeciAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTADeciAmpsB.setUnits("0.1 Amps (rms)")
_Ctrl3ChDELTADeciAmpsC_Type = Gauge32
_Ctrl3ChDELTADeciAmpsC_Object = MibTableColumn
ctrl3ChDELTADeciAmpsC = _Ctrl3ChDELTADeciAmpsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 8),
    _Ctrl3ChDELTADeciAmpsC_Type()
)
ctrl3ChDELTADeciAmpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTADeciAmpsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTADeciAmpsC.setUnits("0.1 Amps (rms)")
_Ctrl3ChDELTAkWattHrsTotal_Type = Gauge32
_Ctrl3ChDELTAkWattHrsTotal_Object = MibTableColumn
ctrl3ChDELTAkWattHrsTotal = _Ctrl3ChDELTAkWattHrsTotal_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 9),
    _Ctrl3ChDELTAkWattHrsTotal_Type()
)
ctrl3ChDELTAkWattHrsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAkWattHrsTotal.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAkWattHrsTotal.setUnits("kWh")
_Ctrl3ChDELTARealPowerTotal_Type = Gauge32
_Ctrl3ChDELTARealPowerTotal_Object = MibTableColumn
ctrl3ChDELTARealPowerTotal = _Ctrl3ChDELTARealPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 10),
    _Ctrl3ChDELTARealPowerTotal_Type()
)
ctrl3ChDELTARealPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTARealPowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTARealPowerTotal.setUnits("Watts")
_Ctrl3ChDELTAkWattHrsAB_Type = Gauge32
_Ctrl3ChDELTAkWattHrsAB_Object = MibTableColumn
ctrl3ChDELTAkWattHrsAB = _Ctrl3ChDELTAkWattHrsAB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 11),
    _Ctrl3ChDELTAkWattHrsAB_Type()
)
ctrl3ChDELTAkWattHrsAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAkWattHrsAB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAkWattHrsAB.setUnits("kWh")
_Ctrl3ChDELTAVoltsAB_Type = Gauge32
_Ctrl3ChDELTAVoltsAB_Object = MibTableColumn
ctrl3ChDELTAVoltsAB = _Ctrl3ChDELTAVoltsAB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 12),
    _Ctrl3ChDELTAVoltsAB_Type()
)
ctrl3ChDELTAVoltsAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAVoltsAB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAVoltsAB.setUnits("Volts (rms)")
_Ctrl3ChDELTAVoltPeakAB_Type = Gauge32
_Ctrl3ChDELTAVoltPeakAB_Object = MibTableColumn
ctrl3ChDELTAVoltPeakAB = _Ctrl3ChDELTAVoltPeakAB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 13),
    _Ctrl3ChDELTAVoltPeakAB_Type()
)
ctrl3ChDELTAVoltPeakAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAVoltPeakAB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAVoltPeakAB.setUnits("Volts (rms)")
_Ctrl3ChDELTARealPowerAB_Type = Gauge32
_Ctrl3ChDELTARealPowerAB_Object = MibTableColumn
ctrl3ChDELTARealPowerAB = _Ctrl3ChDELTARealPowerAB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 14),
    _Ctrl3ChDELTARealPowerAB_Type()
)
ctrl3ChDELTARealPowerAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTARealPowerAB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTARealPowerAB.setUnits("Watts")
_Ctrl3ChDELTAApparentPowerAB_Type = Gauge32
_Ctrl3ChDELTAApparentPowerAB_Object = MibTableColumn
ctrl3ChDELTAApparentPowerAB = _Ctrl3ChDELTAApparentPowerAB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 15),
    _Ctrl3ChDELTAApparentPowerAB_Type()
)
ctrl3ChDELTAApparentPowerAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAApparentPowerAB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAApparentPowerAB.setUnits("Volt-Amps")


class _Ctrl3ChDELTAPowerFactorAB_Type(Integer32):
    """Custom type ctrl3ChDELTAPowerFactorAB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ctrl3ChDELTAPowerFactorAB_Type.__name__ = "Integer32"
_Ctrl3ChDELTAPowerFactorAB_Object = MibTableColumn
ctrl3ChDELTAPowerFactorAB = _Ctrl3ChDELTAPowerFactorAB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 16),
    _Ctrl3ChDELTAPowerFactorAB_Type()
)
ctrl3ChDELTAPowerFactorAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAPowerFactorAB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAPowerFactorAB.setUnits("%")
_Ctrl3ChDELTAkWattHrsBC_Type = Gauge32
_Ctrl3ChDELTAkWattHrsBC_Object = MibTableColumn
ctrl3ChDELTAkWattHrsBC = _Ctrl3ChDELTAkWattHrsBC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 17),
    _Ctrl3ChDELTAkWattHrsBC_Type()
)
ctrl3ChDELTAkWattHrsBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAkWattHrsBC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAkWattHrsBC.setUnits("kWh")
_Ctrl3ChDELTAVoltsBC_Type = Gauge32
_Ctrl3ChDELTAVoltsBC_Object = MibTableColumn
ctrl3ChDELTAVoltsBC = _Ctrl3ChDELTAVoltsBC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 18),
    _Ctrl3ChDELTAVoltsBC_Type()
)
ctrl3ChDELTAVoltsBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAVoltsBC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAVoltsBC.setUnits("Volts (rms)")
_Ctrl3ChDELTAVoltPeakBC_Type = Gauge32
_Ctrl3ChDELTAVoltPeakBC_Object = MibTableColumn
ctrl3ChDELTAVoltPeakBC = _Ctrl3ChDELTAVoltPeakBC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 19),
    _Ctrl3ChDELTAVoltPeakBC_Type()
)
ctrl3ChDELTAVoltPeakBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAVoltPeakBC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAVoltPeakBC.setUnits("Volts (rms)")
_Ctrl3ChDELTARealPowerBC_Type = Gauge32
_Ctrl3ChDELTARealPowerBC_Object = MibTableColumn
ctrl3ChDELTARealPowerBC = _Ctrl3ChDELTARealPowerBC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 20),
    _Ctrl3ChDELTARealPowerBC_Type()
)
ctrl3ChDELTARealPowerBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTARealPowerBC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTARealPowerBC.setUnits("Watts")
_Ctrl3ChDELTAApparentPowerBC_Type = Gauge32
_Ctrl3ChDELTAApparentPowerBC_Object = MibTableColumn
ctrl3ChDELTAApparentPowerBC = _Ctrl3ChDELTAApparentPowerBC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 21),
    _Ctrl3ChDELTAApparentPowerBC_Type()
)
ctrl3ChDELTAApparentPowerBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAApparentPowerBC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAApparentPowerBC.setUnits("Volt-Amps")


class _Ctrl3ChDELTAPowerFactorBC_Type(Integer32):
    """Custom type ctrl3ChDELTAPowerFactorBC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ctrl3ChDELTAPowerFactorBC_Type.__name__ = "Integer32"
_Ctrl3ChDELTAPowerFactorBC_Object = MibTableColumn
ctrl3ChDELTAPowerFactorBC = _Ctrl3ChDELTAPowerFactorBC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 22),
    _Ctrl3ChDELTAPowerFactorBC_Type()
)
ctrl3ChDELTAPowerFactorBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAPowerFactorBC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAPowerFactorBC.setUnits("%")
_Ctrl3ChDELTAkWattHrsCA_Type = Gauge32
_Ctrl3ChDELTAkWattHrsCA_Object = MibTableColumn
ctrl3ChDELTAkWattHrsCA = _Ctrl3ChDELTAkWattHrsCA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 23),
    _Ctrl3ChDELTAkWattHrsCA_Type()
)
ctrl3ChDELTAkWattHrsCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAkWattHrsCA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAkWattHrsCA.setUnits("kWh")
_Ctrl3ChDELTAVoltsCA_Type = Gauge32
_Ctrl3ChDELTAVoltsCA_Object = MibTableColumn
ctrl3ChDELTAVoltsCA = _Ctrl3ChDELTAVoltsCA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 24),
    _Ctrl3ChDELTAVoltsCA_Type()
)
ctrl3ChDELTAVoltsCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAVoltsCA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAVoltsCA.setUnits("Volts (rms)")
_Ctrl3ChDELTAVoltPeakCA_Type = Gauge32
_Ctrl3ChDELTAVoltPeakCA_Object = MibTableColumn
ctrl3ChDELTAVoltPeakCA = _Ctrl3ChDELTAVoltPeakCA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 25),
    _Ctrl3ChDELTAVoltPeakCA_Type()
)
ctrl3ChDELTAVoltPeakCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAVoltPeakCA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAVoltPeakCA.setUnits("Volts (rms)")
_Ctrl3ChDELTARealPowerCA_Type = Gauge32
_Ctrl3ChDELTARealPowerCA_Object = MibTableColumn
ctrl3ChDELTARealPowerCA = _Ctrl3ChDELTARealPowerCA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 26),
    _Ctrl3ChDELTARealPowerCA_Type()
)
ctrl3ChDELTARealPowerCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTARealPowerCA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTARealPowerCA.setUnits("Watts")
_Ctrl3ChDELTAApparentPowerCA_Type = Gauge32
_Ctrl3ChDELTAApparentPowerCA_Object = MibTableColumn
ctrl3ChDELTAApparentPowerCA = _Ctrl3ChDELTAApparentPowerCA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 27),
    _Ctrl3ChDELTAApparentPowerCA_Type()
)
ctrl3ChDELTAApparentPowerCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAApparentPowerCA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAApparentPowerCA.setUnits("Volt-Amps")


class _Ctrl3ChDELTAPowerFactorCA_Type(Integer32):
    """Custom type ctrl3ChDELTAPowerFactorCA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ctrl3ChDELTAPowerFactorCA_Type.__name__ = "Integer32"
_Ctrl3ChDELTAPowerFactorCA_Object = MibTableColumn
ctrl3ChDELTAPowerFactorCA = _Ctrl3ChDELTAPowerFactorCA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 6, 1, 28),
    _Ctrl3ChDELTAPowerFactorCA_Type()
)
ctrl3ChDELTAPowerFactorCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDELTAPowerFactorCA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDELTAPowerFactorCA.setUnits("%")
_DoorSensorTable_Object = MibTable
doorSensorTable = _DoorSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 7)
)
if mibBuilder.loadTexts:
    doorSensorTable.setStatus("current")
_DoorSensorEntry_Object = MibTableRow
doorSensorEntry = _DoorSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 7, 1)
)
doorSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "doorSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 7, 1, 1),
    _DoorSensorIndex_Type()
)
doorSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    doorSensorIndex.setStatus("current")
_DoorSensorSerial_Type = DisplayString
_DoorSensorSerial_Object = MibTableColumn
doorSensorSerial = _DoorSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 7, 1, 2),
    _DoorSensorSerial_Type()
)
doorSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSensorSerial.setStatus("current")
_DoorSensorName_Type = DisplayString
_DoorSensorName_Object = MibTableColumn
doorSensorName = _DoorSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 7, 1, 3),
    _DoorSensorName_Type()
)
doorSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSensorName.setStatus("current")
_DoorSensorAvail_Type = Gauge32
_DoorSensorAvail_Object = MibTableColumn
doorSensorAvail = _DoorSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 7, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 7, 1, 5),
    _DoorSensorStatus_Type()
)
doorSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSensorStatus.setStatus("current")
_WaterSensorTable_Object = MibTable
waterSensorTable = _WaterSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 8)
)
if mibBuilder.loadTexts:
    waterSensorTable.setStatus("current")
_WaterSensorEntry_Object = MibTableRow
waterSensorEntry = _WaterSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 8, 1)
)
waterSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "waterSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 8, 1, 1),
    _WaterSensorIndex_Type()
)
waterSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    waterSensorIndex.setStatus("current")
_WaterSensorSerial_Type = DisplayString
_WaterSensorSerial_Object = MibTableColumn
waterSensorSerial = _WaterSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 8, 1, 2),
    _WaterSensorSerial_Type()
)
waterSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterSensorSerial.setStatus("current")
_WaterSensorName_Type = DisplayString
_WaterSensorName_Object = MibTableColumn
waterSensorName = _WaterSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 8, 1, 3),
    _WaterSensorName_Type()
)
waterSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterSensorName.setStatus("current")
_WaterSensorAvail_Type = Gauge32
_WaterSensorAvail_Object = MibTableColumn
waterSensorAvail = _WaterSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 8, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 8, 1, 5),
    _WaterSensorDampness_Type()
)
waterSensorDampness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterSensorDampness.setStatus("current")
_CurrentMonitorTable_Object = MibTable
currentMonitorTable = _CurrentMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 9)
)
if mibBuilder.loadTexts:
    currentMonitorTable.setStatus("current")
_CurrentMonitorEntry_Object = MibTableRow
currentMonitorEntry = _CurrentMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 9, 1)
)
currentMonitorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "currentMonitorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 9, 1, 1),
    _CurrentMonitorIndex_Type()
)
currentMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorIndex.setStatus("current")
_CurrentMonitorSerial_Type = DisplayString
_CurrentMonitorSerial_Object = MibTableColumn
currentMonitorSerial = _CurrentMonitorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 9, 1, 2),
    _CurrentMonitorSerial_Type()
)
currentMonitorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorSerial.setStatus("current")
_CurrentMonitorName_Type = DisplayString
_CurrentMonitorName_Object = MibTableColumn
currentMonitorName = _CurrentMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 9, 1, 3),
    _CurrentMonitorName_Type()
)
currentMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorName.setStatus("current")
_CurrentMonitorAvail_Type = Gauge32
_CurrentMonitorAvail_Object = MibTableColumn
currentMonitorAvail = _CurrentMonitorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 9, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 9, 1, 5),
    _CurrentMonitorDeciAmps_Type()
)
currentMonitorDeciAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorDeciAmps.setStatus("current")
if mibBuilder.loadTexts:
    currentMonitorDeciAmps.setUnits("0.1 Amps")
_MillivoltMonitorTable_Object = MibTable
millivoltMonitorTable = _MillivoltMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 10)
)
if mibBuilder.loadTexts:
    millivoltMonitorTable.setStatus("current")
_MillivoltMonitorEntry_Object = MibTableRow
millivoltMonitorEntry = _MillivoltMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 10, 1)
)
millivoltMonitorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "millivoltMonitorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 10, 1, 1),
    _MillivoltMonitorIndex_Type()
)
millivoltMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    millivoltMonitorIndex.setStatus("current")
_MillivoltMonitorSerial_Type = DisplayString
_MillivoltMonitorSerial_Object = MibTableColumn
millivoltMonitorSerial = _MillivoltMonitorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 10, 1, 2),
    _MillivoltMonitorSerial_Type()
)
millivoltMonitorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    millivoltMonitorSerial.setStatus("current")
_MillivoltMonitorName_Type = DisplayString
_MillivoltMonitorName_Object = MibTableColumn
millivoltMonitorName = _MillivoltMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 10, 1, 3),
    _MillivoltMonitorName_Type()
)
millivoltMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    millivoltMonitorName.setStatus("current")
_MillivoltMonitorAvail_Type = Gauge32
_MillivoltMonitorAvail_Object = MibTableColumn
millivoltMonitorAvail = _MillivoltMonitorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 10, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 10, 1, 5),
    _MillivoltMonitorMV_Type()
)
millivoltMonitorMV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    millivoltMonitorMV.setStatus("current")
if mibBuilder.loadTexts:
    millivoltMonitorMV.setUnits("millivolts")
_Pow3ChTable_Object = MibTable
pow3ChTable = _Pow3ChTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11)
)
if mibBuilder.loadTexts:
    pow3ChTable.setStatus("current")
_Pow3ChEntry_Object = MibTableRow
pow3ChEntry = _Pow3ChEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1)
)
pow3ChEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "pow3ChIndex"),
)
if mibBuilder.loadTexts:
    pow3ChEntry.setStatus("current")


class _Pow3ChIndex_Type(Integer32):
    """Custom type pow3ChIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Pow3ChIndex_Type.__name__ = "Integer32"
_Pow3ChIndex_Object = MibTableColumn
pow3ChIndex = _Pow3ChIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 1),
    _Pow3ChIndex_Type()
)
pow3ChIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pow3ChIndex.setStatus("current")
_Pow3ChSerial_Type = DisplayString
_Pow3ChSerial_Object = MibTableColumn
pow3ChSerial = _Pow3ChSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 2),
    _Pow3ChSerial_Type()
)
pow3ChSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChSerial.setStatus("current")
_Pow3ChName_Type = DisplayString
_Pow3ChName_Object = MibTableColumn
pow3ChName = _Pow3ChName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 3),
    _Pow3ChName_Type()
)
pow3ChName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChName.setStatus("current")
_Pow3ChAvail_Type = Gauge32
_Pow3ChAvail_Object = MibTableColumn
pow3ChAvail = _Pow3ChAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 4),
    _Pow3ChAvail_Type()
)
pow3ChAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChAvail.setStatus("current")
_Pow3ChkWattHrsA_Type = Gauge32
_Pow3ChkWattHrsA_Object = MibTableColumn
pow3ChkWattHrsA = _Pow3ChkWattHrsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 5),
    _Pow3ChkWattHrsA_Type()
)
pow3ChkWattHrsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChkWattHrsA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChkWattHrsA.setUnits("kWh")
_Pow3ChVoltsA_Type = Gauge32
_Pow3ChVoltsA_Object = MibTableColumn
pow3ChVoltsA = _Pow3ChVoltsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 6),
    _Pow3ChVoltsA_Type()
)
pow3ChVoltsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltsA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltsA.setUnits("Volts (rms)")
_Pow3ChVoltMaxA_Type = Gauge32
_Pow3ChVoltMaxA_Object = MibTableColumn
pow3ChVoltMaxA = _Pow3ChVoltMaxA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 7),
    _Pow3ChVoltMaxA_Type()
)
pow3ChVoltMaxA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltMaxA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltMaxA.setUnits("Volts (rms)")
_Pow3ChVoltMinA_Type = Gauge32
_Pow3ChVoltMinA_Object = MibTableColumn
pow3ChVoltMinA = _Pow3ChVoltMinA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 8),
    _Pow3ChVoltMinA_Type()
)
pow3ChVoltMinA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltMinA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltMinA.setUnits("Volts (rms)")
_Pow3ChVoltPeakA_Type = Gauge32
_Pow3ChVoltPeakA_Object = MibTableColumn
pow3ChVoltPeakA = _Pow3ChVoltPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 9),
    _Pow3ChVoltPeakA_Type()
)
pow3ChVoltPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltPeakA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltPeakA.setUnits("Volts")
_Pow3ChDeciAmpsA_Type = Gauge32
_Pow3ChDeciAmpsA_Object = MibTableColumn
pow3ChDeciAmpsA = _Pow3ChDeciAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 10),
    _Pow3ChDeciAmpsA_Type()
)
pow3ChDeciAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChDeciAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChDeciAmpsA.setUnits("0.1 Amps (rms)")
_Pow3ChRealPowerA_Type = Gauge32
_Pow3ChRealPowerA_Object = MibTableColumn
pow3ChRealPowerA = _Pow3ChRealPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 11),
    _Pow3ChRealPowerA_Type()
)
pow3ChRealPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChRealPowerA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChRealPowerA.setUnits("Watts")
_Pow3ChApparentPowerA_Type = Gauge32
_Pow3ChApparentPowerA_Object = MibTableColumn
pow3ChApparentPowerA = _Pow3ChApparentPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 13),
    _Pow3ChPowerFactorA_Type()
)
pow3ChPowerFactorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChPowerFactorA.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChPowerFactorA.setUnits("%")
_Pow3ChkWattHrsB_Type = Gauge32
_Pow3ChkWattHrsB_Object = MibTableColumn
pow3ChkWattHrsB = _Pow3ChkWattHrsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 14),
    _Pow3ChkWattHrsB_Type()
)
pow3ChkWattHrsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChkWattHrsB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChkWattHrsB.setUnits("kWh")
_Pow3ChVoltsB_Type = Gauge32
_Pow3ChVoltsB_Object = MibTableColumn
pow3ChVoltsB = _Pow3ChVoltsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 15),
    _Pow3ChVoltsB_Type()
)
pow3ChVoltsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltsB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltsB.setUnits("Volts (rms)")
_Pow3ChVoltMaxB_Type = Gauge32
_Pow3ChVoltMaxB_Object = MibTableColumn
pow3ChVoltMaxB = _Pow3ChVoltMaxB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 16),
    _Pow3ChVoltMaxB_Type()
)
pow3ChVoltMaxB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltMaxB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltMaxB.setUnits("Volts (rms)")
_Pow3ChVoltMinB_Type = Gauge32
_Pow3ChVoltMinB_Object = MibTableColumn
pow3ChVoltMinB = _Pow3ChVoltMinB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 17),
    _Pow3ChVoltMinB_Type()
)
pow3ChVoltMinB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltMinB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltMinB.setUnits("Volts (rms)")
_Pow3ChVoltPeakB_Type = Gauge32
_Pow3ChVoltPeakB_Object = MibTableColumn
pow3ChVoltPeakB = _Pow3ChVoltPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 18),
    _Pow3ChVoltPeakB_Type()
)
pow3ChVoltPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltPeakB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltPeakB.setUnits("Volts")
_Pow3ChDeciAmpsB_Type = Gauge32
_Pow3ChDeciAmpsB_Object = MibTableColumn
pow3ChDeciAmpsB = _Pow3ChDeciAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 19),
    _Pow3ChDeciAmpsB_Type()
)
pow3ChDeciAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChDeciAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChDeciAmpsB.setUnits("0.1 Amps (rms)")
_Pow3ChRealPowerB_Type = Gauge32
_Pow3ChRealPowerB_Object = MibTableColumn
pow3ChRealPowerB = _Pow3ChRealPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 20),
    _Pow3ChRealPowerB_Type()
)
pow3ChRealPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChRealPowerB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChRealPowerB.setUnits("Watts")
_Pow3ChApparentPowerB_Type = Gauge32
_Pow3ChApparentPowerB_Object = MibTableColumn
pow3ChApparentPowerB = _Pow3ChApparentPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 22),
    _Pow3ChPowerFactorB_Type()
)
pow3ChPowerFactorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChPowerFactorB.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChPowerFactorB.setUnits("%")
_Pow3ChkWattHrsC_Type = Gauge32
_Pow3ChkWattHrsC_Object = MibTableColumn
pow3ChkWattHrsC = _Pow3ChkWattHrsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 23),
    _Pow3ChkWattHrsC_Type()
)
pow3ChkWattHrsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChkWattHrsC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChkWattHrsC.setUnits("kWh")
_Pow3ChVoltsC_Type = Gauge32
_Pow3ChVoltsC_Object = MibTableColumn
pow3ChVoltsC = _Pow3ChVoltsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 24),
    _Pow3ChVoltsC_Type()
)
pow3ChVoltsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltsC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltsC.setUnits("Volts (rms)")
_Pow3ChVoltMaxC_Type = Gauge32
_Pow3ChVoltMaxC_Object = MibTableColumn
pow3ChVoltMaxC = _Pow3ChVoltMaxC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 25),
    _Pow3ChVoltMaxC_Type()
)
pow3ChVoltMaxC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltMaxC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltMaxC.setUnits("Volts (rms)")
_Pow3ChVoltMinC_Type = Gauge32
_Pow3ChVoltMinC_Object = MibTableColumn
pow3ChVoltMinC = _Pow3ChVoltMinC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 26),
    _Pow3ChVoltMinC_Type()
)
pow3ChVoltMinC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltMinC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltMinC.setUnits("Volts (rms)")
_Pow3ChVoltPeakC_Type = Gauge32
_Pow3ChVoltPeakC_Object = MibTableColumn
pow3ChVoltPeakC = _Pow3ChVoltPeakC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 27),
    _Pow3ChVoltPeakC_Type()
)
pow3ChVoltPeakC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChVoltPeakC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChVoltPeakC.setUnits("Volts")
_Pow3ChDeciAmpsC_Type = Gauge32
_Pow3ChDeciAmpsC_Object = MibTableColumn
pow3ChDeciAmpsC = _Pow3ChDeciAmpsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 28),
    _Pow3ChDeciAmpsC_Type()
)
pow3ChDeciAmpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChDeciAmpsC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChDeciAmpsC.setUnits("0.1 Amps (rms)")
_Pow3ChRealPowerC_Type = Gauge32
_Pow3ChRealPowerC_Object = MibTableColumn
pow3ChRealPowerC = _Pow3ChRealPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 29),
    _Pow3ChRealPowerC_Type()
)
pow3ChRealPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChRealPowerC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChRealPowerC.setUnits("Watts")
_Pow3ChApparentPowerC_Type = Gauge32
_Pow3ChApparentPowerC_Object = MibTableColumn
pow3ChApparentPowerC = _Pow3ChApparentPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 30),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 31),
    _Pow3ChPowerFactorC_Type()
)
pow3ChPowerFactorC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChPowerFactorC.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChPowerFactorC.setUnits("%")
_Pow3ChkWattHrsTotal_Type = Gauge32
_Pow3ChkWattHrsTotal_Object = MibTableColumn
pow3ChkWattHrsTotal = _Pow3ChkWattHrsTotal_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 32),
    _Pow3ChkWattHrsTotal_Type()
)
pow3ChkWattHrsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChkWattHrsTotal.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChkWattHrsTotal.setUnits("kWh")
_Pow3ChRealPowerTotal_Type = Gauge32
_Pow3ChRealPowerTotal_Object = MibTableColumn
pow3ChRealPowerTotal = _Pow3ChRealPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 11, 1, 33),
    _Pow3ChRealPowerTotal_Type()
)
pow3ChRealPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pow3ChRealPowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    pow3ChRealPowerTotal.setUnits("Watts")
_OutletTable_Object = MibTable
outletTable = _OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 12)
)
if mibBuilder.loadTexts:
    outletTable.setStatus("current")
_OutletEntry_Object = MibTableRow
outletEntry = _OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 12, 1)
)
outletEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "outletIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 12, 1, 1),
    _OutletIndex_Type()
)
outletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outletIndex.setStatus("current")
_OutletSerial_Type = DisplayString
_OutletSerial_Object = MibTableColumn
outletSerial = _OutletSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 12, 1, 2),
    _OutletSerial_Type()
)
outletSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSerial.setStatus("current")
_OutletName_Type = DisplayString
_OutletName_Object = MibTableColumn
outletName = _OutletName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 12, 1, 3),
    _OutletName_Type()
)
outletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletName.setStatus("current")
_OutletAvail_Type = Gauge32
_OutletAvail_Object = MibTableColumn
outletAvail = _OutletAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 12, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 12, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 12, 1, 6),
    _Outlet2Status_Type()
)
outlet2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet2Status.setStatus("current")
_VsfcTable_Object = MibTable
vsfcTable = _VsfcTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13)
)
if mibBuilder.loadTexts:
    vsfcTable.setStatus("current")
_VsfcEntry_Object = MibTableRow
vsfcEntry = _VsfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1)
)
vsfcEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "vsfcIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 1),
    _VsfcIndex_Type()
)
vsfcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsfcIndex.setStatus("current")
_VsfcSerial_Type = DisplayString
_VsfcSerial_Object = MibTableColumn
vsfcSerial = _VsfcSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 2),
    _VsfcSerial_Type()
)
vsfcSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcSerial.setStatus("current")
_VsfcName_Type = DisplayString
_VsfcName_Object = MibTableColumn
vsfcName = _VsfcName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 3),
    _VsfcName_Type()
)
vsfcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcName.setStatus("current")
_VsfcAvail_Type = Gauge32
_VsfcAvail_Object = MibTableColumn
vsfcAvail = _VsfcAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 5),
    _VsfcSetPointC_Type()
)
vsfcSetPointC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcSetPointC.setStatus("current")
if mibBuilder.loadTexts:
    vsfcSetPointC.setUnits("Degrees Celsius")


class _VsfcSetPointF_Type(Integer32):
    """Custom type vsfcSetPointF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65, 100),
    )


_VsfcSetPointF_Type.__name__ = "Integer32"
_VsfcSetPointF_Object = MibTableColumn
vsfcSetPointF = _VsfcSetPointF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 6),
    _VsfcSetPointF_Type()
)
vsfcSetPointF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcSetPointF.setStatus("current")
if mibBuilder.loadTexts:
    vsfcSetPointF.setUnits("Degrees Fahrenheit")


class _VsfcFanSpeed_Type(Integer32):
    """Custom type vsfcFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VsfcFanSpeed_Type.__name__ = "Integer32"
_VsfcFanSpeed_Object = MibTableColumn
vsfcFanSpeed = _VsfcFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 7),
    _VsfcFanSpeed_Type()
)
vsfcFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    vsfcFanSpeed.setUnits("%")


class _VsfcIntTempC_Type(Integer32):
    """Custom type vsfcIntTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 50),
    )


_VsfcIntTempC_Type.__name__ = "Integer32"
_VsfcIntTempC_Object = MibTableColumn
vsfcIntTempC = _VsfcIntTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 8),
    _VsfcIntTempC_Type()
)
vsfcIntTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcIntTempC.setStatus("current")
if mibBuilder.loadTexts:
    vsfcIntTempC.setUnits("Degrees Celsius")


class _VsfcIntTempF_Type(Integer32):
    """Custom type vsfcIntTempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4, 122),
    )


_VsfcIntTempF_Type.__name__ = "Integer32"
_VsfcIntTempF_Object = MibTableColumn
vsfcIntTempF = _VsfcIntTempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 9),
    _VsfcIntTempF_Type()
)
vsfcIntTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcIntTempF.setStatus("current")
if mibBuilder.loadTexts:
    vsfcIntTempF.setUnits("Degrees Fahrenheit")


class _VsfcExt1TempC_Type(Integer32):
    """Custom type vsfcExt1TempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 50),
    )


_VsfcExt1TempC_Type.__name__ = "Integer32"
_VsfcExt1TempC_Object = MibTableColumn
vsfcExt1TempC = _VsfcExt1TempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 10),
    _VsfcExt1TempC_Type()
)
vsfcExt1TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcExt1TempC.setStatus("current")
if mibBuilder.loadTexts:
    vsfcExt1TempC.setUnits("Degrees Celsius")


class _VsfcExt1TempF_Type(Integer32):
    """Custom type vsfcExt1TempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 122),
    )


_VsfcExt1TempF_Type.__name__ = "Integer32"
_VsfcExt1TempF_Object = MibTableColumn
vsfcExt1TempF = _VsfcExt1TempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 11),
    _VsfcExt1TempF_Type()
)
vsfcExt1TempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcExt1TempF.setStatus("current")
if mibBuilder.loadTexts:
    vsfcExt1TempF.setUnits("Degrees Fahrenheit")


class _VsfcExt2TempC_Type(Integer32):
    """Custom type vsfcExt2TempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 50),
    )


_VsfcExt2TempC_Type.__name__ = "Integer32"
_VsfcExt2TempC_Object = MibTableColumn
vsfcExt2TempC = _VsfcExt2TempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 12),
    _VsfcExt2TempC_Type()
)
vsfcExt2TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcExt2TempC.setStatus("current")
if mibBuilder.loadTexts:
    vsfcExt2TempC.setUnits("Degrees Celsius")


class _VsfcExt2TempF_Type(Integer32):
    """Custom type vsfcExt2TempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 122),
    )


_VsfcExt2TempF_Type.__name__ = "Integer32"
_VsfcExt2TempF_Object = MibTableColumn
vsfcExt2TempF = _VsfcExt2TempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 13),
    _VsfcExt2TempF_Type()
)
vsfcExt2TempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcExt2TempF.setStatus("current")
if mibBuilder.loadTexts:
    vsfcExt2TempF.setUnits("Degrees Fahrenheit")


class _VsfcExt3TempC_Type(Integer32):
    """Custom type vsfcExt3TempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 50),
    )


_VsfcExt3TempC_Type.__name__ = "Integer32"
_VsfcExt3TempC_Object = MibTableColumn
vsfcExt3TempC = _VsfcExt3TempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 14),
    _VsfcExt3TempC_Type()
)
vsfcExt3TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcExt3TempC.setStatus("current")
if mibBuilder.loadTexts:
    vsfcExt3TempC.setUnits("Degrees Celsius")


class _VsfcExt3TempF_Type(Integer32):
    """Custom type vsfcExt3TempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 122),
    )


_VsfcExt3TempF_Type.__name__ = "Integer32"
_VsfcExt3TempF_Object = MibTableColumn
vsfcExt3TempF = _VsfcExt3TempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 15),
    _VsfcExt3TempF_Type()
)
vsfcExt3TempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcExt3TempF.setStatus("current")
if mibBuilder.loadTexts:
    vsfcExt3TempF.setUnits("Degrees Fahrenheit")


class _VsfcExt4TempC_Type(Integer32):
    """Custom type vsfcExt4TempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 50),
    )


_VsfcExt4TempC_Type.__name__ = "Integer32"
_VsfcExt4TempC_Object = MibTableColumn
vsfcExt4TempC = _VsfcExt4TempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 16),
    _VsfcExt4TempC_Type()
)
vsfcExt4TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcExt4TempC.setStatus("current")
if mibBuilder.loadTexts:
    vsfcExt4TempC.setUnits("Degrees Celsius")


class _VsfcExt4TempF_Type(Integer32):
    """Custom type vsfcExt4TempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 122),
    )


_VsfcExt4TempF_Type.__name__ = "Integer32"
_VsfcExt4TempF_Object = MibTableColumn
vsfcExt4TempF = _VsfcExt4TempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 13, 1, 17),
    _VsfcExt4TempF_Type()
)
vsfcExt4TempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsfcExt4TempF.setStatus("current")
if mibBuilder.loadTexts:
    vsfcExt4TempF.setUnits("Degrees Fahrenheit")
_Ctrl3ChTable_Object = MibTable
ctrl3ChTable = _Ctrl3ChTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14)
)
if mibBuilder.loadTexts:
    ctrl3ChTable.setStatus("current")
_Ctrl3ChEntry_Object = MibTableRow
ctrl3ChEntry = _Ctrl3ChEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1)
)
ctrl3ChEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "ctrl3ChIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 1),
    _Ctrl3ChIndex_Type()
)
ctrl3ChIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrl3ChIndex.setStatus("current")
_Ctrl3ChSerial_Type = DisplayString
_Ctrl3ChSerial_Object = MibTableColumn
ctrl3ChSerial = _Ctrl3ChSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 2),
    _Ctrl3ChSerial_Type()
)
ctrl3ChSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChSerial.setStatus("current")
_Ctrl3ChName_Type = DisplayString
_Ctrl3ChName_Object = MibTableColumn
ctrl3ChName = _Ctrl3ChName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 3),
    _Ctrl3ChName_Type()
)
ctrl3ChName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChName.setStatus("current")
_Ctrl3ChAvail_Type = Gauge32
_Ctrl3ChAvail_Object = MibTableColumn
ctrl3ChAvail = _Ctrl3ChAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 4),
    _Ctrl3ChAvail_Type()
)
ctrl3ChAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChAvail.setStatus("current")
_Ctrl3ChVoltsA_Type = Gauge32
_Ctrl3ChVoltsA_Object = MibTableColumn
ctrl3ChVoltsA = _Ctrl3ChVoltsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 5),
    _Ctrl3ChVoltsA_Type()
)
ctrl3ChVoltsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChVoltsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChVoltsA.setUnits("Volts (rms)")
_Ctrl3ChVoltPeakA_Type = Gauge32
_Ctrl3ChVoltPeakA_Object = MibTableColumn
ctrl3ChVoltPeakA = _Ctrl3ChVoltPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 6),
    _Ctrl3ChVoltPeakA_Type()
)
ctrl3ChVoltPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChVoltPeakA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChVoltPeakA.setUnits("Volts (rms)")
_Ctrl3ChDeciAmpsA_Type = Gauge32
_Ctrl3ChDeciAmpsA_Object = MibTableColumn
ctrl3ChDeciAmpsA = _Ctrl3ChDeciAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 7),
    _Ctrl3ChDeciAmpsA_Type()
)
ctrl3ChDeciAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsA.setUnits("0.1 Amps (rms)")
_Ctrl3ChDeciAmpsPeakA_Type = Gauge32
_Ctrl3ChDeciAmpsPeakA_Object = MibTableColumn
ctrl3ChDeciAmpsPeakA = _Ctrl3ChDeciAmpsPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 8),
    _Ctrl3ChDeciAmpsPeakA_Type()
)
ctrl3ChDeciAmpsPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsPeakA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsPeakA.setUnits("0.1 Amps (rms)")
_Ctrl3ChRealPowerA_Type = Gauge32
_Ctrl3ChRealPowerA_Object = MibTableColumn
ctrl3ChRealPowerA = _Ctrl3ChRealPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 9),
    _Ctrl3ChRealPowerA_Type()
)
ctrl3ChRealPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChRealPowerA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChRealPowerA.setUnits("Watts")
_Ctrl3ChApparentPowerA_Type = Gauge32
_Ctrl3ChApparentPowerA_Object = MibTableColumn
ctrl3ChApparentPowerA = _Ctrl3ChApparentPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 11),
    _Ctrl3ChPowerFactorA_Type()
)
ctrl3ChPowerFactorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChPowerFactorA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChPowerFactorA.setUnits("%")
_Ctrl3ChVoltsB_Type = Gauge32
_Ctrl3ChVoltsB_Object = MibTableColumn
ctrl3ChVoltsB = _Ctrl3ChVoltsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 12),
    _Ctrl3ChVoltsB_Type()
)
ctrl3ChVoltsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChVoltsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChVoltsB.setUnits("Volts (rms)")
_Ctrl3ChVoltPeakB_Type = Gauge32
_Ctrl3ChVoltPeakB_Object = MibTableColumn
ctrl3ChVoltPeakB = _Ctrl3ChVoltPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 13),
    _Ctrl3ChVoltPeakB_Type()
)
ctrl3ChVoltPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChVoltPeakB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChVoltPeakB.setUnits("Volts (rms)")
_Ctrl3ChDeciAmpsB_Type = Gauge32
_Ctrl3ChDeciAmpsB_Object = MibTableColumn
ctrl3ChDeciAmpsB = _Ctrl3ChDeciAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 14),
    _Ctrl3ChDeciAmpsB_Type()
)
ctrl3ChDeciAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsB.setUnits("0.1 Amps (rms)")
_Ctrl3ChDeciAmpsPeakB_Type = Gauge32
_Ctrl3ChDeciAmpsPeakB_Object = MibTableColumn
ctrl3ChDeciAmpsPeakB = _Ctrl3ChDeciAmpsPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 15),
    _Ctrl3ChDeciAmpsPeakB_Type()
)
ctrl3ChDeciAmpsPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsPeakB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsPeakB.setUnits("0.1 Amps (rms)")
_Ctrl3ChRealPowerB_Type = Gauge32
_Ctrl3ChRealPowerB_Object = MibTableColumn
ctrl3ChRealPowerB = _Ctrl3ChRealPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 16),
    _Ctrl3ChRealPowerB_Type()
)
ctrl3ChRealPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChRealPowerB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChRealPowerB.setUnits("Watts")
_Ctrl3ChApparentPowerB_Type = Gauge32
_Ctrl3ChApparentPowerB_Object = MibTableColumn
ctrl3ChApparentPowerB = _Ctrl3ChApparentPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 18),
    _Ctrl3ChPowerFactorB_Type()
)
ctrl3ChPowerFactorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChPowerFactorB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChPowerFactorB.setUnits("%")
_Ctrl3ChVoltsC_Type = Gauge32
_Ctrl3ChVoltsC_Object = MibTableColumn
ctrl3ChVoltsC = _Ctrl3ChVoltsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 19),
    _Ctrl3ChVoltsC_Type()
)
ctrl3ChVoltsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChVoltsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChVoltsC.setUnits("Volts (rms)")
_Ctrl3ChVoltPeakC_Type = Gauge32
_Ctrl3ChVoltPeakC_Object = MibTableColumn
ctrl3ChVoltPeakC = _Ctrl3ChVoltPeakC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 20),
    _Ctrl3ChVoltPeakC_Type()
)
ctrl3ChVoltPeakC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChVoltPeakC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChVoltPeakC.setUnits("Volts (rms)")
_Ctrl3ChDeciAmpsC_Type = Gauge32
_Ctrl3ChDeciAmpsC_Object = MibTableColumn
ctrl3ChDeciAmpsC = _Ctrl3ChDeciAmpsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 21),
    _Ctrl3ChDeciAmpsC_Type()
)
ctrl3ChDeciAmpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsC.setUnits("0.1 Amps (rms)")
_Ctrl3ChDeciAmpsPeakC_Type = Gauge32
_Ctrl3ChDeciAmpsPeakC_Object = MibTableColumn
ctrl3ChDeciAmpsPeakC = _Ctrl3ChDeciAmpsPeakC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 22),
    _Ctrl3ChDeciAmpsPeakC_Type()
)
ctrl3ChDeciAmpsPeakC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsPeakC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChDeciAmpsPeakC.setUnits("0.1 Amps (rms)")
_Ctrl3ChRealPowerC_Type = Gauge32
_Ctrl3ChRealPowerC_Object = MibTableColumn
ctrl3ChRealPowerC = _Ctrl3ChRealPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 23),
    _Ctrl3ChRealPowerC_Type()
)
ctrl3ChRealPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChRealPowerC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChRealPowerC.setUnits("Watts")
_Ctrl3ChApparentPowerC_Type = Gauge32
_Ctrl3ChApparentPowerC_Object = MibTableColumn
ctrl3ChApparentPowerC = _Ctrl3ChApparentPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 14, 1, 25),
    _Ctrl3ChPowerFactorC_Type()
)
ctrl3ChPowerFactorC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChPowerFactorC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChPowerFactorC.setUnits("%")
_CtrlGrpAmpsTable_Object = MibTable
ctrlGrpAmpsTable = _CtrlGrpAmpsTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15)
)
if mibBuilder.loadTexts:
    ctrlGrpAmpsTable.setStatus("current")
_CtrlGrpAmpsEntry_Object = MibTableRow
ctrlGrpAmpsEntry = _CtrlGrpAmpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1)
)
ctrlGrpAmpsEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "ctrlGrpAmpsIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 1),
    _CtrlGrpAmpsIndex_Type()
)
ctrlGrpAmpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrlGrpAmpsIndex.setStatus("current")
_CtrlGrpAmpsSerial_Type = DisplayString
_CtrlGrpAmpsSerial_Object = MibTableColumn
ctrlGrpAmpsSerial = _CtrlGrpAmpsSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 2),
    _CtrlGrpAmpsSerial_Type()
)
ctrlGrpAmpsSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsSerial.setStatus("current")
_CtrlGrpAmpsName_Type = DisplayString
_CtrlGrpAmpsName_Object = MibTableColumn
ctrlGrpAmpsName = _CtrlGrpAmpsName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 3),
    _CtrlGrpAmpsName_Type()
)
ctrlGrpAmpsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsName.setStatus("current")
_CtrlGrpAmpsAvail_Type = Gauge32
_CtrlGrpAmpsAvail_Object = MibTableColumn
ctrlGrpAmpsAvail = _CtrlGrpAmpsAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 4),
    _CtrlGrpAmpsAvail_Type()
)
ctrlGrpAmpsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsAvail.setStatus("current")
_CtrlGrpAmpsA_Type = Gauge32
_CtrlGrpAmpsA_Object = MibTableColumn
ctrlGrpAmpsA = _CtrlGrpAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 5),
    _CtrlGrpAmpsA_Type()
)
ctrlGrpAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsA.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsB_Type = Gauge32
_CtrlGrpAmpsB_Object = MibTableColumn
ctrlGrpAmpsB = _CtrlGrpAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 6),
    _CtrlGrpAmpsB_Type()
)
ctrlGrpAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsB.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsC_Type = Gauge32
_CtrlGrpAmpsC_Object = MibTableColumn
ctrlGrpAmpsC = _CtrlGrpAmpsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 7),
    _CtrlGrpAmpsC_Type()
)
ctrlGrpAmpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsC.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsD_Type = Gauge32
_CtrlGrpAmpsD_Object = MibTableColumn
ctrlGrpAmpsD = _CtrlGrpAmpsD_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 8),
    _CtrlGrpAmpsD_Type()
)
ctrlGrpAmpsD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsD.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsD.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsE_Type = Gauge32
_CtrlGrpAmpsE_Object = MibTableColumn
ctrlGrpAmpsE = _CtrlGrpAmpsE_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 9),
    _CtrlGrpAmpsE_Type()
)
ctrlGrpAmpsE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsE.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsE.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsF_Type = Gauge32
_CtrlGrpAmpsF_Object = MibTableColumn
ctrlGrpAmpsF = _CtrlGrpAmpsF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 10),
    _CtrlGrpAmpsF_Type()
)
ctrlGrpAmpsF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsF.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsF.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsG_Type = Gauge32
_CtrlGrpAmpsG_Object = MibTableColumn
ctrlGrpAmpsG = _CtrlGrpAmpsG_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 11),
    _CtrlGrpAmpsG_Type()
)
ctrlGrpAmpsG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsG.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsG.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsH_Type = Gauge32
_CtrlGrpAmpsH_Object = MibTableColumn
ctrlGrpAmpsH = _CtrlGrpAmpsH_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 12),
    _CtrlGrpAmpsH_Type()
)
ctrlGrpAmpsH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsH.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsH.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsAVolts_Type = Gauge32
_CtrlGrpAmpsAVolts_Object = MibTableColumn
ctrlGrpAmpsAVolts = _CtrlGrpAmpsAVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 13),
    _CtrlGrpAmpsAVolts_Type()
)
ctrlGrpAmpsAVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsAVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsAVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsBVolts_Type = Gauge32
_CtrlGrpAmpsBVolts_Object = MibTableColumn
ctrlGrpAmpsBVolts = _CtrlGrpAmpsBVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 14),
    _CtrlGrpAmpsBVolts_Type()
)
ctrlGrpAmpsBVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsBVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsBVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsCVolts_Type = Gauge32
_CtrlGrpAmpsCVolts_Object = MibTableColumn
ctrlGrpAmpsCVolts = _CtrlGrpAmpsCVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 15),
    _CtrlGrpAmpsCVolts_Type()
)
ctrlGrpAmpsCVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsCVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsCVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsDVolts_Type = Gauge32
_CtrlGrpAmpsDVolts_Object = MibTableColumn
ctrlGrpAmpsDVolts = _CtrlGrpAmpsDVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 16),
    _CtrlGrpAmpsDVolts_Type()
)
ctrlGrpAmpsDVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsDVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsDVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsEVolts_Type = Gauge32
_CtrlGrpAmpsEVolts_Object = MibTableColumn
ctrlGrpAmpsEVolts = _CtrlGrpAmpsEVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 17),
    _CtrlGrpAmpsEVolts_Type()
)
ctrlGrpAmpsEVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsEVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsEVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsFVolts_Type = Gauge32
_CtrlGrpAmpsFVolts_Object = MibTableColumn
ctrlGrpAmpsFVolts = _CtrlGrpAmpsFVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 18),
    _CtrlGrpAmpsFVolts_Type()
)
ctrlGrpAmpsFVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsFVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsFVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsGVolts_Type = Gauge32
_CtrlGrpAmpsGVolts_Object = MibTableColumn
ctrlGrpAmpsGVolts = _CtrlGrpAmpsGVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 19),
    _CtrlGrpAmpsGVolts_Type()
)
ctrlGrpAmpsGVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsGVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsGVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsHVolts_Type = Gauge32
_CtrlGrpAmpsHVolts_Object = MibTableColumn
ctrlGrpAmpsHVolts = _CtrlGrpAmpsHVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 20),
    _CtrlGrpAmpsHVolts_Type()
)
ctrlGrpAmpsHVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsHVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsHVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsI_Type = Gauge32
_CtrlGrpAmpsI_Object = MibTableColumn
ctrlGrpAmpsI = _CtrlGrpAmpsI_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 21),
    _CtrlGrpAmpsI_Type()
)
ctrlGrpAmpsI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsI.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsI.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsJ_Type = Gauge32
_CtrlGrpAmpsJ_Object = MibTableColumn
ctrlGrpAmpsJ = _CtrlGrpAmpsJ_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 22),
    _CtrlGrpAmpsJ_Type()
)
ctrlGrpAmpsJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsJ.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsJ.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsK_Type = Gauge32
_CtrlGrpAmpsK_Object = MibTableColumn
ctrlGrpAmpsK = _CtrlGrpAmpsK_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 23),
    _CtrlGrpAmpsK_Type()
)
ctrlGrpAmpsK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsK.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsK.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsL_Type = Gauge32
_CtrlGrpAmpsL_Object = MibTableColumn
ctrlGrpAmpsL = _CtrlGrpAmpsL_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 24),
    _CtrlGrpAmpsL_Type()
)
ctrlGrpAmpsL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsL.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsL.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsM_Type = Gauge32
_CtrlGrpAmpsM_Object = MibTableColumn
ctrlGrpAmpsM = _CtrlGrpAmpsM_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 25),
    _CtrlGrpAmpsM_Type()
)
ctrlGrpAmpsM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsM.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsM.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsN_Type = Gauge32
_CtrlGrpAmpsN_Object = MibTableColumn
ctrlGrpAmpsN = _CtrlGrpAmpsN_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 26),
    _CtrlGrpAmpsN_Type()
)
ctrlGrpAmpsN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsN.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsN.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsO_Type = Gauge32
_CtrlGrpAmpsO_Object = MibTableColumn
ctrlGrpAmpsO = _CtrlGrpAmpsO_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 27),
    _CtrlGrpAmpsO_Type()
)
ctrlGrpAmpsO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsO.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsO.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsP_Type = Gauge32
_CtrlGrpAmpsP_Object = MibTableColumn
ctrlGrpAmpsP = _CtrlGrpAmpsP_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 28),
    _CtrlGrpAmpsP_Type()
)
ctrlGrpAmpsP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsP.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsP.setUnits("0.1 Amps (rms)")
_CtrlGrpAmpsIVolts_Type = Gauge32
_CtrlGrpAmpsIVolts_Object = MibTableColumn
ctrlGrpAmpsIVolts = _CtrlGrpAmpsIVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 29),
    _CtrlGrpAmpsIVolts_Type()
)
ctrlGrpAmpsIVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsIVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsIVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsJVolts_Type = Gauge32
_CtrlGrpAmpsJVolts_Object = MibTableColumn
ctrlGrpAmpsJVolts = _CtrlGrpAmpsJVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 30),
    _CtrlGrpAmpsJVolts_Type()
)
ctrlGrpAmpsJVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsJVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsJVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsKVolts_Type = Gauge32
_CtrlGrpAmpsKVolts_Object = MibTableColumn
ctrlGrpAmpsKVolts = _CtrlGrpAmpsKVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 31),
    _CtrlGrpAmpsKVolts_Type()
)
ctrlGrpAmpsKVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsKVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsKVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsLVolts_Type = Gauge32
_CtrlGrpAmpsLVolts_Object = MibTableColumn
ctrlGrpAmpsLVolts = _CtrlGrpAmpsLVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 32),
    _CtrlGrpAmpsLVolts_Type()
)
ctrlGrpAmpsLVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsLVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsLVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsMVolts_Type = Gauge32
_CtrlGrpAmpsMVolts_Object = MibTableColumn
ctrlGrpAmpsMVolts = _CtrlGrpAmpsMVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 33),
    _CtrlGrpAmpsMVolts_Type()
)
ctrlGrpAmpsMVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsMVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsMVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsNVolts_Type = Gauge32
_CtrlGrpAmpsNVolts_Object = MibTableColumn
ctrlGrpAmpsNVolts = _CtrlGrpAmpsNVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 34),
    _CtrlGrpAmpsNVolts_Type()
)
ctrlGrpAmpsNVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsNVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsNVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsOVolts_Type = Gauge32
_CtrlGrpAmpsOVolts_Object = MibTableColumn
ctrlGrpAmpsOVolts = _CtrlGrpAmpsOVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 35),
    _CtrlGrpAmpsOVolts_Type()
)
ctrlGrpAmpsOVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsOVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsOVolts.setUnits("Volts (rms)")
_CtrlGrpAmpsPVolts_Type = Gauge32
_CtrlGrpAmpsPVolts_Object = MibTableColumn
ctrlGrpAmpsPVolts = _CtrlGrpAmpsPVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 15, 1, 36),
    _CtrlGrpAmpsPVolts_Type()
)
ctrlGrpAmpsPVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGrpAmpsPVolts.setStatus("current")
if mibBuilder.loadTexts:
    ctrlGrpAmpsPVolts.setUnits("Volts (rms)")
_CtrlOutletTable_Object = MibTable
ctrlOutletTable = _CtrlOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16)
)
if mibBuilder.loadTexts:
    ctrlOutletTable.setStatus("current")
_CtrlOutletEntry_Object = MibTableRow
ctrlOutletEntry = _CtrlOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1)
)
ctrlOutletEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "ctrlOutletIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 1),
    _CtrlOutletIndex_Type()
)
ctrlOutletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrlOutletIndex.setStatus("current")
_CtrlOutletName_Type = DisplayString
_CtrlOutletName_Object = MibTableColumn
ctrlOutletName = _CtrlOutletName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 2),
    _CtrlOutletName_Type()
)
ctrlOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlOutletName.setStatus("current")
_CtrlOutletStatus_Type = Gauge32
_CtrlOutletStatus_Object = MibTableColumn
ctrlOutletStatus = _CtrlOutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 3),
    _CtrlOutletStatus_Type()
)
ctrlOutletStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlOutletStatus.setStatus("current")
_CtrlOutletFeedback_Type = Gauge32
_CtrlOutletFeedback_Object = MibTableColumn
ctrlOutletFeedback = _CtrlOutletFeedback_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 4),
    _CtrlOutletFeedback_Type()
)
ctrlOutletFeedback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletFeedback.setStatus("current")
_CtrlOutletPending_Type = Gauge32
_CtrlOutletPending_Object = MibTableColumn
ctrlOutletPending = _CtrlOutletPending_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 5),
    _CtrlOutletPending_Type()
)
ctrlOutletPending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlOutletPending.setStatus("current")
_CtrlOutletDeciAmps_Type = Gauge32
_CtrlOutletDeciAmps_Object = MibTableColumn
ctrlOutletDeciAmps = _CtrlOutletDeciAmps_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 7),
    _CtrlOutletGroup_Type()
)
ctrlOutletGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletGroup.setStatus("current")
_CtrlOutletUpDelay_Type = Gauge32
_CtrlOutletUpDelay_Object = MibTableColumn
ctrlOutletUpDelay = _CtrlOutletUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 8),
    _CtrlOutletUpDelay_Type()
)
ctrlOutletUpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlOutletUpDelay.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletUpDelay.setUnits("seconds")
_CtrlOutletDwnDelay_Type = Gauge32
_CtrlOutletDwnDelay_Object = MibTableColumn
ctrlOutletDwnDelay = _CtrlOutletDwnDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 9),
    _CtrlOutletDwnDelay_Type()
)
ctrlOutletDwnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlOutletDwnDelay.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletDwnDelay.setUnits("seconds")
_CtrlOutletRbtDuration_Type = Gauge32
_CtrlOutletRbtDuration_Object = MibTableColumn
ctrlOutletRbtDuration = _CtrlOutletRbtDuration_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 10),
    _CtrlOutletRbtDuration_Type()
)
ctrlOutletRbtDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlOutletRbtDuration.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletRbtDuration.setUnits("seconds")
_CtrlOutletURL_Type = DisplayString
_CtrlOutletURL_Object = MibTableColumn
ctrlOutletURL = _CtrlOutletURL_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 11),
    _CtrlOutletURL_Type()
)
ctrlOutletURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlOutletURL.setStatus("current")
_CtrlOutletPOAAction_Type = Gauge32
_CtrlOutletPOAAction_Object = MibTableColumn
ctrlOutletPOAAction = _CtrlOutletPOAAction_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 12),
    _CtrlOutletPOAAction_Type()
)
ctrlOutletPOAAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlOutletPOAAction.setStatus("current")
_CtrlOutletPOADelay_Type = Gauge32
_CtrlOutletPOADelay_Object = MibTableColumn
ctrlOutletPOADelay = _CtrlOutletPOADelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 13),
    _CtrlOutletPOADelay_Type()
)
ctrlOutletPOADelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlOutletPOADelay.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletPOADelay.setUnits("seconds")
_CtrlOutletkWattHrs_Type = Gauge32
_CtrlOutletkWattHrs_Object = MibTableColumn
ctrlOutletkWattHrs = _CtrlOutletkWattHrs_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 14),
    _CtrlOutletkWattHrs_Type()
)
ctrlOutletkWattHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletkWattHrs.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletkWattHrs.setUnits("kWh")
_CtrlOutletPower_Type = Gauge32
_CtrlOutletPower_Object = MibTableColumn
ctrlOutletPower = _CtrlOutletPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 15),
    _CtrlOutletPower_Type()
)
ctrlOutletPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletPower.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletPower.setUnits("Watts")
_CtrlOutletRbtDelay_Type = Gauge32
_CtrlOutletRbtDelay_Object = MibTableColumn
ctrlOutletRbtDelay = _CtrlOutletRbtDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 16),
    _CtrlOutletRbtDelay_Type()
)
ctrlOutletRbtDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlOutletRbtDelay.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletRbtDelay.setUnits("seconds")
_CtrlOutletStatusTime_Type = Gauge32
_CtrlOutletStatusTime_Object = MibTableColumn
ctrlOutletStatusTime = _CtrlOutletStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 16, 1, 17),
    _CtrlOutletStatusTime_Type()
)
ctrlOutletStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlOutletStatusTime.setStatus("current")
if mibBuilder.loadTexts:
    ctrlOutletStatusTime.setUnits("seconds")
_DewPointSensorTable_Object = MibTable
dewPointSensorTable = _DewPointSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 17)
)
if mibBuilder.loadTexts:
    dewPointSensorTable.setStatus("current")
_DewPointSensorEntry_Object = MibTableRow
dewPointSensorEntry = _DewPointSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 17, 1)
)
dewPointSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "dewPointSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 17, 1, 1),
    _DewPointSensorIndex_Type()
)
dewPointSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dewPointSensorIndex.setStatus("current")
_DewPointSensorSerial_Type = DisplayString
_DewPointSensorSerial_Object = MibTableColumn
dewPointSensorSerial = _DewPointSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 17, 1, 2),
    _DewPointSensorSerial_Type()
)
dewPointSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorSerial.setStatus("current")
_DewPointSensorName_Type = DisplayString
_DewPointSensorName_Object = MibTableColumn
dewPointSensorName = _DewPointSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 17, 1, 3),
    _DewPointSensorName_Type()
)
dewPointSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorName.setStatus("current")
_DewPointSensorAvail_Type = Gauge32
_DewPointSensorAvail_Object = MibTableColumn
dewPointSensorAvail = _DewPointSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 17, 1, 4),
    _DewPointSensorAvail_Type()
)
dewPointSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorAvail.setStatus("current")


class _DewPointSensorTempC_Type(Integer32):
    """Custom type dewPointSensorTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_DewPointSensorTempC_Type.__name__ = "Integer32"
_DewPointSensorTempC_Object = MibTableColumn
dewPointSensorTempC = _DewPointSensorTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 17, 1, 5),
    _DewPointSensorTempC_Type()
)
dewPointSensorTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorTempC.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorTempC.setUnits("Degrees Celsius")


class _DewPointSensorTempF_Type(Integer32):
    """Custom type dewPointSensorTempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_DewPointSensorTempF_Type.__name__ = "Integer32"
_DewPointSensorTempF_Object = MibTableColumn
dewPointSensorTempF = _DewPointSensorTempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 17, 1, 6),
    _DewPointSensorTempF_Type()
)
dewPointSensorTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorTempF.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorTempF.setUnits("Degrees Fahrenheit")


class _DewPointSensorHumidity_Type(Integer32):
    """Custom type dewPointSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DewPointSensorHumidity_Type.__name__ = "Integer32"
_DewPointSensorHumidity_Object = MibTableColumn
dewPointSensorHumidity = _DewPointSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 17, 1, 7),
    _DewPointSensorHumidity_Type()
)
dewPointSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorHumidity.setUnits("%")


class _DewPointSensorDewPointC_Type(Integer32):
    """Custom type dewPointSensorDewPointC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_DewPointSensorDewPointC_Type.__name__ = "Integer32"
_DewPointSensorDewPointC_Object = MibTableColumn
dewPointSensorDewPointC = _DewPointSensorDewPointC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 17, 1, 8),
    _DewPointSensorDewPointC_Type()
)
dewPointSensorDewPointC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorDewPointC.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorDewPointC.setUnits("Degrees Celsius")


class _DewPointSensorDewPointF_Type(Integer32):
    """Custom type dewPointSensorDewPointF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_DewPointSensorDewPointF_Type.__name__ = "Integer32"
_DewPointSensorDewPointF_Object = MibTableColumn
dewPointSensorDewPointF = _DewPointSensorDewPointF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 17, 1, 9),
    _DewPointSensorDewPointF_Type()
)
dewPointSensorDewPointF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorDewPointF.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorDewPointF.setUnits("Degrees Fahrenheit")
_DigitalSensorTable_Object = MibTable
digitalSensorTable = _DigitalSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 18)
)
if mibBuilder.loadTexts:
    digitalSensorTable.setStatus("current")
_DigitalSensorEntry_Object = MibTableRow
digitalSensorEntry = _DigitalSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 18, 1)
)
digitalSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "digitalSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 18, 1, 1),
    _DigitalSensorIndex_Type()
)
digitalSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digitalSensorIndex.setStatus("current")
_DigitalSensorSerial_Type = DisplayString
_DigitalSensorSerial_Object = MibTableColumn
digitalSensorSerial = _DigitalSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 18, 1, 2),
    _DigitalSensorSerial_Type()
)
digitalSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalSensorSerial.setStatus("current")
_DigitalSensorName_Type = DisplayString
_DigitalSensorName_Object = MibTableColumn
digitalSensorName = _DigitalSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 18, 1, 3),
    _DigitalSensorName_Type()
)
digitalSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalSensorName.setStatus("current")
_DigitalSensorAvail_Type = Gauge32
_DigitalSensorAvail_Object = MibTableColumn
digitalSensorAvail = _DigitalSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 18, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 18, 1, 5),
    _DigitalSensorDigital_Type()
)
digitalSensorDigital.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalSensorDigital.setStatus("current")
_DstsTable_Object = MibTable
dstsTable = _DstsTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19)
)
if mibBuilder.loadTexts:
    dstsTable.setStatus("current")
_DstsEntry_Object = MibTableRow
dstsEntry = _DstsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1)
)
dstsEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "dstsIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 1),
    _DstsIndex_Type()
)
dstsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dstsIndex.setStatus("current")
_DstsSerial_Type = DisplayString
_DstsSerial_Object = MibTableColumn
dstsSerial = _DstsSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 2),
    _DstsSerial_Type()
)
dstsSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsSerial.setStatus("current")
_DstsName_Type = DisplayString
_DstsName_Object = MibTableColumn
dstsName = _DstsName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 3),
    _DstsName_Type()
)
dstsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsName.setStatus("current")
_DstsAvail_Type = Gauge32
_DstsAvail_Object = MibTableColumn
dstsAvail = _DstsAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 4),
    _DstsAvail_Type()
)
dstsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsAvail.setStatus("current")
_DstsVoltsA_Type = Gauge32
_DstsVoltsA_Object = MibTableColumn
dstsVoltsA = _DstsVoltsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 5),
    _DstsVoltsA_Type()
)
dstsVoltsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsVoltsA.setStatus("current")
if mibBuilder.loadTexts:
    dstsVoltsA.setUnits("Volts (rms)")
_DstsDeciAmpsA_Type = Gauge32
_DstsDeciAmpsA_Object = MibTableColumn
dstsDeciAmpsA = _DstsDeciAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 6),
    _DstsDeciAmpsA_Type()
)
dstsDeciAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsDeciAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    dstsDeciAmpsA.setUnits("0.1 Amps (rms)")
_DstsVoltsB_Type = Gauge32
_DstsVoltsB_Object = MibTableColumn
dstsVoltsB = _DstsVoltsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 7),
    _DstsVoltsB_Type()
)
dstsVoltsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsVoltsB.setStatus("current")
if mibBuilder.loadTexts:
    dstsVoltsB.setUnits("Volts (rms)")
_DstsDeciAmpsB_Type = Gauge32
_DstsDeciAmpsB_Object = MibTableColumn
dstsDeciAmpsB = _DstsDeciAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 8),
    _DstsDeciAmpsB_Type()
)
dstsDeciAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsDeciAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    dstsDeciAmpsB.setUnits("0.1 Amps (rms)")
_DstsSourceAActive_Type = Gauge32
_DstsSourceAActive_Object = MibTableColumn
dstsSourceAActive = _DstsSourceAActive_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 9),
    _DstsSourceAActive_Type()
)
dstsSourceAActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsSourceAActive.setStatus("current")
_DstsSourceBActive_Type = Gauge32
_DstsSourceBActive_Object = MibTableColumn
dstsSourceBActive = _DstsSourceBActive_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 10),
    _DstsSourceBActive_Type()
)
dstsSourceBActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsSourceBActive.setStatus("current")
_DstsPowerStatusA_Type = Gauge32
_DstsPowerStatusA_Object = MibTableColumn
dstsPowerStatusA = _DstsPowerStatusA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 11),
    _DstsPowerStatusA_Type()
)
dstsPowerStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsPowerStatusA.setStatus("current")
_DstsPowerStatusB_Type = Gauge32
_DstsPowerStatusB_Object = MibTableColumn
dstsPowerStatusB = _DstsPowerStatusB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 19, 1, 14),
    _DstsSourceBTempC_Type()
)
dstsSourceBTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstsSourceBTempC.setStatus("current")
if mibBuilder.loadTexts:
    dstsSourceBTempC.setUnits("Degrees Celsius")
_CpmSensorTable_Object = MibTable
cpmSensorTable = _CpmSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 20)
)
if mibBuilder.loadTexts:
    cpmSensorTable.setStatus("current")
_CpmSensorEntry_Object = MibTableRow
cpmSensorEntry = _CpmSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 20, 1)
)
cpmSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "cpmSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 20, 1, 1),
    _CpmSensorIndex_Type()
)
cpmSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmSensorIndex.setStatus("current")
_CpmSensorSerial_Type = DisplayString
_CpmSensorSerial_Object = MibTableColumn
cpmSensorSerial = _CpmSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 20, 1, 2),
    _CpmSensorSerial_Type()
)
cpmSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmSensorSerial.setStatus("current")
_CpmSensorName_Type = DisplayString
_CpmSensorName_Object = MibTableColumn
cpmSensorName = _CpmSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 20, 1, 3),
    _CpmSensorName_Type()
)
cpmSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmSensorName.setStatus("current")
_CpmSensorAvail_Type = Gauge32
_CpmSensorAvail_Object = MibTableColumn
cpmSensorAvail = _CpmSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 20, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 20, 1, 5),
    _CpmSensorStatus_Type()
)
cpmSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmSensorStatus.setStatus("current")
_SmokeAlarmTable_Object = MibTable
smokeAlarmTable = _SmokeAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 21)
)
if mibBuilder.loadTexts:
    smokeAlarmTable.setStatus("current")
_SmokeAlarmEntry_Object = MibTableRow
smokeAlarmEntry = _SmokeAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 21, 1)
)
smokeAlarmEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "smokeAlarmIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 21, 1, 1),
    _SmokeAlarmIndex_Type()
)
smokeAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smokeAlarmIndex.setStatus("current")
_SmokeAlarmSerial_Type = DisplayString
_SmokeAlarmSerial_Object = MibTableColumn
smokeAlarmSerial = _SmokeAlarmSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 21, 1, 2),
    _SmokeAlarmSerial_Type()
)
smokeAlarmSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeAlarmSerial.setStatus("current")
_SmokeAlarmName_Type = DisplayString
_SmokeAlarmName_Object = MibTableColumn
smokeAlarmName = _SmokeAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 21, 1, 3),
    _SmokeAlarmName_Type()
)
smokeAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeAlarmName.setStatus("current")
_SmokeAlarmAvail_Type = Gauge32
_SmokeAlarmAvail_Object = MibTableColumn
smokeAlarmAvail = _SmokeAlarmAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 21, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 21, 1, 5),
    _SmokeAlarmStatus_Type()
)
smokeAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeAlarmStatus.setStatus("current")
_Neg48VdcSensorTable_Object = MibTable
neg48VdcSensorTable = _Neg48VdcSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 22)
)
if mibBuilder.loadTexts:
    neg48VdcSensorTable.setStatus("current")
_Neg48VdcSensorEntry_Object = MibTableRow
neg48VdcSensorEntry = _Neg48VdcSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 22, 1)
)
neg48VdcSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "neg48VdcSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 22, 1, 1),
    _Neg48VdcSensorIndex_Type()
)
neg48VdcSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neg48VdcSensorIndex.setStatus("current")
_Neg48VdcSensorSerial_Type = DisplayString
_Neg48VdcSensorSerial_Object = MibTableColumn
neg48VdcSensorSerial = _Neg48VdcSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 22, 1, 2),
    _Neg48VdcSensorSerial_Type()
)
neg48VdcSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neg48VdcSensorSerial.setStatus("current")
_Neg48VdcSensorName_Type = DisplayString
_Neg48VdcSensorName_Object = MibTableColumn
neg48VdcSensorName = _Neg48VdcSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 22, 1, 3),
    _Neg48VdcSensorName_Type()
)
neg48VdcSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neg48VdcSensorName.setStatus("current")
_Neg48VdcSensorAvail_Type = Gauge32
_Neg48VdcSensorAvail_Object = MibTableColumn
neg48VdcSensorAvail = _Neg48VdcSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 22, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 22, 1, 5),
    _Neg48VdcSensorVoltage_Type()
)
neg48VdcSensorVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neg48VdcSensorVoltage.setStatus("current")
if mibBuilder.loadTexts:
    neg48VdcSensorVoltage.setUnits("Volts")
_Pos30VdcSensorTable_Object = MibTable
pos30VdcSensorTable = _Pos30VdcSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 23)
)
if mibBuilder.loadTexts:
    pos30VdcSensorTable.setStatus("current")
_Pos30VdcSensorEntry_Object = MibTableRow
pos30VdcSensorEntry = _Pos30VdcSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 23, 1)
)
pos30VdcSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "pos30VdcSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 23, 1, 1),
    _Pos30VdcSensorIndex_Type()
)
pos30VdcSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pos30VdcSensorIndex.setStatus("current")
_Pos30VdcSensorSerial_Type = DisplayString
_Pos30VdcSensorSerial_Object = MibTableColumn
pos30VdcSensorSerial = _Pos30VdcSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 23, 1, 2),
    _Pos30VdcSensorSerial_Type()
)
pos30VdcSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos30VdcSensorSerial.setStatus("current")
_Pos30VdcSensorName_Type = DisplayString
_Pos30VdcSensorName_Object = MibTableColumn
pos30VdcSensorName = _Pos30VdcSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 23, 1, 3),
    _Pos30VdcSensorName_Type()
)
pos30VdcSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos30VdcSensorName.setStatus("current")
_Pos30VdcSensorAvail_Type = Gauge32
_Pos30VdcSensorAvail_Object = MibTableColumn
pos30VdcSensorAvail = _Pos30VdcSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 23, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 23, 1, 5),
    _Pos30VdcSensorVoltage_Type()
)
pos30VdcSensorVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos30VdcSensorVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pos30VdcSensorVoltage.setUnits("Volts")
_AnalogSensorTable_Object = MibTable
analogSensorTable = _AnalogSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 24)
)
if mibBuilder.loadTexts:
    analogSensorTable.setStatus("current")
_AnalogSensorEntry_Object = MibTableRow
analogSensorEntry = _AnalogSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 24, 1)
)
analogSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "analogSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 24, 1, 1),
    _AnalogSensorIndex_Type()
)
analogSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    analogSensorIndex.setStatus("current")
_AnalogSensorSerial_Type = DisplayString
_AnalogSensorSerial_Object = MibTableColumn
analogSensorSerial = _AnalogSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 24, 1, 2),
    _AnalogSensorSerial_Type()
)
analogSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogSensorSerial.setStatus("current")
_AnalogSensorName_Type = DisplayString
_AnalogSensorName_Object = MibTableColumn
analogSensorName = _AnalogSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 24, 1, 3),
    _AnalogSensorName_Type()
)
analogSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogSensorName.setStatus("current")
_AnalogSensorAvail_Type = Gauge32
_AnalogSensorAvail_Object = MibTableColumn
analogSensorAvail = _AnalogSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 24, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 24, 1, 5),
    _AnalogSensorAnalog_Type()
)
analogSensorAnalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogSensorAnalog.setStatus("current")
_Ctrl3ChIECTable_Object = MibTable
ctrl3ChIECTable = _Ctrl3ChIECTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25)
)
if mibBuilder.loadTexts:
    ctrl3ChIECTable.setStatus("current")
_Ctrl3ChIECEntry_Object = MibTableRow
ctrl3ChIECEntry = _Ctrl3ChIECEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1)
)
ctrl3ChIECEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "ctrl3ChIECIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 1),
    _Ctrl3ChIECIndex_Type()
)
ctrl3ChIECIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrl3ChIECIndex.setStatus("current")
_Ctrl3ChIECSerial_Type = DisplayString
_Ctrl3ChIECSerial_Object = MibTableColumn
ctrl3ChIECSerial = _Ctrl3ChIECSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 2),
    _Ctrl3ChIECSerial_Type()
)
ctrl3ChIECSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECSerial.setStatus("current")
_Ctrl3ChIECName_Type = DisplayString
_Ctrl3ChIECName_Object = MibTableColumn
ctrl3ChIECName = _Ctrl3ChIECName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 3),
    _Ctrl3ChIECName_Type()
)
ctrl3ChIECName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECName.setStatus("current")
_Ctrl3ChIECAvail_Type = Gauge32
_Ctrl3ChIECAvail_Object = MibTableColumn
ctrl3ChIECAvail = _Ctrl3ChIECAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 4),
    _Ctrl3ChIECAvail_Type()
)
ctrl3ChIECAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECAvail.setStatus("current")
_Ctrl3ChIECkWattHrsA_Type = Gauge32
_Ctrl3ChIECkWattHrsA_Object = MibTableColumn
ctrl3ChIECkWattHrsA = _Ctrl3ChIECkWattHrsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 5),
    _Ctrl3ChIECkWattHrsA_Type()
)
ctrl3ChIECkWattHrsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECkWattHrsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECkWattHrsA.setUnits("kWh")
_Ctrl3ChIECVoltsA_Type = Gauge32
_Ctrl3ChIECVoltsA_Object = MibTableColumn
ctrl3ChIECVoltsA = _Ctrl3ChIECVoltsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 6),
    _Ctrl3ChIECVoltsA_Type()
)
ctrl3ChIECVoltsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltsA.setUnits("Volts (rms)")
_Ctrl3ChIECVoltPeakA_Type = Gauge32
_Ctrl3ChIECVoltPeakA_Object = MibTableColumn
ctrl3ChIECVoltPeakA = _Ctrl3ChIECVoltPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 7),
    _Ctrl3ChIECVoltPeakA_Type()
)
ctrl3ChIECVoltPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltPeakA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltPeakA.setUnits("Volts (rms)")
_Ctrl3ChIECDeciAmpsA_Type = Gauge32
_Ctrl3ChIECDeciAmpsA_Object = MibTableColumn
ctrl3ChIECDeciAmpsA = _Ctrl3ChIECDeciAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 8),
    _Ctrl3ChIECDeciAmpsA_Type()
)
ctrl3ChIECDeciAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsA.setUnits("0.1 Amps (rms)")
_Ctrl3ChIECDeciAmpsPeakA_Type = Gauge32
_Ctrl3ChIECDeciAmpsPeakA_Object = MibTableColumn
ctrl3ChIECDeciAmpsPeakA = _Ctrl3ChIECDeciAmpsPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 9),
    _Ctrl3ChIECDeciAmpsPeakA_Type()
)
ctrl3ChIECDeciAmpsPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsPeakA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsPeakA.setUnits("0.1 Amps (rms)")
_Ctrl3ChIECRealPowerA_Type = Gauge32
_Ctrl3ChIECRealPowerA_Object = MibTableColumn
ctrl3ChIECRealPowerA = _Ctrl3ChIECRealPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 10),
    _Ctrl3ChIECRealPowerA_Type()
)
ctrl3ChIECRealPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerA.setUnits("Watts")
_Ctrl3ChIECApparentPowerA_Type = Gauge32
_Ctrl3ChIECApparentPowerA_Object = MibTableColumn
ctrl3ChIECApparentPowerA = _Ctrl3ChIECApparentPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 12),
    _Ctrl3ChIECPowerFactorA_Type()
)
ctrl3ChIECPowerFactorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECPowerFactorA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECPowerFactorA.setUnits("%")
_Ctrl3ChIECkWattHrsB_Type = Gauge32
_Ctrl3ChIECkWattHrsB_Object = MibTableColumn
ctrl3ChIECkWattHrsB = _Ctrl3ChIECkWattHrsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 13),
    _Ctrl3ChIECkWattHrsB_Type()
)
ctrl3ChIECkWattHrsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECkWattHrsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECkWattHrsB.setUnits("kWh")
_Ctrl3ChIECVoltsB_Type = Gauge32
_Ctrl3ChIECVoltsB_Object = MibTableColumn
ctrl3ChIECVoltsB = _Ctrl3ChIECVoltsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 14),
    _Ctrl3ChIECVoltsB_Type()
)
ctrl3ChIECVoltsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltsB.setUnits("Volts (rms)")
_Ctrl3ChIECVoltPeakB_Type = Gauge32
_Ctrl3ChIECVoltPeakB_Object = MibTableColumn
ctrl3ChIECVoltPeakB = _Ctrl3ChIECVoltPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 15),
    _Ctrl3ChIECVoltPeakB_Type()
)
ctrl3ChIECVoltPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltPeakB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltPeakB.setUnits("Volts (rms)")
_Ctrl3ChIECDeciAmpsB_Type = Gauge32
_Ctrl3ChIECDeciAmpsB_Object = MibTableColumn
ctrl3ChIECDeciAmpsB = _Ctrl3ChIECDeciAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 16),
    _Ctrl3ChIECDeciAmpsB_Type()
)
ctrl3ChIECDeciAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsB.setUnits("0.1 Amps (rms)")
_Ctrl3ChIECDeciAmpsPeakB_Type = Gauge32
_Ctrl3ChIECDeciAmpsPeakB_Object = MibTableColumn
ctrl3ChIECDeciAmpsPeakB = _Ctrl3ChIECDeciAmpsPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 17),
    _Ctrl3ChIECDeciAmpsPeakB_Type()
)
ctrl3ChIECDeciAmpsPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsPeakB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsPeakB.setUnits("0.1 Amps (rms)")
_Ctrl3ChIECRealPowerB_Type = Gauge32
_Ctrl3ChIECRealPowerB_Object = MibTableColumn
ctrl3ChIECRealPowerB = _Ctrl3ChIECRealPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 18),
    _Ctrl3ChIECRealPowerB_Type()
)
ctrl3ChIECRealPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerB.setUnits("Watts")
_Ctrl3ChIECApparentPowerB_Type = Gauge32
_Ctrl3ChIECApparentPowerB_Object = MibTableColumn
ctrl3ChIECApparentPowerB = _Ctrl3ChIECApparentPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 20),
    _Ctrl3ChIECPowerFactorB_Type()
)
ctrl3ChIECPowerFactorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECPowerFactorB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECPowerFactorB.setUnits("%")
_Ctrl3ChIECkWattHrsC_Type = Gauge32
_Ctrl3ChIECkWattHrsC_Object = MibTableColumn
ctrl3ChIECkWattHrsC = _Ctrl3ChIECkWattHrsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 21),
    _Ctrl3ChIECkWattHrsC_Type()
)
ctrl3ChIECkWattHrsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECkWattHrsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECkWattHrsC.setUnits("kWh")
_Ctrl3ChIECVoltsC_Type = Gauge32
_Ctrl3ChIECVoltsC_Object = MibTableColumn
ctrl3ChIECVoltsC = _Ctrl3ChIECVoltsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 22),
    _Ctrl3ChIECVoltsC_Type()
)
ctrl3ChIECVoltsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltsC.setUnits("Volts (rms)")
_Ctrl3ChIECVoltPeakC_Type = Gauge32
_Ctrl3ChIECVoltPeakC_Object = MibTableColumn
ctrl3ChIECVoltPeakC = _Ctrl3ChIECVoltPeakC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 23),
    _Ctrl3ChIECVoltPeakC_Type()
)
ctrl3ChIECVoltPeakC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltPeakC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECVoltPeakC.setUnits("Volts (rms)")
_Ctrl3ChIECDeciAmpsC_Type = Gauge32
_Ctrl3ChIECDeciAmpsC_Object = MibTableColumn
ctrl3ChIECDeciAmpsC = _Ctrl3ChIECDeciAmpsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 24),
    _Ctrl3ChIECDeciAmpsC_Type()
)
ctrl3ChIECDeciAmpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsC.setUnits("0.1 Amps (rms)")
_Ctrl3ChIECDeciAmpsPeakC_Type = Gauge32
_Ctrl3ChIECDeciAmpsPeakC_Object = MibTableColumn
ctrl3ChIECDeciAmpsPeakC = _Ctrl3ChIECDeciAmpsPeakC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 25),
    _Ctrl3ChIECDeciAmpsPeakC_Type()
)
ctrl3ChIECDeciAmpsPeakC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsPeakC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECDeciAmpsPeakC.setUnits("0.1 Amps (rms)")
_Ctrl3ChIECRealPowerC_Type = Gauge32
_Ctrl3ChIECRealPowerC_Object = MibTableColumn
ctrl3ChIECRealPowerC = _Ctrl3ChIECRealPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 26),
    _Ctrl3ChIECRealPowerC_Type()
)
ctrl3ChIECRealPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerC.setUnits("Watts")
_Ctrl3ChIECApparentPowerC_Type = Gauge32
_Ctrl3ChIECApparentPowerC_Object = MibTableColumn
ctrl3ChIECApparentPowerC = _Ctrl3ChIECApparentPowerC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 27),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 28),
    _Ctrl3ChIECPowerFactorC_Type()
)
ctrl3ChIECPowerFactorC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECPowerFactorC.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECPowerFactorC.setUnits("%")
_Ctrl3ChIECkWattHrsTotal_Type = Gauge32
_Ctrl3ChIECkWattHrsTotal_Object = MibTableColumn
ctrl3ChIECkWattHrsTotal = _Ctrl3ChIECkWattHrsTotal_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 29),
    _Ctrl3ChIECkWattHrsTotal_Type()
)
ctrl3ChIECkWattHrsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECkWattHrsTotal.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECkWattHrsTotal.setUnits("kWh")
_Ctrl3ChIECRealPowerTotal_Type = Gauge32
_Ctrl3ChIECRealPowerTotal_Object = MibTableColumn
ctrl3ChIECRealPowerTotal = _Ctrl3ChIECRealPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 25, 1, 30),
    _Ctrl3ChIECRealPowerTotal_Type()
)
ctrl3ChIECRealPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerTotal.setStatus("current")
if mibBuilder.loadTexts:
    ctrl3ChIECRealPowerTotal.setUnits("Watts")
_ClimateRelayTable_Object = MibTable
climateRelayTable = _ClimateRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26)
)
if mibBuilder.loadTexts:
    climateRelayTable.setStatus("current")
_ClimateRelayEntry_Object = MibTableRow
climateRelayEntry = _ClimateRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1)
)
climateRelayEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "climateRelayIndex"),
)
if mibBuilder.loadTexts:
    climateRelayEntry.setStatus("current")


class _ClimateRelayIndex_Type(Integer32):
    """Custom type climateRelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ClimateRelayIndex_Type.__name__ = "Integer32"
_ClimateRelayIndex_Object = MibTableColumn
climateRelayIndex = _ClimateRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1, 1),
    _ClimateRelayIndex_Type()
)
climateRelayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    climateRelayIndex.setStatus("current")
_ClimateRelaySerial_Type = DisplayString
_ClimateRelaySerial_Object = MibTableColumn
climateRelaySerial = _ClimateRelaySerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1, 2),
    _ClimateRelaySerial_Type()
)
climateRelaySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRelaySerial.setStatus("current")
_ClimateRelayName_Type = DisplayString
_ClimateRelayName_Object = MibTableColumn
climateRelayName = _ClimateRelayName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1, 3),
    _ClimateRelayName_Type()
)
climateRelayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRelayName.setStatus("current")
_ClimateRelayAvail_Type = Gauge32
_ClimateRelayAvail_Object = MibTableColumn
climateRelayAvail = _ClimateRelayAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1, 4),
    _ClimateRelayAvail_Type()
)
climateRelayAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRelayAvail.setStatus("current")


class _ClimateRelayTempC_Type(Integer32):
    """Custom type climateRelayTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_ClimateRelayTempC_Type.__name__ = "Integer32"
_ClimateRelayTempC_Object = MibTableColumn
climateRelayTempC = _ClimateRelayTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1, 5),
    _ClimateRelayTempC_Type()
)
climateRelayTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRelayTempC.setStatus("current")
if mibBuilder.loadTexts:
    climateRelayTempC.setUnits("Degrees Celsius")


class _ClimateRelayTempF_Type(Integer32):
    """Custom type climateRelayTempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_ClimateRelayTempF_Type.__name__ = "Integer32"
_ClimateRelayTempF_Object = MibTableColumn
climateRelayTempF = _ClimateRelayTempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1, 6),
    _ClimateRelayTempF_Type()
)
climateRelayTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRelayTempF.setStatus("current")
if mibBuilder.loadTexts:
    climateRelayTempF.setUnits("Degress Fahrenheit")


class _ClimateRelayIO1_Type(Integer32):
    """Custom type climateRelayIO1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateRelayIO1_Type.__name__ = "Integer32"
_ClimateRelayIO1_Object = MibTableColumn
climateRelayIO1 = _ClimateRelayIO1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1, 7),
    _ClimateRelayIO1_Type()
)
climateRelayIO1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRelayIO1.setStatus("current")


class _ClimateRelayIO2_Type(Integer32):
    """Custom type climateRelayIO2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateRelayIO2_Type.__name__ = "Integer32"
_ClimateRelayIO2_Object = MibTableColumn
climateRelayIO2 = _ClimateRelayIO2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1, 8),
    _ClimateRelayIO2_Type()
)
climateRelayIO2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRelayIO2.setStatus("current")


class _ClimateRelayIO3_Type(Integer32):
    """Custom type climateRelayIO3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateRelayIO3_Type.__name__ = "Integer32"
_ClimateRelayIO3_Object = MibTableColumn
climateRelayIO3 = _ClimateRelayIO3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1, 9),
    _ClimateRelayIO3_Type()
)
climateRelayIO3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRelayIO3.setStatus("current")


class _ClimateRelayIO4_Type(Integer32):
    """Custom type climateRelayIO4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateRelayIO4_Type.__name__ = "Integer32"
_ClimateRelayIO4_Object = MibTableColumn
climateRelayIO4 = _ClimateRelayIO4_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1, 10),
    _ClimateRelayIO4_Type()
)
climateRelayIO4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRelayIO4.setStatus("current")


class _ClimateRelayIO5_Type(Integer32):
    """Custom type climateRelayIO5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateRelayIO5_Type.__name__ = "Integer32"
_ClimateRelayIO5_Object = MibTableColumn
climateRelayIO5 = _ClimateRelayIO5_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1, 11),
    _ClimateRelayIO5_Type()
)
climateRelayIO5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRelayIO5.setStatus("current")


class _ClimateRelayIO6_Type(Integer32):
    """Custom type climateRelayIO6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClimateRelayIO6_Type.__name__ = "Integer32"
_ClimateRelayIO6_Object = MibTableColumn
climateRelayIO6 = _ClimateRelayIO6_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 26, 1, 12),
    _ClimateRelayIO6_Type()
)
climateRelayIO6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateRelayIO6.setStatus("current")
_CtrlRelayTable_Object = MibTable
ctrlRelayTable = _CtrlRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 27)
)
if mibBuilder.loadTexts:
    ctrlRelayTable.setStatus("current")
_CtrlRelayEntry_Object = MibTableRow
ctrlRelayEntry = _CtrlRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 27, 1)
)
ctrlRelayEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "ctrlRelayIndex"),
)
if mibBuilder.loadTexts:
    ctrlRelayEntry.setStatus("current")


class _CtrlRelayIndex_Type(Integer32):
    """Custom type ctrlRelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CtrlRelayIndex_Type.__name__ = "Integer32"
_CtrlRelayIndex_Object = MibTableColumn
ctrlRelayIndex = _CtrlRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 27, 1, 1),
    _CtrlRelayIndex_Type()
)
ctrlRelayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrlRelayIndex.setStatus("current")
_CtrlRelayName_Type = DisplayString
_CtrlRelayName_Object = MibTableColumn
ctrlRelayName = _CtrlRelayName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 27, 1, 2),
    _CtrlRelayName_Type()
)
ctrlRelayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlRelayName.setStatus("current")
_CtrlRelayState_Type = Gauge32
_CtrlRelayState_Object = MibTableColumn
ctrlRelayState = _CtrlRelayState_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 27, 1, 3),
    _CtrlRelayState_Type()
)
ctrlRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlRelayState.setStatus("current")
_CtrlRelayLatchingMode_Type = Gauge32
_CtrlRelayLatchingMode_Object = MibTableColumn
ctrlRelayLatchingMode = _CtrlRelayLatchingMode_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 27, 1, 4),
    _CtrlRelayLatchingMode_Type()
)
ctrlRelayLatchingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlRelayLatchingMode.setStatus("current")
_CtrlRelayOverride_Type = Gauge32
_CtrlRelayOverride_Object = MibTableColumn
ctrlRelayOverride = _CtrlRelayOverride_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 27, 1, 5),
    _CtrlRelayOverride_Type()
)
ctrlRelayOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlRelayOverride.setStatus("current")
_CtrlRelayAcknowledge_Type = Gauge32
_CtrlRelayAcknowledge_Object = MibTableColumn
ctrlRelayAcknowledge = _CtrlRelayAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 27, 1, 6),
    _CtrlRelayAcknowledge_Type()
)
ctrlRelayAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlRelayAcknowledge.setStatus("current")
_AirSpeedSwitchSensorTable_Object = MibTable
airSpeedSwitchSensorTable = _AirSpeedSwitchSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 28)
)
if mibBuilder.loadTexts:
    airSpeedSwitchSensorTable.setStatus("current")
_AirSpeedSwitchSensorEntry_Object = MibTableRow
airSpeedSwitchSensorEntry = _AirSpeedSwitchSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 28, 1)
)
airSpeedSwitchSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "airSpeedSwitchSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 28, 1, 1),
    _AirSpeedSwitchSensorIndex_Type()
)
airSpeedSwitchSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    airSpeedSwitchSensorIndex.setStatus("current")
_AirSpeedSwitchSensorSerial_Type = DisplayString
_AirSpeedSwitchSensorSerial_Object = MibTableColumn
airSpeedSwitchSensorSerial = _AirSpeedSwitchSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 28, 1, 2),
    _AirSpeedSwitchSensorSerial_Type()
)
airSpeedSwitchSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airSpeedSwitchSensorSerial.setStatus("current")
_AirSpeedSwitchSensorName_Type = DisplayString
_AirSpeedSwitchSensorName_Object = MibTableColumn
airSpeedSwitchSensorName = _AirSpeedSwitchSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 28, 1, 3),
    _AirSpeedSwitchSensorName_Type()
)
airSpeedSwitchSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airSpeedSwitchSensorName.setStatus("current")
_AirSpeedSwitchSensorAvail_Type = Gauge32
_AirSpeedSwitchSensorAvail_Object = MibTableColumn
airSpeedSwitchSensorAvail = _AirSpeedSwitchSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 28, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 21239, 2, 28, 1, 5),
    _AirSpeedSwitchSensorAirSpeed_Type()
)
airSpeedSwitchSensorAirSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airSpeedSwitchSensorAirSpeed.setStatus("current")
_PowerDMTable_Object = MibTable
powerDMTable = _PowerDMTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29)
)
if mibBuilder.loadTexts:
    powerDMTable.setStatus("current")
_PowerDMEntry_Object = MibTableRow
powerDMEntry = _PowerDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1)
)
powerDMEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "powerDMIndex"),
)
if mibBuilder.loadTexts:
    powerDMEntry.setStatus("current")


class _PowerDMIndex_Type(Integer32):
    """Custom type powerDMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PowerDMIndex_Type.__name__ = "Integer32"
_PowerDMIndex_Object = MibTableColumn
powerDMIndex = _PowerDMIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 1),
    _PowerDMIndex_Type()
)
powerDMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerDMIndex.setStatus("current")
_PowerDMSerial_Type = DisplayString
_PowerDMSerial_Object = MibTableColumn
powerDMSerial = _PowerDMSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 2),
    _PowerDMSerial_Type()
)
powerDMSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMSerial.setStatus("current")
_PowerDMName_Type = DisplayString
_PowerDMName_Object = MibTableColumn
powerDMName = _PowerDMName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 3),
    _PowerDMName_Type()
)
powerDMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMName.setStatus("current")
_PowerDMAvail_Type = Gauge32
_PowerDMAvail_Object = MibTableColumn
powerDMAvail = _PowerDMAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 4),
    _PowerDMAvail_Type()
)
powerDMAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMAvail.setStatus("current")
_PowerDMUnitInfoTitle_Type = DisplayString
_PowerDMUnitInfoTitle_Object = MibTableColumn
powerDMUnitInfoTitle = _PowerDMUnitInfoTitle_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 5),
    _PowerDMUnitInfoTitle_Type()
)
powerDMUnitInfoTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMUnitInfoTitle.setStatus("current")
_PowerDMUnitInfoVersion_Type = DisplayString
_PowerDMUnitInfoVersion_Object = MibTableColumn
powerDMUnitInfoVersion = _PowerDMUnitInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 6),
    _PowerDMUnitInfoVersion_Type()
)
powerDMUnitInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMUnitInfoVersion.setStatus("current")


class _PowerDMUnitInfoMainCount_Type(Integer32):
    """Custom type powerDMUnitInfoMainCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PowerDMUnitInfoMainCount_Type.__name__ = "Integer32"
_PowerDMUnitInfoMainCount_Object = MibTableColumn
powerDMUnitInfoMainCount = _PowerDMUnitInfoMainCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 7),
    _PowerDMUnitInfoMainCount_Type()
)
powerDMUnitInfoMainCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMUnitInfoMainCount.setStatus("current")


class _PowerDMUnitInfoAuxCount_Type(Integer32):
    """Custom type powerDMUnitInfoAuxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_PowerDMUnitInfoAuxCount_Type.__name__ = "Integer32"
_PowerDMUnitInfoAuxCount_Object = MibTableColumn
powerDMUnitInfoAuxCount = _PowerDMUnitInfoAuxCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 8),
    _PowerDMUnitInfoAuxCount_Type()
)
powerDMUnitInfoAuxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMUnitInfoAuxCount.setStatus("current")
_PowerDMChannelName1_Type = DisplayString
_PowerDMChannelName1_Object = MibTableColumn
powerDMChannelName1 = _PowerDMChannelName1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 9),
    _PowerDMChannelName1_Type()
)
powerDMChannelName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName1.setStatus("current")
_PowerDMChannelName2_Type = DisplayString
_PowerDMChannelName2_Object = MibTableColumn
powerDMChannelName2 = _PowerDMChannelName2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 10),
    _PowerDMChannelName2_Type()
)
powerDMChannelName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName2.setStatus("current")
_PowerDMChannelName3_Type = DisplayString
_PowerDMChannelName3_Object = MibTableColumn
powerDMChannelName3 = _PowerDMChannelName3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 11),
    _PowerDMChannelName3_Type()
)
powerDMChannelName3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName3.setStatus("current")
_PowerDMChannelName4_Type = DisplayString
_PowerDMChannelName4_Object = MibTableColumn
powerDMChannelName4 = _PowerDMChannelName4_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 12),
    _PowerDMChannelName4_Type()
)
powerDMChannelName4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName4.setStatus("current")
_PowerDMChannelName5_Type = DisplayString
_PowerDMChannelName5_Object = MibTableColumn
powerDMChannelName5 = _PowerDMChannelName5_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 13),
    _PowerDMChannelName5_Type()
)
powerDMChannelName5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName5.setStatus("current")
_PowerDMChannelName6_Type = DisplayString
_PowerDMChannelName6_Object = MibTableColumn
powerDMChannelName6 = _PowerDMChannelName6_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 14),
    _PowerDMChannelName6_Type()
)
powerDMChannelName6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName6.setStatus("current")
_PowerDMChannelName7_Type = DisplayString
_PowerDMChannelName7_Object = MibTableColumn
powerDMChannelName7 = _PowerDMChannelName7_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 15),
    _PowerDMChannelName7_Type()
)
powerDMChannelName7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName7.setStatus("current")
_PowerDMChannelName8_Type = DisplayString
_PowerDMChannelName8_Object = MibTableColumn
powerDMChannelName8 = _PowerDMChannelName8_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 16),
    _PowerDMChannelName8_Type()
)
powerDMChannelName8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName8.setStatus("current")
_PowerDMChannelName9_Type = DisplayString
_PowerDMChannelName9_Object = MibTableColumn
powerDMChannelName9 = _PowerDMChannelName9_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 17),
    _PowerDMChannelName9_Type()
)
powerDMChannelName9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName9.setStatus("current")
_PowerDMChannelName10_Type = DisplayString
_PowerDMChannelName10_Object = MibTableColumn
powerDMChannelName10 = _PowerDMChannelName10_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 18),
    _PowerDMChannelName10_Type()
)
powerDMChannelName10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName10.setStatus("current")
_PowerDMChannelName11_Type = DisplayString
_PowerDMChannelName11_Object = MibTableColumn
powerDMChannelName11 = _PowerDMChannelName11_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 19),
    _PowerDMChannelName11_Type()
)
powerDMChannelName11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName11.setStatus("current")
_PowerDMChannelName12_Type = DisplayString
_PowerDMChannelName12_Object = MibTableColumn
powerDMChannelName12 = _PowerDMChannelName12_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 20),
    _PowerDMChannelName12_Type()
)
powerDMChannelName12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName12.setStatus("current")
_PowerDMChannelName13_Type = DisplayString
_PowerDMChannelName13_Object = MibTableColumn
powerDMChannelName13 = _PowerDMChannelName13_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 21),
    _PowerDMChannelName13_Type()
)
powerDMChannelName13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName13.setStatus("current")
_PowerDMChannelName14_Type = DisplayString
_PowerDMChannelName14_Object = MibTableColumn
powerDMChannelName14 = _PowerDMChannelName14_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 22),
    _PowerDMChannelName14_Type()
)
powerDMChannelName14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName14.setStatus("current")
_PowerDMChannelName15_Type = DisplayString
_PowerDMChannelName15_Object = MibTableColumn
powerDMChannelName15 = _PowerDMChannelName15_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 23),
    _PowerDMChannelName15_Type()
)
powerDMChannelName15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName15.setStatus("current")
_PowerDMChannelName16_Type = DisplayString
_PowerDMChannelName16_Object = MibTableColumn
powerDMChannelName16 = _PowerDMChannelName16_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 24),
    _PowerDMChannelName16_Type()
)
powerDMChannelName16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName16.setStatus("current")
_PowerDMChannelName17_Type = DisplayString
_PowerDMChannelName17_Object = MibTableColumn
powerDMChannelName17 = _PowerDMChannelName17_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 25),
    _PowerDMChannelName17_Type()
)
powerDMChannelName17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName17.setStatus("current")
_PowerDMChannelName18_Type = DisplayString
_PowerDMChannelName18_Object = MibTableColumn
powerDMChannelName18 = _PowerDMChannelName18_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 26),
    _PowerDMChannelName18_Type()
)
powerDMChannelName18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName18.setStatus("current")
_PowerDMChannelName19_Type = DisplayString
_PowerDMChannelName19_Object = MibTableColumn
powerDMChannelName19 = _PowerDMChannelName19_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 27),
    _PowerDMChannelName19_Type()
)
powerDMChannelName19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName19.setStatus("current")
_PowerDMChannelName20_Type = DisplayString
_PowerDMChannelName20_Object = MibTableColumn
powerDMChannelName20 = _PowerDMChannelName20_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 28),
    _PowerDMChannelName20_Type()
)
powerDMChannelName20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName20.setStatus("current")
_PowerDMChannelName21_Type = DisplayString
_PowerDMChannelName21_Object = MibTableColumn
powerDMChannelName21 = _PowerDMChannelName21_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 29),
    _PowerDMChannelName21_Type()
)
powerDMChannelName21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName21.setStatus("current")
_PowerDMChannelName22_Type = DisplayString
_PowerDMChannelName22_Object = MibTableColumn
powerDMChannelName22 = _PowerDMChannelName22_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 30),
    _PowerDMChannelName22_Type()
)
powerDMChannelName22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName22.setStatus("current")
_PowerDMChannelName23_Type = DisplayString
_PowerDMChannelName23_Object = MibTableColumn
powerDMChannelName23 = _PowerDMChannelName23_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 31),
    _PowerDMChannelName23_Type()
)
powerDMChannelName23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName23.setStatus("current")
_PowerDMChannelName24_Type = DisplayString
_PowerDMChannelName24_Object = MibTableColumn
powerDMChannelName24 = _PowerDMChannelName24_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 32),
    _PowerDMChannelName24_Type()
)
powerDMChannelName24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName24.setStatus("current")
_PowerDMChannelName25_Type = DisplayString
_PowerDMChannelName25_Object = MibTableColumn
powerDMChannelName25 = _PowerDMChannelName25_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 33),
    _PowerDMChannelName25_Type()
)
powerDMChannelName25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName25.setStatus("current")
_PowerDMChannelName26_Type = DisplayString
_PowerDMChannelName26_Object = MibTableColumn
powerDMChannelName26 = _PowerDMChannelName26_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 34),
    _PowerDMChannelName26_Type()
)
powerDMChannelName26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName26.setStatus("current")
_PowerDMChannelName27_Type = DisplayString
_PowerDMChannelName27_Object = MibTableColumn
powerDMChannelName27 = _PowerDMChannelName27_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 35),
    _PowerDMChannelName27_Type()
)
powerDMChannelName27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName27.setStatus("current")
_PowerDMChannelName28_Type = DisplayString
_PowerDMChannelName28_Object = MibTableColumn
powerDMChannelName28 = _PowerDMChannelName28_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 36),
    _PowerDMChannelName28_Type()
)
powerDMChannelName28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName28.setStatus("current")
_PowerDMChannelName29_Type = DisplayString
_PowerDMChannelName29_Object = MibTableColumn
powerDMChannelName29 = _PowerDMChannelName29_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 37),
    _PowerDMChannelName29_Type()
)
powerDMChannelName29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName29.setStatus("current")
_PowerDMChannelName30_Type = DisplayString
_PowerDMChannelName30_Object = MibTableColumn
powerDMChannelName30 = _PowerDMChannelName30_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 38),
    _PowerDMChannelName30_Type()
)
powerDMChannelName30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName30.setStatus("current")
_PowerDMChannelName31_Type = DisplayString
_PowerDMChannelName31_Object = MibTableColumn
powerDMChannelName31 = _PowerDMChannelName31_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 39),
    _PowerDMChannelName31_Type()
)
powerDMChannelName31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName31.setStatus("current")
_PowerDMChannelName32_Type = DisplayString
_PowerDMChannelName32_Object = MibTableColumn
powerDMChannelName32 = _PowerDMChannelName32_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 40),
    _PowerDMChannelName32_Type()
)
powerDMChannelName32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName32.setStatus("current")
_PowerDMChannelName33_Type = DisplayString
_PowerDMChannelName33_Object = MibTableColumn
powerDMChannelName33 = _PowerDMChannelName33_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 41),
    _PowerDMChannelName33_Type()
)
powerDMChannelName33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName33.setStatus("current")
_PowerDMChannelName34_Type = DisplayString
_PowerDMChannelName34_Object = MibTableColumn
powerDMChannelName34 = _PowerDMChannelName34_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 42),
    _PowerDMChannelName34_Type()
)
powerDMChannelName34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName34.setStatus("current")
_PowerDMChannelName35_Type = DisplayString
_PowerDMChannelName35_Object = MibTableColumn
powerDMChannelName35 = _PowerDMChannelName35_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 43),
    _PowerDMChannelName35_Type()
)
powerDMChannelName35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName35.setStatus("current")
_PowerDMChannelName36_Type = DisplayString
_PowerDMChannelName36_Object = MibTableColumn
powerDMChannelName36 = _PowerDMChannelName36_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 44),
    _PowerDMChannelName36_Type()
)
powerDMChannelName36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName36.setStatus("current")
_PowerDMChannelName37_Type = DisplayString
_PowerDMChannelName37_Object = MibTableColumn
powerDMChannelName37 = _PowerDMChannelName37_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 45),
    _PowerDMChannelName37_Type()
)
powerDMChannelName37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName37.setStatus("current")
_PowerDMChannelName38_Type = DisplayString
_PowerDMChannelName38_Object = MibTableColumn
powerDMChannelName38 = _PowerDMChannelName38_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 46),
    _PowerDMChannelName38_Type()
)
powerDMChannelName38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName38.setStatus("current")
_PowerDMChannelName39_Type = DisplayString
_PowerDMChannelName39_Object = MibTableColumn
powerDMChannelName39 = _PowerDMChannelName39_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 47),
    _PowerDMChannelName39_Type()
)
powerDMChannelName39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName39.setStatus("current")
_PowerDMChannelName40_Type = DisplayString
_PowerDMChannelName40_Object = MibTableColumn
powerDMChannelName40 = _PowerDMChannelName40_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 48),
    _PowerDMChannelName40_Type()
)
powerDMChannelName40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName40.setStatus("current")
_PowerDMChannelName41_Type = DisplayString
_PowerDMChannelName41_Object = MibTableColumn
powerDMChannelName41 = _PowerDMChannelName41_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 49),
    _PowerDMChannelName41_Type()
)
powerDMChannelName41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName41.setStatus("current")
_PowerDMChannelName42_Type = DisplayString
_PowerDMChannelName42_Object = MibTableColumn
powerDMChannelName42 = _PowerDMChannelName42_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 50),
    _PowerDMChannelName42_Type()
)
powerDMChannelName42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName42.setStatus("current")
_PowerDMChannelName43_Type = DisplayString
_PowerDMChannelName43_Object = MibTableColumn
powerDMChannelName43 = _PowerDMChannelName43_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 51),
    _PowerDMChannelName43_Type()
)
powerDMChannelName43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName43.setStatus("current")
_PowerDMChannelName44_Type = DisplayString
_PowerDMChannelName44_Object = MibTableColumn
powerDMChannelName44 = _PowerDMChannelName44_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 52),
    _PowerDMChannelName44_Type()
)
powerDMChannelName44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName44.setStatus("current")
_PowerDMChannelName45_Type = DisplayString
_PowerDMChannelName45_Object = MibTableColumn
powerDMChannelName45 = _PowerDMChannelName45_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 53),
    _PowerDMChannelName45_Type()
)
powerDMChannelName45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName45.setStatus("current")
_PowerDMChannelName46_Type = DisplayString
_PowerDMChannelName46_Object = MibTableColumn
powerDMChannelName46 = _PowerDMChannelName46_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 54),
    _PowerDMChannelName46_Type()
)
powerDMChannelName46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName46.setStatus("current")
_PowerDMChannelName47_Type = DisplayString
_PowerDMChannelName47_Object = MibTableColumn
powerDMChannelName47 = _PowerDMChannelName47_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 55),
    _PowerDMChannelName47_Type()
)
powerDMChannelName47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName47.setStatus("current")
_PowerDMChannelName48_Type = DisplayString
_PowerDMChannelName48_Object = MibTableColumn
powerDMChannelName48 = _PowerDMChannelName48_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 56),
    _PowerDMChannelName48_Type()
)
powerDMChannelName48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName48.setStatus("current")
_PowerDMChannelFriendly1_Type = DisplayString
_PowerDMChannelFriendly1_Object = MibTableColumn
powerDMChannelFriendly1 = _PowerDMChannelFriendly1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 57),
    _PowerDMChannelFriendly1_Type()
)
powerDMChannelFriendly1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly1.setStatus("current")
_PowerDMChannelFriendly2_Type = DisplayString
_PowerDMChannelFriendly2_Object = MibTableColumn
powerDMChannelFriendly2 = _PowerDMChannelFriendly2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 58),
    _PowerDMChannelFriendly2_Type()
)
powerDMChannelFriendly2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly2.setStatus("current")
_PowerDMChannelFriendly3_Type = DisplayString
_PowerDMChannelFriendly3_Object = MibTableColumn
powerDMChannelFriendly3 = _PowerDMChannelFriendly3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 59),
    _PowerDMChannelFriendly3_Type()
)
powerDMChannelFriendly3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly3.setStatus("current")
_PowerDMChannelFriendly4_Type = DisplayString
_PowerDMChannelFriendly4_Object = MibTableColumn
powerDMChannelFriendly4 = _PowerDMChannelFriendly4_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 60),
    _PowerDMChannelFriendly4_Type()
)
powerDMChannelFriendly4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly4.setStatus("current")
_PowerDMChannelFriendly5_Type = DisplayString
_PowerDMChannelFriendly5_Object = MibTableColumn
powerDMChannelFriendly5 = _PowerDMChannelFriendly5_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 61),
    _PowerDMChannelFriendly5_Type()
)
powerDMChannelFriendly5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly5.setStatus("current")
_PowerDMChannelFriendly6_Type = DisplayString
_PowerDMChannelFriendly6_Object = MibTableColumn
powerDMChannelFriendly6 = _PowerDMChannelFriendly6_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 62),
    _PowerDMChannelFriendly6_Type()
)
powerDMChannelFriendly6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly6.setStatus("current")
_PowerDMChannelFriendly7_Type = DisplayString
_PowerDMChannelFriendly7_Object = MibTableColumn
powerDMChannelFriendly7 = _PowerDMChannelFriendly7_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 63),
    _PowerDMChannelFriendly7_Type()
)
powerDMChannelFriendly7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly7.setStatus("current")
_PowerDMChannelFriendly8_Type = DisplayString
_PowerDMChannelFriendly8_Object = MibTableColumn
powerDMChannelFriendly8 = _PowerDMChannelFriendly8_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 64),
    _PowerDMChannelFriendly8_Type()
)
powerDMChannelFriendly8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly8.setStatus("current")
_PowerDMChannelFriendly9_Type = DisplayString
_PowerDMChannelFriendly9_Object = MibTableColumn
powerDMChannelFriendly9 = _PowerDMChannelFriendly9_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 65),
    _PowerDMChannelFriendly9_Type()
)
powerDMChannelFriendly9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly9.setStatus("current")
_PowerDMChannelFriendly10_Type = DisplayString
_PowerDMChannelFriendly10_Object = MibTableColumn
powerDMChannelFriendly10 = _PowerDMChannelFriendly10_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 66),
    _PowerDMChannelFriendly10_Type()
)
powerDMChannelFriendly10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly10.setStatus("current")
_PowerDMChannelFriendly11_Type = DisplayString
_PowerDMChannelFriendly11_Object = MibTableColumn
powerDMChannelFriendly11 = _PowerDMChannelFriendly11_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 67),
    _PowerDMChannelFriendly11_Type()
)
powerDMChannelFriendly11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly11.setStatus("current")
_PowerDMChannelFriendly12_Type = DisplayString
_PowerDMChannelFriendly12_Object = MibTableColumn
powerDMChannelFriendly12 = _PowerDMChannelFriendly12_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 68),
    _PowerDMChannelFriendly12_Type()
)
powerDMChannelFriendly12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly12.setStatus("current")
_PowerDMChannelFriendly13_Type = DisplayString
_PowerDMChannelFriendly13_Object = MibTableColumn
powerDMChannelFriendly13 = _PowerDMChannelFriendly13_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 69),
    _PowerDMChannelFriendly13_Type()
)
powerDMChannelFriendly13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly13.setStatus("current")
_PowerDMChannelFriendly14_Type = DisplayString
_PowerDMChannelFriendly14_Object = MibTableColumn
powerDMChannelFriendly14 = _PowerDMChannelFriendly14_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 70),
    _PowerDMChannelFriendly14_Type()
)
powerDMChannelFriendly14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly14.setStatus("current")
_PowerDMChannelFriendly15_Type = DisplayString
_PowerDMChannelFriendly15_Object = MibTableColumn
powerDMChannelFriendly15 = _PowerDMChannelFriendly15_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 71),
    _PowerDMChannelFriendly15_Type()
)
powerDMChannelFriendly15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly15.setStatus("current")
_PowerDMChannelFriendly16_Type = DisplayString
_PowerDMChannelFriendly16_Object = MibTableColumn
powerDMChannelFriendly16 = _PowerDMChannelFriendly16_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 72),
    _PowerDMChannelFriendly16_Type()
)
powerDMChannelFriendly16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly16.setStatus("current")
_PowerDMChannelFriendly17_Type = DisplayString
_PowerDMChannelFriendly17_Object = MibTableColumn
powerDMChannelFriendly17 = _PowerDMChannelFriendly17_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 73),
    _PowerDMChannelFriendly17_Type()
)
powerDMChannelFriendly17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly17.setStatus("current")
_PowerDMChannelFriendly18_Type = DisplayString
_PowerDMChannelFriendly18_Object = MibTableColumn
powerDMChannelFriendly18 = _PowerDMChannelFriendly18_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 74),
    _PowerDMChannelFriendly18_Type()
)
powerDMChannelFriendly18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly18.setStatus("current")
_PowerDMChannelFriendly19_Type = DisplayString
_PowerDMChannelFriendly19_Object = MibTableColumn
powerDMChannelFriendly19 = _PowerDMChannelFriendly19_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 75),
    _PowerDMChannelFriendly19_Type()
)
powerDMChannelFriendly19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly19.setStatus("current")
_PowerDMChannelFriendly20_Type = DisplayString
_PowerDMChannelFriendly20_Object = MibTableColumn
powerDMChannelFriendly20 = _PowerDMChannelFriendly20_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 76),
    _PowerDMChannelFriendly20_Type()
)
powerDMChannelFriendly20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly20.setStatus("current")
_PowerDMChannelFriendly21_Type = DisplayString
_PowerDMChannelFriendly21_Object = MibTableColumn
powerDMChannelFriendly21 = _PowerDMChannelFriendly21_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 77),
    _PowerDMChannelFriendly21_Type()
)
powerDMChannelFriendly21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly21.setStatus("current")
_PowerDMChannelFriendly22_Type = DisplayString
_PowerDMChannelFriendly22_Object = MibTableColumn
powerDMChannelFriendly22 = _PowerDMChannelFriendly22_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 78),
    _PowerDMChannelFriendly22_Type()
)
powerDMChannelFriendly22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly22.setStatus("current")
_PowerDMChannelFriendly23_Type = DisplayString
_PowerDMChannelFriendly23_Object = MibTableColumn
powerDMChannelFriendly23 = _PowerDMChannelFriendly23_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 79),
    _PowerDMChannelFriendly23_Type()
)
powerDMChannelFriendly23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly23.setStatus("current")
_PowerDMChannelFriendly24_Type = DisplayString
_PowerDMChannelFriendly24_Object = MibTableColumn
powerDMChannelFriendly24 = _PowerDMChannelFriendly24_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 80),
    _PowerDMChannelFriendly24_Type()
)
powerDMChannelFriendly24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly24.setStatus("current")
_PowerDMChannelFriendly25_Type = DisplayString
_PowerDMChannelFriendly25_Object = MibTableColumn
powerDMChannelFriendly25 = _PowerDMChannelFriendly25_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 81),
    _PowerDMChannelFriendly25_Type()
)
powerDMChannelFriendly25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly25.setStatus("current")
_PowerDMChannelFriendly26_Type = DisplayString
_PowerDMChannelFriendly26_Object = MibTableColumn
powerDMChannelFriendly26 = _PowerDMChannelFriendly26_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 82),
    _PowerDMChannelFriendly26_Type()
)
powerDMChannelFriendly26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly26.setStatus("current")
_PowerDMChannelFriendly27_Type = DisplayString
_PowerDMChannelFriendly27_Object = MibTableColumn
powerDMChannelFriendly27 = _PowerDMChannelFriendly27_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 83),
    _PowerDMChannelFriendly27_Type()
)
powerDMChannelFriendly27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly27.setStatus("current")
_PowerDMChannelFriendly28_Type = DisplayString
_PowerDMChannelFriendly28_Object = MibTableColumn
powerDMChannelFriendly28 = _PowerDMChannelFriendly28_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 84),
    _PowerDMChannelFriendly28_Type()
)
powerDMChannelFriendly28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly28.setStatus("current")
_PowerDMChannelFriendly29_Type = DisplayString
_PowerDMChannelFriendly29_Object = MibTableColumn
powerDMChannelFriendly29 = _PowerDMChannelFriendly29_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 85),
    _PowerDMChannelFriendly29_Type()
)
powerDMChannelFriendly29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly29.setStatus("current")
_PowerDMChannelFriendly30_Type = DisplayString
_PowerDMChannelFriendly30_Object = MibTableColumn
powerDMChannelFriendly30 = _PowerDMChannelFriendly30_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 86),
    _PowerDMChannelFriendly30_Type()
)
powerDMChannelFriendly30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly30.setStatus("current")
_PowerDMChannelFriendly31_Type = DisplayString
_PowerDMChannelFriendly31_Object = MibTableColumn
powerDMChannelFriendly31 = _PowerDMChannelFriendly31_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 87),
    _PowerDMChannelFriendly31_Type()
)
powerDMChannelFriendly31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly31.setStatus("current")
_PowerDMChannelFriendly32_Type = DisplayString
_PowerDMChannelFriendly32_Object = MibTableColumn
powerDMChannelFriendly32 = _PowerDMChannelFriendly32_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 88),
    _PowerDMChannelFriendly32_Type()
)
powerDMChannelFriendly32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly32.setStatus("current")
_PowerDMChannelFriendly33_Type = DisplayString
_PowerDMChannelFriendly33_Object = MibTableColumn
powerDMChannelFriendly33 = _PowerDMChannelFriendly33_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 89),
    _PowerDMChannelFriendly33_Type()
)
powerDMChannelFriendly33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly33.setStatus("current")
_PowerDMChannelFriendly34_Type = DisplayString
_PowerDMChannelFriendly34_Object = MibTableColumn
powerDMChannelFriendly34 = _PowerDMChannelFriendly34_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 90),
    _PowerDMChannelFriendly34_Type()
)
powerDMChannelFriendly34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly34.setStatus("current")
_PowerDMChannelFriendly35_Type = DisplayString
_PowerDMChannelFriendly35_Object = MibTableColumn
powerDMChannelFriendly35 = _PowerDMChannelFriendly35_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 91),
    _PowerDMChannelFriendly35_Type()
)
powerDMChannelFriendly35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly35.setStatus("current")
_PowerDMChannelFriendly36_Type = DisplayString
_PowerDMChannelFriendly36_Object = MibTableColumn
powerDMChannelFriendly36 = _PowerDMChannelFriendly36_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 92),
    _PowerDMChannelFriendly36_Type()
)
powerDMChannelFriendly36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly36.setStatus("current")
_PowerDMChannelFriendly37_Type = DisplayString
_PowerDMChannelFriendly37_Object = MibTableColumn
powerDMChannelFriendly37 = _PowerDMChannelFriendly37_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 93),
    _PowerDMChannelFriendly37_Type()
)
powerDMChannelFriendly37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly37.setStatus("current")
_PowerDMChannelFriendly38_Type = DisplayString
_PowerDMChannelFriendly38_Object = MibTableColumn
powerDMChannelFriendly38 = _PowerDMChannelFriendly38_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 94),
    _PowerDMChannelFriendly38_Type()
)
powerDMChannelFriendly38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly38.setStatus("current")
_PowerDMChannelFriendly39_Type = DisplayString
_PowerDMChannelFriendly39_Object = MibTableColumn
powerDMChannelFriendly39 = _PowerDMChannelFriendly39_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 95),
    _PowerDMChannelFriendly39_Type()
)
powerDMChannelFriendly39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly39.setStatus("current")
_PowerDMChannelFriendly40_Type = DisplayString
_PowerDMChannelFriendly40_Object = MibTableColumn
powerDMChannelFriendly40 = _PowerDMChannelFriendly40_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 96),
    _PowerDMChannelFriendly40_Type()
)
powerDMChannelFriendly40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly40.setStatus("current")
_PowerDMChannelFriendly41_Type = DisplayString
_PowerDMChannelFriendly41_Object = MibTableColumn
powerDMChannelFriendly41 = _PowerDMChannelFriendly41_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 97),
    _PowerDMChannelFriendly41_Type()
)
powerDMChannelFriendly41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly41.setStatus("current")
_PowerDMChannelFriendly42_Type = DisplayString
_PowerDMChannelFriendly42_Object = MibTableColumn
powerDMChannelFriendly42 = _PowerDMChannelFriendly42_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 98),
    _PowerDMChannelFriendly42_Type()
)
powerDMChannelFriendly42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly42.setStatus("current")
_PowerDMChannelFriendly43_Type = DisplayString
_PowerDMChannelFriendly43_Object = MibTableColumn
powerDMChannelFriendly43 = _PowerDMChannelFriendly43_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 99),
    _PowerDMChannelFriendly43_Type()
)
powerDMChannelFriendly43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly43.setStatus("current")
_PowerDMChannelFriendly44_Type = DisplayString
_PowerDMChannelFriendly44_Object = MibTableColumn
powerDMChannelFriendly44 = _PowerDMChannelFriendly44_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 100),
    _PowerDMChannelFriendly44_Type()
)
powerDMChannelFriendly44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly44.setStatus("current")
_PowerDMChannelFriendly45_Type = DisplayString
_PowerDMChannelFriendly45_Object = MibTableColumn
powerDMChannelFriendly45 = _PowerDMChannelFriendly45_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 101),
    _PowerDMChannelFriendly45_Type()
)
powerDMChannelFriendly45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly45.setStatus("current")
_PowerDMChannelFriendly46_Type = DisplayString
_PowerDMChannelFriendly46_Object = MibTableColumn
powerDMChannelFriendly46 = _PowerDMChannelFriendly46_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 102),
    _PowerDMChannelFriendly46_Type()
)
powerDMChannelFriendly46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly46.setStatus("current")
_PowerDMChannelFriendly47_Type = DisplayString
_PowerDMChannelFriendly47_Object = MibTableColumn
powerDMChannelFriendly47 = _PowerDMChannelFriendly47_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 103),
    _PowerDMChannelFriendly47_Type()
)
powerDMChannelFriendly47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly47.setStatus("current")
_PowerDMChannelFriendly48_Type = DisplayString
_PowerDMChannelFriendly48_Object = MibTableColumn
powerDMChannelFriendly48 = _PowerDMChannelFriendly48_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 104),
    _PowerDMChannelFriendly48_Type()
)
powerDMChannelFriendly48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly48.setStatus("current")
_PowerDMChannelGroup1_Type = DisplayString
_PowerDMChannelGroup1_Object = MibTableColumn
powerDMChannelGroup1 = _PowerDMChannelGroup1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 105),
    _PowerDMChannelGroup1_Type()
)
powerDMChannelGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup1.setStatus("current")
_PowerDMChannelGroup2_Type = DisplayString
_PowerDMChannelGroup2_Object = MibTableColumn
powerDMChannelGroup2 = _PowerDMChannelGroup2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 106),
    _PowerDMChannelGroup2_Type()
)
powerDMChannelGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup2.setStatus("current")
_PowerDMChannelGroup3_Type = DisplayString
_PowerDMChannelGroup3_Object = MibTableColumn
powerDMChannelGroup3 = _PowerDMChannelGroup3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 107),
    _PowerDMChannelGroup3_Type()
)
powerDMChannelGroup3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup3.setStatus("current")
_PowerDMChannelGroup4_Type = DisplayString
_PowerDMChannelGroup4_Object = MibTableColumn
powerDMChannelGroup4 = _PowerDMChannelGroup4_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 108),
    _PowerDMChannelGroup4_Type()
)
powerDMChannelGroup4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup4.setStatus("current")
_PowerDMChannelGroup5_Type = DisplayString
_PowerDMChannelGroup5_Object = MibTableColumn
powerDMChannelGroup5 = _PowerDMChannelGroup5_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 109),
    _PowerDMChannelGroup5_Type()
)
powerDMChannelGroup5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup5.setStatus("current")
_PowerDMChannelGroup6_Type = DisplayString
_PowerDMChannelGroup6_Object = MibTableColumn
powerDMChannelGroup6 = _PowerDMChannelGroup6_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 110),
    _PowerDMChannelGroup6_Type()
)
powerDMChannelGroup6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup6.setStatus("current")
_PowerDMChannelGroup7_Type = DisplayString
_PowerDMChannelGroup7_Object = MibTableColumn
powerDMChannelGroup7 = _PowerDMChannelGroup7_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 111),
    _PowerDMChannelGroup7_Type()
)
powerDMChannelGroup7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup7.setStatus("current")
_PowerDMChannelGroup8_Type = DisplayString
_PowerDMChannelGroup8_Object = MibTableColumn
powerDMChannelGroup8 = _PowerDMChannelGroup8_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 112),
    _PowerDMChannelGroup8_Type()
)
powerDMChannelGroup8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup8.setStatus("current")
_PowerDMChannelGroup9_Type = DisplayString
_PowerDMChannelGroup9_Object = MibTableColumn
powerDMChannelGroup9 = _PowerDMChannelGroup9_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 113),
    _PowerDMChannelGroup9_Type()
)
powerDMChannelGroup9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup9.setStatus("current")
_PowerDMChannelGroup10_Type = DisplayString
_PowerDMChannelGroup10_Object = MibTableColumn
powerDMChannelGroup10 = _PowerDMChannelGroup10_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 114),
    _PowerDMChannelGroup10_Type()
)
powerDMChannelGroup10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup10.setStatus("current")
_PowerDMChannelGroup11_Type = DisplayString
_PowerDMChannelGroup11_Object = MibTableColumn
powerDMChannelGroup11 = _PowerDMChannelGroup11_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 115),
    _PowerDMChannelGroup11_Type()
)
powerDMChannelGroup11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup11.setStatus("current")
_PowerDMChannelGroup12_Type = DisplayString
_PowerDMChannelGroup12_Object = MibTableColumn
powerDMChannelGroup12 = _PowerDMChannelGroup12_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 116),
    _PowerDMChannelGroup12_Type()
)
powerDMChannelGroup12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup12.setStatus("current")
_PowerDMChannelGroup13_Type = DisplayString
_PowerDMChannelGroup13_Object = MibTableColumn
powerDMChannelGroup13 = _PowerDMChannelGroup13_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 117),
    _PowerDMChannelGroup13_Type()
)
powerDMChannelGroup13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup13.setStatus("current")
_PowerDMChannelGroup14_Type = DisplayString
_PowerDMChannelGroup14_Object = MibTableColumn
powerDMChannelGroup14 = _PowerDMChannelGroup14_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 118),
    _PowerDMChannelGroup14_Type()
)
powerDMChannelGroup14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup14.setStatus("current")
_PowerDMChannelGroup15_Type = DisplayString
_PowerDMChannelGroup15_Object = MibTableColumn
powerDMChannelGroup15 = _PowerDMChannelGroup15_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 119),
    _PowerDMChannelGroup15_Type()
)
powerDMChannelGroup15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup15.setStatus("current")
_PowerDMChannelGroup16_Type = DisplayString
_PowerDMChannelGroup16_Object = MibTableColumn
powerDMChannelGroup16 = _PowerDMChannelGroup16_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 120),
    _PowerDMChannelGroup16_Type()
)
powerDMChannelGroup16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup16.setStatus("current")
_PowerDMChannelGroup17_Type = DisplayString
_PowerDMChannelGroup17_Object = MibTableColumn
powerDMChannelGroup17 = _PowerDMChannelGroup17_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 121),
    _PowerDMChannelGroup17_Type()
)
powerDMChannelGroup17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup17.setStatus("current")
_PowerDMChannelGroup18_Type = DisplayString
_PowerDMChannelGroup18_Object = MibTableColumn
powerDMChannelGroup18 = _PowerDMChannelGroup18_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 122),
    _PowerDMChannelGroup18_Type()
)
powerDMChannelGroup18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup18.setStatus("current")
_PowerDMChannelGroup19_Type = DisplayString
_PowerDMChannelGroup19_Object = MibTableColumn
powerDMChannelGroup19 = _PowerDMChannelGroup19_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 123),
    _PowerDMChannelGroup19_Type()
)
powerDMChannelGroup19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup19.setStatus("current")
_PowerDMChannelGroup20_Type = DisplayString
_PowerDMChannelGroup20_Object = MibTableColumn
powerDMChannelGroup20 = _PowerDMChannelGroup20_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 124),
    _PowerDMChannelGroup20_Type()
)
powerDMChannelGroup20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup20.setStatus("current")
_PowerDMChannelGroup21_Type = DisplayString
_PowerDMChannelGroup21_Object = MibTableColumn
powerDMChannelGroup21 = _PowerDMChannelGroup21_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 125),
    _PowerDMChannelGroup21_Type()
)
powerDMChannelGroup21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup21.setStatus("current")
_PowerDMChannelGroup22_Type = DisplayString
_PowerDMChannelGroup22_Object = MibTableColumn
powerDMChannelGroup22 = _PowerDMChannelGroup22_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 126),
    _PowerDMChannelGroup22_Type()
)
powerDMChannelGroup22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup22.setStatus("current")
_PowerDMChannelGroup23_Type = DisplayString
_PowerDMChannelGroup23_Object = MibTableColumn
powerDMChannelGroup23 = _PowerDMChannelGroup23_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 127),
    _PowerDMChannelGroup23_Type()
)
powerDMChannelGroup23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup23.setStatus("current")
_PowerDMChannelGroup24_Type = DisplayString
_PowerDMChannelGroup24_Object = MibTableColumn
powerDMChannelGroup24 = _PowerDMChannelGroup24_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 128),
    _PowerDMChannelGroup24_Type()
)
powerDMChannelGroup24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup24.setStatus("current")
_PowerDMChannelGroup25_Type = DisplayString
_PowerDMChannelGroup25_Object = MibTableColumn
powerDMChannelGroup25 = _PowerDMChannelGroup25_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 129),
    _PowerDMChannelGroup25_Type()
)
powerDMChannelGroup25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup25.setStatus("current")
_PowerDMChannelGroup26_Type = DisplayString
_PowerDMChannelGroup26_Object = MibTableColumn
powerDMChannelGroup26 = _PowerDMChannelGroup26_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 130),
    _PowerDMChannelGroup26_Type()
)
powerDMChannelGroup26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup26.setStatus("current")
_PowerDMChannelGroup27_Type = DisplayString
_PowerDMChannelGroup27_Object = MibTableColumn
powerDMChannelGroup27 = _PowerDMChannelGroup27_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 131),
    _PowerDMChannelGroup27_Type()
)
powerDMChannelGroup27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup27.setStatus("current")
_PowerDMChannelGroup28_Type = DisplayString
_PowerDMChannelGroup28_Object = MibTableColumn
powerDMChannelGroup28 = _PowerDMChannelGroup28_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 132),
    _PowerDMChannelGroup28_Type()
)
powerDMChannelGroup28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup28.setStatus("current")
_PowerDMChannelGroup29_Type = DisplayString
_PowerDMChannelGroup29_Object = MibTableColumn
powerDMChannelGroup29 = _PowerDMChannelGroup29_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 133),
    _PowerDMChannelGroup29_Type()
)
powerDMChannelGroup29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup29.setStatus("current")
_PowerDMChannelGroup30_Type = DisplayString
_PowerDMChannelGroup30_Object = MibTableColumn
powerDMChannelGroup30 = _PowerDMChannelGroup30_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 134),
    _PowerDMChannelGroup30_Type()
)
powerDMChannelGroup30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup30.setStatus("current")
_PowerDMChannelGroup31_Type = DisplayString
_PowerDMChannelGroup31_Object = MibTableColumn
powerDMChannelGroup31 = _PowerDMChannelGroup31_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 135),
    _PowerDMChannelGroup31_Type()
)
powerDMChannelGroup31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup31.setStatus("current")
_PowerDMChannelGroup32_Type = DisplayString
_PowerDMChannelGroup32_Object = MibTableColumn
powerDMChannelGroup32 = _PowerDMChannelGroup32_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 136),
    _PowerDMChannelGroup32_Type()
)
powerDMChannelGroup32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup32.setStatus("current")
_PowerDMChannelGroup33_Type = DisplayString
_PowerDMChannelGroup33_Object = MibTableColumn
powerDMChannelGroup33 = _PowerDMChannelGroup33_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 137),
    _PowerDMChannelGroup33_Type()
)
powerDMChannelGroup33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup33.setStatus("current")
_PowerDMChannelGroup34_Type = DisplayString
_PowerDMChannelGroup34_Object = MibTableColumn
powerDMChannelGroup34 = _PowerDMChannelGroup34_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 138),
    _PowerDMChannelGroup34_Type()
)
powerDMChannelGroup34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup34.setStatus("current")
_PowerDMChannelGroup35_Type = DisplayString
_PowerDMChannelGroup35_Object = MibTableColumn
powerDMChannelGroup35 = _PowerDMChannelGroup35_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 139),
    _PowerDMChannelGroup35_Type()
)
powerDMChannelGroup35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup35.setStatus("current")
_PowerDMChannelGroup36_Type = DisplayString
_PowerDMChannelGroup36_Object = MibTableColumn
powerDMChannelGroup36 = _PowerDMChannelGroup36_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 140),
    _PowerDMChannelGroup36_Type()
)
powerDMChannelGroup36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup36.setStatus("current")
_PowerDMChannelGroup37_Type = DisplayString
_PowerDMChannelGroup37_Object = MibTableColumn
powerDMChannelGroup37 = _PowerDMChannelGroup37_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 141),
    _PowerDMChannelGroup37_Type()
)
powerDMChannelGroup37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup37.setStatus("current")
_PowerDMChannelGroup38_Type = DisplayString
_PowerDMChannelGroup38_Object = MibTableColumn
powerDMChannelGroup38 = _PowerDMChannelGroup38_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 142),
    _PowerDMChannelGroup38_Type()
)
powerDMChannelGroup38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup38.setStatus("current")
_PowerDMChannelGroup39_Type = DisplayString
_PowerDMChannelGroup39_Object = MibTableColumn
powerDMChannelGroup39 = _PowerDMChannelGroup39_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 143),
    _PowerDMChannelGroup39_Type()
)
powerDMChannelGroup39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup39.setStatus("current")
_PowerDMChannelGroup40_Type = DisplayString
_PowerDMChannelGroup40_Object = MibTableColumn
powerDMChannelGroup40 = _PowerDMChannelGroup40_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 144),
    _PowerDMChannelGroup40_Type()
)
powerDMChannelGroup40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup40.setStatus("current")
_PowerDMChannelGroup41_Type = DisplayString
_PowerDMChannelGroup41_Object = MibTableColumn
powerDMChannelGroup41 = _PowerDMChannelGroup41_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 145),
    _PowerDMChannelGroup41_Type()
)
powerDMChannelGroup41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup41.setStatus("current")
_PowerDMChannelGroup42_Type = DisplayString
_PowerDMChannelGroup42_Object = MibTableColumn
powerDMChannelGroup42 = _PowerDMChannelGroup42_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 146),
    _PowerDMChannelGroup42_Type()
)
powerDMChannelGroup42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup42.setStatus("current")
_PowerDMChannelGroup43_Type = DisplayString
_PowerDMChannelGroup43_Object = MibTableColumn
powerDMChannelGroup43 = _PowerDMChannelGroup43_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 147),
    _PowerDMChannelGroup43_Type()
)
powerDMChannelGroup43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup43.setStatus("current")
_PowerDMChannelGroup44_Type = DisplayString
_PowerDMChannelGroup44_Object = MibTableColumn
powerDMChannelGroup44 = _PowerDMChannelGroup44_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 148),
    _PowerDMChannelGroup44_Type()
)
powerDMChannelGroup44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup44.setStatus("current")
_PowerDMChannelGroup45_Type = DisplayString
_PowerDMChannelGroup45_Object = MibTableColumn
powerDMChannelGroup45 = _PowerDMChannelGroup45_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 149),
    _PowerDMChannelGroup45_Type()
)
powerDMChannelGroup45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup45.setStatus("current")
_PowerDMChannelGroup46_Type = DisplayString
_PowerDMChannelGroup46_Object = MibTableColumn
powerDMChannelGroup46 = _PowerDMChannelGroup46_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 150),
    _PowerDMChannelGroup46_Type()
)
powerDMChannelGroup46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup46.setStatus("current")
_PowerDMChannelGroup47_Type = DisplayString
_PowerDMChannelGroup47_Object = MibTableColumn
powerDMChannelGroup47 = _PowerDMChannelGroup47_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 151),
    _PowerDMChannelGroup47_Type()
)
powerDMChannelGroup47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup47.setStatus("current")
_PowerDMChannelGroup48_Type = DisplayString
_PowerDMChannelGroup48_Object = MibTableColumn
powerDMChannelGroup48 = _PowerDMChannelGroup48_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 152),
    _PowerDMChannelGroup48_Type()
)
powerDMChannelGroup48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup48.setStatus("current")


class _PowerDMDeciAmps1_Type(Integer32):
    """Custom type powerDMDeciAmps1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps1_Type.__name__ = "Integer32"
_PowerDMDeciAmps1_Object = MibTableColumn
powerDMDeciAmps1 = _PowerDMDeciAmps1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 153),
    _PowerDMDeciAmps1_Type()
)
powerDMDeciAmps1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps1.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps1.setUnits("0.1 Amps")


class _PowerDMDeciAmps2_Type(Integer32):
    """Custom type powerDMDeciAmps2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps2_Type.__name__ = "Integer32"
_PowerDMDeciAmps2_Object = MibTableColumn
powerDMDeciAmps2 = _PowerDMDeciAmps2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 154),
    _PowerDMDeciAmps2_Type()
)
powerDMDeciAmps2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps2.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps2.setUnits("0.1 Amps")


class _PowerDMDeciAmps3_Type(Integer32):
    """Custom type powerDMDeciAmps3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps3_Type.__name__ = "Integer32"
_PowerDMDeciAmps3_Object = MibTableColumn
powerDMDeciAmps3 = _PowerDMDeciAmps3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 155),
    _PowerDMDeciAmps3_Type()
)
powerDMDeciAmps3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps3.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps3.setUnits("0.1 Amps")


class _PowerDMDeciAmps4_Type(Integer32):
    """Custom type powerDMDeciAmps4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps4_Type.__name__ = "Integer32"
_PowerDMDeciAmps4_Object = MibTableColumn
powerDMDeciAmps4 = _PowerDMDeciAmps4_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 156),
    _PowerDMDeciAmps4_Type()
)
powerDMDeciAmps4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps4.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps4.setUnits("0.1 Amps")


class _PowerDMDeciAmps5_Type(Integer32):
    """Custom type powerDMDeciAmps5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps5_Type.__name__ = "Integer32"
_PowerDMDeciAmps5_Object = MibTableColumn
powerDMDeciAmps5 = _PowerDMDeciAmps5_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 157),
    _PowerDMDeciAmps5_Type()
)
powerDMDeciAmps5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps5.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps5.setUnits("0.1 Amps")


class _PowerDMDeciAmps6_Type(Integer32):
    """Custom type powerDMDeciAmps6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps6_Type.__name__ = "Integer32"
_PowerDMDeciAmps6_Object = MibTableColumn
powerDMDeciAmps6 = _PowerDMDeciAmps6_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 158),
    _PowerDMDeciAmps6_Type()
)
powerDMDeciAmps6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps6.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps6.setUnits("0.1 Amps")


class _PowerDMDeciAmps7_Type(Integer32):
    """Custom type powerDMDeciAmps7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps7_Type.__name__ = "Integer32"
_PowerDMDeciAmps7_Object = MibTableColumn
powerDMDeciAmps7 = _PowerDMDeciAmps7_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 159),
    _PowerDMDeciAmps7_Type()
)
powerDMDeciAmps7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps7.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps7.setUnits("0.1 Amps")


class _PowerDMDeciAmps8_Type(Integer32):
    """Custom type powerDMDeciAmps8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps8_Type.__name__ = "Integer32"
_PowerDMDeciAmps8_Object = MibTableColumn
powerDMDeciAmps8 = _PowerDMDeciAmps8_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 160),
    _PowerDMDeciAmps8_Type()
)
powerDMDeciAmps8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps8.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps8.setUnits("0.1 Amps")


class _PowerDMDeciAmps9_Type(Integer32):
    """Custom type powerDMDeciAmps9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps9_Type.__name__ = "Integer32"
_PowerDMDeciAmps9_Object = MibTableColumn
powerDMDeciAmps9 = _PowerDMDeciAmps9_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 161),
    _PowerDMDeciAmps9_Type()
)
powerDMDeciAmps9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps9.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps9.setUnits("0.1 Amps")


class _PowerDMDeciAmps10_Type(Integer32):
    """Custom type powerDMDeciAmps10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps10_Type.__name__ = "Integer32"
_PowerDMDeciAmps10_Object = MibTableColumn
powerDMDeciAmps10 = _PowerDMDeciAmps10_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 162),
    _PowerDMDeciAmps10_Type()
)
powerDMDeciAmps10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps10.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps10.setUnits("0.1 Amps")


class _PowerDMDeciAmps11_Type(Integer32):
    """Custom type powerDMDeciAmps11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps11_Type.__name__ = "Integer32"
_PowerDMDeciAmps11_Object = MibTableColumn
powerDMDeciAmps11 = _PowerDMDeciAmps11_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 163),
    _PowerDMDeciAmps11_Type()
)
powerDMDeciAmps11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps11.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps11.setUnits("0.1 Amps")


class _PowerDMDeciAmps12_Type(Integer32):
    """Custom type powerDMDeciAmps12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps12_Type.__name__ = "Integer32"
_PowerDMDeciAmps12_Object = MibTableColumn
powerDMDeciAmps12 = _PowerDMDeciAmps12_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 164),
    _PowerDMDeciAmps12_Type()
)
powerDMDeciAmps12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps12.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps12.setUnits("0.1 Amps")


class _PowerDMDeciAmps13_Type(Integer32):
    """Custom type powerDMDeciAmps13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps13_Type.__name__ = "Integer32"
_PowerDMDeciAmps13_Object = MibTableColumn
powerDMDeciAmps13 = _PowerDMDeciAmps13_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 165),
    _PowerDMDeciAmps13_Type()
)
powerDMDeciAmps13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps13.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps13.setUnits("0.1 Amps")


class _PowerDMDeciAmps14_Type(Integer32):
    """Custom type powerDMDeciAmps14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps14_Type.__name__ = "Integer32"
_PowerDMDeciAmps14_Object = MibTableColumn
powerDMDeciAmps14 = _PowerDMDeciAmps14_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 166),
    _PowerDMDeciAmps14_Type()
)
powerDMDeciAmps14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps14.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps14.setUnits("0.1 Amps")


class _PowerDMDeciAmps15_Type(Integer32):
    """Custom type powerDMDeciAmps15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps15_Type.__name__ = "Integer32"
_PowerDMDeciAmps15_Object = MibTableColumn
powerDMDeciAmps15 = _PowerDMDeciAmps15_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 167),
    _PowerDMDeciAmps15_Type()
)
powerDMDeciAmps15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps15.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps15.setUnits("0.1 Amps")


class _PowerDMDeciAmps16_Type(Integer32):
    """Custom type powerDMDeciAmps16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps16_Type.__name__ = "Integer32"
_PowerDMDeciAmps16_Object = MibTableColumn
powerDMDeciAmps16 = _PowerDMDeciAmps16_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 168),
    _PowerDMDeciAmps16_Type()
)
powerDMDeciAmps16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps16.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps16.setUnits("0.1 Amps")


class _PowerDMDeciAmps17_Type(Integer32):
    """Custom type powerDMDeciAmps17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps17_Type.__name__ = "Integer32"
_PowerDMDeciAmps17_Object = MibTableColumn
powerDMDeciAmps17 = _PowerDMDeciAmps17_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 169),
    _PowerDMDeciAmps17_Type()
)
powerDMDeciAmps17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps17.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps17.setUnits("0.1 Amps")


class _PowerDMDeciAmps18_Type(Integer32):
    """Custom type powerDMDeciAmps18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps18_Type.__name__ = "Integer32"
_PowerDMDeciAmps18_Object = MibTableColumn
powerDMDeciAmps18 = _PowerDMDeciAmps18_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 170),
    _PowerDMDeciAmps18_Type()
)
powerDMDeciAmps18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps18.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps18.setUnits("0.1 Amps")


class _PowerDMDeciAmps19_Type(Integer32):
    """Custom type powerDMDeciAmps19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps19_Type.__name__ = "Integer32"
_PowerDMDeciAmps19_Object = MibTableColumn
powerDMDeciAmps19 = _PowerDMDeciAmps19_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 171),
    _PowerDMDeciAmps19_Type()
)
powerDMDeciAmps19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps19.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps19.setUnits("0.1 Amps")


class _PowerDMDeciAmps20_Type(Integer32):
    """Custom type powerDMDeciAmps20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps20_Type.__name__ = "Integer32"
_PowerDMDeciAmps20_Object = MibTableColumn
powerDMDeciAmps20 = _PowerDMDeciAmps20_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 172),
    _PowerDMDeciAmps20_Type()
)
powerDMDeciAmps20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps20.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps20.setUnits("0.1 Amps")


class _PowerDMDeciAmps21_Type(Integer32):
    """Custom type powerDMDeciAmps21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps21_Type.__name__ = "Integer32"
_PowerDMDeciAmps21_Object = MibTableColumn
powerDMDeciAmps21 = _PowerDMDeciAmps21_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 173),
    _PowerDMDeciAmps21_Type()
)
powerDMDeciAmps21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps21.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps21.setUnits("0.1 Amps")


class _PowerDMDeciAmps22_Type(Integer32):
    """Custom type powerDMDeciAmps22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps22_Type.__name__ = "Integer32"
_PowerDMDeciAmps22_Object = MibTableColumn
powerDMDeciAmps22 = _PowerDMDeciAmps22_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 174),
    _PowerDMDeciAmps22_Type()
)
powerDMDeciAmps22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps22.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps22.setUnits("0.1 Amps")


class _PowerDMDeciAmps23_Type(Integer32):
    """Custom type powerDMDeciAmps23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps23_Type.__name__ = "Integer32"
_PowerDMDeciAmps23_Object = MibTableColumn
powerDMDeciAmps23 = _PowerDMDeciAmps23_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 175),
    _PowerDMDeciAmps23_Type()
)
powerDMDeciAmps23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps23.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps23.setUnits("0.1 Amps")


class _PowerDMDeciAmps24_Type(Integer32):
    """Custom type powerDMDeciAmps24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps24_Type.__name__ = "Integer32"
_PowerDMDeciAmps24_Object = MibTableColumn
powerDMDeciAmps24 = _PowerDMDeciAmps24_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 176),
    _PowerDMDeciAmps24_Type()
)
powerDMDeciAmps24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps24.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps24.setUnits("0.1 Amps")


class _PowerDMDeciAmps25_Type(Integer32):
    """Custom type powerDMDeciAmps25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps25_Type.__name__ = "Integer32"
_PowerDMDeciAmps25_Object = MibTableColumn
powerDMDeciAmps25 = _PowerDMDeciAmps25_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 177),
    _PowerDMDeciAmps25_Type()
)
powerDMDeciAmps25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps25.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps25.setUnits("0.1 Amps")


class _PowerDMDeciAmps26_Type(Integer32):
    """Custom type powerDMDeciAmps26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps26_Type.__name__ = "Integer32"
_PowerDMDeciAmps26_Object = MibTableColumn
powerDMDeciAmps26 = _PowerDMDeciAmps26_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 178),
    _PowerDMDeciAmps26_Type()
)
powerDMDeciAmps26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps26.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps26.setUnits("0.1 Amps")


class _PowerDMDeciAmps27_Type(Integer32):
    """Custom type powerDMDeciAmps27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps27_Type.__name__ = "Integer32"
_PowerDMDeciAmps27_Object = MibTableColumn
powerDMDeciAmps27 = _PowerDMDeciAmps27_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 179),
    _PowerDMDeciAmps27_Type()
)
powerDMDeciAmps27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps27.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps27.setUnits("0.1 Amps")


class _PowerDMDeciAmps28_Type(Integer32):
    """Custom type powerDMDeciAmps28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps28_Type.__name__ = "Integer32"
_PowerDMDeciAmps28_Object = MibTableColumn
powerDMDeciAmps28 = _PowerDMDeciAmps28_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 180),
    _PowerDMDeciAmps28_Type()
)
powerDMDeciAmps28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps28.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps28.setUnits("0.1 Amps")


class _PowerDMDeciAmps29_Type(Integer32):
    """Custom type powerDMDeciAmps29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps29_Type.__name__ = "Integer32"
_PowerDMDeciAmps29_Object = MibTableColumn
powerDMDeciAmps29 = _PowerDMDeciAmps29_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 181),
    _PowerDMDeciAmps29_Type()
)
powerDMDeciAmps29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps29.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps29.setUnits("0.1 Amps")


class _PowerDMDeciAmps30_Type(Integer32):
    """Custom type powerDMDeciAmps30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps30_Type.__name__ = "Integer32"
_PowerDMDeciAmps30_Object = MibTableColumn
powerDMDeciAmps30 = _PowerDMDeciAmps30_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 182),
    _PowerDMDeciAmps30_Type()
)
powerDMDeciAmps30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps30.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps30.setUnits("0.1 Amps")


class _PowerDMDeciAmps31_Type(Integer32):
    """Custom type powerDMDeciAmps31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps31_Type.__name__ = "Integer32"
_PowerDMDeciAmps31_Object = MibTableColumn
powerDMDeciAmps31 = _PowerDMDeciAmps31_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 183),
    _PowerDMDeciAmps31_Type()
)
powerDMDeciAmps31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps31.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps31.setUnits("0.1 Amps")


class _PowerDMDeciAmps32_Type(Integer32):
    """Custom type powerDMDeciAmps32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps32_Type.__name__ = "Integer32"
_PowerDMDeciAmps32_Object = MibTableColumn
powerDMDeciAmps32 = _PowerDMDeciAmps32_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 184),
    _PowerDMDeciAmps32_Type()
)
powerDMDeciAmps32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps32.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps32.setUnits("0.1 Amps")


class _PowerDMDeciAmps33_Type(Integer32):
    """Custom type powerDMDeciAmps33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps33_Type.__name__ = "Integer32"
_PowerDMDeciAmps33_Object = MibTableColumn
powerDMDeciAmps33 = _PowerDMDeciAmps33_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 185),
    _PowerDMDeciAmps33_Type()
)
powerDMDeciAmps33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps33.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps33.setUnits("0.1 Amps")


class _PowerDMDeciAmps34_Type(Integer32):
    """Custom type powerDMDeciAmps34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps34_Type.__name__ = "Integer32"
_PowerDMDeciAmps34_Object = MibTableColumn
powerDMDeciAmps34 = _PowerDMDeciAmps34_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 186),
    _PowerDMDeciAmps34_Type()
)
powerDMDeciAmps34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps34.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps34.setUnits("0.1 Amps")


class _PowerDMDeciAmps35_Type(Integer32):
    """Custom type powerDMDeciAmps35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps35_Type.__name__ = "Integer32"
_PowerDMDeciAmps35_Object = MibTableColumn
powerDMDeciAmps35 = _PowerDMDeciAmps35_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 187),
    _PowerDMDeciAmps35_Type()
)
powerDMDeciAmps35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps35.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps35.setUnits("0.1 Amps")


class _PowerDMDeciAmps36_Type(Integer32):
    """Custom type powerDMDeciAmps36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps36_Type.__name__ = "Integer32"
_PowerDMDeciAmps36_Object = MibTableColumn
powerDMDeciAmps36 = _PowerDMDeciAmps36_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 188),
    _PowerDMDeciAmps36_Type()
)
powerDMDeciAmps36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps36.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps36.setUnits("0.1 Amps")


class _PowerDMDeciAmps37_Type(Integer32):
    """Custom type powerDMDeciAmps37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps37_Type.__name__ = "Integer32"
_PowerDMDeciAmps37_Object = MibTableColumn
powerDMDeciAmps37 = _PowerDMDeciAmps37_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 189),
    _PowerDMDeciAmps37_Type()
)
powerDMDeciAmps37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps37.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps37.setUnits("0.1 Amps")


class _PowerDMDeciAmps38_Type(Integer32):
    """Custom type powerDMDeciAmps38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps38_Type.__name__ = "Integer32"
_PowerDMDeciAmps38_Object = MibTableColumn
powerDMDeciAmps38 = _PowerDMDeciAmps38_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 190),
    _PowerDMDeciAmps38_Type()
)
powerDMDeciAmps38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps38.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps38.setUnits("0.1 Amps")


class _PowerDMDeciAmps39_Type(Integer32):
    """Custom type powerDMDeciAmps39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps39_Type.__name__ = "Integer32"
_PowerDMDeciAmps39_Object = MibTableColumn
powerDMDeciAmps39 = _PowerDMDeciAmps39_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 191),
    _PowerDMDeciAmps39_Type()
)
powerDMDeciAmps39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps39.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps39.setUnits("0.1 Amps")


class _PowerDMDeciAmps40_Type(Integer32):
    """Custom type powerDMDeciAmps40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps40_Type.__name__ = "Integer32"
_PowerDMDeciAmps40_Object = MibTableColumn
powerDMDeciAmps40 = _PowerDMDeciAmps40_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 192),
    _PowerDMDeciAmps40_Type()
)
powerDMDeciAmps40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps40.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps40.setUnits("0.1 Amps")


class _PowerDMDeciAmps41_Type(Integer32):
    """Custom type powerDMDeciAmps41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps41_Type.__name__ = "Integer32"
_PowerDMDeciAmps41_Object = MibTableColumn
powerDMDeciAmps41 = _PowerDMDeciAmps41_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 193),
    _PowerDMDeciAmps41_Type()
)
powerDMDeciAmps41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps41.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps41.setUnits("0.1 Amps")


class _PowerDMDeciAmps42_Type(Integer32):
    """Custom type powerDMDeciAmps42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps42_Type.__name__ = "Integer32"
_PowerDMDeciAmps42_Object = MibTableColumn
powerDMDeciAmps42 = _PowerDMDeciAmps42_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 194),
    _PowerDMDeciAmps42_Type()
)
powerDMDeciAmps42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps42.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps42.setUnits("0.1 Amps")


class _PowerDMDeciAmps43_Type(Integer32):
    """Custom type powerDMDeciAmps43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps43_Type.__name__ = "Integer32"
_PowerDMDeciAmps43_Object = MibTableColumn
powerDMDeciAmps43 = _PowerDMDeciAmps43_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 195),
    _PowerDMDeciAmps43_Type()
)
powerDMDeciAmps43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps43.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps43.setUnits("0.1 Amps")


class _PowerDMDeciAmps44_Type(Integer32):
    """Custom type powerDMDeciAmps44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps44_Type.__name__ = "Integer32"
_PowerDMDeciAmps44_Object = MibTableColumn
powerDMDeciAmps44 = _PowerDMDeciAmps44_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 196),
    _PowerDMDeciAmps44_Type()
)
powerDMDeciAmps44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps44.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps44.setUnits("0.1 Amps")


class _PowerDMDeciAmps45_Type(Integer32):
    """Custom type powerDMDeciAmps45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps45_Type.__name__ = "Integer32"
_PowerDMDeciAmps45_Object = MibTableColumn
powerDMDeciAmps45 = _PowerDMDeciAmps45_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 197),
    _PowerDMDeciAmps45_Type()
)
powerDMDeciAmps45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps45.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps45.setUnits("0.1 Amps")


class _PowerDMDeciAmps46_Type(Integer32):
    """Custom type powerDMDeciAmps46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps46_Type.__name__ = "Integer32"
_PowerDMDeciAmps46_Object = MibTableColumn
powerDMDeciAmps46 = _PowerDMDeciAmps46_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 198),
    _PowerDMDeciAmps46_Type()
)
powerDMDeciAmps46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps46.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps46.setUnits("0.1 Amps")


class _PowerDMDeciAmps47_Type(Integer32):
    """Custom type powerDMDeciAmps47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps47_Type.__name__ = "Integer32"
_PowerDMDeciAmps47_Object = MibTableColumn
powerDMDeciAmps47 = _PowerDMDeciAmps47_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 199),
    _PowerDMDeciAmps47_Type()
)
powerDMDeciAmps47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps47.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps47.setUnits("0.1 Amps")


class _PowerDMDeciAmps48_Type(Integer32):
    """Custom type powerDMDeciAmps48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209),
    )


_PowerDMDeciAmps48_Type.__name__ = "Integer32"
_PowerDMDeciAmps48_Object = MibTableColumn
powerDMDeciAmps48 = _PowerDMDeciAmps48_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 29, 1, 200),
    _PowerDMDeciAmps48_Type()
)
powerDMDeciAmps48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps48.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps48.setUnits("0.1 Amps")
_IoExpanderTable_Object = MibTable
ioExpanderTable = _IoExpanderTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30)
)
if mibBuilder.loadTexts:
    ioExpanderTable.setStatus("current")
_IoExpanderEntry_Object = MibTableRow
ioExpanderEntry = _IoExpanderEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1)
)
ioExpanderEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "ioExpanderIndex"),
)
if mibBuilder.loadTexts:
    ioExpanderEntry.setStatus("current")


class _IoExpanderIndex_Type(Integer32):
    """Custom type ioExpanderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IoExpanderIndex_Type.__name__ = "Integer32"
_IoExpanderIndex_Object = MibTableColumn
ioExpanderIndex = _IoExpanderIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 1),
    _IoExpanderIndex_Type()
)
ioExpanderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ioExpanderIndex.setStatus("current")
_IoExpanderSerial_Type = DisplayString
_IoExpanderSerial_Object = MibTableColumn
ioExpanderSerial = _IoExpanderSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 2),
    _IoExpanderSerial_Type()
)
ioExpanderSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderSerial.setStatus("current")
_IoExpanderName_Type = DisplayString
_IoExpanderName_Object = MibTableColumn
ioExpanderName = _IoExpanderName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 3),
    _IoExpanderName_Type()
)
ioExpanderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderName.setStatus("current")
_IoExpanderAvail_Type = Gauge32
_IoExpanderAvail_Object = MibTableColumn
ioExpanderAvail = _IoExpanderAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 4),
    _IoExpanderAvail_Type()
)
ioExpanderAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderAvail.setStatus("current")
_IoExpanderFriendlyName1_Type = DisplayString
_IoExpanderFriendlyName1_Object = MibTableColumn
ioExpanderFriendlyName1 = _IoExpanderFriendlyName1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 5),
    _IoExpanderFriendlyName1_Type()
)
ioExpanderFriendlyName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName1.setStatus("current")
_IoExpanderFriendlyName2_Type = DisplayString
_IoExpanderFriendlyName2_Object = MibTableColumn
ioExpanderFriendlyName2 = _IoExpanderFriendlyName2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 6),
    _IoExpanderFriendlyName2_Type()
)
ioExpanderFriendlyName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName2.setStatus("current")
_IoExpanderFriendlyName3_Type = DisplayString
_IoExpanderFriendlyName3_Object = MibTableColumn
ioExpanderFriendlyName3 = _IoExpanderFriendlyName3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 7),
    _IoExpanderFriendlyName3_Type()
)
ioExpanderFriendlyName3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName3.setStatus("current")
_IoExpanderFriendlyName4_Type = DisplayString
_IoExpanderFriendlyName4_Object = MibTableColumn
ioExpanderFriendlyName4 = _IoExpanderFriendlyName4_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 8),
    _IoExpanderFriendlyName4_Type()
)
ioExpanderFriendlyName4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName4.setStatus("current")
_IoExpanderFriendlyName5_Type = DisplayString
_IoExpanderFriendlyName5_Object = MibTableColumn
ioExpanderFriendlyName5 = _IoExpanderFriendlyName5_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 9),
    _IoExpanderFriendlyName5_Type()
)
ioExpanderFriendlyName5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName5.setStatus("current")
_IoExpanderFriendlyName6_Type = DisplayString
_IoExpanderFriendlyName6_Object = MibTableColumn
ioExpanderFriendlyName6 = _IoExpanderFriendlyName6_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 10),
    _IoExpanderFriendlyName6_Type()
)
ioExpanderFriendlyName6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName6.setStatus("current")
_IoExpanderFriendlyName7_Type = DisplayString
_IoExpanderFriendlyName7_Object = MibTableColumn
ioExpanderFriendlyName7 = _IoExpanderFriendlyName7_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 11),
    _IoExpanderFriendlyName7_Type()
)
ioExpanderFriendlyName7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName7.setStatus("current")
_IoExpanderFriendlyName8_Type = DisplayString
_IoExpanderFriendlyName8_Object = MibTableColumn
ioExpanderFriendlyName8 = _IoExpanderFriendlyName8_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 12),
    _IoExpanderFriendlyName8_Type()
)
ioExpanderFriendlyName8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName8.setStatus("current")
_IoExpanderFriendlyName9_Type = DisplayString
_IoExpanderFriendlyName9_Object = MibTableColumn
ioExpanderFriendlyName9 = _IoExpanderFriendlyName9_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 13),
    _IoExpanderFriendlyName9_Type()
)
ioExpanderFriendlyName9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName9.setStatus("current")
_IoExpanderFriendlyName10_Type = DisplayString
_IoExpanderFriendlyName10_Object = MibTableColumn
ioExpanderFriendlyName10 = _IoExpanderFriendlyName10_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 14),
    _IoExpanderFriendlyName10_Type()
)
ioExpanderFriendlyName10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName10.setStatus("current")
_IoExpanderFriendlyName11_Type = DisplayString
_IoExpanderFriendlyName11_Object = MibTableColumn
ioExpanderFriendlyName11 = _IoExpanderFriendlyName11_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 15),
    _IoExpanderFriendlyName11_Type()
)
ioExpanderFriendlyName11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName11.setStatus("current")
_IoExpanderFriendlyName12_Type = DisplayString
_IoExpanderFriendlyName12_Object = MibTableColumn
ioExpanderFriendlyName12 = _IoExpanderFriendlyName12_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 16),
    _IoExpanderFriendlyName12_Type()
)
ioExpanderFriendlyName12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName12.setStatus("current")
_IoExpanderFriendlyName13_Type = DisplayString
_IoExpanderFriendlyName13_Object = MibTableColumn
ioExpanderFriendlyName13 = _IoExpanderFriendlyName13_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 17),
    _IoExpanderFriendlyName13_Type()
)
ioExpanderFriendlyName13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName13.setStatus("current")
_IoExpanderFriendlyName14_Type = DisplayString
_IoExpanderFriendlyName14_Object = MibTableColumn
ioExpanderFriendlyName14 = _IoExpanderFriendlyName14_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 18),
    _IoExpanderFriendlyName14_Type()
)
ioExpanderFriendlyName14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName14.setStatus("current")
_IoExpanderFriendlyName15_Type = DisplayString
_IoExpanderFriendlyName15_Object = MibTableColumn
ioExpanderFriendlyName15 = _IoExpanderFriendlyName15_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 19),
    _IoExpanderFriendlyName15_Type()
)
ioExpanderFriendlyName15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName15.setStatus("current")
_IoExpanderFriendlyName16_Type = DisplayString
_IoExpanderFriendlyName16_Object = MibTableColumn
ioExpanderFriendlyName16 = _IoExpanderFriendlyName16_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 20),
    _IoExpanderFriendlyName16_Type()
)
ioExpanderFriendlyName16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName16.setStatus("current")
_IoExpanderFriendlyName17_Type = DisplayString
_IoExpanderFriendlyName17_Object = MibTableColumn
ioExpanderFriendlyName17 = _IoExpanderFriendlyName17_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 21),
    _IoExpanderFriendlyName17_Type()
)
ioExpanderFriendlyName17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName17.setStatus("current")
_IoExpanderFriendlyName18_Type = DisplayString
_IoExpanderFriendlyName18_Object = MibTableColumn
ioExpanderFriendlyName18 = _IoExpanderFriendlyName18_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 22),
    _IoExpanderFriendlyName18_Type()
)
ioExpanderFriendlyName18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName18.setStatus("current")
_IoExpanderFriendlyName19_Type = DisplayString
_IoExpanderFriendlyName19_Object = MibTableColumn
ioExpanderFriendlyName19 = _IoExpanderFriendlyName19_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 23),
    _IoExpanderFriendlyName19_Type()
)
ioExpanderFriendlyName19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName19.setStatus("current")
_IoExpanderFriendlyName20_Type = DisplayString
_IoExpanderFriendlyName20_Object = MibTableColumn
ioExpanderFriendlyName20 = _IoExpanderFriendlyName20_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 24),
    _IoExpanderFriendlyName20_Type()
)
ioExpanderFriendlyName20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName20.setStatus("current")
_IoExpanderFriendlyName21_Type = DisplayString
_IoExpanderFriendlyName21_Object = MibTableColumn
ioExpanderFriendlyName21 = _IoExpanderFriendlyName21_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 25),
    _IoExpanderFriendlyName21_Type()
)
ioExpanderFriendlyName21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName21.setStatus("current")
_IoExpanderFriendlyName22_Type = DisplayString
_IoExpanderFriendlyName22_Object = MibTableColumn
ioExpanderFriendlyName22 = _IoExpanderFriendlyName22_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 26),
    _IoExpanderFriendlyName22_Type()
)
ioExpanderFriendlyName22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName22.setStatus("current")
_IoExpanderFriendlyName23_Type = DisplayString
_IoExpanderFriendlyName23_Object = MibTableColumn
ioExpanderFriendlyName23 = _IoExpanderFriendlyName23_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 27),
    _IoExpanderFriendlyName23_Type()
)
ioExpanderFriendlyName23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName23.setStatus("current")
_IoExpanderFriendlyName24_Type = DisplayString
_IoExpanderFriendlyName24_Object = MibTableColumn
ioExpanderFriendlyName24 = _IoExpanderFriendlyName24_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 28),
    _IoExpanderFriendlyName24_Type()
)
ioExpanderFriendlyName24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName24.setStatus("current")
_IoExpanderFriendlyName25_Type = DisplayString
_IoExpanderFriendlyName25_Object = MibTableColumn
ioExpanderFriendlyName25 = _IoExpanderFriendlyName25_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 29),
    _IoExpanderFriendlyName25_Type()
)
ioExpanderFriendlyName25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName25.setStatus("current")
_IoExpanderFriendlyName26_Type = DisplayString
_IoExpanderFriendlyName26_Object = MibTableColumn
ioExpanderFriendlyName26 = _IoExpanderFriendlyName26_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 30),
    _IoExpanderFriendlyName26_Type()
)
ioExpanderFriendlyName26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName26.setStatus("current")
_IoExpanderFriendlyName27_Type = DisplayString
_IoExpanderFriendlyName27_Object = MibTableColumn
ioExpanderFriendlyName27 = _IoExpanderFriendlyName27_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 31),
    _IoExpanderFriendlyName27_Type()
)
ioExpanderFriendlyName27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName27.setStatus("current")
_IoExpanderFriendlyName28_Type = DisplayString
_IoExpanderFriendlyName28_Object = MibTableColumn
ioExpanderFriendlyName28 = _IoExpanderFriendlyName28_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 32),
    _IoExpanderFriendlyName28_Type()
)
ioExpanderFriendlyName28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName28.setStatus("current")
_IoExpanderFriendlyName29_Type = DisplayString
_IoExpanderFriendlyName29_Object = MibTableColumn
ioExpanderFriendlyName29 = _IoExpanderFriendlyName29_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 33),
    _IoExpanderFriendlyName29_Type()
)
ioExpanderFriendlyName29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName29.setStatus("current")
_IoExpanderFriendlyName30_Type = DisplayString
_IoExpanderFriendlyName30_Object = MibTableColumn
ioExpanderFriendlyName30 = _IoExpanderFriendlyName30_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 34),
    _IoExpanderFriendlyName30_Type()
)
ioExpanderFriendlyName30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName30.setStatus("current")
_IoExpanderFriendlyName31_Type = DisplayString
_IoExpanderFriendlyName31_Object = MibTableColumn
ioExpanderFriendlyName31 = _IoExpanderFriendlyName31_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 35),
    _IoExpanderFriendlyName31_Type()
)
ioExpanderFriendlyName31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName31.setStatus("current")
_IoExpanderFriendlyName32_Type = DisplayString
_IoExpanderFriendlyName32_Object = MibTableColumn
ioExpanderFriendlyName32 = _IoExpanderFriendlyName32_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 36),
    _IoExpanderFriendlyName32_Type()
)
ioExpanderFriendlyName32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderFriendlyName32.setStatus("current")


class _IoExpanderIO1_Type(Integer32):
    """Custom type ioExpanderIO1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO1_Type.__name__ = "Integer32"
_IoExpanderIO1_Object = MibTableColumn
ioExpanderIO1 = _IoExpanderIO1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 37),
    _IoExpanderIO1_Type()
)
ioExpanderIO1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO1.setStatus("current")


class _IoExpanderIO2_Type(Integer32):
    """Custom type ioExpanderIO2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO2_Type.__name__ = "Integer32"
_IoExpanderIO2_Object = MibTableColumn
ioExpanderIO2 = _IoExpanderIO2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 38),
    _IoExpanderIO2_Type()
)
ioExpanderIO2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO2.setStatus("current")


class _IoExpanderIO3_Type(Integer32):
    """Custom type ioExpanderIO3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO3_Type.__name__ = "Integer32"
_IoExpanderIO3_Object = MibTableColumn
ioExpanderIO3 = _IoExpanderIO3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 39),
    _IoExpanderIO3_Type()
)
ioExpanderIO3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO3.setStatus("current")


class _IoExpanderIO4_Type(Integer32):
    """Custom type ioExpanderIO4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO4_Type.__name__ = "Integer32"
_IoExpanderIO4_Object = MibTableColumn
ioExpanderIO4 = _IoExpanderIO4_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 40),
    _IoExpanderIO4_Type()
)
ioExpanderIO4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO4.setStatus("current")


class _IoExpanderIO5_Type(Integer32):
    """Custom type ioExpanderIO5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO5_Type.__name__ = "Integer32"
_IoExpanderIO5_Object = MibTableColumn
ioExpanderIO5 = _IoExpanderIO5_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 41),
    _IoExpanderIO5_Type()
)
ioExpanderIO5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO5.setStatus("current")


class _IoExpanderIO6_Type(Integer32):
    """Custom type ioExpanderIO6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO6_Type.__name__ = "Integer32"
_IoExpanderIO6_Object = MibTableColumn
ioExpanderIO6 = _IoExpanderIO6_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 42),
    _IoExpanderIO6_Type()
)
ioExpanderIO6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO6.setStatus("current")


class _IoExpanderIO7_Type(Integer32):
    """Custom type ioExpanderIO7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO7_Type.__name__ = "Integer32"
_IoExpanderIO7_Object = MibTableColumn
ioExpanderIO7 = _IoExpanderIO7_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 43),
    _IoExpanderIO7_Type()
)
ioExpanderIO7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO7.setStatus("current")


class _IoExpanderIO8_Type(Integer32):
    """Custom type ioExpanderIO8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO8_Type.__name__ = "Integer32"
_IoExpanderIO8_Object = MibTableColumn
ioExpanderIO8 = _IoExpanderIO8_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 44),
    _IoExpanderIO8_Type()
)
ioExpanderIO8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO8.setStatus("current")


class _IoExpanderIO9_Type(Integer32):
    """Custom type ioExpanderIO9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO9_Type.__name__ = "Integer32"
_IoExpanderIO9_Object = MibTableColumn
ioExpanderIO9 = _IoExpanderIO9_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 45),
    _IoExpanderIO9_Type()
)
ioExpanderIO9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO9.setStatus("current")


class _IoExpanderIO10_Type(Integer32):
    """Custom type ioExpanderIO10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO10_Type.__name__ = "Integer32"
_IoExpanderIO10_Object = MibTableColumn
ioExpanderIO10 = _IoExpanderIO10_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 46),
    _IoExpanderIO10_Type()
)
ioExpanderIO10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO10.setStatus("current")


class _IoExpanderIO11_Type(Integer32):
    """Custom type ioExpanderIO11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO11_Type.__name__ = "Integer32"
_IoExpanderIO11_Object = MibTableColumn
ioExpanderIO11 = _IoExpanderIO11_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 47),
    _IoExpanderIO11_Type()
)
ioExpanderIO11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO11.setStatus("current")


class _IoExpanderIO12_Type(Integer32):
    """Custom type ioExpanderIO12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO12_Type.__name__ = "Integer32"
_IoExpanderIO12_Object = MibTableColumn
ioExpanderIO12 = _IoExpanderIO12_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 48),
    _IoExpanderIO12_Type()
)
ioExpanderIO12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO12.setStatus("current")


class _IoExpanderIO13_Type(Integer32):
    """Custom type ioExpanderIO13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO13_Type.__name__ = "Integer32"
_IoExpanderIO13_Object = MibTableColumn
ioExpanderIO13 = _IoExpanderIO13_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 49),
    _IoExpanderIO13_Type()
)
ioExpanderIO13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO13.setStatus("current")


class _IoExpanderIO14_Type(Integer32):
    """Custom type ioExpanderIO14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO14_Type.__name__ = "Integer32"
_IoExpanderIO14_Object = MibTableColumn
ioExpanderIO14 = _IoExpanderIO14_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 50),
    _IoExpanderIO14_Type()
)
ioExpanderIO14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO14.setStatus("current")


class _IoExpanderIO15_Type(Integer32):
    """Custom type ioExpanderIO15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO15_Type.__name__ = "Integer32"
_IoExpanderIO15_Object = MibTableColumn
ioExpanderIO15 = _IoExpanderIO15_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 51),
    _IoExpanderIO15_Type()
)
ioExpanderIO15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO15.setStatus("current")


class _IoExpanderIO16_Type(Integer32):
    """Custom type ioExpanderIO16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO16_Type.__name__ = "Integer32"
_IoExpanderIO16_Object = MibTableColumn
ioExpanderIO16 = _IoExpanderIO16_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 52),
    _IoExpanderIO16_Type()
)
ioExpanderIO16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO16.setStatus("current")


class _IoExpanderIO17_Type(Integer32):
    """Custom type ioExpanderIO17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO17_Type.__name__ = "Integer32"
_IoExpanderIO17_Object = MibTableColumn
ioExpanderIO17 = _IoExpanderIO17_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 53),
    _IoExpanderIO17_Type()
)
ioExpanderIO17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO17.setStatus("current")


class _IoExpanderIO18_Type(Integer32):
    """Custom type ioExpanderIO18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO18_Type.__name__ = "Integer32"
_IoExpanderIO18_Object = MibTableColumn
ioExpanderIO18 = _IoExpanderIO18_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 54),
    _IoExpanderIO18_Type()
)
ioExpanderIO18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO18.setStatus("current")


class _IoExpanderIO19_Type(Integer32):
    """Custom type ioExpanderIO19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO19_Type.__name__ = "Integer32"
_IoExpanderIO19_Object = MibTableColumn
ioExpanderIO19 = _IoExpanderIO19_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 55),
    _IoExpanderIO19_Type()
)
ioExpanderIO19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO19.setStatus("current")


class _IoExpanderIO20_Type(Integer32):
    """Custom type ioExpanderIO20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO20_Type.__name__ = "Integer32"
_IoExpanderIO20_Object = MibTableColumn
ioExpanderIO20 = _IoExpanderIO20_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 56),
    _IoExpanderIO20_Type()
)
ioExpanderIO20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO20.setStatus("current")


class _IoExpanderIO21_Type(Integer32):
    """Custom type ioExpanderIO21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO21_Type.__name__ = "Integer32"
_IoExpanderIO21_Object = MibTableColumn
ioExpanderIO21 = _IoExpanderIO21_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 57),
    _IoExpanderIO21_Type()
)
ioExpanderIO21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO21.setStatus("current")


class _IoExpanderIO22_Type(Integer32):
    """Custom type ioExpanderIO22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO22_Type.__name__ = "Integer32"
_IoExpanderIO22_Object = MibTableColumn
ioExpanderIO22 = _IoExpanderIO22_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 58),
    _IoExpanderIO22_Type()
)
ioExpanderIO22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO22.setStatus("current")


class _IoExpanderIO23_Type(Integer32):
    """Custom type ioExpanderIO23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO23_Type.__name__ = "Integer32"
_IoExpanderIO23_Object = MibTableColumn
ioExpanderIO23 = _IoExpanderIO23_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 59),
    _IoExpanderIO23_Type()
)
ioExpanderIO23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO23.setStatus("current")


class _IoExpanderIO24_Type(Integer32):
    """Custom type ioExpanderIO24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO24_Type.__name__ = "Integer32"
_IoExpanderIO24_Object = MibTableColumn
ioExpanderIO24 = _IoExpanderIO24_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 60),
    _IoExpanderIO24_Type()
)
ioExpanderIO24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO24.setStatus("current")


class _IoExpanderIO25_Type(Integer32):
    """Custom type ioExpanderIO25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO25_Type.__name__ = "Integer32"
_IoExpanderIO25_Object = MibTableColumn
ioExpanderIO25 = _IoExpanderIO25_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 61),
    _IoExpanderIO25_Type()
)
ioExpanderIO25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO25.setStatus("current")


class _IoExpanderIO26_Type(Integer32):
    """Custom type ioExpanderIO26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO26_Type.__name__ = "Integer32"
_IoExpanderIO26_Object = MibTableColumn
ioExpanderIO26 = _IoExpanderIO26_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 62),
    _IoExpanderIO26_Type()
)
ioExpanderIO26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO26.setStatus("current")


class _IoExpanderIO27_Type(Integer32):
    """Custom type ioExpanderIO27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO27_Type.__name__ = "Integer32"
_IoExpanderIO27_Object = MibTableColumn
ioExpanderIO27 = _IoExpanderIO27_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 63),
    _IoExpanderIO27_Type()
)
ioExpanderIO27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO27.setStatus("current")


class _IoExpanderIO28_Type(Integer32):
    """Custom type ioExpanderIO28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO28_Type.__name__ = "Integer32"
_IoExpanderIO28_Object = MibTableColumn
ioExpanderIO28 = _IoExpanderIO28_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 64),
    _IoExpanderIO28_Type()
)
ioExpanderIO28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO28.setStatus("current")


class _IoExpanderIO29_Type(Integer32):
    """Custom type ioExpanderIO29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO29_Type.__name__ = "Integer32"
_IoExpanderIO29_Object = MibTableColumn
ioExpanderIO29 = _IoExpanderIO29_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 65),
    _IoExpanderIO29_Type()
)
ioExpanderIO29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO29.setStatus("current")


class _IoExpanderIO30_Type(Integer32):
    """Custom type ioExpanderIO30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO30_Type.__name__ = "Integer32"
_IoExpanderIO30_Object = MibTableColumn
ioExpanderIO30 = _IoExpanderIO30_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 66),
    _IoExpanderIO30_Type()
)
ioExpanderIO30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO30.setStatus("current")


class _IoExpanderIO31_Type(Integer32):
    """Custom type ioExpanderIO31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO31_Type.__name__ = "Integer32"
_IoExpanderIO31_Object = MibTableColumn
ioExpanderIO31 = _IoExpanderIO31_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 67),
    _IoExpanderIO31_Type()
)
ioExpanderIO31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO31.setStatus("current")


class _IoExpanderIO32_Type(Integer32):
    """Custom type ioExpanderIO32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IoExpanderIO32_Type.__name__ = "Integer32"
_IoExpanderIO32_Object = MibTableColumn
ioExpanderIO32 = _IoExpanderIO32_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 68),
    _IoExpanderIO32_Type()
)
ioExpanderIO32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderIO32.setStatus("current")
_IoExpanderRelayName1_Type = DisplayString
_IoExpanderRelayName1_Object = MibTableColumn
ioExpanderRelayName1 = _IoExpanderRelayName1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 69),
    _IoExpanderRelayName1_Type()
)
ioExpanderRelayName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioExpanderRelayName1.setStatus("current")
_IoExpanderRelayState1_Type = Gauge32
_IoExpanderRelayState1_Object = MibTableColumn
ioExpanderRelayState1 = _IoExpanderRelayState1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 70),
    _IoExpanderRelayState1_Type()
)
ioExpanderRelayState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderRelayState1.setStatus("current")
_IoExpanderRelayLatchingMode1_Type = Gauge32
_IoExpanderRelayLatchingMode1_Object = MibTableColumn
ioExpanderRelayLatchingMode1 = _IoExpanderRelayLatchingMode1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 71),
    _IoExpanderRelayLatchingMode1_Type()
)
ioExpanderRelayLatchingMode1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioExpanderRelayLatchingMode1.setStatus("current")
_IoExpanderRelayOverride1_Type = Gauge32
_IoExpanderRelayOverride1_Object = MibTableColumn
ioExpanderRelayOverride1 = _IoExpanderRelayOverride1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 72),
    _IoExpanderRelayOverride1_Type()
)
ioExpanderRelayOverride1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioExpanderRelayOverride1.setStatus("current")
_IoExpanderRelayAcknowledge1_Type = Gauge32
_IoExpanderRelayAcknowledge1_Object = MibTableColumn
ioExpanderRelayAcknowledge1 = _IoExpanderRelayAcknowledge1_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 73),
    _IoExpanderRelayAcknowledge1_Type()
)
ioExpanderRelayAcknowledge1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioExpanderRelayAcknowledge1.setStatus("current")
_IoExpanderRelayName2_Type = DisplayString
_IoExpanderRelayName2_Object = MibTableColumn
ioExpanderRelayName2 = _IoExpanderRelayName2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 74),
    _IoExpanderRelayName2_Type()
)
ioExpanderRelayName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioExpanderRelayName2.setStatus("current")
_IoExpanderRelayState2_Type = Gauge32
_IoExpanderRelayState2_Object = MibTableColumn
ioExpanderRelayState2 = _IoExpanderRelayState2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 75),
    _IoExpanderRelayState2_Type()
)
ioExpanderRelayState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderRelayState2.setStatus("current")
_IoExpanderRelayLatchingMode2_Type = Gauge32
_IoExpanderRelayLatchingMode2_Object = MibTableColumn
ioExpanderRelayLatchingMode2 = _IoExpanderRelayLatchingMode2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 76),
    _IoExpanderRelayLatchingMode2_Type()
)
ioExpanderRelayLatchingMode2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioExpanderRelayLatchingMode2.setStatus("current")
_IoExpanderRelayOverride2_Type = Gauge32
_IoExpanderRelayOverride2_Object = MibTableColumn
ioExpanderRelayOverride2 = _IoExpanderRelayOverride2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 77),
    _IoExpanderRelayOverride2_Type()
)
ioExpanderRelayOverride2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioExpanderRelayOverride2.setStatus("current")
_IoExpanderRelayAcknowledge2_Type = Gauge32
_IoExpanderRelayAcknowledge2_Object = MibTableColumn
ioExpanderRelayAcknowledge2 = _IoExpanderRelayAcknowledge2_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 78),
    _IoExpanderRelayAcknowledge2_Type()
)
ioExpanderRelayAcknowledge2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioExpanderRelayAcknowledge2.setStatus("current")
_IoExpanderRelayName3_Type = DisplayString
_IoExpanderRelayName3_Object = MibTableColumn
ioExpanderRelayName3 = _IoExpanderRelayName3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 79),
    _IoExpanderRelayName3_Type()
)
ioExpanderRelayName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioExpanderRelayName3.setStatus("current")
_IoExpanderRelayState3_Type = Gauge32
_IoExpanderRelayState3_Object = MibTableColumn
ioExpanderRelayState3 = _IoExpanderRelayState3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 80),
    _IoExpanderRelayState3_Type()
)
ioExpanderRelayState3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioExpanderRelayState3.setStatus("current")
_IoExpanderRelayLatchingMode3_Type = Gauge32
_IoExpanderRelayLatchingMode3_Object = MibTableColumn
ioExpanderRelayLatchingMode3 = _IoExpanderRelayLatchingMode3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 81),
    _IoExpanderRelayLatchingMode3_Type()
)
ioExpanderRelayLatchingMode3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioExpanderRelayLatchingMode3.setStatus("current")
_IoExpanderRelayOverride3_Type = Gauge32
_IoExpanderRelayOverride3_Object = MibTableColumn
ioExpanderRelayOverride3 = _IoExpanderRelayOverride3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 82),
    _IoExpanderRelayOverride3_Type()
)
ioExpanderRelayOverride3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioExpanderRelayOverride3.setStatus("current")
_IoExpanderRelayAcknowledge3_Type = Gauge32
_IoExpanderRelayAcknowledge3_Object = MibTableColumn
ioExpanderRelayAcknowledge3 = _IoExpanderRelayAcknowledge3_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 30, 1, 83),
    _IoExpanderRelayAcknowledge3_Type()
)
ioExpanderRelayAcknowledge3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioExpanderRelayAcknowledge3.setStatus("current")
_T3hdSensorTable_Object = MibTable
t3hdSensorTable = _T3hdSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31)
)
if mibBuilder.loadTexts:
    t3hdSensorTable.setStatus("current")
_T3hdSensorEntry_Object = MibTableRow
t3hdSensorEntry = _T3hdSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1)
)
t3hdSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "t3hdSensorIndex"),
)
if mibBuilder.loadTexts:
    t3hdSensorEntry.setStatus("current")


class _T3hdSensorIndex_Type(Integer32):
    """Custom type t3hdSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_T3hdSensorIndex_Type.__name__ = "Integer32"
_T3hdSensorIndex_Object = MibTableColumn
t3hdSensorIndex = _T3hdSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 1),
    _T3hdSensorIndex_Type()
)
t3hdSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t3hdSensorIndex.setStatus("current")
_T3hdSensorSerial_Type = DisplayString
_T3hdSensorSerial_Object = MibTableColumn
t3hdSensorSerial = _T3hdSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 2),
    _T3hdSensorSerial_Type()
)
t3hdSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorSerial.setStatus("current")
_T3hdSensorName_Type = DisplayString
_T3hdSensorName_Object = MibTableColumn
t3hdSensorName = _T3hdSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 3),
    _T3hdSensorName_Type()
)
t3hdSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorName.setStatus("current")
_T3hdSensorAvail_Type = Gauge32
_T3hdSensorAvail_Object = MibTableColumn
t3hdSensorAvail = _T3hdSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 4),
    _T3hdSensorAvail_Type()
)
t3hdSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorAvail.setStatus("current")
_T3hdSensorIntName_Type = DisplayString
_T3hdSensorIntName_Object = MibTableColumn
t3hdSensorIntName = _T3hdSensorIntName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 5),
    _T3hdSensorIntName_Type()
)
t3hdSensorIntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntName.setStatus("current")


class _T3hdSensorIntTempC_Type(Integer32):
    """Custom type t3hdSensorIntTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_T3hdSensorIntTempC_Type.__name__ = "Integer32"
_T3hdSensorIntTempC_Object = MibTableColumn
t3hdSensorIntTempC = _T3hdSensorIntTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 6),
    _T3hdSensorIntTempC_Type()
)
t3hdSensorIntTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntTempC.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntTempC.setUnits("Degrees Celsius")


class _T3hdSensorIntTempF_Type(Integer32):
    """Custom type t3hdSensorIntTempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_T3hdSensorIntTempF_Type.__name__ = "Integer32"
_T3hdSensorIntTempF_Object = MibTableColumn
t3hdSensorIntTempF = _T3hdSensorIntTempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 7),
    _T3hdSensorIntTempF_Type()
)
t3hdSensorIntTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntTempF.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntTempF.setUnits("Degrees Fahrenheit")


class _T3hdSensorIntHumidity_Type(Integer32):
    """Custom type t3hdSensorIntHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_T3hdSensorIntHumidity_Type.__name__ = "Integer32"
_T3hdSensorIntHumidity_Object = MibTableColumn
t3hdSensorIntHumidity = _T3hdSensorIntHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 8),
    _T3hdSensorIntHumidity_Type()
)
t3hdSensorIntHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntHumidity.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntHumidity.setUnits("%")


class _T3hdSensorIntDewPointC_Type(Integer32):
    """Custom type t3hdSensorIntDewPointC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_T3hdSensorIntDewPointC_Type.__name__ = "Integer32"
_T3hdSensorIntDewPointC_Object = MibTableColumn
t3hdSensorIntDewPointC = _T3hdSensorIntDewPointC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 9),
    _T3hdSensorIntDewPointC_Type()
)
t3hdSensorIntDewPointC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntDewPointC.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntDewPointC.setUnits("Degrees Celsius")


class _T3hdSensorIntDewPointF_Type(Integer32):
    """Custom type t3hdSensorIntDewPointF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_T3hdSensorIntDewPointF_Type.__name__ = "Integer32"
_T3hdSensorIntDewPointF_Object = MibTableColumn
t3hdSensorIntDewPointF = _T3hdSensorIntDewPointF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 10),
    _T3hdSensorIntDewPointF_Type()
)
t3hdSensorIntDewPointF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorIntDewPointF.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorIntDewPointF.setUnits("Degress Fahrenheit")
_T3hdSensorExt1Avail_Type = Gauge32
_T3hdSensorExt1Avail_Object = MibTableColumn
t3hdSensorExt1Avail = _T3hdSensorExt1Avail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 11),
    _T3hdSensorExt1Avail_Type()
)
t3hdSensorExt1Avail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExt1Avail.setStatus("current")
_T3hdSensorExt1Name_Type = DisplayString
_T3hdSensorExt1Name_Object = MibTableColumn
t3hdSensorExt1Name = _T3hdSensorExt1Name_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 12),
    _T3hdSensorExt1Name_Type()
)
t3hdSensorExt1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExt1Name.setStatus("current")


class _T3hdSensorExt1TempC_Type(Integer32):
    """Custom type t3hdSensorExt1TempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_T3hdSensorExt1TempC_Type.__name__ = "Integer32"
_T3hdSensorExt1TempC_Object = MibTableColumn
t3hdSensorExt1TempC = _T3hdSensorExt1TempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 13),
    _T3hdSensorExt1TempC_Type()
)
t3hdSensorExt1TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExt1TempC.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorExt1TempC.setUnits("Degrees Celsius")


class _T3hdSensorExt1TempF_Type(Integer32):
    """Custom type t3hdSensorExt1TempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_T3hdSensorExt1TempF_Type.__name__ = "Integer32"
_T3hdSensorExt1TempF_Object = MibTableColumn
t3hdSensorExt1TempF = _T3hdSensorExt1TempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 14),
    _T3hdSensorExt1TempF_Type()
)
t3hdSensorExt1TempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExt1TempF.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorExt1TempF.setUnits("Degress Fahrenheit")
_T3hdSensorExt2Avail_Type = Gauge32
_T3hdSensorExt2Avail_Object = MibTableColumn
t3hdSensorExt2Avail = _T3hdSensorExt2Avail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 15),
    _T3hdSensorExt2Avail_Type()
)
t3hdSensorExt2Avail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExt2Avail.setStatus("current")
_T3hdSensorExt2Name_Type = DisplayString
_T3hdSensorExt2Name_Object = MibTableColumn
t3hdSensorExt2Name = _T3hdSensorExt2Name_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 16),
    _T3hdSensorExt2Name_Type()
)
t3hdSensorExt2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExt2Name.setStatus("current")


class _T3hdSensorExt2TempC_Type(Integer32):
    """Custom type t3hdSensorExt2TempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_T3hdSensorExt2TempC_Type.__name__ = "Integer32"
_T3hdSensorExt2TempC_Object = MibTableColumn
t3hdSensorExt2TempC = _T3hdSensorExt2TempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 17),
    _T3hdSensorExt2TempC_Type()
)
t3hdSensorExt2TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExt2TempC.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorExt2TempC.setUnits("Degrees Celsius")


class _T3hdSensorExt2TempF_Type(Integer32):
    """Custom type t3hdSensorExt2TempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_T3hdSensorExt2TempF_Type.__name__ = "Integer32"
_T3hdSensorExt2TempF_Object = MibTableColumn
t3hdSensorExt2TempF = _T3hdSensorExt2TempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 31, 1, 18),
    _T3hdSensorExt2TempF_Type()
)
t3hdSensorExt2TempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSensorExt2TempF.setStatus("current")
if mibBuilder.loadTexts:
    t3hdSensorExt2TempF.setUnits("Degress Fahrenheit")
_ThdSensorTable_Object = MibTable
thdSensorTable = _ThdSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32)
)
if mibBuilder.loadTexts:
    thdSensorTable.setStatus("current")
_ThdSensorEntry_Object = MibTableRow
thdSensorEntry = _ThdSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32, 1)
)
thdSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "thdSensorIndex"),
)
if mibBuilder.loadTexts:
    thdSensorEntry.setStatus("current")


class _ThdSensorIndex_Type(Integer32):
    """Custom type thdSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ThdSensorIndex_Type.__name__ = "Integer32"
_ThdSensorIndex_Object = MibTableColumn
thdSensorIndex = _ThdSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32, 1, 1),
    _ThdSensorIndex_Type()
)
thdSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thdSensorIndex.setStatus("current")
_ThdSensorSerial_Type = DisplayString
_ThdSensorSerial_Object = MibTableColumn
thdSensorSerial = _ThdSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32, 1, 2),
    _ThdSensorSerial_Type()
)
thdSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorSerial.setStatus("current")
_ThdSensorName_Type = DisplayString
_ThdSensorName_Object = MibTableColumn
thdSensorName = _ThdSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32, 1, 3),
    _ThdSensorName_Type()
)
thdSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorName.setStatus("current")
_ThdSensorAvail_Type = Gauge32
_ThdSensorAvail_Object = MibTableColumn
thdSensorAvail = _ThdSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32, 1, 4),
    _ThdSensorAvail_Type()
)
thdSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorAvail.setStatus("current")


class _ThdSensorTempC_Type(Integer32):
    """Custom type thdSensorTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_ThdSensorTempC_Type.__name__ = "Integer32"
_ThdSensorTempC_Object = MibTableColumn
thdSensorTempC = _ThdSensorTempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32, 1, 5),
    _ThdSensorTempC_Type()
)
thdSensorTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorTempC.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorTempC.setUnits("Degrees Celsius")


class _ThdSensorTempF_Type(Integer32):
    """Custom type thdSensorTempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_ThdSensorTempF_Type.__name__ = "Integer32"
_ThdSensorTempF_Object = MibTableColumn
thdSensorTempF = _ThdSensorTempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32, 1, 6),
    _ThdSensorTempF_Type()
)
thdSensorTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorTempF.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorTempF.setUnits("Degrees Fahrenheit")


class _ThdSensorHumidity_Type(Integer32):
    """Custom type thdSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ThdSensorHumidity_Type.__name__ = "Integer32"
_ThdSensorHumidity_Object = MibTableColumn
thdSensorHumidity = _ThdSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32, 1, 7),
    _ThdSensorHumidity_Type()
)
thdSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorHumidity.setUnits("%")


class _ThdSensorDewPointC_Type(Integer32):
    """Custom type thdSensorDewPointC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_ThdSensorDewPointC_Type.__name__ = "Integer32"
_ThdSensorDewPointC_Object = MibTableColumn
thdSensorDewPointC = _ThdSensorDewPointC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32, 1, 8),
    _ThdSensorDewPointC_Type()
)
thdSensorDewPointC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorDewPointC.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorDewPointC.setUnits("Degrees Celsius")


class _ThdSensorDewPointF_Type(Integer32):
    """Custom type thdSensorDewPointF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_ThdSensorDewPointF_Type.__name__ = "Integer32"
_ThdSensorDewPointF_Object = MibTableColumn
thdSensorDewPointF = _ThdSensorDewPointF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32, 1, 9),
    _ThdSensorDewPointF_Type()
)
thdSensorDewPointF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSensorDewPointF.setStatus("current")
if mibBuilder.loadTexts:
    thdSensorDewPointF.setUnits("Degress Fahrenheit")
_Pos60VdcSensorTable_Object = MibTable
pos60VdcSensorTable = _Pos60VdcSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 33)
)
if mibBuilder.loadTexts:
    pos60VdcSensorTable.setStatus("current")
_Pos60VdcSensorEntry_Object = MibTableRow
pos60VdcSensorEntry = _Pos60VdcSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 33, 1)
)
pos60VdcSensorEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "pos60VdcSensorIndex"),
)
if mibBuilder.loadTexts:
    pos60VdcSensorEntry.setStatus("current")


class _Pos60VdcSensorIndex_Type(Integer32):
    """Custom type pos60VdcSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Pos60VdcSensorIndex_Type.__name__ = "Integer32"
_Pos60VdcSensorIndex_Object = MibTableColumn
pos60VdcSensorIndex = _Pos60VdcSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 33, 1, 1),
    _Pos60VdcSensorIndex_Type()
)
pos60VdcSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pos60VdcSensorIndex.setStatus("current")
_Pos60VdcSensorSerial_Type = DisplayString
_Pos60VdcSensorSerial_Object = MibTableColumn
pos60VdcSensorSerial = _Pos60VdcSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 33, 1, 2),
    _Pos60VdcSensorSerial_Type()
)
pos60VdcSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos60VdcSensorSerial.setStatus("current")
_Pos60VdcSensorName_Type = DisplayString
_Pos60VdcSensorName_Object = MibTableColumn
pos60VdcSensorName = _Pos60VdcSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 33, 1, 3),
    _Pos60VdcSensorName_Type()
)
pos60VdcSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos60VdcSensorName.setStatus("current")
_Pos60VdcSensorAvail_Type = Gauge32
_Pos60VdcSensorAvail_Object = MibTableColumn
pos60VdcSensorAvail = _Pos60VdcSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 33, 1, 4),
    _Pos60VdcSensorAvail_Type()
)
pos60VdcSensorAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos60VdcSensorAvail.setStatus("current")


class _Pos60VdcSensorVoltage_Type(Integer32):
    """Custom type pos60VdcSensorVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 100),
    )


_Pos60VdcSensorVoltage_Type.__name__ = "Integer32"
_Pos60VdcSensorVoltage_Object = MibTableColumn
pos60VdcSensorVoltage = _Pos60VdcSensorVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 33, 1, 5),
    _Pos60VdcSensorVoltage_Type()
)
pos60VdcSensorVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pos60VdcSensorVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pos60VdcSensorVoltage.setUnits("Volts")
_Ctrl2CirTotTable_Object = MibTable
ctrl2CirTotTable = _Ctrl2CirTotTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34)
)
if mibBuilder.loadTexts:
    ctrl2CirTotTable.setStatus("current")
_Ctrl2CirTotEntry_Object = MibTableRow
ctrl2CirTotEntry = _Ctrl2CirTotEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1)
)
ctrl2CirTotEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "ctrl2CirTotIndex"),
)
if mibBuilder.loadTexts:
    ctrl2CirTotEntry.setStatus("current")


class _Ctrl2CirTotIndex_Type(Integer32):
    """Custom type ctrl2CirTotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Ctrl2CirTotIndex_Type.__name__ = "Integer32"
_Ctrl2CirTotIndex_Object = MibTableColumn
ctrl2CirTotIndex = _Ctrl2CirTotIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 1),
    _Ctrl2CirTotIndex_Type()
)
ctrl2CirTotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctrl2CirTotIndex.setStatus("current")
_Ctrl2CirTotSerial_Type = DisplayString
_Ctrl2CirTotSerial_Object = MibTableColumn
ctrl2CirTotSerial = _Ctrl2CirTotSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 2),
    _Ctrl2CirTotSerial_Type()
)
ctrl2CirTotSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotSerial.setStatus("current")
_Ctrl2CirTotName_Type = DisplayString
_Ctrl2CirTotName_Object = MibTableColumn
ctrl2CirTotName = _Ctrl2CirTotName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 3),
    _Ctrl2CirTotName_Type()
)
ctrl2CirTotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotName.setStatus("current")
_Ctrl2CirTotAvail_Type = Gauge32
_Ctrl2CirTotAvail_Object = MibTableColumn
ctrl2CirTotAvail = _Ctrl2CirTotAvail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 4),
    _Ctrl2CirTotAvail_Type()
)
ctrl2CirTotAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotAvail.setStatus("current")
_Ctrl2CirTotkWattHrsTot_Type = Gauge32
_Ctrl2CirTotkWattHrsTot_Object = MibTableColumn
ctrl2CirTotkWattHrsTot = _Ctrl2CirTotkWattHrsTot_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 5),
    _Ctrl2CirTotkWattHrsTot_Type()
)
ctrl2CirTotkWattHrsTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotkWattHrsTot.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotkWattHrsTot.setUnits("kWh")
_Ctrl2CirTotVoltsTot_Type = Gauge32
_Ctrl2CirTotVoltsTot_Object = MibTableColumn
ctrl2CirTotVoltsTot = _Ctrl2CirTotVoltsTot_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 6),
    _Ctrl2CirTotVoltsTot_Type()
)
ctrl2CirTotVoltsTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotVoltsTot.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotVoltsTot.setUnits("Volts (rms)")
_Ctrl2CirTotVoltPeakTot_Type = Gauge32
_Ctrl2CirTotVoltPeakTot_Object = MibTableColumn
ctrl2CirTotVoltPeakTot = _Ctrl2CirTotVoltPeakTot_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 7),
    _Ctrl2CirTotVoltPeakTot_Type()
)
ctrl2CirTotVoltPeakTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotVoltPeakTot.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotVoltPeakTot.setUnits("Volts (rms)")
_Ctrl2CirTotDeciAmpsTot_Type = Gauge32
_Ctrl2CirTotDeciAmpsTot_Object = MibTableColumn
ctrl2CirTotDeciAmpsTot = _Ctrl2CirTotDeciAmpsTot_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 8),
    _Ctrl2CirTotDeciAmpsTot_Type()
)
ctrl2CirTotDeciAmpsTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotDeciAmpsTot.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotDeciAmpsTot.setUnits("0.1 Amps (rms)")
_Ctrl2CirTotDeciAmpsPeakTot_Type = Gauge32
_Ctrl2CirTotDeciAmpsPeakTot_Object = MibTableColumn
ctrl2CirTotDeciAmpsPeakTot = _Ctrl2CirTotDeciAmpsPeakTot_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 9),
    _Ctrl2CirTotDeciAmpsPeakTot_Type()
)
ctrl2CirTotDeciAmpsPeakTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotDeciAmpsPeakTot.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotDeciAmpsPeakTot.setUnits("0.1 Amps (rms)")
_Ctrl2CirTotRealPowerTot_Type = Gauge32
_Ctrl2CirTotRealPowerTot_Object = MibTableColumn
ctrl2CirTotRealPowerTot = _Ctrl2CirTotRealPowerTot_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 10),
    _Ctrl2CirTotRealPowerTot_Type()
)
ctrl2CirTotRealPowerTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotRealPowerTot.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotRealPowerTot.setUnits("Watts")
_Ctrl2CirTotApparentPowerTot_Type = Gauge32
_Ctrl2CirTotApparentPowerTot_Object = MibTableColumn
ctrl2CirTotApparentPowerTot = _Ctrl2CirTotApparentPowerTot_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 11),
    _Ctrl2CirTotApparentPowerTot_Type()
)
ctrl2CirTotApparentPowerTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotApparentPowerTot.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotApparentPowerTot.setUnits("Volt-Amps")


class _Ctrl2CirTotPowerFactorTot_Type(Integer32):
    """Custom type ctrl2CirTotPowerFactorTot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ctrl2CirTotPowerFactorTot_Type.__name__ = "Integer32"
_Ctrl2CirTotPowerFactorTot_Object = MibTableColumn
ctrl2CirTotPowerFactorTot = _Ctrl2CirTotPowerFactorTot_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 12),
    _Ctrl2CirTotPowerFactorTot_Type()
)
ctrl2CirTotPowerFactorTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotPowerFactorTot.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotPowerFactorTot.setUnits("%")
_Ctrl2CirTotkWattHrsA_Type = Gauge32
_Ctrl2CirTotkWattHrsA_Object = MibTableColumn
ctrl2CirTotkWattHrsA = _Ctrl2CirTotkWattHrsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 13),
    _Ctrl2CirTotkWattHrsA_Type()
)
ctrl2CirTotkWattHrsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotkWattHrsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotkWattHrsA.setUnits("kWh")
_Ctrl2CirTotVoltsA_Type = Gauge32
_Ctrl2CirTotVoltsA_Object = MibTableColumn
ctrl2CirTotVoltsA = _Ctrl2CirTotVoltsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 14),
    _Ctrl2CirTotVoltsA_Type()
)
ctrl2CirTotVoltsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotVoltsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotVoltsA.setUnits("Volts (rms)")
_Ctrl2CirTotVoltPeakA_Type = Gauge32
_Ctrl2CirTotVoltPeakA_Object = MibTableColumn
ctrl2CirTotVoltPeakA = _Ctrl2CirTotVoltPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 15),
    _Ctrl2CirTotVoltPeakA_Type()
)
ctrl2CirTotVoltPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotVoltPeakA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotVoltPeakA.setUnits("Volts (rms)")
_Ctrl2CirTotDeciAmpsA_Type = Gauge32
_Ctrl2CirTotDeciAmpsA_Object = MibTableColumn
ctrl2CirTotDeciAmpsA = _Ctrl2CirTotDeciAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 16),
    _Ctrl2CirTotDeciAmpsA_Type()
)
ctrl2CirTotDeciAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotDeciAmpsA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotDeciAmpsA.setUnits("0.1 Amps (rms)")
_Ctrl2CirTotDeciAmpsPeakA_Type = Gauge32
_Ctrl2CirTotDeciAmpsPeakA_Object = MibTableColumn
ctrl2CirTotDeciAmpsPeakA = _Ctrl2CirTotDeciAmpsPeakA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 17),
    _Ctrl2CirTotDeciAmpsPeakA_Type()
)
ctrl2CirTotDeciAmpsPeakA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotDeciAmpsPeakA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotDeciAmpsPeakA.setUnits("0.1 Amps (rms)")
_Ctrl2CirTotRealPowerA_Type = Gauge32
_Ctrl2CirTotRealPowerA_Object = MibTableColumn
ctrl2CirTotRealPowerA = _Ctrl2CirTotRealPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 18),
    _Ctrl2CirTotRealPowerA_Type()
)
ctrl2CirTotRealPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotRealPowerA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotRealPowerA.setUnits("Watts")
_Ctrl2CirTotApparentPowerA_Type = Gauge32
_Ctrl2CirTotApparentPowerA_Object = MibTableColumn
ctrl2CirTotApparentPowerA = _Ctrl2CirTotApparentPowerA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 19),
    _Ctrl2CirTotApparentPowerA_Type()
)
ctrl2CirTotApparentPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotApparentPowerA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotApparentPowerA.setUnits("Volt-Amps")


class _Ctrl2CirTotPowerFactorA_Type(Integer32):
    """Custom type ctrl2CirTotPowerFactorA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ctrl2CirTotPowerFactorA_Type.__name__ = "Integer32"
_Ctrl2CirTotPowerFactorA_Object = MibTableColumn
ctrl2CirTotPowerFactorA = _Ctrl2CirTotPowerFactorA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 20),
    _Ctrl2CirTotPowerFactorA_Type()
)
ctrl2CirTotPowerFactorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotPowerFactorA.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotPowerFactorA.setUnits("%")
_Ctrl2CirTotkWattHrsB_Type = Gauge32
_Ctrl2CirTotkWattHrsB_Object = MibTableColumn
ctrl2CirTotkWattHrsB = _Ctrl2CirTotkWattHrsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 21),
    _Ctrl2CirTotkWattHrsB_Type()
)
ctrl2CirTotkWattHrsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotkWattHrsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotkWattHrsB.setUnits("kWh")
_Ctrl2CirTotVoltsB_Type = Gauge32
_Ctrl2CirTotVoltsB_Object = MibTableColumn
ctrl2CirTotVoltsB = _Ctrl2CirTotVoltsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 22),
    _Ctrl2CirTotVoltsB_Type()
)
ctrl2CirTotVoltsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotVoltsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotVoltsB.setUnits("Volts (rms)")
_Ctrl2CirTotVoltPeakB_Type = Gauge32
_Ctrl2CirTotVoltPeakB_Object = MibTableColumn
ctrl2CirTotVoltPeakB = _Ctrl2CirTotVoltPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 23),
    _Ctrl2CirTotVoltPeakB_Type()
)
ctrl2CirTotVoltPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotVoltPeakB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotVoltPeakB.setUnits("Volts (rms)")
_Ctrl2CirTotDeciAmpsB_Type = Gauge32
_Ctrl2CirTotDeciAmpsB_Object = MibTableColumn
ctrl2CirTotDeciAmpsB = _Ctrl2CirTotDeciAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 24),
    _Ctrl2CirTotDeciAmpsB_Type()
)
ctrl2CirTotDeciAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotDeciAmpsB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotDeciAmpsB.setUnits("0.1 Amps (rms)")
_Ctrl2CirTotDeciAmpsPeakB_Type = Gauge32
_Ctrl2CirTotDeciAmpsPeakB_Object = MibTableColumn
ctrl2CirTotDeciAmpsPeakB = _Ctrl2CirTotDeciAmpsPeakB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 25),
    _Ctrl2CirTotDeciAmpsPeakB_Type()
)
ctrl2CirTotDeciAmpsPeakB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotDeciAmpsPeakB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotDeciAmpsPeakB.setUnits("0.1 Amps (rms)")
_Ctrl2CirTotRealPowerB_Type = Gauge32
_Ctrl2CirTotRealPowerB_Object = MibTableColumn
ctrl2CirTotRealPowerB = _Ctrl2CirTotRealPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 26),
    _Ctrl2CirTotRealPowerB_Type()
)
ctrl2CirTotRealPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotRealPowerB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotRealPowerB.setUnits("Watts")
_Ctrl2CirTotApparentPowerB_Type = Gauge32
_Ctrl2CirTotApparentPowerB_Object = MibTableColumn
ctrl2CirTotApparentPowerB = _Ctrl2CirTotApparentPowerB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 27),
    _Ctrl2CirTotApparentPowerB_Type()
)
ctrl2CirTotApparentPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotApparentPowerB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotApparentPowerB.setUnits("Volt-Amps")


class _Ctrl2CirTotPowerFactorB_Type(Integer32):
    """Custom type ctrl2CirTotPowerFactorB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ctrl2CirTotPowerFactorB_Type.__name__ = "Integer32"
_Ctrl2CirTotPowerFactorB_Object = MibTableColumn
ctrl2CirTotPowerFactorB = _Ctrl2CirTotPowerFactorB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 34, 1, 28),
    _Ctrl2CirTotPowerFactorB_Type()
)
ctrl2CirTotPowerFactorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrl2CirTotPowerFactorB.setStatus("current")
if mibBuilder.loadTexts:
    ctrl2CirTotPowerFactorB.setUnits("%")
_Sc10Table_Object = MibTable
sc10Table = _Sc10Table_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 35)
)
if mibBuilder.loadTexts:
    sc10Table.setStatus("current")
_Sc10Entry_Object = MibTableRow
sc10Entry = _Sc10Entry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 35, 1)
)
sc10Entry.setIndexNames(
    (0, "GEIST-MIB-V3", "sc10Index"),
)
if mibBuilder.loadTexts:
    sc10Entry.setStatus("current")


class _Sc10Index_Type(Integer32):
    """Custom type sc10Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Sc10Index_Type.__name__ = "Integer32"
_Sc10Index_Object = MibTableColumn
sc10Index = _Sc10Index_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 35, 1, 1),
    _Sc10Index_Type()
)
sc10Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sc10Index.setStatus("current")
_Sc10Serial_Type = DisplayString
_Sc10Serial_Object = MibTableColumn
sc10Serial = _Sc10Serial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 35, 1, 2),
    _Sc10Serial_Type()
)
sc10Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc10Serial.setStatus("current")
_Sc10Name_Type = DisplayString
_Sc10Name_Object = MibTableColumn
sc10Name = _Sc10Name_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 35, 1, 3),
    _Sc10Name_Type()
)
sc10Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc10Name.setStatus("current")
_Sc10Avail_Type = Gauge32
_Sc10Avail_Object = MibTableColumn
sc10Avail = _Sc10Avail_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 35, 1, 4),
    _Sc10Avail_Type()
)
sc10Avail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc10Avail.setStatus("current")


class _Sc10ControlMode_Type(Integer32):
    """Custom type sc10ControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("setpoint", 0),
          ("capacity", 1))
    )


_Sc10ControlMode_Type.__name__ = "Integer32"
_Sc10ControlMode_Object = MibTableColumn
sc10ControlMode = _Sc10ControlMode_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 35, 1, 5),
    _Sc10ControlMode_Type()
)
sc10ControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc10ControlMode.setStatus("current")


class _Sc10SetpointC_Type(Integer32):
    """Custom type sc10SetpointC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Sc10SetpointC_Type.__name__ = "Integer32"
_Sc10SetpointC_Object = MibTableColumn
sc10SetpointC = _Sc10SetpointC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 35, 1, 6),
    _Sc10SetpointC_Type()
)
sc10SetpointC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc10SetpointC.setStatus("current")
if mibBuilder.loadTexts:
    sc10SetpointC.setUnits("Degrees Celsius")


class _Sc10SetpointF_Type(Integer32):
    """Custom type sc10SetpointF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 212),
    )


_Sc10SetpointF_Type.__name__ = "Integer32"
_Sc10SetpointF_Object = MibTableColumn
sc10SetpointF = _Sc10SetpointF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 35, 1, 7),
    _Sc10SetpointF_Type()
)
sc10SetpointF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc10SetpointF.setStatus("current")
if mibBuilder.loadTexts:
    sc10SetpointF.setUnits("Degrees Fahrenheit")


class _Sc10TempC_Type(Integer32):
    """Custom type sc10TempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Sc10TempC_Type.__name__ = "Integer32"
_Sc10TempC_Object = MibTableColumn
sc10TempC = _Sc10TempC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 35, 1, 8),
    _Sc10TempC_Type()
)
sc10TempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc10TempC.setStatus("current")
if mibBuilder.loadTexts:
    sc10TempC.setUnits("Degrees Celsius")


class _Sc10TempF_Type(Integer32):
    """Custom type sc10TempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 212),
    )


_Sc10TempF_Type.__name__ = "Integer32"
_Sc10TempF_Object = MibTableColumn
sc10TempF = _Sc10TempF_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 35, 1, 9),
    _Sc10TempF_Type()
)
sc10TempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc10TempF.setStatus("current")
if mibBuilder.loadTexts:
    sc10TempF.setUnits("Degrees Fahrenheit")


class _Sc10Capacity_Type(Integer32):
    """Custom type sc10Capacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Sc10Capacity_Type.__name__ = "Integer32"
_Sc10Capacity_Object = MibTableColumn
sc10Capacity = _Sc10Capacity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 35, 1, 10),
    _Sc10Capacity_Type()
)
sc10Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc10Capacity.setStatus("current")
if mibBuilder.loadTexts:
    sc10Capacity.setUnits("%")
_AlarmSystem_ObjectIdentity = ObjectIdentity
alarmSystem = _AlarmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 2, 101)
)
_AlarmCfgTable_Object = MibTable
alarmCfgTable = _AlarmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 101, 1)
)
if mibBuilder.loadTexts:
    alarmCfgTable.setStatus("current")
_AlarmCfgEntry_Object = MibTableRow
alarmCfgEntry = _AlarmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 101, 1, 1)
)
alarmCfgEntry.setIndexNames(
    (0, "GEIST-MIB-V3", "alarmCfgIndex"),
)
if mibBuilder.loadTexts:
    alarmCfgEntry.setStatus("current")


class _AlarmCfgIndex_Type(Integer32):
    """Custom type alarmCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AlarmCfgIndex_Type.__name__ = "Integer32"
_AlarmCfgIndex_Object = MibTableColumn
alarmCfgIndex = _AlarmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 101, 1, 1, 1),
    _AlarmCfgIndex_Type()
)
alarmCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmCfgIndex.setStatus("current")
_AlarmCfgReadingID_Type = ObjectIdentifier
_AlarmCfgReadingID_Object = MibTableColumn
alarmCfgReadingID = _AlarmCfgReadingID_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 101, 1, 1, 2),
    _AlarmCfgReadingID_Type()
)
alarmCfgReadingID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmCfgReadingID.setStatus("current")
_AlarmCfgThreshold_Type = Integer32
_AlarmCfgThreshold_Object = MibTableColumn
alarmCfgThreshold = _AlarmCfgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 101, 1, 1, 3),
    _AlarmCfgThreshold_Type()
)
alarmCfgThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmCfgThreshold.setStatus("current")
if mibBuilder.loadTexts:
    alarmCfgThreshold.setUnits("Tenths")


class _AlarmCfgTripSelect_Type(Integer32):
    """Custom type alarmCfgTripSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tripBelow", 0),
          ("tripAbove", 1))
    )


_AlarmCfgTripSelect_Type.__name__ = "Integer32"
_AlarmCfgTripSelect_Object = MibTableColumn
alarmCfgTripSelect = _AlarmCfgTripSelect_Object(
    (1, 3, 6, 1, 4, 1, 21239, 2, 101, 1, 1, 4),
    _AlarmCfgTripSelect_Type()
)
alarmCfgTripSelect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmCfgTripSelect.setStatus("current")
_GstTrap_ObjectIdentity = ObjectIdentity
gstTrap = _GstTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767)
)
_GstTrapPrefix_ObjectIdentity = ObjectIdentity
gstTrapPrefix = _GstTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0)
)

# Managed Objects groups


# Notification objects

gstTestNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10101)
)
if mibBuilder.loadTexts:
    gstTestNOTIFY.setStatus(
        "current"
    )

gstClimateTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10205)
)
gstClimateTempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateTempC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateTempCNOTIFY.setStatus(
        "current"
    )

gstClimateTempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10206)
)
gstClimateTempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateTempF"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateTempFNOTIFY.setStatus(
        "current"
    )

gstClimateHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10207)
)
gstClimateHumidityNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateHumidity"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateHumidityNOTIFY.setStatus(
        "current"
    )

gstClimateLightNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10208)
)
gstClimateLightNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateLight"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateLightNOTIFY.setStatus(
        "current"
    )

gstClimateAirflowNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10209)
)
gstClimateAirflowNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateAirflow"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateAirflowNOTIFY.setStatus(
        "current"
    )

gstClimateSoundNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10210)
)
gstClimateSoundNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateSound"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateSoundNOTIFY.setStatus(
        "current"
    )

gstClimateIO1NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10211)
)
gstClimateIO1NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateIO1"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateIO1NOTIFY.setStatus(
        "current"
    )

gstClimateIO2NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10212)
)
gstClimateIO2NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateIO2"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateIO2NOTIFY.setStatus(
        "current"
    )

gstClimateIO3NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10213)
)
gstClimateIO3NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateIO3"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateIO3NOTIFY.setStatus(
        "current"
    )

gstClimateVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10214)
)
gstClimateVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateVolts"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateVoltsNOTIFY.setStatus(
        "current"
    )

gstClimateVoltPeakNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10215)
)
gstClimateVoltPeakNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateVoltPeak"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateVoltPeakNOTIFY.setStatus(
        "current"
    )

gstClimateDeciAmpsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10216)
)
gstClimateDeciAmpsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateDeciAmpsA"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpsANOTIFY.setStatus(
        "current"
    )

gstClimateDeciAmpPeakANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10217)
)
gstClimateDeciAmpPeakANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateDeciAmpPeakA"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpPeakANOTIFY.setStatus(
        "current"
    )

gstClimateRealPowerANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10218)
)
gstClimateRealPowerANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateRealPowerA"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRealPowerANOTIFY.setStatus(
        "current"
    )

gstClimateApparentPowerANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10219)
)
gstClimateApparentPowerANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateApparentPowerA"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateApparentPowerANOTIFY.setStatus(
        "current"
    )

gstClimatePowerFactorANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10220)
)
gstClimatePowerFactorANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climatePowerFactorA"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimatePowerFactorANOTIFY.setStatus(
        "current"
    )

gstClimateDeciAmpsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10221)
)
gstClimateDeciAmpsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateDeciAmpsB"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpsBNOTIFY.setStatus(
        "current"
    )

gstClimateDeciAmpPeakBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10222)
)
gstClimateDeciAmpPeakBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateDeciAmpPeakB"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpPeakBNOTIFY.setStatus(
        "current"
    )

gstClimateRealPowerBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10223)
)
gstClimateRealPowerBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateRealPowerB"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRealPowerBNOTIFY.setStatus(
        "current"
    )

gstClimateApparentPowerBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10224)
)
gstClimateApparentPowerBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateApparentPowerB"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateApparentPowerBNOTIFY.setStatus(
        "current"
    )

gstClimatePowerFactorBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10225)
)
gstClimatePowerFactorBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climatePowerFactorB"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimatePowerFactorBNOTIFY.setStatus(
        "current"
    )

gstClimateDeciAmpsCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10226)
)
gstClimateDeciAmpsCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateDeciAmpsC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpsCNOTIFY.setStatus(
        "current"
    )

gstClimateDeciAmpPeakCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10227)
)
gstClimateDeciAmpPeakCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateDeciAmpPeakC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpPeakCNOTIFY.setStatus(
        "current"
    )

gstClimateRealPowerCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10228)
)
gstClimateRealPowerCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateRealPowerC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRealPowerCNOTIFY.setStatus(
        "current"
    )

gstClimateApparentPowerCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10229)
)
gstClimateApparentPowerCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateApparentPowerC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateApparentPowerCNOTIFY.setStatus(
        "current"
    )

gstClimatePowerFactorCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10230)
)
gstClimatePowerFactorCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climatePowerFactorC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimatePowerFactorCNOTIFY.setStatus(
        "current"
    )

gstClimateDewPointCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10231)
)
gstClimateDewPointCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateDewPointC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDewPointCNOTIFY.setStatus(
        "current"
    )

gstClimateDewPointFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10232)
)
gstClimateDewPointFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateDewPointF"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDewPointFNOTIFY.setStatus(
        "current"
    )

gstPowMonkWattHrsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10305)
)
gstPowMonkWattHrsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonkWattHrs"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonkWattHrsNOTIFY.setStatus(
        "current"
    )

gstPowMonVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10306)
)
gstPowMonVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonVolts"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltsNOTIFY.setStatus(
        "current"
    )

gstPowMonVoltMaxNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10307)
)
gstPowMonVoltMaxNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonVoltMax"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltMaxNOTIFY.setStatus(
        "current"
    )

gstPowMonVoltMinNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10308)
)
gstPowMonVoltMinNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonVoltMin"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltMinNOTIFY.setStatus(
        "current"
    )

gstPowMonVoltPeakNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10309)
)
gstPowMonVoltPeakNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonVoltPeak"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltPeakNOTIFY.setStatus(
        "current"
    )

gstPowMonDeciAmpsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10310)
)
gstPowMonDeciAmpsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonDeciAmps"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonDeciAmpsNOTIFY.setStatus(
        "current"
    )

gstPowMonRealPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10311)
)
gstPowMonRealPowerNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonRealPower"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonRealPowerNOTIFY.setStatus(
        "current"
    )

gstPowMonApparentPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10312)
)
gstPowMonApparentPowerNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonApparentPower"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonApparentPowerNOTIFY.setStatus(
        "current"
    )

gstPowMonPowerFactorNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10313)
)
gstPowMonPowerFactorNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonPowerFactor"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonPowerFactorNOTIFY.setStatus(
        "current"
    )

gstPowMonOutlet1NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10314)
)
gstPowMonOutlet1NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonOutlet1"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonOutlet1NOTIFY.setStatus(
        "current"
    )

gstPowMonOutlet2NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10315)
)
gstPowMonOutlet2NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonOutlet2"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonOutlet2NOTIFY.setStatus(
        "current"
    )

gstPowMonOutlet1StatusTimeNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10316)
)
gstPowMonOutlet1StatusTimeNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonOutlet1StatusTime"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonOutlet1StatusTimeNOTIFY.setStatus(
        "current"
    )

gstPowMonOutlet2StatusTimeNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10317)
)
gstPowMonOutlet2StatusTimeNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powMonOutlet2StatusTime"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonOutlet2StatusTimeNOTIFY.setStatus(
        "current"
    )

gstTempSensorTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10405)
)
gstTempSensorTempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "tempSensorTempC"),
        ("GEIST-MIB-V3", "tempSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstTempSensorTempCNOTIFY.setStatus(
        "current"
    )

gstTempSensorTempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10406)
)
gstTempSensorTempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "tempSensorTempF"),
        ("GEIST-MIB-V3", "tempSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstTempSensorTempFNOTIFY.setStatus(
        "current"
    )

gstAirFlowSensorTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10505)
)
gstAirFlowSensorTempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "airFlowSensorTempC"),
        ("GEIST-MIB-V3", "airFlowSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorTempCNOTIFY.setStatus(
        "current"
    )

gstAirFlowSensorTempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10506)
)
gstAirFlowSensorTempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "airFlowSensorTempF"),
        ("GEIST-MIB-V3", "airFlowSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorTempFNOTIFY.setStatus(
        "current"
    )

gstAirFlowSensorFlowNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10507)
)
gstAirFlowSensorFlowNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "airFlowSensorFlow"),
        ("GEIST-MIB-V3", "airFlowSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorFlowNOTIFY.setStatus(
        "current"
    )

gstAirFlowSensorHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10508)
)
gstAirFlowSensorHumidityNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "airFlowSensorHumidity"),
        ("GEIST-MIB-V3", "airFlowSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorHumidityNOTIFY.setStatus(
        "current"
    )

gstAirFlowSensorDewPointCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10509)
)
gstAirFlowSensorDewPointCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "airFlowSensorDewPointC"),
        ("GEIST-MIB-V3", "airFlowSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorDewPointCNOTIFY.setStatus(
        "current"
    )

gstAirFlowSensorDewPointFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10510)
)
gstAirFlowSensorDewPointFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "airFlowSensorDewPointF"),
        ("GEIST-MIB-V3", "airFlowSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorDewPointFNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTADeciAmpsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10606)
)
gstCtrl3ChDELTADeciAmpsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTADeciAmpsA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTADeciAmpsANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTADeciAmpsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10607)
)
gstCtrl3ChDELTADeciAmpsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTADeciAmpsB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTADeciAmpsBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTADeciAmpsCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10608)
)
gstCtrl3ChDELTADeciAmpsCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTADeciAmpsC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTADeciAmpsCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAkWattHrsTotalNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10609)
)
gstCtrl3ChDELTAkWattHrsTotalNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAkWattHrsTotal"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAkWattHrsTotalNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTARealPowerTotalNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10610)
)
gstCtrl3ChDELTARealPowerTotalNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTARealPowerTotal"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTARealPowerTotalNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAkWattHrsABNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10611)
)
gstCtrl3ChDELTAkWattHrsABNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAkWattHrsAB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAkWattHrsABNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAVoltsABNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10612)
)
gstCtrl3ChDELTAVoltsABNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAVoltsAB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAVoltsABNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAVoltPeakABNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10613)
)
gstCtrl3ChDELTAVoltPeakABNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAVoltPeakAB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAVoltPeakABNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTARealPowerABNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10614)
)
gstCtrl3ChDELTARealPowerABNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTARealPowerAB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTARealPowerABNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAApparentPowerABNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10615)
)
gstCtrl3ChDELTAApparentPowerABNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAApparentPowerAB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAApparentPowerABNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAPowerFactorABNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10616)
)
gstCtrl3ChDELTAPowerFactorABNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAPowerFactorAB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAPowerFactorABNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAkWattHrsBCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10617)
)
gstCtrl3ChDELTAkWattHrsBCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAkWattHrsBC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAkWattHrsBCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAVoltsBCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10618)
)
gstCtrl3ChDELTAVoltsBCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAVoltsBC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAVoltsBCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAVoltPeakBCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10619)
)
gstCtrl3ChDELTAVoltPeakBCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAVoltPeakBC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAVoltPeakBCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTARealPowerBCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10620)
)
gstCtrl3ChDELTARealPowerBCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTARealPowerBC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTARealPowerBCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAApparentPowerBCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10621)
)
gstCtrl3ChDELTAApparentPowerBCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAApparentPowerBC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAApparentPowerBCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAPowerFactorBCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10622)
)
gstCtrl3ChDELTAPowerFactorBCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAPowerFactorBC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAPowerFactorBCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAkWattHrsCANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10623)
)
gstCtrl3ChDELTAkWattHrsCANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAkWattHrsCA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAkWattHrsCANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAVoltsCANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10624)
)
gstCtrl3ChDELTAVoltsCANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAVoltsCA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAVoltsCANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAVoltPeakCANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10625)
)
gstCtrl3ChDELTAVoltPeakCANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAVoltPeakCA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAVoltPeakCANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTARealPowerCANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10626)
)
gstCtrl3ChDELTARealPowerCANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTARealPowerCA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTARealPowerCANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAApparentPowerCANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10627)
)
gstCtrl3ChDELTAApparentPowerCANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAApparentPowerCA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAApparentPowerCANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDELTAPowerFactorCANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10628)
)
gstCtrl3ChDELTAPowerFactorCANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAPowerFactorCA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAPowerFactorCANOTIFY.setStatus(
        "current"
    )

gstDoorSensorStatusNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10705)
)
gstDoorSensorStatusNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "doorSensorStatus"),
        ("GEIST-MIB-V3", "doorSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDoorSensorStatusNOTIFY.setStatus(
        "current"
    )

gstWaterSensorDampnessNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10805)
)
gstWaterSensorDampnessNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "waterSensorDampness"),
        ("GEIST-MIB-V3", "waterSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstWaterSensorDampnessNOTIFY.setStatus(
        "current"
    )

gstCurrentMonitorDeciAmpsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 10905)
)
gstCurrentMonitorDeciAmpsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "currentMonitorDeciAmps"),
        ("GEIST-MIB-V3", "currentMonitorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCurrentMonitorDeciAmpsNOTIFY.setStatus(
        "current"
    )

gstMillivoltMonitorMVNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11005)
)
gstMillivoltMonitorMVNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "millivoltMonitorMV"),
        ("GEIST-MIB-V3", "millivoltMonitorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstMillivoltMonitorMVNOTIFY.setStatus(
        "current"
    )

gstPow3ChkWattHrsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11105)
)
gstPow3ChkWattHrsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChkWattHrsA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChkWattHrsANOTIFY.setStatus(
        "current"
    )

gstPow3ChVoltsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11106)
)
gstPow3ChVoltsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltsA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltsANOTIFY.setStatus(
        "current"
    )

gstPow3ChVoltMaxANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11107)
)
gstPow3ChVoltMaxANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltMaxA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMaxANOTIFY.setStatus(
        "current"
    )

gstPow3ChVoltMinANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11108)
)
gstPow3ChVoltMinANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltMinA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMinANOTIFY.setStatus(
        "current"
    )

gstPow3ChVoltPeakANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11109)
)
gstPow3ChVoltPeakANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltPeakA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltPeakANOTIFY.setStatus(
        "current"
    )

gstPow3ChDeciAmpsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11110)
)
gstPow3ChDeciAmpsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChDeciAmpsA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChDeciAmpsANOTIFY.setStatus(
        "current"
    )

gstPow3ChRealPowerANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11111)
)
gstPow3ChRealPowerANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChRealPowerA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerANOTIFY.setStatus(
        "current"
    )

gstPow3ChApparentPowerANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11112)
)
gstPow3ChApparentPowerANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChApparentPowerA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChApparentPowerANOTIFY.setStatus(
        "current"
    )

gstPow3ChPowerFactorANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11113)
)
gstPow3ChPowerFactorANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChPowerFactorA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChPowerFactorANOTIFY.setStatus(
        "current"
    )

gstPow3ChkWattHrsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11114)
)
gstPow3ChkWattHrsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChkWattHrsB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChkWattHrsBNOTIFY.setStatus(
        "current"
    )

gstPow3ChVoltsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11115)
)
gstPow3ChVoltsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltsB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltsBNOTIFY.setStatus(
        "current"
    )

gstPow3ChVoltMaxBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11116)
)
gstPow3ChVoltMaxBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltMaxB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMaxBNOTIFY.setStatus(
        "current"
    )

gstPow3ChVoltMinBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11117)
)
gstPow3ChVoltMinBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltMinB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMinBNOTIFY.setStatus(
        "current"
    )

gstPow3ChVoltPeakBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11118)
)
gstPow3ChVoltPeakBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltPeakB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltPeakBNOTIFY.setStatus(
        "current"
    )

gstPow3ChDeciAmpsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11119)
)
gstPow3ChDeciAmpsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChDeciAmpsB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChDeciAmpsBNOTIFY.setStatus(
        "current"
    )

gstPow3ChRealPowerBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11120)
)
gstPow3ChRealPowerBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChRealPowerB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerBNOTIFY.setStatus(
        "current"
    )

gstPow3ChApparentPowerBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11121)
)
gstPow3ChApparentPowerBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChApparentPowerB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChApparentPowerBNOTIFY.setStatus(
        "current"
    )

gstPow3ChPowerFactorBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11122)
)
gstPow3ChPowerFactorBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChPowerFactorB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChPowerFactorBNOTIFY.setStatus(
        "current"
    )

gstPow3ChkWattHrsCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11123)
)
gstPow3ChkWattHrsCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChkWattHrsC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChkWattHrsCNOTIFY.setStatus(
        "current"
    )

gstPow3ChVoltsCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11124)
)
gstPow3ChVoltsCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltsC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltsCNOTIFY.setStatus(
        "current"
    )

gstPow3ChVoltMaxCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11125)
)
gstPow3ChVoltMaxCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltMaxC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMaxCNOTIFY.setStatus(
        "current"
    )

gstPow3ChVoltMinCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11126)
)
gstPow3ChVoltMinCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltMinC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMinCNOTIFY.setStatus(
        "current"
    )

gstPow3ChVoltPeakCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11127)
)
gstPow3ChVoltPeakCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltPeakC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltPeakCNOTIFY.setStatus(
        "current"
    )

gstPow3ChDeciAmpsCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11128)
)
gstPow3ChDeciAmpsCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChDeciAmpsC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChDeciAmpsCNOTIFY.setStatus(
        "current"
    )

gstPow3ChRealPowerCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11129)
)
gstPow3ChRealPowerCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChRealPowerC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerCNOTIFY.setStatus(
        "current"
    )

gstPow3ChApparentPowerCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11130)
)
gstPow3ChApparentPowerCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChApparentPowerC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChApparentPowerCNOTIFY.setStatus(
        "current"
    )

gstPow3ChPowerFactorCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11131)
)
gstPow3ChPowerFactorCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChPowerFactorC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChPowerFactorCNOTIFY.setStatus(
        "current"
    )

gstPow3ChkWattHrsTotalNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11132)
)
gstPow3ChkWattHrsTotalNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChkWattHrsTotal"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChkWattHrsTotalNOTIFY.setStatus(
        "current"
    )

gstPow3ChRealPowerTotalNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11133)
)
gstPow3ChRealPowerTotalNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pow3ChRealPowerTotal"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerTotalNOTIFY.setStatus(
        "current"
    )

gstOutlet1StatusNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11205)
)
gstOutlet1StatusNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "outlet1Status"),
        ("GEIST-MIB-V3", "outletName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstOutlet1StatusNOTIFY.setStatus(
        "current"
    )

gstOutlet2StatusNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11206)
)
gstOutlet2StatusNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "outlet2Status"),
        ("GEIST-MIB-V3", "outletName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstOutlet2StatusNOTIFY.setStatus(
        "current"
    )

gstVsfcSetPointCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11305)
)
gstVsfcSetPointCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcSetPointC"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcSetPointCNOTIFY.setStatus(
        "current"
    )

gstVsfcSetPointFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11306)
)
gstVsfcSetPointFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcSetPointF"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcSetPointFNOTIFY.setStatus(
        "current"
    )

gstVsfcFanSpeedNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11307)
)
gstVsfcFanSpeedNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcFanSpeed"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcFanSpeedNOTIFY.setStatus(
        "current"
    )

gstVsfcIntTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11308)
)
gstVsfcIntTempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcIntTempC"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcIntTempCNOTIFY.setStatus(
        "current"
    )

gstVsfcIntTempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11309)
)
gstVsfcIntTempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcIntTempF"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcIntTempFNOTIFY.setStatus(
        "current"
    )

gstVsfcExt1TempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11310)
)
gstVsfcExt1TempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt1TempC"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt1TempCNOTIFY.setStatus(
        "current"
    )

gstVsfcExt1TempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11311)
)
gstVsfcExt1TempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt1TempF"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt1TempFNOTIFY.setStatus(
        "current"
    )

gstVsfcExt2TempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11312)
)
gstVsfcExt2TempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt2TempC"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt2TempCNOTIFY.setStatus(
        "current"
    )

gstVsfcExt2TempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11313)
)
gstVsfcExt2TempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt2TempF"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt2TempFNOTIFY.setStatus(
        "current"
    )

gstVsfcExt3TempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11314)
)
gstVsfcExt3TempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt3TempC"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt3TempCNOTIFY.setStatus(
        "current"
    )

gstVsfcExt3TempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11315)
)
gstVsfcExt3TempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt3TempF"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt3TempFNOTIFY.setStatus(
        "current"
    )

gstVsfcExt4TempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11316)
)
gstVsfcExt4TempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt4TempC"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt4TempCNOTIFY.setStatus(
        "current"
    )

gstVsfcExt4TempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11317)
)
gstVsfcExt4TempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt4TempF"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt4TempFNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChVoltsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11405)
)
gstCtrl3ChVoltsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChVoltsA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltsANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChVoltPeakANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11406)
)
gstCtrl3ChVoltPeakANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChVoltPeakA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltPeakANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDeciAmpsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11407)
)
gstCtrl3ChDeciAmpsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDeciAmpsA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDeciAmpsPeakANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11408)
)
gstCtrl3ChDeciAmpsPeakANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDeciAmpsPeakA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsPeakANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChRealPowerANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11409)
)
gstCtrl3ChRealPowerANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChRealPowerA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChRealPowerANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChApparentPowerANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11410)
)
gstCtrl3ChApparentPowerANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChApparentPowerA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChApparentPowerANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChPowerFactorANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11411)
)
gstCtrl3ChPowerFactorANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChPowerFactorA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChPowerFactorANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChVoltsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11412)
)
gstCtrl3ChVoltsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChVoltsB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltsBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChVoltPeakBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11413)
)
gstCtrl3ChVoltPeakBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChVoltPeakB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltPeakBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDeciAmpsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11414)
)
gstCtrl3ChDeciAmpsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDeciAmpsB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDeciAmpsPeakBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11415)
)
gstCtrl3ChDeciAmpsPeakBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDeciAmpsPeakB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsPeakBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChRealPowerBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11416)
)
gstCtrl3ChRealPowerBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChRealPowerB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChRealPowerBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChApparentPowerBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11417)
)
gstCtrl3ChApparentPowerBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChApparentPowerB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChApparentPowerBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChPowerFactorBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11418)
)
gstCtrl3ChPowerFactorBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChPowerFactorB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChPowerFactorBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChVoltsCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11419)
)
gstCtrl3ChVoltsCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChVoltsC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltsCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChVoltPeakCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11420)
)
gstCtrl3ChVoltPeakCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChVoltPeakC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltPeakCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDeciAmpsCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11421)
)
gstCtrl3ChDeciAmpsCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDeciAmpsC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChDeciAmpsPeakCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11422)
)
gstCtrl3ChDeciAmpsPeakCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDeciAmpsPeakC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsPeakCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChRealPowerCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11423)
)
gstCtrl3ChRealPowerCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChRealPowerC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChRealPowerCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChApparentPowerCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11424)
)
gstCtrl3ChApparentPowerCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChApparentPowerC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChApparentPowerCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChPowerFactorCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11425)
)
gstCtrl3ChPowerFactorCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChPowerFactorC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChPowerFactorCNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11505)
)
gstCtrlGrpAmpsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsA"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsANOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11506)
)
gstCtrlGrpAmpsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsB"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsBNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11507)
)
gstCtrlGrpAmpsCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsC"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsCNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsDNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11508)
)
gstCtrlGrpAmpsDNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsD"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsDNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsENOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11509)
)
gstCtrlGrpAmpsENOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsE"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsENOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11510)
)
gstCtrlGrpAmpsFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsF"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsFNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsGNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11511)
)
gstCtrlGrpAmpsGNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsG"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsGNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsHNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11512)
)
gstCtrlGrpAmpsHNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsH"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsHNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsAVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11513)
)
gstCtrlGrpAmpsAVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsAVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsAVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsBVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11514)
)
gstCtrlGrpAmpsBVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsBVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsBVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsCVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11515)
)
gstCtrlGrpAmpsCVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsCVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsCVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsDVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11516)
)
gstCtrlGrpAmpsDVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsDVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsDVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsEVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11517)
)
gstCtrlGrpAmpsEVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsEVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsEVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsFVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11518)
)
gstCtrlGrpAmpsFVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsFVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsFVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsGVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11519)
)
gstCtrlGrpAmpsGVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsGVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsGVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsHVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11520)
)
gstCtrlGrpAmpsHVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsHVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsHVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsINOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11521)
)
gstCtrlGrpAmpsINOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsI"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsINOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsJNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11522)
)
gstCtrlGrpAmpsJNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsJ"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsJNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsKNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11523)
)
gstCtrlGrpAmpsKNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsK"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsKNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsLNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11524)
)
gstCtrlGrpAmpsLNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsL"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsLNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsMNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11525)
)
gstCtrlGrpAmpsMNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsM"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsMNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsNNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11526)
)
gstCtrlGrpAmpsNNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsN"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsNNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsONOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11527)
)
gstCtrlGrpAmpsONOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsO"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsONOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsPNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11528)
)
gstCtrlGrpAmpsPNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsP"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsPNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsIVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11529)
)
gstCtrlGrpAmpsIVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsIVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsIVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsJVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11530)
)
gstCtrlGrpAmpsJVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsJVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsJVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsKVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11531)
)
gstCtrlGrpAmpsKVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsKVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsKVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsLVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11532)
)
gstCtrlGrpAmpsLVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsLVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsLVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsMVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11533)
)
gstCtrlGrpAmpsMVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsMVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsMVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsNVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11534)
)
gstCtrlGrpAmpsNVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsNVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsNVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsOVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11535)
)
gstCtrlGrpAmpsOVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsOVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsOVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlGrpAmpsPVoltsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11536)
)
gstCtrlGrpAmpsPVoltsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsPVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsPVoltsNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletPendingNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11605)
)
gstCtrlOutletPendingNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletPending"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletPendingNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletDeciAmpsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11606)
)
gstCtrlOutletDeciAmpsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletDeciAmps"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletDeciAmpsNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletGroupNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11607)
)
gstCtrlOutletGroupNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletGroup"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletGroupNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletUpDelayNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11608)
)
gstCtrlOutletUpDelayNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletUpDelay"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletUpDelayNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletDwnDelayNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11609)
)
gstCtrlOutletDwnDelayNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletDwnDelay"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletDwnDelayNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletRbtDurationNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11610)
)
gstCtrlOutletRbtDurationNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletRbtDuration"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletRbtDurationNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletURLNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11611)
)
gstCtrlOutletURLNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletURL"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletURLNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletPOAActionNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11612)
)
gstCtrlOutletPOAActionNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletPOAAction"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletPOAActionNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletPOADelayNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11613)
)
gstCtrlOutletPOADelayNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletPOADelay"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletPOADelayNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletkWattHrsNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11614)
)
gstCtrlOutletkWattHrsNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletkWattHrs"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletkWattHrsNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletPowerNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11615)
)
gstCtrlOutletPowerNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletPower"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletPowerNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletRbtDelayNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11616)
)
gstCtrlOutletRbtDelayNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletRbtDelay"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletRbtDelayNOTIFY.setStatus(
        "current"
    )

gstCtrlOutletStatusTimeNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11617)
)
gstCtrlOutletStatusTimeNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletStatusTime"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletStatusTimeNOTIFY.setStatus(
        "current"
    )

gstDewPointSensorTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11705)
)
gstDewPointSensorTempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dewPointSensorTempC"),
        ("GEIST-MIB-V3", "dewPointSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorTempCNOTIFY.setStatus(
        "current"
    )

gstDewPointSensorTempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11706)
)
gstDewPointSensorTempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dewPointSensorTempF"),
        ("GEIST-MIB-V3", "dewPointSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorTempFNOTIFY.setStatus(
        "current"
    )

gstDewPointSensorHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11707)
)
gstDewPointSensorHumidityNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dewPointSensorHumidity"),
        ("GEIST-MIB-V3", "dewPointSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorHumidityNOTIFY.setStatus(
        "current"
    )

gstDewPointSensorDewPointCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11708)
)
gstDewPointSensorDewPointCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dewPointSensorDewPointC"),
        ("GEIST-MIB-V3", "dewPointSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorDewPointCNOTIFY.setStatus(
        "current"
    )

gstDewPointSensorDewPointFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11709)
)
gstDewPointSensorDewPointFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dewPointSensorDewPointF"),
        ("GEIST-MIB-V3", "dewPointSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorDewPointFNOTIFY.setStatus(
        "current"
    )

gstDigitalSensorDigitalNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11805)
)
gstDigitalSensorDigitalNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "digitalSensorDigital"),
        ("GEIST-MIB-V3", "digitalSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDigitalSensorDigitalNOTIFY.setStatus(
        "current"
    )

gstDstsVoltsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11905)
)
gstDstsVoltsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dstsVoltsA"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsVoltsANOTIFY.setStatus(
        "current"
    )

gstDstsDeciAmpsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11906)
)
gstDstsDeciAmpsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dstsDeciAmpsA"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsDeciAmpsANOTIFY.setStatus(
        "current"
    )

gstDstsVoltsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11907)
)
gstDstsVoltsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dstsVoltsB"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsVoltsBNOTIFY.setStatus(
        "current"
    )

gstDstsDeciAmpsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11908)
)
gstDstsDeciAmpsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dstsDeciAmpsB"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsDeciAmpsBNOTIFY.setStatus(
        "current"
    )

gstDstsSourceAActiveNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11909)
)
gstDstsSourceAActiveNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dstsSourceAActive"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsSourceAActiveNOTIFY.setStatus(
        "current"
    )

gstDstsSourceBActiveNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11910)
)
gstDstsSourceBActiveNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dstsSourceBActive"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsSourceBActiveNOTIFY.setStatus(
        "current"
    )

gstDstsPowerStatusANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11911)
)
gstDstsPowerStatusANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dstsPowerStatusA"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsPowerStatusANOTIFY.setStatus(
        "current"
    )

gstDstsPowerStatusBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11912)
)
gstDstsPowerStatusBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dstsPowerStatusB"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsPowerStatusBNOTIFY.setStatus(
        "current"
    )

gstDstsSourceATempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11913)
)
gstDstsSourceATempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dstsSourceATempC"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsSourceATempCNOTIFY.setStatus(
        "current"
    )

gstDstsSourceBTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 11914)
)
gstDstsSourceBTempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "dstsSourceBTempC"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsSourceBTempCNOTIFY.setStatus(
        "current"
    )

gstCpmSensorStatusNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12005)
)
gstCpmSensorStatusNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "cpmSensorStatus"),
        ("GEIST-MIB-V3", "cpmSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCpmSensorStatusNOTIFY.setStatus(
        "current"
    )

gstSmokeAlarmStatusNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12105)
)
gstSmokeAlarmStatusNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "smokeAlarmStatus"),
        ("GEIST-MIB-V3", "smokeAlarmName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSmokeAlarmStatusNOTIFY.setStatus(
        "current"
    )

gstNeg48VdcSensorVoltageNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12205)
)
gstNeg48VdcSensorVoltageNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "neg48VdcSensorVoltage"),
        ("GEIST-MIB-V3", "neg48VdcSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstNeg48VdcSensorVoltageNOTIFY.setStatus(
        "current"
    )

gstPos30VdcSensorVoltageNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12305)
)
gstPos30VdcSensorVoltageNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pos30VdcSensorVoltage"),
        ("GEIST-MIB-V3", "pos30VdcSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPos30VdcSensorVoltageNOTIFY.setStatus(
        "current"
    )

gstAnalogSensorAnalogNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12405)
)
gstAnalogSensorAnalogNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "analogSensorAnalog"),
        ("GEIST-MIB-V3", "analogSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAnalogSensorAnalogNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECkWattHrsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12505)
)
gstCtrl3ChIECkWattHrsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECkWattHrsA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECkWattHrsANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECVoltsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12506)
)
gstCtrl3ChIECVoltsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECVoltsA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltsANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECVoltPeakANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12507)
)
gstCtrl3ChIECVoltPeakANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECVoltPeakA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltPeakANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECDeciAmpsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12508)
)
gstCtrl3ChIECDeciAmpsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECDeciAmpsA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECDeciAmpsPeakANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12509)
)
gstCtrl3ChIECDeciAmpsPeakANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECDeciAmpsPeakA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsPeakANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECRealPowerANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12510)
)
gstCtrl3ChIECRealPowerANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECRealPowerA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECApparentPowerANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12511)
)
gstCtrl3ChIECApparentPowerANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECApparentPowerA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECApparentPowerANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECPowerFactorANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12512)
)
gstCtrl3ChIECPowerFactorANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECPowerFactorA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECPowerFactorANOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECkWattHrsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12513)
)
gstCtrl3ChIECkWattHrsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECkWattHrsB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECkWattHrsBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECVoltsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12514)
)
gstCtrl3ChIECVoltsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECVoltsB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltsBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECVoltPeakBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12515)
)
gstCtrl3ChIECVoltPeakBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECVoltPeakB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltPeakBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECDeciAmpsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12516)
)
gstCtrl3ChIECDeciAmpsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECDeciAmpsB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECDeciAmpsPeakBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12517)
)
gstCtrl3ChIECDeciAmpsPeakBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECDeciAmpsPeakB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsPeakBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECRealPowerBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12518)
)
gstCtrl3ChIECRealPowerBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECRealPowerB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECApparentPowerBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12519)
)
gstCtrl3ChIECApparentPowerBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECApparentPowerB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECApparentPowerBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECPowerFactorBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12520)
)
gstCtrl3ChIECPowerFactorBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECPowerFactorB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECPowerFactorBNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECkWattHrsCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12521)
)
gstCtrl3ChIECkWattHrsCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECkWattHrsC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECkWattHrsCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECVoltsCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12522)
)
gstCtrl3ChIECVoltsCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECVoltsC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltsCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECVoltPeakCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12523)
)
gstCtrl3ChIECVoltPeakCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECVoltPeakC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltPeakCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECDeciAmpsCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12524)
)
gstCtrl3ChIECDeciAmpsCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECDeciAmpsC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECDeciAmpsPeakCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12525)
)
gstCtrl3ChIECDeciAmpsPeakCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECDeciAmpsPeakC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsPeakCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECRealPowerCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12526)
)
gstCtrl3ChIECRealPowerCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECRealPowerC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECApparentPowerCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12527)
)
gstCtrl3ChIECApparentPowerCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECApparentPowerC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECApparentPowerCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECPowerFactorCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12528)
)
gstCtrl3ChIECPowerFactorCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECPowerFactorC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECPowerFactorCNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECkWattHrsTotalNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12529)
)
gstCtrl3ChIECkWattHrsTotalNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECkWattHrsTotal"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECkWattHrsTotalNOTIFY.setStatus(
        "current"
    )

gstCtrl3ChIECRealPowerTotalNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12530)
)
gstCtrl3ChIECRealPowerTotalNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECRealPowerTotal"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerTotalNOTIFY.setStatus(
        "current"
    )

gstClimateRelayTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12605)
)
gstClimateRelayTempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateRelayTempC"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayTempCNOTIFY.setStatus(
        "current"
    )

gstClimateRelayTempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12606)
)
gstClimateRelayTempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateRelayTempF"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayTempFNOTIFY.setStatus(
        "current"
    )

gstClimateRelayIO1NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12607)
)
gstClimateRelayIO1NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateRelayIO1"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayIO1NOTIFY.setStatus(
        "current"
    )

gstClimateRelayIO2NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12608)
)
gstClimateRelayIO2NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateRelayIO2"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayIO2NOTIFY.setStatus(
        "current"
    )

gstClimateRelayIO3NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12609)
)
gstClimateRelayIO3NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateRelayIO3"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayIO3NOTIFY.setStatus(
        "current"
    )

gstClimateRelayIO4NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12610)
)
gstClimateRelayIO4NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateRelayIO4"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayIO4NOTIFY.setStatus(
        "current"
    )

gstClimateRelayIO5NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12611)
)
gstClimateRelayIO5NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateRelayIO5"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayIO5NOTIFY.setStatus(
        "current"
    )

gstClimateRelayIO6NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12612)
)
gstClimateRelayIO6NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "climateRelayIO6"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayIO6NOTIFY.setStatus(
        "current"
    )

gstAirSpeedSwitchSensorAirSpeedNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 12805)
)
gstAirSpeedSwitchSensorAirSpeedNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "airSpeedSwitchSensorAirSpeed"),
        ("GEIST-MIB-V3", "airSpeedSwitchSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirSpeedSwitchSensorAirSpeedNOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO1NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13037)
)
gstIoExpanderIO1NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO1"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO1NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO2NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13038)
)
gstIoExpanderIO2NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO2"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO2NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO3NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13039)
)
gstIoExpanderIO3NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO3"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO3NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO4NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13040)
)
gstIoExpanderIO4NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO4"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO4NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO5NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13041)
)
gstIoExpanderIO5NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO5"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO5NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO6NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13042)
)
gstIoExpanderIO6NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO6"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO6NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO7NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13043)
)
gstIoExpanderIO7NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO7"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO7NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO8NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13044)
)
gstIoExpanderIO8NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO8"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO8NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO9NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13045)
)
gstIoExpanderIO9NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO9"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO9NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO10NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13046)
)
gstIoExpanderIO10NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO10"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO10NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO11NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13047)
)
gstIoExpanderIO11NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO11"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO11NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO12NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13048)
)
gstIoExpanderIO12NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO12"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO12NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO13NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13049)
)
gstIoExpanderIO13NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO13"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO13NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO14NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13050)
)
gstIoExpanderIO14NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO14"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO14NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO15NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13051)
)
gstIoExpanderIO15NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO15"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO15NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO16NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13052)
)
gstIoExpanderIO16NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO16"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO16NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO17NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13053)
)
gstIoExpanderIO17NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO17"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO17NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO18NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13054)
)
gstIoExpanderIO18NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO18"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO18NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO19NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13055)
)
gstIoExpanderIO19NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO19"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO19NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO20NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13056)
)
gstIoExpanderIO20NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO20"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO20NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO21NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13057)
)
gstIoExpanderIO21NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO21"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO21NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO22NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13058)
)
gstIoExpanderIO22NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO22"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO22NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO23NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13059)
)
gstIoExpanderIO23NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO23"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO23NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO24NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13060)
)
gstIoExpanderIO24NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO24"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO24NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO25NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13061)
)
gstIoExpanderIO25NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO25"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO25NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO26NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13062)
)
gstIoExpanderIO26NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO26"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO26NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO27NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13063)
)
gstIoExpanderIO27NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO27"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO27NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO28NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13064)
)
gstIoExpanderIO28NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO28"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO28NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO29NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13065)
)
gstIoExpanderIO29NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO29"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO29NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO30NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13066)
)
gstIoExpanderIO30NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO30"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO30NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO31NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13067)
)
gstIoExpanderIO31NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO31"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO31NOTIFY.setStatus(
        "current"
    )

gstIoExpanderIO32NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13068)
)
gstIoExpanderIO32NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO32"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO32NOTIFY.setStatus(
        "current"
    )

gstT3hdSensorIntTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13106)
)
gstT3hdSensorIntTempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorIntTempC"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorIntTempCNOTIFY.setStatus(
        "current"
    )

gstT3hdSensorIntTempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13107)
)
gstT3hdSensorIntTempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorIntTempF"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorIntTempFNOTIFY.setStatus(
        "current"
    )

gstT3hdSensorIntHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13108)
)
gstT3hdSensorIntHumidityNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorIntHumidity"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorIntHumidityNOTIFY.setStatus(
        "current"
    )

gstT3hdSensorIntDewPointCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13109)
)
gstT3hdSensorIntDewPointCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorIntDewPointC"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorIntDewPointCNOTIFY.setStatus(
        "current"
    )

gstT3hdSensorIntDewPointFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13110)
)
gstT3hdSensorIntDewPointFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorIntDewPointF"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorIntDewPointFNOTIFY.setStatus(
        "current"
    )

gstT3hdSensorExt1TempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13113)
)
gstT3hdSensorExt1TempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorExt1TempC"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorExt1TempCNOTIFY.setStatus(
        "current"
    )

gstT3hdSensorExt1TempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13114)
)
gstT3hdSensorExt1TempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorExt1TempF"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorExt1TempFNOTIFY.setStatus(
        "current"
    )

gstT3hdSensorExt2TempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13117)
)
gstT3hdSensorExt2TempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorExt2TempC"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorExt2TempCNOTIFY.setStatus(
        "current"
    )

gstT3hdSensorExt2TempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13118)
)
gstT3hdSensorExt2TempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorExt2TempF"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorExt2TempFNOTIFY.setStatus(
        "current"
    )

gstThdSensorTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13205)
)
gstThdSensorTempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "thdSensorTempC"),
        ("GEIST-MIB-V3", "thdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstThdSensorTempCNOTIFY.setStatus(
        "current"
    )

gstThdSensorTempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13206)
)
gstThdSensorTempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "thdSensorTempF"),
        ("GEIST-MIB-V3", "thdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstThdSensorTempFNOTIFY.setStatus(
        "current"
    )

gstThdSensorHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13207)
)
gstThdSensorHumidityNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "thdSensorHumidity"),
        ("GEIST-MIB-V3", "thdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstThdSensorHumidityNOTIFY.setStatus(
        "current"
    )

gstThdSensorDewPointCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13208)
)
gstThdSensorDewPointCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "thdSensorDewPointC"),
        ("GEIST-MIB-V3", "thdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstThdSensorDewPointCNOTIFY.setStatus(
        "current"
    )

gstThdSensorDewPointFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13209)
)
gstThdSensorDewPointFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "thdSensorDewPointF"),
        ("GEIST-MIB-V3", "thdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstThdSensorDewPointFNOTIFY.setStatus(
        "current"
    )

gstPos60VdcSensorVoltageNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13305)
)
gstPos60VdcSensorVoltageNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "pos60VdcSensorVoltage"),
        ("GEIST-MIB-V3", "pos60VdcSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPos60VdcSensorVoltageNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotkWattHrsTotNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13405)
)
gstCtrl2CirTotkWattHrsTotNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotkWattHrsTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotkWattHrsTotNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotVoltsTotNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13406)
)
gstCtrl2CirTotVoltsTotNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotVoltsTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotVoltsTotNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotVoltPeakTotNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13407)
)
gstCtrl2CirTotVoltPeakTotNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotVoltPeakTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotVoltPeakTotNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotDeciAmpsTotNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13408)
)
gstCtrl2CirTotDeciAmpsTotNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotDeciAmpsTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotDeciAmpsTotNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotDeciAmpsPeakTotNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13409)
)
gstCtrl2CirTotDeciAmpsPeakTotNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotDeciAmpsPeakTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotDeciAmpsPeakTotNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotRealPowerTotNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13410)
)
gstCtrl2CirTotRealPowerTotNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotRealPowerTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotRealPowerTotNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotApparentPowerTotNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13411)
)
gstCtrl2CirTotApparentPowerTotNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotApparentPowerTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotApparentPowerTotNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotPowerFactorTotNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13412)
)
gstCtrl2CirTotPowerFactorTotNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotPowerFactorTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotPowerFactorTotNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotkWattHrsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13413)
)
gstCtrl2CirTotkWattHrsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotkWattHrsA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotkWattHrsANOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotVoltsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13414)
)
gstCtrl2CirTotVoltsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotVoltsA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotVoltsANOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotVoltPeakANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13415)
)
gstCtrl2CirTotVoltPeakANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotVoltPeakA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotVoltPeakANOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotDeciAmpsANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13416)
)
gstCtrl2CirTotDeciAmpsANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotDeciAmpsA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotDeciAmpsANOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotDeciAmpsPeakANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13417)
)
gstCtrl2CirTotDeciAmpsPeakANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotDeciAmpsPeakA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotDeciAmpsPeakANOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotRealPowerANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13418)
)
gstCtrl2CirTotRealPowerANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotRealPowerA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotRealPowerANOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotApparentPowerANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13419)
)
gstCtrl2CirTotApparentPowerANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotApparentPowerA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotApparentPowerANOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotPowerFactorANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13420)
)
gstCtrl2CirTotPowerFactorANOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotPowerFactorA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotPowerFactorANOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotkWattHrsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13421)
)
gstCtrl2CirTotkWattHrsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotkWattHrsB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotkWattHrsBNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotVoltsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13422)
)
gstCtrl2CirTotVoltsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotVoltsB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotVoltsBNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotVoltPeakBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13423)
)
gstCtrl2CirTotVoltPeakBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotVoltPeakB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotVoltPeakBNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotDeciAmpsBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13424)
)
gstCtrl2CirTotDeciAmpsBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotDeciAmpsB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotDeciAmpsBNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotDeciAmpsPeakBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13425)
)
gstCtrl2CirTotDeciAmpsPeakBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotDeciAmpsPeakB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotDeciAmpsPeakBNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotRealPowerBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13426)
)
gstCtrl2CirTotRealPowerBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotRealPowerB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotRealPowerBNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotApparentPowerBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13427)
)
gstCtrl2CirTotApparentPowerBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotApparentPowerB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotApparentPowerBNOTIFY.setStatus(
        "current"
    )

gstCtrl2CirTotPowerFactorBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13428)
)
gstCtrl2CirTotPowerFactorBNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotPowerFactorB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotPowerFactorBNOTIFY.setStatus(
        "current"
    )

gstSc10ControlModeNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13505)
)
gstSc10ControlModeNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "sc10ControlMode"),
        ("GEIST-MIB-V3", "sc10Name"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSc10ControlModeNOTIFY.setStatus(
        "current"
    )

gstSc10SetpointCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13506)
)
gstSc10SetpointCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "sc10SetpointC"),
        ("GEIST-MIB-V3", "sc10Name"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSc10SetpointCNOTIFY.setStatus(
        "current"
    )

gstSc10SetpointFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13507)
)
gstSc10SetpointFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "sc10SetpointF"),
        ("GEIST-MIB-V3", "sc10Name"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSc10SetpointFNOTIFY.setStatus(
        "current"
    )

gstSc10TempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13508)
)
gstSc10TempCNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "sc10TempC"),
        ("GEIST-MIB-V3", "sc10Name"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSc10TempCNOTIFY.setStatus(
        "current"
    )

gstSc10TempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13509)
)
gstSc10TempFNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "sc10TempF"),
        ("GEIST-MIB-V3", "sc10Name"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSc10TempFNOTIFY.setStatus(
        "current"
    )

gstSc10CapacityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 13510)
)
gstSc10CapacityNOTIFY.setObjects(
      *(("GEIST-MIB-V3", "sc10Capacity"),
        ("GEIST-MIB-V3", "sc10Name"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSc10CapacityNOTIFY.setStatus(
        "current"
    )

gstClimateTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20205)
)
gstClimateTempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateTempC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateTempCCLEAR.setStatus(
        "current"
    )

gstClimateTempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20206)
)
gstClimateTempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateTempF"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateTempFCLEAR.setStatus(
        "current"
    )

gstClimateHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20207)
)
gstClimateHumidityCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateHumidity"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateHumidityCLEAR.setStatus(
        "current"
    )

gstClimateLightCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20208)
)
gstClimateLightCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateLight"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateLightCLEAR.setStatus(
        "current"
    )

gstClimateAirflowCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20209)
)
gstClimateAirflowCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateAirflow"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateAirflowCLEAR.setStatus(
        "current"
    )

gstClimateSoundCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20210)
)
gstClimateSoundCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateSound"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateSoundCLEAR.setStatus(
        "current"
    )

gstClimateIO1CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20211)
)
gstClimateIO1CLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateIO1"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateIO1CLEAR.setStatus(
        "current"
    )

gstClimateIO2CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20212)
)
gstClimateIO2CLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateIO2"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateIO2CLEAR.setStatus(
        "current"
    )

gstClimateIO3CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20213)
)
gstClimateIO3CLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateIO3"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateIO3CLEAR.setStatus(
        "current"
    )

gstClimateVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20214)
)
gstClimateVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateVolts"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateVoltsCLEAR.setStatus(
        "current"
    )

gstClimateVoltPeakCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20215)
)
gstClimateVoltPeakCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateVoltPeak"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateVoltPeakCLEAR.setStatus(
        "current"
    )

gstClimateDeciAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20216)
)
gstClimateDeciAmpsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateDeciAmpsA"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpsACLEAR.setStatus(
        "current"
    )

gstClimateDeciAmpPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20217)
)
gstClimateDeciAmpPeakACLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateDeciAmpPeakA"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpPeakACLEAR.setStatus(
        "current"
    )

gstClimateRealPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20218)
)
gstClimateRealPowerACLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateRealPowerA"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRealPowerACLEAR.setStatus(
        "current"
    )

gstClimateApparentPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20219)
)
gstClimateApparentPowerACLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateApparentPowerA"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateApparentPowerACLEAR.setStatus(
        "current"
    )

gstClimatePowerFactorACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20220)
)
gstClimatePowerFactorACLEAR.setObjects(
      *(("GEIST-MIB-V3", "climatePowerFactorA"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimatePowerFactorACLEAR.setStatus(
        "current"
    )

gstClimateDeciAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20221)
)
gstClimateDeciAmpsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateDeciAmpsB"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpsBCLEAR.setStatus(
        "current"
    )

gstClimateDeciAmpPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20222)
)
gstClimateDeciAmpPeakBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateDeciAmpPeakB"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpPeakBCLEAR.setStatus(
        "current"
    )

gstClimateRealPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20223)
)
gstClimateRealPowerBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateRealPowerB"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRealPowerBCLEAR.setStatus(
        "current"
    )

gstClimateApparentPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20224)
)
gstClimateApparentPowerBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateApparentPowerB"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateApparentPowerBCLEAR.setStatus(
        "current"
    )

gstClimatePowerFactorBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20225)
)
gstClimatePowerFactorBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climatePowerFactorB"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimatePowerFactorBCLEAR.setStatus(
        "current"
    )

gstClimateDeciAmpsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20226)
)
gstClimateDeciAmpsCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateDeciAmpsC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpsCCLEAR.setStatus(
        "current"
    )

gstClimateDeciAmpPeakCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20227)
)
gstClimateDeciAmpPeakCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateDeciAmpPeakC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDeciAmpPeakCCLEAR.setStatus(
        "current"
    )

gstClimateRealPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20228)
)
gstClimateRealPowerCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateRealPowerC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRealPowerCCLEAR.setStatus(
        "current"
    )

gstClimateApparentPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20229)
)
gstClimateApparentPowerCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateApparentPowerC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateApparentPowerCCLEAR.setStatus(
        "current"
    )

gstClimatePowerFactorCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20230)
)
gstClimatePowerFactorCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climatePowerFactorC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimatePowerFactorCCLEAR.setStatus(
        "current"
    )

gstClimateDewPointCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20231)
)
gstClimateDewPointCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateDewPointC"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDewPointCCLEAR.setStatus(
        "current"
    )

gstClimateDewPointFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20232)
)
gstClimateDewPointFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateDewPointF"),
        ("GEIST-MIB-V3", "climateName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateDewPointFCLEAR.setStatus(
        "current"
    )

gstPowMonkWattHrsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20305)
)
gstPowMonkWattHrsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonkWattHrs"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonkWattHrsCLEAR.setStatus(
        "current"
    )

gstPowMonVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20306)
)
gstPowMonVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonVolts"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltsCLEAR.setStatus(
        "current"
    )

gstPowMonVoltMaxCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20307)
)
gstPowMonVoltMaxCLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonVoltMax"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltMaxCLEAR.setStatus(
        "current"
    )

gstPowMonVoltMinCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20308)
)
gstPowMonVoltMinCLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonVoltMin"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltMinCLEAR.setStatus(
        "current"
    )

gstPowMonVoltPeakCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20309)
)
gstPowMonVoltPeakCLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonVoltPeak"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonVoltPeakCLEAR.setStatus(
        "current"
    )

gstPowMonDeciAmpsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20310)
)
gstPowMonDeciAmpsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonDeciAmps"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonDeciAmpsCLEAR.setStatus(
        "current"
    )

gstPowMonRealPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20311)
)
gstPowMonRealPowerCLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonRealPower"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonRealPowerCLEAR.setStatus(
        "current"
    )

gstPowMonApparentPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20312)
)
gstPowMonApparentPowerCLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonApparentPower"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonApparentPowerCLEAR.setStatus(
        "current"
    )

gstPowMonPowerFactorCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20313)
)
gstPowMonPowerFactorCLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonPowerFactor"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonPowerFactorCLEAR.setStatus(
        "current"
    )

gstPowMonOutlet1CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20314)
)
gstPowMonOutlet1CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonOutlet1"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonOutlet1CLEAR.setStatus(
        "current"
    )

gstPowMonOutlet2CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20315)
)
gstPowMonOutlet2CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonOutlet2"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonOutlet2CLEAR.setStatus(
        "current"
    )

gstPowMonOutlet1StatusTimeCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20316)
)
gstPowMonOutlet1StatusTimeCLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonOutlet1StatusTime"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonOutlet1StatusTimeCLEAR.setStatus(
        "current"
    )

gstPowMonOutlet2StatusTimeCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20317)
)
gstPowMonOutlet2StatusTimeCLEAR.setObjects(
      *(("GEIST-MIB-V3", "powMonOutlet2StatusTime"),
        ("GEIST-MIB-V3", "powMonName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowMonOutlet2StatusTimeCLEAR.setStatus(
        "current"
    )

gstTempSensorTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20405)
)
gstTempSensorTempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "tempSensorTempC"),
        ("GEIST-MIB-V3", "tempSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstTempSensorTempCCLEAR.setStatus(
        "current"
    )

gstTempSensorTempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20406)
)
gstTempSensorTempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "tempSensorTempF"),
        ("GEIST-MIB-V3", "tempSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstTempSensorTempFCLEAR.setStatus(
        "current"
    )

gstAirFlowSensorTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20505)
)
gstAirFlowSensorTempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "airFlowSensorTempC"),
        ("GEIST-MIB-V3", "airFlowSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorTempCCLEAR.setStatus(
        "current"
    )

gstAirFlowSensorTempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20506)
)
gstAirFlowSensorTempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "airFlowSensorTempF"),
        ("GEIST-MIB-V3", "airFlowSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorTempFCLEAR.setStatus(
        "current"
    )

gstAirFlowSensorFlowCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20507)
)
gstAirFlowSensorFlowCLEAR.setObjects(
      *(("GEIST-MIB-V3", "airFlowSensorFlow"),
        ("GEIST-MIB-V3", "airFlowSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorFlowCLEAR.setStatus(
        "current"
    )

gstAirFlowSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20508)
)
gstAirFlowSensorHumidityCLEAR.setObjects(
      *(("GEIST-MIB-V3", "airFlowSensorHumidity"),
        ("GEIST-MIB-V3", "airFlowSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorHumidityCLEAR.setStatus(
        "current"
    )

gstAirFlowSensorDewPointCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20509)
)
gstAirFlowSensorDewPointCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "airFlowSensorDewPointC"),
        ("GEIST-MIB-V3", "airFlowSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorDewPointCCLEAR.setStatus(
        "current"
    )

gstAirFlowSensorDewPointFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20510)
)
gstAirFlowSensorDewPointFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "airFlowSensorDewPointF"),
        ("GEIST-MIB-V3", "airFlowSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirFlowSensorDewPointFCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTADeciAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20606)
)
gstCtrl3ChDELTADeciAmpsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTADeciAmpsA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTADeciAmpsACLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTADeciAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20607)
)
gstCtrl3ChDELTADeciAmpsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTADeciAmpsB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTADeciAmpsBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTADeciAmpsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20608)
)
gstCtrl3ChDELTADeciAmpsCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTADeciAmpsC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTADeciAmpsCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAkWattHrsTotalCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20609)
)
gstCtrl3ChDELTAkWattHrsTotalCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAkWattHrsTotal"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAkWattHrsTotalCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTARealPowerTotalCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20610)
)
gstCtrl3ChDELTARealPowerTotalCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTARealPowerTotal"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTARealPowerTotalCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAkWattHrsABCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20611)
)
gstCtrl3ChDELTAkWattHrsABCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAkWattHrsAB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAkWattHrsABCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAVoltsABCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20612)
)
gstCtrl3ChDELTAVoltsABCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAVoltsAB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAVoltsABCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAVoltPeakABCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20613)
)
gstCtrl3ChDELTAVoltPeakABCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAVoltPeakAB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAVoltPeakABCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTARealPowerABCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20614)
)
gstCtrl3ChDELTARealPowerABCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTARealPowerAB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTARealPowerABCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAApparentPowerABCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20615)
)
gstCtrl3ChDELTAApparentPowerABCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAApparentPowerAB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAApparentPowerABCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAPowerFactorABCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20616)
)
gstCtrl3ChDELTAPowerFactorABCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAPowerFactorAB"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAPowerFactorABCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAkWattHrsBCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20617)
)
gstCtrl3ChDELTAkWattHrsBCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAkWattHrsBC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAkWattHrsBCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAVoltsBCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20618)
)
gstCtrl3ChDELTAVoltsBCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAVoltsBC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAVoltsBCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAVoltPeakBCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20619)
)
gstCtrl3ChDELTAVoltPeakBCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAVoltPeakBC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAVoltPeakBCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTARealPowerBCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20620)
)
gstCtrl3ChDELTARealPowerBCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTARealPowerBC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTARealPowerBCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAApparentPowerBCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20621)
)
gstCtrl3ChDELTAApparentPowerBCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAApparentPowerBC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAApparentPowerBCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAPowerFactorBCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20622)
)
gstCtrl3ChDELTAPowerFactorBCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAPowerFactorBC"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAPowerFactorBCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAkWattHrsCACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20623)
)
gstCtrl3ChDELTAkWattHrsCACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAkWattHrsCA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAkWattHrsCACLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAVoltsCACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20624)
)
gstCtrl3ChDELTAVoltsCACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAVoltsCA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAVoltsCACLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAVoltPeakCACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20625)
)
gstCtrl3ChDELTAVoltPeakCACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAVoltPeakCA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAVoltPeakCACLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTARealPowerCACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20626)
)
gstCtrl3ChDELTARealPowerCACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTARealPowerCA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTARealPowerCACLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAApparentPowerCACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20627)
)
gstCtrl3ChDELTAApparentPowerCACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAApparentPowerCA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAApparentPowerCACLEAR.setStatus(
        "current"
    )

gstCtrl3ChDELTAPowerFactorCACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20628)
)
gstCtrl3ChDELTAPowerFactorCACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDELTAPowerFactorCA"),
        ("GEIST-MIB-V3", "ctrl3ChDELTAName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDELTAPowerFactorCACLEAR.setStatus(
        "current"
    )

gstDoorSensorStatusCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20705)
)
gstDoorSensorStatusCLEAR.setObjects(
      *(("GEIST-MIB-V3", "doorSensorStatus"),
        ("GEIST-MIB-V3", "doorSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDoorSensorStatusCLEAR.setStatus(
        "current"
    )

gstWaterSensorDampnessCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20805)
)
gstWaterSensorDampnessCLEAR.setObjects(
      *(("GEIST-MIB-V3", "waterSensorDampness"),
        ("GEIST-MIB-V3", "waterSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstWaterSensorDampnessCLEAR.setStatus(
        "current"
    )

gstCurrentMonitorDeciAmpsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 20905)
)
gstCurrentMonitorDeciAmpsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "currentMonitorDeciAmps"),
        ("GEIST-MIB-V3", "currentMonitorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCurrentMonitorDeciAmpsCLEAR.setStatus(
        "current"
    )

gstMillivoltMonitorMVCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21005)
)
gstMillivoltMonitorMVCLEAR.setObjects(
      *(("GEIST-MIB-V3", "millivoltMonitorMV"),
        ("GEIST-MIB-V3", "millivoltMonitorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstMillivoltMonitorMVCLEAR.setStatus(
        "current"
    )

gstPow3ChkWattHrsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21105)
)
gstPow3ChkWattHrsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChkWattHrsA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChkWattHrsACLEAR.setStatus(
        "current"
    )

gstPow3ChVoltsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21106)
)
gstPow3ChVoltsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltsA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltsACLEAR.setStatus(
        "current"
    )

gstPow3ChVoltMaxACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21107)
)
gstPow3ChVoltMaxACLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltMaxA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMaxACLEAR.setStatus(
        "current"
    )

gstPow3ChVoltMinACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21108)
)
gstPow3ChVoltMinACLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltMinA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMinACLEAR.setStatus(
        "current"
    )

gstPow3ChVoltPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21109)
)
gstPow3ChVoltPeakACLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltPeakA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltPeakACLEAR.setStatus(
        "current"
    )

gstPow3ChDeciAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21110)
)
gstPow3ChDeciAmpsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChDeciAmpsA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChDeciAmpsACLEAR.setStatus(
        "current"
    )

gstPow3ChRealPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21111)
)
gstPow3ChRealPowerACLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChRealPowerA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerACLEAR.setStatus(
        "current"
    )

gstPow3ChApparentPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21112)
)
gstPow3ChApparentPowerACLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChApparentPowerA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChApparentPowerACLEAR.setStatus(
        "current"
    )

gstPow3ChPowerFactorACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21113)
)
gstPow3ChPowerFactorACLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChPowerFactorA"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChPowerFactorACLEAR.setStatus(
        "current"
    )

gstPow3ChkWattHrsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21114)
)
gstPow3ChkWattHrsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChkWattHrsB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChkWattHrsBCLEAR.setStatus(
        "current"
    )

gstPow3ChVoltsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21115)
)
gstPow3ChVoltsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltsB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltsBCLEAR.setStatus(
        "current"
    )

gstPow3ChVoltMaxBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21116)
)
gstPow3ChVoltMaxBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltMaxB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMaxBCLEAR.setStatus(
        "current"
    )

gstPow3ChVoltMinBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21117)
)
gstPow3ChVoltMinBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltMinB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMinBCLEAR.setStatus(
        "current"
    )

gstPow3ChVoltPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21118)
)
gstPow3ChVoltPeakBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltPeakB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltPeakBCLEAR.setStatus(
        "current"
    )

gstPow3ChDeciAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21119)
)
gstPow3ChDeciAmpsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChDeciAmpsB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChDeciAmpsBCLEAR.setStatus(
        "current"
    )

gstPow3ChRealPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21120)
)
gstPow3ChRealPowerBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChRealPowerB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerBCLEAR.setStatus(
        "current"
    )

gstPow3ChApparentPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21121)
)
gstPow3ChApparentPowerBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChApparentPowerB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChApparentPowerBCLEAR.setStatus(
        "current"
    )

gstPow3ChPowerFactorBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21122)
)
gstPow3ChPowerFactorBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChPowerFactorB"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChPowerFactorBCLEAR.setStatus(
        "current"
    )

gstPow3ChkWattHrsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21123)
)
gstPow3ChkWattHrsCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChkWattHrsC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChkWattHrsCCLEAR.setStatus(
        "current"
    )

gstPow3ChVoltsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21124)
)
gstPow3ChVoltsCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltsC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltsCCLEAR.setStatus(
        "current"
    )

gstPow3ChVoltMaxCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21125)
)
gstPow3ChVoltMaxCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltMaxC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMaxCCLEAR.setStatus(
        "current"
    )

gstPow3ChVoltMinCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21126)
)
gstPow3ChVoltMinCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltMinC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltMinCCLEAR.setStatus(
        "current"
    )

gstPow3ChVoltPeakCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21127)
)
gstPow3ChVoltPeakCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChVoltPeakC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChVoltPeakCCLEAR.setStatus(
        "current"
    )

gstPow3ChDeciAmpsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21128)
)
gstPow3ChDeciAmpsCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChDeciAmpsC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChDeciAmpsCCLEAR.setStatus(
        "current"
    )

gstPow3ChRealPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21129)
)
gstPow3ChRealPowerCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChRealPowerC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerCCLEAR.setStatus(
        "current"
    )

gstPow3ChApparentPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21130)
)
gstPow3ChApparentPowerCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChApparentPowerC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChApparentPowerCCLEAR.setStatus(
        "current"
    )

gstPow3ChPowerFactorCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21131)
)
gstPow3ChPowerFactorCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChPowerFactorC"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChPowerFactorCCLEAR.setStatus(
        "current"
    )

gstPow3ChkWattHrsTotalCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21132)
)
gstPow3ChkWattHrsTotalCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChkWattHrsTotal"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChkWattHrsTotalCLEAR.setStatus(
        "current"
    )

gstPow3ChRealPowerTotalCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21133)
)
gstPow3ChRealPowerTotalCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pow3ChRealPowerTotal"),
        ("GEIST-MIB-V3", "pow3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPow3ChRealPowerTotalCLEAR.setStatus(
        "current"
    )

gstOutlet1StatusCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21205)
)
gstOutlet1StatusCLEAR.setObjects(
      *(("GEIST-MIB-V3", "outlet1Status"),
        ("GEIST-MIB-V3", "outletName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstOutlet1StatusCLEAR.setStatus(
        "current"
    )

gstOutlet2StatusCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21206)
)
gstOutlet2StatusCLEAR.setObjects(
      *(("GEIST-MIB-V3", "outlet2Status"),
        ("GEIST-MIB-V3", "outletName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstOutlet2StatusCLEAR.setStatus(
        "current"
    )

gstVsfcSetPointCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21305)
)
gstVsfcSetPointCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcSetPointC"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcSetPointCCLEAR.setStatus(
        "current"
    )

gstVsfcSetPointFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21306)
)
gstVsfcSetPointFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcSetPointF"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcSetPointFCLEAR.setStatus(
        "current"
    )

gstVsfcFanSpeedCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21307)
)
gstVsfcFanSpeedCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcFanSpeed"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcFanSpeedCLEAR.setStatus(
        "current"
    )

gstVsfcIntTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21308)
)
gstVsfcIntTempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcIntTempC"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcIntTempCCLEAR.setStatus(
        "current"
    )

gstVsfcIntTempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21309)
)
gstVsfcIntTempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcIntTempF"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcIntTempFCLEAR.setStatus(
        "current"
    )

gstVsfcExt1TempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21310)
)
gstVsfcExt1TempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt1TempC"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt1TempCCLEAR.setStatus(
        "current"
    )

gstVsfcExt1TempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21311)
)
gstVsfcExt1TempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt1TempF"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt1TempFCLEAR.setStatus(
        "current"
    )

gstVsfcExt2TempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21312)
)
gstVsfcExt2TempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt2TempC"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt2TempCCLEAR.setStatus(
        "current"
    )

gstVsfcExt2TempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21313)
)
gstVsfcExt2TempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt2TempF"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt2TempFCLEAR.setStatus(
        "current"
    )

gstVsfcExt3TempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21314)
)
gstVsfcExt3TempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt3TempC"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt3TempCCLEAR.setStatus(
        "current"
    )

gstVsfcExt3TempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21315)
)
gstVsfcExt3TempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt3TempF"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt3TempFCLEAR.setStatus(
        "current"
    )

gstVsfcExt4TempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21316)
)
gstVsfcExt4TempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt4TempC"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt4TempCCLEAR.setStatus(
        "current"
    )

gstVsfcExt4TempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21317)
)
gstVsfcExt4TempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "vsfcExt4TempF"),
        ("GEIST-MIB-V3", "vsfcName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstVsfcExt4TempFCLEAR.setStatus(
        "current"
    )

gstCtrl3ChVoltsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21405)
)
gstCtrl3ChVoltsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChVoltsA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltsACLEAR.setStatus(
        "current"
    )

gstCtrl3ChVoltPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21406)
)
gstCtrl3ChVoltPeakACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChVoltPeakA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltPeakACLEAR.setStatus(
        "current"
    )

gstCtrl3ChDeciAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21407)
)
gstCtrl3ChDeciAmpsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDeciAmpsA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsACLEAR.setStatus(
        "current"
    )

gstCtrl3ChDeciAmpsPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21408)
)
gstCtrl3ChDeciAmpsPeakACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDeciAmpsPeakA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsPeakACLEAR.setStatus(
        "current"
    )

gstCtrl3ChRealPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21409)
)
gstCtrl3ChRealPowerACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChRealPowerA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChRealPowerACLEAR.setStatus(
        "current"
    )

gstCtrl3ChApparentPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21410)
)
gstCtrl3ChApparentPowerACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChApparentPowerA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChApparentPowerACLEAR.setStatus(
        "current"
    )

gstCtrl3ChPowerFactorACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21411)
)
gstCtrl3ChPowerFactorACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChPowerFactorA"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChPowerFactorACLEAR.setStatus(
        "current"
    )

gstCtrl3ChVoltsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21412)
)
gstCtrl3ChVoltsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChVoltsB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltsBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChVoltPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21413)
)
gstCtrl3ChVoltPeakBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChVoltPeakB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltPeakBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDeciAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21414)
)
gstCtrl3ChDeciAmpsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDeciAmpsB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDeciAmpsPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21415)
)
gstCtrl3ChDeciAmpsPeakBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDeciAmpsPeakB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsPeakBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChRealPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21416)
)
gstCtrl3ChRealPowerBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChRealPowerB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChRealPowerBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChApparentPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21417)
)
gstCtrl3ChApparentPowerBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChApparentPowerB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChApparentPowerBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChPowerFactorBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21418)
)
gstCtrl3ChPowerFactorBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChPowerFactorB"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChPowerFactorBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChVoltsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21419)
)
gstCtrl3ChVoltsCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChVoltsC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltsCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChVoltPeakCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21420)
)
gstCtrl3ChVoltPeakCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChVoltPeakC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChVoltPeakCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDeciAmpsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21421)
)
gstCtrl3ChDeciAmpsCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDeciAmpsC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChDeciAmpsPeakCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21422)
)
gstCtrl3ChDeciAmpsPeakCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChDeciAmpsPeakC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChDeciAmpsPeakCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChRealPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21423)
)
gstCtrl3ChRealPowerCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChRealPowerC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChRealPowerCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChApparentPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21424)
)
gstCtrl3ChApparentPowerCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChApparentPowerC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChApparentPowerCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChPowerFactorCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21425)
)
gstCtrl3ChPowerFactorCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChPowerFactorC"),
        ("GEIST-MIB-V3", "ctrl3ChName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChPowerFactorCCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21505)
)
gstCtrlGrpAmpsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsA"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsACLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21506)
)
gstCtrlGrpAmpsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsB"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsBCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21507)
)
gstCtrlGrpAmpsCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsC"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsCCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsDCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21508)
)
gstCtrlGrpAmpsDCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsD"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsDCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsECLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21509)
)
gstCtrlGrpAmpsECLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsE"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsECLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21510)
)
gstCtrlGrpAmpsFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsF"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsFCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsGCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21511)
)
gstCtrlGrpAmpsGCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsG"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsGCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsHCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21512)
)
gstCtrlGrpAmpsHCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsH"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsHCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsAVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21513)
)
gstCtrlGrpAmpsAVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsAVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsAVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsBVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21514)
)
gstCtrlGrpAmpsBVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsBVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsBVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsCVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21515)
)
gstCtrlGrpAmpsCVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsCVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsCVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsDVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21516)
)
gstCtrlGrpAmpsDVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsDVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsDVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsEVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21517)
)
gstCtrlGrpAmpsEVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsEVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsEVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsFVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21518)
)
gstCtrlGrpAmpsFVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsFVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsFVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsGVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21519)
)
gstCtrlGrpAmpsGVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsGVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsGVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsHVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21520)
)
gstCtrlGrpAmpsHVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsHVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsHVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsICLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21521)
)
gstCtrlGrpAmpsICLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsI"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsICLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsJCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21522)
)
gstCtrlGrpAmpsJCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsJ"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsJCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsKCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21523)
)
gstCtrlGrpAmpsKCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsK"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsKCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsLCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21524)
)
gstCtrlGrpAmpsLCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsL"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsLCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsMCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21525)
)
gstCtrlGrpAmpsMCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsM"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsMCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsNCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21526)
)
gstCtrlGrpAmpsNCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsN"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsNCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsOCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21527)
)
gstCtrlGrpAmpsOCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsO"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsOCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsPCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21528)
)
gstCtrlGrpAmpsPCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsP"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsPCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsIVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21529)
)
gstCtrlGrpAmpsIVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsIVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsIVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsJVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21530)
)
gstCtrlGrpAmpsJVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsJVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsJVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsKVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21531)
)
gstCtrlGrpAmpsKVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsKVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsKVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsLVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21532)
)
gstCtrlGrpAmpsLVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsLVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsLVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsMVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21533)
)
gstCtrlGrpAmpsMVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsMVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsMVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsNVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21534)
)
gstCtrlGrpAmpsNVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsNVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsNVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsOVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21535)
)
gstCtrlGrpAmpsOVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsOVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsOVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlGrpAmpsPVoltsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21536)
)
gstCtrlGrpAmpsPVoltsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlGrpAmpsPVolts"),
        ("GEIST-MIB-V3", "ctrlGrpAmpsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlGrpAmpsPVoltsCLEAR.setStatus(
        "current"
    )

gstCtrlOutletPendingCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21605)
)
gstCtrlOutletPendingCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletPending"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletPendingCLEAR.setStatus(
        "current"
    )

gstCtrlOutletDeciAmpsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21606)
)
gstCtrlOutletDeciAmpsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletDeciAmps"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletDeciAmpsCLEAR.setStatus(
        "current"
    )

gstCtrlOutletGroupCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21607)
)
gstCtrlOutletGroupCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletGroup"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletGroupCLEAR.setStatus(
        "current"
    )

gstCtrlOutletUpDelayCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21608)
)
gstCtrlOutletUpDelayCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletUpDelay"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletUpDelayCLEAR.setStatus(
        "current"
    )

gstCtrlOutletDwnDelayCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21609)
)
gstCtrlOutletDwnDelayCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletDwnDelay"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletDwnDelayCLEAR.setStatus(
        "current"
    )

gstCtrlOutletRbtDurationCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21610)
)
gstCtrlOutletRbtDurationCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletRbtDuration"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletRbtDurationCLEAR.setStatus(
        "current"
    )

gstCtrlOutletURLCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21611)
)
gstCtrlOutletURLCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletURL"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletURLCLEAR.setStatus(
        "current"
    )

gstCtrlOutletPOAActionCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21612)
)
gstCtrlOutletPOAActionCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletPOAAction"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletPOAActionCLEAR.setStatus(
        "current"
    )

gstCtrlOutletPOADelayCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21613)
)
gstCtrlOutletPOADelayCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletPOADelay"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletPOADelayCLEAR.setStatus(
        "current"
    )

gstCtrlOutletkWattHrsCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21614)
)
gstCtrlOutletkWattHrsCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletkWattHrs"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletkWattHrsCLEAR.setStatus(
        "current"
    )

gstCtrlOutletPowerCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21615)
)
gstCtrlOutletPowerCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletPower"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletPowerCLEAR.setStatus(
        "current"
    )

gstCtrlOutletRbtDelayCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21616)
)
gstCtrlOutletRbtDelayCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletRbtDelay"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletRbtDelayCLEAR.setStatus(
        "current"
    )

gstCtrlOutletStatusTimeCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21617)
)
gstCtrlOutletStatusTimeCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrlOutletStatusTime"),
        ("GEIST-MIB-V3", "ctrlOutletStatus"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrlOutletStatusTimeCLEAR.setStatus(
        "current"
    )

gstDewPointSensorTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21705)
)
gstDewPointSensorTempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "dewPointSensorTempC"),
        ("GEIST-MIB-V3", "dewPointSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorTempCCLEAR.setStatus(
        "current"
    )

gstDewPointSensorTempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21706)
)
gstDewPointSensorTempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "dewPointSensorTempF"),
        ("GEIST-MIB-V3", "dewPointSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorTempFCLEAR.setStatus(
        "current"
    )

gstDewPointSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21707)
)
gstDewPointSensorHumidityCLEAR.setObjects(
      *(("GEIST-MIB-V3", "dewPointSensorHumidity"),
        ("GEIST-MIB-V3", "dewPointSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorHumidityCLEAR.setStatus(
        "current"
    )

gstDewPointSensorDewPointCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21708)
)
gstDewPointSensorDewPointCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "dewPointSensorDewPointC"),
        ("GEIST-MIB-V3", "dewPointSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorDewPointCCLEAR.setStatus(
        "current"
    )

gstDewPointSensorDewPointFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21709)
)
gstDewPointSensorDewPointFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "dewPointSensorDewPointF"),
        ("GEIST-MIB-V3", "dewPointSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDewPointSensorDewPointFCLEAR.setStatus(
        "current"
    )

gstDigitalSensorDigitalCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21805)
)
gstDigitalSensorDigitalCLEAR.setObjects(
      *(("GEIST-MIB-V3", "digitalSensorDigital"),
        ("GEIST-MIB-V3", "digitalSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDigitalSensorDigitalCLEAR.setStatus(
        "current"
    )

gstDstsVoltsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21905)
)
gstDstsVoltsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "dstsVoltsA"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsVoltsACLEAR.setStatus(
        "current"
    )

gstDstsDeciAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21906)
)
gstDstsDeciAmpsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "dstsDeciAmpsA"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsDeciAmpsACLEAR.setStatus(
        "current"
    )

gstDstsVoltsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21907)
)
gstDstsVoltsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "dstsVoltsB"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsVoltsBCLEAR.setStatus(
        "current"
    )

gstDstsDeciAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21908)
)
gstDstsDeciAmpsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "dstsDeciAmpsB"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsDeciAmpsBCLEAR.setStatus(
        "current"
    )

gstDstsSourceAActiveCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21909)
)
gstDstsSourceAActiveCLEAR.setObjects(
      *(("GEIST-MIB-V3", "dstsSourceAActive"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsSourceAActiveCLEAR.setStatus(
        "current"
    )

gstDstsSourceBActiveCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21910)
)
gstDstsSourceBActiveCLEAR.setObjects(
      *(("GEIST-MIB-V3", "dstsSourceBActive"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsSourceBActiveCLEAR.setStatus(
        "current"
    )

gstDstsPowerStatusACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21911)
)
gstDstsPowerStatusACLEAR.setObjects(
      *(("GEIST-MIB-V3", "dstsPowerStatusA"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsPowerStatusACLEAR.setStatus(
        "current"
    )

gstDstsPowerStatusBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21912)
)
gstDstsPowerStatusBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "dstsPowerStatusB"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsPowerStatusBCLEAR.setStatus(
        "current"
    )

gstDstsSourceATempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21913)
)
gstDstsSourceATempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "dstsSourceATempC"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsSourceATempCCLEAR.setStatus(
        "current"
    )

gstDstsSourceBTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 21914)
)
gstDstsSourceBTempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "dstsSourceBTempC"),
        ("GEIST-MIB-V3", "dstsName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstDstsSourceBTempCCLEAR.setStatus(
        "current"
    )

gstCpmSensorStatusCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22005)
)
gstCpmSensorStatusCLEAR.setObjects(
      *(("GEIST-MIB-V3", "cpmSensorStatus"),
        ("GEIST-MIB-V3", "cpmSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCpmSensorStatusCLEAR.setStatus(
        "current"
    )

gstSmokeAlarmStatusCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22105)
)
gstSmokeAlarmStatusCLEAR.setObjects(
      *(("GEIST-MIB-V3", "smokeAlarmStatus"),
        ("GEIST-MIB-V3", "smokeAlarmName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSmokeAlarmStatusCLEAR.setStatus(
        "current"
    )

gstNeg48VdcSensorVoltageCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22205)
)
gstNeg48VdcSensorVoltageCLEAR.setObjects(
      *(("GEIST-MIB-V3", "neg48VdcSensorVoltage"),
        ("GEIST-MIB-V3", "neg48VdcSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstNeg48VdcSensorVoltageCLEAR.setStatus(
        "current"
    )

gstPos30VdcSensorVoltageCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22305)
)
gstPos30VdcSensorVoltageCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pos30VdcSensorVoltage"),
        ("GEIST-MIB-V3", "pos30VdcSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPos30VdcSensorVoltageCLEAR.setStatus(
        "current"
    )

gstAnalogSensorAnalogCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22405)
)
gstAnalogSensorAnalogCLEAR.setObjects(
      *(("GEIST-MIB-V3", "analogSensorAnalog"),
        ("GEIST-MIB-V3", "analogSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAnalogSensorAnalogCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECkWattHrsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22505)
)
gstCtrl3ChIECkWattHrsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECkWattHrsA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECkWattHrsACLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECVoltsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22506)
)
gstCtrl3ChIECVoltsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECVoltsA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltsACLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECVoltPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22507)
)
gstCtrl3ChIECVoltPeakACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECVoltPeakA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltPeakACLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECDeciAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22508)
)
gstCtrl3ChIECDeciAmpsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECDeciAmpsA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsACLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECDeciAmpsPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22509)
)
gstCtrl3ChIECDeciAmpsPeakACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECDeciAmpsPeakA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsPeakACLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECRealPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22510)
)
gstCtrl3ChIECRealPowerACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECRealPowerA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerACLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECApparentPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22511)
)
gstCtrl3ChIECApparentPowerACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECApparentPowerA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECApparentPowerACLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECPowerFactorACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22512)
)
gstCtrl3ChIECPowerFactorACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECPowerFactorA"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECPowerFactorACLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECkWattHrsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22513)
)
gstCtrl3ChIECkWattHrsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECkWattHrsB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECkWattHrsBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECVoltsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22514)
)
gstCtrl3ChIECVoltsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECVoltsB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltsBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECVoltPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22515)
)
gstCtrl3ChIECVoltPeakBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECVoltPeakB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltPeakBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECDeciAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22516)
)
gstCtrl3ChIECDeciAmpsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECDeciAmpsB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECDeciAmpsPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22517)
)
gstCtrl3ChIECDeciAmpsPeakBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECDeciAmpsPeakB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsPeakBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECRealPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22518)
)
gstCtrl3ChIECRealPowerBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECRealPowerB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECApparentPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22519)
)
gstCtrl3ChIECApparentPowerBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECApparentPowerB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECApparentPowerBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECPowerFactorBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22520)
)
gstCtrl3ChIECPowerFactorBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECPowerFactorB"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECPowerFactorBCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECkWattHrsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22521)
)
gstCtrl3ChIECkWattHrsCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECkWattHrsC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECkWattHrsCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECVoltsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22522)
)
gstCtrl3ChIECVoltsCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECVoltsC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltsCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECVoltPeakCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22523)
)
gstCtrl3ChIECVoltPeakCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECVoltPeakC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECVoltPeakCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECDeciAmpsCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22524)
)
gstCtrl3ChIECDeciAmpsCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECDeciAmpsC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECDeciAmpsPeakCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22525)
)
gstCtrl3ChIECDeciAmpsPeakCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECDeciAmpsPeakC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECDeciAmpsPeakCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECRealPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22526)
)
gstCtrl3ChIECRealPowerCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECRealPowerC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECApparentPowerCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22527)
)
gstCtrl3ChIECApparentPowerCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECApparentPowerC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECApparentPowerCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECPowerFactorCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22528)
)
gstCtrl3ChIECPowerFactorCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECPowerFactorC"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECPowerFactorCCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECkWattHrsTotalCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22529)
)
gstCtrl3ChIECkWattHrsTotalCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECkWattHrsTotal"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECkWattHrsTotalCLEAR.setStatus(
        "current"
    )

gstCtrl3ChIECRealPowerTotalCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22530)
)
gstCtrl3ChIECRealPowerTotalCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl3ChIECRealPowerTotal"),
        ("GEIST-MIB-V3", "ctrl3ChIECName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl3ChIECRealPowerTotalCLEAR.setStatus(
        "current"
    )

gstClimateRelayTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22605)
)
gstClimateRelayTempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateRelayTempC"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayTempCCLEAR.setStatus(
        "current"
    )

gstClimateRelayTempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22606)
)
gstClimateRelayTempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateRelayTempF"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayTempFCLEAR.setStatus(
        "current"
    )

gstClimateRelayIO1CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22607)
)
gstClimateRelayIO1CLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateRelayIO1"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayIO1CLEAR.setStatus(
        "current"
    )

gstClimateRelayIO2CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22608)
)
gstClimateRelayIO2CLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateRelayIO2"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayIO2CLEAR.setStatus(
        "current"
    )

gstClimateRelayIO3CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22609)
)
gstClimateRelayIO3CLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateRelayIO3"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayIO3CLEAR.setStatus(
        "current"
    )

gstClimateRelayIO4CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22610)
)
gstClimateRelayIO4CLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateRelayIO4"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayIO4CLEAR.setStatus(
        "current"
    )

gstClimateRelayIO5CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22611)
)
gstClimateRelayIO5CLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateRelayIO5"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayIO5CLEAR.setStatus(
        "current"
    )

gstClimateRelayIO6CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22612)
)
gstClimateRelayIO6CLEAR.setObjects(
      *(("GEIST-MIB-V3", "climateRelayIO6"),
        ("GEIST-MIB-V3", "climateRelayName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstClimateRelayIO6CLEAR.setStatus(
        "current"
    )

gstAirSpeedSwitchSensorAirSpeedCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 22805)
)
gstAirSpeedSwitchSensorAirSpeedCLEAR.setObjects(
      *(("GEIST-MIB-V3", "airSpeedSwitchSensorAirSpeed"),
        ("GEIST-MIB-V3", "airSpeedSwitchSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstAirSpeedSwitchSensorAirSpeedCLEAR.setStatus(
        "current"
    )

gstIoExpanderIO1CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23037)
)
gstIoExpanderIO1CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO1"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO1CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO2CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23038)
)
gstIoExpanderIO2CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO2"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO2CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO3CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23039)
)
gstIoExpanderIO3CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO3"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO3CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO4CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23040)
)
gstIoExpanderIO4CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO4"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO4CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO5CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23041)
)
gstIoExpanderIO5CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO5"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO5CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO6CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23042)
)
gstIoExpanderIO6CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO6"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO6CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO7CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23043)
)
gstIoExpanderIO7CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO7"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO7CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO8CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23044)
)
gstIoExpanderIO8CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO8"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO8CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO9CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23045)
)
gstIoExpanderIO9CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO9"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO9CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO10CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23046)
)
gstIoExpanderIO10CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO10"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO10CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO11CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23047)
)
gstIoExpanderIO11CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO11"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO11CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO12CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23048)
)
gstIoExpanderIO12CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO12"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO12CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO13CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23049)
)
gstIoExpanderIO13CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO13"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO13CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO14CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23050)
)
gstIoExpanderIO14CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO14"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO14CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO15CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23051)
)
gstIoExpanderIO15CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO15"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO15CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO16CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23052)
)
gstIoExpanderIO16CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO16"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO16CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO17CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23053)
)
gstIoExpanderIO17CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO17"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO17CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO18CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23054)
)
gstIoExpanderIO18CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO18"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO18CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO19CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23055)
)
gstIoExpanderIO19CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO19"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO19CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO20CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23056)
)
gstIoExpanderIO20CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO20"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO20CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO21CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23057)
)
gstIoExpanderIO21CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO21"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO21CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO22CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23058)
)
gstIoExpanderIO22CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO22"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO22CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO23CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23059)
)
gstIoExpanderIO23CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO23"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO23CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO24CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23060)
)
gstIoExpanderIO24CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO24"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO24CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO25CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23061)
)
gstIoExpanderIO25CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO25"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO25CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO26CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23062)
)
gstIoExpanderIO26CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO26"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO26CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO27CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23063)
)
gstIoExpanderIO27CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO27"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO27CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO28CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23064)
)
gstIoExpanderIO28CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO28"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO28CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO29CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23065)
)
gstIoExpanderIO29CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO29"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO29CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO30CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23066)
)
gstIoExpanderIO30CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO30"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO30CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO31CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23067)
)
gstIoExpanderIO31CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO31"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO31CLEAR.setStatus(
        "current"
    )

gstIoExpanderIO32CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23068)
)
gstIoExpanderIO32CLEAR.setObjects(
      *(("GEIST-MIB-V3", "ioExpanderIO32"),
        ("GEIST-MIB-V3", "ioExpanderName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstIoExpanderIO32CLEAR.setStatus(
        "current"
    )

gstT3hdSensorIntTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23106)
)
gstT3hdSensorIntTempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorIntTempC"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorIntTempCCLEAR.setStatus(
        "current"
    )

gstT3hdSensorIntTempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23107)
)
gstT3hdSensorIntTempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorIntTempF"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorIntTempFCLEAR.setStatus(
        "current"
    )

gstT3hdSensorIntHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23108)
)
gstT3hdSensorIntHumidityCLEAR.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorIntHumidity"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorIntHumidityCLEAR.setStatus(
        "current"
    )

gstT3hdSensorIntDewPointCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23109)
)
gstT3hdSensorIntDewPointCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorIntDewPointC"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorIntDewPointCCLEAR.setStatus(
        "current"
    )

gstT3hdSensorIntDewPointFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23110)
)
gstT3hdSensorIntDewPointFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorIntDewPointF"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorIntDewPointFCLEAR.setStatus(
        "current"
    )

gstT3hdSensorExt1TempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23113)
)
gstT3hdSensorExt1TempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorExt1TempC"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorExt1TempCCLEAR.setStatus(
        "current"
    )

gstT3hdSensorExt1TempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23114)
)
gstT3hdSensorExt1TempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorExt1TempF"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorExt1TempFCLEAR.setStatus(
        "current"
    )

gstT3hdSensorExt2TempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23117)
)
gstT3hdSensorExt2TempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorExt2TempC"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorExt2TempCCLEAR.setStatus(
        "current"
    )

gstT3hdSensorExt2TempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23118)
)
gstT3hdSensorExt2TempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "t3hdSensorExt2TempF"),
        ("GEIST-MIB-V3", "t3hdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstT3hdSensorExt2TempFCLEAR.setStatus(
        "current"
    )

gstThdSensorTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23205)
)
gstThdSensorTempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "thdSensorTempC"),
        ("GEIST-MIB-V3", "thdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstThdSensorTempCCLEAR.setStatus(
        "current"
    )

gstThdSensorTempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23206)
)
gstThdSensorTempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "thdSensorTempF"),
        ("GEIST-MIB-V3", "thdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstThdSensorTempFCLEAR.setStatus(
        "current"
    )

gstThdSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23207)
)
gstThdSensorHumidityCLEAR.setObjects(
      *(("GEIST-MIB-V3", "thdSensorHumidity"),
        ("GEIST-MIB-V3", "thdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstThdSensorHumidityCLEAR.setStatus(
        "current"
    )

gstThdSensorDewPointCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23208)
)
gstThdSensorDewPointCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "thdSensorDewPointC"),
        ("GEIST-MIB-V3", "thdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstThdSensorDewPointCCLEAR.setStatus(
        "current"
    )

gstThdSensorDewPointFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23209)
)
gstThdSensorDewPointFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "thdSensorDewPointF"),
        ("GEIST-MIB-V3", "thdSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstThdSensorDewPointFCLEAR.setStatus(
        "current"
    )

gstPos60VdcSensorVoltageCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23305)
)
gstPos60VdcSensorVoltageCLEAR.setObjects(
      *(("GEIST-MIB-V3", "pos60VdcSensorVoltage"),
        ("GEIST-MIB-V3", "pos60VdcSensorName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPos60VdcSensorVoltageCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotkWattHrsTotCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23405)
)
gstCtrl2CirTotkWattHrsTotCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotkWattHrsTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotkWattHrsTotCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotVoltsTotCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23406)
)
gstCtrl2CirTotVoltsTotCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotVoltsTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotVoltsTotCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotVoltPeakTotCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23407)
)
gstCtrl2CirTotVoltPeakTotCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotVoltPeakTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotVoltPeakTotCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotDeciAmpsTotCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23408)
)
gstCtrl2CirTotDeciAmpsTotCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotDeciAmpsTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotDeciAmpsTotCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotDeciAmpsPeakTotCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23409)
)
gstCtrl2CirTotDeciAmpsPeakTotCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotDeciAmpsPeakTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotDeciAmpsPeakTotCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotRealPowerTotCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23410)
)
gstCtrl2CirTotRealPowerTotCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotRealPowerTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotRealPowerTotCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotApparentPowerTotCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23411)
)
gstCtrl2CirTotApparentPowerTotCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotApparentPowerTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotApparentPowerTotCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotPowerFactorTotCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23412)
)
gstCtrl2CirTotPowerFactorTotCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotPowerFactorTot"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotPowerFactorTotCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotkWattHrsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23413)
)
gstCtrl2CirTotkWattHrsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotkWattHrsA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotkWattHrsACLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotVoltsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23414)
)
gstCtrl2CirTotVoltsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotVoltsA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotVoltsACLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotVoltPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23415)
)
gstCtrl2CirTotVoltPeakACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotVoltPeakA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotVoltPeakACLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotDeciAmpsACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23416)
)
gstCtrl2CirTotDeciAmpsACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotDeciAmpsA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotDeciAmpsACLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotDeciAmpsPeakACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23417)
)
gstCtrl2CirTotDeciAmpsPeakACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotDeciAmpsPeakA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotDeciAmpsPeakACLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotRealPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23418)
)
gstCtrl2CirTotRealPowerACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotRealPowerA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotRealPowerACLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotApparentPowerACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23419)
)
gstCtrl2CirTotApparentPowerACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotApparentPowerA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotApparentPowerACLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotPowerFactorACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23420)
)
gstCtrl2CirTotPowerFactorACLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotPowerFactorA"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotPowerFactorACLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotkWattHrsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23421)
)
gstCtrl2CirTotkWattHrsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotkWattHrsB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotkWattHrsBCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotVoltsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23422)
)
gstCtrl2CirTotVoltsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotVoltsB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotVoltsBCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotVoltPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23423)
)
gstCtrl2CirTotVoltPeakBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotVoltPeakB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotVoltPeakBCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotDeciAmpsBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23424)
)
gstCtrl2CirTotDeciAmpsBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotDeciAmpsB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotDeciAmpsBCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotDeciAmpsPeakBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23425)
)
gstCtrl2CirTotDeciAmpsPeakBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotDeciAmpsPeakB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotDeciAmpsPeakBCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotRealPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23426)
)
gstCtrl2CirTotRealPowerBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotRealPowerB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotRealPowerBCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotApparentPowerBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23427)
)
gstCtrl2CirTotApparentPowerBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotApparentPowerB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotApparentPowerBCLEAR.setStatus(
        "current"
    )

gstCtrl2CirTotPowerFactorBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23428)
)
gstCtrl2CirTotPowerFactorBCLEAR.setObjects(
      *(("GEIST-MIB-V3", "ctrl2CirTotPowerFactorB"),
        ("GEIST-MIB-V3", "ctrl2CirTotName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstCtrl2CirTotPowerFactorBCLEAR.setStatus(
        "current"
    )

gstSc10ControlModeCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23505)
)
gstSc10ControlModeCLEAR.setObjects(
      *(("GEIST-MIB-V3", "sc10ControlMode"),
        ("GEIST-MIB-V3", "sc10Name"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSc10ControlModeCLEAR.setStatus(
        "current"
    )

gstSc10SetpointCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23506)
)
gstSc10SetpointCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "sc10SetpointC"),
        ("GEIST-MIB-V3", "sc10Name"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSc10SetpointCCLEAR.setStatus(
        "current"
    )

gstSc10SetpointFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23507)
)
gstSc10SetpointFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "sc10SetpointF"),
        ("GEIST-MIB-V3", "sc10Name"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSc10SetpointFCLEAR.setStatus(
        "current"
    )

gstSc10TempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23508)
)
gstSc10TempCCLEAR.setObjects(
      *(("GEIST-MIB-V3", "sc10TempC"),
        ("GEIST-MIB-V3", "sc10Name"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSc10TempCCLEAR.setStatus(
        "current"
    )

gstSc10TempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23509)
)
gstSc10TempFCLEAR.setObjects(
      *(("GEIST-MIB-V3", "sc10TempF"),
        ("GEIST-MIB-V3", "sc10Name"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "temperaturePrecision"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSc10TempFCLEAR.setStatus(
        "current"
    )

gstSc10CapacityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 23510)
)
gstSc10CapacityCLEAR.setObjects(
      *(("GEIST-MIB-V3", "sc10Capacity"),
        ("GEIST-MIB-V3", "sc10Name"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstSc10CapacityCLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps1NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129153)
)
gstPowerDMDeciAmps1NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps1"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps1NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps2NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129154)
)
gstPowerDMDeciAmps2NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps2"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps2NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps3NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129155)
)
gstPowerDMDeciAmps3NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps3"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps3NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps4NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129156)
)
gstPowerDMDeciAmps4NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps4"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps4NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps5NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129157)
)
gstPowerDMDeciAmps5NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps5"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps5NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps6NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129158)
)
gstPowerDMDeciAmps6NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps6"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps6NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps7NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129159)
)
gstPowerDMDeciAmps7NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps7"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps7NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps8NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129160)
)
gstPowerDMDeciAmps8NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps8"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps8NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps9NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129161)
)
gstPowerDMDeciAmps9NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps9"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps9NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps10NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129162)
)
gstPowerDMDeciAmps10NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps10"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps10NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps11NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129163)
)
gstPowerDMDeciAmps11NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps11"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps11NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps12NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129164)
)
gstPowerDMDeciAmps12NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps12"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps12NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps13NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129165)
)
gstPowerDMDeciAmps13NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps13"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps13NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps14NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129166)
)
gstPowerDMDeciAmps14NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps14"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps14NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps15NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129167)
)
gstPowerDMDeciAmps15NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps15"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps15NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps16NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129168)
)
gstPowerDMDeciAmps16NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps16"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps16NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps17NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129169)
)
gstPowerDMDeciAmps17NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps17"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps17NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps18NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129170)
)
gstPowerDMDeciAmps18NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps18"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps18NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps19NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129171)
)
gstPowerDMDeciAmps19NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps19"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps19NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps20NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129172)
)
gstPowerDMDeciAmps20NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps20"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps20NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps21NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129173)
)
gstPowerDMDeciAmps21NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps21"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps21NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps22NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129174)
)
gstPowerDMDeciAmps22NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps22"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps22NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps23NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129175)
)
gstPowerDMDeciAmps23NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps23"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps23NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps24NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129176)
)
gstPowerDMDeciAmps24NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps24"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps24NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps25NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129177)
)
gstPowerDMDeciAmps25NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps25"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps25NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps26NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129178)
)
gstPowerDMDeciAmps26NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps26"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps26NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps27NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129179)
)
gstPowerDMDeciAmps27NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps27"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps27NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps28NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129180)
)
gstPowerDMDeciAmps28NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps28"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps28NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps29NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129181)
)
gstPowerDMDeciAmps29NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps29"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps29NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps30NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129182)
)
gstPowerDMDeciAmps30NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps30"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps30NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps31NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129183)
)
gstPowerDMDeciAmps31NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps31"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps31NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps32NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129184)
)
gstPowerDMDeciAmps32NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps32"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps32NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps33NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129185)
)
gstPowerDMDeciAmps33NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps33"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps33NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps34NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129186)
)
gstPowerDMDeciAmps34NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps34"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps34NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps35NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129187)
)
gstPowerDMDeciAmps35NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps35"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps35NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps36NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129188)
)
gstPowerDMDeciAmps36NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps36"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps36NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps37NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129189)
)
gstPowerDMDeciAmps37NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps37"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps37NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps38NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129190)
)
gstPowerDMDeciAmps38NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps38"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps38NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps39NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129191)
)
gstPowerDMDeciAmps39NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps39"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps39NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps40NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129192)
)
gstPowerDMDeciAmps40NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps40"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps40NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps41NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129193)
)
gstPowerDMDeciAmps41NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps41"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps41NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps42NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129194)
)
gstPowerDMDeciAmps42NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps42"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps42NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps43NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129195)
)
gstPowerDMDeciAmps43NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps43"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps43NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps44NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129196)
)
gstPowerDMDeciAmps44NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps44"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps44NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps45NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129197)
)
gstPowerDMDeciAmps45NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps45"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps45NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps46NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129198)
)
gstPowerDMDeciAmps46NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps46"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps46NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps47NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129199)
)
gstPowerDMDeciAmps47NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps47"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps47NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps48NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 129200)
)
gstPowerDMDeciAmps48NOTIFY.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps48"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps48NOTIFY.setStatus(
        "current"
    )

gstPowerDMDeciAmps1CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139153)
)
gstPowerDMDeciAmps1CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps1"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps1CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps2CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139154)
)
gstPowerDMDeciAmps2CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps2"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps2CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps3CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139155)
)
gstPowerDMDeciAmps3CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps3"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps3CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps4CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139156)
)
gstPowerDMDeciAmps4CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps4"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps4CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps5CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139157)
)
gstPowerDMDeciAmps5CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps5"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps5CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps6CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139158)
)
gstPowerDMDeciAmps6CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps6"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps6CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps7CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139159)
)
gstPowerDMDeciAmps7CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps7"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps7CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps8CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139160)
)
gstPowerDMDeciAmps8CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps8"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps8CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps9CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139161)
)
gstPowerDMDeciAmps9CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps9"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps9CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps10CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139162)
)
gstPowerDMDeciAmps10CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps10"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps10CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps11CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139163)
)
gstPowerDMDeciAmps11CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps11"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps11CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps12CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139164)
)
gstPowerDMDeciAmps12CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps12"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps12CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps13CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139165)
)
gstPowerDMDeciAmps13CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps13"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps13CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps14CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139166)
)
gstPowerDMDeciAmps14CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps14"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps14CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps15CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139167)
)
gstPowerDMDeciAmps15CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps15"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps15CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps16CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139168)
)
gstPowerDMDeciAmps16CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps16"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps16CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps17CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139169)
)
gstPowerDMDeciAmps17CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps17"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps17CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps18CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139170)
)
gstPowerDMDeciAmps18CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps18"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps18CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps19CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139171)
)
gstPowerDMDeciAmps19CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps19"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps19CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps20CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139172)
)
gstPowerDMDeciAmps20CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps20"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps20CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps21CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139173)
)
gstPowerDMDeciAmps21CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps21"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps21CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps22CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139174)
)
gstPowerDMDeciAmps22CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps22"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps22CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps23CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139175)
)
gstPowerDMDeciAmps23CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps23"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps23CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps24CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139176)
)
gstPowerDMDeciAmps24CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps24"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps24CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps25CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139177)
)
gstPowerDMDeciAmps25CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps25"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps25CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps26CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139178)
)
gstPowerDMDeciAmps26CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps26"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps26CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps27CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139179)
)
gstPowerDMDeciAmps27CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps27"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps27CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps28CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139180)
)
gstPowerDMDeciAmps28CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps28"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps28CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps29CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139181)
)
gstPowerDMDeciAmps29CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps29"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps29CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps30CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139182)
)
gstPowerDMDeciAmps30CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps30"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps30CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps31CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139183)
)
gstPowerDMDeciAmps31CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps31"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps31CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps32CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139184)
)
gstPowerDMDeciAmps32CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps32"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps32CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps33CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139185)
)
gstPowerDMDeciAmps33CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps33"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps33CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps34CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139186)
)
gstPowerDMDeciAmps34CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps34"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps34CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps35CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139187)
)
gstPowerDMDeciAmps35CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps35"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps35CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps36CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139188)
)
gstPowerDMDeciAmps36CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps36"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps36CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps37CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139189)
)
gstPowerDMDeciAmps37CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps37"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps37CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps38CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139190)
)
gstPowerDMDeciAmps38CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps38"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps38CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps39CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139191)
)
gstPowerDMDeciAmps39CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps39"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps39CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps40CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139192)
)
gstPowerDMDeciAmps40CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps40"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps40CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps41CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139193)
)
gstPowerDMDeciAmps41CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps41"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps41CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps42CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139194)
)
gstPowerDMDeciAmps42CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps42"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps42CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps43CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139195)
)
gstPowerDMDeciAmps43CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps43"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps43CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps44CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139196)
)
gstPowerDMDeciAmps44CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps44"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps44CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps45CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139197)
)
gstPowerDMDeciAmps45CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps45"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps45CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps46CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139198)
)
gstPowerDMDeciAmps46CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps46"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps46CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps47CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139199)
)
gstPowerDMDeciAmps47CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps47"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps47CLEAR.setStatus(
        "current"
    )

gstPowerDMDeciAmps48CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 21239, 2, 32767, 0, 139200)
)
gstPowerDMDeciAmps48CLEAR.setObjects(
      *(("GEIST-MIB-V3", "powerDMDeciAmps48"),
        ("GEIST-MIB-V3", "powerDMName"),
        ("GEIST-MIB-V3", "productFriendlyName"),
        ("GEIST-MIB-V3", "alarmTripType"),
        ("GEIST-MIB-V3", "alarmTrigger"),
        ("GEIST-MIB-V3", "alarmInstance"))
)
if mibBuilder.loadTexts:
    gstPowerDMDeciAmps48CLEAR.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GEIST-MIB-V3",
    **{"geist": geist,
       "geistV3": geistV3,
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
       "ctrl3ChDELTACount": ctrl3ChDELTACount,
       "doorSensorCount": doorSensorCount,
       "waterSensorCount": waterSensorCount,
       "currentSensorCount": currentSensorCount,
       "millivoltSensorCount": millivoltSensorCount,
       "power3ChSensorCount": power3ChSensorCount,
       "outletCount": outletCount,
       "vsfcCount": vsfcCount,
       "ctrl3ChCount": ctrl3ChCount,
       "ctrlGrpAmpsCount": ctrlGrpAmpsCount,
       "ctrlOutletCount": ctrlOutletCount,
       "dewpointSensorCount": dewpointSensorCount,
       "digitalSensorCount": digitalSensorCount,
       "dstsSensorCount": dstsSensorCount,
       "cpmSensorCount": cpmSensorCount,
       "smokeAlarmSensorCount": smokeAlarmSensorCount,
       "neg48VdcSensorCount": neg48VdcSensorCount,
       "pos30VdcSensorCount": pos30VdcSensorCount,
       "analogSensorCount": analogSensorCount,
       "ctrl3ChIECCount": ctrl3ChIECCount,
       "climateRelayCount": climateRelayCount,
       "ctrlRelayCount": ctrlRelayCount,
       "airSpeedSwitchSensorCount": airSpeedSwitchSensorCount,
       "powerDMCount": powerDMCount,
       "ioExpanderCount": ioExpanderCount,
       "t3hdSensorCount": t3hdSensorCount,
       "thdSensorCount": thdSensorCount,
       "pos60VdcSensorCount": pos60VdcSensorCount,
       "ctrl2CirTotCount": ctrl2CirTotCount,
       "sc10Count": sc10Count,
       "temperaturePrecision": temperaturePrecision,
       "alarmTrigger": alarmTrigger,
       "alarmInstance": alarmInstance,
       "climateTable": climateTable,
       "climateEntry": climateEntry,
       "climateIndex": climateIndex,
       "climateSerial": climateSerial,
       "climateName": climateName,
       "climateAvail": climateAvail,
       "climateTempC": climateTempC,
       "climateTempF": climateTempF,
       "climateHumidity": climateHumidity,
       "climateLight": climateLight,
       "climateAirflow": climateAirflow,
       "climateSound": climateSound,
       "climateIO1": climateIO1,
       "climateIO2": climateIO2,
       "climateIO3": climateIO3,
       "climateVolts": climateVolts,
       "climateVoltPeak": climateVoltPeak,
       "climateDeciAmpsA": climateDeciAmpsA,
       "climateDeciAmpPeakA": climateDeciAmpPeakA,
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
       "climateDewPointC": climateDewPointC,
       "climateDewPointF": climateDewPointF,
       "powMonTable": powMonTable,
       "powMonEntry": powMonEntry,
       "powMonIndex": powMonIndex,
       "powMonSerial": powMonSerial,
       "powMonName": powMonName,
       "powMonAvail": powMonAvail,
       "powMonkWattHrs": powMonkWattHrs,
       "powMonVolts": powMonVolts,
       "powMonVoltMax": powMonVoltMax,
       "powMonVoltMin": powMonVoltMin,
       "powMonVoltPeak": powMonVoltPeak,
       "powMonDeciAmps": powMonDeciAmps,
       "powMonRealPower": powMonRealPower,
       "powMonApparentPower": powMonApparentPower,
       "powMonPowerFactor": powMonPowerFactor,
       "powMonOutlet1": powMonOutlet1,
       "powMonOutlet2": powMonOutlet2,
       "powMonOutlet1StatusTime": powMonOutlet1StatusTime,
       "powMonOutlet2StatusTime": powMonOutlet2StatusTime,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorIndex": tempSensorIndex,
       "tempSensorSerial": tempSensorSerial,
       "tempSensorName": tempSensorName,
       "tempSensorAvail": tempSensorAvail,
       "tempSensorTempC": tempSensorTempC,
       "tempSensorTempF": tempSensorTempF,
       "airFlowSensorTable": airFlowSensorTable,
       "airFlowSensorEntry": airFlowSensorEntry,
       "airFlowSensorIndex": airFlowSensorIndex,
       "airFlowSensorSerial": airFlowSensorSerial,
       "airFlowSensorName": airFlowSensorName,
       "airFlowSensorAvail": airFlowSensorAvail,
       "airFlowSensorTempC": airFlowSensorTempC,
       "airFlowSensorTempF": airFlowSensorTempF,
       "airFlowSensorFlow": airFlowSensorFlow,
       "airFlowSensorHumidity": airFlowSensorHumidity,
       "airFlowSensorDewPointC": airFlowSensorDewPointC,
       "airFlowSensorDewPointF": airFlowSensorDewPointF,
       "ctrl3ChDELTATable": ctrl3ChDELTATable,
       "ctrl3ChDELTAEntry": ctrl3ChDELTAEntry,
       "ctrl3ChDELTAIndex": ctrl3ChDELTAIndex,
       "ctrl3ChDELTASerial": ctrl3ChDELTASerial,
       "ctrl3ChDELTAName": ctrl3ChDELTAName,
       "ctrl3ChDELTAAvail": ctrl3ChDELTAAvail,
       "ctrl3ChDELTAPowerChCount": ctrl3ChDELTAPowerChCount,
       "ctrl3ChDELTADeciAmpsA": ctrl3ChDELTADeciAmpsA,
       "ctrl3ChDELTADeciAmpsB": ctrl3ChDELTADeciAmpsB,
       "ctrl3ChDELTADeciAmpsC": ctrl3ChDELTADeciAmpsC,
       "ctrl3ChDELTAkWattHrsTotal": ctrl3ChDELTAkWattHrsTotal,
       "ctrl3ChDELTARealPowerTotal": ctrl3ChDELTARealPowerTotal,
       "ctrl3ChDELTAkWattHrsAB": ctrl3ChDELTAkWattHrsAB,
       "ctrl3ChDELTAVoltsAB": ctrl3ChDELTAVoltsAB,
       "ctrl3ChDELTAVoltPeakAB": ctrl3ChDELTAVoltPeakAB,
       "ctrl3ChDELTARealPowerAB": ctrl3ChDELTARealPowerAB,
       "ctrl3ChDELTAApparentPowerAB": ctrl3ChDELTAApparentPowerAB,
       "ctrl3ChDELTAPowerFactorAB": ctrl3ChDELTAPowerFactorAB,
       "ctrl3ChDELTAkWattHrsBC": ctrl3ChDELTAkWattHrsBC,
       "ctrl3ChDELTAVoltsBC": ctrl3ChDELTAVoltsBC,
       "ctrl3ChDELTAVoltPeakBC": ctrl3ChDELTAVoltPeakBC,
       "ctrl3ChDELTARealPowerBC": ctrl3ChDELTARealPowerBC,
       "ctrl3ChDELTAApparentPowerBC": ctrl3ChDELTAApparentPowerBC,
       "ctrl3ChDELTAPowerFactorBC": ctrl3ChDELTAPowerFactorBC,
       "ctrl3ChDELTAkWattHrsCA": ctrl3ChDELTAkWattHrsCA,
       "ctrl3ChDELTAVoltsCA": ctrl3ChDELTAVoltsCA,
       "ctrl3ChDELTAVoltPeakCA": ctrl3ChDELTAVoltPeakCA,
       "ctrl3ChDELTARealPowerCA": ctrl3ChDELTARealPowerCA,
       "ctrl3ChDELTAApparentPowerCA": ctrl3ChDELTAApparentPowerCA,
       "ctrl3ChDELTAPowerFactorCA": ctrl3ChDELTAPowerFactorCA,
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
       "pow3ChTable": pow3ChTable,
       "pow3ChEntry": pow3ChEntry,
       "pow3ChIndex": pow3ChIndex,
       "pow3ChSerial": pow3ChSerial,
       "pow3ChName": pow3ChName,
       "pow3ChAvail": pow3ChAvail,
       "pow3ChkWattHrsA": pow3ChkWattHrsA,
       "pow3ChVoltsA": pow3ChVoltsA,
       "pow3ChVoltMaxA": pow3ChVoltMaxA,
       "pow3ChVoltMinA": pow3ChVoltMinA,
       "pow3ChVoltPeakA": pow3ChVoltPeakA,
       "pow3ChDeciAmpsA": pow3ChDeciAmpsA,
       "pow3ChRealPowerA": pow3ChRealPowerA,
       "pow3ChApparentPowerA": pow3ChApparentPowerA,
       "pow3ChPowerFactorA": pow3ChPowerFactorA,
       "pow3ChkWattHrsB": pow3ChkWattHrsB,
       "pow3ChVoltsB": pow3ChVoltsB,
       "pow3ChVoltMaxB": pow3ChVoltMaxB,
       "pow3ChVoltMinB": pow3ChVoltMinB,
       "pow3ChVoltPeakB": pow3ChVoltPeakB,
       "pow3ChDeciAmpsB": pow3ChDeciAmpsB,
       "pow3ChRealPowerB": pow3ChRealPowerB,
       "pow3ChApparentPowerB": pow3ChApparentPowerB,
       "pow3ChPowerFactorB": pow3ChPowerFactorB,
       "pow3ChkWattHrsC": pow3ChkWattHrsC,
       "pow3ChVoltsC": pow3ChVoltsC,
       "pow3ChVoltMaxC": pow3ChVoltMaxC,
       "pow3ChVoltMinC": pow3ChVoltMinC,
       "pow3ChVoltPeakC": pow3ChVoltPeakC,
       "pow3ChDeciAmpsC": pow3ChDeciAmpsC,
       "pow3ChRealPowerC": pow3ChRealPowerC,
       "pow3ChApparentPowerC": pow3ChApparentPowerC,
       "pow3ChPowerFactorC": pow3ChPowerFactorC,
       "pow3ChkWattHrsTotal": pow3ChkWattHrsTotal,
       "pow3ChRealPowerTotal": pow3ChRealPowerTotal,
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
       "vsfcSetPointF": vsfcSetPointF,
       "vsfcFanSpeed": vsfcFanSpeed,
       "vsfcIntTempC": vsfcIntTempC,
       "vsfcIntTempF": vsfcIntTempF,
       "vsfcExt1TempC": vsfcExt1TempC,
       "vsfcExt1TempF": vsfcExt1TempF,
       "vsfcExt2TempC": vsfcExt2TempC,
       "vsfcExt2TempF": vsfcExt2TempF,
       "vsfcExt3TempC": vsfcExt3TempC,
       "vsfcExt3TempF": vsfcExt3TempF,
       "vsfcExt4TempC": vsfcExt4TempC,
       "vsfcExt4TempF": vsfcExt4TempF,
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
       "ctrlGrpAmpsG": ctrlGrpAmpsG,
       "ctrlGrpAmpsH": ctrlGrpAmpsH,
       "ctrlGrpAmpsAVolts": ctrlGrpAmpsAVolts,
       "ctrlGrpAmpsBVolts": ctrlGrpAmpsBVolts,
       "ctrlGrpAmpsCVolts": ctrlGrpAmpsCVolts,
       "ctrlGrpAmpsDVolts": ctrlGrpAmpsDVolts,
       "ctrlGrpAmpsEVolts": ctrlGrpAmpsEVolts,
       "ctrlGrpAmpsFVolts": ctrlGrpAmpsFVolts,
       "ctrlGrpAmpsGVolts": ctrlGrpAmpsGVolts,
       "ctrlGrpAmpsHVolts": ctrlGrpAmpsHVolts,
       "ctrlGrpAmpsI": ctrlGrpAmpsI,
       "ctrlGrpAmpsJ": ctrlGrpAmpsJ,
       "ctrlGrpAmpsK": ctrlGrpAmpsK,
       "ctrlGrpAmpsL": ctrlGrpAmpsL,
       "ctrlGrpAmpsM": ctrlGrpAmpsM,
       "ctrlGrpAmpsN": ctrlGrpAmpsN,
       "ctrlGrpAmpsO": ctrlGrpAmpsO,
       "ctrlGrpAmpsP": ctrlGrpAmpsP,
       "ctrlGrpAmpsIVolts": ctrlGrpAmpsIVolts,
       "ctrlGrpAmpsJVolts": ctrlGrpAmpsJVolts,
       "ctrlGrpAmpsKVolts": ctrlGrpAmpsKVolts,
       "ctrlGrpAmpsLVolts": ctrlGrpAmpsLVolts,
       "ctrlGrpAmpsMVolts": ctrlGrpAmpsMVolts,
       "ctrlGrpAmpsNVolts": ctrlGrpAmpsNVolts,
       "ctrlGrpAmpsOVolts": ctrlGrpAmpsOVolts,
       "ctrlGrpAmpsPVolts": ctrlGrpAmpsPVolts,
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
       "ctrlOutletRbtDuration": ctrlOutletRbtDuration,
       "ctrlOutletURL": ctrlOutletURL,
       "ctrlOutletPOAAction": ctrlOutletPOAAction,
       "ctrlOutletPOADelay": ctrlOutletPOADelay,
       "ctrlOutletkWattHrs": ctrlOutletkWattHrs,
       "ctrlOutletPower": ctrlOutletPower,
       "ctrlOutletRbtDelay": ctrlOutletRbtDelay,
       "ctrlOutletStatusTime": ctrlOutletStatusTime,
       "dewPointSensorTable": dewPointSensorTable,
       "dewPointSensorEntry": dewPointSensorEntry,
       "dewPointSensorIndex": dewPointSensorIndex,
       "dewPointSensorSerial": dewPointSensorSerial,
       "dewPointSensorName": dewPointSensorName,
       "dewPointSensorAvail": dewPointSensorAvail,
       "dewPointSensorTempC": dewPointSensorTempC,
       "dewPointSensorTempF": dewPointSensorTempF,
       "dewPointSensorHumidity": dewPointSensorHumidity,
       "dewPointSensorDewPointC": dewPointSensorDewPointC,
       "dewPointSensorDewPointF": dewPointSensorDewPointF,
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
       "dstsDeciAmpsA": dstsDeciAmpsA,
       "dstsVoltsB": dstsVoltsB,
       "dstsDeciAmpsB": dstsDeciAmpsB,
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
       "ctrl3ChIECkWattHrsA": ctrl3ChIECkWattHrsA,
       "ctrl3ChIECVoltsA": ctrl3ChIECVoltsA,
       "ctrl3ChIECVoltPeakA": ctrl3ChIECVoltPeakA,
       "ctrl3ChIECDeciAmpsA": ctrl3ChIECDeciAmpsA,
       "ctrl3ChIECDeciAmpsPeakA": ctrl3ChIECDeciAmpsPeakA,
       "ctrl3ChIECRealPowerA": ctrl3ChIECRealPowerA,
       "ctrl3ChIECApparentPowerA": ctrl3ChIECApparentPowerA,
       "ctrl3ChIECPowerFactorA": ctrl3ChIECPowerFactorA,
       "ctrl3ChIECkWattHrsB": ctrl3ChIECkWattHrsB,
       "ctrl3ChIECVoltsB": ctrl3ChIECVoltsB,
       "ctrl3ChIECVoltPeakB": ctrl3ChIECVoltPeakB,
       "ctrl3ChIECDeciAmpsB": ctrl3ChIECDeciAmpsB,
       "ctrl3ChIECDeciAmpsPeakB": ctrl3ChIECDeciAmpsPeakB,
       "ctrl3ChIECRealPowerB": ctrl3ChIECRealPowerB,
       "ctrl3ChIECApparentPowerB": ctrl3ChIECApparentPowerB,
       "ctrl3ChIECPowerFactorB": ctrl3ChIECPowerFactorB,
       "ctrl3ChIECkWattHrsC": ctrl3ChIECkWattHrsC,
       "ctrl3ChIECVoltsC": ctrl3ChIECVoltsC,
       "ctrl3ChIECVoltPeakC": ctrl3ChIECVoltPeakC,
       "ctrl3ChIECDeciAmpsC": ctrl3ChIECDeciAmpsC,
       "ctrl3ChIECDeciAmpsPeakC": ctrl3ChIECDeciAmpsPeakC,
       "ctrl3ChIECRealPowerC": ctrl3ChIECRealPowerC,
       "ctrl3ChIECApparentPowerC": ctrl3ChIECApparentPowerC,
       "ctrl3ChIECPowerFactorC": ctrl3ChIECPowerFactorC,
       "ctrl3ChIECkWattHrsTotal": ctrl3ChIECkWattHrsTotal,
       "ctrl3ChIECRealPowerTotal": ctrl3ChIECRealPowerTotal,
       "climateRelayTable": climateRelayTable,
       "climateRelayEntry": climateRelayEntry,
       "climateRelayIndex": climateRelayIndex,
       "climateRelaySerial": climateRelaySerial,
       "climateRelayName": climateRelayName,
       "climateRelayAvail": climateRelayAvail,
       "climateRelayTempC": climateRelayTempC,
       "climateRelayTempF": climateRelayTempF,
       "climateRelayIO1": climateRelayIO1,
       "climateRelayIO2": climateRelayIO2,
       "climateRelayIO3": climateRelayIO3,
       "climateRelayIO4": climateRelayIO4,
       "climateRelayIO5": climateRelayIO5,
       "climateRelayIO6": climateRelayIO6,
       "ctrlRelayTable": ctrlRelayTable,
       "ctrlRelayEntry": ctrlRelayEntry,
       "ctrlRelayIndex": ctrlRelayIndex,
       "ctrlRelayName": ctrlRelayName,
       "ctrlRelayState": ctrlRelayState,
       "ctrlRelayLatchingMode": ctrlRelayLatchingMode,
       "ctrlRelayOverride": ctrlRelayOverride,
       "ctrlRelayAcknowledge": ctrlRelayAcknowledge,
       "airSpeedSwitchSensorTable": airSpeedSwitchSensorTable,
       "airSpeedSwitchSensorEntry": airSpeedSwitchSensorEntry,
       "airSpeedSwitchSensorIndex": airSpeedSwitchSensorIndex,
       "airSpeedSwitchSensorSerial": airSpeedSwitchSensorSerial,
       "airSpeedSwitchSensorName": airSpeedSwitchSensorName,
       "airSpeedSwitchSensorAvail": airSpeedSwitchSensorAvail,
       "airSpeedSwitchSensorAirSpeed": airSpeedSwitchSensorAirSpeed,
       "powerDMTable": powerDMTable,
       "powerDMEntry": powerDMEntry,
       "powerDMIndex": powerDMIndex,
       "powerDMSerial": powerDMSerial,
       "powerDMName": powerDMName,
       "powerDMAvail": powerDMAvail,
       "powerDMUnitInfoTitle": powerDMUnitInfoTitle,
       "powerDMUnitInfoVersion": powerDMUnitInfoVersion,
       "powerDMUnitInfoMainCount": powerDMUnitInfoMainCount,
       "powerDMUnitInfoAuxCount": powerDMUnitInfoAuxCount,
       "powerDMChannelName1": powerDMChannelName1,
       "powerDMChannelName2": powerDMChannelName2,
       "powerDMChannelName3": powerDMChannelName3,
       "powerDMChannelName4": powerDMChannelName4,
       "powerDMChannelName5": powerDMChannelName5,
       "powerDMChannelName6": powerDMChannelName6,
       "powerDMChannelName7": powerDMChannelName7,
       "powerDMChannelName8": powerDMChannelName8,
       "powerDMChannelName9": powerDMChannelName9,
       "powerDMChannelName10": powerDMChannelName10,
       "powerDMChannelName11": powerDMChannelName11,
       "powerDMChannelName12": powerDMChannelName12,
       "powerDMChannelName13": powerDMChannelName13,
       "powerDMChannelName14": powerDMChannelName14,
       "powerDMChannelName15": powerDMChannelName15,
       "powerDMChannelName16": powerDMChannelName16,
       "powerDMChannelName17": powerDMChannelName17,
       "powerDMChannelName18": powerDMChannelName18,
       "powerDMChannelName19": powerDMChannelName19,
       "powerDMChannelName20": powerDMChannelName20,
       "powerDMChannelName21": powerDMChannelName21,
       "powerDMChannelName22": powerDMChannelName22,
       "powerDMChannelName23": powerDMChannelName23,
       "powerDMChannelName24": powerDMChannelName24,
       "powerDMChannelName25": powerDMChannelName25,
       "powerDMChannelName26": powerDMChannelName26,
       "powerDMChannelName27": powerDMChannelName27,
       "powerDMChannelName28": powerDMChannelName28,
       "powerDMChannelName29": powerDMChannelName29,
       "powerDMChannelName30": powerDMChannelName30,
       "powerDMChannelName31": powerDMChannelName31,
       "powerDMChannelName32": powerDMChannelName32,
       "powerDMChannelName33": powerDMChannelName33,
       "powerDMChannelName34": powerDMChannelName34,
       "powerDMChannelName35": powerDMChannelName35,
       "powerDMChannelName36": powerDMChannelName36,
       "powerDMChannelName37": powerDMChannelName37,
       "powerDMChannelName38": powerDMChannelName38,
       "powerDMChannelName39": powerDMChannelName39,
       "powerDMChannelName40": powerDMChannelName40,
       "powerDMChannelName41": powerDMChannelName41,
       "powerDMChannelName42": powerDMChannelName42,
       "powerDMChannelName43": powerDMChannelName43,
       "powerDMChannelName44": powerDMChannelName44,
       "powerDMChannelName45": powerDMChannelName45,
       "powerDMChannelName46": powerDMChannelName46,
       "powerDMChannelName47": powerDMChannelName47,
       "powerDMChannelName48": powerDMChannelName48,
       "powerDMChannelFriendly1": powerDMChannelFriendly1,
       "powerDMChannelFriendly2": powerDMChannelFriendly2,
       "powerDMChannelFriendly3": powerDMChannelFriendly3,
       "powerDMChannelFriendly4": powerDMChannelFriendly4,
       "powerDMChannelFriendly5": powerDMChannelFriendly5,
       "powerDMChannelFriendly6": powerDMChannelFriendly6,
       "powerDMChannelFriendly7": powerDMChannelFriendly7,
       "powerDMChannelFriendly8": powerDMChannelFriendly8,
       "powerDMChannelFriendly9": powerDMChannelFriendly9,
       "powerDMChannelFriendly10": powerDMChannelFriendly10,
       "powerDMChannelFriendly11": powerDMChannelFriendly11,
       "powerDMChannelFriendly12": powerDMChannelFriendly12,
       "powerDMChannelFriendly13": powerDMChannelFriendly13,
       "powerDMChannelFriendly14": powerDMChannelFriendly14,
       "powerDMChannelFriendly15": powerDMChannelFriendly15,
       "powerDMChannelFriendly16": powerDMChannelFriendly16,
       "powerDMChannelFriendly17": powerDMChannelFriendly17,
       "powerDMChannelFriendly18": powerDMChannelFriendly18,
       "powerDMChannelFriendly19": powerDMChannelFriendly19,
       "powerDMChannelFriendly20": powerDMChannelFriendly20,
       "powerDMChannelFriendly21": powerDMChannelFriendly21,
       "powerDMChannelFriendly22": powerDMChannelFriendly22,
       "powerDMChannelFriendly23": powerDMChannelFriendly23,
       "powerDMChannelFriendly24": powerDMChannelFriendly24,
       "powerDMChannelFriendly25": powerDMChannelFriendly25,
       "powerDMChannelFriendly26": powerDMChannelFriendly26,
       "powerDMChannelFriendly27": powerDMChannelFriendly27,
       "powerDMChannelFriendly28": powerDMChannelFriendly28,
       "powerDMChannelFriendly29": powerDMChannelFriendly29,
       "powerDMChannelFriendly30": powerDMChannelFriendly30,
       "powerDMChannelFriendly31": powerDMChannelFriendly31,
       "powerDMChannelFriendly32": powerDMChannelFriendly32,
       "powerDMChannelFriendly33": powerDMChannelFriendly33,
       "powerDMChannelFriendly34": powerDMChannelFriendly34,
       "powerDMChannelFriendly35": powerDMChannelFriendly35,
       "powerDMChannelFriendly36": powerDMChannelFriendly36,
       "powerDMChannelFriendly37": powerDMChannelFriendly37,
       "powerDMChannelFriendly38": powerDMChannelFriendly38,
       "powerDMChannelFriendly39": powerDMChannelFriendly39,
       "powerDMChannelFriendly40": powerDMChannelFriendly40,
       "powerDMChannelFriendly41": powerDMChannelFriendly41,
       "powerDMChannelFriendly42": powerDMChannelFriendly42,
       "powerDMChannelFriendly43": powerDMChannelFriendly43,
       "powerDMChannelFriendly44": powerDMChannelFriendly44,
       "powerDMChannelFriendly45": powerDMChannelFriendly45,
       "powerDMChannelFriendly46": powerDMChannelFriendly46,
       "powerDMChannelFriendly47": powerDMChannelFriendly47,
       "powerDMChannelFriendly48": powerDMChannelFriendly48,
       "powerDMChannelGroup1": powerDMChannelGroup1,
       "powerDMChannelGroup2": powerDMChannelGroup2,
       "powerDMChannelGroup3": powerDMChannelGroup3,
       "powerDMChannelGroup4": powerDMChannelGroup4,
       "powerDMChannelGroup5": powerDMChannelGroup5,
       "powerDMChannelGroup6": powerDMChannelGroup6,
       "powerDMChannelGroup7": powerDMChannelGroup7,
       "powerDMChannelGroup8": powerDMChannelGroup8,
       "powerDMChannelGroup9": powerDMChannelGroup9,
       "powerDMChannelGroup10": powerDMChannelGroup10,
       "powerDMChannelGroup11": powerDMChannelGroup11,
       "powerDMChannelGroup12": powerDMChannelGroup12,
       "powerDMChannelGroup13": powerDMChannelGroup13,
       "powerDMChannelGroup14": powerDMChannelGroup14,
       "powerDMChannelGroup15": powerDMChannelGroup15,
       "powerDMChannelGroup16": powerDMChannelGroup16,
       "powerDMChannelGroup17": powerDMChannelGroup17,
       "powerDMChannelGroup18": powerDMChannelGroup18,
       "powerDMChannelGroup19": powerDMChannelGroup19,
       "powerDMChannelGroup20": powerDMChannelGroup20,
       "powerDMChannelGroup21": powerDMChannelGroup21,
       "powerDMChannelGroup22": powerDMChannelGroup22,
       "powerDMChannelGroup23": powerDMChannelGroup23,
       "powerDMChannelGroup24": powerDMChannelGroup24,
       "powerDMChannelGroup25": powerDMChannelGroup25,
       "powerDMChannelGroup26": powerDMChannelGroup26,
       "powerDMChannelGroup27": powerDMChannelGroup27,
       "powerDMChannelGroup28": powerDMChannelGroup28,
       "powerDMChannelGroup29": powerDMChannelGroup29,
       "powerDMChannelGroup30": powerDMChannelGroup30,
       "powerDMChannelGroup31": powerDMChannelGroup31,
       "powerDMChannelGroup32": powerDMChannelGroup32,
       "powerDMChannelGroup33": powerDMChannelGroup33,
       "powerDMChannelGroup34": powerDMChannelGroup34,
       "powerDMChannelGroup35": powerDMChannelGroup35,
       "powerDMChannelGroup36": powerDMChannelGroup36,
       "powerDMChannelGroup37": powerDMChannelGroup37,
       "powerDMChannelGroup38": powerDMChannelGroup38,
       "powerDMChannelGroup39": powerDMChannelGroup39,
       "powerDMChannelGroup40": powerDMChannelGroup40,
       "powerDMChannelGroup41": powerDMChannelGroup41,
       "powerDMChannelGroup42": powerDMChannelGroup42,
       "powerDMChannelGroup43": powerDMChannelGroup43,
       "powerDMChannelGroup44": powerDMChannelGroup44,
       "powerDMChannelGroup45": powerDMChannelGroup45,
       "powerDMChannelGroup46": powerDMChannelGroup46,
       "powerDMChannelGroup47": powerDMChannelGroup47,
       "powerDMChannelGroup48": powerDMChannelGroup48,
       "powerDMDeciAmps1": powerDMDeciAmps1,
       "powerDMDeciAmps2": powerDMDeciAmps2,
       "powerDMDeciAmps3": powerDMDeciAmps3,
       "powerDMDeciAmps4": powerDMDeciAmps4,
       "powerDMDeciAmps5": powerDMDeciAmps5,
       "powerDMDeciAmps6": powerDMDeciAmps6,
       "powerDMDeciAmps7": powerDMDeciAmps7,
       "powerDMDeciAmps8": powerDMDeciAmps8,
       "powerDMDeciAmps9": powerDMDeciAmps9,
       "powerDMDeciAmps10": powerDMDeciAmps10,
       "powerDMDeciAmps11": powerDMDeciAmps11,
       "powerDMDeciAmps12": powerDMDeciAmps12,
       "powerDMDeciAmps13": powerDMDeciAmps13,
       "powerDMDeciAmps14": powerDMDeciAmps14,
       "powerDMDeciAmps15": powerDMDeciAmps15,
       "powerDMDeciAmps16": powerDMDeciAmps16,
       "powerDMDeciAmps17": powerDMDeciAmps17,
       "powerDMDeciAmps18": powerDMDeciAmps18,
       "powerDMDeciAmps19": powerDMDeciAmps19,
       "powerDMDeciAmps20": powerDMDeciAmps20,
       "powerDMDeciAmps21": powerDMDeciAmps21,
       "powerDMDeciAmps22": powerDMDeciAmps22,
       "powerDMDeciAmps23": powerDMDeciAmps23,
       "powerDMDeciAmps24": powerDMDeciAmps24,
       "powerDMDeciAmps25": powerDMDeciAmps25,
       "powerDMDeciAmps26": powerDMDeciAmps26,
       "powerDMDeciAmps27": powerDMDeciAmps27,
       "powerDMDeciAmps28": powerDMDeciAmps28,
       "powerDMDeciAmps29": powerDMDeciAmps29,
       "powerDMDeciAmps30": powerDMDeciAmps30,
       "powerDMDeciAmps31": powerDMDeciAmps31,
       "powerDMDeciAmps32": powerDMDeciAmps32,
       "powerDMDeciAmps33": powerDMDeciAmps33,
       "powerDMDeciAmps34": powerDMDeciAmps34,
       "powerDMDeciAmps35": powerDMDeciAmps35,
       "powerDMDeciAmps36": powerDMDeciAmps36,
       "powerDMDeciAmps37": powerDMDeciAmps37,
       "powerDMDeciAmps38": powerDMDeciAmps38,
       "powerDMDeciAmps39": powerDMDeciAmps39,
       "powerDMDeciAmps40": powerDMDeciAmps40,
       "powerDMDeciAmps41": powerDMDeciAmps41,
       "powerDMDeciAmps42": powerDMDeciAmps42,
       "powerDMDeciAmps43": powerDMDeciAmps43,
       "powerDMDeciAmps44": powerDMDeciAmps44,
       "powerDMDeciAmps45": powerDMDeciAmps45,
       "powerDMDeciAmps46": powerDMDeciAmps46,
       "powerDMDeciAmps47": powerDMDeciAmps47,
       "powerDMDeciAmps48": powerDMDeciAmps48,
       "ioExpanderTable": ioExpanderTable,
       "ioExpanderEntry": ioExpanderEntry,
       "ioExpanderIndex": ioExpanderIndex,
       "ioExpanderSerial": ioExpanderSerial,
       "ioExpanderName": ioExpanderName,
       "ioExpanderAvail": ioExpanderAvail,
       "ioExpanderFriendlyName1": ioExpanderFriendlyName1,
       "ioExpanderFriendlyName2": ioExpanderFriendlyName2,
       "ioExpanderFriendlyName3": ioExpanderFriendlyName3,
       "ioExpanderFriendlyName4": ioExpanderFriendlyName4,
       "ioExpanderFriendlyName5": ioExpanderFriendlyName5,
       "ioExpanderFriendlyName6": ioExpanderFriendlyName6,
       "ioExpanderFriendlyName7": ioExpanderFriendlyName7,
       "ioExpanderFriendlyName8": ioExpanderFriendlyName8,
       "ioExpanderFriendlyName9": ioExpanderFriendlyName9,
       "ioExpanderFriendlyName10": ioExpanderFriendlyName10,
       "ioExpanderFriendlyName11": ioExpanderFriendlyName11,
       "ioExpanderFriendlyName12": ioExpanderFriendlyName12,
       "ioExpanderFriendlyName13": ioExpanderFriendlyName13,
       "ioExpanderFriendlyName14": ioExpanderFriendlyName14,
       "ioExpanderFriendlyName15": ioExpanderFriendlyName15,
       "ioExpanderFriendlyName16": ioExpanderFriendlyName16,
       "ioExpanderFriendlyName17": ioExpanderFriendlyName17,
       "ioExpanderFriendlyName18": ioExpanderFriendlyName18,
       "ioExpanderFriendlyName19": ioExpanderFriendlyName19,
       "ioExpanderFriendlyName20": ioExpanderFriendlyName20,
       "ioExpanderFriendlyName21": ioExpanderFriendlyName21,
       "ioExpanderFriendlyName22": ioExpanderFriendlyName22,
       "ioExpanderFriendlyName23": ioExpanderFriendlyName23,
       "ioExpanderFriendlyName24": ioExpanderFriendlyName24,
       "ioExpanderFriendlyName25": ioExpanderFriendlyName25,
       "ioExpanderFriendlyName26": ioExpanderFriendlyName26,
       "ioExpanderFriendlyName27": ioExpanderFriendlyName27,
       "ioExpanderFriendlyName28": ioExpanderFriendlyName28,
       "ioExpanderFriendlyName29": ioExpanderFriendlyName29,
       "ioExpanderFriendlyName30": ioExpanderFriendlyName30,
       "ioExpanderFriendlyName31": ioExpanderFriendlyName31,
       "ioExpanderFriendlyName32": ioExpanderFriendlyName32,
       "ioExpanderIO1": ioExpanderIO1,
       "ioExpanderIO2": ioExpanderIO2,
       "ioExpanderIO3": ioExpanderIO3,
       "ioExpanderIO4": ioExpanderIO4,
       "ioExpanderIO5": ioExpanderIO5,
       "ioExpanderIO6": ioExpanderIO6,
       "ioExpanderIO7": ioExpanderIO7,
       "ioExpanderIO8": ioExpanderIO8,
       "ioExpanderIO9": ioExpanderIO9,
       "ioExpanderIO10": ioExpanderIO10,
       "ioExpanderIO11": ioExpanderIO11,
       "ioExpanderIO12": ioExpanderIO12,
       "ioExpanderIO13": ioExpanderIO13,
       "ioExpanderIO14": ioExpanderIO14,
       "ioExpanderIO15": ioExpanderIO15,
       "ioExpanderIO16": ioExpanderIO16,
       "ioExpanderIO17": ioExpanderIO17,
       "ioExpanderIO18": ioExpanderIO18,
       "ioExpanderIO19": ioExpanderIO19,
       "ioExpanderIO20": ioExpanderIO20,
       "ioExpanderIO21": ioExpanderIO21,
       "ioExpanderIO22": ioExpanderIO22,
       "ioExpanderIO23": ioExpanderIO23,
       "ioExpanderIO24": ioExpanderIO24,
       "ioExpanderIO25": ioExpanderIO25,
       "ioExpanderIO26": ioExpanderIO26,
       "ioExpanderIO27": ioExpanderIO27,
       "ioExpanderIO28": ioExpanderIO28,
       "ioExpanderIO29": ioExpanderIO29,
       "ioExpanderIO30": ioExpanderIO30,
       "ioExpanderIO31": ioExpanderIO31,
       "ioExpanderIO32": ioExpanderIO32,
       "ioExpanderRelayName1": ioExpanderRelayName1,
       "ioExpanderRelayState1": ioExpanderRelayState1,
       "ioExpanderRelayLatchingMode1": ioExpanderRelayLatchingMode1,
       "ioExpanderRelayOverride1": ioExpanderRelayOverride1,
       "ioExpanderRelayAcknowledge1": ioExpanderRelayAcknowledge1,
       "ioExpanderRelayName2": ioExpanderRelayName2,
       "ioExpanderRelayState2": ioExpanderRelayState2,
       "ioExpanderRelayLatchingMode2": ioExpanderRelayLatchingMode2,
       "ioExpanderRelayOverride2": ioExpanderRelayOverride2,
       "ioExpanderRelayAcknowledge2": ioExpanderRelayAcknowledge2,
       "ioExpanderRelayName3": ioExpanderRelayName3,
       "ioExpanderRelayState3": ioExpanderRelayState3,
       "ioExpanderRelayLatchingMode3": ioExpanderRelayLatchingMode3,
       "ioExpanderRelayOverride3": ioExpanderRelayOverride3,
       "ioExpanderRelayAcknowledge3": ioExpanderRelayAcknowledge3,
       "t3hdSensorTable": t3hdSensorTable,
       "t3hdSensorEntry": t3hdSensorEntry,
       "t3hdSensorIndex": t3hdSensorIndex,
       "t3hdSensorSerial": t3hdSensorSerial,
       "t3hdSensorName": t3hdSensorName,
       "t3hdSensorAvail": t3hdSensorAvail,
       "t3hdSensorIntName": t3hdSensorIntName,
       "t3hdSensorIntTempC": t3hdSensorIntTempC,
       "t3hdSensorIntTempF": t3hdSensorIntTempF,
       "t3hdSensorIntHumidity": t3hdSensorIntHumidity,
       "t3hdSensorIntDewPointC": t3hdSensorIntDewPointC,
       "t3hdSensorIntDewPointF": t3hdSensorIntDewPointF,
       "t3hdSensorExt1Avail": t3hdSensorExt1Avail,
       "t3hdSensorExt1Name": t3hdSensorExt1Name,
       "t3hdSensorExt1TempC": t3hdSensorExt1TempC,
       "t3hdSensorExt1TempF": t3hdSensorExt1TempF,
       "t3hdSensorExt2Avail": t3hdSensorExt2Avail,
       "t3hdSensorExt2Name": t3hdSensorExt2Name,
       "t3hdSensorExt2TempC": t3hdSensorExt2TempC,
       "t3hdSensorExt2TempF": t3hdSensorExt2TempF,
       "thdSensorTable": thdSensorTable,
       "thdSensorEntry": thdSensorEntry,
       "thdSensorIndex": thdSensorIndex,
       "thdSensorSerial": thdSensorSerial,
       "thdSensorName": thdSensorName,
       "thdSensorAvail": thdSensorAvail,
       "thdSensorTempC": thdSensorTempC,
       "thdSensorTempF": thdSensorTempF,
       "thdSensorHumidity": thdSensorHumidity,
       "thdSensorDewPointC": thdSensorDewPointC,
       "thdSensorDewPointF": thdSensorDewPointF,
       "pos60VdcSensorTable": pos60VdcSensorTable,
       "pos60VdcSensorEntry": pos60VdcSensorEntry,
       "pos60VdcSensorIndex": pos60VdcSensorIndex,
       "pos60VdcSensorSerial": pos60VdcSensorSerial,
       "pos60VdcSensorName": pos60VdcSensorName,
       "pos60VdcSensorAvail": pos60VdcSensorAvail,
       "pos60VdcSensorVoltage": pos60VdcSensorVoltage,
       "ctrl2CirTotTable": ctrl2CirTotTable,
       "ctrl2CirTotEntry": ctrl2CirTotEntry,
       "ctrl2CirTotIndex": ctrl2CirTotIndex,
       "ctrl2CirTotSerial": ctrl2CirTotSerial,
       "ctrl2CirTotName": ctrl2CirTotName,
       "ctrl2CirTotAvail": ctrl2CirTotAvail,
       "ctrl2CirTotkWattHrsTot": ctrl2CirTotkWattHrsTot,
       "ctrl2CirTotVoltsTot": ctrl2CirTotVoltsTot,
       "ctrl2CirTotVoltPeakTot": ctrl2CirTotVoltPeakTot,
       "ctrl2CirTotDeciAmpsTot": ctrl2CirTotDeciAmpsTot,
       "ctrl2CirTotDeciAmpsPeakTot": ctrl2CirTotDeciAmpsPeakTot,
       "ctrl2CirTotRealPowerTot": ctrl2CirTotRealPowerTot,
       "ctrl2CirTotApparentPowerTot": ctrl2CirTotApparentPowerTot,
       "ctrl2CirTotPowerFactorTot": ctrl2CirTotPowerFactorTot,
       "ctrl2CirTotkWattHrsA": ctrl2CirTotkWattHrsA,
       "ctrl2CirTotVoltsA": ctrl2CirTotVoltsA,
       "ctrl2CirTotVoltPeakA": ctrl2CirTotVoltPeakA,
       "ctrl2CirTotDeciAmpsA": ctrl2CirTotDeciAmpsA,
       "ctrl2CirTotDeciAmpsPeakA": ctrl2CirTotDeciAmpsPeakA,
       "ctrl2CirTotRealPowerA": ctrl2CirTotRealPowerA,
       "ctrl2CirTotApparentPowerA": ctrl2CirTotApparentPowerA,
       "ctrl2CirTotPowerFactorA": ctrl2CirTotPowerFactorA,
       "ctrl2CirTotkWattHrsB": ctrl2CirTotkWattHrsB,
       "ctrl2CirTotVoltsB": ctrl2CirTotVoltsB,
       "ctrl2CirTotVoltPeakB": ctrl2CirTotVoltPeakB,
       "ctrl2CirTotDeciAmpsB": ctrl2CirTotDeciAmpsB,
       "ctrl2CirTotDeciAmpsPeakB": ctrl2CirTotDeciAmpsPeakB,
       "ctrl2CirTotRealPowerB": ctrl2CirTotRealPowerB,
       "ctrl2CirTotApparentPowerB": ctrl2CirTotApparentPowerB,
       "ctrl2CirTotPowerFactorB": ctrl2CirTotPowerFactorB,
       "sc10Table": sc10Table,
       "sc10Entry": sc10Entry,
       "sc10Index": sc10Index,
       "sc10Serial": sc10Serial,
       "sc10Name": sc10Name,
       "sc10Avail": sc10Avail,
       "sc10ControlMode": sc10ControlMode,
       "sc10SetpointC": sc10SetpointC,
       "sc10SetpointF": sc10SetpointF,
       "sc10TempC": sc10TempC,
       "sc10TempF": sc10TempF,
       "sc10Capacity": sc10Capacity,
       "alarmSystem": alarmSystem,
       "alarmCfgTable": alarmCfgTable,
       "alarmCfgEntry": alarmCfgEntry,
       "alarmCfgIndex": alarmCfgIndex,
       "alarmCfgReadingID": alarmCfgReadingID,
       "alarmCfgThreshold": alarmCfgThreshold,
       "alarmCfgTripSelect": alarmCfgTripSelect,
       "gstTrap": gstTrap,
       "gstTrapPrefix": gstTrapPrefix,
       "gstTestNOTIFY": gstTestNOTIFY,
       "gstClimateTempCNOTIFY": gstClimateTempCNOTIFY,
       "gstClimateTempFNOTIFY": gstClimateTempFNOTIFY,
       "gstClimateHumidityNOTIFY": gstClimateHumidityNOTIFY,
       "gstClimateLightNOTIFY": gstClimateLightNOTIFY,
       "gstClimateAirflowNOTIFY": gstClimateAirflowNOTIFY,
       "gstClimateSoundNOTIFY": gstClimateSoundNOTIFY,
       "gstClimateIO1NOTIFY": gstClimateIO1NOTIFY,
       "gstClimateIO2NOTIFY": gstClimateIO2NOTIFY,
       "gstClimateIO3NOTIFY": gstClimateIO3NOTIFY,
       "gstClimateVoltsNOTIFY": gstClimateVoltsNOTIFY,
       "gstClimateVoltPeakNOTIFY": gstClimateVoltPeakNOTIFY,
       "gstClimateDeciAmpsANOTIFY": gstClimateDeciAmpsANOTIFY,
       "gstClimateDeciAmpPeakANOTIFY": gstClimateDeciAmpPeakANOTIFY,
       "gstClimateRealPowerANOTIFY": gstClimateRealPowerANOTIFY,
       "gstClimateApparentPowerANOTIFY": gstClimateApparentPowerANOTIFY,
       "gstClimatePowerFactorANOTIFY": gstClimatePowerFactorANOTIFY,
       "gstClimateDeciAmpsBNOTIFY": gstClimateDeciAmpsBNOTIFY,
       "gstClimateDeciAmpPeakBNOTIFY": gstClimateDeciAmpPeakBNOTIFY,
       "gstClimateRealPowerBNOTIFY": gstClimateRealPowerBNOTIFY,
       "gstClimateApparentPowerBNOTIFY": gstClimateApparentPowerBNOTIFY,
       "gstClimatePowerFactorBNOTIFY": gstClimatePowerFactorBNOTIFY,
       "gstClimateDeciAmpsCNOTIFY": gstClimateDeciAmpsCNOTIFY,
       "gstClimateDeciAmpPeakCNOTIFY": gstClimateDeciAmpPeakCNOTIFY,
       "gstClimateRealPowerCNOTIFY": gstClimateRealPowerCNOTIFY,
       "gstClimateApparentPowerCNOTIFY": gstClimateApparentPowerCNOTIFY,
       "gstClimatePowerFactorCNOTIFY": gstClimatePowerFactorCNOTIFY,
       "gstClimateDewPointCNOTIFY": gstClimateDewPointCNOTIFY,
       "gstClimateDewPointFNOTIFY": gstClimateDewPointFNOTIFY,
       "gstPowMonkWattHrsNOTIFY": gstPowMonkWattHrsNOTIFY,
       "gstPowMonVoltsNOTIFY": gstPowMonVoltsNOTIFY,
       "gstPowMonVoltMaxNOTIFY": gstPowMonVoltMaxNOTIFY,
       "gstPowMonVoltMinNOTIFY": gstPowMonVoltMinNOTIFY,
       "gstPowMonVoltPeakNOTIFY": gstPowMonVoltPeakNOTIFY,
       "gstPowMonDeciAmpsNOTIFY": gstPowMonDeciAmpsNOTIFY,
       "gstPowMonRealPowerNOTIFY": gstPowMonRealPowerNOTIFY,
       "gstPowMonApparentPowerNOTIFY": gstPowMonApparentPowerNOTIFY,
       "gstPowMonPowerFactorNOTIFY": gstPowMonPowerFactorNOTIFY,
       "gstPowMonOutlet1NOTIFY": gstPowMonOutlet1NOTIFY,
       "gstPowMonOutlet2NOTIFY": gstPowMonOutlet2NOTIFY,
       "gstPowMonOutlet1StatusTimeNOTIFY": gstPowMonOutlet1StatusTimeNOTIFY,
       "gstPowMonOutlet2StatusTimeNOTIFY": gstPowMonOutlet2StatusTimeNOTIFY,
       "gstTempSensorTempCNOTIFY": gstTempSensorTempCNOTIFY,
       "gstTempSensorTempFNOTIFY": gstTempSensorTempFNOTIFY,
       "gstAirFlowSensorTempCNOTIFY": gstAirFlowSensorTempCNOTIFY,
       "gstAirFlowSensorTempFNOTIFY": gstAirFlowSensorTempFNOTIFY,
       "gstAirFlowSensorFlowNOTIFY": gstAirFlowSensorFlowNOTIFY,
       "gstAirFlowSensorHumidityNOTIFY": gstAirFlowSensorHumidityNOTIFY,
       "gstAirFlowSensorDewPointCNOTIFY": gstAirFlowSensorDewPointCNOTIFY,
       "gstAirFlowSensorDewPointFNOTIFY": gstAirFlowSensorDewPointFNOTIFY,
       "gstCtrl3ChDELTADeciAmpsANOTIFY": gstCtrl3ChDELTADeciAmpsANOTIFY,
       "gstCtrl3ChDELTADeciAmpsBNOTIFY": gstCtrl3ChDELTADeciAmpsBNOTIFY,
       "gstCtrl3ChDELTADeciAmpsCNOTIFY": gstCtrl3ChDELTADeciAmpsCNOTIFY,
       "gstCtrl3ChDELTAkWattHrsTotalNOTIFY": gstCtrl3ChDELTAkWattHrsTotalNOTIFY,
       "gstCtrl3ChDELTARealPowerTotalNOTIFY": gstCtrl3ChDELTARealPowerTotalNOTIFY,
       "gstCtrl3ChDELTAkWattHrsABNOTIFY": gstCtrl3ChDELTAkWattHrsABNOTIFY,
       "gstCtrl3ChDELTAVoltsABNOTIFY": gstCtrl3ChDELTAVoltsABNOTIFY,
       "gstCtrl3ChDELTAVoltPeakABNOTIFY": gstCtrl3ChDELTAVoltPeakABNOTIFY,
       "gstCtrl3ChDELTARealPowerABNOTIFY": gstCtrl3ChDELTARealPowerABNOTIFY,
       "gstCtrl3ChDELTAApparentPowerABNOTIFY": gstCtrl3ChDELTAApparentPowerABNOTIFY,
       "gstCtrl3ChDELTAPowerFactorABNOTIFY": gstCtrl3ChDELTAPowerFactorABNOTIFY,
       "gstCtrl3ChDELTAkWattHrsBCNOTIFY": gstCtrl3ChDELTAkWattHrsBCNOTIFY,
       "gstCtrl3ChDELTAVoltsBCNOTIFY": gstCtrl3ChDELTAVoltsBCNOTIFY,
       "gstCtrl3ChDELTAVoltPeakBCNOTIFY": gstCtrl3ChDELTAVoltPeakBCNOTIFY,
       "gstCtrl3ChDELTARealPowerBCNOTIFY": gstCtrl3ChDELTARealPowerBCNOTIFY,
       "gstCtrl3ChDELTAApparentPowerBCNOTIFY": gstCtrl3ChDELTAApparentPowerBCNOTIFY,
       "gstCtrl3ChDELTAPowerFactorBCNOTIFY": gstCtrl3ChDELTAPowerFactorBCNOTIFY,
       "gstCtrl3ChDELTAkWattHrsCANOTIFY": gstCtrl3ChDELTAkWattHrsCANOTIFY,
       "gstCtrl3ChDELTAVoltsCANOTIFY": gstCtrl3ChDELTAVoltsCANOTIFY,
       "gstCtrl3ChDELTAVoltPeakCANOTIFY": gstCtrl3ChDELTAVoltPeakCANOTIFY,
       "gstCtrl3ChDELTARealPowerCANOTIFY": gstCtrl3ChDELTARealPowerCANOTIFY,
       "gstCtrl3ChDELTAApparentPowerCANOTIFY": gstCtrl3ChDELTAApparentPowerCANOTIFY,
       "gstCtrl3ChDELTAPowerFactorCANOTIFY": gstCtrl3ChDELTAPowerFactorCANOTIFY,
       "gstDoorSensorStatusNOTIFY": gstDoorSensorStatusNOTIFY,
       "gstWaterSensorDampnessNOTIFY": gstWaterSensorDampnessNOTIFY,
       "gstCurrentMonitorDeciAmpsNOTIFY": gstCurrentMonitorDeciAmpsNOTIFY,
       "gstMillivoltMonitorMVNOTIFY": gstMillivoltMonitorMVNOTIFY,
       "gstPow3ChkWattHrsANOTIFY": gstPow3ChkWattHrsANOTIFY,
       "gstPow3ChVoltsANOTIFY": gstPow3ChVoltsANOTIFY,
       "gstPow3ChVoltMaxANOTIFY": gstPow3ChVoltMaxANOTIFY,
       "gstPow3ChVoltMinANOTIFY": gstPow3ChVoltMinANOTIFY,
       "gstPow3ChVoltPeakANOTIFY": gstPow3ChVoltPeakANOTIFY,
       "gstPow3ChDeciAmpsANOTIFY": gstPow3ChDeciAmpsANOTIFY,
       "gstPow3ChRealPowerANOTIFY": gstPow3ChRealPowerANOTIFY,
       "gstPow3ChApparentPowerANOTIFY": gstPow3ChApparentPowerANOTIFY,
       "gstPow3ChPowerFactorANOTIFY": gstPow3ChPowerFactorANOTIFY,
       "gstPow3ChkWattHrsBNOTIFY": gstPow3ChkWattHrsBNOTIFY,
       "gstPow3ChVoltsBNOTIFY": gstPow3ChVoltsBNOTIFY,
       "gstPow3ChVoltMaxBNOTIFY": gstPow3ChVoltMaxBNOTIFY,
       "gstPow3ChVoltMinBNOTIFY": gstPow3ChVoltMinBNOTIFY,
       "gstPow3ChVoltPeakBNOTIFY": gstPow3ChVoltPeakBNOTIFY,
       "gstPow3ChDeciAmpsBNOTIFY": gstPow3ChDeciAmpsBNOTIFY,
       "gstPow3ChRealPowerBNOTIFY": gstPow3ChRealPowerBNOTIFY,
       "gstPow3ChApparentPowerBNOTIFY": gstPow3ChApparentPowerBNOTIFY,
       "gstPow3ChPowerFactorBNOTIFY": gstPow3ChPowerFactorBNOTIFY,
       "gstPow3ChkWattHrsCNOTIFY": gstPow3ChkWattHrsCNOTIFY,
       "gstPow3ChVoltsCNOTIFY": gstPow3ChVoltsCNOTIFY,
       "gstPow3ChVoltMaxCNOTIFY": gstPow3ChVoltMaxCNOTIFY,
       "gstPow3ChVoltMinCNOTIFY": gstPow3ChVoltMinCNOTIFY,
       "gstPow3ChVoltPeakCNOTIFY": gstPow3ChVoltPeakCNOTIFY,
       "gstPow3ChDeciAmpsCNOTIFY": gstPow3ChDeciAmpsCNOTIFY,
       "gstPow3ChRealPowerCNOTIFY": gstPow3ChRealPowerCNOTIFY,
       "gstPow3ChApparentPowerCNOTIFY": gstPow3ChApparentPowerCNOTIFY,
       "gstPow3ChPowerFactorCNOTIFY": gstPow3ChPowerFactorCNOTIFY,
       "gstPow3ChkWattHrsTotalNOTIFY": gstPow3ChkWattHrsTotalNOTIFY,
       "gstPow3ChRealPowerTotalNOTIFY": gstPow3ChRealPowerTotalNOTIFY,
       "gstOutlet1StatusNOTIFY": gstOutlet1StatusNOTIFY,
       "gstOutlet2StatusNOTIFY": gstOutlet2StatusNOTIFY,
       "gstVsfcSetPointCNOTIFY": gstVsfcSetPointCNOTIFY,
       "gstVsfcSetPointFNOTIFY": gstVsfcSetPointFNOTIFY,
       "gstVsfcFanSpeedNOTIFY": gstVsfcFanSpeedNOTIFY,
       "gstVsfcIntTempCNOTIFY": gstVsfcIntTempCNOTIFY,
       "gstVsfcIntTempFNOTIFY": gstVsfcIntTempFNOTIFY,
       "gstVsfcExt1TempCNOTIFY": gstVsfcExt1TempCNOTIFY,
       "gstVsfcExt1TempFNOTIFY": gstVsfcExt1TempFNOTIFY,
       "gstVsfcExt2TempCNOTIFY": gstVsfcExt2TempCNOTIFY,
       "gstVsfcExt2TempFNOTIFY": gstVsfcExt2TempFNOTIFY,
       "gstVsfcExt3TempCNOTIFY": gstVsfcExt3TempCNOTIFY,
       "gstVsfcExt3TempFNOTIFY": gstVsfcExt3TempFNOTIFY,
       "gstVsfcExt4TempCNOTIFY": gstVsfcExt4TempCNOTIFY,
       "gstVsfcExt4TempFNOTIFY": gstVsfcExt4TempFNOTIFY,
       "gstCtrl3ChVoltsANOTIFY": gstCtrl3ChVoltsANOTIFY,
       "gstCtrl3ChVoltPeakANOTIFY": gstCtrl3ChVoltPeakANOTIFY,
       "gstCtrl3ChDeciAmpsANOTIFY": gstCtrl3ChDeciAmpsANOTIFY,
       "gstCtrl3ChDeciAmpsPeakANOTIFY": gstCtrl3ChDeciAmpsPeakANOTIFY,
       "gstCtrl3ChRealPowerANOTIFY": gstCtrl3ChRealPowerANOTIFY,
       "gstCtrl3ChApparentPowerANOTIFY": gstCtrl3ChApparentPowerANOTIFY,
       "gstCtrl3ChPowerFactorANOTIFY": gstCtrl3ChPowerFactorANOTIFY,
       "gstCtrl3ChVoltsBNOTIFY": gstCtrl3ChVoltsBNOTIFY,
       "gstCtrl3ChVoltPeakBNOTIFY": gstCtrl3ChVoltPeakBNOTIFY,
       "gstCtrl3ChDeciAmpsBNOTIFY": gstCtrl3ChDeciAmpsBNOTIFY,
       "gstCtrl3ChDeciAmpsPeakBNOTIFY": gstCtrl3ChDeciAmpsPeakBNOTIFY,
       "gstCtrl3ChRealPowerBNOTIFY": gstCtrl3ChRealPowerBNOTIFY,
       "gstCtrl3ChApparentPowerBNOTIFY": gstCtrl3ChApparentPowerBNOTIFY,
       "gstCtrl3ChPowerFactorBNOTIFY": gstCtrl3ChPowerFactorBNOTIFY,
       "gstCtrl3ChVoltsCNOTIFY": gstCtrl3ChVoltsCNOTIFY,
       "gstCtrl3ChVoltPeakCNOTIFY": gstCtrl3ChVoltPeakCNOTIFY,
       "gstCtrl3ChDeciAmpsCNOTIFY": gstCtrl3ChDeciAmpsCNOTIFY,
       "gstCtrl3ChDeciAmpsPeakCNOTIFY": gstCtrl3ChDeciAmpsPeakCNOTIFY,
       "gstCtrl3ChRealPowerCNOTIFY": gstCtrl3ChRealPowerCNOTIFY,
       "gstCtrl3ChApparentPowerCNOTIFY": gstCtrl3ChApparentPowerCNOTIFY,
       "gstCtrl3ChPowerFactorCNOTIFY": gstCtrl3ChPowerFactorCNOTIFY,
       "gstCtrlGrpAmpsANOTIFY": gstCtrlGrpAmpsANOTIFY,
       "gstCtrlGrpAmpsBNOTIFY": gstCtrlGrpAmpsBNOTIFY,
       "gstCtrlGrpAmpsCNOTIFY": gstCtrlGrpAmpsCNOTIFY,
       "gstCtrlGrpAmpsDNOTIFY": gstCtrlGrpAmpsDNOTIFY,
       "gstCtrlGrpAmpsENOTIFY": gstCtrlGrpAmpsENOTIFY,
       "gstCtrlGrpAmpsFNOTIFY": gstCtrlGrpAmpsFNOTIFY,
       "gstCtrlGrpAmpsGNOTIFY": gstCtrlGrpAmpsGNOTIFY,
       "gstCtrlGrpAmpsHNOTIFY": gstCtrlGrpAmpsHNOTIFY,
       "gstCtrlGrpAmpsAVoltsNOTIFY": gstCtrlGrpAmpsAVoltsNOTIFY,
       "gstCtrlGrpAmpsBVoltsNOTIFY": gstCtrlGrpAmpsBVoltsNOTIFY,
       "gstCtrlGrpAmpsCVoltsNOTIFY": gstCtrlGrpAmpsCVoltsNOTIFY,
       "gstCtrlGrpAmpsDVoltsNOTIFY": gstCtrlGrpAmpsDVoltsNOTIFY,
       "gstCtrlGrpAmpsEVoltsNOTIFY": gstCtrlGrpAmpsEVoltsNOTIFY,
       "gstCtrlGrpAmpsFVoltsNOTIFY": gstCtrlGrpAmpsFVoltsNOTIFY,
       "gstCtrlGrpAmpsGVoltsNOTIFY": gstCtrlGrpAmpsGVoltsNOTIFY,
       "gstCtrlGrpAmpsHVoltsNOTIFY": gstCtrlGrpAmpsHVoltsNOTIFY,
       "gstCtrlGrpAmpsINOTIFY": gstCtrlGrpAmpsINOTIFY,
       "gstCtrlGrpAmpsJNOTIFY": gstCtrlGrpAmpsJNOTIFY,
       "gstCtrlGrpAmpsKNOTIFY": gstCtrlGrpAmpsKNOTIFY,
       "gstCtrlGrpAmpsLNOTIFY": gstCtrlGrpAmpsLNOTIFY,
       "gstCtrlGrpAmpsMNOTIFY": gstCtrlGrpAmpsMNOTIFY,
       "gstCtrlGrpAmpsNNOTIFY": gstCtrlGrpAmpsNNOTIFY,
       "gstCtrlGrpAmpsONOTIFY": gstCtrlGrpAmpsONOTIFY,
       "gstCtrlGrpAmpsPNOTIFY": gstCtrlGrpAmpsPNOTIFY,
       "gstCtrlGrpAmpsIVoltsNOTIFY": gstCtrlGrpAmpsIVoltsNOTIFY,
       "gstCtrlGrpAmpsJVoltsNOTIFY": gstCtrlGrpAmpsJVoltsNOTIFY,
       "gstCtrlGrpAmpsKVoltsNOTIFY": gstCtrlGrpAmpsKVoltsNOTIFY,
       "gstCtrlGrpAmpsLVoltsNOTIFY": gstCtrlGrpAmpsLVoltsNOTIFY,
       "gstCtrlGrpAmpsMVoltsNOTIFY": gstCtrlGrpAmpsMVoltsNOTIFY,
       "gstCtrlGrpAmpsNVoltsNOTIFY": gstCtrlGrpAmpsNVoltsNOTIFY,
       "gstCtrlGrpAmpsOVoltsNOTIFY": gstCtrlGrpAmpsOVoltsNOTIFY,
       "gstCtrlGrpAmpsPVoltsNOTIFY": gstCtrlGrpAmpsPVoltsNOTIFY,
       "gstCtrlOutletPendingNOTIFY": gstCtrlOutletPendingNOTIFY,
       "gstCtrlOutletDeciAmpsNOTIFY": gstCtrlOutletDeciAmpsNOTIFY,
       "gstCtrlOutletGroupNOTIFY": gstCtrlOutletGroupNOTIFY,
       "gstCtrlOutletUpDelayNOTIFY": gstCtrlOutletUpDelayNOTIFY,
       "gstCtrlOutletDwnDelayNOTIFY": gstCtrlOutletDwnDelayNOTIFY,
       "gstCtrlOutletRbtDurationNOTIFY": gstCtrlOutletRbtDurationNOTIFY,
       "gstCtrlOutletURLNOTIFY": gstCtrlOutletURLNOTIFY,
       "gstCtrlOutletPOAActionNOTIFY": gstCtrlOutletPOAActionNOTIFY,
       "gstCtrlOutletPOADelayNOTIFY": gstCtrlOutletPOADelayNOTIFY,
       "gstCtrlOutletkWattHrsNOTIFY": gstCtrlOutletkWattHrsNOTIFY,
       "gstCtrlOutletPowerNOTIFY": gstCtrlOutletPowerNOTIFY,
       "gstCtrlOutletRbtDelayNOTIFY": gstCtrlOutletRbtDelayNOTIFY,
       "gstCtrlOutletStatusTimeNOTIFY": gstCtrlOutletStatusTimeNOTIFY,
       "gstDewPointSensorTempCNOTIFY": gstDewPointSensorTempCNOTIFY,
       "gstDewPointSensorTempFNOTIFY": gstDewPointSensorTempFNOTIFY,
       "gstDewPointSensorHumidityNOTIFY": gstDewPointSensorHumidityNOTIFY,
       "gstDewPointSensorDewPointCNOTIFY": gstDewPointSensorDewPointCNOTIFY,
       "gstDewPointSensorDewPointFNOTIFY": gstDewPointSensorDewPointFNOTIFY,
       "gstDigitalSensorDigitalNOTIFY": gstDigitalSensorDigitalNOTIFY,
       "gstDstsVoltsANOTIFY": gstDstsVoltsANOTIFY,
       "gstDstsDeciAmpsANOTIFY": gstDstsDeciAmpsANOTIFY,
       "gstDstsVoltsBNOTIFY": gstDstsVoltsBNOTIFY,
       "gstDstsDeciAmpsBNOTIFY": gstDstsDeciAmpsBNOTIFY,
       "gstDstsSourceAActiveNOTIFY": gstDstsSourceAActiveNOTIFY,
       "gstDstsSourceBActiveNOTIFY": gstDstsSourceBActiveNOTIFY,
       "gstDstsPowerStatusANOTIFY": gstDstsPowerStatusANOTIFY,
       "gstDstsPowerStatusBNOTIFY": gstDstsPowerStatusBNOTIFY,
       "gstDstsSourceATempCNOTIFY": gstDstsSourceATempCNOTIFY,
       "gstDstsSourceBTempCNOTIFY": gstDstsSourceBTempCNOTIFY,
       "gstCpmSensorStatusNOTIFY": gstCpmSensorStatusNOTIFY,
       "gstSmokeAlarmStatusNOTIFY": gstSmokeAlarmStatusNOTIFY,
       "gstNeg48VdcSensorVoltageNOTIFY": gstNeg48VdcSensorVoltageNOTIFY,
       "gstPos30VdcSensorVoltageNOTIFY": gstPos30VdcSensorVoltageNOTIFY,
       "gstAnalogSensorAnalogNOTIFY": gstAnalogSensorAnalogNOTIFY,
       "gstCtrl3ChIECkWattHrsANOTIFY": gstCtrl3ChIECkWattHrsANOTIFY,
       "gstCtrl3ChIECVoltsANOTIFY": gstCtrl3ChIECVoltsANOTIFY,
       "gstCtrl3ChIECVoltPeakANOTIFY": gstCtrl3ChIECVoltPeakANOTIFY,
       "gstCtrl3ChIECDeciAmpsANOTIFY": gstCtrl3ChIECDeciAmpsANOTIFY,
       "gstCtrl3ChIECDeciAmpsPeakANOTIFY": gstCtrl3ChIECDeciAmpsPeakANOTIFY,
       "gstCtrl3ChIECRealPowerANOTIFY": gstCtrl3ChIECRealPowerANOTIFY,
       "gstCtrl3ChIECApparentPowerANOTIFY": gstCtrl3ChIECApparentPowerANOTIFY,
       "gstCtrl3ChIECPowerFactorANOTIFY": gstCtrl3ChIECPowerFactorANOTIFY,
       "gstCtrl3ChIECkWattHrsBNOTIFY": gstCtrl3ChIECkWattHrsBNOTIFY,
       "gstCtrl3ChIECVoltsBNOTIFY": gstCtrl3ChIECVoltsBNOTIFY,
       "gstCtrl3ChIECVoltPeakBNOTIFY": gstCtrl3ChIECVoltPeakBNOTIFY,
       "gstCtrl3ChIECDeciAmpsBNOTIFY": gstCtrl3ChIECDeciAmpsBNOTIFY,
       "gstCtrl3ChIECDeciAmpsPeakBNOTIFY": gstCtrl3ChIECDeciAmpsPeakBNOTIFY,
       "gstCtrl3ChIECRealPowerBNOTIFY": gstCtrl3ChIECRealPowerBNOTIFY,
       "gstCtrl3ChIECApparentPowerBNOTIFY": gstCtrl3ChIECApparentPowerBNOTIFY,
       "gstCtrl3ChIECPowerFactorBNOTIFY": gstCtrl3ChIECPowerFactorBNOTIFY,
       "gstCtrl3ChIECkWattHrsCNOTIFY": gstCtrl3ChIECkWattHrsCNOTIFY,
       "gstCtrl3ChIECVoltsCNOTIFY": gstCtrl3ChIECVoltsCNOTIFY,
       "gstCtrl3ChIECVoltPeakCNOTIFY": gstCtrl3ChIECVoltPeakCNOTIFY,
       "gstCtrl3ChIECDeciAmpsCNOTIFY": gstCtrl3ChIECDeciAmpsCNOTIFY,
       "gstCtrl3ChIECDeciAmpsPeakCNOTIFY": gstCtrl3ChIECDeciAmpsPeakCNOTIFY,
       "gstCtrl3ChIECRealPowerCNOTIFY": gstCtrl3ChIECRealPowerCNOTIFY,
       "gstCtrl3ChIECApparentPowerCNOTIFY": gstCtrl3ChIECApparentPowerCNOTIFY,
       "gstCtrl3ChIECPowerFactorCNOTIFY": gstCtrl3ChIECPowerFactorCNOTIFY,
       "gstCtrl3ChIECkWattHrsTotalNOTIFY": gstCtrl3ChIECkWattHrsTotalNOTIFY,
       "gstCtrl3ChIECRealPowerTotalNOTIFY": gstCtrl3ChIECRealPowerTotalNOTIFY,
       "gstClimateRelayTempCNOTIFY": gstClimateRelayTempCNOTIFY,
       "gstClimateRelayTempFNOTIFY": gstClimateRelayTempFNOTIFY,
       "gstClimateRelayIO1NOTIFY": gstClimateRelayIO1NOTIFY,
       "gstClimateRelayIO2NOTIFY": gstClimateRelayIO2NOTIFY,
       "gstClimateRelayIO3NOTIFY": gstClimateRelayIO3NOTIFY,
       "gstClimateRelayIO4NOTIFY": gstClimateRelayIO4NOTIFY,
       "gstClimateRelayIO5NOTIFY": gstClimateRelayIO5NOTIFY,
       "gstClimateRelayIO6NOTIFY": gstClimateRelayIO6NOTIFY,
       "gstAirSpeedSwitchSensorAirSpeedNOTIFY": gstAirSpeedSwitchSensorAirSpeedNOTIFY,
       "gstIoExpanderIO1NOTIFY": gstIoExpanderIO1NOTIFY,
       "gstIoExpanderIO2NOTIFY": gstIoExpanderIO2NOTIFY,
       "gstIoExpanderIO3NOTIFY": gstIoExpanderIO3NOTIFY,
       "gstIoExpanderIO4NOTIFY": gstIoExpanderIO4NOTIFY,
       "gstIoExpanderIO5NOTIFY": gstIoExpanderIO5NOTIFY,
       "gstIoExpanderIO6NOTIFY": gstIoExpanderIO6NOTIFY,
       "gstIoExpanderIO7NOTIFY": gstIoExpanderIO7NOTIFY,
       "gstIoExpanderIO8NOTIFY": gstIoExpanderIO8NOTIFY,
       "gstIoExpanderIO9NOTIFY": gstIoExpanderIO9NOTIFY,
       "gstIoExpanderIO10NOTIFY": gstIoExpanderIO10NOTIFY,
       "gstIoExpanderIO11NOTIFY": gstIoExpanderIO11NOTIFY,
       "gstIoExpanderIO12NOTIFY": gstIoExpanderIO12NOTIFY,
       "gstIoExpanderIO13NOTIFY": gstIoExpanderIO13NOTIFY,
       "gstIoExpanderIO14NOTIFY": gstIoExpanderIO14NOTIFY,
       "gstIoExpanderIO15NOTIFY": gstIoExpanderIO15NOTIFY,
       "gstIoExpanderIO16NOTIFY": gstIoExpanderIO16NOTIFY,
       "gstIoExpanderIO17NOTIFY": gstIoExpanderIO17NOTIFY,
       "gstIoExpanderIO18NOTIFY": gstIoExpanderIO18NOTIFY,
       "gstIoExpanderIO19NOTIFY": gstIoExpanderIO19NOTIFY,
       "gstIoExpanderIO20NOTIFY": gstIoExpanderIO20NOTIFY,
       "gstIoExpanderIO21NOTIFY": gstIoExpanderIO21NOTIFY,
       "gstIoExpanderIO22NOTIFY": gstIoExpanderIO22NOTIFY,
       "gstIoExpanderIO23NOTIFY": gstIoExpanderIO23NOTIFY,
       "gstIoExpanderIO24NOTIFY": gstIoExpanderIO24NOTIFY,
       "gstIoExpanderIO25NOTIFY": gstIoExpanderIO25NOTIFY,
       "gstIoExpanderIO26NOTIFY": gstIoExpanderIO26NOTIFY,
       "gstIoExpanderIO27NOTIFY": gstIoExpanderIO27NOTIFY,
       "gstIoExpanderIO28NOTIFY": gstIoExpanderIO28NOTIFY,
       "gstIoExpanderIO29NOTIFY": gstIoExpanderIO29NOTIFY,
       "gstIoExpanderIO30NOTIFY": gstIoExpanderIO30NOTIFY,
       "gstIoExpanderIO31NOTIFY": gstIoExpanderIO31NOTIFY,
       "gstIoExpanderIO32NOTIFY": gstIoExpanderIO32NOTIFY,
       "gstT3hdSensorIntTempCNOTIFY": gstT3hdSensorIntTempCNOTIFY,
       "gstT3hdSensorIntTempFNOTIFY": gstT3hdSensorIntTempFNOTIFY,
       "gstT3hdSensorIntHumidityNOTIFY": gstT3hdSensorIntHumidityNOTIFY,
       "gstT3hdSensorIntDewPointCNOTIFY": gstT3hdSensorIntDewPointCNOTIFY,
       "gstT3hdSensorIntDewPointFNOTIFY": gstT3hdSensorIntDewPointFNOTIFY,
       "gstT3hdSensorExt1TempCNOTIFY": gstT3hdSensorExt1TempCNOTIFY,
       "gstT3hdSensorExt1TempFNOTIFY": gstT3hdSensorExt1TempFNOTIFY,
       "gstT3hdSensorExt2TempCNOTIFY": gstT3hdSensorExt2TempCNOTIFY,
       "gstT3hdSensorExt2TempFNOTIFY": gstT3hdSensorExt2TempFNOTIFY,
       "gstThdSensorTempCNOTIFY": gstThdSensorTempCNOTIFY,
       "gstThdSensorTempFNOTIFY": gstThdSensorTempFNOTIFY,
       "gstThdSensorHumidityNOTIFY": gstThdSensorHumidityNOTIFY,
       "gstThdSensorDewPointCNOTIFY": gstThdSensorDewPointCNOTIFY,
       "gstThdSensorDewPointFNOTIFY": gstThdSensorDewPointFNOTIFY,
       "gstPos60VdcSensorVoltageNOTIFY": gstPos60VdcSensorVoltageNOTIFY,
       "gstCtrl2CirTotkWattHrsTotNOTIFY": gstCtrl2CirTotkWattHrsTotNOTIFY,
       "gstCtrl2CirTotVoltsTotNOTIFY": gstCtrl2CirTotVoltsTotNOTIFY,
       "gstCtrl2CirTotVoltPeakTotNOTIFY": gstCtrl2CirTotVoltPeakTotNOTIFY,
       "gstCtrl2CirTotDeciAmpsTotNOTIFY": gstCtrl2CirTotDeciAmpsTotNOTIFY,
       "gstCtrl2CirTotDeciAmpsPeakTotNOTIFY": gstCtrl2CirTotDeciAmpsPeakTotNOTIFY,
       "gstCtrl2CirTotRealPowerTotNOTIFY": gstCtrl2CirTotRealPowerTotNOTIFY,
       "gstCtrl2CirTotApparentPowerTotNOTIFY": gstCtrl2CirTotApparentPowerTotNOTIFY,
       "gstCtrl2CirTotPowerFactorTotNOTIFY": gstCtrl2CirTotPowerFactorTotNOTIFY,
       "gstCtrl2CirTotkWattHrsANOTIFY": gstCtrl2CirTotkWattHrsANOTIFY,
       "gstCtrl2CirTotVoltsANOTIFY": gstCtrl2CirTotVoltsANOTIFY,
       "gstCtrl2CirTotVoltPeakANOTIFY": gstCtrl2CirTotVoltPeakANOTIFY,
       "gstCtrl2CirTotDeciAmpsANOTIFY": gstCtrl2CirTotDeciAmpsANOTIFY,
       "gstCtrl2CirTotDeciAmpsPeakANOTIFY": gstCtrl2CirTotDeciAmpsPeakANOTIFY,
       "gstCtrl2CirTotRealPowerANOTIFY": gstCtrl2CirTotRealPowerANOTIFY,
       "gstCtrl2CirTotApparentPowerANOTIFY": gstCtrl2CirTotApparentPowerANOTIFY,
       "gstCtrl2CirTotPowerFactorANOTIFY": gstCtrl2CirTotPowerFactorANOTIFY,
       "gstCtrl2CirTotkWattHrsBNOTIFY": gstCtrl2CirTotkWattHrsBNOTIFY,
       "gstCtrl2CirTotVoltsBNOTIFY": gstCtrl2CirTotVoltsBNOTIFY,
       "gstCtrl2CirTotVoltPeakBNOTIFY": gstCtrl2CirTotVoltPeakBNOTIFY,
       "gstCtrl2CirTotDeciAmpsBNOTIFY": gstCtrl2CirTotDeciAmpsBNOTIFY,
       "gstCtrl2CirTotDeciAmpsPeakBNOTIFY": gstCtrl2CirTotDeciAmpsPeakBNOTIFY,
       "gstCtrl2CirTotRealPowerBNOTIFY": gstCtrl2CirTotRealPowerBNOTIFY,
       "gstCtrl2CirTotApparentPowerBNOTIFY": gstCtrl2CirTotApparentPowerBNOTIFY,
       "gstCtrl2CirTotPowerFactorBNOTIFY": gstCtrl2CirTotPowerFactorBNOTIFY,
       "gstSc10ControlModeNOTIFY": gstSc10ControlModeNOTIFY,
       "gstSc10SetpointCNOTIFY": gstSc10SetpointCNOTIFY,
       "gstSc10SetpointFNOTIFY": gstSc10SetpointFNOTIFY,
       "gstSc10TempCNOTIFY": gstSc10TempCNOTIFY,
       "gstSc10TempFNOTIFY": gstSc10TempFNOTIFY,
       "gstSc10CapacityNOTIFY": gstSc10CapacityNOTIFY,
       "gstClimateTempCCLEAR": gstClimateTempCCLEAR,
       "gstClimateTempFCLEAR": gstClimateTempFCLEAR,
       "gstClimateHumidityCLEAR": gstClimateHumidityCLEAR,
       "gstClimateLightCLEAR": gstClimateLightCLEAR,
       "gstClimateAirflowCLEAR": gstClimateAirflowCLEAR,
       "gstClimateSoundCLEAR": gstClimateSoundCLEAR,
       "gstClimateIO1CLEAR": gstClimateIO1CLEAR,
       "gstClimateIO2CLEAR": gstClimateIO2CLEAR,
       "gstClimateIO3CLEAR": gstClimateIO3CLEAR,
       "gstClimateVoltsCLEAR": gstClimateVoltsCLEAR,
       "gstClimateVoltPeakCLEAR": gstClimateVoltPeakCLEAR,
       "gstClimateDeciAmpsACLEAR": gstClimateDeciAmpsACLEAR,
       "gstClimateDeciAmpPeakACLEAR": gstClimateDeciAmpPeakACLEAR,
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
       "gstClimateDewPointCCLEAR": gstClimateDewPointCCLEAR,
       "gstClimateDewPointFCLEAR": gstClimateDewPointFCLEAR,
       "gstPowMonkWattHrsCLEAR": gstPowMonkWattHrsCLEAR,
       "gstPowMonVoltsCLEAR": gstPowMonVoltsCLEAR,
       "gstPowMonVoltMaxCLEAR": gstPowMonVoltMaxCLEAR,
       "gstPowMonVoltMinCLEAR": gstPowMonVoltMinCLEAR,
       "gstPowMonVoltPeakCLEAR": gstPowMonVoltPeakCLEAR,
       "gstPowMonDeciAmpsCLEAR": gstPowMonDeciAmpsCLEAR,
       "gstPowMonRealPowerCLEAR": gstPowMonRealPowerCLEAR,
       "gstPowMonApparentPowerCLEAR": gstPowMonApparentPowerCLEAR,
       "gstPowMonPowerFactorCLEAR": gstPowMonPowerFactorCLEAR,
       "gstPowMonOutlet1CLEAR": gstPowMonOutlet1CLEAR,
       "gstPowMonOutlet2CLEAR": gstPowMonOutlet2CLEAR,
       "gstPowMonOutlet1StatusTimeCLEAR": gstPowMonOutlet1StatusTimeCLEAR,
       "gstPowMonOutlet2StatusTimeCLEAR": gstPowMonOutlet2StatusTimeCLEAR,
       "gstTempSensorTempCCLEAR": gstTempSensorTempCCLEAR,
       "gstTempSensorTempFCLEAR": gstTempSensorTempFCLEAR,
       "gstAirFlowSensorTempCCLEAR": gstAirFlowSensorTempCCLEAR,
       "gstAirFlowSensorTempFCLEAR": gstAirFlowSensorTempFCLEAR,
       "gstAirFlowSensorFlowCLEAR": gstAirFlowSensorFlowCLEAR,
       "gstAirFlowSensorHumidityCLEAR": gstAirFlowSensorHumidityCLEAR,
       "gstAirFlowSensorDewPointCCLEAR": gstAirFlowSensorDewPointCCLEAR,
       "gstAirFlowSensorDewPointFCLEAR": gstAirFlowSensorDewPointFCLEAR,
       "gstCtrl3ChDELTADeciAmpsACLEAR": gstCtrl3ChDELTADeciAmpsACLEAR,
       "gstCtrl3ChDELTADeciAmpsBCLEAR": gstCtrl3ChDELTADeciAmpsBCLEAR,
       "gstCtrl3ChDELTADeciAmpsCCLEAR": gstCtrl3ChDELTADeciAmpsCCLEAR,
       "gstCtrl3ChDELTAkWattHrsTotalCLEAR": gstCtrl3ChDELTAkWattHrsTotalCLEAR,
       "gstCtrl3ChDELTARealPowerTotalCLEAR": gstCtrl3ChDELTARealPowerTotalCLEAR,
       "gstCtrl3ChDELTAkWattHrsABCLEAR": gstCtrl3ChDELTAkWattHrsABCLEAR,
       "gstCtrl3ChDELTAVoltsABCLEAR": gstCtrl3ChDELTAVoltsABCLEAR,
       "gstCtrl3ChDELTAVoltPeakABCLEAR": gstCtrl3ChDELTAVoltPeakABCLEAR,
       "gstCtrl3ChDELTARealPowerABCLEAR": gstCtrl3ChDELTARealPowerABCLEAR,
       "gstCtrl3ChDELTAApparentPowerABCLEAR": gstCtrl3ChDELTAApparentPowerABCLEAR,
       "gstCtrl3ChDELTAPowerFactorABCLEAR": gstCtrl3ChDELTAPowerFactorABCLEAR,
       "gstCtrl3ChDELTAkWattHrsBCCLEAR": gstCtrl3ChDELTAkWattHrsBCCLEAR,
       "gstCtrl3ChDELTAVoltsBCCLEAR": gstCtrl3ChDELTAVoltsBCCLEAR,
       "gstCtrl3ChDELTAVoltPeakBCCLEAR": gstCtrl3ChDELTAVoltPeakBCCLEAR,
       "gstCtrl3ChDELTARealPowerBCCLEAR": gstCtrl3ChDELTARealPowerBCCLEAR,
       "gstCtrl3ChDELTAApparentPowerBCCLEAR": gstCtrl3ChDELTAApparentPowerBCCLEAR,
       "gstCtrl3ChDELTAPowerFactorBCCLEAR": gstCtrl3ChDELTAPowerFactorBCCLEAR,
       "gstCtrl3ChDELTAkWattHrsCACLEAR": gstCtrl3ChDELTAkWattHrsCACLEAR,
       "gstCtrl3ChDELTAVoltsCACLEAR": gstCtrl3ChDELTAVoltsCACLEAR,
       "gstCtrl3ChDELTAVoltPeakCACLEAR": gstCtrl3ChDELTAVoltPeakCACLEAR,
       "gstCtrl3ChDELTARealPowerCACLEAR": gstCtrl3ChDELTARealPowerCACLEAR,
       "gstCtrl3ChDELTAApparentPowerCACLEAR": gstCtrl3ChDELTAApparentPowerCACLEAR,
       "gstCtrl3ChDELTAPowerFactorCACLEAR": gstCtrl3ChDELTAPowerFactorCACLEAR,
       "gstDoorSensorStatusCLEAR": gstDoorSensorStatusCLEAR,
       "gstWaterSensorDampnessCLEAR": gstWaterSensorDampnessCLEAR,
       "gstCurrentMonitorDeciAmpsCLEAR": gstCurrentMonitorDeciAmpsCLEAR,
       "gstMillivoltMonitorMVCLEAR": gstMillivoltMonitorMVCLEAR,
       "gstPow3ChkWattHrsACLEAR": gstPow3ChkWattHrsACLEAR,
       "gstPow3ChVoltsACLEAR": gstPow3ChVoltsACLEAR,
       "gstPow3ChVoltMaxACLEAR": gstPow3ChVoltMaxACLEAR,
       "gstPow3ChVoltMinACLEAR": gstPow3ChVoltMinACLEAR,
       "gstPow3ChVoltPeakACLEAR": gstPow3ChVoltPeakACLEAR,
       "gstPow3ChDeciAmpsACLEAR": gstPow3ChDeciAmpsACLEAR,
       "gstPow3ChRealPowerACLEAR": gstPow3ChRealPowerACLEAR,
       "gstPow3ChApparentPowerACLEAR": gstPow3ChApparentPowerACLEAR,
       "gstPow3ChPowerFactorACLEAR": gstPow3ChPowerFactorACLEAR,
       "gstPow3ChkWattHrsBCLEAR": gstPow3ChkWattHrsBCLEAR,
       "gstPow3ChVoltsBCLEAR": gstPow3ChVoltsBCLEAR,
       "gstPow3ChVoltMaxBCLEAR": gstPow3ChVoltMaxBCLEAR,
       "gstPow3ChVoltMinBCLEAR": gstPow3ChVoltMinBCLEAR,
       "gstPow3ChVoltPeakBCLEAR": gstPow3ChVoltPeakBCLEAR,
       "gstPow3ChDeciAmpsBCLEAR": gstPow3ChDeciAmpsBCLEAR,
       "gstPow3ChRealPowerBCLEAR": gstPow3ChRealPowerBCLEAR,
       "gstPow3ChApparentPowerBCLEAR": gstPow3ChApparentPowerBCLEAR,
       "gstPow3ChPowerFactorBCLEAR": gstPow3ChPowerFactorBCLEAR,
       "gstPow3ChkWattHrsCCLEAR": gstPow3ChkWattHrsCCLEAR,
       "gstPow3ChVoltsCCLEAR": gstPow3ChVoltsCCLEAR,
       "gstPow3ChVoltMaxCCLEAR": gstPow3ChVoltMaxCCLEAR,
       "gstPow3ChVoltMinCCLEAR": gstPow3ChVoltMinCCLEAR,
       "gstPow3ChVoltPeakCCLEAR": gstPow3ChVoltPeakCCLEAR,
       "gstPow3ChDeciAmpsCCLEAR": gstPow3ChDeciAmpsCCLEAR,
       "gstPow3ChRealPowerCCLEAR": gstPow3ChRealPowerCCLEAR,
       "gstPow3ChApparentPowerCCLEAR": gstPow3ChApparentPowerCCLEAR,
       "gstPow3ChPowerFactorCCLEAR": gstPow3ChPowerFactorCCLEAR,
       "gstPow3ChkWattHrsTotalCLEAR": gstPow3ChkWattHrsTotalCLEAR,
       "gstPow3ChRealPowerTotalCLEAR": gstPow3ChRealPowerTotalCLEAR,
       "gstOutlet1StatusCLEAR": gstOutlet1StatusCLEAR,
       "gstOutlet2StatusCLEAR": gstOutlet2StatusCLEAR,
       "gstVsfcSetPointCCLEAR": gstVsfcSetPointCCLEAR,
       "gstVsfcSetPointFCLEAR": gstVsfcSetPointFCLEAR,
       "gstVsfcFanSpeedCLEAR": gstVsfcFanSpeedCLEAR,
       "gstVsfcIntTempCCLEAR": gstVsfcIntTempCCLEAR,
       "gstVsfcIntTempFCLEAR": gstVsfcIntTempFCLEAR,
       "gstVsfcExt1TempCCLEAR": gstVsfcExt1TempCCLEAR,
       "gstVsfcExt1TempFCLEAR": gstVsfcExt1TempFCLEAR,
       "gstVsfcExt2TempCCLEAR": gstVsfcExt2TempCCLEAR,
       "gstVsfcExt2TempFCLEAR": gstVsfcExt2TempFCLEAR,
       "gstVsfcExt3TempCCLEAR": gstVsfcExt3TempCCLEAR,
       "gstVsfcExt3TempFCLEAR": gstVsfcExt3TempFCLEAR,
       "gstVsfcExt4TempCCLEAR": gstVsfcExt4TempCCLEAR,
       "gstVsfcExt4TempFCLEAR": gstVsfcExt4TempFCLEAR,
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
       "gstCtrlGrpAmpsGCLEAR": gstCtrlGrpAmpsGCLEAR,
       "gstCtrlGrpAmpsHCLEAR": gstCtrlGrpAmpsHCLEAR,
       "gstCtrlGrpAmpsAVoltsCLEAR": gstCtrlGrpAmpsAVoltsCLEAR,
       "gstCtrlGrpAmpsBVoltsCLEAR": gstCtrlGrpAmpsBVoltsCLEAR,
       "gstCtrlGrpAmpsCVoltsCLEAR": gstCtrlGrpAmpsCVoltsCLEAR,
       "gstCtrlGrpAmpsDVoltsCLEAR": gstCtrlGrpAmpsDVoltsCLEAR,
       "gstCtrlGrpAmpsEVoltsCLEAR": gstCtrlGrpAmpsEVoltsCLEAR,
       "gstCtrlGrpAmpsFVoltsCLEAR": gstCtrlGrpAmpsFVoltsCLEAR,
       "gstCtrlGrpAmpsGVoltsCLEAR": gstCtrlGrpAmpsGVoltsCLEAR,
       "gstCtrlGrpAmpsHVoltsCLEAR": gstCtrlGrpAmpsHVoltsCLEAR,
       "gstCtrlGrpAmpsICLEAR": gstCtrlGrpAmpsICLEAR,
       "gstCtrlGrpAmpsJCLEAR": gstCtrlGrpAmpsJCLEAR,
       "gstCtrlGrpAmpsKCLEAR": gstCtrlGrpAmpsKCLEAR,
       "gstCtrlGrpAmpsLCLEAR": gstCtrlGrpAmpsLCLEAR,
       "gstCtrlGrpAmpsMCLEAR": gstCtrlGrpAmpsMCLEAR,
       "gstCtrlGrpAmpsNCLEAR": gstCtrlGrpAmpsNCLEAR,
       "gstCtrlGrpAmpsOCLEAR": gstCtrlGrpAmpsOCLEAR,
       "gstCtrlGrpAmpsPCLEAR": gstCtrlGrpAmpsPCLEAR,
       "gstCtrlGrpAmpsIVoltsCLEAR": gstCtrlGrpAmpsIVoltsCLEAR,
       "gstCtrlGrpAmpsJVoltsCLEAR": gstCtrlGrpAmpsJVoltsCLEAR,
       "gstCtrlGrpAmpsKVoltsCLEAR": gstCtrlGrpAmpsKVoltsCLEAR,
       "gstCtrlGrpAmpsLVoltsCLEAR": gstCtrlGrpAmpsLVoltsCLEAR,
       "gstCtrlGrpAmpsMVoltsCLEAR": gstCtrlGrpAmpsMVoltsCLEAR,
       "gstCtrlGrpAmpsNVoltsCLEAR": gstCtrlGrpAmpsNVoltsCLEAR,
       "gstCtrlGrpAmpsOVoltsCLEAR": gstCtrlGrpAmpsOVoltsCLEAR,
       "gstCtrlGrpAmpsPVoltsCLEAR": gstCtrlGrpAmpsPVoltsCLEAR,
       "gstCtrlOutletPendingCLEAR": gstCtrlOutletPendingCLEAR,
       "gstCtrlOutletDeciAmpsCLEAR": gstCtrlOutletDeciAmpsCLEAR,
       "gstCtrlOutletGroupCLEAR": gstCtrlOutletGroupCLEAR,
       "gstCtrlOutletUpDelayCLEAR": gstCtrlOutletUpDelayCLEAR,
       "gstCtrlOutletDwnDelayCLEAR": gstCtrlOutletDwnDelayCLEAR,
       "gstCtrlOutletRbtDurationCLEAR": gstCtrlOutletRbtDurationCLEAR,
       "gstCtrlOutletURLCLEAR": gstCtrlOutletURLCLEAR,
       "gstCtrlOutletPOAActionCLEAR": gstCtrlOutletPOAActionCLEAR,
       "gstCtrlOutletPOADelayCLEAR": gstCtrlOutletPOADelayCLEAR,
       "gstCtrlOutletkWattHrsCLEAR": gstCtrlOutletkWattHrsCLEAR,
       "gstCtrlOutletPowerCLEAR": gstCtrlOutletPowerCLEAR,
       "gstCtrlOutletRbtDelayCLEAR": gstCtrlOutletRbtDelayCLEAR,
       "gstCtrlOutletStatusTimeCLEAR": gstCtrlOutletStatusTimeCLEAR,
       "gstDewPointSensorTempCCLEAR": gstDewPointSensorTempCCLEAR,
       "gstDewPointSensorTempFCLEAR": gstDewPointSensorTempFCLEAR,
       "gstDewPointSensorHumidityCLEAR": gstDewPointSensorHumidityCLEAR,
       "gstDewPointSensorDewPointCCLEAR": gstDewPointSensorDewPointCCLEAR,
       "gstDewPointSensorDewPointFCLEAR": gstDewPointSensorDewPointFCLEAR,
       "gstDigitalSensorDigitalCLEAR": gstDigitalSensorDigitalCLEAR,
       "gstDstsVoltsACLEAR": gstDstsVoltsACLEAR,
       "gstDstsDeciAmpsACLEAR": gstDstsDeciAmpsACLEAR,
       "gstDstsVoltsBCLEAR": gstDstsVoltsBCLEAR,
       "gstDstsDeciAmpsBCLEAR": gstDstsDeciAmpsBCLEAR,
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
       "gstCtrl3ChIECkWattHrsACLEAR": gstCtrl3ChIECkWattHrsACLEAR,
       "gstCtrl3ChIECVoltsACLEAR": gstCtrl3ChIECVoltsACLEAR,
       "gstCtrl3ChIECVoltPeakACLEAR": gstCtrl3ChIECVoltPeakACLEAR,
       "gstCtrl3ChIECDeciAmpsACLEAR": gstCtrl3ChIECDeciAmpsACLEAR,
       "gstCtrl3ChIECDeciAmpsPeakACLEAR": gstCtrl3ChIECDeciAmpsPeakACLEAR,
       "gstCtrl3ChIECRealPowerACLEAR": gstCtrl3ChIECRealPowerACLEAR,
       "gstCtrl3ChIECApparentPowerACLEAR": gstCtrl3ChIECApparentPowerACLEAR,
       "gstCtrl3ChIECPowerFactorACLEAR": gstCtrl3ChIECPowerFactorACLEAR,
       "gstCtrl3ChIECkWattHrsBCLEAR": gstCtrl3ChIECkWattHrsBCLEAR,
       "gstCtrl3ChIECVoltsBCLEAR": gstCtrl3ChIECVoltsBCLEAR,
       "gstCtrl3ChIECVoltPeakBCLEAR": gstCtrl3ChIECVoltPeakBCLEAR,
       "gstCtrl3ChIECDeciAmpsBCLEAR": gstCtrl3ChIECDeciAmpsBCLEAR,
       "gstCtrl3ChIECDeciAmpsPeakBCLEAR": gstCtrl3ChIECDeciAmpsPeakBCLEAR,
       "gstCtrl3ChIECRealPowerBCLEAR": gstCtrl3ChIECRealPowerBCLEAR,
       "gstCtrl3ChIECApparentPowerBCLEAR": gstCtrl3ChIECApparentPowerBCLEAR,
       "gstCtrl3ChIECPowerFactorBCLEAR": gstCtrl3ChIECPowerFactorBCLEAR,
       "gstCtrl3ChIECkWattHrsCCLEAR": gstCtrl3ChIECkWattHrsCCLEAR,
       "gstCtrl3ChIECVoltsCCLEAR": gstCtrl3ChIECVoltsCCLEAR,
       "gstCtrl3ChIECVoltPeakCCLEAR": gstCtrl3ChIECVoltPeakCCLEAR,
       "gstCtrl3ChIECDeciAmpsCCLEAR": gstCtrl3ChIECDeciAmpsCCLEAR,
       "gstCtrl3ChIECDeciAmpsPeakCCLEAR": gstCtrl3ChIECDeciAmpsPeakCCLEAR,
       "gstCtrl3ChIECRealPowerCCLEAR": gstCtrl3ChIECRealPowerCCLEAR,
       "gstCtrl3ChIECApparentPowerCCLEAR": gstCtrl3ChIECApparentPowerCCLEAR,
       "gstCtrl3ChIECPowerFactorCCLEAR": gstCtrl3ChIECPowerFactorCCLEAR,
       "gstCtrl3ChIECkWattHrsTotalCLEAR": gstCtrl3ChIECkWattHrsTotalCLEAR,
       "gstCtrl3ChIECRealPowerTotalCLEAR": gstCtrl3ChIECRealPowerTotalCLEAR,
       "gstClimateRelayTempCCLEAR": gstClimateRelayTempCCLEAR,
       "gstClimateRelayTempFCLEAR": gstClimateRelayTempFCLEAR,
       "gstClimateRelayIO1CLEAR": gstClimateRelayIO1CLEAR,
       "gstClimateRelayIO2CLEAR": gstClimateRelayIO2CLEAR,
       "gstClimateRelayIO3CLEAR": gstClimateRelayIO3CLEAR,
       "gstClimateRelayIO4CLEAR": gstClimateRelayIO4CLEAR,
       "gstClimateRelayIO5CLEAR": gstClimateRelayIO5CLEAR,
       "gstClimateRelayIO6CLEAR": gstClimateRelayIO6CLEAR,
       "gstAirSpeedSwitchSensorAirSpeedCLEAR": gstAirSpeedSwitchSensorAirSpeedCLEAR,
       "gstIoExpanderIO1CLEAR": gstIoExpanderIO1CLEAR,
       "gstIoExpanderIO2CLEAR": gstIoExpanderIO2CLEAR,
       "gstIoExpanderIO3CLEAR": gstIoExpanderIO3CLEAR,
       "gstIoExpanderIO4CLEAR": gstIoExpanderIO4CLEAR,
       "gstIoExpanderIO5CLEAR": gstIoExpanderIO5CLEAR,
       "gstIoExpanderIO6CLEAR": gstIoExpanderIO6CLEAR,
       "gstIoExpanderIO7CLEAR": gstIoExpanderIO7CLEAR,
       "gstIoExpanderIO8CLEAR": gstIoExpanderIO8CLEAR,
       "gstIoExpanderIO9CLEAR": gstIoExpanderIO9CLEAR,
       "gstIoExpanderIO10CLEAR": gstIoExpanderIO10CLEAR,
       "gstIoExpanderIO11CLEAR": gstIoExpanderIO11CLEAR,
       "gstIoExpanderIO12CLEAR": gstIoExpanderIO12CLEAR,
       "gstIoExpanderIO13CLEAR": gstIoExpanderIO13CLEAR,
       "gstIoExpanderIO14CLEAR": gstIoExpanderIO14CLEAR,
       "gstIoExpanderIO15CLEAR": gstIoExpanderIO15CLEAR,
       "gstIoExpanderIO16CLEAR": gstIoExpanderIO16CLEAR,
       "gstIoExpanderIO17CLEAR": gstIoExpanderIO17CLEAR,
       "gstIoExpanderIO18CLEAR": gstIoExpanderIO18CLEAR,
       "gstIoExpanderIO19CLEAR": gstIoExpanderIO19CLEAR,
       "gstIoExpanderIO20CLEAR": gstIoExpanderIO20CLEAR,
       "gstIoExpanderIO21CLEAR": gstIoExpanderIO21CLEAR,
       "gstIoExpanderIO22CLEAR": gstIoExpanderIO22CLEAR,
       "gstIoExpanderIO23CLEAR": gstIoExpanderIO23CLEAR,
       "gstIoExpanderIO24CLEAR": gstIoExpanderIO24CLEAR,
       "gstIoExpanderIO25CLEAR": gstIoExpanderIO25CLEAR,
       "gstIoExpanderIO26CLEAR": gstIoExpanderIO26CLEAR,
       "gstIoExpanderIO27CLEAR": gstIoExpanderIO27CLEAR,
       "gstIoExpanderIO28CLEAR": gstIoExpanderIO28CLEAR,
       "gstIoExpanderIO29CLEAR": gstIoExpanderIO29CLEAR,
       "gstIoExpanderIO30CLEAR": gstIoExpanderIO30CLEAR,
       "gstIoExpanderIO31CLEAR": gstIoExpanderIO31CLEAR,
       "gstIoExpanderIO32CLEAR": gstIoExpanderIO32CLEAR,
       "gstT3hdSensorIntTempCCLEAR": gstT3hdSensorIntTempCCLEAR,
       "gstT3hdSensorIntTempFCLEAR": gstT3hdSensorIntTempFCLEAR,
       "gstT3hdSensorIntHumidityCLEAR": gstT3hdSensorIntHumidityCLEAR,
       "gstT3hdSensorIntDewPointCCLEAR": gstT3hdSensorIntDewPointCCLEAR,
       "gstT3hdSensorIntDewPointFCLEAR": gstT3hdSensorIntDewPointFCLEAR,
       "gstT3hdSensorExt1TempCCLEAR": gstT3hdSensorExt1TempCCLEAR,
       "gstT3hdSensorExt1TempFCLEAR": gstT3hdSensorExt1TempFCLEAR,
       "gstT3hdSensorExt2TempCCLEAR": gstT3hdSensorExt2TempCCLEAR,
       "gstT3hdSensorExt2TempFCLEAR": gstT3hdSensorExt2TempFCLEAR,
       "gstThdSensorTempCCLEAR": gstThdSensorTempCCLEAR,
       "gstThdSensorTempFCLEAR": gstThdSensorTempFCLEAR,
       "gstThdSensorHumidityCLEAR": gstThdSensorHumidityCLEAR,
       "gstThdSensorDewPointCCLEAR": gstThdSensorDewPointCCLEAR,
       "gstThdSensorDewPointFCLEAR": gstThdSensorDewPointFCLEAR,
       "gstPos60VdcSensorVoltageCLEAR": gstPos60VdcSensorVoltageCLEAR,
       "gstCtrl2CirTotkWattHrsTotCLEAR": gstCtrl2CirTotkWattHrsTotCLEAR,
       "gstCtrl2CirTotVoltsTotCLEAR": gstCtrl2CirTotVoltsTotCLEAR,
       "gstCtrl2CirTotVoltPeakTotCLEAR": gstCtrl2CirTotVoltPeakTotCLEAR,
       "gstCtrl2CirTotDeciAmpsTotCLEAR": gstCtrl2CirTotDeciAmpsTotCLEAR,
       "gstCtrl2CirTotDeciAmpsPeakTotCLEAR": gstCtrl2CirTotDeciAmpsPeakTotCLEAR,
       "gstCtrl2CirTotRealPowerTotCLEAR": gstCtrl2CirTotRealPowerTotCLEAR,
       "gstCtrl2CirTotApparentPowerTotCLEAR": gstCtrl2CirTotApparentPowerTotCLEAR,
       "gstCtrl2CirTotPowerFactorTotCLEAR": gstCtrl2CirTotPowerFactorTotCLEAR,
       "gstCtrl2CirTotkWattHrsACLEAR": gstCtrl2CirTotkWattHrsACLEAR,
       "gstCtrl2CirTotVoltsACLEAR": gstCtrl2CirTotVoltsACLEAR,
       "gstCtrl2CirTotVoltPeakACLEAR": gstCtrl2CirTotVoltPeakACLEAR,
       "gstCtrl2CirTotDeciAmpsACLEAR": gstCtrl2CirTotDeciAmpsACLEAR,
       "gstCtrl2CirTotDeciAmpsPeakACLEAR": gstCtrl2CirTotDeciAmpsPeakACLEAR,
       "gstCtrl2CirTotRealPowerACLEAR": gstCtrl2CirTotRealPowerACLEAR,
       "gstCtrl2CirTotApparentPowerACLEAR": gstCtrl2CirTotApparentPowerACLEAR,
       "gstCtrl2CirTotPowerFactorACLEAR": gstCtrl2CirTotPowerFactorACLEAR,
       "gstCtrl2CirTotkWattHrsBCLEAR": gstCtrl2CirTotkWattHrsBCLEAR,
       "gstCtrl2CirTotVoltsBCLEAR": gstCtrl2CirTotVoltsBCLEAR,
       "gstCtrl2CirTotVoltPeakBCLEAR": gstCtrl2CirTotVoltPeakBCLEAR,
       "gstCtrl2CirTotDeciAmpsBCLEAR": gstCtrl2CirTotDeciAmpsBCLEAR,
       "gstCtrl2CirTotDeciAmpsPeakBCLEAR": gstCtrl2CirTotDeciAmpsPeakBCLEAR,
       "gstCtrl2CirTotRealPowerBCLEAR": gstCtrl2CirTotRealPowerBCLEAR,
       "gstCtrl2CirTotApparentPowerBCLEAR": gstCtrl2CirTotApparentPowerBCLEAR,
       "gstCtrl2CirTotPowerFactorBCLEAR": gstCtrl2CirTotPowerFactorBCLEAR,
       "gstSc10ControlModeCLEAR": gstSc10ControlModeCLEAR,
       "gstSc10SetpointCCLEAR": gstSc10SetpointCCLEAR,
       "gstSc10SetpointFCLEAR": gstSc10SetpointFCLEAR,
       "gstSc10TempCCLEAR": gstSc10TempCCLEAR,
       "gstSc10TempFCLEAR": gstSc10TempFCLEAR,
       "gstSc10CapacityCLEAR": gstSc10CapacityCLEAR,
       "gstPowerDMDeciAmps1NOTIFY": gstPowerDMDeciAmps1NOTIFY,
       "gstPowerDMDeciAmps2NOTIFY": gstPowerDMDeciAmps2NOTIFY,
       "gstPowerDMDeciAmps3NOTIFY": gstPowerDMDeciAmps3NOTIFY,
       "gstPowerDMDeciAmps4NOTIFY": gstPowerDMDeciAmps4NOTIFY,
       "gstPowerDMDeciAmps5NOTIFY": gstPowerDMDeciAmps5NOTIFY,
       "gstPowerDMDeciAmps6NOTIFY": gstPowerDMDeciAmps6NOTIFY,
       "gstPowerDMDeciAmps7NOTIFY": gstPowerDMDeciAmps7NOTIFY,
       "gstPowerDMDeciAmps8NOTIFY": gstPowerDMDeciAmps8NOTIFY,
       "gstPowerDMDeciAmps9NOTIFY": gstPowerDMDeciAmps9NOTIFY,
       "gstPowerDMDeciAmps10NOTIFY": gstPowerDMDeciAmps10NOTIFY,
       "gstPowerDMDeciAmps11NOTIFY": gstPowerDMDeciAmps11NOTIFY,
       "gstPowerDMDeciAmps12NOTIFY": gstPowerDMDeciAmps12NOTIFY,
       "gstPowerDMDeciAmps13NOTIFY": gstPowerDMDeciAmps13NOTIFY,
       "gstPowerDMDeciAmps14NOTIFY": gstPowerDMDeciAmps14NOTIFY,
       "gstPowerDMDeciAmps15NOTIFY": gstPowerDMDeciAmps15NOTIFY,
       "gstPowerDMDeciAmps16NOTIFY": gstPowerDMDeciAmps16NOTIFY,
       "gstPowerDMDeciAmps17NOTIFY": gstPowerDMDeciAmps17NOTIFY,
       "gstPowerDMDeciAmps18NOTIFY": gstPowerDMDeciAmps18NOTIFY,
       "gstPowerDMDeciAmps19NOTIFY": gstPowerDMDeciAmps19NOTIFY,
       "gstPowerDMDeciAmps20NOTIFY": gstPowerDMDeciAmps20NOTIFY,
       "gstPowerDMDeciAmps21NOTIFY": gstPowerDMDeciAmps21NOTIFY,
       "gstPowerDMDeciAmps22NOTIFY": gstPowerDMDeciAmps22NOTIFY,
       "gstPowerDMDeciAmps23NOTIFY": gstPowerDMDeciAmps23NOTIFY,
       "gstPowerDMDeciAmps24NOTIFY": gstPowerDMDeciAmps24NOTIFY,
       "gstPowerDMDeciAmps25NOTIFY": gstPowerDMDeciAmps25NOTIFY,
       "gstPowerDMDeciAmps26NOTIFY": gstPowerDMDeciAmps26NOTIFY,
       "gstPowerDMDeciAmps27NOTIFY": gstPowerDMDeciAmps27NOTIFY,
       "gstPowerDMDeciAmps28NOTIFY": gstPowerDMDeciAmps28NOTIFY,
       "gstPowerDMDeciAmps29NOTIFY": gstPowerDMDeciAmps29NOTIFY,
       "gstPowerDMDeciAmps30NOTIFY": gstPowerDMDeciAmps30NOTIFY,
       "gstPowerDMDeciAmps31NOTIFY": gstPowerDMDeciAmps31NOTIFY,
       "gstPowerDMDeciAmps32NOTIFY": gstPowerDMDeciAmps32NOTIFY,
       "gstPowerDMDeciAmps33NOTIFY": gstPowerDMDeciAmps33NOTIFY,
       "gstPowerDMDeciAmps34NOTIFY": gstPowerDMDeciAmps34NOTIFY,
       "gstPowerDMDeciAmps35NOTIFY": gstPowerDMDeciAmps35NOTIFY,
       "gstPowerDMDeciAmps36NOTIFY": gstPowerDMDeciAmps36NOTIFY,
       "gstPowerDMDeciAmps37NOTIFY": gstPowerDMDeciAmps37NOTIFY,
       "gstPowerDMDeciAmps38NOTIFY": gstPowerDMDeciAmps38NOTIFY,
       "gstPowerDMDeciAmps39NOTIFY": gstPowerDMDeciAmps39NOTIFY,
       "gstPowerDMDeciAmps40NOTIFY": gstPowerDMDeciAmps40NOTIFY,
       "gstPowerDMDeciAmps41NOTIFY": gstPowerDMDeciAmps41NOTIFY,
       "gstPowerDMDeciAmps42NOTIFY": gstPowerDMDeciAmps42NOTIFY,
       "gstPowerDMDeciAmps43NOTIFY": gstPowerDMDeciAmps43NOTIFY,
       "gstPowerDMDeciAmps44NOTIFY": gstPowerDMDeciAmps44NOTIFY,
       "gstPowerDMDeciAmps45NOTIFY": gstPowerDMDeciAmps45NOTIFY,
       "gstPowerDMDeciAmps46NOTIFY": gstPowerDMDeciAmps46NOTIFY,
       "gstPowerDMDeciAmps47NOTIFY": gstPowerDMDeciAmps47NOTIFY,
       "gstPowerDMDeciAmps48NOTIFY": gstPowerDMDeciAmps48NOTIFY,
       "gstPowerDMDeciAmps1CLEAR": gstPowerDMDeciAmps1CLEAR,
       "gstPowerDMDeciAmps2CLEAR": gstPowerDMDeciAmps2CLEAR,
       "gstPowerDMDeciAmps3CLEAR": gstPowerDMDeciAmps3CLEAR,
       "gstPowerDMDeciAmps4CLEAR": gstPowerDMDeciAmps4CLEAR,
       "gstPowerDMDeciAmps5CLEAR": gstPowerDMDeciAmps5CLEAR,
       "gstPowerDMDeciAmps6CLEAR": gstPowerDMDeciAmps6CLEAR,
       "gstPowerDMDeciAmps7CLEAR": gstPowerDMDeciAmps7CLEAR,
       "gstPowerDMDeciAmps8CLEAR": gstPowerDMDeciAmps8CLEAR,
       "gstPowerDMDeciAmps9CLEAR": gstPowerDMDeciAmps9CLEAR,
       "gstPowerDMDeciAmps10CLEAR": gstPowerDMDeciAmps10CLEAR,
       "gstPowerDMDeciAmps11CLEAR": gstPowerDMDeciAmps11CLEAR,
       "gstPowerDMDeciAmps12CLEAR": gstPowerDMDeciAmps12CLEAR,
       "gstPowerDMDeciAmps13CLEAR": gstPowerDMDeciAmps13CLEAR,
       "gstPowerDMDeciAmps14CLEAR": gstPowerDMDeciAmps14CLEAR,
       "gstPowerDMDeciAmps15CLEAR": gstPowerDMDeciAmps15CLEAR,
       "gstPowerDMDeciAmps16CLEAR": gstPowerDMDeciAmps16CLEAR,
       "gstPowerDMDeciAmps17CLEAR": gstPowerDMDeciAmps17CLEAR,
       "gstPowerDMDeciAmps18CLEAR": gstPowerDMDeciAmps18CLEAR,
       "gstPowerDMDeciAmps19CLEAR": gstPowerDMDeciAmps19CLEAR,
       "gstPowerDMDeciAmps20CLEAR": gstPowerDMDeciAmps20CLEAR,
       "gstPowerDMDeciAmps21CLEAR": gstPowerDMDeciAmps21CLEAR,
       "gstPowerDMDeciAmps22CLEAR": gstPowerDMDeciAmps22CLEAR,
       "gstPowerDMDeciAmps23CLEAR": gstPowerDMDeciAmps23CLEAR,
       "gstPowerDMDeciAmps24CLEAR": gstPowerDMDeciAmps24CLEAR,
       "gstPowerDMDeciAmps25CLEAR": gstPowerDMDeciAmps25CLEAR,
       "gstPowerDMDeciAmps26CLEAR": gstPowerDMDeciAmps26CLEAR,
       "gstPowerDMDeciAmps27CLEAR": gstPowerDMDeciAmps27CLEAR,
       "gstPowerDMDeciAmps28CLEAR": gstPowerDMDeciAmps28CLEAR,
       "gstPowerDMDeciAmps29CLEAR": gstPowerDMDeciAmps29CLEAR,
       "gstPowerDMDeciAmps30CLEAR": gstPowerDMDeciAmps30CLEAR,
       "gstPowerDMDeciAmps31CLEAR": gstPowerDMDeciAmps31CLEAR,
       "gstPowerDMDeciAmps32CLEAR": gstPowerDMDeciAmps32CLEAR,
       "gstPowerDMDeciAmps33CLEAR": gstPowerDMDeciAmps33CLEAR,
       "gstPowerDMDeciAmps34CLEAR": gstPowerDMDeciAmps34CLEAR,
       "gstPowerDMDeciAmps35CLEAR": gstPowerDMDeciAmps35CLEAR,
       "gstPowerDMDeciAmps36CLEAR": gstPowerDMDeciAmps36CLEAR,
       "gstPowerDMDeciAmps37CLEAR": gstPowerDMDeciAmps37CLEAR,
       "gstPowerDMDeciAmps38CLEAR": gstPowerDMDeciAmps38CLEAR,
       "gstPowerDMDeciAmps39CLEAR": gstPowerDMDeciAmps39CLEAR,
       "gstPowerDMDeciAmps40CLEAR": gstPowerDMDeciAmps40CLEAR,
       "gstPowerDMDeciAmps41CLEAR": gstPowerDMDeciAmps41CLEAR,
       "gstPowerDMDeciAmps42CLEAR": gstPowerDMDeciAmps42CLEAR,
       "gstPowerDMDeciAmps43CLEAR": gstPowerDMDeciAmps43CLEAR,
       "gstPowerDMDeciAmps44CLEAR": gstPowerDMDeciAmps44CLEAR,
       "gstPowerDMDeciAmps45CLEAR": gstPowerDMDeciAmps45CLEAR,
       "gstPowerDMDeciAmps46CLEAR": gstPowerDMDeciAmps46CLEAR,
       "gstPowerDMDeciAmps47CLEAR": gstPowerDMDeciAmps47CLEAR,
       "gstPowerDMDeciAmps48CLEAR": gstPowerDMDeciAmps48CLEAR}
)
