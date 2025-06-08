# SNMP MIB module (KMX-RACK) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kentix_37954/KMX-RACK.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:59:29 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Kentix_ObjectIdentity = ObjectIdentity
kentix = _Kentix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954)
)
_MultisensorRack_ObjectIdentity = ObjectIdentity
multisensorRack = _MultisensorRack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3)
)
_Datapoints_ObjectIdentity = ObjectIdentity
datapoints = _Datapoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1)
)
_TemperatureEntry_ObjectIdentity = ObjectIdentity
temperatureEntry = _TemperatureEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 1)
)


class _TemperatureValue_Type(Integer32):
    """Custom type temperatureValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TemperatureValue_Type.__name__ = "Integer32"
_TemperatureValue_Object = MibScalar
temperatureValue = _TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 1, 1),
    _TemperatureValue_Type()
)
temperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureValue.setStatus("mandatory")


class _TemperatureMin_Type(Integer32):
    """Custom type temperatureMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TemperatureMin_Type.__name__ = "Integer32"
_TemperatureMin_Object = MibScalar
temperatureMin = _TemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 1, 2),
    _TemperatureMin_Type()
)
temperatureMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureMin.setStatus("mandatory")


class _TemperatureMax_Type(Integer32):
    """Custom type temperatureMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TemperatureMax_Type.__name__ = "Integer32"
_TemperatureMax_Object = MibScalar
temperatureMax = _TemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 1, 3),
    _TemperatureMax_Type()
)
temperatureMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureMax.setStatus("mandatory")


class _TemperatureAlarm_Type(Integer32):
    """Custom type temperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TemperatureAlarm_Type.__name__ = "Integer32"
_TemperatureAlarm_Object = MibScalar
temperatureAlarm = _TemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 1, 4),
    _TemperatureAlarm_Type()
)
temperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureAlarm.setStatus("mandatory")
_TemperatureAlarmtext_Type = DisplayString
_TemperatureAlarmtext_Object = MibScalar
temperatureAlarmtext = _TemperatureAlarmtext_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 1, 5),
    _TemperatureAlarmtext_Type()
)
temperatureAlarmtext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureAlarmtext.setStatus("mandatory")


class _TemperatureAlarmArm_Type(Integer32):
    """Custom type temperatureAlarmArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TemperatureAlarmArm_Type.__name__ = "Integer32"
_TemperatureAlarmArm_Object = MibScalar
temperatureAlarmArm = _TemperatureAlarmArm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 1, 6),
    _TemperatureAlarmArm_Type()
)
temperatureAlarmArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureAlarmArm.setStatus("mandatory")
_HumidityEntry_ObjectIdentity = ObjectIdentity
humidityEntry = _HumidityEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 2)
)


class _HumidityValue_Type(Integer32):
    """Custom type humidityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HumidityValue_Type.__name__ = "Integer32"
_HumidityValue_Object = MibScalar
humidityValue = _HumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 2, 1),
    _HumidityValue_Type()
)
humidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityValue.setStatus("mandatory")


class _HumidityMin_Type(Integer32):
    """Custom type humidityMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_HumidityMin_Type.__name__ = "Integer32"
_HumidityMin_Object = MibScalar
humidityMin = _HumidityMin_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 2, 2),
    _HumidityMin_Type()
)
humidityMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityMin.setStatus("mandatory")


class _HumidityMax_Type(Integer32):
    """Custom type humidityMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_HumidityMax_Type.__name__ = "Integer32"
_HumidityMax_Object = MibScalar
humidityMax = _HumidityMax_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 2, 3),
    _HumidityMax_Type()
)
humidityMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityMax.setStatus("mandatory")


class _HumidityAlarm_Type(Integer32):
    """Custom type humidityAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HumidityAlarm_Type.__name__ = "Integer32"
_HumidityAlarm_Object = MibScalar
humidityAlarm = _HumidityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 2, 4),
    _HumidityAlarm_Type()
)
humidityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityAlarm.setStatus("mandatory")
_HumidityAlarmtext_Type = DisplayString
_HumidityAlarmtext_Object = MibScalar
humidityAlarmtext = _HumidityAlarmtext_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 2, 5),
    _HumidityAlarmtext_Type()
)
humidityAlarmtext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityAlarmtext.setStatus("mandatory")


class _HumidityAlarmArm_Type(Integer32):
    """Custom type humidityAlarmArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HumidityAlarmArm_Type.__name__ = "Integer32"
_HumidityAlarmArm_Object = MibScalar
humidityAlarmArm = _HumidityAlarmArm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 2, 6),
    _HumidityAlarmArm_Type()
)
humidityAlarmArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityAlarmArm.setStatus("mandatory")
_DewpointEntry_ObjectIdentity = ObjectIdentity
dewpointEntry = _DewpointEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 3)
)


