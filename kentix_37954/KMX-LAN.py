# SNMP MIB module (KMX-LAN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kentix_37954/KMX-LAN.mib
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
_MultisensorLan_ObjectIdentity = ObjectIdentity
multisensorLan = _MultisensorLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2)
)
_Datapoints_ObjectIdentity = ObjectIdentity
datapoints = _Datapoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1)
)
_TemperatureEntry_ObjectIdentity = ObjectIdentity
temperatureEntry = _TemperatureEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 1, 4),
    _TemperatureAlarm_Type()
)
temperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureAlarm.setStatus("mandatory")
_TemperatureAlarmtext_Type = DisplayString
_TemperatureAlarmtext_Object = MibScalar
temperatureAlarmtext = _TemperatureAlarmtext_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 1, 6),
    _TemperatureAlarmArm_Type()
)
temperatureAlarmArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureAlarmArm.setStatus("mandatory")
_HumidityEntry_ObjectIdentity = ObjectIdentity
humidityEntry = _HumidityEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 2, 4),
    _HumidityAlarm_Type()
)
humidityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityAlarm.setStatus("mandatory")
_HumidityAlarmtext_Type = DisplayString
_HumidityAlarmtext_Object = MibScalar
humidityAlarmtext = _HumidityAlarmtext_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 2, 6),
    _HumidityAlarmArm_Type()
)
humidityAlarmArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityAlarmArm.setStatus("mandatory")
_DewpointEntry_ObjectIdentity = ObjectIdentity
dewpointEntry = _DewpointEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 3, 3),
    _DewpointAlarm_Type()
)
dewpointAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpointAlarm.setStatus("mandatory")
_DewpointAlarmtext_Type = DisplayString
_DewpointAlarmtext_Object = MibScalar
dewpointAlarmtext = _DewpointAlarmtext_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 3, 4),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 3, 6),
    _DewpointAlarmArm_Type()
)
dewpointAlarmArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dewpointAlarmArm.setStatus("mandatory")
_CoEntry_ObjectIdentity = ObjectIdentity
coEntry = _CoEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 4)
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 4, 3),
    _CoAlarm_Type()
)
coAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coAlarm.setStatus("mandatory")
_CoAlarmtext_Type = DisplayString
_CoAlarmtext_Object = MibScalar
coAlarmtext = _CoAlarmtext_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 4, 4),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 4, 6),
    _CoAlarmArm_Type()
)
coAlarmArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coAlarmArm.setStatus("mandatory")
_MotionEntry_ObjectIdentity = ObjectIdentity
motionEntry = _MotionEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 5)
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 5, 3),
    _MotionAlarm_Type()
)
motionAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motionAlarm.setStatus("mandatory")
_MotionAlarmtext_Type = DisplayString
_MotionAlarmtext_Object = MibScalar
motionAlarmtext = _MotionAlarmtext_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 5, 6),
    _MotionAlarmArm_Type()
)
motionAlarmArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    motionAlarmArm.setStatus("mandatory")
_DigitalIn1_ObjectIdentity = ObjectIdentity
digitalIn1 = _DigitalIn1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 6)
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 6, 1),
    _DigitalIn1Value_Type()
)
digitalIn1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalIn1Value.setStatus("mandatory")
_DigitalIn1Name_Type = DisplayString
_DigitalIn1Name_Object = MibScalar
digitalIn1Name = _DigitalIn1Name_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 6, 2),
    _DigitalIn1Name_Type()
)
digitalIn1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalIn1Name.setStatus("mandatory")
_DigitalIn2_ObjectIdentity = ObjectIdentity
digitalIn2 = _DigitalIn2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 7)
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 7, 1),
    _DigitalIn2Value_Type()
)
digitalIn2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalIn2Value.setStatus("mandatory")
_DigitalIn2Name_Type = DisplayString
_DigitalIn2Name_Object = MibScalar
digitalIn2Name = _DigitalIn2Name_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 7, 2),
    _DigitalIn2Name_Type()
)
digitalIn2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalIn2Name.setStatus("mandatory")
_DigitalOut2_ObjectIdentity = ObjectIdentity
digitalOut2 = _DigitalOut2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 8)
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 8, 1),
    _DigitalOut2Value_Type()
)
digitalOut2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalOut2Value.setStatus("mandatory")
_BuzzerTime_ObjectIdentity = ObjectIdentity
buzzerTime = _BuzzerTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 9)
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 9, 1),
    _BuzzerTimeValue_Type()
)
buzzerTimeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buzzerTimeValue.setStatus("mandatory")
_RelayTime_ObjectIdentity = ObjectIdentity
relayTime = _RelayTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 10)
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 10, 1),
    _RelayTimeValue_Type()
)
relayTimeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayTimeValue.setStatus("mandatory")
_RearmMotion_ObjectIdentity = ObjectIdentity
rearmMotion = _RearmMotion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 11)
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
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 11, 1),
    _RearmMotionValue_Type()
)
rearmMotionValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rearmMotionValue.setStatus("mandatory")
_VibrationEntry_ObjectIdentity = ObjectIdentity
vibrationEntry = _VibrationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 12)
)


class _VibrationValue_Type(Integer32):
    """Custom type vibrationValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VibrationValue_Type.__name__ = "Integer32"
_VibrationValue_Object = MibScalar
vibrationValue = _VibrationValue_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 12, 1),
    _VibrationValue_Type()
)
vibrationValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationValue.setStatus("mandatory")


class _VibrationMax_Type(Integer32):
    """Custom type vibrationMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_VibrationMax_Type.__name__ = "Integer32"
_VibrationMax_Object = MibScalar
vibrationMax = _VibrationMax_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 12, 2),
    _VibrationMax_Type()
)
vibrationMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vibrationMax.setStatus("mandatory")


class _VibrationAlarm_Type(Integer32):
    """Custom type vibrationAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VibrationAlarm_Type.__name__ = "Integer32"
_VibrationAlarm_Object = MibScalar
vibrationAlarm = _VibrationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 12, 3),
    _VibrationAlarm_Type()
)
vibrationAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationAlarm.setStatus("mandatory")
_VibrationAlarmtext_Type = DisplayString
_VibrationAlarmtext_Object = MibScalar
vibrationAlarmtext = _VibrationAlarmtext_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 12, 4),
    _VibrationAlarmtext_Type()
)
vibrationAlarmtext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationAlarmtext.setStatus("mandatory")


class _VibrationAlarmArm_Type(Integer32):
    """Custom type vibrationAlarmArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VibrationAlarmArm_Type.__name__ = "Integer32"
_VibrationAlarmArm_Object = MibScalar
vibrationAlarmArm = _VibrationAlarmArm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 1, 12, 6),
    _VibrationAlarmArm_Type()
)
vibrationAlarmArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vibrationAlarmArm.setStatus("mandatory")
_AlarmText_Type = DisplayString
_AlarmText_Object = MibScalar
alarmText = _AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 37954, 2, 2),
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
    ("KMX-LAN", "alarmText")
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
    "KMX-LAN",
    **{"kentix": kentix,
       "wrongLogin": wrongLogin,
       "login": login,
       "alarm": alarm,
       "multisensorLan": multisensorLan,
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
       "vibrationEntry": vibrationEntry,
       "vibrationValue": vibrationValue,
       "vibrationMax": vibrationMax,
       "vibrationAlarm": vibrationAlarm,
       "vibrationAlarmtext": vibrationAlarmtext,
       "vibrationAlarmArm": vibrationAlarmArm,
       "alarmText": alarmText}
)
