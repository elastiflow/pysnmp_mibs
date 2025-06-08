# SNMP MIB module (ODS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/opengate_29414/ODS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:53:41 2025
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

opengate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29414)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ods_ObjectIdentity = ObjectIdentity
ods = _Ods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29414, 1)
)
_DeviceInfo_ObjectIdentity = ObjectIdentity
deviceInfo = _DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1)
)
_ProductTitle_Type = DisplayString
_ProductTitle_Object = MibScalar
productTitle = _ProductTitle_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 1),
    _ProductTitle_Type()
)
productTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productTitle.setStatus("current")
_ProductVersion_Type = DisplayString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 2),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")
_ProductFriendlyName_Type = DisplayString
_ProductFriendlyName_Object = MibScalar
productFriendlyName = _ProductFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 3),
    _ProductFriendlyName_Type()
)
productFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productFriendlyName.setStatus("current")
_ProductMacAddress_Type = DisplayString
_ProductMacAddress_Object = MibScalar
productMacAddress = _ProductMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 4),
    _ProductMacAddress_Type()
)
productMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMacAddress.setStatus("current")
_ProductUrl_Type = DisplayString
_ProductUrl_Object = MibScalar
productUrl = _ProductUrl_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 6),
    _AlarmTripType_Type()
)
alarmTripType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTripType.setStatus("current")
_ProductHardware_Type = DisplayString
_ProductHardware_Object = MibScalar
productHardware = _ProductHardware_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 7),
    _ProductHardware_Type()
)
productHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productHardware.setStatus("current")
_SensorCountsBase_ObjectIdentity = ObjectIdentity
sensorCountsBase = _SensorCountsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 8)
)
_SensorCounts_ObjectIdentity = ObjectIdentity
sensorCounts = _SensorCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 8, 1)
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 8, 1, 2),
    _ClimateCount_Type()
)
climateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateCount.setStatus("current")


class _DewPointSensorCount_Type(Integer32):
    """Custom type dewPointSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DewPointSensorCount_Type.__name__ = "Integer32"
_DewPointSensorCount_Object = MibScalar
dewPointSensorCount = _DewPointSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 8, 1, 3),
    _DewPointSensorCount_Type()
)
dewPointSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorCount.setStatus("current")


class _FancontrolCount_Type(Integer32):
    """Custom type fancontrolCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_FancontrolCount_Type.__name__ = "Integer32"
_FancontrolCount_Object = MibScalar
fancontrolCount = _FancontrolCount_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 8, 1, 4),
    _FancontrolCount_Type()
)
fancontrolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolCount.setStatus("current")


class _TempSensorCount_Type(Integer32):
    """Custom type tempSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TempSensorCount_Type.__name__ = "Integer32"
_TempSensorCount_Object = MibScalar
tempSensorCount = _TempSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 8, 1, 5),
    _TempSensorCount_Type()
)
tempSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorCount.setStatus("current")


class _FlowcontrolCount_Type(Integer32):
    """Custom type flowcontrolCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_FlowcontrolCount_Type.__name__ = "Integer32"
_FlowcontrolCount_Object = MibScalar
flowcontrolCount = _FlowcontrolCount_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 8, 1, 6),
    _FlowcontrolCount_Type()
)
flowcontrolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolCount.setStatus("current")


class _PowerDMCount_Type(Integer32):
    """Custom type powerDMCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PowerDMCount_Type.__name__ = "Integer32"
_PowerDMCount_Object = MibScalar
powerDMCount = _PowerDMCount_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 1, 8, 1, 7),
    _PowerDMCount_Type()
)
powerDMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMCount.setStatus("current")
_ClimateTable_Object = MibTable
climateTable = _ClimateTable_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2)
)
if mibBuilder.loadTexts:
    climateTable.setStatus("current")
_ClimateEntry_Object = MibTableRow
climateEntry = _ClimateEntry_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1)
)
climateEntry.setIndexNames(
    (0, "ODS-MIB", "climateIndex"),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 1),
    _ClimateIndex_Type()
)
climateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    climateIndex.setStatus("current")
_ClimateSerial_Type = DisplayString
_ClimateSerial_Object = MibTableColumn
climateSerial = _ClimateSerial_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 2),
    _ClimateSerial_Type()
)
climateSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateSerial.setStatus("current")
_ClimateName_Type = DisplayString
_ClimateName_Object = MibTableColumn
climateName = _ClimateName_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 3),
    _ClimateName_Type()
)
climateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateName.setStatus("current")
_ClimateAvail_Type = Gauge32
_ClimateAvail_Object = MibTableColumn
climateAvail = _ClimateAvail_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 2, 1, 13),
    _ClimateIO3_Type()
)
climateIO3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    climateIO3.setStatus("current")
_DewPointSensorTable_Object = MibTable
dewPointSensorTable = _DewPointSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 3)
)
if mibBuilder.loadTexts:
    dewPointSensorTable.setStatus("current")
_DewPointSensorEntry_Object = MibTableRow
dewPointSensorEntry = _DewPointSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 3, 1)
)
dewPointSensorEntry.setIndexNames(
    (0, "ODS-MIB", "dewPointSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 3, 1, 1),
    _DewPointSensorIndex_Type()
)
dewPointSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dewPointSensorIndex.setStatus("current")
_DewPointSensorSerial_Type = DisplayString
_DewPointSensorSerial_Object = MibTableColumn
dewPointSensorSerial = _DewPointSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 3, 1, 2),
    _DewPointSensorSerial_Type()
)
dewPointSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorSerial.setStatus("current")
_DewPointSensorName_Type = DisplayString
_DewPointSensorName_Object = MibTableColumn
dewPointSensorName = _DewPointSensorName_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 3, 1, 3),
    _DewPointSensorName_Type()
)
dewPointSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorName.setStatus("current")
_DewPointSensorAvail_Type = Gauge32
_DewPointSensorAvail_Object = MibTableColumn
dewPointSensorAvail = _DewPointSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 3, 1, 5),
    _DewPointSensorTempC_Type()
)
dewPointSensorTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorTempC.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorTempC.setUnits("Temperature reading in C")


class _DewPointSensorTempF_Type(Integer32):
    """Custom type dewPointSensorTempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_DewPointSensorTempF_Type.__name__ = "Integer32"
_DewPointSensorTempF_Object = MibTableColumn
dewPointSensorTempF = _DewPointSensorTempF_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 3, 1, 6),
    _DewPointSensorTempF_Type()
)
dewPointSensorTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorTempF.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorTempF.setUnits("Temperature reading in F")


class _DewPointSensorHumidity_Type(Integer32):
    """Custom type dewPointSensorHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DewPointSensorHumidity_Type.__name__ = "Integer32"
_DewPointSensorHumidity_Object = MibTableColumn
dewPointSensorHumidity = _DewPointSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 3, 1, 7),
    _DewPointSensorHumidity_Type()
)
dewPointSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorHumidity.setUnits("Humidity reading")


class _DewPointSensorDewpointC_Type(Integer32):
    """Custom type dewPointSensorDewpointC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DewPointSensorDewpointC_Type.__name__ = "Integer32"
_DewPointSensorDewpointC_Object = MibTableColumn
dewPointSensorDewpointC = _DewPointSensorDewpointC_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 3, 1, 8),
    _DewPointSensorDewpointC_Type()
)
dewPointSensorDewpointC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorDewpointC.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorDewpointC.setUnits("Dew point reading")


class _DewPointSensorDewpointF_Type(Integer32):
    """Custom type dewPointSensorDewpointF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DewPointSensorDewpointF_Type.__name__ = "Integer32"
_DewPointSensorDewpointF_Object = MibTableColumn
dewPointSensorDewpointF = _DewPointSensorDewpointF_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 3, 1, 9),
    _DewPointSensorDewpointF_Type()
)
dewPointSensorDewpointF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorDewpointF.setStatus("current")
if mibBuilder.loadTexts:
    dewPointSensorDewpointF.setUnits("Dew point reading")
_FancontrolTable_Object = MibTable
fancontrolTable = _FancontrolTable_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4)
)
if mibBuilder.loadTexts:
    fancontrolTable.setStatus("current")
_FancontrolEntry_Object = MibTableRow
fancontrolEntry = _FancontrolEntry_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1)
)
fancontrolEntry.setIndexNames(
    (0, "ODS-MIB", "fancontrolIndex"),
)
if mibBuilder.loadTexts:
    fancontrolEntry.setStatus("current")


class _FancontrolIndex_Type(Integer32):
    """Custom type fancontrolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_FancontrolIndex_Type.__name__ = "Integer32"
_FancontrolIndex_Object = MibTableColumn
fancontrolIndex = _FancontrolIndex_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 1),
    _FancontrolIndex_Type()
)
fancontrolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fancontrolIndex.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolIndex.setUnits("Table entry index value")
_FancontrolSerial_Type = DisplayString
_FancontrolSerial_Object = MibTableColumn
fancontrolSerial = _FancontrolSerial_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 2),
    _FancontrolSerial_Type()
)
fancontrolSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolSerial.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolSerial.setUnits("Serial Number")
_FancontrolName_Type = DisplayString
_FancontrolName_Object = MibTableColumn
fancontrolName = _FancontrolName_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 3),
    _FancontrolName_Type()
)
fancontrolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolName.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolName.setUnits("Friendly Name")
_FancontrolAvail_Type = Gauge32
_FancontrolAvail_Object = MibTableColumn
fancontrolAvail = _FancontrolAvail_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 4),
    _FancontrolAvail_Type()
)
fancontrolAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolAvail.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolAvail.setUnits("Is device currently plugged in?")


class _FancontrolTempCreturnA_Type(Integer32):
    """Custom type fancontrolTempCreturnA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 100),
    )


_FancontrolTempCreturnA_Type.__name__ = "Integer32"
_FancontrolTempCreturnA_Object = MibTableColumn
fancontrolTempCreturnA = _FancontrolTempCreturnA_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 5),
    _FancontrolTempCreturnA_Type()
)
fancontrolTempCreturnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolTempCreturnA.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolTempCreturnA.setUnits("Celsius temperature of return air on fan A")


class _FancontrolTempFreturnA_Type(Integer32):
    """Custom type fancontrolTempFreturnA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 212),
    )


_FancontrolTempFreturnA_Type.__name__ = "Integer32"
_FancontrolTempFreturnA_Object = MibTableColumn
fancontrolTempFreturnA = _FancontrolTempFreturnA_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 6),
    _FancontrolTempFreturnA_Type()
)
fancontrolTempFreturnA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolTempFreturnA.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolTempFreturnA.setUnits("Fahrenheit temperature of return air on fan A")


class _FancontrolTempCreturnB_Type(Integer32):
    """Custom type fancontrolTempCreturnB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 100),
    )


_FancontrolTempCreturnB_Type.__name__ = "Integer32"
_FancontrolTempCreturnB_Object = MibTableColumn
fancontrolTempCreturnB = _FancontrolTempCreturnB_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 7),
    _FancontrolTempCreturnB_Type()
)
fancontrolTempCreturnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolTempCreturnB.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolTempCreturnB.setUnits("Celsius temperature of return air on fan B")


class _FancontrolTempFreturnB_Type(Integer32):
    """Custom type fancontrolTempFreturnB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 212),
    )


_FancontrolTempFreturnB_Type.__name__ = "Integer32"
_FancontrolTempFreturnB_Object = MibTableColumn
fancontrolTempFreturnB = _FancontrolTempFreturnB_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 8),
    _FancontrolTempFreturnB_Type()
)
fancontrolTempFreturnB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolTempFreturnB.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolTempFreturnB.setUnits("Fahrenheit temperature of return air on fan B")
_FancontrolRpmFanA_Type = Gauge32
_FancontrolRpmFanA_Object = MibTableColumn
fancontrolRpmFanA = _FancontrolRpmFanA_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 9),
    _FancontrolRpmFanA_Type()
)
fancontrolRpmFanA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolRpmFanA.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolRpmFanA.setUnits("RPM of fan A")
_FancontrolRpmFanB_Type = Gauge32
_FancontrolRpmFanB_Object = MibTableColumn
fancontrolRpmFanB = _FancontrolRpmFanB_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 10),
    _FancontrolRpmFanB_Type()
)
fancontrolRpmFanB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolRpmFanB.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolRpmFanB.setUnits("RPM of fan B")


class _FancontrolCapacityA_Type(Integer32):
    """Custom type fancontrolCapacityA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FancontrolCapacityA_Type.__name__ = "Integer32"
_FancontrolCapacityA_Object = MibTableColumn
fancontrolCapacityA = _FancontrolCapacityA_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 11),
    _FancontrolCapacityA_Type()
)
fancontrolCapacityA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolCapacityA.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolCapacityA.setUnits("Capacity of fan A")


class _FancontrolCapacityB_Type(Integer32):
    """Custom type fancontrolCapacityB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FancontrolCapacityB_Type.__name__ = "Integer32"
_FancontrolCapacityB_Object = MibTableColumn
fancontrolCapacityB = _FancontrolCapacityB_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 12),
    _FancontrolCapacityB_Type()
)
fancontrolCapacityB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolCapacityB.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolCapacityB.setUnits("Capacity of fan B")


class _FancontrolPressErr_Type(Integer32):
    """Custom type fancontrolPressErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_FancontrolPressErr_Type.__name__ = "Integer32"
_FancontrolPressErr_Object = MibTableColumn
fancontrolPressErr = _FancontrolPressErr_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 13),
    _FancontrolPressErr_Type()
)
fancontrolPressErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolPressErr.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolPressErr.setUnits("Pressure Errorm x1000")


class _FancontrolPressDiff_Type(Integer32):
    """Custom type fancontrolPressDiff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_FancontrolPressDiff_Type.__name__ = "Integer32"
_FancontrolPressDiff_Object = MibTableColumn
fancontrolPressDiff = _FancontrolPressDiff_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 14),
    _FancontrolPressDiff_Type()
)
fancontrolPressDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolPressDiff.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolPressDiff.setUnits("Pressure Difference x1000")


class _FancontrolSetPoint_Type(Integer32):
    """Custom type fancontrolSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_FancontrolSetPoint_Type.__name__ = "Integer32"
_FancontrolSetPoint_Object = MibTableColumn
fancontrolSetPoint = _FancontrolSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 15),
    _FancontrolSetPoint_Type()
)
fancontrolSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolSetPoint.setUnits("Pressure Set Point x1000")
_FancontrolCFM_Type = Gauge32
_FancontrolCFM_Object = MibTableColumn
fancontrolCFM = _FancontrolCFM_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 16),
    _FancontrolCFM_Type()
)
fancontrolCFM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolCFM.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolCFM.setUnits("Cubic Feet per minute of system air")
_FancontrolMCH_Type = Gauge32
_FancontrolMCH_Object = MibTableColumn
fancontrolMCH = _FancontrolMCH_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 17),
    _FancontrolMCH_Type()
)
fancontrolMCH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolMCH.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolMCH.setUnits("Meters cubed per hour of system air")


class _FancontrolTempCreturn_Type(Integer32):
    """Custom type fancontrolTempCreturn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 100),
    )


_FancontrolTempCreturn_Type.__name__ = "Integer32"
_FancontrolTempCreturn_Object = MibTableColumn
fancontrolTempCreturn = _FancontrolTempCreturn_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 18),
    _FancontrolTempCreturn_Type()
)
fancontrolTempCreturn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolTempCreturn.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolTempCreturn.setUnits("Higher temp of fan A or B")


class _FancontrolTempFreturn_Type(Integer32):
    """Custom type fancontrolTempFreturn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 212),
    )


_FancontrolTempFreturn_Type.__name__ = "Integer32"
_FancontrolTempFreturn_Object = MibTableColumn
fancontrolTempFreturn = _FancontrolTempFreturn_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 19),
    _FancontrolTempFreturn_Type()
)
fancontrolTempFreturn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolTempFreturn.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolTempFreturn.setUnits("Higher temp of fan A or B")


class _FancontrolCapacity_Type(Integer32):
    """Custom type fancontrolCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FancontrolCapacity_Type.__name__ = "Integer32"