class _DewpointValue_Type(Integer32):
    """Custom type dewpointValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DewpointValue_Type.__name__ = "Integer32"
_DewpointValue_Object = MibScalar
dewpointValue = _DewpointValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 3, 1),
    _DewpointValue_Type()
)
dewpointValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpointValue.setStatus("mandatory")


class _DewpointMin_Type(Integer32):
    """Custom type dewpointMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DewpointMin_Type.__name__ = "Integer32"
_DewpointMin_Object = MibScalar
dewpointMin = _DewpointMin_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 3, 2),
    _DewpointMin_Type()
)
dewpointMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dewpointMin.setStatus("mandatory")


class _DewpointAlarm_Type(Integer32):
    """Custom type dewpointAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DewpointAlarm_Type.__name__ = "Integer32"
_DewpointAlarm_Object = MibScalar
dewpointAlarm = _DewpointAlarm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 3, 3),
    _DewpointAlarm_Type()
)
dewpointAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpointAlarm.setStatus("mandatory")
_DewpointAlarmtext_Type = DisplayString
_DewpointAlarmtext_Object = MibScalar
dewpointAlarmtext = _DewpointAlarmtext_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 3, 4),
    _DewpointAlarmtext_Type()
)
dewpointAlarmtext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpointAlarmtext.setStatus("mandatory")


class _DewpointAlarmArm_Type(Integer32):
    """Custom type dewpointAlarmArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DewpointAlarmArm_Type.__name__ = "Integer32"
_DewpointAlarmArm_Object = MibScalar
dewpointAlarmArm = _DewpointAlarmArm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 3, 6),
    _DewpointAlarmArm_Type()
)
dewpointAlarmArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dewpointAlarmArm.setStatus("mandatory")
_CoEntry_ObjectIdentity = ObjectIdentity
coEntry = _CoEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 4)
)


class _CoValue_Type(Integer32):
    """Custom type coValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_CoValue_Type.__name__ = "Integer32"
_CoValue_Object = MibScalar
coValue = _CoValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 4, 1),
    _CoValue_Type()
)
coValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coValue.setStatus("mandatory")


class _CoMax_Type(Integer32):
    """Custom type coMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CoMax_Type.__name__ = "Integer32"
_CoMax_Object = MibScalar
coMax = _CoMax_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 4, 2),
    _CoMax_Type()
)
coMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coMax.setStatus("mandatory")


class _CoAlarm_Type(Integer32):
    """Custom type coAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CoAlarm_Type.__name__ = "Integer32"
_CoAlarm_Object = MibScalar
coAlarm = _CoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 4, 3),
    _CoAlarm_Type()
)
coAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coAlarm.setStatus("mandatory")
_CoAlarmtext_Type = DisplayString
_CoAlarmtext_Object = MibScalar
coAlarmtext = _CoAlarmtext_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 4, 4),
    _CoAlarmtext_Type()
)
coAlarmtext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coAlarmtext.setStatus("mandatory")


class _CoAlarmArm_Type(Integer32):
    """Custom type coAlarmArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CoAlarmArm_Type.__name__ = "Integer32"
_CoAlarmArm_Object = MibScalar
coAlarmArm = _CoAlarmArm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 4, 6),
    _CoAlarmArm_Type()
)
coAlarmArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coAlarmArm.setStatus("mandatory")
_MotionEntry_ObjectIdentity = ObjectIdentity
motionEntry = _MotionEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 5)
)


class _MotionValue_Type(Integer32):
    """Custom type motionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MotionValue_Type.__name__ = "Integer32"
_MotionValue_Object = MibScalar
motionValue = _MotionValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 5, 1),
    _MotionValue_Type()
)
motionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motionValue.setStatus("mandatory")


class _MotionMax_Type(Integer32):
    """Custom type motionMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_MotionMax_Type.__name__ = "Integer32"
_MotionMax_Object = MibScalar
motionMax = _MotionMax_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 5, 2),
    _MotionMax_Type()
)
motionMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    motionMax.setStatus("mandatory")


class _MotionAlarm_Type(Integer32):
    """Custom type motionAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MotionAlarm_Type.__name__ = "Integer32"
_MotionAlarm_Object = MibScalar
motionAlarm = _MotionAlarm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 5, 3),
    _MotionAlarm_Type()
)
motionAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motionAlarm.setStatus("mandatory")
_MotionAlarmtext_Type = DisplayString
_MotionAlarmtext_Object = MibScalar
motionAlarmtext = _MotionAlarmtext_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 5, 4),
    _MotionAlarmtext_Type()
)
motionAlarmtext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motionAlarmtext.setStatus("mandatory")


class _MotionAlarmArm_Type(Integer32):
    """Custom type motionAlarmArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MotionAlarmArm_Type.__name__ = "Integer32"
_MotionAlarmArm_Object = MibScalar
motionAlarmArm = _MotionAlarmArm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 5, 6),
    _MotionAlarmArm_Type()
)
motionAlarmArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    motionAlarmArm.setStatus("mandatory")
_DigitalIn1_ObjectIdentity = ObjectIdentity
digitalIn1 = _DigitalIn1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 6)
)


class _DigitalIn1Value_Type(Integer32):
    """Custom type digitalIn1Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DigitalIn1Value_Type.__name__ = "Integer32"
_DigitalIn1Value_Object = MibScalar
digitalIn1Value = _DigitalIn1Value_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 6, 1),
    _DigitalIn1Value_Type()
)
digitalIn1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalIn1Value.setStatus("mandatory")
_DigitalIn1Name_Type = DisplayString
_DigitalIn1Name_Object = MibScalar
digitalIn1Name = _DigitalIn1Name_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 6, 2),
    _DigitalIn1Name_Type()
)
digitalIn1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalIn1Name.setStatus("mandatory")
_DigitalIn2_ObjectIdentity = ObjectIdentity
digitalIn2 = _DigitalIn2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 7)
)


class _DigitalIn2Value_Type(Integer32):
    """Custom type digitalIn2Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DigitalIn2Value_Type.__name__ = "Integer32"
_DigitalIn2Value_Object = MibScalar
digitalIn2Value = _DigitalIn2Value_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 7, 1),
    _DigitalIn2Value_Type()
)
digitalIn2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalIn2Value.setStatus("mandatory")
_DigitalIn2Name_Type = DisplayString
_DigitalIn2Name_Object = MibScalar
digitalIn2Name = _DigitalIn2Name_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 7, 2),
    _DigitalIn2Name_Type()
)
digitalIn2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalIn2Name.setStatus("mandatory")
_DigitalOut2_ObjectIdentity = ObjectIdentity
digitalOut2 = _DigitalOut2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 8)
)


class _DigitalOut2Value_Type(Integer32):
    """Custom type digitalOut2Value based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DigitalOut2Value_Type.__name__ = "Integer32"
_DigitalOut2Value_Object = MibScalar
digitalOut2Value = _DigitalOut2Value_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 8, 1),
    _DigitalOut2Value_Type()
)
digitalOut2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalOut2Value.setStatus("mandatory")
_BuzzerTime_ObjectIdentity = ObjectIdentity
buzzerTime = _BuzzerTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 9)
)


class _BuzzerTimeValue_Type(Integer32):
    """Custom type buzzerTimeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_BuzzerTimeValue_Type.__name__ = "Integer32"
_BuzzerTimeValue_Object = MibScalar
buzzerTimeValue = _BuzzerTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 9, 1),
    _BuzzerTimeValue_Type()
)
buzzerTimeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buzzerTimeValue.setStatus("mandatory")
_RelayTime_ObjectIdentity = ObjectIdentity
relayTime = _RelayTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 10)
)


class _RelayTimeValue_Type(Integer32):
    """Custom type relayTimeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_RelayTimeValue_Type.__name__ = "Integer32"
_RelayTimeValue_Object = MibScalar
relayTimeValue = _RelayTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 10, 1),
    _RelayTimeValue_Type()
)
relayTimeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayTimeValue.setStatus("mandatory")
_RearmMotion_ObjectIdentity = ObjectIdentity
rearmMotion = _RearmMotion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 11)
)


class _RearmMotionValue_Type(Integer32):
    """Custom type rearmMotionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_RearmMotionValue_Type.__name__ = "Integer32"
_RearmMotionValue_Object = MibScalar
rearmMotionValue = _RearmMotionValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 11, 1),
    _RearmMotionValue_Type()
)
rearmMotionValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rearmMotionValue.setStatus("mandatory")
_Pdu1_ObjectIdentity = ObjectIdentity
pdu1 = _Pdu1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12)
)


class _Pdu1activepowerValue_Type(Integer32):
    """Custom type pdu1activepowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_Pdu1activepowerValue_Type.__name__ = "Integer32"
_Pdu1activepowerValue_Object = MibScalar
pdu1activepowerValue = _Pdu1activepowerValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 1),
    _Pdu1activepowerValue_Type()
)
pdu1activepowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1activepowerValue.setStatus("mandatory")


class _Pdu1apparentpowerValue_Type(Integer32):
    """Custom type pdu1apparentpowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_Pdu1apparentpowerValue_Type.__name__ = "Integer32"
_Pdu1apparentpowerValue_Object = MibScalar
pdu1apparentpowerValue = _Pdu1apparentpowerValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 2),
    _Pdu1apparentpowerValue_Type()
)
pdu1apparentpowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1apparentpowerValue.setStatus("mandatory")


class _Pdu1energyValue_Type(Integer32):
    """Custom type pdu1energyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_Pdu1energyValue_Type.__name__ = "Integer32"
_Pdu1energyValue_Object = MibScalar
pdu1energyValue = _Pdu1energyValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 3),
    _Pdu1energyValue_Type()
)
pdu1energyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1energyValue.setStatus("mandatory")


class _Pdu1energycostsValue_Type(Integer32):
    """Custom type pdu1energycostsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_Pdu1energycostsValue_Type.__name__ = "Integer32"