_FancontrolCapacity_Object = MibTableColumn
fancontrolCapacity = _FancontrolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 20),
    _FancontrolCapacity_Type()
)
fancontrolCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolCapacity.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolCapacity.setUnits("Total Capacity")
_FancontrolFanMissing_Type = Gauge32
_FancontrolFanMissing_Object = MibTableColumn
fancontrolFanMissing = _FancontrolFanMissing_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 21),
    _FancontrolFanMissing_Type()
)
fancontrolFanMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolFanMissing.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolFanMissing.setUnits("Fan Missing Error")
_FancontrolFanMismatch_Type = Gauge32
_FancontrolFanMismatch_Object = MibTableColumn
fancontrolFanMismatch = _FancontrolFanMismatch_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 22),
    _FancontrolFanMismatch_Type()
)
fancontrolFanMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolFanMismatch.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolFanMismatch.setUnits("Fan Mismatch Error")
_FancontrolFanErrorA_Type = Gauge32
_FancontrolFanErrorA_Object = MibTableColumn
fancontrolFanErrorA = _FancontrolFanErrorA_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 23),
    _FancontrolFanErrorA_Type()
)
fancontrolFanErrorA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolFanErrorA.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolFanErrorA.setUnits("Fan Cartridge A Error")
_FancontrolFanErrorB_Type = Gauge32
_FancontrolFanErrorB_Object = MibTableColumn
fancontrolFanErrorB = _FancontrolFanErrorB_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 24),
    _FancontrolFanErrorB_Type()
)
fancontrolFanErrorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolFanErrorB.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolFanErrorB.setUnits("Fan Cartridge B Error")
_FancontrolTempBus1_Type = Gauge32
_FancontrolTempBus1_Object = MibTableColumn
fancontrolTempBus1 = _FancontrolTempBus1_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 25),
    _FancontrolTempBus1_Type()
)
fancontrolTempBus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolTempBus1.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolTempBus1.setUnits("Disconnected External Sensor")
_FancontrolPowerFeed_Type = Gauge32
_FancontrolPowerFeed_Object = MibTableColumn
fancontrolPowerFeed = _FancontrolPowerFeed_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 26),
    _FancontrolPowerFeed_Type()
)
fancontrolPowerFeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolPowerFeed.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolPowerFeed.setUnits("A/B Feed Error")
_FancontrolFanEndofLife_Type = Gauge32
_FancontrolFanEndofLife_Object = MibTableColumn
fancontrolFanEndofLife = _FancontrolFanEndofLife_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 27),
    _FancontrolFanEndofLife_Type()
)
fancontrolFanEndofLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fancontrolFanEndofLife.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolFanEndofLife.setUnits("Fan End of Life")


class _FancontrolTargetCapacity_Type(Integer32):
    """Custom type fancontrolTargetCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_FancontrolTargetCapacity_Type.__name__ = "Integer32"
_FancontrolTargetCapacity_Object = MibTableColumn
fancontrolTargetCapacity = _FancontrolTargetCapacity_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 4, 1, 28),
    _FancontrolTargetCapacity_Type()
)
fancontrolTargetCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fancontrolTargetCapacity.setStatus("current")
if mibBuilder.loadTexts:
    fancontrolTargetCapacity.setUnits("Target Capacity")
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 5)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("current")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 5, 1)
)
tempSensorEntry.setIndexNames(
    (0, "ODS-MIB", "tempSensorIndex"),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 5, 1, 1),
    _TempSensorIndex_Type()
)
tempSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempSensorIndex.setStatus("current")
_TempSensorSerial_Type = DisplayString
_TempSensorSerial_Object = MibTableColumn
tempSensorSerial = _TempSensorSerial_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 5, 1, 2),
    _TempSensorSerial_Type()
)
tempSensorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorSerial.setStatus("current")
_TempSensorName_Type = DisplayString
_TempSensorName_Object = MibTableColumn
tempSensorName = _TempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 5, 1, 3),
    _TempSensorName_Type()
)
tempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorName.setStatus("current")
_TempSensorAvail_Type = Gauge32
_TempSensorAvail_Object = MibTableColumn
tempSensorAvail = _TempSensorAvail_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 5, 1, 5),
    _TempSensorTempC_Type()
)
tempSensorTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorTempC.setStatus("current")
if mibBuilder.loadTexts:
    tempSensorTempC.setUnits("Temperature in Celsius")


class _TempSensorTempF_Type(Integer32):
    """Custom type tempSensorTempF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 212),
    )


_TempSensorTempF_Type.__name__ = "Integer32"
_TempSensorTempF_Object = MibTableColumn
tempSensorTempF = _TempSensorTempF_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 5, 1, 6),
    _TempSensorTempF_Type()
)
tempSensorTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorTempF.setStatus("current")
if mibBuilder.loadTexts:
    tempSensorTempF.setUnits("Temperature in Fahrenheit")
_FlowcontrolTable_Object = MibTable
flowcontrolTable = _FlowcontrolTable_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6)
)
if mibBuilder.loadTexts:
    flowcontrolTable.setStatus("current")
_FlowcontrolEntry_Object = MibTableRow
flowcontrolEntry = _FlowcontrolEntry_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1)
)
flowcontrolEntry.setIndexNames(
    (0, "ODS-MIB", "flowcontrolIndex"),
)
if mibBuilder.loadTexts:
    flowcontrolEntry.setStatus("current")


class _FlowcontrolIndex_Type(Integer32):
    """Custom type flowcontrolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_FlowcontrolIndex_Type.__name__ = "Integer32"
_FlowcontrolIndex_Object = MibTableColumn
flowcontrolIndex = _FlowcontrolIndex_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 1),
    _FlowcontrolIndex_Type()
)
flowcontrolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flowcontrolIndex.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolIndex.setUnits("Table entry index value")
_FlowcontrolSerial_Type = DisplayString
_FlowcontrolSerial_Object = MibTableColumn
flowcontrolSerial = _FlowcontrolSerial_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 2),
    _FlowcontrolSerial_Type()
)
flowcontrolSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolSerial.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolSerial.setUnits("Serial Number")
_FlowcontrolName_Type = DisplayString
_FlowcontrolName_Object = MibTableColumn
flowcontrolName = _FlowcontrolName_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 3),
    _FlowcontrolName_Type()
)
flowcontrolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolName.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolName.setUnits("Friendly Name")
_FlowcontrolAvail_Type = Gauge32
_FlowcontrolAvail_Object = MibTableColumn
flowcontrolAvail = _FlowcontrolAvail_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 4),
    _FlowcontrolAvail_Type()
)
flowcontrolAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolAvail.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolAvail.setUnits("Is device currently plugged in?")
_FlowcontrolRpmFan_Type = Gauge32
_FlowcontrolRpmFan_Object = MibTableColumn
flowcontrolRpmFan = _FlowcontrolRpmFan_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 5),
    _FlowcontrolRpmFan_Type()
)
flowcontrolRpmFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolRpmFan.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolRpmFan.setUnits("RPM of fan")


class _FlowcontrolCapacity_Type(Integer32):
    """Custom type flowcontrolCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FlowcontrolCapacity_Type.__name__ = "Integer32"
_FlowcontrolCapacity_Object = MibTableColumn
flowcontrolCapacity = _FlowcontrolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 6),
    _FlowcontrolCapacity_Type()
)
flowcontrolCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolCapacity.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolCapacity.setUnits("Total Capacity")


class _FlowcontrolPressErr_Type(Integer32):
    """Custom type flowcontrolPressErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_FlowcontrolPressErr_Type.__name__ = "Integer32"
_FlowcontrolPressErr_Object = MibTableColumn
flowcontrolPressErr = _FlowcontrolPressErr_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 7),
    _FlowcontrolPressErr_Type()
)
flowcontrolPressErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolPressErr.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolPressErr.setUnits("Pressure error")


class _FlowcontrolPressDiff_Type(Integer32):
    """Custom type flowcontrolPressDiff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_FlowcontrolPressDiff_Type.__name__ = "Integer32"
_FlowcontrolPressDiff_Object = MibTableColumn
flowcontrolPressDiff = _FlowcontrolPressDiff_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 8),
    _FlowcontrolPressDiff_Type()
)
flowcontrolPressDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolPressDiff.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolPressDiff.setUnits("Pressure Difference")