_Pdu1energycostsValue_Object = MibScalar
pdu1energycostsValue = _Pdu1energycostsValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 4),
    _Pdu1energycostsValue_Type()
)
pdu1energycostsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1energycostsValue.setStatus("mandatory")


class _Pdu1currentValue_Type(Integer32):
    """Custom type pdu1currentValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pdu1currentValue_Type.__name__ = "Integer32"
_Pdu1currentValue_Object = MibScalar
pdu1currentValue = _Pdu1currentValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 5),
    _Pdu1currentValue_Type()
)
pdu1currentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1currentValue.setStatus("mandatory")


class _Pdu1voltageValue_Type(Integer32):
    """Custom type pdu1voltageValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Pdu1voltageValue_Type.__name__ = "Integer32"
_Pdu1voltageValue_Object = MibScalar
pdu1voltageValue = _Pdu1voltageValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 6),
    _Pdu1voltageValue_Type()
)
pdu1voltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1voltageValue.setStatus("mandatory")


class _Pdu1powerfactorValue_Type(Integer32):
    """Custom type pdu1powerfactorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pdu1powerfactorValue_Type.__name__ = "Integer32"
_Pdu1powerfactorValue_Object = MibScalar
pdu1powerfactorValue = _Pdu1powerfactorValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 7),
    _Pdu1powerfactorValue_Type()
)
pdu1powerfactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1powerfactorValue.setStatus("mandatory")


class _Pdu1frequencyValue_Type(Integer32):
    """Custom type pdu1frequencyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pdu1frequencyValue_Type.__name__ = "Integer32"
_Pdu1frequencyValue_Object = MibScalar
pdu1frequencyValue = _Pdu1frequencyValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 8),
    _Pdu1frequencyValue_Type()
)
pdu1frequencyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1frequencyValue.setStatus("mandatory")
_Pdu1VoltageFlicker_ObjectIdentity = ObjectIdentity
pdu1VoltageFlicker = _Pdu1VoltageFlicker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 9)
)


class _Pdu1VoltageFlickerValue_Type(Integer32):
    """Custom type pdu1VoltageFlickerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu1VoltageFlickerValue_Type.__name__ = "Integer32"
_Pdu1VoltageFlickerValue_Object = MibScalar
pdu1VoltageFlickerValue = _Pdu1VoltageFlickerValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 9, 1),
    _Pdu1VoltageFlickerValue_Type()
)
pdu1VoltageFlickerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1VoltageFlickerValue.setStatus("mandatory")
_Pdu1VoltageFlickerTime_Type = DisplayString
_Pdu1VoltageFlickerTime_Object = MibScalar
pdu1VoltageFlickerTime = _Pdu1VoltageFlickerTime_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 9, 2),
    _Pdu1VoltageFlickerTime_Type()
)
pdu1VoltageFlickerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1VoltageFlickerTime.setStatus("mandatory")


class _Pdu1VoltageFlickerState_Type(Integer32):
    """Custom type pdu1VoltageFlickerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu1VoltageFlickerState_Type.__name__ = "Integer32"
_Pdu1VoltageFlickerState_Object = MibScalar
pdu1VoltageFlickerState = _Pdu1VoltageFlickerState_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 9, 3),
    _Pdu1VoltageFlickerState_Type()
)
pdu1VoltageFlickerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1VoltageFlickerState.setStatus("mandatory")
_Pdu1VoltageSwell_ObjectIdentity = ObjectIdentity
pdu1VoltageSwell = _Pdu1VoltageSwell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 10)
)


class _Pdu1VoltageSwellValue_Type(Integer32):
    """Custom type pdu1VoltageSwellValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu1VoltageSwellValue_Type.__name__ = "Integer32"
_Pdu1VoltageSwellValue_Object = MibScalar
pdu1VoltageSwellValue = _Pdu1VoltageSwellValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 10, 1),
    _Pdu1VoltageSwellValue_Type()
)
pdu1VoltageSwellValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1VoltageSwellValue.setStatus("mandatory")
_Pdu1VoltageSwellTime_Type = DisplayString
_Pdu1VoltageSwellTime_Object = MibScalar
pdu1VoltageSwellTime = _Pdu1VoltageSwellTime_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 10, 2),
    _Pdu1VoltageSwellTime_Type()
)
pdu1VoltageSwellTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1VoltageSwellTime.setStatus("mandatory")


class _Pdu1VoltageSwellState_Type(Integer32):
    """Custom type pdu1VoltageSwellState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu1VoltageSwellState_Type.__name__ = "Integer32"
_Pdu1VoltageSwellState_Object = MibScalar
pdu1VoltageSwellState = _Pdu1VoltageSwellState_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 10, 3),
    _Pdu1VoltageSwellState_Type()
)
pdu1VoltageSwellState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1VoltageSwellState.setStatus("mandatory")
_Pdu1VoltagePeak_ObjectIdentity = ObjectIdentity
pdu1VoltagePeak = _Pdu1VoltagePeak_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 11)
)


class _Pdu1VoltagePeakValue_Type(Integer32):
    """Custom type pdu1VoltagePeakValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu1VoltagePeakValue_Type.__name__ = "Integer32"
_Pdu1VoltagePeakValue_Object = MibScalar
pdu1VoltagePeakValue = _Pdu1VoltagePeakValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 11, 1),
    _Pdu1VoltagePeakValue_Type()
)
pdu1VoltagePeakValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1VoltagePeakValue.setStatus("mandatory")
_Pdu1VoltagePeakTime_Type = DisplayString
_Pdu1VoltagePeakTime_Object = MibScalar
pdu1VoltagePeakTime = _Pdu1VoltagePeakTime_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 11, 2),
    _Pdu1VoltagePeakTime_Type()
)
pdu1VoltagePeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1VoltagePeakTime.setStatus("mandatory")


class _Pdu1VoltagePeakState_Type(Integer32):
    """Custom type pdu1VoltagePeakState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu1VoltagePeakState_Type.__name__ = "Integer32"
_Pdu1VoltagePeakState_Object = MibScalar
pdu1VoltagePeakState = _Pdu1VoltagePeakState_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 12, 11, 3),
    _Pdu1VoltagePeakState_Type()
)
pdu1VoltagePeakState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu1VoltagePeakState.setStatus("mandatory")
_Pdu2_ObjectIdentity = ObjectIdentity
pdu2 = _Pdu2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13)
)


class _Pdu2activepowerValue_Type(Integer32):
    """Custom type pdu2activepowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_Pdu2activepowerValue_Type.__name__ = "Integer32"
_Pdu2activepowerValue_Object = MibScalar
pdu2activepowerValue = _Pdu2activepowerValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 1),
    _Pdu2activepowerValue_Type()
)
pdu2activepowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2activepowerValue.setStatus("mandatory")


class _Pdu2apparentpowerValue_Type(Integer32):
    """Custom type pdu2apparentpowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_Pdu2apparentpowerValue_Type.__name__ = "Integer32"
_Pdu2apparentpowerValue_Object = MibScalar
pdu2apparentpowerValue = _Pdu2apparentpowerValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 2),
    _Pdu2apparentpowerValue_Type()
)
pdu2apparentpowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2apparentpowerValue.setStatus("mandatory")


class _Pdu2energyValue_Type(Integer32):
    """Custom type pdu2energyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_Pdu2energyValue_Type.__name__ = "Integer32"
_Pdu2energyValue_Object = MibScalar
pdu2energyValue = _Pdu2energyValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 3),
    _Pdu2energyValue_Type()
)
pdu2energyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2energyValue.setStatus("mandatory")


class _Pdu2energycostsValue_Type(Integer32):
    """Custom type pdu2energycostsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_Pdu2energycostsValue_Type.__name__ = "Integer32"
_Pdu2energycostsValue_Object = MibScalar
pdu2energycostsValue = _Pdu2energycostsValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 4),
    _Pdu2energycostsValue_Type()
)
pdu2energycostsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2energycostsValue.setStatus("mandatory")


class _Pdu2currentValue_Type(Integer32):
    """Custom type pdu2currentValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pdu2currentValue_Type.__name__ = "Integer32"
_Pdu2currentValue_Object = MibScalar
pdu2currentValue = _Pdu2currentValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 5),
    _Pdu2currentValue_Type()
)
pdu2currentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2currentValue.setStatus("mandatory")


class _Pdu2voltageValue_Type(Integer32):
    """Custom type pdu2voltageValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Pdu2voltageValue_Type.__name__ = "Integer32"
_Pdu2voltageValue_Object = MibScalar
pdu2voltageValue = _Pdu2voltageValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 6),
    _Pdu2voltageValue_Type()
)
pdu2voltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2voltageValue.setStatus("mandatory")


class _Pdu2powerfactorValue_Type(Integer32):
    """Custom type pdu2powerfactorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pdu2powerfactorValue_Type.__name__ = "Integer32"
_Pdu2powerfactorValue_Object = MibScalar
pdu2powerfactorValue = _Pdu2powerfactorValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 7),
    _Pdu2powerfactorValue_Type()
)
pdu2powerfactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2powerfactorValue.setStatus("mandatory")


class _Pdu2frequencyValue_Type(Integer32):
    """Custom type pdu2frequencyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pdu2frequencyValue_Type.__name__ = "Integer32"