class _FlowcontrolSetPoint_Type(Integer32):
    """Custom type flowcontrolSetPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_FlowcontrolSetPoint_Type.__name__ = "Integer32"
_FlowcontrolSetPoint_Object = MibTableColumn
flowcontrolSetPoint = _FlowcontrolSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 9),
    _FlowcontrolSetPoint_Type()
)
flowcontrolSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolSetPoint.setUnits("Pressure Set Point")
_FlowcontrolCFM_Type = Gauge32
_FlowcontrolCFM_Object = MibTableColumn
flowcontrolCFM = _FlowcontrolCFM_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 10),
    _FlowcontrolCFM_Type()
)
flowcontrolCFM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolCFM.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolCFM.setUnits("Cubic Feet per minute of system air")
_FlowcontrolMCH_Type = Gauge32
_FlowcontrolMCH_Object = MibTableColumn
flowcontrolMCH = _FlowcontrolMCH_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 11),
    _FlowcontrolMCH_Type()
)
flowcontrolMCH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolMCH.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolMCH.setUnits("Meters cubed per hour of system air")
_FlowcontrolTempBus1_Type = Gauge32
_FlowcontrolTempBus1_Object = MibTableColumn
flowcontrolTempBus1 = _FlowcontrolTempBus1_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 12),
    _FlowcontrolTempBus1_Type()
)
flowcontrolTempBus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolTempBus1.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolTempBus1.setUnits("Disconnected External Sensor")
_FlowcontrolPowerFeed_Type = Gauge32
_FlowcontrolPowerFeed_Object = MibTableColumn
flowcontrolPowerFeed = _FlowcontrolPowerFeed_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 6, 1, 13),
    _FlowcontrolPowerFeed_Type()
)
flowcontrolPowerFeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowcontrolPowerFeed.setStatus("current")
if mibBuilder.loadTexts:
    flowcontrolPowerFeed.setUnits("A/B Feed Error")
_PowerDMTable_Object = MibTable
powerDMTable = _PowerDMTable_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7)
)
if mibBuilder.loadTexts:
    powerDMTable.setStatus("current")
_PowerDMEntry_Object = MibTableRow
powerDMEntry = _PowerDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1)
)
powerDMEntry.setIndexNames(
    (0, "ODS-MIB", "powerDMIndex"),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 1),
    _PowerDMIndex_Type()
)
powerDMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerDMIndex.setStatus("current")
_PowerDMSerial_Type = DisplayString
_PowerDMSerial_Object = MibTableColumn
powerDMSerial = _PowerDMSerial_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 2),
    _PowerDMSerial_Type()
)
powerDMSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMSerial.setStatus("current")
_PowerDMName_Type = DisplayString
_PowerDMName_Object = MibTableColumn
powerDMName = _PowerDMName_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 3),
    _PowerDMName_Type()
)
powerDMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMName.setStatus("current")
_PowerDMAvail_Type = Gauge32
_PowerDMAvail_Object = MibTableColumn
powerDMAvail = _PowerDMAvail_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 4),
    _PowerDMAvail_Type()
)
powerDMAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMAvail.setStatus("current")
_PowerDMUnitInfoTitle_Type = DisplayString
_PowerDMUnitInfoTitle_Object = MibTableColumn
powerDMUnitInfoTitle = _PowerDMUnitInfoTitle_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 5),
    _PowerDMUnitInfoTitle_Type()
)
powerDMUnitInfoTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMUnitInfoTitle.setStatus("current")
_PowerDMUnitInfoVersion_Type = DisplayString
_PowerDMUnitInfoVersion_Object = MibTableColumn
powerDMUnitInfoVersion = _PowerDMUnitInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 8),
    _PowerDMUnitInfoAuxCount_Type()
)
powerDMUnitInfoAuxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMUnitInfoAuxCount.setStatus("current")
_PowerDMChannelName1_Type = DisplayString
_PowerDMChannelName1_Object = MibTableColumn
powerDMChannelName1 = _PowerDMChannelName1_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 9),
    _PowerDMChannelName1_Type()
)
powerDMChannelName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName1.setStatus("current")
_PowerDMChannelName2_Type = DisplayString
_PowerDMChannelName2_Object = MibTableColumn
powerDMChannelName2 = _PowerDMChannelName2_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 10),
    _PowerDMChannelName2_Type()
)
powerDMChannelName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName2.setStatus("current")
_PowerDMChannelName3_Type = DisplayString
_PowerDMChannelName3_Object = MibTableColumn
powerDMChannelName3 = _PowerDMChannelName3_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 11),
    _PowerDMChannelName3_Type()
)
powerDMChannelName3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName3.setStatus("current")
_PowerDMChannelName4_Type = DisplayString
_PowerDMChannelName4_Object = MibTableColumn
powerDMChannelName4 = _PowerDMChannelName4_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 12),
    _PowerDMChannelName4_Type()
)
powerDMChannelName4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName4.setStatus("current")
_PowerDMChannelName5_Type = DisplayString
_PowerDMChannelName5_Object = MibTableColumn
powerDMChannelName5 = _PowerDMChannelName5_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 13),
    _PowerDMChannelName5_Type()
)
powerDMChannelName5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName5.setStatus("current")
_PowerDMChannelName6_Type = DisplayString
_PowerDMChannelName6_Object = MibTableColumn
powerDMChannelName6 = _PowerDMChannelName6_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 14),
    _PowerDMChannelName6_Type()
)
powerDMChannelName6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName6.setStatus("current")
_PowerDMChannelName7_Type = DisplayString
_PowerDMChannelName7_Object = MibTableColumn
powerDMChannelName7 = _PowerDMChannelName7_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 15),
    _PowerDMChannelName7_Type()
)
powerDMChannelName7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName7.setStatus("current")
_PowerDMChannelName8_Type = DisplayString
_PowerDMChannelName8_Object = MibTableColumn
powerDMChannelName8 = _PowerDMChannelName8_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 16),
    _PowerDMChannelName8_Type()
)
powerDMChannelName8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName8.setStatus("current")
_PowerDMChannelName9_Type = DisplayString
_PowerDMChannelName9_Object = MibTableColumn
powerDMChannelName9 = _PowerDMChannelName9_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 17),
    _PowerDMChannelName9_Type()
)
powerDMChannelName9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName9.setStatus("current")
_PowerDMChannelName10_Type = DisplayString
_PowerDMChannelName10_Object = MibTableColumn
powerDMChannelName10 = _PowerDMChannelName10_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 18),
    _PowerDMChannelName10_Type()
)
powerDMChannelName10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName10.setStatus("current")
_PowerDMChannelName11_Type = DisplayString
_PowerDMChannelName11_Object = MibTableColumn
powerDMChannelName11 = _PowerDMChannelName11_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 19),
    _PowerDMChannelName11_Type()
)
powerDMChannelName11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName11.setStatus("current")
_PowerDMChannelName12_Type = DisplayString
_PowerDMChannelName12_Object = MibTableColumn
powerDMChannelName12 = _PowerDMChannelName12_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 20),
    _PowerDMChannelName12_Type()
)
powerDMChannelName12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName12.setStatus("current")
_PowerDMChannelName13_Type = DisplayString
_PowerDMChannelName13_Object = MibTableColumn
powerDMChannelName13 = _PowerDMChannelName13_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 21),
    _PowerDMChannelName13_Type()
)
powerDMChannelName13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName13.setStatus("current")
_PowerDMChannelName14_Type = DisplayString
_PowerDMChannelName14_Object = MibTableColumn
powerDMChannelName14 = _PowerDMChannelName14_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 22),
    _PowerDMChannelName14_Type()
)
powerDMChannelName14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName14.setStatus("current")
_PowerDMChannelName15_Type = DisplayString
_PowerDMChannelName15_Object = MibTableColumn
powerDMChannelName15 = _PowerDMChannelName15_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 23),
    _PowerDMChannelName15_Type()
)
powerDMChannelName15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName15.setStatus("current")
_PowerDMChannelName16_Type = DisplayString
_PowerDMChannelName16_Object = MibTableColumn
powerDMChannelName16 = _PowerDMChannelName16_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 24),
    _PowerDMChannelName16_Type()
)
powerDMChannelName16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName16.setStatus("current")
_PowerDMChannelName17_Type = DisplayString
_PowerDMChannelName17_Object = MibTableColumn
powerDMChannelName17 = _PowerDMChannelName17_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 25),
    _PowerDMChannelName17_Type()
)
powerDMChannelName17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName17.setStatus("current")
_PowerDMChannelName18_Type = DisplayString
_PowerDMChannelName18_Object = MibTableColumn
powerDMChannelName18 = _PowerDMChannelName18_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 26),
    _PowerDMChannelName18_Type()
)
powerDMChannelName18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName18.setStatus("current")
_PowerDMChannelName19_Type = DisplayString
_PowerDMChannelName19_Object = MibTableColumn
powerDMChannelName19 = _PowerDMChannelName19_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 27),
    _PowerDMChannelName19_Type()
)
powerDMChannelName19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName19.setStatus("current")
_PowerDMChannelName20_Type = DisplayString
_PowerDMChannelName20_Object = MibTableColumn
powerDMChannelName20 = _PowerDMChannelName20_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 28),
    _PowerDMChannelName20_Type()
)
powerDMChannelName20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName20.setStatus("current")
_PowerDMChannelName21_Type = DisplayString
_PowerDMChannelName21_Object = MibTableColumn
powerDMChannelName21 = _PowerDMChannelName21_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 29),
    _PowerDMChannelName21_Type()
)
powerDMChannelName21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName21.setStatus("current")
_PowerDMChannelName22_Type = DisplayString
_PowerDMChannelName22_Object = MibTableColumn
powerDMChannelName22 = _PowerDMChannelName22_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 30),
    _PowerDMChannelName22_Type()
)
powerDMChannelName22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName22.setStatus("current")
_PowerDMChannelName23_Type = DisplayString
_PowerDMChannelName23_Object = MibTableColumn
powerDMChannelName23 = _PowerDMChannelName23_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 31),
    _PowerDMChannelName23_Type()
)
powerDMChannelName23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName23.setStatus("current")
_PowerDMChannelName24_Type = DisplayString
_PowerDMChannelName24_Object = MibTableColumn
powerDMChannelName24 = _PowerDMChannelName24_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 32),
    _PowerDMChannelName24_Type()
)
powerDMChannelName24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName24.setStatus("current")
_PowerDMChannelName25_Type = DisplayString
_PowerDMChannelName25_Object = MibTableColumn
powerDMChannelName25 = _PowerDMChannelName25_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 33),
    _PowerDMChannelName25_Type()
)
powerDMChannelName25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName25.setStatus("current")
_PowerDMChannelName26_Type = DisplayString
_PowerDMChannelName26_Object = MibTableColumn
powerDMChannelName26 = _PowerDMChannelName26_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 34),
    _PowerDMChannelName26_Type()
)
powerDMChannelName26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName26.setStatus("current")
_PowerDMChannelName27_Type = DisplayString
_PowerDMChannelName27_Object = MibTableColumn
powerDMChannelName27 = _PowerDMChannelName27_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 35),
    _PowerDMChannelName27_Type()
)
powerDMChannelName27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName27.setStatus("current")
_PowerDMChannelName28_Type = DisplayString
_PowerDMChannelName28_Object = MibTableColumn
powerDMChannelName28 = _PowerDMChannelName28_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 36),
    _PowerDMChannelName28_Type()
)
powerDMChannelName28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName28.setStatus("current")
_PowerDMChannelName29_Type = DisplayString
_PowerDMChannelName29_Object = MibTableColumn
powerDMChannelName29 = _PowerDMChannelName29_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 37),
    _PowerDMChannelName29_Type()
)
powerDMChannelName29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName29.setStatus("current")
_PowerDMChannelName30_Type = DisplayString
_PowerDMChannelName30_Object = MibTableColumn
powerDMChannelName30 = _PowerDMChannelName30_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 38),
    _PowerDMChannelName30_Type()
)
powerDMChannelName30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName30.setStatus("current")
_PowerDMChannelName31_Type = DisplayString
_PowerDMChannelName31_Object = MibTableColumn
powerDMChannelName31 = _PowerDMChannelName31_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 39),
    _PowerDMChannelName31_Type()
)
powerDMChannelName31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName31.setStatus("current")
_PowerDMChannelName32_Type = DisplayString
_PowerDMChannelName32_Object = MibTableColumn
powerDMChannelName32 = _PowerDMChannelName32_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 40),
    _PowerDMChannelName32_Type()
)
powerDMChannelName32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName32.setStatus("current")
_PowerDMChannelName33_Type = DisplayString
_PowerDMChannelName33_Object = MibTableColumn
powerDMChannelName33 = _PowerDMChannelName33_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 41),
    _PowerDMChannelName33_Type()
)
powerDMChannelName33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName33.setStatus("current")
_PowerDMChannelName34_Type = DisplayString
_PowerDMChannelName34_Object = MibTableColumn
powerDMChannelName34 = _PowerDMChannelName34_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 42),
    _PowerDMChannelName34_Type()
)
powerDMChannelName34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName34.setStatus("current")
_PowerDMChannelName35_Type = DisplayString
_PowerDMChannelName35_Object = MibTableColumn
powerDMChannelName35 = _PowerDMChannelName35_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 43),
    _PowerDMChannelName35_Type()
)
powerDMChannelName35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName35.setStatus("current")
_PowerDMChannelName36_Type = DisplayString
_PowerDMChannelName36_Object = MibTableColumn
powerDMChannelName36 = _PowerDMChannelName36_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 44),
    _PowerDMChannelName36_Type()
)
powerDMChannelName36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName36.setStatus("current")
_PowerDMChannelName37_Type = DisplayString
_PowerDMChannelName37_Object = MibTableColumn
powerDMChannelName37 = _PowerDMChannelName37_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 45),
    _PowerDMChannelName37_Type()
)
powerDMChannelName37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName37.setStatus("current")
_PowerDMChannelName38_Type = DisplayString
_PowerDMChannelName38_Object = MibTableColumn
powerDMChannelName38 = _PowerDMChannelName38_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 46),
    _PowerDMChannelName38_Type()
)
powerDMChannelName38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName38.setStatus("current")
_PowerDMChannelName39_Type = DisplayString
_PowerDMChannelName39_Object = MibTableColumn
powerDMChannelName39 = _PowerDMChannelName39_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 47),
    _PowerDMChannelName39_Type()
)
powerDMChannelName39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName39.setStatus("current")
_PowerDMChannelName40_Type = DisplayString
_PowerDMChannelName40_Object = MibTableColumn
powerDMChannelName40 = _PowerDMChannelName40_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 48),
    _PowerDMChannelName40_Type()
)
powerDMChannelName40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName40.setStatus("current")
_PowerDMChannelName41_Type = DisplayString
_PowerDMChannelName41_Object = MibTableColumn
powerDMChannelName41 = _PowerDMChannelName41_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 49),
    _PowerDMChannelName41_Type()
)
powerDMChannelName41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName41.setStatus("current")
_PowerDMChannelName42_Type = DisplayString
_PowerDMChannelName42_Object = MibTableColumn
powerDMChannelName42 = _PowerDMChannelName42_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 50),
    _PowerDMChannelName42_Type()
)
powerDMChannelName42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName42.setStatus("current")
_PowerDMChannelName43_Type = DisplayString
_PowerDMChannelName43_Object = MibTableColumn
powerDMChannelName43 = _PowerDMChannelName43_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 51),
    _PowerDMChannelName43_Type()
)
powerDMChannelName43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName43.setStatus("current")
_PowerDMChannelName44_Type = DisplayString
_PowerDMChannelName44_Object = MibTableColumn
powerDMChannelName44 = _PowerDMChannelName44_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 52),
    _PowerDMChannelName44_Type()
)
powerDMChannelName44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName44.setStatus("current")
_PowerDMChannelName45_Type = DisplayString
_PowerDMChannelName45_Object = MibTableColumn
powerDMChannelName45 = _PowerDMChannelName45_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 53),
    _PowerDMChannelName45_Type()
)
powerDMChannelName45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName45.setStatus("current")
_PowerDMChannelName46_Type = DisplayString
_PowerDMChannelName46_Object = MibTableColumn
powerDMChannelName46 = _PowerDMChannelName46_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 54),
    _PowerDMChannelName46_Type()
)
powerDMChannelName46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName46.setStatus("current")
_PowerDMChannelName47_Type = DisplayString
_PowerDMChannelName47_Object = MibTableColumn
powerDMChannelName47 = _PowerDMChannelName47_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 55),
    _PowerDMChannelName47_Type()
)
powerDMChannelName47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName47.setStatus("current")
_PowerDMChannelName48_Type = DisplayString
_PowerDMChannelName48_Object = MibTableColumn
powerDMChannelName48 = _PowerDMChannelName48_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 56),
    _PowerDMChannelName48_Type()
)
powerDMChannelName48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelName48.setStatus("current")
_PowerDMChannelFriendly1_Type = DisplayString
_PowerDMChannelFriendly1_Object = MibTableColumn
powerDMChannelFriendly1 = _PowerDMChannelFriendly1_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 57),
    _PowerDMChannelFriendly1_Type()
)
powerDMChannelFriendly1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly1.setStatus("current")
_PowerDMChannelFriendly2_Type = DisplayString
_PowerDMChannelFriendly2_Object = MibTableColumn
powerDMChannelFriendly2 = _PowerDMChannelFriendly2_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 58),
    _PowerDMChannelFriendly2_Type()
)
powerDMChannelFriendly2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly2.setStatus("current")
_PowerDMChannelFriendly3_Type = DisplayString
_PowerDMChannelFriendly3_Object = MibTableColumn
powerDMChannelFriendly3 = _PowerDMChannelFriendly3_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 59),
    _PowerDMChannelFriendly3_Type()
)
powerDMChannelFriendly3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly3.setStatus("current")
_PowerDMChannelFriendly4_Type = DisplayString
_PowerDMChannelFriendly4_Object = MibTableColumn
powerDMChannelFriendly4 = _PowerDMChannelFriendly4_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 60),
    _PowerDMChannelFriendly4_Type()
)
powerDMChannelFriendly4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly4.setStatus("current")
_PowerDMChannelFriendly5_Type = DisplayString
_PowerDMChannelFriendly5_Object = MibTableColumn
powerDMChannelFriendly5 = _PowerDMChannelFriendly5_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 61),
    _PowerDMChannelFriendly5_Type()
)
powerDMChannelFriendly5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly5.setStatus("current")
_PowerDMChannelFriendly6_Type = DisplayString
_PowerDMChannelFriendly6_Object = MibTableColumn
powerDMChannelFriendly6 = _PowerDMChannelFriendly6_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 62),
    _PowerDMChannelFriendly6_Type()
)
powerDMChannelFriendly6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly6.setStatus("current")
_PowerDMChannelFriendly7_Type = DisplayString
_PowerDMChannelFriendly7_Object = MibTableColumn
powerDMChannelFriendly7 = _PowerDMChannelFriendly7_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 63),
    _PowerDMChannelFriendly7_Type()
)
powerDMChannelFriendly7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly7.setStatus("current")
_PowerDMChannelFriendly8_Type = DisplayString
_PowerDMChannelFriendly8_Object = MibTableColumn
powerDMChannelFriendly8 = _PowerDMChannelFriendly8_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 64),
    _PowerDMChannelFriendly8_Type()
)
powerDMChannelFriendly8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly8.setStatus("current")
_PowerDMChannelFriendly9_Type = DisplayString
_PowerDMChannelFriendly9_Object = MibTableColumn
powerDMChannelFriendly9 = _PowerDMChannelFriendly9_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 65),
    _PowerDMChannelFriendly9_Type()
)
powerDMChannelFriendly9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly9.setStatus("current")
_PowerDMChannelFriendly10_Type = DisplayString
_PowerDMChannelFriendly10_Object = MibTableColumn
powerDMChannelFriendly10 = _PowerDMChannelFriendly10_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 66),
    _PowerDMChannelFriendly10_Type()
)
powerDMChannelFriendly10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly10.setStatus("current")
_PowerDMChannelFriendly11_Type = DisplayString
_PowerDMChannelFriendly11_Object = MibTableColumn
powerDMChannelFriendly11 = _PowerDMChannelFriendly11_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 67),
    _PowerDMChannelFriendly11_Type()
)
powerDMChannelFriendly11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly11.setStatus("current")
_PowerDMChannelFriendly12_Type = DisplayString
_PowerDMChannelFriendly12_Object = MibTableColumn
powerDMChannelFriendly12 = _PowerDMChannelFriendly12_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 68),
    _PowerDMChannelFriendly12_Type()
)
powerDMChannelFriendly12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly12.setStatus("current")
_PowerDMChannelFriendly13_Type = DisplayString
_PowerDMChannelFriendly13_Object = MibTableColumn
powerDMChannelFriendly13 = _PowerDMChannelFriendly13_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 69),
    _PowerDMChannelFriendly13_Type()
)
powerDMChannelFriendly13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly13.setStatus("current")
_PowerDMChannelFriendly14_Type = DisplayString
_PowerDMChannelFriendly14_Object = MibTableColumn
powerDMChannelFriendly14 = _PowerDMChannelFriendly14_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 70),
    _PowerDMChannelFriendly14_Type()
)
powerDMChannelFriendly14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly14.setStatus("current")
_PowerDMChannelFriendly15_Type = DisplayString
_PowerDMChannelFriendly15_Object = MibTableColumn
powerDMChannelFriendly15 = _PowerDMChannelFriendly15_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 71),
    _PowerDMChannelFriendly15_Type()
)
powerDMChannelFriendly15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly15.setStatus("current")
_PowerDMChannelFriendly16_Type = DisplayString
_PowerDMChannelFriendly16_Object = MibTableColumn
powerDMChannelFriendly16 = _PowerDMChannelFriendly16_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 72),
    _PowerDMChannelFriendly16_Type()
)
powerDMChannelFriendly16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly16.setStatus("current")
_PowerDMChannelFriendly17_Type = DisplayString
_PowerDMChannelFriendly17_Object = MibTableColumn
powerDMChannelFriendly17 = _PowerDMChannelFriendly17_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 73),
    _PowerDMChannelFriendly17_Type()
)
powerDMChannelFriendly17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly17.setStatus("current")
_PowerDMChannelFriendly18_Type = DisplayString
_PowerDMChannelFriendly18_Object = MibTableColumn
powerDMChannelFriendly18 = _PowerDMChannelFriendly18_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 74),
    _PowerDMChannelFriendly18_Type()
)
powerDMChannelFriendly18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly18.setStatus("current")
_PowerDMChannelFriendly19_Type = DisplayString
_PowerDMChannelFriendly19_Object = MibTableColumn
powerDMChannelFriendly19 = _PowerDMChannelFriendly19_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 75),
    _PowerDMChannelFriendly19_Type()
)
powerDMChannelFriendly19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly19.setStatus("current")
_PowerDMChannelFriendly20_Type = DisplayString
_PowerDMChannelFriendly20_Object = MibTableColumn
powerDMChannelFriendly20 = _PowerDMChannelFriendly20_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 76),
    _PowerDMChannelFriendly20_Type()
)
powerDMChannelFriendly20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly20.setStatus("current")
_PowerDMChannelFriendly21_Type = DisplayString
_PowerDMChannelFriendly21_Object = MibTableColumn
powerDMChannelFriendly21 = _PowerDMChannelFriendly21_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 77),
    _PowerDMChannelFriendly21_Type()
)
powerDMChannelFriendly21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly21.setStatus("current")
_PowerDMChannelFriendly22_Type = DisplayString
_PowerDMChannelFriendly22_Object = MibTableColumn
powerDMChannelFriendly22 = _PowerDMChannelFriendly22_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 78),
    _PowerDMChannelFriendly22_Type()
)
powerDMChannelFriendly22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly22.setStatus("current")
_PowerDMChannelFriendly23_Type = DisplayString
_PowerDMChannelFriendly23_Object = MibTableColumn
powerDMChannelFriendly23 = _PowerDMChannelFriendly23_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 79),
    _PowerDMChannelFriendly23_Type()
)
powerDMChannelFriendly23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly23.setStatus("current")
_PowerDMChannelFriendly24_Type = DisplayString
_PowerDMChannelFriendly24_Object = MibTableColumn
powerDMChannelFriendly24 = _PowerDMChannelFriendly24_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 80),
    _PowerDMChannelFriendly24_Type()
)
powerDMChannelFriendly24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly24.setStatus("current")
_PowerDMChannelFriendly25_Type = DisplayString
_PowerDMChannelFriendly25_Object = MibTableColumn
powerDMChannelFriendly25 = _PowerDMChannelFriendly25_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 81),
    _PowerDMChannelFriendly25_Type()
)
powerDMChannelFriendly25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly25.setStatus("current")
_PowerDMChannelFriendly26_Type = DisplayString
_PowerDMChannelFriendly26_Object = MibTableColumn
powerDMChannelFriendly26 = _PowerDMChannelFriendly26_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 82),
    _PowerDMChannelFriendly26_Type()
)
powerDMChannelFriendly26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly26.setStatus("current")
_PowerDMChannelFriendly27_Type = DisplayString
_PowerDMChannelFriendly27_Object = MibTableColumn
powerDMChannelFriendly27 = _PowerDMChannelFriendly27_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 83),
    _PowerDMChannelFriendly27_Type()
)
powerDMChannelFriendly27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly27.setStatus("current")
_PowerDMChannelFriendly28_Type = DisplayString
_PowerDMChannelFriendly28_Object = MibTableColumn
powerDMChannelFriendly28 = _PowerDMChannelFriendly28_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 84),
    _PowerDMChannelFriendly28_Type()
)
powerDMChannelFriendly28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly28.setStatus("current")
_PowerDMChannelFriendly29_Type = DisplayString
_PowerDMChannelFriendly29_Object = MibTableColumn
powerDMChannelFriendly29 = _PowerDMChannelFriendly29_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 85),
    _PowerDMChannelFriendly29_Type()
)
powerDMChannelFriendly29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly29.setStatus("current")
_PowerDMChannelFriendly30_Type = DisplayString
_PowerDMChannelFriendly30_Object = MibTableColumn
powerDMChannelFriendly30 = _PowerDMChannelFriendly30_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 86),
    _PowerDMChannelFriendly30_Type()
)
powerDMChannelFriendly30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly30.setStatus("current")
_PowerDMChannelFriendly31_Type = DisplayString
_PowerDMChannelFriendly31_Object = MibTableColumn
powerDMChannelFriendly31 = _PowerDMChannelFriendly31_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 87),
    _PowerDMChannelFriendly31_Type()
)
powerDMChannelFriendly31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly31.setStatus("current")
_PowerDMChannelFriendly32_Type = DisplayString
_PowerDMChannelFriendly32_Object = MibTableColumn
powerDMChannelFriendly32 = _PowerDMChannelFriendly32_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 88),
    _PowerDMChannelFriendly32_Type()
)
powerDMChannelFriendly32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly32.setStatus("current")
_PowerDMChannelFriendly33_Type = DisplayString
_PowerDMChannelFriendly33_Object = MibTableColumn
powerDMChannelFriendly33 = _PowerDMChannelFriendly33_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 89),
    _PowerDMChannelFriendly33_Type()
)
powerDMChannelFriendly33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly33.setStatus("current")
_PowerDMChannelFriendly34_Type = DisplayString
_PowerDMChannelFriendly34_Object = MibTableColumn
powerDMChannelFriendly34 = _PowerDMChannelFriendly34_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 90),
    _PowerDMChannelFriendly34_Type()
)
powerDMChannelFriendly34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly34.setStatus("current")
_PowerDMChannelFriendly35_Type = DisplayString
_PowerDMChannelFriendly35_Object = MibTableColumn
powerDMChannelFriendly35 = _PowerDMChannelFriendly35_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 91),
    _PowerDMChannelFriendly35_Type()
)
powerDMChannelFriendly35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly35.setStatus("current")
_PowerDMChannelFriendly36_Type = DisplayString
_PowerDMChannelFriendly36_Object = MibTableColumn
powerDMChannelFriendly36 = _PowerDMChannelFriendly36_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 92),
    _PowerDMChannelFriendly36_Type()
)
powerDMChannelFriendly36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly36.setStatus("current")
_PowerDMChannelFriendly37_Type = DisplayString
_PowerDMChannelFriendly37_Object = MibTableColumn
powerDMChannelFriendly37 = _PowerDMChannelFriendly37_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 93),
    _PowerDMChannelFriendly37_Type()
)
powerDMChannelFriendly37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly37.setStatus("current")
_PowerDMChannelFriendly38_Type = DisplayString
_PowerDMChannelFriendly38_Object = MibTableColumn
powerDMChannelFriendly38 = _PowerDMChannelFriendly38_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 94),
    _PowerDMChannelFriendly38_Type()
)
powerDMChannelFriendly38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly38.setStatus("current")
_PowerDMChannelFriendly39_Type = DisplayString
_PowerDMChannelFriendly39_Object = MibTableColumn
powerDMChannelFriendly39 = _PowerDMChannelFriendly39_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 95),
    _PowerDMChannelFriendly39_Type()
)
powerDMChannelFriendly39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly39.setStatus("current")
_PowerDMChannelFriendly40_Type = DisplayString
_PowerDMChannelFriendly40_Object = MibTableColumn
powerDMChannelFriendly40 = _PowerDMChannelFriendly40_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 96),
    _PowerDMChannelFriendly40_Type()
)
powerDMChannelFriendly40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly40.setStatus("current")
_PowerDMChannelFriendly41_Type = DisplayString
_PowerDMChannelFriendly41_Object = MibTableColumn
powerDMChannelFriendly41 = _PowerDMChannelFriendly41_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 97),
    _PowerDMChannelFriendly41_Type()
)
powerDMChannelFriendly41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly41.setStatus("current")
_PowerDMChannelFriendly42_Type = DisplayString
_PowerDMChannelFriendly42_Object = MibTableColumn
powerDMChannelFriendly42 = _PowerDMChannelFriendly42_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 98),
    _PowerDMChannelFriendly42_Type()
)
powerDMChannelFriendly42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly42.setStatus("current")
_PowerDMChannelFriendly43_Type = DisplayString
_PowerDMChannelFriendly43_Object = MibTableColumn
powerDMChannelFriendly43 = _PowerDMChannelFriendly43_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 99),
    _PowerDMChannelFriendly43_Type()
)
powerDMChannelFriendly43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly43.setStatus("current")
_PowerDMChannelFriendly44_Type = DisplayString
_PowerDMChannelFriendly44_Object = MibTableColumn
powerDMChannelFriendly44 = _PowerDMChannelFriendly44_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 100),
    _PowerDMChannelFriendly44_Type()
)
powerDMChannelFriendly44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly44.setStatus("current")
_PowerDMChannelFriendly45_Type = DisplayString
_PowerDMChannelFriendly45_Object = MibTableColumn
powerDMChannelFriendly45 = _PowerDMChannelFriendly45_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 101),
    _PowerDMChannelFriendly45_Type()
)
powerDMChannelFriendly45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly45.setStatus("current")
_PowerDMChannelFriendly46_Type = DisplayString
_PowerDMChannelFriendly46_Object = MibTableColumn
powerDMChannelFriendly46 = _PowerDMChannelFriendly46_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 102),
    _PowerDMChannelFriendly46_Type()
)
powerDMChannelFriendly46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly46.setStatus("current")
_PowerDMChannelFriendly47_Type = DisplayString
_PowerDMChannelFriendly47_Object = MibTableColumn
powerDMChannelFriendly47 = _PowerDMChannelFriendly47_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 103),
    _PowerDMChannelFriendly47_Type()
)
powerDMChannelFriendly47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly47.setStatus("current")
_PowerDMChannelFriendly48_Type = DisplayString
_PowerDMChannelFriendly48_Object = MibTableColumn
powerDMChannelFriendly48 = _PowerDMChannelFriendly48_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 104),
    _PowerDMChannelFriendly48_Type()
)
powerDMChannelFriendly48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelFriendly48.setStatus("current")
_PowerDMChannelGroup1_Type = DisplayString
_PowerDMChannelGroup1_Object = MibTableColumn
powerDMChannelGroup1 = _PowerDMChannelGroup1_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 105),
    _PowerDMChannelGroup1_Type()
)
powerDMChannelGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup1.setStatus("current")
_PowerDMChannelGroup2_Type = DisplayString
_PowerDMChannelGroup2_Object = MibTableColumn
powerDMChannelGroup2 = _PowerDMChannelGroup2_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 106),
    _PowerDMChannelGroup2_Type()
)
powerDMChannelGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup2.setStatus("current")
_PowerDMChannelGroup3_Type = DisplayString
_PowerDMChannelGroup3_Object = MibTableColumn
powerDMChannelGroup3 = _PowerDMChannelGroup3_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 107),
    _PowerDMChannelGroup3_Type()
)
powerDMChannelGroup3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup3.setStatus("current")
_PowerDMChannelGroup4_Type = DisplayString
_PowerDMChannelGroup4_Object = MibTableColumn
powerDMChannelGroup4 = _PowerDMChannelGroup4_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 108),
    _PowerDMChannelGroup4_Type()
)
powerDMChannelGroup4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup4.setStatus("current")
_PowerDMChannelGroup5_Type = DisplayString
_PowerDMChannelGroup5_Object = MibTableColumn
powerDMChannelGroup5 = _PowerDMChannelGroup5_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 109),
    _PowerDMChannelGroup5_Type()
)
powerDMChannelGroup5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup5.setStatus("current")
_PowerDMChannelGroup6_Type = DisplayString
_PowerDMChannelGroup6_Object = MibTableColumn
powerDMChannelGroup6 = _PowerDMChannelGroup6_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 110),
    _PowerDMChannelGroup6_Type()
)
powerDMChannelGroup6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup6.setStatus("current")
_PowerDMChannelGroup7_Type = DisplayString
_PowerDMChannelGroup7_Object = MibTableColumn
powerDMChannelGroup7 = _PowerDMChannelGroup7_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 111),
    _PowerDMChannelGroup7_Type()
)
powerDMChannelGroup7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup7.setStatus("current")
_PowerDMChannelGroup8_Type = DisplayString
_PowerDMChannelGroup8_Object = MibTableColumn
powerDMChannelGroup8 = _PowerDMChannelGroup8_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 112),
    _PowerDMChannelGroup8_Type()
)
powerDMChannelGroup8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup8.setStatus("current")
_PowerDMChannelGroup9_Type = DisplayString
_PowerDMChannelGroup9_Object = MibTableColumn
powerDMChannelGroup9 = _PowerDMChannelGroup9_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 113),
    _PowerDMChannelGroup9_Type()
)
powerDMChannelGroup9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup9.setStatus("current")
_PowerDMChannelGroup10_Type = DisplayString
_PowerDMChannelGroup10_Object = MibTableColumn
powerDMChannelGroup10 = _PowerDMChannelGroup10_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 114),
    _PowerDMChannelGroup10_Type()
)
powerDMChannelGroup10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup10.setStatus("current")
_PowerDMChannelGroup11_Type = DisplayString
_PowerDMChannelGroup11_Object = MibTableColumn
powerDMChannelGroup11 = _PowerDMChannelGroup11_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 115),
    _PowerDMChannelGroup11_Type()
)
powerDMChannelGroup11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup11.setStatus("current")
_PowerDMChannelGroup12_Type = DisplayString
_PowerDMChannelGroup12_Object = MibTableColumn
powerDMChannelGroup12 = _PowerDMChannelGroup12_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 116),
    _PowerDMChannelGroup12_Type()
)
powerDMChannelGroup12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup12.setStatus("current")
_PowerDMChannelGroup13_Type = DisplayString
_PowerDMChannelGroup13_Object = MibTableColumn
powerDMChannelGroup13 = _PowerDMChannelGroup13_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 117),
    _PowerDMChannelGroup13_Type()
)
powerDMChannelGroup13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup13.setStatus("current")
_PowerDMChannelGroup14_Type = DisplayString
_PowerDMChannelGroup14_Object = MibTableColumn
powerDMChannelGroup14 = _PowerDMChannelGroup14_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 118),
    _PowerDMChannelGroup14_Type()
)
powerDMChannelGroup14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup14.setStatus("current")
_PowerDMChannelGroup15_Type = DisplayString
_PowerDMChannelGroup15_Object = MibTableColumn
powerDMChannelGroup15 = _PowerDMChannelGroup15_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 119),
    _PowerDMChannelGroup15_Type()
)
powerDMChannelGroup15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup15.setStatus("current")
_PowerDMChannelGroup16_Type = DisplayString
_PowerDMChannelGroup16_Object = MibTableColumn
powerDMChannelGroup16 = _PowerDMChannelGroup16_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 120),
    _PowerDMChannelGroup16_Type()
)
powerDMChannelGroup16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup16.setStatus("current")
_PowerDMChannelGroup17_Type = DisplayString
_PowerDMChannelGroup17_Object = MibTableColumn
powerDMChannelGroup17 = _PowerDMChannelGroup17_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 121),
    _PowerDMChannelGroup17_Type()
)
powerDMChannelGroup17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup17.setStatus("current")
_PowerDMChannelGroup18_Type = DisplayString
_PowerDMChannelGroup18_Object = MibTableColumn
powerDMChannelGroup18 = _PowerDMChannelGroup18_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 122),
    _PowerDMChannelGroup18_Type()
)
powerDMChannelGroup18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup18.setStatus("current")
_PowerDMChannelGroup19_Type = DisplayString
_PowerDMChannelGroup19_Object = MibTableColumn
powerDMChannelGroup19 = _PowerDMChannelGroup19_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 123),
    _PowerDMChannelGroup19_Type()
)
powerDMChannelGroup19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup19.setStatus("current")
_PowerDMChannelGroup20_Type = DisplayString
_PowerDMChannelGroup20_Object = MibTableColumn
powerDMChannelGroup20 = _PowerDMChannelGroup20_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 124),
    _PowerDMChannelGroup20_Type()
)
powerDMChannelGroup20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup20.setStatus("current")
_PowerDMChannelGroup21_Type = DisplayString
_PowerDMChannelGroup21_Object = MibTableColumn
powerDMChannelGroup21 = _PowerDMChannelGroup21_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 125),
    _PowerDMChannelGroup21_Type()
)
powerDMChannelGroup21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup21.setStatus("current")
_PowerDMChannelGroup22_Type = DisplayString
_PowerDMChannelGroup22_Object = MibTableColumn
powerDMChannelGroup22 = _PowerDMChannelGroup22_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 126),
    _PowerDMChannelGroup22_Type()
)
powerDMChannelGroup22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup22.setStatus("current")
_PowerDMChannelGroup23_Type = DisplayString
_PowerDMChannelGroup23_Object = MibTableColumn
powerDMChannelGroup23 = _PowerDMChannelGroup23_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 127),
    _PowerDMChannelGroup23_Type()
)
powerDMChannelGroup23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup23.setStatus("current")
_PowerDMChannelGroup24_Type = DisplayString
_PowerDMChannelGroup24_Object = MibTableColumn
powerDMChannelGroup24 = _PowerDMChannelGroup24_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 128),
    _PowerDMChannelGroup24_Type()
)
powerDMChannelGroup24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup24.setStatus("current")
_PowerDMChannelGroup25_Type = DisplayString
_PowerDMChannelGroup25_Object = MibTableColumn
powerDMChannelGroup25 = _PowerDMChannelGroup25_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 129),
    _PowerDMChannelGroup25_Type()
)
powerDMChannelGroup25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup25.setStatus("current")
_PowerDMChannelGroup26_Type = DisplayString
_PowerDMChannelGroup26_Object = MibTableColumn
powerDMChannelGroup26 = _PowerDMChannelGroup26_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 130),
    _PowerDMChannelGroup26_Type()
)
powerDMChannelGroup26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup26.setStatus("current")
_PowerDMChannelGroup27_Type = DisplayString
_PowerDMChannelGroup27_Object = MibTableColumn
powerDMChannelGroup27 = _PowerDMChannelGroup27_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 131),
    _PowerDMChannelGroup27_Type()
)
powerDMChannelGroup27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup27.setStatus("current")
_PowerDMChannelGroup28_Type = DisplayString
_PowerDMChannelGroup28_Object = MibTableColumn
powerDMChannelGroup28 = _PowerDMChannelGroup28_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 132),
    _PowerDMChannelGroup28_Type()
)
powerDMChannelGroup28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup28.setStatus("current")
_PowerDMChannelGroup29_Type = DisplayString
_PowerDMChannelGroup29_Object = MibTableColumn
powerDMChannelGroup29 = _PowerDMChannelGroup29_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 133),
    _PowerDMChannelGroup29_Type()
)
powerDMChannelGroup29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup29.setStatus("current")
_PowerDMChannelGroup30_Type = DisplayString
_PowerDMChannelGroup30_Object = MibTableColumn
powerDMChannelGroup30 = _PowerDMChannelGroup30_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 134),
    _PowerDMChannelGroup30_Type()
)
powerDMChannelGroup30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup30.setStatus("current")
_PowerDMChannelGroup31_Type = DisplayString
_PowerDMChannelGroup31_Object = MibTableColumn
powerDMChannelGroup31 = _PowerDMChannelGroup31_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 135),
    _PowerDMChannelGroup31_Type()
)
powerDMChannelGroup31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup31.setStatus("current")
_PowerDMChannelGroup32_Type = DisplayString
_PowerDMChannelGroup32_Object = MibTableColumn
powerDMChannelGroup32 = _PowerDMChannelGroup32_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 136),
    _PowerDMChannelGroup32_Type()
)
powerDMChannelGroup32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup32.setStatus("current")
_PowerDMChannelGroup33_Type = DisplayString
_PowerDMChannelGroup33_Object = MibTableColumn
powerDMChannelGroup33 = _PowerDMChannelGroup33_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 137),
    _PowerDMChannelGroup33_Type()
)
powerDMChannelGroup33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup33.setStatus("current")
_PowerDMChannelGroup34_Type = DisplayString
_PowerDMChannelGroup34_Object = MibTableColumn
powerDMChannelGroup34 = _PowerDMChannelGroup34_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 138),
    _PowerDMChannelGroup34_Type()
)
powerDMChannelGroup34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup34.setStatus("current")
_PowerDMChannelGroup35_Type = DisplayString
_PowerDMChannelGroup35_Object = MibTableColumn
powerDMChannelGroup35 = _PowerDMChannelGroup35_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 139),
    _PowerDMChannelGroup35_Type()
)
powerDMChannelGroup35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup35.setStatus("current")
_PowerDMChannelGroup36_Type = DisplayString
_PowerDMChannelGroup36_Object = MibTableColumn
powerDMChannelGroup36 = _PowerDMChannelGroup36_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 140),
    _PowerDMChannelGroup36_Type()
)
powerDMChannelGroup36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup36.setStatus("current")
_PowerDMChannelGroup37_Type = DisplayString
_PowerDMChannelGroup37_Object = MibTableColumn
powerDMChannelGroup37 = _PowerDMChannelGroup37_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 141),
    _PowerDMChannelGroup37_Type()
)
powerDMChannelGroup37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup37.setStatus("current")
_PowerDMChannelGroup38_Type = DisplayString
_PowerDMChannelGroup38_Object = MibTableColumn
powerDMChannelGroup38 = _PowerDMChannelGroup38_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 142),
    _PowerDMChannelGroup38_Type()
)
powerDMChannelGroup38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup38.setStatus("current")
_PowerDMChannelGroup39_Type = DisplayString
_PowerDMChannelGroup39_Object = MibTableColumn
powerDMChannelGroup39 = _PowerDMChannelGroup39_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 143),
    _PowerDMChannelGroup39_Type()
)
powerDMChannelGroup39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup39.setStatus("current")
_PowerDMChannelGroup40_Type = DisplayString
_PowerDMChannelGroup40_Object = MibTableColumn
powerDMChannelGroup40 = _PowerDMChannelGroup40_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 144),
    _PowerDMChannelGroup40_Type()
)
powerDMChannelGroup40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup40.setStatus("current")
_PowerDMChannelGroup41_Type = DisplayString
_PowerDMChannelGroup41_Object = MibTableColumn
powerDMChannelGroup41 = _PowerDMChannelGroup41_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 145),
    _PowerDMChannelGroup41_Type()
)
powerDMChannelGroup41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup41.setStatus("current")
_PowerDMChannelGroup42_Type = DisplayString
_PowerDMChannelGroup42_Object = MibTableColumn
powerDMChannelGroup42 = _PowerDMChannelGroup42_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 146),
    _PowerDMChannelGroup42_Type()
)
powerDMChannelGroup42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup42.setStatus("current")
_PowerDMChannelGroup43_Type = DisplayString
_PowerDMChannelGroup43_Object = MibTableColumn
powerDMChannelGroup43 = _PowerDMChannelGroup43_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 147),
    _PowerDMChannelGroup43_Type()
)
powerDMChannelGroup43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup43.setStatus("current")
_PowerDMChannelGroup44_Type = DisplayString
_PowerDMChannelGroup44_Object = MibTableColumn
powerDMChannelGroup44 = _PowerDMChannelGroup44_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 148),
    _PowerDMChannelGroup44_Type()
)
powerDMChannelGroup44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup44.setStatus("current")
_PowerDMChannelGroup45_Type = DisplayString
_PowerDMChannelGroup45_Object = MibTableColumn
powerDMChannelGroup45 = _PowerDMChannelGroup45_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 149),
    _PowerDMChannelGroup45_Type()
)
powerDMChannelGroup45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup45.setStatus("current")
_PowerDMChannelGroup46_Type = DisplayString
_PowerDMChannelGroup46_Object = MibTableColumn
powerDMChannelGroup46 = _PowerDMChannelGroup46_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 150),
    _PowerDMChannelGroup46_Type()
)
powerDMChannelGroup46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup46.setStatus("current")
_PowerDMChannelGroup47_Type = DisplayString
_PowerDMChannelGroup47_Object = MibTableColumn
powerDMChannelGroup47 = _PowerDMChannelGroup47_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 151),
    _PowerDMChannelGroup47_Type()
)
powerDMChannelGroup47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMChannelGroup47.setStatus("current")
_PowerDMChannelGroup48_Type = DisplayString
_PowerDMChannelGroup48_Object = MibTableColumn
powerDMChannelGroup48 = _PowerDMChannelGroup48_Object(
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 152),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 153),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 154),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 155),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 156),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 157),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 158),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 159),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 160),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 161),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 162),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 163),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 164),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 165),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 166),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 167),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 168),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 169),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 170),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 171),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 172),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 173),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 174),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 175),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 176),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 177),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 178),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 179),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 180),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 181),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 182),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 183),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 184),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 185),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 186),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 187),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 188),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 189),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 190),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 191),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 192),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 193),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 194),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 195),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 196),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 197),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 198),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 199),
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
    (1, 3, 6, 1, 4, 1, 29414, 1, 7, 1, 200),
    _PowerDMDeciAmps48_Type()
)
powerDMDeciAmps48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerDMDeciAmps48.setStatus("current")
if mibBuilder.loadTexts:
    powerDMDeciAmps48.setUnits("0.1 Amps")
_OdsTrap_ObjectIdentity = ObjectIdentity
odsTrap = _OdsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767)
)
_OdsTrapPrefix_ObjectIdentity = ObjectIdentity
odsTrapPrefix = _OdsTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0)
)

# Managed Objects groups


# Notification objects

odsTestNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10101)
)
if mibBuilder.loadTexts:
    odsTestNOTIFY.setStatus(
        "current"
    )

odsClimateTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10205)
)
odsClimateTempCNOTIFY.setObjects(
      *(("ODS-MIB", "climateTempC"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateTempCNOTIFY.setStatus(
        "current"
    )

odsClimateTempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10206)
)
odsClimateTempFNOTIFY.setObjects(
      *(("ODS-MIB", "climateTempF"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateTempFNOTIFY.setStatus(
        "current"
    )

odsClimateHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10207)
)
odsClimateHumidityNOTIFY.setObjects(
      *(("ODS-MIB", "climateHumidity"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateHumidityNOTIFY.setStatus(
        "current"
    )

odsClimateLightNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10208)
)
odsClimateLightNOTIFY.setObjects(
      *(("ODS-MIB", "climateLight"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateLightNOTIFY.setStatus(
        "current"
    )

odsClimateAirflowNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10209)
)
odsClimateAirflowNOTIFY.setObjects(
      *(("ODS-MIB", "climateAirflow"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateAirflowNOTIFY.setStatus(
        "current"
    )

odsClimateSoundNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10210)
)
odsClimateSoundNOTIFY.setObjects(
      *(("ODS-MIB", "climateSound"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateSoundNOTIFY.setStatus(
        "current"
    )

odsClimateIO1NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10211)
)
odsClimateIO1NOTIFY.setObjects(
      *(("ODS-MIB", "climateIO1"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateIO1NOTIFY.setStatus(
        "current"
    )

odsClimateIO2NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10212)
)
odsClimateIO2NOTIFY.setObjects(
      *(("ODS-MIB", "climateIO2"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateIO2NOTIFY.setStatus(
        "current"
    )

odsClimateIO3NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10213)
)
odsClimateIO3NOTIFY.setObjects(
      *(("ODS-MIB", "climateIO3"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateIO3NOTIFY.setStatus(
        "current"
    )

odsDewPointSensorTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10305)
)
odsDewPointSensorTempCNOTIFY.setObjects(
      *(("ODS-MIB", "dewPointSensorTempC"),
        ("ODS-MIB", "dewPointSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsDewPointSensorTempCNOTIFY.setStatus(
        "current"
    )

odsDewPointSensorTempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10306)
)
odsDewPointSensorTempFNOTIFY.setObjects(
      *(("ODS-MIB", "dewPointSensorTempF"),
        ("ODS-MIB", "dewPointSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsDewPointSensorTempFNOTIFY.setStatus(
        "current"
    )

odsDewPointSensorHumidityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10307)
)
odsDewPointSensorHumidityNOTIFY.setObjects(
      *(("ODS-MIB", "dewPointSensorHumidity"),
        ("ODS-MIB", "dewPointSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsDewPointSensorHumidityNOTIFY.setStatus(
        "current"
    )

odsDewPointSensorDewpointCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10308)
)
odsDewPointSensorDewpointCNOTIFY.setObjects(
      *(("ODS-MIB", "dewPointSensorDewpointC"),
        ("ODS-MIB", "dewPointSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsDewPointSensorDewpointCNOTIFY.setStatus(
        "current"
    )

odsDewPointSensorDewpointFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10309)
)
odsDewPointSensorDewpointFNOTIFY.setObjects(
      *(("ODS-MIB", "dewPointSensorDewpointF"),
        ("ODS-MIB", "dewPointSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsDewPointSensorDewpointFNOTIFY.setStatus(
        "current"
    )

odsFancontrolTempCreturnANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10405)
)
odsFancontrolTempCreturnANOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolTempCreturnA"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempCreturnANOTIFY.setStatus(
        "current"
    )

odsFancontrolTempFreturnANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10406)
)
odsFancontrolTempFreturnANOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolTempFreturnA"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempFreturnANOTIFY.setStatus(
        "current"
    )

odsFancontrolTempCreturnBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10407)
)
odsFancontrolTempCreturnBNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolTempCreturnB"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempCreturnBNOTIFY.setStatus(
        "current"
    )

odsFancontrolTempFreturnBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10408)
)
odsFancontrolTempFreturnBNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolTempFreturnB"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempFreturnBNOTIFY.setStatus(
        "current"
    )

odsFancontrolRpmFanANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10409)
)
odsFancontrolRpmFanANOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolRpmFanA"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolRpmFanANOTIFY.setStatus(
        "current"
    )

odsFancontrolRpmFanBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10410)
)
odsFancontrolRpmFanBNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolRpmFanB"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolRpmFanBNOTIFY.setStatus(
        "current"
    )

odsFancontrolCapacityANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10411)
)
odsFancontrolCapacityANOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolCapacityA"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolCapacityANOTIFY.setStatus(
        "current"
    )

odsFancontrolCapacityBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10412)
)
odsFancontrolCapacityBNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolCapacityB"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolCapacityBNOTIFY.setStatus(
        "current"
    )

odsFancontrolPressErrNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10413)
)
odsFancontrolPressErrNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolPressErr"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolPressErrNOTIFY.setStatus(
        "current"
    )

odsFancontrolPressDiffNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10414)
)
odsFancontrolPressDiffNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolPressDiff"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolPressDiffNOTIFY.setStatus(
        "current"
    )

odsFancontrolSetPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10415)
)
odsFancontrolSetPointNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolSetPoint"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolSetPointNOTIFY.setStatus(
        "current"
    )

odsFancontrolCFMNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10416)
)
odsFancontrolCFMNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolCFM"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolCFMNOTIFY.setStatus(
        "current"
    )

odsFancontrolMCHNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10417)
)
odsFancontrolMCHNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolMCH"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolMCHNOTIFY.setStatus(
        "current"
    )

odsFancontrolTempCreturnNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10418)
)
odsFancontrolTempCreturnNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolTempCreturn"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempCreturnNOTIFY.setStatus(
        "current"
    )

odsFancontrolTempFreturnNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10419)
)
odsFancontrolTempFreturnNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolTempFreturn"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempFreturnNOTIFY.setStatus(
        "current"
    )

odsFancontrolCapacityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10420)
)
odsFancontrolCapacityNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolCapacity"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolCapacityNOTIFY.setStatus(
        "current"
    )

odsFancontrolFanMissingNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10421)
)
odsFancontrolFanMissingNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolFanMissing"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolFanMissingNOTIFY.setStatus(
        "current"
    )

odsFancontrolFanMismatchNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10422)
)
odsFancontrolFanMismatchNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolFanMismatch"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolFanMismatchNOTIFY.setStatus(
        "current"
    )

odsFancontrolFanErrorANOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10423)
)
odsFancontrolFanErrorANOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolFanErrorA"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolFanErrorANOTIFY.setStatus(
        "current"
    )

odsFancontrolFanErrorBNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10424)
)
odsFancontrolFanErrorBNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolFanErrorB"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolFanErrorBNOTIFY.setStatus(
        "current"
    )

odsFancontrolTempBus1NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10425)
)
odsFancontrolTempBus1NOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolTempBus1"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempBus1NOTIFY.setStatus(
        "current"
    )

odsFancontrolPowerFeedNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10426)
)
odsFancontrolPowerFeedNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolPowerFeed"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolPowerFeedNOTIFY.setStatus(
        "current"
    )

odsFancontrolFanEndofLifeNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10427)
)
odsFancontrolFanEndofLifeNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolFanEndofLife"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolFanEndofLifeNOTIFY.setStatus(
        "current"
    )

odsFancontrolTargetCapacityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10428)
)
odsFancontrolTargetCapacityNOTIFY.setObjects(
      *(("ODS-MIB", "fancontrolTargetCapacity"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTargetCapacityNOTIFY.setStatus(
        "current"
    )

odsTempSensorTempCNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10505)
)
odsTempSensorTempCNOTIFY.setObjects(
      *(("ODS-MIB", "tempSensorTempC"),
        ("ODS-MIB", "tempSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsTempSensorTempCNOTIFY.setStatus(
        "current"
    )

odsTempSensorTempFNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10506)
)
odsTempSensorTempFNOTIFY.setObjects(
      *(("ODS-MIB", "tempSensorTempF"),
        ("ODS-MIB", "tempSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsTempSensorTempFNOTIFY.setStatus(
        "current"
    )

odsFlowcontrolRpmFanNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10605)
)
odsFlowcontrolRpmFanNOTIFY.setObjects(
      *(("ODS-MIB", "flowcontrolRpmFan"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolRpmFanNOTIFY.setStatus(
        "current"
    )

odsFlowcontrolCapacityNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10606)
)
odsFlowcontrolCapacityNOTIFY.setObjects(
      *(("ODS-MIB", "flowcontrolCapacity"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolCapacityNOTIFY.setStatus(
        "current"
    )

odsFlowcontrolPressErrNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10607)
)
odsFlowcontrolPressErrNOTIFY.setObjects(
      *(("ODS-MIB", "flowcontrolPressErr"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolPressErrNOTIFY.setStatus(
        "current"
    )

odsFlowcontrolPressDiffNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10608)
)
odsFlowcontrolPressDiffNOTIFY.setObjects(
      *(("ODS-MIB", "flowcontrolPressDiff"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolPressDiffNOTIFY.setStatus(
        "current"
    )

odsFlowcontrolSetPointNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10609)
)
odsFlowcontrolSetPointNOTIFY.setObjects(
      *(("ODS-MIB", "flowcontrolSetPoint"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolSetPointNOTIFY.setStatus(
        "current"
    )

odsFlowcontrolCFMNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10610)
)
odsFlowcontrolCFMNOTIFY.setObjects(
      *(("ODS-MIB", "flowcontrolCFM"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolCFMNOTIFY.setStatus(
        "current"
    )

odsFlowcontrolMCHNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10611)
)
odsFlowcontrolMCHNOTIFY.setObjects(
      *(("ODS-MIB", "flowcontrolMCH"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolMCHNOTIFY.setStatus(
        "current"
    )

odsFlowcontrolTempBus1NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10612)
)
odsFlowcontrolTempBus1NOTIFY.setObjects(
      *(("ODS-MIB", "flowcontrolTempBus1"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolTempBus1NOTIFY.setStatus(
        "current"
    )

odsFlowcontrolPowerFeedNOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 10613)
)
odsFlowcontrolPowerFeedNOTIFY.setObjects(
      *(("ODS-MIB", "flowcontrolPowerFeed"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolPowerFeedNOTIFY.setStatus(
        "current"
    )

odsClimateTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20205)
)
odsClimateTempCCLEAR.setObjects(
      *(("ODS-MIB", "climateTempC"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateTempCCLEAR.setStatus(
        "current"
    )

odsClimateTempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20206)
)
odsClimateTempFCLEAR.setObjects(
      *(("ODS-MIB", "climateTempF"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateTempFCLEAR.setStatus(
        "current"
    )

odsClimateHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20207)
)
odsClimateHumidityCLEAR.setObjects(
      *(("ODS-MIB", "climateHumidity"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateHumidityCLEAR.setStatus(
        "current"
    )

odsClimateLightCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20208)
)
odsClimateLightCLEAR.setObjects(
      *(("ODS-MIB", "climateLight"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateLightCLEAR.setStatus(
        "current"
    )

odsClimateAirflowCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20209)
)
odsClimateAirflowCLEAR.setObjects(
      *(("ODS-MIB", "climateAirflow"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateAirflowCLEAR.setStatus(
        "current"
    )

odsClimateSoundCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20210)
)
odsClimateSoundCLEAR.setObjects(
      *(("ODS-MIB", "climateSound"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateSoundCLEAR.setStatus(
        "current"
    )

odsClimateIO1CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20211)
)
odsClimateIO1CLEAR.setObjects(
      *(("ODS-MIB", "climateIO1"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateIO1CLEAR.setStatus(
        "current"
    )

odsClimateIO2CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20212)
)
odsClimateIO2CLEAR.setObjects(
      *(("ODS-MIB", "climateIO2"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateIO2CLEAR.setStatus(
        "current"
    )

odsClimateIO3CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20213)
)
odsClimateIO3CLEAR.setObjects(
      *(("ODS-MIB", "climateIO3"),
        ("ODS-MIB", "climateName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsClimateIO3CLEAR.setStatus(
        "current"
    )

odsDewPointSensorTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20305)
)
odsDewPointSensorTempCCLEAR.setObjects(
      *(("ODS-MIB", "dewPointSensorTempC"),
        ("ODS-MIB", "dewPointSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsDewPointSensorTempCCLEAR.setStatus(
        "current"
    )

odsDewPointSensorTempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20306)
)
odsDewPointSensorTempFCLEAR.setObjects(
      *(("ODS-MIB", "dewPointSensorTempF"),
        ("ODS-MIB", "dewPointSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsDewPointSensorTempFCLEAR.setStatus(
        "current"
    )

odsDewPointSensorHumidityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20307)
)
odsDewPointSensorHumidityCLEAR.setObjects(
      *(("ODS-MIB", "dewPointSensorHumidity"),
        ("ODS-MIB", "dewPointSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsDewPointSensorHumidityCLEAR.setStatus(
        "current"
    )

odsDewPointSensorDewpointCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20308)
)
odsDewPointSensorDewpointCCLEAR.setObjects(
      *(("ODS-MIB", "dewPointSensorDewpointC"),
        ("ODS-MIB", "dewPointSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsDewPointSensorDewpointCCLEAR.setStatus(
        "current"
    )

odsDewPointSensorDewpointFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20309)
)
odsDewPointSensorDewpointFCLEAR.setObjects(
      *(("ODS-MIB", "dewPointSensorDewpointF"),
        ("ODS-MIB", "dewPointSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsDewPointSensorDewpointFCLEAR.setStatus(
        "current"
    )

odsFancontrolTempCreturnACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20405)
)
odsFancontrolTempCreturnACLEAR.setObjects(
      *(("ODS-MIB", "fancontrolTempCreturnA"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempCreturnACLEAR.setStatus(
        "current"
    )

odsFancontrolTempFreturnACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20406)
)
odsFancontrolTempFreturnACLEAR.setObjects(
      *(("ODS-MIB", "fancontrolTempFreturnA"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempFreturnACLEAR.setStatus(
        "current"
    )

odsFancontrolTempCreturnBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20407)
)
odsFancontrolTempCreturnBCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolTempCreturnB"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempCreturnBCLEAR.setStatus(
        "current"
    )

odsFancontrolTempFreturnBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20408)
)
odsFancontrolTempFreturnBCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolTempFreturnB"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempFreturnBCLEAR.setStatus(
        "current"
    )

odsFancontrolRpmFanACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20409)
)
odsFancontrolRpmFanACLEAR.setObjects(
      *(("ODS-MIB", "fancontrolRpmFanA"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolRpmFanACLEAR.setStatus(
        "current"
    )

odsFancontrolRpmFanBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20410)
)
odsFancontrolRpmFanBCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolRpmFanB"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolRpmFanBCLEAR.setStatus(
        "current"
    )

odsFancontrolCapacityACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20411)
)
odsFancontrolCapacityACLEAR.setObjects(
      *(("ODS-MIB", "fancontrolCapacityA"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolCapacityACLEAR.setStatus(
        "current"
    )

odsFancontrolCapacityBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20412)
)
odsFancontrolCapacityBCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolCapacityB"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolCapacityBCLEAR.setStatus(
        "current"
    )

odsFancontrolPressErrCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20413)
)
odsFancontrolPressErrCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolPressErr"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolPressErrCLEAR.setStatus(
        "current"
    )

odsFancontrolPressDiffCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20414)
)
odsFancontrolPressDiffCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolPressDiff"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolPressDiffCLEAR.setStatus(
        "current"
    )

odsFancontrolSetPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20415)
)
odsFancontrolSetPointCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolSetPoint"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolSetPointCLEAR.setStatus(
        "current"
    )

odsFancontrolCFMCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20416)
)
odsFancontrolCFMCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolCFM"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolCFMCLEAR.setStatus(
        "current"
    )

odsFancontrolMCHCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20417)
)
odsFancontrolMCHCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolMCH"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolMCHCLEAR.setStatus(
        "current"
    )

odsFancontrolTempCreturnCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20418)
)
odsFancontrolTempCreturnCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolTempCreturn"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempCreturnCLEAR.setStatus(
        "current"
    )

odsFancontrolTempFreturnCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20419)
)
odsFancontrolTempFreturnCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolTempFreturn"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempFreturnCLEAR.setStatus(
        "current"
    )

odsFancontrolCapacityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20420)
)
odsFancontrolCapacityCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolCapacity"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolCapacityCLEAR.setStatus(
        "current"
    )

odsFancontrolFanMissingCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20421)
)
odsFancontrolFanMissingCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolFanMissing"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolFanMissingCLEAR.setStatus(
        "current"
    )

odsFancontrolFanMismatchCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20422)
)
odsFancontrolFanMismatchCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolFanMismatch"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolFanMismatchCLEAR.setStatus(
        "current"
    )

odsFancontrolFanErrorACLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20423)
)
odsFancontrolFanErrorACLEAR.setObjects(
      *(("ODS-MIB", "fancontrolFanErrorA"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolFanErrorACLEAR.setStatus(
        "current"
    )

odsFancontrolFanErrorBCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20424)
)
odsFancontrolFanErrorBCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolFanErrorB"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolFanErrorBCLEAR.setStatus(
        "current"
    )

odsFancontrolTempBus1CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20425)
)
odsFancontrolTempBus1CLEAR.setObjects(
      *(("ODS-MIB", "fancontrolTempBus1"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTempBus1CLEAR.setStatus(
        "current"
    )

odsFancontrolPowerFeedCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20426)
)
odsFancontrolPowerFeedCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolPowerFeed"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolPowerFeedCLEAR.setStatus(
        "current"
    )

odsFancontrolFanEndofLifeCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20427)
)
odsFancontrolFanEndofLifeCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolFanEndofLife"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolFanEndofLifeCLEAR.setStatus(
        "current"
    )

odsFancontrolTargetCapacityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20428)
)
odsFancontrolTargetCapacityCLEAR.setObjects(
      *(("ODS-MIB", "fancontrolTargetCapacity"),
        ("ODS-MIB", "fancontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFancontrolTargetCapacityCLEAR.setStatus(
        "current"
    )

odsTempSensorTempCCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20505)
)
odsTempSensorTempCCLEAR.setObjects(
      *(("ODS-MIB", "tempSensorTempC"),
        ("ODS-MIB", "tempSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsTempSensorTempCCLEAR.setStatus(
        "current"
    )

odsTempSensorTempFCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20506)
)
odsTempSensorTempFCLEAR.setObjects(
      *(("ODS-MIB", "tempSensorTempF"),
        ("ODS-MIB", "tempSensorName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsTempSensorTempFCLEAR.setStatus(
        "current"
    )

odsFlowcontrolRpmFanCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20605)
)
odsFlowcontrolRpmFanCLEAR.setObjects(
      *(("ODS-MIB", "flowcontrolRpmFan"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolRpmFanCLEAR.setStatus(
        "current"
    )

odsFlowcontrolCapacityCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20606)
)
odsFlowcontrolCapacityCLEAR.setObjects(
      *(("ODS-MIB", "flowcontrolCapacity"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolCapacityCLEAR.setStatus(
        "current"
    )

odsFlowcontrolPressErrCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20607)
)
odsFlowcontrolPressErrCLEAR.setObjects(
      *(("ODS-MIB", "flowcontrolPressErr"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolPressErrCLEAR.setStatus(
        "current"
    )

odsFlowcontrolPressDiffCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20608)
)
odsFlowcontrolPressDiffCLEAR.setObjects(
      *(("ODS-MIB", "flowcontrolPressDiff"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolPressDiffCLEAR.setStatus(
        "current"
    )

odsFlowcontrolSetPointCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20609)
)
odsFlowcontrolSetPointCLEAR.setObjects(
      *(("ODS-MIB", "flowcontrolSetPoint"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolSetPointCLEAR.setStatus(
        "current"
    )

odsFlowcontrolCFMCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20610)
)
odsFlowcontrolCFMCLEAR.setObjects(
      *(("ODS-MIB", "flowcontrolCFM"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolCFMCLEAR.setStatus(
        "current"
    )

odsFlowcontrolMCHCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20611)
)
odsFlowcontrolMCHCLEAR.setObjects(
      *(("ODS-MIB", "flowcontrolMCH"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolMCHCLEAR.setStatus(
        "current"
    )

odsFlowcontrolTempBus1CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20612)
)
odsFlowcontrolTempBus1CLEAR.setObjects(
      *(("ODS-MIB", "flowcontrolTempBus1"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolTempBus1CLEAR.setStatus(
        "current"
    )

odsFlowcontrolPowerFeedCLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 20613)
)
odsFlowcontrolPowerFeedCLEAR.setObjects(
      *(("ODS-MIB", "flowcontrolPowerFeed"),
        ("ODS-MIB", "flowcontrolName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsFlowcontrolPowerFeedCLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps1NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107153)
)
odsPowerDMDeciAmps1NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps1"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps1NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps2NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107154)
)
odsPowerDMDeciAmps2NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps2"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps2NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps3NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107155)
)
odsPowerDMDeciAmps3NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps3"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps3NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps4NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107156)
)
odsPowerDMDeciAmps4NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps4"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps4NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps5NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107157)
)
odsPowerDMDeciAmps5NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps5"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps5NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps6NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107158)
)
odsPowerDMDeciAmps6NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps6"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps6NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps7NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107159)
)
odsPowerDMDeciAmps7NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps7"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps7NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps8NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107160)
)
odsPowerDMDeciAmps8NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps8"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps8NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps9NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107161)
)
odsPowerDMDeciAmps9NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps9"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps9NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps10NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107162)
)
odsPowerDMDeciAmps10NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps10"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps10NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps11NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107163)
)
odsPowerDMDeciAmps11NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps11"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps11NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps12NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107164)
)
odsPowerDMDeciAmps12NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps12"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps12NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps13NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107165)
)
odsPowerDMDeciAmps13NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps13"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps13NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps14NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107166)
)
odsPowerDMDeciAmps14NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps14"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps14NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps15NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107167)
)
odsPowerDMDeciAmps15NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps15"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps15NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps16NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107168)
)
odsPowerDMDeciAmps16NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps16"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps16NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps17NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107169)
)
odsPowerDMDeciAmps17NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps17"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps17NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps18NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107170)
)
odsPowerDMDeciAmps18NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps18"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps18NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps19NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107171)
)
odsPowerDMDeciAmps19NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps19"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps19NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps20NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107172)
)
odsPowerDMDeciAmps20NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps20"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps20NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps21NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107173)
)
odsPowerDMDeciAmps21NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps21"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps21NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps22NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107174)
)
odsPowerDMDeciAmps22NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps22"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps22NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps23NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107175)
)
odsPowerDMDeciAmps23NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps23"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps23NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps24NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107176)
)
odsPowerDMDeciAmps24NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps24"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps24NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps25NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107177)
)
odsPowerDMDeciAmps25NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps25"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps25NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps26NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107178)
)
odsPowerDMDeciAmps26NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps26"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps26NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps27NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107179)
)
odsPowerDMDeciAmps27NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps27"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps27NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps28NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107180)
)
odsPowerDMDeciAmps28NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps28"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps28NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps29NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107181)
)
odsPowerDMDeciAmps29NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps29"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps29NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps30NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107182)
)
odsPowerDMDeciAmps30NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps30"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps30NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps31NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107183)
)
odsPowerDMDeciAmps31NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps31"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps31NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps32NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107184)
)
odsPowerDMDeciAmps32NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps32"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps32NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps33NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107185)
)
odsPowerDMDeciAmps33NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps33"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps33NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps34NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107186)
)
odsPowerDMDeciAmps34NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps34"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps34NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps35NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107187)
)
odsPowerDMDeciAmps35NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps35"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps35NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps36NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107188)
)
odsPowerDMDeciAmps36NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps36"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps36NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps37NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107189)
)
odsPowerDMDeciAmps37NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps37"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps37NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps38NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107190)
)
odsPowerDMDeciAmps38NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps38"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps38NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps39NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107191)
)
odsPowerDMDeciAmps39NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps39"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps39NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps40NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107192)
)
odsPowerDMDeciAmps40NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps40"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps40NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps41NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107193)
)
odsPowerDMDeciAmps41NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps41"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps41NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps42NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107194)
)
odsPowerDMDeciAmps42NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps42"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps42NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps43NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107195)
)
odsPowerDMDeciAmps43NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps43"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps43NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps44NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107196)
)
odsPowerDMDeciAmps44NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps44"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps44NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps45NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107197)
)
odsPowerDMDeciAmps45NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps45"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps45NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps46NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107198)
)
odsPowerDMDeciAmps46NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps46"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps46NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps47NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107199)
)
odsPowerDMDeciAmps47NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps47"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps47NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps48NOTIFY = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 107200)
)
odsPowerDMDeciAmps48NOTIFY.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps48"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps48NOTIFY.setStatus(
        "current"
    )

odsPowerDMDeciAmps1CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117153)
)
odsPowerDMDeciAmps1CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps1"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps1CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps2CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117154)
)
odsPowerDMDeciAmps2CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps2"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps2CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps3CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117155)
)
odsPowerDMDeciAmps3CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps3"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps3CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps4CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117156)
)
odsPowerDMDeciAmps4CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps4"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps4CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps5CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117157)
)
odsPowerDMDeciAmps5CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps5"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps5CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps6CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117158)
)
odsPowerDMDeciAmps6CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps6"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps6CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps7CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117159)
)
odsPowerDMDeciAmps7CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps7"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps7CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps8CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117160)
)
odsPowerDMDeciAmps8CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps8"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps8CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps9CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117161)
)
odsPowerDMDeciAmps9CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps9"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps9CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps10CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117162)
)
odsPowerDMDeciAmps10CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps10"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps10CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps11CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117163)
)
odsPowerDMDeciAmps11CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps11"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps11CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps12CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117164)
)
odsPowerDMDeciAmps12CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps12"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps12CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps13CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117165)
)
odsPowerDMDeciAmps13CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps13"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps13CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps14CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117166)
)
odsPowerDMDeciAmps14CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps14"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps14CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps15CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117167)
)
odsPowerDMDeciAmps15CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps15"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps15CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps16CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117168)
)
odsPowerDMDeciAmps16CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps16"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps16CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps17CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117169)
)
odsPowerDMDeciAmps17CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps17"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps17CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps18CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117170)
)
odsPowerDMDeciAmps18CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps18"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps18CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps19CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117171)
)
odsPowerDMDeciAmps19CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps19"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps19CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps20CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117172)
)
odsPowerDMDeciAmps20CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps20"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps20CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps21CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117173)
)
odsPowerDMDeciAmps21CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps21"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps21CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps22CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117174)
)
odsPowerDMDeciAmps22CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps22"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps22CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps23CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117175)
)
odsPowerDMDeciAmps23CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps23"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps23CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps24CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117176)
)
odsPowerDMDeciAmps24CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps24"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps24CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps25CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117177)
)
odsPowerDMDeciAmps25CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps25"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps25CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps26CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117178)
)
odsPowerDMDeciAmps26CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps26"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps26CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps27CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117179)
)
odsPowerDMDeciAmps27CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps27"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps27CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps28CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117180)
)
odsPowerDMDeciAmps28CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps28"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps28CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps29CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117181)
)
odsPowerDMDeciAmps29CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps29"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps29CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps30CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117182)
)
odsPowerDMDeciAmps30CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps30"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps30CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps31CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117183)
)
odsPowerDMDeciAmps31CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps31"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps31CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps32CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117184)
)
odsPowerDMDeciAmps32CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps32"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps32CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps33CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117185)
)
odsPowerDMDeciAmps33CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps33"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps33CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps34CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117186)
)
odsPowerDMDeciAmps34CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps34"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps34CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps35CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117187)
)
odsPowerDMDeciAmps35CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps35"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps35CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps36CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117188)
)
odsPowerDMDeciAmps36CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps36"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps36CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps37CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117189)
)
odsPowerDMDeciAmps37CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps37"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps37CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps38CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117190)
)
odsPowerDMDeciAmps38CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps38"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps38CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps39CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117191)
)
odsPowerDMDeciAmps39CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps39"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps39CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps40CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117192)
)
odsPowerDMDeciAmps40CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps40"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps40CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps41CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117193)
)
odsPowerDMDeciAmps41CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps41"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps41CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps42CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117194)
)
odsPowerDMDeciAmps42CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps42"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps42CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps43CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117195)
)
odsPowerDMDeciAmps43CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps43"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps43CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps44CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117196)
)
odsPowerDMDeciAmps44CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps44"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps44CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps45CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117197)
)
odsPowerDMDeciAmps45CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps45"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps45CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps46CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117198)
)
odsPowerDMDeciAmps46CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps46"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps46CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps47CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117199)
)
odsPowerDMDeciAmps47CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps47"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps47CLEAR.setStatus(
        "current"
    )

odsPowerDMDeciAmps48CLEAR = NotificationType(
    (1, 3, 6, 1, 4, 1, 29414, 1, 32767, 0, 117200)
)
odsPowerDMDeciAmps48CLEAR.setObjects(
      *(("ODS-MIB", "powerDMDeciAmps48"),
        ("ODS-MIB", "powerDMName"),
        ("ODS-MIB", "productFriendlyName"),
        ("ODS-MIB", "alarmTripType"))
)
if mibBuilder.loadTexts:
    odsPowerDMDeciAmps48CLEAR.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ODS-MIB",
    **{"opengate": opengate,
       "ods": ods,
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
       "dewPointSensorCount": dewPointSensorCount,
       "fancontrolCount": fancontrolCount,
       "tempSensorCount": tempSensorCount,
       "flowcontrolCount": flowcontrolCount,
       "powerDMCount": powerDMCount,
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
       "dewPointSensorTable": dewPointSensorTable,
       "dewPointSensorEntry": dewPointSensorEntry,
       "dewPointSensorIndex": dewPointSensorIndex,
       "dewPointSensorSerial": dewPointSensorSerial,
       "dewPointSensorName": dewPointSensorName,
       "dewPointSensorAvail": dewPointSensorAvail,
       "dewPointSensorTempC": dewPointSensorTempC,
       "dewPointSensorTempF": dewPointSensorTempF,
       "dewPointSensorHumidity": dewPointSensorHumidity,
       "dewPointSensorDewpointC": dewPointSensorDewpointC,
       "dewPointSensorDewpointF": dewPointSensorDewpointF,
       "fancontrolTable": fancontrolTable,
       "fancontrolEntry": fancontrolEntry,
       "fancontrolIndex": fancontrolIndex,
       "fancontrolSerial": fancontrolSerial,
       "fancontrolName": fancontrolName,
       "fancontrolAvail": fancontrolAvail,
       "fancontrolTempCreturnA": fancontrolTempCreturnA,
       "fancontrolTempFreturnA": fancontrolTempFreturnA,
       "fancontrolTempCreturnB": fancontrolTempCreturnB,
       "fancontrolTempFreturnB": fancontrolTempFreturnB,
       "fancontrolRpmFanA": fancontrolRpmFanA,
       "fancontrolRpmFanB": fancontrolRpmFanB,
       "fancontrolCapacityA": fancontrolCapacityA,
       "fancontrolCapacityB": fancontrolCapacityB,
       "fancontrolPressErr": fancontrolPressErr,
       "fancontrolPressDiff": fancontrolPressDiff,
       "fancontrolSetPoint": fancontrolSetPoint,
       "fancontrolCFM": fancontrolCFM,
       "fancontrolMCH": fancontrolMCH,
       "fancontrolTempCreturn": fancontrolTempCreturn,
       "fancontrolTempFreturn": fancontrolTempFreturn,
       "fancontrolCapacity": fancontrolCapacity,
       "fancontrolFanMissing": fancontrolFanMissing,
       "fancontrolFanMismatch": fancontrolFanMismatch,
       "fancontrolFanErrorA": fancontrolFanErrorA,
       "fancontrolFanErrorB": fancontrolFanErrorB,
       "fancontrolTempBus1": fancontrolTempBus1,
       "fancontrolPowerFeed": fancontrolPowerFeed,
       "fancontrolFanEndofLife": fancontrolFanEndofLife,
       "fancontrolTargetCapacity": fancontrolTargetCapacity,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorIndex": tempSensorIndex,
       "tempSensorSerial": tempSensorSerial,
       "tempSensorName": tempSensorName,
       "tempSensorAvail": tempSensorAvail,
       "tempSensorTempC": tempSensorTempC,
       "tempSensorTempF": tempSensorTempF,
       "flowcontrolTable": flowcontrolTable,
       "flowcontrolEntry": flowcontrolEntry,
       "flowcontrolIndex": flowcontrolIndex,
       "flowcontrolSerial": flowcontrolSerial,
       "flowcontrolName": flowcontrolName,
       "flowcontrolAvail": flowcontrolAvail,
       "flowcontrolRpmFan": flowcontrolRpmFan,
       "flowcontrolCapacity": flowcontrolCapacity,
       "flowcontrolPressErr": flowcontrolPressErr,
       "flowcontrolPressDiff": flowcontrolPressDiff,
       "flowcontrolSetPoint": flowcontrolSetPoint,
       "flowcontrolCFM": flowcontrolCFM,
       "flowcontrolMCH": flowcontrolMCH,
       "flowcontrolTempBus1": flowcontrolTempBus1,
       "flowcontrolPowerFeed": flowcontrolPowerFeed,
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
       "odsTrap": odsTrap,
       "odsTrapPrefix": odsTrapPrefix,
       "odsTestNOTIFY": odsTestNOTIFY,
       "odsClimateTempCNOTIFY": odsClimateTempCNOTIFY,
       "odsClimateTempFNOTIFY": odsClimateTempFNOTIFY,
       "odsClimateHumidityNOTIFY": odsClimateHumidityNOTIFY,
       "odsClimateLightNOTIFY": odsClimateLightNOTIFY,
       "odsClimateAirflowNOTIFY": odsClimateAirflowNOTIFY,
       "odsClimateSoundNOTIFY": odsClimateSoundNOTIFY,
       "odsClimateIO1NOTIFY": odsClimateIO1NOTIFY,
       "odsClimateIO2NOTIFY": odsClimateIO2NOTIFY,
       "odsClimateIO3NOTIFY": odsClimateIO3NOTIFY,
       "odsDewPointSensorTempCNOTIFY": odsDewPointSensorTempCNOTIFY,
       "odsDewPointSensorTempFNOTIFY": odsDewPointSensorTempFNOTIFY,
       "odsDewPointSensorHumidityNOTIFY": odsDewPointSensorHumidityNOTIFY,
       "odsDewPointSensorDewpointCNOTIFY": odsDewPointSensorDewpointCNOTIFY,
       "odsDewPointSensorDewpointFNOTIFY": odsDewPointSensorDewpointFNOTIFY,
       "odsFancontrolTempCreturnANOTIFY": odsFancontrolTempCreturnANOTIFY,
       "odsFancontrolTempFreturnANOTIFY": odsFancontrolTempFreturnANOTIFY,
       "odsFancontrolTempCreturnBNOTIFY": odsFancontrolTempCreturnBNOTIFY,
       "odsFancontrolTempFreturnBNOTIFY": odsFancontrolTempFreturnBNOTIFY,
       "odsFancontrolRpmFanANOTIFY": odsFancontrolRpmFanANOTIFY,
       "odsFancontrolRpmFanBNOTIFY": odsFancontrolRpmFanBNOTIFY,
       "odsFancontrolCapacityANOTIFY": odsFancontrolCapacityANOTIFY,
       "odsFancontrolCapacityBNOTIFY": odsFancontrolCapacityBNOTIFY,
       "odsFancontrolPressErrNOTIFY": odsFancontrolPressErrNOTIFY,
       "odsFancontrolPressDiffNOTIFY": odsFancontrolPressDiffNOTIFY,
       "odsFancontrolSetPointNOTIFY": odsFancontrolSetPointNOTIFY,
       "odsFancontrolCFMNOTIFY": odsFancontrolCFMNOTIFY,
       "odsFancontrolMCHNOTIFY": odsFancontrolMCHNOTIFY,
       "odsFancontrolTempCreturnNOTIFY": odsFancontrolTempCreturnNOTIFY,
       "odsFancontrolTempFreturnNOTIFY": odsFancontrolTempFreturnNOTIFY,
       "odsFancontrolCapacityNOTIFY": odsFancontrolCapacityNOTIFY,
       "odsFancontrolFanMissingNOTIFY": odsFancontrolFanMissingNOTIFY,
       "odsFancontrolFanMismatchNOTIFY": odsFancontrolFanMismatchNOTIFY,
       "odsFancontrolFanErrorANOTIFY": odsFancontrolFanErrorANOTIFY,
       "odsFancontrolFanErrorBNOTIFY": odsFancontrolFanErrorBNOTIFY,
       "odsFancontrolTempBus1NOTIFY": odsFancontrolTempBus1NOTIFY,
       "odsFancontrolPowerFeedNOTIFY": odsFancontrolPowerFeedNOTIFY,
       "odsFancontrolFanEndofLifeNOTIFY": odsFancontrolFanEndofLifeNOTIFY,
       "odsFancontrolTargetCapacityNOTIFY": odsFancontrolTargetCapacityNOTIFY,
       "odsTempSensorTempCNOTIFY": odsTempSensorTempCNOTIFY,
       "odsTempSensorTempFNOTIFY": odsTempSensorTempFNOTIFY,
       "odsFlowcontrolRpmFanNOTIFY": odsFlowcontrolRpmFanNOTIFY,
       "odsFlowcontrolCapacityNOTIFY": odsFlowcontrolCapacityNOTIFY,
       "odsFlowcontrolPressErrNOTIFY": odsFlowcontrolPressErrNOTIFY,
       "odsFlowcontrolPressDiffNOTIFY": odsFlowcontrolPressDiffNOTIFY,
       "odsFlowcontrolSetPointNOTIFY": odsFlowcontrolSetPointNOTIFY,
       "odsFlowcontrolCFMNOTIFY": odsFlowcontrolCFMNOTIFY,
       "odsFlowcontrolMCHNOTIFY": odsFlowcontrolMCHNOTIFY,
       "odsFlowcontrolTempBus1NOTIFY": odsFlowcontrolTempBus1NOTIFY,
       "odsFlowcontrolPowerFeedNOTIFY": odsFlowcontrolPowerFeedNOTIFY,
       "odsClimateTempCCLEAR": odsClimateTempCCLEAR,
       "odsClimateTempFCLEAR": odsClimateTempFCLEAR,
       "odsClimateHumidityCLEAR": odsClimateHumidityCLEAR,
       "odsClimateLightCLEAR": odsClimateLightCLEAR,
       "odsClimateAirflowCLEAR": odsClimateAirflowCLEAR,
       "odsClimateSoundCLEAR": odsClimateSoundCLEAR,
       "odsClimateIO1CLEAR": odsClimateIO1CLEAR,
       "odsClimateIO2CLEAR": odsClimateIO2CLEAR,
       "odsClimateIO3CLEAR": odsClimateIO3CLEAR,
       "odsDewPointSensorTempCCLEAR": odsDewPointSensorTempCCLEAR,
       "odsDewPointSensorTempFCLEAR": odsDewPointSensorTempFCLEAR,
       "odsDewPointSensorHumidityCLEAR": odsDewPointSensorHumidityCLEAR,
       "odsDewPointSensorDewpointCCLEAR": odsDewPointSensorDewpointCCLEAR,
       "odsDewPointSensorDewpointFCLEAR": odsDewPointSensorDewpointFCLEAR,
       "odsFancontrolTempCreturnACLEAR": odsFancontrolTempCreturnACLEAR,
       "odsFancontrolTempFreturnACLEAR": odsFancontrolTempFreturnACLEAR,
       "odsFancontrolTempCreturnBCLEAR": odsFancontrolTempCreturnBCLEAR,
       "odsFancontrolTempFreturnBCLEAR": odsFancontrolTempFreturnBCLEAR,
       "odsFancontrolRpmFanACLEAR": odsFancontrolRpmFanACLEAR,
       "odsFancontrolRpmFanBCLEAR": odsFancontrolRpmFanBCLEAR,
       "odsFancontrolCapacityACLEAR": odsFancontrolCapacityACLEAR,
       "odsFancontrolCapacityBCLEAR": odsFancontrolCapacityBCLEAR,
       "odsFancontrolPressErrCLEAR": odsFancontrolPressErrCLEAR,
       "odsFancontrolPressDiffCLEAR": odsFancontrolPressDiffCLEAR,
       "odsFancontrolSetPointCLEAR": odsFancontrolSetPointCLEAR,
       "odsFancontrolCFMCLEAR": odsFancontrolCFMCLEAR,
       "odsFancontrolMCHCLEAR": odsFancontrolMCHCLEAR,
       "odsFancontrolTempCreturnCLEAR": odsFancontrolTempCreturnCLEAR,
       "odsFancontrolTempFreturnCLEAR": odsFancontrolTempFreturnCLEAR,
       "odsFancontrolCapacityCLEAR": odsFancontrolCapacityCLEAR,
       "odsFancontrolFanMissingCLEAR": odsFancontrolFanMissingCLEAR,
       "odsFancontrolFanMismatchCLEAR": odsFancontrolFanMismatchCLEAR,
       "odsFancontrolFanErrorACLEAR": odsFancontrolFanErrorACLEAR,
       "odsFancontrolFanErrorBCLEAR": odsFancontrolFanErrorBCLEAR,
       "odsFancontrolTempBus1CLEAR": odsFancontrolTempBus1CLEAR,
       "odsFancontrolPowerFeedCLEAR": odsFancontrolPowerFeedCLEAR,
       "odsFancontrolFanEndofLifeCLEAR": odsFancontrolFanEndofLifeCLEAR,
       "odsFancontrolTargetCapacityCLEAR": odsFancontrolTargetCapacityCLEAR,
       "odsTempSensorTempCCLEAR": odsTempSensorTempCCLEAR,
       "odsTempSensorTempFCLEAR": odsTempSensorTempFCLEAR,
       "odsFlowcontrolRpmFanCLEAR": odsFlowcontrolRpmFanCLEAR,
       "odsFlowcontrolCapacityCLEAR": odsFlowcontrolCapacityCLEAR,
       "odsFlowcontrolPressErrCLEAR": odsFlowcontrolPressErrCLEAR,
       "odsFlowcontrolPressDiffCLEAR": odsFlowcontrolPressDiffCLEAR,
       "odsFlowcontrolSetPointCLEAR": odsFlowcontrolSetPointCLEAR,
       "odsFlowcontrolCFMCLEAR": odsFlowcontrolCFMCLEAR,
       "odsFlowcontrolMCHCLEAR": odsFlowcontrolMCHCLEAR,
       "odsFlowcontrolTempBus1CLEAR": odsFlowcontrolTempBus1CLEAR,
       "odsFlowcontrolPowerFeedCLEAR": odsFlowcontrolPowerFeedCLEAR,
       "odsPowerDMDeciAmps1NOTIFY": odsPowerDMDeciAmps1NOTIFY,
       "odsPowerDMDeciAmps2NOTIFY": odsPowerDMDeciAmps2NOTIFY,
       "odsPowerDMDeciAmps3NOTIFY": odsPowerDMDeciAmps3NOTIFY,
       "odsPowerDMDeciAmps4NOTIFY": odsPowerDMDeciAmps4NOTIFY,
       "odsPowerDMDeciAmps5NOTIFY": odsPowerDMDeciAmps5NOTIFY,
       "odsPowerDMDeciAmps6NOTIFY": odsPowerDMDeciAmps6NOTIFY,
       "odsPowerDMDeciAmps7NOTIFY": odsPowerDMDeciAmps7NOTIFY,
       "odsPowerDMDeciAmps8NOTIFY": odsPowerDMDeciAmps8NOTIFY,
       "odsPowerDMDeciAmps9NOTIFY": odsPowerDMDeciAmps9NOTIFY,
       "odsPowerDMDeciAmps10NOTIFY": odsPowerDMDeciAmps10NOTIFY,
       "odsPowerDMDeciAmps11NOTIFY": odsPowerDMDeciAmps11NOTIFY,
       "odsPowerDMDeciAmps12NOTIFY": odsPowerDMDeciAmps12NOTIFY,
       "odsPowerDMDeciAmps13NOTIFY": odsPowerDMDeciAmps13NOTIFY,
       "odsPowerDMDeciAmps14NOTIFY": odsPowerDMDeciAmps14NOTIFY,
       "odsPowerDMDeciAmps15NOTIFY": odsPowerDMDeciAmps15NOTIFY,
       "odsPowerDMDeciAmps16NOTIFY": odsPowerDMDeciAmps16NOTIFY,
       "odsPowerDMDeciAmps17NOTIFY": odsPowerDMDeciAmps17NOTIFY,
       "odsPowerDMDeciAmps18NOTIFY": odsPowerDMDeciAmps18NOTIFY,
       "odsPowerDMDeciAmps19NOTIFY": odsPowerDMDeciAmps19NOTIFY,
       "odsPowerDMDeciAmps20NOTIFY": odsPowerDMDeciAmps20NOTIFY,
       "odsPowerDMDeciAmps21NOTIFY": odsPowerDMDeciAmps21NOTIFY,
       "odsPowerDMDeciAmps22NOTIFY": odsPowerDMDeciAmps22NOTIFY,
       "odsPowerDMDeciAmps23NOTIFY": odsPowerDMDeciAmps23NOTIFY,
       "odsPowerDMDeciAmps24NOTIFY": odsPowerDMDeciAmps24NOTIFY,
       "odsPowerDMDeciAmps25NOTIFY": odsPowerDMDeciAmps25NOTIFY,
       "odsPowerDMDeciAmps26NOTIFY": odsPowerDMDeciAmps26NOTIFY,
       "odsPowerDMDeciAmps27NOTIFY": odsPowerDMDeciAmps27NOTIFY,
       "odsPowerDMDeciAmps28NOTIFY": odsPowerDMDeciAmps28NOTIFY,
       "odsPowerDMDeciAmps29NOTIFY": odsPowerDMDeciAmps29NOTIFY,
       "odsPowerDMDeciAmps30NOTIFY": odsPowerDMDeciAmps30NOTIFY,
       "odsPowerDMDeciAmps31NOTIFY": odsPowerDMDeciAmps31NOTIFY,
       "odsPowerDMDeciAmps32NOTIFY": odsPowerDMDeciAmps32NOTIFY,
       "odsPowerDMDeciAmps33NOTIFY": odsPowerDMDeciAmps33NOTIFY,
       "odsPowerDMDeciAmps34NOTIFY": odsPowerDMDeciAmps34NOTIFY,
       "odsPowerDMDeciAmps35NOTIFY": odsPowerDMDeciAmps35NOTIFY,
       "odsPowerDMDeciAmps36NOTIFY": odsPowerDMDeciAmps36NOTIFY,
       "odsPowerDMDeciAmps37NOTIFY": odsPowerDMDeciAmps37NOTIFY,
       "odsPowerDMDeciAmps38NOTIFY": odsPowerDMDeciAmps38NOTIFY,
       "odsPowerDMDeciAmps39NOTIFY": odsPowerDMDeciAmps39NOTIFY,
       "odsPowerDMDeciAmps40NOTIFY": odsPowerDMDeciAmps40NOTIFY,
       "odsPowerDMDeciAmps41NOTIFY": odsPowerDMDeciAmps41NOTIFY,
       "odsPowerDMDeciAmps42NOTIFY": odsPowerDMDeciAmps42NOTIFY,
       "odsPowerDMDeciAmps43NOTIFY": odsPowerDMDeciAmps43NOTIFY,
       "odsPowerDMDeciAmps44NOTIFY": odsPowerDMDeciAmps44NOTIFY,
       "odsPowerDMDeciAmps45NOTIFY": odsPowerDMDeciAmps45NOTIFY,
       "odsPowerDMDeciAmps46NOTIFY": odsPowerDMDeciAmps46NOTIFY,
       "odsPowerDMDeciAmps47NOTIFY": odsPowerDMDeciAmps47NOTIFY,
       "odsPowerDMDeciAmps48NOTIFY": odsPowerDMDeciAmps48NOTIFY,
       "odsPowerDMDeciAmps1CLEAR": odsPowerDMDeciAmps1CLEAR,
       "odsPowerDMDeciAmps2CLEAR": odsPowerDMDeciAmps2CLEAR,
       "odsPowerDMDeciAmps3CLEAR": odsPowerDMDeciAmps3CLEAR,
       "odsPowerDMDeciAmps4CLEAR": odsPowerDMDeciAmps4CLEAR,
       "odsPowerDMDeciAmps5CLEAR": odsPowerDMDeciAmps5CLEAR,
       "odsPowerDMDeciAmps6CLEAR": odsPowerDMDeciAmps6CLEAR,
       "odsPowerDMDeciAmps7CLEAR": odsPowerDMDeciAmps7CLEAR,
       "odsPowerDMDeciAmps8CLEAR": odsPowerDMDeciAmps8CLEAR,
       "odsPowerDMDeciAmps9CLEAR": odsPowerDMDeciAmps9CLEAR,
       "odsPowerDMDeciAmps10CLEAR": odsPowerDMDeciAmps10CLEAR,
       "odsPowerDMDeciAmps11CLEAR": odsPowerDMDeciAmps11CLEAR,
       "odsPowerDMDeciAmps12CLEAR": odsPowerDMDeciAmps12CLEAR,
       "odsPowerDMDeciAmps13CLEAR": odsPowerDMDeciAmps13CLEAR,
       "odsPowerDMDeciAmps14CLEAR": odsPowerDMDeciAmps14CLEAR,
       "odsPowerDMDeciAmps15CLEAR": odsPowerDMDeciAmps15CLEAR,
       "odsPowerDMDeciAmps16CLEAR": odsPowerDMDeciAmps16CLEAR,
       "odsPowerDMDeciAmps17CLEAR": odsPowerDMDeciAmps17CLEAR,
       "odsPowerDMDeciAmps18CLEAR": odsPowerDMDeciAmps18CLEAR,
       "odsPowerDMDeciAmps19CLEAR": odsPowerDMDeciAmps19CLEAR,
       "odsPowerDMDeciAmps20CLEAR": odsPowerDMDeciAmps20CLEAR,
       "odsPowerDMDeciAmps21CLEAR": odsPowerDMDeciAmps21CLEAR,
       "odsPowerDMDeciAmps22CLEAR": odsPowerDMDeciAmps22CLEAR,
       "odsPowerDMDeciAmps23CLEAR": odsPowerDMDeciAmps23CLEAR,
       "odsPowerDMDeciAmps24CLEAR": odsPowerDMDeciAmps24CLEAR,
       "odsPowerDMDeciAmps25CLEAR": odsPowerDMDeciAmps25CLEAR,
       "odsPowerDMDeciAmps26CLEAR": odsPowerDMDeciAmps26CLEAR,
       "odsPowerDMDeciAmps27CLEAR": odsPowerDMDeciAmps27CLEAR,
       "odsPowerDMDeciAmps28CLEAR": odsPowerDMDeciAmps28CLEAR,
       "odsPowerDMDeciAmps29CLEAR": odsPowerDMDeciAmps29CLEAR,
       "odsPowerDMDeciAmps30CLEAR": odsPowerDMDeciAmps30CLEAR,
       "odsPowerDMDeciAmps31CLEAR": odsPowerDMDeciAmps31CLEAR,
       "odsPowerDMDeciAmps32CLEAR": odsPowerDMDeciAmps32CLEAR,
       "odsPowerDMDeciAmps33CLEAR": odsPowerDMDeciAmps33CLEAR,
       "odsPowerDMDeciAmps34CLEAR": odsPowerDMDeciAmps34CLEAR,
       "odsPowerDMDeciAmps35CLEAR": odsPowerDMDeciAmps35CLEAR,
       "odsPowerDMDeciAmps36CLEAR": odsPowerDMDeciAmps36CLEAR,
       "odsPowerDMDeciAmps37CLEAR": odsPowerDMDeciAmps37CLEAR,
       "odsPowerDMDeciAmps38CLEAR": odsPowerDMDeciAmps38CLEAR,
       "odsPowerDMDeciAmps39CLEAR": odsPowerDMDeciAmps39CLEAR,
       "odsPowerDMDeciAmps40CLEAR": odsPowerDMDeciAmps40CLEAR,
       "odsPowerDMDeciAmps41CLEAR": odsPowerDMDeciAmps41CLEAR,
       "odsPowerDMDeciAmps42CLEAR": odsPowerDMDeciAmps42CLEAR,
       "odsPowerDMDeciAmps43CLEAR": odsPowerDMDeciAmps43CLEAR,
       "odsPowerDMDeciAmps44CLEAR": odsPowerDMDeciAmps44CLEAR,
       "odsPowerDMDeciAmps45CLEAR": odsPowerDMDeciAmps45CLEAR,
       "odsPowerDMDeciAmps46CLEAR": odsPowerDMDeciAmps46CLEAR,
       "odsPowerDMDeciAmps47CLEAR": odsPowerDMDeciAmps47CLEAR,
       "odsPowerDMDeciAmps48CLEAR": odsPowerDMDeciAmps48CLEAR}
)