_Pdu2frequencyValue_Object = MibScalar
pdu2frequencyValue = _Pdu2frequencyValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 8),
    _Pdu2frequencyValue_Type()
)
pdu2frequencyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2frequencyValue.setStatus("mandatory")
_Pdu2VoltageFlicker_ObjectIdentity = ObjectIdentity
pdu2VoltageFlicker = _Pdu2VoltageFlicker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 9)
)


class _Pdu2VoltageFlickerValue_Type(Integer32):
    """Custom type pdu2VoltageFlickerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu2VoltageFlickerValue_Type.__name__ = "Integer32"
_Pdu2VoltageFlickerValue_Object = MibScalar
pdu2VoltageFlickerValue = _Pdu2VoltageFlickerValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 9, 1),
    _Pdu2VoltageFlickerValue_Type()
)
pdu2VoltageFlickerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2VoltageFlickerValue.setStatus("mandatory")
_Pdu2VoltageFlickerTime_Type = DisplayString
_Pdu2VoltageFlickerTime_Object = MibScalar
pdu2VoltageFlickerTime = _Pdu2VoltageFlickerTime_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 9, 2),
    _Pdu2VoltageFlickerTime_Type()
)
pdu2VoltageFlickerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2VoltageFlickerTime.setStatus("mandatory")


class _Pdu2VoltageFlickerState_Type(Integer32):
    """Custom type pdu2VoltageFlickerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu2VoltageFlickerState_Type.__name__ = "Integer32"
_Pdu2VoltageFlickerState_Object = MibScalar
pdu2VoltageFlickerState = _Pdu2VoltageFlickerState_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 9, 3),
    _Pdu2VoltageFlickerState_Type()
)
pdu2VoltageFlickerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2VoltageFlickerState.setStatus("mandatory")
_Pdu2VoltageSwell_ObjectIdentity = ObjectIdentity
pdu2VoltageSwell = _Pdu2VoltageSwell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 10)
)


class _Pdu2VoltageSwellValue_Type(Integer32):
    """Custom type pdu2VoltageSwellValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu2VoltageSwellValue_Type.__name__ = "Integer32"
_Pdu2VoltageSwellValue_Object = MibScalar
pdu2VoltageSwellValue = _Pdu2VoltageSwellValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 10, 1),
    _Pdu2VoltageSwellValue_Type()
)
pdu2VoltageSwellValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2VoltageSwellValue.setStatus("mandatory")
_Pdu2VoltageSwellTime_Type = DisplayString
_Pdu2VoltageSwellTime_Object = MibScalar
pdu2VoltageSwellTime = _Pdu2VoltageSwellTime_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 10, 2),
    _Pdu2VoltageSwellTime_Type()
)
pdu2VoltageSwellTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2VoltageSwellTime.setStatus("mandatory")


class _Pdu2VoltageSwellState_Type(Integer32):
    """Custom type pdu2VoltageSwellState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu2VoltageSwellState_Type.__name__ = "Integer32"
_Pdu2VoltageSwellState_Object = MibScalar
pdu2VoltageSwellState = _Pdu2VoltageSwellState_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 10, 3),
    _Pdu2VoltageSwellState_Type()
)
pdu2VoltageSwellState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2VoltageSwellState.setStatus("mandatory")
_Pdu2VoltagePeak_ObjectIdentity = ObjectIdentity
pdu2VoltagePeak = _Pdu2VoltagePeak_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 11)
)


class _Pdu2VoltagePeakValue_Type(Integer32):
    """Custom type pdu2VoltagePeakValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Pdu2VoltagePeakValue_Type.__name__ = "Integer32"
_Pdu2VoltagePeakValue_Object = MibScalar
pdu2VoltagePeakValue = _Pdu2VoltagePeakValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 11, 1),
    _Pdu2VoltagePeakValue_Type()
)
pdu2VoltagePeakValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2VoltagePeakValue.setStatus("mandatory")
_Pdu2VoltagePeakTime_Type = DisplayString
_Pdu2VoltagePeakTime_Object = MibScalar
pdu2VoltagePeakTime = _Pdu2VoltagePeakTime_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 11, 2),
    _Pdu2VoltagePeakTime_Type()
)
pdu2VoltagePeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2VoltagePeakTime.setStatus("mandatory")


class _Pdu2VoltagePeakState_Type(Integer32):
    """Custom type pdu2VoltagePeakState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu2VoltagePeakState_Type.__name__ = "Integer32"
_Pdu2VoltagePeakState_Object = MibScalar
pdu2VoltagePeakState = _Pdu2VoltagePeakState_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 13, 11, 3),
    _Pdu2VoltagePeakState_Type()
)
pdu2VoltagePeakState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2VoltagePeakState.setStatus("mandatory")
_Pdusum_ObjectIdentity = ObjectIdentity
pdusum = _Pdusum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 14)
)


class _PdusumactivepowerValue_Type(Integer32):
    """Custom type pdusumactivepowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PdusumactivepowerValue_Type.__name__ = "Integer32"
_PdusumactivepowerValue_Object = MibScalar
pdusumactivepowerValue = _PdusumactivepowerValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 14, 1),
    _PdusumactivepowerValue_Type()
)
pdusumactivepowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdusumactivepowerValue.setStatus("mandatory")


class _PdusumapparentpowerValue_Type(Integer32):
    """Custom type pdusumapparentpowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PdusumapparentpowerValue_Type.__name__ = "Integer32"
_PdusumapparentpowerValue_Object = MibScalar
pdusumapparentpowerValue = _PdusumapparentpowerValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 14, 2),
    _PdusumapparentpowerValue_Type()
)
pdusumapparentpowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdusumapparentpowerValue.setStatus("mandatory")


class _PdusumenergyValue_Type(Integer32):
    """Custom type pdusumenergyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_PdusumenergyValue_Type.__name__ = "Integer32"
_PdusumenergyValue_Object = MibScalar
pdusumenergyValue = _PdusumenergyValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 14, 3),
    _PdusumenergyValue_Type()
)
pdusumenergyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdusumenergyValue.setStatus("mandatory")


class _PdusumenergycostsValue_Type(Integer32):
    """Custom type pdusumenergycostsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000000),
    )


_PdusumenergycostsValue_Type.__name__ = "Integer32"
_PdusumenergycostsValue_Object = MibScalar
pdusumenergycostsValue = _PdusumenergycostsValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 14, 4),
    _PdusumenergycostsValue_Type()
)
pdusumenergycostsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdusumenergycostsValue.setStatus("mandatory")


class _PdusumcurrentValue_Type(Integer32):
    """Custom type pdusumcurrentValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PdusumcurrentValue_Type.__name__ = "Integer32"
_PdusumcurrentValue_Object = MibScalar
pdusumcurrentValue = _PdusumcurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 14, 5),
    _PdusumcurrentValue_Type()
)
pdusumcurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdusumcurrentValue.setStatus("mandatory")


class _PdusumvoltageValue_Type(Integer32):
    """Custom type pdusumvoltageValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PdusumvoltageValue_Type.__name__ = "Integer32"
_PdusumvoltageValue_Object = MibScalar
pdusumvoltageValue = _PdusumvoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 14, 6),
    _PdusumvoltageValue_Type()
)
pdusumvoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdusumvoltageValue.setStatus("mandatory")


class _PdusumpowerfactorValue_Type(Integer32):
    """Custom type pdusumpowerfactorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PdusumpowerfactorValue_Type.__name__ = "Integer32"
_PdusumpowerfactorValue_Object = MibScalar
pdusumpowerfactorValue = _PdusumpowerfactorValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 14, 7),
    _PdusumpowerfactorValue_Type()
)
pdusumpowerfactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdusumpowerfactorValue.setStatus("mandatory")


class _PdusumfrequencyValue_Type(Integer32):
    """Custom type pdusumfrequencyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PdusumfrequencyValue_Type.__name__ = "Integer32"
_PdusumfrequencyValue_Object = MibScalar
pdusumfrequencyValue = _PdusumfrequencyValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 1, 14, 8),
    _PdusumfrequencyValue_Type()
)
pdusumfrequencyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdusumfrequencyValue.setStatus("mandatory")
_AlarmText_Type = DisplayString
_AlarmText_Object = MibScalar
alarmText = _AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 37954, 3, 2),
    _AlarmText_Type()
)
alarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmText.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wrongLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 37954, 0, 1)
)
if mibBuilder.loadTexts:
    wrongLogin.setStatus(
        ""
    )

login = NotificationType(
    (1, 3, 6, 1, 4, 1, 37954, 0, 2)
)
if mibBuilder.loadTexts:
    login.setStatus(
        ""
    )

alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37954, 0, 3)
)
alarm.setObjects(
    ("KMX-RACK", "alarmText")
)
if mibBuilder.loadTexts:
    alarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KMX-RACK",
    **{"kentix": kentix,
       "wrongLogin": wrongLogin,
       "login": login,
       "alarm": alarm,
       "multisensorRack": multisensorRack,
       "datapoints": datapoints,
       "temperatureEntry": temperatureEntry,
       "temperatureValue": temperatureValue,
       "temperatureMin": temperatureMin,
       "temperatureMax": temperatureMax,
       "temperatureAlarm": temperatureAlarm,
       "temperatureAlarmtext": temperatureAlarmtext,
       "temperatureAlarmArm": temperatureAlarmArm,
       "humidityEntry": humidityEntry,
       "humidityValue": humidityValue,
       "humidityMin": humidityMin,
       "humidityMax": humidityMax,
       "humidityAlarm": humidityAlarm,
       "humidityAlarmtext": humidityAlarmtext,
       "humidityAlarmArm": humidityAlarmArm,
       "dewpointEntry": dewpointEntry,
       "dewpointValue": dewpointValue,
       "dewpointMin": dewpointMin,
       "dewpointAlarm": dewpointAlarm,
       "dewpointAlarmtext": dewpointAlarmtext,
       "dewpointAlarmArm": dewpointAlarmArm,
       "coEntry": coEntry,
       "coValue": coValue,
       "coMax": coMax,
       "coAlarm": coAlarm,
       "coAlarmtext": coAlarmtext,
       "coAlarmArm": coAlarmArm,
       "motionEntry": motionEntry,
       "motionValue": motionValue,
       "motionMax": motionMax,
       "motionAlarm": motionAlarm,
       "motionAlarmtext": motionAlarmtext,
       "motionAlarmArm": motionAlarmArm,
       "digitalIn1": digitalIn1,
       "digitalIn1Value": digitalIn1Value,
       "digitalIn1Name": digitalIn1Name,
       "digitalIn2": digitalIn2,
       "digitalIn2Value": digitalIn2Value,
       "digitalIn2Name": digitalIn2Name,
       "digitalOut2": digitalOut2,
       "digitalOut2Value": digitalOut2Value,
       "buzzerTime": buzzerTime,
       "buzzerTimeValue": buzzerTimeValue,
       "relayTime": relayTime,
       "relayTimeValue": relayTimeValue,
       "rearmMotion": rearmMotion,
       "rearmMotionValue": rearmMotionValue,
       "pdu1": pdu1,
       "pdu1activepowerValue": pdu1activepowerValue,
       "pdu1apparentpowerValue": pdu1apparentpowerValue,
       "pdu1energyValue": pdu1energyValue,
       "pdu1energycostsValue": pdu1energycostsValue,
       "pdu1currentValue": pdu1currentValue,
       "pdu1voltageValue": pdu1voltageValue,
       "pdu1powerfactorValue": pdu1powerfactorValue,
       "pdu1frequencyValue": pdu1frequencyValue,
       "pdu1VoltageFlicker": pdu1VoltageFlicker,
       "pdu1VoltageFlickerValue": pdu1VoltageFlickerValue,
       "pdu1VoltageFlickerTime": pdu1VoltageFlickerTime,
       "pdu1VoltageFlickerState": pdu1VoltageFlickerState,
       "pdu1VoltageSwell": pdu1VoltageSwell,
       "pdu1VoltageSwellValue": pdu1VoltageSwellValue,
       "pdu1VoltageSwellTime": pdu1VoltageSwellTime,
       "pdu1VoltageSwellState": pdu1VoltageSwellState,
       "pdu1VoltagePeak": pdu1VoltagePeak,
       "pdu1VoltagePeakValue": pdu1VoltagePeakValue,
       "pdu1VoltagePeakTime": pdu1VoltagePeakTime,
       "pdu1VoltagePeakState": pdu1VoltagePeakState,
       "pdu2": pdu2,
       "pdu2activepowerValue": pdu2activepowerValue,
       "pdu2apparentpowerValue": pdu2apparentpowerValue,
       "pdu2energyValue": pdu2energyValue,
       "pdu2energycostsValue": pdu2energycostsValue,
       "pdu2currentValue": pdu2currentValue,
       "pdu2voltageValue": pdu2voltageValue,
       "pdu2powerfactorValue": pdu2powerfactorValue,
       "pdu2frequencyValue": pdu2frequencyValue,
       "pdu2VoltageFlicker": pdu2VoltageFlicker,
       "pdu2VoltageFlickerValue": pdu2VoltageFlickerValue,
       "pdu2VoltageFlickerTime": pdu2VoltageFlickerTime,
       "pdu2VoltageFlickerState": pdu2VoltageFlickerState,
       "pdu2VoltageSwell": pdu2VoltageSwell,
       "pdu2VoltageSwellValue": pdu2VoltageSwellValue,
       "pdu2VoltageSwellTime": pdu2VoltageSwellTime,
       "pdu2VoltageSwellState": pdu2VoltageSwellState,
       "pdu2VoltagePeak": pdu2VoltagePeak,
       "pdu2VoltagePeakValue": pdu2VoltagePeakValue,
       "pdu2VoltagePeakTime": pdu2VoltagePeakTime,
       "pdu2VoltagePeakState": pdu2VoltagePeakState,
       "pdusum": pdusum,
       "pdusumactivepowerValue": pdusumactivepowerValue,
       "pdusumapparentpowerValue": pdusumapparentpowerValue,
       "pdusumenergyValue": pdusumenergyValue,
       "pdusumenergycostsValue": pdusumenergycostsValue,
       "pdusumcurrentValue": pdusumcurrentValue,
       "pdusumvoltageValue": pdusumvoltageValue,
       "pdusumpowerfactorValue": pdusumpowerfactorValue,
       "pdusumfrequencyValue": pdusumfrequencyValue,
       "alarmText": alarmText}
)
